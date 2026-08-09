#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DEPRECATED stub.

The synthetic T2 mock has been replaced by the real-data pipeline:

  python scripts/r1/r1_T2_real_pipeline.py

That script uses DESI DR2 multipoles (local Zenodo pack) and Cosmicflows-4
table2. It does not inject Gaussian mock fields.
"""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

REAL = Path(__file__).resolve().parent / "r1_T2_real_pipeline.py"


def main() -> int:
    print("r1_T2_mock_pipeline.py is retired. Running real-data T2 instead:")
    print(" ", REAL)
    if not REAL.is_file():
        print("ERROR: real pipeline missing", REAL)
        return 2
    sys.argv = [str(REAL)] + sys.argv[1:]
    runpy.run_path(str(REAL), run_name="__main__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
