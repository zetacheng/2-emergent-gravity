# Task specification — integrate the declared-total `P1` grammar, and land it

Specification evidence base: `e3ce80639337956af5f934f7530d3b2476e5f6c1`

    Branch to create   governance/integrate-p1-declared-total
    Cut from           authoritative main @ e3ce8063…
    Source             governance/p1-declared-total
                       8ff032e7f90ecfce4666fac34691b5670016bb75

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18.

**This is the integration authorization AND the landing authorization.**
§7 carries the landing clause; **no second task is required.**

**One merge, measured clean.** Dry run from the evidence base: **no
conflict**, merge-base `1cb5550f…`, **3 additions and 3 modifications
arriving.** **Any conflict is an immediate STOP.**

**The merge-base is NOT the evidence base.** The source was cut from
`1cb5550f…`, five landings ago. **That is a stale base, and it is
survivable here only because the merge was measured clean** — §1 records
what was and was not established by that measurement.

**The source task STOPPED.** Its `A10` was never discharged. §2 governs
what this integration may and may not do about that.

---

## 0. What lands

**A `P1` that reads a declared total instead of inferring one from
prose.**

    scope blocks gain a 'stated:' key; the count comes from there
    no sentence anywhere in the document is consulted
    a specification with no 'stated:' key is NOT_PARSEABLE
    a non-path token under add:/modify: is NOT_PARSEABLE

**Why it was built.** The landed grammar walked backwards from the scope
block for the nearest line carrying a count. **Measured over the
twenty-nine scope-bearing specifications present at the time: 10 PASS, 3
FAIL, 16 NOT_PARSEABLE** — the backward walk stopped at the first
markdown heading and never reached a count. **The repair replaces
inference with a declaration.**

## 1. The stale base, and what the clean merge does and does not establish

**The source branch was cut from `1cb5550f…`. `main` is now
`e3ce8063…`, five landings later**, and the intervening work included the
`P7` repair, which modifies the same file.

**Measured: the merge is clean, and `task_checker.py`,
`tests/test_task_checker.py` and the classification are all
AUTO-MERGED.**

**Measured at the merged head, and this is the part that matters:**

    GATE_HEADING present and parsing        14 of 14 raw headings
    RAW_GATE_HEADING present                yes
    parse_scope_block present               yes
    the declared-total grammar present      yes

**Both repairs survive the merge.** **That is a semantic check, not a
textual one, and it was run because a clean auto-merge does not establish
it.** **A previous specification in this line claimed order-independence
from a textual merge and withdrew it; this section does not repeat
that.**

**What is still NOT established here:** that the merged suite passes.
**A11 measures it.**

## 2. The source task's undischarged `A10`

**The source task stopped at its own `A10` and did not complete it.**
Its `RUN 2`, configured as its specification worded it, returned
`INCOMPLETE` at exit 2 with no property failed and `P1` passing — the
cause was `P3` and `P7` reporting `NOT_DECLARED`. **Its specification
forbade supplying empty declared sets to make the run green, and no
truthful non-empty set was available to it, so it stopped and did not
decide.**

**Both causes have since been addressed elsewhere.** `P3`'s declared set
is now named in every specification's config —
`["DECISION_LOG.md"]` — and `P7` was repaired and landed at
`e3ce8063…`.

**This integration MUST NOT claim to discharge that `A10`.** **A
criterion is discharged by the task that carries it, over that task's own
range, under its own review.** **The source task's report records a
STOP, and that record stands.**

**What this task does instead: it measures what would have happened.**
**A9 runs the repaired checker over THE EXACT RANGE GOVERNED BY THE
SOURCE TASK'S ORIGINAL `A10`** — base `1cb5550f…`, head
**`f02a7116…`, the source task's commit 4 and pre-report head** — **with
the config every specification now uses, and reports the result as
EVIDENCE, labelled as evidence.**

**The head is `f02a7116…`, not the branch tip.** The source task's `A10`
ran at its commit 4; `8ff032e7…` is its commit 5, the report, and the
range ending there is what its `A10-final` governed. **An earlier version
of this specification named the tip, which would have measured a
different criterion than the one that stopped** — and **§2's whole
argument is that a criterion is judged over its own range**, so getting
the range wrong here would undercut the principle it exists to protect.

**If that run passes, the correct statement is: "the source task's `A10`
would pass today under a config it was not given."** **Not: "`A10` is
discharged."** **The difference is the whole of §2, and a report that
blurs it fails this criterion.**

## 3. What this task must not do

- **Do not touch `main` until §7's landing.**
- **Do not modify any arriving file.**
- **Do not modify `GATES.md`.**
- **Do not claim the source task's `A10` is discharged**, in the report,
  the commit messages, or anywhere else.
- **Do not rebase the source branch onto the current `main`**, and do not
  re-cut it. **Its stale base is a fact of the record.**
- **Do not fix `F1`** — the harness's forbidden trailer — **or `F2`**,
  the `frozen Wilson D` docstring.
- **Do not unify the two gate-heading grammars.** They still coexist and
  still agree; **nothing keeps them agreeing**, and the unification
  belongs to the conventions task.
- **Do not add a `stated:` key to any existing specification.**
- **Do not write a superseded-register entry.** Nothing is superseded.

## 4. Acceptance criteria

**A1 — Refs.** Read from the remote: `refs/heads/main` resolves to
`e3ce80639337956af5f934f7530d3b2476e5f6c1` and
`governance/p1-declared-total` to
`8ff032e7f90ecfce4666fac34691b5670016bb75`. **Any mismatch → STOP.**
**Report the merge-base of the two and confirm it is `1cb5550f…`, not
the evidence base.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18, **carrying `reviewed specification SHA-256:` filled in.** **If blank
or naming a different digest, STOP and say which.** Report both digests
equal.

**A3 — Merge parentage, three separately derived measurements.**

    parent 1 = this task's pre-execution review commit (commit 2)
    parent 2 = 8ff032e7f90ecfce4666fac34691b5670016bb75
    merge-base(parent 1, parent 2)
             = 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**Commit 1 MUST be an ancestor of parent 1**; verify and report that too.
**Here the merge-base equals NEITHER parent NOR the evidence base**,
which is the shape a stale-base merge has. **Report all three values and
the evidence base as four distinct SHAs.**

**A4 — No conflict.** Report the merge's conflict list. **It must be
empty.** **Any conflict is a STOP.**

**A5 — Scope, frozen manifest. Final base-to-head scope: 6 additions and
3 modifications.**

    stated: 6 additions, 3 modifications
    base: e3ce80639337956af5f934f7530d3b2476e5f6c1
    head: <commit 4>
    mode: exact
    add:
      reports/2026-08-12T2015Z_p1-declared-total.md
      reports/2026-08-XXT{HHMM}Z_integrate-p1-declared-total.md
      reviews/chatgpt/2026-08-12T2015Z_p1-declared-total.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-p1-declared-total.md
      specs/2026-08-12T2015Z_p1-declared-total.md
      specs/2026-08-XXT{HHMM}Z_integrate-p1-declared-total.md
    modify:
      derivations/GOVERNANCE-ENFORCEMENT_classification.md
      scripts/governance_tools/task_checker.py
      tests/test_task_checker.py
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Nine paths. Six from the source branch — three added, three modified —
and three authored here.** **At the merge commit, before the report
exists, the count is 5 additions and 3 modifications.** **Report which
head each figure was measured at.**

**A6 — Source-branch artifacts intact.** **Six of the eight paths changed
base-to-merge-commit are contributed by `8ff032e7…`** — its three added
and three modified. **Derive that six from the source branch, not from
this list**, and **report a disagreement if the two differ.** Compare
those six at the merge commit against the source tip and require blob
identity for the three additions.

**The three MODIFIED paths will NOT be blob-identical to the source
tip**, because they were auto-merged with `P7`'s changes to the same
files. **Report each one's blob at the source tip, at `main`, and at the
merge commit, and confirm the merged blob differs from both** — that is
what an auto-merge of two real changes looks like, and **a merged blob
equal to either side would mean one side's change was lost.**

**A7 — Both repairs survive, measured at the merge commit.** Report:

    raw '^## P2-' count                     expected 14
    GATE_HEADING parsed count               expected 14
    equality holds                          expected true
    RAW_GATE_HEADING present                expected yes
    the declared-total grammar present      expected yes
    parse_scope_block reads 'stated:'       expected yes

**Both changes are in one file and both were auto-merged. This is the
criterion that establishes neither was lost.** **A missing one is a
STOP.**

**A8 — `P1` over the whole corpus at the merge commit.** Run the
integrated `P1` against **every `.md` file under `specs/`** and **report
the full table**: path, status, and the reason for each `NOT_PARSEABLE`.

**Measured at the evidence base: 48 specification files, of which 11
carry a `stated:` key.** **The source task's own record measured 1 of 38
when it was written** — **the corpus has changed under it**, because
every specification issued since then has carried the key.

**Expected at the merge commit: roughly a dozen `PASS` and the rest
`NOT_PARSEABLE`.** **Report what you actually measured, with the count of
each status.** **A `FAIL` anywhere is a finding and the file must be
named** — it would mean a document declares a total that disagrees with
its manifest.

**A9 — Evidence about the source task's `A10`, and NOT its discharge.**

**A9a, required.** Run the repaired checker over **the exact range
governed by the source task's original `A10`** — base `1cb5550f…`, head
**`f02a7116…`, its commit 4** — with:

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md
    specification_paths        ["specs/2026-08-12T2015Z_p1-declared-total.md"]

**A9b, also required.** Run the same checker with the same config over
base `1cb5550f…`, head **`8ff032e7…`, the branch tip** — the range the
source task's `A10-final` governed. **Report it separately.**

**Report both JSON outputs verbatim.** **Label both EVIDENCE.** **State,
in those words, that the source task's `A10` remains undischarged and
that neither run discharges it.** **A report that calls either a
discharge fails A9 regardless of what the runs returned.**

**Report whether A9a and A9b agree.** **If they differ, say how** — the
difference would be exactly the report commit, and it is the kind of
detail that makes a counterfactual either informative or misleading.

**For reference, the source task's commit chain, measured:**

    d9a8ba6b  commit 1  spec
    ec4de78e  commit 2  review
    bb59c4b1  commit 3  checker + tests
    f02a7116  commit 4  classification   ← A9a's head, A10's head
    8ff032e7  commit 5  report           ← A9b's head, A10-final's head

**A10 — The checker over THIS task's own range**, base `e3ce8063…`, head
**commit 3, the merge commit**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_integrate-p1-declared-total.md

**Config as in A9, less `specification_paths`, which RUN 2 sets as above
and RUN 1 omits.**

**`P7` must report fourteen sections.** **`PASS` at zero sections is a
STOP.** **`P1` must parse this specification's own `stated:` line** —
`6 additions, 3 modifications` against a nine-path manifest.

**RUN 2 is stop-governing; any failure is a STOP.** **Both configs and
both JSON outputs verbatim.** **Report the subject set RUN 1 actually
selected, as measured.**

**A10-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.** **If it fails, STOP before advancing `main`.**

**A11 — Validators, exit status 0.** Run `python -m pytest` from the
repository root at the merge commit and at commit 4. **Report pass and
deselect counts.** **The count MUST rise from 301**, because the source
adds fixtures to `tests/test_task_checker.py`. **Report the delta and
what accounts for it.** **A count that did not move would mean the
source's tests are not being collected after the auto-merge**, which is
the failure an auto-merge of two test files can produce silently.

**A12 — `GATES.md` untouched.** Blob-identical at the evidence base and
at the head — `2b3bd5069414f009e1a0466c4990db2949519bd8`. **Report
both.**

**A13 — Both pins match at the head**, and both unchanged from the
evidence base. **Report the pair for each and the count found.**

**A14 — Protected paths.** Every path existing at the evidence base other
than the three in A5's `modify:` list is blob-identical at the head.
Compare path by path and report the count.

**A15 — Gate invariants.** `^## P2-` count **14**; `P2-PHASE-01` reads
`Status: PROPOSED`; both prerequisites read `SATISFIED`; every `Status:`
line textually identical to the evidence base. **Report all four.**

**A16 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A17 — Commit-message hygiene** on all four commits including the merge.
**`F1` says your harness will try; report what happened per commit.**
**Commits 1–3 go in the report; commit 4 is post-report evidence.**

## 5. Landing preconditions specific to this merge

**Do not advance `main` unless A7 reports both repairs present and `P7`
parsing fourteen of fourteen, and A11 reports a risen suite count.**

**Two real changes to one file were auto-merged.** **A landing that
carried the text without the behaviour would leave `main` with a parser
that looks repaired twice over and is repaired once**, and the suite
would not say so.

## 6. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-p1-declared-total.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-p1-declared-total.md
    commit 3  --no-ff merge of 8ff032e7…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-p1-declared-total.md
    then      fast-forward refs/heads/main to commit 4, and push

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes the
merge**, per Rule 15's timing clause.

**Committed report — measured at commit 3:** A1–A9 and A11–A17 for
commits 1–3; **A10's two runs with both configs verbatim**; commit 1–3
SHAs and stored messages; commit 4's intended message; **A5's final scope
stated as INTENDED, with the measured 5/3 figure at commit 3.**

**Post-report evidence, NOT written back:** A5's final scope measured
base-to-commit-4; A10-final; A11 at commit 4; A13 and A16 re-run after
the advance; A17 for commit 4; the push; remote `main` read back; final
ancestry confirmation.

**Nothing in the committed report may claim to measure commit 4.**

## 7. The landing clause

**This task ends with authoritative `main` at its own final report
commit.** The target is named as **commit 4**, not as a SHA: any SHA
naming a commit that carries this task's review is unreachable as a
landing target, because Rule 15 places commits after it.

**The advance is a fast-forward. Verified available:** `e3ce8063…` is the
base of this branch. **Verify `--is-ancestor` before the push and report
the exit status as a measurement.** **If a fast-forward is not available,
STOP.**

**Push without `--force` and without `--force-with-lease`.**

**`governance/p1-declared-total` is not deleted and does not move.**
Verify and report its tip after the advance.

## 8. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** After this lands, the three checks this line set out to repair
are all on `main`. **A reader may take that for the enforcement gap being
closed.** **The classification still records twenty-two of twenty-nine
objects with no machine behind them**, and **`P1`, `P3` and `P7` all
remain `PARTIAL`.** **Three checks now work. That is the claim.**

**Second.** **`P1`'s coverage will look like it grew.** Eleven of
forty-eight specifications now declare a total, against one of
thirty-eight when the repair was written. **That is not the repair
working better; it is the corpus having been written to suit it**,
because every specification issued since carries the key. **Say which
it is.**

**Third.** **The source task's `A10` is undischarged and stays that
way.** **Say so, and say that A9's run is evidence about a
counterfactual, not a discharge.**

**Fourth.** **The two gate-heading grammars still coexist and still
agree.** **Nothing keeps them agreeing.** **Report that they still agree
at the head, and that the agreement is measured rather than enforced.**

## 9. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed, and
  the three auto-merged files are integrated as `git` merged them** —
  **do not hand-edit a merge result.**
- **If the auto-merge produced anything you would want to adjust, STOP
  and report it.** **Adjusting it is authoring content during an
  integration.**
- **Do not adjust the config to make RUN 2 pass.**
- **Do not describe A9 as a discharge.**
- No force-push, no history rewrite, no branch deletion.
- Merge commit only for the integration: no fast-forward there, no
  squash, no rebase. **The landing is a fast-forward or a stop.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 10. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A3's four distinct SHAs** — three parentage values and the evidence
  base;
- **A5's two scope figures**, with the head each was measured at;
- **A6's six source comparisons**, and **the three-way blob report for
  each auto-merged file**, confirming the merged blob differs from both
  sides;
- **A7's six measurements**;
- **A8's full corpus table** with the count of each status;
- **A9a's and A9b's JSON verbatim, both labelled EVIDENCE**, whether
  they agree, and **the sentence stating that `A10` remains
  undischarged**;
- **A10's two runs**, both configs verbatim, the section count `P7` saw,
  and the measured RUN 1 subject set;
- **A11's counts and delta**, and what accounts for it;
- **A12 through A17 as specified**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, and the source tip unchanged;
- **§8's four Rule 16 junctions**;
- **whether `main` now reads as though the enforcement gap were
  closed.** It is not;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 11. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**
**Every line was produced by running the stated method in a clean
clone.** **No measurement was taken through a truncated view, and no
statement below is clone-dependent.**

    target      refs and the merge-base
    method      git fetch; git rev-parse; git merge-base
    MEASURED    main = e3ce80639337956af5f934f7530d3b2476e5f6c1;
                governance/p1-declared-total =
                8ff032e7f90ecfce4666fac34691b5670016bb75;
                merge-base = 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab,
                which is FIVE landings behind the evidence base. The
                source is NOT an ancestor of main.

    target      the merge
    method      dry run from e3ce8063 with two placeholder commits,
                then git merge --no-ff of the pinned ref
    MEASURED    CLEAN. task_checker.py, tests/test_task_checker.py and
                the classification were AUTO-MERGED. Arriving: 3
                additions and 3 modifications; with the placeholders and
                a placeholder report, 6 additions and 3 modifications.
                e3ce8063 is an ancestor of that head, so the landing
                fast-forward is available.

    target      whether both repairs survive the auto-merge
    method      read task_checker.py in the dry-run tree and apply its
                GATE_HEADING to GATES.md there
    MEASURED    GATE_HEADING present, parsing 14 of 14 raw headings;
                RAW_GATE_HEADING present; parse_scope_block present;
                the declared-total grammar present. BOTH REPAIRS
                SURVIVE.
    SCOPE       this is a presence-and-parse check on the merged file.
                It does not establish that the merged suite passes; A11
                measures that.

    target      the corpus P1 will face
    method      count .md files under specs/ at e3ce8063, and count
                those carrying a 'stated:' line
    MEASURED    48 specification files; 11 carry the key. The source
                task's own record measured 1 of 38. The corpus changed
                under the repair, because every specification issued
                since has carried it.

    target      GATES.md across the merge
    method      git rev-parse <rev>:GATES.md
    MEASURED    2b3bd5069414f009e1a0466c4990db2949519bd8 at the evidence
                base and in the dry-run tree. The source modifies no
                gate.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                e3ce8063 and executed — not re-implemented
    MEASURED    one scope block; stated 6 additions, 3 modifications;
                the manifest lists six and three; parse OK, counted
                equals stated.
