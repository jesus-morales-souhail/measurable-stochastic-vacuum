#!/usr/bin/env python3
"""
Real LIGO strain experiment (public GWOSC data).

What this is:
  - Load H1 and L1 4 kHz open data around GW150914
  - Estimate amplitude spectral density (ASD) per detector
  - Coherence and cross-spectrum between the two interferometers (long baseline)
  - Band-limited RMS strain in 20-300 Hz
  - Honest comparison table: published O3 SGWB / PTA numbers vs our residual map

What this is not:
  - A measurement of DESI residual sigma_X
  - A claim that ell_*=R_nl is seen in LIGO
  - A scalar-polarisation search (needs a dedicated pipeline)

SDiff / unimodular note: isotropic vacuum stress is not the same operator as
TT tensor strain. This script only characterises the *tensor* data channel.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import h5py
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "gw_public"
OUT = ROOT / "results" / "gw_channel"

# Published anchors (literature; not re-derived here)
# LIGO/Virgo/KAGRA O3 stochastic background (isotropic), Ω_GW upper limits
# Abbott et al., Phys. Rev. D 104, 022004 (2021); arXiv:2101.12130
# Order-of-magnitude: Ω_GW ≲ few × 10^{-9} near 25 Hz (power-law integrated / α=0 class)
O3_OMEGA_GW_OOM = 5e-9
O3_F_REF_HZ = 25.0
O3_ARXIV = "2101.12130"

# PTA nHz stochastic background (Hellings–Downs) — NANOGrav 15 yr evidence class
# Agazie et al., ApJL 951 L8 (2023); arXiv:2306.16213
# Characteristic strain scale h_c ~ 10^{-15} at f ~ 1/yr (order of magnitude)
PTA_HC_OOM = 1e-15
PTA_F_YR = 1.0  # cycles per year
PTA_ARXIV = "2306.16213"

# Sister residual programme (counting + DESI) — different operator
SIGMA_FREE = 8.5e-5
SIGMA_X_DESI = 2.5e-2
RMS_PATH_FREE = 1.45e-3


def load_strain(path: Path) -> tuple[np.ndarray, float, int]:
    with h5py.File(path, "r") as f:
        strain = np.asarray(f["strain/Strain"][()], dtype=float)
        duration = float(f["meta/Duration"][()])
        gps = int(f["meta/GPSstart"][()])
    fs = strain.size / duration
    return strain, fs, gps


def welch_asd(x: np.ndarray, fs: float, nperseg: int = 4096) -> tuple[np.ndarray, np.ndarray]:
    """One-sided ASD ~ 1/sqrt(Hz) via Welch PSD."""
    nperseg = min(nperseg, x.size // 4)
    step = nperseg // 2
    window = np.hanning(nperseg)
    wnorm = np.sum(window**2)
    segs = []
    for start in range(0, x.size - nperseg + 1, step):
        seg = (x[start : start + nperseg] - np.mean(x[start : start + nperseg])) * window
        segs.append(np.fft.rfft(seg))
    specs = np.mean(np.abs(np.stack(segs, axis=0)) ** 2, axis=0)
    # PSD (strain^2 / Hz); rfft frequency resolution
    df = fs / nperseg
    psd = specs / (wnorm * fs)
    # one-sided: double positive freqs except DC/Nyquist handled by rfft scaling
    asd = np.sqrt(psd)
    freqs = np.fft.rfftfreq(nperseg, d=1.0 / fs)
    return freqs, asd


def cross_coherence(
    x: np.ndarray, y: np.ndarray, fs: float, nperseg: int = 4096
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    nperseg = min(nperseg, x.size // 4, y.size // 4)
    step = nperseg // 2
    window = np.hanning(nperseg)
    wnorm = np.sum(window**2)
    xs, ys = [], []
    for start in range(0, min(x.size, y.size) - nperseg + 1, step):
        sx = (x[start : start + nperseg] - np.mean(x[start : start + nperseg])) * window
        sy = (y[start : start + nperseg] - np.mean(y[start : start + nperseg])) * window
        xs.append(np.fft.rfft(sx))
        ys.append(np.fft.rfft(sy))
    X = np.stack(xs, axis=0)
    Y = np.stack(ys, axis=0)
    pxx = np.mean(np.abs(X) ** 2, axis=0) / (wnorm * fs)
    pyy = np.mean(np.abs(Y) ** 2, axis=0) / (wnorm * fs)
    pxy = np.mean(X * np.conjugate(Y), axis=0) / (wnorm * fs)
    coh = (np.abs(pxy) ** 2) / (pxx * pyy + 1e-300)
    freqs = np.fft.rfftfreq(nperseg, d=1.0 / fs)
    return freqs, coh, pxy


def _bandpass_series(x: np.ndarray, fs: float, fmin: float, fmax: float) -> np.ndarray:
    n = x.size
    x0 = x - np.mean(x)
    X = np.fft.rfft(x0)
    f = np.fft.rfftfreq(n, d=1.0 / fs)
    mask = (f >= fmin) & (f <= fmax)
    Xf = np.zeros_like(X)
    Xf[mask] = X[mask]
    return np.fft.irfft(Xf, n=n)


def band_rms(x: np.ndarray, fs: float, fmin: float, fmax: float) -> float:
    """RMS of bandpass via FFT brick-wall (simple, for OOM)."""
    y = _bandpass_series(x, fs, fmin, fmax)
    return float(np.sqrt(np.mean(y**2)))


def asd_at(freqs: np.ndarray, asd: np.ndarray, f0: float) -> float:
    i = int(np.argmin(np.abs(freqs - f0)))
    return float(asd[i])


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    h1_path = DATA / "H-H1_GWOSC_4KHZ_R1-1126259447-32.hdf5"
    l1_path = DATA / "L-L1_GWOSC_4KHZ_R1-1126259447-32.hdf5"
    if not h1_path.exists() or not l1_path.exists():
        raise SystemExit(
            "Missing strain files. Run: python scripts/gw/download_gwosc_strain.py"
        )

    h1, fs_h, gps = load_strain(h1_path)
    l1, fs_l, _ = load_strain(l1_path)
    assert abs(fs_h - fs_l) < 1e-6
    fs = fs_h
    n = min(h1.size, l1.size)
    h1, l1 = h1[:n], l1[:n]

    # Whitening-free ASD (raw open data includes calibration; event in the middle)
    f_h, asd_h = welch_asd(h1, fs)
    f_l, asd_l = welch_asd(l1, fs)
    f_c, coh, pxy = cross_coherence(h1, l1, fs)

    # Event GPS 1126259462.4; file starts 1126259447 → ~15.4 s into the stretch
    # Peak on raw strain is low-frequency noise; use 35–350 Hz for the chirp band.
    t_event = 1126259462.4 - gps
    i0 = int(max(0, (t_event - 0.15) * fs))
    i1 = int(min(n, (t_event + 0.05) * fs))
    h1_bp = _bandpass_series(h1, fs, 35.0, 350.0)
    l1_bp = _bandpass_series(l1, fs, 35.0, 350.0)
    peak_h = float(np.max(np.abs(h1_bp[i0:i1])))
    peak_l = float(np.max(np.abs(l1_bp[i0:i1])))

    rms_20_300_h = band_rms(h1, fs, 20.0, 300.0)
    rms_20_300_l = band_rms(l1, fs, 20.0, 300.0)

    # Mean coherence in 40-200 Hz (where BBH signal lives; noise usually incoherent)
    m = (f_c >= 40.0) & (f_c <= 200.0)
    coh_mid = float(np.mean(coh[m]))

    summary = {
        "data": {
            "source": "GWOSC open data",
            "event": "GW150914",
            "gps_start": gps,
            "duration_s": n / fs,
            "sample_rate_hz": fs,
            "detectors": ["H1", "L1"],
            "baseline": "Hanford–Livingston ~3000 km (laser interferometers)",
            "doi": "https://doi.org/10.7935/82H3-HH23",
        },
        "measurements_this_run": {
            "ASD_H1_at_100Hz_strain_per_sqrtHz": asd_at(f_h, asd_h, 100.0),
            "ASD_L1_at_100Hz_strain_per_sqrtHz": asd_at(f_l, asd_l, 100.0),
            "ASD_H1_at_25Hz": asd_at(f_h, asd_h, 25.0),
            "ASD_L1_at_25Hz": asd_at(f_l, asd_l, 25.0),
            "band_RMS_20_300Hz_H1": rms_20_300_h,
            "band_RMS_20_300Hz_L1": rms_20_300_l,
            "peak_abs_strain_near_event_H1_band_35_350Hz": peak_h,
            "peak_abs_strain_near_event_L1_band_35_350Hz": peak_l,
            "mean_coherence_H1L1_40_200Hz": coh_mid,
        },
        "literature_anchors": {
            "O3_Omega_GW_OOM": O3_OMEGA_GW_OOM,
            "O3_f_ref_Hz": O3_F_REF_HZ,
            "O3_arxiv": O3_ARXIV,
            "PTA_hc_OOM": PTA_HC_OOM,
            "PTA_arxiv": PTA_ARXIV,
        },
        "sister_residual_programme_NOT_same_operator": {
            "sigma_free_if_ell_star_R_nl": SIGMA_FREE,
            "sigma_X_DESI_ceiling": SIGMA_X_DESI,
            "RMS_path_free_OOM": RMS_PATH_FREE,
            "warning": (
                "Do not equate sigma_X or sigma_free with LIGO strain. "
                "Isotropic DE residual ≠ TT tensor h."
            ),
        },
        "interpretation": {
            "channel": "tensor interferometer strain (GW)",
            "baseline": "Earth-scale (H1–L1), not VLBI radio; same idea: long baseline interferometry",
            "SDiff": "Kills isotropic T~g_μν vacuum noise, not TT gravitational waves",
            "this_run": (
                "Characterises real public strain and H1–L1 coherence; "
                "does not measure BAO residual amplitude."
            ),
        },
    }

    # Save ASD tables (downsample for repo size)
    step = max(1, f_h.size // 2000)
    np.savetxt(
        OUT / "asd_H1.txt",
        np.column_stack([f_h[::step], asd_h[::step]]),
        header="freq_Hz  ASD_strain_per_sqrtHz  (H1, Welch, GW150914 open data)",
    )
    np.savetxt(
        OUT / "asd_L1.txt",
        np.column_stack([f_l[::step], asd_l[::step]]),
        header="freq_Hz  ASD_strain_per_sqrtHz  (L1, Welch, GW150914 open data)",
    )
    np.savetxt(
        OUT / "coherence_H1L1.txt",
        np.column_stack([f_c[::step], coh[::step]]),
        header="freq_Hz  coherence_H1L1",
    )
    (OUT / "SUMMARY.json").write_text(json.dumps(summary, indent=2) + "\n")

    lines = [
        "GW channel — real LIGO open data (GWOSC)",
        "=" * 50,
        f"Event: GW150914  GPS start {gps}  fs={fs:.0f} Hz  N={n}",
        f"Baseline: H1–L1 laser interferometers (~3000 km)",
        "",
        "ASD @ 100 Hz [1/sqrt(Hz)]:",
        f"  H1  {summary['measurements_this_run']['ASD_H1_at_100Hz_strain_per_sqrtHz']:.3e}",
        f"  L1  {summary['measurements_this_run']['ASD_L1_at_100Hz_strain_per_sqrtHz']:.3e}",
        f"Band RMS 20–300 Hz: H1={rms_20_300_h:.3e}  L1={rms_20_300_l:.3e}",
        f"Peak |strain| near merger (35–350 Hz): H1={peak_h:.3e}  L1={peak_l:.3e}",
        f"Mean coherence H1–L1 (40–200 Hz): {coh_mid:.4f}",
        "",
        "Literature (not from this 32 s stretch):",
        f"  O3 isotropic SGWB Ω_GW ≲ {O3_OMEGA_GW_OOM:.1e} near {O3_F_REF_HZ} Hz  [arXiv:{O3_ARXIV}]",
        f"  PTA h_c ~ {PTA_HC_OOM:.0e} at ~1/yr                   [arXiv:{PTA_ARXIV}]",
        "",
        "Sister residual map (DIFFERENT operator):",
        f"  sigma_free (ell_*=R_nl) ~ {SIGMA_FREE:.2e}",
        f"  DESI sigma_X ceiling   ~ {SIGMA_X_DESI:.2e}",
        f"  path-RMS free          ~ {RMS_PATH_FREE:.2e}",
        "",
        "Non-claims: no sigma_X from LIGO; no ell_* from ASD; no scalar mode search.",
        "SDiff cancels isotropic vacuum stress; TT GW remain a separate measurable channel.",
        f"Wrote {OUT}/SUMMARY.json and ASD/coherence tables.",
    ]
    text = "\n".join(lines) + "\n"
    (OUT / "SUMMARY.txt").write_text(text)
    print(text)


if __name__ == "__main__":
    main()
