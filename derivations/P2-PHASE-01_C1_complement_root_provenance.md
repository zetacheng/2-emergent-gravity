# `P2-PHASE-01` C1 — is the complement root recovered or constructed?

## The question

`derivations/P2-PHASE-01_microscopic_parameter_domain.md` records that the
stored complement-root position satisfies `Mhat_comp = -8 - Mhat_ord` exactly,
and defers to `C1` whether that is an independently recovered root or a
constructed companion. Across all six grids and all sixteen couplings, ninety
pairs of non-trivial roots satisfy `|Mhat_ord + Mhat_comp + 8| = 0.00e+00` —
exactly zero, ninety times — and a residual of exactly zero is a property of a
method rather than of physics. This artifact answers the question by reading
the generating script and inspecting the stored values. **It runs nothing and
computes no new numerical result.**

Script read, pinned and verified byte for byte before reading:

    scripts/p2_phase01_scalar_exploratory.py
    sha256  3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0
    blob    b44bc63d115f4e88a706d046e60488c51d8a06a0
    462 lines

That digest is also the `script_sha256` field of
`results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json` at
`1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`. **The study's outputs are
attributable to this script.**

## (a) ROOT PROVENANCE

**RECOVERED.**

Both non-trivial roots of the production table are located by separate
bracketed bisection searches that do not use the complement relation, and no
discrete mass-search grid forces their positions.

## (b) EXACTNESS PROVENANCE

**SEARCH-STRUCTURE-INDUCED.**

The exact zero is forced by the search structure: the two production brackets
are mirror images of one another under `m -> -8 - m`, every bisection node lies
on an exactly representable dyadic lattice, and the bisection's branch decisions
mirror exactly. **The stored `0.00e+00` is not numerical agreement between two
independent determinations of a position.**

## (c) `symmetry_check()`'s `complement_pairs` is CONSTRUCTED FOR CHECKING

`symmetry_check()` does construct `complement = -8.0 - mhat` and compares two
`bubble()` evaluations at those two masses. **That construction is a diagnostic
of the Wilson-complement relation and is NOT the mechanism that populates the
production root table.** A later reader who meets `complement = -8.0 - mhat` at
line 315 must not conclude that the root table was built the same way: it was
not, and (d) gives the lines that establish it.

## (d) The evidence

### The production path constructs no complement

`bisect_root`, line 138, obtains its root only by repeated evaluation of
`divided_gap`:

    142  f_left = divided_gap(left, coupling, quadrature)
    143  f_right = divided_gap(right, coupling, quadrature)
    152  for _ in range(17):
    153      middle = 0.5 * (left + right)
    154      f_middle = divided_gap(middle, coupling, quadrature)
    155      if f_left * f_middle <= 0.0:
    156          right, f_right = middle, f_middle
    157      else:
    158          left, f_left = middle, f_middle
    159  return 0.5 * (left + right)

`algebraic_roots`, line 162, calls it separately on the two brackets:

    164  roots = [0.0]
    165  for left, right in ((-12.0, -4.0), (-4.0, 4.0)):
    166      root = bisect_root(left, right, coupling, quadrature)
    167      if all(abs(root - known) > 2.0e-4 for known in roots):
    168          roots.append(root)
    169  return sorted(roots)

`grid_result`, line 190, stores each returned root without touching the pair:

    197  roots = [
    198      root_record(root, coupling, quadrature)
    199      for root in algebraic_roots(coupling, quadrature)
    200  ]

and `root_record`, line 172, records the value it is given
(`"mhat": mhat`, line 181). `build_results`, line 387, passes the grid list
straight through as `"grid_results": grids`.

**The decisive check is exhaustive rather than local.** Every occurrence of the
literal `-8` and of the word `complement` in all 462 lines:

    163  a docstring, "Wilson-complement sectors"
    297  complement_pairs = []                  } inside
    311  second = quadrature.bubble(-8.0 - mhat) } symmetry_check
    312  complement_pairs.append(                } (line 294)
    315  "complement": -8.0 - mhat,              }
    325  "wilson_complement_relation": (         }
    326  a string literal quoting the relation   }
    329  "complement_pairs": complement_pairs,   }

**`-8.0 -` occurs at exactly two lines, 311 and 315, and both are inside
`symmetry_check`.** No production root anywhere in the script is computed from
another root.

### Why the residual is exactly zero

**The two brackets are exact reflections of one another.** With
`phi(m) = -8 - m`: `phi(-12.0) = 4.0` and `phi(-4.0) = -4.0`, so `phi` maps
bracket A `(-12.0, -4.0)` onto bracket B `(-4.0, 4.0)` **with the endpoints
exchanged** — it reverses orientation.

**Every node of both searches is exactly representable.** Each bracket has
width `8 = 2**3`, both endpoints are exact, and 17 halvings place every node on
the lattice of integer multiples of `2**3 / 2**17 = 2**-14`; the returned value
`0.5 * (left + right)` is a multiple of `2**-15`. All of these are dyadic
rationals of magnitude below 16, so every midpoint, every `-8 - x`, and every
sum below is computed **without rounding**.

**The midpoint recursion commutes with the reflection, exactly.** Write bracket
A as `[a, b]` and bracket B as `[c, d]`, and suppose `c = -8 - b` and
`d = -8 - a`. Then

    middle_B = 0.5*(c + d) = 0.5*((-8-b) + (-8-a)) = -8 - 0.5*(a+b) = phi(middle_A)

**The branch decisions mirror, and the left/right exchange is what makes them
mirror rather than what breaks them.** In bracket A the test at line 155 is
`f(a) * f(middle) <= 0`; in bracket B it is `f(c) * f(middle) <= 0` with
`c = phi(b)`, so B tests the sign of `f` at the reflection of A's **right**
endpoint. Because `f(a) * f(b) < 0` in a proper bracket, the two tests are
complementary: exactly one of them takes the `<= 0` branch. And that is
precisely what preserving the reflection requires — reflection reverses
orientation, so *A keeps its left half* must correspond to *B keeps its right
half*. Checking both cases:

    f(a)*f(m) < 0   ->  A: right = m, left  unchanged
                        B: f(b)*f(m) > 0, else-branch, left = m, right unchanged
                        new c = phi(new b) = phi(m) = middle_B     OK
                        new d = phi(new a) = phi(a) = d            OK

    f(a)*f(m) > 0   ->  A: left = m, right unchanged
                        B: f(b)*f(m) < 0, if-branch, right = m, left unchanged
                        new c = phi(new b) = phi(b) = c            OK
                        new d = phi(new a) = phi(m) = middle_B     OK

The invariant therefore survives all 17 iterations, and the returned values
satisfy `root_B = phi(root_A) = -8 - root_A` exactly. The early returns at lines
144–147 preserve it too: if `f(-4.0) == 0.0` both searches return `-4.0`, and if
`f(-12.0) == 0.0` then A returns `-12.0` while B's `f_right` is `f(4.0)`, its
reflection. The single case that would break the invariant is
`f_middle == 0.0` exactly, in which both tests take the `<= 0` branch; that does
not occur in the stored data, whose smallest `stationarity_residual` is nonzero.

**The mechanism needs only sign agreement under reflection, not bit-equality of
the integrand — and the stored data show the integrand is NOT bit-symmetric.**
`symmetry.complement_pairs` reports, as measured by the study itself,

    mhat = -1.3  complement -6.7  absolute_difference 1.1102230246251565e-16
    mhat = -0.4  complement -7.6  absolute_difference 1.3877787807814457e-17
    mhat =  0.7  complement -8.7  absolute_difference 2.0816681711721685e-17
    mhat =  1.8  complement -9.8  absolute_difference 1.3877787807814457e-17

**`I0(m)` and `I0(-8-m)` differ at the 1e-16 level; they are not the same
double.** The asymmetry induced in `divided_gap = 1 - 2*G*I0` is therefore of
order `2*G*1e-16`, a few times `1e-15`, while the stored
`stationarity_residual` values show `|divided_gap|` at the returned roots to be
of order `1e-5` (the maximum over the whole study is `1.875e-05`). **The margin
between the two is about ten orders of magnitude, so no branch decision in any
of the 17 iterations can flip.** The exactness is carried by the lattice and the
mirrored decisions, not by the function values.

**The stored values confirm the lattice, and this is inspection of numbers
already in the results file.** Expressing each stored root exactly:

    non-trivial roots inspected                                   186
    roots that are NOT an integer multiple of 2**-15                0
    pairs of non-trivial roots                                     90
    pairs whose stored doubles sum to exactly -8.0                 90

Worked example, `G/Gc = 1.20`, `n = 48`, `shift 0.0`:

    -8.290557861328125  = -271665 x 2**-15   hex -0x1.094c400000000p+3
     0.290557861328125  =    9521 x 2**-15   hex  0x1.2988000000000p-2
    -271665 + 9521 = -262144 = -8 x 32768

and the six single-root points at `G/Gc = 1.00` are
`-7.999969482421875 = -262143 x 2**-15`, one lattice step from `-8.0`, with the
bracket-B partner at `+2**-15` discarded by the `2.0e-4` de-duplication test at
line 167 as a repeat of the trivial root. **Every stored non-trivial root sits
on the dyadic lattice that bisection over a width-8 bracket produces, and every
pair mirrors on it exactly.**

### Are the two `symmetry` fields computed from the relation or measured against it?

**`wilson_complement_relation` is a string literal** — lines 325–328 — asserting
`I0(Mhat) = I0(-8 - Mhat)` and stating that it is "numerically checked below".
**It is a claim, not a measurement.**

**`complement_pairs` is both, and the distinction matters.** The complement
*mass* is computed **from** the relation (`-8.0 - mhat`, line 311), while the
quantity reported, `absolute_difference`, is **measured against** it by two
independent `bubble()` evaluations. **So the abscissa is constructed and the
test is genuine.** Its measured values are the 1e-16 figures above, which is why
this field is evidence *against* the exactness of the root mirroring being a
property of the integrand.

**It is checked on one grid only:** `symmetry_check` builds
`WilsonQuadrature(n=finest_n, shift=0.0)` at line 295, so the relation is tested
at `shift 0.0` and never at `shift 0.25`. **The exactness conclusion above does
not depend on that, because it does not depend on the integrand's symmetry
holding to any particular precision.**

## (e) The consequences, transcribed from the specification

### For ROOT PROVENANCE = `RECOVERED`

**Consequence:** the complement root is **independently recovered
numerically, rather than constructed** from the ordinary root. This
discharges the adopted artifact's caution about numerical provenance.
**It does NOT make the complement position algebraically independent:**
under the exact Wilson-complement identity, its position remains
determined by `Mhat_comp = -8 - Mhat_ord`. The independent recovery
therefore **validates the solver and the realised symmetry, but does not
by itself add independent positional physics.** The branch's potentially
distinctive content remains in quantities not fixed by that positional
identity, including the curvature asymmetry, whose interpretation remains
deferred to `C3`.

### For EXACTNESS PROVENANCE = `SEARCH-STRUCTURE-INDUCED`

**Consequence:** the roots are independent as searches but **the
exactness is not evidence of anything.** `max |sum + 8| = 0.00e+00`
must not be quoted as numerical agreement, because a reflected search of
a function with an exact reflection symmetry cannot produce anything
else.

**One observation about the second consequence, kept separate from it because
the text above is transcribed and not amended.** Its closing clause reasons from
"a function with an exact reflection symmetry". **Measured, the symmetry is not
exact** — the `complement_pairs` differences are `1e-16` to `1e-17`, not zero.
**The operative claim is unaffected and is in fact stronger than its stated
rationale:** the exactness survives an integrand that is only approximately
symmetric, which shows the search structure rather than the symmetry is what
produces it.

## (f) What this does not establish

**This task establishes something about the script, not about the physics, and
it adds no evidence — it changes the weight of evidence that already exists.**

- **It does not show the complement branch is physical or unphysical.** A
  `RECOVERED` root table says the solver found both roots; it says nothing about
  whether the branch is an admissible stable phase. The full condensate-space
  Hessian and the gate's admissibility assessment remain absent, and
  `OPEN-AC-3` still blocks the common-normalised depth comparison.
- **It does not make the complement position independent evidence.** Under the
  exact Wilson-complement identity the position is algebraically determined by
  the ordinary root, whatever the solver did, and the exactness of the stored
  mirroring is a property of the bracket geometry.
- **It does not establish that the ninety zero residuals were ever presented as
  agreement.** The adopted artifact already cautioned that a residual of exactly
  zero is a property of a method; **this task supplies the method.**
- **It settles nothing about the curvature asymmetry**, which is `C3`.
- **It settles nothing about the sign of `I0` or about negative `G`**, which is
  `C2`.
- **It is a static reading.** No variant of the solver was run, no asymmetric
  mass grid was tried, and nothing here rests on a computation performed by this
  task.

## (g) Whether the reading bore on `C2` or `C3`

**`C2`:** the reading exposes the form of the integrand summed by
`WilsonQuadrature.bubble` — `1.0 / denominator` with
`denominator = s + w * w` at lines 82–83, where `s` is a sum of `sin**2` terms —
and that form bears directly on `C2`'s question about the sign of `I0`; **no
conclusion is drawn here.**

**`C3`:** `reduced_curvature` at line 109 returns
`1.0 / (2.0 * coupling) - bubble - mhat * derivative`, whose third term is not
invariant under `m -> -8 - m` while the first two are, which bears directly on
`C3`'s question whether the curvature asymmetry is induced by the chosen
coordinate; **no conclusion is drawn here.**
