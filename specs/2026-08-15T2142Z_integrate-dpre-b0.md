# Task specification — integrate the transfer-matrix and reflection-positivity scope assessment, and land it

Specification evidence base: `e70f55def26a96ffc325c0ae3231223e4623c76b`

    Branch to create   science/integrate-dpre-b0
    Cut from           authoritative main @ e70f55de…
    Source             science/dpre-b0-tm-rp-scope
                       fbb37c57…

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This is the integration authorization AND the landing authorization.**
§7 carries the landing clause; **no second task is required.**

**One merge, measured clean.** Dry run from the evidence base: **no
conflict**, merge-base `e70f55de…`, **6 additions and 0 modifications at
the merge commit.** **Any conflict is an immediate STOP.**

**Nothing is modified.** No gate, no pin, no register, no script.

---

## 0. Four load-bearing conclusions, and why this task re-derives them

**The Reviewer will not approve landing on the strength of an execution
summary**, and **is right not to.** Four conclusions carry the scientific
weight of this branch, and **each changes what the programme does next:**

    twelve of twelve cells NOT DETERMINABLE, zero REFUTED
    only proposition (ii) can discriminate — eight cells cannot
    the overlap with D-pre-B is 3 of 9, and shared as INPUTS
    seven to eleven distinct constructions

**Each is re-derived by this task, from the artifact and the frozen
text, not read from the report.** §5's criteria say how.

**The third is the one that changed the programme's plan.** Both the
Researcher and the Reviewer expected transfer-matrix normalisation to be
the joint. **It is not, once `(i)` is separated from `(ii)`** — and the
three items that ARE shared are shared as inputs, not as constructions.
**Two lines needing the same setup fixed is weaker overlap than two
needing the same theorem**, and that distinction is what turns one large
task into two with a preliminary.

## 1. What lands

**A scope assessment that answers what the work is, and does none of
it.**

    derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md

**Twelve cells `NOT DETERMINABLE BY THIS TASK`. Zero `REFUTED`.**

**Within `B0`'s admitted evidence and methods, none of the twelve cells
can be settled without proceeding beyond scope assessment into
substantive proof or construction work.**

**That is a statement about `B0`'s boundary, not about every possible
route.** **An earlier draft said nothing about any proposition can be
settled for any candidate without construction work** — **a claim about
all future methods, which no scope assessment can establish.** **`B0`
itself leaves literature verification undone**, and a theorem whose
hypotheses were shown to cover the declared action could in principle
settle a cell by applicability rather than by construction.

**Only `(ii)` would discriminate, derived from the frozen text.** Line 71
states the obligation as a condition on the action — that is `(ii)`.
Line 74 describes `(i)` as *sufficient, in that finite model* — **so a
failed finite transfer matrix refutes a route, not the obligation.**
Line 85 says which axis is time *is not a selection problem*, and `(iii)`
is its own deliverable. **Four cells could carry discriminating
information; eight structurally cannot.**

**Recommendation: two pieces of work with a shared preliminary.**
**Neither written.**

## 2. What this does NOT establish

- **No candidate is eliminated, preferred, or ranked.** **Zero
  `REFUTED`** means no negative candidate evidence exists.
- **A scope assessment is not a result.** **Knowing what the work is
  does not make any candidate more or less admissible**, and nothing
  here brings the programme closer to a phase verdict.
- **Even completing the work may not discriminate.** **Four
  `ESTABLISHED` results would discriminate exactly as little as four
  `NOT ESTABLISHED` results.** **The estimate counts constructions, not
  outcomes**, and that possibility is not priced into it. **Report this
  where a reader meets the estimate.**
- **Zero literature claims have `COVERAGE` reaching the declared
  action.** The estimate is robust to their accuracy **because none of
  them covers what the programme needs** — **a property of this claim
  set, not a general margin.**
- **The estimate's lower bound rests on an undetermined question** —
  whether `(iii)` levels 2–3 are absorbed by the transfer-matrix
  construction is itself `NOT DETERMINABLE BY THIS TASK`, which is why
  the range stays wide.
- **`C-iii` and `D0` are not unblocked.**

## 3. Two findings carried, neither registered

**3a. Reflection positivity's value is not operator selection.**

**Line 181 freezes it as an obligation.** **Discharging it is required
whether or not it eliminates anything.** **Eliminating a candidate is a
possible outcome, not the success criterion**, and a report that frames
the work as a selection tool misstates why it must be done.

**3b. Four artifacts now share near-identical section numbering.**

`derivations/P2-LATTICE-MICROSPEC-01_*` — the dossier, the discriminants,
the plaquette provenance, and the arriving scope assessment — **all carry
a `§4.1`, a `§5.2`, and so on.** **The source task wrote two
cross-references from memory and both pointed at the wrong file**; it
caught them and re-verified every remaining reference.

**A citation of the form `§4.1` without a filename is ambiguous across
four landed artifacts.** **This is adjacent to `G-08` but is a different
shape: a cross-file reference that cannot be self-checked because the
namespace collides.** **Report it. Do not register it** — the register is
frozen at eleven.

## 4. What this task must not do

- **Do not touch `main` until §7's landing.**
- **Do not modify any file.** There are no authorised modifications.
- **Do not begin any construction.** **Not the reflection split, not a
  transfer matrix, not a normalisation.** **The source task reported
  stopping one step short of the reflection split and named the step
  small; a small step into forbidden work is still forbidden.**
- **Do not select, eliminate, rank or prefer a candidate.**
- **Do not write the next specification**, and do not decide whether the
  reflection-positivity work is one task or four.
- **Do not upgrade the overlap obstruction to a refutation.**
- **Do not add a register entry anywhere.**
- **Do not claim `C-iii` or `D0` is unblocked.**

## 5. Acceptance criteria

**A1 — Refs.** `refs/heads/main` resolves to
`e70f55def26a96ffc325c0ae3231223e4623c76b` and
`science/dpre-b0-tm-rp-scope` to `fbb37c57…`. **Any mismatch → STOP.**
**Report the `--is-ancestor` exit status of the source against `main`** —
expected non-zero.

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**
**If absent, blank, or naming a different digest, STOP and say which.**

**A3 — Merge parentage, three separately derived measurements**, with
parent 1 this task's review commit, parent 2 `fbb37c57…`, and the
merge-base the evidence base. **Commit 1 must be an ancestor of parent
1.**

**A4 — No conflict.** Report the conflict list. **It must be empty.**

**A5 — The twelve cells, counted FROM THE TABLE and not by grep.**
**Report the disposition of each of the twelve cells** — four candidates
× three propositions — **and the count of each disposition.**

**Then report the whole-file grep counts for the TWO cell-disposition
strings** — `NOT DETERMINABLE BY THIS TASK` and `REFUTED` — **and state
them beside the table counts.**

**Report the grep count for `UNVERIFIED FROM THIS REPOSITORY`
SEPARATELY, as a literature-evidence label and not a cell disposition.**
**It belongs with `A10`, not here.** **The Researcher's own grep returned
17, 5 and 6 and listed all three together, which conflated the two
vocabularies.**

**Against a table of twelve cells, 17 and 5 are not cell counts** —
**definitions, the disposition list and prose each contribute hits.** **A
count taken by grep over a document that defines its own vocabulary is
not a count of the thing defined**, and this criterion exists so the
difference is on the record rather than discovered later.

**Expected: twelve `NOT DETERMINABLE BY THIS TASK`, zero `REFUTED`.**
**Report what you actually measured.**

**A6 — The "only `(ii)` discriminates" derivation, re-derived.** From
`P2-LATTICE-ONTOLOGY-01` lines 71, 74 and 85 **as measured at the head**,
**derive which of the three propositions could carry discriminating
information.** **Quote each line.** **Report the count of cells that
could discriminate and the count that structurally cannot** — expected
four and eight.

**This conclusion determines the potential OPERATOR-SELECTION VALUE of
the coming work. It does not determine whether the frozen
reflection-positivity obligation is worth discharging** — **§3a says why:
line 181 freezes it, and discharging it is required whether or not it
eliminates anything.** **An earlier draft said this conclusion determines
whether the next task is worth its cost, which would have made a frozen
obligation contingent on its selection value.**

**A re-derivation that quotes the report rather than the ontology fails
this criterion.**

**A7 — The 3-of-9 overlap, re-derived item by item.** For each of
`P2-LATTICE-ROUTE-01`'s nine `D-pre-B` items, **report whether it is
required by the reflection-positivity obligation as well, by `D-pre-B`
alone, or by neither once `(i)` is separated from `(ii)`.** **Nine
results.** **Report the count shared.**

**And report, separately, whether each shared item is shared as an INPUT
or as a CONSTRUCTION.** **The source task's distinction is what turns one
large task into two, and it must be re-derived rather than repeated.**
**Confirm or refute that transfer-matrix normalisation is NOT among the
shared items once the propositions are separated** — **that single result
reversed both the Researcher's and the Reviewer's expectation.**

**A8 — The seven-to-eleven estimate, and what makes it a range.**
**Report the count of distinct constructions, the four-fold part, and
the reason the lower bound is not firm.** **Confirm that whether `(iii)`
levels 2–3 are absorbed by the transfer-matrix construction is itself
`NOT DETERMINABLE BY THIS TASK`**, and **that the range stays wide
because of it.**

**A9 — The staggered determinant identity, recomputed.** **`det(E D E) =
det(E)² det(D) = det(D)`**, and **the maximum of
`|det D(permuted) − det D|` over all 23 non-trivial axis permutations.**
**Expected `0.00e+00`.** **State the operator and lattice extent you
used**, and **state the shift convention**, per the hazard `D-pre-A3`
recorded.

**A10 — Literature claims, counted.** **Report the number recorded, the
number with all four fields, the number marked `UNVERIFIED FROM THIS
REPOSITORY`, and the number whose `COVERAGE` reaches the declared
action.** **Expected: the last is zero.** **Report the one claim the
source expressly did not count as a claim, and why.**

**A11 — The dossier does not attribute the RP results to a missing
transfer matrix**, re-verified. **Search the dossier's
reflection-positivity section at the head and report the count of
transfer-matrix mentions in it** — expected zero — **and report the line
numbers where the dossier does mention a transfer operator**, confirming
they concern the ontology line 180 and line 184 material.

**A12 — Scope, frozen manifest. Final base-to-head scope: 7 additions
and 0 modifications.**

    stated: 7 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: e70f55def26a96ffc325c0ae3231223e4623c76b
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md
      reports/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md
      reports/2026-08-XXT{HHMM}Z_integrate-dpre-b0.md
      reviews/chatgpt/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-dpre-b0.md
      specs/2026-08-15T2055Z_dpre-b0-tm-rp-scope.md
      specs/2026-08-XXT{HHMM}Z_integrate-dpre-b0.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths.** **Four arrive from the source, all additions; three are
authored here.** **Report the ARRIVING PATH count and the ARRIVING
ADDITION count separately, AND state whether they coincide** — **they do,
at four, and `D-pre-A3`'s executor observed that a guard should stay
visible when it does nothing.**

**At the merge commit the count is 6 additions and 0 modifications.**
**Report which head each figure was measured at.**

**A13 — Which merge case.** **The merge-base is the evidence base, so no
commit on `main` could have touched an arriving path** — report that,
**then** the four blob comparisons.

**A14 — Nothing existing changed.** Every path at the evidence base is
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, both lattice artifacts, all three earlier
microspec artifacts, both registers, `docs/GOVERNANCE-DEBT.md`, and
everything under `scripts/`, `tests/` and `results/`.

**A15 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; both pins match. **Report all four.**

**A16 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A17 — The checker over this task's own range**, base `e70f55de…`, head
**commit 3, the merge commit**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_integrate-dpre-b0.md

**Config for both runs, agreeing with this specification's own
declarations:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.** **`RUN 1` has two specifications in range and
both declare `DECISION_LOG.md` alone** — **verified by the Researcher
against the committed bytes of the arriving specification** — **so the
`C3` multi-specification conflict should not arise.** **Report what
`RUN 1` actually did.**

**`P7` must report fourteen sections.** **`PASS` at zero is a STOP.**

**RUN 2 is stop-governing.** **Both configs and both JSON outputs
verbatim.**

**A17-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.**

**A18 — Validators, exit status 0.** **Expected unchanged at 324 passed,
2 deselected.**

**A19 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.** **Commits 1–3 go in the report; commit 4 is post-report
evidence.**

## 6. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-dpre-b0.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-dpre-b0.md
    commit 3  --no-ff merge of fbb37c57…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-dpre-b0.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.**

**Committed report — measured at commit 3:** A1–A16, A18 and A19;
**A17's two runs with both configs verbatim**; commit 1–3 SHAs and stored
messages; commit 4's intended message; **A12's final scope stated as
INTENDED, with the measured 6/0 figure at commit 3.**

**Post-report evidence, NOT written back:** A12's final scope measured
base-to-commit-4; A17-final; A15 and A16 re-run after the advance; A19
for commit 4; the push; remote `main` read back; final ancestry
confirmation.

**Nothing in the committed report may claim to measure commit 4.**

## 7. The landing clause

**This task ends with authoritative `main` at its own final report
commit**, named as **commit 4**, not as a SHA. **The advance is a
fast-forward; `e70f55de…` is the base of this branch.** **Verify
`--is-ancestor` before the push and report the exit status as a
measurement.** **If a fast-forward is not available, STOP.** **Push
without `--force` and without `--force-with-lease`.** **The source branch
is not deleted and does not move** — verify and report its tip.

**Landing precondition specific to this merge.** **Do not advance `main`
unless A5, A6, A7 and A8 have each been re-derived and reported.**
**These four conclusions are why the branch exists**, and **a landing
that carried them without re-derivation would put the programme's next
plan on `main` resting on a summary.**

## 8. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** **Twelve `NOT DETERMINABLE` results are a determinate finding
about what `B0` could settle WITHIN ITS ADMITTED EVIDENCE AND METHODS,
and nothing more.** **They are not a theorem that no route could settle
them**, and **they are not evidence about any candidate.** **Say both
where a reader meets the table.**

**Second.** **Reflection positivity is a frozen obligation, and
discharging it is required whether or not it eliminates anything.**
**Framing the coming work as a selection tool would misstate why it must
be done**, per §3a. **Say so.**

**Third.** **The estimate counts constructions, not outcomes.** **Four
`ESTABLISHED` results would discriminate exactly as little as four
`NOT ESTABLISHED`.** **Report that beside the seven-to-eleven figure**,
and **say that a completed programme of work may leave the selection
problem exactly where it is.**

**Fourth.** **Zero literature claims cover the declared action.** **The
estimate's robustness to their accuracy is a property of this claim set,
not a general margin**, and **verifying them is work no task so far has
been able to do.** **Say that, and say it is not a gap this integration
closes.**

## 9. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Modify nothing.**
- **Do not begin construction, select, rank, or write the next
  specification.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Merge commit only for the integration: no fast-forward there, no
  squash, no rebase. **The landing is a fast-forward or a stop.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 10. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A5's twelve cells with disposition counts, AND the whole-file grep
  figures beside them**;
- **A6's re-derivation with lines 71, 74 and 85 quoted**;
- **A7's nine results, the shared count, the input-versus-construction
  classification, and the transfer-matrix-normalisation finding**;
- **A8's estimate with its basis and the reason the lower bound is not
  firm**;
- **A9's recomputation with operator, extent and shift convention
  stated**;
- **A10's four literature counts**;
- **A11's search of the dossier's RP section, with line numbers**;
- **A12's two scope figures and the arriving-path versus
  arriving-addition statement, including that they coincide**;
- **A13's merge case, stated BEFORE the blob comparisons**;
- **A14's path count**;
- **A15's four invariants**;
- **A16's six exit statuses, before and after**;
- **A17's two runs**, both configs verbatim, `declared_source` for each,
  the section count `P7` saw, and what `RUN 1` did;
- **A18's counts**;
- **§3b's cross-reference hazard, reported and not registered**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, and the source tip unchanged;
- **§8's four Rule 16 junctions**;
- **whether re-deriving the scope made you want to begin the work.**
  **Say so, and confirm you did not** — **the source task reported this
  as its strongest pull and named the remaining step small**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 11. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.** **This record covers facts about the repository AND facts
this specification asserts about itself.**

    target      refs and the merge
    method      git fetch; git rev-parse; dry run from e70f55de with two
                placeholder commits, then git merge --no-ff
    MEASURED    main = e70f55de…; source = fbb37c57…, NOT an ancestor of
                main. Merge CLEAN; merge-base = e70f55de; 6 additions
                and 0 modifications at the merge commit; 7 and 0 with a
                placeholder report; the landing fast-forward is
                available.

    target      the three ontology lines the discrimination argument
                rests on
    method      read P2-LATTICE-ONTOLOGY-01 lines 71, 74 and 85
    MEASURED    line 71 states the obligation as a condition on the
                ACTION; line 74 describes the finite transfer matrix as
                "sufficient, in that finite model"; line 85 says which
                axis is time "is not a selection problem".
    DERIVED     sufficiency is not necessity, so a failed finite
                transfer matrix refutes a route and not the obligation.
                A6 requires the executor to re-derive this rather than
                take it from here.

    target      whether the dossier attributes its RP results to a
                missing transfer matrix
    method      read the dossier's reflection-positivity section at the
                head and count transfer-matrix mentions in it; then
                locate every transfer mention in the file
    MEASURED    ZERO mentions within the reflection-positivity section.
                Transfer mentions occur at lines 271, 387, 437, 441 and
                445, which are the ontology line 180 and line 184
                material. The source task's correction stands.

    target      the twelve-cell counts
    method      grep the arriving artifact for each disposition string
    MEASURED    17 hits for NOT DETERMINABLE BY THIS TASK, 5 for
                REFUTED, 6 for UNVERIFIED FROM THIS REPOSITORY.
    NOT A COUNT OF CELLS. The artifact defines its own vocabulary, so
                definitions and prose contribute hits. A5 requires the
                cells counted from the table and BOTH figures reported.
                The author records the grep figures here so that the
                discrepancy is anticipated rather than discovered.

    target      the staggered determinant identity
    method      form E as a random diagonal sign matrix and D as a
                random 16x16 matrix; compare det(EDE) with det(D)
    MEASURED    |det(EDE) - det(D)| = 0.00e+00 with det(E)^2 = 1, which
                is the algebraic content of the identity. A9 requires
                the executor to recompute it on the actual operator with
                the extent and shift convention stated.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations. append_only carries
                one path, one per line, matching A17's config.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                e70f55de and executed — not re-implemented
    MEASURED    one scope block; stated 7 additions, 0 modifications;
                the manifest lists seven and 'modify: []' contributes
                none; parse OK, counted equals stated per category.
