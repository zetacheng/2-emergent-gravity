# Pre-execution review — integrate conventions C-a

**Review status:** APPROVED FOR EXECUTION AND LANDING  
**reviewed specification SHA-256:** `026d8ce8f81c62e75b7aec1878f2125f63a297e243d75bc27c2cfd4cd2708ecf`

## Scope of review

This review covers the updated specification supplied as `SPEC integrate conventions ca(1).md`, for integration and landing of `governance/conventions-consolidation-ca`.

## Determination

**APPROVED. No further specification amendment is required before execution.**

The previously identified A7 defect has been corrected. The specification no longer claims that a zero-deletion line diff permits an existing line to be rewritten and restored elsewhere. It correctly treats the in-order subsequence test as an **independent preservation measurement** alongside Git's line-diff accounting.

The correction does not alter A7's required preservation result, merge scope, acceptance thresholds, commit structure, or landing authorization.

## Review findings

The integration architecture is coherent: the arriving branch is merged with `--no-ff`; arriving content is not to be hand-edited; the report follows the merge; and authoritative `main` advances only by fast-forward after the specified post-report checks.

The treatment of the two PI rulings is acceptable. The non-binding `Consolidation record — C-a` may remain because it does not create a third binding governance form. The marker explanation is likewise acceptable because it describes enforcement status rather than creating or modifying an obligation.

The prospective-governance treatment is also sound. Governance introduced by C-a is not used retroactively to invalidate the review/integration process that necessarily precedes its landing.

The marker accounting appropriately measures the seven principles rather than relying on a whole-file token count. The expected disposition — one `MECHANISM EXISTS`, five `MECHANISM DEFERRED`, and one `RULE-ONLY` — preserves the distinction between consolidating the prose contract and closing enforcement debt.

The preservation controls are sufficient for this integration. In particular, A7 requires both Git line-diff preservation and a direct in-order subsequence comparison. These are separate measurements of preservation and should both be reported as specified.

Residual governance debt identified by C-a, including review/specification digest enforcement, auto-merge line-survival enforcement, and formal placement of marker-vocabulary semantics, is not an integration blocker and must not be represented as repaired merely by landing C-a.

## Execution disposition

Execution may proceed under the specification as reviewed. Landing remains conditional on satisfying every stop-governing acceptance criterion and the specification's fast-forward-only landing clause.

**Final verdict: APPROVED FOR EXECUTION AND LANDING.**
