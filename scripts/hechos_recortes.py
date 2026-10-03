#!/usr/bin/env python3
"""Hechos básicos de las tablas oficiales publicadas en datos/.

No junta capítulo con país. No mezcla millones con miles. Escribe hechos.json.
"""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATOS = ROOT / "datos"
OUT = ROOT / "hechos.json"

MODES = frozenset({"Aéreo", "Carretero", "Ferroviario", "Marítimo", "Otros modos"})
TOTALS = frozenset({"Exportación total", "Importación total"})


def fnum(s: str) -> float:
    return float(s) if s not in ("", None) else 0.0


def r_millones(x: float) -> float:
    return round(x, 3)


def r_miles(x: float) -> int:
    return int(round(x))


def ym_label(y: int, m: int) -> str:
    return f"{y:04d}-{m:02d}"


def months_in_year(periods: set[tuple[int, int]], year: int) -> int:
    return sum(1 for y, _m in periods if y == year)


def last_full_year(periods: set[tuple[int, int]]) -> int | None:
    years = sorted({y for y, _m in periods})
    full = [y for y in years if months_in_year(periods, y) == 12]
    return full[-1] if full else None


def analyze_capitulo(path: Path, total_label: str, tipo: str) -> dict:
    n = 0
    periods: set[tuple[int, int]] = set()
    official_year: dict[int, float] = defaultdict(float)
    official_month: dict[tuple[int, int], float] = defaultdict(float)
    chapters: dict[tuple[int, str], float] = defaultdict(float)
    unclassified: dict[int, float] = defaultdict(float)
    estatus: dict[int, set[str]] = defaultdict(set)
    latest = (0, 0)

    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("TIPO") != tipo:
                continue
            n += 1
            y, m = int(row["ANIO"]), int(row["MES"])
            periods.add((y, m))
            latest = max(latest, (y, m))
            estatus[y].add(row["ESTATUS"].rstrip("."))
            val = fnum(row["VAL_USD"])
            concepto = row["CONCEPTO"]
            if concepto == total_label:
                official_year[y] += val
                official_month[(y, m)] += val
            elif concepto.startswith("Capítulo"):
                chapters[(y, concepto)] += val
            elif concepto == "Productos no clasificados":
                unclassified[y] += val

    year = last_full_year(periods)
    if year is None:
        raise SystemExit(f"sin año calendario completo en {path.name}")
    by_chapter = {c: v for (y, c), v in chapters.items() if y == year}
    top_name, top_val = max(by_chapter.items(), key=lambda kv: kv[1])
    total = official_year[year]
    return {
        "archivo": path.name,
        "filas": n,
        "periodo": {
            "primero": ym_label(*min(periods)),
            "ultimo": ym_label(*max(periods)),
            "meses": len(periods),
        },
        "ultimo_mes": ym_label(*latest),
        "ultimo_mes_total_oficial": r_millones(official_month[latest]),
        "anio_calendario_completo": year,
        "estatus_anio_completo": sorted(estatus[year]),
        "estatus_ultimo_mes": sorted(estatus[latest[0]]),
        "total_oficial_anio": r_millones(total),
        "no_clasificados_anio": r_millones(unclassified[year]),
        "capitulo_mayor": {
            "concepto": top_name,
            "valor": r_millones(top_val),
            "participacion": round(top_val / total, 6),
        },
        "unidad": "millones de dólares FOB",
        "excluidas": [
            total_label,
            "filas de medio de transporte (Aéreo, Carretero, Ferroviario, Marítimo, Otros modos)",
        ],
    }


def analyze_pais(paths: list[Path], tipo: str) -> dict:
    n = 0
    periods: set[tuple[int, int]] = set()
    official_year: dict[int, float] = defaultdict(float)
    official_month: dict[tuple[int, int], float] = defaultdict(float)
    countries: dict[tuple[int, str], float] = defaultdict(float)
    estatus: dict[int, set[str]] = defaultdict(set)
    latest = (0, 0)

    for path in paths:
        with path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("TIPO") != tipo:
                    continue
                n += 1
                y, m = int(row["ANIO"]), int(row["MES"])
                periods.add((y, m))
                latest = max(latest, (y, m))
                estatus[y].add(row["ESTATUS"].rstrip("."))
                val = fnum(row["VAL_USD"])
                pais = row["PAIS_O_D"].strip()
                cont = row["CLAVE_CONTINENTE"].strip()
                reg = row["CLAVE_REGION"].strip()
                if pais == "" and cont == "" and reg == "":
                    official_year[y] += val
                    official_month[(y, m)] += val
                elif pais != "":
                    countries[(y, pais)] += val

    year = last_full_year(periods)
    if year is None:
        raise SystemExit("sin año calendario completo en las tablas de país")
    by_country = {p: v for (y, p), v in countries.items() if y == year}
    top_name, top_val = max(by_country.items(), key=lambda kv: kv[1])
    total = official_year[year]
    return {
        "archivos": [p.name for p in paths],
        "tipo": tipo,
        "filas": n,
        "periodo": {
            "primero": ym_label(*min(periods)),
            "ultimo": ym_label(*max(periods)),
            "meses": len(periods),
        },
        "ultimo_mes": ym_label(*latest),
        "ultimo_mes_total_oficial": r_miles(official_month[latest]),
        "anio_calendario_completo": year,
        "estatus_anio_completo": sorted(estatus[year]),
        "estatus_ultimo_mes": sorted(estatus[latest[0]]),
        "total_oficial_anio": r_miles(total),
        "paises_con_valor_anio": len(by_country),
        "pais_mayor": {
            "pais_o_d": top_name,
            "valor": r_miles(top_val),
            "participacion": round(top_val / total, 6),
        },
        "unidad": "miles de dólares",
        "excluidas": [
            "PAIS_O_D vacío (total nacional, de continente o de zona; volvería a contar)",
        ],
    }


def analyze_aduana(path: Path) -> dict:
    n = 0
    periods: set[tuple[int, int]] = set()
    official_year: dict[tuple[str, int], float] = defaultdict(float)
    official_month: dict[tuple[str, int, int], float] = defaultdict(float)
    offices: dict[tuple[str, int, str], float] = defaultdict(float)
    otras: dict[tuple[str, int], float] = defaultdict(float)
    estatus: dict[int, set[str]] = defaultdict(set)
    tipos: set[str] = set()
    latest = (0, 0)

    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            n += 1
            y, m = int(row["ANIO"]), int(row["MES"])
            periods.add((y, m))
            latest = max(latest, (y, m))
            estatus[y].add(row["ESTATUS"].rstrip("."))
            val = fnum(row["VAL_USD"])
            concepto = row["CONCEPTO"]
            tipo = row["TIPO"]
            tipos.add(tipo)
            if concepto in TOTALS:
                official_year[(tipo, y)] += val
                official_month[(tipo, y, m)] += val
            elif concepto in MODES:
                continue
            elif concepto == "Otras aduanas":
                otras[(tipo, y)] += val
            else:
                offices[(tipo, y, concepto)] += val

    year = last_full_year(periods)
    if year is None:
        raise SystemExit(f"sin año calendario completo en {path.name}")
    flujos = {}
    for tipo in sorted(tipos):
        by_office = {c: v for (t, y, c), v in offices.items() if t == tipo and y == year}
        top_name, top_val = max(by_office.items(), key=lambda kv: kv[1])
        total = official_year[(tipo, year)]
        flujos[tipo] = {
            "total_oficial_anio": r_millones(total),
            "otras_aduanas_anio": r_millones(otras[(tipo, year)]),
            "ultimo_mes_total_oficial": r_millones(
                official_month[(tipo, latest[0], latest[1])]
            ),
            "aduana_mayor": {
                "concepto": top_name,
                "valor": r_millones(top_val),
                "participacion": round(top_val / total, 6),
            },
        }
    return {
        "archivo": path.name,
        "filas": n,
        "periodo": {
            "primero": ym_label(*min(periods)),
            "ultimo": ym_label(*max(periods)),
            "meses": len(periods),
        },
        "ultimo_mes": ym_label(*latest),
        "anio_calendario_completo": year,
        "estatus_anio_completo": sorted(estatus[year]),
        "estatus_ultimo_mes": sorted(estatus[latest[0]]),
        "flujos": flujos,
        "unidad": "millones de dólares",
        "excluidas": [
            "Exportación total / Importación total",
            "filas de medio de transporte",
            "Otras aduanas (residual publicado, no es una aduana nombrada)",
        ],
    }


def main() -> None:
    hechos = {
        "metodo": (
            "Se sumó VAL_USD del último año calendario con 12 meses en la misma tabla oficial; "
            "el denominador es la fila de total oficial de ese archivo; "
            "se excluyeron subtotales que volverían a contar el mismo valor."
        ),
        "exportaciones_capitulo": analyze_capitulo(
            DATOS
            / "mensual_mtra/conjunto_de_datos/bcmm_mtra_capitulo_mensual_tr_cifra_2012_2026.csv",
            "Exportación total",
            "Exportación",
        ),
        "importaciones_capitulo": analyze_capitulo(
            DATOS
            / "mensual_mtra/conjunto_de_datos/bcmm_mtra_capitulo_mensual_tr_cifra_2012_2026.csv",
            "Importación total",
            "Importación",
        ),
        "exportaciones_pais": analyze_pais(
            [
                DATOS
                / "mensual_paises_bien/conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2015_2022.csv",
                DATOS
                / "mensual_paises_bien/conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2023_2025.csv",
                DATOS
                / "mensual_paises_bien/conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2026.csv",
            ],
            "Exportaciones",
        ),
        "importaciones_pais": analyze_pais(
            [
                DATOS
                / "mensual_paises_bien/conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2015_2022.csv",
                DATOS
                / "mensual_paises_bien/conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2023_2025.csv",
                DATOS
                / "mensual_paises_bien/conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2026.csv",
            ],
            "Importaciones",
        ),
        "aduana": analyze_aduana(
            DATOS
            / "mensual_mtra/conjunto_de_datos/bcmm_mtra_aduana_mensual_tr_cifra_2012_2026.csv"
        ),
    }
    OUT.write_text(
        json.dumps(hechos, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"escribió {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
