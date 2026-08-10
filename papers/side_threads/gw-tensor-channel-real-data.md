# Tensor channel: real LIGO open data (not DESI residual)

Jesús Morales Souhail · August 2026  
[github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)

I spent a long time on DESI residual amplitude and counting cells. That is the **isotropic** residual channel. The place I had not run real data was the **tensor** channel: laser interferometers with a continental baseline (LIGO H1–L1).

This note records a first public-data run. It is **not** a claim that $\sigma_X$ was measured with LIGO.

---

## Data (real, open)

| Item | Value |
|:-----|:------|
| Source | GWOSC (Gravitational Wave Open Science Center) |
| Event | GW150914 |
| Files | H1 and L1, 4 kHz, 32 s around the merger |
| DOI | https://doi.org/10.7935/82H3-HH23 |
| Local path | `data/gw_public/` |

```bash
python scripts/gw/download_gwosc_strain.py
python scripts/gw/gw_channel_real_strain.py
```

Output: `results/gw_channel/SUMMARY.txt`.

The two detectors form a **long-baseline interferometer network** (~3000 km Hanford–Livingston). That is laser interferometry, not VLBI radio; the shared idea is a long baseline.

---

## What the script measures

On the public strain time series:

- amplitude spectral density (ASD) for H1 and L1  
- band-limited RMS strain in 20–300 Hz  
- peak $|h|$ near the merger time  
- mean coherence between H1 and L1 in 40–200 Hz  

Those are properties of **calibrated tensor strain** in the open data stretch. They are not BAO $\alpha$ residuals.

---

## Why this sits next to the residual programme

Unimodular / SDiff reasoning in this corpus kills local vacuum stress of the form $T_{\mu\nu}\propto V(x)\,g_{\mu\nu}$ (isotropic). That protects a smooth $\Lambda$ and makes a small $\sigma_X$ natural.

It does **not** remove transverse-traceless gravitational waves. So:

| Channel | Operator | Instrument in this programme |
|:--------|:---------|:-----------------------------|
| Isotropic residual $X$ | $\delta\Omega_\Lambda$ / BAO $\alpha$ | DESI (sister repo) |
| Slip / path-RMS | anisotropic scalar potentials | OOM vs Maus/Sakr |
| Tensor $h_{ij}^{\mathrm{TT}}$ | strain | LIGO open data (this note) |

Falsifier already written in the unimodular note: a **scalar polarisation** in GW would go beyond pure GR / two-tensor structure. That search is **not** implemented here; it needs a dedicated pipeline.

---

## What I will not claim from this run

- That $\sigma_{\mathrm{free}}\approx 8.5\times 10^{-5}$ equals a LIGO strain.  
- That $\ell_\ast=R_{\mathrm{nl}}$ is measured in the ASD.  
- That O3 $\Omega_{\mathrm{GW}}$ limits are re-derived from 32 seconds of GW150914 (they are cited as literature anchors only).  
- That PTA $h_c\sim 10^{-15}$ is the same object as DESI $\sigma_X$.

---

## Literature anchors used for context

- O3 isotropic stochastic GW background: arXiv:2101.12130  
- NANOGrav 15 yr PTA background (order of magnitude $h_c$): arXiv:2306.16213  

---

## Next real experiments (if I continue this thread)

1. Longer clean open-data segments for a proper SGWB-style cross-correlation (still tensor).  
2. Published constraints on extra polarisations — cite, do not invent.  
3. Keep DESI residual and GW strain in separate likelihoods until a derived $X\to h$ map exists.

For the residual grain map, the next step remains path-RMS with $\ell_\ast=R_{\mathrm{nl}}$ fixed. For the geometric vacuum story, the **open measurable crack** is the tensor / anisotropic sector, not another soft gain on $\sigma_0$.
