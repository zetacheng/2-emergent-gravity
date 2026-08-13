# Pre-execution review — integrate the science line, and land it

**Review status: APPROVED FOR EXECUTION.**

**Task:** `integrate-phase01-line`

**Reviewed specification SHA-256:** `b40415c71fa4a747328f56f1b43fd7ccc55b9b0769e1137142689aae9e6f4070`

**Reviewed specification:** `Task specification — integrate the science line, and land it`

**Evidence base named by the specification:** `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`

This review approves **only the specification at the SHA-256 above**. A file with the same task name but different bytes is not covered by this review.

## 1. Disposition

**APPROVED FOR EXECUTION.** I find no unresolved specification defect that prevents execution as written.

The material integration risk is concentrated in merge 2, and the specification now resolves it adequately. In particular, the `GATES.md` resolution is defined by semantic blocks rather than by conflict-marker geometry: preserve source 1's already-landed MICROSCOPIC PARAMETER DOMAIN block byte-for-byte, replace only the PHASE INPUT / ADMISSIBILITY CONTRACT block with source 2's adopted block, and preserve the separating blank line. A5 independently makes byte identity of the preserved parameter-domain block a stop-governing check. Together these prevent an accidental rollback caused by taking an incoming conflict side too broadly.

The second authorised conflict, in `derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md`, is also sufficiently specified. The reviewed reconciliation text resolves the genuine contradiction between source 1's later `OPEN-AC-2` / `OPEN-AC-5` state and source 2's historical statement that all entries remained open, while leaving the pre-existing `OPEN-AC` bodies untouched.

## 2. Scope and evidence layering

The scope arithmetic is internally coherent. The final manifest states **26 additions and 3 modifications**. The specification separately identifies the pre-report merge-head state as **25 additions and 3 modifications**, with the report itself supplying the twenty-sixth addition. That distinction is correctly tied to the head at which each figure is measured.

A9 correctly separates three different comparison classes that must not be conflated: the twenty-three added paths arriving blob-identical from their source commits; the parameter-domain draft, which must match source 1; and the reconciled admissibility-contract draft, which is expected to match neither source because §4b authors reviewed integration text.

The source-1 ancestry rule is also clear: `8b79fad4…` already contains the earlier parameter-domain adoption and repair commits, so those ancestors must not be merged separately.

## 3. Gate-state review

The intended integrated state is coherent: `P2-PHASE-01` remains `PROPOSED`, while both prerequisite blocks read `SATISFIED`. The specification repeatedly distinguishes prerequisite completion from scientific evaluation. It expressly requires `Required computations` to remain not started, leaves the evaluation-input gaps open, and forbids evaluating any candidate during integration.

The pin requirements are also coherent in the final form: A7 expects exactly two operative pins in the merged `GATES.md`, both matching the adopted artifacts. The contract draft becomes unpinned after its prerequisite block is replaced, and the specification requires that fact to be stated explicitly rather than inferred.

## 4. Conflict-resolution review

### `GATES.md`

**Approved.** The normative resolution is semantic and does not depend on where Git places conflict markers. This is the important repair over the earlier formulation.

A5's additional requirement that the MICROSCOPIC PARAMETER DOMAIN block be byte-identical to source 1 is necessary and sufficient as a stop condition against accidental rollback.

### Admissibility-contract draft

**Approved.** The supplied reconciliation is substantive integration text, but it is pre-reviewed here and therefore does not require the executor to invent content. It preserves the historical draft, records the later authoritative cross-reference, and keeps `OPEN-AC-1`, `OPEN-AC-3`, and `OPEN-AC-4` open.

No third conflict is authorised. The specification correctly makes any additional conflict an immediate STOP.

## 5. Checker and governance limits

The specification correctly refuses to treat P7 as evidence of gate integrity. Its stated parser defect makes the P7 `PASS` vacuous at this evidence base. The substantive confinement of the gate edit therefore rests on A5, A7, A8, A9 and A10, not on P7.

RUN 2 is appropriately stop-governing, while RUN 1 is observational. The specification also correctly requires the executor to report the actual default subject set rather than infer it from the prose.

## 6. Rule 16 review

The three required junctions are appropriate and should remain explicit in the report.

First, two satisfied prerequisites do **not** mean the gate has run or that a phase has been found. Second, the integration repairs a misleading split-branch state in which each adoption branch showed only half of the eventual prerequisite state. Third, the checker can return a vacuous P7 green beside a material `GATES.md` change, so that result must not be presented as gate-integrity evidence.

The specification also correctly preserves the arriving inaccuracy in `specs/2026-08-13T0740Z_adopt-admissibility-contract.md` rather than rewriting historical source content during integration: its reference to “all four pins” is wrong for the merged state, where A7 expects and measures two. The report must name the inaccuracy and place the measured count beside it.

## 7. Non-blocking observation

The phrase **“take the incoming side entire”** remains in the §4a heading/history, but the operative instructions immediately below supersede that older marker-relative formulation with the semantic-block resolution. Read in context, it is retrospective explanation rather than an executable instruction. I do not treat it as a blocker.

If this wording is ever revised before execution, the specification digest will change and this review will no longer apply; a new review artifact would be required.

## 8. Stops and clarifications

`SPECIFICATION_DEFECT`: none found that blocks execution.

`ENVIRONMENT`: none established by this review; execution-time environment checks remain the executor's responsibility.

`OBSERVATION_METHOD_ERROR`: none in the reviewed specification that requires correction before execution. The specification itself records and retracts earlier measurement errors where relevant.

`REPOSITORY_DEFECT`: the known P7 gate-heading parser defect remains open and is explicitly outside this task; the specification correctly prevents reliance on it.

`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`: none that blocks this integration. The authorised conflict resolutions, landing authority, source order, scope, and stop conditions are sufficiently explicit.

## 9. Final review statement

**APPROVED FOR EXECUTION at reviewed specification SHA-256 `b40415c71fa4a747328f56f1b43fd7ccc55b9b0769e1137142689aae9e6f4070`.**

The executor should follow the four-source merge order exactly, apply only the two reviewed conflict resolutions, stop on any additional conflict or scope deviation, complete the pre-landing checks including A12-final, and advance `main` only by the authorised fast-forward landing after all stop-governing checks pass.
