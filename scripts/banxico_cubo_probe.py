#!/usr/bin/env python3
"""Probe Banxico Cubo de Comercio Exterior for a complete official dump.

Records exact HTTP, Content-Type, bytes and response head.
Does not scrape the tablero chapter by chapter.
Does not write a truncated Excel.
"""

from __future__ import annotations

import json
import re
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

UA = "cubos-mx extract (public pages; contact via GitHub Rentheria/cubos-mx)"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "datos" / "banxico_cubo"
CTX = ssl.create_default_context()

URLS = [
    "https://www.banxico.org.mx/CuboComercioExterior/",
    "https://www.banxico.org.mx/CuboComercioExterior/ValorDolares/inicio",
    "https://www.banxico.org.mx/CuboComercioExterior/ValorDolaresAnual/inicio",
    "https://www.banxico.org.mx/CuboComercioExterior/ValorDolares/seriesproducto",
    "https://www.banxico.org.mx/CuboComercioExterior/ValorDolares/matrizprodregion",
    "https://www.banxico.org.mx/CuboComercioExterior/Volumen/inicio",
    "https://www.banxico.org.mx/CuboComercioExterior/Volumen/seriesproducto",
    "https://www.banxico.org.mx/CuboComercioExterior/ValorDolares/export",
    "https://www.banxico.org.mx/CuboComercioExterior/ValorDolares/csv",
    "https://www.banxico.org.mx/CuboComercioExterior/datos.csv",
    "https://www.banxico.org.mx/CuboComercioExterior/datos.zip",
    "https://www.banxico.org.mx/CuboComercioExterior/cubo.csv",
    "https://www.banxico.org.mx/CuboComercioExterior/cubo.zip",
    "https://www.banxico.org.mx/DataSetsWeb/?idioma=es",
    "https://www.banxico.org.mx/DataSetsWeb/dataset?ruta=Cubo&idioma=es",
    "https://www.banxico.org.mx/DataSetsWeb/dataset?ruta=Balanza&idioma=es",
    "https://www.banxico.org.mx/DataSetsWeb/dataset?ruta=MLL&idioma=es",
    "https://www.banxico.org.mx/DataSetsWeb/cubo",
    "https://tablero.banxico.org.mx/",
    "https://tablero.banxico.org.mx/no-shell/",
    "https://tablero.banxico.org.mx/no-shell/embed.js",
    "https://tablero.banxico.org.mx/API/auth/login",
    "https://tablero.banxico.org.mx/API3/authentication/authenticateUserEmbed",
    "https://tablero.banxico.org.mx/API/export",
    "https://www.banxico.org.mx/SieAPIRest/service/v1/",
    "https://www.snice.gob.mx/cs/avi/snice/fuentesestadisticas.html",
]


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    rec: dict = {
        "url": url,
        "http": 0,
        "content_type": "",
        "bytes": 0,
        "head": "",
        "disposition": "",
        "csv_hrefs": [],
        "file_hrefs": [],
        "pk": False,
    }
    try:
        with urllib.request.urlopen(req, timeout=45, context=CTX) as r:
            raw = r.read()
            rec["http"] = r.status
            rec["content_type"] = r.headers.get("Content-Type", "")
            rec["disposition"] = r.headers.get("Content-Disposition", "")
            rec["final_url"] = r.geturl()
            rec["bytes"] = len(raw)
            rec["head"] = raw[:240].decode("utf-8", errors="replace")
            rec["pk"] = raw[:4] == b"PK\x03\x04"
            if "html" in rec["content_type"].lower():
                text = raw.decode("utf-8", errors="replace")
                hrefs = re.findall(r'href=["\']([^"\']+)["\']', text, re.I)
                rec["csv_hrefs"] = [h for h in hrefs if re.search(r"\.(csv|zip)(\?|$)", h, re.I)]
                rec["file_hrefs"] = [
                    h for h in hrefs if re.search(r"\.(csv|zip|xlsx|xls)(\?|$)", h, re.I)
                ]
    except urllib.error.HTTPError as e:
        raw = e.read() if e.fp else b""
        rec["http"] = e.code
        rec["content_type"] = e.headers.get("Content-Type", "") if e.headers else ""
        rec["bytes"] = len(raw)
        rec["head"] = raw[:240].decode("utf-8", errors="replace")
        rec["error"] = f"HTTP Error {e.code}: {e.reason}"
    except Exception as e:
        rec["error"] = f"{type(e).__name__}: {e}"
    print(f"{rec['http']:>4} {rec['bytes']:>8} {url}", flush=True)
    return rec


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    hits = [fetch(url) for url in URLS]
    report = {
        "consulta": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ua": UA,
        "complete_file_found": any(h.get("pk") or (h.get("http") == 200 and h.get("csv_hrefs")) for h in hits if "CuboComercioExterior" in h["url"]),
        "hits": hits,
    }
    (OUT / "probe.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("complete_file_found", report["complete_file_found"], flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
