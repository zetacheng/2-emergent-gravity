# Paper 2 v2.15 — independent recomputation vs the source

**Source now imported:** `paper/emergent_gr_paper_v2_15.tex` (1833 lines). Every
"Paper 2 v2.15" cell below is a quotation from that file with its equation or
line label — no longer an inference. This supersedes the first comparison, which
was made without the source and contained an inference error (see "Retractions").

## Retractions (read first)

- **D1 (Weyl vs Dirac `β_F`) is WITHDRAWN.** It was an artifact of comparing the
  paper's `β_F` against *this repo's* `β_B`, which are in different `Z`
  normalizations. The paper states `β_B^cont = 1/(384π²)` (eq. `betaB`) and
  `β_F = 2β_B = 1/(192π²)` (line 1155): **`β_F/β_B = 2`, identical to this
  repo's.** There is no species-content disagreement. The real effect is a
  *uniform* factor 2 in the definition of `Z` (see gate `P2-NORM-01`).
- **D2 (lattice `I_0` ≈1.2% gap) is WITHDRAWN.** It compared this repo's
  *massless* `I_0` against the paper's value at reference mass `ma=0.02`. At
  matched mass they agree to `<0.1%` (see gate `P2-GAP-01` below).
- The earlier "Agree: `β_B` continuum exact" row was **wrong**: it compared this
  repo's lattice `β_B` to this repo's own continuum value (an internal check),
  not to the paper. Corrected below.

## Block I — convention-independent quantities (comparable as they stand)

| Quantity | Paper 2 v2.15 (quoted) | This repository | Agreement |
|---|---|---|---|
| `β_F/β_B` | `β_F = 2β_B` (line 1155) → `2` | `2` (exact) | **agree** |
| `β_V/β_B` (analytic) | `−3` (eq. `betaVlat`; `β_V=−3β_B`, line 1287) | `−3` (exact) | **agree** |
| `β_B(ξ)/β_B` | `β_B(ξ)=(1−6ξ)/(384π²)` (line 1171) → `1−6ξ` | `1−6ξ` (exact) | **agree** |
| `I_0` lattice (Wilson `r=1`, `ma=0.02`) | `0.0844` (line 1229); `0.0845` at `ma=0.02` on `64⁴` (line 1346) | `0.084341` (inf-vol), `0.084465` (`64⁴`) | **agree (<0.1%)** |
| `a_1` bundle traces | (used implicitly) scalar `+R/6`, Dirac `−R/3`, vector `−R/3` | same | **agree** |
| survival structure | `ξ_eff>1/6 ⟹ L<2 ⟹ m>e⁻¹Λ` (lines 1238–1240) | `L<2 ⟹ m>0.368Λ` (paper conv.) | **agree** |

## Block II — convention-dependent quantities (comparable only in one stated `Z` normalization)

The paper's `Z` is "the axis-TT induced kinetic coefficient per unit `4N`"
(lines 1209–1210). This repo's `Z` is the coefficient of `∫√g R` in the action
(`=1/(16πG_ind)`). They differ by a uniform factor `R_Z=2` (gate `P2-NORM-01`).
Rows below are shown in **both** normalizations.

| Quantity | Paper 2 v2.15 (quoted) | This repo (own `Z`) | This repo (paper `Z`, ÷2) | Agreement |
|---|---|---|---|---|
| `β_B` continuum | `1/(384π²)=2.64e-4` (eq. `betaB`) | `1/(192π²)=5.28e-4` | `2.64e-4` | **agree** (same in paper `Z`) |
| `β_B` lattice | `+2.50(13)e-4` (eq. `betaB`) | `5.44e-4` | `2.72e-4` | **agree** (`~5%` vs paper's cont., matching its own `5%`) |
| `β_F` | `1/(192π²)=5.28e-4` (line 1155) | `1/(96π²)=1.06e-3` | `5.28e-4` | **agree** |
| `β_V` (analytic) | `−3β_B=−1/(128π²)=−7.92e-4` (line 1287) | `1/(64π²)=1.58e-3` | `−7.92e-4` | **agree** (same in paper `Z`) |
| `G_c` continuum | `8π²/Λ²` (line 1221) | `8π²/Λ²` | (`Z`-independent) | **agree** |
| `G_c` lattice | `5.93` (lines 1229, 1351) | `5.928` (at `ma=0.02`) | (`Z`-independent) | **agree** |
| `4G_cβ_F` continuum | `1/6` (line 1222) | `1/3` | `1/6` | **agree** in paper `Z` |
| `4G_cβ_F` lattice | `0.013` (line 1230) | `0.025` | `0.012` | **agree** in paper `Z` |
| `ξ_ind` survival | `m>0.37Λ` (line 1239) | `m>0.287Λ` | `m>0.368Λ` | **agree** in paper `Z` |

Tolerance justifications: Block-I exact rows are symbolic equality; `I_0` matched
to `<0.1%` (this repo's numerical scatter `2e-5`); `β_B` lattice compared as a
`~few-%` extraction. Block-II rows agree exactly once expressed in the paper's
`Z` normalization; the apparent "`1/3` vs `1/6`" is entirely the `R_Z=2`
convention, not physics.

## Not computed this sweep

- **Lattice `β_V/β_B = −3.2(5)`** (eq. `betaVlat`): not reproduced. Its
  *discriminating power* is analyzed in gate `P2-BETAV-CIRC-01` (the target
  ratio is structure-dependent `−(k+2)`, so the test is not degenerate; full
  lattice reproduction is `OPEN`).

## Bottom line (corrected)

The independent recomputation **confirms Paper 2 v2.15** across the board once
normalizations and the `I_0` evaluation mass are matched: every
convention-independent quantity agrees (ratios, `I_0`, survival structure), and
every convention-dependent quantity agrees in the paper's own `Z` normalization.
The two open items are **bookkeeping** (the `R_Z=2` `Z`-definition, `P2-NORM-01`)
and a **methodological audit** (the `β_V` discriminating-power / circularity
question, `P2-BETAV-CIRC-01`) — neither disturbs the paper's central negative
conclusion that the minimal model fails its own survival condition.
