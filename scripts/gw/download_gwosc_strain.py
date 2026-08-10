#!/usr/bin/env python3
"""Download public LIGO strain for GW150914 from GWOSC (real interferometer data)."""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "gw_public"
EVENT_JSON = "https://gwosc.org/eventapi/json/GWTC-1-confident/GW150914/v3"
CATALOG = "https://gwosc.org/eventapi/json/GWTC-3-confident/"

# 4 kHz, 32 s around the event (public open data)
FILES = [
    "H-H1_GWOSC_4KHZ_R1-1126259447-32.hdf5",
    "L-L1_GWOSC_4KHZ_R1-1126259447-32.hdf5",
]


def fetch(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 1000:
        print(f"have {dest.name} ({dest.stat().st_size} bytes)")
        return
    print(f"GET {url}")
    with urllib.request.urlopen(url, timeout=120) as r:
        dest.write_bytes(r.read())
    print(f"  -> {dest} ({dest.stat().st_size} bytes)")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fetch(EVENT_JSON, OUT / "GW150914.json")
    fetch(CATALOG, OUT / "GWTC-3-confident.json")
    base = EVENT_JSON.rstrip("/")
    for name in FILES:
        fetch(f"{base}/{name}", OUT / name)
    meta = {
        "source": "GWOSC",
        "event": "GW150914",
        "reference": "https://doi.org/10.7935/82H3-HH23",
        "detectors": "H1 (Hanford), L1 (Livingston) — laser interferometers, ~3000 km baseline",
        "files": FILES,
        "note": "Tensor-channel open data. Not DESI residual sigma_X.",
    }
    (OUT / "PROVENANCE.json").write_text(json.dumps(meta, indent=2) + "\n")
    print("done", OUT)


if __name__ == "__main__":
    main()
