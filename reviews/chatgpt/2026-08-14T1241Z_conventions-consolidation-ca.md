# Pre-execution review --- `C-a`: conventions consolidation

**Disposition: APPROVED**

reviewed specification SHA-256:
`2311e04d50861e14bcc24170be429b38dfa418c35ac698d0196a8587a684b591`

Reviewed specification: `SPEC conventions consolidation ca(2).md`

## Review conclusion

I approve this specification for execution under Rule 18.

The specification now resolves the substantive defects identified in the
prior review. In particular, the mechanism-marker semantics are
correctly attached to **the obligation imposed by the rule**, rather
than to the mere existence of related machinery. This makes the A1
assignment coherent: `P1` already parses `stated:`, while the obligation
requiring newly issued specifications to supply that declaration remains
`MECHANISM DEFERRED`.

The Rule 16 treatment is also corrected. It no longer claims that none
of the underlying violations were mechanically detected. It expressly
records the B4 counterexample and distinguishes machine detection of an
underlying violation from human identification, interpretation, or
repair of the governance gap.

The source-item accounting is internally consistent. The task covers
twelve observed failures (`A1`--`A8`, `B1`--`B4`) plus the separately
ruled `E2` namespace item, giving thirteen traceability rows. The
candidate consolidation is not improperly frozen as mandatory
architecture: alternative consolidation is permitted if justified and if
the thirteen-row traceability requirement remains complete.

## Governance and execution review

The specification appropriately limits `C-a` to prose governance. It
prohibits checker, parser, test, gate, script, result, and derivation
changes; separates `C-b` and `C-c`; and does not represent deferred
mechanisms as implemented.

The placement rules are sufficiently constrained. Existing rules and
amendments may not be renumbered or reworded; amendments must modify an
identified existing rule; standalone principles must use new numbered
rules; Amendment `J` is expressly excluded; and an executor who
concludes that a third structural form is required must stop rather than
invent it.

The B4 issue is correctly left for a durable prospective choice within
this task. The specification requires the executor to decide whether a
permitted pre-push hygiene repair requires all affected checks or only
the failing check to be rerun, while expressly preventing the earlier
voluntary rerun from being misrepresented as an already-settled
precedent.

The evidence layering and frozen scope are coherent: specification,
review, `CONVENTIONS.md`, then report. The committed report is
restricted to measurements available at commit 3, with commit-4
verification kept as post-report evidence. `CONVENTIONS.md` is the sole
substantive modified path.

## Acceptance-criterion review

The acceptance criteria are sufficiently testable and mutually
compatible. Of particular importance are the thirteen-row traceability
matrix; exactly one mechanism marker per written rule or amendment;
independent verification of the four known mechanism assignments; full
additive-only diff inspection; explicit placement justification;
unchanged protected paths; gate and pin invariants; non-vacuous P7
section counting; stop-governing RUN 2; and unchanged validator count
unless an explained finding arises.

I identify no instruction that presently requires the executor to choose
between inconsistent repository/governance obligations. The explicit
contradiction-stop clause remains appropriate if execution evidence
reveals such a conflict.

## Non-blocking observation

The specification deliberately does not prescribe the final number of
consolidated principles. That is appropriate. The candidate
seven-principle grouping is a reviewable starting structure, while the
traceability matrix, placement justification, and mechanism-marker
requirements provide the stronger invariant. The executor should
therefore optimize for non-overlapping durable principles rather than
mechanically reproducing seven headings.

## Final disposition

**APPROVED --- no blocking specification defect identified.**

This approval is bound to the exact specification digest recorded above.
Any modification to the specification requires the review binding to be
reconsidered before execution.
