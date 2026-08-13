# `P2-PHASE-01` C3 — is the curvature asymmetry physical or coordinate-induced?

## Verdict

**COORDINATE-INDUCED.**

Operationally, and no wider than this: **definition-induced / algebraically
determined.** At any non-trivial stationary root the restricted curvature
reduces to a single term whose only asymmetry is an explicit prefactor `mhat`,
so the ratio of the two branches' curvatures is fixed once the two root
positions are — and those positions are themselves fixed by the
Wilson-complement identity. **This does not assert a pure
coordinate-transformation Jacobian artefact**, and it does not exclude the other
ordinary explanations; §5 says which are excluded and which are not.

## The derivation

**Anchoring disclosure, stated before the working so it cannot be read as a
claim of independence.** **The structural half was mine and is on the record;
the closed form was not.** My `C1` report and `C1` findings artifact, committed
at `92726596f29e12ec12e7f795bd68b902ac712d50` on 2026-08-13T02:02:05Z, state:
*"`reduced_curvature` at line 109 returns
`1.0 / (2.0 * coupling) - bubble - mhat * derivative`, whose third term is not
invariant under `m -> -8 - m` while the first two are, which bears directly on
`C3`'s question whether the curvature asymmetry is induced by the chosen
coordinate."* **That was written before this task's specification existed and
identifies the mechanism.** **But I read §2's closed form `-m2/m1`, its gap-
condition cancellation and its verification figures before writing the working
below.** **So: the mechanism was independently identified and on record; the
derivation as presented was completed after reading §2, and I do not claim it as
blind.**

### What the code defines

From `first_derivative`, line 101:

    return mhat * (1.0 / (2.0 * coupling) - quadrature.bubble(mhat))

so, writing `I0` for `bubble` and `G` for `coupling`,

    V'(m) = m * ( 1/(2G) - I0(m) )

From `reduced_curvature`, line 109, whose docstring at line 107 names it the
analytic derivative of that expression:

    return 1.0 / (2.0 * coupling) - bubble - mhat * derivative

    V''(m) = 1/(2G) - I0(m) - m * I0'(m)

**where `derivative` is the second element of `bubble_and_derivative` (line
108), formed at lines 84 and 85 as the analytic mass derivative of the same
quadrature sum.** **Three terms; the first two carry no `m` prefactor and the
third does.**

### Two terms vanish at a root

The non-trivial stationary condition is `V'(m) = 0` with `m != 0`, which forces

    1/(2G) = I0(m)

**so the first two terms of `V''` cancel identically at any non-trivial root**,
leaving

    V''(root) = - m * I0'(m)

**Everything about the asymmetry now sits in that one term.**

### The ratio is fixed by the positions

The frozen Wilson-complement identity gives `I0(-8-m) = I0(m)`. Differentiating
with respect to `m`:

    d/dm I0(-8-m) = -I0'(-8-m)   and   d/dm I0(m) = I0'(m)
    =>  I0'(-8-m) = -I0'(m)

**so `I0` is even about `m = -4` and `I0'` is odd about it.** With
`m2 = -8 - m1`:

    V''(m2)     - m2 * I0'(m2)     - (-8-m1) * (-I0'(m1))          m2
    -------  =  ---------------  = ------------------------  =  - ----
    V''(m1)     - m1 * I0'(m1)         - m1 * I0'(m1)              m1

**The unknown `I0'(m1)` cancels.** **The ratio depends on nothing but the two
root positions, and `m2` is not free: it is `-8 - m1`.**

So the ratio may be written in terms of `m1` alone:

    V''(m2) / V''(m1)  =  (8 + m1) / m1

**which diverges as `m1 -> 0` and tends to 1 as `m1 -> -4`.** **The large
ratios near criticality in the adopted artifact's §5b table are this divergence,
not a physical effect** — at `G/Gc = 0.99`, `m1` is of order `1e-2` and
`8/m1` is of order `5e2`, which is the observed `-477.9`.

## The check, over all ninety pairs

**Using only values stored in
`results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json` —
`mhat`, `reduced_curvature`, `divided_gap_factor` and `G`. Nothing was
evaluated from the model.**

    pairs checked                                            90
    worst relative deviation of V''(m2)/V''(m1) from -m2/m1   1.7811e-03
    where                                    G/Gc = 0.99, n = 48, shift 0.25
    median relative deviation                                4.925e-05

**Deviations grow monotonically as `|m1|` falls**, max over the six grids per
coupling:

    G/Gc   0.80  5.216e-05      |m1| ~ 0.409
    G/Gc   0.90  1.548e-04      |m1| ~ 0.185
    G/Gc   0.98  8.423e-04      |m1| ~ 0.034
    G/Gc   0.99  1.781e-03      |m1| ~ 0.017
    G/Gc   1.01  1.555e-03      |m1| ~ 0.016
    G/Gc   1.20  9.106e-05      |m1| ~ 0.290
    G/Gc   3.00  1.047e-05      |m1| ~ 2.269

### The deviation is accounted for exactly, not merely bounded

**The leftover is a stored quantity, so the sources separate without any new
evaluation.** Because `divided_gap(m) = 1 - 2*G*I0(m)` (line 135), the first two
terms of `V''` are exactly

    1/(2G) - I0(m)  =  divided_gap_factor(m) / (2G)

**and `divided_gap_factor` is stored in every root record** (line 183).
**The stored roots are not exact roots** — their `stationarity_residual` values
are non-zero, up to `1.875e-05` — so that bracket does not vanish, and the
prediction `-m2/m1` omits it.

Subtracting the stored leftover from each stored curvature and re-forming the
ratio:

    quantity compared                       max over 90 pairs      median
    raw   V''(m2)/V''(m1)  vs  -m2/m1            1.7811e-03      4.925e-05
    with divided_gap_factor/(2G) removed         1.1951e-14      6.664e-16

**The worst case improves by about eleven orders of magnitude, and every one of
the ninety pairs agrees to within `1.2e-14` relative — double-precision
round-off.** Per coupling, the corrected maximum never exceeds `1.2e-14`, and it
no longer varies systematically with `|m1|`.

**So the entire deviation is the first-two-terms leftover of roots resolved to
the bisection step, and nothing remains beyond floating-point round-off.**
**This is an attribution, not a consistency statement**: the omitted term was
computed from stored fields and removing it closes the gap. **The specification
required a decomposition before the deviation could be attributed rather than
called consistent; the decomposition is above, and it is exact.**

**The same check simultaneously measures the differentiated identity.** After
the subtraction the compared quantities are `-m2*I0'(m2)` and `-m1*I0'(m1)` as
the script computed them, so agreement with `-m2/m1` to `1.2e-14` also
establishes `I0'(-8-m) = -I0'(m)` on all six finite grids to that precision.
**That was assumed by the derivation and is here confirmed from the stored
data.**

## The consequence

**Consequence:** **the curvature asymmetry carries no independent
physical content.** Combined with `C1`, **the negative-mass branch then
has no independent content of any kind that has been demonstrated** —
its stored position is fixed by the Wilson-complement identity, and its
curvature ratio is fixed by that position and a prefactor.

**Bit-exactness is deliberately absent from this consequence.** The
mechanism behind the mirroring is unresolved under `OPEN-CC-3`, and
**`C3` does not rest on it**; a consequence that cited it would tie this
verdict to an open question it does not need. **This is a finding about what the
existing evidence supports, NOT a demonstration that the branch is
unphysical.** **It is material to the PI ruling that admitted the branch
as a candidate, because the ruling's stated basis was that the branch
was the computable thing available.** **Report it; do not act on it.**

## Which of the four ordinary explanations are excluded, and which are not

The adopted artifact requires four to be excluded before any physical reading.
**Two are settled by this derivation. Two are not, and "all four" is not
available on this evidence.**

**EXCLUDED — "whether the parameterisation in `Mhat` makes the second
derivative non-invariant under `m -> -8-m` by construction."** **It does.** The
prefactor `m` in the third term of `V''` is not invariant while the first two
terms are, and at a root only that term survives. **This is not a residual
possibility; it is the demonstrated mechanism.**

**EXCLUDED — "whether the potential is symmetric while the derivative with
respect to the chosen coordinate picks up sign or coordinate effects."** **It
does.** `I0` is even about `m = -4` and `I0'` is odd about it, so
differentiating in `m` introduces exactly the sign flip that, combined with the
`m` prefactor, produces the ratio `-m2/m1`.

**NOT EXCLUDED — "whether the curvature definition is genuinely covariant at
the two stationary points."** **Untested.** This derivation works entirely
inside the one parameterisation the script uses. **It shows the asymmetry is
fixed within that parameterisation; it does not show what a covariant
second-derivative definition would give**, and nothing here computes one.

**NOT EXCLUDED — "whether the second derivative carries a Wilson mass-dependent
Jacobian or measure contribution that differs between them."** **Untested.**
`reduced_curvature` at line 109 carries no Jacobian or measure factor, so the
question is not whether the implemented quantity has one — it does not — but
whether a fuller formulation should. **That is outside this reading.**

## What this does not establish

- **It does not establish that the negative-mass branch is unphysical or
  absent.** **The absence of demonstrated independent evidence and evidence of
  absence are different things, and only the first is produced here.**
- **It rests on one restricted one-dimensional curvature under a uniform scalar
  ansatz at `mu = 0`.** **The full condensate-space Hessian has never been
  computed**, and nothing here bears on what it would show. The results file's
  own `limitations` field records the same three boundaries.
- **It does not establish covariance of the restricted curvature under a general
  field reparameterisation**, nor exclude measure or Jacobian contributions in a
  fuller formulation — see §5.
- **It does not rest on, and does not settle, the mechanism of the bit-exact
  mirroring**, which is open under `OPEN-CC-3`. The derivation uses only the
  positional relation `m2 = -8 - m1` between the stored roots and the Wilson
  identity, both established.
- **It is a static reading plus arithmetic on stored values.** No script was
  run, no model quantity was evaluated at a new point, and no new numerical
  result was produced.
- **It settles nothing about `C2`.**
