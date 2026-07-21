# measurable-stochastic-vacuum

**Author:** Jesús Morales Souhail · ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Language:** English  
**Status:** Theory programme with a **verified, test-gated core**  
**Date:** July 2026  

Independent research on *when* late-time stochastic vacuum / dark-energy noise could be telescope-measurable **without free-lunch numerology**.

---

## 1. Start here

| Priority | Document | Role |
|:---------|:---------|:-----|
| **1** | [`papers/VERIFIED_RESULTS.md`](papers/VERIFIED_RESULTS.md) | **Publication spine — hard claims only** |
| **2** | [`papers/NARROW_PATH.md`](papers/NARROW_PATH.md) | Only soft-regime coherent architecture (NP-A / NP-B) |
| **3** | [`tests/test_verified.py`](tests/test_verified.py) | Gate: `pytest -q` (31 tests) |
| 4 | [`scripts/lib_verified.py`](scripts/lib_verified.py) | Verified identities library |
| 5 | [`papers/wp4-joint-predictions-and-zeros.md`](papers/wp4-joint-predictions-and-zeros.md) | Joint table + structural zeros |
| 6 | [`papers/wp5-falsification.md`](papers/wp5-falsification.md) | Falsification criteria |

```bash
git clone https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum.git
cd measurable-stochastic-vacuum
pip install -r requirements.txt
pytest -q
```

---

## 2. Verified core (one paragraph)

Under $N_{\mathrm{eff}}=(L/\ell_*)^d$, the seed is $\sigma_{0,\mathrm{eff}}=(\ell_*/L)^{d/2}$. Holographic Sorkin counting gives $\sigma_0\sim 10^{-61}$. Soft open gain $e^{2r}$ with $r=\mathcal{O}(1)$ is only $\mathcal{O}(10)$ and cannot lift Sorkin to $10^{-5}$ (that would need $r\sim 64$). Sub-horizon anisotropic stress yields $|\gamma-1|=2\varepsilon\sigma(\rho_X/\rho_m)/|\delta_m|$; incoherent light-path accumulation multiplies by $\sqrt{\chi/\ell_*}=\mathcal{O}(10$–$10^{2})$ for Mpc cells on Gpc paths—not $10^{56}$. **Measurability requires a mesoscopic counting cell (principle still open) or a derived hard open map (not constructed).**

---

## 3. Document map

### 3.1 Hard / verified

| Path | Content |
|:-----|:--------|
| `papers/VERIFIED_RESULTS.md` | Counting, soft gain, slip + path |
| `scripts/lib_verified.py` | Implementation |
| `tests/test_verified.py` | Automated checks |
| `papers/wp4-joint-predictions-and-zeros.md` | Joint predictions |
| `papers/wp5-falsification.md` | Falsification criteria |

### 3.2 Programme (narrative)

| Path | Content |
|:-----|:--------|
| `papers/THEORY_REVOLUTION.md` | R1–R2–R3 manifesto |
| `papers/SELF_SHIELDING_AXIOMS.md` | Axioms A0–A8 |
| `notes/WORK_PACKAGES.md` | Live WP status |
| `BOUNDARY.md` | Sister-repo fence |

### 3.3 Work-package discussions

| Path | Rule |
|:-----|:-----|
| `papers/r1-counting-principle.md` | R1 landscape |
| `papers/r3-open-horizon-map.md` | R3 soft map |
| `papers/r2-slip-from-same-sector.md` | R2 light path |

### 3.4 Demo scripts

```bash
python scripts/lib_verified.py
python scripts/r1_counting_landscape.py
python scripts/r3_open_horizon_map.py
python scripts/r2_light_path_accumulation.py
```

---

## 4. Explicit non-claims

- No derivation yet of galactic $\ell_*$  
- No horizon bath with $r\sim 64$  
- No first-principles $\varepsilon$  
- No detection claim  
- Not peer reviewed  

---

## 5. Sister repositories

| Repo | Role |
|:-----|:-----|
| [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou) | DESI empirical claims |
| [stochastic-de-exploratory-notes](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes) | Wrong-scale pedagogy |

---

## 6. License and contact

- Code: MIT  
- Author text: CC BY 4.0  

**Jesús Morales Souhail** · jmskjym@gmail.com · ORCID 0009-0000-7637-1818
