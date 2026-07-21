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

## 2026-07-19 — Accept the Paper 2 normalization/gap/βV-circularity follow-up

### Decision

Accept the Paper 2 normalization, gap, and βV-circularity follow-up at the
statuses currently recorded.

### Reason

Independent review confirmed:

* D1 correctly retracted as convention mixing;
* `P2-NORM-01` correctly resolves the factor of two as uniform `Z`-normalization
  bookkeeping (`R_Z = 2`; paper `4 G_c β_F = 1/6` internally consistent);
* `P2-GAP-01` correctly resolves the approximately `1.2%` discrepancy as a
  matched-mass issue;
* the analytic layer of `P2-BETAV-CIRC-01` is genuinely discriminating, with
  `R(k) = -(k + 2)`;
* the full lattice discrimination test has not been run, so the gate correctly
  remains OPEN;
* regression/mutation anchors are live;
* the complete suite passes.

### Evidence

* `reviews/claude/2026-07-19-paper2-followup.md`;
* branch `claude/paper-2-independent-verification-dysdp0` at
  `de754ea6d7aff94c253b29bb80aea9ebb70cd54f`;
* the relevant derivations, scripts, gate records, raw/processed results, and
  tests already committed on that branch.

### Consequences

* the follow-up conclusions may be cited at their current statuses;
* D1 must not be revived as a physical factor-of-two discrepancy;
* `P2-BETAV-CIRC-01` remains OPEN;
* Paper 3's numerical βV dependency remains unresolved/suspended;
* `P3-C-004` remains unaffected;
* nothing becomes VERIFIED;
* the next scientific gate is the full lattice Proca discrimination run for
  `k ≠ 1`.

### Supersedes

None, except that the D1 discrepancy is explicitly withdrawn by the
already-recorded D1 retraction (the 2026-07-17 "Retract D1" entry above).

### Related gate

`P2-NORM-01`, `P2-BETAV-CIRC-01`, `P2-GAP-01`; and the D1 retraction recorded in
the 2026-07-17 "Retract D1 (Weyl-vs-Dirac `β_F` \"disagreement\")" DECISION_LOG
entry (no separate gate ID exists for D1).

### Related branch and files

`claude/paper-2-independent-verification-dysdp0`;
`reviews/claude/2026-07-19-paper2-followup.md`, `DECISION_LOG.md`,
`PROGRESS.md`, `HANDOFF.md`.

## 2026-07-19 — `P2-BETAV-CIRC-01` blocked by provenance; the honest A/B split

### Decision

Set `P2-BETAV-CIRC-01` to `SUSPENDED` (blocked by provenance). Register two
honest, separately-labelled substitutes: `P2-BETAV-ASSEMBLY-01` (implementation
regression, `PASS` on its own terms) and `P2-BETAV-RECON-01` (clean-room
reconstruction, `PROPOSED`). Neither closes the circularity question.

### Reason

The circularity question is about the *historical Finding 5 lattice pipeline's*
projection/normalization. That pipeline is **not in the repository** — a
provenance search (`results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md`, verdict NOT
LOCATED) found no lattice 1-form operator, no Stueckelberg determinant, no
metric perturbation, no `h`-derivative/projection code, and no raw artifact.
`scripts/lattice_beta_scan.py` is the scalar `P2-BETA-01` tadpole and must not
be substituted for it. A pipeline that does not exist cannot be tested for
circularity.

The determinant-bookkeeping construction returns `−(k+2)` **by construction**:
the shared scalar integral cancels in the numerator/denominator ratio, so it has
no power to expose a circular historical projection. It is therefore recorded as
an implementation regression (`P2-BETAV-ASSEMBLY-01`), not as an answer to the
circularity question.

### Evidence

`results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md`; `scripts/betav_assembly.py`
(ratio variant spread `≤9e-16`, `C` cancels); `MIGRATION.md` ("no legacy
source").

### Consequences

* `P2-BETAV-CIRC-01` = `SUSPENDED` (the non-standard `OPEN` label is corrected to
  the allowed `SUSPENDED`); circularity neither demonstrated nor ruled out.
* `P2-BETAV-ASSEMBLY-01` = `PASS` (implementation only; does not close CIRC-01).
* `P2-BETAV-RECON-01` = `PROPOSED` (reconstruction ≠ historical test).
* Finding 5's `−3.2(5)` remains an unreproduced paper value.
* `3-vector-sector` `P3-C-004` rests on the `C_6 = −G_V/2` sign structure, not on
  `−3.2(5)`, and is unaffected; the `MIGRATION.md` flag stays as-is (that repo
  not read or edited).
* Nothing is promoted to `VERIFIED`.
* Next scientific gate: the full lattice Proca `k ≠ 1` discrimination run
  (`P2-BETAV-RECON-01`, or a located historical pipeline).

### Supersedes

The `OPEN`/`analytic-layer-discriminating` framing of `P2-BETAV-CIRC-01` in the
2026-07-17 gate record (it overstated the analytic bookkeeping's power). The
earlier entries are preserved.

### Related gate

`P2-BETAV-CIRC-01`, `P2-BETAV-ASSEMBLY-01`, `P2-BETAV-RECON-01`.

### Related branch and files

`gate/p2-betav-circ`; `results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md`,
`scripts/betav_assembly.py`, `derivations/P2-BETAV-*`.

## 2026-07-20 — βV pipeline recovered; revive P2-BETAV-CIRC-01 SUSPENDED → SPECIFIED

### Decision

The βV (Proca) pipeline is now complete and runs. Revive `P2-BETAV-CIRC-01`
from `SUSPENDED` to `SPECIFIED` (the discrimination `k`-scan is runnable but not
yet run). **No PASS/FAIL verdict is set.** `β_V/β_B = −3.2(5)` is **not**
promoted — it stays an unpromoted, quarantined paper value.

### Reason

The provenance block is removed: `mlog_coeff.py` (previously missing) is
recovered, so `proca_loop.py` runs. The pipeline reproduces the scalar `β_B`
(`+3.0e-4 → +2.82e-4`, converging into `+2.50…2.64e-4`) and the vector `β_V`
**sign** (`Z_V(m)` rises ⟹ `β_V<0`, Finding 5). The gate can no longer be
justified as provenance-blocked.

### Evidence

`scripts/recovered_2026/{mlog_coeff.py, proca_loop.py, reproduce_betav.py}`;
`results/recovered-2026/BETAV_REPRODUCTION.md`.

### Consequences

- `P2-BETAV-CIRC-01` = `SPECIFIED` (runnable, not run; no verdict).
- The βV *magnitude* at accessible grids is longitudinal-artifact limited
  (light-window ratio `−61` at `n=12`, `−16` at `n=16`; heavy window flips sign)
  — recovery does **not** reproduce `−3.2(5)`.
- `−3.2(5)` is **not** promoted to a verified claim; `P2-C9` stays `PROPOSED`.
  The quarantine holds until the `k`-scan discrimination test passes.
- `MIGRATION.md`'s "nothing can be re-run" is now fully superseded for Paper 2's
  gravity sector.
- No historical claim upgraded or downgraded by the recovery itself.

### Supersedes

The `SUSPENDED`/provenance-blocked disposition of `P2-BETAV-CIRC-01` (2026-07-19
entry), which was correct while the pipeline was missing. Preserved above.

### Related gate

`P2-BETAV-CIRC-01`, `P2-GRAV-ENGINE-RECOVERED-01`.

### Related branch and files

`recover/betav-complete`; `scripts/recovered_2026/`, `results/recovered-2026/`,
`GATES.md`, `MIGRATION.md`.

## 2026-07-20 — P2-BETAV-CIRC-01 Phase-1 decomposition: DECOMP-NOT-REPRESENTABLE

### Decision

The historical `k`-scan for `P2-BETAV-CIRC-01` **cannot be defined from the
recovered numerical pipeline alone.** Phase-1 adjudication verdict:
**DECOMP-NOT-REPRESENTABLE**. No `k`-scan is run.

### Reason

Operator-level analysis of the recovered `proca_loop.py` (evidence:
`scripts/betav_decomp_check.py`,
`derivations/P2-BETAV-CIRC-01_determinant-decomposition.md`):
1. The Proca longitudinal factor is the **ultralocal `m²`** eigenfactor of
   `M = (ŝ²+m²)δ − a⊗a*` (spread over `p̂²` is `3e-16`), **not** the propagating
   external scalar `Δ₀ = ŝ²+m²` of `boson_loop.py` (`1/m²` vs `1/(ŝ²+m²)`
   propagator; different `m²ln m²` content). So an external scalar loop cannot
   represent a change of compensator power.
2. The one-graviton vertex `δM` **mixes** transverse and longitudinal
   (`max|⟨T|δM|L⟩| = 0.17`), so the flat split `det M = m²(ŝ²+m²)³` does **not**
   lift to an invariant additive determinant decomposition on a curved
   background. No `Z_Proca + k·Z_scalar` construction reduces pointwise to
   recovered Proca while deforming the compensator power and avoiding
   double-count.
Secondary: every historical extraction step (TT recipes, `/5`, `fit_mlog`, ratio
by fixed `β_B`) is **linear**, so even the invalid algebraic scan would be
`LINEAR-ONLY` (bookkeeping, not circularity).

### Evidence

`scripts/betav_decomp_check.py`,
`results/P2-BETAV-CIRC-01/decomp/regen/decomp_check.json`,
`derivations/P2-BETAV-CIRC-01_determinant-decomposition.md`,
`reports/2026-07-20_betav-decomposition-adjudication_report.md`.

### Consequences

- The circularity question must be reformulated as an operator/determinant-
  identity audit (analytic gauge-fixed identity (d) vs recovered operator (a)),
  or addressed via `P2-BETAV-RECON-01` (clean-room operator) — **not** a `k`-scan
  on the recovered code. This is a real result, not a failure.
- Gate statuses **unchanged**: `P2-BETAV-CIRC-01` = `SPECIFIED`,
  `P2-BETAV-NUMREPRO-01` = `PROPOSED`, `P2-C9` = `PROPOSED`; the `−3.2(5)`
  quarantine is untouched.

### Supersedes

None (the withdrawn `Z_V + k·Z_scalar` k-scan draft was never committed; this
records why it is invalid).

### Related gate

`P2-BETAV-CIRC-01`, `P2-BETAV-RECON-01`.

### Related branch and files

`gate/p2-betav-decomp`; `derivations/P2-BETAV-CIRC-01_determinant-decomposition.md`,
`scripts/betav_decomp_check.py`, `results/P2-BETAV-CIRC-01/decomp/`.

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
