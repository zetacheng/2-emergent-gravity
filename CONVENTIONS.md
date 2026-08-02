# Convention Registry

No calculation may begin until every relevant convention below is filled,
reviewed, and locked for the applicable gate. **These conventions were fixed
before any computation in gates `P2-HK-01`, `P2-GAP-01`, `P2-BETA-01`, and
`P2-BETAV-01`, and were not adjusted afterwards to reproduce a paper value.**

## Locked conventions for the independent-verification sweep

| Convention | Value |
|---|---|
| Metric signature | Euclidean, `(+,+,+,+)`, `d = 4`. Curvature sign: `R > 0` on a sphere (`R = +d(d-1)/a²` for a `d`-sphere of radius `a`). |
| Wick rotation | All loop integrals performed in Euclidean signature. `∫ d⁴p_E` with `p²≡p_E² ≥ 0`. |
| Fourier transform | `f(x) = ∫ d⁴p/(2π)⁴ e^{ipx} f̃(p)`; loop measure `∫ d⁴p/(2π)⁴`. |
| Heat-kernel operator | `Δ = −∇² + E` (Laplace-type). `E` is the endomorphism (potential/bundle) term; **sign convention: `E` enters with a `+` so that a scalar curvature coupling `ξR` appears inside `E` as `E ⊃ +ξR`.** The mass `m²` is separated out explicitly (`Δ + m²`) and is **not** counted inside `E` for the `a_k`. |
| Heat-kernel expansion | `Tr e^{−τΔ} = (4πτ)^{−d/2} ∫ d^dx √g Σ_{k≥0} a_k(x) τ^k`, `d=4`. Indexing: `a_0 = tr 𝟙`, and `a_1 = tr[(1/6)R·𝟙 − E]` (the `R`-linear Seeley–DeWitt coefficient). This is the "`a_1`/`b_2`" in the τ-power indexing; some references call it `b_4`. |
| Curvature coupling of scalar | Non-minimal coupling term `½ ξ R φ²` in the action ⟹ `E = ξ R` for the scalar; minimal coupling is `ξ = 0`. The conformal value in `d=4` is `ξ = 1/6`. |
| Dirac operator squaring | `−(γ·∇)² = −∇² + (1/4)R` (Lichnerowicz), so for a Dirac fermion `E = (1/4)R·𝟙₄` on the 4-component spinor bundle; the fermion loop carries an overall statistics sign `−1` relative to a real boson. |
| Massive-vector (Proca) structure | `Z_{s=1,m} = det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)`, with the vector Laplacian `Δ^{(1)}` having `E^{μ}{}_{ν}=R^{μ}{}_{ν}` (`tr E = R`) and the Stueckelberg scalar `Δ^{(0)}` having `E=0`. This determinant structure is taken as an input from the paper; the coefficient it implies is what we compute. |
| Definition of `Z(m²)` | The induced axis/transverse-traceless (TT) graviton kinetic coefficient, i.e. the coefficient of the induced Einstein–Hilbert term `∫√g R` normalized **per unit `4N`** of fermionic degrees of freedom (`4` spinor components × `N` flavors). Concretely `Z ≡ 1/(16πG_ind)` in the TT channel, expressed per `4N`. The `m²ln m²` piece defines the species coefficient: `Z ⊃ β_s · m² ln m²`. |
| Species coefficient `β_s` | Coefficient of `m² ln m²` in `Z(m²)`. Computed from `a_1`: `β_s = −p_s (4π)^{−2} (tr a_1 / R)`, where `p_s` is the log-det prefactor of the species (`+1/2` per bosonic `det^{−1/2}` factor, `−1/2` per `det^{+1/2}` factor / fermion loop). Reported both as a raw value (this convention) and as convention-independent ratios `β_F/β_B`, `β_V/β_B`, `β_B(ξ)/β_B`. |
| Definition of `L` | `L ≡ ln(Λ²/m²)`. The mass `m` is measured **in units of the cutoff `Λ`** (i.e. `Λ ≡ 1` unless a gate states otherwise), so `L = −ln m²` in those units. `ln m²` and `L` differ only by sign and the `ln Λ²` reference. |
| Regularization | **Sharp Euclidean 4-ball `|p| < Λ`** for all continuum momentum integrals, unless a gate explicitly states another regulator. |
| Lattice regularization | Hypercubic lattice, spacing `a` (`a ≡ 1` in lattice units), Brillouin zone `p_μ ∈ (−π, π]`. Free-field lattice momenta: `p̂² = Σ_μ 4 sin²(p_μ/2)` (naive/scalar), `s̄_μ = sin p_μ`, Wilson term `W(p) = r Σ_μ (1 − cos p_μ)` with Wilson parameter `r = 1`. |
| Sign of the action | Euclidean action `S_E ≥ 0`; `Z = ∫ e^{−S_E}`, effective action `W = −ln Z`. Boson: `W = +½ Tr ln(Δ+m²)`. Dirac fermion: `W = −Tr ln(iγ·D − m) = −½ Tr ln(−(γD)² + m²)`. |
| Gamma matrices | Euclidean, Hermitian `γ_μ = γ_μ^†`, `{γ_μ,γ_ν} = 2δ_{μν}`, `tr 𝟙₄ = 4`. |
| Gamma5 | `γ_5 = γ_1γ_2γ_3γ_4`, Hermitian, `γ_5² = 𝟙`, `{γ_5,γ_μ}=0`. |
| Generator normalization | Not used in gates `P2-*` (single-species loops); `tr(T^aT^b)=½δ^{ab}` if flavor generators are ever needed. |
| Flavor basis | `N` degenerate flavors; the induced coefficient is reported per unit `4N`. |
| Field dimensions | Canonical: scalar `[φ]=1`, Dirac `[ψ]=3/2` in `d=4`. |
| Cutoff and lattice units | `Λ ≡ 1` (continuum), `a ≡ 1` (lattice); masses quoted as `m/Λ` or `m a`. |
| Definition of attractive and repulsive channels | Scalar (`ψ̄ψ`) condensate channel is the attractive channel driving the gap; the four-fermion coupling `G > 0` is attractive there. |
| Normalization of Green functions | Euclidean Wilson propagator `S(p) = 1/(iγ·s̄(p) + W(p) + m)`; scalar `1/(p̂²+m²)`. |
| Gap-equation integral `I_0` | `I_0` is defined by the linearization of the mean-field gap equation about zero condensate, `1 = 2 G_c I_0`; the precise integrand and the derivation of the relation `G_c = 1/(2I_0)` are given in the `P2-GAP-01` derivation note and script. |
| Statistical-error convention | Numerical uncertainties are reported as spreads over discretization / fit-window / ansatz variations (systematic), not as formal fit errors alone. Convergence is demonstrated by grid refinement and half-shifted (offset) grid cross-checks. |

## Change control

Any change to a locked convention after a gate has been committed must be
recorded as a new `DECISION_LOG.md` entry that supersedes the prior one, and
must trigger re-examination of every gate that consumed it. Conventions are
never changed silently, and never changed in order to reach a target number.

## Execution discipline for decisive runs and merges

These rules bind prospectively only. They imply no retrospective action for
campaigns run under prior discipline and alter no interpretation of previously
approved scientific results; in particular, the Arm H `INCONCLUSIVE` verdict
is untouched.

### 1. Contradiction-stop

Origin: `reports/2026-07-22_betav-arm-h-decisive_report.md` §1e.

A gate-bookkeeping task that changes a gate status MUST enumerate, in its
frozen scope, the specific governance-test updates that status change entails
(pre-authorized test diffs, listed by test name); and the executor MUST stop
and report on any conflict between frozen-scope clauses — a contradiction in
the prompt is itself a reportable defect, never something to resolve
unilaterally.

This rule has been in force since 2026-07-22 and is relocated here for
discoverability, not newly created; it was applied in commit `6f32d10`. This
rule is normative regardless of where it was first recorded.

### 2. Scope precedence

When an execution prompt and a repository rule (or the authorized scope) are
or appear inconsistent, the executor MUST stop immediately and report. The
inconsistency is itself a governance finding. The executor SHALL NOT infer,
assume, or decide which instruction takes precedence — precedence is
determined by the PI and reviewers, never by the executor.

### 3. Declared frozen scope is normative

A decisive or gate-bookkeeping prompt MUST declare its frozen file set
explicitly. Before the gate is updated, the commit's changed-file list MUST be
compared against that declared set — `git diff --name-only <base>..<head>` —
and any file outside it reported. The declared frozen file set is
authoritative. It SHALL be treated as normative: a file outside it constitutes
an authorization failure, not a matter of review judgement. A checker script
consuming a declared manifest is to be implemented separately; until it
exists, the manual comparison is mandatory and its output MUST be recorded in
the run report.

### 4. Execution prompts are evidence

The execution prompt governing any decisive or pre-registered run MUST be
committed to the repository, AND its sha256 recorded in the run's report,
before the run begins.

### 5. Minimum mandatory merge discipline

The following is a floor which may not be reduced; it is not an adaptable
checklist. The `gate/p2-betav-cleanup` merge (`fd5f6b9`) is an exercised
precedent.

1. Working tree: no tracked file modified, staged, deleted, renamed or
   conflicted. Untracked paths MUST be enumerated and explicitly accepted, and
   the approval MUST itself be recorded with its source. Nothing may be
   stashed, cleaned or discarded to satisfy this.
2. Ancestry checked after fetching; merge the pinned REMOTE ref, never a local
   branch. If the base has moved past the reviewed base, do not merge —
   approval covers branch AND base together.
3. Scope checked BEFORE merging: changed-file list limited to the declared
   set; diff restricted to protected paths (`scripts/ tests/ results/
   derivations/ reports/`) MUST be empty.
4. After merging, verify both parents AND `git diff --name-only HEAD^1..HEAD`;
   correct parentage does not imply a correct tree.
5. Re-verify by fixed-string grep that pinned artifact digests survive the
   merge unchanged.
6. Any merge conflict is an immediate STOP: do not resolve, do not edit either
   side, do not force a strategy.
7. No environment repair and no dependency installation: no `pip`, `poetry`,
   `conda`, `uv`, or equivalent installation of any kind; no venv changes; no
   validator reconfiguration; no formatters, no repository-wide maintenance.
   Nothing outside the merged files may change by any mechanism, including
   automated ones.
8. Push verification: `git rev-parse HEAD` and `git rev-parse origin/main`
   identical; record `git merge-base HEAD^1 HEAD^2`.
9. Overriding rule: if any required command produces an unexpected result,
   STOP; do not repair the repository, do not retry by changing its state,
   report the exact output. This takes precedence over the instruction to
   complete the merge.

### 6. Reporting honesty for merges

A report MUST distinguish "the main worktree carries approved untracked
paths" from "the repository is clean"; state which worktree was clean.

A validator that examined nothing MUST NOT be recorded as a pass. For example,
`ruff check` on Markdown files returns "All checks passed" together with "No
Python files found"; it verified nothing. Substantive verification for a
documentation merge is: governance tests, scope diff, digest checks, and a
clean merge worktree.

### 7. Evidence precedence

When repository state, committed artifacts, and narrative reports disagree,
the committed artifacts take precedence. Reports explain; artifacts govern.
Any claim about the state of the repository — by any agent, in any review, at
any time — MUST be verified against the committed artifacts before it is
relied upon or recorded.

This rule arose from the Arm-H audit, in which several claims about repository
state, made from recollection of prior sessions rather than from inspection,
were found on checking to be incorrect. Verification against artifacts is not
optional courtesy; it is the governing evidential rule.
