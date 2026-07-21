# Canonical report — merge of recovery batch 2 (+ session-log addendum) into `main`

**Date:** 2026-07-21. **Repository:** `zetacheng/2-emergent-gravity`.
**Type:** merge record. Reviewers approved (Claude sign-off; ChatGPT
`BATCH-2 ADDENDUM VERIFIED / APPROVED FOR MERGE REVIEW`); PI authorized the
merge. Strategy: `--no-ff`, no squash, no force, branch **not** deleted, no PR.
**No gate status change; `P2-C9` and the `−3.2(5)` quarantine untouched.**

## 1. SHAs

- **Pre-merge `main`:** `aaa36948c963cdf298e3da5258c1fc2e19b924ec` — verified
  unchanged against **`origin/main`** (Part 0) and again by `--ff-only` pull
  ("Already up to date").
- **Pre-Part-A branch tip:** `2aa0dec8ad44161178a8e704f838d501ef9c27a5` —
  verified against `origin/recover/batch2-gfvec-and-foundations` (Part 0).
- **Part-A commit (docs-only):** `324ef969476dd1c7488055971a3ed47dadf21767` —
  the merged tip; `git diff --name-only 2aa0dec..324ef96` = exactly
  `DECISION_LOG.md` + `scripts/recovered_2026/PROVENANCE.md`; remote tip
  re-verified after push.
- **Merge commit (= pre-report `main` HEAD):**
  `1ff42fd86b1e51d27a2e7cece319f0546ea25505` — a true two-parent merge of the
  **pinned** Part-A SHA:

  ```
  1ff42fd86b1e51d27a2e7cece319f0546ea25505 aaa36948c963cdf298e3da5258c1fc2e19b924ec 324ef969476dd1c7488055971a3ed47dadf21767
  ```

Per the self-reference constraint, this report commit's own SHA and the
resulting final `main` SHA are **not** embedded here (given in the task
response, not amended in).

## 2. Part A — convergent-evidence wording + standards-evolution note (docs only)

Two reviewer-suggested permanent-record touches, committed as `324ef96`:

1. `PROVENANCE.md` (batch-2 addendum) and `DECISION_LOG.md` now state the
   Phase-1 ↔ historical-session relationship as **convergent evidence, not
   mutual verification**: *"Two independent lines of reasoning … converged on
   the same engineering decision (a gauge-fixed / Stueckelberg minimal-vector
   construction). This is convergent evidence for the design direction, not
   mutual verification of any numerical result."*
2. `DECISION_LOG.md` gained the **standards-evolution** sentence: *"The
   historical programme itself evolved its standards over time: target-aware
   exploration → a designed precision campaign → the present blind
   preregistration and dual-gate discipline. This is recorded as natural
   maturation of the programme's own standards, not as a past-wrong/now-right
   judgment."*

**Docs-only guard:** the committed diff touched **exactly** the two documents;
no code, gate, or results artifact changed. Merging the **pinned** Part-A SHA
(not the branch ref) guarantees the merged tip is exactly the reviewed +
Part-A commit.

## 3. Part C — post-merge verification on merged `main` (at the merge commit)

- **Batch-2 originals:** `scripts/recovered_2026/batch2/` contains **13**
  `.py` originals. sha256 spot-check:
  - `gfvec_loop.py` = `cb8b2f656d218c3c5a1e94608586ab68edd7c71d8b19f8328793d8218d83b310` ✓
  - `fierz_verify.py` = `bb83b82dcf35ab4f794cd0172d6be226f01799bd0d4cfe2a512adde55e28e196` ✓
  (both match the batch-2 report.)
- **Session log:** `results/recovered-2026/session_log_full.md` present and
  **byte-identical**; `sha256 -c` against the sidecar → `OK`
  (`61c54701d7e61f31168aaadd0a6ee70c964f4b2175e92c1d9dd3a02749303a9c`).
- **Run-record index:** 15 rows present in `PROVENANCE.md`; the two bold rows
  **R10** (direct Proca: `n=32`, `m_V a=0.11–0.20`, `β_V=−7.2e-4`, ratio
  `−3.2(5)`, subwindows `−2.6`/`−3.4`) and **R12** (gfvec summary: `0.125–0.55`,
  `−2.4…−2.9`) are present and kept **distinct** (two windows).
- **Seagull scope clarification** present: the gfvec q-dependent seagull
  statement "does not contradict the Phase-1 report's" implementation-specific
  `proca_loop`-extractor statement.
- **`MISSING.md`:** #2 never-run-computation sentence; #3 resolved (session
  side); #6 finite-q position-space validation script — all present.
- **`DECISION_LOG.md`:** the historical-criterion sentence ("enforces the
  programme's own historical criterion, not a retroactive standard") **and** the
  Part-A standards-evolution note — both present.
- **Gates:** `P2-BETAV-CIRC-01` = `SPECIFIED` (Phase-1 adjudication fields +
  batch-2 Solodukhin addendum present); `P2-BETAV-NUMREPRO-01` = `PROPOSED`
  (pre-registration input note present); `P2-C9` = `PROPOSED`; `−3.2(5)`
  quarantined; Ward summary **recorded-not-adopted** present.
- **Tests/lint:** `python -m pytest tests -q` → **34 passed, 2 deselected**;
  `-m "slow or not slow"` → **36 passed**; `tests/test_si1_governance.py` →
  **12 passed**; `ruff check .` → **All checks passed**; `git status
  --porcelain` → clean.

## 4. What this merge does / does not do

**Does** (permanent record): the 13 recovered batch-2 originals (the gauge-fixed
Solodukhin construction and the Fierz foundations), their validation (Fierz
algebra; constant-h machinery to ~1e-7), the complete historical session log
with a 15-row auditable run-record index, the pinned (historically reported)
`−3.2(5)` provenance, the missing-artifacts registry, and the governance
conclusion that the current quarantine enforces the programme's own historical
promotion criterion.

**Does not:** verify any historical number; change any gate status; promote
`P2-C9`; or touch the `−3.2(5)` quarantine. The next scientific step (the
blind-harness precision campaign / operator-identity audit and the separate
NUMREPRO pre-registration) is a subsequent decision, not part of this merge.

## 5. Repository state (pre-report)

`git status` on `main`: clean. `git ls-remote --heads origin` (pre-report):

```
5395d4b3f5c1d81dc9954f484802d9f534009dc1  refs/heads/claude/paper-2-independent-verification-dysdp0
ca334fe0361d76fadb68e1866f71f0c40a4ed858  refs/heads/gate/p2-betav-circ
05a1e7f81eb814f0bb3e438e95e261aa07900031  refs/heads/gate/p2-betav-decomp
c1f1bec27085335b077dbdd26cb460f994acffd6  refs/heads/gate/p2-si1-unblock
1ff42fd86b1e51d27a2e7cece319f0546ea25505  refs/heads/main
324ef969476dd1c7488055971a3ed47dadf21767  refs/heads/recover/batch2-gfvec-and-foundations
836bf1441603565ba8d07207f31fabee8f04e5fc  refs/heads/recover/betav-complete
cdcbd840df8252d59ecfd29e662a797adc7216f9  refs/heads/recover/lattice-gravity-engine
b02c70279b382e05d415b23b9b5f562e3c5e2156  refs/heads/sea-ice/gate-stubs
```

`recover/batch2-gfvec-and-foundations` remains at `324ef96` (not deleted, as
required).
