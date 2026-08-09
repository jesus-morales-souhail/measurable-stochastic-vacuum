# Line A: effective $g$ from averaging residual (not from DESI dial)

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail) · July 2026

*Derivation sketch and OOM path. Not a finished Buchert MCMC.*

Parent: [`FRONTIER_INQUIRY.md`](FRONTIER_INQUIRY.md) · [`r1-a1-microphysics.md`](r1-a1-microphysics.md)

---

## Goal

I want to replace “$g$ is free until DESI bounds it” with something better:

> Estimate $g_{\mathrm{eff}}$ from residual variance of averaged Einstein equations on domain $L_{\mathrm{av}}=R_{\mathrm{nl}}$, then compare a posteriori to $\lvert g\rvert\lesssim 1.45$.

---

## 1. What is derived vs postulated

| Step | Status |
|:-----|:-------|
| Domain $L_{\mathrm{av}}:=R_{\mathrm{nl}}$ from $\sigma(R)=1$ | Geometry (done) |
| Averaging produces effective sources $Q$, $\langle\mathcal{R}\rangle$, … | Standard Buchert structure |
| Mean $Q$ explains cosmic acceleration | Not claimed (contested; out of scope) |
| Fluctuations $\delta Q$ about the average act as residual $\chi$ | Postulate M1 (programme) |
| Map $\delta Q\to g_{\mathrm{eff}}$ | This note’s OOM path |

---

## 2. OOM map $\delta Q \to g_{\mathrm{eff}}$

Buchert kinematical backreaction (schematic):


Q=\tfrac{2}{3}\bigl(\langle\theta^2\rangle-\langle\theta\rangle^2\bigr)-2\langle\sigma^2\rangle


on domain $D$ of size $L_{\mathrm{av}}$.

At the onset of nonlinearity, expansion and shear fluctuations are set by the density field with $\sigma_\delta(R_{\mathrm{nl}})=1$. OOM:


\frac{\sqrt{\mathrm{Var}(Q)}}{H^2} \sim \mathcal{O}(1)\times \sigma_\delta^2 \sim \mathcal{O}(1) \quad\text{on a single nonlinear domain.}


After coarse-graining over $N=(L_H/R_{\mathrm{nl}})^3$ domains, the Hubble-volume residual of a dimensionless averaged source is


\sigma_Q \sim \frac{\mathcal{O}(1)}{\sqrt{N}} =\mathcal{O}(1)\times\Bigl(\frac{R_{\mathrm{nl}}}{L_H}\Bigr)^{3/2} \sim \mathcal{O}(\sigma_{\mathrm{free}}) \sim 10^{-4}.


I identify residual contrast with programme $\chi$ (normalised so free RMS $=\sigma_{\mathrm{free}}$):


\chi \sim \frac{\delta Q/H^2}{\sigma_Q}\cdot\sigma_{\mathrm{free}} \quad\Rightarrow\quad \text{order-unity field in patch units.}


Coupling to matter: on the same domain, $\delta_m\sim\mathcal{O}(1)$. The induced residual response


\lambda \sim \frac{\partial(\delta\rho_X/\rho_X)}{\partial\delta_m} \sim \frac{\sigma_Q}{\sigma_\delta} \sim \sigma_{\mathrm{free}} \quad(\sigma_\delta=1)


gives, under $\lambda=g\sigma_{\mathrm{free}}$,


\boxed{g_{\mathrm{eff}}\sim\mathcal{O}(1)}.


Averaging residual naturally lands $g_{\mathrm{eff}}$ at the same order as the DESI working bound $\lvert g\rvert\lesssim 1.45$ — without dialing $g$ to DESI first. DESI then becomes an a posteriori consistency check, not the definition of $g$.

---

## 3. Limits

- Not a proof that Buchert $Q$ is dark energy.
- Not a full relativistic gauge-fixed variance calculation (needs dedicated numerics / constrained realisations).
- Not a licence to raise $\sigma$ to 8% for $H_0$.

---

## 4. Executed: Gaussian proxy numerics

```bash
python scripts/r1/r1_lineA_Q_variance_proxy.py
```

Map used: $g_{\mathrm{eff}}=\mathrm{rms}(q)$ on one $R_{\mathrm{nl}}$ domain with $q\sim Q/H^2$, $\delta\sim\mathcal{N}(0,1)$, $\lambda_{\mathrm{eff}}=g_{\mathrm{eff}}\sigma_{\mathrm{free}}$.

| Proxy | Definition | $g_{\mathrm{eff}}$ (MC / analytic) |
|:------|:-----------|:-------------------------------------|
| P0 | $q=\delta^2-1$ | $\sqrt{2}\approx 1.41$ |
| P1 (primary) | $q=\tfrac{2}{3}f^2(\delta^2-1)$, $f=\Omega_m^{0.55}$ | $\approx 0.48$ |
| P2 | $\alpha(\delta^2-1)+\beta\delta^3$ | $\mathcal{O}(1)$ |
| Sub-cell var | sample var of $n_{\mathrm{sub}}$ cells | $\mathcal{O}(1)$ |

A posteriori vs DESI working $\lvert g\rvert\lesssim 1.45$: all proxies are same order (factor $\sim 0.3$–$1$). DESI is consistency, not the definition of $g$.

Artefact: `results/r1_lineA_Q/`.

Still open for upgrade: true $\mathrm{Var}(Q)$ from N-body / constrained realisations (full Buchert on domains).

---

## 5. Parallel SDiff edge estimate

Volume fraction of edges $f\sim 0.16$($\delta>1$). If residual anisotropic stress lives only on edges,


\sigma_{\mathrm{edge}}\sim \sigma_{\mathrm{free}}/\sqrt{f}


or support-weighted $\sigma\sim\sigma_{\mathrm{free}}\sqrt{f}$ depending on normalisation — both stay $\mathcal{O}(10^{-4})$. Mapping to $g$ via slip wall again yields $\lvert g\rvert\sim\mathcal{O}(1)$ if $\varepsilon\sim\mathcal{O}(1)$.

---

## 6. Summary

| ID | Claim | Status |
|:---|:------|:-------|
| GA1 | $g_{\mathrm{eff}}\sim\mathcal{O}(1)$ from averaging residual OOM | sketch |
| GA2 | Gaussian proxy: $g_{\mathrm{eff}}\approx 0.5$–$1.4$(P1–P0) | executed |
| GA3 | Matches DESI working bound order | consistency |
| GA4 | Full $Q$ variance from N-body | open |

