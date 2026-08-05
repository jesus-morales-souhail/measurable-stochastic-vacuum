# Work packages (live checklist)

Jesús Morales Souhail · updated with the residual-scale work
Hard results live in [`papers/core/VERIFIED_RESULTS.md`](../papers/core/VERIFIED_RESULTS.md). Green `pytest -q` is the gate.

This is my own checklist, not a paper.

| WP | Theme | Status | Notes |
|:---|:------|:-------|:------|
| WP1 | counting seed / open kernel | partial → uniqueness under axioms | [`r1-counting-principle.md`](../papers/r1_kernel/r1-counting-principle.md), [`r1-open-kernel.md`](../papers/r1_kernel/r1-open-kernel.md), [`NOTE_uniqueness…`](../papers/r1_kernel/NOTE_uniqueness_residual_grain.md) |
| WP2 | slip from residual | kinematics done | [`r2-slip-from-same-sector.md`](../papers/work_packages/r2-slip-from-same-sector.md) |
| WP3 | soft open / horizon maps | soft gains too small | [`r3-open-horizon-map.md`](../papers/work_packages/r3-open-horizon-map.md) |
| WP4 | joint zeros | table written | [`wp4-…`](../papers/work_packages/wp4-joint-predictions-and-zeros.md) |
| WP5 | falsification | criteria written | [`wp5-…`](../papers/work_packages/wp5-falsification.md) |
| — | $R_{\mathrm{nl}}$ full integral | done | [`r1-principle-nonlinear-matter.md`](../papers/r1_kernel/r1-principle-nonlinear-matter.md) |
| — | T1 geometry | done | [`r1-t1-mechanisms-compute.md`](../papers/r1_kernel/r1-t1-mechanisms-compute.md) |
| — | $g$ proxy + T2 mock | done at OOM / synthetic level | line A + T2 scripts |

```bash
python scripts/core/lib_verified.py
python scripts/r1/r1_counting_landscape.py
python scripts/r1/r1_sandwich_derivation.py
pytest -q
```
