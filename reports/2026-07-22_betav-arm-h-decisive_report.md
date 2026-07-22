# Report — DECISIVE Arm H (NUMREPRO): single frozen-harness run, verdict recorded as-is

**Date:** 2026-07-22. **Repository:** `zetacheng/2-emergent-gravity`.
**Branch:** `run/p2-betav-arm-h-decisive` (off `main` = `11c8ee9`).
**No merge, no PR.** **Authorization:** PI authorized **this Arm-H run only**.
**Arm P is NOT authorized** (it requires its own review of these Arm-H results
first) and was not run. The harness was frozen — no edits to
`harness_compute.py`, `compare.py`, the schema, the tests, or the prereg doc.

## Part 0 — verification

- `git merge-base --is-ancestor 21efcf8 origin/main` → **true** (the reviewed
  prereg + fix round is merged).
- `git rev-parse origin/main` = `11c8ee93ccec026a5757897e93fdede1d4b70c03`.
- `git checkout main`; `HEAD == origin/main` → **true** (no stale/contaminated
  local main); working tree clean.
- Branched `run/p2-betav-arm-h-decisive` off `main`.

## Task 1 — the decisive compute (one run)

Command (executed exactly once; deterministic, no RNG):

    python scripts/P2-BETAV-CAMPAIGN/harness_compute.py --arm H

- **Start:** `2026-07-22T21:42:01Z` · **End:** `2026-07-22T22:18:47Z`
  (~36.8 min) · **shell exit code:** `0`.
- **Raw artifact:** `results/P2-BETAV-CAMPAIGN/raw/H.json` (created
  `2026-07-22 22:18:47Z`) + external sidecar `H.json.sha256`.
  `H.json` sha256 =
  `8576d560252eadeb66fcaf99ff899af9ceacc9cb91546007c58b56c19e27010b`.
- **Sidecar verification:** `sha256sum -c H.json.sha256` → `H.json: OK`.
- **Schema (frozen v2):** `schema_version = p2-betav-campaign/compute/v2`; arm H;
  species `[proca, boson]`; `n=32`; `required_diagnostics = []` (Arm H requires
  none); `mutation = none`; 9 VERDICT variants (baseline, eps-drop-largest,
  eps-drop-smallest, fit-order, mass-drop-one[0..3], window-shift). No ratios, no
  targets, no self-hash. `compute_git_commit = 11c8ee9…` — the code-state HEAD the
  frozen computation ran from; **not edited** (it is correctly an ancestor of the
  later artifact commit, as the comparator's ancestry check expects).
- **Environment metadata (from the JSON):** Python `3.11.15`, NumPy `2.4.6`,
  platform `Linux-6.18.5-x86_64-with-glibc2.39`.

Compute commit (compute only, preceding the comparison per prereg (g)):
`ab36ca4`.

## Task 2 — the comparison (separate, later commit)

Command (run once; the comparator **prints** its result JSON, stdout captured to
the frozen artifact path — the same convention as the pilot):

    python scripts/P2-BETAV-CAMPAIGN/compare.py --json results/P2-BETAV-CAMPAIGN/raw/H.json \
      > results/P2-BETAV-CAMPAIGN/H_comparison.json     # exit code 0

- **Artifact:** `results/P2-BETAV-CAMPAIGN/H_comparison.json`, sha256 =
  `918a9b87a8cac8fdff351d85bbfba66d09a80053926d370b634b76b3f11baa1f`
  (digest-in-report; no non-standard sidecar, per the pilot convention).
- **Five refuse-checks — all pass, in order:** (1) sidecar hash OK; (2) prereg-doc
  hash OK; (3) registered-source hashes OK; (4) compute commit is ancestor of
  HEAD; (5) schema version OK.
- **Status fields:** `integrity_status = VERIFIED`,
  `scientific_status = ASSESSABLE`, shell exit code `0`.

### Verdict (stated once, plainly, no spin)

**NUMREPRO verdict: INCONCLUSIVE.** Reason: the registered **2σ interval does not
fit inside the band** `[−3.7, −2.7]`. Numbers as emitted:

- central `R_H = β_V/β_B ≈ −2.2313` (baseline variant);
- battery `σ_H ≈ 4.0834`; 2σ interval `[−10.398, +5.935]`; band `[−3.7, −2.7]`;
- `assessable = true`, `harness_invalid = false`.

Per-variant `R_H` (as recorded):

| variant | R_H |
|---|---|
| baseline | −2.231 |
| eps-drop-largest | −5.608 |
| eps-drop-smallest | **+1.852** (sign flip; drives σ_H) |
| fit-order | −3.592 |
| mass-drop-one[0] | −3.791 |
| mass-drop-one[1] | −3.652 |
| mass-drop-one[2] | −3.511 |
| mass-drop-one[3] | −3.376 |
| window-shift | −3.519 |

**Interpretation (taxonomy).** This is a **scientifically assessable**
INCONCLUSIVE — the ordinary "2σ interval straddles the band boundary" case, with
`integrity_status=VERIFIED` and `scientific_status=ASSESSABLE` and exit 0. It is
**not** `HARNESS_INVALID` and **not** `REFUSED`: no required verdict variant was
invalid, no denominator failed, no integrity/schema check failed. It is exactly
the pre-registered honest expectation (c2): the historical `n=32` configuration
**cannot distinguish `−3` at the registered confidence** — a statement about the
configuration's discriminating power, **not** a failure of the operator identity
(that is Arm P's job, which is not run) and **not** a harness defect. The battery
spread is led here by the eps-drop-smallest VERDICT variant (its 3-point eps fit
flips the sign to `+1.85`), not by the window-shift variant alone. Recorded as-is;
no band widening, no variant changes, no rerun.

Comparison commit: `da62d44`.

## Task 3 — gate bookkeeping (record, never promote)

`GATES.md` `P2-BETAV-NUMREPRO-01` now carries three **separate** fields:

```
Status: RUN
Verdict: INCONCLUSIVE (registered 2σ interval exceeds the NUMREPRO band boundary …)
Artifact: results/P2-BETAV-CAMPAIGN/H_comparison.json (sha256: 918a9b87…)
```

(`RUN` added to the allowed-status list = "the registered test executed"; the
verdict is an independent field, never folded into the status.) Unchanged:

- `P2-BETAV-CIRC-01` = `SPECIFIED` (its decisive test is Arm P — **not run**);
- `P2-C9` = `PROPOSED`; the `−3.2(5)` quarantine is **unchanged**. Canonical
  wording quoted in the gate: *quarantine release or `P2-C9` promotion requires
  the registered dual-gate conditions AND explicit consideration of the
  separately recorded Arm-P historical-promotion outcome, followed by PI+reviewer
  authorization; no script automatically promotes.*
- Governance suite stays green: **14 passed** — the dual-gate tests confirm a
  NUMREPRO verdict alone flips nothing (`P2-C9` still `PROPOSED`, quarantine
  intact).

Gate commit: `fef78fc`.

## Task 4 — guards (clean checkout)

- `python -m pytest tests -q`: **50 passed, 2 deselected**.
- `tests/test_si1_governance.py`: **14 passed**;
  `tests/test_betav_campaign_guards.py`: **5 passed**;
  `tests/test_betav_campaign_comparator.py`: **9 passed**.
- `ruff check .`: **All checks passed**.
- `git status --porcelain`: clean.

## Commit chronology (off `main` `11c8ee9`)

```
ab36ca4 decisive: Arm H compute (n=32, frozen harness, blind) — raw Z/beta tables + sidecar
da62d44 decisive: Arm H comparison — verdict recorded as emitted (NUMREPRO output (2) of three)
fef78fc gate: NUMREPRO-01 -> RUN, verdict recorded; quarantine and P2-C9 untouched
```

Pre-report HEAD: `fef78fc` (compute commit precedes the comparison commit, per
prereg (g)). This report is the next commit; its own SHA is in the task response,
not embedded. `git ls-remote` is captured in the task response after the push.

## What this task did NOT do

No Arm P (n=48 audit + historical criterion) — unauthorized. No decisive rerun,
no band widening, no variant/mass-set changes, no harness edits, no `P2-C9`
promotion, no change to the `−3.2(5)` quarantine. The Discriminator and PI review
these Arm-H results on clean clones; only after that may Arm P be considered for
its own authorization. Nothing here pre-commits that decision.
