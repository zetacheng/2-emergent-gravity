# Canonical report — merge of the betaV campaign prereg + Amendment 1 fix round into `main`

**Date:** 2026-07-22. **Repository:** `zetacheng/2-emergent-gravity`.
**Type:** merge record. **Authorization:** Discriminator review APPROVED
(2026-07-22); PI authorized the merge. Strategy: `--no-ff`, no squash, no force,
branch **not** deleted, no PR. **No decisive run, no code changes** — merge only.

## Guard 1 — remote-ref verification (before merging)

- `origin/main` = `20f96f160b543fe9a4081be89b60d1ef9571daa2` ✓
- `origin/gate/p2-betav-campaign-prereg` =
  `21efcf857d6f686be32af405c861d51116ae2baa` ✓

Both matched the reviewed state; neither ref had moved.

## Guard 2 — merged the pinned SHA (not the branch ref)

`main` re-verified at `20f96f1` by `--ff-only` pull ("Already up to date"), then:

```
git merge --no-ff 21efcf8 \
  -m "merge: betaV campaign preregistration + Amendment 1 fix round (reviewed; pinned 21efcf8)"
```

Merging the **pinned SHA** `21efcf8` (never the branch ref) guarantees the merged
tip is exactly the reviewed commit. The result is a true two-parent merge:

```
<merge> 20f96f160b543fe9a4081be89b60d1ef9571daa2 21efcf857d6f686be32af405c861d51116ae2baa
```

(The merge-commit SHA is the pre-report `main` HEAD; per the self-reference rule
neither it nor the final `main` SHA is embedded in a commit — they are given in
the task response.)

## Guard 3 — post-merge verification on merged `main` (clean state)

- `python -m pytest tests -q`: **50 passed, 2 deselected**.
- `ruff check .`: **All checks passed**.
- `git merge-base --is-ancestor 21efcf8 HEAD`: **true** (21efcf8 is an ancestor of
  the merged `main`).
- `git status --porcelain`: **clean**.

All three guards passed; the merge was pushed.

## What this merge lands (permanent record)

- The betaV campaign **pre-registration** (`derivations/P2-BETAV-CAMPAIGN_prereg.md`)
  with Amendment 1 (pilot eps-grid fix; Arm-H rulings A2.1/A2.2 recorded;
  three-output canonical wording; n=6 probe downgraded; §(c7) comparator
  clarifications).
- The **blind harness** (`scripts/P2-BETAV-CAMPAIGN/harness_compute.py`,
  schema `…/compute/v2` with the `required_diagnostics` manifest + keyed
  `diagnostics`) and the **separated comparator** (`compare.py`, required-variant
  validity, uniform `τ_denom`, diagnostics-gate-the-audit, integrity/scientific
  exit contract).
- The **machine guards** (`tests/test_betav_campaign_guards.py`) and the
  **negative fixtures** (`tests/test_betav_campaign_comparator.py`).
- The **NON-DECISIVE** re-qualified pilot artifacts (4-eps grid) with sidecars and
  comparison outputs.
- Gate bookkeeping: `P2-BETAV-NUMREPRO-01` = `SPECIFIED` (rules registered, not
  run); `P2-BETAV-CIRC-01` = `SPECIFIED` with the audit rules filled.

**Does not:** run any decisive computation, change `P2-C9`, or touch the
`−3.2(5)` quarantine. The decisive **Arm H** run is a separate task with its own
prompt and its own PI authorization.

## Repository state (pre-report)

`git ls-remote --heads origin` for `main` and the branch (branch still exists):

```
a686bf3a9d2269da750a04403f0bb815c72280df  refs/heads/main
21efcf857d6f686be32af405c861d51116ae2baa  refs/heads/gate/p2-betav-campaign-prereg
```

`git status` on `main`: clean. The branch `gate/p2-betav-campaign-prereg` is
preserved (not deleted), still at the reviewed `21efcf8`.
