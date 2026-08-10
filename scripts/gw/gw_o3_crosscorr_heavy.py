#!/usr/bin/env python3
"""
Heavy tensor-channel experiment on real O3 open data (GWOSC).

Data: 4096 s, 4 kHz, H1 + L1 around GW190521 (public).
Does:
  - segment Welch autospectra + H1×L1 cross-spectrum
  - mean coherence and cross-power in the SGWB band
  - crude isotropic SGWB SNR / Ω_GW scale from this stretch (not a full O3 result)
  - literature anchors: O3 Ω_GW, extra polarisations, PTA

Not:
  - DESI residual sigma_X
  - claim that ell_* is measured in strain
  - full LVK SGWB pipeline (no DQ flags, no optimal filters library)

Run:
  python scripts/gw/download_o3_long.py   # if needed
  python scripts/gw/gw_o3_crosscorr_heavy.py
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import h5py
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "gw_public" / "o3"
OUT = ROOT / "results" / "gw_channel"
CATALOG = ROOT / "data" / "gw_public" / "GWTC-3-confident.json"

H1_FILE = DATA / "H-H1_GWOSC_4KHZ_R1-1242440920-4096.hdf5"
L1_FILE = DATA / "L-L1_GWOSC_4KHZ_R1-1242440920-4096.hdf5"

# Hanford–Livingston separation (m); light travel ~0.01 s
D_HL_M = 3.002e6
C_M_S = 2.99792458e8

# Literature anchors
O3_OMEGA_REF = 5.8e-9  # O3 isotropic PLI / α=0 class OOM, arXiv:2101.12130
O3_FREF = 25.0
# Extra polarisations: LVK searches (order-of-magnitude constraints, cite papers)
# Abbott et al. GWTC polarisation / scalar-vector papers — no detection of non-GR modes
# Representative: scalar breathing / longitudinal searches null at O3 sensitivity
POLARISATION_NOTE = (
    "LVK O3: no evidence for non-tensor polarisations in catalogued events "
    "(see e.g. arXiv:2112.06861 and follow-ups). This script does not re-run those searches."
)
# PTA
PTA_HC = 2.4e-15  # NANOGrav 15yr A_GWB ~ few×10^{-15} at f=1/yr class; arXiv:2306.16213
PTA_ARXIV = "2306.16213"


def load_strain(path: Path) -> tuple[np.ndarray, float, int]:
    with h5py.File(path, "r") as f:
        x = np.asarray(f["strain/Strain"][()], dtype=np.float64)
        dur = float(f["meta/Duration"][()])
        gps = int(f["meta/GPSstart"][()])
    return x, x.size / dur, gps


def highpass(x: np.ndarray, fs: float, fmin: float = 15.0) -> np.ndarray:
    n = x.size
    X = np.fft.rfft(x - np.mean(x))
    f = np.fft.rfftfreq(n, d=1.0 / fs)
    X[f < fmin] = 0
    return np.fft.irfft(X, n=n)


def overlap_gamma_hl(f: np.ndarray) -> np.ndarray:
    """Rough HL overlap reduction (order-of-magnitude, not full Earth response)."""
    # isotropic unpolarised SGWB: γ(f) ≈ j0(2π f d/c) with geometric factor ~1/5…1
    # Use spherical Bessel j0 = sin(x)/x, times ~0.5 for HL orientation OOM
    x = 2.0 * math.pi * f * D_HL_M / C_M_S
    j0 = np.ones_like(f)
    m = x != 0
    j0[m] = np.sin(x[m]) / x[m]
    return 0.5 * j0


def segment_spectra(
    h: np.ndarray, l: np.ndarray, fs: float, seg_s: float = 64.0
) -> dict:
    nseg = int(seg_s * fs)
    nseg = min(nseg, h.size // 8)
    step = nseg // 2
    window = np.hanning(nseg)
    w2 = np.sum(window**2)
    phh, pll, phl = [], [], []
    for i in range(0, h.size - nseg + 1, step):
        wh = (h[i : i + nseg] - np.mean(h[i : i + nseg])) * window
        wl = (l[i : i + nseg] - np.mean(l[i : i + nseg])) * window
        Hh = np.fft.rfft(wh)
        Ll = np.fft.rfft(wl)
        phh.append(np.abs(Hh) ** 2)
        pll.append(np.abs(Ll) ** 2)
        phl.append(Hh * np.conjugate(Ll))
    phh = np.mean(np.stack(phh), axis=0) / (w2 * fs)
    pll = np.mean(np.stack(pll), axis=0) / (w2 * fs)
    phl = np.mean(np.stack(phl), axis=0) / (w2 * fs)
    freqs = np.fft.rfftfreq(nseg, d=1.0 / fs)
    coh = (np.abs(phl) ** 2) / (phh * pll + 1e-300)
    return {
        "freqs": freqs,
        "P_HH": phh,
        "P_LL": pll,
        "P_HL": phl,
        "coh": coh,
        "n_segments": 1 + (h.size - nseg) // step,
        "seg_s": nseg / fs,
    }


def omega_from_cross(
    freqs: np.ndarray,
    p_hl: np.ndarray,
    p_hh: np.ndarray,
    p_ll: np.ndarray,
    fmin: float = 20.0,
    fmax: float = 90.0,
) -> dict:
    """
    Crude isotropic SGWB estimator on one baseline.
    S_h(f) ~ Re(P_HL) / γ(f); Ω_GW(f) = (2 π² / 3 H0²) f³ S_h(f).
    H0 = 67.4 km/s/Mpc in SI.
    """
    H0 = 67.4 * 1000.0 / (3.085677581e22)  # 1/s
    m = (freqs >= fmin) & (freqs <= fmax) & (freqs > 0)
    f = freqs[m]
    gamma = overlap_gamma_hl(f)
    # avoid zeros of γ
    good = np.abs(gamma) > 0.05
    f, gamma = f[good], gamma[good]
    re_c = np.real(p_hl[m][good])
    sh = re_c / gamma  # strain PSD of common signal (can be ± noise)
    omega = (2.0 * math.pi**2 / (3.0 * H0**2)) * (f**3) * sh

    # variance proxy: noise-only cross variance ~ 0.5 P_H P_L / (T df) per bin
    # We report median |Ω| and a noise-only scale from autospectra
    pnn = 0.5 * np.sqrt(p_hh[m][good] * p_ll[m][good]) / (np.abs(gamma) + 1e-12)
    omega_noise = (2.0 * math.pi**2 / (3.0 * H0**2)) * (f**3) * pnn

    # broadband: mean Ω weighted by 1/var
    w = 1.0 / (omega_noise**2 + 1e-60)
    omega_hat = float(np.sum(w * omega) / np.sum(w))
    omega_sig = float(1.0 / math.sqrt(np.sum(w)))
    return {
        "fmin": fmin,
        "fmax": fmax,
        "Omega_hat": omega_hat,
        "Omega_noise_scale": omega_sig,
        "Omega_abs_median_bins": float(np.median(np.abs(omega))),
        "n_bins": int(f.size),
        "SNR_proxy": float(omega_hat / omega_sig) if omega_sig > 0 else 0.0,
    }


def catalog_stats(path: Path) -> dict:
    if not path.exists():
        return {}
    d = json.loads(path.read_text())
    events = d.get("events") or {}
    snrs = []
    for e in events.values():
        s = e.get("network_matched_filter_snr")
        if s is not None:
            snrs.append(float(s))
    return {
        "n_events_GWTC3_confident_json": len(events),
        "median_network_SNR": float(np.median(snrs)) if snrs else None,
        "max_network_SNR": float(np.max(snrs)) if snrs else None,
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    if not H1_FILE.exists() or not L1_FILE.exists():
        raise SystemExit(f"Missing O3 files under {DATA}. Download first.")

    h, fs, gps = load_strain(H1_FILE)
    l, fs2, _ = load_strain(L1_FILE)
    assert abs(fs - fs2) < 1e-6
    n = min(h.size, l.size)
    h, l = highpass(h[:n], fs), highpass(l[:n], fs)

    sp = segment_spectra(h, l, fs, seg_s=64.0)
    f = sp["freqs"]
    m_sgwb = (f >= 20.0) & (f <= 90.0)
    coh_mean = float(np.mean(sp["coh"][m_sgwb]))
    asd_h_100 = float(np.sqrt(sp["P_HH"][np.argmin(np.abs(f - 100.0))]))
    asd_l_100 = float(np.sqrt(sp["P_LL"][np.argmin(np.abs(f - 100.0))]))

    om = omega_from_cross(f, sp["P_HL"], sp["P_HH"], sp["P_LL"])

    cat = catalog_stats(CATALOG)

    # Band-limited RMS of cross-filtered residual (noise)
    rms_h = float(np.sqrt(np.mean(h**2)))
    rms_l = float(np.sqrt(np.mean(l**2)))

    summary = {
        "data": {
            "files": [H1_FILE.name, L1_FILE.name],
            "event_window": "GW190521 4096 s open data (O3)",
            "gps_start": gps,
            "duration_s": n / fs,
            "fs_Hz": fs,
            "baseline": "H1–L1 ~3000 km laser interferometers",
            "source": "GWOSC",
        },
        "measurements": {
            "n_welch_segments": sp["n_segments"],
            "segment_s": sp["seg_s"],
            "ASD_H1_100Hz": asd_h_100,
            "ASD_L1_100Hz": asd_l_100,
            "mean_coherence_20_90Hz": coh_mean,
            "rms_highpass_H1": rms_h,
            "rms_highpass_L1": rms_l,
            "Omega_GW_hat_this_stretch": om["Omega_hat"],
            "Omega_GW_noise_scale_this_stretch": om["Omega_noise_scale"],
            "Omega_SNR_proxy": om["SNR_proxy"],
            "Omega_band_Hz": [om["fmin"], om["fmax"]],
        },
        "literature": {
            "O3_Omega_GW_upper_OOM": O3_OMEGA_REF,
            "O3_f_ref_Hz": O3_FREF,
            "O3_arxiv": "2101.12130",
            "extra_polarisations": POLARISATION_NOTE,
            "polarisation_arxiv": "2112.06861",
            "PTA_hc_OOM": PTA_HC,
            "PTA_arxiv": PTA_ARXIV,
        },
        "catalog": cat,
        "sister_residual_NOT_same_operator": {
            "sigma_free": 8.5e-5,
            "sigma_X_DESI": 2.5e-2,
            "note": "Do not equate with Omega_GW or strain.",
        },
        "verdict": {
            "this_stretch_Omega_consistent_with_noise": abs(om["SNR_proxy"]) < 3,
            "full_O3_limit_stronger_by_factor_OOM": (
                abs(om["Omega_noise_scale"]) / O3_OMEGA_REF
                if O3_OMEGA_REF > 0
                else None
            ),
            "point": (
                "Tensor channel is open and measured; isotropic DE residual is a different operator. "
                "SDiff does not cancel TT GW. Extra polarisations remain a literature null, not re-derived here."
            ),
        },
    }

    # save coherence curve downsample
    step = max(1, f.size // 1500)
    np.savetxt(
        OUT / "o3_coherence_H1L1.txt",
        np.column_stack([f[::step], sp["coh"][::step]]),
        header="freq_Hz  mean_coherence_H1L1_O3_4096s",
    )
    (OUT / "O3_HEAVY_SUMMARY.json").write_text(json.dumps(summary, indent=2) + "\n")

    lines = [
        "O3 H1–L1 cross-correlation (real GWOSC open data)",
        "=" * 55,
        f"Files: {H1_FILE.name}",
        f"       {L1_FILE.name}",
        f"Duration: {n/fs:.0f} s @ {fs:.0f} Hz  segments: {sp['n_segments']} × {sp['seg_s']:.0f} s",
        f"ASD @ 100 Hz: H1={asd_h_100:.3e}  L1={asd_l_100:.3e}  1/sqrt(Hz)",
        f"Mean coherence 20–90 Hz: {coh_mean:.4f}",
        "",
        "Crude isotropic Ω_GW estimator (this stretch only):",
        f"  Ω_hat        = {om['Omega_hat']:.3e}",
        f"  noise scale  = {om['Omega_noise_scale']:.3e}",
        f"  SNR proxy    = {om['SNR_proxy']:.2f}  (|SNR|<3 ⇒ noise-like)",
        f"  Full O3 published Ω ≲ {O3_OMEGA_REF:.1e} @ {O3_FREF} Hz  [arXiv:2101.12130]",
        f"  This stretch weaker by ~{summary['verdict']['full_O3_limit_stronger_by_factor_OOM']:.0f}× (expected)",
        "",
        "Extra polarisations: " + POLARISATION_NOTE,
        f"PTA h_c ~ {PTA_HC:.1e}  [arXiv:{PTA_ARXIV}]",
        "",
        f"GWTC-3 catalog events in local JSON: {cat.get('n_events_GWTC3_confident_json')}",
        f"  median network SNR: {cat.get('median_network_SNR')}",
        "",
        "NOT sigma_X. NOT ell_*. Tensor interferometry, long baseline H1–L1.",
        f"Wrote {OUT/'O3_HEAVY_SUMMARY.json'}",
    ]
    text = "\n".join(lines) + "\n"
    (OUT / "O3_HEAVY_SUMMARY.txt").write_text(text)
    print(text)


if __name__ == "__main__":
    main()
