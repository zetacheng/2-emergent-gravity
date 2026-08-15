# Task specification — `D-pre-A`: the canonical kinetic operator, candidate dossier and selection grounds

Specification evidence base: `ae3604def317667b44ea59458569ba105463fd6b`

    Branch to create   science/dpre-a-kinetic-operator-dossier
    Cut from           authoritative main @ ae3604de…

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This task does not touch `main`.** It produces a branch. **Integration
is a separate task.**

**IT FREEZES NOTHING AND SELECTS NOTHING.** It produces the material a
PI ruling on the canonical kinetic operator requires, and **stops before
the ruling.**

---

## 0. What this task is, and what an earlier framing got wrong

**`D-pre` was described as a freeze.** **Measured against
`P2-LATTICE-ONTOLOGY-01`'s delegation table, almost nothing it delegates
can be frozen before the kinetic operator is chosen:**

    §185  microscopic Euclidean variables, state space and measure
          — DELEGATED. The field content differs between candidates:
            a staggered formulation carries one-component fields where
            a Wilson formulation carries four.
    §188  which fields are summed over versus held fixed — DELEGATED
    §189  canonical kinetic operator and species accounting
          — DELEGATED. THIS IS THE CHOICE ITSELF.
    §190  geometry map {t_ij} -> g, e, ω and curvature estimator
          — DELEGATED. The t_ij ARE the operator's hoppings.
    §191  reference equivalence class and matching conditions
          — DELEGATED

**So `D-pre-A` cannot be "freeze the choice-independent parts".** **There
is almost no choice-independent part.** **An earlier framing by the
Researcher said `D-pre-A` would unblock the phase line's `C-iii`; it will
not.** **The PI ruling it informs will, together with the freeze task
that follows it.**

**What `D-pre-A` delivers is a dossier**: for each candidate kinetic
operator, what it commits the theory to, derived rather than recalled.

## 1. The PI ruling this task serves

**Recorded verbatim as issued.**

> **`D-pre` does not impose an a priori target species count. The species
> content of the microscopic theory is the species ledger implied by the
> selected canonical H(4) kinetic operator, including any lattice
> multiplicities or lifted modes intrinsic to that operator. Whether some
> microscopic species decouple, become gapped, pair, confine, or
> otherwise disappear from the infrared observable spectrum is a
> downstream dynamical question and is not used to define the canonical
> microscopic theory. The canonical kinetic operator must instead be
> selected on independent physical and structural grounds; agreement with
> a desired species count is not an admissible selection criterion.**

**The ruling removes a bad selection criterion. It does not supply a good
one.** **That is what this dossier is for**: it assembles the independent
physical and structural grounds so that a ruling can be made on them.

**Do not select. Do not recommend a selection.** **Presenting the
grounds is the deliverable; weighing them is the PI's.**

## 2. The four candidates

`P2-LATTICE-ONTOLOGY-01` §347 names them and says the choice among them
**is a choice of the theory's matter content**, not a regulator
convenience: **naive**, **Wilson**, **staggered**, **overlap**.

**For each, the dossier answers the same questions**, and **says which
answers it derived and which it could not establish from the repository
alone.**

### (a) The species ledger, derived, and the derivation method is not
### shared between candidates

**For each candidate, derive its physical free-fermion species content
from THAT FORMULATION'S OWN canonical free-field representation.**
Identify the independent low-energy branches, tastes or species; the
momentum regions or reconstructed Brillouin zones they arise from; and
**any additional lattice branches that are lifted rather than absent.**
**State the derivation method used, per candidate.**

**DO NOT equate a raw zero or pole count in the unreduced Brillouin zone
with physical species count unless that equivalence is derived FOR THAT
FORMULATION.**

**The methods differ and the specification does not pretend otherwise:**

    naive       corner expansion about the degenerate zeros
    Wilson      corner branches together with the Wilson mass shifts
    staggered   spin/taste reconstruction — the one-component
                momentum representation's zero count is NOT the taste
                count, and treating it as such would be a derivation
                error
    overlap     the free spectrum of the overlap operator itself, with
                the kernel mass or domain-wall height convention
                stated, and with the propagator taken as the physical
                fermion propagator identified for that formulation

**An earlier version of this section required all four to be answered by
"poles in the Brillouin zone".** **That template is Wilson-shaped.** **A
dossier written to avoid prejudging the operator would have prejudged it
by measuring every candidate with one candidate's ruler.**

**Derive. Do not recall.** The repository contains no literature, and **a
species count carried from memory is the kind of unanchored figure this
programme has repeatedly had to retract.** **If a figure cannot be
derived from the material available, mark it NOT ESTABLISHED.**

### (b) Reflection positivity

`P2-LATTICE-ONTOLOGY-01` §181 freezes reflection positivity of the
action **as an obligation**. **For each candidate, state whether the
obligation is satisfied, violated, or not established from the material
available.** **"Not established" is an acceptable and expected answer for
at least one candidate**, and is more useful than a recalled claim.

### (c) Compatibility with what is already frozen

**Check each candidate against the four items `P2-LATTICE-ONTOLOGY-01`
freezes rather than delegates** — §180 Euclidean-fundamental formulation
with derived Hamiltonian; §181 reflection positivity as obligation; §182
isotropy of the four axes; §184 the vacuum selection rule. **Report any
candidate that is inconsistent with any of the four**, and **the lines
that establish the inconsistency.**

### (d) What each candidate does to the existing computed evidence

**The exploratory work used a Wilson-form kernel.** **Measured at this
evidence base**, the exploratory script's denominator is
`s + w²` with `s = Σ sin²(p_μ)` and `w = Mhat + Σ(1 − cos p_μ)`.

**For each candidate, state what happens to the existing results if it
becomes canonical:**

- **which stored results remain evidence about the canonical theory**;
- **which become evidence about a theory the programme did not adopt**;
- **and in particular, what becomes of the complement relation
  `I0(Mhat) = I0(−8−Mhat)`**, which is a property of the Wilson term and
  not of the lattice.

**State this as a consequence, not as an argument for or against any
candidate.** **Continuity with existing computation is a convenience, and
§1's ruling requires independent physical and structural grounds** —
**report the consequence and let the PI decide what weight it carries.**

### (e) What each candidate does to `N`

**Measured: `P2-GENERATOR-SUM-CRITICALITY_01` §145 gives the gap
condition `1 = (8/N) G I0` and `G_c = N/(8 I0)`.** **`N` enters the
critical coupling directly.**

**`P2-LATTICE-ONTOLOGY-01` §356 says the species multiplicity enters
`N`-accounting explicitly. IT DOES NOT SAY HOW.**

**Measured: in `P2-GENERATOR-SUM-CRITICALITY_01`, `N` is the `U(N)`
flavour rank** — the `λ^A` form an `N×N` Hermitian basis with
`A = 0 … N²−1`. **That is a flavour-index rank. It is not a lattice
species multiplicity, and no rule in the repository states that one
multiplies into the other.**

**So the question is not "what new `N` does this candidate give".** **It
is: HOW does this candidate's species ledger enter the existing
`N`-accounting?** **Derive the mapping before applying it.**

**If the mapping cannot be established from the repository, mark it NOT
ESTABLISHED and stop there.** **Do not multiply a taste or doubler count
into `N`**, and **do not report a revised `G_c`** — a consequence derived
through a link that does not exist is worse than no consequence.

**An earlier version of this section presupposed
`species ledger → new N → new G_c`.** **The middle link is absent from
the repository**, and the Reviewer identified it.

**Do not recompute the adopted parameter domain either way.** The domain
is stated as `G/G_c` and the ratio is unaffected by a change in `N`;
**what would need revisiting is any statement reading `G/G_c` as a
physical quantity**, and that is a later task's.

## 3. One connection the dossier must address

**For the Wilson candidate, the complement relation is generated by the
Brillouin-zone involution `p_μ → π − p_μ`**, which sends
`Σ(1 − cos p_μ) → 8 − Σ(1 − cos p_μ)` and thereby yields
`I0(Mhat) = I0(−8 − Mhat)`.

**The involution exchanges the neighbourhood of the origin with the
all-`π` corner. It is a map of the WHOLE zone, not a statement about one
corner.** **Consequently a stationary branch near `Mhat ≈ −8` is
CONDITIONALLY associated with the all-`π` Wilson doubler branch** — and
**that association is something the dossier derives, not something this
specification asserts.**

**An earlier version of this section called the complement root "the
all-π corner of the Wilson term".** **That is too strong**: the identity
comes from the involution over the entire zone, and only the association
of one particular branch with the corner is corner-specific.

**Under §1's ruling and a Wilson-form canonical operator, that corner is
a species, not an artifact.**

**So state, for the Wilson candidate specifically:** whether the
negative-mass stationary branch recorded as `DEFERRED-02` is the doubler
sector's reflection, **and what that would mean for the `C1` and `C3`
findings** — which established that the branch's position and restricted
curvature carry no content independent of the ordinary branch.

**If the answer is yes, the correct reading is that the branch is not
independent BECAUSE it is the mirror, not because it is spurious.**
**Say whether that reading holds, and do not extend it to candidates
other than Wilson.**

## 4. `(b)` is registered, not performed

**The PI has ruled that option `(b)` of `P2-LATTICE-ONTOLOGY-01` §354 —
demonstrating that `H(4)`'s structure dynamically removes or gaps
unwanted species — is a downstream hypothesis and not a definitional
requirement.**

**Add `DEFERRED-04` to `derivations/P2-DEFERRED-ITEMS.md`**, whose own
text says entries are added by PI decision. **Record:**

- the question, as a hypothesis: **does the canonical `H(4)` dynamics
  naturally gap or otherwise remove some microscopic species from the
  low-energy spectrum?**
- **that a NO answer does not make the microscopic theory inconsistent**
  — it means the theory's predicted infrared species content is what it
  is, and phenomenology compares against that;
- **that a YES answer would be derived physics rather than a definitional
  rescue**, which is the whole reason it is deferred rather than assumed;
- **the cross-reference to `DEFERRED-02`**, the negative-mass branch,
  which §3 may show is the same sector seen from the other side.

**Append only.** **Do not edit `DEFERRED-01`, `-02` or `-03`.**

## 5. What this task must not do

- **Do not touch `main`**, do not merge.
- **DO NOT SELECT A CANDIDATE**, and **do not rank, recommend, or
  indicate a preference.** **Reporting that one candidate satisfies more
  frozen obligations than another is a finding; concluding that it should
  therefore be chosen is not this task's.**
- **Do not freeze anything.** Not the operator, not the measure, not the
  geometry map, not the species ledger. **`D-pre-A` produces a dossier.**
- **Do not compute anything new about the exploratory kernel**, and **do
  not run `scripts/p2_phase01_scalar_exploratory.py`.**
- **Do not recompute or reinterpret the adopted parameter domain.**
- **Do not modify `GATES.md`**, and **do not change any gate status or
  prerequisite state.** **`P2-PHASE-01` is untouched by this task.**
- **Do not modify `derivations/P2-LATTICE-ONTOLOGY-01.md` or
  `P2-LATTICE-ROUTE-01.md`.** **They are consumed, not reopened**, per
  `ROUTE-01` §185.
- **Do not answer `OPEN-AC-1`, `OPEN-AC-3`, `C2`, `OPEN-CC-2` or
  `OPEN-CC-3`.**
- **Do not claim this task unblocks `C-iii` or `D0`.** §7 governs.

## 6. Acceptance criteria

**A1 — Refs and pinned inputs.** `refs/heads/main` resolves to
`ae3604def317667b44ea59458569ba105463fd6b`. Report the Git blob ids of
`derivations/P2-LATTICE-ONTOLOGY-01.md`,
`derivations/P2-LATTICE-ROUTE-01.md`,
`derivations/P2-GENERATOR-SUM-CRITICALITY_01.md`,
`derivations/P2-DEFERRED-ITEMS.md` and
`scripts/p2_phase01_scalar_exploratory.py`. **Any ref mismatch → STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **If blank or naming a different digest, STOP and say
which.** Report both digests equal.

**A3 — The species ledger, per candidate, DERIVED BY THAT
FORMULATION'S OWN METHOD.** Report, for each of the four: **the
derivation method used and why it is the right one for that
formulation**; the independent low-energy branches, tastes or species;
the momentum regions or reconstructed zones they arise from; and the
**lifted-versus-absent** distinction.

**Report explicitly, per candidate, whether raw zero or pole counting
was used, and if so the derivation that licenses it for that
formulation.** **Using it for staggered without that derivation is a
STOP.**

**State per figure whether it was derived here or is NOT ESTABLISHED.**
**A figure reported without its derivation fails this criterion**, and
**"standard result" is not a derivation.**

**A4 — Reflection positivity, per candidate.** **Satisfied, violated, or
NOT ESTABLISHED**, with the reasoning or the reason it could not be
established. **Report the count of each.** **`NOT ESTABLISHED` is
expected for at least one candidate and is not a failure of this
criterion.**

**A5 — Compatibility with the four frozen items**, per candidate, with
the lines that establish any inconsistency. **Report all four checks for
all four candidates: sixteen results.**

**A6 — Consequences for existing evidence**, per candidate, per §2(d).
**Report what happens to the complement relation under each.**

**A7 — The species-to-`N` MAPPING, derived before anything is applied.**

**First report what `N` is** in `P2-GENERATOR-SUM-CRITICALITY_01`, **as
measured, with line numbers**, and **the gap condition as measured
there** — **do not restate either from this specification.**

**Then, per candidate, report the mapping**: how that candidate's
species ledger enters the existing `N`-accounting. **`NOT ESTABLISHED`
is an expected and acceptable answer** and **is the required answer if
the mapping cannot be derived from the repository.**

**Only where a mapping IS derived may a consequence for `G_c` be
reported.** **A revised `G_c` reported without its mapping is a STOP.**
**Report the count of candidates for which the mapping was established
and the count for which it was not.**

**A8 — §3's Wilson-specific connection, DERIVED not assumed.**

**First derive the complement identity from the Brillouin-zone
involution `p_μ → π − p_μ`**, and **report that derivation.** **Then**
report whether the `DEFERRED-02` branch is conditionally associable with
the all-`π` doubler branch, **with the derivation that establishes or
fails to establish it**, and **what it implies for the `C1` and `C3`
findings.**

**`NOT ESTABLISHED` is acceptable here.** **Report explicitly that any
association is confined to the Wilson candidate** and **that the
canonical operator is not chosen**, so the statement is conditional on a
candidate the programme has not adopted.

**A9 — `DEFERRED-04` added, append-only.** Report the diff of
`derivations/P2-DEFERRED-ITEMS.md`. **Zero deleted lines**, and **the
base file an exact in-order subsequence of the head file** — report the
matched count against the base line count. **Confirm `DEFERRED-01`,
`-02` and `-03` are byte-identical**, and **that the register now carries
four entries.**

**A10 — No selection made.** **Search the dossier and the report for any
sentence that selects, ranks, recommends or prefers a candidate, and
report the search.** **Report that none was found**, or **report what you
found and treat it as a STOP.** **This criterion is the one most easily
satisfied in appearance**: a dossier that lists one candidate's
advantages at length and another's briefly has ranked them without
saying so. **Report the length of each candidate's treatment.**

**A11 — Scope, frozen manifest.**

    stated: 4 additions, 1 modification
    append_only:
      DECISION_LOG.md
      derivations/P2-DEFERRED-ITEMS.md
    authorised_gates: []
    base: ae3604def317667b44ea59458569ba105463fd6b
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md
      reports/2026-08-XXT{HHMM}Z_dpre-a-kinetic-operator-dossier.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_dpre-a-kinetic-operator-dossier.md
      specs/2026-08-XXT{HHMM}Z_dpre-a-kinetic-operator-dossier.md
    modify:
      derivations/P2-DEFERRED-ITEMS.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Five paths.** **`append_only` names two paths, one per line, and this
is the first task to declare more than one** — `P3` checks both.

**The one-path-per-line form is required and was verified.** **An earlier
draft wrote both on the `append_only:` line and the parser returned
`NOT_PARSEABLE`: "not a path under 'append_only:'".** **The author's own
pre-issue run caught it**, which is the discipline `A1`'s rule was
consolidated for.

**A12 — Protected paths.** Every path existing at the evidence base other
than `derivations/P2-DEFERRED-ITEMS.md` is blob-identical at the head.
**In particular `GATES.md`, `CONVENTIONS.md`, both lattice artifacts, the
exploratory script, and everything under `results/`, `scripts/` and
`tests/`.** Compare path by path and report the count.

**A13 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; **both pins match their targets.** **Report all four.**
**Neither pin names `P2-DEFERRED-ITEMS.md`** — verify and report that,
because a task modifying a pinned file would owe a re-pin under Rule 19.

**A14 — The checker over this task's own range**, base `ae3604de…`, head
**commit 3**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_dpre-a-kinetic-operator-dossier.md

**Config for both runs, written to agree with this specification's own
declarations:**

    append_only_paths          ["DECISION_LOG.md",
                                "derivations/P2-DEFERRED-ITEMS.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT` arose.** **`P3` now has two declared paths and
one of them is modified by this task** — **report what `P3` returned for
each.**

**`P7` must report fourteen sections.** **`PASS` at zero is a STOP.**

**RUN 2 is stop-governing; any failure is a STOP.** **Both configs and
both JSON outputs verbatim.** **Report the subject set RUN 1 actually
selected, as measured.**

**A14-final, post-report evidence:** re-run RUN 2 at commit 4.

**A15 — Validators, exit status 0.** Run `python -m pytest` from the
repository root. **Report pass and deselect counts before and after.**
**Expected: unchanged at 324 passed, 2 deselected.**

**A16 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.** **Commits 1–3 go in the report; commit 4 is post-report
evidence.**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Four junctions, all four required in the report.**

**First.** **This task does not unblock `C-iii`, and it does not unblock
`D0`.** A dossier is not a freeze. **`C-iii` becomes evaluable when the
PI rules and a freeze task lands; `D0` additionally requires
`D-pre-B`'s Euclidean–spectral equivalence.** **Say both**, and **say
that an earlier framing by the Researcher claimed `D-pre-A` would unblock
the phase line.**

**Second.** **The dossier's completeness is bounded by what can be
derived from this repository.** There is no literature here. **Report
how many of the questions you could answer by derivation and how many
you marked NOT ESTABLISHED**, and **say that a dossier with gaps is the
honest form of this deliverable, not a defective one** — **provided the
gaps are named.**

**Third.** **Nothing here establishes that the four candidates are the
complete set.** `P2-LATTICE-ONTOLOGY-01` §347 names four. **Whether a
fifth formulation exists that satisfies the frozen obligations is not
addressed**, and **the ruling that follows will be a choice among the
four this dossier examined.**

**Fourth.** **§3's connection, if it holds, changes how an existing
result reads and changes no number.** The `DEFERRED-02` branch would be
the doubler sector rather than a curiosity. **Say that this is a
reinterpretation conditional on a candidate the programme has not
adopted**, and **that `C1` and `C3`'s measurements are unaffected either
way.**

## 8. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_dpre-a-kinetic-operator-dossier.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_dpre-a-kinetic-operator-dossier.md
    commit 3  derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md
              derivations/P2-DEFERRED-ITEMS.md
    commit 4  reports/2026-08-XXT{HHMM}Z_dpre-a-kinetic-operator-dossier.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **The dossier and the deferred
entry move together in commit 3** — `DEFERRED-04` records the disposition
of a question the dossier frames, and a commit carrying one without the
other would be a partial record.

**Committed report — measured at commit 3:** A1–A13, A15 and A16;
**A14's two runs with both configs verbatim**; commit 1–3 SHAs and stored
messages; commit 4's intended message; **A11's final scope stated as
INTENDED.**

**Post-report evidence, NOT written back:** A11's final scope measured
base-to-commit-4; A14-final; A15 at commit 4; A16 for commit 4; the
push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 9. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, the
  dossier, and an append to `derivations/P2-DEFERRED-ITEMS.md`.
  **Nothing else.**
- **No deletion from `P2-DEFERRED-ITEMS.md`, for any reason.**
- **Do not select a candidate**, in the dossier, the report, or a commit
  message.
- **Do not adjust the config or this specification's declarations to make
  RUN 2 pass.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 10. Report contract

- everything in §8 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A3's four species ledgers, each with the derivation METHOD used and
  why it suits that formulation**, and the count of figures marked NOT
  ESTABLISHED;
- **A4's four reflection-positivity assessments and the count of each
  answer**;
- **A5's sixteen compatibility results**;
- **A6's four consequence statements**, including the complement
  relation;
- **A7's measured definition of `N` and the gap condition, with line
  numbers**, the mapping derived or NOT ESTABLISHED per candidate, and
  **the count of each**;
- **A8's involution derivation**, the conditional association or its
  failure, and its confinement to the Wilson candidate;
- **A9's diff, zero-deletion count, subsequence match, and the four-entry
  confirmation**;
- **A10's search, the finding, and the length of each candidate's
  treatment**;
- **A14's two runs**, both configs verbatim, `declared_source` for each,
  **`P3`'s result for each of the two declared paths**, the section count
  `P7` saw, and the measured RUN 1 subject set;
- **§7's four Rule 16 junctions**;
- **whether assembling the dossier made you want to select a
  candidate.** **Say which and why, and confirm you did not** — **that
  answer is useful to the PI and is not a selection**;
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

    target      the delegation table
    method      read P2-LATTICE-ONTOLOGY-01 §178-192 at ae3604de
    MEASURED    five items delegated to D-pre or MICROSPEC: microscopic
                variables and measure (§185), which fields are summed
                (§188), canonical kinetic operator and species
                accounting (§189), geometry map and curvature estimator
                (§190), reference equivalence class (§191). Four items
                FROZEN there and not delegated: formulation (§180),
                reflection positivity as obligation (§181), isotropy
                (§182), vacuum selection rule (§184).
    DERIVED     almost every delegated item depends on the operator
                choice, which is why §0 says there is no substantial
                choice-independent freeze. This is the author's reading
                of the table, not a statement in it.

    target      the obligation on the operator choice
    method      read P2-LATTICE-ONTOLOGY-01 §352-361
    MEASURED    the (a)/(b) obligation; "(a) is the honest default"
                until (b) is done; and the sequencing note that D-pre
                may be authorized with the obligation open but D0 may
                NOT be authorized until the kinetic operator and its
                species ledger are frozen.

    target      N in the critical coupling
    method      grep for the gap condition in derivations/
    MEASURED    P2-GENERATOR-SUM-CRITICALITY_01 line 145:
                1 = (8/N) G I_0, G_c = N/(8 I_0). N enters directly.

    target      the Wilson term and the complement corner
    method      read WilsonQuadrature at lines 78-86 of the exploratory
                script
    MEASURED    w = mhat + Σ(1 − cos p_μ) over four axes; at p_μ = π in
                all four, Σ(1 − cos) = 8.
    DERIVED     hence Mhat -> −8 − Mhat is the all-π corner. The
                identification is the author's; A8 requires the executor
                to derive it independently.

    target      the deferred register
    method      read its headings and its own rules
    MEASURED    three entries, DEFERRED-01 to -03; the register states
                that entries are added by PI decision. DEFERRED-04 is
                added under §1's ruling, and A9 requires append-only
                verified two ways.

    target      whether P2-DEFERRED-ITEMS.md is pinned
    method      grep 'sha256 `[0-9a-f]{64}`' over GATES.md and read the
                path above each
    MEASURED    TWO pins, naming the adopted parameter-domain artifact
                and the adopted admissibility contract. NEITHER names
                P2-DEFERRED-ITEMS.md. No re-pin is owed; A13 requires
                that verified.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys and values
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations. append_only carries
                TWO paths. A14 checks them against the committed bytes.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                ae3604de and executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 1 modification;
                the manifest lists four and one; parse OK, counted
                equals stated per category.
