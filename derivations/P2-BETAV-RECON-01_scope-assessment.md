# `P2-BETAV-RECON-01` — scope assessment

**This file measures what a clean-room Proca reconstruction would require. IT
BUILDS NOTHING AND COMPUTES NOTHING.** No operator was constructed, no
derivative taken, no scan run, and **no script named below was executed.**

**A component count is not a difficulty**, and this assessment measures
existence, not difficulty. **It does not adjudicate whether the historical
pipeline is circular**, does not open or make any of `R1`–`R5`, and does not
write the `RECON-01` specification.

    evidence base   ece34f7bacbbee00efa0fecf0be644d593eed72f

---

## 1. The gate, quoted

**`P2-BETAV-RECON-01`, `GATES.md:725`–`789`. Read scoped to the section.**

    Status              (:727)   PROPOSED (not run; distinct from the historical
                                 circularity question)

    Scope               (:737-740)
        1-form operator `Δ^{(1)}[g,h]` + compensating scalar `Δ^{(0)}[g,h]` on a
        weak-field background; `Γ_k=½logdetΔ^{(1)}−(k/2)logdetΔ^{(0)}`; numerical
        `h`-derivatives at the determinant/eigenvalue level; fixed axis-TT projection;
        vary only `k∈{0,1,2,3,½}`.

    Analytic anchors    (:751)   `β_V/β_B = −(k+2)` (from `P2-HK-01`), compared only
                                 at the end.

    Regression anchors  (:754)   None yet (proposed).

    Kill criterion      (:757-759)
        For the reconstruction itself: stuck at `−3` ∀k ⟹ the new pipeline is degenerate
        (a bug); drift toward `−5` at heavy mass ⟹ longitudinal artifact. None of these
        closes `P2-BETAV-CIRC-01`.

**What the gate says a successful reconstruction does NOT show, `:731-734`,
verbatim:**

> **Scope label: a 2026 reconstructed pipeline, NOT a test of the historical
> Finding 5 implementation.** A faithful reconstruction returning `−(k+2)`
> shows only that the reconstruction is correct; it does not show the
> historical pipeline was non-circular.

**A sign discrepancy, recorded and not resolved here.** The gate writes the
anchor as `−(k+2)` and the kill criteria as `−3` and `−5`. **The specification
governing this assessment writes them unsigned** — `(k+2)`, `3`, `5`. **The
gate's signed form is the repository's, and it is what is quoted above.** No
value is recomputed here and the discrepancy is reported, not adjudicated.

## 2. The eleven scripts

**Every one was READ. NONE was executed.** Classification is
`starting point` / `check` / `neither` **as a clean-room component**, which is
a different question from `§4`'s existence states.

### 2.1 `scripts/recovered_2026/proca_loop.py` — 173 lines

**Computes** the universal `m² ln m²` coefficient of a massive vector coupled
to a background metric. **METRIC-COUPLED**, and explicitly so: `geomV(h)`
builds `g = 1 + h` and forms `J2 = √g · g⁻¹⊗g⁻¹`, `J = √g · g⁻¹`, both
described in its docstring as *exact*. Its docstring also states the flat
kernel and its eigenvalues, and that the longitudinal lattice mode has exactly
no kinetic term, so *"the compensating-scalar structure of the Proca
determinant is built in"*.

**This is the single most consequential finding of `§3`'s question one.**

**Reuse: `check`, NOT a starting point. Reuse as a component WOULD compromise
the clean-room label**, on two independent grounds. First, it *is* the
recovered historical pipeline — `GATES.md:376` names it as such — so importing
its operator imports what the label excludes. Second, **its docstring embeds
the analytic ratio target**, which is the blind-harness hazard `GATES.md:415-418`
records: *"the historical drivers embed the analytic targets … in
comments/docstrings, so the target must be stripped from the driver and the
number frozen before any comparison."*

**What it could check:** the flat limit. A new operator's flat eigenstructure
can be compared against what this one produces — a comparison, not a copy.

**One correction to a common reading, and it matters here.** `CIRC-01`'s
`DECOMP-UNAVAILABLE-AS-RECOVERED` finding is about the recovered **`boson_loop`
scalar** — `GATES.md:382-385`: *"the recovered `boson_loop` scalar (`Δ₀=ŝ²+m²`,
propagating) is **not** the flat Proca longitudinal eigenfactor (`m²`,
ultralocal)"*. **It is not a finding that `proca_loop.py` mis-builds its own
longitudinal band.** The specification's `§2` says `CIRC-01` *"found its scalar
factor is not the Proca longitudinal eigenfactor"*; **the scalar in question is
the external one, from a different script.**

### 2.2 `scripts/recovered_2026/boson_loop.py` — 179 lines

**Computes** the condensate-boson (real scalar) one-loop contribution to the
induced graviton kernel. **METRIC-COUPLED**: `geomB(h)`, `J = √g g⁻¹` exact,
kernel from *"bubble + seagull, vertices from exact numerical derivatives of
J(h), edet(h); validated against constant-h second differences."*

**Reuse: `check`.** Same clean-room objection as `§2.1` — recovered pipeline
code. **And a second, sharper one:** this is the operator `CIRC-01` found is
not the Proca longitudinal eigenfactor, so **using it as the compensating
scalar is precisely the substitution `CIRC-01` ruled unavailable.**

### 2.3 `scripts/recovered_2026/batch2/gfvec_loop.py` — 269 lines

**Computes** a gauge-fixed *minimal* lattice vector, adding
`S_gf = ½ Σ E B²` so the operator becomes the minimal `Δ^{(1)} + m²` with **no
longitudinal flat band**, and uses the Solodukhin determinant identity
`Γ_Proca = Γ_minvec − Γ_scalar(m)`. **METRIC-COUPLED**: `E = 1/√g`,
`J = √g g⁻¹`, with first and second `h`-derivatives of both.

**Its machinery is validated at constant `h`** — `GATES.md:403-405` records
perturbative bubble+seagull against exact `ln det` agreeing to `~1e-7`.

**Reuse: `check`.** **Its docstring embeds two sharp analytic targets**, so as
a component it carries the same blind-harness defect. **As a check it is the
strongest of the eleven**: a constant-`h` exact-`ln det` comparison is exactly
the kind of validation a new pipeline needs and does not presuppose the new
pipeline's construction.

### 2.4 `scripts/recovered_2026/reproduce_betav.py` — 125 lines

**Computes** nothing new: it is a driver that runs the recovered pipeline
against pre-registered paper targets. **FLAT/driver — it constructs no
operator.** **Its docstring enumerates the targets, including the heavy-mass
drift the gate names as a kill criterion.**

**Reuse: `neither`.** It is a target-bearing driver for the historical
pipeline. **Reuse would compromise the clean-room label completely** and it
offers nothing a check needs.

### 2.5 `scripts/betav_discriminating.py` — 102 lines

**Computes**, at the ANALYTIC layer, whether the ratio is structure-dependent:
it feeds a modified determinant structure `det^{−1/2}(Δ^{(1)}+m²) ·
det^{+1/2}(Δ^{(0)}+m²)^k` through the Seeley–DeWitt `a₁` route and reports the
induced ratio's `k`-dependence. **FLAT / continuum — no metric coupling, no
lattice operator.**

**Reuse: `check`.** It is the analytic layer the reconstruction is compared
against at the end, and **it does not construct anything the clean-room
pipeline would build**, so using it does not compromise the label. **It is the
anchor's derivation, not the pipeline.**

### 2.6 `scripts/betav_decomp_check.py` — 178 lines

**Computes** operator-level checks of the recovered determinant: the flat Proca
kernel eigenstructure, that the longitudinal eigenvalue is exactly `m²` and
ultralocal while the external scalar is propagating, and the propagator
eigenvalues. **FLAT — it reads the flat kernels of the recovered operators.**
**Its docstring states `NO k-scan, NO target`.**

**Reuse: `check`, and it is the natural flat-limit harness.** **It carries no
target**, so reusing it does not import the blind-harness defect. **What it
would compromise is narrower:** it reads the *recovered* operators, so a new
pipeline must supply its own kernel and use this only as the comparison
recipe.

### 2.7 `scripts/betav_decomp_q2.py` — 180 lines

**Computes** a `q²`-level transverse/longitudinal sector decomposition of the
Proca bubble, with projectors built INDEPENDENTLY from `a(k)` and `a(k+q)`, and
reports small-`q` scaling exponents **without fitting toward any supplied
value**. **FLAT background, `q`-dependent.** Docstring: *"still NO k-scan, NO
target"*, and it carries a pre-registered protocol fixed before running.

**Reuse: `check`.** **It is the artifact that superseded a withdrawn
same-basis figure**, and its projector-independence discipline is directly
relevant to the reconstruction's fixed-projection requirement. **No target, so
no blind-harness compromise.**

### 2.8 `scripts/betav_assembly.py` — 157 lines

**Computes** the determinant-bookkeeping regression: given the shared scalar
lattice tadpole and the Proca determinant powers, does the assembly preserve
the `k`-dependence with no hardcoded value. **FLAT / analytic bookkeeping** —
it composes species prefactors and one shared tadpole coefficient; **it builds
no metric-coupled operator.** Its own docstring states it is **NOT** the
`CIRC-01` circularity test.

**Reuse: `check`.** It is the `k`-dependence bookkeeping the reconstruction's
own `Γ_k` must agree with, at a layer above the operator. **Its docstring
states the ratio formula**, so a blind harness must not import it into the
measuring stage.

### 2.9 `scripts/hk_species.py` — 178 lines

**Computes**, symbolically, the species coefficients from the Seeley–DeWitt
expansion and the convention-independent ratios. **CONTINUUM, symbolic — no
lattice, no metric perturbation.** Its docstring states it *"contains no paper
value and is not tuned toward one"* and that conventions are locked in
`CONVENTIONS.md`.

**Reuse: `check`.** **This is where the anchor comes from.** It is not part of
the pipeline and cannot compromise the clean-room label; it is the thing the
pipeline is compared to, at the end.

### 2.10 `scripts/P2-BETAV-CAMPAIGN/harness_compute.py` — 428 lines

**Computes** raw `Z(m)` tables and fitted betas per species/variant to frozen
JSON with an EXTERNAL sha256 sidecar. **Contains NO target numbers and prints
no ratios, verdicts or bands.** **FLAT with respect to this question — it is
harness infrastructure, not an operator**, though it imports the recovered
scientific functions.

**Reuse: `starting point`, with one qualification.** **Its architecture is
what a clean-room reconstruction needs** — blind compute stage, frozen output,
external digest, comparison deferred. **Its imports are what would compromise
the label:** it *"imports the recovered scientific functions (never their
target-bearing docstrings / drivers)"*, and a clean-room pipeline must supply
its own functions in their place. **The harness is reusable; what it currently
computes with is not.**

### 2.11 `scripts/P2-BETAV-CAMPAIGN/compare.py` — 447 lines

**Computes** nothing physical: it is the comparison/acceptance stage, refusing
to run unless five integrity checks pass, then applying pre-registered
acceptance rules and emitting a verdict with a two-field exit-code contract.
**By design the target numbers and bands live here** — it is the non-blind
stage.

**Reuse: `starting point`**, for the same architectural reason and with the
same qualification: **its rules and bands are the campaign's, not the
reconstruction's**, and the reconstruction's tolerance is a different quantity
(`§4`, component 9).

### 2.12 The counts

    starting point    2     harness_compute.py, compare.py
    check             8     proca_loop, boson_loop, gfvec_loop, betav_discriminating,
                            betav_decomp_check, betav_decomp_q2, betav_assembly,
                            hk_species
    neither           1     reproduce_betav.py
                     --
                     11

**MEASURED: NONE of the eleven was executed.**

**Six of the eleven embed a target or a target formula in docstrings or code**
— `proca_loop`, `gfvec_loop`, `reproduce_betav`, `betav_discriminating`,
`betav_assembly`, `compare` — **and three explicitly state that they carry
none** — `betav_decomp_check`, `betav_decomp_q2`, `harness_compute`.
**That split is the practical content of the clean-room label.**

## 3. The five questions

### 3.1 Question one — is `Δ⁽¹⁾[g,h]` defined anywhere, or must it be constructed?

**Where I searched:** `derivations/`, `scripts/`, `GATES.md` and
`CONVENTIONS.md`, for the `Δ^{(1)}` notation; and separately for the
metric-coupled construction itself — `geom*` functions, `√g g⁻¹` factors,
weak-field `g = 1 + h`.

**MEASURED — the notation appears in eleven places** across five derivations
(`P2-BETAV-CIRC-01_determinant-decomposition`, `P2-BETAV-RECON-01_cleanroom_reconstruction`,
`betav_discriminating_power`, `P2-HK-01_heat_kernel_species`,
`P2-BETAV-ASSEMBLY-01_bookkeeping_regression`), two scripts
(`gfvec_loop.py`, `betav_assembly.py` — plus `betav_discriminating.py`),
`scripts/recovered_2026/PROVENANCE.md`, `GATES.md` and `CONVENTIONS.md`.

**THE ANSWER IS NOT "NOT PRESENT", and it is not "present" either. It is
present in three different senses that must be kept apart.**

**As a DEFINED OPERATOR: `CONVENTIONS.md:19` fixes it.**

> `Z_{s=1,m} = det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)`, with the vector
> Laplacian `Δ^{(1)}` having `E^{μ}{}_{ν}=R^{μ}{}_{ν}` (`tr E = R`) and the
> Stueckelberg scalar `Δ^{(0)}` having `E=0`.

**That is a continuum, curvature-level definition, frozen. It is not a lattice
construction.**

**As a LATTICE IMPLEMENTATION: `scripts/recovered_2026/proca_loop.py` builds
one**, metric-coupled, with exact `√g g⁻¹⊗g⁻¹` geometric factors and a
weak-field `g = 1 + h`; `batch2/gfvec_loop.py` builds the gauge-fixed minimal
variant. **So a metric-coupled 1-form operator exists as recovered code.**

**As a SYMBOLIC FIRST-ORDER VARIATION `δΔ^{(1)}[g,h]`: MEASURED, NOT PRESENT.**
No derivation in `derivations/` defines the first-order variation of the
operator in `h` symbolically. **The recovered scripts obtain their vertices by
exact NUMERICAL derivatives of the geometric factors, not from a written
variation.**

**The consequence for scope, and it is not the consequence "NOT PRESENT" would
have had.** The reconstruction does not need `Δ⁽¹⁾` invented from nothing —
its continuum definition is frozen and a lattice realisation exists to compare
against. **What it needs is a NEW lattice realisation that does not import the
recovered one**, because the recovered one is the object the clean-room label
excludes. **Existence is not availability.**

### 3.2 Question two — what must the flat limit reproduce, and is it stated?

**MEASURED: the flat Proca eigenstructure is stated in three places, in
compatible notations:**

    derivations/betav_discriminating_power.md:21   `{ŝ²+m²(×3), m²}`
    scripts/betav_decomp_check.py:7               `{p̂²+m² (×3), m² (×1)}`
    scripts/recovered_2026/proca_loop.py:12       `{shat^2+m^2 (x3 transverse), m^2 (x1 longitudinal)}`

**And `betav_decomp_check.py` states two further flat facts a validation would
use:** the longitudinal eigenvalue is exactly `m²` and invariant under `p̂²`
(ultralocal), and the propagator eigenvalues are transverse `1/(p̂²+m²)`,
longitudinal `1/m²`.

**IS IT STATED PRECISELY ENOUGH TO TEST AGAINST? For the EIGENSTRUCTURE, YES.**
Multiplicities, both eigenvalues and the ultralocality of the longitudinal
band are all written down, in a derivation and in a target-free script.

**AS A REGISTERED REGRESSION TARGET, NO — and the gate says so itself.**
`GATES.md:754`: `Regression anchors — None yet (proposed).` **The eigenstructure
is stated in the repository; it is not registered as this gate's regression
anchor.**

**So stating it is not part of the work; REGISTERING it is.** That is a
narrower deliverable than "state the flat-limit target", and the difference
matters to scope: **the physics content exists and the pre-registration does
not.**

**What is NOT stated anywhere I found: a numerical tolerance for the flat-limit
comparison.** The `RECON-01` derivation states the *form* the tolerance must
take — a propagated ratio error, numerator and denominator correlated through
a shared momentum grid — **but no value or rule.** `§4`, component 9.

### 3.3 Question three — the anchor's dependencies, TWO SEPARATE VERDICTS

**First, the conventions.** **MEASURED: `P2-HK-01`'s `a₁` conventions ARE
FROZEN in `CONVENTIONS.md`.**

    :16   `a_1 = tr[(1/6)R·𝟙 − E]` — the R-linear Seeley–DeWitt coefficient,
          with the heat-kernel expansion and d = 4 fixed
    :15   `Δ = −∇² + E`, E entering with a `+`; m² separated out and NOT
          counted inside E for the a_k
    :19   the Proca determinant structure, with `E^μ_ν = R^μ_ν` (tr E = R) for
          the vector and `E = 0` for the Stueckelberg scalar
    :21   `β_s = −p_s (4π)^{−2} (tr a_1 / R)`, with p_s the log-det prefactor

**And `CONVENTIONS.md:5-6` states these were fixed before any computation in
`P2-HK-01` and were not adjusted afterwards to reproduce a paper value.**

#### `A8a` — does the RATIO `β_V/β_B = −(k+2)` depend on any of `R1`–`R5`?

**VERDICT: IT DEPENDS ON NONE OF THEM.**

**The lines that establish it:**

**`CONVENTIONS.md:21` makes the ratio convention-independent by
construction** — it says the results are reported *"both as a raw value (this
convention) and as convention-independent ratios `β_F/β_B`, `β_V/β_B`,
`β_B(ξ)/β_B`"*. **`derivations/P2-HK-01_heat_kernel_species.md:90` heads its
ratio section `### Ratios (convention-independent)`**, and `:10` repeats the
phrase.

**The ratio's inputs are exhausted by `CONVENTIONS.md:15`, `:16`, `:19` and
`:21`** — a continuum heat-kernel coefficient, an endomorphism assignment, a
determinant structure and a prefactor rule. **Every one is frozen, and not one
of them is any of `R1`–`R5`'s subject:**

    R1  canonical lattice kinetic operator and species accounting  — the ratio
        uses no lattice Dirac operator; it is a vector-plus-scalar determinant
        structure in the continuum
    R2  admissible lattice extent / finite volume                  — absent from
        every input line
    R3  boundary conditions                                        — absent
    R4  microscopic Euclidean variables, state space and measure    — absent; the
        ratio is a Seeley–DeWitt statement, not a functional-measure one
    R5  internal multiplicity N                                    — present in
        the ABSOLUTE normalisation (`:20`, `:29`) and CANCELS in a ratio of two
        species coefficients both reported per unit `4N`

**`R5` is the one to be careful about, and it is the reason `A8a` and `A8b` are
separate.** `N` genuinely appears in `CONVENTIONS.md:20` and `:29`. **It
appears in the NORMALISATION of `Z`, identically for both species**, so it
cancels in `β_V/β_B`. **An assessment that answered `A8a` "yes, via `R5`"
would have found `N` in the right document and drawn the wrong conclusion.**

#### `A8b` — does the ABSOLUTE or assembled `β_V`, or the induced-`G` normalisation, depend on any of `R1`–`R5`?

**VERDICT: YES — on `R5`, and on `R1`.**

**`R5`, internal multiplicity `N`. The lines:**

    CONVENTIONS.md:20   Z is "normalized **per unit `4N`** of fermionic degrees of
                        freedom (`4` spinor components × `N` flavors). Concretely
                        `Z ≡ 1/(16πG_ind)` in the TT channel, expressed per `4N`."
    CONVENTIONS.md:29   "`N` degenerate flavors; the induced coefficient is reported
                        per unit `4N`."

**`Z` is `1/(16πG_ind)` per unit `4N`. Converting a per-`4N` coefficient into
an induced `G` requires `N`.** **`R5` is open** —
`P2-CHANNEL-FREEZE-01_phaseA_freeze.md:43` keeps `N` symbolic — **so the
induced-`G` normalisation is ruling-dependent.**

**`R1`, the canonical kinetic operator AND SPECIES ACCOUNTING. The line:**

    P2-LATTICE-ONTOLOGY-01.md:189   "| Canonical kinetic operator and species
                                     accounting | DELEGATED: D-pre (§4 obligation
                                     binds it) |"

**"Species accounting" is the multiplicity ledger.** An assembled `β_V`
summing microscopic species contributions needs to know how many species of
each kind the declared operator carries — **which is exactly what `R1`
delegates.** The `kinetic-operator dossier`'s per-candidate species ledgers
make the point concretely: the four candidates carry different species counts.

**Not asserted for `R2`, `R3`, `R4`.** A lattice extraction of an absolute
`β` plausibly touches the extent and the measure, **but I did not find lines
that establish it**, and `A8b` asks for lines. **Reported as not established
rather than as absent.**

#### Which verdict the parallel-or-serial conclusion rests on

**IT RESTS ON `A8a`, AND ON `A8a` ALONE.**

**`A8a` returns NO DEPENDENCE. So the ratio is convention-fixed and a
reconstruction can be built and checked against it while `R1`–`R5` remain
open** — **two parallel lines.**

**`A8b` returns a dependence, on `R5` and `R1`. That does not change the
answer.** The assembled quantity's dependence **is not the ratio's**, and
projecting it back onto the ratio is the error the two-verdict structure
exists to prevent. **What `A8b`'s dependence does constrain is a different
deliverable — an absolute induced `G` — which this gate does not ask for.**

### 3.4 Question four — the component inventory

**In `§4`.**

### 3.5 Question five — what could make it fail, and would the failure be visible?

**The gate's two kill criteria, `GATES.md:757-759`, verbatim:**

> For the reconstruction itself: stuck at `−3` ∀k ⟹ the new pipeline is
> degenerate (a bug); drift toward `−5` at heavy mass ⟹ longitudinal artifact.
> None of these closes `P2-BETAV-CIRC-01`.

**COULD EITHER BE MISTAKEN FOR A PHYSICAL RESULT? YES — the first one, and
badly.**

**`−3` is the Proca value at `k=1`.** A degenerate pipeline that returns it
for every `k` returns **the physically expected number** at the physical point.
**A run that reported only `k=1` would be indistinguishable from success.**
**What distinguishes them is the `k`-scan**, which is why the gate's Scope
says *"vary only `k`"* and why `betav_discriminating.py` exists to establish
that the target is structure-dependent at the analytic layer. **The
`k`-dependence is the whole discriminator, and a single-`k` run has none.**

**The second is less mistakable but not innocent.** A drift toward `−5` at
heavy mass is **not** a value anything predicts, so it would not be read as
success — **but `reproduce_betav.py`'s docstring records this drift as a
*known* feature of the recovered pipeline attributed to the longitudinal flat
band.** **A new pipeline reproducing it could therefore be read as
faithfully reproducing the historical behaviour** rather than as carrying the
same artifact. **The gate's wording is the guard: it calls the drift an
artifact, not a signature.**

**And a third failure mode the gate does not name, recorded because `§2` found
it.** **Six of the eleven scripts embed the analytic target in docstrings or
code.** A reconstruction that imported any of them into its measuring stage
could recover the target through the import rather than through the physics,
**and neither kill criterion would fire** — the scan would track `−(k+2)`
because the number was in the room. **`GATES.md:415-418` already requires a
blind harness for exactly this reason**, and `harness_compute.py` is built to
that discipline. **This is a scope requirement, not a new criterion.**

## 4. The component inventory

**Four MUTUALLY EXCLUSIVE existence states. An implementation counts only if
it is POTENTIALLY APPLICABLE TO THE CLEAN-ROOM RECONSTRUCTION; where it exists
but is not, the component is reclassified and the fact recorded.**

**This is SEPARATE from `§2`'s reuse classification.**

| # | Component | State |
|---|---|---|
| 1 | metric-coupled 1-form operator `Δ⁽¹⁾[g,h]` on a weak-field background, exact geometric factors | `SPECIFICATION ONLY` |
| 2 | compensating scalar `Δ⁽⁰⁾[g,h]` | `SPECIFICATION ONLY` |
| 3 | `Γ_k = ½ logdet Δ⁽¹⁾ − (k/2) logdet Δ⁽⁰⁾` at the determinant level | `SPECIFICATION ONLY` |
| 4 | numerical `h`-derivatives at determinant/eigenvalue level, with Richardson check | `SPECIFICATION ONLY` |
| 5 | fixed axis-TT projection, identical for every `k`, pre-registered | `SPECIFICATION ONLY` |
| 6 | the `k`-scan driver over `k ∈ {0,1,2,3,½}` | `SPECIFICATION ONLY` |
| 7 | flat-limit validation against the Proca eigenstructure | `IMPLEMENTATION + SPECIFICATION` |
| 8 | blind two-stage harness: frozen output, external digest, deferred comparison | `IMPLEMENTATION + SPECIFICATION` |
| 9 | ratio-error tolerance rule, numerator and denominator correlated | `SPECIFICATION ONLY` |
| 10 | registered regression anchors for the reconstruction itself | `NEITHER` |

    N_both      2      components 7, 8
    N_impl      0
    N_spec      7      components 1, 2, 3, 4, 5, 6, 9
    N_neither   1      component 10
               --
    N_total    10      2 + 0 + 7 + 1 = 10   ✓

### 4.1 The applicability statement, per component counted as implemented

**Component 7 — flat-limit validation.** Implementation:
`scripts/betav_decomp_check.py`, which records the flat eigenstructure and the
propagator eigenvalues from actual operators and **states that it carries no
target**. **POTENTIALLY APPLICABLE**: a flat-limit comparison is a check, and
`§2` of the specification says a check is not a copied operator. It supplies
the comparison recipe; the new pipeline supplies the kernel.

**Component 8 — the blind harness.** Implementation:
`scripts/P2-BETAV-CAMPAIGN/harness_compute.py` and `compare.py`. **POTENTIALLY
APPLICABLE**: `harness_compute.py` contains no target numbers, emits frozen
JSON with an external digest, and defers all comparison — the architecture the
reconstruction needs. **Its current imports are not applicable and the
architecture is.**

### 4.2 Components whose implementation exists but is unusable here

**Three, and each for a stated reason.**

**Component 1, `Δ⁽¹⁾[g,h]`.** An implementation exists —
`proca_loop.py`'s `geomV`, and `gfvec_loop.py`'s gauge-fixed variant. **NOT
POTENTIALLY APPLICABLE**: it is the recovered historical pipeline
(`GATES.md:376`), so importing it defeats the clean-room label the gate
attaches at `:731`; and its docstring embeds the analytic target, the hazard
`GATES.md:415-418` names. **Reclassified `SPECIFICATION ONLY`.**

**Component 2, `Δ⁽⁰⁾[g,h]`.** An implementation exists — `boson_loop.py`'s
`geomB`. **NOT POTENTIALLY APPLICABLE**, for the clean-room reason above and
for a second: **`CIRC-01` found this scalar is not the Proca longitudinal
eigenfactor** (`GATES.md:382-385`), so substituting it is the step already
ruled unavailable. **Reclassified `SPECIFICATION ONLY`.**

**Component 5, the axis-TT projection.** An implementation exists —
`mlog_coeff.TT_RECIPES` and `proca_loop.g2_axis_proca`, reused by
`betav_decomp_q2.py`. **NOT POTENTIALLY APPLICABLE as a component**: the gate
requires the projection *pre-registered* with targets kept out of code and
tests (`GATES.md:748`), and the existing recipes live inside target-bearing
recovered modules. **Reclassified `SPECIFICATION ONLY`.**

**So the inventory's `SPECIFICATION ONLY` count of seven contains three
components that DO have code in the repository.** **That is what "existence is
not availability" costs, stated as a number.**

### 4.3 What the count is and is not

**Ten components. Two exist in usable form, seven are specified without usable
implementation, one has neither.**

**THIS IS A COUNT, NOT A DURATION, AND NOT A DIFFICULTY.** **Four components
of which none exists is not necessarily harder than eight of which six do**,
and nothing here measures how hard any of the ten is. **The one component with
NEITHER specification nor implementation — the registered regression anchors —
is plausibly the cheapest of the ten to produce**, which is itself the
demonstration that state does not track effort.

## 5. What this assessment does not establish

**A component count is not a difficulty**, `§4.3`.

**A successful reconstruction would not vindicate the historical pipeline.**
The gate says so at `:731-734` and the `RECON-01` derivation repeats it: a
faithful new pipeline returning the anchor *"demonstrates only that a correct
pipeline exists, not that the historical one was correct."* **`P2-BETAV-CIRC-01`
remains `RUN`, and `GATES.md:389` states it has NOT passed or failed.**
**Nothing in this line adjudicates it, and this assessment does not.** **A
reader meeting a future `−(k+2)` result must not read it as Finding 5
restored.**

**This assessment is bounded by the repository.** A component existing in a
paper, a notebook or an earlier machine is not counted here. **MEASURED: the
repository itself records that such things existed** —
`GATES.md:375-378` says the historical pipeline was *missing* and is now
*recovered*, and `scripts/recovered_2026/PROVENANCE.md` and
`results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md` are provenance records of a
search for absent material. **So evidence of outside-repository components
exists, and they are not counted.** **Absence from the repository is not
absence.**

**Whether this line is parallel to the `D-pre` line or downstream of it turns
on `A8a` alone.** `A8a` returns no dependence, so **the two lines are
parallel**: the ratio is convention-fixed and a reconstruction can be built
and checked against it while `R1`–`R5` stay open. **`A8b` returns a dependence
on `R5` and `R1`, and that does not change it** — the assembled quantity is a
different object, and this gate does not ask for it.

**Nothing here opens, orders or makes any of `R1`–`R5`; selects a canonical
kinetic operator; designs the reconstruction algorithm; constructs the
metric-coupled operator; or writes `RECON-01`.** **No script was executed, no
operator built, no derivative taken, and no `β` ratio computed or restated
beyond quoting the gate's anchor and kill criteria as the gate states them.**
