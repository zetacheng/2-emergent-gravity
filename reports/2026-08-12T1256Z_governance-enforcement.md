# Task report — mechanical enforcement for the governance rules that admit it

Specification:        `specs/2026-08-12T1256Z_governance-enforcement.md`
Pre-execution review: `reviews/chatgpt/2026-08-12T1256Z_governance-enforcement.md`
Classification:       `derivations/GOVERNANCE-ENFORCEMENT_classification.md`
Evidence base:        `8939ff4a46445d88c6470fb4f27eec71f2f39172`
Branch:               `governance/enforcement-checks`
Pre-report head:      `49ef50d03e2e57a2e1f4ce514f618ac19dd39bb1`
UTC token `{HHMM}Z`:  `1256`, fixed by commit 1; `XX` = `12`

**Headline.** **Two of twenty-nine objects are mechanical, one of those
only in part; five more have a necessary condition behind them; twenty-two
have no machine behind them at all.** Nine properties are implemented —
four MECHANICAL, five PARTIAL — with 42 tests giving every property a
passing and a failing case. **The planted A9 defect was caught by the
checker, on this specification, for the right reason.**

**Nothing here is enforced in the sense a reader will assume.** The
checker exists; **no workflow runs it.** §12 states that where a reader
will meet it.

---

## 1. A1 — Pinned inputs and the two gating counts

```
CONVENTIONS.md                   928dea15d7a2699384510240381f6bc9f86fd9bb3a7cbfaff5370839b430ce2d
docs/BRANCHING_POLICY.md         9d99f8365f798cfc27b5a2612f21130b4534cd32ea4778be4be97f15b7daa3f0
scripts/governance_tools/core.py c927be3eee4c773d6b9ef5944ecf992d434e8d466518285f38e96734f220b73f
```

**All three match. No STOP.**

```
numbered rules   : 18
amendment letters: A B C D E F G H I K L
amendment count  : 11
```

**Eighteen rules and eleven amendments, confirmed before classifying.
There is no Amendment J.** 29 objects.

## 2. A2 — How both artifacts arrived

**For the first time in this line, BOTH the specification and the review
arrived as files.**

```
spec   supplied : 42a4071812a2d1221cf996dd190a99c5c32adb2de42c06b0abefc8403a9403a1
spec   committed: 42a4071812a2d1221cf996dd190a99c5c32adb2de42c06b0abefc8403a9403a1
review supplied : beace6efab0eed9d522ee6dc8bed3c8a58ff6c3f581b66cdf571c2e124535961
review committed: beace6efab0eed9d522ee6dc8bed3c8a58ff6c3f581b66cdf571c2e124535961
```

**Both byte-identical.** Review: 175 lines, 8456 bytes; zero occurrences of
`REVIEW ARTIFACT`, zero attachment-marker lines. **No extraction of any
kind, and no boundary to locate.**

**Correspondence: by task name**, at the review's lines 1, 3 and 165 —
`mechanical enforcement for the governance rules that admit it`. **Not a
different specification. No STOP.**

**Rule 18's SHOULD is satisfied for the first time.** Commit 1's bytes are
the sender's file, verifiable against a digest, rather than my
transcription — which is what the three preceding tasks could not say.
**The asymmetry those reports flagged is closed for this task.**

## 3. A3 — The classification

Committed in full at
`derivations/GOVERNANCE-ENFORCEMENT_classification.md`. Summary:

```
MECHANICAL   Rule 15                                          1 rule
             Amendment B (heading presence only)              1 amendment
PARTIAL      Rules 3, 4, 5, 12                                4 rules
             Amendment K                                      1 amendment
JUDGEMENT    Rules 1, 2, 6, 7, 8, 9, 10, 11, 13, 14, 16,
             17, 18                                          13 rules
             Amendments A, C, D, E, F, G, H, I, L             9 amendments
-----------------------------------------------------------------------
             18 rules + 11 amendments                        29 objects
```

**Rule 15 is the only rule mechanical without qualification**, and it is so
because its text is entirely about paths and order. **Rule 18 is
JUDGEMENT with no check behind it**, as §3 requires: how a review file
reached the executor is not recoverable from repository objects, and a
byte-identical blob is consistent with a file supply, a paste and a
reconstruction. **No check was invented for it.**

Each `JUDGEMENT` entry carries its one-sentence reason and proposes no
mechanism; each `PARTIAL` states its necessary condition and what it
misses. Both worked examples from §0 — **Amendment G** and **Amendment
I** — are classified `JUDGEMENT`, which is why the amendments had to be
in scope.

## 4. A4, A5 — The checker and its fixtures

`scripts/governance_tools/task_checker.py`, JSON in the existing tools'
style, `--repo` and `--config`.

**Nine properties. §2 commissioned seven; P8 and P9 are added**, with
reasons in the classification: P8 covers Rule 15's *Placement* and
*Timing* paragraphs, which are the most mechanical text in the document
and had no property; P9 covers Amendment B's heading, which is decidable
from the blob. **Nothing was subtracted.**

| id | property | class |
|---|---|---|
| P1 | scope manifest arithmetic | PARTIAL |
| P2 | Rule 15 commit order | MECHANICAL |
| P3 | append-only on both measures | PARTIAL |
| P4 | superseded branches are not merged | MECHANICAL |
| P5 | merge parentage against recomputed facts | PARTIAL |
| P6 | commit-message hygiene | PARTIAL |
| P7 | gate integrity | PARTIAL |
| P8 | Rule 15 placement and specification-first | MECHANICAL |
| P9 | reports carry "Stops and clarifications" | MECHANICAL |

### The result vocabulary, and why a missing subject is never green

```
PASS            the property held over the range
FAIL            the property was evaluated and did not hold
NOT_APPLICABLE  the subject genuinely does not occur in the range
NOT_DECLARED    the subject set was not supplied by the caller
NOT_PARSEABLE   the input did not admit the property's grammar
OUT_OF_SCOPE    excluded by the prospectivity boundary
```

**`NOT_DECLARED` and `NOT_PARSEABLE` make the run `INCOMPLETE` and exit
non-zero.** **`NOT_APPLICABLE` does not**, because a range with no merge
genuinely has no P5 subject and penalising it would be noise. **This is
the distinction the review's §8.1 required**, and the line is drawn where
the subject is missing *because the caller did not supply it* — the
dangerous case — rather than because the range does not contain one.

**Exit contract, per A4 and Rule 14:** `0` only when `overall` is `PASS`;
`2` for `FAIL` and for `INCOMPLETE`; `3` for tool error. **Governance
failure and tool error are distinguishable**, and `INCOMPLETE` is
deliberately non-zero.

**Caller-supplied sets are explicit config inputs** — `append_only_paths`,
`authorised_modified_gates`, `recorded_merge_facts`,
`specification_paths` — **never inferred inside the checker from prose**,
which is the review's §8.2 constraint.

### A5 — fixture counts per property

```
  P1: 5 tests — passing-direction 2, failing/non-green 3
  P2: 5 tests — passing-direction 4, failing/non-green 1
  P3: 4 tests — passing-direction 1, failing/non-green 3
  P4: 2 tests — passing-direction 1, failing/non-green 1
  P5: 6 tests — passing-direction 4, failing/non-green 2
  P6: 4 tests — passing-direction 1, failing/non-green 3
  P7: 6 tests — passing-direction 4, failing/non-green 2
  P8: 3 tests — passing-direction 1, failing/non-green 2
  P9: 2 tests — passing-direction 1, failing/non-green 1
  total tests: 42
```

**Every property has at least one fixture in each direction.**

**The five shapes A5 names by hand each have their own fixture**, named
for it:

- **two merges, the second's parent 1 being the first** —
  `test_p5_two_merges_where_parent_1_is_the_first_merge`, which also
  asserts P2 passes on that range;
- **a stopped task holding only a specification, a review and a report** —
  `test_p2_stopped_task_has_no_work_commit_to_order`, asserting
  `first_work_commit is None`; the result follows from the task-record
  set including `reports/`, not from an exception;
- **a merge-base legitimately equal to parent 1** —
  `test_p5_accepts_a_merge_base_equal_to_parent_1`, asserting
  `merge_base_equals_parent_1 is True` and status `PASS`;
- **a specification with several count-bearing sentences** —
  `test_p1_selects_the_governing_sentence_not_another_count`, where an
  A4-style "9 additions and 3 modifications" precedes the A9-style
  governing sentence and must not be selected;
- **a file the checker was not told is append-only** —
  `test_p3_not_told_a_file_is_append_only_must_not_silently_pass`, which
  truncates `DECISION_LOG.md` and asserts `NOT_DECLARED`, `!= "PASS"`,
  and `overall == "INCOMPLETE"`.

Two tests run against **this repository's own history** rather than a
fixture: the landing task's range satisfies P2, P8, P9, P4 and P6, and
the register read from the shipped `docs/BRANCHING_POLICY.md` yields
exactly the six expected branch names.

## 5. A6 — Prospectivity

**The boundary, determined from the repository rather than assumed.**

Two candidates, and they are the two readings §3 names:

```
2e878f61319d98d83314865028ceb66ed7ccf3a9  2026-08-09 16:56:52
  docs: adopt amendments A-D and add CONVENTIONS.md Rules 14 and 15
  — the first commit in main's history whose CONVENTIONS.md carries '### 15.'
  — a single-parent commit on the landing branch

ce86b534fff6febb5291842e4eb60769affd12db  2026-08-09 17:12:21
  merge: integrate Rules 14 and 15 and amendments A-D (reviewed; pinned e045ee0)
  — the merge at which Rule 15 became authoritative on main
```

Method: walk `git rev-list --reverse <base> -- CONVENTIONS.md` and take
the first revision whose blob matches `^### 15\.`; then locate the merge
that carried it onto `main`. Confirmed either side:

```
  2e878f61^      rule15=0        ce86b534^1     rule15=0
  2e878f61       rule15=1        ce86b534       rule15=1
```

**The boundary used is `ce86b534…`** — Rule 15 became operative on `main`
there — **and the inclusivity is an explicit parameter, run both ways.**

**Both readings run over the three post-boundary task ranges. No merge
classification differs.**

```
range        incl       overall     P1   P2   P3   P4   P5   P6   P7   P8   P9
v3 build     INCLUSIVE  PASS        PASS PASS n/a  PASS n/a  PASS PASS PASS PASS
v3 build     EXCLUSIVE  PASS        PASS PASS n/a  PASS n/a  PASS PASS PASS PASS
integration  INCLUSIVE  INCOMPLETE  n/p  PASS n/a  PASS PASS PASS PASS PASS PASS
integration  EXCLUSIVE  INCOMPLETE  n/p  PASS n/a  PASS PASS PASS PASS PASS PASS
landing      INCLUSIVE  INCOMPLETE  n/p  PASS n/a  PASS n/a  PASS PASS PASS PASS
landing      EXCLUSIVE  INCOMPLETE  n/p  PASS n/a  PASS n/a  PASS PASS PASS PASS
```

**No classification differs between the readings over this range.** **That
is a useful negative result and it retires the question for this range
only** — it is not a ruling that the readings are equivalent, and the
checker picks no winner.

**Pre-boundary commits are reported as out of scope, not as passing.**
`test_p2_reports_pre_boundary_commits_as_out_of_scope` asserts exactly
that, and `test_p2_inclusivity_changes_which_commits_are_in_scope`
demonstrates a fixture where the two readings *do* differ — 2 commits in
scope versus 1, and P2 `FAIL` versus `PASS`. **So the parameter is shown
to matter even though it does not matter here.**

**No history was backfilled, no commit modified, and no check weakened so
that history would pass.**

### The merge shapes actually in main's history

**§3 told me to determine the shapes by reading the history rather than
taking its sentence as the inventory. I did, and the sentence is wrong.**
Parent-1 subject prefixes across all 42 merges on `main`:

```
     14 merge        11 docs        7 review        6 spec
      1 specs         1 reports     1 conventions   1 ci
```

**Six merges have a `spec:` commit as parent 1**, which §11's `MEASURED`
line denies and §3's prose excludes:

```
  ce86b534  p1 545d1410  spec: integrate Rules 14 and 15 and amendments A-D
  10f14f01  p1 c881b3e5  spec: integrate the attraction/repulsion ruling and the recomputed layers
  d8afb74e  p1 d5b46fcf  spec: integrate the generator-sum criticality derivation with an addendum
  d56335b5  p1 471a7a7b  spec: integrate the exponent-mapping ruling
  46b2915d  p1 ead58b64  spec: integrate the channel-character derivation and the normalisation audit
  f62fc89a  p1 cf427532  spec: integrate the freeze-checker repair and the branch-deletion policy
```

**This changes no fixture and no result** — those parent-1 commits add
paths under `specs/`, which are in the task-record set, so they are not
work commits and P2 is unaffected. **It is reported because a `MEASURED`
line under Amendment H that is false is exactly the failure no machine
catches**, and §11's own `RETRACTED` note shows the author correcting a
different instance of the same thing. §13 records it.

**At least one merge has another merge as parent 1** — 14 of them do —
which is the legitimate two-merge shape §2 requires the checker to pass,
and `test_p5_two_merges_where_parent_1_is_the_first_merge` fixtures it.

## 6. A7 — The checker against this task's own range

**Run before this report, both readings, `exit 2` each:**

```
  INCLUSIVE  exit=2  overall FAIL | P1:FAIL P2:PASS P3:NOT_APPLICABLE P4:PASS
                                    P5:NOT_APPLICABLE P6:PASS P7:PASS P8:PASS
                                    P9:NOT_APPLICABLE
  EXCLUSIVE  exit=2  overall FAIL | (identical)
```

**The only failure is P1, and it is the planted A9 defect.** Every other
property passes or is legitimately not applicable — P3 because the caller
declared an empty append-only set for this range, P5 because the range
has no merge, P9 because the range adds no report at the time of the run.

**§5's stop is not triggered**, because A9's mismatch is its single
pre-authorised exception and no other check failed.

## 7. A9 — The planted P1 violation, caught

**Caught, on this specification, by the grammar rather than by a search
for a number.**

```
 path       : specs/2026-08-12T1256Z_governance-enforcement.md
 governing  : **A9 — Scope**, five additions:
 stated     : 5
 counted    : 6
 counted set:
     specs/2026-08-XXT{HHMM}Z_governance-enforcement.md
     reviews/chatgpt/2026-08-XXT{HHMM}Z_governance-enforcement.md
     derivations/GOVERNANCE-ENFORCEMENT_classification.md
     scripts/governance_tools/task_checker.py
     tests/test_task_checker.py
     reports/2026-08-XXT{HHMM}Z_governance-enforcement.md
```

**The correct count is SIX.** The manifest lists six paths and the
governing sentence says five.

**The grammar selected the right sentence.** The specification carries
many count-bearing lines — §1(a)'s "twenty-nine objects", §2's "Three of
the seven", §11's "18 rules, 11 amendments" — and the parser took the
nearest preceding count to the scope block, which is A9's own. **A search
for a number would have been right or wrong by accident; this was right
by construction**, and the fixture
`test_p1_selects_the_governing_sentence_not_another_count` pins that
behaviour.

**The task proceeded on the six-path manifest**, and A8/A9 below measure
six paths at the final head.

**P1's real coverage, stated because it is smaller than it looks.** Of the
four most recent specifications, **two admit the parse and two do not**:

```
  specs/2026-08-12T0131Z_supply-protocol-v3.md         OK
  specs/2026-08-12T1256Z_governance-enforcement.md     OK  (and FAILS, correctly)
  specs/2026-08-12T0409Z_integrate-supply-protocol-v3.md
                                                       NOT_PARSEABLE
                                                       — no governing count sentence
  specs/2026-08-12T1122Z_land-supply-protocol-v3.md    NOT_PARSEABLE
                                                       — 0 'add:' records
```

**Both refusals are correct.** The integration specification's manifest is
preceded by `base:`/`head:`/`mode:` lines and a criterion heading with no
count, its count appearing *after* the block; the landing specification
has no manifest at all, stating its counts in prose and listing paths as
`A  <path>`. **The checker does not guess, and NOT_PARSEABLE is not a
pass** — which is why both ranges report `INCOMPLETE` in §5's table.

## 8. A8, A9 — Scope and nothing else touched

```
ADDED:
   A derivations/GOVERNANCE-ENFORCEMENT_classification.md
   A reviews/chatgpt/2026-08-12T1256Z_governance-enforcement.md
   A scripts/governance_tools/task_checker.py
   A specs/2026-08-12T1256Z_governance-enforcement.md
   A tests/test_task_checker.py
MODIFIED: NONE
DELETED : NONE
unauthorised additions: NONE

  CONVENTIONS.md               identical=True
  AGENTS.md                    identical=True
  GATES.md                     identical=True
  DECISION_LOG.md              identical=True
  docs/BRANCHING_POLICY.md     identical=True
  pyproject.toml               identical=True

  tests/         pre-existing=19   identical=19   differing=0  gained=['tests/test_task_checker.py']
  results/       pre-existing=69   identical=69   differing=0  gained=[]
  derivations/   pre-existing=34   identical=34   differing=0  gained=['derivations/GOVERNANCE-ENFORCEMENT_classification.md']
  reviews/       pre-existing=23   identical=23   differing=0  gained=['reviews/chatgpt/2026-08-12T1256Z_governance-enforcement.md']
```

**No existing test was modified** — all 19 pre-existing `tests/` paths are
blob-identical and the directory gains exactly one file. **`CONVENTIONS.md`
is untouched**, including the rules §13 reports as unenforceable.

**No gate status changed:** `GATES.md` blob-identical at
`849a4fbfe62d6478f092a84b0175357a74bbbb06`, 15 `^Status:` lines either
side.

Scope checker at the pre-report head, verbatim:

```json
{
  "base": "8939ff4a46445d88c6470fb4f27eec71f2f39172",
  "failures": [],
  "head": "49ef50d03e2e57a2e1f4ce514f618ac19dd39bb1",
  "mode": "exact",
  "observed_operations": [
    {
      "operation": "add",
      "path": "derivations/GOVERNANCE-ENFORCEMENT_classification.md"
    },
    {
      "operation": "add",
      "path": "reviews/chatgpt/2026-08-12T1256Z_governance-enforcement.md"
    },
    {
      "operation": "add",
      "path": "scripts/governance_tools/task_checker.py"
    },
    {
      "operation": "add",
      "path": "specs/2026-08-12T1256Z_governance-enforcement.md"
    },
    {
      "operation": "add",
      "path": "tests/test_task_checker.py"
    }
  ],
  "overall": "PASS",
  "tool": "scope_checker"
}
EXIT: 0
```

**PASS, 5 additions at the pre-report head; 6 at the final head**, the
sixth being this report. **The corrected A9 count is six**, and the final
scope check is post-report evidence.

**Intended final manifest:** the five paths above plus
`reports/2026-08-12T1256Z_governance-enforcement.md`, `mode: exact`,
`modify: []`, same `forbidden_operations`.

## 9. A10-pre, A11, A12, A13

### A10-pre — five validators, at the pre-report head

```
  tests/test_repository_structure.py     exit=0   4 passed
  tests/test_si1_governance.py           exit=0  14 passed
  tests/test_gate_anchors.py             exit=0  18 passed, 2 deselected
  tests/test_governance_tools.py         exit=0   8 passed
  tests/test_task_checker.py             exit=0  42 passed
```

**All five exit 0.** The 2 deselected are `@pytest.mark.slow`, excluded by
`pyproject.toml`; pre-existing and unchanged. Python 3.11.15,
`python -m pytest` 9.1.1.

### A11 — lint

```
ruff check scripts/governance_tools/task_checker.py tests/test_task_checker.py
All checks passed!
ruff exit: 0
```

**No rule was disabled and no `noqa` added.** Four lint failures were
fixed during development by rewriting the code — an unused `end`
variable, an over-long line, and two import-ordering problems.

### A12 — branch only

```
  remote refs/heads/main    8939ff4a46445d88c6470fb4f27eec71f2f39172
  refs/remotes/origin/main  8939ff4a46445d88c6470fb4f27eec71f2f39172
  local  refs/heads/main    0f7961747abe2a18b436c0b1e5b928f425ea4d9a  (stale by design)
```

**Both authoritative refs resolve to the evidence base.** Branch created
from it; **no `main` ref moved; no branch deleted.**

### A13 — commit-message hygiene

Method: proposed message written to a file and scanned before committing;
stored message read back from the object and scanned again. Pattern,
case-insensitive:
`co-authored-by|claude-session|generated with|noreply@|https?://|opus|sonnet|anthropic`.

    commit 1 (0071ac4f)  proposed: none found   stored: none found   suppressed: NONE
    commit 2 (cbfce533)  proposed: none found   stored: none found   suppressed: NONE
    commit 3 (a32a898d)  proposed: none found   stored: none found   suppressed: NONE
    commit 4 (49ef50d0)  proposed: none found   stored: none found   suppressed: NONE
    commit 5             proposed: none found at authoring time      suppressed: NONE

**No trailer was suppressed on any commit, because none appeared.** The
author/committer identity field matches `noreply@` on the raw object; **it
is not message content** and is the repository's standing identity on 204
of `main`'s commits. **P6 excludes it explicitly**, and says so in its
`does_not_establish`.

Commit 1–4 SHAs and messages:

    0071ac4f  spec: mechanical enforcement for the governance rules that admit it
    cbfce533  review: pre-execution review for the governance enforcement checks
    a32a898d  derivations: classify all eighteen rules and eleven amendments for
              enforceability
    49ef50d0  tools: add the task checker and its passing and failing fixtures

**Intended report commit message**, scanned clean at authoring time:

```
docs: report the governance enforcement classification and checker

Records A1-A13, the classification of all twenty-nine objects, the nine
properties with 42 fixtures, the prospectivity boundary and both readings
compared, and the checker's output on this task's own range.

The planted A9 count mismatch was caught by P1 on this specification. Two
findings about the commissioning document are reported and neither is
repaired here: a false MEASURED line about parent-1 subjects, and
commit-message hygiene enforcing no standing rule.

The checker is available, not enforcing. No workflow runs it.
```

## 10. Every PARTIAL's limitation, and where it lives

**A5 of the report contract asks for confirmation that these sentences are
in the checker's JSON and not only in the classification.** They are: the
`DOES_NOT_ESTABLISH` table in `task_checker.py` is the single source, and
`_result()` attaches the sentence to every PARTIAL record it emits.
`test_every_partial_property_carries_its_limitation` asserts that each
PARTIAL record carries a non-empty `does_not_establish` **and that no
MECHANICAL record carries one**.

- **P1** — *Does not establish that the manifest is correct, only that its
  path count matches the count in the sentence the grammar selects as
  governing; a specification whose text does not admit the parse is
  reported NOT_PARSEABLE, which is not a pass.*
- **P3** — *Does not establish which files are append-only; the declared
  set is a caller-supplied parameter and the check is silent about whether
  that set is the right one, or complete.*
- **P5** — *Does not establish that the executor derived the parentage
  values independently; three correct values are equally consistent with
  fresh recomputation and with one field copied into another. The diquark
  task's shared-rationale defect would pass this check.*
- **P6** — *Does not establish absence of "session identifier" or "tool
  attribution", which no repository document defines; only Co-Authored-By
  trailers and URLs are matched, and the author and committer identity
  fields are not message content and are out of scope.*
- **P7** — *Does not establish which gate sections were authorised to
  change; the authorised set is a caller-supplied parameter, and an empty
  set means "nothing may change", never "nothing to check".*

### P5, explicitly, as the report contract requires

**The checker recomputes all three Git facts freshly.** Parent 1 and
parent 2 are read from the merge object's own parent list; **the
merge-base is computed by a fresh `git merge-base(parent 1, parent 2)`
and is never read from any recorded value.**

**It makes NO claim about whether the executor derived them
independently.** That is not a fact about any object in the repository.
`test_p5_makes_no_claim_about_independent_derivation` asserts the
classification is `PARTIAL` and that the limitation names it.

**It does not test pairwise distinctness**, and
`test_p5_accepts_a_merge_base_equal_to_parent_1` proves the correct
history that a distinctness test would have failed.

**Comparison to recorded values is optional and explicit.** When
`recorded_merge_facts` is supplied the checker compares and can `FAIL`;
when it is not, the record carries `"compared_to_recorded": "UNAVAILABLE"`
rather than a scraped value. **No prose parser was written for recorded
parentage**, which is the review's §8.3 constraint.

## 11. Is any check a proxy for the property it claims to test?

**The report contract asks directly, and the honest answer is that one is,
and it is labelled.**

**P9 is the clearest case.** Amendment B requires a report to record each
stop *with its output, whether it was correct, its category, and the
clarification that followed*. **P9 checks that a heading matching "Stops
and clarifications" exists.** A report with the heading and nothing under
it passes. **This is a proxy, it is named as one in the classification and
in P9's own title, and its classification is MECHANICAL only about the
heading** — the amendment itself is classified `JUDGEMENT` for everything
beyond it.

**Two more that are bounded rather than proxies, and the distinction
matters.** P6 does not attempt "session identifier" or "tool attribution"
— it matches two patterns and says what it does not match, rather than
approximating the other two. P7's count is explicitly *only* a guard
against addition and removal, with byte identity doing the real work;
**the 103-line gate deletion that once passed the validators is fixtured
in `test_p7_catches_a_deleted_section_that_keeps_the_body_of_another`.**

**The one design error I made and corrected was itself a proxy.** P2's
first implementation walked every commit in `base..head` in `rev-list`
order. **That is a proxy for commit order, and a bad one**: `rev-list`'s
default emission is not topological, and a failing fixture showed a
side-branch commit ordered before a review that had been committed
earlier in wall-clock time. **Worse, walking merged-in commits would have
failed every integration**, whose merged branch necessarily commits its
work before the integrating task's review exists. **P2, P5, P8 and P9 now
walk the task's own first-parent line**, which is the property Rule 15
actually states — a task's own commits — and the scope note says so in the
JSON. §13 records this under `OBSERVATION_METHOD_ERROR`.

## 12. Rule 16 assessment

**Rule 16 is operative.** **§7's candidate junction is confirmed and I
adopt it**, with additions. Named precisely:

    CONVENTIONS.md's eighteen rules on authoritative main
      + derivations/GOVERNANCE-ENFORCEMENT_classification.md
      + scripts/governance_tools/task_checker.py
      + tests/test_task_checker.py, 42 tests, all green
    ------------------------------------------------------------------
    available inference:  the eighteen rules are now enforced

**Only the mechanical subset is checkable at all, and nothing runs the
checker automatically.** **A checker that exists but is invoked by no
workflow is AVAILABLE, not ENFORCING**, and the difference is the whole
of this section.

**Four additions of my own.**

- **The 42 green tests are the most misleading artifact this task
  produces.** They test *the checker*, not the repository. **A reader
  seeing "42 passed" beside a document titled "governance enforcement"
  will read it as forty-two rules being enforced.** It is nine properties
  behind two-and-a-bit rules.
- **The classification's own numbers are the correction, and they should
  travel with the tool.** Twenty-two of twenty-nine objects have no
  machine behind them. **That ratio is the finding**, not the checker.
- **`.github/workflows/ci.yml` exists and does not invoke the checker.**
  This task was not authorised to change it, and did not. **Until
  something does, every result in this report is a thing someone chose to
  run by hand** — which is the same standing as the reports that preceded
  it.
- **P1's coverage is two specifications in four.** A property that
  refuses to parse half its intended subjects is honest, but **a reader
  told "P1 catches the recurring defect shape" would overestimate it.**
  The two refusals are in §7.

## 13. Stops and clarifications

**One primary category per stop; secondary findings separate.**

### `SPECIFICATION_DEFECT`

**None blocking, and no stop occurred beyond A9's pre-authorised one.**

**One planted and caught, exactly as designed.** A9 states "five
additions" over a six-path manifest. **P1 failed on this specification,
the correct count is six, and the task proceeded on the manifest** per
§5's single exception. §7 gives the evidence.

**One found and not planted, and it is the more interesting of the two.**
**§11's `MEASURED` line "NO merge on main has a commit whose subject
begins 'spec:' as parent 1" is false — six merges do**, and §3's prose
carries the same error. §5 names all six. **No fixture or result depends
on it**, because those parent-1 commits add `specs/` paths and are
therefore task-record commits, not work commits. **It is reported because
§11's stated purpose is to separate executed from asserted, and this line
was recorded under `MEASURED` while being wrong** — the same failure mode
that section's own `RETRACTED` note corrects elsewhere. **§3 anticipated
it** — "do not take this sentence as the inventory" — **so I measured, and
the measurement is in §5.**

**Secondary, non-blocking.** The review's §9 asked whether P6's forbidden
vocabulary is mechanically delimited. **It is not, anywhere:
`CONVENTIONS.md` contains zero occurrences of "Co-Authored-By", "session
identifier", "tool attribution" or "trailer".** P6 is `PARTIAL`
accordingly and the classification records that **it enforces no standing
rule at all** — commit-message hygiene has been an acceptance criterion in
every recent specification and has never been written into the
conventions.

### `ENVIRONMENT`

**None. Neither of Rule 13's two diagnostic orders was exercised**,
because no environment failure occurred. Nothing was installed. **Rule 13
is separately reported in §14 as unenforceable as written**, which is a
finding about the rule, not an environment event.

### `OBSERVATION_METHOD_ERROR`

**One, mine, caught by a failing fixture before any result rested on it.**
**P2's first implementation walked every commit in the range in
`rev-list`'s default order.** Two defects in one: the default order is not
topological, so a fixture showed a side-branch commit ordered before a
review committed earlier; and walking merged-in commits **would have
failed every integration task in this repository's history**, since a
merged branch commits its work before the integrating task's review
exists. **Corrected to the first-parent line**, which is what Rule 15
actually governs. **The failing test found it; I did not reason it out in
advance.**

**Two smaller ones, both fixture defects rather than checker defects.**
Five fixtures initially asserted `overall == "PASS"` on ranges whose only
commits were work commits with no preceding review — **P2 was right and
the fixtures were asking the wrong question**, corrected by giving them a
`reviewed_base`. And one P5 fixture asserted the merge-base equalled the
range base when the fixture's own structure made it the review commit.

### `REPOSITORY_DEFECT`

**None introduced.** No existing test modified, no existing file changed.

**One pre-existing and now measured rather than asserted: the gap this
task exists to narrow is narrowed, not closed.** §12 gives the size.
**`.github/workflows/ci.yml` does not invoke the new checker**, and this
task was not authorised to change it.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`

**One, and it is left open deliberately.** **Whether the INCLUSIVE or the
EXCLUSIVE reading of Rule 15's prospectivity boundary is authoritative.**
The checker takes it as a parameter, both readings were run, and **no
classification differs over the tested range** — so the question did not
need answering here, and **the checker picks no winner.** §5 states that
the negative result retires the question for this range only. **Which
reading is correct is a governance decision.**

## 14. Rules unenforceable as written

**Findings about `CONVENTIONS.md`. It was not modified.**

- **Rule 13 carries two conflicting diagnostic orders.** No conformance
  check is possible until one is chosen. Long-standing open item.
- **Commit-message hygiene is enforced by no rule.** Zero occurrences of
  its vocabulary in `CONVENTIONS.md`; two of its four forbidden categories
  have no delimited definition anywhere in the repository.
- **Rule 15's "Prospective only" names no boundary commit.** The rule says
  earlier records are not retrospectively non-conforming without saying
  which commit divides them, which is why §5's boundary had to be derived
  and parameterised rather than read.
- **Amendment B demands more than any heading check can see.** It requires
  the lines establishing a stop to be reproduced; P9 checks a heading and
  says so.

## 15. Ambiguous, unsatisfiable, or would have specified differently

- **§1(b)'s "checking every property your classification marked MECHANICAL
  or PARTIAL" is ambiguous between rules and properties**, since §1(a)
  classifies 29 rules and §2 lists 7 properties and the mapping is not
  1:1. **I resolved it by classifying a rule MECHANICAL or PARTIAL only
  where a property actually checks it**, and stating the mapping in a
  table — the alternative reading would require a check for every rule
  with any decidable aspect, which is how a suite ends up claiming
  eighteen and delivering five.
- **A5's fixture list and §2's exception list overlap without saying so.**
  §2 lists the two-merge and stopped-task cases as "a case to FIXTURE, not
  an exception to code around", and A5 lists them again among five. **They
  are the same cases**; I fixtured each once and named the tests for it.
- **A9's planted defect worked, and I would keep the device** — but the
  narrow pre-authorisation in §5 is what made it usable. **Without it, §5
  and A9 would have been two imperatives in conflict**, and the executor
  would have had to choose which governs, which is exactly the judgement
  these specifications exist to remove. **That construction is worth
  reusing.**
- **The report contract asks for "the count of each" fixture per property
  but not for the named-case mapping**; I gave both, since a count without
  the named cases would not show that the five required shapes exist.
- **Nothing was unsatisfiable.** No instruction conflicted with a
  repository rule or with another instruction.

## 16. What this task did not do

**It enforced nothing automatically.** No workflow invokes the checker.
**It changed no rule** — `CONVENTIONS.md` is blob-identical, including the
four items §14 reports as unenforceable. **It modified no existing test**;
all 19 pre-existing `tests/` paths are blob-identical. **It added no check
for anything classified `JUDGEMENT`**, and invented none for Rule 18.
**It claimed no coverage it did not demonstrate** — every property the
checker reports has a failing fixture. **It ran against no branch but this
repository's own history and modified no branch.** No gate, gate status,
verdict, digest or hash-pinned artifact was modified; `GATES.md` is
blob-identical. **No `main` ref was moved and no branch was deleted.** **No
history was backfilled and no check was weakened so that history would
pass it.**
