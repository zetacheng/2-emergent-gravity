# Decision Log

This log is append-only. New decisions must use the entry template below and
must not erase superseded decisions.

## 2026-07-15 — Separate the five papers into five repositories

### Decision

Maintain each paper in a dedicated repository, with this repository containing
Paper 2 only.

### Reason

Separate repositories preserve scientific scope, provenance, gate history, and
paper-specific review boundaries.

### Evidence

The Principal Investigator supplied a five-repository mapping during
infrastructure initialization.

### Consequences

Content from Papers 1, 3, 4, and 5 must not be imported here. Cross-paper work
must be referenced rather than merged.

### Supersedes

None.

### Related gate

None; infrastructure decision.

### Related branch and files

`main`; repository governance files.

## 2026-07-17 — Independent verification of Paper 2's load-bearing inputs

### Decision

Populate Paper 2's numbers by **independent recomputation** under
pre-registration discipline (compute and commit, then compare), not migration,
because Paper 2 has no legacy source (see `MIGRATION.md`). Record the outcome of
the first verification sweep (gates `P2-HK-01`, `P2-GAP-01`, `P2-BETA-01`;
`P2-BETAV-01` deferred).

### Reason

Paper 2's headline numbers had no script, archived result, or provenance. A
fresh first-principles computation is the only way to check them, and the
pre-registration rule prevents unconsciously tuning toward the paper.

### Evidence

- `P2-HK-01` (symbolic): `β_B=−1/(192π²)`, `β_F=−1/(96π²)`, `β_V=+1/(64π²)`;
  ratios `β_F/β_B=2`, `β_V/β_B=−3`, `β_B(ξ)/β_B=1−6ξ`.
- `P2-GAP-01`: continuum `G_c=8π²/Λ²` (`c=8` exact); lattice `I_0=0.085388(20)`,
  `G_c=5.856`.
- `P2-BETA-01`: lattice `β_B=5.44e-4` (`+3.1%` of continuum).
- Comparison: `results/comparison/PAPER_COMPARISON.md`.

### Outcome

- **Agree:** `β_B` (continuum exact, lattice few-percent), `β_V/β_B=−3` (exact),
  continuum `G_c` (`c=8`).
- **Disagree (recorded, reviewer to adjudicate):**
  (1) `β_F` by exactly ×2 — Dirac (`1/96π²`, this repo) vs Weyl (`1/192π²`,
      paper); propagates to `4G_cβ_F` (`1/3` vs `1/6`) and the survival window
      (`m>0.287Λ` vs `0.368Λ`). **Load-bearing.**
  (2) lattice `I_0`/`G_c` by ≈1.2% (outside my numerical uncertainty).
- The paper `.tex` was not supplied; comparison used the transcribed numerical
  claims. Import `emergent_gr_paper_v2_15.tex` and re-check when available.

### Consequences

No claim is `VERIFIED` (no reviewer record, no provenance). Disagreements are
`INCONCLUSIVE` with both values recorded; the un-run lattice Proca ratio is
`PROPOSED`. Candidate reconciliations (e.g. Weyl vs Dirac) are recorded
separately from the disagreements and are **not** adopted as the finding.

### Supersedes

None (extends the 2026-07-15 repository-scope decision).

### Related gate

`P2-HK-01`, `P2-GAP-01`, `P2-BETA-01`, `P2-BETAV-01`.

### Related branch and files

`claude/paper-2-independent-verification-dysdp0`; `scripts/`, `derivations/`,
`results/`, `CLAIMS.md`, `GATES.md`, `results/comparison/PAPER_COMPARISON.md`.

## 2026-07-17 — Retract D1 (Weyl-vs-Dirac `β_F` "disagreement")

### Decision

Withdraw the first report's headline disagreement D1. Supersede the
`INCONCLUSIVE` `β_F` claim; the recomputation **agrees** with Paper 2 v2.15.

### Reason

Comparison across normalizations. The paper source
(`paper/emergent_gr_paper_v2_15.tex`) — unavailable at the first comparison —
states `β_B^cont = 1/(384π²)` (eq. `betaB`) and `β_F = 2β_B = 1/(192π²)`
(line 1155). The paper's `β_F/β_B = 2`, identical to this repo's. The
"factor 2" is a *uniform* normalization of `Z` (coefficient of `R` in the action
vs axis-TT slope per unit `4N`), not a species-content (Weyl-vs-Dirac)
difference: this repo's `β_B` is *also* `2×` the paper's, so species content
cannot explain it. Consequently the `1/6` vs `1/3` for `4G_cβ_F` was an artifact
of mixing this repo's `Z` (for `β_F`) with the paper's `G_c` — retracted.

### Evidence

`scripts/normalization_chain.py` (gate `P2-NORM-01`): `R_Z = 2` uniformly across
scalar, Dirac, Proca; `4G_cβ_F = 1/6` in the paper's convention.

### Consequences

`P2-C2` and `P2-C8` move from `INCONCLUSIVE` to `SUPPORTED`. The physics is
unchanged: `ξ_ind < 0` for `L ≫ 1` in either convention.

### Supersedes

The `β_F`/`4G_cβ_F` disagreement recorded in the 2026-07-17 verification-outcome
entry above. That entry is preserved, not deleted.

### Related gate

`P2-NORM-01`, `P2-HK-01`.

### Related branch and files

`results/comparison/PAPER_COMPARISON.md`, `derivations/P2-NORM-01_normalization_chain.md`.

## 2026-07-17 — Resolve the `I_0` comparison (evaluation mass, not disagreement)

### Decision

Withdraw the first report's D2 (lattice `I_0` ≈1.2% "disagreement"). At matched
convention the recomputation **agrees** with Paper 2 v2.15.

### Reason

The paper evaluates `I_0` with the Wilson term `W = m + Σ(1−cos p)` at a small
reference fermion mass `ma = 0.02` (its "`0.0845 at ma=0.02 on 64⁴`", line 1346),
not in the strict massless limit used in the first report. The reference mass
lowers `I_0` by ≈1.2%.

### Evidence

`scripts/gap_criticality.py` `reference_mass_evaluation`: `I_0(ma=0.02) =
0.084341` (inf-vol), `0.084465` (`64⁴`), `G_c = 5.928` — vs paper `0.0844`,
`0.0845`, `5.93` (`<0.1%`). The under-convergence hypothesis was tested and
rejected (coarse grids do not cleanly reproduce `0.0844`).

### Consequences

`P2-C6` moves from `INCONCLUSIVE` to `SUPPORTED`. `P2-GAP-01` status → `PASS`.
This is a correction to the first report, not to the paper.

### Supersedes

The `I_0`/`G_c` disagreement (D2) in the 2026-07-17 verification-outcome entry.

### Related gate

`P2-GAP-01`.

### Related branch and files

`scripts/gap_criticality.py`, `results/P2-GAP-01/`.

## Entry template

```markdown
## YYYY-MM-DD — Decision title

### Decision

### Reason

### Evidence

### Consequences

### Supersedes

### Related gate

### Related branch and files
```
