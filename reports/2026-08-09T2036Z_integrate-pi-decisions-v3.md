# Integration report — the PI decisions v3 replay

Specification: `specs/2026-08-09T2036Z_integrate-pi-decisions-v3.md`
Pre-execution review: `reviews/chatgpt/2026-08-09T2036Z_integrate-pi-decisions-v3.md`
Specification evidence base: `7c5cba5df76de6ef8f52af390ca92100dcdf0d8b`
Source branch: `fix/pi-decisions-v3` @ `93de3218095cafdabcd0fda92abc31af33109879`
Integration branch: `fix/integrate-pi-decisions-v3`
Pre-report head: `d26daab5fba81999e454511a9e575abfeb825bc2` (the merge commit)

**Outcome.** One `--no-ff` merge, no conflict, correct parentage,
merge-base the original base. All five arriving blobs are byte-identical
to their declared values. **`DECISION_LOG.md` satisfies all four
append-only measures**, including the strongest: the base's log is an
exact byte prefix of the merged head's. All 185 pre-existing paths under
the six protected directories are identical. Four validators pass. No
gate, no science, no result changes.

**Four things the Reviewer should read before the detail.**

**(a) §1 is right, and my earlier phrasing was the problem, not my
method.** §5 sets it out plainly: I reported the branch-name difference
rather than normalising it away, but I described the fix instead of
describing the scope, and that invited the reading §1 corrects. **The
structural fact settles it better than my framing did.**

**(b) A2's parentage is now correct, and it closes a loop I opened.** I
flagged at the previous integration that A2's parenthetical lagged §5's
commit order. **This specification fixed it and says so.** §2.

**(c) §2's entry counts and mine differ by denominator, not by fact.**
§7.5. Both are `+3`.

**(d) The V/A junction becomes co-located on `main` for the first time
with this merge**, and I can show that. §12.

---

## 1. A1 — refs, read from the remote

    refs/remotes/origin/main             7c5cba5df76de6ef8f52af390ca92100dcdf0d8b
    remote refs/heads/main               7c5cba5df76de6ef8f52af390ca92100dcdf0d8b
    local  refs/heads/main               0f7961747abe2a18b436c0b1e5b928f425ea4d9a
    remote refs/heads/fix/pi-decisions-v3   93de3218095cafdabcd0fda92abc31af33109879

Both remote `main` refs resolve to the evidence base and the source
branch to `93de3218…`. **Local `main` is stale by design and was not
repaired.** No `main` ref was moved.

**The merge took the pinned remote ref**, fetched immediately before and
confirmed to resolve to `93de3218095cafdabcd0fda92abc31af33109879`.

**`{HHMM}Z` is `2036`**, fixed by commit 1 and reused.

## 2. A2 — merge parentage

    merge commit   d26daab5fba81999e454511a9e575abfeb825bc2
    parent 1       5d0178a157a09bd26a828c8e1f50fc3d8c3ec56e   (commit 2, the review)
    parent 2       93de3218095cafdabcd0fda92abc31af33109879   (the reviewed source branch)
    merge-base     7c5cba5df76de6ef8f52af390ca92100dcdf0d8b   (the original base)

    commit 1       9688c99fce0594d238b0e2b15466f4412c06ea38   (the specification)
    git merge-base --is-ancestor 9688c99… 5d0178a…   ->  exit 0
      commit 1 is an ancestor of parent 1: YES

Read as four distinct values. **Parent 1 is the review commit**, because
§5's order puts the review at commit 2 and the merge at commit 3, and
parent 1 is whatever the merge is made from.

**This closes a loop.** At the previous integration I reported that A2's
parenthetical identified parent 1 as the specification commit while §5's
order made it the review commit, and filed it as an Amendment G
propagation slip. **This specification names the review commit
explicitly, requires commit 1's ancestry to be verified separately, and
records why the earlier version was wrong.** Both are now checked and
both hold.

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
                = 5d0178a157a09bd26a828c8e1f50fc3d8c3ec56e
              attachment = fix/integrate-pi-decisions-v3
      PASS  merge_base
              expected = actual = 7c5cba5df76de6ef8f52af390ca92100dcdf0d8b
      PASS  scope        overall PASS, 5 observed operations, failures []
              base 7c5cba5d…  head 93de3218…  mode exact
                modify  DECISION_LOG.md
                add     derivations/P2-DEFERRED-ITEMS.md
                add     reports/2026-08-09T1958Z_pi-decisions-v3.md
                add     reviews/chatgpt/2026-08-09T1958Z_pi-decisions-v3.md
                add     specs/2026-08-09T1958Z_pi-decisions-v3.md
      PASS  pinned_artifacts
              GATES.md
                dbe797ab53c3748baaf44f59442971e5e48b2c2719542b88e0c2f956fe14fd5f
              scripts/p2_channel_character_layers.py
                b7463a421b29bdd58b4c8736e1bbe53dd0e5283e131db628eee46cbdf36eb994
              CONVENTIONS.md
                e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451

    mode     PRE_MERGE
    overall  PASS

**`GATES.md` and `scripts/p2_channel_character_layers.py` were pinned
deliberately** — §3 names both as subjects of separate open items and §7
forbids touching either, so the prohibition is mechanically checked at
the earliest point rather than only asserted.

**A3's two-SHA requirement is satisfiable.** The `POST_MERGE` config
carries `merge_commit` and `expected_remote_sha` as separate fields.
**No stop was required.** The intended parameters are in §9.

## 4. A5 — this task's pre-execution review, committed unedited before the merge

    reviews/chatgpt/2026-08-09T2036Z_integrate-pi-decisions-v3.md
      committed blob sha256
        75006782b2743275d471775aca4f42cac011c118072260bbd78364a873c82b46
      git blob id
        379c33088548fe8e293742d9ca9910f42387a8e4
      86 lines

**Committed as commit 2, before the merge in commit 3** — Rule 15's
timing clause.

### 4.1 The delimiters were located as whole lines, and the trap was real

A5 requires locating the delimiters **as whole lines, not as first
occurrences of the delimiter string**, and notes the trap has been met
twice. **I verified that it would have fired again:**

    first occurrence of the string "=== REVIEW ARTIFACT BEGINS ==="
      -> line 1, inside the accompanying instruction
    the delimiter as its own line
      -> line 4

    each delimiter occurs exactly once as a whole line: BEGINS 4, ENDS 93

**A first-occurrence search would have matched the instruction, not the
boundary**, for the third time. The whole-line locator found exactly one
of each, and the boundaries were printed and checked before anything was
written.

**This is the recommendation I made at the end of the v3 execution,
adopted.** I proposed fixing the supply convention rather than relying on
my locator; A5 states the rule and the accompanying message repeats it.
**Both now say it, which is why it did not recur.**

### 4.2 What I did to the text

**The delimiter lines and the instruction accompanying them are
excluded**, per A5. Blank lines adjoining the delimiters were dropped and
the file ends with exactly one newline. **No character of the review's
own content was added, removed or altered**, verified by comparing the
committed blob to the extracted text. **No placeholder was resolved in
the body**; the path token was resolved in the filename only.

### 4.3 It corresponds to this specification

Checked rather than assumed. It cites the evidence base
`7c5cba5df76de6ef8f52af390ca92100dcdf0d8b` and the source branch
`93de3218095cafdabcd0fda92abc31af33109879` — both confirmed in §1; it
addresses A2's parentage fix, A4's scope arithmetic, A8's base-absent
exclusions, A9a's metadata separation and the Rule 16 requirement by
name; and it identifies the same V/A junction §12 reports.
**Disposition: APPROVED FOR EXECUTION.**

**Its own limits, honoured.** It lists twelve repository-dependent claims
it did not verify — refs, blob ids, conflict-freedom, merge-base, the
byte-prefix property, §9's structural assertions, protected paths, gate
state, validators, guards, scope and branch preservation — and says they
remain the Executor's obligations. **§1 through §11 are those
executions.**

**Its one non-blocking observation, recorded:** Decision 2 is written as
`eta` in the specification's summary while the programme normally uses
`η`. **I made no change** — the merged entry's own heading reads
``The charge-conjugation phase `eta` is not selected``, arriving exactly
as reviewed, and §7 forbids editing anything that arrives by merge.

## 5. §1 — A4's comparison scope, and my earlier phrasing

**§1 settles this correctly, and the correction is to my wording rather
than to what I did.**

**What I did at the v3 execution:** I reported the seven differing line
pairs before normalisation, showed that A4's stated normalisation left
them differing, and stated that adding a branch-name canonicalisation
would make them identical. **I applied no such canonicalisation**, and
said so — the v3 report's §5.4 reads *"Reported this way, rather than by
extending the function myself, because A4 defines the function for the
register and prescribes only the textual normalisation for the
rulings."*

**What §1 is right about:** describing the difference in terms of *a
normalisation that would remove it* reads as though a criterion had been
extended, even accompanied by a denial. **The better description was
available and I did not use it** — the differing lines are outside A4's
comparison scope entirely.

**§9's structural claim, re-verified here** against a PI-decision entry
at the source branch:

    entry: 78 lines, five ### sections

      ### Decision                    lines  7-34    blockquote lines: 23
      ### Reason                      lines 35-49    blockquote lines:  0
      ### Consequences                lines 50-67    blockquote lines:  0
      ### Related gate                lines 68-72    blockquote lines:  0
      ### Related branch and files    lines 73-78    blockquote lines:  0

    CONFIRMED  '### Related branch and files' is a top-level ### section
               with zero blockquote lines
    CONFIRMED  the ruling text sits in '### Decision' as a blockquote

**So the ruling text and the metadata never overlapped.** A4's ruling
comparison covers the blockquote under `### Decision`; the differing
lines were in a sibling section. **No extra normalisation was needed,
none was adopted, and none is authorised.**

**I applied no branch-name canonicalisation to any comparison in this
task**, per §7.

## 6. A9a — entry metadata, checked separately from any ruling-text comparison

**This is a metadata check. It is not part of any equivalence
comparison**, and no canonicalisation was applied to it.

For each of the three PI-decision entries at the merged head, the
`### Related branch and files` section reads:

    ## 2026-08-09 — Mean-field channel for `P2-PHASE-01`: …
        `fix/pi-decisions-v3`;
        `DECISION_LOG.md`, `derivations/P2-DEFERRED-ITEMS.md`,
        `specs/2026-08-09T1958Z_pi-decisions-v3.md`.

    ## 2026-08-09 — The charge-conjugation phase `eta` is not selected; …
        `fix/pi-decisions-v3`;
        `DECISION_LOG.md`,
        `specs/2026-08-09T1958Z_pi-decisions-v3.md`.

    ## 2026-08-09 — The negative-mass stationary branch is DEFERRED, …
        `fix/pi-decisions-v3`;
        `DECISION_LOG.md`, `derivations/P2-DEFERRED-ITEMS.md`,
        `specs/2026-08-09T1958Z_pi-decisions-v3.md`.

**All three name `fix/pi-decisions-v3` and this execution's
specification path.** The second omits the register, correctly: the `η`
decision has no register entry. **No metadata names a superseded branch
or a superseded specification.**

## 7. A6 and A7 — arriving artifacts, and the four append-only measures

### 7.1 Arriving blobs

Git blob ids at the merged head, compared both to the specification's
declared values and to the source branch:

    DECISION_LOG.md
      04539f26a6bc39367d32f5cd6c6a887a1d05e491   MATCH
    derivations/P2-DEFERRED-ITEMS.md
      33b3a664e0578ded484e31ad7f96f3a2908bcbb1   MATCH
    reports/2026-08-09T1958Z_pi-decisions-v3.md
      885399c243902f46ffa55291e075e029acf789d9   MATCH
    reviews/chatgpt/2026-08-09T1958Z_pi-decisions-v3.md
      eb77adfb19f288df2a64cdf76cb3b4f5a8185fd9   MATCH
    specs/2026-08-09T1958Z_pi-decisions-v3.md
      706cc00f7ce09433ca975af1d943cb08592a6dc4   MATCH

**All five agree with the specification and with the source branch.
Nothing arriving was edited.**

### 7.2 Measure 1 — evidence base to merged head

    git diff --numstat 7c5cba5d… d26daab5… -- DECISION_LOG.md
      256     0       DECISION_LOG.md

    deleted lines across the whole base-to-head diff:  0

### 7.3 Measure 2 — merge commit against PARENT 1 (`5d0178a1…`)

    256     0       DECISION_LOG.md          deletions: 0

**This establishes that the integration deleted none of the base's
log.** Parent 1 carries the base's `DECISION_LOG.md` unchanged — commits
1 and 2 add only a specification and a review — so the 256 added lines
are exactly the source branch's entries arriving.

### 7.4 Measure 3 — merge commit against PARENT 2 (`93de3218…`)

    (empty numstat)                          deletions: 0

**This establishes that the merge dropped none of the branch's
entries.** An empty numstat is stronger than zero deletions: the merged
`DECISION_LOG.md` is *identical* to the source branch's.

### 7.5 Measure 4 — the byte-prefix property

    the base's DECISION_LOG.md is an EXACT BYTE PREFIX of the merged head's:
      True
    appended characters: 10605

**This is the strongest of the four and it survived the merge**, as §2 of
the specification expected. It rules out a class the zero-deletion diffs
do not: a log rewritten into an equivalent final state rather than
genuinely extended.

**On the entry counts.** §2 states entries went `29 → 32`; I measured
`27 → 30`. **Both are correct and count different things:**

    ^## 20   dated entries            base 27  ->  head 30
    ^##      all top-level headings   base 29  ->  head 32

The two extra headings are `## Entry template` and
`## YYYY-MM-DD — Decision title`, the file's template block. **The
difference is `+3` either way**, which is the quantity that matters.
Recorded because §2 is a specification claim I re-verified, and a reader
comparing the two numbers should not read a discrepancy into them.

## 8. A8 and A9 — protected paths and gates

    GATES.md                                  bd48205…  IDENTICAL
    CONVENTIONS.md                            0db56c39…  IDENTICAL
    AGENTS.md                                 5e60b5f…  IDENTICAL
    pyproject.toml                            9fc6fdd…  IDENTICAL
    scripts/p2_channel_character_layers.py    68ba9bb…  IDENTICAL

**Every path under `scripts/`, `results/`, `tests/`, `derivations/`,
`docs/` and `reviews/` that exists at the evidence base**, enumerated
from the base and compared one by one — **not as tree objects**:

    185 pre-existing paths checked, 0 differ

**The three base-absent authorised paths A8 does not compare**, listed
so the exclusion is explicit rather than silent:

    A   derivations/P2-DEFERRED-ITEMS.md                              (arriving)
    A   reviews/chatgpt/2026-08-09T1958Z_pi-decisions-v3.md           (arriving)
    A   reviews/chatgpt/2026-08-09T2036Z_integrate-pi-decisions-v3.md (authored here)

**No existing review record was modified or back-filled.**

**`GATES.md` and `scripts/p2_channel_character_layers.py` are byte-identical**
and were additionally pinned by digest in the guard. **The SI-1
cross-reference was not added and Amendment L's known instance is
untouched.**

**A9 — no gate changed.** `GATES.md` blob-identical, `^## P2-` anchor
count **14 before and 14 after**, `P2-GAP-01` still
`Status: PASS (continuum exact; lattice I_0 agrees with paper at matched
mass)`, `P2-PHASE-01` still `Status: PROPOSED`.

## 9. A4 — scope, and the intended final `POST_MERGE`

### Intended final manifest

    base: 7c5cba5df76de6ef8f52af390ca92100dcdf0d8b
    head: <the report commit, computed after this file is committed>
    mode: exact
    required:
      add     derivations/P2-DEFERRED-ITEMS.md
      add     reports/2026-08-09T1958Z_pi-decisions-v3.md
      add     reports/2026-08-09T2036Z_integrate-pi-decisions-v3.md
      add     reviews/chatgpt/2026-08-09T1958Z_pi-decisions-v3.md
      add     reviews/chatgpt/2026-08-09T2036Z_integrate-pi-decisions-v3.md
      add     specs/2026-08-09T1958Z_pi-decisions-v3.md
      add     specs/2026-08-09T2036Z_integrate-pi-decisions-v3.md
      modify  DECISION_LOG.md
    optional: []
    forbidden_operations: [delete, rename, copy, type_change, unmerged, unknown]

**7 additions and 1 modification.** Four arrive from the branch; three
are authored here. **A ninth path would be a defect.**

### Observed at the pre-report head

`git diff --name-status 7c5cba5d… d26daab5…`, seven paths, this report
not yet existing:

    M   DECISION_LOG.md
    A   derivations/P2-DEFERRED-ITEMS.md
    A   reports/2026-08-09T1958Z_pi-decisions-v3.md
    A   reviews/chatgpt/2026-08-09T1958Z_pi-decisions-v3.md
    A   reviews/chatgpt/2026-08-09T2036Z_integrate-pi-decisions-v3.md
    A   specs/2026-08-09T1958Z_pi-decisions-v3.md
    A   specs/2026-08-09T2036Z_integrate-pi-decisions-v3.md

### Intended final `POST_MERGE` parameters

    mode                   POST_MERGE
    merge_commit           d26daab5fba81999e454511a9e575abfeb825bc2
    expected_parent_1      5d0178a157a09bd26a828c8e1f50fc3d8c3ec56e
    expected_parent_2      93de3218095cafdabcd0fda92abc31af33109879
    expected_merge_base    7c5cba5df76de6ef8f52af390ca92100dcdf0d8b
    scope_manifest         the final manifest above
    pinned_artifacts       GATES.md, scripts/p2_channel_character_layers.py,
                           CONVENTIONS.md, as PRE_MERGE
    remote_check_policy    REQUIRED
    expected_remote_ref    refs/remotes/origin/main
    expected_remote_sha    <the report commit head>

**Two distinct SHAs in two distinct fields.** **The final guard result is
post-report evidence.**

## 10. A10-pre — validators at the pre-report head

Run individually with `python -m pytest <path>`, that exact invocation,
since `pytest` on this host resolves to 9.0.2 while `python -m pytest`
resolves to 9.1.1.

    tests/test_repository_structure.py    exit=0    4 passed
    tests/test_si1_governance.py          exit=0   14 passed
    tests/test_gate_anchors.py            exit=0   18 passed, 2 deselected
    tests/test_governance_tools.py        exit=0    8 passed

`pytest 9.1.1`, Python 3.11.15. **Under Rule 14** each is a PASS on the
full contract: the process started, completed without timeout or external
termination, returned exit 0, and no test, collection or teardown phase
was skipped or aborted. The two deselections are the file's own marker
configuration, present identically at the base. **A10-final at the pushed
head is post-report evidence.**

## 11. A11 and A12 — hygiene, commits, and branch preservation

### 11.1 Commit-message hygiene

Every message was written to a file, inspected for `Co-Authored-By`,
`Claude-Session`, `claude.ai`, `Generated with` and `http` **before**
committing, committed with `git commit -F <file>` and never `-m`, and
the stored message read back from the object afterwards.

    commit 1   9688c99…   trailers suppressed: Co-Authored-By, Claude-Session
    commit 2   5d0178a…   trailers suppressed: Co-Authored-By, Claude-Session
    commit 3   d26daab…   trailers suppressed: Co-Authored-By, Claude-Session
               (the merge; committed via --no-commit then -F)

**Suppression is a fact to disclose, not an absence.**

**Commit 1** — `9688c99fce0594d238b0e2b15466f4412c06ea38`, committed
content sha256
`625eea42a634000881d34cc195c7b3aeb3bf37a40d07ed179012fdcaea6c5d1b`
(recorded because **Rule 4** requires the execution prompt committed
*and* its digest in the report):

    spec: integrate the PI decisions v3 replay

    Verbatim transcription of the PI specification authorizing the
    integration of fix/pi-decisions-v3 at 93de3218.

    Rules 1-17 are in force at the evidence base, so this task is governed
    by Rule 15 and its pre-execution review is committed as commit 2, before
    the merge proceeds. A2 identifies the review commit as merge parent 1,
    which is the structural propagation Rule 15's insertion requires.

**Commit 2** — `5d0178a157a09bd26a828c8e1f50fc3d8c3ec56e`:

    review: pre-execution review of the PI decisions v3 integration

    The Reviewer's approval of
    specs/2026-08-09T2036Z_integrate-pi-decisions-v3.md, committed unedited
    before the merge proceeds, as Rule 15 requires.
    Disposition: APPROVED FOR EXECUTION.

    The executor did not write, edit, summarise or reformat it. The
    delimiters were located as whole lines, not as first occurrences of the
    delimiter string, so the accompanying instruction that names them was
    not mistaken for the boundary. The delimiter lines and that instruction
    are excluded.

    The review records what it could not verify and states that those remain
    execution-time obligations of the Executor.

**Commit 3, the merge** — `d26daab5fba81999e454511a9e575abfeb825bc2`:

    merge: integrate the PI decisions v3 replay (reviewed; pinned 93de321)

    Merges fix/pi-decisions-v3 at 93de3218095cafdabcd0fda92abc31af33109879,
    reviewed and unmodified.

    Brings three PI decisions of 2026-08-09 and the deferred-items register,
    replayed on the current authoritative base after the earlier execution
    lost conflict-free integrability. Decision 1 selects the scalar channel
    with a real auxiliary field as a choice of direct route, not a judgement
    that the V/A representation is wrong; Decision 2 declines to select eta
    and computes both signs; Decision 3 defers the negative-mass branch
    without admitting or excluding it.

    derivations/P2-DEFERRED-ITEMS.md records DEFERRED-01, DEFERRED-02 and
    DEFERRED-03, the last carrying Evidence: none and marked UNTESTED.

    None of the three is a physics result. OPEN-AC-1 is not closed, eta is
    not selected, the negative-mass branch is not classified, and the V/A
    representation was not set aside on physical grounds - DEFERRED-01's PI
    position is that it may contain physically relevant information and must
    be returned to.

    DECISION_LOG.md arrives append-only and the base remains an exact byte
    prefix of it. DEFERRED-02's consequence for the SI-1 kill criterion is
    unresolved and GATES.md still does not reference the register; that
    cross-reference is a separate task. No gate status changes and no
    science or result is affected.

**Intended report commit message**, prepared the same way with the same
two suppressed:

    docs: report the integration of the PI decisions v3 replay

    Records one --no-ff merge of fix/pi-decisions-v3 at 93de3218, with
    parent 1 the pre-execution review commit, commit 1 verified as its
    ancestor, and the original base as merge-base. All five arriving blobs
    are byte-identical. DECISION_LOG.md satisfies all four append-only
    measures, including the base remaining an exact byte prefix of the
    merged head.

    Reports A9a's metadata check separately from any equivalence
    comparison, applies no branch-name canonicalisation anywhere, and
    records that the differing lines the v3 report described were outside
    A4's comparison scope rather than requiring an extension to it.

    Reports that the V/A junction becomes co-located on main for the first
    time with this merge, and that nothing in the merged state asserts the
    V/A sector was set aside on physical grounds.

### 11.2 A12 — branches preserved

Read from the remote:

    fix/pi-decisions-v3               93de3218095cafdabcd0fda92abc31af33109879
    fix/pi-decisions-v2               ebd531ab568aaffabd86a4a94d925a711e62aa36
    fix/pi-decisions-and-deferred     52f651174dc1fef03b4fb9276078fa1f08d94bd7
    review/role-model-and-executors   10c260b96882ac12610f78840aeeabd07be2d7cb

**All four at their recorded values.** The post-push re-verification is
post-report evidence. **No branch was deleted, nothing was force-pushed,
and no history was rewritten.**

## 12. §6 — the Rule 16 assessment

**Rule 16 is operative and governs this task.**

### 12.1 The junction, named — and it is new to `main` with this merge

**§3 offers the V/A junction as the leading candidate. I confirm it, and
I can now show something §3 does not claim: this merge is what makes it
available on the authoritative branch.**

    results/P2-PHASE-01/channel-character-layers/layers.json
      PRESENT at the evidence base — the induced V and A singlets are
      REPULSIVE with no real linear HS contour
    DECISION_LOG.md, the scalar-channel decision
      ARRIVES with this merge
    derivations/P2-DEFERRED-ITEMS.md, DEFERRED-01
      ABSENT at the evidence base; ARRIVES with this merge

**Verified**: `git cat-file -e 7c5cba5d:results/…/layers.json` succeeds;
the same command for `derivations/P2-DEFERRED-ITEMS.md` fails. **The
three artifacts have never been on one branch before.**

**The inference their combination makes available:** *the V/A sector was
examined and set aside on physical grounds.*

**It was not.** The deferral is about which machinery exists — the
programme's apparatus is built for a real auxiliary field — and
`DEFERRED-01`'s own PI position, now on `main`, says the opposite:

> **PI position.** The V/A representation may contain physically relevant
> information and must be returned to. **No evidence indicates it is
> unphysical.**

**This is Rule 16's own stated reason for splitting the obligation
between the producing task and the integrator** — the strongest
misleading inference is sometimes available only once separate branches
sit on one `main`. **This is an instance of exactly that, and it is the
first one the programme has produced.**

### 12.2 The second candidate, and why I do not rank it above the first

§6 also offers: four executions of this task now exist, each preserved,
and a reader could take four executions for four substantive revisions.
**It was revised once on substance** — the v3 report's §13.1 measured
each transition, and only `59c763ab → 52f65117` changed the decisions.

**I do not report it as the stronger one.** It concerns how to read the
repository's history; the V/A junction concerns how to read its physics,
**and only the second is something a downstream paper could act on.**

### 12.3 What the assembled set does NOT establish

1. **That the V/A representation was rejected on physical grounds.**
   §12.1.
2. **That any of the three decisions is a physics result.** §13.
3. **That `DEFERRED-02`'s consequence is resolved.** The SI-1 kill
   criterion's quantifier range remains undetermined, `GATES.md` still
   does not reference the register, and that cross-reference is a
   separate task.
4. **That Decision 2 has been acted on.** It authorizes a two-sign
   diquark calculation that has not been performed and that §7 forbids
   here.

## 13. Does the merged state read as though any decision were a physics result, or as though V/A were physically excluded?

**No, and I searched rather than asserting it.**

I searched the merged tree for any statement that the V/A sector is
excluded, unphysical, ruled out, rejected, or set aside on physical
grounds — excluding `reports/`, `specs/`, `reviews/` and
`docs/amendments/`, which discuss the risk by design. **One hit, and it
is the disclaimer:**

    DECISION_LOG.md:1773
      > **No evidence indicates the V/A representation is unphysical, and the
        PI's position is that it may contain physically relevant information
        and must be returned to. It is deferred, not excluded** …

**Each decision carries its own limit in its own text**, arriving exactly
as reviewed:

    Decision 1   "a choice of direct route, not a judgement that the V/A
                 representation is wrong"; "This does not close
                 OPEN-AC-1"
    Decision 2   declines to select η; "the programme evaluates both …
                 rather than selecting between them"
    Decision 3   "DEFERRED, not excluded"; "they do not establish full
                 condensate-space stability, phase admissibility, or
                 absence of physical content"

**`DEFERRED-03` carries `Evidence: none` and `PI HYPOTHESIS, UNTESTED`**,
so it cannot be read as carrying support comparable to the two
evidence-backed entries.

**Nothing in the merged state states or implies a physics result.** The
risk §3 identifies is an *assembled* reading, not a claim anyone made —
which is why it belongs in a Rule 16 assessment and not in a correction.

## 14. Worktree states, stated separately

**The merge worktree**, `<scratch>/integ10`: created from `7c5cba5d…`
for this task, attached to `fix/integrate-pi-decisions-v3`, clean at the
pre-report head `d26daab5…`. The `PRE_MERGE` guard's `worktree_clean`
check confirmed it independently before the merge.

**The primary worktree**, `/home/user/2-emergent-gravity`: on
`gate/p2-grassmann-crossing-sign` at `cf4c789`, **zero modified or
untracked entries, and not touched by this task.**

No other worktree was altered. Nothing was cleaned, stashed or
discarded.

## 15. Stops and clarifications

**No stop occurred.** No conflict arose and every check passed.

### `SPECIFICATION_DEFECT`

**None.** The two defects the specification itself records as fixed —
A2's parentage and A8's base-absent ambiguity — are both correct in the
issued text, and §2 and §8 execute the corrected forms.

### `ENVIRONMENT`

None. Nothing was installed.

**No environment failure occurred, so neither of Rule 13's two
diagnostic orders was exercised.** §7 asks me to say that rather than
name one; naming one would assert a procedure I never ran.

### `OBSERVATION_METHOD_ERROR`

**None, and the one that has recurred twice did not recur.** §4.1: the
whole-line locator was used from the outset, and I verified that a
first-occurrence search would still have matched the instruction. **The
fix was in the specification and in the supply message, not only in my
method** — which is what stopped it.

### `REPOSITORY_DEFECT`

None.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`

**None that blocked.** One recorded for completeness: the review's
`eta`-versus-`η` observation (§4.3). **I made no change**, because the
merged entry arrives exactly as reviewed and §7 forbids editing arriving
content. **If the heading is ever to read `η`, that is a change to the
source branch's content and needs its own authorization.**

## 16. Secondary findings, and what I would have specified differently

**1. My v3 phrasing is the finding I would most want carried forward.**
§5. I applied no unauthorised normalisation and said so — **but I
described a difference by naming the transformation that would remove it,
which reads as an extension even when accompanied by a denial.** The
better description was structural and was available: the lines were
outside the comparison's scope. **The lesson is about how to report a
difference, not about what to do with one.**

**2. Two recommendations I made have now landed and worked.** The
whole-line delimiter rule (§4.1) and A2's parentage propagation (§2) were
both raised in earlier reports and both are fixed in this specification.
**Recorded because the loop closing is worth as much as the finding
was.**

**3. `DEFERRED-02`'s `Blocks:` line is now on `main` and still
unreferenced from `GATES.md`.** It has survived four executions and one
integration. **`GATES.md` is protected in every one of these
specifications**, so the cross-reference cannot happen as a side effect;
it needs its own authorization, and it now has a permanent home to point
at.

**4. Amendment L's obligation still has no assignee**, and §8 confirms
`scripts/p2_channel_character_layers.py` is untouched. Raised at the E–L
landing, its integration, and the v3 replay; unchanged.

**5. What I would have specified differently — A6 should say which entry
count it means.** §7.5. `29 → 32` and `27 → 30` are both right, and the
difference is the two template headings. **One word — "dated entries" or
"top-level headings" — would remove the need for a reader to reconcile
them.**
