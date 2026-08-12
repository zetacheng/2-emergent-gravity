# Report — replace P1's prose inference with a declared total

Specification: `specs/2026-08-12T2015Z_p1-declared-total.md`
Review: `reviews/chatgpt/2026-08-12T2015Z_p1-declared-total.md` — APPROVED FOR EXECUTION
Evidence base: `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`
Branch: `governance/p1-declared-total`, cut from that commit. **`main` was not touched.**

**Every figure in this report is labelled MEASURED or INTENDED.** **Nothing here
claims to measure commit 5**, which does not exist while this file is written.

---

## 0. Executive summary, including three findings the specification did not predict

**The repair is built and behaves as specified.** P1 reads its total from a
`stated:` record inside the scope block; no sentence anywhere is consulted; the
prose-count pattern is gone from the module. **A5, the criterion the
specification calls the point of the task, matched its prediction exactly**: 38
rows, one `PASS`, thirty-seven `NOT_PARSEABLE`, splitting 29 / 6 / 2. **A7
passes**: this task's own specification parses under the syntax it commissions.

**Three things I measured differ from what the specification states, and one is
a STOP.**

**FINDING 1 — §0's and A6's diagnosis of the old parser is not reproducible
against the actual blob, and A6's stated "Before" is wrong.** §9 records that
the corpus figures were obtained from *"the parser at `1922fe88…`
**re-implemented** line for line"*. I ran the extracted blob itself. It agrees
with §0 on the headline — **10 PASS and 19 non-PASS over the twenty-nine
scope-bearing specifications** — and disagrees on the split and on the
mechanism:

    §0 / §9 state    17 FAIL + 2 NOT_PARSEABLE ("two files with no count
                     sentence"); dominant mode = the WRONG SENTENCE is selected
    MEASURED          3 FAIL + 16 NOT_PARSEABLE; dominant mode = NO sentence is
                     selected, because the backward walk breaks at the first
                     markdown heading and the count sentence sits in an
                     earlier section

**A6 names three specifications and states "Before: `FAIL`. After:
`NOT_PARSEABLE`." All three measure `NOT_PARSEABLE` before, not `FAIL`.**
A6's stop condition — *"if any still reports `FAIL`, prose is still being
consulted"* — is satisfied: none does. **The repair is unaffected**; the
declared total removes both modes. **But the premise on which the task's §0
argues for it is half wrong, and the "nineteen false positives" of A6's heading
were nineteen non-passes of two different kinds.** §6 below states what this
does and does not change.

**FINDING 2 — A10's RUN 2 cannot reach exit 0 under any configuration §7
permits. I stopped there and did not choose.** Detail in §10 and §14.

**FINDING 3, out of this task's scope and reported because it is the same
defect class — P7 is vacuous against the real `GATES.md`.** Its heading
pattern is `^## (P2-[A-Z0-9-]+)\s*$`; the real file's fourteen gate headings
read `## P2-HK-01 — Heat-kernel species coefficients`. **The pattern matches
zero of them**, so whenever P7 is exercised on this repository it compares two
empty section maps and reports `PASS`. **MEASURED: `section_count_base` 0,
`section_count_head` 0** in RUN 2-D's JSON below. **The forty-two fixtures did
not catch it because their fixture gate file writes bare IDs.** This is the P1
lesson repeating on another property, and §2 of the specification forbids me to
touch P7. **It is reported, not fixed.**

**The honest summary of what this task did to coverage:** ten specifications
passed P1 before; **one does now.** That is a reduction in coverage and an
increase in what a pass means. §13 says which it reads as.

---

## 1. A1 — Refs

**MEASURED**, read from the remote:

```
git ls-remote origin refs/heads/main
1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab	refs/heads/main
```

**Matches the evidence base. No STOP.** Local `main` is stale by design and was
not repaired.

## 2. A2 — Specification and review, supplied as files, committed unedited

**MEASURED.** **Both the specification and the review arrived as FILES.**
Neither was pasted; no delimiter question arose; Rule 18 is satisfied on both.
The review names this task — *"Task reviewed: replace P1's prose inference with
a declared total"* — and this evidence base, and carries **APPROVED FOR
EXECUTION**. It is not a review of a different specification.

    supplied  specification  ca576015a620ed1589b2977df7ff78e614c26eecbb182c2c3cf880b22777d678
    committed specification  ca576015a620ed1589b2977df7ff78e614c26eecbb182c2c3cf880b22777d678
    EQUAL

    supplied  review         770e4ccd4676ba9b199f334ac0d1257ab1a9cfd788e000eaa2a080c1bf219e20
    committed review         770e4ccd4676ba9b199f334ac0d1257ab1a9cfd788e000eaa2a080c1bf219e20
    EQUAL

**A first review of an earlier draft of this task was supplied and withdrawn by
the PI before execution** (*"i misread and thought it was approved, please do
not process"*). **Nothing was committed under it and no branch existed at that
point.** The withdrawn review is not in this branch.

## 3. A3 — Pinned inputs at the evidence base

**MEASURED**, `git rev-parse 1cb5550f:<path>`, Git blob ids:

```
1922fe88f3a29909a006b2adf03cfb5229d20d84  scripts/governance_tools/task_checker.py
a68568568f50b2bfbccbcbe4f87bcd70b55b6423  tests/test_task_checker.py
183df9468c986fd8ba4cd5c2ecaf95ee1561adb4  derivations/GOVERNANCE-ENFORCEMENT_classification.md
```

**All three match A3. No STOP.**

## 4. The grammar as implemented

### 4a. `stated:` — what it accepts and what it rejects

**MEASURED from the code at commit 3.**

**Where it lives.** The scope block is located exactly as before: the document's
single **bare** `add:` record (`^\s+add:\s*$` or `^\s+add:\s*\[\]\s*$`) is the
anchor. **The block's extent now also runs upward** — from the anchor, up while
each line is non-empty and no less indented than the anchor, stopping at the
first blank line or dedent. **`stated:` is read from anywhere inside that
block**, above or below the manifest. It is not required to sit on a fixed line.

**The value.** A comma-separated list of `<decimal integer> <noun>` items,
`noun` one of `addition`, `additions`, `modification`, `modifications`. Each
noun may appear at most once. **A category not named is taken as zero**, so
`stated: 3 additions` against a `modify:` list of two paths is a `FAIL`, not a
silent pass.

**Rejected, each as `NOT_PARSEABLE` with a distinct reason:**

    stated: three additions        malformed 'stated:' item: 'three additions'
    stated: 1 additions, 2 additions   'stated:' names additions twice
    stated:                        malformed 'stated:' record: ''
    stated: 3 files                malformed 'stated:' item: '3 files'
    (two stated: records)          two 'stated:' records in the scope block
    (no stated: record)            no 'stated:' record in the scope block

**Is a malformed declaration distinguishable from an absent one? YES**, and the
distinction is asserted by a fixture. The reason strings differ in kind:
*"malformed"* names the offending text, *"no `stated:` record"* names its
absence. A caller reading the JSON can tell an author who wrote the syntax
wrongly from one who did not write it at all.

**Number words are deliberately not accepted.** `stated:` is read by a machine;
number words are a prose affordance, and admitting them would have kept a
prose-shaped pattern in the module. **The consequence is that
`COUNT_WORDS` and the count regex are deleted outright**, so *"no sentence is
consulted"* is checkable by the absence of the machinery rather than by reading
the control flow.

### 4b. Path shape — the definition, and what it would reject

**MEASURED from the code:** `^[A-Za-z0-9._{}-]+(?:/[A-Za-z0-9._{}-]+)*$`.

One or more `/`-separated segments; each segment non-empty; each character an
ASCII letter, a digit, `.`, `_`, `-`, `{` or `}`. **Braces are admitted because
this repository's manifests carry `{HHMM}` placeholders.** **A single segment
with no slash is a path**, so `GATES.md` is accepted. A leading dot is
accepted, so `.github/workflows/ci.yml` is accepted. `[]` remains the empty-set
form and is not path-checked.

**A token under `add:` or `modify:` failing that shape makes the file
`NOT_PARSEABLE`**, with the reason naming the key and the token:
`not a path under 'modify:': '(none)'`. **It is never counted.** Under the old
parser `(none)` was appended to the counted set, which is how a live
integration was failed by a false count.

**What this would reject that a reasonable author might write** — stated
plainly, because the specification asks and because a rejection here costs the
author a `NOT_PARSEABLE`, not a wrong answer:

    a path containing a space                 my notes/summary.md
    a trailing comma from a list habit        specs/a.md,
    a path wrapped in backticks               `GATES.md`
    a trailing sentence period                docs/BRANCHING_POLICY.md.
    a parenthetical or annotation             GATES.md (unchanged)
    '+', '~', '@', '(', ')', ',', "'" anywhere
    a non-ASCII filename
    a glob or a directory wildcard            scripts/**
    an inline comment after the path          GATES.md  # unchanged

**The trailing comma and the backticks are the two I would expect to bite
first**, because both are natural in a document that is also prose. **The
failure is loud** — `NOT_PARSEABLE`, exit non-zero, the token quoted — which is
the trade the specification asks for over a silently wrong count.

### 4c. Comparison is per category

**MEASURED.** `stated_add` against the paths under `add:`, `stated_modify`
against the paths under `modify:`, separately. **A manifest whose totals agree
while its split does not now fails**; under the old total-only comparison it
passed. A fixture asserts exactly that.

## 5. A4 — Every fixture's old-parser result, and which fixture discharges each mode

**MEASURED.** Method: the P1 grammar was extracted **verbatim** from blob
`1922fe88f3a29909a006b2adf03cfb5229d20d84` (`git cat-file blob`, then the slice
from `COUNT_WORDS = {` to `def check_p1(`, unmodified) and each fixture's text
run through both parsers. **This is the actual landed code, not a
re-implementation of it.**

### A4(i) — per fixture, not in aggregate

Fourteen P1 fixtures exist at commit 3. **All fourteen were run against both
parsers.** `SAME` means the old parser reached the same verdict; it does not
mean the fixture is worthless — an agreeing manifest that passed before and
passes after establishes that the new syntax did not break the agreeing case.

    FIXTURE                                                    OLD          NEW            
    p1_passes_when_the_declared_total_matches_the_manifest      PASS         PASS           SAME
      old read 'stated: 2 additions, 0 modifications' as prose: 2 vs 2
    p1_fails_when_the_declared_total_disagrees                  FAIL         FAIL           SAME
      old: stated 5 counted 6, via the stated: line read as a sentence
    p1_fails_when_the_declared_categories_do_not_sum...         FAIL         FAIL           SAME
      old: stated 6 counted 4;  new: stated 3/3 counted 3/1
    p1_fails_when_only_one_category_disagrees                   PASS         FAIL           DIFFERS
      old: totals 4 == 4, passes;  new: add 2 vs 3, fails
    p1_consults_no_sentence_when_a_nearer_one_contradicts       FAIL         PASS           DIFFERS
      old selected '**A9 -- Scope**, seven additions:', stated 7 counted 3
    p1_reads_a_stated_record_placed_below_the_manifest          FAIL         PASS           DIFFERS
      same document; asserts stated: is read from below the manifest
    p1_passes_with_an_empty_modify_and_a_declared_zero          PASS         PASS           SAME
    p1_reports_not_parseable_and_that_is_not_a_pass             NOT_PARSEABLE NOT_PARSEABLE SAME
      both: "0 'add:' records"
    p1_reports_not_parseable_when_no_total_is_declared          PASS         NOT_PARSEABLE  DIFFERS
      old selected A9's prose, stated 2 counted 2, and passed a document
      that declares nothing
    p1_distinguishes_a_malformed_declaration_from_an_absent_one PASS         NOT_PARSEABLE  DIFFERS
      old read 'stated: three additions' as a sentence and passed
    p1_rejects_a_declaration_naming_a_category_twice            FAIL         NOT_PARSEABLE  DIFFERS
      old summed 1+2=3 against 1 path and called it a scope defect
    p1_reports_not_parseable_for_a_non_path_token_under_modify  FAIL         NOT_PARSEABLE  DIFFERS
      old counted '(none)' as a path: stated 1 counted 2
    p1_accepts_the_path_shapes_this_repository_writes           PASS         PASS           SAME
    p1_partial_carries_its_limitation_in_the_json               PASS         PASS           SAME

    SAME 7   DIFFERS 7

### A4(ii) — which fixture discharges each repaired failure mode

**Seven modes, seven discharging fixtures, each one the old parser cannot get
right.** Named individually, because this is the criterion most easily satisfied
in appearance:

    MODE                                   DISCHARGED BY                        OLD -> NEW
    a nearer contradicting prose count is  p1_consults_no_sentence_when_a_       FAIL -> PASS
    ignored  [THE BINDING CASE]            nearer_one_contradicts
    stated: is read anywhere in the block   p1_reads_a_stated_record_placed_     FAIL -> PASS
                                           below_the_manifest
    a document declaring no total is not    p1_reports_not_parseable_when_no_    PASS -> NOT_PARSEABLE
    guessed at                              total_is_declared
    a malformed declaration is refused and  p1_distinguishes_a_malformed_        PASS -> NOT_PARSEABLE
    named as malformed                      declaration_from_an_absent_one
    a declaration naming a category twice    p1_rejects_a_declaration_naming_a_  FAIL -> NOT_PARSEABLE
    is refused, not summed                  category_twice
    a non-path token is refused, not         p1_reports_not_parseable_for_a_     FAIL -> NOT_PARSEABLE
    counted                                 non_path_token_under_modify
    comparison is per category               p1_fails_when_only_one_category_    PASS -> FAIL
                                            disagrees

**The binding case behaves differently under the two parsers, as A4 requires.**
Getting it to do so took a deliberate fixture design, and the reason is worth
recording: **if `stated:` sits ABOVE the manifest, the old parser's backward
walk hits the `stated:` line itself, reads `3 additions` out of it as prose, and
accidentally agrees.** The binding fixture therefore places `stated:` **below**
the manifest, so the old walk reaches A9's contradicting dry-run sentence and
fails while the new grammar passes. **A fixture with `stated:` above the block
would have shown SAME and discharged nothing** — an appearance of regression
evidence with none in it.

## 6. A5 — the whole corpus re-measured, and A6

**MEASURED at commit 4**, P1's grammar run against **every `.md` file under
`specs/`**, 38 files, none omitted, none sampled.

**READ THIS BEFORE THE TABLE. `NOT_PARSEABLE` IS NOT A PASS AND IS NOT A
FAILURE. For all thirty-seven rows below carrying it, P1 HAS MADE NO
CORRECTNESS DETERMINATION AT ALL.** Those documents have not been checked and
found acceptable; they have not been checked. **One document in this repository
is judged by P1.**

     1  2026-08-06T0456Z_role-model-and-executors.md                     NOT_PARSEABLE   more than one scope block
     2  2026-08-06T1218Z_role-model-clean-rebuild.md                     NOT_PARSEABLE   one scope block, no declared total
     3  2026-08-06T2307Z_role-model-raw-evidence-and-integration.md      NOT_PARSEABLE   more than one scope block
     4  2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md          NOT_PARSEABLE   no scope block
     5  2026-08-07T1159Z_grassmann-crossing-sign.md                      NOT_PARSEABLE   no scope block
     6  2026-08-07T1320Z_integrate-fierz-and-sign-ruling.md              NOT_PARSEABLE   one scope block, no declared total
     7  2026-08-07T1424Z_freeze-checker-sign-repair.md                   NOT_PARSEABLE   one scope block, no declared total
     8  2026-08-07T1437Z_branch-deletion-policy.md                       NOT_PARSEABLE   one scope block, no declared total
     9  2026-08-07T1508Z_branch-deletion-policy-amendment.md             NOT_PARSEABLE   one scope block, no declared total
    10  2026-08-07T2158Z_integrate-freeze-repair-and-deletion-policy.md  NOT_PARSEABLE   one scope block, no declared total
    11  2026-08-08T1321Z_channel-character.md                            NOT_PARSEABLE   no scope block
    12  2026-08-08T1354Z_normalisation-audit.md                          NOT_PARSEABLE   no scope block
    13  2026-08-08T1427Z_integrate-channel-character-and-audit.md        NOT_PARSEABLE   one scope block, no declared total
    14  2026-08-08T1634Z_exponent-mapping-ruling.md                      NOT_PARSEABLE   one scope block, no declared total
    15  2026-08-08T1702Z_integrate-exponent-mapping-ruling.md            NOT_PARSEABLE   one scope block, no declared total
    16  2026-08-08T2350Z_generator-sum-criticality.md                    NOT_PARSEABLE   no scope block
    17  2026-08-09T0059Z_integrate-generator-sum-criticality.md          NOT_PARSEABLE   one scope block, no declared total
    18  2026-08-09T0300Z_attraction-ruling-and-layers.md                 NOT_PARSEABLE   one scope block, no declared total
    19  2026-08-09T0346Z_integrate-attraction-and-layers.md              NOT_PARSEABLE   one scope block, no declared total
    20  2026-08-09T1653Z_land-rules-14-15.md                             NOT_PARSEABLE   one scope block, no declared total
    21  2026-08-09T1711Z_integrate-rules-14-15.md                        NOT_PARSEABLE   one scope block, no declared total
    22  2026-08-09T1801Z_land-amendments-e-to-l.md                       NOT_PARSEABLE   one scope block, no declared total
    23  2026-08-09T1849Z_integrate-amendments-e-to-l.md                  NOT_PARSEABLE   one scope block, no declared total
    24  2026-08-09T1958Z_pi-decisions-v3.md                              NOT_PARSEABLE   one scope block, no declared total
    25  2026-08-09T2036Z_integrate-pi-decisions-v3.md                    NOT_PARSEABLE   one scope block, no declared total
    26  2026-08-09T2153Z_si1-deferred-02-crossref.md                     NOT_PARSEABLE   one scope block, no declared total
    27  2026-08-10T0113Z_integrate-si1-crossref.md                       NOT_PARSEABLE   one scope block, no declared total
    28  2026-08-10T0245Z_diquark-both-eta.md                             NOT_PARSEABLE   one scope block, no declared total
    29  2026-08-10T1112Z_diquark-adjudication.md                         NOT_PARSEABLE   one scope block, no declared total
    30  2026-08-11T1134Z_chirality-census.md                             NOT_PARSEABLE   one scope block, no declared total
    31  2026-08-11T1239Z_integrate-chirality-census.md                   NOT_PARSEABLE   one scope block, no declared total
    32  2026-08-11T2207Z_land-diquark-line.md                            NOT_PARSEABLE   one scope block, no declared total
    33  2026-08-12T0131Z_supply-protocol-v3.md                           NOT_PARSEABLE   one scope block, no declared total
    34  2026-08-12T0409Z_integrate-supply-protocol-v3.md                 NOT_PARSEABLE   one scope block, no declared total
    35  2026-08-12T1122Z_land-supply-protocol-v3.md                      NOT_PARSEABLE   no scope block
    36  2026-08-12T1256Z_governance-enforcement.md                       NOT_PARSEABLE   one scope block, no declared total
    37  2026-08-12T1919Z_integrate-enforcement-checks-v2.md              NOT_PARSEABLE   one scope block, no declared total
    38  2026-08-12T2015Z_p1-declared-total.md                            PASS            stated 3 add / 3 mod == counted 3 / 3

    SPLIT, measured:
      1  PASS
     29  NOT_PARSEABLE  one scope block, no declared total
      6  NOT_PARSEABLE  no scope block
      2  NOT_PARSEABLE  more than one scope block
     38  total

**This matches A5's prediction exactly** — one `PASS` and thirty-seven
`NOT_PARSEABLE` splitting 29 / 6 / 2 — and A5's evidence-base arithmetic is
independently confirmed: **37 files at `1cb5550f`, 29 with exactly one scope
block, 6 with none, 2 with more than one; 38 at the new head.**

**No `FAIL` anywhere in the table.** No document in this repository declares a
total that disagrees with its manifest, because only one declares a total.

**The two multiple-block files were already unjudgeable and remain so.** They
are `2026-08-06T0456Z_role-model-and-executors.md` and
`2026-08-06T2307Z_role-model-raw-evidence-and-integration.md`; the old parser
reported the same `2 'add:' records` for both. **This change neither helped nor
harmed them and it would be an overstatement to report them as newly
`NOT_PARSEABLE`.** The same is true of the six with no scope block.

**Also measured, and worth stating because the specification's §1(c) motivates
the path-shape rule from a live incident: no scope block in the corpus at the
new head contains a non-path token.** `(none)` appears in this corpus only
inside prose. The specification that carried it in a manifest is not on `main`.
**So the path-shape rule is prospective here; it is demonstrated by fixture, not
by a corpus row.**

### A6 — the three named specifications, before and after

**MEASURED, and this is FINDING 1.** A6 states *"Before: `FAIL`. After:
`NOT_PARSEABLE`"*:

    integrate-chirality-census      OLD  NOT_PARSEABLE  "no governing count sentence"
                                    NEW  NOT_PARSEABLE  "no 'stated:' record in the scope block"
    integrate-supply-protocol-v3    OLD  NOT_PARSEABLE  "no governing count sentence"
                                    NEW  NOT_PARSEABLE  "no 'stated:' record in the scope block"
    land-diquark-line               OLD  NOT_PARSEABLE  "no governing count sentence"
                                    NEW  NOT_PARSEABLE  "no 'stated:' record in the scope block"

**None of the three reported `FAIL` before.** **A6's own stop condition — "if
any still reports `FAIL`, prose is still being consulted somewhere" — is
satisfied**, and I have not treated the wrong "Before" as a stop, because A6
attaches no stop to it.

**Why the actual parser differs from §9's re-implementation.** The old backward
walk skipped blank lines but **broke on the first line starting with `#`**. In
all three files the scope block sits under an `## A4 — Scope` style heading with
no count sentence between, so the walk stopped at the heading and returned
`NOT_PARSEABLE`. **A re-implementation omitting that one break would walk past
the heading into an earlier section and find the dry-run sentence** — which is
exactly the behaviour §0 describes. **§0's mechanism is real; it is simply not
what the landed code does.**

**The full old-parser corpus distribution, MEASURED over the 29 scope-bearing
specifications at `1cb5550f`:**

    10  PASS
     3  FAIL                                      (integrate-fierz-and-sign-ruling,
                                                   land-amendments-e-to-l,
                                                   governance-enforcement)
    16  NOT_PARSEABLE  no governing count sentence
    29  total

**The pass rate of ten, which §1(e) requires me to record in the
classification, is confirmed.** The 17/2 split is not.

## 7. A7 — This specification parses and passes

**MEASURED at commit 4**, P1 run against
`specs/2026-08-12T2015Z_p1-declared-total.md`:

```json
{
  "parse": "OK",
  "counted_set": [
    "reports/2026-08-XXT{HHMM}Z_p1-declared-total.md",
    "reviews/chatgpt/2026-08-XXT{HHMM}Z_p1-declared-total.md",
    "specs/2026-08-XXT{HHMM}Z_p1-declared-total.md",
    "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
    "scripts/governance_tools/task_checker.py",
    "tests/test_task_checker.py"
  ],
  "counted": 6,
  "counted_add": 3,
  "counted_modify": 3,
  "stated_record": "stated: 3 additions, 3 modifications",
  "stated_add": 3,
  "stated_modify": 3,
  "stated": 6
}
```

**`PASS`.** Three declared additions against three listed, three declared
modifications against three listed. **The syntax parses the first document
written in it, including the `{HHMM}` placeholders in its own manifest** — which
is why braces are in the path-shape character class.

**One thing the specification warned about and which held.** §1(a) warns that a
specification's own text is parser input and that a second bare `add:` line
would make the file carry two scope blocks. **MEASURED: the file contains
exactly one bare `add:` record.** §1(a)'s illustration writes
`add:  (unchanged, one path per line)`, which the anchor pattern does not match,
and §1(d)'s fixture list carries no `add:` line at all. **The precaution was
necessary and it worked.**

## 8. A8 — Validators

**MEASURED**, run individually with `python -m pytest <path>`, pytest 9.1.1,
Python 3.11.15. **Before** = the evidence base in a detached worktree at
`1cb5550f`; **after** = commit 4.

    VALIDATOR                             BEFORE                      AFTER                       EXIT
    tests/test_repository_structure.py     4 passed                    4 passed                    0
    tests/test_si1_governance.py          14 passed                   14 passed                    0
    tests/test_gate_anchors.py            18 passed, 2 deselected     18 passed, 2 deselected      0
    tests/test_governance_tools.py         8 passed                    8 passed                    0
    tests/test_task_checker.py            42 passed                   51 passed                    0

**All five exit 0 before and after.** **No test was deleted and none was
adjusted to make the suite green.** The task-checker suite grows by nine.

**Pre-existing tests whose behaviour changed — named, with what each now
asserts.** Five P1 tests existed; two are unchanged, three changed:

    test_p1_passes_when_manifest_count_matches_governing_sentence
      -> RENAMED test_p1_passes_when_the_declared_total_matches_the_manifest.
         Same document, same PASS. The name asserted prose selection and no
         longer does; the assertion is unchanged.

    test_p1_fails_when_manifest_count_disagrees
      -> RENAMED test_p1_fails_when_the_declared_total_disagrees, and given a
         docstring recording that it now carries the planted five-versus-six
         property, which the historical document no longer demonstrates.
         Same FAIL, same overall FAIL.

    test_p1_selects_the_governing_sentence_not_another_count
      -> REPLACED by test_p1_consults_no_sentence_when_a_nearer_one_contradicts.
         It asserted that the grammar picks A9's sentence over A4's
         ('"A9" in governing_sentence', '"9 additions" not in ...'). Both
         assertions are about a field that no longer exists. It now asserts
         that a contradicting sentence immediately before the block is IGNORED
         and the document PASSES on its declared total. It keeps the NAMED CASE
         label the module docstring refers to — 'a specification with several
         count-bearing sentences' — with the opposite expected behaviour.

    test_p1_reports_not_parseable_and_that_is_not_a_pass       UNCHANGED
    test_p1_partial_carries_its_limitation_in_the_json         UNCHANGED
      (its subject string changed with P1's does_not_establish; the assertion
       is on 'does not establish' appearing in it, which still holds)

**The shared fixture helper changed and did not change any test's meaning.**
`SPEC_TEMPLATE` gained a `stated:` record and `base:`/`head:`/`mode:` records;
`spec_text(stated, paths)` now derives the `stated:` value from the same word it
puts in A9's prose, **so every call site outside P1 — twelve of them — is
unchanged in text and in meaning**: `spec_text("five", six_paths)` disagreed
before and disagrees now. **No non-P1 test was touched.**

**`ruff check .` — MEASURED, and it is not clean, at the evidence base or at
commit 4, identically.** 8 errors, all in `scripts/euclidean_reconstruction.py`
(E501 ×5, E702 ×2, I001 ×1). **That file is blob-identical between base and
commit 4** and is not in this task's writable set. `ruff check
scripts/governance_tools/ tests/` passes at both revisions. **This is
pre-existing repository state, reported and not fixed.**

## 9. A9 — The classification carries no verdict change

**MEASURED**, `git diff 1cb5550f..commit 4` on
`derivations/GOVERNANCE-ENFORCEMENT_classification.md`:

```diff
@@ -50,9 +50,10 @@ under each.
 **These sentences are the checker's `does_not_establish` field verbatim.**
 
 - **P1** — *Does not establish that the manifest is correct, only that
-  its path count matches the count in the sentence the grammar selects as
-  governing; a specification whose text does not admit the parse is
-  reported NOT_PARSEABLE, which is not a pass.*
+  the total the specification declares in its `stated:` record agrees,
+  per category, with the paths that record's block enumerates; a
+  specification declaring no total is reported NOT_PARSEABLE, which is
+  not a pass and is not a finding about that specification's scope.*
 - **P3** — *Does not establish which files are append-only; the declared
   set is a caller-supplied parameter and the check is silent about
   whether that set is the right one, or complete.*
@@ -140,11 +141,27 @@ is a `SHOULD` about how much work belongs in one task.
 
 **Rule 12 — Acceptance criteria must be mechanically checkable.**
 `PARTIAL` via **P1**. **One recurring instance is decidable** — a scope
-manifest's path count against the sentence that governs it — and that
-instance is the defect shape which recurred four times in this
-programme. **Whether every criterion in a specification has a
-machine-executable verification is not decidable**; P1 checks one
-criterion's internal arithmetic, not the rule.
+manifest's path count against the total the block itself declares in a
+`stated:` record — and that instance is the defect shape which recurred
+four times in this programme. **No sentence is consulted**; a document
+that declares no total is not judged. **Whether every criterion in a
+specification has a machine-executable verification is not decidable**;
+P1 checks one criterion's internal arithmetic, not the rule.
+
+**P1's decidability is narrow, and it was measured, not assumed.** P1 is
+decidable only over specifications written in the declared-total syntax.
+**Forty-two fixtures did not establish behaviour over real documents; one
+corpus run did.** Over the twenty-nine specifications carrying exactly
+one scope block at `1cb5550f`, **the pre-repair pass rate was ten**, and
+the nineteen non-passes were not defects in those documents: sixteen
+found no count sentence at all, because the backward walk stopped at the
+nearest markdown heading, and three took an intermediate dry-run count
+for the manifest's. **After the repair those twenty-nine are
+`NOT_PARSEABLE`.** **`NOT_PARSEABLE` is not a pass and is not a failure;
+P1 has made no determination about those documents at all**, and a corpus
+reading `NOT_PARSEABLE` throughout has not been checked. **Adoption of
+the syntax by convention is a separate matter this classification does
+not record as done.**
 
 **Rule 13 — Execution environment.** `JUDGEMENT`. It governs which
 diagnostic order an executor follows on failure, and **it carries two
```

**Verdict-label census, MEASURED as a whole-file token count on both sides:**

    MECHANICAL   base 13   head 13
    PARTIAL      base 17   head 17
    JUDGEMENT    base 26   head 26

**No label changed and no object was reclassified. P1 remains `PARTIAL`.** The
diff contains exactly two hunks: P1's `does_not_establish` sentence, restated for
the new grammar, and Rule 12's grammar description plus an added paragraph
recording the measured limitation. **No `does_not_establish` sentence is
weakened** — P1's gains a clause (*"and is not a finding about that
specification's scope"*) and loses none.

**The added paragraph records what §1(e) requires** — decidability only over
declaring specifications, that forty-two fixtures did not establish behaviour
over real documents, and the pre-repair pass rate of ten over the twenty-nine —
**and adds the corrected mechanism from FINDING 1**: sixteen found no count
sentence because the walk stopped at a heading; three took a dry-run count. **I
did not write §0's 17/2 split into the classification**, because I measured
otherwise.

## 10. A10 — The two checker runs, and the STOP

Base `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`, head **commit 4**
`f02a71163c46e205df4a29277c72d851a59777a8`. **Not commit 5**, which does not
exist yet and which carries this output.

### RUN 1 — default subject selection, observational, governs nothing

Config, verbatim:

```json
{
  "base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
  "head": "f02a71163c46e205df4a29277c72d851a59777a8"
}
```

**MEASURED: `overall` INCOMPLETE, exit 2.** P1 PASS, P2 PASS, P3 NOT_DECLARED,
P4 PASS, P5 NOT_APPLICABLE, P6 PASS, P7 NOT_DECLARED, P8 PASS, P9
NOT_APPLICABLE. **No property FAILED.**

### RUN 2 — `specification_paths` naming only this specification

Config, verbatim — **exactly what A10 words, and nothing else**:

```json
{
  "base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
  "head": "f02a71163c46e205df4a29277c72d851a59777a8",
  "specification_paths": [
    "specs/2026-08-12T2015Z_p1-declared-total.md"
  ]
}
```

**MEASURED: `overall` INCOMPLETE, exit 2. No property FAILED.** **P1 — the
property this task changes — PASSED.**

**What RUN 2 excluded, and why: NOTHING, and the narrowing had no effect.**
**MEASURED: RUN 1's and RUN 2's JSON outputs are BYTE-IDENTICAL** (`diff`
returns empty). The range adds exactly one specification, so the default
selection already selects precisely the file RUN 2 names. **I will not describe
this narrowing as having protected anything.** Unlike the previous integration
task, there is no second specification arriving by merge for RUN 2 to exclude —
this branch merges nothing.

### THE STOP: RUN 2 does not reach exit 0, and §7 forbids every route that would

**A10:** *"RUN 2 is stop-governing; any failure is a STOP, with no
pre-authorised exception."*

**§7:** *"Do not adjust the config to make RUN 2 pass. Narrowing a subject set,
supplying an empty declared set or dropping a property is a specification
stop."*

RUN 2 is INCOMPLETE for one reason: **P3 and P7 report `NOT_DECLARED`**, because
the config A10 specifies supplies neither `append_only_paths` nor
`authorised_modified_gates`. Those two properties have nothing to do with this
task, and neither reports a failure — the tool's own vocabulary reserves `FAIL`
for *"the property was evaluated and did not hold"*, while `NOT_DECLARED` means
*"the subject set was not supplied by the caller"*.

**To reach exit 0 I would have to supply those two sets. MEASURED: supplying
both as `[]` is sufficient and is the ONLY difference needed.** I ran that as a
labelled diagnostic, **RUN 2-D, which does NOT discharge A10**:

```json
{
  "base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
  "head": "f02a71163c46e205df4a29277c72d851a59777a8",
  "append_only_paths": [],
  "authorised_modified_gates": [],
  "specification_paths": ["specs/2026-08-12T2015Z_p1-declared-total.md"]
}
```

**RUN 2-D: `overall` PASS, exit 0.** The diff against RUN 2's output is confined
to P3 and P7.

**And `[]` is exactly the weakening §7 names.** MEASURED, RUN 2-D's own JSON:

```json
{
  "classification": "PARTIAL",
  "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
  "evidence": {
    "declared": []
  },
  "id": "P3",
  "reason": "caller declared an empty append-only set for this range",
  "status": "NOT_APPLICABLE",
  "title": "append-only on both measures"
}
{
  "classification": "PARTIAL",
  "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
  "evidence": {
    "added_sections": [],
    "authorised_modified": [],
    "gates_path": "GATES.md",
    "removed_sections": [],
    "section_count_base": 0,
    "section_count_head": 0,
    "unauthorised_changed": []
  },
  "id": "P7",
  "status": "PASS",
  "title": "gate integrity"
}
```

**`append_only_paths: []` does not check anything. It converts `NOT_DECLARED`
into `NOT_APPLICABLE`** — reason: *"caller declared an empty append-only set for
this range"* — **and `NOT_APPLICABLE` does not make a run INCOMPLETE.** That is
a subject set emptied to obtain a green, which is precisely the motion §7
prohibits. **The previous integration task's RUN 2 used `[]` for both keys.**

**Could I have declared a truthful non-empty append-only set instead? I looked
and could not.** No repository rule names the append-only path set; `CONVENTIONS.md`
speaks of *"an append-only log"* without enumerating one. **Any non-empty set I
supplied would be my invention, not a measurement**, and inventing a subject set
to obtain a green is the same defect wearing better clothes.

**So there is no configuration available to me that satisfies both A10 and §7.**
Per §7's final clause — *"If any instruction here is inconsistent with a
repository rule or with another instruction, stop and report; do not decide
which prevails"* — **I stop at A10 and do not decide.** The four alternatives I
can see, none of which I have taken:

1. **A10's stop rule means "any `FAIL`".** Then RUN 2 is satisfied as it
   stands: no property FAILED and P1 PASSED. This requires reading "failure" as
   the tool's `FAIL`, not as a non-zero exit.
2. **RUN 2's config should have included the declared sets**, as the previous
   task's did, and §7's clause bars only *reacting* to a failure by emptying
   them. Then RUN 2-D is RUN 2 and it passes.
3. **P3 and P7 should be excluded from RUN 2's scope**, which §7 calls
   "dropping a property" and prohibits.
4. **A10 is unsatisfiable as written for a branch that touches no append-only
   file and no gate**, and the criterion needs re-wording before any task can
   discharge it.

**My own reading, offered and not acted on, is (2)** — but the difference
between (1) and (2) changes what a future task may put in a config, which is a
governance question and not mine.

**What I did NOT do:** I did not designate RUN 2-D as RUN 2. I did not narrow
`specification_paths`. I did not drop a property. I did not edit the checker or
a fixture to change any of these results. **RUN 2 stands as A10 words it, with
its measured exit 2.**

### FINDING 3 — P7 is vacuous against the real `GATES.md`

**Visible in RUN 2-D's P7 record above: `section_count_base` 0,
`section_count_head` 0, verdict `PASS`.** `GATES.md` is 1390 lines and carries fourteen
gates.

**MEASURED:**

```
GATE_HEADING pattern                      ^## (P2-[A-Z0-9-]+)\s*$
'^## P2-' headings in GATES.md                                   14
headings matching GATE_HEADING                                    0
gate_sections(1cb5550f, 'GATES.md')                     0 sections
real heading form   '## P2-HK-01 — Heat-kernel species coefficients'
```

**The pattern requires the line to end after the gate ID; every real heading
continues with an em-dash and a title.** So whenever P7 is exercised against
this repository it compares two empty maps and returns `PASS`. **A gate section
could be rewritten, added or removed and P7 would still say `PASS`.** The
fixture gate file writes bare `## P2-ALPHA-01` headings, which is why fifty-one
fixtures do not catch it.

**This is the same defect class this task exists to repair — a check whose
fixtures pass and whose behaviour over real documents was never measured — on a
different property.** §2 forbids me to touch P2 through P9, and I have not.
**It needs its own task.** It also means the previous integration task's RUN 2
`PASS` included a vacuous P7.

## 11. A11 — Protected paths

**MEASURED at commit 4**, whole-tree `git ls-tree -r` blob comparison, path by
path, base against commit 4:

    paths at base                    343
    paths at commit 4                345
    removed                          none
    added                            2  (this specification, this review)
    changed                          3
    identical                      340
    changed set == §4's modify: set   TRUE
    unexpected changes               none
    specifications modified          none

    derivations/GOVERNANCE-ENFORCEMENT_classification.md  183df946 -> d966db0c
    scripts/governance_tools/task_checker.py              1922fe88 -> 1b17dfa1
    tests/test_task_checker.py                            a6856856 -> 8970bfeb

**Named individually, as A11 requires:**

    GATES.md                  849a4fbfe62d6478f092a84b0175357a74bbbb06  SAME   (as A11 states)
    CONVENTIONS.md            b3c96300a1f3eab967d3d141a1e81b278887342c  SAME
    DECISION_LOG.md           d9dd2bf3a8cca405f03b31c51b1f478c7db77ca2  SAME
    docs/BRANCHING_POLICY.md  3f0f35d4da448eb444d223fd003a5b0601792dc3  SAME
    .github/workflows/ci.yml  7e1add3371b1423da726421da2f9b428147b1a69  SAME

**Everything else under `scripts/`: 60 paths at base, 60 at commit 4, exactly
one differing** — `scripts/governance_tools/task_checker.py`. **No gate, gate
status, verdict or hash-pinned artifact was modified. No superseded-register
entry was written.** `review/role-model-and-executors` was not touched.

**INTENDED for commit 5:** commit 5 adds `reports/2026-08-12T2015Z_p1-declared-
total.md` and modifies nothing, so the comparison above holds unchanged at
commit 5 with `added` becoming 3. **Measured confirmation is post-report
evidence.**

## 12. A12 — Commit-message hygiene

**MEASURED. Proposed messages were inspected and scanned before each commit;
stored messages were read back after.** Commits 1–4:

    d9a8ba6b00987feafd5eb4b070a83c1f95b4c78c  spec: replace P1's prose inference with a declared total
    ec4de78e3849219086a91c699df14db94a3bc1ad  review: pre-execution review for the P1 declared-total repair
    bb59c4b14447f8d23cb1f5128cdc5e865bdf0d99  checker: read P1's declared total from the scope block, not from prose
    f02a71163c46e205df4a29277c72d851a59777a8  docs: describe P1's grammar as a declared total and record its narrow reach

    trailers on each of the four                              none
    'Co-Authored-By' in any stored message                    0
    session identifier or URL in any stored message           0
    tool or model attribution in any stored message            0

**Scanned case-insensitively over all four stored message bodies** for
`co-authored`, `http`, `session_`, `generated with`, and tool and model names:
**no match.** Author and committer identity fields are not message content and
are out of P6's scope, per the classification.

**Commit 5's INTENDED message** — first line, with the same hygiene applied
before committing:

    report: record the P1 declared-total repair and the RUN 2 stop

## 12a. Commit order and the final scope

**MEASURED — commits 1 to 4, in the order §4 specifies:**

    commit 1  d9a8ba6b  specs/2026-08-12T2015Z_p1-declared-total.md
    commit 2  ec4de78e  reviews/chatgpt/2026-08-12T2015Z_p1-declared-total.md
    commit 3  bb59c4b1  scripts/governance_tools/task_checker.py
                        tests/test_task_checker.py
    commit 4  f02a7116  derivations/GOVERNANCE-ENFORCEMENT_classification.md
    commit 5  INTENDED  reports/2026-08-12T2015Z_p1-declared-total.md

**Code and tests moved together in commit 3**, as §4 requires: the parser change
and its fourteen fixtures are one commit, so no commit exists at which the
grammar changed and its fixtures had not.

**The final scope, INTENDED — commit 5 does not exist while this is written:**

    stated: 3 additions, 3 modifications
    base: 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    head: <commit 5, INTENDED>
    mode: exact
    add:
      reports/2026-08-12T2015Z_p1-declared-total.md
      reviews/chatgpt/2026-08-12T2015Z_p1-declared-total.md
      specs/2026-08-12T2015Z_p1-declared-total.md
    modify:
      derivations/GOVERNANCE-ENFORCEMENT_classification.md
      scripts/governance_tools/task_checker.py
      tests/test_task_checker.py
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**MEASURED at commit 4, two of the three additions and all three modifications
are already in place** (§11); **the third addition is this file.** **The scope
measured base-to-commit-5 is post-report evidence and is not claimed here.**

**The UTC token `2015Z` and the day `12` were fixed by commit 1 and reused. Both
were MEASURED** — `date -u` at the time commit 1 was written — **and not chosen.**
`main` was not touched: no merge, no fast-forward, no push to `main`.

## 13. §6 — Rule 16 assessment

**Rule 16 is operative. The specification offered a candidate junction and asked
me to confirm or replace it. I confirm it, and add a second.**

### The junction the specification named, confirmed

**After this task P1 judges exactly ONE document in this repository.** Every
other specification — thirty-seven of thirty-eight — is `NOT_PARSEABLE`.

**A reader meeting a corpus run of thirty-seven `NOT_PARSEABLE` and no `FAIL`
may take it for a corpus that was checked and found acceptable. It was not
checked at all.** For each of those documents P1 made no correctness
determination: not a pass, not a failure, no statement about its scope manifest.
**This is stated in §6 above, immediately before the table a reader meets, and
not only here.** It is also now recorded in the classification itself.

**What would change it:** the declared-total syntax must be **adopted as
repository authoring convention**, and existing specifications must be written in
it, before P1 covers anything beyond a single document. **This task performs
neither.** It changes the consumer grammar only. **No rule requires `stated:`;
no convention mentions it; §2 forbade me to add it to any existing
specification, and I added it to none.** A future author writing a specification
without a `stated:` record will produce a document P1 cannot judge, and nothing
in this repository will tell them so.

### The narrower limit, stated as the specification requires

**Ten specifications passed P1 before this change. After it, one does.**
MEASURED, both figures. **That is a reduction in coverage.** A tool that judges
fewer documents more honestly is the intended outcome, and it must not be
reported as an improvement in coverage. It is not one.

### A second junction, added

**Nothing invokes this checker.** `.github/workflows/ci.yml` runs `ruff` and
`pytest` and does not mention `task_checker`. **MEASURED: the string
`task_checker` does not appear in the workflow.** So every result in this
report was produced by a human-initiated run, and **no rule is enforced by this
work — before or after it.** A reader who sees a checker in `scripts/` and a
green CI badge may connect them. They are not connected.

**And FINDING 3 is itself a Rule 16 junction:** a `PASS` from this tool is only
as good as the grammar behind it, and P7's grammar matches nothing in the file it
claims to check. **The set of properties whose behaviour over real documents has
now been measured is: P1, and P1 only.** P2 through P9 stand where P1 stood
before this task — fixtures green, corpus unmeasured. **P7 is now known to be
vacuous; the other seven are unmeasured, which is not the same as sound.**

## 14. Does the reduction from ten passing documents to one read as a regression?

**The specification asks which it reads as, and the honest answer is: it reads
as a regression, and it is not one.**

It reads as a regression because the visible numbers move the wrong way — ten
green rows become zero, and a planted defect that was being caught stops being
caught. **A reader scanning for improvement will not find it here.**

It is not one because the ten passes were not evidence. **MEASURED: of the
nineteen non-passes under the old grammar, sixteen arose because the backward
walk stopped at a markdown heading and three because it selected an
intermediate dry-run count — and in every one of those nineteen cases the
manifest itself was correct.** A grammar with that error rate produces its
passes by the same mechanism it produces its failures. **The ten were ten
coincidences of document layout, not ten verified manifests.**

**What actually improved is not measurable as a count**: a `PASS` from P1 now
means the author declared a total and the manifest matches it, per category, and
nothing else was consulted to reach that conclusion. **What got worse is real
and is a count**: the number of documents about which P1 will say anything at
all fell from twenty-nine to one.

**One concrete loss, named:** the planted five-versus-six mismatch in
`specs/2026-08-12T1256Z_governance-enforcement.md` was being detected and is not
any more. It is preserved as a fixture, which tests the checker and not that
document. **If that document's scope is ever wrong again, nothing in this
repository will notice.**

## 15. Stops and clarifications

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary stop

**A10's RUN 2 cannot reach exit 0 under any configuration §7 permits.** Full
statement, alternatives and what I declined to do: §10. **I did not decide which
instruction prevails.** RUN 2 stands as A10 words it, exit 2, with no property
FAILED and P1 PASSED.

### `SPECIFICATION_DEFECT` — one primary stop, reported without halting

**A6's stated "Before" is contradicted by measurement, and §0's account of the
dominant failure mode is not what the landed code does.** §0/§9 state 17 `FAIL`
+ 2 `NOT_PARSEABLE`; MEASURED 3 `FAIL` + 16 `NOT_PARSEABLE`. A6's three named
specifications report `NOT_PARSEABLE` before, not `FAIL`. **A6 attaches its stop
condition only to the "After" status, which is satisfied**, so I completed the
criterion and reported the discrepancy rather than halting on it. §6 gives the
mechanism. **§0's headline figures — 10 PASS, 19 non-PASS, and the corpus
arithmetic 37 / 29 / 6 / 2 — are all confirmed.** The re-implementation in §9
evidently omitted the old walk's break on `#`.

### `REPOSITORY_DEFECT` — one primary stop, out of scope and not fixed

**P7 is vacuous against the real `GATES.md`.** §10, FINDING 3. §2 forbids
touching P2 through P9 and I have not. **This is not a defect this task
introduced or was asked to repair.** It needs its own task.

### `ENVIRONMENT`

**None.** No environment failure occurred. **Rule 13 carries two conflicting
diagnostic orders, a known open item; neither was exercised**, and I am not
naming one as having applied.

### `OBSERVATION_METHOD_ERROR`

**None in this task's final measurements.** One is recorded because it happened
and was self-caught before any push: **I first typed the token `2019Z` into the
task-identity paths while the measured clock read `2014Z`** — a fabricated
literal of the class Amendment H exists to prevent. **Nothing had been pushed.**
I reset the unpushed branch to `1cb5550f`, obtained the token by running
`date -u +%H%M`, and redid commits 1 and 2 with the MEASURED token `2015Z`.
Amendment K permits local iteration before a push. **No history visible to
anyone else was rewritten.**

**A second, smaller one, recorded because it changed a fixture's value.** My
first version of the binding regression fixture placed `stated:` **above** the
manifest. Run against the old parser it read `SAME`, not `DIFFERS`, because the
old backward walk hit the `stated:` line and read `3 additions` out of it as
prose — the fixture would have appeared to discharge A4(ii) while discharging
nothing. **I found this by running A4(i) rather than by reasoning about it**,
and rewrote the fixture with `stated:` below the manifest. §5 records both the
correction and why it matters.

### Secondary findings, kept separate

- **`ruff check .` is not clean at the evidence base or at commit 4**, 8 errors,
  all pre-existing in `scripts/euclidean_reconstruction.py`, blob-identical
  across this task. §8.
- **RUN 2's narrowing had no effect**: its output is byte-identical to RUN 1's,
  because the range adds exactly one specification. §10. A10 asks what RUN 2
  excluded; the answer is nothing, and I have not dressed it up as a protection.
- **No corpus row exercises the path-shape rule.** No scope block at the new
  head contains a non-path token, so §1(c)'s repair is demonstrated by fixture
  only. §6.
- **`NOT_APPLICABLE` for P3 under an empty declared set is a weaker result than
  it looks.** It is not a check that passed; it is a check the caller switched
  off, and it does not make a run INCOMPLETE. §10.

### Anything ambiguous, unsatisfiable, or that I would have specified differently

- **A10 versus §7 is the unsatisfiable pair.** §10.
- **A6's "Before: `FAIL`" is unsatisfiable as stated.** I would have written A6
  as *"report the before and after status of each; the After must not be
  `FAIL`"*, with no predicted Before — which is how A5 is written, and A5 gave
  no trouble.
- **§9's method line should say whether a figure came from the blob or from a
  re-implementation of it, per figure.** It says so once, at the top of one
  entry; the entries that then disagree with the blob are the ones a reader most
  needs the distinction for. **Amendment H is satisfied by "I ran the stated
  method"; it does not require the stated method to be the code under test.**
  For a task whose subject IS a parser, running the parser is available and is
  strictly better.
- **`stated:` position within the block is unspecified.** I accept it anywhere
  in the block, which is what made the binding fixture possible. **If the PI
  intends a fixed position, that is a further constraint and not what I built.**
- **Nothing in this task makes `stated:` required.** A specification omitting it
  is `NOT_PARSEABLE` and no rule, convention or check tells its author. §13.

---

## 16. Appendix — A10's two JSON outputs, verbatim

### RUN 1, verbatim

```json
{
  "base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
  "commits_in_range": 4,
  "commits_on_first_parent_line": 4,
  "head": "f02a71163c46e205df4a29277c72d851a59777a8",
  "overall": "INCOMPLETE",
  "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
  "properties": [
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
      "evidence": [
        {
          "counted": 6,
          "counted_add": 3,
          "counted_modify": 3,
          "counted_set": [
            "reports/2026-08-XXT{HHMM}Z_p1-declared-total.md",
            "reviews/chatgpt/2026-08-XXT{HHMM}Z_p1-declared-total.md",
            "specs/2026-08-XXT{HHMM}Z_p1-declared-total.md",
            "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
            "scripts/governance_tools/task_checker.py",
            "tests/test_task_checker.py"
          ],
          "parse": "OK",
          "path": "specs/2026-08-12T2015Z_p1-declared-total.md",
          "stated": 6,
          "stated_add": 3,
          "stated_modify": 3,
          "stated_record": "stated: 3 additions, 3 modifications"
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
            "commit": "d9a8ba6b00987feafd5eb4b070a83c1f95b4c78c",
            "work_paths": []
          },
          {
            "adds_review": true,
            "commit": "ec4de78e3849219086a91c699df14db94a3bc1ad",
            "work_paths": []
          },
          {
            "adds_review": false,
            "commit": "bb59c4b14447f8d23cb1f5128cdc5e865bdf0d99",
            "work_paths": [
              "scripts/governance_tools/task_checker.py",
              "tests/test_task_checker.py"
            ]
          },
          {
            "adds_review": false,
            "commit": "f02a71163c46e205df4a29277c72d851a59777a8",
            "work_paths": [
              "derivations/GOVERNANCE-ENFORCEMENT_classification.md"
            ]
          }
        ],
        "first_review_commit": "ec4de78e3849219086a91c699df14db94a3bc1ad",
        "first_work_commit": "bb59c4b14447f8d23cb1f5128cdc5e865bdf0d99",
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
      "evidence": {},
      "id": "P3",
      "reason": "no append_only_paths supplied; the set is not inferred",
      "status": "NOT_DECLARED",
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
          "commit": "d9a8ba6b00987feafd5eb4b070a83c1f95b4c78c",
          "matches": [],
          "status": "PASS"
        },
        {
          "commit": "ec4de78e3849219086a91c699df14db94a3bc1ad",
          "matches": [],
          "status": "PASS"
        },
        {
          "commit": "bb59c4b14447f8d23cb1f5128cdc5e865bdf0d99",
          "matches": [],
          "status": "PASS"
        },
        {
          "commit": "f02a71163c46e205df4a29277c72d851a59777a8",
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
      "evidence": {},
      "id": "P7",
      "reason": "no authorised_modified_gates supplied; the set is not inferred",
      "status": "NOT_DECLARED",
      "title": "gate integrity"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {
        "first_commit": "d9a8ba6b00987feafd5eb4b070a83c1f95b4c78c",
        "first_commit_paths": [
          "specs/2026-08-12T2015Z_p1-declared-total.md"
        ],
        "reports_added": [],
        "reviews_added": [
          "reviews/chatgpt/2026-08-12T2015Z_p1-declared-total.md"
        ],
        "reviews_missing_function_directory": [],
        "specification_is_first_commit": true,
        "specs_added": [
          "specs/2026-08-12T2015Z_p1-declared-total.md"
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
    "boundary": null,
    "commits_in_scope": 4,
    "commits_out_of_scope": [],
    "inclusivity": "INCLUSIVE",
    "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
  },
  "tool": "task_checker"
}
```

### RUN 2, verbatim

**MEASURED: byte-identical to RUN 1 above** (`diff` returns empty), for the
reason given in §10.

```json
{
  "base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
  "commits_in_range": 4,
  "commits_on_first_parent_line": 4,
  "head": "f02a71163c46e205df4a29277c72d851a59777a8",
  "overall": "INCOMPLETE",
  "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
  "properties": [
    {
      "classification": "PARTIAL",
      "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
      "evidence": [
        {
          "counted": 6,
          "counted_add": 3,
          "counted_modify": 3,
          "counted_set": [
            "reports/2026-08-XXT{HHMM}Z_p1-declared-total.md",
            "reviews/chatgpt/2026-08-XXT{HHMM}Z_p1-declared-total.md",
            "specs/2026-08-XXT{HHMM}Z_p1-declared-total.md",
            "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
            "scripts/governance_tools/task_checker.py",
            "tests/test_task_checker.py"
          ],
          "parse": "OK",
          "path": "specs/2026-08-12T2015Z_p1-declared-total.md",
          "stated": 6,
          "stated_add": 3,
          "stated_modify": 3,
          "stated_record": "stated: 3 additions, 3 modifications"
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
            "commit": "d9a8ba6b00987feafd5eb4b070a83c1f95b4c78c",
            "work_paths": []
          },
          {
            "adds_review": true,
            "commit": "ec4de78e3849219086a91c699df14db94a3bc1ad",
            "work_paths": []
          },
          {
            "adds_review": false,
            "commit": "bb59c4b14447f8d23cb1f5128cdc5e865bdf0d99",
            "work_paths": [
              "scripts/governance_tools/task_checker.py",
              "tests/test_task_checker.py"
            ]
          },
          {
            "adds_review": false,
            "commit": "f02a71163c46e205df4a29277c72d851a59777a8",
            "work_paths": [
              "derivations/GOVERNANCE-ENFORCEMENT_classification.md"
            ]
          }
        ],
        "first_review_commit": "ec4de78e3849219086a91c699df14db94a3bc1ad",
        "first_work_commit": "bb59c4b14447f8d23cb1f5128cdc5e865bdf0d99",
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
      "evidence": {},
      "id": "P3",
      "reason": "no append_only_paths supplied; the set is not inferred",
      "status": "NOT_DECLARED",
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
          "commit": "d9a8ba6b00987feafd5eb4b070a83c1f95b4c78c",
          "matches": [],
          "status": "PASS"
        },
        {
          "commit": "ec4de78e3849219086a91c699df14db94a3bc1ad",
          "matches": [],
          "status": "PASS"
        },
        {
          "commit": "bb59c4b14447f8d23cb1f5128cdc5e865bdf0d99",
          "matches": [],
          "status": "PASS"
        },
        {
          "commit": "f02a71163c46e205df4a29277c72d851a59777a8",
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
      "evidence": {},
      "id": "P7",
      "reason": "no authorised_modified_gates supplied; the set is not inferred",
      "status": "NOT_DECLARED",
      "title": "gate integrity"
    },
    {
      "classification": "MECHANICAL",
      "evidence": {
        "first_commit": "d9a8ba6b00987feafd5eb4b070a83c1f95b4c78c",
        "first_commit_paths": [
          "specs/2026-08-12T2015Z_p1-declared-total.md"
        ],
        "reports_added": [],
        "reviews_added": [
          "reviews/chatgpt/2026-08-12T2015Z_p1-declared-total.md"
        ],
        "reviews_missing_function_directory": [],
        "specification_is_first_commit": true,
        "specs_added": [
          "specs/2026-08-12T2015Z_p1-declared-total.md"
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
    "boundary": null,
    "commits_in_scope": 4,
    "commits_out_of_scope": [],
    "inclusivity": "INCLUSIVE",
    "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
  },
  "tool": "task_checker"
}
```
