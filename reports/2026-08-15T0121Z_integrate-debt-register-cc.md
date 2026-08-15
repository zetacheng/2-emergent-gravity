# Execution report — integrate the governance debt register, and land it

**Specification:** `specs/2026-08-15T0121Z_integrate-debt-register-cc.md`
**Specification evidence base:** `80595d4cd575d1d024d1415b9b599947bf847677`
**Branch:** `governance/integrate-debt-register-cc`, cut from authoritative `main` @ `80595d4c…`
**Source merged:** `governance/debt-register-cc` @ `023b8b026d8e2040ae818e93e3630e85dee999e3`
**Classification:** MATERIAL. Governed by Rule 15, Rule 18, and **Amendments M–P and Rules 19–21.**

**Every figure below is labelled MEASURED or INTENDED.** **This report is
written at commit 3, the merge commit, and measures nothing at commit 4.**

---

## 1. Outcome

**One merge, clean. Nothing auto-merged. Nothing edited.**

**MEASURED at commit 3:** empty conflict list; merge-base `80595d4c…`; 6
additions and 1 modification; all five arriving paths blob-identical to the
source tip in the **one-sided** case, which §5 establishes before interpreting
them; `CONVENTIONS.md` grows by 2 lines and loses 0, with the base an exact
in-order subsequence at 1405 of 1405; 400 of 400 other paths blob-identical;
the register intact at eleven entries with the dispositions §0 names;
validators unchanged at 324 passed, 2 deselected; all four checker invocations
exit 0 with `overall: PASS` and `P7` reading fourteen sections.

**The planned `C-a` / `C-b` / `C-c` sequence completes with this landing.**
**That is a plan completing, and not governance work completing.** §16 gives
the disposition counts beside that statement, as §7 requires.

---

## 2. Refs — A1

**MEASURED, against `origin` after a fetch:**

    refs/heads/main                      80595d4cd575d1d024d1415b9b599947bf847677
    governance/debt-register-cc          023b8b026d8e2040ae818e93e3630e85dee999e3

**Both match the specification. No mismatch, no STOP.**

**As recorded in the `C-c` report, this container's local `refs/heads/main` is
stale** at `0f79617…`, a strict ancestor of the authoritative `main`. **No
measurement in this report reads it**; every measurement names an explicit SHA
or `origin/main`. **A1 is satisfied against the authoritative ref**, read with
`git ls-remote`.

---

## 3. The review binds to these bytes — A2

**MEASURED.**

    SHA-256 of the arriving specification         e99e39a53e0222d1ba8a3e065b3968e48408508e341b0d3d0a175ea365d3d8f1
    SHA-256 the review records as reviewed        e99e39a53e0222d1ba8a3e065b3968e48408508e341b0d3d0a175ea365d3d8f1

**Equal.** The digest field is filled in and names this specification.
**Both arriving files were committed byte-identical**, verified by `cmp`.
**Neither was modified.**

The review's verdict is **APPROVED FOR EXECUTION AND LANDING**. It records
that the Rule 20 ambiguity and the revision-attribution requirement were both
corrected before issue, and it directs that completion be read as the planned
`C-a`/`C-b`/`C-c` sequence and **not** as closure of the governance gap. **§16
uses the specification's narrower formulation.**

---

## 4. Merge parentage — A3

**Three values, separately derived. MEASURED:**

    parent 1          7092d289770c1fe90440a6d001f58577e4fec5a8
    parent 2          023b8b026d8e2040ae818e93e3630e85dee999e3
    merge-base(1,2)   80595d4cd575d1d024d1415b9b599947bf847677

**Each equals what A3 requires:** parent 1 is this task's review commit
(commit 2), parent 2 is the pinned source tip, and the merge-base is the
evidence base.

**The merge-base is NOT parent 1**, because parent 1 already carries this
task's specification and review — two commits made after the base on this
branch. **The merge-base is `main` itself.**

**MEASURED: commit 1 is an ancestor of parent 1** — `--is-ancestor` exit 0.
So the specification precedes the review, which precedes the merge, which is
Rule 15's timing clause.

### 4.1 No conflict — A4

**MEASURED: the conflict list is empty.** `git diff --diff-filter=U`
returns nothing and the index carries **0** unmerged entries.

**MEASURED: no `Auto-merging` line was emitted.** Nothing was
content-merged, so Amendment `P(b)`'s line-survival check has no auto-merge to
verify here; §6 gives the reason from the merge case, and §7 runs the
subsequence measurement regardless.

---

## 5. Which merge case, established BEFORE any blob comparison — A7

**A blob comparison reported without its case is uninterpretable, so the case
comes first.**

**MEASURED:**

    merge-base(parent 1, parent 2)          80595d4cd575d1d024d1415b9b599947bf847677
    authoritative main tip                  80595d4cd575d1d024d1415b9b599947bf847677
    commits on main after the base          0
    commits on main touching CONVENTIONS.md 0

**The merge-base IS `main`.** No commit exists on `main` after the source was
cut, so `main` has not touched `CONVENTIONS.md` — or anything else — since.

**THE CASE IS ONE-SIDED: only the source changed the modified path.**

**Therefore a merged blob equal to the source side is the CORRECT outcome**,
and is not evidence that a side was lost. **In the two-sided case the same
measurement would mean the opposite**, and Amendment `P(b)`'s line-survival
measurement would have been required instead of blob equality. **It is not
required here**, and I did not substitute one for the other.

### 5.1 The blob comparison, now interpretable

**MEASURED, source tip against the merge commit:**

    CONVENTIONS.md                                        8badc51f38d8   IDENTICAL
    docs/GOVERNANCE-DEBT.md                               b77e961d49c2   IDENTICAL
    reports/2026-08-15T0008Z_debt-register-cc.md          ab4b4baa6a66   IDENTICAL
    reviews/chatgpt/2026-08-15T0008Z_debt-register-cc.md  dd6e37b128be   IDENTICAL
    specs/2026-08-15T0008Z_debt-register-cc.md            e6b7dfec1c98   IDENTICAL

**All five arriving paths are blob-identical to the source tip.** **Nothing
arriving by merge was edited**, and in the one-sided case that is what
correctness looks like.

---

## 6. Scope — A5 and A6

### 6.1 A6, derived from the SOURCE and not from A5

**MEASURED, `80595d4c…` to `023b8b02…`, computed from the source branch
alone:**

    M  CONVENTIONS.md
    A  docs/GOVERNANCE-DEBT.md
    A  reports/2026-08-15T0008Z_debt-register-cc.md
    A  reviews/chatgpt/2026-08-15T0008Z_debt-register-cc.md
    A  specs/2026-08-15T0008Z_debt-register-cc.md

    4 additions, 1 modification

**This agrees with A5's decomposition**, which attributes 4 additions and 1
modification to the source and 3 additions to this task. **No disagreement to
report.**

### 6.2 A5, and the head each figure was measured at

**MEASURED at commit 3, the merge commit:**

    M  CONVENTIONS.md
    A  docs/GOVERNANCE-DEBT.md
    A  reports/2026-08-15T0008Z_debt-register-cc.md
    A  reviews/chatgpt/2026-08-15T0008Z_debt-register-cc.md
    A  reviews/chatgpt/2026-08-15T0121Z_integrate-debt-register-cc.md
    A  specs/2026-08-15T0008Z_debt-register-cc.md
    A  specs/2026-08-15T0121Z_integrate-debt-register-cc.md

    6 additions, 1 modification      <- MEASURED, head = commit 3

**INTENDED, head = commit 4:** 7 additions and 1 modification, the seventh
addition being this report at
`reports/2026-08-15T0121Z_integrate-debt-register-cc.md`. **That figure is
INTENDED, not MEASURED: this report is written before the commit containing
it.**

**The decomposition, MEASURED where it can be:**

    source      4 additions + 1 modification = 5     MEASURED (§6.1)
    this task   3 additions                  = 3     2 MEASURED, 1 INTENDED
    total       7 additions + 1 modification = 8     INTENDED at commit 4

**MEASURED: no status code other than `A` or `M` appears** — no delete,
rename, copy, type change, unmerged or unknown, which is the manifest's
`forbidden_operations` list.

---

## 7. `CONVENTIONS.md` grows by addition only — A8

**MEASURED, base to commit 3:**

    added lines      2
    deleted lines    0
    hunks            1

**The whole change:**

    @@ -1402,3 +1402,5 @@
      were found only because a later task tripped over them. **A list assembled by
      noticing is not a survey**, and the absence of a rule here is not evidence
      that the corresponding failure cannot occur.
    +
    +**Governance debt is registered in `docs/GOVERNANCE-DEBT.md`** — an eleven-entry record of the known governance debt, each entry with its disposition and where its evidence sits. Nothing in that file binds either.

### 7.1 The subsequence check, run independently

**A8 calls these two independent measurements of one property, neither
substituting for the other. Both were run.**

**MEASURED**, by walking the merged file once and advancing a pointer into the
base file on each equal line:

    base lines          1405
    head lines          1407
    matched in order    1405
    exact subsequence   True

**1405 of 1405, as A8 expects.** Every line of the base survives, in order.
**Nothing was reflowed, reworded or reordered**, which a zero-deletion count
alone would not have established.

### 7.2 Rules and amendments, unchanged

**MEASURED at base and at commit 3:**

    numbered rules        21    21
    amendment letters     15    15
    Amendment J present    0     0

**Twenty-one rules, fifteen amendment letters `A`–`P` with no `J`, identical
at both** — **because the source adds neither**, and this task adds neither.

---

## 8. The register is intact and non-binding — A9

**MEASURED, parsed from the file at commit 3.**

**Eleven entries, `G-01` to `G-11`:**

    G-01  the executor harness conflicts with P6                 NOT REPAIRABLE HERE
    G-02  a docstring asserts a freeze the determination rejects  REPAIRABLE
    G-03  corrections are not discoverable from what they correct OPEN
    G-04  nothing requires a new specification to carry stated:   SPECIFIABLE
    G-05  nothing compares a review's digest to the specification SPECIFIABLE
    G-06  nothing performs the auto-merge line-survival check     SPECIFIABLE
    G-07  the marker vocabulary is defined only in a record       RULED
    G-08  a criterion can assert something false about itself     OPEN
    G-09  nothing independently validates the shared grammar      OPEN
    G-10  nothing detects a guard going vacuous                   OPEN
    G-11  a probe contradicting a check is likelier to be wrong   METHOD NOTE

**Counts, MEASURED:**

    REPAIRABLE            1     G-02
    SPECIFIABLE           3     G-04  G-05  G-06
    NOT REPAIRABLE HERE   1     G-01
    RULED                 1     G-07
    METHOD NOTE           1     G-11
    OPEN                  4     G-03  G-08  G-09  G-10
    ---------------------------------------------------
    entries              11

**These match §0 entry for entry and count for count.** **MEASURED: every one
of the eleven carries exactly one disposition** — none carries two, none
carries none. **`G-09` and `G-10` are `OPEN`, not `SPECIFIABLE`**, as §0
requires.

**MEASURED: no entry reads `CLOSED`.** The string occurs on one line of the
file, and that line is the sentence stating no entry is marked `CLOSED`.

**MEASURED: the count of lines containing `MUST`, `SHALL` or `binds` is ONE**,
and it is

> **Nothing in this file binds.**

**The count does not exceed one, so there is nothing to name and justify.**

**MEASURED: nothing was added to, removed from, or re-disposed in the
register.** It is blob-identical to the source tip (§5.1), which is the
strongest form of that statement.

---

## 9. `D4` is cross-referenced, not duplicated — A10

**MEASURED:** `derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md` is
blob-identical at base and at commit 3, `cd53ec3db038fb6bfde299b75661eec4824458c1`
at both. **The C-check register was read and not touched.**

**MEASURED: `OPEN-CC-3` is in it**, at line 70 —
"the mechanism of the bit-exact mirroring is unresolved".

**MEASURED: the register points at it rather than restating it.** Its section
"Not entered here — `D4`" names `OPEN-CC-3` and the file it lives in, and
gives the reason: a second entry would create a second place for one status to
drift. **`D4` is not an entry, and the register still holds eleven.**

---

## 10. The two carried findings — A11

**Both are reported. Neither is registered. The register remains at eleven
entries, MEASURED in §8.**

### 10.1 The revision-attribution error, three figures at three revisions

**MEASURED independently at each revision, by counting `.md` files under
`specs/` and those carrying a `stated:` record:**

    bec01171    13 of 50
    f179b45e    15 of 52
    80595d4c    17 of 54

**These are three figures at three different revisions, and they are not three
figures at this evidence base.** Only the last belongs to `80595d4c…`.

**The `C-c` specification stated `13 of 50` for `f179b45e…`. The number was
right and the anchor was wrong** — 13 of 50 is exact at `bec01171…`, one
landing earlier, and `f179b45e…` carries 15 of 52.

**The `C-c` executor did not take the specification's figure as true.** It
re-measured, found the mismatch, verified its own probe before contradicting a
written figure, and corrected the attribution in both its report and the
register entry. **That is the behaviour `A5` of that task was written to
produce, and it worked.**

**This correction is reported and NOT registered.**

### 10.2 The classification artifact is absent from the repository

**`C-a` and `C-c` both cite the governance debt classification —
`1c65e68c0263b1fcfab24d260d81409a4cd687139c4f106e0a8112fb346d61d9` — as the
source of the `C1`–`C5` and `D1`–`D4` identifiers.** **MEASURED: no file in
the tree at the evidence base has that digest, at any path.**

**So a reader of `main` can see the debt identifiers referenced and cannot
reconstruct their authoritative definitions.** **This is a provenance gap and
not a discoverability one: the file is not merely hard to find, it is
absent.**

**Reported in the words A11 requires: this provenance gap is
`identified but not registered by this task`.**

**No twelfth entry was added, and no disposition was changed.** A later task
may register it. **This one records that it was found.**

---

## 11. Protected paths — A12

**MEASURED, path by path, base to commit 3:**

    paths at the evidence base          401
    excluded (CONVENTIONS.md)             1
    compared                            400
    blob-identical                      400
    differing                             0
    missing at head                       0

**The named ones, MEASURED individually:**

    GATES.md                                        2b3bd5069414   IDENTICAL
    DECISION_LOG.md                                 d9dd2bf3a8cc   IDENTICAL
    docs/BRANCHING_POLICY.md                        3f0f35d4da44   IDENTICAL
    derivations/P2-DEFERRED-ITEMS.md                33b3a664e057   IDENTICAL
    derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md   cd53ec3db038   IDENTICAL

**Nothing under `scripts/`, `tests/` or `results/` changed**, covered by the
400. **`GATES.md` was modified for no reason, because it was not modified at
all.**

---

## 12. Gate invariants and pins — A13

**All five, MEASURED at commit 3:**

    1.  ^## P2- count                    14
    2.  P2-PHASE-01                       Status: PROPOSED
    3.  first prerequisite                Prerequisite state: SATISFIED
    4.  second prerequisite               Prerequisite state: SATISFIED
    5.  both pins match their targets, and CONVENTIONS.md is named by neither

**The pins, MEASURED through the committed collector rather than a hand
probe:**

    line 1017   derivations/P2-PHASE-01_microscopic_parameter_domain.md    MATCH
    line 1040   derivations/P2-PHASE-01_input_admissibility_contract.md    MATCH

    CONVENTIONS.md is a pin target:  False

**`CONVENTIONS.md` is modified by this merge and is pinned by no gate**, so
**no re-pin is owed under Rule 19.** That was verified rather than assumed.
`CONVENTIONS.md` is named elsewhere in `GATES.md` as a locked-assumptions
reference; **being named is not being pinned**, and the two pins name neither
it nor anything else this merge touches.

---

## 13. The checker — A14, MEASURED at commit 3

    base   80595d4cd575d1d024d1415b9b599947bf847677
    head   0f3660afb221dfb4c877d29c3e234d3b8b9bde20   (commit 3, the merge commit)

**Both prospectivity readings for each run, so four invocations. All four
exited 0 with `overall: PASS`.**

    run 1 INCLUSIVE   exit 0   PASS   sha256 392022c45edc12f987166df484e4f7e208954bea54839cbd8ac2249153e35a12
    run 1 EXCLUSIVE   exit 0   PASS   sha256 fb888c12f9fc102721dbe1f3f87ed6404a449dcf72b9da39c7e5cde5a6b4fa1b
    run 2 INCLUSIVE   exit 0   PASS   sha256 cf2bfbaaded053808214851568b173258e2f47edfb08f82d12b12eddbce65e25
    run 2 EXCLUSIVE   exit 0   PASS   sha256 f41e45aa66d0359d6bb3fcdd512e8dce72b7d8f47e4f1307e2322932afd80d0a

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 PASS
    P6 PASS   P7 PASS   P8 PASS   P9 PASS

**Nine of nine `PASS`, in every invocation.** No property returned
`NOT_DECLARED`, `NOT_PARSEABLE` or `DECLARATION_CONFLICT`, which are the three
results that make a run INCOMPLETE.

### 13.1 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "80595d4cd575d1d024d1415b9b599947bf847677",
      "head": "0f3660afb221dfb4c877d29c3e234d3b8b9bde20",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 13.2 RUN 2 config, verbatim — stop-governing

    {
      "base": "80595d4cd575d1d024d1415b9b599947bf847677",
      "head": "0f3660afb221dfb4c877d29c3e234d3b8b9bde20",
      "specification_paths": ["specs/2026-08-15T0121Z_integrate-debt-register-cc.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I chose.** `append_only_paths`,
`authorised_modified_gates`, the boundary and `register_path` are fixed by
A14. **Neither the config nor this specification's declarations were adjusted
to make RUN 2 pass** — §8 forbids both, and neither was needed: they were
written to agree and they do.

### 13.3 The measured RUN 1 subject set

**MEASURED: RUN 1's default selection chose TWO specifications**, because the
merge brings the source task's own into the range:

    specs/2026-08-15T0008Z_debt-register-cc.md              stated add 4 modify 1   counted add 4 modify 1
    specs/2026-08-15T0121Z_integrate-debt-register-cc.md    stated add 7 modify 1   counted add 7 modify 1

**RUN 2 names only the second**, as A14 requires. **A real difference, so both
JSON outputs are given verbatim below**, rather than one standing for the
other.

The two prospectivity readings differ in exactly one line and in no verdict:
the `inclusivity` field.

### 13.4 What `P1`'s "7" counts, so it is not misread against A5's "6"

**`P1` counted 7 additions for this task's specification. §6.2 measured 6
additions at commit 3. These do not conflict, and the reason is what `P1`
checks.**

**MEASURED, `P1`'s `counted_set` for this task's specification:**

    docs/GOVERNANCE-DEBT.md
    reports/2026-08-15T0008Z_debt-register-cc.md
    reports/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md
    reviews/chatgpt/2026-08-15T0008Z_debt-register-cc.md
    reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md
    specs/2026-08-15T0008Z_debt-register-cc.md
    specs/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md
    CONVENTIONS.md

**Those are the paths the manifest block enumerates, not the paths the range
changed.** `P1`'s own `does_not_establish` says so: it establishes only that
the declared total agrees, per category, with the paths that record's block
enumerates. **`P1` compares a specification against itself. A5 compares the
repository against the specification.** **The 7 is the manifest's; the 6 is
the merge commit's**, and the two agree once this report is committed.

### 13.5 `P7`, and the section count it saw

    declared_source          specification
    declared                 []
    raw_heading_count_head   14        section_count_head   14

**`P7` reports fourteen sections, read through the shared helper. `PASS` at
zero would have been a STOP.**

### 13.6 Both declarations came from the specification

**MEASURED, identical in all four invocations:**

    P3   declared_source: specification    declared: ['DECISION_LOG.md']
    P7   declared_source: specification    declared: []

**Both properties took their set from this specification's own scope block,
not from the config.** The config supplied the same two values, so the
precedence rule resolved to `specification`. **MEASURED:
`DECLARATION_CONFLICT` appears nowhere in any of the four outputs.**

**They agree because they were written to agree.** Had they differed, `P3` and
`P7` would have returned `DECLARATION_CONFLICT`, RUN 2 would have exited
non-zero, and §8 makes that a finding and a STOP rather than something to fix
by editing either side.

### 13.7 Two files a reader might call "the register", and which is which

**Said explicitly, because after this merge `main` carries both, and the
adjacency is what produces a wrong reading later.**

**`docs/BRANCHING_POLICY.md` is the superseded-branch register.** It is what
`register_path` names in both configs, and it is what **`P4` checks** — the
record of branches that were superseded and may not be merged. **MEASURED: it
is blob-identical at base and head**, so the register `P4` reads was not
touched by this merge.

**`docs/GOVERNANCE-DEBT.md` is not that register, and this task does not make
it one.** It records governance debt. **`P4` does not read it. Nothing in the
checker reads it. It is checked by nothing**, and **its contents bind
nobody** — its own third line says so, and §8 measures that the sentence is
there.

**One is checked by `P4`; the other is checked by nothing. They share the word
"register" and nothing else.**

### 13.8 RUN 1 output, verbatim

    {
      "base": "80595d4cd575d1d024d1415b9b599947bf847677",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "0f3660afb221dfb4c877d29c3e234d3b8b9bde20",
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
              "counted": 5,
              "counted_add": 4,
              "counted_modify": 1,
              "counted_set": [
                "docs/GOVERNANCE-DEBT.md",
                "reports/2026-08-XXT{HHMM}Z_debt-register-cc.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_debt-register-cc.md",
                "specs/2026-08-XXT{HHMM}Z_debt-register-cc.md",
                "CONVENTIONS.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-15T0008Z_debt-register-cc.md",
              "stated": 5,
              "stated_add": 4,
              "stated_modify": 1,
              "stated_record": "stated: 4 additions, 1 modification"
            },
            {
              "append_only": [
                "DECISION_LOG.md"
              ],
              "authorised_gates": [],
              "counted": 8,
              "counted_add": 7,
              "counted_modify": 1,
              "counted_set": [
                "docs/GOVERNANCE-DEBT.md",
                "reports/2026-08-15T0008Z_debt-register-cc.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md",
                "reviews/chatgpt/2026-08-15T0008Z_debt-register-cc.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md",
                "specs/2026-08-15T0008Z_debt-register-cc.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md",
                "CONVENTIONS.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-15T0121Z_integrate-debt-register-cc.md",
              "stated": 8,
              "stated_add": 7,
              "stated_modify": 1,
              "stated_record": "stated: 7 additions, 1 modification"
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
                "commit": "6b4911ba1dc3853ecd216358549891781dce72e0",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "7092d289770c1fe90440a6d001f58577e4fec5a8",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "0f3660afb221dfb4c877d29c3e234d3b8b9bde20",
                "work_paths": [
                  "CONVENTIONS.md",
                  "docs/GOVERNANCE-DEBT.md"
                ]
              }
            ],
            "first_review_commit": "7092d289770c1fe90440a6d001f58577e4fec5a8",
            "first_work_commit": "0f3660afb221dfb4c877d29c3e234d3b8b9bde20",
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
              "specs/2026-08-15T0008Z_debt-register-cc.md",
              "specs/2026-08-15T0121Z_integrate-debt-register-cc.md"
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
              "merge": "0f3660afb221dfb4c877d29c3e234d3b8b9bde20",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "80595d4cd575d1d024d1415b9b599947bf847677",
              "recomputed_parent_1": "7092d289770c1fe90440a6d001f58577e4fec5a8",
              "recomputed_parent_2": "023b8b026d8e2040ae818e93e3630e85dee999e3",
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
              "commit": "6b4911ba1dc3853ecd216358549891781dce72e0",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "7092d289770c1fe90440a6d001f58577e4fec5a8",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "e69d1ca1098951741d69c0dc42e73ea32dd58ed4",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "42ab2107d1c9d63aee64c754799ca922641e47ca",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "25ef7f57a928fd1e9007605883b66a5b9a10d0d9",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "023b8b026d8e2040ae818e93e3630e85dee999e3",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "0f3660afb221dfb4c877d29c3e234d3b8b9bde20",
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
              "specs/2026-08-15T0008Z_debt-register-cc.md",
              "specs/2026-08-15T0121Z_integrate-debt-register-cc.md"
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
            "first_commit": "6b4911ba1dc3853ecd216358549891781dce72e0",
            "first_commit_paths": [
              "specs/2026-08-15T0121Z_integrate-debt-register-cc.md"
            ],
            "reports_added": [
              "reports/2026-08-15T0008Z_debt-register-cc.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-15T0121Z_integrate-debt-register-cc.md",
              "reviews/chatgpt/2026-08-15T0008Z_debt-register-cc.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-15T0121Z_integrate-debt-register-cc.md",
              "specs/2026-08-15T0008Z_debt-register-cc.md"
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
              "path": "reports/2026-08-15T0008Z_debt-register-cc.md",
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

### 13.9 RUN 2 output, verbatim

    {
      "base": "80595d4cd575d1d024d1415b9b599947bf847677",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "0f3660afb221dfb4c877d29c3e234d3b8b9bde20",
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
              "counted": 8,
              "counted_add": 7,
              "counted_modify": 1,
              "counted_set": [
                "docs/GOVERNANCE-DEBT.md",
                "reports/2026-08-15T0008Z_debt-register-cc.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md",
                "reviews/chatgpt/2026-08-15T0008Z_debt-register-cc.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md",
                "specs/2026-08-15T0008Z_debt-register-cc.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md",
                "CONVENTIONS.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-15T0121Z_integrate-debt-register-cc.md",
              "stated": 8,
              "stated_add": 7,
              "stated_modify": 1,
              "stated_record": "stated: 7 additions, 1 modification"
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
                "commit": "6b4911ba1dc3853ecd216358549891781dce72e0",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "7092d289770c1fe90440a6d001f58577e4fec5a8",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "0f3660afb221dfb4c877d29c3e234d3b8b9bde20",
                "work_paths": [
                  "CONVENTIONS.md",
                  "docs/GOVERNANCE-DEBT.md"
                ]
              }
            ],
            "first_review_commit": "7092d289770c1fe90440a6d001f58577e4fec5a8",
            "first_work_commit": "0f3660afb221dfb4c877d29c3e234d3b8b9bde20",
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
              "specs/2026-08-15T0121Z_integrate-debt-register-cc.md"
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
              "merge": "0f3660afb221dfb4c877d29c3e234d3b8b9bde20",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "80595d4cd575d1d024d1415b9b599947bf847677",
              "recomputed_parent_1": "7092d289770c1fe90440a6d001f58577e4fec5a8",
              "recomputed_parent_2": "023b8b026d8e2040ae818e93e3630e85dee999e3",
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
              "commit": "6b4911ba1dc3853ecd216358549891781dce72e0",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "7092d289770c1fe90440a6d001f58577e4fec5a8",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "e69d1ca1098951741d69c0dc42e73ea32dd58ed4",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "42ab2107d1c9d63aee64c754799ca922641e47ca",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "25ef7f57a928fd1e9007605883b66a5b9a10d0d9",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "023b8b026d8e2040ae818e93e3630e85dee999e3",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "0f3660afb221dfb4c877d29c3e234d3b8b9bde20",
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
              "specs/2026-08-15T0121Z_integrate-debt-register-cc.md"
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
            "first_commit": "6b4911ba1dc3853ecd216358549891781dce72e0",
            "first_commit_paths": [
              "specs/2026-08-15T0121Z_integrate-debt-register-cc.md"
            ],
            "reports_added": [
              "reports/2026-08-15T0008Z_debt-register-cc.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-15T0121Z_integrate-debt-register-cc.md",
              "reviews/chatgpt/2026-08-15T0008Z_debt-register-cc.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-15T0121Z_integrate-debt-register-cc.md",
              "specs/2026-08-15T0008Z_debt-register-cc.md"
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
              "path": "reports/2026-08-15T0008Z_debt-register-cc.md",
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

## 14. Validators — A15

**MEASURED, `python -m pytest` from the repository root, exit status 0 both
times:**

    before, at the base 80595d4c      324 passed, 2 deselected
    after,  at commit 3               324 passed, 2 deselected

**Unchanged, and expected to be: neither the source nor this task adds a
test.** **No change to explain.**

The "before" figure was measured in a separate worktree checked out at the
evidence base, not quoted from an earlier report.

---

## 15. Superseded branches, and commit-message hygiene — A16, A17

**A16, MEASURED before the advance. Six separate exit statuses, all 1 —
not merged:**

    52f65117  exit 1        7146a093  exit 1
    ebd531ab  exit 1        10c260b9  exit 1
    40168469  exit 1        d64cd912  exit 1

**A17, MEASURED on commits 1–3. Commit 4 is post-report evidence.**

    commit 1   6b4911ba   spec: integrate the governance debt register, and land it
               trailer hits 0      not amended
    commit 2   7092d289   review: pre-execution review for the debt-register integration
               trailer hits 0      not amended
    commit 3   0f3660af   merge: integrate the governance debt register
               trailer hits 0      not amended

**MEASURED over the whole range: a scan for `Co-Authored-By`,
`claude.ai/code`, `Generated with`, `Claude-Session` and `noreply@anthropic`
returns nothing.**

**Rule 20 binds this task and was NOT exercised.** No commit was written with
a hygiene violation to repair, so no amend was needed. **`P6` passed on the
first attempt in all four invocations.** **No force-push, no branch deletion,
no history rewrite of any kind occurred** — and §8's corrected clause is why
that sentence can be written without qualification: Rule 20 permits none of
those three, only the amending of an unpushed commit, and even that was not
needed.

---

## 16. Commits

    commit 1   6b4911ba1dc3853ecd216358549891781dce72e0   specs/2026-08-15T0121Z_integrate-debt-register-cc.md
    commit 2   7092d289770c1fe90440a6d001f58577e4fec5a8   reviews/chatgpt/2026-08-15T0121Z_integrate-debt-register-cc.md
    commit 3   0f3660afb221dfb4c877d29c3e234d3b8b9bde20   --no-ff merge of 023b8b02…

**Commit 4's message, INTENDED:**

    report: the governance debt register lands on main

---

## 17. Did completing the `C` line make me want to repair `G-02` or build `G-05`?

**Asked by §9, and the answer is yes to both, more strongly than in the source
task.**

**`G-02` is one docstring line**, and the pull was sharper here than when the
entry was written, because this is the last task in the line. A line that ends
with every entry unrepaired reads as a line that achieved a filing system.
**Repairing the one entry marked `REPAIRABLE` would have made the closing
report look like it finished something.** That is precisely the wrong reason
to make a change.

**`G-05` was the stronger temptation**, because its shape is written into its
own entry: compare the digest a review cites against the SHA-256 of the
committed specification blob. **I performed exactly that comparison by hand in
§3 of this report**, as A2 required. **Having just executed the measurement, a
mechanism that performs it is about fifteen lines of test.** The gap between
"I did this once by hand" and "the repository does this always" felt like
nothing, and it is the entire content of `SPECIFIABLE`.

**I confirm I built neither, and repaired neither.** **MEASURED:
`scripts/p2_phase01_scalar_exploratory.py` and everything under `tests/` are
blob-identical at base and head**, inside §11's 400 of 400. **`G-04`, `G-05`
and `G-06` remain unbuilt, and all three entries still read `SPECIFIABLE`.**

**Why the prohibition is right and not merely obeyed:** doing the measurement
once by hand is what `SPECIFIABLE` means, and an executor who converts that
into a mechanism inside an integration task has built an unreviewed mechanism
and dated it with someone else's review. **The distance between doing a check
once and the repository doing it always is exactly the debt**, and shortening
it opportunistically is how a register becomes fiction.

**I also added no twelfth entry, changed no disposition, registered §10.2
nowhere, and created no classification artifact in the repository.**

---

## 18. Rule 16 assessment — what the assembled set does NOT establish

**Rule 16 is operative. All four junctions the specification names are
addressed.**

### 18.1 First junction — a completed line is not a closed gap

**After this lands, the planned `C-a` / `C-b` / `C-c` sequence is complete.**
Prose conventions were consolidated, two selected mechanisms were built, and
the known debt set has an authoritative register. **That is a plan completing.
It is not governance work completing**, and a reader may take the one for the
other.

**The disposition counts, MEASURED, stated beside the completion claim as §7
requires:**

    REPAIRABLE            1
    SPECIFIABLE           3
    NOT REPAIRABLE HERE   1
    RULED                 1
    METHOD NOTE           1
    OPEN                  4

**Three of eleven entries name a mechanism that does not exist. Four are
`OPEN`, with no mechanism shape defined at all. One is not repairable inside
this repository.** **The one entry marked `REPAIRABLE` is unrepaired**, and
the one marked `RULED` was ruled acceptable rather than fixed.

**`SPECIFIABLE` means specifiable and not specified.** **The count of entries
whose underlying defect this line removed is zero.** **The classification's
count of objects with no machine behind them is unchanged by this merge.**

**I do not describe the `C` line as closing the governance gap**, and nothing
in this report should be read as claiming that no governance work remains.

### 18.2 Second junction — the register has no mechanism

**Nothing requires an entry to be added when governance debt is found.**
Nothing checks that an entry stays current, and nothing would notice if the
file stopped being updated tomorrow. **It is maintained by the same authoring
habit that `G-04` records as insufficient for `stated:`.**

**`G-03`'s own reservation applies to the file carrying it.** The recorded
objection to the proposed `CORRECTIONS.md` was that nothing would keep such a
file updated. **That objection is not answered by `docs/GOVERNANCE-DEBT.md`
existing** — it is the same objection, now attached to a file that was created
rather than declined, and the file states this about itself so a reader who
never sees this report still meets the limit.

### 18.3 Third junction — the provenance gap is real and unregistered

**The identifiers `C1`–`C5` and `D1`–`D4` are cited on `main` — in
`CONVENTIONS.md`'s consolidation record, in the enforcement classification, and
in several specifications and reports — and their authoritative source is not
there.** §10.2 gives the measurement: no file in the tree carries the digest
those documents cite.

**This gap is `identified but not registered by this task`.**

**The register does not cover it**, and I do not present it as covering it.
**The eleven entries are the eleven entries**, and this gap is not among them.
A reader who wants to know what `D4` says still cannot find out from this
repository after this lands.

### 18.4 Fourth junction — two files a reader might call the register

**`docs/BRANCHING_POLICY.md` is the superseded-branch register. `P4` checks
it.** It is what `register_path` names, and A16's six exit statuses are read
against the branches it records.

**`docs/GOVERNANCE-DEBT.md` is checked by nothing.** No property reads it, no
validator asserts anything about its contents, and **its contents bind
nobody.** Nothing enforces that its entries are accurate, complete or current.

**A reader meeting "the register" on `main` after this lands must ask which
one.** §13.7 states the distinction in the report body as A14 directs, and it
is repeated here because the fourth junction is exactly that a correct
statement in one section does not prevent a wrong reading in another.

---

## 19. Stops and clarifications

**No stop occurred.** All four checker invocations exited 0, RUN 2 passed at
both prospectivity readings, the conflict list was empty, and no acceptance
criterion failed.

**Primary categories, each reported even where empty:**

    SPECIFICATION_DEFECT                          0 stops, 0 findings
    ENVIRONMENT                                   0 stops, 0 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 1 finding
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 2 findings

### 19.1 `SPECIFICATION_DEFECT` — none in THIS specification

**Nothing in this specification was found false about the repository or about
its own bytes.** Its scope block declares both keys, and §13.6 verified that
against the committed bytes rather than trusting the claim.

**§10.1's attribution error belongs to the `C-c` specification, not this
one**, and this specification carries it as a corrected finding with the right
anchors. **It is reported under A11 rather than here**, because it is a
finding this task was told to carry, not a defect this task discovered.

### 19.2 `OBSERVATION_METHOD_ERROR` — one finding, mine, caught before it was reported

**A probe read a field name the checker does not emit.** Listing `P1`'s
selected subjects, I used `specification` as the key; the record's key is
`path`, and the probe printed `None` for both subjects. **Re-run against the
actual keys, the subject set is the two specifications in §13.3.**

**This is `G-11` exactly, for the second time in two tasks**, and it is worth
recording that the entry's own advice worked: the probe disagreed with a
checker that had just exited 0, and the probe was wrong. **No figure from the
faulty probe reached a commit.**

### 19.3 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — two findings

**First: the classification artifact is absent**, §10.2 and §18.3.
**Identified but not registered by this task.** Whether it becomes a twelfth
entry is the PI's to decide; §3 forbids this task from deciding it, and I did
not.

**Second: `G-11`'s own evidence still does not resolve on `main`.** The `C-c`
report recorded this and the entry says so in its own text. **Landing does not
change it**: the incident it describes was post-report evidence returned to
the Reviewer and never written back, so after this merge `main` carries an
entry whose instance cannot be verified from `main`. **Reported, not
repaired** — repairing it would mean editing an arriving file, which §3
forbids.

### 19.4 `ENVIRONMENT` — nothing to report

**No environment failure occurred.** **Rule 13 carries two diagnostic orders,
a known open item. Neither was exercised**, and I am not naming one as having
applied.

**Nothing was installed.** Python 3.11.15 and pytest 9.1.1, as present.

### 19.5 `REPOSITORY_DEFECT` — nothing to report

**No defect in the repository was found by this task.** The one repository
fact that reads as a defect — the absent classification artifact — is recorded
under §19.3 as an evidence-provenance gap, because the repository is not
malfunctioning: a document was never committed.

### 19.6 One thing I would have specified differently

**A5 gives the frozen manifest with `{HHMM}Z` placeholders, and `P1` counts
those placeholder strings as paths.** §13.4 shows the `counted_set` containing
`reports/2026-08-XXT{HHMM}Z_integrate-debt-register-cc.md` — a path that
exists nowhere. **`P1` passes because it compares the declared total against
the block's own enumeration, and both contain the placeholder**, so the check
is self-consistent and blind to whether any listed path is real.

**That is not a defect in this specification**, which followed the established
convention, and `P1`'s `does_not_establish` states the limit honestly. **But a
reader comparing `P1`'s `counted_set` against the repository will find two
entries that resolve to nothing**, and I would have preferred the manifest to
carry the resolved paths once the token is fixed by commit 1 — or `P1` to
report that it is counting placeholders. **I raise it as an observation, not
as an obstruction: nothing here was blocked by it.**

**Nothing in the specification was unsatisfiable or ambiguous enough to
require a stop.** §8's corrected Rule 20 clause removed the one ambiguity that
would have forced one, and it removed it in the specification rather than
leaving the executor to choose between inconsistent instructions.

---

## 20. Evidence layering

**Committed in this report, MEASURED at commit 3:** A1–A13 and A15–A17 for
commits 1–3; A14's four invocations with both configs and both JSON outputs;
commits 1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; A5's final
base-to-commit-4 scope of 7 additions and 1 modification.

**Post-report evidence, returned to the Reviewer and NOT written back:** A5's
final scope measured base-to-commit-4; A14-final, being RUN 2 re-run at commit
4 before the landing; A13 and A16 re-run after the advance; A17 for commit 4;
the pre-advance `--is-ancestor` exit status; the exact push command; remote
`main` read back; the source branch tip unchanged; final ancestry
confirmation.

**Nothing in this report claims to measure commit 4.**
