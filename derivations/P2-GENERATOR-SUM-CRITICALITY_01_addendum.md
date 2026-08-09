# Addendum — `P2-GENERATOR-SUM-CRITICALITY-01`: calibration and ansatz scope

**Kind:** addendum. It corrects two consequences drawn in artifacts that
are already committed. It computes no new criticality result and revises
no earlier document.

**No committed artifact is altered.**
`results/P2-PHASE-01/generator-sum-criticality/criticality.json`,
`derivations/P2-GENERATOR-SUM-CRITICALITY_01.md` and
`reports/2026-08-08T2350Z_generator-sum-criticality.md` are preserved
exactly as reviewed. They record honestly what was concluded at the
time; rewriting them would destroy that record, which is why this
addendum exists instead.

Authority: `specs/2026-08-09T0059Z_integrate-generator-sum-criticality.md`.

---

## 1. The accepted result

The singlet-only control reproduces `P2-GAP-01`: with the "NJL"
normalisation `L_int = G_N(ψ̄ψ)²` the gap equation is `1 = 8·G_N·I_0`,
the channel coupling is `G = 4·G_N`, the combinatorial prefactor is
exactly `2`, and `G_c = 1/(2·I_0)`. The full `U(N)` generator-sum
canonical interaction instead gives `1 = (8/N)·G·I_0` and
`G_c = N/(8·I_0)`. The ratio of the coefficients in front is `N`, equal
to `1` only at `N = 1` — the correct degeneration, since the generator
sum collapses to the singlet interaction there. **`P2-GAP-01`'s `PASS`
stands for the form it computed**, and neither its gate entry nor its
derivation is touched.

## 2. The correction: the exploratory `G/G_c` positions do not move

The `verdict` field of `criticality.json` ends:

> The exploratory G/G_c positions carry an N/4 factor.

**They do not.** The argument is algebraic, and the numerics of §4 are a
regression check on it rather than its proof.

### 2.1 The cancellation

Both gap equations have the same form, differing only in the constant
`c` in front:

    1 = c · G · I_0(M̂)          c = 2    singlet-only control
                                c = 8/N  canonical generator sum

At a fixed `M̂` this is solved by `G(M̂) = 1/(c·I_0(M̂))`, and the
critical coupling is the same expression at `M̂ = 0`:

    G_c = 1/(c · I_0(0))

Therefore

    G/G_c = [1/(c·I_0(M̂))] / [1/(c·I_0(0))] = I_0(0)/I_0(M̂)

**`c` cancels identically.** The relation between the dimensionless
ratio `G/G_c` and `M̂` contains no reference to the prefactor at all,
and so is the same for the singlet-only control and for the generator
sum at every `N`.

Equivalently, and in the form the root finder actually solves: at a
given ratio `r = G/G_c` the coupling is `G = r/(c·I_0(0))`, so the gap
equation reads

    1 = c · [r/(c·I_0(0))] · I_0(M̂) = r · I_0(M̂)/I_0(0)

i.e. **`I_0(M̂) = I_0(0)/r`, in which `c` does not appear.** The
exploratory study scanned exactly this dimensionless ratio `r` and
solved for `M̂`, so its positions are untouched.

### 2.2 The condition under which this holds

**The invariance is not automatic and its condition must travel with
it.** It holds because the generator-sum derivation changes **only the
overall gap-equation prefactor** and leaves **the same regulated
`I_0(M̂)`**:

    1 = 2·G·I_0(M̂)      becomes      1 = (8/N)·G·I_0(M̂)

with `I_0` the identical function of `M̂` in both.

**It would NOT follow from a change that altered the `M̂`-dependence of
the gap equation.** A modification that changed the regulator, the
propagator denominator, the internal-index structure inside the loop, or
anything else that makes `I_0` a different function of `M̂` would break
the cancellation, because then the two `I_0(0)/I_0(M̂)` curves would not
be the same curve. **A reader must check that condition before reusing
this result for a different modification of the gap equation.**

## 3. What changes and what does not

    unchanged     the M-hat versus G/G_c curve
                  the M-hat = 1 crossing at G/G_c = 1.769
                  the 282-row branch-depth table, indexed by G/G_c
                  the drafted parameter domain, expressed in G/G_c

    changed       the value of G_c in terms of I_0 and N:
                    1/(2 I_0)  ->  N/(8 I_0)
                  the absolute coupling G at a given G/G_c: factor N/4

## 4. The numerical demonstration

**Reproduced independently for this addendum**, not copied. It uses
exactly the regulated `I_0(M̂)`, the cutoff and unit conventions, and the
root prescription of
`derivations/P2-PHASE-01_scalar_stationary_exploratory.md` and its
existing implementation `scripts/p2_phase01_scalar_exploratory.py`:
the product-midpoint Wilson quadrature `WilsonQuadrature`, the finest
grid `n = 48` at the unshifted `shift = 0.0`, and the bracketed
bisection on `[-4, 4]` with 17 halvings. **Only the prefactor `c` was
changed**, from the implementation's hardcoded `2` to the value under
test.

The three prefactors, labelled so they are not mistaken for arbitrary
models:

    c = 2      the original exploratory / control prefactor;
               numerically also the canonical prefactor at N = 4
    c = 8/3    canonical, N = 3
    c = 4      canonical, N = 2

With `I_0(0) = 0.0853597428025065` on that grid, the critical couplings
differ as expected —

    c = 2      G_c = 5.857562166709317
    c = 8/3    G_c = 4.3931716250319885
    c = 4      G_c = 2.9287810833546586

— and the roots at matched `G/G_c` do not:

    G/G_c        c = 2 (N=4)        c = 8/3 (N=3)        c = 4 (N=2)     max |diff|
     1.05     0.078094482422       0.078094482422       0.078094482422    0.000e+00
     1.2      0.290557861328       0.290557861328       0.290557861328    0.000e+00
     1.4      0.552886962891       0.552886962891       0.552886962891    0.000e+00
     1.769    0.999847412109       0.999847412109       0.999847412109    0.000e+00
     2.0      1.260833740234       1.260833740234       1.260833740234    0.000e+00
     3.0      2.270050048828       2.270050048828       2.270050048828    0.000e+00

**The `M̂` values are identical, not merely agreeing to some tolerance.**
The specification anticipated agreement to nine decimal places; the
observed spread is exactly zero at every ratio.

**One honest qualification.** The exploratory root prescription returns
the midpoint of a bracket halved 17 times from `[-4, 4]`, so its output
is quantised at `8/2¹⁷ ≈ 6.1e-05`. Identical returned values are
therefore consistent with, but do not by themselves establish, agreement
below that quantum. Re-running the same bisection to 60 halvings —
**beyond the prescription, as corroboration only** — gives a spread of
`0.000e+00` again, now at a quantum below `1e-17`:

    G/G_c              c = 2              c = 8/3                c = 4    max |diff|
     1.05    0.078115750640350    0.078115750640350    0.078115750640350   0.000e+00
     1.2     0.290533037587750    0.290533037587750    0.290533037587750   0.000e+00
     1.4     0.552876558110250    0.552876558110250    0.552876558110250   0.000e+00
     1.769   0.999834694922150    0.999834694922150    0.999834694922150   0.000e+00
     2.0     1.260858524623150    1.260858524623150    1.260858524623150   0.000e+00
     3.0     2.270064539994150    2.270064539994150    2.270064539994150   0.000e+00

The `M̂ = 1` crossing, located by bisecting on `r`:

    c = 2     (N = 4 / original)   M-hat = 1 at G/G_c = 1.769143
    c = 8/3   (N = 3)              M-hat = 1 at G/G_c = 1.769143
    c = 4     (N = 2)              M-hat = 1 at G/G_c = 1.769143

And the identity of §2.1 checked directly on the solved roots:

    r = 1.05    I_0(M̂)/I_0(0) = 0.952380952381    1/r = 0.952380952381
    r = 1.2     I_0(M̂)/I_0(0) = 0.833333333333    1/r = 0.833333333333
    r = 1.4     I_0(M̂)/I_0(0) = 0.714285714286    1/r = 0.714285714286
    r = 1.769   I_0(M̂)/I_0(0) = 0.565291124929    1/r = 0.565291124929
    r = 2.0     I_0(M̂)/I_0(0) = 0.500000000000    1/r = 0.500000000000
    r = 3.0     I_0(M̂)/I_0(0) = 0.333333333333    1/r = 0.333333333333

**Note that `M̂ = 1` at `G/G_c ≈ 1.769` comes from this specific
regulated integral**, not from the cancellation. The cancellation says
the three curves coincide; where on the common curve `M̂ = 1` falls is a
property of the Wilson `I_0`.

## 5. The fixed-`G` statement, which is correct and about something else

For a **fixed physical `G`**, the two dimensionless labels differ:

    (G/G_c)_canonical = (4/N) · (G/G_c)_old

**That is true**, and it follows immediately from `G_c` changing by
`N/4`. It does not conflict with §2: the two statements are about
different quantities. §2 says that *at a matched value of the ratio*,
`M̂` is the same; §5 says that *a fixed absolute coupling* corresponds to
different ratios under the two normalisations.

**The exploratory study never fixed a physical `G`.** It scanned the
dimensionless ratio `G/G_c` over `G_RATIOS` and solved the stationarity
condition for `M̂` at each. **The fixed-`G` conversion therefore does not
bear on the exploratory scan; the prefactor cancellation of §2 does.**

## 6. Ansatz scope: what was analysed, and what was not

The reviewed derivation note states, of an adjoint condensate
`⟨ψ̄_iψ_j⟩ ∝ (λ^B)_{ij}` with traceless `B`, that it "would break the
`U(N)` flavour symmetry the freeze imposes and is **not** fixed by the
frozen material", concluding "the singlet ansatz is the only condensate
the frozen material supports".

**The first half is right as a statement about the ansatz used. The
second does not follow.** A symmetric action admits symmetry-breaking
saddle points — that is what spontaneous symmetry breaking is — so
"would break the symmetry" is not "is not supported by the theory".

**The accurate statement:** under the `U(N)`-symmetric mean-field ansatz
this derivation adopted, only the singlet condensate is retained;
adjoint condensates belong to symmetry-breaking ansätze and **were not
analysed**. Whether the generator sum admits one remains an open
question that this work does not answer in either direction.

**Out of scope must not become non-existent.** No adjoint condensate is
analysed here either; doing so is a separate task.

## 7. What is left as committed

**The `verdict` field of `criticality.json` is left exactly as
committed**, including its final sentence. This addendum corrects the
consequence that sentence draws; it does not edit the artifact.

**The artifact's correction-factor fields are themselves accurate.** The
artifact carries two, and both name a correction to `G_c`:

    generator_sum_symbolic.exploratory_correction_factor_symbolic  = "N/4"
    per_N[*].exploratory_correction_factor_vs_half_I0              = 1/2, 3/4, 1
                                                                     (N = 2, 3, 4)

The critical coupling changes by `N/4` relative to the `1/(2·I_0)`
form — `N/(8·I_0) = (N/4)·(1/(2·I_0))` — and the per-`N` values are
exactly that factor, reaching `1` at `N = 4` where the canonical
prefactor `8/N` equals the original `2`. **Both names are right**: each
says "correction factor **vs half `I_0`**", i.e. a correction to the
critical coupling.

What does not follow from them is a correction to positions expressed in
`G/G_c`. **The field names describe a `G_c` correction; the verdict
sentence extended that factor to the scan, and it is the extension that
is withdrawn here** — not the factor, and not the names.

The derivation note and the execution report are likewise unaltered.

## 8. Scope of this addendum

It registers no gate and changes no status. `P2-PHASE-01` remains
`PROPOSED` and `P2-GAP-01` remains `PASS`. No exploratory result, no
branch-depth table row, and no line of the parameter-domain draft is
rescaled, restated or amended — **the point of this addendum is that
they need no change.**
