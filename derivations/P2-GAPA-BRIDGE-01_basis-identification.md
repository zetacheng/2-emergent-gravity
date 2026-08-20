# `P2-GAPA-BRIDGE-01` — the basis identification, performed

    KIND        BOUNDED DERIVATION. Linear algebra only. No landing.
    ORIGIN      GAP-A of P2-PROJ-01-CLASS-01, under rule 22
    BASE        a6be149f531c4a55ad331f26412a16472b803628

    OUTCOME     IDENTIFICATION HOLDS

                Both conjuncts established, at the momentum direction
                TT_RECIPES fix, under the single Barnes–Rivers convention
                the repository fixes.

**This artifact settles a structural question in linear algebra.** It computes
no `β` of any kind, no ratio, no `k`-scan, no propagator, no lattice sum and no
loop integral. It does not change `Q1`, does not touch `GAP-B`, and does not
resolve `H-EXT-01`.

---

## 0. The question, as pre-registered

From `derivations/P2-RECON-PROJ-01_projection-adjudication.md:261-264`:

> **One statement, of either sign, in a document:** that for `q` along an axis
> the Barnes–Rivers TT block and the span of `TT_RECIPES` are the same
> five-dimensional space, and that the Barnes–Rivers non-TT blocks are the five
> components `EXT-01` enumerates as discarded — or that they are not.

**Two conjuncts. Both are answered below, and both in the affirmative.**

The derivation script is `scripts/diagnostics/gapa01_basis_identification.py`.
It is new; no existing file under `scripts/` was modified.

---

## 1. `M1` — the Barnes–Rivers projectors, as the repository defines them

**Two implementations, and they are the same convention.**

`scripts/recovered_2026/tt_check.py:105-126`, whose docstring at `:106` is
*"Barnes-Rivers projectors for Euclidean momentum q (4-vector)."*:

    def projectors(q):
        q2 = np.dot(q, q)
        om = np.outer(q, q) / q2
        th = np.eye(4) - om
        P2[a, b, c, d] = (0.5 * (th[a, c] * th[b, d] + th[a, d] * th[b, c])
                          - th[a, b] * th[c, d] / 3.0)
        P1[a, b, c, d] = 0.5 * (th[a, c] * om[b, d] + th[a, d] * om[b, c]
                                + th[b, c] * om[a, d] + th[b, d] * om[a, c])
        P0s = np.einsum("ab,cd->abcd", th, th) / 3.0
        P0w = np.einsum("ab,cd->abcd", om, om)

`scripts/recovered_2026/seagull_check.py:241-253` implements `P2` by the same
expression, differing only in a loop variable's name.

    projector set          four: P2, P1, P0s, P0w
    spacetime dimension    4, from np.eye(4) and the index ranges
    trace coefficient      1/3, written "/ 3.0" at tt_check.py:119 and
                           seagull_check.py:252, and again in P0s at :124.
                           This is 1/(D−1) at D = 4, θ having rank 3.
    momentum argument      q, a Euclidean 4-vector; om = q⊗q/q², th = I − om
    index space            symmetric rank-2 tensors on four indices. The array
                           is symmetric under a↔b and under c↔d, and acts by
                           (P h)_{ab} = Σ_{c,d} P[a,b,c,d] h_{cd}.

**A third `projectors` function in the repository is a different object and is
excluded by reading.** `scripts/p2_chirality_census.py:167` returns
`(I − γ₅)/2, (I + γ₅)/2` — chirality projectors on Dirac indices. §9's
`projector` hazard is exactly this.

## 2. `M2` — `TT_RECIPES`, as the repository defines them

`scripts/recovered_2026/mlog_coeff.py:21-31`:

    # 5 TT basis tensors for q || e0, expressed as pair-combination recipes:
    #   each entry: list of (pair, coefficient) such that
    #   U_eff = sum coeff * U^{pair}   corresponds to a unit-normalized tensor.
    TT_RECIPES = [
        [((1, 1), 1 / np.sqrt(2)), ((2, 2), -1 / np.sqrt(2))],
        [((1, 1), 1 / np.sqrt(6)), ((2, 2), 1 / np.sqrt(6)),
         ((3, 3), -2 / np.sqrt(6))],
        [((1, 2), 1 / np.sqrt(2))],
        [((1, 3), 1 / np.sqrt(2))],
        [((2, 3), 1 / np.sqrt(2))],
    ]

    five recipes           R1 … R5, as enumerated above
    normalisation          unit Frobenius norm of the h-matrix, per the
                           comment at :23 and as EXT-01:45-51 records. An
                           off-diagonal pair at 1/√2 sets h[a,b] = h[b,a] =
                           1/√2, of norm 1.
    momentum direction     q ∥ e₀, fixed by the comment at :21 and by
                           mlog_coeff.py:38, q = (q0, 0.0, 0.0, 0.0)
    index space            the same symmetric rank-2 space: a recipe is a
                           combination over PAIRS, and
                           seagull_check.py:49 defines
                           PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]
                           — the ten independent components of a symmetric
                           4×4 h.

**MEASURED, not assumed:** all five recipe h-matrices have Frobenius norm `1`,
and the ten retained-plus-discarded vectors are orthonormal to
`max|G − I| = 4.441e-16`.

## 3. `M3` — do they act on the same index space?

**YES. Both act on Sym²(R⁴), the ten-dimensional space of symmetric 4×4
matrices.**

The evidence is structural, not a coincidence of dimension:

- `TT_RECIPES` are combinations over `PAIRS`, which `seagull_check.py:49`
  defines as the ten independent components of a symmetric `4×4` `h`.
- `tt_check.py`'s `P2[a,b,c,d]` is symmetric under `a↔b` and under `c↔d`, so
  as a linear map it carries Sym²(R⁴) into Sym²(R⁴).
- **Measured on the merge of the two:** written in one orthonormal basis of
  Sym²(R⁴), `P2 + P1 + P0s + P0w = I₁₀` exactly, symbolically. Four blocks of
  ranks `5 + 3 + 1 + 1 = 10`. **A projector set summing to the identity on a
  space is acting on that space**, and this one sums to the identity on
  exactly the space `TT_RECIPES` are written in.

### 3.1 The `EXT-01` statement, and what this measurement does to it

`derivations/P2-RECON-EXT-01_discarded-external-space.md:119-124` reads:

> The tokens `spin-2`, `spin-1`
> and `spin-0` occur in 18, 13 and 12 files respectively, but **none of those
> occurrences is a statement about the external `h` decomposition this artifact
> measures** — they belong to the manuscript's stress-tensor channel discussion
> and to the `CHANNEL-B0` and `POLE-B0` assessments, which concern
> Barnes–Rivers projectors acting on a different object.

**The measurement does not contradict it, and does not support it either. It
settles a different question than the one that sentence asks.**

Read precisely, `EXT-01:124` is a statement about **what those eighteen,
thirteen and twelve occurrences are about** — the stress-tensor correlator
`⟨TT⟩` — and not about the index space the projector arrays act on. **Those
are two different senses of "object", and the distinction is the whole of
`GAP-A`:**

    the OBJECT PROJECTED   differs. tt_check.py projects the bubble tensor B,
                           a correlator; TT_RECIPES build effective vertices.
    the INDEX SPACE        is the same. Both are linear operations on the
                           symmetric 4×4 h.

**`EXT-01`'s caution was about the first and is correct about it. `GAP-A` is
about the second.** A reader who took `:124` to mean the projectors act on a
different *index space* would have concluded the identification was
impossible; measured, it is not.

**`EXT-01` also declined to supply the correspondence for a stated reason**, at
`:129-133`: that the retained space is defined for a single momentum direction
and that a covariant construction was absent. **That reason is respected here
rather than overridden** — §6 below measures exactly how far the identification
extends in direction, and it does not extend beyond `q ∥ e₀`.

## 4. `M4` — the discarded components, verbatim

`derivations/P2-RECON-EXT-01_discarded-external-space.md:74-78`:

    D1   h00                                       coefficient 1
    D2   the (0,1) direction                       coefficient 1/√2
    D3   the (0,2) direction                       coefficient 1/√2
    D4   the (0,3) direction                       coefficient 1/√2
    D5   ( h11 + h22 + h33 ) / √3   — the SPATIAL TRACE

with `:80-82`: "**`D1`–`D4` are every component carrying the axis index `0`.**
**`D5` is the spatial trace**, which no retained recipe reaches because `R1`
and `R2` are constructed traceless."

## 5. `M5` — does the repository fix one Barnes–Rivers convention?

**Yes. One convention, in two implementations that agree exactly.**

    tt_check.py:105-126        P2 with trace coefficient 1/3, D = 4
    seagull_check.py:241-253   the same expression

**MEASURED:** the two `P2` arrays at the same `q` differ by `max|diff| = 0.0` —
not "within tolerance", identically zero.

**No competing convention exists to test against.** The manuscript passage at
`paper/emergent_gr_paper_v2_15.tex:770-788` names the Barnes–Rivers basis and
writes `P^TT` but supplies no component formula, so it fixes no second
convention; it constrains nothing this derivation could have chosen
differently.

**A substring-hazard correction, recorded because it changes a landed count.**
`derivations/P2-POLE-B0_milestone-scope.md:214` records
*"OBJECT A — the full Barnes–Rivers set. ONE implementation, one file."* That
census counted files matching `Barnes`. **Measured, there are two
implementations of `P2` in two files**; `seagull_check.py` carries the same
formula without the name. The earlier count is right about how many files say
`Barnes` and undercounts implementations by one. **This does not change any
`POLE-B0` conclusion** — the two agree — and is recorded so the count is not
carried forward as an implementation count.

---

## 6. The derivation

### `D1` — SYMBOLIC

Built with `sympy` from `M1`'s formula, at symbolic momentum `q = (q0,0,0,0)`
with `q0 > 0`, and represented as a `10×10` matrix on Sym²(R⁴) in the
orthonormal basis of `M2`'s convention.

    P2 map is independent of q0                     True
    rank Im(P2)                                     5
    rank Im(P1)                                     3
    rank Im(P0s)                                    1
    rank Im(P0w)                                    1
    P2 idempotent, P2·P2 = P2                       True
    P2 symmetric, P2ᵀ = P2                          True
    P2 + P1 + P0s + P0w = I₁₀                       True
    each recipe fixed by P2, P2 v = v      [True, True, True, True, True]
    rank[ Im(P2) | recipes ]                        5
    each discarded component annihilated, P2 v = 0
                                           [True, True, True, True, True]

**`rank[Im(P2) | recipes] = 5` with `rank Im(P2) = 5` and all five recipes
fixed by `P2` is subspace equality**, not a dimension coincidence: every recipe
lies in `Im(P2)`, the five are independent, and `Im(P2)` has no room for
anything else.

**The comparison is of subspaces, never of basis lists.** No recipe is required
to equal any particular eigenvector of `P2`, and none was checked that way.

### `D2` — NUMERICAL

Independently constructed: the four projector arrays are built by the explicit
quadruple loop `tt_check.py` uses, then turned into `10×10` maps by applying
them to each basis matrix and projecting back — a different route from `D1`'s
symbolic assembly. Subspaces are compared by SVD and by projector difference.

    tolerance                                        1e-10
    rank(P2 map)                                     5
    ‖P2·P2 − P2‖_F                                   4.228e-16
    ‖P2ᵀ − P2‖_F                                     0.000e+00
    ‖P2map − Q_span(recipes)‖_F                      4.228e-16   → equal
    rank[ P2map | recipes ]                          5
    singular values of [P2map | recipes]   1.4142, 1.4142, 1.4142, 1.4142,
                                           1.4142, 1.055e-16, 0.0

**Five singular values at √2 and the sixth at `1.055e-16`** — a spectral gap of
sixteen orders of magnitude, which is what subspace equality looks like when it
is exact and the arithmetic is floating point.

**`D1` and `D2` AGREE.**

**They are independent implementations of the same formal definitions, not
independent evidence.** Both read the same two source tables. A transcription
error common to both would not be caught by their agreement; what their
agreement excludes is an error in either construction.

### `D3` — THE SECOND CONJUNCT, COMPONENT BY COMPONENT

**Not answered by dimension.** Each discarded component is tested individually
against each Barnes–Rivers non-TT block:

    component   ‖P2 v‖        fixed by
    D1          0.000e+00     P0w        the weak scalar block
    D2          0.000e+00     P1         the vector block
    D3          0.000e+00     P1
    D4          0.000e+00     P1
    D5          9.615e-17     P0s        the strong scalar block

    rank(span D1…D5)                                 5
    ‖(P1 + P0s + P0w) − Q_span(D1…D5)‖_F             4.191e-16

**Every discarded component is annihilated by `P2` and is fixed by exactly one
Barnes–Rivers non-TT block.** Not merely "lies in the complement" — each lands
in a single named block, and the three blocks partition the five components
`1 + 3 + 1`:

    P0w  ↔  {D1}            h00, the component along the axis twice
    P1   ↔  {D2, D3, D4}    the three mixed axis-spatial components
    P0s  ↔  {D5}            the spatial trace

**And the correspondence is onto.** The sum `P1 + P0s + P0w` equals the
orthogonal projector onto `span(D1…D5)` to `4.191e-16`. Neither side has a
direction the other lacks.

**`D5`'s `9.615e-17` is floating-point zero**, sixteen orders below the
components it is compared against; symbolically `D1` returns exact
annihilation for all five.

---

## 7. Bounding the claim — which momenta it holds for

**Measured, not assumed.** `TT_RECIPES` are hard-coded for `q ∥ e₀`;
the Barnes–Rivers projectors are built from whatever `q` they are given.

    momentum direction              ‖P2map − Q_recipes‖_F      equal
    e0, the axis TT_RECIPES fix     4.228e-16                  YES
    e1                              2.404e+00                  no
    e2                              2.404e+00                  no
    e3                              2.404e+00                  no
    diagonal (1,1,1,1)              2.121e+00                  no
    e0 rescaled, q0 = 13.0          4.228e-16                  YES

**The identification holds at `q ∥ e₀` and at no other direction tested**, and
it is independent of `|q₀|` — `D1` establishes that symbolically, the rescaled
row confirms it numerically.

**This is the correct scope of the result and not a weakening of it.** The
question asks about `q` along an axis, and `mlog_coeff.py:38` sets
`q = (q0, 0.0, 0.0, 0.0)` — **`e₀` is the only direction the extraction ever
uses**, so the identification covers every use of `TT_RECIPES` in the
repository. What it does not license is reading `TT_RECIPES` as a covariant
object: they do not rotate with `q`, and at any other direction the two
subspaces are far apart, not nearly equal.

**This is the concern `EXT-01:129-133` raised** — that the retained space is
defined for a single momentum direction — measured rather than left open.

---

## 8. Outcome

    IDENTIFICATION HOLDS

**First conjunct.** For `q ∥ e₀`, the Barnes–Rivers TT block and the span of
`TT_RECIPES` are the same five-dimensional subspace of Sym²(R⁴). Established
symbolically and numerically, by subspace comparison and by projector
difference, with agreement between the two.

**Second conjunct.** The Barnes–Rivers non-TT blocks are the five components
`EXT-01` enumerates as discarded — component by component, each in exactly one
block, with the three blocks together equal to the span of the five.

**Convention dependence, per `M5`.** The repository fixes **one**
Barnes–Rivers convention, implemented twice and identically. **The result holds
for that convention, which is every convention the repository has.** No second
convention exists under which it could differ, and none was introduced here.

**Direction dependence, per §7.** The result holds at `q ∥ e₀`, the direction
`TT_RECIPES` presuppose and the only direction the extraction uses. It does not
hold at the other coordinate axes or at the diagonal.

---

## 9. What this does not establish

**`Q1` is unchanged.** It remains `INCONCLUSIVE` with reason `UNDETERMINED BY
READING`, and nothing here alters it. Re-verification of `Q1` against its own
pre-registered test is a separate task, performed under the verification
prohibition this task was exempt from.

**`GAP-B` is untouched and survives this result.** Whether `L2`'s
`O(p⁴/Λ²)` suppression — derived for the infrared effective kernel, under
Symanzik power counting, for the improved stress tensor up to contact terms —
transfers to the object `EXT-01` measured, a lattice Proca bubble at `a = 1`,
`m = 0.3`, finite `n`, unimproved, is a question this derivation does not
touch. **It was independent of `GAP-A` before this result and is independent of
it after.**

**`H-EXT-01` remains `UNESTABLISHED` and `NOT ASSUMED BY RECON-01b`.**

**No number of the programme's kind was produced.** No `β_V`, no `β_B`, no
ratio, no `k`-scan, no lattice evaluation, no loop integral. No gate moves and
`P2-PHASE-01` does not advance.

**This result does not make the physics conclusion at
`paper/emergent_gr_paper_v2_15.tex:770-788` true of the measured object.** It
establishes that the two decompositions name the same subspace at `q ∥ e₀`.
Whether the manuscript's suppression statement applies to what `EXT-01`
measured is `GAP-B`.
