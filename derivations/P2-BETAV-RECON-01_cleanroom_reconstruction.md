# Derivation note — `P2-BETAV-RECON-01`: clean-room Proca reconstruction (PROPOSED)

**Kind:** numerical proxy (a *new* pipeline). **Scope label — read first:**
**this is a 2026 reconstructed pipeline. It is NOT a test of the historical
Finding 5 implementation.** If built and it tracks `−(k+2)`, that shows only
that *this reconstruction* is faithful; it does **not** show the historical
Finding 5 pipeline (which is absent from the repository — see
`results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md`) was non-circular.

## Why a reconstruction is a distinct object

`P2-BETAV-CIRC-01` asks whether the *historical* extraction's
projection/normalization silently fixed the ratio at `−3`. That question is
about *that code*. A clean-room reconstruction cannot answer it: a faithful new
pipeline that returns `−(k+2)` demonstrates only that a correct pipeline exists,
not that the historical one was correct. The two must never be conflated.

## Proposed construction (if scoped and run later)

1. Lattice 1-form operator `Δ^{(1)}[g,h]` (metric-coupled vector Laplacian) and
   the compensating scalar `Δ^{(0)}[g,h]`, on a weak-field background
   `g = δ + h`, with the exact geometric factors `√g g⁻¹⊗g⁻¹`, `√g g⁻¹`.
2. Effective action `Γ_k[h] = ½ log det Δ^{(1)}[h] − (k/2) log det Δ^{(0)}[h]`.
3. **Numerical `h`-derivatives** `∂²Γ_k/∂h∂h` taken at the determinant /
   eigenvalue level (this is where a circular pipeline could normalise `k` out;
   it must be exercised, not bypassed by an analytic shortcut).
4. Extract the EH coefficient with a **fixed** axis-TT projection and
   normalization, identical for every `k`.
5. Vary **only** the determinant exponent `k ∈ {0, 1, 2, 3, 1/2}`.
6. Compare `R_k` to `−(k+2)` only at the end (targets kept out of the code and
   tests; pre-register the `h`-derivative step, Richardson check, and projection
   in a separate pre-reg note *before* running).

Decision rule (for the reconstruction, on its own terms): tracks `−(k+2)` →
the reconstruction is faithful; stuck at `−3` ∀k → the reconstruction itself is
degenerate (a bug in the new pipeline); drift toward `−5` at heavy mass →
longitudinal artifact identified. **None of these outcomes closes
`P2-BETAV-CIRC-01`.** The tolerance is a propagated *ratio* error (numerator and
denominator share the momentum grid — correlated), not two independent `β`
scatters divided.

## Status

`PROPOSED`. Not run in this sweep: the metric-coupled lattice Proca operator
with numerical `h`-derivatives is a substantial implementation, not a
straightforward one. Registered so the path is on the record with its scope
label attached.

## Implementing script

None yet (proposed).
