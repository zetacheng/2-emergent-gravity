# Task specification — integrate the `C-a` conventions consolidation, and land it

Specification evidence base: `bec0117168144d54fb23338b673cf7a7e4771868`

    Branch to create   governance/integrate-conventions-ca
    Cut from           authoritative main @ bec01171…
    Source             governance/conventions-consolidation-ca
                       8de19fec0dd7e4ba52c2417f0dfe3fab84ae7ef6

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18.

**This is the integration authorization AND the landing authorization.**
§6 carries the landing clause; **no second task is required.**

**One merge, measured clean.** Dry run from the evidence base: **no
conflict**, merge-base `bec01171…`, **5 additions and 1 modification at
the merge commit.** **Any conflict is an immediate STOP.**

**`CONVENTIONS.md` is the only pre-existing file that changes**, and it
changes by addition only. **No gate, no pin, no script, no test.**

---

## 0. What lands

**Seven consolidated principles covering thirteen source items**, and a
non-binding record that makes the coverage countable.

    Amendment M -> Rule 7    A4 A5 A6 A8   the scope of a recorded
                                           measurement
    Amendment N -> Rule 18   A2 A3         supply as a file, bind by
                                           digest
    Amendment O -> Rule 12   A1 A7         machine-readable declarations,
                                           complete reading lists
    Amendment P -> Rule 5    B1 B3         landing outcome inline, line
                                           survival
    Rule 19                  B2            pinned-artifact integrity
    Rule 20                  B4            permitted pre-push hygiene
                                           repair
    Rule 21                  E2            artifact-state / statement-kind
                                           namespaces

**Rules 18 → 21 contiguous. Amendments A–L → A–P, and no `J`.**

## 1. What this does NOT establish, and the sentence that must appear

**The prose contract is consolidated; most enforcement remains
outstanding.**

**Five of the seven principles carry `MECHANISM DEFERRED`.** **A rule so
marked prevents nothing by itself** — it records what should happen and
relies on an author remembering. **The deferred count is the size of what
`C-b` and `C-c` still owe.**

**Do not describe this merge as closing the governance gap.** **It
converts hidden enforcement debt into countable enforcement debt**, which
is progress of a different kind and must be reported as the kind it is.

**Two deferred obligations are registered nowhere**: Amendment `N(b)`'s
review-digest comparison and Amendment `P(b)`'s line-survival check.
**Both are fully specifiable inside the repository.** **`C-c`'s debt set
has grown and this task does not register them** — §2 forbids it.

## 2. Two PI rulings this integration rests on

**Recorded verbatim. Neither is this task's to interpret.**

**On the placement of the consolidation record:**

> **PI RULING.** §4's amendment / new-numbered-rule dichotomy applies to
> binding governance principles, and does not apply to material expressly
> marked non-binding — traceability, provenance or consolidation records.
> **`## Consolidation record — C-a` may remain, provided that section
> creates, modifies or explains no new obligation and only records what
> the formal rules and amendments already carry.**

**On the one sentence that tested that condition:**

> **PI RULING.** The record's sentence explaining what `MECHANISM
> DEFERRED` means is acceptable, **because a marker is an annotation and
> not a requirement.**

**Measured, and this is what the first ruling's condition was checked
against:** the section runs 57 lines; `MUST`, `SHALL` and `binds` occur
**once between them**, in the sentence *"Nothing here binds"*. **All seven
mechanism markers are attached to the amendments and rules themselves,
not to the record.**

**Consequence for this task: the record is integrated as it stands.**
**Do not edit it, do not move it, and do not extend it.**

## 3. What this task must not do

- **Do not touch `main` until §6's landing.**
- **Do not modify any arriving text**, including the consolidation
  record.
- **Do not register `N(b)`, `P(b)`, or the marker-vocabulary gap.**
  **`C-c` does that**, and its list has grown.
- **Do not write any code, test or checker property.** **`C-b` does
  that.**
- **Do not rule on `E1`**, which remains the PI's.
- **Do not modify `GATES.md`**, and **do not touch anything under
  `scripts/`, `tests/`, `results/` or `derivations/`.**
- **Do not describe the governance gap as closed.**
- **Do not write a superseded-register entry.** Nothing is superseded.

## 4. Acceptance criteria

**A1 — Refs.** Read from the remote: `refs/heads/main` resolves to
`bec0117168144d54fb23338b673cf7a7e4771868` and
`governance/conventions-consolidation-ca` to
`8de19fec0dd7e4ba52c2417f0dfe3fab84ae7ef6`. **Any mismatch → STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18, **carrying `reviewed specification SHA-256:` filled in.** **If blank
or naming a different digest, STOP and say which.** Report both digests
equal.

**Note the timing.** **Amendment `N` lands in this merge and binds
prospectively from it.** **It does not govern this task's own review**,
which was written before it existed. **Report which rules governed this
task and which land in it**, so the distinction is on the record rather
than inferred.

**A3 — Merge parentage, three separately derived measurements.**

    parent 1 = this task's pre-execution review commit (commit 2)
    parent 2 = 8de19fec0dd7e4ba52c2417f0dfe3fab84ae7ef6
    merge-base(parent 1, parent 2)
             = bec0117168144d54fb23338b673cf7a7e4771868

**Commit 1 MUST be an ancestor of parent 1**; verify and report that too.

**A4 — No conflict.** Report the merge's conflict list. **It must be
empty.** **Any conflict is a STOP.**

**A5 — Scope, frozen manifest. Final base-to-head scope: 6 additions and
1 modification.**

    stated: 6 additions, 1 modification
    base: bec0117168144d54fb23338b673cf7a7e4771868
    head: <commit 4>
    mode: exact
    add:
      reports/2026-08-14T1241Z_conventions-consolidation-ca.md
      reports/2026-08-XXT{HHMM}Z_integrate-conventions-ca.md
      reviews/chatgpt/2026-08-14T1241Z_conventions-consolidation-ca.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-conventions-ca.md
      specs/2026-08-14T1241Z_conventions-consolidation-ca.md
      specs/2026-08-XXT{HHMM}Z_integrate-conventions-ca.md
    modify:
      CONVENTIONS.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths. Four from the source — three added and one modified — and
three authored here.** **At the merge commit, before the report exists,
the count is 5 additions and 1 modification.** **Report which head each
figure was measured at.**

**A6 — Source-branch artifacts intact.** **Four of the six paths changed
base-to-merge-commit are contributed by `8de19fec…`.** **Derive that four
from the source branch, not from this list**, and report a disagreement
if they differ. **All four must be blob-identical to the source tip**,
including `CONVENTIONS.md` — **this merge auto-merges nothing, because
`main` has not touched that file since the source was cut.** **Verify
that rather than assume it.**

**A7 — `CONVENTIONS.md` grows by addition only, verified two ways.**

**(i) Zero deleted lines** base to head. Report the count.

**(ii) The base file is an exact IN-ORDER SUBSEQUENCE of the merged
file.** Report the matched count and the base line count. **Expected
1023 of 1023.**

**(ii) is an INDEPENDENT preservation check, and that is its value.** It
establishes directly that every base line survives in its original order
in the merged file, **rather than inferring preservation solely from
`git`'s line-diff accounting.**

**An earlier version of this criterion justified (ii) by claiming that
zero deletions permits a line being rewritten and an identical line added
back elsewhere. That is false.** **A rewritten line appears in a line
diff as a deletion and an addition**, so (i) already excludes rewriting
under the stated measurement. **(ii) is not stronger by covering a case
(i) misses; it is stronger by not depending on the same instrument.**

**Both are required.** **This test was performed by the source task's
executor beyond its criterion, and is required here because two
independent measurements of one property are worth more than one.**

**A8 — Rule and amendment counts at the head.** **Twenty-one numbered
rules, contiguous 1 through 21.** **Fifteen amendment letters: A–I, K–P.**
**No `J`.** **Report both lists**, and **confirm the eighteen pre-existing
rules and eleven pre-existing amendments are all still present.**

**A9 — Markers, counted per principle and not by string.** **Report the
marker attached to each of the seven principles**, and the totals.
**Expected: 1 `EXISTS`, 5 `DEFERRED`, 1 `RULE-ONLY`.**

**Count by bounding each principle's text, not by grepping the file** —
**a whole-file grep returns twelve hits, because the consolidation record
restates them and one line explains the vocabulary.** **The
specification author made exactly that error when verifying this branch,
and reports twelve where the answer is seven.**

**A10 — The consolidation record is unchanged and still non-binding.**
Report that `## Consolidation record — C-a` is byte-identical to the
source, and report the count of lines in it containing `MUST`, `SHALL`
or `binds`. **Expected: one, the sentence saying nothing here binds.**

**A11 — The thirteen-row matrix is intact.** Report the row count and
confirm each of `A1`–`A8`, `B1`–`B4` and `E2` appears exactly once.

**A12 — Protected paths.** Every path existing at the evidence base other
than `CONVENTIONS.md` is blob-identical at the head. **In particular
`GATES.md`, `DECISION_LOG.md`, `docs/BRANCHING_POLICY.md`, and everything
under `scripts/`, `tests/`, `results/` and `derivations/`.** Compare path
by path and report the count.

**A13 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; **both pins match their targets**. **Report all four.**
**`CONVENTIONS.md` is referenced thirteen times in `GATES.md` and is
pinned by neither pin** — **verify and report that**, because a task
modifying a pinned file would owe a re-pin under the Rule 19 this merge
lands, and this one must establish that it does not.

**A14 — The checker over this task's own range**, base `bec01171…`, head
**commit 3, the merge commit**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_integrate-conventions-ca.md

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**`P7` must report fourteen sections.** **`PASS` at zero is a STOP.**

**RUN 2 is stop-governing; any failure is a STOP.** **Both configs and
both JSON outputs verbatim.** **Report the subject set RUN 1 actually
selected, as measured.**

**A14-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.** **If it fails, STOP before advancing `main`.**

**A15 — Validators, exit status 0.** Run `python -m pytest` from the
repository root. **Report pass and deselect counts before and after.**
**Expected: unchanged at 310 passed, 2 deselected** — this merge adds no
test. **A change is a finding and must be explained.**

**A16 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A17 — Commit-message hygiene** on all four commits including the merge.
**`F1` says your harness will try; report what happened per commit.**
**Commits 1–3 go in the report; commit 4 is post-report evidence.**

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-conventions-ca.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-conventions-ca.md
    commit 3  --no-ff merge of 8de19fec…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-conventions-ca.md
    then      fast-forward refs/heads/main to commit 4, and push

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes the
merge**, per Rule 15's timing clause.

**Committed report — measured at commit 3:** A1–A13 and A15–A17 for
commits 1–3; **A14's two runs with both configs verbatim**; commit 1–3
SHAs and stored messages; commit 4's intended message; **A5's final scope
stated as INTENDED, with the measured 5/1 figure at commit 3.**

**Post-report evidence, NOT written back:** A5's final scope measured
base-to-commit-4; A14-final; A13 and A16 re-run after the advance; A17
for commit 4; the push; remote `main` read back; final ancestry
confirmation.

**Nothing in the committed report may claim to measure commit 4.**

## 6. The landing clause

**This task ends with authoritative `main` at its own final report
commit.** The target is named as **commit 4**, not as a SHA: any SHA
naming a commit that carries this task's review is unreachable as a
landing target, because Rule 15 places commits after it.

**The advance is a fast-forward. Verified available:** `bec01171…` is the
base of this branch. **Verify `--is-ancestor` before the push and report
the exit status as a measurement.** **If a fast-forward is not available,
STOP.**

**Push without `--force` and without `--force-with-lease`.**

**`governance/conventions-consolidation-ca` is not deleted and does not
move.** Verify and report its tip after the advance.

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Three junctions, all three required in the report.**

**First.** `main` will carry twenty-one rules where it carried eighteen,
covering twelve failures that previously had none. **A reader may take
that for the failures being prevented.** **Five of seven principles are
`MECHANISM DEFERRED` and prevent nothing by themselves.** **Report the
marker totals beside the rule count**, and **say that the prose contract
is consolidated while most enforcement remains outstanding.**

**Second.** **Writing a rule is not detecting a violation.** Every one of
the twelve failures was identified, interpreted or repaired through human
review or re-measurement — **though some underlying violations were
mechanically caught**, `B4`'s commit-hygiene violation among them.
**Landing the rules changes neither fact.**

**Third.** **The rule set covers what was noticed and is silent about
what was not.** The classification behind it is a list assembled across
one working session, several of whose items were found only because a
later task tripped over them. **The absence of a rule is not evidence
that the corresponding failure cannot occur.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Do not edit `CONVENTIONS.md` in any way.** It arrives from the source
  and this task adds nothing to it.
- **Do not adjust the config to make RUN 2 pass.**
- **Do not claim the rules landing here govern this task.** They bind
  prospectively from the landing.
- No force-push, no history rewrite, no branch deletion.
- Merge commit only for the integration: no fast-forward there, no
  squash, no rebase. **The landing is a fast-forward or a stop.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §5 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A2's statement of which rules governed this task and which land in
  it**;
- **A3's three values, separately derived**;
- **A5's two scope figures**, with the head each was measured at;
- **A6's four source comparisons**, and confirmation that nothing was
  auto-merged;
- **A7's two verifications**, the deleted-line count and the subsequence
  match, **with the subsequence named as the INDEPENDENT check rather
  than as one covering a case the deleted-line count misses**;
- **A8's two lists and the confirmation of pre-existing survival**;
- **A9's per-principle markers and totals**, and **the note that a
  whole-file grep gives twelve**;
- **A10's byte-identity and the one-line count**;
- **A11's thirteen rows**;
- **A12's path count**;
- **A13's four invariants plus the not-pinned verification**;
- **A14's two runs**, both configs verbatim, the section count `P7` saw,
  and the measured RUN 1 subject set;
- **A15's counts**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, and the source tip unchanged;
- **§7's three Rule 16 junctions**;
- **whether `main` now reads as though the governance gap were closed.**
  It is not;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**
**Every line was produced by running the stated method in a clean
clone.** **No measurement was taken through a truncated view, and no
statement below is clone-dependent.**

    target      refs
    method      git fetch; git rev-parse against origin
    MEASURED    main = bec0117168144d54fb23338b673cf7a7e4771868;
                governance/conventions-consolidation-ca =
                8de19fec0dd7e4ba52c2417f0dfe3fab84ae7ef6; the source is
                NOT an ancestor of main; 4 commits ahead, 0 behind.

    target      the merge
    method      dry run from bec01171 with two placeholder commits, then
                git merge --no-ff of the pinned ref
    MEASURED    CLEAN, no conflict; merge-base = bec01171; 5 additions
                and 1 modification at the merge commit; 6 and 1 with a
                placeholder report; bec01171 is an ancestor of that
                head, so the landing fast-forward is available.

    target      CONVENTIONS.md across the merge
    method      git diff --numstat; and an in-order subsequence test of
                the base file's lines against the merged file's
    MEASURED    382 lines added, ZERO deleted, four hunks all pure
                additions. The base file is an exact in-order
                subsequence: 1023 of 1023 lines matched.
    NOTE        the two agree, as they must: a rewritten line would show
                in the line diff as a deletion. The subsequence test is
                valuable because it does not rely on git's diff
                accounting, not because it covers a case the deletion
                count misses.
    MEASURED    at the merged head: 21 numbered rules; 15 amendment
                letters; no J.

    target      the mechanism markers
    method      bound each principle's text and count within it;
                separately, grep the whole file
    MEASURED    per principle: 1 EXISTS, 5 DEFERRED, 1 RULE-ONLY.
                Whole-file grep returns TWELVE, because the
                consolidation record restates them and one line explains
                the vocabulary.
    RETRACTED   the specification author first reported the whole-file
                figure as though it were the per-principle one, and the
                executor's 1/5/1 is correct. That is the same
                vocabulary-hit error the author made once before, on the
                governance classification's kind labels.

    target      the consolidation record against the PI's condition
    method      read the section in full and count binding vocabulary
    MEASURED    57 lines; MUST, SHALL and binds occur ONCE between them,
                in "Nothing here binds". All seven markers are attached
                to the amendments and rules themselves. The only
                sentence explaining the marker vocabulary is inside the
                record, at line 1387, and the PI has ruled it acceptable
                because a marker is an annotation and not a requirement.

    target      whether CONVENTIONS.md is pinned
    method      grep 'sha256 `[0-9a-f]{64}`' over GATES.md and read the
                path above each
    MEASURED    TWO pins, naming the adopted parameter-domain artifact
                and the adopted admissibility contract. NEITHER names
                CONVENTIONS.md. No re-pin is owed, and A13 requires that
                verified rather than assumed.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                bec01171 and executed — not re-implemented
    MEASURED    one scope block; stated 6 additions, 1 modification;
                the manifest lists six and one; parse OK, counted
                equals stated per category.
