Pre-execution review — land the diquark line v2

Reviewer: ChatGPT
Disposition: APPROVE FOR EXECUTION

Review scope

I reviewed the re-issued specification for landing:

* gate/p2-diquark-adjudication @ 3767973bf57c52f4dd2be1fddcf62916ec409c72
* gate/p2-diquark-both-eta @ bc1e5c743aada004c52dc7ab7ce2af61de439955

against the stated evidence base:

* 57c5a6eb1de11bb7aaf27b779054070ee6870c29

This review covers the internal consistency of the execution specification, the repair of the first issue’s merge-base defect, the two-merge sequencing, the Amendment-K re-issue construction, the evidence layering, the scope contract, and the epistemic limits placed on the sensitivity addendum.

This review does not independently execute repository commands, inspect Git objects, recompute blob identities, or run the guards, validators, dry-run merges, ancestry checks or scope checker. Those remain execution-time obligations under A1–A13.

Findings

1. The first issue’s blocking defect is correctly repaired

The prior issue required both integration merges to have merge-base 57c5a6eb…, even though both source branches were cut from 8701a97a… before main advanced.

This re-issue now distinguishes the relevant quantities correctly:

* merge-base(branch 1, branch 2) = 8701a97a…
* merge-base(evidence base, branch 1) = 8701a97a…
* merge-base(evidence base, branch 2) = 8701a97a…

A2 no longer requires an impossible parentage relation.

The additional A2a ancestry observation is useful because it records the underlying stale-branch fact separately rather than treating it as a merge failure. A source branch need not descend from the current evidence base for a legitimate three-way merge to exist.

2. The re-issue satisfies the construction Amendment K required

The failed first execution is preserved at:

gate/p2-land-diquark-line @ d64cd912ca9ff78a85787f0e54f345f474cdb192

and is explicitly superseded for integration rather than rewritten.

The new execution uses:

* a new branch, gate/p2-land-diquark-line-v2;
* new task-identity paths;
* a new {HHMM} token that must not reuse 2152;
* the same authoritative evidence base;
* the same pinned source branches.

This is a clear re-issue rather than an attempted continuation of the stopped execution.

3. The aborted-execution path is now specified

The first issue exposed a real gap: its frozen successful-path commit order did not say where a report belongs when execution stops before the planned merge commits.

The new clause resolves that explicitly:

If the task stops before the merges, the frozen order does not apply beyond the point reached. Commit the report as the next commit in sequence and say which number it is and why.

That removes the executor judgement required in the first issue and is consistent with the requirement that the task still leave a durable report of a governed stop.

4. The two merges are now independently observable

A2 explicitly requires the parentage and merge-base for each merge to be derived separately from the objects.

That is an important correction. The first issue used one shared rationale for two entries and propagated one false assumption into both. The revised wording prevents a repeated value from being treated as evidence merely because the two branches are siblings.

Two PRE_MERGE guards remain required, one immediately before each merge. That is the correct placement: the first issue demonstrated that this can stop an invalid integration before any merged tree is created.

5. The scientific and epistemic scope is appropriately limited

The addendum is correctly framed as a sensitivity record, not a correction to the both-η derivation.

The specification distinguishes:

* frozen, load-bearing conventions:
    * canonical iγ₅;
    * the explicit i factors in the A/T basis;
* still-unfrozen conventions:
    * η;
    * particle–particle Grassmann ordering;
    * diquark normalisation.

It also keeps the adjudication result at the strongest justified level:

* the observed discrepancy was not caused by the tested L3 ordering map;
* this provides no evidence against the branch’s independence claim in that tested construction;
* it does not prove independence over untested admissible pp orderings.

That distinction should be preserved exactly in the addendum and report.

6. OPPOSITE is correctly constrained to a relative verdict

The specification does not promote OPPOSITE into an absolute channel label.

Its intended meaning remains:

η → -η reverses the non-zero coefficient signs for a fixed remainder of the construction.

It does not determine which representative is absolutely attractive or repulsive, and it does not settle the diquark channel.

This is an important limitation and is consistently stated in §§1–3, 7 and 9.

7. The combined scope is internally consistent

The frozen manifest contains eighteen additions:

* fourteen arriving from the two reviewed source branches;
* the integration specification;
* the pre-execution review;
* the sensitivity addendum;
* the integration report.

No modification is authorised.

The stated total of 18 additions and 0 modifications matches the manifest. The previous count inconsistency is not present here.

8. The sensitivity addendum has a legitimate dependency on both merges

Commit 5 is correctly placed after both merge commits.

The addendum records a relation among:

* the both-η result;
* the adjudication;
* the already-integrated chirality census.

Writing it before either arriving body of evidence was present in the task tree would make its provenance weaker. The sequencing therefore has substantive meaning rather than being cosmetic.

Items that must be re-verified by the Executor

Approval does not certify the repository observations written in §10. The Executor must independently reproduce them.

In particular:

1. both remote source refs and remote main;
2. the merge-base of each source branch against the current integration parent;
3. A2a’s two --is-ancestor negative observations, distinguishing exit 1 from execution failure;
4. both conflict-free PRE_MERGE guards;
5. all fourteen arriving blob IDs;
6. the final 18-addition / 0-modification scope;
7. all protected-path comparisons;
8. all eight validator executions;
9. both source branches and the protected review branch remaining unmoved;
10. final POST_MERGE verification with the merge object and pushed report head supplied in their distinct roles.

A failure of any one of those observations must be handled according to its actual observation state rather than mapped automatically to a negative result.

Review-artifact correspondence

This review corresponds specifically to the re-issued specification whose evidence base is:

57c5a6eb1de11bb7aaf27b779054070ee6870c29

and whose two source branch heads are:

3767973bf57c52f4dd2be1fddcf62916ec409c72

bc1e5c743aada004c52dc7ab7ce2af61de439955

The specification digest should be recorded by the Executor once commit 1 has fixed the exact specification artifact. The absence of that future digest from this pre-commit review is not a substitute for correspondence; the evidence base, branch heads, task title, re-issue status and prescribed branch gate/p2-land-diquark-line-v2 identify the reviewed task.

Stops and clarifications

No blocking SPECIFICATION_DEFECT found in this revision.

No ENVIRONMENT finding can be assessed pre-execution.

No current OBSERVATION_METHOD_ERROR is identified in the revised specification. The previous unexecuted merge-base CONFIRMED is explicitly retracted and replaced by executable observations.

No blocking REPOSITORY_DEFECT is established by this review.

No blocking UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY remains in the execution construction. The scientific ambiguities concerning η, pp ordering and diquark normalisation are intentionally preserved as subject-matter limitations, not execution ambiguities.

Disposition

APPROVE FOR EXECUTION.

The first issue’s stop was valid. This re-issue repairs the unsatisfiable merge-base requirement without rewriting either reviewed science branch, provides the missing stale-branch ancestry observation, specifies the aborted-task reporting path, and preserves the appropriate scientific limitations.

Execution should proceed only if the repository observations above reproduce exactly as required.
