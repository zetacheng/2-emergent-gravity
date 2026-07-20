# Canonical report — merge `gate/p2-si1-unblock` into `main`

**Date:** 2026-07-20. **Repository:** `zetacheng/2-emergent-gravity`.
**Task type:** controlled merge of the reviewed SI-1 governance clarification
(docs/ledger-graph only; no scientific content).

## 1. Executive summary

This lands the SI-1 operational dependency clarification (`P2-SI1-UNBLOCK-01`)
into `main`. It separates the **historical audit** (`P2-BETAV-CIRC-01`, does the
absent Finding 5 pipeline's projection secretly fix the ratio?) from the
**operational dependency** (what numerical vector input SI-1/SI-2 consumes).
`P2-BETAV-CIRC-01` stays `SUSPENDED`; the historical value `β_V/β_B = −3.2(5)`
stays unreproduced and quarantined; SI-1 (channel freeze, phase/parameter/Fierz
registration, SI-2 metric pre-registration) is operationally unblocked; SI-2
numerical execution remains gated on `P2-BETAV-RECON-01 = PASS` or a frozen
pinned Paper 3 analytic vector input. No gate status, claim status, numerical
value, tolerance, or scientific verdict is changed by this merge.

## 2. Source branch

`gate/p2-si1-unblock`

## 3. Source branch HEAD SHA

`4f6aa74d47b0754c74fa314c326c23429a76fc50` (`4f6aa74`)

## 4. Substantive governance commit SHA

`642bb9a72a6356891e8839ffaab925ec177e6606` (verified ancestor of the source
HEAD). The later commit `4f6aa74` is a report-only finalize of the SI-1 report.

## 5. Target branch

`main`

## 6. Pre-merge main SHA

`23f8b79653fd831653f277b9c106d5f1b14c456f` (`23f8b79`)

## 7. Merge-base SHA

`23f8b79653fd831653f277b9c106d5f1b14c456f` — identical to `origin/main`; the
source branch is based directly on the merged provenance-adjudication main, with
no divergence.

## 8. Branch topology

`origin/main..origin/gate/p2-si1-unblock` contains exactly two commits:
- `642bb9a` — `docs: clarify SI-1 dependency after provenance adjudication`
  (substantive governance)
- `4f6aa74` — `docs: finalize the SI-1 unblock canonical report` (report-only)

No unexpected scientific code, raw numerical artifact, paper text, or
claim-status change is present.

## 9. Files changed (vs base `23f8b79`)

Modified: `GATES.md`, `MIGRATION.md`, `tests/test_repository_structure.py`.
Added: `derivations/P2-SI1-UNBLOCK-01.md`, `results/P2-SI1-DEPENDENCY.md`,
`reports/REPORTING_POLICY.md`, `reports/2026-07-20_P2-SI1-unblock_report.md`,
`tests/test_si1_governance.py`.
(This merge-report file is added by the pre-merge report commit below.)
No change to `scripts/`, any `results/*/raw/`, `paper/`, or `CLAIMS.md`.

## 10. Source-branch test results

Clean checkout of `gate/p2-si1-unblock` at `4f6aa74`:
- `python -m pytest tests -q` → **31 passed, 2 deselected**
- `python -m pytest tests -q -m "slow or not slow"` → **33 passed**
- `git status --porcelain` → empty.

## 11. Scientific invariants checked (source branch)

All twelve invariants verified directly from the source branch:
`P2-BETAV-CIRC-01 = SUSPENDED`; `P2-BETAV-RECON-01 = PROPOSED`; `−3.2(5)`
labelled unreproduced and prohibited as validated evidence;
`P2-CHANNEL-FREEZE-01` no longer requires `P2-BETAV-CIRC-01` to PASS;
`P2-PHASE-01` proceeds only after the freeze without consuming `−3.2(5)`;
`P2-MULTIPHASE-GRAV-01` may not consume the historical extraction; the analytic
input pinned to `P3-C-001` / `P3-FIERZ-01` @
`8c363ef08368f5c022278ea5f36e01496be3d5ca`, repulsive (`G_ω = −G/N`), headwind,
not validated by `−3.2(5)`; no `CLAIMS.md` promotion/demotion; no numerical
value/tolerance/result changed.

## 12. Confirmation — `P2-BETAV-CIRC-01 = SUSPENDED`

Confirmed.

## 13. Confirmation — `P2-BETAV-RECON-01 = PROPOSED`

Confirmed.

## 14. Confirmation — `−3.2(5)` remains unreproduced and quarantined

Confirmed. Must not be cited or consumed as validated numerical evidence.

## 15. Confirmation — Paper 3 analytic input pinned

`zetacheng/3-vector-sector`, `P3-C-001` / `P3-FIERZ-01`, commit
`8c363ef08368f5c022278ea5f36e01496be3d5ca`.

## 16. Confirmation — no scientific change

No claim status, numerical value, tolerance, or scientific verdict was changed.

## 17. Confirmation — no PR opened

No pull request was opened for this merge.

## 18. Authorization scope

This task authorizes **SI-1 governance progression only**. It does **not**
authorize SI-2 numerical execution, which stays gated on `P2-BETAV-RECON-01 =
PASS` or a frozen pre-registered Paper 3 analytic vector path.

## 19. Merge execution record

- Merge command used: `git checkout main && git pull --ff-only origin main &&
  git merge --no-ff gate/p2-si1-unblock -m "merge: land the SI-1 operational
  dependency clarification"` (no squash).
- Merge commit SHA: `dc4ab9e7dfb21ddb0428d688bb257f2178da7f0a`
  (two parents: `23f8b79` main + `c1f1bec` source — a genuine `--no-ff` merge).
- Post-merge `main` SHA (at merge): `dc4ab9e7dfb21ddb0428d688bb257f2178da7f0a`
  (this report's finalize commit is a report-only successor on top; its SHA is
  the resulting `main` HEAD, reported in the terminal summary).
- Post-merge test results: `python -m pytest tests -q` → **31 passed, 2
  deselected**; `-m "slow or not slow"` → **33 passed**. Counts unchanged from
  the source branch (no new tests on main).
- Final `git status`: clean (`git status --porcelain` empty).
- Source branch HEAD: `c1f1bec27085335b077dbdd26cb460f994acffd6`; remote
  `origin/gate/p2-si1-unblock` = `c1f1bec` (identical). **Source branch remains
  intact — not deleted.**
- `--no-ff` used: yes. **No PR opened.** No scientific file (`scripts/`,
  `results/*/raw/`, `paper/`, `CLAIMS.md`) was changed during the merge task.
- **SI-1 is now operationally unblocked on `main`.** **SI-2 numerical execution
  remains blocked** pending `P2-BETAV-RECON-01 = PASS`, or a frozen
  pre-registered Paper 3 analytic vector path
  (`P3-C-001` / `P3-FIERZ-01` @ `8c363ef08368f5c022278ea5f36e01496be3d5ca`).

### Post-merge gate statuses on `main` (verified)

- `P2-BETAV-CIRC-01` = `SUSPENDED`
- `P2-BETAV-RECON-01` = `PROPOSED`
- `β_V/β_B = −3.2(5)` — unreproduced, quarantined, not validated evidence.
- No `CLAIMS.md` row is `VERIFIED`; no historical claim upgraded or downgraded.
