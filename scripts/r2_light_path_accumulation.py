#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WP3 / R2 — anisotropic stress → potential wrinkles → light-path accumulation.

Physical picture (honest):
  Stochastic DE need not change the global expansion rate H(z).
  It can source traceless anisotropic stress π_T, which wrinkles Φ,Ψ.
  Photons accumulate lensing / ISW-like shifts over Gpc paths.

  THIS IS NOT free lunch for a Sorkin seed 1e-61.
  Path accumulation multiplies by at most ~sqrt(N_patches) for incoherent
  noise (or ~N for perfectly coherent), with N ~ χ / ell_* = O(10^2–10^4)
  for mesoscopic cells — NOT 10^56.

  Galaxy formation from Big Bang quantum noise used inflationary amplitude
  ~ H/M_Pl ~ 1e-5 after freeze-out, not late-time Sorkin counting.

Run (uses all cores for path Monte Carlo):
  python scripts/r2_light_path_accumulation.py
  python scripts/r2_light_path_accumulation.py --heavy
"""

from __future__ import annotations

import argparse
import math
import os
from concurrent.futures import ProcessPoolExecutor

import numpy as np

# ---- Cosmology (flat ΛCDM, Planck/DESI-ish) ----
OM = 0.315
OL = 0.685
H0 = 67.4  # km/s/Mpc
C_KMS = 299792.458
MPC_M = 3.085677581e22
L_P_M = 1.616e-35

# Observational floors (a posteriori tests only)
DESI_SIGMA_X = 1.5e-4
MAUS_SLIP = 0.17  # |γ-1| ~ 0.17 for γ=1.17
SAKR_FLOOR = 0.05
# Weak lensing / shear: order-of-magnitude rms sensitivity ~ 1e-2 to few 1e-3
SHEAR_FLOOR = 1e-3
# ISW / potential: very rough multipole-integrated sensitivity
ISW_FLOOR = 1e-5


def E(z: float) -> float:
    return math.sqrt(OM * (1 + z) ** 3 + OL)


def chi_of_z(z: float, n: int = 800) -> float:
    """Comoving distance χ(z) in Mpc/h units... use Mpc with H0."""
    # χ = ∫ c dz / H(z), H = 100 h E with h=H0/100 — use km/s/Mpc
    zs = np.linspace(0.0, z, n)
    integrand = C_KMS / (H0 * np.array([E(float(zi)) for zi in zs]))
    return float(np.trapezoid(integrand, zs))  # Mpc


def rho_x_over_m(z: float) -> float:
    return OL / (OM * (1.0 + z) ** 3)


def local_slip(eps: float, sigma: float, z: float, delta_m: float = 1.0) -> float:
    """|γ-1| ≈ 2 ε σ (ρ_X/ρ_m) / |δ_m|  (sub-horizon anisotropy eq.)."""
    return 2.0 * eps * sigma * rho_x_over_m(z) / abs(delta_m)


def single_patch_potential_wrinkle(
    eps: float, sigma: float, z: float, delta_m: float = 1.0
) -> float:
    """
    Order-of-magnitude |Φ-Ψ| / |Ψ| = |γ-1|.
    For lensing, Weyl potential (Φ+Ψ)/2; slip contribution to Φ-Ψ is the wrinkle.
    Take |Φ-Ψ| ~ |γ-1| |Ψ| and |Ψ| ~ O(1e-5) on linear large scales from matter,
    or bound by Poisson: k²Ψ ~ 4πG a² ρ_m δ_m → |Ψ| ~ O(1e-5–1e-4) typical.
    We report dimensionless wrinkle amplitude w = |γ-1| (fractional slip).
    Absolute potential difference ~ w * Psi_typ.
    """
    return local_slip(eps, sigma, z, delta_m)


def n_patches(chi_mpc: float, ell_mpc: float) -> float:
    """Number of independent correlation cells along a line of sight."""
    return max(chi_mpc / max(ell_mpc, 1e-12), 1.0)


def accumulate_incoherent(single: float, n: float) -> float:
    """Random-walk / uncorrelated patch accumulation (RMS)."""
    return single * math.sqrt(n)


def accumulate_coherent(single: float, n: float) -> float:
    """Perfect phase locking (upper, usually unphysical for stochastic DE)."""
    return single * n


def worker_mc(args):
    """Monte Carlo: sum independent Gaussian wrinkles along path."""
    seed, n_path, single_amp, n_pat = args
    rng = np.random.default_rng(seed)
    # each path: sum of n_pat independent N(0, single_amp^2) then |mean| or end value
    # accumulated observable ~ sum; RMS of sum = single * sqrt(n)
    n_pat = int(max(n_pat, 1))
    draws = rng.normal(0.0, single_amp, size=(n_path, n_pat))
    totals = draws.sum(axis=1)
    return {
        "rms": float(np.sqrt(np.mean(totals**2))),
        "p95": float(np.percentile(np.abs(totals), 95)),
        "mean_abs": float(np.mean(np.abs(totals))),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--heavy", action="store_true", help="more MC paths")
    args = ap.parse_args()

    n_paths = 50000 if args.heavy else 8000
    z_src = 1.5
    chi = chi_of_z(z_src)
    L_H_mpc = C_KMS / H0  # ~ c/H0 in Mpc

    print("=" * 72)
    print("WP3 / R2 — light-path accumulation of anisotropic DE stress")
    print("=" * 72)
    print(f"Source plane z={z_src}, χ ≈ {chi:.1f} Mpc")
    print(f"Hubble scale c/H0 ≈ {L_H_mpc:.0f} Mpc")
    print(f"MC paths per case: {n_paths}")
    print()
    print("Physics: π_T = ε σ ρ_X  →  |γ-1| = 2 ε σ (ρ_X/ρ_m)/δ_m")
    print("Noise need NOT change global H(z); it wrinkles Φ,Ψ; light integrates.")
    print("Accumulation is geometric (path / correlation length), NOT 10^56 free lunch.")
    print()

    # ---- Cases ----
    cases = [
        ("Sorkin seed", 1.2e-61, 1.0, L_H_mpc),  # ell ~ horizon? use Planck cell → N huge but amp tiny
        ("Sorkin + ell_*=1 Mpc", 1.2e-61, 1.0, 1.0),
        ("WP1 meso d=2 (ell~0.04 Mpc, σ=1e-5)", 1e-5, 1.0, 0.04),
        ("WP1 meso d=3 (ell~2 Mpc, σ=1e-5)", 1e-5, 1.0, 2.1),
        ("DESI ceiling σ_X (a posteriori)", DESI_SIGMA_X, 1.0, 10.0),
        ("DESI ceiling, ε=0.1", DESI_SIGMA_X, 0.1, 10.0),
    ]

    # For Sorkin, local slip is tiny; ell_* for patch count from WP1 Planck is L_P
    # Use ell in Mpc: L_P in Mpc
    L_P_mpc = L_P_M / MPC_M
    cases[0] = ("Sorkin + Planck cell", 1.2e-61, 1.0, max(L_P_mpc, 1e-60))

    print(f"{'case':<42} {'|γ-1|_loc':>10} {'N_pat':>10} {'RMS_incoh':>12} {'coherent':>12}")
    print("-" * 90)

    z_mid = 0.8
    rows = []
    for name, sigma, eps, ell in cases:
        slip = local_slip(eps, sigma, z_mid)
        npat = n_patches(chi, ell)
        # Cap N_pat for Planck cell: path can't resolve Planck patches as independent
        # classical light observables — still report math
        if npat > 1e12:
            npat_eff = 1e12  # numerical cap for display of coherent (already absurd)
        else:
            npat_eff = npat
        rms = accumulate_incoherent(slip, npat_eff)
        coh = accumulate_coherent(slip, min(npat_eff, 1e6))  # cap coherent print
        print(
            f"{name:<42} {slip:10.3e} {npat:10.3e} {rms:12.3e} {coh:12.3e}"
        )
        rows.append((name, sigma, eps, ell, slip, npat, rms, coh))

    print()
    print("--- Comparison to observational floors (order-of-magnitude) ---")
    print(f"  Maus |γ-1| scale     ~ {MAUS_SLIP}")
    print(f"  Sakr forecast floor  ~ {SAKR_FLOOR}")
    print(f"  Shear rms floor      ~ {SHEAR_FLOOR}  (schematic)")
    print(f"  ISW-like floor       ~ {ISW_FLOOR}   (schematic)")
    print()

    # Path Monte Carlo for the interesting mesoscopic case
    print("--- Monte Carlo path sum (mesoscopic σ=1e-5, ell=2.1 Mpc, ε=1) ---")
    slip = local_slip(1.0, 1e-5, z_mid)
    npat = n_patches(chi, 2.1)
    n_workers = os.cpu_count() or 4
    chunk = max(n_paths // n_workers, 1)
    jobs = []
    seed0 = 42
    left = n_paths
    s = seed0
    while left > 0:
        take = min(chunk, left)
        jobs.append((s, take, slip, npat))
        s += 1
        left -= take
    with ProcessPoolExecutor(max_workers=n_workers) as ex:
        parts = list(ex.map(worker_mc, jobs))
    # combine
    # re-run single pool result aggregation approximately via weighted
    rms_list = [p["rms"] for p in parts]
    p95_list = [p["p95"] for p in parts]
    print(f"  single-patch |γ-1|     = {slip:.3e}")
    print(f"  N_patches              = {npat:.1f}")
    print(f"  analytic RMS (√N)      = {accumulate_incoherent(slip, npat):.3e}")
    print(f"  MC RMS (chunk mean)    = {float(np.mean(rms_list)):.3e}")
    print(f"  MC p95 |sum| (mean)    = {float(np.mean(p95_list)):.3e}")
    print()

    print("--- Inflation analogy (correct scale comparison) ---")
    print("  Primordial curvature ζ ~ 1e-5 (after inflation) → structure / galaxies.")
    print("  That is NOT late-time Sorkin 1e-61 stretched by Δx=O(1).")
    print("  'Universe as telescope' for galaxies used an already large seed.")
    print()

    print("--- Max geometric gain √N along z=1.5 path ---")
    for ell in (0.04, 1.0, 2.1, 10.0, 100.0):
        n = n_patches(chi, ell)
        print(f"  ell_*={ell:<6} Mpc  N≈{n:8.1f}  √N≈{math.sqrt(n):8.2f}  "
              f"(gain on dimensionless slip, not on 1e-61→1e-5)")
    print()

    # What √N would need to lift Sorkin local slip to Sakr floor?
    slip_s = local_slip(1.0, 1.2e-61, z_mid)
    need = SAKR_FLOOR / max(slip_s, 1e-300)
    print("--- Free-lunch check: √N needed to lift Sorkin slip to Sakr floor 0.05 ---")
    print(f"  local Sorkin |γ-1| = {slip_s:.3e}")
    print(f"  required √N        = {need:.3e}  =>  N = {need**2:.3e}")
    print(f"  available √N (ell=1 Mpc) = {math.sqrt(n_patches(chi, 1.0)):.1f}")
    print("  Deficit: many decades. Path accumulation does NOT replace R1.")
    print()

    print("VERDICT:")
    print("  Right idea: measure π_T via light (lensing/slip/ISW), not only H(z).")
    print("  Wrong hope: Gpc paths do not multiply 1e-61 into 1e-5.")
    print("  Geometric gain ~ √N = O(10–100) for Mpc cells over Gpc paths.")
    print("  Measurable wrinkles still require WP1 mesoscopic σ_0,eff (or hard R3).")
    print("  Act IV inheritance confirmed with path integral language.")


if __name__ == "__main__":
    main()
