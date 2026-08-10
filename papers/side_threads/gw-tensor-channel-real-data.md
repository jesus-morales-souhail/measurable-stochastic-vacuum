# Tensor channel: real LIGO data

Jesús Morales Souhail · August 2026

DESI residual work is the isotropic channel. Here I run **public LIGO strain** (GWOSC): laser interferometers, H1–L1 baseline ~3000 km.

## Run

```bash
python scripts/gw/download_gwosc_strain.py      # GW150914, 32 s
python scripts/gw/gw_channel_real_strain.py
python scripts/gw/download_o3_long.py           # O3, 4096 s (~250 MB, gitignored)
python scripts/gw/gw_o3_crosscorr_heavy.py
```

Results: `results/gw_channel/`. Large O3 HDF5 stays local (`data/gw_public/o3/`).

## What came out (O3 stretch, this machine)

| Quantity | Value |
|:---------|:------|
| Data | 4096 s × H1+L1, 4 kHz, GW190521 open window |
| Mean coherence 20–90 Hz | ~0.008 |
| $\Omega_{\mathrm{GW}}$ hat (crude) | noise-like (SNR proxy $\sim 0.1$) |
| Published O3 $\Omega_{\mathrm{GW}}$ | $\lesssim 5.8\times 10^{-9}$ @ 25 Hz (arXiv:2101.12130) — full run, not this stretch |
| Extra polarisations | null in LVK literature (arXiv:2112.06861); not re-derived here |
| PTA $h_c$ | $\sim 2\times 10^{-15}$ (arXiv:2306.16213) |

SDiff kills isotropic $T\propto g_{\mu\nu}$. It does **not** kill TT strain. Do not equate $\sigma_X$ or $\sigma_{\mathrm{free}}$ with $h$ or $\Omega_{\mathrm{GW}}$.
