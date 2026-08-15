# Execution report — `C-c`: an authoritative register for governance debt

**Specification:** `specs/2026-08-15T0008Z_debt-register-cc.md`
**Specification evidence base:** `80595d4cd575d1d024d1415b9b599947bf847677`
**Branch:** `governance/debt-register-cc`, cut from authoritative `main` @ `80595d4c…`
**Classification:** MATERIAL. Governed by Rule 15, Rule 18, and **Amendments M–P and Rules 19–21.**

**Every figure below is labelled MEASURED or INTENDED.** **This report is
written at commit 3 and measures nothing at commit 4.**

**This task does not touch `main`.** It produces a branch. Integration is a
separate task.

---

## 1. Outcome

**The register exists, it is reachable, and it repairs nothing.**

**MEASURED at commit 3:** eleven entries, each with exactly one disposition,
none `CLOSED`; 3 additions and 1 modification; `CONVENTIONS.md` gains one
region of two lines and loses none, and the base file is an exact in-order
subsequence of the head; 400 of 400 other paths blob-identical; validators
unchanged at 324 passed, 2 deselected; all four checker invocations exit 0
with `overall: PASS`.

**Two findings are carried forward rather than silently absorbed**, and both
concern facts asserted rather than measured:

- **`A5`'s figure was misattributed.** §2 states 13 of 50 at `f179b45e`.
  **MEASURED: `f179b45e` carries 15 of 52. The figure 13 of 50 belongs to
  `bec01171`, one landing earlier.** The register records the corrected
  attribution.
- **The classification that defines `C1`–`C5` and `D1`–`D4` is not a
  committed artifact.** It is identified in the `C-a` consolidation record by
  digest `1c65e68c…`, and **MEASURED: no committed file has that digest.**

**No twelfth entry was added.** Both findings are reported here and left, per
§8.

---

## 2. Refs and inputs — A1

**MEASURED.**

    remote refs/heads/main (git ls-remote)     80595d4cd575d1d024d1415b9b599947bf847677
    refs/remotes/origin/main                   80595d4cd575d1d024d1415b9b599947bf847677
    specification evidence base                80595d4cd575d1d024d1415b9b599947bf847677

**The authoritative `main` resolves to the specified base. No ref mismatch,
and no STOP.**

**Blob ids at the evidence base:**

    CONVENTIONS.md                                   85b437869cface425ae1d5f3207644a599f2c9de
    derivations/P2-DEFERRED-ITEMS.md                 33b3a664e0578ded484e31ad7f96f3a2908bcbb1
    derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md    cd53ec3db038fb6bfde299b75661eec4824458c1

### 2.1 One local ref is stale, and it is not the one A1 names

**Reported because a reader running `git rev-parse main` in a fresh clone of
this container would see a different answer, and should not conclude the base
is wrong.**

**MEASURED:** this container's local `refs/heads/main` resolves to
`0f7961747abe2a18b436c0b1e5b928f425ea4d9a`.

**It is a strict ancestor of the authoritative `main`** — `--is-ancestor`
exit 0 — **so it is behind, not divergent.** Its reflog shows it was last
moved by a `pull --ff-only` and never since: every landing in this programme
advances the remote's `refs/heads/main` by direct push, which does not update
a local branch ref that is never checked out.

**Nothing measured in this report reads that ref.** Every measurement names an
explicit SHA or `origin/main`. **A1 is satisfied against the authoritative
ref, and this is recorded as a clarification, not a stop.**

---

## 3. The review binds to these bytes — A2

**MEASURED.**

    SHA-256 of the arriving specification            3b145a2a4bef0bad6e0ccbc301ba172a6c89d357628f859e57ef8ab953582ec1
    SHA-256 the review records as reviewed           3b145a2a4bef0bad6e0ccbc301ba172a6c89d357628f859e57ef8ab953582ec1
    SHA-256 of specs/2026-08-15T0008Z_...-cc.md      3b145a2a4bef0bad6e0ccbc301ba172a6c89d357628f859e57ef8ab953582ec1

**Equal, all three.** The digest field is filled in and names this
specification, not a different one. **The committed specification is
byte-identical to the arriving file** — verified by `cmp`, not by inspection.
**Nothing in either arriving file was modified.**

**The review's verdict is `APPROVED`,** and it records one non-blocking
wording ambiguity: the sentence pairing `C1` and `C3` with `G-09` and `G-04`
can be misread as mapping `C3` to `G-04`. **§4 of this report follows the
body's explicit mapping**, and **`G-04` is not reported as the residual of
`C3`.** `G-04` is the remaining `C2` authoring-enforcement gap for `stated:`;
`G-09` is the residual of the gate-heading grammar problem.

---

## 4. The eleven entries and their dispositions — A3

**MEASURED at commit 3, read from the committed file.**

    G-01  the executor harness conflicts with P6                NOT REPAIRABLE HERE
    G-02  a docstring asserts a freeze the determination rejects REPAIRABLE
    G-03  corrections are not discoverable from what they correct OPEN
    G-04  nothing requires a new specification to carry stated:  SPECIFIABLE
    G-05  nothing compares a review's digest to the specification SPECIFIABLE
    G-06  nothing performs the auto-merge line-survival check    SPECIFIABLE
    G-07  the marker vocabulary is defined only in a record      RULED
    G-08  a criterion can assert something false about itself    OPEN
    G-09  nothing independently validates the shared grammar     OPEN
    G-10  nothing detects a guard going vacuous                  OPEN
    G-11  a probe contradicting a check is likelier to be wrong  METHOD NOTE

**Counts, MEASURED:**

    REPAIRABLE            1
    SPECIFIABLE           3
    NOT REPAIRABLE HERE   1
    RULED                 1
    METHOD NOTE           1
    OPEN                  4
    ---------------------------
    entries              11

**Every entry carries exactly one disposition.** None carries two, none
carries none. **MEASURED: the string `CLOSED` occurs on one line of the new
file, and that line is the sentence saying no entry is marked `CLOSED`.**

### 4.1 Why `G-09` and `G-10` are `OPEN` and `G-04` is not

**§3 of the specification names `G-05` and `G-06` as having a mechanism shape
and `G-09` and `G-10` as not.** It is silent on `G-04`, so the judgment is
mine and I state it rather than leave it implicit.

**`G-04` carries `SPECIFIABLE` because a shape exists and is written into the
entry:** over the specifications a task's range adds, require each
scope-bearing one to carry `stated:`, rather than reaching the question only
through subject selection. That is the same kind of range-property `P1`
already is, differing in that it does not depend on selection. **The
definitional edge — what counts as scope-bearing — is real and is not
resolved by naming the shape.**

**`G-09` and `G-10` carry `OPEN`,** as §3 expects. An independent oracle for
a grammar and a detector for a guard gone vacuous are problems whose shape is
not defined, and **`C5`'s own record says naming the regress is not solving
it.** **I did not assign `SPECIFIABLE` to either.**

**`G-08` also carries `OPEN`**, for the same reason: checking what a
specification asserts about its own bytes, in general, has no shape I can
name, and asserting one would be the false green this line of work exists to
prevent.

---

## 5. Where each entry's evidence sits — A4

**MEASURED: every path cited below resolves at the evidence base**, verified
with `git cat-file -e` against `80595d4c`, fourteen paths, fourteen resolving.

    G-01  CONVENTIONS.md Rule 20 and item B4 in the C-a record;
          reports/2026-08-13T1239Z_ac4-symmetry-goldstone.md          RESOLVES
    G-02  scripts/p2_phase01_scalar_exploratory.py line 73            RESOLVES
    G-03  reports/2026-08-12T1919Z_integrate-enforcement-checks-v2.md
          line 433                                                    RESOLVES
    G-04  derivations/GOVERNANCE-ENFORCEMENT_classification.md
          line 145; the C-a record in CONVENTIONS.md                  RESOLVES
    G-05  CONVENTIONS.md line 1183 (Amendment N); C-a record item A3  RESOLVES
    G-06  CONVENTIONS.md line 262 (Amendment P); C-a record item B3   RESOLVES
    G-07  CONVENTIONS.md lines 264, 388, 896, 1185 (markers in use);
          C-a record lines 1378-1391 (the explaining sentence)        RESOLVES
    G-08  specs/2026-08-14T2212Z_mechanisms-cb.md A13;
          reports/2026-08-14T2212Z_mechanisms-cb.md;
          specs/2026-08-14T2307Z_integrate-mechanisms-cb.md §2        RESOLVES
    G-09  scripts/governance_tools/task_checker.py;
          tests/test_repository_structure.py; both C-b reports        RESOLVES
    G-10  tests/test_gate_pins.py;
          scripts/governance_tools/task_checker.py (P7);
          reports/2026-08-14T0325Z_p7-repair-and-pin-validator.md     RESOLVES
    G-11  the instance itself                              DOES NOT RESOLVE

**`G-02` verified by content, not by path alone.** MEASURED, line 73 of
`scripts/p2_phase01_scalar_exploratory.py` at the base:

    """Return ``I0(Mhat)`` and ``d I0 / d Mhat`` for the frozen Wilson D."""

### 5.1 The one entry whose evidence does not resolve

**`G-11`'s instance is not in the repository.** It arose as post-report
evidence for the `C-b` integration, returned to the Reviewer and — correctly,
under that task's evidence layering — **not written back.**

**A4 says an entry whose evidence cannot be located is a finding to record
rather than a reason to drop the entry.** The entry is kept and says so in its
own text. **The committed artifacts it concerns — `tests/test_gate_pins.py`
and its `collect_pins` field names — do resolve**; what does not resolve is
the account of the incident.

### 5.2 A second reference that does not resolve, reported and not entered

**The classification that assigns the labels `C1`–`C5` and `D1`–`D4` is not a
committed artifact.**

The `C-a` consolidation record identifies it by digest:
`1c65e68c0263b1fcfab24d260d81409a4cd687139c4f106e0a8112fb346d61d9`.
**MEASURED: I computed the SHA-256 of every file in the tree at `80595d4c` and
none equals that digest.** A path search for a debt-classification file
returns nothing.

**MEASURED, how far the labels are traceable from the repository alone:**

    `C4`  named in 6 files    `C5`  named in 3 files
    `D1`  named in 2 files    `D4`  named in 2 files
    `D2`  named in 0 files    `D3`  named in 0 files

The occurrences are citations and ranges — `C1`–`C5`, `D1`–`D4` — in specs
and reports. **None of them defines the labels.** A reader with only this
repository can see that `D4` is referred to and cannot learn what `D4` says.
(`C1`, `C2` and `C3` return higher counts, but most are science tasks named
`c1-complement-provenance` and `c3-curvature-asymmetry`, not debt items.)

**This is reported and left.** It is arguably an instance of `G-03`'s shape —
a thing referred to with no route from the reference to the referent — but
**§8 forbids adding a twelfth entry, and the register stays at eleven.**
Whether it belongs in the register is the PI's to decide, not mine.

---

## 6. `G-04`'s figure, re-measured — A5

**Method: count `.md` files under `specs/`, and those carrying a line matching
`^[[:space:]]*stated:`, at each revision. `stated:` ALONE — the three keys
were counted separately and are reported separately below.**

**MEASURED:**

    13 of 50   at bec01171   <- the figure §2 quotes
    15 of 52   at f179b45e   <- the revision §2 attributes it to
    17 of 54   at 80595d4c   <- this evidence base

**The specification's figure is right and its attribution is wrong.** §2 and
§10 both state "13 of 50 at `f179b45e`". **MEASURED, `f179b45e` carries 15 of
52.** The pair 13 of 50 is exact at `bec01171`, the base of the `C-a`
integration and one landing earlier; the two specifications that `C-a` and its
integration landed account for the difference in both numerator and
denominator.

**I checked my own method before reporting this**, because a probe that
contradicts a written figure is the shape `G-11` records. **MEASURED: all 15
matches at `f179b45e` are genuine indented `stated: N additions, M
modifications` scope records — no prose false positives** — and every entry
under `specs/` at that revision is a `.md` file, so the denominator is not a
filter artefact.

**The qualitative claim in §2 is TRUE as written.** MEASURED: the set carrying
`stated:` is contiguous. Every specification from
`specs/2026-08-12T2015Z_p1-declared-total.md` onward carries the key; none
before it does. **"Exactly those issued after the grammar landed" holds at
every one of the three revisions.**

**The register records the corrected attribution**, because writing a
knowingly false attribution into the authoritative register would be the `G-08`
defect the register itself records.

### 6.1 The other two keys, reported and not entered — A5, second part

**Two measurements, because the obvious one is wrong.**

**MEASURED, specifications carrying a line matching the key anywhere:**

    key                  at f179b45e     at 80595d4c
    stated:              15 of 52        17 of 54
    append_only:          0 of 52         2 of 54
    authorised_gates:     0 of 52         2 of 54

**MEASURED, specifications whose SCOPE BLOCK declares the key** — parsed by
walking the indented block containing `stated:` and reading its keys:

    key                  at 80595d4c
    append_only:          1 of 54
    authorised_gates:     1 of 54

**The line-match count is inflated, and by exactly the entry the register
records as `G-08`.** The two line-matching files are the `C-b` pair. Only
`specs/2026-08-14T2307Z_integrate-mechanisms-cb.md` declares the keys in its
scope block, at lines 142 and 143. The other,
`specs/2026-08-14T2212Z_mechanisms-cb.md`, matches at lines 106, 108 and 181 —
**all three in its design description of the key format, none in its scope
block, which runs from line 290 and carries `stated`, `base`, `head`, `mode`,
`add`, `modify` and `forbidden_operations` and neither declaration key.**

**That is `C-b`'s `A13` visible as a measurement:** the criterion asserted
that this scope block declared both keys, and the block does not. **I report
the strict figure as the real one**, because a grep for the key name answers a
different question than the one asked.

**Both figures are reported as findings and enter no register entry.** §2 says
why: `C-b` established `append_only:` and `authorised_gates:` as a declaration
mechanism in which `DECLARED_EMPTY` is a valid and meaningful state, so
whether a given task needs either depends on the task, and no uniform
obligation follows from a low count. **Whether their absence is debt is
undecided, and I did not decide it.** **`G-04` is about `stated:` alone.**

---

## 7. `D4` is cross-referenced, not duplicated — A6

**MEASURED at the evidence base:** `derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md`
line 70 carries

    ## `OPEN-CC-3` — the mechanism of the bit-exact mirroring is unresolved

**The register points at it** and does not restate it: the section "Not
entered here — `D4`" names `OPEN-CC-3` and the file it lives in, and gives the
reason — a second entry would create a second place for one status to drift.

**MEASURED: `derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md` is byte-identical
at base and head**, blob `cd53ec3db038fb6bfde299b75661eec4824458c1` at both.
**The C-check register was read and not touched.**

---

## 8. Nothing in the register binds — A7

**The sentence, MEASURED, line 3 of the new file:**

> **Nothing in this file binds.** It records what the rules, amendments and
> task reports already carry, and it creates, modifies and explains no
> obligation.

**MEASURED: the count of lines in `docs/GOVERNANCE-DEBT.md` containing `MUST`,
`SHALL` or `binds` is ONE**, and it is that line. **The count does not exceed
the one sentence, so there is nothing to name and justify.**

**A wider sweep, reported because the narrow one could pass while the file
still read as obligatory.** MEASURED, case-insensitive, for `must`, `shall` or
`bind` in any form: **two lines.** The second is line 164, "The binding rules
use the mechanism markers", inside `G-07`. **It describes the rules in
`CONVENTIONS.md`, which do bind; it creates no obligation here.** It does not
match `A7`'s pattern and is reported for completeness.

---

## 9. The pointer, and nothing else in `CONVENTIONS.md` — A8

**The full diff, base to commit 3, MEASURED:**

    diff --git a/CONVENTIONS.md b/CONVENTIONS.md
    index 85b4378..8badc51 100644
    --- a/CONVENTIONS.md
    +++ b/CONVENTIONS.md
    @@ -1402,3 +1402,5 @@ list of what was noticed across one working session, and several of its items
      were found only because a later task tripped over them. **A list assembled by
      noticing is not a survey**, and the absence of a rule here is not evidence
      that the corresponding failure cannot occur.
    +
    +**Governance debt is registered in `docs/GOVERNANCE-DEBT.md`** — an eleven-entry record of the known governance debt, each entry with its disposition and where its evidence sits. Nothing in that file binds either.

**That is the whole diff. One hunk, MEASURED by `grep -c '^@@'`.**

    added lines      2      (one blank separator, one pointer line)
    deleted lines    0

**The pointer lands inside the `C-a` consolidation record**, which begins at
line 1349 and is the section the specification names. **It adds no rule and no
amendment**, and its own last clause says nothing in the register binds
either — so the pointer does not turn a non-binding record into a binding
source.

### 9.1 The subsequence check, run independently

**A8 calls the diff and the subsequence two independent measurements of one
property, neither substituting for the other. Both were run.**

**MEASURED**, by walking the head file once and advancing a pointer into the
base file on each equal line:

    base lines          1405
    head lines          1407
    matched in order    1405
    exact subsequence   True

**Every line of the base survives, in order.** Nothing was reflowed, reworded
or reordered. **Zero deletions from `CONVENTIONS.md`, as §8 requires.**

### 9.2 Rules and amendments, unchanged

**MEASURED at base and at head:**

    numbered rules            21    21
    amendment letters         15    15
    Amendment J present        0     0

**Twenty-one rules, fifteen amendment letters `A`–`P` with no `J`, identical
at both.** **This task adds neither, and the measurement confirms it rather
than assuming it.**

---

## 10. Scope — A9

**MEASURED, base to commit 3:**

    M  CONVENTIONS.md
    A  docs/GOVERNANCE-DEBT.md
    A  reviews/chatgpt/2026-08-15T0008Z_debt-register-cc.md
    A  specs/2026-08-15T0008Z_debt-register-cc.md

    3 additions, 1 modification

**MEASURED: no status code other than `A` or `M` appears** — no delete,
rename, copy, type change, unmerged or unknown, which is the frozen manifest's
`forbidden_operations` list.

**INTENDED, base to commit 4:** 4 additions and 1 modification, the fourth
addition being this report at
`reports/2026-08-15T0008Z_debt-register-cc.md`. **That figure is INTENDED, not
MEASURED: this report is written before the commit that contains it.** The
frozen manifest's five paths are exactly these five.

---

## 11. Protected paths — A10

**MEASURED, path by path, base to commit 3:**

    paths at the evidence base          401
    excluded (CONVENTIONS.md)             1
    compared                            400
    blob-identical                      400
    differing                             0
    missing at head                       0

**Every path that existed at the base, other than `CONVENTIONS.md`, is
blob-identical at the head.**

**The named ones, MEASURED individually:**

    GATES.md                                        2b3bd5069414   IDENTICAL
    DECISION_LOG.md                                 d9dd2bf3a8cc   IDENTICAL
    docs/BRANCHING_POLICY.md                        3f0f35d4da44   IDENTICAL
    derivations/P2-DEFERRED-ITEMS.md                33b3a664e057   IDENTICAL
    derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md   cd53ec3db038   IDENTICAL

**Nothing under `scripts/`, `tests/`, `results/` or `derivations/` changed** —
covered by the 400, and the two registers are named above because the
specification names them.

---

## 12. The checker — A12, MEASURED at commit 3

    base   80595d4cd575d1d024d1415b9b599947bf847677
    head   25ef7f57a928fd1e9007605883b66a5b9a10d0d9   (commit 3)

**Both prospectivity readings for each run, so four invocations. All four
exited 0 with `overall: PASS`.**

    run 1 INCLUSIVE   exit 0   PASS   sha256 1f13f207d400e20c201f7899ab7422498cc9e4fa029597b3c5c7c7c5441c2d89
    run 1 EXCLUSIVE   exit 0   PASS   sha256 f24f27a3cc052fce5d2f3f7d15f981168ae7cefee182c92fd6feb1f65af2698f
    run 2 INCLUSIVE   exit 0   PASS   sha256 1f13f207d400e20c201f7899ab7422498cc9e4fa029597b3c5c7c7c5441c2d89
    run 2 EXCLUSIVE   exit 0   PASS   sha256 f24f27a3cc052fce5d2f3f7d15f981168ae7cefee182c92fd6feb1f65af2698f

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 NOT_APPLICABLE
    P6 PASS   P7 PASS   P8 PASS   P9 NOT_APPLICABLE

**`P5` and `P9` are `NOT_APPLICABLE` because this task has no merge**, which
is the state the vocabulary was widened to express: a range with no merge
genuinely has no `P5` subject. **`NOT_APPLICABLE` does not make the run
INCOMPLETE, and no property returned `NOT_DECLARED`, `NOT_PARSEABLE` or
`DECLARATION_CONFLICT`.**

### 12.1 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "80595d4cd575d1d024d1415b9b599947bf847677",
      "head": "25ef7f57a928fd1e9007605883b66a5b9a10d0d9",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 12.2 RUN 2 config, verbatim — stop-governing

    {
      "base": "80595d4cd575d1d024d1415b9b599947bf847677",
      "head": "25ef7f57a928fd1e9007605883b66a5b9a10d0d9",
      "specification_paths": ["specs/2026-08-15T0008Z_debt-register-cc.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I chose.** `append_only_paths`,
`authorised_modified_gates`, the boundary and `register_path` are fixed by
A12. **Neither the config nor this specification's declarations were adjusted
to make RUN 2 pass** — §8 forbids both, and neither was needed.

### 12.3 The measured RUN 1 subject set

**MEASURED: RUN 1's default selection chose exactly one specification**, and
it is the one RUN 2 names:

    specs/2026-08-15T0008Z_debt-register-cc.md   stated add 4 modify 1   counted add 4 modify 1

**The range adds no other specification**, so the default selection and the
named selection coincide. **MEASURED: the two runs' outputs are byte-identical
at each prospectivity reading** — `cmp` returns equal, and the sha256 pairs
above are equal by inspection. **Both outputs are still given verbatim below,
as A12 requires**, rather than one being reported as standing for the other.

The two prospectivity readings differ in exactly one line and in no verdict:

    254c254
    <         "inclusivity": "INCLUSIVE",
    ---
    >         "inclusivity": "EXCLUSIVE",

### 12.4 `P7`, and the section count it saw

    declared_source          specification
    declared                 []
    raw_heading_count_base   14        section_count_base   14
    raw_heading_count_head   14        section_count_head   14
    unauthorised_changed     []        added_sections  []   removed_sections  []

**`P7` reports fourteen sections, read through the shared helper. `PASS` at
zero would have been a STOP.**

### 12.5 Both declarations came from the specification

**MEASURED, identical in all four invocations:**

    P3   declared_source: specification    declared: ['DECISION_LOG.md']
    P7   declared_source: specification    declared: []

**Both properties took their set from this specification's own scope block,
not from the config.** The config supplied the same two values, so the
precedence rule resolved to `specification` and no conflict arose.
**MEASURED: `DECLARATION_CONFLICT` appears nowhere in any of the four
outputs.**

**They agree because they were written to agree**, not because either was
adjusted. Had they differed, `P3` and `P7` would have returned
`DECLARATION_CONFLICT`, RUN 2 would have exited non-zero, and §8 makes that a
finding and a STOP rather than something to fix by editing either side.

### 12.6 `docs/GOVERNANCE-DEBT.md` is not the superseded-branch register

**Said explicitly, because two files described as registers are exactly the
adjacency that produces a wrong reading later.**

**`register_path` in both configs names `docs/BRANCHING_POLICY.md`, and not
the new file.** `P4` checks the superseded-branch register — the record of
branches that were superseded and may not be merged — and
`docs/BRANCHING_POLICY.md` is that register.

**`docs/GOVERNANCE-DEBT.md` is not that register, and this task does not make
it one.** It records governance debt. `P4` does not read it, nothing in the
checker reads it, and **MEASURED: `docs/BRANCHING_POLICY.md` is blob-identical
at base and head**, so the register `P4` does read was not touched. **The two
files share the word "register" and nothing else.**

### 12.7 RUN 1 output, verbatim

    {
      "base": "80595d4cd575d1d024d1415b9b599947bf847677",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "25ef7f57a928fd1e9007605883b66a5b9a10d0d9",
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
                "commit": "e69d1ca1098951741d69c0dc42e73ea32dd58ed4",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "42ab2107d1c9d63aee64c754799ca922641e47ca",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "25ef7f57a928fd1e9007605883b66a5b9a10d0d9",
                "work_paths": [
                  "CONVENTIONS.md",
                  "docs/GOVERNANCE-DEBT.md"
                ]
              }
            ],
            "first_review_commit": "42ab2107d1c9d63aee64c754799ca922641e47ca",
            "first_work_commit": "25ef7f57a928fd1e9007605883b66a5b9a10d0d9",
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
              "specs/2026-08-15T0008Z_debt-register-cc.md"
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
              "specs/2026-08-15T0008Z_debt-register-cc.md"
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
            "first_commit": "e69d1ca1098951741d69c0dc42e73ea32dd58ed4",
            "first_commit_paths": [
              "specs/2026-08-15T0008Z_debt-register-cc.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-15T0008Z_debt-register-cc.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-15T0008Z_debt-register-cc.md"
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
        "commits_in_scope": 3,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

### 12.8 RUN 2 output, verbatim

    {
      "base": "80595d4cd575d1d024d1415b9b599947bf847677",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "25ef7f57a928fd1e9007605883b66a5b9a10d0d9",
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
                "commit": "e69d1ca1098951741d69c0dc42e73ea32dd58ed4",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "42ab2107d1c9d63aee64c754799ca922641e47ca",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "25ef7f57a928fd1e9007605883b66a5b9a10d0d9",
                "work_paths": [
                  "CONVENTIONS.md",
                  "docs/GOVERNANCE-DEBT.md"
                ]
              }
            ],
            "first_review_commit": "42ab2107d1c9d63aee64c754799ca922641e47ca",
            "first_work_commit": "25ef7f57a928fd1e9007605883b66a5b9a10d0d9",
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
              "specs/2026-08-15T0008Z_debt-register-cc.md"
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
              "specs/2026-08-15T0008Z_debt-register-cc.md"
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
            "first_commit": "e69d1ca1098951741d69c0dc42e73ea32dd58ed4",
            "first_commit_paths": [
              "specs/2026-08-15T0008Z_debt-register-cc.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-15T0008Z_debt-register-cc.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-15T0008Z_debt-register-cc.md"
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
        "commits_in_scope": 3,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

---

## 13. Validators — A13

**MEASURED, `python -m pytest` from the repository root:**

    before, at the base 80595d4c      324 passed, 2 deselected
    after,  at commit 3               324 passed, 2 deselected

**Unchanged, and expected to be: this task adds no test.** The "before" figure
was measured in a separate worktree checked out at the evidence base, not
quoted from the previous task's report.

**Exit status 0 both times.** **No change to explain.**

---

## 14. Commit-message hygiene — A14

**MEASURED on commits 1–3. Commit 4 is post-report evidence.**

    commit 1   e69d1ca1   spec: an authoritative register for governance debt
               trailer hits 0      not amended
    commit 2   42ab2107   review: pre-execution review for the governance-debt register
               trailer hits 0      not amended
    commit 3   25ef7f57   docs: register the governance debt and point at it from the conventions
               trailer hits 0      not amended

**MEASURED over the whole range: a scan for `Co-Authored-By`, `claude.ai/code`,
`Generated with`, `Claude-Session` and `noreply@anthropic` returns nothing.**

**Rule 20 binds this task and was not exercised.** No commit needed a
pre-push hygiene amend, because no commit was written with a trailer to
repair. **`P6` passed on the first attempt in all four invocations.**

---

## 15. Commits

    commit 1   e69d1ca1098951741d69c0dc42e73ea32dd58ed4   specs/2026-08-15T0008Z_debt-register-cc.md
    commit 2   42ab2107d1c9d63aee64c754799ca922641e47ca   reviews/chatgpt/2026-08-15T0008Z_debt-register-cc.md
    commit 3   25ef7f57a928fd1e9007605883b66a5b9a10d0d9   docs/GOVERNANCE-DEBT.md + CONVENTIONS.md

**The register and its pointer move together in commit 3, as §6 requires.** A
commit carrying one without the other would land either an unreachable
register or a pointer to nothing. **MEASURED: commit 3 touches exactly those
two paths.**

**Commit 4's message, INTENDED:**

    report: the governance-debt register and its two findings

---

## 16. Did writing the register make me want to repair `G-02`?

**Asked by §9, and the honest answer is yes.**

`G-02` is one docstring line. I had the file open to verify the line number,
the correct wording was obvious, and the edit would have taken less time than
writing the entry describing why it was not made. **The pull was real and it
was strongest at the moment I had already confirmed the defect** — having
proved something is wrong makes leaving it wrong feel like the error.

**I confirm I did not repair it.** `scripts/p2_phase01_scalar_exploratory.py`
is blob-identical at base and head, covered by A10's 400 of 400. **I read the
file and wrote nothing to it.**

**The reason the prohibition is right, and not merely a rule I obeyed:** a
recording task that repairs one item has repaired the cheapest item, not the
most important one, and its report then describes a repository that no longer
matches the register it just wrote. The entry's disposition is `REPAIRABLE`
and names its blocker — no task has been authorised to touch `scripts/`. **A
task that quietly authorises itself makes that field a lie.**

**I also did not build `G-05` or `G-06`**, did not create a `CORRECTIONS.md`,
did not decide `G-03`, added no rule or amendment, and entered no twelfth
entry. **Two findings that might have become entries are reported in §5.2 and
§6.1 and left there.**

---

## 17. Rule 16 assessment — what the assembled set does NOT establish

**Rule 16 is operative. All three junctions the specification names are
addressed.**

### 17.1 First junction — a register is not progress

**After this lands, governance debt has a home, and a reader may take the
existence of a home for progress on what lives in it. Nothing in the register
is repaired by being written down.**

**The disposition counts, MEASURED:**

    REPAIRABLE            1
    SPECIFIABLE           3
    NOT REPAIRABLE HERE   1
    RULED                 1
    METHOD NOTE           1
    OPEN                  4

**`SPECIFIABLE` means specifiable and not specified.** Three entries carry it.
**Zero mechanisms exist for them.** It records that a shape is known — compare
a cited digest against a committed blob; measure line survival across a merge;
require a scope-bearing specification to carry `stated:` — and knowing a shape
is not having built it.

**The one `REPAIRABLE` entry is unrepaired.** The one `RULED` entry was ruled
acceptable, not fixed. **The four `OPEN` entries have no shape at all.** **No
entry is `CLOSED`, and the count of entries whose underlying defect this task
removed is zero.**

### 17.2 Second junction — a list of what was noticed is not a survey

**This register is a list of what was noticed.** Three of its eleven entries
were found only because a later task tripped over them: the vacuous `P7`, the
harness trailer conflict, and `C-b`'s false self-assertion were each
discovered by a task that was doing something else and hit them.

**No survey was performed, and this task did not perform one.** I did not
enumerate the ways governance could fail and check each; I recorded eleven
items that were already known and located their evidence. **The absence of an
entry is not evidence that the corresponding debt does not exist.**

**Two pieces of direct evidence that the list is incomplete, from this task
alone.** §5.2 found a reference class that resolves nowhere — the
classification defining `C1`–`C5` and `D1`–`D4` is not committed — and §6
found a figure in the issuing specification attributed to the wrong revision.
**Neither was in the eleven. Both were found by doing something else.** That
is the second junction demonstrating itself during the task meant to record
it.

### 17.3 Third junction — the register has no mechanism

**Nothing requires an entry to be added when governance debt is found.**
Nothing checks that an entry stays current. Nothing detects an entry that has
gone stale, and nothing would notice if the file stopped being updated
tomorrow. **The register is maintained by the same authoring habit that
`G-04` records as insufficient for `stated:`.**

**`G-03`'s reservation applies to this file as much as to the
`CORRECTIONS.md` it describes.** The recorded objection to that proposal was
that nothing would keep such a file updated. **That objection is not answered
by this file existing**, and this file does not answer it. It is the same
objection, now attaching to a file that was created rather than declined.

**I did not build the mechanism here**, and §4 forbids it. **The register's
own closing section states this in the file itself**, so a reader who never
sees this report still meets the limit.

---

## 18. Stops and clarifications

**No stop occurred.** All four checker invocations exited 0, RUN 2 passed at
both prospectivity readings, and no acceptance criterion failed.

**Primary categories, each reported even where empty:**

    SPECIFICATION_DEFECT                          0 stops, 1 finding
    ENVIRONMENT                                   0 stops, 0 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 2 findings
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 2 findings

### 18.1 `SPECIFICATION_DEFECT` — one finding, not a stop

**§2 and §10 attribute the figure "13 of 50" to `f179b45e`. MEASURED: that
revision carries 15 of 52, and 13 of 50 belongs to `bec01171`.** §6 gives the
measurement and the register records the corrected attribution.

**Not a stop, because A5 anticipated re-measurement and required it.** The
specification asked for the figure to be re-measured rather than quoted, and
the re-measurement is what surfaced the misattribution. **The qualitative
claim attached to the figure is true at every revision measured.**

**Its shape is `G-08`'s** — an unchecked factual assertion in a specification —
though about a repository fact rather than about the specification's own
bytes, so it is `G-08`'s neighbour and not an instance of it. **It is reported
and not entered, per §8.**

### 18.2 `OBSERVATION_METHOD_ERROR` — two findings, both mine, both caught

**First: a probe over-counted the declaration keys.** Counting specifications
by grepping for a key name returned 2 of 54 for `append_only:`; parsing the
scope block returns 1 of 54. **The grep answered a different question than the
one asked.** §6.1 reports both figures and identifies the strict one as the
real one. **Caught before it reached the register, and the register does not
carry either figure.**

**Second: two counting probes were written wrong and corrected.** A rule-count
probe used a heading pattern the file does not use and returned 0 rules; the
correct pattern returns 21 at both base and head. An amendment-letter probe
returned a count of 0 while correctly listing 15 letters. **Both were rerun
before any figure was recorded**, and §9.2 reports the corrected measurements.
**Neither error reached a commit.**

**`G-11` is why these are reported rather than quietly fixed.** The entry
records that a hand-written probe contradicting a committed check is likelier
wrong than the check. **In §6 the same discipline ran the other way**: my
probe contradicted a figure written in the specification, and because there
was no committed check to defer to, I verified the probe — no false positives
among the 15 matches, no non-`.md` files in the denominator, and the
contiguity claim independently confirmed — **before reporting the
specification wrong.**

### 18.3 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — two findings

**First: the classification defining `C1`–`C5` and `D1`–`D4` is not
committed**, and is identified only by a digest no file in the tree matches.
§5.2 gives the measurement. **A reader with only this repository can see `D4`
cited and cannot learn what `D4` says.** **Whether this belongs in the
register is the PI's to decide; I reported it and left it.**

**Second: `G-11`'s own evidence does not resolve at the evidence base**, being
post-report evidence that was correctly not written back. §5.1 gives it.
**A4 required recording it rather than dropping the entry**, and the entry
says so in its own text.

### 18.4 `ENVIRONMENT` — nothing to report

**No environment failure occurred.** **Rule 13 carries two diagnostic orders,
a known open item. Neither was exercised**, and I am not naming one as having
applied.

**Nothing was installed.** Python 3.11.15 and pytest 9.1.1, as present.

### 18.5 A clarification that is not a finding

**The local `refs/heads/main` in this container is stale at `0f79617…`**, a
strict ancestor of the authoritative `main`. §2.1 gives the measurement and
the reason. **No measurement in this report reads that ref**, and A1 is
satisfied against the authoritative one.

### 18.6 One thing I would have specified differently

**A5 asks for the figure "at THIS evidence base" and states the prior figure
with a revision attached.** Had it asked for the prior figure to be
re-measured at its stated revision — which is what I did, and what surfaced
the misattribution — the check would have been explicit rather than a
by-product of my choosing to verify a number before contradicting it.

**A criterion that quotes a figure and asks only for a new one invites the
quoted figure to be trusted.** That is a small instance of the pattern `G-08`
records, and I mention it because the specification asked what I would have
specified differently, not because it obstructed anything here.

**Nothing in the specification was unsatisfiable, and nothing was ambiguous
enough to require a stop.** The one wording ambiguity the review flagged —
whether `C3` maps to `G-04` — was resolved by the body, as the review
directed, and §3 records which mapping was used.

---

## 19. Evidence layering

**Committed in this report, MEASURED at commit 3:** A1–A8, A10, A11, A13 and
A14 for commits 1–3; A9's scope base-to-commit-3; A12's four invocations with
both configs and both JSON outputs; commits 1–3 SHAs and their stored
messages.

**Committed in this report, INTENDED:** commit 4's message; A9's final scope
of 4 additions and 1 modification base-to-commit-4.

**Post-report evidence, returned to the Reviewer and NOT written back:** A9's
final scope measured base-to-commit-4; A12-final, being RUN 2 re-run at commit
4; A13 at commit 4; A14 for commit 4; the push; the branch tip read back.

**Nothing in this report claims to measure commit 4.**

**This task does not touch `main`.** The branch is the outcome; integration is
a separate task, and no merge, landing or register entry for a superseded
branch was written here.
