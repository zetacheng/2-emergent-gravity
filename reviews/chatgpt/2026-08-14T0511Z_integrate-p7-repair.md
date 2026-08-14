# Pre-execution review — integrate the P7 repair and pin validator

reviewed specification SHA-256: `8932e99a88f43957ac78f2a14b9d35fe1f1dec1a0f394676720e82418a5a9f03`

## Disposition

**APPROVED**

I reviewed the supplied specification **“Task specification — integrate the P7 repair and the pin validator, and land it”** as a whole against its stated evidence base and execution contract.

The earlier ambiguity in A6 has been corrected. The specification now distinguishes the **nine paths changed base-to-merge-commit** from the **seven paths contributed by source branch `7102a60ef249da04e2ad3326a3b8135b688aa065`**. A6 correctly requires blob-identity comparison only for those seven source-contributed paths; the integration task’s own specification and review are separate additions and are not part of that source-integrity comparison.

The merge arithmetic and evidence layering are internally consistent: the merge commit is specified as **6 additions and 3 modifications**, the source contributes **4 additions and 3 modifications**, and the later report adds the final integration-task addition. These quantities are no longer conflated.

The P7 acceptance criteria are materially stronger than the previously vacuous check. The specification requires the repaired grammar to report the real gate population and requires the raw-heading and parsed-section counts to agree, so a `PASS` must carry non-zero, complete coverage rather than a `0/0` comparison. The same execution also preserves a before/after measurement of the old grammar so the claimed repair remains falsifiable.

The pin validator acceptance criteria likewise establish detection power rather than mere test presence. The specification requires the validator to be collected by the suite, requires the post-repair suite count to exceed the historical 280-test baseline with the delta explained, and retains the stale-pin counterfactual demonstrating that the pre-repair suite passed a state the repaired suite rejects.

The specification appropriately limits the conclusions drawn from the P1/P7 dry-merges. Clean merges in both orders establish **textual merge cleanliness only**. They do not establish semantic order-independence, do not discharge P1’s outstanding A10, and do not remove the requirement for the later P1 integration task to measure the three shared files and their combined behaviour.

The Rule 16 limitations are also adequate. In particular, the repository still contains more than one gate-heading grammar, current agreement does not itself guarantee future consistency, and the pin correspondence remains a check implemented by a validator rather than a proof that future specifications will always remember to maintain pins correctly.

I found no remaining stop-level inconsistency, unsatisfied prerequisite, scope contradiction, or evidence-layering defect that should prevent execution.

## Non-blocking observation

The phrase in §0, “Two checks that work, and one that did not,” is slightly easy to misread in isolation because the surrounding table lists three landed capabilities while the “did not” refers to the former P7 behaviour. The surrounding text makes the intended meaning clear, so this is not execution-changing and does not require amendment.

## Execution boundary

This approval authorises execution of the supplied specification only. It does not approve integration of `governance/p1-declared-total`, does not discharge that branch’s A10, and does not broaden the frozen manifest or the stated landing conditions.
