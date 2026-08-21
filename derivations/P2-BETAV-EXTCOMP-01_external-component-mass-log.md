# `P2-BETAV-EXTCOMP-01` — the mass-log content of the discarded external space

    KIND        MEASUREMENT. Protocol frozen before any result exists.
    BASE        caf5111dacad21da9e204b79b4b7add1f648107c
    QUESTION    Do the discarded external components carry `m² ln m²`
                content, and at what size relative to the retained ones?

**No criterion, threshold, pass band or acceptance range is set on any quantity
in this artifact.**

---

## PART 1 — PRE-REGISTRATION (`M2`)

**This part is committed before any result exists.** It contains no value
produced by `M4`, `M5` or `M6`. Everything below is an input read from landed
state under `M1`, or a formula fixed by the governing specification.

### 1. `M1` — every frozen parameter, read from landed state with its citation

**Nothing here is restated from the specification. Each value carries the line
that fixes it.**

#### 1.1 The object and its decomposition

    ten orthonormal external components, in the Frobenius norm
      5 RETAINED    scripts/diagnostics/ext01_discarded_external_space.py:63-69
                    R1  (h11 - h22)/sqrt(2)          TT_RECIPES[0]
                    R2  (h11 + h22 - 2 h33)/sqrt(6)  TT_RECIPES[1]
                    R3  (1,2) direction              TT_RECIPES[2]
                    R4  (1,3) direction              TT_RECIPES[3]
                    R5  (2,3) direction              TT_RECIPES[4]
      5 DISCARDED   scripts/diagnostics/ext01_discarded_external_space.py:71-79
                    D1  h00
                    D2  (0,1) direction
                    D3  (0,2) direction
                    D4  (0,3) direction
                    D5  spatial trace (h11 + h22 + h33)/sqrt(3)

    basis            TT_RECIPES at scripts/recovered_2026/mlog_coeff.py:24-31
    counts           5 retained, 5 discarded, 10 total — READ, not assumed

#### 1.2 The lattice extent, q grid and fit form

    lattice extent   n = 12
                     scripts/diagnostics/ext01_discarded_external_space.py:57
                     `EXTENT = 12`, the extent EXT-01 used

    q grid           4 points: 0.10, 0.16, 0.22, 0.28
                     scripts/recovered_2026/proca_loop.py, `def slope(...)`
                     default `eps=np.array([0.10, 0.16, 0.22, 0.28])`;
                     the same default at
                     scripts/recovered_2026/mlog_coeff.py:76

    step-1 fit form  Π(q) = A + B q² + C q⁴, B taken as the q² coefficient
                     scripts/recovered_2026/seagull_check.py, `fit_even`,
                     `np.vander(eps**2, order + 1, increasing=True)` with
                     `order=2`; index [1] is taken by
                     scripts/recovered_2026/proca_loop.py `slope`

    step-2 fit form  Z(m²) = z0 + z1 m² + β m² ln(m²) + z2 m⁴
                     scripts/recovered_2026/mlog_coeff.py:81-92,
                     `fit_mlog(m2, Z, with_m4=True)` — INHERITED, not chosen
                     here

    finite-difference step   EPSF = 1e-3
                     scripts/recovered_2026/seagull_check.py:75

#### 1.3 The two mass windows, each used in full

**The landed pipeline's VECTOR path uses exactly two windows**, at
`scripts/recovered_2026/reproduce_betav.py:62-63`, consumed by `vector_ZV` at
`:70-71`. A third window at `:61`, `paper_win`, is the SCALAR `β_B` window and
is **not used here** — §0d.1 forbids computing `β_B`.

    LIGHT   np.linspace(0.11, 0.30, 7)   reproduce_betav.py:62
            0.110000  0.141667  0.173333  0.205000  0.236667  0.268333  0.300000

    HEAVY   np.linspace(0.20, 0.45, 7)   reproduce_betav.py:63
            0.200000  0.241667  0.283333  0.325000  0.366667  0.408333  0.450000

    7 points each, 14 mass points in total. NEITHER IS PRIMARY.

**The mass-times-extent product at each window's extreme points**, which is
what `n = 12`'s recorded limitation turns on:

    LIGHT   m_min · n = 0.11 · 12 = 1.3200      m_max · n = 0.30 · 12 = 3.6000
    HEAVY   m_min · n = 0.20 · 12 = 2.4000      m_max · n = 0.45 · 12 = 5.4000

**The light window's lightest point has the smallest product and is where
finite-volume contamination is worst; the heavy window reaches the largest.
Both are target-free objections and neither window is free of one.**

#### 1.4 The retained weights `w_i`, READ — this is `A8`'s subject

**The landed line that fixes them:**

    scripts/recovered_2026/proca_loop.py:130
        return total / (n ** 4) / 5.0

**in `g2_axis_proca`, the landed axis-TT Proca bubble.** The same `/ 5.0`
appears at `scripts/recovered_2026/mlog_coeff.py:54` for the fermion path and
`:73` for the boson path.

**THE WEIGHTS ARE `w_i = 1/5`, NOT UNITY.** The landed assembly is a MEAN over
the five retained components.

**Established structurally, not only from the constant.** The landed
`g2_axis_proca` and the per-component `component_bubble` of
`scripts/diagnostics/ext01_discarded_external_space.py:104-127` build the same
`R2`, `Rm`, `U1`, `U2`, `X` and `Y`, and differ in exactly two places:

    landed        np.einsum("rpij,rpji->",  X, Y)   then  / n**4 / 5.0
    per component np.einsum("rpij,rpji->r", X, Y)   then  / n**4

**The landed output is therefore the mean of the per-component outputs over
the five retained recipes, by construction.** A numerical identity check of
this statement is performed after this pre-registration and reported in PART 2.

#### 1.5 The discarded weights `v_i` — THIS TASK'S CHOICE, so labelled

**The repository has never assembled the discarded components, so no landed
weight exists.** Per §1.4 of the governing specification, `v_i` takes the same
functional form as `w_i`. The landed form is an average, so:

    v_i = 1/5,  an average over the five discarded components

**THIS IS A CHOICE OF THIS TASK AND NOT A LANDED FACT**, and every result
below that uses it is labelled accordingly.

### 2. The assembly, with the read weights substituted

    B_R  =  Σ_{i∈R} (1/5) β_i        w_i = 1/5, LANDED
    B_D  =  Σ_{i∈D} (1/5) β_i        v_i = 1/5, THIS TASK'S CHOICE

    R_signed  =  |B_D| / |B_R|
    R_abs     =  ( Σ_{i∈D} |(1/5) β_i| ) / ( Σ_{i∈R} |(1/5) β_i| )

**A consequence of the read weights, recorded here before any result.**
Because the retained and discarded sets each have five members, the factor
`1/5` appears identically in numerator and denominator and **cancels in both
ratios**. It does **not** cancel in `B_R` and `B_D` themselves, which are each
a factor of five smaller than the corresponding plain sums.

**So the ratios are insensitive to this weight choice and the aggregates are
not.** This is stated now, in the pre-registration, so that it cannot be
offered afterwards as a reason the choice did not matter.

### 3. The frozen variant set (`V1` × `V2`) — four combinations

    V1   mass window
         V1a  LIGHT   the seven points of §1.3
         V1b  HEAVY   the seven points of §1.3

    V2   step-2 fit form
         V2a  INHERITED    fit_mlog(..., with_m4=True)
                           Z = z0 + z1 m² + β m² ln m² + z2 m⁴
         V2b  SENSITIVITY  fit_mlog(..., with_m4=False)
                           Z = z0 + z1 m² + β m² ln m²

**`V2b` differs from `V2a` in a single stated respect: the `m⁴` column is
absent from the design matrix.** It is the landed function's own `with_m4`
flag, not a new fit written here.

**THE SET IS FOUR COMBINATIONS AND IS FROZEN NOW.** No variant is added after
a number exists and none is dropped. The band is this set's spread, so
changing the set would change every band.

### 4. Numerical validity, frozen (`E3`)

    solver            numpy.linalg.lstsq, the solver the landed pipeline uses
                      — seagull_check.fit_even and mlog_coeff.fit_mlog both
                      call it, and it is not chosen here

    NON-FINITE        any NaN or infinity in a coefficient -> that fit FAILS
    EXACTLY SINGULAR  design matrix reported rank deficient -> that fit FAILS
    HIGH CONDITION    finite, full-rank, any condition number -> the value IS
                      REPORTED, flagged with its condition number.
                      **NO CONDITION NUMBER IS A PASS/FAIL LINE.**
    RESIDUAL          reported per fit as a diagnostic of fit quality or model
                      mismatch. **NOT an error bar and NOT a fail criterion.**

**There is no statistical uncertainty in this computation.** The lattice sum is
deterministic. **The only band reported is the spread over the four frozen
variant combinations.**

### 5. What is reported, fixed here

    PRIMARY     β_i per component, over every variant combination
    PRIMARY     the discarded-to-retained ratio in BOTH aggregations,
                R_signed and R_abs, both always
    BAND        the spread of each reported quantity over the four combinations
    SECONDARY   the absolute spread of the retained aggregate on its own

    PREDICTION  the ratio's spread is expected SMALLER than the spread of its
                numerator and of its denominator separately, because both are
                produced by one pipeline on one grid and shared systematics
                partly cancel.

**The prediction is recorded so that it can fail.** Whether it held is stated
either way in PART 2.

### 6. `M8` — what this task must not move

    A-EXT-01   ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
    H-EXT-01   e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47

Every blob under `scripts/recovered_2026/` and `scripts/recon2026/` is recorded
and confirmed unchanged in PART 2.

---

**END OF PRE-REGISTRATION. No result value appears above this line, and none
appears in the commit that carries it.**

---

## PART 2 — RESULTS

**Committed after the pre-registration above.** Every parameter used is PART 1's.

### 7. `M3` — the measured cost, and the projection

    one mass point, all 10 components, 4 q values     17.10 s
    mass points in the frozen set                     14
    projected total for the full grid                 239.5 s
    E5's second pass over the light window (7)        ~120 s

**Measured, not assumed.** The projection was made before the full run and the
run did not exceed it.

### 8. `M1`'s weight identity, verified numerically

**PART 1 §1.4 states the landed assembly is the mean of the per-component
outputs over the five retained recipes, by construction.** That statement is
checked against the landed code running, at `q = 0.10`, `m = 0.11`, `n = 12`:

    landed g2_axis_proca                  -3.290003604783e-01
    mean of per-component over retained   -3.290003604783e-01
    relative difference                    2.531e-15

**`w_i = 1/5` is therefore established twice**: by the line
`proca_loop.py:130` and by this identity at machine precision. **`A8` does not
fire.**

### 9. `β_i` per component, per variant combination — all four

**All ten components are `REPORTED` under all four combinations.** No fit was
`NON-FINITE`, none was `EXACTLY SINGULAR`, and no component is
`NOT EVALUABLE`. **`A4` does not fire.**

    component          HEAVY|V2a_with_m4         HEAVY|V2b_no_m4       LIGHT|V2a_with_m4         LIGHT|V2b_no_m4
    R1                    +3.311124e-03           +1.207456e-03           -8.172226e-03           -3.919449e-04
    R2                    +3.311124e-03           +1.207456e-03           -8.172226e-03           -3.919449e-04
    R3                    +1.620972e-03           +2.176838e-05           -9.028303e-03           -1.625978e-03
    R4                    +1.620972e-03           +2.176838e-05           -9.028303e-03           -1.625978e-03
    R5                    +1.620972e-03           +2.176837e-05           -9.028303e-03           -1.625978e-03
    D1                    +1.482084e-03           +2.227417e-03           -7.762685e-03           -7.533763e-04
    D2                    +1.146967e-03           +1.090053e-04           -4.530628e-03           -6.653118e-04
    D3                    +1.146967e-03           +1.090053e-04           -4.530628e-03           -6.653118e-04
    D4                    +1.146967e-03           +1.090053e-04           -4.530628e-03           -6.653118e-04
    D5                    +2.293546e-03           +2.100235e-03           -1.429066e-03           +1.219040e-03

**Design-matrix conditioning, per variant. NO THRESHOLD IS APPLIED**, per
`E3`'s `HIGH CONDITION` rule and §1.7.

    HEAVY|V2a_with_m4      cond 3.4302e+03   rank 4/4   full rank
    HEAVY|V2b_no_m4        cond 1.3924e+02   rank 3/3   full rank
    LIGHT|V2a_with_m4      cond 1.1191e+04   rank 4/4   full rank
    LIGHT|V2b_no_m4        cond 3.5590e+02   rank 3/3   full rank

    step-1 design (the fixed q grid)  cond 1.9846e+03   rank 3/3

**Residuals, max absolute, per component per variant.** Per §0c and `E3` these
are diagnostics of fit quality or model mismatch. **They are NOT error bars and
NOT a fail criterion.**

    component          HEAVY|V2a_with_m4         HEAVY|V2b_no_m4       LIGHT|V2a_with_m4         LIGHT|V2b_no_m4
    R1                       3.8187e-07              4.0930e-06              5.6297e-06              1.2998e-05
    R2                       3.8187e-07              4.0930e-06              5.6297e-06              1.2998e-05
    R3                       2.4404e-07              3.1358e-06              5.4341e-06              1.2444e-05
    R4                       2.4404e-07              3.1358e-06              5.4341e-06              1.2444e-05
    R5                       2.4404e-07              3.1358e-06              5.4341e-06              1.2444e-05
    D1                       1.0941e-06              2.1781e-06              3.8783e-06              1.0516e-05
    D2                       1.3168e-07              2.0255e-06              2.8191e-06              6.4796e-06
    D3                       1.3168e-07              2.0255e-06              2.8191e-06              6.4796e-06
    D4                       1.3168e-07              2.0255e-06              2.8191e-06              6.4796e-06
    D5                       3.2642e-07              5.6105e-07              1.5570e-06              4.0649e-06

**Observed near-degeneracies, recorded as measured.** Within `LIGHT|V2a`, and
similarly in the other combinations, several components agree to a relative
difference of order `1e-9` or smaller:

    R1 ~ R2                relative difference  1.1e-09
    R3 ~ R4 ~ R5           relative differences 1.2e-10 to 1.3e-09
    D2 ~ D3 ~ D4           relative differences 2.5e-10 to 1.2e-09

**These are recorded, not explained.** They are consistent with the basis's
symmetry under the cubic group at `q ∥ e₀`, and nothing here establishes that
this is their cause.

### 10. The aggregates and BOTH ratios, per variant

**`B_R` uses the landed `w_i = 1/5`. `B_D` uses `v_i = 1/5`, WHICH IS THIS
TASK'S CHOICE AND NOT A LANDED DEFINITION.**

    variant                            B_R             B_D    R_signed       R_abs
    HEAVY|V2a_with_m4        +2.297033e-03   +1.443306e-03      0.6283      0.6283
    HEAVY|V2b_no_m4          +4.960433e-04   +9.309336e-04      1.8767      1.8767
    LIGHT|V2a_with_m4        -8.685872e-03   -4.556727e-03      0.5246      0.5246
    LIGHT|V2b_no_m4          -1.132365e-03   -3.060544e-04      0.2703      0.7009

**Both aggregations are reported for every variant, and neither is presented as
the result.**

**`R_signed` and `R_abs` coincide in three of the four combinations and diverge
in one.** In `LIGHT|V2b_no_m4` they are 0.2703 against 0.7009. The cause is
visible in §9's table: in that combination `D5` carries the opposite sign to
`D1`–`D4`, so the signed sum cancels partially while the sum of magnitudes does
not. **This is why the specification requires both, and it is the case that
makes the requirement bite.**

### 11. BAND — the spread over the four frozen variant combinations

**The band is this set's spread and nothing else.** There is no statistical
uncertainty in this computation.

    B_R        min  -8.685872e-03   max  +2.297033e-03   spread 1.098290e-02
    B_D        min  -4.556727e-03   max  +1.443306e-03   spread 6.000033e-03
    R_signed   min  +2.702790e-01   max  +1.876718e+00   spread 1.606439e+00
    R_abs      min  +5.246136e-01   max  +1.876718e+00   spread 1.352105e+00

### 12. SECONDARY — the absolute spread of the retained aggregate on its own

    |B_R| across the four combinations   min 4.960433e-04
                                         max 8.685872e-03
    absolute spread of B_R               1.098290e-02

**`B_R` changes sign across the windows** — positive on `HEAVY`, negative on
`LIGHT` — so its spread exceeds either endpoint's magnitude. **The retained
aggregate is itself poorly resolved across this variant set**, which is the
condition §1.6 requires be visible so that a stable-looking ratio cannot be
read as well-determined.

### 13. The §1.6 PREDICTION — it HELD

**Predicted before any number existed:** the ratio's spread would be SMALLER
than the spread of its numerator and denominator separately.

**Measured**, as relative spread, since the aggregates and the ratios do not
share units:

    relative spread   B_R        3.4382
    relative spread   B_D        3.8543
    relative spread   R_signed   1.4965
    relative spread   R_abs      1.1261

**Both ratios have a smaller relative spread than either aggregate. THE
PREDICTION HELD.**

**What that does and does not license.** It is consistent with shared
systematics partly cancelling between numerator and denominator. **It does not
establish that cancellation as the cause**, and no such claim is made — the
Reviewer's §12 records that observed relative spread alone should not be
promoted into a causal claim, and it is not promoted here.

### 14. `E5` — deterministic reproduction

    component `R1`, variant `LIGHT|V2a_with_m4`
      first pass    -8.172226097176e-03
      second pass   -8.172226097176e-03
      identical at the printed precision:  True

The second pass recomputed step 1 over the whole light window and step 2 on its
output, independently of the first. **A difference would have been a defect in
the computation, not noise.**

### 15. `M7` — import disclosure

The computation imports:

    scripts/diagnostics/ext01_discarded_external_space.py
        component definitions and the per-component bubble
    scripts/recovered_2026/mlog_coeff.py         the mass-log fit
    scripts/recovered_2026/proca_loop.py         geometry, propagator, bubble
    scripts/recovered_2026/seagull_check.py      transitively, fit_even, EPSF
    scripts/recovered_2026/boson_loop.py         transitively

**One of them carries an analytic target in its text**, and the fact is
recorded here as required: `scripts/recovered_2026/proca_loop.py:18`, in its
module docstring, states a target for the species ratio. **Its value is not
read, printed, stored, or compared against anywhere in this task**, and it
appears in no output.

**`scripts/recovered_2026/reproduce_betav.py` is NOT imported.** It carries
both a numerical reproduction target and a drift figure. Its two mass-window
definitions were READ as literals and cited at PART 1 §1.3, precisely so that
the module is never loaded.

### 16. `M8` — what this task did not move

    A-EXT-01   ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
    H-EXT-01   e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47

Unchanged. Every blob under `scripts/recon2026/` and
`scripts/recovered_2026/` is unchanged; the ids are recorded in the task
report.

### 17. What the measurement shows, stated as measurement

**The discarded external components carry `m² ln m²` content.** No component's
`β` is zero under any of the four combinations; the smallest magnitude in the
table is `2.1768e-05`.

**The discarded-to-retained ratio takes values between `0.2703` and
`1.8767` across the frozen set, in both aggregations.**

**NO CRITERION IS APPLIED TO THOSE NUMBERS.** §1.7 sets none, no target-free
ground for one presently exists, and one set after seeing these values would be
post-hoc.

**§0b's pre-registered consequence for the case where the discarded content is
not small relative to the retained**, reproduced because §0b requires the
record to state it:

> The retained space would not carry the scheme-independent content alone.
> **This does not change `β_V`'s value** — `β_V` is by definition the log
> coefficient of the retained space. It would mean `β_V` is not the whole of
> the scheme-independent story. **Reach, not correctness.**

**That is §0b's text and not a verdict of this task.** Whether the measured
values fall in that case, and what follows, is the PI's reading — §12 of the
governing specification places it there and assumes nothing.

### 18. What this measurement does NOT establish

**It is ONE lattice extent.** `n = 12`, the extent `EXT-01` used. Nothing here
measures the approach to any continuum or infinite-volume limit, and the
recorded `m · n` products — `1.32` to `3.60` on the light window, `2.40` to
`5.40` on the heavy — bound how far the result can be read.

**IT SETS NO CRITERION.** No threshold, pass band or acceptance range appears
in this artifact for any quantity.

**A RATIO IS NOT A VERDICT.** The numbers in §10 are a measurement over a
frozen set of analysis choices, with a band that is that set's spread. The
retained aggregate's own poor resolution across the set, recorded at §12, limits
what the ratio can be read as showing.

**`H-EXT-01` IS UNRESOLVED, IN EITHER DIRECTION.** This task bears on it and
resolves it neither way. Its `Statement SHA` is unchanged and `A-EXT-01`'s is
unchanged.

**Further limits, stated because the natural reading would exceed them.**
`v_i` is this task's choice, so `B_D` is this task's construction and not a
repository quantity — though both ratios are insensitive to it, as PART 1 §2
recorded before any number existed. The variant set has four members, which is
a small set on which to base a band. And the sign of `B_R` differs between the
two windows, so the two windows are not two measurements of one well-determined
number.

### 19. Open, and recorded rather than settled

    THE WINDOW DISAGREEMENT   `B_R` and every `β_i` change sign between the
                              light and heavy windows. Whether one window is
                              the right one to read, and on what target-free
                              ground, is NOT DECIDED here and no criterion for
                              deciding it exists in the repository.

    THE m⁴ COLUMN             Dropping it changes every `β_i` by a factor of
                              order three to thirty. Which form is correct for
                              this object is NOT DECIDED here; both are
                              reported and neither is primary.

    THE NEAR-DEGENERACIES     `R1 ~ R2`, `R3 ~ R4 ~ R5` and `D2 ~ D3 ~ D4`
                              agree to `~1e-9`. Whether these are exact
                              symmetries of the object, and if so which, is
                              NOT ESTABLISHED — only observed.

    THE DISCARDED ASSEMBLY    `v_i` has no landed definition. Whether the
                              repository should adopt one, and what it should
                              be, is NOT DECIDED here.

    A SECOND EXTENT           Whether `n ≠ 12` changes any of the above is
                              UNMEASURED. §12 of the governing specification
                              places that decision with the PI.

