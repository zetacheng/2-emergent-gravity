# Gate Registry

Allowed statuses: `PROPOSED`, `SPECIFIED`, `RUNNING`, `RUN`, `PASS`, `FAIL`,
`INCONCLUSIVE`, `SUSPENDED`, and `RETIRED`. (`RUN` = the registered test
executed; the outcome is carried in a separate `Verdict:` field, never folded
into the status.)

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

Status: SPECIFIED
Phase-1 design adjudication: DECOMP-UNAVAILABLE-AS-RECOVERED
Previous additive k-scan design: WITHDRAWN
Current registered test: operator/determinant-identity audit — **rules now
  pre-registered** in `derivations/P2-BETAV-CAMPAIGN_prereg.md` §(c1) (three-state
  PASS/FAIL/INCONCLUSIVE with dimensionless residual `C_cons` and resolving-power
  ceiling `δ_audit=0.05`), §(c4) (frozen variant table), §(c6)
  (verdict/diagnostic classification), §(e) (mutation anchors). Object: the
  Solodukhin quotient `Γ_Proca = Γ_minvec − Γ_scalar` as implemented in
  `gfvec_loop.py`, via `R_cons = β_proca − β_gfvec + β_boson = 0`. Blind harness
  built and pilot-validated (`scripts/P2-BETAV-CAMPAIGN/`); **the decisive Arm-P
  run is a separate, subsequently authorized task.** Scope: an audit PASS
  establishes the operators obey the claimed determinant identity (correct `−3`
  multiplicity bookkeeping); per Phase-1 every pipeline step is linear, so it
  **cannot** establish strong historical non-circularity, and a CIRC audit PASS
  **alone does not verify or promote** `β_V/β_B = −3.2(5)`.

**Adjudication note (design, not a CIRC verdict).** This gate was `SUSPENDED`
while the historical Finding 5 pipeline was missing; the pipeline is now
**recovered** (`scripts/recovered_2026/proca_loop.py` + `mlog_coeff.py`) and
**runs**, reproducing the scalar `β_B` and the vector `β_V` sign
(`results/recovered-2026/BETAV_REPRODUCTION.md`), so the gate is `SPECIFIED`. A
Phase-1 determinant-decomposition adjudication
(`derivations/P2-BETAV-CIRC-01_determinant-decomposition.md`) then found the
originally-proposed additive `Z_Proca + k·Z_scalar` k-scan **invalid as
recovered** (`DECOMP-UNAVAILABLE-AS-RECOVERED`): the recovered `boson_loop`
scalar (`Δ₀=ŝ²+m²`, propagating) is **not** the flat Proca longitudinal
eigenfactor (`m²`, ultralocal) and cannot be substituted without an extra
operator identity; and the additive scan would in any case be `LINEAR-ONLY`. A
`q²`-level sector decomposition shows the transverse/longitudinal split is only
*approximately* invariant (a small, `≈0.4%`, nonzero mixed `q²` term). A
clean-room lattice Stueckelberg / gauge-fixed construction is **not excluded**.
The CIRC gate has **not** passed or failed; the next step is an operator/
determinant-identity audit or `P2-BETAV-RECON-01`, **not** the withdrawn k-scan.
`P2-BETAV-ASSEMBLY-01` (bookkeeping) and `P2-BETAV-RECON-01` (PROPOSED) remain as
recorded.

### Addendum — 2026-07-21 (batch-2 recovery; no status change, Phase-1 verdict intact)

The Phase-1 adjudication (`DECOMP-UNAVAILABLE-AS-RECOVERED`) stated that a
clean-room lattice Stueckelberg / gauge-fixed construction was **not excluded**
but was **unavailable from the then-recovered set**. The batch-2 recovery shows
such a construction **existed historically**: `scripts/recovered_2026/batch2/gfvec_loop.py`
implements a gauge-fixed **minimal** lattice vector via the explicit determinant
identity `Γ_Proca = Γ_minvec − Γ_scalar(m)` (hence `β_V = β_gfvec − β_B`),
including a constant-`h` validation harness and a `q`-dependent gauge-fixed
seagull (v2). Its machinery is validated (constant-`h`: perturbative
bubble+seagull vs exact `ln det` agree to `~1e-7`, `n=6,8`, `m=0.5`;
`results/recovered-2026/BATCH2_VALIDATION.md`).

Consequences for the **registered test** (operator/determinant-identity audit):

- it now has a **concrete recovered object** — the Solodukhin determinant
  quotient as implemented in `gfvec_loop.py`. The audit will examine this
  identity at the operator level and via the consistency relation
  `β_proca − (β_gfvec − β_boson) = 0` (pre-encoded in
  `scripts/recovered_2026/batch2/precision_campaign.py`);
- **PASS/FAIL/INCONCLUSIVE rules remain to be pre-registered before any run.**
  Any β-extraction run **must** use a **blind harness**: the historical drivers
  embed the analytic targets (`−2.000`, `−3.000`, consistency `0`) in
  comments/docstrings, so the target must be stripped from the driver and the
  number frozen before any comparison;
- **this does not reopen or overturn the Phase-1 verdict or its token** — the
  verdict `DECOMP-UNAVAILABLE-AS-RECOVERED` was correct **for the then-recovered
  set** (the additive `Z_Proca + k·Z_scalar` scan on `proca_loop`/`boson_loop`).
  What batch-2 changes is that the *reformulated* operator-identity audit now has
  an object to run against; the additive k-scan stays **withdrawn**.

Status stays **`SPECIFIED`**; `P2-BETAV-NUMREPRO-01` stays `PROPOSED`; `P2-C9`
and the `β_V/β_B = −3.2(5)` quarantine are **untouched**.

**Ward summary — recorded, not adopted.** `results/recovered-2026/ward_analysis_summary.txt`
(the Ward-complete vierbein-link graviton-kernel results document) is recorded
as a **historical results document whose claims are recorded, not adopted**. Its
central claims — the covariant kinetic coefficient is **negative**
(`Z_cov < 0`), and the earlier positive axis slope was **entirely** the
non-covariant hypercubic `c4` piece — bear directly on the `M_Pl²` sign question
and SI-2 priors, **but the generating code (the Ward-complete vierbein-link
kernel) is not recovered and the claims are unverified**
(`scripts/recovered_2026/MISSING.md`, item 1). **No gate, paper text, or prior
may cite these as established** until the generating computation is recovered or
independently reproduced.

### Scientific question
Can Paper 2 Finding 5's lattice extraction distinguish `β_V/β_B=−3` from
anything else, or would it return `−3` regardless (circular confirmation)?

### Scope
The discriminating power of the extraction, not reproducing `−3.2(5)`.

**Scope (promotion boundary):** this gate tests only non-circularity /
discriminating power. A PASS does **not** verify or promote
`β_V/β_B = −3.2(5)`. Promotion of `P2-C9` requires **both**:
- `P2-BETAV-CIRC-01 = PASS`; **and**
- `P2-BETAV-NUMREPRO-01 = PASS`.

### Locked assumptions
`CONVENTIONS.md`; the **recovered non-minimal Proca operator** `M[h]`
(`scripts/recovered_2026/proca_loop.py`) as the object under audit. The external
`boson_loop` scalar (`Δ₀=ŝ²+m²`, propagating) is **not** assumed equivalent to
the longitudinal spectral factor (`m²`, ultralocal) of `M[h]`; any such
equivalence must be demonstrated, not assumed.

### Inputs
The recovered operator `M[h]` and its metric variations; the continuum
gauge-fixed / Stueckelberg determinant identity
`det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)` (where the analytic `−3` lives);
and any proposed **lattice** realization of that identity to be checked against
`M[h]`.

### Analytic anchors
The continuum gauge-fixed / Stueckelberg quotient supplies the analytic `−3`
target; the recovered lattice operator `M[h]` supplies the object it must be
matched against. (The withdrawn additive `k`-scan's `β_V(k)/β_B=−(k+2)`
relation is recorded in the superseded block below and is **not** a live anchor.)

### Regression anchors
`scripts/recovered_2026/reproduce_betav.py` (pipeline runs; scalar `β_B` and
vector sign reproduce); `scripts/betav_decomp_check.py` (flat eigenstructure and
`Δ₀`-vs-`m²` operator comparison); `scripts/betav_decomp_q2.py` (`q²`-level
sector decomposition). The bookkeeping anchor lives in `P2-BETAV-ASSEMBLY-01`.

### Kill criterion
For the **operator/determinant-identity audit** (rules to be pre-registered
before it runs): the audit fails if no explicit lattice gauge-fixed operator can
be written down; if there is no consistent Jacobian / ghost determinant for the
gauge fixing; if the identity fails at the physical point; or if the proposed
identity cannot reproduce the recovered `M[h]` metric variations.

### Required computations
Pre-register (PASS / FAIL / INCONCLUSIVE rules fixed **before** execution) and
run the operator/determinant-identity audit: whether an explicit lattice
gauge-fixed / Stueckelberg operator can be constructed whose determinant
quotient reproduces the recovered `M[h]` metric variations and carries the
analytic `−3`. **The original additive `Z_Proca + k·Z_scalar` `k`-scan is
withdrawn** (`DECOMP-UNAVAILABLE-AS-RECOVERED`) and must not be run on the
recovered code as a CIRC test.

### Required deliverables
`results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md` (historical record);
`scripts/recovered_2026/` (recovered pipeline); `BETAV_REPRODUCTION.md`;
`derivations/P2-BETAV-CIRC-01_determinant-decomposition.md` (Phase-1
adjudication) and its `q²`-level evidence
(`scripts/betav_decomp_q2.py`). The pre-registered rules and result of the
operator-identity audit are the remaining deliverables.

### Result
**Phase-1 design adjudication completed: `DECOMP-UNAVAILABLE-AS-RECOVERED`.** No
CIRC PASS/FAIL verdict. The recovered pipeline runs and reproduces the scalar
`β_B` and the vector `β_V` sign; the βV magnitude at accessible grids is
longitudinal-artifact limited (`BETAV_REPRODUCTION.md`); Finding 5's `−3.2(5)`
remains an **unpromoted, quarantined** paper value (recovery ≠ verification).
The additive `k`-scan design is withdrawn; the next step is the
operator-identity audit or `P2-BETAV-RECON-01`.

### Reviewer verdict
`SPECIFIED` — Phase-1 design adjudication completed
(`DECOMP-UNAVAILABLE-AS-RECOVERED`); **no CIRC PASS/FAIL** verdict. Not closed by
assertion in either direction. Next step: the operator/determinant-identity
audit or `P2-BETAV-RECON-01` — **not** the withdrawn `k`-scan.

### Superseded specification (historical record)

> The following was the original `k`-scan specification. It is **withdrawn**
> (`DECOMP-UNAVAILABLE-AS-RECOVERED`) and is retained only as a historical
> record. It is **not** a live specification; do not run it as a CIRC test.
>
> - *Locked assumptions (superseded):* `CONVENTIONS.md`; Proca determinant
>   structure, generalized to a compensating scalar power `k`.
> - *Inputs (superseded):* modified structure
>   `det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)^k`.
> - *Analytic anchors (superseded):* `β_V(k)/β_B = −(k+2)`
>   (`k=1→−3`, `k=2→−4`, `k=3→−5`).
> - *Kill criterion (superseded):* feed the recovered extraction the `k≠1`
>   structure holding `TT_RECIPES` and normalization fixed; if `β_V/β_B` returns
>   `−3` regardless of `k`, the extraction is circular. This was invalidated
>   because the external `boson_loop` scalar is not the flat longitudinal
>   eigenfactor, so the additive deformation is built on the wrong operator; and
>   the additive scan would in any case be `LINEAR-ONLY`.
> - *Required computations (superseded):* vary `k ∈ {0,1,2,3,½}` and check
>   whether `β_V/β_B` tracks `−(k+2)` or stays at `−3`.
> - *Structural hypothesis (superseded):* `TT_RECIPES` is 5 fixed,
>   unit-normalized, `k`-independent TT polarizations with no mechanism to
>   normalize `k` away, suggesting the projection cannot by construction force
>   `−3`.

### Consequences
Cross-repo: `3-vector-sector` `P3-C-004` rests on the `C_6 = −G_V/2` sign
structure, **not** on `−3.2(5)`, so it is unaffected; the flag in `MIGRATION.md`
stays as-is (that repo not read from or edited).

### Operational consequence
(Governance clarification `P2-SI1-UNBLOCK-01` — not a new scientific verdict.
The SI-1 unblock holds independent of this gate's status, now `SPECIFIED`; it
still does not gate SI-1, and `−3.2(5)` is still quarantined pending the
dual-gate promotion rule — `P2-BETAV-NUMREPRO-01` and a future
operator-identity CIRC verdict, **not** the withdrawn `k`-scan.)

`P2-BETAV-CIRC-01` **does not block**:
- `P2-CHANNEL-FREEZE-01`;
- `P2-PHASE-01`;

because those gates do not consume the historical Finding 5 numerical value.

It blocks only:
- treating `−3.2(5)` as validated numerical evidence;
- using the historical extraction as an operational numerical input.

`P2-MULTIPHASE-GRAV-01` **may not consume** the historical Finding 5 extraction.
Before the SI-2 numerical graviton-kernel computation, the vector input must be
one of:
1. `P2-BETAV-RECON-01` with status `PASS`; **or**
2. a separately pre-registered **analytic** vector-sector input sourced from
   Paper 3 `P3-C-001` / `P3-FIERZ-01` at pinned commit
   `8c363ef08368f5c022278ea5f36e01496be3d5ca`.

If path 2 is used: it must be frozen inside `P2-CHANNEL-FREEZE-01` before SI-2
computation; its repulsive sign (`G_ω = −G/N`) must be preserved; it must be
treated as a headwind; and it must **not** be claimed to have lattice
confirmation from `−3.2(5)`.

### Repository branch
`gate/p2-betav-circ`

### Relevant files
`scripts/recovered_2026/proca_loop.py`, `scripts/recovered_2026/mlog_coeff.py`,
`scripts/recovered_2026/reproduce_betav.py`,
`results/recovered-2026/BETAV_REPRODUCTION.md`,
`results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md`,
`derivations/betav_discriminating_power.md`,
`derivations/P2-BETAV-RECON-01_cleanroom_reconstruction.md`,
`derivations/P2-SI1-UNBLOCK-01.md`, `MIGRATION.md`.

### Date opened
2026-07-17

### Date closed
Open (`SPECIFIED` 2026-07-20 — pipeline recovered; Phase-1 design adjudication
`DECOMP-UNAVAILABLE-AS-RECOVERED`, additive `k`-scan withdrawn, no CIRC PASS/FAIL;
was `SUSPENDED` 2026-07-19 while the pipeline was missing).

## P2-BETAV-NUMREPRO-01 — Numerical reproduction of `β_V/β_B` at physical `k=1`

Status: RUN
Verdict: INCONCLUSIVE (registered 2σ interval exceeds the NUMREPRO band boundary — a scientifically assessable outcome, not a harness failure)
Artifact: results/P2-BETAV-CAMPAIGN/H_comparison.json (sha256: 918a9b87a8cac8fdff351d85bbfba66d09a80053926d370b634b76b3f11baa1f)

The decisive Arm-H run executed once on 2026-07-22 (frozen harness, `n=32`,
blind; `results/P2-BETAV-CAMPAIGN/raw/H.json`) and was compared under the
pre-registered interval rules §(c2). The comparator returned
`integrity_status=VERIFIED`, `scientific_status=ASSESSABLE`, exit 0. Result:
central `R_H = β_V/β_B ≈ −2.23` (baseline variant) with battery `σ_H ≈ 4.08`;
the battery spread is led by the **eps-drop-smallest** VERDICT variant, whose
3-point eps fit even flips the sign to `R_H ≈ +1.85` (window-shift gives
`R_H ≈ −3.52`; eps-drop-largest `≈ −5.61`). The 2σ interval `[−10.40, +5.94]`
does not fit inside the band `[−3.7, −2.7]` → **INCONCLUSIVE**. This is exactly the
pre-registered honest expectation (c2): the historical configuration cannot
distinguish `−3` at the registered confidence — a statement about the
configuration's discriminating power, **not** a failure of the operator
identity (that is Arm P's job, which is **not** run) and **not** a harness
defect. Recorded as-is; no band widening, no variant changes.

Rules registered 2026-07-21 in `derivations/P2-BETAV-CAMPAIGN_prereg.md`: Arm H
(`n=32`, windows `M_H`/`M_Hs`, `EPS_H`), the interval rules §(c2) (2σ interval
⊆ band `[−3.7, −2.7]`, no resolving-power ceiling — a larger σ makes PASS
harder), the frozen variant table §(c4) (window-shift is a VERDICT variant), and
the blind harness `scripts/P2-BETAV-CAMPAIGN/`. This is NUMREPRO output (2) of
the three campaign outputs; a NUMREPRO verdict reproduces a historical number
and **does not by itself promote `P2-C9`**. **Quarantine release or `P2-C9`
promotion requires the registered dual-gate conditions AND explicit
consideration of the separately recorded Arm-P historical-promotion outcome,
followed by PI+reviewer authorization; no script automatically promotes.** The
`−3.2(5)` quarantine is **unchanged** by this run.

### Scientific question
At physical `k=1`, does the recovered `β_V/β_B` converge reproducibly into the
frozen paper band for `−3.2(5)`, under preregistered grid refinement,
mass-window, longitudinal-sector, and fit-order stability checks?

### Relation to `P2-BETAV-CIRC-01` (distinct question)
This is **scientifically distinct** from `P2-BETAV-CIRC-01` (non-circularity /
discriminating power). Numerical work may be prepared independently, but
**`P2-C9` promotion requires BOTH `P2-BETAV-CIRC-01 = PASS` AND
`P2-BETAV-NUMREPRO-01 = PASS`**. Neither gate alone is sufficient.

### Current state
**Not run.** Current accessible-grid magnitudes do **not** reproduce the paper
value: `n=12: ≈ −61`, `n=16: ≈ −16` (light window); the heavy-inclusive window
even flips sign — longitudinal-artifact/grid limited
(`results/recovered-2026/BETAV_REPRODUCTION.md`). Only the vector `β_V` **sign**
(and the scalar `β_B`) are reproduced.

### Historical target configuration pinned — 2026-07-21 (pre-registration input; status unchanged)

The recovered full session log (`results/recovered-2026/session_log_full.md`)
pins the **historical target configuration(s)** for this reproduction. These are
**historically reported by the recovered session message, not independently
verified**; they are recorded here as pre-registration *input*, not as a result.
See the run-record index in `scripts/recovered_2026/PROVENANCE.md` (rows R7, R10,
R12, R14). At minimum the index includes:

- **direct Proca extraction:** `n=32`, mass window `m_V a = 0.11–0.20`,
  `β_V = −7.2×10⁻⁴` vs predicted `−7.9×10⁻⁴` (9%), ratio `−3.2(5)` (subwindows
  `−2.6`/`−3.4`; wide/heavy window drifts to `−5`);
- **gfvec/Solodukhin summary:** window `0.125–0.55`, `β_gfvec/β_B ≈ −2.4 … −2.9`
  (target `−2`), same summary quoting `Proca/B = −3.2(5)`;
- **boson grid-systematics test:** `n=48` vs `n=32` ratio test for `β_B`.

When this gate's PASS/FAIL/INCONCLUSIVE rules are pre-registered, the
reproduction **must target this configuration** and **must run through a blind
harness** — the historical drivers embed the analytic targets (`−2`, `−3`) in
comments/docstrings and the historical runs were **not blind**. **No status
change:** the gate stays `PROPOSED` (not run); `P2-C9` and the `−3.2(5)`
quarantine are untouched.

### Required preregistration before execution
Before any execution, freeze and commit:
- the exact grid sequence;
- the mass windows;
- the fit basis and fit orders;
- the longitudinal-mode prescription;
- the convergence metric and tolerance;
- the frozen paper acceptance band for `−3.2(5)`;
- the treatment of finite-volume / grid artifacts;
- the PASS, FAIL, and INCONCLUSIVE rules;
- the computational ceiling and stopping rule.

### Kill criterion
Under the frozen protocol, the `k=1` result fails to converge, is unstable under
the registered analysis variations, or converges **outside** the frozen paper
band.

### Claim consequence
A PASS is **necessary but not sufficient** by itself to promote `P2-C9`;
`P2-BETAV-CIRC-01` must **also** PASS.

### Regression anchors
`scripts/recovered_2026/reproduce_betav.py` (records the current, non-reproducing
accessible-grid magnitudes).

### Repository branch
`recover/betav-complete`

### Relevant files
`scripts/recovered_2026/proca_loop.py`, `scripts/recovered_2026/mlog_coeff.py`,
`scripts/recovered_2026/reproduce_betav.py`,
`results/recovered-2026/BETAV_REPRODUCTION.md`.

### Date opened
2026-07-20

### Date closed
Open (`PROPOSED` — not run).

## P2-BETAV-RECON-01 — Clean-room curved-background Proca reconstruction

Status: PROPOSED (not run; distinct from the historical circularity question)

### Scientific question
Build a *new* metric-coupled lattice Proca extraction and check whether it
tracks `β_V/β_B = −(k+2)`. **Scope label: a 2026 reconstructed pipeline, NOT a
test of the historical Finding 5 implementation.** A faithful reconstruction
returning `−(k+2)` shows only that the reconstruction is correct; it does not
show the historical pipeline was non-circular.

### Scope
1-form operator `Δ^{(1)}[g,h]` + compensating scalar `Δ^{(0)}[g,h]` on a
weak-field background; `Γ_k=½logdetΔ^{(1)}−(k/2)logdetΔ^{(0)}`; numerical
`h`-derivatives at the determinant/eigenvalue level; fixed axis-TT projection;
vary only `k∈{0,1,2,3,½}`.

### Locked assumptions
`CONVENTIONS.md`; historical-vs-reconstructed distinction kept explicit in every
artifact.

### Inputs
Metric-coupled lattice Proca operator; `h`-derivative step + Richardson check;
pre-registered projection (targets kept out of code/tests).

### Analytic anchors
`β_V/β_B = −(k+2)` (from `P2-HK-01`), compared only at the end.

### Regression anchors
None yet (proposed).

### Kill criterion
For the reconstruction itself: stuck at `−3` ∀k ⟹ the new pipeline is degenerate
(a bug); drift toward `−5` at heavy mass ⟹ longitudinal artifact. None of these
closes `P2-BETAV-CIRC-01`.

### Required computations
Full curved-background lattice Proca with numerical `h`-derivatives — a
substantial implementation, **not run** this sweep.

### Required deliverables
`derivations/P2-BETAV-RECON-01_cleanroom_reconstruction.md` (done); pipeline +
pre-reg note pending.

### Result
Not run.

### Reviewer verdict
`PROPOSED`.

### Consequences
Provides the honest path to eventually inform (not close) `P2-BETAV-CIRC-01`.

### Repository branch
`gate/p2-betav-circ`

### Relevant files
`derivations/P2-BETAV-RECON-01_cleanroom_reconstruction.md`.

### Date opened
2026-07-19

### Date closed
Open (proposed).

## P2-BETAV-ASSEMBLY-01 — Determinant-bookkeeping regression (does NOT close CIRC-01)

Status: PASS (implementation regression only; does not test the historical projection)

### Scientific question
Given the shared scalar lattice tadpole integral and the Proca determinant
powers, does the assembly code preserve the `k`-dependence correctly, with no
hardcoded `−3`? **This is an implementation-regression gate, not a
discrimination test, and it does NOT close `P2-BETAV-CIRC-01`.**

### Scope
The `k`-generalized determinant assembly `det^{−1/2}(Δ^{(1)})·det^{+1/2}(Δ^{(0)})^k`
realized on the one shared scalar lattice tadpole `⟨φ²⟩_lat`.

### Locked assumptions
`CONVENTIONS.md`; `P2-HK-01` per-factor `a_1` traces; `P2-BETA-01` tadpole.

### Inputs
Shared tadpole log coefficient `C`; determinant exponent `k∈{0,1,2,3,½}`.

### Analytic anchors
`β_B=−C/12`, `β_V(k)=C(2+k)/12`, `R_k=−(k+2)` (`C` cancels).

### Regression anchors
`scripts/betav_assembly.py`: `ratio(C,k)=−(k+2)` for all `k`, ratio variant
spread `≤9e-16`; mutation `freeze_scalar_power=True` collapses every `R_k→−3`.

### Kill criterion
Assembly returns a `k`-independent ratio (e.g. hardcoded `−3`) for the
un-mutated code ⟹ implementation bug. (This gate cannot pass/fail the
*historical* circularity question — that is `P2-BETAV-CIRC-01`.)

### Required computations
`k`-scan on the shared lattice integral + mutation. Done.

### Required deliverables
`derivations/P2-BETAV-ASSEMBLY-01_bookkeeping_regression.md`,
`scripts/betav_assembly.py`, `results/P2-BETAV-ASSEMBLY-01/`.

### Result
`R_k=−(k+2)` exactly (`k=2→−4`), ratio variant spread `≤9e-16` because the
shared integral `C` cancels (fully correlated numerator/denominator). Mutation
(freeze scalar power=1) collapses every `R_k` to `−3`. **Explicit caveat:** the
`C`-cancellation is precisely why this construction has no power to test the
historical Finding 5 projection; it verifies only that the code reads `k`.

### Reviewer verdict
Pending. PASS on its own (implementation-only) terms. Does **not** close
`P2-BETAV-CIRC-01` and does **not** show any real pipeline is non-circular.

### Consequences
None for the historical circularity question; that remains `SUSPENDED`.

### Repository branch
`gate/p2-betav-circ`

### Relevant files
`scripts/betav_assembly.py`,
`derivations/P2-BETAV-ASSEMBLY-01_bookkeeping_regression.md`,
`results/P2-BETAV-ASSEMBLY-01/`.

### Date opened
2026-07-19

### Date closed
2026-07-19 (implementation regression; `P2-BETAV-CIRC-01` remains SUSPENDED)

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
Updated by governance clarification `P2-SI1-UNBLOCK-01` (2026-07-20): this gate
**no longer requires `P2-BETAV-CIRC-01` to `PASS`**. `P2-BETAV-CIRC-01` is
`SUSPENDED` (provenance NOT LOCATED) and does not consume the historical Finding
5 value, so it does not block the channel freeze. The freeze requires instead
that the **provenance adjudication is complete** and the historical value
`−3.2(5)` is **quarantined as unreproduced** (`results/P2-BETAV-CIRC-01/
PROVENANCE_SEARCH.md`, `results/P2-SI1-DEPENDENCY.md`). Feeds `P2-PHASE-01`
(SI-1) and `P2-MULTIPHASE-GRAV-01` (SI-2).

This gate must **freeze the selected operational vector-input path**, exactly
one of:
- the reconstructed lattice path `P2-BETAV-RECON-01`, **if available and
  `PASS`**; or
- the pinned Paper 3 analytic path (`P3-C-001` / `P3-FIERZ-01` at
  `8c363ef08368f5c022278ea5f36e01496be3d5ca`, repulsive `G_ω = −G/N`, a
  headwind), which receives **no** validation from `−3.2(5)`.

### Kill criterion
None (a freeze, not a test). Operational rule: `P2-MULTIPHASE-GRAV-01` is not
admissible evidence until this freeze is committed first (policy §1). After
the freeze, adding a channel is an extension (AE-4), not a continuation.

### Required computations
(not started)

### Required deliverables
The channel/metric freeze document, committed with a commit hash (policy §1,
§3), before the SI-2 scan. The document must record which vector-input path
(reconstructed-PASS or pinned-analytic) is frozen.

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
Governance clarification `P2-SI1-UNBLOCK-01` (2026-07-20): phase enumeration may
proceed once the channel freeze is committed, **without consuming** the
historical Finding 5 value `−3.2(5)` (quarantined as unreproduced). It is not
blocked by `P2-BETAV-CIRC-01` = `SUSPENDED`.

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
interaction sector, not a rescue branch — see the pinned reference below).

### Paper 3 pinned input
The Paper 3 vector input is pinned to a fixed result so a later Paper 3 update
cannot silently change what this gate depends on:

- **Repository / SHA:** `zetacheng/3-vector-sector`, commit
  `8c363ef08368f5c022278ea5f36e01496be3d5ca` (`8c363ef`, `main` HEAD at
  re-confirmation via `git ls-remote`).
- **Claims / gates:** `P3-C-001` (the computed vector channel, repulsive) and
  `P3-FIERZ-01` (the Fierz/basis identity constraining the vector channel).
- **Conventions:** the vector channel is **repulsive**, `G_ω = -G/N`; the
  response saturates/screens — `D_00 = g_0 / (1 + g_0 Π_V) → 1/Π_V` — so
  increasing the nominal vector coupling does not automatically strengthen
  anything.
- **What Paper 3 supplies to `K_ij`:** the vector-channel (ω) contribution to
  the graviton kernel `K_ij(p)` — i.e. the vector entries of the frozen-channel
  mixing, entering with the repulsive sign above. Paper 3 is a supporting
  interaction sector, not an independent rescue branch.

### Dependency
Depends on `P2-PHASE-01` (and the `P2-CHANNEL-FREEZE-01` freeze). Paper 3
enters only as an interaction input to `K_ij(p)`, pinned at `8c363ef` (above).
Feeds `P4-SEA-ICE-01` (SI-3).

Governance clarification `P2-SI1-UNBLOCK-01` (2026-07-20): the full numerical
kernel evaluation requires a **frozen, admissible vector input** (from
`P2-CHANNEL-FREEZE-01`) and **may not use the historical Finding 5 value**
`−3.2(5)` (`SUSPENDED`, unreproduced). The frozen vector input must be either
`P2-BETAV-RECON-01` with status `PASS`, or the pinned Paper 3 analytic input
(`P3-C-001` / `P3-FIERZ-01` at `8c363ef`). The honest prior stands unchanged:
the vector channel is **repulsive** (`G_ω = −G/N`) and is a **headwind**, not a
rescue branch; this clarification does not soften it, and does not alter the
SI-2 PASS/FAIL criteria.

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

## P2-GRAV-ENGINE-RECOVERED-01 — Recovered historical gravity engine (Class A)

Status: PASS (recovered originals run and reproduce the paper's sign structure
and light-cone numbers within the stated tolerance below)

### Scientific question
Do the historical lattice gravity-engine files, recovered by the PI in 2026
(previously believed lost), run and reproduce Paper 2's Finding 3/4 numbers —
so they count as genuine provenance, not just "a file"?

### Scope
The five Class-A **runnable** originals in `scripts/recovered_2026/`:
`seagull_check.py` (root engine), `boson_loop.py`, `tt_check.py`,
`speed_check.py`, `structure_decomp.py`. The Class-B `proca_loop.py` (βV,
incomplete) is **excluded** and unaffected.

### Locked assumptions
Files landed **verbatim** (unedited, hash-pinned); reproduction targets
pre-registered from `paper/emergent_gr_paper_v2_15.tex` before running; nothing
tuned to match.

### Inputs / sha256
- `seagull_check.py` `6ec034e5a30e24d205c43c7dd0ea39c90a89f67c9db0da6e734a68862acefd90`
- `boson_loop.py` `32d6a4e0b9cca8ec4debb80758f77d0574d98a299492cb1ab9cfe2fdd26c08c2`
- `tt_check.py` `a40592a3b320cd9f118b3d96bd61abb10d5b20087d6b7a201dae5deabf90ba00`
- `speed_check.py` `8a374601161dd324795c2f1c9f7cc9d48031d83c5cc05e9896ae1e2814b1044c`
- `structure_decomp.py` `87d311fa4d86bb1c6862ace85bdd2c4a232db4f44e1662696f46c7226675fb9a`

### Analytic anchors
`speed_check`: `c_χ²−1≈0` (dim-4 protected), `ξ_χ=−0.078`, `ξ_f=−0.250`,
`Δξ=+0.17` (Case A); `c_χ²={1.22,1.42,2.44,3.77}` (Case B).
`seagull_check`/`tt_check`/`boson_loop`: `Z_h>0`, `xi_h<0` (Finding 4).

### Regression anchors
`scripts/recovered_2026/reproduce_check.py`; `results/recovered-2026/REPRODUCTION.md`.

### Kill criterion
A recovered file fails to run, or a checked quantity has the wrong sign vs the
paper ⟹ that file recorded as "recovered but unverified" (not silently landed).

### Required computations
Run each file's `run()`/`part_A`/`part_B` at a representative grid; compare to
pre-registered targets. Done.

### Required deliverables
`scripts/recovered_2026/` (files + `PROVENANCE.md` + `reproduce_check.py`),
`results/recovered-2026/REPRODUCTION.md`.

### Result / reproduction (with stated tolerance)
- **`speed_check` — reproduces quantitatively.** Case A to machine precision
  (`c_χ²−1=−5.46e-13`; `ξ_χ=−0.0777`, `ξ_f=−0.250`, `Δξ=+0.172`); Case B to
  `≤2.6%` (`1.251,1.421,2.438,3.774` vs `1.22,1.42,2.44,3.77`). Tolerance: `<1%`
  (Case A dim-6), `≤5%` (Case B, finite-`n`).
- **`seagull_check` — reproduces Finding 4 sign structure.** `Z_h=+1.48e-3>0`;
  `xi_h<0`, converging to `−1/6` (`n=8→−0.109`, `n=16→−0.142`). Residual: `~15%`
  finite-`n` gap to exact `−0.167` at `n≤16` (recorded, trend-consistent). The
  paper itself flags the `Λ²`-level `Z_h`/`c₂` as scheme-dependent and `c₂>0` as
  a defining assumption (lines 722–739); the reproduced content is the
  sign/structure.
- **`tt_check`** (bubble-only): `Z_h>0`, exact isotropy, `ξ_f=−0.250`.
- **`boson_loop`**: `Z_cov^B>0`, internal const-`h` validation to `~1e-8`.
- **`structure_decomp`**: decomposition tool; imports and its projector basis
  computes (no standalone `run()`).
- A full βV/Finding-3 β-coefficient mass-scan **through these engines** is not
  performed here (β is covered by `P2-BETA-01`); the engines are consistent with
  it. No file was "recovered but unverified".

### Reviewer verdict
Pending. `PASS`: all Class-A originals run and reproduce the paper's sign
structure; `speed_check` reproduces quantitatively. Residual finite-`n` gap on
`seagull_check`'s `xi_h` magnitude to `−1/6` recorded, not hidden.

### Consequences
Provides genuine, runnable provenance for the gravity-kernel sector. Partially
supersedes `MIGRATION.md`'s "nothing can be re-run" (gravity sector only); does
not touch βV (`P2-BETAV-CIRC-01` stays `SUSPENDED`). No historical claim
upgraded/downgraded by the recovery itself.

### Repository branch
`recover/lattice-gravity-engine`

### Relevant files
`scripts/recovered_2026/`, `results/recovered-2026/REPRODUCTION.md`, `MIGRATION.md`.

### Date opened
2026-07-20

### Date closed
2026-07-20 (recovery + reproduction; reviewer adjudication pending).

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
