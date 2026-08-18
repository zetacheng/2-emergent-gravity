# Task specification — `CHANNEL-B0`: which channel is gravity, and which is a fifth force?

Specification evidence base: `af145d5a3e36e6bca62f038092748ada3abdcec1`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/channel-b0-spin-scope
    Cut from           authoritative main — refs/remotes/origin/main

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This task does not touch `main`.** Integration is a separate task.

**NORMATIVE EXECUTION ORDER, stated once:**

    A3  environment conformance
    A1  repository identity, refs, branch availability
    A2  review binding
    A4  onward

**IT COMPUTES NOTHING AND DERIVES NOTHING.** It reads what the
repository says about two mediation channels and reports where they are
separated and where they are not.

---

## 0. The question, and why it is worth one task

**This programme carries TWO collective channels of the same fermion
condensate:**

    Z     the induced transverse-traceless (TT) graviton kinetic
          coefficient — CONVENTIONS.md:20, a SPIN-2 object
    θ̃     the pseudo-Goldstone angular mode whose Yukawa exchange is
          the halo mechanism — a SPIN-0 object

**Same origin. Different spin. Therefore different coupling structure,
and possibly different force.**

**A spin-2 mediator coupling universally to `T_μν` is gravity.** **A
spin-0 mediator coupling to a scalar charge is a SCALAR-MEDIATED
ADDITIONAL FORCE.**

**Whether that scalar force is universal, or violates the equivalence
principle, DEPENDS ON ITS CHARGE AND COUPLING STRUCTURE and must be
established separately.** **Spin alone does not settle it** — a scalar
can couple universally, and a scalar-tensor theory's extra degree of
freedom is part of the gravitational sector rather than a separate
force.

> **Which is which in this programme, and does the repository keep them
> apart?**

**This is not idle taxonomy** — but the taxonomy this task can settle is
narrower than *dark matter versus modified gravity*.

**Mediator spin does NOT by itself decide that ontology.** A universally
coupled scalar in the gravitational sector is scalar-tensor MODIFIED
GRAVITY; a spin-2 excitation's role depends on what it does in the
theory.

**What this task can reliably establish is:**

    the spin-2 TT channel versus the spin-0 angular channel
    each one's STATED source, coupling, and universality status

**If the manuscript itself calls the scalar-mediated halo a dark-matter
mechanism, report that as THE MANUSCRIPT'S CLASSIFICATION.** **Do not
derive the label from the mediator's spin.**

## 1. What the Researcher measured, and why it complicates the question

**The repository DOES discuss universality — the question is not whether
it is mentioned but which channel the discussion covers.**

    :816   \subsection{Emergent gauge redundancy and universal coupling}
    :832   the equivalence principle is an emergent consequence of the …

**And separately, on `θ̃`'s coupling:**

    :637-640  A pure Goldstone couples derivatively; a monopole coupling
              must be induced by the explicit breaking and/or by mixing
              with the heavy radial mode, and is therefore suppressed by
              powers of ε and the mixing angle.

**A coupling suppressed by `ε` and a mixing angle is NOT thereby
universal OR non-universal.**

**Suppression concerns its MAGNITUDE. Universality concerns whether the
scalar charge or coupling is the same, in the relevant sense, across
matter species or test bodies.** **A coupling `g_eff ~ ε·α` with `α`
common to all matter is WEAK AND UNIVERSAL.**

**An earlier draft of this section inferred non-universality from
suppression.** **That inference does not hold**, and it would have
handed `A6` its answer before the executor read anything.

**The passage alone settles universality only if it states how the
mixing or the scalar charge depends on the object.** **`A6` must
determine whether it does.**

**So the repository asserts emergent universality in one place and
describes a suppressed coupling in another.** **Whether those are about
the same channel, and whether they conflict at all, is what this task
determines** — **and they may not conflict even if both are about the
same channel.**

## 2. The four questions

**One: what does `Z` couple to?** **Report what the repository says the
TT channel's source is.** **If it says `T_μν`, report where. If it says
nothing, report that.** **`CONVENTIONS.md:20` defines `Z` as a kinetic
coefficient — a kinetic term is not a coupling**, so do not read one
from the other.

**Two: what does `θ̃` couple to, and is it universal?** **Report the
coupling as the manuscript states it**, including `:637-640`'s
suppression. **State plainly whether the coupling is universal,
non-universal, or unstated.**

**Three: does the repository anywhere treat the two as the same force?**
**Search for places where a halo, an attraction, or a gravitational
effect is attributed without naming the channel.** **Report each, with
lines.** **An unnamed channel is not an error; it is an ambiguity, and
counting them is the point.**

**Four: what does `:816`–`:832`'s universality claim cover?** **Report
which channel it is about, on what basis, and whether the section states
its own scope.** **If it does not, report that the scope is unstated
rather than inferring it.**

**Report whether the equivalence principle is CLAIMED, DERIVED, or
TESTED in this repository** — three different things, and **`:832` uses
the word "consequence", which is a claim of derivation.** **Report
whether the derivation is present here or cited elsewhere.**

## 3. The pre-registered verdicts

    CHANNELS SEPARATED
        the repository distinguishes spin-2 from spin-0 mediation, and
        the universality claim is scoped to one of them. Name which.

    CHANNELS CONFLATED
        the repository attributes one channel's property to the other,
        or treats the two as one force. NAME THE INSTANCES with lines.

    SEPARATION NOT STATED
        the two are discussed without their distinction being addressed
        either way. This is neither separation nor conflation.

**`SEPARATION NOT STATED` is the outcome the Researcher expects and is
therefore the one to be most careful about** — **measured: `spin-2`
appears in 1 file, `spin-0` in 0, `fifth force` in 0.** **An absence of
vocabulary is not a finding about the physics**, and a verdict of
`SEPARATION NOT STATED` must rest on reading the argument, not on
counting words.

**If the repository separates the channels using different vocabulary
than this specification uses, that is `CHANNELS SEPARATED` and the
specification's word list was wrong.**

## 4. What this task must not do

- **Do not touch `main`**, do not merge.
- **DO NOT DERIVE ANYTHING.** **Do not determine what `θ̃` SHOULD couple
  to, what `Z`'s source SHOULD be, or whether the equivalence principle
  HOLDS.** **Report what the repository says.**
- **Do not compute any coupling, suppression factor, or mixing angle.**
- **Do not judge whether a fifth force is a problem.** **A
  non-universal scalar force is a legitimate dark-matter mechanism**,
  and this task takes no position on whether it is the right one.
- **Do not read or reason from Paper 1, Paper 4, or Paper 5.** **They
  are not here.**
- **Do not adjudicate `R1`–`R5`, `ε`, or the monopole coupling's
  origin.**
- **Do not recommend a next task or compare routes.**
- **Do not modify any existing file.**
- **Do not add a register entry anywhere.**
- **Do not push any ref but this task's branch.**

## 5. Acceptance criteria

**A1 — Repository, refs, branch availability.** Report the `origin`
remote URL as measured, **verbatim and not normalised**; confirm it
identifies `zetacheng/2-emergent-gravity`. Fetch, then report
`refs/remotes/origin/main` **pasted from `git rev-parse` output** and
confirm it is `af145d5a3e36e6bca62f038092748ada3abdcec1`.

**Report whether `science/channel-b0-spin-scope` already exists.** **If
it does, STOP.**

**Every SHA in your report is pasted from command output, not
transcribed.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0. **Report whether the clone is shallow
and its commit count.**

**A4 — The inventory, in two passes.**

**PASS 1**: `transverse-traceless`, `TT`, `spin-2`, `spin-0`,
`graviton`, `equivalence principle`, `universal`, `fifth force`,
`Yukawa`, `monopole`, `derivative coupling`.

**PASS 2**, terms that may carry the same content otherwise: `tensor`,
`scalar mode`, `angular mode`, `mixing angle`, `composition`, `Eötvös`,
`test body`, `geodesic`, `source`, `charge`, `gauge redundancy`.

**Report each term's file and line counts, the union, and the lines PASS
2 finds that PASS 1 does not.** **Neither list is exhaustive; if you
meet vocabulary outside both, add it and say why.**

**Measured by the Researcher over `derivations/` and `paper/`: `spin-2`
1 file, `spin-0` 0, `fifth force` 0, `transverse-traceless` 2,
`equivalence principle` 1, `universal coupl` 1.** **These are
observations to reproduce, not evidence.**

**A5 — `Z`'s coupling**, per question one. **Report what the repository
says the TT channel's source is, with lines, or that it says nothing.**
**Confirm you did not infer a coupling from a kinetic coefficient.**

### 1a. The `ε` rider — coupling STRENGTH is not frozen

**A parallel task, `EPS-B0`, has completed on branch
`science/eps-b0-scope @ efb8d63f…`.** **IT IS NOT LANDED** — it is not
an ancestor of `main` and its artifact is ABSENT from this evidence
base. **You cannot verify it and you are not asked to.**

**Its verdict, stated here as a CONSTRAINT ON YOUR REPORTING and not as
a fact you may cite:** `ε`'s computation is `BLOCKED PENDING A RULING`
with `R1 DEPENDENCE ESTABLISHED`, and `ε`'s own normalisation is not
numerically closed.

**What follows for this task:**

**If the manuscript states that the angular or scalar coupling is
suppressed by, or proportional to, `ε`, you MAY classify the stated
coupling STRUCTURE and you MAY separately assess UNIVERSALITY.**

**You MUST NOT treat that coupling's microscopic MAGNITUDE as frozen,
derived, or independently determined.**

**Three separable properties, and this task can reach only the first
two:**

    universality   assessable from the manuscript's own statements
    strength       ε-dependent, and ε is not closed
    numerical value  not available at all

**This does NOT block `A6`.** **`ε` being open makes the magnitude
unavailable; it says nothing about whether the coupling is universal.**
**Answer the universality question on its own evidence.**

**And note the general form, because it may recur:**

> **Channel separation does not establish parameter independence.**

**Two channels can be conceptually distinct while one channel's strength
depends on unresolved microscopic data through a shared parameter.**
**If your verdict is `CHANNELS SEPARATED`, say this explicitly** — `A9`
requires it.

**A6 — `θ̃`'s coupling**, per question two. **Quote `:633-640` with line
numbers.**

**Report the suppression the manuscript gives**, and **SEPARATELY**
state whether the coupling is `UNIVERSAL`, `NON-UNIVERSAL`, or
`UNSTATED`.

**These are two different findings and the first does not imply the
second.** **Report `NON-UNIVERSAL` only if the manuscript states that
the mixing or the scalar charge depends on the object** — a composition
dependence, a species dependence, a body-dependent charge-to-mass ratio.
**Absent such a statement, the answer is `UNSTATED`.**

**A7 — The conflation search**, per question three. **Report every place
a halo, an attraction, or a gravitational effect is attributed without
naming the channel.** **Report the count and the lines.** **Zero is an
acceptable answer.**

**A8 — The universality claim's scope**, per question four. **Quote
`:816` and `:832` and their surrounding argument.** **Report which
channel the claim covers and on what basis**, or **that the scope is
unstated.**

**Report separately whether the equivalence principle is CLAIMED,
DERIVED HERE, DERIVED ELSEWHERE AND CITED, or TESTED.** **These are four
states and the report must pick one, with evidence.**

**A9 — The verdict**, one of §3's three, **with the evidence.** **If
`SEPARATION NOT STATED`, confirm the verdict rests on reading the
argument and not on the absence of the specification's vocabulary.**

**IF THE VERDICT IS `CHANNELS SEPARATED`, add §1a's statement
verbatim:**

> **Channel separation does not establish parameter independence.** The
> spin-0 and spin-2 observables may be conceptually distinct while the
> scalar channel's strength remains dependent on unresolved microscopic
> data through `ε`.

**Confirm you did not report any coupling magnitude as frozen or
derived**, and **confirm you did not cite `EPS-B0` as evidence** — it is
not on your evidence base. **Report §1a as a constraint you were given,
not as a finding you verified.**

**A10 — Nothing derived.** **Search the artifact, the report and the
commit messages for any statement about what a channel SHOULD couple to,
any computed suppression or mixing factor, and any judgement about
whether the equivalence principle holds.** **Report the search and the
result.**

**A11 — Scope, frozen manifest.**

    stated: 4 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: af145d5a3e36e6bca62f038092748ada3abdcec1
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-CHANNEL-B0_spin-channel-scope.md
      reports/2026-08-XXT{HHMM}Z_channel-b0-spin-scope.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_channel-b0-spin-scope.md
      specs/2026-08-XXT{HHMM}Z_channel-b0-spin-scope.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths.** **Report the cumulative figure at each commit and the
contributions separately.** **`append_only: DECISION_LOG.md` is a
checker-configuration declaration, NOT an authorisation to write that
file.** **Measure the UTC time and use the value you measured.**

**NOTE: `EPS-B0` may be executing against the same base.** **If
`refs/remotes/origin/main` has advanced when you fetch, STOP and report
— do not rebase.**

**A12 — Nothing existing changed.** Every path at the evidence base
blob-identical at the head, **`paper/emergent_gr_paper_v2_15.tex` in
particular — report its blob id at both ends.** **Report the count
compared**, and confirm for `GATES.md`, `CONVENTIONS.md`, **every
`derivations/P2-*` artifact — re-measure the count**, the two
`scripts/recon2026/` files and `tests/test_recon2026_flat_limit.py`,
both registers, and everything under `results/`.

**A13 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four, read SCOPED.**

**A14 — The checker over this task's own range**, base `af145d5a…`, head
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

    commit 1  specs/2026-08-XXT{HHMM}Z_channel-b0-spin-scope.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_channel-b0-spin-scope.md
    commit 3  derivations/P2-CHANNEL-B0_spin-channel-scope.md
    commit 4  reports/2026-08-XXT{HHMM}Z_channel-b0-spin-scope.md

**Committed report — measured at commit 3:** A1–A13, A15 and A16;
**A14's two runs with both configs verbatim**; commit 1–3 SHAs **pasted
from `git rev-parse`** and stored messages; commit 4's intended message;
**A11's final scope stated as INTENDED.**

**Post-report evidence, NOT written back:** A11's final scope measured
base-to-commit-4; A14-final; A15 at commit 4; A16 for commit 4; the
push; the branch tip read back from command output.

**Nothing in the committed report may claim to measure commit 4.**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Five junctions, all five required in the report.**

**First.** **This reports what the repository SAYS about two channels.**
**It does not establish which channel is physically responsible for
anything.** **A `CHANNELS SEPARATED` verdict means the documents are
clear, not that the separation is correct.**

**Second, and it now carries a rider.** **`CHANNEL-B0` can classify the
coupling's STRUCTURE; it cannot report its MAGNITUDE**, because `ε` is
not closed and its computation waits on an open node. **Say that
universality and strength are separable and that only the first was
assessed.**

**A non-universal scalar force would not be a defect**, and
neither would a universal one. **Scalar-mediated dark matter is a
legitimate mechanism; so is a universally coupled scalar in the
gravitational sector.** **Whichever the repository states, the finding
is a CLASSIFICATION and not a criticism.**

**And say what the classification does NOT follow from:** **not from the
mediator's spin, and not from the coupling's suppression.** **If the
manuscript calls the halo a dark-matter mechanism, that is the
manuscript's classification and this task reports it as such.**

**Third.** **`Z` being a kinetic coefficient tells you nothing about its
source.** **Say that the programme has computed one side of the TT
channel and not the other**, and **that `SRC-B0` already established the
source side is absent.**

**Fourth.** **The equivalence principle's status has four possible
answers and they are not interchangeable.** **A claim is not a
derivation; a derivation elsewhere is not a derivation here; and neither
is a test.** **Say which one the repository supports.**

**Fifth.** **The vocabulary is the Researcher's and both passes may miss
a separation stated in other terms.** **An absence of the words
`spin-0` and `fifth force` is not evidence that the channels are
conflated.** **Say what was searched and what you added.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  scope artifact. **Nothing else, at all.**
- **No file existing at the evidence base may be modified.**
- **Derive nothing, compute nothing, recommend nothing.**
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
  labelled MEASURED or INTENDED**, and **every SHA pasted from command
  output**;
- **A1's verbatim `origin` URL and the pasted `main` SHA**;
- **A3's environment diagnosis in Rule 13's order, run FIRST**;
- **A4's two-pass inventory with counts, union, PASS-2-only lines, and
  any term you added**;
- **A5's `Z` coupling finding and the confirmation about kinetic
  coefficients**;
- **A6's quoted `:633-640`, the suppression, and — SEPARATELY — the
  universality status as `UNIVERSAL`, `NON-UNIVERSAL` or `UNSTATED`**;
- **A7's conflation instances with lines and the count**;
- **A8's scope finding and the four-state equivalence-principle
  status**;
- **A9's verdict with its evidence**, the parameter-independence
  statement if `CHANNELS SEPARATED`, and the confirmation that no
  magnitude was reported as frozen and `EPS-B0` was not cited;
- **A10's search and result**;
- **A11's cumulative figures and contributions, separately labelled**;
- **A12's path count, the manuscript blob id at both ends, and the
  artifact count re-measured**;
- **A13's four invariants**;
- **A14's two runs**, both configs verbatim, the section count `P7` saw,
  what `RUN 1` did, and confirmation the output was parsed not grepped;
- **A15's counts**;
- **§7's five Rule 16 junctions**;
- **whether reading made you want to decide which channel is right, to
  derive the monopole coupling, or to say the equivalence principle
  holds.** **Say which and why, and confirm you did not**;
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
    MEASURED    af145d5a3e36e6bca62f038092748ada3abdcec1.

    target      Z's channel
    method      read CONVENTIONS.md line 20
    MEASURED    "The induced axis/transverse-traceless (TT) graviton
                kinetic coefficient, i.e. the coefficient of the induced
                Einstein-Hilbert term ∫√g R". Z is a SPIN-2 kinetic
                coefficient. It states no coupling; A5 requires the
                source looked for separately.

    target      θ̃'s coupling
    method      read paper lines 633-640
    MEASURED    ":633-636 One element of this identification remains
                open: the effective coupling of the angular mode to
                visible (baryonic) matter with the scalar (monopole)
                structure used phenomenologically in [Paper 1].
                :637-640 A pure Goldstone couples derivatively; a
                monopole coupling must be induced by the explicit
                breaking and/or by mixing with the heavy radial mode,
                and is therefore suppressed by powers of ε and the
                mixing angle."
    NOT DETERMINED  suppression by ε and a mixing angle does NOT by
                itself determine universality. Suppression concerns
                magnitude; universality concerns whether the scalar
                charge is the same across species or bodies. An earlier
                draft of this record inferred non-universality from
                suppression and labelled it DERIVED; that inference does
                not hold and is retracted. A6 must establish whether the
                manuscript states composition or object dependence,
                universality, or neither.

    target      the universality claim
    method      grep for equivalence principle and universal coupling
    MEASURED    :816 "\subsection{Emergent gauge redundancy and
                universal coupling}"; :832 "the equivalence principle is
                an emergent consequence of the". The claim EXISTS. Its
                CHANNEL SCOPE was not determined by this author; A8
                requires it read.

    target      whether EPS-B0 is available to this task
    method      git rev-parse origin/main; git merge-base --is-ancestor;
                git cat-file -e on the EPS-B0 artifact path
    MEASURED    origin/main = af145d5a…; the EPS-B0 branch tip
                efb8d63f… is NOT an ancestor of main; the artifact
                derivations/P2-EPS-B0_epsilon-tractability-scope.md is
                ABSENT from this evidence base.
    CONSEQUENCE §1a states EPS-B0's verdict as a REPORTING CONSTRAINT
                rather than as citable evidence. The executor cannot
                verify it and A9 forbids citing it. Had this
                specification told the executor to cite an artifact
                absent from its own base, the executor could only have
                accepted it from this author's prose.

    target      channel vocabulary
    method      git grep -cil over derivations/ and paper/
    MEASURED    spin-2 1 file, spin-0 0, fifth force 0,
                transverse-traceless 2, equivalence principle 1,
                universal coupl 1. §3 warns that absence of vocabulary
                is not a finding about the physics.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 0 modifications;
                parse OK, counted equals stated per category.
