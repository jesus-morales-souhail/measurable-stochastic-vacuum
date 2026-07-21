"""
WP1 / R1 — counting principle for the stochastic-DE seed.

Derive sigma_{0,eff} = 1/sqrt(N_eff) from a counting principle, WITHOUT using
the DESI number 1.5e-4 as a dial (axiom A5). The seed is set by an effective
cell scale ell_* and a counting dimensionality d of the DE-residual sector.

Sorkin (the excluded seed) corresponds to the holographic count:
    N_BH = (L_H / L_P)^2  ~ 1e122   ->   sigma_0 = 1/sqrt(N_BH) = L_P/L_H ~ 1e-61.

R1 redefines WHICH region and WHICH cell the DE sector counts. We do NOT pick
ell_* to hit 1e-5; we compute the LANDSCAPE sigma(ell_*, d) and read off the
cell scale that measurability would require, then state the open kernel
honestly: what PRINCIPLE fixes that cell scale for the DE sector?
"""
import numpy as np

L_P  = 1.616e-35                 # Planck length, m
L_H  = 3e8/(67.4/3.086e19)       # Hubble radius c/H0, m  (~4.46 Gpc)
Mpc  = 3.086e22                  # m
N_Sorkin = (L_H/L_P)**2
sigma_Sorkin = 1/np.sqrt(N_Sorkin)
print(f"Hubble radius L_H = {L_H/Mpc:.0f} Mpc ;  Planck L_P = {L_P:.2e} m")
print(f"Sorkin (holographic, d=2): N_BH = (L_H/L_P)^2 = {N_Sorkin:.2e}  ->  sigma_0 = {sigma_Sorkin:.2e}")
print()

def sigma_seed(ell, L, d):
    """sigma_{0,eff} = (ell/L)^{d/2}  for a d-dimensional count N=(L/ell)^d."""
    return (ell/L)**(d/2)

# Structural zeros (axiom A6): Planck cell => always null, regardless of d
print("Structural zeros (cell = Planck):")
for d in (2,3,4):
    s = sigma_seed(L_P, L_H, d)
    print(f"  d={d}: sigma = {s:.2e}   (<< 1e-5  ->  DESI/Euclid null is a THEOREM, not a failure)")
print()

# Landscape: what cell scale does MEASURABILITY (sigma ~ 1e-5) require?
sigma_target = 1e-5
print(f"Cell scale ell_* required for measurability sigma ~ {sigma_target:.0e}:")
for d in (2,3,4):
    # sigma = (ell/L_H)^{d/2} = sigma_target  ->  ell = L_H * sigma_target^{2/d}
    ell = L_H * sigma_target**(2.0/d)
    print(f"  d={d}: ell_* = {ell/Mpc:.2f} Mpc   (NOT Planck; galactic / mesoscopic)")
print()

# Cross-check: with ell = L_P the whole measurable band is unreachable for all d
print("Reachable band [1e-5, 1.5e-4] needs ell_* >> L_P by:")
for d in (2,3,4):
    ell = L_H * sigma_target**(2.0/d)
    print(f"  d={d}: ell_*/L_P = {ell/L_P:.2e}")
print()
print("OPEN KERNEL (honest): the counting CELL for the DE sector must be")
print("mesoscopic/galactic (~kpc-Mpc), not Planck, for the residual to be")
print("telescope-measurable. The R1 programme's load-bearing question is:")
print("  WHAT PRINCIPLE fixes a galactic-scale DE counting cell, distinct")
print("  from the Planck/holographic one?  (Sorkin = L_P -> null by theorem.)")
