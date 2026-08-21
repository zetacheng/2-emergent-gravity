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
