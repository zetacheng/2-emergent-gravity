# Phase-A verifier rebuild — typed-AST completion

Execution date: 2026-07-27.  This is an implementation-accuracy addendum only:
the freeze document, canonical artifacts, gate entry, SI-2, and quarantine are
unchanged.

## Implemented parser coverage

`vocab_parser.py` now uses a lexer plus recursive-descent parser for the frozen
expression grammar: equality, additive and multiplicative operators, power,
unary operators, grouped expressions, typed function calls, index tuples, and
the dedicated `Sum` production.  The checker consumes typed ASTs for every
frozen expression it uses: basis expressions, gamma5, trace and generator
normalization declarations, matrix entries, scalar coefficients, canonical and
decomposition interactions, and the companion singlet declaration.  Scalar
leaves alone lower to exact SymPy expressions; bilinears, gamma products and
bound sums remain typed.  No unrestricted `sympy.sympify` is used.

The parser does not claim a general natural-language grammar.  The companion
`lam(A)` vocabulary entry is the authoritative machine source for the exact
singlet equality `lam(0) = sqrt(2/N)*IdN`; that equality is extracted and then
parsed as a typed AST.  With typed internal-identity semantics
`trace(IdN)=N`, its parsed right-hand side derives
`trace(lam(0)**2)=(2/N)*N=2`.  The independently parsed generator
normalization declaration fixes the same value and its generator index domain
has cardinality `N**2`.

Canonical and decomposition interactions are compared as typed `GeneratorSum`
records: bound index/range, internal generator, Dirac bilinear, power and
outside schema coefficient.  Comparison permits bound-index alpha-renaming and
explicitly commutative additive ordering only; it does not move scalar factors
across `Sum`.

Gamma5 is now matrix-evaluated from the typed parsed `gamma5_definition` on
the constructed gamma matrices, then checked for equality with the independent
product, square, adjoint, anticommutation, and trace properties.

## Nine historical mutation cases — evidence-derived table

The test suite captures the actual `VerificationError` from the same mutation
registry used below and parses this table against those captured values.

| mutation name | expected frozen tag | actual raised tag | PASS/FAIL |
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

The metric case exercises the v4.5 unsupported-signature fallback: the typed
grammar admits the alternate signature, while the frozen primitive factory
supports only the frozen Euclidean signature.  It is not an adaptive-factory
test.

The tenth regression is separate from the historical nine-row table: changing
the frozen gamma5 definition to `-gamma(0)*gamma(1)*gamma(2)*gamma(3)` raises
`gamma5 parsed-definition mismatch` through AST evaluation rather than a raw
string comparison.

## Checks and chronology through pre-report HEAD

The final suite and Ruff check are recorded from this continuation before the
report commit.  The branch remains unmerged pending re-review.

1. `7e9cb1c` — JSON-driven algebra and pair-space verifier.
2. `510a884` — original nine-corruption mutation suite.
3. `f2a8280` — previous accuracy addendum.
4. This continuation's typed-AST and generator-normalization commits precede
   this report commit.
