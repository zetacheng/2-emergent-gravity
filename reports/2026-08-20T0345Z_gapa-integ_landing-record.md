# Landing record — `P2-GAPA-INTEG`

**Transport only.** Every statement below is one the reviewed result already
made. **Nothing here is a new result, and no rule is created.**

    Source   science/gapa-bridge-01   02a83403e359941dcf1fff3c7690d1fc778b277e
    Base     f76387474204a4cadda5275995eaa031ccdca8bf
    Fork     a6be149f531c4a55ad331f26412a16472b803628

---

## 1. The result, with its condition, in the same statement

    OUTCOME   IDENTIFICATION HOLDS — for q ∥ e₀, and at no other momentum
              direction tested.

**This statement is this record's, composed to §5.1's requirement that the
outcome carry its condition. The reviewed result's own words are quoted in §3
below and are marked as quotations there.**

**The condition is part of the statement, not a footnote to it.** Measured, at
`derivations/P2-GAPA-BRIDGE-01_basis-identification.md:295-302`:

    momentum direction              ‖P2map − Q_recipes‖_F      equal
    e0, the axis TT_RECIPES fix     4.228e-16                  YES
    e1                              2.404e+00                  no
    e2                              2.404e+00                  no
    e3                              2.404e+00                  no
    diagonal (1,1,1,1)              2.121e+00                  no
    e0 rescaled, q0 = 13.0          4.228e-16                  YES

**The failure at other directions is `O(1)`, not marginal** — `2.4` and `2.1`
against a `1e-10` tolerance. `TT_RECIPES` are hard-coded for `q ∥ e₀` and do
not rotate with `q`; the Barnes–Rivers projectors are built from whatever `q`
they are given.

**`e₀` is the only direction the extraction uses** — `mlog_coeff.py:38` sets
`q = (q0, 0.0, 0.0, 0.0)` — **so the identification, holding for `q ∥ e₀`,
covers every use of `TT_RECIPES` in the repository.** It is independent of
`|q₀|`: established symbolically, and confirmed by the rescaled row.

**Convention scope.** The repository fixes one Barnes–Rivers convention,
implemented twice and identically. **The result, for `q ∥ e₀`, holds for that
convention, which is every convention the repository has.**

---

## 2. Both conjuncts

### First conjunct — subspace equality, for `q ∥ e₀`

For `q ∥ e₀`, the Barnes–Rivers TT block and the span of `TT_RECIPES` are the
same five-dimensional subspace of Sym²(R⁴).

    D1  SYMBOLIC (sympy, symbolic q0)
        rank Im(P2) = 5;  P2 idempotent;  P2 symmetric;
        P2 + P1 + P0s + P0w = I₁₀ exactly;
        each of the five recipes fixed by P2, P2 v = v;
        rank[ Im(P2) | recipes ] = 5

    D2  NUMERICAL (numpy, SVD)
        tolerance                              1e-10
        ‖P2map − Q_span(recipes)‖_F            4.228e-16   → equal
        rank(P2 map)                           5
        singular values of [P2map | recipes]   1.4142 ×5, then 1.055e-16, 0.0

**Established as subspace equality, not as dimension matching.** Every recipe
lies in `Im(P2)`, the five are independent, and `rank Im(P2) = 5` leaves no
room for anything else. **The two methods agree.**

### Second conjunct — the block-by-block correspondence, for `q ∥ e₀`

**For `q ∥ e₀`, the Barnes–Rivers non-TT blocks are the five components
`EXT-01` enumerates as discarded — as a correspondence, component by
component.** The condition is the same one §1 records and applies here for the
same reason: the Barnes–Rivers blocks are built from `q`, and the discarded
components `D1`–`D4` are defined by carrying the axis index `0`.

    component   ‖P2 v‖        fixed by
    D1          0.000e+00     P0w        the weak scalar block
    D2          0.000e+00     P1         the vector block
    D3          0.000e+00     P1
    D4          0.000e+00     P1
    D5          9.615e-17     P0s        the strong scalar block

**Each discarded component is annihilated by `P2` and fixed by exactly one
non-TT block**, and the three blocks partition the five as `1 + 3 + 1`:

    P0w  ↔  {D1}
    P1   ↔  {D2, D3, D4}
    P0s  ↔  {D5}

**And the correspondence is onto:**
`‖(P1 + P0s + P0w) − Q_span(D1…D5)‖_F = 4.191e-16`. Neither side carries a
direction the other lacks.

**This is not the statement that both complements are five-dimensional.** Two
distinct five-dimensional subspaces can share an ambient space; what is
established is which block each named component occupies.

---

## 3. What the reviewed result says it does not license

Transported verbatim from
`derivations/P2-GAPA-BRIDGE-01_basis-identification.md`:

> **This is the correct scope of the result and not a weakening of it.** The
> question asks about `q` along an axis, and `mlog_coeff.py:38` sets
> `q = (q0, 0.0, 0.0, 0.0)` — **`e₀` is the only direction the extraction ever
> uses**, so the identification covers every use of `TT_RECIPES` in the
> repository. What it does not license is reading `TT_RECIPES` as a covariant
> object: they do not rotate with `q`, and at any other direction the two
> subspaces are far apart, not nearly equal.

and:

> **This result does not make the physics conclusion at
> `paper/emergent_gr_paper_v2_15.tex:770-788` true of the measured object.** It
> establishes that the two decompositions name the same subspace at `q ∥ e₀`.
> Whether the manuscript's suppression statement applies to what `EXT-01`
> measured is `GAP-B`.

---

## 4. What this result does NOT establish

**`H-EXT-01` IS UNCHANGED.** It remains `UNESTABLISHED` and `NOT ASSUMED BY
RECON-01b`. The reviewed result states it at its `:360`. **`GAP-A` identifies
which subspace the discarded components occupy; it says nothing about whether
they contribute to the physically relevant observable.**

**`Q1` IS UNCHANGED.** It remains `INCONCLUSIVE`, with reason `UNDETERMINED BY
READING`, and with its subclass `INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED`
and its `Resolution path` intact. **`GAP-B` survives**, as the classification
recorded in advance that it would: `GAP-A`'s entry stated that closing it
"WOULD NOT DO SO AUTOMATICALLY" and that "`GAP-B` would remain open".

**THE APPARENT CHAIN IS NOT CLOSED.** A reader can now assemble:

    1. the discarded components are the Barnes–Rivers non-TT blocks
                                                        — established here
    2. the manuscript states non-TT structures are suppressed at O(p⁴/Λ²)
                                                        — paper:770-788
    3. therefore the discarded space is negligible
                                                        — NOT ESTABLISHED

**The step from 2 to 3 is `GAP-B` and is unestablished.** Step 2 is derived for
the infrared effective kernel, under Symanzik power counting, for the improved
stress tensor up to contact terms. `EXT-01` measured a lattice Proca bubble at
`a = 1`, `m = 0.3`, finite `n`, unimproved, and found the discarded components'
`q²` coefficients comparable in magnitude to the retained ones. **Whether the
first statement transfers to the second object is exactly `GAP-B`, and this
landing does not touch it.**

**`A-EXT-01` IS UNCHANGED** and remains a definitional convention. Its
`Statement SHA` is `ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378`,
unchanged by this landing.

**This section is here because the result makes a wrong inference easier than
it was before, not because anyone has drawn it.**

---

## 5. Method provenance

**The two methods are independent computational checks of the same formal
inputs, not independent evidence sources.** Both read the same two source
tables: the projector convention from `scripts/recovered_2026/tt_check.py:105-126`
and `scripts/recovered_2026/seagull_check.py:241-253`, and the recipes from
`scripts/recovered_2026/mlog_coeff.py:24-31`. **A transcription error common to
both would survive their agreement.** What their agreement excludes is an error
in either construction.

**The symbolic-float incident, transported as the reviewed result records it.**
The first symbolic run reported the two methods disagreeing on the `1/√6`
recipe, with residual `5.551115123125783e-17` — machine epsilon. The cause was
in the check, not in the repository: the symbolic path had been fed the recipe
vectors converted from `numpy` floats, and `1/√6` as a float is not `1/√6`. The
repair replaced them with exact radicals **verified inside the script against
the float table**, `max|diff| = 2.220e-16`. **A defect of the check, corrected,
and not a tuning toward a wanted answer** — the exact-radical table is checked
against the source values rather than asserted.

---

## 6. Records registered

    R-1   Whether a standing citation rule should require the momentum
          condition to accompany this result wherever it is cited.
          REGISTERED AS UNDECIDED. This landing does not create such a rule.
          REGISTER: docs/GOVERNANCE-DEBT.md, as `G-17`, disposition OPEN.

    R-2   That GAP-B is now the sole remaining gap named by Q1's Resolution
          path, and is unowned pending PI direction.
          REGISTER: none — see below.

**`R-2` restates an existing obligation and does not increment the count.**
`P2-PROJ-01-INTEG` registered `O-2` as "The bridge tasks. `GAP-A` and `GAP-B`,
one bounded task each, opened only on PI direction." **`GAP-A` is now closed, so
`R-2` is `O-2` narrowed to its remaining half. The number of obligations with
no admissible home stays at three.**

**Recorded without rewording, because two statements in the governing
specification sit oddly together:** §6 words `R-2` as "unowned pending PI
direction", while §12.1 records that "PI has directed it as the next task."
Both are transported as written. The consistent reading is that the PI has
directed `GAP-B` and no task specification for it yet exists, so it is directed
but not yet owned by a task.

**Confirmed at execution, before the word "sole" was used:** the authoritative
`Q1` `Resolution path`, `derivations/P2-PROJ-01-CLASS-01_q1-classification.md`
on `main`, names exactly two gaps — `GAP-A` at `:304` and `GAP-B` at `:340`,
with no third — and the artifact has not been amended since it landed. Its blob
is `e7b63d44319a7df3807f7d61aceb15afc2e0aa59`, and its history is a single
commit.

**Why `R-2` has no register.** The three scopes, read on the merge product:

    derivations/P2-DEFERRED-ITEMS.md      ":191" — "Entries are added by PI
                                          decision", each carrying a PI
                                          position. EXCLUDED by who may write.
    derivations/P2-PHASE-01_C-CHECK…      ":3-5" — scope is the C1/C2/C3 line.
                                          EXCLUDED by subject.
    docs/GOVERNANCE-DEBT.md               ":1-6" — the governance-side
                                          register. EXCLUDED by kind: R-2 is
                                          a scientific bridge task, not a gap
                                          in a rule.

**`R-1` differs from `R-2` in kind, which is why their registers differ.**
`R-1` asks whether a rule should exist; that is governance debt and
`docs/GOVERNANCE-DEBT.md` admits it. `R-2` names scientific work.

**No register was created, and none was used by convenience.**

---

## 7. What this landing does not establish

It lands a derivation already made, reviewed and independently reproduced. **It
produces no new result**, no `β_V`, moves no gate, and `P2-PHASE-01` is
unchanged.

**`Q1` remains `INCONCLUSIVE`. `H-EXT-01` remains `UNESTABLISHED`.** What
changes is that one of the two gaps `Q1`'s `Resolution path` names is closed —
for `q ∥ e₀` — and the line's outcome now turns on the other.
