# Analysis plan: residual–structure correlation on the nonlinear scale

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail) · July 2026

*Pre-registered protocol for a residual–matter cross test. Not a claim of Stage-IV detection.*

Related: [`FRONTIER_INQUIRY.md`](FRONTIER_INQUIRY.md), [`r1-sandwich-falsifiers.md`](r1-sandwich-falsifiers.md)
Code: [`scripts/r1/r1_stage4_test_design.py`](../../scripts/r1/r1_stage4_test_design.py), [`scripts/r1/r1_T2_mock_pipeline.py`](../../scripts/r1/r1_T2_mock_pipeline.py)

---

## 0. Purpose

If a residual of amplitude $\sim 10^{-5}$–$10^{-4}$ couples locally to matter, its spatial correlation is predicted to lie near the nonlinear scale $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ (allowed band roughly $4$–$26\,\mathrm{Mpc}$), not at the Planck length, the Hubble radius, or an 8% distance shift.

This document fixes, before inspection of residual maps:

1. hypotheses;
2. observable definitions;
3. the scale band and null tests;
4. support and exclusion criteria;
5. analysis choices that are not permitted after unblinding.

Deviations from the plan should be stated explicitly in any application to DESI or Euclid data.

---

## 1. Hypothesis (T2)

**H1 (scale).**
The two-point structure of a residual field $\chi$ (or a residual proxy correlated with anisotropic stress / BAO residual template) has correlation length


\ell_{\ast}\in [0.5,\,3]\,R_{\mathrm{nl}}\approx [4.3,\,25.8]\,\mathrm{Mpc}


when the residual amplitude is in the programme window $\sigma\sim 10^{-5}$–$1.5\times 10^{-4}$.

**H2 (matter lock).**
$\chi$ is positively correlated with a nonlinear mask built only from matter:


m=\mathbf{1}\{\delta_m(R_{\mathrm{nl}})>\delta_c\},\qquad \delta_c\in\{1.0,\,1.5\}


(pre-registered defaults: $\delta_c=1.0$ primary; $1.5$ robustness).

**H0 (null).**
Residual is spatially white on survey scales, or correlated only on $\ll 1\,\mathrm{Mpc}$ or $\gg 100\,\mathrm{Mpc}$, or anti-correlated with $m$ at high significance without a derived sign flip.

---

## 2. What is fixed a priori (no floating)

| Quantity | Value | Source |
|:---------|:------|:-------|
| $R_{\mathrm{nl}}$ | $\approx 8.61\,\mathrm{Mpc}$ | $\sigma(R)=1$, EH-like $P(k)$, $\sigma_8=0.81$ |
| Counting $d$ | $3$ | programme default |
| $\sigma_{\mathrm{free}}$ | $\approx 8.5\times 10^{-5}$ | $(R_{\mathrm{nl}}/L_H)^{3/2}$ |
| Residual ceiling | $\sigma_X<1.5\times 10^{-4}$ (95%) | related DESI OU |
| Allowed $\ell_{\ast}$ band | $[0.5,3]R_{\mathrm{nl}}$ | sandwich $\mathcal{O}(1)$ |
| $k_{\mathrm{nl}}$ pivot | $\sim 0.17\,h\,\mathrm{Mpc}^{-1}$ | $\sim 1/(R_{\mathrm{nl}}h)$ OOM |
| $\ell_{\mathrm{sep}}$ (packing) | $\approx 15.9\,\mathrm{Mpc}$ | $f(\delta>1)\approx 0.16$ |

Excluded: refit $R_{\mathrm{nl}}$ or $\ell_{\ast}$ to improve T2 after looking at residual maps.

---

## 3. Observable definitions

### 3.1 Preferred residual proxy (ordered)

| Priority | Proxy | Notes |
|:---------|:------|:------|
| P1 | BAO residual field / bin-wise $(\alpha-1)$ or $D/D_{\mathrm{fid}}-1$ after fixed smooth background | Sister OU pipeline; primary amplitude gate is T1 |
| P2 | Gravitational slip residual map (if available) after subtracting mean MG fit | Secondary; operator $\eta=\Phi/\Psi$ |
| P3 | Path-slip proxy (line-of-sight variance of lensing potential residuals) | Future; not multiplicative shear bias $m$ |

This protocol focuses on cross-structure, assuming a residual amplitude map or template $r(\hat n,z)$ exists at the level of summary statistics.

### 3.2 Matter mask (blind to residual)

1. Build $\delta_m$ from spectroscopic / photometric LSS on a grid with top-hat or Gaussian smoothing $R=R_{\mathrm{nl}}$ (or $R=8\,h^{-1}\mathrm{Mpc}$ robustness).
2. Define $m=\mathbf{1}\{\delta_m>\delta_c\}$.
3. Do not use residual $r$ when building $m$.

### 3.3 Primary T2 statistics

| ID | Statistic | Prediction under H1–H2 |
|:---|:-----------|:------------------------|
| S1 | Correlation length $r_e$ of residual auto $\xi_{rr}$ where $\xi_{rr}(r_e)/\xi_{rr}(0)=1/e$ | $r_e\in[0.5,3]R_{\mathrm{nl}}$ |
| S2 | Cross-correlation $\xi_{rm}(r)$ or $P_{rm}(k)$ residual × mask | Positive near $k\sim k_{\mathrm{nl}}$; significance quoted |
| S3 | Scale of max $\lvert P_{rm}(k)\rvert$ or $\xi_{rm}$ | Within factor 3 of $R_{\mathrm{nl}}$ or $\ell_{\mathrm{sep}}$ |
| S4 | Null control: residual × random mask with same $f_{\mathrm{vol}}$ | Consistent with 0 |

### 3.4 Secondary (robustness, not discovery alone)

- Vary $\delta_c\in\{1.0,1.5,2.0\}$.
- Replace mask by $\delta_m$ itself (linear cross $P_{r\delta}$).
- Split redshift bins ($z<0.8$ vs $z>0.8$) — sandwich is late-time structure; no claim of high-$z$ detection required.
- Jackknife / mock covariance only; no hand-tuned $\theta$ kernels to force a peak at $8.6\,\mathrm{Mpc}$.

---

## 4. Success / kill criteria (frozen)

### 4.1 Support (does not mean discovery of DE residual alone)

T2 supports the sandwich scale lock if all hold:

1. T1 amplitude still $\sigma_{\mathrm{res}}\le 1.5\times 10^{-4}$ (or updated public ceiling) at fixed $\ell_{\ast}=R_{\mathrm{nl}}$.
2. S1: $r_e\in[0.5,3]R_{\mathrm{nl}}$ at $\ge 2\sigma$ preference over white / Gpc-scale alternatives **or** upper limits still allow the band.
3. S2: $\xi_{rm}$ or $P_{rm}$ positive in the $R_{\mathrm{nl}}$ band at $\ge 2\sigma$ vs S4 random mask.
4. No excluded $\ell_{\ast}$ refit.

### 4.2 Kill (L2 for sandwich form)

T2 kills the sandwich scale claim if any hold:

| Kill ID | Condition |
|:--------|:----------|
| K1 | Best-fit residual correlation length $\lt 1\,\mathrm{Mpc}$ or $\gt 100\,\mathrm{Mpc}$ at $\sigma\sim 10^{-4}$ with $\Delta\mathrm{ln}L\ge 1.92$ against the allowed band |
| K2 | Residual significantly anti-correlated with nonlinear mask in all $\delta_c$ with no derived sign mechanism |
| K3 | Only way to pass S1–S2 is to float $\ell_{\ast}$ after unblinding residual maps |
| K4 | Amplitude required for a T2 detection forces $\sigma_{\mathrm{res}}\gg 1.5\times 10^{-4}$ without damping |

### 4.3 Inconclusive (default today)

- No residual detection (T1 null): T2 cannot confirm H1–H2; programme remains upper-limit + theory.
- Mean slip (Maus) alone: insufficient (wrong sensitivity).
- Stage-IV $m\sim 10^{-3}$ shear calibration: wrong operator (never used as T2).

---

## 5. Relation to surveys

| Survey / data | Role in T2 |
|:--------------|:-----------|
| DESI BAO DR2/DR3 | T1 amplitude; optional bin residual template for S2 if maps exist |
| DESI full-shape / LSS | Matter $\delta_m$ and mask $m$ |
| Euclid BAO + WL + clustering | Deeper residual limits; mask from photo/spec LSS; not $m$-bias as residual |
| Rubin/LSST | Mask geometry; systematics budget for any lensing residual proxy |
| CMB lensing × DESI | Mean slip consistency (T3), not T2 primary |

---

## 6. Analysis blinding (recommended)

1. Freeze $R_{\mathrm{nl}}$, band, $\delta_c$, estimators (this document).
2. Build masks from matter only.
3. Optional: inject mock residual at $R_{\mathrm{nl}}$ with $\sigma=\sigma_{\mathrm{free}}$ to validate pipeline before real residual cross.
4. Unblind S1–S4 once covariance and null tests (S4) pass.
5. Report support / kill / inconclusive with the pre-registered thresholds above.

---

## 7. What T2 is not

| Non-goal | Why |
|:---------|:----|
| Explain $H_0\sim 8\%$ | Short by $\sim 30$–$10^{3}\times$(T5) |
| Claim Stage-IV detection today | Floors still coarse for path RMS |
| Replace T1 BAO amplitude gate | T1 remains primary for $\sigma$ |
| Fit $g$ from T2 alone | $g$ from Line A + DESI a posteriori |

---

## 8. Minimal report table (for any future paper)

| Item | Pre-registered value | Measured | Support? |
|:-----|:---------------------|:---------|:---------|
| $R_{\mathrm{nl}}$ fixed | $8.61\,\mathrm{Mpc}$ | — | — |
| $\sigma_{\mathrm{res}}$ (T1) | $\le 1.5\times 10^{-4}$ | | |
| $r_e$(S1) | $[4.3,25.8]\,\mathrm{Mpc}$ | | |
| Sign $\xi_{rm}$ (S2) | $>0$ in band | | |
| Random mask (S4) | null | | |
| $\ell_{\ast}$ floated? | No | | |

---

## 9. End-to-end mock validation (pipeline proof)

Code: [`scripts/r1/r1_T2_mock_pipeline.py`](../../scripts/r1/r1_T2_mock_pipeline.py)
Results: `results/r1_T2_mock/`

Synthetic 2D Gaussian matter field with corr $\sim R_{\mathrm{nl}}$; residual injected as
$r = g\,\sigma_{\mathrm{free}}\,\delta + \mathrm{noise}$.

| Check | Result (fiducial run) |
|:------|:----------------------|
| Recover $r_e$ in allowed band | Yes — ensemble $r_e\approx 16.8\pm 0.9\,\mathrm{Mpc}$ ($\sim 2\,R_{\mathrm{nl}}$) |
| Cross residual×mask positive | Yes — $\approx +0.60$ |
| Cross residual×random mask | Null — $\sim 0$ |
| White residual control | $r_e$ small; cross $\sim 0$ |
| Wrong scale (100 Mpc) injection | $r_e\sim 96\,\mathrm{Mpc}$ outside allowed band |
| Ensemble fraction meeting criteria | 12/12 |
| Pipeline validation | estimators and kill/support logic work on mock |

This shows the estimators and kill/support logic work when the hypothesis is true in the mock. It does not prove nature realises the residual.

```bash
python scripts/r1/r1_T2_mock_pipeline.py
```

---

## 10. Reproduce programme numbers

```bash
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_stage4_test_design.py
python scripts/r1/r1_sandwich_falsifiers.py
python scripts/r1/r1_T2_mock_pipeline.py
pytest -q
```
