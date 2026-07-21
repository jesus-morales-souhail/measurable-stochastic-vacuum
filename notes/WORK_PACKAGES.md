# Work packages (estado vivo)

Sin numerología: cada WP produce un **objeto derivado**, no un fit a DESI.

**Última actualización:** julio 2026 (WP1 parcial entregado; WP2 abierto)

---

## WP0 — Frontera con el corpus DESI

| | |
|:--|:--|
| **Estado** | **Hecho** (repo hermano) |
| **Output** | null OU/QNM, $\sigma_X < 1.5\times 10^{-4}$, exclusión taquiónica, no free lunch, slip starved |

No se repite análisis BAO aquí; se **cita**.

---

## WP1 — R1: principio de contaje (semilla)

| | |
|:--|:--|
| **Estado** | **Parcial / acotado** |
| **Entregado** | [`papers/r1-counting-principle.md`](../papers/r1-counting-principle.md) · [`scripts/r1_counting_landscape.py`](../scripts/r1_counting_landscape.py) |

### Qué está derivado

$$
\sigma_{0,\mathrm{eff}} = N_{\mathrm{eff}}^{-1/2} = (\ell_*/L)^{d/2}
$$

| Resultado | Valor |
|:----------|:------|
| Sorkin ($d=2$, $\ell_*=L_P$) | $\sigma_0 \sim 1.2\times 10^{-61}$ — **cero estructural** |
| Celda para $\sigma\sim 10^{-5}$, $d=2$ | $\ell_* \approx 0.04\,\mathrm{Mpc}$ |
| Celda para $\sigma\sim 10^{-5}$, $d=3$ | $\ell_* \approx 2.1\,\mathrm{Mpc}$ |
| Celda para $\sigma\sim 10^{-5}$, $d=4$ | $\ell_* \approx 14\,\mathrm{Mpc}$ |
| Ceros A6 | Planck-cell null; $\ell_*=L_H$ absurdo; operador óptico null |

### Qué **no** está cerrado (kernel abierto)

| Candidato | Pregunta abierta |
|:----------|:-----------------|
| R1a causal set local | ¿Qué fija $\ell_*$ del sector DE? |
| R1b cutoff IR de vacío | ¿De qué acción sale $\ell_*$? |
| R1c grano SDiff/unimodular | ¿Por qué $\ell_*$ galáctico y no $L_P$? |

**Estado R1 en tabla A4:** semilla **derivada como paisaje**; principio que fija $\ell_*$ = **ausente (declarado)**.

DESI se usa solo a posteriori (A5): no se eligió $\ell_*$ para entrar en $1.5\times 10^{-4}$.

---

## WP2 — R3: mapa abierto (ganancia)

| | |
|:--|:--|
| **Estado** | **En curso** |
| **Entregable** | [`papers/r3-open-horizon-map.md`](../papers/r3-open-horizon-map.md) · [`scripts/r3_open_horizon_map.py`](../scripts/r3_open_horizon_map.py) |
| **Input** | $\sigma_{0,\mathrm{eff}}$ de WP1 (no dial) |

**Objetivo:** master / residual path con mapa $\gamma_{\mathrm{open}}\leftrightarrow \theta H(z)$ **o** teorema de no-ganancia.

Criterio de aceptación: o $A_0$ en banda telescópica desde R1+R3, o cota de ganancia que cierre el free lunch de forma definitiva en el paquete abierto.

---

## WP3 — R2: slip desde la misma microfísica

| | |
|:--|:--|
| **Estado** | Pendiente (después de WP2) |
| **Entregable** | `papers/r2-slip-from-same-sector.md` |

$\varepsilon$ / $\pi_T$ no libres. Predicción $\lvert\gamma-1\rvert$ o cota.

---

## WP4 — Predicciones conjuntas y ceros

Pendiente. Tabla única BAO / slip / ceros de laboratorio.

---

## WP5 — Falsación

Pendiente. Criterios de muerte del paquete R1–R3.

---

## Orden

```
WP0 ✓ → WP1 parcial ✓ → WP2 (ahora) → WP3 → WP4 → WP5
         └── R1a/b/c (principio de ℓ_*) en paralelo si hay candidato
```
