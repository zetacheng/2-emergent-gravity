# Canonical report — Paper 2 βV provenance adjudication merge

**Date:** 2026-07-20. **Repository:** `zetacheng/2-emergent-gravity`.
**Task type:** controlled merge of already-reviewed work (no new scientific
content).

## 1. Executive summary

This report lands the completed `P2-BETAV-CIRC-01` provenance adjudication into
`main`. The circularity question of Paper 2's Finding 5 (`β_V/β_B = −3.2(5)`)
could **not** be tested, because the historical lattice Proca pipeline that
produced that value is **not present** in the repository (provenance verdict:
NOT LOCATED). The reviewed branch therefore records the honest disposition:
the circularity gate is `SUSPENDED`; a determinant-bookkeeping *implementation
regression* (`P2-BETAV-ASSEMBLY-01`) is `PASS` on its own terms but explicitly
does not test the historical projection; and a clean-room reconstruction path
(`P2-BETAV-RECON-01`) is `PROPOSED` but not run. Nothing is promoted to
`VERIFIED`. This merge is governance/ledger-landing only.

## 2. Source branch and reviewed source SHA

- Source branch: `gate/p2-betav-circ`
- Reviewed scientific HEAD: `e6c9f5b9d8f7917966ec534095afb55a78ce5b19` (`e6c9f5b`)
- Report-only successor HEAD: recorded in §16 after the report commit.

## 3. Target branch and pre-merge target SHA

- Target branch: `main`
- Pre-merge target SHA: `e21f81ea7f750c71fcfe2734ab86423cadf91b17` (`e21f81e`)

## 4. Scientific outcomes being landed

| Gate | Status |
|---|---|
| `P2-BETAV-CIRC-01` | **SUSPENDED** (blocked by provenance) |
| `P2-BETAV-ASSEMBLY-01` | **PASS** (implementation regression only) |
| `P2-BETAV-RECON-01` | **PROPOSED** (not run) |

These statuses are landed unchanged from the reviewed branch; this merge does
not alter any gate outcome.

## 5. Provenance conclusion

**The historical Finding 5 lattice pipeline was NOT LOCATED.** A repository-wide
search (`results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md`) found no lattice
1-form/vector operator, no Stueckelberg compensating determinant, no
metric-perturbation / `h`-derivative / graviton-projection code, and no raw
artifact or table from which `−3.2(5)` was produced. `MIGRATION.md` states there
is no legacy source; there is no `PROVENANCE.md`; and the paper references the
companion `3-vector-sector` only for the Fierz/Proca *construction*, not for the
graviton `β_V` extraction. The only `numpy.linalg` call in `scripts/` is `lstsq`
in the **scalar** `P2-BETA-01` tadpole, which implements none of the required
machinery and was **not** substituted.

## 6. Status of `β_V/β_B = −3.2(5)`

`β_V/β_B = −3.2(5)` (paper eq. `betaVlat`) **remains an unreproduced paper
value.** It is not reproduced anywhere in this repository and has no archived
provenance.

## 7. The assembly gate does not test the historical projection

`P2-BETAV-ASSEMBLY-01` builds the `k`-generalized Proca determinant assembly on
the *one shared* scalar lattice tadpole. Because numerator and denominator are
the same integral `C` times different rational prefactors, `C` **cancels
exactly** in the ratio `R_k = β_V(k)/β_B = −(k+2)`. Consequently the ratio is
grid-independent (variant spread `≤ 9e-16`) and the construction has **no
power** to expose a circular historical projection or normalization. It verifies
only that the assembly code reads `k` and does not hardcode `−3`. It does
**not** test — and does **not** close — `P2-BETAV-CIRC-01`.

## 8. Mutation demonstration summary

The committed mutation anchor freezes the scalar determinant power to `1` (the
Proca value — the analogue of a projection that pins the compensating sector).
Under the mutation, every `R_k` collapses to `−3` for all `k ∈ {0,1,2,3,½}`,
so the `k`-scan anchor fails. This proves only that the code reads `k`; per the
gate's explicit caveat, it does **not** show any real pipeline is non-circular.
Un-mutated `k`-scan (from `results/P2-BETAV-ASSEMBLY-01/raw/betav_assembly.json`):
`k=0→−2, 1→−3, 2→−4, 3→−5, ½→−5/2`, ratio variant spread `≤ 9e-16`.

## 9. Clean-clone test result and test count

Fresh clone of `gate/p2-betav-circ` at `e6c9f5b`, `python -m pytest tests -q`:
**22 passed, 2 deselected** (the 2 deselected are `@pytest.mark.slow`; the full
suite `-m "slow or not slow"` is 24 passed). Working tree clean.

## 10. Files introduced or modified by the reviewed branch (vs `e21f81e`)

Added:
- `derivations/P2-BETAV-ASSEMBLY-01_bookkeeping_regression.md`
- `derivations/P2-BETAV-RECON-01_cleanroom_reconstruction.md`
- `results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md`
- `results/P2-BETAV-ASSEMBLY-01/` (`README.md`, `raw/betav_assembly.json`,
  `environment.txt`, `branch.txt`, `commit_parent.txt`)
- `scripts/betav_assembly.py`

Modified (ledger/tests only):
- `CLAIMS.md`, `DECISION_LOG.md`, `GATES.md`, `HANDOFF.md`, `PROGRESS.md`,
  `tests/test_gate_anchors.py`, `tests/test_repository_structure.py`

No `results/*/raw/` file was modified or deleted (additions only).

## 11. Pre-merge git status

Working tree clean on both the reviewed branch and the fresh clone
(`git status --porcelain` empty) prior to creating this report.

## 12. Limitations

- The circularity question is not answered — it is *blocked by provenance*.
  Neither circularity nor non-circularity of the historical Finding 5 pipeline
  is demonstrated.
- `P2-BETAV-RECON-01` is a proposed *new* pipeline; if built and faithful it
  would inform, but not close, `P2-BETAV-CIRC-01`.

## 13. No PR opened

No pull request was opened for this merge (git `--no-ff` merge only).

## 14. No new scientific content added during this merge task

This task added only this canonical report (documentation). No scientific
script, test logic, numerical value, gate outcome, or claim status was created
or altered during the merge.

## 15. SI-2 authorization statement

**This merge does NOT authorize SI-2 numerical use of the historical Finding 5
lattice value `−3.2(5)`.** That value remains unreproduced and without
provenance; it must not be cited as validated numerical evidence.

## 16. Merge execution record

- Reviewed scientific HEAD (source): `e6c9f5b9d8f7917966ec534095afb55a78ce5b19`
- Report-only successor HEAD (source branch): `ca334fe0361d76fadb68e1866f71f0c40a4ed858`
- Merge command used: `git checkout main && git pull --ff-only origin main &&
  git merge --no-ff gate/p2-betav-circ -m "merge: land the Paper 2 betaV
  provenance adjudication"` (no squash)
- Merge commit SHA: `30062c4cace7918173d7f44a558fb84a37392b57`
- Post-merge `main` SHA (at merge): `30062c4cace7918173d7f44a558fb84a37392b57`
  (this report's own finalize commit is a report-only successor on top of it;
  its SHA is the resulting `main` HEAD, reported in the terminal summary).
- Post-merge test count: **22 passed, 2 deselected** (`python -m pytest tests
  -q`; the 2 deselected are `@pytest.mark.slow`).
- Final `git status`: clean (`git status --porcelain` empty).
- Remote branch state after push:
  `main` = the finalize-commit HEAD; `gate/p2-betav-circ` = `ca334fe`
  (**intact, not deleted**); `claude/paper-2-independent-verification-dysdp0`
  and `sea-ice/gate-stubs` unchanged.
- Source branch intact: yes — `gate/p2-betav-circ` is preserved at `ca334fe`.
- No PR opened.

### Post-merge gate statuses on `main` (verified)

- `P2-BETAV-CIRC-01` = `SUSPENDED`
- `P2-BETAV-ASSEMBLY-01` = `PASS`
- `P2-BETAV-RECON-01` = `PROPOSED`
- `β_V/β_B = −3.2(5)` labelled an unreproduced paper value; not presented as
  validated numerical evidence.
