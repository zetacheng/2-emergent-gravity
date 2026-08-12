# Pre-execution review — integrate-supply-protocol-v3

**Reviewer:** ChatGPT

**Disposition:** APPROVED

**Specification reviewed:** `integrate-supply-protocol-v3`

## Review scope

This review assesses the supplied integration specification for internal consistency, executability, acceptance-criterion coherence, evidence-layer separation, merge-parentage logic, scope arithmetic, protected-path treatment, superseded-branch handling, and whether the previous five-versus-six register defect has been fully propagated through the specification.

This review does **not** independently read the Git repository or re-run the pre-issue Git commands. The object identities, blob ids, branch tips, byte lengths, ancestry results, dry-run merge result, validator expectations, and register contents recorded in §10 therefore remain executor-verification obligations under A1–A13.

## Findings

### 1. The prior register-count defect is corrected throughout

The previous blocking defect is resolved.

The specification now consistently treats the superseded register as containing **six entries**:

1. `fix/pi-decisions-and-deferred @ 52f65117…`
2. `fix/pi-decisions-v2 @ ebd531ab…`
3. `governance/supply-protocol-v2 @ 40168469…`
4. `governance/supply-protocol-and-superseded @ 7146a093…`
5. `review/role-model-and-executors @ 10c260b9…`
6. `gate/p2-land-diquark-line @ d64cd912…`

That correction has propagated to §0, §2, §3, A9, A11, §9 and §10. A11 additionally requires the six branch names to be listed, so a correct numerical count cannot conceal a wrong target set.

The earlier five-entry pre-issue record is explicitly retracted and its observation-method error is explained: the count came from truncated output rather than the complete object. That is the correct treatment of the earlier defect.

### 2. Merge parentage is coherent

A2 is internally consistent with the commit order in §5.

The merge is performed after the integration specification and pre-execution review have been committed, so:

- parent 1 is the review commit;
- parent 2 is the pinned source branch head `aa531aea…`;
- the merge-base is the evidence base `0ab6369a…`;
- commit 1 is required to be an ancestor of parent 1.

The specification explicitly requires the three values to be derived independently rather than inferred from one another. This correctly avoids the shared-rationale failure seen in the earlier diquark integration specification.

### 3. Scope arithmetic is consistent at both relevant heads

A4 distinguishes the merge head from the final report head.

At the merge commit, the expected base-to-head scope is:

- 5 additions;
- 3 modifications.

After the report commit, the final scope is:

- 6 additions;
- 3 modifications;
- 9 paths total.

The manifest contains exactly six additions and three modifications. The explanation of which paths arrive from the source branch and which are authored by the integration task is consistent with that arithmetic.

### 4. Review supply is not circular

The specification correctly states that Rule 18 is **not yet operative** at the evidence base.

The file-supply requirement in §4 is therefore an instruction of this integration specification, not an attempt to apply a rule before it has entered authority. This avoids the circularity that caused an earlier supply-protocol execution to stop.

A5 is compatible with §4: the review must arrive as a file, identify this specification by task name or digest, and be committed byte-identical to the supplied file.

This review identifies the specification by the task name `integrate-supply-protocol-v3`.

### 5. Protected-path treatment is coherent

A7 correctly removes the three intended governance modifications from the protected set:

- `CONVENTIONS.md`
- `DECISION_LOG.md`
- `docs/BRANCHING_POLICY.md`

Those paths are instead pinned to their source-branch blobs under A6.

The remaining pre-existing paths under the protected prefixes are required to remain blob-identical. This is internally consistent with the integration's purpose and avoids the common defect of simultaneously authorising and prohibiting the same modification.

### 6. Append-only verification uses two distinct properties

A8 correctly requires both:

- zero deleted lines; and
- exact byte-prefix preservation.

The specification expressly states that the first is not a proxy for the second. This is sound.

### 7. Superseded-branch coverage is now complete for the landed register

A9 checks **all six** register members, not only the two direct predecessors named in §3.

That is the correct property. The six `git merge-base --is-ancestor` results are required individually, and the six branch tips must also remain at their recorded commits after the task.

The prohibition against reading from register branches should be understood as prohibiting use of their contents as task input; A9's ref-resolution and ancestry checks necessarily inspect Git graph metadata. The specification's operational requirements make that distinction clear enough that I do not treat it as an inconsistency.

### 8. Rule and register counting methods are appropriately specific

A11 no longer accepts a bare number.

For the register, it requires:

- reading the fenced block under `## Superseded branches`;
- counting entry records;
- reporting the six branch names.

That is materially stronger than vocabulary counting or heading counting and directly addresses the previous observation-method failure.

### 9. Evidence layering is coherent

The committed report is limited to evidence available before the final report commit, while the final `POST_MERGE`, final scope check, final validators, push confirmation, stored report message, and ancestry confirmation remain post-report evidence.

The final guard correctly distinguishes:

- the merge object under verification; and
- the final pushed report-commit head.

No evidence-layer contradiction is apparent.

## Non-blocking observations

The historical sentence in §0 describing Rule 18 as the “ninth attempt” and referring to “the five preceding failure modes” is not used by any acceptance criterion. Earlier execution history recorded differing tallies of attempts and failure modes. I would not block integration on that prose because the governance content being merged is pinned by object identity and A6, but future historical summaries should avoid relying on that sentence as a canonical count.

The phrase “do not read from” superseded branches is broader than the literal operations A9 requires. Ref lookup and ancestry testing are necessary to satisfy A9 and do not consume branch contents as substantive evidence. If this wording is reused later, “do not read branch contents” would be more precise.

Neither observation makes the present task internally inconsistent.

## What this review verified

From the specification text itself, I verified:

- the previous five-versus-six defect is corrected throughout the operative criteria;
- A2 matches §5's commit order;
- A4's manifest arithmetic is internally consistent;
- A5 is compatible with §4 and does not rely on Rule 18 already being operative;
- A6 and A7 divide authorised modifications from protected paths consistently;
- A8 preserves two distinct append-only measures;
- A9 covers all six register entries;
- A11's counting method measures entry records rather than a proxy;
- the report contract and evidence layering are mutually consistent;
- no instruction in the supplied text requires the executor to choose between conflicting acceptance criteria.

## What this review did not independently verify

This review did not independently verify:

- remote and local refs in A1;
- the actual merge-base or dry-run merge result;
- the six source blob ids in A6;
- the protected-path blob comparison in A7;
- the `DECISION_LOG.md` byte lengths or prefix relation in A8;
- the six ancestry exit statuses and branch-tip values in A9;
- the `GATES.md` blob, gate count, or gate status in A10;
- the actual 18-rule and 6-entry counts in A11;
- validator results in A12;
- commit-message hygiene in A13;
- the clean-clone measurements recorded in §10.

Those are executor checks and remain mandatory. Any mismatch at execution is governed by the specification's STOP conditions.

## Stops and clarifications

**SPECIFICATION_DEFECT:** none blocking.

**ENVIRONMENT:** none identified from the specification.

**OBSERVATION_METHOD_ERROR:** the prior five-entry count was an observation-method error caused by truncated output; this version explicitly retracts it and replaces it with a complete-object counting method. No new observation-method defect is apparent in the specification.

**REPOSITORY_DEFECT:** none established by this review.

**UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY:** none blocking. The distinction between recorded governance and mechanical enforcement is explicitly preserved in §2 and §7.

## Disposition

**APPROVED FOR EXECUTION.**

The previous blocking register-count defect has been corrected and propagated through the integration specification. I find no remaining internal inconsistency that would require the executor to choose between competing instructions. Execution remains conditional on the repository-level checks A1–A13 reproducing the pinned evidence.
