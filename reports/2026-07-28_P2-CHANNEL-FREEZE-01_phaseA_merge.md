# P2-CHANNEL-FREEZE-01 Phase-A merge report

## Guard 0 — pre-merge observations

- Approved remote Phase-A tip: `47e271bbf1a73b6d3f2fc779c1ffcd024abaa80b`.
- Observed `origin/main`: `188989a68810dfbf5e369025cce27205a95ab410`.
- Observed checked-out Phase-A `HEAD`: `47e271bbf1a73b6d3f2fc779c1ffcd024abaa80b`.
- Phase-A freeze SHA-256: `fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a`.
- Canonical markdown SHA-256: `27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81`.
- Canonical JSON SHA-256: `f94c35efe2d2ea434b0105a9c206cb67c1006cb96b95af71431012a3279c54f1`.
- `python -m pytest tests -q`: `71 passed, 2 deselected`.
- `python -m ruff check .`: all checks passed.
- Working tree was clean. This Windows executor used PowerShell's SHA-256
  implementation because `sha256sum` was unavailable; the full digests above
  are the equivalent checks.

## Guard 1 — merge

The fast-forward pull left main at `188989a68810dfbf5e369025cce27205a95ab410`.
The post-pull ancestry check exited zero. The required no-ff merge commit is
`e045aa5c6c4353ee539fa902b41ca8dffd3f3686` with parents:

1. `188989a68810dfbf5e369025cce27205a95ab410` (pre-merge main)
2. `47e271bbf1a73b6d3f2fc779c1ffcd024abaa80b` (approved Phase-A tip)

## Guard 2 — post-merge verification

Both merge-parent checks matched the recorded values. All three frozen hashes
remained exact matches. `python -m pytest tests -q` again reported `71 passed,
2 deselected`; Ruff was clean; and the Phase-A checker reported PASS. The gate
entry remains intact.

The merged, already-committed Phase-A record freezes interaction-coordinate rank
1 with scan-eligible `G`; Fierz-family rank 5; K_ij component count `16*N**2`;
and zero exclusions. Its gate status remains `PROPOSED`, its freeze state is
`PHASE-A FROZEN`, its metric state is `PHASE-B PENDING`, and SI-2 admissibility
remains `BLOCKED`. No Phase-B work, promotion, or quarantine action occurred.

Dual Discriminator approval was recorded on 2026-07-26: Claude's clean-clone
re-review passed and ChatGPT's repository review approved, lifting the merge
block. The Phase-A branch remains present.

## Chronology through pre-report HEAD

1. `bd9f77d` — canonical machine companion landed.
2. `dbddb0e` — Phase-A freeze document landed.
3. `aab1199` — initial exact-rational verification.
4. `86e38e7` — PROPOSED gate fields and blocked Phase-B state recorded.
5. `37c8a9e` and `cf4bb9b` — document hash-chain corrections.
6. `c41199b` through `47e271b` — verifier, typed-AST, declaration-semantics,
   regression, and evidence-linkage commits.
7. `e045aa5` — no-ff merge of approved Phase A into main.

This report deliberately excludes its own commit SHA and all post-push output.
