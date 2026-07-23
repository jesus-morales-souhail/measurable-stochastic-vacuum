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
    amplification_gap,
    comoving_distance_mpc,
    ell_for_target_sigma,
    ell_mpc_for_sigma,
    hubble_radius_m,
    hubble_radius_mpc,
    n_eff,
    n_patches,
    r8_mpc,
    residual_soft_map,
    rho_x_over_rho_m,
    rms_incoherent,
    r_needed_for_target,
    sigma_for_cell_mpc,
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


class TestPastLightCone:
    """Past null-cone accumulation atlas consistency."""

    def test_C_equals_one_identity(self):
        s, chi, ell = 1e-5, 4482.0, 2.065
        n = n_patches(chi, ell)
        assert rms_incoherent(s, n) == pytest.approx(s * math.sqrt(n), rel=1e-12)

    def test_np_a_boost_order_40_to_60(self):
        L_H, _, _ = sorkin_holographic()
        mpc = 3.085677581e22
        ell = ell_for_target_sigma(1e-5, L_H, 3) / mpc
        chi = comoving_distance_mpc(1.5)
        boost = math.sqrt(n_patches(chi, ell))
        assert 40 < boost < 55

    def test_np_b_rms_frontier_not_euclid_easy(self):
        L_H, _, _ = sorkin_holographic()
        mpc = 3.085677581e22
        s0 = 5e-6
        sres = residual_soft_map(s0, r=1.5)
        ell = ell_for_target_sigma(s0, L_H, 3) / mpc
        slip = slip_deviation(1.0, sres, 0.8)
        rms = rms_incoherent(slip, n_patches(comoving_distance_mpc(1.5), ell))
        assert sres <= 1.5e-4
        assert 1e-3 < rms < 1e-2
        assert rms < 0.03  # still below indicative Euclid floor

    def test_deeper_source_increases_rms(self):
        L_H, _, _ = sorkin_holographic()
        mpc = 3.085677581e22
        ell = ell_for_target_sigma(1e-5, L_H, 3) / mpc
        slip = slip_deviation(1.0, 1e-5, 0.5)
        r1 = rms_incoherent(slip, n_patches(comoving_distance_mpc(1.0), ell))
        r2 = rms_incoherent(slip, n_patches(comoving_distance_mpc(2.0), ell))
        assert r2 > r1


class TestObservableWall:
    """Einstein + Morales slip wall and detectability inverse."""

    def test_wall_formula_z0(self):
        # |g-1| = 2*1.5e-4*(0.685/0.315) = 2*1.5e-4*2.1746...
        s = slip_deviation(1.0, 1.5e-4, 0.0, 1.0)
        expected = 2.0 * 1.5e-4 * (0.685 / 0.315)
        assert s == pytest.approx(expected, rel=1e-12)
        assert 6e-4 < s < 7e-4

    def test_wall_decreases_with_z(self):
        assert slip_deviation(1.0, 1.5e-4, 0.0) > slip_deviation(1.0, 1.5e-4, 1.0)

    def test_detectability_threshold_exceeds_desi_ceiling(self):
        # sigma_X needed for |g-1| = 5*0.03 at z=0, eps=1, dm=1
        S = 5 * 0.03
        ratio = 0.685 / 0.315
        sx_need = S / (2.0 * ratio)
        assert sx_need > 0.03
        assert sx_need / 1.5e-4 > 200  # shielding factor

    def test_self_shielding_inequality_euclid_floor(self):
        s_max = slip_deviation(1.0, 1.5e-4, 0.0)
        sigma_exp = 0.03
        assert s_max < sigma_exp / 10  # strongly shielded


class TestSimpleAsLambda:
    """Blackboard reduction: RMS ~ sigma**(2/3) for d=3."""

    def test_ell_from_sigma_d3(self):
        L_H, _, _ = sorkin_holographic()
        sigma = 1e-5
        ell = ell_for_target_sigma(sigma, L_H, 3)
        assert sigma_from_count(ell, L_H, 3) == pytest.approx(sigma, rel=1e-12)

    def test_simple_power_matches_structure(self):
        # ell = L * sigma**(2/3); sqrt(L/ell) * sigma = sigma * sigma**(-1/3) = sigma**(2/3)
        sigma = 1e-5
        L = 1.0
        ell = L * sigma ** (2.0 / 3.0)
        rms_geom = sigma * math.sqrt(L / ell)
        assert rms_geom == pytest.approx(sigma ** (2.0 / 3.0), rel=1e-12)

    def test_sorkin_simple_rms_invisible(self):
        _, _, s0 = sorkin_holographic()
        assert s0 ** (2.0 / 3.0) < 1e-40


class TestNarrowPath:
    """DESI-safe mesoscopic architecture (NP-A / NP-B)."""

    def test_d3_cell_for_1e_5_is_cluster_scale(self):
        L_H, _, _ = sorkin_holographic()
        mpc = 3.085677581e22
        ell_mpc = ell_for_target_sigma(1e-5, L_H, 3) / mpc
        assert 1.5 < ell_mpc < 3.0

    def test_user_chain_r15_exceeds_desi_ceiling(self):
        """sigma0=1e-5 and r=1.5 => sigma_res > 1.5e-4 (must be clipped to NP-B)."""
        sres = residual_soft_map(1e-5, r=1.5)
        assert sres > 1.5e-4


class TestTwoAmplificationGaps:
    """Do not mix Euclid-target 10^56 with DESI-ceiling 10^57."""

    def test_euclid_gap_is_about_10_to_56(self):
        g = amplification_gap(1e-5)
        assert 5e55 < g < 2e56
        assert math.log10(g) == pytest.approx(55.93, abs=0.05)

    def test_desi_gap_is_about_10_to_57(self):
        g = amplification_gap(1.5e-4)
        assert 5e56 < g < 3e57
        assert math.log10(g) == pytest.approx(57.10, abs=0.05)

    def test_desi_over_euclid_is_exactly_15(self):
        assert amplification_gap(1.5e-4) / amplification_gap(1e-5) == pytest.approx(15.0)

    def test_slip_decreases_with_z_at_fixed_delta(self):
        """(1+z)^3 is in the denominator of (W)."""
        s0 = slip_deviation(1.0, 1.5e-4, 0.0, 1.0)
        s1 = slip_deviation(1.0, 1.5e-4, 1.0, 1.0)
        assert s0 > s1
        assert s0 == pytest.approx(6.52e-4, rel=0.02)


class TestLensingRealDataCompare:
    """Anchors from papers/lensing-rms-forecast-real-data.md (published numbers)."""

    def test_maus_error_above_np_b_path_rms(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        from lensing_rms_real_data_compare import (  # noqa: E402
            MAUS_GAMMA_ERR,
            programme_path_rms,
        )

        np_b = programme_path_rms("NP-B", 5e-6, 1.5)
        assert 3e-3 < np_b["rms_path"] < 6e-3
        assert MAUS_GAMMA_ERR / np_b["rms_path"] > 15  # ~25×

    def test_sakr_5pct_still_above_np_b(self):
        from lensing_rms_real_data_compare import (  # noqa: E402
            SAKR_ETA_CONST_FRAC,
            programme_path_rms,
        )

        np_b = programme_path_rms("NP-B", 5e-6, 1.5)
        assert SAKR_ETA_CONST_FRAC / np_b["rms_path"] > 8  # ~11×

    def test_stage4_mbias_not_equal_to_path_rms_claim(self):
        """m~2e-3 is same OOM as NP-B numerically — test documents the hazard."""
        from lensing_rms_real_data_compare import (  # noqa: E402
            STAGE4_M_MULT_BIAS_OOM,
            programme_path_rms,
        )

        np_b = programme_path_rms("NP-B", 5e-6, 1.5)
        # same decade; must NOT be used as detection (paper N-L4)
        assert 0.2 < STAGE4_M_MULT_BIAS_OOM / np_b["rms_path"] < 1.0

    def test_published_anchors_match_cited_values(self):
        from lensing_rms_real_data_compare import (  # noqa: E402
            DESI_MG_SIGMA0_ERR,
            MAUS_GAMMA,
            MAUS_GAMMA_ERR,
            SAKR_ETA_CONST_FRAC,
            SAKR_ETA_ZK_FRAC,
        )

        assert MAUS_GAMMA == pytest.approx(1.17)
        assert MAUS_GAMMA_ERR == pytest.approx(0.11)
        assert SAKR_ETA_CONST_FRAC == pytest.approx(0.05)
        assert SAKR_ETA_ZK_FRAC == pytest.approx(0.30)
        assert DESI_MG_SIGMA0_ERR == pytest.approx(0.045)


class TestR1OpenKernelScales:
    """
    Scale anchors for papers/r1-open-kernel.md.
    Arithmetic only — does not claim ell_* = R_8 or a derivation.
    """

    def test_r8_definition(self):
        # H0=67.4 => h=0.674 => R_8 = 8/0.674 ≈ 11.87 Mpc
        assert r8_mpc() == pytest.approx(8.0 / 0.674, rel=1e-12)
        assert 11.5 < r8_mpc() < 12.2

    def test_hubble_radius_mpc_consistent(self):
        L_m = hubble_radius_m()
        mpc = 3.085677581e22
        assert hubble_radius_mpc() == pytest.approx(L_m / mpc, rel=1e-12)

    def test_sigma_for_r8_d3_near_desi_ceiling_order(self):
        """If ell_*=R_8 and d=3, sigma is O(1e-4) — landscape fact, not a fit."""
        s = sigma_for_cell_mpc(r8_mpc(), 3)
        assert 5e-5 < s < 3e-4
        # published OOM in r1-open-kernel.md
        assert s == pytest.approx(1.38e-4, rel=0.05)

    def test_sigma_for_r8_d4_near_1e_5_band(self):
        s = sigma_for_cell_mpc(r8_mpc(), 4)
        assert 3e-6 < s < 2e-5

    def test_ell_for_desi_ceiling_d3_near_r8(self):
        """d=3 inverse at DESI ceiling lands near R_8 (scale coincidence)."""
        ell = ell_mpc_for_sigma(1.5e-4, 3)
        R8 = r8_mpc()
        assert ell == pytest.approx(12.557, rel=0.01)
        assert abs(ell / R8 - 1.0) < 0.10  # ~5.8%

    def test_r8_proximity_is_specific_to_d3(self):
        """Honesty lock: d=2 and d=4 at DESI ceiling are FAR from R_8."""
        R8 = r8_mpc()
        for d, min_frac in ((2, 0.5), (4, 1.0)):
            ell = ell_mpc_for_sigma(1.5e-4, d)
            assert abs(ell / R8 - 1.0) > min_frac

    def test_ell_for_1e_5_d4_order_of_structure_scale(self):
        """d=4 at 1e-5 is O(10 Mpc); not the same claim as d=3@DESI ceiling."""
        ell = ell_mpc_for_sigma(1e-5, 4)
        assert 12.0 < ell < 16.0

    def test_planck_not_near_r8(self):
        """Sanity: Sorkin seed is not a mesoscopic R8 story."""
        _, _, s0 = sorkin_holographic()
        assert s0 < 1e-50
        assert sigma_for_cell_mpc(r8_mpc(), 3) / s0 > 1e50

    def test_np_b_on_desi_ceiling(self):
        """sigma0 = 1.5e-4 / e^{3} keeps residual on the DESI ceiling."""
        g = soft_squeeze_gain(1.5)
        s0 = 1.5e-4 / g
        sres = residual_soft_map(s0, r=1.5)
        assert sres == pytest.approx(1.5e-4, rel=1e-10)

    def test_np_a_path_rms_order(self):
        """G_O=1, sigma0=1e-5, d=3 cell: path RMS ~ few x 10^{-4}."""
        L_H, _, _ = sorkin_holographic()
        mpc = 3.085677581e22
        ell_mpc = ell_for_target_sigma(1e-5, L_H, 3) / mpc
        sres = residual_soft_map(1e-5, r=0.0)
        slip = slip_deviation(1.0, sres, 0.8)
        chi = comoving_distance_mpc(1.5)
        rms = rms_incoherent(slip, n_patches(chi, ell_mpc))
        assert 1e-4 < rms < 1e-3

    def test_np_b_path_rms_order(self):
        """DESI-safe soft open: path RMS ~ few x 10^{-3}."""
        L_H, _, _ = sorkin_holographic()
        mpc = 3.085677581e22
        g = soft_squeeze_gain(1.5)
        s0 = 1.0e-4 / g  # residual 1e-4 < ceiling
        ell_mpc = ell_for_target_sigma(s0, L_H, 3) / mpc
        sres = residual_soft_map(s0, r=1.5)
        assert sres <= 1.5e-4
        slip = slip_deviation(1.0, sres, 0.8)
        rms = rms_incoherent(slip, n_patches(comoving_distance_mpc(1.5), ell_mpc))
        assert 1e-3 < rms < 1e-2

    def test_naive_product_is_not_rms(self):
        L_H, _, _ = sorkin_holographic()
        mpc = 3.085677581e22
        s0, r = 1e-5, 1.5
        ell_mpc = ell_for_target_sigma(s0, L_H, 3) / mpc
        sres = residual_soft_map(s0, r=r)
        slip = slip_deviation(1.0, sres, 0.8)
        n = n_patches(comoving_distance_mpc(1.5), ell_mpc)
        rms = rms_incoherent(slip, n)
        naive = s0 * soft_squeeze_gain(r) * math.sqrt(n)
        assert rms != pytest.approx(naive, rel=0.01)
        assert rms < naive  # prefactor 2(ρX/ρm)/δm < 1 at z=0.8 typically... actually ~1.5e-4*sqrtN vs 2e-4*sqrtN
