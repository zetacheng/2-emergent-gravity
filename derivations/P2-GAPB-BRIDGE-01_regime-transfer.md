# `P2-GAPB-BRIDGE-01` — the regime transfer, attempted

    KIND        BOUNDED DERIVATION. Documentary and analytic.
                No new lattice measurement. No landing.
    ORIGIN      GAP-B of P2-PROJ-01-CLASS-01, under rule 22
    BASE        f23a0e1e1a24398d082a9597444ff9f750ed38e1

    OUTCOME     INDETERMINATE — UNDETERMINED BY READING

                Five mismatches identified. One is controlled with a stated
                reason; one is met; three are not determinable here. Two of
                those three require a DERIVATION, not a measurement, and are
                logically prior to the third, which requires one.

**No mismatch is shown to prevent `L2`'s conclusion from applying, and none is
shown to be absent or controlled except where stated. Neither `TRANSFER HOLDS`
nor `TRANSFER FAILS` is earned by this analysis.**

**Nothing here says the manuscript is wrong.** Every finding below is about
**reach** — which objects an argument as stated delivers its conclusion for —
and not about correctness.

---

## 0. A note on how the manuscript is quoted

**Manuscript quotations below are verbatim in their prose and RENDERED in their
mathematics.** `\emph{}` and `\textbf{}` markup is dropped, and inline math is
written in plain notation — `$\geq 6$` as `≥ 6`, `$(p/\Lambda)^2$` as
`(p/Λ)²`, `$\mathcal{O}(1)$` as `O(1)`. **The source wraps lines mid-sentence**,
so a quotation spanning a line break is joined. Every quotation below was
checked against the source with whitespace normalised and that markup stripped;
the prose bytes are unaltered. Where a quotation is elided, `…` marks the
elision.

---

## 1. `M1` — every condition `L2`'s argument states or requires

Read from `paper/emergent_gr_paper_v2_15.tex`, `\subsection{Spin-2 selection
and masslessness}` at `:770-788` together with the identity it invokes at
`:752-768` and the definition it is about at `:685-696`.

    L-1  THE OBJECT IS THE FERMION-INDUCED KERNEL.
         :685-696, eq:Gamma2 — "Integrating out the fermions defines the
         induced effective action", with
         Γ⁽²⁾_{μν,ρσ}(p) = (κ²/4)⟨T_{μν}(−p) T_{ρσ}(p)⟩_1PI + (seagull terms).

    L-2  THE DIFFEOMORPHISM INVARIANCE IS THAT OF THE FERMION SECTOR.
         :754-758 — "the continuum fermion measure and action are invariant;
         on the lattice this invariance is explicitly broken by the
         discretization."

    L-3  A SYMANZIK EFFECTIVE DESCRIPTION IN WHICH THE BREAKING IS dim ≥ 6.
         :759-761 — "In the Symanzik effective description, all such breaking
         is carried by local operators of dimension ≥ 6".

    L-4  THE APPROXIMATE WARD IDENTITY HOLDS.
         :762-767, eq:Ward —
         p_μ Γ⁽²⁾^{μν,ρσ}(p) = O(p²/Λ²) Γ⁽²⁾^{ν,ρσ}(p).

    L-5  UP TO LOCAL CONTACT TERMS THAT DO NOT PRODUCE PROPAGATING POLES.
         :768.

    L-6  THE TRACE IDENTITY, FOR THE IMPROVED STRESS TENSOR, UP TO CONTACT
         TERMS, REMOVES THE PROPAGATING SCALAR BLOCK.
         :775-777.

    L-7  THE DECOMPOSITION IS IN THE BARNES–RIVERS PROJECTOR BASIS.
         :772.

    L-8  THE CONCLUSION IS STATED FOR THE INFRARED KERNEL.
         :778 — "The infrared kernel is therefore", introducing eq:PiTT.
         Λ ~ 1/a, :75, :497, :717.

    L-9  THE SUPPRESSION IS RELATIVE TO THE TT BLOCK, BY (p/Λ)².
         :773-775 — "forces all longitudinal structures to be suppressed by
         (p/Λ)² relative to the transverse-traceless (TT) block";
         :779-786, eq:PiTT — Γ⁽²⁾ = Z_h p² P^TT + O(p⁴/Λ²) × (non-TT).

**Nine conditions. `L-1` and `L-2` are conditions on the object; `L-3` to `L-6`
on the argument's inputs; `L-7` on the basis; `L-8` and `L-9` on the regime and
the form of the claim.**

---

## 2. `M2` — `EXT-01`'s object, as the landed artifact describes it

    E-1  A LATTICE PROCA LOOP — A MASSIVE VECTOR FIELD.
         scripts/recovered_2026/proca_loop.py:2-3 — "Lattice Proca loop:
         universal m^2 log m^2 coefficient of a massive vector field coupled
         to a background metric."
         :5-9 — the Euclidean action, with forward differences
         D_μ f(x) = f(x+μ) − f(x), J2 = √g g⁻¹ ⊗ g⁻¹ and J = √g g⁻¹ exact,
         F_{μν} = D_μ A_ν − D_ν A_μ.
         :17 — "Loop sign: boson, Gamma = +(1/2) <ln det M>."

    E-2  MASS m = 0.3.
         derivations/P2-RECON-EXT-01_discarded-external-space.md:144.

    E-3  EXTENT n = 12, FINITE.
         …:143.

    E-4  q-GRID [0.10, 0.16, 0.22, 0.28].
         …:145.

    E-5  MOMENTUM DIRECTION q ∥ e₀.
         …:150.

    E-6  FIT FORM Π(q) = A + B q² + C q⁴; B IS THE REPORTED COEFFICIENT.
         …:146-147.

    E-7  DETERMINANT POWER k = 1, AND THE BUBBLE DOES NOT TAKE k.
         …:161-165.

    E-8  BASIS: THE TEN ORTHONORMAL COMPONENTS.
         …:151, and §1–§2.1 of the same artifact.

### 2.1 Two properties the pre-registered question names that the repository does not state

**MEASURED, and recorded because `M3` is three-valued and silence is not an
answer.** A repository-wide search for `unimproved` returns **zero** occurrences
in `EXT-01`'s artifact, its report, its diagnostic script, or `proca_loop.py`.
Every occurrence is in `PROJ-01`'s adjudication and downstream of it. A search
for a stated lattice spacing in `EXT-01`'s artifact and report likewise returns
nothing.

**So "a = 1, unimproved" is `PROJ-01`'s characterisation of the object, not a
property `EXT-01` states.** Both are nonetheless settled below by reading the
action rather than by taking the characterisation on trust — see `D1`.

---

## 3. `M3` — for each `M1` condition, what the repository states about `EXT-01`'s object

**Three-valued. Silence is recorded as silence and is not collapsed into
either answer.**

    L-1  object is the fermion-induced kernel
         STATES THAT IT DOES NOT. proca_loop.py:2-3 states a massive vector
         field; :17 states a boson loop sign. The object is not a fermion
         determinant, and the repository says so directly.

    L-2  the invariance is the fermion sector's
         STATES NOTHING. No repository location states a diffeomorphism
         Ward identity for the lattice Proca action, in either direction.

    L-3  Symanzik dim ≥ 6 breaking
         STATES NOTHING for this object.

    L-4  the approximate Ward identity holds
         STATES NOTHING for this object. The manuscript's :1057-1059 records
         a lattice Ward identity check for the PHOTON sector — q̂_μ Π^{μν} = 0
         to 2×10⁻¹⁴ — which is a different identity (gauge, not
         diffeomorphism) on a different kernel, and is not a statement about
         this object.

    L-5  up to contact terms with no propagating poles
         STATES THAT IT IS SATISFIED, in effect: mlog_coeff.py:10-11 —
         "seagull and CC are q^0 / q-independent and drop from the slope".

    L-6  trace identity for the IMPROVED stress tensor
         STATES NOTHING. No improvement statement exists for this object;
         §2.1 records the silence.

    L-7  Barnes–Rivers basis
         STATES THAT IT IS SATISFIED, for q ∥ e₀ and by derivation rather
         than by assertion: derivations/P2-GAPA-BRIDGE-01_basis-identification.md
         establishes that for q ∥ e₀ the Barnes–Rivers TT block is the span
         of TT_RECIPES and the non-TT blocks are the five discarded
         components, 1+3+1. **That result carries its momentum condition and
         is not promoted here to a covariant identity.**

    L-8  infrared regime
         STATES THE PARAMETERS but not the comparison: E-4's q-grid and
         Λ ~ 1/a are each stated; whether q ≪ Λ holds is arithmetic, done
         under D1.

    L-9  suppression relative to the TT block
         STATES NOTHING about whether the measured object exhibits it. What
         EXT-01 records is a measurement, not a statement about L2's reach.

**Two conditions the repository affirms, one it denies, six on which it is
silent.**

---

## 4. `M4` — conditions the manuscript or repository states under which `L2`'s conclusion would fail, weaken, or not apply

**NOT SILENCE. The manuscript states several, in the same section that builds
the lattice kernel.**

**`:818-819`** — "Up to $\mathcal{O}(p^2/\Lambda^2)$ corrections, the quadratic
action defined by Eq.~\eqref{eq:PiTT} is the Fierz--Pauli action". The
conclusion is carried only to that accuracy.

**`:805-809`** — "that the interacting lattice theory possesses a genuine
massless spin-2 *pole* in $\langle TT \rangle$ … is supported by the Ward
structure above but is ultimately a nonperturbative question."

**Finding 1, `:1067-1084`** — "two continuum expectations fail at
$\mathcal{O}(1)$: the $q\to0$ kernel does not equal the covariant
cosmological-constant structure … and **the subtracted kernel is not
transverse**. The lattice therefore induces genuinely *non-covariant* local
terms at cutoff order"; and "**covariance of the infrared effective action must
be restored by local counterterms**, which include … a transverse-traceless
$q^0$ subtraction (a graviton mass counterterm) and non-covariant
$\mathcal{O}(q^2)$ structures."

**Finding 2, `:1088-1098`** — "At $\mathcal{O}(q^2)$ the transverse-traceless
projection of the kernel receives contributions from the covariant structure
and from several $H(4)$-invariant non-covariant local structures", with "the
positive bubble-only axis slope traced entirely to the non-covariant piece";
and `:1099-1107`, an "exact null space of the orientation-weight matrix, with a
large component along the covariant direction … The covariant kinetic
coefficient is therefore *not identifiable* from transverse-traceless data".

**`:733-739`** — "transverse-traceless data alone cannot separate the covariant
kinetic coefficient from non-covariant counterterm structures: at quadratic
order in the cutoff, $c_2$ is part of the definition of the model rather than a
derived quantity".

**These are the manuscript's own statements about where its lattice kernel
departs from the continuum expectations `L2` reasons from.** They are recorded
as found. **None of them says `L2` is wrong**; they bound the objects and the
orders at which its conclusion is claimed.

---

## 5. `M5` and `M6` — the states this task must not alter

    Q1          INCONCLUSIVE, reason UNDETERMINED BY READING
                subclass INCONCLUSIVE — CONSTRUCTIVE GAP IDENTIFIED
                derivations/P2-PROJ-01-CLASS-01_q1-classification.md:11-12
    GAP-A       IDENTIFICATION HOLDS, for q ∥ e₀ and at no other direction
                tested
                derivations/P2-GAPA-BRIDGE-01_basis-identification.md:7, §7
    H-EXT-01    UNESTABLISHED — NOT ASSUMED BY RECON-01b
                assumptions/H-EXT-01.md:14

    A-EXT-01  Statement SHA  ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
    H-EXT-01  Statement SHA  e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47

**This task alters none of them.**

---

## 6. `D1` and `D2` — the analysis, condition by condition, and each mismatch classified

### `MM-1` — SPECIES. `L-1`, `L-2`. Classification: **(iv), not determinable here**

**The mismatch.** `L2`'s object is the kernel obtained by integrating out
**fermions**, and the Ward identity it rests on is the diffeomorphism
invariance of the **fermion** measure and action. `EXT-01`'s object is a
**massive vector** loop, a boson determinant.

**Why not (i).** The repository states the difference; it is not an artefact of
description.

**Why not (ii).** For the mismatch to be irrelevant to the `q²` conclusion, the
Ward and trace structure `L2` uses would have to hold for the vector species.
**The manuscript extends its machinery to one other species and to one other
purpose:** `:1116-1122` applies it to "the condensate (boson) sector---a lattice
scalar" and reports that the boson loop "is subject to the identical
degeneracy" — a statement about **Finding 2's degeneracy**, not about `eq:Ward`
or `eq:PiTT`, and about a **scalar**, not a vector.

**Why not (iii).** A controlling relation would be a Ward identity for the
lattice Proca action of `proca_loop.py:5-9`, with its diffeomorphism breaking
shown to be carried by dimension ≥ 6 operators in the Symanzik sense. **No such
derivation exists in the repository, and this task does not supply one.**
Supplying it would be the construction `D4` and `C9` exist to prevent being
invented to remove a mismatch.

**What would settle it.** A reviewed derivation of the diffeomorphism Ward
identity for this lattice Proca discretisation, with its Symanzik counting.
**A measurement would not settle it** — it is a question about which argument
applies, not about a value.

**Recorded, because the pre-registered question did not name it.** `GAP-B`'s
establishing direction names the regime, the spacing, the mass, the extent and
the improvement. **It does not name the species.** This is not a re-opening of
`GAP-B`'s wording; it is a mismatch found by executing `M1` and `M2` as
specified.

### `MM-2` — REGIME. `L-8`, `L-9`. Classification: **(i), the condition is met**

**Arithmetic on stated parameters only. No measured value is used.** `Λ ~ 1/a`
(`:75`, `:497`, `:717`), and `a = 1` for this object — settled by reading, not
by taking `PROJ-01`'s word: `proca_loop.py:5` defines
`D_μ f(x) = f(x+μ) − f(x)` with unit shift, and the diagnostic's momentum grid
runs over the Brillouin zone `[−π, π)`, so lengths are in units of the spacing.

    q       q·a      (q·a)²
    0.10    0.100    0.0100
    0.16    0.160    0.0256
    0.22    0.220    0.0484
    0.28    0.280    0.0784

**`q ≪ Λ` holds across the grid**, with the relative correction `L-9` predicts
running from `1.0%` to `7.8%`. **The condition `L2` states is met.**

**One ratio recorded because a reader will ask for it, and it is not a
condition `L2` states.** With `m = 0.3`, `q/m` runs `0.333` to `0.933`, so the
measurement is **not** in a `q ≪ m` regime. **`L2` states no such condition:**
its "infrared" is the external kernel's regime relative to `Λ`, while
`:1133-1134`'s "infrared ($k \sim m$) region of the loop" is a statement about
the **loop** momentum in a different argument. **The two are not the same
regime and are not conflated here.**

### `MM-3` — IMPROVEMENT. `L-6`. Classification: **(iv), and a measurement would bear on it**

**The mismatch.** `L-6` invokes the trace identity **for the improved stress
tensor**. `M3` records that the repository states nothing about improvement for
this object. **Settled here by reading the action:** `proca_loop.py:5-9` is a
minimal forward-difference discretisation with the exact geometric factors and
**no Symanzik improvement term of any kind** — no clover, no `O(a)` or `O(a²)`
counterterm, no improved operator. The object is unimproved.

**Why not (ii).** The trace identity's function in `L2` is to **remove the
propagating scalar block**. `EXT-01`'s discarded set contains exactly the
components that block would govern: `D5`, the spatial trace, and `D1`, `h00` —
and `GAP-A` established that these are the `P0s` and `P0w` blocks respectively.
**A mismatch in the identity that removes the scalar block cannot be irrelevant
to two of the five components at issue**, and calling it irrelevant without a
reason is the failure mode this taxonomy is written to expose.

**Why not (iii).** A controlling relation would be an analytic statement
relating the improved and unimproved trace identities at `O(q²)` for this
discretisation. Not in the repository, and not constructed here.

**What would bear on it, specified and NOT performed.** A lattice measurement:
evaluate the same ten-component decomposition **at two or more lattice
spacings** at fixed physical `m` and `q` — that is, vary `a` with `m a` and
`q a` scaled together — and observe whether the discarded group's `q²`
coefficients approach zero relative to the retained group as `a → 0`. **What
would decide each way:** a discarded-to-retained ratio falling like `a²` toward
zero would show the mismatch is a lattice artefact that the continuum limit
removes; a ratio approaching a non-zero constant would show it is not. **`K4`
forbids running it and it was not run.**

**But see `§7`: this measurement would not settle transfer on its own**, because
`MM-1` and `MM-5` are prior to it and are not measurement questions.

### `MM-4` — CONTACT TERMS. `L-5`, and the "up to contact terms" of `L-6`. Classification: **(ii), present and provably irrelevant to the `q²` conclusion**

**The reason, not merely the verdict, and from two independent stated grounds.**

**The manuscript, `:1046-1049`:** "Because the coefficients are local in $h(x)$,
the seagull tadpole $T$ carries no net momentum through any link and is
*exactly* $q$-independent: contact terms shift the momentum-independent part of
the kernel but not its $q^2$ slope."

**The repository, `scripts/recovered_2026/mlog_coeff.py:10-11`**, for the family
of objects `EXT-01`'s bubble belongs to: "bubble-only axis-TT slope (seagull and
CC are q^0 / q-independent and drop from the slope)".

**And the observable isolates it.** `EXT-01` reports `B`, the `q²` coefficient
of `Π(q) = A + B q² + C q⁴` (`E-6`). **A `q`-independent contact term
contributes to `A` and to nothing else.**

**This is the one mismatch that is controlled**, and it is controlled because
the quantity reported is a slope and the mismatch is an intercept.

### `MM-5` — THE KERNEL'S COVARIANCE STATE. `L-4`, `L-8`. Classification: **(iv), not determinable here**

**The mismatch.** `eq:PiTT` is stated for **the infrared kernel** — and the
manuscript states, at `:1080-1084`, that "covariance of the infrared effective
action **must be restored by local counterterms**", which "include … non-covariant
$\mathcal{O}(q^2)$ structures". `EXT-01`'s object is the **bare finite-spacing
kernel**, before any such restoration: no counterterm subtraction appears in its
pre-registration or in `scripts/diagnostics/ext01_discarded_external_space.py`.

**So `L2`'s conclusion and `EXT-01`'s object are separated by the counterterm
restoration the manuscript says is required**, and the manuscript states at
`:1067-1072` that the pre-restoration lattice kernel fails transversality at
`O(1)` — which is `L-4`'s premise, at an order that `eq:Ward`'s
`O(p²/Λ²)` does not cover.

**Why this is NOT `TRANSFER FAILS`.** For that, a mismatch must be shown to
**prevent** the conclusion from applying. Finding 2 establishes an **exact null
space** making the covariant coefficient **not identifiable from TT data** —
that is an obstruction to *determining* the covariant piece, and it is a
demonstrated impossibility result. **But it is not a demonstration that `L2`'s
conclusion is false of the restored kernel**, and turning "cannot be determined"
into "does not hold" is precisely the invalid conversion `§5` forbids.

**Why this is not (iii).** Controlling it would require the counterterms, and
the manuscript states the covariant part is not identifiable from the data that
would fix them.

**What would settle it.** A construction: a specification of the
covariance-restoring counterterms for this discretisation, sufficient to state
the restored kernel's non-TT content. **`:1099-1107` is evidence that the
obvious route to it — fitting from TT data — cannot supply it.**

### Every `M1` condition is covered

    L-1  MM-1     L-2  MM-1     L-3  MM-1 (the same construction)
    L-4  MM-5     L-5  MM-4     L-6  MM-3
    L-7  MET, by GAP-A, for q ∥ e₀ and not beyond
    L-8  MM-2 (met) and MM-5 (not determinable)
    L-9  MM-2, met as a condition; its consequence is §7

---

## 7. `D3` — the standing of `EXT-01`'s numbers, given the above

**`EXT-01`'s values are not re-analysed. They appear as recorded.**

**Transfer is not established in either direction, so `EXT-01`'s measurement is
neither a measurement of a regime `L2` reaches nor one it fails to reach.** Its
standing is exactly what it was before this analysis: **a measurement of the
bare finite-spacing Proca kernel's ten-component `q²` decomposition at
`q ∥ e₀`**, whose relation to `L2`'s conclusion is undetermined.

**What it does bear on**, unchanged by this task: the magnitudes of the
discarded components of the axis-TT projection, in the object the `RECON` line
measures, at the pre-registered parameters.

**What it does not bear on:** whether `L2`'s conclusion is true. It is a
measurement of a different object than `L2`'s, related to it by a bridge this
task did not cross.

### 7.1 `D4` — an apparent conflict, recorded and not resolved

**Recorded after the classification above and not used to reach it.**

`EXT-01` records `|sum discarded| / |sum retained| = 0.297300` at `:206`, and
records that `D1` alone is `1.008193` times the mean retained component at
`:207`.

**If `eq:PiTT` applied to this object**, `L-9` would place the non-TT content at
`O((q·a)²)` relative to the TT block — from `MM-2`'s table, **at most `0.0784`
at the top of the grid**, and `0.0100` at the bottom.

    recorded ratio                                    0.297300
    the largest relative suppression L-9 would allow  0.0784   at q = 0.28

**These are recorded side by side, both as stated, and neither is adjusted.**

**No mechanism that would remove the discrepancy is proposed here**, and none
should be read into the placement of the two numbers together. **The comparison
is not evidence that `L2` is wrong** — `L2`'s conclusion is about the
covariance-restored infrared kernel of a fermion determinant, and the recorded
ratio is from the bare finite-spacing kernel of a Proca determinant.
**`MM-1`, `MM-3` and `MM-5` are exactly the reasons the two numbers cannot yet
be compared as though they were about one object.**

---

## 8. Outcome

    INDETERMINATE — UNDETERMINED BY READING

**Which conditions, and what would settle each:**

    MM-1  species        a reviewed derivation of the diffeomorphism Ward
                         identity for this lattice Proca discretisation, with
                         its Symanzik counting. NOT a measurement.
    MM-5  covariance     a specification of the covariance-restoring
          state         counterterms sufficient to state the restored kernel's
                         non-TT content. NOT a measurement, and :1099-1107 is
                         evidence that the obvious route cannot supply it.
    MM-3  improvement    a two-or-more-spacing lattice measurement, specified
                         at MM-3 and NOT performed. THIS ONE IS A MEASUREMENT.

**Why the outcome is `UNDETERMINED BY READING` and not `MEASUREMENT
REQUIRED`.** `§5` reserves `MEASUREMENT REQUIRED` for a mismatch whose status
"cannot be settled without a lattice measurement". **`MM-1` and `MM-5` are
logically prior to `MM-3` and are not measurement questions.** Until the species
bridge exists, a continuum-limit study of the Proca object would report the
continuum behaviour of the Proca object — **it would not establish whether
`L2`'s fermion-sector conclusion transfers to it.**

**Stated plainly, because a PI decision may turn on it: the measurement a
reader would reach for first would not, on its own, settle `GAP-B`.** The
measurement is specified at `MM-3` so that it can be commissioned if it is
wanted for its own sake, and so that the decision is made with its limits
visible.

**Neither `TRANSFER HOLDS` nor `TRANSFER FAILS` is earned.** `TRANSFER HOLDS`
would require every mismatch in `(i)`–`(iii)`; three are in `(iv)`.
`TRANSFER FAILS` would require at least one shown to **prevent** the conclusion
from applying; **the strongest candidate, `MM-5`, establishes non-identifiability,
which is not the same thing.**

---

## 9. What this does not establish

**`Q1` is unchanged.** `INCONCLUSIVE`, reason `UNDETERMINED BY READING`, with
its subclass and `Resolution path` intact. **`GAP-B` is not closed by this
result** — it is bounded, and its three unresolved mismatches are named.

**`GAP-A` is unchanged and is not re-opened.** Its result is used at `L-7`
strictly within its momentum condition and is not promoted to a covariant
identity.

**`H-EXT-01` remains `UNESTABLISHED` and `NOT ASSUMED BY RECON-01b`.**

**`A-EXT-01` is unchanged and remains a definitional convention.**

**Nothing here says the manuscript is wrong.** Every mismatch above is a
statement about **which objects `L2` as stated delivers its conclusion for**.
An argument that does not reach an object is not an argument that is false.

**No number of the programme's kind was produced.** No `β_V`, no `β_B`, no
ratio of them, no `k`-scan, no lattice evaluation of any kind. No gate moves and
`P2-PHASE-01` does not advance.

**No new lattice measurement was run**, no spacing was varied, no improved
operator was evaluated, and no continuum extrapolation was performed.
