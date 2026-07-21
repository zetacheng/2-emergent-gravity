# Batch-2 validation — Fierz algebra & gauge-fixed constant-h machinery

**Date:** 2026-07-21. Cheap validation runs only (seconds); **no β extraction,
no ratio target evaluated.** The hours-long `precision_campaign.py` was **not**
run (see item 3). All runs used the verbatim recovered originals under
`scripts/recovered_2026/batch2/` with the batch-1 modules on `PYTHONPATH`.

## 1. Fierz foundations — `fierz_verify.py`, `grassmann_check.py` (pure algebra)

Both ran to completion (exit 0); they are self-validating (internal `assert`s on
the γ-algebra, hermiticity, orthonormality, and completeness, plus printed
booleans). `pairing_fierz.py` was run additionally as a supplementary
foundations check.

**`fierz_verify.py`** (exit 0):
- `completeness (hermitian orthonormal basis): True` — `Σ_A (B_A)_ij (B_A)_kl =
  4 δ_il δ_kj` holds.
- 5×5 Fierz exchange matrix `F` printed (channels `S,P,V,A,T`):
  ```
  [[ 0.25  0.25  0.25  0.25  0.25]
   [ 0.25  0.25 -0.25 -0.25  0.25]
   [ 1.   -1.   -0.5   0.5   0.  ]
   [ 1.   -1.    0.5  -0.5   0.  ]
   [ 1.5   1.5   0.    0.   -0.5 ]]
  ```
- Note (printed by the script, expected): `paper basis (Γ^A = Γ_A) equals
  completeness delta: False` — a diagnostic about the paper's raised/lowered
  convention, **not** an assertion failure; every internal `assert` passed and
  the run exited 0.

**`grassmann_check.py`** (exit 0): the Grassmann exchange identity
```
Σ_A (ψ̄ Γ_A ψ)²  ==  −4 Σ_ab exchange :  True   (N=1)
                                          True   (N=2)
```
(the `+4` variant is correctly `False`; the physical identity carries the
Grassmann minus sign).

**`pairing_fierz.py`** (exit 0, supplementary): `C = γ₂γ₄` satisfies
`C γ_μ C⁻¹ = −γ_μᵀ` (True) and is antisymmetric (True); `C S(−p)ᵀ C⁻¹ = S(p)`
for the Wilson propagator incl. mass+`r` (True); antisymmetric pairing channels
(N=1) `= [S, P, A1..A4]`; exact pairing decomposition residual `5.21e-15`
(rank 36/36), with `(ψ̄ψ)²+(ψ̄iγ₅ψ)² = −½ Σ_μ (A_μ,A_μ)` (diagonal axial pairing).

**Verdict: VALIDATES.** These underpin the future `P2-CHANNEL-FREEZE-01` basis
freeze. No numerical physics target is involved; this is closed algebra.

## 2. Gauge-fixed operator machinery — `gfvec_loop.const_h_check_gf` (small `n`)

Ran `const_h_check_gf(n, m=0.5)` for `n∈{6,8}` — the constant-`h` validation:
perturbative **bubble+seagull** vs the **exact** `½⟨ln det M⟩` of the
*minimal-vector* kernel `Δ^{(1)}+m²` (= Proca + gauge-fixing term). This
validates the recovered determinant-quotient (Solodukhin) machinery **without**
any β extraction and **without** any ratio target.

```
n=6, m=0.5   (elapsed 0.2s)
  (0,0)(0,0): exact=+2.871710e-01  pert=+2.871713e-01  diff=2.7e-07
  (0,1)(0,1): exact=+7.072147e-01  pert=+7.072152e-01  diff=5.2e-07
  (0,0)(1,1): exact=-9.614086e-02  pert=-9.614102e-02  diff=1.6e-07
n=8, m=0.5   (elapsed 0.7s)
  (0,0)(0,0): exact=+2.879797e-01  pert=+2.879800e-01  diff=2.7e-07
  (0,1)(0,1): exact=+7.071655e-01  pert=+7.071660e-01  diff=5.1e-07
  (0,0)(1,1): exact=-9.633869e-02  pert=-9.633885e-02  diff=1.6e-07
```

Exact-vs-perturbative agreement to `~1e-7` for all three `h`-component pairs at
both grids (the residual is the `O(EPSF²)` finite-difference floor, consistent
across `n`). This is the machinery that implements
`Γ_Proca = Γ_minvec − Γ_scalar(m)`.

**Verdict: VALIDATES (machinery only).** The recovered gauge-fixed vertex +
seagull reproduce the exact `ln det` of the minimal-vector operator. This
confirms the *implementation* of the determinant-quotient object; it does **not**
compute or endorse any `β_gfvec/β_B` or `β_V/β_B` value — that is deferred to a
blind-harness run (item 3) and to the `P2-BETAV-CIRC-01` operator-identity audit.

## 3. Precision campaign — `precision_campaign.py` — NOT RUN (by design)

**Verdict: NOT-RUN-AND-WHY.** Two reasons:
1. **Cost:** its own docstring estimates *several hours* on N=48 lattices.
2. **Provenance hazard:** its docstring and printed lines embed the analytic
   targets `β_gfvec/β_B = −2.000` and `β_V/β_B = −3.000` (and the consistency
   target `proca − (gfvec − boson) = 0`). Running it as-is would compute a ratio
   in the presence of the answer. **Any future β-extraction run must go through
   a blind harness** (targets stripped from the driver, compare only after the
   number is frozen) — recorded in the `P2-BETAV-CIRC-01` gate addendum. Its
   output `precision_results.json` is registered as a missing artifact
   (`scripts/recovered_2026/MISSING.md`).

## Summary table

| Item | What | Verdict |
|---|---|---|
| 1 | Fierz/Grassmann/pairing algebra | **VALIDATES** (self-validating, exit 0) |
| 2 | `const_h_check_gf(n=6,8; m=0.5)` | **VALIDATES** (machinery; exact≈pert to 1e-7) |
| 3 | `precision_campaign.py` | **NOT RUN** (hours; embeds targets → blind harness required) |
