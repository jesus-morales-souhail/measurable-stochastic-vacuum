#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verified kinematic / OOM maps for the measurable-stochastic-vacuum programme.

Only identities and standard sub-horizon GR relations used in papers/VERIFIED_RESULTS.md.
No Boltzmann solver. No free 1e56 factors.

Notation
--------
ell_* : counting / correlation cell length
L     : IR region size used in the count (e.g. Hubble radius)
d     : counting dimension (2 holographic area, 3 volume, 4 spacetime volume)
sigma_0_eff : 1/sqrt(N_eff) with N_eff = (L/ell_*)^d
eps   : anisotropic fraction of residual density contrast in DE sector
"""

from __future__ import annotations

import math
from typing import Tuple

import numpy as np

# ---- Fixed physical constants (SI / cosmology conventions) ----
C_M_S = 299_792_458.0
MPC_M = 3.085_677_581e22
L_P_M = 1.616_255e-35  # CODATA-style Planck length

# Flat ΛCDM fiducial used only for OOM distances and ρ_X/ρ_m (not fitted to DESI here)
OM0 = 0.315
OL0 = 0.685
H0_KM_S_MPC = 67.4


# ---------------------------------------------------------------------------
# R1 — counting identities (exact given the counting hypothesis)
# ---------------------------------------------------------------------------

def n_eff(ell: float, L: float, d: float) -> float:
    """N_eff = (L/ell)^d. Requires ell>0, L>0, d>0."""
    if ell <= 0 or L <= 0 or d <= 0:
        raise ValueError("ell, L, d must be positive")
    return (L / ell) ** d


def sigma_from_count(ell: float, L: float, d: float) -> float:
    """sigma_0,eff = (ell/L)^{d/2} = 1/sqrt(N_eff)."""
    return (ell / L) ** (0.5 * d)


def ell_for_target_sigma(sigma: float, L: float, d: float) -> float:
    """
    Invert sigma = (ell/L)^{d/2}  =>  ell = L * sigma^{2/d}.
    Exact under the counting hypothesis.
    """
    if sigma <= 0 or L <= 0 or d <= 0:
        raise ValueError("sigma, L, d must be positive")
    return L * (sigma ** (2.0 / d))


def hubble_radius_m(H0_km_s_mpc: float = H0_KM_S_MPC) -> float:
    """L_H = c/H0 in metres."""
    H0_si = (H0_km_s_mpc * 1e3) / MPC_M  # 1/s
    return C_M_S / H0_si


def sorkin_holographic(H0_km_s_mpc: float = H0_KM_S_MPC) -> Tuple[float, float, float]:
    """
    Standard holographic count on the Hubble sphere:
      N_BH = (L_H/L_P)^2,  sigma_0 = 1/sqrt(N_BH) = L_P/L_H.
    Returns (L_H_m, N_BH, sigma_0).
    """
    L_H = hubble_radius_m(H0_km_s_mpc)
    N_BH = (L_H / L_P_M) ** 2
    sigma_0 = 1.0 / math.sqrt(N_BH)
    return L_H, N_BH, sigma_0


# ---------------------------------------------------------------------------
# R2 — sub-horizon anisotropic stress → gravitational slip (standard GR)
# ---------------------------------------------------------------------------

def rho_x_over_rho_m(z: float, Om0: float = OM0, Ol0: float = OL0) -> float:
    """ρ_X/ρ_m for constant-ρ_X (Λ-like) and matter ∝ (1+z)^3."""
    if z < -1:
        raise ValueError("z < -1 invalid")
    return Ol0 / (Om0 * (1.0 + z) ** 3)


def slip_deviation(
    eps: float,
    sigma: float,
    z: float,
    delta_m: float = 1.0,
    Om0: float = OM0,
    Ol0: float = OL0,
) -> float:
    """
    |γ - 1| = |Φ/Ψ - 1| from sub-horizon anisotropy equation
    (Ma & Bertschinger 1995 form used in Option 0 / slip_bridge):

        k² Ψ = -4π G a² ρ_m δ_m
        k² (Φ - Ψ) = 8π G a² π_T
        π_T = eps * sigma * ρ_X

    ⇒ |Φ-Ψ|/|Ψ| = 2 |π_T| / |ρ_m δ_m| = 2 eps sigma (ρ_X/ρ_m) / |δ_m|.

    Assumptions (must be stated in any publication claim):
      - Newtonian gauge, flat FLRW, sub-horizon k ≫ aH
      - μ = 1 (standard Poisson for Ψ)
      - π_T amplitude model as above (phenomenological)
    """
    if delta_m == 0:
        raise ZeroDivisionError("delta_m must be non-zero")
    return 2.0 * abs(eps) * abs(sigma) * rho_x_over_rho_m(z, Om0, Ol0) / abs(delta_m)


# ---------------------------------------------------------------------------
# Path accumulation (probability, not new GR)
# ---------------------------------------------------------------------------

def n_patches(chi: float, ell: float) -> float:
    """Number of independent patches along a path of length chi with cell ell."""
    if chi <= 0 or ell <= 0:
        raise ValueError("chi and ell must be positive")
    return chi / ell


def rms_incoherent(single_amp: float, n_pat: float) -> float:
    """
    If X = sum_{i=1}^N x_i with x_i iid, E[x_i]=0, Var(x_i)=s^2,
    then RMS(X) = s * sqrt(N).  Here single_amp plays the role of s
    (RMS of one patch), n_pat = N.
    """
    if n_pat < 0:
        raise ValueError("n_pat must be non-negative")
    return abs(single_amp) * math.sqrt(n_pat)


def e_z(z: float, Om0: float = OM0, Ol0: float = OL0) -> float:
    return math.sqrt(Om0 * (1.0 + z) ** 3 + Ol0)


def comoving_distance_mpc(
    z: float,
    H0_km_s_mpc: float = H0_KM_S_MPC,
    Om0: float = OM0,
    Ol0: float = OL0,
    n: int = 2000,
) -> float:
    """
    χ(z) = ∫_0^z c dz' / H(z') in Mpc, H(z)=H0 E(z).
    Trapezoidal integration; n controls accuracy (tested).
    """
    if z < 0:
        raise ValueError("z must be >= 0")
    if z == 0:
        return 0.0
    zs = np.linspace(0.0, z, n)
    invE = np.array([1.0 / e_z(float(zi), Om0, Ol0) for zi in zs])
    # χ = (c/H0) ∫ dz/E ; c/H0 in Mpc: C_KMS/H0
    c_over_H0 = 299792.458 / H0_km_s_mpc
    return float(c_over_H0 * np.trapezoid(invE, zs))


# ---------------------------------------------------------------------------
# R3 — soft open-system gain bounds (definitions, not microphysics)
# ---------------------------------------------------------------------------

def soft_squeeze_gain(r: float) -> float:
    """
    Intensity-like factor e^{2r} for a single-mode squeeze parameter r.
    This is a kinematic identity of the squeeze operator, not a derivation
    that cosmology realises a given r.
    """
    return math.exp(2.0 * r)


def residual_soft_map(sigma0_eff: float, r: float = 1.5, g_f: float = 1.0, g_u: float = 1.0) -> float:
    """
    sigma_res = G_U * G_F * G_O * sigma0_eff with G_O = e^{2r}.
    Default G_F=1 (freeze preserves), G_U=1 (late Δx=O(1) stretch OOM).
    """
    return g_u * g_f * soft_squeeze_gain(r) * abs(sigma0_eff)


def r_needed_for_target(sigma0: float, target: float) -> float:
    """r such that e^{2r} * sigma0 = target  =>  r = (1/2) ln(target/sigma0)."""
    if sigma0 <= 0 or target <= 0:
        raise ValueError("sigma0 and target must be positive")
    return 0.5 * math.log(target / sigma0)


if __name__ == "__main__":
    L_H, N_BH, s0 = sorkin_holographic()
    print("lib_verified smoke check")
    print(f"  L_H = {L_H:.6e} m")
    print(f"  N_BH = {N_BH:.6e}")
    print(f"  sigma_Sorkin = {s0:.6e}")
    print(f"  ell(d=2, sigma=1e-5) / Mpc = {ell_for_target_sigma(1e-5, L_H, 2)/MPC_M:.4f}")
    print(f"  slip(eps=1, sigma=1.5e-4, z=0.5) = {slip_deviation(1.0, 1.5e-4, 0.5):.6e}")
    print(f"  chi(1.5) Mpc = {comoving_distance_mpc(1.5):.1f}")
    print(f"  G_O(r=1.5) = {soft_squeeze_gain(1.5):.6f}")
    print("  OK")
