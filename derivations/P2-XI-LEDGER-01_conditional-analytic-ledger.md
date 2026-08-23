# `P2-XI-LEDGER-01` — the conditional analytic ξ ledger (Phase 1)

    Kind            Derivation and construction. NOT a gate.
    Specification   specs/2026-08-23T0600Z_xi-ledger-01_v3.md
    Review          reviews/chatgpt/2026-08-23T0600Z_xi-ledger-01_v3.md
    Base            main @ 9eefe4c85c646b96ce334426598bc0e405f6e3d5
    Script          scripts/xi_ledger.py
    Tests           tests/test_p2_xi_ledger.py

**No gate status changes. `P2-PHASE-01` and SI-2 are untouched. No
`PASS`/`FAIL`/`INCONCLUSIVE` is emitted — this task has no verdict to give.**

**This task does not adjudicate `H-XI-SIGN-01`, and no sentence of this
artifact states or implies a status change for it.** The per-class table of §3
is data. Establishment or refutation requires the later reviewed specification
that `assumptions/H-XI-SIGN-01.md` names, which must operationally define
"coupling structure" and pre-register its discriminating test.

---

## 0. THE CONDITIONALITY — carried on every total in this artifact

**Every assembled number below is `ξ(G) | COND-1..4`.** The bare symbol `ξ(G)`
is not used for a number anywhere in this task's deliverables.

    COND-1  MEMBERSHIP = LANDED MEMBERSHIP ONLY. The assembled chain is the
            landed chain of P2-NORM-01 (:26):
                Z(m²) → β_s → 4G_c β_F → ξ_ind = 4Gβ_F(3−L).
            **The condensate scalar's own fluctuation loop is NOT included
            and NOT excluded on physical grounds** — it is an OPEN ledger row
            pending the PI's Q-M2 ruling
            (derivations/P2-XI-B0a_induced-xi-scope-assessment.md:615-618).

    COND-2  **The Hubbard–Stratonovich Jacobian/normalization term is NOT
            included and NOT asserted absent** — an OPEN ledger row pending
            the PI's Q-M3 disposition. The landed text requiring its
            inclusion if curvature-dependent is
            derivations/P2-FIERZSUM-01.md:451-460, via Q-M3 at
            derivations/P2-XI-B0a_induced-xi-scope-assessment.md:620-624.

    COND-3  Single mass, `L ≡ ln(Λ²/m²)` per CONVENTIONS.md:22. The
            multi-mass scenario `m_f ≪ m_V ≪ Λ` is recorded untested (Q-M4,
            assessment:626-628) and is not entered.

    COND-4  The composite vector's determinant structure is the Proca
            structure taken as an input convention (CONVENTIONS.md:19; Q-M5,
            assessment:630-632).

**An OPEN row is not a zero.** Reading any total below as if the OPEN rows
contributed nothing is the one misreading this artifact is built to prevent.

---

## 1. `M1` — provenance of the assembly chain

**Every node is quoted verbatim from the Base. Every downstream step of this
task uses these extracted bytes.** Each `path:line` resolves at
`9eefe4c85c646b96ce334426598bc0e405f6e3d5`.

### 1.1 The chain

`derivations/P2-NORM-01_normalization_chain.md:26`

```text
Z(m²)  ──►  β_s (coeff of m²ln m² in Z)  ──►  4 G_c β_F  ──►  ξ_ind = 4Gβ_F(3−L)
```

### 1.2 Both convention values of `4 G_c β_F`, each with the convention that owns it

`derivations/P2-NORM-01_normalization_chain.md:54-59`

```text
4. **The product `4 G_c β_F`.** Because `G_c` is `Z`-independent but `β_F`
   carries `R_Z`, the product inherits the `Z`-convention of `β_F` alone:
   ```
   4 G_c β_F = 1/3   (Z_here)      = 1/6   (Z_paper).
   ```
   The paper's `4·8π²/(192π²) = 1/6` is exact **in its own convention**. The
```

    Z_paper   4 G_c β_F = 1/6
    Z_here    4 G_c β_F = 1/3

### 1.3 The recorded survival-window boundaries, with convention assignment

`derivations/P2-NORM-01_normalization_chain.md:81-84`

```text
`ξ_ind = 4Gβ_F(3−L)` is negative for `L ≫ 1` whether the prefactor is `1/6` or
`1/3` (both positive, times `(3−L) < 0`). Only the survival-window boundary
moves — `m > 0.368Λ` (`1/6`) vs `m > 0.287Λ` (`1/3`) — and the paper notes both
are unattainable in the lattice scheme (`L` large). **The paper's central
```

    m > 0.368Λ   belongs to the 1/6 convention  (Z_paper)
    m > 0.287Λ   belongs to the 1/3 convention  (Z_here)

### 1.4 The `L` definition

`CONVENTIONS.md:22`

```text
| Definition of `L` | `L ≡ ln(Λ²/m²)`. The mass `m` is measured **in units of the cutoff `Λ`** (i.e. `Λ ≡ 1` unless a gate states otherwise), so `L = −ln m²` in those units. `ln m²` and `L` differ only by sign and the `ln Λ²` reference. |
```

### 1.5 The `β_s` definition and the `p_s` prefactor rule

`CONVENTIONS.md:21`

```text
| Species coefficient `β_s` | Coefficient of `m² ln m²` in `Z(m²)`. Computed from `a_1`: `β_s = −p_s (4π)^{−2} (tr a_1 / R)`, where `p_s` is the log-det prefactor of the species (`+1/2` per bosonic `det^{−1/2}` factor, `−1/2` per `det^{+1/2}` factor / fermion loop). Reported both as a raw value (this convention) and as convention-independent ratios `β_F/β_B`, `β_V/β_B`, `β_B(ξ)/β_B`. |
```

### 1.6 The three species coefficients and the ratio block

`derivations/P2-HK-01_heat_kernel_species.md:81-96`

```text
With `K ≡ (4π)^{−2} = 1/(16π²)` and `β_s = −p_s K (tr a_1/R)`:

```
β_B      = −(+½) K (1/6)      = −K/12  = −1/(192π²)
β_B(ξ)   = −(+½) K (1/6 − ξ)  = −K(1/6 − ξ)/2
β_F      = −(−½) K (−1/3)     = −K/6   = −1/(96π²)
β_V      = [−(+½)K(−1/3)] + [−(−½)K(1/6)] = K/6 + K/12 = K/4 = +1/(64π²)
```

### Ratios (convention-independent)

```
β_B(ξ)/β_B = (1/6 − ξ)/(1/6) = 1 − 6ξ
β_F/β_B    = (−K/6)/(−K/12)  = +2
β_V/β_B    = (K/4)/(−K/12)   = −3
```
```

### 1.7 The Proca-as-input convention

`CONVENTIONS.md:19`

```text
| Massive-vector (Proca) structure | `Z_{s=1,m} = det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)`, with the vector Laplacian `Δ^{(1)}` having `E^{μ}{}_{ν}=R^{μ}{}_{ν}` (`tr E = R`) and the Stueckelberg scalar `Δ^{(0)}` having `E=0`. This determinant structure is taken as an input from the paper; the coefficient it implies is what we compute. |
```

### 1.8 Supporting landed lines the decomposition of §2 rests on

`CONVENTIONS.md:16` — the `a_1` convention:

```text
| Heat-kernel expansion | `Tr e^{−τΔ} = (4πτ)^{−d/2} ∫ d^dx √g Σ_{k≥0} a_k(x) τ^k`, `d=4`. Indexing: `a_0 = tr 𝟙`, and `a_1 = tr[(1/6)R·𝟙 − E]` (the `R`-linear Seeley–DeWitt coefficient). This is the "`a_1`/`b_2`" in the τ-power indexing; some references call it `b_4`. |
```

`CONVENTIONS.md:17` — the action-level non-minimal coupling:

```text
| Curvature coupling of scalar | Non-minimal coupling term `½ ξ R φ²` in the action ⟹ `E = ξ R` for the scalar; minimal coupling is `ξ = 0`. The conformal value in `d=4` is `ξ = 1/6`. |
```

`derivations/P2-HK-01_heat_kernel_species.md:59-68` — the bundle-trace table:

```text
Let `d_s = tr 𝟙` (bundle dimension) and `e_s ≡ tr E / R`. Then
`tr a_1 / R = d_s/6 − e_s`.

| Species | det factor(s) | `d_s` | `E` | `e_s = tr E/R` | `tr a_1/R = d_s/6 − e_s` | `p_s` |
|---|---|---|---|---|---|---|
| Real scalar (minimal) | `det^{−1/2}` | 1 | 0 | 0 | `1/6` | `+½` |
| Non-minimal scalar `ξ` | `det^{−1/2}` | 1 | `ξR` | `ξ` | `1/6 − ξ` | `+½` |
| Dirac fermion | `det^{−1/2}` (squared op) | 4 | `(1/4)R·𝟙₄` | `1` | `4/6 − 1 = −1/3` | `−½` |
| Proca vector part | `det^{−1/2}` | 4 | `R^{μ}{}_{ν}` | `1` | `4/6 − 1 = −1/3` | `+½` |
| Proca scalar part | `det^{+1/2}` | 1 | 0 | 0 | `1/6` | `−½` |
```

### 1.9 Landed `L`-regime statements, extracted for the record

**Per §1a of the specification these are recorded, and do NOT alter the frozen
grid within this task.** None contradicts the grid's suitability, so `A3` does
not fire on this limb.

    derivations/P2-NORM-01_normalization_chain.md:81
        "`ξ_ind = 4Gβ_F(3−L)` is negative for `L ≫ 1`"
    CLAIMS.md:31
        "`4G_cβ_F = 1/6` (paper `Z` convention) and `ξ_ind<0` for `L≫1`"
    DECISION_LOG.md:124
        "unchanged: `ξ_ind < 0` for `L ≫ 1` in either convention."
    GATES.md:309
        "Pending. Physics unchanged: `ξ_ind<0` for `L≫1` either way; only the survival"
    GATES.md:1189 and derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md:220
        "result gives `ξ_ind < 0` for `L ≫ 1`, and the one computed vector channel is"
    results/P2-NORM-01/README.md:11
        "unchanged: `ξ_ind < 0` for `L ≫ 1` either way."
    paper/emergent_gr_paper_v2_15.tex:1238
        "$\xi_{\mathrm{eff}} > 1/6$ requires $L < 2$ in the most favorable"
    paper/emergent_gr_paper_v2_15.tex:1241
        "In the logarithmically induced regime $L \gg 1$, which is precisely"
    derivations/P2-XI-B0a_induced-xi-scope-assessment.md:395
        "**Finding: the term is landed, and its landed sense is `L ≫ 1`.**"

**The landed statements are qualitative (`L ≫ 1`) or single-point (`L < 2`);
none fixes a canonical finite grid.** That is why §1a of the specification
pre-registers one, and the grid below is that pre-registration, not a choice
made here.

    Range               L ∈ [0.5, 20]
    Representative pts  L ∈ {0.5, 1, 2, 3, 5, 10, 20}

---

## 2. `M2` — the curvature-coupling decomposition, and why it needs no new choice

### 2.1 The three classes

The landed `a_1` is `tr[(1/6)R·𝟙 − E]` (CONVENTIONS.md:16), and
`tr a_1/R = d_s/6 − e_s` with `e_s ≡ tr E/R` (P2-HK-01:59-60). Since
`β_s = −p_s K (tr a_1/R)` is **linear** in `tr a_1/R`, any additive split of
`tr a_1/R` induces an additive split of `β_s`. The specification's
pre-registered classes are that split:

    (i)   universal R/6      the `(1/6)R·𝟙` term — present for every bundle,
                             weighted by the bundle dimension `d_s`, carrying
                             no species coupling
    (ii)  endomorphism       the `−E` term where `E` is fixed by the species'
          (bundle)           OWN KINETIC OPERATOR: Lichnerowicz `(1/4)R·𝟙₄`
                             for Dirac (CONVENTIONS.md:18), `R^{μ}{}_{ν}` for
                             the Proca vector part (CONVENTIONS.md:19)
    (iii) explicit ξR        the `−E` term where `E = ξR` comes from an
                             ACTION-LEVEL non-minimal coupling `½ξRφ²`
                             (CONVENTIONS.md:17)

**`A2` does not fire, and the reason is recorded rather than assumed.** Classes
(ii) and (iii) are both `E` contributions in the landed `a_1`; what separates
them is fixed by landed text, not chosen here. `CONVENTIONS.md:18` and `:19`
derive their `E` from the species' kinetic operator — a Dirac field has
`E = (1/4)R·𝟙₄` because of Lichnerowicz, not because anyone chose it — while
`CONVENTIONS.md:17` introduces `E = ξR` from a term written into the action
with a free parameter. **Every landed species falls on exactly one side of that
line, and no species required a choice the landed text does not fix.**

**This three-class list is this specification's operationalization of Ruling
2's curvature-coupling axis.** The ruling names the axis; the classes are how
this task instantiates it on `a_1`'s own structure. **Any needed refinement of
the list is model-level and routes to the PI.**

### 2.2 The per-species × per-class coefficient table

Exact, in units of `K = 1/(16π²)`, with per-class signs shown. Derived
symbolically in `scripts/xi_ledger.py`; no value is transcribed from memory.

    species                universal R/6   endomorphism (bundle)   explicit ξR        total
    ---------------------------------------------------------------------------------------------
    minimal real scalar            −1/12                       0             0        −1/12
    non-minimal scalar ξ           −1/12                       0           ξ/2   ξ/2 − 1/12
    Dirac fermion                  +1/3                     −1/2             0         −1/6
    Proca vector (both factors)    −1/4                     +1/2             0         +1/4

The Proca row is the sum of its two determinant factors, kept separate in the
script as the landed table keeps them:

    Proca vector part (d=4, e=1, p=+½)     universal −1/3   endomorphism +1/2   subtotal +1/6
    Stueckelberg scalar (d=1, e=0, p=−½)   universal +1/12  endomorphism    0   subtotal +1/12

which reproduces P2-HK-01:87's own bracketing, `[−(+½)K(−1/3)] + [−(−½)K(1/6)]
= K/6 + K/12`.

### 2.3 Cross-checks against the `M1`-extracted values

**Evaluated as measurements, by symbolic equality. The recorded quantity is the
difference of the compared expressions, so a near-miss could not read as a
match.**

    quantity        assembled           landed (M1)         difference
    -----------------------------------------------------------------
    β_B             (−1/12) K           (−1/12) K           0
    β_F             (−1/6) K            (−1/6) K            0
    β_V             (+1/4) K            (+1/4) K            0
    β_B(ξ)          (ξ/2 − 1/12) K      (ξ/2 − 1/12) K      0
    β_F/β_B         2                   +2                  0
    β_V/β_B         −3                  −3                  0
    β_B(ξ)/β_B      1 − 6ξ              1 − 6ξ              0

**All seven differences are exactly zero.** `A3` does not fire on this limb.

---

## 3. `M3` — the ledger

Rows are the curvature-coupling classes of §2.1. **The MEMBERSHIP column takes
exactly one status per row, and the two OPEN rows carry an em-dash in every
numeric cell.**

    row (coupling-structure class)          landed contributions        sign   MEMBERSHIP
    ------------------------------------------------------------------------------------------------
    universal R/6                           β_F share: +1/3 K           +      LANDED
      the (1/6)R·𝟙 term of a_1              (assembled ledger uses
                                             the fermion determinant
                                             under COND-1)
    endomorphism (bundle)                   β_F share: −1/2 K           −      LANDED
      Lichnerowicz E = (1/4)R·𝟙₄
    explicit ξR                             none in the assembled       n/a    LANDED
      action-level ½ξRφ²                    chain: the condensate
                                             scalar enters only through
                                             m = y(v+χ̃), so its own ξ
                                             is not a free input here
    ------------------------------------------------------------------------------------------------
    condensate scalar's own                 —                            —     OPEN(Q-M2)
      fluctuation loop
    Hubbard–Stratonovich Jacobian /         —                            —     OPEN(Q-M3)
      normalization term
    ------------------------------------------------------------------------------------------------
    single-mass treatment                   L ≡ ln(Λ²/m²)               n/a    CONVENTION(Q-M4,
                                                                                single-mass)
    Proca determinant structure             det^{−1/2}(Δ⁽¹⁾+m²)·        n/a    CONVENTION(Q-M5,
                                            det^{+1/2}(Δ⁽⁰⁾+m²)                Proca)

**The two OPEN rows, with their `Q-M` items cited verbatim from the landed
assessment:**

`derivations/P2-XI-B0a_induced-xi-scope-assessment.md:615-618` — `Q-M2`:

```text
    Q-M2  Does the condensate scalar's own fluctuation loop enter the ξ
          ledger, and at what order? session_log_full.md:101 identifies it
          as the genuinely new object and counts it O(1) against the
          fermion's O(N); no landed statement settles whether it enters.
```

`derivations/P2-XI-B0a_induced-xi-scope-assessment.md:620-624` — `Q-M3`:

```text
    Q-M3  Does the Hubbard–Stratonovich decoupling's Jacobian or
          normalization contribute? derivations/P2-FIERZSUM-01.md:451-460
          states that any metric-, regulator- or curvature-dependent
          normalization "must be included in `ξ_ind`, not discarded as an
          irrelevant constant", and records the check as undone.
```

**No row is marked resolved, superseded, or estimated.** No sign, bound, or
magnitude is offered for either OPEN row anywhere in this task.

---

## 4. `M4` — the conditional total and the margin deliverable

### 4a. The assembled conditional total

Per the `M1`-extracted chain (§1.1) with the two `M1`-extracted convention
values (§1.2):

    ξ(G) | COND-1..4  =  4Gβ_F (3 − L)

    Z_paper  (4G_cβ_F = 1/6)     ξ(G) | COND-1..4  =  1/2 − L/6
    Z_here   (4G_cβ_F = 1/3)     ξ(G) | COND-1..4  =  1 − L/3

Evaluated symbolically and numerically over exactly the §1a range
`L ∈ [0.5, 20]` at exactly the §1a representative points, **and no others**.

### 4b. The survival comparison, as a CONDITIONAL reading

The landed threshold is `ξ_eff > 1/6` (`CONVENTIONS.md:17`'s conformal value;
`P2-NORM-01:83`'s window is its consequence). **Solving
`ξ(G) | COND-1..4 = 1/6` for `L`, and converting by `m = exp(−L/2)` from
`CONVENTIONS.md:22`:**

    convention   L boundary, derived   m/Λ = exp(−L/2), derived   landed value (M1)   agreement
    -------------------------------------------------------------------------------------------
    Z_paper      L = 2                 0.3678794412               m > 0.368Λ          0.368 = 0.368
    Z_here       L = 5/2               0.2865047969               m > 0.287Λ          0.287 = 0.287

**Both boundaries are derived from the assembly, not carried as input.** The
`L`-correspondences `L = 2` and `L = 5/2` reproduce §1a's stated `≈2.00` and
`≈2.50` exactly, and the masses reproduce the landed record to the three
decimal places the landed record carries. **No mismatch with the landed record,
so `A3` does not fire.**

**The reading is CONDITIONAL and is not a verdict.** It says where
`ξ(G) | COND-1..4` — a total assembled from landed membership only, with two
rows OPEN — stands relative to `1/6`. **It says nothing about where a complete
ledger would stand**, because two of its rows have no value.

### 4c. THE MARGIN DELIVERABLE

**Definition.** `|δξ_flip(L)|` is the size an additional ledger term would need
in order to move the conditional reading across the `1/6` threshold:

    |δξ_flip(L)| = | 1/6 − (ξ(G) | COND-1..4)(L) |

**Normalization, frozen in §1a before any evaluation:**

    r_margin(L) = |δξ_flip(L)| / F0 ,     F0 ≡ |4Gβ_F|

    F0 = 1/6  (Z_paper)        F0 = 1/3  (Z_here)

`F0` is the landed fermionic COEFFICIENT scale and is deliberately
`L`-independent. **The alternative normalization by the full `L`-dependent
fermion contribution `|4Gβ_F(3−L)|` vanishes at the pre-registered point
`L = 3` and is NOT used**; no other denominator was substituted at execution
time. **The absolute `|δξ_flip(L)|` is reported alongside `r_margin` at every
point**, so a reader can form any other ratio afterwards without this task
having chosen one on the evidence.

**`Z_paper` convention — `ξ(G) | COND-1..4 = 1/2 − L/6`, `F0 = 1/6`:**

        L    ξ(G)|COND-1..4          |δξ_flip|        r_margin   direction of the flip
      ----------------------------------------------------------------------------------------
      0.5    5/12   = 0.416666667    1/4  = 0.25      3/2 = 1.5  above 1/6; the added term
                                                                 would move it DOWN across
        1    1/3    = 0.333333333    1/6  ≈ 0.16667   1          above 1/6; DOWN across
        2    1/6    = 0.166666667    0                0          exactly at 1/6 — the boundary
        3    0                       1/6  ≈ 0.16667   1          below 1/6; UP across
        5    −1/3   = −0.333333333   1/2  = 0.5       3          below 1/6; UP across
       10    −7/6   ≈ −1.16666667    4/3  ≈ 1.33333   8          below 1/6; UP across
       20    −17/6  ≈ −2.83333333    3                18         below 1/6; UP across

**`Z_here` convention — `ξ(G) | COND-1..4 = 1 − L/3`, `F0 = 1/3`:**

        L    ξ(G)|COND-1..4          |δξ_flip|        r_margin     direction of the flip
      ------------------------------------------------------------------------------------------
      0.5    5/6    = 0.833333333    2/3  ≈ 0.66667   2            above 1/6; DOWN across
        1    2/3    = 0.666666667    1/2  = 0.5       3/2 = 1.5    above 1/6; DOWN across
        2    1/3    = 0.333333333    1/6  ≈ 0.16667   1/2 = 0.5    above 1/6; DOWN across
        3    0                       1/6  ≈ 0.16667   1/2 = 0.5    below 1/6; UP across
        5    −2/3   ≈ −0.666666667   5/6  ≈ 0.83333   5/2 = 2.5    below 1/6; UP across
       10    −7/3   ≈ −2.33333333    5/2  = 2.5       15/2 = 7.5   below 1/6; UP across
       20    −17/3  ≈ −5.66666667    35/6 ≈ 5.83333   35/2 = 17.5  below 1/6; UP across

**Units.** `ξ` is dimensionless, so `|δξ_flip|` is dimensionless and
`r_margin` is a pure ratio to the landed fermionic coefficient scale `F0`.

**WHAT THIS IS AND IS NOT.** `|δξ_flip(L)|` is **a property of the assembled
function**. It is the answer to "how large would an added term have to be".
**It is NOT a statement that the `Q-M2` or `Q-M3` terms have that size, that
sign, or any size or sign at all.** This task computes what WOULD change the
reading and does not estimate the open terms themselves. **Reading the table as
a bound on either open term inverts what it says.**

---

## 5. What this task does not establish

1. **No verdict.** No gate status changes; no `PASS`, `FAIL` or `INCONCLUSIVE`
   is emitted. `P2-PHASE-01` and SI-2 are untouched.
2. **No status for `H-XI-SIGN-01`.** The §2.2 table is data. Nothing here
   establishes or refutes the hypothesis, and nothing here bears on its status.
3. **No estimate, bound, or sign guess for the `Q-M2` or `Q-M3` terms.** They
   are OPEN, valueless, and returned as they arrived.
4. **No unconditional total.** Every number above is `ξ(G) | COND-1..4`. The
   verdict-grade reading is Phase 2, which does not exist until the PI rules on
   membership.
5. **No multi-mass extension (`Q-M4`) and no alternative vector structure
   (`Q-M5`).**
6. **No cross-reference edits to the landed assessment or to any other landed
   file.** This task adds its own artifacts only.

---

## 6. Open questions, recorded

    O-1  Q-M2 and Q-M3 remain open and are the two OPEN ledger rows. Their
         disposition is the PI's, and Phase 2 does not exist until it is made.
    O-2  Whether the §2.1 three-class list needs refinement is model-level and
         routes to the PI. It was not needed here — no landed species required
         a choice the landed text does not fix — but the list was pre-registered
         against the landed species set, not proved complete for species not
         yet in it.
    O-3  The §1a grid is a sampling choice pre-registered in the specification,
         not a landed object. No landed text fixes a canonical finite grid;
         §1.9 records what landed text does say.
