# Plan to bound the coupling \(g\) (residual \(\chi\)–matter)

**Author:** Jesús Morales Souhail  
**Date:** July 2026  
**Status:** Analysis plan + OOM bounds — **not** a finished MCMC paper  
**Code:** [`scripts/r1_bound_g_oom.py`](../scripts/r1_bound_g_oom.py)  
**Depends on:** [`r1-t12-bbks-and-derivation.md`](r1-t12-bbks-and-derivation.md) · sister DESI \(\sigma_X\) · [`lensing-rms-forecast-real-data.md`](lensing-rms-forecast-real-data.md)

---

## 1. What is already fixed (not free)

| Quantity | Value | Role |
|:---------|:------|:-----|
| \(R_{\mathrm{nl}}\) | \(\approx 8.61\,\mathrm{Mpc}\) | Domain / filter cell (T1.1) |
| \(R_*\) | \(\approx 1.58\,\mathrm{Mpc}\) | Peak tip (BBKS); substructure |
| \(\ell_{\mathrm{sep}}\) | \(\approx 15.9\,\mathrm{Mpc}\) | Packing of \(\delta>1\) patches |
| \(\sigma_{\mathrm{count}}\) (\(d=3\), \(\ell_*=R_{\mathrm{nl}}\)) | \(\approx 8.5\times 10^{-5}\) | Free residual amplitude from counting |
| DESI residual ceiling | \(\sigma_X<1.5\times 10^{-4}\) (95% CL) | A posteriori bound (sister repo) |

**Free parameter to bound:** coupling strength between residual field \(\chi\) and matter contrast \(\delta_m\).

---

## 2. Parameterization of \(g\) (so it is observable)

The sketch used \(\mathcal{L}_{\mathrm{int}}=g\,\chi\,\delta_m\). For bounds we use a **dimensionless** effective coupling on the nonlinear domain (clearer than a dimensionful \(g\)):

### 2.1 Response coupling \(\lambda\) (primary)

On the filter scale \(R_{\mathrm{nl}}\),
\[
\Bigl(\frac{\delta\rho_X}{\rho_X}\Bigr)_{\mathrm{ind}}
=\lambda\,\delta_m\big|_{R_{\mathrm{nl}}}
+\text{(free residual orthogonal to }\delta_m\text{)}.
\]
- \(\lambda=0\): no induced residual (pure free grain).  
- \(\lvert\lambda\rvert\sim 1\): residual tracks matter 1:1 (ruled out by BAO smoothness).  

**Relation to action \(g\):** once the normalization of \(\chi\) is fixed (e.g. \(\langle\chi^2\rangle^{1/2}=\sigma_{\mathrm{count}}\)),  
\(\lambda = g\times\text{(normalisation factor)}\). Bounding \(\lambda\) bounds \(g\) up to that convention — state the convention in any paper.

### 2.2 Free residual \(\sigma_{\mathrm{free}}\) (secondary, already OOM-fixed)

\[
\sigma_{\mathrm{free}}\equiv\Bigl(\frac{R_{\mathrm{nl}}}{L_H}\Bigr)^{3/2}\approx 8.5\times 10^{-5}
\]
under P\(_\mathrm{nl}\)+counting \(d=3\). Not a free MCMC parameter unless P\(_\mathrm{nl}\) is abandoned.

### 2.3 Effective residual for DESI / slip

\[
\sigma_{\mathrm{res}}^2
\simeq
\sigma_{\mathrm{free}}^2
+\lambda^2\,\sigma_\delta^2(R_{\mathrm{nl}})
+\cdots
\]
At \(R_{\mathrm{nl}}\), \(\sigma_\delta=1\) by definition, so the induced piece has RMS \(\lvert\lambda\rvert\) if \(\delta_m\) is order-unity on that scale.

---

## 3. Observables and methods (ordered)

### Stage 0 — OOM inequality (now; script)

**Observable:** sister DESI BAO residual bound under OU/QNM kernel.  
**Method:** algebraic, no MCMC.

\[
\sigma_{\mathrm{res}}\le \sigma_X^{\mathrm{DESI}}=1.5\times 10^{-4}.
\]
Optimistic induced-only bound (\(\sigma_{\mathrm{free}}=0\)):
\[
\lvert\lambda\rvert\lesssim 1.5\times 10^{-4}.
\]
With free grain included (independent, Gaussian add in quadrature):
\[
\lvert\lambda\rvert
\lesssim
\sqrt{
\bigl(\sigma_X^{\mathrm{DESI}}\bigr)^2-\sigma_{\mathrm{free}}^2
}
\approx 1.24\times 10^{-4}
\quad(\sigma_{\mathrm{free}}=8.5\times 10^{-5}).
\]

```bash
python scripts/r1_bound_g_oom.py
```

**Status:** **executable now.** Does not replace a full likelihood; freezes the ceiling.

---

### Stage 1 — BAO residual likelihood (primary precision path)

| | |
|:--|:--|
| **Data** | Public DESI DR2 BAO summary stats + covariance (sister repo pipelines) |
| **Model** | Flat \(\Lambda\)CDM background + residual kernel with \(\sigma_{\mathrm{res}}(\lambda)=\sqrt{\sigma_{\mathrm{free}}^2+\lambda^2}\) (or linear response template correlated with \(\delta_m\) if implemented) |
| **Parameters** | \(\lambda\) (and optionally \(\sigma_{\mathrm{free}}\) with prior around \(8.5\times 10^{-5}\) if testing P\(_\mathrm{nl}\)); **not** \(\ell_*\) free |
| **Method** | Nested sampling / MCMC (emcee or existing sister Cobaya/custom OU likelihood) on **public** BAO only first; then multi-probe only a posteriori |
| **Output** | Posterior \(p(\lambda\mid\mathrm{BAO})\); 95% upper limit \(\lambda_{95}\) |
| **Illegal** | Refit \(\ell_*\) or \(R_{\mathrm{nl}}\) to improve the limit |

**Why BAO first:** that is where \(\sigma_X\) is already defined and audited in this programme.

---

### Stage 2 — Gravitational slip / RSD + lensing (operator check)

| | |
|:--|:--|
| **Data** | Maus et al. DESI×CMB-lensing slip \(\gamma=1.17\pm 0.11\) (arXiv:2505.20656); later TDCOSMO / Stage-IV as available |
| **Model** | Programme wall: \(\lvert\gamma-1\rvert=2\varepsilon\sigma_{\mathrm{res}}(\rho_X/\rho_m)/\lvert\delta_m\rvert\) with \(\sigma_{\mathrm{res}}(\lambda)\) from Stage 0–1; path RMS optional |
| **Method** | (i) OOM: require predicted \(\lvert\gamma-1\rvert_{\mathrm{loc}}\) and \(\mathrm{RMS}_{\mathrm{path}}\) below published errors; (ii) later, importance sampling of Stage-1 chains through slip likelihood |
| **Output** | Consistency check; typically **weaker** than BAO for \(\lambda\) today (Maus error \(\mathcal{O}(0.1)\) vs signal \(\sim 10^{-3}\)–\(10^{-4}\)) |
| **Ref.** | [`lensing-rms-forecast-real-data.md`](lensing-rms-forecast-real-data.md) |

**Role:** not the tightest bound on \(\lambda\), but the right **operator** (anisotropic residual / SDiff gap).

---

### Stage 3 — Clusters / nonlinear scales (scale structure, not \(g\) first)

| | |
|:--|:--|
| **Data** | Cluster abundances, weak-lensing mass maps; \(\xi_{gg}\) (DESI/SDSS) for \(r_0\) |
| **Model** | Mask of nonlinear regions; check that residual support \(\propto\mathbf{1}\{\delta>\delta_c\}\) does not overproduce cluster-scale systematics |
| **Method** | Forward model of residual-induced bias in \(n(M)\) or in \(w_p(r_p)\) — **after** Stage 1 prior on \(\lambda\) |
| **Output** | Test of T1.2 geometry (edge on \(\delta_m\)); secondary bound on \(\lambda\) if residual correlates with \(\delta_m\) |
| **Caution** | Easy to double-count nonlinear systematics; pre-register scales \(R_{\mathrm{nl}},R_*\) |

---

### Stage 4 — Full MCMC only when Stage 1 is green

| | |
|:--|:--|
| **Sampler** | Nested sampling (dynesty/ultranest) or emcee |
| **Likelihood** | Sister OU-BAO + optional slip; **fixed** \(R_{\mathrm{nl}}\) from \(\sigma(R)=1\) |
| **Priors** | \(\lambda\sim\mathrm{Uniform}(-10^{-3},10^{-3})\) or log-uniform on \(\lvert\lambda\rvert\); \(\sigma_{\mathrm{free}}\) delta or narrow prior at \(8.5\times 10^{-5}\) under P\(_\mathrm{nl}\) |
| **Systematics** | OU kernel hyperparameters as in sister paper; no free \(10^{56}\) |
| **Success metric** | \(\lambda_{95}\) reported with \(\ell_*\) **not** varied |

---

## 4. Which observable wins for \(g\)?

| Observable | Sensitivity to \(\lambda\) today | Role |
|:-----------|:---------------------------------|:-----|
| **DESI BAO residual \(\sigma_X\)** | **Strongest** (ceiling \(1.5\times 10^{-4}\)) | **Primary bound** |
| Slip \(\gamma\) (Maus) | Weak (error \(\sim 0.1\)) | Operator sanity |
| Path RMS / Stage-IV lensing | Future | Tighten anisotropic channel |
| Clusters / \(r_0\) | Scale geometry, weak on \(\lambda\) alone | T1.2 structure test |

**Plan in one line:** bound \(\lambda\) (hence \(g\)) **primarily with BAO residual likelihood**; use lensing/slip as consistency; clusters for mask geometry — not as the first \(g\) constraint.

---

## 5. Mapping \(\lambda\to g\) (convention to freeze before MCMC)

Fix residual field normalisation so that free variance matches counting:
\[
\langle\chi^2\rangle^{1/2}_{\mathrm{free}}=\sigma_{\mathrm{free}}.
\]
If the induced contrast is \(\delta\rho_X/\rho_X=\kappa\,g\,\chi\,\delta_m\) with \(\kappa\) fixed by the action convention (\(\kappa=1\) if \(\chi\) already dimensionless contrast), then
\[
\lambda=\kappa\,g\,\langle\chi^2\rangle^{1/2}
\quad\Rightarrow\quad
g=\frac{\lambda}{\kappa\,\sigma_{\mathrm{free}}}.
\]
With \(\kappa=1\), \(\sigma_{\mathrm{free}}=8.5\times 10^{-5}\), \(\lvert\lambda\rvert\lesssim 1.2\times 10^{-4}\):
\[
\lvert g\rvert\lesssim\frac{1.2\times 10^{-4}}{8.5\times 10^{-5}}\sim\mathcal{O}(1).
\]
**Interpretation:** order-unity dimensionless \(g\) is already at the edge of the DESI residual ceiling once \(\chi\) is normalized to the free grain — so BAO is informative, not empty.

(Report both \(\lambda_{95}\) and \(g_{95}\) under this convention in any paper.)

---

## 6. What we will **not** do

| Move | Why |
|:-----|:----|
| Fit \(R_{\mathrm{nl}}\) or \(\ell_*\) inside the MCMC | BOUNDARY / undeclared free scale |
| Use H0 9% as a \(g\) target | Amplitude short; wrong problem |
| Claim Stage-0 OOM is a detection of \(\chi\) | Ceiling only |
| Skip BAO and jump to clusters | Weaker for \(g\); more systematics |

---

## 7. Immediate next engineering steps

1. **Now:** Stage 0 script (done) + freeze \(\lambda\leftrightarrow g\) convention.  
2. **Next code:** sister-repo OU likelihood wrapper `logL(lambda)` with \(\sigma_{\mathrm{res}}(\lambda)=\sqrt{\sigma_{\mathrm{free}}^2+\lambda^2}\), \(\ell_*\) fixed.  
3. **Then:** short MCMC / profile likelihood → \(\lambda_{95}\).  
4. **Then:** push chains through slip OOM / Maus consistency.  
5. **Optional:** cluster mask test with fixed \((R_{\mathrm{nl}},R_*,\lambda_{95})\).

---

## 8. One-sentence plan

> Bound the dimensionless response \(\lambda\) (and \(g\) under fixed \(\chi\)-normalisation) **first** with the DESI BAO residual likelihood at fixed \(\ell_*=R_{\mathrm{nl}}\); use slip/lensing as operator checks and clusters only for nonlinear-mask geometry — Stage-0 already implies \(\lvert\lambda\rvert\lesssim 10^{-4}\) and \(\lvert g\rvert\lesssim\mathcal{O}(1)\).

---

*End of \(g\)-bounding plan.*
