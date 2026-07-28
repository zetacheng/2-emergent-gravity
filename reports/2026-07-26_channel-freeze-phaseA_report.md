# P2-CHANNEL-FREEZE-01 Phase-A freeze report

**Date:** 2026-07-26  
**Branch:** `gate/p2-channel-freeze`

## Part 0 and source-integrity continuation

The continuation began at the authorized branch tip
`8d2bc88b93aaf95a162cc036456702849ea16fa0`.  `origin/main` was verified at
`188989a68810dfbf5e369025cce27205a95ab410`, already an ancestor of this
branch through the preserved no-FF synchronization merge.  Executor-local EOL
settings were `core.autocrlf=false` and `core.eol=lf`.

All six source-integrity conditions passed.  The ratified governing source is
`derivations/CANONICAL_INTERACTION.md`, §2, SHA-256
`27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81`; the
ratification evidence is
`reports/2026-07-25_canonical-interaction_evidence.md`.  Its byte-identical
machine companion was landed at
`derivations/CANONICAL_INTERACTION.json`, SHA-256
`f94c35efe2d2ea434b0105a9c206cb67c1006cb96b95af71431012a3279c54f1`.
The companion parsed, named the required Markdown path, and carried the exact
reverse Markdown hash.

## Phase-A algebraic result

The canonical generator-sum interaction has one genuine microscopic
four-fermion coordinate, `G`; `N` remains symbolic.  The five-family
`S,P,V,A,T` Fierz matrix is exact rational, involutory, and has family rank
five.  It is a representation-family map, distinct from the symbolic full
candidate `K_ij` component count `16*N**2`.  The canonical source has support
on generator-sum scalar and pseudoscalar terms; all five families are retained
as candidate HS/K_ij fields, with no exclusions asserted.  Per-channel free
couplings remain rejected as a theory extension.

The frozen document is
`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`, SHA-256
`036a1a7b4959aab28b2ce6ddab56c261853be2a4a9a34223accab3bc0eafa1c2`.
It was not modified after its Task-1 commit.

## Machine verification

`scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py` parsed only the two frozen
JSON blocks for machine inputs.  It passed exact matrix comparison, artifact
sidecar verification, involution, source-companion hash links, canonical
expression equality, reconstruction equality, rank separation, and complete
nonduplicating indexed HS/K_ij registry checks.  The exact checker output was:

```text
P2-CHANNEL-FREEZE Phase-A exact verification: PASS
```

## Governance and correction

`P2-CHANNEL-FREEZE-01` remains `PROPOSED` with separate fields:
`Freeze state: PHASE-A FROZEN`, `Metric state: PHASE-B PENDING`, and
`SI-2 admissibility: BLOCKED UNTIL PHASE-B FREEZE`.  It records the immutable
document hash, pinned Paper-3 analytic path, current Arm-H/Arm-P dependency
record, and continuing quarantine.

The only test additions are the three pre-authorized entries in
`tests/test_channel_freeze_phase_a.py`: checker entry point, gate/hash check,
and analytic-vector-path check.  The existing
`test_channel_freeze_no_longer_requires_circ_pass` was not edited.  The
authorized continuation correction restored its required literal dependency
wording in the Phase-A gate entry and applied formatter-only changes to the two
new Python files; no pre-existing test was changed.

## Final verification

- `python -m pytest tests -q`: `53 passed, 2 deselected`.
- `python -m ruff check .`: `All checks passed!`.
- The Phase-A document hash matched the frozen gate value above.

## Commit chronology through pre-report HEAD

1. `8d2bc88b93aaf95a162cc036456702849ea16fa0` — preserved source-blocked
   cycle / synchronized continuation base.
2. `bd9f77d8d118d97192438cf687682f0f59bce22d` — machine companion landing.
3. `dbddb0e322adf912e3cc1959a04e9ab59078b7f3` — immutable Phase-A freeze
   document and matrix artifact.
4. `aab11990b696d63c0e3bce19682f2715056b9128` — exact verifier and
   pre-authorized test file.
5. `86e38e7b47518373cbc559bb815712ccba4fb031` — Phase-A gate bookkeeping.
6. `c683bc3eca4a8246ce2fdb40be72dd57366a9120` — authorized wording and
   formatting correction.

Phase B remains deferred.  No SI-2 computation, promotion, quarantine release,
merge to main, or pull request was performed.  This report omits its own commit
SHA and all post-push remote output.
