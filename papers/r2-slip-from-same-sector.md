# WP3 — R2: del ruido estocástico al estrés anisotrópico y a la luz

**Autor:** Jesús Morales Souhail · ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Programa:** measurable-stochastic-vacuum  
**Estado:** Derivación WP3 · no es detección  
**Fecha:** julio 2026  
**Código:** [`scripts/r2_light_path_accumulation.py`](../scripts/r2_light_path_accumulation.py)  
**Salida numérica:** [`results/r2_light_path.txt`](../results/r2_light_path.txt)  
**Inputs:** WP1 ([`r1-counting-principle.md`](r1-counting-principle.md)), WP2 ([`r3-open-horizon-map.md`](r3-open-horizon-map.md))  
**Puente empírico:** Option 0 + `slip_bridge.py` en [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou)  

---

## 1. La idea física (la que hay que tomar en serio)

Una fluctuación **clásica** de densidad y presión en el sector de energía oscura **no tiene por qué** modificar el ritmo global $H(z)$ (difícil de ver en BAO residual isótropo). Le basta generar **estrés anisotrópico** $\pi_T$ (parte sin traza del tensor de energía-momento).

Eso significa:

1. El ruido **no** empuja el espacio por igual en todas direcciones.  
2. Crea **arrugas** en los potenciales newtonianos $\Phi$, $\Psi$.  
3. La luz de galaxias lejanas cruza esas arrugas: se curva (lente) y acumula desplazamiento (ISW / Sachs–Wolfe integrado).  
4. El telescopio **no** mide el vacío “a pelo”: mide la **distorsión acumulada** a lo largo de Gpc de camino.

Esta es la **opción de operador correcta** (R2 / Option 0): el canal de la grieta SDiff es el shear, no un wiggle isótropo en $D_V$.

---

## 2. Lo que esta idea **no** concede (anti-free-lunch)

Es tentador decir: “un ruido de $10^{-61}$ se hace visible porque el universo en expansión actúa como un telescopio gigante, igual que las fluctuaciones del Big Bang se convirtieron en galaxias”.

Hay que separar dos historias:

| Historia | Semilla real | Amplificación |
|:---------|:-------------|:--------------|
| Galaxias desde el Big Bang | curvatura primordial $\zeta\sim 10^{-5}$ **tras inflación** | crecimiento gravitatorio + muchos e-folds **tempranos** |
| Ruido Sorkin tardío | $\sigma_0\sim 10^{-61}$ (contaje holográfico global) | $\Delta x=\mathcal{O}(1)$ tardío **no** es $e^{60}$ |

El universo **sí** es un “telescopio” de **acumulación geométrica** a lo largo de la línea de visión.  
Eso multiplica efectos de orden $\sqrt{N_{\mathrm{patches}}}$ (ruido incoherente) o $N$ (coherente, poco realista).  
Con celdas de Mpc y caminos de Gpc, $\sqrt{N}\sim 10$–$10^{2}$ — **no** $10^{56}$.

**Teorema de este WP (machine-checked):**  
la acumulación de camino **no sustituye** a R1. Un Sorkin local $|\gamma-1|\sim 10^{-61}$ seguiría necesitando $\sqrt{N}\sim 10^{59}$ para rozar el floor de Sakr $\sim 0.05$; disponible $\sqrt{N}\sim 67$ (celda 1 Mpc, $z_s=1.5$).

---

## 3. Mapa local (misma microfísica que Option 0)

Gauge newtoniano, subhorizonte:

$$
k^{2}\Psi = -4\pi G a^{2}\rho_m\delta_m,
\qquad
k^{2}(\Phi-\Psi) = 8\pi G a^{2}\pi_T.
$$

Si el sector estocástico aporta

$$
\pi_T = \varepsilon\,\sigma\,\rho_X,
$$

con $\varepsilon\in[0,1]$ fracción anisotrópica del residual (idealmente **fijada** por la simetría residual de SDiff, no libre), entonces

$$
|\gamma-1| = \left|\frac{\Phi-\Psi}{\Psi}\right| = 2\varepsilon\sigma\frac{\rho_X}{\rho_m|\delta_m|}.
$$

Esto **no** depende de $(1+w)\to 0$: $\pi_T$ es amplitud de shear, no presión isótropa de fluido perfecto.

---

## 4. Acumulación a lo largo del camino

Sea $\ell_*$ la longitud de correlación del ruido (celda de contaje de WP1) y $\chi(z_s)$ la distancia comóvil a la fuente. Número de parches independientes:

$$
N_{\mathrm{pat}} \approx \frac{\chi(z_s)}{\ell_*}.
$$

Para un observable aditivo (suma de arrugas incoherentes):

$$
\mathrm{RMS}_{\mathrm{path}} \approx |\gamma-1|_{\mathrm{loc}}\sqrt{N_{\mathrm{pat}}}.
$$

(Cota superior coherente: $|\gamma-1|_{\mathrm{loc}} N_{\mathrm{pat}}$, rara para ruido estocástico.)

Fiducial del script: $z_s=1.5$, $\chi\approx 4480\,\mathrm{Mpc}$.

---

## 5. Resultados numéricos (script)

| Caso | $\sigma$ | $\ell_*$ | $\|\gamma-1\|_{\mathrm{loc}}$ | $N_{\mathrm{pat}}$ | RMS incoherente |
|:-----|:---------|:---------|:------------------------------|:------------------|:----------------|
| Sorkin + celda Planck | $1.2\times 10^{-61}$ | $L_P$ | $\sim 9\times 10^{-62}$ | enorme | $\sim 10^{-56}$ (sigue muerto) |
| Sorkin + $\ell_*=1\,\mathrm{Mpc}$ | $1.2\times 10^{-61}$ | 1 Mpc | $\sim 9\times 10^{-62}$ | $\sim 4.5\times 10^{3}$ | $\sim 6\times 10^{-60}$ |
| WP1 meso $\sigma=10^{-5}$, $\ell_*\sim 2\,\mathrm{Mpc}$ | $10^{-5}$ | 2.1 Mpc | $\sim 7.5\times 10^{-6}$ | $\sim 2\times 10^{3}$ | $\sim 3\times 10^{-4}$ |
| WP1 meso $\sigma=10^{-5}$, $\ell_*\sim 0.04\,\mathrm{Mpc}$ | $10^{-5}$ | 0.04 Mpc | $\sim 7.5\times 10^{-6}$ | $\sim 10^{5}$ | $\sim 2\times 10^{-3}$ |
| Techo DESI $\sigma_X=1.5\times 10^{-4}$ (a posteriori) | $1.5\times 10^{-4}$ | 10 Mpc | $\sim 1\times 10^{-4}$ | $\sim 450$ | $\sim 2\times 10^{-3}$ |

Monte Carlo (8000 caminos, $\sigma=10^{-5}$, $\ell_*=2.1\,\mathrm{Mpc}$): RMS $\approx 3.5\times 10^{-4}$, p95 $\approx 6.7\times 10^{-4}$ — coincide con $\sqrt{N}$.

### Lectura frente a floors (orden de magnitud)

| Floor | Valor | ¿Sorkin path? | ¿WP1 meso path? | ¿Techo DESI path? |
|:------|:------|:--------------|:----------------|:------------------|
| Maus $\|\gamma-1\|\sim 0.17$ | 0.17 | no | no | no (aún $\sim 10^{2}$ corto en incoherente) |
| Sakr $\sim 0.05$ | 0.05 | no | no | borde solo si coherente/optimista |
| Shear esquemático $\sim 10^{-3}$ | $10^{-3}$ | no | **sí, orden** | **sí, orden** |

Conclusión operativa:

- El canal de **luz** es el correcto y puede ser **más sensible** que el residual isótropo de BAO a la misma $\sigma$.  
- Aun así, **Sorkin path-integrado sigue siendo cero estructural**.  
- La semilla mesoscópica de WP1 (o el techo DESI como bound a posteriori) es lo que pone el RMS cerca de $10^{-3}$–$10^{-4}$.

---

## 6. Ganancia geométrica máxima a $z_s=1.5$

| $\ell_*$ (Mpc) | $N$ | $\sqrt{N}$ |
|:---------------|:----|:-----------|
| 0.04 | $\sim 1.1\times 10^{5}$ | $\sim 335$ |
| 1 | $\sim 4.5\times 10^{3}$ | $\sim 67$ |
| 2.1 | $\sim 2.1\times 10^{3}$ | $\sim 46$ |
| 10 | $\sim 450$ | $\sim 21$ |
| 100 | $\sim 45$ | $\sim 7$ |

Eso es **todo** el “telescopio geométrico” del camino. Útil; no mágico.

---

## 7. Ceros estructurales (A6)

1. **Sorkin + cualquier camino cosmológico realista** $\Rightarrow$ arruga de luz $\ll$ floors (teorema numérico).  
2. **Solo $H(z)$ isótropo** $\Rightarrow$ ciego al $\pi_T$ (operador incorrecto para la grieta SDiff).  
3. **Pupila / tesseract / lab** $\Rightarrow$ escala incorrecta; el path integral cosmológico no aplica.

---

## 8. Estado de R2 en la tabla A4

| Pieza | Estado |
|:------|:-------|
| Mapa $\pi_T\to\|\gamma-1\|$ | **Derivado** (anisotropía newtoniana) |
| Acumulación $\sqrt{N}$ a lo largo del camino | **Derivado + MC** |
| $\varepsilon$ desde simetría SDiff (no libre) | **Ausente** (abierto; se declara) |
| Boltzmann hi_class / MGCAMB | **No** (aún no hay $A_0$ + $\varepsilon$ derivados del todo) |

**Estado R2:** operador y path map **cerrados a orden de magnitud**; $\varepsilon$ microfísico **abierto**.

---

## 9. Encaje del paquete R1–R2–R3

```
R1:  σ_0,eff = (ℓ_*/L)^{d/2}     →  sin celda Mpc, semilla muerta
R3:  G_O ~ O(10) suave           →  no salva Sorkin
R2:  π_T → arrugas → luz         →  operador correcto; gain geométrico √N ~ O(10–100)
        ⇒  “universo telescopio” = √N path, no 10^56
        ⇒  medibilidad de arrugas ⇔ semilla mesoscópica (R1) ± open suave (R3)
```

La frase correcta del programa:

> El ruido no necesita empujar $H(z)$; puede arrugar $\Phi,\Psi$ y acumularse en la luz.  
> Pero un ruido de $10^{-61}$ **no** se vuelve $10^{-5}$ por viajar Gpc: se vuelve visible solo si la **celda de contaje** (R1) ya lo sacó del abismo, o si un baño abierto **derivado** (R3 duro) lo engorda — y eso aún no está construido sin numerología.

---

## 10. Cómo correr

```bash
cd measurable-stochastic-vacuum
python scripts/r2_light_path_accumulation.py
python scripts/r2_light_path_accumulation.py --heavy   # más caminos MC
```

---

*Fin de WP3. Siguiente natural: WP4 (tabla conjunta de predicciones y ceros) o un candidato R1a/b/c que fije $\ell_*$.*
