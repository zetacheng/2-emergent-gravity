# `P2-PHASE-01` — the chirality census

**Status:** derivation. Registers no gate, changes no gate status, freezes
no convention, and introduces **no new programme coefficient or
channel-character result**. `P2-PHASE-01` remains `PROPOSED`. Any
coefficients below are diagnostic reproductions used to test a structural
explanation.

**What is being explained.** The frozen `S² + P²` interaction decomposes
with `S`, `P` and `T` absent in both the particle–hole and the
particle–particle pairing. The programme holds that as two separate
numerical facts. This note tests whether a counting argument over
chirality explains it.

**Provenance boundary.** The particle–hole coefficients are pinned from
`main`. **The particle–particle coefficients are not an input to this
note**: they live on unintegrated branches, which this task is forbidden
to read, so the particle–particle side below is established
**structurally and independently**, from the projector algebra alone.

**Reading order.** §1 is the classification, because a projector-placement
error there inverts everything after it. §2 is the factorisation, §3 the
census, §4 the two chirality-support tables, §5 the falsification test,
§6 what the argument does not explain.

---

## 1. The classification, and where the bar goes

**The placement convention, stated before anything is computed.**

    P_L = (1 - g5)/2        P_R = (1 + g5)/2        g5 = g0 g1 g2 g3

    psi_X   = P_X psi
    psibar_L = psibar P_R           <-- the bar FLIPS the projector

so a particle–hole bilinear translates as

    psibar_X Gamma psi_Y   <->   P_Xbar Gamma P_Y

and in particular `psibar_L Γ psi_R` corresponds to `P_R Γ P_R`, **not**
to `P_L Γ P_R`. **An earlier informal analysis made exactly this error**,
and §4's tables are computed rather than quoted for that reason.

A particle–particle bilinear carries no bar:

    psi_X^T C^-1 Gamma psi_Y   <->   P_X^T C^-1 Gamma P_Y

**Computed, not assumed**, in both representations of §7:

    C g5^T C^-1 = +g5          hence     P_X^T C^-1 = C^-1 P_X

so the transpose introduces **no** chirality flip on the
particle–particle side.

**This is the whole of the inversion, and it is worth stating precisely
because the specification's §1 states it slightly more strongly than the
algebra supports.** The two projector tables in §4 have **identical**
non-zero patterns: diagonal for `S`, `P`, `T` and off-diagonal for `V`,
`A`, in both pairings. What differs is the translation to field labels —
the bar flips one side and nothing flips the other. So:

    the inversion is NOT an independent algebraic fact about C;
    it is the bar-flip on the particle-hole side, together with the
    ABSENCE of a flip on the particle-particle side, and the absence
    is what C g5^T C^-1 = +g5 delivers.

Had the relation been `C g5^T C⁻¹ = −g5`, then `P_X^T C⁻¹ = C⁻¹ P_Xbar`,
the pp side would have flipped too, and the two classifications would
have **agreed** in field labels. The frozen relation is therefore
load-bearing exactly as §1 says — but as the thing that *prevents* a
second flip, not as the thing that *causes* the inversion.

---

## 2. Step A — the factorisation, verified

Rank-4 Dirac tensors, `T[a,b,c,d] = Γ₁[a,b] Γ₂[c,d]`, summed over the two
canonical operators. With the frozen `P = iγ₅`:

    frozen:  I(x)I + (i g5)(x)(i g5)  =  I(x)I - g5(x)g5
    no-i:    I(x)I +    g5 (x)   g5   =  I(x)I + g5(x)g5

    residual || frozen - 2[P_R(x)P_L + P_L(x)P_R] ||_max  =  0.000e+00
    residual || no-i   - 2[P_R(x)P_R + P_L(x)P_L] ||_max  =  0.000e+00

**Both identities are exact.**

**One refinement of the specification's Step 1, reported rather than
absorbed.** §1 writes the frozen case as
`S² + P² = 4(ψ̄_L ψ_R)(ψ̄_R ψ_L)`. That is correct as an **operator**
statement — the two bilinears are Grassmann-even and commute, so the two
orderings are the same operator and `2 + 2 = 4`. It is **not** an identity
on the ordered rank-4 tensor:

    residual || frozen - 4 P_R(x)P_L ||_max  =  2.000e+00

The ordered-tensor identity is the symmetrised `2[P_R⊗P_L + P_L⊗P_R]`
above. Nothing in the argument depends on which form is used, but a
reader checking the identity slot by slot would find the factor-4 form
failing, so the distinction is recorded.

---

## 3. Step C3 — the census, computed

Coefficients of each chiral-pair component of the source tensor:

    frozen  S^2 + P^2
      (psibar_L psi_R) x (psibar_R psi_L)      2
      (psibar_R psi_L) x (psibar_L psi_R)      2
      (psibar_L psi_R) x (psibar_L psi_R)      0
      (psibar_R psi_L) x (psibar_R psi_L)      0

    no-i    S^2 + (gamma5 term)^2
      (psibar_L psi_R) x (psibar_R psi_L)      0
      (psibar_R psi_L) x (psibar_L psi_R)      0
      (psibar_L psi_R) x (psibar_L psi_R)      2
      (psibar_R psi_L) x (psibar_R psi_L)      2

    frozen census   psibar_L , psi_R , psibar_R , psi_L    one of each
    no-i census     psibar_L , psi_R , psibar_L , psi_R    two of each, doubled
                    (and the mirror term with L <-> R)

**Exactly as the specification's Step 2 states**, and now measured.

---

## 4. Step C — the two chirality-support tables, complete

**All four entries are reported in each table, including those symmetry
makes redundant.** A table with entries omitted because they follow is
half-inferred; the cost of computing them is negligible.

### C1 — particle–hole, `P_X Γ P_Y`

    fam   P_L G P_L   P_L G P_R   P_R G P_L   P_R G P_R    ph type
    S     nonzero     0           0           nonzero      OPPOSITE-chirality
    P     nonzero     0           0           nonzero      OPPOSITE-chirality
    V     0           nonzero     nonzero     0            SAME-chirality
    A     0           nonzero     nonzero     0            SAME-chirality
    T     nonzero     0           0           nonzero      OPPOSITE-chirality

Reading the entries through `psibar_X Γ psi_Y ↔ P_Xbar Γ P_Y`:
`P_R Γ P_R` is `ψ̄_L Γ ψ_R` and `P_R Γ P_L` is `ψ̄_L Γ ψ_L`. So `S`, `P`,
`T` carry only opposite-chirality `ψ̄ψ` pairs and `V`, `A` only
same-chirality ones.

### C2 — particle–particle, `P_X^T C⁻¹ Γ P_Y`

    fam   LL          LR          RL          RR           qq type
    S     nonzero     0           0           nonzero      SAME-chirality qq
    P     nonzero     0           0           nonzero      SAME-chirality qq
    V     0           nonzero     nonzero     0            OPPOSITE-chirality qq
    A     0           nonzero     nonzero     0            OPPOSITE-chirality qq
    T     nonzero     0           0           nonzero      SAME-chirality qq

Here `LL` means `ψ_L^T C⁻¹ Γ ψ_L`; there is no bar and no flip.

**The two classifications are inverted in field labels**, as §1 claims,
and §1's mechanism is refined in §1 of this note.

**C2 requires no Fierz crossing, no Grassmann ordering and no diquark
normalisation.** It is a statement about which chirality pairs a kernel
can carry. **No particle–particle coefficient decomposition is performed
in this note and no slot map is chosen** — both confirmed explicitly,
which is what allows the pp side to be addressed while those conventions
remain unfrozen.

### Step 5 — the conclusion, reached twice

    PH:  the frozen census re-pairs, under exchange, into
         (psibar_L psi_L) and (psibar_R psi_R)  -- SAME-chirality ph
         -> only V and A are available; S, P, T cannot form

    PP:  the two psi fields of the frozen census are psi_L and psi_R
         -> an OPPOSITE-chirality qq pair
         -> only V and A are available; S, P, T cannot form

**Both select `V` and `A`, from the same census, through inverted
classifications.** `S`, `P` and `T` are absent because nothing can form
them, not because numbers cancel.

---

## 5. Step D — the falsification test, prediction recorded first

**The criterion, stated in a form applicable without decomposing.**

Write the interaction's rank-4 tensor in the chiral projector basis as a
sum of terms `K₁ ⊗ K₂` with `K ∈ {P_L, P_R}`. Each term fixes the
chirality of the four fields `ψ̄_a ψ_b ψ̄_c ψ_d`. The particle–hole
exchange re-pairs them as `(ψ̄_a ψ_d)(ψ̄_c ψ_b)`. For each term the two
exchange pairs have a definite type:

    every term gives SAME-chirality exchange pairs
        -> only V and A can appear; S, P and T must vanish
    every term gives OPPOSITE-chirality exchange pairs
        -> only S, P and T can appear; V and A must vanish
    terms of BOTH kinds present
        -> no family is excluded

**The predictions below are recorded in this note, which is commit 3. The
script that computes them is commit 4. The git history is the evidence of
ordering**, and no Step D decomposition had been run when this note was
written.

**D0, control — frozen `S² + P²`.** Census: one of each. Exchange pairs
`(ψ̄_L ψ_L)` and `(ψ̄_R ψ_R)`, both SAME.
**PREDICT: `V` and `A` non-zero; `S`, `P`, `T` zero.**

**D1 — the no-`i` interaction `S² + (γ₅ term)²`.** Census: doubled,
`(ψ̄_L ψ_R)(ψ̄_L ψ_R)` and the `L ↔ R` mirror. Exchange pairs
`(ψ̄_L ψ_R)` and `(ψ̄_L ψ_R)`, both OPPOSITE.
**PREDICT: `S`, `P`, `T` non-zero; `V` and `A` zero.**

**D4 — chosen by the executor: the pseudoscalar-only interaction
`(ψ̄ iγ₅ ψ)²`, with the frozen `i`.**

*Why this one.* The criterion's two exclusion branches are the easy ones.
A criterion that only ever forbids things can look successful without
discriminating, and this task's stated failure mode is an explanation
that fits because it was fitted. **The branch that predicts NO exclusion
is where a criterion invented after seeing the answer would most likely
fail**, so that is the branch worth testing. The pseudoscalar-only tensor
is `−γ₅⊗γ₅`, which in the projector basis is

    -P_R(x)P_R + P_R(x)P_L + P_L(x)P_R - P_L(x)P_L

containing **both** one-of-each and doubled terms, so the third branch
applies.
**PREDICT: all five families non-zero; nothing excluded.**

Four of the five families could have come out zero, so the prediction is
not a safe one.

---

## 6. Step E — what the argument does not explain

- **The inter-channel sign.** Particle–hole gives `V = +A`; the
  particle–particle pairing gives `V = −A`. **A census counts fields; it
  does not distinguish them.** This note does not attempt it and the
  argument is silent on it.
- **The magnitudes.** The census says which families can form, not with
  what coefficient. `−G/4` is not derived here.
- **Anything about states.** Which operators can form is not a
  bound-state or pole calculation.
- **The relative weight of the two exchange pairs**, and hence the `V`/`A`
  degeneracy in the particle–hole channel. Both are same-chirality and the
  census does not separate them.
- **The particle–particle coefficients.** Not computed here, by design.

---

## 7. Representation independence

Chirality is not a property of the representation, so §4's tables were
computed in two independently written Euclidean Hermitian gamma sets:

    frozen_factory     the repository's own gamma_factory, metric (1,1,1,1)
    independent_kron   g0 = kron(s1,s1)  g1 = kron(s1,s2)
                       g2 = kron(s1,s3)  g3 = kron(s2,I2)

In both: `g5² = I`, `P_L + P_R = I`, `P_L P_R = 0`, the `C` null space has
dimension 1, `C g5^T C⁻¹ = +g5`, and `P_X^T C⁻¹ = C⁻¹ P_X`.

**Both C1 and C2 come out identical in the two representations.** Had
they not, the classification would be representation-dependent and the
argument would fail; that is reported as the outcome rather than resolved
by choosing a representation.

---

## 8. What this note does not do

It registers no gate and changes no status. It selects no convention:
`η`, the particle–particle Grassmann ordering and the diquark
normalisation are untouched and remain unfrozen. It states nothing about
whether a composite vector exists or is absent — this is a structural
argument about which operators can form, not a bound-state calculation.
It does not state that the diquark channel is settled; the branches
carrying those coefficients are not integrated and were not read. It
selects no Hubbard–Stratonovich channel and does not revisit the
2026-08-09 rulings. It does not restate either coefficient table as a
result of its own.

**A note on what would not be evidence.** Projecting the frozen source
onto an LL/RR-type sector and finding zero is close to tautological:
`S² + P²` has no such component to begin with (§3 measures it as exactly
`0`). It is recorded there for completeness and is **not** offered as
support; §5 carries the falsification.

## 9. Repository inputs read

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    derivations/P2-PHASE-01_channel_character.md
    results/P2-PHASE-01/channel-character/channel_character.json
    results/P2-CHANNEL-FREEZE/fierz_matrix.json
    scripts/P2-CHANNEL-FREEZE/gamma_algebra.py

Nothing else was read. **Neither `gate/p2-diquark-both-eta` nor
`gate/p2-diquark-adjudication` was read**, per A1.
