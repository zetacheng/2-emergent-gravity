# Execution report — integrate the P7 repair and the pin validator, and land it

**Specification:** `specs/2026-08-14T0511Z_integrate-p7-repair.md`
**Specification evidence base:** `88ef5eec08ab269eddcea8c617cf4f5b09b7336e`
**Branch:** `governance/integrate-p7-repair`, cut from authoritative `main` @ `88ef5eec…`
**Source merged:** `governance/p7-repair-and-pin-validator` @ `7102a60ef249da04e2ad3326a3b8135b688aa065`
**Classification:** MATERIAL. Governed by Rule 15 and Rule 18.

**Every figure below is labelled MEASURED or INTENDED.** **This report is
written at commit 3, the merge commit, and measures nothing at commit 4.**

---

## 1. Outcome

**One merge, clean. Both landing preconditions met.**

**§5 makes the advance conditional on two measurements, and both were
taken at the merged head before anything was pushed:**

    A8    raw '^## P2-' 14   parsed 14   equality TRUE   pre-merge grammar 0
    A10   301 passed, 2 deselected, up from 280; tests/test_gate_pins.py collected, 11 tests

**MEASURED at commit 3:** 6 additions, 3 modifications, 9 changed paths,
empty conflict list. All seven source-contributed paths blob-identical to the
source tip. `GATES.md` byte-identical at base and head —
`2b3bd5069414f009e1a0466c4990db2949519bd8` at both. All four checker
invocations `PASS` at exit 0, **with `P7` reporting 14 sections over 14 raw
headings while running the repair it is integrating.**

**What `main` will carry, and the reading it must not receive.**
**Governance is NOT enforced.** **Twenty-two of twenty-nine objects still
have no machine behind them**, and `P7` remains `PARTIAL` because the
authorised-set discovery problem is untouched. **Two checks now work. That is
the whole claim.** A `P7` `PASS` now means *fourteen sections parsed, none
changed without authorisation*, where it meant *zero compared against zero*;
**the improvement is that the sentence has content, not that the content is
large.**

**`governance/p1-declared-total` is not merged and its `A10` is not
discharged.** **Nothing in this report or in any of this task's commit
messages claims that `P1` and `P7` are order-independent** — §14.4 records the
search that confirms it.

**A15, answered up front.** My harness's standing git guidance does instruct a
`Co-Authored-By` trailer and a session URL. **None was written on any of the
four commits**, nothing was suppressed by amendment, and no commit was
amended.

---

## 2. Refs — A1, MEASURED

**Read from the remote after `git fetch origin`:**

    refs/heads/main                                     88ef5eec08ab269eddcea8c617cf4f5b09b7336e   as specified
    refs/heads/governance/p7-repair-and-pin-validator   7102a60ef249da04e2ad3326a3b8135b688aa065   as specified
    refs/heads/governance/p1-declared-total             8ff032e7f90ecfce4666fac34691b5670016bb75   as specified

**No mismatch. No stop.** **`governance/p1-declared-total` is confirmed
unchanged at `8ff032e7…` after this task** in the post-advance evidence, which
is returned separately; it was not merged, not moved, and its `A10` was not
discharged.

---

## 3. The pre-execution review — A2, MEASURED

    supplied specification    8932e99a88f43957ac78f2a14b9d35fe1f1dec1a0f394676720e82418a5a9f03
    committed specification   8932e99a88f43957ac78f2a14b9d35fe1f1dec1a0f394676720e82418a5a9f03   equal
    supplied review           07e3b8a299a1928b2a8aeb95f1907a6e0f50aeea9958b99d71cf6fb5e46642fc
    committed review          07e3b8a299a1928b2a8aeb95f1907a6e0f50aeea9958b99d71cf6fb5e46642fc   equal

The review's `reviewed specification SHA-256:` field is filled in and reads
`8932e99a88f43957ac78f2a14b9d35fe1f1dec1a0f394676720e82418a5a9f03` — **the
digest of the specification actually committed and executed.** Not blank, not
a different specification. Committed unedited, per Rule 18, and **committed
before the merge**, per Rule 15's timing clause.

---

## 4. Merge parentage — A3, three separately derived measurements

**Each by a different method, all three taken BEFORE the merge existed.**

| Value | Method | MEASURED |
|---|---|---|
| parent 1 | `git rev-parse HEAD` on the branch tip after commit 2 | `5354b63e954b1d6a9d1959e06c700a432447a6cb` |
| parent 2 | `git rev-parse 7102a60e…^{commit}` — the pinned ref resolved to a commit object | `7102a60ef249da04e2ad3326a3b8135b688aa065` |
| merge-base | `git merge-base HEAD 7102a60e…` — computed from the two, not assumed | `88ef5eec08ab269eddcea8c617cf4f5b09b7336e` |

**The merge-base equals the evidence base:** yes.
**The merge-base is NOT parent 1:** confirmed — parent 1 carries this task's
two commits, so the base of the merge lies behind it.
**Commit 1 is an ancestor of parent 1:** `git merge-base --is-ancestor
56c094c6… 5354b63e…` → **exit status 0**.

**Confirmed against the merge commit as stored:**

    git rev-list --parents -n 1 HEAD
    22bfa684…  5354b63e…  7102a60e…

**A fourth derivation arrived unsolicited from the checker.** `P5` recomputes
parentage from the merge itself: `recomputed_parent_1: 5354b63e…`,
`recomputed_parent_2: 7102a60e…`, `recomputed_merge_base: 88ef5eec…`,
`merge_base_equals_parent_1: false`. **All four agree.**

---

## 5. The conflict list — A4, MEASURED

    git diff --name-only --diff-filter=U      (no output)
    unmerged path count                       0
    git ls-files -u | wc -l                   0

**Empty.** `git merge --no-ff --no-commit` reported *"Automatic merge went
well; stopped before committing as requested"*. **Nothing moved since the dry
run.**

**Additionally, MEASURED tree-wide over every tracked file at commit 3:** a
search for conflict markers at line start returns **0 hits**, over all tracked
paths with no directory exclusion.

---

## 6. Scope — A5, and the three figures kept apart

**MEASURED at commit 3, the merge commit:**

    M  derivations/GOVERNANCE-ENFORCEMENT_classification.md
    A  reports/2026-08-14T0325Z_p7-repair-and-pin-validator.md
    A  reviews/chatgpt/2026-08-14T0325Z_p7-repair-and-pin-validator.md
    A  reviews/chatgpt/2026-08-14T0511Z_integrate-p7-repair.md
    M  scripts/governance_tools/task_checker.py
    A  specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md
    A  specs/2026-08-14T0511Z_integrate-p7-repair.md
    A  tests/test_gate_pins.py
    M  tests/test_task_checker.py

    additions 6   modifications 3   deleted/renamed/copied/type-changed/unmerged/unknown 0
    total changed paths 9

**INTENDED at commit 4:** 7 additions and 3 modifications — the nine above
plus `reports/2026-08-14T0511Z_integrate-p7-repair.md`, giving A5's manifest
of ten paths.

**The three figures the specification warns are distinct, all MEASURED and
reconciled:**

    6   additions at the merge commit
    7   paths contributed by source branch 7102a60e…   ← what A6 compares
    9   changed paths at the merge commit               = 7 source + 2 authored here

**Both scope figures with the head each was measured at: 6/3 at commit 3
`22bfa684…`, MEASURED; 7/3 at commit 4, INTENDED.**

---

## 7. Source-branch artifacts intact — A6, MEASURED

**The seven were derived from the source branch itself —
`git diff --name-only 88ef5eec 7102a60e` — not read off this specification**,
and the derivation returned exactly seven.

**Source tip blob vs merge-commit blob:**

    derivations/GOVERNANCE-ENFORCEMENT_classification.md         74fc207423f1a7f91f3249d187f3155773124332   IDENTICAL
    reports/2026-08-14T0325Z_p7-repair-and-pin-validator.md      c426f956400a40bd568e94e9c1538dc46b5c13fc   IDENTICAL
    reviews/chatgpt/2026-08-14T0325Z_p7-repair-and-pin-validator.md
                                                                 50b4939fb33463ba8a88a8164f7764b795597c2a   IDENTICAL
    scripts/governance_tools/task_checker.py                     b41a5b34728339829420174ab02b809a3d55f483   IDENTICAL
    specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md        54a11bd2522484935ee78bd019e066267abf8aeb   IDENTICAL
    tests/test_gate_pins.py                                      32664ad0bf584227501751de01fa1737ac536cca   IDENTICAL
    tests/test_task_checker.py                                   7d71230869f0f9d6e8977179c318ba78554daf4c   IDENTICAL

**All seven identical. Not one byte of the parser, the tests or the
classification was authored, edited or reformatted by this task.**

**The two additions excluded, named and with the reason:**

    specs/2026-08-14T0511Z_integrate-p7-repair.md              this task's own specification
    reviews/chatgpt/2026-08-14T0511Z_integrate-p7-repair.md    this task's own review

**They exist on no source branch — verified, not assumed:**
`git rev-parse 7102a60e:<path>` fails for both. **They are outside the
comparison by construction, not by omission.**

---

## 8. `GATES.md` untouched — A7, MEASURED

    evidence base 88ef5eec…    2b3bd5069414f009e1a0466c4990db2949519bd8
    merged head   22bfa684…    2b3bd5069414f009e1a0466c4990db2949519bd8

**Identical, and equal to the value A7 names.** **This is the precondition
for A8 being trustworthy:** the grammar being landed reads this file, and a
`GATES.md` edited during the merge would make the first meaningful `P7`
result a measurement of something this task had just changed.

---

## 9. The first meaningful `P7` — A8, one measurement session

**All four numbers produced by a single script run against `GATES.md` at the
merged head, importing the integrated `GATE_HEADING` and `RAW_GATE_HEADING`
from the merged `task_checker.py`, and applying the pre-merge expression
`^## (P2-[A-Z0-9-]+)\s*$` to the same lines in the same pass.**

    raw '^## P2-' count          14      expected 14
    parsed section count         14      expected 14
    equality holds               True    expected true
    PRE-MERGE grammar parsed      0      expected 0

    distinct ids parsed          14      (no duplicate collapsing the count)

**Fourteen of fourteen, and the pre-merge grammar reads zero of the same
file in the same session.** **Both numbers come from one measurement, not
from the specification.**

**A `PASS` at the head with a section count of zero would have been a STOP.**
It is now unreachable: the completeness invariant returns `NOT_PARSEABLE` when
parsed and raw disagree, and again when raw is zero.

---

## 10. Pins, gates, and protected paths — A9, A11, A12

### 10.1 A9 — pins at the merged head, MEASURED

| # | `GATES.md` line | Artifact named above | Declared | Measured | Verdict |
|---|---|---|---|---|---|
| 1 | 1017 | `derivations/P2-PHASE-01_microscopic_parameter_domain.md` (line 1016) | `4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214` | same | **MATCH** |
| 2 | 1040 | `derivations/P2-PHASE-01_input_admissibility_contract.md` (line 1039) | `e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3` | same | **MATCH** |

**Pin count found: 2.** **A9's assertion that the count is at least one holds
— 2 ≥ 1.** **Both unchanged from the evidence base**, which follows from §8:
`GATES.md` is blob-identical, so the declared values cannot have moved, and
both pinned artifacts are among the paths A11 found unchanged.

### 10.2 A11 — protected paths, MEASURED

    paths existing at the evidence base                       376
    excluded as authorised modifications (A5's modify: list)    3
    compared                                                  373
    differing                                                   0

    GATES.md                   2b3bd5069414f009e1a0466c4990db2949519bd8   IDENTICAL
    CONVENTIONS.md             b3c96300a1f3eab967d3d141a1e81b278887342c   IDENTICAL
    DECISION_LOG.md            d9dd2bf3a8cca405f03b31c51b1f478c7db77ca2   IDENTICAL
    docs/BRANCHING_POLICY.md   3f0f35d4da448eb444d223fd003a5b0601792dc3   IDENTICAL

    everything under results/                                   0 differing
    everything under scripts/ other than task_checker.py        0 differing
    everything under tests/ other than the two named            0 differing

### 10.3 A12 — gate invariants at the merged head, MEASURED

    1.  ^## P2- section count                    14
    2.  P2-PHASE-01                              Status: PROPOSED   (GATES.md line 973)
    3.  prerequisites                            ### Satisfied prerequisite — MICROSCOPIC PARAMETER DOMAIN        (line 1010)
                                                 ### Satisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT (line 1035)
                                                 zero occurrences of "### Unsatisfied prerequisite"
    4.  every Status: line vs the evidence base  diff empty — all 15 IDENTICAL

**All four reported. No gate, gate status, prerequisite state or verdict
changed.**

---

## 11. Superseded branches — A13, MEASURED before the advance

**Six separate exit statuses.** `git merge-base --is-ancestor <commit> HEAD`
against commit 3; **exit 1 means NOT an ancestor, the required result.**

    52f65117   exit 1      ebd531ab   exit 1      40168469   exit 1
    7146a093   exit 1      10c260b9   exit 1      d64cd912   exit 1

**No superseded-register entry was written; nothing is superseded by this
task.** **The six statuses after the advance are post-report evidence.**

---

## 12. The suite — A10, MEASURED at the merged head

    before, at the evidence base 88ef5eec…      280 passed, 2 deselected
    after,  at the merged head 22bfa684…        301 passed, 2 deselected     exit 0

    delta   +21 passed,  deselected unchanged at 2

**`tests/test_gate_pins.py` was COLLECTED — confirmed, not inferred:**
`python -m pytest --collect-only -q` lists **11 node ids** under that path,
and running the file alone reports `11 passed`.

**What accounts for the +21:**

    tests/test_gate_pins.py       new file, collected          +11
    tests/test_task_checker.py    42 -> 52 test functions      +10
                                                               ----
                                                               +21

**A delta that did not include `tests/test_gate_pins.py` would have meant the
file landed without being run** — which is the shape of failure this whole
line has been chasing. It was collected and it ran.

---

## 13. The checker — A14, MEASURED at commit 3

    base   88ef5eec08ab269eddcea8c617cf4f5b09b7336e
    head   22bfa68441b537c24533db18b053ee07b3dc6547   (commit 3, the merge commit — NOT commit 4)

**Both prospectivity readings for each of the two runs, so four invocations.
All four exited 0 with `overall: PASS`.**

    run 1 INCLUSIVE   exit 0   PASS   sha256 3c4db60ad0e1f603ecf405c6251fc35edbf6be0e8931b853edb85858ad26e5a4
    run 1 EXCLUSIVE   exit 0   PASS   sha256 7e546b6aaaf52c0aea01c7c6d2ea2afe89602d7d4d4ebc5f5034e17d06335598
    run 2 INCLUSIVE   exit 0   PASS   sha256 eb25b678f5e17ff90469af88a7db27be270d7326414a7a6954cd90984169bd9f
    run 2 EXCLUSIVE   exit 0   PASS   sha256 0e79150ec8e42060e06b807ccec508709e4055b18eb77095fd609b671b18d872

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 PASS
    P6 PASS   P7 PASS   P8 PASS   P9 PASS

### 13.1 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "88ef5eec08ab269eddcea8c617cf4f5b09b7336e",
      "head": "22bfa68441b537c24533db18b053ee07b3dc6547",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 13.2 RUN 2 config, verbatim — stop-governing

    {
      "base": "88ef5eec08ab269eddcea8c617cf4f5b09b7336e",
      "head": "22bfa68441b537c24533db18b053ee07b3dc6547",
      "specification_paths": ["specs/2026-08-14T0511Z_integrate-p7-repair.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I supplied of my own choosing; all are
taken from A14.** **`append_only_paths` is `["DECISION_LOG.md"]` and not
`[]`**, so `P3` is live. **`authorised_modified_gates` is `[]`, and here that
is truthful: no gate may change in this task.** **The config was never
adjusted to make RUN 2 pass; it passed on its first invocation.**

### 13.3 The measured RUN 1 subject set — two specifications, where RUN 2 names one

**RUN 1's default selection chose TWO**, because the merge brings the source
task's specification into the range:

    specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md   "stated: 4 additions, 3 modifications"   counted 7   stated 7    OK
    specs/2026-08-14T0511Z_integrate-p7-repair.md           "stated: 7 additions, 3 modifications"   counted 10  stated 10   OK

**RUN 2 names only the second**, as A14 requires. **This is a real difference
and not a formatting one, so both JSON outputs are given verbatim below.**
**RUN 1 additionally re-checks the arriving task's own manifest and finds it
consistent** — an observation, and RUN 1 governs nothing.

**The two prospectivity readings differ in exactly one line and in no
verdict**, for each run:

    286c286
    <         "inclusivity": "INCLUSIVE",
    ---
    >         "inclusivity": "EXCLUSIVE",

**A note on `P1`'s figures so they are not misread.** `P1` as landed reports
`counted 10 / stated 10` for a manifest declaring *"7 additions, 3
modifications"* — it totals the manifest's paths rather than comparing per
category. **That is the pre-repair `P1` behaviour and this task does not
touch it**; the per-category repair is `governance/p1-declared-total`'s, whose
`A10` is undischarged and stays with it. **Ten is A5's own count of its
manifest**, and the seven counted for the source specification is likewise
4 + 3.

### 13.4 `P7`, running the repair it is integrating

**MEASURED — the section count `P7` saw, identical in all four
invocations:**

    raw_heading_count_base   14        section_count_base   14
    raw_heading_count_head   14        section_count_head   14
    unauthorised_changed     []        added_sections  []    removed_sections  []
    authorised_modified      []

**`PASS` at fourteen sections, which A14 names as the expected result.**
**`PASS` at zero would have been a STOP.** **This is `P7` evaluating the
range that lands its own repair, and it reports a real number.**

**What the `PASS` means, and no more:** the range modifies no gate, and
fourteen parsed sections equal fourteen raw headings at base and at head.
**`P7` stays `PARTIAL`. It still does not establish which gate sections were
authorised to change.**

### 13.5 RUN 1 output, verbatim

    {
      "base": "88ef5eec08ab269eddcea8c617cf4f5b09b7336e",
      "commits_in_range": 8,
      "commits_on_first_parent_line": 3,
      "head": "22bfa68441b537c24533db18b053ee07b3dc6547",
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
            },
            {
              "counted": 10,
              "counted_set": [
                "reports/2026-08-14T0325Z_p7-repair-and-pin-validator.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-p7-repair.md",
                "reviews/chatgpt/2026-08-14T0325Z_p7-repair-and-pin-validator.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-p7-repair.md",
                "specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-p7-repair.md",
                "tests/test_gate_pins.py",
                "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                "scripts/governance_tools/task_checker.py",
                "tests/test_task_checker.py"
              ],
              "governing_sentence": "stated: 7 additions, 3 modifications",
              "parse": "OK",
              "path": "specs/2026-08-14T0511Z_integrate-p7-repair.md",
              "stated": 10
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
                "commit": "56c094c68861c5c3467cdc4786eb2811693c9c7f",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "5354b63e954b1d6a9d1959e06c700a432447a6cb",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "22bfa68441b537c24533db18b053ee07b3dc6547",
                "work_paths": [
                  "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                  "scripts/governance_tools/task_checker.py",
                  "tests/test_gate_pins.py",
                  "tests/test_task_checker.py"
                ]
              }
            ],
            "first_review_commit": "5354b63e954b1d6a9d1959e06c700a432447a6cb",
            "first_work_commit": "22bfa68441b537c24533db18b053ee07b3dc6547",
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
          "evidence": [
            {
              "compared_to_recorded": "UNAVAILABLE",
              "merge": "22bfa68441b537c24533db18b053ee07b3dc6547",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "88ef5eec08ab269eddcea8c617cf4f5b09b7336e",
              "recomputed_parent_1": "5354b63e954b1d6a9d1959e06c700a432447a6cb",
              "recomputed_parent_2": "7102a60ef249da04e2ad3326a3b8135b688aa065",
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
              "commit": "56c094c68861c5c3467cdc4786eb2811693c9c7f",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "5354b63e954b1d6a9d1959e06c700a432447a6cb",
              "matches": [],
              "status": "PASS"
            },
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
            },
            {
              "commit": "7102a60ef249da04e2ad3326a3b8135b688aa065",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "22bfa68441b537c24533db18b053ee07b3dc6547",
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
            "first_commit": "56c094c68861c5c3467cdc4786eb2811693c9c7f",
            "first_commit_paths": [
              "specs/2026-08-14T0511Z_integrate-p7-repair.md"
            ],
            "reports_added": [
              "reports/2026-08-14T0325Z_p7-repair-and-pin-validator.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-14T0511Z_integrate-p7-repair.md",
              "reviews/chatgpt/2026-08-14T0325Z_p7-repair-and-pin-validator.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-14T0511Z_integrate-p7-repair.md",
              "specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md"
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
              "path": "reports/2026-08-14T0325Z_p7-repair-and-pin-validator.md",
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

### 13.6 RUN 2 output, verbatim

    {
      "base": "88ef5eec08ab269eddcea8c617cf4f5b09b7336e",
      "commits_in_range": 8,
      "commits_on_first_parent_line": 3,
      "head": "22bfa68441b537c24533db18b053ee07b3dc6547",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that its path count matches the count in the sentence the grammar selects as governing; a specification whose text does not admit the parse is reported NOT_PARSEABLE, which is not a pass.",
          "evidence": [
            {
              "counted": 10,
              "counted_set": [
                "reports/2026-08-14T0325Z_p7-repair-and-pin-validator.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-p7-repair.md",
                "reviews/chatgpt/2026-08-14T0325Z_p7-repair-and-pin-validator.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-p7-repair.md",
                "specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-p7-repair.md",
                "tests/test_gate_pins.py",
                "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                "scripts/governance_tools/task_checker.py",
                "tests/test_task_checker.py"
              ],
              "governing_sentence": "stated: 7 additions, 3 modifications",
              "parse": "OK",
              "path": "specs/2026-08-14T0511Z_integrate-p7-repair.md",
              "stated": 10
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
                "commit": "56c094c68861c5c3467cdc4786eb2811693c9c7f",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "5354b63e954b1d6a9d1959e06c700a432447a6cb",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "22bfa68441b537c24533db18b053ee07b3dc6547",
                "work_paths": [
                  "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                  "scripts/governance_tools/task_checker.py",
                  "tests/test_gate_pins.py",
                  "tests/test_task_checker.py"
                ]
              }
            ],
            "first_review_commit": "5354b63e954b1d6a9d1959e06c700a432447a6cb",
            "first_work_commit": "22bfa68441b537c24533db18b053ee07b3dc6547",
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
          "evidence": [
            {
              "compared_to_recorded": "UNAVAILABLE",
              "merge": "22bfa68441b537c24533db18b053ee07b3dc6547",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "88ef5eec08ab269eddcea8c617cf4f5b09b7336e",
              "recomputed_parent_1": "5354b63e954b1d6a9d1959e06c700a432447a6cb",
              "recomputed_parent_2": "7102a60ef249da04e2ad3326a3b8135b688aa065",
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
              "commit": "56c094c68861c5c3467cdc4786eb2811693c9c7f",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "5354b63e954b1d6a9d1959e06c700a432447a6cb",
              "matches": [],
              "status": "PASS"
            },
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
            },
            {
              "commit": "7102a60ef249da04e2ad3326a3b8135b688aa065",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "22bfa68441b537c24533db18b053ee07b3dc6547",
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
            "first_commit": "56c094c68861c5c3467cdc4786eb2811693c9c7f",
            "first_commit_paths": [
              "specs/2026-08-14T0511Z_integrate-p7-repair.md"
            ],
            "reports_added": [
              "reports/2026-08-14T0325Z_p7-repair-and-pin-validator.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-14T0511Z_integrate-p7-repair.md",
              "reviews/chatgpt/2026-08-14T0325Z_p7-repair-and-pin-validator.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-14T0511Z_integrate-p7-repair.md",
              "specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md"
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
              "path": "reports/2026-08-14T0325Z_p7-repair-and-pin-validator.md",
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

## 14. Commits — A15, MEASURED for commits 1–3

    commit 1   56c094c68861c5c3467cdc4786eb2811693c9c7f   specs/2026-08-14T0511Z_integrate-p7-repair.md
    commit 2   5354b63e954b1d6a9d1959e06c700a432447a6cb   reviews/chatgpt/2026-08-14T0511Z_integrate-p7-repair.md
    commit 3   22bfa68441b537c24533db18b053ee07b3dc6547   --no-ff merge of 7102a60e…

    UTC token fixed by commit 1:  0511Z        day at execution: 14
    full stamp:                   2026-08-14T0511Z

**Stored subjects, MEASURED:**

    commit 1   spec: integrate the P7 repair and the pin validator, and land it
    commit 2   review: pre-execution review for the P7 repair integration
    commit 3   merge: integrate the P7 repair and the pin validator

| Commit | `Co-Authored-By` | session id or URL | tool attribution | Trailer suppressed? |
|---|---|---|---|---|
| 1 | none | none | none | **No — none was ever written** |
| 2 | none | none | none | **No — none was ever written** |
| 3 | none | none | none | **No — none was ever written** |

**Commit 4's message, INTENDED:**

    report: the P7 repair and the pin validator land on main

**Commit 4 is post-report evidence. Nothing in this report measures it.**

### 14.1 Did my harness attempt a forbidden trailer?

**Yes as a standing instruction, no in what was committed.** The guidance is
live in this session. **Each message was composed without the trailers at
first writing**, the proposed text inspected before each commit and the
stored text after. **No commit was amended and no history was rewritten.**
`P6` reports `PASS` on all three commits in every one of the four checker
invocations. **The ratification recorded for a past unpushed amend confers
nothing here and was not relied on.**

### 14.2 §8's prohibition, checked mechanically

**§8 forbids claiming in the report or the commit messages that `P1` and
`P7` are order-independent.** **MEASURED:** searching every commit message in
`88ef5eec..HEAD` for `order.independen` returns four hits, **and all four are
denials**, quoted here so the check is auditable rather than asserted:

    commit 3 (this task's merge)
      "Nothing in this merge supports any claim that P1 and P7 are order-independent."
    commit 2 (this task's review)
      "…establish textual merge cleanliness only, do not establish semantic
       order-independence, and do not discharge that branch's A10."
    arriving, source commit 2
      "…does not infer that the completed P1 and P7 branches are conflict-free or
       order-independent; integration must measure all three shared files."
    arriving, source commit 1
      "…explicitly does not claim the two branches are order-independent…"

**No affirmative claim exists in any commit message in the range, and none
appears in this report.**

---

## 15. `F1` and `F2` — met, reported, unrepaired

**`F1` — the harness conflicts with `P6` structurally.** **Met: the guidance
is live in my session now.** It is caught only because each specification
remembers to write a hygiene criterion and because I wrote against it by
hand. **Reported. Not fixed.**

**`F2` — `scripts/p2_phase01_scalar_exploratory.py` line 73 reads
`for the frozen Wilson D`.** **Met and confirmed still present at the merged
head:**

    73:        """Return ``I0(Mhat)`` and ``d I0 / d Mhat`` for the frozen Wilson D."""

    git diff --name-only 88ef5eec HEAD -- scripts/p2_phase01_scalar_exploratory.py    ->    0 paths

**Reported. Not fixed.**

---

## 16. Rule 16 assessment — all three junctions

### 16.1 First — two checks work; governance is not enforced

**After this lands, `P7` reports a real number and a pin validator runs on
every suite invocation. A reader may take that for governance being enforced.
It is not.**

**Where a reader meets that, named as locations on `main` after this merge,
not as a general caution:**

- **`derivations/GOVERNANCE-ENFORCEMENT_classification.md` §5, "The count
  that matters"** — *"Two of twenty-nine objects are mechanical, and one of
  those only in part. Five more have a necessary condition behind them.
  Twenty-two have no machine behind them at all."* **That section is
  byte-identical before and after this merge**, deliberately: nothing this
  line did changes the count.
- **The same file's `P7` row and limitation**, which state that `P7` remains
  `PARTIAL` and that the authorised-set discovery problem is untouched.
- **The new VALIDATOR subsection**, which states that validators are not
  among the nine and must never be numbered among them.
- **`reports/2026-08-14T0325Z_p7-repair-and-pin-validator.md` §14.1**, the
  source task's own first junction.

**Two checks now work. That is the whole claim, and it is the whole of it.**

### 16.2 Second — two gate-heading grammars now coexist, and nothing keeps them agreeing

**This is the finding worth carrying forward.** The source task discovered
that `tests/test_repository_structure.py` **already contained a working
gate-heading pattern with a non-empty guard**, at the same revision as the
broken parser, **and nothing had ever compared them.**

**After this merge the repository holds two, MEASURED at the merged head:**

    scripts/governance_tools/task_checker.py:497
      ^## (P2-[A-Z0-9-]+)[ \t]+[—–-][ \t]+\S.*$          -> 14 ids

    tests/test_repository_structure.py:154
      ^##\s+(P2-[A-Z]+(?:-[A-Z]+)*-\d+)                   -> 14 ids

    agree today                : True
    symmetric difference       : empty

**They agree today. Nothing keeps them agreeing**, and they are not even the
same language: the checker's requires a separator and a title and accepts
digits inside the id; the structure test's requires the id to end in
`-<digits>` and ignores whatever follows. **A gate id like `P2-FOO2-01` parses
under one and not the other**, and no test compares their outputs.

**I did not unify them and did not add the invariant test**, as §2 and §7
require. **The unification, or a test asserting both return the same id set,
belongs to the conventions task.**

### 16.3 Third — what would detect the pin validator going vacuous

**Nothing currently does.** **`test_pin_set_is_not_empty` is a guard of
exactly the kind it exists to enforce, written by the same hand**, and it
would fail in the way `P7` failed: **if the pin notation in `GATES.md`
drifted so that the `PIN` pattern stopped matching, the non-empty assertion is
the thing that would fire** — which is why it exists, and is precisely not an
independent check.

**What would detect it, named and NOT built here:**

1. **An expected-count assertion with the number written down** — "`GATES.md`
   contains exactly N pins" — failing when the count moves in either
   direction rather than only at zero. Every legitimate pin addition would
   edit a test; **that cost is the point**, making the count declared rather
   than discovered.
2. **A standing mutation check** running the validator against a known-stale
   fixture and asserting it fails. The source task's runs (ii)–(iv) are that
   observation performed once by hand in a report; **they are not a test that
   runs.**
3. **A cross-check between two independently written pin locators**, on the
   same principle as `RAW_GATE_HEADING` versus `GATE_HEADING` — agreement
   between two patterns nobody wrote to match each other.

**None is built here.** **The regress is real:** every guard available to me
is a guard written by me, and only a second pair of eyes or a signal from
outside the file breaks it.

---

## 17. Does `main` now read as though governance were enforced?

**No, and the honest answer needs the qualification that follows.**

**MEASURED at the merged head:** no file on `main` states that governance is
enforced; the classification's §5 count of **twenty-two of twenty-nine
objects with no machine behind them is byte-identical** to its value before
this merge; and `P7`'s row still reads `PARTIAL`.

**Where the residual risk actually lies, stated plainly.** **The suite now
returns a larger green number — 301 rather than 280 — and a larger green
number is exactly what a reader mistakes for more assurance.** The count rose
because two checks were added, **not because more of the repository is
covered.** A reader who sees `301 passed` and `P7 PASS` without opening the
classification will over-read both.

**The mitigation on `main` is that the classification says so in four places
(§16.1), including one this merge adds.** **It is not a mechanism.** Nothing
prevents the misreading; the document merely contradicts it for anyone who
reads it.

---

## 18. The landing — INTENDED at the time of writing

**This task ends with authoritative `main` at its own final report commit,
named as commit 4 and not as a SHA**, because any SHA naming a commit that
carries this task's review is unreachable as a landing target under Rule 15.

**§5's two landing preconditions are already MEASURED and both are met:** A8
reports fourteen parsed of fourteen raw (§9), and A10 reports a risen count
of 301 including `tests/test_gate_pins.py` (§12). **A landing that carried
the files without the behaviour is the failure mode this line has been
chasing, and it did not occur.**

**INTENDED, and measured only as post-report evidence:** the pre-advance
`--is-ancestor` exit status; a fast-forward push **without `--force` and
without `--force-with-lease`**; `governance/p7-repair-and-pin-validator`
neither deleted nor moved, its tip verified after the advance;
`governance/p1-declared-total` confirmed unchanged at `8ff032e7…`; A9, A10 and
A13 re-run after the advance; A14-final before the landing, **which stops the
advance if it fails.**

**Nothing in this report claims the landing has happened.**

---

## 19. Stops and clarifications

### 19.1 Stops

**None.** No stop was reached in any of the five primary categories:
`SPECIFICATION_DEFECT`, `ENVIRONMENT`, `OBSERVATION_METHOD_ERROR`,
`REPOSITORY_DEFECT`, `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`.

**Every stop condition the specification names was tested and none
triggered:** A1's three refs matched; A2's review names the executed digest;
A4's conflict list is empty; A7 shows `GATES.md` byte-identical; A8 reports
fourteen parsed, not zero; A14's RUN 2 exited 0 with `P7` at fourteen
sections; §5's two landing preconditions are met.

### 19.2 Secondary findings

**F1 and F2 arrive unrepaired and are reported in §15.** Beyond those:

**S1 — carried forward from the source task, now a property of `main`.** Two
gate-heading grammars coexist and nothing keeps them agreeing (§16.2).
**MEASURED as agreeing today with an empty symmetric difference.** **Not
unified here, as §2 requires.**

**S2 — observation, not a defect.** `P1` totals a manifest's paths rather
than comparing per category, so it reports `10 / 10` for a specification
declaring "7 additions, 3 modifications" (§13.3). **Pre-repair behaviour,
untouched here, and the repair stays with `governance/p1-declared-total`.**

**S3 — observation, agreeing with the review.** The review's non-blocking
note on §0's *"Two checks that work, and one that did not"* is fair; the
third row of that table is the same `P7` whose old behaviour "did not". **It
changed nothing in execution.**

**S4 — recorded because §1a asks whoever integrates `P1` to have it.** This
task merged three files that `governance/p1-declared-total` also
modifies — `scripts/governance_tools/task_checker.py`,
`tests/test_task_checker.py` and
`derivations/GOVERNANCE-ENFORCEMENT_classification.md`. **`main` after this
task carries the `P7` side of all three.** **Nothing in this report supports
any claim about integration order**, and the `P1` integration must measure
merged behaviour, at minimum running the full suite at its merged head and
confirming `P7` still reports fourteen of fourteen. **I did not perform that
measurement and this task does not authorise skipping it.**

### 19.3 Ambiguous, unsatisfiable, or what I would have specified differently

**Nothing was unsatisfiable, and no instruction was inconsistent with a
repository rule.** Three observations:

1. **A6's arithmetic is the clearest version of this criterion so far, and
   the spelling-out was warranted.** 6, 7 and 9 are three different figures
   and I derived the seven **from the source branch** rather than from the
   specification's list, so the comparison could have caught a mismatch
   between them. It did not — they agree.
2. **A11 says "every path existing at the evidence base other than the three
   in A5's `modify:` list".** I read the exclusion as applying to those three
   paths only and compared the other 373, reporting the arithmetic
   (376 − 3 = 373). **The three excluded are precisely the authorised
   modifications, so nothing was excluded that a reader would expect
   checked.**
3. **A9 says "unchanged from the evidence base" for the pins.** I established
   that from §8 — `GATES.md` blob-identical means the declared values cannot
   have moved — plus A11 showing both pinned artifacts unchanged, rather than
   re-hashing at the base. **Both routes reach the same conclusion; I state
   which one I took.**

### 19.4 Rule 13

**No environment failure occurred, so neither of Rule 13's two diagnostic
orders was exercised.** **Rule 13 carrying two such orders remains a known
open item; I name neither as the one that applies.**

    Python   3.11.15
    pytest   9.1.1

**Nothing was installed.**

---

## 20. Evidence layering

**Committed in this report, MEASURED at commit 3:** A1–A13 and A15 for
commits 1–3; A14's four invocations with both configs and both JSON outputs;
commits 1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; A5's final
base-to-head scope of 7 additions and 3 modifications.

**Post-report evidence, returned to the Reviewer and NOT written back:** A5's
final scope measured base-to-commit-4; A14-final, being RUN 2 re-run at commit
4 before the landing; A9, A10 and A13 re-run after the advance; A15 for commit
4; the pre-advance `--is-ancestor` exit status; the exact push command; remote
`main` read back; the source tip unchanged; `governance/p1-declared-total`
confirmed unchanged; final ancestry confirmation.

**Nothing in this report claims to measure commit 4.**
