# `P2-POLE-B0` — what the manuscript's own decisive test would require

    STATUS      SCOPE AND TRACTABILITY ASSESSMENT. NOTHING IS COMPUTED HERE.
    BASE        11af14a792c5858b368180d99ab9ee4692a7f698
    VERDICT     REQUIRES A CONSTRUCTION NOT YET SCOPED
                with TRACTABLE BUT BLOCKED PENDING A RULING applying in part

**This artifact determines what the manuscript's named milestone would
require and what already exists.** It computes no correlator, no projection,
no pole and no residue; it estimates none of them and bounds none of them. It
chooses no tolerance, no volume and no mass. It ranks no task against any
other. Where a number appears it is either a count of repository objects or a
value quoted from a repository file with its line — never a value produced
here.

---

## 1. The passage, and the two statements inside it

**MEASURED verbatim at the evidence base,
`paper/emergent_gr_paper_v2_15.tex`:**

    :805  We also state plainly the strongest form of the dynamical claim:
    :806  that the interacting lattice theory possesses a genuine massless
    :807  spin-2 \emph{pole} in $\langle TT \rangle$ (rather than merely an
    :808  induced kinetic term for an external field) is supported by the
    :809  Ward structure above but is ultimately a nonperturbative question.
    :810  A lattice measurement of the Barnes--Rivers--projected
    :811  stress-tensor correlator, checking for a single $p^2 = 0$ pole in
    :812  the spin-2 sector with vanishing spin-1/0 residues, is the decisive
    :813  test; we identify it as the key numerical milestone for this
    :814  programme.

**Two statements are made there and they are not the same statement.**

### 1.1 An induced kinetic term is not a pole

`:807-808` draws the distinction explicitly: *"a genuine massless spin-2
pole in ⟨TT⟩"* **as against** *"merely an induced kinetic term for an
external field"*.

**These are different objects and the difference is not one of precision.**
An induced kinetic term is a coefficient in an effective action for a field
supplied from outside the theory. A pole in `⟨TT⟩` is a statement that the
interacting theory contains a propagating state. The first can be nonzero,
correct, and beautifully isotropic in a theory with no graviton in its
spectrum at all.

**Everything this programme has computed on the graviton side is the first.**
`Z` is defined at `CONVENTIONS.md:20` as the coefficient of the induced
Einstein–Hilbert term `∫√g R`. `scripts/recovered_2026/tt_check.py` states its
own object at `:7`: *"Euclidean quadratic effective kernel: Gamma^(2) = N *
B(q) (per species)"*, and its deliverables at `:9-15` are the isotropy of the
`q²` coefficient, the sign and size of `Z_h = dG2/dq²`, and a dim-6
anisotropy. `RECON-01a` builds `D1[g,h]` and `D0[g,h]` — operators for
**bosonic** fields on a **prescribed external** metric background, per
`P2-BETAV-RECON-01a_construction-and-flat-validation.md:19-23`.

**A 1PI kernel and a propagator are not the same object, and their
singularities are not in the same places.** A pole of the propagator sits at
a **zero** of the kernel. `Γ^(2)(q)` having a clean `q²` coefficient is a
statement about the kernel's low-momentum expansion; it is not a statement
that the inverse kernel has a pole at `p² = 0` in the interacting theory.

### 1.2 The manuscript calls the question nonperturbative

`:808-809` says the claim *"is supported by the Ward structure above but is
ultimately a nonperturbative question."*

**So this is not a gap the programme overlooked. It is one the manuscript
identifies, characterises, and defers.** The word *supported* is doing exact
work there: a Ward identity constrains the form a kernel may take; it does
not populate a spectrum.

**Every graviton-channel computation in this repository is perturbative.**
`tt_check.py:1-7` is a one-loop bubble, `B_{μν,ρσ}(q) = mean_k tr[V S V S]`,
evaluated over a momentum grid at fixed `m` and `r`. The manuscript's own
characterisation places the milestone outside what that method can answer.

### 1.3 Has the test been performed, attempted, or scheduled?

**Searched over the manuscript. Reported as measured.**

    we have measured       0        in progress            0
    we measured            0        underway               0
    we performed           0        forthcoming            0
    has been performed     0        we defer               0
    we report the          0        remains to be          0

    scheduled              1        future work            3
    left open              1        not yet                1

**Every non-zero hit was opened and none of them is this milestone.**

- `:395` *"It is therefore scheduled for re-audit under the corrected
  convention"* — a pair decomposition, not the pole test.
- `:446`, `:448` — *"connections (future work)"*, *"Torsion / Kalb–Ramond
  sector (future work)"*, both other sectors.
- `:642` — the coupling of the angular mode to matter, deferred to future work.
- `:544` — `ε`, *"left open in Section~\ref{sec:angular}"*.
- `:1257` — *"the vector channel, whose universal mass-logarithmic
  coefficient has a different spin structure and is not yet computed"*.

**The manuscript nowhere states that the decisive test has been performed,
attempted, or scheduled.** It states the test, designates it the key numerical
milestone, and stops.

---

## 2. What already exists, classified

### 2.1 The counts, and a substring hazard that the counts conceal

**MEASURED over the whole tree with `git grep -lil`, at commit 2 of this
task.** Two figures are given for each term because **this task's own
specification and review are in the tree and contain every one of these
terms.** A search that must name its own patterns matches them.

    TERM                      TOTAL   THIS TASK'S OWN   EXCLUDING OWN
    Barnes                        9          2                7
    Rivers                       14          2               12
    projector                    56          2               54
    stress-tensor correlator     10          2                8
    pole                         69          2               67
    spin projector                1          1                0

**Excluding this task's own two files, every count reproduces the
Researcher's figure exactly.** `spin projector` at zero is the sharpest case:
the single hit in the tree is this specification's own line stating that the
count is zero.

**These are FILE COUNTS. They are not machinery.** The rest of this section is
what the hits actually are.

### 2.2 `Rivers` — five of twelve are the word `drivers`

**MEASURED per file, comparing the count of `rivers` against the count of
`drivers`:**

    SUBSTRING-ONLY — every occurrence is inside "drivers"
      GATES.md                                            2
      derivations/P2-BETAV-RECON-01_scope-assessment.md   2
      reports/2026-08-17T1105Z_recon-b0-scope.md          1
      scripts/P2-BETAV-CAMPAIGN/harness_compute.py        1
      scripts/recovered_2026/PROVENANCE.md                1

    GENUINE — at least one "Barnes--Rivers"
      derivations/P2-CHANNEL-B0_spin-channel-scope.md
      paper/emergent_gr_paper_v2_15.tex
      reports/2026-08-18T2219Z_channel-b0-spin-scope.md
      reports/2026-08-19T0138Z_integrate-channel-b0.md
      results/recovered-2026/emergent_gr_paper_v2_7.tex
      scripts/recovered_2026/tt_check.py
      specs/2026-08-19T0138Z_integrate-channel-b0.md

**Five of the twelve `Rivers` files are the historical β-extraction
`drivers`** that `GATES.md:415` and `:681` warn about — an entirely unrelated
object. **The seven genuine files are exactly the seven `Barnes` files.**

This is the same failure mode `CHANNEL-B0` recorded for
`composition`/`decomposition`. It is recorded here because it recurred, in a
different pair of words, in the same repository, within one task of the first
instance.

### 2.3 `pole` — twenty-four of sixty-seven are `tadpole`

**MEASURED the same way, over the whole tree:**

    files where every "pole" is inside "tadpole"        24
    files with at least one non-tadpole "pole"          43

**In code the ratio is worse.** Of the ten `.py` files matching `pole`:

    TADPOLE-ONLY   betav_assembly.py (8), lattice_beta_scan.py (2),
                   p2_generator_sum_criticality.py (1),
                   recovered_2026/batch2/calibrate.py (1),
                   recovered_2026/batch2/overlap_phase1.py (1),
                   recovered_2026/seagull_check.py (4)

    GENUINE        p2_channel_character_layers.py:462  — prose, and it is a
                     DISCLAIMER: "channel-character label is not a
                     bound-state or pole …"
                   p2_chirality_census.py:508          — prose, same form
                   p2_diquark_both_eta.py:768          — prose, same form
                   recovered_2026/batch2/ep_test.py:43 — a FREE-FERMION
                     DISPERSION pole, "free anisotropic Wilson fermion
                     speed^2 at p->0 from pole dispersion"

**Six of the ten are `tadpole`. Three of the remaining four are prose saying
that something is NOT a pole. The tenth is a single-particle dispersion
relation for a free fermion**, which is a different object from a singularity
of an interacting two-point function.

**`residue` in code returns exactly one file:**
`scripts/recovered_2026/speed_check.py:89`, *"omega integral done analytically
by residues"* — a contour-integration remark.

**No implementation in this repository extracts a pole or a residue from a
correlator.**

### 2.4 `projector` at fifty-four files — and the distinction the count hides

**MEASURED, the fifty-four files by directory:**

    reports 9   specs 8   derivations 8   scripts 6   scripts/recovered_2026 5
    tests 4     reviews/chatgpt 4   scripts/recon2026 2
    results/recovered-2026 2   scripts/P2-CHANNEL-FREEZE 1
    results/P2-PHASE-01/… 2   results/P2-CHANNEL-FREEZE/… 1
    paper 1     GATES.md 1

**Eighteen are `.py` files.** Of those, three distinct objects appear, and the
word `projector` names all three.

**OBJECT A — the full Barnes–Rivers set. ONE implementation, one file.**
`scripts/recovered_2026/tt_check.py:105-126`:

> `def projectors(q):`
> `    """Barnes-Rivers projectors for Euclidean momentum q (4-vector)."""`

It builds `P2`, `P1`, `P0s`, `P0w` from `θ_{μν} = δ_{μν} − q_μ q_ν/q²` and
`ω_{μν} = q_μ q_ν/q²`, and `project()` at `:129-135` returns all four
contractions `g2, g1, g0s, g0w`.

**OBJECT B — the spin-2 projector ALONE, and it is a different function with
the same name.** `scripts/recovered_2026/seagull_check.py:241-253` also
defines `def projectors(q)`, but it returns **`P2` only**. Its `P2` is
algebraically the same tensor as `tt_check.py`'s, and `structure_decomp.py:16`
and `boson_loop.py:23` import it.

**The consequence is exact and is the reason the distinction matters here:
every file that imports `seagull_check.projectors` can project onto spin-2 and
CANNOT measure a spin-1 or spin-0 residue, because it never receives `P1`,
`P0s` or `P0w`.**

**OBJECT C — a longitudinal projector, unrelated.**
`scripts/recon2026/proca_curved.py:332`, `longitudinal_projector_flat` — a
rank-1 projector onto the flat longitudinal direction at a given momentum,
used by `flat_validation.py:143-176` for the Proca gauge-mode check. It is not
a spin decomposition.

**So: `projector` at 54 files resolves to exactly ONE implementation of the
object this milestone names, and it lives in one file.**

### 2.5 The one implementation computes the four channels and discards three

**MEASURED, `tt_check.py:152-155`:**

    G2[name] = np.array([project(tt_bubble(pf(e), n, m, r,
                                           wilson_vertex), pf(e))[0]
                         for e in eps])

**`project()` returns `(g2, g1, g0s, g0w)` and the caller takes `[0]`.** The
spin-1 and both spin-0 channels are computed on every call and thrown away.
`run()` at `:156-177` then fits `G2` in `ε` and reports `Z_h`, an isotropy
ratio, and a dim-6 anisotropy.

**The repository therefore contains the projectors the milestone needs and no
use of them for the milestone's question.** The single existing consumer uses
the one channel the milestone is not asking about, and the manuscript's
criterion — *vanishing spin-1/0 residues* — is precisely a statement about the
three channels that code discards.

---

## 3. Is `⟨TT⟩` reachable from what `RECON-01a` landed?

### 3.1 What `RECON-01a` landed

`derivations/P2-BETAV-RECON-01a_construction-and-flat-validation.md:19-23`
records the deliverables:

> `D1[g,h]` metric-coupled 1-form operator, from the covariant field-strength
> action with exact geometric factors
> `D0[g,h]` metric-coupled compensating scalar, from the covariant Dirichlet
> action

with `scripts/recon2026/proca_curved.py:356` supplying `logdet_operator`, and
`flat_validation.py` validating the flat limit.

**MEASURED: `fermion`, `Dirac` and `stress` return ZERO lines in the
`RECON-01a` artifact.** The construction is bosonic throughout — a 1-form and
a compensating scalar. **The fermionic stress tensor is not in it.**

### 3.2 The formal route exists, and it lands on the object the manuscript
excludes

There is a route in principle. `Γ = ½ log det` is what `logdet_operator`
computes; a stress tensor may be defined as `T^{μν} = (2/√g) δΓ/δg_{μν}`; and
a second metric variation of the same functional produces a two-index-pair
object.

**That object is `Γ^(2)`, the 1PI kernel for an external metric — which is
`:807-808`'s "induced kinetic term for an external field", by name.** It is
not the connected correlator of the fermionic stress-tensor operator in an
interacting state. Reaching the milestone's object by this route would require
inverting the kernel, and the inversion is where a pole would live, and the
inversion is not performed anywhere in this repository.

**And the route inherits `DET-01`.** `derivations/P2-SRC-B0_source-side-scope.md:186-192`
records the finding: *"`Γ = ½ log det K − ½ log det 𝔊` with `𝔊` unspecified.
So a stress tensor defined from the full quantum effective action inherits the
unfixed measure."*

**Answer to question three, first half: `⟨TT⟩` as the manuscript defines it is
NOT reachable from what `RECON-01a` landed.** What is reachable is a bosonic
induced kernel for an external background — the object the milestone's own
sentence sets aside.

### 3.3 Does `SRC-B0`'s absent source side transfer? — answered explicitly

**It does not transfer as an entailment, and it does partially transfer
through a shared dependency. Both halves are needed and they are different
statements.**

**Why it does not transfer.** `SRC-B0` returned `NOT PRESENT / EXTERNAL STATUS
NOT DETERMINED` about **a configuration** — a lump of matter whose field one
would compute in order to ask whether two such lumps attract. `⟨T T⟩` is a
**vacuum or ensemble two-point function of an operator**. It needs no
configuration at all: it needs an operator, a state, and a measure. **A
correlator of stress tensors and a stress tensor sourcing a field are
different objects, and the absence of the second does not imply the absence of
the first.** This assessment does not infer unavailability from `SRC-B0`.

**Where it does bear.** `SRC-B0` §4.1 established a conditional that applies
here verbatim:

    Γ-DEFINED  T_μν = (2/√g) δΓ/δg^{μν}     REQUIRES the unfixed measure
    S-DEFINED  T_μν = (2/√g) δS/δg^{μν}     DOES NOT

**The manuscript's `T^{μν}` is S-defined.** `:673-675` gives it as a bilinear
operator built from the classical action:

    T^{\mu\nu} = \frac{i}{4}\,\bar{\psi}\gamma^{(\mu}
    \!\overleftrightarrow{\partial}{}^{\nu)}\psi + \mathrm{h.c.}
    - \eta^{\mu\nu}\mathcal{L}

**So the OPERATOR does not need the measure.** But `⟨ · ⟩` does. **The
milestone's object is not `T^{μν}`; it is the expectation value of a product
of two of them, and an expectation value is measure-weighted by definition.**
The dependency enters through the bracket, not through the operator — a
different route from `SRC-B0`'s, reaching the same open node. §4.4 states this
as the `R4` finding.

---

## 4. Dependence on `R1`–`R5`

**Per node, one of `INDEPENDENT`, `DEPENDENCE ESTABLISHED`, `DEPENDENCE NOT
ESTABLISHED`. Silence is not independence.** Node definitions are quoted from
`derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md`; all five carry
`STATUS OPEN` there.

    R1  the canonical kinetic operator and its parameters   DEPENDENCE ESTABLISHED
    R2  the admissible lattice extent and finite-volume rules DEPENDENCE ESTABLISHED
    R3  boundary conditions, the temporal one in particular  DEPENDENCE ESTABLISHED
    R4  the microscopic variables, state space and measure   DEPENDENCE ESTABLISHED
    R5  the internal multiplicity N                          DEPENDENCE NOT ESTABLISHED

**This assessment adjudicates none of them.** Each is reported as a dependency
of the observable, not as a ruling on the node.

### 4.1 `R1` — DEPENDENCE ESTABLISHED

`R1`'s `NODE` is *"which lattice Dirac operator is canonical, and the
parameter values that come with the choice"*, with `CONTROLS W8 the Wilson
parameter r`.

**The dependence is established two ways, both from repository text.**

**Through the operator.** `T^{μν}` at `:673-675` is a derivative fermion
bilinear. Its lattice realisation is a discretisation of `∂^ν` against a
specific Dirac operator, and the propagators `S(k)` and `S(k+q)` in any
evaluation are that operator's propagators. `tt_check.py:17-24` makes the
choice explicit and declares it: a sine-improved `γ` vertex plus an **optional**
Wilson part carrying `r`, with `:12-13` recording that the script tests
*"prescription sensitivity by switching the Wilson-term vertex on/off"*. **A
computation that reports its own sensitivity to a prescription is a
computation that depends on the ruling that would fix the prescription.**

**Through reflection positivity.** `P2-LATTICE-ONTOLOGY-01.md:75-80` requires
Osterwalder–Schrader reflection positivity to be *"proved per declared kinetic
operator"*. §5.3 below explains why the milestone's interpretation needs it.

### 4.2 `R2` — DEPENDENCE ESTABLISHED

`R2`'s `NODE` is *"what lattice extent and finite-volume regime the programme
admits"*; `P2-LATTICE-ROUTE-01.md:192-193` lists *"finite-volume and
thermodynamic rules"* among what must be frozen.

**The criterion is a massless pole — `p² = 0` exactly.** On a finite periodic
lattice the momenta are discrete and `p² = 0` is a single point. Establishing
that a singularity sits **at** zero rather than near it is a statement about a
limit, and the repository names the requirement for the structurally
analogous case: `P2-LATTICE-ROUTE-01.md:294-295` requires *"finite-volume pole
extraction"* for a `⟨J J⟩` cross-check. **The same requirement applies to
`⟨T T⟩` for the same reason.**

### 4.3 `R3` — DEPENDENCE ESTABLISHED

`R3`'s `NODE` is *"which boundary conditions the programme adopts, temporal
above all"*.

`P2-LATTICE-ROUTE-01.md:201-203` names, among the content of a blocking
deliverable, *"transfer-matrix normalization; geometry-dependent measure and
Jacobian factors; finite temporal extent; temporal boundary conditions"*. **A
two-point function's spectral decomposition is taken along the temporal
direction and its content depends on the temporal boundary condition; the
repository names that dependency in the one place it discusses reconstructing
spectral information.**

### 4.4 `R4` — the measure, in its own paragraph

`R4`'s `NODE` is stated in three words at
`P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md:138`: *"what the microscopic
measure is"*. `STATUS OPEN`.

**`DEPENDENCE ESTABLISHED`, and the route is the bracket.**

`⟨ T T ⟩` is by construction a measure-weighted expectation. Whatever
`T^{μν}` is — and §3.3 established that the manuscript's `T^{μν}` is
S-defined and therefore needs no measure of its own — the angle brackets are
an integral against a measure, and `DET-01` established that the functional
measure is `NOT DETERMINABLE` from the frozen conventions.

**The distinction from `SRC-B0` is worth stating precisely, because the two
assessments reach the same node by different roads.** `SRC-B0` asked whether a
stress tensor needs the measure and answered *conditionally* — the Γ-defined
one does, the S-defined one does not. **That conditional does not rescue this
milestone**, because the milestone does not ask for a stress tensor. It asks
for a **correlation function of two of them**, and the correlation is where
the measure enters. **An S-defined operator inserted into an undefined measure
yields an undefined number.**

**This is the finding §7's fifth Rule 16 junction anticipated.** The
`βV`/heat-kernel line inherits the unfixed measure through `Γ`. The source
side inherits it conditionally, through the choice of which `T` a calculation
uses. **This milestone inherits it unconditionally, through `⟨·⟩`.** Nothing
here rules on `R4`, and nothing here says the measure cannot be fixed. It says
that this observable does not route around it.

### 4.5 `R5` — DEPENDENCE NOT ESTABLISHED

`R5`'s `NODE` is *"what value, or what restriction, the programme fixes for
N"*, `CONTROLS f7 s7`, `STATUS OPEN`.

**The repository contains one relevant statement and it is not enough to
settle the question either way.** `tt_check.py:7` writes `Γ^(2) = N * B(q)`
and `:26` records *"N = 1 (overall N trivial)"* — an overall factor on a
one-loop kernel.

**That is a statement about a perturbative kernel, not about the interacting
correlator this milestone names**, and this assessment does not extend it by
argument. **`DEPENDENCE NOT ESTABLISHED` is reported, and it is not
`INDEPENDENT`.** The repository is silent on whether the interacting
correlator's spin-channel structure depends on `N`, and silence is not
independence.

---

## 5. The component inventory

**Four mutually exclusive states, as in `RECON-B0`.** An implementation counts
only if it is **potentially applicable to this test**; existence is not
availability, and applicability is stated for each.

    N_total = N_both + N_impl + N_spec + N_neither
       12   =    0   +   3    +   3    +    6

### 5.1 `BOTH` — implementation and specification. **ZERO.**

**No component of this test has both.** That is the inventory's governing
number and it is reported first for that reason.

### 5.2 `IMPL` — an applicable implementation exists, no specification freezes it

**C1. A lattice stress-tensor operator `T^{μν}`.**
Implementation: `tt_check.py:17-24`, a declared vertex prescription
`V^g + V^W`. **Applicable:** yes — it is a lattice EMT vertex for Wilson
fermions, the same species the milestone concerns.
Specification: none. `P2-LATTICE-ROUTE-01.md:189-190` lists the canonical
Dirac operator among what must be frozen and the ledger records `R1` as
`OPEN`. The script's prescription is **declared by the script**, not frozen by
the repository — `tt_check.py:17` says *"Vertex prescription (declared)"*.

**C2. Barnes–Rivers projectors, all four.**
Implementation: `tt_check.py:105-126`. **Applicable:** yes — Euclidean, `d=4`,
the exact four-projector set.
Specification: none. `Barnes` returns zero in `GATES.md`. It appears in one
other `specs/` file — `specs/2026-08-19T0138Z_integrate-channel-b0.md`, which
quotes the manuscript's milestone sentence — and that is a quotation, not a
freeze.

**C3. Projection of a rank-4 object onto the four spin channels.**
Implementation: `tt_check.py:129-135`, returning `g2, g1, g0s, g0w`.
**Applicable:** yes, with the qualification recorded in §2.5 — the only
existing caller discards three of the four returns.
Specification: none.

### 5.3 `SPEC` — a specification exists, no implementation

**C4. The method for identifying a pole.**
Specification: `P2-FIERZSUM-01.md:250-252` fixes it — spectral structures are
*"identified from eigenvalue singularities of `G`, or equivalently determinant
zeros of its inverse kernel; not poles alone."*
`P2-LATTICE-ROUTE-01.md:294-295` names the components for the analogous
`⟨J J⟩` case: *"spectral reconstruction or transfer-matrix analysis,
finite-volume pole extraction, and residue/overlap study."*
Implementation: none — §2.3.
**Qualification, stated because it matters:** both passages were written for
`P2-VECPOLE-01`, the vector channel. `FIERZSUM-01 §5`'s doctrine is stated
generally and governs any spectral claim; `ROUTE-01`'s list is explicitly a
`⟨J J⟩` list. **Neither was written for `⟨T T⟩`, and this artifact does not
transplant them; it records that the repository has specified this class of
component once, for a different correlator.**

**C5. Residue / spectral-weight extraction.**
Specification: `FIERZSUM-01:247-250` — *"poles, resonances and branch cuts,
together with their operator-dependent spectral weights"*, with the warning at
`:249-250` that *"the weights describe operator overlap with those structures;
they are not themselves states"*.
Implementation: none — `residue` returns one `.py` file and it is a contour
remark.
Same qualification as C4.

**C6. Osterwalder–Schrader reflection positivity, for a spectral reading.**
Specification: `P2-LATTICE-ONTOLOGY-01.md:70-80` freezes the obligation and
separates the three propositions — `(i)` positivity of a particular finite
transfer matrix, `(ii)` OS reflection positivity of the Euclidean
measure/action, `(iii)` axis equivalence — and states that `(ii)` *"must be
proved per declared kinetic operator, and cannot be transplanted from a
bosonic Ising example"*.
Implementation: none. `P2-LATTICE-MICROSPEC-01_tm-rp-scope.md:3` opens *"THIS
ARTIFACT CONSTRUCTS NOTHING. No transfer matrix, no reflection-positivity
proof, no spectral equivalence"*, and `:99` records *"The repository state is
`NOT ESTABLISHED` for all four"* candidate fermion theories.

**Why this is a component of THIS test and not general background.** The
milestone's word is **pole** — a claim about a propagating state. A
singularity of a Euclidean correlator is a physical state only under
reconstruction, and `ONTOLOGY-01:68` names Osterwalder–Schrader as the
reconstruction in force. **Without `(ii)`, a singularity found in `⟨TT⟩`
would be a feature of a Euclidean function, and the step from there to "the
theory has a massless graviton" is the step `(ii)` licenses.**

### 5.4 `NEITHER` — no implementation, no specification

**C7. A definition of `⟨·⟩` — the microscopic measure and state.**
`R4` is `OPEN`; `DET-01` returned `NOT DETERMINABLE`. In code: `monte` 0,
`ensemble` 0, `importance sampling` 0, `HMC` 0, `thermaliz` 0, `jackknife` 0,
`bootstrap` 0, `gauge configuration` 0, `path integral measure` 0 — **all zero
`.py` files.**

**C8. An evaluation of `⟨TT⟩` beyond one loop.**
The manuscript calls the question nonperturbative at `:809`. The only existing
evaluation is a one-loop bubble. **Nothing in the repository evaluates any
correlator nonperturbatively**, and no specification says how this one would
be.

**C9. A preregistered operator basis for the tensor sector.**
`FIERZSUM-01:239-243` requires *"the full connected matrix over a
preregistered operator basis, complete within the declared symmetry sector and
truncation order"*, and `:257-259` warns that *"Individual projected
correlators supply operator-dependent spectral weights and may miss states to
which the chosen current has zero overlap."*
**The milestone as `:810-814` states it is a single projected correlator built
from one operator.** No tensor-sector operator basis is preregistered
anywhere. `FIERZSUM-01:261-266` forbids borrowing one: *"Three bases must be
kept separate: interaction basis, source/operator basis, physical-state
basis"* — so `P2-CHANNEL-FREEZE-01`'s frozen HS/Fierz **interaction** basis is
not this.

**C10. Finite-volume rules and the massless limit.** `R2` is `OPEN`;
no implementation. `tt_check.py` varies `n ∈ {12, 16, 20}` at `:186-197`, but
that is grid convergence of a momentum sum, not a finite-volume spectrum
study, and it is not applicable.

**C11. The numerical meaning of "vanishing".** §6.

**C12. An artefact-versus-physics discriminator.** §6.

---

## 6. What a pre-registration would have to fix

**Per question five. This section names what must be chosen. IT CHOOSES
NOTHING.** No tolerance, no volume, no mass, no window, no threshold appears
below, and none is implied.

**The manuscript's criterion is `:811-812`** — *"a single `p² = 0` pole in the
spin-2 sector with vanishing spin-1/0 residues"*. **Three of those words are
not operational on a finite lattice as they stand.**

**One — what "vanishing" means.** A measured residue on a finite lattice is a
number with an uncertainty; it is never identically zero. A pre-registration
must fix **which** of these the criterion is, because they are different
tests and can disagree:
- a **tolerance** — `|R_{1,0}| < τ` for a stated `τ`;
- a **ratio** — `|R_{1,0}| / |R_2| < τ`, which is scale-free where the first
  is not;
- a **scaling rule** — `R_{1,0} → 0` as the continuum or infinite-volume limit
  is approached, at a stated rate;
- a **significance statement** — consistency with zero within a stated
  multiple of the estimated uncertainty.
**Which of the four, and the value of `τ` or the rate, must be fixed in
advance.** Neither is fixed here.

**Two — "a single `p² = 0` pole".** *Single* requires a rule for what counts as
one structure rather than two nearby ones, and `FIERZSUM-01:247` records that
the spectral content includes *"poles, resonances and branch cuts"* — so a
rule distinguishing a pole from a cut is required as well. *`p² = 0`* requires
a rule for how close to zero counts as at zero, on a lattice whose momenta are
discrete. **Both must be pre-registered.**

**Three — volumes and masses.** The extraction needs a stated set of lattice
extents and a stated set of fermion masses, together with the order of limits:
**whether the massless limit is taken before or after the infinite-volume
limit changes what is measured**, and the pre-registration must say which.
`R2` is the open node that would fix the admissible extents. **This artifact
states neither a volume nor a mass.**

**Four — the artefact-versus-physics discriminator.** A non-vanishing spin-0
or spin-1 residue can arise from at least these sources, and a
pre-registration must state how each is excluded before a non-zero residue is
read as physics:
- **contact and seagull terms** — `tt_check.py:12-13` already defers them,
  *"contact/seagull terms deferred"*, and `seagull_check.py:21` records that
  *"seagull tadpole is exactly q-independent"*, which is a statement about one
  such term and not a treatment of all of them;
- **the Wilson term's explicit symmetry breaking** — the same script tests
  prescription sensitivity by switching that vertex off, so the repository
  already knows the answer moves;
- **finite-lattice-spacing `O(a²)` operator mixing** between the spin
  channels, which hypercubic symmetry permits and continuum rotational
  symmetry does not;
- **finite-volume distortion** of the projector decomposition at small `|p|`,
  where `θ` and `ω` are built from a discrete momentum;
- **the non-conservation of a lattice `T^{μν}`** unless an improvement
  programme is carried out — a conserved continuum current is generally only
  conserved up to `O(a)` on the lattice, and `:826` of the manuscript makes
  `∂_μ X^{μν} = 0` at `:827` the load-bearing premise of its universality
  argument.

**Five — the operator basis.** Per `FIERZSUM-01:255-259`, a single projected
correlator *"may miss states to which the chosen current has zero overlap"*, so
a pre-registration must state the operator basis and state the conclusion's
truncation-relative form. **`FIERZSUM-01:255` fixes the wording a downstream
task is allowed to use**: *"no pole detected in the frozen correlator matrix"*
— never *"the theory contains no vector state"*. The tensor-channel analogue
of that sentence must be written before the test is run, not after.

---

## 7. The verdict

    REQUIRES A CONSTRUCTION NOT YET SCOPED

**with `TRACTABLE BUT BLOCKED PENDING A RULING` applying in part.**

### 7.1 The evidence

Twelve components. **`N_both = 0`.** Three have an applicable implementation
and no specification; three have a specification and no implementation; **six
have neither.**

The six with neither are not peripheral. They are the definition of `⟨·⟩`
(C7), an evaluation beyond one loop (C8), a preregistered tensor-sector
operator basis (C9), the finite-volume and massless-limit rules (C10), the
meaning of "vanishing" (C11), and the artefact discriminator (C12). **A test
missing all six is not a test that is nearly ready.**

### 7.2 Why `REQUIRES A CONSTRUCTION NOT YET SCOPED` governs

**Because a ruling is removable by a decision and a missing construction is
not.**

`R1`, `R2`, `R3` and `R4` are open and this observable depends on all four —
that is a real blockage and `TRACTABLE BUT BLOCKED PENDING A RULING` applies
in part on its strength. **But if all four were ruled tomorrow, C7 through C12
would be exactly where they are now.** Ruling `R4` says what the measure is;
it does not supply a method for evaluating a correlator against it. Ruling
`R2` says what extents are admissible; it does not supply a finite-volume pole
extraction. **The blockage would lift and the construction would still be
absent.**

**The repository supplies its own demonstration that this is substantial
work.** `P2-VECPOLE-01` is the structurally analogous task — a pole question
about a projected correlator, in the vector channel. It is named in
`P2-FIERZSUM-01.md`, `P2-LATTICE-ONTOLOGY-01.md` and
`P2-LATTICE-ROUTE-01.md`. **It has no gate section in `GATES.md` and no
specification anywhere.** `FIERZSUM-01:472` states its status exactly:
`P2-VECPOLE-01` *"may then be SPECIFIED against the frozen correlator/kernel
framework"* once a prerequisite is discharged, and *"it additionally requires
its own frozen operator basis, analytic continuation, vector quantum-number
sector, residue/pole criteria, and exceptional-locus rules."*

**A task the repository has been unable to specify for the vector channel,
and whose specification it describes as requiring five further frozen items,
is not a task whose tensor-channel counterpart is a small increment.**

### 7.3 What `NOT DETERMINABLE FROM THIS REPOSITORY` would have required, and
why it does not apply

That verdict is for a repository that does not say enough to determine the
requirements. **This one says a great deal.** It names the observable, freezes
a doctrine governing spectral claims, enumerates the components for the
analogous correlator, records the reflection-positivity obligation and its
`NOT ESTABLISHED` state, and contains a working Barnes–Rivers implementation.
**The requirements are determinable. It is the construction that is absent.**

### 7.4 What remains to be built — named, not scoped

For completeness of the verdict and nothing more: C7 through C12 of §5.4, plus
implementations for C4, C5 and C6. **This artifact does not scope any of them,
does not estimate the work, and does not say in what order they should be
taken.**

---

## 8. What this assessment does NOT establish

- **It does not establish that the pole exists, or that it does not.** The
  manuscript calls the question nonperturbative and unresolved at `:808-809`
  and this artifact leaves it exactly there.
- **A `TRACTABLE` verdict was not returned, and would not have meant the
  answer was known.** Buildability and truth are different properties.
- **It does not establish that the emergent graviton is clean or unclean.**
  No residue was computed, estimated, or bounded.
- **It does not say this milestone should be done before or after anything
  else.** No task is compared to any other in these pages.
- **It does not adjudicate `R1`–`R5`.** Every node is reported as a dependency
  of the observable and every one is left open.
- **It does not choose a vanishing criterion, a volume, a mass, a window, or a
  tolerance.** §6 names what must be chosen and chooses none of it.
- **`N_both = 0` is a statement about this repository at this commit**, not a
  statement about the difficulty of the physics.
- **A validated `−(k+2)` in the `RECON-01b` line would not answer this
  question.** §1.1 gives the reason: that line measures a coefficient of an
  induced action for an external field, and this milestone asks whether the
  interacting theory has a propagating state.

## 9. Stops and clarifications

**`SPECIFICATION_DEFECT`** — none. §2's counts were supplied as the
Researcher's and were reproduced exactly once this task's own two files are
excluded, which is the expected behaviour of a whole-tree search run from
inside the tree it searches, not a defect in the figures.

**`ENVIRONMENT`** — `scipy` is absent while `pyproject.toml:12` declares
`scipy>=1.11`. **The repository's own code records the same fact and takes the
opposite side of the contradiction:** `scripts/recon2026/proca_curved.py:43-44`
states *"``scipy`` is not a declared package of this environment and is not
installed."* **The manifest says it is declared; the code says it is not.**
Recorded, not repaired — nothing here may modify an existing file.

**`OBSERVATION_METHOD_ERROR`** — none committed, two avoided. `Rivers` matches
inside `drivers` in five of twelve files and `pole` matches inside `tadpole`
in twenty-four of sixty-seven; both were caught by opening the matched lines
rather than reporting the counts. §2.2 and §2.3 record them because the same
failure mode — a substring of a longer word inflating a search that decides a
classification — has now occurred three times in this line, counting
`CHANNEL-B0`'s `composition`/`decomposition`.

**`REPOSITORY_DEFECT`** — none newly found by this assessment. Two standing
observations are re-recorded rather than treated as settled: the `scipy`
manifest contradiction above, and that two distinct functions named
`projectors(q)` exist in the same directory returning different objects
(`tt_check.py:105`, four projectors; `seagull_check.py:241`, one), which is a
name collision an importer cannot detect from the call site.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`** — one, reported and not
resolved. **`FIERZSUM-01 §5`'s doctrine is stated in general terms but was
written for `P2-VECPOLE-01`.** Whether it binds a tensor-channel task as
frozen governance, or merely as a precedent a tensor-channel specification
should follow, is not stated anywhere. **This artifact applied it as evidence
about what such a test requires and did NOT treat it as a ruling on this
milestone.** The question of which it is belongs to the PI, and §4 of the
governing specification forbids this task from deciding it.
