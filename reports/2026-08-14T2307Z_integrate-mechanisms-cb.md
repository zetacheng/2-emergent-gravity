# Execution report — integrate the `C-b` mechanisms, and land them

**Specification:** `specs/2026-08-14T2307Z_integrate-mechanisms-cb.md`
**Specification evidence base:** `f179b45eee359ef007da5e30833e9aed92069039`
**Branch:** `governance/integrate-mechanisms-cb`, cut from authoritative `main` @ `f179b45e…`
**Source merged:** `governance/mechanisms-cb` @ `1c80e2f67c305b9f5b9656fefdbf0f7261bf34dc`
**Classification:** MATERIAL. Governed by Rule 15, Rule 18, and **Amendments M–P and Rules 19–21, which bind this task prospectively.**

**Every figure below is labelled MEASURED or INTENDED.** **This report is
written at commit 3, the merge commit, and measures nothing at commit 4.**

---

## 1. Outcome

**One merge, clean. Nothing auto-merged. Nothing edited.**

**MEASURED at commit 3:** 5 additions, 4 modifications, empty conflict list;
all seven source paths blob-identical to the source tip; 391 of 395 base paths
unchanged; `GATES.md` blob-identical; validators **310 → 324, delta +14**; all
four checker invocations `PASS` at exit 0.

**The result this task exists to produce, and it is the first of its kind.**

    P3   declared_source: specification     declared: ['DECISION_LOG.md']
    P7   declared_source: specification     declared: []
    no DECLARATION_CONFLICT arose
    P7 read 14 sections over 14 raw headings through the shared helper

**This is the first task in which a specification's own reviewed declaration
governed its own checker run.** **`C-b`'s `A13` claimed that of itself and was
wrong; I verified it here against the committed bytes rather than asserting
it** — §4 records the verification, §12.5 the result.

**And it is this task's result, not `C-b`'s.** **`C-b`'s `A13` is not
satisfied by this**, and §2's ruling says so: it remains a recorded
specification defect. **`C-b` demonstrated declaration parsing and precedence
through fixtures; it did not demonstrate the end-to-end authoring path, and
this report does not describe it as demonstrated.**

**What does not change.** **`P3` and `P7` remain `PARTIAL`.** A specification
still declares its own sets and can declare them wrongly, and nothing here
verifies that a declaration is complete. **`C2` remains open** — nothing
requires a newly issued specification to carry the keys, so compliance still
rests on an authoring habit. **`F1` and `F2` arrive unrepaired.**

**A16, answered up front.** My harness's standing git guidance does instruct a
`Co-Authored-By` trailer and a session URL. **None was written on any of the
four commits.** **Rule 20 binds this task and was not needed**: no commit
carried a violation, none was amended, no history was rewritten, **so there
are no two commit ids to report.**

---

## 2. Refs — A1, MEASURED

**Read from the remote after `git fetch origin`:**

    refs/heads/main                    f179b45eee359ef007da5e30833e9aed92069039    as specified
    refs/heads/governance/mechanisms-cb 1c80e2f67c305b9f5b9656fefdbf0f7261bf34dc   as specified

**No mismatch. No stop.**

---

## 3. The pre-execution review — A2, MEASURED

    supplied specification    3b75f9ad3f038b9cf3fcd2d52807851b6855e899b00ad8209d3d1d9c38163ff5
    committed specification   3b75f9ad3f038b9cf3fcd2d52807851b6855e899b00ad8209d3d1d9c38163ff5   equal
    supplied review           95fc49f2e23d9982be0e9ae28b315dc0d90179fc8f0b1cc2f3ea7114a57c7fc4
    committed review          95fc49f2e23d9982be0e9ae28b315dc0d90179fc8f0b1cc2f3ea7114a57c7fc4   equal

The review's `reviewed specification SHA-256:` is filled in and names the
digest of the specification actually committed and executed. **Committed
unedited, per Rule 18 and Amendment `N`, and before the merge**, per Rule 15's
timing clause. **Both artifacts arrived as FILES**, which Amendment `N(a)`
requires of the producer and Rule 18 requires me to report.

---

## 4. This specification's own scope block — verified, not asserted

**§10 asserts that this specification's scope block carries both new keys.**
**`C-b`'s `A13` asserted the same of itself and was false, so I measured this
one before relying on it**, reading the committed bytes rather than the
sentence.

**MEASURED — the scope keys present, extracted from the committed file:**

    stated  append_only  authorised_gates  base  head  mode  add  modify  forbidden_operations

**Both declarations are really there, and their values are:**

    append_only: DECISION_LOG.md
    authorised_gates: []

**§10's self-claim holds. This is the difference between §10 and `C-b`'s
`A13`, and it is a difference in evidence rather than in wording** — §10 says
the claim is checked against the committed bytes, and A14 requires the same
again at run time, which §12.5 reports.

---

## 5. Merge parentage — A3, three separately derived measurements

**Each by a different method, all before the merge existed.**

| Value | Method | MEASURED |
|---|---|---|
| parent 1 | `git rev-parse HEAD` on the branch tip after commit 2 | `bd50e874264be879e9df0361a4ae054e5ecb16ee` |
| parent 2 | `git rev-parse 1c80e2f6…^{commit}` | `1c80e2f67c305b9f5b9656fefdbf0f7261bf34dc` |
| merge-base | `git merge-base HEAD 1c80e2f6…` | `f179b45eee359ef007da5e30833e9aed92069039` |

**The merge-base equals the evidence base** and **is NOT parent 1** — parent 1
carries this task's two commits. **Commit 1 is an ancestor of parent 1:**
`git merge-base --is-ancestor fdd1fab6… bd50e874…` → **exit status 0**.

**Confirmed against the merge commit as stored:**

    git rev-list --parents -n 1 HEAD
    cf397545…  bd50e874…  1c80e2f6…

**A fourth derivation from the checker:** `P5` recomputes the same three values
with `merge_base_equals_parent_1: false`.

---

## 6. The conflict list — A4, MEASURED

    git diff --name-only --diff-filter=U      (no output)
    unmerged path count                       0
    git ls-files -u | wc -l                   0

**Empty.** The merge printed only *"Automatic merge went well; stopped before
committing as requested"* — **no `Auto-merging` line for any path.**

**Additionally, MEASURED tree-wide over every tracked file at commit 3:** a
search for conflict markers at line start returns **0 hits**, over all tracked
paths with no directory exclusion.

---

## 7. Scope — A5, and A6's source-derived split

### 7.1 A6 — derived from the SOURCE, not read from A5's list

    git diff --name-status f179b45 1c80e2f6

    M  derivations/GOVERNANCE-ENFORCEMENT_classification.md
    A  reports/2026-08-14T2212Z_mechanisms-cb.md
    A  reviews/chatgpt/2026-08-14T2212Z_mechanisms-cb.md
    M  scripts/governance_tools/task_checker.py
    A  specs/2026-08-14T2212Z_mechanisms-cb.md
    M  tests/test_repository_structure.py
    M  tests/test_task_checker.py

    MEASURED   3 additions + 4 modifications = 7 paths

**A5's prose says "three additions and four modifications" from the source.
MEASURED: three and four. AGREES.** **No disagreement to report.**

**A5's arithmetic reconciles:** 7 source + 3 authored here (all additions) =
10 paths = 6 additions + 4 modifications.

### 7.2 A5 — scope, MEASURED at commit 3

    M  derivations/GOVERNANCE-ENFORCEMENT_classification.md
    A  reports/2026-08-14T2212Z_mechanisms-cb.md
    A  reviews/chatgpt/2026-08-14T2212Z_mechanisms-cb.md
    A  reviews/chatgpt/2026-08-14T2307Z_integrate-mechanisms-cb.md
    M  scripts/governance_tools/task_checker.py
    A  specs/2026-08-14T2212Z_mechanisms-cb.md
    A  specs/2026-08-14T2307Z_integrate-mechanisms-cb.md
    M  tests/test_repository_structure.py
    M  tests/test_task_checker.py

    additions 5   modifications 4   deleted/renamed/copied/type-changed/unmerged/unknown 0

**INTENDED at commit 4:** 6 additions and 4 modifications — the nine above
plus `reports/2026-08-14T2307Z_integrate-mechanisms-cb.md`.

**Both figures with the head each was measured at: 5/4 at commit 3
`cf397545…`, MEASURED; 6/4 at commit 4, INTENDED.**

---

## 8. Which merge case, and only then the blob comparison — A7

### 8.1 The case, established BEFORE any blob was compared

    merge-base                    f179b45eee359ef007da5e30833e9aed92069039
    refs/heads/main               f179b45eee359ef007da5e30833e9aed92069039

**The merge-base IS `main`.** There is no commit on `main` after it, so there
is no commit that could have touched any path since the source was cut.

**Per modified path, commits on `main` since the merge-base:**

    derivations/GOVERNANCE-ENFORCEMENT_classification.md    0    ONE-SIDED
    scripts/governance_tools/task_checker.py                0    ONE-SIDED
    tests/test_repository_structure.py                      0    ONE-SIDED
    tests/test_task_checker.py                              0    ONE-SIDED

**All four are one-sided: only the source changed them.**

### 8.2 What that makes the blob comparison mean

**In the one-sided case a merged blob EQUAL to the source is the CORRECT
result.** In the two-sided case the same measurement would mean **a side was
LOST**. **The number is identical and the meaning is opposite**, which is why
A7 requires the case first — and why an earlier integration in this line
reported a blob comparison that would have meant the opposite thing under
different circumstances.

### 8.3 The comparison, now interpretable

    derivations/GOVERNANCE-ENFORCEMENT_classification.md   c09a052cb5dc3e13266567023055f58d5d517770   IDENTICAL
    reports/2026-08-14T2212Z_mechanisms-cb.md              e44a9eb3b8400d4b97effd5acf5da0ec4485d8c7   IDENTICAL
    reviews/chatgpt/2026-08-14T2212Z_mechanisms-cb.md      6391c6e31c9bbb551c74ce195c6511936386f658   IDENTICAL
    scripts/governance_tools/task_checker.py               0c5b90b47f15283109e2b2e3fe5bd112fda83487   IDENTICAL
    specs/2026-08-14T2212Z_mechanisms-cb.md                900eae62a3d1ffc1fe6972de3a43f405c8903448   IDENTICAL
    tests/test_repository_structure.py                     636ab5592b7af65705bc11ac8c1a6fa39ab44a2e   IDENTICAL
    tests/test_task_checker.py                             f0998693438ee43eeae9ef20b323056a86ef3668   IDENTICAL

**All seven identical to the source tip, which under the one-sided case is
what correctness looks like.** **Not one byte of the arriving content was
authored, edited or reformatted by this task.**

**No path is in the two-sided case, so Amendment `P(b)`'s line-survival
measurement does not apply here.** **I did not perform it, and I do not report
it as having been performed** — reporting an unrun measurement as clean would
be the defect Amendment `M(a)` exists to prevent.

---

## 9. The helper at the merged head — A8, MEASURED

    gate_heading_ids(GATES.md)    14
    raw '^## P2-' count           14
    equal                         True

     1  P2-HK-01                       8  P2-BETAV-RECON-01
     2  P2-GAP-01                      9  P2-BETAV-ASSEMBLY-01
     3  P2-BETA-01                    10  P2-CHANNEL-FREEZE-01
     4  P2-BETAV-01                   11  P2-PHASE-01
     5  P2-NORM-01                    12  P2-MULTIPHASE-GRAV-01
     6  P2-BETAV-CIRC-01              13  P2-GRAV-ENGINE-RECOVERED-01
     7  P2-BETAV-NUMREPRO-01          14  P2-LATTICE-ONTOLOGY-01

**Fourteen of fourteen, equal to the raw count.** **Fewer would have made `P7`
return `NOT_PARSEABLE` — correct behaviour but a finding — and it did not
arise.** **This is one of the two landing preconditions §6 names, and it is
met.**

---

## 10. Both call sites use the helper — A9

**`tests/test_repository_structure.py` imports it:**

    from scripts.governance_tools.task_checker import (
        GATE_ID_TOKEN,
        gate_heading_ids,
    )

**and carries no gate-heading expression of its own: MEASURED, 0 regex
literals matching `P2-[A-Z` or `^##` in that file.**

### 10.1 The search, CODE separated from PROSE

**CODE — every `.py` file tracked by git, fixed-string, `__pycache__`
excluded:**

    task_checker.py:712   GATE_ID = r"P2-[A-Z]+(?:-[A-Z]+)*-\d+"        the one id shape
    task_checker.py:715   rf"^## ({GATE_ID})[ \t]+[—–-][ \t]+\S.*$"      the one heading grammar
    task_checker.py:746   RAW_GATE_HEADING = re.compile(r"^## P2-")      separate by design
    task_checker.py:710   a comment                                      prose in code
    test_task_checker.py:674  a comment quoting the OLD grammar          prose in code

**One gate-heading expression and one id shape exist in the repository's
code.** **`RAW_GATE_HEADING` remains separate and is not routed through the
helper**, preserving `P7`'s independent non-vacuity signal.

**PROSE — `specs/`, `reports/`, `reviews/`, `derivations/`:** **17 files quote
a gate-heading regex.** **These are historical records** — pre-issue
verification blocks, measurement tables and this line's own prior reports,
several quoting the *pre-repair* grammar `^## (P2-[A-Z0-9-]+)\s*$` as the
thing that was broken. **They are expected, they are not code, and nothing
compiles them.**

**One correction to my own working.** My first prose search used an
over-escaped pattern and returned **0 files**, which I did not believe given
that this line's reports quote the grammar repeatedly. **I re-ran with
fixed-string matching and got 17.** The zero was an artifact of my regex, not
a property of the repository.

---

## 11. The three declaration states at the merged head — A10

**One run each, against the merged code.**

### (a) No declaration anywhere

    status    NOT_DECLARED
    source    none          declared: None
    message   no append-only set declared by the specification or supplied by
              config; the set is not inferred
    overall   INCOMPLETE

### (b) `append_only: []`

    status    DECLARED_EMPTY
    source    specification   declared: []
    message   nothing was checked because nothing was declared applicable: the
              declared append-only set is empty, which is a declaration and not
              an exemption
    overall   PASS

### (c) A non-empty declared set

    status    PASS
    source    specification   declared: ['DECISION_LOG.md']
    message   (none — a PASS carries no reason field)
    overall   PASS

### 11.1 Can a reader of the JSON alone tell `DECLARED_EMPTY` from `PASS`?

**Yes, on three independent fields**, none requiring this report:

    status              DECLARED_EMPTY   vs   PASS
    reason              present, and says nothing was checked   vs   absent
    evidence.declared   []               vs   a populated list

### 11.2 Does `DECLARED_EMPTY` affect the exit status?

**It does not, and it must not.** Run (b) is `overall: PASS` with `P3` at
`DECLARED_EMPTY`. **`DECLARED_EMPTY` is not in `NON_GREEN`.**

**That is right because it is a VALID declaration.** `NOT_DECLARED` means the
specification said nothing, so a subject is missing and the run is
`INCOMPLETE`. **`DECLARED_EMPTY` means the specification SAID the applicable
set is empty** — nothing is missing, so there is nothing to be incomplete
about. **What keeps it from reading as a successful verification is the JSON,
not the exit code**, and §11.1 is why that suffices.


---

## 12. The checker — A14, MEASURED at commit 3

    base   f179b45eee359ef007da5e30833e9aed92069039
    head   cf397545f3116d57149f330a40414f4fd73400ba   (commit 3, the merge commit)

**Both prospectivity readings for each run, so four invocations. All four
exited 0 with `overall: PASS`.**

    run 1 INCLUSIVE   exit 0   PASS   sha256 aa3219c59fe4e4121b2272579c922357b21c89c81c4eb065d48dbd57c243f1fe
    run 1 EXCLUSIVE   exit 0   PASS   sha256 1985d6cd89ad84a056703085f4b69c063dbaf52161f40d528c363b8a503c37d4
    run 2 INCLUSIVE   exit 0   PASS   sha256 e46aab575e30a879befd94062768b56d2fc4b516afca50e36651eef89072d49d
    run 2 EXCLUSIVE   exit 0   PASS   sha256 bfb07b680c739c55b38fbe2db59964a204f22056479cae11984af4eb3913fb2c

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 PASS
    P6 PASS   P7 PASS   P8 PASS   P9 PASS

### 12.1 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "f179b45eee359ef007da5e30833e9aed92069039",
      "head": "cf397545f3116d57149f330a40414f4fd73400ba",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 12.2 RUN 2 config, verbatim — stop-governing

    {
      "base": "f179b45eee359ef007da5e30833e9aed92069039",
      "head": "cf397545f3116d57149f330a40414f4fd73400ba",
      "specification_paths": ["specs/2026-08-14T2307Z_integrate-mechanisms-cb.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I supplied of my own choosing; all are
taken from A14.** **Neither the config nor this specification's declarations
were adjusted to make RUN 2 pass** — §8 forbids both, and neither was needed:
they were written to agree and they do.

### 12.3 The measured RUN 1 subject set

**RUN 1's default selection chose TWO specifications**, because the merge
brings the source task's own into the range:

    specs/2026-08-14T2212Z_mechanisms-cb.md              stated add 3 modify 4   counted add 3 modify 4
    specs/2026-08-14T2307Z_integrate-mechanisms-cb.md    stated add 6 modify 4   counted add 6 modify 4

**RUN 2 names only the second**, as A14 requires. **A real difference, so both
JSON outputs are given verbatim below.** The two prospectivity readings differ
in exactly one line and in no verdict:

    324c324
    <         "inclusivity": "INCLUSIVE",
    ---
    >         "inclusivity": "EXCLUSIVE",

### 12.4 `P7`, and the section count it saw through the helper

    declared_source          specification
    declared                 []
    raw_heading_count_base   14        section_count_base   14
    raw_heading_count_head   14        section_count_head   14
    unauthorised_changed     []        added_sections  []   removed_sections  []

**`PASS` at fourteen sections, read through the shared helper. `PASS` at zero
would have been a STOP.**

### 12.5 The mechanism governing its own run — verified against the committed bytes

**This is what A14 asks to be verified rather than asserted, and it is the
first time it has been true.**

**MEASURED, identical in all four invocations:**

    P3   declared_source: specification    declared: ['DECISION_LOG.md']
    P7   declared_source: specification    declared: []

**Both properties took their set from this specification's own scope block,
not from the config.** **The config supplied the same two values**
(`append_only_paths: ["DECISION_LOG.md"]`, `authorised_modified_gates: []`),
**so the precedence rule resolved to `specification` and no
`DECLARATION_CONFLICT` arose.** **MEASURED: `DECLARATION_CONFLICT` appears
nowhere in any of the four outputs.**

**That the two agree is not luck and not an adjustment.** §4 measured the
specification's declarations from the committed bytes before the merge, and
A14's config is fixed by the specification. **Had they differed, `P3` and `P7`
would have returned `DECLARATION_CONFLICT`, RUN 2 would have exited non-zero,
and §8 makes that a finding and a STOP rather than something to fix by
editing either side.**

**What this is evidence of, stated narrowly.** **It shows the mechanism can
govern a task whose specification carries reviewed declarations.** **It is
not evidence that `C-b`'s `A13` was satisfied** — that criterion was about
`C-b`'s own specification, which declared nothing, and §2's ruling records it
as a defect. **This task's success is this task's.**

### 12.6 RUN 1 output, verbatim

    {
      "base": "f179b45eee359ef007da5e30833e9aed92069039",
      "commits_in_range": 8,
      "commits_on_first_parent_line": 3,
      "head": "cf397545f3116d57149f330a40414f4fd73400ba",
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
            },
            {
              "append_only": [
                "DECISION_LOG.md"
              ],
              "authorised_gates": [],
              "counted": 10,
              "counted_add": 6,
              "counted_modify": 4,
              "counted_set": [
                "reports/2026-08-14T2212Z_mechanisms-cb.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-mechanisms-cb.md",
                "reviews/chatgpt/2026-08-14T2212Z_mechanisms-cb.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-mechanisms-cb.md",
                "specs/2026-08-14T2212Z_mechanisms-cb.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-mechanisms-cb.md",
                "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                "scripts/governance_tools/task_checker.py",
                "tests/test_repository_structure.py",
                "tests/test_task_checker.py"
              ],
              "parse": "OK",
              "path": "specs/2026-08-14T2307Z_integrate-mechanisms-cb.md",
              "stated": 10,
              "stated_add": 6,
              "stated_modify": 4,
              "stated_record": "stated: 6 additions, 4 modifications"
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
                "commit": "fdd1fab67bc4bbd8f79cb801a874ac67ccde0b19",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "bd50e874264be879e9df0361a4ae054e5ecb16ee",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "cf397545f3116d57149f330a40414f4fd73400ba",
                "work_paths": [
                  "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                  "scripts/governance_tools/task_checker.py",
                  "tests/test_repository_structure.py",
                  "tests/test_task_checker.py"
                ]
              }
            ],
            "first_review_commit": "bd50e874264be879e9df0361a4ae054e5ecb16ee",
            "first_work_commit": "cf397545f3116d57149f330a40414f4fd73400ba",
            "in_scope": 3,
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
            "declared_by_specification": [
              "DECISION_LOG.md"
            ],
            "declared_key": "append_only",
            "declared_source": "specification",
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
            "specification_paths_read": [
              "specs/2026-08-14T2307Z_integrate-mechanisms-cb.md"
            ],
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
          "evidence": [
            {
              "compared_to_recorded": "UNAVAILABLE",
              "merge": "cf397545f3116d57149f330a40414f4fd73400ba",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "f179b45eee359ef007da5e30833e9aed92069039",
              "recomputed_parent_1": "bd50e874264be879e9df0361a4ae054e5ecb16ee",
              "recomputed_parent_2": "1c80e2f67c305b9f5b9656fefdbf0f7261bf34dc",
              "status": "PASS"
            }
          ],
          "id": "P5",
          "status": "PASS",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "fdd1fab67bc4bbd8f79cb801a874ac67ccde0b19",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "bd50e874264be879e9df0361a4ae054e5ecb16ee",
              "matches": [],
              "status": "PASS"
            },
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
            },
            {
              "commit": "1c80e2f67c305b9f5b9656fefdbf0f7261bf34dc",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "cf397545f3116d57149f330a40414f4fd73400ba",
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
            "declared_by_specification": [],
            "declared_key": "authorised_gates",
            "declared_source": "specification",
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "specification_paths_read": [
              "specs/2026-08-14T2307Z_integrate-mechanisms-cb.md"
            ],
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
            "first_commit": "fdd1fab67bc4bbd8f79cb801a874ac67ccde0b19",
            "first_commit_paths": [
              "specs/2026-08-14T2307Z_integrate-mechanisms-cb.md"
            ],
            "reports_added": [
              "reports/2026-08-14T2212Z_mechanisms-cb.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-14T2307Z_integrate-mechanisms-cb.md",
              "reviews/chatgpt/2026-08-14T2212Z_mechanisms-cb.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-14T2307Z_integrate-mechanisms-cb.md",
              "specs/2026-08-14T2212Z_mechanisms-cb.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": [
            {
              "heading_present": true,
              "path": "reports/2026-08-14T2212Z_mechanisms-cb.md",
              "status": "PASS"
            }
          ],
          "id": "P9",
          "status": "PASS",
          "title": "reports carry a Stops and clarifications section"
        }
      ],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 3,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

### 12.7 RUN 2 output, verbatim

    {
      "base": "f179b45eee359ef007da5e30833e9aed92069039",
      "commits_in_range": 8,
      "commits_on_first_parent_line": 3,
      "head": "cf397545f3116d57149f330a40414f4fd73400ba",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "append_only": [
                "DECISION_LOG.md"
              ],
              "authorised_gates": [],
              "counted": 10,
              "counted_add": 6,
              "counted_modify": 4,
              "counted_set": [
                "reports/2026-08-14T2212Z_mechanisms-cb.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-mechanisms-cb.md",
                "reviews/chatgpt/2026-08-14T2212Z_mechanisms-cb.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-mechanisms-cb.md",
                "specs/2026-08-14T2212Z_mechanisms-cb.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-mechanisms-cb.md",
                "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                "scripts/governance_tools/task_checker.py",
                "tests/test_repository_structure.py",
                "tests/test_task_checker.py"
              ],
              "parse": "OK",
              "path": "specs/2026-08-14T2307Z_integrate-mechanisms-cb.md",
              "stated": 10,
              "stated_add": 6,
              "stated_modify": 4,
              "stated_record": "stated: 6 additions, 4 modifications"
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
                "commit": "fdd1fab67bc4bbd8f79cb801a874ac67ccde0b19",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "bd50e874264be879e9df0361a4ae054e5ecb16ee",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "cf397545f3116d57149f330a40414f4fd73400ba",
                "work_paths": [
                  "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                  "scripts/governance_tools/task_checker.py",
                  "tests/test_repository_structure.py",
                  "tests/test_task_checker.py"
                ]
              }
            ],
            "first_review_commit": "bd50e874264be879e9df0361a4ae054e5ecb16ee",
            "first_work_commit": "cf397545f3116d57149f330a40414f4fd73400ba",
            "in_scope": 3,
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
            "declared_by_specification": [
              "DECISION_LOG.md"
            ],
            "declared_key": "append_only",
            "declared_source": "specification",
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
            "specification_paths_read": [
              "specs/2026-08-14T2307Z_integrate-mechanisms-cb.md"
            ],
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
          "evidence": [
            {
              "compared_to_recorded": "UNAVAILABLE",
              "merge": "cf397545f3116d57149f330a40414f4fd73400ba",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "f179b45eee359ef007da5e30833e9aed92069039",
              "recomputed_parent_1": "bd50e874264be879e9df0361a4ae054e5ecb16ee",
              "recomputed_parent_2": "1c80e2f67c305b9f5b9656fefdbf0f7261bf34dc",
              "status": "PASS"
            }
          ],
          "id": "P5",
          "status": "PASS",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "fdd1fab67bc4bbd8f79cb801a874ac67ccde0b19",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "bd50e874264be879e9df0361a4ae054e5ecb16ee",
              "matches": [],
              "status": "PASS"
            },
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
            },
            {
              "commit": "1c80e2f67c305b9f5b9656fefdbf0f7261bf34dc",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "cf397545f3116d57149f330a40414f4fd73400ba",
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
            "declared_by_specification": [],
            "declared_key": "authorised_gates",
            "declared_source": "specification",
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "specification_paths_read": [
              "specs/2026-08-14T2307Z_integrate-mechanisms-cb.md"
            ],
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
            "first_commit": "fdd1fab67bc4bbd8f79cb801a874ac67ccde0b19",
            "first_commit_paths": [
              "specs/2026-08-14T2307Z_integrate-mechanisms-cb.md"
            ],
            "reports_added": [
              "reports/2026-08-14T2212Z_mechanisms-cb.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-14T2307Z_integrate-mechanisms-cb.md",
              "reviews/chatgpt/2026-08-14T2212Z_mechanisms-cb.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-14T2307Z_integrate-mechanisms-cb.md",
              "specs/2026-08-14T2212Z_mechanisms-cb.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": [
            {
              "heading_present": true,
              "path": "reports/2026-08-14T2212Z_mechanisms-cb.md",
              "status": "PASS"
            }
          ],
          "id": "P9",
          "status": "PASS",
          "title": "reports carry a Stops and clarifications section"
        }
      ],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 3,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

---

## 13. Protected paths, gates and pins — A11, A12

### 13.1 A11, MEASURED

    paths existing at the evidence base                    395
    excluded (the four in A5's modify: list)                 4
    compared                                               391
    differing                                                0

    GATES.md                    IDENTICAL      tests/test_gate_pins.py    IDENTICAL
    CONVENTIONS.md              IDENTICAL      results/                   0 differing
    DECISION_LOG.md             IDENTICAL
    docs/BRANCHING_POLICY.md    IDENTICAL

### 13.2 A12 — gate invariants and pins, MEASURED

    1.  ^## P2- section count       14
    2.  P2-PHASE-01                 Status: PROPOSED          (GATES.md line 973)
    3.  prerequisites               ### Satisfied prerequisite — MICROSCOPIC PARAMETER DOMAIN        (line 1010)
                                    ### Satisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT (line 1035)
                                    zero occurrences of "### Unsatisfied prerequisite"
    4.  pins                        2 found, both MATCH

**`GATES.md` is blob-identical to the evidence base**, as §3 requires — every
mechanism landing here reads it.

---

## 14. Superseded branches — A13, MEASURED before the advance

    52f65117   exit 1      ebd531ab   exit 1      40168469   exit 1
    7146a093   exit 1      10c260b9   exit 1      d64cd912   exit 1

**Exit 1 means NOT an ancestor, for all six.** **No superseded-register entry
was written.**

---

## 15. Validators — A15, MEASURED

    before, at the evidence base f179b45e…    310 passed, 2 deselected
    after,  at commit 3 cf397545…             324 passed, 2 deselected     exit 0

    delta   +14 passed,  deselected unchanged at 2

**What accounts for the +14, MEASURED:**

    tests/test_task_checker.py            61 -> 73 test functions      +12
    tests/test_repository_structure.py     4 ->  6 test functions       +2
                                                                       ---
                                                                       +14

**The twelve** are four `C1` fixtures (the real file through the helper; the
conjunction's three rejected shapes; a digit inside an id segment surfacing
through `P7`; a title-less heading surfacing the same way) and eight `C3`
fixtures (declaration in the scope block; the JSON naming config; conflict;
agreement; `DECLARED_EMPTY`; `NOT_DECLARED`; `P7` reading its set from the
scope block; a non-gate-id rejected). **The two** are the agreement invariant
and the conjunction's identity.

**Every added function is collected**: the two files' own totals account for
the delta exactly, with no parametrisation to reconcile. **This is one of the
two landing preconditions §6 names, and it is met.**

---

## 16. Commits — A16, MEASURED for commits 1–3

    commit 1   fdd1fab67bc4bbd8f79cb801a874ac67ccde0b19   specs/2026-08-14T2307Z_integrate-mechanisms-cb.md
    commit 2   bd50e874264be879e9df0361a4ae054e5ecb16ee   reviews/chatgpt/2026-08-14T2307Z_integrate-mechanisms-cb.md
    commit 3   cf397545f3116d57149f330a40414f4fd73400ba   --no-ff merge of 1c80e2f6…

    UTC token fixed by commit 1:  2307Z        day at execution: 14

**Stored subjects, MEASURED:**

    commit 1   spec: integrate the C-b mechanisms, and land them
    commit 2   review: pre-execution review for the C-b mechanisms integration
    commit 3   merge: integrate the C-b mechanisms

| Commit | `Co-Authored-By` | session id or URL | tool attribution | Trailer suppressed? |
|---|---|---|---|---|
| 1 | none | none | none | **No — none was ever written** |
| 2 | none | none | none | **No — none was ever written** |
| 3 | none | none | none | **No — none was ever written** |

**Commit 4's message, INTENDED:**

    report: the C-b mechanisms land on main

**Commit 4 is post-report evidence. Nothing in this report measures it.**

**Rule 20 binds this task and was not invoked.** No commit carried a
mechanically detected hygiene violation, **so no amend was made, there are no
two commit ids to report, and the "every affected check re-run" clause was not
reached.** **`F1` remains unrepaired and is reported, not fixed.**

---

## 17. Rule 16 assessment — all four junctions

### 17.1 First — one grammar and reviewed declarations; `P3` and `P7` stay `PARTIAL`

**After this lands, one grammar reads the registry and declarations sit in
reviewed artifacts. A reader may take that for the declared-set problem being
solved. It is not.**

**A specification still declares its own sets and can declare them wrongly.**
Nothing verifies that a declared append-only set is complete, or that an
authorised-gate set names only gates the task was authorised to change.
**What changed is that a reviewer now SEES the declaration** — it moved from a
JSON file written after the review into the artifact the review is of.

**Where a reader meets that, as locations on `main` after this merge:**

- **`derivations/GOVERNANCE-ENFORCEMENT_classification.md`**, the `P3` and
  `P7` rows, both still reading `PARTIAL`, and the added paragraphs stating
  that the discovery problem narrows rather than vanishes;
- **`scripts/governance_tools/task_checker.py`**, each property's
  `does_not_establish` field, carried into every JSON the checker emits;
- **`reports/2026-08-14T2212Z_mechanisms-cb.md` §15.1**, the source task's own
  first junction.

### 17.2 Second — this task's success is this task's, not `C-b`'s

**`C-b` did NOT demonstrate the end-to-end authoring path.** §2's ruling
records why: its specification asserted that its own scope block declared
`append_only` and `authorised_gates`, and **it declared neither**. Its
executor followed the specification's expressly defined config-only path,
which the PI has ratified, and **`A13` remains a recorded specification
defect that is not retroactively satisfied.**

**This integration IS the first task in which a specification's own
declaration governed its own run, and it did.** §12.5 gives the measurement:
`declared_source: specification` for both `P3` and `P7`, no conflict, verified
against the committed bytes rather than asserted.

**These are two different facts and this report keeps them apart.** **`C-b`
built the mechanism and demonstrated it through fixtures. This task is the
first subject of it.** **Nothing here converts `C-b`'s false self-description
into a satisfied criterion**, and a later reader who finds this task's success
should not carry it back one branch.

### 17.3 Third — the helper and its agreement test share an author

**The agreement invariant replaces a coincidence with a check, and the check
is written by the same hand as the helper it checks.** Both call sites now
call one function, so they cannot disagree about it; **the invariant proves
they share an implementation, not that the implementation is right.**

**What would detect them drifting together, named and NOT built here:**

1. **An expected-id-set assertion with the fourteen ids written down**, so a
   grammar change that silently drops or admits one fails against a literal
   rather than against itself.
2. **A differential test against a deliberately independent second reader** —
   the role `RAW_GATE_HEADING` already plays for the *count*, and which
   nothing plays for the *id set*.
3. **A property test over generated headings**, asserting the accepted
   language against a specification written separately from the expression.

**This programme has met this regress before** — a guard written by the hand
that wrote the thing it guards. **That is a contextual statement and not a
count.** **I do not report a number of prior instances**, because §7 is right
that a historical tally is a claim whose scope must be checked like any other,
**and I have not located and verified each one.** My own earlier reports have
put a number on it; **that number is not carried here.**

**Naming the regress is not solving it.**

### 17.4 Fourth — the suite count rises again, and that is not coverage

**310 → 324.** **A larger green number is what a reader mistakes for more
coverage.**

**What accounts for the delta: fourteen tests about the two mechanisms this
merge lands** (§15), **not fourteen more rules enforced.** Twelve concern the
gate-heading grammar and the declaration states; two concern the agreement
invariant. **They test the new code. They do not extend coverage to anything
else.**

**Two mechanisms landing is not the enforcement gap closing.** **`C2` is
open** — nothing requires a newly issued specification to carry `stated:`,
`append_only:` or `authorised_gates:`, so compliance rests on an authoring
habit. **And the classification's count of objects with no machine behind
them is unchanged by this merge**: `derivations/GOVERNANCE-ENFORCEMENT_classification.md`
§5 is byte-identical across it, because `C-b` edited only the `P3` and `P7`
entries and left the count alone.

---

## 18. Did integrating these mechanisms make me want to build `C2`?

**Yes, and §4 is why.**

**The concrete pull.** I had to verify by hand that this specification's scope
block really carries the two keys, **because the previous task's specification
claimed exactly that and was wrong and nothing mechanical noticed.** A `C2`
that required the keys would have made that check automatic: the `C-b`
specification would have failed its own RUN 2 and the discrepancy would have
surfaced before execution instead of in a report and then a PI ruling.

**I did not build it.** §3 puts `C2` out of scope and reserves it, and §8
forbids modifying any arriving file. **A requirement that would fail most of
the existing corpus needs its own specification and its own review** to decide
what happens to those documents — landing it inside an integration would
convert a merge into an unreviewed corpus-wide migration.

**I confirm I did not build `C2`, registered nothing, and modified no arriving
file.** **MEASURED:** the changed-file set is the nine paths of §7.2, all
seven source paths are blob-identical to the source tip, and `derivations/` is
otherwise untouched.

---

## 19. Stops and clarifications

### 19.1 Stops

**None.** No stop was reached in any of the five primary categories:
`SPECIFICATION_DEFECT`, `ENVIRONMENT`, `OBSERVATION_METHOD_ERROR`,
`REPOSITORY_DEFECT`, `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`.

**Every stop condition the specification names was tested and none
triggered:** A1's refs matched; A2's review names the executed digest; A4's
conflict list is empty; **A8 reports fourteen of fourteen**; **A14's RUN 2
exited 0 with `declared_source: specification` and no
`DECLARATION_CONFLICT`**; **A15's count rose**. **§8's "if they do not agree,
that is a finding and a STOP" was tested against the committed bytes and they
agree.** **§6's two landing preconditions are both met.**

### 19.2 Secondary findings

**S1 — `C-b`'s `A13` remains a recorded specification defect**, per §2's PI
ruling, and **this task does not satisfy it.** §17.2 keeps the two facts
apart. **The deeper pattern — an acceptance criterion making an unchecked
factual assertion about the specification artifact itself, a narrower subtype
of `C4` — is recorded and not repaired here.** **Registering it is `C-c`'s,
whose list has grown again**, and §3 forbids this task from registering
anything.

**S2 — `OBSERVATION_METHOD_ERROR` in my own working, self-caught.** My first
prose search for stray gate-heading expressions used an over-escaped pattern
and returned **0 files**, which I disbelieved because this line's own reports
quote the grammar repeatedly. **Re-run with fixed-string matching: 17 files.**
The zero was an artifact of my regex. §10.1 reports the corrected figure.

**S3 — observation on A7's design, and it earned its keep.** Requiring the
merge case *before* the blob comparison changed what I could conclude: all
seven paths are blob-identical to the source, and **that fact means
"correct" here and would mean "a side was lost" if any path had been
two-sided.** **The measurement is identical in both worlds.** Without §8.1 the
table in §8.3 would be uninterpretable.

**`F1` and `F2`.** `F1` met and unrepaired (§16). `F2` not met in this task's
reading; `scripts/p2_phase01_scalar_exploratory.py` is among the 391 paths
measured unchanged.

### 19.3 Ambiguous, unsatisfiable, or what I would have specified differently

**Nothing was unsatisfiable, and no instruction was inconsistent with a
repository rule or with another instruction.** Four observations:

1. **§10's new second kind of claim — facts the specification asserts about
   ITSELF — is the right repair for the `A13` failure**, and it worked: §4
   verified it and it held. **I would keep it, and I would go one step
   further** — the verification record could name the check a reader can
   re-run, as A14 does, rather than only recording the result.
2. **A7 is the strongest form this criterion has taken in this line.** Earlier
   integrations reported blob equality and reasoned about its meaning
   afterwards. **Establishing the case first makes the conclusion follow from
   the measurement rather than from the narrative.**
3. **§7's instruction not to report a count of prior regress instances is
   pointed at something I did.** My own earlier reports said "the third time
   this programme has met that shape" without locating each instance.
   **Amendment M(a) makes that a claim whose scope must be checked**, and
   §17.3 states the regress contextually with no number.
4. **A9's split between code and prose was necessary and I would keep it.**
   The prose hits number 17 and are entirely historical; a search that
   reported them undifferentiated would look like seventeen stray grammars.

### 19.4 Rule 13

**No environment failure occurred, so neither of Rule 13's two diagnostic
orders was exercised.** **Rule 13 carries two such orders, a known open item;
I name neither as the one that applies.**

    Python   3.11.15
    pytest   9.1.1

**Nothing was installed.**

---

## 20. Evidence layering

**Committed in this report, MEASURED at commit 3:** A1–A13, A15 and A16 for
commits 1–3; A14's four invocations with both configs and both JSON outputs;
commits 1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; A5's final
base-to-head scope of 6 additions and 4 modifications.

**Post-report evidence, returned to the Reviewer and NOT written back:** A5's
final scope measured base-to-commit-4; A14-final, being RUN 2 re-run at commit
4 before the landing; A12 and A13 re-run after the advance; A16 for commit 4;
the pre-advance `--is-ancestor` exit status; the exact push command; remote
`main` read back; the source tip unchanged; final ancestry confirmation.

**Nothing in this report claims to measure commit 4.**
