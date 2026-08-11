# `P2-PHASE-01` — adjudication of the diquark decomposition discrepancy

**Status:** adjudication. Registers no gate, changes no gate status,
freezes no convention, and produces **no channel-character result**.
`P2-PHASE-01` remains `PROPOSED`. The branch under adjudication,
`gate/p2-diquark-both-eta` @ `bc1e5c743aada004c52dc7ab7ce2af61de439955`,
is **not modified and not integrated**; its disposition remains
`HOLD — MATERIAL RESULT DISCREPANCY`.

**This note finds where two computations first diverge.** It does not
decide which is right beyond what the frozen material settles by
quotation, and it does not repair either.

---

## 1. Determinism, first

Both methods were re-run twice in one environment, comparing the complete
numerical payload used in L1–L6 — every field, none ignored.

    method A   run 1 == run 2   byte-identical over the complete payload
    method B   run 1 == run 2   integer and index data byte-identical;
                                floating arrays identical to 0.0 absolute
    tolerance used for method B's floating comparisons   1e-12
    (the observed maximum difference between runs was exactly 0.0)

Both computations are stable within this environment, so the comparison
below is between methods and not between runs.

**Method A also reproduces its committed record.** Run from the branch's
committed script without modification, its `build()` output equals the
committed `diquark.json` exactly, and its per-component family sums are
those the branch reports.

---

## 2. The two results

    per-component family sums     S       P       V       A       T
    method A, the branch          0       0     +1/2    -1/2      0
    method B, from §2 of the spec -1/2    -1/2     0       0     -1/2

**Method B as constructed here reproduces the specification's record of
it** — `S -1/2, P -1/2, V 0, A 0, T -1/2`, with reconstruction exact
(maximum absolute residual `9.5e-16` scalar, `1.1e-15` pseudoscalar), the
design matrix of full rank 256/256, and every off-family coefficient below
`3e-16`. So the discrepancy is real and is not an artefact of either
transcription.

---

## 3. L1 — the matrices actually used

The two methods use **different but equivalent** gamma representations.

    method A   from the repository's gamma_factory, metric (1,1,1,1)
    method B   g0 = kron(s1,s1)  g1 = kron(s1,s2)
               g2 = kron(s1,s3)  g3 = kron(s2,I2)

Both satisfy `{g_m, g_n} = 2 delta_mn` with Hermitian gammas, and both
give `g5 = g0 g1 g2 g3` Hermitian with `g5^2 = I4`.

**`C`, obtained as the null space of the homogeneous system.** Solving
`C g_m^T + g_m C = 0` for all four `m` as a single homogeneous linear
system over a **general complex 4x4 matrix** — 64 equations in 16
unknowns, by SVD:

    null-space dimension, computed   1
    smallest singular values         [2, 2, 2, 0]
    representative                   equals g0 g2 after rescaling
    C^T = -C                         True
    C g_m^T C^-1 = -g_m, all m       True

The dimension is **computed, not inferred from a basis search**. A search
over sixteen basis elements could not have excluded a linear combination;
the null space can and does.

**L1 verdict: DIFFERS**, elementwise, in every matrix.

**But the difference is not causal, and this is demonstrated rather than
argued.** The two representations are related by a similarity transform:
solving `S g^B_mu = g^A_mu S` gives a null space of dimension **1** — `S`
unique up to scale, as it must be for two irreducible four-dimensional
Clifford representations — and `S g^B_mu S^-1 = g^A_mu` holds for all four
`mu`, and for `g5`. §7's ablation then shows the family sums are
unchanged when the representation is swapped with all other conventions
held fixed.

**One further L1 difference, which *is* causal.** The two family bases
differ on `A` and `T`:

    method A   A = I*g_m*g5        T = I*(g_m g_n - g_n g_m)/2
    method B   A =   g_m*g5        T =   (g_m g_n - g_n g_m)/2

Representation-matched, the ratio of A's element to B's is exactly `1` for
`S`, `P`, `V` and exactly `i` for `A` and `T`, with proportionality
verified elementwise. This enters at L5.

---

## 4. L2 — the raw canonical rank-4 tensor

Index positions, stated explicitly because the whole question turns on
them. For a canonical operator `Gamma`,

    T[a,b,c,d] = Gamma[a,b] * Gamma[c,d]
    a, c   the psibar indices
    b, d   the psi indices

**Both methods build exactly this tensor with exactly this index
assignment.** They differ in *which* `Gamma` they use for the
pseudoscalar canonical term:

    method A   scalar Gamma = I4      pseudoscalar Gamma = I*g5
    method B   scalar Gamma = I4      pseudoscalar Gamma =   g5

Compared separately, as the two terms must be:

    scalar term
      literal, each in its own representation          IDENTICAL  (diff 0)
      representation-matched, B mapped into A by S     IDENTICAL  (diff 2.2e-16)

    pseudoscalar term
      literal                                          DIFFERS  (max diff 2.0)
      representation-matched                           DIFFERS  (max diff 2.0)
      representation-matched, against the negative     t_A = -S(t_B)  EXACTLY

**L2 verdict: the scalar tensors are identical; the pseudoscalar tensors
differ by exactly a factor of `-1`.** That is `(i)^2`, from `Gamma = i g5`
versus `Gamma = g5`.

**This is the first divergence.** One term matching while the other does
not is itself the diagnostic, and a summed comparison would have hidden
it: summing the two tensors before comparison would have shown "differs"
with no indication that the scalar half is in perfect agreement.

### Which pseudoscalar operator the frozen material fixes

Quoted from `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` at the
evidence base, exact literal substring, no normalisation, one occurrence
each:

> line 32:
> `P^A(x) ≡ Σ_{a,b=1}^{N} Σ_{α,β=1}^{4} ψ̄_{aα}(x) (λ^A)_{ab} (iγ₅)_{αβ} ψ_{bβ}(x)`

and in the machine block, twice:

    bilinear(lam(A),I*gamma5)**2

**The frozen canonical pseudoscalar bilinear carries `iγ₅`.** Method A
uses it. Method B, as specified, uses `γ₅`, so the tensor it decomposes is
the negative of the frozen interaction's pseudoscalar tensor.

**This is a statement about which tensor is the frozen one, established by
quotation.** It is not a judgement that method B computed anything
incorrectly: method B decomposes the tensor it was given, exactly, and its
reconstruction proves as much.

---

## 5. L3 — the pp slot map and the Grassmann permutation

    source ordering    psibar_a psi_b psibar_c psi_d
    diquark grouping   (psibar_a psibar_c)(psi_b psi_d)
    decomposition      Gamma_{ab} Gamma_{cd}
                         = sum_pq f_pq (Gamma_p C)_{ac} (C^-1 Gamma_q)_{bd}
    row index pair     (a,c)   the psibar pair
    column index pair  (b,d)   the psi pair

**Both methods use this map, and neither applies any Grassmann crossing
sign, `eta`, or normalisation before projection.** Method B's is
prescribed that way in the specification. Method A's `pp_dirac_
decomposition` decomposes the bare Dirac tensor and introduces `s_pp`,
`eta` and `nu` only afterwards, in a separate function.

**L3 verdict: IDENTICAL.** The parity of the permutation taking the
source ordering to the diquark grouping is `-1` — one adjacent
transposition — in both, and in both it is applied after projection or not
at all.

**This matters more than any other layer's verdict.** The possibility §0
of the specification exists to probe — two self-consistent results
corresponding to two *different pp orderings* — **is not what is
happening.** The slot map does not differ.

---

## 6. L4, L5, L6

**L4 — the target vector `t`.** `t` is L2's tensor after L3's map,
flattened in the order the extractor consumes, namely `(a,c,b,d)`. Since
L3 is identical, `t` differs exactly where L2 does: **scalar identical,
pseudoscalar differing by `-1`.** L4 verdict: **DIFFERS**, inherited from
L2 and from nowhere else.

**L5 — the design matrix `M`.** Columns are the 256 products
`(Gamma_p C) ⊗ (C^-1 Gamma_q)`. Representation-matched, the two design
matrices agree on the `S`, `P` and `V` columns and differ on the `A` and
`T` columns by exactly a factor of `i` per basis element. Both have rank
256, so in both cases the decomposition is **unique** and the extractor
has no freedom.

L5 verdict: **DIFFERS**, on the `A` and `T` columns only.

Its effect is confined and computable: `f_pp` carries `Gamma_p` in *both*
factors, so multiplying `Gamma_p` by `i` multiplies `f_pp` by `i^{-2} =
-1`. **The `A` and `T` diagonal coefficients flip sign; nothing else
moves.**

What the frozen material fixes, quoted, one occurrence each:

> `A=I*gamma(mu)*gamma5`, and
> `T=I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2`

and in the machine block:

    "basis_id":"A","expression":"I*gamma(mu)*gamma5"
    "basis_id":"T","expression":"I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2"

**Method A's family basis is the frozen one. Method B's is not.**

**L6 — the coefficient vector `f` and its family aggregation.** Differs,
as §2 records. Both decompositions are exact and both are unique, so `f`
differs *only* because `t` and `M` differ.

**First diverging layer: L2**, the raw canonical rank-4 tensor,
pseudoscalar term. Every downstream difference is accounted for by L2 and
L5 together, with nothing left over — §7 demonstrates this.

---

## 7. The ablation: the difference attributed, with nothing left over

One input changed at a time, the same least-squares extractor over the
same 256-element product basis throughout. Family sums, per component:

    #  representation  i on A/T  pseudoscalar Gamma      S      P      V      A      T
    1  B               no        g5                    -1/2   -1/2     0      0    -1/2   = method B
    2  B               no        i*g5                     0      0   +1/2   +1/2     0
    3  B               yes       g5                    -1/2   -1/2     0      0    +1/2
    4  B               yes       i*g5                     0      0   +1/2   -1/2     0   = method A
    5  A               yes       i*g5                     0      0   +1/2   -1/2     0   = method A
    6  A               no        g5                    -1/2   -1/2     0      0    -1/2   = method B

**Rows 4 and 5 are equal, and rows 1 and 6 are equal.** Swapping the
representation with everything else held fixed changes nothing:
**the representation is not causal.** The family sums are
representation-independent, as a covariant statement about the frozen
interaction must be.

**Rows 1 → 2 isolate the L2 cause.** Restoring `iγ₅` alone moves the
support from `S,P,T` to `V,A` — this single convention is what relocates
the surviving irreps as a group.

**Rows 2 → 4 isolate the L5 cause.** Restoring the `i` on the `A` and `T`
basis elements flips the sign of the `A` coefficient and of `T`'s
contributions, leaving `S`, `P`, `V` untouched.

**Row 4 equals method A exactly.** Method B's own machinery, its own
representation, its own least-squares extractor — with method A's two
frozen conventions restored — reproduces method A's numbers exactly.
**The discrepancy is fully explained by those two conventions and nothing
else remains unaccounted for.**

---

## 8. Neither extractor is defective

`t_A == t_B` is false and `M_A == M_B` is false, so **no implementation
defect in coefficient extraction or in the solver may be asserted**: the
case that would license it does not hold.

Two further checks were run because the absence of a licence is not the
same as the absence of a defect:

- **Method A's closed-form trace formula agrees exactly with least squares
  on method A's own `(M, t)`** — same values in every family, rank 256,
  maximum reconstruction residual `1.0e-15` scalar and `8.9e-16`
  pseudoscalar. A's extractor is internally consistent, and the trace
  formula it uses is not a shortcut that hides anything.
- **Both design matrices have rank 256**, so in each case the
  decomposition is unique and neither extractor had a choice to make.

**No defect is localised in either method**, and none is repaired here.

---

## 9. What this does and does not establish

**Established.**

- The two computations diverge first at **L2**, the raw canonical
  pseudoscalar tensor, and the divergence is exactly a factor of `-1`.
- A second, independent divergence sits at **L5**, the `A` and `T` design
  columns, exactly a factor of `i` each.
- **L3, the particle–particle slot map and its Grassmann permutation, is
  identical in the two methods.**
- Both differing conventions are ones the **frozen material fixes**, and
  method A uses the frozen values in both cases. This is established by
  literal quotation of the freeze, not by preference.
- The gamma representation is not causal.
- Neither extractor is defective, and the implementation-defect case does
  not apply.

**Not established, and explicitly not concluded.**

- **That the particle–particle ordering is harmless.** This adjudication
  found that *this* discrepancy does not arise from the ordering, because
  the two methods share a slot map. It tested **no alternative slot map**,
  and it therefore provides no evidence either way about whether some
  other admissible ordering would move the family support. The ordering
  remains unfrozen and, on this question, untested.
- **That method B is wrong as a computation.** It decomposes the tensor it
  was given, exactly and uniquely. It decomposes a different interaction.
- Which method is "correct" in any sense beyond the frozen material's own
  statements. What the evidence settles is which conventions the freeze
  fixes; it settles that by quotation.

**The branch's independence claim.** The branch's argument is that each
coefficient has the form `c = K*eta`, so the `eta` ratio is `-1` whatever
`K` is. **This discrepancy is silent on that claim**, because the
divergence is upstream of the point where `eta`, `s_pp` and `nu` enter and
because the slot map is shared. The claim is neither contradicted nor
further supported here. What the branch's report listed as *well-defined
independently of `eta`, `s_pp` and `nu`* — that `V` and `A` are the only
surviving families — is now known to be sensitive to the basis
normalisation and the canonical pseudoscalar operator. **Both are frozen,
not free**, so this is not a newly discovered unfrozen dependence; but it
is a sensitivity the branch did not state, and a reader of the branch
would not have known that its family support rests on those two frozen
choices.

---

## 10. Repository inputs read

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md          (evidence base)
    results/P2-CHANNEL-FREEZE/fierz_matrix.json                (evidence base)
    scripts/p2_diquark_both_eta.py                             (branch bc1e5c7)
    results/P2-PHASE-01/diquark-both-eta/diquark.json          (branch bc1e5c7)
    derivations/P2-PHASE-01_diquark_both_eta.md                (branch bc1e5c7)
    scripts/P2-CHANNEL-FREEZE/gamma_algebra.py                 (via method A's script)

Nothing else was read. The quarantined `-3.2(5)` value, the suspended
`P2-BETAV-CIRC-01` result and the historical Finding 5 extraction were not
consumed.
