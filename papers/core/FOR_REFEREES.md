# Reading guide: statement of results, reading order, and formula sheet

**Author:** Jesús Morales Souhail
**ORCID:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)
**Email:** jmskjym@gmail.com
**Repository:** https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum
**Date:** July 2026
**Status:** Independent research
**Index:** [`INDEX.md`](INDEX.md)
**Tests:** `pytest -q`

---

## 1. What this repository is (and is not)

Theory and data live in two places. This repo: kinematics and identities I can check with code. Related repository: DESI residual analysis.

| This repository | Related repositoriesitory |
|:----------------|:------------------|
| Theory kinematics + verified identities | Empirical DESI BAO residual analysis |
| Minimal model as simple as $\Lambda$ | Working bound $\sigma_X < 2.5\times 10^{-2}$ (95% CL) |
| Conditional light-path predictions | Model kills (e.g. coherent tachyonic growth) |
| Map of **measured walls** vs **open kernel** (R1) | Amplification gap (no free soft gain on Sorkin) |
| **Not** a detection paper | Empirical DESI residual bound |
| Conditional uniqueness $\ell_{\ast}\sim R_{\mathrm{nl}}$ under A0–A4 | **Not** a proof that SM realises $\chi$ |

**Related empirical corpus:**
https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou
Manuscript: `manuscript/PREPRINT.md`

---

## 2. Reading order

| Step | Document | Content |
|:-----|:---------|:--------|
| 1 | This file | claim boundaries |
| 2 | [`OBSERVABLE_WALL.md`](OBSERVABLE_WALL.md) | slip wall + self-shielding inequality |
| 2b | [`PAST_LIGHT_CONE_INTEGRATION.md`](PAST_LIGHT_CONE_INTEGRATION.md) | path $\mathrm{RMS}=\lvert\gamma-1\rvert\sqrt{\chi/\ell_{\ast}}$ |
| 3 | [`SIMPLE_AS_LAMBDA.md`](SIMPLE_AS_LAMBDA.md) | minimal equations |
| 4 | [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md) | unit-tested claims |
| 5 | [`NARROW_PATH.md`](NARROW_PATH.md) | DESI-safe windows NP-A / NP-B |
| 5b | [`r1-open-kernel.md`](../r1_kernel/r1-open-kernel.md) | walls vs open kernel |
| 5c | [`lensing-rms-forecast-real-data.md`](../side_threads/lensing-rms-forecast-real-data.md) | path RMS vs Maus / Sakr / DESI MG |
| 5d | [`inflation-spectator-seed-gordon-wands.md`](../side_threads/inflation-spectator-seed-gordon-wands.md) | Gordon & Wands spectator (factor $\sim 45$) |
| 5e | [`inflation-spectator-residual-atlas.md`](../side_threads/inflation-spectator-residual-atlas.md) | $r\to\sigma_\rho$ atlas |
| 5f | [`h0-running-brachistochrone-bridge.md`](../closed_walls/h0-running-brachistochrone-bridge.md) | H0 running + time-delay literature |
| 5g | [`h0-bridge-toy-map.md`](../closed_walls/h0-bridge-toy-map.md) | toy $\delta D/D$ short of H0 tension |
| 5h | [`h0-desqueezing-filter.md`](../closed_walls/h0-desqueezing-filter.md) | invented $H_0(z)$ rejected; $\sigma_X\ll 9\%$ |
| 5i | [`ell-star-r0-peculiar-scales.md`](../closed_walls/ell-star-r0-peculiar-scales.md) | $r_0$ / $n^{-1/3}$ vs NP-A |
| 5j | [`r1-scale-decade-8-12.md`](../r1_kernel/r1-scale-decade-8-12.md) | 8–12 Mpc decade |
| 5k | [`r1-principle-nonlinear-matter.md`](../r1_kernel/r1-principle-nonlinear-matter.md) | $\ell_{\ast}=R_{\mathrm{nl}}$; $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ |
| 5l | [`r1-t1-mechanisms-compute.md`](../r1_kernel/r1-t1-mechanisms-compute.md) | domain counting + nonlinear mask |
| 5m | [`r1-mechanism-candidates.md`](../r1_kernel/r1-mechanism-candidates.md) | mechanism candidates |
| 5n | [`r1-t12-bbks-and-derivation.md`](../r1_kernel/r1-t12-bbks-and-derivation.md) | BBKS $R_{\ast}$ |
| 5o | [`r1-derivation-sandwich.md`](../r1_kernel/r1-derivation-sandwich.md) | sandwich under A0–A4 |
| 5p | [`NOTE_uniqueness_residual_grain.md`](../r1_kernel/NOTE_uniqueness_residual_grain.md) | uniqueness note |
| 5q | [`r1-sandwich-falsifiers.md`](../r1_kernel/r1-sandwich-falsifiers.md) | F1–F4 falsifiers |
| 5r | [`r1-a1-microphysics.md`](../r1_kernel/r1-a1-microphysics.md) | $g\chi\delta_m$ map |
| 5s | [`r1-real-velocity-block-net.md`](../r1_kernel/r1-real-velocity-block-net.md) | CF4 block net (matter) |
| 5t | [`r1-collapse-relief.md`](../r1_kernel/r1-collapse-relief.md) | CF4 collapse peaks (matter) |
| 5u | [`what-i-would-put-in-a-paper.md`](../what-i-would-put-in-a-paper.md) | paper map |
| 6 | [`TOPOLOGICAL_EDGE_ANALOGY.md`](../side_threads/TOPOLOGICAL_EDGE_ANALOGY.md) | analogy only |
| 7 | Sister `PREPRINT.md` | empirical $\sigma_X$ bound |

Not hard results: `minimal-theory-package.md`, exploratory optics sister, long WP discussion unless it restates verified identities.
`r1-open-kernel.md`: walls vs kernel and scale arithmetic — not a derivation of $\ell_{\ast}=R_8$.
CF4 notes: matter $v_{\mathrm{pec}}$ only — not $\sigma_X$ or $g$.

---

## 3. Formula sheet (consistent notation)

### 3.1 Background (identical to flat $\Lambda$CDM)


H^{2}(z)=H_{0}^{2}\bigl[\Omega_{m}(1+z)^{3}+\Omega_{\Lambda}\bigr].


### 3.2 Counting seed (hypothesis $d=3$)


N_{\mathrm{eff}}=\Bigl(\frac{L_{H}}{\ell_{*}}\Bigr)^{3}, \qquad \sigma=\frac{1}{\sqrt{N_{\mathrm{eff}}}}=\Bigl(\frac{\ell_{*}}{L_{H}}\Bigr)^{3/2}, \qquad \ell_{*}=L_{H} \sigma^{2/3},


with $L_{H}=c/H_{0}$.

### 3.3 Holographic Sorkin seed (special case $d=2$, $\ell_{*}=L_{P}$)


\sigma_{0}=\frac{L_{P}}{L_{H}}\sim 1.18\times 10^{-61} \quad(H_{0}=67.4 \mathrm{km s^{-1} Mpc^{-1}}).


### 3.4 Soft open map (optional, bounded)


G_{O}=e^{2r}, \qquad \sigma_{\mathrm{res}}=G_{O} \sigma \quad(r=\mathcal{O}(1);\ e.g.\ r=1.5\Rightarrow G_{O}\approx 20.09).


**DESI-safe constraint (a posteriori):** $\sigma_{\mathrm{res}}\le 2.5\times 10^{-2}$.

### 3.5 Local gravitational slip (sub-horizon GR)


\pi_{T}=\varepsilon \sigma_{\mathrm{res}} \rho_{X}, \qquad \lvert\gamma-1\rvert = 2\varepsilon\sigma_{\mathrm{res}}\frac{\rho_{X}}{\rho_{m}\lvert\delta_{m}\rvert}.


Assumptions: Newtonian gauge, $k\gg aH$, $\mu=1$, phenomenological $\pi_{T}$.

### 3.6 Light-path accumulation (iid patches)


N_{\mathrm{pat}}=\frac{\chi}{\ell_{*}}, \qquad \mathrm{RMS}_{\mathrm{path}} = \lvert\gamma-1\rvert_{\mathrm{loc}}\sqrt{N_{\mathrm{pat}}}.


### 3.7 Simplified presentation reduction ($d=3$, $\chi\sim L_{H}$, $\alpha\sim\mathcal{O}(1)$)


\mathrm{RMS}_{\mathrm{path}} \sim \alpha \sigma\sqrt{\frac{L_{H}}{\ell_{*}}} = \alpha \sigma^{2/3}.


**Warning:** $\sigma\times G_{O}\times\sqrt{N}\neq\mathrm{RMS}_{\mathrm{path}}$ in general (prefactor $\alpha$ and operator order).

---

## 4. Claims

### 4.1 Supported in-repo

| ID | Claim | Evidence |
|:---|:------|:---------|
| C1 | Counting identities and inversion $\ell_{*}(\sigma)$ | `lib_verified` + tests |
| C2 | Sorkin $\sigma_{0}\sim 10^{-61}$ under holographic $d=2$ | identity + test |
| C3 | Soft $G_{O}=e^{2r}$; $r\sim 64$ needed to lift Sorkin to $10^{-5}$ | algebra + tests |
| C4 | Local slip formula under stated GR assumptions | §3.5 + tests |
| C5 | Path $\mathrm{RMS}=s\sqrt{N}$ for iid zero-mean patches | MC + tests |
| C6 | Path + soft open **cannot** rescue Sorkin | combined tests |
| C7 | DESI-safe windows NP-A / NP-B exist as **hand-placed** kinematics with $\mathrm{RMS}\sim 10^{-4}$–$10^{-3}$ | `NARROW_PATH` + tests |
| C8 | Sister DESI bound $\sigma_{X}<2.5\times 10^{-2}$ (95% CL) used only a posteriori | related repository |
| C9 | Slip wall (W) from Einstein+(M1); self-shielding (S); invert (D) | `OBSERVABLE_WALL.md` + tests |
| C10 | Soft amplifiers of Sorkin are **measured walls**; R1 principle for $\ell_{\ast}$ is a separate **open kernel** | `r1-open-kernel.md` + verified core |
| C11 | Scale arithmetic: $R_8=8/h$; $\ell_{\ast}(\sigma,d)$ and $\sigma(R_8,d)$ under counting; **$R_8$ proximity is $d=3$-specific** | `lib_verified` + `scripts/r1/r1_open_kernel_scales.py` + tests |
| C12 | Path RMS (NP-A/B) vs published Maus/Sakr/DESI-MG errors: mean slip still $\sim 10$–$25\times$ above NP-B | `lensing-rms-forecast-real-data.md` + script + tests |
| C13 | Gordon & Wands: seed $H_{\mathrm{inf}}/2\pi$; growth factor $\sim 45$ (not $10^{56}$); distinct from Sorkin soft gap | `inflation-spectator-seed-gordon-wands.md` + `scripts/side/gordon_wands_factor45.py` |
| C14 | At $r\sim 0.036$, $\delta Q/M_p\sim 3\times 10^{-6}$; with $A\sim 45$, $\varepsilon_Q\sim 0.05$ get $\sigma_\rho\sim\mathrm{few}\times 10^{-5}$ (OOM) | `inflation-spectator-residual-atlas.md` + script + tests |
| C15 | DESI-safe path-RMS toy: $H_0(0.15)/H_0(1.5)\approx 1.006$, not $1.083$; $\beta$ short $\times 16$–$38$ | `h0-bridge-toy-map.md` + script + tests |
| C16 | Residual amplitude $\sigma_X<2.5\times 10^{-2}$ (95% CL) cannot source $\delta H/H\sim 0.083$ (short $\gtrsim 500\times$); hand-tuned $\theta\sim 0.47$ excluded | `h0-desqueezing-filter.md` + script + tests |

### 4.2 Not claimed

| ID | Not claimed |
|:---|:----------|
| N1 | No derivation of why $\ell_{*}$ is galactic |
| N2 | No microphysical horizon bath fixing $r=\mathcal{O}(1)$ or $r\sim 64$ |
| N3 | No first-principles $\varepsilon$ from SDiff |
| N4 | No detection of stochastic DE or of slip |
| N5 | Cosmos is **not** asserted to be a fractional Hall bar (analogy only) |
| N6 | Entropy of the universe does **not** “stop”; only local backscattering of a protected channel is suppressed (analogy) |
| N7 | Preprint status |
| N8 | $\ell_{\ast}=R_8$ is **not** derived; S$_8$ is **not** explained; $d=3$ proximity is **tolerated**, not preferred by fit |
| N9 | NP-B is **not** a derived prediction; detection of $\mathrm{RMS}\sim 10^{-3}$ is **not** automatic DE texture |
| N10 | Null lensing at $\sim 10^{-3}$ does **not** kill the whole model — only the tested $(\ell_{\ast},G_O,\varepsilon)$ corner |
| N11 | Stage-IV sensitivity to **this** path-RMS statistic at $10^{-3}$ is **not** claimed established |
| N12 | Gordon & Wands (2005) is **not** “the same $10^{56}$ wall”; factor $\sim 45$ for **their** target; **not** automatic DESI claim |
| N13 | Atlas windows $ (r,A,\varepsilon_Q)$ are **not** DESI fits; $\sigma_\rho\not\equiv\sigma_X$ without map |
| N14 | Brachistochrone / H0-running note does **not** solve Hubble tension or derive $\ell_{\ast}$ |
| N15 | Coherent $\delta D/D\propto N$ is not an $H_0$ fix under the amplifier rules of this programme |
| N16 | $H_0(z)=H_{0,\mathrm{fid}}[1+\varepsilon e^{-\theta x}]$ with $\theta$ fit to $z\sim 0.5$–$0.7$ is **not** a result |
| N17 | CPL 2.5σ/4.2σ must **not** be relabelled as H0-running significance |

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
python scripts/core/simple_as_lambda.py
python scripts/core/lib_verified.py
python scripts/r1/r1_open_kernel_scales.py
```

---

## 6. Topological edge analogy (scope control)

[`TOPOLOGICAL_EDGE_ANALOGY.md`](../side_threads/TOPOLOGICAL_EDGE_ANALOGY.md) is **pedagogy**:

- bulk $\leftrightarrow\Lambda$ (smooth mean),
- edge $\leftrightarrow$ grain $\sigma$ (shear / light),
- no backscattering $\leftrightarrow$ unphysical amplification channels closed.

It is **not** a condensed-matter derivation of dark energy. I use it only as a picture, never as a proof.

---

## 7. How I would like a careful reader to judge this

1. Are documented results limited to C1–C11 and backed by `pytest`?
2. Is the DESI number used only as a bound, never to fit $\ell_{*}$?
3. Is the minimal model no more complex than $\Lambda$CDM + one $\sigma$?
4. Are free $10^{56}$ (Euclid target) / $10^{57}$ (DESI ceiling), $r\sim 64$, and $N\sim 10^{119}$ correctly rejected as **walls** — without mixing the two gap labels?
5. Are open problems (N1–N3, N8–N11) stated without hype — especially the R1 open kernel?
6. Is any $R_8$ / S$_8$ discussion limited to scale class + limits (C11 / N8)?
7. Is NP-B / $\mathrm{RMS}\sim 10^{-3}$ free of binary “discovery / model death” language (N9–N11; `NARROW_PATH` §5.1)?

---

## 8. Contact

**Jesús Morales Souhail** · jmskjym@gmail.com · ORCID 0009-0000-7637-1818
github.com/jesus-morales-souhail

