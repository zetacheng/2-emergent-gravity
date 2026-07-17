# Result — `P2-GAP-01`: gap-equation criticality

**Scientific question.** The critical scalar-channel four-fermion coupling
`G_c` from the leading-order (mean-field) gap equation, continuum (sharp
4-ball) and lattice (Wilson `r=1`); derive `G_c = 1/(2 I_0)`.

**Gate:** `P2-GAP-01`. **Derivation:** `derivations/P2-GAP-01_gap_criticality.md`.
**Producing script:** `scripts/gap_criticality.py` (`python -m scripts.gap_criticality`).

## Artifact map

- `raw/gap_criticality.json` — authoritative frozen output.
- `regen/` — non-authoritative re-runs (gitignored).
- `environment.txt`, `branch.txt`, `commit_parent.txt` — provenance.

## Computed values (pre-registration: computed before consulting the paper)

| Quantity | Value | How obtained |
|---|---|---|
| `I_0` continuum | `Λ²/(16π²) = 0.00633257` | exact (sharp 4-ball `∫1/p²`) |
| `G_c` continuum | `8π²/Λ² = 78.9568` → `c = 8` (exact) | `1/(2I_0)` |
| `I_0` lattice (Wilson `r=1`) | `0.085388 ± 0.00002` | BZ midpoint quadrature |
| `G_c` lattice | `5.8556` | `1/(2I_0)` |

**Uncertainty on `I_0^lat`.** Grid refinement `n=64,96,128` gives
`0.085373, 0.085383, 0.085386` (straight grid); straight-vs-offset (shift 0.25)
spread at `n=128` is `3.2e-6`. Extrapolated value `≈ 0.08539`, uncertainty
`±2e-5` dominated by residual grid drift — a systematic bound, not a formal
error.

## Which criticality

Gap-equation (leading-order effective-potential) criticality — the tadpole
self-consistency `1 = 2 G_c I_0`. **Not** a channel-bubble criticality; the
leading-order gap equation cannot distinguish them (recorded, not glossed).

## Caveat

Wilson explicitly breaks chiral symmetry; `I_0` is defined at the tree-level
chiral point `Σ=0` with `W` as the regulating mass. A fully consistent
treatment tunes the bare mass to `κ_c`. This affects the absolute lattice `G_c`
at the level of lattice artifacts, not the definition of `I_0`. The absolute
`G_c` also depends on the coupling normalization (the factor `2`); `I_0` is the
convention-independent deliverable.
