# `P2-PHASE-01` exploratory scalar stationary study (`μ = 0`)

## Scope and status

This is an **exploratory** calculation, not a gate result. `P2-PHASE-01`
remains `PROPOSED`; its MICROSCOPIC PARAMETER DOMAIN and PHASE INPUT /
ADMISSIBILITY CONTRACT remain not created / not adopted. No admissibility,
preference, exclusion, or gate verdict is reached here.

The calculation is the declared `μ = 0` slice of a uniform scalar ansatz. It
does not enumerate finite-density stationary solutions and is not a scan over
the eventual `P2-PHASE-01` domain.

## Method

The derivation fixed before numerics is
`derivations/P2-PHASE-01_scalar_stationary_exploratory.md`. With Wilson `r=1`,

```text
D(p; Mhat) = Sum sin^2(p_mu) + [Mhat + Sum(1-cos(p_mu))]^2,
V'_red = Mhat [1/(2G) - I0(Mhat)],
V''_red = 1/(2G) - I0(Mhat) - Mhat I0'(Mhat).
```

The potential was reconstructed with `V_red(0)=0` by numerical integration of
the complete first derivative. Curvature in this report is the analytic
derivative of that complete expression; a finite-difference curvature of the
reconstructed potential is a separate regression check. This is curvature only
along the one-parameter scalar ansatz, **not** the full condensate-space
Hessian. Full multichannel local stability is **NOT ESTABLISHED**.

The Brillouin-zone integral used product-midpoint grids `n=32,40,48`, each at
shifts `0` and `0.25`. The result companion is
`results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json`.

## A1 — frozen anchor

The finest offset estimate is `I0(0)=0.08538273` and `Gc=5.85598486`.
`P2-GAP-01` records `I0(0)=0.0853876831` and `Gc=5.85564548`; the relative
differences are `5.8e-5`, within the stated `1e-4` relative reproduction
tolerance.

| n | shift | I0(0) | Gc | G/Gc at Mhat=1 |
|---:|---:|---:|---:|---:|
| 32 | 0.00 | 0.08532107 | 5.86021696 | 1.768341 |
| 32 | 0.25 | 0.08537317 | 5.85664066 | 1.769421 |
| 40 | 0.00 | 0.08534618 | 5.85849294 | 1.768862 |
| 40 | 0.25 | 0.08537937 | 5.85621547 | 1.769550 |
| 48 | 0.00 | 0.08535974 | 5.85756217 | 1.769143 |
| 48 | 0.25 | 0.08538273 | 5.85598486 | 1.769619 |

Across the full refinement envelope, the stable reported scales are
`I0(0)≈0.0854`, `Gc≈5.86`, and the `Mhat=1` observation `G/Gc≈1.77`.
Additional digits in the companion JSON are finite-grid values, not stable
claims.

## A2–A3 — scalar roots, symmetry, and restricted curvature

`Mhat -> -Mhat` is **not** a symmetry of the frozen Wilson functional. At the
finest straight grid, `I0(-Mhat)/I0(+Mhat)` is `1.12834` at `Mhat=0.1`,
`1.77840` at `0.5`, and `2.98444` at `1.0`.

There is instead an exact Wilson-complement relation
`I0(Mhat)=I0(-8-Mhat)`, induced by `p_mu -> pi-p_mu`; numerical differences
for four checked pairs are at most `1.1e-16`. It relates algebraic roots but is
not an `Mhat -> -Mhat` symmetry. Positive and negative roots are therefore not
declared phase-equivalent.

The table gives the finest-offset roots. `Mhat_left` is the Wilson-complement
partner of `Mhat_right`; `Mhat=0` is always retained from the complete first
derivative. Every root residual is at most `1.85e-5`.

| G/Gc | Mhat_left | Mhat_right | curvature(left) | curvature(right) | curvature(0) |
|---:|---:|---:|---:|---:|---:|
| 0.80 | -7.589264 | -0.410736 | 0.417872 | -0.022615 | 0.021346 |
| 0.90 | -7.813202 | -0.186798 | 0.400036 | -0.009564 | 0.009487 |
| 0.98 | -7.966034 | -0.033966 | 0.404749 | -0.001725 | 0.001743 |
| 0.99 | -7.983246 | -0.016754 | 0.409307 | -0.000861 | 0.000862 |
| 1.00 | -7.999969 | 0.000000 | 0.414969 | 0.000000 | 0.000000 |
| 1.01 | -8.016205 | 0.016205 | 0.419641 | 0.000848 | -0.000845 |
| 1.02 | -8.032013 | 0.032013 | 0.421893 | 0.001681 | -0.001674 |
| 1.05 | -8.077789 | 0.077789 | 0.418361 | 0.004030 | -0.004066 |
| 1.10 | -8.150848 | 0.150848 | 0.401499 | 0.007431 | -0.007762 |
| 1.20 | -8.290070 | 0.290070 | 0.361629 | 0.012652 | -0.014230 |
| 1.40 | -8.552399 | 0.552399 | 0.293296 | 0.018944 | -0.024395 |
| 1.60 | -8.799713 | 0.799713 | 0.243575 | 0.022137 | -0.032019 |
| 1.80 | -9.035065 | 1.035065 | 0.206992 | 0.023713 | -0.037948 |
| 2.00 | -9.260284 | 1.260284 | 0.179248 | 0.024395 | -0.042691 |
| 2.50 | -9.786224 | 1.786224 | 0.132961 | 0.024269 | -0.051230 |
| 3.00 | -10.269318 | 2.269318 | 0.104786 | 0.023156 | -0.056922 |

Thus this restricted scalar functional does not make every algebraic solution a
one-dimensional local minimum: below `Gc`, the near-zero nontrivial root has
negative reduced curvature; above `Gc`, the trivial branch has negative reduced
curvature. These signs do **not** establish phase stability or preference.

At `n=16`, shift `0.25`, and `G/Gc=1.4`, finite-difference curvature of the
reconstructed potential is `0.0189659739`; the independently evaluated full
derivative gives `0.0189659981`, differing by `2.42e-8`.

## A4 — frozen-channel executability

The scalar setup is executable because `derivations/P2-GAP-01_gap_criticality.md`
fixes its normalization, uniform self-energy ansatz, and scalar gap functional.
The Phase-A freeze, `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` §§B–D,
freezes S/P/V/A/T as candidate HS families and explicitly classifies HS scale
and Fierz basis as auxiliary; it does not supply cross-family mean-field
functionals.

| family | result | missing frozen inputs; no computation performed |
|---|---|---|
| S | executable | scalar inputs fixed by `P2-GAP-01` |
| P | not uniquely constructible | HS normalization; quadratic projection/sign; uniform ansatz; common potential zero/measure |
| V | not uniquely constructible | HS normalization; uniform direction/components; internal generator; common potential zero/measure |
| A | not uniquely constructible | HS normalization; uniform direction/components; internal generator; common potential zero/measure |
| T | not uniquely constructible | HS normalization; tensor plane/components; internal generator; common potential zero/measure |

No Fierz projection, HS convention, or comparison normalization was selected.

## A5–A7 — scale observation, onset, and convergence

The `Mhat=1` crossing is observed at `G/Gc=1.7696` on the finest offset grid
and spans `1.7683–1.7696` across all controls. It is an observation only, not a
domain boundary or an admissibility criterion.

For `0.01 <= Mhat <= 0.16`, the finest-grid fit of
`I0(0)-I0(Mhat)` gives exponent `0.9964` and log-RMS residual `0.00552`.
Across all six quadratures its exponent ranges from `0.99496` to `0.99648`.
This finite-grid diagnostic supports a regular approximately linear small-mass
difference; no logarithmically corrected ansatz was motivated or fitted.

Bare fits of the positive branch `Mhat = A(G/Gc-1)^beta` on the finest offset
grid give `beta=0.9744` over `1.01–1.10`, `0.9574` over `1.02–1.20`, and
`0.9427` over `1.05–1.40`. The local effective exponent drifts from `0.9822`
between `1.01` and `1.02` to `0.8321` between `2.5` and `3.0`; the
`G/Gc-1 < 0.01` points are excluded because root/grid resolution dominates.
The central-window exponent ranges only `0.9559–0.9569` across all six
quadratures. This is a finite-window characterization, not a universality-class
claim. Candidate explanations for any continuum mismatch remain discretization,
fit window, logarithmic corrections, finite grid, and the mean-field truncation.

## A8–A10 — exclusions, tests, and provenance

No quarantined `−3.2(5)`, suspended `P2-BETAV-CIRC-01` result, or historical
Finding 5 extraction entered the script, derivation, or result artifact.

`tests/test_p2_phase01_scalar_exploratory.py` covers the zero-mass anchor,
absence of sign reflection (and the Wilson complement relation), every reported
root residual, finite-difference versus analytic curvature, and the
grid-refinement schema. The focused pytest process reached `..... [100%]` but
did not terminate before the known 120-second runner limit. Direct invocation
of all five test functions completed successfully: `5 direct test functions
passed`. Ruff reported `All checks passed!` for the new script and test.

The script hash is
`3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0`.
No pre-existing file, gate status, verdict, digest, hash-pinned artifact,
`GATES.md`, `CONVENTIONS.md`, or `pyproject.toml` was modified.

## What a later domain/admissibility decision must address

This computation exposes several unresolved inputs rather than resolving them:
the Wilson-complement roots and the sign-asymmetric near-zero branch; the
observed lattice-scale crossing; restricted-curvature sign changes; and the
absence of uniquely frozen P/V/A/T mean-field functionals or a full Hessian.
None supplies an admissibility rule by itself.
