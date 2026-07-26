# Filter note: desqueezing is real; invented $H_0(z)=H_{0,\mathrm{fid}}[1+\varepsilon e^{-\theta x}]$ is not

**Author:** Jesús Morales Souhail  
**ORCID / web:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818) · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)  
**Date:** July 2026  
**Status:** Claim-boundary filter — applies `pattern-undeclared-physical-power` + `BOUNDARY`  
**Code:** [`scripts/closed/h0_desqueezing_filter.py`](../../scripts/closed/h0_desqueezing_filter.py)  
**Related:** sister desqueezing note · [`h0-bridge-toy-map.md`](h0-bridge-toy-map.md) · OU residual bound  

---

## Abstract

Complex frequency $\omega=\omega_R-i\gamma/2$ and half-life $t_{1/2}=\ln 2/\gamma$ are **standard** and already validated in this programme’s desqueezing scans.  
A draft construction that writes

$$
H_0(z)=H_{0,\mathrm{fid}}\bigl[1+\varepsilon\,e^{-\theta x}\bigr]
$$

and then chooses $\theta\sim 0.47$ so the knee sits at $z\sim 0.5$–$0.7$ **fails** the filter I use here: the functional form is not derived from Einstein or OU dynamics, and $\theta$ is fitted to the known transition.

This note freezes that filter, restores the correct status of $\sigma_X$ (temporal in $x=\ln a$), separates **CPL 2.5σ/4.2σ** from **H0-running**, and runs the only legal test: **amplitude** of any desqueezing/OU residual is bounded by $\sigma_X<1.5\times 10^{-4}$, which is $\sim 500\times$ too small to produce an $8\%$ $H_0$ drift — **independent of hand-tuned $\theta$**.

---

## 1. What is real (keep)

| Element | Status | Where |
|:--------|:-------|:------|
| $\omega=\omega_R-i\gamma/2$, decay $e^{-\gamma t/2}$ | Standard | QM / QNM |
| $t_{1/2}(\lvert\langle a^2\rangle\rvert)=\ln 2/\gamma$ | Measured (QuTiP) | sister `desqueezing_relax_time.py` / heavy scan |
| Map $\Gamma_{\mathrm{phys}}(z)=\theta H(z)$, $\gamma\leftrightarrow\theta H_0$ | Programme continuity | sister desqueezing note |
| H0-running as **active literature** | Real (contested) | Krishnan, Dainotti, Wong/H0LiCOW |
| DESI residual bound $\sigma_X<1.5\times 10^{-4}$ (95% CL) | Measured | sister OU analysis |
| BAO-only free $(w_0,w_a)$: $w_0\approx -0.99$, $w_a\approx -0.02$ | Measured (BAO-only baseline) | `results/eos_cpl_desi_dr2/eos_cpl_summary.txt` |

---

## 2. What fails the filter (reject)

| Claim | Why illegal |
|:------|:------------|
| $H_0(z)=H_{0,\mathrm{fid}}[1+\varepsilon e^{-\theta x}]$ as physics | **Not derived** from field equations, OU SDE, or desqueezing Lindblad map — free functional form |
| $\theta\sim 0.47$ because transition is at $z\sim 0.5$–$0.7$ | **Post-hoc fit** of the free parameter to the known answer (`BOUNDARY`: no fit of $\ell_{\ast}/r/\theta$ to the gap) |
| $\theta$ “analogous” to $\gamma$ without equation | Undeclared physical power (`pattern-undeclared-physical-power`) |
| “Read the data backwards” as a new method | Same monotone function; no new information |
| $\sigma_X$ is **spatial** so H0 running is unconstrained | **False** — see §3 |
| Table row “DESI+Planck 2.5σ–4.2σ” as H0-running | Those figures are the project’s **CPL dynamical-DE** significances in the DESI paper abstract, **not** an H0-running measurement — do not relabel |

---

## 3. $\sigma_X$ is temporal in $x=\ln a$

In the OU corpus,

$$
X(x)\equiv \delta\Omega_\Lambda(x),\qquad x=\ln a=-\ln(1+z).
$$

The residual amplitude $\sigma_X$ is the stationary scale of fluctuations along **e-fold time**, not a purely spatial grain label.

Consequences:

1. Any claim that a temporal DE drift of order $8\%$ in $H_0$ is “orthogonal” to $\sigma_X$ is **wrong**.  
2. The BAO-only free-$(w_0,w_a)$ fit already asked whether the **mean** DE history needs strong time dependence: it prefers nearly $\Lambda$ ($w_0\approx -0.99$, $w_a\approx -0.02$). Nested $(\sigma,\theta)$ is not preferred ($\Delta\mathrm{AIC}=+4$).  
3. Stochastic residual $\sigma_X$ is an **additional** bound on fluctuations about that mean.

---

## 4. Legal test: amplitude first (no free $\theta$ to the 9%)

### 4.1 Desqueezing / OU residual envelope (programme map)

Anomalous correlator / residual track (schematic, already in desqueezing note):

$$
\lvert X\rvert(x)\;\lesssim\;\sigma\,e^{-\theta\,\Delta x},
$$

with $\sigma\le\sigma_X^{\mathrm{DESI}}=1.5\times 10^{-4}$ and $\theta$ set by OU continuity ($\Gamma=\theta H$), **not** by the H0-running knee.

Even at the **most optimistic** bound $\theta\to 0$ (no damping, residual sits at ceiling for all $z$):

$$
\biggl\lvert\frac{\delta H}{H}\biggr\rvert_{\mathrm{from\ residual}} \;\lesssim\; \sigma_X \;<\; 1.5\times 10^{-4} \;\ll\; 0.083 \;\approx\; \frac{73}{67.4}-1.
$$

**Short by a factor $\gtrsim 500$**, independent of inventing $H_0(z)=H_{0,\mathrm{fid}}[1+\varepsilon e^{-\theta x}]$ and independent of hand-tuned $\theta\sim 0.47$.

Complex $\omega$ changes the **phase** of the correlator, not the **energy budget** allowed by $\sigma_X$.

### 4.2 Same conclusion as path-RMS toy

[`h0-bridge-toy-map.md`](h0-bridge-toy-map.md): DESI-safe stochastic path bias gives $H_0(0.15)/H_0(1.5)\approx 1.006$, not $1.083$.  
Desqueezing packaging does not repair that deficit.

### 4.3 What $\theta$ from the repo actually is (a priori, not H0-fit)

| Anchor | Value | Role |
|:-------|:------|:-----|
| MLE / undamped floor in residual scans | $\theta\sim 10^{-3}$ | effectively undamped on DESI $\Delta x\sim 1$ |
| Nested BAO example | $\theta\sim 1.7$ with $\sigma\to 0$ | not preferred; $\sigma$ dies |
| Mapping $\gamma\leftrightarrow\theta H_0$ | defines lab↔cosmo rate | **does not** fix $\varepsilon=0.083$ |

None of these is “choose $\theta$ so $e^{-\theta x}$ knees at $z=0.5$”.

```bash
python scripts/closed/h0_desqueezing_filter.py
```

---

## 5. CPL 2.5σ / 4.2σ vs H0-running (do not mix)

From sister DESI paper abstract (multi-probe CPL, **not** this note’s H0-running table):

| Combination class | Typical CPL claim in abstract | Meaning |
|:------------------|:------------------------------|:--------|
| DESI+CMB+SN class | $w_0,w_a$ away from $(-1,0)$ at **2.5σ–4.2σ** (dataset-dependent) | Preference for **dynamical mean DE** in CPL |
| This programme BAO-only | $w_0\approx -0.99$, $w_a\approx -0.02$ | Nearly $\Lambda$ under BAO-only diagonal baseline |

**Illegal:** paste 2.5σ–4.2σ into a table labelled “H0 running significance.”  
**Legal:** cite H0-running papers (Dainotti, Krishnan, Wong trend $\sim 1.9\sigma$) with **their** numbers.

---

## 6. Verdict table

| Element | Verdict |
|:--------|:--------|
| Desqueezing + complex $\omega$ | Keep |
| H0-running as literature | Keep (with caveats) |
| Invented $H_0(z)=H_{0,\mathrm{fid}}[1+\varepsilon e^{-\theta x}]$ | **Reject** |
| $\theta$ fitted to $z\sim 0.5$–$0.7$ | **Reject** |
| $\sigma_X$ “spatial only” | **Reject** (false) |
| 2.5σ–4.2σ as H0-running | **Reject / relabel as CPL** |
| Can desqueezing $\theta$ move $H_0$ by 9% under $\sigma_X$ bound? | **No** ($\lesssim 0.015\%$ ceiling) |

---

## 7. Claim checklist

| ID | Claim |
|:---|:------|
| F1 | $t_{1/2}=\ln 2/\gamma$ is programme-validated |
| F2 | $\sigma_X$ is defined on $x=\ln a$ (temporal e-folds) |
| F3 | $\lvert\delta H/H\rvert\lesssim\sigma_X<1.5\times 10^{-4}\ll 0.083$ under residual identification |
| F4 | Hand-tuned $\theta\sim 0.47$ is illegal |
| F5 | BAO-only $(w_0,w_a)\approx(-0.99,-0.02)$ |

---

## 8. Reproduce

```bash
cd measurable-stochastic-vacuum
python scripts/closed/h0_desqueezing_filter.py
python scripts/closed/h0_bridge_toy.py
pytest -q
```

Sister:
```bash
# BAO-only w0,wa
cat results/eos_cpl_desi_dr2/eos_cpl_summary.txt
```
