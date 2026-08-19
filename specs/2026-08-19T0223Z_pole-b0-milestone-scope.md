# Task specification — `POLE-B0`: what the manuscript's own decisive test would require

Specification evidence base: `11af14a792c5858b368180d99ab9ee4692a7f698`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/pole-b0-milestone-scope
    Cut from           authoritative main — refs/remotes/origin/main

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This task does not touch `main`.** Integration is a separate task.

**NORMATIVE EXECUTION ORDER, stated once:**

    A3  environment conformance
    A1  repository identity, refs, branch availability
    A2  review binding
    A4  onward

**IT COMPUTES NOTHING AND BUILDS NOTHING.** It determines what the
manuscript's own named milestone would require, and what already exists.

---

## 0. The manuscript names its own decisive test, and has not performed it

**Measured verbatim at the evidence base:**

    :805-809  We also state plainly the strongest form of the dynamical
              claim: that the interacting lattice theory possesses a
              genuine massless spin-2 *pole* in ⟨TT⟩ (rather than merely
              an induced kinetic term for an external field) is
              supported by the Ward structure above but is ultimately a
              nonperturbative question.

    :810-814  A lattice measurement of the Barnes–Rivers–projected
              stress-tensor correlator, checking for a single p² = 0
              pole in the spin-2 sector with vanishing spin-1/0
              residues, is the decisive test; we identify it as the key
              numerical milestone for this programme.

**Two things are stated there and both matter.**

**First, the manuscript distinguishes an INDUCED KINETIC TERM FOR AN
EXTERNAL FIELD from a GENUINE MASSLESS SPIN-2 POLE.** **Everything the
`βV` line has computed — `Z`, `β_s`, the coefficient of `∫√g R` — is the
first.** **The second is what would make the emergent metric a
propagating degree of freedom of the interacting theory.**

**Second, the manuscript calls it NONPERTURBATIVE and says the Ward
structure only SUPPORTS it.** **So this is not a gap the programme
overlooked; it is one the manuscript identifies and defers.**

> **What would performing this test require, and what already exists?**

## 1. Why this is worth scoping before anything else in the `βV` line

**`RECON-01b`'s `k`-scan validates heat-kernel arithmetic against a
blind target.** **This milestone asks whether the object that arithmetic
describes is a clean spin-2 excitation at all.**

**If the spin-1/0 residues do not vanish, the emergent graviton is not
clean** — and a correct `−(k+2)` would then be a correct coefficient for
something that is not a graviton.

**Do not conclude from this that the milestone should be done first.**
**That is a PI decision and §4 forbids you from making it.** **State
what each would establish and stop.**

## 2. The five questions

**One: what does the test actually require?** **Report the distinct
components**, and for each: **an implementation exists here, a
specification exists, or neither.** **Four mutually exclusive states as
in `RECON-B0`, with `N_total = N_both + N_impl + N_spec + N_neither`.**

**An implementation counts only if it is POTENTIALLY APPLICABLE to this
test.** **Existence is not availability.**

**Two: what already exists?** **Measured by the Researcher over the
whole tree: `Barnes` 7 files, `Rivers` 12, `projector` 54,
`stress-tensor correlator` 8, `pole` 67, `spin projector` 0.**

**Report what those hits actually are.** **A high count is not
machinery** — `projector` at 54 files may be the axis-TT projection
`RECON-01a` already uses, which is a different object from a
Barnes–Rivers spin decomposition. **Distinguish them.**

**Three: is `⟨TT⟩` computable from what is on `main`?** **`RECON-01a`
landed `Δ⁽¹⁾[g,h]`, `Δ⁽⁰⁾[g,h]` and validated `h`-derivative
machinery.** **Report whether a stress-tensor correlator is reachable
from those, or whether it needs a different construction.**

**`SRC-B0` established the SOURCE side is absent.** **Report whether
`⟨T T⟩` — a correlator of stress tensors — inherits that absence, or
whether the correlator is computable without a source configuration.**
**These are different questions and the answer is not obvious.**

**Four: does the test depend on `R1`–`R5`?** **Per node, report
`INDEPENDENT`, `DEPENDENCE ESTABLISHED`, or `DEPENDENCE NOT
ESTABLISHED`.** **Silence is not independence.**

**Report `R4` — microscopic variables, state space, measure — with
particular care.** **A correlator is a measure-weighted expectation, and
`DET-01` established the functional measure is `NOT DETERMINABLE` from
frozen conventions.** **Report whether the correlator inherits that.**

**Five: what would count as failure, and would it be visible?** **The
manuscript states the criterion — a single `p²=0` pole in spin-2 with
vanishing spin-1/0 residues.** **Report what a pre-registration would
have to fix: what "vanishing" means numerically, at what volumes and
masses, and how a lattice artefact would be distinguished from a
physical non-vanishing residue.**

**Do not choose any of these.** **State what must be chosen.**

## 3. The pre-registered verdicts

    TRACTABLE FROM WHAT EXISTS
        the components are present or specified, and no open ruling
        blocks it. Name what remains to be built.

    TRACTABLE BUT BLOCKED PENDING A RULING
        the construction is legible but depends on one or more open
        R-nodes. NAME WHICH.

    REQUIRES A CONSTRUCTION NOT YET SCOPED
        a component is neither implemented nor specified and its
        specification is itself substantial work. NAME IT.

    NOT DETERMINABLE FROM THIS REPOSITORY
        the repository does not say enough to determine the
        requirements. Name the missing evidence.

**More than one may apply in part; if so, report the governing one and
say why.**

## 4. What this task must not do

- **Do not touch `main`**, do not merge.
- **DO NOT COMPUTE ANYTHING.** No correlator, no projection, no
  residue, no pole, no estimate of any of them.
- **Do not build or prototype.** **Do not run any script.**
- **Do not decide whether this milestone or `RECON-01b` should come
  first.** **That is a PI decision.** **Report what each would
  establish; do not rank them.**
- **Do not choose a vanishing criterion, a volume, or a mass.**
- **Do not judge whether the emergent graviton IS clean.** **The
  manuscript calls this nonperturbative and unresolved; nothing here
  resolves it.**
- **Do not adjudicate `R1`–`R5` or the measure question.**
- **Do not modify any existing file.**
- **Do not add a register entry anywhere.**
- **Do not push any ref but this task's branch.**

## 5. Acceptance criteria

**A1 — Repository, refs, branch availability.** Report the `origin`
remote URL as measured, **verbatim and not normalised**; confirm it
identifies `zetacheng/2-emergent-gravity`. Fetch, then report
`refs/remotes/origin/main` **pasted from `git rev-parse` output** and
confirm it is `11af14a792c5858b368180d99ab9ee4692a7f698`.

**Report whether `science/pole-b0-milestone-scope` already exists.**
**If it does, STOP.**

**Every SHA in your report is pasted from command output.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0.

**A4 — The milestone passage, re-read.** **Quote `:805-814` verbatim
with line numbers**, and **report both statements separately**: the
induced-kinetic-term versus genuine-pole distinction, and the
nonperturbative characterisation.

**Report whether the manuscript states anywhere that the test has been
performed, attempted, or scheduled.** **Search and report.**

**A5 — The component inventory**, per question one. **Four mutually
exclusive states and their sum.** **Applicability stated per
implementation.**

**A6 — What exists, classified**, per question two. **Report the hit
counts you measure**, and **for each term, what the hits actually
are.** **Distinguish an axis-TT projection from a Barnes–Rivers spin
decomposition if both appear.**

**A high count is not machinery.** **Report how many hits are usable
components versus prose, citations, or a different object with a similar
name.**

**A7 — Reachability from `RECON-01a`**, per question three. **Report
whether `⟨TT⟩` is computable from the landed operators and derivative
machinery**, and **whether it inherits `SRC-B0`'s absent source side.**

**Answer the second explicitly.** **A correlator of stress tensors and a
stress tensor sourcing a field are not the same object**, and **whether
the absence transfers is a question, not an assumption.**

**A8 — `R1`–`R5` dependence**, per question four. **Per node, one of
three states.** **`R4` reported with its own paragraph**, including
whether the correlator inherits `DET-01`'s unfixed measure.

**A9 — The failure criterion's requirements**, per question five.
**Report what must be pre-registered: the numerical meaning of
"vanishing", the volumes and masses, and the artefact-versus-physics
discriminator.** **Choose none of them.**

**A10 — The verdict**, one of §3's four, **with the evidence.** **If
more than one applies in part, name the governing one and say why.**

**A11 — Nothing computed, nothing ranked.**

**Search the artifact, the report and the commit messages for any NEWLY
COMPUTED OR ESTIMATED SCIENTIFIC QUANTITY BELONGING TO THIS MILESTONE**:
a value of `⟨TT⟩`, a projected correlator, `Π^{(2)}(p)` or any spin
component of it, a pole position, a spin-0 or spin-1 residue, or a
numerical estimate or bound on any of them.

**EXPRESSLY EXCLUDED**, because this task's own criteria require them:
**governance and checker measurements, hit counts, path counts, test
counts, section counts, blob ids, SHAs, timestamps, environment
versions, and any figure quoted from the repository.**

**An earlier draft searched for "any computed quantity", which `A6`,
`A12`, `A13`, `A15` and `A16` all require this report to contain.** **A
correct execution would have violated that search by satisfying those
criteria** — the fourth time this line has issued a criterion that a
correct execution cannot satisfy.

**Then search separately for any statement that one task should precede
another.** **Report both searches and their results.**

**A12 — Scope, frozen manifest.**

    stated: 4 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: 11af14a792c5858b368180d99ab9ee4692a7f698
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-POLE-B0_milestone-scope.md
      reports/2026-08-XXT{HHMM}Z_pole-b0-milestone-scope.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_pole-b0-milestone-scope.md
      specs/2026-08-XXT{HHMM}Z_pole-b0-milestone-scope.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths.** **Report the cumulative figure at each commit and the
contributions separately.** **`append_only: DECISION_LOG.md` is a
checker-configuration declaration, NOT an authorisation to write that
file.** **Measure the UTC time and use the value you measured.**

**A13 — Nothing existing changed.** Every path blob-identical at the
head, **`paper/emergent_gr_paper_v2_15.tex` in particular — report its
blob id at both ends.** **Report the count compared**, and confirm for
`GATES.md`, `CONVENTIONS.md`, **every `derivations/P2-*` artifact —
re-measure the count**, the two `scripts/recon2026/` files and
`tests/test_recon2026_flat_limit.py`, both registers, and everything
under `results/`.

**A14 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four, read SCOPED.**

**Also report whether any gate covers this milestone.** **Search
`GATES.md` for the milestone's own terms and report the result.**

**A15 — The checker over this task's own range**, base `11af14a7…`, head
**commit 3**. Two runs, `RUN 1` observational and `RUN 2` naming only
this task's specification.

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` AS IT EXISTS.** **Measured by the previous
executor: it is NOT a per-property field — it occurs twice per document,
nested inside `evidence` on `P3` and `P7` only.** **Report what you
find; do not manufacture nine values.**

**Confirm no `DECLARATION_CONFLICT`.** **`P7` must report fourteen
sections.** **`PASS` at zero is a STOP.** **RUN 2 is stop-governing.**
**Both configs and both JSON outputs verbatim.** **PARSE the output; do
not grep it.**

**A15-final, post-report evidence:** re-run RUN 2 at commit 4.

**A16 — Validators, exit status 0.** **Expected 332 passed, 2
deselected.**

**A17 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 6. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_pole-b0-milestone-scope.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_pole-b0-milestone-scope.md
    commit 3  derivations/P2-POLE-B0_milestone-scope.md
    commit 4  reports/2026-08-XXT{HHMM}Z_pole-b0-milestone-scope.md

**Committed report — measured at commit 3:** A1–A14, A16 and A17;
**A15's two runs with both configs verbatim**; commit 1–3 SHAs pasted
from `git rev-parse` and stored messages; commit 4's intended message;
**A12's final scope stated as INTENDED.**

**Post-report evidence, NOT written back:** A12's final scope measured
base-to-commit-4; A15-final; A16 at commit 4; A17 for commit 4; the
push; the branch tip read back from command output.

**Nothing in the committed report may claim to measure commit 4.**

## 7. Rule 16 assessment

**Rule 16 is operative.** **Five junctions, all five required.**

**First, and it is the distinction the whole task turns on.** **An
induced kinetic term is not a pole.** **Everything the `βV` line has
computed is the former** — `Z` is a coefficient for a metric treated as
an external field. **The milestone asks whether the interacting theory
has a propagating spin-2 excitation at all.** **Say that a validated
`−(k+2)` would not answer it.**

**Second.** **The manuscript itself calls this nonperturbative and says
the Ward structure only SUPPORTS the claim.** **This assessment does not
change that status.** **A `TRACTABLE` verdict would mean the measurement
is buildable, not that the answer is known or likely.**

**Third.** **A scope assessment ranks nothing.** **This task must not
say whether the milestone or `RECON-01b` comes first**, and **a reader
who takes a `TRACTABLE` verdict as a recommendation would be reading
one in.**

**Fourth.** **The counts in §2 are the Researcher's and are file counts,
not machinery counts.** **`projector` at 54 files almost certainly
includes the axis-TT projection already in use, which is a different
object.** **Say what you found and how you separated them.**

**Fifth.** **If the correlator inherits `DET-01`'s unfixed measure, this
milestone is not independent of the microscopic line either** — and
**the programme would then have no route that is.** **Report `A7` and
`A8` prominently for that reason.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  scope artifact. **Nothing else, at all.**
- **No file existing at the evidence base may be modified.**
- **Compute nothing, build nothing, rank nothing, choose no criterion.**
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
- **A4's quoted passage, both statements separately, and the
  performed/attempted/scheduled search**;
- **A5's four counts and their sum, with applicability per
  implementation**;
- **A6's hit counts and what the hits are, with the axis-TT versus
  Barnes–Rivers distinction**;
- **A7's reachability finding and the explicit answer on whether
  `SRC-B0`'s absence transfers**;
- **A8's five node states, with `R4` in its own paragraph**;
- **A9's list of what must be pre-registered, with nothing chosen**;
- **A10's verdict with its evidence**;
- **A11's two searches and their results**, with the exclusion of this
  task's own required measurements stated;
- **A12's cumulative figures and contributions, separately labelled**;
- **A13's path count, the manuscript blob id at both ends, and the
  `P2-*` count re-measured**;
- **A14's four invariants and the gate-coverage search**;
- **A15's two runs**, both configs verbatim, `declared_source` as it
  exists, the section count `P7` saw, what `RUN 1` did, and confirmation
  the output was parsed not grepped;
- **A16's counts**;
- **§7's five Rule 16 junctions**;
- **whether reading the milestone made you want to estimate whether the
  residues vanish, to say which task should come first, or to start
  building the projector.** **Say which and why, and confirm you did
  not**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 10. Pre-issue literal verification record

    target      the evidence base
    method      git fetch; git rev-parse origin/main
    MEASURED    11af14a792c5858b368180d99ab9ee4692a7f698, the head
                landed by the CHANNEL-B0 integration.

    target      the milestone passage
    method      read paper lines 800-815
    MEASURED    :805-809 "We also state plainly the strongest form of
                the dynamical claim: that the interacting lattice theory
                possesses a genuine massless spin-2 *pole* in <TT>
                (rather than merely an induced kinetic term for an
                external field) is supported by the Ward structure above
                but is ultimately a nonperturbative question."
                :810-814 "A lattice measurement of the
                Barnes--Rivers--projected stress-tensor correlator,
                checking for a single p^2 = 0 pole in the spin-2 sector
                with vanishing spin-1/0 residues, is the decisive test;
                we identify it as the key numerical milestone for this
                programme."
    NOTE        :805-809 was NOT in the Researcher's earlier reading and
                is the more consequential half: it distinguishes an
                induced kinetic term from a genuine pole, and calls the
                question nonperturbative.

    target      existing machinery
    method      git grep -cil over the whole tree
    MEASURED    Barnes 7 files, Rivers 12, projector 54,
                stress-tensor correlator 8, pole 67, spin projector 0.
    LIMIT       these are FILE COUNTS, not machinery. A6 requires the
                hits classified. The Researcher did not open them.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 0 modifications;
                parse OK, counted equals stated per category.
