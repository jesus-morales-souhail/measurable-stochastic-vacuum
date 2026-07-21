# Minimal theoretical package: when could stochastic vacuum noise be measurable?

**Author:** Jesús Morales Souhail 
**ORCID:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818) 
**Status:** Programme manifesto (theoretical programme note) 
**Date:** July 2026 
**Verified claims only:** [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md) 
**Sister empirical corpus:** [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou)

---

## 0. Why parameter fitting is not enough

The sister DESI corpus has already established, under stated pipelines:

| Result | Implication |
|:-------|:------------|
| $\sigma_X < 1.5\times 10^{-4}$ (95% CL, OU kernel) | Bound on **effective** residual amplitude |
| Coherent tachyonic growth excluded | One hard amplifier class is dead |
| Soft amplifiers fail by many decades | No free amplification from $\sigma_0\sim 10^{-61}$ to $10^{-5}$ |
| Slip with BAO-scale $\sigma$ is amplitude-starved | Right operator, insufficient amplitude |

Therefore a measurable stochastic dark-energy sector is not “one more $\sigma$ in $\Lambda$CDM”. 
It requires a **minimal package of rule changes**, coupled, with **self-shielding** (predicted zeros).

---

## 1. Scale-fixing rule

A construction is **ad hoc** if it inserts a factor $\sim 10^{56}$ (or free $N_{\mathrm{eff}}$, $r$, $\varepsilon$) **without a principle that fixes the scale**.

Admissible work must:

1. Derive or define the seed $\sigma_{0,\mathrm{eff}}$ from a counting principle. 
2. Derive or bound the gain $G$ of any open map. 
3. State the observable operator (BAO residual vs slip vs both). 
4. Predict structural zeros (wrong scale / wrong operator / Sorkin soft). 
5. Use DESI only **a posteriori**.

---

## 2. Three coupled rules (not a menu)

| Rule | Idealization weakened | Content | Verified status |
|:-----|:----------------------|:--------|:----------------|
| **R1** | Continuum / global holographic count for the DE sector | Cell $\ell_*$, $N_{\mathrm{eff}}=(L/\ell_*)^d$, $\sigma_{0,\mathrm{eff}}=(\ell_*/L)^{d/2}$ | Kinematics verified; principle for $\ell_*$ **open** ([`r1-open-kernel.md`](r1-open-kernel.md)) |
| **R2** | Strong equivalence (universal light/mass potentials) | $\pi_T\Rightarrow\gamma=\Phi/\Psi\neq 1$; light-path accumulation | Local slip + $\sqrt{N}$ path verified; $\varepsilon$ **open** |
| **R3** | Unitary closed patch only | Soft open gain $G_O=e^{2r}$ | Soft bound verified; hard bath **open** |

**Hard rule:** treating R1, R2, R3 as independent free knobs is out of scope.

```
R1: what is counted? → seed
R3: how does it evolve? → residual amplitude
R2: what is observed? → H(z) residual and/or light/slip
 ↓
a posteriori tests (DESI / Euclid / RSD+lensing)
```

---

## 3. Self-shielding

“Measurable without being shielded” does **not** mean signal everywhere. 
It means shielding becomes a **theorem of the model**:

- Sorkin cell + soft dynamics → null (verified). 
- Wrong operator (lab optics) → null. 
- Possible non-null only if mesoscopic counting or a **derived** hard open map exists.

See [`SELF_SHIELDING_AXIOMS.md`](SELF_SHIELDING_AXIOMS.md) and [`wp5-falsification.md`](wp5-falsification.md).

---

## 4. Light without changing global expansion

A classical residual need not shift mean $H(z)$. 
Anisotropic stress $\pi_T$ wrinkles $\Phi,\Psi$; photons accumulate lensing/ISW-like shifts over Gpc paths.

**Verified:** geometric path gain is $\sqrt{N_{\mathrm{pat}}}=\mathcal{O}(10$–$10^{2})$ for Mpc cells — **not** $10^{56}$. 
**Analogy limit:** galaxies grew from post-inflation $\zeta\sim 10^{-5}$, not from late Sorkin $10^{-61}$.

---

## 5. Division of repositories

| Repository | Role |
|:-----------|:-----|
| [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou) | Empirical claim set (nulls, bounds) |
| **this repo** | Theory package + verified kinematics |
| [stochastic-de-exploratory-notes](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes) | Wrong-scale pedagogy only |

---

## 6. Closing sentence

> For Sorkin-type vacuum noise to be telescope-measurable under soft dynamics, the continuum global count, universal equivalence, and closed-patch unitarity cannot all remain untouched — but neither may any one of them be broken by a free $10^{56}$ dial. The package must derive seed, gain, and operator, and predict its own blinds.

---

*Manifesto only. Cite [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md) for documented results.*
