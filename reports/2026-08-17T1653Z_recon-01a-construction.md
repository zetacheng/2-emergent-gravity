# Report — `RECON-01a`: building the curved-background Proca operators and validating them against the flat limit

    branch      science/recon-01a-construction
    base        f21198cd25ae285b789b706f7c4ac0730f9fff69   (authoritative main)
    measured at commit 3b, 611292b5c6b9deb55a852852f531ae9badcb75c7
    main        NOT TOUCHED. No merge. Integration is a separate task.

**THIS TASK BUILT AND VALIDATED. IT ASSEMBLED NO DETERMINANT COMBINATION, VARIED
NO DETERMINANT POWER, AND COMPARED NOTHING TO ANY EXTERNAL TARGET.**

**THE CONSTRUCTION FREEZE HELD.** The three code files are byte-identical at
commit `3a`, at commit `3b` and at the head. `§10` gives the object ids.

**Validators: 324 passed / 2 deselected at the base, 332 passed / 2 deselected at
the head. `+8`, exactly the eight tests added.**

**A conjugation bug was found and fixed BEFORE the freeze by the one validation
that could see it. Every eigenvalue was already correct.** `§7.2` and `§15.2`.

**I have read all four withheld documents — in earlier tasks of this session,
before this specification existed, and one of them I wrote.** `§10.1` is the
disclosure. **In this task none of the four was opened.**

---

## 1. `A3` — environment conformance, run FIRST

**Rule 13's diagnostic order with Amendment D's step 0, run before any other
criterion. MEASURED, not assumed.**

    (0) execution location    /home/user/2-emergent-gravity — the primary
        (Amendment D)         worktree. git dir .git, common dir .git, so not a
                              linked worktree. HEAD branch
                              claude/paper-2-independent-verification-dysdp0,
                              resolved bfef924c368658cac85c04ed18d96eb4450afba6.
                              Eleven linked worktrees existed; this task's work
                              was done in a TWELFTH, cut fresh at
                              refs/remotes/origin/main.

    (1) interpreter           Python 3.11.15 at /usr/local/bin/python3

    (2) packages              MEASURED, every package the construction uses:
                                  numpy   2.4.6      <- used
                                  sympy   1.14.0     declared, NOT used here
                                  pytest  9.1.1      <- used
                                  ruff    0.15.8     <- used
                                  scipy   ABSENT
                              All four DECLARED packages are present.
                              numpy.linalg supplies eigvalsh, eigvals, slogdet,
                              solve and inv, which is everything the
                              construction needs.

    (3) clone depth           NOT shallow. `--is-shallow-repository` returns
                              false and no `shallow` file exists in the common
                              git dir. 501 commits reachable from all refs,
                              423 from HEAD.

    (4) working tree          clean; `status --porcelain` empty before any work.

    (5) declaration compared  `docs/local/execution_environment.md` declares a
                              WINDOWS environment. See `§15.5`.

**NO RESTORATION WAS NEEDED AND NONE WAS PERFORMED. No repository content was
touched by `A3`.**

**Rule 13 carries TWO diagnostic orders, a known open item. No environment
failure occurred, so NEITHER order was exercised.**

**`scipy` is absent and that mattered to the design.** It is not one of the four
declared packages, so **the construction was written to numpy alone.**
`pyproject.toml:11` nonetheless declares `scipy>=1.11` a project dependency —
`§15.5`.

## 2. `A1` — repository, refs, branch availability

**`origin` URL, MEASURED and reported VERBATIM, not normalised:**

    https://github.com/zetacheng/2-emergent-gravity

No `.git` suffix, no trailing slash. It identifies `zetacheng/2-emergent-gravity`.

**Refs, MEASURED after `git fetch origin main`:**

    refs/remotes/origin/main   f21198cd25ae285b789b706f7c4ac0730f9fff69
    expected by §6 A1          f21198cd25ae285b789b706f7c4ac0730f9fff69   MATCH

    refs/heads/main            1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**`refs/heads/main` LAGS and is reported for contrast.** Every measurement here
is against `refs/remotes/origin/main`.

**BRANCH AVAILABILITY — the criterion says STOP if it already exists:**

    science/recon-01a-construction   remote hits 0   local hits 0
    IT DID NOT EXIST. No stop. This task created it.

## 3. `A2` — the pre-execution review

**Field-present check run BEFORE the match check, in that order:**

    field name present     grep 'reviewed specification SHA-256' → line 4, ONE hit
    field filled in        yes — a 64-hex value, not a placeholder
    value in the review    faa403258be4a276cfafcf0b51872be19714bb9febcdad25de61184561be6068
    sha256 of the spec     faa403258be4a276cfafcf0b51872be19714bb9febcdad25de61184561be6068
                           MATCH

**Committed UNEDITED**: the committed blob's sha256 is
`1aee4bc2b7a202cac83f0a1c4f4f391ffa342745a7a5f5030929b2a955b5856a`, identical to
the uploaded bytes. **Verdict `APPROVE FOR EXECUTION`, fifteen sections all
`PASS`.**

## 4. `A4` — the construction, and every convention fixed HERE

**Two operators on a periodic `L^4` Euclidean lattice, spacing `a = 1`, built
from covariant ACTIONS rather than from kernels written down directly:**

    S0[phi] = 1/2 sum_x sqrt(g) g^{mu nu} (d_mu phi)(d_nu phi)
                + m^2/2 sum_x sqrt(g) phi^2
    S1[A]   = 1/4 sum_x sqrt(g) g^{mu al} g^{nu be} F_{mu nu} F_{al be}
                + m^2/2 sum_x sqrt(g) g^{mu nu} A_mu A_nu
    F_{mu nu}(x) = (d_mu A_nu)(x) - (d_nu A_mu)(x)

    D0 + m^2 = G0^{-1} K0 + m^2 * 1      G0 = diag(sqrt(g))
    D1 + m^2 = G1^{-1} K1 + m^2 * 1      G1[(x,mu),(x,nu)] = sqrt(g) g^{mu nu}

**Per operator, as `A4` requires:**

    D1   discretisation   forward differences in the field strength;
                          the Hessian of S1 accumulated per site
         metric coupling  sqrt(g) g^{mu al} g^{nu be}, site-centred, with
                          g^{mu nu} the exact inverse
         boundary cond.   periodic in all four directions
         free parameters  L in {4, 6}; m^2 in {0.25, 1.0} spectral,
                          {0.09, 0.5} derivative; amplitude in
                          {0, 0.02, 0.04, 0.08}; wavevector q = (1,0,0,0),
                          and (2,0,0,0), (3,0,0,0) in the post-freeze check

    D0   discretisation   forward differences in the Dirichlet form;
                          the Hessian of S0 accumulated per site
         metric coupling  sqrt(g) g^{mu nu}, site-centred
         boundary cond.   periodic in all four directions
         free parameters  as above

**SIX CONVENTIONS WERE FIXED HERE THAT `CONVENTIONS.md` DOES NOT FIX. EACH IS A
CHOICE MADE BY THIS TASK AND NOT A REPOSITORY FACT.** `CONVENTIONS.md` supplies
only `:12`'s Euclidean `d = 4` and `:24`'s hypercubic lattice, `a == 1`,
Brillouin zone and `phat2 = sum_mu 4 sin^2(p_mu/2)`. **It fixes no lattice
realisation of either operator.**

    C1  FORWARD DIFFERENCES, (d_mu f)(x) = f(x+mu) - f(x).
        Load-bearing twice over: it makes the free scalar kernel equal :24's
        phat2 exactly, and it makes the 1-form's non-dispersing band exactly
        momentum-independent, because forward differences commute.
    C2  SITE-CENTRED geometric factors, not link- or plaquette-centred.
    C3  PERIODIC boundary conditions in all four directions.
    C4  g^{mu nu} the EXACT MATRIX INVERSE, not a weak-field truncation;
        sqrt(g) = sqrt(det g).  The construction is not perturbative in h.
    C5  THE OPERATOR IS THE HESSIAN DIVIDED BY THE MASS METRIC, so the mass
        term is exactly m^2 * 1.  THE MOST CONSEQUENTIAL OF THE SIX — §7.2.
    C6  A single-cosine weak-field background.  Nothing in the repository
        fixes a background profile.

**`§14.3` states what follows for a later reader, and it is the answer to Rule
16's third junction: SIX is the number of places to look first if `RECON-01b`
returns a wrong number.**

## 5. `A5`, `A6` — the five validations

### 5.1 `A6` — the flat-limit target, and the one thing I had to make precise

**`derivations/P2-BETAV-CIRC-01_determinant-decomposition.md:17-18`, quoted:**

> Flat kernel `M_{μν}(k) = (ŝ²+m²)δ_{μν} − a_μ a_ν*`. Spectrum (verified):
> `{ŝ²+m² (×3 transverse), m² (×1 longitudinal)}`, `det M(k)=m²(ŝ²+m²)³`.

**PRECISE AS STATED:** the multiplicities three and one, which band disperses,
and the determinant `m²(ŝ²+m²)³` — a third, independent statement that `§5.2`
uses as a global check.

**NOT PRECISE, AND I HAD TO MAKE IT SO: what `ŝ²` is.** The symbol is undefined
in those lines, and **`CONVENTIONS.md:24` defines TWO different free-field
momenta** — `phat2 = sum_mu 4 sin^2(p_mu/2)` for the naive/scalar case and
`sbar_mu = sin p_mu` — **either of which could be squared and summed into
something called `ŝ²`. They are different functions.**

**I made it precise by construction, not by choosing:** C1's forward difference
gives `|exp(i p_mu) - 1|^2 = 4 sin^2(p_mu/2)`, so this construction's dispersing
band is `phat2 + m^2`. **A construction with symmetric differences would have
produced the other function and disagreed with the same quoted line.** Recorded
as the resolution of an ambiguity.

**A second thing the quoted line does not say, which the construction forced:**
at `p = 0` the symbol vanishes, so all four bands sit at `m²` and the total
multiplicity of `m²` is `nsite + 3`, not `nsite`. **A test asserting `nsite`
would fail on a correct construction.** `A7` of `RECON-B0` asked whether this
target was precise enough to test against; **its answer was yes for the
eigenstructure, and this is the residue that answer did not cover.**

### 5.2 `(a)` The flat 1-form spectrum

    L = 4, m^2 = 0.25
      relative asymmetry of the operator at h = 0        0.0        (measured)
      max |numeric - required| over the spectrum          7.46e-14
      multiplicity of the non-dispersing band             259  (required 259)
      log det, full position-space operator          1206.5450159411748
      log det, sum over analytic momentum blocks     1206.5450159411760
      absolute difference                                 1.14e-12

**The determinant cross-check is the strongest single statement in this report.**
A `1024 x 1024` matrix assembled by per-site accumulation agrees with a product
of analytic `4 x 4` blocks to `1.1e-12`. **It tests the geometric-factor
bookkeeping in a way no eigenvalue comparison does.**

    sampled blocks    coord        phat2      eigenvalues
                      (0,0,0,0)   0.000000   [0.25, 0.25, 0.25, 0.25]
                      (1,0,0,0)   2.000000   [0.25, 2.25, 2.25, 2.25]
                      (0,2,0,0)   4.000000   [0.25, 4.25, 4.25, 4.25]
                      (1,2,0,0)   6.000000   [0.25, 6.25, 6.25, 6.25]
                      (2,2,0,0)   8.000000   [0.25, 8.25, 8.25, 8.25]

**One band pinned at `m²` regardless of momentum; three at `phat2 + m²`.**

### 5.3 `(b)` Transverse/longitudinal separation — MY NUMBERS FIRST

**MEASURED BEFORE `CIRC-01`'s FIGURE WAS READ. Two forms, because they do not
agree, and the disagreement is the finding.**

    L = 4, m^2 = 0.25                THE OPERATOR       THE HESSIAN
    ||Pi_T X Pi_L||_F / ||X||_F      D1 + m^2 (C5)      K1 + m^2 G1
      amplitude 0.00                   3.0721e-16         3.0721e-16
      amplitude 0.02                   3.2752e-16         1.7467e-04
      amplitude 0.04                   3.2335e-16         3.4933e-04
      amplitude 0.08                   3.2533e-16         6.9864e-04
      leading power in amplitude          -0.0048            0.99996

**The operator as constructed has NO mixing at all — machine level, every
amplitude, no amplitude dependence. The Hessian of the same action before
dividing by the mass metric mixes at exactly `O(amplitude)`.**

**`CIRC-01`'s figure, read only after commit `3a`:**
`P2-BETAV-CIRC-01_determinant-decomposition.md:37-47` reports the mixed `TL+LT`
`q²` coefficient as **`≈ +9.0e-5`, about `0.4%` of the total, exponent `≈ 1.98`,
stable `8.7e-5`–`9.1e-5` across grids.**

**THE TWO ARE NOT COMMENSURABLE, AND SAYING `3e-16 vs 9e-5` WOULD BE A CATEGORY
ERROR.** Mine is the off-diagonal block of the OPERATOR at a single momentum — a
one-graviton vertex-level quantity. `CIRC-01`'s is the mixed `q²` coefficient of
the induced BUBBLE with projectors built independently at `k` and `k+q` — a
two-momentum, second-order-in-vertex quantity.

**`CIRC-01` says so itself and withdraws the single-momentum measurement.** Its
`:26-29`: *"The relevant test is **not** whether the one-graviton vertex
off-block norm vanishes as `q→0`."* Its `:50-52`: the vertex mixing does vanish
as `q→0`, and *"the earlier vertex-norm figure was measured in the wrong,
single-momentum basis and is withdrawn."*

**`§5.3`'s measurement is in the class `CIRC-01` withdrew.** Not a defect in the
construction — the criterion asked for the separation built and measured, and it
was — **but the comparison is a statement about commensurability, not a
number.**

**One genuine consistency point:** `CIRC-01` says the vertex mixing vanishes as
`q→0`; my operator-level mixing is exactly zero at every `q`, **consistent with
that and stronger.**

**One genuine non-correspondence, measured POST-FREEZE with the construction
unchanged** (`L = 6`, `m² = 0.09` to match `CIRC-01`'s stated mass,
amplitude `0.04`):

    q = (3,0,0,0)   qhat2 4.00000   operator 6.1384e-16   Hessian 1.8114e-04
    q = (2,0,0,0)   qhat2 3.00000   operator 6.1446e-16   Hessian 1.2829e-04
    q = (1,0,0,0)   qhat2 1.00000   operator 6.1567e-16   Hessian 1.2845e-04

**The Hessian form's mixing does NOT fall toward zero as `qhat2` falls** — it is
dominated by the mass-metric block, which is `O(h)` and carries no factor of the
background momentum. **So neither of my forms reproduces a `q→0`-vanishing
vertex: one is identically zero, the other momentum-insensitive.** **Reported,
not tuned — the code was frozen and tuning was unavailable.**

### 5.4 `(c)` The compensating scalar is PROPAGATING

    L = 4, m^2 = 0.25
      max |numeric - (phat2 + m^2)|   2.84e-14
      minimum eigenvalue              0.24999999999999395
      maximum eigenvalue             16.250000000000018
      eigenvalue spread              16.000000000000025
      distinct eigenvalues            9
      is_ultralocal                   False

**`D0 + m²` DISPERSES: spread 16, nine distinct values.** Its minimum equals
`m²` only because `phat2(0) = 0`. **It is `Δ + m²`, not the ultralocal `m²`** —
the distinction `CIRC-01:157-158` says `DECOMP-UNAVAILABLE-AS-RECOVERED` turned
on. **A correctness condition, not a fitting condition.**

### 5.5 `(d)` Extents and masses

    L   m^2    vec max dev   logdet diff   band/req     asym    scalar dev   scalar min   ultralocal
    4   0.25    7.461e-14     1.137e-12    259/259     0.0e+00   2.842e-14    0.250000     False
    4   1.00    7.816e-14     2.501e-12    259/259     0.0e+00   2.398e-14    1.000000     False
    6   0.25    1.474e-13     2.728e-11   1299/1299    0.0e+00   6.573e-14    0.250000     False
    6   1.00    1.510e-13     2.910e-11   1299/1299    0.0e+00   7.994e-14    1.000000     False

**WHAT WAS VARIED: the extent `L` from 4 to 6 — 256 to 1296 sites, 1024 to 5184
one-form degrees of freedom — and `m²` from 0.25 to 1.0.** Deviations grow with
problem size and stay at accumulated-round-off level; relative to the
determinant the error FALLS, from `9e-16` to `5e-15` on a value growing from
`1.2e3` to `6.1e3`. **Band multiplicity exact in all four rows.**

**WHAT THIS IS NOT: a continuum limit.** `a` is fixed at 1 by
`CONVENTIONS.md:24`, so **no lattice spacing was varied; two extents at fixed
`a` is a finite-volume check.** I report that rather than calling `L`-variation
a refinement.

### 5.6 `(e)` The derivative machinery, validated and NOT applied

**First known answer — a closed form.** `d/d(m²) log det (D0 + m²)` equals
`trace (D0+m²)^{-1}`, which at `h = 0` is `sum_p 1/(phat2(p) + m²)`.

    L = 4, m^2 = 0.5     closed form  36.45856448712421
      step 0.04   estimate 36.4634891200   abs error 4.925e-03
      step 0.02   estimate 36.4597925457   abs error 1.228e-03
      step 0.01   estimate 36.4588713089   abs error 3.068e-04
      Richardson             36.4585642299   abs error 2.572e-07

**The error falls by 4.01 then 4.00 per halving, confirming second order.**
**RICHARDSON EXTRAPOLATION IS IMPLEMENTED — the gate names it in `Inputs` — and
it gives `2.57e-7`, an improvement of 1193x over the smallest raw step.**

**Second known answer — a symmetry-enforced zero.** The background's half period
is `L/(2 q_0) = 2` sites, an integer, so a two-site translation sends `h → −h`
while leaving the periodic lattice invariant; the determinant is therefore EVEN
in the amplitude and its first derivative at zero vanishes exactly.

    L = 4, m^2 = 0.5     baseline log det  1412.4669172371591
      step 0.02   first derivative  -3.979e-11
      step 0.01   first derivative  +4.547e-11
      step 0.005  first derivative  -4.547e-11
      largest magnitude  4.547e-11  =  3.2e-14 of the baseline
      second derivative  454.12222740 / 454.04455675 / 454.02514492
      Richardson         454.01867430882703

**The sign alternates and the magnitude does not fall with the step — the
signature of a quantity that is zero up to round-off, not one that is merely
small.** **NO `h`-derivative was applied to any quantity bearing on the gate's
target.**

## 6. `A8` — the new test

**Eight tests in `tests/test_recon2026_flat_limit.py`, all PASSING. Node ids and
what each asserts:**

    ::test_flat_one_form_spectrum_has_three_dispersing_bands_and_one_flat_band
        the operator is symmetric at h = 0; the spectrum matches the required
        structure to 1e-9; the non-dispersing multiplicity equals nsite + 3
    ::test_flat_one_form_longitudinal_band_is_momentum_independent
        at EVERY momentum the lowest band is m^2 to 1e-12 and the other three
        are phat2 + m^2
    ::test_position_space_determinant_matches_momentum_block_factorisation
        log det of the assembled operator equals the analytic block sum to 1e-8
    ::test_compensating_scalar_is_propagating_not_ultralocal
        D0 + m^2 disperses: spread > 1, more than one distinct eigenvalue,
        minimum equal to m^2, and NOT ultralocal
    ::test_transverse_longitudinal_mixing_vanishes_on_the_flat_background
        relative mixing < 1e-12 at h = 0
    ::test_gauge_kernel_of_the_field_strength_hessian_is_metric_independent
        on a CURVED background K1 still annihilates the flat longitudinal band;
        the operator does not mix and the pre-division Hessian does
    ::test_mass_derivative_machinery_reproduces_the_closed_form
        the raw error is < 1e-5 relative, falls by a factor in (3.5, 4.5) per
        halving, and Richardson agrees to < 1e-7
    ::test_background_derivative_vanishes_at_zero_amplitude_by_symmetry
        the symmetry is available and the first derivative is < 1e-9 of the
        baseline

**VALIDATOR COUNTS, BOTH MEASURED:**

    at the base f21198cd…     324 passed, 2 deselected
    at commit 3b              332 passed, 2 deselected
    difference                 +8 passed, deselected unchanged

**The increase equals the number of tests added, exactly. No other change.** The
base figure was measured by me at this very commit — it is the `A17` measurement
of the preceding integration task, whose commit 4 IS this evidence base.

## 7. Two findings from the construction itself

### 7.1 The gauge kernel is metric-independent, and C5 relocates the mixing

**`||K1 · Pi_L||` is `7.6e-14` at every amplitude tested, curved as well as
flat.** The reason is exact and carries no metric: `F_{mu nu}` vanishes
identically on `A_mu = d_mu lambda` because forward differences commute (C1),
and the flat longitudinal direction at momentum `p` is exactly that pure-gauge
direction. **So the flat longitudinal subspace is the exact gauge kernel of `K1`
for ANY metric.**

**The mass term is the only part that could mix, and C5 divides it away:**
`(D1+m²) Pi_L = m² Pi_L`, so `Pi_T (D1+m²) Pi_L = 0` identically, and on a
curved background the non-dispersing band is still exactly `m²` with
multiplicity 259.

**C5 IS THEREFORE NOT A BOOKKEEPING PREFERENCE.** It moves the whole
transverse/longitudinal mixing out of the operator and into the measure factor
`det G1`. **The mixing is not removed from the physics; it is relocated to a
place this stage does not examine.** **`RECON-01b` inherits that and must decide
whether the determinant it needs is of `D1 + m²` or of `K1 + m² G1`, because
they differ by `det G1` and only the second mixes.**

### 7.2 A conjugation bug the spectrum could not see

**The flat momentum kernel is `phat2 delta_{mu nu} - s_mu conj(s_nu)`. An early
version of this construction wrote `- conj(s_mu) s_nu`, the complex
conjugate.**

**Both are Hermitian with IDENTICAL eigenvalues.** Validation `(a)` passed at
`2e-13` with the error present, and so did the determinant cross-check and the
scalar check. **The two differ only in their null direction — `s` versus
`conj(s)` — so the transverse and longitudinal subspaces were swapped, and only
validation `(b)` could see it.** It surfaced as a relative mixing of `0.238`
where machine zero was required.

**I diagnosed it analytically before changing anything**: expanding
`sum_{mu<nu} |Ftilde|^2` gives `phat2 |A|^2 - |s^dag A|^2`, which fixes the
order, and the measurement then agreed. **Fixed before commit `3a`.**

**THIS IS THE CONCRETE CASE FOR THE SPLIT `§1` OF THE SPECIFICATION ARGUES
FOR.** A single task that built and scanned would have met this as a wrong
number at the end, with "bug" versus "result" decided after seeing it.

## 8. `A9`, `A10` — isolation, staging, scope

### 8.1 The contamination scan — hit counts and paths, patterns NOT reproduced

**Seventeen patterns, supplied externally and held only in the scanning process,
covering the ratio form in both signs, both kill values in both signs, the
kill-criterion phrasings, the determinant combination, the determinant-power
scan, and the four withheld document names.**

    CODE   scripts/recon2026/proca_curved.py           hits 0
    CODE   scripts/recon2026/flat_validation.py        hits 0
    CODE   tests/test_recon2026_flat_limit.py          hits 0
    GOVN   specs/…T1653Z_recon-01a-construction.md     hits 46
    GOVN   reviews/chatgpt/…T1653Z_recon-01a-…md       hits 25

**ZERO HITS IN ALL THREE CODE FILES. The `A9` stop condition is NOT triggered by
the anchor-information pattern set.** The governance-file hits are the
specification and its review discussing the discipline, which is what those
documents are for.

**A BROADER EIGHTEENTH PATTERN WAS ALSO RUN AND IT MATCHED TWICE.** `§15.1`
reports it as a stop-class finding rather than dropping it silently.

**The derivation artifact was scanned too: zero hits on every value, form and
phrasing; its only matches are the four document NAMES, which `A9` requires it
to disclose.**

### 8.2 The four withheld documents — READ, AND NOT IN THIS TASK

**`A9` asks separately whether I read `P2-HK-01`,
`betav_discriminating_power.md`, `P2-BETAV-SIGN-01_anchor-reconciliation.md`, or
the gate's `Analytic anchors` line, and to say which and when if so.**

**I HAVE READ ALL FOUR, IN FULL, IN EARLIER TASKS OF THIS SESSION, BEFORE THIS
SPECIFICATION EXISTED:**

    P2-HK-01                          read in full during SIGN-01
    betav_discriminating_power.md      read in full during SIGN-01
    the gate's Analytic anchors line   read during RECON-B0 and again during
                                       SIGN-01 and its integration
    P2-BETAV-SIGN-01_anchor-…md        I WROTE IT

**No prohibition could have made me blind to them, and this specification does
not claim otherwise** — its `§2` says so and retracts an earlier draft that
did.

**IN THIS TASK NONE OF THE FOUR WAS OPENED.** The `Analytic anchors` line was
avoided even though `A11` required the `Regression anchors` value three lines
below it, which was read by explicit line range `753-755`.

**So the isolation claim rests on the code and the staging, not on my memory** —
`§8.1` and `§8.3`.

### 8.3 The staging, and the freeze

    commit 3a   1a9c4af369baffd189c34caf521a7fe349427fb7   17:09:17Z
                the three code files, and ONLY those three
    commit 3b   611292b5c6b9deb55a852852f531ae9badcb75c7   17:20:05Z
                the derivation artifact, and ONLY that

**THE THREE CODE BLOBS, AT `3a`, AT `3b`, AND AT THE HEAD:**

    scripts/recon2026/proca_curved.py     03f46905e5798fb7f6880dfae9ed5a1931be895b
    scripts/recon2026/flat_validation.py  6b21f9d6db67641ec7de31b7006884b617de3e8c
    tests/test_recon2026_flat_limit.py    1d7ba5672614dedcd3b78483b5d43431af65fc7a

**ALL THREE SETS IDENTICAL.** `git diff --name-status` on `3a..3b` returns
exactly one line, the artifact's addition. **That identity is the evidence that
`CIRC-01`'s quantitative figure did not reach the construction** — it was read
between the two commits and the tree did not move.

**No `__init__.py` was added under `scripts/recon2026/`, and none was needed:**
pytest's `pythonpath = ["."]` plus namespace-package resolution imports it. **The
manifest does not name one, and `A10` says a construction that outgrows the
manifest is a specification defect and not an executor decision — so I confirmed
the import worked without one rather than adding a file.**

### 8.4 `A10` — scope

**MEASURED at commit 3b — 6 ADDITIONS, 0 MODIFICATIONS:**

    A  derivations/P2-BETAV-RECON-01a_construction-and-flat-validation.md
    A  reviews/chatgpt/2026-08-17T1653Z_recon-01a-construction.md
    A  scripts/recon2026/flat_validation.py
    A  scripts/recon2026/proca_curved.py
    A  specs/2026-08-17T1653Z_recon-01a-construction.md
    A  tests/test_recon2026_flat_limit.py

**INTENDED at commit 4 — 7 additions, 0 modifications**, adding
`reports/2026-08-17T1653Z_recon-01a-construction.md`, this file. **MEASURING
THAT IS POST-REPORT EVIDENCE AND NOTHING HERE CLAIMS TO HAVE DONE IT.**

**`modify:` is `[]` and remained `[]`. Zero non-addition status entries in the
range.**

**`append_only: DECISION_LOG.md` is a CHECKER-CONFIGURATION DECLARATION, NOT AN
AUTHORISATION TO WRITE THAT FILE.** It was not written.

**The `{HHMM}Z` token.** UTC measured before writing anything:
`2026-08-17T16:53:50Z`, giving `1653Z`. **Commit 1's recorded time is
`2026-08-17 16:54:07 +0000`** — 17 seconds later, the same minute. All four
authored governance paths carry `1653Z`.

## 9. `A11`, `A12` — nothing existing changed, and the gate is untouched

    paths at the evidence base   474
    paths at the head            479
    COMPARED                     474
    IDENTICAL                    474
    DIFFERING                      0
    missing at the head            0
    new at the head                5 at commit 3a, 6 at commit 3b

**Named confirmations, each a blob comparison:**

    GATES.md                                1 path    unchanged
    CONVENTIONS.md                          1 path    unchanged
    derivations/P2-BETAV-*                  6 paths   all unchanged
    P2-LATTICE-MICROSPEC-01 artifacts       7 paths   all unchanged
    registers                               2 paths   both unchanged
    scripts/recovered_2026/                24 paths   ALL UNCHANGED
    results/                               69 paths   all unchanged
    scripts/ (all, at the base)            60 paths   all unchanged
    tests/  (all, at the base)             21 paths   all unchanged

**`GATES.md` IN PARTICULAR — the `Regression anchors` field, read by explicit
line range to avoid the line `§2` withholds:**

    GATES.md:753   ### Regression anchors
    GATES.md:754   None yet (proposed).

**IT STILL READS `None yet (proposed)`. This task did not register its test as an
anchor, and `GATES.md` is blob-identical to the base.**

**`A12`, all four invariants, each read SCOPED:**

    ^## P2- section count                    14        expected 14   MATCH
    P2-PHASE-01, GATES.md:971-1108
      :973    Status: PROPOSED                                       MATCH
    both prerequisites SATISFIED
      :1011   Artifact state: **ADOPTED**. Prerequisite state: **SATISFIED**,
      :1036   Artifact state: **ADOPTED**. Prerequisite state: **SATISFIED**.
    both pins recomputed
      :1017   4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214   identical
      :1040   e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3   identical

**THE THREE `BETAV` STATUSES, scoped:**

    P2-BETAV-RECON-01   GATES.md:725-789   :727  Status: PROPOSED (not run;
                        distinct from the historical circularity question)
    P2-BETAV-CIRC-01    GATES.md:328-597   :330  Status: RUN
    P2-BETAV-01         GATES.md:207-264   :209  Status: PROPOSED (deferred —
                        not computed this sweep)

**NONE CHANGED. BUILDING A CONSTRUCTION DOES NOT ADVANCE A GATE**, and the
strongest evidence is that `GATES.md` is blob-identical.

## 10. `A7` — clean-room provenance, every file read

**Read, and what entered the implementation:**

    CONVENTIONS.md
        Lines 12, 15, 16, 19, 21, 24.  ENTERED: :12's Euclidean d = 4 and :24's
        lattice, a == 1, Brillouin zone and phat2 are used directly.  :15, :16,
        :19, :21 read as context for what the operators must be; no formula from
        them is transcribed into code, because they are continuum heat-kernel
        statements and this stage builds lattice operators.

    derivations/P2-BETAV-CIRC-01_determinant-decomposition.md
        PRE-FREEZE: :17-18 and :66-72, :145-158, reached by TARGETED SEARCH
        rather than by reading the file, so its §2 stayed unread.
        ENTERED: the required flat structure and the propagating-scalar
        requirement, as validation TARGETS — not as implementation.
        POST-FREEZE: :24-63, the quantitative sector decomposition, read only
        after commit 3a.  ENTERED NOTHING; the code was frozen.

    GATES.md
        :727, :753-755, and the four A12 invariant lines.  ENTERED: nothing.
        The Analytic anchors line was not displayed in this task.

    pyproject.toml, tests/test_gate_anchors.py, tests/test_governance_tools.py
        Read for the repository's import and pytest conventions.  ENTERED: the
        import style `from scripts.<pkg> import <mod>`, and the fact that
        pythonpath is the repository root — which is why no __init__.py was
        needed and none was added.

    docs/local/execution_environment.md      ENTERED: nothing (A3 only).
    this task's spec and review               ENTERED: the requirements.

**NOT READ IN THIS TASK, AND NOT OPENED AT ALL:**

    every file under scripts/recovered_2026/ — 24 paths, including
    proca_loop.py, boson_loop.py, gfvec_loop.py, reproduce_betav.py

**The specification PERMITS reading them and I chose not to.** The construction
came from the two covariant actions and the six discretisation choices. **Reading
them could only have weakened the provenance claim, because the file list is the
only evidence there is and a shorter list is a stronger claim.**

**NO CODE WAS COPIED, IMPORTED, OR STRUCTURALLY REPRODUCED FROM
`scripts/recovered_2026/`.** All 24 files there are blob-identical base to head,
and no module under it is imported anywhere in the three new files.

**`scripts/betav_decomp_check.py` and the `P2-BETAV-CAMPAIGN` harness — the two
components `RECON-B0` classified usable — were NOT used either.** They are usable
as checks; this stage's checks are the analytic flat structure and two
known-answer derivatives, independent of both.

## 11. `A13` — the checker over this task's own range, MEASURED at commit 3b

    base   f21198cd25ae285b789b706f7c4ac0730f9fff69
    head   611292b5c6b9deb55a852852f531ae9badcb75c7   (commit 3b)

    run 1 INCLUSIVE   exit 0   PASS   273 lines   sha256 0005fe083c7db88eab730289271b57a203c4905298eeb838871b5e9ee249deff
    run 1 EXCLUSIVE   exit 0   PASS   273 lines   sha256 4f5161d34120407e54e5a73b54d85f1f386ef2a38d84968f441d39b06138d0c9
    run 2 INCLUSIVE   exit 0   PASS   273 lines   sha256 0005fe083c7db88eab730289271b57a203c4905298eeb838871b5e9ee249deff
    run 2 EXCLUSIVE   exit 0   PASS   273 lines   sha256 4f5161d34120407e54e5a73b54d85f1f386ef2a38d84968f441d39b06138d0c9

    stderr empty in all four.

    P1 PASS   P2 PASS   P3 PASS   P4 PASS
    P5 NOT_APPLICABLE — no merge commit in range
    P6 PASS   P7 PASS   P8 PASS
    P9 NOT_APPLICABLE — range adds no report

    overall PASS in all four.   commits_in_range 4   first-parent 4

### 11.1 PARSED, not grepped

**PARSED with a JSON walker over every `status` and `overall` field:**

    19 x PASS  +  2 x NOT_APPLICABLE  =  21 values, and NOTHING ELSE.
    ZERO NON_GREEN statuses. ZERO DECLARATION_CONFLICT statuses.

**A TOKEN GREP OF THE SAME BYTES RETURNS, in every one of the four outputs:**
`NOT_DECLARED` 1, `NOT_PARSEABLE` 2, `DECLARATION_CONFLICT` 0. **All three are
`NON_GREEN` members and there are none — both tokens occur only in definitional
prose, the `overall_note` and `P1`'s `does_not_establish`.** The specification
instructs parsing; I parsed, and the measurement reproduces at this range.

### 11.2 What `RUN 1` did

**MEASURED: `RUN 1`'s default subject selection selected exactly ONE
specification** — this task's, the only one in range:

    specs/2026-08-17T1653Z_recon-01a-construction.md
    stated: 7 additions, 0 modifications    counted 7 / 0    parse OK

**`RUN 1` and `RUN 2` are BYTE-IDENTICAL at each reading**, `diff` returning
nothing, so the four invocations produce exactly TWO distinct byte strings.
**That does not make them the same check: `RUN 2` names the subject and `RUN 1`
discovers it.**

**The `C3` multi-specification residual DID NOT ARISE, and the reason is that
there is ONE declaring specification, not that declarations agreed** — the
"cannot trigger" half of that diagnosis. **Unchanged and still unregistered.**

**`P1`'s `counted_set` holds the literal `{HHMM}Z` placeholders**, because `P1`
compares a specification's `stated:` total against its own manifest block rather
than against the diff. **The three code paths in the manifest carry no token and
appear literally.**

### 11.3 `declared_source`, `P7`, `P8`

    P3   PASS   declared_source: specification   declared ['DECISION_LOG.md']
    P7   PASS   declared_source: specification   declared []
                section_count_base 14   section_count_head 14   raw 14
    P8   PASS   specification_is_first_commit: true
                first_commit_paths ['specs/2026-08-17T1653Z_recon-01a-construction.md']

**`P7` REPORTS FOURTEEN SECTIONS. `PASS` AT ZERO WOULD HAVE BEEN A STOP.**

**`P5` and `P9` are `NOT_APPLICABLE`, not weak passes** — no merge in range, and
no report in range at commit 3b. **At commit 4 `P9` acquires a subject;
measuring that is post-report evidence.**

### 11.4 `RUN 1` config, verbatim — observational, governs nothing

    {
      "base": "f21198cd25ae285b789b706f7c4ac0730f9fff69",
      "head": "611292b5c6b9deb55a852852f531ae9badcb75c7",
      "append_only_paths": [
        "DECISION_LOG.md"
      ],
      "authorised_modified_gates": [],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "inclusivity": "INCLUSIVE"
      },
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 11.5 `RUN 2` config, verbatim — stop-governing

    {
      "base": "f21198cd25ae285b789b706f7c4ac0730f9fff69",
      "head": "611292b5c6b9deb55a852852f531ae9badcb75c7",
      "specification_paths": [
        "specs/2026-08-17T1653Z_recon-01a-construction.md"
      ],
      "append_only_paths": [
        "DECISION_LOG.md"
      ],
      "authorised_modified_gates": [],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "inclusivity": "INCLUSIVE"
      },
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

**No value in either config is one I chose**, and **neither the config nor this
specification's declarations were adjusted to make `RUN 2` pass. `RUN 2` passed
on its first invocation at both readings.**

### 11.6 The output, verbatim, `INCLUSIVE` reading

**`RUN 1` and `RUN 2` are byte-identical here, verified by `diff`.**

    {
      "base": "f21198cd25ae285b789b706f7c4ac0730f9fff69",
      "commits_in_range": 4,
      "commits_on_first_parent_line": 4,
      "head": "611292b5c6b9deb55a852852f531ae9badcb75c7",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "append_only": [
                "DECISION_LOG.md"
              ],
              "authorised_gates": [],
              "counted": 7,
              "counted_add": 7,
              "counted_modify": 0,
              "counted_set": [
                "derivations/P2-BETAV-RECON-01a_construction-and-flat-validation.md",
                "reports/2026-08-XXT{HHMM}Z_recon-01a-construction.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_recon-01a-construction.md",
                "scripts/recon2026/flat_validation.py",
                "scripts/recon2026/proca_curved.py",
                "specs/2026-08-XXT{HHMM}Z_recon-01a-construction.md",
                "tests/test_recon2026_flat_limit.py"
              ],
              "parse": "OK",
              "path": "specs/2026-08-17T1653Z_recon-01a-construction.md",
              "stated": 7,
              "stated_add": 7,
              "stated_modify": 0,
              "stated_record": "stated: 7 additions, 0 modifications"
            }
          ],
          "id": "P1",
          "status": "PASS",
          "title": "scope manifest arithmetic"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "commits": [
              {
                "adds_review": false,
                "commit": "4bddd1162b27ec6ec6012f8680492ca81641d4b5",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "d183d36dfaf808d58be66f77293ef71e22f38196",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "1a9c4af369baffd189c34caf521a7fe349427fb7",
                "work_paths": [
                  "scripts/recon2026/flat_validation.py",
                  "scripts/recon2026/proca_curved.py",
                  "tests/test_recon2026_flat_limit.py"
                ]
              },
              {
                "adds_review": false,
                "commit": "611292b5c6b9deb55a852852f531ae9badcb75c7",
                "work_paths": [
                  "derivations/P2-BETAV-RECON-01a_construction-and-flat-validation.md"
                ]
              }
            ],
            "first_review_commit": "d183d36dfaf808d58be66f77293ef71e22f38196",
            "first_work_commit": "1a9c4af369baffd189c34caf521a7fe349427fb7",
            "in_scope": 4,
            "out_of_scope": []
          },
          "id": "P2",
          "status": "PASS",
          "title": "Rule 15 commit order"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
          "evidence": {
            "declared": [
              "DECISION_LOG.md"
            ],
            "declared_by_specification": [
              "DECISION_LOG.md"
            ],
            "declared_key": "append_only",
            "declared_source": "specification",
            "paths": [
              {
                "base_bytes": 89541,
                "base_is_byte_prefix_of_head": true,
                "commits_with_deletions": [],
                "deleted_lines_base_to_head": 0,
                "head_bytes": 89541,
                "path": "DECISION_LOG.md",
                "status": "PASS"
              }
            ],
            "specification_paths_read": [
              "specs/2026-08-17T1653Z_recon-01a-construction.md"
            ],
            "supplied_by_config": [
              "DECISION_LOG.md"
            ]
          },
          "id": "P3",
          "status": "PASS",
          "title": "append-only on both measures"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "entries": [
              {
                "branch": "fix/pi-decisions-and-deferred",
                "commit": "52f651174dc1fef03b4fb9276078fa1f08d94bd7",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "fix/pi-decisions-v2",
                "commit": "ebd531ab568aaffabd86a4a94d925a711e62aa36",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-v2",
                "commit": "40168469608618aef6812735ff70e32de0e3cbc8",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-and-superseded",
                "commit": "7146a093c65788a57d63a747b71d86edb91eddc6",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "review/role-model-and-executors",
                "commit": "10c260b96882ac12610f78840aeeabd07be2d7cb",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "gate/p2-land-diquark-line",
                "commit": "d64cd912ca9ff78a85787f0e54f345f474cdb192",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              }
            ],
            "register_path": "docs/BRANCHING_POLICY.md"
          },
          "id": "P4",
          "status": "PASS",
          "title": "superseded branches are not merged"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the executor derived the parentage values independently; three correct values are equally consistent with fresh recomputation and with one field copied into another. The diquark task's shared-rationale defect would pass this check.",
          "evidence": {
            "merges": []
          },
          "id": "P5",
          "reason": "no merge commit in range",
          "status": "NOT_APPLICABLE",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "4bddd1162b27ec6ec6012f8680492ca81641d4b5",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "d183d36dfaf808d58be66f77293ef71e22f38196",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "1a9c4af369baffd189c34caf521a7fe349427fb7",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "611292b5c6b9deb55a852852f531ae9badcb75c7",
              "matches": [],
              "status": "PASS"
            }
          ],
          "id": "P6",
          "status": "PASS",
          "title": "commit-message hygiene"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
          "evidence": {
            "added_sections": [],
            "authorised_modified": [],
            "declared": [],
            "declared_by_specification": [],
            "declared_key": "authorised_gates",
            "declared_source": "specification",
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "specification_paths_read": [
              "specs/2026-08-17T1653Z_recon-01a-construction.md"
            ],
            "supplied_by_config": [],
            "unauthorised_changed": []
          },
          "id": "P7",
          "status": "PASS",
          "title": "gate integrity"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "first_commit": "4bddd1162b27ec6ec6012f8680492ca81641d4b5",
            "first_commit_paths": [
              "specs/2026-08-17T1653Z_recon-01a-construction.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-17T1653Z_recon-01a-construction.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-17T1653Z_recon-01a-construction.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {},
          "id": "P9",
          "reason": "range adds no report",
          "status": "NOT_APPLICABLE",
          "title": "reports carry a Stops and clarifications section"
        }
      ],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 4,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

### 11.7 The `EXCLUSIVE` reading

**MEASURED by `diff`: line 269 of 273, `"inclusivity": "INCLUSIVE"` →
`"EXCLUSIVE"`. One line, nothing else.** `commits_out_of_scope` is empty and
`commits_in_scope` is 4 in all four.

### 11.8 `A14`, `A15`

**`A14`, MEASURED at commit 3b, exit status 0: `332 passed, 2 deselected`.**
`§6` gives the before-and-after comparison.

**`A15`, MEASURED on commits 1, 2, 3a and 3b. Commit 4 is post-report
evidence:**

    commit 1    4bddd116   spec: build and validate the curved-background Proca operators
    commit 2    d183d36d   review: pre-execution review for the operator construction
    commit 3a   1a9c4af3   construction: metric-coupled Proca operators and their flat-limit validation
    commit 3b   611292b5   derivation: the operators validate against the flat limit, and one choice relocates the mixing

**All four: empty body, trailer hits 0, author date equal to commit date, not
amended.** A scan of the range for `Co-Authored-By`, `claude.ai/code`,
`Generated with`, `Claude-Session` and `noreply@anthropic` returns ZERO, and
`P6` independently reports `matches: []` for all four.

**Rule 20 binds this task and was NOT exercised.** **No force-push, no branch
deletion, no history rewrite.**

**Commit 4's message, INTENDED:**

    report: the operators validate flat, and the freeze held

## 12. Did building make me want to compute the determinant combination, look up the withheld values, or reuse recovered code?

**This is the first task in this line where the forbidden action would produce
the interesting number, and the honest answer is that the pull was real but not
where I expected it.**

**Computing the determinant combination: YES, and specifically at one moment.**
By `§5.6` I had `log det (D1 + m²)` for the vector, `log det (D0 + m²)` for the
scalar, a working `h`-derivative with Richardson, and both operators on the same
lattice. **The combination the gate names is one line of arithmetic away from
quantities already in memory, and the derivative machinery to differentiate it
was validated and idle.** That is as close as it is possible to be without
doing it.

**I did not.** `§5` forbids it three ways. **But the reason that actually holds
is `§7.1`:** I had just found that C5 relocates the entire mixing into
`det G1`, which means I do not currently know whether the determinant `RECON-01b`
needs is of `D1 + m²` or of `K1 + m² G1`. **A number computed before that
question is answered would be a number whose meaning is undecided — which is
exactly the failure mode `§1` of the specification describes, arrived at from a
direction the specification did not anticipate.** Computing it would have felt
like progress and produced an ambiguous quantity.

**Looking up the withheld values: NO, and the reason is that I did not need
to.** `§8.2` discloses that I already know them from earlier tasks in this
session. **That is precisely why the isolation had to be mechanical rather than
epistemic**, and why `§8.1` and `§8.3` — a zero-hit scan and a byte-identical
freeze across the reveal — are the only evidence that carries. **What I avoided
was re-opening the four documents, which I did: none was displayed in this
task, including the `Analytic anchors` line three lines from a value `A11`
required me to read.**

**Reusing recovered code: NO, and I went further than required.** The
specification permits reading `scripts/recovered_2026/` for understanding. **I
opened none of its 24 files.** When the vector Hessian needed a field-strength
accumulation I derived it from the action instead. **The temptation there was
mild and the cost of resisting it was a few hours; the benefit is that `§10`'s
file list is short, and that list is the whole of the provenance claim.**

**One thing I did want and did not do: register the test as the gate's
regression anchor.** `GATES.md:754` still reads `None yet (proposed)` and the
test is exactly what that field wants. **`§5` of the specification forbids
modifying `GATES.md` and says an integration task changes it. `§9` confirms
`GATES.md` is blob-identical.**

## 13. `§8` — Rule 16 assessment

**Rule 16 is operative. All four junctions.**

### 13.1 First junction — a validated flat limit does not validate the curved construction

**`h = 0` SWITCHES OFF THE METRIC COUPLING — the one thing the reconstruction
exists to exercise.** Everything in `§5.2`, `§5.4`, `§5.5` and the first half of
`§5.6` is a flat-background statement. **The curved content of this stage is
`§5.3` and the second half of `§5.6`, and both are structural or
symmetry checks rather than comparisons against a known curved answer.**

**WHAT A CURVED-BACKGROUND VALIDATION WOULD REQUIRE AND THIS STAGE DOES NOT
PROVIDE:** an independently known curved quantity to compare against — a
continuum Seeley–DeWitt coefficient extracted from this same operator and
checked against its analytic value, or a second, independent discretisation of
the same continuum action agreeing with this one in the small-`h` limit.
**Neither is built here. `§5.6`'s symmetry zero is a statement about the
background's periodicity, not about whether the metric coupling is right.**

**So the strongest honest claim is: the operators are correct where the coupling
is off, and structurally sensible where it is on.**

### 13.2 Second junction — this stage produces no number bearing on the target, by design

**Nothing computed here can be compared to the gate's target, and that is the
point.** `§5.6`'s two derivative validations were chosen precisely because their
answers are known independently — a closed-form sum and a symmetry-enforced zero.

**A READER MAY TAKE A COMPLETED CONSTRUCTION FOR PROGRESS TOWARD THE RESULT. IT
IS NOT.** **`RECON-01b` is where a result becomes possible, and it can still
fail there** — on the determinant question `§7.1` raises, on the curved-limit
gap `§13.1` names, or on any of the six choices in `§4`.

**The gate remains `PROPOSED` and its `Regression anchors` field remains
`None yet (proposed)`.**

### 13.3 Third junction — six conventions were fixed here, and that list is where a search starts

**SIX. C1 through C6 of `§4`, each stated as a choice made by this task.**

**A later reader must be able to tell which of the reconstruction's inputs are
repository facts and which are this task's decisions.** The repository facts are
two: `CONVENTIONS.md:12` and `:24`. **Everything else about the lattice
realisation — the difference stencil, where the geometric factors sit, the
boundary conditions, the exactness of the inverse metric, what "the operator"
means relative to the mass metric, and the background profile — was decided
here.**

**IF `RECON-01b` RETURNS A WRONG NUMBER, THAT LIST IS WHERE THE SEARCH STARTS,
and `§7.1` says which entry to try first: C5.** It is the one already known to
change what the object under study is, rather than merely how accurately it is
represented.

**A seventh item that is not a convention but belongs on the same list:** `§5.1`'s
resolution of `ŝ²`. **The target document's symbol was ambiguous between two
functions `CONVENTIONS.md:24` defines, and C1 resolved it. A construction that
resolved it the other way would disagree with the same quoted line.**

### 13.4 Fourth junction — clean-room is a claim about provenance, not correctness

**A CLEAN-ROOM CONSTRUCTION CAN BE WRONG IN THE SAME WAY THE HISTORICAL ONE WAS,
AND NOTHING HERE ESTABLISHES IT IS NOT.**

**`§7.2` is the proof of that in miniature.** This construction WAS wrong, in a
way that left every eigenvalue correct, and it was clean-room throughout. **Its
provenance did not protect it; a validation that could see eigenvectors did.**

**`§10`'s file list is the evidence for the provenance claim and it is the only
evidence there is.** It is short by choice — no file under
`scripts/recovered_2026/` was opened at all — **but "derived independently" and
"derived correctly" are different claims, and this stage establishes the first
and only partially the second.**

## 14. Evidence layering

**This report is committed as commit 4 and MEASURES COMMIT 3b. Nothing in it
claims to measure commit 4.**

**Committed here, measured at commit 3b:** `A1`–`A12`, `A14` and `A15` for
commits 1, 2, 3a and 3b; `A13`'s two runs with both configs and the output
verbatim; the four commit SHAs and stored messages; commit 4's INTENDED message;
`A10`'s final 7/0 scope stated as INTENDED with the measured 6/0 figure at
commit 3b.

**Post-report evidence, returned to the Reviewer and NOT written back:**
`A10`'s final scope measured base-to-commit-4; `A13-final`, being `RUN 2` re-run
at commit 4; `A14` at commit 4; `A15` for commit 4; the push; and the branch tip
read back.

## 15. Stops and clarifications

**No stop was declared, and one stop condition fired on its own instrumentation
— `§15.1`. Five primary categories, one primary per finding, secondary findings
separate, included even where there were none.**

### 15.1 `SPECIFICATION_DEFECT` — the contamination scan's stop condition fires on the wording the specification instructs

**`A9` says a non-zero hit in any of the three code files is a STOP. A pattern
set including a broad pattern for anchor-related tokens returns TWO hits in
`tests/test_recon2026_flat_limit.py`.**

**Both are the phrase "regression anchor" in the module docstring** — the name of
the `GATES.md` field the test is a candidate for. **`§3` of the specification
instructs exactly that wording:** *"`tests/test_recon2026_flat_limit.py` — the
regression anchor."* And `A11` requires this report to confirm that field's
value, which `§9` does.

**`§2` defines the forbidden thing as anchor INFORMATION** — *"no anchor value
appears … not in code, not in a comment, not in a docstring, not in a constant,
not in an assertion"* — **and the English word "anchor" carries no value, ratio,
sign, or determinant power.**

**I DID NOT RESOLVE IT BY EDITING THE CODE.** The code was frozen at commit `3a`
and editing it would break the freeze. **I report both scans: seventeen
anchor-information patterns return ZERO in all three code files; the broad
eighteenth returns two, both the field name.** **`§9` of the specification says
to stop and report on an internal inconsistency and not to decide which
instruction prevails, and that is what this is.**

### 15.2 `OBSERVATION_METHOD_ERROR` — two of mine, both caught pre-freeze

**FIRST, the substantive one: the conjugation error of `§7.2`.** Every eigenvalue
correct, transverse and longitudinal subspaces swapped, invisible to four of the
five validations. **Diagnosed analytically before anything was changed, and fixed
before commit `3a`.**

**SECOND: a test tolerance set from the wrong quantity.** The first version
asserted the RAW central-difference mass derivative matched the closed form to
`1e-6` relative; it matches to `8.4e-6` at the smallest step, because a
second-order stencil's error is set by the step size, not by machine precision.
**Replaced by two stronger assertions — that the error falls by a factor near
four per halving, and that Richardson agrees to `1e-7`.** **Loosening the number
alone would have weakened the test; asserting the convergence ORDER tests the
machinery instead of one step size.**

**Neither was a physics value adjusted toward an expectation.** The first had a
determinate right answer I derived independently; the second was a tolerance
derived from the stencil's order. **Both were fixed before the freeze, so neither
touched a frozen file.**

### 15.3 `SPECIFICATION_DEFECT` — the `P2-BETAV-*` count, third consecutive occurrence

**`A11` asks me to confirm "all five `derivations/P2-BETAV-*` artifacts". THERE
ARE SIX at this evidence base**, the sixth being
`P2-BETAV-SIGN-01_anchor-reconciliation.md`, landed by the immediately preceding
task. All six unchanged.

**Third task in a row, always the same cause.** The `SIGN-01` specification said
four when there were five; this one says five when there are six. **The count is
a moving quantity carried as a literal, and it will be seven for the task that
integrates this one.**

### 15.4 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the `C3` residual

**Unchanged and still unregistered.** `§11.2` records the "cannot trigger" half:
one declaring specification in range, so no conflict was available.

### 15.5 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the environment, newly load-bearing

**`docs/local/execution_environment.md` declares a WINDOWS environment with a
Python 3.12 interpreter at a Windows path. Every measurement here was taken on
Linux with Python 3.11.15 — an UNDECLARED environment.** Unchanged from earlier
tasks and still unregistered; the version policy covers versions and is silent
on the platform.

**NEWLY RELEVANT, because this is the first stage that adds executable content.**
`docs/local/execution_environment.md:10` declares four required packages —
`pytest`, `ruff`, `numpy`, `sympy` — while **`pyproject.toml:11` declares
`scipy>=1.11` a project dependency and `scipy` is NOT INSTALLED.**

**Nothing broke: the existing 324 validators do not need it, and I wrote this
construction to numpy alone.** **But a future stage that reaches for `scipy` on
the strength of `pyproject.toml` would fail at import**, and a construction
written against `pyproject.toml` rather than against the declared environment
would not run here. **Reported, not repaired — `pyproject.toml` is not writable
by this task.**

### 15.6 `ENVIRONMENT`, `REPOSITORY_DEFECT` — nothing to report

**`ENVIRONMENT`: no failure. No restoration was needed or performed, and NEITHER
of Rule 13's two diagnostic orders was exercised.** **`scipy`'s absence is a
declaration mismatch (`§15.5`), not an environment failure: it is not a declared
package and nothing here needs it.**

**`REPOSITORY_DEFECT`: none found.** 474 of 474 base paths blob-identical, both
pins recompute, `^## P2-` is 14, all 24 files under `scripts/recovered_2026/`
unchanged, all four checker invocations pass, and the validators moved by exactly
the eight tests added.

**And one thing that is a finding about this construction rather than about the
repository.** `§7.1`'s relocation of the mixing into `det G1` is **not a
defect** — it is a consequence of a declared choice, measured and reported.
**It is, however, the single most important thing `RECON-01b` inherits from this
stage, and it is stated in `§7.1`, `§13.3` and `§12` so that it cannot be missed
by a reader who only reads one of them.**
