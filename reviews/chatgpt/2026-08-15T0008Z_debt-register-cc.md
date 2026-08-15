# Pre-execution review — `C-c`: authoritative governance-debt register

**Verdict: APPROVED**

reviewed specification SHA-256: `3b145a2a4bef0bad6e0ccbc301ba172a6c89d357628f859e57ef8ab953582ec1`

## Review determination

I approve this specification for execution.

The task is appropriately scoped as a **recording task rather than a repair or mechanism task**. It creates an authoritative governance-debt register, adds one discoverability pointer in `CONVENTIONS.md`, and expressly forbids using this task to repair the debts it records. That separation is important and is stated consistently through the specification.

The specification also correctly preserves the distinction between governance debt and the existing science-side registers. `OPEN-CC-3` is cross-referenced rather than duplicated, and the register is expressly non-binding.

## Material points reviewed

### 1. `G-04` is now correctly scoped

`G-04` is limited to the missing authoring enforcement for `stated:` on newly issued scope-bearing specifications. It does not fold `append_only:` or `authorised_gates:` into the same obligation.

The specification separately requires measurement of those two declaration keys and expressly forbids silently converting any observed absence into a twelfth debt item. This is the correct boundary after C-b.

### 2. `G-09` identifies the remaining grammar risk correctly

After C-b there is one shared gate-heading grammar. The residual debt is therefore not continued divergence between two production grammars; it is the absence of an independent oracle capable of detecting a common-mode mistake in the shared grammar.

`G-09` states that residual accurately. Its expected `OPEN` disposition is appropriate unless execution discovers a genuinely specified mechanism shape.

### 3. The disposition taxonomy is suitable for a register

The six dispositions distinguish repairability, external constraints, already-existing mechanisms, genuinely open problems, and deliberately unchosen approaches without pretending that registration itself closes any item.

In particular, `G-09` and `G-10` should remain `OPEN` unless the evidence gathered by this task supports a more specific mechanism. Naming a regress problem is not itself a mechanism.

### 4. Discoverability is part of the task without becoming a new rule

The single pointer in `CONVENTIONS.md` is justified by the purpose of the register and by the already-recorded correction-discoverability problem. The specification confines that edit to one pointer line and requires verification that `CONVENTIONS.md` is not gate-pinned.

This does not turn the register into a binding governance source. The specification repeatedly requires the register to state that it creates no obligation.

### 5. Self-verification is materially improved

The pre-issue and execution criteria do not restrict verification to repository facts. They also require factual assertions about this specification's own bytes and scope block to be checked directly.

That is an appropriate response to the earlier class of specification defect in which a criterion asserted that its own specification contained declarations that were not actually present. This task uses that lesson without attempting to build the deferred cross-document-consistency mechanism.

## Clarification to preserve in execution

There is one wording ambiguity that is **non-blocking but should not be amplified in the report**.

The sentence stating that "`C1` and `C3` are not entered as open debt" and that "their residuals are `G-09` and `G-04`" can be read as mapping `C3` to `G-04`. The body of the specification is clearer: `G-09` is the residual associated with the former gate-heading grammar problem, while `G-04` is explicitly the remaining `C2` authoring-enforcement gap for `stated:`. The residual question concerning whether `append_only:` or `authorised_gates:` should have been declared is deliberately not classified as an additional debt item here.

Execution should preserve the body's explicit mapping and must not report `G-04` as the residual of `C3`.

This does not require editing the reviewed specification and does not prevent execution because the operative definitions of `G-04`, `G-09`, A5, and the frozen eleven-entry scope are unambiguous when read together.

## Scope and governance assessment

The specification is materially reviewable and bounded. It fixes the entry count at eleven, freezes the allowed paths, prohibits repair work, requires exact scope checking, retains the branch-only outcome, and separates committed evidence from later integration.

No inconsistency requiring a STOP was identified in the reviewed specification.

## Final verdict

**APPROVED FOR EXECUTION.**

Approval is for the specification whose SHA-256 is recorded above. A byte-different specification requires a new review or an explicit process permitted by the repository's governing rules.
