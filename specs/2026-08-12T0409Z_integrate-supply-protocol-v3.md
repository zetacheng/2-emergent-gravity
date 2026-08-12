# Task specification — integrate the review supply protocol and the superseded-branch register

Specification evidence base: `0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5`

    Branch  governance/supply-protocol-v3
            aa531aeab3a98b51b2b55b1f79f9e21c139e7dde

Classification: **MATERIAL**. The branch completed result review. This
is the integration authorization.

**Rules 1–17 are in force**, so this task is governed by Rule 15: its
pre-execution review is a committed artifact — see §5 commit 2 and A5.
**Rule 18 is NOT in force at the evidence base — this task lands it —
and this task does not apply it.** §4 governs how the review arrives.

**One merge.** Dry run from the evidence base with the specification and
review commits in place: **no conflict**, merge-base
`0ab6369a…`, and at the merge commit **5 additions and 3
modifications**. **If a conflict occurs, STOP.**

---

## 0. What is being integrated

**A supply rule for pre-execution reviews, and an attribute for branches
that must not be integrated.**

    Rule 18   a pre-execution review is supplied to the executor AS A
              FILE and committed byte-unchanged; no delimiters, no
              extraction, no normalisation, because there is no
              boundary to locate
    register  docs/BRANCHING_POLICY.md gains a SUPERSEDED attribute and
              a SIX-entry register naming each superseded branch, its
              commit, what replaced it, and why

**Rule 18 is the ninth attempt at this problem and the first that
removes it rather than patching it.** The five preceding failure modes
were boundary problems: where does the review text begin, what counts as
preamble, what must be stripped, what happens when the specification
itself contains the delimiter literals. **A file has no boundary to
infer.**

**The register is prose, and prose is what it can be.** It records
integrability, which a Git ref cannot carry. **It does not prevent
anything mechanically**, and §7 returns to that.

## 1. Two properties of the branch that make it integrable

**(a) No stale base.** `git merge-base --is-ancestor origin/main
origin/governance/supply-protocol-v3` exits 0, and the merge-base equals
`main` exactly. **The failure mode that stopped two earlier tasks is
absent here, and it was checked rather than assumed.**

**(b) `DECISION_LOG.md` is append-only on both measures.** Zero deleted
lines base-to-head, and the base blob is an **exact byte prefix** of the
head blob — 82337 bytes extended to 89541. **Zero deleted lines alone
would not establish this**; a rewritten line with an equal-count
insertion passes the line measure and fails the prefix measure.

## 2. What this integration does NOT establish

- **It does not enforce anything.** After this merge `main` carries
  eighteen rules and **no test that checks any of them.** The register
  is text; **nothing prevents a superseded branch from being merged**,
  and this task's A9 is a hand-checked criterion, not a machine one.
- **It settles no science.** No gate, no coefficient, no channel, no
  verdict. `P2-PHASE-01` stays `PROPOSED`.
- **It does not close the review-supply problem for tasks already in
  flight.** Rule 18 is prospective from this merge forward.
- **It assigns no branch to a status it did not already carry.** Per
  Rule 17: the six register entries record what the superseding tasks
  already established. **Do not add a seventh, do not re-characterise an
  entry, and do not assign a deletion outcome to any branch here.**

## 3. Two branches this task must not touch

**`governance/supply-protocol-v2 @ 40168469608618aef6812735ff70e32de0e3cbc8`**
and
**`governance/supply-protocol-and-superseded @ 7146a093c65788a57d63a747b71d86edb91eddc6`**
are entered in the very register this merge lands, as superseded by the
branch being merged.

**Neither may be merged, read from, or deleted.** **These two are singled
out because they are this task's own predecessors, NOT because the
register stops at two** — it holds six entries, and **A9 checks all
six.** **This task is the first occasion on which the register governs,
and it governs the task that lands it.**

## 4. How the review arrives

**Rule 18 is not operative at the evidence base.** An earlier attempt
stopped precisely because a specification required an executor to apply a
Rule 18 whose own text forbade the only available action. **This
specification does not repeat that.** What follows is a specification
instruction, and it is stated as one:

- **The pre-execution review is supplied as a FILE.** **This
  specification names no delimiters**, so there is nothing to extract.
- **If no file is supplied, STOP.** Do not reconstruct a review from a
  conversation, do not author one, do not accept pasted text as a
  substitute.
- **The review must identify this specification**, by digest or by task
  name. **If it identifies a different one, STOP and say which.**
- **Commit the file's bytes unchanged.** Placeholders inside the review's
  text stay as written; **placeholders are resolved in the PATH only.**
- **Report how the review arrived, and how this specification arrived.**

**This is the supply mode Rule 18 will require from the next task
onward.** Using it here is a choice made by this specification, **not an
application of a rule that is not yet in force.**

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-supply-protocol-v3.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-supply-protocol-v3.md
    commit 3  --no-ff merge of the source branch
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-supply-protocol-v3.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes the
merge**, per Rule 15's timing clause.

**Committed report:** raw output for A1, A2, A6–A9, A10-pre, A11 for
commits 1–3; the `PRE_MERGE` JSON verbatim; the intended final manifest
and the intended final `POST_MERGE` parameters; commit 1–3 SHAs and
messages; the pre-report head; the intended report commit message.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final `POST_MERGE` JSON, A4's final scope check, A10-final, the
push, the report commit's stored message read back from the object, and
ancestry confirmation.

## 6. Acceptance criteria

**A1 — Refs.** `refs/remotes/origin/main` and remote `refs/heads/main`
both resolve to `0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5`; the source
branch to `aa531aeab3a98b51b2b55b1f79f9e21c139e7dde`. Any mismatch →
STOP. **Local `main` is stale by design.** Report all refs, read from
the remote.

**A2 — Merge parentage, each value derived separately.**

    parent 1 = the integration pre-execution review commit (commit 2)
    parent 2 = aa531aeab3a98b51b2b55b1f79f9e21c139e7dde
    merge-base(parent 1, parent 2)
             = 0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5

**Parent 1 is fixed by which commit you are standing on**, and with §5's
order that is the review commit, not the specification commit. **Commit 1
MUST be an ancestor of parent 1**; verify and report that too.

**Derive the three values independently and report them as three
measurements.** Do not compute one and infer the others: the merge-base
here equals the evidence base and **not** parent 1, because parent 1
already carries two commits of this task's own.

**A3 — Guards.** `PRE_MERGE` before the merge; one final `POST_MERGE`
after the push. **The final guard carries TWO DISTINCT SHAs**: the merge
object is the merge commit; remote agreement is checked against the final
report-commit head. **If the guard cannot represent both roles
separately, STOP.**

**A4 — Scope, frozen manifest:**

    base: 0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
    head: <computed final head>
    mode: exact
    add:
      reports/2026-08-12T0131Z_supply-protocol-v3.md
      reports/2026-08-XXT{HHMM}Z_integrate-supply-protocol-v3.md
      reviews/chatgpt/2026-08-12T0131Z_supply-protocol-v3.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-supply-protocol-v3.md
      specs/2026-08-12T0131Z_supply-protocol-v3.md
      specs/2026-08-XXT{HHMM}Z_integrate-supply-protocol-v3.md
    modify:
      CONVENTIONS.md
      DECISION_LOG.md
      docs/BRANCHING_POLICY.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 6 additions and 3 modifications**, matching
the six and the three paths above — **nine paths in total.** Six arrive
from the branch (three additions and all three modifications); three are
authored here.

**At the merge commit, before the report exists, the count is 5
additions and 3 modifications.** Both figures are correct at their own
head; **report which head each measurement was taken at.**

**A5 — This task's pre-execution review committed, unedited**, at
`reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-supply-protocol-v3.md`,
**byte-identical to the supplied file**, per §4. **Report the supply mode
for both the review and this specification.**

**A6 — Arriving artifacts intact.** After the merge, these six paths are
blob-identical to the source branch:

    CONVENTIONS.md
    b3c96300a1f3eab967d3d141a1e81b278887342c

    DECISION_LOG.md
    d9dd2bf3a8cca405f03b31c51b1f478c7db77ca2

    docs/BRANCHING_POLICY.md
    3f0f35d4da448eb444d223fd003a5b0601792dc3

    reports/2026-08-12T0131Z_supply-protocol-v3.md
    f1250e759eac6da55bc67c99878afed1eeb6bba6

    reviews/chatgpt/2026-08-12T0131Z_supply-protocol-v3.md
    b0d9afd17f009a611699f8390e09b1f35a953740

    specs/2026-08-12T0131Z_supply-protocol-v3.md
    ac91efeb012c2740367c1c5d0c42929366b00b58

**These are Git blob ids, not content SHA-256 digests.** Compare with
`git rev-parse <rev>:<path>`.

**A7 — Protected paths, with the three authorised exceptions named.**

**`CONVENTIONS.md`, `DECISION_LOG.md` and `docs/BRANCHING_POLICY.md` are
NOT protected in this task.** They are the three paths this integration
exists to change, and A6 pins their post-merge blobs instead. **Recent
specifications list all three among the protected set; carrying that
list over unchanged would make A7 unsatisfiable.**

Protected, blob-identical between base and merged head:
`GATES.md`, `AGENTS.md`, `pyproject.toml`, and **every path under
`scripts/`, `results/`, `tests/`, `derivations/`, `docs/` and `reviews/`
that exists at the evidence base**, `docs/BRANCHING_POLICY.md` excepted.
**Compare path by path, not as tree objects** — `specs/`, `reviews/` and
`reports/` gain base-absent authorised paths.

**`tests/` gains nothing and loses nothing: 17 files before, 17 after,
none modified.**

**A8 — Append-only, on both measures.** For `DECISION_LOG.md`, base to
merged head: **zero deleted lines**, AND **the base blob is an exact byte
prefix of the merged blob.** Report both. **Expected: 82337 bytes
extended to 89541, zero deletions.** **A zero-deletion count alone does
not establish the prefix property and is not accepted for it.**

**A9 — Superseded branches not merged, ALL SIX.** No commit in the
register is an ancestor of the merged head:

    52f65117…  fix/pi-decisions-and-deferred
    ebd531ab…  fix/pi-decisions-v2
    40168469…  governance/supply-protocol-v2
    7146a093…  governance/supply-protocol-and-superseded
    10c260b9…  review/role-model-and-executors
    d64cd912…  gate/p2-land-diquark-line

Verify each with `git merge-base --is-ancestor` and **report six exit
statuses.** **The two of §3 are not a sufficient check**: the register
this task lands governs every branch in it, and a criterion covering a
subset would be a proxy for the property.

**All six still resolve to those commits after the task. This task
deletes no branch.**

**A10 — No gate changed.** `GATES.md` blob-identical at
`849a4fbfe62d6478f092a84b0175357a74bbbb06`; `^## P2-` count 14 before and
after; `P2-PHASE-01` still `PROPOSED`.

**A11 — Rule and register counts after the merge.** `CONVENTIONS.md`
carries **eighteen numbered rules**, Rule 18 being the review supply
protocol; the register in `docs/BRANCHING_POLICY.md` carries **SIX
entries.**

**Count the entries by a method that counts ENTRIES**, not vocabulary
hits and not headings: read the fenced block under `## Superseded
branches` and count entry records within it. **Report the method, and
LIST the six branch names counted**, so a correct number cannot conceal
a wrong target set. Expected:

    fix/pi-decisions-and-deferred            @ 52f65117…
    fix/pi-decisions-v2                      @ ebd531ab…
    governance/supply-protocol-v2            @ 40168469…
    governance/supply-protocol-and-superseded@ 7146a093…
    review/role-model-and-executors          @ 10c260b9…
    gate/p2-land-diquark-line                @ d64cd912…

**A count without the names is not accepted for this criterion.**

**A12 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`. **A12-pre** at the pre-report head goes
in the report; **A12-final** at the pushed head is post-report evidence.

**A13 — Commit-message hygiene** on every commit including the merge:
inspect the proposed message before, the stored message after; permit no
`Co-Authored-By`, no session identifier or URL, no tool attribution.
**Report per commit whether any trailer was suppressed and which.**

## 7. Rule 16 assessment

**Rule 16 is operative and governs this task.** State what the assembled
set does NOT establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** After this
merge `main` carries a supply rule, a superseded register, and eighteen
numbered rules. **A reader could conclude that review supply is now
verified and that superseded branches cannot be integrated.** **Neither
is mechanically true.** No test checks Rule 18; nothing but a reader
stops a superseded branch from being merged; **the register constrains
what a person may do, not what the repository will accept.** The
distinction between a rule that is written and a rule that is enforced
should be stated where a reader will meet it.

## 8. Invariants and prohibitions

- Executor-writable: the integration specification, its pre-execution
  review, and the integration report. **Everything arriving by merge is
  integrated exactly as reviewed and may not be edited.**
- **Do not edit `CONVENTIONS.md` or `docs/BRANCHING_POLICY.md` by hand.**
  They change only by merging the pinned ref. **If a rule looks wrong,
  report it; amending it is a separate task with its own review.**
- **Do not merge, read from, cherry-pick or delete ANY branch in the
  register** — the two named in §3, or any of the other four listed in
  A9.
- **Do not add a register entry, re-word one, or assign any branch a
  deletion outcome.** Rule 17.
- **Do not state that any rule is enforced, tested, or checked.** §7
  governs.
- No gate, gate status, verdict, digest, or hash-pinned artifact may be
  modified.
- Merge commit only: no fast-forward, no squash, no rebase, no
  force-push, no history rewrite. **Merge the pinned remote ref.**
- Any merge conflict is an immediate stop.
- Branch naming: use `governance/integrate-supply-protocol-v3`.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything listed in §5 under its correct layer;
- the merge commit SHA, its two parents and the merge-base, **as three
  separately derived values**, with the method for each;
- **A6's blob comparison for all six arriving paths**;
- **A7's path-by-path comparison**, with the count of pre-existing paths
  checked, and **explicit confirmation that the three authorised
  modifications were excluded from the protected set deliberately**;
- **A8's two measures reported separately**, byte lengths included;
- **A9's six ancestry exit statuses**, and the six branch tips read back
  after the task;
- **A11's register count WITH the six branch names**, and the counting
  method;
- the states of the merge worktree and the main worktree, **stated
  separately**;
- **§7's Rule 16 assessment**, junction named or search described;
- **whether the merged state reads as though any rule were now
  enforced.** It is not; §2 and §7 say so;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**
**Every line below was produced by running the stated method in a clean
clone.** Nothing here is asserted.

    target      the source branch and its base relation
    method      git merge-base --is-ancestor origin/main
                origin/governance/supply-protocol-v3; git merge-base
    CONFIRMED   exit 0; merge-base = 0ab6369a… = main exactly.
                NO STALE BASE.

    target      the merge itself
    method      dry run from 0ab6369a with a placeholder specification
                commit and a placeholder review commit, then
                git merge --no-ff of the pinned remote ref
    CONFIRMED   no conflict; parent 1 = the placeholder review commit,
                parent 2 = aa531aea…, merge-base = 0ab6369a…
    CONFIRMED   at the merge commit: 5 additions, 3 modifications
                (M CONVENTIONS.md, M DECISION_LOG.md,
                 M docs/BRANCHING_POLICY.md, and three additions under
                 specs/, reviews/chatgpt/ and reports/ from the branch,
                 plus the two placeholders)
    DERIVED     final head adds one report path: 6 additions,
                3 modifications. THIS IS ARITHMETIC ON A MEASURED
                VALUE, not a measured final head — the report commit
                does not exist yet.

    target      the six arriving blob ids of A6
    method      git rev-parse aa531aea:<path>
    CONFIRMED   all six, as listed in A6

    target      DECISION_LOG.md append-only, both measures
    method      git diff --numstat for deletions; byte-prefix test on
                the two blobs read with git cat-file
    CONFIRMED   0 deleted lines; base 82337 bytes is an EXACT BYTE
                PREFIX of head 89541 bytes; 7204 bytes added

    target      GATES.md across the merge
    method      git rev-parse <rev>:GATES.md; grep -c '^## P2-'
    CONFIRMED   849a4fbf… at both revisions, identical; 14 gate
                sections

    target      counts after the merge
    method      grep -cE '^### [0-9]+\.' on CONVENTIONS.md; register
                entries counted INSIDE the fenced block under
                '## Superseded branches', by entry record, with the
                branch names read back
    CONFIRMED   18 rules at aa531aea (17 at 0ab6369a); SIX register
                entries: fix/pi-decisions-and-deferred,
                fix/pi-decisions-v2, governance/supply-protocol-v2,
                governance/supply-protocol-and-superseded,
                review/role-model-and-executors,
                gate/p2-land-diquark-line
    RETRACTED   an earlier version of this record stated FIVE entries.
                That value was read from a diff truncated at 80 lines
                and never measured against the whole object. The
                truncation removed the sixth entry exactly. The method
                did not establish the property it was recorded under;
                the count is corrected here and the reviewer who
                caught it is the reason.

    target      all six register commits against the merged head
    method      git merge-base --is-ancestor <commit> <dry-run merged
                head>, run once per commit
    CONFIRMED   none of the six is an ancestor; six separate exit
                statuses

    target      tests/ across the merge
    method      git ls-tree -r --name-only <rev> tests/
    CONFIRMED   17 test files at both revisions; the branch touches no
                path under tests/
