# measurable-stochastic-vacuum

**Author:** Jesús Morales Souhail · [ORCID 0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Status:** Independent research · July 2026 · not peer reviewed

Theory notes and reproducible scripts on whether a late-time residual in the dark-energy or vacuum sector can reach survey sensitivity without free soft amplification of a Planck-scale seed.

| Document | Purpose |
|:---------|:--------|
| [`START_HERE.md`](START_HERE.md) | Entry guide |
| [`papers/INDEX.md`](papers/INDEX.md) | Full document map |
| [`BOUNDARY.md`](BOUNDARY.md) | Claim boundaries |

**Related work**

- Empirical DESI BAO residual analysis: [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou)  
- Exploratory / pedagogical material: [stochastic-de-exploratory-notes](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes)

---

## Installation

```bash
git clone https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum.git
cd measurable-stochastic-vacuum
pip install -r requirements.txt
pytest -q
```

---

## Repository structure

```
papers/core/           stable claims and formulae
papers/r1_kernel/      residual scale, coupling, survey tests
papers/closed_walls/   mechanisms already excluded
papers/side_threads/   secondary topics
papers/work_packages/  longer work-package notes
scripts/core|r1|closed|side
tests/  results/  data/
```

---

## Working picture

Mean expansion is taken to be flat \(\Lambda\)CDM. A residual amplitude is written, under a counting hypothesis,
\[
\sigma=\Bigl(\frac{\ell_*}{L_H}\Bigr)^{3/2}.
\]
If free residual degrees of freedom couple locally to classical nonlinear matter, the counting scale is identified with the matter nonlinear scale \(R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}\), giving \(\sigma\sim 8.5\times 10^{-5}\), consistent with the companion DESI residual ceiling \(\sigma_X<1.5\times 10^{-4}\) (95% CL). A dimensionless coupling of order unity is then compatible with that ceiling. The same residual amplitude is far too small to account for the \(\sim 8\%\) Hubble tension.

Main draft: [`papers/r1_kernel/NOTE_uniqueness_residual_grain.md`](papers/r1_kernel/NOTE_uniqueness_residual_grain.md).

```bash
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_T2_mock_pipeline.py
```

---

## Contact

Jesús Morales Souhail · jmskjym@gmail.com · ORCID 0009-0000-7637-1818
