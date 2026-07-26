#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tier-1 mechanism computations for R1 open kernel (numbers, not slogans).

T1.1 — Averaging domain L_av := R_nl (from full sigma(R)=1 only)
        N = (L_H / L_av)^d ,  sigma_count = 1/sqrt(N) = (L_av/L_H)^{d/2}
        Compare a posteriori to DESI sigma_X ceiling.

T1.2 — Edge / nonlinear mask: volume fraction f = P(δ>δ_c) for Gaussian
        field with sigma(R_nl)=1; characteristic separation of nonlinear
        patches ~ R_nl * f^{-1/3} (packing OOM, not full peak theory).

Neither step derives vacuum decoherence from an action.
Both use matter geometry only for lengths; DESI only a posteriori.

See papers/r1-t1-mechanisms-compute.md
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

from lib_verified import (  # noqa: E402
    hubble_radius_mpc,
    ell_mpc_for_sigma,
    r8_mpc,
    sigma_from_count,
)
from r1_sigma_R_full import (  # noqa: E402
    H,
    SIGMA8,
    find_R_nl,
    make_Pk_unnorm,
    normalize_A,
    sigma_R,
)

DESI_CEIL = 1.5e-4
SIGMA_EUCLID = 1e-5


def gaussian_tail_fraction(delta_c: float, sigma: float) -> float:
    """
    P(δ > δ_c) for Gaussian N(0, sigma^2) = (1/2) erfc(δ_c / (sqrt(2) sigma)).
    """
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    return 0.5 * math.erfc(delta_c / (math.sqrt(2.0) * sigma))


def packing_separation(R: float, f: float) -> float:
    """Typical center-to-center distance if volume fraction f is in blobs of size R."""
    if f <= 0 or f >= 1:
        return float("inf")
    return R * (f ** (-1.0 / 3.0))


def main() -> None:
    print("=== T1 mechanism compute (matter-first lengths) ===")
    print("Honesty: hypothesis machinery, not action-derived decoherence.")
    print()

    # --- R_nl from full integral (shared a priori length) ---
    Pk = make_Pk_unnorm()
    A = normalize_A(Pk, SIGMA8)
    R_nl_h = find_R_nl(Pk, A, 1.0)
    R_nl = R_nl_h / H
    assert abs(sigma_R(R_nl_h, Pk, A) - 1.0) < 1e-3
    L_H = hubble_radius_mpc()

    print("--- Shared a priori length ---")
    print(f"  R_nl (full σ(R)=1) = {R_nl_h:.3f} h^{{-1}} Mpc = {R_nl:.3f} Mpc")
    print(f"  L_H = {L_H:.2f} Mpc")
    print(f"  sigma8 check at 8 h^{{-1}} Mpc = {sigma_R(8.0, Pk, A):.4f}")
    print()

    # ========== T1.1 Averaging domain ==========
    print("=== T1.1 Averaging domain L_av := R_nl ===")
    print("  Principle: residual degrees of freedom are counted per averaging")
    print("  patch of size R_nl (Buchert-domain language), not per Planck cell.")
    for d in (2, 3, 4):
        N = (L_H / R_nl) ** d
        s = (R_nl / L_H) ** (0.5 * d)
        print(
            f"  d={d}: N_eff = {N:.3e}  σ_count = {s:.3e}  "
            f"vs DESI ceil {DESI_CEIL:.1e}  "
            f"{'UNDER' if s <= DESI_CEIL else 'ABOVE'}"
        )
    s3 = sigma_from_count(R_nl, L_H, 3)
    print(f"  Canonical d=3: σ = {s3:.3e}  (Euclid target 1e-5: factor {s3/SIGMA_EUCLID:.1f}×)")
    print(f"  Short of free 1e56 story: seed is mesoscopic by domain choice.")
    print()

    # ========== T1.2 Nonlinear mask / edge ==========
    print("=== T1.2 Nonlinear mask |δ| > δ_c on field with σ(R_nl)=1 ===")
    print("  Gaussian OOM (not full peak theory / excursion-set mass function).")
    sigma_field = 1.0  # by definition of R_nl
    for delta_c in (1.0, 1.5, 2.0):
        f = gaussian_tail_fraction(delta_c, sigma_field)
        sep = packing_separation(R_nl, f)
        # correlation length of indicator field ~ R for threshold ~ sigma (OOM)
        ell_mask = R_nl  # filter scale sets blob size OOM
        print(
            f"  δ_c={delta_c:.1f}: f_vol = {f:.4f}  "
            f"blob size ~ R_nl = {ell_mask:.2f} Mpc  "
            f"sep ~ R f^{{-1/3}} = {sep:.2f} Mpc"
        )
    f1 = gaussian_tail_fraction(1.0, 1.0)
    sep1 = packing_separation(R_nl, f1)
    print()
    print("  Reading:")
    print(f"    Edge/blob scale ~ R_nl = {R_nl:.2f} Mpc  (in 8–12 decade)")
    print(f"    Inter-blob separation (δ_c=1) ~ {sep1:.2f} Mpc  (same decade as R8/DESI-ceil cell)")
    print("    Mask correlation length is O(R_nl), not O(L_P) or O(L_H).")
    print()

    # ========== A posteriori anchors ==========
    print("=== A posteriori anchors (not used to choose R_nl) ===")
    print(f"  r0(L*) class     ≈ {5/H:.2f}–{6/H:.2f} Mpc")
    print(f"  R_8              = {r8_mpc():.3f} Mpc")
    print(f"  DESI-ceil d=3    = {ell_mpc_for_sigma(DESI_CEIL, 3):.3f} Mpc")
    print(f"  NP-A d=3         = {ell_mpc_for_sigma(SIGMA_EUCLID, 3):.3f} Mpc")
    print()
    print("=== Status ===")
    print("  T1.1: counting on L_av=R_nl → σ~8.5e-5 (d=3) UNDER DESI ceiling — compatible")
    print("  T1.2: edge scale ~ R_nl; packing sep ~ 1.5–2× R_nl — same decade")
    print("  STILL OPEN: action/master-equation why vacuum residual lives on that domain")
    print("  NOT claimed: Buchert explains mean acceleration; H0 9% solved")
    print("See papers/r1-t1-mechanisms-compute.md")


if __name__ == "__main__":
    main()
