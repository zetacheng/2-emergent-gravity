# Task specification — `DET-01`: which determinant the vector effective action requires

Specification evidence base: `8108c29846adb3b69c4ea73ab66a1c04b66106dc`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/det-01-measure-adjudication
    Cut from           authoritative main — refs/remotes/origin/main

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This task does not touch `main`.** Integration is a separate task.

**NORMATIVE EXECUTION ORDER, stated once:**

    A3  environment conformance
    A1  repository identity, refs, branch availability
    A2  review binding
    A4  onward

**Criterion numbering is not execution order.**

**THE JUDGEMENT IS COMMITTED BEFORE ANY CANDIDATE IS EVALUATED
NUMERICALLY.** §2 is the mechanism and it is not optional.

---

## 0. The question

**`RECON-01a` landed an identity, verified against the arriving code's
own definitions:**

    K1 + m²G1 = G1(D1 + m²)
    det(K1 + m²G1) = det G1 · det(D1 + m²)

**and measured `logdet(G1) = −1.1338458300` at amplitude `0.08` on a
curved background, `0.0000000000` flat.** **`det G1 ≠ 1` when the metric
is switched on**, so this is not a harmless algebraic rewriting.

**ALGEBRAICALLY, the difference between the two determinant
representations is carried by `det G1`.** **Whether that factor belongs
to the physical one-loop effective action is the question `DET-01`
adjudicates.**

**An earlier draft said the mixing "moved into `det G1`" and did not
leave the physics.** **That is one step stronger than what is
established**: the identity is arithmetic, and where the factor belongs
is the open question.

> **Which object does the vector one-loop effective action require?**

    Γ_vector  ~  log det(D1 + m²)          — det G1 outside the action
    Γ_vector  ~  log det(K1 + m²G1)        — C5 an intermediate only
    Γ_vector  ~  a combination carrying an explicit log det G1 as
                 path-integral measure or field-space Jacobian

**`RECON-01b` cannot begin until this is settled.** **A `k`-scan run
first would return a number belonging to whichever determinant happened
to be picked** — **and it would look clean precisely because `C5`
removes the mixing from the object scanned.**

## 1. What the repository does and does not fix

**Measured at the evidence base: `CONVENTIONS.md` fixes the HEAT-KERNEL
side and says nothing about the functional measure.**

    :14   Fourier transform and the LOOP measure ∫d⁴p/(2π)⁴
    :19   Proca structure Z = det^{−1/2}(Δ⁽¹⁾+m²)·det^{+1/2}(Δ⁽⁰⁾+m²)
    :21   β_s = −p_s (4π)^{−2}(tr a_1/R), prefactor rule

**No line addresses the path-integral measure, the field-space metric,
or a change-of-variables Jacobian.** **`A5` requires this search re-run
and reported, including a null result.**

**So `NOT DETERMINABLE` is a real and expected outcome** — **and if it
is the answer, this task's product is a stated PI decision, not a
derived one.** **Do not manufacture a determination from an absence.**

**`:19` is the closest thing to a constraint and must be examined
carefully.** **It states the Proca structure as a ratio of determinants
with no measure factor written.** **Report whether that silence
constrains the answer, or whether `:19` is a continuum statement whose
lattice realisation is exactly what is in question.**

## 2. The judgement is frozen before any candidate is evaluated

**This task's characteristic danger is specific and is not the same as
`SIGN-01`'s.**

**`SIGN-01`'s derivation was symbolic — there was nothing to try.**
**Here, `RECON-01a`'s code is on `main`, the three candidates are
numerically separable, and `logdet(G1)` is already measured.**
**Computing `Γ_k` for the three and seeing which one gives the expected
ratio is available, cheap, and would destroy the adjudication.**

**Therefore the commit sequence is staged:**

    commit 3a   the adjudication artifact — the derivation and the
                verdict, from measure theory and the repository's
                conventions ONLY. No candidate evaluated numerically.
    commit 3b   the numerical appendix, if any — permitted only AFTER
                3a is committed, and it may not alter the verdict.

**After `3a` the verdict is FROZEN.** **If the numerical appendix shows
something unexpected, you report it as a finding; you do not revise the
verdict.**

**`A9` requires the `3a` artifact blob-identical at `3a`, `3b` and the
head.** **That identity is the evidence, not the prose.**

**And do not compute `Γ_k` for any candidate at any stage of this
task** — **not in `3b` either.** **The appendix, if you write one, may
report `logdet` values for the individual objects; it may NOT assemble
them into `Γ_k` or any quantity comparable to the ratio anchor.**

## 3. What the adjudication must derive from

**Four sources, and the verdict must name which carried it:**

    (i)    the continuum Proca functional measure — what is integrated
           over, and with what measure
    (ii)   THE CANDIDATE lattice field-space metric. G1 = √g g^{μν}
           appears as the mass and inner-product matrix in the landed
           construction. DETERMINE whether it is ALSO the metric that
           defines the functional integration measure. DO NOT ASSUME
           THAT IT IS. If it is, derive the induced measure factor and
           its coefficient. If it is not, identify what fixes the
           actual field-space measure.
    (iii)  the change-of-variables Jacobian between the two natural
           field parametrisations
    (iv)   CONVENTIONS.md's determinant convention at :19 and :21

**Report each separately, and report which of the four is
load-bearing.**

**Source `(ii)` is a QUESTION, not a premise.** **An earlier draft of
this specification asserted that `G1` is a metric on the space of
1-forms rather than merely a matrix in the operator** — **which is part
of what `DET-01` must decide.** **Had it stood, a `MEASURE-EXPLICIT`
verdict could have looked derived while resting on a premise the
specification inserted.** **`SIGN-01` found that the convention most obviously
labelled a convention was NOT the one carrying the result; expect the
same possibility here and check for it.**

**The selection criterion is what the measure requires.** **IT IS NOT
which candidate is easier, which is already implemented, or which would
be expected to reproduce any anchor.** **Selecting on the last would
derive the microscopic content from the answer it is supposed to
test** — the inversion this whole line exists to avoid.

## 4. The pre-registered verdicts

**Fixed before the executor derives. Not renegotiated afterwards.**

    OPERATOR-DETERMINANT
        Γ_vector ~ log det(D1 + m²); det G1 does not enter the
        effective action. Name what carries it.

    HESSIAN-DETERMINANT
        Γ_vector ~ log det(K1 + m²G1); C5 is an intermediate quantity
        only. Name what carries it.

    MEASURE-EXPLICIT
        an explicit log det G1 enters as path-integral measure or
        field-space Jacobian, with a stated coefficient. State the
        coefficient and what fixes it.

    NOT DETERMINABLE
        the repository's frozen conventions do not fix it. Name what a
        PI would have to rule, and what each ruling would commit the
        programme to.

**`NOT DETERMINABLE` is legitimate and may well be correct.** **§1
measured that no convention line addresses the functional measure.**
**A verdict of `NOT DETERMINABLE` that names the missing convention
precisely is more useful than a determination argued from silence.**

**If the derivation establishes something none of these represents,
STOP and report a `SPECIFICATION_DEFECT`.**

## 5. What this task must not do

- **Do not touch `main`**, do not merge.
- **DO NOT COMPUTE `Γ_k` FOR ANY CANDIDATE, at any stage**, and do not
  vary `k`.
- **Do not evaluate any candidate numerically before `3a` is
  committed.**
- **Do not select on which candidate reproduces an expected ratio**, and
  **do not read the ratio anchor, `P2-HK-01`, `betav_discriminating_power.md`
  or `P2-BETAV-SIGN-01_anchor-reconciliation.md` during this task.**
  **You know the anchor; the requirement is that it not enter the
  derivation.**
- **Do not modify any existing file**, including the three frozen
  `scripts/recon2026/` files and `GATES.md`.
- **Do not register a regression anchor.**
- **Do not write the `RECON-01b` specification.**
- **Do not adjudicate `r = 1`**, and do not touch `R1`–`R5`.
- **Do not add a register entry anywhere.**
- **Do not push any ref but this task's branch.**

## 6. Acceptance criteria

**A1 — Repository, refs, branch availability.** Report the `origin`
remote URL as measured, **verbatim and not normalised**; confirm it
identifies `zetacheng/2-emergent-gravity`, accepting either URL form.
Fetch, then report `refs/remotes/origin/main` and confirm it is
`8108c29846adb3b69c4ea73ab66a1c04b66106dc`. **Report `refs/heads/main`
for contrast.**

**Report whether `science/det-01-measure-adjudication` already exists.**
**If it does, STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0. **Report whether the clone is shallow
and its commit count.** **Any restoration in one line each, with
confirmation that no repository content was touched.**

**A4 — The identity re-verified.** **Confirm
`K1 + m²G1 = G1(D1 + m²)` from the landed code's own definitions**, and
**report `logdet(G1)` flat and at a curved amplitude.** **This is
permitted and required — it is the premise, not a candidate
evaluation.**

**A5 — The convention search, re-run.** **Search `CONVENTIONS.md` for
any statement of the path-integral measure, the field-space metric, or a
change-of-variables Jacobian.** **Report the search terms and the
result, INCLUDING A NULL RESULT.**

**Report `:14`, `:19` and `:21` in full**, and **report whether `:19`'s
silence on a measure factor constrains the answer or is a continuum
statement whose lattice realisation is the open question.**

**A6 — The four sources of §3**, each reported separately, **with which
one carries the verdict.** **If the load-bearing source is not the one
most obviously labelled a convention, say so** — `SIGN-01` found exactly
that.

**A7 — The verdict**, one of §4's four, **with its derivation.**

**If `MEASURE-EXPLICIT`: state the coefficient of `log det G1` and what
fixes it.** **If `NOT DETERMINABLE`: name the missing convention
precisely, and state what each possible ruling would commit the
programme to.**

**A8 — What the verdict implies for `RECON-01b`.** **State which object
`RECON-01b` must scan**, or, if `NOT DETERMINABLE`, **that it cannot
begin until a ruling lands.** **Do not write the scan specification.**

**A9 — The freeze verified.** **Report the object id of the `3a`
artifact at commits `3a`, `3b` and the head.** **All three identical.**
**If you wrote no numerical appendix, say so and report that `3b` does
not exist**, and adjust the commit sequence accordingly — **that is a
permitted and clean outcome.**

**A10 — No candidate evaluated before the freeze, and no `Γ_k` at all.**
**Search the artifact, any appendix, the report and the commit messages
for any assembled `Γ_k`, any `k`-dependent quantity, and any comparison
to a ratio.** **Report the search and the result.**

**Report separately whether you read the four withheld documents.**
**A disclosed reading is recoverable; an undisclosed one makes the
isolation claim unverifiable.**

**A11 — Scope, frozen manifest.**

    stated: 4 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: 8108c29846adb3b69c4ea73ab66a1c04b66106dc
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-BETAV-DET-01_measure-adjudication.md
      reports/2026-08-XXT{HHMM}Z_det-01-measure-adjudication.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_det-01-measure-adjudication.md
      specs/2026-08-XXT{HHMM}Z_det-01-measure-adjudication.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths.** **The numerical appendix, if you write one, goes INTO
the adjudication artifact as a clearly separated section committed at
`3b` — it is not a fifth path.** **If your derivation needs a file this
manifest does not name, STOP and report.**

**Report the cumulative base-to-head figures at each commit**, and
**state which head each was measured at.** **A reviewer of a recent task
read a cumulative figure as a contribution and computed a total three
higher; report both kinds separately.**

**`append_only: DECISION_LOG.md` is a checker-configuration declaration,
NOT an authorisation to write that file.**

**Measure the UTC time and use the value you measured.**

**A12 — Nothing existing changed.** Every path at the evidence base
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, `CONVENTIONS.md`, **every
`derivations/P2-BETAV-*` artifact — re-measure the count and report
what you measure**, all seven microspec artifacts, the three
`scripts/recon2026/` files at their frozen object ids, both registers,
and everything under `results/`.

**The `P2-BETAV-*` count was wrong in three consecutive specifications
and right in the fourth, each time because the preceding task added an
artifact to the directory being counted.** **Re-measure; do not carry a
number.**

**A13 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four, read SCOPED.** **Also report:**
`P2-BETAV-RECON-01` `PROPOSED`, `P2-BETAV-CIRC-01` `RUN`, `P2-BETAV-01`
`PROPOSED (deferred)`, and **`Regression anchors` still `None yet
(proposed)`.**

**A14 — The checker over this task's own range**, base `8108c298…`, head
**the last content commit** — `3b` if you wrote an appendix, `3a` if you
did not. Two runs, `RUN 1` observational and `RUN 2` naming only this
task's specification.

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.** **`P7` must report fourteen sections.**
**`PASS` at zero is a STOP.** **RUN 2 is stop-governing.** **Both configs
and both JSON outputs verbatim.** **PARSE the output; do not grep it.**

**A14-final, post-report evidence:** re-run RUN 2 at commit 4.

**A15 — Validators, exit status 0.** **Expected 332 passed, 2
deselected.** **A change is a finding.**

**A16 — Commit-message hygiene** on every commit. **Rule 20 binds this
task.**

## 7. Commit order and evidence layering

    commit 1   specs/2026-08-XXT{HHMM}Z_det-01-measure-adjudication.md
    commit 2   reviews/chatgpt/2026-08-XXT{HHMM}Z_det-01-measure-adjudication.md
    commit 3a  derivations/P2-BETAV-DET-01_measure-adjudication.md
                 — the derivation and the verdict. FROZEN after this.
    commit 3b  the same file, appendix section only, IF you write one
                 — permitted only after 3a exists; may not alter the
                   verdict
    commit 4   reports/2026-08-XXT{HHMM}Z_det-01-measure-adjudication.md

**If you write no appendix, there is no `3b` and the sequence is four
commits.** **Say which you did.**

**Committed report — measured at the last content commit:** A1–A13, A15
and A16; **A14's two runs with both configs verbatim**; commit SHAs and
stored messages; commit 4's intended message; **A11's final scope stated
as INTENDED.**

**Post-report evidence, NOT written back:** A11's final scope measured
base-to-commit-4; A14-final; A15 at commit 4; A16 for commit 4; the
push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 8. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** **An adjudication is a decision about what the theory means,
not a discovery about what is true.** **Whichever verdict lands, no
number changes and no measurement is added.** **Say that**, and **say
that `RECON-01b`'s result will inherit this choice** — **so if that
result later looks wrong, this verdict is among the first places to
look.**

**Second.** **`NOT DETERMINABLE` would mean the programme has been
computing one-loop determinants without a frozen functional measure.**
**That is a finding about the repository, not only about this task.**
**Say so if it is the outcome**, and **say that it would apply to work
already landed, not only to work ahead.**

**Third.** **This task evaluates no candidate against the anchor and
therefore cannot be wrong in the way a scan can be wrong.** **It can be
wrong in a worse way: silently, by choosing a measure that makes a later
number come out right.** **The staged freeze is the only evidence
against that**, and **`A9`'s object ids are the whole of it.**

**Fourth.** **`RECON-01a`'s construction fixed six conventions that
`CONVENTIONS.md` does not fix.** **This adjudication may depend on one
of them** — **`C5`, the choice of what "the operator" means relative to
the mass metric, is the one the source executor named first.** **Report
whether the verdict depends on any of the six**, and **if it does, say
that the verdict is conditional on a construction choice rather than on
the repository.**

## 9. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  adjudication artifact. **Nothing else, at all.**
- **No file existing at the evidence base may be modified.**
- **Do not compute `Γ_k`, vary `k`, or compare to any ratio.**
- **Do not evaluate a candidate before `3a` is committed.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **Push only this task's branch.** **No session branch, no other
  branch, and not `main`.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies, and
  **A3 requires it run FIRST and reported rather than assumed.** **Rule
  13 carries two such orders, a known open item; if no environment
  failure occurs, say neither was exercised rather than naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 10. Report contract

- everything in §7 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A1's verbatim `origin` URL and the branch-availability check**;
- **A3's environment diagnosis in Rule 13's order, run FIRST**;
- **A4's identity re-verification and both `logdet(G1)` values**;
- **A5's search with its terms and result, including a null result**,
  and the `:19` assessment;
- **A6's four sources with the load-bearing one named**;
- **A7's verdict with its derivation**;
- **A8's implication for `RECON-01b`**;
- **A9's three object ids and whether a `3b` exists**;
- **A10's search and the four-document reading statement**;
- **A11's cumulative figures per commit, contributions reported
  separately**;
- **A12's path count with the `P2-BETAV-*` count re-measured**;
- **A13's four invariants, the three `BETAV` statuses, and the
  `Regression anchors` value**;
- **A14's two runs**, both configs verbatim, the section count `P7` saw,
  what `RUN 1` did, and confirmation the output was parsed not grepped;
- **A15's counts**;
- **§8's four Rule 16 junctions**;
- **whether deriving made you want to evaluate a candidate, assemble
  `Γ_k`, or choose the measure that would give a familiar answer.**
  **Say which and why, and confirm you did not** — **the previous
  executor reported being one line of arithmetic from `Γ_k` with the
  logdets already printed, and this task starts from that position**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 11. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      the evidence base
    method      git fetch; git rev-parse origin/main
    MEASURED    8108c29846adb3b69c4ea73ab66a1c04b66106dc, the head
                landed by the RECON-01a integration, carrying the three
                frozen scripts/recon2026/ files.

    target      whether CONVENTIONS.md fixes the functional measure
    method      read every line of CONVENTIONS.md matching measure,
                jacobian, path integral, functional, field-space or det
    MEASURED    :14 fixes the Fourier transform and the LOOP measure
                ∫d⁴p/(2π)⁴; :19 fixes the Proca determinant structure;
                :21 fixes β_s and the prefactor rule. NO LINE addresses
                the path-integral measure, the field-space metric, or a
                change-of-variables Jacobian. The remaining matches are
                governance text about measurement discipline.
    CONSEQUENCE NOT DETERMINABLE is a real possibility and §4 makes it
                legitimate. A5 requires the search re-run rather than
                taken from here.

    target      the identity and the measured logdet
    method      NOT VERIFIED by this author. K1 + m²G1 = G1(D1 + m²),
                ‖difference‖ 0.000e+00 flat and 6.434e-17 at amplitude
                0.08, and logdet(G1) = −1.1338458300 at that amplitude
                are the RECON-01a integration executor's measurements,
                verified there against the arriving code. A4 requires
                them re-verified.

    target      whether this specification prejudges its own question
    method      inspection of an earlier draft of §3(ii)
    MEASURED    it stated that G1 "is a metric on the space of 1-forms,
                not merely a matrix in the operator".
    RETRACTED   what RECON-01a established is that G1 appears as the
                mass and inner-product matrix in the discrete action and
                Hessian, and that K1 + m²G1 = G1(D1 + m²) follows. That
                does not establish that G1 defines the functional
                integration measure, nor fix any power of det G1 in it.
                §3(ii) now asks the question instead of answering it.

    target      the danger specific to this task
    method      comparison with SIGN-01
    DERIVED     SIGN-01's derivation was symbolic and had nothing to
                try. Here the code is on main, the three candidates are
                numerically separable, and logdet(G1) is already
                measured — so evaluating them and picking the one that
                gives a familiar ratio is available and cheap. §2's
                staged freeze exists for that, and A9's object ids are
                its only evidence.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 0 modifications;
                parse OK, counted equals stated per category.
