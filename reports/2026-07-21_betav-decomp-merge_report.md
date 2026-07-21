# Canonical report — merge of the Phase-1 βV decomposition adjudication into `main`

**Date:** 2026-07-21. **Repository:** `zetacheng/2-emergent-gravity`.
**Type:** merge record. Reviewers approved (Claude sign-off; ChatGPT
`APPROVED FOR MERGE REVIEW`); PI authorized the merge. Merge strategy:
`--no-ff`, no squash, no force, branch **not** deleted, no PR.

## 1. SHAs

- **Pre-merge `main`:** `2c396fc9ffadfc961c636ae3e3aae7740a1f14a4` (verified
  unchanged by an `--ff-only` pull before merging — "Already up to date").
- **Branch tip merged (`gate/p2-betav-decomp`):**
  `05a1e7f81eb814f0bb3e438e95e261aa07900031` (attestation commit at tip).
- **Merge commit (= pre-report `main` HEAD):**
  `4c70628fce287c97e5144cf3a65d37a866b72e63` — a true two-parent merge:

  ```
  4c70628fce287c97e5144cf3a65d37a866b72e63 2c396fc9ffadfc961c636ae3e3aae7740a1f14a4 05a1e7f81eb814f0bb3e438e95e261aa07900031
  ```

The report commit that carries this file sits one commit after the merge
commit; per the same self-reference constraint as the attestation, neither this
report commit's own SHA nor the resulting final `main` SHA is embedded here
(they are given in the task response, not amended in after the fact).

## 2. Part-B verification on merged `main` (at the merge commit)

### Gate specification consistency (two-step grep)

**(1) Live portion — must be zero-hit:**

```
$ sed -n '/## P2-BETAV-CIRC-01/,/### Superseded specification/p' GATES.md | grep -nE 'runnable|decisive'
(no output)
```

**(2) Full section — historical hits allowed inside the marked block:**

```
$ sed -n '/## P2-BETAV-CIRC-01/,/## P2-BETAV-NUMREPRO-01/p' GATES.md | grep -nE 'runnable|decisive'
(no output)
```

Both are zero-hit: the live specification carries no stale `runnable`/`decisive`
wording, and the "Superseded specification (historical record)" block
paraphrases the withdrawn k-scan without those trigger words — so there is no
hit to place, inside or outside the block. The separated fields are present:
`Status: SPECIFIED`, `Phase-1 design adjudication:
DECOMP-UNAVAILABLE-AS-RECOVERED`, `Previous additive k-scan design: WITHDRAWN`,
and the current registered test = operator/determinant-identity audit.

### Gate statuses and quarantine (unchanged)

- `P2-BETAV-CIRC-01`: `Status: SPECIFIED` (no CIRC PASS/FAIL).
- `P2-BETAV-NUMREPRO-01`: `Status: PROPOSED (not run)`.
- `P2-C9`: `PROPOSED` — `β_V/β_B = −3.2(5)` still `unreproduced`, quarantined.
- Governance suite (`tests/test_si1_governance.py`): **12 passed**.

### Scripts and evidence

- `scripts/betav_decomp_check.py` default run prints **no** `no invariant split`
  string; the wrong-basis section runs only behind `--deprecated`, prefixed
  `DEPRECATED (wrong same-momentum basis; superseded by betav_decomp_q2.py): ...`
  (`max |<T| delta M |L>| = 0.1655`).
- `scripts/betav_decomp_q2.py` present (q²-level sector decomposition).
- The derivation and the q²-level report both carry the sector table unchanged
  (TT ≈96.5%, LL ≈3.1%, TL+LT ≈0.4%; scaling exponents ≈2; mixed TL+LT a finite
  leading-order `O(q²)` contribution).
- Attestation file present with `Pre-attestation HEAD:
  9bdc29b19bb6ab179d20065df9f16ea6b8e12475`.

### Tests and lint (merged `main`)

- `python -m pytest tests -q`: **34 passed, 2 deselected**.
- `ruff check .`: **All checks passed.**

## 3. What this merge does / does not do

**Does** (permanent record): the q²-level sector decomposition (mixed
TL+LT ≈0.4%, a finite leading-order contribution), the adjudication verdict
`DECOMP-UNAVAILABLE-AS-RECOVERED`, the withdrawal of the additive k-scan design,
and the re-registration of the CIRC test as an operator/determinant-identity
audit.

**Does not:** pass or fail `P2-BETAV-CIRC-01`; promote `P2-C9`; or touch the
`−3.2(5)` quarantine. The strategy decision (operator-identity audit vs
NUMREPRO focus vs clean-room RECON) is a separate, subsequent programme
decision — not part of this merge.

## 4. Repository state (pre-report)

`git status` on `main`: clean (the `results/**/decomp/` regen output is
gitignored and not tracked).

`git ls-remote --heads origin` (pre-report):

```
5395d4b3f5c1d81dc9954f484802d9f534009dc1  refs/heads/claude/paper-2-independent-verification-dysdp0
ca334fe0361d76fadb68e1866f71f0c40a4ed858  refs/heads/gate/p2-betav-circ
05a1e7f81eb814f0bb3e438e95e261aa07900031  refs/heads/gate/p2-betav-decomp
c1f1bec27085335b077dbdd26cb460f994acffd6  refs/heads/gate/p2-si1-unblock
4c70628fce287c97e5144cf3a65d37a866b72e63  refs/heads/main
836bf1441603565ba8d07207f31fabee8f04e5fc  refs/heads/recover/betav-complete
cdcbd840df8252d59ecfd29e662a797adc7216f9  refs/heads/recover/lattice-gravity-engine
b02c70279b382e05d415b23b9b5f562e3c5e2156  refs/heads/sea-ice/gate-stubs
```

`gate/p2-betav-decomp` remains at `05a1e7f` (not deleted, as required).
