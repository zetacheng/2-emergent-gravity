# Pre-execution review — supply protocol v3 and superseded-branch attribute

Reviewer: ChatGPT (GPT-5.6 Sol)  
Disposition: **APPROVED — PRE-EXECUTION REVIEW**

## Review scope

I reviewed the task specification titled **“the review supply protocol, and a superseded-branch attribute”**, task identity `supply-protocol-v3`, at the stated evidence base:

`0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5`

The review covers the specification’s internal consistency, Rule-15 sequencing, the proposed Rule 18 file-supply protocol, the superseded-branch attribute and register construction, the stated acceptance criteria A0–A12, scope arithmetic, stop conditions, prospectivity, and the relationship between the two superseded prior executions and this re-issue.

The source branches explicitly carried into the proposed superseded register include:

- `governance/supply-protocol-v2 @ 40168469608618aef6812735ff70e32de0e3cbc8`
- `governance/supply-protocol-and-superseded @ 7146a093c65788a57d63a747b71d86edb91eddc6`

## What I verified from the specification

### 1. The re-issue resolves the A3 contradiction that stopped v2

The prior defect is addressed directly. The proposed Rule 18 abandons delimiter extraction and requires a review to arrive **as a file**, while A3 now tests for the corresponding file-supply content.

A3 positively requires:

- `AS A FILE`;
- `no delimiters`;
- a correspondence requirement; and
- a STOP condition for a missing, pasted, or non-corresponding review.

A3 also requires the old delimiter and blank-line concepts to be absent.

That is structurally consistent with §0. The earlier contradiction — §0 abandoning delimiters while A3 required them — is not present in this issue.

### 2. Rule 18 v3 removes the semantic boundary judgement

The proposed Rule 18 no longer asks an executor to identify a review boundary inside a mixed transport stream. It requires a supplied file and byte-unchanged commit.

That eliminates the failure class seen in the earlier delimiter protocol: delimiter strings inside instructions, missing delimiter lines, preamble placement, fused transport prefixes, and blank-line normalisation.

The specification also correctly makes a pasted review a STOP while permitting a pasted specification. That distinction is explicit rather than left to executor judgement.

### 3. The correspondence check is materially specified

The review must identify the specification by task name or digest before it may be committed.

That is a genuine remaining semantic check, but it is an authorised check rather than an inferred transport rule. The specification states what evidence is sufficient and what outcomes require STOP.

This review identifies the task by the task name `supply-protocol-v3` and by the title of the specification under review.

### 4. The superseded attribute is orthogonal to deletion state

The specification keeps the existing three-state deletion machine intact and introduces `SUPERSEDED` as an integration attribute rather than a fourth deletion state.

That separation is coherent:

- deletion eligibility remains governed by the existing Stage-1 states;
- integration eligibility gains an independent supersession attribute;
- the closed deletion-count identity is expressly protected by A5.

This avoids conflating “must be preserved” with “may be integrated”.

### 5. The register membership threshold is materially improved

The specification no longer requires the literal word `superseded` in prior artifacts. It requires a durable repository artifact to establish the underlying fact of re-issue, replacement, or supersession and to identify the replacement or reason.

That is a better evidentiary rule because it prevents both extremes:

- topology/name similarity alone cannot create a governance classification; and
- an established replacement is not excluded merely because an older artifact used different vocabulary.

The specification also correctly requires ambiguous candidates to remain outside the register and be reported as `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`.

### 6. The six supplied register entries are internally differentiated without ordinal dependence

The issue explicitly removes the earlier ordinal-reference defect. Entries are referred to by branch name and divided by evidentiary kind:

- approved work re-instantiated elsewhere;
- stop-only evidence with no work landed; and
- completed work whose execution contract made that instance non-integrable.

This is materially safer than statements such as “the third entry”, which became false as the register grew.

### 7. A0 now specifies the aborted-task report behaviour

The specification expressly handles a STOP before commit 3: the report is committed at the frozen report path as the next actual commit, with the skipped work commit explained rather than silently renumbered.

That closes the ambiguity previously improvised in two stopped tasks.

### 8. Scope arithmetic is internally consistent

A9 lists exactly six paths:

- three additions; and
- three modifications.

Its summary states `3 additions and 3 modifications`, matching the manifest.

I found no scope-count contradiction in the current issue.

### 9. Rule-15 ordering is coherent

A0 requires:

1. specification;
2. pre-execution review;
3. governance work;
4. report.

The review precedes the work. The STOP-path exception preserves the review-before-work principle and does not manufacture an unperformed work commit.

### 10. A4, A5 and A7 provide meaningful structural guards

The specification does not rely on heading counts alone:

- A4 requires Rules 1–17 to be byte-identical after removal of Rule 18;
- A5 requires the existing branching-policy deletion state machine and closed identity to remain byte-identical; and
- A7 requires append-only evidence against both the evidence base and commit parents.

These are appropriately stronger than proxy checks.

## What I could not independently verify

I do not have direct repository-object access in this review turn. Therefore I did **not** independently verify:

- the SHA-256 values in A1 or §8;
- the current remote value of `main`;
- whether all six named superseded branches are currently present at the stated commits;
- whether any of those branches is currently an ancestor of `main`;
- whether further remote branches satisfy the register threshold;
- the exact existing contents or formatting style of `CONVENTIONS.md`, `docs/BRANCHING_POLICY.md`, or `DECISION_LOG.md`;
- whether the Stage-1 deletion-state section is byte-identical before and after execution;
- validator behaviour or exit status;
- the final scope-checker output;
- commit-message hygiene;
- branch preservation after push.

Those are execution-time acceptance checks. The specification correctly treats mismatches in the material pinned facts as STOP conditions rather than asking the executor to repair or reinterpret them.

## Findings

I found **no blocking internal contradiction** in the current specification.

One point should remain explicit in execution reporting: Rule 18 v3 removes transport-boundary judgement, but it does not eliminate all judgement from review handling. The executor must still determine whether the supplied file “corresponds” to the specification. Here that judgement is bounded by an explicit criterion — task name or digest — so it is not the uncontrolled judgement that broke the delimiter protocol. The report should state exactly which correspondence marker was used.

A second non-blocking point is that the statement “Specifications have been supplied as files throughout” is historical justification rather than an acceptance predicate. Nothing in this approval depends on that historical claim being exhaustive. The operative rule stands or falls on its own file-supply procedure.

## Rule 16 / accumulated-reading assessment

The specification’s proposed junction is sound.

If Rule 18 and the superseded register land, a reader could infer that review supply and superseded-branch integration are mechanically enforced. They are not. Rule 18 records a required protocol and the register records a governance attribute; neither, by itself, guarantees that future tasks consult or obey them.

The strongest specific junction is:

`Rule 18 + superseded register + green existing validators`

does **not** establish automated enforcement of either rule. A future task can still omit the register check unless a mechanical governance checker or workflow explicitly reaches it.

That limitation should remain visible in the report and must not be converted into a claim that the governance gap is closed.

## Stops and clarifications

`SPECIFICATION_DEFECT`: none found in this issue.

`ENVIRONMENT`: none assessed; repository/environment execution was not available in this review.

`OBSERVATION_METHOD_ERROR`: none identified in the specification’s stated verification methods.

`REPOSITORY_DEFECT`: the known absence of mechanical enforcement remains expressly out of scope and is not repaired by this task.

`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`: none created by the specification itself. Any additional branch whose durable evidence suggests but does not establish supersession must remain outside the register and be reported under this category, as the specification requires.

## Disposition

**APPROVED.**

This specification is internally coherent enough to execute. The principal defects that stopped or weakened the two prior issues are now addressed: the delimiter protocol is replaced rather than patched; A3 matches the rule actually being landed; the superseded register uses branch names rather than ordinals; the evidence threshold distinguishes observation from classification; and the STOP-report commit path is explicitly defined.

Approval is conditional only in the ordinary execution sense: all pinned facts, remote refs, branch ancestry, byte-identity checks, append-only checks, validators, and final scope must still reproduce exactly as A1–A12 require. Any specified STOP condition remains dispositive.
