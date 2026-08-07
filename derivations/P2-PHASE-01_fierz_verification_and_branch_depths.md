# Derivation note — `P2-PHASE-01`: Fierz-matrix verification and stationary-branch depths

**Kind:** two derivations. Neither decides anything. This note fixes the
analytic content of both **before any numerical or symbolic output is
produced**, so that the algebra is reviewable before the results can
influence it.

**`P2-PHASE-01` remains `PROPOSED` and not runnable.** Nothing here
registers a gate, changes a status, adopts a prerequisite draft, or
reaches an admissibility verdict.

Authority: `specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md`.

---

## 0. Governing conventions, fixed before any computation

All of (a) is carried out under the Phase-A freeze conventions, quoted
from `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` (SHA-256
`fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a`):

    metric_signature:            (1, 1, 1, 1)
    gamma5_definition:           gamma(0)*gamma(1)*gamma(2)*gamma(3)
    sigma_definition:            I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2
    dirac_trace_normalization:   trace(Id4) = 4
    un_generator_normalization:  trace(lam(A)*lam(B)) = 2*KroneckerDelta(A,B)
    grassmann_crossing_sign:     -1
    singlet_traceless_order:     [singlet, traceless]
    compound_index_order:        [dirac_family, internal_family, component]
    basis_order:                 [S, P, V, A, T]

None of these is chosen here. `gamma5` means
`gamma(0)*gamma(1)*gamma(2)*gamma(3)` throughout, per the PI ruling of
2026-08-07 recorded in §8 of the authority specification. That ruling
resolves a disagreement between the freeze and the
`vocabulary.gamma5` entry of `derivations/CANONICAL_INTERACTION.json`;
the latter is not authoritative here and is not modified by this work.

### 0.1 The λ-algebra determination (settled, not open)

The frozen `un_generator_normalization` is sufficient to fix the
internal-index rearrangement uniquely, so derivation (a) is executable.
The reasoning, recorded before any code was written:

The generators `lam(A)`, `A = 0 … N²−1`, span the full space of `N×N`
complex matrices — the index set includes the singlet
`lam(0) = sqrt(2/N)·Id_N`, as stated in the canonical interaction. With
the declared normalisation `trace(lam(A) lam(B)) = 2 δ_AB`, the
completeness relation on that space is fixed with no residual freedom:

    Sum_A (lam(A))_{ij} (lam(A))_{kl} = 2 δ_{il} δ_{kj}

This is the standard consequence of completeness plus the stated trace
normalisation: expanding an arbitrary `M` as
`M = (1/2) Sum_A trace(lam(A) M) lam(A)` and reading off the kernel. The
factor 2 is set by the declared normalisation and by nothing else. **No
internal-index convention is invented here**; the relation is derived
from the frozen normalisation and is verified numerically for several
`N` in the accompanying script.

### 0.2 The sixteen-element Dirac basis

The five families and their component counts are frozen as
`S=Id4 (1)`, `P=gamma5 (1)`, `V=gamma(mu) (4)`,
`A=I*gamma(mu)*gamma5 (4)`, `T=I*(gamma(mu)gamma(nu)-gamma(nu)gamma(mu))/2
(6)`, total sixteen. Under the declared Euclidean signature every basis
element is Hermitian and squares to `Id4`; consequently

    trace(Gamma^a_i Gamma^b_j) = 4 δ^{ab} δ_{ij}

so the proportionality constant in the orthogonality relation is **4 for
every family**, and the expansion of an arbitrary `4×4` matrix is
`M = (1/4) Sum_A trace(Gamma^A M) Gamma^A`. Completeness, Hermiticity,
the square-to-identity property and the trace normalisation are all
verified explicitly rather than assumed (Deliverable 5).

---

## 1. Derivation (a) — the Fierz exchange matrix

### 1.1 The exchange map

The canonical interaction is a product of two bilinears built from the
same four fermion fields. Label the legs so that the interaction term is

    (psibar_1 lam(A) Gamma^a_i psi_2) (psibar_3 lam(A) Gamma^a_i psi_4)

with `1 = 3` and `2 = 4` for the physical operator. **The exchange is of
the two `psi` legs, `psi_2 <-> psi_4`**; the two `psibar` legs are left
in place. **Dirac and internal indices are exchanged jointly**, because
it is the field operators that are permuted and each field carries both
indices; there is no independent internal-only exchange.

Writing the reference ordering as `psibar_1 psi_2 psibar_3 psi_4` and
the exchanged ordering as `psibar_1 psi_4 psibar_3 psi_2`, restoring the
reference ordering requires an odd permutation of anticommuting fields.
**That is where `grassmann_crossing_sign = -1` enters** — as a single
overall factor multiplying the whole rearrangement, not per family and
not per component.

`compound_index_order = [dirac_family, internal_family, component]`
fixes how a compound basis label is read: the outermost label is the
Dirac family `a ∈ {S,P,V,A,T}`, then the internal family label `A`, then
the component index running within the Dirac family
(`mu = 0..3` for V and A, `0 <= mu < nu <= 3` for T, single for S and
P). The compound basis element is the tensor product
`lam(A) ⊗ Gamma^a_i` acting on the joint (internal, Dirac) index pair.

### 1.2 The kernel identity to be demonstrated

Purely in Dirac space, the rearrangement asserts

    Sum_i (Gamma^a_i)_{alpha beta} (Gamma^a_i)_{gamma delta}
        = Sum_b M_{ab} Sum_j (Gamma^b_j)_{alpha delta} (Gamma^b_j)_{gamma beta}

Projecting both sides with `(Gamma^c_k)_{delta alpha} (Gamma^c_k)_{beta
gamma}` and using `trace(Gamma^A Gamma^B) = 4 δ^{AB}` gives the closed
formula, for any fixed component `k` of family `c`:

    M_{ac} = (1/16) Sum_i trace(Gamma^a_i Gamma^c_k Gamma^a_i Gamma^c_k)

The Fierz matrix including the crossing sign is

    F = grassmann_crossing_sign * M = -M

**This kernel identity is demonstrated as a tensor equation on all
`4^4 = 256` index combinations**, not asserted from the projection
formula, and independently of `k` (the formula's `k`-independence is
itself checked).

### 1.3 The internal factor and the singlet/traceless split

The frozen 5×5 matrix is a **Dirac-family** matrix and does not by
itself resolve the internal decomposition. The split is derived here
from the declared generator normalisation, per §0.1:

    Sum_A (lam(A))_{ab} (lam(A))_{cd} = 2 δ_{ad} δ_{cb}

After the leg exchange, the internal structure of each exchanged
bilinear is therefore `Id_N`, with an overall factor 2. Re-expressing
`Id_N` in the generator basis uses only the frozen singlet definition
`lam(0) = sqrt(2/N)·Id_N`, i.e. `Id_N = sqrt(N/2)·lam(0)`, so

    2 · (psibar Id_N Gamma^b psi)(psibar Id_N Gamma^b psi)
        = 2 · (N/2) · (psibar lam(0) Gamma^b psi)(psibar lam(0) Gamma^b psi)
        = N · (psibar lam(0) Gamma^b psi)^2

**The induced internal structure is therefore purely singlet, and the
traceless (`A >= 1`) induced coefficient is exactly zero** — a result,
not an omission. This step uses only the frozen normalisation and the
frozen singlet definition; **no internal-index convention is invented.**

### 1.4 The mandatory basis conversion

The canonical interaction writes its pseudoscalar bilinear with
`I*gamma5`, whereas the frozen Fierz family basis defines `P` as
`gamma5`. At the level of the squared bilinear this is a sign:

    (bilinear(lam(A), I*gamma5))**2 = -(bilinear(lam(A), gamma5))**2

so the canonical coefficient vector, expressed in the canonical
operators, is

    v_canonical = (G/(2N), G/(2N), 0, 0, 0)   over [S, P, V, A, T]

and the coefficient vector **in the frozen basis**, after conversion, is

    v_frozen    = (G/(2N), -G/(2N), 0, 0, 0)

**The Fierz matrix is applied only to `v_frozen`.** Applying it to the
unconverted vector is prohibited: every matrix-level check would pass
unchanged while the induced coefficients carried a wrong pseudoscalar
sign. A dedicated test locks this conversion and asserts the sign
explicitly.

Combining §1.3 and §1.4, the induced singlet coefficient of family `b`
is

    c_b^singlet = (G/(2N)) · N · Sum_a (v_frozen)_a F_{ab} / (G/(2N))
                = (G/2) · Sum_a (v_frozen_unit)_a F_{ab}

with the traceless coefficient zero, where `v_frozen_unit` is
`v_frozen` with the common `G/(2N)` factored out. The script reports the
exact symbolic result in `G` and `N`.

### 1.5 Checks that must pass

- **Completeness (Deliverable 5):** the sixteen elements are linearly
  independent and span the `4×4` matrices, with no residual.
- **Trace normalisation:** `trace(Id4) = 4`, and
  `trace(Gamma^a Gamma^b) = 4 δ^{ab}` per family.
- **Generator normalisation:** `trace(lam(A) lam(B)) = 2 δ_AB` verified
  for explicit `N`, together with the completeness relation of §0.1.
- **Element-by-element equality (Deliverable 2):** the reconstructed
  matrix is compared to the frozen `matrix_rational` as **exact
  rationals**, entry by entry. Any disagreement is a STOP.
- **Involution (Deliverable 6):** `F` is applied twice and the outcome
  is reported **as it actually holds**. If `F² != Identity` the exact
  residual is reported and no convention is adjusted to force it.

### 1.6 Blind-then-expose protocol

The reconstruction is performed and **serialised to a scratch artifact
outside the repository, whose SHA-256 is recorded, before either frozen
copy of the matrix is parsed or printed**. Only then are the two frozen
copies compared to each other and to the reconstruction. This gives the
independence claim an auditable chronology rather than an attestation.

---

## 2. Derivation (b) — potential values at each stationary branch

### 2.1 The potential is the existing one

**No new effective potential is constructed.** The reduced potential is
the one already fixed in
`derivations/P2-PHASE-01_scalar_stationary_exploratory.md` (SHA-256
`80586e33ef07e307729af4597f72b48f6ecee74fc6a0f396b593f735ef322599`):

    D(p; Mhat) = Sum_mu sin^2 p_mu + W(p; Mhat)^2
    W(p; Mhat) = Mhat + Sum_mu (1 - cos p_mu)
    I0(Mhat)   = Integral_BZ d^4p/(2pi)^4  1 / D(p; Mhat)

    V_red(Mhat; G) - V_red(0; G) = Mhat^2/(4G) - Integral_0^Mhat m I0(m) dm

The evaluation reuses the pinned script's own
`reconstructed_potential`, `WilsonQuadrature` and
`first_derivative` implementations by import, so the quadrature, the
Gauss–Legendre order and the grid construction are identical to the
study that produced the roots.

### 2.2 Conventions fixed before any number is reported

- **Units and measure.** Lattice units, `a = 1`, Wilson parameter
  `r = 1`. `I0` carries the measure `d^4p/(2pi)^4` over the Brillouin
  zone, so the potential is a density **per site (per unit
  four-volume in lattice units)**, not per mode and not extensive.
- **Sign convention.** A more negative value of
  `V_red(Mhat) - V_red(0)` is deeper. Depth statements below use this
  and nothing else.
- **The zero.** The pinned derivation supplies only the **difference**
  `V_red(Mhat; G) - V_red(0; G)`, and scopes its "declared common zero"
  explicitly to within this scalar ansatz. The absolute value
  `V_red(0; G)` — which contains the `Mhat`-independent part of the
  reduced effective action — is **not** reconstructed anywhere in the
  frozen material. Accordingly `potential_value` is reported as
  `NOT DEFINED UNDER THE FROZEN MATERIAL` and the missing zero is
  recorded as `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`. **No zero
  is chosen here.** All depth analysis uses
  `potential_minus_trivial`, which is exactly the quantity the frozen
  formula defines and is unaffected by the missing constant.

### 2.3 Scope limit, stated as required

This comparison is **within the single reconstructed scalar potential**,
where all branches share one potential and one reference point. It says
nothing about cross-family comparison, which would require a common
Hubbard–Stratonovich choice, measure and potential-zero normalisation
that is not frozen. That remains `OPEN-AC-3` and is untouched here.

### 2.4 Evaluation domain, frozen before any result is seen

    grids (n, shift): (32,0.0) (32,0.25) (40,0.0) (40,0.25)
                      (48,0.0) (48,0.25)
    couplings G/G_c:  0.8 0.9 0.98 0.99 1.0 1.01 1.02 1.05
                      1.1 1.2 1.4 1.6 1.8 2.0 2.5 3.0

Branches are the algebraic roots recorded per (grid, shift, coupling) in
the pinned exploratory results artifact.

### 2.5 Cross-grid correspondence and stability, frozen algorithm

**Correspondence.** At fixed `G/G_c`, roots are partitioned by sign;
`mhat = 0` matches only itself; within each nonzero sign sector roots are
ordered monotonically by `mhat` and equal ordinal positions correspond
across grid/shift combinations. If root counts differ between
combinations, or the rule does not yield a one-to-one correspondence,
the branch is recorded as having UNRESOLVED CROSS-GRID CORRESPONDENCE,
with no stable-digit count and no cross-grid depth ordering.

**Stability.** Over the participating combinations,
`V_min = min(V_i)`, `V_max = max(V_i)`, `spread = V_max - V_min`, all
three reported. `stable_decimal_places` is the largest `d` with
`0 <= d <= d_max` for which all participating values quantized to `d`
decimal places are identical, where `d_max` is the minimum number of
decimal places explicitly stored; if agreement survives through `d_max`,
`d_max` is reported. Quantization goes through the decimal
representation with `decimal.ROUND_HALF_EVEN`; binary-float `round()` is
not used. `stability_status` disambiguates a bare `0` between
"agreement exists at `d = 0`" and "no non-negative decimal-place
agreement exists".

**Depth ordering.** Two branches are RESOLVED in depth only if their
`[V_min, V_max]` envelopes are disjoint. Overlapping envelopes are
reported as unresolved at the available grid resolution and are not
ranked.

Comparisons are at fixed `G/G_c`, not fixed absolute `G`; `G_c` is
grid-dependent and corresponding points need not share an absolute `G`.

### 2.6 Regression anchor and derivative check

The accompanying test file asserts a **nonzero** reference value of the
reconstructed potential at a stated `Mhat != 0` on a stated grid, to a
stated tolerance, so that an identically-zero implementation cannot
pass. **That reference value is computed by this task and recorded in
this task's results artifact; it is not a pre-existing frozen number**
and is a regression anchor against future drift, not independent
validation of correctness. The test also checks that the numerical
derivative of the reconstructed potential reproduces the reduced first
derivative `V'_red(Mhat; G) = Mhat (1/(2G) - I0(Mhat))` at several
`Mhat`, including at least one stationary point where it must vanish and
one non-stationary point where it must not.

---

## 3. What this note does NOT conclude

- **No Hubbard–Stratonovich channel is chosen.** That is `OPEN-AC-1` and
  belongs to the PI.
- **No V/A/T orientation or component structure is chosen.**
- **No inference is drawn from the size of the bare Fierz coefficients
  about the size of the mean-field ambiguity.** They are different
  quantities; the latter depends on which channel is bosonised and on
  the truncation, and is `P2-FIERZSUM-01`'s subject.
- **No branch is characterised as "the vacuum", "preferred",
  "physical", or as an artifact.** Whether the deepest branch is the
  physical ground state, and whether the negative-mass branch is a
  physical phase or a doubler sector, is `OPEN-AC-2` and is not answered
  here. Depth ordering is reported as an observation and nothing more.
- **No absolute potential zero is chosen** (§2.2).

## 4. Exclusions

The quarantined `−3.2(5)`, the suspended `P2-BETAV-CIRC-01` result, and
the historical Finding 5 extraction are **not** inputs to either
derivation. The complete list of repository inputs actually read is
enumerated in the report and in the results artifact.
