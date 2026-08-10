# Grain size, microscope limit, and what is still open

Jesús Morales Souhail · August 2026  
[github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)

A plain-language map of three numbers and one open question. No new derivation of $\ell_\ast$.

---

## The microscope (DESI residual)

On public DESI DR2 BAO I bound a stationary residual amplitude $\sigma_X$ with the OU kernel

$$
C_{ij}=C^{\mathrm{meas}}_{ij}+S_i S_j\,\sigma_X^{2}\,e^{-\theta\lvert\Delta x_{ij}\rvert}.
$$

Free-$\theta$ profile, 95% CL:

$$
\sigma_X < 2.5\times 10^{-2}.
$$

Best fit still goes to $\sigma_X\to 0$. In the analogy: the instrument only sees vibrations larger than about $0.025$ (in residual units). That number is **not** the baryon density $\omega_b=\Omega_b h^2\approx 0.022$. Same digits, different physics.

Sister empirical repo: [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou).

---

## The grain on the table (counting at $R_{\mathrm{nl}}$)

If the residual counting cell is the matter nonlinear scale, $d=3$,

$$
\sigma_{\mathrm{free}}=\Bigl(\frac{R_{\mathrm{nl}}}{L_H}\Bigr)^{3/2}\approx 8.5\times 10^{-5}
$$

with $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ (`r1_three_gate_lock.py`). That is about $300\times$ smaller than the DESI ceiling above. So if the grain really is $R_{\mathrm{nl}}$, the residual is invisible to the current microscope. That is **gate G1**: compatibility, not a proof of the grain size.

Three-gate also checks CF4 velocity scales (G2) and $\eta=\mathcal{O}(1)$ near $R_{\mathrm{nl}}$ (G3). All three pass under the proposal $\ell_\ast=R_{\mathrm{nl}}$. Output: `results/r1_three_gate/three_gate_lock.txt`.

---

## What is still open (R1)

Why should the rubbing piece be a sand grain ($R_{\mathrm{nl}}$) rather than a fist ($\ell_\ast\gg R_{\mathrm{nl}}$, large residual, already in tension with DESI) or a molecule ($\ell_\ast\ll R_{\mathrm{nl}}$, forever invisible)?

I have plugged $R_{\mathrm{nl}}$ into the counting formula and checked that it does not break the microscope. I have **not** derived that the cell must be that size. That missing step is stated in `r1-counting-principle.md` and `r1-principle-nonlinear-matter.md`: need a decoherence or effective-action argument that forces $\ell_\ast=R_{\mathrm{nl}}$, not a soft amplifier and not a retune to DESI.

---

## Next calculation (not a false derivation)

Do not invent a principle from chat. Hold $\ell_\ast=R_{\mathrm{nl}}$ fixed and compute consequences already in the kinematics:

1. residual amplitude $\sigma\sim 8.5\times 10^{-5}$  
2. local slip proxy and path-RMS (line-of-sight accumulation)  
3. compare OOM to published mean-slip / MG floors (Maus, Sakr), without renaming operators  

From the three-gate run with $\ell_\ast=R_{\mathrm{nl}}$ fixed:

$$
\mathrm{RMS}_{\mathrm{path}}^{\mathrm{(free)}}\approx 1.45\times 10^{-3}.
$$

Published mean-slip / MG errors sit much higher (Maus $\sigma(\gamma)\sim 0.11$; Sakr constant $\eta$ forecasts $\sim 5\%$). Operators are not the same, so this is an OOM check only: the sand-grain path signal is still well below current *mean*-slip floors. Stage-IV shear *calibration* at $\sim 10^{-3}$ must not be renamed as a measurement of this path-RMS.

```bash
python scripts/r1/r1_three_gate_lock.py
python scripts/side/lensing_rms_real_data_compare.py
```

Longer notes: `r1-sandwich-falsifiers.md`, `side_threads/lensing-rms-forecast-real-data.md`, `NEXT_QUESTION.md`.

---

## Baryons (different problem)

Feedback, WHIM, cluster gas, and kSZ can bias large-scale structure and distances. That is real work. It is **not** “whatever lives at amplitude $0.025$” because $0.025$ here is the residual ceiling $\sigma_X$, not $\omega_b$.

---

## One line

G1 says: sand grain fits under the microscope. R1 asks: why sand grain? Next: fix the grain, compute slip / path-RMS, compare honestly to published floors — then, only then, hunt a principle.
