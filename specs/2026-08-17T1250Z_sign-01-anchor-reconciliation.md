# Task specification — `SIGN-01`: reconciling the `β_V/β_B` anchor sign

Specification evidence base: `aebca32c6129746b8e1c58ca9f907b734024fb83`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/sign-01-anchor-reconciliation
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

**IT COMPUTES NOTHING AND BUILDS NOTHING.** It determines which signed
form the repository's own conventions require, so that `RECON-01` can be
pre-registered.

---

## 0. Why this blocks, and why it is small

**`RECON-01` is a BLIND comparison.** The target is kept out of code and
tests and compared only at the end. **A target whose sign is undecided
is not a blind target**: a pipeline returning `+3` could be read as a
sign-convention artefact or as a failure, **and that reading would be
made after seeing the number.**

**Both kill criteria are sign-specific.** *Stuck at `−3`* and *stuck at
`3`* are different tests.

**The discrepancy, measured at the evidence base with bytes preserved:**

    GATES.md          β_V/β_B = −(k+2), kill values −3 and −5
    P2-HK-01          β_V/β_B = −3 at k=1
    RECON-B0 spec     (k+2), 3, 5 — UNSIGNED

**The unsigned form is the Researcher's**, carried into the `RECON-B0`
specification from `CIRC-01` without checking it against the gate.
**Both landed science artifacts carry the signed form and each flags the
unsigned specification.**

**So this may not be a contradiction between two conventions at all.**
**It may be one convention plus one specification error.** **Determining
which is the task.**

## 1. The question, stated so it can come out either way

> **Under the repository's own frozen conventions, what signed value is
> the correct pre-registration target for `β_V/β_B` at general `k`?**

**Three outcomes are available and all are legitimate:**

    SIGNED NEGATIVE      the conventions require −(k+2); the unsigned
                         form in the RECON-B0 specification is an error
                         and is recorded as one
    SIGNED POSITIVE      the conventions require +(k+2); GATES.md and
                         P2-HK-01 carry a sign error
    NOT DETERMINABLE     the conventions do not fix the sign, and
                         fixing it is a PI ruling this task prepares
                         rather than makes

**`NOT DETERMINABLE` is a real outcome.** **If the sign depends on a
convention the repository states two ways, or on a choice nobody has
frozen, say so** — **do not resolve it by preferring the form that
appears more often.**

## 2. What the sign actually depends on, and where to look

**Measured: `CONVENTIONS.md:21` defines**

    β_s = −p_s (4π)^{−2} (tr a_1 / R)

**with `p_s` the log-det prefactor — `+1/2` per bosonic `det^{−1/2}`
factor, `−1/2` per `det^{+1/2}` factor or fermion loop.**

**So the sign of `β_V/β_B` follows from three things**, and you must
report each separately:

    (i)    the sign convention in β_s's own definition — the leading −p_s
    (ii)   the prefactors p_V and p_B for the two species
    (iii)  the sign of tr a_1 / R for each

**Derive the ratio from `CONVENTIONS.md:21` and `P2-HK-01`'s stated
`a_1` values.** **Report every intermediate sign.** **A verdict that
quotes `−3` from `P2-HK-01` without re-deriving it fails `A5`** — the
question is what the conventions REQUIRE, not what a document says.

**Then check the general-`k` form.** **`P2-HK-01` states the `k=1`
case.** **The `(k+2)` generalisation is in
`derivations/betav_discriminating_power.md`.** **Report whether the
generalisation preserves the sign, and whether it was derived under the
same convention.**

**Measured occurrence counts of `β_V/β_B` at the evidence base**, so you
know where to read: `GATES.md` 16, `P2-HK-01` 3,
`betav_discriminating_power.md` 3, the `RECON-B0` assessment 4,
`CONVENTIONS.md` 1.

## 3. Read the bytes

**The sign character in `GATES.md` and `P2-HK-01` is `U+2212`, not
ASCII hyphen.** **A display filter that strips non-ASCII removes the
character in dispute.**

**The Researcher did exactly this once and nearly reported the gate as
unsigned.** **Enumerate codepoints rather than displaying filtered
text**, and **report the codepoint of every sign character you rely
on.**

## 4. What this task must not do

- **Do not touch `main`**, do not merge.
- **Do not modify `GATES.md`, `P2-HK-01`, `betav_discriminating_power.md`,
  `CONVENTIONS.md`, or the `RECON-B0` assessment.** **Whatever the
  verdict, the repair is a separate task.** **Landing a verdict and
  landing a correction are different acts, and this task performs only
  the first.**
- **Do not NUMERICALLY EVALUATE any `β`, determinant, eigenvalue or
  derivative.** **Symbolic determinant factors and prefactor and sign
  algebra are PERMITTED AND REQUIRED by `A5`–`A6`** — `det^{−1/2}`,
  `det^{+1/2}`, `p_s = ±1/2`, and the resulting signed ratio are the
  deliverable, not a violation. **The derivation is symbolic: signs and
  prefactors.**
- **Do not adjudicate the `r = 1` conflict**, and do not touch `R1`–`R5`.
- **Do not judge whether the historical Finding 5 is circular.**
  **`CIRC-01` remains `RUN`.**
- **Do not write the `RECON-01` specification.**
- **Do not resolve `NOT DETERMINABLE` by majority of occurrences.**
  **Sixteen mentions in `GATES.md` is not sixteen derivations.**
- **Do not add a register entry anywhere.**
- **Do not push any ref but this task's branch.**

## 5. Acceptance criteria

**A1 — Repository, refs, branch availability.** Report the `origin`
remote URL as measured, **verbatim and not normalised**; confirm it
identifies `zetacheng/2-emergent-gravity`, accepting either URL form.
Fetch, then report `refs/remotes/origin/main` and confirm it is
`aebca32c6129746b8e1c58ca9f907b734024fb83`. **Report `refs/heads/main`
for contrast; a lagging local ref is not a stop.**

**Report whether `science/sign-01-anchor-reconciliation` already
exists.** **If it does, STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0. **Report whether the clone is shallow
and its commit count.** **Any restoration in one line each, with
confirmation that no repository content was touched.**

**A4 — The four statements, quoted with codepoints.** For each of
`GATES.md`, `P2-HK-01`, `betav_discriminating_power.md` and the
`RECON-B0` assessment, **quote the ratio statement with its line number,
and report the codepoint of the sign character or its absence.**
**Report `CONVENTIONS.md:21` in full.**

**A5 — The ratio re-derived from the conventions.** Report **each of
§2's three ingredients separately**, then the ratio.

**Derive it. Do not quote it.** **A verdict resting on `P2-HK-01`'s
stated `−3` rather than on `CONVENTIONS.md:21`'s rule fails this
criterion**, because the question is what the conventions require.

**Report `p_V` and `p_B` with the determinant factors they come from**,
and **the sign of `tr a_1 / R` for each species.**

**A6 — The general-`k` form.** Report where `(k+2)` is derived, **whether
that derivation uses `CONVENTIONS.md:21`'s sign rule**, and **whether the
sign is preserved at general `k` or only stated at `k=1`.**

**Report the two kill values under your verdict** — what *stuck at
degenerate* and *heavy-mass drift* become as signed numbers.

**A7 — The verdict**, one of §1's three, **with the derivation behind
it.**

**If `SIGNED NEGATIVE` or `SIGNED POSITIVE`: name every document that is
now inconsistent with the verdict, with lines.** **Do not correct
them.** **List them so the repair task knows its scope.**

**If `NOT DETERMINABLE`: name the convention that is missing or stated
two ways, with lines**, and **state what a PI would have to rule.**

**A8 — No majority reasoning.** **Search the artifact and report that
the verdict does not rest on how many documents state a given form.**
**Report the occurrence counts anyway** — they say where to read, not
what is true.

**A9 — Nothing NUMERICALLY EVALUATED, nothing corrected.**

**Search the artifact, the report and the commit messages for any NEW
NUMERICAL RECONSTRUCTION OUTPUT**: numerically evaluated `β`
coefficients, determinant values, eigenvalues, finite-difference or
derivative outputs, fitted quantities, or reconstruction-run results.

**EXPRESSLY EXCLUDED from this search**: governance measurements, line
numbers, SHAs, quoted repository values, **and the symbolic sign and
prefactor arithmetic that `A4`–`A6` REQUIRE** — including `p_V` and
`p_B`, the determinant factors they come from, the derived signed ratio,
and the signed kill values.

**An earlier draft searched for "any numerical `β` value, determinant or
eigenvalue result".** **`A5` requires `p_V` and `p_B` with their
determinant factors; `A6` requires the two signed kill values; `A4`
requires `−3` and `−5` quoted.** **A correct execution would have
violated that search by satisfying those criteria.**

**The distinction is `symbolic reconciliation` versus `numerical
reconstruction`, and only the second is forbidden.**

**Then search separately for any edit to a document other than this
task's own four paths.** **Report both searches.**

**A10 — Scope, frozen manifest.**

    stated: 4 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: aebca32c6129746b8e1c58ca9f907b734024fb83
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md
      reports/2026-08-XXT{HHMM}Z_sign-01-anchor-reconciliation.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_sign-01-anchor-reconciliation.md
      specs/2026-08-XXT{HHMM}Z_sign-01-anchor-reconciliation.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths. `modify:` is `[]` and must remain so.**

**`append_only: DECISION_LOG.md` is a checker-configuration declaration,
NOT an authorisation to write that file.** **If they appear to conflict,
§8 governs; stop and report.**

**Measure the UTC time and use the value you measured.**

**A11 — Nothing existing changed.** Every path at the evidence base
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, `CONVENTIONS.md`, all four
`derivations/P2-BETAV-*` artifacts, all seven microspec artifacts, both
registers, and everything under `scripts/`, `tests/` and `results/`.

**Seven microspec artifacts, not six** — the previous executor measured
seven where its specification said six, and reported the count it
measured.

**A12 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four, read SCOPED to the gate section.**
**Also report, scoped:** `P2-BETAV-RECON-01` `PROPOSED`,
`P2-BETAV-CIRC-01` `RUN`, `P2-BETAV-01` `PROPOSED (deferred)`.
**Confirm none changed.**

**A13 — The checker over this task's own range**, base `aebca32c…`, head
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

**PARSE the checker's output; do not grep it.** **Measured by the
previous executor: a grep of any output returns `NOT_DECLARED` once and
`NOT_PARSEABLE` twice, both from definitional prose, while every actual
status value is `PASS`.**

**A13-final, post-report evidence:** re-run RUN 2 at commit 4.

**A14 — Validators, exit status 0.** **Expected 324 passed, 2
deselected.**

**A15 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 6. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_sign-01-anchor-reconciliation.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_sign-01-anchor-reconciliation.md
    commit 3  derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md
    commit 4  reports/2026-08-XXT{HHMM}Z_sign-01-anchor-reconciliation.md

**Committed report — measured at commit 3:** A1–A12, A14 and A15;
**A13's two runs with both configs verbatim**; commit 1–3 SHAs and
stored messages; commit 4's intended message; **A10's final scope stated
as INTENDED.**

**Post-report evidence, NOT written back:** A10's final scope measured
base-to-commit-4; A13-final; A14 at commit 4; A15 for commit 4; the
push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** **A sign verdict does not correct anything.** **Whichever way
it goes, at least one landed document is left inconsistent with it**,
and **this task lists them rather than repairing them.** **Say that the
repository will carry a known inconsistency until a repair task lands.**

**Second.** **This unblocks `RECON-01`'s PRE-REGISTRATION and nothing
else.** **Ten components remain, eight without a usable
implementation.** **A blind target is a precondition for starting, not a
step toward finishing.**

**Third.** **The verdict rests on `CONVENTIONS.md:21`'s sign rule.**
**If that rule is itself a convention rather than a derived result,
then the sign is conventional too** — **and a different convention
would give a different signed target without any physics changing.**
**Say whether `CONVENTIONS.md:21` is stated as a convention or as a
derivation**, and **say what follows.**

**Fourth.** **Nothing here touches the ABSOLUTE `β_V` or `G_ind`.**
**`A8b` established those depend on `R5` and `R1`, as a lower bound.**
**A signed ratio target does not make the absolute quantity
assemblable.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  reconciliation artifact. **Nothing else, at all.**
- **No file existing at the evidence base may be modified.**
- **Do not compute, correct, adjudicate `r = 1`, or write `RECON-01`.**
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

## 9. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A1's verbatim `origin` URL and the branch-availability check**;
- **A3's environment diagnosis in Rule 13's order, run FIRST**;
- **A4's four quoted statements with line numbers and sign codepoints**,
  and `CONVENTIONS.md:21` in full;
- **A5's three ingredients separately, then the derived ratio**;
- **A6's general-`k` finding and the two signed kill values**;
- **A7's verdict with its derivation, and the list of documents left
  inconsistent — or the missing convention if `NOT DETERMINABLE`**;
- **A8's statement that the verdict does not rest on counts, with the
  counts reported anyway**;
- **A9's two searches**, with the exclusion of `A4`–`A6`'s required
  symbolic arithmetic stated;
- **A10's scope**;
- **A11's path count, with seven microspec artifacts**;
- **A12's four invariants plus the three `BETAV` gate statuses**;
- **A13's two runs**, both configs verbatim, the section count `P7` saw,
  what `RUN 1` did, and **confirmation that the output was parsed rather
  than grepped**;
- **A14's counts**;
- **§7's four Rule 16 junctions**;
- **whether deriving the sign made you want to correct a document, start
  `RECON-01`, or settle `r = 1`.** **Say which and why, and confirm you
  did not**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      the evidence base
    method      git fetch; git rev-parse origin/main
    MEASURED    aebca32c6129746b8e1c58ca9f907b734024fb83, the head
                landed by the RECON-B0 integration.

    target      where the ratio is stated
    method      count occurrences of β_V/β_B per file, bytes preserved
    MEASURED    GATES.md 16; P2-HK-01 3;
                betav_discriminating_power.md 3; the RECON-B0
                assessment 4; CONVENTIONS.md 1.
    NOTE        these counts say WHERE TO READ. §4 forbids using them as
                evidence of which form is correct.

    target      the sign rule
    method      read CONVENTIONS.md line 21
    MEASURED    "β_s = −p_s (4π)^{−2} (tr a_1 / R), where p_s is the
                log-det prefactor of the species (+1/2 per bosonic
                det^{−1/2} factor, −1/2 per det^{+1/2} factor / fermion
                loop)." The leading minus is part of the definition.
    NOT DERIVED by this author: whether this rule yields −(k+2) or
                +(k+2). A5 requires it derived, not quoted.

    target      the sign characters
    method      earlier reading with and without a non-ASCII filter
    MEASURED    GATES.md and P2-HK-01 carry U+2212, not ASCII hyphen. A
                tr -cd '[:print:]' filter removed them and displayed the
                gate as unsigned. §3 requires codepoints enumerated.

    target      the microspec artifact count
    method      the RECON-B0 integration executor's measurement
    MEASURED    SEVEN, where its specification said six. A11 states
                seven.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 0 modifications;
                parse OK, counted equals stated per category.
