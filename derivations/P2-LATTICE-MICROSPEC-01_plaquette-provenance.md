# `P2-LATTICE-MICROSPEC-01` — the provenance of the staggered plaquette phase

**VERDICT: `REPRESENTATION-EQUIVALENT`.**

**Consequence, transcribed verbatim from the specification's §3:**

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

**This artifact asks where a structure comes from. It does not ask what the
answer implies for any candidate.** No candidate is eliminated, preferred,
ranked or recommended here, and no admissibility conclusion is drawn from a
structural finding.

**Evidence base:** `773dd2cb2ad8fb457e23150f0cb19ab80dd614a5`.

---

## 1. Conventions and the two objects

Euclidean hypercubic lattice, integer coordinates `x ∈ ℤ⁴`, unit vectors `μ̂`.
Euclidean gamma matrices hermitian with `{γ_μ, γ_ν} = 2δ_μν`.

**Staggered phases:** `η_μ(x) = (−1)^{x_1 + … + x_{μ−1}}`, so `η_1 ≡ 1`.

**The plaquette**, an oriented product around the closed loop
`x → x+μ̂ → x+μ̂+ν̂ → x+ν̂ → x`:

    P_μν(x) = η_μ(x) · η_ν(x+μ̂) · η_μ(x+ν̂)⁻¹ · η_ν(x)⁻¹

Each `η = ±1` is its own inverse, so this equals the unsigned product
`η_μ(x) η_ν(x+μ̂) η_μ(x+ν̂) η_ν(x)`. **The oriented form is written first
because it is the form that maps onto a group commutator in §4.**

**The Clifford group commutator:** `C_μν = γ_μ γ_ν γ_μ⁻¹ γ_ν⁻¹`.

**A computational convention that matters, stated once.** The plaquette is a
**local** object and is computed here **without modular identification**:
`x+μ̂` means the integer-shifted site, not a site reduced modulo a lattice
extent. `η_μ` is periodic only under shifts of even period, so on an odd-extent
torus the identification `x + L ≡ x` flips signs that are not part of the local
structure. **§7.1 records that this was met as an error before it was avoided.**

---

## 2. The two structures, each established before the derivation

### 2.1 The staggered plaquette on all six planes — MEASURED

**Computed over `3⁴ = 81` base sites, all six planes, no modular wrap:**

    plane (1,2)   {−1}        plane (2,3)   {−1}
    plane (1,3)   {−1}        plane (2,4)   {−1}
    plane (1,4)   {−1}        plane (3,4)   {−1}

**Repeated at `4⁴ = 256` and `5⁴ = 625` base sites: the union of all values
over all six planes and all sites is `{−1}` in each case.**

**`P_μν(x) = −1` on every plane at every site.**

### 2.2 Invariance under site-sign redefinition — PROVED for arbitrary `ε(x)`

**This is a proof for all `ε`, not a sample.**

Let `ε: ℤ⁴ → {±1}` be arbitrary and let

    η'_μ(x) = ε(x) η_μ(x) ε(x+μ̂) .

Substituting into the plaquette and collecting the `ε` factors:

    P'_μν(x) = [ε(x) η_μ(x) ε(x+μ̂)]
             · [ε(x+μ̂) η_ν(x+μ̂) ε(x+μ̂+ν̂)]
             · [ε(x+ν̂) η_μ(x+ν̂) ε(x+ν̂+μ̂)]
             · [ε(x) η_ν(x) ε(x+ν̂)]

**The loop has four corners — `x`, `x+μ̂`, `x+ν̂`, `x+μ̂+ν̂` — and each is an
endpoint of exactly two of the four links.** So each `ε` value occurs exactly
twice:

    ε(x)² · ε(x+μ̂)² · ε(x+ν̂)² · ε(x+μ̂+ν̂)² · P_μν(x)

**Since `ε(x) ∈ {±1}`, every square is `1`.** Therefore

    P'_μν(x) = P_μν(x)     for every ε, every x, and every plane.   ∎

**The argument uses only that the loop is closed and that `ε` takes values in a
group where every element is its own inverse.** It does not depend on the
particular `η`, on the lattice extent, or on any sampling.

### 2.3 A fixed-seed numerical sanity check — MEASURED, and it does not replace §2.2

    seed                            20260815
    ε drawn over the 5⁴ span        314 of 625 sites negative
    base sites checked              3⁴ = 81, all six planes
    plaquette unchanged everywhere  True
    transformed values              {−1}

**This is a reproducible check of a statement §2.2 already proved.** A single
draw, or any finite number of draws, cannot establish a statement quantified
over all `ε`.

### 2.4 The Clifford group commutator on all six planes — MEASURED

**Representation stated and verified before use.** With Pauli matrices
`σ_x, σ_y, σ_z`:

    γ_1 = σ_x ⊗ σ_x    γ_2 = σ_x ⊗ σ_y    γ_3 = σ_x ⊗ σ_z    γ_4 = σ_y ⊗ 1₂

**VERIFIED: `{γ_μ, γ_ν} = 2δ_μν · 1₄` for all sixteen pairs, and all four are
hermitian.**

    plane (1,2)   C_μν = −1 · 1₄      plane (2,3)   C_μν = −1 · 1₄
    plane (1,3)   C_μν = −1 · 1₄      plane (2,4)   C_μν = −1 · 1₄
    plane (1,4)   C_μν = −1 · 1₄      plane (3,4)   C_μν = −1 · 1₄

**In every case the commutator is a SCALAR multiple of the identity**, verified
as such and not merely read off one entry. **That scalarity is load-bearing in
§4 and is not incidental.**

### 2.5 The agreement between §2.1 and §2.4 is NOT the verdict

**Both equal `−1` on the same six planes. That is the reason to ask the
question, and it is not the answer to it.**

**Coincidence of value is not identity of structure.** Two objects can take the
same value in every case and be different structures; the matching numbers
license an investigation and nothing more. **A verdict resting on the
agreement would be wrong in either direction** — `REPRESENTATION-EQUIVALENT`
asserted from matching values would be unsupported, and `STAGGERED-SPECIFIC`
asserted despite them would be equally unsupported.

**What follows in §4 is a structural mapping, and it is what the verdict
rests on.**

---

## 3. The starting identity

**Recorded at the dossier's §3.3 and taken from there, not re-derived:**

    Γ(x)† γ_μ Γ(x+μ̂) = η_μ(x) · 1₄        (★)

with `Γ(x) = γ_1^{x_1} γ_2^{x_2} γ_3^{x_3} γ_4^{x_4}`.

**`Γ(x)` is unitary. DERIVED:** each `γ_μ` is hermitian with `γ_μ² = 1`, hence
unitary; a product of unitaries is unitary; so `Γ(x)† = Γ(x)⁻¹`.
**VERIFIED: `max |Γ(x)†Γ(x) − 1₄| = 0` over all 81 sites.**

**This is the step where the gamma structure becomes a phase**, and it is the
only input the derivation needs beyond the definitions.

---

## 4. The derivation, step by step

**Step 1 — invert (★) for the two reversed links.** Using `Γ† = Γ⁻¹` and
`γ_μ⁻¹ = γ_μ`:

    η_μ(x)⁻¹ · 1₄ = [Γ(x)† γ_μ Γ(x+μ̂)]⁻¹ = Γ(x+μ̂)† γ_μ⁻¹ Γ(x)

**Step 2 — write each of the four plaquette factors via (★).**

    η_μ(x)      · 1₄ = Γ(x)†       γ_μ    Γ(x+μ̂)
    η_ν(x+μ̂)   · 1₄ = Γ(x+μ̂)†    γ_ν    Γ(x+μ̂+ν̂)
    η_μ(x+ν̂)⁻¹ · 1₄ = Γ(x+ν̂+μ̂)†  γ_μ⁻¹  Γ(x+ν̂)
    η_ν(x)⁻¹    · 1₄ = Γ(x+ν̂)†    γ_ν⁻¹  Γ(x)

**Step 3 — multiply them in loop order.** The `η` are scalars, so their product
is `P_μν(x)`:

    P_μν(x) · 1₄ = Γ(x)† γ_μ Γ(x+μ̂) · Γ(x+μ̂)† γ_ν Γ(x+μ̂+ν̂)
                   · Γ(x+ν̂+μ̂)† γ_μ⁻¹ Γ(x+ν̂) · Γ(x+ν̂)† γ_ν⁻¹ Γ(x)

**Step 4 — the interior telescopes.** Three cancellations, each `Γ Γ† = 1₄`:

    Γ(x+μ̂) Γ(x+μ̂)†       = 1₄
    Γ(x+μ̂+ν̂) Γ(x+ν̂+μ̂)†  = 1₄     the same site, since x+μ̂+ν̂ = x+ν̂+μ̂
    Γ(x+ν̂) Γ(x+ν̂)†       = 1₄

**The second cancellation is the one that requires the loop to close.** It is
available only because the two paths around the plaquette reach the same
corner, and it is where "closed loop" enters the algebra rather than the
prose.

Leaving:

    P_μν(x) · 1₄ = Γ(x)† [ γ_μ γ_ν γ_μ⁻¹ γ_ν⁻¹ ] Γ(x) = Γ(x)† C_μν Γ(x)

**Step 5 — the identity, VERIFIED.** Over `81 sites × 6 planes = 486` cases,
`P_μν(x)·1₄ = Γ(x)† C_μν Γ(x)` holds with **maximum deviation `0.00e+00`.**

**Step 6 — the conjugation drops out.** By §2.4, `C_μν = −1 · 1₄` is a scalar,
and a scalar commutes with everything:

    Γ(x)† (−1 · 1₄) Γ(x) = −1 · Γ(x)†Γ(x) = −1 · 1₄

Therefore

    P_μν(x) = −1     for every x and every plane.        ∎

**The derivation closes.**

### 4.1 What the derivation establishes, and what it explains

**`P_μν` IS the Clifford group commutator, written in the variables spin
diagonalisation produces.** The equality of §4 is an identity between the two
objects, not an agreement between two numbers.

**Three facts previously observed separately are consequences of the one
identity:**

- **why the value is `−1`** — it is `C_μν`'s value, and nothing else enters;
- **why it is site-independent** — `C_μν` is a scalar, so the `Γ(x)`
  conjugation, which is the only `x`-dependence, cancels;
- **why it is redefinition-invariant** — §2.2 proves this independently, and
  §4 explains it: the redefinition acts on `Γ`, and a scalar is invariant under
  conjugation.

**The site-independence and the redefinition-invariance have the same cause**,
which no argument from matching values could have shown.

---

## 5. The four candidates

**Analysing staggered alone would be looking for staggered's problem.** Each
row is derived.

### 5.1 naive

**Structure carried:** the Clifford group commutator `C_μν = γ_μγ_νγ_μ⁻¹γ_ν⁻¹`,
equal to `−1 · 1₄` on all six planes.

**How represented:** explicitly, in the gamma matrices of the operator
`i Σ_μ γ_μ sin p_μ`. **DERIVED:** the operator's Dirac structure is the gamma
algebra itself, so the commutator is present in the operator as written.

**Redefinition-invariance:** under a local invertible `ψ(x) → V(x)ψ(x)`, the
commutator is conjugated by `V`; being a scalar multiple of the identity, it is
unchanged. **The same invariance, by the same mechanism as §4 Step 6.**

### 5.2 Wilson

**Structure carried:** `C_μν = −1 · 1₄`, identical to naive.

**How represented:** in the same gamma matrices. **DERIVED and VERIFIED:** the
Wilson term `m + r W(p)` is a multiple of `1₄` in Dirac space, so it commutes
through and contributes nothing to `[γ_μ, γ_ν]`. **VERIFIED: adding any scalar
multiple of `1₄` to a gamma leaves `[γ_μ, γ_ν]` unchanged.**

**Redefinition-invariance:** as §5.1.

### 5.3 staggered

**Structure carried:** `P_μν = −1` on all six planes at every site, §2.1.

**How represented:** in **link phases** rather than gamma matrices — the
formulation carries no explicit Dirac index, the spin diagonalisation (★)
having moved the structure into the site and link signs.

**Redefinition-invariance:** PROVED for arbitrary `ε` in §2.2, by cancellation
around the closed loop.

**Relation to the other three:** §4 derives that this IS `C_μν`, conjugated by
`Γ(x)` and therefore equal to it. **Same structure, different variables.**

### 5.4 overlap

**Structure carried:** `C_μν = −1 · 1₄`, identical to naive.

**How represented:** in the same gamma matrices. **DERIVED and VERIFIED:**
`D_ov = 1 + [i Σ γ_μ sin p_μ + (W − M_0)]/√(s + (W−M_0)²)` carries its gammas
in the same `i Σ γ_μ sin p_μ` term; the remaining factors — `W − M_0` and the
inverse square root — are scalars in Dirac space and commute through.
**Non-ultralocality does not bear on this**: the scalar prefactor is a function
of momentum, not of the Dirac index.

**Redefinition-invariance:** as §5.1.

### 5.5 The four rows

    candidate    invariant structure          how represented
    naive        C_μν = −1 on all six planes  gamma matrices, explicitly
    Wilson       C_μν = −1 on all six planes  gamma matrices; r-term is scalar
    staggered    P_μν = −1 on all six planes  link phases; = C_μν by §4
    overlap      C_μν = −1 on all six planes  gamma matrices; scalar prefactors

**All four carry the same invariant.** They differ in **representation** and
not in the structure represented.

---

## 6. The companion question — the translation sector

**§2a asks whether the translation side carries a redefinition-invariant
structure, and whether it is the same one.**

**The 96 mismatches, RE-MEASURED here rather than quoted** from lines 224–235
of the discriminants artifact:

    translation along axis 1    48 mismatches
    translation along axis 2    32 mismatches
    translation along axis 3    16 mismatches
    translation along axis 4     0 mismatches
    TOTAL                       96

**The split is reported because the total alone conceals it.** Axis 4 has zero
because `η_μ` depends only on coordinates with index `< μ`, so a shift along
the last axis changes no phase.

**The naive candidate for a translation invariant fails. DERIVED and
MEASURED:** `T_μν(x) ≡ η_μ(x+ν̂) η_μ(x)` is the constant sign `(−1)^{[ν<μ]}`.
Under `η → εηε` its four `ε` factors sit on **four distinct sites**, each
appearing once, so they do not cancel: **`T` is not redefinition-invariant.**

**The translation defect is PURE GAUGE. VERIFIED** by exhaustive search over
all `2¹⁶` sign assignments on the `2⁴` block: **for each of the four axes a
redefinition `ε` exists that restores the original phases — 4 of 4.**

**Consequence, DERIVED:** if the translated configuration is gauge-equivalent
to the original, every redefinition-invariant quantity agrees between them.
**VERIFIED directly: the translated configuration's plaquettes are `{−1}` on
all six planes for each of the four axes.**

**ANSWER: the translation sector carries no redefinition-invariant structure of
its own.** Its non-invariance is entirely removable by a redefinition, and the
one invariant present is `P_μν` — **the same structure**, which §4 identifies
as `C_μν`.

**So the two questions have one answer**, which is stronger than either alone:
the axis-permutation sector and the translation sector are not two structures
but one, and that one is the Clifford anticommutation structure.

---

## 7. What this artifact does not establish

### 7.1 A method error met before it was avoided

**The plaquette was first computed with periodic identification at odd extent
`L = 3`, and returned mixed `{+1, −1}` values.** That is a **wrap artefact**:
`η_μ` is periodic only under shifts of even period, so identifying `x + 3 ≡ x`
introduces signs that are not part of the local structure. **Recomputed without
modular identification the product is uniformly `−1`**, at `3⁴`, `4⁴` and `5⁴`.

**Recorded because a reader reproducing §2.1 on a periodic odd lattice will
disagree with it**, and the disagreement would be the reader's convention, not
a defect in the result.

### 7.2 The limits of the verdict

- **A structural finding is not an admissibility finding.** Nothing here bears
  on whether any candidate may be canonical.
- **This artifact derives from an identity the dossier records. It does not
  re-derive the dossier's species ledgers and does not check them.** A result
  consistent with the dossier is **not corroboration of the dossier**, because
  both rest on the same reconstruction (★).
- **The comparison is at ONE level** — the plaquette, and the translation
  sector of §6. **Nothing here establishes that no other
  redefinition-invariant structure distinguishes the candidates.** **A negative
  result at this level is not a negative result at every level.**
- **Reflection positivity remains outstanding** among the
  formulation-discriminating requirements already identified, and waits on a
  transfer matrix that does not exist. **It is not scoped here, and this
  artifact does not establish that it is the only possible remaining
  discriminator.**

## 8. No elimination, no preference

**No candidate is eliminated, preferred, ranked or recommended.**

**The verdict is `REPRESENTATION-EQUIVALENT`, which is a statement that the
four candidates carry the same structure at the level tested.** It is not a
statement that any of them is admissible, inadmissible, better or worse suited.

**Had the verdict been `STAGGERED-SPECIFIC`, the same boundary would apply**: a
difference in structure is not a difference in admissibility, and whether a
uniform `π` flux on a physically real substrate would be a defect or a feature
is a PI ruling this artifact does not prepare and does not anticipate.

**All four candidates receive a derived row in §5.** None is treated as the
subject of the investigation with the others as controls.
