# `P2-OBS-IDENT-01` — which observable, and did `EXT-01` measure it

    KIND        DOCUMENTARY AND OBJECT TRACING. No new numerical
                measurement. No script. No landing.
    ORIGIN      PI ruling of this session, following P2-GAPB-BRIDGE-01
    BASE        f23a0e1e1a24398d082a9597444ff9f750ed38e1

    OUTCOME     PROXY ONLY

                The repository defines β_V as the coefficient of m² ln m²
                in Z(m²) — a quantity extracted from a MASS SCAN.
                EXT-01 extracted the q² coefficient at a SINGLE mass, per
                component. Those are Z at one mass, and a coefficient of
                Z's mass-dependence: two quantities, one of which is an
                input to the other.

**`EXT-01` measured what it measured, correctly.** Its numbers were
pre-registered and independently reproduced, and nothing here re-analyses them.
**This outcome does not make `EXT-01` mistaken, void, invalidated, or wasted.**
It records what its numbers are a measurement *of*.

**This artifact does not conclude anything about whether the discarded external
space matters for `β_V`.** That question follows from this outcome and is not
answered here.

---

## 0. The rule this audit is executed under

**A characterisation quoted from a prior artifact is not evidence about the
object; it is evidence about the prior artifact.** Every item below is
established against the object itself — the convention table, the gate text,
the code, the landed pre-registration — and not from any downstream
description of them.

---

## 1. `M1` — every location that DEFINES `β_V`, as a quantity

**Three locations define it, and they agree.** A fourth line gives a
computational route to the same coefficient and is recorded separately so that
"agree" is not doing work it has not earned.

### 1.1 `CONVENTIONS.md:21` — the locked-conventions table, `Species coefficient β_s`

> | Species coefficient `β_s` | Coefficient of `m² ln m²` in `Z(m²)`. …

**This is the definition.** `β_V` is `β_s` for the massive-vector species,
whose determinant structure the same table fixes at `CONVENTIONS.md:19`:
`Z_{s=1,m} = det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)`, with the closing
clause "This determinant structure is taken as an input from the paper; the
coefficient it implies is what we compute."

### 1.2 `CONVENTIONS.md:20` — the definition of `Z(m²)`, which `β_s` is a coefficient *in*

> | Definition of `Z(m²)` | The induced axis/transverse-traceless (TT) graviton
> kinetic coefficient, i.e. the coefficient of the induced Einstein–Hilbert term
> `∫√g R` normalized **per unit `4N`** … The `m²ln m²` piece defines the species
> coefficient: `Z ⊃ β_s · m² ln m²`.

**Two quantities are named in one line and they are not the same.** `Z(m²)` is
a function of mass; `β_s` is the coefficient of one term in its expansion.

### 1.3 `GATES.md:152` — the gate that extracts one of them, stating the same definition

> Extract `β_B` (coefficient of `m²ln m²` in `Z(m²)`) for a minimal scalar from a
> lattice mass scan, with honest self-derived systematics.

**The gate for the scalar species states the definition and the method in one
sentence: it is a coefficient in `Z(m²)`, and it comes from a lattice mass
scan.** `GATES.md:156` fixes the scan window for that gate.

### 1.4 `scripts/recovered_2026/mlog_coeff.py:2` — the module title

> Universal m^2 log(m^2) coefficient of the induced graviton kinetic term.

### 1.5 Do they agree? — YES, on the quantity; and one line adds a second route

**On what the quantity is, the three agree without qualification:** the
coefficient of `m² ln m²` in the mass-dependence of the induced axis-TT
kinetic coefficient.

**`CONVENTIONS.md:21` continues with a computational route** — "Computed from
`a_1`: `β_s = −p_s (4π)^{−2} (tr a_1 / R)`, where `p_s` is the log-det
prefactor of the species". **That is a continuum heat-kernel route to the same
coefficient, not a second definition of it**, and it is recorded here because a
reader checking "they agree" should see that the line contains two things and
that only one of them is the definition.

**No location found defines `β_V` as a fixed-mass `q²` coefficient.** A search
across `*.md` and `*.py` for a definitional verb applied to `β_V` or `β_s`
returns `CONVENTIONS.md:21` and nothing else.

### 1.6 `GATES.md:207-228` — the gate for `β_V` itself

`## P2-BETAV-01 — Lattice β_V/β_B (Proca / Stueckelberg)`, `Status: PROPOSED
(deferred — not computed this sweep)`. Its scope at `:216-218` is "Massive
vector on the lattice, induced graviton coefficient including the longitudinal
(Stueckelberg) modes." **Its `Regression anchors` at `:230-231` read "None yet
(not computed)."** The analytic anchor is cited at `:228` by location; **its
value is not restated here.**

---

## 2. `M2` — the same for `β_B`

**`β_B` is `β_s` for the minimal scalar species and is defined by the same
`CONVENTIONS.md:21` line.** `GATES.md:147-165` is its gate — a lattice mass
scan over a stated window, with the fit basis fixed at `GATES.md:159` as
`{1, m², m²ln m², m⁴}`.

**The anchor pairs `β_V` with `β_B` as a ratio**, `GATES.md:19` naming
`β_V/β_B` among the reported ratios and `CONVENTIONS.md:21` closing with
"Reported both as a raw value (this convention) and as convention-independent
ratios `β_F/β_B`, `β_V/β_B`, `β_B(ξ)/β_B`." **The ratio's target values are
cited by location and not restated.**

---

## 3. `M3` — what the implementation actually extracts, step by step

**Procedure only. No value produced by any step is reproduced here.**

The `β_V` extraction path is `scripts/recovered_2026/reproduce_betav.py`,
`vector_ZV`, at `:53-57`. It has three steps and they are nested:

    STEP 1 — the bubble at one momentum
        scripts/recovered_2026/proca_loop.py, g2_axis_proca(q0, n, m, dJ2, dJ)
        at :108. Evaluates the axis-TT projected Proca bubble at a single
        external momentum q0, at a single mass m.

    STEP 2 — the q² coefficient at one mass  →  THIS IS Z(m²)
        proca_loop.py:171-173:
            def slope(n, m, dJ2, dJ, eps=np.array([0.10, 0.16, 0.22, 0.28])):
                vals = np.array([g2_axis_proca(e, n, m, dJ2, dJ) for e in eps])
                return fit_even(eps, vals, order=2)[1]
        VARIED: the external momentum, over the four-point eps grid.
        HELD FIXED: the mass m, the extent n, the geometric derivatives.
        FIT FORM: even polynomial in eps, order 2 — seagull_check.fit_even
        at :256-259 builds the Vandermonde in eps² with three columns.
        EXTRACTED: index [1] of the coefficient vector — THE q² COEFFICIENT.

    STEP 3 — the m² ln m² coefficient across masses  →  THIS IS β_V
        reproduce_betav.py:53-57:
            def vector_ZV(n, masses):
                dJ2, dJ, _, _ = pl.derivsV()
                Z = np.array([pl.slope(n, m, dJ2, dJ) for m in masses])
                coef, resid = ml.fit_mlog(masses ** 2, Z, with_m4=True)
                return float(coef[2]), Z.tolist()
        VARIED: the mass, over the supplied scan window.
        HELD FIXED: the extent n and the eps grid inherited by step 2.
        FIT FORM: mlog_coeff.fit_mlog at :81-89, docstring at :82 —
            "Z(m^2) = z0 + z1 m^2 + beta m^2 ln(m^2) (+ z2 m^4)"
        EXTRACTED: coef[2] — THE COEFFICIENT OF m² ln m².

    THE SCAN WINDOWS, as the driver supplies them
        reproduce_betav.py:61-63 defines three windows by np.linspace, and
        :69-70 calls vector_ZV on two of them. The windows are procedure, not
        results, and are recorded as such.

**Step 2's output is the input to step 3, one point per mass.** `β_V` is not
obtainable from step 2 at any single mass, because a coefficient of
`m² ln m²` is a property of how `Z` varies with `m`.

**Corroborated by an independent landed artifact, on the same objects.**
`derivations/P2-BETAV-CIRC-01_determinant-decomposition.md:4-5` states it works
"at the `q²` level (the level at which `Z` is extracted)", and its `:19` states
"`Z` is the axis-TT `q²` slope of `g2_axis_proca`". **`Z` is the `q²` slope;
`β_V` is a coefficient of `Z`'s mass-dependence.**

---

## 4. `M4` — what `EXT-01` extracted

**As the landed artifact states it**,
`derivations/P2-RECON-EXT-01_discarded-external-space.md`:

    FIT FORM              :146-147, quoted from the pre-registration —
                          "fit form  Pi(q) = A + B q^2 + C q^4;  B is the
                          reported q^2 coefficient"
    COEFFICIENT REPORTED  B, the q² coefficient, per component — :152-153,
                          "reported per component   the q^2 coefficient B, and
                          B as a fraction of the sum of B over all ten
                          components"
    MASS                  HELD FIXED. EXT-01:144 pre-registers
                          "mass            m        0.3" — A SINGLE VALUE.
                          (Attributed to EXT-01; quoted to identify what it
                          held fixed, per M4.)
    EXTENT                HELD FIXED, EXT-01:143 — "lattice extent  n  12".
                          (Attributed to EXT-01.)
    q-GRID                VARIED, EXT-01:145 — the four-point grid.
                          (Attributed to EXT-01.)
    DIRECTION             q ∥ e₀, EXT-01:150.
    BASIS                 the ten orthonormal components, EXT-01:151.

**MASS WAS NOT VARIED.** Confirmed against the object as well as the artifact:
`scripts/diagnostics/ext01_discarded_external_space.py:57` sets `MASS = 0.3` as
a module constant, `:167` passes it unchanged into every evaluation, and **the
script does not import or call `fit_mlog`** — the only fit it defines is
`fit_even` at `:129-132`, a three-column Vandermonde in `eps²`.

**So `EXT-01` performed step 2 of `M3`, per component, at one mass. It did not
perform step 3.**

---

## 5. `M5` — does `A-EXT-01` disambiguate?

**NO. Silence, recorded as silence.**

`A-EXT-01`'s exact statement, `CONVENTIONS.md:91-97`, opens:

> For `RECON-01b`, `Z_axis-TT` is defined as the coefficient extracted after
> the repository's axis-TT projection.

**"the coefficient extracted after the projection" does not say which
coefficient.** Read against `M1`, two candidates sit under that phrase: the
`q²` coefficient of the projected bubble at a given mass, and the `m² ln m²`
coefficient of that quantity's mass-dependence. **The exact statement selects
neither.**

**What it does fix is the name `Z_axis-TT`**, and `CONVENTIONS.md:20` defines
`Z(m²)` as the induced axis/TT kinetic coefficient with `β_s` as a coefficient
*inside* it. **On that reading `A-EXT-01` names the step-2 quantity** — but the
exact statement does not say so, and this artifact does not read the
disambiguation into it.

**`A-EXT-01` is a landed definitional convention and is not altered here.** Its
`Statement SHA` is unchanged; see `M7`. **This records what it does and does
not fix, which is what `M5` asks.**

---

## 6. `M6` — the scheme-independence statement, and whether the repository connects it to the definition

**The manuscript's statement**, `paper/emergent_gr_paper_v2_15.tex:1123-1128`:

> The scheme-independent induced content consists of the
> \emph{mass-dependence} of the kernel (counterterms being
> mass-independent constants of the bare action), in particular the
> universal $m^2\ln(\Lambda^2/m^2)$ coefficients per species

and Finding 3 at `:1130-1137`, which repeats it and adds that "the
infrared ($k \sim m$) region of the loop is effectively continuum
and covariant".

**A repository location DOES connect it to the observable's definition, and the
connection is not left to inference.** `scripts/recovered_2026/mlog_coeff.py:4-8`:

    Scheme-independent statement: counterterms are mass-independent, and the
    IR (k ~ m) region of the loop is effectively continuum+covariant, so the
    m^2 ln m^2 part of the axis-TT slope Z(m) is the universal covariant
    induced contribution.

**This is in the module that defines the extraction machinery, and it names
both objects in one sentence: the axis-TT slope `Z(m)`, and its `m² ln m²`
part.** `CONVENTIONS.md:20-21` carries the same distinction into the locked
table.

**Recorded as found, and no more is drawn from it here.** `M6` asks whether the
connection exists; it does. **Whether that makes any particular measurement
scheme-dependent is not this task's question**, and the outcome below does not
rest on it.

---

## 7. `M7` — the two Statement SHAs

    A-EXT-01  ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
              CONVENTIONS.md:129
    H-EXT-01  e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47
              assumptions/H-EXT-01.md:53

**This task alters neither, and modifies neither file.**

---

## 8. The determination

### `D1` — the target observable

**`β_V` is the coefficient of `m² ln m²` in `Z(m²)`, where `Z(m²)` is the
induced axis-TT graviton kinetic coefficient — the `q²` slope of the axis-TT
projected Proca bubble — as a function of the vector mass.**

`M1`'s locations agree on this and no location contradicts it. **Obtaining it
requires varying the mass**, which is `M3`'s step 3 and `GATES.md:152`'s
"lattice mass scan".

### `D2` — the measured quantity

**`EXT-01` extracted `B`, the `q²` coefficient of `Π(q) = A + Bq² + Cq⁴`, for
each of the ten orthonormal external components, at one mass and one extent, at
`q ∥ e₀`.** That is `M3`'s step 2, decomposed by component.

### `D3` — the relation, stated explicitly

**They are not the same quantity. They differ in the MASS TREATMENT, and
consequently in the EXTRACTION.**

    target      β_V     a coefficient of Z's MASS-DEPENDENCE
                        requires Z at several masses; obtained by a second
                        fit, in m², on top of the q² fit
    measured    B       Z ITSELF, AT ONE MASS, per component
                        one q² fit, at m held fixed

**The relation between them is precise and is not a mere resemblance:
`EXT-01`'s quantity is the INPUT to the fit that produces the target.** Step 2
feeds step 3, one point per mass, and `EXT-01` supplies one such point —
decomposed into ten components, which the `β_V` path does not do.

**They do not differ in the projection or the object.** Both are the axis-TT
projection of the same Proca bubble, in the same basis, at `q ∥ e₀`, at the
same extent. `EXT-01`'s momentum grid is the same four-point grid
`proca_loop.slope` uses by default. **The single difference is the mass
treatment, and it is sufficient to make them different quantities.**

**One further difference, recorded because it bears on what a target extraction
would look like.** `EXT-01` reports `B` **per component**, over all ten. The
`β_V` path does not: `proca_loop.g2_axis_proca` builds its vertices from
`TT_RECIPES` at `:115-116` — the five RETAINED components only — and returns
`total / (n ** 4) / 5.0` at `:130`, **an average over those five**. The five
discarded components enter it nowhere.

**MEASURED, and stated with its exclusion rather than as a bare universal.**
Five files call `fit_mlog`: `mlog_coeff.py`, `proca_loop.py`,
`reproduce_betav.py`, `batch2/precision_campaign.py`, and
`scripts/P2-BETAV-CAMPAIGN/harness_compute.py`. **None decomposes the mass fit
over the ten external-index components.** The three that reference `TT_RECIPES`
use the retained five as one combination; the fifth uses the word "component"
in a different sense — `harness_compute.py:392` lists
`["proca", "gfvec", "boson", "D"]`, which are determinant species, not external
index components. **So no per-component `β` is computed anywhere in the
repository**, and the exclusion is why a count of the word would have misled.

### `D4` — what the target extraction would require. **Specified, not performed.**

To obtain the target observable, decomposed the way `EXT-01` decomposes:

    VARY        the vector mass m, over a scan window, at no fewer points than
                the fit basis requires — the basis is {1, m², m²ln m², m⁴},
                GATES.md:159, so four coefficients and a window that resolves
                the non-analytic term against the analytic ones.

    HOLD FIXED  the extent n; the external momentum grid; the direction q ∥ e₀;
                the basis of ten components; the geometric derivatives.

    EXTRACT     for each mass, and for each of the ten components, the q²
                coefficient B — that is EXT-01's step, repeated per mass.
                Then, for each component, fit
                    Z(m²) = z0 + z1 m² + β m² ln m² + z2 m⁴
                and take the m² ln m² coefficient.

    YIELDS      a per-component β, which is the quantity a question about the
                discarded space's contribution to β_V would be about.

**This task does not perform it, and `K3` forbids running it.** Whether it
should be performed, and by whom, is not decided here.

---

## 9. Outcome

    PROXY ONLY

**`EXT-01` measured a quantity related to but different from the
repository-defined `β_V` observable: the `q²` coefficient at a single mass,
which is one input point to the mass fit that defines `β_V`.**

**This does not invalidate `EXT-01`.** Its execution, pre-registration and
independent reproduction stand. What changes is what its numbers are evidence
about: they are evidence about `Z` at one mass, per component.

**This does not establish that the discarded external space is, or is not,
relevant to `β_V`.** The discarded components' contribution to the target
observable is a separate question, and `D4` states what measuring it would
require. **Nothing here answers it in either direction.**

---

## 10. What this does not establish

**No number was produced by this task.** No `β_V`, no `β_B`, no ratio, no
`k`-scan, no evaluation of any kind. **No script was written**; none is
authorised, and none was needed.

**`Q1` remains `INCONCLUSIVE`. `GAP-A` remains closed with its momentum
condition. `GAP-B` remains `INDETERMINATE — UNDETERMINED BY READING` with its
five mismatches. `H-EXT-01` remains `UNESTABLISHED`. `A-EXT-01` is unchanged
and remains a definitional convention.** No gate moves and `P2-PHASE-01` does
not advance.

**`MM-1`, `MM-3` and `MM-5` are untouched**, and this artifact takes no
position on any of them.

**What this outcome may change is what the tasks above are about**, and that
consequence is for the specifications that follow, not for this artifact.
