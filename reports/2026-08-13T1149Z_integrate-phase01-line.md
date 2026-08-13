# Report — integrate the science line, and land it

Specification: `specs/2026-08-13T1149Z_integrate-phase01-line.md`
Review: `reviews/chatgpt/2026-08-13T1149Z_integrate-phase01-line.md` — APPROVED FOR EXECUTION
Evidence base: `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`
Branch: `science/integrate-phase01-line`, cut from that commit.

**Every figure is labelled MEASURED or INTENDED.** **Nothing here claims to
measure commit 7, and nothing here claims `main` has moved** — the landing
follows this commit and its evidence is post-report.

---

## 0. What happened

**Four merges in the frozen order. Exactly two conflicts, both in the two named
paths, both resolved by the text §4 supplies verbatim. No third conflict.**

    merge 1  8b79fad4  clean                          commit 3  9e6c3e68
    merge 2  f27f868a  CONFLICT in exactly 2 paths    commit 4  a133f04e
    merge 3  92726596  clean                          commit 5  ba13ac4f
    merge 4  c6f4f5e3  clean                          commit 6  b3ca4484

**MEASURED at commit 6: 25 additions, 3 modifications, 0 removals** — the figure
the specification predicts for the pre-report head. **All 23 arriving paths are
blob-identical to their contributing source.** **Both pins match.** **A12's
RUN 2 — stop-governing — PASSED exit 0 on both prospectivity readings.**

**`P2-PHASE-01` now carries BOTH prerequisites `SATISFIED` and remains
`PROPOSED`.** **MEASURED: zero occurrences of `### Unsatisfied prerequisite` in
`GATES.md`.** **That combination has never existed on any single branch before
this commit.**

**And it must be read for what it is.** **No phase has been found. No candidate
has been assessed. Nothing has been evaluated against the admissibility standard
this merge lands.** The gate's `Required computations` still reads
`(not started)`; three evaluation inputs remain open, one not started at all;
and `C1` and `C3` **removed** evidential weight rather than adding any. **This
merge is progress toward being able to ask the question, not toward an answer**,
and §12 states that where a reader meets it.

**One check deserves naming because it could have silently failed.** §4a's
resolution is semantic precisely so that it cannot revert an already-landed
block. **MEASURED: the MICROSCOPIC PARAMETER DOMAIN block in the resolved tree
is byte-identical to source 1's version — 25 lines, `diff` empty, sha256
`b823ff10…` on both sides.** In this merge the conflict markers happened to fall
below that block (1035/1043/1072, heading at 1010), so a marker-relative
resolution would also have worked. **The semantic form was checked to be correct
rather than assumed to be**, which is the whole point of A5 carrying it as a
stop.

---

## 1. A1 — Refs and ancestry

**MEASURED**, read from the remote:

```
1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab	refs/heads/main
8b79fad4d62be70724b83850c2a8f23ffee1392f	refs/heads/science/adopt-parameter-domain-labels
f27f868a03449416fbf6eb96e9d5522c33f46806	refs/heads/science/adopt-admissibility-contract
92726596f29e12ec12e7f795bd68b902ac712d50	refs/heads/science/c1-complement-root-provenance
c6f4f5e35c8591d18c51443678142f52891b7edd	refs/heads/science/c3-curvature-asymmetry
```

**All five match the specification's header. No STOP.**

**Source 1's ancestry, the two exit statuses A1 asks for:**

    git merge-base --is-ancestor 2e4cc6eb 8b79fad4   ->  exit 0
    git merge-base --is-ancestor cd1ebd84 8b79fad4   ->  exit 0

**Both are ancestors, so merging source 1 merges all three commits' work and
neither was merged separately.**

**And none of the four was already an ancestor of `main`:**

    8b79fad4 -> exit 1    f27f868a -> exit 1
    92726596 -> exit 1    c6f4f5e3 -> exit 1

## 2. A2 — The review, committed unedited

**MEASURED.** The review carries
`Reviewed specification SHA-256: b40415c71fa4a747328f56f1b43fd7ccc55b9b0769e1137142689aae9e6f4070`.

    supplied specification file, sha256
      b40415c71fa4a747328f56f1b43fd7ccc55b9b0769e1137142689aae9e6f4070   EQUAL

    supplied review   d05bdc788874c8d867faa20345ba4ac2df58bc2f7266b1a746340ec52895ab12
    committed blob    d05bdc788874c8d867faa20345ba4ac2df58bc2f7266b1a746340ec52895ab12
    EQUAL

**Filled in, correct, neither blank nor naming a different digest. A2's stop is
not triggered.** The review's own condition — that it approves *"only the
specification at the SHA-256 above"* — is met. Both arrived as FILES.

## 3. A3 — Merge parentage, twelve values, each derived separately

**MEASURED. Parent 1 and parent 2 by `git rev-parse HEAD^1` / `HEAD^2`; the
merge-base by `git merge-base <p1> <p2>` computed from those two values; and
each triple cross-checked against `git rev-list --parents -n 1`, which is an
independent path to the same parentage.**

    merge 1   commit 3  9e6c3e681e19939c96ef698f81027db4c8204059
      parent 1    87e13d745ba28439963277665fe9a2edd4a63cb4   this task's REVIEW commit
      parent 2    8b79fad4d62be70724b83850c2a8f23ffee1392f   source 1
      merge-base  1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

    merge 2   commit 4  a133f04eea4f396b6a968cec2f597fa257e7656a
      parent 1    9e6c3e681e19939c96ef698f81027db4c8204059   merge 1
      parent 2    f27f868a03449416fbf6eb96e9d5522c33f46806   source 2
      merge-base  1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

    merge 3   commit 5  ba13ac4f094ad63057d6fee1bc5d35b735a96171
      parent 1    a133f04eea4f396b6a968cec2f597fa257e7656a   merge 2
      parent 2    92726596f29e12ec12e7f795bd68b902ac712d50   source 3
      merge-base  1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

    merge 4   commit 6  b3ca44847169f251bb0e83dcf598b0ed01996269
      parent 1    ba13ac4f094ad63057d6fee1bc5d35b735a96171   merge 3
      parent 2    c6f4f5e35c8591d18c51443678142f52891b7edd   source 4
      merge-base  1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**Parent 1 of merge 1 is this task's review commit; parent 1 of merges 2, 3 and
4 is the preceding merge.** **That is the legitimate merge-as-parent-1 case the
specification names, not a defect** — the branch is a chain, so each merge's
first parent is necessarily the previous one.

**All four merge-bases are the evidence base**, because all four sources were
cut from it independently. **No source was rebased and none carries another.**

## 4. A4 — Conflicts, per merge

**MEASURED, `git diff --name-only --diff-filter=U` after each merge:**

    merge 1   0 conflicts
    merge 2   2 conflicts:
                GATES.md
                derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
    merge 3   0 conflicts
    merge 4   0 conflicts

**Exactly two conflicts, both in merge 2, both in the two named paths.** **No
conflict in any third path, and none in either named path during merges 1, 3 or
4.** **A4's stop is not triggered, and no unauthorised resolution was
performed.**

## 5. A5 — The two resolutions, in full

### 5a. `GATES.md`, resolved by semantic block

**How the resolution was applied, and why it is not marker-relative.** The
conflict region was located by its markers, but **the decision was made on the
content of the two sides, with three assertions coded as aborts**: that the
`HEAD` side begins with the OLD `### Unsatisfied prerequisite — PHASE INPUT …`
block; that the incoming side begins with the new `### Satisfied prerequisite —
…` block; **and that the string `MICROSCOPIC PARAMETER DOMAIN` appears in
neither side.** **Had the parameter-domain block fallen inside the markers, the
third assertion would have stopped the resolution rather than let a side be
taken whole.**

**MEASURED, where the markers actually fell:**

    <<<<<<< HEAD   line 1035
    =======        line 1043
    >>>>>>>        line 1072
    the MICROSCOPIC PARAMETER DOMAIN heading   line 1010, ABOVE the markers

**So in this merge the block sat outside the conflict**, as the author's dry run
found. **The assertion confirmed it rather than assuming it.**

    PRESERVE  the MICROSCOPIC PARAMETER DOMAIN block from HEAD   — untouched
    REPLACE   the PHASE INPUT / ADMISSIBILITY CONTRACT block     — incoming kept
    PRESERVE  the separating blank line                          — untouched
    AUTHOR    nothing                                            — no line written

**The resolved region, both prerequisite blocks in full:**

```
### Satisfied prerequisite — MICROSCOPIC PARAMETER DOMAIN
Artifact state: **ADOPTED**. Prerequisite state: **SATISFIED**,
per the PI ruling recorded in §3a of
`specs/2026-08-12T2258Z_adopt-parameter-domain.md`.
Owner: Paper 2. Canonical label: **MICROSCOPIC PARAMETER DOMAIN**;
not a gate ID. Adopted artifact:
`derivations/P2-PHASE-01_microscopic_parameter_domain.md`
(sha256 `4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214`).
Superseded draft:
`derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`.

The adopted artifact bounds the scan-eligible coupling `G` to
`G/Gc` in `[0.80, 3.00]` over sixteen pre-registered values, and
answers finite-density `μ` as a FIXED INPUT at `0`. **For the
lattice spacing `a` it answers NEITHER fixed input nor scan
dimension**: `a` is left unfixed because no quantity computed at
this gate depends on it, and every quantity is dimensionless.
**That is a third answer to this gate's binary question and is
recorded as such.** No scan dimension is admitted without a frozen
range.

**Adoption freezes where to look. It certifies no phase**, no root
completeness, no full-space stability, no thermodynamic dominance,
no exclusion of negative `G`, and no finite-density coverage.

### Satisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT
Artifact state: **ADOPTED**. Prerequisite state: **SATISFIED**.
Owner: Paper 2. Canonical label: **PHASE INPUT / ADMISSIBILITY
CONTRACT**; not a gate ID. Adopted artifact:
`derivations/P2-PHASE-01_input_admissibility_contract.md`
(sha256 `e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3`).
Superseded draft:
`derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md`.

An operational admissibility standard is frozen: full
condensate-space Hessian positivity transverse to symmetry-required
flat directions; thermodynamic selection against the comparison set
of stationary solutions satisfying the non-thermodynamic conditions
C-i and C-iii, under a common normalisation; and symmetry accounting
sufficient to identify those flat directions. Per PI ruling, a rule
that can decide a candidate is operational whether or not its inputs
presently exist.

The comparison set is defined WITHOUT reference to admissibility,
deliberately. A summary phrased as "no competing ADMISSIBLE solution
deeper" would define admissibility in terms of itself; the adopted
artifact does not, and this block must not.

**This prerequisite being SATISFIED means a rule exists. It does not
mean any candidate has been assessed, and it does not mean the
evaluation inputs are complete.** Three remain open —
`OPEN-AC-1`, `OPEN-AC-3`, `OPEN-AC-4` — and they are
evaluation-input gaps, not rule-definition gaps.
```

**The byte comparison A5 requires, MEASURED:**

    MICROSCOPIC PARAMETER DOMAIN block, source 1 (8b79fad4)   sha256 b823ff10dce342972f9be850e537702920f976f4aa23a02fd82f69da9a23c418
    the same block in the resolved tree                       sha256 b823ff10dce342972f9be850e537702920f976f4aa23a02fd82f69da9a23c418
    diff                                                      empty, 25 lines
    BYTE-IDENTICAL — not reverted

### 5b. The contract draft, both paragraphs reconciled

**The entire conflict region — both sides and all three markers — was replaced
with §4b's text.** The contradiction was real: **source 2's pointer says the
draft's `OPEN-AC` entries "are unchanged and remain OPEN"**, while **source 1's
cross-reference records `OPEN-AC-2` as `RESOLVED FOR ENUMERATION` and
`OPEN-AC-5` as `CLOSED`.** **Source 2 was written on `main`, where both were
still open, and could not know.** **Concatenating the two sides would have
landed a file that contradicted itself in consecutive paragraphs.**

**The resolved region:**

```
# `P2-PHASE-01` phase input / admissibility contract — DRAFT, NOT ADOPTED

**SUPERSEDED.** Adopted as
`derivations/P2-PHASE-01_input_admissibility_contract.md`. This file is
retained as historical evidence and is not operative.

**Cross-reference.** `OPEN-AC-2` is **RESOLVED FOR ENUMERATION**: the
negative-mass branch is included as a candidate, and is NOT certified as
admissible or stable, by the PI ruling recorded in
`derivations/P2-PHASE-01_microscopic_parameter_domain.md`. `OPEN-AC-5`
is **CLOSED** — `Mhat = 1` is NOT an admissibility bound — by the same
answer that closes `OPEN-PD-1` in that artifact. `OPEN-AC-1`,
`OPEN-AC-3` and `OPEN-AC-4` **remain OPEN**, and the adopted contract
reclassifies those three as evaluation-input gaps without resolving any
of them.

**`RESOLVED FOR ENUMERATION` is not `CLOSED`, and the difference is the
point.** `OPEN-AC-2` asks whether the branch is physical; the ruling
answers only where it may appear in an enumeration.

## Status and evidence boundary

```

**`OPEN-AC-1`, `OPEN-AC-3` and `OPEN-AC-4` remain OPEN, and the
remaining-open claim is scoped to "those three"**, which is correct once
`AC-2` and `AC-5` are accounted for immediately above it. **No `OPEN-AC` body
text was edited and nothing else in the file changed.**

### The tree-wide marker search

**MEASURED over every tracked file — 363 files, not only the two:**

    git grep -n "^<<<<<<< "   ->  none
    git grep -n "^=======$"   ->  none
    git grep -n "^>>>>>>> "   ->  none

**One file matches the bare seven-character forms anywhere on a line:**
`specs/2026-08-13T1149Z_integrate-phase01-line.md:203`, which is **this task's
own A5 text quoting the marker characters as literals inside the criterion.**
**It is the specification describing what to search for, not a surviving
marker.** **No conflict marker survives anywhere in the tree.**

**I record that my first search excluded `specs/`, `reports/` and `reviews/`
and was therefore not tree-wide.** It returned "none" for the wrong reason. **The
search above is the one the criterion asks for**, and it is what found — and
explained — the single legitimate hit.

## 6. A6 — Scope, at two heads

**MEASURED at commit 6, the final merge commit, before this report exists:**

    25 additions, 3 modifications, 0 removals

**That is the figure the specification predicts for the pre-report head.**

**The three modifications, MEASURED:**

    GATES.md
    derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
    derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md

**The twenty-five additions, MEASURED, enumerated:**

    derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md
    derivations/P2-PHASE-01_C1_complement_root_provenance.md
    derivations/P2-PHASE-01_C3_curvature_asymmetry.md
    derivations/P2-PHASE-01_input_admissibility_contract.md
    derivations/P2-PHASE-01_microscopic_parameter_domain.md
    reports/2026-08-12T2258Z_adopt-parameter-domain.md
    reports/2026-08-12T2326Z_adopt-domain-repair.md
    reports/2026-08-13T0034Z_adopt-domain-labels.md
    reports/2026-08-13T0150Z_c1-complement-provenance.md
    reports/2026-08-13T0307Z_c3-curvature-asymmetry.md
    reports/2026-08-13T0740Z_adopt-admissibility-contract.md
    reviews/chatgpt/2026-08-12T2258Z_adopt-parameter-domain.md
    reviews/chatgpt/2026-08-12T2326Z_adopt-domain-repair.md
    reviews/chatgpt/2026-08-13T0034Z_adopt-domain-labels.md
    reviews/chatgpt/2026-08-13T0150Z_c1-complement-provenance.md
    reviews/chatgpt/2026-08-13T0307Z_c3-curvature-asymmetry.md
    reviews/chatgpt/2026-08-13T0740Z_adopt-admissibility-contract.md
    reviews/chatgpt/2026-08-13T1149Z_integrate-phase01-line.md
    specs/2026-08-12T2258Z_adopt-parameter-domain.md
    specs/2026-08-12T2326Z_adopt-domain-repair.md
    specs/2026-08-13T0034Z_adopt-domain-labels.md
    specs/2026-08-13T0150Z_c1-complement-provenance.md
    specs/2026-08-13T0307Z_c3-curvature-asymmetry.md
    specs/2026-08-13T0740Z_adopt-admissibility-contract.md
    specs/2026-08-13T1149Z_integrate-phase01-line.md

**Twenty-three arrive from the four sources** — five under `derivations/` and
six each under `specs/`, `reviews/chatgpt/` and `reports/` — **and two are this
task's own specification and review.** **The twenty-sixth, this report, is
INTENDED at commit 7**, which makes the final manifest figure **26 additions and
3 modifications**, INTENDED:

    stated: 26 additions, 3 modifications
    base: 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    head: <commit 7, INTENDED>
    mode: exact
    modify:
      GATES.md
      derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
      derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Path by path, the manifest matches what the merges produced**: every path in
A6's `add:` list is present at commit 6 except this report, and every path
present at commit 6 is in A6's list. **No path arrived that the manifest does not
name.** **The scope measured base-to-commit-7 is post-report evidence.**

## 7. A7 — Pins, and the now-unpinned draft

**MEASURED at commit 6**, every `` (sha256 `<64 hex>`) `` enumerated over the
whole file, the artifact path taken from the line immediately above.

**AT-LEAST-ONE ASSERTION: 2 pins found, `>= 1` satisfied**, coded as an abort.

    pin 1   line 1017
      path    derivations/P2-PHASE-01_microscopic_parameter_domain.md
      pinned  4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
      actual  4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
      MATCH

    pin 2   line 1040
      path    derivations/P2-PHASE-01_input_admissibility_contract.md
      pinned  e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
      actual  e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
      MATCH

    PINS FOUND: 2   all matching: yes

**The contract DRAFT is pinned by nothing after this merge, and that is
correct.** **MEASURED: its current digest occurs 0 times in `GATES.md`.** §4a's
resolution replaced the block that carried its pin, and the replacement names the
draft as *"Superseded draft"* **without a digest** — the same shape the
parameter-domain line already used. **So a file that changed in this merge is
pinned nowhere, deliberately**, and a reader should not have to infer that from
the absence of a mismatch.

## 8. A8 — Gate invariants at commit 6

**MEASURED:**

    1  '^## P2-' section count                     14
    2  P2-PHASE-01                                 Status: PROPOSED
    3  prerequisites                               BOTH read Satisfied
         line 1010  ### Satisfied prerequisite — MICROSCOPIC PARAMETER DOMAIN
         line 1035  ### Satisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT
       occurrences of '### Unsatisfied prerequisite'      0
    4  every '^Status:' line                       15 lines, TEXTUALLY IDENTICAL
                                                   to the evidence base

**All four hold.** **No gate `Status:` line changed anywhere in the file**, which
is what distinguishes a prerequisite transition from a gate verdict.

## 9. A9 — Arriving artifacts and modified drafts, kept apart

### (i) The twenty-three ADDED paths — all blob-identical to their source

**MEASURED, `git rev-parse <source>:<path>` against `git rev-parse HEAD:<path>`:**

    source 1  8b79fad4  10 paths   all IDENTICAL
    source 2  f27f868a   4 paths   all IDENTICAL
    source 3  92726596   4 paths   all IDENTICAL
    source 4  c6f4f5e3   5 paths   all IDENTICAL

    COMPARISONS 23   identical 23   differing 0

**Nothing that arrived by merge was altered.** Source 1 contributes ten because
it carries three tasks' records; source 4 contributes five because it adds both
the C3 findings and the C-check register.

### (ii) The two MODIFIED drafts, reported separately

**These are not among the twenty-three and are a different universe of
comparison.**

    derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
      at base       158ab187f2576fd8f163cd3ad3b76b7b897e6fb5
      at source 1   c7910bc6a6cca5c684b082aef87de85b6a3d6f4c
      at head       c7910bc6a6cca5c684b082aef87de85b6a3d6f4c
      MATCHES SOURCE 1 — as required. Modified by source 1 alone, not in
      conflict, and §4 authored nothing for it.

    derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
      at base       5f020f33a9230d1aaa7c98c79db49b1efcb822f6
      at source 1   f6f0e524daa11f2f8e3470cc4ab44fd3f6630615
      at source 2   003ed2f9b9ab0684f721fba1b5754036e376e386
      at head       9d18b5f153f4b40c4aa6a2f6a1b01defb7be4e87
      matches source 1: NO      matches source 2: NO
      THE SOLE PATH MATCHING NEITHER SOURCE — correct, because §4b's
      reconciliation text exists on neither branch.

**Four distinct blobs for one file across base, two sources and the head.**
**That is the signature of a genuine reconciliation rather than a side taken**,
and it is why A9 keeps the three comparison classes apart.

## 10. A10 — Protected paths

**MEASURED at commit 6**, whole-tree `git ls-tree -r` blob comparison:

    PATHS COMPARED (existing at the evidence base)   343
    blob-identical at commit 6                       340
    changed                                            3   == A6's modify: set
    removed                                            0

    results/   base 69  head 69   differing: none
    scripts/   base 60  head 60   differing: none
    tests/     base 20  head 20   differing: none

    CONVENTIONS.md                    IDENTICAL
    DECISION_LOG.md                   IDENTICAL
    docs/BRANCHING_POLICY.md          IDENTICAL
    derivations/P2-DEFERRED-ITEMS.md  IDENTICAL

**Nothing under `results/`, `scripts/` or `tests/` moved**, so the merge lands
no computation and no test. **The deferred-items register is untouched**, as the
C-check register's own text requires.

## 11. A11 — Superseded branches, six exit statuses BEFORE the advance

**MEASURED, `git merge-base --is-ancestor <sha> HEAD`, exit 1 meaning NOT an
ancestor:**

    52f65117  exit 1      ebd531ab  exit 1      40168469  exit 1
    7146a093  exit 1      10c260b9  exit 1      d64cd912  exit 1

**None of the six superseded branches is an ancestor of the head.** **Six
separate measurements, not one aggregated claim.** The after-the-advance repeat
is post-report evidence.

## 12. A12 — The two checker runs, and the subject set as measured

Base `1cb5550f…`, head **commit 6** `b3ca4484…` — **not the report commit, which
carries this output.** **Both prospectivity readings run.**

### RUN 1 — default subject selection, observational, governs nothing

```json
{
  "base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
  "head": "b3ca44847169f251bb0e83dcf598b0ed01996269",
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
  "head": "b3ca44847169f251bb0e83dcf598b0ed01996269",
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": ["P2-PHASE-01"],
  "specification_paths": ["specs/2026-08-13T1149Z_integrate-phase01-line.md"],
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

**The `EXCLUSIVE` variants are identical but for the one `inclusivity` field.**

**MEASURED — all four runs `overall` PASS, exit 0:**

    RUN 1  INCLUSIVE  exit 0  PASS
    RUN 2  INCLUSIVE  exit 0  PASS      <- stop-governing
    RUN 1  EXCLUSIVE  exit 0  PASS
    RUN 2  EXCLUSIVE  exit 0  PASS      <- stop-governing

    P1 PASS  P2 PASS  P3 PASS  P4 PASS  P5 PASS
    P6 PASS  P7 PASS  P8 PASS  P9 PASS

**RUN 2's stop is not triggered.** **Every property returned PASS — the first
range in this line where none returned `NOT_APPLICABLE`**, because the range now
contains merges (P5) and reports (P9).

    commits in range              34
    on the first-parent line       6
    in scope                       6

### The subject set RUN 1 actually selected, as measured

**§5 warns not to infer it from the specification. MEASURED: SEVEN, and they
are:**

    specs/2026-08-12T2258Z_adopt-parameter-domain.md          stated 7   counted 7
    specs/2026-08-12T2326Z_adopt-domain-repair.md             stated 5   counted 5
    specs/2026-08-13T0034Z_adopt-domain-labels.md             stated 5   counted 5
    specs/2026-08-13T0150Z_c1-complement-provenance.md        stated 4   counted 4
    specs/2026-08-13T0307Z_c3-curvature-asymmetry.md          stated 5   counted 5
    specs/2026-08-13T0740Z_adopt-admissibility-contract.md    stated 6   counted 6
    specs/2026-08-13T1149Z_integrate-phase01-line.md          stated 29  counted 29

**Seven, not six — the six arriving from the four sources plus this task's own,
added at commit 1.** **The corrected clause is right and the measurement
confirms it.** **All seven parse and all seven agree.**

**RUN 1 and RUN 2 are NOT byte-identical here**, unlike every previous task in
this line: RUN 1 carries seven P1 subjects and RUN 2 carries one. **The
narrowing therefore excluded six specifications** — all six arriving by merge,
all six already reviewed and reported under their own tasks, and **all six
measured PASS in RUN 1 anyway.** **Nothing was hidden by the narrowing, and I
can say so because RUN 1 was run and reported.**

**`P1`'s `stated 29 counted 29` for this task's own specification** is the
declared-total grammar counting 26 `add:` and 3 `modify:` records against a
`stated:` line of 26 and 3. **The landed checker reads that line as prose and
sums it to 29; the counted set is 29 paths.** **Right answer, by the mechanism
the unlanded declared-total repair exists to remove.**

### `P7` returned `PASS` and it is evidence of nothing

**MEASURED:** `section_count_base` 0, `section_count_head` 0, against a
`GATES.md` carrying fourteen gates. `GATE_HEADING` is
`^## (P2-[A-Z0-9-]+)\s*$`; every real heading continues past the ID. **P7
compared two empty maps.**

**This merge modifies `GATES.md` and flips a prerequisite — the largest gate
change this programme has made — and it was handed
`authorised_modified_gates: ["P2-PHASE-01"]`, the strongest possible
declaration.** **A parser matching nothing cannot enforce it.** **The edit's
confinement rests on A5's byte comparison, A7's pin table, A8's four invariants
and A10's 340-of-343 blob identity.**

## 13. A13, A14 — Validators and hygiene

**A13, MEASURED:**

    at the evidence base (recorded by the four source tasks)   280 passed, 2 deselected
    at commit 6                                                280 passed, 2 deselected
    exit status                                                0

**Unchanged, as expected — this merge adds no test and changes none**, and
`tests/` is blob-identical (§10).

**A14, MEASURED.** Proposed messages were scanned before each commit and stored
messages read back after. **The six commits this task authors:**

    7c2b1e84  spec: integrate the science line, and land it
    87e13d74  review: pre-execution review for the science-line integration and landing
    9e6c3e68  merge: land the parameter-domain adoption line
    a133f04e  merge: land the admissibility contract, resolving two authorised conflicts
    ba13ac4f  merge: land the C1 complement-root provenance finding
    b3ca4484  merge: land the C3 curvature-asymmetry finding and the C-check register

    trailers on each of the six                         none
    'Co-Authored-By' in any stored message                0
    session identifier or URL in any stored message       0
    tool or model attribution in any stored message       0

**Case-insensitive scan over all thirty-four stored message bodies in the range
— the six above and the twenty-eight arriving by merge: 0 matches.**

**Commit 7's INTENDED message**, first line:

    report: record the four-merge integration and the landing

## 14. §8 — Rule 16 assessment, all three junctions

### First: two `SATISFIED` prerequisites do not mean a gate ready to run

**`GATES.md` now reads `Satisfied` for both prerequisites of a gate that remains
`PROPOSED`.** **A reader may take that for a gate ready to run. It is not.**

**MEASURED, in the same file:** the gate's `Required computations` section reads
`(not started)` and `Required deliverables` reads `(not started)`. **Three
evaluation inputs remain open — `OPEN-AC-1`, `OPEN-AC-3`, `OPEN-AC-4` — and
`OPEN-AC-1` has not been started at all.**

**Where a reader meets it:** in the admissibility block itself, in bold, four
lines under the word `SATISFIED` — *"This prerequisite being SATISFIED means a
rule exists. It does not mean any candidate has been assessed, and it does not
mean the evaluation inputs are complete."* — and in the parameter-domain block
three lines above it: *"Adoption freezes where to look. It certifies no phase."*
**Both are in `GATES.md`, not only in the artifacts and not only in this
report.**

### Second: until this merge, neither branch showed the state the programme was in

**This is the junction the integration repairs, and it is worth stating because
the shape will recur.** Before this commit, `science/adopt-parameter-domain-labels`
showed the domain prerequisite `SATISFIED` and the contract `UNSATISFIED`;
`science/adopt-admissibility-contract` showed exactly the reverse. **Anyone who
checked out either branch saw a state that did not exist**, and each branch's own
report said so.

**The cause was structural, not careless.** The two prerequisite blocks are
separated by one blank line, so two independently authorised tasks editing
adjacent blocks could not see one another. **The same shape recurs whenever two
branches edit adjacent blocks of one registry file**, and what caught it here was
a dry run, not a reading.

### Third: a vacuous check is most dangerous exactly where the change is largest

**`P7` returned `PASS` over two empty maps in the merge that flips a
prerequisite, rewrites a gate block and moves a pin.** §12. **The larger the
change, the more a green reads as assurance, and this green carries none.**

### The landed inaccuracy that arrives with this merge and is NOT repaired here

**`specs/2026-08-13T0740Z_adopt-admissibility-contract.md`, line 150**, instructs
whoever integrates to *"verify afterwards that all four pins in the merged file
match their targets"*.

**There are TWO pins in the merged file, not four.** **A7 measures two, both
matching, and §7 lists them.** **The sentence conflated how many times a pin was
moved across the two branches — the parameter-domain pin moved twice and the
contract pin once — with how many pins the file ends up carrying.**

**It is arriving content and this task does not edit it.** **It is named here by
file and line, with the measured count beside it**, so a later reader following
that instruction is not left counting to four.

## 15. Does `main` now read as though a phase had been found?

**No.** **And the question is worth answering carefully, because this is the
largest thing this line has landed.**

**What a reader of `GATES.md` meets:** a gate whose `Status:` is `PROPOSED`,
whose two prerequisites read `Satisfied`, and whose two prerequisite blocks each
carry an explicit limit — one saying adoption certifies no phase, the other
saying a rule exists and nothing has been assessed against it. **`Required
computations` reads `(not started)`.**

**What the landed artifacts say:** the adopted domain artifact's boundary
statement — *"Adoption freezes the enumeration window and the treatment of
inputs. It does not certify root completeness, full-space stability,
thermodynamic dominance, negative-`G` exclusion, or finite-density coverage."*
The adopted contract's standalone *What adoption does NOT establish* section.
`C1`'s and `C3`'s findings, **both of which removed evidential weight and added
none** — the negative-mass branch's stored position is fixed by the
Wilson-complement identity and its curvature ratio by that position and a
prefactor. **The C-check register's three open items, one of which qualifies
`C1`'s own exactness verdict as resting on a refuted argument.**

**Nothing in the landed set names a candidate as admissible, and nothing was
evaluated against standard C during this integration.** **The one thing that got
easier is asking the question**: there is now a frozen window to look in and a
frozen rule to judge by. **Both were procedural steps. Neither was a
measurement.**

## 16. The landing, as INTENDED

**Commit 7 is this report.** **The landing follows it and its evidence is
post-report**, so nothing in this section is a measurement.

**INTENDED:** verify `git merge-base --is-ancestor 1cb5550f <commit 7>` and
report the exit status; then `git push origin <commit 7>:refs/heads/main`
**without `--force` and without `--force-with-lease`**; then read `main` back
from the remote and confirm the four source tips are unchanged.

**If a fast-forward is not available, STOP** — the landing is not converted into
a merge. **The branch descends from `1cb5550f…`, which is the base of every one
of the four merges (§3), so a fast-forward is expected to be available.**

## 17. Stops and clarifications

### `SPECIFICATION_DEFECT` — none

**No stop condition fired.** Exactly two conflicts arose, in the two named
paths; both resolutions applied as written; the byte comparison held; the scope
figures matched at both heads; and RUN 2 passed. **Every prediction in §11's
pre-issue record that this task could check was confirmed** — the four refs, the
two ancestry statuses, the conflict count and paths, the 25/3 scope, the two
matching pins, the fourteen sections, and the four merge commits.

**One prediction was corrected in advance by the specification itself and the
correction is confirmed:** §12's clause about RUN 1's subject set says seven, not
six. **MEASURED seven.**

### `OBSERVATION_METHOD_ERROR` — one, self-caught before it reached the report

**My first tree-wide conflict-marker search was not tree-wide.** It excluded
`specs/`, `reports/` and `reviews/`, and returned "none" — **the right answer for
the wrong reason.** A5 says explicitly *"search all files, not only the two"*.
**Re-run over all 363 tracked files, the search found one hit**, in this task's
own specification at line 203, where A5 quotes the marker characters as literals.
**The correct search both proves the property and explains its only apparent
counterexample; the truncated one proved nothing.** §5 reports both runs.

**A second method decision, recorded because it is what makes A5 meaningful.**
The `GATES.md` resolution was applied with three coded assertions — the identity
of each side, and **that `MICROSCOPIC PARAMETER DOMAIN` appears in neither.**
**Had the block fallen inside the markers, the resolution would have aborted
rather than taken a side whole.** It did not fall inside, so the assertion passed
and the byte comparison then confirmed the block unchanged. **The check that
would have caught the failure ran even though the failure did not occur.**

### `REPOSITORY_DEFECT` — one, pre-existing, out of scope

**`P7` is vacuous against the real `GATES.md`.** §12, §14. Known, untouched,
**and not offered as evidence for anything in this report.** **It is now landed
on `main` in a state where it will return `PASS` for any future gate edit**, and
the repair waits on `governance/p1-declared-total`, which this task does not
merge.

### `ENVIRONMENT` — none

**No environment failure occurred.** **`CONVENTIONS.md` Rule 13 carries two
conflicting diagnostic orders, a known open item; neither was exercised**, and I
am not naming one as having applied. Nothing was installed.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — none

**The two conflict resolutions were authored by the specification and reviewed
before they were written**, which is what kept an integration task from authoring
content. **I substituted; I did not decide.** The landing authority is in §7 of
the same specification, so no second task is required and none was assumed.

### Secondary findings, kept separate

- **RUN 1 and RUN 2 are not byte-identical here**, unlike every earlier task in
  this line — RUN 1 carries seven P1 subjects and RUN 2 one. **The six excluded
  all measured PASS in RUN 1**, so the narrowing hid nothing, and I can say that
  only because RUN 1 was run. §12.
- **Every property returned `PASS` for the first time in this line**, because
  the range now contains merges (P5) and reports (P9).
- **The contract draft has four distinct blobs across base, two sources and the
  head** — the signature of a genuine reconciliation. §9.
- **`P1` read this specification's `stated:` line as prose and summed it to 29**,
  matching a 29-path counted set. Right answer, wrong mechanism; the repair is
  unlanded. §12.
- **The two prerequisite blocks are separated by one blank line**, which is what
  made the `GATES.md` conflict certain rather than possible, and what the
  admissibility task measured and corrected. §14.

### Anything ambiguous, unsatisfiable, or that I would have specified differently

- **A5's "search all files, not only the two" is the criterion that caught my
  own shortcut**, and it is well drafted. **What I would add is that the search
  will legitimately hit the specification that describes it** — a criterion whose
  correct execution produces a hit it must then explain should say so, or the
  executor is tempted to exclude the directory that produces it. **Which is
  exactly what I did on the first attempt.**
- **A9's three-universe separation is the best-drafted criterion in this
  specification.** Folding the twenty-three arrivals, the two modified drafts and
  the one path matching neither source into a single count would have produced
  three incompatible numbers, and the specification says so in those words.
- **A3 asks for the merge-base "derived separately", which cannot be fully
  independent**: `git merge-base` takes the two parents as input, so the third
  value depends on the first two. **I cross-checked the parentage against
  `git rev-list --parents`, which is an independent path to the parents**, but
  the merge-base is derived and not independently observed. **A specification
  wanting three genuinely independent values would have to name a second method
  for the base.**
- **§7 names the landing target as "commit 7" rather than a SHA, and gives the
  reason** — any SHA naming a commit that carries this task's review is
  unreachable, because Rule 15 places commits after it. **That is the cleanest
  statement of the recursion problem this programme has produced**, and it is
  worth reusing.
- **Nothing in this task verified that the four sources' own reports are
  accurate.** They arrive blob-identical and are integrated as reviewed. **An
  integration checks that what was reviewed is what lands; it does not re-check
  the review.**
