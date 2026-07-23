# Canonical report — merge of the Arm H decisive run + governance correction into `main`

**Date:** 2026-07-22. **Repository:** `zetacheng/2-emergent-gravity`.
**Type:** merge record. **Precondition:** Discriminator (ChatGPT) reviewed
`run/p2-betav-arm-h-decisive` @ `9b0ceed` (including the approved
governance-correction commit) on a clean clone and approved the merge; PI
authorized. Strategy: `--no-ff`, no squash, no force, branch **not** deleted, no
PR. **Merge only — no Arm P, no code changes, no other work.**

## Guard 1 — remote-ref verification

- `origin/main` = `11c8ee93ccec026a5757897e93fdede1d4b70c03` ✓
- `origin/run/p2-betav-arm-h-decisive` =
  `9b0ceedf820d65d4f7b2bbeea7df043c88d8e72a` ✓

Both matched the reviewed state; neither ref had moved.

## Guard 2 — merged the pinned SHA (not the branch ref)

`main` re-verified: `git rev-parse HEAD == git rev-parse origin/main` (and
`--ff-only` pull "Already up to date"). Then:

```
git merge --no-ff 9b0ceed \
  -m "merge: Arm H decisive run + governance correction — NUMREPRO verdict INCONCLUSIVE recorded as-is (reviewed; pinned 9b0ceed)"
```

Merging the pinned SHA `9b0ceed` (never the branch ref) guarantees the merged tip
is exactly the reviewed commit. True two-parent merge:

```
<merge> 11c8ee93ccec026a5757897e93fdede1d4b70c03 9b0ceedf820d65d4f7b2bbeea7df043c88d8e72a
```

## Guard 3 — post-merge verification on merged `main` (clean state)

- `python -m pytest tests -q`: **50 passed, 2 deselected** (matched the
  expectation).
- `ruff check .`: **All checks passed**.
- `git merge-base --is-ancestor 9b0ceed HEAD`: **true**.
- The **governance-correction section** ("Governance correction (2026-07-22):
  protocol noncompliance in the gate commit") is present at the end of
  `reports/2026-07-22_betav-arm-h-decisive_report.md` — the merge carries the
  **corrected** state (`9b0ceed`), not the pre-correction `6c77c18`.
- `GATES.md` `P2-BETAV-NUMREPRO-01`:
  - `Status: RUN`
  - `Verdict: INCONCLUSIVE (registered 2σ interval exceeds the NUMREPRO band
    boundary — a scientifically assessable outcome, not a harness failure)` (a
    **separate** field, not folded into status)
  - `Artifact: results/P2-BETAV-CAMPAIGN/H_comparison.json (sha256:
    918a9b87a8cac8fdff351d85bbfba66d09a80053926d370b634b76b3f11baa1f)`
- `P2-BETAV-CIRC-01` = `SPECIFIED` (unchanged); `P2-C9` = `PROPOSED` and the
  `−3.2(5)` quarantine **untouched**.
- Working tree clean.

## What this merge lands

The decisive Arm-H (NUMREPRO) run, recorded as-is: the blind `n=32` compute
(`results/P2-BETAV-CAMPAIGN/raw/H.json` + sidecar), the comparison
(`H_comparison.json`, `integrity_status=VERIFIED`, `scientific_status=ASSESSABLE`,
exit 0), the **NUMREPRO verdict = INCONCLUSIVE** (2σ interval `[−10.40, +5.94]`
does not fit the band `[−3.7, −2.7]`), the gate bookkeeping (`NUMREPRO-01` →
`RUN` with the verdict recorded), and the **governance-correction** commit
(acknowledging and retaining the reviewed test change, retracting the false
"no test edits" statement, and superseding the over-claimed expectation wording).

**Does not:** run Arm P, change `P2-C9`, or touch the `−3.2(5)` quarantine. The
Arm-H branch `run/p2-betav-arm-h-decisive` **must remain present** (not deleted).

## Repository state (pre-report)

The merge commit is the pre-report `main` HEAD:
`3c0c484dcac68f203b5dcae25d58245b759549d3`. Per the reporting rule, this report's
own commit SHA and the post-push `git ls-remote` output are given in the task
response, not embedded here.
