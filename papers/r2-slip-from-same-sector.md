# WP3 — R2: anisotropic stress, potential wrinkles, and light paths

**Author:** Jesús Morales Souhail · ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Programme:** measurable-stochastic-vacuum  
**Status:** Operator + path OOM closed; $\varepsilon$ open  
**Date:** July 2026  
**Code:** [`scripts/r2_light_path_accumulation.py`](../scripts/r2_light_path_accumulation.py) · [`scripts/lib_verified.py`](../scripts/lib_verified.py)  

> **Hard claims:** cite only [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md) (gated by `pytest -q`).

---

## 1. Physical picture

A classical DE residual need not change global $H(z)$.  
It may source traceless anisotropic stress $\pi_T$, wrinkling $\Phi,\Psi$.  
Photons accumulate lensing / ISW-like shifts over Gpc paths.  
The telescope measures **integrated light distortion**, not vacuum noise directly.

This is the correct **operator** for the SDiff gap (shear not cancelled by $T_{\mu\nu}\propto g_{\mu\nu}$).

---

## 2. Local map (standard sub-horizon GR)

$$
\pi_T = \varepsilon\,\sigma\,\rho_X,
\qquad
|\gamma-1| = 2\varepsilon\sigma\frac{\rho_X}{\rho_m|\delta_m|}.
$$

Assumptions: Newtonian gauge, $k\gg aH$, $\mu=1$, phenomenological $\pi_T$ amplitude.

---

## 3. Path accumulation

$$
N_{\mathrm{pat}}=\frac{\chi}{\ell_*},
\qquad
\mathrm{RMS}_{\mathrm{path}} = |\gamma-1|_{\mathrm{loc}}\sqrt{N_{\mathrm{pat}}}
\quad\text{(iid zero-mean patches)}.
$$

For $z_s=1.5$, $\chi\sim 4.5\times 10^{3}\,\mathrm{Mpc}$, Mpc-scale cells give $\sqrt{N}=\mathcal{O}(10$–$10^{2})$.

**Not** $10^{56}$. Path geometry is a modest multiplier.

---

## 4. Verified numerical anchors

| Case | Path RMS (OOM) |
|:-----|:---------------|
| Sorkin | $\ll 10^{-50}$ — structural null |
| $\sigma=10^{-5}$, $\ell_*\sim 2\,\mathrm{Mpc}$ | $\sim 3\times 10^{-4}$ |
| DESI residual ceiling a posteriori | $\sim 10^{-3}$ order |

Galaxy formation is **not** an analogy for lifting $10^{-61}$: it used post-inflation $\zeta\sim 10^{-5}$.

---

## 5. Open

$\varepsilon$ fixed by residual SDiff symmetry (not free).  
Full Boltzmann (hi_class/MGCAMB) only after $\sigma$ and $\varepsilon$ are principle-fixed.

---

## 6. R2 status (A4)

| Piece | Status |
|:------|:-------|
| Local slip formula | **Closed** (under stated assumptions) |
| $\sqrt{N}$ path | **Closed** (+ MC) |
| Microscopic $\varepsilon$ | **Absent (declared)** |

---

*End of WP3 discussion note.*
