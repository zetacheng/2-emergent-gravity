# Task specification — integrate the clean-room Proca construction and flat validation, and land it

Specification evidence base: `f21198cd25ae285b789b706f7c4ac0730f9fff69`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/integrate-recon-01a
    Cut from           authoritative main — refs/remotes/origin/main
    Source             science/recon-01a-construction
                       be9ee961…

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This is the integration authorization AND the landing authorization.**
§6 carries the landing clause; **no second task is required.**

**NORMATIVE EXECUTION ORDER, stated once:**

    A3  environment conformance
    A1  repository identity and refs
    A2  review binding
    A4  onward

**Criterion numbering is not execution order.**

**One merge, measured clean.** Dry run: **no conflict**, merge-base
`f21198cd…`, and the suite at the merged head reports **332 passed, 2
deselected.** **Any conflict is an immediate STOP.**

**THREE SCOPE FIGURES, MEASURED SEPARATELY. Do not conflate them.**

    source contributes            7 additions, 0 modifications
    this task authors             3 — spec, review, report
    base → merge commit (3)       9 additions  = 7 arriving + 2 already
                                                 committed (spec, review)
    base → final commit (4)      10 additions  = 7 + 3

**`9` is NOT the merge's contribution.** **It is the CUMULATIVE
base-to-head count AT the merge commit, and it already includes this
task's own first two commits.** **The merge itself brings 7.**

**Measured commit by commit in a dry run: 1, 2, 9, 10.**

**This is the first landing in this line that puts executable code on
`main`.** **Nothing existing is modified.**

---

## 0. What lands

**Two operators on a periodic `L⁴` lattice, built from covariant actions
rather than kernels written directly**, plus a validation driver and
eight tests.

    S1[A] = ¼Σ √g g^{μα}g^{νβ} F_μν F_αβ + (m²/2)Σ √g g^{μν}A_μ A_ν
    D1 + m² = G1⁻¹K1 + m²·1        G1 = √g g^{μν}

**Validations, all pre-freeze:** flat spectrum to `7.5e-14` with the
non-dispersing band at multiplicity `nsite+3`; position-space `logdet`
agreeing with the analytic momentum-block factorisation to `1.1e-12`;
the compensating scalar dispersing with nine distinct eigenvalues —
**`Δ+m²`, not the ultralocal `m²`**; two extents and two masses; and the
derivative machinery checked against a closed-form sum with error
falling `4.01`, `4.00` per halving, and against a symmetry-enforced
zero at `4.5e-11` with sign alternating and magnitude not falling —
**the signature of zero, not of small.**

**Validators 324 → 332, exactly the eight tests added.**

## 1. The finding that changes the next task

### 1a. `C5` relocates the mixing; it does not remove it

    operator  D1 + m²  (choice C5)   3.25e-16 at every amplitude, power ≈ 0
    Hessian   K1 + m² G1             1.75e-4 → 6.99e-4, power 0.99996 — O(h)

**The two are related by `K1 + m²G1 = G1(D1 + m²)`, so
`det(K1 + m²G1) = det G1 · det(D1 + m²)`.**

**The mixing did not leave the physics. It moved into `det G1`.**

**`RECON-01b` inherits this and CANNOT begin a `k`-scan until it is
settled**, because the two determinants differ by `det G1` and only the
second mixes. **A `k`-scan run before the choice is made could return a
clean-looking result from the wrong determinant.**

**Report this as the RECON line's new blocker.** **Do not settle it
here** — §3 forbids it, and settling it is a separate adjudication task.

### 1b. Spectrum agreement does not imply operator correctness

**The source executor's first kernel wrote the complex conjugate:
`p̂²δ_μν − s_μ conj(s_ν)` versus the correct form.** **Both are Hermitian
with IDENTICAL eigenvalues.**

**Validation (a), the determinant cross-check and the scalar check all
PASSED with the error present.** **The two differ only in the null
direction — the transverse and longitudinal subspaces were swapped — and
only the separation check saw it, as mixing of `0.238` where machine
zero was required.**

**Diagnosed analytically and fixed before the freeze.**

> **Spectrum agreement does not imply operator correctness.**

**`RECON-01b` and everything after must retain a projector- or
subspace-sensitive test.** **That is not optional quality assurance.**
**Say so.**

### 1c. §4(b)'s comparison was non-commensurable, and the source was right to refuse it

**The specification asked for two numbers and a comparison.** **The
source executor reported them and declined the comparison**, because its
quantity is a single-momentum operator-level mixing and `CIRC-01`'s is a
two-momentum bubble coefficient.

**`CIRC-01` itself withdrew the single-momentum measurement**, at
`:26-29` and `:50-52`, as *measured in the wrong, single-momentum
basis*. **The source's `§4(b)` falls in the class `CIRC-01` withdrew.**

**Record the outcome as `NON-COMMENSURABLE — VALIDATION TARGET MISMATCH
DISCOVERED`.** **Not `PASS`, and not a scientific discrepancy.**

**This is a specification defect of the Researcher's**: `§4(b)` assumed
the two quantities were comparable. **A curved-background validation
will need a check in `CIRC-01`'s own two-momentum basis**, and building
one is not this task's.

## 2. Two instrumentation items, reported and not resolved

**2a. `A9`'s two hits are a specification ambiguity, not contamination.**

**A broad token pattern returned two hits in the test file, both the
phrase `regression anchor` in a docstring** — **which is `GATES.md`'s
own field name and the wording the `RECON-01a` specification's `§3`
instructed.**

**`A9` said any hit in a code file is a `STOP`; `§2` defined the
forbidden thing as ANCHOR INFORMATION.** **A field name carries no
value.** **The word `anchor` was used for two different things in one
specification, and that is the Researcher's defect.**

**Record it as the source executor did — both scans, neither collapsed:**

    semantic anchor-information scan, 17 patterns   0 hits, all three files
    broad literal scan, 18th pattern                2 hits, both the field name

**Do not claim `A9` fully passed, and do not edit the frozen code to
make a checker green.** **Report the ambiguity.**

**2b. The `derivations/P2-BETAV-*` count is SIX.**

**The `RECON-01a` specification said five. The `SIGN-01` integration
said five, correcting a neighbouring count and not this one. The
`SIGN-01` specification said four.** **Three consecutive tasks carried a
literal that was one behind, each time because the preceding task added
an artifact to the very directory being counted.**

**Measured at this evidence base: six.** **`A12` states six and requires
it re-measured.**

## 3. What this does NOT establish, and what this task must not do

- **A validated flat limit does not validate the curved construction.**
  **`h = 0` switches off the coupling the reconstruction exists to
  exercise**, and **no independently known curved quantity was compared
  against.**
- **Clean-room is provenance, not correctness.** **This construction was
  clean-room throughout and was still wrong once**, and **a validation
  caught it, not its pedigree.**
- **Six conventions were fixed by the construction that `CONVENTIONS.md`
  does not fix.** **Report the count.** **If `RECON-01b` returns a wrong
  number, that list is where the search starts**, and the source names
  `C5` as the entry to try first.
- **The gate's `Regression anchors` field stays `None yet (proposed)`.**
  **Do not register the new test as the gate's anchor.** **What is
  established is a flat construction, a propagating compensator,
  validated derivative machinery and internal consistency — not an
  independent curved-observable validation.** **Promoting it now would
  be premature.**
- **Do not settle the determinant question of §1a.**
- **Do not modify any file**, including the three frozen code files.
- **Do not compute `Γ_k`, vary `k`, or compare anything to the anchor.**
- **Do not write the `RECON-01b` specification or the adjudication
  task's.**
- **Do not add a register entry anywhere.**
- **Do not push any ref but `refs/heads/main` and this task's branch.**

## 4. Acceptance criteria

**A1 — Repository and refs.** Report the `origin` remote URL as measured,
**verbatim and not normalised**; confirm it identifies
`zetacheng/2-emergent-gravity`, accepting either URL form. Fetch, then
report `refs/remotes/origin/main` and confirm it is
`f21198cd25ae285b789b706f7c4ac0730f9fff69`. **Report `refs/heads/main`
for contrast.** Report the source at `be9ee961…` and **that it is not an
ancestor of `main`.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0. **Report whether the clone is shallow
and its commit count, and the versions of every package the arriving
code imports.**

**Report `pyproject.toml:11`'s `scipy>=1.11` declaration and whether
`scipy` is installed.** **The source executor reported it declared and
absent, and that nothing broke because the construction uses `numpy`
alone.** **Verify and report; do not install anything.**

**A4 — Merge parentage, three separately derived measurements**, parent
1 this task's review commit, parent 2 `be9ee961…`, merge-base the
evidence base. **Commit 1 must be an ancestor of parent 1.**

**A5 — No conflict.** Report the conflict list. **It must be empty.**

**A6 — The freeze verified at the head.** **Report the object ids of
`scripts/recon2026/proca_curved.py`,
`scripts/recon2026/flat_validation.py` and
`tests/test_recon2026_flat_limit.py` at the source's commit `3a`, at its
commit `3b`, and at this task's head.** **Confirm all three sets are
identical.**

**That identity is the evidence that the quantitative validation target
did not reach the construction.** **It is the whole enforcement
mechanism of the staged build**, and **a landing that did not check it
would leave the isolation claim resting on prose.**

**A7 — The validations, re-derived by RUNNING the arriving code at the
merged head.** **Run `scripts/recon2026/flat_validation.py` and report
its output.** **Report the flat-spectrum residual, the `logdet`
agreement, the compensating scalar's eigenvalue count and dispersion,
and the derivative-machinery convergence.**

**This is the first integration in this line that can re-derive a source
result by EXECUTION rather than by reading.** **Do so.** **Report any
figure that differs from the source's and treat a difference as a
finding.**

**A8 — §1a's determinant relation, checked symbolically.** **Confirm
`K1 + m²G1 = G1(D1 + m²)` from the arriving code's own definitions**,
and **that `det(K1 + m²G1) = det G1 · det(D1 + m²)` follows.** **Report
the two mixing figures and their powers.**

**Report that this is `RECON-01b`'s blocker and that this task does not
settle it.**

**A9 — §1b transcribed.** Report the two kernel forms, **that their
eigenvalues are identical**, **which validations passed with the error
present**, and **which one caught it.** **Transcribe: spectrum agreement
does not imply operator correctness.**

**A10 — §1c's verdict.** Record `NON-COMMENSURABLE — VALIDATION TARGET
MISMATCH DISCOVERED`. **Quote `CIRC-01`'s `:26-29` and `:50-52`
withdrawal with lines**, and **confirm the source's quantity falls in
the withdrawn class.** **Report that the specification defect was the
Researcher's.**

**A11 — §2a's two scans, both reported.** **Do not collapse them, do not
claim `A9` fully passed, and do not edit the frozen code.**

**A12 — Nothing existing changed.** Every path at the evidence base
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, `CONVENTIONS.md`, **all SIX
`derivations/P2-BETAV-*` artifacts — re-measure the count and report
what you measure**, all seven microspec artifacts, both registers,
everything under `scripts/recovered_2026/`, and everything under
`results/`.

**`GATES.md` in particular: `Regression anchors` still reads `None yet
(proposed)`.** **Confirm it.**

**A13 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four, read SCOPED.** **Also report:**
`P2-BETAV-RECON-01` `PROPOSED`, `P2-BETAV-CIRC-01` `RUN`, `P2-BETAV-01`
`PROPOSED (deferred)`. **Confirm none changed.**

**A14 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A15 — Scope, frozen manifest. Final base-to-head: 10 additions, 0
modifications** — **7 arriving plus 3 authored here.**

**Report all four cumulative figures as measured: at commits 1, 2, 3 and
4.** **Expected 1, 2, 9, 10.** **Report the source's own contribution
separately — expected 7.**

**A reviewer read an earlier draft as saying the merge brings 9 and
computed a final total of 12.** **The figures are 7 arriving, 3
authored, 10 final; the 9 is cumulative.**

    stated: 10 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: f21198cd25ae285b789b706f7c4ac0730f9fff69
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-BETAV-RECON-01a_construction-and-flat-validation.md
      reports/2026-08-17T1653Z_recon-01a-construction.md
      reports/2026-08-XXT{HHMM}Z_integrate-recon-01a.md
      reviews/chatgpt/2026-08-17T1653Z_recon-01a-construction.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-recon-01a.md
      scripts/recon2026/flat_validation.py
      scripts/recon2026/proca_curved.py
      specs/2026-08-17T1653Z_recon-01a-construction.md
      specs/2026-08-XXT{HHMM}Z_integrate-recon-01a.md
      tests/test_recon2026_flat_limit.py
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Ten paths.** **Seven arrive, all additions; three authored here.**
**Report the ARRIVING PATH count and the ARRIVING ADDITION count
separately, and state whether they coincide** — **they do, at seven.**

**At the merge commit the CUMULATIVE base-to-head count is 9 additions
and 0 modifications**, because this task's specification and review are
already committed by then. **Report which head each figure was measured
at.**

**Measure the UTC time and use the value you measured.**

**A16 — Which merge case.** **The merge-base is the evidence base, so no
commit on `main` could have touched an arriving path** — report that,
**then** the seven blob comparisons.

**A17 — The checker over this task's own range**, base `f21198cd…`, head
**commit 3**. Two runs, `RUN 1` observational and `RUN 2` naming only
this task's specification.

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.** **`P7` must report fourteen sections.**
**`PASS` at zero is a STOP.** **RUN 2 is stop-governing.** **Both configs
and both JSON outputs verbatim.** **PARSE the output; do not grep it.**

**A17-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.**

**A18 — Validators, exit status 0.** **Expected 332 passed, 2
deselected** — measured by the Researcher at the merged head in a dry
run. **324 at the base plus the eight arriving tests.** **A different
count is a finding.**

**A19 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-recon-01a.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-recon-01a.md
    commit 3  --no-ff merge of be9ee961…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-recon-01a.md
    then      fast-forward refs/heads/main to commit 4, and push

**Committed report — measured at commit 3:** A1–A16, A18 and A19 for
commits 1–3; **A17's two runs with both configs verbatim**; commit 1–3
SHAs and stored messages; commit 4's intended message; **A15's final
scope stated as INTENDED, with the measured 9/0 figure at commit 3.**

**Post-report evidence, NOT written back:** A15's final scope measured
base-to-commit-4; A17-final; A13 and A14 re-run after the advance; A19
for commit 4; the push; remote `main` read back; final ancestry
confirmation.

**Nothing in the committed report may claim to measure commit 4.**

## 6. The landing clause

**This task ends with authoritative `main` at its own final report
commit**, named as **commit 4**, not as a SHA. **The advance is a
fast-forward; `f21198cd…` is the base of this branch.** **Verify
`--is-ancestor` before the push and report the exit status as a
measurement.** **If a fast-forward is not available, STOP.** **Push
without `--force` and without `--force-with-lease`.** **Push only
`refs/heads/main` and this task's branch — no session branch, no
`science/recon-01a-construction`, no other ref.** **The source branch is
not deleted and does not move**; verify and report its tip.

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Five junctions, all five required in the report.**

**First.** **A validated flat limit does not validate the curved
construction.** **`h = 0` switches off the metric coupling.** **Say
what a curved-background validation would require that this stage does
not provide**, and **say that `CIRC-01`'s two-momentum basis is where
such a check would have to live.**

**Second.** **`C5` relocated the mixing into `det G1`.** **`RECON-01b`
cannot begin until the determinant question is settled**, and **a
`k`-scan run before it could return a clean-looking result from the
wrong determinant.** **Say that this is a blocker discovered BY the
construction, which is what a clean-room build is for.**

**Third.** **Spectrum agreement does not imply operator correctness.**
**A wrong kernel passed three of the four validations.** **Say that
every later stage must retain a subspace-sensitive test**, and **say
that this was found by a validation and not by the construction's
provenance.**

**Fourth.** **Six conventions were fixed here that `CONVENTIONS.md` does
not fix.** **They are this task's decisions, not repository facts.**
**Report the count and say that a later reader must be able to tell the
two apart.**

**Fifth.** **`A9`'s literal condition fired on the specification's own
instructed wording.** **The checker is not green under a literal
reading and the code was not edited to make it so.** **Say both**, and
**say that the ambiguity is the specification's.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Modify nothing**, and in particular **do not touch the three frozen
  code files or `GATES.md`.**
- **Do not settle the determinant question, compute `Γ_k`, vary `k`, or
  register a regression anchor.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Merge commit only for the integration: no fast-forward there, no
  squash, no rebase. **The landing is a fast-forward or a stop.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies, and
  **A3 requires it run FIRST and reported rather than assumed.** **Rule
  13 carries two such orders, a known open item; if no environment
  failure occurs, say neither was exercised rather than naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §5 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A1's verbatim `origin` URL**;
- **A3's environment diagnosis, package versions, and the `scipy`
  finding**;
- **A4's three values, separately derived**;
- **A6's nine object ids and the identity confirmation**;
- **A7's validation output, RE-RUN not read**, with any difference
  reported;
- **A8's determinant relation with the two mixing figures and powers**;
- **A9's two kernel forms and which validation caught the error**;
- **A10's verdict, `CIRC-01`'s withdrawal quoted with lines, and the
  attribution of the specification defect**;
- **A11's two scans, uncollapsed**;
- **A12's path count with six `P2-BETAV-*` as re-measured, and the
  `Regression anchors` confirmation**;
- **A13's four invariants plus the three `BETAV` statuses**;
- **A14's six exit statuses, before and after**;
- **A15's four cumulative figures (1, 2, 9, 10) with the head each was
  measured at, the source's own contribution of 7, and the
  arriving-path statement**;
- **A16's merge case, stated BEFORE the blob comparisons**;
- **A17's two runs**, both configs verbatim, the section count `P7` saw,
  what `RUN 1` did, and confirmation the output was parsed not grepped;
- **A18's counts**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, the source tip unchanged, and
  confirmation that no other ref was pushed;
- **§7's five Rule 16 junctions**;
- **whether landing executable code made you want to run a `k`-scan,
  settle the determinant question, or register the regression anchor.**
  **Say which and why, and confirm you did not** — **the source executor
  reported being one line of arithmetic from `Γ_k` with both logdets in
  memory, and gave a reason beyond the prohibition: it did not know
  which determinant the next stage needs**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      refs, the merge, and the suite
    method      git fetch; git rev-parse; dry run from f21198cd with two
                placeholder commits, then git merge --no-ff; then
                python3 -m pytest -q at the merged head
    MEASURED    origin/main = f21198cd25ae285b789b706f7c4ac0730f9fff69;
                source = be9ee961…, NOT an ancestor of main. Merge
                CLEAN; merge-base = f21198cd; the landing fast-forward
                is available. THE SUITE AT THE MERGED HEAD: 332 passed,
                2 deselected in 32.2 seconds.
    MEASURED    cumulative base-to-head additions, commit by commit in a
                dry run with real placeholder files: 1, 2, 9, 10. The
                SOURCE's own contribution is 7 additions, 0
                modifications. This task authors 3. 7 + 3 = 10.
    NOTE        an earlier draft reported only "9 at the merge commit;
                10 with a placeholder report", and a reviewer read the 9
                as the merge's contribution and computed 9 + 3 = 12. The
                9 is cumulative and already contains this task's first
                two commits.

    target      the freeze
    method      git rev-parse <rev>:<path> for the three code files at
                the source's 1a9c4af3 and 611292b5 and at be9ee961
    MEASURED    proca_curved.py 03f46905e5, flat_validation.py
                6b21f9d6db, test_recon2026_flat_limit.py 1d7ba56726 —
                IDENTICAL at all three revisions. The staged build held.

    target      the P2-BETAV-* count
    method      git ls-tree over derivations/ at the evidence base
    MEASURED    SIX. The RECON-01a specification said five, the SIGN-01
                integration said five, the SIGN-01 specification said
                four. Three consecutive tasks carried a literal one
                behind, each because the preceding task added an
                artifact to the directory being counted. A12 states six
                and requires it re-measured.

    target      GATES.md
    method      git rev-parse f21198cd:GATES.md against be9ee961:GATES.md
    MEASURED    blob-identical. Regression anchors still reads
                "None yet (proposed)".

    target      the C5 determinant relation
    method      NOT VERIFIED by this author. K1 + m²G1 = G1(D1 + m²) and
                the mixing figures are the source executor's. A8
                requires the relation checked against the arriving
                code's own definitions.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 10 additions, 0 modifications;
                parse OK, counted equals stated per category.
