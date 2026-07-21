# Verified results: counting seeds, soft open gain, and light-path slip

**Author:** Jesús Morales Souhail  
**ORCID:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Date:** July 2026  
**Status:** Publication-oriented technical note — **only claims that are algebraically or numerically verified in-repo**  
**Code:** `scripts/lib_verified.py` · **Tests:** `tests/test_verified.py` (`pytest -q` must pass)  
**Sister empirical corpus:** [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou)

---

## Abstract

We record three families of **verified** relations relevant to whether late-time stochastic dark-energy noise can be telescope-measurable:

1. **Counting seeds (R1 kinematics):** under the hypothesis $N_{\mathrm{eff}}=(L/\ell_*)^d$, one has $\sigma_{0,\mathrm{eff}}=(\ell_*/L)^{d/2}$ exactly. The holographic Sorkin case $(d=2,\ell_*=L_P)$ gives $\sigma_0=L_P/L_H\sim 10^{-61}$. Inverting for a target $\sigma=10^{-5}$ forces $\ell_*$ at the **$0.04$–$14\,\mathrm{Mpc}$** scale depending on $d\in\{2,3,4\}$.

2. **Soft open gain (R3 kinematics):** a squeeze factor $e^{2r}$ with $r=\mathcal{O}(1)$ yields $G_O=\mathcal{O}(10)$. Lifting Sorkin $\sigma_0$ to $10^{-5}$ would require $r\sim 64$, i.e. a **new scale**, not a soft open map.

3. **Anisotropic stress and light paths (R2):** under the standard sub-horizon anisotropy equation, $|\gamma-1|=2\varepsilon\sigma(\rho_X/\rho_m)/|\delta_m|$. Incoherent line-of-sight accumulation multiplies by $\sqrt{N_{\mathrm{pat}}}$ with $N_{\mathrm{pat}}=\chi/\ell_*$. For Gpc paths and Mpc cells, $\sqrt{N}=\mathcal{O}(10$–$10^{2})$. Path accumulation **does not** promote Sorkin seeds to observational slip floors; mesoscopic seeds from (1) can reach $\mathrm{RMS}\sim 10^{-4}$–$10^{-3}$.

**We do not claim** a derivation of why $\ell_*$ is galactic, a microphysical horizon bath with $r\sim 64$, or a DESI detection. Those remain open. Empirical DESI residual bounds live in the sister repository and are used here only as **a posteriori** scales.

---

## 1. Scope and method of verification

| Included | Excluded |
|:---------|:---------|
| Algebraic identities | Fits to DESI choosing $\ell_*$ |
| Standard GR sub-horizon relations (stated) | Homemade Boltzmann hierarchies |
| Monte Carlo checks of $\mathrm{RMS}=s\sqrt{N}$ | Optical / lab metaphors as cosmology |
| Order-of-magnitude cosmology ($H_0$, $\Omega_m$, $\Omega_\Lambda$ fiducial) | Peer-reviewed status |

Automated tests: `pytest -q` from the repository root.  
Library: `scripts/lib_verified.py`.

---

## 2. Counting seed (R1) — verified identities

### 2.1 Definitions

Assume the DE residual sector admits a counting of effective degrees of freedom in a region of size $L$ with cell $\ell_*>0$ and dimension $d>0$:

$$
N_{\mathrm{eff}} = \left(\frac{L}{\ell_*}\right)^{d},
\qquad
\sigma_{0,\mathrm{eff}} = \frac{1}{\sqrt{N_{\mathrm{eff}}}} = \left(\frac{\ell_*}{L}\right)^{d/2}.
$$

**Status:** exact given the counting hypothesis (not a theorem of GR).

### 2.2 Inversion

$$
\ell_* = L\,\sigma_{0,\mathrm{eff}}^{2/d}.
$$

**Status:** exact inverse of §2.1 (tested for $d\in\{2,3,4\}$ and several $\sigma$).

### 2.3 Holographic Sorkin seed

Take $d=2$, $\ell_*=L_P$, $L=L_H=c/H_0$:

$$
N_{\mathrm{BH}} = \left(\frac{L_H}{L_P}\right)^{2},
\qquad
\sigma_0 = \frac{L_P}{L_H} \sim 1.2\times 10^{-61}
\quad (H_0=67.4\,\mathrm{km\,s^{-1}\,Mpc^{-1}}).
$$

**Status:** identity under that count. Matches the “Sorkin/Bekenstein” seed used as UV motivation in the sister corpus.

### 2.4 Landscape for a target $\sigma=10^{-5}$

With $L=L_H$ and $\sigma_{0,\mathrm{eff}}=10^{-5}$:

| $d$ | $\ell_*$ (exact inverse) | Character |
|:----|:-------------------------|:----------|
| 2 | $L_H\times 10^{-5}\approx 0.044\,\mathrm{Mpc}$ | mesoscopic |
| 3 | $\approx 2.1\,\mathrm{Mpc}$ | mesoscopic |
| 4 | $\approx 14\,\mathrm{Mpc}$ | mesoscopic |

**Verified reading:** *if* the residual is to sit near $10^{-5}$ by counting alone, the counting cell cannot be Planckian.  
**Not verified:** a dynamical principle that forces $\ell_*$ into that band.

### 2.5 Structural zero

For $\ell_*=L_P$ and $d\in\{2,3,4\}$, $\sigma_{0,\mathrm{eff}}\le\mathcal{O}(10^{-61})\ll 10^{-5}$.  
Any experiment whose sensitivity is $\gtrsim 10^{-5}$ **must** return a null for this seed **if** the residual tracks $\sigma_{0,\mathrm{eff}}$ without a huge derived gain. That null is a **theorem of the counting hypothesis**, not a failure of the survey.

---

## 3. Soft open gain (R3) — verified kinematics

### 3.1 Squeeze factor

For a single-mode squeeze parameter $r\ge 0$,

$$
G_O = e^{2r}.
$$

At $r=1.5$, $G_O = e^{3}\approx 20.086$ (exact).

**Status:** identity of the squeeze map.  
**Not verified:** that cosmology realises a given $r$.

### 3.2 Soft residual map (definition used in programme)

$$
\sigma_{\mathrm{res}} = G_U\, G_F\, G_O\, \sigma_{0,\mathrm{eff}},
$$

with defaults $G_F=1$ (freeze-out preserves amplitude; consistent with sister-repo OU freeze scans) and $G_U=1$ (late-time $\Delta x=\mathcal{O}(1)$ stretch is not $e^{60}$).

### 3.3 No soft rescue of Sorkin

For $\sigma_0\sim 10^{-61}$ and any $r\le 10$, $\sigma_{\mathrm{res}}\ll 10^{-50}$.  
To reach $10^{-5}$ from Sorkin via $G_O$ alone:

$$
r = \frac12\ln\!\left(\frac{10^{-5}}{\sigma_0}\right) \approx 64.4.
$$

**Verified:** the number $r\sim 64$.  
**Not verified / not claimed:** a horizon-bath derivation of $r\sim 64$ (would be a new scale claim).

---

## 4. Anisotropic stress, slip, and light paths (R2) — verified under stated GR assumptions

### 4.1 Local slip

In Newtonian gauge, sub-horizon, with

$$
k^{2}\Psi = -4\pi G a^{2}\rho_m\delta_m,
\qquad
k^{2}(\Phi-\Psi)=8\pi G a^{2}\pi_T,
\qquad
\pi_T = \varepsilon\,\sigma\,\rho_X,
$$

one obtains

$$
|\gamma-1| = \left|\frac{\Phi}{\Psi}-1\right| = 2\varepsilon\sigma\frac{\rho_X}{\rho_m|\delta_m|}.
$$

**Status:** standard consequence of the anisotropy equation under the listed assumptions (Ma & Bertschinger form; same as sister `slip_bridge.py`).  
**Not verified:** value of $\varepsilon$ from first principles; full $k,z$-dependent Boltzmann solution.

### 4.2 Path accumulation (probability)

If a line of sight crosses $N_{\mathrm{pat}}=\chi/\ell_*$ independent patches and each contributes an iid zero-mean wrinkle of RMS $s$, then

$$
\mathrm{RMS}_{\mathrm{path}} = s\sqrt{N_{\mathrm{pat}}}.
$$

**Status:** exact for the iid model (Monte Carlo checked to $\sim 3\%$).  
**Not verified:** Gaussianity or independence of real DE stress along the LOS.

### 4.3 Numerical anchors ($z_s=1.5$, fiducial cosmology)

Comoving distance $\chi(1.5)\approx 4.5\times 10^{3}\,\mathrm{Mpc}$ (trapezoidal integral of $c/H(z)$; convergence tested).

| Seed | Local $\|\gamma-1\|$ ($\varepsilon=\delta_m=1$, $z\sim 0.8$) | $\sqrt{N}$ (example $\ell_*$) | Path RMS |
|:-----|:--------------------------------------------------------------|:------------------------------|:---------|
| Sorkin | $\sim 10^{-61}$ | $\sim 67$ ($\ell_*=1\,\mathrm{Mpc}$) | $\sim 10^{-60}$ |
| $\sigma=10^{-5}$, $\ell_*=2.1\,\mathrm{Mpc}$ | $\sim 7\times 10^{-6}$ | $\sim 46$ | $\sim 3\times 10^{-4}$ |
| $\sigma=1.5\times 10^{-4}$ (DESI residual *ceiling*, a posteriori) | $\sim 10^{-4}$ | $\sim 21$ ($\ell_*=10\,\mathrm{Mpc}$) | $\sim 2\times 10^{-3}$ |

To lift Sorkin local slip to a floor $|\gamma-1|\sim 0.05$ by $\sqrt{N}$ alone requires $\sqrt{N}\sim 10^{59}$ ($N\sim 10^{119}$), versus $\sqrt{N}\sim 67$ available for $\ell_*=1\,\mathrm{Mpc}$.

**Verified reading:** geometric “universe as telescope” along the path is $\sqrt{N}=\mathcal{O}(10$–$10^{2})$ for Mpc cells — useful, **not** a $10^{56}$ amplifier.  
**Not verified:** that DESI/Euclid *will* detect slip from DE noise; only that the OOM can approach $10^{-3}$ if $\sigma\sim 10^{-5}$–$10^{-4}$.

### 4.4 Physical interpretation (tight)

- Correct: noise need not change global $H(z)$; $\pi_T$ wrinkles $\Phi,\Psi$; light integrates.  
- Correct analogy limit: primordial structure used $\zeta\sim 10^{-5}$ after inflation, not late Sorkin $10^{-61}$.  
- Incorrect: “photons travel for Gyr $\Rightarrow$ $10^{-61}$ becomes $10^{-5}$.”

---

## 5. Narrow path (soft regime) — architecture only

If Sorkin rescues are discarded, the only coherent soft-regime architecture is:

$$
\ell_*\sim\mathrm{Mpc}
\;\Rightarrow\;
\sigma_{0,\mathrm{eff}}\sim 10^{-6}\text{–}10^{-5}
\;\xrightarrow{G_O=e^{2r},\;r=\mathcal{O}(1)}\;
\sigma_{\mathrm{res}}\le 1.5\times 10^{-4}
\;\xrightarrow{\pi_T}\;
\mathrm{RMS}_{\mathrm{path}}(|\gamma-1|)\sim 10^{-4}\text{–}10^{-3}.
$$

| Label | Definition | Residual vs DESI ceiling | Path RMS (OOM, $d=3$, $\varepsilon=1$) |
|:------|:-----------|:-------------------------|:----------------------------------------|
| **NP-A** | $\sigma_0=10^{-5}$, $G_O=1$ | OK ($10^{-5}$) | $\sim 3.5\times 10^{-4}$ |
| **NP-B** | $\sigma_0\lesssim 7.5\times 10^{-6}$, $r=1.5$ | OK (on/under ceiling) | $\sim$ few $\times 10^{-3}$ |
| NP-user ($\sigma_0=10^{-5}$, $r=1.5$) | same shape | **Tension** ($\sigma_{\mathrm{res}}\approx 2.0\times 10^{-4}$) | $\sim 7\times 10^{-3}$ |

**Verified:** algebra and numbers for NP-A/B; naive product $\sigma_0\times G_O\times\sqrt{N}\neq\mathrm{RMS}$.  
**Not verified:** a principle that realises mesoscopic $\ell_*$, or a bath that realises $r=\mathcal{O}(1)$.  
Full write-up: [`NARROW_PATH.md`](NARROW_PATH.md).

---

## 6. Combined no-free-lunch statement (verified)

Define the soft residual after open kinematics and before/with path geometry as appropriate. Then:

$$
\sigma_{\mathrm{res}}^{\mathrm{(soft)}} = e^{2r}\sigma_{0,\mathrm{eff}}
\quad (r=\mathcal{O}(1)),
\qquad
\mathrm{RMS}_{\gamma}^{\mathrm{(path)}} \sim |\gamma-1|(\sigma_{\mathrm{res}})\,\sqrt{\chi/\ell_*}.
$$

**Theorem (soft regime, in-repo):**  
If $\sigma_{0,\mathrm{eff}}$ is the holographic Sorkin seed and $r=\mathcal{O}(1)$, then both residual BAO-scale amplitudes and path-integrated slip remain many tens of orders of magnitude below $10^{-5}$ and below $|\gamma-1|\sim 0.05$.  
**Measurability in this framework requires either** (i) a counting cell $\ell_*$ that makes $\sigma_{0,\mathrm{eff}}$ already mesoscopic (R1 principle still open), **or** (ii) a *derived* hard open map with $r\sim 60$ (not constructed).

---

## 7. Relation to DESI empirical claims (sister repo)

| Sister claim (DESI corpus) | Role here |
|:---------------------------|:----------|
| $\sigma_X < 1.5\times 10^{-4}$ (95% CL, OU kernel) | A posteriori scale only |
| Tachyonic rank-1 exclusion | Forbids one hard amplifier class |
| Freeze-out gain $\approx 1$ (Route 2 scans) | Supports $G_F=1$ default |
| Soft desqueezing $\mathcal{O}(10)$ | Supports $G_O$ ceiling used above |

This note **does not re-derive** the DESI likelihood. It consumes those results as external bounds.

---

## 7. Explicit non-claims (do not cite as results)

1. A first-principles derivation of galactic $\ell_*$ for DE (R1a/b/c open).  
2. A horizon Lindblad model that yields $r\sim 64$.  
3. A value of $\varepsilon$ fixed by SDiff symmetry.  
4. A detection of stochastic DE or of slip from vacuum noise.  
5. Peer review.

---

## 8. Reproducibility

```bash
git clone https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum.git
cd measurable-stochastic-vacuum
pip install numpy pytest
pytest -q
python scripts/lib_verified.py   # optional smoke (if __main__ added)
python scripts/r1_counting_landscape.py
python scripts/r3_open_horizon_map.py
python scripts/r2_light_path_accumulation.py
```

---

## 9. Suggested citation of *this* note

> Morales Souhail, J. (2026). *Verified results: counting seeds, soft open gain, and light-path slip.*  
> GitHub: `measurable-stochastic-vacuum`, `papers/VERIFIED_RESULTS.md`.  
> Claims restricted to identities and tests in `tests/test_verified.py`.

---

## References (minimal)

1. Ma, C.-P. & Bertschinger, E. (1995), Astrophys. J. Suppl., arXiv:astro-ph/9506072 — perturbation equations.  
2. Sister repo: Morales Souhail, *stochastic-dark-energy-ou* — DESI residual bounds and amplifier audit.  
3. Maus et al., arXiv:2505.20656 — published slip $\gamma=\Phi/\Psi$ (used only as floor scale).  
4. Sakr et al., arXiv:2501.07477 — indicative $\eta$ forecast floors.

---

*End of verified-results note. Programme narrative remains in `THEORY_REVOLUTION.md`; only this file is the citation spine for hard claims.*
