# WP4 — Joint predictions and structural zeros

**Author:** Jesús Morales Souhail · ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818) 
**Programme:** measurable-stochastic-vacuum 
**Status:** Synthesis of verified maps only 
**Date:** July 2026 
**Documented results:** [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md) · `pytest -q` 

---

## 1. Purpose

Combine R1 (seed), R3 (soft gain), and R2 (slip + path) into a **single prediction table** and an explicit list of **structural zeros**. 
No new free parameters. No DESI dial.

---

## 2. Master map (verified chain)


$$
\sigma_{0,\mathrm{eff}} = \left(\frac{\ell_*}{L}\right)^{d/2} \quad\xrightarrow{ G_O=e^{2r} } \sigma_{\mathrm{res}} = G_U G_F G_O \sigma_{0,\mathrm{eff}} \quad\xrightarrow{ \pi_T=\varepsilon\sigma_{\mathrm{res}}\rho_X } |\gamma-1|_{\mathrm{loc}} = 2\varepsilon\sigma_{\mathrm{res}}\frac{\rho_X}{\rho_m|\delta_m|} \quad\xrightarrow{ \mathrm{iid path} } \mathrm{RMS}_{\mathrm{path}} = |\gamma-1|_{\mathrm{loc}}\sqrt{\frac{\chi}{\ell_*}}.
$$


**Defaults used for soft regime (stated, not fitted):** 
$G_U=1$, $G_F=1$, $r\le 1.5$ $\Rightarrow$ $G_O\le e^{3}\approx 20$, $\varepsilon\le 1$, $\delta_m\sim 1$, $L=L_H=c/H_0$.

---

## 3. Joint numerical table (fiducial $H_0=67.4$, $\Omega_m=0.315$, $\Omega_\Lambda=0.685$, $z_s=1.5$)

| Scenario | $\sigma_{0,\mathrm{eff}}$ | $G_O$ | $\sigma_{\mathrm{res}}$ | $\|\gamma-1\|_{\mathrm{loc}}$ ($z\sim 0.8$) | $\ell_*$ | $\sqrt{N}$ | $\mathrm{RMS}_{\mathrm{path}}$ | Status |
|:---------|:--------------------------|:------|:------------------------|:-------------------------------------------|:---------|:-----------|:-------------------------------|:-------|
| Sorkin holographic | $\sim 1.2\times 10^{-61}$ | 1 | $\sim 10^{-61}$ | $\sim 10^{-61}$ | $L_P$ | — | $\ll 10^{-50}$ | **Structural null** |
| Sorkin + soft open | $\sim 10^{-61}$ | 20 | $\sim 10^{-60}$ | $\sim 10^{-60}$ | 1 Mpc | $\sim 67$ | $\sim 10^{-59}$ | **Structural null** |
| Mesoscopic count $d=2$, $\sigma=10^{-5}$ | $10^{-5}$ | 1 | $10^{-5}$ | $\sim 7\times 10^{-6}$ | $\sim 0.04$ Mpc | $\sim 335$ | $\sim 2\times 10^{-3}$ | Measurable *if* $\ell_*$ derived |
| Mesoscopic $d=3$, $\sigma=10^{-5}$ | $10^{-5}$ | 1 | $10^{-5}$ | $\sim 7\times 10^{-6}$ | $\sim 2.1$ Mpc | $\sim 46$ | $\sim 3\times 10^{-4}$ | Same |
| Mesoscopic + soft open | $10^{-5}$ | 20 | $\sim 2\times 10^{-4}$ | $\sim 1.5\times 10^{-4}$ | $\sim 2$ Mpc | $\sim 46$ | $\sim 10^{-3}$ | Near DESI residual ceiling (a posteriori) |
| DESI residual ceiling (external bound) | — | — | $<1.5\times 10^{-4}$ | $\lesssim 10^{-4}$ | model-dep. | $\mathcal{O}(10$–$10^{2})$ | $\lesssim$ few $\times 10^{-3}$ | Sister-repo limit, not a detection |

**A posteriori scales (not inputs):** 
DESI OU bound $\sigma_X<1.5\times 10^{-4}$ (95% CL); Maus $|\gamma-1|\sim 0.17$; Sakr-like floor $\sim 0.05$; schematic shear $\sim 10^{-3}$.

---

## 4. Channel matrix (what to measure where)

| Channel | Operator | Sensitive to | Blind to |
|:--------|:---------|:-------------|:---------|
| BAO residual kernel (OU/QNM) | Path residual on distances | Isotropic $\sigma_{\mathrm{res}}$ | Pure $\pi_T$ with $\varepsilon\to 0$ |
| Gravitational slip $\gamma=\Phi/\Psi$ | RSD + lensing | $\pi_T$ / $\varepsilon\sigma$ | Pure isotropic residual with $\varepsilon=0$ |
| Weak lensing shear / convergence | Line-of-sight Weyl potential | Path-integrated wrinkles | Local lab EM diffraction |
| Global $H(z)$ only | Background expansion | Mean DE density | Stochastic shear at fixed mean |

**Design rule:** a complete model predicts **both** residual and slip from the same $(\sigma_{\mathrm{res}},\varepsilon)$, or states which is zero and why.

---

## 5. Structural zeros (must remain null)

| # | Setting | Why null is structural |
|:--|:--------|:------------------------|
| Z1 | $\ell_*=L_P$ (any soft $G_O$) | Seed $\le 10^{-61}$; path $\sqrt{N}$ cannot recover |
| Z2 | Soft open only, Sorkin seed | $G_O=\mathcal{O}(10)\ll 10^{56}$ |
| Z3 | Freeze-out only | $G_F=1$ (preserves seed) |
| Z4 | Wrong operator (pupil, tesseract, SLM) | Scale/operator mismatch (exploratory sister repo) |
| Z5 | $\ell_*=L_H$ | $\sigma\sim 1$, destroys BAO smoothness (upper structural bound) |
| Z6 | Claiming $e^{60}$ late-time stretch as Sorkin amplifier | Wrong regime (inflation $\neq$ late $\Delta x=\mathcal{O}(1)$) |

If a model in this programme cannot list Z1–Z4, it is rejected (self-shielding axiom A6).

---

## 6. What would count as a *positive* prediction

A publishable positive claim requires **all** of:

1. A principle fixing $\ell_*$ or $N_{\mathrm{eff}}$ **before** using DESI numbers. 
2. A stated $\varepsilon$ (or derivation). 
3. Numbers for $\sigma_{\mathrm{res}}$ and $\mathrm{RMS}_{\mathrm{path}}$ from the master map. 
4. Explicit zeros Z1–Z4 still satisfied. 
5. A posteriori consistency with sister DESI bound (or tension declared).

Until (1) is done, the only publishable positives are the **theorems of absence** in §5 and the **conditional** landscape in §3.

---

## 7. Summary sentence

> Jointly, the verified maps imply: isotropic residual and light-path slip are two faces of the same amplitude; soft open dynamics and geometric $\sqrt{N}$ are at most decades, not $10^{56}$; Sorkin counting remains a structural null; mesoscopic counting is the only soft-regime door to observability, and it is not yet derived from a principle.

---

*End of WP4.*
