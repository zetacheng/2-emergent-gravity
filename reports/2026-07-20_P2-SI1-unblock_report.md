# Canonical report — unblock SI-1 after the Paper 2 provenance adjudication

**Date:** 2026-07-20. **Repository:** `zetacheng/2-emergent-gravity`.
**Task type:** governance clarification of the operational dependency graph
(docs only; no scientific content added).

## 1. Executive summary

The historical Finding 5 lattice pipeline that produced `β_V/β_B = −3.2(5)` was
not located, so `P2-BETAV-CIRC-01` remains `SUSPENDED` and `−3.2(5)` remains
unreproduced. This task separates the **historical audit** (was that pipeline
circular?) from the **operational dependency** (what numerical vector input does
SI-1/SI-2 actually consume?). The two are distinct. SI-1 activities that consume
no historical value are unblocked; the suspended historical value stays
quarantined; SI-2 numerical work must use a reconstructed-`PASS` or a pinned
Paper 3 analytic vector input. No gate outcome, claim status, or numerical value
was changed — only the dependency graph was clarified.

## 2. Base main SHA

`23f8b79653fd831653f277b9c106d5f1b14c456f` (`23f8b79`).

## 3. Branch

`gate/p2-si1-unblock` (branched from `main` at the base SHA above).

## 4. Motivation for separating historical audit from operational dependency

- `P2-BETAV-CIRC-01` asks: *was the historical Finding 5 pipeline circular?*
- `P2-BETAV-RECON-01` asks: *can a newly constructed curved-background lattice
  Proca pipeline faithfully discriminate the determinant structure?*

These are not interchangeable. The provenance failure of the historical audit
must not permanently block SI-1 work that does not consume the historical
lattice value, but it also must not be converted into a scientific `PASS`.

## 5. `P2-BETAV-CIRC-01` remains SUSPENDED

Confirmed. Status unchanged by this task.

## 6. `−3.2(5)` remains unreproduced

Confirmed. Quarantined; not usable as validated numerical evidence.

## 7. Exact dependency changes

- `P2-CHANNEL-FREEZE-01`: **no longer requires `P2-BETAV-CIRC-01` to `PASS`**;
  instead requires that the provenance adjudication is complete and `−3.2(5)` is
  quarantined as unreproduced. Must freeze the selected operational vector-input
  path (reconstructed-`PASS` or pinned-analytic).
- `P2-PHASE-01`: phase enumeration may proceed after the channel freeze without
  consuming `−3.2(5)`; not blocked by `P2-BETAV-CIRC-01`.
- `P2-MULTIPHASE-GRAV-01`: full numerical kernel evaluation requires a frozen,
  admissible vector input and **may not** use the historical Finding 5 value;
  the repulsive-headwind prior is unchanged and SI-2 PASS/FAIL criteria are not
  altered.
- `P2-BETAV-CIRC-01`: gains an **Operational consequence** subsection (status
  stays `SUSPENDED`).

## 8. Exact analytic-input provenance

- Repository: `zetacheng/3-vector-sector`
- Commit SHA: `8c363ef08368f5c022278ea5f36e01496be3d5ca`
- Claim ID: `P3-C-001`
- Gate ID: `P3-FIERZ-01`
- Coupling sign: `G_ω = −G/N` (repulsive); `D_00 = g_0/(1+g_0Π_V) → 1/Π_V`.

## 9. The analytic path is not validated by `−3.2(5)`

Stated explicitly in `derivations/P2-SI1-UNBLOCK-01.md`, `results/P2-SI1-DEPENDENCY.md`,
`GATES.md`, and `MIGRATION.md`: the analytic input is validated by the pinned
Paper 3 sign/Fierz result, **not** by the suspended historical lattice value.
Using `−3.2(5)` to validate its own replacement would close a circular
provenance loop and is prohibited.

## 10. Status of `P2-BETAV-RECON-01`

`PROPOSED`, not run, replacement path only — not yet a completed replacement.

## 11. Gates and files changed

Gates (text only; the sole status *unchanged* everywhere):
`P2-BETAV-CIRC-01` (added Operational consequence), `P2-CHANNEL-FREEZE-01`,
`P2-PHASE-01`, `P2-MULTIPHASE-GRAV-01` (dependency language).

Files added:
`derivations/P2-SI1-UNBLOCK-01.md`, `results/P2-SI1-DEPENDENCY.md`,
`reports/REPORTING_POLICY.md`, `reports/2026-07-20_P2-SI1-unblock_report.md`,
`tests/test_si1_governance.py`.

Files modified:
`GATES.md`, `MIGRATION.md`, `tests/test_repository_structure.py`.

## 12. Claims changed

None. `CLAIMS.md` is unchanged by this task; `P2-C9` (`−3.2(5)`) remains
`PROPOSED`. No claim was promoted or demoted.

## 13. No claim status changed unless unavoidable

Confirmed: no claim status was changed (none was unavoidable).

## 14. No numerical value changed

Confirmed: no computed numerical value, tolerance, or result was changed. This
is documentation only.

## 15. Test result and exact test count

`python -m pytest tests -q`: **31 passed, 2 deselected** (the 2 deselected are
`@pytest.mark.slow`; full suite `-m "slow or not slow"` = 33 passed). Recorded
from the reviewed working tree; see the commit for the frozen count.

## 16. git status

Clean (`git status --porcelain` empty) at report time.

## 17. Commit SHA

Landed by the commit `docs: clarify SI-1 dependency after provenance
adjudication` on `gate/p2-si1-unblock`; the exact SHA is the branch HEAD after
this commit (recorded in the terminal summary and via `git log`).

## 18. Remote branch

`gate/p2-si1-unblock` pushed to `origin`. Not merged; no PR opened.

## 19. Limitations

- This is a dependency-graph clarification, not a scientific verdict. It does
  not answer the circularity question and does not run any reconstruction.
- `P2-BETAV-RECON-01` remains a proposed path; until it PASSES (or path B is
  frozen), SI-2 numerical execution cannot begin.

## 20. Follow-up sequence

`P2-CHANNEL-FREEZE-01` → `P2-PHASE-01`, with `P2-BETAV-RECON-01` proceeding in
parallel, all **before** any `P2-MULTIPHASE-GRAV-01` numerical execution.
