# Report — `P2-GOVDEBT-REGISTER-GAP-01` v3: `G-18` landed

    Task ID     P2-GOVDEBT-REGISTER-GAP-01
    Version     v3
    Spec        specs/2026-08-24T0600Z_govdebt-register-gap_v3.md
    Review      reviews/chatgpt/2026-08-24T0600Z_govdebt-register-gap_v3.md
    Base        main @ 9af94a4a11cd06e90ef2d24183565412b4043c6a
    Branch      science/govdebt-register-gap-01
    Outcome     COMPLETE through M5. One entry appended, `G-18`,
                disposition OPEN; the counts table updated to
                OPEN 8 / entries 18.

This report records `M1` through `M5` and nothing later. It names the tested
tree `T` and **is itself the next commit on `T`**; it does not state its own
commit SHA, and it does not state the final tip. `M6b`'s post-commit evidence
is recorded outside this file.

---

## 0. Execution location and worktree identity (Amendment D step 0)

    host                     vm
    working directory        /home/user/2-emergent-gravity
    worktree top level       /home/user/2-emergent-gravity
    git common dir           .git
    shallow repository       false
    worktrees                one; /home/user/2-emergent-gravity
    HEAD before the branch   0b3c85cb158f6aae2dd661054d66bcd1f986878f
                             (science/xi-clar-01-landing)

The branch was cut from the Base commit, not from that HEAD:

    git checkout -b science/govdebt-register-gap-01 \
        9af94a4a11cd06e90ef2d24183565412b4043c6a

## 0a. Base and binding, measured before any write

    git ls-remote origin refs/heads/main
      9af94a4a11cd06e90ef2d24183565412b4043c6a   refs/heads/main

Full-string equal to the Base the specification declares. The repository is
non-shallow, so the suite runs on a valid substrate.

    git ls-remote origin refs/heads/science/govdebt-register-gap-01
      (no ref)

**Rule 18 and Amendment N.** The review carries the line
`**Reviewed specification SHA-256:**` — PRESENT — and the value

    815f67094ea827b07c622936b5a0165945b5a672be19466df60067376e2e5a5c

is the only 64-hex string the review contains; it appears twice, at `:4` and
`:150`, identically. The sha256 of the specification bytes was measured **before
the specification commit** and equals it. The committed bytes were re-measured
after the commit and are unchanged:

    sha256 of the spec bytes, before the commit
      815f67094ea827b07c622936b5a0165945b5a672be19466df60067376e2e5a5c
    sha256 of git cat-file blob HEAD:specs/2026-08-24T0600Z_govdebt-register-gap_v3.md
      815f67094ea827b07c622936b5a0165945b5a672be19466df60067376e2e5a5c
    spec bytes 14745    review bytes 6700

The review artifact carries no pre-committed hash. Its sha256 is recorded for
the first time in its commit message as

    76bffe973bd9d2cabfe63d7f03e135d93ca9ed61ad509cba7d7317c956935fe5

provenance transmitted by the PI in session. Commit order was **specification,
then review, then the entry**, with nothing interleaved:

    637cca73c05ac6e6982c223e107b0605c07cac92  spec(...)
    7a678a8846b50bafd8b3283f401a84b93a1ce640  review(...)
    fd331419947c0999b1a6284399d32c9b57d21911  debt(...)

**Reviewer disposition determination, recorded as issued** and not restated:

    Governance-debt framing                CONCUR
    Disposition                            OPEN
    SPECIFIABLE                            NOT ESTABLISHED
    PI ruling required for debt disposition  NO
    A5                                     DOES NOT FIRE

`A5` therefore did not fire, and the disposition executed is the one the
Reviewer determined.

## 0b. `A1`'s gate on the stopped branch, measured before any write

    git rev-parse 2936e967f7fb893e455547e348243bf49b56aff4
      2936e967f7fb893e455547e348243bf49b56aff4

    sha256 of git cat-file blob 2936e967...:decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md
      0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22
    required by M1(c)
      0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22

Full-string equal. `A1` did not fire on this limb, and every node named in `M1`
was located. The pin is a **commit**, not a branch tip; see §7a for what the
branch tip is now and why the reads are unaffected.

---

## 1. `M1` — provenance extraction, before any write

Every node was extracted with `git cat-file blob <rev>:<path> | sed -n 'A,Bp'`
so the bytes are the source's bytes, not retyped text. Each is reproduced in the
entry inside a fenced block, never a blockquote, so no rendering layer stands
between the entry and the source.

**From the Base, `main @ 9af94a4a11cd06e90ef2d24183565412b4043c6a`:**

    node               path:line                                        bytes  sha256 (first 16)
    M1(a) dispositions docs/GOVERNANCE-DEBT.md:25-31                       405  3859e454e4fc9211
    M1(a) OPEN         docs/GOVERNANCE-DEBT.md:31                           44  50c46651bc76e747
    M1(a) SPECIFIABLE  docs/GOVERNANCE-DEBT.md:26-27                       126  f636c2846fb4cf7d
    M1(a) not closed   docs/GOVERNANCE-DEBT.md:33                           77  dd84626cf82321e4
    M1(a) spec. rule   docs/GOVERNANCE-DEBT.md:34-35                       150  8f58cfc2272a2f2f
    M1(b) nothing binds docs/GOVERNANCE-DEBT.md:3-6                        307  1c31eddd48c6149a
    M1(e) title        derivations/P2-DEFERRED-ITEMS.md:1                   44  720107ce38d440bc
    M1(e) how to tell  derivations/P2-DEFERRED-ITEMS.md:19-26              499  fe846c202545d6de
    M1(e) scope        derivations/P2-DEFERRED-ITEMS.md:191-193            211  59266025bacc8a39
    M1(e) title        derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md:1      56  98753871854e5dc1
    M1(e) scope        derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md:3-5   187  b57c10ceda1ee936
    §0b record 1 title DECISION_LOG.md:2147                                 99  5dcad5957e007e28
    §0b record 1 Reason DECISION_LOG.md:2196-2211                          1030  914f8ddb1218cd60

**From `science/xi-clar-01-landing @ 2936e967f7fb893e455547e348243bf49b56aff4`:**

    M1(c) direction    decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md:32-40   579  a15b2b652ff01216
    M1(d) sweep        reports/2026-08-24T0043Z_xi-clar-01-landing.md:238-246        528  9a84441a2dc1266d
    M1(d) finding (A)  reports/2026-08-24T0043Z_xi-clar-01-landing.md:248             75  —
    M1(d) finding (B)  reports/2026-08-24T0043Z_xi-clar-01-landing.md:261             53  —
    M1(d) finding (C)  reports/2026-08-24T0043Z_xi-clar-01-landing.md:278             75  —

The three `M1(d)` findings are non-contiguous single lines and are quoted as
three separate one-line blocks, each carrying its own line number, rather than
as one block claiming a range the file does not have.

**`M1(d)` is attributed, not adopted.** The register-by-register measurement is
the stop report's own. The entry says so in the sentence that introduces it and
again in its `Evidence` paragraph.

**Nothing was read from the branch tip.** All five branch-side nodes were read
from the pinned commit.

## 2. `M2` — the entry identifier, measured

Measured from the register's own headings at the Base, not from the counts
table, which is itself part of the file and is updated by `M3`:

    ## `G-01` ... ## `G-17`     17 headings, at lines 48, 66, 81, 97, 132, 147,
                                160, 177, 199, 221, 239, 258, 301, 467, 512,
                                564 and 606

A scan for `G-[0-9]+` across the whole file returns one further string, `G-1`,
at `:262-264`. It is **not a member of this register's sequence**, and the file
says so at that place:

```text
Recorded as this specification's `G-1` item. The identifier follows this
register's own two-digit sequence; `G-1` is the specification's label for the
item, not a register ID.
```

It is a cross-reference to another document's numbering, not an entry here.

**The next unused identifier in the register's own sequence is `G-18`.**

The dispositions were measured the same way, from each entry's own
`**Disposition:**` line at `:50, 68, 83, 99, 134, 149, 162, 179, 201, 223, 241,
260, 303, 469, 514, 566, 608`, giving REPAIRABLE 2, SPECIFIABLE 3, NOT
REPAIRABLE HERE 1, RULED 3, METHOD NOTE 1, OPEN 7, total 17 — which is what the
Base counts table declares.

## 3. `M3` — the entry

One entry appended, `## `G-18` — no landed index of the repository's registers
and their stated scopes`, inserted after the last entry `G-17` and before
`## Not entered here — `D4``, which is not an entry.

**Disposition: OPEN**, with the register's disposition definitions quoted in
full from `:25-31` and the OPEN row quoted again on its own from `:31`.
`SPECIFIABLE` is quoted from `:26-27` and explicitly **not** claimed, with the
register's own reading rule from `:34-35` given as the reason.

The gap is stated in the specification's terms and no stronger: the repository
holds no landed index of its registers and their stated scopes; the same
candidate-register reasoning was performed on 2026-08-19 and again on
2026-08-24 by different agents; the second omitted `DECISION_LOG.md`, which the
first had identified and used; and the routing of the item that triggered the
second performance **has since been ruled by the PI, on 2026-08-24, for that
item only**, leaving the indexing gap unaddressed.

The two records of the specification's §0b are set side by side, each quoted
and attributed. Both disclaimer sentences are present: the entry records a
missing mechanism and registers no open item, proposes and creates no register
and expresses no preference; and it is not closed by being written down, with
`:33` quoted for that rule.

**The counts table** is updated to the values measured after the append:

    -    OPEN                  7     G-03  G-08  G-09  G-10  G-13  G-16  G-17
    +    OPEN                  8     G-03  G-08  G-09  G-10  G-13  G-16  G-17  G-18
    -    entries              17
    +    entries              18

**Exactly two pre-existing lines change.** Every other Base byte of the file is
unchanged, verified line by line at `M4`.

## 4. `M4` — post-write verification

    (1) the entry exists with its identifier and disposition
        G-18 heading present                                        PASS
        **Disposition: OPEN.** is the entry's first body line        PASS

    (2) the counts table is consistent with the entry list as
        measured from the file itself — 18 headings, each with its
        own Disposition line, re-measured after the append
        REPAIRABLE           declared 2, listed 2, measured 2       PASS
        SPECIFIABLE          declared 3, listed 3, measured 3       PASS
        NOT REPAIRABLE HERE  declared 1, listed 1, measured 1       PASS
        RULED                declared 3, listed 3, measured 3       PASS
        METHOD NOTE          declared 1, listed 1, measured 1       PASS
        OPEN                 declared 8, listed 8, measured 8       PASS
        entries              declared 18, measured 18               PASS
        row counts sum to the total                                 PASS
        every measured entry appears in exactly one row             PASS

    (3) every quotation is byte-identical to its M1 extraction —
        each extraction tested as a substring of the entry's bytes
        15 multi-line nodes                                         PASS
        3 single-line M1(d) findings                                PASS

    (4) git diff --name-status 9af94a4a..HEAD
        M   docs/GOVERNANCE-DEBT.md
        A   reviews/chatgpt/2026-08-24T0600Z_govdebt-register-gap_v3.md
        A   specs/2026-08-24T0600Z_govdebt-register-gap_v3.md
        exactly the paths this task declares, the report excepted,
        which is this commit                                        PASS

    (extra, Reviewer §11 mutation-boundary discipline)
        Base lines 1-41 identical                                   PASS
        Base line 43 identical (counts-table interior)              PASS
        Base lines 45-644 identical                                 PASS
        the tail from "## Not entered here" identical               PASS
        pre-existing lines changed: exactly 2                       PASS

## 5. `M5` — suite

Run on a full, non-shallow tree, at the Base and at the post-`M3` tree.

**At the Base**, tree `9353d6282cb9bee47a0b64f66eda524f1ef2265b`:

    ........................................................................ [ 20%]
    ........................................................................ [ 41%]
    ........................................................................ [ 62%]
    ........................................................................ [ 83%]
    ........................................................                 [100%]
    344 passed, 2 deselected in 40.22s

**At the post-`M3` tree**, which is `T`:

    T = 0bbc080d3096744e6245c9983c255a8cdbd2d85f

    ........................................................................ [ 20%]
    ........................................................................ [ 41%]
    ........................................................................ [ 62%]
    ........................................................................ [ 83%]
    ........................................................                 [100%]
    344 passed, 2 deselected in 38.54s

Identical outcomes. **No test fails on `T` that passes at the Base.**

---

## 6. Acceptance criteria

    C1  PASS  Every extracted node appears in the entry as a verbatim
              quotation with a path:line that resolves at the Base, or
              at 2936e967f7fb893e455547e348243bf49b56aff4 for those read
              from the stopped branch. Verified as byte-substring
              containment, not by inspection.
    C2  PASS  The identifier is G-18, the next unused one in the measured
              sequence. The disposition is OPEN, the one the Reviewer
              determined, with the register's own definition — none of
              the above — quoted verbatim.
    C3  PASS  Both disclaimer sentences are present, and the gap is
              stated in §0b's terms. The entry nowhere asserts that no
              register admits the item; it records that the routing was
              ruled by the PI for that item only.
    C4  PASS  The counts table is consistent with the entry list measured
              from the file; all quotations are byte-identical to M1; the
              diff shows only this task's declared paths.
    C5  PASS  344 passed and 2 deselected at both the Base and T.
    C6  NOT YET REACHED at this commit. Its measurement is post-commit
              and is recorded outside this file, per M6b.

## 7. Abort conditions

    A1  DID NOT FIRE.  Every M1 node was located, and the clarification's
        sha256 at the pin equals the required value as a full string.
    A2  DID NOT FIRE.  The entry registers nothing. It quotes the
        registration direction as evidence of the occasion and states in
        two places that the registration belongs to the resumed landing
        task under the PI's ruling, not here.
    A3  DID NOT FIRE.  No register and no index is created or proposed,
        no register is named as the general answer for future items, and
        no preference among candidate resolutions is expressed.
    A3b DID NOT FIRE.  No sentence of the entry states or implies that no
        register admits the representation-stability item, or that its
        routing is unresolved. The entry states the opposite of the
        latter: the routing was ruled on 2026-08-24, for that item only.
    A4  DID NOT FIRE.  science/xi-clar-01-landing was read at a pinned
        commit and never written; no ref of that branch moved; no
        authorized or registered inquiry was begun, scheduled,
        constrained or prioritised.
    A5  DID NOT FIRE.  The Reviewer recorded "PI ruling required for debt
        disposition: NO" and "A5: DOES NOT FIRE".

---

## 8. Stops and clarifications (Amendment B)

Nothing stopped execution. Three observations are returned rather than resolved.

### 8a. The specification's §0 describes the stopped branch as it no longer is

**Category: `SPECIFICATION_DEFECT`.** §0's fourth bullet says of this task that
"It does not resume, unblock, or modify `P2-XI-CLAR-01-LANDING`, whose branch
stands where it stopped."

Measured:

    git ls-remote origin refs/heads/science/xi-clar-01-landing
      0b3c85cb158f6aae2dd661054d66bcd1f986878f

    git merge-base --is-ancestor 2936e967... 0b3c85cb...   -> 0 (ancestor)

**The branch does not stand where it stopped.** It advanced, under
`P2-XI-CLAR-01-LANDING` v3, which resumed and completed the task; the stop
commit `2936e967…` remains an ancestor of the tip.

**No read is affected**, because `M1(c)` and `M1(d)` name a **pinned commit**
and not a branch name, and every branch-side extraction was taken from that
commit. `A4` is satisfied on the measurement that matters — no ref of that
branch moved during this task — rather than on the spec's premise.

The observation is returned. The executor does not amend a specification.

### 8b. §0b says the PI's ruling is "quoted at M1"; `M1` names no source for it

**Category: `SPECIFICATION_DEFECT`.** §0b says the PI's 2026-08-24 ruling is
"quoted at M1 and recorded in the resumed landing task, not here". `M1`'s node
list is `(a)` through `(e)` and contains no such node, and `C1` admits
branch-read quotations only for "the two read from it" — `M1(c)` and `M1(d)`.

Measured, over the three revisions this task may read:

    decisions/2026-08-24-xi-open-item-register-routing.md
      at the Base            9af94a4a...   absent
      at the pin             2936e967...   absent
      at the landing tip     0b3c85cb...   present

The ruling record exists at **neither** source `M1` authorises. Quoting it
would require reading a third revision the specification does not name and
would exceed `C1`.

**Resolution taken, and it is the conservative one.** `A1` does not fire,
because the ruling is not a node `M1` names. The entry therefore **states and
attributes** the ruling — "ruled by the PI, on 2026-08-24, for that item only" —
rather than quoting it. Nothing turns on the difference for `A3b`, which the
statement satisfies. If the PI wants the ruling's bytes in the entry, that is a
follow-up specification naming the revision to read.

### 8c. What the entry deliberately does not say about the item's present state

**Category: `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`, recorded for
completeness and not raising a question.** The representation-stability item is,
as of `0b3c85cb…`, in fact registered on the landing branch under the PI's
ruling. That is the resumed landing task's record, not this one's, and the entry
says nothing about it: `A2` forbids this entry to register the item or to read
as registering it, and a sentence reporting the registration's completion would
sit uncomfortably close to that line for a benefit the entry does not need.

The entry says only what §0b's terms allow — that the routing was ruled, for
that item only, and that the indexing gap is where it was.

## 9. Rule 22

No result in this task is `INCONCLUSIVE`. The entry's disposition `OPEN` is a
register disposition, defined by that register at `:31` as *none of the above*;
it is not an `INCONCLUSIVE` verdict and carries no subclass or resolution path,
and this report asserts none.

## 10. Environment

    python      3.11.15
    pytest      9.1.1
    numpy       2.4.6
    sympy       1.14.0
    ruff        0.15.8
    scipy       ABSENT
    repository  non-shallow, verified before each suite run

No environment repair was needed and none was performed. No code changed, so no
linter was run over changed sources; the only modified file is Markdown.

## 11. Push scope

`docs/BRANCHING_POLICY.md` `science/*` scope. **Only
`refs/heads/science/govdebt-register-gap-01` is pushed.** `main` does not move,
`science/xi-clar-01-landing` does not move, and no session or harness branch is
pushed. Integration is a separate task and is not begun, scheduled or
constrained here.

`M6b`'s measurements — the final tip, the diff of that tip against `T`, and the
push result — are post-commit and are recorded outside this report, which is
itself the next commit on `T`.

END OF REPORT
