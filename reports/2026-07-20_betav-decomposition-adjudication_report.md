# Canonical report — P2-BETAV-CIRC-01 determinant-decomposition adjudication (Phase 1)

**Date:** 2026-07-20. **Repository:** `zetacheng/2-emergent-gravity`.
**Branch:** `gate/p2-betav-decomp` (off `main` = `2c396fc`).
**Type:** derivation/adjudication — **no k-scan run**, no numerical target.

## 1. Executive summary

Phase-1 adjudication of whether a `k`-scan of `P2-BETAV-CIRC-01` can even be
*defined* from the recovered code. **Verdict: DECOMP-NOT-REPRESENTABLE.** The
recovered Proca operator and the recovered scalar operator cannot be combined
into a compensator-power deformation that reduces to the recovered Proca result
at the physical point and avoids double-counting. No `k`-scan is scientifically
defined from the recovered pipeline alone. This is a real result, not a failure;
gate statuses and the `−3.2(5)` quarantine are unchanged.

## 2. The determinant `proca_loop.py` computes

Flat kernel `M_{μν} = (ŝ²+m²)δ_{μν} − a_μa_ν*`, `a_μ = e^{ik_μ}−1`,
`ŝ² = Σ4sin²(k_μ/2) = p̂²`. Spectrum (verified): `{ŝ²+m² (×3 transverse),
m² (×1 longitudinal)}`, `det M = m²(ŝ²+m²)³`. Loop `Γ = +½⟨ln det M⟩`; `Z` is the
axis-TT slope via the 5 fixed, `k`-independent `TT_RECIPES`, `/5`, `fit_mlog`.
Propagator eigenvalues: `1/(ŝ²+m²)` transverse, `1/m²` longitudinal.

## 3. Longitudinal `m²` vs external scalar `Δ₀` — different operators

| | Proca longitudinal | External scalar (`boson_loop`) |
|---|---|---|
| kernel factor | `m²` (ultralocal) | `Δ₀ = ŝ²+m²` (propagating) |
| momentum dependence | none (spread over `p̂²` = `3e-16`) | full |
| propagator | `1/m²` (drives the `1/m²` artifact) | `1/(ŝ²+m²)` |
| `m²ln m²` content | momentum-independent `½ln m²` | universal propagating IR log |

**They are not the same operator.** An external minimally-coupled scalar loop
cannot represent a change in the Proca compensator power.

## 4. Metric-variation block-diagonality — FAILS

The one-graviton vertex `δM` has nonzero transverse↔longitudinal blocks:
`max|⟨T|δM|L⟩| = 0.17` (from `scripts/betav_decomp_check.py`). Hence the bubble
carries genuine mixed terms `G_T δM G_L δM`, `G_L δM G_T δM ≠ 0`, and the flat
factorization `det M = m²(ŝ²+m²)³` does **not** lift to an additive
three-transverse-plus-scalar split of the curved induced action. No invariant
longitudinal `Z` can be assigned.

## 5. Determinant identities adjudicated

(a) complete curved `det M_Proca` — what the code computes; (b) flat spectral
`m²(ŝ²+m²)³` — `h=0` only, not a curved factorization; (c) external scalar
`det Δ₀ = ŝ²+m²` — a different operator; (d) continuum gauge-fixed Stueckelberg
quotient — where the analytic `−3` lives, **not** an operator identity of the
lattice `M`. The historical `k=1` corresponds to **(a)**; the analytic `−3` to
**(d)**. Different objects — hence the recovered numerics give `−16`/`−61`
(grid/artifact limited), not `−3`.

## 6. Derived generalized-`k` expression — or the obstruction

No operator-defined compensator-power deformation of `det M_Proca` exists that
(i) changes the compensator multiplicity, (ii) reduces pointwise to recovered
Proca at the physical point, and (iii) avoids double-count. The compensator is
the ultralocal `m²` factor **inside** the same kernel (not a separable
determinant, §4), and the external `Δ₀` scalar is the **wrong** operator (§3).
`Γ_Proca + (k−k_phys)Γ_scalar[Δ₀]` reduces only *trivially* at `k=k_phys` (added
term vanishes) and is a different multi-species theory for `k≠k_phys`. **The
obstruction is demonstrated, not bypassed.**

## 7. Pointwise consistency definition

`Z_generalized(k=phys, m_i, n) ≡ Z_recovered_Proca(m_i, n)` per grid (i.e. `−16`
at `n=16`, **not** `−3`). No construction satisfies this while deforming the
compensator power — see §6.

## 8. Non-linearity audit

`TT_RECIPES` averaging (linear), `/5` (linear), `fit_mlog` = ordinary linear
least squares (linear), ratio by a **fixed, `k`-independent** `β_B` (linear up to
constant scale). A non-linear circular mechanism could live only in a
`k`-dependent `β_B`/window/normalization — which the recovered pipeline does not
have. **Every relevant step is linear.**

## 9. Verdict (exactly one): DECOMP-NOT-REPRESENTABLE

The recovered Proca and scalar operators cannot be combined into a
compensator-power deformation preserving the physical-point Proca result and
avoiding double-count (ultralocal `m²` ≠ additive propagating `Δ₀`; inseparable
T–L mixing). No `k`-scan is defined from the recovered code alone. Secondary:
even ignoring the operator objection, all steps are linear ⟹ `LINEAR-ONLY`
(bookkeeping, not circularity). Reformulate the circularity question as an
operator/determinant-identity audit ((a) vs (d)) or via the clean-room
`P2-BETAV-RECON-01` — not a `k`-scan.

## 10. Gate statuses unchanged / quarantine held

`P2-BETAV-CIRC-01` = `SPECIFIED`; `P2-BETAV-NUMREPRO-01` = `PROPOSED`;
`P2-C9` = `PROPOSED`; `β_V/β_B = −3.2(5)` quarantined/unreproduced. Unchanged by
this adjudication (`CLAIMS.md` untouched; no claim promoted).

## 11. Commit order (executable before interpretation)

1. `6fd54d3` derivation: operator-level checks of the recovered Proca determinant (no target)
2. `82157de` derivation: determinant decomposition for P2-BETAV-CIRC-01 (Phase 1, no scan)
3. this report + `DECISION_LOG.md` adjudication commit.

The executable operator-check commit (1) precedes the interpretive commits (2,3).

## 12. Tests / status / remote

Clean-checkout `python -m pytest tests -q`: recorded in the terminal summary.
`git status --porcelain`, commit hashes, and `git ls-remote --heads origin`:
terminal summary. No recovered historical source edited.

## What comes next (not this task)

Because the outcome is DECOMP-NOT-REPRESENTABLE, the next step is **not** a
`k`-scan but the reformulated circularity audit (operator/determinant-identity
(a)-vs-(d)) or the clean-room `P2-BETAV-RECON-01`. `−3.2(5)` promotion stays with
`P2-BETAV-NUMREPRO-01`, untouched.
