# `P2-RECON-EXT-01` — what the axis-TT projection discards

    KIND        MEASUREMENT + DOCUMENTARY. No landing.
    BASE        968e726a5a4322eecf4254ff69b25832f263c155
    STATE       PRE-REGISTRATION COMMIT. §5 and §6 carry NO RESULT yet.
                The parameters of §4 are fixed here, before any number
                exists, and the result is added in a later commit.

**This artifact sets no threshold, no pass band, and no criterion.** PI ruling
2 is measure-first, and a criterion written before the magnitude is known would
be either unfalsifiable or post-hoc. **It also states no judgement of whether
what it measures is acceptable**, and recommends nothing.

**It does not adjudicate the `TT_RECIPES` governance question** (PI ruling 4).
`§7` records that question's documentary state and stops.

---

## 1. `M1` — the external index space the projection retains

**The projection's definition, `scripts/recovered_2026/mlog_coeff.py:21-31`,
quoted:**

    # 5 TT basis tensors for q || e0, expressed as pair-combination recipes:
    #   each entry: list of (pair, coefficient) such that
    #   U_eff = sum coeff * U^{pair}   corresponds to a unit-normalized tensor.
    TT_RECIPES = [
        [((1, 1), 1 / np.sqrt(2)), ((2, 2), -1 / np.sqrt(2))],
        [((1, 1), 1 / np.sqrt(6)), ((2, 2), 1 / np.sqrt(6)),
         ((3, 3), -2 / np.sqrt(6))],
        [((1, 2), 1 / np.sqrt(2))],
        [((1, 3), 1 / np.sqrt(2))],
        [((2, 3), 1 / np.sqrt(2))],
    ]

**RETAINED — five independent components**, written as `h`-matrices via
`seagull_check.hmat`, which sets `h[a,b] += v` and, for `a ≠ b`, `h[b,a] += v`:

    R1   ( h11 − h22 ) / √2
    R2   ( h11 + h22 − 2 h33 ) / √6
    R3   the (1,2) direction, coefficient 1/√2
    R4   the (1,3) direction, coefficient 1/√2
    R5   the (2,3) direction, coefficient 1/√2

**The normalisation convention is the repository's, not one introduced here.**
The comment at `:23` calls each recipe *"a unit-normalized tensor"*, and the
norm under which that is true is the **Frobenius norm of the `h`-matrix**:
`R3`'s single pair at `1/√2` produces `h[1,2] = h[2,1] = 1/√2`, whose Frobenius
norm is `1`; `R1` produces `diag(0, 1/√2, −1/√2, 0)`, norm `1`; `R2` produces
`diag(0, 1/√6, 1/√6, −2/√6)`, norm `1`. **This artifact adopts that convention
and does not invent one.**

**Span:** the symmetric traceless tensor of the 3-space orthogonal to the axis
`q ∥ e₀`.

## 2. `M2` — the full space, and the discarded complement

**The full external index space, `scripts/recovered_2026/seagull_check.py:49`:**

    PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]

**Ten independent components** — the symmetric `4×4` perturbation `h_{μν}`:

    (0,0) (0,1) (0,2) (0,3) (1,1) (1,2) (1,3) (2,2) (2,3) (3,3)

### 2.1 The decomposition

    full space  =  retained (M1)  +  discarded
        10      =       5         +      5

**DISCARDED — five components, enumerated explicitly**, in the same
unit-Frobenius convention:

    D1   h00                                       coefficient 1
    D2   the (0,1) direction                       coefficient 1/√2
    D3   the (0,2) direction                       coefficient 1/√2
    D4   the (0,3) direction                       coefficient 1/√2
    D5   ( h11 + h22 + h33 ) / √3   — the SPATIAL TRACE

**`D1`–`D4` are every component carrying the axis index `0`.** **`D5` is the
spatial trace**, which no retained recipe reaches because `R1` and `R2` are
constructed traceless.

**`trace` and `traceless` are different objects here and are not interchanged.**
`D5` is the spatial trace; `R1` and `R2` are the two independent traceless
diagonal combinations. `§7` of the governing specification names this collision
and it is kept apart throughout.

### 2.2 The arithmetic, checked and not asserted

**Verified numerically over the ten basis `h`-matrices**, using only linear
algebra on `4×4` real symmetric matrices — no lattice, no propagator, no
physical quantity:

    basis size                          10  =  5 retained + 5 discarded
    PAIRS, the full space                10
    Gram matrix, max |G − I|              2.220446049250313e-16
    orthonormal                           True
    rank of the ten basis matrices        10

**The ten are orthonormal to machine precision and span the full
ten-dimensional space.** `D5 ⊥ R1` and `D5 ⊥ R2` hold exactly by construction:
`(1/√3)(1/√2) + (1/√3)(−1/√2) = 0` and `(1/√3)(1/√6)(1 + 1 − 2) = 0`.

## 3. `M3` — correspondence to a spin decomposition

**MEASURED: the repository states no such correspondence, and none is supplied
here.**

Searched for a document relating the axis-TT projection or `TT_RECIPES` to a
spin or helicity label. `git grep -n -i -E 'axis-TT|TT_RECIPES' -- '*.md'`
filtered for `spin` or `helicity` returns **one line**, and it is a warning
against the identification rather than a statement of one:

    specs/2026-08-19T0223Z_pole-b0-milestone-scope.md:191
      **Distinguish an axis-TT projection from a Barnes–Rivers spin
      decomposition if both appear.**

`helicity` returns **0 files** repository-wide. The tokens `spin-2`, `spin-1`
and `spin-0` occur in 18, 13 and 12 files respectively, but **none of those
occurrences is a statement about the external `h` decomposition this artifact
measures** — they belong to the manuscript's stress-tensor channel discussion
and to the `CHANNEL-B0` and `POLE-B0` assessments, which concern
Barnes–Rivers projectors acting on a different object.

**`M3`'s second form is the measured one: no correspondence is stated.** Under
`§8` of the governing specification that is a completed measurement.

**This artifact does not supply the correspondence**, and the reason is not
only that the specification forbids it: the retained space is defined for a
single momentum direction `q ∥ e₀`, and whether its complement decomposes into
spin sectors is a statement that would need a covariant construction the
repository does not have here.

---

## 4. `M4` — PRE-REGISTRATION

**Fixed before any number is produced. This section is committed before the
commit that adds `§5`.**

    k                        1
    lattice extent  n        12
    mass            m        0.3
    q-grid                   [0.10, 0.16, 0.22, 0.28]
    fit form                 Pi(q) = A + B q^2 + C q^4;  B is the reported
                             q^2 coefficient
    geometric-derivative
      step  EPSF             1e-3, read from proca_loop.EPSF
    momentum direction       q parallel to e0
    basis                    the ten orthonormal components of §1 and §2.1
    reported per component   the q^2 coefficient B, and B as a fraction of
                             the sum of B over all ten components

**Why these values.** `n = 12`, `m = 0.3` and the `q`-grid are the parameters
`CIRC-01` used for the decomposition this measurement is the external
counterpart of — `scripts/betav_decomp_q2.py:120-125`, and the grid is its
`R1`. **Matching them is what makes the two decompositions comparable**; they
were not selected after seeing anything.

**On `k`.** `k = 1` is the physical determinant power and is pre-registered as
this task's single value, per `K2`. **The object being measured is the Proca
bubble `Π(q)`**, and the determinant power enters `Γ_k` downstream of it. Which
functions take `k` as an argument is recorded as a measurement in `§6`, not
assumed here.

**No threshold accompanies these parameters.** There is no value of the
discarded fraction that this pre-registration designates as passing or failing,
and none will be added later.

---

## 5. `M5` — RESULT

**NOT YET MEASURED.** This section is completed in a later commit. The
parameters it will be measured at are fixed above and are not revisable.

## 6. `M6` — computation provenance

**NOT YET RECORDED.** Completed with `§5`.

---

## 7. `M7` — documentary provenance of the projection choice

**Q3 asks what the repository records, not what the answer should be.**

### 7.1 Locations that state a GROUND

**`scripts/recovered_2026/mlog_coeff.py:2-13` — the only location supplying a
reason.**

    Universal m^2 log(m^2) coefficient of the induced graviton kinetic term.

    Scheme-independent statement: counterterms are mass-independent, and the
    IR (k ~ m) region of the loop is effectively continuum+covariant, so the
    m^2 ln m^2 part of the axis-TT slope Z(m) is the universal covariant
    induced contribution.  Continuum benchmark (heat kernel):
       beta_Dirac / beta_real-min-scalar = 2   (convention-free ratio test).

    Method: bubble-only axis-TT slope (seagull and CC are q^0 / q-independent
    and drop from the slope).  TT projector spectrally decomposed into 5
    transverse-traceless basis tensors -> 5 effective vertices.

**What it grounds, and what it does not.** It grounds *why the `m² ln m²` part
of the slope is universal*, and it grounds *why the seagull and cosmological
terms drop*. **It does not state why the transverse-traceless space is the
right space to project onto rather than a larger one.** The projection is
introduced at `:11-12` as a method step, in the imperative.

**`derivations/betav_discriminating_power.md:24-30`** states what the
extraction computes and identifies it as the Seeley–DeWitt `a₁` curvature
response realised numerically. **A ground for the extraction; not a ground for
the choice of external projection.**

**`derivations/P2-NORM-01_normalization_chain.md:35-42` and `GATES.md:280-281`
— a ground of a different kind: definitional inheritance.**

    GATES.md:280-281
      This repo's `Z` = coeff of `R` in the action; paper's `Z` = axis-TT slope
      per unit `4N` (lines 1209–1210).

    P2-NORM-01:35-37
      *Paper:* `Z_paper ≡` the axis-TT graviton kinetic slope (coefficient of
      `p²` in the transverse-traceless graviton self-energy) **per unit `4N`**

**These record that the axis-TT slope is the manuscript's definition of `Z`**,
and that the repository's own `Z` differs from it by a fixed normalisation.
**That is a ground for using the projection — it is what the quantity being
reproduced means — and it is not a derivation that the discarded space is
negligible.** The two are different claims and this artifact does not merge
them.

### 7.2 Locations that state only the CHOICE

    GATES.md:739
      `h`-derivatives at the determinant/eigenvalue level; fixed axis-TT
      projection;

    derivations/P2-BETAV-RECON-01_cleanroom_reconstruction.md:27-28
      4. Extract the EH coefficient with a **fixed** axis-TT projection and
         normalization, identical for every `k`.

    derivations/P2-BETAV-CIRC-01_determinant-decomposition.md:19
      `Z` is the axis-TT `q²` slope of `g2_axis_proca`

    paper/emergent_gr_paper_v2_15.tex:1209-1210
      where $Z(m^2)$ is the (axis-TT) induced kinetic coefficient per
      unit $4N$ studied above.

**`RECON-01_cleanroom:27-28` is the strongest of these and it is still not a
ground.** It requires the projection be *fixed* and *identical for every `k`* —
a constraint on how the projection is used, which prevents `k`-dependent
tuning. **It says nothing about why this projection.**

The remaining locations —
`derivations/P2-BETAV-RECON-01_scope-assessment.md:26`, `:479`, `:526`;
`reports/2026-08-17T1105Z_recon-b0-scope.md:93`, `:378`;
`specs/2026-08-17T1105Z_recon-b0-scope.md:58`;
`specs/2026-08-17T1653Z_recon-01a-construction.md:39`, `:507`;
`scripts/betav_decomp_q2.py:10`; `scripts/normalization_chain.py:28`, `:31`,
`:50`, `:77`; `GATES.md:304`; `DECISION_LOG.md:111`;
`results/` and `reviews/` occurrences — **quote or apply the choice and add no
ground.**

### 7.3 The earliest location, by commit date

    first commit introducing the string "axis-TT" anywhere in the repository
      2026-07-17  f95f2eb
      docs: import Paper 2 v2.15 and redo the comparison against the source

    first commit introducing "TT_RECIPES"
      2026-07-20  fb1da32
      provenance: complete the betaV pipeline recovery (mlog_coeff.py recovered)

**The term enters the repository with the manuscript, three days before any
implementation of it exists.** The two commits on the same day as `f95f2eb` —
`eddda67` (`P2-NORM-01`) and `7147ea7` (`P2-BETAV-CIRC-01` registration) — both
refer to the paper's definition rather than establishing one.

### 7.4 Does any location record who or what selected it?

**MEASURED: no.** A search of every `axis-TT` line in the repository's markdown
for selection language — `because`, `chosen`, `selected`, `inherit`,
`follows the paper`, `paper's definition` — **returns no lines.**

**What the record shows instead is inheritance without an attributed
decision.** The projection arrives with the imported manuscript, is recorded in
`P2-NORM-01` and `GATES.md` as *the paper's* definition of `Z`, and is then
carried forward by every downstream gate, specification and script. **No
document records a moment at which the repository considered alternatives and
chose this one**, and no document attributes the choice to a person, a gate, or
a ruling.

**This is a documentary finding and not a criticism.** A definition inherited
from the object under study is a normal thing for a reproduction to inherit.
**Whether it should be re-derived rather than inherited is exactly the question
`§8` records as open**, and PI ruling 4 reserves it.

---

## 8. Questions raised and not settled

**Recorded as open. None is resolved below.**

1. **Whether the retained space is complete for the quantity being extracted.**
   `M7` finds a ground for *what* `Z` means and no ground for *why the
   complement may be dropped*. **The measurement of `§5` bears on this and does
   not settle it**, because a magnitude at one momentum direction and one
   parameter point is not a completeness argument.

2. **Whether the projection should be re-derived rather than inherited.**
   `§7.3` and `§7.4` establish that it arrived with the manuscript and that no
   document records a selection. PI ruling 4 reserves the related `TT_RECIPES`
   governance question and this artifact does not touch it.

3. **Whether a spin correspondence for the discarded components exists to be
   stated.** `M3` measures that the repository states none. Whether one could
   be constructed is not determined here.

4. **Whether the discarded components' contributions are `q²`-scaling at all.**
   The fit form of `§4` extracts a `q²` coefficient from every component
   alike. **Whether that coefficient is meaningful for a component whose
   contribution does not scale as `q²` is a question the fit does not answer**,
   and `§5` will report the observed scaling exponent alongside each
   coefficient so the question stays visible.

---

## 9. What this measurement does not establish

- **It measures one `k` and says nothing about `k`-dependence.** `K2` fixes `k`
  at the pre-registered value for the whole task, and no scan is performed.
- **It sets no criterion, threshold, or acceptance band**, and none may be read
  out of it. PI ruling 2 defers that until the magnitude is known, which is what
  this produces.
- **A magnitude is not by itself a judgement of physical relevance.** A small
  discarded fraction does not establish that the discarded space is irrelevant,
  and a large one does not establish that the projection is wrong. **Both are
  reportable results and neither is a failure.**
- **It produces no `β_V`, no `β_B`, and no ratio of them**, and computes nothing
  the frozen anchor ranges over.
- **It does not begin, scope, or contribute to the `RECON-01b` clean-room
  reconstruction.** It is a diagnostic on an existing object, and
  `scripts/recon2026/` is neither modified nor added to.
- **It does not adjudicate component 5 or component 9**, and does not upgrade
  or downgrade either.
- **`M7` records provenance; it does not judge sufficiency of authority.**
