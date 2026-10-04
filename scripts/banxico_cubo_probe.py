#!/usr/bin/env python3
"""Probe Banxico Cubo de Comercio Exterior for a complete non-Excel export."""

from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

UA = "cubos-mx extract (public pages; contact via GitHub Rentheria/cubos-mx)"
PAGES = [
    "https://www.banxico.org.mx/CuboComercioExterior/",
    "https://www.banxico.org.mx/CuboComercioExterior/ValorDolares/inicio",
    "https://www.banxico.org.mx/CuboComercioExterior/ValorDolaresAnual/inicio",
    "https://www.banxico.org.mx/CuboComercioExterior/ValorDolares/seriesproducto",
    "https://tablero.banxico.org.mx/no-shell/embed.js",
]
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "datos" / "banxico_cubo"


def fetch(url: str) -> tuple[int, str, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.headers.get("Content-Type", ""), r.read()
    except Exception as e:
        return 0, str(e), b""


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    report = {"consulta": "2026-10-03", "paginas": []}
    js_urls = []
    for url in PAGES:
        status, ctype, raw = fetch(url)
        text = raw.decode("utf-8", errors="replace")
        entry = {
            "url": url,
            "http": status,
            "content_type": ctype,
            "bytes": len(raw),
            "csv_links": re.findall(r'https?://[^"\']+\.csv[^"\']*', text, re.I),
            "zip_links": re.findall(r'https?://[^"\']+\.zip[^"\']*', text, re.I),
            "api_like": sorted(
                set(
                    re.findall(
                        r'https?://[^"\']+(?:api|odata|export|download|csv)[^"\']*',
                        text,
                        re.I,
                    )
                )
            )[:40],
        }
        js_urls.extend(re.findall(r'src=["\']([^"\']+\.js[^"\']*)["\']', text, re.I))
        report["paginas"].append(entry)
        print(url, status, ctype, len(raw), "csv", entry["csv_links"][:3], flush=True)

    # follow embed script hosts
    extra = []
    for u in js_urls:
        if u.startswith("//"):
            u = "https:" + u
        elif u.startswith("/"):
            u = "https://www.banxico.org.mx" + u
        extra.append(u)
    report["scripts"] = sorted(set(extra))[:60]

    # common Qlik/PowerBI/tableau endpoints near the embed
    guesses = [
        "https://tablero.banxico.org.mx/",
        "https://tablero.banxico.org.mx/no-shell/",
        "https://www.banxico.org.mx/CuboComercioExterior/ValorDolares/export",
        "https://www.banxico.org.mx/CuboComercioExterior/ValorDolares/csv",
        "https://www.banxico.org.mx/SieAPIRest/service/v1/",
    ]
    report["sondeos"] = []
    for url in guesses:
        status, ctype, raw = fetch(url)
        report["sondeos"].append(
            {
                "url": url,
                "http": status,
                "content_type": ctype,
                "bytes": len(raw),
                "head": raw[:160].decode("utf-8", errors="replace"),
            }
        )
        print("guess", url, status, ctype, len(raw), flush=True)

    (OUT / "probe.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
