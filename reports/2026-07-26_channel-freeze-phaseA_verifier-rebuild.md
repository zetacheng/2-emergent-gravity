# Phase-A verifier rebuild addendum

Joint discriminator verdict (2026-07-26): source landing and branch discipline
PASS; governance mostly PASS; freeze document REVISE; prior machine verification
FAIL because it checked fixtures rather than computed algebra.  This rebuild
replaces fixture matrix/reconstruction logic with parsed-block Dirac basis,
trace-projection Fierz computation, record-derived reconstruction, symbolic
ranks/cardinality, marker-byte quotation checks, and six corruption mutations.

Computed Fierz family matrix:
`[[1/4,1/4,1/4,1/4,1/4],[1/4,1/4,-1/4,-1/4,1/4],[1,-1,-1/2,1/2,0],[1,-1,1/2,-1/2,0],[3/2,3/2,0,0,-1/2]]`.
Computed ranks/cardinality: interaction coordinate rank `1`, Fierz family rank
`5`, K_ij cardinality `16*N**2`.  All six mutations (tensor, matrix,
coefficient, duplicate, removal, companion corruption) failed the checker as
required.  Document SHA-256:
`fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a`.

Final checks: `59 passed, 2 deselected`; `ruff check .` passed.  Chronology
through pre-report HEAD: `cf4bb9b`, `c41199b`, `9576036`, `a82bdee`.
Merge remains blocked pending re-review.
