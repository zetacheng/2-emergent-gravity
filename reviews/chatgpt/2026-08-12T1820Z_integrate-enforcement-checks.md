# Pre-execution review — integrate the governance checker, and land it

**Task:** `integrate-enforcement-checks`

**Review verdict: APPROVED FOR EXECUTION**

The revised specification resolves the material self-reference identified in the previous review.

## 1. Evidence layering is now coherent

The governing checker runs are moved to **commit 3**, the merge commit and pre-report head. Their configs and JSON outputs therefore exist before the report is authored and can legitimately be included in **commit 4**.

The specification also correctly separates facts that cannot exist until commit 4 exists:

- final base-to-commit-4 scope;
- RUN 2 re-executed at commit 4;
- commit-4 stored-message inspection;
- post-report path re-verification;
- final validators at pushed `main`;
- final `POST_MERGE`;
- landing and remote-ref readback.

Those are explicitly classified as **post-report evidence returned to the Reviewer and not written back**. This removes the previous circular requirement that commit 4 contain measurements of itself.

The sentence

> Nothing in the committed report may claim to be a measurement of an object that did not exist when it was written.

is the correct governing principle and should be followed literally.

## 2. A10's two-run design is internally sound

The two P1 runs now answer two different questions without silently tuning the checker.

**RUN 1** uses default subject discovery and is observational only. It may expose the merged source specification and its deliberate five-versus-six P1 failure. That failure is allowed to remain visible and does not govern the integration.

**RUN 2** fixes the subject to the current integration specification and is the stop-governing run. Its exclusion of the source specification is required to be visible in the config and explicitly explained in the report.

This is an appropriate treatment of the discovery boundary. It does not pretend that caller-supplied subject selection is objective discovery.

Running RUN 2 again at commit 4 before landing is also coherent. That later run can include this task's own report as a P9 subject without asking commit 4 to contain evidence produced after commit 4 exists. A failure there correctly stops the task before `main` advances.

## 3. The scope and protected-path criteria are consistent

The path arithmetic is coherent at both evidence layers:

- commit 3: **8 additions, 0 modifications**;
- intended/final commit 4: **9 additions, 0 modifications**.

The report path is the sole difference.

A7 correctly protects only paths that existed at the evidence base while allowing the two authorised base-absent additions under `tests/` and `scripts/governance_tools/`. It also correctly rejects the previous tasks' tree-identity predicate for `tests/`, because this task intentionally adds `tests/test_task_checker.py`.

The test count states its predicate explicitly (`test_*.py`), avoiding the earlier 17/18/19 counting ambiguity.

## 4. Merge and landing sequencing is coherent

Rule 15 ordering is preserved:

1. specification;
2. review;
3. no-ff merge;
4. report;
5. fast-forward authoritative `main` to commit 4.

The merge and landing are distinct operations with distinct rules. The merge must be `--no-ff`; the landing must be a plain fast-forward or a stop. No second integration task is required.

The final `POST_MERGE` correctly uses the merge object and the pushed `main` head as two distinct SHA roles.

## 5. The known false `MEASURED` line is handled without rewriting reviewed history

The incoming source specification's false line is not silently repaired. Its correction arrives in the source report, and this task requires the correction-discoverability issue to be surfaced under Rule 16.

That is the appropriate integration treatment. The false line is an already-reviewed historical artifact; changing it here would violate the merge-integrity rule.

## 6. Available verification is not confused with enforcement

The specification remains precise on the central semantic limit:

- the checker exists;
- its tests exercise the checker;
- CI does not invoke the checker;
- twenty-two of twenty-nine classified governance objects have no machine behind them;
- Rule 18 remains judgement-only.

Therefore the result is **available governance verification**, not enforced governance.

The Rule 16 assessment should retain that distinction prominently after landing.

## 7. One execution note on the report contract

Section 10 asks for some evidence that exists only after the advance, including the post-advance A9 statuses and the remote ref readback.

This is **not a blocking inconsistency**, because §5 expressly separates post-report evidence from the committed report. The executor should therefore interpret §10 as the complete reporting contract across both evidence layers:

- pre-report facts go into commit 4;
- post-report / post-advance facts are returned to the Reviewer and are **not** written back into commit 4.

Do not collapse those layers.

## Review finding classification

- **SPECIFICATION_DEFECT:** none blocking in this revision.
- **ENVIRONMENT:** none identified.
- **OBSERVATION_METHOD_ERROR:** none introduced by this revision.
- **REPOSITORY_DEFECT:** the correction-discoverability gap remains intentionally open and must be reported under Rule 16.
- **UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY:** none requiring a stop.

## Approval

**APPROVED FOR EXECUTION.**

The previous commit-4 self-reference has been removed. The specification now provides a satisfiable ordering for merge-time checks, report authorship, post-report verification, and final landing without requiring history rewrite, an extra commit, or silent evidence substitution.
