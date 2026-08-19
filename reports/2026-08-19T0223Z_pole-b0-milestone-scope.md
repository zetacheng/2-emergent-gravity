# Execution report — `POLE-B0`: what the manuscript's own decisive test would require

**Task:** `science/pole-b0-milestone-scope`
**Specification:** `specs/2026-08-19T0223Z_pole-b0-milestone-scope.md`
**Review:** `reviews/chatgpt/2026-08-19T0223Z_pole-b0-milestone-scope.md`
**Evidence base:** `11af14a792c5858b368180d99ab9ee4692a7f698`
**Artifact:** `derivations/P2-POLE-B0_milestone-scope.md`

**Measurement head for everything in this report: commit 3,
`b83a22fd5d8b882c137a413036e202353020019b`.** Nothing here claims to measure
commit 4. Commit 4 is this file; every figure that depends on it is labelled
**INTENDED**. The post-report layer — A12 final, A15-final, A16 and A17 at
commit 4, the push, and the branch tip read back — is returned to the Reviewer
in chat and is **not** written into this file.

**Nothing was computed. Nothing was built. No script was run against the
physics.** The only executions were the governance checker and the validator
suite, both of which this task's own criteria require.

---

## 0. Execution order

The specification's normative order was followed: **A3 environment first**,
then **A1 refs and branch availability**, then **A2 review binding**, then A4
onward. Criterion numbering is not execution order, and §5's A3 says "run
FIRST" in its own text.

---

## A3 — Environment conformance, run FIRST (MEASURED)

**Amendment D step 0.**

    execution location   /home/user/2-emergent-gravity for the diagnostic,
                         then the linked worktree
                         /tmp/claude-0/-home-user-2-emergent-gravity/
                         30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/poleb0
    worktree identity    primary worktree for A3/A1; a linked worktree,
                         created at the evidence base, for all task commits
    resolved HEAD        11af14a792c5858b368180d99ab9ee4692a7f698 at creation,
                         b83a22fd5d8b882c137a413036e202353020019b at this
                         report's measurement head

**Rule 13's diagnostic order.**

    shallow clone?            no
    commits reachable, HEAD   423
    commits, all refs         551
    Python                    3.11.15
    pytest                    9.1.1
    numpy                     2.4.6
    sympy                     1.14.0
    ruff                      0.15.8
    scipy                     ABSENT

**`scipy` is absent for the thirteenth consecutive task** while
`pyproject.toml:12` declares `scipy>=1.11`. **This task found the repository
taking the opposite side of that contradiction in its own source.**
`scripts/recon2026/proca_curved.py:43-44` states:

> Only ``numpy`` is used.  ``scipy`` is not a declared package of this
> environment and is not installed.

**The manifest says `scipy` is declared. The code says it is not.** Both are
in the tree at the same commit. Recorded, not repaired — §4 forbids modifying
any existing file. This is the first task in this line to find the
contradiction stated inside the repository rather than only between the
repository and the running environment.

`docs/local/execution_environment.md` continues to declare a Windows
environment that has never executed this work. Recorded, not repaired.

**Rule 13 carries two diagnostic orders, a known open item. No environment
failure occurred, so neither order was exercised** as a failure path. I name
neither as operative.

---

## A1 — Repository, refs, branch availability (MEASURED)

**`origin` remote URL, verbatim and not normalised:**

    https://github.com/zetacheng/2-emergent-gravity

It identifies `zetacheng/2-emergent-gravity`.

**After `git fetch origin --prune`, pasted from `git rev-parse`:**

    refs/remotes/origin/main   11af14a792c5858b368180d99ab9ee4692a7f698
    specification's base       11af14a792c5858b368180d99ab9ee4692a7f698

**Equal.** This is the head the `CHANNEL-B0` integration landed.

**Branch availability — `science/pole-b0-milestone-scope`:**

    git ls-remote --heads origin refs/heads/science/pole-b0-milestone-scope
      0 lines
    git branch --list science/pole-b0-milestone-scope
      0 lines
    git rev-parse --verify -q refs/heads/science/pole-b0-milestone-scope
      exit 1

**It did not exist, locally or remotely. No stop.** It was created at the
evidence base by `git worktree add -b`.

**The UTC time was measured, not assumed:** `2026-08-19T02:23:56Z`, giving the
token `0223Z` used in all four paths.

---

## A2 — Review committed, unedited, SHA bound (MEASURED)

**Field presence checked before value.** The review carries the literal string
`Reviewed specification SHA-256:` — present, **one** occurrence, at line 4,
populated with a 64-hex value rather than a placeholder.

    sha256 of the specification bytes as committed
      d69d0d4d04feec8d164ba67c75a8a341fee545c652f56991ff85bb7c4d076df7
    the review's bound SHA
      d69d0d4d04feec8d164ba67c75a8a341fee545c652f56991ff85bb7c4d076df7

**MATCH.** Verdict `APPROVE FOR EXECUTION`. Committed unedited as commit 2.

---

## Commits (MEASURED, pasted from `git rev-parse`)

    commit 1  b5315a2e31851494ba506ae4c3add62731474916
              spec: scope what the manuscript's own decisive pole test would require
    commit 2  53f03d3ad4f531e4cf8b48321706a3050cedae08
              review: pre-execution review for the pole milestone scope
    commit 3  b83a22fd5d8b882c137a413036e202353020019b
              scope: the decisive pole test requires a construction not yet scoped

**Commit 4's intended message:**

    report: the pole milestone's requirements are determinable and its
    construction is absent

---

## A4 — The milestone passage, re-read (MEASURED)

Quoted verbatim from `paper/emergent_gr_paper_v2_15.tex` at the head:

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

**The two statements, reported separately as §5 requires.**

**First — an induced kinetic term is not a pole.** `:807-808` sets *"a genuine
massless spin-2 pole in ⟨TT⟩"* against *"merely an induced kinetic term for an
external field"*. These are different objects. A kinetic coefficient for an
externally supplied field can be nonzero and correct in a theory whose
spectrum contains no such particle. A pole in `⟨TT⟩` asserts a propagating
state. **A 1PI kernel's singularities and a propagator's singularities are not
in the same places** — a propagator pole sits at a *zero* of the kernel.

**Second — the manuscript calls the question nonperturbative.** `:808-809`:
the claim *"is supported by the Ward structure above but is ultimately a
nonperturbative question."* **Supported is not established.** A Ward identity
constrains the form a kernel may take; it does not populate a spectrum. **This
is a gap the manuscript identifies and defers, not one it overlooks**, and the
distinction matters for how the finding should be read.

**Has the test been performed, attempted, or scheduled? Searched and
reported.**

    we have measured 0   has been performed 0   in progress 0   underway 0
    we measured      0   we report the      0   forthcoming  0   we defer  0
    we performed     0   remains to be      0

    scheduled 1     future work 3     left open 1     not yet 1

**Every non-zero hit was opened; none is this milestone.** `:395` schedules a
pair decomposition for re-audit. `:446`, `:448` and `:642` are other sectors.
`:544` is `ε`. `:1257` is the vector channel's mass-logarithmic coefficient,
*"not yet computed"*.

**The manuscript nowhere states that the decisive test has been performed,
attempted, or scheduled.**

---

## A5 — The component inventory (MEASURED)

**Four mutually exclusive states, as in `RECON-B0`. An implementation counts
only if it is potentially applicable to this test; applicability is stated per
implementation.**

    N_total = N_both + N_impl + N_spec + N_neither
       12   =    0   +   3    +   3    +    6

**`N_both = 0`.** No component of this test has both an applicable
implementation and a specification. That is the inventory's governing number.

**`IMPL` — 3.** A lattice stress-tensor operator (`tt_check.py:17-24`, a
declared Wilson-fermion EMT vertex; **applicable**, same species and same
lattice); the four Barnes–Rivers projectors (`tt_check.py:105-126`;
**applicable**, Euclidean `d=4`, the exact set); and spin-channel projection
of a rank-4 object (`tt_check.py:129-135`, returning `g2, g1, g0s, g0w`;
**applicable, with the qualification** that the only existing caller discards
three of the four). **None is frozen by any specification** — `tt_check.py:17`
says *"Vertex prescription (declared)"*, declared by the script.

**`SPEC` — 3.** The pole-identification method (`P2-FIERZSUM-01.md:250-252`,
*"identified from eigenvalue singularities of `G`, or equivalently determinant
zeros of its inverse kernel; not poles alone"*, with
`P2-LATTICE-ROUTE-01.md:294-295` naming the components); residue and
spectral-weight extraction (`FIERZSUM-01:247-250`); and Osterwalder–Schrader
reflection positivity for a spectral reading (`P2-LATTICE-ONTOLOGY-01.md:70-80`,
which freezes the obligation and requires proposition `(ii)` to be proved
*"per declared kinetic operator"*). **No implementation exists for any of the
three**; `P2-LATTICE-MICROSPEC-01_tm-rp-scope.md:3` opens *"THIS ARTIFACT
CONSTRUCTS NOTHING"* and `:99` records the state as `NOT ESTABLISHED` for all
four candidate fermion theories.

**Qualification carried, not glossed:** the two `FIERZSUM`/`ROUTE` passages
were written for `P2-VECPOLE-01`, the vector channel. `FIERZSUM-01 §5`'s
doctrine is stated in general terms; `ROUTE-01`'s component list is explicitly
a `⟨J J⟩` list. **The artifact records them as evidence about what this class
of test requires and does not transplant them as rulings on this milestone.**

**`NEITHER` — 6.** The definition of `⟨·⟩` (the microscopic measure and
state); an evaluation of `⟨TT⟩` beyond one loop; a preregistered operator basis
for the tensor sector; finite-volume rules and the massless limit; the
numerical meaning of *"vanishing"*; and an artefact-versus-physics
discriminator.

**For the first of those, measured in code:** `monte` 0, `ensemble` 0,
`importance sampling` 0, `hybrid monte carlo` 0, `HMC` 0, `thermaliz` 0,
`autocorrelation` 0, `jackknife` 0, `bootstrap` 0, `gauge configuration` 0,
`path integral measure` 0 — **all zero `.py` files.**

---

## A6 — What exists, classified (MEASURED)

### The counts, with the self-inclusion separated

**Measured with `git grep -lil` over the whole tree. Two figures are given
because this task's own specification and review are in the tree and contain
every one of these terms.**

    TERM                      TOTAL   THIS TASK'S OWN   EXCLUDING OWN
    Barnes                        9          2                7
    Rivers                       14          2               12
    projector                    56          2               54
    stress-tensor correlator     10          2                8
    pole                         69          2               67
    spin projector                1          1                0

**Excluding this task's own two files, all six reproduce the Researcher's
figures exactly** — 7, 12, 54, 8, 67, 0. **`spin projector` is the sharp
case:** the single hit in the entire tree is this specification's own line
stating that the count is zero.

**These are file counts. They are not machinery.** The classification follows.

### `Rivers` — five of twelve are the word `drivers`

**Measured per file by comparing the count of `rivers` against the count of
`drivers`.**

    SUBSTRING-ONLY, every occurrence inside "drivers":
      GATES.md (2), P2-BETAV-RECON-01_scope-assessment.md (2),
      reports/2026-08-17T1105Z_recon-b0-scope.md (1),
      scripts/P2-BETAV-CAMPAIGN/harness_compute.py (1),
      scripts/recovered_2026/PROVENANCE.md (1)

    GENUINE "Barnes--Rivers" — 7 files, and they are EXACTLY the 7 `Barnes`
    files.

The five are the historical β-extraction **drivers** that `GATES.md:415` and
`:681` warn about. **A count of twelve would have been a count of twelve
things, five of which are a different word.**

### `pole` — twenty-four of sixty-seven are `tadpole`

    whole tree, every "pole" inside "tadpole"            24 files
    whole tree, at least one non-tadpole "pole"          43 files

**In code the ratio is worse.** Six of the ten `.py` files matching `pole` are
`tadpole`-only. Three of the remaining four are prose **disclaiming** a pole
(`p2_channel_character_layers.py:462`, `p2_chirality_census.py:508`,
`p2_diquark_both_eta.py:768`, all of the form *"… is not a bound-state or
pole …"*). The tenth is `recovered_2026/batch2/ep_test.py:43`, a **free-fermion
dispersion** pole — *"free anisotropic Wilson fermion speed^2 at p->0 from
pole dispersion"* — a single-particle dispersion relation, not a singularity
of an interacting two-point function.

**`residue` in code returns exactly one file:** `speed_check.py:89`, *"omega
integral done analytically by residues"*, a contour remark.

**No implementation in this repository extracts a pole or a residue from a
correlator.**

### `projector` at fifty-four — the axis-TT versus Barnes–Rivers distinction

Eighteen of the fifty-four are `.py`. **Three distinct objects carry the
name.**

**A — the full Barnes–Rivers set. One implementation, one file.**
`scripts/recovered_2026/tt_check.py:105-126`, whose docstring is *"Barnes-Rivers
projectors for Euclidean momentum q (4-vector)"*. It builds `P2`, `P1`, `P0s`,
`P0w`, and `project()` at `:129-135` returns all four contractions.

**B — the spin-2 projector ALONE, a different function with the same name.**
`scripts/recovered_2026/seagull_check.py:241-253` also defines
`def projectors(q)` and returns **`P2` only**. `structure_decomp.py:16` and
`boson_loop.py:23` import it.

**The consequence is exact: every file importing `seagull_check.projectors`
can project onto spin-2 and CANNOT measure a spin-1 or spin-0 residue, because
it never receives `P1`, `P0s` or `P0w`.** That is the axis-TT-style
transverse-traceless projection the specification anticipated, and it is a
different object from the Barnes–Rivers decomposition the milestone names.

**C — a longitudinal projector, unrelated.**
`scripts/recon2026/proca_curved.py:332`, `longitudinal_projector_flat`, a
rank-1 projector used for the Proca gauge-mode check.

**So `projector` at 54 files resolves to exactly ONE implementation of the
object this milestone names.**

### The one implementation computes four channels and discards three

`tt_check.py:152-155` calls `project(...)[0]` — **`g1`, `g0s` and `g0w` are
computed on every call and thrown away.** `run()` then fits `G2` in `ε` and
reports `Z_h`, an isotropy ratio and a dim-6 anisotropy.

**The repository contains the projectors the milestone needs and no use of
them for the milestone's question.** The manuscript's criterion is about
exactly the three channels that code discards.

---

## A7 — Reachability from `RECON-01a`, and whether `SRC-B0`'s absence transfers (MEASURED)

### Is `⟨TT⟩` computable from what `RECON-01a` landed?

**No, as the manuscript defines it.**

`P2-BETAV-RECON-01a_construction-and-flat-validation.md:19-23` records the
deliverables as `D1[g,h]`, the metric-coupled 1-form (Proca) operator, and
`D0[g,h]`, the compensating scalar, with `logdet_operator` at
`proca_curved.py:356`. **MEASURED: `fermion`, `Dirac` and `stress` return zero
lines in that artifact.** The construction is bosonic throughout, on a
prescribed external background. **The fermionic stress tensor is not in it.**

**A formal route exists and it lands on the object the milestone excludes.**
`Γ = ½ log det` is what `logdet_operator` computes; two metric variations of
it produce a two-index-pair object. **That object is `Γ^(2)`, the 1PI kernel
for an external metric — `:807-808`'s "induced kinetic term for an external
field" by name.** Reaching a pole would require inverting the kernel, and no
inversion of that kind is performed anywhere in this repository. **And the
route inherits `DET-01`'s unfixed measure through `Γ`**, per
`P2-SRC-B0_source-side-scope.md:186-192`.

### Does `SRC-B0`'s absent source side transfer? — answered explicitly

**It does not transfer as an entailment. It partially transfers through a
shared dependency. Both halves are stated because they are different
statements.**

**It does not transfer.** `SRC-B0` returned `NOT PRESENT / EXTERNAL STATUS NOT
DETERMINED` about **a configuration** — a lump whose field one would compute
to ask whether two lumps attract. `⟨T T⟩` is a **two-point function of an
operator**. It needs no configuration: it needs an operator, a state, and a
measure. **A correlator of stress tensors and a stress tensor sourcing a field
are different objects, and the absence of the second does not imply the
absence of the first.** This assessment did not infer unavailability from
`SRC-B0`, and the specification was right to require the question be answered
rather than assumed.

**Where it bears.** `SRC-B0` §4.1 established a conditional:

    Γ-DEFINED  T_μν = (2/√g) δΓ/δg^{μν}     REQUIRES the unfixed measure
    S-DEFINED  T_μν = (2/√g) δS/δg^{μν}     DOES NOT

**The manuscript's `T^{μν}` at `:673-675` is S-defined** — a bilinear operator
built from the classical action. **So the operator does not need the measure.**

**But the milestone does not ask for an operator. It asks for the expectation
value of a product of two of them, and an expectation value is
measure-weighted by definition.** The dependency enters through the bracket,
not through the operator — a different route from `SRC-B0`'s, arriving at the
same open node. **An S-defined operator inserted into an undefined measure
yields an undefined number.**

---

## A8 — `R1`–`R5` dependence (MEASURED)

**Per node, one of three states. Silence is not independence. This task
adjudicates none of them.** All five carry `STATUS OPEN` in
`P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md`.

    R1  the canonical kinetic operator and its parameters    DEPENDENCE ESTABLISHED
    R2  the admissible lattice extent, finite-volume rules   DEPENDENCE ESTABLISHED
    R3  boundary conditions, the temporal one in particular  DEPENDENCE ESTABLISHED
    R4  the microscopic variables, state space and measure   DEPENDENCE ESTABLISHED
    R5  the internal multiplicity N                          DEPENDENCE NOT ESTABLISHED

**`R1`** — established twice over. `T^{μν}` at `:673-675` is a derivative
fermion bilinear whose lattice realisation discretises `∂^ν` against a
specific Dirac operator, and the propagators in any evaluation are that
operator's. `tt_check.py:12-13` records that it tests *"prescription
sensitivity by switching the Wilson-term vertex on/off"* — **a computation
that reports its own sensitivity to a prescription depends on the ruling that
would fix it.** Separately, `ONTOLOGY-01:75-80` requires reflection positivity
to be proved *"per declared kinetic operator"*.

**`R2`** — the criterion is a pole at `p² = 0` exactly, and on a finite
periodic lattice that is one discrete point. Establishing that a singularity
sits **at** zero rather than near it is a statement about a limit, and
`ROUTE-01:294-295` names *"finite-volume pole extraction"* as required for the
structurally analogous `⟨J J⟩` case.

**`R3`** — `ROUTE-01:201-203` names *"transfer-matrix normalization;
geometry-dependent measure and Jacobian factors; finite temporal extent;
temporal boundary conditions"* among the content of a blocking deliverable. A
two-point function's spectral decomposition runs along the temporal direction
and its content depends on that boundary condition; the repository names the
dependency in the one place it discusses reconstructing spectral information.

### `R4`, in its own paragraph

`R4`'s node is stated in five words at the ledger's `:138`: *"what the
microscopic measure is"*. `STATUS OPEN`. `DET-01` established that the
functional measure is `NOT DETERMINABLE` from the frozen conventions.

**`DEPENDENCE ESTABLISHED`, and the route is the bracket, not the operator.**
`⟨ T T ⟩` is a measure-weighted expectation by construction. **`SRC-B0`'s
conditional does not rescue this milestone**, because the conditional is about
which stress tensor a calculation uses, and this milestone's object is not a
stress tensor — it is a correlation function of two of them. **The
correlation is where the measure enters, and it enters unconditionally.**

**This is the relation §7's fifth junction anticipated, and it is worth
stating in full.** The `βV`/heat-kernel line inherits the unfixed measure
through `Γ`. The source side inherits it conditionally, through the choice of
which `T`. **This milestone inherits it unconditionally, through `⟨·⟩`.**
Nothing here rules on `R4` and nothing here says the measure cannot be fixed.
It says this observable does not route around it.

**`R5`** — `DEPENDENCE NOT ESTABLISHED`, and deliberately not `INDEPENDENT`.
The repository's one relevant statement is `tt_check.py:7`, `Γ^(2) = N * B(q)`,
with `:26` recording *"N = 1 (overall N trivial)"*. **That is a statement about
a perturbative kernel, not about the interacting correlator this milestone
names**, and I did not extend it by argument. The repository is silent on
whether the interacting correlator's spin-channel structure depends on `N`,
and silence is not independence.

---

## A9 — What a pre-registration would have to fix (MEASURED, and nothing chosen)

**This section names what must be chosen. IT CHOOSES NOTHING.** No tolerance,
no volume, no mass, no window and no threshold appears below or in the
artifact.

**Three words in the manuscript's criterion are not operational on a finite
lattice as they stand.**

**One — "vanishing".** A measured residue is a number with an uncertainty;
it is never identically zero. A pre-registration must fix **which** test the
criterion is, because they are different tests that can disagree: an absolute
tolerance `|R_{1,0}| < τ`; a **ratio** `|R_{1,0}|/|R_2| < τ`, which is
scale-free where the first is not; a **scaling rule**, `R_{1,0} → 0` toward
the continuum or infinite-volume limit at a stated rate; or a **significance
statement** against an estimated uncertainty. **Which of the four, and the
value of `τ` or the rate.** Neither is chosen here.

**Two — "a single `p² = 0` pole".** *Single* needs a rule for what counts as
one structure rather than two nearby ones, and — since `FIERZSUM-01:247`
records that the content includes *"poles, resonances and branch cuts"* — a
rule separating a pole from a cut. *`p² = 0`* needs a rule for how close to
zero counts as at zero on a lattice with discrete momenta.

**Three — volumes and masses.** A stated set of lattice extents, a stated set
of fermion masses, and **the order of limits: whether the massless limit is
taken before or after the infinite-volume limit changes what is measured.**
`R2` is the open node that would fix the admissible extents.

**Four — the artefact-versus-physics discriminator.** A non-vanishing spin-0
or spin-1 residue can arise from: contact and seagull terms, which
`tt_check.py:12-13` explicitly defers; the Wilson term's explicit symmetry
breaking, whose effect the same script already knows is non-zero because it
tests switching it off; finite-spacing `O(a²)` operator mixing between spin
channels, which hypercubic symmetry permits and continuum rotational symmetry
does not; finite-volume distortion of the projector decomposition at small
`|p|`; and non-conservation of a lattice `T^{μν}` absent an improvement
programme — which bears directly on `:827`'s `∂_μ X^{μν} = 0`, the
load-bearing premise of the manuscript's universality argument.

**Five — the operator basis.** `FIERZSUM-01:257-259` warns that a single
projected correlator *"may miss states to which the chosen current has zero
overlap"*, and `:255` fixes the wording a downstream task may use: **"no pole
detected in the frozen correlator matrix" — never "the theory contains no
vector state".** The tensor-channel analogue of that sentence must be written
before the test is run, not after.

---

## A10 — The verdict, with its evidence (MEASURED)

    REQUIRES A CONSTRUCTION NOT YET SCOPED

**with `TRACTABLE BUT BLOCKED PENDING A RULING` applying in part.**

**The evidence.** Twelve components; `N_both = 0`; three `IMPL`, three `SPEC`,
**six `NEITHER`**. The six are not peripheral: the definition of `⟨·⟩`, an
evaluation beyond one loop, a preregistered tensor-sector operator basis, the
finite-volume and massless-limit rules, the meaning of "vanishing", and the
artefact discriminator.

**Why the not-yet-scoped verdict governs.** `TRACTABLE BUT BLOCKED PENDING A
RULING` applies in part on real strength — `R1`, `R2`, `R3` and `R4` are open
and this observable depends on all four. **But a ruling is removable by a
decision and a missing construction is not.** If all four were ruled tomorrow,
the six `NEITHER` components would be exactly where they are. Ruling `R4` says
what the measure is; it does not supply a method for evaluating a correlator
against it. **The blockage would lift and the construction would still be
absent.**

**The repository supplies its own demonstration that this is substantial
work.** `P2-VECPOLE-01` is the structurally analogous task — a pole question
about a projected correlator, in the vector channel. It is named in
`P2-FIERZSUM-01.md`, `P2-LATTICE-ONTOLOGY-01.md` and
`P2-LATTICE-ROUTE-01.md`. **It has no gate section in `GATES.md` and no
specification anywhere.** `FIERZSUM-01:472` records that it *"may then be
SPECIFIED"* only once a prerequisite is discharged, and that it *"additionally
requires its own frozen operator basis, analytic continuation, vector
quantum-number sector, residue/pole criteria, and exceptional-locus rules."*

**Why `NOT DETERMINABLE FROM THIS REPOSITORY` does not apply.** That verdict
is for a repository that does not say enough to determine the requirements.
This one names the observable, freezes a doctrine governing spectral claims,
enumerates the components for the analogous correlator, records the
reflection-positivity obligation and its `NOT ESTABLISHED` state, and contains
a working Barnes–Rivers implementation. **The requirements are determinable.
It is the construction that is absent.**

---

## A11 — Nothing computed, nothing ranked (MEASURED)

**Two separate searches, both reported.**

**Search one — any newly computed or estimated scientific quantity belonging
to this milestone:** a value of `⟨TT⟩`, a projected correlator, `Π^{(2)}(p)`
or any spin component, a pole position, a spin-0 or spin-1 residue, or a
numerical estimate or bound on any of them.

**Expressly excluded, because this task's own criteria require them:**
governance and checker measurements, hit counts, path counts, test counts,
section counts, blob ids, SHAs, timestamps, environment versions, and any
figure quoted from the repository. **The specification records that an earlier
draft searched for "any computed quantity", which A6, A12, A13, A15 and A16 all
require this report to contain, so a correct execution would have violated its
own search — the fourth such criterion in this line. The repaired wording is
satisfiable and was satisfied.**

**Result: zero.** `we compute`, `we estimate`, `we find that the residue`,
`the residue is`, `the pole is at`, `Pi^{(2)}`, `estimated pole`, `we obtain`,
`our value`, `approximately` — **all zero in the artifact and zero in every
commit message in this range.** Every decimal number in the artifact was
enumerated: thirty-five occurrences, **all of them section numbers**.

**No correlator, projection, pole, residue, estimate or bound was produced by
this task.**

**Search two — any statement that one task should precede another.**

**Result: zero substantive hits.** `should come first`, `should be done
first`, `comes first`, `before this`, `priority`, `first priority`, `more
important`, `higher priority`, `next task` — all zero in the artifact and all
zero in the commit messages. **`precede` returned one line in the artifact and
it is the word `precedent`**, in `§9`'s clause about whether `FIERZSUM-01 §5`
binds as frozen governance or as a precedent a tensor-channel specification
should follow.

**That is the third substring false positive this task encountered**, after
`drivers` for `Rivers` and `tadpole` for `pole` — and it landed inside A11's
own compliance search. Reported as a matched line read, not as a count.

**No task is ranked against any other in the artifact or in this report.**

---

## A12 — Scope, against the frozen manifest (MEASURED, plus one INTENDED)

Measured fresh against base `11af14a7…`.

    commit 1  b5315a2e   1 path
      A  specs/2026-08-19T0223Z_pole-b0-milestone-scope.md

    commit 2  53f03d3a   2 paths
      A  reviews/chatgpt/2026-08-19T0223Z_pole-b0-milestone-scope.md
      A  specs/2026-08-19T0223Z_pole-b0-milestone-scope.md

    commit 3  b83a22fd   3 paths
      A  derivations/P2-POLE-B0_milestone-scope.md
      A  reviews/chatgpt/2026-08-19T0223Z_pole-b0-milestone-scope.md
      A  specs/2026-08-19T0223Z_pole-b0-milestone-scope.md

    commit 4             4 paths          INTENDED
      the three above plus
         reports/2026-08-19T0223Z_pole-b0-milestone-scope.md

**Contributions, separately labelled:** commit 1 contributes the
specification; commit 2 the review; commit 3 the artifact; commit 4 this
report. **Each commit contributes exactly one path and modifies nothing.**

**Every status letter is `A` at all three measured commits. Zero
modifications. None of the forbidden operations** — delete, rename, copy, type
change, unmerged, unknown — **appears.** The manifest states 4 additions and 0
modifications; the measured figures agree at every commit. **No stop.**

**`append_only: DECISION_LOG.md` was treated as a checker-configuration
declaration and NOT as an authorisation to write that file.** It is unchanged
at 89541 bytes — A15's P3 evidence measures this independently.

---

## A13 — Nothing existing changed (MEASURED)

    paths in the base tree, compared          519
    paths differing base → head that existed
      at the base                               0

    paper/emergent_gr_paper_v2_15.tex
      blob at 11af14a7   c8246f890b07f53ab8094981cbd5a02972fda4c1
      blob at b83a22fd   c8246f890b07f53ab8094981cbd5a02972fda4c1

**Identical blob id at both ends.** The base-to-head diff contains three
entries and **every one is an addition**.

**`derivations/P2-*` re-measured, not carried: 51 at the base, 52 at the
head.** The one added file is `P2-POLE-B0_milestone-scope.md`.

**Blob-identical at both ends, confirmed individually:**

    GATES.md                            2b3bd5069414f009e1a0466c4990db2949519bd8
    CONVENTIONS.md                      8badc51f38d85d54b5c547d3abc14e7c522dcbcf
    DECISION_LOG.md                     d9dd2bf3a8cca405f03b31c51b1f478c7db77ca2
    docs/BRANCHING_POLICY.md            3f0f35d4da448eb444d223fd003a5b0601792dc3
    docs/GOVERNANCE-DEBT.md             b77e961d49c2d4b7cc51638fae32be5d5a72ec34
    scripts/recon2026/proca_curved.py   03f46905e5798fb7f6880dfae9ed5a1931be895b
    scripts/recon2026/flat_validation.py 6b21f9d6db67641ec7de31b7006884b617de3e8c
    tests/test_recon2026_flat_limit.py  1d7ba5672614dedcd3b78483b5d43431af65fc7a
    results/ (whole subtree)            9015049f68d5ace2790b5c62976e798298442bce

Both registers — `docs/BRANCHING_POLICY.md` and `docs/GOVERNANCE-DEBT.md` —
are unchanged.

---

## A14 — Gate invariants, pins, and gate coverage (MEASURED)

**Read SCOPED at commit 3**, to `^## P2-` headings and to the `P2-PHASE-01`
section body rather than to any substring.

    ^## P2- count                14
    P2-PHASE-01 Status           PROPOSED
    prerequisite 1               ADOPTED / SATISFIED
    prerequisite 2               ADOPTED / SATISFIED

**Both pins recomputed from the pinned files, not read back from the stored
value:**

    P2-PHASE-01_microscopic_parameter_domain.md
      declared  4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
      computed  4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
    P2-PHASE-01_input_admissibility_contract.md
      declared  e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
      computed  e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3

**All four invariants hold.**

### Does any gate cover this milestone?

**`GATES.md` searched for the milestone's own terms:**

    Barnes 0            spin projector 0            massless pole 0
    Rivers 2            stress-tensor correlator 0  decisive test 0
    spin-2 0            stress tensor correlator 0  numerical milestone 0
    spin-1/0 0          <TT> 0, langle TT 0         milestone 0

    residue 1           pole 9

**Both non-zero results are false positives.** `Rivers` at 2 is `drivers`
(`:415`, `:681`). Of the nine `pole` hits, **eight are `tadpole`** — `GATES.md`
contains `tadpole` eight times — and the ninth is `:1180`, *"negative-residue
physical pole"*, which is also the single `residue` hit and belongs to
`P2-MULTIPHASE-GRAV-01`'s FAIL criterion, a different argument about whether
any phase gives healthy gravity.

**No gate covers this milestone.** The fourteen gate sections are named for
the heat-kernel, gap-equation, `β` extraction, normalisation, circularity,
numerical-reproduction, reconstruction, assembly, channel-freeze, phase,
multiphase, recovered-engine and lattice-ontology lines. **None of them is the
pole test**, and `P2-VECPOLE-01` — the vector-channel analogue named in three
derivations — has no gate section either.

---

## A15 — The checker over this task's own range (MEASURED)

Invoked as `python3 -m scripts.governance_tools.task_checker --repo . --config
<json>`, base `11af14a7…`, head **commit 3**, four invocations (two runs × two
prospectivity readings). **All four exited 0 with empty stderr.**

**The output was PARSED, not grepped.** The property list is a **JSON array of
objects** with keys `id`, `status`, `classification`, `evidence` — a key lookup
by property name returns `None`, and a grep for `PASS` counts the word inside
the `does_not_establish` prose. Every figure below comes from `json.load` and
indexing into the parsed structure.

### RUN 1 config, verbatim (INCLUSIVE; EXCLUSIVE differs only in that field)

```json
{
  "base": "11af14a792c5858b368180d99ab9ee4692a7f698",
  "head": "b83a22fd5d8b882c137a413036e202353020019b",
  "append_only_paths": [
    "DECISION_LOG.md"
  ],
  "authorised_modified_gates": [],
  "prospectivity": {
    "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
    "inclusivity": "INCLUSIVE"
  },
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

### RUN 2 config, verbatim (INCLUSIVE; EXCLUSIVE differs only in that field)

```json
{
  "base": "11af14a792c5858b368180d99ab9ee4692a7f698",
  "head": "b83a22fd5d8b882c137a413036e202353020019b",
  "specification_paths": [
    "specs/2026-08-19T0223Z_pole-b0-milestone-scope.md"
  ],
  "append_only_paths": [
    "DECISION_LOG.md"
  ],
  "authorised_modified_gates": [],
  "prospectivity": {
    "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
    "inclusivity": "INCLUSIVE"
  },
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

### Parsed results — identical across all four invocations

    overall            PASS
    properties         9   (a JSON array, length 9)
    PASS               7
    NOT_APPLICABLE     2   (P5, P9)
    NON_GREEN values   none anywhere
      no NOT_DECLARED, no NOT_PARSEABLE, no DECLARATION_CONFLICT

    P1 PASS            scope manifest arithmetic
    P2 PASS            Rule 15 commit order
    P3 PASS            append-only on both measures
    P4 PASS            superseded branches are not merged
    P5 NOT_APPLICABLE  merge parentage against recomputed facts
    P6 PASS            commit-message hygiene
    P7 PASS            gate integrity
    P8 PASS            Rule 15 placement and specification-first
    P9 NOT_APPLICABLE  reports carry a Stops and clarifications section

    commits_in_range               3
    commits_on_first_parent_line   3
    prospectivity commits_in_scope 3
    prospectivity out_of_scope     []   (empty)

**`PASS` is 7, not zero. No stop on that ground.** The count was taken by
counting parsed `status` fields.

**`NOT_APPLICABLE` is not a `NON_GREEN` value.** The `NON_GREEN` set is
`{NOT_DECLARED, NOT_PARSEABLE, DECLARATION_CONFLICT}`, and none of the three
appears anywhere in any of the four documents. Both `NOT_APPLICABLE` results
carry an explicit `reason` field:

    P5  "no merge commit in range"
    P9  "range adds no report"

**Both are correct and both are structural.** This is a scope task, not an
integration — there is no merge commit for P5 to examine. And the report is
commit 4, outside the measured range by construction, so P9 has no report to
check. **This is the first task in this line whose range is a pure scope line,
and the two `NOT_APPLICABLE` results are what that looks like.** In the four
preceding integrations P5 examined a merge and P9 found a report arriving by
merge; neither is present here.

### `declared_source` — reported as it exists

**It is not a per-property field.** Measured across all four outputs, it
occurs **exactly twice** per document, nested inside `evidence`:

    /properties[2]/evidence/declared_source  =  "specification"      (P3)
    /properties[6]/evidence/declared_source  =  "specification"      (P7)

**The other seven properties carry no `declared_source` key at any depth.** P3
and P7 are the two that consume a caller-supplied declared set — `append_only`
and `authorised_gates` — so they are the only two for which the question has a
subject. **I report the two values that exist and do not manufacture nine.**

### P3 and P7 evidence

    P3  declared_key             append_only
        declared                 ["DECISION_LOG.md"]
        declared_by_specification ["DECISION_LOG.md"]
        supplied_by_config       ["DECISION_LOG.md"]
        DECISION_LOG.md          base 89541 bytes, head 89541 bytes,
                                 base_is_byte_prefix_of_head true, PASS

    P7  gates_path               GATES.md
        section_count base/head  14 / 14
        raw_heading_count        14 / 14
        added_sections           []
        removed_sections         []
        authorised_modified      []
        unauthorised_changed     []

**`P7` reports fourteen sections**, at both ends, with the raw heading count
agreeing with the scoped section count — so the fourteen is not an artefact of
a lenient heading match. **`unauthorised_changed` is empty against an empty
authorised set**, the strict reading: nothing may change, and nothing did.

### What RUN 1 did

**RUN 1 is observational: it names no specification and lets the checker
discover every specification in the range. It discovered exactly one** — this
task's own — and `P1` returned a single evidence block, `parse OK`, `stated 4`,
`counted 4`, `"stated: 4 additions, 0 modifications"`.

**RUN 1 and RUN 2 are byte-identical.** `diff` between the two INCLUSIVE
outputs returns exit 0 with no differing lines.

**So there is no C3 multi-specification residual in this range.** That
residual has been recorded in seven consecutive integration ranges, where two
specifications sit in one range declaring different totals and
`_declarations_from_specs` compares only `append_only_paths` and
`authorised_modified_gates`. **A scope task's range contains exactly one
specification, so the conditions for the residual do not arise.** Recorded as
an absence with its reason, not as evidence the residual is fixed — nothing in
the checker changed.

**RUN 2 is stop-governing.** It named only this task's specification, returned
`overall: PASS` with seven `PASS`, two `NOT_APPLICABLE` and no `NON_GREEN`
value, under both prospectivity readings. **No stop.**

**I did not adjust the config or the specification's declarations to make RUN 2
pass.** It passed as issued.

### The two prospectivity readings

Each pair differs at **exactly one line, line 252 — the `inclusivity` field
itself**. `commits_in_scope` is 3 and `commits_out_of_scope` is empty under
both, so the boundary's inclusivity has nothing to decide here. The scope note,
verbatim:

> P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by
> merge were governed by the task that made them.

---

## A16 — Validators (MEASURED)

At commit 3:

    332 passed, 2 deselected in 38.89s
    exit status 0

**Matches the expected 332 passed, 2 deselected.**

---

## A17 — Commit-message hygiene, commits 1–3 (MEASURED)

**Rule 20 binds this task.** Measured on the message body alone
(`git log -1 --format='%B'`), with the git identity reported separately so its
`noreply@anthropic.com` is not confused with a message trailer.

    commit 1  b5315a2e  body 2 lines, 72 bytes
    commit 2  53f03d3a  body 2 lines, 59 bytes
    commit 3  b83a22fd  body 2 lines, 70 bytes

    Per commit, in the message body, case-insensitive:
      Co-Authored-By 0   Claude Code 0   opus 0    Claude-Session 0
      claude.ai      0   Claude      0   sonnet 0  anthropic 0
      Generated with 0                             http 0

**All zero on all three.** No co-author trailer, no session URL, no "Generated
with" line, no model identifier.

The git identity is `Claude <noreply@anthropic.com>` for author and committer
on all three. That is the configured repository identity, not message content.
**No hygiene repair was needed and none was performed**, so Rule 20's narrow
permission to rewrite a message before pushing was not exercised. The
checker's independent `P6` agrees, returning `PASS`.

A17 for commit 4 belongs to the post-report layer.

---

## Rule 16 assessment — five junctions, all five

**Rule 16 is operative.**

### First — an induced kinetic term is not a pole, and this is what the task turns on

`:807-808` draws the distinction in the manuscript's own words. **Everything
the `βV` line has computed is the former.** `Z` is defined at
`CONVENTIONS.md:20` as the coefficient of `∫√g R` — a coefficient for a metric
treated as an **external field**. `tt_check.py:7` states its object as
*"Euclidean quadratic effective kernel: Gamma^(2) = N * B(q)"*, and its
deliverables at `:9-15` are an isotropy check, `Z_h = dG2/dq²`, and a dim-6
anisotropy. `RECON-01a` builds bosonic operators on a prescribed background.

**The milestone asks whether the interacting theory has a propagating spin-2
excitation at all.** A propagator pole sits at a **zero** of the kernel, not a
pole of it.

**A validated `−(k+2)` in the `RECON-01b` line would not answer this
question.** It would validate heat-kernel arithmetic against a blind target —
a correct coefficient. **If the spin-1/0 residues do not vanish, it would be a
correct coefficient for something that is not a graviton.** That is a
statement about what the two lines test, and it is not a statement about which
should be done.

### Second — the manuscript calls this nonperturbative, and this assessment does not change that

`:808-809` says the claim *"is supported by the Ward structure above but is
ultimately a nonperturbative question."* **This report does not move that
status by one inch.**

**And the point generalises to the verdict.** Had the verdict been
`TRACTABLE FROM WHAT EXISTS`, it would have meant the measurement is
buildable — **not that the answer is known, and not that it is likely.**
Buildability and truth are different properties, and a reader who converts one
into the other has added something this report does not contain. The verdict
returned is `REQUIRES A CONSTRUCTION NOT YET SCOPED`, which is weaker still,
and it too says nothing about whether the pole exists.

### Third — a scope assessment ranks nothing

**This task does not say whether this milestone or `RECON-01b` comes first.**
That is a PI decision and §4 forbids it. A11's second search confirms the
prohibition was honoured: zero substantive hits in the artifact and zero in
every commit message, the single `precede` match being the word `precedent`.

**A reader who takes any verdict here as a recommendation would be reading one
in.** §1 of the specification observes that a milestone failure would make a
correct coefficient a coefficient for something that is not a graviton, and
then forbids concluding the milestone should be done first. **Both halves are
carried: the observation is reported under the first junction, and no ordering
follows it.**

### Fourth — the counts are file counts, and the separation is reported

**§2's figures were the Researcher's, are file counts, and were reproduced
exactly** once this task's own specification and review are excluded — 7, 12,
54, 8, 67, 0.

**`projector` at 54 files does include a different object, as the
specification anticipated**, and there are three:

- the **full Barnes–Rivers set**, `tt_check.py:105-126`, four projectors —
  **one file, one implementation**;
- the **spin-2 projector alone**, `seagull_check.py:241-253`, a **different
  function with the same name**, imported by two other scripts, which
  therefore **cannot measure a spin-1 or spin-0 residue at all**;
- a **longitudinal projector**, `proca_curved.py:332`, unrelated.

**How they were separated:** by opening each `.py` hit and reading what the
function returns, rather than by counting names. That is also how `Rivers`
resolved to five `drivers` out of twelve and `pole` to twenty-four `tadpole`
files out of sixty-seven.

### Fifth — `A7` and `A8`, reported prominently for the reason the specification gives

**The correlator does inherit `DET-01`'s unfixed measure, and it inherits it
unconditionally.**

The `βV`/heat-kernel line inherits it through `Γ`. The source side inherits it
conditionally, per `SRC-B0` §4.1 — the Γ-defined stress tensor does, the
S-defined one does not. **This milestone inherits it through `⟨·⟩`, and no
choice of stress tensor avoids that, because the milestone's object is not a
stress tensor but a correlation function of two of them.**

**So this milestone is not independent of the microscopic line either.**
`R1`, `R2`, `R3` and `R4` all carry `DEPENDENCE ESTABLISHED`.

**The specification's own conditional then applies: the programme would have
no route that is independent of the microscopic line.** I report that as the
conditional the specification framed it as, and not as an adjudication —
`R1`–`R5` remain open, this task ruled on none of them, and whether some other
route exists is a question about the whole programme that this assessment did
not survey.

---

## Did the milestone make me want to overstep? — three temptations, answered

**The specification asks whether reading the milestone made me want to
estimate whether the residues vanish, to say which task should come first, or
to start building the projector. All three were live. Here is which, why, and
what I did.**

**Building the projector — the strongest of the three, and the most
dangerous.** `tt_check.py:105-126` already builds all four Barnes–Rivers
projectors. `project()` at `:129-135` already returns `g2, g1, g0s, g0w`. The
existing caller takes `[0]` and discards the rest. **Changing `[0]` to print
all four is a one-character edit against code that already exists, and it
would have produced numbers in the spin-1 and spin-0 channels within one
command.** I did not run it, did not modify it, and did not read its output.

**The reason matters more than the restraint.** Those numbers would have been
**one-loop free-fermion bubble values, not residues of an interacting
correlator** — the milestone's question is nonperturbative by the manuscript's
own `:809`, and `g1` and `g0s` from that script are contractions of a 1PI
kernel, not residues of anything. **The temptation was to produce a number
that looked like the answer and was a different quantity.** That is the
failure the specification's `DO NOT COMPUTE ANYTHING` is aimed at, and its
force here comes from the fact that the wrong number was one command away and
would have been reported in the right-sounding units.

**Estimating whether the residues vanish — declined at the same point and for
the same reason.** No residue was computed, estimated, or bounded. The artifact
states no expectation about whether they vanish, and §8 of the artifact says
so explicitly.

**Saying which task should come first — genuinely tempting, because the
argument for one order is easy to state.** §1 of the specification supplies it:
if the spin-1/0 residues do not vanish, a validated `−(k+2)` is a correct
coefficient for something that is not a graviton. **That is an argument about
what each task would establish, which §4 permits, and it is one sentence away
from an ordering, which §4 forbids.** I reported what each would establish —
under the first Rule 16 junction and in §1.1 of the artifact — and stopped
there. **No ordering appears in the artifact, in this report, or in any commit
message**, and A11's second search was run to check rather than to assert it.

**One further temptation the specification did not name, recorded because it
was real.** The verdict `TRACTABLE BUT BLOCKED PENDING A RULING` was available
and would have been a cleaner-looking result: four open R-nodes, name them,
done. **It would also have been wrong**, because six components are missing
independently of every ruling, and a reader told the task is "blocked pending a
ruling" would reasonably infer that a ruling unblocks it. §7.2 of the artifact
states why the not-yet-scoped verdict governs and records that the blocked
verdict applies in part rather than dropping it.

---

## Stops and clarifications

**One primary category per stop. Secondary findings reported separately.**

**`SPECIFICATION_DEFECT`** — none at stop level, and one repaired defect
recorded because the specification itself records it. A11's earlier draft
searched for *"any computed quantity"*, which A6, A12, A13, A15 and A16 all
require this report to contain — **a criterion a correct execution could not
satisfy, and the fourth such in this line.** The issued wording targets a
*newly computed or estimated scientific quantity belonging to this milestone*
and expressly excludes governance measurements. **It is satisfiable, and it was
satisfied.** No further defect was found.

**`ENVIRONMENT`** — `scipy` absent for the thirteenth consecutive task while
`pyproject.toml:12` declares `scipy>=1.11`; no validator imports it, so nothing
failed. **New this task: the contradiction is stated inside the repository.**
`scripts/recon2026/proca_curved.py:43-44` records *"``scipy`` is not a declared
package of this environment and is not installed"*, which contradicts the
manifest at the same commit. `docs/local/execution_environment.md` continues to
declare a Windows environment that has never executed this work. All recorded,
none repaired — §4 forbids modifying any existing file. **No environment
failure occurred, so neither of Rule 13's two diagnostic orders was exercised.**

**`OBSERVATION_METHOD_ERROR`** — none committed, **three avoided, and the
recurrence is the finding.** `Rivers` matches inside `drivers` in five of
twelve files; `pole` matches inside `tadpole` in twenty-four of sixty-seven
whole-tree files, six of ten `.py` files, and eight of nine `GATES.md` hits;
and `precede` matched `precedent` inside A11's own compliance search. **All
three were caught by opening the matched lines rather than reporting counts.**
Counting `Rivers` would have overstated the Barnes–Rivers machinery by 71%.
Counting `pole` in `GATES.md` would have returned nine hits for a term whose
true count there is one, and that one belongs to a different argument.
**Together with `CHANNEL-B0`'s `composition`/`decomposition`, this is the
fourth instance of one failure mode in two consecutive tasks: a substring of a
longer word inflating a search that decides a classification.**

**Secondary, same category:** every whole-tree count in this task was
initially inflated by exactly two, because this task's own specification and
review were in the tree and contain every search term. Reported as a
side-by-side pair — total, own, excluding-own — rather than as a single
number, so the reader can see the correction rather than take it on trust.

**`REPOSITORY_DEFECT`** — none newly found. Two standing observations
re-recorded rather than treated as settled: the `scipy` manifest
contradiction above; and that **two distinct functions named `projectors(q)`
exist in the same directory returning different objects** —
`tt_check.py:105`, four projectors, and `seagull_check.py:241`, one — which is
a name collision an importer cannot detect from the call site.

**The C3 multi-specification residual did not arise in this range** and its
absence is not evidence it is fixed: a scope task's range contains one
specification, so the conditions for it do not occur. Nothing in the checker
changed.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`** — one, reported and not
resolved. **`FIERZSUM-01 §5`'s doctrine is stated in general terms but was
written for `P2-VECPOLE-01`.** Whether it binds a tensor-channel task as frozen
governance, or only as a precedent a tensor-channel specification should
follow, is stated nowhere. **The artifact applied it as evidence about what
this class of test requires and did NOT treat it as a ruling on this
milestone.** Which it is belongs to the PI, and §4 forbids this task from
deciding it. §8's clause requiring a stop on an inconsistency between the
specification and a repository rule was not triggered: no such inconsistency
was found.

---

## Layering

**Everything above is measured at commit 3,
`b83a22fd5d8b882c137a413036e202353020019b`**, except A12's fourth path and
commit 4's message, both labelled **INTENDED**.

**Not in this file, returned to the Reviewer in chat:** A12's final scope
measured base-to-commit-4; A15-final, RUN 2 re-run at commit 4; A16 at commit
4; A17 for commit 4; the push; and the branch tip read back from command
output.

**This task does not touch `main`.** Integration is a separate task.
