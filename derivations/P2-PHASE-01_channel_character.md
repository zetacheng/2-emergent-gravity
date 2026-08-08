# Derivation note — `P2-PHASE-01`: channel character of the Fierz-induced interaction

**Kind:** a two-part derivation. It fixes the analytic content **before
any output is produced**, per `AGENTS.md` rule 3, so the algebra is
reviewable before a result can influence it.

**This is a computation, not a ruling.** It registers no gate, changes
no status, and reaches no admissibility verdict. `P2-PHASE-01` remains
`PROPOSED`. **It does not select a Hubbard–Stratonovich channel** —
`OPEN-AC-1` is the PI's.

Authority: `specs/2026-08-08T1321Z_channel-character.md`.

---

## 0. Frozen inputs, verified before use

SHA-256 verified against the specification's pins at evidence base
`eb88a2c9174cfda746c266924e741a6f88134234`; all seven matched.

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
      fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a
    results/P2-CHANNEL-FREEZE/fierz_matrix.json
      5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9
    derivations/CANONICAL_INTERACTION.md
      27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81
    derivations/P2-PHASE-01_fierz_verification_and_branch_depths.md
      c7e5744c9744780b6eb205c08ff9b65393e0055d7ebf04f2e0fc406d028edeb5
    results/P2-PHASE-01/fierz-and-branch-depths/fierz_and_depths.json
      9bf14f51cc1fbdf4523debe70ad91164bc6d9c96d75f3450b7bce6d43514ec1d
    derivations/P2-PHASE-01_fierz_sign_addendum.md
      a0553b8a79cfcd521620448f7d1d6928475573e751dd404698adcd48ad6871df
    derivations/P2-GAP-01_gap_criticality.md
      17b6f613ffefb79fae8c0a5c40e3bd67ad31a101112af615945647e143fade00

The conventions are frozen, not chosen: Euclidean `metric_signature
(1,1,1,1)`; Hermitian `gamma_mu` with `{gamma_mu, gamma_nu} = 2
delta_munu`; `gamma5 = gamma(0)gamma(1)gamma(2)gamma(3)`, Hermitian,
`gamma5^2 = Id4`; `trace(Id4) = 4`;
`trace(lam(A) lam(B)) = 2 delta_AB` with `lam(0) = sqrt(2/N) Id_N`;
`grassmann_crossing_sign: -1`; `basis_order [S,P,V,A,T]`.

## 1. Derivation (a) — three layers, kept apart

The three layers depend on strictly increasing amounts of frozen
material. **They are reported separately and never collapsed**, because
the repository may support the first without supporting the later ones,
and it does.

### 1.1 Layer 1a — the frozen algebraic coefficient. Unconditional.

**Normalisation is the whole difficulty here**, so it is stated before
any number. A coefficient is meaningless without the operator it
multiplies, and this note uses **two explicit normalisations
throughout**, never mixing them:

    normalisation L :  coefficient of  (psibar lam(0) Gamma psi)^2
    normalisation P :  coefficient of  (psibar Gamma psi)^2

They are related by the frozen singlet definition alone:

    (psibar lam(0) Gamma psi)^2 = (2/N) (psibar Gamma psi)^2
    so   c_P = (2/N) * c_L

**The scalar coefficient is read from the frozen material**, not
assumed. The freeze's `interaction_decomposition` (line 116 of the
Phase-A freeze) carries, for both supported families,

    family S: coefficient "G/(2*N)", operator Sum(bilinear(lam(A),Id4)**2, (A,0,N**2-1))
    family P: coefficient "G/(2*N)", operator Sum(bilinear(lam(A),I*gamma5)**2, (A,0,N**2-1))

so `c_can = G/(2N)` in normalisation L, with `G > 0` frozen by
`CANONICAL_INTERACTION.md` §2 and §3.

**The induced V and A coefficients are recomputed here**, not copied
from the landed result. The chain is exactly the one the landed Fierz
verification fixed:

1. the canonical coefficient vector over `[S,P,V,A,T]` is
   `v_can = (G/2N, G/2N, 0, 0, 0)`;
2. the mandatory basis conversion `(bilinear(lam(A), I*gamma5))^2 =
   -(bilinear(lam(A), gamma5))^2` gives
   `v_frozen = (G/2N, -G/2N, 0, 0, 0)`;
3. the frozen `matrix_rational` is applied to `v_frozen` only;
4. the internal factor `Sum_A lam(A)_ab lam(A)_cd = 2 delta_ad delta_cb`
   with `Id_N = sqrt(N/2) lam(0)` supplies the factor `N` and makes the
   induced structure purely singlet;
5. the Grassmann crossing sign `s_G = -1` is applied **exactly once at
   operator use**, per the 2026-08-07 ruling, carrying the matrix-level
   values to operator-level ones.

The resulting Layer-1a table, with `G > 0` and `N > 0`:

    channel                         normalisation L      normalisation P
    scalar singlet (direct)            +G/(2N)              +G/N^2
    induced V singlet (operator)       -G/4                 -G/(2N)
    induced A singlet (operator)       -G/4                 -G/(2N)
    induced S, P, T                     0                     0

**Signs: the scalar coefficient is positive; the induced V and A
coefficients are negative. This is unconditional** — it needs no
knowledge of how the expression enters the Euclidean exponent, and it is
the deliverable that stands whatever the later layers do.

**A normalisation observation, recorded because it affects how the
numbers are compared.** The authority's exploratory pairing quotes the
scalar singlet as `+G/N^2` and the induced vector singlet as `-G/4`.
Those are correct values, but **they are stated in different
normalisations** — `+G/N^2` is normalisation P and `-G/4` is
normalisation L. In either single normalisation the pair is
`(+G/(2N), -G/4)` or `(+G/N^2, -G/(2N))`. **The sign conclusion is
unaffected**, which is why this is an observation and not a
disagreement; the magnitudes as paired are not directly comparable.

### 1.2 The scalar control, and what it does and does not test

`P2-GAP-01` states an **attractive scalar (`psibar psi`) channel** and
the normalisation `L_int = G_N (psibar psi)^2` with `G_GAP = 4 G_N`, the
factor 4 absorbing `trace(Id4) = 4` so that the gap equation's
combinatorial prefactor is exactly 2.

The singlet projection of the frozen canonical interaction, in the same
operator and the same normalisation P, gives

    G_N = G/N^2 ,      G_GAP = 4 G/N^2 ,      both > 0 for G > 0.

**Same operator `(psibar psi)^2`; same internal normalisation, using
only the frozen `lam(0) = sqrt(2/N) Id_N`; same factor-of-two convention,
`G_GAP = 4 G_N`.** The sign is positive, matching `P2-GAP-01`'s
attractive scalar channel. **The Layer-1a control passes.**

**What the control does not test, stated so it is not over-read.** It
tests the operator, the normalisation map and the sign. It does **not**
re-derive `G_c = 1/(2 I_0)` for the generator-sum interaction:
`P2-GAP-01` worked from `L_int = G_N (psibar psi)^2`, a singlet-only
form, and the mean-field combinatorics of the full `U(N)` generator sum
were not performed there and are not performed here. A numerical
identification of `G` with `G_GAP` at fixed `N` is a separate question.

### 1.3 Layer 1b — the exponent mapping, and why it is not frozen

The Hubbard–Stratonovich identity

    exp[(g/2) J^2] = Integral dPhi exp[-Phi^2/(2g) + Phi J]

converges only for `g > 0`. **`g` is an exponent-level quantity and is
not `2c`.** If the frozen expression is a term of `S_E`, the Boltzmann
weight carries `exp[-S_E] ⊃ exp[-c J^2]` and `g = -2c`; if the
expression already sits in the exponent, `g = +2c`. The two differ by a
sign.

**The frozen material does not fix which.** What it does contain:

- `CONVENTIONS.md`, "Sign of the action": *"Euclidean action `S_E ≥ 0`;
  `Z = ∫ e^{−S_E}`, effective action `W = −ln Z`."* This fixes the
  **form** of the Boltzmann weight. It says nothing about which term of
  which functional the canonical four-fermion expression is.
- `CANONICAL_INTERACTION.md` §2 writes *"The canonical action:"* and
  then
  `L = Sum_a psibar_a (i gamma^mu d_mu) psi_a + (G/2N) Sum_A [S^A^2 + P^A^2]`.
  The kinetic operator is `i gamma^mu d_mu` — a **Minkowski** form —
  while every convention governing the algebra, including the freeze's
  own `metric_signature (1,1,1,1)`, is **Euclidean**.
- **No Wick-rotation rule connecting the two is recorded anywhere in the
  frozen material.** Searching the seven pinned files plus
  `CONVENTIONS.md` for `S_E`, `Euclidean action`, `Wick`, `Boltzmann`,
  `L_E`, `S_int`, `exp(-`, `exp[-`, `e^{-`, `action density`,
  `Lagrangian`, `enters the exponent` returns only the two
  `CONVENTIONS.md` entries above; there is no statement of the form
  `S_E = -Integral L` or `S_E = Integral L_E`.

**Verdict: `REAL-HS ADMISSIBILITY NOT DEFINED BY THE FROZEN
MATERIAL`.**

**Both branches are nonetheless reported, because one of them is
inconsistent with what the repository has already executed.** Writing
`c J^2 = (g/2) J^2` at exponent level:

    branch (i)   the expression enters the exponent with a + sign, g = +2c
                 scalar   g = +2G/N^2  > 0   real HS field admissible
                 V and A  g = -G/N     < 0   no real linear HS field
    branch (ii)  the expression is a term of S_E,      g = -2c
                 scalar   g = -2G/N^2  < 0   no real linear HS field
                 V and A  g = +G/N     > 0   real HS field admissible

**Branch (ii) contradicts `P2-GAP-01`'s executed calculation**, which
introduces a **real** scalar auxiliary `Sigma` for the attractive scalar
channel and obtains a physical critical coupling `G_c = 1/(2 I_0)`. A
scalar channel with `g < 0` admits no real linear HS field, so branch
(ii) cannot be the convention `P2-GAP-01` operated under.

**This is an inference from usage, not a frozen definition, and it is
labelled as such.** It is reported as evidence bearing on which mapping
the programme is in fact using; it does not turn Layer 1b into a
resolved layer, and the verdict above stands. **Fixing the mapping is a
PI decision this note informs and does not take.**

### 1.4 Layer 2 — the physical label

"Attractive" and "repulsive" are claims about two-body forces and bound
states. **Real-HS admissibility is not the same statement**: a negative
`g` forces an imaginary HS contour, which is not by itself the absence
of an interaction in that channel.

Layer 2 requires the exponent mapping **and** a criterion tying a
coefficient's sign to a force label. The frozen material supplies two
anchor points but no general criterion:

- `CONVENTIONS.md`, "Definition of attractive and repulsive channels":
  *"Scalar (`psibar psi`) condensate channel is the attractive channel
  driving the gap; the four-fermion coupling `G > 0` is attractive
  there."* This labels **one** channel. It is not a rule mapping an
  arbitrary channel's coefficient sign to a label.
- `CANONICAL_INTERACTION.md` §3 and §7(b) record the vector-singlet
  Fierz image `G_omega = -G/N` as **repulsive**, and the classification
  *"`G_V < 0` repulsive/ω survives"*. That is a second anchor of the
  same sign convention — but it is a **recorded Paper-3 claim**, its
  source note `derivations/u3-fierz/u3_fierz.md` is **not present in
  this repository**, and `CANONICAL_INTERACTION.md` carries a DRAFT v0.5
  banner reading *"Nothing here has governing force until the
  ratification record replaces this banner"* while also carrying a
  completed ratification record at its foot.

Since Layer 1b is withheld, **Layer 2 is withheld:
`ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN MATERIAL`.**

**Conditionally**, under branch (i) — the only branch consistent with
`P2-GAP-01`'s executed HS treatment — and reading the two anchors above
as a common sign convention, the induced singlet V and A would be
**repulsive**, the scalar **attractive**. That is stated as a
conditional consequence, not as this note's verdict.

### 1.5 On `U''(0)`

**`U''(0)` is not an independent second route and is not used as
corroboration here.** For the bare quadratic term `U(Phi) = Phi^2/(2g)`,
`U''(0) = 1/g` — the Layer-1b sign test restated in other symbols. For
the fermion-integrated effective potential, `U''(0) = 1/g - Pi(0)`,
whose sign **changes with the coupling**: an attractive scalar channel
still has `U''(0) > 0` below `G_c`. **So `attractive <=> U''(0) > 0` is
false**, and no curvature is offered in this note as evidence for a
force label.

### 1.6 Convention dependence

The Layer-1a signs depend on:

- **the Euclidean signature** `(1,1,1,1)` and Hermitian gammas, which fix
  the frozen Fierz matrix;
- **the mandatory `I*gamma5 -> gamma5` basis conversion**, without which
  the induced coefficients carry a wrong pseudoscalar sign while every
  matrix-level check still passes;
- **the 2026-08-07 ruling** that `matrix_rational` is stored unsigned
  and `s_G = -1` is applied exactly once at operator use.

**If the `s_G` ruling were reversed** — that is, if `matrix_rational`
were held to store the sign already, so that no further factor is
applied at operator use — then the induced V and A operator-level
coefficients become `+G/4` (normalisation L) and `+G/(2N)`
(normalisation P). **Every sign statement about the induced channels in
this note reverses**; the scalar channel, which is direct and not
Fierz-induced, is untouched. The structural results are also untouched:
`S`, `P`, `T` still vanish, `V` and `A` are still equal and purely
singlet, and the exchanged form is still purely left-right, because an
overall sign multiplies all four chiral coefficients equally.

### 1.7 What this does and does not say about a composite vector

This note computes the sign of the induced singlet `V` and `A`
coefficients in the particle–hole rearrangement of the frozen canonical
interaction. **It does not examine every channel**, and in particular
the particle–particle channel is not computed at all — see §2.

**A repulsive `psibar gamma_mu psi` channel would not by itself exclude
a bound state in another channel.** No statement is made here about
whether Paper 3's massive composite vector can form; that would be a
claim about channels this derivation does not examine.

## 2. Derivation (b) — is the diquark channel computable?

This is an **executability determination** first and a computation only
if it passes. It is worked through the four ordered steps of the
authority, not stopped at the first.

### 2.1 Step 1 — is `C` fixed by the frozen material?

**No.** Searching the seven pinned files plus `CONVENTIONS.md` for
`charge conjugation`, `charge-conjugation`, `conjugation matrix`,
`psi^c`, `psi_c`, `diquark`, `particle-particle` and a standalone
capital `C` returns **zero** matches. The six case-insensitive `c =`
hits are all lowercase `c` in `G_c` and `c = 8` in `P2-GAP-01`, none
related to charge conjugation. **The null result is auditable, not
asserted.**

### 2.2 Step 2 — does the defining relation fix `C` up to a scalar?

**Yes, and this is computed rather than argued.** In the frozen
Euclidean representation the defining relation

    C gamma_mu^T C^-1 = -gamma_mu       equivalently   C gamma_mu^T + gamma_mu C = 0

is a linear system on the sixteen entries of `C`. Solving it gives a
solution space of **complex dimension exactly 1**. So every admissible
`C` is `lambda C_0` for a single nonzero complex `lambda`; there is no
further discrete freedom.

The representative `C_0` obtained satisfies `C_0^T = -C_0`
(antisymmetric), `C_0^dagger C_0 = Id4`, `det C_0 = 1`, and the defining
relation for all four `mu`.

### 2.3 Step 3 — does the residual scalar affect the channel character?

**The residual `lambda` cancels, and that too is computed.** A
particle–particle rearrangement pairs the fields so that `C` and `C^-1`
each appear exactly once, in the two conjugate factors:

    psi^c = C psibar^T                 -> lambda   psi^c
    psibar^c = eta psi^T C^-1          -> lambda^-1 psibar^c   (eta a sign convention)

so the Dirac structure of the paired product carries `lambda^{+1}
lambda^{-1} = 1`. **The channel coefficients are invariant under the
residual scale.** Step 2 and step 3 therefore succeed: the absence of a
frozen `C` is **not** the obstruction.

### 2.4 Step 0 — the obstruction, which is elsewhere

Step 0 asks whether **all** operator definitions needed to build the
particle–particle bilinear are fixed or convention-independent. They are
not:

- **the charge-conjugated field definition.** In Euclidean signature
  `psi` and `psibar` are independent Grassmann variables, so `psibar^c`
  is not derivable from `psi^c` by conjugation — it must be **defined**.
  The sign/phase `eta` in `psibar^c = eta psi^T C^-1` appears **once**
  in the paired product, so it multiplies the pp coefficient by `eta`
  and **flips its sign** for `eta = -1`. Nothing in the frozen material
  fixes `eta`.
- **the Grassmann ordering of the pp bilinear.** The freeze fixes
  `compound_index_order [dirac_family, internal_family, component]` and
  a crossing sign for the particle–hole exchange
  `(alpha,beta,gamma,delta) -> (alpha,delta,gamma,beta)`. It fixes **no**
  ordering convention for a particle–particle pairing, and the reordering
  parity there is a different permutation.
- **the diquark operator normalisation.** Not stated anywhere.

**A settled `C` does not license supplying these.** Each is an
independent sign or normalisation convention, and at least one of them —
`eta` — changes the sign of the result, which is precisely the quantity
in question.

### 2.5 Step 4 — the verdict

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`**, reached at step 4 and
not before, with the dependence shown: the pp channel character is
invariant under the residual freedom in `C` but **is not invariant**
under the un-frozen charge-conjugated-field convention `eta`, and the
frozen material fixes neither `eta` nor the pp Grassmann ordering nor the
diquark normalisation.

**No `C` is selected, and no pp projection is constructed.** The
authority records an earlier exploratory diquark projection that
returned zero in all four families and is treated there as a failed
attempt rather than a finding; **this note does not repeat it**, because
constructing the projection would require supplying exactly the
conventions step 0 shows to be missing.

**Whether `C`, `eta` and the pp ordering should be frozen, and to what,
is a PI decision this note informs and does not take.** A blocked (b) is
a satisfactory outcome and does not block (a).

## 3. What this note does not do

It registers no gate and changes no status. It selects no
Hubbard–Stratonovich channel: it reports which channels admit a real
linear auxiliary field **under each of the two possible exponent
mappings**, and reports that the mapping itself is not frozen.
`OPEN-AC-1` is untouched. `P2-PHASE-01` remains `PROPOSED`.
