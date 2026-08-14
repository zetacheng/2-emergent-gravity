# Execution report — `C-b`: one gate-heading grammar, and declarations that a reviewer sees

**Specification:** `specs/2026-08-14T2212Z_mechanisms-cb.md`
**Specification evidence base:** `f179b45eee359ef007da5e30833e9aed92069039`
**Branch:** `governance/mechanisms-cb`, cut from authoritative `main` @ `f179b45e…`
**Classification:** MATERIAL. Governed by Rule 15 and Rule 18, **and by Amendments M–P and Rules 19–21, which landed at the evidence base and bind this task prospectively.**

**Every figure below is labelled MEASURED or INTENDED.** **This report is
written at commit 4 and measures nothing at commit 5.**

**This task does not touch `main`.** Integration is a separate task.

---

## 1. Outcome

**Both mechanisms are built. One criterion's factual premise about this
specification turned out to be false, and §14.1 reports it — the task
remained executable because the specification defines the path that actually
applied.**

    C1   one helper, both call sites; the conjunction reads 14 of 14, unchanged
    C3   append_only and authorised_gates in the scope block; three states, and
         precedence with conflict as a stop

**MEASURED at commit 4:** 2 additions, 4 modifications; 391 of 395 base paths
unchanged; `GATES.md` blob-identical; validators **310 → 324, delta +14**; all
four checker invocations `PASS` at exit 0 with `P7` at 14 sections over 14 raw
headings.

**A3, measured BEFORE anything changed, in one session:** the conjunction
accepts **14**, the checker's expression **14**, the structure test's **14**.
**The decision loses no heading**, so §1's STOP did not trigger.

**The premise that failed.** A13 asserts *"This specification's own scope
block also declares `append_only` and `authorised_gates`, per §3(a)"* and
tells me to make them agree with the config. **MEASURED: the scope block
declares neither.** The keys appear in the specification only in §3(a)'s
definition of them and in §4's fixture list — never inside the manifest.
**So §3(b)'s config-only path applies**, the checker reports
`declared_source: config`, and RUN 2 does not stop. §14.1 gives the full
reading and why it is not a task-level stop.

**A15, answered up front.** My harness's standing git guidance does instruct a
`Co-Authored-By` trailer and a session URL. **None was written on any of the
five commits.** **Rule 20 binds this task and was not needed**: no commit
carried a violation, none was amended, and no history was rewritten.

---

## 2. Refs and inputs — A1, MEASURED

    refs/heads/main    f179b45eee359ef007da5e30833e9aed92069039    as specified

    scripts/governance_tools/task_checker.py                3dfe6498e7c369c5ea1277204861fcd3436ac41a
    tests/test_task_checker.py                              9b7d43e43b3409f066dd56fe6b15702cd6c7d9de
    tests/test_repository_structure.py                      7d63880dd0b9c285bac6a42cee436566dd31959b
    derivations/GOVERNANCE-ENFORCEMENT_classification.md    99b1314ee3592ed64aaafa6a4530cb4afc2c7755
    GATES.md                                                2b3bd5069414f009e1a0466c4990db2949519bd8

**No ref mismatch. No stop.** **§12's governing-rule figures re-measured:** 21
numbered rules, 15 amendment letters `A–P`, no `J`.

---

## 3. The pre-execution review — A2, MEASURED

    supplied specification    fccb7886d075c551c559869fe99042c255535102ad0cb5806f72c4c97e166bab
    committed specification   fccb7886d075c551c559869fe99042c255535102ad0cb5806f72c4c97e166bab   equal
    supplied review           4c2ae5b03ab66cda1152059e1d793dd699c52d735675c2e70b6210555e9783fb
    committed review          4c2ae5b03ab66cda1152059e1d793dd699c52d735675c2e70b6210555e9783fb   equal

The review's `reviewed specification SHA-256:` is filled in and names the
digest of the specification actually committed and executed. Committed
unedited, per Rule 18, and before the work it authorises.

**Amendment `N` binds this task, and A2 requires me to say so.** It landed at
`f179b45e…` and binds prospectively from that landing; this task is on the
far side of it, unlike the task that wrote it. **N(a)** — the specification is
supplied as a file: **met, it arrived as a file.** **N(b)** — the review
records `reviewed specification SHA-256:`: **met, and this is compliance
rather than coincidence**, because the rule was in force when the review was
written.

---

## 4. The conjunction, measured before the change — A3

**One measurement session, three counts from the same file, `GATES.md` at the
evidence base, before any edit:**

    the checker's expression      ^## (P2-[A-Z0-9-]+)[ \t]+[—–-][ \t]+\S.*$     14
    the structure test's          ^##\s+(P2-[A-Z]+(?:-[A-Z]+)*-\d+)             14
    THE CONJUNCTION               ^## (P2-[A-Z]+(?:-[A-Z]+)*-\d+)[ \t]+[—–-][ \t]+\S.*$   14

**Fourteen, as §1 expects. Fewer would have been a STOP and it did not
arise.** The fourteen ids:

     1  P2-HK-01                       8  P2-BETAV-RECON-01
     2  P2-GAP-01                      9  P2-BETAV-ASSEMBLY-01
     3  P2-BETA-01                    10  P2-CHANNEL-FREEZE-01
     4  P2-BETAV-01                   11  P2-PHASE-01
     5  P2-NORM-01                    12  P2-MULTIPHASE-GRAV-01
     6  P2-BETAV-CIRC-01              13  P2-GRAV-ENGINE-RECOVERED-01
     7  P2-BETAV-NUMREPRO-01          14  P2-LATTICE-ONTOLOGY-01

    conjunction set == checker set      True
    conjunction set == structure set    True
    checker/structure symmetric difference   empty

### 4.1 §0's three separating shapes, re-measured

| heading | checker | structure | conjunction |
|---|---|---|---|
| `## P2-FOO2-01 — Title` | ACCEPTS | REJECTS | rejects |
| `## P2-BAR-01` | REJECTS | ACCEPTS | rejects |
| `## P2-BAZ-01 — ` | REJECTS | ACCEPTS | rejects |

**All three reproduce, in both directions.** **And the conjunction is
strictly tighter than both, measured rather than argued:** the set of
headings it accepts but the checker does not is **empty**, and the set it
accepts but the structure test does not is **empty**. **The consolidation
cannot admit anything neither side admitted.**

---

## 5. One helper, two call sites — A4

**Location:** `scripts/governance_tools/task_checker.py`.

    line 712   GATE_ID       = r"P2-[A-Z]+(?:-[A-Z]+)*-\d+"       the strict id shape
    line 714   GATE_HEADING  = re.compile(rf"^## ({GATE_ID})[ \t]+[—–-][ \t]+\S.*$")
    line 720   GATE_ID_TOKEN = re.compile(GATE_ID)                 ids in running text
    line 723   def gate_heading_id(line: str) -> str | None
    line 734   def gate_heading_ids(text: str) -> list[str]
    line 746   RAW_GATE_HEADING = re.compile(r"^## P2-")           NOT part of the helper

**`gate_heading_id`** answers "is this line a gate heading, and which gate".
**`gate_heading_ids`** applies it to a whole text, **preserving order and
keeping duplicates** — a registry declaring one id twice is a defect `P7`'s
completeness invariant reports, and de-duplicating in the helper would hide
it.

**Both call sites use it:**

- `task_checker.py`'s `gate_sections` matches through `GATE_HEADING`, which is
  now built from `GATE_ID`;
- `tests/test_repository_structure.py`'s `_gate_headings()` is now
  `set(gate_heading_ids(text))` and **carries no expression of its own**. Its
  `_cited_gate_ids()` also now uses `GATE_ID_TOKEN` instead of a second copy
  of the id shape, so the id convention lives in one place too.

### 5.1 The search for stray expressions, reported rather than concluded

**Two searches over `scripts/` and `tests/`, every `.py` file:**

    grep -rn "P2-\[A-Z" scripts/ tests/ --include=*.py
      scripts/governance_tools/task_checker.py:712   GATE_ID = r"P2-[A-Z]+(?:-[A-Z]+)*-\d+"
      tests/test_task_checker.py:674                 # a COMMENT quoting the old grammar historically

    grep -rn "\^##" scripts/ tests/ --include=*.py
      scripts/governance_tools/task_checker.py:710   a COMMENT
      scripts/governance_tools/task_checker.py:715   the helper's own expression
      scripts/governance_tools/task_checker.py:746   RAW_GATE_HEADING
      tests/test_task_checker.py:674                 the same COMMENT

**One gate-heading expression exists in the repository, at line 715, and one
gate-id shape, at line 712.** The two remaining hits are prose comments; the
`test_task_checker.py:674` line quotes the *pre-repair* grammar as history and
is not compiled.

**`RAW_GATE_HEADING` remains separate and is NOT routed through the helper**,
as §1 and §6 require. **It is the independent signal `P7`'s completeness
invariant is measured against**, and routing it through the helper would make
the guard depend on the thing it guards.

---

## 6. The agreement invariant — A5

**`tests/test_repository_structure.py::test_both_gate_heading_call_sites_agree`.**

It reads `GATES.md`, takes the id set through the helper directly and through
`_gate_headings()`, and asserts they are equal.

**What it does if the set is empty: it FAILS.**

    assert from_checker, (
        "no gate heading found in GATES.md: either the heading convention "
        "changed or the shared grammar stopped matching, and in both cases "
        "this invariant is comparing two empty sets and asserting nothing")

**An empty set must not pass**, because a test that agrees on nothing agrees.
**This is the third instance of that shape in this repository** — `P7` over
two empty maps, the pin validator's zero-pin assertion, and now this — **and
it gets the same guard rather than a weaker one.**

**A second test, `test_the_shared_grammar_is_the_conjunction_of_the_two_it_replaced`,**
pins the three separating shapes as rejected and a well-formed heading as
read, so the canonical language cannot drift back to either parent silently.

---

## 7. Per-fixture demonstration against the OLD code — A6

**Each fixture classified FIRST, then run against the code at the evidence
base. Per fixture, not in aggregate.**

### F1 — the real `GATES.md` through the helper → 14 ids — **REGRESSION**

    old checker    14        old structure test    14

**The old code gets it right, which is what a regression fixture is for.**
**Correctly labelled**, and §12 of the specification is right that an earlier
version of this criterion implying it should fail was wrong.

**A measurement error of my own, corrected before it reached this report.** My
first run of F1 applied the structure test's pattern with `re.findall` but
**without `re.MULTILINE`**, which the original passes, and reported `0`. The
original reads 14. **I re-measured with the flag the source actually uses.**

### F2 — a digit inside an id segment → rejected — **CHANGE-DISCRIMINATING**

    '## P2-FOO2-01 — Title'      old checker ACCEPTS      old structure rejects

**The old checker admits it, so the old code gets it wrong. Correctly
labelled.** The new fixture also asserts it surfaces through `P7`:
`raw_heading_count_base` 2, `section_count_base` 1, and the offending line
quoted in `unrecognised_headings_base`.

### F3 — no separator, or an empty title → rejected — **REGRESSION for the checker**

    '## P2-BAR-01'        old checker REJECTS     old structure ACCEPTS
    '## P2-BAZ-01 — '     old checker REJECTS     old structure ACCEPTS

**The old checker already rejected both**, so as a checker fixture this is a
regression and I have labelled it so. **The old STRUCTURE test accepted both**,
which is the side the shared grammar tightens. **I report both halves rather
than picking the one that flatters the change.**

### F4 — both call sites return the same id set — **CHANGE-DISCRIMINATING**

**No such test exists at the evidence base.** The agreement was unchecked,
which is `C1`'s whole subject. **A fixture cannot be run against absent code**,
so it is change-discriminating by construction rather than by measurement, and
I say which.

### F5–F8 — the `append_only` fixtures — **CHANGE-DISCRIMINATING**

**Run against the old `parse_scope_block`, a scope block carrying
`append_only: []` returns:**

    {'parse': 'NOT_PARSEABLE', "detail": "not a path under 'modify:': 'append_only: []'"}

**The old grammar has no such key and mis-attributes the line to `modify:`.**
**The old code gets it wrong.** Correctly labelled. The three-state and
precedence fixtures all depend on the key existing, so all are
change-discriminating on the same evidence.

### F9 — no declaration anywhere → `NOT_DECLARED` — **REGRESSION**

The old code returned `NOT_DECLARED` for an absent set and still does.
**Unchanged behaviour, deliberately: absence and emptiness must not share an
outcome, and only the emptiness half moved.**

---

## 8. Precedence, demonstrated — A7

**Three runs. Each fixture orders its range specification-then-review so `P2`
and `P8` are satisfied and `P3` is the only property at issue.**

### (i) Declaration in the SPECIFICATION only

    P3 status                    PASS
    declared_source              specification
    declared                     ['DECISION_LOG.md']
    declared_by_specification    ['DECISION_LOG.md']
    supplied_by_config           None
    overall                      PASS

**The JSON states where the value came from: `specification`.**

### (ii) CONFIG only

    P3 status                    PASS
    declared_source              config
    declared                     ['DECISION_LOG.md']
    declared_by_specification    None
    supplied_by_config           ['DECISION_LOG.md']
    overall                      PASS

**The check proceeds and the JSON names `config` as the source**, exactly as
§3(b) requires.

**One correction to my own working.** My first run of (ii) reported
`overall: INCOMPLETE`. That was **`P7` reporting `NOT_DECLARED`** because that
fixture supplied no authorised-gate set — nothing to do with `P3`. I re-ran
with `authorised_modified_gates: []` supplied so the run isolates `P3`, and
the figure above is the isolated one. **The first number was true and about
the wrong property.**

### (iii) BOTH, differing → **STOP**

    P3 status                    DECLARATION_CONFLICT
    declared_by_specification    ['DECISION_LOG.md']
    supplied_by_config           ['GATES.md']
    reason                       'append_only' is declared by the specification as
                                 ['DECISION_LOG.md'] and supplied by config as
                                 ['GATES.md']. A reviewed declaration and a run-time
                                 config disagree; this is a stop, not a merge, and
                                 not a silent override.
    overall                      INCOMPLETE

**It stops.** `DECLARATION_CONFLICT` is in `NON_GREEN`, so the run is
`INCOMPLETE` and the exit status is non-zero. **Not a merge of the two sets,
and not a silent override.**

**A new status word, and why rather than reusing one.** `NOT_PARSEABLE` means
the input did not admit the grammar; both inputs here parse fine and
contradict each other. **Overloading an existing state with a second meaning
is precisely the defect `C3` exists to remove** — `[]` meaning two opposite
things in `P3` and `P7` — so reusing one to save a word would have reproduced
it while fixing it.

---

## 9. The three states of `append_only` — A8

**One run each. All three distinguishable in the JSON by a reader who has only
the JSON.**

### (a) No declaration anywhere

    status     NOT_DECLARED
    source     none
    declared   None
    reason     no append-only set declared by the specification or supplied by
               config; the set is not inferred
    overall    INCOMPLETE

### (b) `append_only: []` in the scope block

    status     DECLARED_EMPTY
    source     specification
    declared   []
    reason     nothing was checked because nothing was declared applicable: the
               declared append-only set is empty, which is a declaration and not
               an exemption
    overall    PASS

**`DECLARED_EMPTY`, and neither `NOT_APPLICABLE` nor `PASS`**, as A8 requires.

### (c) A non-empty declared set

    status     PASS
    source     specification
    declared   ['DECISION_LOG.md']
    overall    PASS

### 9.1 Can a reader of the JSON alone tell `DECLARED_EMPTY` from `PASS`?

**Yes, on three independent fields.** The `status` differs — the literal
string `DECLARED_EMPTY` against `PASS`. The `reason` field is present on
`DECLARED_EMPTY` and absent on `PASS`, and says in words that nothing was
checked. And `evidence.declared` is `[]` against a populated list.
**No inference is required and no cross-referencing to this report.**

### 9.2 Does `DECLARED_EMPTY` affect the run's exit status, and is that right?

**It does not. The run continues and can still be `PASS` overall** — run (b)
above is `overall: PASS` with `P3` at `DECLARED_EMPTY`.

**That is the right answer, and the reason is the distinction the state
exists to draw.** `NOT_DECLARED` means the specification said *nothing*, so
the checker has no subject and the run must not read green — it is
`INCOMPLETE`. **`DECLARED_EMPTY` means the specification SAID the applicable
set is empty.** That is a valid, reviewed declaration; **there is nothing
missing, so there is nothing to be incomplete about.**

**The Reviewer's non-blocking observation asked exactly this to be stated, and
here is the aggregate effect in one sentence:** a run whose only non-`PASS`
property is `P3` at `DECLARED_EMPTY` reports `overall: PASS`, **and the
per-property JSON is what prevents that from reading as a successful
non-empty verification** — the status word and its reason are both there.

**What it does not do is make the declaration true.** `P3` does not verify
that an empty declaration is correct, and this task does not make it. §11
keeps `P3` `PARTIAL` for that reason.

---

## 10. The classification — A9

**Full diff below.** **Only `P3`'s and `P7`'s entries changed.**

    property rows            9 before, 9 after
    row diff                 exactly two lines, P3's and P7's, and only their
                             DESCRIPTION cell in each
    P3 class                 PARTIAL before, PARTIAL after
    P7 class                 PARTIAL before, PARTIAL after
    §5 "The count that matters"    byte-identical
    deleted lines            2, both the replaced table rows

**No verdict changed. No property was added or removed. The nine stay nine.**
**Neither `P3` nor `P7` is described as no longer `PARTIAL`** — the added
prose says explicitly that the discovery problem narrows rather than vanishes.

    diff --git a/derivations/GOVERNANCE-ENFORCEMENT_classification.md b/derivations/GOVERNANCE-ENFORCEMENT_classification.md
    index 99b1314..c09a052 100644
    --- a/derivations/GOVERNANCE-ENFORCEMENT_classification.md
    +++ b/derivations/GOVERNANCE-ENFORCEMENT_classification.md
    @@ -37,11 +37,11 @@ under each.
     |---|---|---|---|
     | P1 | scope manifest arithmetic | PARTIAL | Rule 12 (instance) |
     | P2 | Rule 15 commit order — review precedes first work commit | MECHANICAL | Rule 15 (timing) |
    -| P3 | append-only on both measures | PARTIAL | no rule; a recurring criterion |
    +| P3 | append-only on both measures, over a set the specification declares | PARTIAL | no rule; a recurring criterion |
     | P4 | superseded branches are not merged | MECHANICAL | Amendment K |
     | P5 | merge parentage against freshly recomputed facts | PARTIAL | Rule 5 (part) |
     | P6 | commit-message hygiene | PARTIAL | **no rule** — see §3 |
    -| P7 | gate integrity — every `## P2-` heading is parsed, and no unauthorised section changed | PARTIAL | Rule 3 (part) |
    +| P7 | gate integrity — every `## P2-` heading is parsed, and no unauthorised section changed, over a set the specification declares | PARTIAL | Rule 3 (part) |
     | P8 | Rule 15 placement and specification-first | MECHANICAL | Rule 15 (placement) |
     | P9 | every report carries "Stops and clarifications" | MECHANICAL | Amendment B |
     
    @@ -106,6 +106,45 @@ already carries. It still makes the run `INCOMPLETE` and exits non-zero.
     is still a caller-supplied parameter and the discovery problem behind it is
     untouched by this repair.
     
    +**`P3` and `P7`, extended again — where the declared set now comes from.**
    +The paragraphs below are **not** part of either `does_not_establish` field
    +quoted above; they record what changed and what did not.
    +
    +**Both properties now read their declared set from the SPECIFICATION'S SCOPE
    +BLOCK**, through the `append_only:` and `authorised_gates:` keys, and from the
    +run-time config only as a fallback. **The config was written after the review**,
    +so a reviewer approved a specification while something else decided what the
    +checks were pointed at. **When the specification declares, it wins. When only
    +config supplies, the check proceeds and the JSON names `config` as the
    +source. When both declare and they DIFFER, the property returns
    +`DECLARATION_CONFLICT` and the run is non-zero** — a config silently
    +overriding a reviewed declaration would reproduce, one layer along, the defect
    +this change removes.
    +
    +**`P3`'s reading of an empty set is corrected.** It formerly returned
    +`NOT_APPLICABLE` for `[]` — the check switched OFF, not passed — and one
    +landed integration supplied `append_only_paths: []` and went green on it.
    +**An empty declared set now returns `DECLARED_EMPTY`**: not `NOT_APPLICABLE`,
    +because the specification SAID the applicable set is empty and absence says
    +nothing; and **not `PASS`, because nothing was checked** and a pass over
    +nothing is the vacuous green this repository has met three times. **It does
    +not make the run `INCOMPLETE`**, because unlike `NOT_DECLARED` it is a valid
    +declaration.
    +
    +**Both remain `PARTIAL`, and the reason is narrowed rather than removed.**
    +**A specification still declares its own sets, and a specification can declare
    +wrongly.** Nothing verifies that a declared append-only set is complete, or
    +that an authorised-gate set names only gates the task was authorised to
    +change. **What changed is that the declaration is now inside the artifact a
    +reviewer reads**, so a wrong declaration is visible at review time instead of
    +being invented afterwards. **That is a narrower discovery problem, not an
    +absent one.**
    +
    +**And nothing requires a specification to carry the keys at all.** A
    +specification that declares neither still reaches `NOT_DECLARED`, exactly as
    +before. **Making the declarations mandatory is `C2`**, which is unbuilt;
    +**compliance therefore still rests on an authoring habit.**
    +
     ### P8 and P9, added, with reasons
     
     **P8 — Rule 15 placement and specification-first.** Rule 15's *Placement*

---

## 11. Scope, protected paths, gates — A10, A11, A12

### 11.1 A10 — scope, MEASURED at commit 4

    M  derivations/GOVERNANCE-ENFORCEMENT_classification.md
    A  reviews/chatgpt/2026-08-14T2212Z_mechanisms-cb.md
    M  scripts/governance_tools/task_checker.py
    A  specs/2026-08-14T2212Z_mechanisms-cb.md
    M  tests/test_repository_structure.py
    M  tests/test_task_checker.py

    additions 2   modifications 4   deleted/renamed/copied/type-changed/unmerged/unknown 0

**INTENDED at commit 5:** 3 additions and 4 modifications — the six above plus
`reports/2026-08-14T2212Z_mechanisms-cb.md`, giving the manifest's seven
paths. **`GATES.md` is not among them.**

### 11.2 A11 — protected paths, MEASURED

    paths existing at the evidence base                    395
    excluded (the four in A10's modify: list)                4
    compared                                               391
    differing                                                0

    GATES.md                    IDENTICAL      tests/test_gate_pins.py     IDENTICAL
    CONVENTIONS.md              IDENTICAL      results/                    0 differing
    DECISION_LOG.md             IDENTICAL
    docs/BRANCHING_POLICY.md    IDENTICAL

### 11.3 A12 — gate invariants and pins, MEASURED

    1.  ^## P2- section count       14
    2.  P2-PHASE-01                 Status: PROPOSED          (GATES.md line 973)
    3.  prerequisites               ### Satisfied prerequisite — MICROSCOPIC PARAMETER DOMAIN        (line 1010)
                                    ### Satisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT (line 1035)
                                    zero occurrences of "### Unsatisfied prerequisite"
    4.  pins                        2 found, both MATCH

**`GATES.md` is blob-identical to the evidence base**, as §6 requires — every
mechanism this task builds reads it.

---

## 12. The checker — A13, MEASURED at commit 4

    base   f179b45eee359ef007da5e30833e9aed92069039
    head   0d7799057d56c27e487a20cca0994c2647016265   (commit 4)

**Both prospectivity readings for each run, so four invocations. All four
exited 0 with `overall: PASS`.**

    run 1 INCLUSIVE   exit 0   PASS   sha256 69ddc725d937b84beb7fa5c2a97a1bc9d8606da169fad934028fce23ea4ebe06
    run 1 EXCLUSIVE   exit 0   PASS   sha256 4e01b5d397f4e9b50d4e9888d131336b37fd44e9548bce1be58eac2dc15dbdde
    run 2 INCLUSIVE   exit 0   PASS   sha256 69ddc725d937b84beb7fa5c2a97a1bc9d8606da169fad934028fce23ea4ebe06
    run 2 EXCLUSIVE   exit 0   PASS   sha256 4e01b5d397f4e9b50d4e9888d131336b37fd44e9548bce1be58eac2dc15dbdde

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 NOT_APPLICABLE
    P6 PASS   P7 PASS   P8 PASS   P9 NOT_APPLICABLE

### 12.1 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "f179b45eee359ef007da5e30833e9aed92069039",
      "head": "0d7799057d56c27e487a20cca0994c2647016265",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 12.2 RUN 2 config, verbatim — stop-governing

    {
      "base": "f179b45eee359ef007da5e30833e9aed92069039",
      "head": "0d7799057d56c27e487a20cca0994c2647016265",
      "specification_paths": ["specs/2026-08-14T2212Z_mechanisms-cb.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I supplied of my own choosing; all are
taken from A13.** **The config was never adjusted to make RUN 2 pass**, and
**this specification's own declarations were not adjusted either** — §10
forbids both, and neither was necessary.

### 12.3 The measured RUN 1 subject set

**RUN 1's default selection chose one specification:**

    specs/2026-08-14T2212Z_mechanisms-cb.md

**The same single path RUN 2 names explicitly**, so the two runs' outputs are
byte-identical at each prospectivity reading — the digests above are equal in
pairs. The readings differ in exactly one line and in no verdict:

    261c261
    <         "inclusivity": "INCLUSIVE",
    ---
    >         "inclusivity": "EXCLUSIVE",

### 12.4 `P7`, and the section count it saw through the new helper

    declared_source          config
    raw_heading_count_base   14        section_count_base   14
    raw_heading_count_head   14        section_count_head   14
    unauthorised_changed     []        added_sections  []   removed_sections  []

**`PASS` at fourteen sections, read through the shared helper. `PASS` at zero
would have been a STOP.**

### 12.5 Do this task's own declarations agree with its config? — the answer A13 asks for

**They cannot disagree, because this specification declares nothing.**

**MEASURED, both properties, in all four invocations:**

    P3   declared_source: config    declared_by_specification: None
    P7   declared_source: config    declared_by_specification: None

**A13 asserts that this specification's scope block declares `append_only`
and `authorised_gates` per §3(a), and instructs me to make them agree with
the config and report that I did. The scope block declares neither.** The
manifest at A10 runs `stated:`, `base:`, `head:`, `mode:`, `add:`, `modify:`,
`forbidden_operations:` and stops. The two key names appear in the
specification only at §3(a), which *defines* them, and in §4's fixture list.

**So §3(b)'s third case applies — "when only config is present, the check
proceeds and the JSON says the value came from config" — and it does.** The
precedence rule was exercised in the sense that it *resolved*; it was not
exercised in the sense of being tested against a competing declaration, and
A7(iii) is where that is demonstrated instead.

**I did not add the keys to the specification.** Rule 18 and A2 require the
committed specification to be the supplied bytes, and editing it would have
broken the digest equality A2 measures. **§10's "do not adjust this
specification's own declarations to make the precedence check pass" points
the same way.** §14.1 records this as a finding rather than a stop, with the
reasoning.

### 12.6 RUN 1 output, verbatim

    {
      "base": "f179b45eee359ef007da5e30833e9aed92069039",
      "commits_in_range": 4,
      "commits_on_first_parent_line": 4,
      "head": "0d7799057d56c27e487a20cca0994c2647016265",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "append_only": null,
              "authorised_gates": null,
              "counted": 7,
              "counted_add": 3,
              "counted_modify": 4,
              "counted_set": [
                "reports/2026-08-XXT{HHMM}Z_mechanisms-cb.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_mechanisms-cb.md",
                "specs/2026-08-XXT{HHMM}Z_mechanisms-cb.md",
                "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                "scripts/governance_tools/task_checker.py",
                "tests/test_repository_structure.py",
                "tests/test_task_checker.py"
              ],
              "parse": "OK",
              "path": "specs/2026-08-14T2212Z_mechanisms-cb.md",
              "stated": 7,
              "stated_add": 3,
              "stated_modify": 4,
              "stated_record": "stated: 3 additions, 4 modifications"
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
                "commit": "4f2c2d6f1937745f16e60426c879d1287bf721f3",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "cc7a766e085a068bdca60f2a0fcaf9adfb175449",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "bba84763cc55c4753d3b77b49dcb9b79034c6be0",
                "work_paths": [
                  "scripts/governance_tools/task_checker.py",
                  "tests/test_repository_structure.py",
                  "tests/test_task_checker.py"
                ]
              },
              {
                "adds_review": false,
                "commit": "0d7799057d56c27e487a20cca0994c2647016265",
                "work_paths": [
                  "derivations/GOVERNANCE-ENFORCEMENT_classification.md"
                ]
              }
            ],
            "first_review_commit": "cc7a766e085a068bdca60f2a0fcaf9adfb175449",
            "first_work_commit": "bba84763cc55c4753d3b77b49dcb9b79034c6be0",
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
          "evidence": {
            "declared": [
              "DECISION_LOG.md"
            ],
            "declared_by_specification": null,
            "declared_key": "append_only",
            "declared_source": "config",
            "paths": [
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
            "specification_paths_read": [],
            "supplied_by_config": [
              "DECISION_LOG.md"
            ]
          },
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
              "commit": "4f2c2d6f1937745f16e60426c879d1287bf721f3",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "cc7a766e085a068bdca60f2a0fcaf9adfb175449",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "bba84763cc55c4753d3b77b49dcb9b79034c6be0",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "0d7799057d56c27e487a20cca0994c2647016265",
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
            "declared": [],
            "declared_by_specification": null,
            "declared_key": "authorised_gates",
            "declared_source": "config",
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "specification_paths_read": [],
            "supplied_by_config": [],
            "unauthorised_changed": []
          },
          "id": "P7",
          "status": "PASS",
          "title": "gate integrity"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "first_commit": "4f2c2d6f1937745f16e60426c879d1287bf721f3",
            "first_commit_paths": [
              "specs/2026-08-14T2212Z_mechanisms-cb.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-14T2212Z_mechanisms-cb.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-14T2212Z_mechanisms-cb.md"
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

### 12.7 RUN 2 output, verbatim

    {
      "base": "f179b45eee359ef007da5e30833e9aed92069039",
      "commits_in_range": 4,
      "commits_on_first_parent_line": 4,
      "head": "0d7799057d56c27e487a20cca0994c2647016265",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "append_only": null,
              "authorised_gates": null,
              "counted": 7,
              "counted_add": 3,
              "counted_modify": 4,
              "counted_set": [
                "reports/2026-08-XXT{HHMM}Z_mechanisms-cb.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_mechanisms-cb.md",
                "specs/2026-08-XXT{HHMM}Z_mechanisms-cb.md",
                "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                "scripts/governance_tools/task_checker.py",
                "tests/test_repository_structure.py",
                "tests/test_task_checker.py"
              ],
              "parse": "OK",
              "path": "specs/2026-08-14T2212Z_mechanisms-cb.md",
              "stated": 7,
              "stated_add": 3,
              "stated_modify": 4,
              "stated_record": "stated: 3 additions, 4 modifications"
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
                "commit": "4f2c2d6f1937745f16e60426c879d1287bf721f3",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "cc7a766e085a068bdca60f2a0fcaf9adfb175449",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "bba84763cc55c4753d3b77b49dcb9b79034c6be0",
                "work_paths": [
                  "scripts/governance_tools/task_checker.py",
                  "tests/test_repository_structure.py",
                  "tests/test_task_checker.py"
                ]
              },
              {
                "adds_review": false,
                "commit": "0d7799057d56c27e487a20cca0994c2647016265",
                "work_paths": [
                  "derivations/GOVERNANCE-ENFORCEMENT_classification.md"
                ]
              }
            ],
            "first_review_commit": "cc7a766e085a068bdca60f2a0fcaf9adfb175449",
            "first_work_commit": "bba84763cc55c4753d3b77b49dcb9b79034c6be0",
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
          "evidence": {
            "declared": [
              "DECISION_LOG.md"
            ],
            "declared_by_specification": null,
            "declared_key": "append_only",
            "declared_source": "config",
            "paths": [
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
            "specification_paths_read": [],
            "supplied_by_config": [
              "DECISION_LOG.md"
            ]
          },
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
              "commit": "4f2c2d6f1937745f16e60426c879d1287bf721f3",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "cc7a766e085a068bdca60f2a0fcaf9adfb175449",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "bba84763cc55c4753d3b77b49dcb9b79034c6be0",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "0d7799057d56c27e487a20cca0994c2647016265",
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
            "declared": [],
            "declared_by_specification": null,
            "declared_key": "authorised_gates",
            "declared_source": "config",
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "specification_paths_read": [],
            "supplied_by_config": [],
            "unauthorised_changed": []
          },
          "id": "P7",
          "status": "PASS",
          "title": "gate integrity"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "first_commit": "4f2c2d6f1937745f16e60426c879d1287bf721f3",
            "first_commit_paths": [
              "specs/2026-08-14T2212Z_mechanisms-cb.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-14T2212Z_mechanisms-cb.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-14T2212Z_mechanisms-cb.md"
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

## 13. Validators — A14, MEASURED

    before, at the evidence base f179b45e…    310 passed, 2 deselected
    after,  at commit 4 0d779905…             324 passed, 2 deselected     exit 0

    delta   +14 passed,  deselected unchanged at 2

**The count MUST rise and it did.** **What accounts for the +14, MEASURED
rather than estimated:**

    tests/test_task_checker.py           61 -> 73 test functions      +12
    tests/test_repository_structure.py    4 ->  6 test functions       +2
                                                                      ---
                                                                      +14

**A count that had not moved would have meant the new tests were not being
collected**, which is the failure this criterion exists to catch. Every added
function is collected: the two files' own totals account for the delta
exactly, with no parametrisation to reconcile.

**The twelve added to `test_task_checker.py`** are four `C1` fixtures (the
real file through the helper; the conjunction's three rejected shapes; a digit
in an id segment surfacing through `P7`; a title-less heading surfacing the
same way) and eight `C3` fixtures (declaration in the scope block; the JSON
naming config; conflict; agreement; `DECLARED_EMPTY`; `NOT_DECLARED`; `P7`
reading its set from the scope block; a non-gate-id rejected). **The two added
to `test_repository_structure.py`** are the agreement invariant and the
conjunction's identity.

---

## 14. Commits — A15, MEASURED for commits 1–4

    commit 1   4f2c2d6f1937745f16e60426c879d1287bf721f3   specs/2026-08-14T2212Z_mechanisms-cb.md
    commit 2   cc7a766e085a068bdca60f2a0fcaf9adfb175449   reviews/chatgpt/2026-08-14T2212Z_mechanisms-cb.md
    commit 3   bba84763cc55c4753d3b77b49dcb9b79034c6be0   task_checker.py + test_task_checker.py + test_repository_structure.py
    commit 4   0d7799057d56c27e487a20cca0994c2647016265   derivations/GOVERNANCE-ENFORCEMENT_classification.md

    UTC token fixed by commit 1:  2212Z        day at execution: 14

**Stored subjects, MEASURED:**

    commit 1   spec: C-b, one gate-heading grammar and declarations a reviewer sees
    commit 2   review: pre-execution review for the C-b mechanisms
    commit 3   mechanisms: one gate-heading grammar, and declared sets a reviewer sees
    commit 4   docs: record where P3's and P7's declared sets now come from

| Commit | `Co-Authored-By` | session id or URL | tool attribution | Trailer suppressed? |
|---|---|---|---|---|
| 1 | none | none | none | **No — none was ever written** |
| 2 | none | none | none | **No — none was ever written** |
| 3 | none | none | none | **No — none was ever written** |
| 4 | none | none | none | **No — none was ever written** |

**Commit 5's message, INTENDED:**

    report: C-b builds one grammar and declarations a reviewer sees

**Commit 5 is post-report evidence. Nothing in this report measures it.**

**Code and both test files moved together in commit 3**, as §8 requires: there
is no revision at which the helper existed and a call site still carried its
own expression.

### 14.1 `F1`, and Rule 20 — which binds this task and was not needed

My harness's standing git guidance instructs a `Co-Authored-By` trailer and a
session URL. **Each message was composed without them at first writing.**
`P6` reports `PASS` on all four commits in every one of the four invocations.

**Rule 20 landed at the evidence base and BINDS this task** — unlike the task
that wrote it. **It was not invoked:** no commit carried a mechanically
detected hygiene violation, **so no amend was made, no commit ids need
reporting, and the "every affected check re-run" clause was not reached.**
**`F1` remains unrepaired and is reported, not fixed.**

---

## 15. Rule 16 assessment — all three junctions

### 15.1 First — a reviewer now sees the declaration; a specification can still declare wrongly

**After this, one grammar reads the gate registry and the declared sets live
in the reviewed artifact. A reader may take that for the declared-set problem
being solved. It is not.**

**A specification still declares its own sets and can declare them wrongly.**
Nothing verifies that a declared append-only set is complete, or that an
authorised-gate set names only gates the task was authorised to change.
**`P3` does not check the declaration against anything**, and this task
deliberately does not make it — §3 records that an earlier version required a
repository-wide append-only list that does not exist, and that the
requirement was withdrawn.

**What changed is that a reviewer now SEES the declaration.** It moved from a
JSON file written after the review into the artifact the review is of. **A
wrong declaration is now wrong in front of someone, instead of being invented
afterwards.** That is a narrower discovery problem, not an absent one.

**`P3` and `P7` stay `PARTIAL` and the classification says why** — §10's diff
carries the sentence, on `main` after integration rather than only here.

### 15.2 Second — the invariant and the helper are written by the same hand

**The agreement invariant replaces a coincidence with a check, and the check
is written by the same hand as the helper it checks.** If I mis-specified the
canonical language, `test_both_gate_heading_call_sites_agree` would agree with
my mistake — both sides now call the same function, so they cannot disagree
about it. **The invariant proves the two call sites share an implementation.
It cannot prove the implementation is right.**

**What would detect the helper and its test drifting together, named and NOT
built here:**

1. **An expected-id-set assertion with the fourteen ids written down**, so a
   grammar change that silently drops or admits one fails against a literal
   rather than against itself. It costs a test edit per legitimate gate
   addition; **that cost is the point** — it makes the registry's contents a
   declared quantity rather than a discovered one.
2. **A differential test against a deliberately independent second reader** —
   the shape `RAW_GATE_HEADING` already has for `P7`. The raw counter is
   exactly this for the *count*; nothing plays that role for the *id set*.
3. **A property test over generated headings**, asserting the accepted
   language equals a specification written separately from the expression.

**None is built here, as §9 requires.** **This is the third time this
programme has met this regress** — the pin validator's non-empty assertion,
`P7`'s completeness guard, and now this — **and naming it is not solving it.**

### 15.3 Third — `C2` remains open, and compliance rests on an authoring habit

**Nothing requires a newly issued specification to carry `stated:`,
`append_only:` or `authorised_gates:`.** **This task makes the declarations
POSSIBLE and READABLE. It does not make them MANDATORY.**

**A specification that declares none of them still reaches `NOT_DECLARED` for
`P3` and `P7` and `NOT_PARSEABLE` for `P1`** — non-green, but only if someone
runs the checker over it, which the specification itself must arrange.
**Compliance therefore still rests on an authoring habit**, exactly as it did
before this task.

**This task is its own illustration.** Its specification carries `stated:` and
does not carry the two new keys (§12.5), and nothing anywhere objected until I
measured it by hand. **`C2` is what would object. It is unbuilt.**

---

## 16. Did building these mechanisms make me want to build `C2`?

**Yes, and more sharply than in the previous task, because this one produced
the evidence for it.**

**The pull was concrete.** Having added `append_only:` and
`authorised_gates:` to the scope-block grammar, requiring them is a
three-line change: `parse_scope_block` already distinguishes absent from
empty, so returning `NOT_PARSEABLE` when a key is missing is the same shape as
the `stated:` refusal that already exists. **I could see it while writing
`_declared_item`.**

**And §12.5 is exactly the case that would have been caught.** This
specification asserts that its scope block declares the two keys; it does
not; **nothing mechanical noticed.** A `C2` that required the keys would have
failed this task's own RUN 2 and sent the discrepancy back before execution
rather than into a report.

**I did not build it.** §6 puts `C2` out of scope and reserves it, and a
requirement that would fail the majority of the existing corpus — 37 of 50
specifications carry no `stated:` key, and all but one carry no `append_only:`
— **needs its own specification and its own review to decide what happens to
those.** Landing it here would have converted a mechanism task into a
corpus-wide migration nobody reviewed.

**I confirm I did not build `C2`, did not build `C4` or `C5`, registered
nothing, and created no repository-wide append-only list.** **MEASURED:** the
changed-file set is the six paths of §11.1, and `derivations/` is otherwise
untouched.

---

## 17. Stops and clarifications

### 17.1 Stops

**None.** No stop was reached in any of the five primary categories:
`SPECIFICATION_DEFECT`, `ENVIRONMENT`, `OBSERVATION_METHOD_ERROR`,
`REPOSITORY_DEFECT`, `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`.

**Every stop condition the specification names was tested and none
triggered:** A1's ref matched; A2's review names the executed digest; **§1's
"if the conjunction accepts fewer than fourteen" was measured and it accepts
fourteen**; A7(iii)'s conflict STOP fired as designed in its fixture and did
not arise in this task's own range; A9 shows no verdict changed; A13's RUN 2
exited 0 with `P7` at fourteen sections; A14's count rose.

### 17.2 Secondary findings

**S1 — `SPECIFICATION_DEFECT`, non-blocking, and the one that matters.**
**A13 asserts that this specification's own scope block declares `append_only`
and `authorised_gates`. It declares neither** (§12.5). The instruction "make
them agree, and report that you did" therefore has no referent.

**Why this is not a stop.** The specification defines the path that actually
applies: §3(b)'s "when only config is present, the check proceeds and the JSON
says the value came from config". **Execution proceeded down a specified
route, not an invented one.** The stop A13 names — "if the two differ, RUN 2
STOPS" — requires two declarations, and there is one. **Nothing was decided by
me that the specification left open**, and the demonstrations A13 was reaching
for are supplied by A7's three fixtures instead.

**Why I did not repair it.** Adding the keys would have changed the
specification's bytes and broken the digest equality A2 measures, and §10
forbids adjusting this specification's declarations to make a precedence check
pass. **Reporting it is the available action.**

**S2 — `OBSERVATION_METHOD_ERROR` in my own working, twice, both self-caught
before they reached a conclusion.** F1's first measurement applied the
structure test's pattern without `re.MULTILINE` and reported 0 where the
original reads 14 (§7). A7(ii)'s first run reported `overall: INCOMPLETE`,
which was `P7` lacking a set in that fixture rather than anything about `P3`
(§8). **Both were re-measured; the corrected figures are the ones reported.**

**S3 — observation, on where the helper lives.** The natural home for a
helper shared by `scripts/` and `tests/` is
`scripts/governance_tools/core.py`, the module whose docstring is "Shared
implementation for the read-only governance CLIs". **`core.py` is not in
A10's `modify:` list**, so the helper lives in `task_checker.py` and the
structure test imports it from there. **That is a defensible home** — the
grammar belongs with the checker that uses it most — **but it was chosen by
the manifest, not on the merits**, and I record which.

**S4 — two pre-existing tests changed one accessor each.** `P3`'s evidence
gained provenance fields and its per-path findings moved under a `paths` key,
so two assertions reading `record["evidence"][0][...]` now read
`record["evidence"]["paths"][0][...]`. **Every assertion's subject and
expected value is unchanged.** No test was deleted, no check weakened. All 61
pre-existing `test_task_checker.py` functions and all 4 pre-existing
`test_repository_structure.py` functions still pass.

**`F1` and `F2`.** `F1` met and unrepaired (§14.1). `F2` not met in this
task's reading; `scripts/p2_phase01_scalar_exploratory.py` is among the 391
paths measured unchanged.

### 17.3 Ambiguous, unsatisfiable, or what I would have specified differently

**Nothing was unsatisfiable, and no instruction was inconsistent with a
repository rule or with another instruction.** Four observations:

1. **A6's insistence that fixture PURPOSE is stated first is the best
   criterion in this specification**, and it changed what I built. Without it
   I would have labelled F3 change-discriminating on the strength of the
   structure test's acceptance and quietly not mentioned that the checker
   already rejected it. **Naming the purpose before running the old code makes
   a mislabel visible rather than convenient.**
2. **The specification does not say which subject specification's declaration
   governs when a range carries more than one.** RUN 1 often selects two. **I
   decided: all subject specifications are read, and two that declare
   DIFFERENT values raise the same conflict as specification-versus-config.**
   It did not arise here — this range has one — but the code would otherwise
   have silently taken whichever came first. **I would have specified it.**
3. **`DECLARATION_CONFLICT` is a new status word and the specification did not
   name one.** §3(b) says "that is a STOP" without saying how a STOP is
   represented in a vocabulary of six results. **I added a word rather than
   overloading `NOT_PARSEABLE`**, for the reason in §8, and I flag it because
   a specification that named the representation would have removed the
   judgement.
4. **A13's premise is the fourth criterion in this programme whose factual
   claim about the artifact did not hold.** The pattern is now familiar
   enough to be worth naming: **the specification's §12 verifies literals
   against the repository, and A13's claim is about the specification itself,
   which §12 does not cover.** **Amendment M(a) — a measurement is taken over
   the whole subject — would have caught it if the subject had included the
   specification's own manifest.**

### 17.4 Rule 13

**No environment failure occurred, so neither of Rule 13's two diagnostic
orders was exercised.** **Rule 13 carries two such orders, a known open item;
I name neither as the one that applies.**

    Python   3.11.15
    pytest   9.1.1

**Nothing was installed.**

---

## 18. Evidence layering

**Committed in this report, MEASURED at commit 4:** A1–A12, A14 and A15 for
commits 1–4; A13's four invocations with both configs and both JSON outputs;
commits 1–4 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 5's message; A10's final scope
of 3 additions and 4 modifications.

**Post-report evidence, returned to the Reviewer and NOT written back:** A10's
final scope measured base-to-commit-5; A13-final, being RUN 2 re-run at commit
5; A14 at commit 5; A15 for commit 5; the push; the branch tip read back.

**Nothing in this report claims to measure commit 5.**

**`main` was not touched and nothing was merged.** **Integration is a separate
task**, and this report authorises none of it.
