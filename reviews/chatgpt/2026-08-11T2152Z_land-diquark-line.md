Pre-execution review — land the diquark line

Reviewer: ChatGPT

Disposition: APPROVED FOR EXECUTION

Review scope

I reviewed the task specification “land the diquark line: adjudication, both-η result, and a sensitivity addendum” for internal consistency, execution ordering, evidence layering, merge authority, scope definition, preservation requirements, and whether the conclusions authorised by the task exceed the evidence described in the specification.

This review is limited to the specification as supplied. I did not independently inspect the repository objects, execute either source branch, reproduce the dry-run merges, recompute the fourteen Git blob ids, or rerun the scientific calculations. Those are executor acceptance checks under A1–A13.

What I verified from the specification

The task identity and execution structure are coherent.

The evidence base is fixed at 57c5a6eb1de11bb7aaf27b779054070ee6870c29. The two source branches are individually pinned. Their required merge order is explicit: adjudication first, both-η second.

The six-commit lifecycle is internally consistent:

1. specification;
2. pre-execution review;
3. adjudication merge;
4. both-η merge;
5. sensitivity addendum;
6. report.

Rule 15 timing is respected because this review precedes both merges. The sensitivity addendum correctly follows both merges because it depends on the relation between the two arriving bodies of evidence.

The merge-parent requirements are structurally consistent with that order. Merge 1 has the review commit as parent 1. Merge 2 has merge 1 as parent 1. Both source branches are required to retain the original evidence base as merge-base. Commit 1 is separately required to be an ancestor of both merges.

The two-merge structure does not silently collapse two integrations into one evidentiary event. A3 requires a separate PRE_MERGE guard before each merge, A2 requires separate parentage evidence for each merge, and A6/A7 require independent blob verification for each branch.

The frozen scope is arithmetically consistent: fourteen additions arrive from the two source branches and four paths are authored by this task, giving 18 additions and 0 modifications. The manifest contains eighteen paths.

The specification correctly distinguishes three different epistemic claims:

* the adjudication establishes why the independent comparison disagreed with the reviewed branch;
* the both-η task establishes the relative η sensitivity;
* the new addendum records which frozen conventions are load-bearing for the observed family support.

The addendum is explicitly a sensitivity record rather than a correction. That distinction is important and is adequately protected by A10 and §2.

The specification also correctly limits the adjudication result. An identical L3 excludes the particular observed discrepancy from being evidence of a pp-ordering divergence. It does not establish independence over every admissible particle–particle ordering. The addendum is required to preserve that limitation.

The treatment of OPPOSITE is appropriately bounded. The specification states that it is a relative statement between the two η representatives, not an assignment of an absolute attractive or repulsive channel character.

The relation to the integrated chirality census is also correctly scoped. The census is cited as explaining family support, not coefficient sign or magnitude.

No prohibited scientific conclusion is required by the task. No convention is frozen, no gate status changes, no bound-state claim is licensed, and no unresolved pp-ordering question is declared closed.

Findings

1. Two merges in one task are acceptable here, but the evidentiary burden is materially higher

I do not regard the two-merge structure as a defect because the specification keeps both merges individually observable and the second result is not sensibly separable from the adjudication that lifted its hold.

The executor should nevertheless report whether batching caused any ambiguity in guard state, parentage, scope attribution, or post-merge verification, as §9 already requires.

If either merge cannot be individually reconstructed from the report, the batching should be treated as having failed its purpose even if the final tree is correct.

2. The OPPOSITE wording is the highest-risk semantic boundary

The specification handles this correctly, but the report must preserve the distinction exactly:

OPPOSITE means that changing η reverses the non-zero coefficient signs for fixed remaining conventions.

It does not establish which representative is absolutely attractive or repulsive.

It also does not settle the wider phase freedom or untested pp-ordering alternatives.

Any report wording that compresses this to “the diquark channel is opposite” or “the channel character is determined” would overstate the result.

3. The addendum must distinguish frozen sensitivity from unresolved convention dependence

The adjudication shows that the iγ₅ canonical pseudoscalar and the explicit i factors in the A/T basis are load-bearing. These are already frozen conventions.

Therefore the addendum should not describe them as newly discovered ambiguities or as weakening the result’s status under the frozen framework.

The correct statement is that the result is sensitive to frozen choices whose provenance and physical role should remain visible.

By contrast, η, pp Grassmann ordering, and diquark normalisation remain unfrozen.

The specification already requires this distinction; the executor should preserve it without compressing the two categories into a generic “convention dependence”.

4. The adjudication’s negative result about ordering must remain negative

L3 being identical establishes that the observed discrepancy was not caused by a difference in the tested slot map / Grassmann permutation.

It does not establish that all admissible alternative pp orderings give the same support.

The proposed addendum states this correctly. I consider that limitation load-bearing.

Rule 16 / accumulated-reading assessment

The candidate junction in §7 is appropriate.

After integration, a reader will see on main:

* the particle-hole coefficient structure;
* the chirality selection explanation;
* the particle-particle both-η computation;
* the adjudication resolving the apparent decomposition discrepancy;
* the sensitivity addendum.

That assembled set naturally invites a stronger conclusion than the evidence licenses: that the interaction’s complete channel structure is now settled.

It is not.

At minimum, the assembled evidence does not establish:

* an absolute particle-particle attractive/repulsive character;
* independence over every admissible pp Grassmann ordering;
* a fixed diquark normalisation;
* the unexplained inter-channel relative sign;
* any bound-state or pole statement.

The integration report should state this explicitly.

What I could not verify in this review

I did not independently verify:

* that remote main still resolves to the stated evidence base;
* that either source branch still resolves to its pinned SHA;
* that both sequential dry-run merges are conflict-free;
* either merge-base;
* the fourteen arriving blob ids;
* the 18-path final scope;
* that no pre-existing repository path changes;
* validator outcomes;
* commit-message trailer suppression;
* preservation of source branches;
* the exact numerical or algebraic contents of either source branch;
* the scientific correctness of the adjudication or both-η computations beyond the internal logic presented in this specification.

Those remain mandatory executor checks and are not converted into PASS by this review.

Disposition

APPROVED FOR EXECUTION.

No blocking contradiction is apparent in the supplied specification.

Execution should STOP if either merge conflicts, any pinned ref or blob fails verification, the two merges cannot be independently represented by the guard tooling, or the resulting report would require strengthening OPPOSITE, the pp-ordering conclusion, or the sensitivity statement beyond the limits specified here.
