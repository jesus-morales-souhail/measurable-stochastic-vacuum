# Finding the gap: spectator inflation seed vs residual band (modern \(r\))

**Author:** Jesús Morales Souhail  
**ORCID:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Date:** July 2026  
**Status:** Programme advance note — **OOM atlas + experimental door**, not a DESI detection  
**Builds on:** [`inflation-spectator-seed-gordon-wands.md`](inflation-spectator-seed-gordon-wands.md) · sister [`amplification-gap.md`](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou/blob/main/papers/amplification-gap.md)  
**Code:** [`scripts/inflation_spectator_residual_atlas.py`](../scripts/inflation_spectator_residual_atlas.py) · `pytest`  

---

## Abstract

Gordon & Wands replace the holographic seed \(\sigma_0\sim 10^{-61}\) by an inflationary spectator fluctuation \(\delta Q\sim H_{\mathrm{inf}}/(2\pi)\). The missing factor for *their* CMB-isocurvature target is \(\sim 45\), not \(10^{56}\).

This note answers the next question for **this** programme:

> Under **modern** tensor bounds on \(r\), what residual density contrast \(\sigma_\rho\sim\lvert\delta\rho_Q/\rho_Q\rvert\) can that seed reach, with or without \(\mathcal{O}(10^{1}\)–\(10^{2})\) post-inflation field growth, as a function of the DE slow-roll parameter \(\varepsilon_Q\)?

**Result (verified arithmetic):** at the BK-class edge \(r\sim 0.036\),
\[
\frac{\delta Q}{M_p}\sim 3\times 10^{-6}.
\]
A frozen, very flat DE potential (\(\varepsilon_Q\sim 10^{-4}\)) still sits **orders below** \(10^{-5}\).  
But **\(A\sim 45\)** (Gordon–Wands roll) **and** a mild \(\varepsilon_Q\sim 0.05\) land \(\sigma_\rho\) in the **\(10^{-5}\)–\(10^{-4}\)** decade — the same decade as the sister DESI ceiling and Euclid residual targets — **without any \(10^{56}\) dial**.

That is the **gap that experiments can close**: measure \(r\) (ceiling on \(\delta Q\)), constrain \(\varepsilon_Q\) / \(w_Q\) (slope), and test residuals \(\sigma_X\) a posteriori. It is **not** a claim that DESI has seen spectator DE, and **not** a fit of \(\varepsilon_Q\) or \(A\) to DESI.

---

## 1. Why this is the place to push

| Pathway | Open number | Status |
|:--------|:------------|:-------|
| Soft amplify Sorkin \(\sigma_0\) | \(G\sim 10^{56}\)–\(10^{57}\) | **Wall measured** (closed as free dial) |
| R1 mesoscopic cell | Principle for \(\ell_*\) | Open kernel (declared) |
| **Spectator during inflation** | \(H_{\mathrm{inf}}\) (via \(r\)), \(A\), \(\varepsilon_Q\), map to BAO kernel | **This note** |

The user pressure is correct: if there is a crack, it is here — **change the seed physics**, then ask which **experiment** kills or allows residual-band amplitudes.

---

## 2. Standard relations (used as definitions)

Scalar amplitude \(A_s\simeq 2.1\times 10^{-9}\) (Planck-class). Tensor-to-scalar ratio \(r\). In reduced Planck units,
\[
\frac{H_{\mathrm{inf}}}{M_p}=\pi\sqrt{\frac{r A_s}{2}},\qquad
\frac{\delta Q}{M_p}=\frac{H_{\mathrm{inf}}}{2\pi M_p}=\sqrt{\frac{r A_s}{8}}.
\]
Potential-dominated fractional density contrast (OOM, flat gauge):
\[
\sigma_\rho\equiv\left\lvert\frac{\delta\rho_Q}{\rho_Q}\right\rvert
\approx\sqrt{2\varepsilon_Q}\;A\;\frac{\delta Q_i}{M_p},
\qquad
\varepsilon_Q=\frac{M_p^2}{2}\left(\frac{V_Q'}{V_Q}\right)^2,
\]
with post-inflation field growth \(A=\delta Q_f/\delta Q_i\) (Gordon & Wands: \(A>45\) for *their* target).

**Modern \(r\) anchors (95% CL class, literature):**  
BICEP/Keck + Planck combinations often quote \(r\lesssim 0.036\); we also show \(r=0.056\) and a low-scale \(r=10^{-3}\).  
Refs.: BK15/BK18 + Planck analyses (e.g. \(r<0.036\) at 95% CL class); energy scale \(V_*^{1/4}\lesssim 1.4\times 10^{16}\,\mathrm{GeV}\) for \(r\sim 0.036\).

---

## 3. Atlas (machine output)

```bash
python scripts/inflation_spectator_residual_atlas.py
```

### 3.1 Field seed only (\(\delta Q/M_p\))

| \(r\) | \(H/M_p\) | \(\delta Q/M_p=H/(2\pi M_p)\) |
|:------|:----------|:------------------------------|
| \(0.001\) | \(\sim 3.2\times 10^{-6}\) | \(\sim 5.1\times 10^{-7}\) |
| \(0.01\) | \(\sim 1.0\times 10^{-5}\) | \(\sim 1.6\times 10^{-6}\) |
| \(0.036\) (BK-class edge) | \(\sim 1.9\times 10^{-5}\) | \(\sim 3.1\times 10^{-6}\) |
| \(0.056\) | \(\sim 2.4\times 10^{-5}\) | \(\sim 3.8\times 10^{-6}\) |

Already **fifty-five decades above** Sorkin \(\sigma_0\sim 10^{-61}\) — because the seed was never holographic counting.

### 3.2 Density contrast and residual band

At \(r=0.036\):

| \(A\) | \(\varepsilon_Q\) | \(\sigma_\rho\) (OOM) | vs \(10^{-5}\) | vs \(1.5\times 10^{-4}\) |
|:------|:------------------|:---------------------|:---------------|:------------------------|
| 1 (frozen) | \(10^{-4}\) (very flat) | \(\sim 4\times 10^{-8}\) | short \(\times\sim 250\) | short \(\times\sim 4000\) |
| 1 | \(0.05\) (mild) | \(\sim 1\times 10^{-6}\) | short \(\times\sim 10\) | short \(\times\sim 150\) |
| **45** (G&W) | \(10^{-4}\) | \(\sim 2\times 10^{-6}\) | short \(\times\sim 5\) | short \(\times\sim 80\) |
| **45** | **\(0.05\)** | \(\mathbf{\sim 4\times 10^{-5}}\) | **in decade** | under DESI ceiling |
| 45 | \(1\) (not DE-like today) | \(\sim 2\times 10^{-4}\) | above Euclid target | near/above DESI ceiling |

**Reading:**  
- Flat frozen spectator **alone** does **not** hit residual band at modern \(r\).  
- **\(A\sim 45\) + mild slope \(\varepsilon_Q\sim\mathrm{few}\times 10^{-2}\)** **can** sit in \(10^{-5}\)–\(10^{-4}\) **without** \(10^{56}\).  
- \(\varepsilon_Q\sim 1\) at late times is **in tension** with \(w_Q\approx -1\); mild \(\varepsilon_Q\) is the honest window to discuss, not \(\varepsilon_Q=1\).

### 3.3 Contrast with Sorkin

| Seed | Gap to \(10^{-5}\) | Gap to \(1.5\times 10^{-4}\) |
|:-----|:-------------------|:----------------------------|
| Sorkin \(\sigma_0\sim 10^{-61}\) | \(\sim 10^{56}\) | \(\sim 10^{57}\) |
| Spectator at \(r=0.036\), \(A=45\), \(\varepsilon_Q=0.05\) | \(\mathcal{O}(1)\) (in band) | under ceiling |

---

## 4. The experimental gap (what can actually decide)

This is the “brecha” that is **not** a free parameter:

| Measurement | What it does to the spectator door |
|:------------|:-----------------------------------|
| **Tighter upper bound on \(r\)** (CMB-S4, LiteBIRD, …) | Lowers max \(\delta Q\propto\sqrt{r}\). If \(r\ll 10^{-3}\), even \(A\sim 100\) + mild \(\varepsilon_Q\) falls below \(10^{-5}\). |
| **Detection of \(r>0\)** near current edge | Keeps \(\delta Q/M_p\sim\mathrm{few}\times 10^{-6}\) available. |
| **\(w_Q\) / \(\varepsilon_Q\)** from BAO+SN+CMB | Caps how large \(\sqrt{2\varepsilon_Q}\) can be while remaining DE-like. |
| **Sister \(\sigma_X\) bound** | A posteriori: if a derived \((r,A,\varepsilon_Q)\) predicts \(\sigma_\rho>\sigma_X^{\mathrm{DESI}}\), that corner dies. |
| **DE isocurvature / CMB** | Gordon–Wands original target; independent of BAO residual kernel. |

**Illegal (BOUNDARY):** choose \(A\) and \(\varepsilon_Q\) after looking at DESI to land in band.  
**Legal:** derive \(A\) from a potential (as G&W try), take \(r\) from tensors, take \(\varepsilon_Q\) from DE dynamics, **then** compare to \(\sigma_X\).

---

## 5. What is still missing (honest)

| Gap in the theory chain | Status |
|:------------------------|:-------|
| Map \(\sigma_\rho\to\) **BAO distance residual kernel** used in sister OU likelihood | **Not derived** — largest remaining theory step |
| Covariance of stochastic residual from inflationary spectator | **Not derived** |
| Modern update of G&W tensor arithmetic (2005 \(V^{1/4}\) numbers → current \(r\)) | **Done at OOM** in this atlas for \(\delta Q\); full G&W quadrupole re-fit not done |
| Proof that DE was light during inflation | Assumption |
| Equivalence of \(\sigma_\rho\) with sister \(\sigma_X\) | **Not claimed** — same *decade* only under that identification |

Until the BAO-kernel map exists, a residual-band hit in this atlas is a **necessary-scale** statement (“the seed is no longer 55 decades too small”), not a DESI likelihood claim.

---

## 6. Claim checklist

| ID | Claim | Evidence |
|:---|:------|:---------|
| IS1 | \(\delta Q/M_p=\sqrt{r A_s/8}\) | standard + script |
| IS2 | At \(r=0.036\), \(\delta Q/M_p\sim 3\times 10^{-6}\) | script / tests |
| IS3 | \(\sigma_\rho=\sqrt{2\varepsilon_Q}\,A\,(\delta Q/M_p)\) OOM | definition |
| IS4 | \(A=45\), \(\varepsilon_Q=0.05\), \(r=0.036\) → \(\sigma_\rho\sim\mathrm{few}\times 10^{-5}\) | script |
| IS5 | Sorkin gaps remain \(\sim 10^{56}\)–\(10^{57}\) | sister `gap_two_targets` |

| Non-claim | |
|:----------|:--|
| N-IS1 | Spectator DE **detected** by DESI |
| N-IS2 | \(\varepsilon_Q=0.05\), \(A=45\) **derived** for our residual |
| N-IS3 | \(\sigma_\rho\equiv\sigma_X\) without map |
| N-IS4 | G&W tachyonic roll = excluded BAO GPE |

---

## 7. One-sentence advance

> The crack is not another soft amplifier of Sorkin: under modern \(r\), an inflationary spectator plus \(\mathcal{O}(10^{1}\)–\(10^{2})\) derived field growth can sit in the residual decade **if** the DE slope is not vanishing — and **future \(r\) and \(w_Q\) measurements** can shut that window without ever needing a \(10^{56}\) miracle.

---

## 8. Reproduce

```bash
cd measurable-stochastic-vacuum
pytest -q
python scripts/gordon_wands_factor45.py
python scripts/inflation_spectator_residual_atlas.py
python scripts/gap_two_targets.py  # sister repo: Sorkin contrast
```

---

*End of spectator residual atlas.*
