# The observable wall: Einstein + Morales, without undeclared free parameters

**Author:** Jesús Morales Souhail 
**ORCID:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818) 
**Date:** July 2026 
**Status:** Derived relation + detectability inequality (English, referee-ready) 
**Code:** `scripts/lib_verified.py` · `tests/test_verified.py` 
**Sister bound:** $\sigma_X < 1.5\times 10^{-4}$ (95% CL) in [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou)

---

## Abstract

The only **fully derived** map from the stochastic dark-energy amplitude $\sigma_X$ (Morales residual sector) to a large-scale structure observable **without undeclared free parameters** is the sub-horizon **gravitational-slip wall**


$$
\lvert\gamma-1\rvert = 2 \varepsilon \sigma_X \frac{\rho_X}{\rho_m \lvert\delta_m\rvert} = 2 \varepsilon \sigma_X \frac{\Omega_{\Lambda 0}}{\Omega_{m0} (1+z)^3 \lvert\delta_m\rvert}.
$$


Combined with the DESI residual ceiling on $\sigma_X$, this equation predicts a **maximum** slip signal $\lvert\gamma-1\rvert_{\max}\sim 10^{-4}$ — hundreds of times below current/forecast experimental floors. That inequality is the mathematical definition of **experimental self-shielding** for this channel.

**Not derived (and not used as a hard wall):** identifying a Lorentz-violation coefficient $\xi$ with $\sigma_X$ in GRB time delays.

**Operational consequence:** the experiment that can probe this physics is not a local amplifier of a Planck seed; it is a **measurement along the past light cone** (integrate shear wrinkles backwards in cosmic time), i.e. deep lensing / RSD×lensing path integrals — still subject to the wall above unless $\sigma_X$ or $\varepsilon$ is larger for derived reasons.

---

## 1. Ingredients (only physics + model definition)

### 1.1 Einstein (linearized Newtonian gauge, sub-horizon)

**Poisson**


$$
k^{2}\Psi = -4\pi G a^{2} \rho_m\delta_m. \tag{E1}
$$


**Anisotropy (traceless spatial stress)**


$$
k^{2}(\Phi-\Psi) = 8\pi G a^{2} \pi_T. \tag{E2}
$$


(Standard form; Ma & Bertschinger 1995.)

### 1.2 Newton / background ratio (flat $\Lambda$CDM)


$$
\frac{\rho_X}{\rho_m} = \frac{\Omega_{\Lambda 0}}{\Omega_{m0} (1+z)^3}. \tag{N1}
$$


### 1.3 Morales stochastic residual (definition of the noise amplitude)

The isotropic fractional residual amplitude of the dark-energy density is bounded by the sister BAO analysis as $\sigma_X$. 
The **anisotropic** piece is defined as a fraction $\varepsilon\in[0,1]$ of that residual:


$$
\pi_T = \varepsilon \delta\rho_X = \varepsilon \sigma_X \rho_X. \tag{M1}
$$


No free $10^{56}$. No identification with Planck-pixel counting unless separately postulated (and then killed by soft dynamics).

---

## 2. Derivation of the wall equation (three lines)

Divide (E2) by (E1):


$$
\frac{\Phi-\Psi}{\Psi} = - \frac{2\pi_T}{\rho_m\delta_m}.
$$


With $\gamma\equiv\Phi/\Psi$ and absolute values for the amplitude,


$$
\lvert\gamma-1\rvert = \frac{2\lvert\pi_T\rvert}{\rho_m\lvert\delta_m\rvert}.
$$


Insert (M1) and (N1):


$$
\lvert\gamma-1\rvert = 2 \varepsilon \sigma_X \frac{\Omega_{\Lambda 0}}{\Omega_{m0} (1+z)^3 \lvert\delta_m\rvert} \tag{W}
$$


**That is the equation.** 
Einstein + Newton background + Morales residual definition. No undeclared free parameters.

---

## 3. Numerical wall (using the DESI residual ceiling)

Sister result (a posteriori input, not a free dial inside the derivation of (W)):


$$
\sigma_X < 1.5\times 10^{-4} \quad(95\%~\mathrm{CL}).
$$


Best-case shear ($\varepsilon=1$, $\lvert\delta_m\rvert=1$, $\Omega_{m0}=0.315$, $\Omega_{\Lambda 0}=0.685$):

| $z$ | $\rho_X/\rho_m$ | $\lvert\gamma-1\rvert_{\max}$ |
|:----|:----------------|:--------------------------------|
| $0$ | $2.175$ | $6.52\times 10^{-4}$ |
| $0.5$ | $0.644$ | $1.93\times 10^{-4}$ |
| $1.0$ | $0.272$ | $8.15\times 10^{-5}$ |

**Order-of-magnitude prediction of the model under the DESI ceiling:**


$$
\lvert\gamma-1\rvert_{\max} \sim 10^{-4}.
$$


---

## 4. Self-shielding: the inequality that *is* the experiment wall

Define the experimental sensitivity on slip as $\sigma_{\mathrm{exp}}(\gamma)$ (rms error on $\lvert\gamma-1\rvert$ or $\lvert\eta-1\rvert$).

**Invisibility (self-shielding) regime**


$$
S_{\mathrm{pred}}^{\max} = \lvert\gamma-1\rvert_{\max}(\sigma_X^{\mathrm{DESI}},\varepsilon=1) \ll \sigma_{\mathrm{exp}}(\gamma) \tag{S}
$$


With $\lvert\gamma-1\rvert_{\max}\sim(2$–$7)\times 10^{-4}$ and

| Experiment | $\sigma_{\mathrm{exp}}(\gamma)$ (indicative) | Factor $S_{\mathrm{pred}}/\sigma_{\mathrm{exp}}$ |
|:-----------|:-----------------------------------------------|:--------------------------------------------------|
| DESI-era slip (Maus-like $\mathcal{O}(0.1)$) | $\sim 0.1$ | $\sim 10^{-3}$ |
| Euclid-like forecast | $\sim 0.03$–$0.05$ | $\sim 10^{-2}$ |

**Interpretation:** under Einstein+(M1) and the BAO residual ceiling, the model **predicts a signal the experiment cannot reach**. That is experimental self-shielding of this channel — not a failure of the derivation.

---

## 5. The inverse equation: what $\sigma_X$ would be needed to *break* the shield

For a discovery-scale threshold $N_{\sigma}$ (e.g. $N_{\sigma}=5$),


$$
\lvert\gamma-1\rvert \ge N_{\sigma} \sigma_{\mathrm{exp}}(\gamma).
$$


Invert (W) at $\varepsilon=1$, $\lvert\delta_m\rvert=1$:


$$
\sigma_X \ge \frac{N_{\sigma} \sigma_{\mathrm{exp}}(\gamma) (1+z)^3 \Omega_{m0}} {2 \Omega_{\Lambda 0}} \tag{D}
$$


**Example** ($z=0$, $N_{\sigma}=5$, $\sigma_{\mathrm{exp}}=0.03$):


$$
\sigma_X \ge \frac{5\times 0.03\times 0.315}{2\times 0.685} \approx 0.0345.
$$


Compare to DESI residual ceiling $1.5\times 10^{-4}$:


$$
\frac{\sigma_X^{\mathrm{(needed)}}}{\sigma_X^{\mathrm{(allowed)}}} \approx \frac{0.0345}{1.5\times 10^{-4}} \approx 230.
$$


**Summary:** 
equation (D) is the door the experiment would need; the DESI residual ceiling locks that door from the inside.

---

## 6. What is *not* the solid wall (GRB / LIV)

A photon time-delay template of the form


$$
\Delta t \sim \xi \frac{E^{n}}{M_{\mathrm{Pl}}^{n}} H_0^{-1}\int_0^z\frac{(1+z')^{n}}{E(z')} \mathrm{d}z'
$$


is standard LIV phenomenology. Setting


$$
\xi \stackrel{?}{=} \sigma_X
$$


is **not** a consequence of Einstein+(M1). It is an extra assumption. 
Therefore GRB delays are **not** used here as a parameter-free observable wall.

---

## 7. “Measure backwards in time” — rigorous meaning

The colloquial phrase means **not** time machines. It means:

### 7.1 The observable lives on the **past null cone**

Photons from $z_s$ to $z=0$ integrate potential wrinkles:


$$
\mathrm{RMS}_{\mathrm{path}} = \lvert\gamma-1\rvert_{\mathrm{loc}} \sqrt{\frac{\chi(z_s)}{\ell_*}}. \tag{P}
$$


That is a measurement **into the past** along the light path — the only direction cosmic light carries information.

### 7.2 Why “forward / local” amplification fails

Trying to amplify a present-day Planck seed ($10^{-61}$) with soft open maps or path geometry is already ruled out (need $r\sim 64$ or $N\sim 10^{119}$). 
**Backwards** means: use **deep path-integrated** probes (lensing, RSD×CMB lensing, multi-$z$ slip), not local free amplification.

### 7.3 Self-shielded experiment design

| Do | Do not |
|:---|:-------|
| Measure $\gamma(z)$ / shear along the past light cone | Invent $\xi=\sigma_X$ for GRBs without derivation |
| Use (W)+(S)+(D) as the quantitative wall | Fit $\ell_*$ to evade DESI |
| Keep background $=\Lambda$CDM (bulk) | Expect isotropic BAO residual detection first |

Even path accumulation only multiplies by $\sqrt{N}=\mathcal{O}(10$–$10^{2})$ — it does **not** cancel the wall of equation (W) under the DESI ceiling; it slightly softens it (see `NARROW_PATH.md` NP-A/B).

---

## 8. Master system (Einstein–Newton–Morales wall)

**(E1) Poisson**


$$
k^{2}\Psi = -4\pi G a^{2}\rho_m\delta_m.
$$


**(E2) Anisotropy**


$$
k^{2}(\Phi-\Psi) = 8\pi G a^{2}\pi_T.
$$


**(M1) Morales residual shear**


$$
\pi_T = \varepsilon\sigma_X\rho_X.
$$


**(W) Observable wall**


$$
\lvert\gamma-1\rvert = 2\varepsilon\sigma_X\frac{\rho_X}{\rho_m\lvert\delta_m\rvert}.
$$


**(S) Self-shielding**


$$
\lvert\gamma-1\rvert_{\max}(\sigma_X^{\mathrm{DESI}}) \ll \sigma_{\mathrm{exp}}.
$$


**(D) Detectability inverse**


$$
\sigma_X^{\mathrm{(detect)}} \ge \frac{N_{\sigma}\sigma_{\mathrm{exp}}(1+z)^{3}\Omega_{m0}}{2\Omega_{\Lambda 0}}.
$$


**(P) Past light-cone RMS**


$$
\mathrm{RMS}_{\mathrm{path}} = \lvert\gamma-1\rvert_{\mathrm{loc}}\sqrt{\frac{\chi(z_s)}{\ell_*}}.
$$


**(W)** defines the observable. 
**(S)** defines self-shielding. 
**(D)** defines what would be needed to break the shield. 
**(P)** is the only natural amplifier (path statistics). 
Past null-cone measurements still face (S) unless new *derived* physics raises $\sigma_X$ or $\varepsilon$ without undeclared free parameters.

---

## 9. Relation to the $\Lambda$-simple model

| $\Lambda$-simple language | Wall language |
|:--------------------------|:--------------|
| Bulk $=\Lambda$CDM | Mean potentials with $\Phi=\Psi$ at leading order |
| Edge grain $\sigma$ | $\sigma_X$ in (M1) |
| $\mathrm{RMS}\sim\sigma^{2/3}$ | Path form of (W)+(P) after counting |
| DESI bound | Input to (S) and (D) |

---

## 10. Reproduce

```bash
cd measurable-stochastic-vacuum
pytest -q
python - <<'PY'
import sys; sys.path.insert(0,"scripts")
from lib_verified import slip_deviation, rho_x_over_rho_m
for z in (0.0,0.5,1.0):
 print(z, slip_deviation(1.0, 1.5e-4, z), rho_x_over_rho_m(z))
# detectability threshold z=0, 5-sigma, sigma_exp=0.03
Om,Ol=0.315,0.685
print("sigma_X needed", 5*0.03*Om/(2*Ol))
PY
```

---

*End of observable-wall note.*
