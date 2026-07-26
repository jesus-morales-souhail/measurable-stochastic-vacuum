#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full linear sigma(R) for flat LCDM (top-hat window), normalized to sigma8.

Honest refinement of the local power-law shortcut in r1_principle_Rnl.py:
  sigma^2(R) = ∫_0^∞ (dk/k) Δ^2(k) W_TH^2(kR)
  Δ^2(k) = k^3 P(k) / (2 π^2)
  W_TH(x) = 3 (sin x - x cos x) / x^3

P(k) = A k^{n_s} T^2(k) with Eisenstein & Hu (1998) zero-baryon
transfer (or EH with Omega_b), normalized so sigma(8/h Mpc)=sigma8.

This still does NOT derive vacuum–matter decoherence from an action.
It only replaces the n_eff power-law map for R_nl where sigma(R_nl)=1.

See papers/r1-principle-nonlinear-matter.md
"""

from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Callable, Tuple

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from lib_verified import H0_KM_S_MPC, ell_mpc_for_sigma, r8_mpc, hubble_radius_mpc, sigma_from_count  # noqa: E402

# Planck-class OOM cosmology (matter sector for P(k); not DESI residual fit)
OM0 = 0.315
OB0 = 0.049
H0 = H0_KM_S_MPC
H = H0 / 100.0
NS = 0.965
SIGMA8 = 0.81
T_CMB = 2.7255  # K


def top_hat_W(x: float) -> float:
    """Spherical top-hat Fourier window. W(0)=1."""
    if x < 1e-4:
        return 1.0 - x * x / 10.0
    return 3.0 * (math.sin(x) - x * math.cos(x)) / (x**3)


def eh_transfer_zero_baryon(k_hmpc: float, omh2: float, theta_cmb: float = T_CMB / 2.7) -> float:
    """
    Eisenstein & Hu (1998) zero-baryon transfer, Eqs. (29)–(31).
    k in h/Mpc; returns T(k) with T→1 as k→0.
    """
    if k_hmpc <= 0:
        return 1.0
    # Gamma shape
    Gamma = omh2 / H  # ≈ Omega_m h in zero-baryon EH; use om * h
    # Actually EH: Γ = Ω_m h; q = k / (Γ h) with k in Mpc^{-1}... careful units.
    # Standard implementation: k in h/Mpc, q = k / (Γ) with Γ = Ω_m h
    Gamma = OM0 * H
    q = k_hmpc / Gamma * theta_cmb**2
    # L0, C0
    L0 = math.log(2.0 * math.e + 1.8 * q)
    C0 = 14.2 + 731.0 / (1.0 + 62.5 * q)
    return L0 / (L0 + C0 * q * q)


def eh_transfer_with_baryons(k_hmpc: float) -> float:
    """
    Simplified EH with baryons: use zero-baryon with effective shape Γ_eff.
    Good enough OOM for R_nl; full EH is longer. Γ_eff = Ω_m h exp(-Ω_b(1+√(2h)/Ω_m))
    """
    omh2 = OM0 * H * H
    obh2 = OB0 * H * H
    # Sugiyama shape approx
    Gamma_eff = OM0 * H * math.exp(-OB0 * (1.0 + math.sqrt(2.0 * H) / OM0))
    if k_hmpc <= 0:
        return 1.0
    q = k_hmpc / max(Gamma_eff, 1e-6) * (T_CMB / 2.7) ** 2
    L0 = math.log(2.0 * math.e + 1.8 * q)
    C0 = 14.2 + 731.0 / (1.0 + 62.5 * q)
    return L0 / (L0 + C0 * q * q)


def make_Pk_unnorm(transfer: Callable[[float], float] = eh_transfer_with_baryons) -> Callable[[float], float]:
    """Unnormalized P(k) with k in h/Mpc."""

    def Pk(k: float) -> float:
        if k <= 0:
            return 0.0
        T = transfer(k)
        return (k**NS) * (T**2)

    return Pk


def sigma2_of_R_unnorm(
    R_hinv: float,
    Pk: Callable[[float], float],
    kmin: float = 1e-4,
    kmax: float = 1e2,
) -> float:
    """
    Unnormalized sigma^2(R) for R in h^{-1} Mpc, k in h/Mpc (A=1).
    Use log-k quadrature so tiny P(k) amplitudes remain accurate.
    integrand: dk * k² P(k) W²(kR) / (2π²)
    """

    def integrand_logk(lk: float) -> float:
        k = math.exp(lk)
        x = k * R_hinv
        W = top_hat_W(x)
        # d ln k = dk/k ⇒ dk * k² = k³ d ln k
        return (k**3) * Pk(k) * (W**2) / (2.0 * math.pi**2)

    val, err = quad(
        integrand_logk,
        math.log(kmin),
        math.log(kmax),
        epsabs=1e-10,
        epsrel=1e-6,
        limit=400,
    )
    return max(val, 0.0)


def normalize_A(Pk: Callable[[float], float], sigma8: float = SIGMA8) -> float:
    """A such that sigma(R=8 h^{-1} Mpc) = sigma8."""
    s2 = sigma2_of_R_unnorm(8.0, Pk)
    if s2 <= 0:
        raise RuntimeError("sigma2(8) vanished")
    return (sigma8**2) / s2


def sigma_R(R_hinv: float, Pk: Callable[[float], float], A: float) -> float:
    """sigma(R) = sqrt(A * sigma2_unnorm). Linear in amplitude (stable)."""
    return math.sqrt(A * sigma2_of_R_unnorm(R_hinv, Pk))


def find_R_nl(Pk: Callable[[float], float], A: float, target: float = 1.0) -> float:
    """R_nl in h^{-1} Mpc with sigma(R_nl)=target."""

    def f(R: float) -> float:
        return sigma_R(R, Pk, A) - target

    # bracket
    lo, hi = 0.5, 30.0
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        # expand
        for hi in (20.0, 40.0, 80.0):
            fhi = f(hi)
            if flo * fhi <= 0:
                break
        else:
            raise RuntimeError(f"cannot bracket R_nl: f({lo})={flo}, f({hi})={fhi}")
    return brentq(f, lo, hi, xtol=1e-5)


def power_law_R_nl(n_eff: float, sigma8: float = SIGMA8) -> float:
    """Old shortcut R_nl [h^{-1} Mpc]."""
    a = 0.5 * (n_eff + 3.0)
    return 8.0 * (sigma8 ** (1.0 / a))


def main() -> None:
    print("=== Full σ(R) integral (top-hat) vs power-law shortcut ===")
    print("Honesty: P_nl is a physical HYPOTHESIS (decoherence at collapse),")
    print("         not a derivation from an action.")
    print()
    print(f"Cosmology: Om={OM0}, Ob={OB0}, h={H:.3f}, n_s={NS}, sigma8={SIGMA8}")
    print()

    Pk = make_Pk_unnorm()
    A = normalize_A(Pk, SIGMA8)
    s8_check = sigma_R(8.0, Pk, A)
    print(f"Normalization check: sigma(8 h^{{-1}} Mpc) = {s8_check:.4f}  (target {SIGMA8})")
    print()

    R_nl_h = find_R_nl(Pk, A, 1.0)
    R_nl_mpc = R_nl_h / H
    print(f"FULL integral: R_nl (sigma=1) = {R_nl_h:.3f} h^{{-1}} Mpc = {R_nl_mpc:.3f} Mpc")
    print()

    print("Power-law shortcut (for comparison only):")
    for ne in (-2.0, -1.5, -1.0):
        rh = power_law_R_nl(ne)
        print(f"  n_eff={ne:+.1f}: R_nl = {rh:.3f} h^{{-1}} Mpc = {rh/H:.3f} Mpc")
    print()

    # table sigma(R) at a few scales
    print(f"{'R h^-1':>10} {'R Mpc':>10} {'sigma(R)':>10}")
    for Rh in (2.0, 5.0, 6.0, 8.0, 10.0, 12.0, R_nl_h):
        print(f"{Rh:10.3f} {Rh/H:10.3f} {sigma_R(Rh, Pk, A):10.4f}")
    print()

    # a posteriori programme neighbours
    L = hubble_radius_mpc()
    sig_count = (R_nl_mpc / L) ** 1.5
    print("A posteriori (not used in R_nl solve):")
    print(f"  R_8 = {r8_mpc():.3f} Mpc")
    print(f"  DESI-ceil d=3 cell = {ell_mpc_for_sigma(1.5e-4, 3):.3f} Mpc")
    print(f"  r0(L*) class ≈ {5/H:.2f}–{6/H:.2f} Mpc")
    print(f"  If ell_*=R_nl full: sigma_count d=3 = {sig_count:.3e}  (DESI ceil 1.5e-4)")
    print()
    print("Still open: why vacuum residual grain = R_nl (hypothesis, not action principle)")
    print("See papers/r1-principle-nonlinear-matter.md")


if __name__ == "__main__":
    main()
