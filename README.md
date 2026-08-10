# measurable-stochastic-vacuum

Jesús Morales Souhail  
[ORCID 0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818) · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)  
July 2026 · independent work

Theory notes and small scripts. The question is simple to state and hard to finish:

Can a late-time residual in dark energy (or the vacuum) be large enough for surveys to care about, without inventing free amplification factors of order \(10^{56}\) from a Planck-scale seed?

The data side lives in [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou).  
Exploratory method notes only: [stochastic-de-exploratory-notes](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes).

---

## Read first

1. [`papers/what-i-would-put-in-a-paper.md`](papers/what-i-would-put-in-a-paper.md) — short-paper outline  
2. [`papers/r1_kernel/NOTE_uniqueness_residual_grain.md`](papers/r1_kernel/NOTE_uniqueness_residual_grain.md) — main residual-scale argument  
3. [`papers/r1_kernel/NEXT_QUESTION.md`](papers/r1_kernel/NEXT_QUESTION.md) — three-gate and what is still open  
4. [`papers/core/VERIFIED_RESULTS.md`](papers/core/VERIFIED_RESULTS.md) — identities checked by tests  
5. [`BOUNDARY.md`](BOUNDARY.md) — what does not belong here  
6. [`papers/INDEX.md`](papers/INDEX.md) — full list of notes  

---

## Where the work sits

Mean expansion: flat \(\Lambda\)CDM.  
Residual amplitude under counting: \(\sigma=(\ell_{\ast}/L_H)^{3/2}\).

If free residual modes couple locally to classical nonlinear matter, the natural cell is the matter nonlinear scale \(R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}\). That gives \(\sigma\sim 8.5\times 10^{-5}\), under the DESI residual ceiling \(\sigma_X<2.5\times 10^{-2}\) (95% CL) from the related analysis. A dimensionless coupling of order one is then allowed. The same residual is far too small to fix the \(\sim 8\%\) Hubble tension — I checked that on purpose.

On public Cosmicflows-4 I also looked at local **matter** kinematics (block residual velocities and collapse-peak relief). That is context near \(R_{\mathrm{nl}}\). It is **not** a dark-energy residual map.

```bash
pip install -r requirements.txt
pytest -q
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_three_gate_lock.py
python scripts/r1/r1_T2_real_pipeline.py
python scripts/r1/r1_real_velocity_block_net.py
```

---

## Folders

```
papers/core/          stable notes
papers/r1_kernel/     residual scale, coupling, CF4 kinematics
papers/closed_walls/  routes already closed with numbers
papers/side_threads/  digressions
papers/work_packages/ longer notes
scripts/  tests/  results/  data/
```

Contact: jmskjym@gmail.com
