# `P2-PHASE-01` — diquark channel character, carrying both `eta` signs

**Status:** derivation. Registers no gate and changes no gate status.
`P2-PHASE-01` remains `PROPOSED`. No convention is frozen here: `eta`, the
particle–particle Grassmann ordering and the diquark operator
normalisation are all left exactly as unfrozen as they were found.

**Authority for carrying both signs:** the PI ruling of 2026-08-09,
`DECISION_LOG.md`, *"The charge-conjugation phase `eta` is not selected;
both signs are computed"*. That ruling addresses the sign ambiguity the
channel-character derivation exposed. It does not characterise the full
phase freedom, and neither does this note.

**Reading order.** §1 is the control that everything else depends on. §2
re-establishes the three blockers. §3 settles `C`. §4 is the
particle–particle rearrangement. §5 is the answer to the diagnostic
question, and §6 says what is still unfrozen after this note.

---

## 1. Particle–hole control

Everything below uses the same frozen inputs and the same crossing
machinery as the particle–hole computation already in the repository, so
the control comes first: if the machinery cannot reproduce the known
particle–hole coefficients, no particle–particle result from it is
trustworthy.

Recomputed from the frozen Fierz block and the frozen canonical
coefficient, in normalisation **L** (coefficient of
`(psibar lam(0) Gamma psi)^2`):

    canonical per-family coefficient, read from the freeze   G/(2*N)

    direct scalar          c_S = G/(2*N)          sign +1
    operator level, s_G applied once at operator use:
      S  0        P  0        V  -G/4        A  -G/4        T  0

`c_S > 0` and `c_V = c_A = -G/4` reproduce. The control passes, so the
particle–particle results below rest on machinery that is known to give
the right answer where the answer is known.

**A structural contrast worth carrying forward:** in the particle–hole
rearrangement `V` and `A` survive with **equal** coefficients. In the
particle–particle rearrangement of §4 they survive with **opposite**
ones. The two rearrangements are different crossings of the same frozen
interaction and there is no reason for them to agree; the contrast is
recorded because it is the sort of thing a reader would otherwise assume.

---

## 2. The three blockers, re-established rather than inherited

The channel-character derivation reported three missing definitions. This
note does not take that on trust. Searching the pinned material —
`derivations/P2-PHASE-01_channel_character.md` and
`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`, raw UTF-8,
case-insensitive substring counts, no normalisation:

    term                     channel_character.md   phaseA_freeze.md
    'eta'                            13                    4
    'Grassmann'                       5                    2
    'ordering'                        5                    0
    'compound_index_order'            1                    1
    'diquark'                         5                    0
    'charge conjugation'              2                    0

The nine lines of `channel_character.md` that mention `eta` are quoted in
the results artifact. The load-bearing ones:

>     psibar^c = eta psi^T C^-1          -> lambda^-1 psibar^c   (eta a sign convention)

>     The sign/phase `eta` in `psibar^c = eta psi^T C^-1` appears **once**
>     in the paired product, so it multiplies the pp coefficient by `eta`
>     and **flips its sign** for `eta = -1`. Nothing in the frozen material
>     fixes `eta`.

>     under the un-frozen charge-conjugated-field convention `eta`, and the
>     frozen material fixes neither `eta` nor the pp Grassmann ordering nor the
>     diquark normalisation.

**All three are confirmed unfixed:**

- **`eta`.** No value appears anywhere in the frozen material. The
  ruling of 2026-08-09 declines to supply one and prescribes carrying
  both `eta = +1` and `eta = -1`.
- **The particle–particle Grassmann ordering.** The freeze fixes
  `compound_index_order = [dirac_family, internal_family, component]`
  and `grassmann_crossing_sign = -1`, and the latter is stated for the
  particle–hole exchange
  `(alpha,beta,gamma,delta) -> (alpha,delta,gamma,beta)`. A
  particle–particle pairing is a different permutation of the same four
  Grassmann factors; nothing in the freeze declares a target ordering
  for it. **Confirmed unfixed.**
- **The diquark operator normalisation.** Absent from the frozen
  material entirely. **Confirmed unfixed.**

None is in fact fixed, so §2's STOP condition is not met and the
computation proceeds.

---

## 3. `C` and its residual freedom

The defining relation, treated as a linear system on the sixteen entries
of `C` in the frozen Euclidean representation:

    C gamma_mu^T C^-1 = -gamma_mu        equivalently   C gamma_mu^T + gamma_mu C = 0

**Solution space: complex dimension exactly 1.** Every admissible `C` is
`lambda C_0` for one nonzero complex `lambda`; there is no further
discrete freedom. The representative obtained,

    C_0 = [[ 0, 1, 0, 0],
           [-1, 0, 0, 0],
           [ 0, 0, 0,-1],
           [ 0, 0, 1, 0]]

satisfies `C_0^T = -C_0`, `C_0^dagger C_0 = Id4`, `det C_0 = 1`, and the
defining relation for all four `mu`.

**The residual scalar cancels, and this is demonstrated rather than
cited.** A particle–particle rearrangement places `C` and `C^-1` in the
two conjugate factors exactly once each:

    psi^c    = C psibar^T             ->  lambda    psi^c
    psibar^c = eta psi^T C^-1         ->  lambda^-1 psibar^c

so any Dirac structure sandwiched between them carries
`lambda^{+1} lambda^{-1} = 1`. Checked three ways on the explicit
matrices: `(lambda C_0)(lambda C_0)^-1 = C_0 C_0^-1`; and
`(lambda C_0) gamma_mu^T (lambda C_0)^-1 = C_0 gamma_mu^T C_0^-1` for
all four `mu`; and the assembled coefficients of §4 contain no `lambda`.

**`C` is therefore not the obstruction**, which is what the earlier note
concluded and what this note independently re-derives. Note what this
does *not* license: a settled `C` says nothing about `eta`, the ordering,
or the normalisation, each of which is an independent convention.

---

## 4. The particle–particle rearrangement, for both `eta`

### 4.1 The structure being computed

The frozen canonical interaction is

    L_int = (G/(2*N)) * Sum_A [ (psibar lam^A psi)^2 + (psibar lam^A I gamma5 psi)^2 ]

Written with every index explicit, one canonical term is

    psibar_{a,alpha} lam^A_{ab} Gamma_{alpha,beta} psi_{b,beta}
      * psibar_{c,gamma} lam^A_{cd} Gamma_{gamma,delta} psi_{d,delta}

with `Gamma = Id4` for the scalar term and `Gamma = I gamma5` for the
pseudoscalar term. The internal generators contract to

    Sum_A lam^A_{ab} lam^A_{cd} = 2 delta_{ad} delta_{cb}

A **particle–particle** rearrangement groups the two `psibar` together
and the two `psi` together — Dirac pairing `(alpha,gamma)` and
`(beta,delta)`, internal pairing `(a,c)` and `(b,d)`. This is a different
crossing from the particle–hole one the freeze fixes a sign for.

### 4.2 Diquark bilinears, and where `eta` enters

Using the definitions of §3,

    Delta_a     = psibar^c Gamma_a psi = eta * psi^T C^-1 Gamma_a psi
    Deltabar_a  = psibar Gamma_a psi^c =       psibar Gamma_a C psibar^T

`Delta` carries `eta`; `Deltabar` does not, because in Euclidean
signature `psi` and `psibar` are independent Grassmann variables and
`psibar^c` is a separate definition rather than a conjugate of `psi^c`.
So the product carries it **once**:

    Deltabar_a Delta_b = eta * (psibar Gamma_a C psibar^T)(psi^T C^-1 Gamma_b psi)

This reproduces the earlier note's counting by construction rather than
by assertion.

### 4.3 The Dirac decomposition

Writing `M_a = Gamma_a C` and `N_b = C^-1 Gamma_b`, the sixteen products
`M_a ⊗ N_b` form a basis of the 256-dimensional space of four-index Dirac
tensors, because `{Gamma_a}` is complete and `C` is invertible. The
decomposition

    Gamma_{alpha,beta} Gamma_{gamma,delta}
        = Sum_{a,b} f_{ab} (Gamma_a C)_{alpha,gamma} (C^-1 Gamma_b)_{beta,delta}

is therefore unique, and with the basis normalised so that
`trace(Gamma_a Gamma_b) = 4 delta_{ab}` — verified for all 256 pairs —
the coefficients follow from a single trace:

    f_{ab} = (1/16) * trace[ (C^-1 Gamma_a Gamma) * (Gamma Gamma_b C)^T ]

**Every decomposition is verified by reconstruction**, not by the trace
formula alone: `Sum f_{ab} M_a ⊗ N_b` is rebuilt entry by entry and
compared with the original tensor on all 256 components. Both canonical
terms reconstruct exactly.

The result is **diagonal in the family basis** — every `f_{ab}` with
`a` and `b` in different families vanishes — and uniform within each
family. Per component:

    family    scalar term    pseudoscalar term    sum
    S            -1/4             +1/4              0
    P            -1/4             +1/4              0
    V            +1/4             +1/4             +1/2
    A            -1/4             -1/4             -1/2
    T            +1/4             -1/4              0

**`S`, `P` and `T` cancel exactly between the two canonical terms; `V`
and `A` reinforce, with opposite signs.** The cancellation is not a
coincidence of arithmetic: the frozen interaction is the chirally
symmetric combination `S^2 + P^2`, and the particle–particle image of a
chirally symmetric interaction lands in the chirally covariant `V` and
`A` diquark structures. **This matters for §7**: a result in which
everything vanishes and a result in which three of five families vanish
look similar at a glance and are not the same thing.

### 4.4 Statistics and the internal channel

`psi_{b,beta} psi_{d,delta}` is antisymmetric under the simultaneous
exchange `(b,beta) <-> (d,delta)`, so a Dirac-symmetric structure pairs
with an internal-antisymmetric one and vice versa. Computed on the
explicit matrices, `M_a` and `N_a` have the **same** symmetry type in
every family — a consistency condition that had to hold and was not
assumed:

    family    Gamma_a C     C^-1 Gamma_a    internal channel
    S         antisym       antisym         internal-symmetric
    P         antisym       antisym         internal-symmetric
    V         sym           sym             internal-antisymmetric
    A         antisym       antisym         internal-symmetric
    T         sym           sym             internal-antisymmetric

The two surviving families therefore live in **different** internal
channels: the induced `V` diquark is internally antisymmetric, the
induced `A` diquark internally symmetric.

The internal factor `2 delta_{ad} delta_{cb}` splits between those two
channels as

    internal-symmetric channel        +2
    internal-antisymmetric channel    +2

**verified for `N = 2, 3, 4, 5` and identical in both.** The load-bearing
fact is not the value but the **equality of sign**: the internal
projection contributes no relative sign between families, so the relative
sign of the `V` and `A` coefficients is the one computed in §4.3. The
magnitude is in any case subject to the unfrozen normalisation below.

### 4.5 The assembled coefficients

Carrying the three unfrozen quantities as symbols — `eta` for the
charge-conjugated-field phase, `s_pp` for the particle–particle Grassmann
ordering sign, `nu` for the diquark operator normalisation:

    c_pp(family) = (G/(2*N)) * 2 * s_pp * eta * nu * f(family)

    S   0
    P   0
    V   + G*eta*nu*s_pp/(2*N)
    A   - G*eta*nu*s_pp/(2*N)
    T   0

**These are the coefficients, and they are labelled as
assumption-dependent because they are.** `s_pp` and `nu` are not supplied
here. What can be said about them:

- **`s_pp`.** For the target ordering
  `(psibar_alpha psibar_gamma)(psi_beta psi_delta)`, reached from
  `psibar_alpha psi_beta psibar_gamma psi_delta` by one adjacent
  transposition, `s_pp = -1`. Two further orderings this note can define
  — exchanging the two `psibar`, or exchanging the two `psi` — each give
  `s_pp = +1`; the ordering
  `(psi_beta psi_delta)(psibar_alpha psibar_gamma)` gives `s_pp = -1`.
  **These are the alternatives this note can define. They are not a
  claim that the admissible ordering space consists only of them** — the
  frozen material says no ordering is fixed, and it does not enumerate
  which are admissible. The same caution the ruling applies to `eta`
  applies here.
- **`nu`.** Three cases, kept apart because collapsing them would send a
  magnitude question to a verdict it does not deserve:
  **a positive real rescaling changes only the magnitude and leaves the
  channel character untouched; a sign or phase convention with
  `nu` real and negative flips the character; a genuinely complex `nu`
  makes a simple attractive/repulsive label inapplicable, because the
  coefficient is then not real and has no sign.**

Evaluated at the adjacent-transposition ordering `s_pp = -1` with
`nu = +1`, and applying `g = 2c` and the attraction/repulsion labels of
the 2026-08-08 rulings in `DECISION_LOG.md`:

    eta = +1     V   c = -G/(2*N)   g = -G/N   REPULSIVE
                 A   c = +G/(2*N)   g = +G/N   ATTRACTIVE

    eta = -1     V   c = +G/(2*N)   g = +G/N   ATTRACTIVE
                 A   c = -G/(2*N)   g = -G/N   REPULSIVE

**Every label in that table is conditional on `s_pp = -1` and `nu = +1`,
neither of which is frozen.** Changing either flips all four.

---

## 5. The diagnostic question

The ruling asked whether the two `eta` representatives give the same
channel character or opposite ones. **The answer is OPPOSITE**, and —
this is the part that makes it worth having — **the answer does not
depend on either remaining unfrozen definition.**

The reason is structural rather than numerical. Each coefficient has the
form `c = K * eta` with `K = (G/(2*N)) * 2 * s_pp * nu * f` containing
every unfrozen quantity except `eta` itself. For any real nonzero `K`,

    sign(c(eta = +1)) = sign(K)        sign(c(eta = -1)) = -sign(K)

so the two are opposite whatever `K` is. Computed explicitly, the ratio
`c(eta = -1) / c(eta = +1)` is exactly `-1` in both surviving families,
with `s_pp` and `nu` still symbolic and cancelling.

**Therefore, in the words of the ruling: the diquark channel character
depends on an unresolved sign convention.** This is the outcome the
ruling was designed to expose. It is a real result, and a more useful one
than a single label would have been, because a single label would have
concealed the dependence rather than measuring it.

**What is well-defined and what is not**, stated separately because they
are different claims:

    well-defined, independent of eta, s_pp and nu
      S, P and T carry no induced diquark coefficient at all
      V and A are the only surviving families
      V and A always carry OPPOSITE characters to each other
      flipping eta flips the character of every surviving family

    NOT well-defined
      whether the induced V diquark is attractive or repulsive
      whether the induced A diquark is attractive or repulsive
      the magnitude of either coefficient

**Two scope limits on the verdict.** It requires `nu` real and nonzero;
for complex `nu` there is no attractive/repulsive label to compare and
no verdict is licensed. And `S`, `P` and `T` vanish for both `eta`, so
they have no character in either case — that is **not** a "same" answer,
it is the absence of a quantity to compare.

---

## 6. What remains unfrozen after this note

- **`eta`.** Not selected. Both representatives are carried and reported,
  per the ruling. The residual phase freedom beyond the `eta = ±1` sign
  is still uncharacterised — the ruling says so and this note adds
  nothing to it.
- **The particle–particle Grassmann ordering.** Not selected. Four
  orderings are defined and evaluated above; the admissible space is not
  enumerated.
- **The diquark operator normalisation.** Not selected. Its three cases
  are distinguished, not resolved.

Whether any of the three should be frozen, and to what, is a PI decision
this note informs and does not take.

---

## 7. Comparison with the earlier exploratory attempt

The authority records an exploratory diquark projection, performed
outside this repository, that **returned zero in all four families** and
is treated there as a failed attempt rather than a finding.

**That failure mode did not recur here.** `V` and `A` carry non-zero
coefficients `± G*eta*nu*s_pp/(2*N)`. But the result is not far from it:
**three of the five families do vanish**, by exact cancellation between
the scalar and pseudoscalar canonical terms (§4.3). A projector wrong by
one sign — for instance one that gave the pseudoscalar term the scalar
term's signs — would cancel `V` and `A` as well and return zero
everywhere, which is presumably what happened.

This is why §4.3's decompositions are **verified by reconstruction on all
256 tensor components** rather than trusted from the trace formula, and
why §1's control runs first. A vanishing result and a broken projector
look alike, and only an independent check distinguishes them.

---

## 8. What this note does not do

It registers no gate and changes no status; `P2-PHASE-01` remains
`PROPOSED`. It freezes no convention and supplies none silently.

**It makes no statement about whether a massive composite vector can
form, in either `eta` case.** A channel-character label is the sign of a
coefficient in a rearranged interaction; a bound state or a pole is a
different calculation, and computing the particle–particle channel does
not change that. This is a disclaimer, not a result.

**It does not state that the channel picture is complete.** It computes
one crossing of one frozen interaction.

It selects no Hubbard–Stratonovich channel. The 2026-08-09 ruling
selected the scalar channel for mean-field work; that is untouched here.
It does not revisit `G_c`, the exploratory stationary positions, or the
parameter-domain draft, and it consumes neither the quarantined
`-3.2(5)` value, nor the suspended `P2-BETAV-CIRC-01` result, nor the
historical Finding 5 extraction.

## 9. Repository inputs read

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    results/P2-CHANNEL-FREEZE/fierz_matrix.json
    derivations/P2-PHASE-01_channel_character.md
    derivations/P2-PHASE-01_channel_character_layers.md
    results/P2-PHASE-01/channel-character-layers/layers.json
    DECISION_LOG.md
    scripts/P2-CHANNEL-FREEZE/gamma_algebra.py
