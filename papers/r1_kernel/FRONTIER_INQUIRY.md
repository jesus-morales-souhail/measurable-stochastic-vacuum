# Frontier inquiry: after the \(H_0\) door closes

**Author:** Jesús Morales Souhail  
**Date:** July 2026  
**Status:** Research-programme reframe + ranked inquiry lines — **not** a detection paper  
**Depends on:** sandwich uniqueness · DESI \(\sigma_X\) · closed H0 walls  

---

## 0. Narrative shift (internal)

| Before (problem framing) | Now (frontier framing) |
|:-------------------------|:-----------------------|
| “The grain does not explain \(H_0\); the model fails the 8%.” | “We have an **upper bound** on the grain (\(\sigma\lesssim 10^{-4}\)). What physics lives in the remaining gap to 8%?” |
| “Force parameters to hit \(H_0^{\mathrm{loc}}/H_0^{\mathrm{CMB}}\sim 1.08\).” | “The model predicts a **fine signature** \(\sim 10^{-4}\)–\(10^{-3}\) at \(\ell_*\sim 8.6\,\mathrm{Mpc}\). Design Stage-IV falsifiers.” |
| “Why is the amplitude so small?” | “What **symmetry / coupling** fixes \(\ell_*=R_{\mathrm{nl}}\) and \(\lvert g\rvert\lesssim\mathcal{O}(1)\) without fine-tuning?” |

**Structural fact (numbers):**

| Quantity | Value | Ratio to 8% distance jump |
|:---------|:------|:--------------------------|
| DESI residual ceiling \(\sigma_X\) | \(1.5\times 10^{-4}\) | \(0.08/\sigma_X\sim\mathbf{530}\) |
| Free-grain \(\sigma\) at \(R_{\mathrm{nl}}\) | \(8.5\times 10^{-5}\) | \(\sim 940\times\) short of 8% |
| Path \(\mathrm{RMS}\) (working) | \(\sim 2.5\times 10^{-3}\) | \(\sim 30\)–\(55\times\) short of 8% |

The grain is **not** a failed \(H_0\) model. It is a **successful upper-bound + scale-structure programme** in the \(10^{-5}\)–\(10^{-4}\) window. The 8% is a **different physical problem**.

---

## 1. Inversion questions (change the problem focus)

### I1. If the vacuum grain is **not** responsible for the \(\sim 8\%\) \(H_0\) tension, what physics **can** generate an 8% jump without violating DESI \(\sigma_X\lesssim 10^{-4}\) on mesoscopic scales?

**Logical filter.** Any mechanism \(M\) that produces \(\Delta H/H\sim 8\%\) (or \(\Delta D/D\sim 8\%\) on local ladders) must **not** inject a **stationary BAO residual** of amplitude \(\gtrsim 10^{-4}\) on the DESI OU/QNM kernel at the redshifts and scales where the sister bound applies.

| Class of mechanism | Can it give \(\sim 8\%\)? | Compatible with \(\sigma_X\lesssim 10^{-4}\)? | Notes |
|:-------------------|:-------------------------|:-----------------------------------------------|:------|
| **A. Early-universe / pre-recombination** (early DE, \(N_{\mathrm{eff}}\), recombination) | Yes (standard literature path) | **Yes** — acts on CMB sound horizon / early \(H(z)\), not as late residual on BAO \(\alpha(z)\) kernel | Changes \(r_d\) or early expansion; **orthogonal** to residual grain |
| **B. Local calibration systematics** (Cepheid metallicity, SN colour, anchor distances) | Yes (partial; contested) | **Yes** — not a cosmological residual field | “Physics” of measurement chain, not DE grain |
| **C. Local void / bulk flow / inhomogeneity on \(\gtrsim 100\,\mathrm{Mpc}\)** | Possibly OOM | **If** it does **not** look like OU residual on DESI BAO bins | Must be tested as large-scale structure, not \(\sigma_X\) |
| **D. Late modified gravity / evolving \(w(z)\) mean** | Possibly | **Only if** mean \(w(z)\) fits BAO+SN **and** residual about that mean stays \(\lt 10^{-4}\) | Mean DE ≠ residual grain; sister null is on **stochastic residual**, not all DE models |
| **E. Stochastic DE residual at \(\sigma\sim 10^{-4}\)** | **No** — short by \(\sim 10^{2}\)–\(10^{3}\) | Already at ceiling | **Closed as \(H_0\) solution** |
| **F. Soft Planck amplification \(10^{56}\)** | Numerically yes if free | Illegal / closed wall | Not a mechanism |

**Answer in one sentence:**  
Physics that can inhabit the 8% gap while respecting DESI residual bounds is **either early-universe / sound-horizon physics, local distance-ladder systematics, or large-scale mean (not residual) inhomogeneity/MG** — not a mesoscopic stochastic DE grain at \(\sigma\sim 10^{-4}\).

**Programme role:** we **do not** compete with early DE for \(H_0\). We **own** the residual window and the grain-scale uniqueness problem.

---

### I2. What fundamental property of the **local** universe (\(z\lt 0.15\)) breaks symmetry with the early universe (\(z\sim 1100\)) if it is **not** a stochastic DE fluctuation?

Candidates that **do not** require residual DE grain:

| Property | Symmetry broken | Why not residual grain |
|:---------|:----------------|:------------------------|
| **Density environment** (Local Group / local void) | Homogeneous FLRW assumption at \(z\sim 0\) | Spatial mean density, not DE noise |
| **Calibration chain** (anchors, SN sample) | “Same \(H_0\) estimator at all \(z\)” | Instrumental / astrophysical |
| **Growth / peculiar velocities** | Pure Hubble flow at low \(z\) | Matter kinematics |
| **Photometric vs spectroscopic selection** | Identical tracer populations | Sample variance / bias |
| **Sound horizon scale fixed at \(z\sim 1100\)** vs **local absolute ladder** | Single absolute calibration | Early vs late **rulers**, not residual \(\sigma_X\) |

**Answer:** the sharpest symmetry break is **not** “DE becomes noisy at low \(z\)” (ruled out at the amplitude needed for 8%). It is the **mismatch between an early absolute scale (\(r_d\))** and a **local absolute scale (ladder)**, and/or **local structure + calibration**. Residual grain is a **third, smaller** sector.

---

## 2. Fine inquiry (where the model **does** live: \(\sigma\sim 10^{-5}\)–\(10^{-4}\))

### F1. How to **deduce** \(g\) from first principles (SM / quantum gravity / averaging), not only from DESI?

| Path | Status | Next concrete step |
|:-----|:-------|:-------------------|
| **M1 Averaging** | Best emergent \(\chi\) | Estimate \(\mathrm{Var}(Q)\) / residual about Buchert average on \(L_{\mathrm{av}}=R_{\mathrm{nl}}\) → effective \(g_{\mathrm{eff}}\) |
| **M2 SDiff edge** | Best A0 fit | Residual stress \(\pi_T\propto f_{\mathrm{edge}}\sigma\) → map to \(g\) via slip wall |
| **M3 Influence functional** | Best UV lemma language | Write Feynman–Vernon kernel with \(\delta_m\) bath; match \(\Gamma\) to § sandwich OOM |
| SM only | No natural DE residual scalar | Do **not** force; emergent preferred |
| Quantum gravity (generic) | Too underdetermined | Only if it predicts mesoscopic cell \(R_{\mathrm{nl}}\) |

**Honest bar:** a true first-principles \(g\) is **not** available today. Mature goal: **\(g_{\mathrm{eff}}\) from averaging residual variance**, order-of-magnitude, compared to DESI \(\lvert g\rvert\lesssim 1.45\).

### F2. Exact influence functional (Feynman–Vernon) with collapsed matter as bath

**Target equation (programme form):** for residual field \(\chi\) and classical matter record \(m=\delta_m\),
\[
\mathcal{F}[\chi^+,\chi^-]
=\exp\Biggl(
-\frac{1}{\hbar}\int\mathrm{d}^4x\,\mathrm{d}^4x'\,
\Delta\chi(x)\,N(x,x')\,\Delta\chi(x')
+\mathrm{i}\,(\text{noise kernel / dissipation})
\Biggr),
\]
with noise kernel \(N\) built from \(\langle\delta_m(x)\delta_m(x')\rangle\) on the nonlinear mask (correlation length \(\sim R_{\mathrm{nl}}\)).

**What we have:** OOM \(\Gamma\sim g^2\sigma_\delta^2/\tau_c\) (sandwich script).  
**What is missing:** relativistic, gauge-fixed kernel on FLRW+structure; decoherence functional for patch modes only.

**Status:** **Frontier WP-IF** (influence functional), not closed.

### F3. Alternative observables for Stage-IV (uniqueness of signature)

If invisible in global luminosity distance at \(10^{-4}\), where does a **unique** signature live?

| Observable | Expected size (working point) | Unique to residual grain? | Stage-IV readiness |
|:-----------|:------------------------------|:--------------------------|:-------------------|
| BAO residual \(\sigma_X\) (OU/QNM) | \(\lesssim 10^{-4}\) | Primary definition | DESI now; deeper with DR3/Euclid BAO |
| Gravitational slip \(\eta=\Phi/\Psi\) **mean** | \(\lvert\gamma-1\rvert_{\mathrm{loc}}\sim 10^{-4}\) | No (MG degeneracy) | Maus \(\sim 0.1\) still \(\sim 10^{3}\times\) coarse |
| Path-accumulated slip RMS | \(\sim(1{-}3)\times 10^{-3}\) | Partially (stochastic path) | Needs dedicated proxy; not \(m\)-bias |
| Weak lensing higher \(N\)-point / trispectrum | OOM: residual modulates edges at \(R_{\mathrm{nl}}\) | **Scale peak near \(k\sim 1/R_{\mathrm{nl}}\)** if residual tracks mask | Hard; Stage-IV possible long-term |
| Residual–matter cross power \(P_{\chi\delta}\) | \(\propto g\,P_{\delta\delta}\) on nonlinear scales | **Yes if \(\chi\) measured** | Requires residual tracer (indirect via slip) |

**Design principle:** the unique fingerprint is **not** “8% in \(H_0\)”. It is  
**correlation of a DESI-safe residual with nonlinear structure on \(\sim 8\)–\(16\,\mathrm{Mpc}\)** (mask / \(R_{\mathrm{nl}}\) / \(\ell_{\mathrm{sep}}\)).

---

## 3. Causality and information (read the photon path differently)

### C1. Is transit across \(R_{\mathrm{nl}}\) equal to Shannon / von Neumann information loss on the wavefront?

**Careful answer:**  
- **Analogically:** each independent patch can imprint an uncorrelated phase / slip residual → path entropy \(\sim \tfrac12\log N_{\mathrm{pat}}\) bits of classical ignorance if one only measures the integrated path.  
- **Not automatic:** Shannon/von Neumann loss requires a **defined quantum state** of the EM field + environment. Programme path RMS \(s\sqrt{N}\) is **classical statistics of iid patches**, not yet a derived \(S_{\mathrm{vN}}\).  
- **Mature claim level:** “incoherent accumulation of residual slip across \(N\sim \chi/R_{\mathrm{nl}}\) patches” — **yes, verified kinematics**.  
- “Photon decoherence entropy equals that” — **open formalisation** (WP-INFO).

### C2. Past light cone / “retrocausal” observer-to-source transport: is residual an entropy-of-transport term?

**Programme language (safe):**  
Observables are integrals along the **past light cone** (already in `PAST_LIGHT_CONE_INTEGRATION`). Writing the integral from the observer outward is a **coordinate choice on the same null geodesic**, not retrocausality in the dynamical sense.

**If** one packages residual slip as a stochastic source along the ray,
\[
\frac{\mathrm{d}\varphi}{\mathrm{d}\chi}=s(\chi),\qquad
\mathrm{RMS}(\varphi)=s\sqrt{N},
\]
then \(\varphi\) is a **transport noise** term. Calling it “entropy of transport” is valid **only after** defining an ensemble and an information measure on wavefront modes.

**Status:** kinematics ready; thermodynamic/information layer is **frontier**, not established.

**Illegal:** complex \(W=F\cdot d\) with imaginary parts **fitted** to \(H_0\) — same class as desqueezing filter (closed).

---

## 4. Three inquiry lines — ordered attack

```
LINE A — Microphysics of g          [FOUNDATION]
         Einstein averaging residual / SDiff edge → g_eff
              ↓
LINE B — Stage-IV test design       [FALSIFIABILITY]
         Unique signature: residual × structure at R_nl
              ↓
LINE C — Information / entropy      [OPTIONAL DEPTH]
         Formalise path entropy only after A+B definitions fixed
```

| Line | Goal | Success metric | First deliverable |
|:-----|:-----|:---------------|:------------------|
| **A** | \(g_{\mathrm{eff}}\) OOM from averaging or edge stress | \(\lvert g_{\mathrm{eff}}\rvert\) vs DESI \(\lesssim 1.45\) | Script + note: \(\mathrm{Var}(Q)\) proxy / edge fraction |
| **B** | Pre-registered Stage-IV test | Scale-dependent residual–matter cross or BAO residual at fixed \(\ell_*=R_{\mathrm{nl}}\) | Test protocol note + forecast table |
| **C** | Info metric on past light cone | \(S\sim f(N_{\mathrm{pat}})\) derived from same \(s,N\) | Only after B’s observable is fixed |

**Default programme order: A ∥ B first (parallel), C later.**  
Do **not** open C as a path to \(H_0\).

---

## 5. Decision rules (keep maturity)

1. Residual grain **owns** \(\sigma\sim 10^{-5}\)–\(10^{-4}\) and \(\ell_*\sim R_{\mathrm{nl}}\).  
2. \(H_0\sim 8\%\) is **outsourced** to early physics / ladder / large-scale mean effects (I1).  
3. No imaginary work, no free \(10^{56}\), no post-hoc \(\ell_*\).  
4. Every new formula must state: **derived / OOM / postulate**.

---

## 6. Immediate next actions (executable)

| # | Action | Command / file |
|:--|:-------|:---------------|
| 1 | This frontier note | `FRONTIER_INQUIRY.md` (here) |
| 2 | Line B numbers | `scripts/r1/r1_stage4_test_design.py` |
| 3 | Line A start | extend M1 with residual variance OOM note |
| 4 | Keep H0 closed | `papers/closed_walls/` — do not reopen |

---

## 7. One-sentence programme identity

> We have **bounded** mesoscopic vacuum residual and **derived** its scale under local coupling to nonlinear matter; the research frontier is **\(g\) from averaging/SDiff**, **Stage-IV residual×structure tests**, and only later an information metric on the past light cone — **not** the 8% \(H_0\) gap.

---

*End of frontier inquiry note.*
