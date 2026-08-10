# Public gravitational-wave data (GWOSC)

Real open data from the Gravitational Wave Open Science Center. Not DESI BAO.

```bash
python scripts/gw/download_gwosc_strain.py
```

| File | Content |
|:-----|:--------|
| `H-H1_GWOSC_4KHZ_R1-1126259447-32.hdf5` | Hanford strain, GW150914 window |
| `L-L1_GWOSC_4KHZ_R1-1126259447-32.hdf5` | Livingston strain, same window |
| `GW150914.json` | event metadata |
| `GWTC-3-confident.json` | catalog snapshot |
| `PROVENANCE.json` | download record |

DOI: https://doi.org/10.7935/82H3-HH23  
Analysis: `scripts/gw/gw_channel_real_strain.py` → `results/gw_channel/`
