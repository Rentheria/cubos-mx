#!/usr/bin/env python3
"""Export every month of COMEX_BCMM_MENSUAL_2023 as official CSV.

A month is written only when the exported data rows equal Actualiza Cant_Fil.
"""

from __future__ import annotations

import csv
import io
import json
import sys
from pathlib import Path

from olap_bcmm_extract import (
    CUBE_PAGE,
    OUT,
    Client,
    actualiza,
    write_manifest,
)

FMT = "Texto separado por comas(.csv)"
ROWS = (
    "crossjoin(crossjoin("
    "{[Tipo operación].[Tipo operación].[Total].Children}, "
    "{[País].[País].[Total].Children}), "
    "Descendants([Tarifa].[Tarifa].[Total], 4))"
)
NOMF = "Tipo operación|País|Tarifa"


def months() -> list[tuple[int, int]]:
    out = []
    for y in (2023, 2024, 2025):
        for m in range(1, 13):
            out.append((y, m))
    for m in range(1, 8):
        out.append((2026, m))
    return out


def count_data_rows(raw: bytes) -> int:
    text = raw.decode("iso-8859-1", errors="replace")
    n = 0
    buf = False
    for ln in text.splitlines():
        s = ln.lstrip()
        if s.startswith("Importaciones") or s.startswith("Exportaciones"):
            n += 1
            buf = True
        elif not ln.strip():
            buf = False
    return n


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    client = Client()
    print("open…", flush=True)
    client.open_default()
    index = []
    for year, month in months():
        name = f"olap_{year}_{month:02d}_tipo_pais_fraccion"
        csv_path = OUT / f"{name}.csv"
        if csv_path.exists() and csv_path.stat().st_size > 1000:
            print(f"skip existing {name}", flush=True)
            continue
        where = {
            "Where_Tarifa": "[Tarifa].[Tarifa].[Total]",
            "Where_País": "[País].[País].[Total]",
            "Where_Tipo operación": "[Tipo operación].[Tipo operación].[Total]",
            "Where_Año": f"[Año].[ID FECHA REGISTRO].&[{year}]",
            "Where_Mes": f"[Mes].[Mes].[DES MES].&[{month}]",
            "C_Where_Año": f"[Año].[ID FECHA REGISTRO].&[{year}]",
            "C_Where_Mes": f"[Mes].[Mes].[DES MES].&[{month}]",
            "C_Where_Tipo moneda": "[Tipo moneda].[ID TIPO MONEDA].&[1]",
        }
        print(f"query {name}…", flush=True)
        html = client.run_mdx(ROWS, NOMF, where)
        act = actualiza(html)
        print(f"  Actualiza {act}", flush=True)
        if not act:
            (OUT / "STOP.md").write_text(
                f"{name}: no Actualiza() after MDX. Stopped.\n", encoding="utf-8"
            )
            return 3
        cant_fil, num_fil = act
        ctype, raw = client.try_export(FMT)
        looks_html = raw.lstrip().lower().startswith(b"<") or b"error acumulado" in raw.lower()
        if looks_html:
            print("  export HTML, retry once…", flush=True)
            html = client.run_mdx(ROWS, NOMF, where)
            act = actualiza(html)
            ctype, raw = client.try_export(FMT)
            looks_html = raw.lstrip().lower().startswith(b"<") or b"error acumulado" in raw.lower()
        n = 0 if looks_html else count_data_rows(raw)
        print(f"  export {len(raw)} B rows={n} html={looks_html}", flush=True)
        if looks_html:
            note = (
                f"{name}: exporta.aspx returned HTML ({len(raw)} B), "
                f"Cant_Fil={cant_fil}. No CSV for this month.\n"
            )
            (OUT / "STOP.md").write_text(note, encoding="utf-8")
            print("  STOP", note.strip(), flush=True)
            continue
        if n != cant_fil:
            note = (
                f"{name}: exported data rows={n}, Actualiza Cant_Fil={cant_fil}. "
                "Mismatch. File not published as complete.\n"
            )
            (OUT / "STOP.md").write_text(note, encoding="utf-8")
            (OUT / f"{name}.INCOMPLETE.bin").write_bytes(raw)
            print("  STOP", note.strip(), flush=True)
            continue
        csv_path.write_bytes(raw)
        meta = {
            "consulta": "2026-10-03",
            "url": CUBE_PAGE,
            "cube": "COMEX_BCMM_MENSUAL_2023",
            "periodo": f"{year}-{month:02d}",
            "unidad": "dólares FOB",
            "cruce": "tipo_operacion × país × fracción (8 dígitos; el capítulo es el prefijo)",
            "cant_fil": cant_fil,
            "filas_datos": n,
            "export_bytes": len(raw),
            "completo_del_mes": True,
            "archivo": csv_path.name,
        }
        write_manifest(OUT / f"{name}.json", meta)
        index.append(meta)
        if len(raw) >= 100 * 1024 * 1024:
            print("  >=100 MB — leave out of git", flush=True)
    (OUT / "indice.json").write_text(
        json.dumps(
            {
                "consulta": "2026-10-03",
                "url": CUBE_PAGE,
                "meses": index,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    raise SystemExit(main())
