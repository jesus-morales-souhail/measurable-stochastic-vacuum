# measurable-stochastic-vacuum

Jesús Morales Souhail
[ORCID 0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818) · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)
July 2026 · independent work

I keep theory notes and small scripts here. The question is simple to state and hard to finish:

Can a late-time residual in dark energy (or the vacuum) be large enough for surveys to care about, without inventing free amplification factors of order $10^{56}$ from a Planck-scale seed?

I do the data side in a related repository. This one is the map of what is closed, what is still open, and the numbers that do not move when you re-run the tests.

| | |
|:--|:--|
| [`START_HERE.md`](START_HERE.md) | how to read the folder |
| [`papers/what-i-would-put-in-a-paper.md`](papers/what-i-would-put-in-a-paper.md) | outline for a short paper |
| [`papers/INDEX.md`](papers/INDEX.md) | list of notes |
| [`BOUNDARY.md`](BOUNDARY.md) | claims that are out of scope |

Related repositories: [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou) (DESI data), [stochastic-de-exploratory-notes](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes) (exploratory only).

---

## Setup

```bash
git clone https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum.git
cd measurable-stochastic-vacuum
pip install -r requirements.txt
pytest -q
```

If `pytest` is green, the algebraic identities I rely on still hold.

---

## Layout

```
papers/core/ stable notes
papers/r1_kernel/ residual scale, coupling, CF4 kinematics
papers/closed_walls/ routes I already killed with numbers
papers/side_threads/ digressions
papers/work_packages/ longer notes
scripts/core|r1|closed|side
tests/ results/ data/
```

---

## Where the work sits right now

Mean expansion: flat $\Lambda$CDM.
Residual amplitude under counting: $\sigma=(\ell_{\ast}/L_H)^{3/2}$.

If free residual modes couple locally to classical nonlinear matter, the natural cell is the matter nonlinear scale $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$. That gives $\sigma\sim 8.5\times 10^{-5}$, under the DESI residual ceiling $\sigma_X<1.5\times 10^{-4}$ (95% CL) from the related analysis. A dimensionless coupling of order one is then allowed. The same residual is far too small to fix the $\sim 8\%$ Hubble tension — I checked that and closed it on purpose.

On public Cosmicflows-4 I also looked at local **matter** kinematics (block residual velocities and collapse-peak relief). That is context for gravity vs expansion near $R_{\mathrm{nl}}$. It is **not** a dark-energy residual map.

Main write-up: [`papers/r1_kernel/NOTE_uniqueness_residual_grain.md`](papers/r1_kernel/NOTE_uniqueness_residual_grain.md).

```bash
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_T2_mock_pipeline.py
python scripts/r1/r1_real_velocity_block_net.py
python scripts/r1/r1_collapse_relief_cf4.py
```

---

## Contact

jmskjym@gmail.com
