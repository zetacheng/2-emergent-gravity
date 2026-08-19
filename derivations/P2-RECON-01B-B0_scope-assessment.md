# `P2-RECON-01B-B0` — what a clean-room `k`-scan would be starting from

    KIND        SCOPE ASSESSMENT. MEASUREMENT ONLY. NO LANDING.
    BASE        968e726a5a4322eecf4254ff69b25832f263c155
    ANSWERS     Q1  the state of each of RECON-01b's ten components
                Q2  what the axis-TT projection removes, and where
                    CIRC-01's mixed sector falls relative to it

**This artifact computes nothing.** No `β_V` value, no `k`-scan, no
determinant, no derivative. **No script named below was executed.** Every
state, count and classification was measured at `968e726a`; **nothing was
carried from `derivations/P2-BETAV-RECON-01_scope-assessment.md`**, whose
figures are prior observations against an earlier tree and are not targets.

**It recommends no course of action on the blind target.** `§12` of the
governing specification reserves that, and every question of that kind is
listed in `§7` below as open rather than answered.

---

## 1. `M1` — the ten components, re-measured

**Four mutually exclusive states, and the same applicability test the prior
assessment defines: an implementation counts only if it is POTENTIALLY
APPLICABLE TO THE CLEAN-ROOM RECONSTRUCTION.**

The inventory was located at
`derivations/P2-BETAV-RECON-01_scope-assessment.md:473-484` — ten numbered
rows. **No `A2` abort: the list is in the repository and was not reconstructed
from the specification, which does not contain it.**

| # | Component | State at `968e726a` |
|---|---|---|
| 1 | metric-coupled 1-form operator `Δ⁽¹⁾[g,h]` on a weak-field background, exact geometric factors | `IMPLEMENTATION + SPECIFICATION` |
| 2 | compensating scalar `Δ⁽⁰⁾[g,h]` | `IMPLEMENTATION + SPECIFICATION` |
| 3 | `Γ_k = ½ logdet Δ⁽¹⁾ − (k/2) logdet Δ⁽⁰⁾` at the determinant level | `SPECIFICATION ONLY` |
| 4 | numerical `h`-derivatives at determinant/eigenvalue level, with Richardson check | `IMPLEMENTATION + SPECIFICATION` |
| 5 | fixed axis-TT projection, identical for every `k`, pre-registered | `SPECIFICATION ONLY` |
| 6 | the `k`-scan driver over `k ∈ {0,1,2,3,½}` | `SPECIFICATION ONLY` |
| 7 | flat-limit validation against the Proca eigenstructure | `IMPLEMENTATION + SPECIFICATION` |
| 8 | blind two-stage harness: frozen output, external digest, deferred comparison | `IMPLEMENTATION + SPECIFICATION` |
| 9 | ratio-error tolerance rule, numerator and denominator correlated | `SPECIFICATION ONLY` |
| 10 | registered regression anchors for the reconstruction itself | `NEITHER` |

### 1.1 Totals, recomputed from the rows

    N_both      5      components 1, 2, 4, 7, 8
    N_impl      0
    N_spec      4      components 3, 5, 6, 9
    N_neither   1      component 10
               --
    N_total    10      5 + 0 + 4 + 1 = 10   ✓

**The four totals were counted from the ten rows above, not carried.** The sum
is checked: `5 + 0 + 4 + 1 = 10`, and the table has ten rows.

### 1.2 Evidence, per component

**Component 1 — `IMPLEMENTATION + SPECIFICATION`.**
Implementation: `scripts/recon2026/proca_curved.py:287`,
`vector_operator(geom, h, mass_squared)`, the metric-coupled 1-form operator
built from the covariant field-strength action's Hessian divided by the mass
metric (`:242`, `:274`), on the weak-field background `cosine_weak_field` at
`:143`. Exact geometric factors are a declared convention: `:28-29`,
*"`g^{mu nu}` is the exact matrix inverse of `g_{mu nu}`, not a truncated
weak-field expansion, and `sqrt(g) = sqrt(det g)`."*
**POTENTIALLY APPLICABLE**, and the reason is stated in the file itself at
`:9-10`: *"Nothing is imported from, copied from, or structurally modelled on
any script under ``scripts/recovered_2026/``."* **The clean-room objection that
disqualified the prior implementation does not apply to this one.**
Specification: `GATES.md:737-738`;
`derivations/P2-BETAV-RECON-01a_construction-and-flat-validation.md:19-23`.

**Component 2 — `IMPLEMENTATION + SPECIFICATION`.**
Implementation: `scripts/recon2026/proca_curved.py:196`,
`scalar_operator(geom, h, mass_squared)`, from the covariant Dirichlet action,
same construction and same conventions. **POTENTIALLY APPLICABLE** for the same
reason as component 1.
**And the second objection the prior assessment raised does not transfer.** It
reclassified this component partly because `CIRC-01` found the recovered
external scalar is not the Proca longitudinal eigenfactor
(`GATES.md:382-385`). That is a finding about `boson_loop.geomB`, a specific
recovered operator. `scalar_operator` is a different object built from a
different action, and
`P2-BETAV-RECON-01a_construction-and-flat-validation.md:170` records validation
`(c)` — the compensating scalar is **propagating and not ultralocal** — as a
measurement on this construction.
Specification: `GATES.md:737-738`.

**Component 3 — `SPECIFICATION ONLY`.**
**The determinant primitive exists and the combination does not.**
`scripts/recon2026/proca_curved.py:356` supplies `logdet_operator(matrix)`, and
`flat_validation.py` calls it on `scalar_operator` and `vector_operator` output.
**But `Γ_k` is the `k`-weighted combination `½ logdet Δ⁽¹⁾ − (k/2) logdet Δ⁽⁰⁾`,
and no code forms it.** The `RECON-01a` artifact states this of its own scope at
`:3-5`: *"It builds and validates. It does not assemble a determinant
combination, does not vary any determinant power, and does not compare any
quantity to an external target."* `flat_validation.py:16` repeats it:
*"Nothing here computes a determinant ratio, varies a determinant power…"*
**A primitive is not the component. The component is the assembly, and the
assembly is specified and unbuilt.**
Specification: `GATES.md:738`.

**Component 4 — `IMPLEMENTATION + SPECIFICATION`.**
Implementation: `scripts/recon2026/flat_validation.py:299`
`_central_difference`, `:303` `_richardson`, `:312` `validate_mass_derivative`,
`:356` `validate_background_derivative`. The last takes **first and second
background (`h`) derivatives of `log det(D1 + m²)` at `h = 0`** — a derivative
at the determinant level, which is the component as specified. The Richardson
step is at `:303-309` and is applied at `:343`.
**POTENTIALLY APPLICABLE**: clean-room, and validated against two independent
known answers rather than against any ratio — `:313-317` names the closed form
`sum_p 1/(phat2(p) + m^2)` and states it is *"an answer known independently of
the construction and unrelated to any ratio target."*
Specification: `GATES.md:738`, `:747`.

**Component 5 — `SPECIFICATION ONLY`. Code exists and is not applicable.**
Implementation exists: `scripts/recovered_2026/mlog_coeff.py:21-31`
`TT_RECIPES`, and `proca_loop.g2_axis_proca`, reused by
`scripts/betav_decomp_q2.py:51`.
**NOT POTENTIALLY APPLICABLE**, and the prior assessment's reason holds
unchanged at this base: the gate requires the projection **pre-registered with
targets kept out of code and tests** (`GATES.md:748`), and these recipes live
inside recovered modules that carry the analytic target.
**MEASURED: no axis-TT projection exists in the clean-room tree.**
`grep -c -i -E 'axis|TT_RECIPE|traceless'` over both files of
`scripts/recon2026/` returns **0** for each. What that tree does contain is
`longitudinal_projector_flat` (`proca_curved.py:332`), a rank-1 longitudinal
projector — **a different object**, and §8's warning that `projection` does not
match `projector` and that both may be relevant is exactly this case.
Specification: `GATES.md:739`, `:748`.

**Component 6 — `SPECIFICATION ONLY`. Code exists that scans `k`, and it is
not an implementation of this component.**
`scripts/betav_assembly.py:144-148` prints a `k`-scan and iterates `res["per_k"]`.
**NOT POTENTIALLY APPLICABLE, for two independent reasons, each measured:**
**first, it embeds the analytic target** — `:148` prints
`target {d['target_minus_k_plus_2']:+.1f}`, and its docstring at `:19` writes
`R_k = beta_V(k)/beta_B = -(k+2)` — which is the hazard `GATES.md:415-418`
names; **second, it is not scanning the right object.** It composes analytic
species prefactors against **one shared scalar lattice tadpole** and builds no
metric-coupled operator, and it says so itself at `:152-153`: *"C cancels in the
ratio -> spread ~ machine zero -> this construction cannot test the historical
projection."* **A driver that scans `k` over cancelling analytic prefactors is
not a driver that scans `k` over curved-background determinants.**
`git grep -n -i -E 'k-scan|k_scan|kscan' -- '*.py'` returns no other candidate:
the remaining matches are `betav_decomp_check.py:3`, `:126` and
`betav_decomp_q2.py:3` declaring **NO k-scan**, and two test files asserting
governance text.
Specification: `GATES.md:740`.

**Component 7 — `IMPLEMENTATION + SPECIFICATION`.**
The state is unchanged from the prior assessment; **the implementation
satisfying it is not.** The prior assessment cited
`scripts/betav_decomp_check.py`, a recovered-side check. At this base
`scripts/recon2026/flat_validation.py` supplies validations `(a)`, `(c)` and
`(d)` against the Proca eigenstructure — `:60` `analytic_flat_vector_spectrum`,
`:77` `validate_flat_vector_spectrum`, `:240` `validate_compensating_scalar`,
`:266` `scan_extents_and_masses` — with `tests/test_recon2026_flat_limit.py`
exercising them. **POTENTIALLY APPLICABLE**: clean-room, and `:1-19` states the
driver *"runs the five validations this stage owes, none of which involves any
final ratio target."*
Specification: `GATES.md:747`.

**Component 8 — `IMPLEMENTATION + SPECIFICATION`.**
Implementation: `scripts/P2-BETAV-CAMPAIGN/harness_compute.py` and
`compare.py`, both blob-unchanged from the prior assessment.
**POTENTIALLY APPLICABLE** on the prior assessment's stated ground, re-read and
still true: the architecture — frozen JSON, external digest, deferred
comparison — is what the reconstruction needs, and its current imports are not
what is being reused.
Specification: `GATES.md:748`.

**Component 9 — `SPECIFICATION ONLY`.**
**No implementation.** The ratio-error tolerance rule with correlated numerator
and denominator is named in
`derivations/P2-BETAV-RECON-01_scope-assessment.md` and its report and nowhere
else; a search for `ratio-error` and `ratio error` over the tree returns those
two documents and no code.
**The correlation is not incidental to the rule.**
`scripts/betav_assembly.py:20-23` records why: *"Because numerator and
denominator are the SAME integral C times different rational prefactors, C
cancels exactly."* A tolerance rule that treated the two as independent would
mis-state the error on a ratio whose parts cancel.
Specification: `GATES.md`'s `Inputs` block at `:746-748` does not name it; it is
specified in the prior scope assessment.

**Component 10 — `NEITHER`.**
`GATES.md:753-754`, quoted in full:

    ### Regression anchors
    None yet (proposed).

**No implementation and no specification.** `results/` contains no directory
matching `recon` at this base.

---

## 2. `M2` — comparison against the prior assessment

**The prior assessment's evidence base is `ece34f7bacbbee00efa0fecf0be644d593eed72f`**,
recorded at its `:12`. Its table is at `:473-484` and its totals at `:486-491`.

| # | prior state | state at `968e726a` | differs? |
|---|---|---|---|
| 1 | `SPECIFICATION ONLY` | `IMPLEMENTATION + SPECIFICATION` | **YES** |
| 2 | `SPECIFICATION ONLY` | `IMPLEMENTATION + SPECIFICATION` | **YES** |
| 3 | `SPECIFICATION ONLY` | `SPECIFICATION ONLY` | no |
| 4 | `SPECIFICATION ONLY` | `IMPLEMENTATION + SPECIFICATION` | **YES** |
| 5 | `SPECIFICATION ONLY` | `SPECIFICATION ONLY` | no |
| 6 | `SPECIFICATION ONLY` | `SPECIFICATION ONLY` | no |
| 7 | `IMPLEMENTATION + SPECIFICATION` | `IMPLEMENTATION + SPECIFICATION` | no |
| 8 | `IMPLEMENTATION + SPECIFICATION` | `IMPLEMENTATION + SPECIFICATION` | no |
| 9 | `SPECIFICATION ONLY` | `SPECIFICATION ONLY` | no |
| 10 | `NEITHER` | `NEITHER` | no |

    totals      prior                    968e726a
    N_both        2   (7, 8)               5   (1, 2, 4, 7, 8)
    N_impl        0                        0
    N_spec        7   (1,2,3,4,5,6,9)      4   (3, 5, 6, 9)
    N_neither     1   (10)                 1   (10)
                 --                       --
    N_total      10                       10

### 2.1 The cause, measured

**Three components differ, and one event accounts for all three.**

**MEASURED: `scripts/recon2026/` did not exist at the prior base.**
`git ls-tree -r --name-only ece34f7b scripts/ | grep -c 'recon2026'` returns
**0**, and the prior assessment's text contains **0** occurrences of
`recon2026`. At `968e726a` the tree carries three files:

    scripts/recon2026/proca_curved.py        364 lines
    scripts/recon2026/flat_validation.py     442 lines
    tests/test_recon2026_flat_limit.py       110 lines

**`P2-BETAV-RECON-01a` landed the clean-room construction between the two
bases.** Components 1, 2 and 4 moved from `SPECIFICATION ONLY` to
`IMPLEMENTATION + SPECIFICATION` because an applicable implementation came into
existence, not because the applicability test was applied differently.

**The prior assessment's own reasoning is what changed footing.** It
reclassified components 1 and 2 to `SPECIFICATION ONLY` on the ground that the
only implementations were recovered-pipeline code whose reuse would defeat the
clean-room label. **That ground is gone for those two components** — there is
now a construction built expressly to be clean-room, and its own file says so.
**The prior classification was correct when it was made.**

### 2.2 One refinement that is NOT a state difference, recorded so it is not
mistaken for one

**Component 6.** The prior assessment listed three components as "implementation
exists but unusable here" — 1, 2 and 5 — at its `:509-535`. **Component 6 is a
fourth case of the same kind**, and it was not listed as one.

This is not a disagreement about state: the prior assessment did assess
`scripts/betav_assembly.py` at its `:172-184`, classified its reuse as `check`,
and recorded that *"Its docstring states the ratio formula, so a blind harness
must not import it into the measuring stage."* **Both readings reach
`SPECIFICATION ONLY` for component 6.** The blob is unchanged —
`f3d8fa25d233871c4cd3de8c7acc3343bdc7bf9f` at both bases.

**What differs is only whether the fact appears in the inventory's
"code exists and is not applicable" list.** `§5.1` of the governing
specification requires this measurement to distinguish "no code exists" from
"code exists and is not applicable" and to record the reason in the second
case. **At `968e726a` that second case holds for components 1, 2, 5 and 6** —
though for components 1 and 2 it no longer decides the state, because an
applicable implementation now exists alongside the inapplicable one.

**Component 7's implementation also changed without its state changing**, and
that is recorded at `§1.2` rather than here, because a state comparison would
show `no` for it and the change would otherwise be invisible.

---

## 3. `M3` — what the axis-TT projection retains and discards

**Located in both forms.** No `A3` abort.

**Implementation:** `scripts/recovered_2026/mlog_coeff.py:21-31`, quoted:

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

**Specification:** `GATES.md:739`, *"fixed axis-TT projection"*, and `:748`,
*"pre-registered projection (targets kept out of code/tests)"*.

**The index space it acts on.** The recipes are combinations of **external
polarization index pairs**, for momentum along the axis `q ∥ e₀`.

**RETAINS: five components**, and they span the symmetric traceless tensor of
the 3-space orthogonal to `q`. Recipes 1 and 2 are the two independent diagonal
traceless combinations of `(1,1)`, `(2,2)`, `(3,3)`; recipes 3, 4 and 5 are the
three off-diagonal spatial pairs `(1,2)`, `(1,3)`, `(2,3)`. Each is
unit-normalised.

**DISCARDS: every external index pair involving the axis index `0`** —
`(0,0)`, `(0,1)`, `(0,2)`, `(0,3)` — **and the spatial trace**
`(1,1)+(2,2)+(3,3)`, which no recipe reaches because recipes 1 and 2 are
constructed traceless.

**Read, not counted.** `§8` records that `TT` matches `tt_check` and matches
inside unrelated words, and that `transverse` appears both as a sector name and
in prose. The determination above is from reading the recipe list and its
comment, not from any count of either token.

---

## 4. `M4` — `CIRC-01`'s `q²`-level decomposition, as stated

`derivations/P2-BETAV-CIRC-01_determinant-decomposition.md:37-45`. **Measured
by `scripts/betav_decomp_q2.py` at `m = 0.3`, `n ∈ {10,12}`, q-ranges
R1/R2/R3, with sector `q²` coefficients summing to the total to `<1e-12`.**

| sector | `q²` coefficient | scaling exp of `Π−Π(0)` |
|---|---|---|
| TT | `≈ +2.12e-2` (≈96.5% of total) | `≈ 1.99` (q²) |
| LL | `≈ +6.8e-4` (≈3.1%) | `≈ 1.97` |
| **TL+LT (mixed)** | **`≈ +9.0e-5` (≈0.4%)** | **`≈ 1.98` (q²)** |
| total | `≈ +2.20e-2` | `≈ 1.99` |

**Stability, as stated at `:47`:** *"Stable across `n=10,12` (mixed:
`8.7e-5`↔`9.1e-5`) and across q-ranges."*

**These magnitudes are quoted from `CIRC-01`. Nothing here recomputed them.**

**What the sector labels mean, from `:30-35`.** The projectors are `P_{T,L}(k)`
and `P_{T,L}(k+q)`, **built independently from `a(k)` and `a(k+q)`**, applied to
the two internal propagators: `G1 → P_X(k) G1`, `G2 → P_Y(k+q) G2`.
**The labels are a decomposition of the INTERNAL propagator index structure, at
two momenta.** They are not a decomposition of the external polarization.

---

## 5. `M5` — where each sector falls relative to the projected object

**Determination per sector, structural, from `M3` and `M4` together.**

| sector `M4` reports | determination |
|---|---|
| TT | **INSIDE** |
| LL | **INSIDE** |
| TL+LT (mixed) | **INSIDE** |
| total | **INSIDE** |

**All four are inside. No sector `CIRC-01` reports is removed by the axis-TT
projection**, and the evidence is the order of operations in the code that
produced the table.

### 5.1 The evidence — the projection is applied upstream of the decomposition

`scripts/betav_decomp_q2.py:10-12` states the construction:

> We decompose the recovered Proca **axis-TT bubble** (same construction as
> `proca_loop.g2_axis_proca`) into sectors using projectors built INDEPENDENTLY
> from a(k) and a(k+q)

and `sector_bubble` at `:69-102` carries it out in that order:

    :51   from mlog_coeff import TT_RECIPES
    :74   R2 = np.stack([sum(c * dJ2[p] for p, c in r) for r in TT_RECIPES])
    :75   Rm = np.stack([sum(c * dJ[p]  for p, c in r) for r in TT_RECIPES])
    :83   U1 = 2.0 * pl.kin_form(R2, np.conj(a1), b1) + m**2 * Rm[:, None, :, :]
    :86   PTk, PLk = _projectors(pl.avec(kk))     # basis a(k)
    :87   PTq, PLq = _projectors(pl.avec(kkq))    # basis a(k+q)
    :92   for X in ("T", "L"):  ...  for Y in ("T", "L"):
    :102  return {k: v / n**4 / 5.0 for k, v in acc.items()}

**Lines 74-75 apply the axis-TT projection**, contracting the vertex derivative
tensors with `TT_RECIPES` to produce the five-component index `r`. **Lines
83-85 build the vertices from those already-projected tensors.** Only then, at
`:86-97`, are the `T`/`L` projectors applied — to the internal propagators.
`:102` divides by `5.0`, the average over the five retained recipes.

**So every sector in `M4`'s table is a sub-decomposition of an object that has
already passed through the axis-TT projection.** A sector cannot be outside a
projection that was applied before the sector existed.

### 5.2 Why the question does not reduce to competing projections

**The two decompositions act on different index spaces**, and this is the
structural point that makes all four determinations `INSIDE` rather than
contingent.

    axis-TT projection   acts on the EXTERNAL polarization index pair,
                         retaining a 5-dimensional symmetric traceless
                         spatial tensor space for q || e0
    CIRC-01's T / L      acts on the INTERNAL Proca propagator indices,
                         with projectors built at k and at k+q separately

**`P2-BETAV-RECON-01a_construction-and-flat-validation.md:246-254` states the
same distinction independently**, for a different pair of measurements, and
warns against collapsing them:

> **MY NUMBERS AND `CIRC-01`'s MEASURE DIFFERENT OBJECTS AT DIFFERENT ORDERS,
> AND REPORTING `3e-16 vs 9e-5` AS AGREEMENT OR DISAGREEMENT WOULD BE A
> CATEGORY ERROR.**

**The `M5` limitation did not bind.** No sector required a `β_V` value, a
`k`-scan, or any quantity over which the blind target ranges. **No
determination is `INCONCLUSIVE`, and none was reached by executing anything.**

### 5.3 What the projection does remove, and whether anything measured lives there

**It removes the external index pairs involving `0` and the spatial trace**,
per `M3`. **`CIRC-01` reports no magnitude in that space.** Its table has four
rows and all four are `T`/`L` sectors of the already-projected bubble.

**So the measured `≈0.4%` mixed contribution is not a blind spot of the
projection.** It is a component of what the projection retains. **Whether
anything of physical consequence lives in the discarded external space is a
question this assessment does not answer**, because no repository measurement
reports a magnitude there — see `§7`.

---

## 6. `M6` — the blind target and kill values

**Locations and text as read at `968e726a`.**

**The analytic anchor — `GATES.md:750-751`:**

    ### Analytic anchors
    `β_V/β_B = −(k+2)` (from `P2-HK-01`), compared only at the end.

**The kill criterion — `GATES.md:756-759`:**

    ### Kill criterion
    For the reconstruction itself: stuck at `−3` ∀k ⟹ the new pipeline is degenerate
    (a bug); drift toward `−5` at heavy mass ⟹ longitudinal artifact. None of these
    closes `P2-BETAV-CIRC-01`.

**The regression anchors — `GATES.md:753-754`:**

    ### Regression anchors
    None yet (proposed).

**The gate's own status — `GATES.md:727`, `:769-773`:**

    Status: PROPOSED (not run; distinct from the historical circularity question)
    ### Result
    Not run.
    ### Reviewer verdict
    `PROPOSED`.

### 6.1 By what mechanism

**Two mechanisms are recorded and they are different in kind.**

**The blinding mechanism — `GATES.md:748`:** *"pre-registered projection
(targets kept out of code/tests)"*, and `:751`'s *"compared only at the end"*.
**The target is not hidden from the repository; it is written in the gate. What
is required is that it stay out of the measuring code and its tests.**

**The sign — `derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md:11-15`:**

> **`SIGNED NEGATIVE`.**
>
> **The repository's frozen conventions require `β_V/β_B = −(k+2)`, hence `−3`
> at the physical `k = 1`. The unsigned form carried by the `RECON-B0`
> specification is an error.**

`SIGN-01` derived this from `CONVENTIONS.md:15`, `:16`, `:19` and `:21` rather
than quoting `P2-HK-01` (`:17-20`), and **it corrected none of the documents it
found inconsistent** — it states so at `:22-23` and lists them at `§6`.

### 6.2 What is and is not frozen — stated as measured, not concluded

**The target's VALUE and the kill values are written in the gate** at the lines
quoted above, and the gate section is subject to the repository's gate-integrity
checking. **The sign is settled by a landed adjudication.**

**The regression anchors are `None yet (proposed)`** — component 10's `NEITHER`
state and this line are the same fact seen twice.

**`SIGN-01` recorded that documents asserting the target UNSIGNED remained
inconsistent with its verdict and that it corrected none of them.** Whether
those were subsequently repaired is not measured here; `M6` asks for the target
and kill values' status, and both are as quoted.

---

## 7. Questions this measurement raised and could not settle

**Recorded as open. None is resolved in prose below.**

1. **Component 3's boundary.** A determinant primitive exists and the `k`-weighted
   assembly does not. **Whether "an implementation exists" for a component
   should be judged on the assembly or on its primitives is a classification
   question this assessment answered one way** — on the assembly, since that is
   what the component names — **and a different reader could answer it the other
   way and reach `IMPLEMENTATION + SPECIFICATION`.** The evidence for both
   readings is at `§1.2`.

2. **What lives in the discarded external space.** `M3` establishes what the
   axis-TT projection removes. **No repository measurement reports a magnitude
   there**, so this assessment cannot say whether anything of consequence does.
   Measuring it would require constructing the unprojected object, which is
   outside this task.

3. **Whether component 9's rule is specified enough to implement.** It is named
   in the prior scope assessment and appears in no gate `Inputs` block. **Whether
   that constitutes a specification, or only the identification of one that must
   be written, is not determined here.**

4. **Component 5's pre-registration requirement.** `GATES.md:748` requires the
   projection pre-registered with targets kept out of code and tests. **A
   clean-room re-expression of `TT_RECIPES` would be arithmetically identical to
   the recipes at `mlog_coeff.py:21-31`** — the tensors are fixed by the
   symmetry, not chosen. **Whether transcribing a target-free constant from a
   target-bearing module counts as reuse is a governance question**, and it is
   not answered here.

---

## 8. What this assessment does not establish

- **It produces no `β_V` value**, no `k`-scan, no determinant ratio, and no
  estimate or bound on any of them. No script named in this artifact was
  executed.
- **It makes no PI decision on the blind target.** Whether the target and kill
  values of `§6` are used as they stand, re-registered, or amended is not
  decided, recommended, or hinted at here.
- **A count of components is not a measure of difficulty or duration.** Five
  components in `BOTH` is not five-tenths of the work done. **Component 10, the
  one in `NEITHER`, is plausibly among the cheapest of the ten to produce** —
  which is the same demonstration the prior assessment made at its `:542-547`,
  and it survives the change in the counts.
- **It does not establish that `RECON-01b` should proceed**, that it is ready,
  or that it would succeed. It measures what `RECON-01b` would be starting from.
- **It does not re-adjudicate `CIRC-01`'s verdict** `DECOMP-UNAVAILABLE-AS-RECOVERED`,
  and nothing in `§4` or `§5` bears on it: `M4` quotes `CIRC-01`'s own table and
  `M5` reads the order of operations in the code that produced it.
- **It rules no `R`-node** and takes no position on `r = 1` or the order of `Z_M`.
- **A clean-room implementation existing is not a clean-room implementation
  validated for this purpose.**
  `P2-BETAV-RECON-01a_construction-and-flat-validation.md:367` records that *"A
  validated flat limit does not validate the curved construction"*, and `:381`
  that *"Clean-room is a claim about provenance, not correctness."* **The three
  state changes at `§2` are changes in availability, not in correctness.**
