# Result — `P2-HK-01`: heat-kernel species coefficients

**Scientific question.** The `m² ln m²` coefficient `β_s` of the induced
Einstein–Hilbert kinetic coefficient `Z(m²)` for each species, from the
Seeley–DeWitt expansion, and the ratios `β_F/β_B`, `β_V/β_B`, `β_B(ξ)/β_B`.

**Gate:** `P2-HK-01`. **Derivation:** `derivations/P2-HK-01_heat_kernel_species.md`.
**Producing script:** `scripts/hk_species.py` (`python -m scripts.hk_species`).

## Artifact map

- `raw/hk_species.json` — authoritative frozen output (exact symbolic values).
- `regen/` — non-authoritative re-runs (gitignored).
- `environment.txt`, `branch.txt`, `commit_parent.txt` — provenance.

## Computed values (pre-registration: computed before consulting the paper)

| Quantity | Value |
|---|---|
| `β_B` (real scalar, minimal) | `−1/(192π²)` ≈ `−5.277e-4` |
| `β_B(ξ)` (non-minimal scalar) | `(6ξ−1)/(192π²) = −(1−6ξ)/(192π²)` |
| `β_F` (Dirac) | `−1/(96π²)` ≈ `−1.055e-3` |
| `β_V` (Proca) | `+1/(64π²)` ≈ `+1.583e-3` |
| `β_F/β_B` | `2` |
| `β_V/β_B` | `−3` |
| `β_B(ξ)/β_B` | `1 − 6ξ` |
| proper-time `m²ln m²` coefficient (route 2) | `1` |

The `β_s` absolute normalization uses the convention in `CONVENTIONS.md`
(`β_s = −p_s (4π)^{−2} tr a_1/R`); the ratios are convention-independent and
are the primary deliverable.

**Note on the Proca `tr a_1/R` field.** The JSON lists `−1/6` for Proca as the
naive sum of the two determinant factors' `tr a_1/R` (`−1/3` vector `+ 1/6`
scalar). Because the two factors carry *different* log-det prefactors `p`
(`+½` and `−½`), `β_V` is assembled per factor, not from this sum; see the
derivation note's table.
