# Block-net on real peculiar velocities (Cosmicflows-4)

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)
July 2026 · data note

**Code:** [`scripts/r1/r1_real_velocity_block_net.py`](../../scripts/r1/r1_real_velocity_block_net.py)
**Results:** [`results/r1_real_velocity_net/`](../../results/r1_real_velocity_net/)
**Data (local copy):** [`data/real_velocity_net/table2.dat`](../../data/real_velocity_net/table2.dat)

---

## What this is

A concrete version of the “cast a net, split into blocks, measure means and covariances” idea — **only on real galaxy data**, with a documented public catalog.

This measures **matter** line-of-sight residual velocities relative to a pure Hubble flow.
$$
It does **not** measure dark-energy residuals, \(\Omega_\Lambda\), or a work origin for vacuum energy.
$$

---

## Data source (reliable, public)

| Item | Value |
|:-----|:------|
| Catalog | **Cosmicflows-4** |
| Paper | Tully et al. 2023, ApJ **944**, 94 |
| Archive | CDS `J/ApJ/944/94` |
| File used | `table2.dat` (galaxy sample) |
| Download | https://cdsarc.cds.unistra.fr/ftp/J/ApJ/944/94/table2.dat.gz |
| ReadMe | https://cdsarc.cds.unistra.fr/ftp/J/ApJ/944/94/ReadMe |

Columns used (from ReadMe):

- `Vcmb` — systemic velocity in the CMB frame (km/s)
- `DM`, `e_DM` — distance modulus and uncertainty (mag)
- `SGL`, `SGB` — supergalactic coordinates (deg)

---

## Definitions (fixed, not fitted)

**Distance** from distance modulus (standard):
\[
$$
d = 10^{({\rm DM}-25)/5}\quad[\mathrm{Mpc}]. \]
$$

**Line-of-sight residual velocity** (pure Hubble subtraction at fixed \(H_0\)):
\[
$$
v_{\mathrm{pec}} = V_{\mathrm{cmb}} - H_0\, d. \]
$$

$$
**\(H_0 = 75\,\mathrm{km\,s^{-1}Mpc^{-1}}\)**
$$
This is the conventional Cosmicflows residual scale for converting distance to Hubble velocity.
It is **not** fitted in this script and is **not** a claim about the true cosmic \(H_0\).

$$
**Coordinates:** supergalactic Cartesian \((x,y,z)\) from \((d,\mathrm{SGL},\mathrm{SGB})\).
$$

**Blocks:** cubes of side \(L\) Mpc; keep blocks with \(\ge 3\) galaxies.
$$
Per block: mean \(v_{\mathrm{pec}}\), internal rms, galaxy count.
$$

**Correlation:** for block means demeaned,
\[
$$
C(r)=\langle v_i v_j\rangle \]
$$
in separation bins; \(r_e\) = first separation where \(C(r)/C(0)\le 1/e\).

**Expansion comparison at block scale:**
\[
$$
v_H(L)=H_0 L,\qquad \eta(L)=\frac{\mathrm{std}(\text{block-mean }v_{\mathrm{pec}})}{v_H(L)}. \]
$$
If \(\eta>1\), block-to-block residual-velocity scatter exceeds pure Hubble across one block side (at this \(H_0\) convention).

---

## Quality cuts (stated once)

| Cut | Value |
|:----|:------|
| \(e_{\mathrm{DM}}\) | \(\le 0.5\) mag |
| Distance | \(1 < d < 200\) Mpc |
| \(\lvert V_{\mathrm{cmb}}\rvert\) | \(< 30000\) km/s |
| Galaxies per block | \(\ge 3\) |

These are standard quality / volume limits for a local CF analysis. They are not tuned to a theoretical target scale.

---

## Results (this run)

Reproduce:

```bash
python scripts/r1/r1_real_velocity_block_net.py
```

| Quantity | Value (this run) |
|:---------|:-----------------|
| \(N\) galaxies after cuts | 18011 |
| \(d\) range | 1.06 – 200 Mpc |
| Global \(\mathrm{rms}(v_{\mathrm{pec}})\) | \(\approx 1608\) km/s |
| Jackknife std of that rms (50× 90% subsamples) | \(\approx 4\) km/s |

**Block scan**

| \(L\) [Mpc] | \(N_{\mathrm{blocks}}\) | \(\sigma(v_{\mathrm{block}})\) [km/s] | \(v_H(L)=H_0 L\) | \(\eta=\sigma/v_H\) | \(r_e\) [Mpc] |
|:------------|:------------------------|:-------------------------------------|:-----------------|:-------------------|:--------------|
| 5 | 888 | 899 | 375 | 2.40 | 6.6 |
| 10 | 1878 | 1042 | 750 | 1.39 | 8.8 |
| 15 | 1821 | 1130 | 1125 | 1.00 | 10.7 |
| 20 | 1295 | 1141 | 1500 | 0.76 | 19.0 |
| 30 | 635 | 994 | 2250 | 0.44 | 30.5 |
| 40 | 360 | 1058 | 3000 | 0.35 | 39.2 |

---

## Interpretation

$$
Block-mean residual velocities relative to \(v=H_0 d\) (CF \(H_0\) convention) scatter by \(\sim 900\)–\(1100\) km/s depending on \(L\). \(\eta(L)\) falls with \(L\): at \(L\sim 5\)–\(10\,\mathrm{Mpc}\), block-mean residual scatter exceeds \(H_0 L\); at \(L\sim 30\)–\(40\,\mathrm{Mpc}\), expansion across the block wins — for this estimator and this \(H_0\). The pair scale \(r_e\) grows with block size in this simple estimator; treat it as descriptive, not a fixed constant.
$$

$$
Median \(e_{\mathrm{DM}}\approx 0.43\) mag. Roughly \(\delta d/d \sim (\ln 10/5)\,e_{\mathrm{DM}}\sim 0.2\), so distance error alone contributes of order \(H_0 d \times 0.2\) to \(v_{\mathrm{pec}}\). Global rms \(1608\) km/s mixes signal and noise; block means help but do not remove Malmquist / selection systematics (Tully+2023).
$$

$$
This is matter kinematics from published distances and redshifts. It is not a DE residual measurement, not \(\Omega_m/\Omega_\Lambda\), not an \(H_0\) solution, and \(L\) is only a scan grid (not a fit of \(\ell_*\)).
$$

$$
Method: cover CF4 volume \(d<200\,\mathrm{Mpc}\), cubic blocks of side \(L\), mean residual velocity per block, then scatter and pair correlation of block means.
$$

---

## Reproduce from scratch

```bash
mkdir -p data/real_velocity_net && cd data/real_velocity_net
curl -fsSL -o table2.dat.gz https://cdsarc.cds.unistra.fr/ftp/J/ApJ/944/94/table2.dat.gz
curl -fsSL -o ReadMe_CF4 https://cdsarc.cds.unistra.fr/ftp/J/ApJ/944/94/ReadMe
gunzip -kf table2.dat.gz
cd ../..
python scripts/r1/r1_real_velocity_block_net.py
```

---

## References

1. R. B. Tully et al., *Cosmicflows-4*, Astrophys. J. **944**, 94 (2023).
2. CDS catalog [J/ApJ/944/94](https://cdsarc.cds.unistra.fr/viz-bin/cat/J/ApJ/944/94).

