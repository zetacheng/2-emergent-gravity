# Result — `P2-BETAV-ASSEMBLY-01`: determinant-bookkeeping regression

**This gate does NOT close `P2-BETAV-CIRC-01`.** It is an implementation
regression, not the historical circularity test (that pipeline is absent — see
`results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md`).

**Gate:** `P2-BETAV-ASSEMBLY-01`.
**Derivation:** `derivations/P2-BETAV-ASSEMBLY-01_bookkeeping_regression.md`.
**Script:** `scripts/betav_assembly.py` (`python -m scripts.betav_assembly`).

`R_k = β_V(k)/β_B = −(k+2)` (k=0→−2, 1→−3, 2→−4, 3→−5, ½→−5/2), realized on the
shared scalar lattice tadpole. The shared integral `C` **cancels** in the ratio,
so the ratio's variant spread is ~machine zero (≤ 9e-16) — the numerator and
denominator are fully correlated. That exact cancellation is why this
construction has no power to test the historical projection; it only verifies
the code reads `k` and does not hardcode `−3`. Mutation (freeze scalar power=1)
collapses every `R_k` to `−3`.

- `raw/betav_assembly.json` — authoritative output.
- `regen/` — non-authoritative re-runs (gitignored).
