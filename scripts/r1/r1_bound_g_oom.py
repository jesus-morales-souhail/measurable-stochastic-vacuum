#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stage-0 OOM bounds on dimensionless coupling lambda (and g under convention).

  (δρ_X / ρ_X)_ind = lambda * δ_m |_{R_nl}
  sigma_res^2 ≈ sigma_free^2 + lambda^2 * sigma_delta^2
  At R_nl: sigma_delta = 1  =>  |lambda| ≲ sqrt(sigma_X^2 - sigma_free^2)

  Convention: <chi^2>^{1/2}_free = sigma_free,  lambda = g * sigma_free  (kappa=1)
  => |g| ≲ |lambda| / sigma_free

Does NOT run MCMC. Primary precision path remains sister BAO likelihood.

See papers/r1-bounding-g-plan.md
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

from lib_verified import hubble_radius_mpc, sigma_from_count  # noqa: E402
from r1_sigma_R_full import (  # noqa: E402
    H,
    SIGMA8,
    find_R_nl,
    make_Pk_unnorm,
    normalize_A,
)

DESI_CEIL = 2.5e-2


def main() -> None:
    Pk = make_Pk_unnorm()
    A = normalize_A(Pk, SIGMA8)
    R_nl = find_R_nl(Pk, A, 1.0) / H
    L_H = hubble_radius_mpc()
    sigma_free = sigma_from_count(R_nl, L_H, 3)

    print("=== Stage-0 OOM bound on lambda / g ===")
    print(f"  R_nl = {R_nl:.3f} Mpc")
    print(f"  sigma_free (d=3 count) = {sigma_free:.3e}")
    print(f"  DESI sigma_X ceiling   = {DESI_CEIL:.3e}")
    print()

    # Induced-only
    lam_ind_only = DESI_CEIL
    print("Induced-only (sigma_free=0):")
    print(f"  |lambda| ≲ {lam_ind_only:.3e}")
    print()

    # Quadrature with free grain
    if sigma_free >= DESI_CEIL:
        print("WARNING: sigma_free >= DESI ceiling under this ell_*; P_nl d=3 tension.")
        lam_quad = 0.0
    else:
        lam_quad = math.sqrt(DESI_CEIL**2 - sigma_free**2)
    print("Free + induced in quadrature (sigma_delta=1 at R_nl):")
    print(f"  |lambda| ≲ {lam_quad:.3e}")
    print()

    # g under convention lambda = g * sigma_free (kappa=1)
    if sigma_free > 0 and lam_quad > 0:
        g_max = lam_quad / sigma_free
        print("Convention: lambda = g * sigma_free  (chi normalized to free RMS):")
        print(f"  |g| ≲ {g_max:.3f}   (O(1) — BAO is informative)")
    print()

    # Slip OOM at lambda max
    # |γ-1| ~ 2 * sigma_res * (Ol/Om) at z=0, δ_m=1, ε=1
    from lib_verified import slip_deviation  # noqa: E402

    s_res = DESI_CEIL  # worst case at ceiling
    slip0 = slip_deviation(1.0, s_res, 0.0, 1.0)
    print("Slip OOM at sigma_res = DESI ceiling (ε=1, z=0, δ_m=1):")
    print(f"  |γ−1|_loc ≈ {slip0:.3e}  ≪ Maus error ~0.11  → slip does not beat BAO for g")
    print()
    print("Next: sister OU BAO likelihood with sigma_res(lambda), ell_* fixed.")
    print("See papers/r1-bounding-g-plan.md")


if __name__ == "__main__":
    main()
