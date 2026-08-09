# Report — generator-sum mean-field criticality: does `G_c = 1/(2·I_0)` transfer?

Task: derivation (MATERIAL). Evidence base
`51d4bbe1a2e965b0793b18f4ead5a11dab54c364`. Branch
`gate/p2-generator-sum-criticality`. Decides nothing: `P2-GAP-01` keeps
`PASS`, `P2-PHASE-01` keeps `PROPOSED`.

Committed-report layer (A1–A8, A9-pre, A10, commit SHAs/messages, pre-report
head, intended manifest + SHA-256, intended report message). Post-report
evidence (scope check at the pushed head, A9-final, the push, the report
commit's stored message read back, ancestry) is returned to the Reviewer and
not written back.

## A1 — pinned inputs verified (STOP on mismatch)

All four sha256 matched at `51d4bbe1` (read from the git objects):

```
derivations/P2-GAP-01_gap_criticality.md               17b6f613…fade00  OK
scripts/gap_criticality.py                             b99f9a66…a90c2   OK
derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md      fe68b9c6…a4e67a  OK
derivations/P2-PHASE-01_scalar_stationary_exploratory  80586e33…322599  OK
```

Repository inputs actually read (read-only, by path): the four above plus
`DECISION_LOG.md` (exponent-mapping ruling, 2026-08-08). The quarantined
`−3.2(5)`, the suspended `P2-BETAV-CIRC-01` result, and the historical
Finding 5 extraction were **not** consumed.

## A2 — control reproduced (first, since everything depends on it)

Singlet-only `L_int = G_N (ψ̄ψ)²`, single Dirac fermion. Hartree (direct)
self-energy `Σ = 2 G_N ⟨ψ̄ψ⟩`; tadpole `⟨ψ̄ψ⟩ = −4 m B(m)` (Dirac trace 4
explicit); attractive sign (exponent ruling). Linearising:

    1 = 8 G_N I_0        (coefficient-in-front normalisation)
    1 = 2 G   I_0  ,  G = 4 G_N   ⟹   G_c = 1/(2 I_0)   (channel form)

The channel form reproduces `P2-GAP-01` exactly (prefactor 2). Script field
`control_singlet_only.reproduces_P2_GAP_01 = true`. **Gate passes.**

## A3 — generator-sum gap equation (λ^A sums explicit)

Scalar interaction `X_S = (G/2N) Σ_A (S^A)²`, `S^A = ψ̄(λ^A⊗1_4)ψ`. Under the
uniform flavour-singlet condensate `⟨ψ̄_iψ_j⟩ = δ_{ij}Φ`:

- **Which generators condense (determined, not assumed):**
  `⟨S^A⟩ = Tr(λ^A)·Φ`; `Tr(λ^0)=√(2N)`, `Tr(λ^{A≠0})=0`. Only the singlet
  `A=0` acquires a mean field: `⟨S^0⟩ = √(2N)Φ`.
- **Self-energy:** `Σ_{ij} = 2·(G/2N) Σ_A (λ^A)_{ij}⟨S^A⟩ =
  (G/N)(λ^0)_{ij}√(2N)Φ = (G/N)·√(2/N)·√(2N)·Φδ_{ij} = (2G/N)Φδ_{ij}`
  (using `√(2/N)·√(2N)=2`). Equivalently `Σ_A λ^A Tr(λ^A) = 2·1_N` (computed
  for `N=2,3,4`). A completeness-relation cross-check (§2 of the note)
  gives the identical `(2G/N)Φ`.
- **Gap equation:** `m = (2G/N)·4·m B(m)` ⟹

      1 = (8/N) G I_0     ⟹     G_c = N/(8 I_0).

The mean-field combinatorial factor the generator sum produces is **8/N**
(canonical coupling, trace explicit) = `2` (Hartree) × `4` (Dirac trace) ×
`1/N` (canonical `1/2N` × singlet projection `2`). Every factor is shown in
`derivations/P2-GENERATOR-SUM-CRITICALITY_01.md` and computed from explicit
`λ^A` in `scripts/p2_generator_sum_criticality.py`.

The completeness relation `Σ_A λ^A_{ij}λ^A_{kl} = 2δ_{il}δ_{kj}` was
**derived** from the frozen facts (complete Hermitian basis + `Tr=2δ`), not
supplied; it is verified against the constructed bases for `N=2,3,4`. No
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` arose.

## A4 — the ratio, and the case

Both critical couplings measured as the coefficient literally in front of
their interaction, all computational conventions identical:

| N | gen-sum gap (canonical G) | `G_c` gen-sum | `G_c` singlet | ratio `G_c^{(b)}/G_c^{(a)}` |
|---|---|---|---|---|
| symbolic | `1 = (8/N) G I_0` | `N/(8 I_0)` | `1/(8 I_0)` | **`N`** |
| 2 | `1 = 4 G I_0` | `1/(4 I_0)` | `1/(8 I_0)` | 2 |
| 3 | `1 = (8/3) G I_0` | `3/(8 I_0)` | `1/(8 I_0)` | 3 |
| 4 | `1 = 2 G I_0` | `1/(2 I_0)` | `1/(8 I_0)` | 4 |

**Case: `N`-dependent** (the "more serious" case). The ratio is `N`, computed
by the script from the reduced `Σ_A λ^A Tr(λ^A)`, not asserted. `R(1)=1` (at
`N=1` the generator sum *is* `G(ψ̄ψ)²`, the control interaction — a
consistency check the derivation passes).

**`G_c = 1/(2 I_0)` does not transfer.** It is the trace-absorbed *channel*
coupling statement. For the *canonical* coupling `G` (the single coupling the
`P2-PHASE-01` scan varies) the critical value is `N/(8 I_0)`, i.e. the gap is
`1 = (8/N) G I_0`, whose prefactor depends on `N`. **The step that differs**
is the canonical `1/2N` normalisation times the singlet projection
`⟨S^0⟩=√(2N)Φ`, `(λ^0)=√(2/N)δ`, giving the per-flavour coefficient `2G/N`
in place of the singlet-only `2G_N`.

## A5 — ansatz observation (no second ansatz supplied)

The frozen material fixes the uniform flavour-singlet scalar condensate
`⟨ψ̄_iψ_j⟩ = δ_{ij}Φ` (the exploratory `M̂ = aM`), under which only the
singlet generator condenses. An **adjoint** condensate
`⟨ψ̄_iψ_j⟩ ∝ (λ^B)_{ij}` (traceless `B`) would break the U(N) flavour
symmetry the freeze imposes and is **not** fixed by the frozen material.
**The singlet ansatz is the only condensate the frozen material supports;**
whether an adjoint one exists is a different question and is not answered
here (no second ansatz supplied).

## Consequence for the exploratory results (implication only)

The `P2-PHASE-01` exploratory note applied `1 = 2 G I_0` — i.e.
`G_c = 1/(2 I_0)` — to the **canonical** coupling `G`. The value derived here
for that coupling is `G_c = N/(8 I_0) = (N/4)·(1/(2 I_0))`. Every position
quoted in `G/G_c` (the `M̂=1` crossing at `G/G_c = 1.769`, the 282-row
branch-depth table, the drafted domain bounds) therefore carries an
`N`-dependent calibration factor **`N/4`**: correct only at `N=4`, off by
`1/2` at `N=2` and `3/4` at `N=3`. The qualitative findings (local stability,
linear onset, a stable negative-mass branch) do not depend on that scale and
are expected to survive; only the `G/G_c` scale moves. **The rescaling is a
separate task and is not performed here.**

## A6 — deliverables

Derivation note (`derivations/P2-GENERATOR-SUM-CRITICALITY_01.md`), script
(`scripts/p2_generator_sum_criticality.py`), result artifact
(`results/P2-PHASE-01/generator-sum-criticality/criticality.json`), test
(`tests/test_p2_generator_sum_criticality.py`), this report. Tests: control
`1 = 2 G_c I_0`; generator normalisation `Tr(λ^Aλ^B)=2δ_AB` for `N=2,3,4`;
completeness; `Σ_A λ^A Tr λ^A = 2`; the ratio (`=N`) computed by the script
with a mutation-detection companion (`ratio ≠ 1`).

## A7 — nothing pre-existing disturbed

Base↔head blob-identity confirmed for `GATES.md`, `CONVENTIONS.md`,
`AGENTS.md`, `DECISION_LOG.md`, `pyproject.toml` (read from the objects). No
gate, gate status, verdict, digest, hash-pinned artifact, or pre-existing
test is modified. `P2-GAP-01` untouched.

## A8 — scope (six additions, zero modifications)

Manifest template = the standard scope-checker manifest (`base`, `head`,
`mode: exact`, `required` add-operations, `forbidden_operations`). Resolved
manifest (intended final):

```
add specs/2026-08-08T2350Z_generator-sum-criticality.md
add derivations/P2-GENERATOR-SUM-CRITICALITY_01.md
add scripts/p2_generator_sum_criticality.py
add results/P2-PHASE-01/generator-sum-criticality/criticality.json
add tests/test_p2_generator_sum_criticality.py
add reports/2026-08-08T2350Z_generator-sum-criticality.md
```

Manifest SHA-256: `42e20a7fc614eee2fc076eda21c7ef99ea1d66c8e40a29bb670ce6f1ffda8631`.
`scripts/governance_tools/scope_checker.py` is present here (unlike
`0-programme`); its JSON (`overall`, `observed_operations`) at the pushed
head is post-report evidence. At the pre-report head it reports the five
non-report additions and one "required operation missing" for the report,
as expected.

## A9-pre — validators at the pre-report head (`9f759b5`)

Each run individually with `python -m pytest <path>`, all exit 0:

```
tests/test_repository_structure.py            4 passed
tests/test_si1_governance.py                 14 passed
tests/test_gate_anchors.py                   18 passed, 2 deselected
tests/test_governance_tools.py                8 passed
tests/test_p2_phase01_scalar_exploratory.py   5 passed
tests/test_p2_phase01_fierz_and_depths.py    14 passed
tests/test_p2_channel_character.py           23 passed
tests/test_p2_generator_sum_criticality.py    7 passed
```

A9-final (same set at the pushed head) is post-report evidence and carries
the verdict.

## A10 — lint

`ruff check scripts/p2_generator_sum_criticality.py
tests/test_p2_generator_sum_criticality.py` → All checks passed. Pre-existing
diagnostics elsewhere were not touched.

## Commit hygiene (A9 of the task; commits 1–3)

The harness appends `Co-Authored-By:` and `Claude-Session:` trailers by
default; both **suppressed** on every commit (inspected before, read back
after). Stored messages carry no trailer:

- commit 1 `8a36e11` — `spec: generator-sum mean-field criticality derivation task`.
- commit 2 `be18350` — `derivation: generator-sum mean-field scalar criticality note (before code, rule 3)`.
- commit 3 `9f759b5` — `compute: generator-sum criticality script, result artifact, and regression test`.

Pre-report head: `9f759b561966810d5e3179477b86b5e3c5fd0fbd`. Intended report
commit message: `report: generator-sum criticality — G_c does not transfer (N-dependent)`, trailer-free.

## Stops and clarifications

No hard STOP (the control calibrated; A2 passed). One primary category per
stop; none triggered.

- **SPECIFICATION_DEFECT** — none.
- **ENVIRONMENT** — none. `sympy 1.14.0` already present; nothing installed.
- **OBSERVATION_METHOD_ERROR** — none.
- **REPOSITORY_DEFECT** — none.
- **UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY** — none: the completeness
  relation is a consequence of the frozen complete-basis + normalisation, not
  an unfrozen input; no relation outside the freeze was supplied.

## Anything ambiguous / would have specified differently

- **The word "ratio".** Two defensible numbers exist and both are reported:
  the convention-consistent **`N`** (each `G_c` as the coefficient in front of
  its interaction; gives the mandatory `R(1)=1`), and the **`N/4`**
  calibration factor for the exploratory work (which applied the channel value
  `1/(2 I_0)` to the canonical coupling). The headline transfer verdict —
  `G_c = 1/(2 I_0)` does **not** transfer, the case is `N`-dependent — is the
  same under either. A future spec could name which coupling normalisation the
  reported ratio should use, to remove the ambiguity.
- Otherwise the specification was internally consistent and consistent with the
  repository's rules.
