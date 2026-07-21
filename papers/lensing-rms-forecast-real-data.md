# Path-RMS vs real lensing / slip data: an OOM forecast gate

**Author:** Jesús Morales Souhail  
**ORCID:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Date:** July 2026  
**Status:** Publication-oriented data note — **uses published external results**; not a full survey likelihood  
**Code:** [`scripts/lensing_rms_real_data_compare.py`](../scripts/lensing_rms_real_data_compare.py)  
**Sister data pack:** [stochastic-dark-energy-ou `data-pack-option0-internet.md`](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou/blob/main/papers/data-pack-option0-internet.md)  
**Claim discipline:** [`NARROW_PATH.md`](NARROW_PATH.md) §5.1–5.2 · [`r1-open-kernel.md`](r1-open-kernel.md)

---

## Abstract

We compare the programme’s **hand-placed** path-integrated slip RMS at DESI-safe corners (NP-A / NP-B) to **published** gravitational-slip and modified-gravity constraints and to Stage-IV **shear-calibration** requirements from the literature. All external numbers are taken from named papers (arXiv IDs below). The conclusion is quantitative and non-binary:

1. Current mean-slip precision (Maus et al.) is \(\mathcal{O}(0.1)\) on \(\gamma=\Phi/\Psi\).  
2. Euclid-like + DESI-like **forecasts** for constant anisotropic stress \(\eta\) reach \(\sim 5\%\) (Sakr et al.); free \((z,k)\) remains \(\gtrsim 30\%\).  
3. DESI full-shape MG constraints on the lensing parameter \(\Sigma_0\) are still \(\mathcal{O}(0.05)\).  
4. Programme NP-B path RMS is \(\sim 4\times 10^{-3}\); NP-A is \(\sim 3.5\times 10^{-4}\).  
5. Therefore published / forecast **mean** slip precision sits **roughly \(10\)–\(30\times\)** (Sakr constant \(\eta\)) to **\(\sim 25\times\)** (Maus) above NP-B, and far above NP-A — **before** equating operators.  
6. Stage-IV multiplicative bias control at \(\sim 10^{-3}\) is a **calibration** requirement, **not** a measurement of stochastic path-RMS of DE wrinkles.

We do **not** claim discovery, model death, or that Euclid/LSST “reach \(10^{-3}\) on this statistic.”

---

## 1. What is being compared (operator honesty)

| Side | Quantity | Status |
|:-----|:---------|:-------|
| **This programme** | \(\mathrm{RMS}_{\mathrm{path}}=\lvert\gamma-1\rvert_{\mathrm{loc}}\sqrt{\chi/\ell_*}\) for iid patches | Verified **kinematics** for hand-placed \(\sigma_0,r\) ([`NARROW_PATH.md`](NARROW_PATH.md)) |
| **Maus / DESI×κ** | Mean gravitational slip \(\gamma=\Phi/\Psi\) | **Measured** |
| **Sakr et al.** | Model-independent anisotropic stress \(\eta\) | **Forecast** (Euclid-like ± DESI-like) |
| **DESI MG** | \(\mu_0\), \(\Sigma_0\) (clustering / lensing MG) | **Measured** (DESI 2024 FS era) |
| **Stage-IV SRD / Euclid WL** | Multiplicative shear bias \(m\) control | **Requirement**, not a slip detection |

**Category error to avoid:** treating \(\sigma(m)\sim 10^{-3}\) or \(\sigma(\gamma)\sim 0.1\) as if they were \(\sigma(\mathrm{RMS}_{\mathrm{path}})\). They bound how far the field is from the programme’s **theory-side** OOM, under an imperfect operator map.

---

## 2. Programme numbers (reproducible, hand-placed)

Fiducial: \(H_0=67.4\), \(\Omega_m=0.315\), \(\Omega_\Lambda=0.685\), \(z_s=1.5\), \(\varepsilon=1\), \(d=3\), evaluation redshift for local slip \(z=0.8\).

| Corner | \(\sigma_0\) | \(r\) | \(\sigma_{\mathrm{res}}\) | \(\ell_*\) [Mpc] | \(\mathrm{RMS}_{\mathrm{path}}\) |
|:-------|:-------------|:------|:--------------------------|:-----------------|:--------------------------------|
| **NP-A** | \(10^{-5}\) | \(0\) | \(10^{-5}\) | \(\approx 2.06\) | \(\approx 3.5\times 10^{-4}\) |
| **NP-B** | \(5\times 10^{-6}\) | \(1.5\) | \(\approx 1.00\times 10^{-4}\) | \(\approx 1.30\) | \(\approx 4.4\times 10^{-3}\) |

```bash
python scripts/lensing_rms_real_data_compare.py
pytest -q
```

**Reminder:** NP-B is **not** derived from the open R1 kernel ([`BOUNDARY.md`](../BOUNDARY.md)).

---

## 3. External real data (cited)

### 3.1 Maus et al. (2025) — DESI DR1 × CMB lensing

| | |
|:--|:--|
| **Reference** | Maus, White, Sailer et al., arXiv:[2505.20656](https://arxiv.org/abs/2505.20656) (v3); JCAP 11 (2025) 077 |
| **Definition** | \(\gamma=\Phi/\Psi\) (GR: \(1\)) |
| **Result** | \(\gamma = 1.17 \pm 0.11\) (\(\sim 1.5\sigma\) from GR; authors note possible projection effects) |
| **Data** | DESI DR1 BGS+LRG full-shape + recon; Planck PR4 + ACT DR6 \(\kappa\); Legacy photometry |
| **Also** | \(\sigma_8=0.803\pm 0.017\), \(S_8=0.808\pm 0.017\) |

**Use here:** \(1\sigma\) scale on mean slip \(\sim 0.11\).

### 3.2 Sakr, Zheng, Casas (2025) — anisotropic stress forecasts

| | |
|:--|:--|
| **Reference** | Sakr et al., arXiv:[2501.07477](https://arxiv.org/abs/2501.07477); MNRAS 2025 |
| **Definition** | Model-independent effective anisotropic stress \(\eta\) from spectro clustering + photo lensing/clustering (no assumed \(P(k)\) shape / bias / expansion beyond observables) |
| **Survey model** | Euclid-like photometric ± DESI-like spectroscopic |
| **Forecast (abstract)** | free \((z,k)\): **at least \(\sim 30\%\)**; \(z\)-only: **\(<10\%\)** average; **constant \(\eta\): \(\sim 5\%\)** |

**Use here:** best Stage-IV-class **mean** \(\eta\) precision in the constant case \(\sim 0.05\) absolute if \(\eta\sim 1\).

### 3.3 DESI modified gravity full-shape (2024/25)

| | |
|:--|:--|
| **Reference** | DESI Collaboration / Ishak et al., arXiv:[2411.12026](https://arxiv.org/abs/2411.12026) |
| **Result (ΛCDM bg, DESI FS+BAO + CMB + DESY3 + DESY5-SN)** | \(\mu_0=0.05\pm 0.22\), \(\Sigma_0=0.008\pm 0.045\) (GR-compatible) |
| **Note** | \(\mu,\Sigma\) are **not** identical to Maus \(\gamma\), but they are correct-scale RSD+lensing MG operators |

**Use here:** \(\sigma(\Sigma_0)\sim 0.045\) as a current lensing-sector MG error bar.

### 3.4 Stage-IV shear calibration (requirement, not detection)

| | |
|:--|:--|
| **LSST DESC SRD** | Mandelbaum et al., arXiv:[1809.01669](https://arxiv.org/abs/1809.01669) — Stage-IV dark-energy systematic budgets for weak lensing |
| **Euclid WL** | Euclid preparation (e.g. LensMC, A&A 691 A319, 2024) — Stage-IV multiplicative / additive bias control |
| **OOM used** | Multiplicative bias control \(\lvert m\rvert\sim \mathrm{few}\times 10^{-3}\) |

**Use here:** \(\sim 2\times 10^{-3}\) as an OOM **calibration** floor — **not** \(\sigma(\mathrm{RMS}_{\mathrm{path}})\).

### 3.5 Sister empirical residual (this programme’s BAO side)

| | |
|:--|:--|
| **DESI DR2 BAO** | arXiv:[2503.14738](https://arxiv.org/abs/2503.14738) |
| **Sister bound** | \(\sigma_X < 1.5\times 10^{-4}\) (95% CL, OU kernel) — [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou) |

---

## 4. Quantitative comparison (OOM ratios)

Define
\[
\mathcal{R} \equiv \frac{\text{published or forecast error scale}}{\mathrm{RMS}_{\mathrm{path}}(\mathrm{NP})}.
\]
\(\mathcal{R}\gg 1\) means the external precision is still **coarser** than the programme corner (under the imperfect operator identification).

| External scale | Value | \(\mathcal{R}\) vs NP-B (\(\sim 4.4\times 10^{-3}\)) | \(\mathcal{R}\) vs NP-A (\(\sim 3.5\times 10^{-4}\)) |
|:---------------|:------|:-----------------------------------------------------|:-----------------------------------------------------|
| Maus \(\sigma(\gamma)\) | \(0.11\) | \(\sim 25\times\) | \(\sim 310\times\) |
| Sakr constant \(\eta\) \(\sim 5\%\) | \(0.05\) | \(\sim 11\times\) | \(\sim 140\times\) |
| Sakr free \((z,k)\) \(\gtrsim 30\%\) | \(0.30\) | \(\sim 68\times\) | \(\sim 860\times\) |
| DESI MG \(\sigma(\Sigma_0)\) | \(0.045\) | \(\sim 10\times\) | \(\sim 130\times\) |
| Stage-IV \(m\)-bias OOM | \(2\times 10^{-3}\) | \(\sim 0.5\times\) (**wrong operator**) | \(\sim 6\times\) |
| Historical prog. mean-slip floor | \(0.03\) | \(\sim 7\times\) | \(\sim 85\times\) |

Numbers from `python scripts/lensing_rms_real_data_compare.py` (may differ at \(\sim 10\%\) relative if evaluation \(z\) choices change; order is stable).

### 4.1 Reading (calibrated)

1. **Today (Maus):** mean slip is measured at \(\mathcal{O}(0.1)\). NP-B path RMS is \(\sim 25\times\) smaller even before systematics and operator mismatch. A claim that “deep lensing already tests NP-B” is **false**.  
2. **Stage-IV mean \(\eta\) (Sakr, constant):** \(\sim 5\%\) is the optimistic homogeneous case — still \(\sim 10\times\) above NP-B path RMS if one naively equates \(\lvert\eta-1\rvert\) with path RMS. Free \((z,k)\) is worse (\(\gtrsim 30\%\)).  
3. **\(m\sim 10^{-3}\):** looks numerically near NP-B, but it is **shear calibration**, not stochastic DE texture. Using it as a detection threshold is the category error §5.1 of [`NARROW_PATH.md`](NARROW_PATH.md) forbids.  
4. **Null / excess:** same binary lock — excess needs baryons / photo-\(z\) / IA control; null excludes the **tested corner**, not the open kernel.

---

## 5. Systematics that can fake or hide \(\mathrm{RMS}\sim 10^{-3}\)

These are standard Stage-III/IV contaminants (not optional):

| Systematic | Why it matters at \(10^{-3}\) |
|:-----------|:------------------------------|
| **Baryonic feedback** | Suppresses small-scale \(P(k)\); biases cosmic shear and \(S_8\) |
| **Photo-\(z\) errors** | Bin leakage couples kernels; Stage-IV requires \(\sim 0.1\%\)-class mean-\(z\) control (Euclid WL literature) |
| **Intrinsic alignments** | Galaxy shapes correlate without lensing; IA models are leading WL systematics |
| **Multiplicative bias \(m\)** | Shear calibration at few \(\times 10^{-3}\) is already a Stage-IV requirement |
| **Additive shear / PSF** | Can imprint coherent residuals along the line of sight |

Any “first positive evidence” language **must** list these as first-line null hypotheses ([`NARROW_PATH.md`](NARROW_PATH.md) §5.1).

---

## 6. What would count as a real forecast of *this* statistic

A paper-grade forecast (not yet done here) would need:

1. A **defined observable** mapping \(\mathrm{RMS}_{\mathrm{path}}\) (or a two-point proxy of stochastic slip wrinkles) onto measurable spectra (\(C_\ell^{\kappa g}\), \(E_G\), slip tomography, …).  
2. A **likelihood** with Euclid/LSST+DESI specifications.  
3. A **systematics budget** (baryons, IA, photo-\(z\), \(m\)).  
4. A **prior** on \((\ell_*,G_O,\varepsilon)\) that does **not** fit DESI residual \(\sigma_X\) as a dial.  
5. Clear output: exclusion contours on the **corner**, not “model death.”

Until then, this note is the **gate**: real data say mean-slip / MG precision is still **decades of millides** away from claiming NP-B as tested, and Stage-IV \(m\sim 10^{-3}\) must not be rebranded as DE texture sensitivity.

---

## 7. Claim checklist

| ID | Claim | Status |
|:---|:------|:-------|
| L1 | Programme NP-A/B path RMS numbers as in §2 | Verified kinematics |
| L2 | Maus \(\gamma=1.17\pm 0.11\) | External published |
| L3 | Sakr \(\eta\) forecasts 5% / \(<10\%\) / \(\ge 30\%\) | External forecast abstract |
| L4 | DESI MG \(\Sigma_0=0.008\pm 0.045\) (stated combo) | External published |
| L5 | \(\mathcal{R}\gg 1\) for mean-slip errors vs NP path RMS | Arithmetic from L1–L4 |
| L6 | Stage-IV \(m\sim 10^{-3}\) is calibration, not path-RMS detection | Definitional |

| Non-claim | |
|:----------|:--|
| N-L1 | Euclid/LSST **will** detect \(\mathrm{RMS}_{\mathrm{path}}\sim 10^{-3}\) |
| N-L2 | Detection \(\Rightarrow\) texture of dark energy |
| N-L3 | Null \(\Rightarrow\) full programme death |
| N-L4 | \(m\sim 10^{-3}\) \(\equiv\) slip path-RMS sensitivity |
| N-L5 | Operator equality \(\gamma\equiv\eta\equiv\Sigma\equiv\mathrm{RMS}_{\mathrm{path}}\) |

---

## 8. One-sentence verdict

> Real published slip and MG errors (Maus \(\mathcal{O}(0.1)\), DESI \(\Sigma_0\sim 0.05\)) and optimistic Stage-IV mean-\(\eta\) forecasts (Sakr \(\sim 5\%\)) still sit about an order of magnitude or more above the programme’s hand-placed NP-B path RMS, while Stage-IV \(10^{-3}\) shear-calibration requirements are the wrong operator for claiming dark-energy texture.

---

## 9. Reproduce

```bash
cd measurable-stochastic-vacuum
pip install -r requirements.txt
pytest -q
python scripts/lensing_rms_real_data_compare.py
python scripts/lib_verified.py
```

**Related:** [`NARROW_PATH.md`](NARROW_PATH.md) · [`PAST_LIGHT_CONE_INTEGRATION.md`](PAST_LIGHT_CONE_INTEGRATION.md) · [`OBSERVABLE_WALL.md`](OBSERVABLE_WALL.md) · sister `data-pack-option0-internet.md`

---

*End of real-data lensing forecast gate.*
