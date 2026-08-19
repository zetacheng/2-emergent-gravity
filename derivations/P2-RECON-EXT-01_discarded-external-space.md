# `P2-RECON-EXT-01` — what the axis-TT projection discards

    KIND        MEASUREMENT + DOCUMENTARY. No landing.
    BASE        968e726a5a4322eecf4254ff69b25832f263c155
    STATE       COMPLETE. §4's parameters were committed at 9cb63733,
                before the diagnostic script existed and before any number
                was produced; §5 and §6 are added here.

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

**Measured at the `§4` parameters, which were committed at `9cb63733` before
the script that produced these numbers existed.** Reported as measured, in the
direction it falls.

### 5.1 Per component

| component | description | group | `q²` coefficient | share of the ten-component sum | scaling exponent |
|---|---|---|---|---|---|
| `R1` | `(h11 − h22)/√2` | retained | `+2.223856432e-02` | `+28.80%` | `1.9887` |
| `R2` | `(h11 + h22 − 2h33)/√6` | retained | `+2.223856432e-02` | `+28.80%` | `1.9887` |
| `R3` | the `(1,2)` direction | retained | `+2.180202143e-02` | `+28.24%` | `1.9894` |
| `R4` | the `(1,3)` direction | retained | `+2.180202143e-02` | `+28.24%` | `1.9894` |
| `R5` | the `(2,3)` direction | retained | `+2.180202143e-02` | `+28.24%` | `1.9894` |
| `D1` | `h00` | **discarded** | `−2.215669317e-02` | `−28.69%` | `1.9982` |
| `D2` | the `(0,1)` direction | **discarded** | `−7.265655290e-03` | `−9.41%` | `1.9940` |
| `D3` | the `(0,2)` direction | **discarded** | `−7.265655290e-03` | `−9.41%` | `1.9940` |
| `D4` | the `(0,3)` direction | **discarded** | `−7.265655290e-03` | `−9.41%` | `1.9940` |
| `D5` | the spatial trace `(h11 + h22 + h33)/√3` | **discarded** | `+1.128540201e-02` | `+14.62%` | `1.9898` |

**All ten discarded components enumerated in `§2.1` are present. None is
omitted.**

### 5.2 Group sums

    sum over all ten                   +7.721493588e-02
    sum over the five retained         +1.098831929e-01     share  +142.31%
    sum over the five discarded        -3.266825703e-02     share   -42.31%

    mean over the five retained        +2.197663858e-02
    mean over the five discarded       -6.533651406e-03

    |sum discarded| / |sum retained|    0.297300
    largest |discarded| / mean retained 1.008193

### 5.3 Reading these numbers, with the caveats that belong to them

**The shares are SIGNED and are not bounded in `[0, 1]`.** The retained group
sums to `+142%` and the discarded group to `−42%` because the two groups carry
opposite signs and the denominator is their sum. **A share outside `[0,1]` is
not an error; it is what a signed decomposition with cancellation produces**,
and reporting only the magnitudes would hide the cancellation while reporting
only the shares would suggest a bound that does not exist. Both are given.

**The discarded components are the same order of magnitude as the retained
ones.** `D1` alone has `|q²| coefficient` `1.008` times the mean retained
component — **larger than the average retained component, not smaller.**

**Every component scales as `q²`.** The observed exponents lie in
`[1.9887, 1.9982]`, so `§8.4`'s question is answered for this parameter point:
the `q²` coefficient is a meaningful extraction for the discarded components
and not an artefact of fitting a `q²` form to something that does not scale
that way.

**The symmetry structure is a consistency check and it holds.** `R1 = R2`
exactly, `R3 = R4 = R5` exactly, and `D2 = D3 = D4` exactly, to every printed
digit — the hypercubic symmetry of the 3-space transverse to `q ∥ e₀` acting on
components that symmetry relates. **Nothing enforces this in the code**; the
ten components are evaluated independently.

### 5.4 Cross-check against `CIRC-01`, reported after the fact

**The mean over the five retained components is `+2.1977e-02`.**
`CIRC-01`'s `total` row — the same bubble without an internal `T/L` split,
averaged over the five recipes — is stated at
`derivations/P2-BETAV-CIRC-01_determinant-decomposition.md:45` as `≈ +2.20e-2`,
with scaling exponent `≈ 1.99`.

**These agree to the precision `CIRC-01` states**, and the exponents agree.
**This is reported as a validation that the diagnostic reproduces the reference
object, not as a new result**, and it was computed after the parameters were
fixed, not tuned to reach it.

## 6. `M6` — computation provenance

**The code that produced `§5`:**
`scripts/diagnostics/ext01_discarded_external_space.py`, added by this task
under a path that names it a diagnostic and **outside `scripts/recon2026/`**.
**No existing file under `scripts/` was modified.**

### 6.1 Every module imported, with its path and target status

| module | path | under `scripts/recovered_2026/`? | carries an analytic target? |
|---|---|---|---|
| `proca_loop` | `scripts/recovered_2026/proca_loop.py` | **yes** | **YES — see §6.2** |
| `mlog_coeff` | `scripts/recovered_2026/mlog_coeff.py` | **yes** | no target literal in the module; it states a convention-free continuum benchmark ratio at its `:8` |
| `seagull_check` | `scripts/recovered_2026/seagull_check.py` | **yes** | no |
| `numpy` | site-packages | no | no |
| `json`, `sys`, `pathlib`, `inspect` | standard library | no | no |

**Three of the imports are recovered-pipeline modules.** That is disclosed
rather than avoided: the object being diagnosed **is** the recovered bubble,
and `A3` of the governing specification makes it an abort to reach it by
modifying an existing file instead.

### 6.2 The target-bearing import, recorded

**`scripts/recovered_2026/proca_loop.py:18` carries an analytic target in its
module docstring**, stating a species-ratio value for the physical determinant
power. **This artifact does not restate that line's numeral**, and the
diagnostic does not read, print, store or compare against it.

**What is used from that module:** `derivsV` (the geometric derivatives of
`√g g⁻¹⊗g⁻¹` and `√g g⁻¹`), `G_flat` (the flat Proca propagator), `avec`,
`kin_form` (the kinetic bilinear form) and `EPSF`. **None of these carries or
returns the target**, and the docstring is not executed.

### 6.3 Where the determinant power enters, measured

**Measured by inspecting the call signatures rather than describing them:**

    component_bubble   ["q0", "n", "m", "dJ2", "dJ", "recipes"]
    derivsV            []
    G_flat             ["kk", "m"]
    avec               ["kk"]
    kin_form           ["D", "ac", "b"]

**None of the five takes the determinant power as an argument.** The object
measured in `§5` is the bubble, and the power enters `Γ_k` downstream of it.
**`K2` is satisfied not by refraining from a scan but because there is nothing
here to scan over** — and that is recorded as a measurement of the code path,
which is why `§4` pre-registered `k = 1` rather than assuming the question
away.

### 6.4 Output disposition

**The diagnostic prints to standard output and writes no file.** Its results
are transcribed into `§5` of this artifact. **No output path was added to the
repository**, because the authorised manifest names none and writing one would
have put a path outside it.

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
   **ANSWERED at this parameter point and closed:** every observed exponent
   lies in `[1.9887, 1.9982]`, so the `q²` coefficient is a meaningful
   extraction for all ten. **It is answered for one `n`, one `m` and one
   `q`-grid**, and whether it holds elsewhere is not measured.

5. **What the ten-component sum means.** The denominator of `§5.2`'s shares is
   the sum over an orthonormal basis of the external space — a basis-independent
   trace. **Whether that trace is the right normaliser for judging what the
   projection discards is a question this artifact does not answer**, and a
   different normaliser (the retained sum, the largest single component, a
   covariant invariant) would give different-looking shares from the same
   measurement. The raw coefficients of `§5.1` are given so any normaliser can
   be applied to them.

6. **Why `D1` and the retained components are opposite in sign.** The
   measurement records that they are. **No mechanism for it is offered**, and
   whether the near-cancellation between `D1` and a retained component is
   structural or coincidental at this parameter point is not determined here.

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
