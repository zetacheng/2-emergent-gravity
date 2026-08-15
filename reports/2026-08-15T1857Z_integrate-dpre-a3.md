# Execution report — integrate the plaquette-provenance result, and land it

**Specification:** `specs/2026-08-15T1857Z_integrate-dpre-a3.md`
**Specification evidence base:** `773dd2cb2ad8fb457e23150f0cb19ab80dd614a5`
**Branch:** `science/integrate-dpre-a3`, cut from authoritative `main` @ `773dd2cb…`
**Source merged:** `science/dpre-a3-plaquette-provenance` @ `4b27009fbc7692f1e22bd68a137dfbb3a1e8deab`
**Classification:** MATERIAL. Governed by Rule 15, Rule 18, and **Amendments M–P and Rules 19–21.**

**Every figure below is labelled MEASURED, DERIVED, VERIFIED or INTENDED.**
**This report is written at commit 3, the merge commit, and measures nothing at
commit 4.**

---

## 1. Outcome

**One merge, clean. Nothing auto-merged. Nothing edited. Nothing modified.**

**MEASURED at commit 3:** conflict list empty; merge-base the evidence base; **6
additions and 0 modifications**; all four arriving paths blob-identical to the
source tip; **419 of 419 paths at the evidence base blob-identical**; validators
unchanged at 324 passed, 2 deselected; all four checker invocations exit 0 with
`overall: PASS` and `P7` reading fourteen sections.

**A10 reproduces the derivation independently at the merged head**, under the
stated convention: **324 of 324** reconstruction-identity cases hold, the
plaquette is uniformly `−1` at `L = 3, 4, 5` under **integer shifts**, and the
Clifford commutator is `−1·1₄` and scalar on all six planes.

**`RUN 1` completed.** The two specifications in range declare the same
append-only set, so the multi-specification conflict the earlier integration met
did not arise — **measured during the task, not taken from the pre-issue
record.**

**A6a confirms the summary's phrasing is not in the artifact:** zero hits for
"as real" and zero for "not merely a representation". **The report does not
carry the summary's wording.**

**No candidate is eliminated, preferred or ranked. Neither `D-pre-A2` question
is ruled. The transfer matrix is not scoped.**

---

## 2. Refs — A1

**MEASURED, read from `origin` with `git ls-remote`:**

    refs/heads/main                              773dd2cb2ad8fb457e23150f0cb19ab80dd614a5
    science/dpre-a3-plaquette-provenance         4b27009fbc7692f1e22bd68a137dfbb3a1e8deab

**Both match the specification. No mismatch, no STOP.**

**MEASURED:**

    git merge-base --is-ancestor 4b27009f… origin/main      exit 1

**Non-zero, as expected — the source is not an ancestor of `main`**, which is
why there is a merge to perform.

---

## 3. The review binds to these bytes — A2, checked in the order the criterion sets

**A2 requires the field checked for PRESENCE before it is checked for MATCH.**

**Step 1 — presence. MEASURED:**

    'reviewed specification SHA-256' occurrences     1
    64-hex strings in the review                     1

**Step 2 — match. MEASURED:**

    SHA-256 of the arriving specification     48b881652c8d937a3b946098b7fb4f40e072cb96e97a71fbecfb64e58f1326cb
    SHA-256 the review records as reviewed    48b881652c8d937a3b946098b7fb4f40e072cb96e97a71fbecfb64e58f1326cb

**Equal.** Both arriving files committed byte-identical, verified by `cmp`;
neither modified.

**The two-step order is not ceremony.** Two tasks ago the field was absent
entirely, and a match test alone would have compared a digest against nothing.
**`G-05` remains the reason this is a per-task criterion rather than a
repository check.**

---

## 4. Merge parentage and the absence of conflict — A3, A4

**Three values, separately derived. MEASURED:**

    parent 1          82d31a5dc5fda61295e062786e923a6c3b274718   this task's review commit
    parent 2          4b27009fbc7692f1e22bd68a137dfbb3a1e8deab   the source tip
    merge-base(1,2)   773dd2cb2ad8fb457e23150f0cb19ab80dd614a5   the evidence base

**Each equals what A3 requires.** **The merge-base is NOT parent 1**, because
parent 1 already carries this task's specification and review.

**MEASURED: commit 1 is an ancestor of parent 1** — `--is-ancestor` exit 0. So
specification precedes review, which precedes the merge, which is Rule 15's
timing clause.

**A4, MEASURED: the conflict list is empty.** `git diff --diff-filter=U`
returns nothing and the index carries **0** unmerged entries. **MEASURED: no
`Auto-merging` line was emitted**, so Amendment `P(b)`'s line-survival check has
no auto-merge to verify.

---

## 5. Scope — A5 and A6

### 5.1 A6, derived from the SOURCE and not from A5

**MEASURED, `773dd2cb…` to `4b27009f…`:**

    A  derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md
    A  reports/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md
    A  reviews/chatgpt/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md
    A  specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md

**The two counts, stated separately as A6 requires:**

    arriving ADDITIONS      4
    arriving MODIFICATIONS  0
    arriving PATHS          4

**They coincide at four, and A6 is right that this is the case in which a
conflation is least likely to be noticed.** The previous integration's
specification conflated them where they differed — eight additions and nine
paths — and the error was visible only because the modification existed. **Here
nothing would have exposed it**, which is why both are measured and reported
rather than one being inferred from the other.

**No disagreement with A5's arithmetic: 4 arriving + 3 authored here = 7
additions, 0 modifications.**

### 5.2 The two scope figures, each with the head it was measured at

    6 additions, 0 modifications     MEASURED at commit 3, the merge commit
    7 additions, 0 modifications     INTENDED at commit 4, with this report

**The second is INTENDED, not MEASURED: this report is written before the
commit containing it.**

**MEASURED: no status code other than `A` appears at commit 3.** **`modify:` is
`[]` and remained so** — this task has no authorised modifications and made
none.

---

## 6. Which merge case — A7, established BEFORE the blob comparisons

**MEASURED, before any blob comparison was interpreted:**

    merge-base(HEAD, source)           773dd2cb2ad8fb457e23150f0cb19ab80dd614a5
    authoritative main tip             773dd2cb2ad8fb457e23150f0cb19ab80dd614a5
    commits on main after the base     0

**The merge-base IS `main`.** **No commit exists on `main` after the base, so
no commit on `main` could have touched an arriving path.**

**THE CASE IS ONE-SIDED for every arriving path.**

**Therefore a merged blob equal to the source side is the CORRECT outcome**,
and is not evidence that a side was lost. **In a two-sided merge the same
measurement would mean the opposite**, and Amendment `P(b)`'s line-survival
measurement would have been required instead.

**Here the case is simpler than the previous integration's in one respect worth
stating: all four arriving paths are ADDITIONS.** A path that did not exist at
the base cannot have a second side, so the one-sided classification is
structural rather than contingent on `main` having stood still — **though it
stood still, and that was measured first.**

### 6.1 The blob comparisons, now interpretable

**MEASURED, source tip against the merge commit:**

    derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md   5fccdda96480   IDENTICAL
    reports/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md      e8171bfd2bb1   IDENTICAL
    reviews/chatgpt/2026-08-15T1642Z_dpre-a3-…-provenance.md      5c78f9ed3851   IDENTICAL
    specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md        5612c0dc75dd   IDENTICAL

**Four of four identical. Nothing arriving by merge was edited.**

---

## 7. The summary's phrasing is not in the artifact — A6a

**MEASURED, searching the ARRIVING artifact at the source tip:**

    "as real"                          0 hits
    "not merely a representation"      0 hits

**Zero, as expected.** **The stronger phrasing exists only in the execution
summary**, and the artifact never carried it.

**The artifact's own statement of what the verdict means, MEASURED at line 380:**

> **The verdict is `REPRESENTATION-EQUIVALENT`, which is a statement that the
> four candidates carry the same structure at the level tested.**

and line 381–382 continues: *"It is not a statement that any of them is
admissible, inadmissible, better or worse suited."*

**One near-miss reported for completeness.** The word "merely" occurs once in
the artifact, at line 125: *"verified as such and not merely read off one
entry"* — **about the measurement method, not about the structure.** It is
unrelated to the forbidden phrasing and is reported because a coarser search
would have flagged it.

**This report does not carry the summary's phrasing**, and §14.1 states the
verdict at the level the artifact does.

### 7.1 The pattern, recorded and not repaired

**This is the third time in this line an execution summary has stated something
stronger than its artifact** — after *violate outright* and *physical
difference between candidates*. **The first two required specification repairs.
This one does not, because the artifact is correct and the specification that
integrates it declines to strengthen it.**

**All three were mine.** The artifacts were right each time; the summaries
compressed a qualifier out. **No register entry is added** — §4 forbids it —
and the pattern is recorded here for whoever holds the register.

---

## 8. The derivation reproduces at the merged head — A10

**Recomputed independently from the artifact at the head, not inherited from
the source report.**

**The gamma representation, stated and verified before use:**

    γ_1 = σ_x ⊗ σ_x    γ_2 = σ_x ⊗ σ_y    γ_3 = σ_x ⊗ σ_z    γ_4 = σ_y ⊗ 1₂

    {γ_μ, γ_ν} = 2δ_μν · 1₄   for all sixteen pairs    VERIFIED
    all four hermitian                                  VERIFIED

**(1) The reconstruction identity `Γ(x)† γ_μ Γ(x+μ̂) = η_μ(x) · 1₄`**, with
`Γ(x)` the ordered product `γ_1^{x_1} γ_2^{x_2} γ_3^{x_3} γ_4^{x_4}`, over a
`3⁴` block and all four directions:

    324 of 324 cases hold

**That figure equals the specification's own independent verification in §3**,
reached here by a separate computation.

**(2) The plaquette product. THE CONVENTION, STATED EXPLICITLY: INTEGER SHIFTS,
no modular identification.**

    L = 3   (81 base sites × 6 planes)    value set = {−1}
    L = 4   (256 base sites × 6 planes)   value set = {−1}
    L = 5   (625 base sites × 6 planes)   value set = {−1}

**Uniformly `−1` at all three extents.**

**A10 exists because §3 records a convention under which a correct result reads
as wrong**, so the convention is reported and not only the numbers. **Under
periodic identification at odd extent the same computation returns mixed
`{+1, −1}`** — that is the artefact §3 records, and it is a property of the
convention, not of the result.

**(3) The Clifford group commutator on all six planes:**

    plane (1,2)  −1 · 1₄   scalar     plane (2,3)  −1 · 1₄   scalar
    plane (1,3)  −1 · 1₄   scalar     plane (2,4)  −1 · 1₄   scalar
    plane (1,4)  −1 · 1₄   scalar     plane (3,4)  −1 · 1₄   scalar

**Verified scalar in every case, not read off one entry.** **That scalarity is
what makes the conjugation drop out**, so it is checked rather than assumed.

**All three reproduce. The arriving result stands at the merged head.**

---

## 9. Nothing existing changed, and the gate invariants — A8, A9, A11

**A8, MEASURED path by path, base to commit 3:**

    paths at the evidence base      419
    compared                        419
    blob-identical                  419
    differing                         0
    missing at head                   0

**The comparison excludes no path**, because this task modifies none.

**The named ones, MEASURED individually — all IDENTICAL:**

    GATES.md                                                CONVENTIONS.md
    derivations/P2-LATTICE-ONTOLOGY-01.md
    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md
    derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md
    derivations/P2-DEFERRED-ITEMS.md          (the deferred register)
    derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md
    docs/GOVERNANCE-DEBT.md                   (the governance-debt register)
    docs/BRANCHING_POLICY.md                  (the superseded-branch register)

    everything under scripts/, tests/, results/:   0 paths changed

**No register entry was added anywhere** — not for §3's convention defect, not
for the `C3` multi-specification residual. **Both are reported and left.**

**A9, all four invariants, MEASURED at commit 3:**

    1.  ^## P2- count                14
    2.  P2-PHASE-01                  Status: PROPOSED
    3.  first prerequisite           Prerequisite state: SATISFIED
    4.  second prerequisite          Prerequisite state: SATISFIED

    both pins match their targets:  line 1017 MATCH,  line 1040 MATCH

**No gate state changed, and no pinned file was modified**, so no re-pin is
owed under Rule 19.

**A11, MEASURED before the advance. Six separate exit statuses, all 1 — not
merged:**

    52f65117  exit 1        7146a093  exit 1
    ebd531ab  exit 1        10c260b9  exit 1
    40168469  exit 1        d64cd912  exit 1

---

## 10. Validators and hygiene — A13, A14

**A13, MEASURED, `python -m pytest` from the repository root, exit status 0
both times:**

    before, at the base 773dd2cb     324 passed, 2 deselected
    after,  at commit 3              324 passed, 2 deselected

**Unchanged, as expected: neither the source nor this task adds a test.** **No
change to explain.**

**A14, MEASURED on commits 1–3. Commit 4 is post-report evidence.**

    commit 1   e2c9857e   spec: integrate the plaquette-provenance result, and land it
               trailer hits 0      not amended
    commit 2   82d31a5d   review: pre-execution review for the plaquette-provenance integration
               trailer hits 0      not amended
    commit 3   c36073b6   merge: integrate the plaquette-provenance result
               trailer hits 0      not amended

**MEASURED over the whole range: a scan for `Co-Authored-By`, `claude.ai/code`,
`Generated with`, `Claude-Session` and `noreply@anthropic` returns nothing.**

**Rule 20 binds this task and was NOT exercised.** **No force-push, no branch
deletion, no history rewrite of any kind.**

---

## 11. Commits

    commit 1   e2c9857ec855109b6c4404095a26be127bc613a5   specs/2026-08-15T1857Z_integrate-dpre-a3.md
    commit 2   82d31a5dc5fda61295e062786e923a6c3b274718   reviews/chatgpt/2026-08-15T1857Z_integrate-dpre-a3.md
    commit 3   c36073b60134bb5edf1c8e65829ed6d7d1967dcc   --no-ff merge of 4b27009f…

**Commit 2 precedes the merge**, per Rule 15's timing clause.

**Commit 4's message, INTENDED:**

    report: the plaquette-provenance result lands on main

---

## 12. The checker — A12, MEASURED at commit 3

    base   773dd2cb2ad8fb457e23150f0cb19ab80dd614a5
    head   c36073b60134bb5edf1c8e65829ed6d7d1967dcc   (commit 3, the merge commit)

**All four invocations exited 0 with `overall: PASS`.**

    run 1 INCLUSIVE   exit 0   PASS   sha256 4c0c2e79a9359a66ebc1990e20b0496a7bb72d0035930cd295baedfc6f98e5e4
    run 1 EXCLUSIVE   exit 0   PASS   sha256 ce075faa6a582fb3a5c7dacaa581b052b1affd67a8ea4f346e9b9ad79df9e2a0
    run 2 INCLUSIVE   exit 0   PASS   sha256 a3634c8e7d99f404bd75e5255b40a17f429b229295b2756a1b7f43f2ad8d3ed5
    run 2 EXCLUSIVE   exit 0   PASS   sha256 4ae37f6992aa4fc4c03df1385fa4bb61d2a9728ac5fafdb65dc92564ff757999

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 PASS
    P6 PASS   P7 PASS   P8 PASS   P9 PASS

**Nine of nine, in every invocation.** No property returned `NOT_DECLARED`,
`NOT_PARSEABLE` or `DECLARATION_CONFLICT`.

### 12.1 What `RUN 1` actually did — the question A12 asks explicitly

**A12 predicts `RUN 1` has TWO specifications in range, both declaring
`append_only: DECISION_LOG.md` alone, so the multi-specification conflict the
earlier integration met should not arise — and requires the outcome measured
during the task rather than taken from the pre-issue record.**

**MEASURED: `RUN 1` completed. It did not raise.**

    specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md   stated 4 / 0   counted 4 / 0   parse OK
    specs/2026-08-15T1857Z_integrate-dpre-a3.md              stated 7 / 0   counted 7 / 0   parse OK

**Two specifications selected, exactly as predicted, and both parsed.**
**MEASURED: `P3` resolved to a single declared set, `['DECISION_LOG.md']`, with
`declared_source: specification`** — which is the checker reporting that the two
subject specifications agree, since a difference is what `_declarations_from_specs`
raises on.

**This is the first multi-specification range in this line to complete.** The
earlier integration's range carried three specifications declaring two different
sets and the run raised; here two specifications declare one set and it does
not. **The contrast confirms the earlier diagnosis: the limitation is a
difference between declarations, not a count of them.**

**The `C3` residual is unchanged and remains unregistered.** A multi-source
integration whose sources touch different append-only paths will still raise.
**This range does not exhibit that shape**, and no register entry is added.

### 12.2 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "773dd2cb2ad8fb457e23150f0cb19ab80dd614a5",
      "head": "c36073b60134bb5edf1c8e65829ed6d7d1967dcc",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 12.3 RUN 2 config, verbatim — stop-governing

    {
      "base": "773dd2cb2ad8fb457e23150f0cb19ab80dd614a5",
      "head": "c36073b60134bb5edf1c8e65829ed6d7d1967dcc",
      "specification_paths": ["specs/2026-08-15T1857Z_integrate-dpre-a3.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I chose**; all are fixed by A12. **Neither
the config nor this specification's declarations were adjusted to make RUN 2
pass** — §8 forbids both, and neither was touched.

### 12.4 `declared_source`, `P3` and `P7`

**MEASURED, identical in all four invocations:**

    P3   PASS   declared_source: specification   declared: ['DECISION_LOG.md']
           DECISION_LOG.md   PASS   deleted 0   base is byte prefix of head: True
    P7   PASS   declared_source: specification   declared: []
           section_count_head 14

**`P7` reports fourteen sections. `PASS` at zero would have been a STOP.**

**MEASURED: `DECLARATION_CONFLICT` appears nowhere in any of the four
outputs.**

**`DECISION_LOG.md` is not modified by this range**, so its `PASS` records an
absence of change rather than a verified append. **The distinction is worth
keeping**: this task declares one append-only path and modifies none, so `P3`
passed without exercising the append property at all.

### 12.5 RUN 2 output, verbatim, INCLUSIVE reading

    {
      "base": "773dd2cb2ad8fb457e23150f0cb19ab80dd614a5",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "c36073b60134bb5edf1c8e65829ed6d7d1967dcc",
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
              "counted": 7,
              "counted_add": 7,
              "counted_modify": 0,
              "counted_set": [
                "derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md",
                "reports/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-dpre-a3.md",
                "reviews/chatgpt/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-dpre-a3.md",
                "specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-dpre-a3.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-15T1857Z_integrate-dpre-a3.md",
              "stated": 7,
              "stated_add": 7,
              "stated_modify": 0,
              "stated_record": "stated: 7 additions, 0 modifications"
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
                "commit": "e2c9857ec855109b6c4404095a26be127bc613a5",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "82d31a5dc5fda61295e062786e923a6c3b274718",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "c36073b60134bb5edf1c8e65829ed6d7d1967dcc",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md"
                ]
              }
            ],
            "first_review_commit": "82d31a5dc5fda61295e062786e923a6c3b274718",
            "first_work_commit": "c36073b60134bb5edf1c8e65829ed6d7d1967dcc",
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
              "specs/2026-08-15T1857Z_integrate-dpre-a3.md"
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
              "merge": "c36073b60134bb5edf1c8e65829ed6d7d1967dcc",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "773dd2cb2ad8fb457e23150f0cb19ab80dd614a5",
              "recomputed_parent_1": "82d31a5dc5fda61295e062786e923a6c3b274718",
              "recomputed_parent_2": "4b27009fbc7692f1e22bd68a137dfbb3a1e8deab",
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
              "commit": "e2c9857ec855109b6c4404095a26be127bc613a5",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "82d31a5dc5fda61295e062786e923a6c3b274718",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "36dd627fdad09a4512bd42dc69d8271fd915619b",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "4bddf8bbf2619d2f18a808d5bcda196c3bc941df",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "f2fe7036fb500badc341d670790bc77617646fff",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "4b27009fbc7692f1e22bd68a137dfbb3a1e8deab",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "c36073b60134bb5edf1c8e65829ed6d7d1967dcc",
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
              "specs/2026-08-15T1857Z_integrate-dpre-a3.md"
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
            "first_commit": "e2c9857ec855109b6c4404095a26be127bc613a5",
            "first_commit_paths": [
              "specs/2026-08-15T1857Z_integrate-dpre-a3.md"
            ],
            "reports_added": [
              "reports/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-15T1857Z_integrate-dpre-a3.md",
              "reviews/chatgpt/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-15T1857Z_integrate-dpre-a3.md",
              "specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md"
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
              "path": "reports/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md",
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

## 13. Did landing a closed derivation make me want to select an operator or scope the transfer matrix?

**Asked by §9, and the answer is no to the first and yes to the second.**

**On selecting an operator: no, and the reason is structural rather than
creditable.** This result **removes a candidate discriminator, not a
candidate.** After it lands, the four candidates are exactly as
indistinguishable as before — one fewer way of telling them apart. **There is
nothing to select on**, and a closed derivation that closes a route does not
feel like an invitation to choose.

**On scoping the transfer matrix: yes, and it was the strongest pull in this
task.** Three cheap routes are now tried; reflection positivity is the
outstanding requirement among those identified; it needs a transfer matrix; and
`D-pre-B` needs transfer-matrix normalisation too. **The sentence "these should
be scoped together" writes itself**, and I have now written the observation
that they share a construction in three consecutive reports.

**Writing it again is not scoping it, and the line between them is thinner than
it looks.** Naming an overlap is a measurement. Proposing that two tasks be
combined, estimating what the combination would cost, or listing what it would
have to establish are all scoping, and none appears here. **§8 forbids it, and I
did not do it.**

**A third pull was toward the word "exhausted".** §2 requires reporting that
**the three cheap routes identified and tested so far** are exhausted, and the
shorter phrasing — *the cheap discriminators are exhausted* — is one word away
and reads better. **It is also one step from "only reflection positivity
remains", which nothing establishes.** §14.1 and §14.3 use the long form.

**I confirm I selected no operator, eliminated, preferred and ranked no
candidate, ruled on neither `D-pre-A2` question, scoped neither the transfer
matrix nor `D-pre-B`, added no register entry, and modified nothing.**

---

## 14. Rule 16 assessment — what the assembled set does NOT establish

**Rule 16 is operative. All four junctions are addressed.**

### 14.1 First junction — a closed derivation is the opposite of progress toward selection

**After this lands, `main` carries a closed derivation with a definite verdict.
That looks like progress toward selecting an operator. It is the opposite.**

**This result removes a candidate discriminator rather than a candidate.**

**MEASURED from the landed artifacts: all four candidates survive**, and they
carry the same invariant, differing only in representation — gammas for
`naive`, `Wilson` and `overlap`, link phases for `staggered`.

**The three cheap routes now tried, per §2:**

    isotropy reading      elimination is of a PRESENTATION, and only under
                          the stronger reading
    finite-range case     elimination costs a NEW ontology commitment that
                          ontology line 115 does not require
    plaquette phase       no difference — all four carry the same invariant

**Under the weaker reading of each question, all four candidates survive.**

**THE THREE CHEAP ROUTES IDENTIFIED AND TESTED SO FAR ARE EXHAUSTED.** **That
is not the claim that cheap routes in general are exhausted, and it is not the
claim that the selection problem is nearly solved.** Neither is established,
and §14.3 is why the distinction is kept.

### 14.2 Second junction — this is not corroboration of the dossier

**The derivation and the dossier's staggered ledger rest on the same
reconstruction** — the identity `Γ(x)† γ_μ Γ(x+μ̂) = η_μ(x) · 1₄`.

**So agreement between them is not independent support.** If that identity were
wrong, this derivation and the dossier's taste count would be wrong together,
and their consistency would be silent about it. **The agreement is a
consequence of shared machinery.**

**A10's re-derivation does not change this.** It re-derived the identity from
the same starting point, which confirms the arithmetic and not the premise.

### 14.3 Third junction — the outstanding requirement, and what is not established about it

**Reflection positivity is the outstanding requirement among those ALREADY
IDENTIFIED.** It is `NOT ESTABLISHED` for all four candidates and waits on a
transfer matrix that does not exist.

**It is NOT established to be the only discriminator that could exist**, and
this report does not write it as the only one.

**Nothing establishes that the space of redefinition-invariant structures is
exhausted.** The comparison that landed here is at one level — the plaquette,
and the translation sector, which turned out to be the same level. **Higher
loops, larger loop-like objects, structures involving mass terms, and anything
outside the free-field phase-and-gamma comparison were not examined.**

**The source specification had to be revised once for exactly this
overreach**, and the revision is why §3's consequence and §7's fourth junction
agree in the landed artifact instead of denying each other. **A consequence and
a limitation that contradict each other cannot both be true, and an artifact
carrying both would have been unusable to the PI.**

### 14.4 Fourth junction — the correction and its cause land in the same merge

**A specification defect of the Researcher's is landing inside the artifact
that corrects it.**

**The source specification's pre-issue record named "81 base sites" without
stating the shift convention** — and `81 = 3⁴` is exactly the extent at which
periodic identification produces mixed signs. **The arriving artifact records
the convention**, at its §1 and §7.1, because a reader reproducing the
measurement on a periodic odd lattice would disagree with a correct result.

**Both land in this merge. A reader meets the correction and the cause in the
same commit, and NOTHING IN THE REPOSITORY LINKS THEM.** The specification does
not point forward to the artifact that corrects it, and the artifact does not
point back to the specification that caused the confusion.

**That is `G-03` in the governance-debt register, unrepaired**: *"A false
`MEASURED` line and its correction landed in the same merge with no pointer
between them; the shape recurred."* **It has recurred again, here, in this
merge.**

**No register entry is added** — §4 forbids it, and `G-03` already carries the
shape. **The instance is reported.**

---

## 15. Stops and clarifications

**No stop occurred.** All four checker invocations exited 0, RUN 2 passed at
both prospectivity readings, the conflict list was empty, `RUN 1` completed,
and no acceptance criterion failed.

    SPECIFICATION_DEFECT                          0 stops, 1 finding
    ENVIRONMENT                                   0 stops, 0 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 0 findings
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 2 findings

### 15.1 `SPECIFICATION_DEFECT` — one finding, in the SOURCE specification, carried and not repaired

**The source specification's pre-issue record named "81 base sites" for the
plaquette measurement and did not state the shift convention.** §14.4 gives the
consequence.

**Not a stop, and not repaired.** The source is landed as reviewed; §4 forbids
modifying any arriving file, and the correction is already inside the arriving
artifact. **The defect is the Researcher's**, and the criterion should have
stated the convention rather than the extent.

**MEASURED here at the merged head: under integer shifts the plaquette is
uniformly `−1` at `L = 3, 4, 5`**, so the specification's figure was right and
its method description was silent on the one convention that changes the
answer.

### 15.2 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — two findings, both carried

**First: `G-03`'s shape has recurred in this merge** — a correction and its
cause landing together with nothing linking them. §14.4. **Reported; no entry
added.**

**Second: the `C3` multi-specification residual remains unregistered.** §12.1
measures that it did not arise here, because the two subject specifications
agree, and confirms the earlier diagnosis that the trigger is a difference
between declarations rather than a count. **Reported; no entry added**, §4
forbidding it.

### 15.3 `OBSERVATION_METHOD_ERROR` — none this task

**No probe of mine contradicted a committed check or a written figure.** A10's
three recomputations were run under the convention §3 records, stated before
the numbers, precisely because the previous task met the artefact.

**The convention was carried forward rather than rediscovered**, which is what
recording it in the artifact was for.

### 15.4 `ENVIRONMENT` and `REPOSITORY_DEFECT` — nothing to report

**No environment failure occurred.** **Rule 13 carries two diagnostic orders, a
known open item. Neither was exercised**, and I am not naming one as having
applied. **Nothing was installed.** Python 3.11.15 and pytest 9.1.1, as
present.

**No defect in the repository was found by this task.**

### 15.5 What I would have specified differently

**A6 asks for the arriving-path and arriving-addition counts separately and
says this is the case where a conflation is least likely to be noticed — and it
is right, but the criterion cannot detect the conflation it guards against.**
Here both counts are four. **A criterion that asked for them separately AND for
a statement of whether they coincide would make the guard visible when it does
nothing**, which is when a guard is most likely to be quietly dropped in a
later task.

**I report both counts and the fact that they coincide** in §5.1, which is what
I would have had the criterion require.

**Nothing in the specification was unsatisfiable or ambiguous enough to require
a stop.** The one place a prior specification in this line was wrong — the
arriving-path arithmetic — this one gets right, and says why it is easy to get
wrong.

---

## 16. Evidence layering

**Committed in this report, MEASURED at commit 3:** A1–A11, A13 and A14 for
commits 1–3; A12's four invocations with both configs and the output; commits
1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; A5's final
base-to-commit-4 scope of 7 additions and 0 modifications.

**Post-report evidence, returned to the Reviewer and NOT written back:** A5's
final scope measured base-to-commit-4; A12-final, being RUN 2 re-run at commit
4 before the landing; A9 and A11 re-run after the advance; A14 for commit 4;
the pre-advance `--is-ancestor` exit status; the exact push command; remote
`main` read back; the source tip unchanged; final ancestry confirmation.

**Nothing in this report claims to measure commit 4.**
