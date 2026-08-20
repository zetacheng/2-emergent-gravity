# Landing record — `P2-OBS-IDENT-INTEG`

**Transport only.** Every statement below is one the reviewed result already
made. **Nothing here is a new result, and no consequence of the result is
drawn.**

    Source   science/obs-ident-01   612817cb9ffa75ca02341e4f408f5fc952000557
    Base     f23a0e1e1a24398d082a9597444ff9f750ed38e1
    Fork     f23a0e1e1a24398d082a9597444ff9f750ed38e1

---

## 1. The outcome and the relation

    OUTCOME   PROXY ONLY

**The definitional location.** `CONVENTIONS.md:21`, the locked-conventions
table, defines the species coefficient as the **coefficient of `m² ln m²` in
`Z(m²)`**. `CONVENTIONS.md:20` defines `Z(m²)` as the induced axis/TT graviton
kinetic coefficient and states that "The `m²ln m²` piece defines the species
coefficient". `GATES.md:152` states the same definition for the scalar species
and adds the method — "from a lattice mass scan".

**The two extraction steps, with the reviewed result's code citations.**

    STEP 2   proca_loop.slope at :171-173
             VARIES the external momentum over a four-point grid;
             HOLDS the mass and the extent;
             fits an even polynomial of order 2 and returns index [1] —
             THE q² COEFFICIENT. THIS IS Z(m²).

    STEP 3   reproduce_betav.vector_ZV at :53-57
             VARIES the mass over a scan window, calling step 2 once per
             mass; then mlog_coeff.fit_mlog at :81-89, whose docstring at
             :82 is "Z(m^2) = z0 + z1 m^2 + beta m^2 ln(m^2) (+ z2 m^4)",
             and returns coef[2] — THE COEFFICIENT OF m² ln m².
             THIS IS THE TARGET COEFFICIENT.

(The reviewed result numbers a preceding step 1, `proca_loop.g2_axis_proca` at
`:108`, the bubble at one momentum at one mass; the two steps above are the
ones the relation turns on.)

**The relation, as the reviewed result states it.** The two quantities differ
in the **mass treatment**, and consequently in the extraction.

**What is COMMON is recorded alongside what differs**, because the difference
is otherwise easy to overstate: both are the axis-TT projection of the same
Proca bubble, in the same basis, at `q ∥ e₀`, at the same extent, and
`EXT-01`'s momentum grid is the same four-point grid `proca_loop.slope` uses by
default. **The single difference is the mass treatment.**

---

## 2. What `EXT-01` measured, and what it did not

**`EXT-01` performed step 2, per component, at one mass.** It reported `B`, the
`q²` coefficient of `Π(q) = A + Bq² + Cq⁴`, for each of ten orthonormal
external components.

**It did not perform step 3.** No mass scan; no `m² ln m²` fit.

**Established against the code by the reviewed result, and transported as
such.** `scripts/diagnostics/ext01_discarded_external_space.py:57` sets the mass
as a module constant, `:167` passes it unchanged into every evaluation, and the
script **neither imports nor calls `fit_mlog`** — the only fit it defines is
`fit_even` at `:129-132`.

**Step 2's output is step 3's input, one point per mass.** `EXT-01`'s quantity
is therefore **the input to the fit that produces the target coefficient,
rather than the coefficient itself.**

---

## 3. What this does not establish

**`EXT-01` IS NOT INVALIDATED.** Its execution, its pre-registration and its
independent reproduction stand. **The question the audit asked was what its
numbers bear on, not whether they are right.**

**NOTHING IS CONCLUDED ABOUT WHETHER THE DISCARDED EXTERNAL SPACE MATTERS FOR
THE TARGET COEFFICIENT.** The reviewed result specifies what measuring that
would require — vary the mass over a window that resolves the non-analytic term
against the analytic ones, hold the extent, momentum grid, direction and basis,
extract `B` per mass per component, then fit `Z(m²)` per component — **and does
not perform it.** Neither does this landing.

**`A-EXT-01` IS UNCHANGED**, and the silence recorded at §4 below is **not read
either way**.

**`Q1`, `GAP-A`, `GAP-B` AND `H-EXT-01` ARE UNCHANGED IN STATUS.** `Q1` remains
`INCONCLUSIVE` with its subclass and `Resolution path`; `GAP-A` remains closed
with its momentum condition; `GAP-B` remains `INDETERMINATE — UNDETERMINED BY
READING` with its five mismatches; `H-EXT-01` remains `UNESTABLISHED — NOT
ASSUMED BY RECON-01b`.

---

## 4. The `A-EXT-01` finding, transported and not resolved

**As the reviewed result records it:** `A-EXT-01`'s exact statement opens

> For `RECON-01b`, `Z_axis-TT` is defined as the coefficient extracted after
> the repository's axis-TT projection.

and **"the coefficient" does not say which.** Two candidates sit under the
phrase — the `q²` coefficient at a given mass, and the `m² ln m²` coefficient
of its mass-dependence. **The exact statement selects neither.**

**The statement is unaltered and no reading is supplied here.** Its
`Statement SHA` is `ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378`,
unchanged by this landing. **Resolving the ambiguity would require a new exact
statement, which would break that pin and void the pinned review**, and is
registered at §6 as `R-4`.

---

## 5. The negative existence finding, with its search extent

**No per-component instance of the target coefficient was found.**

**The search extent, transported because without it the finding is not
checkable.** The reviewed result examined **the five files that call
`fit_mlog`**: `scripts/recovered_2026/mlog_coeff.py`,
`scripts/recovered_2026/proca_loop.py`,
`scripts/recovered_2026/reproduce_betav.py`,
`scripts/recovered_2026/batch2/precision_campaign.py`, and
`scripts/P2-BETAV-CAMPAIGN/harness_compute.py`. **None decomposes the mass fit
over the ten external-index components.**

**With its exclusion, stated by the reviewed result.** Three of the five
reference `TT_RECIPES` and use the retained five components as **one
combination** — `proca_loop.g2_axis_proca` builds its vertices from
`TT_RECIPES` at `:115-116` and returns an average over them at `:130`. The
fifth uses the word "component" in a different sense: `harness_compute.py:392`
lists `["proca", "gfvec", "boson", "D"]`, which are **determinant species, not
external index components**. **A count of the word would have misled**, which is
why the exclusion travels with the finding.

---

## 6. The compliance self-correction

**Transported because a compliance check that becomes a violation source is a
reusable finding.**

The reviewed result's own report contains a criterion paragraph verifying that
certain forbidden literals do not appear in the audit artifact. **Its first
draft listed those literals as the search terms** — placing them into a
document the same criterion's search extent covers. **It was corrected before
commit**, to name their locations and report the search result instead, and the
correction is recorded in that report rather than made silently.

**The general form: a compliance report that proves a literal absent by
quoting it has introduced the thing it was checking for.** The check's extent
must be read before its evidence is written.

---

## 7. Records registered, per `M5` — none answered

**All four are admitted by `DECISION_LOG.md`**, and are registered there in one
entry dated 2026-08-20, "OBS-IDENT open records, registered and none answered".

    R-1   D-2's purpose, undecided.
    R-2   The scope of GAP-B, MM-1, MM-3 and MM-5, undecided.
    R-3   Whether any landed description of EXT-01's measurement requires
          narrowing, and by what mechanism, undecided.
    R-4   The A-EXT-01 ambiguity, and whether a definitional convention
          silent at its load-bearing point requires supersession, open.

**Why `DECISION_LOG.md` admits them, on its stated scope.** Its head requires
new entries to use the entry template, and the entry dated 2026-08-19 —
"EXT-01 execution-layer dispositions and open findings" — is the precedent:
`O-1` and `O-2` were registered there as **open findings** by an **executor for
an integration**, with "Nothing is settled by recording them" stated in those
words, and with a `### Reason` explaining that dispositions otherwise live only
in a task report. **The new entry has the same shape and says the same thing.**

**`R-4` is NOT duplicated into `docs/GOVERNANCE-DEBT.md`.** It is adjacent to
`G-13`, and the two are different questions — `G-13` asks whether a reviewed
definitional statement **may be** edited in place (permission); `R-4` asks
whether **this** statement's silence **requires** supersession (necessity,
about one instance). The new entry cross-references `G-13` and states the
difference. **A second entry would create a second place for one status to
drift**, which `docs/GOVERNANCE-DEBT.md`'s `## Not entered here — D4` section
warns against.

**No register was created, and none was used by convenience.**

**No record restates an existing obligation, and the count of obligations with
no admissible home is not incremented by this task** — all four found a home.

---

## 8. What this landing does not establish

It lands an audit already performed, reviewed and verified. **It produces no
new subject-matter result and no measurement of any physical quantity.** No
gate moves; `P2-PHASE-01` is unchanged.

**It is not without consequence** — four are registered above — **but every one
is registered as open, and none is drawn.**
