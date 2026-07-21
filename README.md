# measurable-stochastic-vacuum

**Author:** Jesús Morales Souhail · ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Status:** Theory programme with a **verified core** + open research questions  
**Date:** July 2026  

---

## Start here (publication spine)

| Document | Role |
|:---------|:-----|
| **[`papers/VERIFIED_RESULTS.md`](papers/VERIFIED_RESULTS.md)** | **Only hard claims** — counting, soft gain, slip+path; all covered by tests |
| [`tests/test_verified.py`](tests/test_verified.py) | Automated verification (`pytest -q`) |
| [`scripts/lib_verified.py`](scripts/lib_verified.py) | Library of verified identities |

```bash
pip install -r requirements.txt
pytest -q
```

**Sister empirical corpus (DESI bounds, not re-derived here):**  
https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou

---

## What is verified (one paragraph)

Under a counting hypothesis $N_{\mathrm{eff}}=(L/\ell_*)^d$, the seed is $\sigma_{0,\mathrm{eff}}=(\ell_*/L)^{d/2}$. The holographic Sorkin case is $\sigma_0\sim 10^{-61}$. Soft open gain $e^{2r}$ with $r=\mathcal{O}(1)$ is only $\mathcal{O}(10)$ and cannot lift Sorkin to $10^{-5}$ ($r\sim 64$ would be required). Sub-horizon anisotropic stress gives $|\gamma-1|=2\varepsilon\sigma(\rho_X/\rho_m)/|\delta_m|$; incoherent light-path accumulation multiplies by $\sqrt{\chi/\ell_*}=\mathcal{O}(10$–$10^{2})$ for Mpc cells on Gpc paths—not $10^{56}$. Measurability therefore requires a **mesoscopic counting cell** (principle still open) or a **derived** hard open map (not constructed).

---

## What is programme narrative (not yet verified physics)

| Document | Role |
|:---------|:-----|
| [`papers/THEORY_REVOLUTION.md`](papers/THEORY_REVOLUTION.md) | Manifesto R1–R2–R3 |
| [`papers/SELF_SHIELDING_AXIOMS.md`](papers/SELF_SHIELDING_AXIOMS.md) | Method axioms A0–A8 |
| [`notes/WORK_PACKAGES.md`](notes/WORK_PACKAGES.md) | Live WP status |
| WP1–WP3 notes (`r1-…`, `r3-…`, `r2-…`) | Expanded derivations / discussion; **cite VERIFIED_RESULTS for hard claims** |

### Open (explicitly not claimed)

- Principle fixing galactic $\ell_*$ (R1a/b/c)  
- Horizon bath with $r\sim 64$  
- $\varepsilon$ from SDiff symmetry  
- Detection forecasts as certainties  

---

## Demo scripts (use verified library logic)

```bash
python scripts/r1_counting_landscape.py
python scripts/r3_open_horizon_map.py
python scripts/r2_light_path_accumulation.py
python scripts/lib_verified.py
```

---

## Repository map

```
papers/VERIFIED_RESULTS.md   ← cite this
scripts/lib_verified.py      ← identities
tests/test_verified.py       ← must stay green
papers/r1,r2,r3-*.md         ← WP discussion
papers/THEORY_REVOLUTION.md  ← programme only
```

---

## License

Code MIT · Author text CC BY 4.0  

## Contact

**Jesús Morales Souhail** · jmskjym@gmail.com
