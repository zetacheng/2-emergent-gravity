# Task specification — re-issue the PI decisions and deferred-items task on a clean branch

Specification evidence base: `f309f61c9c14b0e2c63e078f9c0d0809422742e7`

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**This re-issues a task whose first two executions are both preserved
and neither integrated.** Its content has been reviewed and approved;
what was not approved was how the second execution was represented.

---

## 0. Why this specification exists

**The content is not in dispute.** The three PI decisions and the
deferred-items register were reviewed and approved. Two problems in the
first issue were corrected — the evidence for `DEFERRED-02` was pinned
to the artifacts that actually carry it, and the negative-mass branch's
description was narrowed from "stable" to positive restricted curvature.
**Both corrections stand.**

**What was not approved was the re-issue mechanism.** The corrected
specification named the same branch, the same task and the same paths as
the first, and still instructed *create the branch from that commit* — an
instruction that cannot be executed against a branch that already
exists. The executor identified the conflict and, having no guidance,
resolved it by overwriting the first execution's records on the same
branch.

**Two diffs describe the resulting branch:**

    evidence base -> head     no deletions
    first -> second issue     35/13, 31/18, 422/344, 57/14

**The evidence-base-to-head diff satisfied the stated final-state
criterion. The first-to-second-issue diff exposes the history mutation
that criterion did not measure.** The measurement was not wrong; it was
used to establish a property it does not measure. A pushed `DECISION_LOG.md` entry was replaced by a later
commit; that the old commit survives in Git history does not make the
branch's operative log append-only.

**The fault is the specification's.** The executor's instructions say to
stop on inconsistency, and it should have. **But it had nothing to
follow, because the re-issued specification did not say how a second
execution should be represented.** That gap is now a governance
amendment; this task is its first application.

**Nothing is rewritten, reset, or force-pushed.** **There is ONE
superseded branch, not two**: `fix/pi-decisions-and-deferred` at
`52f65117…`, with the first execution `59c763ab…` reachable as its
ancestor. The branch is preserved unchanged and **both execution
histories remain reachable** as evidence of what was attempted.

## 1. What to do

**Create a NEW branch from the evidence base**, under a new name and new
paths, and land the approved content there.

    superseded, preserved, not carried forward — ONE branch:
      fix/pi-decisions-and-deferred @ 52f651174dc1fef03b4fb9276078fa1f08d94bd7
      first execution 59c763abcfd406bf6757859825c17bff4e4a0c25 is an
      ANCESTOR of that head, not a separate branch, and remains
      reachable

    this task:
      fix/pi-decisions-v2   cut from f309f61c…

**The approved content is the content of `52f65117…`**, whose four
files were reviewed and accepted. **Reproduce that content**; do not
re-derive it, and do not re-open the wording that review settled.

**But re-verify it rather than transcribing it blind.** Confirm each of
A2's evidence quotations independently against the pinned material, and
run the A4 literal check yourself. **A re-issue that copies an approved
artifact without re-checking it inherits any error the approval
missed.**

## 2. Acceptance criteria

**A0 — Commit order and paths, frozen.**

    commit 1  specs/2026-08-09T{HHMM}Z_pi-decisions-v2.md
    commit 2  DECISION_LOG.md, derivations/P2-DEFERRED-ITEMS.md
    commit 3  reports/2026-08-09T{HHMM}Z_pi-decisions-v2.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused. **You choose
no path.** **The `{HHMM}` token MUST differ from `0430`**, which the
superseded branch used — reusing it would make the two executions
indistinguishable by path.

**A1 — Pinned inputs**, verified before use; any mismatch is a STOP:

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a

    derivations/P2-PHASE-01_channel_character.md
    380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f

    derivations/P2-PHASE-01_channel_character_layers.md
    4cea53a7163ccc6aadadd0fca276714c16d805ad8aed3594d64d66d412606711

    results/P2-PHASE-01/channel-character-layers/layers.json
    fe343c74389cc996e42567d7dd510f479f1e7ed01cba81de61ff1d6f7e9d1542

    reports/2026-08-05_p2-phase-01_scalar-stationary-exploratory.md
    70ab88eda32483420c0bfd522babd2ca4a73941bc2d2d20f8414976641756cbe

    results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json
    a4537efad3b46e5e429b5310baad8b4dbf36d9c95582873dbfa0b03cc44d7028

    derivations/P2-PHASE-01_scalar_stationary_exploratory.md
    80586e33ef07e307729af4597f72b48f6ecee74fc6a0f396b593f735ef322599

**`DEFERRED-02`'s evidence is split across these three, and the split
matters:**

    the report and results artifact   supply the roots, the curvatures,
                                      and the tested complement relation
    the exploratory derivation note   supplies the SCOPE LIMITATION on
                                      that curvature — "Neither curvature
                                      is a full condensate-space Hessian
                                      or a phase-admissibility
                                      statement" — which is what narrowed
                                      Decision 3 from "stable" to
                                      positive restricted curvature

**The note is a pre-registration and does not contain the numerical
findings**; it was wrongly dropped from a previous issue's pinned set
when the other two were added, **leaving the assertion about its content
unverifiable from A1.**

**A2 — Evidence re-verified, not inherited.** For `DEFERRED-01` and
`DEFERRED-02`, locate each `Evidence:` statement in the pinned material
and quote it. **If either is not there, STOP.**

**For `DEFERRED-03`, verify instead that the entry states
`Evidence: none` and supplies no citation. The absence of evidence is
intentional content there, not a failed lookup.**

**A3 — Content reproduced from the superseded branch.** The three
`DECISION_LOG.md` entries and `derivations/P2-DEFERRED-ITEMS.md` carry
the substance of `52f65117…`. **Report any place where you judged a
change necessary, and why** — the expectation is none, and a silent
difference between an approved artifact and its re-issue is a defect.

**A4 — Required phrases present**, checked against NORMALISED text:
strip blockquote prefixes (`> `), strip `**` and backticks, collapse
whitespace. **Keep en dashes.**

    entry 1   scalar channel with a real auxiliary field
              This is a choice of direct route
              It is deferred, not excluded
              This does not close OPEN-AC-1
    entry 2   the programme evaluates both the
              rather than selecting between them
              depends on an unresolved sign convention
    entry 3   DEFERRED, not excluded
              they do not establish full condensate-space stability,
                phase admissibility, or absence of physical content
              cannot by itself classify this branch as an unphysical
                lattice artifact
              that criterion's quantifier range is undetermined

**A phrase may appear in the entry's surrounding prose where the
verbatim ruling does not contain it. Do not edit a ruling to make a
check pass.**

**A5 — `DECISION_LOG.md` append-only, on BOTH measures.**

    evidence base -> branch head    zero deleted lines
    each commit -> its parent       zero deleted lines

**Report both.** The second is the one the superseded branch failed, and
**satisfying only the first is what this re-issue exists to correct.**

**A6 — Nothing else touched.** `GATES.md`, `CONVENTIONS.md`,
`AGENTS.md`, `pyproject.toml`, every path under `scripts/`, `results/`
and `tests/`, and **every path under `derivations/` that exists at the
evidence base**: blob-identical to the evidence base.
`P2-DEFERRED-ITEMS.md` does not exist there and is added by A7. **`P2-PHASE-01` remains
`PROPOSED`; `P2-GAP-01` remains `PASS`.**

**A7 — Scope**, three additions and one modification:

    add:
      specs/2026-08-09T{HHMM}Z_pi-decisions-v2.md
      derivations/P2-DEFERRED-ITEMS.md
      reports/2026-08-09T{HHMM}Z_pi-decisions-v2.md
    modify:
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 3 additions and 1 modification.**

**A8 — The superseded branch untouched.** After the push, verify from
the remote that `fix/pi-decisions-and-deferred` still resolves to
`52f651174dc1fef03b4fb9276078fa1f08d94bd7`, and that
`59c763abcfd406bf6757859825c17bff4e4a0c25` **remains reachable as its
ancestor.** **Delete no branch, and do not force-push anything.**

**A9 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`. **A9-pre** at the pre-report head goes
in the report; **A9-final** at the pushed head is post-report evidence.

**A10 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to
`f309f61c9c14b0e2c63e078f9c0d0809422742e7`; **create the new branch from
that commit — it does not yet exist, and this instruction is executable
here.** Move no `main` ref. **Local `main` is stale by design.** Report
all three. Push the task branch only.

## 3. Evidence layering

**Committed report:** A1–A8, A9-pre, the earlier commit SHAs and
messages, the pre-report head, the intended final manifest, and the
intended report commit message with its authoring-time trailer
suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A9-final, the push, the report
commit's stored message read back from the object, and ancestry
confirmation.

## 4. Invariants and prohibitions

- Executor-writable: the four paths of A7 only.
- **Do not touch, reset, rewrite, or delete the superseded branch.** It
  is evidence of what was attempted.
- **Do not reuse the `0430` token.**
- **Decide nothing.** The decisions are the PI's; record them.
- **Do not compute anything**, and do not perform the diquark
  calculation Decision 2 authorizes.
- **Do not add the SI-1 cross-reference** — `GATES.md` is protected and
  that is an agreed separate task.
- Commit-message hygiene: inspect the proposed message before each
  commit and the stored message after; permit no `Co-Authored-By`, no
  session identifier or URL, no tool attribution. **Report per commit
  whether any trailer was suppressed and which.**
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: `fix/pi-decisions-v2`.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.
  **This specification exists because that instruction was met and could
  not be followed; if it happens again, stop and say what is missing.**

## 5. Report contract

- raw output for A1–A9, scope-checker JSON verbatim including
  `observed_operations`;
- the evidence quotations for `DEFERRED-01` and `DEFERRED-02`, with
  their source paths;
- the A4 literal check results;
- **both append-only measures of A5**, stated separately;
- **any difference between what you landed and `52f65117…`'s content**,
  with your reason — the expectation is none;
- **confirmation that the superseded branch remains at `52f65117…`, and
  that the first execution commit `59c763ab…` remains reachable as its
  ancestor** — there is one branch, not two;
- **whether this specification told you how to represent a re-issue
  clearly enough that no judgement was required.** The previous issue
  did not, and the executor had to invent a semantics. **If this one is
  still unclear anywhere, that matters more than a clean report**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
