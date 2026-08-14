# Pre-execution Review — Replace P1's Prose Inference with a Declared Total

**Review status: APPROVED FOR EXECUTION**

Task reviewed: **replace P1's prose inference with a declared total**

Specification evidence base: `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`

Proposed branch: `governance/p1-declared-total`

## Executive finding

The revised specification resolves the two blocking defects identified in the prior pre-execution review.

The proposed design is suitable for execution. Replacing P1's inference from nearby prose with an explicit `stated:` declaration inside the scope block is a materially cleaner boundary: the checker compares structured declared data with structured manifest data instead of attempting to infer which prose count the author intended to govern the block.

This review therefore approves execution subject to the specification's own stop conditions and acceptance criteria.

## 1. Declared-total design

The central design decision is approved.

`stated:` becomes the sole source of the declared total. P1 no longer consults prose anywhere in the document. This directly removes the observed false-positive class in which a dry-run count immediately preceding the scope block was mistaken for the final manifest count.

It also removes the line-wrapping ambiguity without replacing it with paragraph or sentence inference.

A disagreement between a valid `stated:` declaration and the enumerated manifest remains a genuine `FAIL`, preserving the property P1 is intended to test.

## 2. Legacy documents and NOT_PARSEABLE

The decision to make absence of `stated:` produce `NOT_PARSEABLE` is approved.

This deliberately reduces the number of historical specifications P1 can judge. That reduction must not be represented as improved coverage. It is instead a more accurate statement of the checker's knowledge boundary.

The historical planted five-versus-six specification consequently becomes `NOT_PARSEABLE` rather than `FAIL`. That regression is explicitly acknowledged by the specification and is acceptable because the mismatch property is preserved by a declared-total fixture.

No prose fallback should be introduced.

## 3. Path-shape validation

The proposed rejection of non-path tokens under `add:` and `modify:` is approved.

The live `(none)` incident demonstrates that arbitrary stripped text cannot safely be counted as a path. Invalid tokens should make the block `NOT_PARSEABLE`; they must not silently alter the manifest total.

The implementation and report should state the path-shape definition precisely, including reasonable repository-relative names it might reject.

`[]` remains the explicit empty-set representation.

## 4. A4 fixture obligations

The revised A4 resolves the prior review finding.

It now correctly separates two obligations:

1. every new fixture must have its old-parser result recorded individually; and
2. each distinct failure mode claimed as repaired must have at least one fixture demonstrating that the old parser cannot produce the intended new semantics, whether by a different verdict, the right verdict for the wrong reason, or inability to judge.

This avoids the previous overstatement that any fixture already passing under the old parser tests nothing.

The binding regression fixture is correctly identified: a contradictory dry-run count immediately before the scope block must fail under the old prose-inference behaviour and pass under the new declared-total behaviour because the prose is ignored.

The executor should identify explicitly which fixture discharges each repaired failure mode.

## 5. A5 corpus cardinality

The revised corpus accounting resolves the second prior blocking finding.

At the evidence base, the specification records:

- 37 `.md` specification files in total;
- 29 carrying exactly one scope block;
- 6 carrying no scope block; and
- 2 carrying more than one scope block.

The task adds its own specification, producing 38 files at the new head.

Accordingly, A5 and the report contract now consistently require a full **38-row** table.

The expected distribution is one `PASS` and thirty-seven `NOT_PARSEABLE`, with the legacy reasons reported rather than collapsed into a single token. The actual measured distribution governs.

The two multiple-block files were already unjudgeable and must not be described as newly broken by this change.

## 6. Classification correction

The proposed classification edit is appropriate provided the acceptance criterion is met exactly.

P1 remains `PARTIAL`. No `MECHANICAL`, `PARTIAL`, or `JUDGEMENT` verdict may change, and no `does_not_establish` statement may be weakened.

The classification should cease describing P1 as selecting a governing sentence and instead state that P1 operates on an explicit declaration inside the scope block.

Recording the measured pre-repair corpus behaviour — ten passing specifications among the twenty-nine single-scope-block documents — is appropriate evidence for P1's limitation.

## 7. Rule 16 assessment

The important inference junction after this task is `NOT_PARSEABLE`.

A corpus dominated by `NOT_PARSEABLE` must not be presented as a corpus checked and found acceptable. For those documents, P1 has made no correctness determination.

This distinction should appear where the reader encounters the corpus results, not only in a distant methodological note.

Prospective adoption of `stated:` as repository authoring syntax is a separate governance task. This task changes the checker grammar; it does not migrate historical specifications and does not establish repository-wide P1 coverage.

The narrower limit is also material: before this task, ten historical specifications happened to PASS P1. After the task, the expected number of judged documents is one. That is a reduction in coverage and an increase in honesty, not an improvement in coverage.

## 8. What this task establishes and does not establish

If executed successfully, this task establishes a substantially cleaner P1 proposition:

**For a specification admitting the declared-total syntax, P1 checks whether the explicit declared total agrees with the enumerated manifest.**

It does not establish that historical specifications satisfy P1. It does not establish that future specifications will use the syntax. It does not establish governance enforcement, because the checker is still not automatically invoked by CI.

The change therefore improves the semantic reliability of an available verification tool while intentionally narrowing the set of documents it can presently judge.

## 9. Execution-sensitive points

The executor should apply the specification's stop conditions literally.

In particular, RUN 2 in A10 remains stop-governing; the task's own specification must parse and pass under the grammar it commissions; no existing specification may be edited to manufacture coverage; P2 through P9 must remain outside the change; and no configuration or fixture may be weakened merely to obtain a green result.

The final report must preserve the evidence layering distinction between measurements available at commit 4 and post-report evidence available only after commit 5 exists.

## Decision

**APPROVED FOR EXECUTION.**

The two defects identified in the previous review have been corrected:

1. A4 now records every fixture's old-parser behaviour while requiring genuine regression evidence per repaired failure mode; and
2. A5 now uses internally consistent corpus arithmetic and requires the full 38-row new-head table.

I find no remaining specification contradiction that should block execution.

Approval is conditional only in the ordinary sense that the executor must obey the specification's explicit STOP conditions if the repository measurements differ from the stated premises or if any acceptance criterion fails.
