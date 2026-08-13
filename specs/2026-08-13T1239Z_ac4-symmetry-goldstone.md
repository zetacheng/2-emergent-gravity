# Task specification — `OPEN-AC-4`: exact and remnant symmetry, and whether `C-i` reads plainly

Specification evidence base: `1b569851a914589242024c4dde7d2eb020e3800c`

    Branch to create   science/ac4-symmetry-goldstone
    Cut from           authoritative main @ 1b569851…

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18.

**This task reads and derives. It modifies nothing that already exists**,
runs no script, computes no new numerical result, and touches no pinned
artifact.

**It does not apply standard C to anything.** It determines **how `C-i`
is to be read**. **Naming any candidate as passing or failing any
condition is forbidden by §5.**

---

> ## THE AUTHOR DERIVED A PREDICTION BEFORE WRITING THIS
>
> **Blind pre-registration is not available, and this section says so
> rather than pretending otherwise** — the same disclosure `C3` carried,
> for the same reason.
>
> **While scoping the reading list the author established what kernel the
> exploratory study used, and treated that as the regularised theory.**
> **That promotion was unfounded and the Reviewer refuted it.** The
> canonical lattice Dirac operator is NOT frozen — §0a records the lines
> — **so a fact about the exploratory kernel is not a fact about the
> frozen microscopic action, which is what standard C asks about.**
>
> **§2's prediction survives, narrowed to the kernel it was derived
> from.** **§3 now carries TWO verdicts**, because the narrow question
> and the question `OPEN-AC-4` actually asks are not the same question.
>
> **The executor derives independently first, then checks §2, then
> rules.** **Report whether the derivation was reached independently,
> reached after reading §2, or cannot be separated from it.** **All three
> are acceptable answers. Silence is not.**

## 0. The question

**The adopted admissibility contract commissions `OPEN-AC-4` as the input
to `C-iii`, and through `C-iii` it governs how `C-i` is read.**

`C-i` requires the full condensate-space Hessian to be **positive
definite on the space transverse to any flat directions required by an
exact or remnant symmetry.**

**If no exact continuous symmetry is broken by the candidate condensate,
there are no such flat directions and `C-i` reads plainly.** **If one is,
`C-i` reads transverse, and the flat directions must be identified before
any Hessian can be read at all.**

**What is already recorded, and it is thin.** The existing material
establishes that `Mhat -> -Mhat` is **not** a symmetry of the Wilson
scalar functional, and reports the complement relation. **The adopted
contract states that the symmetry interpretation is a review inference,
not a computed result.** **This task replaces the inference with a
determination.**

## 0a. The canonical lattice Dirac operator is NOT frozen

**Standard C's `C-iii` asks for the exact and remnant symmetries of the
FROZEN MICROSCOPIC ACTION.** **The repository has not frozen the operator
that would fix them**, and says so in four places:

    P2-LATTICE-ONTOLOGY-01, §189
      "Canonical kinetic operator and species accounting |
       DELEGATED: D-pre"

    P2-LATTICE-ONTOLOGY-01, §347
      "the choice among naive / Wilson / staggered / overlap kinetic
       terms is a choice of the theory's matter content"

    P2-LATTICE-ROUTE-01, §138
      "Wilson / staggered / overlap are *different microscopic models*,
       not interchangeable regulators"

    P2-LATTICE-ROUTE-01, §189 and §322
      D-pre freezes "the canonical lattice Dirac operator"; and
      P2-LATTICE-MICROSPEC-01, which is D-pre, is "not created"

**So the exploratory study's Wilson-form kernel is a property of that
calculation, not a declaration that the theory's microscopic operator is
Wilson.** **Treating the two as one would silently promote an
exploratory choice into an ontological commitment**, which
`P2-LATTICE-ONTOLOGY-01` §347 says is a choice of the theory's matter
content.

**The author made exactly that promotion in an earlier draft of this
specification**, having recorded in §11 that the two lattice documents
were unread. **The unread documents are the ones that refute it.**

**Consequence for this task, stated before the executor starts:**
**`OPEN-AC-4` as adopted probably CANNOT be closed here.** §3's second
verdict exists so that the task can say so precisely rather than deliver
a narrow answer dressed as a complete one.

## 1. What is read

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    sha256  fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a
    271 lines — §2 carries the canonical interaction verbatim

    scripts/p2_phase01_scalar_exploratory.py
    sha256  3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0
    — lines 46-90, WilsonQuadrature, for the regularisation actually used

    derivations/P2-PHASE-01_input_admissibility_contract.md
    — for standard C and OPEN-AC-4 as adopted

    derivations/P2-LATTICE-ONTOLOGY-01.md
    derivations/P2-LATTICE-ROUTE-01.md
    — for what the lattice is taken to be

**Verify both digests before reading. If either differs, STOP.**

**Read whatever else is needed. If the answer turns on a file outside
this list, say which** — `C3`'s reading list omitted three lines that
carried its answer, and the omission was found by its executor rather
than by its author.

## 2. The author's prediction, stated so it can be refuted

**Derive independently first. Then read this. Then check it.**

**(a) The frozen action's stated symmetry is a CONTINUUM statement.**
`phaseA_freeze.md` §2 gives

    L = Σ_a ψ̄_a (i γ^μ ∂_μ) ψ_a + (G/2N) Σ_A [ S^A² + P^A² ]

and records the classical symmetry as `U(N)_L × U(N)_R`, with the
anomalous `U(1)_A` breaking explicitly excluded from the canonical
interaction.

**(b) The computation does not use that regulator.** `WilsonQuadrature`
at lines 57-87 builds

    s = Σ_μ sin²(p_μ)
    w = Mhat + Σ_μ (1 - cos p_μ)
    denominator = s + w²

**That is the Wilson fermion denominator with `r = 1`.** The
Wilson term `Σ_μ (1 - cos p_μ)` sits **inside the mass slot `w`**, and at
`p_μ = π` in all four directions it equals `8` — **which is where the
complement relation `Mhat -> -8-Mhat` comes from.**

**(c) A momentum-dependent addition to the mass slot breaks chiral
symmetry explicitly.** **PREDICTION: the `U(N)_L × U(N)_R` of §2 is NOT
an exact symmetry of the regularised theory the study computes.** **The standard Wilson
operator does not satisfy the Ginsparg-Wilson relation and therefore does
not possess the corresponding exact lattice chiral symmetry at finite
lattice spacing.** An earlier draft said Wilson fermions "carry no
Ginsparg-Wilson remnant", which treats `remnant` as a universally defined
object; the relation is the precise statement.

**(d) PREDICTION, the consequence: a singlet scalar condensate breaks no
exact CONTINUOUS symmetry here.** `U(N)_V` remains exact and a singlet
condensate does not break it. **So there are no exact Goldstone
directions, and `C-i` reads plainly.**

**(e) Where the prediction could fail, named so the check is real:**

- **if the condensate is not singlet** — a non-singlet `λ^A` condensate
  would break `U(N)_V`, and that symmetry IS exact;
- **if a remnant continuous symmetry survives the Wilson term** that the
  author has not identified;
- **if the lattice's own exact symmetries** — hypercubic `H(4)`, parity,
  charge conjugation — **are broken by the candidate in a way that
  produces flat directions**, which discrete breaking normally does not
  but degenerate vacua do bear on `C-ii`.

**The author has NOT read the lattice ontology or route documents.**
**(e)'s third item is the most likely place for this prediction to be
wrong**, and it is where the executor should look hardest.

## 3. The pre-registered verdicts and their consequences

**TWO verdicts. They answer different questions and the second is the one
`OPEN-AC-4` asks.** **Fixed before the executor reads. Not renegotiated
afterwards.**

### Verdict A — the exploratory Wilson kernel, singlet scalar candidate

**Scope, and it is narrow by construction:** the kernel at lines 46-90 of
the exploratory script, and a **uniform flavour-singlet scalar**
condensate. **Nothing else.**

**`A-NO-EXACT-CONTINUOUS-BREAKING`** — under that kernel and for that
candidate class, no exact continuous symmetry is broken.

**Consequence:** **for the singlet-scalar candidate class under the
Wilson-form exploratory kernel, `C-i` would read PLAINLY** — full
positive definiteness, no transverse qualification, because the flat-
direction set is empty **for that class and that kernel**. **The
transverse clause is NOT dead text**: a non-singlet `λ^A` condensate
would break the exact `U(N)_V`, and a different kinetic operator would
change the exact symmetries entirely. **Any statement of this consequence
that omits the candidate class or the kernel is a misstatement of it.**

**`A-EXACT-BREAKING-WITH-GOLDSTONES`** — an exact continuous symmetry is
broken under that kernel and for that candidate.

**Consequence:** `C-i` would read TRANSVERSE for that class, **the flat
directions must be named and counted**, and **every existing
one-dimensional curvature result becomes uninterpretable as a stability
statement** until it is known whether the slice lies along or across
them.

**`A-DISCRETE-ONLY-BREAKING`** — only discrete symmetries are broken.

**Consequence:** `C-i` reads plainly for that class, **but degenerate
vacua exist and `C-ii`'s depth comparison must state how they are
counted.** **That is a finding for `OPEN-AC-3`, recorded and not acted
on.**

**`A-INCONCLUSIVE`** — the kernel and the freeze do not determine even
the narrow question.

### Verdict B — can `OPEN-AC-4` be closed?

**`B-CLOSABLE`** — the canonical lattice Dirac operator IS frozen and
verdict A's answer therefore transfers to the frozen microscopic action.

**Consequence:** `OPEN-AC-4` closes, `C-iii` is satisfiable by recording
the determination, and the work order moves to `OPEN-AC-3`.

**`B-NOT-CLOSABLE`** — the canonical operator is not frozen, so verdict A
holds only for the exploratory kernel.

**Consequence:** **`OPEN-AC-4` REMAINS OPEN and this task does not close
it.** **`C-iii` cannot be evaluated, and therefore standard C cannot be
completed, until `D-pre` freezes the canonical lattice Dirac operator.**
**Verdict A is recorded as a conditional result: "if the canonical
operator is Wilson-form, then …".** **State plainly that the science
line's blocker moves from `OPEN-AC-4` to `D-pre`
(`P2-LATTICE-MICROSPEC-01`, recorded as "not created")**, and **do not
recommend anything about it** — the next step is a PI decision, not this
task's.

**`B-INCONCLUSIVE`** — whether the operator is frozen cannot be
determined from the material.

**The author's expectation, stated as a prediction and not an
instruction: `A-NO-EXACT-CONTINUOUS-BREAKING` and `B-NOT-CLOSABLE`.**
**Report what you determine.**

**If the reading establishes something none of these represents, STOP and
report a `SPECIFICATION_DEFECT`.** **Do not invent a consequence.**

## 4. The findings artifact

`derivations/P2-PHASE-01_AC4_symmetry_and_goldstone.md`, containing:

1. **BOTH verdicts**, each in the first line of its own section, with
   verdict A's candidate class and kernel named in the same sentence;
2. **the symmetry inventory** — for the regularised theory actually
   computed, not the continuum Lagrangian: which continuous symmetries
   are exact, which are explicitly broken and by what term, and which
   discrete symmetries are exact;
3. **whether the scalar condensate is an order parameter for any of
   them**, stated per symmetry;
4. **the flat-direction count**, which may be zero, with its
   justification;
5. **how `C-i` would be read for the candidate class examined**,
   transcribed from §3 **verbatim**, **with the class and kernel stated
   beside it**, and **an explicit statement of what is NOT thereby
   determined for non-singlet or non-scalar candidates**;
6. **the gap between the frozen action and the regularisation**, if the
   reading confirms one — **stated plainly, because a frozen action
   whose stated symmetry does not survive its own regulator is a
   governance finding as well as a physical one**;
7. **what this does not establish**, per §7.

**Define every kind label used, and use no others.** **Four consecutive
tasks were spent repairing labels that asserted a state their document
was no longer in.**

## 5. What this task must not do

- **Do not modify any existing file.** Not the freeze, the script, the
  results, the adopted contract, or `GATES.md`.
- **Do not run the script** and do not write under `results/`.
- **Do not compute a new numerical result.** Reading a stored value is
  reading; evaluating the integrand at a new point is not.
- **Do not apply standard C to any candidate**, and **do not name any
  candidate as passing or failing `C-i`, `C-ii` or `C-iii`.**
  **Determining how a criterion reads is not applying it**, and the
  distinction is this task's boundary.
- **Do not answer `OPEN-AC-3` or `OPEN-AC-1`.** If the reading bears on
  either, one sentence each, no conclusion.
- **Do not amend the frozen action**, and do not propose an amendment.
  **If §2(a)/(b)'s gap is confirmed, report it; repairing it is a
  separate task with its own review.**
- **Do not change any gate, gate status, prerequisite state or verdict.**
- **Do not touch `main`**, do not merge.
- **Do not add an item to `derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md`
  or to any register.** **Report findings in this task's own artifact.**

## 6. Acceptance criteria

**A1 — Refs and inputs.** `refs/heads/main` resolves to
`1b569851a914589242024c4dde7d2eb020e3800c`. The freeze measures
`fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a` and
the script `3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0`,
the latter equal to the results file's `script_sha256`. **Any mismatch →
STOP.** Report all four.

**A2 — This task's pre-execution review committed, unedited**, per Rule
18, **carrying `reviewed specification SHA-256:` filled in.** **If blank
or naming a different digest, STOP and say which.** Report both digests
equal.

**A3 — The symmetry inventory**, per §4 item 2, **for the regularised
theory**. **Report it in full**, and **state for each entry the lines it
rests on.**

**A4 — §2's claims checked individually: SEVEN verdicts.** (a), (b),
(c), (d), and each of (e)'s three failure modes — **four plus three is
seven.** **Report CONFIRMED, REFUTED or CANNOT DETERMINE for each, with
the lines.** **A blanket "prediction confirmed" is not accepted.**

**(e)'s third item — the lattice's own exact symmetries — must be
answered from the lattice ontology and route documents**, which the
author did not read and which §0a shows are decisive.

**A5 — BOTH verdicts of §3**, each in the first line of its own section:
**verdict A with its candidate class and kernel named in the same
sentence**, and **verdict B**. **A verdict A stated without its scope is
a STOP**, because the scope is what distinguishes it from an answer to
`OPEN-AC-4`.

**A6 — Both consequences transcribed, not paraphrased.** Diff each
against §3's text for the selected verdict and report that they
correspond. **A rewritten consequence is a STOP.**

**A7 — The anchoring disclosure**, per the block at the head of this
specification.

**A8 — Scope. Final base-to-head scope: 4 additions and 0
modifications.** **`modify:` is `[]` and must remain so.** **A single
modification anywhere is a STOP.**

**A9 — Nothing existing changed.** Every path existing at the evidence
base is blob-identical at commit 4. **Report the count compared**, and
confirm explicitly for the freeze, the script, the results file,
`GATES.md`, and the adopted contract.

**A10 — The checker over this task's own range**, base `1b569851…`, head
**commit 3**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_ac4-symmetry-goldstone.md

**Config for both runs, stated so that you supply no value of your own:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**`append_only_paths` is NOT `[]`** — an empty set turns `P3` from
`NOT_DECLARED` into `NOT_APPLICABLE`. **`authorised_modified_gates` IS
`[]`, and here that is truthful**: no gate may change.

**`P7` will return `PASS` and it is evidence of nothing.** This task
changes no gate; **A9 is what establishes that.**

**RUN 2 is stop-governing; any failure is a STOP.** **Both configs and
both JSON outputs verbatim.** **Report the subject set RUN 1 actually
selected, as measured.**

**A10-final, post-report evidence:** re-run RUN 2 at commit 4.

**A11 — Commit-message hygiene** on all four commits. **Commits 1–3 go
in the report; commit 4 is post-report evidence.**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**First junction, offered so you can confirm or replace it.** An
`A-NO-EXACT-CONTINUOUS-BREAKING` verdict **makes `C-i` readable for the
class examined. It does not make it satisfied by anything.** **The full condensate-space Hessian
has still never been computed**, and every stability figure in the
repository remains a one-dimensional restricted curvature under a uniform
scalar ansatz at `mu = 0`.

**A reader may take "no Goldstone modes" for "the condensate is stable".**
**It is not a stability statement at all** — it is a statement about
which stability statement would be the right one to make.

**Second junction.** If §2(a)/(b)'s gap is confirmed, **the frozen
action's recorded classical symmetry does not describe the kernel the
programme has been computing with.** **A reader of `phaseA_freeze.md` §2
alone would not know that.** **Say where such a reader would meet the
correction**, and **note that this task is forbidden to create it.**

**Third junction, and it is the one this task most easily produces.** A
verdict A of `A-NO-EXACT-CONTINUOUS-BREAKING` **will read as though the
Goldstone question were settled.** **It is settled for one kernel and one
candidate class, neither of which the programme has committed to.**
**Say that beside the verdict, not below it**, and **say that
`OPEN-AC-4` closing or not is verdict B's answer, not verdict A's.**

## 8. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_ac4-symmetry-goldstone.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_ac4-symmetry-goldstone.md
    commit 3  derivations/P2-PHASE-01_AC4_symmetry_and_goldstone.md
    commit 4  reports/2026-08-XXT{HHMM}Z_ac4-symmetry-goldstone.md

    stated: 4 additions, 0 modifications
    base: 1b569851a914589242024c4dde7d2eb020e3800c
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-PHASE-01_AC4_symmetry_and_goldstone.md
      reports/2026-08-XXT{HHMM}Z_ac4-symmetry-goldstone.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_ac4-symmetry-goldstone.md
      specs/2026-08-XXT{HHMM}Z_ac4-symmetry-goldstone.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Four commits, not five** —
commit 3 is the content.

**Committed report — measured at commit 3:** A1–A9 and A11; **A10's two
runs with both configs verbatim**; commit 1–3 SHAs and stored messages;
commit 4's intended message; **the final scope stated as INTENDED.**

**Post-report evidence, NOT written back:** the final scope measured
base-to-commit-4; A10-final; A11 for commit 4; validators at commit 4;
the push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 9. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  findings artifact. **Nothing else, at all.**
- **No file existing at the evidence base may be modified**, for any
  reason, including a formatting fix.
- **Do not adjust the config to make RUN 2 pass.**
- **Do not describe `P7` as having checked gate integrity.**
- No force-push, no history rewrite, no branch deletion.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 10. Report contract

- everything in §8 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A3's inventory in full**, with lines per entry;
- **A4's SEVEN individual verdicts** — (a) through (d) and (e)'s three —
  **not an aggregate**;
- **both verdicts, with verdict A's candidate class and kernel stated in
  the same sentence**, and confirmation both consequences were
  transcribed;
- **whether `OPEN-AC-4` closes**, and if not, **that the blocker moves
  to `D-pre`** — stated, not recommended;
- **the flat-direction count and its justification**, even when zero;
- **whether the frozen action's symmetry statement survives its own
  regulator**, and if not, where a reader would meet the correction;
- **A7's anchoring disclosure**;
- **A9's path count**;
- **A10's two runs**, both configs verbatim, the measured RUN 1 subject
  set, and the `P7` statement;
- **whether answering `OPEN-AC-4` made you want to apply standard C to a
  candidate.** **Say so, and confirm you did not**;
- **§7's Rule 16 assessment**, **all three junctions**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 11. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**
**Every line was produced by running the stated method in a clean
clone.** **No measurement was taken through a truncated view.**

    target      the evidence base
    method      git fetch; git rev-parse origin/main
    MEASURED    1b569851a914589242024c4dde7d2eb020e3800c, the head
                landed by the science-line integration

    target      the frozen action's stated symmetry
    method      read derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
                §2 at 1b569851, lines 12-59
    MEASURED    the canonical interaction is the U(N) chiral NJL
                generator-sum form; the recorded classical symmetry is
                U(N)_L × U(N)_R; the anomalous U(1)_A breaking is
                explicitly excluded from the canonical interaction.
                The statement is made for the continuum Lagrangian.
                File sha256 fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a,
                271 lines.

    target      the regularisation actually computed
    method      read WilsonQuadrature at lines 46-90 of the exploratory
                script at 1b569851
    MEASURED    s = Σ sin²(p_μ) over four axes; w = Mhat + Σ(1-cos p_μ)
                over four axes; denominator = s + w². The Wilson term
                enters the MASS SLOT. At p_μ = π in all four directions
                Σ(1-cos) = 8, which is the origin of the complement
                relation Mhat -> -8-Mhat.
    DERIVED     this is the Wilson fermion denominator with r = 1. The
                identification is the author's and is §2's prediction,
                not a measurement.

    target      OPEN-AC-4 as adopted
    method      read derivations/P2-PHASE-01_input_admissibility_contract.md
                at 1b569851
    MEASURED    OPEN-AC-4 is STILL OPEN, is the input to C-iii, and
                through C-iii governs how C-i is read. The existing
                material establishes only that Mhat -> -Mhat is not a
                symmetry, and the symmetry interpretation is recorded
                as a review inference rather than a computed result.

    target      what the author did NOT read
    method      —
    NOT READ    derivations/P2-LATTICE-ONTOLOGY-01.md and
                derivations/P2-LATTICE-ROUTE-01.md. §2(e)'s third
                failure mode — the lattice's own exact symmetries —
                therefore rests on nothing the author has checked, and
                A4 requires it answered from those documents.

    target      pins at the evidence base
    method      grep 'sha256 `[0-9a-f]{64}`' over GATES.md
    MEASURED    TWO pins, both matching their targets. This task
                modifies no file named by either, so no re-pin is
                required and none is authorised.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from blob 1922fe88… and
                executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 0 modifications;
                the manifest lists four paths and 'modify: []'
                contributes none; parse OK, counted equals stated.
