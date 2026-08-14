# Task specification — integrate the `C-b` mechanisms, and land them

Specification evidence base: `f179b45eee359ef007da5e30833e9aed92069039`

    Branch to create   governance/integrate-mechanisms-cb
    Cut from           authoritative main @ f179b45e…
    Source             governance/mechanisms-cb
                       1c80e2f67c305b9f5b9656fefdbf0f7261bf34dc

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21, which bind this task prospectively.**

**This is the integration authorization AND the landing authorization.**
§6 carries the landing clause; **no second task is required.**

**One merge, measured clean.** Dry run from the evidence base: **no
conflict**, merge-base `f179b45e…`, **5 additions and 4 modifications at
the merge commit.** **Any conflict is an immediate STOP.**

---

## 0. What lands

**Two mechanisms, both with a measured failure behind them.**

    C1  one gate-heading grammar in a shared helper, called by
        task_checker.py and tests/test_repository_structure.py.
        The canonical language is the CONJUNCTION of the two
        expressions it replaces, and reads 14 of 14 real headings.
        RAW_GATE_HEADING stays outside the helper.

    C3  append_only and authorised_gates declared in the scope block
        of the specification a reviewer reads, with the specification's
        declaration taking precedence over config and disagreement
        stopping the run. Three distinguishable states:
        NOT_DECLARED, DECLARED_EMPTY, declared non-empty.

**`DECLARED_EMPTY` is not `PASS` and is not `NOT_APPLICABLE`.** It is a
valid declaration that leaves nothing to check, and it says so in the
JSON. **It does not make the run `INCOMPLETE`.**

**`DECLARATION_CONFLICT` is a new status word**, added rather than
overloading `NOT_PARSEABLE` — **overloading one state with a second
meaning is the defect `C3` exists to remove**, and the source task did
not reproduce it while repairing it.

## 1. What this does NOT establish

- **`P3` and `P7` remain `PARTIAL`, and the classification says why.**
  A specification still declares its own sets and can declare them
  wrongly. **What changed is that the declaration now sits inside the
  artifact a reviewer reads.**
- **`P3` does not verify that a declaration is complete**, and nothing
  in this merge makes it.
- **`C2` remains open.** **Nothing requires a newly issued specification
  to carry `stated:`, `append_only:` or `authorised_gates:`.** This merge
  makes the declarations possible and readable; **it does not make them
  mandatory**, and compliance still rests on an authoring habit.
- **The agreement between the two former grammars is now a single
  source rather than a coincidence** — but **the helper and its test were
  written by the same hand**, and nothing detects them drifting together.
- **`F1` and `F2` arrive unrepaired.**

## 2. The `A13` ruling

**Recorded verbatim as issued by the PI.**

> **PI RULING — `C-b` `A13`.** The statement that the reviewed `C-b`
> specification itself declared `append_only` and `authorised_gates` was
> **factually incorrect**. **Continuation under the specification's
> expressly defined config-only path is ratified**, because the executor
> neither altered the reviewed specification nor invented a new execution
> route. **`A13` is recorded as a specification defect; it is not
> retroactively deemed satisfied by the task's own manifest.** The `A7`
> fixtures constitute the evidence for declaration parsing and
> precedence. **No branch rebuild is required.**

**Measured, and this is what the ruling rests on.** The `C-b`
specification's scope block carries seven keys — `stated`, `base`,
`head`, `mode`, `add`, `modify`, `forbidden_operations` — **and neither
`append_only` nor `authorised_gates`.** The two appear only in §3(a)'s
definition and §4's fixture list.

**The consequence for this integration, stated so it is not overread.**
**`C-b` demonstrated declaration parsing and precedence through
fixtures.** **It did not demonstrate the end-to-end authoring path
`A13` claimed it would**, because the specification did not declare.
**This integration must not describe the authoring path as
demonstrated.**

**The deeper pattern, recorded and not repaired here.** This is a
narrower subtype of `C4`: **an acceptance criterion making an unchecked
factual assertion about the specification artifact itself.** A
pre-issue verification record checks literals against the repository;
**it does not check what the specification asserts about its own
bytes.** **Registering this belongs to `C-c`, whose list has grown
again.**

## 3. What this task must not do

- **Do not touch `main` until §6's landing.**
- **Do not modify any arriving file.**
- **Do not modify `GATES.md`.** Every mechanism landing here reads it.
- **Do not add `append_only` or `authorised_gates` to the `C-b`
  specification.** It is committed and reviewed; **its defect is
  recorded, not retouched.**
- **Do not build `C2`**, and **do not register anything** — `C-c` holds
  the register.
- **Do not describe `P3` or `P7` as no longer `PARTIAL`.**
- **Do not describe the declaration mechanism as demonstrated
  end-to-end.** §2 says why.
- **Do not write a superseded-register entry.**

## 4. Acceptance criteria

**A1 — Refs.** Read from the remote: `refs/heads/main` resolves to
`f179b45eee359ef007da5e30833e9aed92069039` and
`governance/mechanisms-cb` to
`1c80e2f67c305b9f5b9656fefdbf0f7261bf34dc`. **Any mismatch → STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **If blank or naming a different digest, STOP and say
which.** Report both digests equal.

**A3 — Merge parentage, three separately derived measurements.**

    parent 1 = this task's pre-execution review commit (commit 2)
    parent 2 = 1c80e2f67c305b9f5b9656fefdbf0f7261bf34dc
    merge-base(parent 1, parent 2)
             = f179b45eee359ef007da5e30833e9aed92069039

**Commit 1 MUST be an ancestor of parent 1**; verify and report that too.

**A4 — No conflict.** Report the merge's conflict list. **It must be
empty.** **Any conflict is a STOP.**

**A5 — Scope, frozen manifest. Final base-to-head scope: 6 additions and
4 modifications.**

    stated: 6 additions, 4 modifications
    append_only: DECISION_LOG.md
    authorised_gates: []
    base: f179b45eee359ef007da5e30833e9aed92069039
    head: <commit 4>
    mode: exact
    add:
      reports/2026-08-14T2212Z_mechanisms-cb.md
      reports/2026-08-XXT{HHMM}Z_integrate-mechanisms-cb.md
      reviews/chatgpt/2026-08-14T2212Z_mechanisms-cb.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-mechanisms-cb.md
      specs/2026-08-14T2212Z_mechanisms-cb.md
      specs/2026-08-XXT{HHMM}Z_integrate-mechanisms-cb.md
    modify:
      derivations/GOVERNANCE-ENFORCEMENT_classification.md
      scripts/governance_tools/task_checker.py
      tests/test_repository_structure.py
      tests/test_task_checker.py
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**This scope block declares `append_only` and `authorised_gates`, and
this time the declaration is real.** **`C-b`'s `A13` asserted the same of
its own specification and was wrong; §12 checks this one against the
committed bytes rather than asserting it.**

**Ten paths.** **Seven come from the source — three additions and four
modifications — and three are authored here, all additions.**

    source      3 additions + 4 modifications = 7
    this task   3 additions                   = 3
    total       6 additions + 4 modifications = 10

**An earlier draft of this sentence said "six from the source, three
added and three modified", which is wrong twice over and was caught by
the author's own pre-issue count.** **A6 requires the split re-derived
from the source branch rather than read from here.**

**At the merge commit, before the report exists, the count is 5 additions
and 4 modifications.** **Report which head each figure was measured at.**

**A6 — Source-branch paths, counted from the SOURCE and not from this
list.** **Derive the set of paths `1c80e2f6…` changes relative to
`f179b45e…` and report it.** **Expected: three additions and four
modifications, seven paths.** **Report a disagreement with A5's manifest
if one exists** — A5's prose sentence about the split is deliberately
left for this criterion to check rather than for a reader to trust.

**A7 — Which merge case this is, established BEFORE any blob comparison
is interpreted.** **Report the merge-base and whether `main` has touched
any of the four modified paths since `1c80e2f6…` was cut.**

**This determines what a blob comparison means, and the two cases are
opposite:**

    only one side changed a file    merged blob EQUALS the source side,
                                    and that is correct
    both sides changed a file       merged blob equals one side means a
                                    side was LOST

**Report which case applies to each of the four modified paths**, and
**then** report the blob comparison. **A blob comparison reported without
its case is uninterpretable**, and an earlier integration in this line
reported one that would have meant the opposite thing under different
circumstances.

**For paths in the one-sided case, require blob identity with the
source.** **For any path in the two-sided case, require the line-survival
measurement Amendment `P(b)` now mandates** — every line each side added
over the merge-base, present in the merged file, zero missing on either
side.

**A8 — The helper works at the merged head.** Call `gate_heading_ids` on
`GATES.md` at the merge commit and **report the count and the id list.**
**Expected fourteen, equal to the raw `^## P2-` count.** **Report both
numbers.** **Fewer than the raw count means `P7` returns
`NOT_PARSEABLE`, which is correct behaviour but a finding.**

**A9 — Both call sites use the helper.** Report that
`tests/test_repository_structure.py` imports it and carries no
gate-heading expression of its own, and that `RAW_GATE_HEADING` remains
separate. **Search the repository for stray gate-heading expressions and
report the search**, distinguishing **code** from **prose in specs and
reports** — the latter are historical records and are expected.

**A10 — The three declaration states at the merged head.** Report one run
for each: **no declaration**, **`[]`**, **non-empty.** **Report status and
JSON message for each**, and **confirm `DECLARED_EMPTY` is
distinguishable from `PASS` by a reader of the JSON alone.** **Report
whether `DECLARED_EMPTY` affects the exit status** — it must not.

**A11 — Protected paths.** Every path existing at the evidence base other
than the four in A5's `modify:` list is blob-identical at the head. **In
particular `GATES.md`, `CONVENTIONS.md`, `DECISION_LOG.md`,
`docs/BRANCHING_POLICY.md`, `tests/test_gate_pins.py` and everything
under `results/`.** Compare path by path and report the count.

**A12 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; **both pins match their targets.** **Report all four.**

**A13 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A14 — The checker over this task's own range**, base `f179b45e…`, head
**commit 3, the merge commit**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_integrate-mechanisms-cb.md

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**This task's own scope block declares the same two sets**, so **§3(b)'s
precedence rule applies to this run and the two must agree.** **They are
written to agree: `append_only: DECISION_LOG.md` and
`authorised_gates: []`.** **Report `declared_source` for each**, and
**report that no `DECLARATION_CONFLICT` arose.**

**This is the first task in which the mechanism governs its own run**,
and `C-b`'s `A13` claimed that of itself and was wrong. **Verify it here
against the committed bytes; do not assert it.**

**`P7` must report fourteen sections through the helper.** **`PASS` at
zero is a STOP.**

**RUN 2 is stop-governing; any failure is a STOP.** **Both configs and
both JSON outputs verbatim.** **Report the subject set RUN 1 actually
selected, as measured.**

**A14-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.** **If it fails, STOP before advancing `main`.**

**A15 — Validators, exit status 0.** Run `python -m pytest` from the
repository root. **Report pass and deselect counts before and after.**
**The count MUST rise from 310** — the source adds fixtures. **Report the
delta and what accounts for it.**

**A16 — Commit-message hygiene** on all four commits including the merge.
**Rule 20 binds this task**: an unpushed commit carrying a mechanically
detected hygiene violation may be amended, **and every affected check is
re-run, not only the failing one.** **Report both commit ids if that
happens.** **Commits 1–3 go in the report; commit 4 is post-report
evidence.**

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-mechanisms-cb.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-mechanisms-cb.md
    commit 3  --no-ff merge of 1c80e2f6…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-mechanisms-cb.md
    then      fast-forward refs/heads/main to commit 4, and push

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes the
merge**, per Rule 15's timing clause.

**Committed report — measured at commit 3:** A1–A13, A15 and A16 for
commits 1–3; **A14's two runs with both configs verbatim**; commit 1–3
SHAs and stored messages; commit 4's intended message; **A5's final scope
stated as INTENDED, with the measured 5/4 figure at commit 3.**

**Post-report evidence, NOT written back:** A5's final scope measured
base-to-commit-4; A14-final; A12 and A13 re-run after the advance; A16
for commit 4; the push; remote `main` read back; final ancestry
confirmation.

**Nothing in the committed report may claim to measure commit 4.**

## 6. The landing clause

**This task ends with authoritative `main` at its own final report
commit.** The target is named as **commit 4**, not as a SHA: any SHA
naming a commit that carries this task's review is unreachable as a
landing target, because Rule 15 places commits after it.

**The advance is a fast-forward. Verified available:** `f179b45e…` is the
base of this branch. **Verify `--is-ancestor` before the push and report
the exit status as a measurement.** **If a fast-forward is not available,
STOP.**

**Push without `--force` and without `--force-with-lease`.**

**`governance/mechanisms-cb` is not deleted and does not move.** Verify
and report its tip after the advance.

**Landing precondition specific to this merge.** **Do not advance `main`
unless A8 reports fourteen of fourteen and A15 reports a risen count.**
**A landing that carried the helper without the behaviour would put a
single source of truth on `main` that reads nothing**, and the suite
would not say so.

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** After this lands, one grammar reads the registry and
declarations sit in reviewed artifacts. **A reader may take that for the
declared-set problem being solved.** **`P3` and `P7` stay `PARTIAL`**,
because a specification still declares its own sets and can declare
wrongly. **Say where a reader meets that.**

**Second.** **`C-b` did not demonstrate the end-to-end authoring path**,
per §2. **This integration is the first task in which a specification's
own declaration governs its own run.** **Say whether it did**, and **do
not let this task's success be reported as `C-b`'s.**

**Third.** **The helper and its agreement test share an author.** **Say
what would detect them drifting together**, and **do not build it here.**

**This programme has met that regress before** — a guard written by the
hand that wrote the thing it guards. **That is a CONTEXTUAL statement,
not a count.** **Do not report a number of prior instances unless you
locate each one**, per Amendment M: a historical tally is a claim whose
scope must be checked like any other, and none has been.

**Naming the regress is not solving it.**

**Fourth.** **The suite count rises again.** **A larger green number is
what a reader mistakes for more coverage.** **Say what accounts for the
delta**, and **say that two mechanisms landing is not the enforcement gap
closing** — `C2` is open and the classification's count of objects with
no machine behind them is unchanged by this merge.

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Do not modify `GATES.md`, for any reason.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.** **They are written to agree; if they do not, that is
  a finding and a STOP.**
- **Do not claim `C-b`'s `A13` was satisfied.**
- No force-push, no history rewrite, no branch deletion **except as Rule
  20 permits**, and then per its terms.
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
- **A3's three values, separately derived**;
- **A5's two scope figures**, with the head each was measured at;
- **A6's source-derived path set**, and any disagreement with A5;
- **A7's per-path merge case, stated BEFORE the blob comparison**;
- **A8's two numbers and the id list**;
- **A9's search, code separated from prose**;
- **A10's three states, with the JSON message for each**;
- **A14's two runs**, both configs verbatim, `declared_source` for each
  declared set, the section count `P7` saw, and the measured RUN 1
  subject set;
- **A15's delta and what accounts for it**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, and the source tip unchanged;
- **§7's four Rule 16 junctions**;
- **whether integrating these mechanisms made you want to build `C2`.**
  **Say so, and confirm you did not**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.** **Every line was produced by running the stated method in
a clean clone.** **No measurement was taken through a truncated view, and
no statement below is clone-dependent.**

**This record now covers two kinds of claim: facts about the repository,
and facts this specification asserts about ITSELF.** **The second kind is
new, and it is here because `C-b`'s `A13` asserted something about its
own scope block that was false and that no verification record checked.**

    target      refs
    method      git fetch; git rev-parse against origin
    MEASURED    main = f179b45eee359ef007da5e30833e9aed92069039;
                governance/mechanisms-cb =
                1c80e2f67c305b9f5b9656fefdbf0f7261bf34dc; the source is
                NOT an ancestor of main.

    target      the merge
    method      dry run from f179b45e with two placeholder commits, then
                git merge --no-ff of the pinned ref
    MEASURED    CLEAN, no conflict; merge-base = f179b45e; 5 additions
                and 4 modifications at the merge commit; 6 and 4 with a
                placeholder report; f179b45e is an ancestor of that
                head, so the landing fast-forward is available.

    target      which merge case each modified path is in
    method      the merge-base equals main, so no commit exists on main
                since the source was cut
    MEASURED    all four modified paths are ONE-SIDED: only the source
                changed them. A6 requires this re-derived rather than
                taken from here.

    target      the helper at the merged head
    method      exec the helper's definitions from the merged
                task_checker.py and call gate_heading_ids on the merged
                GATES.md
    MEASURED    14 ids, against a raw '^## P2-' count of 14.

    target      the C-b specification's own scope block
    method      parse the committed specs/2026-08-14T2212Z_mechanisms-cb.md
                and list its scope keys
    MEASURED    stated, base, head, mode, add, modify,
                forbidden_operations. NEITHER append_only NOR
                authorised_gates. C-b's A13 was factually wrong about
                its own document, and §2 records the ruling.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations. BOTH declarations are
                present, and A14 checks them against the committed bytes
                rather than trusting this line.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                f179b45e and executed — not re-implemented
    MEASURED    one scope block; stated 6 additions, 4 modifications;
                the manifest lists six and four; parse OK, counted
                equals stated per category.
