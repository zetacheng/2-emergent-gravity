# Task specification — integrate the configuration provenance verdict, and land it

Specification evidence base: `de547d9d6e152f6be0ef2215cb30c9c3fe3bd248`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/integrate-src-01a
    Cut from           authoritative main — refs/remotes/origin/main
    Source             science/src-01a-configuration-provenance
                       6193df29eddd911c8e5829b3745fc342b5dc8065

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This is the integration authorization AND the landing authorization.**
§6 carries the landing clause; **no second task is required.**

**NORMATIVE EXECUTION ORDER, stated once:**

    A3  environment conformance
    A1  repository identity and refs
    A2  review binding
    A4  onward

**One merge, measured clean.** Dry run: **no conflict**, merge-base
`de547d9d…`.

    source contributes          4 additions, 0 modifications
    this task authors           3 — spec, review, report
    cumulative at merge (3)     6 additions
    cumulative at final (4)     7 additions

**`6` is CUMULATIVE, not the merge's contribution.** **Any conflict is
an immediate STOP.** **Nothing is modified.**

---

## 0. The verdict, and the two ways it must not be compressed

    VERDICT     FORM DERIVED / SCALE FITTED

**`SRC-B0`'s two-way taxonomy could not express this.** **The four-way
taxonomy was a repair, and the repaired option is the one that
obtained.**

### 0a. Do NOT compress this to "the halo is derived"

**What is derived is the FUNCTIONAL FORM: a Yukawa Green's function of
range `r_c = 1/m_θ`, from the static field equation of a massive
scalar.**

**What is NOT derived is the SCALE.** **The chain runs**

    SPARC observation → r_c ~ 10 kpc → m_θ ~ 10⁻²⁷ eV → ε

**— observation inward, not theory outward.** **`r_c ~ 10 kpc` is not a
first-principles prediction of this framework and must not be reported
as one.**

**`r_c = 1/m_θ` is a DERIVED RELATION. It is not a derived numerical
value of `r_c`.** **Say both, in those terms.**

### 0b. Do NOT compress the Green's function to a halo profile

**Lines `:613-615` establish the MEDIATING FIELD's Green's-function
behaviour.** **Getting from there to a galaxy halo requires a source
distribution and a coupling, and neither is established.**

**Measured at the evidence base, `:641-643`:** *Establishing this
coupling chain quantitatively is deferred to future work; in
Ref.~\\cite{Cheng:2025sparc} the coupling is treated as an effective
parameter…*

**So `SRC-B0`'s "the source side is absent" and `SRC-01a`'s "the form is
derived" are COMPATIBLE, not contradictory.** **A form without a source
and a coupling is not a halo.** **Report that they are compatible and
why** — a reader meeting both verdicts on `main` will otherwise take
them for a conflict.

## 1. The finding upstream of the parameters

**The `SRC-01a` specification asked about parameter provenance.** **The
executor found the load-bearing step is EARLIER: the IDENTIFICATION
itself.**

    1  θ̃ exists                    DERIVED HERE — the only such step
    2  θ̃ ≡ χ                       an IDENTIFICATION, made because χ
                                    already accounts for the
                                    phenomenology
    3  Yukawa form, r_c = 1/m_θ     derived, but from χ's field
                                    equation
    4  m_θ ~ 10⁻²⁷ eV               inferred from SPARC

**Measured, verbatim at the evidence base:**

    :80-81   This mode is identified with the ultralight scalar
             responsible for the dark-matter phenomenology of
             Ref.~\\cite{Cheng:2025sparc}
    :616-620 We identify θ̃ with the ultralight scalar χ whose
             galactic-scale phenomenology was tested in [Paper 1]; the
             SPARC-scale cutoff radii r_c ~ 10 kpc correspond to
             m_θ ~ 10⁻²⁷ eV

**"responsible for" and "correspond to" are identification language, not
derivation language.**

> **The identification behaves, for classification purposes, as `m_θ`
> does: both are fixed by the phenomenology — but NOT in the same
> epistemic way.** **The identification is a QUALITATIVE
> phenomenological identification; `m_θ` is a QUANTITATIVE inference
> from an observed `r_c`.**

**Keep that distinction in the report.** **"Fixed by the phenomenology"
covers both; "fixed in the same way" does not.**

**And `:641-643` records the coupling as deferred**, so the
identification does not rest on an internal dynamical reason either.

**Report this as the verdict's upstream half.** **A landing that
reported only "scale fitted" would leave the impression that the
identification is secure and only a number is borrowed.**

## 2. What this decides about the source-side test

**Which field equation is used decides whether the test is circular.**

    using χ's field equation      the Yukawa form is already known;
                                  a computation returning it carries
                                  no information about the form

    using θ̃'s independently       AVOIDS THIS SPECIFIC CIRCULARITY,
    derived microscopic field     provided the derivation does not use
    equation                      the phenomenological θ̃ ≡ χ
                                  identification as an input — and it
                                  requires R1, R5 and D-pre

**THAT IS NOT THE SAME AS THE TEST BEING NON-CIRCULAR.**

**Whether the eventual source-side test is non-circular AS A WHOLE
remains unresolved**, because the source and configuration mapping, the
coupling, and the normalisation each have their own provenance and
**none has been established.** **If any of them is also fixed by the
same phenomenology, circularity re-enters by another door.**

**An earlier draft of this section wrote that the microscopic route is
"non-circular".** **`SRC-01a` established circularity for ONE layer —
the Yukawa form — and looked at no other.**

**Report this as an implication of the verdict, not as a
recommendation.** **Do not say whether the test should be done.**

## 3. What this does NOT establish

- **This reads Paper 2's account of Paper 1's work.** **Paper 1 is not
  in this repository and was not read.** **Every statement about what
  Paper 1 derived is this manuscript's claim.**
- **The verdict is about PROVENANCE, not validity.** **Nothing here
  bears on whether the halo phenomenology is correct.**
- **`SRC-B0`'s verdict stands**: no configuration usable for computation
  is in this repository. **This task supplies none.**
- **The search vocabulary was the Researcher's and is not exhaustive.**
  **A step using terms outside both passes would have been missed.**
- **Nothing here touches `R1`–`R5`, the `Γ`-versus-`S` source
  definition, `RECON-01b`, or the `r = 1` conflict.**

## 4. What this task must not do

- **Do not touch `main` until §6's landing.**
- **Do not modify any file.**
- **Do not write `r_c ~ 10 kpc` as a prediction**, and **do not write
  `r_c = 1/m_θ` as a derived value.**
- **Do not report the Green's function as a halo profile.**
- **Do not read or reason from Paper 1 directly.**
- **Do not evaluate the phenomenology's correctness.**
- **Do not say whether the source-side test should be done.**
- **Do not add a register entry anywhere.**
- **Do not push any ref but `refs/heads/main` and this task's branch.**

## 5. Acceptance criteria

**A1 — Repository and refs.** Report the `origin` remote URL as measured,
**verbatim and not normalised**; confirm it identifies
`zetacheng/2-emergent-gravity`. Fetch, then report
`refs/remotes/origin/main` **pasted from `git rev-parse` output** and
confirm it is `de547d9d6e152f6be0ef2215cb30c9c3fe3bd248`.

**Report the source tip PASTED FROM `git rev-parse` OUTPUT** and confirm
it is `6193df29eddd911c8e5829b3745fc342b5dc8065`, **and that it is not
an ancestor of `main`.**

**Every SHA in your report is pasted from command output, not
transcribed.** **This requirement stands on its own reasoning: a pasted
identifier can be checked against the ref it names; a statement that you
checked cannot.** **It does not rest on any claim about earlier
reports** — **an earlier specification in this line asserted that three
reports gave unresolvable ids, and that attribution was retracted after
the tokens were found to appear zero times in the reports concerned.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0. **Report whether the clone is shallow
and its commit count.**

**A4 — Merge parentage, three separately derived measurements**, parent
1 this task's review commit, parent 2 the source tip **as re-resolved**,
merge-base the evidence base. **Commit 1 must be an ancestor of parent
1.**

**A5 — No conflict.** Report the conflict list. **It must be empty.**

**A6 — The four-step chain, re-read at the head.** **Quote `:80-81`,
`:613-615`, `:616-620` and `:641-643` verbatim with line numbers.**
**Classify each of the four steps** as derived here, identified here, or
deferred.

**Report the direction of the scale chain explicitly** — observation to
`r_c` to `m_θ` to `ε` — **and confirm no step runs theory-outward.**

**A7 — The two compressions, both guarded.** **Confirm the report
contains no sentence calling the halo derived, and none calling
`r_c ~ 10 kpc` a prediction.** **Search for both and report the
search.**

**Report the relation-versus-value distinction in its own words**:
`r_c = 1/m_θ` derived as a relation, `r_c` not derived as a value.

**A8 — Compatibility with `SRC-B0`, stated.** **Report why "the source
side is absent" and "the form is derived" do not conflict**, with
`:641-643` quoted as the reason — **a Green's function without a source
distribution and a coupling is not a halo.**

**A9 — The identification as the upstream finding.** **Report that the
identification is fixed by the phenomenology in the same way `m_θ` is**,
and **that the coupling is deferred**, so it rests on no internal
dynamical reason. **Quote the manuscript's own wording.**

**A10 — The circularity implication**, per §2, **stated as an
implication and SCOPED TO ONE LAYER.**

**Report that the `χ` route is circular FOR TESTING THE YUKAWA FORM**,
and **that the microscopic route avoids THAT SPECIFIC circularity under
a stated condition** — that its derivation does not take the
phenomenological identification as an input.

**Confirm the report contains no sentence calling the microscopic route
non-circular without qualification.** **Search for it and report the
search.**

**Report the three provenances not yet examined**: the source and
configuration mapping, the coupling, and the normalisation. **Confirm
you did not examine them.**

**Confirm you did not say whether the test should be done.**

**A11 — Scope, frozen manifest. Cumulative final: 7 additions, 0
modifications.**

    stated: 7 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: de547d9d6e152f6be0ef2215cb30c9c3fe3bd248
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-SRC-01a_configuration-provenance.md
      reports/2026-08-18T1205Z_src-01a-configuration-provenance.md
      reports/2026-08-XXT{HHMM}Z_integrate-src-01a.md
      reviews/chatgpt/2026-08-18T1205Z_src-01a-configuration-provenance.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-src-01a.md
      specs/2026-08-18T1205Z_src-01a-configuration-provenance.md
      specs/2026-08-XXT{HHMM}Z_integrate-src-01a.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Seven paths.** **Four arrive, all additions; three authored here.**
**Report the ARRIVING PATH count and the ARRIVING ADDITION count
separately** — they coincide, at four.

**Report the cumulative figure at each commit AND the source's own
contribution, separately labelled.** **Expected cumulative 1, 2, 6, 7;
source contribution 4.**

**`append_only: DECISION_LOG.md` is a checker-configuration declaration,
NOT an authorisation to write that file.** **Measure the UTC time and use
the value you measured.**

**A12 — Which merge case.** **The merge-base is the evidence base, so no
commit on `main` could have touched an arriving path** — report that,
**then** the four blob comparisons.

**A13 — Nothing existing changed.** Every path at the evidence base
blob-identical at the head, **`paper/emergent_gr_paper_v2_15.tex` in
particular.** **Report the count compared**, and confirm for `GATES.md`,
`CONVENTIONS.md`, **every `derivations/P2-BETAV-*` and
`derivations/P2-SRC-*` artifact — re-measure both counts**, the two
`scripts/recon2026/` files and `tests/test_recon2026_flat_limit.py`,
both registers, and everything under `results/`.

**A14 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four, read SCOPED.**

**A15 — Superseded branches not merged, all six.**

    52f65117  ebd531ab  40168469  7146a093  10c260b9  d64cd912

**Six separate exit statuses**, before and after the advance.

**A16 — The checker over this task's own range**, base `de547d9d…`, head
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

**A16-final, post-report evidence:** re-run RUN 2 at commit 4, **before
the landing.**

**A17 — Validators, exit status 0.** **Expected 332 passed, 2
deselected** — the arriving task adds no code.

**A18 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 6. Commit order, evidence layering, and the landing clause

    commit 1  specs/2026-08-XXT{HHMM}Z_integrate-src-01a.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-src-01a.md
    commit 3  --no-ff merge of 6193df29…
    commit 4  reports/2026-08-XXT{HHMM}Z_integrate-src-01a.md
    then      fast-forward refs/heads/main to commit 4, and push

**Committed report — measured at commit 3:** A1–A15, A17 and A18 for
commits 1–3; **A16's two runs with both configs verbatim**; commit 1–3
SHAs **pasted from `git rev-parse`** and stored messages; commit 4's
intended message; **A11's final scope stated as INTENDED, with the
measured cumulative 6 at commit 3.**

**Post-report evidence, NOT written back:** A11's final scope measured
base-to-commit-4; A16-final; A14 and A15 re-run after the advance; A18
for commit 4; the push; remote `main` read back **from command output**;
final ancestry confirmation.

**Nothing in the committed report may claim to measure commit 4.**

**The landing.** **This task ends with authoritative `main` at its own
final report commit**, named as **commit 4**, not as a SHA. **The
advance is a fast-forward; `de547d9d…` is the base of this branch.**
**Verify `--is-ancestor` before the push and report the exit status as a
measurement.** **If a fast-forward is not available, STOP.** **Push
without `--force` and without `--force-with-lease`.** **Push only
`refs/heads/main` and this task's branch.** **The source branch is not
deleted and does not move**; verify and report its tip.

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Five junctions, all five required in the report.**

**First.** **"Form derived" is not "halo derived", and a derived
relation is not a derived value.** **Say both**, and **say that the
scale chain runs observation-inward.**

**Second.** **The identification is the upstream half of the verdict.**
**It is fixed by the phenomenology in the same way the number is**, and
**the coupling that might have grounded it internally is deferred to
future work by the manuscript's own words.** **Say that reporting only
"scale fitted" would leave the identification looking secure.**

**Third.** **This is a verdict about what Paper 2 CLAIMS about Paper 1,
not about what Paper 1 did.** **Paper 1 was not read and is not here.**
**Say that a `FORM DERIVED` finding reached this way is a finding about
a claim.**

**Fourth.** **The search vocabulary came from the Researcher and from a
description, not from the manuscript's own index.** **Two passes were
run and neither list is exhaustive.** **Say what was searched and that a
step outside it would have been missed.**

**Fifth.** **This landing removes no blocker.** **`SRC-B0`'s absent
configuration is still absent; `R1`–`R5` are still open; the
`Γ`-versus-`S` question is still unresolved.**

**What it establishes is narrower than it may read:** **ONE ROUTE is
circular FOR TESTING THE YUKAWA FORM; the microscopic route can avoid
THAT SPECIFIC circularity** — **and this task does NOT establish that
the eventual source-side test as a whole is non-circular.**

**Say that the source mapping, the coupling and the normalisation each
carry their own provenance, that none was examined, and that
circularity could re-enter through any of them.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, and its report.
  **Everything arriving by merge is integrated exactly as reviewed.**
- **Modify nothing.**
- **Do not call the halo derived, call `r_c` predicted, read Paper 1, or
  recommend the source-side test.**
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

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**, and **every SHA pasted from command
  output**;
- **A1's verbatim `origin` URL and both pasted SHAs**;
- **A3's environment diagnosis in Rule 13's order, run FIRST**;
- **A4's three values, separately derived**;
- **A6's four quoted passages, the step classification, and the scale
  chain's direction**;
- **A7's two searches and the relation-versus-value distinction**;
- **A8's compatibility statement with `:641-643` quoted**;
- **A9's identification finding with the manuscript's wording**, and the
  qualitative-versus-quantitative distinction kept;
- **A10's implication, scoped to the Yukawa-form layer**, the search
  confirming no unqualified "non-circular" claim, and the three
  provenances not examined;
- **A11's cumulative figures and the source's contribution, separately
  labelled**;
- **A12's merge case, stated BEFORE the blob comparisons**;
- **A13's path count with both artifact counts re-measured**;
- **A14's four invariants**;
- **A15's six exit statuses, before and after**;
- **A16's two runs**, both configs verbatim, the section count `P7` saw,
  what `RUN 1` did, and confirmation the output was parsed not grepped;
- **A17's counts**;
- **the landing**: the pre-advance is-ancestor exit status, the exact
  push command, remote `main` read back, the source tip unchanged, and
  confirmation that no other ref was pushed;
- **§7's five Rule 16 junctions**;
- **whether landing this made you want to call the halo derived, to say
  the test is worth doing, or to reason from Paper 1.** **Say which and
  why, and confirm you did not**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      refs and the merge
    method      git fetch; git rev-parse; dry run from de547d9d with two
                placeholder commits, then git merge --no-ff
    MEASURED    origin/main = de547d9d6e152f6be0ef2215cb30c9c3fe3bd248;
                source tip = 6193df29eddd911c8e5829b3745fc342b5dc8065,
                NOT an ancestor of main. Merge CLEAN; merge-base =
                de547d9d. SOURCE CONTRIBUTES 4 additions, 0
                modifications. CUMULATIVE: 6 at the merge commit, 7 with
                a placeholder report.

    target      the four passages
    method      read lines 78-82, 613-615, 616-622 and 641-643 of
                paper/emergent_gr_paper_v2_15.tex at the evidence base
    MEASURED    :80-81 "This mode is identified with the ultralight
                scalar responsible for the dark-matter phenomenology of
                Ref.~\\cite{Cheng:2025sparc}." :616-620 "We identify
                θ̃ with the ultralight scalar χ whose galactic-scale
                phenomenology was tested in [Paper 1]; the SPARC-scale
                cutoff radii r_c ~ 10 kpc correspond to m_θ ~ 10⁻²⁷ eV."
                :641-643 "Establishing this coupling chain
                quantitatively is deferred to future work; in
                Ref.~\\cite{Cheng:2025sparc} the coupling is treated as
                an effective parameter…"
    DERIVED     "responsible for" and "correspond to" are identification
                language. A6 requires all four re-read at the head.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 7 additions, 0 modifications;
                parse OK, counted equals stated per category.
