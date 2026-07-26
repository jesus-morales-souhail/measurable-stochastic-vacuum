# Blind R1 candidate: DE residual cell = matter nonlinear scale \(R_{\mathrm{nl}}\)

**Author:** Jesús Morales Souhail  
**Date:** July 2026  
**Status:** Hypothesis class with **a priori** length prediction — **not** a completed microphysical derivation  
**Code:** [`scripts/r1_principle_Rnl.py`](../scripts/r1_principle_Rnl.py)  
**Steering:** [`r1-scale-decade-8-12.md`](r1-scale-decade-8-12.md) · [`r1-open-kernel.md`](r1-open-kernel.md)

---

## Abstract

We state a **blind** candidate principle for the open R1 kernel (written so the length is fixed by **matter** physics, not by DESI residual targets):

> **(P\(_\mathrm{nl}\))** The effective counting / correlation cell \(\ell_*\) of the stochastic DE residual sector is the scale at which **matter** density fluctuations become order unity,
> \[
> \sigma(R_{\mathrm{nl}})=1,
> \]
> because that is the scale where collapsed structure can source decoherence, residual grain, or projection for a vacuum sector coupled to matter.

Using only standard cosmological inputs (\(\sigma_8\), local spectral index \(n_{\mathrm{eff}}\), \(H_0\)) — **not** \(\sigma_X\), not \(r_0\), not a DESI fit — one obtains
\[
R_{\mathrm{nl}}\sim 5\text{–}6.5\,h^{-1}\mathrm{Mpc}
\approx 8\text{–}10\,\mathrm{Mpc}
\quad(h=0.674,\ \sigma_8\simeq 0.81).
\]
**A posteriori:** this lands in the same 8–12 Mpc decade as \(R_8\), \(r_0(L_*)\), and the DESI-ceiling \(d=3\) counting cell.  
**Not claimed:** a Lagrangian derivation of vacuum–matter decoherence; that \(\ell_*=R_{\mathrm{nl}}\) is proven; that \(H_0\) tension is solved.

---

## 1. Principle (stated before the a posteriori table)

### 1.1 Physical content

1. Matter clustering becomes **nonlinear** on a characteristic comoving scale \(R_{\mathrm{nl}}\) defined by the variance of the linear density field in a top-hat (or equivalent) filter: \(\sigma(R_{\mathrm{nl}})=1\).  
2. That scale is fixed by the **observed** \(\sigma_8\) (amplitude at \(8\,h^{-1}\mathrm{Mpc}\)) and the shape of \(P(k)\) near that pivot — both are **matter / growth** data, not DE residual likelihoods.  
3. **Hypothesis:** the DE residual sector does not count Planck cells; it inherits a grain set by the **matter nonlinear patch**, because residual isotropy / SDiff leakage / decoherence is tied to collapsed structure (edge / grain language of the programme).

This is a **principle class**, not a free dial: once \(\sigma_8\) and \(P(k)\) are fixed, \(R_{\mathrm{nl}}\) is fixed.

### 1.2 What is *not* input

| Forbidden as input to the prediction | Why |
|:-------------------------------------|:----|
| DESI \(\sigma_X\) ceiling | A posteriori only |
| Target \(\ell_*=12.56\,\mathrm{Mpc}\) | That is the comparison target |
| Hand-tuned \(\theta\) or \(r\) | Amplifier walls |
| NP-A \(2.06\,\mathrm{Mpc}\) | Different \(\sigma\) row; not the lead |

---

## 2. A priori calculation

### 2.1 Local power-law map (standard OOM)

Near the \(8\,h^{-1}\mathrm{Mpc}\) pivot,
\[
\sigma(R)\approx\sigma_8\left(\frac{R_8}{R}\right)^{\alpha},\qquad
\alpha=\frac{n_{\mathrm{eff}}+3}{2},\qquad R_8\equiv 8\,h^{-1}\mathrm{Mpc}.
\]
Require \(\sigma(R_{\mathrm{nl}})=1\):
\[
R_{\mathrm{nl}}=R_8\,\sigma_8^{1/\alpha}.
\]

**Inputs (matter sector, Planck-class OOM):**

| Quantity | Value | Role |
|:---------|:------|:-----|
| \(\sigma_8\) | \(0.81\) | amplitude of matter fluctuations |
| \(n_{\mathrm{eff}}\) | \(-2.0\) to \(-1.0\) (local slope OOM) | shape near nonlinear pivot |
| \(h\) | \(0.674\) (\(H_0=67.4\)) | unit conversion only |

### 2.2 Predicted band (code)

| \(n_{\mathrm{eff}}\) | \(\alpha\) | \(R_{\mathrm{nl}}\) [\(h^{-1}\) Mpc] | \(R_{\mathrm{nl}}\) [Mpc] |
|:---------------------|:-----------|:-------------------------------------|:------------------------|
| \(-2.0\) | \(0.50\) | \(5.25\) | \(7.79\) |
| \(-1.5\) | \(0.75\) | \(6.04\) | \(8.96\) |
| \(-1.0\) | \(1.00\) | \(6.48\) | \(9.61\) |

**Blind prediction:** \(\ell_*\sim R_{\mathrm{nl}}\sim \mathbf{8\text{–}10\,\mathrm{Mpc}}\) (central band).

```bash
python scripts/r1_principle_Rnl.py
```

---

## 3. A posteriori comparison (after the prediction)

| Quantity | Value [Mpc] | Relation to \(R_{\mathrm{nl}}\sim 8\)–\(10\) |
|:---------|:------------|:---------------------------------------------|
| \(R_{\mathrm{nl}}\) (this principle) | \(8\)–\(10\) | **prediction** |
| \(r_0(L_*)\) (Zehavi class) | \(7.4\)–\(8.9\) | same decade; clustering length, not identical object |
| \(R_8=8/h\) | \(11.87\) | pivot of \(\sigma_8\); adjacent |
| DESI-ceiling cell \(d=3\), \(\sigma=1.5\times 10^{-4}\) | \(12.56\) | counting inverse a posteriori |
| NP-A cell \(\sigma=10^{-5}\), \(d=3\) | \(2.06\) | **different** aspirational row — not the lead |

**Downstream residual if \(\ell_*=R_{\mathrm{nl}}\approx 9\,\mathrm{Mpc}\), \(d=3\):**
\[
\sigma_{0,\mathrm{eff}}=\Bigl(\frac{\ell_*}{L_H}\Bigr)^{3/2}
\approx\Bigl(\frac{9}{4448}\Bigr)^{3/2}
\sim 9\times 10^{-5},
\]
which sits **under** the sister DESI ceiling \(1.5\times 10^{-4}\) and in the residual decade — a **compatibility** check, not a fit.

---

## 4. Falsifiers and open microphysics

| If… | Then… |
|:----|:------|
| \(\sigma_8\) and \(P(k)\) imply \(R_{\mathrm{nl}}\ll 3\,\mathrm{Mpc}\) or \(\gg 30\,\mathrm{Mpc}\) under standard growth | Principle still well-defined but leaves the 8–12 decade coincidence |
| Microphysics forces DE grain = \(L_P\) | Soft null; telescope residual not from this channel |
| Derived \(\ell_*=R_{\mathrm{nl}}\) but BAO residual \(\gg 1.5\times 10^{-4}\) without damping | Tension with sister bound |
| Only way to hit data is to retune \(R_{\mathrm{nl}}\) after seeing DESI | **Illegal** — reject under BOUNDARY |

**Still missing for a full theory claim:** an explicit map from “matter nonlinear patch” to the OU residual operator / SDiff grain (decoherence calculation, not a slogan).

---

## 5. Relation to programme walls

This does **not** re-open soft amplification of Sorkin. It **changes the counting cell** so the seed is already mesoscopic — the only soft-regime door left open in the kernel notes.

Scope if successful: residual \(\sigma_X\) and path slip RMS \(10^{-4}\)–\(10^{-3}\).  
**Not** the \(\sim 9\%\) \(H_0\) tension (amplitude still short under DESI-safe residual).

---

## 6. Claim checklist

| ID | Claim | Status |
|:---|:------|:-------|
| P1 | Principle P\(_\mathrm{nl}\) stated without DESI \(\sigma_X\) as input | this note |
| P2 | \(R_{\mathrm{nl}}=R_8\sigma_8^{1/\alpha}\) band \(\sim 8\)–\(10\,\mathrm{Mpc}\) | arithmetic + script |
| P3 | A posteriori overlap with \(r_0\), \(R_8\), ceiling cell decade | comparison |
| P4 | \(\sigma(\ell_*=9\,\mathrm{Mpc},d=3)\sim 10^{-4}\) under ceiling | arithmetic |

| Non-claim | |
|:----------|:--|
| N-P1 | Microscopic derivation of vacuum decoherence at \(R_{\mathrm{nl}}\) |
| N-P2 | \(\ell_*=R_{\mathrm{nl}}\) proven |
| N-P3 | \(H_0\) tension explained |

---

## 7. One-sentence status

> A blind matter-only definition \(R_{\mathrm{nl}}\) with \(\sigma(R_{\mathrm{nl}})=1\) predicts \(\sim 8\)–\(10\,\mathrm{Mpc}\); that is the first principle-shaped candidate aimed at the 8–12 Mpc decade, still short of a full derivation, now open to the same audit as every prior attempt.

---

*End of R_nl principle candidate note.*
