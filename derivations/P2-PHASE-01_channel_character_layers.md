# Derivation note — `P2-PHASE-01`: Layer 1b and Layer 2 of the channel character

**Kind:** a recomputation. It resolves the two layers that
`derivations/P2-PHASE-01_channel_character.md` deliberately withheld,
using two conventions supplied by PI ruling since that note was written.
It fixes the analytic content **before any output is produced**, per
`AGENTS.md` rule 3.

**This is a computation, not a ruling.** It registers no gate, changes
no status, and reaches no admissibility verdict. `P2-PHASE-01` remains
`PROPOSED`. **It does not select a Hubbard–Stratonovich channel** —
`OPEN-AC-1` is the PI's.

**It is conditional on two rulings and derives neither of them.** Both
are recorded in `DECISION_LOG.md`, both are dated 2026-08-08, and both
state in their own text that they supply conventions the frozen material
never carried. Every Layer-1b and Layer-2 value below inherits that
status.

Authority: `specs/2026-08-09T0300Z_attraction-ruling-and-layers.md`.

---

## 0. Scientific question

The channel-character derivation delivered Layer 1a and withheld the
other two:

    Layer 1a   delivered      c per channel
    Layer 1b   NOT DEFINED    exponent mapping not frozen
    Layer 2    NOT DEFINED    no sign-to-label rule anywhere

Both blockers have since been removed by ruling. The question here is
narrow: **given `c` per channel, what is `g` per channel, and what label
does each `g` carry?**

## 1. Frozen and pinned inputs, verified before use

SHA-256 verified against the specification's pins at evidence base
`3b3d3b2e34a0a60fb6066bd97b8bdfa8279ff05b`; all four matched.

    derivations/P2-PHASE-01_channel_character.md
      380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f
    results/P2-PHASE-01/channel-character/channel_character.json
      093d20c0e01dc5626cafb4da9b5a0d0e5e95edbd0a8853bbc562248a5b36ee7f
    scripts/p2_channel_character.py
      521dfd0ba8585dbaabe731bcb231a19ea599a54e975682b819f8da8d0f6e1126
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
      fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a

The freeze is reached transitively: the Layer-1a control re-executes the
pinned script's `layer_1a()`, which reads the frozen basis block and the
frozen `matrix_rational` from that document and from
`results/P2-CHANNEL-FREEZE/fierz_matrix.json`.

## 2. Locked conventions

**Two normalisations, carried side by side and never mixed** — as in the
pinned note:

    L : coefficient of (psibar lam(0) Gamma psi)^2
    P : coefficient of (psibar Gamma psi)^2
    c_P = (2/N) * c_L,   from lam(0) = sqrt(2/N) Id_N

**Convention I — the Euclidean exponent mapping**, `DECISION_LOG.md`
entry `## 2026-08-08 — Euclidean exponent mapping: the canonical
interaction is written in the exponent`. The canonical interaction
expression is written as it appears in the Boltzmann exponent:

    exp(-S_E) contains exp(+X)        <=>        S_E = S_E,0 - X

so that for a channel whose coefficient in `X` is `c`, written as
`c * J**2`,

    g = +2c

**Convention II — the attraction/repulsion label**, `DECISION_LOG.md`
entry `## 2026-08-08 — Attraction/repulsion sign convention: the label
is assigned to the sign of g`:

    g > 0   ->   ATTRACTIVE
    g < 0   ->   REPULSIVE

**Both are conventions, not results.** Convention II depends on
Convention I: reversing the mapping reverses every `g` and therefore
every label. They are a chain.

**The Hubbard–Stratonovich identity**, unchanged from the pinned note:

    exp[(g/2) J^2] = Integral dPhi exp[-Phi^2/(2g) + Phi J]

convergent only for `g > 0`. **`g` is an exponent-level quantity.** It
is `2c` here because Convention I says so, not because `g` and `c` are
the same kind of object.

**What does not enter.** `G_c` does not appear anywhere in this
derivation. The generator-sum criticality result `G_c = N/(8·I_0)`
concerns the critical coupling; `g` is a channel coefficient. They are
different quantities and no reconciliation between them is attempted.

## 3. The analytic derivation

### 3.1 Layer 1a, restated as the control

From the pinned artifact, in both normalisations:

    channel                     c_L          c_P        sign(c)
    scalar_singlet_direct     G/(2*N)      G/N**2         +1
    induced_V_singlet           -G/4     -G/(2*N)         -1
    induced_A_singlet           -G/4     -G/(2*N)         -1

`G` and `N` are positive, so the signs are unambiguous.

**This is a gating control.** The recomputation re-executes the pinned
script's `layer_1a()` and compares every coefficient, in both
normalisations, as an exact symbolic difference against the pinned
`channel_character.json`. Everything downstream is a function of `c`; if
the control fails, nothing below is trustworthy.

### 3.2 Layer 1b — the exponent coefficient

Applying Convention I channel by channel, `g = 2c` in whichever
normalisation `c` is stated:

    channel                     g_L          g_P        sign(g)   real HS
    scalar_singlet_direct         G/N    2*G/N**2         +1        yes
    induced_V_singlet            -G/2       -G/N          -1        no
    induced_A_singlet            -G/2       -G/N          -1        no

**The sign of `g` equals the sign of `c`**, because the mapping factor
`+2` is positive. That is a consequence of Convention I and would not
survive its reversal: under the opposite mapping every `g` above flips
and every entry in the "real HS" column flips with it.

**"Real HS" means exactly one thing**: whether the standard linear
Hubbard–Stratonovich representation with a *real* Gaussian auxiliary
field is available, i.e. whether the Gaussian integral converges, i.e.
whether `g > 0`. It is not a statement about two-body forces, and a
`no` in that column is not the absence of an interaction in the channel.

**Cross-check against the pinned artifact.** The pinned note computed
both possible mappings as branches without choosing between them. Its
branch (i), described there as `weight carries exp[+c J^2]; g = +2c`, is
the branch Convention I selects, and its `g_in_normalisation_P` values
are `2*G/N**2`, `-G/N`, `-G/N` for the scalar, V and A. **These agree
with the table above.** The ruling did not change the arithmetic; it
chose which of two arithmetics is the programme's.

### 3.3 Layer 2 — the label

Applying Convention II to the signs of §3.2:

    channel                   sign(g)     label
    scalar_singlet_direct        +1     ATTRACTIVE
    induced_V_singlet            -1     REPULSIVE
    induced_A_singlet            -1     REPULSIVE

**The ruling is the basis, not a derivation.** Convention II assigns a
name to a sign. Nothing in §3.3 is derived from the frozen material, and
the labels are exactly as reversible as the mapping they rest on.

### 3.4 The scalar control

`P2-GAP-01` describes its scalar channel as attractive at positive
coupling, and its mean-field treatment introduces a real auxiliary
field. The scalar singlet here has `c > 0`, hence `g > 0`, hence
`ATTRACTIVE`, and admits a real linear auxiliary field.

**This is gating.** The scalar coming out anything other than
`ATTRACTIVE` would mean the chain from `c` through `g` to the label is
wrong, and the V and A results could not be trusted either.

**What the control does not test.** It does not re-derive
`G_c = 1/(2·I_0)`, and it does not lift `P2-GAP-01` to the generator-sum
interaction. It checks a sign against a description.

## 4. Expected limiting cases and dimensional analysis

**Dimensions.** `c` and `g` carry the dimensions of `G` throughout; the
mapping multiplies by the pure number `2` and the normalisation change
by the pure number `2/N`. No dimensionful quantity is introduced, and
none of the sign conclusions can depend on units.

**`N` dependence.** Every coefficient is a positive rational multiple of
`G` divided by a positive power of `N`, so no sign changes with `N` and
no channel degenerates or crosses zero at any admissible `N`. The
`G -> 0` limit sends every `g` to zero from its own side without a sign
change.

**The relation between normalisations.** `c_P = (2/N) c_L` with `N > 0`
multiplies by a positive number, so `sign(c_P) = sign(c_L)` and
`sign(g_P) = sign(g_L)` channel by channel. **A label therefore cannot
depend on which normalisation it was computed in** — checked explicitly
rather than assumed.

## 5. Known failure modes

1. **Mixing normalisations.** Pairing `+G/N**2` with `-G/4` compares a
   `P`-normalised number with an `L`-normalised one. Magnitudes so
   paired are not comparable; the pinned note records this. Signs are
   unaffected, and only signs are used here.
2. **Treating `g = 2c` as algebra.** It is a convention. A note that
   loses the citation turns a ruling into an apparent identity.
3. **Reading Layer 2 as a bound-state result.** See §6.
4. **Importing `G_c`.** The criticality result concerns a different
   quantity; attempting to reconcile it with `g` is a category error the
   specification warns against explicitly.
5. **Hard-coding `g = 2c` or the labels in the implementation.** That
   would make the outputs independent of the rulings they claim to
   consume. The implementation therefore parses both rulings out of
   `DECISION_LOG.md` and fails if either is absent, and the tests mutate
   the parsed mapping to confirm the outputs move with it.

## 6. What this note does not say about a composite vector

**A repulsive label in a `ψ̄ψ` channel does not settle whether a
composite vector exists.** Convention II says so in its own text, and
the reason is that a mean-field channel-character label is not a
bound-state or pole calculation. The question would require its own
analysis, and may involve a differently paired channel that this note
does not examine.

**Nor does an attractive label establish that condensation occurs.**
That depends on the full quadratic kernel `Γ⁽²⁾(0) = 1/g − Π(0)`, the
fermion determinant, stability, and the critical coupling — none of
which is computed here.

## 7. The diquark channel is still blocked

**This note does not touch the particle–particle channel**, and the
channel picture is not complete without it. The pinned derivation
established that the obstruction is not the charge-conjugation matrix
`C` — that is fixed up to a scalar which cancels in the paired product —
but three conventions the frozen material does not fix:

    eta in psibar^c = eta psi^T C^-1      not frozen
    particle-particle Grassmann ordering  not frozen
    diquark operator normalisation        not frozen

`η` appears once in the paired product and flips the coefficient sign,
so the diquark channel character is not determined by anything available
here. **The two rulings consumed above do not unblock it**: they supply
an exponent mapping and a sign-to-label rule, neither of which is a
particle–particle operator definition.

## 8. Pre-registered verdicts

    Layer 1a control   c reproduced exactly per channel, both
                       normalisations. GATING; disagreement is a stop.
    Layer 1b           g = 2c per channel with the sign as tabulated in
                       3.2, and real-HS admissibility yes/no/no.
    Layer 2            ATTRACTIVE / REPULSIVE / REPULSIVE.
    Scalar control     ATTRACTIVE. GATING; anything else is a stop.
    Diquark            unchanged, still blocked on three conventions.

**Registered before execution.** If the implementation disagrees with
any line above, the disagreement is the finding and the note is wrong,
not the output.

## 9. The exact scripts that implement this

    scripts/p2_channel_character_layers.py
    tests/test_p2_channel_character_layers.py
    results/P2-PHASE-01/channel-character-layers/layers.json

## 10. Scope

Model: the original model — the frozen `U(N)` chiral interaction, not an
extension, an EFT, or a numerical proxy.

It registers no gate and changes no status. It selects no
Hubbard–Stratonovich channel; `OPEN-AC-1` remains the PI's. It freezes
no diquark convention. It does not update the programme registry. It
modifies no frozen or pinned artifact. It revisits neither `G_c`, the
exploratory positions, nor the parameter-domain draft.
