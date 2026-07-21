# measurable-stochastic-vacuum

**Author:** Jesús Morales Souhail · ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Status:** Theory programme (pre-construction) · **not** a DESI detection claim  
**Date:** July 2026  

---

## What this repository is

A **fundamental-theory** programme that asks a single question:

> Under what *minimal redefinition of physical rules* could late-time vacuum / dark-energy stochasticity be **both real and telescope-measurable**, without free-lunch numerology and without self-destruction (black-hole / energy barriers)?

This is **not** a re-fit of BAO residuals. Empirical **limits and exclusions** already live in:

| Repository | Role |
|------------|------|
| [`stochastic-dark-energy-ou`](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou) | DESI claim set: $\sigma_X$ bound, model kills, $10^{56}$ bottleneck, slip starvation |
| [`stochastic-de-exploratory-notes`](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes) | Scale/operator hygiene digressions (not cosmology claims) |
| **this repo** | Theory package: which rules must change so the noise is *allowed* to be measurable |

**Read first:** [`papers/THEORY_REVOLUTION.md`](papers/THEORY_REVOLUTION.md)  
**Self-shielding law:** [`papers/SELF_SHIELDING_AXIOMS.md`](papers/SELF_SHIELDING_AXIOMS.md)  
**Work packages (live):** [`notes/WORK_PACKAGES.md`](notes/WORK_PACKAGES.md)

### Derivations delivered

| WP | Status | Document | Script |
|----|--------|----------|--------|
| **WP1 / R1** | Parcial | [`papers/r1-counting-principle.md`](papers/r1-counting-principle.md) | [`scripts/r1_counting_landscape.py`](scripts/r1_counting_landscape.py) |
| **WP2 / R3** | No-ganancia suave | [`papers/r3-open-horizon-map.md`](papers/r3-open-horizon-map.md) | [`scripts/r3_open_horizon_map.py`](scripts/r3_open_horizon_map.py) |
| **WP3 / R2** | Path + slip OOM | [`papers/r2-slip-from-same-sector.md`](papers/r2-slip-from-same-sector.md) | [`scripts/r2_light_path_accumulation.py`](scripts/r2_light_path_accumulation.py) |

```bash
python scripts/r1_counting_landscape.py
python scripts/r3_open_horizon_map.py
python scripts/r2_light_path_accumulation.py
```

---

## One-sentence thesis

A measurable stochastic dark sector is not a parameter tweak on $\Lambda$CDM; it is a **coupled triple redefinition** of (i) the counting scale of spacetime discreteness, (ii) the equivalence structure of gravity (slip), and (iii) the information-theoretic status of the cosmological horizon as an open system — and the theory must **predict its own blind spots**.

---

## Three rule changes (package, not menu)

| # | Rule broken / redefined | Physical content | Connects to old corpus |
|---|-------------------------|------------------|------------------------|
| **R1** | Local continuum / Lorentz-complete spacetime at *all* scales | Effective discrete cells with $N_{\mathrm{eff}} \ll N_{\mathrm{BH}}$ set the **seed**, not a free $A_0$ | Route 1 |
| **R2** | Strong equivalence (universal coupling of light and mass to the same potentials) | Anisotropic / sector-selective stress $\Rightarrow \gamma=\Phi/\Psi \neq 1$ as the **operator** of leakage | Option 0 / SDiff gap |
| **R3** | Global unitarity of the observable patch alone | Open-system / horizon bath dynamics can **feed** residual variance without local free lunch | Desqueezing / Act III |

**Hard rule of this programme:** R1–R3 are **not** three independent knobs. A paper that uses only one of them as a free multiplier is **out of scope** (numerology).

---

## What this programme forbids

- Multiplying $\sigma_0 \sim 10^{-61}$ by $10^{56}$ “by hand.”
- Claiming Euclid will see Sorkin noise without a derived map $\sigma_0 \to A_0$.
- Using lab optics / tesseracts as cosmological amplifiers ([exploratory fence](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes)).
- Homemade Boltzmann codes before a target amplitude is *derived* from R1+R3.
- Treating slip as a shortcut that evades the amplification problem (it does not, unless R1/R3 supply $A_0$).

---

## License

- Text: CC BY 4.0  
- Code (when added): MIT  

## Contact

**Jesús Morales Souhail** · jmskjym@gmail.com · ORCID 0009-0000-7637-1818
