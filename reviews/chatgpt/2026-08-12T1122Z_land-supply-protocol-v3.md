# Pre-execution review — land the supply protocol integration on main

**Reviewer:** ChatGPT (GPT-5.6 Sol)  
**Disposition:** **APPROVED — MATERIAL, with non-blocking clarifications**  
**Task:** `land-supply-protocol-v3`  
**Specification evidence base:** `cc8adaa04ed75f5118ae2c25926a05e51a0056ff`  
**Authoritative main before landing:** `0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5`  
**Reviewed integration head:** `cc8adaa04ed75f5118ae2c25926a05e51a0056ff`

## Review scope

I reviewed the supplied task specification as a governance and execution contract. The review covers internal consistency of the stated commit order, the fast-forward-only landing model, the distinction between the reviewed integration head and the final authoritative `main`, the scope and ancestry criteria, Rule 15 / Rule 18 handling, protected-tree requirements, branch-preservation requirements, post-advance verification, and the stated evidence layering.

This review does **not** independently reproduce the Git measurements in §9. In particular, I have not independently fetched the repository or recomputed the stated refs, tree objects, blob identities, ancestry relations, validator results, or branch tips. Those remain execution-time acceptance criteria and must be measured by the executor exactly as specified.

## What I verified from the specification

The task now supplies the authority that the preceding integration specification omitted: it explicitly authorises advancing authoritative `main`, and limits that advance to a plain fast-forward. The prohibitions against merge, rebase, squash, cherry-pick, revert, force-push and history rewrite are consistent with that objective.

The departure from landing `main` exactly on `cc8adaa0…` is sound. Rule 15 requires this task's review to precede the authorised work, and the task also requires its own report to become part of the authoritative history. Therefore the final target must descend from `cc8adaa0…`. A3 and A5 correctly preserve the substantive property that matters: the reviewed integration head and its merge commit remain ancestors, while the only tree changes above `cc8adaa0…` are this task's three governance artifacts.

A3 and A4 separate the two relevant scopes correctly. `cc8adaa0… -> commit 3` is exactly three additions and no other operation; `0ab6369a… -> commit 3` is the reviewed integration plus those three additions, for nine additions and three modifications. This avoids re-deriving or silently modifying the reviewed integration.

A5 is appropriately stronger than merely checking that the branch tip descends from old `main`: it separately verifies ancestry of both the reviewed integration head and merge commit, and constrains the merge count. That protects against rebuilding the integration by a different route.

A6 correctly replaces file-count reasoning for `tests/` with tree-object identity. That is the exact property required here and removes the earlier proxy/count ambiguity.

A8 and A9 preserve the integration branch, source branch and superseded branches rather than collapsing landing into branch cleanup. That is consistent with the repository's evidence-preservation model.

The report/post-report split is coherent. The report can record the intended ref advance and pre-advance checks; the actual remote `main` update, read-back and post-advance ancestry necessarily belong to post-report evidence.

## Rule 18 / authority reading

I would apply Rule 18 for the review-supply procedure in this task.

The task's evidence base is `cc8adaa0…`, which contains Rule 18. The fact that authoritative `main` has not yet advanced to that commit creates a governance-authority question, but it does not create an execution ambiguity here because §3 independently imposes the same file-supply procedure as a specification instruction. The chosen reading therefore changes no executor action.

This should be reported exactly as the specification requests rather than used as a reason to stop.

## Non-blocking clarifications

First, the phrase “advance `refs/heads/main`” should be implemented as an update of the **remote authoritative main ref**, not as an unnecessary mutation of a stale local `main` worktree. The acceptance criteria consistently make remote `refs/heads/main` dispositive. A plain push of the verified commit-3 SHA to `origin:refs/heads/main`, without force or force-with-lease, satisfies the substantive requirement while avoiding an unrelated local-main operation. The executor should report the exact push command.

Second, A5's merge-count statement should be measured against the final target commit rather than inferred from the current `main` ref before the push. The intended property is clear: in the range `0ab6369a..commit3`, the existing integration merge `48268e6c…` is the only merge commit and this landing task adds none.

Neither clarification changes the authorised tree, ref target, scope, or disposition.

## What the task does not establish

Landing this branch does not make Rule 18 or the superseded-branch register mechanically enforced. It makes them authoritative repository content. The junction identified in §6 is the correct Rule 16 risk: future readers may confuse “present on `main`” with “machine-enforced”. No acceptance criterion in this task closes that gap, and none should.

The landing also does not reopen or re-review the substantive content of `cc8adaa0…`; A5 deliberately treats that integration as contained evidence rather than reconstructing it.

## Stops and clarifications

**SPECIFICATION_DEFECT:** none found that blocks execution of this re-issued landing task.

**ENVIRONMENT:** not assessed by this review; execution-time Rule 13 handling remains applicable if an environment failure occurs.

**OBSERVATION_METHOD_ERROR:** none found in the specification's stated methods. The `tests/` tree-object comparison is specifically an improvement over the earlier count proxy.

**REPOSITORY_DEFECT:** the known enforcement gap remains: written governance rules and the superseded register are not automatically enforced.

**UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY:** the formal question whether Rule 18 is operative merely because it exists at this task's evidence base while not yet on authoritative `main` remains conceptually open. It is non-blocking here because §3 independently requires the same file-supply action.

## Final disposition

**APPROVED.**

Execution is authorised only if A1 confirms that remote authoritative `main` is still exactly `0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5` and A2 confirms a plain fast-forward to commit 3. If either premise fails, the correct outcome is **STOP**, not conversion into a merge or another integration task.

The specification is materially stronger than the preceding integration contract because it now makes the final authoritative-ref mutation explicit and constrains it independently from the reviewed integration tree.
