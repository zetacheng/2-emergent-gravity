# Report — repair the adopted artifact's wording and both stale gate pins

Specification: `specs/2026-08-12T2326Z_adopt-domain-repair.md`
Review: `reviews/chatgpt/2026-08-12T2326Z_adopt-domain-repair.md` — APPROVED FOR EXECUTION
Evidence base: `2e4cc6eb9ae8a34d7a5e81c86d82a5b631dabe7a` (`science/adopt-parameter-domain`)
Branch: `science/adopt-parameter-domain-repair`, cut from that commit.
**Authoritative `main` = `1cb5550f…`, NOT touched and not merged.**

**Every figure is labelled MEASURED or INTENDED.** **Nothing here claims to
measure commit 5.**

---

## 0. Executive summary

**Both defects are repaired and the repair's own consequence is repaired with
it.** Three wording anchors were found verbatim exactly once each; the adopted
artifact's diff is confined to its first twelve lines. Two digest strings in
`GATES.md` changed and nothing else did. **A6's by-hand enumeration finds two
pins in `GATES.md` and both now MATCH their targets.** A9's RUN 2 — the
stop-governing run — **PASSED, exit 0, on both prospectivity readings.**

**All five gate invariants hold**: 14 gate sections, every `Status:` line
textually identical, `P2-PHASE-01` `PROPOSED`, MICROSCOPIC PARAMETER DOMAIN
`SATISFIED`, PHASE INPUT / ADMISSIBILITY CONTRACT `UNSATISFIED`.

**The adoption branch is now internally consistent and the pin conflict the
previous report stopped on is discharged.** Integration remains a separate task
and is not authorised here.

**One measured discrepancy with the specification, and it is presentational,
not substantive.** A4 requires *"exactly three hunks"* in the adopted
artifact's diff. **MEASURED: three hunks at zero context, ONE hunk at git's
default three-line context**, because the three edited regions are adjacent
(lines 1, 4–7, 9–12) and coalesce. **A4's stop condition is "a fourth hunk",
which is not triggered.** §4 reports both counts and the decomposition, so the
criterion's substance — that the change is exactly the three authorised
substitutions and nothing else — is established rather than asserted.

**`C1`, `C2` and `C3` were not answered and
`scripts/p2_phase01_scalar_exploratory.py` was not read.** No physics was
computed.

**`P7` returned `PASS` and it is evidence of nothing.** §7.

---

## 1. A1 — Refs

**MEASURED**, read from the remote:

```
2e4cc6eb9ae8a34d7a5e81c86d82a5b631dabe7a	refs/heads/science/adopt-parameter-domain
1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab	refs/heads/main
```

**Both match. No STOP.**

## 2. A2 — The review, committed unedited, with BOTH digests filled in

**MEASURED.** The review carries, at its head and repeated in its final
disposition:

    reviewed specification SHA-256:
      665ef240218bc6d0d7b3ae7dfe2d75e9d2ad104eccb25e166e05b13c904c3488
    reviewed artifact SHA-256:
      c27e57f080ecf8a2472a7f614aedcc19c5c72622650f6ddd0bc802d3fced5003

**Both are filled in and both are correct:**

    supplied specification file, sha256
      665ef240218bc6d0d7b3ae7dfe2d75e9d2ad104eccb25e166e05b13c904c3488   EQUAL
    2e4cc6eb:derivations/P2-PHASE-01_microscopic_parameter_domain.md, sha256
      c27e57f080ecf8a2472a7f614aedcc19c5c72622650f6ddd0bc802d3fced5003   EQUAL

**Neither is blank and neither names a different digest. A2's stop is not
triggered.**

    supplied review   a29d269bd133d3652ee669d9ba2e70e37d7590d51a971cc0dad6fdd9f4c48fce
    committed blob    a29d269bd133d3652ee669d9ba2e70e37d7590d51a971cc0dad6fdd9f4c48fce
    EQUAL

**Both the specification and the review arrived as FILES.** Rule 18 satisfied
on both; neither was pasted.

**This is the first review in this line to pin the specification it approved.**
The adoption task's review pinned only the artifact, which established what was
being adopted but not which specification authorised it. **Pinning both closes
that gap** — and it is still practice rather than rule: **no repository
convention requires either digest.**

## 3. A3 — Pinned inputs at the evidence base

**MEASURED**, Git blob ids at `2e4cc6eb`:

```
0e34e7686d4881a84e778b079b0b3dcc5d559c6c  GATES.md
d4aa28b7b8fbbfdc3f685f02cb6929e7c07a7d31  derivations/P2-PHASE-01_microscopic_parameter_domain.md
f6f0e524daa11f2f8e3470cc4ab44fd3f6630615  derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
c7910bc6a6cca5c684b082aef87de85b6a3d6f4c  derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
```

**SHA-256 of the two files named in §4, at the evidence base:**

```
adopted artifact  c27e57f080ecf8a2472a7f614aedcc19c5c72622650f6ddd0bc802d3fced5003
contract draft    e373efcb0d14db641604537c6a264e2c48536ab516162b7fef6a995cbd11d1cb
```

**A3 requires the contract draft to measure
`e373efcb0d14db641604537c6a264e2c48536ab516162b7fef6a995cbd11d1cb`. It does.
No STOP.** **That value is therefore RE-PIN 2's target, measured and not
copied.**

## 4. A4 — The three wording repairs

**MEASURED.**

    adopted artifact, before   c27e57f080ecf8a2472a7f614aedcc19c5c72622650f6ddd0bc802d3fced5003
    adopted artifact, after    a481955be9bfa248b925ef7bf49f0f57cc462799ee72278507f71f99ac70cfc8

**The "after" digest is read from the COMMITTED BLOB at commit 3**, not from a
working-tree file, because RE-PIN 1 embeds it.

**THREE operations. Each OLD anchor was required to occur exactly once; a count
other than one was coded to abort, not to search for a near match.**

    op 1  OLD-1 title                    1 match, substituted
    op 2  OLD-2 status paragraph         1 match, substituted
    op 3  OLD-3 supersession paragraph   1 match, substituted

**The operation count is three. No approximate match was attempted.**

### The hunk count, measured both ways

**A4 says "exactly three hunks". MEASURED:**

    git diff -U0   3 hunks   — one per operation
    git diff       1 hunk    — git's default 3 lines of context

**The three edited regions are lines 1, 4–7 and 9–12**, separated only by the
single blank lines 2, 3 and 8. **At default context they coalesce into one
hunk. That is a presentation property of adjacency, not a fourth change.**
**A4's stop — "a fourth hunk is a STOP" — is not triggered**, and the
zero-context decomposition below shows one hunk per authorised substitution and
no other.

**Full diff at zero context, one hunk per operation:**

```diff
+++ b/derivations/P2-PHASE-01_microscopic_parameter_domain.md
@@ -1 +1 @@
-# `P2-PHASE-01` microscopic parameter domain — DRAFT FOR ADOPTION
+# `P2-PHASE-01` microscopic parameter domain — ADOPTED
@@ -4,4 +4,6 @@
-`specs/2026-08-12T2258Z_adopt-parameter-domain.md`. This artifact
-is written for PI confirmation and reviewer scrutiny. **Adoption requires
-a task with its own specification and pre-execution review**; nothing
-here is in force until that task lands.
+`specs/2026-08-12T2258Z_adopt-parameter-domain.md`, under the
+pre-execution review committed alongside it. **This artifact is in
+force.** It was written for PI confirmation and reviewer scrutiny,
+both of which it received; **the sentences that described it as
+awaiting them were left behind by an anchored substitution that
+repaired only the status line, and are corrected here.**
@@ -9,4 +11,6 @@ here is in force until that task lands.
-**It supersedes nothing.** `derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`
-deliberately adopted no domain and retained five open items. **This
-artifact answers four of them and leaves one open**, and says which is
-which.
+**It supersedes one artifact.**
+`derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`
+deliberately adopted no domain and retained five open items; **it is
+now marked SUPERSEDED and is retained as historical evidence.** **This
+artifact answers four of those items and leaves one open**, and says
+which is which.
```

**Changed-line accounting, MEASURED: 9 lines removed, 13 added, every one of
them inside lines 1–12.** No hunk touches an adopted decision, a measured
figure, an open-item verdict, or the boundary statement.

### Does the artifact now read as adopted from its first line?

**Yes. MEASURED, the committed opening:**

    # `P2-PHASE-01` microscopic parameter domain — ADOPTED

    **Status: ADOPTED.** Adopted by
    `specs/2026-08-12T2258Z_adopt-parameter-domain.md`, under the
    pre-execution review committed alongside it. **This artifact is in
    force.** It was written for PI confirmation and reviewer scrutiny,
    both of which it received; **the sentences that described it as
    awaiting them were left behind by an anchored substitution that
    repaired only the status line, and are corrected here.**

    **It supersedes one artifact.**
    `derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`
    deliberately adopted no domain and retained five open items; **it is
    now marked SUPERSEDED and is retained as historical evidence.** **This
    artifact answers four of those items and leaves one open**, and says
    which is which.

**The title says ADOPTED, the status says ADOPTED, the artifact says it is in
force, and the supersession sentence agrees with the gate registry and with the
old draft's own `SUPERSEDED.` stamp.** **The three claims that contradicted the
status line are gone.**

**The repaired text keeps the record of its own repair** — *"left behind by an
anchored substitution that repaired only the status line"* — rather than
silently reading as though it had always been right. **A later reader can see
that the file was corrected and why.**

**No fourth wording defect was found, and the search is reported rather than
asserted.** **MEASURED: the string `draft` occurs three more times in the file,
and none of the three is a status claim about this artifact:**

    line  12   `derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`
               — a path, and the correct one
    line  34   "daaaca4e…   first draft; four revisions required"
               — the revision-provenance block, describing this artifact's own
                 earlier drafts as history. Correct as history.
    line 114   "The earlier draft's `Mhat = 1` crossing at `G/Gc ≈ 1.77`"
               — a reference to the superseded draft artifact. Correct.

**§3's `RECOMMENDATION, for PI adoption` (line 85) also survives**, and it is a
label on the recommendation the PI has since ruled on rather than a claim that
the artifact awaits adoption. **I left all four and report them; none is inside
§3's anchors and §2 forbids correcting beyond §3.**

**I had first written that `DRAFT` appears nowhere else, and running the search
falsified it.** That sentence never reached a commit.

## 5. A5 — The two re-pins, and `GATES.md` in no other way

**MEASURED. Each old 64-hex digest was verified to occur exactly once in
`GATES.md` before substituting:**

    c27e57f080ec…  1 occurrence   ->  a481955be9bf…   (RE-PIN 1)
    a3ec0cb6f796…  1 occurrence   ->  e373efcb0d14…   (RE-PIN 2)

**Two operations. MEASURED: exactly TWO hunks, at both zero and default
context, each a single digest line.** Full diff:

```diff
+++ b/GATES.md
@@ -1014,7 +1014,7 @@ per the PI ruling recorded in §3a of
 Owner: Paper 2. Canonical label: **MICROSCOPIC PARAMETER DOMAIN**;
 not a gate ID. Adopted artifact:
 `derivations/P2-PHASE-01_microscopic_parameter_domain.md`
-(sha256 `c27e57f080ecf8a2472a7f614aedcc19c5c72622650f6ddd0bc802d3fced5003`).
+(sha256 `a481955be9bfa248b925ef7bf49f0f57cc462799ee72278507f71f99ac70cfc8`).
 Superseded draft:
 `derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`.
 
@@ -1037,7 +1037,7 @@ Artifact state: **DRAFTED / NOT ADOPTED**. Prerequisite state:
 **UNSATISFIED**. Owner: Paper 2. Canonical label: **PHASE INPUT /
 ADMISSIBILITY CONTRACT**; not a gate ID. Draft:
 `derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md`
-(sha256 `a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73`).
+(sha256 `e373efcb0d14db641604537c6a264e2c48536ab516162b7fef6a995cbd11d1cb`).
 No operational stability or admissibility rule is presently frozen.
 
 ### Integrated exploratory evidence
```

**Every `-`/`+` pair is a `(sha256 …)` line. No hunk touches a heading, a path,
a prerequisite state or a `Status:` line.** **A5's stop is not triggered.**

**RE-PIN 1's value existed only after commit 3** and was measured from that
commit's blob. **RE-PIN 2's value was stated in the specification and
independently measured at the evidence base in A3; the two agreed**, so it was
confirmed rather than copied.

## 6. A6 — Every pin in `GATES.md` checked against its target

**MEASURED at the final head, by enumerating every occurrence of
`` (sha256 `<64 hex>`) `` over the WHOLE file — no `head`, no `tail`, no
sampling — and taking the artifact path named immediately above each.**

    PINS FOUND: 2      (the specification expects TWO)

    pin 1   GATES.md line 1017
      path    derivations/P2-PHASE-01_microscopic_parameter_domain.md
      pinned  a481955be9bfa248b925ef7bf49f0f57cc462799ee72278507f71f99ac70cfc8
      actual  a481955be9bfa248b925ef7bf49f0f57cc462799ee72278507f71f99ac70cfc8
      MATCH

    pin 2   GATES.md line 1040
      path    derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
      pinned  e373efcb0d14db641604537c6a264e2c48536ab516162b7fef6a995cbd11d1cb
      actual  e373efcb0d14db641604537c6a264e2c48536ab516162b7fef6a995cbd11d1cb
      MATCH

**Two pins, both matching. No pin whose target does not match; nothing to
name.**

**This check found nothing wrong, and that is the whole point of running it.**
**MEASURED and stated plainly: the staleness this task repairs survived a full
280-test validator run, twice** — once in the adopting task's report and once in
this task's own before-measurement at the evidence base (§9). **No test compares
any pin to any file.** **A6 was performed by hand, in this task, once. That is
not the same as the property being enforced**, and §11 says what follows from
that.

## 7. A7 — Gate invariants, and what `P7` is worth

**A7's five, MEASURED at commit 4 against the evidence base:**

    1  '^## P2-' section count        base 14   head 14        UNCHANGED
    2  every '^Status:' line          15 lines, TEXTUALLY IDENTICAL
    3  P2-PHASE-01                    Status: PROPOSED
    4  MICROSCOPIC PARAMETER DOMAIN   Prerequisite state: **SATISFIED**
    5  PHASE INPUT / ADMISSIBILITY    **UNSATISFIED**

**All five hold. No prerequisite state, gate status or admissibility verdict
changed.**

### `P7` returned `PASS` and it checked nothing

**MEASURED, from this task's own run:**

```json
{
  "gates_path": "GATES.md",
  "authorised_modified": ["P2-PHASE-01"],
  "section_count_base": 0,
  "section_count_head": 0,
  "unauthorised_changed": [],
  "added_sections": [],
  "removed_sections": []
}
```

**Zero sections at base and zero at head, against a file carrying fourteen
gates.** `GATE_HEADING` is `^## (P2-[A-Z0-9-]+)\s*$` and every real heading
continues past the ID. **P7 compared two empty maps.**

**This task modifies `GATES.md`, so the vacuous green sits exactly where it is
most dangerous.** **The claim that the `GATES.md` edit stayed within two digest
strings rests on §5's two-hunk diff and §6's pin table, both direct
measurements of the file — not on `P7`.**

## 8. A8 — Protected paths, and the commit order

**MEASURED at commit 4**, whole-tree `git ls-tree -r` blob comparison, path by
path:

    paths at base                    347
    paths at commit 4                349
    removed                          none
    added                              2   (this specification, this review)
    changed                            2
    identical                        345
    changed set == §5's modify: set  TRUE
    unexpected changes               none

    results/      base  69  head  69   differing: none
    scripts/      base  60  head  60   differing: none
    tests/        base  20  head  20   differing: none
    reports/      base  67  head  67   differing: none
    specs/        base  38  head  39   differing: only this specification
    reviews/      base  26  head  27   differing: only this review

    derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md   SAME
    derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md   SAME
    CONVENTIONS.md                                                  SAME
    DECISION_LOG.md                                                 SAME
    docs/BRANCHING_POLICY.md                                        SAME

**Both DRAFT files are untouched, as §2 requires** — and the contract draft's
bytes at the evidence base are exactly what RE-PIN 2 now denotes, which is why
it had to stay untouched.

**Commits, MEASURED, in the order §5 specifies:**

    commit 1  03a195b303ac3d1ae242cd8114e35858c103c652  specs/2026-08-12T2326Z_adopt-domain-repair.md
    commit 2  92749d4ec468ca10bbd9d527863f90a786d8a727  reviews/chatgpt/2026-08-12T2326Z_adopt-domain-repair.md
    commit 3  2a1c6261e059e70afb2005d31d4223c341b8bfff  derivations/P2-PHASE-01_microscopic_parameter_domain.md
    commit 4  b10395db7edad285ae8876ea29403abcb3cbe19b  GATES.md
    commit 5  INTENDED                                  reports/2026-08-12T2326Z_adopt-domain-repair.md

**Commit 3 precedes commit 4 because RE-PIN 1 embeds commit 3's blob digest**,
and that digest was read from the blob.

**The UTC token `2326` and the day `12` were MEASURED** (`date -u`) when commit
1 was written, not chosen.

**The final scope, INTENDED** — commit 5 does not exist while this is written:

    stated: 3 additions, 2 modifications
    base: 2e4cc6eb9ae8a34d7a5e81c86d82a5b631dabe7a
    head: <commit 5, INTENDED>
    mode: exact
    add:
      reports/2026-08-12T2326Z_adopt-domain-repair.md
      reviews/chatgpt/2026-08-12T2326Z_adopt-domain-repair.md
      specs/2026-08-12T2326Z_adopt-domain-repair.md
    modify:
      GATES.md
      derivations/P2-PHASE-01_microscopic_parameter_domain.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Five paths. MEASURED at commit 4: two of the three additions are in place and
both modifications are; the third addition is this file.** **The scope measured
base-to-commit-5 is post-report evidence and is not claimed here.**

## 9. A9 — The two checker runs, and A10 — validators

Base `2e4cc6eb…`, head **commit 4** `b10395db…`. **Both prospectivity readings
were run.**

### RUN 1 — default subject selection, observational, governs nothing

```json
{
  "base": "2e4cc6eb9ae8a34d7a5e81c86d82a5b631dabe7a",
  "head": "b10395db7edad285ae8876ea29403abcb3cbe19b",
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": ["P2-PHASE-01"],
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

### RUN 2 — `specification_paths` naming only this specification

```json
{
  "base": "2e4cc6eb9ae8a34d7a5e81c86d82a5b631dabe7a",
  "head": "b10395db7edad285ae8876ea29403abcb3cbe19b",
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": ["P2-PHASE-01"],
  "specification_paths": ["specs/2026-08-12T2326Z_adopt-domain-repair.md"],
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

**The `EXCLUSIVE` variants are identical but for the one `inclusivity` field.**

**MEASURED — all four runs `overall` PASS, exit 0:**

    RUN 1  INCLUSIVE  exit 0  PASS
    RUN 2  INCLUSIVE  exit 0  PASS      <- stop-governing
    RUN 1  EXCLUSIVE  exit 0  PASS
    RUN 2  EXCLUSIVE  exit 0  PASS      <- stop-governing

    P1 PASS  P2 PASS  P3 PASS  P4 PASS  P5 NOT_APPLICABLE
    P6 PASS  P7 PASS  P8 PASS  P9 NOT_APPLICABLE

**RUN 2's stop is not triggered.** Four commits in range, four on the
first-parent line, four in scope on both readings.

**What RUN 2 excluded: NOTHING. MEASURED: RUN 1's and RUN 2's JSON are
byte-identical**, because the range adds exactly one specification and the
default selection already selects it. **I will not describe this narrowing as
having protected anything.**

**No config value was supplied by me.** `append_only_paths` is
`["DECISION_LOG.md"]`, never `[]`. **`P3` passed truthfully:** MEASURED
`base_bytes` 89541, `head_bytes` 89541, `base_is_byte_prefix_of_head` true,
`deleted_lines_base_to_head` 0.

**`P1` PASS, counted 5 against a stated 5** — the manifest's three additions and
two modifications. **It reached that by reading the `stated:` line as prose**,
since this branch descends from `main` and not from the unlanded declared-total
repair. **Right answer, by the mechanism that repair exists to remove.**

### A10 — Validators

**MEASURED**, the repository's own invocation (`python -m pytest`), run in a
detached worktree at the evidence base and then at commit 4:

    BEFORE  2e4cc6eb   280 passed, 2 deselected
    AFTER   commit 4   280 passed, 2 deselected

**Exit status 0 both times. Identical counts.** **No test changed behaviour and
none was expected to** — this task changes prose and two digest strings.

**And that identity is itself the finding of §6:** the suite passed at the
evidence base **while a gate pin was stale**, and passes now that it is not.
**The suite cannot tell the two states apart.**

## 10. A11 — Commit-message hygiene

**MEASURED.** Proposed messages were scanned before each commit; stored messages
read back after:

    03a195b3  spec: repair the adopted artifact's wording and both stale gate pins
    92749d4e  review: pre-execution review for the adopt-domain repair
    2a1c6261  derivations: make the adopted artifact read as adopted from its first line
    b10395db  gates: re-pin both P2-PHASE-01 artifact digests to their operative bytes

    trailers on each of the four                        none
    'Co-Authored-By' in any stored message                0
    session identifier or URL in any stored message       0
    tool or model attribution in any stored message       0

**Case-insensitive scan over all four stored bodies: 0 matches.**

**Commit 5's INTENDED message**, first line:

    report: record the wording repair and both gate re-pins

## 11. §7 — Rule 16 assessment

**Rule 16 is operative. The specification's candidate junction is correct and I
confirm it without replacing it.**

### The junction: two matching pins do not mean pins are kept correct

**After this task both pins in `GATES.md` match their targets — MEASURED, §6.**
**A reader may infer that gate pins are kept correct. Nothing keeps them
correct.**

**They match because A6 was performed by hand, once, in this task.** **MEASURED
and decisive: no test compares any `GATES.md` pin to any file.** The evidence is
not an argument but a measurement taken twice — the 280-test suite passed at the
evidence base with pin 2 stale, and passes now with it repaired, **with
identical counts both times** (§9). **A suite that cannot distinguish a stale
pin from a correct one is not enforcing pin correspondence, whatever it reports.**

**A check performed once by a person is not a check that runs.** The next task
that edits a hash-pinned artifact will go stale in exactly the same silence
unless its own specification remembers to authorise, perform and verify the
re-pin. **This task did not add automation and was not asked to.** **What would
change it is a validator that enumerates every pin and compares it to its
target — precisely what A6 does by hand — and that is a separate task.**

**The pattern already repeated once.** The adopting task modified a pinned
artifact and left the pin; this task repairs that and would have created a
second stale pin had §4 carried only one re-pin. **Two occurrences in two
consecutive tasks, both caught by a human reading rather than by machinery.**

### A second junction, added: `SATISFIED` still does not mean the gate is ready

**This task changed no prerequisite state, so the previous report's junction
stands unchanged and unweakened.** `P2-PHASE-01` is `PROPOSED`, its
ADMISSIBILITY CONTRACT prerequisite is `UNSATISFIED`, and that block still
reads *"No operational stability or admissibility rule is presently frozen."*
**A reader meeting a tidier `## P2-PHASE-01` block — two matching pins, one
prerequisite satisfied, an artifact whose title now says ADOPTED — may read
tidiness as readiness.** **Nothing about the gate's scientific state changed
here.** **This task made a branch consistent; it did not make a gate ready.**

### A third junction: an artifact that now asserts it is "in force"

**The repaired status paragraph says `**This artifact is in force.**`** That is
true of its governance status and **says nothing about the strength of the
evidence inside it.** The artifact's own §7 and the boundary statement the
adopting task inserted are unchanged and still say adoption certifies no root
completeness, no full-space stability, no thermodynamic dominance, no
negative-`G` exclusion and no finite-density coverage. **"In force" means the
enumeration window is frozen, not that anything was found in it.**

## 12. Stops and clarifications

### `SPECIFICATION_DEFECT` — none

**No anchor failed, no instruction was unsatisfiable, and no stop condition
fired.** A4's *"exactly three hunks"* is measured as three at zero context and
one at default context (§4); **the stop it attaches — a fourth hunk — did not
occur**, and I report both counts rather than picking the flattering one.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — none; the previous task's stop is discharged

**The stop I raised in the adoption report is resolved by authority, not by my
judgement.** §1's PI ruling states that a registered-gate pin denotes exact
operative bytes and that the prohibition on unilateral executor re-pinning
"does not require an authorised modification to leave a knowingly stale pin",
and requires a separately reviewed corrective task before integration.
**This is that task.**

**§9 of the report contract asks specifically whether §1's reading — that the
ruling's principle reaches the SECOND pin — is sound. My answer: yes, and it is
the only reading under which this task is coherent.** The ruling names one pin
because only one was stale when it was issued. **Its stated principle is about
what a pin denotes, not about which pin**, and pin 1 becomes stale for exactly
the reason pin 2 did: an authorised task intentionally changed the bytes.
**Applying the principle to pin 1 is not an extension of the ruling but an
instance of it.** **The alternative reading is self-defeating**: repairing the
wording while re-pinning only the contract draft would land the branch with a
different stale pin, which §0 of the specification names as landing "in exactly
the state it was written to remove." **The Reviewer reached the same reading in
its §3 independently, and the specification's §1 invited a STOP if it did not —
so the reading is authorised twice over, and I did not have to supply it.**

### `REPOSITORY_DEFECT` — two, both pre-existing and out of scope

**1. `P7` is vacuous against the real `GATES.md`.** §7. Known, scheduled for
repair in a separate task, not touched here, and **not offered as evidence for
anything in this report.**

**2. No validator compares a `GATES.md` pin to its target.** §11. **MEASURED
twice in this task.** A6 compensates for it once, by hand. **The absence is the
reason both defects this task repairs were invisible until a person read the
file.**

### `ENVIRONMENT` — none

**No environment failure occurred.** **`CONVENTIONS.md` Rule 13 carries two
conflicting diagnostic orders, a known open item; neither was exercised**, and I
am not naming one as having applied. Nothing was installed.

### `OBSERVATION_METHOD_ERROR` — one, self-caught before it reached a commit

**I drafted the sentence "the phrase `DRAFT` appears nowhere else in the file"
for §4's fourth-defect search, then ran the search, and it was false — the
string occurs three more times.** **None of the three is a status claim** (a
path, a historical revision note, and a reference to the superseded draft), so
the conclusion held; **the literal did not.** §4 now reports the three
occurrences and the fourth surviving label with their line numbers. **The false
sentence never reached a commit, and it was caught by executing the check rather
than by re-reading the claim** — which is the Amendment H discipline working on
its intended target, my own draft.

**A second method choice, recorded because it could have gone the other way.**
RE-PIN 1's value was read from **commit 3's committed blob**
(`git show HEAD:<path> | sha256sum`), not from the working-tree file, as §4
requires. The two agreed; **the working-tree value would have been the
unverified one and is not what was used.**

**RE-PIN 2's value was stated in the specification. I measured it independently
at the evidence base (A3) and compared, rather than pasting the specification's
value into `GATES.md`.** They agreed.

### Secondary findings

- **RUN 2's narrowing excluded nothing** — byte-identical to RUN 1. §9.
- **The two prospectivity readings differ in one field and no verdict.** §9.
- **`P1` passed by reading a structured `stated:` declaration as prose**, on a
  branch that descends from `main` rather than from the unlanded declared-total
  repair. §9.
- **Four `draft`-related strings survive in the adopted artifact, all correct
  in context**, listed with line numbers in §4. **None was touched.**
- **The validator counts are identical across a state change that mattered.**
  §9, §11.

### Anything ambiguous, unsatisfiable, or that I would have specified differently

- **A4 should have said "three hunks at zero context", or asked for the change
  to be shown per anchor.** As written, a literal reading of "exactly three
  hunks" is falsified by git's default context on adjacent edits, and an
  executor optimising for the criterion's words rather than its purpose could
  have reported `-U0` alone and never mentioned that the default view shows one.
  **The purpose is that nothing beyond the three substitutions changed, and that
  is established in §4 by decomposition and line accounting.**
- **A6 is the best criterion in this specification and it should be a test.** It
  is the only check in this task that could have failed for a reason nobody
  anticipated, and it is performed by hand. **I would specify the validator as
  the next task rather than leaving it to the next specification to remember.**
- **A3 asked for four blob ids and named no expected values**, so a mismatch
  there cannot be a STOP. The two SHA-256 values it does pin — one of them with
  an explicit STOP — are where the criterion has teeth. **A pinned input whose
  value the executor supplies is a record, not a check**, and I noted the same
  thing about the adopting task's A3.
- **Nothing in this task or the adopting one prevents the next recurrence.**
  §11.

## 13. Confirmations the report contract asks for explicitly

- **`P2-PHASE-01`'s `Status:` line reads `PROPOSED`.** MEASURED, base and head.
- **MICROSCOPIC PARAMETER DOMAIN reads `SATISFIED`; PHASE INPUT /
  ADMISSIBILITY CONTRACT reads `UNSATISFIED`.** Both MEASURED at commit 4.
- **`C1`, `C2` and `C3` were not answered.** No claim is made about the
  complement root's provenance, the global sign of `I0(Mhat)`, or whether the
  curvature asymmetry is physical.
- **`scripts/p2_phase01_scalar_exploratory.py` was NOT read.** MEASURED: the
  whole of `scripts/` is blob-identical between the evidence base and commit 4.
- **No enumeration was run and nothing was computed.**
- **No superseded-register entry was written.** MEASURED:
  `docs/BRANCHING_POLICY.md` is blob-identical. **Nothing is superseded by this
  task** — the adoption branch is completed, not replaced.
- **`main` was not touched and no merge was performed.**
