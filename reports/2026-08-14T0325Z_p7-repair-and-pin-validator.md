# Execution report — repair `P7`, forbid the vacuous pass, and validate the gate pins

**Specification:** `specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md`
**Specification evidence base:** `88ef5eec08ab269eddcea8c617cf4f5b09b7336e`
**Branch:** `governance/p7-repair-and-pin-validator`, cut from authoritative `main` @ `88ef5eec…`
**Classification:** MATERIAL. Governed by Rule 15 and Rule 18.

**Every figure below is labelled MEASURED or INTENDED.** **This report is
written at commit 4 and measures nothing at commit 5.**

**This task does not touch `main`.** Integration is a separate task.

---

## 1. Outcome

**All three repairs are in, and the one measurement that decides the task
came out right.**

**MEASURED, and it is the criterion this task exists to satisfy:** `P7` over
this task's own range returns `PASS` with **`section_count_base` 14 and
`section_count_head` 14**, against **`raw_heading_count` 14 at both**. **Not
zero over zero.** **This is the first task in this repository in which a
`P7` result means anything.**

    grammar        raw '^## P2-' 14   old grammar parsed 0   new grammar parsed 14
    invariant      the old code returns PASS at 14 parsed of 15 raw; the new returns NOT_PARSEABLE
    pin validator  2 pins at the evidence base, both matching; fails on mismatch, on zero pins,
                   and on a pin with no resolvable path
    suite          280 -> 301 passed, 2 deselected, delta +21
    stale tree     pre-repair suite: 280 passed, exit 0.  repaired suite: 1 failed, 300 passed.

**`GATES.md` is byte-identical at base and head** — `2b3bd5069414f009e1a0466c4990db2949519bd8`
at both. The file is read by everything this task built and modified by none
of it.

**A11, answered before it is asked.** My harness's standing git guidance does
instruct a `Co-Authored-By` trailer and a session URL. **None was written on
any of the five commits**, nothing was suppressed by amendment, and no commit
was amended. **`F1` is live and unrepaired**; §13 reports it.

---

## 2. Refs and inputs — A1, MEASURED

    refs/heads/main    88ef5eec08ab269eddcea8c617cf4f5b09b7336e    as specified, read from the remote

**Blob ids at the evidence base:**

    GATES.md                                              2b3bd5069414f009e1a0466c4990db2949519bd8
    scripts/governance_tools/task_checker.py              1922fe88f3a29909a006b2adf03cfb5229d20d84
    tests/test_task_checker.py                            a68568568f50b2bfbccbcbe4f87bcd70b55b6423
    derivations/GOVERNANCE-ENFORCEMENT_classification.md  183df9468c986fd8ba4cd5c2ecaf95ee1561adb4

**No ref mismatch. No stop.** The `task_checker.py` blob is
`1922fe88…`, the same blob §9 of the specification names as the source of the
verbatim `P1` parser, so the pre-issue record and this execution read the same
file.

---

## 3. The pre-execution review — A2 and §3, MEASURED

**It arrived as a FILE, not pasted**, and was committed byte-unchanged.

    supplied specification    e925f074d81af4ed11e32be371aaa6d3dbce2e8d76b7e5c22d1a432d2fe34dd2
    committed specification   e925f074d81af4ed11e32be371aaa6d3dbce2e8d76b7e5c22d1a432d2fe34dd2   equal
    supplied review           96e57ee4a43a82d45dc277fa7dff115501776e886b1084025e22887ff58eac6d
    committed review          96e57ee4a43a82d45dc277fa7dff115501776e886b1084025e22887ff58eac6d   equal

The review's `reviewed specification SHA-256:` field is filled in and reads
`e925f074d81af4ed11e32be371aaa6d3dbce2e8d76b7e5c22d1a432d2fe34dd2` — **the
digest of the specification actually committed and executed.** Not blank, not
a different specification.

---

## 4. The grammar — A3, MEASURED on the real file

**Both counts from the same file, `GATES.md` at the evidence base:**

    raw lines matching '^## P2-'                    14
    NEW grammar (GATE_HEADING at head) matched      14
    OLD grammar (GATE_HEADING at 88ef5eec) matched   0

**The fourteen ids found, in file order:**

    1   P2-HK-01                       8   P2-BETAV-RECON-01
    2   P2-GAP-01                      9   P2-BETAV-ASSEMBLY-01
    3   P2-BETA-01                    10   P2-CHANNEL-FREEZE-01
    4   P2-BETAV-01                   11   P2-PHASE-01
    5   P2-NORM-01                    12   P2-MULTIPHASE-GRAV-01
    6   P2-BETAV-CIRC-01              13   P2-GRAV-ENGINE-RECOVERED-01
    7   P2-BETAV-NUMREPRO-01          14   P2-LATTICE-ONTOLOGY-01

**Duplicates: none.** **Fourteen was expected and fourteen is what I got.**

### 4.1 The separator, defined and stated

**Every one of the fourteen headings uses U+2014 EM DASH**, measured by
decoding the character after the id and reading its Unicode name. **Zero
headings are bare.**

**The grammar accepts three separators:**

    U+2014  EM DASH         —     the character all fourteen real headings use
    U+2013  EN DASH         –     accepted so a reasonable author is not silently unread
    U+002D  HYPHEN-MINUS    -     likewise

    GATE_HEADING = re.compile(r"^## (P2-[A-Z0-9-]+)[ \t]+[—–-][ \t]+\S.*$")

**A non-empty title is REQUIRED**, and horizontal whitespace is required on
both sides of the separator. **The id is unambiguous even with a hyphen
separator**, because the mandatory whitespace prevents the greedy
`[A-Z0-9-]+` from absorbing it.

### 4.2 What the grammar rejects that a reasonable author might write

**Stated, because it is the cost of the choice and not a detail:**

    ## P2-ALPHA-01                     rejected — a bare id with no title
    ## P2-ALPHA-01 —                   rejected — a separator with no title
    ## P2-ALPHA-01: Title              rejected — a colon separator
    ## P2-ALPHA-01 -- Title            rejected — a double hyphen
    ## P2-alpha-01 — Title             rejected — a lowercase id
    ###  P2-ALPHA-01 — Title           rejected — not an H2

**The bare form is rejected DELIBERATELY, and I state it here as §1(a)
requires.** It is the one shape the pre-repair grammar did match, and **no
heading in `GATES.md` has ever used it.** A registry written that way now
reports that it could not be read, rather than parsing quietly into a shape
that resembles the real file but is not it. **It is fixtured** —
`test_gate_grammar_rejects_the_bare_heading_the_old_grammar_accepted` asserts
each accepted and each rejected form above.

**Every rejection above is safe rather than silent**, and that is the point
of the design: **a rejected heading is still counted by `RAW_GATE_HEADING`**,
so it breaks the equality and surfaces as `NOT_PARSEABLE` with the offending
line quoted in `unrecognised_headings_base` / `_head`. **The grammar can only
make `P7` refuse to judge; it cannot make `P7` judge wrongly, and it cannot
make it pass.**

---

## 5. The completeness invariant — A4, demonstrated against the OLD code

**The old checker was extracted VERBATIM from the evidence-base blob and
executed — not re-implemented.**

    git show 88ef5eec:scripts/governance_tools/task_checker.py
    sha256 of the extracted file  0ad668bd416dc8e26291bcddaa8a766363c61bb173c3df0769517c9158dfed98

Only the import line was redirected to a shim supplying `blob` and
`path_exists_at_revision` over in-memory fixtures. **`GATE_HEADING`,
`gate_sections` and `check_p7` are the landed code, untouched.**

**Reported per fixture, not in aggregate.**

### Fixture 1 — the `0 / N` case: the real `GATES.md`, 14 raw headings, grammar matches none

    OLD code status                PASS
    section_count_base / head      0 / 0
    raw '^## P2-' headings         14

**This is the repository's actual defect, reproduced against the actual
file.** The old code returns `PASS` over zero parsed sections drawn from
fourteen real headings.

    NEW code on the same input     NOT_PARSEABLE

### Fixture 2 — the `14 / 15` case, and it is the one that matters

**My first construction of this fixture was wrong and I discarded it.** I
built fifteen headings in the real em-dash shape plus one bare, which the old
grammar reads as **1 of 15**, not 14 of 15 — a `1 / N` case wearing a `14 /
15` label. **A fixture that does not put the old code in the state the
criterion names is not testing the repair**, which is exactly what A4 warns
about, so I rebuilt it in the old grammar's own terms.

**The true `14 / 15` fixture:** fourteen headings in the bare shape the old
grammar reads, plus `## P2-lower-01`, which it cannot.

    raw '^## P2-' headings         15
    OLD grammar parses             14
    OLD code status                PASS
    section_count_base / head      14 / 14

**The old code returns `PASS` while one of fifteen gates is invisible to
it.** **A guard that fired only at zero would not have caught this**, and
that is why the invariant compares for equality.

    NEW code on the same input     NOT_PARSEABLE
    reason                         parsed gate sections do not equal the independently
                                   counted '## P2-' headings

**Neither fixture is one the pre-repair code gets right**, as §1(d)
requires.

### 5.1 Raw and parsed counts, and what the invariant compares

**MEASURED at base and at head of this task's range:**

    raw_heading_count_base   14        section_count_base   14
    raw_heading_count_head   14        section_count_head   14

**The invariant compares these for EQUALITY, not for non-zero.** The
implemented condition is

    if len(before) != len(raw_base) or len(after) != len(raw_head):
        return NOT_PARSEABLE

evaluated **before** the authorised-set comparison, so **no arrangement of
the authorised set and no identity between base and head can reach a `PASS`
through an incompletely read registry.** A separate, earlier branch returns
`NOT_PARSEABLE` when either raw count is **zero**.

**`RAW_GATE_HEADING = re.compile(r"^## P2-")` is written independently of
`GATE_HEADING`** — a prefix test, not the grammar. **A guard expressed
through the parser it protects would fail together with it**, which is the
whole reason the count is taken over a cheap independent signal.

**One case the invariant catches that the specification did not name.** A
**duplicate gate id** collapses in the section map, so raw and parsed differ
with nothing unrecognised. The evidence therefore reports
`duplicate_ids_base` / `_head` alongside `unrecognised_headings_*`, so a
reader of a `NOT_PARSEABLE` can tell the two causes apart. **`GATES.md` has
no duplicate id today** — measured, 14 ids, 14 distinct.

### 5.2 `NOT_PARSEABLE`, not `FAIL`

**Fixed here as the specification fixes it.** The state means *the grammar
cannot fully read the gate registry*, **not** *an unauthorised gate change
has been shown*. **Cannot judge is not judged wrong** — the distinction `P1`
already carries. It still lands in `NON_GREEN`, so the run is `INCOMPLETE`
and the exit status is non-zero; a fixture asserts exactly that.

---

## 6. The pin validator — A5, three separate runs

**Path: `tests/test_gate_pins.py`, as §4 fixes it. I judged no other
location and relocated nothing.**

**How it locates the artifact path.** For each `` (sha256 `<64 hex>`) ``
occurrence it scans the pin's own line and the **three lines above it** for a
repository-relative path under one of `derivations/`, `scripts/`, `results/`,
`docs/`, `paper/`, `tests/`, in backticks or bare. The root list and the
three-line window are both deliberate: a wider net would let an incidental
path-like string in the prose bind to a pin, and a longer window would let a
pin whose path is missing silently attach to an unrelated path further up.

**What it does when a pin has no resolvable path: it FAILS.** Not skipped —
`test_every_pin_resolves_to_a_path` collects them and asserts the list is
empty. **A pin nobody can trace to a file is exactly as unchecked as a pin
that was never verified.**

### Run (i) — against `GATES.md` at the evidence base

    python -m pytest tests/test_gate_pins.py -q
    11 passed in 1.16s

    pin 1   GATES.md line 1017   derivations/P2-PHASE-01_microscopic_parameter_domain.md
            4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214    MATCH
    pin 2   GATES.md line 1040   derivations/P2-PHASE-01_input_admissibility_contract.md
            e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3    MATCH

**Expected pass, two pins, both matching. That is what happened.**

### Run (ii) — a fixture whose pin does not match

Built in a disposable temporary directory holding only `tests/test_gate_pins.py`
and a synthetic `GATES.md`. **Failure message, verbatim:**

    E       AssertionError: GATES.md line 2: derivations/thing.md is stale -- pinned bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb, measured 73cb3858a687a8494ca3323053016282f3dad39d42cf62ca4e79dda2aac7d9ac

    FAILED tests/test_gate_pins.py::test_every_pinned_artifact_matches_its_pin
    1 failed, 10 passed in 0.53s

**It failed, and it failed for the right reason** — the digest comparison,
naming the pin, the path, the declared value and the measured value.

### Run (iii) — a fixture with zero pins

**Failure message, verbatim:**

    E       AssertionError: no `(sha256 `<64 hex>`)` pin found in GATES.md: either the pins were removed or the notation changed, and in both cases this validator is checking nothing
    E       assert []

    FAILED tests/test_gate_pins.py::test_pin_set_is_not_empty
    1 failed, 10 passed in 0.56s

**It failed on the empty pin set**, which is the defect `P7` carried, one
level along.

### Run (iv) — a pin with no resolvable path, reported because §1(d) lists it

**Failure message, verbatim:**

    E       AssertionError: GATES.md line 5: pin cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc names no artifact path within 3 lines above it

    FAILED tests/test_gate_pins.py::test_every_pin_resolves_to_a_path
    1 failed, 10 passed in 0.06s

**Failed, not skipped.**

**All four temporary fixture directories were removed.** They were plain
scratch directories outside the repository, never committed, and never inside
the task branch's working tree.

---

## 7. The suite now distinguishes what it could not — A6

**Where the temporary tree was created:**

    /tmp/claude-0/-home-user-2-emergent-gravity/30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/a6-worktree

**A DETACHED temporary git worktree at commit 3**, created with
`git worktree add --detach`. **It is not the task branch's working tree.**

**A method correction, self-caught, reported because it changed the
measurement.** My first attempt copied the working tree and deleted `.git` to
guarantee nothing could be committed from it. **That broke six unrelated
tests that require a git repository**, and the run came back `7 failed` —
six of them artifacts of my own instrument. **A measurement whose failures
are mostly caused by the apparatus does not establish what A6 asks.** I
discarded that tree and used a detached worktree, which the specification
explicitly permits and which keeps git available.

**Baseline first, in the same tree, before anything was made stale:**

    python -m pytest    ->    301 passed, 2 deselected

**Then one pin made stale**, by appending a line to the pinned artifact
`derivations/P2-PHASE-01_input_admissibility_contract.md`. **`GATES.md`
itself was not edited** — `git diff --name-only -- GATES.md` in that tree
returned 0 paths, so the pin's declared value is the landed one and only the
artifact moved.

    pinned artifact now hashes to   96479d2f1e2dc6a083d368f022913b3651eb21a6a0437d9b465ba622f27dcb11
    GATES.md still declares         e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3

**The command named by A6, run from that tree's root, not a narrower
selection:**

    python -m pytest

    FAILED tests/test_gate_pins.py::test_every_pinned_artifact_matches_its_pin
    1 failed, 300 passed, 2 deselected in 29.14s

**It FAILS. Pass count 300, deselect count 2, exactly one failure, and it is
the pin validator.**

### 7.1 The counterfactual, measured rather than quoted

**A6's claim is that the suite could not previously make this distinction.
Rather than cite the four earlier reports for that, I measured it.** A second
detached worktree at the evidence base `88ef5eec…` received **the same
one-line staleness**:

    python -m pytest    ->    280 passed, 2 deselected in 27.92s    exit 0

**The pre-repair suite reports green over a stale pin.** Side by side:

    same stale pin, pre-repair suite    280 passed, 2 deselected    exit 0
    same stale pin, repaired suite      1 failed, 300 passed, 2 deselected

**That is the distinction the task exists to create, and it is now a measured
pair rather than an inference from an unchanged count.**

**Both temporary worktrees were removed** with `git worktree remove --force`,
and their removal was verified. **Neither was ever committed.** **No byte of
the task branch's working tree was altered for either measurement** —
`git status --short` on the task branch is empty, verified after removal.

---

## 8. Scope — A7

**MEASURED at commit 4:**

    M  derivations/GOVERNANCE-ENFORCEMENT_classification.md
    A  reviews/chatgpt/2026-08-14T0325Z_p7-repair-and-pin-validator.md
    M  scripts/governance_tools/task_checker.py
    A  specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md
    A  tests/test_gate_pins.py
    M  tests/test_task_checker.py

    additions 3   modifications 3   deleted/renamed/copied/type-changed/unmerged/unknown 0

**INTENDED at commit 5:** 4 additions and 3 modifications — the six above
plus `reports/2026-08-14T0325Z_p7-repair-and-pin-validator.md`.

**`GATES.md` is NOT among them**, as A7 requires. **MEASURED:**
`git diff --name-only 88ef5eec HEAD -- GATES.md` returns 0 paths, and the
blob is `2b3bd5069414f009e1a0466c4990db2949519bd8` at base and at head.

---

## 9. The classification — A8

**Full diff, base to head:**

    diff --git a/derivations/GOVERNANCE-ENFORCEMENT_classification.md b/derivations/GOVERNANCE-ENFORCEMENT_classification.md
    index 183df94..74fc207 100644
    --- a/derivations/GOVERNANCE-ENFORCEMENT_classification.md
    +++ b/derivations/GOVERNANCE-ENFORCEMENT_classification.md
    @@ -41,7 +41,7 @@ under each.
     | P4 | superseded branches are not merged | MECHANICAL | Amendment K |
     | P5 | merge parentage against freshly recomputed facts | PARTIAL | Rule 5 (part) |
     | P6 | commit-message hygiene | PARTIAL | **no rule** — see §3 |
    -| P7 | gate integrity | PARTIAL | Rule 3 (part) |
    +| P7 | gate integrity — every `## P2-` heading is parsed, and no unauthorised section changed | PARTIAL | Rule 3 (part) |
     | P8 | Rule 15 placement and specification-first | MECHANICAL | Rule 15 (placement) |
     | P9 | every report carries "Stops and clarifications" | MECHANICAL | Amendment B |
     
    @@ -69,6 +69,42 @@ under each.
       change; the authorised set is a caller-supplied parameter, and an empty
       set means "nothing may change", never "nothing to check".*
     
    +**P7's limitation, extended by measurement rather than by argument.** The
    +paragraph below is **not** part of the `does_not_establish` field quoted
    +above; it records what `P7` was found to be doing, and what now prevents it.
    +
    +**`P7` returned `PASS` while checking nothing, in every task that ran it.**
    +Its heading grammar was `^## (P2-[A-Z0-9-]+)\s*$`, which requires the line to
    +end after the gate id. **Every one of the fourteen headings in `GATES.md` is
    +`## <id> — <title>`, so the expression matched none of them**: `gate_sections`
    +returned an empty map at both base and head, `check_p7` compared two empty
    +maps, found nothing changed, and returned `PASS`. **Among the tasks that
    +green were two which modified `GATES.md` and one which flipped a gate
    +prerequisite.** **An empty match returning True is the most dangerous kind of
    +green, and it was demonstrated in the tool built to prevent it.**
    +
    +**What prevents the recurrence is the completeness invariant, not the new
    +grammar.** A better grammar closes the instance; **only the invariant closes
    +the class.** `check_p7` now counts `## P2-` lines through a pattern written
    +independently of the grammar it guards, and returns **`NOT_PARSEABLE` unless
    +the parsed section count EQUALS that raw count, at base and at head.**
    +**Equality, not merely non-zero:** a guard firing only at zero would still
    +pass a grammar that read fourteen of fifteen headings, because the fourteen
    +it sees are unchanged and the fifteenth is invisible to it — and one unseen
    +gate is enough. **A raw count of zero is `NOT_PARSEABLE` too**, because a
    +registry the grammar could not read has not been checked, which is not the
    +same as having been read and found clean. **Both hold when the authorised set
    +is empty and when base and head are identical.**
    +
    +**`NOT_PARSEABLE` and not `FAIL`, deliberately.** The state means the grammar
    +cannot fully read the gate registry, **not** that an unauthorised change has
    +been shown. **Cannot judge is not judged wrong** — the distinction `P1`
    +already carries. It still makes the run `INCOMPLETE` and exits non-zero.
    +
    +**`P7` remains `PARTIAL`, and for the unchanged reason:** the authorised set
    +is still a caller-supplied parameter and the discovery problem behind it is
    +untouched by this repair.
    +
     ### P8 and P9, added, with reasons
     
     **P8 — Rule 15 placement and specification-first.** Rule 15's *Placement*
    @@ -86,6 +122,42 @@ the blob.** What that section must *contain* is not, so P9 checks
     presence only and says so — it is MECHANICAL about the heading and makes
     no claim about the section's adequacy.
     
    +### Validators — suite checks, and NOT properties of the checker
    +
    +**These are not among the nine and must never be numbered among them.** A
    +property runs when someone invokes the checker with a config; a validator
    +runs whenever anyone runs the suite. **They are listed here because the
    +document's purpose is to say what has a machine behind it**, and a check that
    +runs only in the suite still has one.
    +
    +| id | validator | class | what it guards |
    +|---|---|---|---|
    +| V1 | gate pin integrity — `tests/test_gate_pins.py` | MECHANICAL | that every artifact pinned by SHA-256 in `GATES.md` still hashes to its pin |
    +
    +**V1 — why it is a test and not a property.** The measured failure was that
    +**the suite could not distinguish a stale pin from a correct one**:
    +`python -m pytest` returned `280 passed, 2 deselected` across four
    +consecutive revisions spanning a stale pin, a repaired pin, an edited
    +artifact and a re-pinned one. **The count never moved.** **A suite invariant
    +across the property in question is not testing that property.** The
    +demonstrated gap was the suite's, so the repair went in the suite.
    +
    +**V1 fails on three things, and the third is the one that matters:** a pin
    +whose target does not hash to it; a pin with no resolvable artifact path
    +above it, which fails rather than being skipped; and **a `GATES.md` carrying
    +no pin at all.** **A pin validator that passes over an empty pin set is the
    +same defect `P7` carried, one level along**, and this programme has now met
    +that shape twice.
    +
    +**What V1 does not establish.** It does not establish that the pinned
    +digests are the *right* ones — only that the artifacts still match whatever
    +`GATES.md` declares. **A pin that was wrong when it was written passes.**
    +**Nor does anything currently detect V1 itself going vacuous:** its non-empty
    +assertion is a guard written by the same hand as the guard it imitates, and
    +if the pin notation drifted so that the pattern stopped matching, the
    +non-empty assertion would be the thing that fires — which is why it exists,
    +and is not a substitute for an independent check that does not exist.
    +
     ---
     
     ## 2. The eighteen rules

### 9.1 Verdicts unchanged, and the nine stay nine — MEASURED

    property rows '^| P[1-9] |'   base 9   head 9
    diff of those rows            one line differs: P7's DESCRIPTION cell only

    | P7 | gate integrity | PARTIAL | Rule 3 (part) |
    | P7 | gate integrity — every `## P2-` heading is parsed, and no unauthorised section changed | PARTIAL | Rule 3 (part) |

**`P7`'s class is `PARTIAL` at base and `PARTIAL` at head.** **No other
property row changed in any column.** **No property was added or removed.**

**§5, "The count that matters", is byte-identical base to head** — verified
by diffing the whole section. **The validator is not numbered among the nine
and does not appear in that count**, which is why the count did not need to
move.

**The `MECHANICAL` and `PARTIAL` token totals each rose by one** (13→14 and
17→18). **Both increments are mine and neither is a verdict change:** the new
`V1` row carries `MECHANICAL`, and my added `P7` paragraph states that `P7`
**remains** `PARTIAL`. **`JUDGEMENT` is unchanged at 26.**

### 9.2 Exactly two authorised changes, in three diff regions

**A8 authorises two changes and makes a third a STOP. I measured three diff
hunks and map them explicitly, because three hunks and two changes need
reconciling rather than asserting:**

    @@ -44 +44 @@          P7's table row              -- change 1, "P7's description"
    @@ -71,0 +72,36 @@      P7's limitation paragraphs  -- change 1, "and limitation"
    @@ -88,0 +125,36 @@     the VALIDATOR subsection    -- change 2

**A8's first authorised change is "`P7`'s description **and** limitation" —
one change spanning two adjacent regions.** The second is the VALIDATOR
entry. **There is no third change**: the diff is 73 insertions and 1
deletion, the single deletion being `P7`'s old table row.

**One deliberate choice inside change 1, stated so it can be overruled.** The
document says of its limitation bullets: *"These sentences are the checker's
`does_not_establish` field verbatim."* **I did not alter that bullet**, and I
did not alter `DOES_NOT_ESTABLISH["P7"]` in the code. **The new limitation
text is added as prose below the bullet, explicitly marked as not part of the
quoted field.** That keeps the document's own verbatim claim true. **The
alternative — rewriting both — would have made the code change and the
document change interdependent across two commits, and would have altered a
field the specification did not ask me to touch.**

---

## 10. The checker — A9, MEASURED at commit 4

    base   88ef5eec08ab269eddcea8c617cf4f5b09b7336e
    head   036dd4d6666e0ca7a2d1602edf5ab57d9b8cf698   (commit 4 — not commit 5)

**Both prospectivity readings run for each of the two runs, so four
invocations. All four exited 0 with `overall: PASS`.**

    run 1 INCLUSIVE   exit 0   PASS   sha256 c1bd630879c7c7f220131cfdebba791da5e911e64d3b929971dd43e1b6da5195
    run 1 EXCLUSIVE   exit 0   PASS   sha256 9ec3920a659d577000ab1faaedc5f32f22c75ac1256f05493850398345108e19
    run 2 INCLUSIVE   exit 0   PASS   sha256 c1bd630879c7c7f220131cfdebba791da5e911e64d3b929971dd43e1b6da5195
    run 2 EXCLUSIVE   exit 0   PASS   sha256 9ec3920a659d577000ab1faaedc5f32f22c75ac1256f05493850398345108e19

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 NOT_APPLICABLE
    P6 PASS   P7 PASS   P8 PASS   P9 NOT_APPLICABLE

### 10.1 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "88ef5eec08ab269eddcea8c617cf4f5b09b7336e",
      "head": "036dd4d6666e0ca7a2d1602edf5ab57d9b8cf698",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 10.2 RUN 2 config, verbatim — stop-governing

    {
      "base": "88ef5eec08ab269eddcea8c617cf4f5b09b7336e",
      "head": "036dd4d6666e0ca7a2d1602edf5ab57d9b8cf698",
      "specification_paths": ["specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I supplied of my own choosing; all are
taken from A9.** **`append_only_paths` is `["DECISION_LOG.md"]` and not
`[]`**, so `P3` is live. **`authorised_modified_gates` is `[]`, and here that
is truthful: no gate may change in this task.** **The config was never
adjusted to make RUN 2 pass; it passed on its first invocation.**

### 10.3 The measured RUN 1 subject set

**RUN 1's default selection chose one specification:**

    specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md
      governing sentence  "stated: 4 additions, 3 modifications"
      counted 7   stated 7   parse OK

**The same single path RUN 2 names explicitly**, so the two runs' outputs are
**byte-identical** at each prospectivity reading (the digests above are equal
in pairs). **The two readings differ in exactly one line and in no verdict:**

    237c237
    <         "inclusivity": "INCLUSIVE",
    ---
    >         "inclusivity": "EXCLUSIVE",

**The verbatim JSON is therefore given once below**, and the four digests are
what establish that this is complete rather than abridged.

**A note on `P1`'s figures, so they are not misread.** `P1` as landed at the
evidence base reports `counted 7 / stated 7` for a manifest declaring *"4
additions, 3 modifications"* — it totals the manifest's paths rather than
reporting the two categories separately. **That is the pre-repair `P1`
behaviour and this task does not touch it**; the per-category repair is
`governance/p1-declared-total`'s, whose `A10` is undischarged and stays with
it. **The seven counted paths are the seven in §4's manifest**, which I
verified against the `counted_set` in the JSON.

### 10.4 `P7`, and what its `PASS` means here

**MEASURED — the section count `P7` saw:**

    raw_heading_count_base   14        section_count_base   14
    raw_heading_count_head   14        section_count_head   14
    unauthorised_changed     []        added_sections  []    removed_sections  []
    authorised_modified      []

**`PASS`, and for the right reason: zero unauthorised gate changes over
fourteen parsed sections, not zero over zero.** **A `PASS` with a section
count of zero would have been a STOP, and it is now unreachable** — the same
input that produced it before produces `NOT_PARSEABLE` (§5, fixture 1).

**This is the first `P7` result in this repository that means anything.**
**What it means remains narrow:** the range modifies no gate, and `P7` stays
`PARTIAL` because the authorised-set discovery problem is untouched. **It
still does not establish which gate sections were authorised to change.**

### 10.5 The JSON output, verbatim

    {
      "base": "88ef5eec08ab269eddcea8c617cf4f5b09b7336e",
      "commits_in_range": 4,
      "commits_on_first_parent_line": 4,
      "head": "036dd4d6666e0ca7a2d1602edf5ab57d9b8cf698",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that its path count matches the count in the sentence the grammar selects as governing; a specification whose text does not admit the parse is reported NOT_PARSEABLE, which is not a pass.",
          "evidence": [
            {
              "counted": 7,
              "counted_set": [
                "reports/2026-08-XXT{HHMM}Z_p7-repair-and-pin-validator.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_p7-repair-and-pin-validator.md",
                "specs/2026-08-XXT{HHMM}Z_p7-repair-and-pin-validator.md",
                "tests/test_gate_pins.py",
                "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                "scripts/governance_tools/task_checker.py",
                "tests/test_task_checker.py"
              ],
              "governing_sentence": "stated: 4 additions, 3 modifications",
              "parse": "OK",
              "path": "specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md",
              "stated": 7
            }
          ],
          "id": "P1",
          "status": "PASS",
          "title": "scope manifest arithmetic"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "commits": [
              {
                "adds_review": false,
                "commit": "1ceb1b1150f7468c4b441f176296d024fa1c873b",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "2351e8beb04a6c9e4a2fe4fd266a006c637c1cf7",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "b67f75542255edb7e0af13543e770839934c2037",
                "work_paths": [
                  "scripts/governance_tools/task_checker.py",
                  "tests/test_gate_pins.py",
                  "tests/test_task_checker.py"
                ]
              },
              {
                "adds_review": false,
                "commit": "036dd4d6666e0ca7a2d1602edf5ab57d9b8cf698",
                "work_paths": [
                  "derivations/GOVERNANCE-ENFORCEMENT_classification.md"
                ]
              }
            ],
            "first_review_commit": "2351e8beb04a6c9e4a2fe4fd266a006c637c1cf7",
            "first_work_commit": "b67f75542255edb7e0af13543e770839934c2037",
            "in_scope": 4,
            "out_of_scope": []
          },
          "id": "P2",
          "status": "PASS",
          "title": "Rule 15 commit order"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
          "evidence": [
            {
              "base_bytes": 89541,
              "base_is_byte_prefix_of_head": true,
              "commits_with_deletions": [],
              "deleted_lines_base_to_head": 0,
              "head_bytes": 89541,
              "path": "DECISION_LOG.md",
              "status": "PASS"
            }
          ],
          "id": "P3",
          "status": "PASS",
          "title": "append-only on both measures"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "entries": [
              {
                "branch": "fix/pi-decisions-and-deferred",
                "commit": "52f651174dc1fef03b4fb9276078fa1f08d94bd7",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "fix/pi-decisions-v2",
                "commit": "ebd531ab568aaffabd86a4a94d925a711e62aa36",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-v2",
                "commit": "40168469608618aef6812735ff70e32de0e3cbc8",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-and-superseded",
                "commit": "7146a093c65788a57d63a747b71d86edb91eddc6",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "review/role-model-and-executors",
                "commit": "10c260b96882ac12610f78840aeeabd07be2d7cb",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "gate/p2-land-diquark-line",
                "commit": "d64cd912ca9ff78a85787f0e54f345f474cdb192",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              }
            ],
            "register_path": "docs/BRANCHING_POLICY.md"
          },
          "id": "P4",
          "status": "PASS",
          "title": "superseded branches are not merged"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the executor derived the parentage values independently; three correct values are equally consistent with fresh recomputation and with one field copied into another. The diquark task's shared-rationale defect would pass this check.",
          "evidence": {
            "merges": []
          },
          "id": "P5",
          "reason": "no merge commit in range",
          "status": "NOT_APPLICABLE",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "1ceb1b1150f7468c4b441f176296d024fa1c873b",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "2351e8beb04a6c9e4a2fe4fd266a006c637c1cf7",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "b67f75542255edb7e0af13543e770839934c2037",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "036dd4d6666e0ca7a2d1602edf5ab57d9b8cf698",
              "matches": [],
              "status": "PASS"
            }
          ],
          "id": "P6",
          "status": "PASS",
          "title": "commit-message hygiene"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
          "evidence": {
            "added_sections": [],
            "authorised_modified": [],
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "unauthorised_changed": []
          },
          "id": "P7",
          "status": "PASS",
          "title": "gate integrity"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "first_commit": "1ceb1b1150f7468c4b441f176296d024fa1c873b",
            "first_commit_paths": [
              "specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-14T0325Z_p7-repair-and-pin-validator.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {},
          "id": "P9",
          "reason": "range adds no report",
          "status": "NOT_APPLICABLE",
          "title": "reports carry a Stops and clarifications section"
        }
      ],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 4,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

---

## 11. Validators — A10, MEASURED

    before, at the evidence base 88ef5eec…    280 passed, 2 deselected    exit 0
    after,  at commit 4 036dd4d6…             301 passed, 2 deselected    exit 0

    delta   +21 passed,  deselected unchanged at 2

**The count MUST rise, and it did.** **What accounts for the +21, measured
rather than estimated:**

    tests/test_task_checker.py    42 -> 52 test functions   +10 collected
    tests/test_gate_pins.py       new: 9 test functions, one parametrized x3
                                                            +11 collected
                                                            ----
                                                            +21

**Per-file collection, MEASURED:** `tests/test_task_checker.py` alone reports
`52 passed`; `tests/test_gate_pins.py` alone reports `11 passed`. **9 + 3 − 1
= 11** — eight plain tests plus one parametrized over three separators.

**A count that did not move would have meant the new tests were not being
collected.** It moved by exactly the number of tests added.

**The ten new `test_task_checker.py` fixtures**, each of which the pre-repair
code fails:

    test_gate_grammar_reads_every_heading_of_the_real_gates_file
    test_gate_grammar_rejects_the_bare_heading_the_old_grammar_accepted
    test_p7_is_not_parseable_when_the_grammar_reads_none_of_the_headings
    test_p7_is_not_parseable_when_one_heading_of_many_is_unread
    test_p7_is_not_parseable_when_a_heading_parses_at_base_but_not_at_head
    test_p7_is_not_parseable_when_the_gate_file_has_no_headings_at_all
    test_p7_zero_sections_is_not_a_pass_even_with_an_empty_authorised_set
    test_p7_zero_sections_is_not_a_pass_when_base_and_head_are_identical
    test_p7_not_parseable_makes_the_run_incomplete_and_exits_non_zero
    test_p7_still_fails_on_an_unauthorised_change_it_can_read

### 11.1 The pre-existing tests, and one change to a shared fixture

**No test was deleted and no check was weakened.** All 42 pre-existing
`test_task_checker.py` tests still exist and still pass, **with every
assertion unchanged.**

**One fixture's DATA changed, and it is worth its own paragraph because it is
part of the finding.** The shared `base_repo` fixture built its gate file
from **bare** headings — `## P2-ALPHA-01`, `## P2-BETA-01` — which is
**precisely the shape the broken grammar matched, and a shape no heading in
`GATES.md` has ever used.** The fixtures were shaped to suit the parser
rather than to resemble the file, **so the suite confirmed the broken grammar
instead of catching it.**

**I gave those fixture headings titles**, matching the real file. **The six
pre-existing `P7` tests pass unchanged** — verified by running them
before and after. **This is a change to fixture data, not to a test's
assertion**, and I report it explicitly rather than let it pass as
housekeeping, because a reader comparing the diff would otherwise see test
inputs edited in a task that repairs the thing those tests cover.

**The refactor that came with it:** `base_repo` now delegates to
`base_repo_with_gates(tmp_path, gates)`, so the new fixtures get the same
register and decision log. **My first draft of the new fixtures hand-rolled a
register and seven of them failed `P4`** — the checker behaving correctly and
my fixture asking the wrong question. Sharing the real fixture base fixed it.

---

## 12. Commits — A11, MEASURED for commits 1–4

    commit 1   1ceb1b1150f7468c4b441f176296d024fa1c873b   specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md
    commit 2   2351e8beb04a6c9e4a2fe4fd266a006c637c1cf7   reviews/chatgpt/2026-08-14T0325Z_p7-repair-and-pin-validator.md
    commit 3   b67f75542255edb7e0af13543e770839934c2037   task_checker.py + test_task_checker.py + test_gate_pins.py
    commit 4   036dd4d6666e0ca7a2d1602edf5ab57d9b8cf698   derivations/GOVERNANCE-ENFORCEMENT_classification.md

    UTC token fixed by commit 1:  0325Z        day at execution: 14
    full stamp:                   2026-08-14T0325Z

**Stored subjects, MEASURED:**

    commit 1   spec: repair P7, forbid the vacuous pass, and validate the gate pins
    commit 2   review: pre-execution review for the P7 repair and pin validator
    commit 3   fix: P7 reads the real gate headings and refuses an incomplete parse
    commit 4   docs: record what P7 was doing, and add the pin validator as a VALIDATOR

**Per-commit hygiene, on the stored message of each:**

| Commit | `Co-Authored-By` | session id or URL | tool attribution | Trailer suppressed? |
|---|---|---|---|---|
| 1 | none | none | none | **No — none was ever written** |
| 2 | none | none | none | **No — none was ever written** |
| 3 | none | none | none | **No — none was ever written** |
| 4 | none | none | none | **No — none was ever written** |

**Code and tests moved together in commit 3**, as §4 requires: the parser
change and its fixtures are one commit, so there is no revision at which the
grammar had changed and its fixtures had not.

**Commit 5's message, INTENDED:**

    report: P7 now reads fourteen gates, and the suite catches a stale pin

**Commit 5 is post-report evidence. Nothing in this report measures it.**

### 12.1 Did my harness attempt a forbidden trailer? — A11, answered

**Yes as a standing instruction, no in what was committed.** My harness
carries generic git guidance instructing that every commit message end with a
`Co-Authored-By` line and a session URL. **Each of this task's messages was
composed without them at first writing**; the proposed text was inspected
before each commit and the stored text after. **No commit was amended and no
history was rewritten.** `P6` reports `PASS` on all four commits in every one
of the four checker invocations, which is the mechanical confirmation.

**The ratification recorded for a past unpushed amend confers nothing here
and was not relied on.**

---

## 13. `F1` and `F2` — met, reported, unrepaired

**`F1` — the harness conflicts with `P6` structurally.** **I met it: the
guidance is live in my session now.** It is caught only because each
specification remembers to write a hygiene criterion and because I wrote
against it by hand. **Reported. Not fixed** — §2 forbids it, and the durable
repair is not this task's.

**`F2` — `scripts/p2_phase01_scalar_exploratory.py` line 73 reads
`for the frozen Wilson D`.** **I met it and confirmed it is still there,
unrepaired**, at head:

    73:        """Return ``I0(Mhat)`` and ``d I0 / d Mhat`` for the frozen Wilson D."""

    git diff --name-only 88ef5eec HEAD -- scripts/p2_phase01_scalar_exploratory.py    ->    0 paths

**Reported. Not fixed** — `scripts/` is protected by A9 except for
`task_checker.py`, and §2 forbids the repair. **I did not read the
exploratory script for physics and did not answer `C2`.**

---

## 14. Rule 16 assessment — all three junctions

### 14.1 First — two checks now work, and that is the whole claim

**After this task `P7` sees fourteen gates and the pin validator runs in the
suite. A reader may take that for governance being enforced. It is not.**

**The classification still records twenty-two of twenty-nine objects with no
machine behind them**, and §5's count is byte-identical after this task —
**deliberately, because nothing this task did changes it.** `P7` remains
`PARTIAL`: **the authorised-set discovery problem is untouched.** The
authorised set is still whatever the caller passes, and nothing verifies that
the set passed is the set the task was authorised to change.

**Two checks now work. That is the claim, and it is the whole of it.**

### 14.2 Second — I looked for other vacuous checks, and a search is not a check

**Yes, I looked. Here is what over, and what it is worth.**

**What I searched:** every assertion in `tests/` of the form `assert not X` or
`assert all(...)` over a collection derived from a regex, a glob or a
comprehension — **28 such assertions** — plus every `re.findall` /
`re.finditer` / `.match` driving a collection in `tests/` and
`scripts/governance_tools/`. I read the ones whose collection could be empty
without the file being obviously broken.

**What I found, and it is a real secondary finding.**
`tests/test_repository_structure.py` already contained a **working**
gate-heading pattern —

    r"^##\s+(P2-[A-Z]+(?:-[A-Z]+)*-\d+)"      finds all 14

— **in the same repository, at the same revision, as the broken one in
`task_checker.py`.** The two never agreed and nothing compared them.
**That test also already carries a non-empty guard**
(`assert cited, "No gate IDs found in CLAIMS.md; parser or table changed."`),
which is the shape this task had to add to `P7`. **The pattern for the repair
was already in the repository; it had simply never been applied to the
checker.**

**What I did not find:** any other assertion in the suite whose only
protection against an empty collection is absent. **I did not fix anything I
found, and I found nothing needing a fix.**

**And now the limit, plainly. A search I performed once is not a check that
runs.** Nothing prevents the next vacuous assertion from being written, and
**nothing re-runs my search.** **This task does not establish that no other
check in the suite passes vacuously** — it establishes that I looked once,
over the shapes named above, on one revision, and reports what I saw.

### 14.3 Third — what would detect the pin validator itself going vacuous

**Nothing currently does, and the specification is right that this is the
uncomfortable one.** **`test_pin_set_is_not_empty` is a guard written by the
same hand as the guard it is imitating**, and it fails in exactly the way
`P7` failed: **if the pin notation in `GATES.md` drifted so that `PIN` stopped
matching, the non-empty assertion is the thing that would fire** — which is
why it exists, and is precisely not an independent check.

**What would detect it, named and NOT built here:**

1. **An expected-count assertion with the number written down** — "`GATES.md`
   contains exactly N pins" — which fails when the count moves in either
   direction, rather than only at zero. It has a maintenance cost: every
   legitimate pin addition edits a test. **That cost is the point**; it makes
   the count a declared quantity rather than a discovered one.
2. **A mutation check that runs the validator against a fixture known to be
   stale and asserts it fails** — the pin-validator analogue of §5's
   demonstration against the old parser. **A validator that has never been
   observed to fail on live data has not been shown to check anything.** Runs
   (ii)–(iv) of §6 are that observation performed once, by hand, in this
   report; they are not a standing test over `GATES.md` itself.
3. **A cross-check between two independently written pin locators**, on the
   same principle as `RAW_GATE_HEADING` versus `GATE_HEADING`: agreement
   between two patterns nobody wrote to match each other.

**None of the three is built here**, as §6 instructs. **The recursion is real
and I do not claim to have closed it:** every guard I could add is a guard
written by me, and the only thing that breaks the regress is a second pair of
eyes or a signal from outside the file.

---

## 15. Did building these checks make me want to fix something else?

**Yes. Three things, and I fixed none of them.**

**(a) `P1`'s per-category counting.** §10.3 records that `P1` reports
`counted 7 / stated 7` for a manifest declaring "4 additions, 3
modifications" — it totals rather than comparing per category. **I knew the
repair, having written it on `governance/p1-declared-total`.** **I did not
touch it:** §2 forbids repairing `P1` through `P6`, `P8` or `P9`, and that
branch's `A10` is undischarged and stays with it.

**(b) `check_p7`'s missing head-side existence guard.** `check_p7` guards
`path_exists_at_revision` at **base** only. If `GATES.md` were absent at
**head**, `gate_sections` would raise rather than return a status. **I noticed
it while adding the invariant and left it alone** — it is a distinct defect,
not the one this task was specified to close, and adding a guard nobody
reviewed would have widened the change beyond the manifest. **Reported in
§16.2 as a secondary finding.**

**(c) `F2`, the `frozen Wilson D` docstring.** One line, obviously wrong,
sitting in a file I had open. **§2 forbids it and `scripts/` is protected.**
**Not touched** — verified, 0 paths changed in that file.

**I confirm I did not fix any of them.**

---

## 16. Stops and clarifications

### 16.1 Stops

**None.** No stop was reached in any of the five primary categories:
`SPECIFICATION_DEFECT`, `ENVIRONMENT`, `OBSERVATION_METHOD_ERROR`,
`REPOSITORY_DEFECT`, `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`.

**Every stop condition the specification names was tested and none
triggered:** A1's ref matched; A2's review names the executed digest and
arrived as a file; A7 shows `GATES.md` unmodified; A8's diff carries exactly
the two authorised changes and no third; A9's RUN 2 exited 0 with `P7` at a
section count of 14, not 0; A10's count rose. **`tests/test_gate_pins.py` was
accepted as specified and not relocated**, so §4's "STOP and say where" did
not arise.

### 16.2 Secondary findings

**S1 — `REPOSITORY_DEFECT`, arriving, reported and not repaired.**
`check_p7` checks `path_exists_at_revision` for the gate file at **base**
only. **A `GATES.md` absent at head would raise out of `gate_sections`
instead of returning a status.** Not reachable in this task's range, and not
repaired here. See §15(b).

**S2 — observation, and it reframes the defect.** A **correct** gate-heading
pattern already existed in `tests/test_repository_structure.py`, complete
with the non-empty guard this task had to add to `P7` (§14.2). **The
repository was not missing the technique; it had simply never applied it to
the checker**, and nothing compared the two patterns. **Making them agree, or
sharing one, is not this task's** — I report it as the most useful thing my
Rule 16 search turned up.

**S3 — `OBSERVATION_METHOD_ERROR` in my own working, self-caught, twice.**
Both are recorded above in the sections they affected rather than only here:
my first `14 / 15` fixture was really a `1 / 15` case and would have passed
A4 in appearance only (§5, fixture 2); my first A6 instrument deleted `.git`
and broke six unrelated tests, contaminating the measurement (§7). **Both
were discarded and redone before anything was committed or reported as a
result.**

**S4 — observation, non-blocking, agreeing with the review.** The review's
non-blocking note on §1a's opening sentence is fair: *"the question was
whether they would collide. Measured: they do not"* reads more broadly in
isolation than the limitation that follows. **It changed nothing in
execution** — I cut this branch from `main`, did not merge
`governance/p1-declared-total`, and did not discharge its `A10`. **I record
here, as §1a requires whoever integrates to note, that this task modifies all
three shared files**: `task_checker.py`, `tests/test_task_checker.py` and the
classification. **Nothing in this report supports any claim about the order
in which the two branches can be integrated.**

**F1 and F2 are reported in §13** as arriving and unrepaired.

### 16.3 Ambiguous, unsatisfiable, or what I would have specified differently

**Nothing was unsatisfiable, and no instruction was inconsistent with a
repository rule.** Four observations:

1. **A8's "exactly two changes" versus a diff's hunk count.** `P7`'s
   description and its limitation are one authorised change but two
   non-adjacent regions, so a literal hunk count reads three where the
   criterion says two. **§9.2 reconciles them explicitly.** **I would have
   specified the count in terms of the entries changed, not the changes** —
   "`P7`'s entry and one new VALIDATOR entry" — which is unambiguous against
   any diff.
2. **The `does_not_establish` verbatim claim is a coupling A8 does not
   mention.** The classification asserts its limitation bullets are the
   checker's field verbatim, so extending `P7`'s limitation could have
   required editing the code too. **I resolved it by adding prose outside the
   bullet** (§9.2) and say so rather than leaving the reader to infer it.
   **A specification that named which of the two to move would have removed
   the judgement call.**
3. **A6 says "make one `GATES.md` pin stale" and I read it as making the
   pinned artifact stale**, not as editing `GATES.md`'s declared digest.
   Either produces a mismatch; **the artifact-side edit is the one that
   models the real failure** — an adopted file drifting from its pin — and it
   leaves `GATES.md` untouched, which sits better with §2. **Stated because
   the other reading was available.**
4. **A10's "before and after" does not name the two revisions.** I read them
   as the evidence base and commit 4 and **measured both**, rather than
   quoting the 280 figure from earlier reports. §7.1 does the same for the
   counterfactual. **I would have named the revisions.**

### 16.4 Rule 13

**No environment failure occurred, so neither of Rule 13's two diagnostic
orders was exercised.** **Rule 13 carrying two such orders remains a known
open item; I name neither as the one that applies.**

    Python   3.11.15
    pytest   9.1.1

**Nothing was installed.**

---

## 17. Evidence layering

**Committed in this report, MEASURED at commit 4:** A1–A8, A10 and A11 for
commits 1–4; A9's four invocations with both configs and the JSON output;
commits 1–4 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 5's message; the final
base-to-head scope of 4 additions and 3 modifications.

**Post-report evidence, returned to the Reviewer and NOT written back:** the
final scope measured base-to-commit-5; A9-final, being RUN 2 re-run at commit
5; A11 for commit 5; the validators at commit 5; the push; the branch tip
read back.

**Nothing in this report claims to measure commit 5.**

**`main` was not touched, nothing was merged, and no branch was deleted.**
**Integration is a separate task**, and this report authorises none of it.
