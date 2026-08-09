# Integration report — amendments E–L and Rules 16 and 17

Specification: `specs/2026-08-09T1849Z_integrate-amendments-e-to-l.md`
Pre-execution review: `reviews/chatgpt/2026-08-09T1849Z_integrate-amendments-e-to-l.md`
Specification evidence base: `a4bfb337bd6ee92d60303e5cbb8f0646c48c16ed`
Source branch: `governance/land-amendments-e-to-l` @ `c58f1b9148828b8b37e775c6c499848bb63fd781`
Integration branch: `governance/integrate-amendments-e-to-l`
Pre-report head: `b4721ce2ae8f20cc1df425e609a265885557feec` (the merge commit)

**Outcome.** One `--no-ff` merge, no conflict, correct parentage,
merge-base the original base. All six arriving blobs are byte-identical
to their reviewed values, and the amendment draft's content digest is the
reviewed one. **Rules 1–15 keep their titles; exactly six rule bodies
changed — 3, 5, 8, 9, 12 and 14 — and the other nine are byte-identical.**
`DECISION_LOG.md` is append-only on all three measures. All 182
pre-existing paths under the six protected directories are identical.
Four validators pass.

**`CONVENTIONS.md` now runs 1–17 on the integration branch.**

**Rule 15's lifecycle ran again**: specification (commit 1), review
(commit 2), merge (commit 3), report (commit 4), with the review commit
an ancestor of the merge.

**Four things the Reviewer should read before the detail.**

**(a) The Amendment I weakness reported one task ago is closed, and
closed by design.** §17.2. The same chat-message instruction arrived —
but this time **A5 of the specification already said it**, so the
authority was durable before the message existed. **That is the fix
§1(a) promised, working.**

**(b) A6a's predicted Rule 15 newline artifact did not appear under my
extraction method, and I can show why.** §6.1. Both methods agree that
Rule 15's content is unchanged; the artifact is a property of how a
section is sliced, not of the file. **I reproduced the specification
author's observation under their method, so their claim is confirmed,
not contradicted.**

**(c) I found a stronger junction than §4's candidate, and report it
instead.** §16.

**(d) A prospective Amendment H check finds one shortfall in this
specification.** §17.1. It does not affect the result — every literal
reproduced — and H did not govern this task.

---

## 1. A1 — refs, read from the remote

    refs/remotes/origin/main                                  a4bfb337bd6ee92d60303e5cbb8f0646c48c16ed
    remote refs/heads/main                                    a4bfb337bd6ee92d60303e5cbb8f0646c48c16ed
    local  refs/heads/main                                    0f7961747abe2a18b436c0b1e5b928f425ea4d9a
    remote refs/heads/governance/land-amendments-e-to-l       c58f1b9148828b8b37e775c6c499848bb63fd781
    local  refs/heads/governance/land-amendments-e-to-l       c58f1b9148828b8b37e775c6c499848bb63fd781

Both remote `main` refs resolve to the evidence base and the source
branch to `c58f1b91…`. **Local `main` is stale by design and was not
repaired.** No `main` ref was moved.

**The merge took the pinned remote ref**, fetched immediately before and
confirmed to resolve to `c58f1b9148828b8b37e775c6c499848bb63fd781`.

**`{HHMM}Z` is `1849`**, fixed by commit 1 and reused.

## 2. A2 — merge parentage

    merge commit   b4721ce2ae8f20cc1df425e609a265885557feec
    parent 1       fdf39b46668b67ef73e82f6fad7550e5def4cfee   (commit 2, the review)
    parent 2       c58f1b9148828b8b37e775c6c499848bb63fd781   (the reviewed source branch)
    merge-base     a4bfb337bd6ee92d60303e5cbb8f0646c48c16ed   (the original base)

**Parent 1 is the review commit, not the specification commit.** A2 says
"Parent 1 is fixed by which commit you are standing on. With §5's commit
order it is the specification commit." **§5's commit order puts the
review at commit 2 and the merge at commit 3**, so the commit being stood
on is the review, and parent 1 is `fdf39b46…`.

**This is not a deviation.** A2's normative sentence — parent 1 is
whatever you are standing on — is satisfied exactly; its parenthetical
identification is one commit stale relative to §5, which the same
specification introduced. **The specification commit `229b8f39…` remains
an ancestor of parent 1 and therefore of the merge**, verified below.
Recorded because a reader checking A2's literal expectation against
`<merge>^1` would find a different SHA and should know why.

    git merge-base --is-ancestor 229b8f39… fdf39b46…   ->  exit 0
    commit 1 -> commit 2 -> merge, first-parent chain intact

**No conflict.** `git merge --no-ff --no-commit` reported
`Automatic merge went well; stopped before committing as requested`, and
`git diff --name-only --diff-filter=U` returned nothing.

## 3. A3 — `PRE_MERGE` guard

Run at the review commit, before the merge. **`overall: PASS`, exit
status 0, empty stderr.**

    checks
      PASS  worktree_clean
      PASS  worktree_matches_declared_target
              expected_worktree_head = worktree_head
                = fdf39b46668b67ef73e82f6fad7550e5def4cfee
              attachment = governance/integrate-amendments-e-to-l
      PASS  merge_base
              expected = actual = a4bfb337bd6ee92d60303e5cbb8f0646c48c16ed
      PASS  scope        overall PASS, 6 observed operations, failures []
              base a4bfb337…  head c58f1b91…  mode exact
                modify  CONVENTIONS.md
                modify  DECISION_LOG.md
                add     docs/amendments/2026-08-09_observation-and-propagation.md
                add     reports/2026-08-09T1801Z_land-amendments-e-to-l.md
                add     reviews/chatgpt/2026-08-09T1801Z_land-amendments-e-to-l.md
                add     specs/2026-08-09T1801Z_land-amendments-e-to-l.md
      PASS  pinned_artifacts
              AGENTS.md
                270c7ea4c38621cbafc9cee940c95c5ecf4cc65ff1e5d01e8029b1b12339d461
              scripts/p2_channel_character_layers.py
                b7463a421b29bdd58b4c8736e1bbe53dd0e5283e131db628eee46cbdf36eb994

    mode     PRE_MERGE
    overall  PASS

**`scripts/p2_channel_character_layers.py` was pinned deliberately.**
§1(b) names it as Amendment L's known unsatisfied instance and §6
forbids touching it; pinning it by digest makes the prohibition
mechanically checked at the earliest point rather than only asserted.

**A3's two-SHA requirement is satisfiable.** The `POST_MERGE` config
carries `merge_commit` and `expected_remote_sha` as separate fields.
**No stop was required.** The intended parameters are in §10.

## 4. A5 — this task's pre-execution review, committed unedited before the merge

    reviews/chatgpt/2026-08-09T1849Z_integrate-amendments-e-to-l.md
      committed blob sha256
        4f9f780562d90bc68d5905e61a08ad82f3f0c774a6963bfd42301bc54a3d3bfd
      git blob id
        31bb7a205cace327d629baec90b68b91342203ec
      25 lines

**Committed as commit 2, before the merge in commit 3** — Rule 15's
timing clause, and §5's explicit ordering.

**Exactly what I did, stated because representation can be substance.**
The text was supplied between two delimiter lines. **The delimiter lines
themselves are excluded, as is the instruction accompanying them**, per
A5. Blank lines adjoining the delimiters were dropped and the file ends
with exactly one newline. **No character of the review's own content was
added, removed or altered**, verified by comparing the committed blob
against the extracted text.

**Placeholders inside the review body were not resolved.** Its closing
paragraph still reads *"{HHMM} in the review artifact path is resolved
from the token fixed by commit 1"*, with the braces intact. **Only the
filename resolves the token**, to `2026-08-09T1849Z`.

**It corresponds to this specification**, checked rather than assumed. It
names the specification by title; it cites the evidence base
`a4bfb337bd6ee92d60303e5cbb8f0646c48c16ed` and the source branch
`governance/land-amendments-e-to-l @ c58f1b9148828b8b37e775c6c499848bb63fd781`,
both of which §1 confirms; it states that the source branch carries four
additions and two modifications, which §3's `PRE_MERGE` scope confirms
as six operations of exactly that shape; and it addresses A5's own
placeholder rule. **Disposition: APPROVED. Approval: EXECUTION
AUTHORIZED AS WRITTEN.**

**The review's one non-blocking observation, honoured.** It reads §4's
phrase *"exercise the rule prospectively"* as exercising the procedure
Rule 16 will impose once operative, **not as applying Rule 16 as current
authority**. §16 is written on that reading and says so.

## 5. A6, A7 and A8 — everything arriving is byte-identical

Git blob ids at the merged head, compared both to the specification's
declared values and to the source branch:

    CONVENTIONS.md
      0db56c39d44e19126b1035b13ebcf357259c482f   MATCH
    DECISION_LOG.md
      bdb9dac59cc84416b51e626c7b26a0a7c956d68e   MATCH
    docs/amendments/2026-08-09_observation-and-propagation.md
      642b2541571dcb6fa91edb36bbc75dc93df33f6b   MATCH
    reports/2026-08-09T1801Z_land-amendments-e-to-l.md
      4e9f40e2b8e2a30948bd8df3b2e5c80376adc4ec   MATCH
    reviews/chatgpt/2026-08-09T1801Z_land-amendments-e-to-l.md
      10a95fca0b56638f0115963e1d14ad99fe95dcb3   MATCH
    specs/2026-08-09T1801Z_land-amendments-e-to-l.md
      fb4dbf2094453ec891265fb3d3bd32f4f5090dbf   MATCH

**All six agree with the specification and with the source branch.
Nothing arriving was edited.**

**The amendment draft's CONTENT digest at the merged head**, computed
from `git cat-file blob <merge>:<path>`:

    6368aff4ad66126f115be3fd0689e513db59e6061a28dd4e599b9bb5aa91c0e4

**Both quantities are reported because they establish different things**,
as A8 says: the blob id proves the file arrived through the merge
unaltered; the SHA-256 proves it is the reviewed draft and not merely
*a* file that travelled intact. **They are different quantities and this
report does not conflate them** — which is Amendment C's subject, landed
in Rule 9 at the previous integration.

## 6. A6a — rules 1–15 unchanged apart from the seven authorised insertions

**Method.** Each `### <n>. <title>` section was extracted from the base
blob and the merged-head blob by heading boundary, and title and body
compared separately.

    rules present            base 1-15          head 1-17
    titles 1-15 identical    True               differing titles: none
    rule bodies that differ  [3, 5, 8, 9, 12, 14]     exactly as specified
    byte-identical bodies    [1, 2, 4, 6, 7, 10, 11, 13, 15]    9 of 15

**Exactly the six rules the seven amendments attach to changed** — Rule 9
takes two, G and L — **and no others.** Comparison by raw body and by
`rstrip`ped body give the same six.

### 6.1 The Rule 15 newline artifact, and why it did not appear

**A6a predicts** that Rule 15's extracted block "gains one trailing
newline because it is no longer the file's last section" and is
"identical after `rstrip`". **Under my extraction it is byte-identical
with no rstrip needed**, and Rule 15 appears in the byte-identical list
above.

**Both observations are correct and they measure different things.** I
reproduced each:

    method A — slice the LINE LIST between heading lines
      base == head            True
      base tail  '…are not to be back-filled.\n'
      head tail  '…are not to be back-filled.\n'

    method B — slice the RAW TEXT from the heading to the next heading marker
      base == head            False
      base == head (rstrip)   True
      base tail  '…are not to be back-filled.\n'
      head tail  '…are not to be back-filled.\n\n'

**Method B reproduces the specification author's observation exactly.**
Under method A the file-final blank line and the blank line before
`### 16.` occupy the same position in the sliced list, so they cancel;
under method B the second one is inside the slice and the first is the
end of the string.

**The artifact is a property of the extraction, not of the file.** Both
methods agree on the property that matters — **Rule 15's content is
unchanged** — and neither shows a rewording. **This is the umbrella
principle of the amendments this merge lands, met while verifying the
merge that lands it**: a difference that exists in the measurement and
not in the thing measured.

**No rstrip was needed to reach the verdict**, and I report the raw
comparison rather than the rstripped one so the reader can see which is
which.

## 7. The rule heading list at the merged head

    ### 1. Contradiction-stop
    ### 2. Scope precedence
    ### 3. Declared frozen scope is normative
    ### 4. Execution prompts are evidence
    ### 5. Minimum mandatory merge discipline
    ### 6. Reporting honesty for merges
    ### 7. Evidence precedence
    ### 8. Responsibility separation (root rule of this section)
    ### 9. Outcome-based task specification
    ### 10. Self-correction authority and its limit
    ### 11. Task granularity and integration boundary
    ### 12. Acceptance criteria must be mechanically checkable
    ### 13. Execution environment
    ### 14. Validator outcome contract
    ### 15. Governing artifacts are committed
    ### 16. Accumulated reading                                          <- arrived
    ### 17. Integrations do not add epistemic or governance classifications   <- arrived

**Seventeen rules, contiguous from 1, no duplicates, no renumbering.**

## 8. Rules 16 and 17, quoted in full as they now stand

### 8.1 Rule 16, at the merged head — lines 943–980

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

### 8.2 Rule 17, at the merged head — lines 982–990

    ### 17. Integrations do not add epistemic or governance classifications

    **An integration, derivation, or any task that carries reviewed
    results forward MUST NOT add a governance or epistemic classification
    the reviewed results did not carry.**

    Recording what a result did not establish is required. **Assigning it
    to an open item, a gate, a status, or a category it was never assigned
    to is not.**

## 9. A7 — `DECISION_LOG.md`, all three append-only measures

**Measure 1 — evidence base to merged head:**

    git diff --numstat a4bfb337… b4721ce2… -- DECISION_LOG.md
      124     0       DECISION_LOG.md

    deleted lines across the whole base-to-head diff:  0

**Measure 2 — merge commit against PARENT 1 (`fdf39b46…`):**

    124     0       DECISION_LOG.md          deletions: 0

**This establishes that the integration deleted none of the base's log.**
Parent 1 carries the base's `DECISION_LOG.md` unchanged — commits 1 and
2 add only a specification and a review — so the 124 added lines are
exactly the source branch's entry arriving, with nothing of the base
removed to make room.

**Measure 3 — merge commit against PARENT 2 (`c58f1b91…`):**

    (empty numstat)                          deletions: 0

**This establishes that the merge dropped none of the source branch's
entries.** An empty numstat is stronger than zero deletions: the merged
`DECISION_LOG.md` is *identical* to the source branch's, so nothing the
source branch wrote was lost, reordered or truncated.

**The three measure different things and are reported separately**, as
A7 requires. Measure 1 is the net effect on `main`'s history; measure 2
is what the integrator did to the base; measure 3 is what the merge did
to the reviewed content.

**Corroboration:** the merged blob has the base blob as an **exact byte
prefix**, with 5455 characters appended. Entry count **26 at the base, 27
at the merged head** — one arriving entry,
`## 2026-08-09 — CONVENTIONS.md amendments E–L adopted; Rules 16 and 17
added`.

## 10. A4 — scope, and the intended final `POST_MERGE`

### Intended final manifest

    base: a4bfb337bd6ee92d60303e5cbb8f0646c48c16ed
    head: <the report commit, computed after this file is committed>
    mode: exact
    required:
      add     docs/amendments/2026-08-09_observation-and-propagation.md
      add     reports/2026-08-09T1801Z_land-amendments-e-to-l.md
      add     reports/2026-08-09T1849Z_integrate-amendments-e-to-l.md
      add     reviews/chatgpt/2026-08-09T1801Z_land-amendments-e-to-l.md
      add     reviews/chatgpt/2026-08-09T1849Z_integrate-amendments-e-to-l.md
      add     specs/2026-08-09T1801Z_land-amendments-e-to-l.md
      add     specs/2026-08-09T1849Z_integrate-amendments-e-to-l.md
      modify  CONVENTIONS.md
      modify  DECISION_LOG.md
    optional: []
    forbidden_operations: [delete, rename, copy, type_change, unmerged, unknown]

**7 additions and 2 modifications.** Four arrive from the branch; three
are authored here — this specification, its pre-execution review, and
this report. **A tenth path would be a defect.**

### Observed at the pre-report head

`git diff --name-status a4bfb337… b4721ce2…`, eight paths, this report
not yet existing:

    M   CONVENTIONS.md
    M   DECISION_LOG.md
    A   docs/amendments/2026-08-09_observation-and-propagation.md
    A   reports/2026-08-09T1801Z_land-amendments-e-to-l.md
    A   reviews/chatgpt/2026-08-09T1801Z_land-amendments-e-to-l.md
    A   reviews/chatgpt/2026-08-09T1849Z_integrate-amendments-e-to-l.md
    A   specs/2026-08-09T1801Z_land-amendments-e-to-l.md
    A   specs/2026-08-09T1849Z_integrate-amendments-e-to-l.md

### Intended final `POST_MERGE` parameters

    mode                   POST_MERGE
    merge_commit           b4721ce2ae8f20cc1df425e609a265885557feec
    expected_parent_1      fdf39b46668b67ef73e82f6fad7550e5def4cfee
    expected_parent_2      c58f1b9148828b8b37e775c6c499848bb63fd781
    expected_merge_base    a4bfb337bd6ee92d60303e5cbb8f0646c48c16ed
    scope_manifest         the final manifest above
    pinned_artifacts       AGENTS.md and
                           scripts/p2_channel_character_layers.py, as PRE_MERGE
    remote_check_policy    REQUIRED
    expected_remote_ref    refs/remotes/origin/main
    expected_remote_sha    <the report commit head>

**Two distinct SHAs in two distinct fields.** **The final guard result is
post-report evidence.**

## 11. A9 — protected paths, compared path by path

    AGENTS.md                                 5e60b5f…  IDENTICAL
    GATES.md                                  bd48205…  IDENTICAL
    pyproject.toml                            9fc6fdd…  IDENTICAL
    scripts/p2_channel_character_layers.py    68ba9bb…  IDENTICAL

**Every path under `scripts/`, `results/`, `tests/`, `derivations/`,
`reviews/` and `docs/` that exists at the evidence base**, enumerated
from the base and compared one by one — **not as tree objects**, since
`reviews/` and `docs/` both gain paths this task authorises:

    182 pre-existing paths checked, 0 differ

and the only changes to those directories, all additions of paths absent
at the base:

    A   docs/amendments/2026-08-09_observation-and-propagation.md
    A   reviews/chatgpt/2026-08-09T1801Z_land-amendments-e-to-l.md
    A   reviews/chatgpt/2026-08-09T1849Z_integrate-amendments-e-to-l.md

**No existing review record was modified or back-filled.**

**`scripts/p2_channel_character_layers.py` is byte-identical**, and was
additionally pinned by digest in the `PRE_MERGE` guard. **Amendment L's
known unsatisfied instance is untouched**, as §1(b) and §6 require. No
conventions-index entry was added.

## 12. A10 — no gate changed

    GATES.md   base bd48205…   merged bd48205…   IDENTICAL
    ^## P2- anchor count:   14 before,  14 after

    P2-GAP-01     Status: PASS (continuum exact; lattice `I_0` agrees
                  with paper at matched mass)          — unchanged
    P2-PHASE-01   Status: PROPOSED                     — unchanged

No gate, gate status, verdict, digest or hash-pinned artifact was
modified. **No science, no result, no claim is affected.**

## 13. A11-pre — validators at the pre-report head

Run individually with `python -m pytest <path>`, that exact invocation,
since `pytest` on this host resolves to 9.0.2 while `python -m pytest`
resolves to 9.1.1.

    tests/test_repository_structure.py    exit=0    4 passed
    tests/test_si1_governance.py          exit=0   14 passed
    tests/test_gate_anchors.py            exit=0   18 passed, 2 deselected
    tests/test_governance_tools.py        exit=0    8 passed

`pytest 9.1.1`, Python 3.11.15. **A11-final at the pushed head is
post-report evidence.**

**Under Rule 14, as landed at the previous integration**, each of these
is a PASS on the full contract and not only on the exit status: the
process started, completed without timeout or external termination,
returned exit 0, and no test, collection phase or teardown phase was
skipped or aborted. **The two deselections in `test_gate_anchors.py` are
the file's own marker configuration, present identically at the base**,
not a skip introduced here.

**What the validators assert about `CONVENTIONS.md`: nothing
structural.** `test_repository_structure.py` lists the path in a
required-paths set — it asserts the file EXISTS.
`test_governance_tools.py` uses it as a fixture path inside synthetic
criteria evaluated against historical commits. **No validator asserts a
rule count, numbering, ordering or heading structure**, so gaining two
more rules could not trip one. §16 uses this.

## 14. A12 — commit-message hygiene

Every message was written to a file, inspected for `Co-Authored-By`,
`Claude-Session`, `claude.ai`, `Generated with` and `http` **before**
committing, committed with `git commit -F <file>` and never `-m`, and
the stored message read back from the object afterwards.

    commit 1   229b8f39…   trailers suppressed: Co-Authored-By, Claude-Session
    commit 2   fdf39b46…   trailers suppressed: Co-Authored-By, Claude-Session
    commit 3   b4721ce2…   trailers suppressed: Co-Authored-By, Claude-Session
               (the merge; committed via --no-commit then -F)

**Suppression is a fact to disclose, not an absence.**

### Commit 1 — the specification

    229b8f3990bd5fde9f285a17f231ad1cd6574eae
    committed content sha256
      e9cd68dfc4065f0aa36e68dc7aa64541fdc788e95f2c3c548ab75a1bfca50b0b

    spec: integrate amendments E-L and Rules 16 and 17

    Verbatim transcription of the PI specification authorizing the
    integration of governance/land-amendments-e-to-l at c58f1b91.

    Rules 1-15 are in force at the evidence base, so this task is governed
    by Rule 15 and its pre-execution review is committed as commit 2, before
    the merge proceeds. Rules 16 and 17 arrive with the merge and do not
    govern this task.

**The digest is recorded because Rule 4 requires it** — the execution
prompt committed *and* its sha256 in the run's report. Rule 4 is in force
at this evidence base.

### Commit 2 — the pre-execution review

    fdf39b46668b67ef73e82f6fad7550e5def4cfee

    review: pre-execution review of the amendments E-L integration

    The Reviewer's approval of
    specs/2026-08-09T1849Z_integrate-amendments-e-to-l.md, committed
    unedited before the merge proceeds, as Rule 15 requires.
    Disposition: APPROVED. Approval: EXECUTION AUTHORIZED AS WRITTEN.

    The executor did not write, edit, summarise or reformat it. The
    delimiter lines and the instruction accompanying them are excluded.
    Only the filename resolves the specification's {HHMM} token; any
    placeholder inside the review body stays exactly as supplied.

### Commit 3 — the merge

    b4721ce2ae8f20cc1df425e609a265885557feec

    merge: integrate amendments E-L and Rules 16 and 17 (reviewed; pinned c58f1b9)

    Merges governance/land-amendments-e-to-l at
    c58f1b9148828b8b37e775c6c499848bb63fd781, reviewed and unmodified.

    CONVENTIONS.md goes from 1-15 to 1-17. Amendment E refines Rule 14, F
    Rule 12, G and L both Rule 9 as distinct blocks, H Rule 3, I Rule 8 and
    K Rule 5; Rule 16 adds accumulated reading and Rule 17 records that
    integrations do not add epistemic or governance classifications. Rules
    1-15 keep their titles and, apart from the seven authorised insertions,
    their bodies are byte-identical.

    The amendments' justification arrives committed at
    docs/amendments/2026-08-09_observation-and-propagation.md, byte-identical
    to the reviewed draft.

    Rules 16 and 17 become operative on main with this merge and do not
    retroactively govern the tasks that landed or integrated them. Three
    findings the source task reported remain open and are not addressed
    here: the Amendment I process weakness, Amendment L's known unsatisfied
    instance in scripts/p2_channel_character_layers.py, and Rule 13's two
    diagnostic orders.

    AGENTS.md is untouched, no existing review record is back-filled, no
    gate status changes, and no science or result is affected.

### Intended report commit message

Prepared the same way, with the same two suppressed:

    docs: report the integration of amendments E-L and Rules 16 and 17

    Records one --no-ff merge of governance/land-amendments-e-to-l at
    c58f1b91, with correct parentage and the original base as merge-base.
    All six arriving blobs are byte-identical and the amendment draft's
    content digest is the reviewed one. CONVENTIONS.md now runs 1-17;
    extracted section by section, rules 1-15 keep their titles, exactly
    bodies 3, 5, 8, 9, 12 and 14 changed, and the other nine are
    byte-identical. DECISION_LOG.md is append-only on all three measures.

    Reports that A6a's predicted Rule 15 newline artifact is a property of
    the extraction method rather than of the file, with both methods
    reproduced, and that Rule 15's content is unchanged either way.

    Reports that the Amendment I process weakness of the previous task is
    closed by design, one prospective Amendment H shortfall in this
    specification, and a stronger accumulated-reading junction than the
    candidate offered: the rules are entirely self-reported, with no
    mechanical enforcement anywhere in the repository.

## 15. Worktree states, stated separately

**The merge worktree**, `<scratch>/integ9`: created from `a4bfb337…` for
this task, attached to `governance/integrate-amendments-e-to-l`, clean at
the pre-report head `b4721ce2…`. The `PRE_MERGE` guard's
`worktree_clean` check confirmed it independently before the merge.

**The primary worktree**, `/home/user/2-emergent-gravity`: on
`gate/p2-grassmann-crossing-sign` at `cf4c789`, **zero modified or
untracked entries, and not touched by this task.**

No other worktree was altered. Nothing was cleaned, stashed or
discarded.

## 16. §4 — the accumulated-reading assessment, in Rule 16's form

**Rule 16 is not governing authority for this task.** It does not exist
at the evidence base and becomes operative when this merge lands. **This
section exists because §4 of the specification requires it**, and it
exercises the procedure Rule 16 will impose rather than applying Rule 16
as authority — which is the reading the pre-execution review states and
§4's surrounding text confirms.

### 16.1 The candidate junction, and why I report a stronger one

**§4 offers:** `CONVENTIONS.md` with seventeen rules, `DECISION_LOG.md`
with six recent rulings, `docs/amendments/` with one justification
document — a reader could conclude the programme's execution discipline
is now complete and self-consistent.

**That is true and it is the weaker form.** "Complete and
self-consistent" is a vague conclusion, and §1's three open items are
themselves recorded on `main`, so a careful reader has the counterweight
in front of them.

### 16.2 The stronger junction, named

**Three artifacts, one specific inference.**

    docs/amendments/2026-08-09_observation-and-propagation.md
      each incident marked CAUGHT PRE-ISSUE or REACHED EXECUTION
    docs/amendments/… and CONVENTIONS.md rules 3, 5, 8, 9, 12, 14, 16, 17
      each incident answered by a landed rule
    DECISION_LOG.md 2026-08-09
      "amendments E–L adopted; Rules 16 and 17 added"

**The inference their combination makes available:** *an incident marked
`REACHED EXECUTION` has a rule against it, therefore that failure mode
is now prevented.*

**It is not.** Nothing in the repository detects a violation of any of
the seventeen rules.

### 16.3 The search that establishes it, described

I searched `tests/` and `scripts/governance_tools/` for any check bearing
on the rules — for `reviews/`, `pre-execution`, `literal.verif`,
`rule <n>`, `append-only`, `accumulated`. **Four hits, none of them an
enforcement:**

    tests/test_repository_structure.py:88-90
      "reviews/README.md", "reviews/chatgpt/.gitkeep",
      "reviews/claude/.gitkeep"   — path-existence entries
    tests/test_governance_tools.py:28
      REVIEW = "reviews/pi/2026-08-03-…md"   — a fixture path

`test_si1_governance.py` constrains the gate ledger's content;
`test_gate_anchors.py` constrains scientific results. **Neither touches
execution discipline.**

**Concretely, nothing checks:** that `CONVENTIONS.md`'s rules are
contiguous or unduplicated (§13); that a specification carries a literal
verification record (Amendment H); that a review commit precedes the work
commit (Rule 15, and this task's own commit order); that a mutation test
reaches its dependency (Amendment F); that an append-only file was not
rewritten from a distant base (Amendment K).

### 16.4 What the assembled set does NOT establish

1. **That any failure mode is prevented, or detected.** The set
   establishes that failures were observed, classified and turned into
   obligations. **Every one of the seventeen rules is self-reported.**
2. **That past work complied.** All seventeen bind prospectively; the
   incident records describe work done under earlier rules and are not
   retrospectively non-conforming.
3. **That the three open items of §1 are closed.** They are not, and
   this merge does not close them.
4. **That Rule 15's lifecycle is enforced.** It has now run twice and is
   visible only in commit order. **Two consecutive tasks following a
   rule is evidence of compliance, not of a mechanism.**

**The limitation whose omission would most change the natural reading is
(1)**, and it is the only one not already stated somewhere on `main`.

## 17. The two separate questions §7 asks

### 17.1 Did this task comply with the rules actually in force at its evidence base?

**Rules 1–15 were in force. Yes, and Rule 15 in particular.**

    Rule 15   specification committed as commit 1                     YES
              pre-execution review under reviews/chatgpt/, committed
                before the work it authorises proceeded               YES — commit 2
                                                                      precedes the
                                                                      merge in commit 3
              task report under reports/                              YES — commit 4
              supplied manifests reproduced in the report             YES — §3 and §10

    Rule 4    execution prompt committed AND its sha256 in the report  YES — §14,
                                                                      e9cd68df…
    Rule 1    contradiction-stop                                      no contradiction met
    Rule 3    declared frozen scope compared against the changed-file
              list, output recorded                                   YES — §10
    Rule 7    every claim about repository state verified against the
              committed artifacts                                     YES — every digest
                                                                      in this report is
                                                                      read from a git
                                                                      object
    Rule 12   every acceptance criterion mechanically checkable       YES
    Rule 14   validators pass on the full contract, not exit code
              alone                                                   YES — §13

**Rule 13's two diagnostic orders did not have to be chosen between.**
§6 of the specification asks me to report which I followed if they
differ. **No environment failure occurred**, so neither order was
exercised. **Reporting that I "followed" one would be asserting a
procedure I never ran** — which is the failure Amendment E, landed by
this merge, exists to prevent.

### 17.2 Would this execution ALSO satisfy Amendments H, I, K and Rule 17?

**A prospective self-application check. None of these governed this
task. One shortfall found, in the specification rather than in the
execution.**

**Amendment I — PASSES, and by design.** The previous task's weakness was
that a chat message resolved an ambiguity A4a left open. **The same chat
message arrived this time** — the review supplied with an instruction to
commit it verbatim, excluding the delimiters and the instruction itself.
**But A5 of this specification already says exactly that**, in its own
text:

    byte-identical to the text supplied between the supplied delimiters,
    excluding the delimiter lines themselves and any instruction
    accompanying them
    …
    If a placeholder appears inside the review's text, it stays as written
    — resolve placeholders only in the path.

**So the durable authority existed before the message did.** The message
was redundant rather than load-bearing. **§1(a) promised this fix — "A
clause in A4a would have put the resolution where Amendment I requires
… and A5 of this one does" — and it works.** Last time the pass was
luck; this time it is design.

**Amendment K — PASSES, and its distinguishing measure is vacuous
here.** K evaluates append-only against the last pushed state of the
branch as well as the evidence base. **This branch has never been
pushed**, so there is no earlier pushed state and the measures coincide;
§9's three measures are all zero. **K's general trigger did not fire**:
nothing required a construction the specification does not describe.

**Rule 17 — PASSES, and it was actively applied.** Rule 17 forbids
adding a governance or epistemic classification the reviewed results did
not carry. **§5 of this report reports the draft's blob id and content
digest as two quantities establishing two different things, without
calling the draft a category Rule 15 does not name** — the trap the
previous landing report identified. **§16 records what the assembled set
does not establish without assigning anything to a gate, an open item or
a status.** No arriving artifact was reclassified.

**Amendment H — ONE SHORTFALL, in the specification.** H requires that
where a literal is itself sensitive — "especially a hash, an object id, a
machine-consumed heading, or an identifier" — **"the expected value and
the executable verification method MUST be written out."**

**This specification writes out the expected values and not the
method.** A6, A7 and A8 give six Git blob ids and one content digest, and
A8 says *"These are Git blob ids, not content SHA-256 digests"* — which
is the Amendment C distinction, correctly drawn. **It does not say how to
obtain them.** The previous integration specification did: *"Compare with
`git rev-parse <rev>:<path>`."*

**What this cost: nothing.** All seven literals reproduced, and the
method is unambiguous from the quantity named. **Why it is still worth
reporting:** H exists because a blob id and a content digest are
routinely confused and because an unstated method lets two people compute
different things from the same word. **A one-clause addition would close
it**, and H did not govern this task, so this is a prospective finding
and not a breach.

**Also under H:** §0's verification claim — "Verified independently
before this specification was written, by extracting each rule section
from both revisions" — **is the execution record H asks for, and §6
reproduces its three findings.** The Rule 15 newline artifact is where
the method's absence shows: §0 states the artifact without saying how the
section was extracted, and §6.1 had to reconstruct two candidate methods
to reconcile it. **That is a concrete instance of the cost H names.**

## 18. Do any of the seventeen rules contradict one another?

**One unresolved problem carried forward; five overlaps and near-conflicts
that resolve.**

### 18.1 Rule 13's two diagnostic orders — unresolved, and now flagged by the specification itself

Rule 13's pre-existing text says environment failures "SHALL be diagnosed
in this order: (1)…(5)"; Amendment D, in the same rule, says the order
"is extended by a step before identity" and gives `(0)`–`(6)`.
`docs/local/execution_environment.md` still says "Follow rule 13's
diagnostic order".

**§6 of this specification is the first to acknowledge it operationally**
— "Rule 13 carries two such orders — §1(c). If they differ for what you
need, report which you followed and why." **That converts a latent
ambiguity into an instruction that can be answered**, which is an
improvement, but the rule text is still ambiguous and the fix is a
rewording of Rule 13.

### 18.2 Rule 3 (Amendment H) and Rule 12's existing literal refinement — overlapping

Rule 12 already required repository-derived literals to be machine-checked
at the evidence base before issue; Amendment H now requires, in Rule 3,
that a specification requiring a literal match have executed it and
declared its check type. **Different scope, same subject.** §17.2 is an
instance: the shortfall is under H's clause, and Rule 12 alone would not
have caught it. **A cross-reference would help; neither rule is in this
task's writable set.**

### 18.3 Rule 1 and Amendment K's partial stop — refinement, not conflict

Rule 1 says stop and report on any contradiction, "never something to
resolve unilaterally". Amendment K, four rules later, gives that
operational content — stop before the first irreversible or
authority-expanding step, complete what is independently authorised,
then report — and warns that a bare stop teaches silence. **Consistent,
and K is the useful half. Rule 1 read alone still reads as a bare stop**,
and nothing points from one to the other.

### 18.4 Rule 14 now carries two three-valued vocabularies

Rule 14's dispositions — `satisfied`, `not satisfied, PI-authorized
exception`, `waived` — now sit beside Amendment E's observation states —
observed positive, observed negative, not observed. **Different subjects,
both threefold, one rule.** A careless reader could map "not observed"
onto "waived"; they are not the same, since a waiver removes an
obligation before evaluation while "not observed" means the measurement
failed and must be repaired. §17.1's Rule 13 answer is exactly this
distinction in use.

### 18.5 Rule 16 and Rule 17 — a near-conflict the draft settled

Rule 16 requires stating what an assembled set does **not** establish;
Rule 17 forbids adding an epistemic classification the reviewed results
did not carry. **Rule 17's own text resolves it**: *"Recording what a
result did not establish is required. Assigning it to an open item, a
gate, a status, or a category it was never assigned to is not."* **§16 is
written inside that boundary.**

### 18.6 Rule 16 and Rule 9's Amendment L — adjacent, not overlapping

Both concern discoverability, and they are different. **L is about a
convention a computation consumes being findable from the index; 16 is
about what a reader assembles from artifacts none of which says it.**
**§16.2's junction is a Rule 16 matter, and §1(b)'s script is an L
matter, and neither substitutes for the other.** Recorded because both
landed in Rule 9 and Rule 16 in one merge and a reader could take them
for one obligation.

### 18.7 Rule 4 and Rule 15 — the overlap persists, and this task satisfies both

Rule 4 requires the execution prompt committed **and its sha256 in the
report**; Rule 15 requires the specification committed as the first
commit and says nothing about a digest. **Both bind, and §14 records the
digest**, so the open question — whether a governance task is a "decisive
or pre-registered run" — does not need answering for this task. **It
remains open and is not mine.**

## 19. Stops and clarifications

**No stop occurred.** No conflict arose and every check passed.

### `SPECIFICATION_DEFECT`

**None that affected execution.** Two observations, neither a defect in
substance:

**(a)** A2's parenthetical says parent 1 "is the specification commit",
while §5's commit order makes it the review commit. **A2's normative
sentence — parent 1 is whatever you are standing on — is satisfied
exactly**, and §2 reports both SHAs with the ancestry shown. This is the
parenthetical lagging the structure §5 introduced, and it is exactly the
propagation Amendment G describes.

**(b)** The Amendment H shortfall of §17.2 — expected values written out,
executable method not. **Prospective only**; H did not govern this task.

### `ENVIRONMENT`

None. Nothing was installed. **No environment failure occurred**, so Rule
13's diagnostic order — either version — was not exercised (§17.1).

### `OBSERVATION_METHOD_ERROR`

**None reached an output. One was caught during execution, and it is the
same class as §6.1's.**

My first extraction of the review artifact located the delimiters with
`text.index("=== REVIEW ARTIFACT BEGINS ===")`. **That found the
delimiters' first mention — inside the accompanying instruction sentence,
which names both of them in prose** — and returned a four-character
fragment, ` 同 `.

**The available readings were "the artifact is nearly empty" and "my
locator matched the wrong occurrence."** The second was correct. The
extraction was redone by requiring the delimiter to be a **line of its
own**, which found exactly one of each, and the boundaries were printed
and checked before anything was written. **No file was created by the
failed attempt.**

**This is Amendment E's shape**, met while integrating Amendment E: a
measurement that produced a result, where the result was a property of
the locator rather than of the text.

### `REPOSITORY_DEFECT`

**None.** §16.3's finding — that no test enforces any of the seventeen
rules — is a coverage gap, not a violation of a frozen requirement, and
is filed in §20.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`

**One, raised and not resolved.** Whether a governance or integration
task is a "decisive or pre-registered run" within Rule 4 (§18.7). It does
not block this task, which records the digest either way.

## 20. Secondary findings, and what I would have specified differently

**1. `CONVENTIONS.md` carries seventeen rules and nothing enforces any of
them.** §16.3 is the search; §13 is the specific case for the file's own
structure. **Raised at the A–D landing, at its integration, at the E–L
landing, and here — while the file grew from 13 rules to 17.** A standing
test asserting contiguous numbering from 1, no duplicates, and
`^### <n>. <title>` headings would make the next silent renumbering
impossible to land, and a second asserting that every `specs/*.md` has a
matching `reports/*.md` would make Rule 15's lifecycle partly checkable.
**`tests/` is protected in every one of these tasks**, so this needs its
own authorization and will not happen as a side effect.

**2. The Amendment I fix should be generalised into the specification
template.** §17.2. A5's two clauses — what the delimiters exclude, and
that placeholders resolve in the path only — turned a chat-message
dependency into issued authority in one revision. **Every future task
supplying an artifact verbatim needs those two clauses**, and they are
currently re-derived per specification.

**3. Amendment L's obligation still has no first assignee.** §1(b)
identifies the instance — `scripts/p2_channel_character_layers.py`, two
rulings located by exact `DECISION_LOG.md` heading text — and §6 forbids
touching it here, correctly. **The rule is now on `main`; the instance is
named; nothing schedules the fix.** A follow-up naming the two rulings
and the index entries they need would convert a rule into a change.

**4. Rule 13's rewording is now blocking two things.** §18.1. It is
ambiguous in the file, it has an active downstream reader in
`docs/local/execution_environment.md`, and **this specification had to
add a clause telling the executor what to do if the two orders differ.**
Three tasks have now worked around it.

**5. What I would have specified differently — A8's method.** §17.2.
One clause — *"compare with `git rev-parse <rev>:<path>`"* — would have
brought A8 inside Amendment H's requirement. **It is the same clause the
previous integration specification carried**, so this is a regression in
the template rather than an oversight in kind.
