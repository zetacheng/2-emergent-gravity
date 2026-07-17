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
Pending. `β_V/β_B=−3` and `β_B` match the paper; `β_F` disagrees by exactly a
factor 2 (Dirac vs Weyl) — see `results/comparison/PAPER_COMPARISON.md` D1.

### Consequences
The `β_F` factor-2 propagates to `4G_cβ_F` (`1/3` vs `1/6`) and the survival
window (`m>0.287Λ` vs `0.368Λ`).

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

Status: INCONCLUSIVE (continuum PASS exact; lattice `I_0` disagrees ≈1.2%)

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
Continuum `G_c=8π²/Λ²` (`c=8`). Lattice `I_0=0.085388(20)`, `G_c=5.856`.

### Reviewer verdict
Pending. Continuum matches paper (`8π²`). Lattice `I_0` differs from paper's
`0.0844` by ≈1.2%, outside my numerical uncertainty — see PAPER_COMPARISON D2.

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
