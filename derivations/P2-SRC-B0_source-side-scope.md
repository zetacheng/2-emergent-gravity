# `P2-SRC-B0` — can this programme ask whether two configurations attract?

    STATUS      SCOPE AND DEPENDENCY ASSESSMENT. NOTHING IS COMPUTED HERE.
    BASE        0a7a988cb1c1ca7de4cbfebd46fd690245789a2d
    VERDICT     NOT PRESENT / EXTERNAL STATUS NOT DETERMINED

**This artifact determines whether the proposed source-side calculation can be
posed from repository materials, and what it would cost.** It computes no
stress tensor, no potential, no profile and no comparison, and it chooses no
tolerance. Where a number appears it is a value QUOTED from a repository file
with its line, never a value produced here.

## 1. The two sides, and which one this programme has built

**Every quantity this programme has computed lives on the LEFT side of the
field equation.** `Z` — defined at `CONVENTIONS.md:20` as the coefficient of
the induced Einstein–Hilbert term `∫√g R` — the species coefficients `β_s`,
and the ratio `β_V/β_B`. These describe the ELASTICITY of spacetime: how the
geometry responds.

**The RIGHT side is a different object.** A source. What curves the geometry
rather than what resists being curved.

**MEASURED over the whole tree, not over `derivations/` alone.** The
specification's author searched `derivations/` and measured zero on eight
terms. **The whole-tree search does not return zero**, and the difference is
the finding:

    TERM                 FILES   WHERE, AND WHAT THE HITS ACTUALLY ARE
    stress tensor            5   2 = this task's own spec and review
                                 2 = the manuscript and its recovered twin
                                 1 = results/recovered-2026/session_log_full.md
    energy-momentum          3   1 = this task's spec; 2 = manuscript + twin
    T_{mu nu}                1   this task's specification only
    T_mu_nu                  1   this task's review only
    source term              1   this task's specification only
    Einstein equation        3   1 = this task's spec; 2 = manuscript + twin
    field equation           3   1 = this task's spec; 2 = manuscript + twin
    geodesic                 1   this task's specification only
    test particle            1   this task's specification only
    Poisson                  3   1 = this task's spec; 2 = manuscript + twin
    Newtonian limit          7   1 = this task's spec; 2 = manuscript + twin;
                                 1 = session_log_full.md; and THREE governance
                                 or programme-text hits: GATES.md:1191,
                                 README.md:6, P2-CHANNEL-FREEZE-01:222

**EVERY NON-ZERO COUNT RESOLVES INTO ONE OF THREE CLASSES, AND NONE OF THE
THREE IS A REPOSITORY COMPUTATION:**

**Class 1 — this task's own specification and review.** Six of the eleven terms
appear ONLY here. The instruction to search installed its own vocabulary into
the corpus being searched, one commit before the search ran.

**Class 2 — the manuscript under verification**,
`paper/emergent_gr_paper_v2_15.tex`, and its recovered duplicate
`results/recovered-2026/emergent_gr_paper_v2_7.tex`, plus the recovered chat
log `results/recovered-2026/session_log_full.md`. **The manuscript is the
object being verified, not verified material.**

**Class 3 — three programme-text hits, all for `Newtonian limit` only:**

    README.md:6              "…Einstein-Hilbert term, Newtonian limit, and
                              induced gravitational source."
    GATES.md:1191            "…a headwind for a healthy Newtonian limit, not a
                              help: SI-2 is more likely to fail than to pass."
    P2-CHANNEL-FREEZE-01:222  the same sentence, in the gate's source artifact

**`README.md:6` names "induced gravitational source" as core scientific
responsibility of this repository.** **Nothing under `derivations/`,
`scripts/`, `tests/` or `results/` computes one.** The responsibility is
declared and unmet, and that is a repository-level observation rather than a
defect of any task.

**So the programme has never asked whether two configurations attract**, and
the whole-tree search sharpens rather than overturns that: what exists is a
manuscript that writes the right-hand side down, and no repository computation
that produces one.

## 2. What the manuscript does write down, and why it is not the missing piece

**The manuscript defines a fermionic energy-momentum tensor at
`paper/emergent_gr_paper_v2_15.tex:673-676`:**

> `T^{μν} = (i/4) ψ̄ γ^{(μ} ∂⃡^{ν)} ψ + h.c. − η^{μν} L`

coupled linearly as `(κ/2)∫ h_{μν} T^{μν}`, and at `:678-679` calls it "the
symmetric energy-momentum tensor of the fermions".

**THIS MATTERS FOR `§4`, AND IT IS NOT A CONDENSATE STRESS TENSOR.** It is the
EMT of the elementary fermion field, written as the linear source of `h_{μν}`
in the induced-gravity construction — the object whose CORRELATORS give `Γ^{(2)}`
and hence `Z`. It is an input to the left-side calculation, not an output of a
right-side one.

**At `:462-465` the manuscript is explicit about the direction of use:** the
graviton "resides in the symmetric, derivative bilinear sector — the
energy-momentum tensor — and is obtained by the induced-gravity route … one
couples the fermions to an external metric perturbation and reads off the
induced dynamics from the STRESS-TENSOR CORRELATORS."

**And the manuscript's own Newtonian-limit section takes the source as GIVEN.**
At `:1515-1523` it writes the linearized Einstein equation "sourced by a static
mass distribution `T^{00} = ρ(r)`" and reads off `∇²Φ_N = 4πGρ`. **`ρ` is an
input there. Nothing derives it from the condensate.** The section establishes
that the induced sector reproduces standard Newtonian gravity given a source;
it does not produce a source.

**That is precisely the gap the PI's question falls into.**

## 3. The first question: is a configuration available here?

**VERDICT: `NOT PRESENT / EXTERNAL STATUS NOT DETERMINED`.**

**MEASURED, whole-tree, by CONTENT and separately by FILENAME:**

    TERM              CONTENT FILES   FILENAME MATCHES
    sparc                         4                  0
    halo                          5                  0
    soliton                       1                  0
    domain wall / domain-wall   3/6                  0
    yukawa                        8                  0
    rotation curve                1                  0
    rotation-curve                2                  0
    profile                       8                  0
    r_c (as a token)              4                  0

**The Researcher measured "NO FILES MATCH" over filenames. That reproduces
exactly: zero filename matches on every term.** The content search is not zero,
and every content hit resolves as follows.

**`soliton`, `rotation curve` and the `r_c ∝ V_max^{0.82}` relation appear ONLY
in this task's own specification and review.** The scaling relation in
particular: a search for `0.82` as a standalone decimal over the whole tree
returns **one file — this task's specification, at its line 130, the sentence
that asks whether the relation exists.** It is the only occurrence in the
repository.

**`sparc`, `halo` and `yukawa` appear in the manuscript, and ONLY as references
to Paper 1**, which is a separate repository and a manuscript in preparation:

    paper:206-208   "In Ref. [Cheng:2025sparc], we derived a Yukawa-type dark
                     matter halo profile from the scalar sector of the same
                     lattice fermion framework and tested it against 175 SPARC
                     galaxies."
    paper:1813-1817  bibliography: Z. H.-H. Cheng, "Emergent Yukawa Dark Matter
                     Halos from a Lattice Fermion Condensate: Fits to 175 SPARC
                     Galaxies," in preparation (2026).

**NO PROFILE FUNCTION, NO PARAMETER VALUES, NO FITTED POTENTIAL AND NO
`r_c`-SCALING RELATION ARE PRESENT.** What is present is a citation, a
one-sentence description, and a title.

**AND THE PROVENANCE CANNOT BE SETTLED FROM THEM — WHICH IS A MEASUREMENT, NOT
A CONCESSION.** The repository's own description of the cited work contains
**both** words: the body text at `:206` says "we DERIVED a Yukawa-type dark
matter halo profile … and TESTED it against 175 SPARC galaxies", while the
bibliography title at `:1816` says "FITS to 175 SPARC Galaxies". **A rule that
a title cannot settle provenance is usually a caution about inference. Here it
is a fact about the evidence: the two in-repository descriptions of the same
work point in opposite directions.**

**THIS TASK THEREFORE DOES NOT DETERMINE WHETHER THE EXTERNAL CONFIGURATION IS
DERIVED OR FITTED, AND DOES NOT CHARACTERISE IT.**

**THE PROPOSED SOURCE-SIDE CALCULATION CANNOT PRESENTLY BE EXECUTED FROM
REPOSITORY MATERIALS.** There is no configuration here to compute a `T_μν` of.

**What would have to land** — named because naming it is the useful part of a
`NOT PRESENT` finding:

    1  the condensate configuration itself: the profile as a function, with
       the equations it solves and the boundary conditions it satisfies
    2  its provenance record: derived from the field equations, or fitted, and
       to what data — stated by whoever lands it, not inferred here
    3  the potential or observable Paper 1 compares against, in a form this
       repository can read
    4  the r_c scaling relation, if it is to be part of the comparison

**AND `NOT PRESENT` IS A STATEMENT ABOUT THIS REPOSITORY. IT IS NOT A
STATEMENT THAT THE PHYSICS IS WRONG.**

## 4. Would `T_μν` need the measure `DET-01` left unfixed?

### 4.1 It depends on WHICH `T_μν`, and the repository supports two different objects

**`T_μν = (2/√g) δΓ/δg^{μν}` requires `Γ`.** `DET-01` established, and the
landed artifact records, that the functional measure is `NOT DETERMINABLE` from
the frozen conventions: `Γ = ½ log det K − ½ log det 𝔊` with `𝔊` unspecified.
**So a stress tensor defined from the full quantum effective action inherits
the unfixed measure. That is a true statement about that object.**

**IT IS NOT A UNIVERSAL THEOREM, AND THE REPOSITORY ITSELF SUPPLIES THE
COUNTEREXAMPLE.** The manuscript's `T^{μν}` at `:673-676` is a bilinear
OPERATOR built from the classical action — a metric variation of `S`, not of
`Γ`. **A classical stress tensor obtained by varying a classical action needs
no functional measure at all.**

**SO THE ANSWER IS CONDITIONAL, AND THE CONDITION IS WHICH OBJECT THE
CALCULATION USES:**

    Γ-DEFINED  T_μν = (2/√g) δΓ/δg^{μν}     REQUIRES the unfixed measure
    S-DEFINED  T_μν = (2/√g) δS/δg^{μν}     DOES NOT

**Which one the proposed calculation needs is not settled by this assessment**,
because it depends on a configuration that is not here. **A one-loop condensate
lump computed as a quantum expectation value takes the first road; a classical
soliton solution of a stated effective action takes the second.**

### 4.2 The rider does NOT carry over, and here is the derivation

**`DET-01`'s rider was proved for the `m² ln m²` coefficient of `Z`.** Two
candidate measures differ by an ultralocal `Σₓ F(g(x))`, which lands at `q⁰`
rather than `q²` and carries no `m`. **That argument says nothing about the
metric VARIATION of the same term, and the variation is not zero.**

**DERIVED, symbolically, `sympy` 1.14.0, over a general symmetric `4×4` inverse
metric of ten free symbols.** For the case `DET-01` established — `det G1 = ∏ₓ
det g(x)` in four dimensions, so the candidate difference is
`±½ Σₓ log det g(x)` — take `F(g) = ½ log det g`:

    δ/δg^{μν}(y)  Σₓ F(g(x))  =  [ ∂F/∂g^{μν} ](y) · δ_{x,y}      ULTRALOCAL

    ∂/∂g^{μν} [ ½ log det g ]  =  − ½ g_{μν}                       NOT ZERO

**Every component of the symbolic derivative matched the closed form
`−½ g_{μν}`, with zero residual.**

**THE STRUCTURE OF THE RESULT IS THE POINT.** The variation is

- **not zero** — so the ambiguity DOES reach a stress tensor defined from `Γ`;
- **still ultralocal** — a `δ_{x,y}`, no derivatives of the metric;
- **proportional to `g_{μν}` itself** — which is the form of a
  cosmological-constant / vacuum stress tensor, `T_μν ∝ g_{μν}`;
- **independent of the condensate** — `F` is a function of the metric alone.
  **The term is identical for a lump and for the vacuum around it, at the same
  metric.**

**SO THE AMBIGUITY ENTERS THE SOURCE OBSERVABLE AS AN UNDETERMINED VACUUM-LIKE
TERM.** That is exactly where `DET-01` said the unfixed measure would land — the
absolute `Γ` and the induced cosmological constant — now reached from the source
side rather than the coefficient side. **`DET-01`'s conclusion and this one
agree, and they are different derivations of different objects.**

**This does NOT settle the measure question and does not choose a `𝔊`.**

### 4.3 Could a background-subtracted stress tensor remove it?

**ALGEBRAICALLY, AT FIXED METRIC, YES — AND THAT IS THE SMALLER HALF OF THE
ANSWER.** Because the term depends on `g(x)` alone and not on the configuration,
a difference taken between two configurations AT THE SAME METRIC cancels it
identically. Nothing about ultralocality alone gives this; it is the
configuration-independence that does.

**GOVERNANCE-WISE, NO SUCH PRESCRIPTION IS AVAILABLE, AND THE REPOSITORY HAS
ALREADY REFUSED THE PARTICULAR USE THE PROPOSED CALCULATION WOULD NEED.**

**MEASURED. No frozen subtraction prescription exists:**

    P2-LATTICE-ONTOLOGY-01.md:191   "| Reference equivalence class and matching
                                     conditions | DELEGATED: FIERZSUM §4.2 /
                                     D-pre |"
    P2-LATTICE-ONTOLOGY-01.md:256   the renormalization deliverable "collapses
                                     into a finite, explicit subtraction-and-
                                     matching rule, which FIERZSUM MUST STILL
                                     FREEZE"

**AND THE FROZEN GOVERNANCE SEPARATION IS DIRECTLY ADVERSE**, at
`P2-LATTICE-ONTOLOGY-01.md:289-292`:

> "**Governance separation (frozen):** the response subtraction of `§2`
> authorizes removing the common baseline from RESPONSE observables only; it
> does not authorize deleting the substrate energy from the cosmological
> SOURCE."

**The subtraction that exists in the repository is authorised for response
observables — the left side — and is EXPRESSLY NOT authorised for a source
observable.** The proposed calculation needs a source observable. **So the
subtraction it would rely on is not merely unfrozen; the one thing the
repository has frozen about it is that it does not extend there.**

**A SECOND DEPENDENCY IS ALSO ALREADY ON RECORD**, at
`P2-LATTICE-ROUTE-01.md:247-248`: among the things a later gate must verify is
"whether the flat/reference subtraction is applied before or after `∂/∂G`; and
whether the derivative and the subtraction commute." **Subtract-then-vary and
vary-then-subtract are the two orders the proposed calculation would have to
choose between, and the repository records that the choice is open.**

**DEPENDENCY, THEREFORE: defining an explicit subtraction-and-matching rule
that covers SOURCE observables, and fixing the order in which it composes with
`δ/δg`, is a prerequisite of the proposed calculation.** Neither is done, and
one of them is currently forbidden by a frozen separation rather than merely
absent.

### 4.4 The rider's dimensional scope

**MEASURED, not transcribed. The general relation follows from two determinant
identities — `det(cM) = c^d det M` and `det(M⁻¹) = 1/det M`:**

    det[ √(det g) · g⁻¹ ] = (√(det g))^d · (det g)⁻¹ = (det g)^{d/2 − 1}

**Confirmed symbolically in full at `d = 2` and `d = 3` (residual exactly `0`),
and numerically on random symmetric positive-definite matrices at `d = 4, 5, 6`
(worst relative deviation `3.6e-15`).**

    d = 2   (det g)^0    = 1          G1 CARRIES NO DETERMINANT AT ALL
    d = 3   (det g)^{1/2}
    d = 4   (det g)^1    = det g      the DET-01 relation
    d = 5   (det g)^{3/2}
    d = 6   (det g)^2

**`d = 4` IS THE ONLY DIMENSION IN WHICH THE RELATION IS `det g`.** At `d = 2`
it is identically `1` — **the rider is EMPTY there, not approximately true**:
there is no `det G1` ambiguity to be ultralocal about, because the
determinant is unity for every metric.

**`RECON-01a`'s construction hard-codes `d = 4`** (`scripts/recon2026/proca_curved.py:52`
sets `DIM = 4`, and every operator in that module is built on it), **so the equality is a property of that
construction, not a general identity.**

**DOES THE LANDED ARTIFACT STATE THE QUALIFIER? YES, ONCE, AND ONLY INSIDE THE
ALGEBRA.** `derivations/P2-BETAV-DET-01_measure-adjudication.md:64` reads "and
per site, with `g ≡ det g_{μν}` and `√g = g^{1/2}` in four dimensions," followed
at `:66` by `det[√g g⁻¹] = (√g)^4 · det(g⁻¹) = g² · g⁻¹ = g`. **The `(√g)^4`
carries the dimension. But the artifact's headline statements of the rider — at
`:24` and at `:302` — carry no dimensional qualifier at all**, and a reader who
reads the rider and not the algebra would take `det G1 = ∏ₓ det g(x)` for a
general identity. **It is not one.**

## 5. Could the comparison avoid an absolute `G_ind`?

**FINDING: NO REPOSITORY-GROUNDED DIMENSIONLESS COMPARISON HAS BEEN
ESTABLISHED. This is not the same as saying none could exist.**

**The absolute route is blocked, and the blockers are already measured**, in
`derivations/P2-BETAV-RECON-01_scope-assessment.md` `§A8b`:

    R5   internal multiplicity N.  CONVENTIONS.md:20 defines Z per unit 4N and
         Z ≡ 1/(16πG_ind).  "Converting a per-4N coefficient into an induced G
         requires N."  R5 is open — P2-CHANNEL-FREEZE-01_phaseA_freeze.md:43
         keeps N symbolic.
    R1   canonical kinetic operator and species accounting, DELEGATED to D-pre
         at P2-LATTICE-ONTOLOGY-01.md:189.

**So a comparison that needs an absolute `G_ind` inherits `R5` and `R1`.**

**A dimensionless comparison would not inherit them** — `§A8a` of the same
artifact records that the RATIO depends on none of `R1`–`R5`, and `R5` in
particular "CANCELS in a ratio of two species coefficients both reported per
unit `4N`". **The ratio-side precedent shows the escape route is real in
principle.**

**BUT NO CONCRETE DIMENSIONLESS OBSERVABLE CAN BE CONSTRUCTED FROM WHAT IS
HERE, FOR TWO INDEPENDENT REASONS:**

**First, a comparison needs two sides, and the source side is absent.** A
shape-only comparison — `Φ(r)/Φ(r₀)` against `r/r_c` — still requires the
computed profile and the reference profile, and `§3` measured that neither is
present.

**Second, the only length scale the repository names on the computed side is
imported from the data the comparison would test.** `paper:613-615` states "The
static field equation of `θ̃` is that of a massive scalar, with Yukawa Green's
function of range `r_c = 1/m_θ`" — and `:618-620` then fixes `m_θ` FROM the
observed scale: the "SPARC-scale cutoff radii `r_c ∼ 10 kpc` correspond to
`m_θ ∼ 10⁻²⁷ eV`". **(Both figures are QUOTED from those lines; nothing is
computed here.)** **The direction of that inference runs phenomenology →
parameter.** Using `r_c` as the computed side's own scale would put the
measured quantity into the prediction, which is the circularity the whole
assessment exists to detect.

**A third fact bears on it and is on record in the manuscript itself**, at
`:633-643`: the coupling of the angular mode to baryonic matter "remains open",
is "deferred to future work", and in the cited work "the coupling is treated as
an effective parameter". **A comparison of potentials needs that coupling, and
the manuscript records it as not established.**

**THEREFORE: the calculation as proposed inherits `R1` and `R5` if made
absolutely, and cannot yet be made dimensionlessly, because the objects a
dimensionless observable would be built from are not in this repository.**

## 6. What a failure criterion would have to fix

**NOTHING IS CHOSEN HERE. Choosing is a PI ruling.** What follows is the list
of what a pre-registration must fix, and it must be fixed BEFORE the number is
seen.

    1  THE COMPARED QUANTITY.  Not "the potential" — a specific functional of
       it, evaluated at a specific place, in specific units, on both sides:
       the value at a stated radius; the logarithmic slope over a stated
       interval; the ratio of two radii; the shape after a stated
       normalisation.  Both sides must be the SAME functional.
    2  THE TOLERANCE.  A number, with the metric it is measured in — relative,
       absolute, in units of a stated uncertainty — and the uncertainty's own
       source, since neither side currently carries one.
    3  THE DIRECTION.  Which outcome is failure.  A two-sided band, a one-sided
       bound, or a sign requirement.  Also which side is the prediction.

**AND THE REASON THIS IS NOT PEDANTRY:**

**A COMPARISON WITHOUT A FIXED TOLERANCE IS NOT A TEST.** It is a measurement
followed by a judgement, and the judgement is made by someone who has already
seen the measurement.

**THE FACTOR-OF-THREE CASE IS THE CLEAN EXAMPLE.** A factor-of-three
disagreement can be read as "same order of magnitude — success for a
first-principles calculation with no free parameters", or as "wrong by a factor
of three". **Both readings are defensible, and which one wins is decided after
the number is seen unless the criterion is fixed first.** Fixing it first costs
nothing and is the only thing that distinguishes a test from a
rationalisation.

## 7. Component inventory

**Classified into exactly one of four mutually exclusive states.** An
implementation counts only if it is POTENTIALLY APPLICABLE to this calculation.

    #   COMPONENT                                        STATE
    1   metric-coupled lattice operator machinery         IMPLEMENTATION + SPEC
        (√g g⁻¹ factors, K1, G1, D1 on a weak-field
        background) — scripts/recon2026/proca_curved.py
        and flat_validation.py, specified by
        P2-BETAV-RECON-01a §C1–C6
    2   a validator / regression harness able to check    IMPLEMENTATION ONLY
        whatever is built — tests/ (332 validators) and
        scripts/governance_tools/
    3   the definition of a stress tensor for a matter    SPECIFICATION ONLY
        configuration — paper:673-676 states the fermion
        EMT operator form; nothing computes it
    4   a localized condensate configuration             NEITHER
    5   the functional measure needed by a Γ-defined      NEITHER
        T_μν — DET-01: NOT DETERMINABLE
    6   an explicit subtraction-and-matching rule that    NEITHER
        covers SOURCE observables, with its composition
        order against δ/δg fixed
    7   the absolute induced G — needs R5 (N symbolic)   NEITHER
        and R1 (species accounting, delegated)
    8   the geometry map {t_ij} ↔ g, e, ω —              NEITHER
        DELEGATED to D-pre at ONTOLOGY:190; :134 records
        that the lattice degrees of freedom corresponding
        to the metric are "still to be identified"
    9   a solver taking a source to a field or potential  NEITHER
    10  Paper 1's potential, profile, or r_c relation     NEITHER
    11  a pre-registered failure criterion                NEITHER

    N_both    = 1
    N_impl    = 1
    N_spec    = 1
    N_neither = 8
    N_total   = 1 + 1 + 1 + 8 = 11

**A NOTE ON COMPONENT 9, BECAUSE THE LEXICAL SEARCH LOOKS LIKE A HIT.**
`scripts/p2_phase01_scalar_exploratory.py:112` defines
`reconstructed_potential`, and `scripts/p2_phase01_fierz_and_depths.py` calls
it six times. **That is the effective potential `V_eff` of the scalar/Fierz
analysis — a thermodynamic potential in field space, not a gravitational
potential in position space.** Counting it would have inflated readiness by
matching a word.

**A NOTE ON COMPONENT 8, WHICH IS EASY TO OVERLOOK.** The metric in
`RECON-01a`'s construction is an INPUT — a background `g = δ + h` supplied by
hand. **It is not an emergent quantity built from lattice variables**, and the
map that would make it one is delegated and unwritten. **A source-side
calculation that produced `T_μν` for a lattice condensate would still have no
frozen way to say which geometry that condensate lives in.**

**AND THE COUNT IS NOT A DIFFICULTY.** Eleven components with eight missing is
an inventory, not an estimate. Some of the eight may be short; component 5 is a
question `DET-01` proved cannot be answered from the present conventions at
all. **The count says what is absent. It does not say what it would cost, and
this artifact does not estimate that.**

## 8. What this assessment does NOT establish

**It does not establish that the physics is wrong.** `NOT PRESENT` is a fact
about this repository on 2026-08-18. **What would change it is listed in `§3`.**

**It does not establish anything about Paper 1.** That is a separate repository
and a manuscript in preparation. **A configuration existing there is not a
configuration available here**, and `§3` measured that this repository's own two
descriptions of it disagree about whether it was derived or fitted.

**It does not establish that the PI's question is the same question this
programme has been answering.** **The programme computes the coefficient of
`∫√g R`. The PI asked for a solution with a source.** Both are legitimate
physics questions about the same theory. **Only the first has been attempted**,
and `README.md:6` shows the second was in scope from the beginning.

**It does not establish that a homogeneous vacuum fails to gravitate.** A
homogeneous Lorentz-invariant vacuum contributes a cosmological-constant-type
stress tensor. **It does not provide the localized, clustering source the
proposed halo test requires — and that is NOT the same as having no
gravitational effect, which would be false**; a positive `Λ` produces de
Sitter-type relative acceleration. **The proposed calculation therefore probes
the condensate's INHOMOGENEOUS sector**, and **a null result there would say
nothing about the vacuum sector, which `DET-01` left unfixed** — and which `§4.2`
has now shown is exactly where the measure ambiguity enters a stress tensor.

**It does not establish that a posable calculation would succeed.** Finding
that a calculation can be posed says nothing about the value it would return.

## 9. Stops and clarifications

**No stop was declared.**

**`SPECIFICATION_DEFECT` — none found in this specification.** The `§0`
measurement it reports for `derivations/` reproduces; the whole-tree figures
differ, and `A4` anticipated exactly that and required the difference reported.

**`REPOSITORY_DEFECT` — `README.md:6` declares "induced gravitational source"
as core scientific responsibility, and no repository computation addresses
it.** Recorded as an observation about programme scope, not attributed to any
task.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the landed `DET-01` artifact
states the rider without its dimensional qualifier at `:24` and `:302`**, and
carries `in four dimensions` only inside the algebra at `:64`. **Not repaired
here; this task modifies nothing.**

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the self-referential search
hazard, again.** Six of `A4`'s eleven terms, and three of `A5`'s, occur ONLY in
this task's own committed specification and review, which were committed before
the searches ran. **The `r_c ∝ V_max^{0.82}` relation exists in exactly one file
in the repository: the sentence asking whether it exists.**
