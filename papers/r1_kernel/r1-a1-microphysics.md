# Microphysics of A1: where can \(g\chi\delta_m\) come from?

**Author:** Jesús Morales Souhail  
**Date:** July 2026  
**Status:** Ranked microphysics map for postulate A1 — not a derivation of \(g\) from the Standard Model  
**Depends on:** [`r1-derivation-sandwich.md`](r1-derivation-sandwich.md) · [`r1-mechanism-candidates.md`](r1-mechanism-candidates.md) · [`OBSERVABLE_WALL.md`](../core/OBSERVABLE_WALL.md)

---

## Abstract

The sandwich uniqueness theorem needs **A1**: a local coupling between residual sector \(\chi\) and matter contrast \(\delta_m\),
\[
\mathcal{L}_{\mathrm{int}}=g\,\chi\,\delta_m
\quad\text{(or density form }g\,\chi\,\rho_m\text{)}.
\]
This note asks the only remaining microphysical question at the same level of seriousness:

> **What known or semi-standard frameworks can generate an effective operator of this form without inventing a free mesoscopic dial?**

We rank candidates by: (i) naturalness of locality; (ii) whether \(\chi\) is new or emergent; (iii) compatibility with SDiff / isotropic-mean projection (A0); (iv) risk of reintroducing free \(10^{56}\) or mean-\(\Lambda\) overclaim.

**Result:** A1 is **not** forced by the Standard Model alone, but it is **not** an arbitrary invention either — several Tier-1 frameworks already produce residual–matter mixing at structure scales. The sandwich + DESI bound then fix \(\lvert g\rvert\lesssim\mathcal{O}(1)\) under the programme normalisation.

---

## 1. What A1 must deliver

| Requirement | Why |
|:------------|:----|
| **Local in space** | UV/IR sandwich lemmas use local monitoring by \(\delta_m\) |
| **Couples to \(\delta_m\) (or \(\rho_m\))** | Pointer basis = nonlinear matter patches |
| **Does not source a large homogeneous \(\langle\chi\rangle\)** | A0 / BAO \(w_0,w_a\approx\Lambda\) |
| **Effective strength** \(\lvert g\rvert\sim\mathcal{O}(1)\) allowed, \(\gg 1\) disfavoured | Working bound from DESI residual |
| **Scale of support** \(\sim R_{\mathrm{nl}}\) | Follows from sandwich once A1 holds — not a second dial |

**Illegal:** invent \(\chi\) *and* set \(\ell_*\) by hand *and* amplify from Planck.

---

## 2. Tier 1 — most coherent with the programme

### M1. Emergent residual from averaging / backreaction (Buchert / multiscale)

| | |
|:--|:--|
| **Idea** | Nonlinear Einstein equations averaged on domain \(L_{\mathrm{av}}\sim R_{\mathrm{nl}}\) produce effective sources \(Q\), averaged curvature, and **fluctuations about the average**. Those fluctuations play the role of \(\chi\). |
| **Coupling** | By construction, backreaction is sourced by \(\delta_m\) inhomogeneity — effective \(g\chi\delta_m\) is **emergent**, not a new fundamental field. |
| **A0 fit** | Mean acceleration from \(Q\) is **contested** and **not** claimed here; only the **residual** about the average is used (programme residual, not mean DE). |
| **Literature** | Buchert arXiv:0707.2153; Wiegand & Buchert arXiv:1002.3912 |
| **Risk** | Literature often targets mean DE; we must keep residual-only discipline. |
| **Verdict** | **Best match:** \(\chi\) need not be fundamental; A1 is structural to averaging. |

### M2. SDiff / unimodular residual at structure edges

| | |
|:--|:--|
| **Idea** | Isotropic vacuum stress is projected out (unimodular / SDiff). Residual anisotropic stress lives where conformal / volume-preserving symmetry is broken by structure — edges of \(\delta_m\sim\mathcal{O}(1)\) regions. |
| **Coupling** | Residual support \(\propto\) nonlinear mask \(\Rightarrow\) effective coupling to \(\delta_m\) on edges. |
| **A0 fit** | Exact design goal of programme bulk–edge language. |
| **Literature** | Unimodular gravity corpus; programme [`OBSERVABLE_WALL.md`](../core/OBSERVABLE_WALL.md), [`TOPOLOGICAL_EDGE_ANALOGY.md`](../side_threads/TOPOLOGICAL_EDGE_ANALOGY.md) (pedagogy only for CM analogy). |
| **Risk** | Without a derived residual operator, still semi-phenomenological. |
| **Verdict** | **Strong programme fit;** pairs with T1.2 mask geometry (\(r_{e,\mathrm{mask}}\approx 1.1 R_{\mathrm{nl}}\)). |

### M3. Environment-induced residual from open GR + matter bath

| | |
|:--|:--|
| **Idea** | Matter is the environment; gravitational / vacuum degrees of freedom are the system. Influence functionals (Feynman–Vernon) generate decoherence and effective residual noise correlated with \(\delta_m\). |
| **Coupling** | \(g\) is the system–bath coupling strength in the influence functional; locality follows if interaction is local. |
| **A0 fit** | Homogeneous mode can be projected or redressed into mean \(\Lambda\); residual is the fluctuating influence. |
| **Literature** | Burrage et al. influence functionals arXiv:1902.09607; Kiefer-class decoherence→effective \(\Lambda\) (usually mean, methods reusable). |
| **Risk** | Easy to overclaim mean \(\Lambda\) from decoherence; keep residual-only. |
| **Verdict** | **Best formal language** for Lemma UV; still needs a concrete gravitational DOF for \(\chi\). |

---

## 3. Tier 2 — serious but weaker map

### M4. Light spectator DE field (Gordon–Wands class)

| | |
|:--|:--|
| **Idea** | A light field \(Q\) during inflation seeds \(\delta Q\); late residual can couple to matter if non-minimal or through metric. |
| **Why weaker for A1** | Natural seed is inflationary, not necessarily \(R_{\mathrm{nl}}\)-local coupling today; needs extra map to mesoscopic grain (see spectator notes). |
| **Use** | Changes UV seed so Planck count is not mandatory; **does not by itself** give A1 at \(R_{\mathrm{nl}}\). |
| **Ref.** | [`inflation-spectator-seed-gordon-wands.md`](../side_threads/inflation-spectator-seed-gordon-wands.md) |

### M5. EFT of DE with matter operators

| | |
|:--|:--|
| **Idea** | Cosmological EFT allows operators \(\delta g^{00}\delta_m\), braiding, etc. |
| **Why weaker** | Usually organised about FLRW + linear perturbations; nonlinear \(R_{\mathrm{nl}}\) grain is not automatic. |
| **Use** | Language for writing \(g\chi\delta_m\) as a low-energy operator with Wilson coefficient \(g\). |
| **Ref.** | Gubitosi et al. arXiv:1210.0201 class; nonlinear EFT of DE arXiv:1712.02782 |

### M6. Disformal / conformal matter couplings of a residual scalar

| | |
|:--|:--|
| **Idea** | \(\tilde g_{\mu\nu}=A(\chi)g_{\mu\nu}+B(\chi)\partial_\mu\chi\partial_\nu\chi\) induces matter–\(\chi\) mixing. |
| **Why intermediate** | Standard scalar–tensor toolkit; screening (chameleon/Vainshtein) can hide fifth forces in Solar System while leaving cosmological residual. |
| **Risk** | Fifth-force bounds; must not revive \(H_0\) from large \(g\). |
| **Verdict** | Viable **if** \(\chi\) is fundamental scalar; more assumptions than M1–M3. |

---

## 4. Tier 3 — deprioritize for A1

| Candidate | Why weak here |
|:----------|:--------------|
| Pure holographic DE with \(L=H^{-1}\) | Wrong scale (Gpc); mean DE focus |
| Ad hoc \(\chi\) with free \(\ell_*\) and free \(g\) | Double dial; fails self-shielding |
| Soft squeeze of Sorkin seed to set effective \(g\) | Wall: needs \(r\sim 64\) |
| Fitting \(g\) to Maus \(\gamma-1\sim 0.1\) | Illegal (wrong amplitude + dial) |

---

## 5. Recommended microphysics path (ordered)

```
1) Prefer emergent χ (M1 averaging residual) or SDiff edge residual (M2)
   → A1 is structural, not a new particle
2) Write influence-functional / master-equation form (M3)
   → makes Lemma UV quantitative beyond OOM
3) If χ must be fundamental, use EFT operator language (M5) + screening (M6)
4) Spectator seed (M4) only for UV history, not as substitute for A1 locality
```

**Programme default stance:**  
\(\chi\) is the **residual about the isotropic vacuum mean** after SDiff projection and/or spatial averaging on \(R_{\mathrm{nl}}\) — **emergent**, not a fifth force dark-energy particle tuned to galaxies.

---

## 6. How \(g\) is bounded once A1 is granted

Under programme normalisation \(\langle\chi^2\rangle^{1/2}_{\mathrm{free}}=\sigma_{\mathrm{free}}\) and \(\lambda=g\sigma_{\mathrm{free}}\) (with \(\kappa=1\)):

| Bound | Value | Source |
|:------|:------|:-------|
| Working \(\lvert\lambda\rvert\) | \(\lesssim 1.24\times 10^{-4}\) | DESI \(\sigma_X\) map |
| Working \(\lvert g\rvert\) | \(\lesssim 1.45\) | Stage-0 / profile |
| Formal BAO full-cov | Not informative at \(10^{-4}\) | background thrashing |

So A1 does **not** open a free \(g\sim 10^{2}\) window: BAO residual already forces \(\lvert g\rvert\lesssim\mathcal{O}(1)\).

---

## 7. Falsifiers specific to microphysics choice

| Microphysics | Dies if… |
|:-------------|:---------|
| M1 averaging residual | Residual shown uncorrelated with \(\delta_m\) structure masks at all scales |
| M2 SDiff edge | Residual support found in voids only, anti-correlated with edges, at high significance |
| M3 open-system | Decoherence rate bounds from precision tests exclude \(g\sim\mathcal{O}(1)\) for that DOF |
| M6 fifth force | Solar-System / equivalence-principle bounds force \(g\to 0\) without screening that also kills cosmology |

---

## 8. Claim checklist

| ID | Claim | Status |
|:---|:------|:-------|
| A1-1 | A1 is a postulate, not SM theorem | explicit |
| A1-2 | M1–M3 provide non-ad-hoc effective A1 | ranked map |
| A1-3 | \(\lvert g\rvert\lesssim\mathcal{O}(1)\) under DESI working map | computed elsewhere |
| A1-4 | Emergent residual preferred over new force | programme stance |

| Non-claim | |
|:----------|:--|
| N-A1 | Proof that Buchert \(Q\) is dark energy |
| N-A2 | Detection of \(\chi\) |
| N-A3 | Unique microphysics selected by data |

---

## 9. One-sentence status

> A1 need not be an invented fifth force: averaging residuals, SDiff edge stress, and open-system influence functionals all generate effective \(g\chi\delta_m\)-like mixing; once granted, the sandwich fixes \(\ell_*\sim R_{\mathrm{nl}}\) and DESI bounds \(\lvert g\rvert\lesssim\mathcal{O}(1)\).

---

*End of A1 microphysics map.*
