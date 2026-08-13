# `P2-PHASE-01` C-check line — register of open items

**This is a register of open items arising from the C-check line** — the
follow-up checks `C1`, `C2` and `C3` commissioned by
`derivations/P2-PHASE-01_microscopic_parameter_domain.md`.

**Nothing in this file is a PI decision.** **Entries are added only by a task
authorised to do so**, and this file is not
`derivations/P2-DEFERRED-ITEMS.md`, whose own closing text states that its
entries are added by PI decision and which is not modified by the task that
created this register.

**Three entries. Each states what is known, what is not, and where the evidence
sits.**

---

## `OPEN-CC-1` — the adopted artifact's §5a CAUTION is partly settled and its text is not

**PARTLY SETTLED.**

`C1` established the first disjunct: **the production complement root is NOT
constructed from the ordinary root, but recovered by a separate bracketed
search.**

**THE SECOND IS NOT SETTLED** — why the stored pairs mirror bit-exactly is
unresolved, and `OPEN-CC-3` records the mechanism as open.

**The adopted artifact on the branch still presents the whole provenance question
as open, which is now wrong about the first disjunct and right about the
second.** Amending it is a later task; the branch is not integrated.

**An earlier draft of this entry said both disjuncts were resolved and that the
exactness IS a search-structure artefact; that contradicted §0 and `OPEN-CC-3`
in the same document and is corrected here.**

**Where the evidence sits:** `derivations/P2-PHASE-01_C1_complement_root_provenance.md`
and its report, on `science/c1-complement-root-provenance`.

---

## `OPEN-CC-2` — what the de-duplication threshold suppresses is undetermined

**UNDETERMINED.**

Line 167 of the exploratory script discards a returned bracket root lying within
`2.0e-4` of one already held, and the trivial root `0.0` is held first. At
`G/Gc = 1.00` the stored output carries the complement root near `-8` and the
trivial root, and no near-origin non-trivial root.

**WHAT IS ESTABLISHED:** the de-duplication suppresses the separately searched
near-zero bracket representative when it lies within `2.0e-4` of the
already-recorded trivial root.

**WHAT IS NOT:** whether a **distinct** stationary root was thereby lost. At
criticality the near-origin non-trivial solution merges with the trivial one, so
suppressing it may be correct branch-coalescence handling rather than a
completeness defect.

**An earlier draft called this "a measured exception to root completeness"; that
was stronger than the evidence.**

**Where the evidence sits:** `scripts/p2_phase01_scalar_exploratory.py` line 167
and the `G/Gc = 1.00` root records of
`results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json`, both
at `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`.

---

## `OPEN-CC-3` — the mechanism of the bit-exact mirroring is unresolved

**UNRESOLVED.**

`C1`'s report argued that reflection exchanges which endpoint's sign is tested,
so the bisection paths stay complementary through all 17 iterations, and
separately that both roots lie on a dyadic lattice of `2**-15`.

**A simulation on a bit-exactly symmetric toy function over the same two
brackets does NOT reproduce the complementarity:** the paths diverge at the
fourth iteration and the residual is one bisection step,
`6.103515625e-05`.

**AND THE DYADIC ARGUMENT DOES NOT STAND ALONE:** lying on a common lattice
guarantees only that both roots are integer multiples of `2**-15`; it does not
make the two integer indices sum to `-8 x 32768`. **Ninety exact pairings still
require a mechanism that preserves the mirrored index, and no established
argument supplies one.**

**THE OBSERVATION IS MEASURED AND STANDS** — 186 roots on the lattice, 90 pairs
summing to exactly `-8.0` — **but `C1`'s EXACTNESS PROVENANCE verdict rests on
an argument with a counterexample and an argument that is insufficient. It
should not be cited as settled.**

**Where the evidence sits:** the stored root table of
`results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json`;
`scripts/p2_phase01_scalar_exploratory.py` lines 138–169; and `C1`'s report,
whose exactness argument this entry qualifies.
