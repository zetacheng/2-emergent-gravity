# Pre-registration — P2-BETAV decisive campaign (operator-identity audit + NUMREPRO)

**Frozen before any compute.** This document freezes the rules for the blind
campaign that rebuilds the historical (never-run) `precision_campaign.py` under
modern discipline. It serves **two registered gates, kept strictly distinct**:

- **`P2-BETAV-CIRC-01`** — the operator/determinant-identity **audit** (its
  registered test since the Phase-1 adjudication). Object: the Solodukhin
  quotient as implemented in `scripts/recovered_2026/batch2/gfvec_loop.py`,
  `Γ_Proca = Γ_minvec − Γ_scalar`, numerically the consistency relation
  `R_cons = β_proca − β_gfvec + β_boson = 0`.
- **`P2-BETAV-NUMREPRO-01`** — numerical **reproduction** of the historical
  `−3.2(5)` at the historical configuration, plus execution of the programme's
  own historical promotion criterion (both ratios at `−2.00`/`−3.00`).

**This task pre-registers rules, builds the blind harness, and validates it on
a non-decisive pilot. The decisive runs (Arm H, then Arm P) are a separate,
subsequently authorized task.**

## Scope statements (verbatim, binding)

- An audit PASS establishes that the implemented operators numerically obey the
  claimed determinant identity — i.e. the `−3` target is the correct
  multiplicity bookkeeping of these operators. **Per the Phase-1 adjudication,
  every pipeline step is linear, so this audit does not and cannot establish
  strong historical non-circularity; that question remains as documented in
  Phase-1.**
- A NUMREPRO PASS reproduces a historical number; **it does not by itself
  promote `P2-C9`.** Promotion is a separate PI+reviewer decision applying the
  programme's historical criterion, taken only after results are in. The
  `−3.2(5)` quarantine is untouched by this task.
- **Three distinct recorded outputs (never conflated):** the campaign produces
  (1) the **CIRC audit verdict**; (2) the **Arm-H NUMREPRO verdict**; and (3) the
  **Arm-P historical-promotion-criterion outcome**. `P2-BETAV-NUMREPRO-01` refers
  to output (2) **only**. **CIRC PASS + NUMREPRO PASS is necessary but not
  sufficient.** **Quarantine release or `P2-C9` promotion requires the registered
  dual-gate conditions AND explicit consideration of the separately recorded
  Arm-P historical-promotion outcome, followed by PI+reviewer authorization. No
  script automatically promotes the claim.**
- The audit is non-trivial: `β_gfvec` is extracted from an **independent** loop
  over the composite kernel `M_minvec = M_Proca + M_gf` (the gauge-fixing block
  `M_gf = E (a·J)⊗(ā·J)` built independently from the geometry factors `E`,`J`
  in `gfvec_loop.py`: `geomE`, `derivsGF`, `vertexGF`, `g2_axis_gfvec`), **not**
  from any algebraic shortcut through `β_proca − β_boson`. This is why
  `R_cons ≈ 0` is an informative check rather than a tautology.

---

## (a) The identity's expected structure

On the flat lattice `det M_Proca = m²(ŝ²+m²)³` while
`det M_minvec / det Δ₀ = (ŝ²+m²)³`: they differ by the **ultralocal `m²`
longitudinal factor**. The Solodukhin identity for the induced kinetic term is
therefore claimed **at the β level** (the `m²ln m²` slope coefficient), where
the ultralocal factor contributes no propagating log — **NOT** as a pointwise
`Z` identity. Two tiers:

- **Tier 1 (recorded, characterized).** The pointwise difference
  `D(m) = Z_proca(m) − Z_gfvec(m) + Z_boson(m)` at each mass. Expectation
  (stated here, not in code): `D(m)` is smooth in `m²` with no `m²ln m²`
  content. **Registered test:** fitting `D(m)` with `fit_mlog` must yield an
  `m²ln m²` coefficient consistent with zero within the Tier-2 numerical floor
  `τ_num`.
- **Tier 2 (the audit criterion).** The dimensionless consistency residual and
  resolving-power rule of §(c1). The **numerical floor** is frozen as:

      τ_num = 1e-10 + 1e-6 · max(|β_proca|, |β_gfvec|, |β_boson|)   (baseline variant)

  **Floor-calibration allowance (frozen now):** the pilot may reveal that clean
  floating-point residue exceeds this floor; recalibrating `τ_num` upward to sit
  above measured FP residue plus margin is a legitimate pre-decisive harness
  calibration (it references no target), **provided** it is done before any
  decisive compute, recorded with the measured residue, and the recalibrated
  value re-frozen in an **amended prereg commit** — subject to the
  pilot-amendment invalidation rule (a4). **After the decisive compute begins,
  `τ_num` may not change.**
- **Tier-1↔Tier-2 machine cross-check.** Per verdict variant, fit `D(m)`
  directly (same mass set and `fit_mlog` basis as that variant) to obtain `β_D`;
  require `|β_D − (β_proca − β_gfvec + β_boson)| ≤ τ_num`. This is a
  machine-level internal consistency check (`fit_mlog` is a fixed-design linear
  least-squares, so β is a linear functional of Z and the two computations are
  algebraically identical), **not** an additional physics claim. A cross-check
  failure is a **harness defect**, not a physics result (see §(c1)
  INCONCLUSIVE).

### (a2) Extractor freeze (per species — no discretion later)

- **gfvec:** PRIMARY = bubble-only `slope_gf` / `g2_axis_gfvec` — faithful to the
  historical decisive design (`precision_campaign.py` imports `slope_gf`).
  MANDATORY **diagnostic-only** sensitivity variant = `slope_gf_v2` /
  `g2_axis_gfvec_v2` (includes the q-dependent gauge-fixed seagull); see §(c6).
  **Pointwise tolerance (its own scale, NOT the β-level `τ_num`):**

      τ_Z = 1e-10 + 1e-6 · max_m( |Z_v2(m)|, |Z_bubble(m)| )

  Pre-registered expectation: `|Z_v2(m) − Z_bubble(m)| ≤ τ_Z` at every mass. (An
  exploratory `n=6` probe suggested agreement at machine precision, `~1e-14`, but
  that probe is **exploratory, non-canonical — no branch/commit/hash/environment
  record, not independently reviewed — and is NOT adopted as evidence**; it is
  retained only as the historical motivating observation for the `τ_Z` diagnostic
  design. The pre-registered `τ_Z` expectation stands on its own as a hypothesis
  tested by the frozen harness.) Also
  record the fitted difference `β_v2 − β_bubble` relative to `|β_B^base|`. If the
  decisive configuration departs from the pointwise expectation, the finding is
  labelled **`SEAGULL-SENSITIVITY DETECTED`** — a recorded diagnostic finding
  bearing on the historical seagull-placement claim (session log R13; generator
  is MISSING #6). It is **not** an audit FAIL and **not** a harness failure; it
  must be reported prominently. By contrast, failure to *execute* the v2
  diagnostic (non-finite, source mismatch, crash) **is**
  `HARNESS INVALID / AUDIT INCONCLUSIVE`.
- **proca:** `proca_loop.slope` / `g2_axis_proca` (bubble + q→0 seagull as
  implemented).
- **boson:** `g2_axis_boson` + `fit_even`, exactly as in the historical driver.
  Note: the boson seagull is q-independent and drops from the slope; the
  gauge-fixed seagull is q-dependent, which is why the gfvec sensitivity
  diagnostic above is mandatory rather than assumed.

(The harness calls the recovered `g2_axis_*` kernels unchanged and applies the
recovered `fit_even`/`fit_mlog`; the one-line `slope*` wrappers are reproduced
faithfully inside the harness so that eps-fit diagnostics are exposed.)

### (a3) Fit-basis limitation (frozen physics choice)

The `fit_mlog` basis is `{1, m², m²ln m², m⁴}` — it contains `m⁴` but **not
`m⁴ln m²`**, precisely the longitudinal-contamination form diagnosed in R10
(heavy-window drift to `−5`). The light mass windows are therefore load-bearing:
they suppress `m⁴ln m²` leakage into the `m²ln m²` coefficient. This is frozen as
a physics choice, not discretion. Additionally register a **diagnostic-only**
check (§(c6)): fit `D(m)` and each species' `Z(m)` once with the extended basis
`{1, m², m²ln m², m⁴, m⁴ln m²}` where the point count permits (**Arm P and the
5-mass pilot only**) and record the `m⁴ln m²` coefficient — converting the
window assumption into a checked statement.

### (a4) Pilot-amendment invalidation rule (frozen)

Any preregistration amendment after a pilot (including a `τ_num` recalibration)
**invalidates all earlier pilot JSON and comparison artifacts**, because their
recorded prereg-document hash no longer matches. After the amended prereg commit,
**regenerate and recommit the complete pilot compute and pilot comparison
outputs** before any gate bookkeeping or reporting. A report may never cite pilot
artifacts whose recorded prereg hash differs from the final prereg document.

---

## (b) Configurations (from the run-record index; two decisive arms)

- **Arm H (historical reproduction, NUMREPRO):** `n=32`, species = {proca,
  boson}. Baseline window `M_H = [0.11, 0.14, 0.17, 0.20]`; shifted window
  `M_Hs = [0.12, 0.15, 0.18]`. **Arm H computes the union of baseline and
  shifted masses (7 masses total); the two fits use their separately frozen mass
  sets.** Eps grid frozen by value: `EPS_H = [0.10, 0.16, 0.22, 0.28]`.
  Question: does `β_V/β_B` land in the paper band?
- **Arm P (precision, audit + historical criterion):** `n=48`,
  `M_P = [0.05, 0.065, 0.08, 0.10, 0.12]`, `EPS_P = [0.08, 0.13, 0.18, 0.23]`
  (frozen by value), species = {proca, gfvec, boson}.

Eps grids are frozen **by value**, never by reference to a recovered module
default (which could silently change).

---

## (c) Acceptance rules (numbers live here and in `compare.py` ONLY)

### (c0) Battery uncertainty — frozen definition

For every derived quantity `X` (each ratio, and `C_cons`), the battery
uncertainty relative to the frozen baseline is the **maximum baseline deviation
over the VERDICT variants only** (classification §(c6)):

    σ_X = max_{v ∈ verdict variants, valid} | X^(v) − X^(base) |

`X^(v)` is always constructed from **paired** species results within the same
variant (numerator, denominator, and all three β's from the *same* variant).
Never compute independent per-species spreads and propagate them. Diagnostic-only
variants never enter any σ.

### (c1) Audit (Arm P) — dimensionless residual, resolving-power ceiling, three-state verdict

    C_cons^(v) = ( β_proca^(v) − β_gfvec^(v) + β_boson^(v) ) / |β_B^(v)|
    σ_C        = max over paired valid verdict variants |C_cons^(v) − C_cons^(base)|
    τ_C        = τ_num / |β_B^(base)|
    δ_audit    = 0.05                                  (frozen)

`δ_audit = 0.05` matches the historical promotion precision (5%); it forbids the
degenerate mode where a larger battery spread *widens* the acceptance tolerance
and lets an unstable computation PASS ("noisier ⇒ easier PASS").

- **PASS:** all required verdict variants valid (per (c3)); all diagnostics
  executed and valid; the Tier-1↔Tier-2 machine cross-check passes for **every**
  verdict variant; `|C_cons^(base)| ≤ max(2σ_C, τ_C)`; **and** `2σ_C ≤ δ_audit`.
- **FAIL:** all required verdict variants and diagnostics valid; the machine
  cross-check passes for every verdict variant; `|C_cons^(base)| > max(2σ_C, τ_C)`;
  **and** `2σ_C ≤ δ_audit`.
- **INCONCLUSIVE — insufficient resolving power:** all validity checks pass but
  `2σ_C > δ_audit`.
- **INCONCLUSIVE / HARNESS INVALID:** any required verdict variant invalid; any
  rank/conditioning failure; any denominator invalidity; any Tier-1↔Tier-2
  cross-check failure; any source-hash/schema/prereg-hash mismatch; any
  mutation-anchor failure; or any diagnostic that fails to execute
  (crash/non-finite/source mismatch). Labelled `HARNESS INVALID / AUDIT
  INCONCLUSIVE`; never a physics FAIL of the operator identity.
  (`SEAGULL-SENSITIVITY DETECTED` is expressly NOT in this category — §(a2)/(c6).)
- Additionally record `β_gfvec/β_B` and `β_proca/β_B` with their (c0)
  uncertainties.

### (c2) NUMREPRO (Arm H) — interval rules, no discretion

Per valid verdict variant `v` form the paired ratio `R_H^(v) = β_V^(v)/β_B^(v)`;
central value = baseline variant; `σ_H` per (c0). Band `[−3.7, −2.7]`.

- **PASS** only if all required verdict variants valid, `β_B` never crosses zero
  across variants, and `[R_H − 2σ_H, R_H + 2σ_H] ⊆ [−3.7, −2.7]`.
- **FAIL** only if all required verdict variants valid, `β_B` never crosses zero,
  and the `2σ` interval is **disjoint** from `[−3.7, −2.7]`.
- **INCONCLUSIVE** otherwise (interval straddles a boundary, any invalid variant,
  denominator issue, or conditioning limit exceeded).
- **Structural note:** unlike the audit, NUMREPRO needs no resolving-power
  ceiling — here a larger σ makes PASS *harder* (the 2σ interval must fit inside
  the band) and FAIL harder, pushing toward INCONCLUSIVE. The asymmetry is
  intentional; **do not add a ceiling here.**
- **Pre-registered honest expectation (verbatim):** `[−3.7, −2.7]` is the
  historical 1σ band, and the historical subwindows already give `−2.6`/`−3.4`
  (R10); the window-shift verdict variant alone can therefore produce
  `σ_H ≈ 0.4`, in which case the `2σ` interval exceeds the band and the verdict
  is INCONCLUSIVE **even under perfect reproduction of `−3.2(5)`**. An
  INCONCLUSIVE here would mean the historical configuration cannot distinguish
  `−3` at the pre-registered confidence — a statement about the configuration's
  discriminating power, not a failure of the identity (that is Arm P's job). **No
  band widening after seeing results.** (Per ruling A2.2 / the confound statement
  in (c4), the window-shift deviation that drives this expectation includes a
  **forced fit-basis component** — its 3-point mass set cannot support the
  4-column historical basis, so its deviation from baseline mixes window and basis
  sensitivity. This is accepted and enters `σ_H`; the expectation itself is
  unchanged.)

### (c3) Fit and variant validity — frozen numeric definitions

- A fit is **valid** only if all outputs are finite, the design-matrix rank
  equals the number of fitted columns, and its condition number is finite with
  `κ(A) ≤ 1e12`. Record rank, `κ(A)`, max residual, and `dof = n_points −
  n_columns` for every fit.
- **Exactly determined fits (`dof = 0`) are valid** provided rank and κ pass, but
  their residual diagnostic is vacuous and must be recorded as
  `dof=0 (residual vacuous)`. Fits with `n_points < n_columns` are **invalid** —
  the harness must detect and refuse them, never silently produce an
  underdetermined lstsq solution.
- **Denominator validity:** freeze
  `τ_denom = 1e-10 + 1e-6 · max(|β_proca^base|, |β_gfvec^base|, |β_B^base|)`.
  Any variant with `|β_B^(v)| ≤ τ_denom`, or whose `β_B` sign differs from
  baseline, is **invalid**.

### (c4) Per-arm frozen variant table (implement exactly; no on-the-fly combinations)

`fit_even(order=2)` has 3 columns `{1, ε², ε⁴}`; `fit_mlog(with_m4=True)` has 4
columns, `with_m4=False` has 3.

| Arm | Variant | Class | eps set | mass set | mass-fit basis | dof | Interpretation |
|---|---|---|---|---|---|---|---|
| P | baseline | VERDICT | EPS_P (4) | M_P (5) | with_m4=True | 1 | precision primary extraction |
| P | eps-drop-largest | VERDICT | EPS_P[:3] | M_P | with_m4=True | 1 | pure eps-grid sensitivity |
| P | eps-drop-smallest | VERDICT | EPS_P[1:] | M_P | with_m4=True | 1 | pure eps-grid sensitivity |
| P | fit-order | VERDICT | EPS_P | M_P | with_m4=False | 2 | pure mass-fit-basis sensitivity |
| P | mass-drop-one (×5) | VERDICT | EPS_P | M_P minus one | with_m4=True | 0 (vacuous residual) | mass-window sensitivity (basis fixed) |
| P | gfvec-v2 seagull sensitivity | DIAGNOSTIC-ONLY | EPS_P | M_P | with_m4=True | 1 | seagull-placement diagnostic |
| P | extended-basis `m⁴ln m²` | DIAGNOSTIC-ONLY | EPS_P | M_P | 5-column extended | 0 | window-assumption check |
| H | baseline | VERDICT | EPS_H (4) | M_H (4) | with_m4=True | 0 (vacuous residual) | historical primary extraction |
| H | eps-drop-largest | VERDICT | EPS_H[:3] | M_H | with_m4=True | 0 | pure eps-grid sensitivity |
| H | eps-drop-smallest | VERDICT | EPS_H[1:] | M_H | with_m4=True | 0 | pure eps-grid sensitivity |
| H | fit-order | VERDICT | EPS_H | M_H | with_m4=False | 1 | pure mass-fit-basis sensitivity |
| H | mass-drop-one (×4) | VERDICT | EPS_H | M_H minus one | with_m4=False | 0 | mixed mass-drop + reduced-basis sensitivity |
| H | window-shift | VERDICT | EPS_H | M_Hs (3) | with_m4=False | 0 | historical shifted-window extraction; also differs in basis (3 points cannot support with_m4=True) |

Eps-drop variants leave the `fit_even` eps fit exactly determined (3 pts/3 cols):
valid, `dof=0` recorded. The Arm-H drop-one and window-shift rows' forced
`with_m4=False` is a frozen consequence of the historical 3-point mass sets
(4 columns would be underdetermined: 3<4). **Had the (c3) validity rule been
applied naively, every Arm-H drop-one variant would be invalid and the verdict
structurally INCONCLUSIVE; the table above is the pre-registered resolution.**

**Ruling A2.1 — Arm-H window-shift = VERDICT variant (APPROVED, 2026-07-21).**
It is the dominant genuine systematic of the historical extraction (the R10
subwindows `−2.6`/`−3.4` are exactly this variation); excluding it from `σ_H`
would artificially shrink the NUMREPRO uncertainty and hollow out the (c2) honest
expectation — the mirror image of the diagnostic-leakage error the split exists
to prevent.

**Ruling A2.2 — historical `with_m4=True` baseline retained; mixed variants
explicitly classified (RULED, 2026-07-21).** **Arm H is a reproduction of the
historical extraction, so its baseline fit basis may not be changed merely to
make the variation battery orthogonal. The four-column `with_m4=True` baseline is
retained as the historical primary estimand.** The rejected alternative (a
uniform `with_m4=False` primary basis, proposed to remove the mass/basis
confound) is recorded as **considered and rejected** for changing the primary
estimand. Confound statement (verbatim): **"The mass-drop-one and window-shift
variants are not pure one-factor perturbations relative to the historical
baseline, because their three-point mass sets cannot support the four-column
historical basis. They are conservative mixed variants. Their deviations enter
σ_H, but may not be attributed uniquely to mass-window sensitivity or fit-basis
sensitivity. This confounding is accepted and recorded rather than removed by
changing the historical baseline. A resulting NUMREPRO INCONCLUSIVE verdict is an
honest statement that the historical extraction lacks sufficient registered
stability."**

### (c5) Historical promotion criterion (Arm P, recorded outcome, not an automatic action)

`β_gfvec/β_B ∈ [−2.10, −1.90]` **and** `β_proca/β_B ∈ [−3.15, −2.85]` (baseline
central values), with the uncertainty condition frozen as the faithful-to-history
reading: central value inside the band **and** `σ ≤ 5%` of the target magnitude
(`σ_gf/B ≤ 0.10`, `σ_P/B ≤ 0.15`), σ per (c0) over verdict variants.
**Pre-registered honest expectation (verbatim):** the historical coarse values
are `gfvec/B ≈ −2.4 … −2.9` (R12) — outside `[−2.10, −1.90]`. Arm P therefore
genuinely tests whether the fine configuration (`ma≈0.05, n=48`) pulls `gfvec/B`
to `−2.0`; a FAIL of this criterion is a live possibility and will be recorded
exactly like a PASS. Whatever comes out is recorded; any `P2-C9` promotion is a
subsequent explicit PI+reviewer step.

### (c6) Verdict variants versus diagnostic-only variants (frozen classification)

- **VERDICT variants** (and only these) define every battery uncertainty
  (`σ_C`, `σ_H`, `σ_gf/B`, `σ_P/B`) and enter every acceptance interval and
  PASS/FAIL computation: baseline; eps-drop-largest; eps-drop-smallest;
  fit-order; mass-drop-one; and (Arm H) window-shift.
- **DIAGNOSTIC-ONLY variants** are mandatory to compute and report but are
  **excluded from every σ, acceptance interval, and PASS/FAIL calculation**:
  gfvec-v2 seagull sensitivity; extended `m⁴ln m²` fits; pilot mutation anchors.
- A finite, valid difference between gfvec-v2 and bubble-only gfvec is reported as
  `SEAGULL-SENSITIVITY DETECTED` — an independent diagnostic finding, not an audit
  FAIL and not a harness failure. Failure to *execute* a diagnostic (crash,
  non-finite, source mismatch) or a mutation-anchor failure remains
  `HARNESS INVALID / AUDIT INCONCLUSIVE`.
- Rationale: a diagnostic that entered the verdict σ could widen the acceptance
  tolerance and silently flip a FAIL to PASS — a diagnostic must never be able to
  change the verdict it is diagnosing.

### (c7) Comparator-rule clarifications (Amendment 1; the code must implement these)

- **(i) Required-variant validity is not silently dropped.** Any invalid
  **required verdict variant** forces **INCONCLUSIVE** for NUMREPRO and renders
  the historical criterion **not-assessable**; invalid variants are **never**
  silently dropped to shrink σ. σ is computed only when the full required verdict
  set is valid.
- **(ii) Uniform denominator validity.** The (c3) denominator rule (magnitude
  `|β_B^(v)| > τ_denom` **and** sign consistent with baseline) applies **uniformly
  to every ratio path** — the audit `C_cons`, the Arm-H NUMREPRO ratios, and the
  Arm-P historical-criterion ratios alike.
- **(iii) Diagnostics gate the audit, by manifest.** Audit `PASS`/`FAIL` may be
  emitted **only after all required diagnostics are confirmed executed and
  valid**. Manifest rule (frozen, verbatim): **"Absence of a diagnostic required
  by the arm configuration is an execution failure, not 'not applicable'."** Each
  arm's required diagnostics are declared in a frozen `required_diagnostics`
  manifest written into the compute-output schema (see the schema addition), and
  the comparator **iterates the manifest** and validates the corresponding keyed
  record — it may **never infer completeness** from whichever optional variants
  happen to be present.

### Compute-output schema addition (Amendment 1): manifest + keyed diagnostics

Per arm the compute-output JSON adds: (1) `required_diagnostics` — the frozen list
of diagnostic IDs (Arm P and the pilot: `["gfvec-v2-seagull", "extended-basis"]`);
(2) a structured `diagnostics` mapping keyed by those IDs, each keyed record
carrying at minimum `executed` (bool), `valid` (bool), and a `record_path`
locator into the JSON. Frozen rule (verbatim): **"Every ID in
`required_diagnostics` must be a key in a structured diagnostic-results mapping.
The comparator iterates the manifest and validates the corresponding keyed
record; it may not infer completeness merely from optional variants that happen to
exist."** **Extended-basis components (frozen):** the `extended-basis` record must
declare and satisfy `required_components = [proca, gfvec, boson, D]` (with
`D = Z_P − Z_G + Z_B`); each component's extended fit must be finite, full rank,
within `κ ≤ 1e12`, with its coefficient record present. **"extended-basis valid"
means all four components valid**, never a subset. The schema version identifier
is bumped; the output-schema guard is updated. These fields name diagnostics,
never targets or ratios (no blindness change).

### Exit-code contract (Amendment 1)

The comparison output carries two top-level fields:
`integrity_status ∈ {VERIFIED, REFUSED}` and
`scientific_status ∈ {ASSESSABLE, HARNESS_INVALID}`. **Exit 0** requires
`integrity_status=VERIFIED` **and** `scientific_status=ASSESSABLE`, and covers
PASS, FAIL, and scientifically-assessable INCONCLUSIVE (insufficient resolving
power; NUMREPRO interval straddling a band boundary). **Exit non-zero** covers:
integrity REFUSED; HARNESS INVALID; any required verdict variant invalid; any
required diagnostic missing/invalid; denominator invalidity making a criterion
not-assessable; runtime/schema error. Automation must never mistake a
harness-invalid run for success.

## (d) Uncertainty/stability battery

Exactly the variant table (c4), with σ over VERDICT variants only per (c0)/(c6).
Nothing else; **no additional variants may be added after the pilot.**

## (e) Mutation anchors (pilot only, pre-registered, code-level, diagnostic-only class)

1. **gfvec wiring mutation (output-level — a harness-wiring test, not a physical
   operator mutation):** in pilot mutation mode multiply the returned
   `Z_gfvec(m)` by `1.1` before fitting; with `R = β_P − β_G + β_B`, the
   pre-registered expectation is `ΔR_cons = R_mut − R_base = −0.1·β_gfvec(base)`
   to within `τ_num` (exact because `fit_mlog` is linear in Z). Restore and
   confirm.
2. **boson sign mutation:** replace `+β_boson` with `−β_boson` in the
   combination; expectation `ΔR_cons = −2·β_boson(base)` exactly (to `τ_num`).
   Restore.

A mutation-anchor failure is `HARNESS INVALID`, never a physics result.

## (f) Determinism and cross-machine protocol

The computation contains no RNG (exact lattice sums, `slogdet`, `lstsq`); on a
fixed platform it is bit-reproducible, which is what the sha256 sidecars certify.
Arm P may run on the PI's machine with the frozen harness: its sidecar then
certifies the integrity of **that** run's outputs, not bit-level reproducibility
across machines (BLAS/FP differences preclude that). The physics verdicts are
portable because every tolerance floor (`τ_num`, `τ_denom`, `τ_Z` ≥ 1e-10) sits
far above cross-machine double-precision noise (~1e-13). Environment metadata
(platform, BLAS, versions) must be in every output JSON.

## (g) Blindness protocol

The compute stage contains **no target numbers** (`−2`, `−3`, `−3.2`, band
widths) and prints **no ratios**; it emits raw `Z(m)` tables and fitted `β` per
species/variant to frozen JSON with sha256 sidecars. The comparison stage is a
separate script (separate, later commit) that reads the frozen JSON and applies
(c). The historical files embed targets in docstrings — therefore the harness
imports their **functions** but is itself a new file. Commit chronology:
**prereg → harness → pilot compute → pilot comparison**; the decisive compute
commit (future task) must precede its comparison commit.

## Registered source set (frozen)

Source hashes recorded in the output JSON and rechecked by `compare.py` are
limited to the registered local scientific and harness sources actually governing
the computation: `proca_loop.py`, `gfvec_loop.py`, `mlog_coeff.py`,
`boson_loop.py`, `seagull_check.py`, and `harness_compute.py` — each by resolved
path. Python/NumPy/BLAS are recorded via environment metadata and are **not**
treated as repository source files.

## Gate bookkeeping this task performs (no outcomes)

- `P2-BETAV-NUMREPRO-01`: `PROPOSED → SPECIFIED` (rules registered here; not run).
- `P2-BETAV-CIRC-01`: stays `SPECIFIED`; registered-test field points to
  §(c1)/§(c4)/§(c6)/§(e) and the scope statement above.
- `P2-C9`, `−3.2(5)` quarantine: untouched. A future audit PASS **alone** cannot
  flip the quarantine (dual-gate rule; enforced by the governance suite).

---

## Amendment 1 — 2026-07-22 (audit trail)

This amendment edits the frozen text **in place** above; this section is the
audit trail listing each change and its reason. **It triggers rule (a4):** all
pilot artifacts from commit `db002d7` are invalidated (their recorded prereg-doc
hash no longer matches) and are regenerated under the amended prereg. The
original campaign report keeps its `2026-07-21` filename (this round appends to
it); this amendment section carries the actual execution date 2026-07-22.

- **A1 — pilot eps-grid fix (the (a4) trigger) [APPROVED].** `EPS_pilot` is set
  to **four** points `[0.10, 0.16, 0.22, 0.28]` (identical to `EPS_H`), so the
  pilot exercises the decisive-shaped eps-drop variants (drop-one → 3 pts / 3
  cols, `dof=0`, valid). *Reason/defect:* the previous 3-eps grid made both
  eps-drop verdict variants necessarily underdetermined, so the pilot could only
  reach `HARNESS INVALID` and never validated the valid-path battery. (The pilot
  config lives in `harness_compute.py` `CONFIG["pilot"]`; this amendment records
  the frozen value.)
- **A2.1 — Arm-H window-shift = VERDICT variant [APPROVED, ruling recorded].**
  Markers removed; see (c4) ruling A2.1. *Reason:* the R10 `−2.6`/`−3.4` drift is
  the dominant historical systematic; excluding it would shrink `σ_H` and hollow
  out the (c2) expectation.
- **A2.2 — historical `with_m4=True` baseline retained; mixed variants
  classified [RULED].** The (c4) Arm-H rows are replaced with the ruled table
  (Interpretation column); the retained-baseline rationale and the confound
  statement are recorded verbatim; the rejected uniform-`with_m4=False`
  alternative is recorded as considered and rejected. The (c2) expectation now
  notes the forced fit-basis component (expectation unchanged).
- **A3.1 — three-output canonical wording [APPROVED].** Added to the scope
  statements: three distinct recorded outputs never conflated; "CIRC PASS +
  NUMREPRO PASS is necessary but not sufficient"; "No script automatically
  promotes the claim."
- **A3.2 — n=6 probe downgraded [APPROVED].** The exploratory `n=6` probe is
  reclassified non-canonical and **not adopted as evidence** (§(a2)); it is
  retained only as the motivating observation for the `τ_Z` diagnostic design.
- **A4 — comparator-rule clarifications [APPROVED].** New §(c7): (i)
  required-variant validity is never silently dropped; (ii) uniform `τ_denom`
  denominator validity on every ratio path; (iii) diagnostics gate the audit via
  a frozen `required_diagnostics` manifest ("absence = execution failure, not
  'not applicable'"). Plus the compute-output schema addition (manifest + keyed
  `diagnostics`, extended-basis four-component rule, schema-version bump) and the
  `integrity_status`/`scientific_status` + exit-code contract.

All markers ("ChatGPT to confirm", "reviewer-flagged") are removed from the
frozen text; the rulings above are now recorded facts. No target numbers, bands,
or ratios were added to any blind-compute path. Decisive runs remain out of scope.
