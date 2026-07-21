# measurable-stochastic-vacuum

**Author:** Jesús Morales Souhail · [ORCID 0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818) 
**Language:** English 
**Status:** Independent theory programme — **not peer reviewed** · July 2026 

When can late-time stochastic vacuum / dark-energy noise be telescope-measurable **without free-amplification ad hoc free-parameter tuning**?

---

## Reading guide (start here)

| Priority | Document | Role |
|:---------|:---------|:-----|
| **1** | [`papers/FOR_REFEREES.md`](papers/FOR_REFEREES.md) | Statement of results, formula sheet, C1–C9 / N1–N7 |
| **2** | [`papers/OBSERVABLE_WALL.md`](papers/OBSERVABLE_WALL.md) | **Einstein+Morales wall + self-shielding** |
| **2b** | [`papers/PAST_LIGHT_CONE_INTEGRATION.md`](papers/PAST_LIGHT_CONE_INTEGRATION.md) | **Past light-cone $\mathrm{RMS}$ atlas (only natural amplifier)** |
| **3** | [`papers/SIMPLE_AS_LAMBDA.md`](papers/SIMPLE_AS_LAMBDA.md) | Minimal model (as simple as $\Lambda$) |
| **4** | [`papers/VERIFIED_RESULTS.md`](papers/VERIFIED_RESULTS.md) | Documented results only (unit-tested) |
| **5** | [`papers/NARROW_PATH.md`](papers/NARROW_PATH.md) | DESI-safe windows NP-A / NP-B |
| **5b** | [`papers/r1-open-kernel.md`](papers/r1-open-kernel.md) | **Walls vs open kernel** (R1 load-bearing gap) |
| **6** | [`papers/TOPOLOGICAL_EDGE_ANALOGY.md`](papers/TOPOLOGICAL_EDGE_ANALOGY.md) | Optional bulk/edge analogy |

```bash
git clone https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum.git
cd measurable-stochastic-vacuum
pip install -r requirements.txt
pytest -q # expect: 49 passed
python scripts/simple_as_lambda.py
python scripts/r1_open_kernel_scales.py
```

**Sister empirical corpus (DESI bounds):** 
https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou

---

## Minimal model (simplified presentation)


$$
H^{2}=H_{0}^{2}\bigl[\Omega_{m}(1+z)^{3}+\Omega_{\Lambda}\bigr] \quad\text{(keep $\Lambda$CDM)}
$$



$$
\sigma=\Bigl(\frac{\ell_{*}}{L_{H}}\Bigr)^{3/2} \quad\text{(one grain parameter)}
$$



$$
\mathrm{RMS}(\lvert\gamma-1\rvert)\sim\sigma^{2/3} \quad\text{(one light-path prediction)}
$$


with a posteriori bound $\sigma_{\mathrm{res}}\le 1.5\times 10^{-4}$ from DESI residual analysis.

**Bulk = $\Lambda$ (smooth mean). Edge = $\sigma$ (mesoscopic grain). Signal = light, not a new $H(z)$.**

---

## Verified core (one paragraph)

Under $N_{\mathrm{eff}}=(L/\ell_{*})^{d}$, $\sigma_{0,\mathrm{eff}}=(\ell_{*}/L)^{d/2}$. Holographic Sorkin counting yields $\sigma_{0}\sim 10^{-61}$. Soft open gain $e^{2r}$ with $r=\mathcal{O}(1)$ is only $\mathcal{O}(10)$ and cannot lift Sorkin to $10^{-5}$ (that requires $r\sim 64$). Sub-horizon anisotropic stress gives $\lvert\gamma-1\rvert=2\varepsilon\sigma(\rho_{X}/\rho_{m})/\lvert\delta_{m}\rvert$; incoherent path accumulation multiplies by $\sqrt{\chi/\ell_{*}}=\mathcal{O}(10$–$10^{2})$ for Mpc cells on Gpc paths—not $10^{56}$. **Measurability requires a mesoscopic counting cell (principle still open — see [`r1-open-kernel.md`](papers/r1-open-kernel.md)) or a derived hard open map (not constructed).** Soft amplifiers of a Planck seed are **measured walls**, not open questions of the same type.

---

## Document map

### Quantitative results

| Path | Content |
|:-----|:--------|
| `papers/FOR_REFEREES.md` | Referee package |
| `papers/VERIFIED_RESULTS.md` | Counting, soft gain, slip + path |
| `papers/SIMPLE_AS_LAMBDA.md` | $\Lambda$-simple reduction |
| `papers/NARROW_PATH.md` | NP-A / NP-B architecture |
| `papers/r1-open-kernel.md` | Walls vs open kernel; R1d scale class |
| `scripts/lib_verified.py` | Implementation |
| `scripts/r1_open_kernel_scales.py` | $R_8$ / landscape scale table |
| `tests/test_verified.py` | automated checks (`pytest -q`) |

### Optional / narrative

| Path | Content |
|:-----|:--------|
| `papers/TOPOLOGICAL_EDGE_ANALOGY.md` | Hall/Laughlin bulk–edge analogy |
| `papers/THEORY_REVOLUTION.md` | R1–R2–R3 manifesto |
| `papers/SELF_SHIELDING_AXIOMS.md` | Method axioms |
| `papers/r1-*.md`, `r2-*.md`, `r3-*.md`, `wp4-*`, `wp5-*` | WP discussion |
| `notes/WORK_PACKAGES.md` | Live status |
| `BOUNDARY.md` | Sister-repo fence |

### Demo scripts

```bash
python scripts/lib_verified.py
python scripts/simple_as_lambda.py
python scripts/light_cone_atlas.py # CSV + use with figures/
python scripts/r1_counting_landscape.py
python scripts/r3_open_horizon_map.py
python scripts/r2_light_path_accumulation.py
```

**Figure:** [`figures/past_light_cone_rms.png`](figures/past_light_cone_rms.png)

---

## Explicit non-claims

- No derivation of galactic $\ell_{*}$ 
- No horizon bath with $r\sim 64$ 
- No first-principles $\varepsilon$ 
- No detection claim 
- Cosmos is not a Hall bar (analogy only) 
- Cosmic entropy does not “stop” 
- Not peer reviewed 

---

## Sister repositories

| Repo | Role |
|:-----|:-----|
| [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou) | DESI empirical claims + preprint |
| [stochastic-de-exploratory-notes](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes) | Wrong-scale pedagogy only |

---

## License and contact

- Code: MIT 
- Author text: CC BY 4.0 

**Jesús Morales Souhail** · jmskjym@gmail.com · ORCID 0009-0000-7637-1818
