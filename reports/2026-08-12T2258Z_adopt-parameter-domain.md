# Report — adopt the microscopic parameter domain, with evidence corrections

Specification: `specs/2026-08-12T2258Z_adopt-parameter-domain.md`
Review: `reviews/chatgpt/2026-08-12T2258Z_adopt-parameter-domain.md` — APPROVED FOR EXECUTION
Evidence base: `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`
Branch: `science/adopt-parameter-domain`, cut from that commit. **`main` was not touched.**

**Every figure is labelled MEASURED or INTENDED.** **Nothing here claims to
measure commit 5**, which does not exist while this file is written.

---

## 0. Executive summary

**The adoption is built as specified.** The source artifact digested to
`096220d1…` exactly. **All eight edit anchors were found verbatim, exactly once
each**; the diff carries **eight hunks and no other**. `GATES.md` changed in the
one authorised block; the two drafts each gained one pointer paragraph and lost
nothing. **A9's RUN 2 — the stop-governing run — PASSED, exit 0**, on both
prospectivity readings.

**`P2-PHASE-01` remains `PROPOSED`.** The `PHASE INPUT / ADMISSIBILITY
CONTRACT` prerequisite remains `UNSATISFIED` and its block is byte-identical.
**One prerequisite of a two-prerequisite gate moved. The gate is not ready.**

**`C1`, `C2` and `C3` were not answered, and
`scripts/p2_phase01_scalar_exploratory.py` was not read.**

**One STOP, and it is a governance conflict I did not resolve.** A7 orders a
modification of `derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md`.
**`GATES.md` pins that file by sha256 inside a registered gate**, and A6
forbids changing that block. **MEASURED: the pin now names `a3ec0cb6…` for a
file whose content is `e373efcb…`.** `CONVENTIONS.md` states that an executor
**MUST NOT** re-pin an artifact hash-pinned by a registered gate, so I cannot
repair it, and §8 tells me not to decide which instruction prevails. **I
executed A7 as specified and report the conflict.** Full statement in §11.
**This branch must not be integrated until that is ruled on**, because
integration is where the stale pin would reach `main`.

**A second finding, reported and left per §8's sixth-defect clause:** the
adopted artifact's H1 title still reads `— DRAFT FOR ADOPTION`, and the
sentence following the new `**Status: ADOPTED.**` still reads *"nothing here is
in force until that task lands."* §10 gives the text.

**P7 reported `PASS` and that is evidence of nothing.** §9.

---

## 1. A1 — Refs and inputs

**MEASURED.**

```
git ls-remote origin refs/heads/main
1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab	refs/heads/main

supplied source artifact  sha256
096220d188bcb9db2a2428dba7938c625215fec09b4ed46c879795cdeb13efba
required by §0 and A1
096220d188bcb9db2a2428dba7938c625215fec09b4ed46c879795cdeb13efba
EQUAL
```

**Both match. No STOP.** The specification and review also arrived **as files**
(Rule 18 satisfied on both); neither was pasted.

    supplied specification  adb850ccb07345e47f7079d7dc451fe78f42fcade3df2b57e3faf589bf2f3414
    supplied review         68e146a8e79b83584eb2488445f5dc413e0ad1951c605ab5bdaa924966f95e21

## 2. A2 — The review, committed unedited, with its digest field filled in

**MEASURED.** The review carries, at its head and again at its foot:

    Reviewed source artifact SHA-256: 096220d188bcb9db2a2428dba7938c625215fec09b4ed46c879795cdeb13efba

**It is filled in, not a placeholder, and it names the digest of the artifact
actually supplied.** A2's stop condition is not triggered.

    supplied review   68e146a8e79b83584eb2488445f5dc413e0ad1951c605ab5bdaa924966f95e21
    committed blob    68e146a8e79b83584eb2488445f5dc413e0ad1951c605ab5bdaa924966f95e21
    EQUAL

**This closes, for this task, the correspondence gap the source artifact
records as having already caused one stale review.** It closes it by practice,
not by rule: **no repository convention yet requires a review to carry a
digest**, and the review says so itself.

## 3. A3 — Pinned inputs at the evidence base

**MEASURED**, `git rev-parse 1cb5550f:<path>`, Git blob ids:

```
849a4fbfe62d6478f092a84b0175357a74bbbb06  GATES.md
158ab187f2576fd8f163cd3ad3b76b7b897e6fb5  derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
5f020f33a9230d1aaa7c98c79db49b1efcb822f6  derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
454e70182e3b5de4765a397c10caba88f894d35f  results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json
```

`GATES.md` matches A3's pinned value. **The other three A3 slots were
`<measure at 1cb5550f before use>` and are measured above.**

**Cross-check, MEASURED:** the sha256 of
`..._microscopic_parameter_domain_DRAFT.md` at the base is
`d8e154690e0b3d8131260a9ed0ce0ef804dd5652d21c022c6b29677b90d3eba4`, which is
exactly what the `GATES.md` block being replaced pinned. **The block A6
replaces was pinning the right file.**

**The results file is unmodified** — see A10.

## 4. A4 — The adopted artifact, and the eight edit operations

**MEASURED.**

    supplied file, before   096220d188bcb9db2a2428dba7938c625215fec09b4ed46c879795cdeb13efba
    adopted file, after     c27e57f080ecf8a2472a7f614aedcc19c5c72622650f6ddd0bc802d3fced5003

**The "after" digest is read from the COMMITTED BLOB at commit 3**, not from a
working-tree file, because A6 embeds it.

**EIGHT edit operations applied. Each OLD anchor was required to occur exactly
once; a count other than one was coded as an abort, not as a search for a near
match.** Every one matched:

    op 1  status header          1 match, substituted
    op 2  C-1                    1 match, substituted
    op 3  C-2                    1 match, substituted
    op 4  C-3                    1 match, substituted
    op 5  C-4 column header      1 match, substituted
    op 6  C-4 insertion          1 match, substituted
    op 7  C-5                    1 match, substituted
    op 8  §5 boundary insertion  1 match, substituted

    C-1 1  +  C-2 1  +  C-3 1  +  C-4 2  +  C-5 1
      +  §5 boundary 1  +  status header 1   =  8

**The count came out at eight. A4's stop is not triggered.**

## 5. A5 — Nothing else in the adopted text changed

**MEASURED: the diff carries EIGHT hunks, one per operation, and no other.**
Full diff:

```diff
@@ -1,6 +1,7 @@
 # `P2-PHASE-01` microscopic parameter domain — DRAFT FOR ADOPTION
 
-**Status: DRAFT FOR ADOPTION. Not adopted, not committed.** This artifact
+**Status: ADOPTED.** Adopted by
+`specs/2026-08-12T2258Z_adopt-parameter-domain.md`. This artifact
 is written for PI confirmation and reviewer scrutiny. **Adoption requires
 a task with its own specification and pre-execution review**; nothing
 here is in force until that task lands.
@@ -175,6 +176,10 @@
 **MEASURED.** Over all six grids and all sixteen couplings the two
 non-trivial roots sum to `−8` with `max |sum + 8| = 0.00e+00`.
 
+**The three examples below are from grid `n = 48`, `shift 0.0`; the
+five-decimal figures are not grid-independent.** The accounting that
+follows is over all six grids.
+
 **The accounting, because ninety is not six times sixteen:**
 
     96  grid-coupling points   (6 grids × 16 couplings)
@@ -221,7 +226,7 @@
 
 **MEASURED**, grid `n = 48`, shift `0.0`:
 
-    G/Gc    ordinary branch    complement branch    ratio
+    G/Gc    near-origin root   complement root      ratio
     0.80        -0.02259             0.41782        -18.5
     0.99        -0.00086             0.41127       -477.9
     1.01         0.00085             0.41757        492.6
@@ -229,6 +234,12 @@
     2.00         0.02440             0.17919          7.3
     3.00         0.02315             0.10475          4.5
 
+**Below `Gc` the near-origin root lies at NEGATIVE `Mhat`** — at
+`G/Gc = 0.80` the two non-trivial roots are `-0.41025` and
+`-7.58975`. **It is not the positive-mass condensate branch of
+§5c, which does not exist below `Gc`.** The column is named for
+position, not for sign, and §5b and §5c do not conflict.
+
 **The positions mirror exactly; the stability measure does not.** The
 ratio is not a constant: it diverges near `Gc`, because the ordinary
 branch's curvature passes through zero there while the complement's does
@@ -260,7 +271,11 @@
 the only computable option.** **That was wrong, and the error came from
 reading the deferred-item summary instead of the results file.**
 
-**MEASURED.** The ordinary branch shows a textbook transition:
+**MEASURED**, grid `n = 48`, `shift 0.0`; **the five-decimal figures
+are not grid-independent** — `+0.02134` reads `+0.02133` at
+`n = 32, shift 0.0` and `+0.02135` at `n = 48, shift 0.25`. **The
+qualitative pattern holds on all six.** The ordinary branch shows a
+textbook transition:
 
     G/Gc    trivial root curvature    non-trivial positive root
     0.80           +0.02134           none
@@ -328,6 +343,11 @@
   suspended `P2-BETAV-CIRC-01` result, and the historical Finding 5
   extraction remain excluded.
 
+**Adoption freezes the enumeration window and the treatment of
+inputs. It does not certify root completeness, full-space stability,
+thermodynamic dominance, negative-`G` exclusion, or finite-density
+coverage.**
+
 ## 8. Checks to commission with, or before, the first enumeration
 
 **RECOMMENDATION.** All three are cheap and all three are things this
@@ -337,9 +357,21 @@
 generating script. §5a cannot be interpreted until this is answered.
 
 **C2 — Does negative `G` admit any non-trivial root?** Stationarity is
-`1 = 2 G I0(Mhat)`. Every `I0` in the results file is positive
-(`0.02845` to `0.10670`). **A negative `G` therefore requires
-`I0(Mhat) < 0` somewhere, which no measurement has tested.** If `I0` is
+`1 = 2 G I0(Mhat)`. Every `I0` measured in the results file is
+positive. **The brackets, with their scope stated:** the root-level
+`I0` values span `0.0284403` to `0.1067275` over all six grids;
+on the single grid `n = 48`, `shift 0.0` they span `0.0284534` to
+`0.1067006`; across every `I0`-valued field in the file the upper
+bound reaches `0.1439968`. **An earlier version of this artifact
+quoted the single-grid bracket as if it covered the file.**
+
+**Partial negative-mass evidence already exists and was overlooked.**
+The file's `symmetry.sign_pairs` evaluates `I0` at
+`Mhat = -0.1, -0.5, -1.0`, giving `0.09046`, `0.11173`, `0.14400` —
+**all positive, at negative mass.** **So it is not true that no
+measurement has tested the sign there.** What has not been
+established is **global** non-negativity over the admissible mass
+domain, and a negative `G` requires `I0(Mhat) < 0` somewhere in it. If `I0` is
 positive everywhere, the negative-`G` half-line is empty and the domain's
 restriction to positive `G` would be derived rather than assumed.
 
@@ -371,6 +403,19 @@
 
 **`OPEN-AC-1` — the P/V/A/T construction.** Unchanged and untouched.
 
+**`OPEN-AC-4` — exact/remnant symmetry and Goldstone implications.**
+**REMAINS OPEN.** **An earlier version of this artifact omitted it
+entirely.** It bears on stability and therefore on any later upgrade
+of a candidate to a phase; **it is not a peripheral item and it is
+not addressed here.**
+
+**`OPEN-AC-5` — whether `Mhat = 1` is an admissibility bound.**
+**CLOSED, by the same answer that closes `OPEN-PD-1`: NO.** The two
+are the same question recorded in two artifacts. **An earlier
+version of this one answered `OPEN-PD-1` and was silent on its
+twin**, which is how a reader of the admissibility contract would
+have gone on believing the question undecided.
+
 **`OPEN-AC-3` — cross-family comparison.** Unchanged and untouched. Note
 that comparing the two branches' depths, as distinct from their
 curvatures, would need the common normalisation this item covers.
```

**Every hunk corresponds to §4, §5 or the status header. No unlisted hunk. A5's
stop is not triggered.**

**Two residual wordings, reported and LEFT, per §8's *"if you find a sixth
defect, report it and leave it"*.** Neither is inside §4 or §5, so correcting
either would have been an unauthorised edit:

**(a) The H1 title still says the file is a draft.** MEASURED, the adopted
file's first six lines:

    # `P2-PHASE-01` microscopic parameter domain — DRAFT FOR ADOPTION

    **Status: ADOPTED.** Adopted by
    `specs/2026-08-12T2258Z_adopt-parameter-domain.md`. This artifact
    is written for PI confirmation and reviewer scrutiny. **Adoption requires
    a task with its own specification and pre-execution review**; nothing
    here is in force until that task lands.

**A reader opening the adopted artifact meets "DRAFT FOR ADOPTION" in the
title and "nothing here is in force until that task lands" three lines under a
status that says ADOPTED.** The status line is correct; its neighbours
contradict it. **The specification's §4 anchored only the bold status
sentence.**

**(b) `**It supersedes nothing.**`** remains at line 9. After A6 the adopted
artifact does supersede the earlier draft — `GATES.md` now calls that draft
"Superseded draft" and A7 stamps `**SUPERSEDED.**` into it. **The sentence was
true of the draft and is false of the adopted file.**

**Both are wording, not evidence.** No measurement, ruling or decision is
affected. **A follow-up task correcting the title and those two sentences would
be a typo-class change; I did not make it here.**

## 6. A6 — The `GATES.md` edit

**MEASURED. The block replaced, verbatim as it stood at `1cb5550f`:**

    ### Unsatisfied prerequisite — MICROSCOPIC PARAMETER DOMAIN
    Artifact state: **DRAFTED / NOT ADOPTED**. Prerequisite state:
    **UNSATISFIED**. Owner: Paper 2. Canonical label: **MICROSCOPIC PARAMETER
    DOMAIN**; not a gate ID. Draft:
    `derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`
    (sha256 `d8e154690e0b3d8131260a9ed0ce0ef804dd5652d21c022c6b29677b90d3eba4`).

    The future artifact must decide and bound scan-eligible coupling `G`, and must
    decide whether cutoff ratios and finite-density `μ` are FIXED INPUTS or SCAN
    DIMENSIONS. Any admitted scan dimension must carry a frozen range.

**Both anchors — the opening heading and the following
`### Unsatisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT` — occur
exactly once in `GATES.md`.** Full diff:

```diff
@@ -1007,16 +1007,30 @@ Governance clarification `P2-SI1-UNBLOCK-01` (2026-07-20): phase enumeration
 may proceed without consuming the historical Finding 5 value `−3.2(5)`
 (quarantined as unreproduced). It is not blocked by `P2-BETAV-CIRC-01`.
 
-### Unsatisfied prerequisite — MICROSCOPIC PARAMETER DOMAIN
-Artifact state: **DRAFTED / NOT ADOPTED**. Prerequisite state:
-**UNSATISFIED**. Owner: Paper 2. Canonical label: **MICROSCOPIC PARAMETER
-DOMAIN**; not a gate ID. Draft:
-`derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`
-(sha256 `d8e154690e0b3d8131260a9ed0ce0ef804dd5652d21c022c6b29677b90d3eba4`).
-
-The future artifact must decide and bound scan-eligible coupling `G`, and must
-decide whether cutoff ratios and finite-density `μ` are FIXED INPUTS or SCAN
-DIMENSIONS. Any admitted scan dimension must carry a frozen range.
+### Satisfied prerequisite — MICROSCOPIC PARAMETER DOMAIN
+Artifact state: **ADOPTED**. Prerequisite state: **SATISFIED**,
+per the PI ruling recorded in §3a of
+`specs/2026-08-12T2258Z_adopt-parameter-domain.md`.
+Owner: Paper 2. Canonical label: **MICROSCOPIC PARAMETER DOMAIN**;
+not a gate ID. Adopted artifact:
+`derivations/P2-PHASE-01_microscopic_parameter_domain.md`
+(sha256 `c27e57f080ecf8a2472a7f614aedcc19c5c72622650f6ddd0bc802d3fced5003`).
+Superseded draft:
+`derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`.
+
+The adopted artifact bounds the scan-eligible coupling `G` to
+`G/Gc` in `[0.80, 3.00]` over sixteen pre-registered values, and
+answers finite-density `μ` as a FIXED INPUT at `0`. **For the
+lattice spacing `a` it answers NEITHER fixed input nor scan
+dimension**: `a` is left unfixed because no quantity computed at
+this gate depends on it, and every quantity is dimensionless.
+**That is a third answer to this gate's binary question and is
+recorded as such.** No scan dimension is admitted without a frozen
+range.
+
+**Adoption freezes where to look. It certifies no phase**, no root
+completeness, no full-space stability, no thermodynamic dominance,
+no exclusion of negative `G`, and no finite-density coverage.
 
 ### Unsatisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT
 Artifact state: **DRAFTED / NOT ADOPTED**. Prerequisite state:
```

**A6's four required verifications, MEASURED:**

    '^## P2-' section count       base 14   head 14      UNCHANGED
    P2-PHASE-01 Status:           base PROPOSED  head PROPOSED
    all '^Status:' lines          15 base / 15 head, TEXT IDENTICAL
                                  (only line numbers shift by +14)
    ADMISSIBILITY CONTRACT block  byte-identical to base, still UNSATISFIED

**`GATES.md` changed in that block and nowhere else.**

**The `SATISFIED` rests on a ruling, not on this edit.** A6's replacement text
says so on its face — *"per the PI ruling recorded in §3a of
`specs/2026-08-12T2258Z_adopt-parameter-domain.md`"* — and I neither reached
nor evaluated that ruling. **The gate asks whether cutoff ratios and `μ` are
FIXED INPUTS or SCAN DIMENSIONS; the adopted artifact answers `μ` = FIXED
INPUT and answers `a` as NEITHER.** **That the third answer discharges the
prerequisite is the PI's ruling and the reviewer's approval of it, recorded as
such in the new block, and is not an executor judgement.**

## 7. A7 — The two pointer insertions

**MEASURED. Each was inserted immediately after the file's first heading line,
which was verified to be an H1 before writing.** Full diff:

```diff
--- a/derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
+++ b/derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
@@ -1,5 +1,17 @@
 # `P2-PHASE-01` phase input / admissibility contract — DRAFT, NOT ADOPTED
 
+**Cross-reference.** `OPEN-AC-2` is **RESOLVED FOR ENUMERATION**:
+the negative-mass branch is included as a candidate, and is NOT
+certified as admissible or stable, by the PI ruling recorded in
+`derivations/P2-PHASE-01_microscopic_parameter_domain.md`.
+`OPEN-AC-5` is **CLOSED** — `Mhat = 1` is NOT an admissibility
+bound — by the same answer that closes `OPEN-PD-1` in that artifact.
+`OPEN-AC-1`, `OPEN-AC-3` and `OPEN-AC-4` **remain OPEN**.
+
+**`RESOLVED FOR ENUMERATION` is not `CLOSED`, and the difference is
+the point.** `OPEN-AC-2` asks whether the branch is physical; the
+ruling answers only where it may appear in an enumeration.
+
 ## Status and evidence boundary
 
 This is a **DRAFT, NOT ADOPTED** prerequisite artifact.  It does not define an
diff --git a/derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md b/derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
index 158ab18..c7910bc 100644
--- a/derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
+++ b/derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
@@ -1,5 +1,9 @@
 # `P2-PHASE-01` microscopic parameter domain — DRAFT, NOT ADOPTED
 
+**SUPERSEDED.** Adopted as
+`derivations/P2-PHASE-01_microscopic_parameter_domain.md`. This file
+is retained as historical evidence and is not operative.
+
 ## Status and evidence boundary
 
 This is a **DRAFT, NOT ADOPTED** prerequisite artifact.  It does not define
```

**Nothing else in either file changed. No pre-existing `OPEN-AC` body text and
no pre-existing verdict was edited or replaced.** Each diff is a pure
insertion: **no `-` line in either hunk except the heading context.**

**`RESOLVED FOR ENUMERATION` is not `CLOSED`, and the inserted paragraph says
why.** `OPEN-AC-2` asks whether the negative-mass branch is physical; the PI
ruling answers only where it may appear in an enumeration. **The original
entries still read as they did, so the drafts continue to record the state they
recorded at the time.** That is the reason the specification insists on
insertion rather than editing, and it held.

## 8. A8 — Scope, and the commit order

**MEASURED — commits 1 to 4, in the order §7 specifies:**

    commit 1  8463dd7af73b425e8fd00e04ab8ef0fd168b8477  specs/2026-08-12T2258Z_adopt-parameter-domain.md
    commit 2  e76983e68b273470ee4cc788d1952c50eedb3a10  reviews/chatgpt/2026-08-12T2258Z_adopt-parameter-domain.md
    commit 3  5add3085d5cd139984100baba74d03f0b998a867  derivations/P2-PHASE-01_microscopic_parameter_domain.md
    commit 4  9ed98560249f98ae1a2762575b301dc6e6ad891a  GATES.md + the two drafts
    commit 5  INTENDED                                  reports/2026-08-12T2258Z_adopt-parameter-domain.md

**Commit 3 precedes commit 4 as required**, and A6's embedded digest
`c27e57f0…` was read from commit 3's committed blob, not from the working tree.

**The UTC token `2258` and the day `12` were MEASURED** (`date -u`) at the time
commit 1 was written, not chosen.

**The final scope, INTENDED** — commit 5 does not exist while this is written:

    stated: 4 additions, 3 modifications
    base: 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    head: <commit 5, INTENDED>
    mode: exact
    add:
      derivations/P2-PHASE-01_microscopic_parameter_domain.md
      reports/2026-08-12T2258Z_adopt-parameter-domain.md
      reviews/chatgpt/2026-08-12T2258Z_adopt-parameter-domain.md
      specs/2026-08-12T2258Z_adopt-parameter-domain.md
    modify:
      GATES.md
      derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
      derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths. MEASURED at commit 4: three of the four additions are in place
and all three modifications are; the fourth addition is this file.** **The
scope measured base-to-commit-5 is post-report evidence and is not claimed
here.**

## 9. A9 — The two checker runs, and what P7 is worth

Base `1cb5550f…`, head **commit 4** `9ed98560…`. **Both prospectivity readings
were run**, as A9 requires.

### RUN 1 — default subject selection, observational, governs nothing

```json
{
  "base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
  "head": "9ed98560249f98ae1a2762575b301dc6e6ad891a",
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
  "head": "9ed98560249f98ae1a2762575b301dc6e6ad891a",
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": ["P2-PHASE-01"],
  "register_path": "docs/BRANCHING_POLICY.md",
  "specification_paths": ["specs/2026-08-12T2258Z_adopt-parameter-domain.md"]
}
```

**The `EXCLUSIVE` variants are identical but for the one `inclusivity` field**;
MEASURED, the outputs differ in that one line and nowhere else.

**MEASURED results — all four runs `overall` PASS, exit 0:**

    RUN 1  INCLUSIVE  exit 0  PASS
    RUN 2  INCLUSIVE  exit 0  PASS      <- stop-governing
    RUN 1  EXCLUSIVE  exit 0  PASS
    RUN 2  EXCLUSIVE  exit 0  PASS      <- stop-governing

    P1 PASS  P2 PASS  P3 PASS  P4 PASS  P5 NOT_APPLICABLE
    P6 PASS  P7 PASS  P8 PASS  P9 NOT_APPLICABLE

**RUN 2's stop is not triggered.** Four commits in range, four on the
first-parent line, four in scope on both readings.

**What RUN 2 excluded: NOTHING.** **MEASURED: RUN 1's and RUN 2's JSON are
BYTE-IDENTICAL.** The range adds exactly one specification, so the default
selection already selects the file RUN 2 names. **I will not describe this
narrowing as having protected anything.**

**`P3` passed truthfully, not vacuously.** `append_only_paths` was
`["DECISION_LOG.md"]`, never `[]`. MEASURED evidence: `base_bytes` 89541,
`head_bytes` 89541, `base_is_byte_prefix_of_head` true, `deleted_lines` 0.
**An empty set would have turned this into `NOT_APPLICABLE` — the check
switched off rather than passed — and §8 forbids it.**

**`P1` passed under the OLD prose grammar.** This branch is cut from `main`,
which does not carry the declared-total repair, so P1 still reads the nearest
preceding count line. MEASURED: it selected the line
`stated: 4 additions, 3 modifications` and read `4 + 3 = 7` from it as prose,
against a counted set of 7. **It reached the right answer by reading a
structured declaration as a sentence.**

### `P7` returned `PASS` and that is evidence of NOTHING

**MEASURED, from the run's own JSON:**

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

**`section_count_base` 0 and `section_count_head` 0 against a file carrying
fourteen gates.** `GATE_HEADING` is `^## (P2-[A-Z0-9-]+)\s*$`; every real
heading continues after the ID, as in
`## P2-PHASE-01 — Admissible stable condensed phase (the Ice)`. **The pattern
matches zero of fourteen.** P7 compared two empty maps and returned `PASS`.

**This task really does modify `GATES.md`, which is what makes the vacuous
green dangerous here.** **A gate section could have been rewritten, added or
removed and P7 would still have said `PASS`.** **P7 does not support the claim
that the edit stayed inside the authorised block.** That claim rests on §6's
verifications and §10's path-by-path comparison, which are direct measurements
of the file.

## 10. A10 — Protected paths, and A11 — commit-message hygiene

**A10, MEASURED at commit 4**, whole-tree `git ls-tree -r` blob comparison,
path by path:

    paths at base                    343
    paths at commit 4                346
    removed                          none
    added                              3   (spec, review, adopted artifact)
    changed                            3
    identical                        340
    changed set == A8's modify: set  TRUE
    unexpected changes               none

    results/   base  69  head  69   differing: none
    scripts/   base  60  head  60   differing: none
    tests/     base  20  head  20   differing: none
    specs/     base  37  head  38   differing: only this task's specification

    CONVENTIONS.md            SAME
    DECISION_LOG.md           SAME
    docs/BRANCHING_POLICY.md  SAME
    results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json  SAME

**The results file every `MEASURED` literal is read from is unmodified.**
**No pre-existing specification was edited.** **INTENDED for commit 5:** it adds
this report and modifies nothing, so `added` becomes 4 and the rest is
unchanged; measured confirmation is post-report evidence.

**A11, MEASURED.** Proposed messages were scanned before each commit; stored
messages read back after:

    8463dd7a  spec: adopt the microscopic parameter domain, with evidence corrections
    e76983e6  review: pre-execution review for the parameter-domain adoption
    5add3085  derivations: adopt the P2-PHASE-01 microscopic parameter domain
    9ed98560  gates: mark the microscopic parameter domain prerequisite SATISFIED

    trailers on each of the four                      none
    'Co-Authored-By' in any stored message              0
    session identifier or URL in any stored message     0
    tool or model attribution in any stored message     0

**Commit 5's INTENDED message**, first line:

    report: record the parameter-domain adoption and the gate-pin conflict

## 11. Stops and clarifications

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary stop

**A7 modifies an artifact that a registered gate pins by sha256, and no
instruction in this task can repair the consequence.**

**MEASURED:**

    GATES.md line 1040, inside ## P2-PHASE-01, still reads
      (sha256 `a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73`).

    derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
      at 1cb5550f     a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73
      at commit 4     e373efcb0d14db641604537c6a264e2c48536ab516162b7fef6a995cbd11d1cb

**So on this branch a registered gate pins a digest its target no longer has.**

**The conflict, stated without resolving it.** A7 orders the modification and
A8's frozen manifest lists the path, so the modification is authorised. A6
says `GATES.md` changes "in that block and nowhere else", so the pin may not be
updated here. And `CONVENTIONS.md` states:

> An executor MUST NOT correct, reformat, or re-pin: any artifact
> hash-pinned by a registered gate; any gate status, verdict, or digest;
> any file outside the declared scope; or any repository configuration.

**Two readings, and I am not entitled to pick one.** On the strict reading that
sentence is a flat prohibition and A7 instructs me to modify an artifact
hash-pinned by a registered gate, which the rule forbids outright. On the
narrower reading the sentence governs an executor acting on its own initiative
— its own paragraph opens *"the executor MAY correct it without returning for
authorization where…"* — and a reviewed specification naming the path in a
frozen manifest supplies the authorisation the rule presumes absent. **The
review discusses this exact insertion at length in its §5 and approves it, so
the modification was seen; the pin was not.**

**What I did, said plainly: I executed A7 as specified.** Both instructions
were individually executable, the review approved the specific action, and the
prohibited motion — *re-pinning* — is the one thing I did not do. **My
execution is not a ruling and must not be read as one.**

**What it costs, and where.** Nothing authoritative is affected: this is a
branch, `main` is untouched, and no validator catches the mismatch — MEASURED,
the full suite is 280 passed, 2 deselected, and no test compares a `GATES.md`
pin against its target's content. **The cost lands at integration**, which is a
separate task. **This branch should not be integrated until the PI or Reviewer
rules on whether the pin is re-pinned, whether A7's insertion should be
withdrawn, or whether a stale pin inside a registered gate is acceptable on
`main`.**

**A6 removed the other pin that would have gone stale.** The replaced block
pinned `d8e15469…` for the parameter-domain draft, which A7 also modifies; A6's
replacement names that file as "Superseded draft" with **no digest**, so no
second stale pin arises. **That was a consequence of A6's wording rather than a
provision against the problem** — the admissibility-contract pin is in the
block A6 does not touch.

**One historical reference is NOT a defect and was checked before saying so.**
`specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md` records both
old digests at lines 547 and 550. **A specification pinning the digests that
were current at its own evidence base is correct and must not be updated.**

### `SPECIFICATION_DEFECT` — none

**No instruction was unsatisfiable and no anchor failed.** The two residual
wordings of §5 are §8 sixth-defect items in the adopted artifact, not defects
of this specification; they are reported and left.

### `REPOSITORY_DEFECT` — one, pre-existing and out of scope

**`P7` is vacuous against the real `GATES.md`.** §9. Known, scheduled for
repair in a separate task, not touched here. **It is stated adjacent to the
`PASS` it produced**, as §9 of the specification requires.

### `ENVIRONMENT` — none

**No environment failure occurred.** **`CONVENTIONS.md` Rule 13 carries two
conflicting diagnostic orders, a known open item; neither was exercised**, and
I am not naming one as having applied. Nothing was installed.

### `OBSERVATION_METHOD_ERROR` — none

**One method choice is recorded because it could have gone the other way.**
A6's embedded digest was read from **commit 3's committed blob**
(`git show HEAD:<path> | sha256sum`), not from the working-tree file, as §7
requires. The two agreed, but the working-tree value would have been the
unverified one and is not what was used.

**The eight OLD anchors were matched by exact substring with a required count
of one**, and a count other than one was coded to abort. **No approximate match
was attempted anywhere.**

### Secondary findings

- **RUN 2's narrowing excluded nothing** — its output is byte-identical to
  RUN 1's. §9.
- **The two prospectivity readings differ in one field and no verdict.** §9.
- **`P1` passed by reading a structured `stated:` declaration as prose**, on a
  branch whose checker predates the declared-total repair. It got the right
  answer by the mechanism that repair exists to remove. §9.
- **The adopted artifact's title and two sentences still describe a draft.** §5.
- **No repository convention requires a review to carry the digest of what it
  reviewed.** This review does, voluntarily. §2.

### Anything ambiguous, unsatisfiable, or that I would have specified differently

- **A7 should have anticipated the gate pin.** I would have added a criterion
  either authorising the re-pin explicitly with the PI's ruling attached, or
  recording that the pin is knowingly left stale for the integration task to
  resolve. **As written the specification is silent, and silence on a
  registered gate's digest is the one place silence is expensive.**
- **A4's status-header substitution should have carried the H1 title with it.**
  The title is the first thing a reader sees and it still says
  `DRAFT FOR ADOPTION`. **Anchoring the bold status sentence alone left the
  document self-contradicting in its opening lines.**
- **A3 left three of four blob ids as `<measure at 1cb5550f before use>`.**
  That is honest, but it means three quarters of A3 pins nothing: a mismatch
  there cannot be a STOP, because there is no declared value to mismatch. **A
  pinned input whose value the executor supplies is a record, not a check.**
- **A9 asked for both prospectivity readings without saying which governs if
  they disagree.** They did not disagree here, so nothing turned on it.

## 12. §9 — Rule 16 assessment

**Rule 16 is operative. The specification offered two junctions and I confirm
both, and add a third.**

### First junction, confirmed: `SATISFIED` does not mean the gate is ready

**After this task `GATES.md` reads `Prerequisite state: SATISFIED` for the
MICROSCOPIC PARAMETER DOMAIN of a gate that remains `PROPOSED`.** **A reader
may take "domain adopted" for "the gate is ready to run". It is not.**

**Where a reader meets it, and what the second prerequisite still needs.** The
reader meets it in the `## P2-PHASE-01` block itself, three lines above the
still-`UNSATISFIED` `PHASE INPUT / ADMISSIBILITY CONTRACT` block — **which is
the best possible placement, because the contradiction to the optimistic
reading is on the same screen.** The new block's closing paragraph states it
outright: *"Adoption freezes where to look. It certifies no phase."*

**What the second prerequisite still needs, MEASURED from its own block:**
*"No operational stability or admissibility rule is presently frozen."* **Until
one is, there is no criterion against which a candidate could be judged
admissible or stable**, and the adopted artifact's own §4 names what an upgrade
would take: a full condensate-space Hessian, the gate's admissibility
assessment, and — if "stable" means thermodynamic selection — a free-energy
comparison under a common normalisation, **which needs `OPEN-AC-3`, still
open.** **Three of the five `OPEN-AC` items remain open**, and the adopted
artifact now says so where an earlier version listed only one of them.

### Second junction, confirmed: `P7: PASS` checked nothing

**Stated at length in §9, adjacent to the result rather than in a distant
note.** **A `PASS` from a vacuous check is the most dangerous kind of green
this programme has named**, and it appeared in this task's own output, over the
very file this task modifies.

### Third junction, added: the adopted evidence is `mu = 0` and one ansatz

**Every number in the adopted artifact comes from one exploratory study at
`mu = 0` under a uniform scalar ansatz**, whose own `limitations` field —
MEASURED — reads: *"restricted to a uniform scalar ansatz at mu=0"*,
*"one-dimensional curvature is not the full multichannel Hessian"*, *"no
cross-family effective-potential comparison is constructed"*. **The gate's
scope in `GATES.md` includes finite density.** **A reader may take an adopted
domain for a domain adopted over the gate's scope. It is adopted over a
slice of it**, and `OPEN-PD-4` remains open with no evidence at non-zero `mu`
in the repository at all.

## 13. Does the adopted text now read as though a phase had been found?

**No, and the corrections moved it further from that reading rather than
nearer.**

**The word "adopted" is the risk**, because a document titled `ADOPTED` sitting
beside a gate marked `SATISFIED` invites the inference. **Three things in the
committed text block it**, and all three are inside the artifact rather than in
this report, which is where a later reader will look:

- §3 still says the window is a **positive-coupling enumeration window,
  provisional**, and that its edges are the edge of computed evidence, not
  physical bounds;
- §7 now ends with the boundary statement inserted by §5 of the specification:
  **adoption certifies no root completeness, no full-space stability, no
  thermodynamic dominance, no negative-`G` exclusion, no finite-density
  coverage**;
- §4's candidate-versus-phase distinction is untouched, and **C-5 strengthened
  it** by restoring `OPEN-AC-4`, which bears on stability and had been omitted.

**C-1 is the clearest case of a correction that lowers rather than raises the
claim.** It replaced a bracket that implied file-wide scope with three
explicitly scoped brackets, and it **withdrew the assertion that no measurement
had tested the sign at negative mass** — three such measurements exist in the
file. **The result is a weaker, truer statement: what is missing is global
non-negativity, not evidence.**

**What a hurried reader could still get wrong:** the artifact's own title and
its "nothing here is in force" sentence (§5), which now understate rather than
overstate. **Understating is the safer failure**, but it is still a
contradiction and it should be repaired.

## 14. Confirmations the report contract asks for explicitly

- **`P2-PHASE-01`'s `Status:` line still reads `PROPOSED`.** MEASURED, base and
  head both.
- **The `PHASE INPUT / ADMISSIBILITY CONTRACT` prerequisite still reads
  `UNSATISFIED`**, and its block is byte-identical to the base.
- **`C1`, `C2` and `C3` were not answered.** No claim is made about whether the
  complement root is solved or constructed, about the global sign of
  `I0(Mhat)`, or about whether the curvature asymmetry is physical or
  coordinate-induced.
- **`scripts/p2_phase01_scalar_exploratory.py` was NOT read.** MEASURED: the
  whole of `scripts/` is blob-identical between base and commit 4, and the file
  was never opened in this task. **It was opened in no other sense either — its
  digest was verified against the results file's `script_sha256` in the
  read-only audit that preceded this task, and that is a digest comparison, not
  a reading of the code.**
- **No enumeration was run and nothing was computed.**
