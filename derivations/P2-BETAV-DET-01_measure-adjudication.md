# `P2-BETAV-DET-01` — which determinant the vector effective action requires

**Kind:** adjudication. **It derives from measure theory and the repository's
frozen conventions. It evaluates no candidate numerically before its verdict is
committed, and it assembles no `k`-dependent quantity at any stage.**

**Evidence base:** `8108c29846adb3b69c4ea73ab66a1c04b66106dc`.

**`§0` through `§11` were written and committed at commit `3a`, before any
candidate was evaluated numerically. Any numerical appendix appears BELOW `§11`
as a clearly separated final section added at commit `3b`, and may not alter the
verdict.**

## 0. The verdict

> **`NOT DETERMINABLE`**

**The repository's frozen conventions do not fix the field-space metric that
defines the functional integration measure, and the three candidate determinants
differ precisely by a power of that metric's determinant.** `§6` names the
missing convention exactly.

**AND A RIDER THAT CHANGES WHAT THE VERDICT COSTS.** The difference between the
candidates is **ultralocal in the background and independent of the mass**, so by
`CONVENTIONS.md:20`'s own definition of `Z` — *the coefficient of the induced
Einstein–Hilbert term `∫√g R`* — **it cannot contribute to `Z`, and therefore
cannot contribute to `β_s`.** `§7`.

**So the object `Γ_vector` requires is undetermined, and the quantity the
programme extracts from it is invariant under the undetermined choice.** Those
are two different statements and `§8` keeps them apart.

## 1. What was established before this task, and what was not

**`RECON-01a` landed, and `RECON-01a`'s integration re-verified against the
landed code's own definitions:**

    K1 + m²G1 = G1(D1 + m²)
    det(K1 + m²G1) = det G1 · det(D1 + m²)

**with `logdet(G1) = 0.0000000000` flat and `−1.1338458300` at amplitude `0.08`
on a curved background.** Re-verified again here as this task's `A4` premise:
the relative residual of the identity is `0.000e+00` flat and `6.434e-17`
curved.

**THAT IS ARITHMETIC AND NOTHING MORE.** It says the two determinant
representations differ by `det G1`. **It does not say where that factor belongs.**

**An earlier statement of mine — in the `RECON-01a` integration report — said the
mixing "did not leave the physics; it moved into `det G1`". That is one step
stronger than what was established**, and this specification's `§0` is right to
retract it. **The identity licenses "the two representations differ by
`det G1`"; it does not license "the physics is in `det G1`".**

## 2. What `det G1` actually is

**Derived from the landed construction's own definition of `G1`, not assumed.**

`proca_curved._vector_mass_metric` builds `G1` **block-diagonal in the site
index**, with the `(x; μ,ν)` block equal to `√g(x) g^{μν}(x)`. So

    det G1 = ∏_x det[ √g(x) g^{μν}(x) ]

and per site, with `g ≡ det g_{μν}` and `√g = g^{1/2}` in four dimensions,

    det[ √g g^{-1} ] = (√g)^4 · det(g^{-1}) = g² · g^{-1} = g

**Therefore**

    det G1 = ∏_x det g(x)          log det G1 = Σ_x log det g(x)

**Three properties follow, and all three are load-bearing later:**

    (P1)  ULTRALOCAL — a product over sites with no coupling between sites and
          no difference operator anywhere in it.
    (P2)  MASS-INDEPENDENT — G1 = √g g^{μν} contains no m. Not approximately;
          m does not appear in its definition.
    (P3)  BACKGROUND-DEPENDENT — it is 1 at h = 0 and not 1 otherwise, which is
          why this question is not vacuous.

**(P1) and (P2) are read off the definition. (P3) is `A4`'s measurement.**

## 3. The Gaussian integral with a general field-space metric

**This is standard continuum functional-integral formalism. IT IS NOT A
REPOSITORY FREEZE and `§5` says so again where it matters.**

Let `𝔊` be the field-space metric — the positive-definite bilinear form that
defines the norm on field fluctuations,

    ‖δA‖² = δA · 𝔊 · δA

and hence the integration measure. The covariant measure is fixed by requiring
the Gaussian in that norm to be normalised:

    DA ≡ (det 𝔊)^{1/2} ∏_{x,μ} dA_μ(x)     up to a field-independent constant

**For a quadratic action `S = ½ A·K·A`,**

    Z = ∫ DA e^{−S} = (det 𝔊)^{1/2} (det K)^{−1/2}

    Γ ≡ −log Z = ½ log det K − ½ log det 𝔊

**`K` here is the HESSIAN OF THE ACTION and nothing else.** In the landed
construction that is `K_total = K1 + m²G1`, because `S1` as discretised is
exactly `½ A·(K1 + m²G1)·A`. **There is no choice at this step**: the Hessian is
whatever the action's second variation is.

**Substituting the identity of `§1`:**

    Γ = ½ log det G1 + ½ log det(D1 + m²) − ½ log det 𝔊                (★)

**EVERY AMBIGUITY IN THE PROBLEM IS THE LAST TERM.** The first two are fixed by
the action and by arithmetic.

## 4. The three candidates are three choices of one object

**`(★)` reduces the pre-registered verdict space to a single question — what is
`𝔊`?**

    𝔊 = G1        Γ = ½ log det(D1 + m²)
                  the det G1 factors cancel exactly          OPERATOR-DETERMINANT

    𝔊 = 𝟙         Γ = ½ log det(K1 + m²G1)
                  the Cartesian measure on the components    HESSIAN-DETERMINANT

    𝔊 = anything  Γ = ½ log det(D1 + m²) + ½ log(det G1 / det 𝔊)
    else          an explicit measure term survives          MEASURE-EXPLICIT
                  with coefficient +½ on log det G1 and −½ on log det 𝔊

**THE THREE VERDICTS ARE NOT THREE DIFFERENT PHYSICAL CLAIMS. They are three
values of one unspecified input.** That is worth stating plainly, because it
means the adjudication cannot be settled by comparing the candidates to each
other — **they are not rivals; they are images of `𝔊` under `(★)`.**

## 5. What the repository fixes, and what it does not

### 5.1 The search, re-run — a NULL RESULT

**`CONVENTIONS.md` is 1406 lines. Searched for the path-integral measure, the
field-space metric, and a change-of-variables Jacobian. Terms and counts:**

    jacobian                  0        path integral            0
    path-integral             0        functional               0
    field space               0        field-space              0
    integration variable      0        inner product            0
    inner-product             0        ultralocal               0
    generating functional     0        partition function       0
    volume element            0        DeWitt (as a metric)     0

    measure                  21        norm*                   17
    det*                     20

**All 21 `measure` hits classified: `:14` is the LOOP measure `∫d⁴p/(2π)⁴`;
`:22` uses "measured in units of the cutoff"; the remaining 19 are at lines 289
to 1367 and are GOVERNANCE text about measurement discipline** — Amendment M,
verification records, merge-guard line counting. **None is a functional
measure.**

**All 17 `norm*` hits: `:20`, `:28`, `:33`, `:88`–`:123`, `:1157` are
normalisation of `Z`, of generators, and of species coefficients; the rest are
`normative`/`normally`.** **None is a field-space norm.**

**The only `DeWitt` occurrence is `:16`'s "Seeley–DeWitt coefficient" — a
heat-kernel coefficient, not the DeWitt field-space metric.**

**MEASURED: NO LINE OF `CONVENTIONS.md` ADDRESSES THE PATH-INTEGRAL MEASURE, THE
FIELD-SPACE METRIC, OR A CHANGE-OF-VARIABLES JACOBIAN.** The null result is the
finding.

### 5.2 `:14`, `:19`, `:21` in full

    :14  | Fourier transform | `f(x) = ∫ d⁴p/(2π)⁴ e^{ipx} f̃(p)`; loop measure
         `∫ d⁴p/(2π)⁴`. |

    :19  | Massive-vector (Proca) structure | `Z_{s=1,m} =
         det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)`, with the vector
         Laplacian `Δ^{(1)}` having `E^{μ}{}_{ν}=R^{μ}{}_{ν}` (`tr E = R`) and
         the Stueckelberg scalar `Δ^{(0)}` having `E=0`. This determinant
         structure is taken as an input from the paper; the coefficient it
         implies is what we compute. |

    :21  | Species coefficient `β_s` | Coefficient of `m² ln m²` in `Z(m²)`.
         Computed from `a_1`: `β_s = −p_s (4π)^{−2} (tr a_1 / R)`, where `p_s`
         is the log-det prefactor of the species (`+1/2` per bosonic
         `det^{−1/2}` factor, `−1/2` per `det^{+1/2}` factor / fermion loop).
         Reported both as a raw value (this convention) and as
         convention-independent ratios … |

**`:14` is the MOMENTUM-SPACE LOOP measure — the measure on `∫d⁴p` inside a
loop integral, not the measure on the space of field configurations.** They are
different objects; `:14` does not constrain `𝔊`.

### 5.3 Does `:19`'s silence constrain the answer?

**NO, AND FOR THREE SEPARATE REASONS. This is the criterion's own question and
it deserves each of them.**

**FIRST — `:19` says of itself that it is an INPUT, not a derivation:** *"This
determinant structure is taken as an input from the paper; the coefficient it
implies is what we compute."* **A structure taken from a paper carries that
paper's conventions, including whatever measure convention the paper used and did
not state here.** Reading its silence as "no measure factor" attributes to the
repository a choice the repository copied without recording.

**SECOND — `:19` IS A CONTINUUM STATEMENT AND ITS LATTICE REALISATION IS EXACTLY
WHAT IS IN QUESTION.** `Δ^{(1)}` there is the continuum vector Laplacian
identified by `E^μ_ν = R^μ_ν`, a curvature endomorphism. **The landed
construction has no `R^μ_ν` in it at all**; it has a lattice field-strength
Hessian and a mass metric. **Which lattice object is "the same thing as" `:19`'s
`Δ^{(1)}` is a construction question, and `RECON-01a` answered it by choice `C5`
and not by derivation.** `§9` returns to this.

**THIRD — silence about a factor is not a statement that the factor is absent.**
`:19` writes a ratio of determinants with no measure factor written. **In the
continuum, the measure factor for a 1-form is `det(√g g^{μν})^{1/2}`, which is
`(∏_x det g)^{1/2}` — a quantity that is IDENTICALLY 1 in flat space.** A
continuum formula written for a curved background but *checked* in flat space
would look exactly like `:19` whether the factor is there or not. **`:19`'s
silence is consistent with all three verdicts and discriminates none of them.**

**So `:19` is the line most obviously about determinants and it does not carry
the verdict.** `§9` records that this is the second time in this programme that
the most obviously relevant convention was not the load-bearing one.

## 6. The verdict, and the missing convention named precisely

> **`NOT DETERMINABLE`**

**By `§4`, the verdict is entirely determined by `𝔊`. By `§5.1`, the repository
fixes no property of `𝔊` whatsoever.** Not its existence, not its form, not
whether it is ultralocal, not its power of `√g`.

### 6.1 The missing convention, stated exactly

**What is missing is one line of `CONVENTIONS.md` of this form:**

> *The functional integration measure for a 1-form field `A_μ` is defined by the
> field-space metric `‖δA‖² = ∫d⁴x √g g^{μν} δA_μ δA_ν`, with
> `DA = (det 𝔊)^{1/2} ∏ dA_μ(x)`; equivalently the lattice measure is
> `∏_x (det g(x))^{1/2} ∏_{x,μ} dA_μ(x)`.*

**— or an explicit statement of a different `𝔊`, or an explicit statement that
the measure is Cartesian in the components `A_μ(x)`.** **Any one of the three
would settle it. The repository contains none of the three.**

**Note what is NOT missing.** The action is fixed, the Hessian is fixed, the
identity is arithmetic, and `(★)` is standard formalism. **The single missing
input is the norm on field fluctuations.**

### 6.2 What standard formalism would say, kept separate

**Standard continuum practice takes the DeWitt ultralocal metric on 1-forms to
be `𝔊 = √g g^{μν}`** — the unique ultralocal, diffeomorphism-covariant metric
built from `g` alone, up to a field-independent constant. **Under that choice
`𝔊 = G1` and `(★)` gives `OPERATOR-DETERMINANT`.**

**THAT IS TEXTBOOK, NOT REPOSITORY, AND IT IS RECORDED HERE AS TEXTBOOK.** This
programme's whole method is that a convention counts when the repository freezes
it. **A derivation that silently relabelled standard practice as a frozen
convention would be exactly the failure this line exists to prevent**, and it
would have produced a confident `OPERATOR-DETERMINANT` verdict resting on a
premise nobody reviewed.

**So: standard formalism points at `OPERATOR-DETERMINANT`; the repository points
nowhere; the verdict is `NOT DETERMINABLE`.**

### 6.3 What each ruling would commit the programme to

    OPERATOR-DETERMINANT  (𝔊 = G1)
        Commits the programme to the DeWitt ultralocal 1-form measure, hence to
        a measure that is background-dependent and whose Jacobian cancels the
        mass metric exactly.  Consistent with standard continuum practice.
        Commits every later determinant in the vector sector to being read as an
        OPERATOR determinant, and requires the same treatment of the
        compensating scalar — whose own mass metric is G0 = diag(√g), a
        DIFFERENT matrix.  A ruling that fixes the vector measure and leaves the
        scalar measure unstated would reopen this question one species over.

    HESSIAN-DETERMINANT  (𝔊 = 𝟙)
        Commits the programme to a Cartesian measure on the field components
        A_μ(x).  This is not diffeomorphism-covariant: the components of a
        1-form are not scalars, so a component-wise flat measure privileges the
        coordinate frame.  Anyone ruling this way should say why coordinate
        dependence is acceptable here.

    MEASURE-EXPLICIT  (𝔊 anything else)
        Commits the programme to a stated coefficient.  From (★) the coefficient
        of log det G1 in Γ is +½ and of log det 𝔊 is −½, so the surviving term
        is ½ log(det G1 / det 𝔊).  Nothing in the repository fixes 𝔊, so this
        verdict is only reachable by a PI ruling that supplies it.

**Whoever rules should also rule for the scalar sector at the same time.** The
same question arises there with `G0 = diag(√g)` in place of `G1`, and
`RECON-01b` needs both.

## 7. The rider: why the undetermined choice does not reach `β_s`

**This is derived, and it rests on a repository line rather than on standard
formalism.**

**By `§2`, `det G1` is ULTRALOCAL (P1) and MASS-INDEPENDENT (P2). Any candidate
`𝔊` that is itself ultralocal and built from the background metric alone shares
both properties.** So the difference between any two candidates is

    Γ_candidate − Γ_candidate′ = Σ_x F(g(x))

**for some function `F` of the background at a single site — no mass, no
difference operator, no coupling between sites.**

**NOW APPLY `CONVENTIONS.md:20`, WHICH DEFINES WHAT `Z` IS:**

> *the coefficient of the induced Einstein–Hilbert term `∫√g R` … The `m²ln m²`
> piece defines the species coefficient: `Z ⊃ β_s · m² ln m²`.*

**TWO INDEPENDENT REASONS THE DIFFERENCE CANNOT REACH `β_s`, and either alone
suffices:**

**(A) IT CANNOT REACH `Z`.** `Σ_x F(g(x))` contains no derivative of the
background. In the continuum it is `∫d⁴x` of a function of `g` at a point — a
cosmological-constant-type term proportional to `∫√g`. **`R` requires two
derivatives of the metric, so an ultralocal functional cannot contribute to the
coefficient of `∫√g R`.** On the lattice the same statement is that an
ultralocal term contributes to the graviton two-point function at order `q⁰` and
not at order `q²`, and `Z` is the `q²` coefficient.

**(B) IT CANNOT REACH THE `m² ln m²` PIECE.** Even granting a contribution to
`Z`, the difference carries no `m` at all, so its `m² ln m²` coefficient is zero
identically.

**THEREFORE `β_V` IS INVARIANT ACROSS THE THREE CANDIDATES.**

**THE BOUNDARY OF THIS CLAIM, STATED.** It holds for any `𝔊` that is ultralocal
and mass-independent. **A field-space metric that coupled neighbouring sites, or
that contained `m`, would break argument (A) or (B) respectively.** No such
metric is standard and none is proposed here, **but the invariance is a
conditional statement and the condition is named.**

## 8. What this implies for `RECON-01b` — and it is not what a bare `NOT DETERMINABLE` implies

**`RECON-01b` IS NOT BLOCKED FOR THE RATIO TARGET.**

**By `§7`, the species coefficient the programme extracts is the same whichever
determinant is scanned.** So the scan may proceed, on one condition:

> **`RECON-01b` must NAME the object it scans, and record that the naming is a
> stated choice rather than a repository ruling.**

**WHAT REMAINS BLOCKED, and it is not nothing:**

    the ABSOLUTE Γ_vector          undetermined by an m-independent,
                                   background-dependent additive term
    the induced COSMOLOGICAL       exactly where the ambiguity lands, by §7(A)
      CONSTANT
    any claim that a computed      such a claim would inherit the unstated
      Γ is "the" effective action  measure choice

**`§0` of the governing specification asserts that `RECON-01b` cannot begin until
this is settled, and that a scan run first "would return a number belonging to
whichever determinant happened to be picked".** **The first half of that is too
strong and the second half is true but harmless for the ratio:** the number does
belong to whichever determinant was picked, **and the `m² ln m²` coefficient of
that number is the same either way.** Reported as a specification defect in the
report, not resolved here.

**AND THE SPECIFICATION'S ACTUAL CONCERN SURVIVES INTACT, in a different place.**
Its worry is that a scan could "look clean precisely because `C5` removes the
mixing from the object scanned". **That is a worry about the transverse and
longitudinal SUBSPACES, not about the determinant** — and `RECON-01a` established
that `D1 + m²` has no `T`/`L` mixing while `K1 + m²G1` does. **A scan of `D1+m²`
therefore cannot exhibit a mixing artefact even if one is physically present.**
**That is a real hazard, it is not the determinant question, and this
adjudication does not dispose of it.**

## 9. The four sources, and which carried what

**`§3` of the governing specification names four sources and asks which is
load-bearing. The honest answer separates the verdict from the consequence.**

    (i)   the continuum Proca functional measure
          POINTS AT OPERATOR-DETERMINANT via the DeWitt metric, but it is
          standard formalism and not a repository freeze — §6.2.
          Load-bearing for what the answer would be; not for what the
          repository determines.

    (ii)  G1 as CANDIDATE lattice field-space metric
          NOT DETERMINED.  G1 demonstrably appears as the mass matrix and the
          inner-product matrix in the landed action, and that is all that was
          established.  APPEARING IN THE ACTION DOES NOT MAKE IT THE MEASURE:
          the action's Hessian and the measure's metric are independent inputs,
          and (★) uses them at different points.  I did not assume they
          coincide, and nothing in the repository says they do.

    (iii) the change-of-variables Jacobian
          Between the component parametrisation and A ↦ G1^{1/2}A the Jacobian
          is det(G1)^{1/2} — EXACTLY the disputed factor.  So (iii) RESTATES
          the question in other words rather than answering it.  Useful as a
          consistency check on §4 and useless as evidence.

    (iv)  CONVENTIONS.md:19 and :21
          :19 does not constrain, for the three reasons of §5.3.  :21 fixes the
          PREFACTOR per determinant factor (±½) but presupposes which
          determinants are being taken — it is downstream of this question, not
          upstream of it.

**LOAD-BEARING FOR THE VERDICT: NONE OF THE FOUR. That is precisely why the
verdict is `NOT DETERMINABLE`.**

**LOAD-BEARING FOR THE CONSEQUENCE: `CONVENTIONS.md:20`, WHICH IS NOT AMONG THE
FOUR.** It is the line that says what `Z` is — the coefficient of `∫√g R` — and
it is what makes `§7`'s argument (A) a repository statement rather than my
opinion about what ought to matter.

**`SIGN-01` found that the convention most obviously labelled a convention was
not the one carrying the result. THE SAME PATTERN HOLDS HERE AND ONE STEP
FURTHER:** `:19` is the line most obviously about determinants and it carries
nothing; **the line that carries the useful part of the answer is `:20`, which
is about a definition of `Z` and was not in the specification's list of places to
look.**

## 10. Dependence on `RECON-01a`'s six construction choices

**`RECON-01a` fixed six conventions `CONVENTIONS.md` does not fix. `Rule 16`'s
fourth junction asks whether this verdict depends on any of them. It does, and
differently for the verdict and the rider.**

    THE VERDICT (NOT DETERMINABLE) — INDEPENDENT of all six.
        It is a statement about what CONVENTIONS.md contains.  No construction
        choice could make the repository contain a measure convention.

    THE CANDIDATE FRAMING — DEPENDS ON C5.
        C5 is what creates D1 = G1^{-1}K1 as a named object at all.  Without
        C5 there is one determinant, that of the action's Hessian, and the
        question would not arise in this form.  C5 did not create the ambiguity
        — the measure was unstated before RECON-01a — but it is what made the
        ambiguity VISIBLE, by writing down two objects where the repository had
        written one.

    THE RIDER (§7's invariance) — DEPENDS ON C2 AND C4, NOT ON C5.
        §2 derives det G1 = ∏_x det g(x) from G1 being BLOCK-DIAGONAL IN THE
        SITE INDEX with block √g g^{μν}.  That is C2 (site-centred geometric
        factors) together with C4 (exact matrix inverse and √g = √det g).  A
        link-centred or plaquette-centred discretisation could give a G1 that
        couples neighbouring sites, and det G1 would then not be manifestly
        ultralocal — which is precisely the condition §7 names as the boundary
        of the invariance claim.

**SO THE INVARIANCE IS CONDITIONAL ON A CONSTRUCTION CHOICE, NOT ON THE
REPOSITORY, AND IT IS REPORTED AS CONDITIONAL.** A future construction that
changed `C2` would have to re-derive `§7`. **The verdict itself would be
unaffected.**

## 11. What this adjudication does not establish

- **It does not establish which measure is correct.** It establishes that the
  repository does not say, names the missing line, and records that standard
  formalism would answer `OPERATOR-DETERMINANT` if the programme chose to adopt
  it.
- **It adds no number and changes no number.** An adjudication is a decision
  about what the theory means. Whichever way a PI rules, no measurement in the
  repository moves.
- **It does not dispose of the `T`/`L` mixing hazard** (`§8`), which is a
  different concern that `C5` genuinely does create.
- **It does not settle the scalar sector.** The same question arises with
  `G0 = diag(√g)`, and `RECON-01b` needs both.
- **It evaluated no candidate before this verdict was committed, and it
  assembles no `k`-dependent quantity at any point.**

---

## 12. Post-freeze numerical appendix

**ADDED AT COMMIT `3b`, AFTER `§0`–`§11` WERE COMMITTED AT `3a`. IT DID NOT
ALTER THE VERDICT AND COULD NOT HAVE: the verdict is `NOT DETERMINABLE` because
`CONVENTIONS.md` contains no measure convention, and no number can change what a
file contains.**

**It reports `logdet` values for individual objects. It assembles no
`k`-dependent quantity, touches no scalar determinant, and forms no ratio.**

**Purpose: `§7`'s argument (B) turns on the difference between the candidates
being mass-independent, and `§7`'s argument (A) turns on `det G1` being
ultralocal. Both were derived in `§2` from the definition of `G1`. Both are
checkable, so they are checked.**

    L = 4, curved background at amplitude 0.08

     m²      logdet(D1+m²)      logdet(K1+m²G1)    difference        logdet(G1)
     0.09     925.9542509006     924.8204050706   −1.133845829998  −1.133845829998
     0.25    1208.0451629768    1206.9113171468   −1.133845829997  −1.133845829998
     0.50    1413.9251043501    1412.7912585201   −1.133845829999  −1.133845829998
     1.00    1643.0660491438    1641.9322033138   −1.133845829997  −1.133845829998
     2.00    1911.8028799288    1910.6690340988   −1.133845829998  −1.133845829998

    spread of the difference over m²          2.728e-12
    spread of logdet(G1) over m²              0.000e+00
    max |difference − logdet(G1)|             1.415e-12

**(P2) CONFIRMED. The two candidate determinants differ by a constant as `m²`
runs over a factor of twenty-two, and that constant is `logdet(G1)`.** The
residual spread is at the level of the `LU` factorisation's accumulated error on
a `1024 × 1024` matrix whose `logdet` is of order `10³`.

    ULTRALOCALITY, checked directly
      logdet(G1) from the full 1024 × 1024 matrix    −1.133845829998
      Σ_x log det g(x), computed site by site        −1.133845829998
      absolute difference                             1.688e-14

**(P1) CONFIRMED. `det G1` is exactly the product over sites of `det g(x)`**, as
`§2` derived from the block-diagonal construction.

**WHAT THIS APPENDIX DOES NOT DO.** It does not compare any candidate to any
target, does not assemble the determinant combination the gate names, and does
not vary any determinant power. **It confirms two properties of the DIFFERENCE
between the candidates; it says nothing about which candidate is right, which
remains `NOT DETERMINABLE` per `§6`.**
