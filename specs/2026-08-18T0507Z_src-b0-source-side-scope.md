# Task specification — `SRC-B0`: can this programme ask whether two configurations attract?

Specification evidence base: `0a7a988cb1c1ca7de4cbfebd46fd690245789a2d`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   science/src-b0-source-side-scope
    Cut from           authoritative main — refs/remotes/origin/main

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This task does not touch `main`.** Integration is a separate task.

**IT COMPUTES NOTHING.** It determines whether the calculation the PI
proposed can be posed at all in this repository, and what it would cost.

---

## 0. The question the PI asked

**Every quantity this programme has computed lives on the LEFT side of
the field equation** — `Z`, `β_s`, `G_ind`: the coefficient of
`∫√g R`, the elasticity of spacetime.

**Nothing has been computed on the RIGHT side.** **Measured at this
evidence base: `stress tensor` 0 files, `energy-momentum` 0,
`source term` 0, `Einstein equation` 0, `field equation` 0, `geodesic`
0, `test particle` 0, `Poisson` 0.**

**So the programme has never asked whether two configurations attract.**

**The physics behind the PI's intuition is real and this specification
states it so the task can be scoped against it, and states it
narrowly:**

**A homogeneous Lorentz-invariant vacuum contributes a
cosmological-constant-type stress tensor.** **It does NOT provide a
localized, clustering source of the kind the proposed halo and
rotation-curve test requires.**

**It does not follow that such a vacuum has no gravitational effect.**
**A cosmological-constant stress-energy DOES gravitate — a positive `Λ`
produces de Sitter-type relative acceleration** — **and an earlier draft
of this paragraph wrote "no attraction between two uniform regions",
which conflates "no localized clustering source" with "no gravitational
effect at all".** **The second is false.**

**What provides a clustering source is INHOMOGENEITY**: a condensate
lump differing from the surrounding vacuum.

**The programme has such an object in principle** — Paper 1's halo, a
soliton or domain-wall configuration of the condensate.

> **Could this repository compute that configuration's `T_μν`, feed it
> through this programme's own induced `G`, and compare the resulting
> potential with the one Paper 1 fits to rotation curves?**

**That comparison would be the programme's first two-sided statement.**
**This task determines whether it can be posed, not whether it
succeeds.**

## 1. The first question, and it may end the task

**Measured by the Researcher: the halo configuration is NOT IN THIS
REPOSITORY.** A search over the whole tree for `sparc`, `halo`,
`soliton`, `domain wall`, `yukawa` and `rotation` returned **no files**.

**So the first question is:**

> **Does a condensate configuration exist that this repository can use —
> and if it exists elsewhere, is it DERIVED from the field equations or
> FITTED to rotation curves?**

**This distinction decides whether the calculation is worth doing.**

**If the profile is FITTED to SPARC**, then computing its `T_μν`,
deriving a potential, and finding that potential matches SPARC **is
circular** — the profile was chosen to match SPARC in the first place.
**A task built on a fitted profile would produce a guaranteed apparent
success carrying no information.**

**`FITTED` would be a legitimate eventual finding IF supported by
admissible material.** **But if the configuration is not present in this
repository, this task reports `NOT PRESENT` and MUST NOT infer whether
an external profile is derived or fitted.**

**§3 forbids importing or reconstructing it, and a filename cannot
settle provenance.** **`NOT PRESENT / EXTERNAL STATUS NOT DETERMINED` is
the honest verdict in that case**, and **naming what would have to land
here is the useful part of it.**

## 2. The four further questions

**Two: how would `T_μν` be defined here?** `T_μν = (2/√g) δΓ/δg^{μν}`
requires `Γ`, and **`DET-01` established that the functional measure is
`NOT DETERMINABLE` from the frozen conventions.**

**`DET-01` IS NOW LANDED.** Read its artifact at
`derivations/P2-BETAV-DET-01_measure-adjudication.md` on `main` — **do
not take the rider from this specification.**

**Report whether the ambiguity `DET-01` found affects `T_μν`.** **Its
rider says the ambiguity is ULTRALOCAL and MASS-INDEPENDENT and
therefore does not touch `β_V`** — **but a `Σₓ F(g(x))` term
differentiated with respect to `g` gives something that is NOT
automatically zero.** **That is a different question from the one
`DET-01` answered, and this assessment must not assume the answer
carries over.**

**AND REPORT THE RIDER'S DIMENSIONAL SCOPE.** **Measured: the general
relation is `det[√g g⁻¹] = (det g)^{d/2−1}`, which equals `det g` ONLY
at `d = 4`.** **At `d = 2` it equals `1` — `G1` has no determinant at
all and the rider is empty, not merely coincidental.**

**`RECON-01a`'s construction hard-codes `d = 4`, so the equality is a
property of that construction and not a general identity.** **Report
whether the landed artifact states this qualifier**, and **report your
own measurement of the general relation.**

**Three: which `G` would be used?** **`DET-01` and `RECON-B0` between
them established that the ABSOLUTE `G_ind` is blocked on `R5` and `R1`,
while the RATIO is not.**

**Report whether the comparison can be made DIMENSIONLESS** — a shape
comparison, a scaling relation, a ratio — **so that it does not require
an absolute `G` this programme cannot yet produce.** **If it cannot, say
so: the calculation would then inherit the `R1`/`R5` blockers.**

**Four: where is Paper 1's potential?** **Report whether the fitted
potential, the profile, or the `r_c ∝ V_max^{0.82}` relation exists in
any form this repository can read.** **If it exists only in a manuscript
outside the repository, say so** — **and say what would have to land
here first.**

**Five, and it is the one that decides whether this is a real test:
what would count as FAILURE?**

**Report what a pre-registered failure criterion would have to specify**:
the quantity compared, the tolerance, and the direction. **Do not choose
the tolerance** — that is a PI ruling. **But state what has to be
chosen, because a comparison without a stated tolerance is not a test.**

**A factor-of-three disagreement can be read as "same order of
magnitude, success" or as "wrong by three", and which reading wins is
decided after the number is seen unless the criterion is fixed
first.** **Say that.**

## 3. What this task must not do

- **Do not touch `main`**, do not merge.
- **DO NOT COMPUTE ANYTHING.** No `T_μν`, no potential, no profile, no
  comparison, no order-of-magnitude estimate of any physical quantity.
- **Do not choose a tolerance or a failure criterion.** **State what
  must be chosen.**
- **Do not settle the measure question**, and do not extend `DET-01`'s
  rider to `T_μν` without deriving it.
- **Do not import, reconstruct, or restate Paper 1's profile from
  memory.** **If it is not in this repository, it is not available to
  this task** — **and saying so is the finding.**
- **Do not estimate effort in time.** **Count components.**
- **Do not touch `R1`–`R5`, `RECON-01b`, or the `r = 1` conflict.**
- **Do not add a register entry anywhere.**
- **Do not push any ref but this task's branch.**

## 4. Acceptance criteria

**A1 — Repository, refs, branch availability.** Report the `origin`
remote URL as measured, **verbatim and not normalised**; confirm it
identifies `zetacheng/2-emergent-gravity`, accepting either URL form.
Fetch, then report `refs/remotes/origin/main` and confirm it is
`0a7a988cb1c1ca7de4cbfebd46fd690245789a2d`. **Report `refs/heads/main`
for contrast.**

**Report whether `science/src-b0-source-side-scope` already exists.**
**If it does, STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — Environment conformance, run FIRST.** Rule 13's diagnostic order
including Amendment D's step 0. **Report whether the clone is shallow
and its commit count.**

**A4 — The right-side search, re-run.** **Search the repository for
`stress tensor`, `energy-momentum`, `T_{mu nu}` and its variants,
`source term`, `Einstein equation`, `field equation`, `geodesic`, `test
particle`, `Poisson`, `Newtonian limit`.** **Report each term's file
count and, for any non-zero count, what the hits actually are.**

**The Researcher measured zero for eight of these over `derivations/`
and one file mentioning `Newtonian`.** **Search the WHOLE tree, not just
`derivations/`, and report the difference if there is one.**

**A5 — The configuration search**, per §1. **Search the whole tree for
`sparc`, `halo`, `soliton`, `domain wall`, `yukawa`, `rotation curve`,
`profile`, `r_c`.** **Report each count.**

**Then report the verdict on availability:**

    DERIVED AND PRESENT      a configuration exists here and follows
                             from the field equations. Name it.
    FITTED AND PRESENT       a configuration exists here but was fitted.
                             Say what it was fitted to.
    NOT PRESENT / EXTERNAL   no configuration in this repository. Say
    STATUS NOT DETERMINED    what would have to land, and DO NOT infer
                             whether anything outside is derived or
                             fitted.

**If `FITTED AND PRESENT`, say explicitly that the proposed calculation
cannot be posed non-circularly from that material.**

**If `NOT PRESENT`, say that the proposed source-side calculation cannot
presently be executed from repository materials, and do not characterise
what is outside.**

**THE CALCULATION IS BLOCKED; THIS ASSESSMENT CONTINUES.** **Complete
`A6` through `A17` as a scope and dependency assessment.**

**An earlier draft said to "stop there", which would have halted the
task at its most likely verdict** — **and `§7` would then have required
a stop rather than a choice, because the instruction contradicted the
rest of the contract.** **A `NOT PRESENT` finding makes the remaining
questions MORE useful, not less: they name what would have to exist.**

**A6 — `T_μν`'s definitional dependence**, per §2 question two.
**Report whether defining `T_μν` requires the measure `DET-01` found
unfixed**, and **whether `DET-01`'s ultralocal, mass-independent rider
carries over to `δ/δg` of that term.**

**DERIVE the second part** — **this is symbolic sign-and-structure
work, not the computation of a physical quantity, and §3's prohibition
does not reach it.** **Report `NOT DETERMINED BY THIS TASK` only if the
derivation does not close.**

**Do not assume it carries over.** **The rider was proved for the
`m² ln m²` coefficient of `Z`.** **A functional derivative of
`Σₓ F(g(x))` with respect to `g^{μν}(x)` is a different object and is
NOT generally zero** — **it would give an ultralocal source
contribution.**

**Then report separately, and this is the part that decides whether
`A7` is answerable:**

> **If the ambiguity contributes only an ultralocal, vacuum-like term,
> could an EXPLICITLY DEFINED background-subtracted stress tensor remove
> it from the source observable?**

**Do not assume such a subtraction is already frozen.** **Report whether
any subtraction prescription exists in the repository, and if none does,
report that defining one is a dependency of the proposed
calculation.**

**A7 — Dimensionlessness**, per question three. **Report whether a
comparison exists that avoids the absolute `G_ind`.** **If yes, name
it.** **If no, report that the calculation inherits `R1` and `R5`.**

**A8 — Paper 1's material**, per question four. **Report whether the
potential, the profile or the `r_c` scaling exists in a form this
repository can read.** **If it exists only outside, name what would have
to land here.**

**A9 — The failure criterion's requirements**, per question five.
**Report what a pre-registration would have to fix: the compared
quantity, the tolerance, and the direction.** **Do not choose any of
them.**

**Report explicitly that a comparison without a fixed tolerance is not a
test**, and **that the factor-of-three case is decided after the number
is seen unless fixed first.**

**A10 — The component inventory.** **List the distinct components the
calculation would need**, and classify each into exactly ONE of four
mutually exclusive states:

    1  IMPLEMENTATION + SPECIFICATION
    2  IMPLEMENTATION ONLY
    3  SPECIFICATION ONLY
    4  NEITHER

**Report `N_total = N_both + N_impl + N_spec + N_neither`.** **An
implementation counts only if it is POTENTIALLY APPLICABLE here.**

**A11 — Nothing computed.** **Search the artifact, the report and the
commit messages for any computed physical quantity, any potential, any
profile value, any order-of-magnitude estimate, and any chosen
tolerance.** **Governance measurements, file counts, line numbers, SHAs
and quoted repository values are excluded.** **Report the search and the
result.**

**A12 — Scope, frozen manifest.**

    stated: 4 additions, 0 modifications
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: 0a7a988cb1c1ca7de4cbfebd46fd690245789a2d
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-SRC-B0_source-side-scope.md
      reports/2026-08-XXT{HHMM}Z_src-b0-source-side-scope.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_src-b0-source-side-scope.md
      specs/2026-08-XXT{HHMM}Z_src-b0-source-side-scope.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths.** **Report the cumulative figure at each commit and the
contributions separately.**

**`append_only: DECISION_LOG.md` is a checker-configuration declaration,
NOT an authorisation to write that file.** **Measure the UTC time and use
the value you measured.**

**A13 — Nothing existing changed.** Every path at the evidence base
blob-identical at the head. **Report the count compared**, and confirm
explicitly for `GATES.md`, `CONVENTIONS.md`, **every
`derivations/P2-BETAV-*` artifact — re-measure the count**, all seven
microspec artifacts, the two `scripts/recon2026/` files and
`tests/test_recon2026_flat_limit.py`, both registers, and everything
under `results/`.

**A14 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites `SATISFIED`;
both pins match. **Report all four, read SCOPED.**

**A15 — The checker over this task's own range**, base `0a7a988c…`, head
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

**A15-final, post-report evidence:** re-run RUN 2 at commit 4.

**A16 — Validators, exit status 0.** **Expected 332 passed, 2
deselected.**

**A17 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 5. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_src-b0-source-side-scope.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_src-b0-source-side-scope.md
    commit 3  derivations/P2-SRC-B0_source-side-scope.md
    commit 4  reports/2026-08-XXT{HHMM}Z_src-b0-source-side-scope.md

**Committed report — measured at commit 3:** A1–A14, A16 and A17;
**A15's two runs with both configs verbatim**; commit 1–3 SHAs and
stored messages; commit 4's intended message; **A12's final scope stated
as INTENDED.**

**Post-report evidence, NOT written back:** A12's final scope measured
base-to-commit-4; A15-final; A16 at commit 4; A17 for commit 4; the
push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 6. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Five junctions, all five required in the report.**

**First.** **A `NOT PRESENT` or `FITTED ONLY` verdict does not mean the
physics is wrong.** **It means the calculation cannot be posed
non-circularly from what is here.** **Say that**, and **say what would
change it.**

**Second.** **This assessment is bounded by this repository.** **Paper 1
is a separate repository and a manuscript.** **A configuration existing
there is not a configuration available here**, and **whether it is
derived or fitted cannot be settled from a filename.** **Say what you
could and could not determine.**

**Third.** **The PI's question — do two ground-state configurations
attract — is not the same as the question this programme has been
answering.** **The programme computes the coefficient of `∫√g R`; the
PI asked for a solution with a source.** **Say that both are legitimate
and that only the first has been attempted.**

**Fourth.** **A homogeneous Lorentz-invariant vacuum contributes a
cosmological-constant-type stress tensor.** **It does not provide the
localized, clustering source the proposed test requires** — **and that
is NOT the same as having no gravitational effect, which would be
false.**

**Say that the proposed calculation therefore probes the condensate's
INHOMOGENEOUS sector**, and **that a null result there would say nothing
about the vacuum sector, which `DET-01` left unfixed.**

**Fifth.** **A component count is not a difficulty**, and **an
assessment that finds the calculation posable has not made it likely to
succeed.**

## 7. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  scope artifact. **Nothing else, at all.**
- **No file existing at the evidence base may be modified.**
- **Compute nothing, choose no tolerance, import no external profile.**
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

## 8. Report contract

- everything in §5 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A1's verbatim `origin` URL and the branch-availability check**;
- **A3's environment diagnosis in Rule 13's order, run FIRST**;
- **A4's ten search counts over the whole tree, with the hits named**;
- **A5's eight counts and the availability verdict, with the
  non-circularity statement**;
- **A6's finding in FOUR parts**: whether `T_μν` needs the unfixed
  measure; the functional derivative of the ultralocal term, DERIVED;
  whether a background-subtracted stress tensor could remove it, with
  any existing subtraction prescription named or its absence reported;
  and **the rider's dimensional scope, with the general
  `(det g)^{d/2−1}` relation measured and the `d = 2` case reported**;
- **A7's dimensionlessness finding**;
- **A8's Paper 1 material finding**;
- **A9's list of what a pre-registration must fix, with nothing
  chosen**;
- **A10's four counts and their sum**;
- **A11's search and result**;
- **A12's cumulative figures and contributions, separately labelled**;
- **A13's path count with the `P2-BETAV-*` count re-measured**;
- **A14's four invariants**;
- **A15's two runs**, both configs verbatim, the section count `P7` saw,
  what `RUN 1` did, and confirmation the output was parsed not grepped;
- **A16's counts**;
- **§6's five Rule 16 junctions**;
- **whether assessing made you want to compute a potential, estimate an
  order of magnitude, or reconstruct a profile from memory.** **Say
  which and why, and confirm you did not** — **this is the first task in
  this line whose subject is a number the PI has been asking about all
  session**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 9. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      the right-hand side of the field equation
    method      git grep -ci over derivations/ for six terms
    MEASURED    stress tensor 0 files, T_{mu nu} 0, energy-momentum 0,
                source term 0, Einstein equation 0, field equation 0.
                Separately: geodesic 0, test particle 0, Poisson 0,
                potential well 0, Newtonian 1, two-body 2, attract 10.
                A4 requires the search re-run over the WHOLE TREE, since
                this author searched derivations/ only.

    target      whether a condensate configuration exists here
    method      git ls-tree over the whole tree at the evidence base,
                filtered for sparc, halo, soliton, domain wall, yukawa,
                rotation
    MEASURED    NO FILES MATCH. The halo configuration is not in this
                repository under any of those names.
    NOT DETERMINED whether it exists elsewhere, and whether it is derived
                or fitted. A5 requires the search widened and the
                verdict stated.

    target      the geometry map
    method      read P2-LATTICE-ONTOLOGY-01 lines 134 and 190
    MEASURED    :190 records the map {t_ij} <-> g, e, ω as DELEGATED to
                D-pre; :134 says the lattice degrees of freedom
                corresponding to the metric are "still to be
                identified". The metric used in RECON-01a is an input,
                not an emergent quantity.
    RELEVANCE   this bears on §6's third junction and is stated there;
                it is not itself a criterion of this task.

    target      DET-01's rider, now landed
    method      git cat-file -e on
                derivations/P2-BETAV-DET-01_measure-adjudication.md at
                the new evidence base
    MEASURED    PRESENT. The artifact states at :24 and :302 that det G1
                is ultralocal in the background and independent of the
                mass. It mentions a four-dimensional qualifier once.
    NOT DERIVED by this author whether δ/δg of an ultralocal term
                vanishes. A6 requires it derived or reported
                undetermined.

    target      the rider's dimensional scope
    method      form √(det g)·g⁻¹ for random symmetric positive-definite
                g in d = 2, 3, 4, 5 and compare determinants
    MEASURED    det[√g g⁻¹] = (det g)^{d/2−1} in every case. It equals
                det g ONLY at d = 4. At d = 2 it equals 1 — G1 carries
                no determinant, and the rider is EMPTY there rather than
                approximately true. The DET-01 integration executor
                reported the same and this author confirms it
                independently.

    target      the P2-BETAV-* count at the new base
    method      git ls-tree over derivations/
    MEASURED    EIGHT. It was seven at the previous base; the DET-01
                landing added one. A13 requires it re-measured, not
                carried.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 4 additions, 0 modifications;
                parse OK, counted equals stated per category.
