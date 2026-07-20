# Gate Registry

Allowed statuses: `PROPOSED`, `SPECIFIED`, `RUNNING`, `PASS`, `FAIL`,
`INCONCLUSIVE`, `SUSPENDED`, and `RETIRED`.

These gates were run as an **independent verification** (no legacy source; see
`MIGRATION.md`). A gate is `PASS`/`FAIL`/`INCONCLUSIVE` only for the
*recomputation*; none is reviewer-accepted, so none promotes a claim to
`VERIFIED`.

## P2-HK-01 — Heat-kernel species coefficients

Status: INCONCLUSIVE (bosonic sub-results PASS; fermionic `β_F` disagrees ×2)

### Scientific question
The `m²ln m²` coefficient `β_s` of the induced Einstein–Hilbert term `Z(m²)`
for each species, and the ratios `β_F/β_B`, `β_V/β_B`, `β_B(ξ)/β_B`.

### Scope
Real scalar (minimal), non-minimal scalar `ξ`, Dirac fermion, Proca vector.
One-loop, flat background, `m²ln m²` (log) coefficient only.

### Locked assumptions
`CONVENTIONS.md`: `Δ=−∇²+E`, `a_1=(1/6)R·𝟙−E`; boson `p=+½` per `det^{−1/2}`,
fermion/`det^{+1/2}` `p=−½`; Dirac `E=R/4·𝟙₄`; Proca
`det^{−1/2}(Δ^{(1)})det^{+1/2}(Δ^{(0)})`.

### Inputs
Seeley–DeWitt `a_1`; bundle traces (`dim`, `tr E/R`) per species.

### Analytic anchors
`a_1=(1/6)R·𝟙−E`; `tr a_1=+R/6` (scalar), `−R/3` (Dirac), and the Proca
per-factor traces `−R/3` (vector) `+R/6` (scalar). Second route: proper-time
incomplete-gamma integral gives `m²ln m²` coefficient `+1`.

### Regression anchors
`scripts/hk_species.py`: `beta("scalar_min")=−1/(192π²)`, `beta("dirac")=
−1/(96π²)`, `beta("proca")=+1/(64π²)`, ratios `(2,−3,1−6ξ)`,
`proper_time_log_coefficient()=1`.

### Kill criterion
Any ratio not an exact rational, or the proper-time route disagreeing with the
`a_1` route.

### Required computations
Symbolic `a_1` traces, `β_s`, ratios; second-route cross-check. Done.

### Required deliverables
`derivations/P2-HK-01_heat_kernel_species.md`, `scripts/hk_species.py`,
`results/P2-HK-01/`.

### Result
`β_B=−1/(192π²)`, `β_B(ξ)=−(1−6ξ)/(192π²)`, `β_F=−1/(96π²)`, `β_V=+1/(64π²)`;
`β_F/β_B=2`, `β_V/β_B=−3`, `β_B(ξ)/β_B=1−6ξ`. Second route: `+1`.

### Reviewer verdict
Pending. All coefficients and ratios **agree** with the paper once the uniform
`Z` normalization is matched (`P2-NORM-01`): paper `β_B^cont=1/(384π²)`,
`β_F=2β_B`, `β_V=−3β_B`. The first report's D1 (Weyl-vs-Dirac) is **withdrawn**
— it compared across `Z` normalizations.

### Consequences
The uniform factor 2 is a `Z` definition (`P2-NORM-01`); it cancels in all ratios
and does not affect the physics.

### Repository branch
`claude/paper-2-independent-verification-dysdp0`

### Relevant files
`scripts/hk_species.py`, `derivations/P2-HK-01_heat_kernel_species.md`,
`results/P2-HK-01/`.

### Date opened
2026-07-17

### Date closed
2026-07-17 (recomputation; reviewer adjudication pending)

## P2-GAP-01 — Gap-equation criticality (continuum + lattice)

Status: PASS (continuum exact; lattice `I_0` agrees with paper at matched mass)

### Scientific question
Critical scalar-channel coupling `G_c` from the leading-order gap equation,
continuum (sharp 4-ball) and lattice (Wilson `r=1`); derive `G_c=1/(2I_0)`.

### Scope
Mean-field / effective-potential (gap-equation) criticality, **not** channel
bubbles.

### Locked assumptions
`CONVENTIONS.md`; channel-coupling normalization (Dirac trace absorbed), so the
gap equation is `1=2G_cI_0`.

### Inputs
Untraced scalar bubble `I_0=∫1/D` at the chiral point; `D=p²` (continuum),
`D=Σsin²p+W²`, `W=Σ(1−cos p)` (lattice).

### Analytic anchors
Continuum `I_0=Λ²/(16π²)`, `G_c=8π²/Λ²` (`c=8` exact).

### Regression anchors
`scripts/gap_criticality.py`: `continuum_c()=8`, `continuum_I0(1)=1/(16π²)`;
`lattice_I0(n=128)≈0.085386`.

### Kill criterion
Continuum `c≠8`; lattice `I_0` not converging under grid refinement, or
straight/offset grids disagreeing above 1%.

### Required computations
Symbolic continuum; BZ quadrature lattice with grid-refinement and offset-grid
cross-check. Done.

### Required deliverables
`derivations/P2-GAP-01_gap_criticality.md`, `scripts/gap_criticality.py`,
`results/P2-GAP-01/`.

### Result
Continuum `G_c=8π²/Λ²` (`c=8`). Lattice massless `I_0=0.085388(20)`,
`G_c=5.856`. At the paper's reference mass `ma=0.02`: `I_0=0.084341` (inf-vol),
`0.084465` (`64⁴`), `G_c=5.928` — matching the paper's `0.0844`/`0.0845`/`5.93`
to `<0.1%`.

### Reviewer verdict
Pending. Continuum matches paper (`8π²`). Lattice `I_0` **agrees** with the paper
at matched evaluation mass (`ma=0.02`); the first report's ≈1.2% "D2 gap" was a
massless-vs-`ma=0.02` definition difference, now withdrawn.

### Consequences
`G_c` feeds `4G_cβ_F`. The Wilson chiral-breaking subtlety is flagged.

### Repository branch
`claude/paper-2-independent-verification-dysdp0`

### Relevant files
`scripts/gap_criticality.py`, `derivations/P2-GAP-01_gap_criticality.md`,
`results/P2-GAP-01/`.

### Date opened
2026-07-17

### Date closed
2026-07-17 (recomputation; reviewer adjudication pending)

## P2-BETA-01 — Lattice mass-scan extraction of `β_B`

Status: PASS (recomputation; consistent with continuum and paper's "5%")

### Scientific question
Extract `β_B` (coefficient of `m²ln m²` in `Z(m²)`) for a minimal scalar from a
lattice mass scan, with honest self-derived systematics.

### Scope
Infinite-volume BZ tadpole `Z=(1/12)∫1/(p̂²+m²)`, fit over `m∈[0.125,0.55]`.

### Locked assumptions
`CONVENTIONS.md`; `p̂²=Σ4sin²(p/2)`; fit basis `{1,m²,m²ln m²,m⁴}`.

### Inputs
`Z_lat(m²)`; fit window; ansatz; finite-`L` volumes for the convergence trend.

### Analytic anchors
Continuum `β_B=1/(192π²)=5.28e-4` (from `P2-HK-01`); raw tadpole coefficient
`1/(16π²)`.

### Regression anchors
`scripts/lattice_beta_scan.py`: `beta_central≈5.44e-4`; primary spread
`≈5.0e-5`; volume trend converging to `Linf`.

### Kill criterion
Fitted `β_B` not converging with volume, or primary systematics exceeding the
continuum value by more than the spread.

### Required computations
BZ tadpole scan + linear fit + window/ansatz/volume systematics. Done.

### Required deliverables
`derivations/P2-BETA-01_lattice_mass_scan.md`,
`scripts/lattice_beta_scan.py`, `results/P2-BETA-01/`.

### Result
`β_B=5.44e-4` (primary spread `±0.5e-4`), `+3.1%` above continuum; volume trend
`L=24,32,48,∞ → 6.99,5.73,5.45,5.44 e-4`.

### Reviewer verdict
Pending. Consistent with continuum at the few-percent level (better than the
paper's stated 5%).

### Consequences
Confirms the lattice reproduces the IR-universal log coefficient.

### Repository branch
`claude/paper-2-independent-verification-dysdp0`

### Relevant files
`scripts/lattice_beta_scan.py`, `derivations/P2-BETA-01_lattice_mass_scan.md`,
`results/P2-BETA-01/`.

### Date opened
2026-07-17

### Date closed
2026-07-17 (recomputation; reviewer adjudication pending)

## P2-BETAV-01 — Lattice `β_V/β_B` (Proca / Stueckelberg)

Status: PROPOSED (deferred — not computed this sweep)

### Scientific question
The lattice `β_V/β_B` for the Proca loop with Stueckelberg decomposition; the
paper reports `−3.2(5)` vs analytic `−3`, attributing the gap to longitudinal-
sector lattice artifacts.

### Scope
Massive vector on the lattice, induced graviton coefficient including the
longitudinal (Stueckelberg) modes.

### Locked assumptions
`CONVENTIONS.md`; Proca determinant structure.

### Inputs
Lattice vector propagator with longitudinal modes; weak-field / curved
background to expose the `a_1` `R` coefficient.

### Analytic anchors
`β_V/β_B=−3` (from `P2-HK-01`).

### Regression anchors
None yet (not computed).

### Kill criterion
Extraction unstable ⟹ report the instability, not a number (per the task).

### Required computations
Deferred. A flat-space tadpole would only reproduce the analytic `−3` (the
loop integral is species-independent in flat space); a genuine test needs a
curved/weak-field lattice graviton self-energy.

### Required deliverables
Pending a dedicated sweep.

### Result
Not computed. Paper value `−3.2(5)` has paper-text-only provenance.

### Reviewer verdict
N/A (not run).

### Consequences
None yet.

### Repository branch
`claude/paper-2-independent-verification-dysdp0`

### Relevant files
`results/comparison/PAPER_COMPARISON.md` (rationale for deferral).

### Date opened
2026-07-17

### Date closed
Open (deferred).

## P2-NORM-01 — Locate the `β`/`G` normalization factor 2

Status: PASS (bookkeeping resolved; outcome (a))

### Scientific question
The first report's D1 (`β_F` Weyl-vs-Dirac) and the `4G_cβ_F` `1/3`-vs-`1/6`
were flagged as disagreements. Are they physics, or a normalization convention?

### Scope
The chain `Z → β_s → 4G_cβ_F → ξ_ind`, both this repo's and the paper's.

### Locked assumptions
`CONVENTIONS.md`; `P2-HK-01` `β_s`; `P2-GAP-01` `G_c=8π²`.

### Inputs
This repo's `Z` = coeff of `R` in the action; paper's `Z` = axis-TT slope per
unit `4N` (lines 1209–1210).

### Analytic anchors
`R_Z = 2` uniform across species; `4G_cβ_F = 1/6` (paper `Z`), `1/3` (this `Z`).

### Regression anchors
`scripts/normalization_chain.py`: per-species ratio `2.0`; `four_Gc_betaF`.

### Kill criterion
`R_Z` not uniform across species ⟹ the factor 2 would be physics, not
convention.

### Required computations
Express both chains in one convention; locate the step. Done.

### Required deliverables
`derivations/P2-NORM-01_normalization_chain.md`,
`scripts/normalization_chain.py`, `results/P2-NORM-01/`.

### Result
Outcome **(a)**: same theory, different `Z` normalization. The factor 2 enters
at the definition of `Z`, uniform across all species (verified `R_Z=2` for
scalar/Dirac/Proca). The paper's `4G_cβ_F=1/6` is self-consistent; the report's
`1/3` was convention-mixing (retracted). Residual (c) element: the axis-TT-slope
normalization + `G=Ny²=G_c` map is taken on the paper's word (not text-derivable
to the factor-of-2 level).

### Reviewer verdict
Pending. Physics unchanged: `ξ_ind<0` for `L≫1` either way; only the survival
boundary moves (`0.37Λ` vs `0.29Λ`), both unattainable on the lattice.

### Consequences
D1 withdrawn; `P2-C2`, `P2-C8` → `SUPPORTED`. Bookkeeping gate; not physics.

### Repository branch
`claude/paper-2-independent-verification-dysdp0`

### Relevant files
`scripts/normalization_chain.py`, `derivations/P2-NORM-01_normalization_chain.md`,
`results/P2-NORM-01/`.

### Date opened
2026-07-17

### Date closed
2026-07-17 (recomputation; reviewer adjudication pending)

## P2-BETAV-CIRC-01 — Does the lattice `β_V` test discriminate?

Status: OPEN (analytic layer PASS; full lattice reproduction not run)

### Scientific question
Can Paper 2 Finding 5's lattice extraction distinguish `β_V/β_B=−3` from
anything else, or would it return `−3` regardless (circular confirmation)?

### Scope
The discriminating power of the extraction, not reproducing `−3.2(5)`.

### Locked assumptions
`CONVENTIONS.md`; Proca determinant structure, generalized to a compensating
scalar power `k`.

### Inputs
Modified structure `det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)^k`.

### Analytic anchors
`β_V(k)/β_B = −(k+2)` (`k=1→−3`, `k=2→−4`, `k=3→−5`).

### Regression anchors
`scripts/betav_discriminating.py`: closed form `−(k+2)`; `k=1→−3`;
discriminating (`k=1≠k=2`).

### Kill criterion
Feed the paper's *lattice* extraction the `k≠1` structure. **If it returns `−3`
regardless, the extraction is circular and Finding 5's lattice confirmation is
withdrawn.** If it returns `−(k+2)`, it discriminates.

### Required computations
Analytic discriminating test: done (target is structure-dependent, so not
degenerate). Full curved-background lattice Proca with numerical `h`-derivatives:
**not run** — a substantial implementation. Blocks: reproducing `√g g⁻¹⊗g⁻¹`
metric-coupled lattice Proca operator, numerical `h`-derivative extraction, and
the longitudinal-artifact model.

### Required deliverables
`derivations/betav_discriminating_power.md`, `scripts/betav_discriminating.py`,
`results/P2-BETAV-CIRC-01/`; full lattice pipeline pending.

### Result
Analytic layer: the target `β_V/β_B` is structure-dependent `−(k+2)`, so the
extraction is **not** degenerate/circular at the coefficient level; Finding 5 is
a legitimate numerical-vs-analytic cross-check *given* the Proca structure. It
does not independently establish the structure. Note: the paper's own heavy-mass
drift "to ratios near `−5`" equals the `k=3` value — consistent with a
longitudinal artifact mimicking an extra compensating power.

### Reviewer verdict
Not closed by assertion in either direction; `OPEN` pending the full lattice
reproduction.

### Consequences
Cross-repo: `3-vector-sector` (`P3-C-004`, `VERIFIED`) quotes `−3.2(5)`; flagged
in `MIGRATION.md`, that repo not edited.

### Repository branch
`claude/paper-2-independent-verification-dysdp0`

### Relevant files
`scripts/betav_discriminating.py`, `derivations/betav_discriminating_power.md`,
`results/P2-BETAV-CIRC-01/`, `MIGRATION.md`.

### Date opened
2026-07-17

### Date closed
Open.

## Sea–Ice programme gate stubs (PROPOSED)

The gates below are **stubs** created from the programme Sea–Ice research map
(`0-programme:sea-ice/SEA_ICE_RESEARCH_MAP.md`, snapshot 2026-07-19,
re-confirmed against this `GATES.md` before creation — no ID collision with
`P2-HK-01`, `P2-GAP-01`, `P2-BETA-01`, `P2-BETAV-01`, `P2-NORM-01`,
`P2-BETAV-CIRC-01`). Each is the real, paper-owned object behind a Sea–Ice
`SI-x` routing alias; the programme repo owns no evidence.

**CLAIMS↔GATES note.** These gate IDs have **no** claim rows in `CLAIMS.md`
yet, and none is added here. A claim appears only when a gate is actually
run. The CLAIMS↔GATES guard (`tests/test_repository_structure.py ::
test_every_cited_gate_id_has_a_gates_heading`) checks the CLAIMS→GATES
direction only — every gate ID *cited in* `CLAIMS.md` must have a heading
here — so a gate with no backing claim is tolerated and the guard is not
weakened.

## P2-CHANNEL-FREEZE-01 — Freeze the HS/Fierz channel basis + SI-2 metrics

Status: PROPOSED

### Sea–Ice alias
SI-1 (pre-requisite freeze). Owner: Paper 2.

### Scientific question
Freeze the complete Hubbard–Stratonovich / Fierz channel basis and the SI-2
CLEAN-PASS metric before any multiphase scan. This is a **freeze, not a
test** — there is no PASS/FAIL — but `P2-MULTIPHASE-GRAV-01` (SI-2) may not
run until this freeze is committed with a hash.

### Scope
The complete independent bilinear basis (scalar, pseudoscalar, vector, axial,
tensor as the interaction's symmetry dictates), the Fierz identities relating
them, the channels included in / excluded from `K_ij` (with reason), and the
pre-registered SI-2 CLEAN-PASS metric (parameter space, measure, minimum
healthy volume, perturbation magnitude). Per pre-registration policy §1 and §3.

### Locked assumptions
`CONVENTIONS.md`; the fixed four-fermion interaction of the existing
lattice-fermion theory (verbatim in the freeze document).

### Inputs
The original four-fermion interaction; the complete bilinear basis; the Fierz
identities.

### Dependency
Depends on `P2-BETAV-CIRC-01` (SI-0). Feeds `P2-PHASE-01` (SI-1) and
`P2-MULTIPHASE-GRAV-01` (SI-2).

### Kill criterion
None (a freeze, not a test). Operational rule: `P2-MULTIPHASE-GRAV-01` is not
admissible evidence until this freeze is committed first (policy §1). After
the freeze, adding a channel is an extension (AE-4), not a continuation.

### Required computations
(not started)

### Required deliverables
The channel/metric freeze document, committed with a commit hash (policy §1,
§3), before the SI-2 scan.

### Result
(not started)

### Reviewer verdict
(not started)

### Consequences
Fixes the `∀`-phase quantifier for the SI-2 death gate; without it SI-2 can
be postponed indefinitely by appending one more channel.

### Repository branch
`sea-ice/gate-stubs`

### Relevant files
`0-programme:sea-ice/SEA_ICE_RESEARCH_MAP.md`,
`0-programme:sea-ice/SEA_ICE_PREREGISTRATION_POLICY.md`.

### Date opened
2026-07-20

### Date closed
Open (PROPOSED stub).

## P2-PHASE-01 — Admissible stable condensed phase (the Ice)

Status: PROPOSED

### Sea–Ice alias
SI-1. Owner: Paper 2.

### Scientific question
Does the fixed lattice-fermion theory possess ≥1 physically admissible stable
condensed phase (the Ice)?

### Scope
Stationary solutions `δΓ/δΦ_i = 0` of the full effective action, with all
condensates drawn from the frozen channels, at finite density / `μ`, within
the pre-registered microscopic parameter domain (policy §2, §4).

### Locked assumptions
`CONVENTIONS.md`; the frozen channel basis and parameter domain from
`P2-CHANNEL-FREEZE-01`.

### Inputs
Frozen channels; `Γ[Φ_i]`; finite density / `μ`.

### Dependency
Depends on `P2-CHANNEL-FREEZE-01`. Feeds `P2-MULTIPHASE-GRAV-01` (SI-2).

### Kill criterion
No admissible phase anywhere in the frozen space → the simplest Sea–Ice
framework terminates.

### Required computations
(not started)

### Required deliverables
(not started)

### Result
(not started)

### Reviewer verdict
(not started)

### Consequences
Supplies the admissible-phase list scanned by the SI-2 death gate.

### Repository branch
`sea-ice/gate-stubs`

### Relevant files
`0-programme:sea-ice/SEA_ICE_RESEARCH_MAP.md`.

### Date opened
2026-07-20

### Date closed
Open (PROPOSED stub).

## P2-MULTIPHASE-GRAV-01 — Programme-death: does any phase give healthy gravity?

Status: PROPOSED

### Sea–Ice alias
SI-2 (**programme-death gate**). Owner: Paper 2 (primary), Paper 3
(dependency).

### Scientific question
Does *any* admissible stable phase produce healthy gravity?

### Scope
Every phase from `P2-PHASE-01`; the full `K_ij(p)` including all
frozen-channel mixing; Paper 3 vector input. Verdict is one of three
pre-registered tiers (below).

### Locked assumptions
`CONVENTIONS.md`; the frozen channel basis, parameter domain, and CLEAN-PASS
metric from `P2-CHANNEL-FREEZE-01` (registered before the scan, per AE-3).

### Inputs
Every admissible phase from `P2-PHASE-01`; full `K_ij(p)` incl. all
frozen-channel mixing; **Paper 3 vector input to `K_ij`** (constrained
interaction sector, not a rescue branch).

### Dependency
Depends on `P2-PHASE-01` (and the `P2-CHANNEL-FREEZE-01` freeze). Paper 3
enters only as an interaction input to `K_ij(p)`. Feeds `P4-SEA-ICE-01`
(SI-3).

### PASS classification (verbatim from the research map)
`P2-MULTIPHASE-GRAV-01` returns one of three verdicts; the distinguishing
thresholds are themselves pre-registered.

- **CLEAN PASS** — a healthy phase exists on a parameter region of
  **positive volume** under the *pre-registered measure*, at least the
  *pre-registered minimum healthy volume*, and stable under small parameter
  perturbation. Only CLEAN PASS supports continuing into Sea–Ice cosmology.
- **CONDITIONAL PASS (fine-tuned)** — a healthy phase exists only at an
  isolated point, on a zero-measure surface, in a tuning band narrower than
  the registered minimum, or requires fine cancellation. Permits technical
  follow-up; **must not** be written as a theoretical success.
- **FAIL** — every admissible phase is gravitationally pathological
  (negative Newtonian coupling, negative-residue physical pole, unavoidable
  ghost or tachyon, or no viable long-range mode). Hard consequence per AE-1.

### Kill criterion
`∀ Φ: ¬HealthyGravity(Φ)` → **simplest lattice-fermion Sea–Ice programme
terminated** (FAIL tier above).

### Honest prior
SI-2 does not start neutral. The minimal single-channel induced-gravity
result gives `ξ_ind < 0` for `L ≫ 1`, and the one computed vector channel is
repulsive (`G_ω = -G/N`, Paper 3 `P3-C-001`). A repulsive vector entering
the graviton kernel is a **headwind** for a healthy Newtonian limit, not a
help: SI-2 is more likely to fail than to pass.

### Required computations
(not started)

### Required deliverables
(not started)

### Result
(not started)

### Reviewer verdict
(not started)

### Consequences
CLEAN PASS is the only verdict that supports continuing into Sea–Ice
cosmology (`P4-SEA-ICE-01` onward). FAIL terminates the simplest framework
(AE-1).

### Repository branch
`sea-ice/gate-stubs`

### Relevant files
`0-programme:sea-ice/SEA_ICE_RESEARCH_MAP.md`,
`0-programme:sea-ice/SEA_ICE_PHYSICAL_FRAMEWORK.md`,
`0-programme:sea-ice/SEA_ICE_PREREGISTRATION_POLICY.md`.

### Date opened
2026-07-20

### Date closed
Open (PROPOSED stub).

## Gate template

```markdown
## <ID> — <title>

Status: PROPOSED

### Scientific question
### Scope
### Locked assumptions
### Inputs
### Analytic anchors
### Regression anchors
### Kill criterion
### Required computations
### Required deliverables
### Result
### Reviewer verdict
### Consequences
### Repository branch
### Relevant files
### Date opened
### Date closed
```
