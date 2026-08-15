# `P2-LATTICE-MICROSPEC-01` — canonical kinetic operator: candidate dossier and selection grounds

**This artifact freezes nothing and selects nothing.** It assembles, for each
of the four candidate kinetic operators, what that candidate commits the theory
to. **Weighing the grounds is the PI's.** No candidate is selected, ranked,
recommended or preferred here, and the absence of a recommendation is
deliberate rather than an omission.

**Evidence base:** `ae3604def317667b44ea59458569ba105463fd6b`.

**Every figure is marked DERIVED HERE or NOT ESTABLISHED.** "Standard result"
is not used as a derivation anywhere in this file. The repository contains no
literature, so anything not derived from the committed material or from
explicit algebra performed here is marked NOT ESTABLISHED.

## 0. The ruling this dossier serves

> **`D-pre` does not impose an a priori target species count. The species
> content of the microscopic theory is the species ledger implied by the
> selected canonical H(4) kinetic operator, including any lattice
> multiplicities or lifted modes intrinsic to that operator. Whether some
> microscopic species decouple, become gapped, pair, confine, or otherwise
> disappear from the infrared observable spectrum is a downstream dynamical
> question and is not used to define the canonical microscopic theory. The
> canonical kinetic operator must instead be selected on independent physical
> and structural grounds; agreement with a desired species count is not an
> admissible selection criterion.**

**The ruling removes a selection criterion without supplying one.** This
dossier assembles grounds; it does not apply them.

## 1. Conventions, fixed once and used throughout

Euclidean hypercubic lattice, spacing `a = 1`, four axes, momenta
`p_μ ∈ (−π, π]`. Euclidean gamma matrices are hermitian with
`{γ_μ, γ_ν} = 2 δ_μν`, `γ_5 = γ_1γ_2γ_3γ_4`, `γ_5† = γ_5`, `γ_5² = 1`,
`{γ_5, γ_μ} = 0`. **VERIFIED HERE** against an explicit `4×4` representation.

Two abbreviations recur:

    s(p) = Σ_μ sin²p_μ            W(p) = Σ_μ (1 − cos p_μ)

**A corner** is a momentum `π_A` with every component in `{0, π}`. Write
`n = |S|` for the number of components equal to `π`, `S ⊆ {1,2,3,4}`. There are
`C(4,n)` corners with that `n`, and `Σ_n C(4,n) = 16`.

**At a corner, `s = 0` and `W = 2n`.** DERIVED HERE: `sin 0 = sin π = 0`, and
`1 − cos 0 = 0` while `1 − cos π = 2`.

**A lattice branch is LIFTED if it remains a pole of the propagator at a mass
set by the cutoff, and ABSENT if the formulation carries no field degree of
freedom for it at all.** The distinction is used throughout and is not
cosmetic: a lifted branch is a species of the declared theory under §0's
ruling, and an absent one is not a species of anything.

## 2. The corner expansion, derived once and reused

Let `p = π_A + k`. Then

    sin(π_{A,μ} + k_μ) = cos(π_{A,μ}) sin k_μ = σ_μ sin k_μ ,   σ_μ = ±1

with `σ_μ = −1` exactly when `μ ∈ S`. So any operator built from
`i Σ_μ γ_μ sin p_μ` becomes, near corner `A`,

    i Σ_μ (σ_μ γ_μ) k_μ + O(k³)  ≡  i Σ_μ γ̃_μ k_μ + O(k³) .

**DERIVED HERE:** `{γ̃_μ, γ̃_ν} = σ_μ σ_ν · 2δ_μν = 2δ_μν`, so `γ̃` is again a
Clifford representation and the branch at each corner is a full four-component
Dirac fermion with the standard dispersion. **VERIFIED HERE for all sixteen
corners.**

**DERIVED HERE:** `γ̃_5 ≡ γ̃_1γ̃_2γ̃_3γ̃_4 = (Π_μ σ_μ) γ_5 = (−1)^{|S|} γ_5`.
**VERIFIED HERE for all sixteen corners.** So corners with `|S|` odd carry the
opposite chirality assignment to the origin; eight corners have `|S|` even and
eight have `|S|` odd.

**This section is formulation-independent** and is the shared machinery. **It
is not the shared answer** — §3 shows that the four candidates convert it into
four different ledgers by four different routes.

---

## 3. §A — the species ledger, per candidate, by that formulation's own method

**The methods are not interchangeable.** Measuring every candidate by one
candidate's ruler would prejudge the choice while appearing not to. Each
subsection states its method and why that method suits that formulation.

### 3.1 Naive — method: corner expansion about the degenerate zeros

**Why this method.** The naive operator's zeros are isolated points of the full
Brillouin zone and the field carries the full four-component Dirac index at
every site, so an expansion about each zero returns a Dirac branch directly and
nothing is reconstructed.

    D_naive(p) = i Σ_μ γ_μ sin p_μ + m

**Zeros at `m = 0`. DERIVED HERE:** `D = 0` requires `sin p_μ = 0` for every
`μ`, hence `p_μ ∈ {0, π}` — the sixteen corners, and no others in `(−π, π]⁴`.

**Species. DERIVED HERE:** by §2, each of the sixteen corners carries a
four-component Dirac branch with dispersion `i γ̃·k + m`. **The mass at every
corner is `m`**, because the naive operator contains no term distinguishing
corners. **Sixteen degenerate Dirac species.**

**Momentum regions.** The sixteen corner neighbourhoods of the unreduced zone.

**Lifted versus absent. DERIVED HERE: none is lifted and none is absent.** All
sixteen sit at the same mass, so at `m = 0` all sixteen are massless
simultaneously.

**Chirality structure. DERIVED HERE** via §2: eight branches carry `+γ_5` and
eight carry `−γ_5` relative to the origin.

**Raw zero counting: USED, and licensed.** The equivalence of the zero count to
the physical species count is derived rather than assumed — §2 establishes that
each zero yields one full Dirac branch, and no field components were removed or
recombined, so sixteen zeros mean sixteen Dirac species. **This licence is
specific to the naive case and is not exported to any other candidate.**

**NOT ESTABLISHED for this candidate:** whether the sixteen species are
physically distinguishable by any observable defined in this programme; the
interacting-theory fate of the degeneracy.

### 3.2 Wilson — method: corner branches together with the Wilson mass shifts

**Why this method.** The Wilson operator has the same zero structure as the
naive one before the `r`-term is added, so the corner expansion of §2 applies
unchanged; what the method must add is the corner-dependent mass the Wilson
term supplies, which is what distinguishes the branches.

    D_W(p) = i Σ_μ γ_μ sin p_μ + m + r W(p) ,     r = 1 as used in this repository

**Corner masses. DERIVED HERE:** at corner `A`, `s = 0` and `W = 2n`, so the
branch mass is

    m_n = m + 2 r n = m + 2n           n = 0,1,2,3,4

**The ledger. DERIVED HERE:**

    n = 0    1 corner     mass m        the ordinary branch
    n = 1    4 corners    mass m + 2
    n = 2    6 corners    mass m + 4
    n = 3    4 corners    mass m + 6
    n = 4    1 corner     mass m + 8
    ------------------------------------
             16 corners

**Species: sixteen Dirac branches, of which one sits at `m` and fifteen are
lifted to masses `m + 2n` set by the lattice cutoff.**

**Lifted versus absent. DERIVED HERE: fifteen are LIFTED, none is absent.**
Every corner remains a pole of the propagator; the Wilson term shifts masses
and removes no degree of freedom, the field still carrying four Dirac
components at every site.

**This is the sense in which a Wilson doubler is a species under §0's ruling**:
it is present in the declared operator's spectrum at a cutoff-scale mass. **It
is not thereby an independent light infrared particle**, and nothing here
asserts that it is — its mass is `m + 2n`, which is of cutoff order for every
`n ≥ 1` at small `m`.

**Raw zero counting: USED for the corner locations, and licensed only for
those.** The zero structure locates the sixteen corners; the *species content*
is then read from the mass at each, not from the count. **Counting poles alone
would report sixteen degenerate species and would be wrong about fifteen of
them.**

**NOT ESTABLISHED for this candidate:** the value of `r` as a canonical choice
— `r = 1` is what the exploratory script uses, not something the repository
freezes; the interacting fate of the lifted branches.

### 3.3 Staggered — method: spin/taste reconstruction, NOT one-component zero counting

**Why this method, stated before any number.** The staggered field carries one
component per site, not four. **The zeros of the one-component momentum
operator are therefore not in one-to-one correspondence with Dirac branches**,
and counting them would be the derivation error this dossier is required to
avoid. The reconstruction must be performed before any species count is
reported.

**The spin diagonalisation. DERIVED HERE, and VERIFIED HERE** over all
`x ∈ {0,1}⁴` and all `μ`. With `Γ(x) = γ_1^{x_1} γ_2^{x_2} γ_3^{x_3} γ_4^{x_4}`
and `η_μ(x) = (−1)^{x_1 + … + x_{μ−1}}`,

    Γ(x)† γ_μ Γ(x + μ̂)  =  η_μ(x) · 1_4

**The Dirac structure becomes proportional to the identity.** Substituting
`ψ(x) = Γ(x) χ(x)` therefore turns the naive operator into four identical,
decoupled copies of a one-component operator carrying the phases `η_μ(x)`.

**The count. DERIVED HERE:** the naive operator carries sixteen Dirac species
on a four-component field. The identity above exhibits it as **four decoupled
copies** of the staggered one-component operator. Keeping one copy therefore
keeps one quarter of the naive content:

    16 naive Dirac species  /  4 identical copies  =  4 tastes

**Species: four tastes, each a four-component Dirac fermion.**

**Momentum regions. DERIVED HERE from the construction:** the reconstruction is
carried on `2⁴` blocks, the sixteen components of `χ` on a block furnishing
`4 Dirac ⊗ 4 taste = 16`, over a **reduced** Brillouin zone `(−π/2, π/2]⁴`.
The relevant zone is the reduced one, not the unreduced zone the naive and
Wilson ledgers use.

**Lifted versus absent. DERIVED HERE:** the four tastes are exactly degenerate
in the free massless theory and **none is lifted**. Relative to the naive
sixteen, the missing twelve are **ABSENT rather than lifted** — they are
removed by discarding three of the four decoupled copies, which is a reduction
of field content and not a mass term.

**Raw zero counting: NOT USED, and the reason is recorded.** The one-component
momentum operator has sixteen zeros. **The taste count is four.** The factor
between them is the four discarded Dirac copies, and reporting sixteen here
would be a derivation error rather than a different convention.

**NOT ESTABLISHED for this candidate:** whether the reduced-zone reconstruction
is compatible with the H(4) isotropy freeze as that freeze is worded — see
§5.3, which records the question rather than answering it; the interacting-
theory taste-symmetry structure.

### 3.4 Overlap — method: the free spectrum of the overlap operator itself

**Why this method.** The overlap operator is not a corner-local modification of
the naive one; it is a function of a kernel, so its branches must be read from
its own spectrum rather than from an expansion of a kernel it is built out of.

**Convention, stated as required.** Overlap operator
`D_ov = 1 + γ_5 sign(H_W)` with hermitian kernel
`H_W = γ_5 (D_W − M_0)`, `D_W` the Wilson operator at `r = 1` and `m = 0`, and
`M_0` the kernel mass, equivalently the domain-wall height. **`M_0` is a
convention this dossier states and does not choose.**

**The kernel squares to a scalar. DERIVED HERE, VERIFIED HERE:**

    H_W² = [ s(p) + (W(p) − M_0)² ] · 1_4

**The operator in closed form. DERIVED HERE:** since
`γ_5 H_W = γ_5 γ_5 (D_W − M_0) = i γ·sin p + (W − M_0)`,

    D_ov(p) = 1 + [ i Σ_μ γ_μ sin p_μ + (W(p) − M_0) ] / √( s(p) + (W(p) − M_0)² )

**At a corner. DERIVED HERE:** `s = 0`, `W = 2n`, so

    D_ov(π_A) = 1 + sign(2n − M_0)

    2n < M_0   ⟹  D_ov = 0    a massless branch
    2n > M_0   ⟹  D_ov = 2    a branch at the far side of the spectral circle

**The ledger. DERIVED HERE, VERIFIED HERE at `M_0 = 1,3,5,7,9`:**

    number of massless Dirac species  =  Σ_{n : 2n < M_0} C(4,n)

    0 < M_0 < 2      1        4 < M_0 < 6     11
    2 < M_0 < 4      5        6 < M_0 < 8     15
                              M_0 > 8         16

**The species count is a function of the stated convention and is not a
property of "the overlap" without it.** Reporting a single number here without
`M_0` would be an unanchored figure.

**Lifted versus absent. DERIVED HERE: the non-massless corners are LIFTED, not
absent.** Each remains a branch of the operator, at `D_ov = 2`, i.e. at the
cutoff scale on the spectral circle of radius `1` centred at `1`; no field
component is removed.

**Raw zero counting: USED on `D_ov` itself, and licensed for that operator.**
The zeros counted are zeros of the physical fermion operator whose propagator
is the physical propagator for this formulation, not zeros of a kernel — the
licence comes from the closed form derived above and does not transfer to the
kernel's own zeros, which are Wilson's and are different.

**NOT ESTABLISHED for this candidate:** which `M_0` the programme would adopt,
that being part of the choice this dossier does not make; whether the
non-ultralocality derived in §4.4 obstructs any of the frozen obligations.

### 3.5 The four ledgers side by side, with no ordering implied

    naive       16 Dirac species, all at mass m, none lifted, none absent
                method: corner expansion; raw zero count used and licensed

    Wilson      16 Dirac branches, one at m and 15 lifted to m + 2n
                method: corner expansion plus the Wilson mass shifts

    staggered    4 tastes, none lifted; 12 of the naive 16 absent
                method: spin/taste reconstruction on the reduced zone;
                        one-component zero counting NOT used

    overlap     Σ_{2n<M_0} C(4,n) massless, remainder lifted at the cutoff
                method: the overlap operator's own free spectrum, M_0 stated

**These are four ledgers, not four scores.** They are not commensurable without
a criterion, and supplying a criterion is the ruling this dossier precedes.

---

## 4. §B — reflection positivity, per candidate

`P2-LATTICE-ONTOLOGY-01` line 181 freezes reflection positivity of the action
**as an obligation**, and lines 81–84 record that the obligation "has teeth —
it constrains the kinetic-operator choice directly".

**No reflection-positivity construction for any candidate exists in this
repository.** The assessments below are therefore about what the available
material establishes, and all four are recorded at the same standard.

### 4.1 Naive — NOT ESTABLISHED

Nothing in the repository addresses reflection positivity of the naive action,
and no construction is derived here. **Neither satisfaction nor violation is
established.**

### 4.2 Wilson — NOT ESTABLISHED, with a repository assertion recorded

`P2-LATTICE-ONTOLOGY-01` lines 82–84 state that "standard Wilson formulations
admit reflection-positive constructions under the relevant conditions; not
every discretization does."

**That is an assertion in a committed artifact, and it is not a derivation.**
The relevant conditions are not stated there, no construction is given, and
this dossier does not supply one. **Recorded as an assertion on record;
NOT ESTABLISHED as a derived result.**

### 4.3 Staggered — NOT ESTABLISHED

Nothing in the repository addresses reflection positivity of the staggered
action, and no construction is derived here.

### 4.4 Overlap — NOT ESTABLISHED, with a derived structural obstruction to one
### family of methods

**DERIVED HERE: the free overlap operator is not ultralocal.** A finite-range
lattice kernel has a momentum-space form that is a trigonometric polynomial in
`p`. From §3.4 the overlap operator contains
`[s(p) + (W(p) − M_0)²]^{−1/2}`, and the inverse square root of a non-constant
positive trigonometric polynomial is not itself a trigonometric polynomial.
**So the position-space kernel is not of finite range, and the action couples
every pair of time-slices.**

**What this does and does not mean.** Reflection-positivity constructions that
proceed by splitting the action into a piece on each half-lattice plus a
nearest-neighbour-in-time cross-term **do not apply as stated** to an action
with couplings across arbitrarily separated slices. **This is an obstruction to
a family of methods, not a demonstration that reflection positivity fails**,
and it is recorded as the former. Whether another construction succeeds is
**NOT ESTABLISHED**.

### 4.5 Count

    satisfied          0
    violated           0
    NOT ESTABLISHED    4

**All four at the same standard.** `NOT ESTABLISHED` for every candidate is the
honest reading of a repository containing no reflection-positivity
construction, and the criterion authorising this dossier anticipated the answer
for at least one.

---

## 5. §C — compatibility with what `P2-LATTICE-ONTOLOGY-01` freezes

The four items checked are those the specification names: line 180
Euclidean-fundamental formulation with derived Hamiltonian; line 181 reflection
positivity as obligation; line 182 isotropy of the four axes; line 184 the
vacuum selection rule.

**Recorded as a finding: the delegation table freezes FIVE items, not four.**
Line 183, "Lattice: ontologically dynamical, operationally static", also reads
`FROZEN HERE (§1c)`. It is outside the sixteen checks below because the four
checked are the four named. **Its own text (lines 130–143) describes it as an
ontology obligation rather than a completed declaration, and it constrains the
substrate variables rather than the kinetic operator**, so no candidate is
distinguished by it on any reading available here. **Recorded, not resolved.**

### 5.1 Line 180 — Euclidean-fundamental formulation, Hamiltonian derived

    naive       COMPATIBLE      DERIVED HERE: a local Euclidean lattice action
                                in the Euclidean variables; the formulation
                                requirement is met by construction.
    Wilson      COMPATIBLE      DERIVED HERE: as above.
    staggered   COMPATIBLE      DERIVED HERE: as above.
    overlap     NOT ESTABLISHED §4.4 derives that the action is not
                                ultralocal. Line 180 requires the Hamiltonian
                                to be DERIVED by slicing, which presupposes a
                                transfer operator; whether one is constructible
                                from a slice-nonlocal action is not addressed
                                by the repository and is not derived here.

**No candidate is shown inconsistent with line 180.**

### 5.2 Line 181 — reflection positivity as obligation

    naive       NOT ESTABLISHED   §4.1
    Wilson      NOT ESTABLISHED   §4.2, with the repository assertion recorded
    staggered   NOT ESTABLISHED   §4.3
    overlap     NOT ESTABLISHED   §4.4, with the derived method obstruction

**No candidate is shown inconsistent with line 181**, and none is shown to
satisfy it.

### 5.3 Line 182 — isotropy of the four axes

Line 94 states the frozen content precisely: **"H(4) isotropy (equal couplings
on all four axes)"**.

    naive       COMPATIBLE        DERIVED HERE: the coefficient of the hopping
                                  is the same on every axis; the operator is
                                  invariant under permutation of the four axes
                                  by inspection of its momentum form.
    Wilson      COMPATIBLE        DERIVED HERE: both the i γ·sin term and r W
                                  are symmetric sums over μ with a single r.
    staggered   NOT ESTABLISHED   DERIVED HERE: the phases
                                  η_μ(x) = (−1)^{x_1+…+x_{μ−1}} are NOT
                                  symmetric under permutation of the axes —
                                  η_1 ≡ 1 while η_4 depends on three
                                  coordinates. The couplings' MAGNITUDES are
                                  equal on all four axes; their sign patterns
                                  single out an axis ordering.
                                  Whether line 182 requires manifest axis
                                  symmetry of the action, or equality of
                                  couplings up to a field redefinition, is not
                                  settled by the text. RECORDED, NOT RESOLVED.
    overlap     COMPATIBLE        DERIVED HERE: D_ov of §3.4 is built from
                                  s(p) and W(p), both symmetric sums over μ,
                                  so the operator is axis-permutation
                                  symmetric.

**No candidate is declared inconsistent with line 182.** The staggered entry is
an open reading of the frozen text, not a finding against the candidate, and
resolving it is not this dossier's.

### 5.4 Line 184 — the vacuum selection rule

Lines 146–154 make the rule operational: the reference-vacuum sector is the
maximal-eigenvalue eigenspace of the **reconstructed transfer matrix** within
the declared neutral sector, the neutral sector being defined by the conserved
microscopic charge with `Q → −Q` under charge conjugation.

    naive       NOT ESTABLISHED   The rule presupposes a reconstructed transfer
                                  matrix, which is line 181's unmet obligation.
                                  A conserved U(1) charge exists for the free
                                  operator; the rule's remaining content cannot
                                  be checked without the transfer operator.
    Wilson      NOT ESTABLISHED   As above, for the same reason.
    staggered   NOT ESTABLISHED   As above, and additionally the identification
                                  of the microscopic charge with the
                                  reconstructed taste basis is not derived
                                  here.
    overlap     NOT ESTABLISHED   As above, and §4.4's obstruction bears on the
                                  reconstruction the rule presupposes.

**No candidate is shown inconsistent with line 184.**

### 5.5 The sixteen results

                     line 180        line 181        line 182        line 184
    naive        COMPATIBLE      NOT ESTAB.      COMPATIBLE      NOT ESTAB.
    Wilson       COMPATIBLE      NOT ESTAB.      COMPATIBLE      NOT ESTAB.
    staggered    COMPATIBLE      NOT ESTAB.      NOT ESTAB.      NOT ESTAB.
    overlap      NOT ESTAB.      NOT ESTAB.      COMPATIBLE      NOT ESTAB.

    COMPATIBLE          6
    INCONSISTENT        0
    NOT ESTABLISHED    10

**MEASURED: no candidate is inconsistent with any of the four frozen items**,
so the criterion's request for the lines establishing an inconsistency has no
instance to report. **A count of `COMPATIBLE` results is not a score**, and
this dossier does not treat it as one: `NOT ESTABLISHED` records that the
repository is silent, which is a fact about the repository and not a property
of the candidate.

---

## 6. §D — what each candidate does to the existing computed evidence

**MEASURED at the evidence base:** `scripts/p2_phase01_scalar_exploratory.py`
lines 80–82 build the denominator `s + w·w` with
`s = Σ_μ sin²p_μ` and `w = Mhat + Σ_μ (1 − cos p_μ)`. **That is a Wilson-form
kernel at `r = 1`.** Nothing was recomputed and the script was not run.

**These are consequences, not arguments.** Continuity with existing computation
is a convenience; §0's ruling requires independent physical and structural
grounds, and what weight continuity carries is the PI's to decide.

### 6.1 Naive

**Stored results become evidence about a theory the programme did not adopt.**
DERIVED HERE: dropping the Wilson term gives `w = Mhat`, so the denominator
becomes `s + Mhat²` and every stored `I0` value is an integral of a different
integrand.

**The complement relation does NOT hold.** DERIVED HERE: with `w = Mhat`, the
denominator is even in `Mhat`, giving `I0(Mhat) = I0(−Mhat)` — **a reflection
about `0`, not about `−4`.** `I0(Mhat) = I0(−8−Mhat)` has no naive analogue,
because the `8` comes from `W`'s range and `W` is absent.

### 6.2 Wilson

**Stored results remain evidence about the canonical theory**, conditional on
`r = 1` and on the `Mhat` convention the script uses. DERIVED HERE: the script's
denominator is the Wilson denominator, so no re-derivation of the integrand
would be required.

**The complement relation holds and is exact** — §8 derives it.

**Not established even here:** the script computes the untraced scalar bubble
over the full zone, so its `I0` already sums all sixteen corners. **Whether
that sum is the right object once the corners are declared species rather than
artifacts is a question §7 shows the repository does not answer.**

### 6.3 Staggered

**Stored results become evidence about a theory the programme did not adopt.**
DERIVED HERE: the staggered field is one-component, so the bubble's Dirac
structure — and the frozen factor `trace(Id4) = 4` at
`P2-GENERATOR-SUM-CRITICALITY_01` line 31 — does not carry over unchanged; the
integrand and the trace factor would both require re-derivation in the
reconstructed taste basis, over the reduced zone of §3.3.

**The complement relation: NOT ESTABLISHED.** The staggered operator carries no
`W` term, so the specific identity has no direct analogue; whether the
reconstructed taste-basis propagator carries some other involution symmetry is
not derived here.

### 6.4 Overlap

**Stored results become evidence about a theory the programme did not adopt.**
DERIVED HERE: from §3.4 the overlap propagator is built from
`D_ov = 1 + [iγ·sin p + (W − M_0)]/√(s + (W − M_0)²)`, which is not the
script's `s + w²` for any `Mhat`.

**A structural analogue of the complement relation is DERIVED HERE, and it is
an analogue and not the relation.** Under `p_μ → π − p_μ`, §8 gives `s → s` and
`W → 8 − W`, so `W − M_0 → −(W − (8 − M_0))`. **The involution therefore relates
the kernel mass `M_0` to `8 − M_0`**, in the same way it relates `Mhat` to
`−8 − Mhat` in the Wilson case. Consistently with §3.4's ledger, `M_0` and
`8 − M_0` lie symmetrically about `4` and their species counts are the two ends
of the same table.

**No numerical consequence is drawn**, and none is computed.

---

## 7. §E — how a species ledger would enter `N`-accounting

### 7.1 What `N` is, and the gap condition, MEASURED with line numbers

**MEASURED, `derivations/P2-GENERATOR-SUM-CRITICALITY_01.md`:**

- **line 23** — the canonical interaction
  `X = (G/(2N)) * Sum( bilinear(lam(A),Id4)**2 + bilinear(lam(A),I*gamma5)**2, (A,0,N**2-1) )`.
- **line 25** — the bilinears `S^A = ψ̄ (λ^A ⊗ 1_4) ψ`, `P^A = ψ̄ (λ^A ⊗ iγ_5) ψ`.
- **line 28** — `Tr(λ^A λ^B) = 2 δ^{AB}`, `A = 0 … N²−1`, singlet
  `λ^0 = √(2/N)·1_N`.
- **line 29–30** — `{λ^A}` is a complete Hermitian basis of the **`N×N` complex
  matrices** (`N²` of them).
- **line 31** — the Dirac trace, frozen separately: `trace(Id4) = 4`.
- **lines 41–44** — the condensate ansatz: flavour-diagonal
  `⟨ψ̄_i ψ_j⟩ = δ_ij Φ`, "a common per-flavour Dirac-traced amplitude `Φ` and a
  common dynamical mass `m` on every flavour".
- **line 145** — the gap condition and the critical coupling:

      1 = (8/N) G I_0   ⟹   G_c^{(b)} = N/(8 I_0)

- **lines 147–150** — the factor `8/N` is `2` (Hartree) `× 4` (Dirac trace)
  `× (1/N)`.

**So `N` is the `U(N)` flavour rank**, carried by an index the `λ^A` act on. It
is not a Dirac index — line 25 shows the Dirac structure entering as a separate
tensor factor `1_4`, and line 31 accounts for it separately. **`N` is not a
lattice species multiplicity, and no line in the repository states that one
multiplies into the other.**

`P2-LATTICE-ONTOLOGY-01` line 356 states that "the species multiplicity enters
`N`-accounting explicitly". **MEASURED: it states that it does. It does not
state how.**

### 7.2 Three places a multiplicity could enter, and why naming them is not
### choosing among them

**DERIVED HERE from the structure above**, a lattice species multiplicity could
in principle enter at any of:

1. **the flavour rank `N`** — if the species are additional flavours the `λ^A`
   act on, which requires the species to be degenerate and interchangeable;
2. **the Dirac-trace factor `4`** at line 31 — if the species are additional
   components of the spinor structure rather than additional flavours;
3. **the bubble `I_0` itself** — line 38 defines `B(Σ)` as an integral over the
   momentum measure, and a lattice integral over the full Brillouin zone
   already receives a contribution from every corner, so a multiplicity may
   already be inside `I_0` rather than multiplying it.

**Enumerating the three is not a derivation of which one applies**, and this
dossier does not pick one. **Route 3 matters especially**: if a multiplicity is
already inside `I_0`, then also multiplying `N` would double-count it.

### 7.3 A derived obstruction that applies before any of the three

**DERIVED HERE:** lines 41–44 freeze the condensate ansatz as **"a common
dynamical mass `m` on every flavour"**, flavour-diagonal with a single `Φ`.

**For the Wilson ledger of §3.2 the branch masses are `m + 2n` with
`n = 0…4`, which are not equal.** For the overlap ledger of §3.4 the massless
and cutoff-scale branches are likewise not degenerate. **So treating a Wilson
or overlap species ledger as additional flavours of the existing derivation
would violate that derivation's own frozen ansatz**, and the gap condition at
line 145 would have to be re-derived rather than re-used with a substituted
`N`.

**The naive ledger is degenerate and the staggered tastes are degenerate in the
free theory**, so the ansatz is not violated at free level for those two — **but
degeneracy of the free ledger is not by itself the mapping**, since routes 1, 2
and 3 remain undistinguished for them too.

### 7.4 The mapping, per candidate

    naive       NOT ESTABLISHED   Free ledger degenerate, so §7.3's ansatz
                                  obstruction does not arise; routes 1, 2 and 3
                                  remain undistinguished by the repository.
    Wilson      NOT ESTABLISHED   Routes undistinguished, and §7.3's ansatz
                                  obstruction applies: the branch masses are
                                  not equal.
    staggered   NOT ESTABLISHED   Routes undistinguished; and the Dirac trace
                                  at line 31 would itself require re-derivation
                                  in the reconstructed taste basis, so route 2
                                  is not even well posed without that.
    overlap     NOT ESTABLISHED   Routes undistinguished, and §7.3's ansatz
                                  obstruction applies.

    mapping ESTABLISHED        0
    mapping NOT ESTABLISHED    4

**Therefore no revised `G_c` is reported for any candidate**, and none is
computed. A consequence drawn through a link the repository does not contain
would be worse than no consequence.

**The adopted parameter domain is not recomputed or reinterpreted here.** The
domain is stated as `G/G_c` and the ratio is unaffected by a change in `N`;
whether any statement reads `G/G_c` as a physical quantity is a later task's.

---

## 8. §F — the Brillouin-zone involution, and the Wilson-specific connection

### 8.1 The involution, and the complement identity DERIVED

**The map is `p_μ → π − p_μ` on every axis.** It is a bijection of `(−π, π]⁴`
onto itself modulo `2π` with unit Jacobian, so it preserves the momentum
measure. **It is a map of the WHOLE zone.**

**DERIVED HERE, VERIFIED HERE numerically at a random momentum:**

    sin(π − p_μ) = sin p_μ                    ⟹   s(π − p) = s(p)
    1 − cos(π − p_μ) = 1 + cos p_μ            ⟹   W(π − p) = 8 − W(p)

the second because `Σ_μ (1 + cos p_μ) = 4 + Σ_μ cos p_μ = 8 − Σ_μ (1 − cos p_μ)`.

**Now apply the involution together with `Mhat → −8 − Mhat`.** With
`w(Mhat, p) = Mhat + W(p)`:

    w(−8 − Mhat, π − p) = (−8 − Mhat) + (8 − W(p)) = −(Mhat + W(p)) = −w(Mhat, p)

**VERIFIED HERE numerically.** The denominator `s + w²` depends on `w` only
through `w²`, so it is invariant. Since the involution preserves the measure,

    I0(Mhat) = I0(−8 − Mhat)

**DERIVED HERE.** **The identity is a change of integration variable over the
entire Brillouin zone. It is not a statement about any one corner.**

### 8.2 The corner association, DERIVED and stated as conditional

**DERIVED HERE:** the involution maps the neighbourhood of the origin onto the
neighbourhood of the all-`π` corner, since `p = 0 ↔ p = π` componentwise.

**DERIVED HERE:** at `Mhat = −8` the Wilson branch mass at the all-`π` corner
is `Mhat + 2n` with `n = 4`, that is `−8 + 8 = 0`. **So the all-`π` branch is
the branch that becomes light as `Mhat` approaches `−8`.**

**Therefore: a stationary branch near `Mhat ≈ −8` is associable with the
all-`π` Wilson doubler branch, and the association is derived rather than
assumed.** It is **conditional** in a way worth stating exactly: the identity
is a whole-zone statement, and only the identification of *which* branch goes
light at that end of the range is corner-specific.

**The `DEFERRED-02` branch. MEASURED:** that entry records a negative-mass
stationary branch at `M̂ ≈ −7.59`, and records the exact Wilson-complement
relation `I_0(M̂) = I_0(−8−M̂)` "induced by `p_mu -> pi-p_mu`" as its evidence.
**The involution derived in §8.1 is the same map**, and `−7.59` lies near the
`−8` end of the range where §8.2 derives the all-`π` branch to be the light one.

**So: yes — under a Wilson canonical operator, the `DEFERRED-02` branch is
associable with the doubler sector's reflection.** DERIVED HERE, and
conditional on Wilson.

**What is NOT ESTABLISHED here:** that `M̂ ≈ −7.59` specifically is the all-`π`
branch's mass zero rather than a nearby stationary point of the interacting
reduced potential — the recorded root is a stationary point of a coupled
scalar potential, not a free-operator mass zero, and identifying the two would
require a computation this task is not authorised to perform.

### 8.3 What that would mean for `C1` and `C3`

**MEASURED, `derivations/P2-PHASE-01_C3_curvature_asymmetry.md` lines 159–163:**
"the curvature asymmetry carries no independent physical content. Combined with
`C1`, the negative-mass branch then has no independent content of any kind that
has been demonstrated — its stored position is fixed by the Wilson-complement
identity, and its curvature ratio is fixed by that position and a prefactor."

**MEASURED, `derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md` lines 22–24:** `C1`
established that the production complement root "is NOT constructed from the
ordinary root, but recovered by a separate bracketed search."

**The reading §8.2 supports, stated exactly.** If the branch is the all-`π`
sector seen through the involution, then **it carries no independent content
BECAUSE it is the mirror of the ordinary branch under an exact whole-zone
symmetry — not because it is spurious.** The involution is a symmetry of the
Wilson denominator, so a quantity computed on one side is determined by the
other; that is a reason for the absence of independent content, and it is a
different statement from the branch being an artifact.

**DERIVED HERE: this reading changes no measurement.** `C1`'s finding about how
the root is obtained, and `C3`'s closed form and its verification figures, are
statements about the code and the stored numbers. **The involution neither adds
to nor subtracts from either.** `C3` itself records at line 168 that its
consequence is "a finding about what the existing evidence supports, NOT a
demonstration that the branch is unphysical", and the reading here is
consistent with that and does not strengthen it.

**Under §0's ruling and a Wilson canonical operator, the all-`π` corner is a
species rather than an artifact** — a lifted one, at mass `m + 8` when `Mhat`
is near zero. **That is a statement about a candidate the programme has not
adopted.**

### 8.4 Confinement of the association

**This association is confined to the Wilson candidate and is not extended to
any other.** DERIVED HERE: §6.1 shows the naive denominator has no `W` term and
obeys a reflection about `0` rather than about `−4`; §6.3 records the staggered
case as NOT ESTABLISHED; §6.4 derives an `M_0 ↔ 8 − M_0` analogue for the
overlap which relates *conventions* rather than a mass to its complement.

**The canonical operator is not chosen.** Every statement in this section is
therefore conditional on a candidate the programme has not adopted, and none of
it is a reason to adopt it.

---

## 9. What this dossier does not establish

- **It does not select, rank, recommend or prefer a candidate**, and nothing in
  it should be read as doing so. The counts in §5.5 and §4.5 are inventories of
  what the repository establishes, not scores.
- **It does not freeze anything** — not the operator, not the measure, not the
  geometry map, not the species ledger.
- **It does not close `OPEN-AC-4`, does not make `C-iii` evaluable, and does
  not authorise `D0`.**
- **It does not establish that the four candidates are the complete set.**
  `P2-LATTICE-ONTOLOGY-01` line 347 names four; whether a fifth formulation
  satisfies the frozen obligations is not addressed here.
- **Its completeness is bounded by this repository**, which contains no
  literature. Every gap is marked `NOT ESTABLISHED` at the point where it
  arises rather than summarised away.

## 10. No selection was made

**No candidate is selected.** No sentence in this artifact states or implies
that any candidate should be chosen, and the four candidates are treated at
comparable depth by construction — §3 gives each its own derivation section,
§4 assesses each against the same standard, §5 reports all sixteen checks, §6
gives each a consequence statement, and §7 gives each a mapping result.

**Where a candidate's entry is longer, it is because more was derivable, not
because more was favoured.** Where an entry reads `NOT ESTABLISHED`, that
records a silence in the repository and is not a mark against the candidate.
