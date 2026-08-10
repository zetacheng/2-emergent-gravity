# Report — adjudication of the diquark decomposition discrepancy

Specification: `specs/2026-08-10T1112Z_diquark-adjudication.md`
Specification sha256:
`1a071aed4c7bb35f7ddb1fd53e5482577050ba5596fc96d282375b36aaf94eb4`
Pre-execution review: `reviews/chatgpt/2026-08-10T1112Z_diquark-adjudication.md`
Evidence base: `8701a97a6bb58550d4300f75c10638b057335731`
Branch under adjudication: `gate/p2-diquark-both-eta` @
`bc1e5c743aada004c52dc7ab7ce2af61de439955` — **not modified, not
integrated**, disposition `HOLD — MATERIAL RESULT DISCREPANCY`
Branch: `gate/p2-diquark-adjudication`
Classification: MATERIAL. Branch only.

---

## 0. The answer

**A7's case: the divergence is in the canonical construction itself,
`T_A^P != T_B^P`.** Compared separately, as required:

    scalar canonical tensor        IDENTICAL — literally, and after mapping
                                  method B into method A's representation
    pseudoscalar canonical tensor  DIFFERS by exactly -1

**The first diverging layer is L2.** Method B, as the specification
describes it, builds the pseudoscalar tensor from `Γ = γ₅`; the frozen
canonical bilinear carries `iγ₅`, which method A uses. `(i)² = −1`, and
that single factor relocates the surviving families as a group.

**A second, independent divergence sits at L5:** method B's `A` and `T`
family basis elements omit the factor of `i` the freeze fixes. Because
`f_pp` carries `Γ_p` in *both* factors, that flips those two coefficients
and nothing else.

**L3 — the particle–particle slot map and its Grassmann permutation — is
IDENTICAL in the two methods.** This is the load-bearing negative result.
The possibility §0 of the specification exists to probe — two
self-consistent results corresponding to two different pp orderings — **is
not what is happening.** No promotion to dependence on the unfrozen
ordering is licensed, and none is made.

**The attribution is complete.** An ablation changing one input at a time
reproduces method A **exactly**, from method B's own representation,
basis-construction code and least-squares extractor, once the two frozen
conventions are restored. Nothing remains unaccounted for.

**No implementation defect is asserted**, because the case that would
license it does not hold: `t_A != t_B` and `M_A != M_B`. Two further
checks were run anyway and found nothing.

**A8:** the evidence **supports** the branch's independence claim, in the
precise sense that this discrepancy is silent on it. **It does not
establish that the pp ordering is harmless**, and this task tested no
alternative slot map.

Three execution findings, in §3, §12 and §13: the delimiter supply
protocol failed for the **fifth** time; the specification's own §10 record
of method B is reproduced exactly, which is worth stating because it could
have disagreed; and the specification's L2-decisive framing, which an
earlier version had and this one corrected, would have produced the wrong
conclusion here — the corrected framing is what made the right one
reachable.

No STOP condition fired.

---

## 1. A13 — refs, and the branch

    remote refs/heads/main                    8701a97a6bb58550d4300f75c10638b057335731
    refs/remotes/origin/main                  8701a97a6bb58550d4300f75c10638b057335731
    local main (stale by design)              0f7961747abe2a18b436c0b1e5b928f425ea4d9a
    remote gate/p2-diquark-both-eta           bc1e5c743aada004c52dc7ab7ce2af61de439955

Both `main` refs resolve to the evidence base; no mismatch, so no STOP.
Local `main` is stale by design, neither consulted nor repaired.
`gate/p2-diquark-adjudication` was created from `8701a97a…`. No `main` ref
moved and no branch was deleted.

**How method A's script was obtained without touching its branch.** A
**detached** worktree was created at `bc1e5c74`, which moves no ref. Both
before and after, `gate/p2-diquark-both-eta` resolves to
`bc1e5c743aada004c52dc7ab7ce2af61de439955` locally and remotely, and the
three branch artifacts' blob ids are unchanged. The script itself is
loaded inside the adjudication run straight from the commit's blob
(`git cat-file blob`), written to a temporary directory, and executed
there — never into this branch's tree.

---

## 2. A1 — inputs, pinned two different ways

**(a) DIGEST-PINNED — checked; a mismatch would be a STOP.** Method:
`git cat-file blob 8701a97a:<path> | sha256sum`.

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
      expected  fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a
      observed  fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a   MATCH

    results/P2-CHANNEL-FREEZE/fierz_matrix.json
      expected  5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9
      observed  5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9   MATCH

**(b) COMMIT-PINNED — existence checked, digest MEASURED and recorded,
not checked**, at `bc1e5c743aada004c52dc7ab7ce2af61de439955`:

    scripts/p2_diquark_both_eta.py
      exists  yes    bytes 36540
      measured sha256  8da0411d108ed45112ec93cd1135801e2d11765242df365b7f435409e2938586
      git blob id      5158201252ff1d1629ad056787f8c07c36469146

    results/P2-PHASE-01/diquark-both-eta/diquark.json
      exists  yes    bytes 16921
      measured sha256  deda121c98a5ed5ba31b288dca583bb92bba4ac34268a331e805f7c58c7305d1
      git blob id      b9af37d053d77926daed86842bc4f20bf861a6aa

    derivations/P2-PHASE-01_diquark_both_eta.md
      exists  yes    bytes 18499
      measured sha256  50e935f888d48bb1cf48cdbf721a3ec6ff11f08c2149bd033f7d61731a7528a9
      git blob id      e0eff7469e08e093dfd9caed5ca2bec1a1ef01f4

No expected digest was supplied for these three and none was invented, so
no "digest mismatch" criterion applies to them. The distinction is worth
the paragraph the specification spends on it: a digest an author supplies
is evidence about the author's belief, not about the file. **The commit is
the pin.** A test asserts that these three entries carry no `expected`
field, so a later edit cannot quietly turn a measurement into a check.

**Every repository input actually read**, by path:

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md        (evidence base)
    results/P2-CHANNEL-FREEZE/fierz_matrix.json              (evidence base)
    scripts/p2_diquark_both_eta.py                           (branch bc1e5c7)
    results/P2-PHASE-01/diquark-both-eta/diquark.json        (branch bc1e5c7)
    derivations/P2-PHASE-01_diquark_both_eta.md              (branch bc1e5c7)
    scripts/P2-CHANNEL-FREEZE/gamma_algebra.py               (via method A's script)

Method A's script additionally reads four files of its own
(`P2-PHASE-01_channel_character.md`, `…_layers.md`,
`channel-character-layers/layers.json`, `DECISION_LOG.md`), supplied to it
unmodified from the evidence base so that it runs as committed. Nothing
else was read. The quarantined `−3.2(5)` value, the suspended
`P2-BETAV-CIRC-01` result and the historical Finding 5 extraction were not
consumed.

---

## 3. A2 — the review, and the fifth delimiter failure

Committed at `reviews/chatgpt/2026-08-10T1112Z_diquark-adjudication.md` in
commit 2, before the work.

    committed blob sha256  65a3ed7f4c06e154c2ecb511c95d4255652dc6178edb94f50eeec42f0cbf4a4f
    size                   6620 bytes, 6590 characters, 99 lines
    identical to the extracted text:  True

**A2's whole-line rule again returned zero matches for BEGIN:**

    substring occurrences   BEGINS: 1    ENDS: 1
    WHOLE-LINE matches      BEGINS: []   ENDS: [line 102]

Line 0 of the supplied message, in full:

    @"/root/.claude/uploads/…/ece5a40b-SPEC_diquark_adjudication.md" === REVIEW ARTIFACT BEGINS ===

Same cause as last time: the BEGIN delimiter shares its line with the
attachment marker. **This is the fifth instance of the same supply
failure**, and the second consecutive one with this exact cause.

**The rule applied, asserted rather than assumed** — the same one as last
task, unchanged:

    END      located as a whole line, exactly one occurrence (line 102)
    BEGIN    the unique line whose content, after removing a prefix matching
             r'^@"[^"]+"\s+', equals the delimiter exactly

    prefix matches r'^@"[^"]+"\s+'   True
    remainder == the BEGIN literal   True

A2 also instructs "**Exclude any preamble sentence before the BEGIN
line**", which is what the stripped prefix is, differing only in that it
sits on that line rather than above it. Neither of A2's failure modes
applies: the text is present and corresponds — it names this task by
title, both SHAs, `A7`, `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`.
So a reportable deviation, not a stop. One residual normalisation, again
one byte: the literal slice is 6621 bytes with one leading and one
trailing newline; the committed artifact drops the leading blank line and
keeps a single trailing newline.

**Five instances, and the fix has not moved.** The previous report
proposed the paragraph that covers all five and said it belongs in
`CONVENTIONS.md`, not in the next specification. This specification
carries the improved wording again in its own A2 — and A2 was again
insufficient, for the same reason, because a per-task clause cannot
anticipate the harness. Restated once, unchanged:

> The review artifact is delimited by the two literals; each is located as
> the unique line whose content equals the literal **after removal of any
> leading attachment-marker or preamble text on that line**; the committed
> artifact is the lines strictly between them, with leading and trailing
> blank lines removed and a single trailing newline.

**The review's two non-blocking observations, both accepted as correct.**
The Reviewer noted that §3's heading — "stopping at the first divergence" —
reads as though execution halts there, while the body requires
identifying the first divergence and continuing. **The body is what I
followed**: all six layers are reported in §6, with the first divergence
named. And the Reviewer noted A7's four-case classification should be read
as classification by the *earliest* divergence, with downstream quantities
still reported. **That is exactly how §8 states it**: one classification,
three downstream layers also differing, both recorded.

---

## 4. A3 — determinism, first

Everything below depends on this, so it comes first.

**Method A, run twice from its committed script:**

    run 1 payload sha256  5875d9a66a6a673acad303ea162b88ec3faf7f553ffb1f44900596bf1ecd52d4
    run 2 payload sha256  5875d9a66a6a673acad303ea162b88ec3faf7f553ffb1f44900596bf1ecd52d4
    byte-identical over the COMPLETE payload, no field ignored:  True

**The whole adjudication — both methods, all six layers, the ablation —
run twice:**

    run 1 sha256  d249b4ed3eecfbb49c8ad47b22db605960157f52224878c8361ee149eb6d556b
    run 2 sha256  d249b4ed3eecfbb49c8ad47b22db605960157f52224878c8361ee149eb6d556b
    complete payload byte-identical, NO field ignored:  True

    floating values compared                    183
    max |run 1 − run 2| over all of them        0.0
    stated tolerance for floating comparisons   1e-12

**The tolerance is stated because the specification requires it, and the
observed difference is exactly zero**, so the tolerance was never
load-bearing. No field was ignored, and the specification names none as
non-computational metadata, so none was treated as such.

Both computations are stable within this environment. The comparison below
is between methods, not between runs.

---

## 5. A4 — method A reproduced, and A5 — method B constructed

**A4.** Method A's script was loaded from `bc1e5c74`'s blob and executed
**unmodified**.

    script_modified                     False
    reproduces its committed artifact   True   (build() == diquark.json, exactly)
    per_component_sum                   {S 0, P 0, V +1/2, A −1/2, T 0}
    recorded per_component_sum          {S 0, P 0, V +1/2, A −1/2, T 0}

**Method A reproduces its recorded numbers**, so the discrepancy is not a
transcription error on the branch side and the branch's own artifact is
what its script produces.

**A5.** Method B was constructed from §2's prose, not imported.

    Clifford {g_m, g_n} = 2 delta_mn          True
    all gammas Hermitian                      True
    g5^2 = I4,  g5 Hermitian                  True

    C from the NULL SPACE of C g_m^T + g_m C = 0
      system shape                            (64, 16)
      smallest singular values                [2, 2, 2, 0]
      NULL-SPACE DIMENSION, computed           1
      representative equals g0 g2 after rescaling   True
      C^T = -C                                True
      C g_m^T C^-1 = -g_m for all four m      True

    reconstruction, measured not assumed
      scalar        max abs residual  9.5e-16    rank 256/256
      pseudoscalar  max abs residual  1.1e-15    rank 256/256
      max abs off-family coefficient  < 3e-16

**The null-space dimension is computed, not inferred from a basis search**
— the specification is right that a search over sixteen elements cannot
exclude a linear combination, and the SVD of the full homogeneous system
can. The same computation was run for method A's representation, with the
same answer.

**Method B as constructed here reproduces the specification's §10 record
of it exactly** — `S −1/2, P −1/2, V 0, A 0, T −1/2`, with `T`'s sign
resolved to `−1/2` where §10 records `±1/2`. Stating this matters: §10
explicitly warned that a disagreement would itself be a finding. There is
none, so the discrepancy under adjudication is real on both sides and not
an artefact of either transcription.

---

## 6. A6 — L1 through L6, with verdicts

### L1 — the matrices actually used: **DIFFERS**

    method A   the repository's gamma_factory, metric (1,1,1,1)
    method B   g0 = kron(s1,s1)   g1 = kron(s1,s2)
               g2 = kron(s1,s3)   g3 = kron(s2,I2)

Every matrix differs elementwise; both are valid Clifford
representations. `C` in each case comes from the null space, dimension 1
in both.

    method A   C = [[0,1,0,0],[-1,0,0,0],[0,0,0,-1],[0,0,1,0]]
    method B   C = g0 g2 = [[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]]

**The representation difference is not causal, and this is demonstrated
rather than argued.** Solving `S g^B_mu = g^A_mu S`:

    null-space dimension                1
    S g^B_mu S^-1 = g^A_mu, all four mu  True
    S g5^B S^-1 = g5^A                   True

Dimension 1 is what two equivalent irreducible four-dimensional Clifford
representations must give — the intertwiner is unique up to scale. §7's
ablation then shows the family sums are unchanged when the representation
is swapped with everything else fixed.

**One L1 difference that *is* causal**, and it feeds L5. The family bases
differ on `A` and `T`:

    method A   A = I*g_m*g5        T = I*(g_m g_n - g_n g_m)/2
    method B   A =   g_m*g5        T =   (g_m g_n - g_n g_m)/2

Representation-matched, the ratio of A's element to B's is exactly `1` for
`S`, `P`, `V` and exactly `i` for `A`, `T`, with proportionality verified
elementwise on all sixteen entries.

### L2 — the raw canonical rank-4 tensor: **scalar IDENTICAL, pseudoscalar DIFFERS**

Index positions, stated because everything turns on them:

    T[a,b,c,d] = Gamma[a,b] * Gamma[c,d]
    a, c   the psibar indices
    b, d   the psi indices

Both methods build exactly this, with exactly this assignment. They differ
in which `Gamma` the pseudoscalar term uses: `iγ₅` (A) versus `γ₅` (B).

    scalar term
      literal, each in its own representation        IDENTICAL   diff 0
      representation-matched                        IDENTICAL   diff 2.2e-16

    pseudoscalar term
      literal                                       DIFFERS     max diff 2.0
      representation-matched                        DIFFERS     max diff 2.0
      representation-matched against the negative   t_A = -S(t_B)  EXACTLY

**Compared separately, as A7 requires — and the separation is the
diagnostic.** A summed comparison would have returned "differs" and hidden
the fact that the scalar half agrees perfectly, which is what localises
the cause to the pseudoscalar operator alone.

### L3 — the pp slot map and the Grassmann permutation: **IDENTICAL**

    source ordering        psibar_a psi_b psibar_c psi_d
    diquark grouping       (psibar_a psibar_c)(psi_b psi_d)
    decomposition          Gamma_{ab} Gamma_{cd}
                             = sum_pq f_pq (Gamma_p C)_{ac} (C^-1 Gamma_q)_{bd}
    row index pair         (a,c)  the psibar pair
    column index pair      (b,d)  the psi pair
    permutation parity     -1  (one adjacent transposition)

    Grassmann sign applied before projection   A: no    B: no
    eta / s_pp / nu applied before projection  A: no    B: no

Method B's is prescribed that way by §2. Method A's
`pp_dirac_decomposition` decomposes the bare Dirac tensor and introduces
`s_pp`, `eta` and `nu` only afterwards, in a separate function —
verified by reading the committed script, not inferred.

**This is the verdict that matters most**, and it is a negative one.

### L4 — the target vector `t`: **DIFFERS**

`t` is L2's tensor after L3's map, flattened `(a,c,b,d)`. Since L3 is
identical, `t` differs exactly where L2 does and **from nowhere else**:
scalar identical, pseudoscalar differing by `−1`. A test verifies the
flattening convention entry by entry against `Gamma[a,b]*Gamma[c,d]`.

### L5 — the design matrix `M`: **DIFFERS, on `A` and `T` only**

    rank M_A   256      rank M_B   256      both full rank, so f is UNIQUE
    differs on families                     ['A', 'T']
    factor per basis element                exactly i

**Mechanism, and it is confined:** `f_pp` carries `Γ_p` in *both* factors,
so multiplying `Γ_p` by `i` multiplies `f_pp` by `i^{−2} = −1`. Verified
directly by extracting with and without the factor in the same
representation: `S`, `P`, `V` unchanged to `<1e-9`; `A`, `T` exactly
negated.

### L6 — the coefficient vector and its family aggregation: **DIFFERS**

    per-component family sums     S       P       V       A       T
    method A                      0       0     +1/2    -1/2      0
    method B                    -1/2    -1/2      0       0     -1/2

Both decompositions are exact and both are unique, so `f` differs *only*
because `t` and `M` differ.

### First diverging layer

**L2.** L1 differs elementwise, but its difference is shown non-causal, so
the first divergence that changes the answer is L2 — with L5 contributing
a second, independent difference. Both are reported; the classification
follows the earliest.

---

## 7. The ablation — the difference attributed with nothing left over

One input changed at a time, the same least-squares extractor over the same
256-element product basis throughout:

    #  rep   i on A/T   pseudoscalar Γ      S      P      V      A      T
    1  B     no         γ₅               -1/2   -1/2     0      0    -1/2   = method B
    2  B     no         iγ₅                 0      0   +1/2   +1/2     0
    3  B     yes        γ₅               -1/2   -1/2     0      0    +1/2
    4  B     yes        iγ₅                 0      0   +1/2   -1/2     0    = method A
    5  A     yes        iγ₅                 0      0   +1/2   -1/2     0    = method A
    6  A     no         γ₅               -1/2   -1/2     0      0    -1/2   = method B

    row 4 == method A   True        row 5 == method A   True
    row 1 == method B   True        row 6 == method B   True
    representation is not causal    True

**Rows 4 and 5 agree and rows 1 and 6 agree**: swapping the representation
with everything else held fixed changes nothing. The family sums are
representation-independent, as a covariant statement about the frozen
interaction must be.

**Rows 1 → 2 isolate the L2 cause.** Restoring `iγ₅` alone moves the
support from `S,P,T` to `V,A`. This is the factor that relocates the
surviving irreps as a group — the thing §0 of the specification said no
sign or normalisation would do. It does, because it multiplies the *whole
pseudoscalar tensor* by `−1` and the two canonical terms then reinforce
where they had cancelled and cancel where they had reinforced.

**Rows 2 → 4 isolate the L5 cause.** Restoring the `i` on the `A` and `T`
basis elements flips those two and leaves `S`, `P`, `V` untouched.

**Row 4 equals method A exactly**, from method B's own representation,
basis code and extractor. **Nothing remains unaccounted for.**

---

## 8. A7 — the case, stated as exactly one

    CASE:  T_A^S != T_B^S  or  T_A^P != T_B^P
           — the divergence is in the canonical construction itself.

    scalar tensors, compared separately        IDENTICAL
    pseudoscalar tensors, compared separately  DIFFER, by exactly -1

**Exactly one classification**, by the earliest differing quantity.
Downstream quantities also differ — L4, L5 and L6 — and §6 reports each;
"exactly one case" is one classification, not one numerical difference.

**The other three cases, and why each is excluded:**

- *Ordering / index-map divergence (`t_A != t_B` with both canonical
  tensors matching).* **Excluded**: the canonical tensors do not both
  match, and independently **L3 is identical**, so there is no ordering
  divergence to promote. The specification's guard is therefore not even
  reached — but it would fail if it were, since method B applies no
  Grassmann crossing and its source-to-diquark rearrangement is the same
  as method A's.
- *Basis / projector-convention divergence (`t_A == t_B`, `M_A != M_B`).*
  **Excluded** as the classification, because `t` differs. `M` *does* also
  differ, on `A` and `T`, and §6's L5 reports it — but it is not the
  earliest divergence.
- *Implementation defect (`t_A == t_B`, `M_A == M_B`, `f_A != f_B`).*
  **Excluded**: both `t` and `M` differ. **No implementation defect is
  asserted anywhere in this report.**

### Which construction the frozen material fixes

Established by quotation, not by preference. Exact literal substring on
the freeze's raw UTF-8 text, no normalisation:

    "(iγ₅)_{αβ}"                                                    1 occurrence
    "bilinear(lam(A),I*gamma5)**2"                                  2 occurrences
    "A=I*gamma(mu)*gamma5"                                          1 occurrence
    "T=I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2"               1 occurrence
    '"basis_id":"A","expression":"I*gamma(mu)*gamma5"'              1 occurrence
    '"basis_id":"T","expression":"I*(gamma(mu)*gamma(nu)-…)/2"'     1 occurrence

The canonical line, quoted:

> `P^A(x) ≡ Σ_{a,b=1}^{N} Σ_{α,β=1}^{4} ψ̄_{aα}(x) (λ^A)_{ab} (iγ₅)_{αβ} ψ_{bβ}(x)`

**The freeze fixes both quantities method B departs from, in prose and in
the machine block. Method A uses the frozen values in both cases; method
B, as specified, uses neither.**

The script raises if any of these six literals disappears, so the
adjudication's premise cannot silently rot; a test pins that behaviour.

**What this does and does not say.** It says which tensor is the frozen
interaction's. **It does not say method B computed anything incorrectly**:
method B decomposes the tensor it was given, exactly and uniquely, and its
`9.5e-16` residual proves it. It decomposes a different interaction.

---

## 9. Neither method contains a defect I can localise

The implementation-defect case does not apply, but the absence of a licence
is not the absence of a defect, so two further checks were run.

- **Method A's closed-form trace formula against least squares on method
  A's own `(M, t)`**: identical in every family, both terms, rank 256,
  maximum residual `1.0e-15` scalar and `8.9e-16` pseudoscalar, maximum
  off-family coefficient below `1e-9`. **A's extractor is internally
  consistent and its trace formula is not a shortcut that hides
  anything.**
- **Both design matrices have rank 256**, so in each case the
  decomposition is unique and neither extractor had a choice to make.

**No defect is localised in either method, and no file or line is named as
defective.** Nothing was repaired; §5 forbids it and there was nothing to
repair.

One naming imprecision, well short of a defect and reported only because
§9 of the specification asks what I can localise: method A's flag
`decomposition_is_diagonal_in_the_family_basis` actually tests full
diagonality (`p == q`), which is *stronger* than its name. The value it
reports is correct.

---

## 10. A8 — the independence claim

**The branch claims** its verdict is *independent of the two remaining
unfrozen definitions* — the pp Grassmann ordering and the diquark
normalisation.

**Assessment: the evidence supports independence** — the first of A8's
three options — in a precise sense that must not be inflated:

**This discrepancy is silent on the claim.** The divergence is upstream of
the point where `eta`, `s_pp` and `nu` enter, and L3 is identical, so the
discrepancy bears on neither unfrozen definition. The claim is **not
contradicted** and **not further supported**. The branch's algebraic
argument — each coefficient is `c = K·eta`, so the ratio is `−1` whatever
`K` is — is untouched, and §1 of this specification is right that it is
algebra both computations satisfy.

**What is explicitly NOT concluded: that the pp ordering is harmless.**
§5 prohibits it and the evidence would not support it. This adjudication
tested **no alternative slot map**. It found that *this* discrepancy does
not arise from the ordering; it says nothing about whether some other
admissible ordering would move the family support. The ordering remains
unfrozen and, on that question, untested.

**A sensitivity the branch did not state, and a reader would want.** The
branch listed, among things *well-defined independently of `eta`, `s_pp`
and `nu`*, that "`V` and `A` are the only surviving families" and "`S`,
`P` and `T` carry no induced diquark coefficient at all". Those are now
known to depend on **the canonical pseudoscalar operator** and on **the
`A`/`T` basis normalisation**. Both are **frozen, not free**, so this is
not a newly discovered unfrozen dependence and the branch's claim stands
as written. But the family support rests on two frozen choices that the
branch's report never named, and a reader of that report could not have
known which choices its headline result depends on.

---

## 11. Could both results be correct for two different admissible orderings?

The specification asks this directly and says that if so, the finding is
larger than the discrepancy that prompted the task.

**No — and the reason is specific, not a shrug.** The question presupposes
that the two computations differ in their pp ordering. **They do not:
L3 is identical**, verified on the slot map, the index-pair assignment,
the permutation parity, and the absence of any Grassmann sign, `eta` or
`nu` before projection in either. There are not two orderings here; there
is one ordering and two canonical-tensor-plus-basis conventions.

**And the two are not both admissible.** Both quantities method B differs
on are fixed by the frozen material (§8), so method B is not a second
admissible convention. Per the specification's own guard, the stronger
reading does not follow, and per A8 the honest classification of method B
is: **a useful diagnostic comparator, not a second admissible
construction.**

**So the larger finding the specification hoped for is not available on
this evidence.** What replaced it is smaller but solid: the discrepancy is
fully explained, it is not about the unfrozen ordering, and the branch's
numbers are the ones the frozen conventions produce.

---

## 12. What remains unresolved, named precisely

- **Whether a genuinely different but admissible particle–particle slot
  map — as opposed to a reordering sign — would move the family support.**
  Neither the branch nor this adjudication tested one. The branch varied
  `s_pp` over four target orderings, all of which are global sign changes
  under a *fixed* slot map; a different slot map is a different question,
  and it is open.
- **The pp Grassmann ordering and the diquark operator normalisation
  remain unfrozen**, untouched here, and are PI decisions.
- **Whether the branch is integrable.** This task does not decide it. What
  it establishes is that the branch's numbers are what the frozen
  conventions give and that its computation reproduces exactly; whether
  the branch's report needs the §10 sensitivity statement added before
  integration is a PI call, not mine.

---

## 13. A9 — scope; A10 — nothing disturbed; A11-pre; A12

**A10**, compared as individual blob object ids from `git ls-tree -r`:

    paths at base                                 297
    paths at head                                 303
    base-present paths modified or missing          0

    GATES.md, CONVENTIONS.md, AGENTS.md, DECISION_LOG.md,
    pyproject.toml, CLAIMS.md                     all identical

    pre-existing tests/ paths                     16, all blob-identical
    tests/ paths at head                          17

**`tests/` gains exactly one file and no existing test is modified,
renamed or removed.** The branch under adjudication is untouched: its ref
is unmoved locally and remotely and its three artifacts' blob ids are
unchanged (§1).

**A9 — the template**, as the specification states it, and the resolved
manifest (`XX = 10`, `{HHMM} = 1112`, fixed by commit 1):

    {
      "mode": "exact",
      "base": "8701a97a6bb58550d4300f75c10638b057335731",
      "head": "HEAD",
      "required": [
        {"operation": "add", "path": "specs/2026-08-10T1112Z_diquark-adjudication.md"},
        {"operation": "add", "path": "reviews/chatgpt/2026-08-10T1112Z_diquark-adjudication.md"},
        {"operation": "add", "path": "derivations/P2-PHASE-01_diquark_adjudication.md"},
        {"operation": "add", "path": "scripts/p2_diquark_adjudication.py"},
        {"operation": "add", "path": "results/P2-PHASE-01/diquark-adjudication/adjudication.json"},
        {"operation": "add", "path": "tests/test_p2_diquark_adjudication.py"},
        {"operation": "add", "path": "reports/2026-08-10T1112Z_diquark-adjudication.md"}
      ],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

    resolved manifest sha256
      ff134190aa5d23c5e8f432df3cd002a191180ba754fe482fd58409ce529fd0c6

**Scope-checker output at the pre-report head, verbatim**, including
`observed_operations` (this report is the seventh addition, not yet
committed):

    $ python -m scripts.governance_tools.scope_checker --repo . --manifest adjscope_pre.json
    {
      "base": "8701a97a6bb58550d4300f75c10638b057335731",
      "failures": [],
      "head": "03110a992cd90436fc0d7bd7050ab0d90c26c302",
      "mode": "exact",
      "observed_operations": [
        {
          "operation": "add",
          "path": "derivations/P2-PHASE-01_diquark_adjudication.md"
        },
        {
          "operation": "add",
          "path": "results/P2-PHASE-01/diquark-adjudication/adjudication.json"
        },
        {
          "operation": "add",
          "path": "reviews/chatgpt/2026-08-10T1112Z_diquark-adjudication.md"
        },
        {
          "operation": "add",
          "path": "scripts/p2_diquark_adjudication.py"
        },
        {
          "operation": "add",
          "path": "specs/2026-08-10T1112Z_diquark-adjudication.md"
        },
        {
          "operation": "add",
          "path": "tests/test_p2_diquark_adjudication.py"
        }
      ],
      "overall": "PASS",
      "tool": "scope_checker"
    }
    EXIT=0

Six additions and zero modifications at the pre-report head; seven and
zero expected at the final head.

**A11-pre**, run individually with `python -m pytest <path>`:

    tests/test_repository_structure.py         4 passed in 0.01s                EXIT=0
    tests/test_si1_governance.py              14 passed in 0.04s                EXIT=0
    tests/test_gate_anchors.py                18 passed, 2 deselected in 2.64s  EXIT=0
    tests/test_governance_tools.py             8 passed in 1.30s                EXIT=0
    tests/test_p2_channel_character.py        23 passed in 0.90s                EXIT=0
    tests/test_p2_diquark_adjudication.py     24 passed in 0.43s                EXIT=0

All six exit 0.

**What the new test file covers.** Twenty-four tests, each recomputing its
claim rather than reading it back, except where a test exists to pin what
the artifact records: both gamma sets are valid Clifford representations;
`C` from a dimension-1 null space in both, satisfying its defining
relation and antisymmetric; the two representations equivalent; the scalar
tensors equal and the pseudoscalar ones exactly negated; the factor being
`i²` and not something else; the slot map identical; the flattening
convention entry by entry; both design matrices full rank; the `A`/`T`
factor exactly `i` and its effect confined to those two families; the
ablation's four equalities; the freeze fixing both conventions and the
check raising if it stops; method A reproducing and deterministic; its
trace formula agreeing with least squares; no defect asserted; the case
and first layer; the independence claim answered without overreach; the
commit-pinned inputs carrying no `expected` field.

**A12 — lint**, exact command and output:

    $ ruff check scripts/p2_diquark_adjudication.py tests/test_p2_diquark_adjudication.py
    All checks passed!
    EXIT=0

Those two files only. Four findings on the first run — two `E741`
ambiguous `l`, one `E501`, one `F841` unused local — were fixed by
renaming, extracting a helper and deleting the unused binding. No rule was
disabled, no `noqa` added, and the script and tests were re-run afterwards
with identical results.

**Environment.**

    Python              3.11.15
    python -m pytest    9.1.1      (the version A11 mandates)
    pytest on PATH      9.0.2      (not used)
    ruff                0.15.8
    numpy               2.4.6
    sympy               1.14.0

Nothing was installed. No environment failure occurred, so **neither of
Rule 13's two diagnostic orders was exercised** — I am not naming one,
because none was.

---

## 14. A14 — commit-message hygiene, and intended final state

Each message inspected before writing (proposed file) and after
(`git log -1 --format='%B'`, from the object). Scan pattern, case
insensitive: `co-authored-by|claude|session|https?://|generated with|
anthropic`.

    commit 1  79fae727fe02caab48acd4d01316140ef2bdc20c
      specs/2026-08-10T1112Z_diquark-adjudication.md
      "spec: adjudicate the diquark decomposition discrepancy layer by layer"
      proposed: no match   stored: no match
      trailers suppressed: YES — the default Co-Authored-By and session-URL
      trailers were prevented at authoring time; neither is in the object.

    commit 2  a370725d0c1a6f61bf4740af121987aeabe61ced
      reviews/chatgpt/2026-08-10T1112Z_diquark-adjudication.md
      "review: commit the pre-execution review for the diquark adjudication"
      proposed: no match   stored: no match      trailers suppressed: YES, same two.

    commit 3  ebac1581159a5827ddbc26e2f0bc3b70a1ca601e
      derivations/P2-PHASE-01_diquark_adjudication.md
      "adjudicate: locate the first divergence between the two diquark
       decompositions"
      proposed: no match   stored: no match      trailers suppressed: YES, same two.

    commit 4  03110a992cd90436fc0d7bd7050ab0d90c26c302
      scripts/, results/, tests/ — one work commit
      "compute: the layer-by-layer adjudication, script results and tests"
      proposed: no match   stored: no match      trailers suppressed: YES, same two.

**Commit order, as A0 requires:** commit 2 precedes commit 3, so the
review was committed before the work; commit 3 precedes commit 4, so the
derivation note precedes production code per `AGENTS.md` rule 3; commits 4
and 5 are separate because this report carries evidence the work commit
cannot contain.

**Pre-report head:** `03110a992cd90436fc0d7bd7050ab0d90c26c302`

**Intended final manifest:** the resolved manifest of §13, seven additions
and zero modifications.

**Intended report commit message:**

    docs: report the diquark decomposition adjudication

    Records A1-A10, A11-pre, A12, A13 and A14.

    A7's case is the canonical construction itself: the scalar tensors are
    identical, literally and representation-matched, and the pseudoscalar
    ones differ by exactly -1 because method B builds it from gamma5 where
    the frozen canonical bilinear carries i*gamma5. A second, independent
    divergence sits at L5, where method B's A and T basis elements omit the
    factor of i the freeze fixes. L3 -- the particle-particle slot map and
    its Grassmann permutation -- is IDENTICAL, so this is not an ordering
    divergence and no promotion to dependence on the unfrozen ordering is
    licensed. An ablation reproduces method A exactly from method B's own
    machinery once both frozen conventions are restored, with nothing left
    unaccounted for, and shows the gamma representation is not causal.

    No implementation defect is asserted: t and M both differ, so that case
    does not apply, and two further checks found nothing. A8: the evidence
    supports the branch's independence claim only in the sense that this
    discrepancy is silent on it; the report does not conclude the pp
    ordering is harmless and tested no alternative slot map.

    Fifth consecutive failure of the review supply protocol, same shared-line
    cause as the fourth. The one-paragraph fix belongs in CONVENTIONS.md.

    Nothing frozen, nothing repaired, no channel-character result. The branch
    under adjudication is untouched and stays on HOLD.

---

## 15. Stops and clarifications

No stop occurred. All findings below are secondary.

**`SPECIFICATION_DEFECT` — one, now at five instances.**

*A2's whole-line delimiter rule was inapplicable as written* (§3),
returning zero matches for BEGIN because the delimiter shared its line
with an attachment marker — the same cause as the fourth instance. Neither
of A2's failure modes applied, so I applied the same derived rule,
asserted it, and reported it rather than stopping. **The rule is mine and
the specification did not authorise it.** The fix has not changed since
the last report and is restated in §3; it belongs in `CONVENTIONS.md`,
because a per-task clause has now failed to anticipate the harness twice
in a row.

**`OBSERVATION_METHOD_ERROR` — none this task.**

Two secondary observations about method, both about the specification's
own design and both to its credit:

*The specification's earlier L2-decisive framing would have produced the
wrong conclusion here, and its correction is what made the right one
reachable.* §3 records that an earlier version made L2 decisive and
concluded that identical raw tensors implied a broken projector. Had that
version been executed, the L2 comparison would have found the
**pseudoscalar** tensors differing and — under the discarded rule — the
executor would have been steered toward "canonical construction" without
the obligation to check L3, and so without discovering that the slot map
is identical. That negative result is the most load-bearing thing in this
report, and it exists because the corrected specification required all six
layers regardless.

*The `(t, M, f)` hierarchy did real work.* Exact reconstruction is not the
property in dispute, exactly as §0 says: both methods reconstruct at
`~1e-15` and both are unique at rank 256, and the entire difference lives
in what was handed to the extractor and what basis it extracted in.
Without the hierarchy I would have had two self-consistent results and no
way to rank the causes.

**`REPOSITORY_DEFECT` — none reached the threshold of a stop.**

Two secondary observations:

*Method A's script hard-codes two frozen-document line numbers*
(`BASIS_BLOCK_LINE = 98`, `DECOMPOSITION_BLOCK_LINE = 116`) to locate the
freeze's JSON blocks. It works at this evidence base and this
adjudication's reproduction confirms it, but an inserted line anywhere
above line 98 of the freeze would silently change which JSON the script
parses. This is Amendment L's shape — a fragile locator into a mutable
document — and it is not repaired here, per §5. **I record it as located
but not asserted as a defect**: it produces correct results today, and a
repair is a separate task with its own review.

*`CONVENTIONS.md`'s seventeen rules still have no structural validator*,
and the review supply protocol of §3 is precisely the kind of rule that
belongs there and currently lives nowhere. Unchanged from the previous two
reports.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — reported as a scoped
result, not as a stop.**

The adjudication did not need this outcome for its own question: the first
divergence is located, the attribution is complete, and the frozen
material settles which construction is the frozen one. What remains
genuinely unresolved is stated in §12, and the one item that carries this
character is: **whether a different but admissible pp slot map would move
the family support.** That is untested by the branch and untested here, and
no evidence in this report bears on it either way.

**`ENVIRONMENT` — none.** No environment failure occurred, so neither of
Rule 13's two diagnostic orders was exercised. Nothing was installed.

**Things I would have specified differently.**

*A1(b)'s commit-pinned pattern should be the default for cross-branch
inputs, and I would say so in `CONVENTIONS.md`.* It is the cleanest
governance idea in this specification: the commit is the pin, the digest is
measured and recorded, and there is nothing for an author's belief to
corrupt. It also removes a whole failure mode — the author-supplied digest
that turns out to describe a different file — without adding a check that
can go stale.

*§3's heading should say what the Reviewer said it should.* "Stopping at
the first divergence" contradicts the body's "record it and CONTINUE".
The body is unambiguous and I followed it, but the heading is the part a
reader skims, and in this task the continued layers are where the answer
came from.

*A7's four cases are ordered by cause but not by likelihood, and the
ordering matters.* The first case — "the canonical construction itself" —
sounds like the least interesting and turned out to be the true one, while
the second, which the specification's §0 spends most of its argument on,
was excluded by a check the specification only asked for as a guard. I
would keep the guard exactly as written; it is what stopped a wrong,
larger-sounding conclusion. But I would drop the framing that treats one
case as the expected outcome, because it makes the correct answer feel like
an anticlimax rather than a result.
