# Task specification — land the diquark line: adjudication, both-η result, and a sensitivity addendum

Specification evidence base: `57c5a6eb1de11bb7aaf27b779054070ee6870c29`

> ## RE-ISSUE — the first issue stopped correctly
>
> **The first issue stated `merge-base = 57c5a6eb…` for both merges.
> That value is impossible.** Both source branches were cut from
> `8701a97a…`, `main`'s previous head, and `main` has since advanced
> through the chirality-census work. **The true merge-base is
> `8701a97a…` for both.**
>
> **The executor stopped at A3's `PRE_MERGE` guard, before any tree
> changed, and merged nothing.** That was correct: A2 was
> **unsatisfiable, not merely unverified**, and the only ways to make it
> hold — rebasing a source branch, or merging something other than the
> pinned refs — are forbidden.
>
> **The first issue's `§10` recorded `CONFIRMED both branches share the
> merge-base 57c5a6eb…`. That check was never executed.** The dry-run
> merge was run and succeeded; the merge-base was asserted, not measured.
> **An unexecuted `CONFIRMED` in an Amendment H record is the failure
> that amendment exists to prevent**, and it is recorded here rather
> than quietly corrected.
>
> **Per Amendment K this is a re-issue on a NEW branch under NEW
> task-identity paths.** `gate/p2-land-diquark-line @
> d64cd912ca9ff78a85787f0e54f345f474cdb192` is **preserved, superseded
> for integration, and not carried forward.** Its report is the record
> of the stop.
>
> **Everything else in the first issue reproduced**: all three refs, all
> fourteen blob ids, both merges conflict-free. **The correction is two
> values and one missing criterion.**

    Branch 1  gate/p2-diquark-adjudication
              3767973bf57c52f4dd2be1fddcf62916ec409c72
    Branch 2  gate/p2-diquark-both-eta
              bc1e5c743aada004c52dc7ab7ce2af61de439955

Classification: **MATERIAL**. Governed by Rule 15: this task's
pre-execution review is a committed artifact — see §5 commit 2 and A5.

**TWO merges, in the stated order.** Dry run of both in sequence:
**14 additions, 0 modifications, no conflict**, each merge-base the
original base. **If either conflicts, STOP.**

**The adjudication merges FIRST.** It is what lifted the other branch's
`HOLD`, and the addendum this task writes depends on its finding.

**Review artifact delimiters**, each a whole line:

    === REVIEW ARTIFACT BEGINS ===
    === REVIEW ARTIFACT ENDS ===

---

## 0. Why two merges in one task

**These are not two independent results.** `gate/p2-diquark-both-eta`
was held under `HOLD — MATERIAL RESULT DISCREPANCY` because an
independent recomputation disagreed with it. `gate/p2-diquark-adjudication`
established that **the disagreement was caused by the independent
computation, not by the branch**: that computation omitted two frozen
conventions.

**Landing the result without the adjudication would put a number on
`main` whose challenge and resolution live nowhere.** Landing the
adjudication without the result would record a resolution to a dispute
about something absent. **They are one episode.**

**This does not weaken the one-merge discipline.** Each merge is
verified separately, each has its own parentage and blob checks, and
**a conflict in either stops the task.**

## 1. What lands

**From the adjudication.** The discrepancy's cause, localised:

    the independent method omitted the frozen canonical pseudoscalar
    i*gamma5 and the frozen factors of i on the A and T basis elements

    (i g5) x (i g5) = -(g5 x g5), so the two canonical terms of S^2+P^2
    add where they would otherwise cancel; restoring the i moves the
    surviving support from S/P/T to V/A

    established by quotation from the freeze, not by preferring a method

    L3 was IDENTICAL: the two rank-4 tensors matched, so this was NOT
    an ordering divergence and the pp Grassmann ordering hypothesis was
    neither confirmed nor refuted

**From the both-η result.** The particle–particle channel character for
both `η` representatives, and the diagnostic verdict:

    c_S = c_P = c_T = 0,  and c_V = -c_A, non-zero

    OPPOSITE: the two eta representatives give opposite channel
    character, because every coefficient has the form c = K*eta

**That verdict is what PI Decision 2 was designed to expose.** It means
**a diquark channel character depends on an unresolved sign
convention**, and any downstream use of that channel inherits the
dependence.

## 2. The addendum this task writes

**Land `derivations/P2-PHASE-01_diquark_sensitivity_addendum.md`.**

**Its purpose.** The both-η derivation correctly uses and states the
frozen conventions. **What it does not record is that one of them is
load-bearing for its own family support** — a reader would not know that
the V/A support rests on the canonical pseudoscalar carrying `i·γ₅` and
on the A/T basis elements carrying `i`.

**This is not a correction.** The branch is right. **It is a record of a
sensitivity**, and it must say so.

**Contents:**

- **the sensitivity**, with the mechanism `(iγ₅)⊗(iγ₅) = −(γ₅⊗γ₅)` and
  the ablation's outcome;
- **that both conventions are FROZEN, not free** — so this is **not** a
  newly discovered unfrozen dependence;
- **why it is recorded anyway**: a later reader assessing the
  robustness of `c_S = c_P = c_T = 0` needs to know what it rests on;
- **the relation to the chirality census now on `main`**, which explains
  the same vanishing structurally — **cite it, and state that the census
  explains SUPPORT only**, not the coefficient signs or magnitudes;
- **the independence claim, stated at the level the evidence
  licenses**: the adjudication **found no evidence against** the
  branch's claim that its verdict is independent of the two remaining
  unfrozen definitions, since L3 was identical and the divergence was
  not an ordering effect. **It did not establish independence over
  untested admissible pp orderings**, and no alternative slot map was
  tried;
- **what remains unfrozen**: `η`, the particle–particle Grassmann
  ordering, the diquark normalisation.

**Do not restate the coefficients as a new result**, and **do not
resolve any unfrozen convention.**

## 3. What this task does NOT establish

- **The diquark channel is not settled.** Three conventions remain
  unfrozen and the absolute channel character is undetermined.
- **`OPPOSITE` is a relative statement.** It says the two `η`
  representatives differ; **it does not assign either an absolute
  attractive or repulsive character.**
- **Nothing about composite states.** A channel-character label is not
  a bound-state or pole calculation, and **`REPULSIVE` in any channel
  does not imply a composite vector is absent.**
- **The pp ordering question is open**, in both directions. The
  adjudication tested no alternative slot map.
- **No gate status changes.** `P2-PHASE-01` stays `PROPOSED`.

## 4. What must not happen

- **Do not edit anything arriving by merge.** Both branches are
  integrated exactly as reviewed.
- **Do not select `η`**, freeze the pp Grassmann ordering, or fix the
  diquark normalisation.
- **Do not repair either branch's script**, and do not adjudicate the
  unresolved `P`-sign difference recorded in the chirality census
  integration.
- **Do not state that the census explains the coefficient signs.**
- **Do not touch `tests/` beyond the two arriving test files.**

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_land-diquark-line.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_land-diquark-line.md
    commit 3  --no-ff merge of gate/p2-diquark-adjudication
    commit 4  --no-ff merge of gate/p2-diquark-both-eta
    commit 5  derivations/P2-PHASE-01_diquark_sensitivity_addendum.md
    commit 6  reports/2026-08-XXT{HHMM}Z_land-diquark-line.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **The token MUST differ from
`2152`**, which the superseded first issue used — reusing it would make
the two executions indistinguishable by path, which is what Amendment K
requires new task-identity paths to prevent.

**Commit 2 precedes both merges.** **Commit 5 follows both**, because
the addendum records a relation between them.

**If the task stops before the merges**, the frozen order does not
apply beyond the point reached. **Commit the report as the next commit
in sequence and say which number it is and why** — do not renumber
silently, and do not omit the report because the order named a later
position for it. **The first issue met exactly this case and resolved
it the same way; the resolution is now specified rather than
improvised.**

**Committed report:** raw output for A1, A2, A6–A10, A11-pre, A12 for
commits 1–5; both `PRE_MERGE` JSONs verbatim; the intended final
manifest and the intended final `POST_MERGE` parameters; commit 1–5 SHAs
and messages; the pre-report head; the intended report commit message.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final `POST_MERGE` JSON, A4's final scope check, A11-final, the
push, the report commit's stored message read back from the object, and
ancestry confirmation.

## 6. Acceptance criteria

**A1 — Refs.** `refs/remotes/origin/main` and remote `refs/heads/main`
both resolve to `57c5a6eb1de11bb7aaf27b779054070ee6870c29`; branch 1 to
`3767973b…`; branch 2 to `bc1e5c74…`. Any mismatch → STOP. **Local
`main` is stale by design.** Report all refs, read from the remote.

**A2 — Merge parentage, for BOTH merges.** **Parent 1 is fixed by which
commit you are standing on**, and the two differ:

    merge 1 (commit 3)
      parent 1 = the pre-execution review commit (commit 2)
      parent 2 = 3767973bf57c52f4dd2be1fddcf62916ec409c72
      merge-base = 8701a97a6bb58550d4300f75c10638b057335731

    merge 2 (commit 4)
      parent 1 = merge 1 (commit 3)
      parent 2 = bc1e5c743aada004c52dc7ab7ce2af61de439955
      merge-base = 8701a97a6bb58550d4300f75c10638b057335731

**Both merge-bases are `8701a97a…`, NOT the evidence base.** The two
source branches were cut from `main`'s previous head; `main` has since
advanced. **`merge-base(branch 1, branch 2)` is also `8701a97a…`, and
the first issue confused that fact with `merge-base(evidence base,
branch)`.** They are different quantities and only the second is what
A2 constrains.

**Derive each merge's three values SEPARATELY from the objects.** **Do
not compute one and carry it to the other under a shared rationale** —
that is precisely how the first issue's error reached both entries at
once, in a criterion whose own text forbids it.

**Commit 1 MUST be an ancestor of both merges.**

**A2a — Source-branch ancestry, stated as its own property.** For each
source branch, report:

    git merge-base --is-ancestor <evidence base> <branch head>

**Neither branch descends from this evidence base**, and that is
expected: they were cut from `8701a97a…` and waited while `main`
advanced. **Report it as an observed fact, not a failure.**

**This criterion exists because the first issue had no place to see
it.** The underlying property — whether a source branch descends from
the base a specification names — **was never checked in this sequence
because every previous integration merged a branch cut from the
then-current `main`.** **This is the first task where branches waited**,
and a one-line ancestry test would have made the impossibility legible
before the guard hit it.

**A3 — Guards.** A `PRE_MERGE` before EACH merge — **two of them** — and
one final `POST_MERGE` after the push. **The final guard carries TWO
DISTINCT SHAs**: the merge object under verification and the final
report-commit head. **If the guard cannot represent both roles
separately, STOP.**

**A4 — Scope, frozen manifest:**

    base: 57c5a6eb1de11bb7aaf27b779054070ee6870c29
    head: <computed final head>
    mode: exact
    add:
      derivations/P2-PHASE-01_diquark_adjudication.md
      derivations/P2-PHASE-01_diquark_both_eta.md
      derivations/P2-PHASE-01_diquark_sensitivity_addendum.md
      reports/2026-08-10T0245Z_diquark-both-eta.md
      reports/2026-08-10T1112Z_diquark-adjudication.md
      reports/2026-08-XXT{HHMM}Z_land-diquark-line.md
      results/P2-PHASE-01/diquark-adjudication/adjudication.json
      results/P2-PHASE-01/diquark-both-eta/diquark.json
      reviews/chatgpt/2026-08-10T0245Z_diquark-both-eta.md
      reviews/chatgpt/2026-08-10T1112Z_diquark-adjudication.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_land-diquark-line.md
      scripts/p2_diquark_adjudication.py
      scripts/p2_diquark_both_eta.py
      specs/2026-08-10T0245Z_diquark-both-eta.md
      specs/2026-08-10T1112Z_diquark-adjudication.md
      specs/2026-08-XXT{HHMM}Z_land-diquark-line.md
      tests/test_p2_diquark_adjudication.py
      tests/test_p2_diquark_both_eta.py
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 18 additions and 0 modifications**, matching
the eighteen paths above. Fourteen arrive from the two branches; four
are authored here.

**A5 — This task's pre-execution review committed, unedited**, at the
`reviews/chatgpt/` path of §5, **byte-identical to the text between the
delimiter literals at the head of this specification, excluding the
delimiter lines, any preamble before the BEGIN line, and any
accompanying instruction.**

**Match the delimiters as COMPLETE LINES** — this specification contains
them. **Placeholders inside the review's text stay as written**; resolve
them in the path only.

**Strip at most one leading and one trailing blank line as transport
artifacts; apply no other normalisation.**

**The correspondence test needs something to test against.** The first
issue's review named neither source-branch SHA, so the executor had to
judge correspondence from wording. **This specification's review should
name both source-branch heads and this specification's own digest; if
it does not, record which markers you used instead** rather than
treating correspondence as established.

**If the supplied text is missing, carries no delimiter lines, or does
not correspond to this specification, STOP and say which.**

**A6 — Arriving artifacts intact, branch 1:**

    derivations/P2-PHASE-01_diquark_adjudication.md
    7983d4ba1d4dab4b83a31dc90a6a92a99af93d4e

    reports/2026-08-10T1112Z_diquark-adjudication.md
    48bc29652e26458302a0384ce79be03c23557726

    results/P2-PHASE-01/diquark-adjudication/adjudication.json
    77805645d385c45a832000b040d64b45906cf3c8

    reviews/chatgpt/2026-08-10T1112Z_diquark-adjudication.md
    2c7806f9baec7c940e9859abf39eab0c5c7df0ca

    scripts/p2_diquark_adjudication.py
    529d5ef01b02908d3b8e276bebcbbae6b79554f4

    specs/2026-08-10T1112Z_diquark-adjudication.md
    f74ccb54880fb7cf0dc32205b72f418a9b958686

    tests/test_p2_diquark_adjudication.py
    e9792963858f4fa5457c8f06d7a3126e17035e9f

**A7 — Arriving artifacts intact, branch 2:**

    derivations/P2-PHASE-01_diquark_both_eta.md
    e0eff7469e08e093dfd9caed5ca2bec1a1ef01f4

    reports/2026-08-10T0245Z_diquark-both-eta.md
    dd21f90c1eb69d2cadfbca1ce85f8cef03c38171

    results/P2-PHASE-01/diquark-both-eta/diquark.json
    b9af37d053d77926daed86842bc4f20bf861a6aa

    reviews/chatgpt/2026-08-10T0245Z_diquark-both-eta.md
    63d09ee924c4ac3a9c4dd67924cc571e2ba02970

    scripts/p2_diquark_both_eta.py
    5158201252ff1d1629ad056787f8c07c36469146

    specs/2026-08-10T0245Z_diquark-both-eta.md
    2ee216810c26cbbd7810f42c1323c7b75b46837b

    tests/test_p2_diquark_both_eta.py
    abcd0a2281d852ff34d78c6e8a002616016a114f

**These are Git blob ids, not content SHA-256 digests.** Compare with
`git rev-parse <rev>:<path>`.

**A8 — Protected paths.** `GATES.md`, `CONVENTIONS.md`, `AGENTS.md`,
`DECISION_LOG.md`, `pyproject.toml`, and **every path under `scripts/`,
`results/`, `tests/`, `derivations/`, `docs/` and `reviews/` that exists
at the evidence base**: blob-identical between base and merged head.
**Compare path by path, not as tree objects.**

**`tests/` gains exactly two arriving files and no existing test is
modified.** Report the count before and after.

**A9 — No gate changed.** `GATES.md` blob-identical; `^## P2-` count 14
before and after; `P2-PHASE-01` still `PROPOSED`; `P2-GAP-01` still
`PASS`.

**A10 — The addendum**, per §2, with each required element present.
**Report it in full**, and state explicitly that it corrects nothing.

**A11 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`, `tests/test_p2_channel_character.py`,
`tests/test_p2_chirality_census.py`, `tests/test_p2_diquark_both_eta.py`,
`tests/test_p2_diquark_adjudication.py`. **A11-pre** at the pre-report
head goes in the report; **A11-final** at the pushed head is post-report
evidence.

**A12 — Commit-message hygiene** on every commit including both merges:
inspect the proposed message before, the stored message after; permit no
`Co-Authored-By`, no session identifier or URL, no tool attribution.
**Report per commit whether any trailer was suppressed and which.**

**A13 — Branches preserved.** Both source branches still resolve to
their recorded commits; **`review/role-model-and-executors` @
`10c260b96882ac12610f78840aeeabd07be2d7cb` remains untouched.** **This
task deletes no branch.**

## 7. Rule 16 assessment

**Rule 16 is operative and governs this task.** State what the assembled
set does NOT establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** After this
task `main` will carry: a particle–hole coefficient table, a
particle–particle coefficient table, a chirality selection rule, an
adjudication resolving a discrepancy, and a sensitivity addendum. **A
reader could conclude the interaction's channel structure is now
understood.** **It is not.** Three conventions remain unfrozen; the
absolute channel character is undetermined; the inter-channel sign is
unexplained; and **the pp ordering question was neither confirmed nor
refuted.**

**If you find a stronger junction, report that instead.**

## 8. Invariants and prohibitions

- Executor-writable: the four paths authored here — this specification,
  its pre-execution review, the addendum, and the report.
- **Do not draw any conclusion §3 forbids or perform any act §4
  forbids.**
- No gate, gate status, verdict, digest, or hash-pinned artifact may be
  modified.
- Merge commits only: no fast-forward, no squash, no rebase, no
  force-push, no history rewrite. **Merge the pinned remote refs.**
- **Any merge conflict, in either merge, is an immediate stop.**
- Branch naming: use `gate/p2-land-diquark-line-v2`. **The first
  issue's branch is preserved at `d64cd912…`, superseded for
  integration; do not touch, reuse or delete it.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything listed in §5 under its correct layer;
- **both merge commits' SHAs, parents and merge-bases, reported
  separately**;
- A6 and A7's blob comparisons, fourteen in all;
- A8's path-by-path comparison with the `tests/` count before and after;
- the addendum in full;
- **§7's Rule 16 assessment**, junction named or search described;
- **whether the merged state reads as though the diquark channel's
  character were determined**, or as though `OPPOSITE` were an absolute
  label. **Neither is true**;
- **whether landing two merges in one task cost anything in clarity.**
  **The first issue answered this and the answer should be tested, not
  repeated**: the cost was not the merge count but a SHARED RATIONALE
  under which one derivation served two entries, carrying one error into
  both. A2 now requires each merge's values derived separately. **Say
  whether that was sufficient, and whether anything else about the
  batching cost verifiability;**
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**

    method      sequential dry-run merge onto the evidence base, then
                git rev-parse <rev>:<path> for each arriving artifact
    check type  GIT OBJECT IDENTITY

    CONFIRMED   merge 1 then merge 2, both --no-ff, no conflict
    CONFIRMED   combined base-to-head: 14 additions, 0 modifications
    CONFIRMED   the fourteen blob ids of A6 and A7, read from their
                branches
    CONFIRMED   merge-base(branch 1, branch 2) = 8701a97a…
    CONFIRMED   merge-base(evidence base, branch 1) = 8701a97a…
    CONFIRMED   merge-base(evidence base, branch 2) = 8701a97a…
    CONFIRMED   the evidence base is an ancestor of NEITHER branch

    RETRACTED   the first issue recorded "both branches share the
                merge-base 57c5a6eb…". That check was never run. The
                four lines above were measured with git merge-base and
                git merge-base --is-ancestor.
