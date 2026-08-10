#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blind R1 candidate: ell_* = R_nl where sigma(R_nl)=1 for matter.

A priori inputs (matter only — NOT DESI sigma_X, NOT target 12.56 Mpc):
  sigma8 ≈ 0.81 (Planck-class)
  n_eff local ∈ {-2, -1.5, -1}  (OOM slope of P(k) near 8 h^{-1} Mpc)
  R8_def = 8 h^{-1} Mpc
  sigma(R) ≈ sigma8 * (R8/R)^alpha,  alpha=(n_eff+3)/2
  R_nl = R8 * sigma8**(1/alpha)

A posteriori: compare to r0, R8(Mpc), DESI-ceiling d=3 cell.

See papers/r1-principle-nonlinear-matter.md
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
_SCRIPTS = ROOT / "scripts"
for _d in (_SCRIPTS, _SCRIPTS / "core", _SCRIPTS / "r1", _SCRIPTS / "closed", _SCRIPTS / "side"):
    if _d.is_dir() and str(_d) not in sys.path:
        sys.path.insert(0, str(_d))

from lib_verified import H0_KM_S_MPC, ell_mpc_for_sigma, r8_mpc, sigma_from_count, hubble_radius_mpc  # noqa: E402

SIGMA8 = 0.81  # Planck-class OOM; matter amplitude — not a DESI residual
R8_HINV = 8.0  # definition of the sigma8 pivot [h^{-1} Mpc]
H = H0_KM_S_MPC / 100.0


def alpha(n_eff: float) -> float:
    return 0.5 * (n_eff + 3.0)


def R_nl_hinv(n_eff: float, sigma8: float = SIGMA8) -> float:
    """R_nl in h^{-1} Mpc from sigma(R_nl)=1."""
    a = alpha(n_eff)
    if a <= 0:
        raise ValueError("alpha must be positive")
    return R8_HINV * (sigma8 ** (1.0 / a))


def R_nl_mpc(n_eff: float, sigma8: float = SIGMA8) -> float:
    return R_nl_hinv(n_eff, sigma8) / H


def sigma_count_d3(ell_mpc: float) -> float:
    L = hubble_radius_mpc()
    return sigma_from_count(ell_mpc, L, 3.0)


def main() -> None:
    print("=== Blind principle P_nl: ell_* = R_nl with sigma(R_nl)=1 ===")
    print("A priori inputs (matter only):")
    print(f"  sigma8 = {SIGMA8}  (Planck-class matter amplitude)")
    print(f"  R8 pivot = {R8_HINV} h^{{-1}} Mpc")
    print(f"  h = {H:.3f}")
    print("  n_eff scanned as OOM local slope (not fitted to DESI)")
    print()
    print("A priori prediction:")
    print(f"{'n_eff':>8} {'alpha':>8} {'R_nl h^-1':>12} {'R_nl Mpc':>10} {'σ_count d=3':>12}")
    preds = []
    for ne in (-2.0, -1.5, -1.0):
        rh = R_nl_hinv(ne)
        rm = R_nl_mpc(ne)
        sc = sigma_count_d3(rm)
        preds.append(rm)
        print(f"{ne:8.1f} {alpha(ne):8.3f} {rh:12.3f} {rm:10.3f} {sc:12.3e}")
    r_lo, r_hi = min(preds), max(preds)
    print(f"  => Blind band R_nl ≈ {r_lo:.1f}–{r_hi:.1f} Mpc")
    print()

    # A posteriori neighbours (comparison only)
    r8 = r8_mpc()
    ell_ceil = ell_mpc_for_sigma(2.5e-2, 3)
    ell_npa = ell_mpc_for_sigma(1e-5, 3)
    r0_lo = 5.0 / H
    r0_hi = 6.0 / H
    print("A posteriori comparison (NOT used to choose n_eff or sigma8):")
    print(f"  r0(L*) ≈ {r0_lo:.2f}–{r0_hi:.2f} Mpc")
    print(f"  R_8      = {r8:.3f} Mpc")
    print(f"  DESI-ceil d=3 cell = {ell_ceil:.3f} Mpc")
    print(f"  NP-A (σ=1e-5) cell = {ell_npa:.3f} Mpc  [different row; not the lead]")
    print()
    mid = 0.5 * (r_lo + r_hi)
    print(f"  Mid R_nl={mid:.2f} Mpc vs r0 mid: |Δ|/r0 = {abs(mid - 0.5*(r0_lo+r0_hi))/(0.5*(r0_lo+r0_hi)):.0%}")
    print(f"  Mid R_nl vs R8: |Δ|/R8 = {abs(mid - r8)/r8:.0%}")
    print(f"  Mid R_nl vs DESI-ceil cell: |Δ|/cell = {abs(mid - ell_ceil)/ell_ceil:.0%}")
    print()
    print("Honesty locks:")
    print("  Principle uses matter sigma8 + n_eff only — not DESI residual likelihood")
    print("  Overlap with 8–12 Mpc decade is a posteriori")
    print("  Microphysics of vacuum–matter decoherence still OPEN")
    print("  Does NOT solve 9% H0 tension")
    print("See papers/r1-principle-nonlinear-matter.md")


if __name__ == "__main__":
    main()
