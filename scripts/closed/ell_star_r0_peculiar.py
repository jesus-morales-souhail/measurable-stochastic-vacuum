#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NEW result: independent matter-clustering / velocity scales vs NP-A ell_*.

This is NOT a re-print of Andromeda/Virgo tables.
Uses published galaxy correlation lengths r0 and peculiar-velocity
coherence / bulk-flow scales from the literature (cited in the paper note).

Conversion: literature often quotes h^{-1} Mpc with h = H0/100.
Here H0=67.4 ⇒ h=0.674 (same fiducial as lib_verified).

Illegal: choose sample so r0 matches 2.06 Mpc after looking at NP-A.
Legal: quote standard L* / main-sample ranges and report fractional distance.

See papers/ell-star-r0-peculiar-scales.md
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import List, Tuple

ROOT = Path(__file__).resolve().parents[2]
_SCRIPTS = ROOT / "scripts"
for _d in (_SCRIPTS, _SCRIPTS / "core", _SCRIPTS / "r1", _SCRIPTS / "closed", _SCRIPTS / "side"):
    if _d.is_dir() and str(_d) not in sys.path:
        sys.path.insert(0, str(_d))

from lib_verified import H0_KM_S_MPC, ell_mpc_for_sigma, r8_mpc  # noqa: E402

H = H0_KM_S_MPC / 100.0  # 0.674
ELL_NPA = ell_mpc_for_sigma(1e-5, 3)
ELL_CEIL = ell_mpc_for_sigma(2.5e-2, 3)
R8 = r8_mpc()


def hinv_to_mpc(x_hinv: float) -> float:
    """Convert X h^{-1} Mpc → Mpc at programme h."""
    return x_hinv / H


def frac(a: float, b: float) -> float:
    return abs(a / b - 1.0)


# Published anchors (h^{-1} Mpc unless noted). Citations in paper note.
# Zehavi et al. SDSS: L* / main-sample class r0 ~ 5–6 h^{-1} Mpc (power-law ξ fits).
# See arXiv:1005.2413, astro-ph/0408569 — amplitude grows with L; L* class ~5–6.
R0_LSTAR_LO = 5.0   # h^{-1} Mpc
R0_LSTAR_HI = 6.0   # h^{-1} Mpc
# Brighter / redder samples can reach ~7–8 h^{-1} Mpc (same papers, luminosity trend)
R0_BRIGHT_HI = 8.0  # h^{-1} Mpc, upper illustrative for luminous samples

# Mean inter-galaxy separation for n ~ 0.01 h^3 Mpc^{-3} (order of L* abundance)
# n^{-1/3} = 0.01^{-1/3} h^{-1} Mpc ≈ 4.64 h^{-1} Mpc
N_STAR = 0.01  # h^3 Mpc^{-3}
N_INV3 = N_STAR ** (-1.0 / 3.0)

# Peculiar velocity: bulk-flow / coherence scales (literature OOM)
# Convergence / bulk-flow discussion often ~50–150 h^{-1} Mpc (Cosmicflows class)
# Not a single r0-like number — report as scale class FAR above NP-A
VPEC_COHERENCE_LO = 50.0   # h^{-1} Mpc
VPEC_COHERENCE_HI = 150.0  # h^{-1} Mpc


def main() -> None:
    print("=== NEW: r0 / peculiar-velocity scales vs NP-A (not Andromeda table) ===")
    print(f"  Fiducial h = {H:.3f}  (H0={H0_KM_S_MPC})")
    print(f"  NP-A ell_* (d=3,σ=1e-5) = {ELL_NPA:.4f} Mpc   [counting inverse ONLY]")
    print(f"  DESI-ceil ell_* (d=3)   = {ELL_CEIL:.4f} Mpc")
    print(f"  R_8                     = {R8:.4f} Mpc")
    print()

    print("--- Galaxy 2PCF correlation length r0 (ξ≈(r/r0)^{-γ}) ---")
    print("  Sources: Zehavi et al. SDSS class (arXiv:1005.2413, astro-ph/0408569)")
    print("  L* / main-sample power-law fits typically r0 ~ 5–6 h^{-1} Mpc")
    print(f"{'sample':<28} {'h^{-1}Mpc':>10} {'Mpc':>10} {'vs NP-A':>10} {'vs R8':>10}")
    rows: List[Tuple[str, float]] = [
        ("r0 L* low (5 h^{-1})", R0_LSTAR_LO),
        ("r0 L* high (6 h^{-1})", R0_LSTAR_HI),
        ("r0 luminous up (~8 h^{-1})", R0_BRIGHT_HI),
        ("n_*^{-1/3} (n=0.01 h^3)", N_INV3),
    ]
    for name, xh in rows:
        L = hinv_to_mpc(xh)
        print(
            f"{name:<28} {xh:10.2f} {L:10.2f} {frac(L, ELL_NPA):10.1%} {frac(L, R8):10.1%}"
        )
    print()

    print("--- Peculiar-velocity coherence / bulk-flow scale class ---")
    print("  Sources: Cosmicflows / bulk-flow reviews — coherence often tens–hundreds h^{-1} Mpc")
    print("  NOT a sharp r0; quoted as a RANGE, not a single match target")
    for name, xh in (
        ("v_pec coherence low", VPEC_COHERENCE_LO),
        ("v_pec coherence high", VPEC_COHERENCE_HI),
    ):
        L = hinv_to_mpc(xh)
        print(
            f"  {name}: {xh:.0f} h^{{-1}} Mpc = {L:.1f} Mpc  "
            f"vs NP-A {frac(L, ELL_NPA):.0%}  vs R8 {frac(L, R8):.0%}"
        )
    print()

    # Verdicts
    r0_lo = hinv_to_mpc(R0_LSTAR_LO)
    r0_hi = hinv_to_mpc(R0_LSTAR_HI)
    print("=== VERDICT (new content) ===")
    print(f"  r0(L*) ≈ {r0_lo:.1f}–{r0_hi:.1f} Mpc  (h={H:.3f})")
    print(f"  NP-A 2.06 Mpc is a factor ~{r0_lo/ELL_NPA:.1f}–{r0_hi/ELL_NPA:.1f} BELOW standard r0(L*)")
    print(f"  r0(L*) vs R8: factor ~{R8/r0_hi:.2f}–{R8/r0_lo:.2f} (same ballpark decade as structure scale)")
    print(f"  n^{{-1/3}} ≈ {hinv_to_mpc(N_INV3):.1f} Mpc — also NOT ~2.06 Mpc")
    print(f"  v_pec coherence ≫ NP-A (tens–hundreds Mpc class)")
    print()
    print("  Independent matter-clustering lengths do NOT land on NP-A 2.06 Mpc.")
    print("  Closest programme row to r0/R8 class is DESI-ceiling d=3 cell (~12.6 Mpc),")
    print("  not the Euclid-target NP-A cell — and that is STILL not a derived principle.")
    print()
    print("Illegal: pick a faint-galaxy subsample after seeing 2.06 to force r0 match")
    print("Illegal: call this a derivation of ell_*")
    print("Open kernel unchanged: principle fixing ell_* still ABSENT")
    print("See papers/ell-star-r0-peculiar-scales.md")


if __name__ == "__main__":
    main()
