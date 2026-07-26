# Uniqueness of the residual vacuum grain under local coupling to nonlinear structure

**Author:** Jesús Morales Souhail  
**ORCID:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Email:** jmskjym@gmail.com  
**Affiliation:** Independent researcher  
**Date:** July 2026  
**Status:** Programme note intended as a **short paper draft** — **not peer reviewed**  
**Code:** https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum  
**Sister empirical bound:** \(\sigma_X<1.5\times 10^{-4}\) (95% CL), [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou)

---

## Abstract

Standard cosmology treats dark energy as a homogeneous background (\(\Lambda\) or a smooth field). We consider a residual sector \(\chi\) that does **not** source the mean expansion after isotropic projection, but may retain a mesoscopic correlation length \(\ell_*\). Under four axioms — residual sector; local coupling to matter contrast; classicality of matter on nonlinear scales; and counting of free residual degrees of freedom after decoherence — we prove a **sandwich uniqueness** result: free residual cells much smaller than the matter nonlinear scale \(R_{\mathrm{nl}}\) are decohered, while cells much larger renormalize to \(R_{\mathrm{nl}}\) under local coupling. Hence
\[
\ell_*\sim R_{\mathrm{nl}}.
\]
With a standard top-hat variance integral we find \(R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}\) (\(\sigma_8=0.81\)). Volume counting then gives residual amplitude \(\sigma\approx 8.5\times 10^{-5}\) (\(d=3\)), under the DESI residual ceiling. The correlation length of the Gaussian threshold mask \(\delta>1\) is \(r_{e,\mathrm{mask}}\approx 1.11\,R_{\mathrm{nl}}\). We pre-register falsifiers and bound the dimensionless coupling \(\lvert g\rvert\lesssim\mathcal{O}(1)\). We do **not** claim a derivation of \(\chi\) from the Standard Model, nor a solution of the \(H_0\) tension.

**Keywords:** dark energy residual, nonlinear scale, decoherence, gravitational slip, DESI

---

## 1. Introduction

Late-time acceleration is described by \(\Lambda\)CDM with high success on the mean expansion. Whether the dark-energy sector admits a **residual**, stochastic, or granular component at mesoscopic scales is a different question. Amplifying a pure Planck/Sorkin holographic seed \(\sigma_0\sim 10^{-61}\) into a telescope-band residual \(\sim 10^{-5}\) requires soft gains of order \(10^{56}\), which have been audited and closed as free amplifiers in companion work.

An alternative is to change the **counting cell**: if residual degrees of freedom are counted on a mesoscopic length \(\ell_*\) rather than \(L_P\), the amplitude
\[
\sigma=\Bigl(\frac{\ell_*}{L_H}\Bigr)^{d/2}
\]
can sit near \(10^{-5}\)–\(10^{-4}\) without soft amplification. The open problem is then: **what fixes \(\ell_*\)?**

This note proposes a conditional answer. We do not claim that dark energy “knows about galaxies” by assertion. We show that **if** a residual couples locally to classical nonlinear matter, then \(\ell_*\) is forced to the matter nonlinear scale \(R_{\mathrm{nl}}\) defined by \(\sigma(R_{\mathrm{nl}})=1\).

This connection is **not** standard lore. It is a new hypothesis of the programme, elevated here to a uniqueness theorem under stated axioms.

---

## 2. Axioms

| ID | Statement |
|:---|:----------|
| **A0** | A residual sector \(\chi\) exists; its isotropic mean is projected out (SDiff / unimodular-type structural zero). Observables care about fluctuations about that mean. |
| **A1** | Local interaction \(\mathcal{L}_{\mathrm{int}}=g\chi\delta_m\) (or density form). |
| **A2** | On filters with matter variance \(\sigma(R)\ge 1\), \(\delta_m\) is effectively classical, organised in nonlinear patches of size \(\sim R_{\mathrm{nl}}\). |
| **A3** | Free residual DOF after environment-induced decoherence are counted as \(N=(L_H/\ell_*)^d\), \(\sigma=N^{-1/2}\). |
| **A4** | No free soft gain \(\sim 10^{56}\) from a pure Planck seed. |

**Scope:** Results below are theorems **under A0–A4**. Existence of \(\chi\) (A0) and the coupling (A1) remain physical postulates; possible microphysical origins (averaging residual, SDiff edge stress, open-system influence functionals) are discussed in companion notes and are not required for the uniqueness algebra.

---

## 3. Sandwich uniqueness

### 3.1 UV lemma

If \(\chi\) couples locally to classical \(\delta_m\) coherent on patches of size \(R_{\mathrm{nl}}\), residual configurations that differ **within** a single patch are monitored by the same classical record. Open-system / influence-functional logic suppresses such coherences when \(g\sigma_\delta\) is not parametrically tiny. The effective free residual field is therefore the **patch average**
\[
\chi_{\mathrm{eff}}(p)=\frac{1}{V_p}\int_p\chi.
\]
**Consequence:** free residual counting cells with \(\ell\ll R_{\mathrm{nl}}\) are not available.

### 3.2 IR lemma

If one posits a free residual cell \(\ell\gg R_{\mathrm{nl}}\), local coupling implies the interaction is a sum of contributions from \(N_p=(\ell/R_{\mathrm{nl}})^d\) independent nonlinear patches. The independent residual DOF are the patch modes; averaging them yields
\[
\sigma_{\mathrm{eff}}(\ell)=\frac{\sigma(R_{\mathrm{nl}})}{\sqrt{N_p}},
\]
i.e. the same counting as if the cell were \(R_{\mathrm{nl}}\). Super-cells **renormalize** to \(R_{\mathrm{nl}}\).

### 3.3 Theorem

Under A0–A4,
\[
\boxed{\ell_*\sim R_{\mathrm{nl}}\qquad\text{(unique free residual scale up to \(\mathcal{O}(1)\) geometry).}}
\]

Geometric \(\mathcal{O}(1)\) factors from the same filtered matter field include the density correlation length \(r_{e,\delta}\), the threshold-mask correlation length \(r_{e,\mathrm{mask}}\), packing separation of \(\delta>1\) regions, and BBKS peak curvature \(R_*\) (substructure **inside** the domain, not an independent free residual cell under the UV lemma).

---

## 4. Geometry and amplitude

### 4.1 Nonlinear scale

\[
\sigma^2(R)=\int_0^\infty\frac{\mathrm{d}k}{k}\,\Delta^2(k)\,W_{\mathrm{TH}}^2(kR),\qquad
W_{\mathrm{TH}}(x)=\frac{3(\sin x-x\cos x)}{x^3}.
\]
With an Eisenstein–Hu–style \(P(k)\) normalized to \(\sigma_8=0.81\) and \(h=0.674\),
\[
R_{\mathrm{nl}}\approx 5.80\,h^{-1}\mathrm{Mpc}\approx\mathbf{8.61\,\mathrm{Mpc}}.
\]
No DESI residual number enters this solve.

### 4.2 Mask correlation (executed)

For Gaussian threshold \(m=\mathbf{1}\{\delta>1\}\) at filter \(R_{\mathrm{nl}}\),
\[
r_{e,\mathrm{mask}}\approx 9.53\,\mathrm{Mpc}\approx\mathbf{1.11}\,R_{\mathrm{nl}}.
\]
Density correlation: \(r_{e,\delta}\approx 14.6\,\mathrm{Mpc}\approx 1.69\,R_{\mathrm{nl}}\).  
Packing separation of \(\delta>1\) patches: \(\ell_{\mathrm{sep}}\approx 15.9\,\mathrm{Mpc}\).

### 4.3 Counting amplitude

With \(\ell_*=R_{\mathrm{nl}}\), \(d=3\), \(L_H=c/H_0\),
\[
\sigma_{\mathrm{free}}=\Bigl(\frac{R_{\mathrm{nl}}}{L_H}\Bigr)^{3/2}\approx\mathbf{8.5\times 10^{-5}}.
\]
This lies under the sister DESI BAO residual ceiling \(\sigma_X<1.5\times 10^{-4}\) (95% CL, OU/QNM kernel).

### 4.4 Coupling bound

Writing induced residual \(\lambda\) with \(\sigma_{\mathrm{res}}^2=\sigma_{\mathrm{free}}^2+\lambda^2\) and convention \(\lambda=g\sigma_{\mathrm{free}}\),
\[
\lvert\lambda\rvert\lesssim 1.24\times 10^{-4},\qquad
\lvert g\rvert\lesssim 1.45
\]
under the working DESI map. Formal full-covariance profile likelihoods on absolute \(D/r_d\) are **not** informative at \(10^{-4}\) because \(\chi^2_{\Lambda\mathrm{CDM}}\sim 29\) is absorbed by covariance inflation — the working ceiling remains the primary bound.

---

## 5. Decoherence OOM

For \(\Gamma\sim g^2\sigma_\delta^2/\tau_c\) with \(\sigma_\delta=1\):

| \(g\) | \(\Gamma/H_0\) (slow bath \(\tau_c\sim H_0^{-1}\)) | \(\Gamma/H_0\) (fast bath \(\tau_c\sim R_{\mathrm{nl}}/c\)) |
|:------|:--------------------------------------------------|:----------------------------------------------------------|
| \(1\) | \(\sim 1\) | \(\sim 5\times 10^{2}\) |
| \(g_{\mathrm{work}}\approx 1.45\) | \(\sim 2\) | \(\sim 10^{3}\) |

Order-unity \(g\) yields decoherence within cosmological timescales, consistent with the UV lemma.

---

## 6. Falsifiers (pre-registered)

| Gate | Kill condition |
|:-----|:---------------|
| **F1 BAO** | Residual \(\sigma_{\mathrm{res}}\gg 1.5\times 10^{-4}\) at **fixed** \(\ell_*=R_{\mathrm{nl}}\) without derived damping |
| **F2 Scale** | Free residual correlation length at \(\sigma\sim 10^{-4}\) measured \(\ll 1\,\mathrm{Mpc}\) or \(\gg 100\,\mathrm{Mpc}\) |
| **F3 Slip** | Stochastic path-RMS / slip proxy far above Maus/Sakr floors without systematics budget (today predictions sit \(\ll\) floors) |
| **F4 Method** | Post-hoc fit of \(\ell_*\) to DESI; free \(10^{56}\); rebrand Stage-IV shear \(m\sim 10^{-3}\) as residual-texture detection |

**Illegal:** adjusting \(\ell_*\) after looking at residual data.

---

## 7. What we do not claim

1. That the Standard Model + GR **must** contain \(\chi\).  
2. A microscopic derivation of \(g\) (only \(\lvert g\rvert\lesssim\mathcal{O}(1)\) a posteriori).  
3. Explanation of the \(\sim 9\%\) \(H_0\) tension (amplitude short by \(\sim 10^{2}\)–\(10^{3}\) under DESI-safe residual).  
4. That Stage-IV mean slip already tests path-RMS at \(10^{-3}\).  
5. Peer-reviewed status.

---

## 8. Discussion

The scientific content of this note is a **narrowing of the open problem**. Before: any mesoscopic \(\ell_*\) in a broad band could be entertained. After: under local coupling to classical nonlinear matter, \(\ell_*\sim R_{\mathrm{nl}}\) is unique up to \(\mathcal{O}(1)\). The remaining question is whether nature realises a residual sector with that coupling — a sharper, falsifiable target.

Possible non-ad-hoc origins of A1 include: (i) residual fluctuations about spatial averages on nonlinear domains; (ii) SDiff/unimodular edge stress supported on nonlinear masks; (iii) open-system influence functionals with matter as bath. In all three, \(\chi\) need not be a new fifth-force particle.

---

## 9. Conclusions

Under residual sector + local coupling to classical nonlinear matter + post-decoherence counting, the free residual vacuum grain is uniquely
\[
\ell_*\sim R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc},
\]
with amplitude \(\sigma\sim 8.5\times 10^{-5}\) under present DESI residual limits and coupling \(\lvert g\rvert\lesssim\mathcal{O}(1)\). The result is conditional, quantitative, and falsifiable. It does not reinstate soft amplification of a Planck seed, and it does not solve \(H_0\).

---

## Acknowledgements / reproducibility

```bash
git clone https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum.git
cd measurable-stochastic-vacuum && pip install -r requirements.txt
python scripts/r1_sigma_R_full.py
python scripts/r1_sandwich_derivation.py
python scripts/r1_sandwich_falsifiers.py
python scripts/r1_bound_g_oom.py
pytest -q
```

Companion notes: `r1-derivation-sandwich.md`, `r1-a1-microphysics.md`, `r1-sandwich-falsifiers.md`, `r1-bounding-g-plan.md`.

---

## References (selected)

1. Bardeen, Bond, Kaiser, Szalay, ApJ 304, 15 (1986) — peak statistics.  
2. Buchert, arXiv:0707.2153 — averaging / backreaction.  
3. Eisenstein & Hu, ApJ 496, 605 (1998) — transfer function.  
4. Maus et al., arXiv:2505.20656 — DESI×CMB-lensing slip.  
5. Sakr et al., arXiv:2501.07477 — anisotropic stress forecasts.  
6. Programme repos: measurable-stochastic-vacuum; stochastic-dark-energy-ou.

---

*End of short paper draft.*
