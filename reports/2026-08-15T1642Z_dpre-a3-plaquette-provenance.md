# Execution report — `D-pre-A3`: the provenance of the staggered plaquette phase

**Specification:** `specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md`
**Specification evidence base:** `773dd2cb2ad8fb457e23150f0cb19ab80dd614a5`
**Branch:** `science/dpre-a3-plaquette-provenance`, cut from authoritative `main` @ `773dd2cb…`
**Classification:** MATERIAL. Governed by Rule 15, Rule 18, and **Amendments M–P and Rules 19–21.**

**Every figure below is labelled MEASURED, DERIVED, VERIFIED, INTENDED or NOT
ESTABLISHED.** **This report is written at commit 3 and measures nothing at
commit 4.**

**This task does not touch `main`.** It produces a branch. **It asks where a
structure comes from and does not ask what the answer implies for any
candidate.**

---

## 1. Outcome

**VERDICT: `REPRESENTATION-EQUIVALENT`.** It stands in the artifact's first
line after the title, and its consequence is transcribed verbatim from §3 —
**VERIFIED fragment by fragment against the committed specification bytes.**

**The derivation closes.** `P_μν(x)·1₄ = Γ(x)† C_μν Γ(x)`, and because `C_μν`
is a scalar the conjugation drops out. **VERIFIED over 486 cases with maximum
deviation `0.00e+00`.**

**MEASURED at commit 3:** 3 additions and 0 modifications; **419 of 419 paths
at the evidence base blob-identical**; validators unchanged at 324 passed, 2
deselected; all four checker invocations exit 0 with `overall: PASS` and `P7`
reading fourteen sections; **`RUN 1` completes**, as A12 predicted it would.

**The companion question has the same answer.** The translation defect is pure
gauge, so the translation sector contributes no invariant of its own. **The two
questions turn out to be one question**, which §2a anticipated would be a
stronger result than either alone.

**One method error of mine is recorded rather than hidden**, §11.2: the
plaquette computed with periodic identification at odd extent returns mixed
values, which is a wrap artefact.

**No candidate is eliminated, preferred, ranked or recommended.**

---

## 2. Refs and inputs — A1

**MEASURED, `refs/heads/main` read from `origin` with `git ls-remote`:**

    refs/heads/main    773dd2cb2ad8fb457e23150f0cb19ab80dd614a5

**Matches the specification. No mismatch, no STOP.**

**Blob ids at the evidence base, MEASURED:**

    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md
                                          0b227206f3561144b4d5ea869390341aeefddc29
    derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md
                                          fb2f51479bf03daeaed145a2ee48da58aab66f34
    derivations/P2-LATTICE-ONTOLOGY-01.md
                                          6544fb1a72eff49b4af4a1767d63405ddb87e4b8

---

## 3. The review binds to these bytes — A2, checked in the order the criterion sets

**A2 requires the field checked for PRESENCE before it is checked for MATCH,
because the previous task's review failed at the first step and a match test
alone would have reported nothing useful.**

**Step 1 — presence. MEASURED:**

    'reviewed specification SHA-256' occurrences     1
    64-hex strings in the review                     1

**Step 2 — match. MEASURED:**

    SHA-256 of the arriving specification    df46da1f7d52dd7fb8633d5c860f570a33fecac7b214c4c27d3a2295e06251bf
    SHA-256 the review records as reviewed   df46da1f7d52dd7fb8633d5c860f570a33fecac7b214c4c27d3a2295e06251bf

**Equal.** Both arriving files committed byte-identical, verified by `cmp`;
neither modified.

**`G-05` remains the reason this had to be checked by hand.** Nothing in the
repository compares a review's cited digest against the specification committed
beside it; a per-task criterion did it, and the previous task shows what
happens when the field is simply absent.

---

## 4. The two structures, before the derivation — A3

**All four items were established before §5's derivation was attempted**, so
that the derivation could not be steered by knowing where it should land.

### 4.1 (i) The staggered plaquette on all six planes — MEASURED

**Computed with integer shifts and NO modular identification** — §11.2 explains
why that qualifier is load-bearing.

    plane (1,2)  {−1}     plane (2,3)  {−1}
    plane (1,3)  {−1}     plane (2,4)  {−1}
    plane (1,4)  {−1}     plane (3,4)  {−1}

**Repeated at three extents.** The union of all values over all six planes and
all sites is `{−1}` at `3⁴ = 81`, at `4⁴ = 256` and at `5⁴ = 625` base sites.

### 4.2 (ii) Invariance under site-sign redefinition — PROVED for arbitrary `ε`

**A statement about all `ε` needs a proof about all `ε`.** Under
`η'_μ(x) = ε(x) η_μ(x) ε(x+μ̂)`, expanding the four plaquette links gives

    ε(x)² · ε(x+μ̂)² · ε(x+ν̂)² · ε(x+μ̂+ν̂)² · P_μν(x)

**because the loop has four corners and each is an endpoint of exactly two of
the four links.** Since `ε ∈ {±1}`, every square is `1`, so
`P'_μν(x) = P_μν(x)` **for every `ε`, every `x` and every plane.** ∎

**The argument uses only that the loop is closed and that every element of
`{±1}` is its own inverse.** It does not depend on the particular `η`, on the
lattice extent, or on sampling.

### 4.3 (iii) The fixed-seed sanity check — MEASURED

    seed                             20260815
    ε drawn over the 5⁴ span         314 of 625 sites negative
    base sites checked               3⁴ = 81, all six planes
    plaquette unchanged everywhere   True
    transformed values               {−1}

**This supplements §4.2 and does not replace it.** A finite number of draws
cannot establish a statement quantified over all `ε`, and the specification is
right that an earlier form of this criterion asking only for one draw was
weaker than it appeared.

### 4.4 (iv) The Clifford group commutator — MEASURED, representation stated and verified

    γ_1 = σ_x ⊗ σ_x    γ_2 = σ_x ⊗ σ_y    γ_3 = σ_x ⊗ σ_z    γ_4 = σ_y ⊗ 1₂

**VERIFIED before use: `{γ_μ, γ_ν} = 2δ_μν · 1₄` for all sixteen pairs, and all
four hermitian.**

    plane (1,2)  C_μν = −1 · 1₄     plane (2,3)  C_μν = −1 · 1₄
    plane (1,3)  C_μν = −1 · 1₄     plane (2,4)  C_μν = −1 · 1₄
    plane (1,4)  C_μν = −1 · 1₄     plane (3,4)  C_μν = −1 · 1₄

**MEASURED: in every case the commutator is a SCALAR multiple of the
identity** — verified as scalar, not read off one entry. **That scalarity is
load-bearing in §5 Step 6 and is not incidental.**

### 4.5 The agreement between (i) and (iv) is NOT the verdict

**Stated here in the same breath as the four items, as A3 requires.**

**Both equal `−1` on the same six planes, and that is the reason to ask the
question rather than the answer to it.** **Coincidence of value is not identity
of structure.** Two objects can agree in every case and be different
structures.

**It would have been wrong in either direction.** `REPRESENTATION-EQUIVALENT`
asserted from the matching values would have been unsupported; and so would
`STAGGERED-SPECIFIC` asserted in spite of them. **The verdict rests on §5's
structural mapping and on nothing else.**

---

## 5. The derivation, every step — A4

**Starting identity, taken from the dossier's §3.3 and not re-derived:**

    Γ(x)† γ_μ Γ(x+μ̂) = η_μ(x) · 1₄        (★)

**`Γ(x)` is unitary. DERIVED:** each `γ_μ` is hermitian with `γ_μ² = 1`, hence
unitary; a product of unitaries is unitary. **VERIFIED:
`max |Γ(x)†Γ(x) − 1₄| = 0` over all 81 sites.**

**The plaquette in oriented form**, around `x → x+μ̂ → x+μ̂+ν̂ → x+ν̂ → x`:

    P_μν(x) = η_μ(x) · η_ν(x+μ̂) · η_μ(x+ν̂)⁻¹ · η_ν(x)⁻¹

Each `η = ±1` is its own inverse, so this equals the unsigned product. **The
oriented form is used because it is the form that maps onto a group
commutator.**

**Step 1 — invert (★) for the two reversed links**, using `Γ† = Γ⁻¹` and
`γ_μ⁻¹ = γ_μ`:

    η_μ(x)⁻¹ · 1₄ = [Γ(x)† γ_μ Γ(x+μ̂)]⁻¹ = Γ(x+μ̂)† γ_μ⁻¹ Γ(x)

**Step 2 — write each of the four factors via (★):**

    η_μ(x)      · 1₄ = Γ(x)†       γ_μ    Γ(x+μ̂)
    η_ν(x+μ̂)   · 1₄ = Γ(x+μ̂)†    γ_ν    Γ(x+μ̂+ν̂)
    η_μ(x+ν̂)⁻¹ · 1₄ = Γ(x+ν̂+μ̂)†  γ_μ⁻¹  Γ(x+ν̂)
    η_ν(x)⁻¹    · 1₄ = Γ(x+ν̂)†    γ_ν⁻¹  Γ(x)

**Step 3 — multiply in loop order.** The `η` are scalars, so their product is
`P_μν(x)`:

    P_μν(x) · 1₄ = Γ(x)† γ_μ Γ(x+μ̂) · Γ(x+μ̂)† γ_ν Γ(x+μ̂+ν̂)
                   · Γ(x+ν̂+μ̂)† γ_μ⁻¹ Γ(x+ν̂) · Γ(x+ν̂)† γ_ν⁻¹ Γ(x)

**Step 4 — the interior telescopes**, three cancellations of `Γ Γ† = 1₄`:

    Γ(x+μ̂) Γ(x+μ̂)†       = 1₄
    Γ(x+μ̂+ν̂) Γ(x+ν̂+μ̂)†  = 1₄     the same site, since x+μ̂+ν̂ = x+ν̂+μ̂
    Γ(x+ν̂) Γ(x+ν̂)†       = 1₄

**The second cancellation is the one that requires the loop to close**, both
paths reaching the same corner. **That is where closure enters the algebra
rather than the prose**, and it is the step that would fail for an open path.

Leaving:

    P_μν(x) · 1₄ = Γ(x)† [ γ_μ γ_ν γ_μ⁻¹ γ_ν⁻¹ ] Γ(x) = Γ(x)† C_μν Γ(x)

**Step 5 — VERIFIED.** Over `81 sites × 6 planes = 486` cases, the identity
holds with **maximum deviation `0.00e+00`.**

**Step 6 — the conjugation drops out**, because `C_μν = −1 · 1₄` is a scalar
and a scalar commutes with everything:

    Γ(x)† (−1 · 1₄) Γ(x) = −1 · Γ(x)†Γ(x) = −1 · 1₄

    ⟹  P_μν(x) = −1   for every x and every plane.   ∎

**No step is asserted.** Steps 1–4 are algebra from (★) and unitarity; Step 5
is a verification of the resulting identity; Step 6 uses §4.4's measured
scalarity.

### 5.1 What closes, and what it explains

**`P_μν` IS `C_μν`, written in the variables spin diagonalisation produces.**
The result of §5 is an identity between the two objects, not an agreement
between two numbers.

**Three facts previously observed separately are consequences of the one
identity:**

- **why the value is `−1`** — it is `C_μν`'s value, and nothing else enters;
- **why it is site-independent** — `C_μν` is scalar, so the `Γ(x)`
  conjugation, the only `x`-dependence in the expression, cancels;
- **why it is redefinition-invariant** — proved independently in §4.2, and
  explained here: the redefinition acts on `Γ`, and a scalar is invariant under
  conjugation.

**The site-independence and the redefinition-invariance have the same cause**,
which no argument from matching values could have shown. **That is the
difference between the verdict this task reached and the verdict §0 forbade
reaching.**

---

## 6. The four candidates — A5

**Each row is derived. Analysing staggered alone would have been looking for
staggered's problem**, which is the failure mode this task inherits from
`D-pre-A`'s `A10`.

    candidate    invariant structure          how represented
    naive        C_μν = −1 on all six planes  gamma matrices, explicitly
    Wilson       C_μν = −1 on all six planes  gamma matrices; r-term is scalar
    staggered    P_μν = −1 on all six planes  link phases; = C_μν by §5
    overlap      C_μν = −1 on all six planes  gamma matrices; scalar prefactors

**DERIVED and VERIFIED for Wilson and overlap:** adding any scalar multiple of
`1₄` to a gamma leaves `[γ_μ, γ_ν]` unchanged, so the Wilson `r W(p)` term and
the overlap's `(W − M_0)` and inverse-square-root factors — all multiples of
`1₄` in Dirac space — commute through and contribute nothing to the commutator.
**Non-ultralocality does not bear on this**: the overlap's scalar prefactor is
a function of momentum, not of the Dirac index.

**All four carry the same invariant. They differ in representation and not in
the structure represented.**

### 6.1 Derivation length per candidate, and whether the table is symmetric

**MEASURED, non-blank lines in each candidate's dedicated subsection:**

    naive       9
    Wilson      7
    staggered   9
    overlap     9

    range 7–9, spread 2

**The table is symmetric in depth**, and this is the closest to level any
candidate table in this line has been. **Wilson's 7 is the shortest because its
entry cites naive's argument for the gamma representation rather than repeating
it**, and adds only the scalar-term observation.

**Whole-artifact mentions by name, MEASURED: naive 5, Wilson 3, staggered 9,
overlap 2.** **staggered's 9 is disclosed rather than smoothed**: the question
is about a staggered object, so the derivation of §5 names it throughout. **The
structured measure — the four rows of §6, each derived, at 7 to 9 lines — is
the one that speaks to symmetry**, and the mention count reflects which
formulation the question was asked about.

---

## 7. The companion question — A6

**§2a asks whether the translation side carries a redefinition-invariant
structure and whether it is the same one.**

**The 96 mismatches, RE-MEASURED here rather than quoted** from lines 224–235
of the discriminants artifact:

    translation along axis 1    48
    translation along axis 2    32
    translation along axis 3    16
    translation along axis 4     0
    TOTAL                       96

**The split is reported because the total conceals it.** **DERIVED: axis 4 has
zero because `η_μ(x)` depends only on coordinates with index `< μ`, so shifting
the last axis changes no phase.** The quoted 96 is confirmed, and its
composition is new here.

**The naive candidate for a translation invariant FAILS. DERIVED and MEASURED:**
`T_μν(x) ≡ η_μ(x+ν̂) η_μ(x)` is the constant sign `(−1)^{[ν<μ]}`. Under
`η → εηε` its four `ε` factors sit on **four distinct sites, each appearing
once**, so they do not cancel. **`T` is not redefinition-invariant** — and the
contrast with §4.2 is exact: the plaquette's `ε` cancel because the loop is
closed, and `T`'s do not because it is not a loop.

**The translation defect is PURE GAUGE. VERIFIED** by exhaustive search over
all `2¹⁶` sign assignments on the `2⁴` block: **a restoring `ε` exists for each
of the four axes, 4 of 4.**

**Consequence, DERIVED and then VERIFIED directly:** gauge-equivalent
configurations agree on every redefinition-invariant quantity, so the
translated configuration must carry the same plaquettes — **and computed
directly, the translated configuration's plaquettes are `{−1}` on all six
planes for each of the four axes.**

**ANSWER: the translation sector carries no redefinition-invariant structure of
its own.** Its non-invariance is entirely removable, and the one invariant
present is `P_μν` — **the same structure**, which §5 identifies as `C_μν`.

**So the two questions have one answer.** §2a anticipated that if the two
structures turned out to be one it would be a stronger result than either
alone, and that is what happened: **the axis-permutation sector and the
translation sector are not two structures but one, and that one is the Clifford
anticommutation structure.**

**This did not affect §8's verdict**, and §2a is explicit that it must not.

---

## 8. The verdict and its consequence — A7

**VERDICT: `REPRESENTATION-EQUIVALENT`.**

**MEASURED: it stands in the artifact's first line after the title**, before
any other content.

**The consequence, transcribed verbatim from the specification's §3:**

> **Consequence:** **this cheap discriminator is closed.** The four
> candidates do not differ **at the structure tested here**, and **this
> task proposes no further representation-level discriminator.**
>
> **Among the formulation-discriminating requirements ALREADY IDENTIFIED,
> reflection positivity remains outstanding and requires a transfer matrix
> that does not exist.** **State that; do not scope it.**
>
> **THIS TASK DOES NOT ESTABLISH THAT REFLECTION POSITIVITY IS THE ONLY
> POSSIBLE REMAINING DISCRIMINATOR.**

**VERIFIED fragment by fragment against the committed specification bytes**:
each of the four load-bearing fragments is present in both the specification
and the artifact, character for character after normalising the blockquote
prefix and line wrapping. **Nothing was rewritten, shortened or paraphrased.**

**The verdict was reachable.** §3's outcome space is `REPRESENTATION-EQUIVALENT`,
`STAGGERED-SPECIFIC` or `NOT ESTABLISHED`, with a `SPECIFICATION_DEFECT` stop
if the derivation establishes something none represents. **The derivation
established exactly the first**, and no stop was needed.

---

## 9. No elimination, no preference — A8

### 9.1 The search

**Run over the artifact, this report and the commit messages**, for
`eliminat*`, `prefer*`, `favour`/`favor*`, `rank*`, `recommend*`, `superior`,
`better`, `worse`, `best`, `worst`, `disqualif*`, `admissib*`, `inadmissib*`,
`rules out`, `should be chosen`/`selected`/`adopted`, and for `burden`,
`problem*`, `anomal*`, `defect` as characterisation words.

**MEASURED in the artifact: 11 hits, none of which eliminates, favours, ranks
or recommends.** They fall into three classes:

    the explicit denials              lines 19–20, 360, 376–386
    the methodological framing        line 234, "looking for staggered's
                                      problem" — the specification's own phrase
                                      for analysing one candidate alone
    technical uses of "defect"        line 324, "the translation defect is PURE
                                      GAUGE" — an obstruction that is removable,
                                      and the sentence says it is removable;
                                      line 356, "a defect in the result",
                                      about my own method error

**MEASURED over the commit messages: 5 hits, all denials or the same
methodological framing.**

**No sentence in the artifact, this report, or any commit message eliminates,
favours, ranks or recommends a candidate, or draws an admissibility conclusion
from a structural finding.**

### 9.2 How the difference is characterised

**A8 asks how the difference is characterised and requires the
characterisation to be neutral as to admissibility.**

**MEASURED: under this verdict there is no difference to characterise.** The
finding is that all four candidates carry the **same** invariant, differing in
representation only. **A8's concern — that a `STAGGERED-SPECIFIC` verdict
written in the language of burden would take a position without stating one —
does not arise, because the verdict is not `STAGGERED-SPECIFIC`.**

**I did not manufacture a difference in order to have one to characterise
neutrally.** The artifact's §8 records what the boundary would have been had
the verdict gone the other way: **a difference in structure is not a difference
in admissibility**, and whether a uniform `π` flux on a physically real
substrate would be a defect or a feature is a PI ruling this task does not
prepare.

**Where the artifact does describe staggered's representation as different —
link phases rather than gamma matrices — that is a statement about variables,
not about merit**, and it is paired in the same table with the statement that
the structure represented is identical.

---

## 10. Scope, protected paths, gates, checker, validators — A9–A14

**A9, MEASURED at commit 3:**

    A  derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md
    A  reviews/chatgpt/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md
    A  specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md

    3 additions, 0 modifications

**MEASURED: no status code other than `A` appears.** **`modify:` is `[]` and
remained so.**

**INTENDED, base to commit 4:** 4 additions and 0 modifications, the fourth
addition being this report. **INTENDED, not MEASURED: this report is written
before the commit containing it.**

**A10, MEASURED path by path:**

    paths at the evidence base      419
    compared                        419
    blob-identical                  419
    differing                         0
    missing at head                   0

**Nothing existing changed, and the comparison excludes no path**, because this
task's manifest modifies none.

**The named ones, MEASURED individually — all IDENTICAL:**

    GATES.md
    derivations/P2-LATTICE-ONTOLOGY-01.md
    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md
    derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md
    derivations/P2-DEFERRED-ITEMS.md        (the deferred register)
    docs/GOVERNANCE-DEBT.md                 (the governance-debt register)

    everything under scripts/, tests/, results/:   0 paths changed

**Both microspec artifacts were read and not modified. Neither register was
touched. No script was run.**

**A11, all four invariants, MEASURED at commit 3:**

    1.  ^## P2- count                14
    2.  P2-PHASE-01                  Status: PROPOSED
    3.  first prerequisite           Prerequisite state: SATISFIED
    4.  second prerequisite          Prerequisite state: SATISFIED

    both pins match their targets:
      line 1017   MATCH        line 1040   MATCH

**No gate state was changed.** This task modifies no pinned file, so no re-pin
is owed under Rule 19.

**A13, MEASURED, exit status 0 both times:**

    before, at the base 773dd2cb     324 passed, 2 deselected
    after,  at commit 3              324 passed, 2 deselected

**Unchanged, as expected: this task adds no test.** **No change to explain.**

**A14, MEASURED on commits 1–3. Commit 4 is post-report evidence.**

    commit 1   36dd627f   spec: the provenance of the staggered plaquette phase
               trailer hits 0      not amended
    commit 2   4bddf8bb   review: pre-execution review for the plaquette provenance
               trailer hits 0      not amended
    commit 3   f2fe7036   derivations: the staggered plaquette is the Clifford commutator in phase variables
               trailer hits 0      not amended

**MEASURED over the whole range: a scan for `Co-Authored-By`, `claude.ai/code`,
`Generated with`, `Claude-Session` and `noreply@anthropic` returns nothing.**

**Rule 20 binds this task and was NOT exercised.** **No force-push, no branch
deletion, no history rewrite of any kind.**

**Commit 4's message, INTENDED:**

    report: the plaquette is the Clifford commutator in phase variables

---

## 11. The checker — A12, MEASURED at commit 3

    base   773dd2cb2ad8fb457e23150f0cb19ab80dd614a5
    head   f2fe7036fb500badc341d670790bc77617646fff   (commit 3)

**All four invocations exited 0 with `overall: PASS`.**

    run 1 INCLUSIVE   exit 0   PASS   sha256 aa927f2baae555306db6ca9c6ba611d414c694516083f6107bda24f54132a5ca
    run 1 EXCLUSIVE   exit 0   PASS   sha256 89d671cd85955f3ef2fdee104d2e3ab66fec3cc880084ee1c402f5cdfe15cfce
    run 2 INCLUSIVE   exit 0   PASS   sha256 aa927f2baae555306db6ca9c6ba611d414c694516083f6107bda24f54132a5ca
    run 2 EXCLUSIVE   exit 0   PASS   sha256 89d671cd85955f3ef2fdee104d2e3ab66fec3cc880084ee1c402f5cdfe15cfce

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 NOT_APPLICABLE
    P6 PASS   P7 PASS   P8 PASS   P9 NOT_APPLICABLE

### 11.1 What `RUN 1` did — the question A12 asks explicitly

**A12 predicts that `RUN 1` selects one specification in this range and so
should not hit the multi-specification declaration conflict the previous task
met, and asks what it actually did.**

**MEASURED: `RUN 1` completed. It did not raise.**

    specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md
        stated add 4 modify 0    counted add 4 modify 0    parse OK

**One specification selected, exactly as predicted.** **MEASURED: `RUN 1` and
`RUN 2` are byte-identical at each prospectivity reading** — the sha256 pairs
above are equal — because the default selection and the named selection
coincide.

**That the previous task's failure does not recur here confirms its
diagnosis.** The limitation is specific to a range containing several
specifications whose declarations legitimately differ, which is a multi-source
integration's shape and not a single-branch task's. **It remains an
unregistered `C3` residual; this task adds no register entry.**

### 11.2 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "773dd2cb2ad8fb457e23150f0cb19ab80dd614a5",
      "head": "f2fe7036fb500badc341d670790bc77617646fff",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 11.3 RUN 2 config, verbatim — stop-governing

    {
      "base": "773dd2cb2ad8fb457e23150f0cb19ab80dd614a5",
      "head": "f2fe7036fb500badc341d670790bc77617646fff",
      "specification_paths": ["specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I chose**; all are fixed by A12. **Neither
the config nor this specification's declarations were adjusted to make RUN 2
pass** — §8 forbids both, and neither was touched.

### 11.4 `declared_source`, `P3` and `P7`

**MEASURED, identical in all four invocations:**

    P3   PASS   declared_source: specification   declared: ['DECISION_LOG.md']
           DECISION_LOG.md   PASS   deleted 0   base is byte prefix of head: True
    P7   PASS   declared_source: specification   declared: []
           raw_heading_count_head 14      section_count_head 14

**`P7` reports fourteen sections. `PASS` at zero would have been a STOP.**

**MEASURED: `DECLARATION_CONFLICT` appears nowhere in any of the four
outputs.** The config supplied the same single path the scope block declares,
so the precedence rule resolved to `specification` with nothing to conflict.

**`DECISION_LOG.md` is not modified by this range**, so its `PASS` records an
absence of change rather than a verified append — the same distinction the
previous task's report drew, and it applies to the only declared path here.

### 11.5 RUN 2 output, verbatim, INCLUSIVE reading

    {
      "base": "773dd2cb2ad8fb457e23150f0cb19ab80dd614a5",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "f2fe7036fb500badc341d670790bc77617646fff",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "append_only": [
                "DECISION_LOG.md"
              ],
              "authorised_gates": [],
              "counted": 4,
              "counted_add": 4,
              "counted_modify": 0,
              "counted_set": [
                "derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md",
                "reports/2026-08-XXT{HHMM}Z_dpre-a3-plaquette-provenance.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_dpre-a3-plaquette-provenance.md",
                "specs/2026-08-XXT{HHMM}Z_dpre-a3-plaquette-provenance.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md",
              "stated": 4,
              "stated_add": 4,
              "stated_modify": 0,
              "stated_record": "stated: 4 additions, 0 modifications"
            }
          ],
          "id": "P1",
          "status": "PASS",
          "title": "scope manifest arithmetic"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "commits": [
              {
                "adds_review": false,
                "commit": "36dd627fdad09a4512bd42dc69d8271fd915619b",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "4bddf8bbf2619d2f18a808d5bcda196c3bc941df",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "f2fe7036fb500badc341d670790bc77617646fff",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md"
                ]
              }
            ],
            "first_review_commit": "4bddf8bbf2619d2f18a808d5bcda196c3bc941df",
            "first_work_commit": "f2fe7036fb500badc341d670790bc77617646fff",
            "in_scope": 3,
            "out_of_scope": []
          },
          "id": "P2",
          "status": "PASS",
          "title": "Rule 15 commit order"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
          "evidence": {
            "declared": [
              "DECISION_LOG.md"
            ],
            "declared_by_specification": [
              "DECISION_LOG.md"
            ],
            "declared_key": "append_only",
            "declared_source": "specification",
            "paths": [
              {
                "base_bytes": 89541,
                "base_is_byte_prefix_of_head": true,
                "commits_with_deletions": [],
                "deleted_lines_base_to_head": 0,
                "head_bytes": 89541,
                "path": "DECISION_LOG.md",
                "status": "PASS"
              }
            ],
            "specification_paths_read": [
              "specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md"
            ],
            "supplied_by_config": [
              "DECISION_LOG.md"
            ]
          },
          "id": "P3",
          "status": "PASS",
          "title": "append-only on both measures"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "entries": [
              {
                "branch": "fix/pi-decisions-and-deferred",
                "commit": "52f651174dc1fef03b4fb9276078fa1f08d94bd7",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "fix/pi-decisions-v2",
                "commit": "ebd531ab568aaffabd86a4a94d925a711e62aa36",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-v2",
                "commit": "40168469608618aef6812735ff70e32de0e3cbc8",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-and-superseded",
                "commit": "7146a093c65788a57d63a747b71d86edb91eddc6",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "review/role-model-and-executors",
                "commit": "10c260b96882ac12610f78840aeeabd07be2d7cb",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "gate/p2-land-diquark-line",
                "commit": "d64cd912ca9ff78a85787f0e54f345f474cdb192",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              }
            ],
            "register_path": "docs/BRANCHING_POLICY.md"
          },
          "id": "P4",
          "status": "PASS",
          "title": "superseded branches are not merged"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the executor derived the parentage values independently; three correct values are equally consistent with fresh recomputation and with one field copied into another. The diquark task's shared-rationale defect would pass this check.",
          "evidence": {
            "merges": []
          },
          "id": "P5",
          "reason": "no merge commit in range",
          "status": "NOT_APPLICABLE",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "36dd627fdad09a4512bd42dc69d8271fd915619b",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "4bddf8bbf2619d2f18a808d5bcda196c3bc941df",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "f2fe7036fb500badc341d670790bc77617646fff",
              "matches": [],
              "status": "PASS"
            }
          ],
          "id": "P6",
          "status": "PASS",
          "title": "commit-message hygiene"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
          "evidence": {
            "added_sections": [],
            "authorised_modified": [],
            "declared": [],
            "declared_by_specification": [],
            "declared_key": "authorised_gates",
            "declared_source": "specification",
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "specification_paths_read": [
              "specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md"
            ],
            "supplied_by_config": [],
            "unauthorised_changed": []
          },
          "id": "P7",
          "status": "PASS",
          "title": "gate integrity"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "first_commit": "36dd627fdad09a4512bd42dc69d8271fd915619b",
            "first_commit_paths": [
              "specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {},
          "id": "P9",
          "reason": "range adds no report",
          "status": "NOT_APPLICABLE",
          "title": "reports carry a Stops and clarifications section"
        }
      ],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 3,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

---

## 12. Commits

    commit 1   36dd627fdad09a4512bd42dc69d8271fd915619b   specs/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md
    commit 2   4bddf8bbf2619d2f18a808d5bcda196c3bc941df   reviews/chatgpt/2026-08-15T1642Z_dpre-a3-plaquette-provenance.md
    commit 3   f2fe7036fb500badc341d670790bc77617646fff   derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md

---

## 13. Did the derivation make me want to draw an admissibility conclusion?

**Asked by §9, and the answer is yes — once, sharply, and at a specific
moment.**

**The moment was Step 6.** When the conjugation dropped out and `P_μν = −1`
fell straight out of the Clifford commutator, the result felt like it had
settled something about staggered — that the flux is "not really there", that
it is an artefact of a change of variables, that staggered was under a
suspicion which has now been lifted. **All three of those are wrong, and the
third is the seductive one**, because it sounds like exoneration and
exoneration sounds neutral.

**Nothing was ever under suspicion.** The integration that put this question on
`main` carried it explicitly as a question, and the earlier draft that called
the flux "a physical difference between candidates" was retracted before it
landed. **A verdict cannot lift a suspicion that the record does not contain**,
and writing as though it had would have imported the very framing the
retraction removed.

**The second pull was toward the word "merely".** The flux is not *merely* a
representation artefact — it is the Clifford anticommutation structure, which
is as real in staggered as in the other three, just written in different
variables. **"Merely" would have demoted a structure all four candidates
carry**, and it appears nowhere in the artifact.

**A third pull, weaker but worth naming, ran the other way.** The derivation is
clean enough that it is tempting to present it as closing more than it does —
as showing the four candidates are equivalent, rather than that they agree at
one tested structure. **§7 of the artifact states the limit**, and §14.4 states
it again.

**I confirm I drew no admissibility conclusion**, eliminated, preferred, ranked
and recommended no candidate, ruled on neither `D-pre-A2` question, proposed no
ontology requirement, constructed no transfer matrix, attempted no reflection
positivity, ran no script, and modified no existing file.

---

## 14. Rule 16 assessment — what the assembled set does NOT establish

**Rule 16 is operative. All four junctions are addressed.**

### 14.1 First junction — a structural finding is not an admissibility finding

**Had `P_μν` proved staggered-specific, nothing would have followed about
whether staggered may be canonical.** **Deciding whether a uniform `π` flux on
a physically real substrate is a defect or a feature is a PI ruling this task
does not prepare** — and does not anticipate.

**The verdict went the other way, and the same boundary holds in this
direction.** `REPRESENTATION-EQUIVALENT` does not make any candidate more
admissible, and it does not remove an objection, because no objection was on
the record to remove. **It says the four agree at one tested structure. That is
all it says.**

### 14.2 Second junction — this closes a route and opens none

**`REPRESENTATION-EQUIVALENT` closes this cheap discriminator.** **This task
proposes no further representation-level discriminator**, and none was
manufactured when the derivation closed.

**Of the formulation-discriminating requirements ALREADY IDENTIFIED, reflection
positivity is the outstanding one.** It is `NOT ESTABLISHED` for all four
candidates, it waits on a transfer matrix that does not exist, and that
construction **overlaps `D-pre-B`'s Euclidean–spectral equivalence**, which
needs transfer-matrix normalisation too.

**It is not scoped here**, and naming the overlap is not scoping it.

**This task does NOT establish that reflection positivity is the only
discriminator that could exist.** §14.4 is why, and the two statements agree:
one is about the requirements already identified, the other about the space of
possible requirements. **The specification's §3 and §7 were made to agree on
this before issue, and the report keeps them agreeing.**

### 14.3 Third junction — this is not corroboration of the dossier

**This task derives from an identity the dossier records at its §3.3.** **It
does not re-derive the dossier's species ledgers and does not check them.**

**A result consistent with the dossier is NOT corroboration of the dossier**,
because both rest on the same reconstruction (★). If (★) were wrong, this
derivation and the dossier's taste count would be wrong together, and their
agreement would be silent about it. **The agreement is a consequence of shared
machinery, not independent evidence.**

### 14.4 Fourth junction — one level, not every level

**The four candidates' redefinition-invariant structures are compared at ONE
level** — the plaquette, and after §7, the translation sector, which turns out
to be the same level rather than a second one.

**Nothing here establishes that no other redefinition-invariant structure
distinguishes the candidates.** Higher loops, larger Wilson-loop-like objects,
structures involving the mass terms, and anything outside the free-field
phase/gamma comparison were not examined. **A negative result at this level is
not a negative result at every level.**

**That is why §14.2 stops at "the outstanding one among those already
identified".**

---

## 15. Stops and clarifications

**No stop occurred.** All four checker invocations exited 0, RUN 2 passed at
both prospectivity readings, the derivation closed onto one of the three
pre-registered verdicts, and no acceptance criterion failed.

    SPECIFICATION_DEFECT                          0 stops, 0 findings
    ENVIRONMENT                                   0 stops, 0 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 2 findings
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 1 finding

### 15.1 `OBSERVATION_METHOD_ERROR` — two findings, both mine, both caught before they reached a commit

**First, and it is the substantive one: the plaquette computed with periodic
identification at odd extent returns mixed `{+1, −1}` values.** My first probe
used `L = 3` with modular wrap and reported that the product is **not**
uniformly `−1` — apparently contradicting what the specification takes as
given.

**Diagnosed rather than reported: `η_μ` is periodic only under shifts of EVEN
period**, so identifying `x + 3 ≡ x` flips signs that are not part of the local
structure. **The plaquette is a local object and must be computed with integer
shifts.** **Recomputed without modular identification, the product is uniformly
`−1` at `3⁴`, `4⁴` and `5⁴`.**

**This is recorded in the artifact at its §1 and §7.1**, because a reader
reproducing the measurement on a periodic odd lattice will disagree with it,
and the disagreement would be the reader's convention rather than a defect in
the result. **It is the one finding here that a future task could trip over
again.**

**Second, minor: my verbatim-transcription probe reported four of five
fragments missing from the artifact.** The probe normalised whitespace but did
not strip the blockquote `> ` prefixes the artifact uses to quote the
consequence. **Re-run with the prefixes stripped, all fragments match exactly.**
**No figure from the faulty probe reached a commit**, and §8 reports the
corrected result.

**Both are `G-11`'s shape** — a hand-written probe disagreeing with a written
figure — and in both cases the probe was wrong. **In the first the probe
disagreed with the specification and I suspected the probe; that was the right
order.**

### 15.2 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one finding, carried not resolved

**The `C3` residual the previous task surfaced remains unregistered**: the
declaration mechanism has no rule for a range whose specifications legitimately
declare different append-only sets. **§11.1 confirms the diagnosis by the
absence of the failure here** — one specification in range, `RUN 1` completes.

**No register entry is added**, §4 forbidding it. **Reported for whoever holds
the register.**

### 15.3 `SPECIFICATION_DEFECT`, `ENVIRONMENT`, `REPOSITORY_DEFECT` — nothing to report

**Nothing in this specification was found false about the repository or about
its own bytes.** Its scope block declares what §11.4 measured, and the
pre-registered verdicts covered the case the derivation reached.

**The pre-issue record's random-`ε` check is weaker than A3(ii) requires**, and
the review records that this is historical evidence needing no rewrite.
**Execution followed the stronger criterion**: §4.2 proves the arbitrary-`ε`
statement and §4.3 supplements it with a seeded check.

**No environment failure occurred.** **Rule 13 carries two diagnostic orders, a
known open item. Neither was exercised**, and I am not naming one as having
applied. **Nothing was installed.** Python 3.11.15 and pytest 9.1.1, as
present.

**No defect in the repository was found by this task.**

### 15.4 What I would have specified differently

**A3(i) asks for the plaquette product without specifying the boundary
convention**, and §15.1 shows the answer depends on it: periodic at odd extent
gives mixed values, integer shifts give `−1` uniformly. **The pre-issue record
says "over 81 base sites", which is `3⁴` — the extent at which the wrap
artefact appears if periodicity is applied.**

**I would have had A3(i) state "with integer shifts, no modular
identification".** The specification's figure is right and its method
description is silent on the one convention that changes the answer. **This
cost nothing here because the artefact was diagnosed rather than reported, but
a task that reported the mixed values as a finding would have contradicted a
correct specification on a convention neither document stated.**

**Nothing in the specification was unsatisfiable or ambiguous enough to require
a stop**, and the pre-registered verdict space covered the outcome without
renegotiation.

---

## 16. Evidence layering

**Committed in this report, MEASURED at commit 3:** A1–A11, A13 and A14 for
commits 1–3; A12's four invocations with both configs and the output; commits
1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; A9's final
base-to-commit-4 scope of 4 additions and 0 modifications.

**Post-report evidence, returned to the Reviewer and NOT written back:** A9's
final scope measured base-to-commit-4; A12-final, being RUN 2 re-run at commit
4; A13 at commit 4; A14 for commit 4; the push; the branch tip read back.

**Nothing in this report claims to measure commit 4.**

**This task does not touch `main`.** The branch is the outcome; integration is
a separate task. **It does not unblock `C-iii` or `D0`.**
