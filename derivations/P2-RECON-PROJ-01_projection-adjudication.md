# `P2-RECON-PROJ-01` — is there a derivational ground for the axis-TT projection?

    KIND        DOCUMENTARY / DERIVATIONAL READING. No computation.
    BASE        4257e2a22f2460f1669e1869c82130623fd7295b
    Q1          INCONCLUSIVE — reason: one location's status under the §3 test
                cannot be settled by reading. §4 records which and what would
                settle it.
    Q2          COMPONENT 5 — SPECIFICATION ONLY, unchanged in state, and the
                stated ground for it is narrowed by measurement.
    Q3          COMPONENT 9 — the unmet requirement is a SPECIFICATION gap and
                is decisively NOT physical completeness. §7 records the
                boundary the two-way question does not name.

**This artifact computes nothing.** No `β` of any kind, no ratio, no `k`-scan,
no lattice evaluation. **It reports what the repository contains.**

**It does not resolve `H-EXT-01` in either direction**, and **no outcome
recorded here blocks, gates, or is a prerequisite for `RECON-01b`.**

**`A-EXT-01` is not reopened.** That `Z_axis-TT` may be used definitionally is
settled, and nothing below bears on it.

---

## 1. `M7` — the two frozen statements, and confirmation neither is altered

    A-EXT-01   CONVENTIONS.md, definitional-conventions section
               Statement SHA
               ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378

    H-EXT-01   assumptions/H-EXT-01.md, PART 1
               Statement SHA
               e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47

**This task alters neither statement, and modifies neither file.** `§1c`
authorises only this artifact and the task's own spec, review and report.

---

## 2. `M1` — the corpus, and the substring separation that defines it

**The corpus was built by search and then read.** `§8` of the governing
specification names `complement` as matching unrelated linear-algebra prose,
and that hazard is the largest single effect in this task's evidence.

**MEASURED, whole tree, excluding this task's own two files:**

    matching lines for "complement"                278
      of which "complement root" / "complement_root"  84   — the P2-PHASE-01
                                                             C1 line, an
                                                             unrelated
                                                             root-finding sense
      of which "complementary"                        14
      of which "external complement", the §3 sense    12

**Twelve lines of two hundred and seventy-eight are the sense this task is
about.** They occur in seven files, all from the `EXT-01` line. **A count of
`complement` would have been 96% noise.**

    axis-TT              37 files
    TT_RECIPES           21 files
    transverse-traceless 14 files

### 2.1 The locations, with line spans and what each states

**Sixteen locations. Every one was opened and read.**

    L1   paper/emergent_gr_paper_v2_15.tex:752-768
         "Approximate Ward--Takahashi identities". Derives, from diffeomorphism
         invariance of the continuum measure and action and Symanzik power
         counting on the lattice breaking, eq:Ward —
         p_mu Gamma^(2) mu nu,rho sigma (p) = O(p^2/Lambda^2) Gamma^(2),
         "up to local contact terms that do not produce propagating poles."

    L2   paper/emergent_gr_paper_v2_15.tex:770-788
         "Spin-2 selection and masslessness". Decomposes Gamma^(2) in the
         Barnes--Rivers projector basis; states that the approximate
         transversality of L1 "forces all longitudinal structures to be
         suppressed by (p/Lambda)^2 relative to the transverse-traceless (TT)
         block", and that the trace identity "removes the propagating scalar
         block"; concludes eq:PiTT,
         Gamma^(2) = Z_h p^2 P^TT + O(p^4/Lambda^2) x (non-TT),
         "so that the only possible massless pole resides in the TT spin-2
         channel."

    L3   paper/emergent_gr_paper_v2_15.tex:816-833
         "Emergent gauge redundancy and universal coupling". Derives, from the
         infrared Ward identity, that the quadratic action of eq:PiTT is
         Fierz--Pauli and gauge-redundant, that gauge invariance of the linear
         coupling requires d_mu X^{mu nu} = 0, and hence that all matter
         couples with a common kappa.

    L4   paper/emergent_gr_paper_v2_15.tex:1130-1138
         "Finding 3: the universal mass-logarithmic coefficients". Derives,
         from mass-independence of the bare counterterms and the covariance of
         the IR region, that the m^2 ln m^2 part of the axis-TT slope is the
         universal covariant induced contribution.

    L5   paper/emergent_gr_paper_v2_15.tex:1209-1210
         Defines Z(m^2) as "the (axis-TT) induced kinetic coefficient per unit
         4N studied above."

    L6   scripts/recovered_2026/mlog_coeff.py:1-13
         Module docstring. Carries L4's argument in the same terms, and states
         the method: "bubble-only axis-TT slope (seagull and CC are q^0 /
         q-independent and drop from the slope). TT projector spectrally
         decomposed into 5 transverse-traceless basis tensors -> 5 effective
         vertices."

    L7   scripts/recovered_2026/mlog_coeff.py:21-31
         TT_RECIPES: the five basis tensors, "for q || e0, expressed as
         pair-combination recipes", each "a unit-normalized tensor".

    L8   derivations/betav_discriminating_power.md:20-30
         States that Z_V is the axis-TT slope and that the extraction computes
         the m^2-log part of it by numerical metric-derivatives of ln det,
         identifying that with the Seeley--DeWitt a_1 curvature response.

    L9   derivations/P2-NORM-01_normalization_chain.md:35-42
         Records that the paper's Z is "the axis-TT graviton kinetic slope
         (coefficient of p^2 in the transverse-traceless graviton
         self-energy) per unit 4N", differing from this repository's Z by a
         fixed normalisation R_Z = 2.

    L10  GATES.md:280-281
         "This repo's Z = coeff of R in the action; paper's Z = axis-TT slope
         per unit 4N (lines 1209-1210)."

    L11  GATES.md:304-306
         Records as a residual element that "the axis-TT-slope normalization +
         G=Ny^2=G_c map is taken on the paper's word (not text-derivable to the
         factor-of-2 level)."

    L12  GATES.md:739 and :748
         The RECON-01 gate's scope and inputs: "fixed axis-TT projection" and
         "pre-registered projection (targets kept out of code/tests)."

    L13  derivations/P2-BETAV-RECON-01_cleanroom_reconstruction.md:27-32
         "Extract the EH coefficient with a **fixed** axis-TT projection and
         normalization, identical for every k", and requires the projection
         pre-registered before running.

    L14  derivations/P2-BETAV-CIRC-01_determinant-decomposition.md:19-21, :24-62
         Records Z as "the axis-TT q^2 slope of g2_axis_proca", and decomposes
         the axis-TT-projected bubble into internal transverse/longitudinal
         sectors at the q^2 level.

    L15  derivations/P2-RECON-EXT-01_discarded-external-space.md, §1 and §2
         Enumerates the five retained components and the five discarded ones
         explicitly, identifies the unit-Frobenius normalisation from the
         repository's own comment, and verifies orthonormality and
         completeness of the ten.

    L16  CONVENTIONS.md, definitional-conventions section (A-EXT-01), and
         assumptions/H-EXT-01.md
         The landed definition and the landed hypothesis.

---

## 3. `M2` — every location against the two-part test

**The test of `§3` was fixed before the evidence was read and is applied as
written. It is not relaxed for any location.**

    PART 1   supplies a DERIVATIONAL ARGUMENT rather than defining, asserting
             or assuming the projection.
    PART 2   concludes something about the CONTRIBUTION OF THE DISCARDED
             COMPLEMENT to the target observable.

| loc | Part 1 | Part 2 | classification |
|---|---|---|---|
| L1 | **YES** — Ward identity from diffeomorphism invariance plus Symanzik power counting | **NO** — concludes about transversality of `Γ⁽²⁾`, not about a complement's contribution | near-miss (`M3`) |
| L2 | **YES** — decomposition in the Barnes–Rivers basis, using L1's transversality and a trace identity | **CANNOT BE SETTLED BY READING** — see §4 | **INCONCLUSIVE** |
| L3 | **YES** — gauge redundancy derived from the IR Ward identity | **NO** — concludes about universality of the matter coupling | near-miss (`M3`) |
| L4 | **YES** — counterterm mass-independence plus IR covariance | **NO** — concludes which *part of the slope* is universal | near-miss (`M3`) |
| L5 | NO — definitional | NO | not a ground |
| L6 | **YES** — L4's argument, plus a method statement | **NO** — the seagull/CC statement is about `q⁰` terms dropping from the slope, not about the discarded external complement | near-miss (`M3`) |
| L7 | NO — a definition of the five tensors | NO | not a ground |
| L8 | **YES** — identification with the Seeley–DeWitt `a₁` | **NO** — concludes what the extraction computes | near-miss (`M3`) |
| L9 | NO — records a normalisation relation | NO | not a ground |
| L10 | NO — definitional | NO | not a ground |
| L11 | NO — records that a map is **taken on the paper's word**, i.e. explicitly *not* derived | NO | not a ground |
| L12 | NO — states a requirement | NO | not a ground |
| L13 | NO — states a requirement | NO | not a ground |
| L14 | NO — records a definition and performs a decomposition | **NO** — its sectors are internal propagator indices, not the external complement | not a ground |
| L15 | NO — enumerates and verifies a basis | **NO** — measures magnitudes; a measurement is not a derivation | not a ground |
| L16 | NO — a definition and an unestablished hypothesis | NO | not a ground |

**Zero locations satisfy both parts. One location's Part 2 status cannot be
settled by reading.**

### 3.1 The `L11` observation, recorded because it cuts the other way

`GATES.md:304-306` states that the axis-TT-slope normalization map is **"taken
on the paper's word (not text-derivable to the factor-of-2 level)."** **This is
the repository recording, in its own gate text, that a piece of the axis-TT
apparatus is inherited rather than derived.** It is not a ground and it is not
a near-miss; it is a landed statement pointing the same way as this
adjudication's outcome.

---

## 4. `Q1` — outcome `INCONCLUSIVE`

**Which location, and why its status cannot be settled by reading.**

**`L2`, `paper/emergent_gr_paper_v2_15.tex:770-788`.** Quoted:

> Decomposing $\Gamma^{(2)}$ in the Barnes--Rivers projector basis,
> the approximate transversality \eqref{eq:Ward} forces all
> longitudinal structures to be suppressed by $(p/\Lambda)^2$
> relative to the transverse-traceless (TT) block, and the trace
> identity (for the improved stress tensor, up to contact terms)
> removes the propagating scalar block.
> The infrared kernel is therefore
> …
> $\Gamma^{(2)}_{\mu\nu,\rho\sigma}(p) = Z_h\,p^2\,\mathcal{P}^{\mathrm{TT}}_{\mu\nu,\rho\sigma}(p) + \mathcal{O}\!\left(\frac{p^4}{\Lambda^2}\right)\times(\text{non-TT})$
> …
> so that the only possible massless pole resides in the TT spin-2
> channel.

**Part 1 is satisfied and is not in doubt.** This is a derivation: a Ward
identity established at `L1` from diffeomorphism invariance and Symanzik power
counting, combined with a trace identity, applied in a named projector basis.
It defines nothing and assumes nothing about the projection.

**Part 2 is where it cannot be settled.** `L2` concludes that **non-TT
structures enter at `O(p⁴/Λ²)`** while the TT block carries the `p²` term. **If
the manuscript's "non-TT" set is the complement the axis-TT projection
discards, then Part 2 is satisfied**, and satisfied strongly: a structure
entering at `p⁴` contributes nothing to the `p²` coefficient, and the `p²`
coefficient is the target observable — `L9` records the paper's `Z` as exactly
"the coefficient of `p²` in the transverse-traceless graviton self-energy", and
`:781` writes `Z_h p²` in the retained block.

**What is not stated anywhere is that the two sets are the same.**

**MEASURED.** Every repository location mentioning both the axis-TT projection
and the Barnes–Rivers decomposition was read. **There are three, and all three
instruct the reader to distinguish them:**

    derivations/P2-RECON-EXT-01_discarded-external-space.md:116
    specs/2026-08-19T0223Z_pole-b0-milestone-scope.md:191
      "**Distinguish an axis-TT projection from a Barnes–Rivers spin
       decomposition if both appear.**"

    reports/2026-08-19T0223Z_pole-b0-milestone-scope.md:307
      "### `projector` at fifty-four — the axis-TT versus Barnes–Rivers
       distinction"

and `derivations/P2-RECON-EXT-01_discarded-external-space.md:124` describes
Barnes–Rivers projectors as "acting on a different object."

**No location states the identification, and the only locations that mention
both deny or caution against it.** Supplying the identification would be
performing the derivation myself, which `§3` forbids: a location the executor
believes should count but which fails a part is recorded, not promoted.

### 4.1 What would settle it

**One statement, of either sign, in a document:** that for `q` along an axis
the Barnes–Rivers TT block and the span of `TT_RECIPES` are the same
five-dimensional space, and that the Barnes–Rivers non-TT blocks are the five
components `EXT-01` enumerates as discarded — or that they are not.

**That statement would be a derivation, not a reading**, which is why this
outcome is `INCONCLUSIVE` and the reason recorded under `R1` is **`UNDETERMINED
BY READING`.** The computation it would require is a structural identification
of two projector bases, and it was not performed.

### 4.2 A second gap, recorded because it is independent of the first

**Even granting the set identification, `L2` and the repository's own
measurement are not obviously about the same object.**

`L2` derives its suppression for `Γ⁽²⁾`, the **infrared effective kernel**,
under Symanzik power counting, **for the improved stress tensor, up to contact
terms**. `L15` measured a **lattice Proca bubble** at `a = 1`, `m = 0.3`,
finite `n`, **unimproved**, and found the discarded components' `q²`
coefficients comparable in magnitude to the retained ones, with every observed
scaling exponent in `[1.9887, 1.9982]`.

**These are not presented here as contradicting.** They concern different
objects — an IR effective kernel versus a finite-spacing bubble — and different
regimes. **But whether `L2`'s conclusion transfers to the object `EXT-01`
measured is a second question that reading does not answer**, and it would
survive even if the set identification of `§4` were supplied.

**Neither gap is evidence that `H-EXT-01` is false, and neither is recorded as
one.**

### 4.3 What this outcome does not do

**`INCONCLUSIVE` is a completed measurement, not a failure.** Per `§4` of the
governing specification all three outcomes are completed measurements.

**It leaves `H-EXT-01` exactly where it already was** — `UNESTABLISHED`, `NOT
ASSUMED BY RECON-01b` — and **changes nothing about whether `RECON-01b` may
proceed.**

**`L2` is nonetheless the closest existing material in the repository**, and it
is recorded here so that a later derivation knows where to start: it already
carries the physics conclusion in the Barnes–Rivers language, and what it lacks
is the bridge to the basis the extraction actually uses.

---

## 5. `M3` — near-misses

**Five locations satisfy Part 1 and fail Part 2. Each is recorded with which
part failed and why. None is promoted.**

**`L1`, `:752-768`.** Derives the Ward identity. **Fails Part 2**: its
conclusion is about the transversality of `Γ⁽²⁾` — that `p_μ Γ⁽²⁾` is
cutoff-suppressed. It says nothing about how much any component of the external
index space contributes to the `p²` coefficient. **It is the premise `L2` uses,
not a conclusion about a complement.**

**`L3`, `:816-833`.** Derives gauge redundancy from the IR Ward identity and
concludes that all matter couples with a common `κ`. **Fails Part 2**: its
subject is the universality of the matter coupling, not the complement's
contribution. `CHANNEL-B0` already recorded that this subsection scopes itself
to `eq:PiTT` and never mentions the angular mode; **it inherits `eq:PiTT`
rather than establishing anything about what `eq:PiTT` discards.**

**`L4`, `:1130-1138`, and `L6`, `mlog_coeff.py:1-13`, which carry the same
argument.** Derive that the `m² ln m²` part of the axis-TT slope is the
universal covariant induced contribution, from counterterm mass-independence
and IR covariance. **Fails Part 2**: the conclusion is about **which part of
the slope** is scheme-independent, not about which components of `h` contribute
to the slope. **This is the ground `EXT-01`'s `M7` identified, and applying
`§3`'s test to it shows why it is not a ground for the completeness
question**: it grounds the observable's universality in mass, not the
projection's completeness in the index space.

**`L6`'s method sentence, separately.** *"seagull and CC are `q⁰` /
`q`-independent and drop from the slope"* is a genuine derivational statement
about what drops out of the slope. **Fails Part 2**: what drops there are
`q`-independent **terms**, not components of the external index space. **The
two senses of "drops out" are different and are not conflated here.**

**`L8`, `betav_discriminating_power.md:20-30`.** Identifies the extraction with
the Seeley–DeWitt `a₁` curvature response. **Fails Part 2**: it concludes what
the extraction computes, not what the projection may discard.

---

## 6. `Q2` / `M4` — component 5

**`(i)` and `(ii)` are recorded first and the classification is taken from them
alone. `(iii)` is recorded afterwards and marked as not contributing.**

### 6.1 (i) — implementation state of the `TT_RECIPES` machinery

**An implementation exists.** `scripts/recovered_2026/mlog_coeff.py:21-31`
defines `TT_RECIPES` as five pair-combination recipes for `q ∥ e₀`, each a
unit-normalised tensor. **MEASURED, where it is used:** `mlog_coeff.py:46`,
`:69`; `proca_loop.py:23`, `:115-116`; `batch2/gfvec_loop.py:28`, `:139`,
`:238`; `betav_decomp_q2.py:51`, `:74-75`; and
`scripts/diagnostics/ext01_discarded_external_space.py:49`, `:64-68`.

**Applicability — and the prior ground is compound, with one half not holding
as measured.**

The landed assessment at
`derivations/P2-BETAV-RECON-01_scope-assessment.md:526-531` gives two reasons:
*"the gate requires the projection pre-registered with targets kept out of code
and tests (`GATES.md:748`), and the existing recipes live inside target-bearing
recovered modules."*

**MEASURED on the module that DEFINES the recipes,
`scripts/recovered_2026/mlog_coeff.py`:**

    (k+2)      0        beta_V     0
    k+2        0        β_V        0
    -3         0

**`mlog_coeff.py` carries no RECON anchor.** The one benchmark in its docstring
is `beta_Dirac / beta_real-min-scalar = 2`, labelled in place a *"convention-free
ratio test"* — a heat-kernel species ratio, a different quantity. **The
target-bearing module is `proca_loop.py:18`, which imports `TT_RECIPES` from
`mlog_coeff`, not the other way round.**

**So the "target-bearing" half of the ground does not hold for the defining
module.** Recorded as a narrowing of a landed statement, not as a reversal of
its conclusion.

**What survives, and is decisive:**

- **Provenance.** `GATES.md:376` names
  `scripts/recovered_2026/proca_loop.py` **and** `mlog_coeff.py` as
  **recovered**. The clean-room label the `RECON-01` gate attaches at `:731`
  is a claim about provenance, and importing a recovered module defeats it
  regardless of whether that module carries a target.
- **Pre-registration.** `GATES.md:748` requires a *pre-registered* projection.
  **MEASURED: no pre-registration exists.** Searching `derivations/` for a
  RECON pre-registration note returns **none** — the only `prereg` file is
  `P2-BETAV-CAMPAIGN_prereg.md`, a different line — and
  `P2-BETAV-RECON-01_cleanroom_reconstruction.md:31` records pre-registration
  as something still to be done.

**`(i)`: an implementation exists and is NOT potentially applicable, on
provenance and on the absent pre-registration.**

### 6.2 (ii) — specification state of the same

**Requirements are stated.** `GATES.md:739` ("fixed axis-TT projection"),
`:748` (pre-registered, targets out of code and tests), and
`P2-BETAV-RECON-01_cleanroom_reconstruction.md:27-28` ("identical for every
`k`").

**New at this base, and material.**
`derivations/P2-RECON-EXT-01_discarded-external-space.md §1` **reproduces the
five recipes verbatim in an artifact that carries no target**, identifies the
unit-Frobenius normalisation from the repository's own comment, and verifies
orthonormality and completeness of the ten-component basis. `§2.1` enumerates
the five discarded components explicitly.

**That is a written, target-free statement of the projection's content**, and
it did not exist when component 5 was last classified. **It is not, however, a
pre-registration for the gate**: it is a description written for a diagnostic,
it pre-registers nothing for `RECON-01b`, and `GATES.md:748`'s requirement is
unmet by it.

**`(ii)`: the requirement is specified, and the projection's content is now
stated target-free; the pre-registration the gate requires does not exist.**

### 6.3 (iii) — statements bearing on physical completeness

`H-EXT-01`, `assumptions/H-EXT-01.md`, `UNESTABLISHED`. `Q1` above returns
`INCONCLUSIVE`.

**RECORDED AS NOT CONTRIBUTING TO THE CLASSIFICATION OF `(i)` OR `(ii)`.**
Component 5 is not downgraded because complement irrelevance is unproven, and
is not upgraded because the recipe is documented and implemented. **The
classification below uses `(i)` and `(ii)` only.**

### 6.4 Classification

    Component 5    SPECIFICATION ONLY

**Unchanged in state from the last landed assessment.** The implementation is
not potentially applicable — recovered provenance, and no pre-registration —
so it does not count; the specification exists. **What changed is the ground,
not the state:** one of the two reasons the landed assessment gave does not
hold as measured, and the specification side is materially stronger than it
was.

---

## 7. `Q3` / `M5` — component 9

**What the component requires.** `derivations/P2-BETAV-RECON-01_scope-assessment.md:483`
names it *"ratio-error tolerance rule, numerator and denominator correlated"*.

**What is present.** The **form** is stated. `:319-322` of the same document:

> **What is NOT stated anywhere I found: a numerical tolerance for the
> flat-limit comparison.** The `RECON-01` derivation states the *form* the
> tolerance must take — a propagated ratio error, numerator and denominator
> correlated through a shared momentum grid — **but no value or rule.**

and the correlation's physical origin is derived at
`derivations/P2-BETAV-ASSEMBLY-01_bookkeeping_regression.md:33-39`:

> Numerator and denominator are the **same** integral `C` times different
> rational prefactors, so `C` cancels exactly. … Numerator and denominator are
> **fully correlated** — the tolerance is a propagated *ratio* error, not two
> independent `β` scatters divided.

**What is missing: a value or a rule.**

### 7.1 The determination

**The unmet requirement is a SPECIFICATION gap. It is decisively NOT physical
completeness of the projection.**

**The evidence excludes `(b)` cleanly.** A propagated ratio-error tolerance
would be required whatever the projection's completeness status. `H-EXT-01`
being established, refuted, or open changes nothing about whether a numerical
acceptance rule exists for comparing a ratio whose numerator and denominator
share an integral. **No location connects component 9 to the projection at
all**: every repository line bearing on it —
`ASSEMBLY-01:33`, `:38`; `RECON-01_scope-assessment:321`, `:483`;
`SIGN-01:538`; `betav-provenance-merge_report:64`;
`recon-b0-scope:258`, `:382`; `sign-01 report:385`;
`betav_assembly.py:23`, `:25`; `integrate-sign-01:75` — concerns the shared
integral `C` and its cancellation, and none mentions the projection.

**The boundary the two-way question does not name, recorded rather than forced.**
`(a)` is *"specification of the observable"*. **The observable's definition is
supplied — `A-EXT-01` supplies it, and it was already supplied by
`CONVENTIONS.md:20` before that.** What component 9 lacks is an **acceptance
tolerance for a comparison performed on that observable**, which is a third
thing: neither the observable's definition nor the projection's completeness.

**So: `(a)` on the specification/completeness axis the question draws, and the
qualification is that the gap is in the acceptance criterion rather than in the
observable's definition.**

**Consequence for readiness, stated because `Q3`'s premise asks it.**
**`A-EXT-01` did NOT change component 9's readiness state**, and the reason is
now evidence-backed rather than assumed: the gap was never the observable's
definition, so supplying that definition could not close it.

### 7.2 Classification

    Component 9    SPECIFICATION ONLY

**Unchanged in state from the last landed assessment.** No implementation
exists — a search for `ratio-error` and `ratio error` returns two documents and
no code — and the form is specified while the value is not.

---

## 8. `M6` — classifications, and the baseline they are compared against

    Component 5    SPECIFICATION ONLY    unchanged
    Component 9    SPECIFICATION ONLY    unchanged

**The baseline is `derivations/P2-BETAV-RECON-01_scope-assessment.md:479`,
`:483`, which classifies both `SPECIFICATION ONLY`.**

**MEASURED, and it matters for what "the last assessment" means:**
`P2-RECON-01B-B0_scope-assessment.md` is **not present at this evidence base**,
and `science/recon-01b-b0-scope` is **not an ancestor of it** —
`git merge-base --is-ancestor` returns exit 1. **That re-measurement exists on
an unlanded branch and is not the landed baseline.** It also classified
components 5 and 9 as `SPECIFICATION ONLY`, so the comparison is unaffected;
**the fact is recorded so the baseline is not mistaken.**

**Cause of the non-change, for each:**

- **Component 5** — the implementation remains recovered-provenance and no
  pre-registration exists. **`A-EXT-01`'s landing did not bear on either.**
- **Component 9** — the missing value or rule is unchanged. **`A-EXT-01`'s
  landing did not bear on it, because the gap was never the observable's
  definition.**

---

## 9. What this adjudication does not establish

- **It produces no number**, no `β` of any kind, no ratio, no `k`-scan, and no
  lattice evaluation.
- **It does not resolve `H-EXT-01`.** `Q1`'s `INCONCLUSIVE` is a statement
  about what reading can settle, **not evidence that `H-EXT-01` is false and
  not evidence that it is true.**
- **It does not re-adjudicate `A-EXT-01`** and alters no landed exact
  statement; `§1` records both `Statement SHA`s unchanged.
- **It sets no criterion or threshold.**
- **It does not extend the `EXT-01` diagnostic**, which is `D-2` and a separate
  measurement task.
- **It does not modify any register, convention, gate, assumption or decision
  file.** Any reclassification recorded here is landed, if at all, by a later
  integration specification.
- **A `SPECIFICATION ONLY` classification is a statement about availability at
  this base**, not about difficulty, importance, or how much work remains.

## 10. Questions raised and not settled

1. **Whether the Barnes–Rivers non-TT blocks and the axis-TT discarded
   complement are the same space.** `§4` records this as the reason `Q1` is
   `INCONCLUSIVE`. **Three repository locations mention both and all three
   caution against identifying them**; none states the relation either way.

2. **Whether `L2`'s suppression transfers to a finite-spacing unimproved
   lattice bubble.** `§4.2`. Independent of question 1 and would survive its
   resolution.

3. **Whether a clean-room re-expression of `TT_RECIPES` is reuse.** `§6.1`
   narrows the ground — the defining module carries no RECON anchor — without
   settling the provenance question, which is component 5's remaining
   obstacle together with the absent pre-registration. **Not adjudicated here.**

4. **Whether "specification of the observable" was meant to include the
   acceptance tolerance.** `§7.1`. The determination excludes physical
   completeness decisively; the `(a)` boundary is a wording question the
   two-way form does not resolve.
