# Beyond the OU null: the next simple question

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)

The DESI OU residual null is **closed**. This note is the hyperfocus map of what that frees.

---

## 0. Walls already measured (do not re-dig)

| Wall | Result |
|------|--------|
| Stationary OU / QNM residual on DESI DR2 α | null preferred; profile 95% CL $\sigma_X < 2.5\times 10^{-2}$ (former $1.5\times 10^{-4}$ working target corrected) |
| Rank-1 coherent tachyonic growth | excluded when active (\(\Delta\ln\mathcal{L}\sim -13\)) |
| Soft amplify pure Sorkin \(10^{-61}\) | gap \(\sim 10^{56}\); Routes 2–3 dead; Route 1 only redefines seed |
| Slip from BAO residual ceiling | at null preference still small; ceiling $2.5\times 10^{-2}$ weaker than old working target |
| Optics / tesseract / wrong scale | exploratory only |

---

## 1. The hard remaining question (load-bearing)

> What **principle** fixes a mesoscopic counting cell \(\ell_\ast\) for the DE sector
> so that \(\sigma_{0,\mathrm{eff}}=(\ell_\ast/L_H)^{d/2}\) already sits near \(10^{-5}\)–\(10^{-4}\)
> without free soft gain?

That is R1 open kernel. Not solved here.

---

## 2. The simplest *correlated* question that **can** be resolved now

Hard question (1) needs a principle.  
The **simplest linked empirical question** is only about **compatibility**:

> **If** one *proposes* \(\ell_\ast = R_{\mathrm{nl}}\) (matter nonlinear scale),  
> **does** that proposal survive three independent real-data gates at once?

| Gate | Statement | Number |
|------|-----------|--------|
| **G1** | Free grain below DESI residual ceiling | $\sigma_{\mathrm{free}}\approx 8.52\times 10^{-5} < 2.5\times 10^{-2}$ (headroom $\approx 294\times$) |
| **G2** | CF4 velocity coherence in sandwich band | \(r_e(v_{\mathrm{pec}})\approx 19.5\,\mathrm{Mpc} \in [0.5,3]R_{\mathrm{nl}}=[4.3,25.8]\,\mathrm{Mpc}\) (\(r_e/R_{\mathrm{nl}}\approx 2.26\)) |
| **G3** | At \(L\sim R_{\mathrm{nl}}\), block \(\eta=\sigma_v/(H_0 L)\) is \(\mathcal{O}(1)\) | \(\eta(L\approx R_{\mathrm{nl}})\approx 1.4\) |

**Answer (locked):** all three pass.  
Script: `scripts/r1/r1_three_gate_lock.py` → `results/r1_three_gate/`.

### What this is / is not

| Is | Is not |
|----|--------|
| A three-probe consistency lock under the *proposal* \(\ell_\ast=R_{\mathrm{nl}}\) | A derivation that \(\ell_\ast\) *must* be \(R_{\mathrm{nl}}\) |
| Correlated with R1 (same scale decade) | A DE residual detection |
| Uses DESI null as *ceiling*, CF4 as *matter scale*, sandwich as *prediction* | Multipole residual \(r_e\sim 80\)–\(120\,\mathrm{Mpc}/h\) (BAO operator; different story) |

---

## 3. Why this is the right “next” after OU null

The OU null alone only says “no residual noise needed.”  
Together with the sandwich counting identity it says something sharper:

1. DESI *allows* a free residual as large as \(\sim 10^{-4}\).  
2. Counting at \(R_{\mathrm{nl}}\) *predicts* \(\sim 8.5\times 10^{-5}\).  
3. CF4 shows matter velocity structure *lives* in that same few-Mpc decade.

So the open kernel is no longer floating: it has a **single preferred decade** and **two real-data anchors** (DESI ceiling, CF4 \(r_e\)).

The remaining work is a **principle** that picks \(R_{\mathrm{nl}}\) (or another Mpc cell) without circularity — not another soft amplifier.

G1 already says the counting amplitude sits under the DESI residual ceiling. I do not turn that into a new theorem by dividing again by \(\sqrt{2\theta}\). VLBI and \(\omega_b\) are other problems; see the sister note [scope-and-mixups.md](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou/blob/main/papers/scope-and-mixups.md).

---

## 4. Next after *this* lock (ordered)

1. ~~Bootstrap CF4 \(r_e/R_{\mathrm{nl}}\) with jackknife~~ **done** (§5; primary L=20 holds).  
2. **Path-RMS vs published slip floors** with sandwich \(\ell_\ast\) fixed (Maus/Sakr; already OOM in falsifiers).  
3. **Refuse** to retune \(\ell_\ast\) to DESI or \(S_8\) after the fact (illegal move; see open-kernel note).  
4. Only then: hunt a principle (R1a–d) that *derives* the cell.

```bash
python scripts/r1/r1_cf4_re_jackknife.py
```

---

## Reproduce

```bash
python scripts/r1/r1_three_gate_lock.py
# also prior real runs:
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_T2_real_pipeline.py
python scripts/r1/r1_real_velocity_block_net.py
```

---

---

## 5. Jackknife update (real CF4, run in-repo)

Script: `scripts/r1/r1_cf4_re_jackknife.py` → `results/r1_cf4_jackknife/`.

Spatial leave-one-region-out jackknife along SG-X (48 regions, N=18011 galaxies).

| Block side L | r_e (Mpc) | r_e / R_nl | Point in band | 1σ fully inside band |
|-------------:|----------:|-----------:|:-------------:|:--------------------:|
| 15 | 14.92 ± 0.77 | 1.73 ± 0.09 | yes | yes |
| 20 (primary) | 19.27 ± 1.14 | 2.24 ± 0.13 | yes | yes |
| 30 | 30.51 ± 2.86 | 3.54 ± 0.33 | **no** | **no** |

**G2 after errors:** holds at the primary L=20 Mpc scale used in T2/three-gate.

**Honest edge:** at L=30 Mpc the measured r_e leaves the sandwich band — the gate is scale-dependent by construction of the block filter, not a free retune of R_nl.

