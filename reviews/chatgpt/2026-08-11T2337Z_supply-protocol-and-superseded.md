Pre-execution review — review supply protocol and superseded-branch attribute

Reviewer: ChatGPT
Disposition: APPROVED

Specification: the review supply protocol, and a superseded-branch attribute
Specification evidence base: 0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5

Pinned inputs stated by the specification:

* CONVENTIONS.md — SHA-256 e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451
* docs/BRANCHING_POLICY.md — SHA-256 0ba1e2a006d287800d19b1bfadb5fe24f4bda72dedaf38ad3289ddfa700b9da9

Review scope

Reviewed the specification for internal consistency, Rule 15 lifecycle compliance, the proposed Rule 18 review-supply protocol, preservation of the existing branching-policy deletion-state machine, the proposed SUPERSEDED attribute and register, the evidentiary threshold for register membership, scope and commit ordering, and the Rule 16 accumulated-reading requirement.

This review does not independently verify repository objects, remote refs, SHA-256 values, branch ancestry, validator results or the completeness of the remote-branch enumeration. Those are executor-side acceptance checks under A1, A6, A10 and A11.

Rule 18

The proposed Rule 18 is sufficiently specified for execution.

The delimiter block, rather than semantic interpretation by the executor, determines the review artifact’s byte extent. Complete-line matching prevents occurrences of the delimiter strings elsewhere in the specification or accompanying instruction from being mistaken for boundaries.

The transport rule is also bounded mechanically: at most one leading blank line and at most one trailing blank line may be stripped. No other byte may be removed or normalised.

The revised wording correctly removes the earlier construction under which an executor would have had to identify and remove “instruction” text from inside the block. Under this version, text inside the delimiters belongs to the artifact. If instruction text appears there, the supply is defective and execution stops.

Placeholders in review content remain literal while placeholders in the artifact path are resolved. This is consistent with the prior governance lifecycle and removes another previously recurring source of executor judgement.

The specification therefore provides a valid first live test of the rule it is landing.

SUPERSEDED attribute

The proposed branching-policy change is structurally sound.

SUPERSEDED is correctly defined as an attribute orthogonal to the existing Stage-1 deletion states rather than as a fourth deletion outcome. This preserves the closed identity:

listed_count = pending + not_authorized + absent

and keeps two separate questions separate:

1. whether a branch may be deleted; and
2. whether a branch may be integrated.

A branch may therefore remain NOT_AUTHORIZED for deletion while also being SUPERSEDED for integration purposes.

The three supplied examples appropriately cover materially different histories, including a branch whose preserved value is evidence of a correct STOP rather than completed work.

Membership threshold

The revised evidentiary threshold for adding further branches to the register is approved.

A branch may be classified as SUPERSEDED only where a durable repository artifact already records the re-issue, replacement or supersession and identifies the replacement or reason.

Naming similarity, chronology, topology and the existence of a later branch are explicitly insufficient. Where such evidence is suggestive but non-dispositive, the required result is UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY, with the branch excluded pending authority.

This prevents an exhaustive branch search from becoming an executor-created governance classification.

Acceptance-criteria consistency

The operative criteria are internally consistent:

* A3 adds Rule 18 after Rule 17 without renumbering prior rules.
* A4 requires the pre-existing Rules 1–17 to survive byte-identically after removal of the new section.
* A5 preserves the existing deletion state machine and closed count identity.
* A6 consistently identifies all three supplied SUPERSEDED entries and separately governs discovery of additional members.
* A7 keeps DECISION_LOG.md append-only on both required measures.
* A9 resolves to three additions and three modifications.
* A10 leaves enforcement tests unchanged by design rather than implying they protect the new rules.
* A11 is branch-only and moves no main ref.

The report contract has also propagated the corrected count: it now refers to additions beyond the three supplied entries.

Pre-issue verification record

Section 8 now reflects the fixed evidence base rather than an obsolete drafting state.

It explicitly records executable SHA-256 checks for both pinned governing files at 0ab6369a…, alongside the branching-policy structural checks and the known branch observations.

That resolves the prior Amendment-H defect in which the record described checks that a future issuer was still expected to perform.

Rule 16 assessment

The proposed Rule 16 junction is appropriate.

Landing Rule 18 and a SUPERSEDED register establishes durable rules and classifications; it does not establish mechanical enforcement.

This task deliberately adds no test requiring future review supplies to comply with Rule 18 and no mechanism requiring every future integration specification to consult the SUPERSEDED register. The repository can therefore record the rules without mechanically preventing their violation.

That limitation is correctly identified and remains outside this task’s authorised scope.

Non-blocking observation

The historical introduction says the programme encountered “eight attempts and five distinct failure modes”, while items 1 and 2 in the displayed list explicitly describe two occurrences of the same failure mode.

This does not affect Rule 18, any acceptance criterion, scope, authority or execution behaviour. It is therefore non-blocking. If that historical prose is later edited for another authorised reason, “failure instances” or a deduplicated mode count would be more precise.

Stops and clarifications

SPECIFICATION_DEFECT: none blocking.

ENVIRONMENT: none identified by this review.

OBSERVATION_METHOD_ERROR: none blocking. Repository measurements stated in the specification remain to be independently reproduced by the executor.

REPOSITORY_DEFECT: the known absence of persistent mechanical enforcement for the governance rules remains open and is intentionally outside this task.

UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY: none inherent in the specification. A remote branch for which supersession is merely suggested rather than durably recorded must be reported under this category and excluded from the register.

What was verified and what was not

Verified by review: the specification’s internal logic; normative construction of Rule 18; separation of SUPERSEDED from deletion state; evidentiary threshold for register membership; propagation of the three-known-entry count; acceptance-criteria compatibility; scope arithmetic; and consistency of the pre-issue verification record with the now-fixed evidence base.

Not independently verified by this Reviewer: the actual Git object contents at 0ab6369a…; the two SHA-256 values; the three supplied branch heads and ancestry results; the complete remote-branch population; validator behaviour; or the final scope checker output. The specification correctly requires the executor to establish those independently.

Disposition

APPROVED.

No blocking specification defect remains. Execution may proceed subject to the specification’s own pinned-input, branch-state, review-supply, scope, validator and STOP conditions.
