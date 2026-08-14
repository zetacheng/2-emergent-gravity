# Execution report — integrate the declared-total `P1` grammar, and land it

**Specification:** `specs/2026-08-14T1125Z_integrate-p1-declared-total.md`
**Specification evidence base:** `e3ce80639337956af5f934f7530d3b2476e5f6c1`
**Branch:** `governance/integrate-p1-declared-total`, cut from authoritative `main` @ `e3ce8063…`
**Source merged:** `governance/p1-declared-total` @ `8ff032e7f90ecfce4666fac34691b5670016bb75`
**Classification:** MATERIAL. Governed by Rule 15 and Rule 18.

**Every figure below is labelled MEASURED or INTENDED.** **This report is
written at commit 3, the merge commit, and measures nothing at commit 4.**

---

## 1. Outcome

**One merge, clean over a stale base. Both landing preconditions met.**

**§5 makes the advance conditional on two measurements, both taken at the
merge commit before anything was pushed:**

    A7    raw 14   GATE_HEADING parsed 14   equality TRUE
          RAW_GATE_HEADING present   declared-total grammar present
          parse_scope_block reads 'stated:' — exercised, not merely named
    A11   310 passed, 2 deselected, up from 301, delta +9 = the source's own new tests

**Both repairs survive the auto-merge, and I checked it two ways rather than
one.** Beyond A7's presence-and-parse check, I compared, line by line and for
each of the three auto-merged files, **the lines each side added over the
merge-base against the merged file:**

    scripts/governance_tools/task_checker.py     source +90 lines, all 90 present   main +57, all 57 present
    tests/test_task_checker.py                   source +104, all 104 present       main +133, all 133 present
    derivations/GOVERNANCE-ENFORCEMENT_…md       source +24, all 24 present         main +61, all 61 present

**Not one line from either side was lost.**

**The behavioural proof that `P1` changed, MEASURED:** `P1` now reports
**`stated: add 6 modify 3` against `counted: add 6 modify 3`** for this
task's own specification. **Every previous report in this line recorded `P1`
as a bare total** — `counted 10 / stated 10` for the same shape of manifest.
**The comparison is now per category.**

**MEASURED at commit 3:** 5 additions, 3 modifications, 8 changed paths,
empty conflict list. `GATES.md` byte-identical at base and head. All four
A10 invocations `PASS` at exit 0 with `P7` at 14 sections over 14 raw
headings.

**On the source task's `A10`, stated in the words §2 requires: the source
task's `A10` remains undischarged, and neither A9a nor A9b discharges it.**
§10 carries both runs, labelled EVIDENCE.

**A17, answered up front.** My harness's standing git guidance does instruct
a `Co-Authored-By` trailer and a session URL. **None was written on any of
the four commits**, nothing was suppressed by amendment, no commit was
amended.

---

## 2. Refs and the stale base — A1, MEASURED

**Read from the remote after `git fetch origin`:**

    refs/heads/main                            e3ce80639337956af5f934f7530d3b2476e5f6c1   as specified
    refs/heads/governance/p1-declared-total    8ff032e7f90ecfce4666fac34691b5670016bb75   as specified

    git merge-base e3ce8063… 8ff032e7…         1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**The merge-base is `1cb5550f…` and NOT the evidence base**, confirming the
stale base A1 names. **No mismatch. No stop.**

**One correction to the specification's descriptive figure, reported because
I measured it rather than repeating it.** §1 and §11 say the source was cut
*"five landings"* behind. **MEASURED: six.** Merge commits on `main`'s
first-parent line between `1cb5550f…` and `e3ce8063…`:

    22bfa68   merge: integrate the P7 repair and the pin validator
    6a7eab8   merge: integrate the AC-4 symmetry and Goldstone determination
    b3ca448   merge: land the C3 curvature-asymmetry finding and the C-check register
    ba13ac4   merge: land the C1 complement-root provenance finding
    a133f04   merge: land the admissibility contract, resolving two authorised conflicts
    9e6c3e6   merge: land the parameter-domain adoption line

**Six, not five**, over 15 first-parent commits. **This is descriptive colour
and not a criterion**, so it is not a stop; §17.2 records it as a secondary
finding. **The governing fact — that the base is stale and was not rebased —
is unaffected and is if anything understated by the specification.**

---

## 3. The pre-execution review — A2, MEASURED

    supplied specification    9ba407bf136075ac23e76161cc0644f9fbe0d260c6ad135edf3c6d900e399576
    committed specification   9ba407bf136075ac23e76161cc0644f9fbe0d260c6ad135edf3c6d900e399576   equal
    supplied review           f5adaf6ea23a22a5b6e4ab1ec8d4aeb8fd28c00e595921c679cc489b30100cc8
    committed review          f5adaf6ea23a22a5b6e4ab1ec8d4aeb8fd28c00e595921c679cc489b30100cc8   equal

The review's `Reviewed specification SHA-256:` field is filled in and reads
`9ba407bf136075ac23e76161cc0644f9fbe0d260c6ad135edf3c6d900e399576` — **the
digest of the specification actually committed and executed.** Committed
unedited, per Rule 18, and **before the merge**, per Rule 15's timing clause.

---

## 4. Merge parentage — A3, four distinct SHAs

**Three parentage values, each derived by a different method before the merge
existed, plus the evidence base:**

| Value | Method | MEASURED |
|---|---|---|
| parent 1 | `git rev-parse HEAD` on the branch tip after commit 2 | `3e802576e94767efa5bd7ba1a9b62c654d665493` |
| parent 2 | `git rev-parse 8ff032e7…^{commit}` | `8ff032e7f90ecfce4666fac34691b5670016bb75` |
| merge-base | `git merge-base HEAD 8ff032e7…` | `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab` |
| evidence base | `git rev-parse e3ce8063…` | `e3ce80639337956af5f934f7530d3b2476e5f6c1` |

**All four are distinct**, which is the shape a stale-base merge has:

    merge-base != parent 1        YES
    merge-base != parent 2        YES
    merge-base != evidence base   YES   ← the stale base; in the P7 integration these two were equal

**Commit 1 is an ancestor of parent 1:** `git merge-base --is-ancestor
183cc8a7… 3e802576…` → **exit status 0**.

**Confirmed against the merge commit as stored:**

    git rev-list --parents -n 1 HEAD
    86e3c84d…  3e802576…  8ff032e7…

**A fifth, independent derivation from the checker.** `P5` recomputes
parentage from the merge and reports the same three values with
`merge_base_equals_parent_1: false`.

---

## 5. The conflict list — A4, MEASURED

    Auto-merging derivations/GOVERNANCE-ENFORCEMENT_classification.md
    Auto-merging scripts/governance_tools/task_checker.py
    Auto-merging tests/test_task_checker.py
    Automatic merge went well; stopped before committing as requested

    git diff --name-only --diff-filter=U      (no output)
    unmerged path count                       0
    git ls-files -u | wc -l                   0

**Empty.** **Additionally, MEASURED tree-wide over every tracked file at
commit 3:** a search for conflict markers at line start returns **0 hits**,
over all tracked paths with no directory exclusion.

### 5.1 §9's inspection of the auto-merge, before it was committed

**§9 requires a STOP if the auto-merge produced anything I would want to
adjust.** I inspected it before committing:

    conflict markers in the three merged files          0
    merged task_checker.py parses as valid Python       yes
    merged task_checker.py imports cleanly              yes
    duplicated definitions after the merge              none — SCOPE_KEYS, parse_scope_block,
                                                        check_p1, GATE_HEADING, RAW_GATE_HEADING,
                                                        gate_sections, raw_gate_headings and
                                                        check_p7 each appear exactly once

**There was nothing I would want to adjust, so nothing was adjusted and no
stop arose.** **No merge result was hand-edited.**

---

## 6. Scope — A5

**MEASURED at commit 3, the merge commit:**

    M  derivations/GOVERNANCE-ENFORCEMENT_classification.md
    A  reports/2026-08-12T2015Z_p1-declared-total.md
    A  reviews/chatgpt/2026-08-12T2015Z_p1-declared-total.md
    A  reviews/chatgpt/2026-08-14T1125Z_integrate-p1-declared-total.md
    M  scripts/governance_tools/task_checker.py
    A  specs/2026-08-12T2015Z_p1-declared-total.md
    A  specs/2026-08-14T1125Z_integrate-p1-declared-total.md
    M  tests/test_task_checker.py

    additions 5   modifications 3   deleted/renamed/copied/type-changed/unmerged/unknown 0
    total changed paths 8

**INTENDED at commit 4:** 6 additions and 3 modifications — the eight above
plus `reports/2026-08-14T1125Z_integrate-p1-declared-total.md`, giving A5's
manifest of nine paths.

**Both figures with the head each was measured at: 5/3 at commit 3
`86e3c84d…`, MEASURED; 6/3 at commit 4, INTENDED.**

    8   changed paths at the merge commit
    6   contributed by source branch 8ff032e7…   ← what A6 compares
    2   authored here and present at the merge   (this specification, this review)
    3   authored here in total, the third being the report at commit 4

---

## 7. Source-branch artifacts — A6

**The six were DERIVED from the source branch —
`git diff --name-status 1cb5550f 8ff032e7` — not read from the
specification's list**, and the derivation returned exactly six, agreeing
with A5's split of three added and three modified. **No disagreement to
report.**

### 7.1 The three source ADDITIONS — blob-identical to the source tip

    reports/2026-08-12T2015Z_p1-declared-total.md           d8969a05b2e9caf84b5648f0d3040d5f67338f7b   IDENTICAL
    reviews/chatgpt/2026-08-12T2015Z_p1-declared-total.md   a47dcdcb98ed00298ef1af01fdf1778ffd48e53c   IDENTICAL
    specs/2026-08-12T2015Z_p1-declared-total.md             0ddad4310063b5e04e8f04087ed4b41ee54489fd   IDENTICAL

### 7.2 The three AUTO-MERGED files — three-way blob report

**Each merged blob must differ from BOTH sides; a merged blob equal to either
would mean that side's change was lost.**

| Path | source tip `8ff032e7` | `main` `e3ce8063` | merged `86e3c84d` | differs from both? |
|---|---|---|---|---|
| `derivations/GOVERNANCE-ENFORCEMENT_classification.md` | `d966db0cf651dc157953936c44a79e3746982715` | `74fc207423f1a7f91f3249d187f3155773124332` | `99b1314ee3592ed64aaafa6a4530cb4afc2c7755` | **YES / YES** |
| `scripts/governance_tools/task_checker.py` | `1b17dfa1ffee42f8c66e4c569c1498f25778986b` | `b41a5b34728339829420174ab02b809a3d55f483` | `3dfe6498e7c369c5ea1277204861fcd3436ac41a` | **YES / YES** |
| `tests/test_task_checker.py` | `8970bfebe42dd92712f9eb69850fcc6d057214f8` | `7d71230869f0f9d6e8977179c318ba78554daf4c` | `9b7d43e43b3409f066dd56fe6b15702cd6c7d9de` | **YES / YES** |

**All three differ from both sides.** **That is what an auto-merge of two
real changes looks like.**

### 7.3 A stronger check than A6 asks for, because blob inequality is weak evidence

**A merged blob differing from both parents shows only that it is not
identical to either.** It does not show that both sides' content is present.
**So I measured line survival directly**, taking each side's lines added over
the merge-base `1cb5550f…` and asking whether each is present in the merged
file:

    scripts/governance_tools/task_checker.py    source added  90   present  90   missing 0
                                                main   added  57   present  57   missing 0
    tests/test_task_checker.py                  source added 104   present 104   missing 0
                                                main   added 133   present 133   missing 0
    derivations/GOVERNANCE-ENFORCEMENT_…md      source added  24   present  24   missing 0
                                                main   added  61   present  61   missing 0

**Not one line from either side is missing from any of the three files.**
**This is a set-membership check on lines and is not proof of correct
interleaving** — A7 and A11 are what test behaviour — but it closes the
specific failure A6 is aimed at far more tightly than blob inequality does.

---

## 8. Both repairs survive — A7, MEASURED at the merge commit

**All six from one measurement session, importing the merged module:**

    1. raw '^## P2-' count                 14      expected 14
    2. GATE_HEADING parsed count           14      expected 14
    3. equality holds                      True    expected true
    4. RAW_GATE_HEADING present            True    expected yes
    5. the declared-total grammar present  True    expected yes
    6. parse_scope_block reads 'stated:'   True    expected yes

    SCOPE_KEYS = ('stated', 'base', 'head', 'mode', 'add', 'modify', 'forbidden_operations')

**Item 6 was exercised, not merely name-checked.** I fed
`parse_scope_block` a synthetic block declaring `stated: 2 additions, 1
modification` over a two-add / one-modify manifest and read the result:

    {'parse': 'OK', 'counted': 3, 'counted_add': 2, 'counted_modify': 1,
     'stated_record': 'stated: 2 additions, 1 modification',
     'stated_add': 2, 'stated_modify': 1, 'stated': 3}

**It reads the declared total per category.** **A grep for the string
`stated` would have passed even if the parser were broken**, which is why the
check runs the function.

**Neither repair was lost. No stop.**

---

## 9. `P1` over the whole corpus — A8, MEASURED at the merge commit

**Status counts over every `.md` file under `specs/`:**

    PASS            13
    NOT_PARSEABLE   37
    FAIL             0
    ------------------
    corpus          50

**`FAIL` files: none.** **A `FAIL` would have meant a document declares a
total that disagrees with its own manifest**, and there is none.

**The corpus arithmetic, MEASURED, because the specification's figures were
taken at the evidence base and the merge changes them:**

    at the evidence base e3ce8063   48 files, 11 carrying a 'stated:' key
    at the merge commit             50 files, 13 carrying a 'stated:' key
    the two added                   the arriving source specification, and this task's own

**13 `PASS` equals exactly the 13 files carrying the key.** The
specification expected *"roughly a dozen"*; thirteen is what I measured.

**The 37 `NOT_PARSEABLE` results carry THREE distinct reasons, not one.** I
drafted "every one carries the same reason", then counted them and it was
false:

    29   no 'stated:' record in the scope block     — has a manifest, declares no total
     6   0 'add:' records                           — no scope block at all
     2   2 'add:' records                           — two scope blocks; the grammar
                                                      refuses to choose between them

**The distinction matters for reading the number.** Only the 29 are
"specifications the repair could cover once they declare a total". **The six
with no scope block were never in `P1`'s reach**, and **the two with two
`add:` records are a different defect** — an ambiguity the grammar correctly
declines to resolve rather than a missing declaration. **A single headline
figure of 37 would have obscured all three.**

**The full table follows, with the reason for each.**

    A8 -- the integrated P1 over every .md under specs/, at the merge commit
    head: 86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f
    corpus size: 50
    
      specs/2026-08-06T0456Z_role-model-and-executors.md                     NOT_PARSEABLE  2 'add:' records
      specs/2026-08-06T1218Z_role-model-clean-rebuild.md                     NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-06T2307Z_role-model-raw-evidence-and-integration.md      NOT_PARSEABLE  2 'add:' records
      specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md          NOT_PARSEABLE  0 'add:' records
      specs/2026-08-07T1159Z_grassmann-crossing-sign.md                      NOT_PARSEABLE  0 'add:' records
      specs/2026-08-07T1320Z_integrate-fierz-and-sign-ruling.md              NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-07T1424Z_freeze-checker-sign-repair.md                   NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-07T1437Z_branch-deletion-policy.md                       NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-07T1508Z_branch-deletion-policy-amendment.md             NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-07T2158Z_integrate-freeze-repair-and-deletion-policy.md  NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-08T1321Z_channel-character.md                            NOT_PARSEABLE  0 'add:' records
      specs/2026-08-08T1354Z_normalisation-audit.md                          NOT_PARSEABLE  0 'add:' records
      specs/2026-08-08T1427Z_integrate-channel-character-and-audit.md        NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-08T1634Z_exponent-mapping-ruling.md                      NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-08T1702Z_integrate-exponent-mapping-ruling.md            NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-08T2350Z_generator-sum-criticality.md                    NOT_PARSEABLE  0 'add:' records
      specs/2026-08-09T0059Z_integrate-generator-sum-criticality.md          NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-09T0300Z_attraction-ruling-and-layers.md                 NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-09T0346Z_integrate-attraction-and-layers.md              NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-09T1653Z_land-rules-14-15.md                             NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-09T1711Z_integrate-rules-14-15.md                        NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-09T1801Z_land-amendments-e-to-l.md                       NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-09T1849Z_integrate-amendments-e-to-l.md                  NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-09T1958Z_pi-decisions-v3.md                              NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-09T2036Z_integrate-pi-decisions-v3.md                    NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-09T2153Z_si1-deferred-02-crossref.md                     NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-10T0113Z_integrate-si1-crossref.md                       NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-10T0245Z_diquark-both-eta.md                             NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-10T1112Z_diquark-adjudication.md                         NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-11T1134Z_chirality-census.md                             NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-11T1239Z_integrate-chirality-census.md                   NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-11T2207Z_land-diquark-line.md                            NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-12T0131Z_supply-protocol-v3.md                           NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-12T0409Z_integrate-supply-protocol-v3.md                 NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-12T1122Z_land-supply-protocol-v3.md                      NOT_PARSEABLE  0 'add:' records
      specs/2026-08-12T1256Z_governance-enforcement.md                       NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-12T1919Z_integrate-enforcement-checks-v2.md              NOT_PARSEABLE  no 'stated:' record in the scope block
      specs/2026-08-12T2015Z_p1-declared-total.md                            PASS           
      specs/2026-08-12T2258Z_adopt-parameter-domain.md                       PASS           
      specs/2026-08-12T2326Z_adopt-domain-repair.md                          PASS           
      specs/2026-08-13T0034Z_adopt-domain-labels.md                          PASS           
      specs/2026-08-13T0150Z_c1-complement-provenance.md                     PASS           
      specs/2026-08-13T0307Z_c3-curvature-asymmetry.md                       PASS           
      specs/2026-08-13T0740Z_adopt-admissibility-contract.md                 PASS           
      specs/2026-08-13T1149Z_integrate-phase01-line.md                       PASS           
      specs/2026-08-13T1239Z_ac4-symmetry-goldstone.md                       PASS           
      specs/2026-08-13T1424Z_integrate-ac4.md                                PASS           
      specs/2026-08-14T0325Z_p7-repair-and-pin-validator.md                  PASS           
      specs/2026-08-14T0511Z_integrate-p7-repair.md                          PASS           
      specs/2026-08-14T1125Z_integrate-p1-declared-total.md                  PASS           
    
    status counts:
      NOT_PARSEABLE  37
      PASS           13
    
    FAIL files: none

---

## 10. Evidence about the source task's `A10` — A9, and NOT its discharge

### 10.1 The statement A9 requires, in the words it requires

**The source task's `A10` remains undischarged, and neither A9a nor A9b
discharges it.**

**A criterion is discharged by the task that carries it, over that task's own
range, under its own review.** The source task stopped at its `A10` and its
report records that STOP. **That record stands.** **Nothing below changes it,
and nothing below should be quoted as if it did.**

**If the runs pass, the correct statement is: "the source task's `A10` would
pass today under a config it was not given."** **Not: "`A10` is
discharged."** Both runs did pass, so that is the statement I am making.

**Why they pass now and did not then, MEASURED.** The source task's `RUN 2`
returned `INCOMPLETE` at exit 2 with no property failed, because `P3` and
`P7` reported `NOT_DECLARED`. **Both causes were addressed elsewhere, not
here:**

    P3   its declared set is now named in every specification's config, ["DECISION_LOG.md"].
         In A9a it reports PASS with DECISION_LOG.md byte-identical base to head,
         89541 bytes at both.
    P7   repaired and landed at e3ce8063. In A9a it reports PASS with
         section_count 14/14 over raw 14/14.

**The old range's `GATES.md` is a different blob from today's**
(`849a4fbfe62d6478f092a84b0175357a74bbbb06` at `1cb5550f…`, `f02a7116…` and
`8ff032e7…`, against `2b3bd506…` now) **but carries the same fourteen
headings**, so the repaired `P7` reads it correctly too. **That is measured,
not assumed** — a different heading count over the old range would have made
these runs harder to interpret.

### 10.2 A9a — base `1cb5550f…`, head `f02a7116…` — **EVIDENCE**

**The exact range the source task's original `A10` governed.** Its head is
the source task's commit 4, **not the branch tip.**

    exit status                 0
    overall                     PASS
    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 NOT_APPLICABLE
    P6 PASS   P7 PASS   P8 PASS   P9 NOT_APPLICABLE

### 10.3 A9b — base `1cb5550f…`, head `8ff032e7…` — **EVIDENCE**

**The range the source task's `A10-final` governed**, ending at its report.

    exit status                 0
    overall                     PASS
    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 NOT_APPLICABLE
    P6 PASS   P7 PASS   P8 PASS   P9 PASS

### 10.4 Do A9a and A9b agree? — and where they differ

**They agree on every verdict that both evaluate, and they differ in exactly
one property, in exactly the way the report commit predicts.**

    commits_in_range                    A9a 4        A9b 5
    commits_on_first_parent_line        A9a 4        A9b 5
    P9   reports carry "Stops and clarifications"
                                        A9a NOT_APPLICABLE   "range adds no report"
                                        A9b PASS             reports/2026-08-12T2015Z_p1-declared-total.md,
                                                             heading_present: true
    P8   reports_added                  A9a []       A9b ["reports/2026-08-12T2015Z_p1-declared-total.md"]
    P6   per-commit hygiene             A9b carries one extra commit record, 8ff032e7…, matches []

**No other property differs, and no verdict flips from pass to fail or back
in either direction.** **The difference IS the report commit and nothing
else**, which is what makes the counterfactual informative rather than
misleading: A9a measures the criterion that actually stopped, and A9b
measures its final variant, and they say the same thing about `P1`, `P3` and
`P7`.

### 10.5 A9a output, verbatim — **EVIDENCE, not a discharge**

    {
      "base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
      "commits_in_range": 4,
      "commits_on_first_parent_line": 4,
      "head": "f02a71163c46e205df4a29277c72d851a59777a8",
      "overall": "PASS",
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
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 4,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

### 10.6 A9b output, verbatim — **EVIDENCE, not a discharge**

    {
      "base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
      "commits_in_range": 5,
      "commits_on_first_parent_line": 5,
      "head": "8ff032e7f90ecfce4666fac34691b5670016bb75",
      "overall": "PASS",
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
              },
              {
                "adds_review": false,
                "commit": "8ff032e7f90ecfce4666fac34691b5670016bb75",
                "work_paths": []
              }
            ],
            "first_review_commit": "ec4de78e3849219086a91c699df14db94a3bc1ad",
            "first_work_commit": "bb59c4b14447f8d23cb1f5128cdc5e865bdf0d99",
            "in_scope": 5,
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
            },
            {
              "commit": "8ff032e7f90ecfce4666fac34691b5670016bb75",
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
            "first_commit": "d9a8ba6b00987feafd5eb4b070a83c1f95b4c78c",
            "first_commit_paths": [
              "specs/2026-08-12T2015Z_p1-declared-total.md"
            ],
            "reports_added": [
              "reports/2026-08-12T2015Z_p1-declared-total.md"
            ],
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
          "evidence": [
            {
              "heading_present": true,
              "path": "reports/2026-08-12T2015Z_p1-declared-total.md",
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
        "commits_in_scope": 5,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

---

## 11. The checker over this task's own range — A10, MEASURED at commit 3

    base   e3ce80639337956af5f934f7530d3b2476e5f6c1
    head   86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f   (commit 3, the merge commit)

**Both prospectivity readings for each of the two runs, so four invocations.
All four exited 0 with `overall: PASS`.**

    run 1 INCLUSIVE   exit 0   PASS   sha256 1f2ae4a04b802e548fbc594212d68d12dc75fa7456e8c918121b8d65f152baa8
    run 1 EXCLUSIVE   exit 0   PASS   sha256 08c5ba4ab1b81ba8c6d19781c89de2cf988706162f563e7b5b32e44ec8c39972
    run 2 INCLUSIVE   exit 0   PASS   sha256 077c6e0488a0df07c744304410a5deb1b26e84bf68705cf4911bb91ba66b0371
    run 2 EXCLUSIVE   exit 0   PASS   sha256 ffc22e5bac4be4fe09562d98fe935cb27397d81bd6793ccdf2dcbc73393f7999

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 PASS
    P6 PASS   P7 PASS   P8 PASS   P9 PASS

**The A9 digests, for completeness:**

    A9a INCLUSIVE   22d3126ce73bf09d0abfa118ae86e80c153ab07515e0f6603e00a8b86679b6d9
    A9a EXCLUSIVE   02fe0da3645e62767b21ef48f3e560e4429306fede54c8384d4c41b05ff418dc
    A9b INCLUSIVE   7fa1bb9f60a32fc1b1f0e0819118407f039c9064c3e2dab6e409ece0e3fe97d5
    A9b EXCLUSIVE   f99c497fb4fcadbdcf4d636ebe0ec88a278aba78b2d84926205648cf7b5ab9f5

### 11.1 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "e3ce80639337956af5f934f7530d3b2476e5f6c1",
      "head": "86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 11.2 RUN 2 config, verbatim — stop-governing

    {
      "base": "e3ce80639337956af5f934f7530d3b2476e5f6c1",
      "head": "86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f",
      "specification_paths": ["specs/2026-08-14T1125Z_integrate-p1-declared-total.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I supplied of my own choosing; all are
taken from A9 and A10.** **`append_only_paths` is `["DECISION_LOG.md"]` and
not `[]`**, so `P3` is live. **`authorised_modified_gates` is `[]`, and here
that is truthful: no gate may change.** **The config was never adjusted to
make RUN 2 pass; it passed on its first invocation.**

**The same config, less `specification_paths`, was used for A9a and A9b, as
§4 requires.**

### 11.3 The measured RUN 1 subject set

**RUN 1's default selection chose TWO specifications**, because the merge
brings the source task's own into the range:

    specs/2026-08-12T2015Z_p1-declared-total.md              "stated: 3 additions, 3 modifications"
       stated add 3 modify 3   counted add 3 modify 3   parse OK
    specs/2026-08-14T1125Z_integrate-p1-declared-total.md    "stated: 6 additions, 3 modifications"
       stated add 6 modify 3   counted add 6 modify 3   parse OK

**RUN 2 names only the second**, as A10 requires. **This is a real difference
and not a formatting one, so both JSON outputs are given verbatim below.**
The two prospectivity readings differ in exactly one line and in no verdict:

    291c291
    <         "inclusivity": "INCLUSIVE",
    ---
    >         "inclusivity": "EXCLUSIVE",

### 11.4 `P1` parses its own `stated:` line — and this is the repair, visible

**A10 requires `P1` to parse this specification's own `stated:` line:
`6 additions, 3 modifications` against a nine-path manifest. MEASURED:**

    stated_record   "stated: 6 additions, 3 modifications"
    stated_add      6        counted_add      6
    stated_modify   3        counted_modify   3
    counted         9        parse            OK

**Compare what `P1` reported in the four preceding integration reports**, all
of which used the pre-repair grammar:

    the P7 integration      counted 10 / stated 10     for a manifest declaring "7 additions, 3 modifications"
    the P7 repair task      counted  7 / stated  7     for "4 additions, 3 modifications"
    the AC-4 integration    counted 10 / stated 10     for "7 additions, 0 modifications"

**Those reported a bare total. This one compares per category.** **A manifest
with six additions and three modifications that declared "3 additions, 6
modifications" would have totalled nine and passed the old grammar; it
fails the new one.** **That is the repair, and it is visible in this task's
own output rather than only in a fixture.**

### 11.5 `P7`, running over a range that modifies no gate

**MEASURED, identical in all four invocations:**

    raw_heading_count_base   14        section_count_base   14
    raw_heading_count_head   14        section_count_head   14
    unauthorised_changed     []        added_sections  []    removed_sections  []

**`PASS` at fourteen sections. `PASS` at zero would have been a STOP.**

### 11.6 RUN 1 output, verbatim

    {
      "base": "e3ce80639337956af5f934f7530d3b2476e5f6c1",
      "commits_in_range": 8,
      "commits_on_first_parent_line": 3,
      "head": "86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f",
      "overall": "PASS",
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
            },
            {
              "counted": 9,
              "counted_add": 6,
              "counted_modify": 3,
              "counted_set": [
                "reports/2026-08-12T2015Z_p1-declared-total.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-p1-declared-total.md",
                "reviews/chatgpt/2026-08-12T2015Z_p1-declared-total.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-p1-declared-total.md",
                "specs/2026-08-12T2015Z_p1-declared-total.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-p1-declared-total.md",
                "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                "scripts/governance_tools/task_checker.py",
                "tests/test_task_checker.py"
              ],
              "parse": "OK",
              "path": "specs/2026-08-14T1125Z_integrate-p1-declared-total.md",
              "stated": 9,
              "stated_add": 6,
              "stated_modify": 3,
              "stated_record": "stated: 6 additions, 3 modifications"
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
                "commit": "183cc8a78076ce8e543f2229eb936b4bdc6e78ba",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "3e802576e94767efa5bd7ba1a9b62c654d665493",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f",
                "work_paths": [
                  "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                  "scripts/governance_tools/task_checker.py",
                  "tests/test_task_checker.py"
                ]
              }
            ],
            "first_review_commit": "3e802576e94767efa5bd7ba1a9b62c654d665493",
            "first_work_commit": "86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f",
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
              "merge": "86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
              "recomputed_parent_1": "3e802576e94767efa5bd7ba1a9b62c654d665493",
              "recomputed_parent_2": "8ff032e7f90ecfce4666fac34691b5670016bb75",
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
              "commit": "183cc8a78076ce8e543f2229eb936b4bdc6e78ba",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "3e802576e94767efa5bd7ba1a9b62c654d665493",
              "matches": [],
              "status": "PASS"
            },
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
            },
            {
              "commit": "8ff032e7f90ecfce4666fac34691b5670016bb75",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f",
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
            "first_commit": "183cc8a78076ce8e543f2229eb936b4bdc6e78ba",
            "first_commit_paths": [
              "specs/2026-08-14T1125Z_integrate-p1-declared-total.md"
            ],
            "reports_added": [
              "reports/2026-08-12T2015Z_p1-declared-total.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-14T1125Z_integrate-p1-declared-total.md",
              "reviews/chatgpt/2026-08-12T2015Z_p1-declared-total.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-14T1125Z_integrate-p1-declared-total.md",
              "specs/2026-08-12T2015Z_p1-declared-total.md"
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
              "path": "reports/2026-08-12T2015Z_p1-declared-total.md",
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

### 11.7 RUN 2 output, verbatim

    {
      "base": "e3ce80639337956af5f934f7530d3b2476e5f6c1",
      "commits_in_range": 8,
      "commits_on_first_parent_line": 3,
      "head": "86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "counted": 9,
              "counted_add": 6,
              "counted_modify": 3,
              "counted_set": [
                "reports/2026-08-12T2015Z_p1-declared-total.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-p1-declared-total.md",
                "reviews/chatgpt/2026-08-12T2015Z_p1-declared-total.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-p1-declared-total.md",
                "specs/2026-08-12T2015Z_p1-declared-total.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-p1-declared-total.md",
                "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                "scripts/governance_tools/task_checker.py",
                "tests/test_task_checker.py"
              ],
              "parse": "OK",
              "path": "specs/2026-08-14T1125Z_integrate-p1-declared-total.md",
              "stated": 9,
              "stated_add": 6,
              "stated_modify": 3,
              "stated_record": "stated: 6 additions, 3 modifications"
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
                "commit": "183cc8a78076ce8e543f2229eb936b4bdc6e78ba",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "3e802576e94767efa5bd7ba1a9b62c654d665493",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f",
                "work_paths": [
                  "derivations/GOVERNANCE-ENFORCEMENT_classification.md",
                  "scripts/governance_tools/task_checker.py",
                  "tests/test_task_checker.py"
                ]
              }
            ],
            "first_review_commit": "3e802576e94767efa5bd7ba1a9b62c654d665493",
            "first_work_commit": "86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f",
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
              "merge": "86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
              "recomputed_parent_1": "3e802576e94767efa5bd7ba1a9b62c654d665493",
              "recomputed_parent_2": "8ff032e7f90ecfce4666fac34691b5670016bb75",
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
              "commit": "183cc8a78076ce8e543f2229eb936b4bdc6e78ba",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "3e802576e94767efa5bd7ba1a9b62c654d665493",
              "matches": [],
              "status": "PASS"
            },
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
            },
            {
              "commit": "8ff032e7f90ecfce4666fac34691b5670016bb75",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f",
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
            "first_commit": "183cc8a78076ce8e543f2229eb936b4bdc6e78ba",
            "first_commit_paths": [
              "specs/2026-08-14T1125Z_integrate-p1-declared-total.md"
            ],
            "reports_added": [
              "reports/2026-08-12T2015Z_p1-declared-total.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-14T1125Z_integrate-p1-declared-total.md",
              "reviews/chatgpt/2026-08-12T2015Z_p1-declared-total.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-14T1125Z_integrate-p1-declared-total.md",
              "specs/2026-08-12T2015Z_p1-declared-total.md"
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
              "path": "reports/2026-08-12T2015Z_p1-declared-total.md",
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

## 12. The suite — A11, MEASURED

    before, at the evidence base e3ce8063…     301 passed, 2 deselected
    after,  at the merge commit 86e3c84d…      310 passed, 2 deselected     exit 0

    delta   +9 passed,  deselected unchanged at 2

**The count MUST rise, and it did.** **What accounts for the +9, MEASURED
against the merge-base rather than estimated:**

    tests/test_task_checker.py, test functions
      at the merge-base 1cb5550f      42
      at the source tip 8ff032e7      51      the source added 9
      at main e3ce8063                52      the P7 line added 10
      at the merge commit             61      42 + 9 + 10 = 61, and 61 is what was measured

    61 - 52 = 9, which is exactly the suite delta.

**The +9 IS the source's own new tests being collected after the auto-merge.**
**That is precisely what A11 exists to confirm** — a count that had not moved
would have meant the source's tests were merged textually and not collected,
which is the failure an auto-merge of two test files can produce silently.

**Per-file, MEASURED:** `tests/test_task_checker.py` alone reports `61
passed`; `tests/test_gate_pins.py` alone reports `11 passed`.

---

## 13. `GATES.md`, pins, protected paths, gates — A12 to A15

### 13.1 A12 — `GATES.md` untouched, MEASURED

    evidence base e3ce8063…    2b3bd5069414f009e1a0466c4990db2949519bd8
    merged head   86e3c84d…    2b3bd5069414f009e1a0466c4990db2949519bd8

**Identical, and equal to the value A12 names.**

### 13.2 A13 — pins at the head, MEASURED

| # | line | Artifact | Declared | Measured | Verdict |
|---|---|---|---|---|---|
| 1 | 1017 | `derivations/P2-PHASE-01_microscopic_parameter_domain.md` | `4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214` | same | **MATCH** |
| 2 | 1040 | `derivations/P2-PHASE-01_input_admissibility_contract.md` | `e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3` | same | **MATCH** |

**Count found: 2.** **Both unchanged from the evidence base**, which follows
from §13.1 — `GATES.md` blob-identical means the declared values cannot have
moved — and from A14, which finds both pinned artifacts unchanged.
**Independently, the landed `tests/test_gate_pins.py` asserts the same thing
on every suite run and passed as part of the 310.**

### 13.3 A14 — protected paths, MEASURED

    paths existing at the evidence base                       383
    excluded as authorised modifications (A5's modify: list)    3
    compared                                                  380
    differing                                                   0

### 13.4 A15 — gate invariants, MEASURED at the merged head

    1.  ^## P2- section count                    14
    2.  P2-PHASE-01                              Status: PROPOSED   (line 973)
    3.  prerequisites                            ### Satisfied prerequisite — MICROSCOPIC PARAMETER DOMAIN        (line 1010)
                                                 ### Satisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT (line 1035)
                                                 zero occurrences of "### Unsatisfied prerequisite"
    4.  every Status: line vs the evidence base  diff empty — all 15 IDENTICAL

**No gate, gate status, prerequisite state or verdict changed.**

---

## 14. Superseded branches — A16, MEASURED before the advance

    52f65117   exit 1      ebd531ab   exit 1      40168469   exit 1
    7146a093   exit 1      10c260b9   exit 1      d64cd912   exit 1

**Exit 1 means NOT an ancestor, the required result, for all six.** **No
superseded-register entry was written; nothing is superseded by this task.**

---

## 15. Commits — A17, MEASURED for commits 1–3

    commit 1   183cc8a78076ce8e543f2229eb936b4bdc6e78ba   specs/2026-08-14T1125Z_integrate-p1-declared-total.md
    commit 2   3e802576e94767efa5bd7ba1a9b62c654d665493   reviews/chatgpt/2026-08-14T1125Z_integrate-p1-declared-total.md
    commit 3   86e3c84d2a5bdc73528bed39bff1ff7b8246fd3f   --no-ff merge of 8ff032e7…

    UTC token fixed by commit 1:  1125Z        day at execution: 14

**Stored subjects, MEASURED:**

    commit 1   spec: integrate the declared-total P1 grammar, and land it
    commit 2   review: pre-execution review for the P1 declared-total integration
    commit 3   merge: integrate the declared-total P1 grammar

| Commit | `Co-Authored-By` | session id or URL | tool attribution | Trailer suppressed? |
|---|---|---|---|---|
| 1 | none | none | none | **No — none was ever written** |
| 2 | none | none | none | **No — none was ever written** |
| 3 | none | none | none | **No — none was ever written** |

**Commit 4's message, INTENDED:**

    report: the declared-total P1 grammar lands on main

**Commit 4 is post-report evidence. Nothing in this report measures it.**

### 15.1 The harness, and §3's prohibition checked mechanically

**My harness's standing git guidance does instruct a `Co-Authored-By` trailer
and a session URL.** **Each message was composed without them at first
writing**; no commit was amended and no history was rewritten. `P6` reports
`PASS` on all three commits in every one of the four A10 invocations.

**§3 forbids claiming the source task's `A10` is discharged, in the report,
the commit messages, or anywhere else.** **MEASURED:** searching every commit
message in `e3ce8063..HEAD` for `discharg` returns seven hits, **and every
one is a denial or a statement of the principle.** From this task's own
commits:

    "The source task stopped at its own A10 and that criterion is not discharged here."
    "A criterion is discharged by the task that carries it, over its own range, under its own review."
    "…is evidence about a counterfactual, not a discharge."

**No affirmative discharge claim exists in any commit message in the range,
and none appears in this report.**

---

## 16. Rule 16 assessment — all four junctions

### 16.1 First — three checks now work; the enforcement gap is not closed

**After this lands, all three checks this line set out to repair are on
`main`: `P1`'s declared total, `P7`'s heading grammar and completeness
invariant, and the pin validator. A reader may take that for the enforcement
gap being closed. It is not.**

**MEASURED at the merged head: `derivations/GOVERNANCE-ENFORCEMENT_classification.md`
§5 is byte-identical to its value at the evidence base** — *"Twenty-two have
no machine behind them at all."* **`P1`, `P3` and `P7` all still read
`PARTIAL`** in the merged property table, which still carries exactly nine
rows.

**Three checks now work. That is the claim.**

### 16.2 Second — `P1`'s coverage did not grow; the corpus was written to suit it

**`P1`'s coverage will look like it grew, and saying which it is matters more
than the number.**

    when the repair was written    1 of 38 specifications carried a 'stated:' key
    at the evidence base          11 of 48
    at the merge commit           13 of 50

**It is the corpus having been written to suit the repair, not the repair
working better.** **Every specification issued since the repair was written
carries the key** — including this one and the four integration
specifications before it — **because their authors adopted the syntax, not
because the grammar reaches further back.** **The grammar's reach into the
older corpus is unchanged: 29 of the 37 `NOT_PARSEABLE` results are files
that have a manifest and declare no total, and the repair does not and cannot
read those.**

**A future report that quotes a rising `PASS` count as evidence of the
repair's quality would be misreading it**, and §9's three-way breakdown of
the `NOT_PARSEABLE` reasons is there so that the misreading is harder.

### 16.3 Third — the source task's `A10` is undischarged and stays that way

**Said in §10.1 in the words A9 requires, and repeated here because §8 asks
for it under Rule 16: the source task's `A10` remains undischarged, and
neither A9a nor A9b discharges it.** **A9's runs are evidence about a
counterfactual — what the repaired checker reports over that range, under a
config the task was not given — and are labelled EVIDENCE in §10.**

**The source task's report records a STOP. That record stands, and this
report does not amend, supersede or soften it.**

### 16.4 Fourth — two gate-heading grammars still coexist and still agree

**MEASURED at the merged head:**

    scripts/governance_tools/task_checker.py    GATE_HEADING                    -> 14 ids
    tests/test_repository_structure.py          ^##\s+(P2-[A-Z]+(?:-[A-Z]+)*-\d+) -> 14 ids
    agree                                        True
    symmetric difference                         empty

**They still agree.** **The agreement is MEASURED, not enforced.** **Nothing
in the repository compares them**, and they are not the same language: the
checker's requires a separator and a non-empty title and permits digits
inside the id; the structure test's requires the id to end in `-<digits>` and
ignores whatever follows. **A gate id such as `P2-FOO2-01` would parse under
one and not the other.**

**Not unified here, as §3 requires.** The unification, or an invariant test
requiring both to return the same id set, belongs to the conventions task.

---

## 17. Stops and clarifications

### 17.1 Stops

**None.** No stop was reached in any of the five primary categories:
`SPECIFICATION_DEFECT`, `ENVIRONMENT`, `OBSERVATION_METHOD_ERROR`,
`REPOSITORY_DEFECT`, `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`.

**Every stop condition the specification names was tested and none
triggered:** A1's refs matched and the merge-base is `1cb5550f…`; A2's review
names the executed digest; A4's conflict list is empty; A7 found both repairs
present with `P7` parsing fourteen of fourteen; A10's RUN 2 exited 0 with
`P7` at fourteen sections; A12 shows `GATES.md` byte-identical; A11's count
rose. **§9's "if the auto-merge produced anything you would want to adjust,
STOP" was tested explicitly (§5.1) and did not arise.**

### 17.2 Secondary findings

**S1 — `OBSERVATION_METHOD_ERROR` in the specification's descriptive figure,
minor, not blocking.** §1 and §11 say the source was cut *"five landings"*
behind. **MEASURED: six** merge commits on `main`'s first-parent line between
`1cb5550f…` and `e3ce8063…`, listed in §2. **Descriptive colour, not a
criterion**, and the governing fact is if anything understated. **I report it
rather than repeating "five" as though I had reproduced it.**

**S2 — observation, and it sharpens A8's number.** The 37 `NOT_PARSEABLE`
results carry **three** distinct reasons, not one (§9). **I drafted "every
one carries the same reason", counted, and it was false.** Only 29 are
files the repair could cover once they declare a total.

**S3 — carried forward, now a property of `main`.** Two gate-heading grammars
coexist and nothing keeps them agreeing (§16.4). **Measured as agreeing today
with an empty symmetric difference.** **Not unified here.**

**F1 and F2** — the harness's forbidden trailer and the `frozen Wilson D`
docstring at line 73 of the exploratory script. **Both met, both reported,
neither fixed**, as §3 requires. `scripts/p2_phase01_scalar_exploratory.py`
is among the 380 paths A14 found unchanged.

### 17.3 Does `main` now read as though the enforcement gap were closed?

**No, and the qualification below is the honest part of the answer.**

**MEASURED:** no file on `main` states the gap is closed; the
classification's §5 count is byte-identical; `P1`, `P3` and `P7` all read
`PARTIAL`; the property table still has nine rows.

**Where the residual risk lies.** **The suite now returns 310 where it
returned 280 three tasks ago, and `P1` now reports a real per-category
comparison instead of a bare total.** Both are improvements and both are
exactly the kind of signal a reader over-reads. **The rise from 301 to 310 is
nine tests about `P1`'s grammar — not nine more rules enforced.** **`P1`'s
`PASS` count over the corpus rose because specifications adopted a syntax,
not because coverage deepened** (§16.2).

**The mitigation on `main` is that the classification says so, in the same
file, in the entries this line has been editing.** **It is a document, not a
mechanism.** Nothing prevents the misreading.

### 17.4 Ambiguous, unsatisfiable, or what I would have specified differently

**Nothing was unsatisfiable, and no instruction was inconsistent with a
repository rule.** Three observations:

1. **A6 asks only that each auto-merged blob differ from both sides**, which
   is weak evidence: it rules out one side being taken wholesale and nothing
   more. **I added the line-survival check of §7.3** — every line each side
   added over the merge-base, checked for presence in the merged file, 0
   missing across all three files. **I would have specified that instead**,
   or as well; it is cheap and it closes the actual failure A6 names.
2. **A8 says "report the reason for each `NOT_PARSEABLE`" but expects a
   single headline count.** The reasons turned out to be three distinct
   kinds (§9). **I would have specified the breakdown by reason**, since the
   aggregate obscures which files the repair could ever reach.
3. **A9's two runs are correctly separated, and getting the head right was
   the whole point.** §2 says an earlier version named the tip, which would
   have measured `A10-final`'s range while claiming to measure `A10`'s.
   **Both are now run and reported separately, and §10.4 measures that the
   only difference is the report commit** — which is what makes the pair
   informative rather than a single number of uncertain provenance.

### 17.5 Rule 13

**No environment failure occurred, so neither of Rule 13's two diagnostic
orders was exercised.** **Rule 13 carrying two such orders remains a known
open item; I name neither as the one that applies.**

    Python   3.11.15
    pytest   9.1.1

**Nothing was installed.**

---

## 18. Evidence layering

**Committed in this report, MEASURED at commit 3:** A1–A9 and A11–A17 for
commits 1–3; A10's four invocations with both configs and both JSON outputs;
A9a's and A9b's outputs; commits 1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; A5's final
base-to-head scope of 6 additions and 3 modifications.

**Post-report evidence, returned to the Reviewer and NOT written back:** A5's
final scope measured base-to-commit-4; A10-final, being RUN 2 re-run at
commit 4 before the landing; A11 at commit 4; A13 and A16 re-run after the
advance; A17 for commit 4; the pre-advance `--is-ancestor` exit status; the
exact push command; remote `main` read back; the source tip unchanged; final
ancestry confirmation.

**Nothing in this report claims to measure commit 4.**
