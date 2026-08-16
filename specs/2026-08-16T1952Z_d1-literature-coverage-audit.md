# Task specification — `D-1`: literature coverage audit for reflection positivity

Specification evidence base: `b27926aa…` — **authoritative `main` at
issue; the executor measures it and STOPS on mismatch.**

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/d1-literature-coverage-audit-3
    Cut from           authoritative main — refs/remotes/origin/main

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This task does not touch `main`.** Integration is a separate task.

**IT DESIGNS NO PROOF AND SELECTS NO CANDIDATE.** It determines what the
literature already establishes and, precisely, what it does not.

---

> ## READ §1 FIRST. THIS TASK MAY BE UNEXECUTABLE IN YOUR ENVIRONMENT.
>
> **It requires fetching published work.** **The Researcher does not know
> whether your environment can reach the hosts involved**, and **an audit
> conducted from memory would be worse than no audit** — it is exactly
> the failure this task exists to correct.
>
> **§1 is a precondition, not a criterion.** **Run it immediately after
> `A1`'s repository identity and `A2`'s review binding, and before any
> literature or repository scientific content is read.**
>
> **An earlier version of this block said "test it before anything
> else", which contradicted `A1`.**

## 0. The question is per candidate, and the usual phrasing is wrong

**There is no "the declared action".** Measured on `main`:
`P2-CHANNEL-FREEZE-01_phaseA_freeze.md` §2 freezes the **interaction** —
the `U(N)` chiral NJL generator-sum form — and
`P2-LATTICE-ONTOLOGY-01` line 189 leaves the **canonical kinetic
operator** `DELEGATED`.

**So there are four candidate actions, not one.** **Every coverage
question is asked as:**

> does this theorem cover *the frozen `U(N)` chiral NJL interaction
> together with candidate `X`'s kinetic term*?

**Not** *does it cover the declared action*. **A coverage verdict stated
against "the declared action" answers a question that does not yet
exist**, and would be unusable when the operator is eventually frozen.

## 1. Precondition — network reachability, tested and reported

**After `A1`'s repository-identity check and `A2`'s review-binding check
have passed, and before reading any literature or repository scientific
content, test whether you can fetch published work.**

**An earlier version of this sentence read "before reading anything
else", contradicting `A1`, the `ORDER` paragraph below, and the block at
the head of this specification.** **Two executions have already stopped
on control-flow and repository-identity ambiguity; a fourth normative
ordering statement disagreeing with the other three is exactly the shape
that produced them.** Attempt, and report the outcome of each:

    arxiv.org                     a listing or abstract page
    doi.org                       a DOI resolution
    any publisher host you would
      need for a non-arXiv work

**Report exactly what you reached and what you did not**, with the error
or status for each.

**ORDER. This precondition runs AFTER `A1`'s repository identity and
`A2`'s review binding, and BEFORE any literature or repository
scientific content is read.** **Testing literature access inside the
wrong repository establishes nothing, and no branch should exist until
`A1` and `A2` have passed.**

**GLOBAL PRECONDITION. If you can reach NO scholarly source at all,
STOP.** **Report the failure, the hosts attempted, and the errors.**
**Do not proceed from memory**, **do not substitute recollection for a
fetch**, and **do not produce a partial audit built on recalled
content.**

**PER-WORK PRECONDITION, and it is separate.** **Reaching arXiv is not
reaching everything.** For each work, report **what depth you obtained**:
listing, abstract, or full text.

**Abstract-only access is sufficient to IDENTIFY a work. It is NOT
sufficient for a `COVERED` verdict** — **unless the abstract itself
states every hypothesis the mapping needs**, which is rare and must be
demonstrated rather than assumed.

**Where a load-bearing work is available only as an abstract or a
listing, it cannot support `COVERED`.** **If a candidate has no other
fetched theorem, its verdict is `NO COVERAGE FOUND` or `NOT
DETERMINABLE` as the case requires** — **and say which and why.**

**This bites hardest on the 1970s and 1980s works.** **An abstract of a
1978 or 1987 paper will not usually state the reflection type, the
boundary conditions, or the parameter restrictions**, and those are
exactly the hypotheses the mapping turns on.

**A STOP here is a successful outcome of this task**, not a failure: it
establishes that the audit requires someone with library or network
access, which is itself the finding the programme needs. **Report it as
such.**

## 2. The three claims and the gap, read from `main`

**`derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md` records THREE
STRUCTURED LITERATURE CLAIMS AND ONE STAGGERED LITERATURE GAP**, all
marked `UNVERIFIED FROM THIS REPOSITORY`, none carrying an identifier.

**Not "four claims".** **`L3` names no work and `B0` expressly declined
to count it as a claim**, so describing the source as recording four
would misdescribe the artifact this audit exists to correct. **Read them from the file, not from this
specification.** For reference only, they concern:

    L1  Osterwalder and Schrader, reconstruction axioms, 1973 and 1975
    L2  Osterwalder and Seiler, lattice gauge theories, 1978
    L3  staggered reflection positivity — AUTHOR/WORK NOT RECALLED
    L4  Neuberger on the overlap operator; Hernández, Jansen and Lüscher
        on its locality

**`L3` names no work.** **The source task expressly did not count it as a
claim**, on the ground that *a standard construction exists* is the
absence of one. **Treat it as a gap to be filled or left open, not as a
claim to be checked.**

## 3. Citation discipline

**Every work used to support an applicability or coverage conclusion
must carry a resolvable identifier and be FETCHED to the evidential depth
that conclusion requires.**

**Any work identified but not fetched may be recorded ONLY as
`NOT FETCHED` or `RECALLED`, and cannot support `COVERED`.**

**An earlier version said every work discussed is fetched**, which the
same section's own `NOT FETCHED` and `RECALLED` fields, and §6's
encountered-but-not-pursued list, make literally impossible. **The rule
is about what may SUPPORT a conclusion, not about what may be
mentioned.**

**Per work, report:**

    IDENTIFIER    arXiv ID or DOI
    FETCHED       yes, with what you retrieved — abstract, full text,
                  or listing only
    NOT FETCHED   with the reason
    RECALLED      marked as such wherever fetching failed

**A statement about a work you did not fetch is `RECALLED`, and must be
labelled `RECALLED` every time it appears.** **Do not let a recalled
statement acquire the appearance of a verified one by being repeated
beside fetched ones.**

**Report the count of works fetched and the count recalled.**

## 4. What "covers" means, and it is not a judgement

**A theorem can contribute to a `COVERED` verdict for a RELEVANT
candidate only if every common axis and every theorem-specific hypothesis
is explicitly MAPPED to that candidate action.**

**A mismatch in a genuinely relevant theorem–candidate pair makes that
basis `PARTIAL`, and the report must name the precise hypothesis that
fails.** **A theorem outside the candidate's formulation class is `NOT AN
APPLICABILITY CANDIDATE`, not `PARTIAL`.**

**An earlier version of this opening said a theorem covers if it is
"compatible" on the seven axes, and that any incompatibility makes it
`PARTIAL`.** **Both were superseded later in this same section** — by the
`MAPPED` standard and by the applicability-candidate declaration — **and
an opening that contradicts its own section is worse than either
version.**

    1  free versus interacting     the frozen interaction is a
                                   four-fermion term, not free
    2  reflection type             link-reflection or site-reflection
    3  lattice extent              finite or infinite
    4  boundary conditions         which are assumed — and, separately,
                                   WHAT THAT WOULD CONSTRAIN about the
                                   temporal boundary condition the
                                   programme has not yet ruled on. A
                                   theorem assuming one choice is
                                   unavailable under another, so this
                                   axis is not only a coverage question:
                                   it tells the PI what a future ruling
                                   would cost in coverage
    5  locality assumptions        ultralocal, exponentially local, or
                                   none — overlap is not ultralocal and
                                   this axis is where that bites
    6  measure and determinant     Grassmann measure with determinant
                                   signs. ONTOLOGY line 79 states that a
                                   bosonic Ising example cannot be
                                   transplanted; the same caution
                                   applies to any bosonic result
    7  gauge content               the candidate actions carry no gauge
                                   field; a theorem stated for gauge
                                   theories may or may not specialise

**The seven are COMMON axes. They are not the whole test.**

**Every theorem additionally carries its own hypotheses, and each must be
listed and mapped:**

    OPERATOR/PARAMETER HYPOTHESES
      dimension; operator normalisation; mass range; the Wilson
      parameter r; hopping-parameter domain; the overlap kernel mass or
      domain-wall height M0 and any restriction on it; coupling
      restrictions; and any other hypothesis the fetched work states

**A COVERAGE BASIS may be one fetched theorem, or a FINITE SET of
fetched theorems whose conclusions and hypotheses compose without any new
scientific lemma supplied by the executor.** **Every junction in the
composition must be explicitly mapped.** **If the executor must invent or
prove a missing lemma, the result is NOT `COVERED`.**

**This matters because much of the relevant literature is structured that
way**: one theorem establishes reflection positivity for a free kinetic
action, another establishes that adding an interaction of a stated form
preserves it. **Requiring a single paper to cover
`S_kinetic^(X) + S_NJL` alone would systematically understate what the
literature already gives.**

**`COVERED` requires EVERY common axis AND EVERY theorem-specific
hypothesis — of every theorem in the basis — explicitly mapped to the
candidate action.** **Not "compatible" — MAPPED.** **A hypothesis the candidate action has not
frozen cannot be mapped**, and **a theorem requiring `0 < M0 < 2` cannot
cover a candidate whose `M0` is unfrozen**, however many common axes
agree.

**An earlier version of this section made the seven axes the whole test
and defined coverage as compatibility.** **Compatibility is weaker than
applicability**, and seven passing axes with an unfrozen parameter would
have produced a `COVERED` verdict for a theorem that does not apply.

**Report all seven axes AND the full hypothesis list PER RELEVANT
THEOREM–CANDIDATE PAIR.** **A `COVERS` verdict with any axis or any
hypothesis unreported is a STOP.**

**Relevance is declared per work, not assumed.** **For each fetched work,
state:**

    CANDIDATES APPLICABILITY-TESTED     the ones it could bear on
    NOT AN APPLICABILITY CANDIDATE      the others, with one line saying
                                        why

**A theorem stated for Wilson fermions is not `PARTIAL` for staggered.**
**It is not an applicability candidate at all**, and recording it as
`PARTIAL` would fill the table with entries that read as near-misses and
are nothing of the kind. **`PARTIAL` means genuinely close with a named
mismatch, and that meaning has to be protected.**

**An axis may favour one candidate and disfavour another, and the report
must not collapse it.** **Axis 7 is the clearest case: the candidate
actions carry no gauge field, so a theorem stated FOR gauge theories has
to be specialised, while a theorem stated for NON-GAUGE models is
directly in the right class.** **The same axis, opposite directions.**
**Report per candidate; do not report an axis once for all four.**

**`PARTIAL` is expected to be the common answer and is useful**: naming
which hypothesis fails tells the next task exactly what would have to be
proved.

**A theorem or construction establishing proposition `(i)` ONLY cannot
contribute positively to a proposition `(ii)` coverage verdict**, unless
the fetched work **explicitly proves OS or reflection positivity of the
Euclidean action or measure**, or **supplies a theorem that logically
implies it under mapped hypotheses.**

**Record transfer-matrix-only literature SEPARATELY, as `ROUTE
EVIDENCE`, not as coverage.**

**This matters most for `staggered`**, whose literature is likely to be
transfer-matrix constructions. **`B0` spent an entire task separating
`(i)` from `(ii)`**, and a coverage verdict that absorbed a transfer
matrix would undo it in one line.

## 5. The verdicts

**Per candidate — `naive`, `Wilson`, `staggered`, `overlap` — and for
proposition `(ii)` only**, report one of:

    COVERED           one fetched theorem, OR an explicitly composable
                      fetched theorem set, covers the frozen interaction
                      with that candidate's kinetic term — every common
                      axis and every theorem-specific hypothesis mapped,
                      and every composition junction mapped. Name the
                      basis and every theorem in it.
    PARTIAL           a fetched theorem is close; name every axis that
                      fails and the exact hypothesis
    NO COVERAGE FOUND nothing fetched applies
    NOT DETERMINABLE  the precondition failed, or the works could not
                      be fetched

**Four results.**

**Burden accounting is DISCRETE. Do not estimate fractional
reductions.**

    COVERED             one candidate-specific (ii) from-new-construction
                        unit is REPLACED by theorem-applicability
                        documentation. Not removed — replaced.
    PARTIAL             ZERO units removed. Name the remaining mismatch
                        precisely.
    NO COVERAGE FOUND   ZERO units removed.
    NOT DETERMINABLE    no burden conclusion at all.

**Then report one sentence:** *of `B0`'s four candidate-specific `(ii)`
construction units, X are replaced by literature-applicability work and Y
remain full or open.*

**An earlier version asked how many constructions a `PARTIAL` verdict
would "reduce".** **There is no scale on which that is answerable** —
`B0`'s own lower bound is not firm, and *reduces by 0.6 of a
construction* is not a scientific statement. **Discrete accounting or
none.**

## 6. What this task must not do

- **Do not touch `main`**, do not merge.
- **Do not proceed from memory if §1 fails.**
- **Do not design a proof route**, and do not state what a proof would
  look like beyond naming the failing hypothesis.
- **Do not select, eliminate, rank or prefer a candidate.** **A candidate
  with more literature coverage is not a better candidate** — **it is a
  candidate whose remaining work is smaller, and effort is not
  evidence.**
- **Do not conduct a general literature review** — **but `B0`'s four
  claims and the `L3` gap are SEARCH SEEDS, not a boundary.**

  **PURSUE any work that could settle or materially reduce proposition
  `(ii)` for any of the four candidates**, whether or not `B0` recorded
  it. **`B0` recorded what it could recall, and recall is exactly what
  this audit exists to correct** — **a work `B0` failed to remember is
  the most likely place for the audit's value to be.**

  **An earlier version of this clause said to record such works and NOT
  pursue them.** **That would have made the audit's answer a function of
  `B0`'s memory**, and would have biased every verdict toward
  `NO COVERAGE FOUND` in exactly the rows where `B0` recalled least.

  **What remains forbidden is breadth without bearing**: a work that does
  not plausibly settle or reduce `(ii)` for a named candidate is recorded
  with its identifier and not pursued.
- **Do not re-derive `B0`'s estimate**, and do not revise it.
- **Do not add a register entry.**
- **Do not modify any existing file.**

## 7. Acceptance criteria

**A1 — Repository identity FIRST, then refs, then branch-name
availability.**

**The branch to create is `science/d1-literature-coverage-audit-3`, and
the `-2` name is deliberately not reused.** **Measured: a local branch
`science/d1-literature-coverage-audit-2` exists at `a537e036…`, checked
out in a worktree, descending from the superseded base `bfef924c…`.**

**That branch is the residue of `D-1` EXECUTION 2**, which reached
commit 3 and stopped at `A14` when
`tests/test_gate_pins.py::test_a_stale_pin_is_detected` failed on
Windows. **It was never pushed, never integrated, and the specification
it carries is a superseded revision.**

**The naming used throughout, fixed once:**

    D-1 execution 1     branch …-audit @ 8267bd40
                        sandbox; STOP at §1, twelve scholarly hosts
    D-1 preflight 2a    STOP on a stale local refs/heads/main
    D-1 preflight 2b    STOP in the wrong repository, 0-programme
    D-1 execution 2     branch …-audit-2 @ a537e036
                        reached commit 3; STOP at A14
    D-1 preflight 3a    STOP on branch-name occupancy — this criterion
    D-1 execution 3     branch …-audit-3, the present execution

**A PREFLIGHT is a stop before any branch exists. An EXECUTION is one
that created a branch.** **Three executions, three preflight stops, and
no nested "first attempt at a second execution" phrasing anywhere.**

**Do not delete it, reset it, remove its worktree, or reuse its name.**
**It is a record of an attempt, and this specification's own prohibition
on rewriting existing branches applies to it.** **Execution 3 takes a
third name, and the two coexist so that a later reader can see what
happened rather than infer it.**

**Report whether `science/d1-literature-coverage-audit-3` already
exists.** **If it does, STOP** — a fourth name is not this
specification's to choose.

**The evidence base was rebased from `bfef924c…` to `b27926aa…` after
the pin-test repair landed.** Measured: **seven paths differ between
them** — six task records and `tests/test_gate_pins.py` — and **the
artifact this audit reads,
`derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md`, is
BLOB-IDENTICAL at both.** **The three structured claims and the `L3` gap
are unchanged; only the base moved.**

**THE REPOSITORY IS `zetacheng/2-emergent-gravity`.**

**Before any ref is read, report the workspace's `origin` remote URL AS
MEASURED — verbatim, and NOT normalised in the evidence record.**

**Confirm that it identifies the repository `zetacheng/2-emergent-gravity`.**
**Accept equivalent GitHub URL forms, with or without the terminal
`.git`.** **STOP only if the OWNER or REPOSITORY identity differs** —
`0-programme` in particular. **Do not clone, do not switch remotes, and
do not guess.**

**An earlier version of this criterion required the URL to equal a
string ending in `.git`.** **Measured in this line: the same repository's
`git remote get-url origin` returned the form WITHOUT the suffix**, and
an executor correctly judged the two equivalent and did not stop.
**Requiring the exact string would have produced a third stop on
execution-environment metadata rather than on anything about the
task.**

**This specification named no repository until now.** **`D-1` preflight
2b ran in `zetacheng/0-programme`, whose `origin/main` is `ada3087a…`,
and correctly stopped because the required base was absent there.** **The defect was this specification's**: every previous executor
happened to start in the right repository, so the omission never bit.

**The authoritative ref is `refs/remotes/origin/main`.**

**Fetch first, then report BOTH refs as measured:**

    refs/remotes/origin/main    authoritative — must be b27926aa…
    refs/heads/main             reported for contrast; may legitimately
                                differ, and a difference is NOT a stop

**Confirm `origin/main` is `b27926aa…`.** **If IT has advanced, STOP and
report both** — the three claims and the `L3` gap are read from a file
whose content this specification quotes.

**A local `refs/heads/main` that lags is a property of the clone, not of
the repository.** **If the two differ, report the difference, report
whether the local ref is an ancestor of `origin/main`, and CONTINUE.**
**Do not update it** — the specification forbids changing repository
state, and aligning a ref to satisfy a criterion is the shape this
programme has consistently refused.

**An earlier version of this criterion named `refs/heads/main` as the
thing to confirm.** **`D-1` preflight 2a stopped there, correctly**: `origin/main` was `b27926aa…` while
`refs/heads/main` was `fd5f6b96…`, an ancestor. **The executor reported
both, changed nothing, and did not infer a resolution.** **The defect was
this specification's — every verification in this programme has used
`origin/main`, and the criterion named the local ref.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — The §1 precondition, reported before anything else.** **Report
every host attempted and the outcome of each.** **If the precondition
failed, the task STOPS here and A4 through A8 are not attempted** —
**report that as the result, not as an incomplete run.**

**A4 — The three structured claims and the `L3` literature gap, read
from `main`**, with the file's own wording and line numbers. **Confirm
`L3` names no work**, and **confirm the source records three claims and
one gap rather than four claims.**

**A5 — Identifiers and fetch DEPTH per work.** **Report listing,
abstract, or full text for each**, the count at each depth, and the count
recalled. **Every `RECALLED` statement labelled as such at every
occurrence.** **Report which works are load-bearing and available only
at abstract depth**, and **confirm none of them supports a `COVERED`
verdict.**

**A6 — Seven common axes AND the theorem-specific hypothesis list, PER
RELEVANT THEOREM–CANDIDATE PAIR**, per §4. **Report the
applicability-tested and not-an-applicability-candidate declaration for
every fetched work.** **Report the full table and the full
hypothesis list.** **A `COVERS` with any axis or any hypothesis
unreported, or with any hypothesis unmapped because the candidate has
not frozen the parameter, is a STOP.**

**Report separately any `ROUTE EVIDENCE`** — transfer-matrix-only works
— **and confirm none of it contributed to a `(ii)` coverage verdict.**

**A7 — Four verdicts**, per §5, with the count of each. **And the
DISCRETE burden accounting**, with the closing sentence in §5's form:
`X` replaced, `Y` full or open. **No fractional reductions.**

**A8 — Works encountered and not pursued**, per §6, with identifiers.
**Report the count.** **Zero is an acceptable answer.**

**A9 — No selection, no route design.** **Search the artifact, the report
and the commit messages for any sentence that selects, ranks, prefers a
candidate, or describes how a missing proof would be constructed.**
**Report the search and the finding.** **Report the treatment length per
candidate and whether the lengths differ**, with the reason — **coverage
genuinely differs between candidates, so unequal lengths are expected and
must be explained rather than levelled.**

**A10 — Scope, frozen manifest.**

    stated: 4 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: <the measured main at execution>
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md
      reports/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md
      specs/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths. `modify:` is `[]` and must remain so.**

**If §1 fails, commit 3 is still written** — **it records the
precondition failure and the hosts attempted, and nothing else.**

**A11 — Nothing existing changed.** Every path at the evidence base is
blob-identical at the head. **Report the count compared.**

**A12 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; both pins match. **Report all four.**

**A13 — The checker over this task's own range**, base the measured
`main`, head **commit 3**. Two runs, `RUN 1` observational and `RUN 2`
naming only this task's specification.

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.** **`P7` must report fourteen sections.**
**`PASS` at zero is a STOP.** **RUN 2 is stop-governing.** **Both configs
and both JSON outputs verbatim.**

**A13-final, post-report evidence:** re-run RUN 2 at commit 4.

**A13a — Environment conformance, BEFORE any measurement is reported.**
**Run `CONVENTIONS.md` Rule 13's diagnostic order including Amendment
D's step 0**, and **report location, workspace depth, and package
availability.**

**Report whether the clone is shallow and its commit count.** **If a
restoration is needed, report it in one line each and confirm no
repository content was touched to make the environment work.**

**This criterion exists because a container in this line was found
non-conformant** — shallow at 142 commits, with `pytest`, `numpy` and
`sympy` absent — **and its first suite run gave five failures, all `git
rev-parse … Needed a single revision`, none touching the subject.** **A
suite result taken before this check is uninterpretable.**

**A14 — Validators, exit status 0.** **Expected 324 passed, 2
deselected.**

**`tests/test_gate_pins.py::test_a_stale_pin_is_detected` was repaired at
`b27926aa…` and no longer depends on the platform's newline
translation.** **If it fails here, that is a finding and not an expected
condition.** **If you see 5 failed / 319 passed, re-read `A13a`.**

**A15 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 8. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md
    commit 3  derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md
    commit 4  reports/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused. **You choose
no path.**

**Committed report — measured at commit 3:** A1–A12, A14 and A15;
**A13's two runs with both configs verbatim**; commit 1–3 SHAs and stored
messages; commit 4's intended message; **A10's final scope stated as
INTENDED.**

**Post-report evidence, NOT written back:** A10's final scope measured
base-to-commit-4; A13-final; A14 at commit 4; A15 for commit 4; the
push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 9. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** **`COVERED` means the fetched theorem, or the explicitly
composable theorem set, has had EVERY common axis and EVERY
theorem-specific hypothesis explicitly mapped to the candidate action.**
**It means the literature result is applicable under that mapping.**
**It does not mean the programme independently reproved the theorem.**

**An earlier version of this junction said `COVERED` means hypotheses
are "compatible on seven axes"** — **the definition §4 expressly
replaced, and one that omitted the theorem-specific hypotheses
entirely.** **Two normative definitions in one document is a defect
whichever is right.**

**And the accurate limitation is narrower than "not a proof".** **If the
hypotheses are fully mapped, the published theorem applies as
mathematics.** **What is missing is a repository-level applicability
derivation and its provenance, not a further physics proof.** **Say:
literature applicability is not an independent repository proof of the
theorem** — **which is exactly what `A7`'s "replaced by
theorem-applicability documentation" accounts for.**

**Second.** **Coverage is not evidence about physics.** **A candidate
with more literature behind it is not more likely to be the right
microscopic theory** — **it is a candidate other people happened to
study.** **Say this where a reader meets the four verdicts.**

**Third.** **This audit is bounded by what was fetched.** **Report how
many works were fetched and how many statements remain `RECALLED`**, and
**say that a `NO COVERAGE FOUND` verdict means nothing fetched applies,
not that nothing exists.**

**Fourth.** **`L3` is a gap, not a claim: it names no work, so the
staggered row rests on nothing.** **Say whether the audit filled that gap or left it open**, and
**do not let an unfilled gap read as an absence of coverage.**

## 10. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  coverage artifact. **Nothing else, at all.**
- **No file existing at the evidence base may be modified.**
- **Do not proceed from memory if §1 fails.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 11. Report contract

- everything in §8 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A3's precondition result first**, before any content;
- **A4's three structured claims and the `L3` gap, with line numbers**,
  and the confirmation that the source records three and one, not four;
- **A5's identifiers, fetch depths, the counts at each depth, and the
  abstract-only load-bearing works**;
- **A6's seven-axis table AND the theorem-specific hypothesis lists**,
  **axis 4's separate statement of what each theorem's
  boundary-condition assumption would constrain about the pending
  temporal-boundary ruling**, and **the `ROUTE EVIDENCE` list with the
  confirmation it contributed nothing to coverage**;
- **A7's four verdicts with counts and the DISCRETE burden accounting**,
  including the closing `X` replaced / `Y` open sentence;
- **A8's encountered-and-not-pursued list with identifiers**;
- **A9's search, finding, and per-candidate treatment lengths with the
  reason for any inequality**;
- **A13's two runs**, both configs verbatim, the section count `P7` saw,
  and what `RUN 1` did;
- **§9's four Rule 16 junctions**;
- **whether the audit made you want to design a proof route or select a
  candidate.** **Say which and why, and confirm you did not**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

**A `§1` precondition failure is `ENVIRONMENT`**, and **the task is
complete when it is reported.**

## 12. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      whether "the declared action" exists
    method      read P2-CHANNEL-FREEZE-01_phaseA_freeze.md 2 and
                P2-LATTICE-ONTOLOGY-01 line 189 on main
    MEASURED    the INTERACTION is frozen as the U(N) chiral NJL
                generator-sum form. The CANONICAL KINETIC OPERATOR is
                DELEGATED and not frozen. There are four candidate
                actions and no declared action, which is why 0 requires
                the coverage question asked per candidate.

    target      the three structured literature claims and the L3 gap
    method      read the AUTHOR/WORK blocks of
                P2-LATTICE-MICROSPEC-01_tm-rp-scope.md on main
    MEASURED    L1 Osterwalder-Schrader 1973 and 1975; L2
                Osterwalder-Seiler 1978; L4 Neuberger, and Hernandez-
                Jansen-Luscher on locality. THREE STRUCTURED CLAIMS.
                L3 carries AUTHOR/WORK NOT RECALLED and SCOPE NOT
                RECALLED and is a GAP, which B0 expressly declined to
                count as a claim. NONE CARRIES AN IDENTIFIER. All are
                marked UNVERIFIED FROM THIS REPOSITORY.
    NOTE        an earlier draft of this specification called them
                "four claims" in its section heading and in this record
                while correcting the count two lines below the heading.
                A correction that does not reach the heading and the
                verification record has not been made.

    target      branch-name availability
    method      the third executor reported
                refs/heads/science/d1-literature-coverage-audit-2 =
                a537e036311c8b9a77567062943b2e8af500076e, checked out in
                a worktree under .agents/, descending from bfef924c
    MEASURED    the name is occupied by execution 2's residue.
                That branch was never pushed — it is absent from the
                Researcher's clone of the remote — and carries a
                superseded specification revision. Execution 3
                therefore takes the -3 name.
    NOT MEASURED by this author: the worktree path and the branch tip
                are the executor's report, not the Researcher's
                observation. The branch is not on the remote and cannot
                be checked from here.

    target      the repository this specification governs
    method      git remote get-url origin in the Researcher's clone;
                and the reported remote of D-1 preflight 2b
    MEASURED    the governed repository is
                https://github.com/zetacheng/2-emergent-gravity.git,
                whose origin/main is b27926aad0d3a1ef39f5e7e886f8571657c5687c.
                D-1 preflight 2b ran in
                zetacheng/0-programme, origin/main ada3087a…, where
                bfef924c is absent. A1 now names the repository.

    target      whether the executor can fetch published work
    method      NOT MEASURED. The Researcher's own bash network is
                restricted to package and code hosts and cannot reach
                arxiv.org; the executor's environment is separate and
                its configuration is not visible from here.
    CONSEQUENCE 1 is a precondition rather than a criterion, and a
                precondition failure is a complete and useful outcome.
                A specification that assumed reachability would have
                produced an audit from memory, which is the failure this
                task exists to correct.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations. append_only carries
                one path.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker on main
                and executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 0 modifications;
                parse OK, counted equals stated per category.
