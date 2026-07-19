# Derivation note — `P2-NORM-01`: locate the `β`/`G` normalization factor 2

**Kind:** bookkeeping (normalization-convention reconciliation).

## Scientific question

The first verification report's headline disagreement "D1" claimed the paper
used a Weyl `β_F`. That was an artifact of comparing across normalizations. The
real observation: **every** species coefficient in this repository is exactly
`2×` the paper's, uniformly:

| | This repo | Paper (v2.15) | ratio |
|---|---|---|---|
| `β_B` continuum | `1/(192π²)` | `1/(384π²)` (eq. `betaB`) | 2.00 |
| `β_F` | `1/(96π²)` | `1/(192π²)` ("`β_F=2β_B`") | 2.00 |
| `β_V` | `1/(64π²)` | `1/(128π²)` (`=−3β_B`) | 2.00 |
| `β_B(ξ)` | `(1−6ξ)/(192π²)` | `(1−6ξ)/(384π²)` | 2.00 |

A uniform factor 2, cancelling in every ratio (`β_F/β_B=2`, `β_V/β_B=−3`,
`β_B(ξ)/β_B=1−6ξ`) and in the sign. This is a normalization convention in the
definition of `Z`, not physics. Locate the exact step.

## The one normalization chain

```
Z(m²)  ──►  β_s (coeff of m²ln m² in Z)  ──►  4 G_c β_F  ──►  ξ_ind = 4Gβ_F(3−L)
```

Step by step, stating the convention at each node:

1. **Definition of `Z`.**
   - *This repo:* `Z_here ≡ 1/(16πG_ind)`, the coefficient of `∫√g R` in the
     one-loop effective action. From the heat kernel,
     `β_s = −p_s (4π)^{−2} (tr a_1/R)` (P2-HK-01).
   - *Paper:* `Z_paper ≡` the axis-TT graviton kinetic slope (coefficient of
     `p²` in the transverse-traceless graviton self-energy) **per unit `4N`**
     (paper eq. between `xichain` and `xiuniv`; `Π(p) = −4N∫…`, eq. `bubble`).
   The two differ by the fixed factor `R_Z` relating "coefficient of `R` in the
   action" to "coefficient of `p²` in the axis-TT slope" — a graviton-kinetic
   normalization. **Empirically `R_Z = 2`, identical for every species**
   (scalar, Dirac, Proca; verified in `scripts/normalization_chain.py`), so it
   is a definitional constant, not species physics. The `4N` divisor removes
   the fermionic degeneracy and does **not** carry the 2 (the scalar `β_B`,
   with no `4N`, shows the same factor 2).

2. **Dirac trace and `Γ = ½ ln det`.** The Dirac trace (`4`) sits inside the
   bundle `tr a_1` and the real-scalar `½` is the `p_s = +½` prefactor; both are
   already in `β_s` and are the **same** on both sides (they cancel in `R_Z`).

3. **Gap-equation coupling `G_c`.** `G_c = 8π²/Λ²` from `1 = 2G_c I_0`
   (P2-GAP-01). This is a property of the four-fermion bubble `I_0` and is
   **`Z`-independent** — it does *not* carry `R_Z`.

4. **The product `4 G_c β_F`.** Because `G_c` is `Z`-independent but `β_F`
   carries `R_Z`, the product inherits the `Z`-convention of `β_F` alone:
   ```
   4 G_c β_F = 1/3   (Z_here)      = 1/6   (Z_paper).
   ```
   The paper's `4·8π²/(192π²) = 1/6` is exact **in its own convention**. The
   report's "`1/3`" came from combining `Z_here` (for `β_F`) with the paper's
   `G_c` — mixing conventions. **That is the error, and it is retracted.**

## Outcome

**(a)** — the two chains are the same theory in different conventions. The
factor 2 enters at **step 1, the definition of `Z`** (coefficient of `R` in the
action vs axis-TT slope per unit `4N`), uniformly across all species. The
paper's `4G_cβ_F = 1/6` is self-consistent in its convention.

*Residual (c) element, stated honestly:* to certify from first principles that
the paper's `Z_paper` normalization and its compositeness identification
`G ≡ Ny² = G_c` are the mutually consistent pair for which `ξ_ind` is the
*physical* induced coupling (so that `1/6`, not some other number, is the
physical prefactor), one needs the axis-TT extraction normalization spelled out
to the factor-of-2 level and the `Ny² ↔ G_c` map — present in the paper's
pipeline but not reconstructible from the text's numbers alone. This does not
reopen the disagreement; it only marks the one factor taken on the paper's word.

## Physics consequence (this gate is bookkeeping, not physics)

`ξ_ind = 4Gβ_F(3−L)` is negative for `L ≫ 1` whether the prefactor is `1/6` or
`1/3` (both positive, times `(3−L) < 0`). Only the survival-window boundary
moves — `m > 0.368Λ` (`1/6`) vs `m > 0.287Λ` (`1/3`) — and the paper notes both
are unattainable in the lattice scheme (`L` large). **The paper's central
negative conclusion — the minimal model fails its own survival condition — is
not at stake here.** The ledger must not overstate this gate.

## Pre-registered verdict

Report outcome (a); the factor 2 is the `Z` definition; retract D1 and the
`1/3` "disagreement"; state the physics is unchanged.

## Implementing script

`scripts/normalization_chain.py` (`python -m scripts.normalization_chain`).
