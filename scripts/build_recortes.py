#!/usr/bin/env python3
"""Year files for filtered downloads. Chapter ZIP and country ZIP stay apart."""

from __future__ import annotations

import csv
import gzip
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "datos" / "recortes"
OLAP_DIR = ROOT / "datos" / "olap_bcmm_mensual2023"
MTRA = ROOT / "datos/mensual_mtra/conjunto_de_datos/bcmm_mtra_capitulo_mensual_tr_cifra_2012_2026.csv"
PAISES = [
    ROOT / "datos/mensual_paises_bien/conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2015_2022.csv",
    ROOT / "datos/mensual_paises_bien/conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2023_2025.csv",
    ROOT / "datos/mensual_paises_bien/conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2026.csv",
]
PAIS_CAT = ROOT / "datos/mensual_paises_bien/catalogos/tc_pais.csv"
CUBE = "https://www.inegi.org.mx/sistemas/Olap/Proyectos/bd/continuas/comex/comex_bcmm_mensual2023.asp"
ZIP_MTRA = "https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_mensual_mtra_csv.zip"
ZIP_PAIS = "https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_mensual_paises_bien_csv.zip"
CAP_RE = re.compile(r"^Capítulo (\d{2})\b")
FRAC_RE = re.compile(r"(\d{2})\.(\d{2})\.(\d{4})")


def write_csv(path: Path, header: list[str], rows: list[list[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def build_capitulo() -> dict:
    header = None
    by: dict[str, list[list[str]]] = defaultdict(list)
    names: dict[str, str] = {}
    with MTRA.open(encoding="utf-8", newline="") as f:
        r = csv.reader(f)
        header = next(r)
        idx = {h: i for i, h in enumerate(header)}
        i_anio, i_con = idx["ANIO"], idx["CONCEPTO"]
        for row in r:
            m = CAP_RE.match(row[i_con])
            if not m:
                continue
            names[m.group(1)] = row[i_con]
            by[row[i_anio]].append(row)
    for year, rows in by.items():
        write_csv(OUT / "capitulo_millones" / f"{year}.csv", header, rows)
    return {
        "unidad": "millones de dólares FOB",
        "fuente": ZIP_MTRA,
        "forma": "ZIP oficial · solo filas de capítulo (no es país)",
        "archivo": "datos/recortes/capitulo_millones/{anio}.csv",
        "columna": "CONCEPTO",
        "anios": sorted(by),
        "capitulos": [{"id": c, "nombre": names[c]} for c in sorted(names)],
    }


def build_pais() -> dict:
    names = {}
    with PAIS_CAT.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            names[row["PAIS_O_D"].strip()] = row["PAIS_INEGI"].strip()
    header = None
    by: dict[str, list[list[str]]] = defaultdict(list)
    codes: set[str] = set()
    for path in PAISES:
        with path.open(encoding="utf-8", newline="") as f:
            r = csv.reader(f)
            header = next(r)
            idx = {h: i for i, h in enumerate(header)}
            i_anio, i_pais = idx["ANIO"], idx["PAIS_O_D"]
            for row in r:
                code = (row[i_pais] or "").strip()
                if not code:
                    continue
                codes.add(code)
                by[row[i_anio]].append(row)
    for year, rows in by.items():
        write_csv(OUT / "pais_miles" / f"{year}.csv", header, rows)
    return {
        "unidad": "miles de dólares FOB",
        "fuente": ZIP_PAIS,
        "forma": "ZIP oficial · solo filas con país (no es capítulo)",
        "archivo": "datos/recortes/pais_miles/{anio}.csv",
        "columna": "PAIS_O_D",
        "anios": sorted(by),
        "paises": [{"id": c, "nombre": names.get(c, c)} for c in sorted(codes)],
    }


def build_olap() -> dict:
    header = ["anio", "mes", "tipo_operacion", "pais", "capitulo", "fraccion", "valor_usd_fob", "cantidad"]
    by: dict[str, list[list[str]]] = defaultdict(list)
    caps: set[str] = set()
    paises: set[str] = set()
    for path in sorted(OLAP_DIR.glob("olap_*_tipo_pais_fraccion.csv")):
        print("olap", path.name, flush=True)
        year, month = path.name[5:9], path.name[10:12]
        raw = path.read_bytes().decode("iso-8859-1")
        for ln in raw.splitlines():
            s = ln.lstrip()
            if not (s.startswith("Importaciones") or s.startswith("Exportaciones")):
                continue
            rec = next(csv.reader([s]))
            if len(rec) < 4:
                continue
            tipo, pais, tarifa = rec[0].strip(), rec[1].strip(), rec[2].strip()
            valor = rec[3].strip() if len(rec) > 3 else ""
            cant = rec[4].strip() if len(rec) > 4 else ""
            m = FRAC_RE.search(tarifa)
            cap = m.group(1) if m else ""
            frac = (m.group(1) + m.group(2) + m.group(3)) if m else ""
            if cap:
                caps.add(cap)
            if pais:
                paises.add(pais)
            by[year].append([year, month, tipo, pais, cap, frac, valor, cant])
    OUT.joinpath("olap_dolares").mkdir(parents=True, exist_ok=True)
    for year, rows in by.items():
        dest = OUT / "olap_dolares" / f"{year}.csv.gz"
        with gzip.open(dest, "wt", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows(rows)
        print("wrote", dest, dest.stat().st_size, "rows", len(rows), flush=True)
    return {
        "unidad": "dólares FOB",
        "fuente": CUBE,
        "forma": "extracto de cubo · tipo × país × fracción",
        "archivo": "datos/recortes/olap_dolares/{anio}.csv.gz",
        "anios": sorted(by),
        "capitulos": sorted(caps),
        "paises": sorted(paises),
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    print("capítulo…", flush=True)
    cap = build_capitulo()
    print("país…", flush=True)
    pais = build_pais()
    print("olap…", flush=True)
    olap = build_olap()
    catalog = {
        "consulta": "2026-10-04",
        "aviso": (
            "Capítulo (millones de dólares FOB) y país (miles de dólares FOB) "
            "son cortes distintos. No se inventa un cruce capítulo × país a "
            "partir de esos ZIP. El cruce real es el extracto OLAP (dólares FOB)."
        ),
        "capitulo": cap,
        "pais": pais,
        "olap": olap,
    }
    (OUT / "catalogo.json").write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
