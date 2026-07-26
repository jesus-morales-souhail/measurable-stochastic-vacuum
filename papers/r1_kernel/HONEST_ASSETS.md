# What is public data and what is mine

Jesús Morales Souhail · July 2026  
[github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)

---

## Public material I use

- DESI DR2 BAO means and covariances (sister repo): collaboration releases / Zenodo.  
- $\sigma_8$, $\Omega_m$, $n_s$, $h$: standard Planck-class values.  
- Buchert, slip, Stage-IV forecasts: literature.  
- **Cosmicflows-4** (Tully et al. 2023, ApJ 944, 94), CDS `J/ApJ/944/94`.  
  Local files: `data/real_velocity_net/table2.dat`, `table4.dat`, ReadMe.

I do not have private DESI spectra or private CF4 reductions.

---

## What I built on top of that

1. Sister repo: residual analysis under an OU/QNM kernel, $\sigma_X<1.5\times 10^{-4}$ (95% CL), soft-amplification gap for a pure Sorkin seed.  
2. Check that this residual does not explain $\sim 8\%\,H_0$ at DESI-safe amplitude.  
3. Conditional uniqueness $\ell_{\ast}\sim R_{\mathrm{nl}}$ under axioms A0–A4.  
4. $R_{\mathrm{nl}}$, mask correlation, packing, BBKS peak scale.  
5. $g_{\mathrm{eff}}$ order-of-magnitude from a Gaussian averaging proxy (compared afterwards to DESI).  
6. Residual–structure protocol and a synthetic mock of the estimators.  
7. CF4 block-net and collapse-relief scripts (matter $v_{\mathrm{pec}}$; not DE residual).  
8. Unit tests for the kinematic identities.

---

## Citation

Independent research on public catalogs and public BAO products.  
No privileged data access. No residual detection claimed.  
CF4: published distances and redshifts; block and peak definitions are mine and are written in the notes.
