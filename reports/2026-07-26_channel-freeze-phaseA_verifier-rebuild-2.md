# P2-CHANNEL-FREEZE-01 Phase-A verifier rebuild — accuracy addendum

Execution date: 2026-07-27.  This addendum replaces no scientific record and
does not alter the freeze document, canonical interaction artifacts, gate
state, SI-2, or the quarantine.

## Joint-review record and correction

The 2026-07-26 joint Discriminator finding remains: source landing and branch
discipline passed; governance was mostly passing; the Phase-A document required
one expression correction and two quotation corrections; and the earlier
machine verifier failed because it verified fixtures rather than computed
algebra.  The previously reported passing suite therefore established only that
its implemented assertions passed.  It did not establish the frozen algebraic
obligations.  This addendum corrects that overstatement.

## Findings mapped to the implementation

1. **B1 — parsed metric:** `gamma_algebra.gamma_factory` now receives the typed
   diagonal metric parsed from the JSON, and the verifier checks every Clifford
   anticommutator against that data.
2. **B2 — parsed basis and conventions:** each basis family is expanded from
   its JSON expression and component rule; gamma5, tensor equality, the Dirac
   trace declaration, the generator-normalization declaration, and the
   Grassmann sign are consumed as typed values.
3. **B3 — parser:** `vocab_parser.py` is a restricted typed parser for the
   frozen expression, component-rule, descriptor, metric, and normalization
   grammars.  The verifier does not use unrestricted `sympy.sympify`.
4. **B4 — completeness/orthogonality:** the constructed 16-component basis is
   checked by its exact 16-by-16 Hermitian trace Gram matrix, required to equal
   `4 I_16` and have rank 16.
5. **B5 — Fierz construction:** the five-family matrix is projected from the
   computed 16-component contracted-pair tensors using the constructed
   embedding and its Gram-adjoint left inverse.  The check requires
   `P_pair I_pair = I_5`, exact agreement with both frozen representations, and
   exact involution.
6. **B6 — coordinate rank:** the interaction-coordinate rank is the exact rank
   of the coefficient Jacobian derived from the decomposition records, not a
   syntactic count.
7. **B7 — registry domains:** symbolic component domains are parsed from the
   registry and family records; coverage, uniqueness, and the exact `16*N**2`
   total are checked without numerical substitution for `N`.
8. **B8 — Fierz duplicates:** non-zero Jacobian columns, full rank, exact
   involution, and pairwise projective Fierz-orbit disjointness are checked by
   exact two-by-two minors.  With one microscopic coordinate, pairwise
   disjointness is vacuous only after those non-vacuous checks pass.
9. **B9 — source-fidelity chain:** canonical and decomposition records are
   parsed from the frozen blocks and compared against the independently read
   companion expression; altered companion content is rejected.
10. **quotation and report accuracy:** the checker now extracts the canonical
    and SI-2 regions by their frozen heading boundaries and verifies byte
    equality against the existing marker-delimited quotations.  These checks
    live in `verify_quotations`, rather than being claimed as an earlier
    implicit property.

The actual marker lines are `<!-- BEGIN/END VERBATIM CANONICAL §2 -->` and
`<!-- BEGIN/END VERBATIM GATES SI-2 -->`.  The original boundary rule is used
without whitespace normalization.

## Computed verifier outputs

The exact computed family crossing matrix (the parsed basis-record order
`S, P, V, A, T`) is:

```text
[[1/4, 1/4, 1/4, 1/4, 1/4],
 [1/4, 1/4, -1/4, -1/4, 1/4],
 [1, -1, -1/2, 1/2, 0],
 [1, -1, 1/2, -1/2, 0],
 [3/2, 3/2, 0, 0, -1/2]]
```

Its square is the exact five-by-five identity.  The computed Gram verdict is
`G_AB = 4 delta_AB`, with rank 16.  The computed ranks are: interaction
coordinate rank 1 and Fierz-family rank 5.  The per-family symbolic K_ij
cardinalities are `S=N**2`, `P=N**2`, `V=4*N**2`, `A=4*N**2`, and `T=6*N**2`,
which sum exactly to `16*N**2`.

## Mutation evidence

Nine in-memory corruptions are required to raise the corresponding typed
obligation: tensor normalization; a matrix entry; a decomposition coefficient;
a duplicate registry label; a missing registry component; companion canonical
expression; metric signature; non-tensor basis expression; and a component
rule.  The tests exercise these without writing any frozen artifact.

The immutable Phase-A document remains SHA-256
`fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a`.

## Verification and chronology through pre-report HEAD

`python -m pytest tests -q` completed with `62 passed, 2 deselected`; `ruff
check .` reported all checks passed.

1. `cf4bb9b` — mechanical §A/§F re-quotation and regenerated hash chain.
2. `c41199b` — initial computed-verifier attempt.
3. `9576036` — initial six-mutation suite.
4. `a82bdee` — formatting follow-up.
5. `c03f7f9` — prior verifier-rebuild addendum.
6. `7e9cb1c` — JSON-driven typed algebra, pair-space map, ranks, domains, and
   quotation checks.
7. `510a884` — nine typed-obligation mutation tests.

The branch remains unmerged and requires re-review by both Discriminators.
