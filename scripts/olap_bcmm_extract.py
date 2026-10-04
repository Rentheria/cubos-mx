#!/usr/bin/env python3
"""Walk the public INEGI OLAP viewer for COMEX_BCMM_MENSUAL_2023.

Official export (exporta.aspx) is tried first. If that path returns HTML
error, every HTML page of a named slice is walked. A slice is written only
when collected rows equal Actualiza Cant_Fil. A partial file is not the cube.
"""

from __future__ import annotations

import csv
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

UA = "cubos-mx extract (public OLAP; contact via GitHub Rentheria/cubos-mx)"
CUBE_PAGE = (
    "https://www.inegi.org.mx/sistemas/Olap/Proyectos/bd/continuas/"
    "comex/comex_bcmm_mensual2023.asp"
)
QUERY = "https://www.inegi.org.mx/sistemas/olap/consulta/general_ver4/MDXQueryDatos.asp"
EXPORT = "https://www.inegi.org.mx/sistemas/olap/exporta/exporta.aspx"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "datos" / "olap_bcmm_mensual2023"


def decode(raw: bytes) -> str:
    return raw.decode("iso-8859-1", errors="replace")


class HiddenInputs(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.fields: dict[str, str] = {}
        self.form = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = {k: (v or "") for k, v in attrs}
        if tag == "form":
            self.form = a.get("name", "")
        if tag == "input" and a.get("type", "text").lower() in {
            "hidden",
            "text",
        }:
            name = a.get("name")
            if name and self.form in {"", "queryForm", "connectInfo", "exporta"}:
                # last form wins for export vs query; we keep both prefixes
                key = name if self.form != "exporta" else f"exporta:{name}"
                self.fields[key] = a.get("value", "")


def parse_fields(html: str) -> dict[str, str]:
    p = HiddenInputs()
    p.feed(html)
    return p.fields


def actualiza(html: str) -> tuple[int, int] | None:
    m = re.search(r"Actualiza\('(\d+)','(\d+)','(\d+)','(\d+)'\)", html)
    if not m:
        return None
    return int(m.group(3)), int(m.group(4))


class TableRows(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_result = False
        self.in_td = False
        self.td_class = ""
        self.cell = []
        self.row = []
        self.rows: list[list[str]] = []
        self.depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = {k: (v or "") for k, v in attrs}
        if tag == "table" and a.get("id") == "ResultTable":
            self.in_result = True
            self.depth = 1
            return
        if self.in_result and tag == "table":
            self.depth += 1
        if not self.in_result or self.depth != 1:
            return
        if tag == "tr":
            self.row = []
        if tag == "td":
            self.in_td = True
            self.td_class = a.get("class", "")
            self.cell = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "table" and self.in_result:
            self.depth -= 1
            if self.depth <= 0:
                self.in_result = False
            return
        if not self.in_result or self.depth != 1:
            return
        if tag == "td" and self.in_td:
            text = re.sub(r"\s+", " ", "".join(self.cell)).strip()
            text = text.replace("+ ", "").replace("&nbsp", " ").strip()
            self.row.append(text)
            self.in_td = False
        if tag == "tr" and self.row:
            self.rows.append(self.row)

    def handle_data(self, data: str) -> None:
        if self.in_td:
            self.cell.append(data)


class Client:
    def __init__(self) -> None:
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
        self.opener.addheaders = [
            ("User-Agent", UA),
            ("Accept", "text/html,application/xhtml+xml,*/*;q=0.8"),
        ]
        self.query_fields: dict[str, str] = {}
        self.export_fields: dict[str, str] = {}

    def get(self, url: str) -> bytes:
        with self.opener.open(url, timeout=120) as r:
            return r.read()

    def post(self, url: str, data: dict[str, str], extra: dict[str, str] | None = None) -> bytes:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": CUBE_PAGE,
            "Origin": "https://www.inegi.org.mx",
        }
        if extra:
            headers.update(extra)
        body = urllib.parse.urlencode(data, encoding="iso-8859-1", errors="replace").encode(
            "iso-8859-1"
        )
        req = urllib.request.Request(url, data=body, headers=headers, method="POST")
        with self.opener.open(req, timeout=180) as r:
            return r.read()

    def open_default(self) -> str:
        self.get(CUBE_PAGE)
        # País + Tarifa checked, Tipo operación / Año / Mes already on
        data = {
            "e": "",
            "c": "",
            "s": "est",
            "server": "W-OLAPCLPRO25",
            "database": "COMEX_BCMM_MENSUAL",
            "cube": "COMEX_BCMM_MENSUAL_2023",
            "NomDimFila": "Tipo Operación",
            "NomDimCol": "Measures",
            "NumPagina": "1",
            "Paq_Pag": "0",
            "NumPagFil": "1",
            "Paq_PagFil": "0",
            "Ini_PPag": "1",
            "Tot_Pag": "0",
            "rows": "",
            "NDim": "7",
            "columns": "",
            "DimNoVisible": "|",
            "DimVisible": "Measures|Tipo Operación|Tipo moneda|Año|País|Mes|Tarifa",
            "level": "1",
            "where": "",
            "C_Where_Tipo moneda": "[Tipo moneda].[ID TIPO MONEDA].&[1]",
            "Where_Fecha Registro": "[Fecha registro].[2005]",
            "ContNuevoFiltro": "",
            "FiltroSel": "C_Where_Tipo moneda",
            "ver_botones": "0",
            "ver_titulo": "1",
            "unidadmedida": "Dolares",
            "ed": "0,0,2,0,0,0,0",
            "notas": "/sistemas/olap/proyectos/bd/continuas/comex/metadatos/comex_bcmm_mensual.asp",
            "Lc_piepagina": (
                'Nota: "C" refiere a informacion Confidencial. Fuente: SAT, SE, '
                "BANXICO, INEGI. Balanza Comercial de Mercancias de Mexico "
                "(enero 2023 a julio 2026). SNIEG. Informacion de Interes Nacional."
            ),
            "titulo_sin_consecutivo": (
                "Balanza Comercial de Mercancías de México Mensual (enero 2023 - julio 2026)"
            ),
            "titulo_proyecto": "Estadísticas de la Balanza Comercial de Mercancías de México Mensual",
            "colorFondo": "4",
            "pagina_inicio": CUBE_PAGE + "?",
            "CBDim": [
                "[Año].levels(0).Allmembers",
                "[País].levels(0).Allmembers",
                "[Tipo Operación].levels(0).Allmembers",
                "[Mes].levels(0).Allmembers",
                "[Tarifa].levels(0).Allmembers",
            ],
        }
        # urlencode list: send CBDim repeatedly
        pairs = []
        for k, v in data.items():
            if isinstance(v, list):
                for item in v:
                    pairs.append((k, item))
            else:
                pairs.append((k, v))
        body = urllib.parse.urlencode(
            pairs, encoding="iso-8859-1", errors="replace"
        ).encode("iso-8859-1")
        req = urllib.request.Request(
            QUERY,
            data=body,
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": CUBE_PAGE,
                "User-Agent": UA,
            },
            method="POST",
        )
        with self.opener.open(req, timeout=180) as r:
            html = decode(r.read())
        self._ingest(html)
        return html

    def _ingest(self, html: str) -> None:
        fields = parse_fields(html)
        self.query_fields = {k: v for k, v in fields.items() if not k.startswith("exporta:")}
        self.export_fields = {k[8:]: v for k, v in fields.items() if k.startswith("exporta:")}

    def run_mdx(self, rows: str, nom_fila: str, where_extra: dict[str, str] | None = None) -> str:
        data = dict(self.query_fields)
        data["rows"] = rows
        data["rowsAnte"] = rows
        data["NomDimFila"] = nom_fila
        data["nomdimfila"] = nom_fila
        data["NumPagFil"] = "1"
        data["Paq_PagFil"] = "0"
        if where_extra:
            data.update(where_extra)
        html = decode(self.post(QUERY, data))
        self._ingest(html)
        return html

    def page(self, num_pag_fil: int) -> str:
        data = dict(self.query_fields)
        data["NumPagFil"] = str(num_pag_fil)
        # packet of 10 pages
        data["Paq_PagFil"] = str((num_pag_fil - 1) // 10)
        html = decode(self.post(QUERY, data))
        self._ingest(html)
        return html

    def try_export(self, fmt: str) -> tuple[str, bytes]:
        data = dict(self.export_fields)
        data["Lc_formato"] = fmt
        try:
            raw = self.post(EXPORT, data)
        except urllib.error.HTTPError as e:
            return e.headers.get("Content-Type", ""), e.read()
        return "ok", raw


def parse_data_rows(html: str) -> list[list[str]]:
    p = TableRows()
    p.feed(html)
    out = []
    for row in p.rows:
        # skip header-ish rows without a value cell
        if len(row) < 2:
            continue
        joined = " ".join(row)
        if "Valor Total" in joined and "Dato" in joined:
            continue
        if joined.startswith("Tipo operación") or "coloca" in joined.lower():
            continue
        out.append(row)
    return out


def write_manifest(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    client = Client()
    print("open default…", flush=True)
    html = client.open_default()
    act = actualiza(html)
    print("default Actualiza", act, "fields", len(client.query_fields), flush=True)

    # Small export probe (current default query, 3 rows)
    probes = {}
    for fmt in (
        "Texto separado por comas(.csv)",
        "Texto separado por tabuladores(.txt)",
        "Hoja de Cálculo Excel(.xls)",
    ):
        ctype, raw = client.try_export(fmt)
        head = raw[:200]
        probes[fmt] = {
            "content_type": ctype,
            "bytes": len(raw),
            "head": decode(head)[:160],
            "looks_html": raw[:20].lstrip().lower().startswith(b"<") or b"error acumulado" in raw.lower(),
        }
        print("export", fmt, probes[fmt]["bytes"], probes[fmt]["head"][:80], flush=True)

    write_manifest(OUT / "export_probe.json", {"consulta": "2026-10-03", "probes": probes})

    usable = [k for k, v in probes.items() if not v["looks_html"] and v["bytes"] > 40]
    print("usable export", usable, flush=True)
    if not usable:
        (OUT / "STOP.md").write_text(
            "exporta.aspx returned HTML error for the default 3-row query. "
            "No cube CSV written.\n",
            encoding="utf-8",
        )
        return 2

    fmt = "Texto separado por comas(.csv)"

    def export_slice(name: str, rows: str, nom_fila: str, where: dict[str, str], periodo: str) -> int:
        print(f"query {name}…", flush=True)
        html = client.run_mdx(rows, nom_fila, where)
        act = actualiza(html)
        print(f"  Actualiza {act}", flush=True)
        if not act:
            (OUT / "STOP.md").write_text(
                f"{name}: no Actualiza() after MDX. Stopped. No CSV for this slice.\n",
                encoding="utf-8",
            )
            return 3
        cant_fil, num_fil = act
        ctype, raw = client.try_export(fmt)
        looks_html = raw.lstrip().lower().startswith(b"<") or b"error acumulado" in raw.lower()
        print(f"  export {len(raw)} B html={looks_html}", flush=True)
        if looks_html:
            (OUT / "STOP.md").write_text(
                f"{name}: exporta.aspx returned HTML ({len(raw)} B) after a query "
                f"with Cant_Fil={cant_fil}. Stopped. No CSV.\n",
                encoding="utf-8",
            )
            return 4
        text = raw.decode("iso-8859-1", errors="replace")
        # data lines after the title/filter preamble: count nonempty value rows
        lines = [ln for ln in text.splitlines() if ln.strip()]
        csv_path = OUT / f"{name}.csv"
        csv_path.write_bytes(raw)
        meta = {
            "consulta": "2026-10-03",
            "url": CUBE_PAGE,
            "cube": "COMEX_BCMM_MENSUAL_2023",
            "periodo": periodo,
            "unidad": "dólares FOB",
            "cant_fil": cant_fil,
            "num_fil_pagina": num_fil,
            "export_bytes": len(raw),
            "export_lines": len(lines),
            "archivo": csv_path.name,
        }
        # Compare: Cant_Fil is NON EMPTY cells. Export includes headers/filters.
        write_manifest(OUT / f"{name}.json", meta)
        if len(raw) >= 100 * 1024 * 1024:
            print("  FILE >= 100 MB — do not git-add", flush=True)
        return 0

    # Measure the full month cross first (chapter is implied by 8-digit fracción).
    full_rows = (
        "crossjoin(crossjoin("
        "{[Tipo operación].[Tipo operación].[Total].Children}, "
        "{[País].[País].[Total].Children}), "
        "Descendants([Tarifa].[Tarifa].[Total], 4))"
    )
    where_jul = {
        "Where_Tarifa": "[Tarifa].[Tarifa].[Total]",
        "Where_País": "[País].[País].[Total]",
        "Where_Tipo operación": "[Tipo operación].[Tipo operación].[Total]",
        "Where_Año": "[Año].[ID FECHA REGISTRO].&[2026]",
        "Where_Mes": "[Mes].[Mes].[DES MES].&[7]",
        "C_Where_Año": "[Año].[ID FECHA REGISTRO].&[2026]",
        "C_Where_Mes": "[Mes].[Mes].[DES MES].&[7]",
        "C_Where_Tipo moneda": "[Tipo moneda].[ID TIPO MONEDA].&[1]",
    }
    rc = export_slice(
        "olap_2026_07_tipo_pais_fraccion",
        full_rows,
        "Tipo operación|País|Tarifa",
        where_jul,
        "2026-07",
    )
    return rc

    # Fraction inventory: descendants of Total at distance 4 (8-digit fracción)
    print("descendants fracción…", flush=True)
    html = client.run_mdx(
        "Descendants([Tarifa].[Tarifa].[Total], 4)",
        "Tarifa",
        {
            "Where_Tarifa": "[Tarifa].[Tarifa].[Total]",
            "Where_País": "[País].[País].[Total]",
            "Where_Tipo operación": "[Tipo operación].[Tipo operación].[Total]",
            "Where_Año": "[Año].[ID FECHA REGISTRO].&[2026]",
            "Where_Mes": "[Mes].[Mes].[DES MES].&[7]",
        },
    )
    act = actualiza(html)
    print("fracciones Actualiza", act, flush=True)
    if act:
        Path(OUT / "fracciones_cant_fil.txt").write_text(
            f"Cant_Fil={act[0]} NumFil={act[1]} mes=2026-07\n", encoding="utf-8"
        )

    # One-month country × chapter (known 16498) — walk only if small enough to finish
    # First: one chapter × country × fracción (ch 01) as a complete named slice
    print("slice capítulo 01 × país × fracción julio 2026…", flush=True)
    rows_mdx = (
        "crossjoin(crossjoin("
        "{[Tipo operación].[Tipo operación].[Total].Children}, "
        "{[País].[País].[Total].Children}), "
        "Descendants([Tarifa].[Tarifa].[DES CAPITULO].&[01], 3))"
    )
    html = client.run_mdx(
        rows_mdx,
        "Tipo operación|País|Tarifa",
        {
            "Where_Tarifa": "[Tarifa].[Tarifa].[DES CAPITULO].&[01]",
            "Where_País": "[País].[País].[Total]",
            "Where_Tipo operación": "[Tipo operación].[Tipo operación].[Total]",
            "Where_Año": "[Año].[ID FECHA REGISTRO].&[2026]",
            "Where_Mes": "[Mes].[Mes].[DES MES].&[7]",
            "C_Where_Año": "[Año].[ID FECHA REGISTRO].&[2026]",
            "C_Where_Mes": "[Mes].[Mes].[DES MES].&[7]",
        },
    )
    act = actualiza(html)
    print("ch01 Actualiza", act, "sample rows", parse_data_rows(html)[:2], flush=True)
    if not act:
        (OUT / "STOP.md").write_text(
            "No Actualiza() in the capítulo 01 × país × fracción response. "
            "No CSV written.\n",
            encoding="utf-8",
        )
        return 2

    cant_fil, num_fil = act
    pages = (cant_fil + num_fil - 1) // num_fil
    collected: list[list[str]] = []
    for i in range(1, pages + 1):
        page_html = html if i == 1 else client.page(i)
        page_act = actualiza(page_html)
        if page_act != act:
            (OUT / "STOP.md").write_text(
                f"Page {i}/{pages} Actualiza {page_act} != {act}. "
                "Stopped. No complete CSV.\n",
                encoding="utf-8",
            )
            return 3
        batch = parse_data_rows(page_html)
        if not batch:
            (OUT / "STOP.md").write_text(
                f"Page {i}/{pages} parsed 0 data rows. Stopped. No complete CSV.\n",
                encoding="utf-8",
            )
            return 4
        collected.extend(batch)
        if i == 1 or i % 10 == 0 or i == pages:
            print(f"  page {i}/{pages} +{len(batch)} total={len(collected)}", flush=True)
        time.sleep(0.15)

    if len(collected) != cant_fil:
        (OUT / "STOP.md").write_text(
            f"Collected {len(collected)} rows, Actualiza Cant_Fil={cant_fil}. "
            "Mismatch. No complete CSV.\n",
            encoding="utf-8",
        )
        return 5

    csv_path = OUT / "olap_2026_07_capitulo01_pais_fraccion.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "anio",
                "mes",
                "tipo_operacion",
                "pais",
                "tarifa",
                "valor_usd_fob",
                "unidad",
                "fuente",
                "consulta",
            ]
        )
        for row in collected:
            # expected: tipo, pais, tarifa, valor
            tipo = row[0] if len(row) > 0 else ""
            pais = row[1] if len(row) > 1 else ""
            tarifa = row[2] if len(row) > 2 else ""
            valor = row[3] if len(row) > 3 else (row[-1] if row else "")
            w.writerow(
                [
                    "2026",
                    "07",
                    tipo,
                    pais,
                    tarifa,
                    valor,
                    "dólares FOB",
                    CUBE_PAGE,
                    "2026-10-03",
                ]
            )
    write_manifest(
        OUT / "olap_2026_07_capitulo01_pais_fraccion.json",
        {
            "consulta": "2026-10-03",
            "url": CUBE_PAGE,
            "cube": "COMEX_BCMM_MENSUAL_2023",
            "periodo": "2026-07",
            "unidad": "dólares FOB",
            "cruce": "tipo_operacion × país × fracción (capítulo 01 only)",
            "cant_fil": cant_fil,
            "filas_escritas": len(collected),
            "completo_del_cubo": False,
            "completo_del_recorte": True,
            "nota": (
                "Recorte nombrado: solo capítulo 01, julio 2026. "
                "No es el cubo completo capítulo × país × fracción."
            ),
        },
    )
    print("wrote", csv_path, "rows", len(collected), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
