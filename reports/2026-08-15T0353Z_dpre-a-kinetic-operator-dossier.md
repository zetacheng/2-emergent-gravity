# Execution report — `D-pre-A`: the canonical kinetic operator, candidate dossier and selection grounds

**Specification:** `specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md`
**Specification evidence base:** `ae3604def317667b44ea59458569ba105463fd6b`
**Branch:** `science/dpre-a-kinetic-operator-dossier`, cut from authoritative `main` @ `ae3604de…`
**Classification:** MATERIAL. Governed by Rule 15, Rule 18, and **Amendments M–P and Rules 19–21.**

**Every figure below is labelled MEASURED, DERIVED, INTENDED or NOT
ESTABLISHED.** **This report is written at commit 3 and measures nothing at
commit 4.**

**This task does not touch `main`.** It produces a branch. **It freezes nothing
and selects nothing.**

---

## 1. Outcome

**A dossier, a deferred entry, and no selection.**

**MEASURED at commit 3:** 3 additions and 1 modification; `DEFERRED-04`
appended with 0 deleted lines, base a byte prefix of head and an exact in-order
subsequence at 194 of 194; `DEFERRED-01`, `-02` and `-03` byte-identical; 407
of 407 other paths blob-identical; validators unchanged at 324 passed, 2
deselected; all four checker invocations exit 0 with `overall: PASS`, `P7`
reading fourteen sections, and **`P3` passing on BOTH declared append-only
paths** — the first task to declare more than one.

**The derivation tally, MEASURED over the dossier:** 43 statements marked
`DERIVED HERE`, 8 of them additionally `VERIFIED HERE` against explicit matrix
representations, and 36 marked `NOT ESTABLISHED`.

**Headline results, all DERIVED:**

    naive       16 Dirac species, all at mass m, none lifted, none absent
    Wilson      16 branches: one at m, fifteen LIFTED to m + 2n
    staggered    4 tastes; twelve of the naive sixteen ABSENT, not lifted
    overlap     Σ_{2n < M_0} C(4,n) massless, remainder lifted at the cutoff

**Reflection positivity: NOT ESTABLISHED for all four**, at the same standard.
**Compatibility: 6 COMPATIBLE, 0 INCONSISTENT, 10 NOT ESTABLISHED** across the
sixteen checks. **Species-to-`N` mapping: NOT ESTABLISHED for all four, so no
revised `G_c` is reported for any candidate.**

**No candidate was selected, ranked, recommended or preferred.** §12 reports
the search and the treatment depths.

---

## 2. Refs and pinned inputs — A1

**MEASURED, `refs/heads/main` read from `origin` with `git ls-remote`:**

    refs/heads/main    ae3604def317667b44ea59458569ba105463fd6b

**Matches the specification. No mismatch, no STOP.**

**Blob ids at the evidence base, MEASURED:**

    derivations/P2-LATTICE-ONTOLOGY-01.md            6544fb1a72eff49b4af4a1767d63405ddb87e4b8
    derivations/P2-LATTICE-ROUTE-01.md               42be438ff1a4eb1994545cbadabe85cb1f448ad8
    derivations/P2-GENERATOR-SUM-CRITICALITY_01.md   47c28e26a26f2c877bf9dc494fb4e1cd5e18bf52
    derivations/P2-DEFERRED-ITEMS.md                 33b3a664e0578ded484e31ad7f96f3a2908bcbb1
    scripts/p2_phase01_scalar_exploratory.py         b44bc63d115f4e88a706d046e60488c51d8a06a0

**As recorded since the `C-c` task, this container's local `refs/heads/main` is
stale** at `0f79617…`, a strict ancestor of the authoritative ref. **No
measurement here reads it.**

---

## 3. The review binds to these bytes — A2

**MEASURED.**

    SHA-256 of the arriving specification      04ddaf0eb17f40f29410fbd47c672b0be08b3c3d9781ced9669d7036bbcca04d
    SHA-256 the review records as reviewed     04ddaf0eb17f40f29410fbd47c672b0be08b3c3d9781ced9669d7036bbcca04d

**Equal.** Both arriving files were committed byte-identical, verified by
`cmp`. **Neither was modified.**

The review's verdict is **APPROVED FOR EXECUTION**. Its non-blocking
clarification — that describing a Wilson all-`π` corner as a microscopic
species must not be broadened into a claim that it is necessarily an
independent light infrared particle — **is honoured explicitly in the dossier
§3.2 and §8.3**, where the corner's mass is given as `m + 2n`, of cutoff order
for every `n ≥ 1`.

---

## 4. The species ledgers — A3

**Each ledger was derived by that formulation's own method.** The methods are
stated below with the reason each suits its formulation, because a shared
method would have been one candidate's ruler applied to all four.

**Before the candidates, one piece of shared machinery was derived once.**
`DERIVED HERE, VERIFIED HERE`: at a corner `π_A` with `|S| = n` components
equal to `π`, the expansion `p = π_A + k` gives
`sin(π_{A,μ} + k_μ) = σ_μ sin k_μ` with `σ_μ = ±1`, so
`γ̃_μ = σ_μ γ_μ` satisfies `{γ̃_μ, γ̃_ν} = 2δ_μν` and
`γ̃_5 = (−1)^{|S|} γ_5`. **Verified over all sixteen corners against an
explicit `4×4` Euclidean representation** — the Clifford property and the
chirality relation both.

**This is shared machinery, not a shared answer.** The four candidates convert
it into four different ledgers by four different routes.

### 4.1 Naive — corner expansion about the degenerate zeros

**Why this method.** The zeros are isolated points of the full zone and the
field carries the full four-component Dirac index at every site, so expanding
about each zero returns a Dirac branch directly with nothing reconstructed.

**DERIVED:** `D_naive = iΣγ_μ sin p_μ + m` vanishes at `m = 0` only where
`sin p_μ = 0` for every `μ`, hence `p_μ ∈ {0, π}` — the sixteen corners and no
others. Each carries a four-component Dirac branch at mass `m`, the operator
containing no term that distinguishes corners.

    species              16 Dirac, all degenerate at mass m
    momentum regions     the sixteen corner neighbourhoods, unreduced zone
    lifted               none
    absent               none
    chirality            8 corners at +γ_5, 8 at −γ_5     DERIVED

**Raw zero counting: USED, and licensed.** The licence is derived, not
asserted — §4's shared machinery shows each zero yields one full Dirac branch
and no field components were removed or recombined, so sixteen zeros mean
sixteen species. **The licence is specific to this candidate and was not
exported.**

**NOT ESTABLISHED:** whether the sixteen are distinguishable by any observable
this programme defines; the interacting fate of the degeneracy.

### 4.2 Wilson — corner branches together with the Wilson mass shifts

**Why this method.** The zero structure before the `r`-term is the naive one,
so the shared expansion applies unchanged; what the method must add is the
corner-dependent mass that distinguishes the branches.

**DERIVED:** with `D_W = iΣγ_μ sin p_μ + m + r W(p)` at `r = 1`, and `W = 2n`
at a corner, the branch mass is `m_n = m + 2n`.

    n = 0    1 corner     mass m          the ordinary branch
    n = 1    4 corners    mass m + 2
    n = 2    6 corners    mass m + 4
    n = 3    4 corners    mass m + 6
    n = 4    1 corner     mass m + 8
             16 total

    species     16 Dirac branches
    lifted      15, to masses m + 2n set by the cutoff
    absent      none — the Wilson term shifts masses and removes no
                degree of freedom

**Raw zero counting: USED for the corner LOCATIONS only, and licensed only for
those.** The species content is read from the mass at each corner. **Counting
poles alone would report sixteen degenerate species and would be wrong about
fifteen of them** — the same error in the opposite direction to the staggered
one.

**NOT ESTABLISHED:** `r = 1` as canonical — it is what the exploratory script
uses, not something the repository freezes; the interacting fate of the lifted
branches.

### 4.3 Staggered — spin/taste reconstruction, and NOT one-component zero counting

**Why this method, stated before any number.** The field carries one component
per site, not four, so the zeros of the one-component momentum operator are not
in one-to-one correspondence with Dirac branches. **The reconstruction must be
performed before any count is reported.**

**DERIVED, VERIFIED over all `x ∈ {0,1}⁴` and all `μ`:** with
`Γ(x) = γ_1^{x_1}γ_2^{x_2}γ_3^{x_3}γ_4^{x_4}` and
`η_μ(x) = (−1)^{x_1+…+x_{μ−1}}`,

    Γ(x)† γ_μ Γ(x + μ̂) = η_μ(x) · 1_4

**The Dirac structure becomes proportional to the identity**, exhibiting the
naive operator as **four decoupled identical copies** of the one-component
staggered operator.

**DERIVED:** keeping one copy keeps one quarter of the naive content —
`16 naive species / 4 copies = 4 tastes`, each a four-component Dirac fermion,
reconstructed on `2⁴` blocks over the **reduced** zone `(−π/2, π/2]⁴` where the
sixteen block components furnish `4 Dirac ⊗ 4 taste`.

    species     4 tastes, each 4-component Dirac
    zone        the REDUCED zone, not the unreduced one the other ledgers use
    lifted      none — the four are exactly degenerate in the free theory
    absent      12 of the naive 16, removed by discarding three of four
                decoupled copies: a reduction of field content, not a mass term

**Raw zero counting: NOT USED, and the reason is on the record.** The
one-component operator has **sixteen** zeros; the taste count is **four**. The
factor is the discarded Dirac copies. **Reporting sixteen here would be a
derivation error, not a different convention** — and it is the specific error
the specification names as a STOP.

**NOT ESTABLISHED:** whether the reduced-zone reconstruction satisfies the
isotropy freeze as worded — §6.3 records the question rather than answering it;
the interacting taste-symmetry structure.

### 4.4 Overlap — the free spectrum of the overlap operator itself

**Why this method.** The overlap operator is not a corner-local modification of
the naive one but a function of a kernel, so its branches must be read from its
own spectrum rather than from an expansion of the kernel it is built from.

**Convention, stated as required and not chosen:**
`D_ov = 1 + γ_5 sign(H_W)`, `H_W = γ_5(D_W − M_0)` with `D_W` the Wilson
operator at `r = 1`, `m = 0`, and `M_0` the kernel mass / domain-wall height.

**DERIVED, VERIFIED:** `H_W² = [s(p) + (W(p) − M_0)²] · 1_4`, hence

    D_ov(p) = 1 + [ iΣγ_μ sin p_μ + (W − M_0) ] / √( s + (W − M_0)² )

**DERIVED:** at a corner `s = 0`, `W = 2n`, so `D_ov = 1 + sign(2n − M_0)`,
which is `0` when `2n < M_0` and `2` otherwise.

**VERIFIED at `M_0 = 1, 3, 5, 7, 9`** by evaluating `D_ov` at all sixteen
corners with an explicit representation and counting the null ones:

    number of massless Dirac species = Σ_{n : 2n < M_0} C(4,n)

    0 < M_0 < 2    1        4 < M_0 < 6    11
    2 < M_0 < 4    5        6 < M_0 < 8    15
                            M_0 > 8        16

    lifted      the non-massless corners, at D_ov = 2, i.e. the far side of
                the spectral circle — present at the cutoff, not absent
    absent      none

**The species count is a function of the stated convention and is not a
property of "the overlap" without it.** Reporting a single number without `M_0`
would be the unanchored figure this programme has had to retract before.

**Raw zero counting: USED on `D_ov` itself, licensed for that operator** by the
closed form above — the zeros counted are those of the physical fermion
operator, not of a kernel. **The licence does not transfer to the kernel's own
zeros, which are Wilson's.**

**NOT ESTABLISHED:** which `M_0` the programme would adopt, that being part of
the choice this task does not make; whether the non-ultralocality of §5.4
obstructs any frozen obligation.

### 4.5 Figures marked NOT ESTABLISHED in A3

**MEASURED: nine**, distributed two, two, two and three across naive, Wilson,
staggered and overlap. **No figure is reported without its derivation**, and
"standard result" appears nowhere in the dossier as a justification.

---

## 5. Reflection positivity — A4

`P2-LATTICE-ONTOLOGY-01` line 181 freezes reflection positivity **as an
obligation**, and lines 81–84 record that it "has teeth — it constrains the
kinetic-operator choice directly".

**MEASURED: no reflection-positivity construction for any candidate exists in
this repository.**

    naive       NOT ESTABLISHED   nothing in the repository; nothing derived here
    Wilson      NOT ESTABLISHED   with a repository assertion recorded, §5.2
    staggered   NOT ESTABLISHED   nothing in the repository; nothing derived here
    overlap     NOT ESTABLISHED   with a derived obstruction to one method family

    satisfied         0
    violated          0
    NOT ESTABLISHED   4

### 5.2 The Wilson assertion, recorded as an assertion

**MEASURED, `P2-LATTICE-ONTOLOGY-01` lines 82–84:** "standard Wilson
formulations admit reflection-positive constructions under the relevant
conditions; not every discretization does."

**That is an assertion in a committed artifact and it is not a derivation.**
The relevant conditions are not stated, no construction is given, and this task
did not supply one. **Recorded as on record; NOT ESTABLISHED as derived.**
Treating it as established would have been exactly the recalled claim A4 says
is less useful than an honest gap.

### 5.4 The overlap obstruction, derived, and what it is not

**DERIVED: the free overlap operator is not ultralocal.** A finite-range
lattice kernel has a momentum-space form that is a trigonometric polynomial;
`D_ov` contains `[s + (W − M_0)²]^{−1/2}`, and the inverse square root of a
non-constant positive trigonometric polynomial is not one. **So the action
couples every pair of time-slices.**

**Reflection-positivity constructions that split the action into two
half-lattice pieces plus a nearest-neighbour-in-time cross-term therefore do
not apply as stated.** **This is an obstruction to a family of methods, not a
demonstration that the obligation fails**, and it is recorded as the former.

**Recorded so it is not misread as a mark against the candidate:** the Wilson
entry rests on an assertion nobody has verified here, and the overlap entry
rests on a derived fact about method applicability. **Both are NOT
ESTABLISHED**, and the asymmetry in the reasons is not an asymmetry in the
result.

---

## 6. Compatibility with the frozen items — A5, sixteen results

### 6.1 A finding first: the table freezes FIVE items, not four

**MEASURED, `P2-LATTICE-ONTOLOGY-01` lines 180–184:**

    180  Formulation (Euclidean-fundamental; Hamiltonian derived)   FROZEN HERE
    181  Reflection positivity of the action                        FROZEN HERE as obligation
    182  Isotropy of the four axes                                  FROZEN HERE
    183  Lattice: ontologically dynamical, operationally static     FROZEN HERE
    184  Vacuum selection rule                                      FROZEN HERE

**Line 183 also reads `FROZEN HERE`.** The specification's §2(c) and A5 name
four items — 180, 181, 182 and 184 — and omit it.

**I performed the sixteen checks the criterion names**, and report the omission
as a finding rather than silently adding a fifth column. **MEASURED, line
183's own text at lines 130–143:** it describes "dynamical lattice" as "an
ontology OBLIGATION, not a completed microscopic declaration", constraining
substrate variables still to be identified. **On that reading it distinguishes
no candidate**, which is why its omission changed no result — but the omission
is a fact about the criterion, not about the repository, and it is recorded.

### 6.2 The sixteen results

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
instance to report. **The count of `COMPATIBLE` results is not a score and is
not used as one.**

### 6.3 The one entry that could be misread as a finding against a candidate

**Line 182's frozen content, MEASURED at line 94: "H(4) isotropy (equal
couplings on all four axes)".**

**DERIVED:** the staggered phases `η_μ(x) = (−1)^{x_1+…+x_{μ−1}}` are not
symmetric under permutation of the axes — `η_1 ≡ 1` while `η_4` depends on
three coordinates. **The coupling MAGNITUDES are equal on all four axes; the
sign patterns single out an axis ordering.**

**Whether line 182 requires manifest axis symmetry of the action, or equality
of couplings up to a field redefinition, is not settled by the text.** **So the
entry reads `NOT ESTABLISHED`, not `INCONSISTENT`.** Declaring staggered
inconsistent would have been a conclusion drawn on an unresolved reading, and
it would have functioned as a ranking. **Resolving the reading is not this
task's.**

**Line 184's four `NOT ESTABLISHED` results share one cause, derived:** the
rule is operationally defined at lines 146–154 over the **reconstructed
transfer matrix**, which is line 181's unmet obligation. **No candidate can be
checked against it until that obligation is discharged for that candidate.**

---

## 7. Consequences for the existing computed evidence — A6

**MEASURED at the evidence base, `scripts/p2_phase01_scalar_exploratory.py`
lines 80–82:** the denominator is `s + w·w` with `s = Σ_μ sin²p_μ` and
`w = Mhat + Σ_μ(1 − cos p_μ)`. **That is a Wilson-form kernel at `r = 1`.**

**MEASURED: the script was not run and nothing about the exploratory kernel was
recomputed.** The blob is byte-identical at base and head, inside §9's 407 of
407.

**These are consequences, not arguments.** Continuity with existing computation
is a convenience; §0's ruling requires independent physical and structural
grounds, and what weight continuity carries is the PI's.

    naive       stored results become evidence about a theory not adopted.
                DERIVED: w = Mhat, denominator s + Mhat².
                COMPLEMENT RELATION DOES NOT HOLD. DERIVED: the denominator
                is even in Mhat, giving I0(Mhat) = I0(−Mhat) — a reflection
                about 0, not about −4. The 8 comes from W's range and W is
                absent.

    Wilson      stored results remain evidence about the canonical theory,
                conditional on r = 1 and the Mhat convention.
                COMPLEMENT RELATION HOLDS EXACTLY — derived in §8.
                Not established even here: the script's I0 already sums all
                sixteen corners, and whether that sum is the right object once
                the corners are species rather than artifacts is a question
                §8 shows the repository does not answer.

    staggered   stored results become evidence about a theory not adopted.
                DERIVED: the field is one-component, so the bubble's Dirac
                structure and the frozen trace(Id4) = 4 at line 31 do not
                carry over; integrand and trace factor both need re-derivation
                in the reconstructed taste basis over the reduced zone.
                COMPLEMENT RELATION: NOT ESTABLISHED. No W term, so no direct
                analogue; whether the taste-basis propagator carries some
                other involution symmetry was not derived.

    overlap     stored results become evidence about a theory not adopted.
                DERIVED: D_ov is not the script's s + w² for any Mhat.
                COMPLEMENT RELATION: a structural ANALOGUE is derived, and it
                is an analogue and not the relation. Under p → π − p,
                W − M_0 → −(W − (8 − M_0)), so the involution relates the
                CONVENTION M_0 to 8 − M_0 rather than a mass to its
                complement. Consistently with §4.4's ledger, M_0 and 8 − M_0
                lie symmetrically about 4 and their species counts are the two
                ends of the same table. No numerical consequence is drawn.

---

## 8. The species-to-`N` mapping — A7

### 8.1 What `N` is, MEASURED with line numbers, not restated from the specification

**MEASURED, `derivations/P2-GENERATOR-SUM-CRITICALITY_01.md`:**

    line 23      X = (G/(2N)) * Sum( bilinear(lam(A),Id4)**2
                                   + bilinear(lam(A),I*gamma5)**2, (A,0,N**2-1) )
    line 25      S^A = ψ̄ (λ^A ⊗ 1_4) ψ ,   P^A = ψ̄ (λ^A ⊗ iγ_5) ψ
    line 28      Tr(λ^A λ^B) = 2 δ^{AB},  A = 0 … N²−1,  λ^0 = √(2/N)·1_N
    lines 29-30  {λ^A} is a complete Hermitian basis of the N×N complex
                 matrices (N² of them)
    line 31      Dirac trace, frozen separately: trace(Id4) = 4
    lines 41-44  condensate ansatz: flavour-diagonal ⟨ψ̄_i ψ_j⟩ = δ_ij Φ, with
                 "a common per-flavour Dirac-traced amplitude Φ and a common
                 dynamical mass m on every flavour"

**The gap condition, MEASURED at line 145:**

    1 = (8/N) G I_0   ⟹   G_c^{(b)} = N/(8 I_0)

**MEASURED, lines 147–150:** the factor `8/N` is `2` (Hartree) `× 4` (Dirac
trace) `× (1/N)`.

**So `N` is the `U(N)` flavour rank**, carried by the index the `λ^A` act on.
**DERIVED: it is not a Dirac index** — line 25 shows the Dirac structure
entering as a separate tensor factor `1_4`, and line 31 accounts for it
separately. **It is not a lattice species multiplicity, and no line in the
repository states that one multiplies into the other.**

**MEASURED, `P2-LATTICE-ONTOLOGY-01` line 356:** "the species multiplicity
enters `N`-accounting explicitly". **It states that it does. It does not state
how.**

### 8.2 Three places a multiplicity could enter, enumerated and not chosen among

**DERIVED from the structure above**, a lattice species multiplicity could
enter at any of:

1. **the flavour rank `N`** — if the species are additional flavours the `λ^A`
   act on, which requires them degenerate and interchangeable;
2. **the Dirac-trace factor `4`** at line 31 — if the species are additional
   spinor components rather than additional flavours;
3. **the bubble `I_0` itself** — line 38 defines `B(Σ)` as an integral over the
   momentum measure, and a lattice integral over the full zone already receives
   a contribution from every corner.

**Enumerating three routes is not deriving which applies**, and no route is
selected here. **Route 3 matters especially: if a multiplicity is already
inside `I_0`, multiplying `N` as well would double-count it.**

### 8.3 An obstruction that applies before any of the three, DERIVED

**MEASURED, lines 41–44:** the condensate ansatz is frozen as "a common
dynamical mass `m` on every flavour", flavour-diagonal with a single `Φ`.

**DERIVED: the Wilson ledger's branch masses are `m + 2n`, `n = 0…4`, which are
not equal**, and the overlap ledger's massless and cutoff-scale branches are
likewise not degenerate. **So treating a Wilson or overlap species ledger as
additional flavours of the existing derivation would violate that derivation's
own frozen ansatz**, and line 145 would have to be re-derived rather than
re-used with a substituted `N`.

**The naive ledger is degenerate and the staggered tastes are degenerate at
free level**, so the ansatz is not violated for those two — **but free-level
degeneracy is not the mapping**, since routes 1, 2 and 3 remain
undistinguished for them too.

### 8.4 The mapping, per candidate

    naive       NOT ESTABLISHED   ansatz obstruction does not arise; routes
                                  1, 2, 3 undistinguished by the repository
    Wilson      NOT ESTABLISHED   routes undistinguished, AND §8.3's ansatz
                                  obstruction applies
    staggered   NOT ESTABLISHED   routes undistinguished; and trace(Id4) = 4
                                  at line 31 would itself need re-derivation
                                  in the taste basis, so route 2 is not even
                                  well posed
    overlap     NOT ESTABLISHED   routes undistinguished, AND §8.3's ansatz
                                  obstruction applies

    mapping ESTABLISHED        0
    mapping NOT ESTABLISHED    4

**Therefore no revised `G_c` is reported for any candidate, and none was
computed.** **No taste or doubler count was multiplied into `N` anywhere**, in
the dossier or here.

**The adopted parameter domain was not recomputed or reinterpreted.** The
domain is stated as `G/G_c` and the ratio is unaffected by a change in `N`;
whether any statement reads `G/G_c` as a physical quantity is a later task's.

---

## 9. The involution and the Wilson-specific connection — A8

### 9.1 The complement identity, DERIVED from the involution

**The map is `p_μ → π − p_μ` on every axis, a bijection of `(−π, π]⁴` onto
itself modulo `2π` with unit Jacobian, so it preserves the momentum measure.**
**It is a map of the WHOLE zone.**

**DERIVED, VERIFIED numerically at a random momentum:**

    sin(π − p_μ) = sin p_μ                 ⟹  s(π − p) = s(p)
    1 − cos(π − p_μ) = 1 + cos p_μ         ⟹  W(π − p) = 8 − W(p)

the second because `Σ_μ(1 + cos p_μ) = 4 + Σ_μ cos p_μ = 8 − Σ_μ(1 − cos p_μ)`.

**Applying the involution together with `Mhat → −8 − Mhat`, DERIVED and
VERIFIED:**

    w(−8 − Mhat, π − p) = (−8 − Mhat) + (8 − W(p)) = −(Mhat + W(p)) = −w(Mhat, p)

The denominator `s + w²` depends on `w` only through `w²`, so it is invariant;
the involution preserves the measure; therefore

    I0(Mhat) = I0(−8 − Mhat)

**DERIVED.** **The identity is a change of integration variable over the entire
Brillouin zone, and is not a statement about any one corner.**

### 9.2 The corner association, DERIVED and stated as conditional

**DERIVED:** the involution maps the origin neighbourhood onto the all-`π`
corner neighbourhood, since `p = 0 ↔ p = π` componentwise.

**DERIVED:** at `Mhat = −8` the Wilson branch mass at the all-`π` corner is
`Mhat + 2n` with `n = 4`, i.e. `−8 + 8 = 0`. **So the all-`π` branch is the one
that becomes light as `Mhat` approaches `−8`.**

**MEASURED, `DEFERRED-02`:** it records a negative-mass stationary branch at
`M̂ ≈ −7.59`, and records the exact relation `I_0(M̂) = I_0(−8−M̂)` "induced by
`p_mu -> pi-p_mu`" as its evidence. **The involution derived above is the same
map**, and `−7.59` lies near the `−8` end of the range.

**So: yes, under a Wilson canonical operator the `DEFERRED-02` branch is
conditionally associable with the doubler sector's reflection.** **DERIVED, and
conditional on Wilson.**

**NOT ESTABLISHED:** that `M̂ ≈ −7.59` specifically is the all-`π` branch's mass
zero rather than a nearby stationary point of the interacting reduced
potential. The recorded root is a stationary point of a coupled scalar
potential, not a free-operator mass zero, and identifying the two would require
a computation this task is not authorised to perform. **The association is
therefore of the branch with the sector, not of the number with the number.**

### 9.3 What it implies for `C1` and `C3`

**MEASURED, `derivations/P2-PHASE-01_C3_curvature_asymmetry.md` lines 159–163:**
"the curvature asymmetry carries no independent physical content. Combined with
`C1`, the negative-mass branch then has no independent content of any kind that
has been demonstrated."

**MEASURED, `derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md` lines 22–24:** `C1`
established that the production complement root "is NOT constructed from the
ordinary root, but recovered by a separate bracketed search."

**The reading §9.2 supports, stated exactly as the specification frames it:**
if the branch is the all-`π` sector seen through the involution, then **it
carries no independent content BECAUSE it is the mirror of the ordinary branch
under an exact whole-zone symmetry — not because it is spurious.** The
involution is a symmetry of the Wilson denominator, so a quantity computed on
one side is determined by the other. **That is a reason for the absence of
independent content, and it is a different statement from the branch being an
artifact.**

**DERIVED: this reading changes no measurement.** `C1`'s finding about how the
root is obtained, and `C3`'s closed form and verification figures, are
statements about the code and the stored numbers. **The involution neither adds
to nor subtracts from either.** **MEASURED, `C3` line 168:** its consequence is
"a finding about what the existing evidence supports, NOT a demonstration that
the branch is unphysical" — **and the reading here is consistent with that and
does not strengthen it.**

**Under §1's ruling and a Wilson canonical operator, the all-`π` corner is a
species rather than an artifact** — a lifted one, at mass `m + 8` when `Mhat`
is near zero. **It is not thereby an independent light infrared particle**, and
nothing here says it is.

### 9.4 Confinement to Wilson, and the conditionality

**The association is confined to the Wilson candidate and was not extended.**
**DERIVED:** the naive denominator has no `W` term and obeys a reflection about
`0` rather than `−4`; the staggered case is `NOT ESTABLISHED`; the overlap
carries an `M_0 ↔ 8 − M_0` analogue relating **conventions**, not a mass to its
complement.

**The canonical operator is not chosen.** Every statement in §9 is conditional
on a candidate the programme has not adopted, **and none of it is a reason to
adopt it.**

---

## 10. `DEFERRED-04` — A9

**MEASURED, `derivations/P2-DEFERRED-ITEMS.md` base to commit 3:**

    added lines      60
    deleted lines     0

**Both append-only measures, MEASURED:**

    base is a BYTE PREFIX of head       True     8403 → 11442 bytes
    base is an exact in-order
      SUBSEQUENCE of head               True     194 of 194 lines matched

**These are two measurements, and the byte-prefix one is the stricter.** It is
also the one `P3` enforces — `check_p3` computes `after.startswith(before)` —
which decided where the entry goes; see §10.1.

**`DEFERRED-01`, `-02` and `-03` byte-identical, MEASURED by extracting each
section from both revisions and comparing:**

    DEFERRED-01   1798 bytes   identical
    DEFERRED-02   2788 bytes   identical
    DEFERRED-03   1463 bytes   identical

**MEASURED: the register now carries four entries**, `DEFERRED-01` to
`DEFERRED-04`.

### 10.1 Where the entry had to go, and why that is worth recording

**The register's three existing entries sit at lines 44, 87 and 149, and a
closing "Scope of this register" section runs from line 184 to the end.**
Placing `DEFERRED-04` among the entries — before the scope section, where it
belongs structurally — **would have preserved the subsequence property and
FAILED the byte-prefix one**, because insertion mid-file means the base is no
longer a prefix.

**So the entry is appended after the scope section, and says so in its own
first paragraph.** **I checked what `P3` enforces before choosing the position
rather than after**, which is the only reason this did not become a failing run
and a retraction.

**Recorded as an observation, not a finding against anything:** on this file,
"append-only" and "structurally correct placement" can point in different
directions, and the mechanical rule wins. **A register that grows only at its
end will accumulate entries after its own closing section.** Whether the
register wants a different closing structure is not this task's.

---

## 11. Scope, protected paths, gates — A11, A12, A13

**A11, MEASURED at commit 3:**

    M  derivations/P2-DEFERRED-ITEMS.md
    A  derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md
    A  reviews/chatgpt/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md
    A  specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md

    3 additions, 1 modification

**MEASURED: no status code other than `A` or `M` appears**, which is the
manifest's `forbidden_operations` list.

**INTENDED, base to commit 4:** 4 additions and 1 modification, the fourth
addition being this report. **That figure is INTENDED, not MEASURED: this
report is written before the commit containing it.**

**A12, MEASURED path by path:**

    paths at the evidence base                       408
    excluded (derivations/P2-DEFERRED-ITEMS.md)        1
    compared                                         407
    blob-identical                                   407
    differing                                          0
    missing at head                                    0

**The named ones, MEASURED individually:**

    GATES.md                                    2b3bd5069414   IDENTICAL
    CONVENTIONS.md                              8badc51f38d8   IDENTICAL
    derivations/P2-LATTICE-ONTOLOGY-01.md       6544fb1a72ef   IDENTICAL
    derivations/P2-LATTICE-ROUTE-01.md          42be438ff1a4   IDENTICAL
    scripts/p2_phase01_scalar_exploratory.py    b44bc63d115f   IDENTICAL

**The two lattice artifacts were consumed and not reopened.** **The exploratory
script was read and not run.** Everything under `results/`, `scripts/` and
`tests/` is inside the 407.

**A13, all four checks plus the pin question, MEASURED at commit 3:**

    1.  ^## P2- count                14
    2.  P2-PHASE-01                  Status: PROPOSED
    3.  first prerequisite           Prerequisite state: SATISFIED
    4.  second prerequisite          Prerequisite state: SATISFIED

    both pins match their targets:
      line 1017  derivations/P2-PHASE-01_microscopic_parameter_domain.md   MATCH
      line 1040  derivations/P2-PHASE-01_input_admissibility_contract.md   MATCH

    any pin names P2-DEFERRED-ITEMS.md:   False

**`derivations/P2-DEFERRED-ITEMS.md` is modified by this task and is pinned by
no gate, so no re-pin is owed under Rule 19.** **That was verified rather than
assumed**, through the committed pin collector rather than a hand-written
probe.

**No gate status or prerequisite state was changed. `P2-PHASE-01` is untouched
by this task.**

---

## 12. No selection was made — A10

**A10 is the criterion most easily satisfied in appearance, so it is reported
in three parts: a lexical search, a depth measurement, and a semantic
statement.**

### 12.1 The lexical search

**Search run over the dossier and this report**, case-insensitive, for:
`recommend`, `prefer`, `preferable`, `superior`, `better`, `best`, `worse`,
`worst`, `favour`/`favor`, `should be chosen`/`selected`/`adopted`,
`we choose`/`select`/`adopt`, `the right choice`, `the correct choice`,
`most suitable`, `advantage over`, `wins`.

**MEASURED in the dossier: three hits, none of which selects or ranks a
candidate.**

    line 638   "would be worse than no consequence"   — about a consequence
               drawn through a missing link, not about a candidate
    line 754   "It does not select, rank, recommend or prefer a candidate"
    line 771   "...that any candidate should be chosen"   — the denial

**MEASURED over the commit messages in this task's range: one hit**, in commit
2's message, quoting the review's own statement that the executor "is not
authorised to select, rank, recommend or freeze" a candidate. **A denial, not a
selection.**

**MEASURED over this report: every hit falls into one of three classes, and
none is a selection.** The classes are the search-term list quoted in this
section; the three dossier hits quoted above; and denials — "not that the
candidate is preferable", "I did not select, rank, recommend or prefer any
candidate", "in favour of a candidate on a reading I chose". **One further hit,
"the mechanical rule wins" in §10.1, is about `P3`'s prefix rule outranking
structural placement and concerns no candidate.**

**No sentence in the dossier, this report, or any commit message selects,
ranks, recommends or prefers a candidate.**

### 12.2 The depth measurement, which the lexical search cannot substitute for

**A dossier that treats one candidate at length and another briefly has ranked
them without saying so.** **MEASURED, lines in each candidate's dedicated
subsections** (species ledger, reflection positivity, consequences):

    naive        54
    Wilson       73
    staggered    69
    overlap      77

**Range 54 to 77.** **The shortest is naive, and the reason is that its ledger
is the simplest to state** — sixteen degenerate branches, nothing lifted,
nothing absent — **not that it received less attention.** Each candidate has a
dedicated section under every one of §3, §4, §6, §7 in the dossier, and a row
in every table.

**Whole-file mentions by name, MEASURED:**

    naive 27    Wilson 36    staggered 18    overlap 21

**Wilson's excess is disclosed and is specified rather than chosen.** **Ten of
its thirty-six mentions are inside §8**, the Wilson-specific involution section
the specification requires and confines to Wilson, and the remainder reflect
that the existing exploratory kernel is Wilson-form, which §6 must state as a
consequence. **Outside §8 the counts are naive 27, Wilson 26, staggered 18,
overlap 21.**

**Staggered's 18 is the lowest.** Its ledger is stated in fewer words because
the reconstruction argument is short once the diagonalisation identity is
given, and its subsection is the second-longest of the four at 69 lines. **The
mention count and the depth measure disagree here, and I report both rather
than the flattering one.**

### 12.3 The semantic statement

**No candidate is selected.** **No candidate is ranked.** **No candidate is
recommended.** **No preference is indicated.**

**The counts in §5 and §6 are inventories of what this repository establishes,
not scores.** A `NOT ESTABLISHED` entry records a silence in the repository and
is not a mark against a candidate; a `COMPATIBLE` entry records that a check
could be performed and passed, not that the candidate is preferable. **Nothing
in this task's output totals them.**

---

## 13. The checker — A14, MEASURED at commit 3

    base   ae3604def317667b44ea59458569ba105463fd6b
    head   d133a813f3897fbbe8e56867400699f62fe4449a   (commit 3)

**All four invocations exited 0 with `overall: PASS`.**

    run 1 INCLUSIVE   exit 0   PASS   sha256 88fe7bcf125246df3ece27797991f9791668656ecdc555551f4ddc251e932f8a
    run 1 EXCLUSIVE   exit 0   PASS   sha256 cf7130ad40c649ec783842037d2ec48a0b6bc0199a37c54b300525edc84e2f08
    run 2 INCLUSIVE   exit 0   PASS   sha256 88fe7bcf125246df3ece27797991f9791668656ecdc555551f4ddc251e932f8a
    run 2 EXCLUSIVE   exit 0   PASS   sha256 cf7130ad40c649ec783842037d2ec48a0b6bc0199a37c54b300525edc84e2f08

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 NOT_APPLICABLE
    P6 PASS   P7 PASS   P8 PASS   P9 NOT_APPLICABLE

**`P5` and `P9` are `NOT_APPLICABLE` because this task has no merge**, which is
the state the vocabulary was widened to express. **No property returned
`NOT_DECLARED`, `NOT_PARSEABLE` or `DECLARATION_CONFLICT`.**

### 13.1 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "ae3604def317667b44ea59458569ba105463fd6b",
      "head": "d133a813f3897fbbe8e56867400699f62fe4449a",
      "append_only_paths": ["DECISION_LOG.md", "derivations/P2-DEFERRED-ITEMS.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 13.2 RUN 2 config, verbatim — stop-governing

    {
      "base": "ae3604def317667b44ea59458569ba105463fd6b",
      "head": "d133a813f3897fbbe8e56867400699f62fe4449a",
      "specification_paths": ["specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md"],
      "append_only_paths": ["DECISION_LOG.md", "derivations/P2-DEFERRED-ITEMS.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I chose**; all are fixed by A14. **Neither
the config nor this specification's declarations were adjusted to make RUN 2
pass** — §9 of the specification forbids both, and neither was needed.

### 13.3 The measured RUN 1 subject set

**MEASURED: RUN 1's default selection chose exactly one specification**, and it
is the one RUN 2 names:

    specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md
        stated add 4 modify 1    counted add 4 modify 1    parse OK

**The range adds no other specification**, so the default and the named
selection coincide. **MEASURED: the two runs' outputs are byte-identical at
each prospectivity reading** — the sha256 pairs above are equal. **Both are
still given verbatim below, as A14 requires.**

The two prospectivity readings differ in the `inclusivity` field and in no
verdict.

### 13.4 `P3` with TWO declared paths — the first task to exercise it

**MEASURED, `P3` `PASS`, `declared_source: specification`, and the declared set
read from this specification's own scope block:**

    declared: ['DECISION_LOG.md', 'derivations/P2-DEFERRED-ITEMS.md']

**`P3`'s result for each of the two declared paths, as A14 requires:**

    DECISION_LOG.md                     PASS   deleted 0   prefix True   89541 → 89541 bytes
    derivations/P2-DEFERRED-ITEMS.md    PASS   deleted 0   prefix True    8403 → 11442 bytes

**One declared path is untouched by this task and one is modified by it, and
both were checked.** `DECISION_LOG.md` is unchanged, so its prefix test is
trivially satisfied and its byte counts are equal; `P2-DEFERRED-ITEMS.md` grew
by 3039 bytes with zero deletions and the base preserved as a prefix.

**This is the mechanism doing something it had not done before.** Every earlier
task declared a single append-only path. **The one-path-per-line form matters:
the specification records that an earlier draft wrote both paths on the
`append_only:` line and the parser returned `NOT_PARSEABLE`.** **MEASURED here:
the committed two-line form parses, and both paths reached `P3` as separate
subjects with separate results.**

### 13.5 `P7`, and the section count it saw

    declared_source          specification
    declared                 []
    raw_heading_count_head   14        section_count_head   14

**`P7` reports fourteen sections. `PASS` at zero would have been a STOP.**

### 13.6 Both declarations came from the specification

**MEASURED, identical in all four invocations:**

    P3   declared_source: specification    declared: ['DECISION_LOG.md',
                                                      'derivations/P2-DEFERRED-ITEMS.md']
    P7   declared_source: specification    declared: []

**MEASURED: `DECLARATION_CONFLICT` appears nowhere in any of the four
outputs.** The config supplied the same two sets, written to agree, so the
precedence rule resolved to `specification`.

### 13.7 RUN 1 output, verbatim

    {
      "base": "ae3604def317667b44ea59458569ba105463fd6b",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "d133a813f3897fbbe8e56867400699f62fe4449a",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "append_only": [
                "DECISION_LOG.md",
                "derivations/P2-DEFERRED-ITEMS.md"
              ],
              "authorised_gates": [],
              "counted": 5,
              "counted_add": 4,
              "counted_modify": 1,
              "counted_set": [
                "derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md",
                "reports/2026-08-XXT{HHMM}Z_dpre-a-kinetic-operator-dossier.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_dpre-a-kinetic-operator-dossier.md",
                "specs/2026-08-XXT{HHMM}Z_dpre-a-kinetic-operator-dossier.md",
                "derivations/P2-DEFERRED-ITEMS.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md",
              "stated": 5,
              "stated_add": 4,
              "stated_modify": 1,
              "stated_record": "stated: 4 additions, 1 modification"
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
                "commit": "51e3035b177b7dae3c9f5fd567bb576a0f19c39f",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "eb6ac5c49231f968b59c980349c4a668455be3b1",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "d133a813f3897fbbe8e56867400699f62fe4449a",
                "work_paths": [
                  "derivations/P2-DEFERRED-ITEMS.md",
                  "derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md"
                ]
              }
            ],
            "first_review_commit": "eb6ac5c49231f968b59c980349c4a668455be3b1",
            "first_work_commit": "d133a813f3897fbbe8e56867400699f62fe4449a",
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
              "DECISION_LOG.md",
              "derivations/P2-DEFERRED-ITEMS.md"
            ],
            "declared_by_specification": [
              "DECISION_LOG.md",
              "derivations/P2-DEFERRED-ITEMS.md"
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
              },
              {
                "base_bytes": 8403,
                "base_is_byte_prefix_of_head": true,
                "commits_with_deletions": [],
                "deleted_lines_base_to_head": 0,
                "head_bytes": 11442,
                "path": "derivations/P2-DEFERRED-ITEMS.md",
                "status": "PASS"
              }
            ],
            "specification_paths_read": [
              "specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md"
            ],
            "supplied_by_config": [
              "DECISION_LOG.md",
              "derivations/P2-DEFERRED-ITEMS.md"
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
              "commit": "51e3035b177b7dae3c9f5fd567bb576a0f19c39f",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "eb6ac5c49231f968b59c980349c4a668455be3b1",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "d133a813f3897fbbe8e56867400699f62fe4449a",
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
              "specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md"
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
            "first_commit": "51e3035b177b7dae3c9f5fd567bb576a0f19c39f",
            "first_commit_paths": [
              "specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md"
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

### 13.8 RUN 2 output, verbatim

    {
      "base": "ae3604def317667b44ea59458569ba105463fd6b",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "d133a813f3897fbbe8e56867400699f62fe4449a",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "append_only": [
                "DECISION_LOG.md",
                "derivations/P2-DEFERRED-ITEMS.md"
              ],
              "authorised_gates": [],
              "counted": 5,
              "counted_add": 4,
              "counted_modify": 1,
              "counted_set": [
                "derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md",
                "reports/2026-08-XXT{HHMM}Z_dpre-a-kinetic-operator-dossier.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_dpre-a-kinetic-operator-dossier.md",
                "specs/2026-08-XXT{HHMM}Z_dpre-a-kinetic-operator-dossier.md",
                "derivations/P2-DEFERRED-ITEMS.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md",
              "stated": 5,
              "stated_add": 4,
              "stated_modify": 1,
              "stated_record": "stated: 4 additions, 1 modification"
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
                "commit": "51e3035b177b7dae3c9f5fd567bb576a0f19c39f",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "eb6ac5c49231f968b59c980349c4a668455be3b1",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "d133a813f3897fbbe8e56867400699f62fe4449a",
                "work_paths": [
                  "derivations/P2-DEFERRED-ITEMS.md",
                  "derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md"
                ]
              }
            ],
            "first_review_commit": "eb6ac5c49231f968b59c980349c4a668455be3b1",
            "first_work_commit": "d133a813f3897fbbe8e56867400699f62fe4449a",
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
              "DECISION_LOG.md",
              "derivations/P2-DEFERRED-ITEMS.md"
            ],
            "declared_by_specification": [
              "DECISION_LOG.md",
              "derivations/P2-DEFERRED-ITEMS.md"
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
              },
              {
                "base_bytes": 8403,
                "base_is_byte_prefix_of_head": true,
                "commits_with_deletions": [],
                "deleted_lines_base_to_head": 0,
                "head_bytes": 11442,
                "path": "derivations/P2-DEFERRED-ITEMS.md",
                "status": "PASS"
              }
            ],
            "specification_paths_read": [
              "specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md"
            ],
            "supplied_by_config": [
              "DECISION_LOG.md",
              "derivations/P2-DEFERRED-ITEMS.md"
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
              "commit": "51e3035b177b7dae3c9f5fd567bb576a0f19c39f",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "eb6ac5c49231f968b59c980349c4a668455be3b1",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "d133a813f3897fbbe8e56867400699f62fe4449a",
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
              "specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md"
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
            "first_commit": "51e3035b177b7dae3c9f5fd567bb576a0f19c39f",
            "first_commit_paths": [
              "specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md"
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

## 14. Validators and hygiene — A15, A16

**A15, MEASURED, `python -m pytest` from the repository root, exit status 0
both times:**

    before, at the base ae3604de     324 passed, 2 deselected
    after,  at commit 3              324 passed, 2 deselected

**Unchanged, as expected: this task adds no test.** The "before" figure was
measured in a separate worktree checked out at the evidence base.

**A16, MEASURED on commits 1–3. Commit 4 is post-report evidence.**

    commit 1   51e3035b   spec: the canonical kinetic operator, candidate dossier and selection grounds
               trailer hits 0      not amended
    commit 2   eb6ac5c4   review: pre-execution review for the kinetic-operator dossier
               trailer hits 0      not amended
    commit 3   d133a813   derivations: the kinetic-operator candidate dossier, and DEFERRED-04
               trailer hits 0      not amended

**MEASURED over the whole range: a scan for `Co-Authored-By`, `claude.ai/code`,
`Generated with`, `Claude-Session` and `noreply@anthropic` returns nothing.**

**Rule 20 binds this task and was NOT exercised.** No commit was written with a
hygiene violation to repair. **No force-push, no branch deletion, no history
rewrite of any kind occurred.**

---

## 15. Commits

    commit 1   51e3035b177b7dae3c9f5fd567bb576a0f19c39f   specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md
    commit 2   eb6ac5c49231f968b59c980349c4a668455be3b1   reviews/chatgpt/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md
    commit 3   d133a813f3897fbbe8e56867400699f62fe4449a   the dossier + derivations/P2-DEFERRED-ITEMS.md

**The dossier and the deferred entry move together in commit 3**, as §8 of the
specification requires: `DEFERRED-04` records the disposition of a question the
dossier frames, and a commit carrying one without the other would be a partial
record. **MEASURED: commit 3 touches exactly those two paths.**

**Commit 4's message, INTENDED:**

    report: the kinetic-operator dossier, four ledgers and no selection

---

## 16. Did assembling the dossier make me want to select a candidate?

**Asked by §10, and the answer is yes. Naming which and why is the useful
part.**

**The pull was toward the overlap candidate**, and it arrived at a specific
moment: §4.4's derivation came out cleaner than the others. `H_W² ` collapses
to a scalar, the operator has a closed form, and the corner values are exactly
`0` or `2` with the species count an explicit function of `M_0`. **After
deriving a result that crisp it is tempting to read derivational tidiness as
physical merit**, and they are not the same thing. Tidiness of a free-field
calculation is a property of the algebra, not evidence about which theory the
programme should declare.

**A second, weaker pull was toward Wilson**, purely from continuity: it is the
form the exploratory kernel already uses, so choosing it would leave the
existing stored results standing. **§0's ruling is explicit that independent
physical and structural grounds are required**, and "the arithmetic we already
did stays valid" is a convenience, not such a ground. The specification says so
and §7 of this report states it as a consequence rather than an argument.

**A third pull was the most dangerous because it looks like rigour**: the
temptation to total the `COMPATIBLE` counts in §6.2 and treat six-of-sixteen
distributed unevenly as a ranking. **Four of the sixteen results are `NOT
ESTABLISHED` for the same reason for all four candidates** — line 184 depends
on the transfer matrix that line 181's obligation would supply — **so the
column carries no discriminating information at all**, and a naive total would
have converted a uniform silence into a spurious difference.

**I confirm I did not select, rank, recommend or prefer any candidate**, in the
dossier, in this report, or in any commit message. §12 gives the search and the
depth measurement. **The overlap section is the longest of the four at 77
lines, and the reason is that its convention-dependence needed stating; that
length is not an endorsement**, and I record the temptation here precisely so
the PI can discount my treatment of it if the length reads otherwise.

**I also did not freeze anything, did not run the exploratory script, did not
recompute or reinterpret the adopted parameter domain, did not modify
`GATES.md` or either lattice artifact, and did not answer `OPEN-AC-1`,
`OPEN-AC-3`, `C2`, `OPEN-CC-2` or `OPEN-CC-3`.**

---

## 17. Rule 16 assessment — what the assembled set does NOT establish

**Rule 16 is operative. All four junctions the specification names are
addressed.**

### 17.1 First junction — this unblocks neither `C-iii` nor `D0`

**This task does not unblock `C-iii`, and it does not unblock `D0`.** **A
dossier is not a freeze.**

**`C-iii` becomes evaluable when the PI rules and a freeze task lands.** This
task produces the material the ruling requires and stops before it; nothing
here selects an operator, so nothing here supplies the phase line with a
canonical microscopic action to consume.

**`D0` additionally requires `D-pre-B`'s Euclidean–spectral equivalence.**
**MEASURED, `P2-LATTICE-ONTOLOGY-01` lines 358–361:** "D-pre may be authorized
with this obligation open, but D0 may NOT be authorized until the kinetic
operator and its species ledger are frozen — a blocking deliverable of D-pre,
not a separate gate." **The ledger is derived here and frozen nowhere**, so
that blocking deliverable is not discharged.

**An earlier framing by the Researcher claimed `D-pre-A` would unblock the
phase line.** **It does not**, and the specification's §0 records why: measured
against the delegation table, almost every delegated item depends on the
operator choice, so there is no substantial choice-independent part to freeze.

### 17.2 Second junction — the dossier's completeness is bounded by this repository

**There is no literature here.** Every answer is either derived from the
committed material and explicit algebra performed and verified in this task, or
marked `NOT ESTABLISHED`.

**The count, MEASURED over the dossier:**

    DERIVED HERE          43 statements
      of which VERIFIED    8 against explicit matrix representations
    NOT ESTABLISHED       36 statements

    by criterion:
      A3 species ledgers      4 derived,  9 figures NOT ESTABLISHED
      A4 reflection positivity 0 established, 4 NOT ESTABLISHED
      A5 compatibility         6 COMPATIBLE, 0 INCONSISTENT, 10 NOT ESTABLISHED
      A7 species-to-N mapping  0 established, 4 NOT ESTABLISHED

**A dossier with gaps is the honest form of this deliverable, not a defective
one — provided the gaps are named.** **They are named at the point where each
arises**, not summarised away at the end, and each `NOT ESTABLISHED` carries
the reason it could not be established.

**The largest single block of gaps is reflection positivity**, where the answer
is `NOT ESTABLISHED` for all four candidates. **That is the criterion's
expected outcome for at least one candidate**, and it being the outcome for all
four is a fact about a repository containing no such construction, not a
failure to look.

### 17.3 Third junction — nothing establishes that four is the complete set

**`P2-LATTICE-ONTOLOGY-01` line 347 names four: naive, Wilson, staggered,
overlap.** **Nothing in this dossier establishes that they are the complete set
of formulations satisfying the frozen obligations.**

**Whether a fifth formulation exists that satisfies them is not addressed**,
and no search for one was performed. **The ruling that follows will therefore
be a choice among the four this dossier examined**, and the completeness of
that list rests on line 347 rather than on anything derived here.

### 17.4 Fourth junction — §9's connection changes a reading and no number

**If the connection holds, the `DEFERRED-02` branch is the doubler sector
rather than a curiosity.** **That is a reinterpretation conditional on a
candidate the programme has not adopted**, and §9.4 confines it to Wilson.

**`C1`'s and `C3`'s measurements are unaffected either way.** `C1` measured how
the production complement root is obtained; `C3` derived a closed form for the
curvature ratio and verified it over ninety pairs. **Neither measurement
depends on whether the branch is called a doubler sector**, and §9.3 states
that explicitly rather than leaving it to be inferred.

**The reinterpretation changes no number in the repository.** It changes what
"carries no independent content" means: from a bare absence of demonstrated
content to a mirror relation under an exact symmetry. **That is a change in
reading, and this task claims nothing more for it.**

---

## 18. Stops and clarifications

**No stop occurred.** All four checker invocations exited 0, RUN 2 passed at
both prospectivity readings, and no acceptance criterion failed.

    SPECIFICATION_DEFECT                          0 stops, 1 finding
    ENVIRONMENT                                   0 stops, 0 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 0 findings
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 2 findings

### 18.1 `SPECIFICATION_DEFECT` — one finding, not a stop

**§2(c) and A5 name four frozen items; the delegation table freezes five.**
Line 183, "Lattice: ontologically dynamical, operationally static", also reads
`FROZEN HERE`. §6.1 gives the measurement.

**Not a stop.** The criterion asks for sixteen results and I produced the
sixteen it names. **Line 183's own text describes it as an ontology obligation
constraining substrate variables still to be identified, so on the reading
available it distinguishes no candidate** and its omission changed no result.
**Reported rather than silently repaired**, because adding a fifth column would
have been answering a criterion other than the one written.

### 18.2 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — two findings

**First: line 182's isotropy freeze admits two readings and the staggered
candidate falls between them.** §6.3 gives it: the staggered phases have equal
coupling magnitudes on all four axes and a sign pattern that singles out an
axis ordering. **Whether "equal couplings on all four axes" means manifest axis
symmetry of the action or equality up to a field redefinition is not settled by
the text.** **Recorded as `NOT ESTABLISHED` rather than resolved**, because
resolving it in either direction would have produced a finding against or in
favour of a candidate on a reading I chose.

**Second: `P2-LATTICE-ONTOLOGY-01` line 356 asserts that species multiplicity
"enters `N`-accounting explicitly" and no line states how.** §8 gives the
measurement and enumerates three routes without choosing among them. **This is
the middle link the specification records the Reviewer as having identified**,
and the measurement confirms its absence rather than assuming it.

### 18.3 `OBSERVATION_METHOD_ERROR` — none this task, and why

**No probe of mine contradicted a committed check in this task.** The reason is
worth one sentence, given the previous two tasks: **every algebraic claim in
the dossier was verified against an explicit representation before being
written** — the Clifford property and chirality relation over all sixteen
corners, the staggered diagonalisation over all sixteen sites and four
directions, the overlap closed form and its corner values at five kernel
masses, and the involution identities at a random momentum.

**One near-miss is worth recording as a method note rather than an error.**
`DEFERRED-04`'s placement was decided by reading `check_p3` and finding that it
enforces `after.startswith(before)` — a **byte prefix**, not a subsequence.
**Had I placed the entry among the other entries, where it belongs
structurally, `P3` would have failed and the run would have been a retraction.**
§10.1 records this. **The check was consulted before the edit, not after.**

### 18.4 `ENVIRONMENT` and `REPOSITORY_DEFECT` — nothing to report

**No environment failure occurred.** **Rule 13 carries two diagnostic orders, a
known open item. Neither was exercised**, and I am not naming one as having
applied. **Nothing was installed.** Python 3.11.15 and pytest 9.1.1, as
present.

**No defect in the repository was found by this task.**

### 18.5 What I would have specified differently

**A4 says `NOT ESTABLISHED` "is expected for at least one candidate".** It came
back for all four. **The criterion anticipates a gap; it does not anticipate
that the gap is total**, and a reader meeting four identical answers may take
it as a failure to look rather than as the state of the repository. **I would
have had the criterion ask for the reason class per candidate** — absent from
the repository, asserted without derivation, or obstructed for a derived
structural reason — **which is what §5 reports anyway**, and which distinguishes
four answers that are otherwise identical strings.

**A5's sixteen results have the same shape.** Line 184 returns `NOT
ESTABLISHED` four times for one shared cause. **A criterion that asked which
results are independent would have surfaced that the column carries no
discriminating information**, which §16 records as the third temptation.

**Nothing in the specification was unsatisfiable, and nothing was ambiguous
enough to require a stop.** The one instruction that could have been misapplied
— "append only" on a file whose entries precede a closing section — resolved
cleanly once the enforcing code was read.

---

## 19. Evidence layering

**Committed in this report, MEASURED at commit 3:** A1–A13, A15 and A16 for
commits 1–3; A14's four invocations with both configs and both JSON outputs;
commits 1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; A11's final
base-to-commit-4 scope of 4 additions and 1 modification.

**Post-report evidence, returned to the Reviewer and NOT written back:** A11's
final scope measured base-to-commit-4; A14-final, being RUN 2 re-run at commit
4; A15 at commit 4; A16 for commit 4; the push; the branch tip read back.

**Nothing in this report claims to measure commit 4.**

**This task does not touch `main`.** The branch is the outcome; integration is
a separate task. **It freezes nothing and selects nothing.**
