#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
External scale candidates vs NP-A ell_* and R_8.

Does NOT fit ell_*. Does NOT claim Virgo/Andromeda confirm the grain.
Records fractional distance so circular re-labels are obvious.

See papers/ell-star-external-scales.md
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from lib_verified import ell_mpc_for_sigma, r8_mpc  # noqa: E402

# Programme anchors (code)
ELL_NPA = ell_mpc_for_sigma(1e-5, 3)
ELL_DESI_D3 = ell_mpc_for_sigma(1.5e-4, 3)
R8 = r8_mpc()

# Literature / standard OOM anchors (not fitted)
# MW–M31: ~780 kpc (standard; e.g. Riess/van der Marel class OOM)
MW_AND = 0.78
# Virgo r200 / virial radius — range across studies (cite classes in note)
VIRGO_URBAN = 1.08
VIRGO_FERRARESE = 1.55
VIRGO_HOFFMAN = 1.80


def frac(a: float, b: float) -> float:
    return abs(a / b - 1.0)


def main() -> None:
    print("=== ell_* programme anchors (counting inverse, not derived) ===")
    print(f"  NP-A  d=3, σ=1e-5     ell_* = {ELL_NPA:.4f} Mpc")
    print(f"  DESI ceiling d=3      ell_* = {ELL_DESI_D3:.4f} Mpc")
    print(f"  R_8 = 8/h             R_8   = {R8:.4f} Mpc")
    print()
    print("=== External candidates (literature OOM) ===")
    print(f"{'name':<22} {'L [Mpc]':>10} {'vs NP-A':>10} {'vs R8':>10}  note")
    rows = [
        ("MW–Andromeda", MW_AND, "standard distance OOM"),
        ("Virgo Urban-class", VIRGO_URBAN, "r200 X-ray class ~1.08"),
        ("Virgo Ferrarese-class", VIRGO_FERRARESE, "often-cited ~1.55"),
        ("Virgo Hoffman-class", VIRGO_HOFFMAN, "older high ~1.8"),
        ("R8 (structure)", R8, "nonlinear scale anchor"),
        ("NP-A (self)", ELL_NPA, "CIRCULAR if re-labelled 'galaxy sep'"),
        ("DESI-ceil d=3 cell", ELL_DESI_D3, "near R8 (~6%); different σ row"),
    ]
    for name, L, note in rows:
        print(
            f"{name:<22} {L:10.4f} {frac(L, ELL_NPA):10.1%} {frac(L, R8):10.1%}  {note}"
        )
    print()
    print("Honesty:")
    print("  Andromeda / Virgo do NOT independently confirm NP-A ~2.06 Mpc.")
    print("  '2.01 Mpc galaxy separation' is NP-A rounded if no external source.")
    print("  Open kernel: principle for mesoscopic ell_* still ABSENT (declared).")
    print("  Even if ell_* is real: residual/slip window, not 9% H0 (see h0 toys).")
    print("See papers/ell-star-external-scales.md")


if __name__ == "__main__":
    main()
