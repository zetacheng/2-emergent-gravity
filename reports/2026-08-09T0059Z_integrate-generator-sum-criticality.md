# Execution report — integrate the generator-sum criticality derivation, with a calibration addendum

Authority: `specs/2026-08-09T0059Z_integrate-generator-sum-criticality.md`
Evidence base: `51d4bbe1a2e965b0793b18f4ead5a11dab54c364`
Branch: `gate/p2-integrate-generator-sum-criticality`
Classification: MATERIAL.

**One merge, clean, no conflict. Zero files modified.** Written at the
pre-report head `d0672ca269a5db5189bbd1e88f07841388ae8d73`, before the
push; it contains neither its own commit SHA nor the final branch head.

**The reviewed artifacts were not edited**, `criticality.json`'s verdict
field included. The addendum corrects a consequence; it does not rewrite
a record.

---

## 1. Do I agree the exploratory `G/G_c` positions are unaffected?

**Yes, and the reproduction came out stronger than the specification
anticipated.** Taking the question seriously first, since a
disagreement here was said to be worth more than a clean integration.

**The algebra is exact and I can see no step it misses.** Both gap
equations are `1 = c·G·I_0(M̂)`, differing only in the constant `c`. Then
`G(M̂) = 1/(c·I_0(M̂))` and `G_c = 1/(c·I_0(0))`, so
`G/G_c = I_0(0)/I_0(M̂)` with `c` cancelling identically. Written the way
the root finder actually sees it, at a ratio `r = G/G_c` the coupling is
`G = r/(c·I_0(0))` and the gap equation collapses to
`I_0(M̂) = I_0(0)/r` — an equation in which `c` does not appear at all.
That is not an approximation or a near-cancellation; `c` is absent from
the equation being solved.

**Where I looked for a missed step, and found none.** Three places a
cancellation like this can fail:

1. **If `G_c` were not the same expression at `M̂ = 0`.** It is — both
   the critical coupling and the finite-`M̂` coupling come from the one
   relation `1 = c·G·I_0(M̂)`, so the same `c` sits in both and divides
   out. Had `G_c` been defined by some other condition, the cancellation
   would not be automatic.
2. **If `I_0` differed between the two cases.** It does not: the
   generator-sum derivation changes the overall prefactor and leaves the
   same regulated Wilson `I_0(M̂)`. **This is the load-bearing condition,
   and §4.2 states it explicitly in the addendum** because it is the
   thing a later reader would most plausibly violate.
3. **If the exploratory study had fixed a physical `G`.** It did not —
   it scanned the dimensionless ratio over `G_RATIOS` and solved for
   `M̂` at each. §6 addresses the fixed-`G` statement, which is true and
   about a different quantity.

**I therefore agree**: the `M̂`-versus-`G/G_c` curve, the `M̂ = 1`
crossing, the 282-row branch-depth table indexed by `G/G_c`, and the
parameter-domain draft expressed in `G/G_c` all need no rescaling. The
verdict sentence overstates its consequence, and the addendum withdraws
the extension without touching the factor or the artifact.

**One qualification of my own, which the specification did not ask for
and which strengthens rather than weakens the conclusion.** The
specification expected agreement "to nine decimal places". I observed
**exact** agreement — spread `0.000e+00` at every ratio. But the
exploratory root prescription returns the midpoint of a bracket halved
17 times from `[-4, 4]`, so its output is quantised at
`8/2¹⁷ ≈ 6.1e-05`; identical returned values are consistent with, but do
not by themselves establish, agreement below that quantum. I therefore
re-ran the same bisection to 60 halvings — beyond the prescription, as
corroboration only — and the spread is still exactly zero, now at a
quantum below `1e-17`. **Both runs are reported in the addendum, with
the prescription-conforming one first and the corroboration labelled as
such.**

## 2. A1 — refs, read from the remote

    $ git fetch --prune origin                                exit 0
    $ git ls-remote origin …

    51d4bbe1a2e965b0793b18f4ead5a11dab54c364  refs/heads/main
    84aad96d97bab67f636812939bb00ac917f35273  refs/heads/gate/p2-generator-sum-criticality
    10c260b96882ac12610f78840aeeabd07be2d7cb  refs/heads/review/role-model-and-executors

Remote-tracking refs after the fetch, reported separately:

    refs/remotes/origin/main                               51d4bbe1a2e965b0793b18f4ead5a11dab54c364
    refs/remotes/origin/gate/p2-generator-sum-criticality  84aad96d97bab67f636812939bb00ac917f35273

Local `main`, reported separately and **not repaired**:

    refs/heads/main                                        0f7961747abe2a18b436c0b1e5b928f425ea4d9a

**Every A1 value matched. No STOP.** The merge was performed against
`refs/remotes/origin/gate/p2-generator-sum-criticality` immediately
after the fetch, never against a local ref.

**The dry-run claims, re-derived before merging:**

    merge-base(base, source) = 51d4bbe1a2e965b0793b18f4ead5a11dab54c364   the ORIGINAL base
    source changed paths: 6 additions, 0 modifications
    anything not an addition: NONE

## 3. A2 — merge parentage, as distinct values

**Merge commit** — `d8afb74eb08d59fa0755810c7a9db273e7b4f62f`

    parent 1    d5b46fcf5bfc2bbfa3986032a5f73006791d7175   the integration spec commit (commit 1)
    parent 2    84aad96d97bab67f636812939bb00ac917f35273   the source branch tip
    merge-base  51d4bbe1a2e965b0793b18f4ead5a11dab54c364   the ORIGINAL base

Parent 1 was fixed by the commit being stood on, not selected. `--no-ff`,
exactly two parents, no conflict:

    Merge made by the 'ort' strategy.
     6 files changed, 912 insertions(+)

    $ git status --porcelain=v1
    (empty)

**Every arriving line is an insertion** — `912 insertions(+)`, no
deletions.

## 4. A4 — the invariance demonstration, reproduced

Reproduced independently, not copied from the specification. It uses
exactly the regulated `I_0(M̂)`, cutoff and unit conventions, and root
prescription of `derivations/P2-PHASE-01_scalar_stationary_exploratory.md`
and `scripts/p2_phase01_scalar_exploratory.py`: the `WilsonQuadrature`
product-midpoint integral, the finest grid `n = 48` at the unshifted
`shift = 0.0`, bracketed bisection on `[-4, 4]` with 17 halvings.
**Only the prefactor `c` was changed**, from the implementation's
hardcoded `2` to the value under test.

    grid n=48 shift=0.0   I_0(0) = 0.0853597428025065

    c = 2      original exploratory / control prefactor; also canonical at N = 4
               G_c = 5.857562166709317
    c = 8/3    canonical, N = 3
               G_c = 4.3931716250319885
    c = 4      canonical, N = 2
               G_c = 2.9287810833546586

**The critical couplings differ; the roots at matched `G/G_c` do not:**

       G/G_c              c = 2            c = 8/3              c = 4    max |diff|
        1.05     0.078094482422     0.078094482422     0.078094482422    0.000e+00
         1.2     0.290557861328     0.290557861328     0.290557861328    0.000e+00
         1.4     0.552886962891     0.552886962891     0.552886962891    0.000e+00
       1.769     0.999847412109     0.999847412109     0.999847412109    0.000e+00
         2.0     1.260833740234     1.260833740234     1.260833740234    0.000e+00
         3.0     2.270050048828     2.270050048828     2.270050048828    0.000e+00

    worst spread across all ratios: 0.000e+00

**The `M̂` values agree, so A4's gate is open and the addendum was
written.** Corroboration at 60 halvings, and the `M̂ = 1` crossing at
`G/G_c = 1.769143` for all three prefactors, are in the addendum at §4.

The identity of §2.1 checked directly on the solved roots:

    r = 1.05    I_0(M̂)/I_0(0) = 0.952380952381    1/r = 0.952380952381
    r = 1.2     I_0(M̂)/I_0(0) = 0.833333333333    1/r = 0.833333333333
    r = 1.4     I_0(M̂)/I_0(0) = 0.714285714286    1/r = 0.714285714286
    r = 1.769   I_0(M̂)/I_0(0) = 0.565291124929    1/r = 0.565291124929
    r = 2.0     I_0(M̂)/I_0(0) = 0.500000000000    1/r = 0.500000000000
    r = 3.0     I_0(M̂)/I_0(0) = 0.333333333333    1/r = 0.333333333333

**The demonstration was run in a scratch harness and not committed** —
A5's manifest authorises no script path for it, and adding one would be
a tenth path. Every figure quoted in the addendum was checked back
against the harness output before the addendum was committed.

## 5. A6 — arriving artifacts intact

Blob-compared against the source branch tip `84aad96d…`:

    derivations/P2-GENERATOR-SUM-CRITICALITY_01.md                  47c28e26a26f2c877bf9dc494fb4e1cd5e18bf52   IDENTICAL
    reports/2026-08-08T2350Z_generator-sum-criticality.md           71e15f619dd7a2824f3ada1100398dcde00c5729   IDENTICAL
    results/P2-PHASE-01/generator-sum-criticality/criticality.json  f8c7ca38766f3e8da462be788dc9baf25e35b376   IDENTICAL
    scripts/p2_generator_sum_criticality.py                         3ef2666ba64186320eb03ed966abde79eaeff0bd   IDENTICAL
    specs/2026-08-08T2350Z_generator-sum-criticality.md             a968615bec796ac40769b1dc818b649fd3da22a5   IDENTICAL
    tests/test_p2_generator_sum_criticality.py                      c7fc07f749075f76e53742f9473ccf4475533c18   IDENTICAL

**`criticality.json` is unchanged, verdict field included**, read from
the merged tree:

    …ls 1 only at N=1. The exploratory G/G_c positions carry an N/4 factor.

The sentence the addendum corrects is still there, exactly as reviewed.
**That is the intended outcome**: the record stands and the consequence
is corrected beside it.

## 6. A7 — protected paths

Read from the objects, base vs merged head:

    GATES.md                                                            bd4820513217ae7e1c493328dc49536e69b8cfb8   IDENTICAL
    CONVENTIONS.md                                                      2d4f735c55a14fdfc5d1031a58698a8ca075fbbd   IDENTICAL
    AGENTS.md                                                           5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3   IDENTICAL
    DECISION_LOG.md                                                     345688919786874b8837af150d2ec38976eb6bb2   IDENTICAL
    pyproject.toml                                                      9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4   IDENTICAL
    derivations/P2-GAP-01_gap_criticality.md                            70b43834873aac435aaed24af70201a9a16b79b7   IDENTICAL
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md                   0be773f6a52c759abd23438c66da6b43bca44930   IDENTICAL
    derivations/P2-PHASE-01_scalar_stationary_exploratory.md            76934c049e0c8e0ba019337b735ff77e25ce02bc   IDENTICAL
    derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md       158ab187f2576fd8f163cd3ad3b76b7b897e6fb5   IDENTICAL
    results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json  454e70182e3b5de4765a397c10caba88f894d35f   IDENTICAL

**The exploratory artifacts and the parameter-domain draft are
blob-identical.** The addendum's conclusion is that they need no change,
and the integration demonstrates that none was made — which is the whole
point of putting them on the protected list.

## 7. A8 — no gate changed

    GATES.md base vs merged head                        IDENTICAL (bd482051…)
    '^## P2-' count at base                             14
    '^## P2-' count at merged head                      14

    ## P2-GAP-01 — Gap-equation criticality (continuum + lattice)
    Status: PASS (continuum exact; lattice `I_0` agrees with paper at matched mass)

    ## P2-PHASE-01 — Admissible stable condensed phase (the Ice)
    Status: PROPOSED

**`P2-GAP-01` still reads `PASS` with no caveat added.** No gate, gate
status, verdict, digest or hash-pinned artifact was modified.

## 8. Zero modifications

    $ git diff --name-status 51d4bbe1… HEAD
    A	derivations/P2-GENERATOR-SUM-CRITICALITY_01.md
    A	derivations/P2-GENERATOR-SUM-CRITICALITY_01_addendum.md
    A	reports/2026-08-08T2350Z_generator-sum-criticality.md
    A	results/P2-PHASE-01/generator-sum-criticality/criticality.json
    A	scripts/p2_generator_sum_criticality.py
    A	specs/2026-08-08T2350Z_generator-sum-criticality.md
    A	specs/2026-08-09T0059Z_integrate-generator-sum-criticality.md
    A	tests/test_p2_generator_sum_criticality.py

    additions: 8   modifications: 0
    anything not an addition: NONE

**The base-to-head range contains zero `M` operations and no
pre-existing file was modified.** The eight additions above plus the
report commit give the nine of A5; there is no tenth path.

## 9. A9-pre — eight validators, at head `d0672ca2`

    $ python -m pytest tests/test_repository_structure.py            ->  4 passed              exit 0
    $ python -m pytest tests/test_si1_governance.py                  -> 14 passed              exit 0
    $ python -m pytest tests/test_gate_anchors.py                    -> 18 passed, 2 deselected exit 0
    $ python -m pytest tests/test_governance_tools.py                ->  8 passed              exit 0
    $ python -m pytest tests/test_p2_phase01_scalar_exploratory.py   ->  5 passed              exit 0
    $ python -m pytest tests/test_p2_phase01_fierz_and_depths.py     -> 14 passed              exit 0
    $ python -m pytest tests/test_p2_channel_character.py            -> 23 passed              exit 0
    $ python -m pytest tests/test_p2_generator_sum_criticality.py    ->  7 passed              exit 0

All eight exit 0, captured from `python -m pytest` itself and not from
the tail of a pipeline. **`test_p2_phase01_scalar_exploratory.py` passing
is worth naming separately**: the exploratory results the addendum says
need no rescaling still pass their own tests in the merged tree.

## 10. The addendum, quoted in full

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

## 11. A3 — guards

### 11.1 `PRE_MERGE`, at the spec commit, before the merge

    {
      "checks": [
        {
          "condition": "worktree_clean",
          "entries": [],
          "status": "PASS"
        },
        {
          "attachment": "gate/p2-integrate-generator-sum-criticality",
          "condition": "worktree_matches_declared_target",
          "expected_worktree_head": "d5b46fcf5bfc2bbfa3986032a5f73006791d7175",
          "status": "PASS",
          "worktree_head": "d5b46fcf5bfc2bbfa3986032a5f73006791d7175"
        },
        {
          "actual": "51d4bbe1a2e965b0793b18f4ead5a11dab54c364",
          "condition": "merge_base",
          "expected": "51d4bbe1a2e965b0793b18f4ead5a11dab54c364",
          "status": "PASS"
        },
        {
          "condition": "scope",
          "evidence": {
            "base": "51d4bbe1a2e965b0793b18f4ead5a11dab54c364",
            "failures": [],
            "head": "84aad96d97bab67f636812939bb00ac917f35273",
            "mode": "exact",
            "observed_operations": [
              {"operation": "add", "path": "derivations/P2-GENERATOR-SUM-CRITICALITY_01.md"},
              {"operation": "add", "path": "reports/2026-08-08T2350Z_generator-sum-criticality.md"},
              {"operation": "add", "path": "results/P2-PHASE-01/generator-sum-criticality/criticality.json"},
              {"operation": "add", "path": "scripts/p2_generator_sum_criticality.py"},
              {"operation": "add", "path": "specs/2026-08-08T2350Z_generator-sum-criticality.md"},
              {"operation": "add", "path": "tests/test_p2_generator_sum_criticality.py"}
            ],
            "overall": "PASS",
            "tool": "scope_checker"
          },
          "status": "PASS"
        },
        {
          "condition": "pinned_artifacts",
          "evidence": [
            {"actual": "17b6f613ffefb79fae8c0a5c40e3bd67ad31a101112af615945647e143fade00",
             "expected": "17b6f613ffefb79fae8c0a5c40e3bd67ad31a101112af615945647e143fade00",
             "path": "derivations/P2-GAP-01_gap_criticality.md", "status": "PASS"},
            {"actual": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
             "expected": "fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a",
             "path": "derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md", "status": "PASS"},
            {"actual": "5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9",
             "expected": "5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9",
             "path": "results/P2-CHANNEL-FREEZE/fierz_matrix.json", "status": "PASS"}
          ],
          "status": "PASS"
        }
      ],
      "mode": "PRE_MERGE",
      "overall": "PASS",
      "tool": "merge_guard"
    }
    === exit 0 ===

`derivations/P2-GAP-01_gap_criticality.md` is pinned in the guard as well
as protected in A7 — the gate whose `PASS` this derivation must not
disturb had to be verifiably still underneath the merge, and it was.

### 11.2 The final `POST_MERGE` — intended parameters

**The two roles are representable separately, so no stop arose.**
`merge_guard.post_merge` takes `merge_commit` and `expected_remote_sha`
as independent config keys.

    mode                  POST_MERGE
    merge_commit          d8afb74eb08d59fa0755810c7a9db273e7b4f62f   <- the MERGE OBJECT
    expected_parent_1     d5b46fcf5bfc2bbfa3986032a5f73006791d7175
    expected_parent_2     84aad96d97bab67f636812939bb00ac917f35273
    expected_merge_base   51d4bbe1a2e965b0793b18f4ead5a11dab54c364
    remote_check_policy   REQUIRED
    expected_remote_ref   refs/remotes/origin/main
    expected_remote_sha   <the final REPORT-commit head>              <- a DIFFERENT SHA
    scope_manifest        the A5 manifest below, head = final head
    pinned_artifacts      the same three as the PRE_MERGE guard

`merge_commit` is the merge object; `expected_remote_sha` is the report
commit that will be `main`'s tip. Different commits, different keys. The
executed guard is post-report evidence.

**Note the layering here.** The merge commit is `d8afb74e`, but the
addendum lands in commit 3 *after* it, so the merge object is two
commits below the final head rather than one. The guard's two SHAs are
correspondingly further apart than in a merge-then-report integration,
which is exactly why they must be supplied separately.

## 12. A5 — scope manifest

`{PUSHED_HEAD}` placeholder so the digest does not depend on the report
commit. SHA-256:
`b4cc75252dd2f8444494ea476c9d414a2a85527bb4b4f7c5d3895cbe942be1de`.

    {
      "base": "51d4bbe1a2e965b0793b18f4ead5a11dab54c364",
      "head": "{PUSHED_HEAD}",
      "mode": "exact",
      "required": [
        {"operation": "add", "path": "derivations/P2-GENERATOR-SUM-CRITICALITY_01.md"},
        {"operation": "add", "path": "derivations/P2-GENERATOR-SUM-CRITICALITY_01_addendum.md"},
        {"operation": "add", "path": "reports/2026-08-08T2350Z_generator-sum-criticality.md"},
        {"operation": "add", "path": "reports/2026-08-09T0059Z_integrate-generator-sum-criticality.md"},
        {"operation": "add", "path": "results/P2-PHASE-01/generator-sum-criticality/criticality.json"},
        {"operation": "add", "path": "scripts/p2_generator_sum_criticality.py"},
        {"operation": "add", "path": "specs/2026-08-08T2350Z_generator-sum-criticality.md"},
        {"operation": "add", "path": "specs/2026-08-09T0059Z_integrate-generator-sum-criticality.md"},
        {"operation": "add", "path": "tests/test_p2_generator_sum_criticality.py"}
      ],
      "optional": [],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

**9 additions and 0 modifications**, matching A5, with `modify` empty so
the scope checker enforces the additive-only property rather than the
report merely observing it. The `{HHMM}` token resolved to `0059` at
commit 1 and is reused. **There is no tenth path.**

## 13. Worktree states, stated separately

**The merge worktree** — `…/scratchpad/integ6`, attached to
`gate/p2-integrate-generator-sum-criticality`, at
`d0672ca269a5db5189bbd1e88f07841388ae8d73`.
`git status --porcelain=v1` empty after the merge and after the addendum
commit. All merging, the A4 reproduction and all checks in this report
were performed here.

**The main worktree** — `/home/user/2-emergent-gravity`, attached to
`gate/p2-grassmann-crossing-sign` at `cf4c789`. **It was not touched by
this task** beyond read-only `fetch`, `ls-remote` and reading
`scripts/p2_phase01_scalar_exploratory.py` for the A4 reproduction; it
reported 0 dirty entries before the work began and its attachment is
unchanged. Local `main` was not checked out, fast-forwarded or repaired.

**Ten other registered worktrees**, none altered, cleaned or stashed,
all reporting 0 dirty entries at the start of this task: `chan`,
`expmap`, `fixA`, `fixB`, `fixC`, `integ`, `integ2`, `integ3`, `integ4`,
`integ5`, `norm`.

## 14. Stops and clarifications

**Stops: none.** No A1 ref mismatched, the merge did not conflict, the
guard did not return `FAIL`, the manifest allows no modification and
none occurred, A4's `M̂` values agreed so the addendum gate opened, and
the `POST_MERGE` guard proved able to carry the merge object and the
remote head as distinct values.

**Findings: none of my own in this task.** No tool-invocation error, no
observation-method error, no repository defect surfaced during the
integration.

**Finding 1 — secondary, and it strengthens rather than weakens.** The
specification expected the `M̂` values to agree "to nine decimal places";
they agree exactly. §1 explains why I did not simply report the stronger
number: the exploratory root prescription quantises its output at
`≈ 6.1e-05`, so exact agreement of returned values is weaker evidence
than it looks. The 60-halving corroboration removes that doubt, and both
runs are in the addendum.

**Finding 2 — secondary, an observation about the artifact.** Both
correction-factor field names in `criticality.json` are accurate, as the
specification says: `generator_sum_symbolic.exploratory_correction_factor_symbolic`
is `"N/4"`, and `per_N[*].exploratory_correction_factor_vs_half_I0` is
`1/2, 3/4, 1` for `N = 2, 3, 4` — exactly `N/4`, reaching `1` at `N = 4`
where the canonical prefactor `8/N` equals the original `2`. **The
specification named only the second field; both exist and both are
right.** The addendum names both, so a reader is not left looking for one
of them.

**Clarification 1 — the A4 harness was not committed.** A5's manifest
authorises no script path for the reproduction, and adding one would be a
tenth path and a defect. The harness ran in scratch; every figure quoted
in the addendum was checked back against its output before the addendum
was committed, and §4 of this report carries the same figures.

**Clarification 2 — where commit 1 sits in §2's sequence.** §2 lists
eight steps and does not name the specification commit; §4 requires it as
commit 1 and A2 requires it to be parent 1. I took it as part of step 1.
**Fourth integration running with the same gap**; see §15(b).

**Clarification 3 — which ref was merged.** §5 requires merging the
pinned remote ref rather than a local copy. I merged
`refs/remotes/origin/gate/p2-generator-sum-criticality` immediately after
`git fetch --prune`, having confirmed it equals both its `git ls-remote`
value and its pinned SHA.

## 15. Anything ambiguous, unsatisfiable, or that I would have specified differently

**Nothing was unsatisfiable.** A1–A11 were met as written, and every
dry-run claim held on independent re-derivation.

**(a) §2's instruction on what a numerical disagreement would mean is
the best-drafted sentence in this specification, and I would propagate
it.** It says a disagreement "is evidence that the stated invariance
conditions have not been reproduced. It does not by itself overturn the
algebraic cancellation" — and explicitly names the error class of
converting a failure-to-reproduce into a substantive negative result.
That distinction has now produced findings four times in this programme.
**It belongs in `CONVENTIONS.md`, not in individual specifications**, and
this is the second time I have said so.

**(b) §2's step list and §4's commit order should be one list.**
Clarification 2. Fourth integration, unchanged. Here the interleaving is
slightly harder than before because commit 3 is the addendum, which sits
*between* the merge and the report and appears only in §4 — so §2's step
5 ("commit the integration report") silently presupposes a step §2 never
lists.

**(c) A4 gates the addendum but the manifest gives the gate no home.**
The reproduction is the evidence for the addendum's central claim, and
it is required to be performed, yet no manifest path exists for the code
that performs it. I put the figures in the addendum and the report,
which is the best available, but **a later executor cannot re-run my
harness** — they would have to rewrite it from the addendum's prose
description. Authorising a scratch-script path, or naming the
reproduction as a test under `tests/`, would make the claim
independently re-checkable rather than merely re-derivable.

One thing I would keep exactly as written: **the instruction to correct
the consequence by addendum and leave `criticality.json` untouched.**
The alternative — editing the verdict string — would have been quicker
and would have destroyed the record of what was concluded and when. The
verdict sentence and its correction now sit side by side on `main`,
which is what a reader six months from now actually needs.

## 16. Commits, and commit-message hygiene

Commits 1–3, at the pre-report head. The report commit's SHA is
necessarily absent from the report it commits.

**Commit 1** — `d5b46fcf5bfc2bbfa3986032a5f73006791d7175`

    spec: integrate the generator-sum criticality derivation with an addendum

    Records the PI integration authorization, evidence base
    51d4bbe1a2e965b0793b18f4ead5a11dab54c364, transcribed verbatim.

    One merge: six additions, zero modifications, merge-base the original
    base. The derivation's substance is accepted -- the singlet control
    reproduces P2-GAP-01 and the generator sum gives G_c = N/(8 I0).

    The specification adds one addendum because a sentence in the reviewed
    artifacts overstates a consequence. Both gap equations have the form
    1 = c G I0(Mhat), so G/G_c = I0(0)/I0(Mhat) and the prefactor cancels:
    the exploratory G/G_c positions do not carry an N/4 factor. The
    addendum must also carry the condition under which that invariance
    holds, and must correct a second statement that treated an unanalysed
    symmetry-breaking ansatz as unsupported by the theory.

    The reviewed artifacts are not edited. The addendum corrects a
    consequence rather than rewriting a record.

**Commit 2 (the merge)** — `d8afb74eb08d59fa0755810c7a9db273e7b4f62f`

    merge: integrate the generator-sum criticality derivation (reviewed; pinned 84aad96)

    Integrates gate/p2-generator-sum-criticality at
    84aad96d97bab67f636812939bb00ac917f35273 into the integration branch.

    Six additions, all reviewed and all additive: the task specification,
    the derivation note, the script, the results artifact, a new test file,
    and the execution report.

    The singlet-only control reproduces P2-GAP-01 -- 1 = 8 G_N I0 with
    channel coupling G = 4 G_N, prefactor 2, G_c = 1/(2 I0). The full U(N)
    generator sum gives 1 = (8/N) G I0 and G_c = N/(8 I0). The ratio of
    coefficients is N, equal to 1 only at N = 1, which is the correct
    degeneration since the generator sum collapses to the singlet
    interaction there.

    P2-GAP-01's PASS stands for the form it computed, and its gate entry and
    derivation are untouched by this merge.

    One consequence drawn in the results artifact's verdict field is
    corrected by a separate addendum landing alongside this merge. The
    artifact itself is integrated exactly as reviewed, verdict included.

**Commit 3 (the addendum)** — `d0672ca269a5db5189bbd1e88f07841388ae8d73`

    derivation: addendum correcting the calibration consequence and ansatz scope

    Corrects two consequences drawn in artifacts that are already committed.
    No committed artifact is altered: criticality.json, the derivation note
    and the execution report are preserved exactly as reviewed.

    The verdict field concludes that the exploratory G/G_c positions carry
    an N/4 factor. They do not. Both gap equations have the form
    1 = c G I0(Mhat), so G(Mhat) = 1/(c I0(Mhat)) and G_c = 1/(c I0(0)),
    whence G/G_c = I0(0)/I0(Mhat) with c cancelling identically. The
    exploratory study scanned that dimensionless ratio, so its positions are
    untouched. The addendum carries the condition: the cancellation holds
    because only the overall prefactor changed and I0(Mhat) is the same
    regulated function, and it would not follow from a change altering the
    Mhat-dependence.

    The numerical check was reproduced independently using the exploratory
    WilsonQuadrature, grid and bisection prescription with only c varied.
    The Mhat values at c = 2, 8/3 and 4 are identical, spread exactly zero,
    and Mhat = 1 sits at G/G_c = 1.769143 in all three.

    The addendum also corrects a statement that treated an adjoint
    condensate as unsupported by the theory because it would break the U(N)
    symmetry. A symmetric action admits symmetry-breaking saddles; the
    accurate statement is that adjoint condensates were not analysed under
    the symmetric ansatz adopted. Out of scope is not non-existence.

**Intended report commit message** (commit 4):

    docs: report the integration of the generator-sum criticality derivation

    Records A1-A4, A6-A8, A9-pre and A10 for the single merge and the
    addendum, with the merge commit's parents and merge-base as distinct
    values, the PRE_MERGE guard result, and the intended final manifest
    and POST_MERGE parameters.

    The invariance demonstration was reproduced with the exploratory
    quadrature, grid and root prescription, varying only the prefactor:
    the Mhat values at c = 2, 8/3 and 4 are identical at both 17 and 60
    bisection halvings, and Mhat = 1 sits at G/G_c = 1.769143 in all
    three. The report states agreement with the conclusion and names the
    three places a cancellation of this kind could have failed.

    The base-to-head range contains zero M operations. The exploratory
    artifacts and the parameter-domain draft are blob-identical,
    criticality.json arrived unchanged with its verdict field intact,
    GATES.md is unchanged at 14 P2 gates, and P2-GAP-01 still reads PASS
    with no caveat.

### Trailer suppression, per commit

The harness convention in this environment appends `Co-Authored-By:` and
`Claude-Session:` trailers to commit messages. This specification permits
neither. Both were **actively suppressed** on every commit of this
branch — **including the merge commit** — by composing each message in a
file and passing it with `-F`, never `-m`.

    commit 1  d5b46fcf   spec       suppressed: Co-Authored-By, Claude-Session
    commit 2  d8afb74e   MERGE      suppressed: Co-Authored-By, Claude-Session
    commit 3  d0672ca2   addendum   suppressed: Co-Authored-By, Claude-Session
    commit 4  (report)              suppression applied identically; stored
                                    message read back as post-report evidence

Each proposed message was inspected before committing and each stored
message read back with `git log -1 --format=%B` after; a `grep` for
`co-authored-by`, `claude-session`, `claude.ai`, `generated with` and
`noreply@anthropic` returned no match on either form, for all three
commits. **No trailer appeared despite inspection, so A10's pre-push STOP
did not trigger.**

**Suppression is a fact disclosed here, not an absence.** The merge
commit in particular — where a generated message would ordinarily be
accepted with `--no-edit` — was given an authored message by file for
exactly this reason.

Author and committer identity (`Claude <noreply@anthropic.com>`) and the
SSH signature from the global `commit.gpgsign=true` are commit-object
headers, not message content, and are outside this specification's scope.
