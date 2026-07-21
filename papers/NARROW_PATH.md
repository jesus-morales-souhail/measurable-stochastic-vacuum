# The narrow path: the only soft-regime architecture that is mathematically coherent

**Author:** Jesús Morales Souhail 
**ORCID:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818) 
**Date:** July 2026 
**Status:** Architecture note grounded in verified identities 
**Documented results / tests:** [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md) · `pytest -q` · [`scripts/lib_verified.py`](../scripts/lib_verified.py) 
**Sister empirical bound:** $\sigma_X < 1.5\times 10^{-4}$ (95% CL, OU kernel) in [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou)

---

## Abstract

If one discards “ad hoc” rescues of the Planck/Sorkin seed $\sigma_0\sim 10^{-61}$ (soft squeeze $r\sim 64$, or $N_{\mathrm{pat}}\sim 10^{119}$ along the line of sight), the only soft-regime architecture that remains mathematically coherent is a **triple concurrent structure**:

1. **R1 — mesoscopic counting cell** so that $\sigma_{0,\mathrm{eff}}\sim 10^{-5}$–$10^{-6}$ already at the seed; 
2. **R3 — modest open gain** $G_O=e^{2r}$ with $r=\mathcal{O}(1)$ (e.g. $r=1.5\Rightarrow G_O\approx 20$); 
3. **R2 — anisotropic stress + light-path accumulation** $\mathrm{RMS}=|\gamma-1|_{\mathrm{loc}}\sqrt{\chi/\ell_*}$, not a change of global $H(z)$.

This note writes the causal chain correctly (not as a naive product of three ad hoc factors), gives **machine-checked numbers**, and isolates the **DESI-safe window** where the isotropic residual stays under the sister bound while the light-path slip RMS sits near $10^{-3}$.

---

## 1. What is ruled out (already verified)

| Rescue of Sorkin $\sim 10^{-61}$ | Why impossible in the soft / observable regime |
|:--------------------------------|:-----------------------------------------------|
| Soft squeeze alone | Need $r\approx 64.4$ for $e^{2r}\sigma_0=10^{-5}$ |
| Path $\sqrt{N}$ alone | Need $\sqrt{N}\sim 10^{59}$ vs available $\sqrt{N}\sim\mathcal{O}(10$–$10^{2})$ |
| Soft open **and** path stacked | Still $\mathrm{RMS}\ll 10^{-50}$ |
| Late $\Delta x=\mathcal{O}(1)$ as “$e^{60}$” | Wrong regime (inflation $\neq$ late acceleration) |

**Conclusion:** the theory must **not** try to explain a Planck-counted seed into a telescope band by geometry or soft squeezing. It must **change the counting cell** (or invent a *derived* hard open map — not available).

---

## 2. The three concurrent conditions

### 2.1 R1 — Redefine the seed (mesoscopic cell)

**Identity (exact under the counting hypothesis):**


$$
N_{\mathrm{eff}} = \left(\frac{L_H}{\ell_*}\right)^{d}, \qquad \sigma_{0,\mathrm{eff}} = \frac{1}{\sqrt{N_{\mathrm{eff}}}} = \left(\frac{\ell_*}{L_H}\right)^{d/2}, \qquad \ell_* = L_H \sigma_{0,\mathrm{eff}}^{2/d}.
$$


**For $\sigma_{0,\mathrm{eff}}=10^{-5}$ and $L_H=c/H_0$ ($H_0=67.4$):**

| $d$ | $\ell_*$ |
|:----|:---------|
| 2 | $0.0445 \mathrm{Mpc}$ |
| 3 | $2.065 \mathrm{Mpc}$ (cluster / large-group scale) |
| 4 | $14.07 \mathrm{Mpc}$ |

**Physical reading:** DE correlation / counting grain is an **IR emergent scale**, not $L_P$. 
**Still open (not claimed):** which principle fixes $\ell_*$ (R1a/b/c).

---

### 2.2 R3 — Realistic kinematic amplification (soft open)

**Identity:** $G_O=e^{2r}$. For $r=1.5$, $G_O=e^{3}\approx 20.086$.


$$
\sigma_{\mathrm{res}} = G_U G_F G_O \sigma_{0,\mathrm{eff}} \quad\text{with soft defaults }G_U=G_F=1.
$$


| $\sigma_{0,\mathrm{eff}}$ | $r$ | $\sigma_{\mathrm{res}}$ |
|:--------------------------|:----|:------------------------|
| $10^{-5}$ | $0$ | $10^{-5}$ |
| $10^{-5}$ | $1.5$ | $2.009\times 10^{-4}$ |
| $7.47\times 10^{-6}$ | $1.5$ | $1.500\times 10^{-4}$ (DESI ceiling) |

**Reading:** soft open gain is a **factor $\sim 10$–$20$**, not $10^{56}$. 
It does not save Sorkin; it can push a mesoscopic seed toward the DESI residual ceiling.

---

### 2.3 R2 — Project on gravitational slip + short optical path

**Do not** force the signal into global $H(z)$ (BAO residual bound is already tight). 
Source anisotropic stress and read light:


$$
\pi_T = \varepsilon \sigma_{\mathrm{res}} \rho_X, \qquad |\gamma-1|_{\mathrm{loc}} = 2\varepsilon\sigma_{\mathrm{res}}\frac{\rho_X}{\rho_m|\delta_m|} \quad (k\gg aH, \mu=1).
$$


**Path accumulation (iid patches):**


$$
N_{\mathrm{pat}} = \frac{\chi(z_s)}{\ell_*}, \qquad \mathrm{RMS}_{\mathrm{path}} = |\gamma-1|_{\mathrm{loc}} \sqrt{N_{\mathrm{pat}}}.
$$


For $z_s=1.5$, $\chi\approx 4482 \mathrm{Mpc}$ (fiducial cosmology).

---

## 3. Correct causal chain (avoid the false product)

### 3.1 Valid chain

```
ell_* → sigma_0,eff (R1 counting)
 ↓
 G_O = e^{2r} (R3 soft open)
 ↓
 sigma_res
 ↓
 |γ-1|_loc ∝ sigma_res (R2 local slip)
 ↓
 RMS_path = |γ-1|_loc √(χ/ell_*)
```

### 3.2 Invalid shorthand


$$
\underbrace{10^{-5}}_{\text{seed}} \times \underbrace{20}_{G_O} \times \underbrace{46}_{\sqrt{N}} \not= \mathrm{RMS}_{\mathrm{path}}.
$$


That product double-counts structure: $\sqrt{N}$ multiplies the **slip per patch**, which is already $\propto\sigma_{\mathrm{res}}=G_O\sigma_0$, and the prefactor $2\varepsilon(\rho_X/\rho_m)/|\delta_m|$ is $\mathcal{O}(0.1$–$1)$, not $1$.

**Machine check ($d=3$, $\sigma_0=10^{-5}$, $r=1.5$, $\varepsilon=1$, $z=0.8$):**

| Quantity | Value |
|:---------|:------|
| $\ell_*$ | $2.065 \mathrm{Mpc}$ |
| $G_O$ | $20.086$ |
| $\sigma_{\mathrm{res}}$ | $2.009\times 10^{-4}$ |
| $\|\gamma-1\|_{\mathrm{loc}}$ | $1.498\times 10^{-4}$ |
| $N_{\mathrm{pat}}$ | $2171$ |
| $\sqrt{N}$ | $46.59$ |
| $\mathrm{RMS}_{\mathrm{path}}$ | $6.98\times 10^{-3}$ |
| Naive $10^{-5}\times 20\times 46.6$ | $9.36\times 10^{-3}$ (close OOM, **not identical**) |

---

## 4. DESI-safe window (critical for coherence with null residual)

The sister OU bound is $\sigma_X < 1.5\times 10^{-4}$ (95% CL) on the **isotropic residual** kernel.

If $\sigma_{\mathrm{res}}$ is identified with that residual amplitude:

| Choice | $\sigma_{\mathrm{res}}$ | vs DESI ceiling | $\mathrm{RMS}_{\mathrm{path}}$ ($d=3$, $\varepsilon=1$) |
|:-------|:------------------------|:----------------|:------------------------------------------------------|
| $\sigma_0=10^{-5}$, $r=1.5$ | $2.01\times 10^{-4}$ | **Tension** (above ceiling) | $\sim 7\times 10^{-3}$ |
| $\sigma_0=10^{-5}$, $r=0$ | $10^{-5}$ | OK | $\sim 3.5\times 10^{-4}$ |
| $\sigma_0=7.47\times 10^{-6}$, $r=1.5$ | $1.50\times 10^{-4}$ | On ceiling | $\sim 5.7\times 10^{-3}$ |
| $\sigma_0=5\times 10^{-6}$, $r=1.5$ | $1.00\times 10^{-4}$ | OK | $\sim 4.4\times 10^{-3}$ |
| $\sigma_0=3\times 10^{-6}$, $r=1.5$ | $6.03\times 10^{-5}$ | OK | $\sim 3.1\times 10^{-3}$ |

**Coherent architecture options:**

| Label | Definition | Role |
|:------|:-----------|:-----|
| **NP-A** | Mesoscopic seed, $G_O=1$, $\sigma_0\sim 10^{-5}$ | Safest vs DESI residual; path RMS $\sim$ few $\times 10^{-4}$ |
| **NP-B** | Mesoscopic seed + soft $r\sim 1.5$ with $\sigma_0\lesssim 7.5\times 10^{-6}$ | **Illustrative** DESI-safe branch; path RMS $\sim$ few $\times 10^{-3}$ |
| **NP-C** | Same residual $\sigma_{\mathrm{res}}\le 1.5\times 10^{-4}$ but $\varepsilon<1$ | Reduces slip RMS proportionally; needs $\varepsilon$ from theory |

**NP-user sketch** ($\sigma_0=10^{-5}$, $r=1.5$) is the right *shape* of the narrow path but must be **clipped** into NP-B (or NP-A) to stay consistent with the DESI residual null/ceiling.

**Status of NP-B (read carefully):** $\sigma_0$ and $r$ in NP-B are **not derived**. They are a **hand-placed** point in the DESI-safe window used to read order-of-magnitude path RMS **if** a mesoscopic seed and soft $G_O\sim\mathcal{O}(10)$ existed. Fitting $\ell_*$ or $r$ to DESI is forbidden ([`BOUNDARY.md`](../BOUNDARY.md)). NP-B is architecture kinematics, not a prediction of the open kernel.

---

## 5. Concrete observable prediction (conditional)

**If** a principle fixes $\ell_*$ so that $\sigma_{0,\mathrm{eff}}$ lies in the DESI-safe mesoscopic window, **and** soft open gain is at most $G_O\sim\mathcal{O}(10)$, **and** $\varepsilon\sim\mathcal{O}(1)$, then:


$$
\mathrm{RMS}_{\mathrm{path}}(|\gamma-1|) \sim 10^{-3}\text{–}10^{-4} \quad\text{at }z_s\sim 1.5,
$$


while the isotropic BAO residual remains


$$
\sigma_{\mathrm{res}} \le 1.5\times 10^{-4} \quad\text{(sister bound)}.
$$


That is a **conditional** OOM for weak lensing / slip programmes (Euclid, Rubin), **not** a detection claim and **not** a derivation of $\ell_*$.

### 5.1 Forbidden binary (same discipline as the $R_8$ honesty lock)

**Do not write or imply:**

> If deep lensing finds $\mathrm{RMS}_{\mathrm{path}}\sim 10^{-3}$, we have discovered the texture of dark energy; if not, the model is mathematically discarded with no excuses.

That sentence fails on **both** sides.

| Broken claim | Why it fails |
|:-------------|:-------------|
| Detection $\Rightarrow$ “texture of DE” | $\mathrm{RMS}\sim 10^{-3}$ in the table is the **NP-B hand point**, not a derived open-kernel prediction. Even a real excess at that band must first survive **baryonic feedback, photo-$z$ errors, intrinsic alignments, and shape systematics** — standard weak-lensing contaminants that can raise RMS without any vacuum grain. |
| Null $\Rightarrow$ “model discarded without excuses” | A null at that sensitivity excludes the **specific** $(\ell_*,G_O,\varepsilon)$ corner that was tested (e.g. NP-B), **not** the whole programme. While the R1 principle is still **absent (declared)**, smaller $\ell_*$ or smaller $G_O$ can sit below the threshold. That is the meaning of an open kernel, not a loophole. |

**Sustained wording (use this):**

> If a lensing analysis finds an excess of path-integrated slip RMS compatible with this band, **and** it survives control of baryonic feedback, photo-$z$, and intrinsic alignments, it would be the **first positive evidence** the programme has ever had — and still would not by itself prove a mesoscopic DE grain. If it does **not** detect such an excess, that **excludes NP-B (or the tested corner) specifically**, tightening the region where the still-open counting kernel could live — it does **not** close the kernel or the whole model.

Same emotion, binary fixed. Matches the $d=3$–specificity lock: no over-read of a positive coincidence, no over-read of a null.

### 5.2 Sensitivity is **not** established in-repo (check before any paper claim)

| Fact | Scale | Source |
|:-----|:------|:-------|
| Path RMS at NP-B (this repo, kinematics) | $\sim 4\times 10^{-3}$ at $z_s=1.5$ | `lib_verified` / light-cone atlas |
| Path RMS at NP-A | $\sim 3.5\times 10^{-4}$ | same |
| Indicative mean-slip floor used earlier in programme | $\sigma_{\mathrm{exp}}\sim 0.03$ | Option 0 / wall notes (order-of-magnitude) |
| Current published DESI-era slip (Maus et al.) | $\gamma=1.17\pm 0.11$ $\Rightarrow$ $\lvert\gamma-1\rvert$ uncertainty $\mathcal{O}(0.1)$ | arXiv:2505.20656 |

**Reading:** $\mathcal{O}(10^{-3})$ path RMS is **far below** current published slip errors ($\mathcal{O}(0.1)$). Stage-IV surveys (Euclid, LSST/Rubin) aim at percent-level growth/lensing and multiplicative-bias control near $10^{-3}$ in **shear calibration**, but that is **not** the same statement as “the survey measures *this* path-RMS statistic of stochastic slip wrinkles at $10^{-3}$.”

**Open experimental question (must be answered before marketing detection):**  
Does any Stage-III/IV pipeline constrain a **stochastic, path-accumulated** $\mathrm{RMS}(\lvert\gamma-1\rvert)$ (or a well-defined proxy) at $\sim 10^{-3}$ after the systematics list above?

**Partial answer with real published data** (not a full likelihood):  
[`lensing-rms-forecast-real-data.md`](lensing-rms-forecast-real-data.md) · `python scripts/lensing_rms_real_data_compare.py`

| External (cited) | Scale | vs NP-B path RMS \(\sim 4.4\times 10^{-3}\) |
|:-----------------|:------|:-------------------------------------------|
| Maus $\sigma(\gamma)=0.11$ (arXiv:2505.20656) | measured mean slip | \(\sim 25\times\) coarser |
| Sakr constant $\eta\sim 5\%$ (arXiv:2501.07477) | Euclid+DESI-like **forecast** | \(\sim 11\times\) coarser |
| DESI MG $\sigma(\Sigma_0)=0.045$ (arXiv:2411.12026) | measured | \(\sim 10\times\) coarser |
| Stage-IV $m\sim 2\times 10^{-3}$ (SRD/Euclid) | **calibration**, wrong operator | must not be rebranded as path-RMS reach |

Until a dedicated forecast maps **this** statistic into survey likelihoods, treat $10^{-3}$ as a **theory-side OOM target**, not an established survey capability.

---

## 6. What the theory must stop trying to do

| Abandoned programme | Replacement |
|:--------------------|:------------|
| Explain why $\Lambda$ is small via Planck pixel noise seen in BAO | Predict a **mesoscopic DE grain** and its light-path imprint |
| Stretch $10^{-61}$ by geometry or soft squeezing | Change the counting object (R1) |
| Put all signal into $H(z)$ | Prefer $\pi_T$ / slip / lensing (R2) |
| Free $r\sim 64$ or free $N\sim 10^{119}$ | Excluded (A3) |

---

## 7. Causal diagram (narrow path)

```text
R1 mesoscopic cell
 ell_* ~ 1–10 Mpc → sigma_0,eff ~ 3e-6 … 1e-5
 │
 ▼
R3 soft open map (optional, bounded)
 r = O(1) → G_O ~ 1–20
 with sigma_res = G_O * sigma_0 ≤ 1.5e-4 (DESI-safe)
 │
 ▼
R2 anisotropic stress → light
 |γ-1|_loc ∝ sigma_res
 RMS_path = |γ-1|_loc * sqrt(χ / ell_*)
 │
 ▼
 RMS(γ) ~ 1e-4 … few×1e-3 (conditional, testable)
```

---

## 8. Status under the package axioms

| Element | Status |
|:--------|:-------|
| Algebra of the narrow path | **Verified** (`lib_verified` + tests) |
| DESI-safe window NP-A / NP-B numbers | **Verified** as kinematics of **hand-placed** points |
| NP-B as derived prediction | **Not claimed** ($\sigma_0$, $r$ not fixed by principle) |
| Principle fixing $\ell_*$ | **Open** (R1a/b/c/d; [`r1-open-kernel.md`](r1-open-kernel.md)) |
| Microphysical $r=\mathcal{O}(1)$ from horizon bath | **Open** (soft $r$ is only a kinematic allowance) |
| $\varepsilon$ from SDiff | **Open** |
| Detection / “texture of DE” | **Not claimed** |
| Null $\Rightarrow$ full model death | **Not claimed** (null tightens tested corner only) |
| Stage-IV reach of this RMS statistic at $10^{-3}$ | **Not established in-repo** (§5.2) |

---

## 9. One-sentence thesis

> The only soft-regime, physically constrained route to a *conditionally* telescope-visible stochastic DE imprint is a **mesoscopic counting seed**, optionally dressed by **$\mathcal{O}(10)$ open gain**, read out through **anisotropic stress and light-path accumulation** at $\mathrm{RMS}(\gamma-1)\sim 10^{-4}$–$10^{-3}$ **if** that corner is realised, while keeping the isotropic residual under the DESI ceiling — not a rescue of $10^{-61}$ by unphysical amplifiers, and not a binary discovery/death test of the whole programme.

---

## 10. Reproduce

```bash
cd measurable-stochastic-vacuum
pytest -q
python - <<'PY'
import sys; sys.path.insert(0,"scripts")
from lib_verified import *
L_H,_,s0=sorkin_holographic(); MPC=3.085677581e22
print("ell*(d=3,1e-5) Mpc", ell_for_target_sigma(1e-5,L_H,3)/MPC)
print("sigma_res", residual_soft_map(1e-5,1.5))
print("RMS", rms_incoherent(slip_deviation(1,residual_soft_map(1e-5,1.5),0.8),
 n_patches(comoving_distance_mpc(1.5), ell_for_target_sigma(1e-5,L_H,3)/MPC)))
PY
```

---

*End of narrow-path note.*
