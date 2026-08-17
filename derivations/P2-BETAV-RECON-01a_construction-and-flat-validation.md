# `P2-BETAV-RECON-01a` — clean-room Proca operators and their flat-limit validation

**Kind:** clean-room construction plus validation. **It builds and validates. It
does not assemble a determinant combination, does not vary any determinant
power, and does not compare any quantity to an external target.**

**Evidence base:** `f21198cd25ae285b789b706f7c4ac0730f9fff69`.

**Written at commit `3b`, AFTER reading `P2-BETAV-CIRC-01`'s quantitative
transverse/longitudinal result. The three code files were frozen at commit `3a`
and are byte-identical here.** `§7` records the object ids.

## 0. What was built

Three files, `scripts/recon2026/proca_curved.py`,
`scripts/recon2026/flat_validation.py` and
`tests/test_recon2026_flat_limit.py`, on a periodic `L^4` Euclidean lattice with
spacing `a = 1`.

    D1[g,h]   metric-coupled 1-form operator, from the covariant field-strength
              action with exact geometric factors
    D0[g,h]   metric-coupled compensating scalar, from the covariant Dirichlet
              action

**Both from actions, not from kernels written down directly.** The operator is
the action's Hessian divided by the mass metric, so the mass term is exactly
`m²` times the identity. `§2` lists every convention that choice implies.

**Only `numpy` is used.** `scipy` is absent from this environment and is not one
of the four declared packages, though `pyproject.toml:11` lists it as a project
dependency — `§9.4`.

## 1. The two actions, and the discretisation

    S0[phi] = 1/2 sum_x sqrt(g) g^{mu nu} (d_mu phi)(d_nu phi)
                + m^2/2 sum_x sqrt(g) phi^2

    S1[A]   = 1/4 sum_x sqrt(g) g^{mu al} g^{nu be} F_{mu nu} F_{al be}
                + m^2/2 sum_x sqrt(g) g^{mu nu} A_mu A_nu

    F_{mu nu}(x) = (d_mu A_nu)(x) - (d_nu A_mu)(x)
    (d_mu f)(x)  = f(x + mu) - f(x)

**The operators are then**

    D0 + m^2 = G0^{-1} K0 + m^2 * 1      G0 = diag(sqrt(g))
    D1 + m^2 = G1^{-1} K1 + m^2 * 1      G1[(x,mu),(x,nu)] = sqrt(g) g^{mu nu}

with `K0`, `K1` the Hessians of the two actions.

## 2. Every convention fixed HERE, as a choice and not as a repository fact

**`CONVENTIONS.md` supplies two things this construction uses: `:12` Euclidean
`d = 4`, and `:24` the hypercubic lattice with `a == 1`, the Brillouin zone
`p_mu in (-pi, pi]`, and the naive/scalar momentum
`phat2 = sum_mu 4 sin^2(p_mu/2)`. IT DOES NOT FIX A LATTICE REALISATION OF
EITHER OPERATOR.** Six choices were made here. **A later reader tracing a wrong
result should start with this list.**

    C1  FORWARD DIFFERENCES for every lattice derivative,
        (d_mu f)(x) = f(x + mu) - f(x).
        Consequence: the free scalar kernel equals CONVENTIONS.md:24's phat2
        exactly, since |exp(i p_mu) - 1|^2 = 4 sin^2(p_mu / 2); and the flat
        1-form kernel's non-dispersing band is exactly momentum-independent,
        because forward differences commute.  A symmetric or improved
        difference would change both statements.

    C2  SITE-CENTRED geometric factors.  sqrt(g) g^{mu nu} and
        sqrt(g) g^{mu al} g^{nu be} are evaluated at the site at which the
        difference is anchored, not at a link or plaquette midpoint.

    C3  PERIODIC boundary conditions in all four directions.

    C4  g^{mu nu} is the EXACT MATRIX INVERSE of g_{mu nu}, not a truncated
        weak-field expansion, and sqrt(g) = sqrt(det g).  The construction is
        therefore not perturbative in h even though h is used weakly.

    C5  THE OPERATOR IS THE HESSIAN DIVIDED BY THE MASS METRIC, so the mass
        term is exactly m^2 * 1.  This is a choice about what "the operator"
        means; a different split moves factors of G between the operator and
        the measure.  IT TURNED OUT TO BE THE MOST CONSEQUENTIAL CHOICE OF THE
        SIX -- see §4.

    C6  The weak-field background is a single cosine,
        h_{mu nu}(x) = amp * c_{mu nu} * cos(2 pi (q . x) / L),
        with c symmetric and q an integer wavevector.  Nothing in the
        repository fixes a background profile.  The pattern and wavevector used
        throughout are the module constants of flat_validation.py.

**Free parameters and the values used:** extent `L in {4, 6}`; mass
`m^2 in {0.25, 1.0}` for the spectral validations and `m^2 = 0.5` for the
derivative validations; background amplitude `amp in {0, 0.02, 0.04, 0.08}`;
background wavevector `q = (1,0,0,0)`; the symmetric pattern `c` given in
`flat_validation.py`.

**Boundary conditions are C3 for both operators. There are no other free
parameters.**

## 3. The flat-limit target, and where it was not precise

**`P2-BETAV-CIRC-01_determinant-decomposition.md:17-18`, quoted:**

> Flat kernel `M_{μν}(k) = (ŝ²+m²)δ_{μν} − a_μ a_ν*`. Spectrum (verified):
> `{ŝ²+m² (×3 transverse), m² (×1 longitudinal)}`, `det M(k)=m²(ŝ²+m²)³`.

**IS IT PRECISE ENOUGH TO TEST AGAINST? ALMOST, AND I HAD TO MAKE ONE THING
PRECISE.**

**Precise as stated:** the multiplicities (three and one), the identification of
which band disperses and which does not, and the determinant
`m²(ŝ²+m²)³` — which is an independent third statement, not implied by the
first two, and which `§4` uses as a global check.

**NOT PRECISE: what `ŝ²` is.** The symbol is not defined in those lines, and
`CONVENTIONS.md:24` defines TWO distinct free-field momenta —
`phat2 = sum_mu 4 sin^2(p_mu/2)` for the naive/scalar case, and
`sbar_mu = sin p_mu` — either of which could be squared and summed to give
something called `ŝ²`. **They are different functions.**

**I made it precise by construction rather than by choosing:** C1's forward
difference gives `|exp(i p_mu) - 1|^2 = 4 sin^2(p_mu/2)`, so this construction's
dispersing band is `sum_mu 4 sin^2(p_mu/2) + m^2` — `CONVENTIONS.md:24`'s
`phat2`, not `sum_mu sin^2 p_mu`. **That is a consequence of C1, and a
construction using symmetric differences would have produced the other
function and disagreed with the same quoted line.** **Recorded as a resolution
of an ambiguity, not as a repository fact.**

**One further thing the quoted line does not say, which the construction
forced:** at `p = 0` the symbol vanishes, so all four bands sit at `m²` and the
multiplicity of `m²` over the whole lattice is `nsite + 3`, not `nsite`. **A
test asserting `nsite` would fail on a correct construction.**

**And a second statement, from `:66`, `:68` and `:157-158`:** the external
scalar is `Δ₀ = ŝ²+m²` (propagating) while the Proca longitudinal spectral
factor is `m²` (ultralocal), and `DECOMP-UNAVAILABLE-AS-RECOVERED` turns on
exactly that distinction. **`§5` reports which of the two `D0` is.**

## 4. Validation (a) — the flat 1-form spectrum

**MEASURED at `h = 0`. The operator is exactly symmetric there, which was
measured and not assumed: relative asymmetry `0.0` at every extent and mass
tested.**

    L = 4, m^2 = 0.25
      max |numeric - required| over the whole spectrum   7.46e-14
      multiplicity of the non-dispersing band            259  (required 259)
      log det, full position-space operator              1206.5450159411748
      log det, sum over analytic momentum blocks         1206.5450159411760
      absolute difference                                1.14e-12

**The determinant cross-check is the strongest single statement here.** The
position-space operator is a `1024 x 1024` matrix built by accumulating
per-site contributions; the momentum-space blocks are `4 x 4` and analytic.
**They agree to 1.1e-12, which they can only do if the position-space
construction factorises the way the momentum kernel says it must.** It tests
the geometric-factor bookkeeping in a way no eigenvalue comparison does.

**Sampled momentum blocks, showing the structure directly:**

    coord            phat2      eigenvalues of the 4x4 block
    (0,0,0,0)      0.000000     [0.25, 0.25, 0.25, 0.25]
    (1,0,0,0)      2.000000     [0.25, 2.25, 2.25, 2.25]
    (0,2,0,0)      4.000000     [0.25, 4.25, 4.25, 4.25]
    (1,2,0,0)      6.000000     [0.25, 6.25, 6.25, 6.25]
    (2,2,0,0)      8.000000     [0.25, 8.25, 8.25, 8.25]

**One band pinned at `m² = 0.25` regardless of momentum; three at
`phat2 + m²`. The `(0,0,0,0)` row is the degeneracy `§3` warned about.**

## 5. Validation (c) — the compensating scalar is PROPAGATING

    L = 4, m^2 = 0.25
      max |numeric - (phat2 + m^2)|      2.84e-14
      minimum eigenvalue                0.24999999999999395
      maximum eigenvalue                16.250000000000018
      eigenvalue spread                 16.000000000000025
      distinct eigenvalues              9
      is_ultralocal                     False

**`D0 + m²` DISPERSES.** Its spread is `16` at `L = 4`, it takes nine distinct
values, and its minimum equals `m²` only because `phat2(0) = 0`. **It is
`Δ + m²`, not the ultralocal `m²`.**

**This is the distinction `CIRC-01:157-158` says
`DECOMP-UNAVAILABLE-AS-RECOVERED` turned on, and it is a CORRECTNESS condition
here, not a fitting condition:** the compensating scalar of the gate's `Scope`
is a propagating scalar determinant, and an implementation that supplied the
Proca longitudinal eigenfactor instead would be unusable for the same reason
the recovered one was.

## 6. Validation (b) — transverse/longitudinal separation

**MY NUMBERS FIRST, MEASURED BEFORE `CIRC-01`'s FIGURE WAS READ, then
`CIRC-01`'s. The order is the evidence.**

### 6.1 My numbers, pre-freeze

**Two forms were measured, because they do not agree, and the disagreement is
the finding.** The projectors are the FLAT ones; the background is curved. The
reported quantity is `||Pi_T X Pi_L||_F / ||X||_F`.

    L = 4, m^2 = 0.25                     THE OPERATOR      THE HESSIAN
                                          D1 + m^2 (C5)     K1 + m^2 G1
    amplitude 0.00                          3.0721e-16        3.0721e-16
    amplitude 0.02                          3.2752e-16        1.7467e-04
    amplitude 0.04                          3.2335e-16        3.4933e-04
    amplitude 0.08                          3.2533e-16        6.9864e-04
    leading power in the amplitude            -0.0048            0.99996

**The operator as constructed has NO transverse/longitudinal mixing AT ALL — at
machine level, at every amplitude, with no amplitude dependence. The Hessian of
the same action before dividing by the mass metric mixes at O(amplitude).**

### 6.2 Why, structurally

**`||K1 · Pi_L||` is `7.6e-14` at every amplitude tested, on curved backgrounds
as well as flat.** The reason is exact and metric-free: `F_{mu nu}` vanishes
identically on `A_mu = d_mu lambda` because the forward differences commute
(C1), and the flat longitudinal direction at momentum `p` is exactly that
pure-gauge direction. **So the flat longitudinal subspace is the exact gauge
kernel of `K1` for ANY metric.**

**The mass term is the only part that could mix, and C5 divides it away.**
`(D1 + m²) Pi_L = G1^{-1} K1 Pi_L + m² Pi_L = m² Pi_L`, so
`Pi_T (D1+m²) Pi_L = 0` identically. **On the curved background the
non-dispersing band is still exactly `m²` with multiplicity 259.**

**THIS MEANS C5 IS NOT A BOOKKEEPING PREFERENCE. It moves the entire
transverse/longitudinal mixing out of the operator and into the measure factor
`det G1`.** The mixing has not been removed from the physics; it has been
relocated to a place this stage does not examine. **`RECON-01b` inherits that
relocation and must decide whether the determinant it needs is of `D1 + m²` or
of `K1 + m² G1`, because the two differ by `det G1` and only the second mixes.**

### 6.3 `CIRC-01`'s figure, read after the freeze

**`P2-BETAV-CIRC-01_determinant-decomposition.md:37-47`** reports, at `m = 0.3`,
`n in {10,12}`, over three `q`-ranges, a sector decomposition of the induced
bubble in which the **mixed `TL+LT` `q²` coefficient is `≈ +9.0e-5`, about
`0.4%` of the total, with scaling exponent `≈ 1.98`**, stable across grids
(`8.7e-5` to `9.1e-5`). Its finding is that an exactly invariant additive split
fails, but only at that level.

### 6.4 The relation between the two, and it is NOT a numerical comparison

**MY NUMBERS AND `CIRC-01`'s MEASURE DIFFERENT OBJECTS AT DIFFERENT ORDERS, AND
REPORTING `3e-16 vs 9e-5` AS AGREEMENT OR DISAGREEMENT WOULD BE A CATEGORY
ERROR.**

    mine        the off-diagonal block of the OPERATOR, at a single momentum,
                in the flat T/L basis -- a one-graviton vertex-level quantity
    CIRC-01's   the mixed q^2 coefficient of the induced BUBBLE, with
                projectors built INDEPENDENTLY at k and k+q -- a two-momentum,
                second-order-in-vertex quantity

**`CIRC-01` says so itself, and says the single-momentum measurement is the
wrong test.** Its `:26-29` opens *"The relevant test is **not** whether the
one-graviton vertex off-block norm vanishes as `q→0`"*, and its `:50-52` records
that the vertex mixing does vanish as `q→0` and that *"the earlier vertex-norm
figure was measured in the wrong, single-momentum basis and is withdrawn."*

**`§6.1` is a single-momentum measurement. It is in the class `CIRC-01`
withdrew.** That is not a defect in this construction — the criterion asked for
the separation to be built and measured, and it was — **but it means the
comparison `§4(b)` requires is a statement about commensurability, not a
number.**

**The one genuine consistency point.** `CIRC-01` states the one-graviton vertex
mixing vanishes as `q→0`. **My operator-level mixing is exactly zero at every
`q` and every amplitude, which is consistent with that and stronger than it.**

**And one genuine non-correspondence, measured post-freeze with the frozen
construction unchanged.** Varying the background wavevector at `L = 6`,
`m² = 0.09` (matching `CIRC-01`'s stated mass), amplitude `0.04`:

    q = (3,0,0,0)   qhat2 4.00000   operator 6.1384e-16   Hessian 1.8114e-04
    q = (2,0,0,0)   qhat2 3.00000   operator 6.1446e-16   Hessian 1.2829e-04
    q = (1,0,0,0)   qhat2 1.00000   operator 6.1567e-16   Hessian 1.2845e-04

**The Hessian form's mixing does NOT go to zero as `qhat2` falls.** It is
dominated by the mass-metric block, which is `O(h)` and carries no factor of the
background momentum. **So neither of my two forms reproduces `CIRC-01`'s
`q→0`-vanishing vertex: one is identically zero and the other is
momentum-insensitive.** **That is a finding about what a single-momentum
operator-level measure can and cannot see, and it is reported rather than
tuned away — the construction was frozen at `3a` and tuning was not available.**

**What a commensurable measurement would need:** a bubble at two momenta with
projectors built independently at `k` and `k+q`, which is a determinant-level
object. **`§5` of the specification forbids assembling one here, and this
artifact does not.**

## 7. Validation (d) — extents and masses

    L   m^2    vector max dev   logdet diff   band/required   asymmetry   scalar max dev   scalar min   ultralocal
    4   0.25       7.461e-14      1.137e-12      259/259         0.0e+00      2.842e-14      0.250000     False
    4   1.00       7.816e-14      2.501e-12      259/259         0.0e+00      2.398e-14      1.000000     False
    6   0.25       1.474e-13      2.728e-11     1299/1299        0.0e+00      6.573e-14      0.250000     False
    6   1.00       1.510e-13      2.910e-11     1299/1299        0.0e+00      7.994e-14      1.000000     False

**Two extents and two masses, as required. What was varied: the extent `L` from
4 to 6 (256 to 1296 sites, 1024 to 5184 one-form degrees of freedom) and `m²`
from 0.25 to 1.0.**

**The deviations grow roughly with the problem size and stay at the level of
accumulated floating-point error** — `7e-14` to `1.5e-13` for the spectrum, and
`1e-12` to `3e-11` for the determinant, whose magnitude itself grows from
`1.2e3` to `6.1e3`. **Relative to the determinant, the error falls from
`9e-16` to `5e-15`.** **The band multiplicity is exact at every point:
`nsite + 3` in all four rows.**

**What this does NOT show: a continuum limit.** Two extents at fixed `a == 1` is
a finite-volume check, not a refinement of the spacing. **`a` is fixed at 1 by
`CONVENTIONS.md:24`, so "lattice-spacing behaviour" in this construction is
reached by changing `L` at fixed `a`, and no spacing was varied.**

## 8. Validation (e) — the derivative machinery, validated and not applied

**Built and checked against two independently known answers, neither of which is
any target of the gate.**

### 8.1 A closed-form mass derivative

**`d/d(m²) log det (D0 + m²)` must equal `trace (D0+m²)^{-1}`, which at `h = 0`
is `sum_p 1/(phat2(p) + m²)` in closed form.**

    L = 4, m^2 = 0.5      closed form  36.45856448712421
      step 0.04    estimate 36.4634891200    abs error 4.925e-03
      step 0.02    estimate 36.4597925457    abs error 1.228e-03
      step 0.01    estimate 36.4588713089    abs error 3.068e-04
      one Richardson step  36.4585642299    abs error 2.572e-07

**The error falls by a factor of almost exactly four per halving — 4.01, 4.00 —
confirming the central difference is second order as intended. RICHARDSON
EXTRAPOLATION IS IMPLEMENTED and buys three further decades, from `3e-4` to
`2.6e-7`, a factor of 1193.**

### 8.2 A symmetry-enforced vanishing background derivative

**The background is a single cosine whose half period is `L / (2 q_0) = 2`
sites, an integer, so translating by two sites sends `h -> -h` while leaving the
periodic lattice invariant. The determinant is therefore an EVEN function of the
amplitude and its first derivative at zero vanishes exactly.**

    L = 4, m^2 = 0.5      baseline log det  1412.4669172371591
      step 0.02    first derivative  -3.979e-11
      step 0.01    first derivative  +4.547e-11
      step 0.005   first derivative  -4.547e-11
      largest magnitude              4.547e-11,  i.e. 3.2e-14 of the baseline

**The sign alternates and the magnitude does not fall with the step, which is
the signature of a quantity that is zero up to round-off rather than one that is
small.** The second derivative is not zero and converges cleanly:

      step 0.02    second derivative  454.12222740
      step 0.01    second derivative  454.04455675
      step 0.005   second derivative  454.02514492
      one Richardson step             454.01867430882703

**This is a validation of the machinery, not a physics result.** It says the
difference stencil, the step-size range and the Richardson step behave
correctly on a determinant of the actual constructed operator. **NO
`h`-derivative was applied to any quantity that bears on the gate's target.**

## 9. Limits, and what this artifact does not establish

### 9.1 A validated flat limit does not validate the curved construction

**`h = 0` switches off the metric coupling — the one thing the reconstruction
exists to exercise.** Every number in `§4`, `§5`, `§7` and `§8.1` is a
flat-background statement. **The curved-background content of this stage is
confined to `§6` and `§8.2`, and both are structural or symmetry checks rather
than comparisons against a known curved answer.**

**What a curved-background validation would require and this stage does not
provide:** an independently known curved quantity to compare against — a
continuum Seeley–DeWitt coefficient extracted from the same operator, or a
second discretisation of the same continuum action agreeing in the small-`h`
limit. **Neither is built here.**

### 9.2 Clean-room is a claim about provenance, not correctness

**A clean-room construction can be wrong in the same way the historical one
was.** Nothing here establishes it is not. **`§10`'s file list is the evidence
for the provenance claim and it is the only evidence there is.**

### 9.3 The construction bug the spectrum could not see

**A conjugation error was found and fixed BEFORE the freeze, and it is worth
recording because of how it was found.** The flat momentum kernel is
`phat2 delta_{mu nu} - s_mu conj(s_nu)`; an early version of this construction
wrote `- conj(s_mu) s_nu`, the complex conjugate. **Both are Hermitian with
IDENTICAL eigenvalues, so validation (a) passed at `2e-13` with the error
present.** The two differ in their null direction — `s` versus `conj(s)` — so
the transverse and longitudinal subspaces were swapped, and **only validation
(b) could see it.** It surfaced as a mixing of `0.238` where machine zero was
required.

**This is the concrete case for `§1` of the specification.** A single task that
built and scanned would have met this as a wrong number at the end, with the
distinction between "bug" and "result" drawn after seeing it.

### 9.4 A declared-dependency mismatch

**`pyproject.toml:11` lists `scipy>=1.11` as a project dependency. `scipy` is
not installed in this environment and is not among the four packages
`docs/local/execution_environment.md:10` declares required.** The existing
validator suite does not need it. **This construction uses only `numpy`, so the
gap did not block anything**, but a future stage that reaches for `scipy` on the
strength of `pyproject.toml` would fail. **Reported, not repaired.**

### 9.5 What is deliberately absent

**No determinant combination was assembled. No determinant power was varied. No
quantity that depends on such a power was evaluated. No comparison to any
external target was made. `GATES.md` was not modified and its
`Regression anchors` field still reads `None yet (proposed)` at `:754`.**

## 10. Clean-room provenance — every file read

**Read, and what entered the implementation:**

    CONVENTIONS.md
        Lines 12, 15, 16, 19, 21, 24 read.  ENTERED: :12's Euclidean d = 4 and
        :24's hypercubic lattice, a == 1, Brillouin zone and phat2 definition
        are used directly.  :15, :16, :19 and :21 were read as context for what
        the operators must be; no formula from them is transcribed into code,
        because this stage builds lattice operators and those lines are
        continuum heat-kernel statements.

    derivations/P2-BETAV-CIRC-01_determinant-decomposition.md
        PRE-FREEZE: lines 17-18 (the flat spectrum) and 66-72, 145-158 (the
        propagating-versus-ultralocal distinction and the verdict), reached by
        targeted search rather than by reading the file.  ENTERED: the required
        flat structure and the propagating-scalar requirement, as validation
        TARGETS in flat_validation.py and the test -- not as implementation.
        POST-FREEZE: lines 24-63, the quantitative sector decomposition, read
        only after commit 3a.  ENTERED NOTHING: the code was frozen.

    GATES.md
        The P2-BETAV-RECON-01 section's Status line (:727), the Regression
        anchors heading and value (:753-754), and the four gate-status and pin
        lines A12 requires.  ENTERED: nothing.  The Analytic anchors line was
        not displayed in this task -- see §11.1 for what was read in earlier
        tasks.

    pyproject.toml, tests/test_gate_anchors.py, tests/test_governance_tools.py
        Read to learn the repository's import and pytest conventions.
        ENTERED: the import style `from scripts.<pkg> import <mod>` and the
        knowledge that pytest's pythonpath is the repository root, so no
        __init__.py was needed under scripts/recon2026/ and none was added.

    docs/local/execution_environment.md
        Read for A3.  ENTERED: nothing.

    specs/2026-08-17T1653Z_recon-01a-construction.md,
    reviews/chatgpt/2026-08-17T1653Z_recon-01a-construction.md
        This task's own governance artifacts.  ENTERED: the requirements.

**NOT READ IN THIS TASK, AND NOT OPENED AT ALL:**

    scripts/recovered_2026/proca_loop.py, boson_loop.py, gfvec_loop.py,
    reproduce_betav.py, and every other file under scripts/recovered_2026/.

**The specification PERMITS reading them (`§3`) and I chose not to.** The
construction was derived from the two covariant actions in `§1` and the
discretisation choices in `§2`. **Reading them could only have made the
provenance claim weaker, since the only evidence for clean-room provenance is
the file list, and a shorter list is a stronger claim.**

**NO CODE WAS COPIED, IMPORTED, OR STRUCTURALLY REPRODUCED FROM
`scripts/recovered_2026/`.** All 24 files under that directory are
blob-identical between the evidence base and the head, and no module under it is
imported anywhere in the three new files.

**`scripts/betav_decomp_check.py` and the `P2-BETAV-CAMPAIGN` harness — the two
components `RECON-B0` classified usable — were NOT used either.** They were
classified usable as checks; this stage's checks are the analytic flat structure
and the two known-answer derivatives, which are independent of them.

## 11. Anchor isolation

### 11.1 The four withheld documents — READ, AND NOT IN THIS TASK

**`§2` asks whether I read `P2-HK-01`, `betav_discriminating_power.md`,
`P2-BETAV-SIGN-01_anchor-reconciliation.md`, or the gate's `Analytic anchors`
line, and requires disclosure if so.**

**I HAVE READ ALL FOUR, IN FULL, IN EARLIER TASKS OF THIS SAME SESSION, BEFORE
THIS SPECIFICATION EXISTED.** Specifically: `P2-HK-01` and
`betav_discriminating_power.md` were read in full while executing the
`SIGN-01` reconciliation; the gate's `Analytic anchors` line was read while
executing `RECON-B0`; and `P2-BETAV-SIGN-01_anchor-reconciliation.md` is an
artifact **I wrote.**

**NO PROHIBITION COULD HAVE MADE ME BLIND TO THEM, and this specification does
not claim otherwise** — its `§2` says so explicitly and retracts an earlier
draft that did.

**In THIS task none of the four was opened.** The `Analytic anchors` line was
avoided even while `A11` required the `Regression anchors` value three lines
away, which was read by line range.

**What the isolation claim therefore rests on: the code, not my memory.** `§11.2`
is the mechanical evidence.

### 11.2 The mechanical evidence

**Anchor information appears nowhere in the three code files. Hit counts and
paths only; the pattern set is externally supplied and is not reproduced here.**

    CODE   scripts/recon2026/proca_curved.py           hits 0
    CODE   scripts/recon2026/flat_validation.py        hits 0
    CODE   tests/test_recon2026_flat_limit.py          hits 0

**Seventeen patterns covering the ratio form in both signs, the two kill values
in both signs, the kill-criterion phrasings, the determinant combination, the
determinant-power scan, and the four withheld document names.**

**A broader eighteenth pattern was also run and IT MATCHED TWICE.** `§12.1`
reports it as a stop-class finding rather than dropping it silently.

### 11.3 No design choice was made to approach any value

**No quantity computed in this task can be compared to the gate's target.** No
determinant combination was assembled and no determinant power appears in the
code. **The validations' targets are: an analytic flat structure quoted from
`CIRC-01`, a closed-form sum, and a symmetry-enforced zero.** Two of the three
are exact and the third is a quoted repository statement.

**The one target that was adjusted during construction was a TOLERANCE, not a
physics value.** `§12.2` reports it.

## 12. Stops and clarifications

### 12.1 `SPECIFICATION_DEFECT` — the contamination scan's stop condition fires on the wording the specification instructs

**`A9` says a non-zero hit in any of the three code files is a STOP. Running the
pattern set with a broad pattern for anchor-related tokens returns TWO hits in
`tests/test_recon2026_flat_limit.py`.**

**Both are the phrase "regression anchor" in the module docstring** — the name
of the `GATES.md` field this test is a candidate for. **`§3` of the
specification instructs exactly that wording:** *"`tests/test_recon2026_flat_limit.py`
— the regression anchor."* And `A11` requires the report to confirm the
`Regression anchors` field's value.

**So the stop condition as literally instrumented fires on a word the
specification requires the deliverable to be described by.** `§2` defines the
forbidden thing as anchor INFORMATION — *"no anchor value appears … not in code,
not in a comment, not in a docstring, not in a constant, not in an
assertion"* — and the English word "anchor" carries no value, ratio, sign, or
determinant power.

**I did not resolve the inconsistency by editing the code.** The code was frozen
at commit `3a` and editing it would break the freeze `§3` establishes. **I
report both scans: the seventeen anchor-information patterns return ZERO in all
three code files, and the broad eighteenth returns two hits, both the field
name.** `§9` of the specification says to stop and report on an internal
inconsistency and not to decide which instruction prevails, and that is what
this section does.

### 12.2 `OBSERVATION_METHOD_ERROR` — two of mine, both pre-freeze

**FIRST, and it is the substantive one: a conjugation error in the flat momentum
kernel, described in `§9.3`.** It left every eigenvalue correct and swapped the
transverse and longitudinal subspaces. **Found by validation (b), which is the
only one of the five that could see it, and fixed before the freeze.**

**SECOND: a test tolerance set from the wrong quantity.** The first version
asserted that the RAW central-difference mass derivative agreed with the closed
form to `1e-6` relative. It agrees to `8.4e-6` at the smallest step, because a
second-order stencil's error is set by the step size and not by machine
precision. **The assertion was replaced by two stronger ones — that the error
falls by a factor near four per halving, and that the Richardson estimate agrees
to `1e-7`.** **Loosening the number alone would have weakened the test; asserting
the convergence ORDER tests the machinery rather than one step size.**

**Both were found and fixed before commit `3a`, so neither touched a frozen
file.** **Neither was a physics value adjusted toward an expectation:** the first
was a bug with a determinate right answer, the second a tolerance derived from
the stencil's order.

### 12.3 `SPECIFICATION_DEFECT` — the `P2-BETAV-*` count, third occurrence

**`A11` asks me to confirm "all five `derivations/P2-BETAV-*` artifacts". THERE
ARE SIX at this evidence base**, the sixth being
`P2-BETAV-SIGN-01_anchor-reconciliation.md`, landed by the task immediately
before. All six are unchanged.

**This is the third task in a row where this count was one behind, always for the
same reason: the preceding task added an artifact.** The `SIGN-01` specification
said four when there were five; this one says five when there are six. **The
count is a moving quantity being carried as a literal.**

### 12.4 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the declared environment

**`docs/local/execution_environment.md` declares a WINDOWS environment with a
Python 3.12 interpreter. Every measurement here was taken on Linux with Python
3.11.15, so in an UNDECLARED environment.** Unchanged from previous tasks and
still unregistered. **The version policy covers the version differences and is
silent on the platform.**

**Newly relevant to this task, because this is the first stage that adds
executable content:** the declared package set is `pytest`, `ruff`, `numpy`,
`sympy`, and this construction is written to that set. **`pyproject.toml:11`
declares `scipy` and it is absent — `§9.4`.** A construction written against
`pyproject.toml` rather than against the declared environment would not run here.

### 12.5 `REPOSITORY_DEFECT`, `ENVIRONMENT` — nothing to report

**`REPOSITORY_DEFECT`: none found.** 474 of 474 base paths blob-identical, both
pins recompute, `^## P2-` is 14, and all 24 files under
`scripts/recovered_2026/` unchanged.

**`ENVIRONMENT`: no failure. No restoration was needed or performed, and NEITHER
of Rule 13's two diagnostic orders was exercised.** **`scipy`'s absence is
recorded as a declaration mismatch (`§12.4`), not an environment failure: it is
not a declared package and nothing here needs it.**
