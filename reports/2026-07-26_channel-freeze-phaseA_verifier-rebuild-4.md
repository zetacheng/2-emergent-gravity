# Phase-A verifier rebuild — declaration-semantics completion

Execution date: 2026-07-27. Base head: `65b80aaa0eb1447f374c0f2d3a1630d3a96f35a8`.
This addendum changes verifier architecture and tests only. It does not change
the Phase-A freeze document, canonical artifacts, gate entry, SI-2, or quarantine.

## Implemented declaration semantics

The companion `lam(A)` vocabulary value is scanned only through the restricted
frozen-language lexer/parser. Complete parsed equality candidates whose left
side is typed `lam(0)` are collected; exactly one is required. Candidate spans
must end at a lexical boundary, so partial expressions are not accepted. The
extractor ignores surrounding prose, rejects missing declarations, and rejects
duplicate or contradictory declarations without a hardcoded declaration string
or splitting on `=`.

The extracted AST is required to have `lam(0)` on the left and
`sqrt(2/N)*IdN` on the right. A narrow internal evaluator squares that parsed
scalar-times-identity AST, applies the declared principal-sqrt semantics, uses
the typed `IdN` rule `trace(IdN)=N`, and derives `trace(lam(0)**2)=2`. It does
not lower unsupported internal operators to generic SymPy.

The parsed normalization equality supplies its coefficient, both `lam` indices,
and the `KroneckerDelta` arguments. The generator range comes from the parsed
canonical `Sum` index tuple. Generator-sum comparison extracts the bound index,
bounds, internal generator, Dirac operator, bilinear power, and outside schema
coefficient individually. Bound indices are normalized, so a consistent `A` to
`B` renaming compares equal; a partial renaming fails.

The Fierz matrix atom parser remains separate because matrix atoms are outside
the Task 1–2 typed declaration/expression paths. Gamma5 verification now also requires exact
`trace(gamma5)=0`.

## Mutation and focused-regression evidence

| case | expected tag / outcome | actual | result |
|---|---|---|---|
| tensor | tensor normalization mismatch | tensor normalization mismatch | PASS |
| matrix | computed Fierz matrix mismatch | computed Fierz matrix mismatch | PASS |
| coefficient | reconstruction mismatch | reconstruction mismatch | PASS |
| duplicate | duplicate field_label | duplicate field_label | PASS |
| removed | component-domain coverage omission | component-domain coverage omission | PASS |
| companion | companion mismatch | companion mismatch | PASS |
| metric | unsupported metric signature | unsupported metric signature | PASS |
| basis | gram matrix normalization mismatch | gram matrix normalization mismatch | PASS |
| rule | component-domain completeness mismatch | component-domain completeness mismatch | PASS |
| gamma5 parsed definition | gamma5 parsed-definition mismatch | gamma5 parsed-definition mismatch | PASS |

Focused regressions: surrounding companion prose with one unchanged declaration
passes; duplicate parsed declarations and an absent declaration raise `singlet
declaration mismatch`; `sqrt(1/N)*IdN` raises `singlet normalization mismatch`;
a complete `A` to `B` binder rename passes; binder-only and occurrence-only
renames raise `generator sum mismatch`.

The metric mutation remains the frozen unsupported-signature fallback path: the
grammar admits the alternate signature, but the primitive factory supports only
the frozen Euclidean representation.

## Verification and chronology through pre-report HEAD

`python -m pytest tests -q` and `python -m ruff check .` pass after this report
is written and before its commit.

1. `65b80aa` — v5.1 typed-AST accuracy addendum base.
2. This continuation's declaration-semantics verifier commit.
3. This continuation's focused-regression test commit.

The report commit's own SHA is deliberately excluded. The branch remains
unmerged pending re-review.
