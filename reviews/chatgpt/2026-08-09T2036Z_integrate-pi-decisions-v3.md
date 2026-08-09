Pre-execution review — integrate the PI decisions v3 replay

Reviewer: ChatGPT
Disposition: APPROVED FOR EXECUTION

Review scope

I reviewed the specification titled “Task specification — integrate the PI decisions v3 replay” against its own stated evidence base, acceptance criteria, commit ordering, evidence layering, invariants, and reporting contract.

This review addresses whether the specification is internally coherent and executable as written. It does not independently execute the merge, verify repository object IDs, run validators, reproduce Git diffs, or certify facts that require access to the execution repository.

What I verified

I verified that the specification now gives a coherent Rule-15 execution lifecycle:

1. the integration specification is committed first;
2. this pre-execution review is committed second;
3. the merge occurs only after the review commit;
4. the integration report is committed after the merge.

Accordingly, A2 correctly identifies the pre-execution review commit, commit 2, as merge parent 1. The additional requirement that commit 1 be an ancestor of parent 1 preserves the full authority chain. This resolves the earlier structural-propagation defect in which parent 1 was incorrectly identified as the specification commit after Rule 15 inserted a review commit between specification and merge.

I verified that A4’s final scope is internally consistent:

* four additions arrive from fix/pi-decisions-v3;
* three additions are authored by the integration task;
* DECISION_LOG.md is the sole modification;
* final scope is therefore seven additions and one modification.

I verified that A8 no longer conflicts with that authorised scope. It explicitly limits blob-identity protection to paths that existed at the evidence base and excludes the three base-absent authorised paths relevant to that comparison: the two new review paths and derivations/P2-DEFERRED-ITEMS.md.

I verified that the specification cleanly separates substantive ruling comparison from entry metadata. The ruling comparison concerns the blockquoted ruling text under ### Decision; ### Related branch and files is entry-level metadata outside that blockquote. A9a therefore checks the metadata separately and expressly prohibits inventing a branch-name canonicalisation rule. This is the correct treatment: comparison scope is defined before execution rather than expanded after a difference is observed.

I verified that A6 requires four distinct append-only properties rather than treating one proxy as sufficient:

* zero deleted lines from evidence base to merged head;
* zero deleted lines from merge commit against parent 1;
* zero deleted lines from merge commit against parent 2;
* the evidence-base DECISION_LOG.md must be an exact byte prefix of the merged version.

These checks establish different properties. In particular, the parent-2 comparison tests that the merge did not discard source-branch entries, while the byte-prefix check is stronger evidence that the authoritative log was genuinely extended rather than reconstructed into an equivalent final state.

I verified that the specification preserves the substantive limits of the three PI decisions. It does not turn any of them into a physics result, does not close OPEN-AC-1, does not select η, does not classify the negative-mass branch, and does not treat DEFERRED-03 as evidence-backed.

I also verified that the Rule-16 accumulated-reading requirement is meaningfully instantiated rather than satisfied with boilerplate. The identified V/A junction is material: combining the scalar-channel choice with the V/A REPULSIVE / no-real-HS result could invite the inference that V/A physics was rejected. The specification explicitly blocks that inference and correctly states that the deferral concerns the presently available mean-field machinery, not a physical exclusion of the V/A representation.

Finally, I verified that the branch-preservation requirements and report contract are mutually consistent. The report must distinguish the three PI-decision branches from the separately protected review/role-model-and-executors branch, and no branch deletion, history rewrite, or force-push is authorised.

What I could not verify in this review

I did not independently verify the following repository-dependent claims:

* that remote main resolves to 7c5cba5df76de6ef8f52af390ca92100dcdf0d8b;
* that fix/pi-decisions-v3 resolves to 93de3218095cafdabcd0fda92abc31af33109879;
* that the dry-run merge is conflict-free;
* that the stated merge-base is correct;
* that the Git blob IDs in A6 and A7 match the repository objects;
* that the evidence-base DECISION_LOG.md is in fact an exact byte prefix of the source-branch version;
* that the structural assertions in §9 reproduce against the repository;
* that protected paths are blob-identical;
* that the gate states and anchor count are unchanged;
* that the four required test files pass;
* that the merge guards and scope checker accept the resulting history;
* that the preserved branches remain at their stated remote commits after the push.

Those are execution-time acceptance checks and must be established by the Executor using the methods specified in the task.

Reviewer findings

I found no remaining internal contradiction requiring a stop before execution.

The earlier A2 defect is resolved: Rule 15 changes the commit graph, and the specification now propagates that change into merge parentage rather than leaving the old parent description in place.

The earlier A8 ambiguity is also resolved by explicitly distinguishing pre-existing protected paths from authorised base-absent additions.

The earlier ruling-comparison ambiguity is resolved without adding an execution-time normalisation rule. Metadata is checked as metadata; substantive ruling text is checked as substantive ruling text.

One minor presentation point remains non-blocking: Decision 2 is written as eta in the summary while the rest of the programme normally uses η. This does not change meaning or any acceptance criterion.

Disposition

APPROVED FOR EXECUTION.

The specification is sufficiently explicit about merge parentage, Rule-15 review timing, authorised scope, append-only evidence, substantive-versus-metadata comparison boundaries, protected paths, accumulated-reading limits, and prohibited conclusions.

Execution should proceed only if the repository-dependent checks reproduce as specified. Any mismatch in refs, object identities, merge conflict status, guards, protected paths, validators, scope, or branch preservation remains a STOP under the task’s own criteria.
