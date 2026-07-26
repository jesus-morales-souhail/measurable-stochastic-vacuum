#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T1.2 refinement: BBKS spectral moments and peak scales on the R_nl filter.

For a Gaussian field smoothed with top-hat W(kR):
  σ_j²(R) = ∫ (dk/k) Δ²(k) k^{2j} W²(kR)
  γ_BBKS = σ1² / (σ0 σ2)
  R_* = √3 σ1/σ2     (BBKS curvature radius of peaks)

R_nl from full sigma(R)=1; then evaluate moments at R=R_nl.
Characteristic peak size ~ R_* (comoving); packing refined vs pure f^{-1/3}.

Bardeen, Bond, Kaiser, Szalay 1986 (BBKS). Not full mass-function cosmology.

See papers/r1-t12-bbks-and-derivation.md
"""

from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Callable, Tuple

from scipy.integrate import quad

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from lib_verified import hubble_radius_mpc, r8_mpc, ell_mpc_for_sigma, sigma_from_count  # noqa: E402
from r1_sigma_R_full import (  # noqa: E402
    H,
    SIGMA8,
    find_R_nl,
    make_Pk_unnorm,
    normalize_A,
    sigma_R,
    top_hat_W,
)
from r1_t1_mechanisms_compute import gaussian_tail_fraction, packing_separation  # noqa: E402


def sigma_j2(
    R_hinv: float,
    j: int,
    Pk: Callable[[float], float],
    A: float,
    kmin: float = 1e-4,
    kmax: float = 1e2,
) -> float:
    """
    Spectral moment σ_j² with top-hat window.
    σ_j² = ∫ dk k^{2+2j} A P(k) W²(kR) / (2π²)
    (equivalent to ∫ dlnk Δ² k^{2j} W²)
    """

    def integrand_logk(lk: float) -> float:
        k = math.exp(lk)
        W = top_hat_W(k * R_hinv)
        # k^{2+2j} * P * W² / (2π²) * k dlnk wait:
        # dk * k^{2+2j} P W² / (2π²) = dlnk * k^{3+2j} P W² / (2π²)
        return (k ** (3 + 2 * j)) * (A * Pk(k)) * (W**2) / (2.0 * math.pi**2)

    val, _ = quad(
        integrand_logk,
        math.log(kmin),
        math.log(kmax),
        epsabs=1e-10,
        epsrel=1e-5,
        limit=400,
    )
    return max(val, 0.0)


def bbks_at_R(
    R_hinv: float, Pk: Callable[[float], float], A: float
) -> Tuple[float, float, float, float, float]:
    """Return (σ0, σ1, σ2, γ_BBKS, R_star_hinv)."""
    s0 = math.sqrt(sigma_j2(R_hinv, 0, Pk, A))
    s1 = math.sqrt(sigma_j2(R_hinv, 1, Pk, A))
    s2 = math.sqrt(sigma_j2(R_hinv, 2, Pk, A))
    if s0 <= 0 or s2 <= 0:
        raise RuntimeError("vanishing spectral moment")
    gamma = (s1**2) / (s0 * s2)
    R_star = math.sqrt(3.0) * s1 / s2  # h^{-1} Mpc
    return s0, s1, s2, gamma, R_star


def main() -> None:
    print("=== T1.2 BBKS peaks on R_nl filter ===")
    print("Hypothesis machinery + spectral geometry; not action derivation.")
    print()

    Pk = make_Pk_unnorm()
    A = normalize_A(Pk, SIGMA8)
    R_nl_h = find_R_nl(Pk, A, 1.0)
    R_nl = R_nl_h / H
    s0, s1, s2, gamma, R_star_h = bbks_at_R(R_nl_h, Pk, A)
    R_star = R_star_h / H

    print(f"Filter R_nl = {R_nl_h:.3f} h^{{-1}} Mpc = {R_nl:.3f} Mpc")
    print(f"  σ0 = {s0:.4f}  (should be ≈1 at R_nl)")
    print(f"  σ1 = {s1:.4e}  (h/Mpc units mixed in definition)")
    print(f"  σ2 = {s2:.4e}")
    print(f"  γ_BBKS = σ1²/(σ0 σ2) = {gamma:.4f}  (∈(0,1) for physical spectra)")
    print(f"  R_* = √3 σ1/σ2 = {R_star_h:.3f} h^{{-1}} Mpc = {R_star:.3f} Mpc")
    print()

    # Compare peak size to filter and packing
    f1 = gaussian_tail_fraction(1.0, s0)
    sep_pack = packing_separation(R_nl, f1)
    sep_star = packing_separation(R_star, f1)

    print("Scales (Mpc):")
    print(f"  R_nl (blob/filter)     = {R_nl:.3f}")
    print(f"  R_* (BBKS peak curv.)  = {R_star:.3f}   ratio R_*/R_nl = {R_star/R_nl:.3f}")
    print(f"  sep packing on R_nl    = {sep_pack:.3f}")
    print(f"  sep packing on R_*     = {sep_star:.3f}")
    print()

    L_H = hubble_radius_mpc()
    for name, ell in (
        ("R_nl", R_nl),
        ("R_*", R_star),
        ("sep_pack(R_nl)", sep_pack),
    ):
        s = sigma_from_count(ell, L_H, 3)
        print(f"  If ell_*={name}={ell:.2f} Mpc: σ_count d=3 = {s:.3e}")
    print()

    print("A posteriori:")
    print(f"  r0(L*) ≈ {5/H:.2f}–{6/H:.2f} Mpc")
    print(f"  R_8 = {r8_mpc():.3f} Mpc")
    print(f"  DESI-ceil d=3 = {ell_mpc_for_sigma(1.5e-4, 3):.3f} Mpc")
    print()
    print("BBKS splits scales: R_* (peak tip) << R_nl (filter/domain).")
    print("  Counting cell for residual domains → R_nl; R_* is substructure.")
    print("Still OPEN: microphysics of coupling g (derivation sketch assumes P0–P1).")
    print("See papers/r1-t12-bbks-and-derivation.md")


if __name__ == "__main__":
    main()
