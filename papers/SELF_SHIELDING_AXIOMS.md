# Self-shielding axioms

**Programme:** measurable-stochastic-vacuum 
**Author:** Jesús Morales Souhail · July 2026 

These axioms convert scale/operator hygiene into **admission rules** for this repository.

---

## A0 — Repository separation

| Claim type | Allowed repository |
|:-----------|:-------------------|
| DESI residual bound / model kill | `stochastic-dark-energy-ou` |
| Derived counting / open map / slip OOM | **this repo** |
| Lab wrong-scale pedagogy | `stochastic-de-exploratory-notes` |

---

## A1 — Correct scale or silence

A prediction is admissible only if the scale where the effect is $\mathcal{O}(1)$ follows from the same principle that defines the seed or coupling.

---

## A2 — Correct operator or silence

| Mechanism | Legitimate operator | Illegitimate operator |
|:----------|:--------------------|:----------------------|
| Isotropic DE residual | BAO residual kernel | Pupil Airy pattern |
| SDiff gap / shear | $\gamma=\Phi/\Psi$, $\mu,\Sigma$ | Single-bin “wiggle hunt” |
| Open system | Derived $G_O$ + residual | Hand $10^{56}$ factor |

---

## A3 — No undeclared amplification factors

Excluded: free $10^{56}$; $e^{2r}$ with $r\sim\mathcal{O}(1)$ claimed to fix Sorkin; double-counted $\sqrt{N}$; free $A_0$ renamed as microphysics.

---

## A4 — Coupled package R1–R2–R3

Every model states the status of seed, gain, and operator (derived / bounded / absent with reason).

---

## A5 — DESI is a test, not a dial

Sister bounds are used only a posteriori for compatibility, tension, or falsification. 
Excluded: choosing $\ell_*$ or $r$ to sit under $1.5\times 10^{-4}$.

---

## A6 — Predicted zeros

Every model includes a “where the signal must vanish” section (at least the structural zeros in WP4).

---

## A7 — Collapse / energy rhetoric

Any “avoids black holes” claim needs effective volume, probe energy density, and comparison to curvature scales **in that theory**. Otherwise delete the sentence.

---

## A8 — Language in abstracts

**Excluded:** “we prove the vacuum is discrete”; “Euclid will see Sorkin”; “tesseract solves dark energy”. 

**Allowed:** “under counting hypothesis …”; “soft open map implies …”; “compatible / in tension with sister DESI bound …”.

---

## Citation rule

Hard numerical/algebraic claims must appear in [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md) and remain green under `pytest -q`.
