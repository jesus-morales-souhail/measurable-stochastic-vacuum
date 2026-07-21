# For referees: claim map, reading order, and formula sheet

**Author:** Jesús Morales Souhail 
**ORCID:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818) 
**Email:** jmskjym@gmail.com 
**Repository:** https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum 
**Date:** July 2026 
**Status:** Independent research — **not peer reviewed** 
**Automated gate:** `pytest -q` must report **34 passed**

---

## 1. What this repository is (and is not)

| This repository | Sister repository |
|:----------------|:------------------|
| Theory kinematics + verified identities | Empirical DESI BAO residual analysis |
| Minimal model as simple as $\Lambda$ | Working bound $\sigma_X < 1.5\times 10^{-4}$ (95% CL) |
| Conditional light-path predictions | Model kills (e.g. coherent tachyonic growth) |
| **Not** a detection paper | **Not** a first-principles derivation of $\ell_*$ |

**Sister empirical corpus:** 
https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou 
Manuscript: `manuscript/PREPRINT.md`

---

## 2. Mandatory reading order (peer review)

| Step | Document | Purpose |
|:-----|:---------|:--------|
| 1 | This file | Claim boundaries |
| 2 | [`OBSERVABLE_WALL.md`](OBSERVABLE_WALL.md) | **Einstein+Morales slip wall + self-shielding inequality** |
| 2b | [`PAST_LIGHT_CONE_INTEGRATION.md`](PAST_LIGHT_CONE_INTEGRATION.md) | **Only natural amplifier: $\mathrm{RMS}=|\gamma-1|\sqrt{\chi/\ell_*}$** |
| 3 | [`SIMPLE_AS_LAMBDA.md`](SIMPLE_AS_LAMBDA.md) | Minimal equations (public model) |
| 4 | [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md) | **Only hard, test-gated claims** |
| 5 | [`NARROW_PATH.md`](NARROW_PATH.md) | DESI-safe windows NP-A / NP-B |
| 6 | [`TOPOLOGICAL_EDGE_ANALOGY.md`](TOPOLOGICAL_EDGE_ANALOGY.md) | Optional analogy (bulk/edge); not a derivation |
| 7 | Sister `PREPRINT.md` | Empirical null and $\sigma_X$ bound |

**Do not cite as hard results:** `THEORY_REVOLUTION.md`, WP discussion notes (`r1-`, `r2-`, `r3-`), exploratory optics repo.

---

## 3. Formula sheet (consistent notation)

### 3.1 Background (identical to flat $\Lambda$CDM)


$$
H^{2}(z)=H_{0}^{2}\bigl[\Omega_{m}(1+z)^{3}+\Omega_{\Lambda}\bigr].
$$


### 3.2 Counting seed (hypothesis $d=3$)


$$
N_{\mathrm{eff}}=\Bigl(\frac{L_{H}}{\ell_{*}}\Bigr)^{3}, \qquad \sigma=\frac{1}{\sqrt{N_{\mathrm{eff}}}}=\Bigl(\frac{\ell_{*}}{L_{H}}\Bigr)^{3/2}, \qquad \ell_{*}=L_{H} \sigma^{2/3},
$$


with $L_{H}=c/H_{0}$.

### 3.3 Holographic Sorkin seed (special case $d=2$, $\ell_{*}=L_{P}$)


$$
\sigma_{0}=\frac{L_{P}}{L_{H}}\sim 1.18\times 10^{-61} \quad(H_{0}=67.4 \mathrm{km s^{-1} Mpc^{-1}}).
$$


### 3.4 Soft open map (optional, bounded)


$$
G_{O}=e^{2r}, \qquad \sigma_{\mathrm{res}}=G_{O} \sigma \quad(r=\mathcal{O}(1);\ e.g.\ r=1.5\Rightarrow G_{O}\approx 20.09).
$$


**DESI-safe constraint (a posteriori):** $\sigma_{\mathrm{res}}\le 1.5\times 10^{-4}$.

### 3.5 Local gravitational slip (sub-horizon GR)


$$
\pi_{T}=\varepsilon \sigma_{\mathrm{res}} \rho_{X}, \qquad \lvert\gamma-1\rvert = 2\varepsilon\sigma_{\mathrm{res}}\frac{\rho_{X}}{\rho_{m}\lvert\delta_{m}\rvert}.
$$


Assumptions: Newtonian gauge, $k\gg aH$, $\mu=1$, phenomenological $\pi_{T}$.

### 3.6 Light-path accumulation (iid patches)


$$
N_{\mathrm{pat}}=\frac{\chi}{\ell_{*}}, \qquad \mathrm{RMS}_{\mathrm{path}} = \lvert\gamma-1\rvert_{\mathrm{loc}}\sqrt{N_{\mathrm{pat}}}.
$$


### 3.7 Blackboard reduction ($d=3$, $\chi\sim L_{H}$, $\alpha\sim\mathcal{O}(1)$)


$$
\mathrm{RMS}_{\mathrm{path}} \sim \alpha \sigma\sqrt{\frac{L_{H}}{\ell_{*}}} = \alpha \sigma^{2/3}.
$$


**Warning:** $\sigma\times G_{O}\times\sqrt{N}\neq\mathrm{RMS}_{\mathrm{path}}$ in general (prefactor $\alpha$ and operator order).

---

## 4. Claim checklist

### 4.1 Claims (supported in-repo)

| ID | Claim | Evidence |
|:---|:------|:---------|
| C1 | Counting identities and inversion $\ell_{*}(\sigma)$ | `lib_verified` + tests |
| C2 | Sorkin $\sigma_{0}\sim 10^{-61}$ under holographic $d=2$ | identity + test |
| C3 | Soft $G_{O}=e^{2r}$; $r\sim 64$ needed to lift Sorkin to $10^{-5}$ | algebra + tests |
| C4 | Local slip formula under stated GR assumptions | §3.5 + tests |
| C5 | Path $\mathrm{RMS}=s\sqrt{N}$ for iid zero-mean patches | MC + tests |
| C6 | Path + soft open **cannot** rescue Sorkin | combined tests |
| C7 | DESI-safe windows NP-A / NP-B exist with $\mathrm{RMS}\sim 10^{-4}$–$10^{-3}$ | `NARROW_PATH` + tests |
| C8 | Sister DESI bound $\sigma_{X}<1.5\times 10^{-4}$ (95% CL) used only a posteriori | sister repo |
| C9 | Slip wall (W) from Einstein+(M1); self-shielding (S); invert (D) | `OBSERVABLE_WALL.md` + tests |

### 4.2 Non-claims

| ID | Non-claim |
|:---|:----------|
| N1 | No derivation of why $\ell_{*}$ is galactic |
| N2 | No microphysical horizon bath fixing $r=\mathcal{O}(1)$ or $r\sim 64$ |
| N3 | No first-principles $\varepsilon$ from SDiff |
| N4 | No detection of stochastic DE or of slip |
| N5 | Cosmos is **not** asserted to be a fractional Hall bar (analogy only) |
| N6 | Entropy of the universe does **not** “stop”; only local backscattering of a protected channel is suppressed (analogy) |
| N7 | Not peer reviewed |

---

## 5. Numerical anchors (reproducible)

Fiducial: $H_{0}=67.4 \mathrm{km s^{-1} Mpc^{-1}}$, $\Omega_{m}=0.315$, $\Omega_{\Lambda}=0.685$, $z_{s}=1.5$.

| Scenario | $\sigma$ (seed) | $G_{O}$ | $\sigma_{\mathrm{res}}$ | $\ell_{*}$ ($d=3$) | $\mathrm{RMS}_{\mathrm{path}}$ (exact path formula) |
|:---------|:----------------|:--------|:------------------------|:-------------------|:-----------------------------------------------------|
| Sorkin | $1.18\times 10^{-61}$ | 1 | same | (Planck / holographic) | $\ll 10^{-40}$ |
| NP-A | $10^{-5}$ | 1 | $10^{-5}$ | $\approx 2.07 \mathrm{Mpc}$ | $\approx 3.5\times 10^{-4}$ |
| NP-B | $5\times 10^{-6}$ | $\approx 20.1$ | $10^{-4}$ | $\approx 1.30 \mathrm{Mpc}$ | $\approx 4.4\times 10^{-3}$ |

```bash
pip install -r requirements.txt
pytest -q
python scripts/simple_as_lambda.py
python scripts/lib_verified.py
```

---

## 6. Topological edge analogy (scope control)

[`TOPOLOGICAL_EDGE_ANALOGY.md`](TOPOLOGICAL_EDGE_ANALOGY.md) is **pedagogy**:

- bulk $\leftrightarrow$ $\Lambda$ (smooth mean), 
- edge $\leftrightarrow$ grain $\sigma$ (shear / light), 
- no backscattering $\leftrightarrow$ free-lunch channels closed.

It is **not** a condensed-matter derivation of dark energy.

---

## 7. Suggested evaluation criteria for referees

1. Are hard claims limited to C1–C8 and backed by `pytest`? 
2. Is the DESI number used only as a bound, never to fit $\ell_{*}$? 
3. Is the minimal model no more complex than $\Lambda$CDM + one $\sigma$? 
4. Are free $10^{56}$, $r\sim 64$, and $N\sim 10^{119}$ correctly rejected? 
5. Are open problems (N1–N3) stated without hype?

---

## 8. Contact

**Jesús Morales Souhail** · jmskjym@gmail.com · ORCID 0009-0000-7637-1818

---

*End of referee package.*
