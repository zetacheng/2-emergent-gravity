# Result — `P2-NORM-01`: locate the `β`/`G` normalization factor 2

**Gate:** `P2-NORM-01`. **Derivation:** `derivations/P2-NORM-01_normalization_chain.md`.
**Script:** `scripts/normalization_chain.py` (`python -m scripts.normalization_chain`).

Outcome **(a)**: the factor 2 between this repository's `β_s` and Paper 2 v2.15's
is a uniform (`R_Z = 2`, every species) normalization of `Z` — coefficient of
`∫√g R` in the action (here) vs axis-TT slope per unit `4N` (paper). It cancels
in all ratios and the sign. `4G_cβ_F = 1/6` in the paper's convention (self
consistent); the earlier `1/3` was convention-mixing (retracted). Physics
unchanged: `ξ_ind < 0` for `L ≫ 1` either way.

- `raw/normalization_chain.json` — authoritative output.
- `regen/` — non-authoritative re-runs (gitignored).
