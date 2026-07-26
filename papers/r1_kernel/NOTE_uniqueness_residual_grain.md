# Uniqueness of the residual vacuum grain under local coupling to nonlinear structure

Jesús Morales Souhail  
ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818) · jmskjym@gmail.com  
Independent researcher · July 2026  

*Draft note. Not peer reviewed.*  
Code: [measurable-stochastic-vacuum](https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum)  
Companion DESI residual bound \(\sigma_X<1.5\times 10^{-4}\) (95% CL): [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou)

---

## Abstract

In the standard cosmological model, dark energy is treated as a homogeneous background. Here we consider a residual sector \(\chi\) that does not source the mean expansion after isotropic projection, but may retain a mesoscopic correlation length \(\ell_*\). Under four axioms—existence of such a residual, local coupling to the matter density contrast, classicality of matter on nonlinear scales, and counting of free residual degrees of freedom after decoherence—we obtain a uniqueness result for the free residual scale: cells much smaller than the matter nonlinear scale \(R_{\mathrm{nl}}\) are not available as free residual modes, while cells much larger renormalize to \(R_{\mathrm{nl}}\) under local coupling. Thus \(\ell_*\sim R_{\mathrm{nl}}\).

Evaluating the top-hat variance integral with an Eisenstein–Hu–style transfer function normalized to \(\sigma_8=0.81\) yields \(R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}\). Volume counting with \(d=3\) then gives residual amplitude \(\sigma\approx 8.5\times 10^{-5}\), below the DESI residual ceiling from the companion analysis. The correlation length of a Gaussian threshold mask \(\delta>1\) is \(r_{e,\mathrm{mask}}\approx 1.11\,R_{\mathrm{nl}}\). Falsification criteria are stated, and the dimensionless coupling is bounded by \(\lvert g\rvert\lesssim\mathcal{O}(1)\) under the programme normalisation. We do not claim a derivation of \(\chi\) from the Standard Model, nor an explanation of the Hubble tension.

**Keywords:** dark energy residual; nonlinear scale; decoherence; gravitational slip; DESI

---

## 1. Introduction

The mean expansion history of the late universe is well described by flat \(\Lambda\)CDM. Whether the dark-energy sector also admits a residual, stochastic, or granular component on mesoscopic scales is a separate question. Starting from a pure Planck-scale holographic seed \(\sigma_0\sim 10^{-61}\) and reaching a residual of order \(10^{-5}\) under soft open-system maps requires a gain of order \(10^{56}\). That route has been examined in companion work and is not available without introducing a new hard scale.

An alternative is to change the counting cell. If residual degrees of freedom are counted on a mesoscopic length \(\ell_*\) rather than the Planck length, the amplitude
\[
\sigma=\Bigl(\frac{\ell_*}{L_H}\Bigr)^{d/2}
\]
can already lie near \(10^{-5}\)–\(10^{-4}\). The open problem is then what fixes \(\ell_*\).

This note gives a conditional answer. We do not assert that dark energy “knows about galaxies.” We show that if a residual couples locally to classical nonlinear matter, then \(\ell_*\) is forced to the matter nonlinear scale \(R_{\mathrm{nl}}\) defined by \(\sigma(R_{\mathrm{nl}})=1\). That identification is not standard lore; it is a hypothesis of this programme, developed here as a uniqueness argument under explicit axioms.

---

## 2. Axioms

| | Statement |
|:--|:----------|
| A0 | A residual sector \(\chi\) exists. Its isotropic mean is projected out (SDiff / unimodular-type structural zero). Observables concern fluctuations about that mean. |
| A1 | The residual couples locally to matter: \(\mathcal{L}_{\mathrm{int}}=g\chi\delta_m\) (or a density form of the same locality). |
| A2 | On filters with matter variance \(\sigma(R)\ge 1\), \(\delta_m\) is effectively classical and organised in nonlinear patches of size \(\sim R_{\mathrm{nl}}\). |
| A3 | After environment-induced decoherence, free residual degrees of freedom are counted as \(N=(L_H/\ell_*)^d\), with \(\sigma=N^{-1/2}\). |
| A4 | Soft maps do not introduce a free gain \(\sim 10^{56}\) from a pure Planck seed. |

Results below are conditional on A0–A4. Existence of \(\chi\) and the coupling in A1 remain physical postulates. Possible microphysical origins—averaging residuals, edge stress after isotropic projection, or influence functionals with matter as environment—are discussed elsewhere and are not required for the uniqueness algebra.

---

## 3. Uniqueness of the free residual scale

### 3.1 Ultraviolet side

If \(\chi\) couples locally to classical \(\delta_m\) that is coherent on patches of size \(R_{\mathrm{nl}}\), residual configurations that differ within a single patch are monitored by the same classical record. Standard open-system reasoning then suppresses such coherences when \(g\sigma_\delta\) is not parametrically small. The effective free residual is the patch average
\[
\chi_{\mathrm{eff}}(p)=\frac{1}{V_p}\int_p\chi.
\]
Free residual counting cells with \(\ell\ll R_{\mathrm{nl}}\) are therefore not available.

### 3.2 Infrared side

If one posits a free residual cell \(\ell\gg R_{\mathrm{nl}}\), local coupling implies that the interaction on that cell is a sum of contributions from \(N_p=(\ell/R_{\mathrm{nl}})^d\) independent nonlinear patches. The independent residual modes are those of the patches. Averaging them yields
\[
\sigma_{\mathrm{eff}}(\ell)=\frac{\sigma(R_{\mathrm{nl}})}{\sqrt{N_p}},
\]
which is the same counting as if the cell were \(R_{\mathrm{nl}}\). Super-cells renormalize to \(R_{\mathrm{nl}}\).

### 3.3 Result

Under A0–A4,
\[
\ell_*\sim R_{\mathrm{nl}},
\]
up to geometric factors of order unity fixed by the same filtered matter field (density correlation length, threshold-mask correlation length, packing separation of \(\delta>1\) regions, and BBKS peak curvature \(R_*\) as substructure inside the domain rather than as an independent free residual cell).

---

## 4. Geometry and amplitude

### 4.1 Nonlinear scale

\[
\sigma^2(R)=\int_0^\infty\frac{\mathrm{d}k}{k}\,\Delta^2(k)\,W_{\mathrm{TH}}^2(kR),\qquad
W_{\mathrm{TH}}(x)=\frac{3(\sin x-x\cos x)}{x^3}.
\]
With \(P(k)\) of Eisenstein–Hu type, \(n_s=0.965\), \(\Omega_m=0.315\), \(h=0.674\), and \(\sigma_8=0.81\),
\[
R_{\mathrm{nl}}\approx 5.80\,h^{-1}\mathrm{Mpc}\approx 8.61\,\mathrm{Mpc}.
\]
No DESI residual likelihood enters this determination.

### 4.2 Mask and packing scales

For a Gaussian threshold \(m=\mathbf{1}\{\delta>1\}\) at filter \(R_{\mathrm{nl}}\),
\[
r_{e,\mathrm{mask}}\approx 9.53\,\mathrm{Mpc}\approx 1.11\,R_{\mathrm{nl}}.
\]
The density correlation length is \(r_{e,\delta}\approx 14.6\,\mathrm{Mpc}\approx 1.69\,R_{\mathrm{nl}}\). Packing separation of \(\delta>1\) patches is \(\ell_{\mathrm{sep}}\approx 15.9\,\mathrm{Mpc}\).

### 4.3 Counting amplitude

With \(\ell_*=R_{\mathrm{nl}}\), \(d=3\), and \(L_H=c/H_0\),
\[
\sigma_{\mathrm{free}}=\Bigl(\frac{R_{\mathrm{nl}}}{L_H}\Bigr)^{3/2}\approx 8.5\times 10^{-5},
\]
which lies under the companion DESI BAO residual ceiling \(\sigma_X<1.5\times 10^{-4}\) (95% CL, OU/QNM kernel).

### 4.4 Coupling bound

Writing \(\sigma_{\mathrm{res}}^2=\sigma_{\mathrm{free}}^2+\lambda^2\) and \(\lambda=g\sigma_{\mathrm{free}}\),
\[
\lvert\lambda\rvert\lesssim 1.24\times 10^{-4},\qquad
\lvert g\rvert\lesssim 1.45
\]
under the working DESI map. Formal full-covariance profiles on absolute \(D/r_d\) at fixed background are not informative at the \(10^{-4}\) level, because a large \(\chi^2\) against the fiducial theory is absorbed by residual variance; the working ceiling remains the primary bound.

---

## 5. Decoherence estimate

With \(\Gamma\sim g^2\sigma_\delta^2/\tau_c\) and \(\sigma_\delta=1\), order-unity \(g\) gives \(\Gamma/H_0\sim\mathcal{O}(1)\) for a slow bath \(\tau_c\sim H_0^{-1}\), and larger rates if \(\tau_c\sim R_{\mathrm{nl}}/c\). That is consistent with the ultraviolet argument in Sec. 3.1 as an order-of-magnitude check, not a full influence-functional calculation.

---

## 6. Falsification criteria

| | Condition that excludes this form of the claim |
|:--|:-----------------------------------------------|
| F1 | Residual amplitude \(\sigma_{\mathrm{res}}\gg 1.5\times 10^{-4}\) at fixed \(\ell_*=R_{\mathrm{nl}}\) with no derived damping |
| F2 | Free residual correlation length at \(\sigma\sim 10^{-4}\) measured well below \(1\,\mathrm{Mpc}\) or well above \(100\,\mathrm{Mpc}\) |
| F3 | Stochastic slip path RMS forced far above published mean-slip floors without a systematics budget |
| F4 | \(\ell_*\) fitted after residual data are inspected; free \(10^{56}\) gain; shear multiplicative bias treated as residual-texture detection |

A survey-oriented protocol for residual–matter cross-correlation on the \(R_{\mathrm{nl}}\) band is given in a separate pre-registration note.

---

## 7. Scope

We do not claim that the Standard Model and general relativity must contain \(\chi\); that \(g\) is derived microscopically (only that \(\lvert g\rvert\lesssim\mathcal{O}(1)\) under the working residual ceiling); that the \(\sim 8\%\) Hubble tension is explained by this residual (the amplitude is short by two to three orders of magnitude under DESI-safe values); or that present mean-slip measurements test path-accumulated residuals at the \(10^{-3}\) level.

---

## 8. Discussion

The main content of the argument is a narrowing of the open problem. Without A0–A4, any mesoscopic \(\ell_*\) in a wide band remains possible. With local coupling to classical nonlinear matter, \(\ell_*\sim R_{\mathrm{nl}}\) up to order-unity geometry. The remaining question is whether nature realises a residual sector with that coupling.

Non-ad-hoc routes to A1 include residual fluctuations about spatial averages on nonlinear domains, residual stress supported on nonlinear masks after isotropic projection, and open-system influence functionals with matter as the environment. In those settings \(\chi\) need not be introduced as a new fifth-force field.

---

## 9. Conclusions

Under a residual sector, local coupling to classical nonlinear matter, and post-decoherence counting, the free residual scale is
\[
\ell_*\sim R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc},
\]
with amplitude \(\sigma\sim 8.5\times 10^{-5}\) under present DESI residual limits and coupling \(\lvert g\rvert\lesssim\mathcal{O}(1)\). The result is conditional, quantitative, and falsifiable. It does not restore soft amplification of a Planck seed, and it does not address the Hubble tension.

---

## Reproducibility

```bash
git clone https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum.git
cd measurable-stochastic-vacuum
pip install -r requirements.txt
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_sandwich_falsifiers.py
python scripts/r1/r1_bound_g_oom.py
pytest -q
```

Companion notes in this repository: `r1-derivation-sandwich.md`, `r1-a1-microphysics.md`, `r1-sandwich-falsifiers.md`, `r1-T2-preregistration.md`, `r1-lineA-g-from-averaging.md`.

---

## References

1. J. M. Bardeen, J. R. Bond, N. Kaiser, and A. S. Szalay, Astrophys. J. **304**, 15 (1986).  
2. T. Buchert, arXiv:0707.2153.  
3. D. J. Eisenstein and W. Hu, Astrophys. J. **496**, 605 (1998).  
4. M. Maus et al., arXiv:2505.20656.  
5. Z. Sakr, Y. Zheng, and S. Casas, arXiv:2501.07477.  
6. J. Morales Souhail, stochastic-dark-energy-ou and measurable-stochastic-vacuum (2026).
