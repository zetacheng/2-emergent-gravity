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

## 2026-07-20 — P2-BETAV-CIRC-01 Phase-1 REVISION: narrow verdict to DECOMP-UNAVAILABLE-AS-RECOVERED

### Decision

Supersede the verdict token of the 2026-07-20 Phase-1 adjudication: replace
`DECOMP-NOT-REPRESENTABLE` with the narrower, machine-parseable
**`DECOMP-UNAVAILABLE-AS-RECOVERED`**. The practical conclusion is unchanged
(do not run the additive k-scan); the supports are tightened.

### Reason

Review found the original inseparability support rested on a transverse–
longitudinal mixing measured in the wrong (single-momentum) basis. A correct
`q²`-level sector decomposition in the proper bubble basis
(`scripts/betav_decomp_q2.py`, `m=0.3`, `n∈{10,12}`, three q-ranges; sectors sum
to total to `<1e-12`) shows:
- the one-graviton vertex mixing `U_TL` **vanishes as `q→0`** (earlier 0.17
  figure withdrawn); **but**
- the mixed **bubble** contributes at `O(q²)` (scaling exp `≈1.98`): the mixed
  `q²` coefficient is **nonzero** (`≈+9e-5`) and basis/grid-stable — yet
  **small**, `≈0.4%` of the total `Z` (TT `≈96.5%`, LL `≈3.1%`).
So the induced `Z` admits only an *approximate* T/L split; an exact invariant
additive split fails at the `≈0.4%` level. The seagull is `q`-independent
(structural) and does not enter the `q²` slope.

The two solid supports are retained: (a) the additive `Z_V+k·Z_S` design is
invalid and would be `LINEAR-ONLY`; (b) the external `boson_loop` scalar
(`Δ₀=ŝ²+m²`) is not the flat Proca longitudinal eigenfactor (`m²`) and cannot be
substituted without an extra identity. Language re-neutralized (no "compensator
sector" premise; the flat `ln m²`→induced-log inference downgraded; the
continuum-Stueckelberg equivalence marked **unestablished**, not refuted).

### Evidence

`scripts/betav_decomp_q2.py`,
`results/P2-BETAV-CIRC-01/decomp/regen/decomp_q2.json`,
`derivations/P2-BETAV-CIRC-01_determinant-decomposition.md`,
`reports/2026-07-20_betav-decomposition-adjudication_report.md`.

### Consequences

- Verdict token: `DECOMP-UNAVAILABLE-AS-RECOVERED`. A clean-room lattice
  Stueckelberg / gauge-fixed construction is **not excluded**.
- Gate `P2-BETAV-CIRC-01` uses separated fields (Status `SPECIFIED`; design
  adjudication `DECOMP-UNAVAILABLE-AS-RECOVERED`; additive k-scan `WITHDRAWN`);
  the CIRC gate has not passed or failed.
- Unchanged: `P2-BETAV-NUMREPRO-01` = `PROPOSED`, `P2-C9` = `PROPOSED`, `−3.2(5)`
  quarantined. `CLAIMS.md` untouched.

### Supersedes

The verdict token `DECOMP-NOT-REPRESENTABLE` of the 2026-07-20 Phase-1 entry
above (that entry is preserved; only the token and the mixing support are
revised).

### Related gate

`P2-BETAV-CIRC-01`, `P2-BETAV-RECON-01`.

### Related branch and files

`gate/p2-betav-decomp`; `scripts/betav_decomp_q2.py`,
`derivations/P2-BETAV-CIRC-01_determinant-decomposition.md`,
`reports/2026-07-20_betav-decomposition-adjudication_report.md`, `GATES.md`.

## 2026-07-21 — Batch-2 recovery: Solodukhin-quotient object recovered; Ward summary recorded not adopted

### Decision

Record the batch-2 recovery of historical originals (gauge-fixed vector
`gfvec_loop.py`, the precision driver, Fierz/HS foundations, and the
Wilson-frame & overlap eras) and add a **dated addendum** to `P2-BETAV-CIRC-01`.
The addendum notes that the registered operator/determinant-identity audit now
has a **concrete recovered object** — the Solodukhin quotient
`Γ_Proca = Γ_minvec − Γ_scalar(m)` in `gfvec_loop.py`. **No gate status changes;
the Phase-1 verdict token `DECOMP-UNAVAILABLE-AS-RECOVERED` is not altered.**
Separately record `ward_analysis_summary.txt` as a historical results document
whose claims are **recorded, not adopted**.

### Reason

The Phase-1 adjudication said a clean-room gauge-fixed construction was "not
excluded" but unavailable from the then-recovered set. Batch-2 shows such a
construction existed historically. This does not reopen the verdict (which was
correct for the additive scan on the then-recovered `proca_loop`/`boson_loop`
set); it gives the *reformulated* audit an object to run against.

### Evidence

`scripts/recovered_2026/batch2/` (13 originals, sha256 in `PROVENANCE.md`);
constant-`h` machinery validated to `~1e-7` (`n=6,8`, `m=0.5`) and Fierz
foundations self-validated
(`results/recovered-2026/BATCH2_VALIDATION.md`). `precision_campaign.py` **not
run** (hours; embeds `−2.000`/`−3.000` targets → blind harness required).

### Consequences

- `P2-BETAV-CIRC-01` = `SPECIFIED` (unchanged); audit PASS/FAIL/INCONCLUSIVE
  rules still to be pre-registered; any β run must use a blind harness.
- `P2-BETAV-NUMREPRO-01` = `PROPOSED`, `P2-C9` = `PROPOSED`, `−3.2(5)`
  quarantined — all untouched. `CLAIMS.md` untouched.
- `ward_analysis_summary.txt` claims (`Z_cov < 0`; positive axis slope entirely
  the non-covariant `c4` piece) are recorded but **must not be cited as
  established**; the generating Ward vierbein-link kernel is registered missing
  (`scripts/recovered_2026/MISSING.md`, item 1).

### Supersedes

Nothing. The Phase-1 entries and their token stand; this only adds an addendum
and provenance.

### Related gate

`P2-BETAV-CIRC-01` (addendum), `P2-BETAV-NUMREPRO-01`, `P2-BETAV-RECON-01`.

### Related branch and files

`recover/batch2-gfvec-and-foundations`; `scripts/recovered_2026/batch2/`,
`scripts/recovered_2026/PROVENANCE.md`, `scripts/recovered_2026/MISSING.md`,
`results/recovered-2026/BATCH2_VALIDATION.md`,
`results/recovered-2026/ward_analysis_summary.txt`,
`results/recovered-2026/emergent_gr_paper_v2_7.tex`, `GATES.md`.

## 2026-07-21 — Full session log landed; −3.2(5) provenance pinned (quarantine enforces the programme's own criterion)

### Decision

Land the recovered **complete historical session log**
(`results/recovered-2026/session_log_full.md`, byte-for-byte, sidecar SHA256)
and record, in `PROVENANCE.md`, a **run-record index** of every number the log
reports — each labelled *historically reported, not independently verified*. No
gate status changes; `P2-C9` and the `−3.2(5)` quarantine are untouched.

### Reason

The log resolves several open provenance questions: it pins the `−3.2(5)` run
configuration(s), confirms `precision_campaign.py` was never executed, and
records that the historical runs were not blind (targets `−2`,`−3` were known).
**The historical programme itself evolved its standards over time: target-aware
exploration → a designed precision campaign → the present blind preregistration
and dual-gate discipline. This is recorded as natural maturation of the
programme's own standards, not as a past-wrong/now-right judgment.**

### Convergent evidence, not mutual verification

Two independent lines of reasoning (the historical session's artifact-driven
design path and the modern Phase-1 operator adjudication) converged on the same
engineering decision (a gauge-fixed / Stueckelberg minimal-vector construction).
**This is convergent evidence for the design direction, not mutual verification
of any numerical result** — `−3.2(5)` and every other run-record number stay
historically reported and quarantined.

### Evidence

`session_log_full.md` (73853 bytes, SHA256
`61c54701d7e61f31168aaadd0a6ee70c964f4b2175e92c1d9dd3a02749303a9c`): Proca
`β_V=−7.2×10⁻⁴` at `n=32`, `m_V a=0.11–0.20`, ratio `−3.2(5)` (L219–220);
gfvec `−2.4…−2.9` over `0.125–0.55` (L229); `Π_V(0)=+0.297/+0.264/+0.228`
matching `batch2/calibrate.py`; finite-q `0.500000` validation (script not
recovered).

### The pre-stated-criterion sentence (recorded as required)

**The historical promotion criterion was pre-stated and never met**: the
session's own standard was that the scenario upgrades to "lattice-established"
only if the precision campaign lands both ratios at `−2.00` and `−3.00`, and
that campaign never ran. **The current `−3.2(5)` quarantine therefore enforces
the programme's own historical criterion, not a retroactive standard.**

### Consequences

- `precision_results.json` reclassified as the **output of a never-run
  computation** (`MISSING.md` #2); the `n=32` session item is **resolved on the
  session side** (#3); a new missing item (#6) is the finite-q validation script.
- `P2-BETAV-NUMREPRO-01` gains a dated note pinning the historical target
  configuration as pre-registration input (status stays `PROPOSED`).
- Any future β run must use a **blind harness** (targets embedded in the
  historical files and known historically).

### Supersedes

Nothing. Adds provenance and an index; the Phase-1 verdict/token and all gate
statuses stand.

### Related gate

`P2-BETAV-CIRC-01`, `P2-BETAV-NUMREPRO-01`, `P2-C9` (unchanged).

### Related branch and files

`recover/batch2-gfvec-and-foundations`;
`results/recovered-2026/session_log_full.md` (+`.sha256`),
`scripts/recovered_2026/PROVENANCE.md`, `scripts/recovered_2026/MISSING.md`,
`GATES.md`, `reports/2026-07-21_recovery-batch2_report.md`.

## 2026-08-01 — Register P2-LATTICE-ONTOLOGY-01 as a Paper-2 specification gate

### Decision

Register `P2-LATTICE-ONTOLOGY-01` as `SPECIFIED` in Paper 2. This is a
specification and obligation-linkage gate; it authorizes no computation and
issues no physical PASS/FAIL verdict.

### Reason

The pinned concept note makes explicit the programme's physical-H(4)-substrate
declaration and its downstream obligations. The Discriminator approved the
pinned version for registration as SPECIFIED, not for gate completion.

### Evidence

- `derivations/P2-LATTICE-ONTOLOGY-01.md`, SHA-256
  `1a03870eb5a24a748f3803e066a281dbbe4b64fa67860dad32409b41c0660b5c`.
- `reviews/claude/2026-08-01-p2-lattice-ontology-01.md`, SHA-256
  `83e3387316922d0c22812affeec6935a5ba4cb9b8bea17f59e58cc1049ca65fa`.
- Exploratory, non-canonical probe: `scripts/euclidean_reconstruction.py`,
  SHA-256 `30e3b59a0006b2ecc2d6ecce391ab918ce9ba542b2af649c55570e0643e63a78`.
- All artifacts migrated byte-identically from `0-programme`
  `programme/p2-lattice-ontology-01` at
  `315451829412067f2e86d3559975e36b1b2ee03c`.

### Consequences

Cross-paper force awaits a separately ratified summary in `0-programme`.
`P2-LATTICE-MICROSPEC-01` remains a required unregistered subordinate artifact;
SI-2 remains blocked; and no Phase-B, Route-D D0, FIERZSUM, promotion, or
quarantine action is created by this registration.

### Supersedes

None.

### Related gate

`P2-LATTICE-ONTOLOGY-01`.

### Related branch and files

`gate/p2-lattice-ontology-01`; `GATES.md`,
`derivations/P2-LATTICE-ONTOLOGY-01.md`,
`scripts/euclidean_reconstruction.py`, and
`reviews/claude/2026-08-01-p2-lattice-ontology-01.md`.

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

## 2026-07-25 — Register P2-ACT-CANONICAL-ALIGN-01

### Decision

Register `P2-ACT-CANONICAL-ALIGN-01` as a mandatory manuscript-alignment
action.  The Paper-2 manuscript must display the ratified generator-sum
interaction or state unambiguously that its singlet notation is shorthand for
the complete generator contraction.

### Reason

`derivations/CANONICAL_INTERACTION.md` is the ratified governing source for
the Paper-2 canonical interaction.  Its historical manuscript presentation
requires explicit expository alignment; this entry tracks that required action
without editing the manuscript in this task.

### Evidence

- Ratified source: `derivations/CANONICAL_INTERACTION.md`, SHA-256
  `27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81`.
- Landing evidence: `reports/2026-07-25_canonical-interaction_evidence.md`.

### Consequences

The identifier is hereby registered.  No Paper-2 manuscript source is edited
by this tracking entry; manuscript alignment remains a separately authorized
action.

### Supersedes

None.

### Related gate

`P2-CHANNEL-FREEZE-01` (downstream consumer of the ratified interaction).

### Related branch and files

`docs/canonical-interaction`; `derivations/CANONICAL_INTERACTION.md`,
`reports/2026-07-25_canonical-interaction_evidence.md`, `DECISION_LOG.md`.

## 2026-08-01 — Record Arm H procedural deviation and verdict-retention determination

### Decision

The PI determined that the `P2-BETAV-NUMREPRO-01` Arm-H verdict remains
recorded as `INCONCLUSIVE`, rather than withdrawn. This entry records the
approved audit and review conclusions; it adopts no forward governance rule.
A separate governance amendment is to address this class of situation.

### Reason

The repository audit established that `fef78fc` modified
`tests/test_si1_governance.py` without authorization, but did not modify the
harness, comparator, schema, raw artifact, or comparison artifact. The audit
also established that the compute and comparator artifacts were committed before
the edit, and that the replacement test reads `GATES.md` only and is not on the
verdict-producing code path.

The review concluded that the replacement governance test did not weaken the
governance checks. Relocating that test change would require history rewriting,
which merge discipline forbids; the edit itself was therefore retained.

### Evidence

- `fef78fc`: changed `GATES.md` and `tests/test_si1_governance.py` only.
- `ab36ca4`: Arm-H frozen compute artifact commit; `da62d44`: Arm-H comparison
  artifact commit; both precede `fef78fc` in the commit graph.
- `9b0ceed`: governance correction identifying the deviation and retaining the
  test change; `3c0c484`: reviewed merge carrying that correction.
- Discriminator identification and PI authorization of the correction round are
  recorded in `reports/2026-07-22_betav-arm-h-decisive_report.md`.

### Consequences

The documented procedural deviation and the retained `INCONCLUSIVE` verdict are
recorded without changing any script, test, schema, raw artifact, comparison
artifact, gate status token, artifact digest, or verdict field. The forward-rule
topic is reserved for the separate governance-amendment task.

### Supersedes

None. This entry cross-references, but does not erase, the correction record in
`9b0ceed`.

### Related gate

`P2-BETAV-NUMREPRO-01`; `P2-BETAV-CIRC-01`; `P2-C9`.

### Related branch and files

`fef78fc`, `9b0ceed`, `3c0c484`;
`GATES.md`, `DECISION_LOG.md`, and
`reports/2026-07-22_betav-arm-h-decisive_report.md`.

---

## 2026-08-01 — Governance amendment adopted: execution discipline

### Decision

ADOPTED. Paper 2 adopts seven prospective execution-discipline rules in
`CONVENTIONS.md`: contradiction-stop; scope precedence; normative declared
frozen scope; execution-prompt archival and hashing; minimum mandatory merge
discipline; reporting honesty for merges; and evidence precedence.

Rule 1 is promoted from the existing 2026-07-22 decisive-run report rather
than newly created. The review rulings settled that the rules belong in
`CONVENTIONS.md`; that a declared-scope checker is a separate implementation
task rather than a manual procedure replacement; that decisive-run evidence
requires both the committed prompt and its recorded hash; that the merge rules
are mandatory rather than a template; and that this amendment applies at the
Paper 2 level only.

### Rationale

The amendment makes the already approved execution expectations discoverable
and explicit without changing any scientific result or gate interpretation.
A scope-checker script remains to be implemented separately.

### Scope limits

These rules are prospective only. This amendment creates no retrospective
action and alters no previously approved scientific result.

### Templates followed

This entry follows the 2026-07-15 and 2026-07-17 decision-log entry format.

### Related files

`CONVENTIONS.md`; `AGENTS.md`; `.gitignore`;
`reports/2026-07-22_betav-arm-h-decisive_report.md`.

---

## 2026-08-03 — Governance amendment adopted: role separation and outcome-based tasks

### Decision

ADOPTED. Paper 2 adopts prospective rules 8–12 in `CONVENTIONS.md`:
responsibility separation (the section's root rule); outcome-based task
specification; self-correction authority and its limit; task granularity and
the integration boundary; and mechanically checkable acceptance criteria.

### Rationale

The amendment records the approved responsibility boundary: specifications
define objectives, invariants, and acceptance criteria; executors determine
implementation; reviewers assess specifications before execution and resulting
evidence afterwards. The default task classification is MATERIAL.

Two prerequisites remain unbuilt: a standardized merge authorization/tool for
rule 11's integration boundary, and a changed-file scope checker for rule 12.
The section is programme-wide in intent, but is landed in Paper 2 pending
ratification of an approved summary into `0-programme`.

### Scope limits

These rules are prospective only. This amendment creates no retrospective
action and alters no previously approved scientific result.

### Templates followed

This entry follows the 2026-08-01 execution-discipline amendment and the
repository decision-log template.

### Related files

`CONVENTIONS.md`; `DECISION_LOG.md`;
`reviews/pi/2026-08-03-outcome-based-task-specification-amendment.md`.

---

## 2026-08-04 — Record `P2-PHASE-01` dependency ruling and separate prerequisites

### Decision

The PI rules that `P2-PHASE-01`'s dependency on
`P2-CHANNEL-FREEZE-01` is satisfied by the Phase-A freeze. Phase A supplies the
frozen channel basis and identifies scan-eligible microscopic coordinates.
Phase B is not a prerequisite of SI-1 phase enumeration: it governs the SI-2
CLEAN-PASS metric and verdict tiers.

The microscopic parameter domain is a third requirement, distinct from both
freeze phases and frozen by neither. The gate's former attribution of that
domain to `P2-CHANNEL-FREEZE-01` is superseded. Two requirements remain open:
creation, review, and formal adoption of a frozen MICROSCOPIC PARAMETER DOMAIN
artifact; and creation, review, and formal adoption of a PHASE INPUT /
ADMISSIBILITY CONTRACT. These are labels, not gate IDs, and neither label is a
registered gate. `P2-PHASE-01` remains PROPOSED and not runnable.

### Reason

The evidence distinguishes three previously conflated matters: (a) scannable
coordinates — Phase A freezes one genuine coordinate `G`, classifies
`HS_scale` and `Fierz_basis` as non-scan-eligible auxiliary parameters, and
freezes the five HS families and `K_ij` registry; (b) coordinate bounds — the
range of `G`, cutoff ratios, and finite-density `μ`, frozen by neither phase;
and (c) SI-2 result judgement — the Phase-B CLEAN-PASS metric and verdict
tiers. SI-1 requires (a) and (b), not (c).

The inventory also finds no defined `Γ[Φ_i]`, finite-density prescription,
bounded parameter domain, or operational Hessian positivity, free-energy,
global-preference, metastability, susceptibility, causality/unitarity, or
finite-density admissibility criterion. The only criteria-like text is a
PROPOSED 0-programme policy and it supplies no bounds.

### Evidence

- `reviews/codex/2026-08-04-p2-phase-01-feasibility-inventory.md`, SHA-256
  `34163b1276a88b434987da4fa98f4099fc07c2a5a843dd03a1861236f94a50fc`.
- `GATES.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`.
- `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` @
  `1e8d56da124c2ae791fb7a00b23a188d329c56f8`.
- `derivations/P2-SI1-UNBLOCK-01.md` @
  `1e8d56da124c2ae791fb7a00b23a188d329c56f8`.

### Consequences

No parameter domain, numerical bound, scan axis, admissibility criterion, or
physics method is registered or defined by this ruling. No gate status,
verdict, artifact digest, or hash-pinned artifact changes.

### Supersedes

The operative `P2-PHASE-01` wording that attributed the parameter domain to
`P2-CHANNEL-FREEZE-01`; the former wording is preserved in `GATES.md` as
historical / superseded text.

### Related gate

`P2-PHASE-01` (SI-1); `P2-CHANNEL-FREEZE-01`; `P2-MULTIPHASE-GRAV-01` (SI-2).

### Related branch and files

`governance/p2-phase-dependency-ruling`; `GATES.md`; `DECISION_LOG.md`;
`reviews/codex/2026-08-04-p2-phase-01-feasibility-inventory.md`.

## 2026-08-05 — Governance amendment adopted: execution environment and rule refinements

### Decision

ADOPTED. Paper 2 adopts rule 13, Execution environment, in
`CONVENTIONS.md`, and records the declared machine-specific execution
configuration in `docs/local/`. Rule 13 establishes a standing authorization
to restore the declared environment, while preserving the boundary that a
restoration does not change its declaration or license repository changes.

Rules 8–12 are refined: roles must not be assigned on callers' behalf;
prohibitions state what they protect; acceptance criteria are conditional on
offered choices; mid-task authorizations are recorded; and criteria and their
repository-derived literals are checked for satisfiability and integrity before
issue.

### Rationale

The amendments record the response to recurring specification-scope and
execution-environment failures. Each refinement names its originating incident
in the amended rule so that its continuing necessity remains reviewable.

### Scope limits

Rule 13 distinguishes repository content from the execution environment; it
does not authorize changing either a declaration or repository configuration.
The machine configuration is local rather than portable policy. No scientific
result, gate, status, verdict, artifact digest, or hash-pinned artifact changes.

`environment_guard` remains unbuilt queued work; this amendment does not build
or imply its implementation.

### Templates followed

This entry follows the 2026-08-01 execution-discipline amendment and the
repository decision-log template.

### Related files

`CONVENTIONS.md`; `DECISION_LOG.md`; `docs/local/README.md`;
`docs/local/execution_environment.md`.

## 2026-08-06 — Adopt the function-based role model and record the dual-executor arrangement

### Decision

Roles in this programme are **functions**, not fixed agents, and their
assignments are current and change by PI instruction. `AGENTS.md` and
`reviews/README.md` now state the function-based model — PI, Researcher,
Reviewer, Executor — with current assignments, and record the two-executor
arrangement together with the capability difference that makes the two
executors non-interchangeable. Records created or substantively amended
after this decision must state the function under which they were produced.

Record fields:

    Date: 2026-08-06
    Decision owner: Principal Investigator
    Superseded documents: AGENTS.md role section; reviews/README.md
    Effect: prospective only
    No retrospective relabelling of existing reviews/ records
    Reference: CONVENTIONS.md rule 8
    Specification SHA-256: f8409394fa6afc634daeb9df0d28b2fb7a1795569bd28dae6c548e3ec3779fdd
    Specification path: specs/2026-08-06T0456Z_role-model-and-executors.md

### Reason

An independent review found a live conflict inside the repository:
`AGENTS.md` and `reviews/README.md` assigned fixed roles that contradicted
the arrangement actually in use, while `CONVENTIONS.md` rule 8 already
stated that these are functions rather than fixed assignments to a
particular agent — and no committed artifact said that rule 8 superseded
the older text. Any further governance work would have been built on that
contradiction.

### Evidence

The approved specification is committed at
`specs/2026-08-06T0456Z_role-model-and-executors.md`, whose committed-blob
SHA-256 is recorded above. The superseded role text is preserved verbatim in
labelled historical subsections of `AGENTS.md` and `reviews/README.md`.

### Consequences

Effect is prospective only. No gate status, reviewer verdict, artifact
digest, claim, or scientific result changes, and `CONVENTIONS.md` is
byte-identical across this change: no rule is created, renumbered, or
reworded. Existing records under `reviews/` remain valid historical evidence
and are not relabelled. Going forward, a task specification whose acceptance
criteria can only be met on one executor should say so.

### Supersedes

The `## Role separation` bullets of `AGENTS.md` and the role sentences of
`reviews/README.md` as they stood at
`a0e9d11b7281f0c2185aa8d517bae009ab54807f`. Both are preserved, not deleted.

### Related gate

None. This is a governance record and touches no gate.

### Related branch and files

`review/role-model-and-executors`; `AGENTS.md`, `reviews/README.md`,
`HANDOFF.md`, `PROGRESS.md`, `DECISION_LOG.md`,
`specs/2026-08-06T0456Z_role-model-and-executors.md`.

## 2026-08-07 — Fierz matrix sign convention: `matrix_rational` is stored unsigned

Date: 2026-08-07
Decision owner: Principal Investigator
Effect: supplies a definition absent from the frozen material

### Decision

The PI ruling of 2026-08-07, reproduced verbatim:

> **PI ruling, 2026-08-07 — Fierz matrix sign convention.**
>
> `matrix_rational` stores the Dirac/internal exchange matrix **without**
> the operator-level Grassmann crossing factor. The four-fermion operator
> exchange is therefore
>
>     K_exch = s_G · M · K_direct,     s_G = -1
>
> The declared `grassmann_crossing_sign` is applied **exactly once at
> operator use**. The existing double application in
> `basis_freeze_check.py` is an ineffective validation and does not
> define the storage convention.

In short: s_G = -1, applied exactly once at operator use;
matrix_rational is stored unsigned; and the
basis_freeze_check.py double application is ineffective validation.

### Reason

Not a recovery of original intent. The executor established that no
defining kernel equation exists anywhere in the frozen material —
`K_exch`, `K_direct`, `defining equation` and `kernel equation` all occur
zero times, verified independently. The ruling rests on three pieces of
indirect evidence — an unsigned reconstruction matches the frozen
entries; the checker's net effect is `+1`; the sign is declared as a
separate convention field — **none of which is a defining equation**. The
ruling therefore supplies a definition the freeze never carried, rather
than recovering one it did. A record claiming otherwise would overstate
the evidence.

### Evidence

`derivations/P2-CHANNEL-FREEZE-01_grassmann_crossing_sign.md` and
`results/P2-CHANNEL-FREEZE/grassmann-crossing-sign/crossing_sign.json`
establish the operator-level sign `s_G = -1` by explicit four-fermion
exchange under a frozen permutation, by four independent routes, and
record the storage convention as unresolved on the frozen material.
`reports/2026-08-07T1159Z_grassmann-crossing-sign.md` reports both.

### Consequences

Consequence: P2-PHASE-01 induced V and A coefficients are -G/4 at the
operator level, the singlet values reported as `+G/4` at the matrix level
in `reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md`
acquiring the factor `s_G = -1` exactly once. The structural results are
unaffected: S, P and T vanish; V and A are equal and purely singlet; the
exchanged form is purely left-right with `LL = RR = 0`.

Neither original report was altered. The consequence is recorded in
`derivations/P2-PHASE-01_fierz_sign_addendum.md`.

Freeze repair (tenth mutation, checker correction, vocab_parser pin) is
queued as a separate task and is NOT performed here.

### Related gate

None. This ruling changes a convention, not a gate. `P2-CHANNEL-FREEZE-01`
remains `PROPOSED` and `P2-PHASE-01` remains `PROPOSED`.

### Related branch and files

`gate/p2-integrate-fierz-and-sign-ruling`;
`derivations/P2-PHASE-01_fierz_sign_addendum.md`, `DECISION_LOG.md`,
`specs/2026-08-07T1320Z_integrate-fierz-and-sign-ruling.md`.

## 2026-08-07 — Branch-deletion policy adopted; pre-deletion authorization recorded

Date: 2026-08-07
Decision owner: Principal Investigator
Effect: adds a lifecycle rule; authorizes nothing to be deleted yet

### Decision

`docs/BRANCHING_POLICY.md` previously said nothing about deletion. It now
carries a **Branch lifecycle** section with four cases — merged with the
tip recoverable as a merge parent; merged with the tip not a merge
parent; unmerged; and explicitly preserved — together with the rule that
**every deletion is recorded in two committed steps**: an authorization
record before, and a finalized record after.

Deletion proceeds in three stages with hard boundaries. Stage 1, this
entry, lands the policy and the authorization record. **Stage 2 deletes
nothing until Stage 1 is merged into `main`**, so that the record of what
was to be deleted is permanent before the irreversible act. **Stage 3
finalizes the record with what was actually deleted**, because a record
of intent is not a record of outcome.

### Evidence

`docs/BRANCH_DELETION_RECORD_2026-08-07.md` carries one entry per branch
in the deletion set, each with its name, tip SHA, merge commit,
live-verified merge status and deletion status. Every value was computed
from the repository and the live remote, not transcribed.

The deletion set is **26 listed branches**, of which **25 are present on
the remote and all 25 verified as ancestors of `main`**, giving 25
`PENDING_DELETE` entries. **No listed branch failed the merge check.**
The single `NOT_AUTHORIZED` entry, `gate/p2-integrate-fierz-and-sign-ruling`,
is unauthorized because it is absent from the remote, never having been
pushed; its local ref equals `main`, so nothing is at risk.

One branch on the remote is not in the deletion set —
`fix/freeze-checker-sign-repair`, pushed after the specification was
written and awaiting its own review. It must not be deleted.

### Consequences

Nothing is deleted by this entry. Twenty-five refs become eligible for
deletion once Stage 1 is merged; their content, grouping and tip SHAs
survive in the merge commits on `main`, and their names survive in the
record. What deletion costs is the human-readable name, which the record
preserves more durably than a ref does.

**`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` is permanently preserved.** It
is unmerged, so deleting it would destroy content rather than a name. It
appears in no deletion set at any stage, and is verified before and after
every deletion loop.

### Related gate

None. This is a repository-hygiene policy and changes no gate or
scientific status.

### Related branch and files

`fix/branch-deletion-policy`;
`docs/BRANCHING_POLICY.md`, `docs/BRANCH_DELETION_RECORD_2026-08-07.md`,
`DECISION_LOG.md`, `specs/2026-08-07T1437Z_branch-deletion-policy.md`.

## 2026-08-07 — Branch-deletion policy amended: `ABSENT_FROM_REMOTE` and remote-refs-only authority

Date: 2026-08-07
Decision owner: Principal Investigator
Effect: closes two governing gaps; authorizes no deletion

### Decision

Two amendments to the **Branch lifecycle** policy adopted earlier the
same day.

**A third authorization state.** Stage-1 authorization now has three
outcomes and every listed branch reaches exactly one: `PENDING_DELETE`
for a branch present on the remote and verified merged;
`NOT_AUTHORIZED` for one present but not merged; and
**`ABSENT_FROM_REMOTE`** for one that is listed but has no remote ref at
all. The last two are terminal. `verified_merged` is `n/a` for an
`ABSENT_FROM_REMOTE` entry, because with no tip there is no ancestry to
test. The counts must satisfy the closed identity `listed_count =
pending_delete_count + not_authorized_count + absent_from_remote_count`,
reported as arithmetic rather than as a claim.

**Remote refs are the sole deletion authority.** `git ls-remote origin`
governs every tip value, existence test and ancestry check. Local branch
refs must not be used for any deletion decision, each tip is re-verified
from the remote immediately before its deletion command, and deletion is
performed with `git push origin --delete`; `git branch -d` and
`git branch -D` are prohibited because they touch only local refs and
would leave the remote branch in place while appearing to have deleted
it.

### Evidence

**Both gaps were exposed by executing Stage 1, not by reviewing it.**
Stage 1 handled both correctly under the policy as written and reported
them; neither is a defect in what it produced.

The first surfaced as a record that had to explain itself:
`gate/p2-integrate-fierz-and-sign-ruling` is listed but was never
pushed, and the only available state was `NOT_AUTHORIZED`, leaving
`not_merged_count` at 0 while one entry carried that status. The two
situations differ in their futures — an absent branch may be pushed
later and reassessed; a present-but-unmerged one will not become
deletable by anything happening on the remote.

The second surfaced as observed drift: local `main` sits at `0f796174`
against a remote `236f71c6`, and local `run/p2-betav-arm-p-decisive` at
`0f796174` against a remote `48c5cc59`. Stage 1 read every value from
`git ls-remote` and was correct to, but nothing in the policy required
it.

`docs/BRANCH_DELETION_RECORD_2026-08-07.md` is corrected: the one absent
entry is restated as `ABSENT_FROM_REMOTE`, its explanation preserved and
extended with the reason for the restatement, and the count identity
added. **No recorded tip, merge commit or other entry was altered** —
they are pre-deletion evidence.

### Consequences

Nothing is deleted by this entry, and the deletion set is unchanged at
25 `PENDING_DELETE` entries. **Stage 2 is gated on this amendment and
Stage 1 both being merged into `main`.**

`fix/freeze-checker-sign-repair` remains excluded from the deletion set
and must not be deleted; it appeared on the remote after the Stage-1
inventory was taken and is handled in a later inventory.

`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` remains permanently
preserved.

### Related gate

None. This is a repository-hygiene policy and changes no gate or
scientific status.

### Related branch and files

`fix/branch-deletion-policy-amendment`;
`docs/BRANCHING_POLICY.md`, `docs/BRANCH_DELETION_RECORD_2026-08-07.md`,
`DECISION_LOG.md`,
`specs/2026-08-07T1508Z_branch-deletion-policy-amendment.md`.

## 2026-08-08 — Euclidean exponent mapping: the canonical interaction is written in the exponent

Date: 2026-08-08
Decision owner: Principal Investigator
Effect: supplies a convention absent from the frozen material

### Decision

The PI ruling of 2026-08-08, reproduced verbatim:

> **PI ruling, 2026-08-08 — Euclidean exponent mapping.**
>
> The canonical interaction expression
>
>     X = (G/(2N)) * Sum( bilinear(lam(A), Id4)**2
>                       + bilinear(lam(A), I*gamma5)**2, (A, 0, N**2-1) )
>
> is written **as it appears in the Boltzmann exponent**. Equivalently,
> it enters the Euclidean action with a minus sign:
>
>     exp(-S_E) contains exp(+X)        <=>        S_E = S_E,0 - X
>
> Consequently, for a channel whose coefficient in `X` is written
> `c * J**2`, the Hubbard–Stratonovich coefficient is
>
>     g = +2c
>
> **Basis, stated exactly.** This is **NOT derived from the frozen
> material.** The frozen material contains no Euclidean action, no free
> or kinetic part, and no exponent mapping; the derivation that raised
> this question searched for one and found none. The ruling is
> **constrained by executed usage**: `P2-GAP-01` is a PASSed gate whose
> mean-field treatment introduces a **real** scalar auxiliary field `Σ`,
> which is admissible only when the scalar channel has `g > 0`. Under
> the opposite mapping the scalar channel would give `g < 0` and that
> gate's method would not be available.
>
> **This supplies a definition the frozen material never carried. It is
> not a recovery of an original intent.**
>
> **Scope.** This ruling resolves the exponent mapping and nothing else.
> It selects no Hubbard–Stratonovich channel — that remains `OPEN-AC-1`
> and is the PI's. It freezes none of the three diquark-definition gaps
> (`η`, particle–particle Grassmann ordering, diquark normalisation). It
> reaches no conclusion about a composite vector. It does not by itself
> re-run any withheld verdict.

### Reason

The exponent mapping was identified as missing by the channel-character
derivation, which searched the frozen material for it and found none,
and therefore withheld two verdicts: `REAL-HS ADMISSIBILITY NOT DEFINED
BY THE FROZEN MATERIAL` and `ATTRACTIVE/REPULSIVE NOT DEFINED BY THE
FROZEN MATERIAL`. Both remain withheld until separately recomputed; this
entry does not re-run them.

The ruling is **constrained by executed usage** rather than derived.
`P2-GAP-01` is a PASSed gate whose method requires the scalar channel to
admit a real linear auxiliary field.

**Not a recovery of an original intent** — no document ever stated the
mapping, and the constraint fixes which of two conventions the programme
has in fact been using, not which one was once intended.

### Consequences

For any channel whose coefficient in `X` is `c`, the exponent-level
Hubbard–Stratonovich coefficient is `g = +2c`. The withheld Layer-1b and
Layer-2 verdicts of the channel-character derivation become computable;
computing them is a separate authorized task and is not performed here.

This ruling **selects no Hubbard-Stratonovich channel**. `OPEN-AC-1`
remains open and is the PI's. The three diquark-definition gaps — `η`,
the particle–particle Grassmann ordering, and the diquark normalisation
— are untouched and remain unfrozen.

No gate status changes. `P2-GAP-01` remains `PASS` and `P2-PHASE-01`
remains `PROPOSED`.

### Related gate

None. This ruling supplies a convention; it registers no gate and
changes no gate status.

### Related branch and files

`fix/exponent-mapping-ruling`;
`DECISION_LOG.md`,
`specs/2026-08-08T1634Z_exponent-mapping-ruling.md`.

## 2026-08-08 — Open derivation item: generator-sum criticality is UNESTABLISHED

Date: 2026-08-08
Decision owner: Principal Investigator
Effect: opens an unperformed derivation item

### Decision

The open item, reproduced verbatim:

> **Open derivation item — generator-sum criticality.**
>
> `P2-GAP-01` obtained `G_c = 1/(2·I_0)` working from the singlet-only
> form `L_int = G_N (ψ̄ψ)²`, with `G = 4·G_N`. **The mean-field
> combinatorics of the full U(N) generator-sum canonical interaction
> have never been performed**, in that gate or since.
>
> **Status: UNESTABLISHED.** Whether `G_c = 1/(2·I_0)` transfers to the
> canonical generator-sum interaction is not known. **`P2-GAP-01`'s PASS
> stands for the form it computed**; this item concerns whether that
> result may be lifted to the canonical form, and it may not be assumed.
>
> **Not implied by the exponent ruling.** That `P2-GAP-01`'s real-`Σ`
> usage constrains the exponent mapping says nothing about whether its
> `G_c` applies to the generator-sum form. **Treating HS contour
> consistency as evidence for a gap equation would conflate a convention
> with a derivation.**

### Reason

The canonical interaction designated by `CANONICAL_INTERACTION.md` §2 is
the U(N) generator-sum form `(G/2N) Σ_A [S^A² + P^A²]`. `P2-GAP-01`
computed its critical coupling from the singlet-only NJL form
`L_int = G_N(ψ̄ψ)²`. Those are different interactions: the generator sum
carries `N²` internal channels where the singlet-only form carries one,
and the mean-field combinatorics that produce the gap equation's
prefactor have never been carried out for it.

The question this item opens is narrow and dynamical: **does
`G_c = 1/(2·I_0)` survive the change of interaction?** It is a
derivation, not a convention, and no ruling can settle it.

### Consequences

`G_c = 1/(2·I_0)` may not be quoted for the canonical generator-sum
interaction until the derivation is performed. It remains quotable for
the form `P2-GAP-01` actually computed.

**`P2-GAP-01`'s gate entry is not edited and its `PASS` is not
qualified.** The gate passed for the interaction it computed, and that
remains true; this item records a question about lifting the result, not
a doubt about it.

Stated once without markup, so the record carries the sentence plainly:
P2-GAP-01's PASS stands for the form it computed.

### Related gate

`P2-GAP-01`, whose status is unchanged at `PASS`. This entry registers no
gate and changes no gate status.

### Related branch and files

`fix/exponent-mapping-ruling`;
`DECISION_LOG.md`,
`specs/2026-08-08T1634Z_exponent-mapping-ruling.md`.

## 2026-08-08 — Attraction/repulsion sign convention: the label is assigned to the sign of g

Date: 2026-08-08
Decision owner: Principal Investigator
Effect: supplies a convention absent from the frozen material

### Decision

The PI ruling of 2026-08-08, reproduced verbatim:

> **PI ruling, 2026-08-08 — attraction/repulsion sign convention.**
>
> Under the Euclidean exponent mapping ruling of the same date, a channel
> whose Hubbard–Stratonovich coefficient satisfies **`g > 0` is labelled
> ATTRACTIVE**; **`g < 0` is labelled REPULSIVE**.
>
> **The basis, in three separated steps.** Under the Euclidean exponent
> mapping, a channel term with coefficient `g` appears as
> `exp(+(g/2)J²)`. For `g > 0` the standard linear
> Hubbard–Stratonovich representation uses a real Gaussian auxiliary
> field; for `g < 0` that real contour is not available — **that is the
> algebraic fact.** **The programme adopts ATTRACTIVE as the label for
> the `g > 0` sign and REPULSIVE for the `g < 0` sign** — that is the
> convention. This is consistent with `P2-GAP-01`'s description of its
> positive-coupling scalar channel as attractive — that is the
> consistency check. **The naming is not derived from
> Hubbard–Stratonovich admissibility; it is assigned to that sign.**
>
> **`J = ψ̄Γψ` is a Grassmann composite.** Before bosonisation there is
> no c-number configuration space on which "larger `|J|`" can be
> compared pointwise, so **no appeal to enhanced configurations is made
> here.** An earlier formulation did make one and was wrong to.
>
> **This ruling depends on the exponent mapping ruling of the same
> date.** If that mapping were reversed, every channel's `g` reverses
> and so does every label this ruling assigns. **The two are a chain,
> not independent constraints**, and neither is derived from the frozen
> material.
>
> **Scope limit.** The label characterises the sign of the interaction
> in the specified Hubbard–Stratonovich channel. It is conventionally
> associated with an attractive or repulsive tendency in that channel;
> **it does not establish that condensation actually occurs.** Whether
> it does depends on the full quadratic kernel — `Γ⁽²⁾(0) = 1/g − Π(0)`
> — the fermion determinant, stability, and the critical coupling.
> **Nor does it by itself establish the existence or absence of a
> two-body bound state, resonance, or composite excitation.**
>
> **In particular: REPULSIVE in a `ψ̄ψ` channel does NOT imply that a
> composite vector is absent.** That question requires its own
> bound-state or pole analysis, and may also involve a differently
> paired channel. **A channel-character label is not a pole
> calculation.**
>
> **This supplies a convention for the item currently recorded in the
> programme registry as `NOT DEFINED`. It is not a derivation.**

### Reason

The channel-character derivation withheld its Layer-2 verdict as
`ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN MATERIAL`, having
searched the frozen material for a rule mapping the sign of a channel
coefficient to one of those two names and found none. The Euclidean
exponent mapping ruling of the same date makes the coefficient itself
computable — `g = +2c` — but a computable sign is not yet a label. This
ruling supplies the missing half.

The naming is a convention assigned to a sign, and the ruling says so in
its own words. The algebraic fact it is assigned alongside — that the
standard real linear Hubbard–Stratonovich representation is available
for `g > 0` and not for `g < 0` — is stated separately from the naming,
and the consistency check against `P2-GAP-01`'s positive-coupling scalar
channel is stated separately again. The three are deliberately not run
together.

An earlier formulation of this ruling argued from configurations of
larger `|J|` being enhanced. That argument was wrong, because
`J = ψ̄Γψ` is a Grassmann composite and there is no c-number
configuration space on which the comparison can be made before
bosonisation. It is withdrawn by the text above rather than quietly
dropped.

### Consequences

Layer 1b and Layer 2 of the channel character become computable: the
sign of `g` follows from the exponent mapping ruling, and this ruling
names it. Performing that recomputation is the authorized task of
`specs/2026-08-09T0300Z_attraction-ruling-and-layers.md`.

The label is a channel-character statement and nothing more. It does not
establish that condensation occurs, which depends on the full quadratic
kernel, the fermion determinant, stability and the critical coupling;
and it does not establish the existence or absence of a two-body bound
state, resonance or composite excitation. In particular a repulsive
label in a `ψ̄ψ` channel licenses no statement about whether a composite
vector exists — that requires its own bound-state or pole analysis, and
may involve a differently paired channel.

This ruling depends on the exponent mapping ruling of 2026-08-08 and
inherits its status. Reversing that mapping reverses every `g` and every
label assigned here. Neither is derived from the frozen material.

This ruling **selects no Hubbard-Stratonovich channel**. `OPEN-AC-1`
remains open and is the PI's. The three diquark-definition gaps — `η`,
the particle–particle Grassmann ordering, and the diquark normalisation
— are untouched and remain unfrozen.

The programme registry row `Sign convention for attraction and
repulsion` is **not** changed here. It is to record a convention that
has been used, not one only declared, and updating it is a separate
`0-programme` task that should follow the recomputation.

No gate status changes. `P2-GAP-01` remains `PASS` and `P2-PHASE-01`
remains `PROPOSED`.

### Related gate

None. This ruling supplies a convention; it registers no gate and
changes no gate status.

### Related branch and files

`gate/p2-attraction-ruling-and-layers`;
`DECISION_LOG.md`,
`specs/2026-08-09T0300Z_attraction-ruling-and-layers.md`.

## 2026-08-09 — `CONVENTIONS.md` amendments A–D adopted; Rules 14 and 15 added

Date: 2026-08-09
Decision owner: Principal Investigator
Effect: refines four execution-discipline rules and adds two new ones

### Decision

`CONVENTIONS.md`'s execution-discipline rules, which ran 1–13, now run
1–15. Four existing rules are refined by amendment and two rules are
added:

    Amendment A  -> Rule 7    mid-task authorizations are reproduced
                              verbatim in the task report
    Amendment B  -> Rule 8    every task report carries a
                              "Stops and clarifications" section
    Amendment C  -> Rule 9    digest semantics and binary-safe
                              computation
    Amendment D  -> Rule 13   execution location, and the
                              process/harness layer
    Rule 14                   validator outcome and exception contract
    Rule 15                   governing artifacts are committed

**No rule was renumbered, reworded or reordered.** Rules 1–13 keep their
numbers and titles, and their pre-existing text is unchanged apart from
the four authorised insertions.

### Two provenances, which are not the same

**Amendments A–D and Rule 14 come from a previously approved amendment
draft that had never been executed.** The draft is
`DRAFT_amendment_reporting_and_digests.md`, SHA-256
`bef29c4d0ef3d391f2caa2f17ab6336e11677c73a3c37cbf4acb17b23e566822`,
supplied with the authorising specification. Each was derived from a
named incident, and those incident records are landed with them.

**Rule 15 does not come from that draft, and its text is not in it.**
Rule 15 was approved by the PI separately, before this execution, and
is supplied normatively by
`specs/2026-08-09T1653Z_land-rules-14-15.md` §2. **That prior approval
has no separate repository artifact; the authorising specification is
the first durable record of it, and this entry is the second.** It is
not recorded as extracted from an approved document, because it was
not.

### Reason

The four amendments and Rule 14 were each written against a specific
execution incident: mid-task authorizations that existed only in
conversation and could not be distinguished by a reviewer from an
executor expanding its own scope; stop records without a category, which
invite the reader to infer executor unreliability from a count; two
wrong digests in `GATES.md` caused by hashing through a text pipeline;
an "X is absent" conclusion drawn from a worktree that had never checked
out the revision under test; and five validators that each printed
`[100%]` and each exited 124 at the same boundary, for which the
acceptance criterion had no vocabulary.

Rule 15 was written against a different finding. A read-only audit
established that an integration task's repository state was correct in
every respect, but that its scope manifest was never preserved, no
merge-guard output was ever committed, and neither mid-task
authorization appeared in the report verbatim. **The result was right;
the authority under which it was produced could not be reconstructed.**
Since then, specifications passed to the Reviewer as conversational text
have led, on four occasions in one day, to review of a superseded
version and to issues already fixed being raised again.

### Consequences

A task specification may now say "validators must pass under Rule 14"
rather than restating the exit contract, and must state explicitly where
it needs different semantics.

**Rule 15 changes how the Reviewer function works, not only the
Executor.** Pre-execution reviews are to be committed under
`reviews/<function>/` before the work they authorise proceeds. That is a
new step for the reviewing party and is stated here so it is visible
rather than discovered later.

**All of it binds prospectively only.** Records created before this
adoption are not retrospectively non-conforming and are **not to be
back-filled**. No `reviews/` record was created by this task, because
creating one would be the back-filling Rule 15 forbids.

**This task is governed by the rules in force at its evidence base.**
Rule 15 becomes operative only after integration and does not
retroactively require this task's own pre-execution review to be
committed. That is ordering, not exemption.

No gate status changes. No science, no gate, no result is touched.
`AGENTS.md` is not modified: its research rules are a different
numbering from `CONVENTIONS.md`'s execution-discipline rules, and this
adoption touches only the latter.

### Related gate

None. This adoption changes governance text; it registers no gate and
changes no gate status.

### Related branch and files

`governance/land-rules-14-15`;
`CONVENTIONS.md`, `DECISION_LOG.md`,
`specs/2026-08-09T1653Z_land-rules-14-15.md`.

## 2026-08-09 — `CONVENTIONS.md` amendments E–L adopted; Rules 16 and 17 added

Date: 2026-08-09
Decision owner: Principal Investigator
Effect: refines seven execution-discipline rules and adds two new ones

### Decision

`CONVENTIONS.md`'s execution-discipline rules, which ran 1–15, now run
1–17. Seven existing rules are refined by amendment and two rules are
added:

    Amendment E  -> Rule 14   a failed observation is not a negative result
    Amendment F  -> Rule 12   mutation tests must prove reach
    Amendment G  -> Rule 9    structural changes propagate
    Amendment H  -> Rule 3    literals are verified by execution
    Amendment I  -> Rule 8    mid-task authority changes require
                              reviewer-visible provenance
    Amendment K  -> Rule 5    re-issuing an executed specification
    Amendment L  -> Rule 9    consumed conventions must be discoverable
                              through the conventions index

    Rule 16                   accumulated reading
    Rule 17                   integrations do not add epistemic or
                              governance classifications

**No rule was renumbered, reworded or reordered.** Rules 1–15 keep their
numbers and titles, and their pre-existing text is unchanged apart from
the seven authorised insertions.

**Two amendments attach to Rule 9 and remain distinct.** G concerns
structural propagation within a specification; L concerns whether a
consumed convention is discoverable. They are landed as two separate
blocks and are not merged.

### The numbering resolution

**The approved draft left the numbering of the two new rules open.** It
labels the accumulated-reading rule "New Rule 16" and labels the
integration-classification rule only "Amendment J (new)", with no
number.

**Resolved by `specs/2026-08-09T1801Z_land-amendments-e-to-l.md` §1:**
the accumulated-reading rule keeps the number the approved draft gives
it, **16**; the integration-classification rule becomes **17**. The
alternative — renumbering the accumulated-reading rule to make room —
would have changed a label the review settled.

### Provenance

**The reviewed source draft is committed** at
`docs/amendments/2026-08-09_observation-and-propagation.md`, SHA-256
`6368aff4ad66126f115be3fd0689e513db59e6061a28dd4e599b9bb5aa91c0e4`,
byte-identical to the file supplied with the specification. **It is
committed because the authorising specification requires it as the
durable provenance of the reviewed amendments**, consistent with Rule
15's governing-artifact principle. **Rule 15's own text does not name a
reviewed source draft**: it names specifications, pre-execution reviews,
task reports and supplied manifests, and asserting more than it says is
what Rule 17 forbids.

**The incident records that justify each amendment live in that draft
and were deliberately not imported into `CONVENTIONS.md`.** The rules
land; their justifications remain readable at a cited path.

**This is the first task governed by Rule 15**, and its pre-execution
review is committed at
`reviews/chatgpt/2026-08-09T1801Z_land-amendments-e-to-l.md`, before the
work it authorises proceeded. **The prospective exemption the Rules
14/15 landing relied on is no longer available.**

### Reason

Each amendment applies one principle — **evidence must establish the
property claimed, not merely a correlated proxy for it** — to a place
where the proxy had been mistaken for the property: an exit status read
as an observation; a stop counted as proof that a mutation was reached;
a numerical disagreement treated as overturning an algebraic identity; a
near-match accepted as a match; a citation treated as computational
consumption; final-state scope compliance treated as history
preservation.

Rule 16 addresses a different failure: individual artifacts each
scrupulous about what they do not establish, while their accumulation
reads as a stronger conclusion than any of them states. Rule 17 records
that supplying a classification the evidence does not support is
forbidden to specification authors and integrators, not only to
executors.

### Consequences

**All of it binds prospectively only.** Records created before this
adoption are not retrospectively non-conforming and are not to be
back-filled. **No existing review record was modified.**

Rule 16 obliges a task adding a material artifact to a question already
addressed elsewhere to state what the assembled set does not establish,
and obliges an integration to repeat that assessment against the merged
state, naming the junction or reporting the search.

Rule 17 binds any task carrying reviewed results forward, including
integrations and the specifications that authorise them.

Amendment K's append-only measure — evaluated against the last pushed
state of the branch as well as against the evidence base — applies to
this entry itself.

No gate status changes. No science, no gate, no result is touched.
`AGENTS.md` is not modified: its research rules are a different
numbering from `CONVENTIONS.md`'s execution-discipline rules.

### Related gate

None. This adoption changes governance text; it registers no gate and
changes no gate status.

### Related branch and files

`governance/land-amendments-e-to-l`;
`CONVENTIONS.md`, `DECISION_LOG.md`,
`docs/amendments/2026-08-09_observation-and-propagation.md`,
`reviews/chatgpt/2026-08-09T1801Z_land-amendments-e-to-l.md`,
`specs/2026-08-09T1801Z_land-amendments-e-to-l.md`.

## 2026-08-09 — Mean-field channel for `P2-PHASE-01`: the scalar channel with a real auxiliary field

Date: 2026-08-09
Decision owner: Principal Investigator
Effect: selects a route for mean-field work; defers an alternative

### Decision

The PI ruling of 2026-08-09, reproduced verbatim:

> **PI ruling, 2026-08-09 — mean-field channel for `P2-PHASE-01`.**
>
> Mean-field work proceeds in the **scalar channel with a real auxiliary
> field.** Under the 2026-08-08 rulings the scalar singlet has `g > 0`
> and admits the standard real linear Hubbard–Stratonovich
> representation; the induced V and A singlets have `g < 0` and do not.
>
> **This is a choice of direct route, not a judgement that the V/A
> representation is wrong.** The programme's existing machinery — the
> gap equation, `I_0`, the stationary-branch study — is built on a real
> auxiliary field. **The V/A channel does not admit the standard real
> linear HS contour that machinery uses, and would require a non-real
> contour or an otherwise reformulated bosonisation apparatus.**
>
> **No evidence indicates the V/A representation is unphysical, and the
> PI's position is that it may contain physically relevant information
> and must be returned to. It is deferred, not excluded** — see
> `DEFERRED-01`.
>
> **This does not close `OPEN-AC-1`.** It selects the channel for
> mean-field work; the Fierz ambiguity — that channels equivalent as
> operators are inequivalent after truncation — is unaffected by which
> one is used.

### Reason

The Layer-1b recomputation of 2026-08-09 established which of the three
particle-hole channels admits the standard real linear
Hubbard–Stratonovich representation: the scalar singlet has `g > 0` and
does; the induced V and A singlets have `g = -G/2 < 0` and do not. The
programme's existing mean-field machinery — the gap equation, `I_0`, the
scalar stationary-branch study — is built on a real auxiliary field, so
the scalar channel is the route that machinery can already take.

The ruling is a selection among available routes, not a finding about
either channel. **No calculation in this repository bears on whether the
V/A representation is physically correct**, and none was performed for
this decision.

### Consequences

Mean-field work for `P2-PHASE-01` proceeds in the scalar channel with a
real auxiliary field.

The V/A representation is entered in the deferred-items register as
`DEFERRED-01`, deferred and not excluded, with the PI's position
recorded there that it may contain physically relevant information and
must be returned to.

`OPEN-AC-1` is **not** closed. The Fierz ambiguity — that channels
equivalent as operators are inequivalent after mean-field truncation —
is a property of the truncation and is unaffected by which channel is
used.

No gate status changes. `P2-PHASE-01` remains `PROPOSED` and
`P2-GAP-01` remains `PASS`.

### Related gate

None. This ruling selects a route; it registers no gate and changes no
gate status.

### Related branch and files

`fix/pi-decisions-v3`;
`DECISION_LOG.md`, `derivations/P2-DEFERRED-ITEMS.md`,
`specs/2026-08-09T1958Z_pi-decisions-v3.md`.

## 2026-08-09 — The charge-conjugation phase `eta` is not selected; both signs are computed

Date: 2026-08-09
Decision owner: Principal Investigator
Effect: declines to select a convention; prescribes a two-sign evaluation

### Decision

The PI ruling of 2026-08-09, reproduced verbatim:

> **PI ruling, 2026-08-09 — `η` is not selected; both signs are
> computed.**
>
> The diquark rearrangement requires `ψ̄^c = η ψ^T C⁻¹`. **The frozen
> material fixes no value of `η`, and unlike the exponent mapping no
> executed calculation constrains it.**
>
> **For the SIGN AMBIGUITY exposed by the channel-character derivation,
> the programme evaluates both the `η = +1` and the `η = −1`
> representative rather than selecting between them.** This does not
> assert that the full convention space is exactly two elements — the
> residual phase freedom has not been characterised — only that the
> ambiguity shown to affect the paired product is a sign, and both signs
> are to be carried through and reported.
>
> **The reason is diagnostic.** If both signs give the same channel
> character, **the exposed `η = ±1` sign ambiguity does not affect that
> character, and that sign question closes** — the wider phase freedom
> remains uncharacterised either way. **If they give opposite
> characters, then the diquark channel character depends on an
> unresolved sign convention — and that is something the programme must
> know rather than conceal behind a choice.**

### Reason

The channel-character derivation established that `η` appears once in
the paired product and therefore flips the sign of the diquark channel
coefficient, and that the frozen material fixes no value for it. Unlike
the Euclidean exponent mapping, which an executed calculation
constrains through `P2-GAP-01`'s real auxiliary field, **no executed
calculation constrains `η`.**

The alternative to this ruling is a diquark channel character that
rests on an arbitrary sign. Computing both representatives costs one
extra evaluation and converts an unresolved convention into a
measurable question.

### Consequences

When the diquark channel character is computed, both the `η = +1` and
the `η = -1` representative are to be evaluated and both reported.
**That calculation is a separate authorized task and is not performed
here.**

If the two agree, the `η = ±1` sign ambiguity does not affect the
diquark channel character and that sign question closes. If they
disagree, the diquark channel character depends on an unresolved sign
convention, and the programme records that rather than concealing it
behind a choice.

**The residual phase freedom in `η` is not characterised by this
ruling** in either outcome. The ruling addresses the sign ambiguity the
channel-character derivation exposed, not the full convention space.

The particle–particle Grassmann ordering and the diquark operator
normalisation remain unfrozen and are untouched here.

No gate status changes.

### Related gate

None. This ruling declines to select a convention; it registers no gate
and changes no gate status.

### Related branch and files

`fix/pi-decisions-v3`;
`DECISION_LOG.md`,
`specs/2026-08-09T1958Z_pi-decisions-v3.md`.

## 2026-08-09 — The negative-mass stationary branch is DEFERRED, not excluded

Date: 2026-08-09
Decision owner: Principal Investigator
Effect: declines to classify; records a consequence for SI-1

### Decision

The PI ruling of 2026-08-09, reproduced verbatim:

> **PI ruling, 2026-08-09 — the negative-mass branch is DEFERRED, not
> excluded.**
>
> The exploratory study found a second stationary branch at
> `M̂ ≈ −7.59`, the exact Wilson complement of the trivial branch, **with
> positive restricted curvature in the explored one-dimensional
> stationary analysis, including below `G_c`.**
>
> **"Restricted", not "stable", is the accurate word.** The pinned
> exploratory note states of exactly that quantity: *"Neither curvature
> is a full condensate-space Hessian or a phase-admissibility
> statement."* **A bare "stable" would let a later reader take the
> premise as stronger than the evidence.**
>
> **It is not classified as a lattice artifact.** The complement
> relation and the observed restricted stability **tie the branch
> structurally to the Wilson term; they do not establish full
> condensate-space stability, phase admissibility, or absence of
> physical content.** Under the substrate reading there is no continuum limit, so
> **the standard continuum-decoupling argument cannot by itself classify
> this branch as an unphysical lattice artifact.**
>
> **The PI's position is that a solution stable under the analysis
> actually performed corresponds to something that warrants physical
> interpretation rather than automatic dismissal.** The branch is
> deferred pending the main line — see `DEFERRED-02`.
>
> **The qualifier is load-bearing.** Written as *a stable solution
> corresponds to something real*, the position would quietly restore the
> stability claim narrowed two paragraphs above.
>
> **Consequence for SI-1, recorded now so it is not met by surprise.**
> `P2-PHASE-01`'s kill criterion asks whether any admissible phase exists
> in the frozen space. **With this branch neither admitted nor excluded,
> that criterion's quantifier range is undetermined**, and the SI-1
> specification must state whether the branch falls inside it. **This
> ruling does not answer that; it records that the question is now
> unavoidable.**

### Reason

The exploratory scalar stationary study reported a second stationary
root at `M̂ ≈ -7.59`, the exact Wilson complement of the trivial branch
under `I_0(M̂) = I_0(-8-M̂)`, carrying positive restricted curvature at
`G/G_c` values below `1`.

**The word "restricted" is doing work.** The quantity measured is the
curvature of the reduced one-dimensional scalar potential, of which the
pinned exploratory note says: "Neither curvature is a full
condensate-space Hessian or a phase-admissibility statement." The
ruling carries that qualifier in its own text rather than leaving it to
be recovered from the source.

Both facts tie the branch to the Wilson term. **Neither shows the
branch carries no physical content.** The argument that would ordinarily
classify such a branch as an unphysical lattice artifact is
continuum decoupling, and under the substrate reading there is no
continuum limit for it to appeal to.

### Consequences

The branch is entered in the deferred-items register as `DEFERRED-02`,
neither admitted nor excluded, with the PI's position and the strength
of the supporting evidence recorded there separately.

**`P2-PHASE-01`'s kill criterion asks whether any admissible phase
exists in the frozen space. With this branch neither admitted nor
excluded, the range of that quantifier is undetermined**, and the SI-1
specification will have to state whether the branch falls inside it.
**This ruling does not answer that question and does not amend the SI-1
gate text.** It records that the question can no longer be left
implicit.

No gate status changes. `P2-PHASE-01` remains `PROPOSED` and
`P2-GAP-01` remains `PASS`. No exploratory result, branch-depth table
row, or line of the parameter-domain draft is altered.

### Related gate

`P2-PHASE-01`, whose status is unchanged at `PROPOSED`. This entry
registers no gate and changes no gate status.

### Related branch and files

`fix/pi-decisions-v3`;
`DECISION_LOG.md`, `derivations/P2-DEFERRED-ITEMS.md`,
`specs/2026-08-09T1958Z_pi-decisions-v3.md`.

## 2026-08-12 — `CONVENTIONS.md` Rule 18 added; `docs/BRANCHING_POLICY.md` gains a SUPERSEDED attribute and register

Date: 2026-08-12
Decision owner: Principal Investigator
Effect: adds one execution-discipline rule and one branch attribute with
its register; both are prospective

### Decision

Two governance additions, each recording a failure the programme has
already had. **No science, no gate, no computation.**

    Rule 18                   review supply protocol
    SUPERSEDED (attribute)    docs/BRANCHING_POLICY.md, with a register
                              of six branches

**Rule 18 fixes how a pre-execution review reaches the executor.** Rule
15 requires the review to be committed and says nothing about its supply.
**A review is supplied AS A FILE and its bytes are committed unchanged.**
**No extraction, no delimiters, no normalisation** — there is no boundary
to locate, so none can be inferred, and no transport artifact to strip.
The specification **should** also arrive as a file; a pasted
specification is permitted and is not a stop, **but the executor reports
which way it arrived.** Before committing, the executor **verifies
correspondence** — the review must identify the specification by digest
or task name — and **stops** if it does not, if no file is supplied, or
if it corresponds to a different specification.

**SUPERSEDED is an ATTRIBUTE, not a fourth deletion state.** The Stage-1
deletion machine keeps its three outcomes — `PENDING_DELETE`,
`NOT_AUTHORIZED`, `ABSENT_FROM_REMOTE` — and its closed count identity
unchanged and byte-identical. **Two independent questions are kept
independent:** whether a branch may be deleted, and whether it may be
integrated. Every register entry is present and unmerged, so each is
correctly `NOT_AUTHORIZED` for deletion; the attribute answers the second
question only.

**No rule was renumbered or reworded.** Rules 1–17 keep their numbers and
titles, and after removing the Rule 18 section the remaining text is
byte-identical to the evidence-base version.

### Reason

**A supply convention rediscovered per task is not a convention.**
Pasting a review between delimiters failed nine times across five modes:
a first-occurrence search finding the instruction that named the
delimiter; no delimiter supplied at all; a preamble before the BEGIN
line; a leading blank line whose stripping was an unwritten executor
choice; and finally a transport prefix fused to the BEGIN line, leaving
zero complete-line matches for BEGIN and one for END. **The one success
depended on how a message happened to be composed** — and a success that
depends on the sender's habits is not a protocol.

**The delimiter approach is abandoned rather than patched, because every
one of those modes was an extraction problem.** A rule that patches
extraction leaves a judgement point; **removing the need to extract
leaves none.** A file has no boundary inside a shared stream. **The two
transport-artifact clauses the delimiter protocol accumulated are
therefore moot, not inherited** — they fixed real failures, but a file
has no transport artifact to strip.

**Amendment K already requires a superseded branch to be preserved,
identified as superseded, and never integrated, and already records that
`docs/BRANCHING_POLICY.md` had no way to express it** — "no state for
superseded, never to be integrated — so a later integrator reading the
branch list would see two branches claiming to land the same entries."
Amendment K left the choice open: add the state, or state the prohibition
where an integrator will meet it. **This entry records the resolution:
neither a fourth state nor a bare prohibition, but an orthogonal
attribute with a register**, placed immediately after the deletion
machine it disclaims.

### Prospective only

**Both additions are prospective.** Records and reviews created before
this entry are not retrospectively non-conforming and are not to be
back-filled. **The register records supersessions already established by
durable artifacts; it is not a reclassification exercise.** A branch
enters it only where a durable repository artifact records its re-issue,
replacement or supersession and identifies the replacement or the reason.
**The artifact must record the FACT, not use a particular word** — a
specification saying a branch was rebuilt, naming the successor and the
reason, suffices even where "superseded" never appears. **Naming
similarity, age and Git topology do not suffice**, and where evidence
suggests supersession without establishing it the branch is left out
pending a PI decision.

**Register entries are referred to by BRANCH NAME, never by ordinal.** An
ordinal is correct only until the list grows, and a paragraph of this
register was wrong once for exactly that reason.

### Consequences

**Recorded, not enforced.** `CONVENTIONS.md` now carries eighteen rules
and `docs/BRANCHING_POLICY.md` a superseded register, **but no test
checks any of the eighteen rules**, and nothing mechanically prevents an
integration task from merging a superseded branch without consulting the
register. **That enforcement gap is a known open item and was
deliberately not closed here**; this task added no test.

The register's membership at this entry is six branches, each verified
present on the remote at its recorded commit and none an ancestor of
`main`. **`fix/pi-decisions-v3` is an ancestor of `main` and is the
surviving instance of the pi-decisions line; it is NOT superseded.**

**Two of the six entries are this rule's own earlier issues.** Rule 18
took three attempts to land: the first version's rule forbade the only
action available to its executor, who continued and disclosed it; the
second version's rule worked on its first live use, but its A3 had been
carried over from the delimiter version and contradicted the rule it
accompanied, and that executor stopped. **The register records both, and
their content was not at fault in either case.**

**`review/role-model-and-executors` now appears in the register while its
existing "permanently preserved" disposition stands unchanged.** The two
answer different questions — do not delete, and do not integrate — and
the register exists because they are independent. Its preservation entry
was not edited, replaced or weakened.

No gate status changes. No verdict, digest, or hash-pinned artifact is
modified. `AGENTS.md`, `GATES.md`, `CLAIMS.md` and every path under
`scripts/`, `results/`, `tests/` and `derivations/` are untouched.

### Supersedes

Nothing. Rule 18 is additive and Rules 1–17 are unchanged. The SUPERSEDED
attribute adds to `docs/BRANCHING_POLICY.md` without altering its
deletion states, their terminality, or the closed count identity. **No
earlier Rule 18 was ever landed**, so this is a first landing rather than
a replacement of committed text; the two superseded branches carry the
earlier drafts and are not integrated.

### Related gate

None. This entry registers no gate and changes no gate status.

### Related branch and files

`governance/supply-protocol-v3`;
`CONVENTIONS.md`, `docs/BRANCHING_POLICY.md`, `DECISION_LOG.md`,
`specs/2026-08-12T0131Z_supply-protocol-v3.md`.

## 2026-08-19 — Open construction item: the POLE milestone's construction layer is UNESTABLISHED

Date: 2026-08-19
Decision owner: Principal Investigator
Effect: opens an unscoped construction item

### Decision

The open item, reproduced verbatim:

> **Open construction item — the POLE milestone's construction layer.**
>
> `POLE-B0` assessed what the manuscript's own decisive test would require —
> a lattice measurement of the Barnes–Rivers–projected stress-tensor
> correlator, checking for a single `p² = 0` pole in the spin-2 sector with
> vanishing spin-1/0 residues (`paper/emergent_gr_paper_v2_15.tex:810-814`).
> It returned `REQUIRES A CONSTRUCTION NOT YET SCOPED`, with
> `TRACTABLE BUT BLOCKED PENDING A RULING` applying to part of the scope
> only.
>
> **Status: UNESTABLISHED.** Twelve components were inventoried;
> `N_both = 0`, and **six are neither implemented nor specified**: a
> definition of `⟨·⟩`, an evaluation of `⟨TT⟩` beyond one loop, a
> preregistered tensor-sector operator basis, finite-volume rules and the
> massless limit, the numerical meaning of "vanishing", and an
> artefact-versus-physics discriminator. **What the construction is has not
> been defined.**
>
> **This is an OPEN item, not a DEFERRED one.**
> `derivations/P2-DEFERRED-ITEMS.md` holds work that was examined and
> consciously postponed. `POLE-B0`'s result is that the construction is not
> yet scoped, which is a different epistemic state. **Filing it as deferred
> would assert that it was considered and set aside, and it was not.** It
> moves to the deferred side only if a future `POLE-C0` scopes the six
> components and the PI then postpones them.
>
> **Roadmap as it stands:**
>
>     POLE-B0 scope
>       -> POLE construction / specification layer
>       -> executable pole test
>
> **The construction is itself constrained by the open `R1`–`R4` rulings**,
> all four of which `POLE-B0` classified `DEPENDENCE ESTABLISHED`. **Clearing
> the rulings is necessary and not sufficient**: ruling all four would leave
> the six unscoped components exactly where they are.

### Reason

The item is an open programme-design / construction question — what the
construction is has not been defined — rather than an open
acceptance-criterion item, where the work is known and the criteria are not.
That distinction determines which register admits it, and this log is the
register whose stated scope covers an item opened as `UNESTABLISHED`.

The other candidates were read and none admits it.
`derivations/P2-DEFERRED-ITEMS.md` scopes itself to work considered and
consciously postponed, and states that its entries are added by PI decision.
`derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md` scopes itself to items
arising from the `C1`–`C3` follow-up checks of the C-check line.
`OPEN-AC-*` sits in the phase input / admissibility contract and holds
acceptance-criterion items. `OPEN-PD-*` sits in the microscopic parameter
domain and holds parameter-domain items. `docs/GOVERNANCE-DEBT.md` holds
governance debt — gaps in rules and mechanisms — and this is a scientific
construction question, not a rule gap.

### Consequences

**The decisive test may not be described as executable, or as blocked only by
a ruling.** Both statements would be wrong, and in different directions.

**No gate moves.** `P2-PHASE-01` remains `Status: PROPOSED`. This entry
registers no gate and changes no gate status.

Registering the item is not scoping it. **This entry defines no construction,
chooses no numerical criterion, and orders no task against any other.**

Stated once without markup, so the record carries the sentence plainly:
ruling R1 through R4 in full would not make the pole milestone executable.

### Related gate

None. The milestone is named by the manuscript at
`paper/emergent_gr_paper_v2_15.tex:810-814` and is covered by no section of
`GATES.md`.

### Related branch and files

`science/pole-b0-milestone-scope` @ `3f78acfebd7e994460eb30ac54ffd31a5cf3c21f`;
`derivations/P2-POLE-B0_milestone-scope.md`,
`reports/2026-08-19T0223Z_pole-b0-milestone-scope.md`,
`reports/2026-08-19T0448Z_pole-b0-integ-02_landing-record.md`,
`specs/2026-08-19T0448Z_pole-b0-integ-02.md`.

## 2026-08-19 — Physical hypothesis `H-EXT-01`: axis-TT completeness is UNESTABLISHED

Date: 2026-08-19
Decision owner: Principal Investigator
Effect: registers a physical hypothesis and records that nothing assumes it

### Decision

The hypothesis, reproduced verbatim:

> **`H-EXT-01` — physical completeness of the axis-TT projection.**
>
>     ID       H-EXT-01
>     Type     PHYSICAL HYPOTHESIS — directional, falsifiable.
>     Status   UNESTABLISHED — **NOT ASSUMED BY `RECON-01b`.**
>
> **Exact statement:**
>
> > The discarded external complement makes no contribution to the physically
> > relevant gravitational observable, so that `Z_axis-TT = Z_physical`.
>
>     Scope    The axis-TT projection as the repository defines it, and the
>              observable RECON-01b extracts.
>
>     What depends on it
>              Nothing currently in the repository. No landed result asserts
>              it and no pending task requires it.
>
>     What does NOT depend on it
>              RECON-01b. **RECON-01b requires only the definition
>              A-EXT-01; it does not require H-EXT-01 to be true, and does
>              not assume it.** A reader who takes RECON-01b to presuppose
>              H-EXT-01 has read the design backwards.
>
>     Evidence derivations/P2-RECON-EXT-01_discarded-external-space.md.
>              The measurement bears on the hypothesis and does not settle
>              it: it establishes that the discarded directions cannot be
>              neglected on grounds of magnitude, and establishes nothing
>              about whether they contribute to the physically relevant
>              observable.
>
>     Falsifier or resolution condition
>              REFUTED if the complement is shown to contribute irreducibly
>              to the target observable. ESTABLISHED if the complement is
>              derived to make no contribution to it. The adjudication is
>              routed to RECON-PROJ-01 and is not performed by any landed
>              task.
>
>     Review   reviews/chatgpt/2026-08-19T1141Z_assumption-review_a-ext-01_h-ext-01.md
>     Review SHA
>              e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47
>              — the digest of the exact statement bytes above. The review
>              artifact's own digest is
>              e641d4877a15975f224e57320b7e28dcbcd5850fcfecdc8e95a7f716650a0953.
>
>     Date     2026-08-19
>     Supersedes
>              A single earlier draft that merged this hypothesis with the
>              definition A-EXT-01 and treated the definition as itself
>              falsifiable. That draft is superseded by the two-entry form.

### Reason

**A definition is not a falsifiable proposition and a physical hypothesis is.**
The Researcher's earlier draft merged them, which made the definition look
refutable and made the hypothesis look adopted. **The type error is the reason
the two are registered separately and in different files:** `A-EXT-01` is a
convention and lives in `CONVENTIONS.md`'s definitional-conventions section;
`H-EXT-01` is a hypothesis and lives here, where this log already records open
items as `UNESTABLISHED`.

**The `Status` line is load-bearing.** Recording a hypothesis is not adopting
it, and `NOT ASSUMED BY RECON-01b` is the part a later reader is most likely to
drop.

### Consequences

**`RECON-01b` may proceed without settling this.** Its results are stated
relative to `Z_axis-TT` and may not be promoted to the full gravitational `Z`
unless `H-EXT-01` or an equivalent completeness result is independently
established.

**The βV/RECON line may not be cited as evidence for vanishing spin-1/0
residues.** A calculation defined inside the axis-TT subspace cannot
independently establish a channel separation that its own projection already
imposes.

**No gate moves.** `P2-PHASE-01` remains `Status: PROPOSED`. This entry
registers no gate and changes no gate status.

Stated once without markup, so the record carries the sentence plainly:
RECON-01b does not assume that the axis-TT observable is the full physical Z.

### Related gate

`P2-BETAV-RECON-01`, whose status is unchanged at `PROPOSED`.

### Related branch and files

`science/recon-ext-01-discarded-space` @ `70f0e257b9afcd9f97445c5c2c62530fa742321e`;
`CONVENTIONS.md` (the `A-EXT-01` entry),
`derivations/P2-RECON-EXT-01_discarded-external-space.md`,
`reviews/chatgpt/2026-08-19T1141Z_assumption-review_a-ext-01_h-ext-01.md`,
`specs/2026-08-19T1141Z_integrate-recon-ext-01.md`.

## 2026-08-19 — EXT-01 execution-layer dispositions and open findings

Date: 2026-08-19
Decision owner: Executor, adopted for the EXT-01 integration
Effect: records three reversible dispositions and two open findings

### Decision

**`D-1` to `D-3` are execution-layer dispositions, adopted for that task and
reversible by PI adjudication. They are NOT PI rulings and carry no PI-level
scientific authority.** They are recorded so that they can be inspected and
reversed rather than inherited silently.

**`O-1` and `O-2` are open findings, not decisions. Nothing is settled by
recording them.**

> **`D-1` — NO CRITERION IS SET on the discarded space.**
> Ground: the shares are signed, unbounded, and subject to cancellation, so a
> threshold on them would fix an arbitrary choice of normaliser. The robust
> quantities are the two ratios recomputed at this landing.
> Status: MEASURED, NO CRITERION SET, with the reason recorded. **This is not
> "awaiting a PI ruling"; it is a disposition open to reversal.**
>
> **`D-2` — EXTENSION IN MASS AND VOLUME IS DEFERRED, with reason.**
> The measurement stands at one pre-registered point. Robustness of the ratios
> in mass and in volume is unmeasured. Deferred to the `RECON-01b`
> construction, where the same machinery is already required, rather than
> opened as a separate task now. Recorded so that it attaches to that work and
> is not lost.
>
> **`D-3` — THE PROJECTION QUESTION IS ROUTED TO `RECON-PROJ-01`**, not
> settled here, and not settled by the magnitude. **Whether the complement
> matters is a question for derivation, not for a ratio.**
>
> **`O-1` — EVIDENCE-ARCHITECTURE SEPARATION. Open finding.**
> The βV/RECON line is a TT-conditioned reconstruction test. A test of the
> manuscript's decisive claim — a spin-2 pole with vanishing spin-1/0 residues
> — requires a calculation that does not project the other channels away before
> measuring. Whether any current numerical pipeline performs the latter is
> recorded as an open question. **This does not alter `POLE-B0`'s verdict.** It
> records that the construction `POLE-B0` found unscoped may be the pipeline
> the decisive claim requires. **Priority is a PI matter and is not set here.**
>
> **`O-2` — MAGNITUDE IS NOT CHANNEL STRUCTURE. Open finding.**
> The measurement establishes that the discarded directions cannot be neglected
> on grounds of magnitude. **It establishes nothing about whether those
> directions carry physical poles, where any pole lies, or whether a residue
> vanishes.** Recorded so that the magnitude result is not read as a
> channel-structure result.

### Reason

Dispositions taken during execution are otherwise carried only in a task
report, and a report is a record of one task. **Recorded here they can be
found and reversed; left in a report they are inherited silently.**

The identifiers `D-1` to `D-3` and `O-1`, `O-2` are the integration
specification's own labels for these items. **This log's identifier sequence is
its dated headings**, and the two entries dated 2026-08-19 above and here are
this register's identifiers for them.

### Consequences

**Nothing is settled by these five items.** `D-1` sets no criterion, `D-2`
opens no task, `D-3` decides no projection question, and `O-1` and `O-2` are
findings without verdicts.

**No gate moves.** This entry registers no gate and changes no gate status.

### Related gate

None. `P2-BETAV-RECON-01` is referenced and unchanged at `PROPOSED`.

### Related branch and files

`science/recon-ext-01-discarded-space` @ `70f0e257b9afcd9f97445c5c2c62530fa742321e`;
`derivations/P2-RECON-EXT-01_discarded-external-space.md`,
`specs/2026-08-19T1141Z_integrate-recon-ext-01.md`.

## 2026-08-19 — Registry split: assumptions and PI decisions get their own directories

Date: 2026-08-19
Decision owner: Principal Investigator
Effect: creates two directories and relocates one entry's canonical location

### Decision

The ruling, reproduced verbatim:

> 1. `reviews/` holds **reviews of specifications only**.
> 2. Assumptions get their own directory.
> 3. PI decisions get their own directory.
> 4. An assumption's content and its review may live in **one file, as Part 1
>    and Part 2**.
> 5. **PI decisions are also to be reviewed.**

### Reason

Four kinds of epistemic object were mixed across repository files: definitional
conventions, physical assumptions and hypotheses, PI decisions, and
specification reviews. **A reader could not tell which kind a statement was
from where its file sat.** The split gives each a canonical home:

    CONVENTIONS.md    definitions and conventions
    assumptions/      falsifiable or unestablished scientific propositions
    decisions/        PI rulings
    reviews/          reviews of specifications

### Consequences

**`H-EXT-01`'s canonical location is now `assumptions/H-EXT-01.md`.** **The
entry dated 2026-08-19 above is NOT deleted and NOT rewritten** — this log is
append-only, and that entry stands as the historical record of where the
hypothesis was first landed. **The relocation is recorded here rather than by
editing history**, so the repository does not read as though it always had this
taxonomy.

**`A-EXT-01` does not move.** It is a DEFINITIONAL CONVENTION, and
`CONVENTIONS.md` is the Convention Registry. **No stub is created for it in
`assumptions/`**, because `assumptions/` is scoped to falsifiable or
unestablished propositions and a stub would re-admit a definition into the
taxonomy the previous landing was written to keep it out of.
`assumptions/README.md` cross-references `CONVENTIONS.md` so a reader looking
for the pair finds both.

**The `Review SHA` field is split into `Statement SHA` and `Review Artifact
SHA`.** The field landed on 2026-08-19 under the single name `Review SHA`
carried the digest of the exact-statement bytes — the name said review, the
content was a statement binding. **The digests are unchanged and both
re-verify**; only the labels changed, and a label change does not touch a pin
taken over the statement.

**Three `reviews/pi/` records remain in place** as historical evidence, not
moved, not rewritten, not retrospectively reviewed.

**When a PI decision takes effect, and whether its review is ever gating, is
NOT settled by this entry.** `decisions/README.md` carries a **PROVISIONAL**
execution-layer disposition — reviews are recorded, not gating — and names the
adjudication as owed. **A gating review would place the Reviewer above the PI,
inverting the authority model in `AGENTS.md`**, which is the ground for the
provisional choice and not a substitute for the ruling.

**No gate moves.** This entry registers no gate and changes no gate status, and
a directory layout is not a scientific result.

Stated once without markup, so the record carries the sentence plainly:
H-EXT-01's original entry in this log is unchanged and remains the record of
where it was first landed.

### Related gate

None.

### Related branch and files

`science/registry-split-01`;
`assumptions/README.md`, `assumptions/H-EXT-01.md`,
`decisions/README.md`, `reviews/README.md`, `CONVENTIONS.md`,
`specs/2026-08-19T1723Z_registry-split-01.md`.

## 2026-08-20 — OBS-IDENT open records, registered and none answered

Date: 2026-08-20
Decision owner: Executor, adopted for the OBS-IDENT integration
Effect: registers four open records; answers none; settles nothing

### Decision

**`R-1` to `R-4` are OPEN RECORDS, not decisions and not findings with
verdicts. Nothing is settled by recording them.** They are the consequences
that follow from `P2-OBS-IDENT-01`'s `PROXY ONLY` outcome, and **the
integration that landed that outcome is forbidden by Rule 17 from drawing
them**: a consequence drawn from a reviewed result is not the reviewed result.

They are recorded here so that they can be found and taken up, rather than
inherited from a landing record.

> **`R-1` — `D-2`'s PURPOSE IS UNDECIDED.**
> `P2-OBS-IDENT-01`'s governing specification made re-specification of `D-2`
> conditional on the audit's outcome. **The condition is now met by
> measurement rather than by expectation.** Whether `D-2` is re-specified, and
> as what, is not decided. `D-2` as recorded on 2026-08-19 above stands
> unaltered.
>
> **`R-2` — THE SCOPE OF `GAP-B`, `MM-1`, `MM-3` AND `MM-5` IS UNDECIDED.**
> Each reasons about the object the audit has now related to the target
> observable. **None is declared invalid by that relation**, and no rescoping
> is performed. What each is about, given the relation, is not decided here.
>
> **`R-3` — WHETHER ANY LANDED DESCRIPTION OF `EXT-01`'s MEASUREMENT REQUIRES
> NARROWING IS UNDECIDED**, and so is the mechanism if one does. Landed
> reviewed records are not edited in place, so a narrowing — if warranted —
> would need a mechanism this record does not choose. **No landed description
> was altered by the task that registered this.**
>
> **`R-4` — THE `A-EXT-01` AMBIGUITY IS OPEN.** Its exact statement does not
> disambiguate between the two extraction levels at the point where it is
> load-bearing. **Whether a definitional convention silent at that point
> requires supersession is not decided**, and supersession would need a new
> exact statement and a new review. **The statement is unaltered and its
> `Statement SHA` is unchanged.**

**`R-4` is adjacent to `G-13` of `docs/GOVERNANCE-DEBT.md` and is NOT
duplicated there.** `G-13` asks whether a reviewed definitional statement **may
be** edited in place or instead requires supersession — a question of
permission. `R-4` asks whether **this** statement's silence at its load-bearing
point **requires** supersession — a question of necessity about one instance.
**They are different questions and a second register entry would create a
second place for one status to drift**, which `docs/GOVERNANCE-DEBT.md`'s own
`## Not entered here — D4` section warns against.

### Reason

The consequences of a relation are otherwise carried only in a landing record,
and a landing record is a record of one task. **Recorded here they can be found
and taken up; left in a landing record they are inherited silently** — which is
the reasoning the 2026-08-19 EXT-01 entry above gives for the same choice.

**This log's stated scope admits them.** Its head requires the entry template,
and the 2026-08-19 entry above is the precedent: `O-1` and `O-2` were
registered there as open findings by an executor for an integration, with
"Nothing is settled by recording them" stated in the same words.

### Consequences

**Nothing is settled by these four records.** `R-1` re-specifies nothing,
`R-2` rescopes nothing, `R-3` narrows nothing and alters no landed
description, and `R-4` amends no definitional statement.

**No gate moves.** `P2-BETAV-RECON-01` remains `PROPOSED`. `Q1`, `GAP-A`,
`GAP-B`, `A-EXT-01` and `H-EXT-01` are unchanged in status.

**`EXT-01` is not invalidated by any of these records**, and none of them
concludes anything about whether the discarded external space matters for the
target coefficient.

### Related gate

None. `P2-BETAV-RECON-01` is referenced and unchanged at `PROPOSED`.

### Related branch and files

`science/obs-ident-01` @ `612817cb9ffa75ca02341e4f408f5fc952000557`;
`derivations/P2-OBS-IDENT-01_observable-identity.md`,
`reports/2026-08-20T1050Z_obs-ident-01.md`,
`specs/2026-08-20T1113Z_obs-ident-integ.md`.

## 2026-08-20 — R-5: the homeless-obligation enumeration, measured

Date: 2026-08-20
Decision owner: Executor, adopted for the GAP-B integration
Effect: records one open finding; places no obligation; settles nothing

### Decision

**`R-5` is an OPEN RECORD, not a decision. Nothing is settled by recording
it**, and **no obligation is placed by it.**

> **`R-5` — THE STANDING CLAIM THAT NO REGISTER ADMITS THESE OBLIGATIONS IS
> FALSE AS MEASURED.**
> Three landing records — `P2-PROJ-01-INTEG`, `P2-RECON-01B-B0-INTEG` and
> `P2-GAPA-INTEG` — state that no register's stated scope admits `O-1`, `O-2`,
> `O-3` or `P2-GAPA-INTEG`'s `R-2`. **Measured against this log's stated scope
> and its own 2026-08-19 precedent, all four are ADMITTED.** None is "not
> admitted" and none is "not determinable from the stated scope".
> **This log was not among the registers those three tasks enumerated.**
>
> **A second figure does not survive the same enumeration.** Those records
> carry a count alongside the claim. Measured: `O-3` was discharged by the
> same task that restated the count, `O-2` is discharged by the landing this
> record accompanies, and `P2-GAPA-INTEG`'s `R-2` restates `O-2` rather than
> adding to it. **One of the four is outstanding: `O-1`.**
>
> **WHETHER ANY OBLIGATION IS NOW PLACED HERE, AND BY WHAT AUTHORITY, IS
> UNDECIDED.** Admission and placement are different acts, and the task that
> measured the first was not authorised to perform the second.

### Reason

The claim was this line's own repeated assertion, made three times without the
measurement that would test it. **Leaving it standing while landing another
artifact that could inherit it would propagate it a fourth time.**

**This log's stated scope admits this record** on the same ground as the
2026-08-19 EXT-01 entry and the 2026-08-20 OBS-IDENT entry: an open record,
adopted by an executor for an integration, settling nothing.

### Consequences

**Nothing is settled by this record.** No obligation is placed, no register
entry is created for any of the four, and the three landing records that carry
the claim are **not amended** — they are landed reviewed records, and whether
any needs correction is not decided here.

**No gate moves.** `Q1`, `GAP-A`, `GAP-B`, `A-EXT-01` and `H-EXT-01` are
unchanged in status.

### Related gate

None.

### Related branch and files

`science/gapb-bridge-01` @ `46b4791152fd87ced7e718df5ec3d91d394883ac`;
`reports/2026-08-20T0104Z_proj-01-integ_landing-record.md`,
`reports/2026-08-20T0324Z_recon-01b-b0-integ_landing-record.md`,
`reports/2026-08-20T0345Z_gapa-integ_landing-record.md`,
`specs/2026-08-20T1139Z_gapb-integ.md`.

## 2026-08-20 — Adjudication-source records, five registered and none answered

Date: 2026-08-20
Decision owner: Executor, adopted for the adjudication-source landing
Effect: registers five open records; answers none; settles nothing

### Decision

**`R-8` to `R-12` are OPEN RECORDS, not decisions and not findings with
verdicts. Nothing is settled by recording them.**

> **`R-8` — THE CITING ARTIFACTS ARE ENUMERATED, AND THE CITATION FORM IS
> AMBIGUOUS.**
> The landed artifacts citing or relying on an item of the adjudication
> document are: `specs/2026-08-19T2214Z_recon-proj-01.md:8`, which cites item 5
> by number; `specs/2026-08-19T2324Z_gov-housekeep-02.md`, whose §5 transcribes
> items 1, 2 and 4 and whose §7 disposes of item 7;
> `specs/2026-08-19T1723Z_registry-split-01.md:7`, which cites the ruling
> without a number as its `Origin`; `decisions/README.md:70-71` and `:87`;
> `docs/GOVERNANCE-DEBT.md:461`; and the reports and reviews bound to those
> specifications.
>
> **The form `PI ruling N` does not identify a unique ruling set.**
> `derivations/P2-RECON-EXT-01_discarded-external-space.md` cites `PI ruling 4`
> at `:14`, `:421` and `:437` as reserving the `TT_RECIPES` governance
> question, and `PI ruling 2` at `:471` as deferring a criterion until the
> magnitude is known; `reports/2026-08-19T0649Z_recon-ext-01-discarded-space.md`
> does the same at `:143` and `:332`. **Neither matches this document's item 2
> or item 4**, which concern the `CONVENTIONS.md` protection model and the
> retrospective reviews of `reviews/pi/` records. Two different numbered ruling
> sets are cited in the same form.
>
> **No citation is edited, and whether any needs amendment is not decided
> here.**
>
> **`R-9` — ONE ITEM'S SUBSTANTIVE QUESTION HAS SINCE MOVED.**
> Item 6 directs that the discarded-external-space diagnostic be extended, and
> frames it as a measurement task rather than a prerequisite. It was framed
> before `P2-OBS-IDENT-01`'s observable-identity finding, and `R-1` above
> already records that `D-2`'s purpose is undecided in consequence. **The item
> is landed in its stated words regardless**, and that the question has moved
> is recorded beside it, undecided.
>
> **`R-10` — WHETHER ANY ITEM'S EFFECTIVE DATE SHOULD BE FIXED, AND TO WHAT,
> IS OPEN.** The decision record states that the surviving evidence settles it
> in neither direction, and it fixes no date.
>
> **`R-11` — WHETHER THE UNNUMBERED BLOCK IS AN ITEM OF THE DOCUMENT IS OPEN.**
> The source carries one bold block, `Priority / sequencing`, that carries no
> number. It is recorded in the decision record as the reading returned it and
> is **not classified** either way.
>
> **`R-12` — A BLOCK ASSERTING IT REPRODUCES WHAT WAS RULED WAS FOUND NOT TO.**
> `docs/GOVERNANCE-DEBT.md:305`'s label `PI RULING, registered verbatim:`
> introduces a quotation that differs from the PI-confirmed source in what its
> item decides. **Whether other such labels hold is a question for the
> provenance census**, and is not answered here. No other label was measured.

**Which register admits each record, read from the registers' stated scopes.**

    DECISION_LOG.md
        ADMITS all five. Its head requires the entry template and
        append-only treatment, and the 2026-08-19 EXT-01 entry, the
        2026-08-20 OBS-IDENT entry and the 2026-08-20 R-5 entry are the
        precedent: open records adopted by an executor for an integration,
        each stating that nothing is settled by recording them.

    derivations/P2-DEFERRED-ITEMS.md
        DOES NOT ADMIT any of the five. It holds work CONSIDERED and
        consciously POSTPONED, carrying the PI's position at deferral, and
        its entries are added by PI decision. Its own text routes open
        questions elsewhere, naming `DECISION_LOG.md` entries that open an
        item as UNESTABLISHED.

    derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md
        DOES NOT ADMIT any of the five. It holds open items arising from the
        C-check line — `C1`, `C2`, `C3`. None of these arises from it.

    docs/GOVERNANCE-DEBT.md
        ADMITS `R-12`, and would admit `R-8`'s citation-form finding, both
        being governance-side. **Neither is entered there**, and the reason is
        that file's own `## Not entered here — D4`: a second entry would
        create a second place for one status to drift. The five are recorded
        once, here, in the series they continue.

### Reason

The records are consequences of a provenance landing, and Rule 17 forbids the
landing from drawing them. **Recorded here they can be found and taken up;
left in a landing record they are inherited silently.**

### Consequences

**Nothing is settled by these five records.** `R-8` edits no citation, `R-9`
re-specifies nothing, `R-10` fixes no date, `R-11` classifies nothing, and
`R-12` relabels nothing and audits no other label.

**No gate moves.** `Q1`, `GAP-A`, `GAP-B`, `A-EXT-01` and `H-EXT-01` are
unchanged in status. `G-13` remains `OPEN` and its disposition is unchanged.

**No count is incremented.** `R-9` restates a question `R-1` already carries,
and is recorded as restating it.

### Related gate

None.

### Related branch and files

`science/adjudication-source-02`;
`decisions/2026-08-20-adjudication-source.md`,
`docs/GOVERNANCE-DEBT.md`,
`specs/2026-08-20T1705Z_adjudication-source-02.md`,
`reports/2026-08-20T1705Z_adjudication-source-02.md`.

## 2026-08-21 — Census-integration records, three registered and none answered

Date: 2026-08-21
Decision owner: Executor, adopted for the provenance-census integration
Effect: registers three open records; answers none; settles nothing

### Decision

**`R-13` to `R-15` are OPEN RECORDS, not decisions and not findings with
verdicts. Nothing is settled by recording them.** They are consequences and
by-products of `P2-PROVENANCE-CENSUS-01`'s measured result, and Rule 17
forbids the integration that carried that result forward from drawing them.

> **`R-13` — THE PROVENANCE-TIER QUESTION IS OPEN.**
> The census measured provenance as a binary: an adjudication either has a
> landed record or it does not. In the course of that measurement it
> distinguished a third state — **an adjudication a register knows to have
> been ruled, and whose words that register does not carry**, pointing
> elsewhere for them. Four of the twenty-three landed adjudications are in
> that state, and one of them, `G-08`, points at a specification as the place
> its ruling is recorded.
>
> **The binary result is NOT revised.** Whether the model should be, and
> whether a register record that states an adjudication occurred without
> carrying its words is sufficient provenance, is **not decided here**.
>
> **`R-14` — THE CITATION-FORM FINDING IS OPEN.**
> Both the numbered and the named citation forms were measured non-unique.
> `PI ruling N` resolves to two distinct ruling sets; `PI ruling of this
> session` resolves to three distinct referents across four artifacts. **At
> least one citation resolves to nothing**: `derivations/P2-DEFERRED-ITEMS.md:199`
> names the `D-pre-A` ruling on the canonical kinetic operator as the
> authority for `DEFERRED-04`, and no such ruling is landed in the searched
> scope.
>
> **No citation is amended and no rule is proposed.** Whether either form
> should change is not decided here.
>
> **`R-15` — A METHOD FINDING, RECORDED FOR ADOPTION AND NOT ADOPTED.**
> **Set identities all evaluating true does not establish that the parser
> populated the sets correctly.** The census's own verification of its set
> relations passed while wrong: a character-class error dropped every member
> of one set from the parse, after which every relation held trivially — the
> empty set is a subset of anything, and subtracting it changes nothing. The
> error was caught because a cardinality was implausible, not because a
> relation failed.
>
> **Census-class verification therefore requires cardinality sanity, an
> independently written parser, or sentinel cases**, none of which the
> executor's check had. **This is recorded as a finding for adoption. It is
> not adopted here**, no rule is amended, and no existing verification is
> re-run under it.

**Which register admits each record, read from the registers' stated scopes.**

    DECISION_LOG.md
        ADMITS all three. Its head requires the entry template and
        append-only treatment, and the 2026-08-19 EXT-01 entry and the three
        2026-08-20 entries at :2506, :2593 and :2655 are the precedent: open
        records adopted by an executor for an integration, each stating that
        nothing is settled by recording them.

    derivations/P2-DEFERRED-ITEMS.md
        DOES NOT ADMIT any of the three. It holds work CONSIDERED and
        consciously POSTPONED, carrying the PI's position at deferral, and
        its entries are added by PI decision. None of these three is
        postponed work and none carries a PI position.

    derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md
        DOES NOT ADMIT any of the three. It holds open items arising from the
        C-check line — `C1`, `C2`, `C3`. None of these arises from it.

    docs/GOVERNANCE-DEBT.md
        ADMITS `R-13` and `R-14`, both being governance-side, and would admit
        `R-15` under its `METHOD NOTE` disposition. **None is entered there**,
        for the reason that file's own `## Not entered here — D4` gives: a
        second entry would create a second place for one status to drift. The
        three are recorded once, here, in the series they continue.

### Reason

The records are consequences and by-products of a reviewed measurement, and
Rule 17 forbids the integration carrying that measurement forward from adding
a classification the reviewed result did not carry. **Recorded here they can
be found and taken up; left in a landing record they are inherited silently.**

### Consequences

**Nothing is settled by these three records.** `R-13` revises no census value
and resolves no tier question, `R-14` amends no citation and proposes no rule,
and `R-15` adopts no method and re-runs no verification.

**No gate moves.** `Q1`, `GAP-A`, `GAP-B`, `A-EXT-01` and `H-EXT-01` are
unchanged in status. `G-13` remains `OPEN`.

**No count is incremented.** `R-13` restates no existing obligation; `R-14`
restates the citation-form finding already carried as `R-8` and is recorded as
restating it, not as adding to it.

### Related gate

None.

### Related branch and files

`science/provenance-census-01` @ `f69c1a1df5a7d9658ec4e9077cea3894300a1e16`;
`derivations/P2-PROVENANCE-CENSUS-01_census.md`,
`decisions/2026-08-21-specification-is-not-provenance.md`,
`specs/2026-08-21T0503Z_provenance-census-integ.md`,
`reports/2026-08-21T0503Z_provenance-census-integ.md`.

## 2026-08-21 — Mass-log measurement records, three registered and none answered

Date: 2026-08-21
Decision owner: Executor, adopted for the external-component measurement integration
Effect: registers three open records; answers none; settles nothing

### Decision

**`R-16` to `R-18` are OPEN RECORDS, not decisions and not findings with
verdicts. Nothing is settled by recording them.** They are consequences and
by-products of `P2-BETAV-EXTCOMP-01`'s measured result, and Rule 17 forbids
the integration that carried that result forward from drawing them.

> **`R-16` — INTERPRETATION IS OWED.**
> The measurement bears on `H-EXT-01`, which asks whether the axis-TT
> observable is the full physical response, and on `GAP-B`'s mismatches. **No
> task has read it against either.** Reading it is a separate task and is not
> performed at integration.
>
> **Nothing about the statuses changes by this record.** `H-EXT-01` remains
> `UNESTABLISHED` and `NOT ASSUMED BY RECON-01b`; `Q1` remains as its reviewed
> result left it; `GAP-A` and `GAP-B` are unchanged.
>
> **`R-17` — THE SIGN REVERSAL, AS A QUESTION ABOUT THE EXTRACTION.**
> The retained aggregate changes sign between the two frozen mass windows, and
> its spread across the frozen variant set exceeds the magnitude of either
> endpoint. **Why is unexplained**, and the measurement recorded it open rather
> than accounting for it.
>
> **Recorded with a constraint on how it may be approached: additional mass
> windows are not the way.** A window chosen after seeing a reversal is an
> estimator chosen on the evidence it is meant to test. **The question is prior
> to any further window**, and no further window is opened, proposed or scoped
> by this record.
>
> **`R-18` — A METHOD FINDING, RECORDED FOR ADOPTION AND NOT ADOPTED.**
> Two acceptance checks in the measurement task reported false negatives. One
> search term spanned a line break; one survived whitespace normalisation
> because the target text carried backticks that the normalisation did not
> strip. **The line-break case is a recorded lesson of this repository
> recurring. The backtick case is a variant the recorded lesson does not
> name.**
>
> **A normalisation that collapses whitespace but leaves markup delimiters in
> place is not sufficient for a presence check over marked-up text.**
> **Recorded as a finding for adoption. It is not adopted here**, no rule is
> amended, and no existing check is re-run under it.

**Which register admits each record, read from the registers' stated scopes.**

    DECISION_LOG.md
        ADMITS all three. Its head requires the entry template and
        append-only treatment, and the 2026-08-19 EXT-01 entry together with
        the entries at :2506, :2593, :2655 and :2770 are the precedent: open
        records adopted by an executor for an integration, each stating that
        nothing is settled by recording them.

    derivations/P2-DEFERRED-ITEMS.md
        DOES NOT ADMIT any of the three. It holds work CONSIDERED and
        consciously POSTPONED, carrying the PI's position at deferral, and its
        entries are added by PI decision. None of these three is postponed
        work and none carries a PI position.

    derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md
        DOES NOT ADMIT any of the three. It holds open items arising from the
        C-check line — `C1`, `C2`, `C3`. None of these arises from it.

    docs/GOVERNANCE-DEBT.md
        ADMITS `R-18`, which is governance-side and would sit under its
        `METHOD NOTE` disposition. **It does not admit `R-16` or `R-17`**,
        which are scientific questions about a measurement and not governance
        debt. **`R-18` is not entered there**, for the reason that file's own
        `## Not entered here — D4` gives: a second entry would create a second
        place for one status to drift. The three are recorded once, here.

### Reason

The records are consequences and by-products of a reviewed measurement, and
Rule 17 forbids the integration carrying that measurement forward from adding
a classification the reviewed result did not carry. **Recorded here they can be
found and taken up; left in a landing record they are inherited silently.**

### Consequences

**Nothing is settled by these three records.** `R-16` interprets nothing and
reclassifies nothing, `R-17` explains nothing and opens no window, and `R-18`
adopts no method and re-runs no check.

**No gate moves.** `Q1`, `GAP-A`, `GAP-B`, `A-EXT-01` and `H-EXT-01` are
unchanged in status. `P2-PHASE-01` does not advance.

**No count is incremented.** `R-18` restates no existing obligation; it is
adjacent to the observation-method defect class this repository already
records, and is recorded as a new instance of it rather than as a new
obligation.

### Related gate

None. `P2-BETAV-RECON-01` is referenced nowhere by these records and is
unchanged at `PROPOSED`.

### Related branch and files

`science/betav-extcomp-01` @ `7035e0b7b4a6eaeefb91900eefc0a74e78f78fa0`;
`derivations/P2-BETAV-EXTCOMP-01_external-component-mass-log.md`,
`results/P2-BETAV-EXTCOMP-01/external_component_mlog.json`,
`specs/2026-08-22T0021Z_betav-extcomp-integ.md`,
`reports/2026-08-22T0021Z_betav-extcomp-integ.md`.

## 2026-08-22 — XI line: observable, decomposition axis, and SI-2 ordering

Date: 2026-08-22
Decision owner: Principal Investigator
Effect: settles the three items `P2-XI-B0a` returned for PI ruling; registers
one H-type hypothesis as `UNESTABLISHED`

### Decision

**The ruling is an issued document, landed byte-exact. It is not reproduced
here**, because a transcription is not the record:

    Decision key   2026-08-22-xi-rulings-01
    Issued file    decisions/P2-XI-RULINGS-01.issued.md
    Issuance SHA-256
                   1f39b0f9c5cf2cd54fd5a2a0b38fa05ae454bb47a8fd81160f34485a7a2f6941
    git blob id    f793f9fd866f563480fbec6168553a2b967aea8f
    Register record
                   decisions/2026-08-22-xi-rulings-01.md

The document's sections, named and not paraphrased: `RULING 1` (the observable
the survival condition applies to), `RULING 2` (the ξ ledger's decomposition
axis, and the separation of that language choice from the physical
proposition), `RULING 3` (SI-2 ordering), `CROSS-RULING CONSISTENCY`, and
`ROUTING`.

**Document review verdict: `FIT FOR RECORDING`.** The artifact is
`reviews/chatgpt/2026-08-22_document-review_p2-xi-rulings-01.md`, sha256
`c96fc297c576b3d32954118161bd24799e6a28c6c52e64909afbe0fb3336b364`, self-bound
to the issuance SHA-256 above. It is reproduced verbatim in PART 2 of the
register record. **Under `decisions/README.md`'s adopted rule the review is
mandatory and non-gating**, and the decision took effect on issuance.

**One hypothesis registered, as `RULING 2`'s second `RULING` block directs:**

    ID              H-XI-SIGN-01
    File            assumptions/H-XI-SIGN-01.md
    Type            PHYSICAL HYPOTHESIS — directional, falsifiable
    Status          UNESTABLISHED — NOT ADJUDICATED BY P2-XI-RULINGS-01
    Statement SHA   8731037c16e485fd40d279cef827421cd733bc438ff828f1408dbdbd15488e90
    PART 2          REVIEW PENDING

### Reason

`P2-XI-B0a` completed a documentary scope assessment and returned three items
for PI ruling: the `SI-2` overlap, and two model-level questions its `A4`
fired on. **The executor did not decide them and could not**; the issued
document is the PI deciding them.

The hypothesis registration is directed by the ruling itself. The issued text
separates the PI's authority over ledger language from the physical
proposition, and states that the latter "cannot be established or refuted by PI
ruling".

### Evidence

The issued bytes, verified against the issuance SHA-256 before any write
(`M1`/`C1` of `specs/2026-08-22T2001Z_xi-rulings-landing_v2.md`). The carrier
of the registered hypothesis is `results/recovered-2026/session_log_full.md`
lines 177 and 197 at `main` `6da1f7cb`, extracted byte-exact and quoted
verbatim in the entry with working translations identified as translations.

### Consequences

**No gate moves.** `P2-MULTIPHASE-GRAV-01` (SI-2), `P2-CHANNEL-FREEZE-01` and
`P2-NORM-01` are unchanged in status. **No claim status changes.** **Nothing is
computed.**

**`RULING 2`'s forward-terminology effect was not exercised.** No existing
repository text was reworded by this landing; any such rewording proceeds under
the repository's clarification, erratum, or supersession mechanism, per the
issued text.

**`H-XI-SIGN-01` establishes nothing.** It is registered `UNESTABLISHED`, its
falsifier defers operational definition of "coupling structure" to a later
reviewed specification, and nothing landed depends on it.

### Supersedes

Nothing. The three items were open, not previously ruled.

### Related gate

`P2-MULTIPHASE-GRAV-01` (SI-2) is named by `RULING 3` and is unchanged at
`PROPOSED`. No gate section was modified.

### Related branch and files

`science/xi-rulings-landing-01`, cut from `main` `6da1f7cb`;
`decisions/P2-XI-RULINGS-01.issued.md`,
`decisions/2026-08-22-xi-rulings-01.md`,
`reviews/chatgpt/2026-08-22_document-review_p2-xi-rulings-01.md`,
`assumptions/H-XI-SIGN-01.md`,
`specs/2026-08-22T2001Z_xi-rulings-landing_v2.md`,
`reports/2026-08-22T2021Z_xi-rulings-landing.md`.
The assessment that returned the three items is on `science/xi-b0a` @
`012bdff3`, which this task does not integrate.

## 2026-08-23 — INDEX: executor identity for `P2-XI-RULINGS-LANDING-01`

Date: 2026-08-23
Decision owner: Principal Investigator
Effect: index entry only

### Decision

**This entry is a pointer, not the ruling's home.**

    Decision key      2026-08-23-xi-landing-executor-identity
    Canonical record  decisions/2026-08-23-xi-landing-executor-identity.md
    Subject           Claude Code was the designated executor for
                      P2-XI-RULINGS-LANDING-01 under AGENTS.md:86; the
                      reviewed specification's "Codex only" label is
                      superseded for executor identity only, for that
                      execution only

**The ruling's text is not transcribed here.** It is landed byte-identical in
the canonical record above, extracted from the reviewed integration
specification rather than retyped. Under the landed ruling that a
specification transcribing an adjudication is evidence of its content and not
that adjudication's canonical provenance record, a second transcription in
this log would create a second place for one text to drift.

### Reason

`P2-XI-RULINGS-LANDING-01` recorded, at §6a of its execution report, that its
reviewed specification named a different executor than the one the PI
announced in session, and returned the divergence rather than deciding it. The
PI confirmed. The confirmation needed a canonical home in `decisions/`, per the
four-way separation; this log receives the index.

### Evidence

`reports/2026-08-22T2021Z_xi-rulings-landing.md` §6a, on the source branch and
arriving in this integration. The ruling bytes as extracted from
`specs/2026-08-23T0000Z_xi-rulings-landing-integ_v4.md` lines 89–93, sha256
`ca6dbb3c30c37c99074594d4dcfb23692b230f146b800999d7287f36e84ff95f`.

### Consequences

**Nothing scientific changes.** No measurement, no scope, no acceptance
criterion, and no re-execution — the ruling says so in its own words. **No gate
moves and no claim status changes.**

**The forward executor-field convention is NOT landed.** It is a Researcher
authoring practice unless and until the PI issues it as a ruling.

### Supersedes

Nothing. It supersedes no landed decision. **Within its own scope it supersedes
a specification field** — `specs/2026-08-22T2001Z_xi-rulings-landing_v2.md`'s
`Execution` field, for executor identity only and for that execution only. That
field is not rewritten and stands as the reviewed bytes it always was.

### Related gate

None. This is a governance record.

### Related branch and files

`science/integrate-xi-rulings-landing-01`, cut from `main` `6da1f7cb`;
`decisions/2026-08-23-xi-landing-executor-identity.md`,
`specs/2026-08-23T0000Z_xi-rulings-landing-integ_v4.md`,
`reviews/chatgpt/2026-08-23T0000Z_xi-rulings-landing-integ_v4.md`.

## 2026-08-23 — Q-M2 / Q-M3 disposition: routes declined, two tasks authorized

Date: 2026-08-23
Decision owner: Principal Investigator
Effect: disposes the three routes offered at the `P2-XI-LEDGER-01` execution
report; defers membership; authorizes two tasks

### Decision

**The ruling is an issued document, landed byte-exact. It is not transcribed
here**, because a transcription is not the record:

    Decision key   2026-08-23-xi-rulings-02
    Issued file    decisions/P2-XI-RULINGS-02.issued.md
    Issuance SHA-256
                   ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5
    git blob id    72a6b24c9289efde8a096e4e591ff01728323473
    Register record
                   decisions/2026-08-23-xi-rulings-02.md

The document's sections, named and not paraphrased: `RULING 1` (routes declined;
membership deferred), `RULING 2` (`Q-M3`: the undone dependence check is
authorized), `RULING 3` (`Q-M2`: a scope assessment precedes any computation),
`RULING 4` (ordering), and `ROUTING`.

**Document review verdict: `FIT FOR RECORDING`.** The artifact is
`reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02.md`, sha256
`d1d117f28572f8eb19f76a316147f111af96d048dc02559465590f704a984d49`, self-bound
to the issuance SHA-256 above and reproduced verbatim in PART 2 of the register
record. **Under `decisions/README.md`'s adopted rule the review is mandatory
and non-gating**, and the decision took effect on issuance.

### Reason

`P2-XI-LEDGER-01` assembled a conditional total over two OPEN ledger rows and
offered the PI three routes for their disposition. The executor did not choose
among them and could not; the issued document is the PI choosing.

### Evidence

The issued bytes, verified against the review-declared identity before any
write. The subject of the ruling's `SCOPE` is pinned by full SHA and its OPEN
rows were read directly from the pinned commit.

### Consequences

**No gate moves.** `P2-MULTIPHASE-GRAV-01` (SI-2), `P2-CHANNEL-FREEZE-01` and
`P2-NORM-01` are unchanged in status. **No claim status changes.** **Nothing is
computed.**

**The two OPEN ledger rows remain OPEN.** The issued document defers membership
in its own `RULING 1`, and this landing adds no disposition.

**The two authorized tasks are NOT specified, scheduled, or begun by this
landing.** Each is a separate specification subject to the normal pre-execution
review gate, and each will cite the ruling at its landed path.

**Chronology, recorded as fact:** `P2-XI-LEDGER-01` exists as a completed
reviewed measurement at `science/xi-ledger-01` @
`8f9edfead214b5bb3337924c18c5d241274e97c3` and is **not** landed on `main` at
this task's Base `9eefe4c85c646b96ce334426598bc0e405f6e3d5`; this landing does
not integrate it.

### Supersedes

Nothing. The two rows were open, not previously ruled.

### Related gate

None directly. `P2-MULTIPHASE-GRAV-01` (SI-2) is named in the issued document's
rationale only and is unchanged at `PROPOSED`. No gate section was modified.

### Related branch and files

`science/xi-rulings-02-landing`, cut from `main` `9eefe4c8`;
`decisions/P2-XI-RULINGS-02.issued.md`,
`decisions/2026-08-23-xi-rulings-02.md`,
`reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02.md`,
`specs/2026-08-23T0900Z_xi-rulings-02-landing_v3.md`,
`reviews/chatgpt/2026-08-23T0900Z_xi-rulings-02-landing_v3.md`,
`reports/2026-08-23T1540Z_xi-rulings-02-landing.md`.

## 2026-08-24 — Open item: family-wide representation stability of the ξ ledger is UNESTABLISHED

Date: 2026-08-24
Decision owner: Principal Investigator
Effect: opens the representation-stability inquiry as an open item

### Decision

The open item, reproduced from the clarification that directs its registration:

> **Open item — family-wide representation stability of the induced ξ ledger.**
>
> `P2-XI-RULINGS-02-CLARIFICATION-01` scopes the `Q-M3` dependence check to the
> landed decoupling — the Hubbard–Stratonovich transformation of the assembled
> chain — and states that **a family-wide representation-stability inquiry is
> NOT part of that task**, directing instead that it "is to be registered as a
> named open item, linked to the representation-stability disclosure of
> `P2-FIERZSUM-01 §8`".
>
> **The question, as the clarification states it and no broader:** whether the
> ledger's representation is reliable across a decoupling family — in the
> clarification's own words, "it concerns the reliability of the representation
> across a decoupling family, whose membership is itself an unlanded
> model-level choice".
>
> **Link.** `P2-FIERZSUM-01 §8`'s representation-stability disclosure, which
> that gate lists at `derivations/P2-FIERZSUM-01.md:231-233` as deliverable 8 —
> "how far `ξ_ind` moves under change of decoupling within a preregistered
> family (§7, Route B) — reported as a number with its qualifications, never
> asserted zero" — and whose scan `:464` names as producing `Δ_Fierz^(F)`.
>
> **Escalation condition, quoted BYTE-IDENTICAL from the clarification at
> `decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md:36-40`:**
>
> ```text
                escalation condition: if the check returns DEPENDENT
                and the term is subsequently found to grow with L, the
                representation-stability inquiry escalates to required
                status; otherwise it remains registered at ordinary
                priority.
> ```
>
> **Its decoupling-family membership is an unlanded model-level choice.** The
> clarification says so in the words quoted above; the family over which
> stability would be assessed is not fixed by landed state.
>
> **Status: UNESTABLISHED. REGISTERED, NOT AUTHORIZED.**
>
> **Registration is not authorization.** Nothing in this entry begins,
> schedules, constrains or prioritises this inquiry, the `Q-M3` dependence
> check, or the `Q-M2` scope assessment. **The escalation condition is recorded,
> not triggered:** it requires both that the check return `DEPENDENT` and that
> the term be subsequently found to grow with `L`, and this entry establishes
> neither.

### Reason

**Authority: the PI ruling recorded at
`decisions/2026-08-24-xi-open-item-register-routing.md`, decision key
`2026-08-24-xi-open-item-register-routing`.** That ruling determines that the
applicable register for this item is `DECISION_LOG.md`'s `UNESTABLISHED` entry
mechanism — the route `derivations/P2-DEFERRED-ITEMS.md`'s own text names for
open questions.

**The ruling's scope limit, stated as the ruling states it: for this item
only.** It extends or modifies no register's scope, creates no register, and
makes no general determination about where future XI-line open items are
registered.

The landing task's `M4` had stopped because no register's stated scope had been
shown to admit the item; the measurement is at
`reports/2026-08-24T0043Z_xi-clar-01-landing.md` §5. This entry is that stop's
resolution, under the ruling, and follows the format of the landed
`UNESTABLISHED` precedent at `DECISION_LOG.md:2147-2215`, whose own `Reason`
records that "this log is the register whose stated scope covers an item opened
as `UNESTABLISHED`".

### Consequences

**Nothing scientific changes.** No gate moves, no claim status changes, no
measurement is made, and the two OPEN ledger rows of `P2-XI-LEDGER-01` remain
`OPEN(Q-M2)` and `OPEN(Q-M3)`, valueless.

**No task is authorized.** `P2-XI-RULINGS-02` authorizes the `Q-M3` check and
the `Q-M2` scope assessment; this entry authorizes neither, and authorizes no
representation-stability work.

**`Q-M3` remains conditional on the landed Hubbard–Stratonovich decoupling**,
per the clarification, and the family-wide residue stays here rather than
attaching to that binary membership check.

### Supersedes

Nothing. The item was directed and unregistered; it is now registered.

### Related gate

None. `P2-FIERZSUM-01` is landed as a concept note, not registered, and is
unchanged.

### Related branch and files

`science/xi-clar-01-landing`, resumed from `2936e967`;
`decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md`,
`decisions/2026-08-24-xi-rulings-02-clarification-01.md`,
`decisions/2026-08-24-xi-open-item-register-routing.md`,
`specs/2026-08-24T0900Z_xi-clar-01-landing_v3.md`,
`reviews/chatgpt/2026-08-24T0900Z_xi-clar-01-landing_v3.md`.

## 2026-08-24 — INDEX: Ruling-2 scope clarification, landed

Date: 2026-08-24
Decision owner: Principal Investigator
Effect: index entry only

### Decision

**This entry is a pointer, not the clarification's home.**

    Decision key      2026-08-24-xi-rulings-02-clarification-01
    Issued file       decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md
    Issuance SHA-256  0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22
    git blob id       1786124bbe3bfa02809d83c2890d0800e0d3edd8
    Register record   decisions/2026-08-24-xi-rulings-02-clarification-01.md
    Document review   FIT FOR RECORDING
                      reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02-clarification-01.md
                      sha256 c586f0a4c0ec5023705dcac88f4db4b88ff911b99fa3324b3973031b5cad3018
    Open item registered by this landing
                      the 2026-08-24 entry above — "Open item: family-wide
                      representation stability of the ξ ledger is UNESTABLISHED"

**The clarification's text is not transcribed here.** It is landed byte-exact
in the issued file above, and quoted in the register record. Under the landed
ruling that a specification transcribing an adjudication is evidence of its
content and not that adjudication's canonical provenance record, a second
transcription in this log would create a second place for one text to drift.

### Reason

`P2-XI-RULINGS-02-CLARIFICATION-01` fixes the representation on which the
`Q-M3` dependence check is performed and directs the registration of one open
item. The clarification needed a canonical home in `decisions/`, per the
four-way separation; this log receives the index, and — separately, under the
PI ruling recorded at
`decisions/2026-08-24-xi-open-item-register-routing.md` — the open item itself.

### Consequences

**Nothing scientific changes.** No gate moves; no claim status changes; the two
OPEN ledger rows of `P2-XI-LEDGER-01` remain OPEN. The clarification changes no
ruling of `P2-XI-RULINGS-02`, issues no membership ruling, and authorizes no
task — its own words.

**No task was begun, scheduled, constrained or prioritised** by this landing:
not the `Q-M3` check, not the `Q-M2` scope assessment, and not the registered
representation-stability inquiry.

**This landing does not make the clarification canonical on `main`.**
Integration is a separate reviewed task and is not performed here.

### Supersedes

Nothing. It supersedes no landed decision.

### Related gate

None. This is a governance record.

### Related branch and files

`science/xi-clar-01-landing`;
`decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md`,
`decisions/2026-08-24-xi-rulings-02-clarification-01.md`,
`decisions/2026-08-24-xi-open-item-register-routing.md`,
`reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02-clarification-01.md`,
`specs/2026-08-24T0000Z_xi-clar-01-landing_v2.md`,
`specs/2026-08-24T0900Z_xi-clar-01-landing_v3.md`,
`reports/2026-08-24T0043Z_xi-clar-01-landing.md`.
