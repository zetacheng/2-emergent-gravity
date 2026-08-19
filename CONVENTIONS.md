# Convention Registry

No calculation may begin until every relevant convention below is filled,
reviewed, and locked for the applicable gate. **These conventions were fixed
before any computation in gates `P2-HK-01`, `P2-GAP-01`, `P2-BETA-01`, and
`P2-BETAV-01`, and were not adjusted afterwards to reproduce a paper value.**

## Locked conventions for the independent-verification sweep

| Convention | Value |
|---|---|
| Metric signature | Euclidean, `(+,+,+,+)`, `d = 4`. Curvature sign: `R > 0` on a sphere (`R = +d(d-1)/a²` for a `d`-sphere of radius `a`). |
| Wick rotation | All loop integrals performed in Euclidean signature. `∫ d⁴p_E` with `p²≡p_E² ≥ 0`. |
| Fourier transform | `f(x) = ∫ d⁴p/(2π)⁴ e^{ipx} f̃(p)`; loop measure `∫ d⁴p/(2π)⁴`. |
| Heat-kernel operator | `Δ = −∇² + E` (Laplace-type). `E` is the endomorphism (potential/bundle) term; **sign convention: `E` enters with a `+` so that a scalar curvature coupling `ξR` appears inside `E` as `E ⊃ +ξR`.** The mass `m²` is separated out explicitly (`Δ + m²`) and is **not** counted inside `E` for the `a_k`. |
| Heat-kernel expansion | `Tr e^{−τΔ} = (4πτ)^{−d/2} ∫ d^dx √g Σ_{k≥0} a_k(x) τ^k`, `d=4`. Indexing: `a_0 = tr 𝟙`, and `a_1 = tr[(1/6)R·𝟙 − E]` (the `R`-linear Seeley–DeWitt coefficient). This is the "`a_1`/`b_2`" in the τ-power indexing; some references call it `b_4`. |
| Curvature coupling of scalar | Non-minimal coupling term `½ ξ R φ²` in the action ⟹ `E = ξ R` for the scalar; minimal coupling is `ξ = 0`. The conformal value in `d=4` is `ξ = 1/6`. |
| Dirac operator squaring | `−(γ·∇)² = −∇² + (1/4)R` (Lichnerowicz), so for a Dirac fermion `E = (1/4)R·𝟙₄` on the 4-component spinor bundle; the fermion loop carries an overall statistics sign `−1` relative to a real boson. |
| Massive-vector (Proca) structure | `Z_{s=1,m} = det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)`, with the vector Laplacian `Δ^{(1)}` having `E^{μ}{}_{ν}=R^{μ}{}_{ν}` (`tr E = R`) and the Stueckelberg scalar `Δ^{(0)}` having `E=0`. This determinant structure is taken as an input from the paper; the coefficient it implies is what we compute. |
| Definition of `Z(m²)` | The induced axis/transverse-traceless (TT) graviton kinetic coefficient, i.e. the coefficient of the induced Einstein–Hilbert term `∫√g R` normalized **per unit `4N`** of fermionic degrees of freedom (`4` spinor components × `N` flavors). Concretely `Z ≡ 1/(16πG_ind)` in the TT channel, expressed per `4N`. The `m²ln m²` piece defines the species coefficient: `Z ⊃ β_s · m² ln m²`. |
| Species coefficient `β_s` | Coefficient of `m² ln m²` in `Z(m²)`. Computed from `a_1`: `β_s = −p_s (4π)^{−2} (tr a_1 / R)`, where `p_s` is the log-det prefactor of the species (`+1/2` per bosonic `det^{−1/2}` factor, `−1/2` per `det^{+1/2}` factor / fermion loop). Reported both as a raw value (this convention) and as convention-independent ratios `β_F/β_B`, `β_V/β_B`, `β_B(ξ)/β_B`. |
| Definition of `L` | `L ≡ ln(Λ²/m²)`. The mass `m` is measured **in units of the cutoff `Λ`** (i.e. `Λ ≡ 1` unless a gate states otherwise), so `L = −ln m²` in those units. `ln m²` and `L` differ only by sign and the `ln Λ²` reference. |
| Regularization | **Sharp Euclidean 4-ball `|p| < Λ`** for all continuum momentum integrals, unless a gate explicitly states another regulator. |
| Lattice regularization | Hypercubic lattice, spacing `a` (`a ≡ 1` in lattice units), Brillouin zone `p_μ ∈ (−π, π]`. Free-field lattice momenta: `p̂² = Σ_μ 4 sin²(p_μ/2)` (naive/scalar), `s̄_μ = sin p_μ`, Wilson term `W(p) = r Σ_μ (1 − cos p_μ)` with Wilson parameter `r = 1`. |
| Sign of the action | Euclidean action `S_E ≥ 0`; `Z = ∫ e^{−S_E}`, effective action `W = −ln Z`. Boson: `W = +½ Tr ln(Δ+m²)`. Dirac fermion: `W = −Tr ln(iγ·D − m) = −½ Tr ln(−(γD)² + m²)`. |
| Gamma matrices | Euclidean, Hermitian `γ_μ = γ_μ^†`, `{γ_μ,γ_ν} = 2δ_{μν}`, `tr 𝟙₄ = 4`. |
| Gamma5 | `γ_5 = γ_1γ_2γ_3γ_4`, Hermitian, `γ_5² = 𝟙`, `{γ_5,γ_μ}=0`. |
| Generator normalization | Not used in gates `P2-*` (single-species loops); `tr(T^aT^b)=½δ^{ab}` if flavor generators are ever needed. |
| Flavor basis | `N` degenerate flavors; the induced coefficient is reported per unit `4N`. |
| Field dimensions | Canonical: scalar `[φ]=1`, Dirac `[ψ]=3/2` in `d=4`. |
| Cutoff and lattice units | `Λ ≡ 1` (continuum), `a ≡ 1` (lattice); masses quoted as `m/Λ` or `m a`. |
| Definition of attractive and repulsive channels | Scalar (`ψ̄ψ`) condensate channel is the attractive channel driving the gap; the four-fermion coupling `G > 0` is attractive there. |
| Normalization of Green functions | Euclidean Wilson propagator `S(p) = 1/(iγ·s̄(p) + W(p) + m)`; scalar `1/(p̂²+m²)`. |
| Gap-equation integral `I_0` | `I_0` is defined by the linearization of the mean-field gap equation about zero condensate, `1 = 2 G_c I_0`; the precise integrand and the derivation of the relation `G_c = 1/(2I_0)` are given in the `P2-GAP-01` derivation note and script. |
| Statistical-error convention | Numerical uncertainties are reported as spreads over discretization / fit-window / ansatz variations (systematic), not as formal fit errors alone. Convergence is demonstrated by grid refinement and half-shifted (offset) grid cross-checks. |

## Change control

Any change to a locked convention after a gate has been committed must be
recorded as a new `DECISION_LOG.md` entry that supersedes the prior one, and
must trigger re-examination of every gate that consumed it. Conventions are
never changed silently, and never changed in order to reach a target number.

## Execution discipline for decisive runs and merges

These rules bind prospectively only. They imply no retrospective action for
campaigns run under prior discipline and alter no interpretation of previously
approved scientific results; in particular, the Arm H `INCONCLUSIVE` verdict
is untouched.

### 1. Contradiction-stop

Origin: `reports/2026-07-22_betav-arm-h-decisive_report.md` §1e.

A gate-bookkeeping task that changes a gate status MUST enumerate, in its
frozen scope, the specific governance-test updates that status change entails
(pre-authorized test diffs, listed by test name); and the executor MUST stop
and report on any conflict between frozen-scope clauses — a contradiction in
the prompt is itself a reportable defect, never something to resolve
unilaterally.

This rule has been in force since 2026-07-22 and is relocated here for
discoverability, not newly created; it was applied in commit `6f32d10`. This
rule is normative regardless of where it was first recorded.

### 2. Scope precedence

When an execution prompt and a repository rule (or the authorized scope) are
or appear inconsistent, the executor MUST stop immediately and report. The
inconsistency is itself a governance finding. The executor SHALL NOT infer,
assume, or decide which instruction takes precedence — precedence is
determined by the PI and reviewers, never by the executor.

### 3. Declared frozen scope is normative

A decisive or gate-bookkeeping prompt MUST declare its frozen file set
explicitly. Before the gate is updated, the commit's changed-file list MUST be
compared against that declared set — `git diff --name-only <base>..<head>` —
and any file outside it reported. The declared frozen file set is
authoritative. It SHALL be treated as normative: a file outside it constitutes
an authorization failure, not a matter of review judgement. A checker script
consuming a declared manifest is to be implemented separately; until it
exists, the manual comparison is mandatory and its output MUST be recorded in
the run report.

**Amendment H, adopted 2026-08-09 — literals are verified by execution.**

**A specification that requires a literal or normalised-text match
MUST have had the specified match executed against the target text by
its author before issue.** Asserting a literal is not verifying it.

**The specification MUST distinguish two kinds of check:**

    byte- or character-exact    no representation-changing
                                normalisation is permitted
    normalised substantive      one explicitly defined normalisation
                                function, applied to BOTH the
                                requirement and the target

**Once blockquote prefixes are stripped or whitespace collapsed, the
check is no longer an exact string match** — and some literals cannot
tolerate that: a SHA, a JSON key, a Markdown heading a script locates
by. **Say which kind each check is.**

**The specification MUST state which representation features are
SEMANTIC for that check and which are normalised away.** Do not write
that representation is ignored in general — for some literals the
representation IS the substance:

    normally normalisable   blockquote prefixes, line wrapping
    depends on the target   Markdown emphasis, code delimiters
    usually SEMANTIC        Unicode dashes, exact SHAs and blob ids,
                            JSON field names, Markdown headings a
                            script locates by, code identifiers,
                            regex tokens

**The normalisation MUST be a single function applied to BOTH the
requirement and the target**, specified as a function rather than as a
list of removals. **Stripping can manufacture a match the raw text does
not contain as easily as it can repair one it does**; applying one
function to both sides is the property that makes the check auditable.

**The specification MUST record the target, the normalisation, the
verification method, and that the check PASSED before issue** — for
example: *"Pre-issue literal verification: PASS after stripping
blockquote prefixes and collapsing whitespace; code delimiters
stripped; en dashes preserved."* **Raw authoring output may be
retained in the review record rather than embedded in the
specification**, so that a specification does not fill with tool
transcripts.

Where the literal is itself sensitive — **especially a hash, an object
id, a machine-consumed heading, or an identifier** — the expected
value and the executable verification method MUST be written out.
**This is not required of every exact heading**: a specification with
ten of them should not carry ten shell commands. It applies where the
literal is consumed by machine or where a near-match would pass
unnoticed.

### 4. Execution prompts are evidence

The execution prompt governing any decisive or pre-registered run MUST be
committed to the repository, AND its sha256 recorded in the run's report,
before the run begins.

### 5. Minimum mandatory merge discipline

The following is a floor which may not be reduced; it is not an adaptable
checklist. The `gate/p2-betav-cleanup` merge (`fd5f6b9`) is an exercised
precedent.

1. Working tree: no tracked file modified, staged, deleted, renamed or
   conflicted. Untracked paths MUST be enumerated and explicitly accepted, and
   the approval MUST itself be recorded with its source. Nothing may be
   stashed, cleaned or discarded to satisfy this.
2. Ancestry checked after fetching; merge the pinned REMOTE ref, never a local
   branch. If the base has moved past the reviewed base, do not merge —
   approval covers branch AND base together.
3. Scope checked BEFORE merging: changed-file list limited to the declared
   set; diff restricted to protected paths (`scripts/ tests/ results/
   derivations/ reports/`) MUST be empty.
4. After merging, verify both parents AND `git diff --name-only HEAD^1..HEAD`;
   correct parentage does not imply a correct tree.
5. Re-verify by fixed-string grep that pinned artifact digests survive the
   merge unchanged.
6. Any merge conflict is an immediate STOP: do not resolve, do not edit either
   side, do not force a strategy.
7. No environment repair and no dependency installation: no `pip`, `poetry`,
   `conda`, `uv`, or equivalent installation of any kind; no venv changes; no
   validator reconfiguration; no formatters, no repository-wide maintenance.
   Nothing outside the merged files may change by any mechanism, including
   automated ones.
8. Push verification: `git rev-parse HEAD` and `git rev-parse origin/main`
   identical; record `git merge-base HEAD^1 HEAD^2`.
9. Overriding rule: if any required command produces an unexpected result,
   STOP; do not repair the repository, do not retry by changing its state,
   report the exact output. This takes precedence over the instruction to
   complete the merge.

**Amendment K, adopted 2026-08-09 — re-issuing an executed specification.**

**TASK-IDENTITY PATHS are paths whose names identify a particular
execution instance** — ordinarily its specification and its report,
plus any other path the specification explicitly designates as
execution-specific. **Canonical target files are NOT task-identity
paths.**

**A specification that has already been executed and pushed MUST NOT
be re-issued against the same branch while reusing the same
task-identity paths.** A re-issue proceeds on a NEW branch cut from
the evidence base, under a NEW task name and NEW specification and
report `{HHMM}` paths.

**Canonical target paths the task exists to populate or modify may
remain the same** — an append-only log, a registry, a named
derivation — **provided the new branch starts from the original
evidence base and the re-issue specification explicitly authorizes
them.** Only the paths that identify the task are required to change.

**The original branch is preserved UNTOUCHED and is identified as
superseded in the re-issue specification and report**; it is not
rewritten, reset, force-pushed, or carried forward. **A Git branch ref
carries no such marker, so the identification lives in the documents,
not in the ref.**

**A superseded branch MUST NOT be integrated.** `docs/BRANCHING_POLICY.md`'s
authorization machine has `PENDING_DELETE`, `NOT_AUTHORIZED` and
`ABSENT_FROM_REMOTE` and **no state for superseded, never to be
integrated** — so a later integrator reading the branch list would see
two branches claiming to land the same entries. **Either that state is
added or this prohibition is stated where an integrator will meet it.**
This is Amendment E(iii) again: a missing state forcing a
conservative-but-wrong label.

Branch-specific merge mode and allowed-ref policy are defined in
`docs/BRANCHING_POLICY.md`.

**Append-only and forbidden-delete are evaluated against the LAST
PUSHED STATE OF THAT BRANCH, as well as against the evidence base.**
A re-issue on a new branch starts from the original evidence base and
**does not inherit the superseded branch's append-only history.** A record already
pushed and then removed or replaced by a later commit is not
append-only for the branch's operative content, **even though the old
commit survives in Git history.** Evaluating only against a distant
base would let any append-only file be rewritten by rebuilding it from
that base.

**Local iteration before a push is unaffected.** Committing a log
entry and correcting a typo in it two commits later, before anything
is pushed, is ordinary work and is not a violation. **An earlier draft
said "immediate parent-to-child", which would have forbidden that.**

**The re-issue mechanism is supplied by the specification, not derived
by the executor.** A re-issued specification that does not say how the
second execution is to be represented **is a specification defect**,
and the executor's correct response is: **stop before the first
irreversible or authority-expanding step; complete only those
remaining observations or local checks that are independently
authorised and do not alter protected or remote state; then report the
unresolved construction for authorization.**

**"Authorised" is the operative test, not "reversible".** Some
read-only observations have no meaningful notion of reversibility, and
some local commits are technically reversible while not being
authorised at all.

**A bare stop would have delivered nothing** — no entries, no
register, no analysis of the collision. **What serves the PI is the
full work, the conflict laid out, and the choice.** A rule that reads
as "produce nothing when uncertain" teaches silence, which is the
opposite of what this discipline is for.

**This describes required behaviour; it does not create a named
state.** If a formal `PARTIAL_STOP` state is wanted — with its own
semantics for what may be committed, pushed and reported — **it should
be defined deliberately elsewhere, not created in passing here.**

**The general trigger, of which re-issue is one instance.** **If
resolving an apparent inconsistency requires a construction the
specification does not describe, that is a stop-before-push and a
request for authorization — not a resolution.** Re-issue is the worked
example below; the next instance will not be a re-issue.


**Amendment P, adopted 2026-08-14 — the integration authorization states its landing outcome, and an auto-merge is verified by content and not only by blob.**

**Mechanism marker: RULE + MECHANISM DEFERRED.**

Rule 5's numbered floor governs the merge itself. **This amendment adds one
obligation before it and one after it.**

**(a) AN INTEGRATION SPECIFICATION STATES ITS LANDING OUTCOME INLINE**,
including when the outcome is "do not advance". **A complete, reviewed
integration whose specification is silent about the landing leaves `main`
unmoved**, because no clause authorises the advance and the executor may not
supply one. *Incident: exactly that occurred, and the branch sat integrated
and unlanded.*

**The landing target is named as the task's own final report commit, not as a
SHA.** **A SHA naming a commit that carries the task's review is unreachable
as a landing target**, because Rule 15 places the report commit after it. A
specification that names a SHA has named something the task will have moved
past by the time it lands.

**(b) FOR AN AUTO-MERGED FILE, BLOB DIFFERENCE FROM BOTH SIDES IS A NECESSARY
CONDITION AND NOT A SUFFICIENT ONE.** Rule 5 point 4 already records that
correct parentage does not imply a correct tree; **this is the same
observation one level down.** A merged blob differing from both parents rules
out one side having been taken wholesale **and rules out nothing else.**

**Where a file was auto-merged from two sides that both changed it, the
verification MEASURES LINE SURVIVAL: every line each side added over the
merge-base, checked for presence in the merged file, with the count missing
reported and expected to be zero.** *Incident: an executor measured 90/57,
104/133 and 24/61 added lines across three auto-merged files with zero
missing — beyond what its criterion required, which had asked only for blob
difference.*

**This is a necessary condition too, not a sufficient one.** Line survival is
set membership; **it does not establish correct interleaving, and it is not a
substitute for running the merged behaviour.** The verification that a merged
parser still works is the suite, not the diff.

**What is deferred.** **No mechanism enforces either obligation.** For (a),
nothing inspects a specification for a landing clause. For (b), **no
mechanism measures line survival**: `merge_guard.py` compares merge-base
identity and `P5` recomputes parentage, and neither examines file content.
**The line-survival check is fully specifiable and cheap** — it needs the
merge-base, two sides and the merged file, all of which the checker already
resolves — **and it is not currently registered as a mechanism item.**
**Registering it is `C-c`'s.**

### 6. Reporting honesty for merges

A report MUST distinguish "the main worktree carries approved untracked
paths" from "the repository is clean"; state which worktree was clean.

A validator that examined nothing MUST NOT be recorded as a pass. For example,
`ruff check` on Markdown files returns "All checks passed" together with "No
Python files found"; it verified nothing. Substantive verification for a
documentation merge is: governance tests, scope diff, digest checks, and a
clean merge worktree.

### 7. Evidence precedence

When repository state, committed artifacts, and narrative reports disagree,
the committed artifacts take precedence. Reports explain; artifacts govern.
Any claim about the state of the repository — by any agent, in any review, at
any time — MUST be verified against the committed artifacts before it is
relied upon or recorded.

This rule arose from the Arm-H audit, in which several claims about repository
state, made from recollection of prior sessions rather than from inspection,
were found on checking to be incorrect. Verification against artifacts is not
optional courtesy; it is the governing evidential rule.

**Amendment A, adopted 2026-08-09 — mid-task authorizations are reproduced verbatim in the task report.**

Where a task specification is amended mid-task, the amendment's text
MUST be reproduced verbatim in the task report, together with: the
**authorizing authority**; the **time or sequence point** at which it
was issued, so that "before the commits" can be distinguished from
"after them"; and the specific **acceptance criterion, scope manifest,
invariant or prohibition** it superseded or extended. A report that
omits any of these is incomplete regardless of how correct the
repository state is.

**Where the amendment changes a frozen path manifest, authorizes an
otherwise prohibited repository modification, or changes an expected
governance outcome, the report MUST reproduce the amended manifest or
criterion IN FULL**, not summarise it.

**Prior authorization and retrospective ratification are different
things and MUST be named differently.** An instruction issued BEFORE
the affected action is a *mid-task amendment* or *authorization*. An
instruction issued AFTER it is a *retrospective ratification*, and
**MUST NOT be described as prior authorization**. The report records
the two distinctly.

**Retrospective ratification may affect the task's disposition, but it
does not make the earlier action authorized at the time it occurred.**
This is the same principle as Rule 14's: an acceptance changes what is
done about a fact, never the fact.

No separate amendment artifact is required: a committed task report
carrying all of the above is a sufficient audit chain, and requiring a
file per amendment would multiply artifacts without adding evidence.

*Incident.* Two commits in the integration task were explicitly
authorized mid-task — a digest correction and the addition of a task
record to the frozen scope manifest. Neither authorization existed
anywhere except in conversation. The independent reviewer, reading only
the final report, could not distinguish an authorized amendment from an
executor expanding its own scope, and correctly raised both as possible
violations. Resolving them required the specifier to supply evidence
after the fact.

*Why verbatim.* A summary of an amendment is not the amendment. What a
later auditor needs is the wording the executor was actually working to,
so that the executed result can be checked against it rather than
against a paraphrase written once the outcome was known.

**This does not require mid-task amendments to be reviewed before
issue** — the PI may amend a task in flight without a review cycle. It
requires only that the amendment become visible in the artifact the
reviewers read.


**Amendment M, adopted 2026-08-14 — a recorded measurement states its scope, and does not exceed it.**

**Mechanism marker: RULE + MECHANISM DEFERRED.**

Rule 7 requires a claim about repository state to be verified against the
committed artifacts. **This amendment governs the SCOPE of that verification
and how the resulting statement is worded.** A verification performed
correctly over part of a subject, and recorded as though it covered the
whole, satisfies Rule 7's letter and defeats its purpose.

**Four obligations, which are one discipline in four costumes: a recorded
statement may not claim more than the measurement behind it supports.**

**(a) A measurement written into a verification record is taken over the
WHOLE subject.** No `head`, no `tail`, no sampled or scrolled view.
**Where a tool truncates by default, the record names the flag or method
that defeated the truncation**, or states that the full output was read.
*Incident: three recording errors came from truncated output — a register
count cut at eighty lines, a merge list cut at twenty-two, an open-item list
cut at sixty.*

**(b) A verification statement is CLONE-INVARIANT.** A statement about the
repository must be true in any clone of it. **"The object is not present" is
a function of local garbage collection; "the object is not an ancestor of any
ref" is a property of the repository.** Where only the clone-local form was
measured, the record says so and does not present it as a repository
property. *Incident: a `MEASURED` line asserted the former and was true only
in the clone that produced it.*

**(c) A count of diff hunks NAMES THE DIFF CONTEXT it was taken at.** A hunk
count is not a property of a change; it is a property of a change and a
context setting together. *Incident: three logical edits produced three hunks
at `--unified=0` and one at git's default, and the criterion said only "three
hunks".*

**(d) EVIDENCE ABOUT A CRITERION IS LABELLED EVIDENCE, NEVER DISCHARGE.**
**A criterion is discharged by the task that carries it, over that task's own
range, under its own review.** A later measurement showing that a stopped
criterion would pass today is evidence about a counterfactual. **It does not
retroactively discharge the criterion, and a report that blurs the two is
wrong however favourable the measurement was.** **Where such evidence is
gathered, the range it is taken over is named explicitly**, because a range
chosen loosely measures a different criterion than the one that stopped.
*Incident: a counterfactual run over the correct range differed from one over
the branch tip by exactly one property, and naming the wrong range would have
measured a different criterion.*

**What is deferred.** **No mechanism enforces any of (a)–(d).** No partial
mechanism exists: `P1` through `P9` read repository state and none inspects
the relation between a prose statement and the method behind it. **Sub-cases
of (b) and (c) are mechanisable** — a lint could reject clone-local idioms
offered as evidence of absence, and could require a context flag beside any
hunk count — **and neither lint exists.** **This missing enforcement is not
currently registered under any item of the mechanism bucket**; `C4`
(cross-document factual consistency) is the nearest registered item and is a
different gap, being about statements disagreeing across documents rather
than about a statement exceeding its own evidence. **Registering it is
`C-c`'s.**

**Why the general obligation is not simply machinable.** The subject of a
prose measurement is defined in prose. A machine can read the statement; it
cannot read the method the author used, and (a) and (d) are about that
relation. **That is a reason to register the gap, not to call the rule
self-enforcing.**

## Role separation and outcome-based task specification

These rules extend, and do not replace, rules 1–7 above. They bind
prospectively only and alter no interpretation of previously approved
scientific results.

Origin: adopted 2026-08-03 after the Arm H procedural deviation and a
working session in which roughly seven of eleven executor stops were
caused by defects in the *procedural* content of task specifications —
none in their objectives, acceptance conditions, or prohibitions.
Rationale record: the PI amendment draft landed alongside this section.

### 8. Responsibility separation (root rule of this section)

The **specification author** defines objectives, invariants and
acceptance criteria.

The **executor** determines the implementation necessary to satisfy
them.

The **reviewer** verifies the sufficiency and internal consistency of
the specification before execution, and after execution independently
assesses whether the resulting evidence actually supports the claimed
outcome — including whether the acceptance criteria tested the
intended object rather than merely passing implemented assertions.
(Phase A's verifier rounds are the precedent: tests can pass while
testing the wrong thing. A reviewer restricted to "did the criteria
pass" would not catch that.)

Two distinct review functions may be exercised by two independent
reviewers: a **theory reviewer** (completeness, definitions, physics
and mathematics) and an **evidence verifier** (repository results,
computation, non-circularity of checkers, and whether claims exceed
what was shown). These are functions, not fixed assignments to a
particular agent.

These are FUNCTIONS, not fixed agents: specification/theory,
execution/experimentation, and independent review/verification. **PI
authorization sits above all three** — adoption, exceptions, and final
decisions are the PI's, and no rule in this section transfers that
authority.

**Refinement — caller roles.** Neither a specification nor a tool may assign
roles on the caller's behalf; it must fix the interface rather than presume the
caller's meaning. (Origin: the hard-coded worktree-correspondence target and
the proposed target-type enumeration.)

No role prescribes another role's INCIDENTAL implementation process. A method
MAY be prescribed where it is itself load-bearing to scientific
validity, independence, reproducibility, provenance, or governance —
for example: separation of blind compute from comparison; exact
rational rather than floating-point arithmetic; independent
reproduction; clean-clone validation; the prohibition on one program
generating both expected and actual values; mutation tests; sample
size, seed, and regulator prescriptions; merge parentage and the
no-force-push rule. **Every prescribed method MUST carry a stated
reason**, so that ordinary implementation cannot be re-labelled
"load-bearing" to smuggle procedural control back in.

Concretely: the specifier does not choose the executor's git strategy,
working directory, or command sequence; the executor does not alter
objectives, invariants, or scientific content; the reviewer does not
design the implementation.

**Review of specifications, not of executions.** Theory and
acceptance criteria are reviewed BEFORE the task; the resulting state
is reviewed AFTER it. Individual implementation steps are not
submitted for review.

**Amendment B, adopted 2026-08-09 — every task report carries a "Stops and clarifications" section.**

Every task report MUST contain a section recording each stop, with:
where it stopped (stage and acceptance criterion) and the exact
output — **reproduced in the report, or stored in a committed,
content-digested artifact that the report identifies by path,
revision and digest. The report MUST still reproduce the lines that
establish the stop.** This permits bulk raw output to live in an
auditable attachment; it does not permit a summary in place of
evidence; whether the stop was correct; the defect's category; and the
clarification or amendment that followed, naming the specific wording
or value it changed.

The category is one of exactly five:

- `SPECIFICATION_DEFECT` — the task specification's criterion, scope,
  literal, prohibition or workflow is wrong, contradictory,
  unsatisfiable, or broader than its purpose.
- `ENVIRONMENT` — execution identity, runtime, ACL, filesystem,
  package, or harness.
- `OBSERVATION_METHOD_ERROR` — repository state is correct, but the
  inspecting command, path, hashing method, worktree, or parsing was
  wrong.
- `REPOSITORY_DEFECT` — the repository's actual state violates a
  frozen requirement, or an artifact is itself wrong.
- `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the authoritative
  text or evidence cannot uniquely determine the outcome, and the
  executor has no authority to decide it.

**Each stop has exactly one PRIMARY category. Secondary findings
discovered through that stop MAY be recorded separately and classified
independently.**

*Why the classification is normative.* Across recent tasks the great
majority of stops were specification defects — prohibitions written
more broadly than their purpose, criteria unsatisfiable as written,
literals mangled in transcription. A record showing "stopped eleven
times" without categories invites the reader to infer executor
unreliability, when the executor's stops were correct in every case.
The distribution is itself the finding.

*Why five and not four.* A fourfold scheme has no place for the
`P2-PHASE-01` Phase-A/Phase-B dependency stop: the task specification
was not wrong, the repository was not broken — the repository simply had
not decided the question, and the executor was correctly forbidden from
deciding it. That is a distinct and common class, and collapsing it into
"specification defect" would misattribute the fault.

*Why `REPOSITORY_DEFECT` rather than "genuine repository problem".* The
looser name invites lumping together an unwelcome scientific result, an
artifact nobody has yet promised to create, and an actual violation of a
frozen requirement. Only the last is a defect.

*Incident.* The integration task stopped three times. All three were
primarily `OBSERVATION_METHOD_ERROR`; one of them surfaced a secondary
`REPOSITORY_DEFECT` — a wrong digest already written into `GATES.md` —
which was then corrected. **That is precisely the case the
primary/secondary split exists for**: forcing it into a single category
would either hide the registry error or misdescribe the stop.

**Amendment I, adopted 2026-08-09 — mid-task authority changes require reviewer-visible provenance.**

**A specification author who amends a task mid-execution MUST record
the amendment where the reviewers read.**

**Narrative explanation does not itself create execution authority or
governance status.** An account of why a change is reasonable is not
the change's authorization.

**The amendment MUST exist in a durable reviewer-visible record that
is part of the task's issued authority** — at minimum an amended or
re-issued specification, or another repository-defined amendment
record cited by it. **Not a chat message the reviewer happens to see**,
which is the thing this amendment exists to stop.

**`DECISION_LOG.md` is additionally required only where the amendment
itself creates or changes a programme-level decision or governance
state.** A path typo, a manifest count, a corrected command syntax or
a clarified acceptance criterion needs reviewer-visible authority
**without entering the decision log** — and requiring it would both
dilute that log and collide with any task whose scope does not
authorize modifying it.

**The record MUST identify what prior instruction is superseded, the
replacement instruction, and the scope of that replacement.** Without
those three, a reviewer can follow the reasoning and still not know
which line of authority changed.

### 9. Outcome-based task specification

A task specification MUST define **what must be true when the task is
complete**. It SHOULD avoid prescribing implementation details unless
those details are themselves governance objects — merge protocol
(rule 5) and blind-campaign procedure are governance objects, and
remain prescribed; git strategy, working directories, command
sequences and tool invocations are not.

A conforming specification has four MANDATORY NORMATIVE sections.
Other material — context, governing sources, dependency state,
authority and scope, definitions, outcome taxonomy, known limitations
— may be present; only these four carry execution authority:

**(a) Objective** — the required end state, stated as a condition of
the repository, not as a sequence of actions.

**(b) Acceptance criteria** — conditions, each independently
checkable, whose conjunction is sufficient for the objective. Every
criterion MUST have a machine-executable verification procedure and a
defined expected outcome; the specification MAY identify the verifier
interface and required outputs WITHOUT prescribing incidental command
syntax, environment paths, or working-directory details. A procedure
may be a checker script, a symbolic identity, a statistical decision
rule, a generated manifest, or a structured comparison — it need not
be a shell one-liner. A criterion requiring human judgement is not an
acceptance criterion and belongs in (c) or in review.

**(c) Invariants and prohibitions** — what may not change or be done
under any circumstance. This part is authored by the specifier and is
never inferred by the executor.

**(d) Report contract** — what the executor must return: the raw
output of every acceptance criterion, every self-correction with its
before/after hashes and its reason, and any condition it could not
satisfy.

**Refinement — protected prohibitions and conditional choices.** Every
prohibition MUST state what it protects, so its scope need not be inferred;
where a specification offers a choice, each acceptance criterion MUST be
conditional on that choice. (Origin: over-broad repair, formatter, and
scratch-tool prohibitions; and an equivalence-policy alternative whose
criterion allowed only one option.)

Within the bounds of (c), the executor MAY choose its own method,
explore alternatives, retry, and correct its own working artifacts.
**It MUST NOT infer, extend, or relax (c).**

**Amendment C, adopted 2026-08-09 — digest semantics and binary-safe computation.**

A recorded SHA-256 digest is the SHA-256 of **the exact committed
file-content bytes stored in the Git blob**. It is NOT the Git blob
object ID, unless the record explicitly says "Git blob object ID" —
the two are different quantities and are routinely confused.

**Acceptable methods:** reading `git cat-file blob <revision>:<path>`
through a binary-preserving subprocess API, or writing that byte
stream to a binary file and hashing the file.

**Prohibited:** any pipeline or shell construct that decodes the blob
as text, performs line-oriented processing, uses command substitution,
applies implicit encoding conversion, or otherwise fails to preserve
the byte stream exactly. **The defect is not the pipe** — a genuinely
binary subprocess pipe is fine; it is decoding, newline conversion and
substitution. **PowerShell text pipelines are not presumed
byte-preserving and MUST NOT be used for committed-content digests.**

**The record MUST state the revision and path whose committed content
was hashed** — `sha256(content of <rev>:<path>)`, not a bare filename
and digest.

A working-tree digest MAY be used for scratch diagnosis, but it MUST
be labelled as such and **cannot satisfy an acceptance criterion that
requires a committed-content digest**.

*Incident.* Two draft digests recorded in `GATES.md` were wrong. The
cause was hashing through a PowerShell pipeline that altered the byte
stream. The error was found by an acceptance criterion designed for a
different purpose (detecting whether a registry commit had touched a
draft), and the first diagnosis — a line-ending artefact — was itself
wrong; `core.autocrlf` was already `false`. Two round trips were spent
before the actual cause was identified.

**Amendment G, adopted 2026-08-09 — structural changes propagate.**

**When a specification gains, splits, or re-layers a structure — a
stage, a layer, a conditional branch, a state, a commit-order
constraint — every acceptance criterion, invariant, report-contract
item and objective statement MUST be re-read against the new
structure before issue.**

For each, ask two questions: **how does this clause read under the new
structure**, and **does it now require a quantity the new structure
permits to be undefined?**

**Propagation is TRANSITIVE.** Revising one structural element
requires checking every clause whose meaning or satisfiability depends
on it, **not only clauses that name it directly**. A new stage changes
the sequence, which changes commit ordering, which changes evidence
layering, which changes scope timing, which changes the report
contract, which changes what is post-report evidence.

**Residual clauses from the old structure do not lapse. They become
contradictions**, and a correct executor will stop.

**Layer boundaries must be drawn by what each layer actually requires,
not by where a statement intuitively belongs.** A statement placed in
a layer that does not supply its premises invalidates the layering.

**Amendment L, adopted 2026-08-09 — consumed conventions must be discoverable through the conventions index.**

**A convention or decision that a computation CONSUMES MUST be
discoverable from the governing conventions index, not only from a
chronological decision log.**

**The index may point to the authoritative ruling rather than
duplicate it.** This requirement governs discoverability and
provenance; **it does not prescribe the machine-readable storage
format**, which remains an open design question.

**Index discoverability does not by itself make prose a stable machine
interface.** A computation that parses a convention must consume a
representation **whose machine-facing identifier or lookup contract is
explicitly governed.** The storage format and the synchronisation
mechanism remain separate design questions.

**The incident below has two layers. This amendment closes the
governance obligation for BOTH, while leaving the machine-readable
implementation of the second open**: a human should find the ruling
from the conventions index; **and a script should not depend on
mutable prose headings as a semantic API.** **Adding an index pointer
does not by itself discharge the second obligation** — the lookup
contract must still be governed, and how it is represented is the
deferred design question.

### 10. Self-correction authority and its limit

Self-correction is permitted ONLY for artifacts the specification
explicitly classifies as **executor-editable**. Supplied-frozen,
reviewer-approved, canonical-candidate, and content-authoritative
artifacts remain immutable even when not yet registered, unless the
objective explicitly authorizes substantive editing.

For an executor-editable artifact, the executor MAY correct it without
returning for authorization where all of the following hold: it is not
registered and not hash-pinned by any registry entry; the correction
is required to satisfy a stated acceptance criterion; the correction
does not change reviewed scientific meaning, the objective, or any
claim; the executor reports before/after hashes, the exact diff, and
the reason; and result-equivalence is demonstrated by machine means.
**If equivalence cannot be demonstrated mechanically, return for
review.** Result-equivalence is required only where the correction is
represented as non-semantic or output-preserving; substantively
authorized development is judged against the acceptance criteria
instead.

An executor MUST NOT correct, reformat, or re-pin: any artifact
hash-pinned by a registered gate; any gate status, verdict, or digest;
any file outside the declared scope; or any repository configuration.

**Refinement — authorization record.** A mid-task authorization that changes
what an executor may do MUST be recorded in the repository before a report
relies on it. (Origin: the 2026-08-03 and 2026-08-04 environment
authorizations initially existed only in conversation.)

**Tests:** tests may be created or updated within the current task
ONLY where the specification expressly includes them in the authorized
scope and acceptance criteria. Any test change not so authorized
requires a separate specification and review. **An unexpected test
failure never authorizes the executor to modify the test merely to
obtain a green result.** (The Arm H lesson stated exactly:
pre-authorized — permitted; not pre-authorized — stop; for a green
suite — never.)

The executor MAY revise its own intermediate working artifacts as many
times as required — generate, lint, fix, re-lint is ordinary
engineering and does not warrant a round trip — provided the final
state satisfies the acceptance criteria and the report records what
changed.

A re-pin under this rule does not create a precedent for registered
artifacts.

### 11. Task granularity and integration boundary

A task SHOULD combine implementation, local verification and branch
preparation into ONE authorization. Implementation steps within it are
not individually reviewed.

**Integration is a separate authorization.** Merging into `main`
requires a separate authorization, issued only AFTER clean-clone
review of the resulting branch.

**The default classification is MATERIAL.** A task may bypass separate
result review and integration authorization only where its REVIEWED
specification explicitly marks it `SINGLE-AUTHORIZATION-ELIGIBLE` and
states why the change is low-risk. **The executor must not infer that
classification, and may not upgrade a task into it.**

Material work always includes: theory or concept specifications; gate
registrations; decisive scientific runs; governance conventions;
canonical or hash-pinned artifacts; and anything affecting a
downstream gate. Non-exhaustive examples of what MAY be marked
eligible: typo-only documentation corrections; a generated index
refresh with no semantic change; formatting-only changes to unpinned
files; removal of clearly identified scratch artifacts; mechanical
metadata updates. Matching an example is not sufficient — the marking
must be explicit in the reviewed specification.

**Two review points and one integration boundary — and no others:**
1. *Specification review* — before execution: the objective,
   invariants, acceptance criteria, and the theory behind them.
2. *Result review* — after execution, before integration: the
   resulting branch, from a clean clone.
3. *Integration* — under rule 5's merge discipline, which does not
   require a freshly hand-written procedural specification each time
   (see rule 5's standardized authorization).

Nothing between those boundaries is submitted for review. No
additional approval boundary is required unless the specification
itself preregisters a scientific, safety, cost, or governance
checkpoint.

### 12. Acceptance criteria must be mechanically checkable

Each acceptance criterion MUST have a machine-executable verification
procedure with a defined expected outcome. The specification must
identify the verifier interface, required inputs, and expected result,
but need not prescribe incidental command syntax, environment paths,
working directories, or tool invocation details.

Where a criterion concerns the changed-file set, the declared manifest
and the checker invocation are normative; the executor may choose how
to prepare the inputs.

The specifier MUST derive every literal in an acceptance criterion —
hashes, file paths, grep patterns, rule sets, test names — from the
repository as it actually is at specification time, not from
recollection. Each specification MUST record a single line,
`Specification evidence base: <full commit SHA>`; every
repository-derived literal in it must be reproducible at that commit.
Per-literal citation is not required.

**Refinement — satisfiability and literals.** Before issue, the specifier MUST
evaluate each acceptance criterion against the evidence-base repository and
confirm that a conforming implementation can satisfy it. Repository-derived
literals — hashes, paths, SHAs, and grep patterns — MUST be machine-checked
there for presence, completeness, and unbroken form. (Origin: the pure-append
prefix criterion, an inexpressible heading-count check, and reflowed or
nonmatching literals.)

Recording the evidence base does NOT by itself freeze the execution
base. Where base identity is load-bearing, it must ALSO appear
explicitly as an invariant in part (c). Rule 7 (evidence precedence) applies to the authoring of
specifications as much as to the reporting of results.

**Amendment F, adopted 2026-08-09 — mutation tests must prove reach.**

**A mutation test MUST establish three things, separately:**

    1  the mutation was injected
    2  the dependency point was REACHED
    3  the expected downstream consequence was observed — either the
       dependent quantity changed in the expected causal direction, or
       the mutation caused the specifically expected failure AT OR
       AFTER the dependency point

**The expected consequence MUST be one that could not occur under the
un-mutated input.** Reach plus a consequence is not enough if the
consequence was available anyway: **a mutation flipping a sign in a
channel whose coefficient is zero proves reach and nothing else.**

**"The output changed" is too narrow.** Mutating a required convention
may correctly produce a STOP at the parsing or validation point rather
than a different final value; that establishes the dependency just as
well. **What must be excluded is an unrelated earlier STOP being
counted as coverage.**

**Demonstrating that the program stopped is not sufficient.** A
program can stop before the mutation is consumed, for an unrelated
reason, and a test that only asserts a stop will pass while covering
nothing.

**Stop behaviour is tested separately** from mutation reach.


**Amendment O, adopted 2026-08-14 — a specification's declarations are machine-readable, and its reading list names where evidence is written.**

**Mechanism marker: RULE + MECHANISM DEFERRED.**

Rule 12 binds the specifier to make each acceptance criterion mechanically
checkable and to derive its literals from the repository. **This amendment
adds two obligations that make a task answerable at all.**

**(a) A SCOPE BLOCK CARRIES A `stated:` KEY** declaring the total the
manifest is asserted to contain, per category — additions and modifications —
**as a machine-readable record and not as a sentence elsewhere in the
document.** The declared total is what a checker compares the manifest
against. **A count inferred from prose is not a declaration**: it depends on
which sentence a parser reaches first, and a grammar that walks backwards
through a document for the nearest number is reading the author's layout
rather than the author's intent.

**(b) A READING LIST NAMES THE SITES WHERE EVIDENCE FIELDS ARE WRITTEN, not
only the functions that compute them.** A specification that directs an
executor to the routine producing a quantity, but not to the place the
quantity is recorded, has under-described its own question. *Incident: a
task's answer lay at three lines outside its specification's reading list,
and its executor found them anyway — which is not a property the next
specification may rely on.*

**A reading list is a claim about sufficiency**, and Amendment M applies to
it: it may not assert a scope its author did not check.

**What is deferred, and (a) and (b) differ.**

**For (a) there IS a partial mechanism and it is not the obligation.** `P1`
reads the `stated:` record, and returns `NOT_PARSEABLE` for a scope block
that lacks one — **so it does more than parse; it refuses.** **But the
refusal is opt-in.** It occurs only when a task's own specification asks for
the checker to be run against it, names its own path, and the executor runs
it. **Nothing requires a newly issued specification to carry the key**, and
compliance is currently maintained by an authoring habit rather than by a
repository mechanism. **The partial mechanism is `P1`; the missing
enforcement is registered as `C2`.**

**For (b) there is no mechanism at all**, partial or otherwise, and none is
currently registered. **Registering it is `C-c`'s.**

### 13. Execution environment

The repository declares its execution environment in an execution-environment
document. The execution environment SHALL satisfy that document.

**Standing authorization.** An executor MAY restore the declared execution
environment without returning for authorization, and reports what it did in one
line.

**"Restore" means bringing the environment into conformity with the declared
document. It does NOT authorize changing the declaration itself.**

**Still requiring PI authorization:** changing what the document declares;
installing anything it does not declare; modifying `pyproject.toml`, lint rules,
validator configuration, or file permissions; and anything that alters whether
a check passes or what a computation yields.

**Environment failures SHALL be diagnosed in this order:** (1) execution
identity; (2) interpreter availability; (3) permissions; (4) filesystem and
workspace; (5) package availability.

**Execution-environment repair SHALL NEVER be used as justification to modify
repository content.** Restoring an environment never licenses editing a test,
`pyproject.toml`, lint configuration, a script, a gate, or any other repository
file. If a repository change appears necessary to make the environment work,
that is a separate specification requiring its own authorization.

**Repository content SHALL NEVER be modified solely because a different
execution environment would make the modification unnecessary.** The two
clauses bind in both directions: an environment problem is fixed in the
environment, and a repository problem is not fixed by changing what the
environment happens to be.

**The repository and the execution environment are distinct layers.**
`pyproject.toml`, tests, lint configuration and scripts are repository;
interpreter, virtual environment, packages and permissions are environment. A
failure in one is not evidence of a defect in the other.

**Amendment D, adopted 2026-08-09 — execution location, and the process/harness layer.**

Rule 13's diagnostic order is extended by a step before identity:

(0) **execution location** — repository path, worktree identity,
    current branch or detached state, and the **resolved HEAD commit
    SHA**. A directory alone is not a location: the same worktree can
    sit at different revisions.
(1) execution identity; (2) interpreter availability;
(3) permissions; (4) filesystem and workspace; (5) package
    availability; (6) **process and harness lifecycle** — timeouts,
    stdout/stderr pipe closure, plugin teardown, child-process
    survival, signal or job-object termination.

**Where a command evaluates a revision without checking it out, the
report MUST distinguish the executing worktree's revision from the
object revision being inspected.** Both are legitimate; conflating
them is how "X is absent" gets asserted about the wrong revision.

A conclusion of the form "X is absent" is not established until the
location it was observed from has been established.

*Why layer 6 exists.* Five validator files each reaching `[100%]` and
each terminating at the same 120.2 s boundary is a process-lifecycle
condition, not a package-availability one. Without its own layer, the
most significant recent environment finding had nowhere in the
diagnostic order to belong.

*Incident.* The integration task stopped because the governance tools
appeared to be missing. They were present at both pinned revisions. The
observation had been made in the main worktree, which sits on its own
branch and had never checked out the revision under test. The
observation was accurate about that worktree and false about the
revision, and nothing in the diagnostic order caught the difference.

### 14. Validator outcome contract

Unless a task specification states a stricter or explicitly different
requirement, a validator PASSES only when all of the following hold:
the intended validator process started successfully; it completed
without timeout or external termination; it returned **exit status
0**; and no required test, collection phase, or teardown phase was
skipped or aborted.

**Output showing `[100%]`, or the absence of an assertion failure,
does NOT override a non-zero exit status.**

A task specification may then simply say "validators must pass under
Rule 14", rather than restating the exit contract each time. Where a
task genuinely needs different semantics — an expected `exit 5`, a
deselection, a known `xfail` — the specification states it explicitly.

**Disposition vocabulary.** Three distinct dispositions:

- **satisfied** — the criterion genuinely passed as written;
- **not satisfied, PI-authorized exception** — the criterion was
  evaluated, was not met, and the PI accepts the task nonetheless;
- **waived** — the PI removed the obligation BEFORE its evaluation
  deadline, so it was never evaluated.

**A criterion already evaluated and found unsatisfied cannot later be
reported as waived.** Its disposition is a retrospective exception, or
task rejection. Waiving after the fact would erase an evaluation that
actually happened.

Every waiver and every exception records: the authorizing authority;
the time or sequence point; the criterion affected; the specific
evidence accepted; and whether it applies only to this task.
Record an accepted timeout as:

    A9: NOT SATISFIED
    Disposition: PI-AUTHORIZED EXCEPTION
    Evidence: all selected tests reached completion output with no
              assertion failure; process exit 124 after 120.2 s.

**An exception changes the disposition of the TASK, not the historical
evaluation of the CRITERION.** A criterion that was not satisfied is
never written back as passed.

*Incident.* Five validator files each reached `[100%]` with no
assertion failure and each terminated at ~120.2 s with exit 124.
Because all five stopped at the same boundary regardless of their
individual cost, the cost lies in process shutdown rather than in the
tests. The executor reported this as a qualified condition rather than
as a pass, which was correct, but the acceptance criterion had no
vocabulary for the outcome.

**Amendment E, adopted 2026-08-09 — a failed observation is not a negative result.**

**A failure to observe MUST NOT be recorded, mapped, or acted upon as
an observed negative result.**

Where a check can fail to produce an observation, its outcome model
MUST distinguish — **whether by explicit states or by equivalent
evidence** — at least: **observed positive**, **observed negative**,
and **not observed**.

**This does not require every tool to expose a three-valued enum.**
The requirement is that the distinction be recoverable, not that it be
encoded in a particular form. A tool exit status, acceptance criterion, or
state machine that maps "could not determine" onto the same value as
"determined to be false" is a defect.

**The two require opposite responses:** a failed observation calls for
repairing the measurement; an observed negative calls for stopping and
investigating.

### 15. Governing artifacts are committed

**A specification, a pre-execution review, a task report, and any
manifest supplied to a checker are governing artifacts and are
committed to the repository.** An artifact that determines what a task
was authorised to do, or that records what it did, is not evidence
while it exists only in a conversation.

**Placement.** Specifications under `specs/`; task reports under
`reports/`; pre-execution reviews under `reviews/<function>/`, using
the existing directory for the reviewing party. Supplied manifests are
reproduced in the report that used them.

**Timing.** A specification is committed as the task's first commit.
**A pre-execution review is committed before the work it authorises
proceeds.** A report is committed by the task that produced it.

**Prospective only.** Records created before this rule are not
retrospectively non-conforming, and are not to be back-filled.

### 16. Accumulated reading

**A task that adds a MATERIAL artifact bearing on a question already
addressed by other authoritative or reviewable artifacts MUST state
what the assembled set does NOT establish.**

**"Material artifact, same question" is the trigger**, not "any
artifact in any chain" — otherwise every report gains a boilerplate
paragraph.

**An integration task that brings previously separate artifacts into
one authoritative branch MUST perform that assessment again against
the MERGED state.**

Individual artifacts may each be scrupulous while their accumulation
reads as a stronger conclusion than any of them states. **The
responsibility is two-layered**: the producing task assesses the local
accumulated reading; **the integration task assesses the authoritative
one**, because the strongest misleading inference sometimes becomes
available only once separate branches sit on one `main`.

**This does not require repeating every earlier limitation.** **At
each required assessment, the responsible task must identify only the
limitations whose omission would materially change the natural reading
of the assembled evidence** — not reproduce every earlier caveat.

**The assessment MUST name the junction or report a search.** Either
name the artifact pair and the specific inference their combination
makes available, **or state that a search was performed, describe it,
and report that none was found.** Without this, "the accumulation was
assessed" is unfalsifiable and every report gains a paragraph saying
so. **The one finding this rule has actually produced came from
hunting a junction — three artifacts, one named inference — not from a
general assurance.**

**"The responsible task", not "the latest artifact"**: an integration
may produce only its own report, yet it is the task that owes the
assembled-state assessment.

### 17. Integrations do not add epistemic or governance classifications

**An integration, derivation, or any task that carries reviewed
results forward MUST NOT add a governance or epistemic classification
the reviewed results did not carry.**

Recording what a result did not establish is required. **Assigning it
to an open item, a gate, a status, or a category it was never assigned
to is not.**

### 18. Review supply protocol

**A pre-execution review is supplied to the executor AS A FILE, not as
text pasted into a prompt.** The executor commits that file's bytes
unchanged.

**No extraction, no delimiters, no normalisation.** There is no boundary
to locate, so **no boundary can be inferred**; there are no transport
artifacts to strip, so **no stripping rule is needed.**

**The specification SHOULD also be supplied as a file.** It is committed
at a frozen path by the task's first commit, so **a pasted specification
makes commit 1's bytes the executor's transcription with no supplied file
to digest against** — verifiable in the way commit 2 now is only if it
too arrives as a file.

**A pasted specification is permitted and is not a STOP**, because it is
instruction rather than an artifact whose exact bytes carry authority.
**But the executor reports which way it arrived**, and where it was
pasted, says so.

**The executor verifies correspondence before committing**: the supplied
review must identify the specification it reviews, by digest or by task
name. **If it does not, or if no file is supplied, or if the file
corresponds to a different specification, STOP and say which.**

**The executor never authors, edits, summarises or reformats a review**,
and never reconstructs one from a conversation.

**Placeholders inside a review's text stay as written.** Placeholders are
resolved in the artifact's PATH only.

**Amendment N, adopted 2026-08-14 — the specification is supplied as a file, and the review binds to it by digest.**

**Mechanism marker: RULE + MECHANISM DEFERRED.**

Rule 18 governs how a review reaches the executor and what the executor
verifies on receipt. **This amendment adds a producer-side obligation and
tightens what the review must record. It does not alter Rule 18's
executor-side handling of a pasted specification**, which remains permitted
and remains not a stop.

**(a) A SPECIFICATION IS SUPPLIED TO THE REVIEWER AND THE EXECUTOR AS A
FILE.** Rule 18 states this as a SHOULD and states the consequence: a pasted
specification makes commit 1's bytes the executor's transcription, with no
supplied file to digest against. **This amendment makes it an obligation ON
THE PARTY ISSUING THE SPECIFICATION.** **The two are not in tension:** the
producer must supply a file; the executor still does not stop when the
producer fails to, and still reports which way it arrived. *Incident: the
specification was pasted rather than supplied on at least four occasions, and
one review declined to record a digest because of it.*

**(b) A REVIEW ARTIFACT RECORDS `reviewed specification SHA-256:`**, filled
in, naming the digest of the specification it reviewed. **Where it reviews a
further artifact, it also records `reviewed artifact SHA-256:`.** **Both are
required where both apply**: recording only the artifact's leaves the
substitution case open, in which a review of one specification is presented
beside a different one. *Incident: a review of a stale specification version
occurred twice in one session and was undetectable from the text.*

**A review that names a task by title and not by digest binds to nothing a
later reader can check.** Rule 18 permits identification "by digest or by
task name"; **this amendment requires the digest where a specification file
exists to digest.**

**What is deferred, and (a) and (b) differ sharply.**

**(a) is not checkable inside the repository.** The supplied file is outside
it, and whether a specification arrived as a file or as pasted text leaves no
trace in the committed bytes. **The executor's report is the only record, and
that is a disclosure obligation rather than a mechanism.**

**(b) IS fully checkable inside the repository, and no check does it.** The
review blob and the specification blob are both committed by the same task;
extracting the cited digest and comparing it to the specification's measured
digest requires nothing the checker does not already have. **No property does
this — `P1` through `P9` treat `reviews/` only as a path prefix, for ordering
and placement.** **This missing enforcement is not currently registered as a
mechanism item.** **Registering it is `C-c`'s.**

### 19. Pinned-artifact integrity

**Mechanism marker: RULE + MECHANISM EXISTS.**

**A task that modifies a file pinned by digest in a registered gate RE-PINS
IT IN THE SAME TASK.** The re-pin is part of the modification, not a
follow-up: a gate whose pin names a digest its artifact no longer has is a
gate asserting something false, and it asserts it from the moment the
artifact changes until someone notices.

**A task that modifies no pinned file owes no re-pin, and establishes that by
measurement rather than by assumption.** The check is cheap — locate every
pin, resolve the artifact each names, compare against the changed-file set —
and the assumption is exactly the kind Rule 7 forbids.

*Incident: three consecutive tasks required a re-pin written in by hand, and
nothing detected the omission. The rule was ratified once by PI ruling for a
single instance; this is its durable form.*

**The mechanism, named and verified.** `tests/test_gate_pins.py`, landed at
`e3ce8063`, resolves every `` (sha256 `<64 hex>`) `` occurrence in `GATES.md`
to the artifact path named above it, hashes that file's bytes and fails on
any mismatch. It also fails on a pin whose path cannot be resolved, and on a
`GATES.md` carrying no pin at all.

**What the mechanism does and does not enforce.** It enforces the
obligation's effect: a task that modified a pinned artifact without re-pinning
cannot report a green suite, because the pin is stale at its head. **It does
not enforce the words "in the same task"** — it has no notion of tasks — and
**it runs when the suite runs**, not at commit time. **A branch that never
runs its validators is not protected by it.**

### 20. Permitted pre-push hygiene repair

**Mechanism marker: RULE + MECHANISM DEFERRED.**

**An unpushed commit MAY be amended solely to remove a MECHANICALLY DETECTED
commit-message hygiene violation, before any branch publication, provided
both the rejected and the replacement commit ids are recorded in the task
report.**

**Four conditions, and each is load-bearing:**

1. **MECHANICALLY DETECTED.** The violation was reported by a check with a
   non-zero exit, and **the executor exercised no judgement about whether a
   violation existed.** A permission to amend on an executor's own opinion of
   a message would be a different and much wider rule.
2. **UNPUSHED, and before any publication.** No other party can have seen the
   rejected commit.
3. **HYGIENE ONLY.** The commit's tree is unchanged by the amendment; only
   the message differs.
4. **BOTH COMMIT IDS RECORDED** in the report, so the amendment is visible
   rather than silent.

**This authorises nothing about pushed or reviewed history**, and it is not a
general licence to rewrite.

**The open question, decided here.** The ratification of the single instance
left open whether the repair requires EVERY AFFECTED CHECK re-run or only the
failing one. **It requires every affected check.**

**The reason is the same one Amendment M(b) gives.** An amend changes the
commit object and therefore its identifier, and every property computed over
a range ending at or containing that commit was measured against an
identifier that no longer exists. **Re-running only the check that failed
would leave the other results true of a superseded state** — the defect class
Amendment M exists to prevent — **and the cost of re-running all of them is
seconds.**

**The ratified instance did not settle this.** Its executor re-ran all
affected checks voluntarily, and a voluntary act is not a precedent.
**Recording it as though it were would be the substitution Amendment N(b)
guards against, in a different currency.**

**What is deferred.** **The trigger is mechanised and the obligations are
not.** `P6` detects the commit-hygiene violation that opens this permission —
that is the partial mechanism, and it is why condition 1 is checkable at all.
**Nothing verifies that both commit ids were recorded, that the tree was
unchanged across the amendment, or that the affected checks were re-run.**
**None of that is currently registered as a mechanism item.** **Registering
it is `C-c`'s.**

### 21. Artifact-state and statement-kind namespaces

**Mechanism marker: RULE-ONLY.**

**PI RULING, adopted verbatim:**

> **Artifact-state labels and statement-kind labels are distinct
> vocabularies; an artifact-state label does not need to appear in the
> statement-kind vocabulary.**

`ADOPTED`, `PROPOSED`, `SUPERSEDED` and `DRAFT` describe **the state of an
artifact**. `MEASURED`, `DERIVED`, `RECOMMENDATION` and `CAUTION` describe
**the kind of a statement**. **Two namespaces. An entry in one is not a gap
in the other**, and a label census over one vocabulary does not report a
defect merely because a label from the other is absent from it.

**A document that defines its kind labels is not obliged to define its state
labels in the same list**, and a reviewer finding a state label outside the
kind vocabulary has found a category difference rather than an undefined
term.

*Provenance, because it bears on how the rule was reached.* An executor met
the question, **reported it rather than deciding it**, and recorded that
calling `ADOPTED` "not a kind label" would be a judgement. The Reviewer
proposed the namespace distinction and its wording; **the PI issued the
ruling.** **A reviewer proposing a ruling and the PI issuing it are different
acts**, and this item was open precisely because the executor declined to
decide it.

**Why RULE-ONLY.** The rule resolves a category error between two
vocabularies. **It imposes no obligation on any artifact that a machine could
test**: it does not require a label to be present, absent, or of any form. It
tells a reader — and a reviewer — that a question does not arise. **There is
nothing here to check, which is different from there being something to check
that nobody has built.**

## Consolidation record — `C-a`

**This section is a record, not a principle.** It exists so that the coverage
claimed by the four amendments and three rules adopted on 2026-08-14 can be
COUNTED rather than reconstructed from memory. **Nothing here binds; the
rules and amendments it points to are what bind.**

**Source: the governance debt classification, digest
`1c65e68c0263b1fcfab24d260d81409a4cd687139c4f106e0a8112fb346d61d9`**, §A and
§B — twelve observed failures — plus `E2`, ruled by the PI.

**Thirteen source items, thirteen rows, each item exactly once.**

| Item | What it requires | Now covered by |
|---|---|---|
| `A1` | a scope block carries a `stated:` key | Amendment O(a) to Rule 12 |
| `A2` | a specification is supplied as a file | Amendment N(a) to Rule 18 |
| `A3` | a review records the digests it reviewed | Amendment N(b) to Rule 18 |
| `A4` | a measurement is taken over the whole subject | Amendment M(a) to Rule 7 |
| `A5` | a verification statement is clone-invariant | Amendment M(b) to Rule 7 |
| `A6` | a hunk count names its diff context | Amendment M(c) to Rule 7 |
| `A7` | a reading list names evidence-write sites | Amendment O(b) to Rule 12 |
| `A8` | evidence about a criterion is not its discharge | Amendment M(d) to Rule 7 |
| `B1` | an integration states its landing outcome inline | Amendment P(a) to Rule 5 |
| `B2` | a task modifying a pinned file re-pins it | Rule 19 |
| `B3` | an auto-merge is verified by line survival | Amendment P(b) to Rule 5 |
| `B4` | a permitted pre-push hygiene amend | Rule 20 |
| `E2` | artifact-state and statement-kind namespaces | Rule 21 |

**Mechanism markers, counted.**

    RULE + MECHANISM EXISTS      1     Rule 19
    RULE + MECHANISM DEFERRED    5     Amendments M, N, O, P and Rule 20
    RULE-ONLY                    1     Rule 21
    -----------------------------------
    principles adopted           7     covering 13 source items

**FIVE OF THE SEVEN ARE DEFERRED, AND THAT NUMBER IS THE POINT OF THIS
RECORD.** **A rule marked `MECHANISM DEFERRED` prevents nothing by itself.**
It records what should happen and relies on an author remembering to do it.
**The debt these rules were written from is not paid by their adoption**;
`C-b` and `C-c` are the rest of it, and the deferred count is the size of
what they still owe.

**Two of the deferred obligations are fully specifiable inside the repository
and are registered nowhere**: the review-digest comparison of Amendment N(b),
and the line-survival check of Amendment P(b). **Amendment O(a)'s missing
enforcement is registered as `C2`.** The remainder are named in their own
amendments.

**What this rule set does NOT cover.** **It covers the observed failures and
is silent about the unobserved ones.** The classification it comes from is a
list of what was noticed across one working session, and several of its items
were found only because a later task tripped over them. **A list assembled by
noticing is not a survey**, and the absence of a rule here is not evidence
that the corresponding failure cannot occur.

**Governance debt is registered in `docs/GOVERNANCE-DEBT.md`** — an eleven-entry record of the known governance debt, each entry with its disposition and where its evidence sits. Nothing in that file binds either.
