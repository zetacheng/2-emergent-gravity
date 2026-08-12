# Pre-execution review — mechanical enforcement for the governance rules that admit it

**Reviewed specification:** `Task specification — mechanical enforcement for the governance rules that admit it`  
**Evidence base stated by specification:** `8939ff4a46445d88c6470fb4f27eec71f2f39172`  
**Review verdict:** **APPROVED FOR EXECUTION**

This revision resolves the blocking defects identified in the previous review. In particular, P2 now defines the task-record set so that a stopped task with only specification, review and report genuinely has no work commit; P5 is explicitly PARTIAL and no longer claims that repository state can prove an executor's independent derivation process; P1 now requires a grammar; P3 and P7 expose the declaration-discovery problem instead of hiding it; and Rule 15 prospectivity is parameterised rather than silently interpreted.

I find no remaining contradiction that prevents execution.

## 1. P2 is now internally consistent

The earlier contradiction is removed.

A WORK COMMIT is now defined as a commit changing at least one path outside:

- `specs/`
- `reviews/`
- `reports/`

Therefore a stopped task containing only a specification, review and report contains no work commit, and P2 is satisfied because there is nothing to order. This follows from the property itself rather than from an implementation exception.

The required two-merge case is also correctly separated from the review-before-work requirement: a later merge may legitimately have the preceding merge as parent 1.

**Verdict: sound.**

## 2. P5 is now honestly PARTIAL

The revised P5 correctly distinguishes two different claims.

The checker can mechanically recompute and verify:

- parent 1 against the merge object's first parent;
- parent 2 against the merge object's second parent;
- merge-base by a fresh `git merge-base(parent1, parent2)`;
- stated ancestry relations against Git objects.

It cannot prove that the executor mentally or procedurally derived those facts independently. The specification now says so explicitly and requires the checker JSON to state what a PARTIAL check does not establish.

That is the correct boundary. The previous proxy-substitution defect is removed.

**Verdict: sound.**

## 3. P1 has a defined grammar and a proper failure mode

P1 no longer means “find some count near some manifest”. It defines:

- the scope block;
- the counted set;
- the governing sentence;
- a `NOT-PARSEABLE` result when the grammar does not identify one unambiguous target.

That is materially stronger than a prose-number search and is sufficient for the deliberately planted A9 defect.

The planted `five additions` / six-path manifest mismatch remains a legitimate falsification test because it is narrowly pre-authorised, must be detected as a failure, and is explicitly exempted from §5's normal stop rule.

**Verdict: sound.**

## 4. P3 and P7 correctly expose the declaration-discovery boundary

Both properties now distinguish the mechanical measurement from discovery of the set being measured.

For P3, line deletion counts and byte-prefix identity are mechanical once the append-only file set is known.

For P7, byte identity of every non-authorised gate section is mechanical once the authorised-modified set is known.

The specification correctly permits either:

1. caller-supplied sets; or
2. a fixed machine-readable declaration syntax.

It expressly forbids semantic inference from unrestricted prose while claiming a MECHANICAL result.

**Verdict: sound, subject to the implementation constraint in §8 below.**

## 5. Prospectivity is no longer silently chosen

The specification now requires both INCLUSIVE and EXCLUSIVE readings of the Rule 15 boundary to be run and compared.

This is the correct way to handle the remaining governance question: the checker measures whether the readings differ over the tested history, while refusing to decide which reading is authoritative if they do differ.

That keeps the tool on the mechanical side of the line.

**Verdict: sound.**

## 6. The classification scope is now coherent

A3 commissions exactly the objects the specification itself discusses:

- 18 numbered rules;
- 11 lettered amendments, A–I, K and L;
- 29 classified objects in total.

This avoids the earlier mismatch in which examples such as Amendment G and Amendment I were used to explain JUDGEMENT while amendments were outside the classification scope.

The pre-issue record also names the counting methods, including the absence of Amendment J.

**Verdict: sound.**

## 7. A9 remains deliberately defective, not inconsistent

A9 says `five additions` while listing six paths, and then explicitly states that this is a planted P1 violation.

The specification further provides the only authorised exception:

- P1 MUST fail on this specification;
- that failure is reported;
- execution proceeds using the six-path manifest;
- any other checker failure retains the normal stop behaviour.

This is a controlled negative test, not an unresolved conflict.

**Verdict: retain as written.**

## 8. Three implementation constraints the executor must preserve

These are not specification blockers, but violating any of them would turn the implemented checker into a proxy.

### 8.1 Non-applicability is not PASS

Some properties will not apply to every range. Examples include:

- P5 on a task with no merge;
- P3 when no append-only set is supplied or deterministically declared;
- P1 on a specification that is `NOT-PARSEABLE` under the grammar.

The checker must distinguish at least conceptually between:

- PASS;
- FAIL / governance failure;
- NOT_APPLICABLE or OUT_OF_SCOPE;
- NOT_PARSEABLE / insufficient machine-readable input;
- TOOL_ERROR.

A missing subject must not become a green result. This is particularly important because A5 explicitly requires a fixture where P3 is not told that a file is append-only and “must not silently pass”.

### 8.2 Caller-supplied declaration sets must be explicit checker inputs

§1(b) says the checker takes a base and a head. P3 and P7 additionally permit caller-supplied declaration sets.

If that route is chosen, those sets must be explicit command-line/API inputs or an equally explicit structured input, not values inferred inside the checker from unrestricted prose.

Adding optional structured inputs is consistent with “taking a base and a head”; silently reconstructing them is not.

### 8.3 P5 must not invent a prose parser for “recorded” values

P5's mechanical core is fresh recomputation of Git facts. If comparison against task-recorded parent values is implemented, those recorded values need a deterministic source or explicit input.

If no machine-readable source exists, the checker should report the recomputed facts and classify the comparison-to-recorded-prose portion as unavailable/partial rather than scrape arbitrary prose and call the result mechanical.

The classification document and JSON limitation field should make this boundary visible.

## 9. P6 deserves scrutiny during classification, but is not a blocker

`Co-Authored-By` and URLs have straightforward mechanical patterns. “session identifier” and “tool attribution” may or may not have exact syntax in the standing conventions or existing governance tooling.

The classification phase should inspect the actual rule wording and existing tool contract. If the forbidden vocabulary is not mechanically delimited, P6 should be PARTIAL rather than stretched into a full semantic detector.

The specification already authorises the classification to subtract or downgrade expected properties with a stated reason, so no amendment to the specification is required before execution.

## 10. Rule 18 supply requirement

This review identifies the task by its task name:

`mechanical enforcement for the governance rules that admit it`

It is intended to be supplied **as a file** under Rule 18 and committed byte-unchanged. No delimiter extraction is required or authorised.

## 11. Final assessment

The revised specification now embodies the principle the task is trying to enforce: machine-checkable facts, necessary-condition checks and human judgement are kept separate instead of being collapsed into one “green” category.

The remaining risks are implementation risks, not contradictions in the commissioning document. They are testable under A5 and reportable under A4/A10.

**Approval status: APPROVED FOR EXECUTION.**
