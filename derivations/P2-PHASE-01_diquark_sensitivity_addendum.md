# `P2-PHASE-01` — sensitivity addendum to the diquark both-`η` derivation

**Status:** addendum. **This corrects nothing.** The both-`η` derivation
(`derivations/P2-PHASE-01_diquark_both_eta.md`) is right, uses the frozen
conventions, and states them. `P2-PHASE-01` remains `PROPOSED`. No
convention is frozen or selected here, and no coefficient is restated as a
new result.

**What it records.** The both-`η` derivation's family support — `c_S = c_P
= c_T = 0`, with `c_V = −c_A` non-zero — **rests on two of the frozen
conventions it uses.** A reader assessing how robust `c_S = c_P = c_T = 0`
is would not learn that from the derivation itself, because the derivation
has no reason to ablate a convention it correctly treats as fixed. **The
adjudication ablated them, and this addendum records what that showed.**

---

## 1. The sensitivity

**The two conventions.**

    the canonical pseudoscalar bilinear carries  i·γ₅
    the A and T family basis elements each carry an explicit factor of i

**The mechanism.** Because the pseudoscalar operator enters the rank-4
tensor twice,

    (i γ₅) ⊗ (i γ₅)  =  −(γ₅ ⊗ γ₅)

so dropping the `i` flips the sign of the whole pseudoscalar term. The two
canonical terms of `S² + P²` then **add where they would otherwise cancel,
and cancel where they would otherwise add.** Verified directly on the
frozen representation: the residual between the two sides above is exactly
`0`.

The `A`/`T` factor acts differently and more narrowly: the diagonal
coefficient `f_pp` carries `Γ_p` in **both** factors, so a factor `i` on
`Γ_p` multiplies `f_pp` by `i⁻² = −1`. **It flips the `A` and `T`
coefficients and nothing else.**

**The ablation's outcome**, from
`results/P2-PHASE-01/diquark-adjudication/adjudication.json`, per-component
family sums with one input changed at a time:

    rep   i on A/T   pseudoscalar Γ      S      P      V      A      T
    B     no         γ₅               -1/2   -1/2     0      0    -1/2
    B     no         iγ₅                 0      0   +1/2   +1/2     0
    B     yes        γ₅               -1/2   -1/2     0      0    +1/2
    B     yes        iγ₅                 0      0   +1/2   -1/2     0
    A     yes        iγ₅                 0      0   +1/2   -1/2     0
    A     no         γ₅               -1/2   -1/2     0      0    -1/2

**Restoring `i·γ₅` alone moves the surviving support from `S`/`P`/`T` to
`V`/`A`** (rows 1→2). **Restoring the `A`/`T` factor alone flips `A` and
`T`** (rows 2→4). Swapping the gamma representation with everything else
fixed changes nothing (rows 4 and 5 agree; rows 1 and 6 agree), so **the
representation is not causal** and the sensitivity is to the two
conventions, not to the algebra's presentation.

**So the family support is not a robust feature of "the `S² + P²`
interaction" in the abstract.** It is a feature of the frozen interaction
with the frozen basis.

## 2. Both conventions are FROZEN, not free

**This is not a newly discovered unfrozen dependence**, and it must not be
read as one.

Both are fixed by `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`, in
prose and in its machine block:

    P^A(x) ≡ Σ … ψ̄_{aα}(x) (λ^A)_{ab} (iγ₅)_{αβ} ψ_{bβ}(x)
    A=I*gamma(mu)*gamma5
    T=I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2

    "basis_id":"A","expression":"I*gamma(mu)*gamma5"
    "basis_id":"T","expression":"I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2"
    bilinear(lam(A),I*gamma5)**2

**The adjudication established which construction is the frozen one by
quotation, not by preferring a method.** The independent computation that
disagreed with the both-`η` branch had omitted both; that is why it
disagreed, and it is why the branch is right.

**The distinction this addendum insists on:**

    FROZEN and load-bearing        the canonical pseudoscalar's i·γ₅
                                   the i on the A and T basis elements
                                   — the result is SENSITIVE to these, and
                                     they are DECIDED

    STILL UNFROZEN                 η
                                   the particle–particle Grassmann ordering
                                   the diquark normalisation
                                   — these are UNDECIDED

**These two categories must not be compressed into a generic "convention
dependence".** A sensitivity to a decided convention is a fact about what
the result rests on. A dependence on an undecided convention is an open
question. **Only the second is unresolved.**

## 3. Why it is recorded anyway

A later reader assessing the robustness of `c_S = c_P = c_T = 0` needs to
know what it rests on. Three specific uses:

- **If the freeze is ever revisited** — and §D of the freeze contemplates a
  Phase-B contract — then whoever revisits it should know that the diquark
  family support moves under a change to the canonical pseudoscalar
  operator. That is not visible from the both-`η` derivation.
- **If another independent recomputation is attempted**, this is the pair
  of conventions to check first. The adjudication showed that omitting them
  reproduces a specific wrong answer, and that answer is recorded above.
- **Because "S, P and T vanish" is the kind of statement that travels.** It
  is short, memorable, and true only under the frozen conventions. **The
  provenance should travel with it.**

## 4. Relation to the chirality census on `main`

`derivations/P2-PHASE-01_chirality_census.md` explains the same vanishing
**structurally**: the frozen interaction supplies one field of each
chirality, the particle–particle pairing therefore offers an
opposite-chirality `qq` pair, and only `V` and `A` support that. `S`, `P`
and `T` are absent because nothing can form them.

**The census explains SUPPORT only.** It does not explain the coefficient
signs or magnitudes — its own Step E says so, and lists the inter-channel
sign and the magnitudes among the things it is silent on. **This addendum
does not claim the census explains the signs.**

**The two accounts are consistent and complementary**, and the relation is
worth stating precisely because it could otherwise look like a
duplication:

    the census      says WHICH families can form, from the chirality
                    content of the source — a structural statement
    the ablation     says the family support MOVES if the frozen
                    pseudoscalar operator changes — a sensitivity

**They agree on the same conventions being load-bearing.** The census's
own falsification test dropped the `i` and predicted, before computing,
that the support would move from `V`/`A` to `S`/`P`/`T`; it did. **So the
census independently reproduces the ablation's first row**, by a different
route and in the particle–hole channel. That agreement is the strongest
thing this addendum can say about the sensitivity: it is visible
structurally and numerically, in two channels, by two methods.

## 5. The independence claim, at the level the evidence licenses

The both-`η` derivation claims its `OPPOSITE` verdict is independent of the
two remaining unfrozen definitions — the pp Grassmann ordering and the
diquark normalisation — because every coefficient has the form `c = K·η`
with `K` holding those symbols, so they cancel in the ratio. Measured
ratios: `−1` for both `V` and `A`.

**What the adjudication contributes to that claim, stated exactly:**

- **It found no evidence against it.** `L3` — the slot map and its Grassmann
  permutation — was **IDENTICAL** between the two computations, so the
  discrepancy was **not** an ordering effect. Had it been, the branch's
  independence claim would have been in trouble.
- **It did not establish independence over untested admissible pp
  orderings.** No alternative slot map was tried. The adjudication's own
  case decision records that the ordering/index-map case does not apply,
  which is a statement about *this* discrepancy, not about the space of
  orderings.

**So the pp ordering question is open in both directions.** Nothing here
confirms it and nothing refutes it. **The negative result stays negative:**
an identical `L3` excludes the observed discrepancy from being evidence of
an ordering divergence, and excludes nothing else.

## 6. What remains unfrozen

    η                                    not selected; both representatives
                                         carried and reported, per the
                                         2026-08-09 ruling. The residual
                                         phase freedom beyond the ±1 sign
                                         is uncharacterised.
    the particle–particle Grassmann      not selected; four orderings
    ordering                             defined and evaluated on the
                                         branch, the admissible space not
                                         enumerated
    the diquark normalisation            not selected; its three cases
                                         distinguished, not resolved

Whether any should be frozen, and to what, is a PI decision this addendum
informs and does not take.

## 7. What this addendum does not do

**It corrects nothing.** It selects no convention. It restates no
coefficient as a new result — the values in §1 are the adjudication's
ablation, cited to show a sensitivity, not offered as a finding of this
addendum. It does not assign any absolute attractive or repulsive
character, and `OPPOSITE` remains a **relative** statement between the two
`η` representatives. It says nothing about composite states: which
operators can form is not a bound-state or pole calculation, and a
repulsive label in any channel does not imply a composite vector is
absent. It selects no Hubbard–Stratonovich channel and revisits no ruling.
It does not adjudicate the `P`-sign difference recorded in the
chirality-census integration, which remains unresolved.

## 8. Sources

    derivations/P2-PHASE-01_diquark_both_eta.md
    derivations/P2-PHASE-01_diquark_adjudication.md
    derivations/P2-PHASE-01_chirality_census.md
    results/P2-PHASE-01/diquark-both-eta/diquark.json
    results/P2-PHASE-01/diquark-adjudication/adjudication.json
    results/P2-PHASE-01/chirality-census/census.json
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
