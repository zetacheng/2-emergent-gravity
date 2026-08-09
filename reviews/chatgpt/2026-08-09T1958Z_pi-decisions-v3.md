Pre-execution review — replay PI decisions and deferred-items task on the current base

Reviewer: ChatGPT
Disposition: APPROVED / ISSUABLE

Review scope

I reviewed the task specification “replay the PI decisions and deferred-items task on the current base”, with specification evidence base:

7c5cba5df76de6ef8f52af390ca92100dcdf0d8b

The review covers whether the specification is sufficiently complete, internally consistent and mechanically defined for an Executor to perform the stale-base replay without making an unauthorised substantive, governance or representational decision.

This review is pre-execution. It authorises execution of the specification as reviewed; it does not authorise integration into main.

What I verified

I reviewed the specification’s stale-base construction and found it adequately distinguishes a replay from a repair or manual conflict resolution.

The specification does not claim that Amendment K already expressly defines stale-base loss of conflict-free integrability. Instead, it applies K’s re-issue discipline under explicit PI authorization and supplies the missing construction itself: a new branch from the current evidence base, a new task identity, preservation of the superseded execution, and re-instantiation of the already approved substantive content. This leaves no stale-base policy decision to the Executor.

I verified the approved source register at fix/pi-decisions-v2 @ ebd531ab568aaffabd86a4a94d925a711e62aa36 sufficiently to confirm the A4 premise relevant to this review:

derivations/P2-DEFERRED-ITEMS.md

has Git blob id:

ffeae5eb52115e131536e10508b72ac3ff51379d

and contains the authority reference:

Authority: specs/2026-08-09T1416Z_pi-decisions-v2.md.

Accordingly, requiring the v3 register itself to remain blob-identical to the v2 register would be incorrect: it would preserve an authority pointer to the superseded execution.

I specifically reviewed A4 after its earlier ambiguity was identified. The revised criterion now defines an executable task-identity normalisation function rather than merely describing permitted differences. It requires exact replacement of the execution-specific specification path with <TASK_SPEC>, exact replacement of an execution-specific report path, if present, with <TASK_REPORT>, and expressly prohibits every other replacement, deletion, whitespace normalisation or reformatting.

After that function is applied independently to source and destination, A4 requires the complete resulting register byte sequences to be identical. It also requires every pre-normalisation differing line to be reported. This is sufficiently strict to distinguish authorised task-identity substitution from substantive drift.

The specification additionally records that, on the source register, the v2 specification reference occurs once, the v2 report reference occurs zero times, and no pi-decisions-v2 or 1416Z identifier remains after substitution. A vacuous report substitution is explicitly permitted. The destination must be independently checked rather than assumed to have the same occurrence pattern.

I reviewed the separate normalisation specified for the three DECISION_LOG.md rulings. It is defined independently from the register comparison: blockquote prefixes, ** and backticks are stripped and whitespace is collapsed, while en dashes are preserved. The required substantive phrases are separately enumerated in A5. The specification expressly prohibits editing a ruling merely to make a phrase check pass.

I reviewed the append-only construction in A6. Because v3 is created directly from the current authoritative evidence base, the two governance entries already on main remain in place and the three approved PI rulings are appended after them. Their resulting position records entry into the authoritative lineage, not a rewritten decision date. No merge resolver is authorised to choose an ordering between independently appended histories.

I reviewed the Rule 15 lifecycle. The frozen order is specification, this pre-execution review, work, then report. The review therefore precedes the work it authorises.

I also reviewed the Rule 16 accumulated-reading requirement. The proposed junction is legitimate: preservation of several executions could be misread as several substantive revisions, whereas the specification distinguishes substantive revision from later representation/base re-issues. The Executor may report a stronger junction if one is actually established by the assembled evidence.

The specification protects the superseded branches, main, gates, existing derivations, tests, results, scripts, documentation and review records except for the explicitly authorised additions and DECISION_LOG.md modification. It forbids merge-conflict resolution, force-push, history rewriting, scientific computation and the separate SI-1 cross-reference work.

I found no remaining specification ambiguity that requires the Executor to decide the substance of the PI rulings, invent a stale-base replay procedure, choose a conflict ordering, or invent the equivalence semantics for the replayed register.

What I did not verify

I did not execute the task.

I did not create fix/pi-decisions-v3, commit any artifact, modify any repository path, push any ref, merge anything into main, or perform the authorised branch workflow.

I did not independently reproduce all seven A1 SHA-256 checks, all A2 evidence quotations, all eleven A5 phrase checks, the complete A4 source-to-destination equivalence comparison, the A6 append-only measurements, the A7 remote reachability checks, the A8 protected-path comparison, the A9 final scope check, or the A10 pytest validators. Those are execution-time acceptance criteria and remain obligations of the Executor.

I did not verify a destination P2-DEFERRED-ITEMS.md, because no v3 work artifact exists at pre-execution review time. In particular, the destination-side A4 substitutions, occurrence counts, differing-line report and final byte-equivalence result must be established during execution.

I did not independently establish that every factual statement describing the earlier dry-run conflict or every historical execution is complete beyond the repository evidence specifically checked above. The specification pins the relevant source and requires the Executor to re-verify rather than inherit those conclusions blindly.

This approval therefore does not convert any unexecuted acceptance criterion into a PASS.

Review finding

The earlier blocking issue in A4 is resolved.

The specification now defines the stale-base replay construction and its substantive-equivalence test with sufficient precision that the Executor should not need to supply missing governance or comparison semantics.

No blocking specification defect remains in the reviewed text.

Disposition: APPROVED / ISSUABLE.

Execution remains conditional on every STOP condition and acceptance criterion in the specification. A mismatch in a pinned input, missing or non-corresponding review artifact, unexplained substantive difference, unexpected repository state, merge conflict, validator failure, or inconsistency with an operative repository rule remains a STOP rather than being cured by this approval.
