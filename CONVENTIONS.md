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
