#!/usr/bin/env python3
"""Download 4096 s O3 H1+L1 open strain (GW190521 window) from GWOSC."""

from __future__ import annotations

import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "gw_public" / "o3"
BASE = "https://gwosc.org/eventapi/json/GWTC-2.1-confident/GW190521/v4"
FILES = [
    "H-H1_GWOSC_4KHZ_R1-1242440920-4096.hdf5",
    "L-L1_GWOSC_4KHZ_R1-1242440920-4096.hdf5",
]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        dest = OUT / name
        if dest.exists() and dest.stat().st_size > 1_000_000:
            print("have", name, dest.stat().st_size)
            continue
        url = f"{BASE}/{name}"
        print("GET", name)
        with urllib.request.urlopen(url, timeout=600) as r:
            dest.write_bytes(r.read())
        print(" ->", dest.stat().st_size)
    print("done", OUT)


if __name__ == "__main__":
    main()
