# Work packages (orden de construcción)

Sin numerología: cada WP produce un **objeto derivado**, no un fit a DESI.

---

## WP0 — Frontera con el corpus DESI (hecho conceptualmente)

- [x] Null OU/QNM y cota $\sigma_X$  
- [x] Exclusión taquiónica rank-1  
- [x] No free lunch + rutas 1–3  
- [x] Slip amplitude-starved  
- [x] Manifiesto R1–R2–R3 (este repo)

**Output:** no repetir análisis BAO aquí; citar el otro repo.

---

## WP1 — R1: principio de contaje (semilla)

**Objetivo:** definir $N_{\mathrm{eff}}$ o $\ell_*$ **sin** usar $1.5\times 10^{-4}$.

Posibles rutas (elegir **una** y llevarla hasta el final):

| ID | Idea | Entregable |
|----|------|------------|
| R1a | Causal set con región de correlación DE $\neq$ horizonte completo | Fórmula $N_{\mathrm{eff}}(L)$ + hipótesis de contaje |
| R1b | Cutoff IR de un sector de vacío con escala $\ell_*$ de física de DE | $\sigma_{0,\mathrm{eff}}(\ell_*)$ |
| R1c | Grano de un orden de unimodular / SDiff a escala cosmológica | DOF del sector residual |

**Criterio de aceptación:** $\sigma_{0,\mathrm{eff}}$ sale de un principio; se puede falsar cambiando el principio, no el dato DESI.

**Prohibido:** “tomemos $N_{\mathrm{eff}}=10^{10}$ porque Euclid”.

---

## WP2 — R3: mapa abierto (ganancia)

**Objetivo:** master equation o análogo cosmológico con **parámetros del baño derivados** (temperatura de horizonte, tasa de escape, …).

| ID | Idea | Entregable |
|----|------|------------|
| R3a | Lindblad / desqueezing con $\gamma_{\mathrm{open}}$ ligado a $H(z)$ | Mapa $A_0(\sigma_{0,\mathrm{eff}},\gamma_{\mathrm{open}})$ |
| R3b | Residual path-integrated con $\theta(x)$ desde horizonte | $\sigma_{\mathrm{res}}(z)$ |
| R3c | Demostración de cota superior de ganancia (si no hay free lunch, **también es éxito**) | Teorema de no-ganancia |

**Criterio:** o se deriva $A_0\sim 10^{-5}$–$10^{-4}$ desde R1+R3, o se prueba que no, y el programa se cierra en “límites + geometría” sin drama.

---

## WP3 — R2: operador slip desde la misma microfísica

**Objetivo:** $\pi_T$ o $\varepsilon$ **no libre**.

| ID | Entregable |
|----|------------|
| R2a | Del mismo $X$ de R1, proyectar parte anisotrópica bajo SDiff |
| R2b | Predicción $\lvert\gamma-1\rvert(z)$ o cota |
| R2c | Comparar a posteriori con Maus / forecasts Sakr (test, no dial) |

**Criterio:** si $\varepsilon$ queda libre, el WP falla A4.

---

## WP4 — Predicciones conjuntas y ceros

**Objetivo:** una tabla única:

| Canal | Predicción | Cero estructural |
|-------|------------|------------------|
| BAO residual | … | … |
| Slip | … | … |
| Lab / pupila / tesseract | **cero** | escala/operador |

---

## WP5 — Falsación

La teoría del programa muere (o se estrecha) si:

1. Se deriva $A_0$ medible y Euclid/DESI full-cov la excluyen con el kernel **derivado** (no el OU genérico solo).  
2. El principio R1 predice $\ell_*$ en conflicto con tests locales de Lorentz **que realmente acoten ese sector**.  
3. R3 exige un baño incompatible con la historia térmica estándar sin mecanismo de desacoplo.

Falsar es éxito científico.

---

## Orden recomendado

```
WP1 (semilla) → WP2 (mapa) → WP3 (slip) → WP4 (ceros) → WP5 (tests)
```

No invertir: no hacer slip “bonito” antes de tener amplitud honesta.

---

## Archivos a crear en el futuro (cuando haya contenido)

```
papers/r1-counting-principle.md
papers/r3-open-horizon-map.md
papers/r2-slip-from-same-sector.md
papers/joint-predictions-and-zeros.md
scripts/  # solo checks de consistencia, no MCMC de DESI
```
