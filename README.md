# measurable-stochastic-vacuum

**Author:** Jesús Morales Souhail · [ORCID 0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Language:** English · **Status:** Independent theory programme — **not peer reviewed** · July 2026  

**→ New here? Open [`START_HERE.md`](START_HERE.md) (one page).**  
**→ Full map:** [`papers/INDEX.md`](papers/INDEX.md)

When can late-time stochastic vacuum / dark-energy noise be telescope-measurable **without free \(10^{56}\) amplifiers**?

| Sister role | Repo |
|:------------|:-----|
| DESI BAO **data claims** | [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou) |
| Pedagogy / wrong-scale **quarantine** | [stochastic-de-exploratory-notes](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes) |

---

## Quick start

```bash
git clone https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum.git
cd measurable-stochastic-vacuum
pip install -r requirements.txt
pytest -q
```

---

## Layout (reorganised July 2026)

```
START_HERE.md     one-page entry
papers/
  core/           stable claims
  r1_kernel/      active lead (uniqueness of grain)
  closed_walls/   dead ends
  side_threads/   secondary
  work_packages/  WP deep dives
scripts/
  core/  r1/  closed/  side/
tests/  results/  data/
```

---

## Current scientific lead (one block)

**Bulk** expansion = \(\Lambda\).  
**Edge / residual** amplitude \(\sigma = (\ell_*/L_H)^{3/2}\).  
Under axioms (residual sector + local coupling to classical nonlinear matter):  
\(\ell_* \sim R_{\mathrm{nl}} \approx 8.61\,\mathrm{Mpc}\)  
\(\Rightarrow \sigma \sim 8.5\times 10^{-5}\) (under DESI \(\sigma_X < 1.5\times 10^{-4}\)).  
Working coupling \(\lvert g\rvert \lesssim 1.45\).  
\(H_0\) tension **not** explained at safe residual amplitude.

Short draft: [`papers/r1_kernel/NOTE_uniqueness_residual_grain.md`](papers/r1_kernel/NOTE_uniqueness_residual_grain.md)

```bash
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_sandwich_falsifiers.py
```

---

## Contact

**Jesús Morales Souhail** · jmskjym@gmail.com · ORCID 0009-0000-7637-1818
