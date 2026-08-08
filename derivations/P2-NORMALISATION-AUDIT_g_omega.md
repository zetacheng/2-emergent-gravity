# Derivation note — normalisation audit: `G_ω` against the derived vector coefficient

**Kind:** an evidence-production note. It fixes the analytic content
**before any production code**, per `AGENTS.md` rule 3.

**This produces one row of an evidence table. It ratifies nothing.** It
does not remove or amend `CANONICAL_INTERACTION.md`'s DRAFT v0.5 banner,
modifies no Paper-3 content, and decides no other row of that table.

Authority: `specs/2026-08-08T1354Z_normalisation-audit.md`.

---

## 0. Inputs, verified before use

**Local pins**, SHA-256 read from the git objects at evidence base
`eb88a2c9174cfda746c266924e741a6f88134234`; all four matched:

    derivations/CANONICAL_INTERACTION.md
      27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
      fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a
    results/P2-CHANNEL-FREEZE/fierz_matrix.json
      5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9
    derivations/P2-PHASE-01_fierz_sign_addendum.md
      a0553b8a79cfcd521620448f7d1d6928475573e751dd404698adcd48ad6871df

**External pin**, `zetacheng/3-vector-sector` @
`8c363ef08368f5c022278ea5f36e01496be3d5ca`:

    derivations/u3-fierz/u3_fierz.md
      6784d51a5a8d5f8b70b55213e4bf9b3eb50fc8c331397e80a239d16285d58f49

Matched. **The evidence is available; no `UNAVAILABLE EVIDENCE` finding
arises.** The external repository was cloned read-only to a workspace
path outside this repository. **Nothing in Paper 3 was modified and no
Paper-3 file was copied into this repository** — the quotations below
are quotations, not imports.

**The channel-character branch is not an input.** `gate/p2-channel-character`
@ `cb604a4e3a96f9120787a685120f205d8e4c7c88` is unmerged, and its
artifact does not exist at the evidence base. The vector coefficient is
**recomputed here from the frozen material**; the branch is consulted
only afterwards, and only to (i) quote the normalisation definition it
declares, as §2A of the authority requires, and (ii) compare values.

## 1. The two normalisations, quoted

### 1.1 Paper 3, at the pinned revision

`derivations/u3-fierz/u3_fierz.md`, **line 10**:

> Classification (Paper 3 convention `L_V = (G_V/2) J_mu J^mu`,
> `J_mu = psibar gamma_mu psi`):

and **line 11**:

> `G_V < 0` repulsive (omega survives) / `G_V > 0` attractive (fails) /
> `G_V = 0` no channel.

The assembly, **lines 185–190**:

>     - **Level 3 — normalize to `J_mu`.** `psibar gamma_mu lambda^0 psi =
>       sqrt(2/3) psibar gamma_mu psi = sqrt(2/3) J_mu`, so
>       `(psibar gamma_mu lambda^0 psi)^2 = (2/3) J_mu J^mu`. Restoring
>       `L_int = (G/2N)*[...]`:
>
>           L_int -> (G/2N) * (-3/2) * (2/3) J_mu J^mu  =  -(G/2N) J_mu J^mu
>                  =  (G_omega/2) J_mu J^mu   with   G_omega = -G/N.

**This is the decisive text.** Paper 3 states, in one line, both the
coefficient of `J_μ J^μ` and the quantity it calls `G_ω`:

    coefficient of J_mu J^mu  =  -(G/2N)
    G_omega                   =  -G/N     because  L_V = (G_V/2) J_mu J^mu

**`G_ω` is defined as twice the coefficient of `J_μ J^μ`.** That is the
whole of the apparent discrepancy.

### 1.2 This repository

The channel-character artifact declares, verbatim:

    normalisation_L_definition : coefficient of (psibar lam(0) Gamma psi)^2
    normalisation_P_definition : coefficient of (psibar Gamma psi)^2
    normalisation_relation     : c_P = (2/N) * c_L, from lam(0) = sqrt(2/N) Id_N

and reports the induced V singlet as `-G/4` in normalisation L and
`-G/(2*N)` in normalisation P.

**Neither of this repository's normalisations carries a factor of one
half.** Both are plain coefficients of a squared bilinear. `G_ω` is not
one of them — it is a third quantity, defined by Paper 3's `(G_V/2)`
convention.

## 2. The conversion, symbolically

Let `c_J` be the coefficient of `J_μ J^μ = (ψ̄γ_μψ)²` in `L_int`, which
is exactly this repository's normalisation P. Paper 3's convention is

    L_V = (G_V/2) J_mu J^mu       so       G_omega = 2 * c_J

**The conversion factor is exactly 2, and its origin is the explicit
`1/2` in `L_V = (G_V/2) J_mu J^mu` at line 10 of the Paper-3 note.** It
is a definitional prefactor on the reported coupling, not an algebraic
step, and it appears nowhere in the frozen Paper-2 material because
Paper 2 reports plain operator coefficients.

A second, smaller conversion connects this repository's two internal
normalisations and is used by both documents alike:

    (psibar Gamma lam(0) psi)^2 = (2/N) (psibar Gamma psi)^2
    so   c_J = (2/N) * c_L ,   from the frozen  lam(0) = sqrt(2/N) Id_N

Paper 3 performs the same step at its Level 3, writing `sqrt(2/3)` for
`N = 3`.

## 3. Independent recomputation

**Recomputed from the frozen canonical interaction and the verified
Fierz matrix**, not transcribed. The chain, with `N` symbolic:

1. the frozen `interaction_decomposition` gives the per-family canonical
   coefficient `c_can = G/(2N)`, identical for the S and P families;
2. the canonical vector over `[S,P,V,A,T]` is
   `(c_can, c_can, 0, 0, 0)`; the mandatory
   `(bilinear(lam(A), I*gamma5))² = −(bilinear(lam(A), gamma5))²`
   conversion gives `(c_can, −c_can, 0, 0, 0)`;
3. the frozen `matrix_rational` acting on that vector gives the Dirac row
   `[0, 0, 1/2, 1/2, 0]`, so `c_V^Dirac = +1/2`;
4. the internal factor `Sum_A lam(A)_ab lam(A)_cd = 2 δ_ad δ_cb` with
   `Id_N = sqrt(N/2) lam(0)` supplies `N` and makes the induced structure
   purely singlet;
5. the Grassmann crossing sign `s_G = −1` is applied exactly once at
   operator use, per the 2026-08-07 ruling.

Result:

    c_L  (coefficient of (psibar lam(0) gamma_mu psi)^2)   =  -G/4
    c_J  (coefficient of J_mu J^mu)                        =  -G/(2N)
    2*c_J  (Paper 3's G_omega)                             =  -G/N

**Paper 3's intermediate quantities are reproduced at every level**,
which is a stronger check than agreement on the endpoint alone:

    quantity                          Paper 3 (N=3)   recomputed here
    c_V^Dirac                              +1/2            +1/2
    c_V^(0)  (inside the bracket)          -3/2      -N/2 -> -3/2
    coefficient of (psibar lam0 g psi)^2   -G/4            -G/4
    coefficient of J_mu J^mu             -(G/2N)         -G/(2N)
    G_omega                                -G/N            -G/N

Paper 3's `c_V^(0) = (Grassmann -1) * c_V^Dirac * f_singlet` with
`f_singlet = 3 = N` is the same assembly as steps 4–5 above. **Paper 3
also applies the crossing sign once, at operator use**, which is the
convention the 2026-08-07 ruling fixed for this repository; the two
agree on that too, and had they not, the endpoint agreement would have
been accidental.

## 4. Verdict

### **`NORMALISATION MAPPING`.**

The two values agree once the declared normalisations are accounted for.
The mapping, recorded:

    Paper 2 (this repository)   c_J    = -G/(2N)   coefficient of (psibar gamma_mu psi)^2
    Paper 3                     G_omega = -G/N     defined by L_V = (G_V/2) J_mu J^mu
    mapping                     G_omega = 2 * c_J

**The evidence selecting this verdict, rather than `REPOSITORY_DEFECT`,
is line 189 of the Paper-3 note**, which writes the coefficient of
`J_μJ^μ` explicitly as `-(G/2N)` **before** converting it to `G_ω`. That
is the same number this repository derives, in the same operator
normalisation, on the same page. There is no factor-of-two disagreement
to fold away: the two documents never disagreed about a coefficient,
only about which quantity they name.

**Neither value was adjusted.** Both are quoted and recomputed as they
stand.

`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` is also excluded: both
normalisations are stated precisely — Paper 3 at its line 10 and in the
assembly line itself, this repository in its artifact's declared
`normalisation_P_definition`.

## 5. What this row does not close

This is **one row** of the evidence table
`derivations/CANONICAL_INTERACTION.md` §5 requires. The remaining rows
are **not addressed here**:

- starting-interaction match — file path, line range and pinned SHA
  showing Paper 3 begins from §2's generator-sum form;
- `G_ω = −G/N` traced to its derivation equation reference **as a
  provenance record**, distinct from the normalisation reconciliation
  performed here;
- claim status `VERIFIED` — registry path and entry;
- test count — command and output digest;
- convention-compatibility table — explicit comparison.

**`CANONICAL_INTERACTION.md`'s DRAFT v0.5 banner therefore stands**, and
this note does not touch it. The document is unmodified.

**This note also does not revisit** the channel-character task's Layer 1b
and Layer 2 withholdings. The comparison performed here is between
**algebraic coefficients of the same operator inside the written
`L_int`** — Layer 1a in that task's terms, the layer that was
unconditional. It says nothing about how either document's `L_int` enters
a Boltzmann exponent, and nothing about attractive/repulsive labels.

## 6. What this note does not do

It registers no gate, changes no status, and ratifies nothing.
`P2-PHASE-01` remains `PROPOSED`. The Paper-3 claim's own status is
Paper 3's to record.
