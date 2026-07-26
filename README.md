# measurable-stochastic-vacuum

**Author:** Jesús Morales Souhail · [ORCID 0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Language:** English · **Status:** Independent theory programme — **not peer reviewed** · July 2026  

When can late-time stochastic vacuum / dark-energy noise be telescope-measurable **without free \(10^{56}\) amplifiers**?

**Full document map:** [`papers/INDEX.md`](papers/INDEX.md) ← **start here if lost**

**Sister empirical corpus (DESI BAO nulls):**  
https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou

---

## Quick start

```bash
git clone https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum.git
cd measurable-stochastic-vacuum
pip install -r requirements.txt
pytest -q
```

---

## Reading paths

### A — Referee / stable claims (30 min)

1. [`papers/FOR_REFEREES.md`](papers/FOR_REFEREES.md) — claims & formula sheet  
2. [`papers/VERIFIED_RESULTS.md`](papers/VERIFIED_RESULTS.md) — unit-tested identities  
3. [`papers/OBSERVABLE_WALL.md`](papers/OBSERVABLE_WALL.md) — slip wall  
4. [`papers/SIMPLE_AS_LAMBDA.md`](papers/SIMPLE_AS_LAMBDA.md) — minimal model  
5. [`BOUNDARY.md`](BOUNDARY.md) — what this repo is not  

### B — Active research: open R1 kernel (current lead)

1. [`papers/r1-open-kernel.md`](papers/r1-open-kernel.md) — walls vs open kernel  
2. [`papers/r1-scale-decade-8-12.md`](papers/r1-scale-decade-8-12.md) — **lead: 8–12 Mpc decade**  
3. [`papers/r1-principle-nonlinear-matter.md`](papers/r1-principle-nonlinear-matter.md) — \(\ell_*=R_{\mathrm{nl}}\) hypothesis + full \(\sigma(R)\)  
4. [`papers/r1-t1-mechanisms-compute.md`](papers/r1-t1-mechanisms-compute.md) — averaging + mask numbers  
5. [`papers/r1-t12-bbks-and-derivation.md`](papers/r1-t12-bbks-and-derivation.md) — BBKS + coarse-graining sketch  
6. [`papers/r1-bounding-g-plan.md`](papers/r1-bounding-g-plan.md) — bound coupling \(\lambda,g\)  

```bash
python scripts/r1_sigma_R_full.py
python scripts/r1_t1_mechanisms_compute.py
python scripts/r1_t12_bbks_peaks.py
python scripts/r1_bound_g_oom.py
python scripts/r1_profile_lambda_bao.py
python scripts/r1_profile_lambda_fullcov.py   # full 13×13 cov; primary=working
```

### C — Closed walls (do not re-open)

| Topic | Note |
|:------|:-----|
| Soft amplification of Sorkin | sister `amplification-gap.md` |
| \(H_0\) 9% from residual / desqueezing | `h0-bridge-toy-map.md`, `h0-desqueezing-filter.md` |
| NP-A = Andromeda / Virgo / “2.01” | `ell-star-external-scales.md` |
| \(r_0 = 2.06\,\mathrm{Mpc}\) | `ell-star-r0-peculiar-scales.md` |

---

## Minimal model


$$
H^{2}=H_{0}^{2}\bigl[\Omega_{m}(1+z)^{3}+\Omega_{\Lambda}\bigr]
\qquad
\sigma=\Bigl(\frac{\ell_{*}}{L_{H}}\Bigr)^{3/2}
\qquad
\mathrm{RMS}(\lvert\gamma-1\rvert)\sim\sigma^{2/3}
$$


**Current lead:** \(\ell_*\sim R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}\) (hypothesis) \(\Rightarrow\sigma\sim 8.5\times 10^{-5}\) under DESI ceiling.

**Bulk = \(\Lambda\). Edge = \(\sigma\). Signal = light path, not a new \(H(z)\).**

---

## Status snapshot

| Layer | Status |
|:------|:-------|
| Soft amplifiers of \(\sigma_0\sim 10^{-61}\) | **Closed walls** |
| Length \(R_{\mathrm{nl}}\) | **Computed** \(\approx 8.61\,\mathrm{Mpc}\) |
| Why vacuum grain \(=R_{\mathrm{nl}}\) | **Hypothesis + sketch** (not full action) |
| Bound on \(\lambda,g\) | **Working** \(\lvert\lambda\rvert\lesssim 1.24\times 10^{-4}\), \(\lvert g\rvert\lesssim 1.45\); formal full-cov not informative at \(10^{-4}\) |
| \(H_0\) tension from residual | **Excluded** at safe amplitude |

---

## Layout

```
papers/     theory notes (see INDEX.md)
scripts/    verified kinematics + R1 pipeline
tests/      pytest gate
results/    numerical artefacts
notes/      WORK_PACKAGES live status
BOUNDARY.md claim fence vs sister repos
```

---

## Contact

**Jesús Morales Souhail** · jmskjym@gmail.com · ORCID 0009-0000-7637-1818
