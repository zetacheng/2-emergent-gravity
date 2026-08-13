# `P2-PHASE-01` `OPEN-AC-4` — exact and remnant symmetry, and whether `C-i` reads plainly

## Kind labels used in this document

**Every label used anywhere below is defined here, and no other label is
used.**

    FINDINGS                 this document's kind. It records determinations
                             reached by the executor from the material named
                             in §1 of the specification. It binds no gate, it
                             changes no verdict, and it closes nothing. What
                             it may be used for is fixed by the task that
                             adopts it, not by this document.

    CONFIRMED                the claim checked is supported by the lines cited.
    REFUTED                  the claim checked is contradicted by the lines cited.
                             Defined for completeness of the three-valued
                             scale; no finding in this document carries it.
    CANNOT DETERMINE         the material named does not settle the claim
                             either way.

    EXACT                    the transformation leaves the object named
                             invariant, shown from the lines cited.
    EXPLICITLY BROKEN        a term in the object named is not invariant
                             under the transformation, shown from the lines
                             cited, and the breaking is by an explicit term
                             rather than by the state.
    NOT DECLARED             the object actually coded carries no
                             representation of the transformation, so its
                             status is not a property of what was computed.

    A-NO-EXACT-CONTINUOUS-BREAKING   §3 of the specification defines it.
    B-NOT-CLOSABLE                   §3 of the specification defines it.

---

## 1. Verdict A

**`A-NO-EXACT-CONTINUOUS-BREAKING`: for a uniform flavour-singlet scalar
condensate under the exploratory Wilson-form kernel at lines 46–90 of
`scripts/p2_phase01_scalar_exploratory.py`, no exact continuous symmetry
is broken.**

**That candidate class and that kernel are the whole of this verdict's
scope.** It is not a statement about non-singlet condensates, about
non-scalar channels, or about the frozen microscopic action — the
canonical lattice Dirac operator is not frozen, which is §2's subject.
**Whether `OPEN-AC-4` closes is not this verdict's question**; it is
verdict B's, and verdict B answers it in the negative.

### Consequence, transcribed from §3 of the specification

> **Consequence:** **for the singlet-scalar candidate class under the
> Wilson-form exploratory kernel, `C-i` would read PLAINLY** — full
> positive definiteness, no transverse qualification, because the flat-
> direction set is empty **for that class and that kernel**. **The
> transverse clause is NOT dead text**: a non-singlet `λ^A` condensate
> would break the exact `U(N)_V`, and a different kinetic operator would
> change the exact symmetries entirely. **Any statement of this consequence
> that omits the candidate class or the kernel is a misstatement of it.**

---

## 2. Verdict B

**`B-NOT-CLOSABLE`: the canonical lattice Dirac operator is not frozen,
so verdict A holds only for the exploratory kernel.**

The repository records the operator as undelivered in four places, quoted
here as literal lines:

    P2-LATTICE-ROUTE-01.md, lines 189-190
      *Freeze:* microscopic variables and measure; the canonical lattice Dirac
      operator; the species ledger and doubling treatment; the

    P2-LATTICE-ROUTE-01.md, line 322
      | `P2-LATTICE-MICROSPEC-01` (D-pre) | not created | D0 |

    P2-LATTICE-ONTOLOGY-01.md, line 189
      | Canonical kinetic operator and species accounting | DELEGATED: D-pre (§4 obligation binds it) |

    P2-LATTICE-ROUTE-01.md, lines 138-139
      - Wilson / staggered / overlap are *different microscopic models*, not
        interchangeable regulators;

**The first and fourth are quoted at their source line breaks and so carry
their neighbouring clauses; the sentence continues past the fragment shown
in both cases.**

`derivations/P2-LATTICE-ONTOLOGY-01.md` lines 347–349 add that the choice
among naive / Wilson / staggered / overlap kinetic terms **is a choice of
the theory's matter content**.

`C-iii`, at lines 78–83 of
`derivations/P2-PHASE-01_input_admissibility_contract.md`, asks for the
exact and remnant symmetries **of the frozen microscopic action**. There is
no frozen microscopic Dirac operator to take them from.

### Consequence, transcribed from §3 of the specification

> **Consequence:** **`OPEN-AC-4` REMAINS OPEN and this task does not close
> it.** **`C-iii` cannot be evaluated, and therefore standard C cannot be
> completed, until `D-pre` freezes the canonical lattice Dirac operator.**
> **Verdict A is recorded as a conditional result: "if the canonical
> operator is Wilson-form, then …".** **State plainly that the science
> line's blocker moves from `OPEN-AC-4` to `D-pre`
> (`P2-LATTICE-MICROSPEC-01`, recorded as "not created")**, and **do not
> recommend anything about it** — the next step is a PI decision, not this
> task's.

**Stated, not recommended:** the science line's blocker moves from
`OPEN-AC-4` to `D-pre` (`P2-LATTICE-MICROSPEC-01`, recorded as "not
created"). **This document recommends nothing about `D-pre`.**

---

## 3. The symmetry inventory

**For the regularised theory actually computed, not the continuum
Lagrangian.**

### 3.0 What object the inventory is over, and why the distinction is load-bearing

**The exploratory script does not code a fermion action.** It codes one
scalar function of one real parameter: the momentum-space denominator of a
Wilson propagator, summed over a Brillouin-zone grid.
`WilsonQuadrature.bubble_and_derivative`, lines 72–87, builds

    s           = self._s3 + self._sin2[index]              line 80
    w           = mhat + self._w3 + self._omc[index]        line 81
    denominator = s + w * w                                 line 82

from `_sin2 = np.sin(axis) ** 2` (line 59) and `_omc = 1.0 - np.cos(axis)`
(line 60), with `_s3` and `_w3` the three-axis sums at lines 61–70.

**There is no flavour index, no Dirac index and no gauge field anywhere in
lines 46–90.** The inventory below therefore splits into two parts that
must not be merged: what is a property of the coded kernel, and what is a
property of the Wilson Dirac operator that the coded kernel is the
denominator of but which the script does not itself instantiate. **Where
the second is used, this document says so.**

### 3.1 Continuous internal symmetries

| Symmetry | Status | Lines it rests on |
|---|---|---|
| `U(N)_V` — vector flavour rotations, including `U(1)_B` | **EXACT** | Freeze §2, lines 36–39, gives the interaction as `(G/2N) Σ_{A=0}^{N²−1} [S^A(x)² + P^A(x)²]`. Both sums run over the complete generator set with the normalisation `Tr[λ^A λ^B] = 2δ^{AB}` recorded at freeze line 23, so each is the quadratic Casimir contraction and is invariant under `S^A → R^{AB}S^B` for `R` in the adjoint of `U(N)_V`. The kinetic term at freeze line 36 carries no flavour structure, and neither does the coded kernel (script lines 46–90, no flavour index). Nothing in `s + w²` distinguishes flavours. |
| `SU(N)_A` — non-singlet axial rotations | **EXPLICITLY BROKEN**, by the Wilson term | Script line 81 places `self._w3 + self._omc[index]`, i.e. `Σ_μ (1 − cos p_μ)`, **inside the mass slot `w` alongside `mhat`**. In the Dirac-matrix structure of the Wilson operator the mass slot multiplies the identity in Dirac space, so this addition anticommutes with `γ5` in the same way an explicit mass does. §3.2 gives the argument in full. |
| `U(1)_A` — singlet axial rotation | **EXPLICITLY BROKEN**, by the Wilson term; and separately excluded from the frozen interaction | Same lines as `SU(N)_A`. Independently, freeze lines 45–47 record that *"the anomalous breaking of the axial `U(1)_A` is **not** part of this canonical interaction and is governed by its own records"* — so `U(1)_A` is not an exact symmetry of the frozen theory even before the regulator is introduced. |
| Any further exact continuous symmetry | **NOT DECLARED** — see §5.2 | No further continuous invariance of `s + w²` beyond the flavour rotations above was identified. §5.2 states what that does and does not establish. |

### 3.2 Why the Wilson term breaks the axials, stated from the code

The continuum kinetic operator at freeze line 36 is `iγ^μ ∂_μ`, which
anticommutes with `γ5`; that anticommutation is what makes the axial
rotations symmetries of the massless continuum theory. The lattice
operator whose denominator the script codes has momentum-space form

    D(p) = i Σ_μ γ_μ sin(p_μ)  +  [ Mhat + Σ_μ (1 − cos p_μ) ]

read directly off script lines 80–82: `s = Σ_μ sin²(p_μ)` is the square of
the `γ`-odd part, and `w = Mhat + Σ_μ (1 − cos p_μ)` is the entire `γ`-even
part, since `denominator = s + w*w` is exactly `D†D` for that operator with
`r = 1`. **The Wilson term therefore occupies the same Dirac slot as the
mass, and carries the identity in Dirac space.** A term proportional to the
Dirac identity commutes with `γ5` rather than anticommuting with it, so it
is not invariant under `ψ → e^{iαγ5}ψ`: the axial rotations are broken by an
explicit term in the operator, not by the state.

**This is explicit breaking, not spontaneous breaking**, and the
distinction is what makes it relevant here: an explicitly broken symmetry
produces no exact Goldstone directions, because it is not a symmetry of the
action that the state could break.

The standard Wilson operator also does not satisfy the Ginsparg-Wilson
relation, and therefore does not possess the corresponding exact lattice
chiral symmetry at finite lattice spacing. **The material named in §1 of
the specification does not itself state the Ginsparg-Wilson relation**; that
step is standard lattice theory supplied by the executor, and it is flagged
as such in §5.2 rather than presented as a repository fact.

### 3.3 Spacetime symmetries

| Symmetry | Status | Lines it rests on |
|---|---|---|
| `H(4)` — the finite hypercubic group | **EXACT for the coded kernel** | The kernel is built from per-axis arrays `_sin2` and `_omc` (script lines 59–60) combined by symmetric three-axis sums `_s3`, `_w3` (lines 61–70) plus the fourth axis at lines 80–81. The construction is invariant under permutation of the four axes by inspection. Both `sin²(p)` and `1 − cos(p)` are even functions, so the kernel is separately invariant under `p_μ → −p_μ` on each axis. Axis permutations and per-axis reflections generate `H(4)`. |
| Continuous `O(4)` / Lorentz | **NOT an exact symmetry of the lattice**; emergent and contingent | `derivations/P2-LATTICE-ONTOLOGY-01.md` lines 114–115: *"the H(4) symmetry group is the finite hypercubic group, not continuous O(4)"*. Lines 119–125 make `O(4)` a *"mechanism to be demonstrated for the declared fermion operator — H(4) symmetry alone does not guarantee"* it. |
| Lattice translations | **EXACT for the coded kernel** | The kernel is a function of momentum only (script lines 80–82) and is evaluated on a fixed Brillouin-zone grid; there is no position-dependent structure anywhere in lines 46–90. |

### 3.4 Discrete symmetries

| Symmetry | Status | Lines it rests on |
|---|---|---|
| Per-axis reflection `p_μ → −p_μ` | **EXACT for the coded kernel** | Script lines 59–60: `sin²` and `1 − cos` are both even. Included here as well as in §3.3 because it is the generator the code exhibits most directly. |
| `p_μ → π − p_μ` on all four axes | **EXACT as a relation between mass arguments**, not as an invariance at fixed `Mhat` | Script lines 325–327 record *"I0(Mhat) = I0(-8 - Mhat), from p_mu -> pi-p_mu"*, checked numerically at lines 310–317. `Σ_μ (1 − cos p_μ) = 8` when every `p_μ = π`, which is where the shift `−8` comes from. This maps the kernel at `Mhat` onto the kernel at `−8 − Mhat`; it is not an invariance of the kernel at a single `Mhat`. |
| `Mhat → −Mhat` | **EXPLICITLY BROKEN** | Script lines 320–322: *"not a symmetry: the frozen Wilson integral differs at every tested nonzero mass"*, with the supporting pairs at lines 298–308. |
| Parity, charge conjugation, time reversal | **NOT DECLARED** | The coded kernel has no Dirac or flavour representation (script lines 46–90), so it carries no representation of `P`, `C` or `T`. `derivations/P2-LATTICE-ONTOLOGY-01.md` line 153 records charge conjugation as *"mapping `Q → −Q`"* in defining the neutral sector, but does not declare the discrete symmetries of a kinetic operator, because line 189 delegates that operator to `D-pre`. |

---

## 4. Is the scalar condensate an order parameter for any of them?

**Stated per symmetry.** The candidate is the uniform flavour-singlet
scalar condensate: a single real `Mhat` entering the mass slot at script
line 81, with no flavour index anywhere in lines 46–90 and no position
dependence. **A flavour-independent shift of the mass slot is by
construction a flavour singlet**, which is why the candidate class is
described that way; the script states the uniformity at lines 3–4 (*"It
evaluates only the uniform scalar ansatz"*) and at line 437 (*"restricted
to a uniform scalar ansatz at mu=0"*).

| Symmetry | Order parameter? |
|---|---|
| `U(N)_V` (incl. `U(1)_B`) | **No.** A flavour-singlet condensate is invariant under `U(N)_V` — it transforms in the trivial representation. `U(N)_V` is EXACT and the candidate does not break it. **This is the entry that carries verdict A.** |
| `SU(N)_A` | **Yes in form, but the symmetry is already EXPLICITLY BROKEN** by the Wilson term (§3.2), so no exact symmetry is broken by the state and no exact Goldstone direction follows. |
| `U(1)_A` | **Yes in form**, same disposition as `SU(N)_A`, and additionally excluded from the canonical interaction at freeze lines 45–47. |
| `H(4)`, lattice translations | **No.** A uniform scalar is a scalar under axis permutations and per-axis reflections, and is position-independent. It transforms trivially. |
| Continuous `O(4)` / Lorentz | **Not applicable as an exact symmetry** — it is not one (§3.3). A uniform scalar would in any case be an `O(4)` scalar. |
| `Mhat → −Mhat` | **Not applicable** — this is a map on the parameter, not a symmetry of the kernel (§3.4), so there is nothing for the condensate to be an order parameter for. |
| `P`, `C`, `T` | **CANNOT DETERMINE from the coded kernel**, which carries no representation of them (§3.4). A uniform flavour-singlet scalar is even under `P` and `C` in the standard continuum assignment, but the operator whose `P` and `C` these would be is not frozen. |

---

## 5. The flat-direction count

**Zero, for the uniform flavour-singlet scalar candidate class under the
exploratory Wilson-form kernel at script lines 46–90.**

### 5.1 The justification

Exact Goldstone directions require a **continuous** symmetry of the action
that the state breaks. Taking the two conditions in turn against §§3–4:

1. **The exact continuous symmetries are the flavour rotations `U(N)_V`,
   including `U(1)_B`** (§3.1). The candidate is a flavour singlet and
   transforms trivially under them (§4). **Not broken by the state, so no
   flat directions from this source.**
2. **The axial rotations `SU(N)_A` and `U(1)_A` are continuous and would be
   broken by the candidate, but they are not symmetries of the regularised
   object at all** — the Wilson term breaks them explicitly (§3.2). **An
   explicitly broken symmetry contributes no exact flat direction**, because
   the degeneracy that would produce one is lifted by the term in the
   action, not merely by the state.
3. **The exact spacetime symmetry of the lattice is `H(4)`, a *finite*
   group** (§3.3, ontology lines 114–115). **A finite group has no
   continuous generators**, so breaking it cannot produce a flat direction —
   and the candidate does not break it in any case, being a scalar under it.
   **This is a structural exclusion, not an empirical one:** it does not
   depend on the candidate, and it would hold for any candidate whatever.
   `O(4)`, which does have continuous generators, is emergent and contingent
   at this level (ontology lines 119–125) and is therefore not available as
   a source of exact flat directions.
4. **The remaining exact symmetries in the inventory are discrete** (§3.4).
   Discrete breaking produces degenerate vacua, not flat directions.

The union of the sources is empty, so the flat-direction set is empty and
the count is zero.

### 5.2 What the count does not establish

**A zero count is not a proof that the exact continuous symmetry group is
exhausted by `U(N)_V`.** §3.1's last row records `NOT DECLARED` rather than
a negative result: the executor identified no further continuous invariance
of `s + w²`, and **an exhaustive search over all possible continuous
invariances was not performed and is not offered.** The kernel is a
one-parameter scalar function, so a continuous invariance acting on fields
the code does not represent would not be visible in it at all. **The honest
statement is that none was found in the material named, not that none
exists.**

The Ginsparg-Wilson step in §3.2 is standard lattice theory supplied by the
executor and is **not** stated in any file named in §1 of the specification.
It is recorded here so a reader can see which part of the argument rests on
the repository and which does not.

---

## 6. How `C-i` would be read for the candidate class examined

**Transcribed verbatim from §3 of the specification, for verdict
`A-NO-EXACT-CONTINUOUS-BREAKING`:**

> **Consequence:** **for the singlet-scalar candidate class under the
> Wilson-form exploratory kernel, `C-i` would read PLAINLY** — full
> positive definiteness, no transverse qualification, because the flat-
> direction set is empty **for that class and that kernel**. **The
> transverse clause is NOT dead text**: a non-singlet `λ^A` condensate
> would break the exact `U(N)_V`, and a different kinetic operator would
> change the exact symmetries entirely. **Any statement of this consequence
> that omits the candidate class or the kernel is a misstatement of it.**

**The class and the kernel, stated beside it:** the class is the uniform
flavour-singlet scalar condensate; the kernel is the exploratory
Wilson-form kernel at lines 46–90 of
`scripts/p2_phase01_scalar_exploratory.py`, with `r = 1`.

### 6.1 What is NOT thereby determined

- **Nothing is determined for non-singlet candidates.** A condensate along
  a traceless generator `λ^A` breaks `U(N)_V`, which §3.1 records as EXACT.
  For such a candidate `C-i` would read transverse, and the flat directions
  would have to be identified and counted before any Hessian could be read.
- **Nothing is determined for non-scalar channels.** The script records `P`,
  `V`, `A` and `T` as `executable: False` at lines 346–380, each missing an
  HS normalisation and a uniform-condensate ansatz, and `V`, `A` and `T`
  additionally missing an internal generator choice and a Lorentz/`H(4)`
  component choice. Those choices are exactly what would fix whether the
  candidate is an order parameter for `U(N)_V` or for `H(4)`.
- **Nothing is determined for the frozen microscopic action**, because it
  has no frozen kinetic operator (§2). Ontology lines 346–349 make the
  choice among naive / Wilson / staggered / overlap a choice of matter
  content, and lines 346–347 record that *"doublers, IF present in the
  spectrum of the declared kinetic operator, are candidate physical
  species"* — so both the species content and the exact symmetry inventory
  change with the operator, and neither is settled.
- **Nothing about stability is determined.** See §7.

---

## 7. The gap between the frozen action and the regularisation

**CONFIRMED, and it is a governance finding as well as a physical one.**

`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` §2, lines 36–47,
records the canonical action with the kinetic operator `iγ^μ ∂_μ` and the
classical symmetry `U(N)_L × U(N)_R`. **That is a continuum statement** —
there is no lattice spacing in it, and the derivative is the continuum
derivative.

The object the programme has actually been computing with is the Wilson
kernel at script lines 80–82. **Its `U(N)_L × U(N)_R` is not exact**
(§3.2): only the vector subgroup `U(N)_V` survives, and the axials are
explicitly broken by the term the regulator adds to the mass slot.

**A reader of `phaseA_freeze.md` §2 alone would not know that.** The freeze
states its symmetry without qualifying it as a continuum statement, and
does not record that the regularisation in use breaks half of it.

**Where such a reader would meet the correction: only here.** No file
existing at the evidence base carries it. **This task is forbidden by §5 of
its specification to amend the frozen action or to propose an amendment**,
and it has not done so; repairing the freeze is a separate task with its own
review, and this document neither performs nor recommends it.

### 7.1 A secondary finding on the same gap, in the script

**`scripts/p2_phase01_scalar_exploratory.py` line 73 reads:**

    """Return ``I0(Mhat)`` and ``d I0 / d Mhat`` for the frozen Wilson D."""

**The exploratory script calls the Wilson Dirac operator "frozen".** In this
repository "frozen" is the governance term for what a freeze artifact fixes,
and §2 above records that the canonical lattice Dirac operator is precisely
what has **not** been frozen. **The docstring is the same conflation the
specification's §0a identifies as unfounded**, appearing inside the artifact
the conflation was drawn from.

**Stated with its limits.** The word is used loosely elsewhere in the same
file — line 410's `"frozen_relation"` names the gap relation, and line 321's
*"the frozen Wilson integral"* most naturally reads as "the integral as
fixed in this study". Line 73 is the one place where "frozen" attaches to
**`D`**, the operator itself. **The finding is reported, not acted on:** the
script exists at the evidence base and §5 forbids modifying it.

---

## 8. What this does not establish

**Three junctions, per §7 of the specification.**

### 8.1 No Goldstone directions is not a stability result

**An `A-NO-EXACT-CONTINUOUS-BREAKING` verdict makes `C-i` readable for the
class examined. It does not make it satisfied by anything.** **The full
condensate-space Hessian has still never been computed**, and every
stability figure in the repository remains a one-dimensional restricted
curvature under a uniform scalar ansatz at `mu = 0` — the script says so
itself at line 437.

**A reader may take "no Goldstone modes" for "the condensate is stable".**
**It is not a stability statement at all** — it is a statement about which
stability statement would be the right one to make. **No candidate is named
in this document as passing or failing `C-i`, `C-ii` or `C-iii`, and none
may be inferred from it.**

### 8.2 Continuum frozen-action symmetry is not automatically the symmetry of the regularised exploratory kernel

§7 above is the finding; this is its limit as a claim. The freeze's
`U(N)_L × U(N)_R` describes the continuum Lagrangian at freeze lines 36–39
and **does not describe the kernel at script lines 80–82**. A reader of
`phaseA_freeze.md` §2 alone would meet no correction, and would meet one
only here. **This task is forbidden to create the correction in the freeze
and has not created it.**

### 8.3 A narrow verdict A does not close `OPEN-AC-4`

**Verdict A will read as though the Goldstone question were settled. It is
settled for one kernel and one candidate class, neither of which the
programme has committed to.** Ontology lines 346–349 and route line 138
make the choice of kinetic operator a choice of the theory's matter
content, and route line 322 records the artifact that would make it as
*"not created"*. **Whether `OPEN-AC-4` closes is verdict B's answer, not
verdict A's, and verdict B is `B-NOT-CLOSABLE`.**

### 8.4 Bearing on other open items, recorded without conclusion

**`OPEN-AC-3`.** `derivations/P2-LATTICE-ONTOLOGY-01.md` lines 149–152
state that where the relevant eigenvalue is degenerate *"a separately
frozen sector-selection or symmetry-breaking prescription is required
before response observables are defined"*, which bears on how `C-ii`'s
comparison set would be counted. **No conclusion is drawn.**

**`OPEN-AC-1`.** Nothing in this reading bears on it. **No conclusion is
drawn.**

---

## 9. Provenance

**Anchoring disclosure.** The determinations in §§3–5 were **reached after
reading §2 of the specification.** The executor held no prior on record
concerning the chiral symmetry of the exploratory kernel: the `C1` and `C3`
findings artifacts address root provenance and curvature asymmetry and say
nothing about chiral symmetry or Goldstone directions. **This document
therefore does not claim independent derivation for §§3.1–3.2, 3.4 or 4.**

**One determination is independent by construction.** §5.1 item 3 — the
`H(4)` argument — answers §2(e)'s third failure mode, which the
specification's author explicitly could not answer, having recorded the
lattice ontology and route documents as unread. **The reason found is
stronger than the one the author anticipated:** the author expected
discrete breaking to produce no flat directions "normally", whereas ontology
lines 114–115 make the exact spacetime symmetry group **finite**, so the
exclusion is structural and candidate-independent.

**Material read beyond §1's list:** none that carries the answer. §1's five
files were sufficient.

**Evidence base:** `1b569851a914589242024c4dde7d2eb020e3800c`.
`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` measures
`fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a`;
`scripts/p2_phase01_scalar_exploratory.py` measures
`3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0`.
**No file existing at the evidence base was modified by the task that
produced this document, and no script was run to produce it.**
