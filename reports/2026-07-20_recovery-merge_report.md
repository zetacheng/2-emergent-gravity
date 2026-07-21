# Canonical report — merge the Paper 2 recovery branches

**Date:** 2026-07-20. **Repository:** `zetacheng/2-emergent-gravity`.
**Type:** governance correction + dual `--no-ff` merge (no squash, no PR).

## 1. Pre-merge main SHA

`7af645f18490d30256719f967c1d07cc3b7946b9` (verified unchanged before merging).

## 2. Source branch SHAs (initial → final)

- `recover/lattice-gravity-engine`: `cdcbd84…` (unchanged; = reviewed ancestor).
- `recover/betav-complete`: `be4874d…` (initial) → `836bf1441603565ba8d07207f31fabee8f04e5fc` (final, after the Part-A governance correction).

## 3. Reviewed ancestor SHAs

- engine: `cdcbd840df8252d59ecfd29e662a797adc7216f9`
- betaV: `be4874d2323aa92031fb3060ae51e67877cb7c03`

## 4. Topology and ancestry checks

`main(7af645f) → engine(cdcbd84) → betaV(be4874d→836bf14)`, linear.
- `origin/main` == `7af645f` (unchanged). ✔
- `cdcbd84` is an ancestor of `origin/recover/lattice-gravity-engine`. ✔
- `be4874d` is an ancestor of `origin/recover/betav-complete`. ✔
- engine is an ancestor of betaV. ✔
- merge-base(main, engine) = `7af645f`; merge-base(engine, betaV) = `cdcbd84`. ✔

## 5. Governance-correction commit SHA

`836bf1441603565ba8d07207f31fabee8f04e5fc`
(`docs: separate circularity verdict from numerical reproduction`; local = remote).

## 6. Engine merge commit SHA

`d37974c5a201b785880c4a7fd4f131db4e381aad`
(`merge: recover the historical lattice gravity engine (Class A)`; parents
`7af645f` + `cdcbd84`).

## 7. betaV merge commit SHA

`2bacfd09683d92152b71cddc6dcfba56c95b3c46`
(`merge: complete the betaV pipeline recovery and specify CIRC/NUMREPRO gates`;
parents `d37974c` + `836bf14`; no conflict).

## 8. Post-merge main SHA (before this report commit)

`2bacfd09683d92152b71cddc6dcfba56c95b3c46`. (The final `main` HEAD is this
report's own commit; the Git ref is authoritative — no self-referential
finalization commit is added.)

## 9. Seven historical recovered originals + hashes (byte-identical, unedited)

| File | sha256 |
|---|---|
| `scripts/recovered_2026/speed_check.py` | `8a374601161dd324795c2f1c9f7cc9d48031d83c5cc05e9896ae1e2814b1044c` |
| `scripts/recovered_2026/seagull_check.py` | `6ec034e5a30e24d205c43c7dd0ea39c90a89f67c9db0da6e734a68862acefd90` |
| `scripts/recovered_2026/tt_check.py` | `a40592a3b320cd9f118b3d96bd61abb10d5b20087d6b7a201dae5deabf90ba00` |
| `scripts/recovered_2026/boson_loop.py` | `32d6a4e0b9cca8ec4debb80758f77d0574d98a299492cb1ab9cfe2fdd26c08c2` |
| `scripts/recovered_2026/structure_decomp.py` | `87d311fa4d86bb1c6862ace85bdd2c4a232db4f44e1662696f46c7226675fb9a` |
| `scripts/recovered_2026/mlog_coeff.py` | `9f4343f14e70e57122e62d4aa12a3c8b7f708455af03fa74cd18d87751d107f3` |
| `scripts/recovered_2026/proca_loop.py` | `b2361db94eae0995a5a81b16552bb8cd5b4afa049d015ea9401e3b8eac1bc8f5` |

All seven confirmed byte-identical to the PI's attachments (`cmp`) on merged
`main`, and unedited (ruff-excluded).

## 10. Recovered originals vs new reproduction harnesses (distinct)

- **Historical recovered originals (7, above):** written by the PI, landed
  verbatim, hash-pinned.
- **Repository-created audit/reproduction harnesses (not historical):**
  `scripts/recovered_2026/reproduce_check.py`
  (`821ccb1f1937e6ba424a7c5c3fccb36edeae35223ca01179b268e10fee703c74`),
  `scripts/recovered_2026/reproduce_betav.py`
  (`9a383aa2ac244e2a312b6057524e581cd56860dbb3094271e589d90dfbb833a4`).
- **Recovered artifact:** `results/recovered-2026/fig_mlog.pdf`
  (`11cdd36c19b73f67200802a87e5720a7700239d2d94e081a5f118bc069bf565e`).

## 11. Artifact hash verification

Every recorded sha256 (7 originals + `fig_mlog.pdf`) in
`scripts/recovered_2026/PROVENANCE.md`,
`reports/2026-07-20_gravity-engine-recovery_report.md`, and
`reports/2026-07-20_betav-complete-recovery_report.md` matches the merged-`main`
files. ✔

## 12. Class-A reproduction summary

`speed_check` reproduces the light-cone numbers quantitatively (Case A machine
precision, Case B `≤2.6%`); `seagull_check`/`tt_check`/`boson_loop` reproduce the
Finding 4 sign structure (`Z_h>0`, `ξ_ind<0`) with a recorded finite-`n` residual
on `seagull` `xi_h → −1/6`. Detail: `results/recovered-2026/REPRODUCTION.md`.

## 13. betaV reproduction summary

- scalar `β_B`: **reproduced** within the recorded finite-grid behavior
  (`n=12:+3.00e-4 → n=20:+2.82e-4`, into `+2.50…2.64e-4`).
- vector `β_V` **sign**: **reproduced** (negative; `Z_V(m)` rises).
- ratio `β_V/β_B` **magnitude**: **not yet reproduced** — accessible-grid ratios
  are artifact/grid limited (`n=12:≈−61`, `n=16:≈−16`; heavy window flips sign).
  Detail: `results/recovered-2026/BETAV_REPRODUCTION.md`.

## 14–17. Gate / claim states on merged `main`

- `P2-GRAV-ENGINE-RECOVERED-01` = **PASS**.
- `P2-BETAV-CIRC-01` = **SPECIFIED** (not PASS, not FAIL). CIRC Scope
  (promotion-boundary) wording present.
- `P2-BETAV-NUMREPRO-01` = **PROPOSED** (not run).
- `P2-C9` = **PROPOSED**.

## 18. Dual-gate claim-promotion rule (exact)

Promotion of `P2-C9` requires **both** `P2-BETAV-CIRC-01 = PASS` **and**
`P2-BETAV-NUMREPRO-01 = PASS`. Neither gate alone is sufficient. A CIRC PASS
establishes non-circular discriminating power only; it does not numerically
reproduce the physical `k=1` value and does not promote `P2-C9`.

## 19. `−3.2(5)` quarantine

`β_V/β_B = −3.2(5)` remains **quarantined and not validated** — an unpromoted,
unreproduced (at magnitude) paper value. The governance tests
`test_finding5_value_quarantined_as_unreproduced` and
`test_finding5_claim_not_promoted` are unchanged and pass.

## 20. Tests and ruff

Clean checkout of merged `main`: `python -m pytest tests -q` → **34 passed, 2
deselected**; `-m "slow or not slow"` → **36 passed**. `ruff check .` → clean.

## 21. git status

`git status --porcelain` empty (clean) at merge time.

## 22. Remote refs (after push)

`main` = the report-commit HEAD; `recover/lattice-gravity-engine` = `cdcbd84`;
`recover/betav-complete` = `836bf14`; plus the pre-existing
`claude/paper-2-independent-verification-dysdp0`, `gate/p2-betav-circ`,
`gate/p2-si1-unblock`, `sea-ice/gate-stubs`.

## 23. Branches preserved

Both recovery branches remain on `origin` (not deleted).

## 24. No PR

No pull request was opened.

## 25. No recovered historical source edited

The seven historical originals are byte-identical and untouched; only
governance/report/test files changed (Part A), plus the two `--no-ff` merge
commits.

## 26. No numerical claim promoted

`CLAIMS.md` is unchanged; `P2-C9` stays `PROPOSED`; no claim is `VERIFIED`.

## What comes next (not this task)

`P2-BETAV-CIRC-01` `k`-scan (discriminating power only), and — separately —
`P2-BETAV-NUMREPRO-01` preregistration + execution (numerical `k=1`
convergence). `P2-C9` promotion needs both to PASS.
