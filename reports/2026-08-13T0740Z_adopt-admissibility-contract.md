# Report — adopt the phase input / admissibility contract

Specification: `specs/2026-08-13T0740Z_adopt-admissibility-contract.md`
Review: `reviews/chatgpt/2026-08-13T0740Z_adopt-admissibility-contract.md` — APPROVED FOR EXECUTION
Evidence base: `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab` (authoritative `main`)
Branch: `science/adopt-admissibility-contract`, cut from that commit.
**`main` was not touched, nothing was merged, and the parameter-domain adoption
branch was neither merged nor inspected.**

**Every figure is labelled MEASURED or INTENDED.** **Nothing here claims to
measure commit 5.**

---

## 0. Executive summary

**A rule is frozen and nothing was evaluated against it.** Standard C, the PI
ruling and §4's reclassification are transcribed verbatim — 456, 2822 and 2349
characters, each verified present in both the specification and the artifact.
**All three `OPEN-AC` items are marked `STILL OPEN`; none is resolved, closed,
downgraded or partly settled, and no fourth was added.** `GATES.md` changed in
one region. **Both pins match at the head.** A12's RUN 2 — stop-governing —
**PASSED exit 0 on both prospectivity readings.**

**All four A7 invariants hold**, including the fourth: **the MICROSCOPIC
PARAMETER DOMAIN prerequisite still reads `UNSATISFIED`, and its block is
byte-identical to the evidence base.** **That is not a regression** — its
adoption sits on a branch this task does not carry, and §3 requires the reason
be reported so a reader does not conclude the domain question is unresolved. **It
is resolved, on another branch, and `P2-PHASE-01` stays `PROPOSED` because this
branch cannot see it.**

**One measurement contradicts the specification, and it makes the risk §2a names
larger rather than smaller.**

**§11 states "TEN lines separate the end of one from the start of the other" and
§2a concludes a conflict is "possible rather than certain … far enough that it
may not [fold into one hunk]".** **MEASURED at the evidence base, by §11's own
method:**

    1010-1019  the MICROSCOPIC PARAMETER DOMAIN block
    1020       blank
    1021-1027  the PHASE INPUT / ADMISSIBILITY CONTRACT block
    1028       blank

**The two blocks are separated by ONE blank line.** **Ten is the length of the
first block's body, not the separation.** **My own hunk's leading context under
git's default is lines 1018–1020, which lie inside the other block** — so a
branch that rewrites the first block and this one, which rewrites the second,
produce overlapping hunks. **A textual conflict at integration is likely, not
merely possible.**

**Nothing about the task changes.** §2a's operative instruction — take both
blocks, then verify all four pins in the merged file — is unaffected and more
necessary, not less. **The estimate was wrong in the direction that would have
under-warned the integrator, so it is corrected here.**

**No candidate was evaluated against standard C.** §11 of this report answers
the question the report contract asks about that, and the answer is that the
temptation was concrete.

---

## 1. A1 — Refs and inputs

**MEASURED. All four.**

```
refs/heads/main                                1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
GATES.md blob at 1cb5550f                      849a4fbfe62d6478f092a84b0175357a74bbbb06
contract DRAFT sha256                          a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73
contract DRAFT blob                            5f020f33a9230d1aaa7c98c79db49b1efcb822f6
the pin at GATES.md:1026                       a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73
                                               EQUAL to the draft's digest
```

**All match the specification's A1 values. No STOP.** **The pin was correct at
the evidence base**, which is why A8 stales it and A6 moves it.

**Pins in `GATES.md` at the base, counted over the whole file: exactly TWO**, at
lines 1015 and 1026, as §11 records.

## 2. A2 — The review, committed unedited, with its specification digest

**MEASURED.** The review carries
`reviewed specification SHA-256: e19e45b48f092f189aa13658fcf814acca0d0a300e9f24f7be333d4e66edfe62`.

    supplied specification file, sha256
      e19e45b48f092f189aa13658fcf814acca0d0a300e9f24f7be333d4e66edfe62   EQUAL

    supplied review   84fdbeb9f76903195bd640200d27663b9b60fe4f0ee3aa6fad32cc643e15bf96
    committed blob    84fdbeb9f76903195bd640200d27663b9b60fe4f0ee3aa6fad32cc643e15bf96
    EQUAL

**Filled in, correct, neither blank nor naming a different digest. A2's stop is
not triggered.** Both arrived as FILES; Rule 18 satisfied on both. The review's
own closing condition — *"provided the committed specification is byte-identical
to the reviewed file"* — is met.

## 3. A3 — The adopted artifact, its digest, and its labels

**MEASURED, from the COMMITTED BLOB at commit 3:**

    derivations/P2-PHASE-01_input_admissibility_contract.md
    sha256  e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3

**That value, not a working-tree one, is what A6 embeds.**

**The labels used, with the definitions the artifact itself carries.** §5
requires them listed before writing and defined in the artifact; **both are
done, and the artifact carries its own definitions section so a later reader can
check every label against a definition in the same file:**

    ADOPTED               this artifact is in force as the repository's
                          statement of the admissibility standard for
                          P2-PHASE-01
    FROZEN                fixed by this adoption; changed only by a later task
                          authorised to change it
    PI RULING             a decision recorded verbatim as issued by the PI. It
                          is a decision, not a derivation, and nothing presents
                          it as a computed result
    STILL OPEN            not resolved, not closed, not downgraded and not
                          partly settled by this adoption
    EVALUATION-INPUT GAP  a missing input needed to APPLY the frozen rule, as
                          distinct from a gap in the rule's DEFINITION. The
                          rule is complete; the inputs are not
    SUPERSEDED            an earlier artifact retained as historical evidence
                          and not operative

**MEASURED — every kind label used is defined, and no other kind label appears.**
A whole-file count over the vocabulary this programme has used elsewhere:

    ADOPTED 3   FROZEN 3   PI RULING 3   STILL OPEN 6
    EVALUATION-INPUT GAP 4   SUPERSEDED 2
    MEASURED 0   DERIVED 0   RECOMMENDATION 0   CAUTION 0

**The four labels that caused the parameter-domain artifact's four repair tasks
are absent entirely.**

**One string needs stating rather than hiding: `SATISFIED` occurs twice**, both
inside verbatim transcriptions — in the PI ruling and in §4's text. **It is a
prerequisite state in `GATES.md`'s vocabulary, not a kind label on a statement**,
so it is deliberately not in the label set. **I report it because deciding it is
"not a kind label" is a judgement, and a later reader should be able to see the
judgement rather than infer it.**

**Ordering.** §5 lists six required contents in order; the artifact carries all
six in that order, with the label-definitions section inserted between (1)
status and (2) the ruling. **§5 requires the definitions to be in the artifact
and does not place them, so this is the only free choice I made about
structure**, and it puts the definitions before the first label-bearing content.

## 4. A4 — Standard C transcribed, and every restatement of `C-ii`

**MEASURED mechanically.** The three blocks were extracted programmatically from
the committed specification blob by exact substring slice and written into the
artifact unaltered; both files were then searched for each extracted string:

    block                          chars   in specification   in artifact
    the PI ruling                    456        True             True
    standard C (C-i, C-ii, C-iii,
      and the transverse paragraph) 2822        True             True
    §4's reclassification           2349        True             True

**Nothing was retyped. A4's and A5's rewritten-criterion STOPs are not
triggered.**

### Every restatement of `C-ii` in the adopted artifact, reported individually

**A4 requires each one searched out and confirmed to name the `C-i`-and-`C-iii`
comparison set rather than admissibility. MEASURED — five, plus the criterion
itself:**

**1. The criterion, lines 65–77 (verbatim).** *"define the COMPARISON SET S as
every stationary solution satisfying C-i and C-iii — the non-thermodynamic
conditions alone, with C-ii itself excluded from the test."* **Names C-i and
C-iii. Not recursive.**

**2. The repair paragraph, lines 85–93 (verbatim).** This is the one that
*mentions* the recursive form, and it does so to reject it: *"An earlier
statement of `C-ii` compared a candidate against competing ADMISSIBLE stationary
solutions, while `ADMISSIBLE` was itself defined as `C-i AND C-ii AND C-iii`.
That is a self-referential definition, not a decision rule."* **It does not
phrase C-ii recursively; it names the defect and states the repair — "Defining
`S` from `C-i` and `C-iii` alone removes the recursion."** **§5(3) requires this
paragraph be present, so its inclusion is mandated, not incidental.**

**3. Line 123, `OPEN-AC-1`:** *"An input to C-ii whenever a channel beyond the
scalar enters the comparison."* **No admissibility reference.**

**4. Line 130, `OPEN-AC-3`:** *"THE input to C-ii. The cross-family part needs
the common normalisation that does not exist."* **No admissibility reference.**

**5. Line 155, the dependency paragraph:** *"`C-ii`'s comparison is a depth
comparison under a common normalisation whatever the symmetry analysis
returns."* **No admissibility reference.**

**No summary in the adopted artifact phrases `C-ii` in terms of competing
ADMISSIBLE solutions.** **The same is true of the `GATES.md` block** — §6 below
— **which is where the defect reached a reviewer the second time**, and which
now carries an explicit paragraph forbidding the recursive phrasing in that
block.

## 5. A5 — §4 transcribed, all three `STILL OPEN`

**MEASURED.** The 2349-character block is present verbatim in both files, and
within it:

    OPEN-AC-1   STILL OPEN
    OPEN-AC-3   STILL OPEN
    OPEN-AC-4   STILL OPEN

    occurrences of "STILL OPEN" in the artifact                6
    items recorded as resolved / closed / downgraded / partly
      settled                                                  0
    fourth OPEN-AC item added                                  none

**The work order `OPEN-AC-4` → `OPEN-AC-3` → `OPEN-AC-1` is present with its
reason**, and with the narrowing the specification insists on: **`AC-4` is
logically prior to applying `C-i`**, and **it is expressly not claimed that
`AC-4` fixes the form of the criteria `AC-3` or `AC-1` feed.** The transcription
also carries *"Do not record this order as a schedule or a commitment"* — **it is
a dependency statement, and this report does not treat it as a plan.**

**A5's stop — an item recorded as anything other than `STILL OPEN` — is not
triggered.**

## 6. A6 — The `GATES.md` block replacement

**MEASURED. Both anchors occur exactly once at the evidence base**
(`### Unsatisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT` and
`### Integrated exploratory evidence`). **The diff is ONE region at
`--unified=0`.** Full diff:

```diff
@@ -1018,13 +1018,34 @@ The future artifact must decide and bound scan-eligible coupling `G`, and must
 decide whether cutoff ratios and finite-density `μ` are FIXED INPUTS or SCAN
 DIMENSIONS. Any admitted scan dimension must carry a frozen range.
 
-### Unsatisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT
-Artifact state: **DRAFTED / NOT ADOPTED**. Prerequisite state:
-**UNSATISFIED**. Owner: Paper 2. Canonical label: **PHASE INPUT /
-ADMISSIBILITY CONTRACT**; not a gate ID. Draft:
-`derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md`
-(sha256 `a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73`).
-No operational stability or admissibility rule is presently frozen.
+### Satisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT
+Artifact state: **ADOPTED**. Prerequisite state: **SATISFIED**.
+Owner: Paper 2. Canonical label: **PHASE INPUT / ADMISSIBILITY
+CONTRACT**; not a gate ID. Adopted artifact:
+`derivations/P2-PHASE-01_input_admissibility_contract.md`
+(sha256 `e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3`).
+Superseded draft:
+`derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md`.
+
+An operational admissibility standard is frozen: full
+condensate-space Hessian positivity transverse to symmetry-required
+flat directions; thermodynamic selection against the comparison set
+of stationary solutions satisfying the non-thermodynamic conditions
+C-i and C-iii, under a common normalisation; and symmetry accounting
+sufficient to identify those flat directions. Per PI ruling, a rule
+that can decide a candidate is operational whether or not its inputs
+presently exist.
+
+The comparison set is defined WITHOUT reference to admissibility,
+deliberately. A summary phrased as "no competing ADMISSIBLE solution
+deeper" would define admissibility in terms of itself; the adopted
+artifact does not, and this block must not.
+
+**This prerequisite being SATISFIED means a rule exists. It does not
+mean any candidate has been assessed, and it does not mean the
+evaluation inputs are complete.** Three remain open —
+`OPEN-AC-1`, `OPEN-AC-3`, `OPEN-AC-4` — and they are
+evaluation-input gaps, not rule-definition gaps.
 
 ### Integrated exploratory evidence
 The reviewed scalar stationary study is included in the integrated repository
```

**`GATES.md` changed there and nowhere else.** **The block records the frozen
standard, the PI ruling's operational reading, the non-recursion of the
comparison set, and — in bold, in the block itself — that `SATISFIED` means a
rule exists and not that any candidate has been assessed.**

## 7. A7 — The four gate invariants

**MEASURED at commit 4 against the evidence base:**

    1  '^## P2-' section count        base 14   head 14        UNCHANGED
    2  every '^Status:' line          15 lines, TEXTUALLY IDENTICAL
    3  P2-PHASE-01                    Status: PROPOSED
    4  MICROSCOPIC PARAMETER DOMAIN   Prerequisite state: **UNSATISFIED**

**And the fourth's block is byte-identical to the evidence base — 11 lines,
`diff` empty.** **§8 forbids touching it and it was not touched.**

**The reason for the fourth, reported as §3 requires so it is not read as a
regression.** **The microscopic parameter domain question is resolved — on
`science/adopt-parameter-domain-labels`, a branch this task is cut independently
of and does not carry.** **At THIS evidence base that adoption does not exist,
so the block correctly reads `UNSATISFIED` here, and `P2-PHASE-01` stays
`PROPOSED` for that reason and not because the domain is unsettled.** **A reader
of this branch alone would draw the wrong conclusion without this sentence**,
which is why the specification demanded it.

## 8. A8 — The pointer insertion

**MEASURED.** Inserted immediately after the draft's first heading line, which
was verified to be an H1 before writing. Full diff:

```diff
@@ -1,5 +1,12 @@
 # `P2-PHASE-01` phase input / admissibility contract — DRAFT, NOT ADOPTED
 
+**SUPERSEDED.** Adopted as
+`derivations/P2-PHASE-01_input_admissibility_contract.md`. This file
+is retained as historical evidence and is not operative. Its
+`OPEN-AC` entries are unchanged and remain OPEN; the adopted
+artifact reclassifies them as evaluation-input gaps without
+resolving any of them.
+
 ## Status and evidence boundary
 
 This is a **DRAFT, NOT ADOPTED** prerequisite artifact.  It does not define an
```

**A pure insertion: the hunk contains no `-` line.** **No pre-existing text was
edited or replaced, no `OPEN-AC` body was altered, and no verdict in that file
was changed.** **The pointer says the draft's `OPEN-AC` entries remain OPEN and
that the adopted artifact reclassifies them without resolving any**, so the two
files do not contradict each other.

## 9. A9 — Both pins match at the head

**MEASURED at the head**, every occurrence of `` (sha256 `<64 hex>`) ``
enumerated over the whole file, with the artifact path taken from the line
immediately above.

**AT-LEAST-ONE ASSERTION: 2 pins found, `>= 1` satisfied** — coded as an abort,
not assumed.

    pin 1   GATES.md line 1015
      path    derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
      pinned  d8e154690e0b3d8131260a9ed0ce0ef804dd5652d21c022c6b29677b90d3eba4
      actual  d8e154690e0b3d8131260a9ed0ce0ef804dd5652d21c022c6b29677b90d3eba4
      MATCH   — untouched by this task, as required

    pin 2   GATES.md line 1026
      path    derivations/P2-PHASE-01_input_admissibility_contract.md
      pinned  e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
      actual  e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
      MATCH   — moved from the draft to the adopted artifact

    PINS FOUND: 2   all matching: yes

**The contract pin moved and the parameter-domain draft pin did not.** **A8
staled the old contract pin by inserting into the draft; A6 moved the pin to the
adopted artifact rather than re-pinning the draft**, which is why the draft's own
digest no longer appears in `GATES.md` at all.

## 10. A10, A11 — Scope and protected paths

**A11, MEASURED at commit 4**, whole-tree `git ls-tree -r` blob comparison:

    PATHS COMPARED (every path existing at the evidence base)   343
    blob-identical at commit 4                                  341
    changed                                                       2
    changed set == A10's modify: list                          TRUE
    removed                                                       0
    added                                                         3

    scripts/p2_phase01_scalar_exploratory.py                     IDENTICAL
    results/.../scalar_stationary.json                           IDENTICAL
    derivations/P2-DEFERRED-ITEMS.md                             IDENTICAL
    derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md IDENTICAL

    results/   differing: none      scripts/   differing: none
    tests/     differing: none

**All three explicitly required confirmations hold**, and the parameter-domain
draft is untouched as well — **this task does not carry that line and did not
reach into it.**

**The final scope, INTENDED** — commit 5 does not exist while this is written:

    stated: 4 additions, 2 modifications
    base: 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    head: <commit 5, INTENDED>
    mode: exact
    add:
      derivations/P2-PHASE-01_input_admissibility_contract.md
      reports/2026-08-13T0740Z_adopt-admissibility-contract.md
      reviews/chatgpt/2026-08-13T0740Z_adopt-admissibility-contract.md
      specs/2026-08-13T0740Z_adopt-admissibility-contract.md
    modify:
      GATES.md
      derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Six paths. MEASURED at commit 4: three of the four additions are in place and
both modifications are; the fourth addition is this file.** **The scope measured
base-to-commit-5 is post-report evidence and is not claimed here.**

## 11. A12 — The two checker runs, and A13

Base `1cb5550f…`, head **commit 4** `f745d306…`. **Both prospectivity readings
run.**

### RUN 1 — default subject selection, observational, governs nothing

```json
{
  "base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
  "head": "f745d30615328d777a03b2dafc704ce892408b88",
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": ["P2-PHASE-01"],
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

### RUN 2 — `specification_paths` naming only this specification

```json
{
  "base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
  "head": "f745d30615328d777a03b2dafc704ce892408b88",
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": ["P2-PHASE-01"],
  "specification_paths": ["specs/2026-08-13T0740Z_adopt-admissibility-contract.md"],
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

**RUN 2's stop is not triggered.** **What RUN 2 excluded: NOTHING** — RUN 1's and
RUN 2's JSON are byte-identical, because the range adds one specification and the
default selection already selects it. **I will not describe the narrowing as
having protected anything.**

**No config value was supplied by me.** `append_only_paths` is
`["DECISION_LOG.md"]`, never `[]`, and **`P3` passed truthfully**: MEASURED
`base_bytes` 89541, `head_bytes` 89541, `base_is_byte_prefix_of_head` true,
`deleted_lines_base_to_head` 0. **`P1` PASS, counted 6 against a stated 6.**

### `P7` returned `PASS` and it is evidence of nothing

**MEASURED:** `section_count_base` 0, `section_count_head` 0, against a
`GATES.md` carrying fourteen gates. `GATE_HEADING` is
`^## (P2-[A-Z0-9-]+)\s*$` and every real heading continues past the ID, so **P7
compared two empty maps.**

**This task modifies `GATES.md`, so the vacuous green is again exactly where it
is most dangerous** — and it was handed the strongest possible declaration,
`authorised_modified_gates: ["P2-PHASE-01"]`, which a parser matching nothing
cannot enforce. **The edit's confinement rests on A6's single-region diff, A7's
four invariants, A9's pin table and A11's 341-of-343 blob identity — all direct
measurements of the files.**

### A13 — Commit-message hygiene

**MEASURED.** Proposed messages scanned before each commit; stored messages read
back after:

    fb5f64e6  spec: adopt the phase input / admissibility contract
    24cf15a2  review: pre-execution review for the admissibility-contract adoption
    9913bba8  derivations: adopt standard C as the frozen admissibility rule
    f745d306  gates: mark the admissibility-contract prerequisite SATISFIED

    trailers on each of the four                        none
    'Co-Authored-By' in any stored message                0
    session identifier or URL in any stored message       0
    tool or model attribution in any stored message       0

**Case-insensitive scan over all four stored bodies: 0 matches.**

**Commits, MEASURED, in the order §9 specifies:**

    commit 1  fb5f64e658f5dbefa4f9aa4456ed8af932002570  specs/...
    commit 2  24cf15a2ed3786aa516a84cb783373f4b5ae1986  reviews/chatgpt/...
    commit 3  9913bba830f4bfc779a15dabfe1ce383bddfd5e5  the adopted artifact
    commit 4  f745d30615328d777a03b2dafc704ce892408b88  GATES.md + the draft
    commit 5  INTENDED                                  reports/...

**Commit 3 precedes commit 4 because A6 embeds commit 3's blob digest**, read
from the blob and not from the working tree.

**The UTC token `0740` and the day `13` were MEASURED** (`date -u`) at commit 1.

**Commit 5's INTENDED message**, first line:

    report: record the admissibility-contract adoption and the adjacency correction

## 12. Does the adopted artifact read as though admissibility had been settled?

**No, and the structure is what prevents it rather than a disclaimer at the end.**

**The status line says the artifact is in force and immediately says what that
means:** *"It freezes a rule and evaluates nothing. No candidate has been
assessed against standard C by the task that adopted it."* **That sentence is the
third line of the file.**

**`What adoption does NOT establish` is a standalone section, not a footnote**,
as §5(5) requires — a reader meets it without searching. It states that a rule
exists and nothing has been measured against it; that no candidate is admissible
or has been assessed; that one of the three inputs has not been started at all;
that the gate's *Required computations* still read `(not started)`; and that
**standard C was chosen knowing it is not evaluable now.**

**The `GATES.md` block carries the same limit in bold**, so the reader who never
opens the artifact still meets it: *"This prerequisite being SATISFIED means a
rule exists. It does not mean any candidate has been assessed, and it does not
mean the evaluation inputs are complete."*

**The one place a hurried reader could still go wrong is the word `SATISFIED`
itself**, in a gate summary listing prerequisites. **Nothing in this task can fix
that**; it is the vocabulary `GATES.md` uses, and the block spends four lines
qualifying it.

## 13. Did freezing standard C make me want to evaluate anything against it?

**Yes, concretely, and I did not.**

**The pull was specific rather than general.** `C-i` distinguishes the full
condensate-space Hessian from *"the restricted one-dimensional curvature, which
is what every stored result to date carries"* — **and I had just spent the
preceding task deriving exactly what that restricted curvature equals at a
stationary root.** The natural next step is to observe that every stored
`reduced_curvature` is therefore the wrong object for `C-i`, and to say which
candidates that disposes of.

**§8 forbids evaluating anything against standard C — not the negative-mass
branch, not the ordinary branch, not the trivial vacuum — and I evaluated
none.** **The adopted artifact contains no assessment, no candidate is named in
it as passing or failing any condition, and this report names none either.**

**The distinction I held to:** `C-i`'s own text already says the restricted
curvature is not what it asks for, and that sentence is transcribed. **Stating
which candidates it therefore disposes of would be an evaluation**, and it is a
separate task with its own pre-registration.

**A second, smaller pull.** §4's `OPEN-AC-3` records that a within-scalar
comparison *"may be available, since the algebraic branches share one potential
and one stated zero"*. **That is close to an invitation to check.** **I did not
open the results file in this task at all.**

## 14. §7 — Rule 16 assessment

**Rule 16 is operative. I confirm the specification's candidate and add one this
execution exposed.**

### The junction: `SATISFIED` records a rule, not an answer

**After this task `GATES.md` reads `SATISFIED` for the admissibility
prerequisite. A reader may infer that admissibility has been settled, or that
the gate is closer to an answer. Neither is true. A rule now exists and nothing
has been measured against it.**

**No candidate is closer to an admissibility verdict, and no additional
scientific evidence toward the gate's physical verdict has been produced. A
procedural step was completed and nothing was measured.** The three inputs the
rule needs remain open — **`OPEN-AC-1` not started at all.**

**It is a step, and it is not a scientific one.** **Standard C was chosen knowing
it is not evaluable now**, and the PI took it over two weaker standards that
would have let the gate pass on a reason weaker than the question it asks.

**Where a reader meets it:** in the `GATES.md` block itself, in bold, four lines
under the word `SATISFIED`; and in the adopted artifact's standalone section.
**Not only in this report.**

### Second junction: `P7: PASS` checked nothing

**Stated in §11 adjacent to the result.** **A `PASS` from a vacuous check is the
most dangerous green this programme has named, and it appeared in a task that
modifies `GATES.md` while holding the strongest possible gate declaration.**

### A third junction this execution added: two `SATISFIED` prerequisites will never be seen together on this branch

**On this branch the gate shows one prerequisite `SATISFIED` and one
`UNSATISFIED`. On the parameter-domain branch it shows the reverse. Neither
branch shows the state the programme is actually in**, and **only an integration
that takes both blocks will.** **A reader inspecting either branch alone will
under-count the progress made, and a reader who sees a `SATISFIED` line may
assume the other is too.** **The correction in §0 makes this sharper**: the two
blocks are adjacent, so the merge that produces the true state is also the merge
most likely to conflict. **§2a's instruction — take both blocks, then verify all
four pins — is the whole of what protects that.**

### The limit on this task's own evidence

**Nothing here was measured about physics.** Every measurement in this report is
about files: digests, blob identity, line ranges, diffs, checker output. **The
one substantive claim — that standard C is a decision rule rather than a
recursive predicate — is a claim about the text of a definition**, and it rests
on reading the definition, not on applying it. **Whether standard C is the right
standard is a PI judgement recorded as such, and this task neither tested nor
could test it.**

## 15. Stops and clarifications

### `SPECIFICATION_DEFECT` — none blocking; one measurement in the pre-issue record is wrong

**No stop condition fired**, no anchor failed, and no criterion was
unsatisfiable. A4's and A5's rewritten-text STOPs, A7's invariants and A9's
at-least-one assertion were all satisfied by measurement rather than by
assertion.

**§11's adjacency line is wrong, and §2a's conclusion inherits the error.**
§11 states *"TEN lines separate the end of one from the start of the other"*;
**MEASURED at `1cb5550f` by §11's own stated method, the MICROSCOPIC PARAMETER
DOMAIN block occupies lines 1010–1019, line 1020 is blank, and the PHASE INPUT
block begins at 1021 — a separation of ONE blank line.** Ten is the length of the
first block's body.

**§2a's inference is therefore too optimistic**: *"far enough that it may not
[fold into one hunk]"*. **My own hunk's default leading context is lines
1018–1020, inside the other block.** **A conflict at integration is likely, not
merely possible.**

**This is a defect in a premise, not in an instruction**, and it errs in the
direction that would have under-warned the integrator. **§2a's operative
instruction is unaffected and more necessary.** **§11 itself carries a
`RETRACTED` note correcting an earlier "two lines apart / likely" to "ten lines /
possible" — the retraction moved the estimate the wrong way**, and the
measurement above is what the original characterisation was closer to.

### `OBSERVATION_METHOD_ERROR` — none

**No measurement in this report was taken through a truncated view.** The pin
enumeration, the label audit, the `C-ii` restatement search and the protected-path
comparison were each run over whole files with no `head`, no `tail` and no
sampling. **The three verbatim blocks were extracted programmatically rather than
retyped**, and the adopted artifact's digest was read from the committed blob.

**One method decision worth recording.** **I verified A7's fourth invariant by
extracting the MICROSCOPIC PARAMETER DOMAIN block from both revisions and
`diff`-ing them, rather than by grepping for the word `UNSATISFIED`.** A grep
would have passed on a block whose surrounding text had changed; **the `diff`
establishes 11 lines byte-identical, which is what §8's prohibition actually
requires.**

### `REPOSITORY_DEFECT` — one, pre-existing and out of scope

**`P7` is vacuous against the real `GATES.md`.** §11. Known, untouched, **and not
offered as evidence for anything** — A6, A7, A9 and A11 carry that weight.

**No new repository defect was found.** In particular **both pins matched before
this task and both match after**, which is the first task in this line where that
was true at both ends without a repair.

### `ENVIRONMENT` — none

**No environment failure occurred.** **`CONVENTIONS.md` Rule 13 carries two
conflicting diagnostic orders, a known open item; neither was exercised**, and I
am not naming one as having applied. Nothing was installed; the exploratory
script was not read or run; `C2` was not answered.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — none

**The meaning of `operational` was the ambiguity, and it is settled by a PI
ruling recorded verbatim as a ruling rather than presented as a derived
result.** **I did not have to interpret it and did not.** The review reached the
same reading independently and says so.

### Secondary findings, kept separate

- **`SATISFIED` appears twice in the adopted artifact**, both inside verbatim
  transcriptions, as a prerequisite state rather than a kind label. §3 reports it
  because the classification is a judgement.
- **The label-definitions section's placement was the only structural choice I
  made**; §5 requires the definitions in the artifact and does not place them. §3.
- **RUN 2's narrowing excluded nothing** — byte-identical to RUN 1. §11.
- **The two prospectivity readings differ in one field and no verdict.** §11.
- **`P1` passed by reading a structured `stated:` declaration as prose**, on a
  branch cut from `main`, which does not carry the declared-total repair.
- **The draft's own `OPEN-AC-2` and `OPEN-AC-5` were not touched**, and the
  adopted artifact says explicitly that they belong to a separate line.

### Anything ambiguous, unsatisfiable, or that I would have specified differently

- **§11's adjacency measurement should have been a line range, not a count.**
  "Ten lines separate" is ambiguous between the gap and the block length, and the
  record chose the reading that made the risk look smaller. **A range —
  `1010–1019`, blank `1020`, `1021–1027` — cannot be misread**, and it is what
  §11's own stated method produces.
- **§5's ordering requirement and its label requirement are in tension, and the
  specification does not resolve it.** The six contents are ordered; the label
  definitions must be in the artifact but are unplaced. **I put them second and
  said so**, but a specification that had said where would have removed a free
  choice from a task whose whole subject is labels.
- **A3 asks for the artifact's digest and does not pin an expected value**, so a
  mismatch there cannot be a STOP. That is unavoidable — the value does not exist
  until commit 3 — **but it means A3 is a record and A1 is the check**, and only
  A1 can stop the task.
- **§8 forbids referencing the parameter-domain adoption branch, and §2a
  describes what will happen when it meets this one.** **I complied by measuring
  the adjacency at the evidence base rather than by inspecting that branch**,
  which is what §11's method prescribes anyway. **The prohibition and the
  reporting duty are compatible, but only because the measurement that matters is
  available at the base.**
- **Nothing in this task can verify the claim it most rests on** — that standard
  C, once its inputs exist, decides. **That is a property of a rule that has
  never been applied**, and it will be tested the first time somebody tries to
  apply it, not before.
