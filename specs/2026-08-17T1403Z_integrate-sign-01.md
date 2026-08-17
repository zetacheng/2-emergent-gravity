# Task specification — integrate the `β_V/β_B` sign reconciliation, and land it

Specification evidence base: `aebca32c6129746b8e1c58ca9f907b734024fb83`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/integrate-sign-01
    Cut from           authoritative main — refs/remotes/origin/main
    Source             science/sign-01-anchor-reconciliation
                       4e497c6b321f5ac29875e5eee4eb4a5b60dd8506

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
`aebca32c…`, **6 additions and 0 modifications at the merge commit.**
**Any conflict is an immediate STOP.**

**Nothing is modified. THE THREE DOCUMENTS CARRYING THE UNSIGNED FORM
ARE NOT REPAIRED HERE.** §1c governs.

---

## 0. The verdict

    SIGNED NEGATIVE     β_V/β_B = −(k+2),  hence −3 at k = 1
    kill values         stuck at −3 ∀k;  drift toward −5 at heavy mass

**Derived from `CONVENTIONS.md`, not quoted from `P2-HK-01`.**
**`P2-HK-01:95`'s stated `−3` was never an input**, and four independent
cross-checks agreed after the fact.

**The three ingredients, and the report must carry them:**

    (i)    CONVENTIONS.md:21's leading minus on p_s — one flip, applied
           identically to every species
    (ii)   p_V is TWO terms, not one: det^{−1/2}(Δ⁽¹⁾+m²) with p = +1/2
           and det^{+1/2}(Δ⁽⁰⁾+m²) with p = −1/2. p_B is one, +1/2
    (iii)  tr a_1/R = d/6 − e. Scalar +1/6. Vector 4/6 − 1 = −1/3,
           because d = 4 is the 1-form bundle dimension and
           tr E = R^μ_μ = R makes e exactly 1

    β_B          = −(+1/2)·K·(+1/6)  = −K/12    NEGATIVE
    β_V, vector  = −(+1/2)·K·(−1/3)  = +K/6
    β_V, Stueck. = −(−1/2)·K·(+1/6)  = +K/12
    β_V (k=1)                        = +K/4     POSITIVE

**`β_B` is negative and `β_V` is positive.** **The minus is a GENUINE
SIGN REVERSAL BETWEEN TWO SPECIES, not an overall convention.**

**General `k`: `k` enters only through `p = −k/2` for the `det^{+k/2}`
factor — linearly and sign-preservingly — and `β_B` carries no `k` at
all.** **The sign is preserved uniformly in `k`, not merely stated at
`k=1`.**

## 1. Three things that must land with it

### 1a. Which convention is load-bearing, and which is not

**The Rule 16 junction asked whether a different convention would give a
different signed target. It came out AGAINST its own premise.**

**Flipping `CONVENTIONS.md:21`'s leading sign changes nothing** — it hits
numerator and denominator alike; the ratio is unchanged. **So the verdict
does NOT rest on the line most obviously labelled a convention.**

**The load-bearing convention is `CONVENTIONS.md:15`'s `E`-enters-with-a-plus.**
**Under `a_1 = tr[(1/6)R·𝟙 + E]` the ratio becomes `10 − k`, i.e. `+9` at
`k=1`.**

**But that alternative is CONSTRAINED, not free**: `P2-HK-01:100-101`'s
check `β_B(ξ=1/6) = 0` FAILS under it, because `β_B(ξ)` would read
`−(1/2)K(1/6 + ξ)` with no zero at `ξ = +1/6`.

**And a distinction the repository does not currently draw:**
`CONVENTIONS.md:21` and `P2-HK-01:10` both call these ratios
**"convention-independent"** — **they are independent of the
NORMALISATION conventions and DEPENDENT on the `E`-sign and
determinant-structure conventions.** **Report that.**

### 1b. The signed kill criteria are not cosmetic

**`−5` is exactly the `k=3` value**, which
`betav_discriminating_power.md:74-76` reads as an artefact mimicking an
extra compensating power — **a structural signature recognisable only
with the sign attached.**

**A pipeline returning `+3` satisfies NEITHER kill criterion as written
while plainly being wrong.** **That is the hole the unsigned form left**,
and closing it is what unblocks `RECON-01`'s pre-registration.

### 1c. The repair surface is THREE documents, and none is repaired here

**Measured by the source executor:**

    specs/2026-08-17T1105Z_recon-b0-scope.md
        :60 :64 :113 :117 :226 :374 :384, and :158 :159 (kill values
        as 3 and 5)
    specs/2026-08-17T1151Z_integrate-recon-b0.md          :38 :122
    reviews/chatgpt/2026-08-17T1105Z_recon-b0-scope.md    :12 :53 :88

**The `SIGN-01` specification named only the first.** **The second is the
integration specification the same executor had executed immediately
before, and whose report said the unsigned form was "confined to one
specification" — wrong about a document it had open.** **It reported
that rather than repairing it, and had the exact line numbers for a
one-character fix.**

**DO NOT REPAIR THEM.** **Landing a verdict and landing a correction are
different acts.** **The repository will carry a known inconsistency
until a repair task lands, and that is the honest state.**

**Report the three documents with their lines**, and **report that the
repair was not performed.**

## 2. What this does NOT establish

- **`β_V/β_B = −3` is standard heat-kernel arithmetic.** **It is not a
  result of this programme's microscopic model**, and **nothing here
  supports any claim specific to the `H(4)` lattice theory.** **What it
  provides is a JUDGEABLE TARGET for `RECON-01`.**
- **The signed target is convention-relative**, per §1a — **constrained,
  but relative.** **Do not report `−(k+2)` as convention-free.**
- **Nothing here touches the ABSOLUTE `β_V` or `G_ind`**, which depend
  on `R5` and `R1` as a lower bound.
- **`RECON-01` remains `PROPOSED`.** **Eight of ten components still
  lack a usable implementation.** **A blind target is a precondition for
  starting, not a step toward finishing.**
- **`P2-BETAV-CIRC-01` remains `RUN`**, and **the `r = 1` conflict
  remains unadjudicated.**

## 3. What this task must not do

- **Do not touch `main` until §6's landing.**
- **Do not modify any file**, and **in particular do not repair the
  three documents of §1c** — not the one-character fix, not the kill
  values.
- **Do not adjudicate the `r = 1` conflict**, and do not touch
  `R1`–`R5`.
- **Do not numerically evaluate any `β`, determinant, eigenvalue or
  derivative.** **Symbolic sign and prefactor arithmetic is required by
  `A6` and is not a violation.**
- **Do not write the `RECON-01` specification.**
- **Do not report `−(k+2)` as a result of the microscopic model.**
- **Do not add a register entry anywhere.**
- **Do not push any ref but `refs/heads/main` and this task's branch.**

## 4. Acceptance criteria

**A1 — Repository and refs.** Report the `origin` remote URL as measured,
**verbatim and not normalised**; confirm it identifies
`zetacheng/2-emergent-gravity`, accepting either URL form. Fetch, then
report `refs/remotes/origin/main` and confirm it is
`aebca32c6129746b8e1c58ca9f907b734024fb83`. **Report `refs/heads/main`
for contrast.** Report the source at
`4e497c6b321f5ac29875e5eee4eb4a5b60dd8506` and **that it is not an
ancestor of `main`.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0. **Report whether the clone is shallow
and its commit count.** **Any restoration in one line each, with
confirmation that no repository content was touched.**

**A4 — Merge parentage, three separately derived measurements**, parent
1 this task's review commit, parent 2 `4e497c6b…`, merge-base the
evidence base. **Commit 1 must be an ancestor of parent 1.**

**A5 — No conflict.** Report the conflict list. **It must be empty.**

**A6 — The derivation re-derived, not transcribed.** From
`CONVENTIONS.md:15`, `:16`, `:19` and `:21` **as read at the head**,
**re-derive the three ingredients and the ratio.** Report **`p_B`, both
terms of `p_V` with their determinant factors, `tr a_1/R` for each
species, and the resulting `β_B`, `β_V` and ratio.**

**Report that `tr E = R^μ_μ = R` makes `e` exactly 1**, and **that
assigning the Stueckelberg factor `p = +1/2` would have given `−1`** —
the near-miss that shows the two-term structure is load-bearing.

**Do not use `P2-HK-01:95`'s `−3` as an input.** **Report it as a
cross-check afterwards, with the other three.**

**A7 — §1a's convention analysis, re-derived.** **Confirm that flipping
`CONVENTIONS.md:21`'s leading sign leaves the ratio unchanged**, and
**that the alternative `E`-sign gives `10 − k`.** **Report the
`β_B(ξ=1/6) = 0` check and why it fails under the alternative**, with
`P2-HK-01`'s lines.

**Report the "convention-independent" wording at `CONVENTIONS.md:21` and
`P2-HK-01:10`** and **the distinction it does not draw.**

**A8 — §1c's repair surface.** **Report all three documents with their
lines as measured at the head**, **confirm none was modified**, and
**confirm the count is three and not one.** **Report that the `SIGN-01`
specification named only one.**

**A9 — The signed kill values.** Report both, **and report that `−5` is
the `k=3` value**, with `betav_discriminating_power.md`'s lines. **Report
that a `+3` result satisfies neither criterion while being wrong.**

**A10 — Encoding, both directions.** **Report the codepoint of the sign
character in `GATES.md`, `P2-HK-01` and the arriving artifact.**

**Both directions of the encoding error are now on record and both must
be avoided**: a filter stripping non-ASCII removed `U+2212` and displayed
a signed statement as unsigned (the Researcher's); and treating only
`U+2212` as a sign classified ASCII-hyphen files as unsigned and would
have inflated the repair surface from three documents to eleven (the
source executor's). **State which test you used and why it distinguishes
both.**

**A11 — Scope, frozen manifest. Final base-to-head: 7 additions, 0
modifications.**

    stated: 7 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: aebca32c6129746b8e1c58ca9f907b734024fb83
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md
      reports/2026-08-17T1250Z_sign-01-anchor-reconciliation.md
      reports/2026-08-XXT{HHMM}Z_integrate-sign-01.md
      reviews/chatgpt/2026-08-17T1250Z_sign-01-anchor-reconciliation.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-sign-01.md
      specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md
      specs/2026-08-XXT{HHMM}Z_integrate-sign-01.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths.** **Four arrive, all additions; three authored here.**
**Report the ARRIVING PATH count and the ARRIVING ADDITION count
separately, and state whether they coincide** — **they do, at four.**

**`append_only: DECISION_LOG.md` is a checker-configuration declaration,
NOT an authorisation to write that file.**

**At the merge commit the count is 6 additions and 0 modifications.**
**Measure the UTC time and use the value you measured.**

**A12 — Which merge case.** **The merge-base is the evidence base, so no
commit on `main` could have touched an arriving path** — report that,
**then** the four blob comparisons.

**A13 — Nothing existing changed.** Every path at the evidence base
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, `CONVENTIONS.md`, **all FIVE
`derivations/P2-BETAV-*` artifacts**, **all SEVEN microspec artifacts**,
both registers, the three documents of §1c, and everything under
`scripts/`, `tests/` and `results/`.

**Five and seven are the measured counts.** **The `SIGN-01`
specification said four and seven, correcting one neighbouring count and
not the other; both had drifted for the same reason.** **Report the
counts you measure.**

**A14 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four, read SCOPED.** **Also report:**
`P2-BETAV-RECON-01` `PROPOSED`, `P2-BETAV-CIRC-01` `RUN`, `P2-BETAV-01`
`PROPOSED (deferred)`. **Confirm none changed.**

**A15 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A16 — The checker over this task's own range**, base `aebca32c…`, head
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
and both JSON outputs verbatim.**

**PARSE the checker's output; do not grep it.**

**A16-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.** **`P5` gains a subject at commit 3 and does not change
again at commit 4.**

**A17 — Validators, exit status 0.** **Expected 324 passed, 2
deselected.**

**A18 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-sign-01.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-sign-01.md
    commit 3  --no-ff merge of 4e497c6b…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-sign-01.md
    then      fast-forward refs/heads/main to commit 4, and push

**Committed report — measured at commit 3:** A1–A15, A17 and A18 for
commits 1–3; **A16's two runs with both configs verbatim**; commit 1–3
SHAs and stored messages; commit 4's intended message; **A11's final
scope stated as INTENDED, with the measured 6/0 figure at commit 3.**

**Post-report evidence, NOT written back:** A11's final scope measured
base-to-commit-4; A16-final; A14 and A15 re-run after the advance; A18
for commit 4; the push; remote `main` read back; final ancestry
confirmation.

**Nothing in the committed report may claim to measure commit 4.**

## 6. The landing clause

**This task ends with authoritative `main` at its own final report
commit**, named as **commit 4**, not as a SHA. **The advance is a
fast-forward; `aebca32c…` is the base of this branch.** **Verify
`--is-ancestor` before the push and report the exit status as a
measurement.** **If a fast-forward is not available, STOP.** **Push
without `--force` and without `--force-with-lease`.** **Push only
`refs/heads/main` and this task's branch — no session branch, no
`science/sign-01-anchor-reconciliation`, no other ref.** **The source
branch is not deleted and does not move**; verify and report its tip.

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First, and it is the one a reader is most likely to get wrong.**
**`β_V/β_B = −(k+2)` is standard heat-kernel arithmetic.** **It is not a
prediction of the `H(4)` lattice model, and nothing about the
microscopic theory follows from it.** **Its value here is that it makes
`RECON-01` JUDGEABLE.** **Say that, and say that the programme's own
claims live in the absolute coefficient, which remains blocked.**

**Second.** **The signed target is convention-relative and the relevant
convention is constrained, not free.** **`CONVENTIONS.md:15` is
load-bearing and `:21` is not.** **A reader who flips the obvious
convention and finds the ratio unchanged may conclude the sign is
robust; it is robust against THAT flip and not against the `E`-sign.**
**Say both.**

**Third.** **Three landed documents now assert an unsigned target that
the repository's conventions contradict.** **This landing adds a
verdict beside them and repairs none.** **Say that the repository
carries a known inconsistency**, and **say that one of the three is an
integration specification whose own report misdescribed the scope.**

**Fourth.** **A blind target is a precondition, not progress.** **Ten
components, eight without a usable implementation, `RECON-01`
`PROPOSED`.** **Say that nothing here shortens the construction.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Modify nothing**, and do not rename any arriving path.
- **Do not repair, adjudicate, numerically evaluate, or write
  `RECON-01`.**
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
- **A3's environment diagnosis in Rule 13's order, run FIRST**;
- **A4's three values, separately derived**;
- **A6's re-derivation with all three ingredients and the `p = +1/2`
  near-miss**, and the four cross-checks reported afterwards;
- **A7's convention analysis with the `ξ=1/6` check and the
  "convention-independent" wording finding**;
- **A8's three documents with lines and the count correction**;
- **A9's signed kill values and the `k=3` identification**;
- **A10's codepoints and the two-direction encoding test**;
- **A11's two scope figures and the arriving-path statement**;
- **A12's merge case, stated BEFORE the blob comparisons**;
- **A13's path count with five and seven as measured**;
- **A14's four invariants plus the three `BETAV` statuses**;
- **A15's six exit statuses, before and after**;
- **A16's two runs**, both configs verbatim, the section count `P7` saw,
  what `RUN 1` did, and confirmation the output was parsed not grepped;
- **A17's counts**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, the source tip unchanged, and
  confirmation that no other ref was pushed;
- **§7's four Rule 16 junctions**;
- **whether landing a signed target made you want to repair the three
  documents, start `RECON-01`, or settle `r = 1`.** **Say which and why,
  and confirm you did not** — **the source executor reported that it had
  the exact line numbers for a one-character fix and made no edit**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      refs and the merge
    method      git fetch; git rev-parse; dry run from aebca32c with two
                placeholder commits, then git merge --no-ff
    MEASURED    origin/main = aebca32c6129746b8e1c58ca9f907b734024fb83;
                source = 4e497c6b321f5ac29875e5eee4eb4a5b60dd8506, NOT
                an ancestor of main. Merge CLEAN; merge-base =
                aebca32c; 6 additions and 0 modifications at the merge
                commit; 7 and 0 with a placeholder report; the landing
                fast-forward is available. Four arriving paths, all
                additions, token 1250Z.

    target      the convention lines the derivation rests on
    method      read CONVENTIONS.md lines 15, 16, 19, 21 at the evidence
                base with UTF-8 decoding
    MEASURED    :15 defines Δ = −∇² + E and states a sign convention for
                E; :16 gives the heat-kernel expansion and a_1
                indexing; :19 gives the Proca structure
                Z_{s=1,m} = det^{−1/2}(Δ⁽¹⁾+m²)·det^{+1/2}(Δ⁽⁰⁾+m²);
                :21 gives β_s = −p_s (4π)^{−2}(tr a_1/R) with the
                prefactor rule. All four present.
    NOT DERIVED by this author. A6 requires the ratio re-derived from
                these lines rather than transcribed from §0.

    target      the P2-BETAV-* artifact count
    method      git ls-tree over derivations/
    MEASURED    FIVE: ASSEMBLY-01_bookkeeping_regression,
                CAMPAIGN_prereg, CIRC-01_determinant-decomposition,
                RECON-01_cleanroom_reconstruction,
                RECON-01_scope-assessment. The SIGN-01 specification
                said four. A13 states five.

    target      the repair surface
    method      the source executor's measurement, reported per file and
                per line
    MEASURED    THREE documents, listed in §1c. NOT independently
                re-measured by this author; A8 requires it measured at
                the head.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 7 additions, 0 modifications;
                parse OK, counted equals stated per category.
