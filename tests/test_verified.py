#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated verification of identities used in papers/VERIFIED_RESULTS.md.

Run from repo root:
  pytest -q
  python -m pytest tests/ -v
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from lib_verified import (  # noqa: E402
    L_P_M,
    comoving_distance_mpc,
    ell_for_target_sigma,
    hubble_radius_m,
    n_eff,
    n_patches,
    residual_soft_map,
    rho_x_over_rho_m,
    rms_incoherent,
    r_needed_for_target,
    sigma_from_count,
    slip_deviation,
    soft_squeeze_gain,
    sorkin_holographic,
)


class TestR1Counting:
    def test_n_eff_and_sigma_inverse(self):
        L, ell, d = 100.0, 2.0, 3.0
        N = n_eff(ell, L, d)
        s = sigma_from_count(ell, L, d)
        assert N == pytest.approx((L / ell) ** d)
        assert s == pytest.approx(1.0 / math.sqrt(N))
        assert s == pytest.approx((ell / L) ** (d / 2))

    def test_ell_inversion_exact(self):
        L, d, sigma = 4451.0, 2.0, 1e-5
        ell = ell_for_target_sigma(sigma, L, d)
        assert sigma_from_count(ell, L, d) == pytest.approx(sigma, rel=1e-12)

    def test_ell_inversion_all_d(self):
        L = hubble_radius_m() / (3.085677581e22)  # Mpc
        # use metres consistently
        L_m = hubble_radius_m()
        for d in (2, 3, 4):
            for sigma in (1e-5, 1.5e-4, 1e-6):
                ell = ell_for_target_sigma(sigma, L_m, d)
                assert sigma_from_count(ell, L_m, d) == pytest.approx(sigma, rel=1e-10)

    def test_sorkin_identity(self):
        L_H, N_BH, sigma0 = sorkin_holographic()
        assert N_BH == pytest.approx((L_H / L_P_M) ** 2, rel=1e-12)
        assert sigma0 == pytest.approx(L_P_M / L_H, rel=1e-12)
        assert sigma0 == pytest.approx(1.0 / math.sqrt(N_BH), rel=1e-12)
        # order of magnitude: ~1e-61
        assert 5e-62 < sigma0 < 3e-61

    def test_planck_cell_is_structural_zero_vs_1e_5(self):
        L_H, _, _ = sorkin_holographic()
        for d in (2, 3, 4):
            s = sigma_from_count(L_P_M, L_H, d)
            assert s < 1e-50  # far below telescope band 1e-5

    def test_mesoscopic_cells_for_1e_5(self):
        """Published landscape numbers (Mpc) within 5% of algebraic inverse."""
        L_H_m = hubble_radius_m()
        mpc = 3.085677581e22
        L_H_mpc = L_H_m / mpc
        # d=2: ell = L * sigma  (since 2/d=1)
        ell2 = ell_for_target_sigma(1e-5, L_H_m, 2) / mpc
        assert ell2 == pytest.approx(L_H_mpc * 1e-5, rel=1e-9)
        assert 0.03 < ell2 < 0.06  # ~0.04 Mpc
        ell3 = ell_for_target_sigma(1e-5, L_H_m, 3) / mpc
        assert 1.5 < ell3 < 3.0  # ~2.1 Mpc
        ell4 = ell_for_target_sigma(1e-5, L_H_m, 4) / mpc
        assert 10.0 < ell4 < 20.0  # ~14 Mpc


class TestR2Slip:
    def test_rho_ratio_z0(self):
        r = rho_x_over_rho_m(0.0)
        assert r == pytest.approx(0.685 / 0.315, rel=1e-12)

    def test_rho_ratio_high_z_matter_dominated(self):
        r = rho_x_over_rho_m(10.0)
        assert r < 0.01

    def test_slip_formula(self):
        # hand: 2*1*1e-4*(0.685/(0.315*8))/1 at z=1 => (1+z)^3=8
        z = 1.0
        ratio = 0.685 / (0.315 * 8.0)
        expected = 2.0 * 1.0 * 1e-4 * ratio
        assert slip_deviation(1.0, 1e-4, z, 1.0) == pytest.approx(expected, rel=1e-12)

    def test_slip_scales_linearly_in_sigma_and_eps(self):
        a = slip_deviation(1.0, 1e-4, 0.5)
        b = slip_deviation(0.5, 2e-4, 0.5)
        assert a == pytest.approx(b, rel=1e-12)

    def test_desi_ceiling_amplitude_starved_vs_maus(self):
        """|γ-1| with σ=1.5e-4, ε=1, δ_m=1 at z=0.5 is O(1e-4) ≪ 0.17."""
        s = slip_deviation(1.0, 1.5e-4, 0.5, 1.0)
        assert s < 5e-4
        assert s < 0.17 / 100  # >100× below Maus-scale |γ-1|~0.17

    def test_sorkin_slip_is_zero_structurally(self):
        _, _, sigma0 = sorkin_holographic()
        s = slip_deviation(1.0, sigma0, 0.5)
        assert s < 1e-60


class TestPathAccumulation:
    def test_n_patches(self):
        assert n_patches(4480.0, 2.0) == pytest.approx(2240.0)

    def test_rms_incoherent_identity(self):
        # Monte Carlo check of RMS = s * sqrt(N)
        rng = np.random.default_rng(0)
        s, N, n_mc = 1e-5, 2000, 20000
        draws = rng.normal(0.0, s, size=(n_mc, N))
        totals = draws.sum(axis=1)
        rms_mc = float(np.sqrt(np.mean(totals**2)))
        rms_th = rms_incoherent(s, N)
        assert rms_mc == pytest.approx(rms_th, rel=0.03)

    def test_path_cannot_rescue_sorkin(self):
        _, _, sigma0 = sorkin_holographic()
        slip = slip_deviation(1.0, sigma0, 0.8)
        chi = comoving_distance_mpc(1.5)
        n = n_patches(chi, 1.0)  # 1 Mpc cells
        rms = rms_incoherent(slip, n)
        assert rms < 1e-55
        # vs Sakr floor 0.05: need enormous N
        need_sqrt_n = 0.05 / slip
        assert need_sqrt_n > 1e50

    def test_mesoscopic_path_oom(self):
        slip = slip_deviation(1.0, 1e-5, 0.8)
        chi = comoving_distance_mpc(1.5)
        n = n_patches(chi, 2.1)
        rms = rms_incoherent(slip, n)
        # should be O(1e-4), not O(1) and not O(1e-60)
        assert 1e-5 < rms < 5e-3

    def test_comoving_distance_monotonic_and_scale(self):
        chi1 = comoving_distance_mpc(1.0)
        chi15 = comoving_distance_mpc(1.5)
        assert chi15 > chi1
        # z=1 roughly 3 Gpc for this cosmology
        assert 2500 < chi1 < 4000
        assert 4000 < chi15 < 5500

    def test_comoving_distance_converges_with_n(self):
        a = comoving_distance_mpc(1.5, n=500)
        b = comoving_distance_mpc(1.5, n=4000)
        assert a == pytest.approx(b, rel=1e-3)


class TestR3SoftGain:
    def test_squeeze_gain_r_zero(self):
        assert soft_squeeze_gain(0.0) == pytest.approx(1.0)

    def test_squeeze_gain_r_1_5(self):
        assert soft_squeeze_gain(1.5) == pytest.approx(math.exp(3.0), rel=1e-12)
        assert soft_squeeze_gain(1.5) == pytest.approx(20.08553692, rel=1e-6)

    def test_soft_map_cannot_lift_sorkin_to_1e_5(self):
        _, _, sigma0 = sorkin_holographic()
        for r in (0.0, 1.5, 3.0, 10.0):
            assert residual_soft_map(sigma0, r=r) < 1e-50

    def test_r_needed_for_sorkin_to_1e_5(self):
        _, _, sigma0 = sorkin_holographic()
        r = r_needed_for_target(sigma0, 1e-5)
        # r ~ 64
        assert 60 < r < 70
        # invert
        assert residual_soft_map(sigma0, r=r) == pytest.approx(1e-5, rel=1e-10)

    def test_freeze_and_late_stretch_defaults(self):
        # G_F=G_U=1 by default in residual_soft_map
        assert residual_soft_map(1e-5, r=0.0) == pytest.approx(1e-5)


class TestNoFreeLunchCombined:
    """Cross-rules: path + soft open still fail for Sorkin."""

    def test_stack_path_and_soft_open_on_sorkin(self):
        _, _, sigma0 = sorkin_holographic()
        # first apply soft open r=1.5
        s1 = residual_soft_map(sigma0, r=1.5)
        slip = slip_deviation(1.0, s1, 0.8)
        chi = comoving_distance_mpc(1.5)
        rms = rms_incoherent(slip, n_patches(chi, 1.0))
        assert rms < 1e-54

    def test_mesoscopic_seed_with_soft_open_reaches_band(self):
        s1 = residual_soft_map(1e-5, r=0.0)  # G=1
        assert 1e-5 <= s1 <= 1.5e-4 or s1 == pytest.approx(1e-5)
        s20 = residual_soft_map(1e-5, r=1.5)
        # e^{3}*1e-5 ~ 2e-4, near DESI ceiling
        assert 1e-4 < s20 < 5e-4
