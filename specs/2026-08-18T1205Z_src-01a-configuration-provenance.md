# Task specification — `SRC-01a`: is the halo configuration derived, fitted, or both?

Specification evidence base: `de547d9d6e152f6be0ef2215cb30c9c3fe3bd248`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/src-01a-configuration-provenance
    Cut from           authoritative main — refs/remotes/origin/main

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This task does not touch `main`.** Integration is a separate task.

**NORMATIVE EXECUTION ORDER, stated once:**

    A3  environment conformance
    A1  repository identity, refs, branch availability
    A2  review binding
    A4  onward

**IT COMPUTES NOTHING AND IMPORTS NOTHING.** It reads a manuscript
already in this repository and determines what can and cannot be
established from it.

---

## 0. What changed since `SRC-B0`

**`SRC-B0` returned `NOT PRESENT / EXTERNAL STATUS NOT DETERMINED` and
was FORBIDDEN from characterising any external profile.** That
prohibition was correct for that task: it was scoped to repository
materials and told not to reason about a manuscript nobody in this line
had read.

**But a manuscript IS in this repository.**
**`paper/emergent_gr_paper_v2_15.tex`, 1834 lines, present at the
evidence base.** **`SRC-B0`'s own search found `sparc` and `halo` hits
there and correctly classified them as not a usable CONFIGURATION** —
which is a different question from whether they settle PROVENANCE.

**This task reads it.**

**It does not change `SRC-B0`'s verdict.** **A configuration usable for
computation is still absent; nothing here supplies one.**

## 1. The question, and it is not binary

> **Is the halo profile DERIVED from the framework's field equations, or
> FITTED to rotation curves?**

**And the question has a hidden first step.** **The manuscript's halo
argument runs through an IDENTIFICATION** — a mode of the framework is
identified with the ultralight scalar whose galactic phenomenology
Paper 1 tested. **The mass `m_θ` appears in an identification chain, not
only in a fitted formula.**

**So the verdict may turn on whether that IDENTIFICATION is derived,
postulated, or itself fixed by the phenomenology it is meant to
explain.** **`A6` and `A7` must treat the identification as a
load-bearing step and classify it, not step over it to the parameter
values.**

**The Researcher read two passages and they point different ways.**
**Both are quoted here so the executor knows what to examine, and both
must be re-read at the head rather than taken from this specification.**

    :613-615  the static field equation of θ̃ is that of a massive
              scalar, with Yukawa Green's function of range r_c = 1/m_θ
    :618-620  the SPARC-scale cutoff radii r_c ~ 10 kpc correspond to
              m_θ ~ 10⁻²⁷ eV

**Read together, these suggest the FUNCTIONAL FORM is derived while the
SCALE is set from observation.** **That is neither `DERIVED` nor
`FITTED` as `SRC-B0`'s taxonomy had them**, and **if it is what the
manuscript says, the taxonomy is the thing that needs correcting.**

**Do not adopt the Researcher's reading.** **Two passages are not a
manuscript**, and this specification's author read fourteen matching
lines out of twenty-five. **Read all of them, and the surrounding
argument.**

## 2. The four pre-registered verdicts

    DERIVED
        the identification AND the profile's functional form AND its
        parameters follow from the framework. Name what fixes each.

    FITTED
        the profile was chosen to match rotation curves. Name what was
        fitted to what.

    FORM DERIVED / SCALE FITTED
        the functional form follows from the field equations while one
        or more parameters are set from observation. NAME WHICH
        PARAMETERS ARE WHICH.

    NOT DETERMINABLE FROM THIS MANUSCRIPT
        the text does not settle it. Name what would.

**The third is available because the Researcher's reading suggests it.**
**Its availability is not evidence for it**, and **a verdict of
`DERIVED`, `FITTED` or `NOT DETERMINABLE` is equally legitimate.**

**`NOT DETERMINABLE FROM THIS MANUSCRIPT` is a real outcome**: the
manuscript is Paper 2 and repeatedly cites Paper 1 for the halo work.
**A citation is not a derivation**, and if the load-bearing steps live
in the cited paper, this manuscript cannot settle them.

## 3. Why the answer decides whether the source-side test is worth doing

**If the profile is FITTED**, then computing its `T_μν`, deriving a
potential and finding it matches rotation curves **is circular** — the
profile was chosen to match them.

**If the FORM is derived and only the SCALE is fitted**, the test is
partially informative: **the shape prediction is testable; the
normalisation is not.** **Report what would remain testable under that
verdict** — that is the useful part of the finding, and it is not
obvious in advance.

**If it is DERIVED**, the test is fully informative and the remaining
prerequisites are the ones `SRC-B0` named.

**Do not judge whether the test is worth doing.** **Report what each
verdict would imply and stop.**

## 4. What this task must not do

- **Do not touch `main`**, do not merge.
- **Do not import anything from outside this repository**, and **do not
  read, cite, or reason from Paper 1 itself.** **It is not here.**
  **Reason from what this manuscript says about it, and mark every such
  statement as the manuscript's claim rather than a verified fact.**
- **Do not compute any `T_μν`, potential, profile value, or fit.**
- **Do not evaluate whether the halo phenomenology is correct.** **The
  question is provenance, not validity.**
- **Do not revise `SRC-B0`'s verdict.** **A usable configuration is
  still absent.**
- **Do not choose a tolerance or a failure criterion.**
- **Do not settle the `Γ`-versus-`S` source definition**, and do not
  touch `R1`–`R5`, `RECON-01b`, or the `r = 1` conflict.
- **Do not add a register entry anywhere.**
- **Do not push any ref but this task's branch.**

## 5. Acceptance criteria

**A1 — Repository, refs, branch availability.** Report the `origin`
remote URL as measured, **verbatim and not normalised**; confirm it
identifies `zetacheng/2-emergent-gravity`. Fetch, then report
`refs/remotes/origin/main` **as resolved by `git rev-parse` and pasted
verbatim from that command's output**, and confirm it is
`de547d9d6e152f6be0ef2215cb30c9c3fe3bd248`.

**Report whether `science/src-01a-configuration-provenance` already
exists.** **If it does, STOP.**

**EVERY SHA IN YOUR REPORT MUST BE PASTED FROM `git rev-parse` OUTPUT AT
REPORTING TIME.**

**Earlier specifications in this line recorded several allegedly
misreported commit ids.** **The latest landed integration could not
reproduce that attribution**, and **the Researcher has since confirmed
the same: the named tokens appear ZERO times in the committed reports
they were attributed to.**

**What is established is that the tokens do not resolve as Git
objects.** **What was ASSERTED — that those reports gave them as their
commit ids — has no support in the committed bytes.** **The tokens
reached the Researcher through conversation, not through the
repository.**

**THIS TASK DOES NOT RELY ON THAT HISTORY.** **The requirement below
stands on its own merits and not on a disputed precedent.**

**Paste the command output rather than reporting that you re-resolved.**
**A pasted identifier can be checked against the ref it names; a
statement that you checked cannot.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0. **Report whether the clone is shallow
and its commit count.**

**A4 — The manuscript inventory, in TWO PASSES.**

**PASS 1, the seed terms**: `sparc`, `halo`, `rotation curve`, `r_c`,
`fit`, `derive`, `profile`, `Yukawa`, and the LaTeX forms of the
scalar's mass — **note that `m_theta` returns ZERO because the
manuscript writes `m_\theta`.**

**PASS 2, the identification terms, which the seed list misses**:
`chi`, `\theta`, `\tilde\theta`, `ultralight`, `scalar sector`,
`dark matter`, `Green`, `cutoff`, `identif`.

**Measured by the Researcher: PASS 2 finds 136 LINES THAT PASS 1 DOES
NOT.** Among them `:80`, *This mode is identified with the ultralight
scalar responsible for…* — **the carrier identification itself, which
the seed list does not reach.**

**`chi` returns 72 hits, many of them LaTeX macro noise.** **Report hit
counts and then report which hits are SUBSTANTIVE**, distinguishing them
from markup.

**Report both passes' counts, the union, and the lines found only by
PASS 2.** **An inventory built on PASS 1 alone would have missed the
carrier and the identification chain**, and **a provenance verdict
reached from it would be a verdict about a subset of the argument.**

**Neither list is exhaustive.** **If you meet vocabulary outside both,
add it, report that you added it, and say why.**

**A5 — The two passages re-read**, `:606-625` and `:200-215` at minimum,
**quoted verbatim with line numbers**, **and the surrounding argument
summarised.** **Report whether the Researcher's reading survives.**

**A6 — What the manuscript claims versus what it establishes.** For each
load-bearing statement about the halo, report:

    CLAIMED HERE AND DERIVED HERE      the manuscript performs the step
    CLAIMED HERE, CITED TO PAPER 1     the manuscript asserts it and
                                       points elsewhere
    NOT ADDRESSED

**Report the count in each category.** **This distinction is the whole
task**: a manuscript that says *we derived* is making a claim about
another paper, **and this line has spent the session establishing that a
claim is not a measurement.**

**A7 — Parameter-by-parameter provenance, AND the identification
first.**

**Before the parameters, report the IDENTIFICATION**: which mode of the
framework is identified with which phenomenological scalar, **where the
manuscript does it, and on what basis** — derived, postulated, or fixed
by the phenomenology. **Classify it under `A6`'s three categories too.**

**Then, for each parameter of the profile** — at least `m_θ`, `r_c`, and
any coupling or amplitude — **report what the manuscript says fixes
it**: a field equation, a symmetry, a matching condition, an
observational input, or nothing.

**`r_c = 1/m_θ` is a relation, not a determination.** **Report what
determines `m_θ` itself**, and **if the answer is that `r_c ~ 10 kpc` is
taken from SPARC and `m_θ` inferred from it, say so plainly.**

**A8 — The verdict**, one of §2's four, **with the evidence.** **If
`FORM DERIVED / SCALE FITTED`, name which parameters fall on each
side.**

**A9 — What would remain testable**, per §3, **under the verdict you
reach.** **Report it as an implication, not a recommendation.** **Do not
say whether the source-side test should be done.**

**A10 — Nothing imported, nothing computed.** **Search the artifact, the
report and the commit messages for any numerical value not quoted from
the manuscript, any statement sourced to Paper 1 directly rather than to
this manuscript's description of it, and any computed quantity.**
**Report the search and the result.**

**A11 — Scope, frozen manifest.**

    stated: 4 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: de547d9d6e152f6be0ef2215cb30c9c3fe3bd248
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-SRC-01a_configuration-provenance.md
      reports/2026-08-XXT{HHMM}Z_src-01a-configuration-provenance.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_src-01a-configuration-provenance.md
      specs/2026-08-XXT{HHMM}Z_src-01a-configuration-provenance.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths.** **Report the cumulative figure at each commit and the
contributions separately.** **`append_only: DECISION_LOG.md` is a
checker-configuration declaration, NOT an authorisation to write that
file.** **Measure the UTC time and use the value you measured.**

**A12 — Nothing existing changed.** Every path at the evidence base
blob-identical at the head, **`paper/emergent_gr_paper_v2_15.tex` in
particular.** **Report the count compared**, and confirm for `GATES.md`,
`CONVENTIONS.md`, **every `derivations/P2-BETAV-*` and
`derivations/P2-SRC-*` artifact — re-measure both counts**, the two
`scripts/recon2026/` files and `tests/test_recon2026_flat_limit.py`,
both registers, and everything under `results/`.

**A13 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four, read SCOPED.**

**A14 — The checker over this task's own range**, base `de547d9d…`, head
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

**A14-final, post-report evidence:** re-run RUN 2 at commit 4.

**A15 — Validators, exit status 0.** **Expected 332 passed, 2
deselected.**

**A16 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 6. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_src-01a-configuration-provenance.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_src-01a-configuration-provenance.md
    commit 3  derivations/P2-SRC-01a_configuration-provenance.md
    commit 4  reports/2026-08-XXT{HHMM}Z_src-01a-configuration-provenance.md

**Committed report — measured at commit 3:** A1–A13, A15 and A16;
**A14's two runs with both configs verbatim**; commit 1–3 SHAs **pasted
from `git rev-parse`** and stored messages; commit 4's intended message;
**A11's final scope stated as INTENDED.**

**Post-report evidence, NOT written back:** A11's final scope measured
base-to-commit-4; A14-final; A15 at commit 4; A16 for commit 4; the
push; the branch tip read back **from `git rev-parse` output**.

**Nothing in the committed report may claim to measure commit 4.**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Five junctions, all five required in the report.**

**First.** **This reads Paper 2's description of Paper 1's work.** **It
does not read Paper 1.** **Every statement about what Paper 1 derived is
this manuscript's claim**, and **nothing here verifies it.** **Say
that**, and **say that a `DERIVED` verdict reached this way is a verdict
about what is CLAIMED, not about what was done.**

**Second.** **A provenance verdict supplies no configuration.**
**`SRC-B0`'s finding stands: nothing usable for computation is in this
repository.** **Say that this task moves the question, not the
blocker.**

**Third.** **If the verdict is `FORM DERIVED / SCALE FITTED`,
`SRC-B0`'s two-way taxonomy was wrong and this specification's four-way
one is a repair.** **Say whether the taxonomy needed repairing**, and
**say that a taxonomy which cannot express the answer is a defect in the
question, not in the material.**

**Fourth.** **The search terms are the Researcher's and came from a
description, not from the manuscript.** **A configuration or a
derivation using vocabulary outside them would be missed.** **Report
what you searched and say the list is not exhaustive.**

**Fifth.** **This specification's own earlier draft asserted that three
execution reports gave unresolvable commit ids, and labelled it
`MEASURED`.** **The tokens do not resolve — that part was measured.**
**That the reports gave them was not**, and a search finds them zero
times in those reports.

**Say that the paste requirement in `A1` rests on its own reasoning and
not on that attribution.** **And say what the episode shows: a
measurement of one proposition was carried into an assertion about a
different one**, which is the failure this line has recorded under
several names.

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  provenance artifact. **Nothing else, at all.**
- **No file existing at the evidence base may be modified.**
- **Import nothing, compute nothing, evaluate no phenomenology.**
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
  labelled MEASURED or INTENDED**, and **every SHA pasted from
  `git rev-parse`**;
- **A1's verbatim `origin` URL and the pasted `main` SHA**;
- **A3's environment diagnosis in Rule 13's order, run FIRST**;
- **A4's TWO-PASS inventory**: both term sets' counts, the union, the
  lines found only by PASS 2, and which `chi` hits are substantive
  rather than markup;
- **A5's two passages verbatim and whether the Researcher's reading
  survives**;
- **A6's three-category classification with counts**;
- **A7's identification finding FIRST, classified under `A6`'s
  categories**, then the parameter-by-parameter provenance with what
  determines `m_θ` stated plainly;
- **A8's verdict with its evidence, and the parameter split if the third
  verdict**;
- **A9's implication, stated as an implication**;
- **A10's search and result**;
- **A11's cumulative figures and contributions, separately labelled**;
- **A12's path count with both artifact counts re-measured**;
- **A13's four invariants**;
- **A14's two runs**, both configs verbatim, the section count `P7` saw,
  what `RUN 1` did, and confirmation the output was parsed not grepped;
- **A15's counts**;
- **§7's five Rule 16 junctions**;
- **whether reading the manuscript made you want to evaluate the
  phenomenology, reason from Paper 1 directly, or say whether the
  source-side test is worth doing.** **Say which and why, and confirm
  you did not**;
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
    MEASURED    de547d9d6e152f6be0ef2215cb30c9c3fe3bd248, the head
                landed by the SRC-B0 integration.

    target      whether a manuscript is in this repository
    method      git ls-tree over paper/ at the evidence base
    MEASURED    paper/README.md, paper/emergent_gr_paper_v2_15.tex
                (1834 lines), paper/figures/.gitkeep. The manuscript is
                present. SRC-B0 correctly found it carried no usable
                configuration; it was not asked whether it settles
                provenance.

    target      whether A4's seed term list is sufficient
    method      run both term sets over the manuscript and count lines
                matched by the second but not the first
    MEASURED    136 lines are found ONLY by the wider set. m_theta
                returns ZERO on the seed list because the manuscript
                writes m_\theta; rotation curve returns zero. Line 80,
                "This mode is identified with the ultralight scalar
                responsible for", is reached only by the wider set and
                is the carrier identification.
    CONSEQUENCE A4 is now two passes. An inventory on the seed list
                alone would have supported a provenance verdict about a
                subset of the argument.

    target      the two passages
    method      read lines 204-212 and 612-622 of the manuscript
    MEASURED    :206-208 "In Ref.~\cite{Cheng:2025sparc}, we derived a
                Yukawa-type dark matter halo profile from the scalar
                sector of the same lattice fermion framework and tested
                it against 175 SPARC galaxies." :613-615 "The static
                field equation of θ̃ is that of a massive scalar, with
                Yukawa Green's function of range r_c = 1/m_θ."
                :618-620 "the SPARC-scale cutoff radii r_c ~ 10 kpc
                correspond to m_θ ~ 10⁻²⁷ eV".
    DERIVED     the author's reading is that the functional form is
                derived while the scale is set from observation. §1
                states it as a reading to be tested, not adopted. The
                author read 14 of 25 matching lines on a narrow term
                set; A4 requires a wider search and the full inventory.

    target      the historical SHA-attribution claim
    method      git cat-file -t on each token; then grep each token in
                the committed report it was attributed to
    MEASURED    the named tokens do not resolve as Git objects. THEY
                ALSO APPEAR ZERO TIMES in the reports in question —
                55c2e4a4 zero times in the DET-01 integration report,
                8f5e3c4c zero times in the SRC-B0 report, d3f1173a zero
                times across reports/.
    RETRACTED   an earlier draft of this record stated as MEASURED that
                three execution reports gave those ids. Non-resolution
                as a Git object was measured; the attribution to those
                reports was not, and the committed bytes do not support
                it. The tokens reached the author through conversation.
                The latest landed integration reached the same
                conclusion independently. A1 no longer rests on this
                history.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 0 modifications;
                parse OK, counted equals stated per category.
