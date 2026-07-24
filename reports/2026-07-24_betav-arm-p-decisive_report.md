# Arm P decisive run report

## Scope and chronology

This report records the Arm-P compute provenance, the sandbox comparison, and
the governance record. It does not promote `P2-C9`, release the `−3.2(5)`
quarantine, merge a branch, or edit Paper 2.

Pre-report commit chronology:

1. `0f7961747abe2a18b436c0b1e5b928f425ea4d9a` — pinned base;
2. `95a828542f0daf44011f0172f94203fb7b69de3f` — PI-machine compute artifact
   commit;
3. `c2253bb6ef99e728647775feafe0d43c88f6641f` — Arm-P comparison commit;
4. `6f32d10a87a6e48fc1c827caf7a62d4c05c43269` — CIRC bookkeeping and the
   pre-authorized test update.

## Sandbox Part-0 verification

In the normalized sandbox clone, `origin/main` was
`0f7961747abe2a18b436c0b1e5b928f425ea4d9a`; the Arm-P remote branch existed
and its artifact-only initial tip was
`95a828542f0daf44011f0172f94203fb7b69de3f`. The checked-out branch was one
commit beyond the pinned base before the comparison, with the base as its
parent; its only changed paths were:

- `results/P2-BETAV-CAMPAIGN/raw/P.json`
- `results/P2-BETAV-CAMPAIGN/raw/P.json.sha256`

The sidecar verified `P.json: OK`. The working-tree SHA-256 and committed-blob
SHA-256 both equal
`836cc1ab04cd153358d41e677280e058a652244196ba53a34369e373b56d7c4f`.
The JSON parsed with `compute_git_commit` exactly
`0f7961747abe2a18b436c0b1e5b928f425ea4d9a`, schema
`p2-betav-campaign/compute/v2`, and arm `P`. The in-sandbox
`git merge-base --is-ancestor` check exited 0.

The first temporary clone had checkout conversion enabled:

```text
file:C:/Program Files/Git/etc/gitconfig true
exit: 0
exit: 1
results/P2-BETAV-CAMPAIGN/raw/P.json: text: unspecified
results/P2-BETAV-CAMPAIGN/raw/P.json: eol: unspecified
```

Its checkout-time EOL transformation changed the raw working-tree bytes while
the committed blob retained the pinned digest. The final sandbox clone was
created with `core.autocrlf=false` and `core.eol=lf`; these executor
environment settings, not any repository, harness, schema, or artifact change,
were required because comparator check (1) reads the working tree.

## Compute provenance and prior executor/PI records

The raw artifact was completed at `2026-07-24 11:20:22Z`, with measured wall
time `5:41:01`; the start timestamp `2026-07-24 05:39:21Z` is derived
arithmetically. The launcher did not retain an independently queryable exit
code. The executor reported the harness's normal success line and established
integrity by sidecar verification, JSON parsing, and deterministic completion.

The compute JSON records the PI-machine environment:

```text
platform: Windows-11-10.0.26200-SP0
python_version: 3.12.13
numpy_version: 2.3.5
blas_info: {}
```

The following are **prior executor/PI records, not observations made by this
sandbox**:

- the sandbox compute launch at `2026-07-23 02:07:45Z` (PID 2627) was killed
  by container reclamation after approximately nine hours, produced zero
  artifact, and complied with the stop rule;
- the preregistration §(f) PI-machine relaunch completed as recorded above;
- the `armp-run` clone was absent at landing time, so provenance rests on the
  pinned digest, the sealed `compute_git_commit`, and sidecar integrity at each
  relocation step — one rung weaker than retaining the live run clone;
- the PI reported a non-shallow manual ancestry probe with exit 0 and Git
  reachable from a Python subprocess;
- the earlier PI-machine comparator refusal occurred at ancestry check (4),
  attributed to a transient environmental Git failure folded into “not
  ancestor” by `_is_ancestor` broad exception handling (a hardening-backlog
  item);
- the failed PowerShell capture was 624 UTF-16-with-BOM bytes, while a
  diagnostic stdout was 311 valid-JSON bytes, consistent with redirect
  transcoding; no physics-result keys were inspected before a mechanical
  refusal-only safety gate;
- the original launcher emitted its normal success line, as reported by the
  executor.

## Comparator record

The sandbox comparator command was:

```text
python scripts/P2-BETAV-CAMPAIGN/compare.py --json results/P2-BETAV-CAMPAIGN/raw/P.json > results/P2-BETAV-CAMPAIGN/P_comparison.json
```

It exited 0. The emitted comparison artifact SHA-256 is
`29f937e467d0c3d6ed157f4dbd752af65084b621ee7f209badb3845524f26d7d`.
All five refuse checks verified; `integrity_status=VERIFIED` and
`scientific_status=ASSESSABLE`.

## Campaign outputs

### Output 1 — Arm-P CIRC audit

Verdict: **INCONCLUSIVE (insufficient resolving power)**. Baseline
`C_cons=0.059846062787177995`; `σ_C=0.7353056040292271`;
`2σ_C=1.4706112080584541`; `δ_audit=0.05`; and
`τ_C=1.4975142348013066e-05`. The comparator classified the outcome as
scientifically assessable, with resolving power insufficient because
`2σ_C > δ_audit`.

### Output 2 — Arm-H NUMREPRO

Arm-H NUMREPRO is already recorded as **INCONCLUSIVE**. It is referenced here
only as the previously recorded Arm-H result, not as a new Arm-P result.

### Output 3 — Arm-P historical-promotion criterion

Recorded outcome: **not met**. `β_gfvec/β_B=-13.185938988618338` with
`σ_gf/B=20.08326113789817`; `β_proca/β_B=-14.12609292583116` with
`σ_P/B=20.818566741927395`. This is a historical campaign outcome, not a gate
verdict, and causes no automatic promotion.

## Diagnostics

The Tier-1 `D(m)` and Tier-1↔Tier-2 cross-check completed; the maximum
cross-check difference was `4.383968435126527e-14` versus numerical tolerance
`1.7637539060482024e-09`. The gfvec-v2 seagull diagnostic was consistent:
`dZ_max=6.6193578396323e-14`, `dbeta=2.5906498604330586e-10`, and
`dbeta/|B_base|=2.1995897670763248e-06`, below
`tau_Z=2.219790498676402e-08`. No seagull-sensitivity label was emitted.

The extended-basis diagnostic executed and was valid for all four required
components: `proca`, `gfvec`, `boson`, and `D`. The `D` fit was valid, rank 5
with 5 points and 5 columns, 0 degrees of freedom, condition number
`18444466.334790725`, residual `2.9778502051908996e-22`, and the recorded note
`dof=0 (residual vacuous)`. The comparator’s extended-basis and seagull
diagnostic gates both returned `ok=true`.

## Governance record

`P2-BETAV-CIRC-01` changed from `SPECIFIED` to `RUN`; its comparator wording is
in a separate `Verdict:` field and its path/digest in a separate `Artifact:`
field. The Arm-P historical-promotion outcome is separately labelled in the
CIRC block.

The sole test edit was the pre-authorized forward-rule-1e replacement of
`test_circ01_is_specified_after_recovery` with
`test_circ01_run_verdict_recorded_separately`; no other test changed.
`P2-C9` remains unchanged and the `−3.2(5)` quarantine remains in force.

Quarantine release or `P2-C9` promotion requires the registered dual-gate
conditions AND explicit consideration of the separately recorded Arm-P
historical-promotion outcome, followed by PI+reviewer authorization; no script
automatically promotes.

Because Arm-H NUMREPRO is already INCONCLUSIVE, the registered dual-gate
PASS+PASS condition is presently not satisfiable regardless of the Arm-P audit
verdict or historical-promotion outcome. An Arm-P audit PASS alone creates no
promotion path.

## Verification and environment incidents

The final checks before this report were:

```text
python -m pytest tests -q
50 passed, 2 deselected

ruff check .
All checks passed!
```

The initial v8 stop occurred because pytest and ruff were unavailable in the
normalized environment. The v9 continuation installed them but stopped when
test collection showed SymPy unavailable. Both incidents were resolved in this
continuation by installing the repository-declared dependency set:
NumPy 2.3.5, SciPy 1.18.0, SymPy 1.14.0, pytest 9.1.1, and ruff 0.16.0.

The pre-report working tree was clean after the gate commit.
