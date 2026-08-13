# Pre-execution review — adopted domain operative-label repair and sweep

**Disposition: APPROVED FOR EXECUTION.**

reviewed specification SHA-256: `d358a9d9f021291eef380f65373686060d1e10473b9d0e29134038d545109ee7`

Reviewed specification:
`Task specification — repair the adopted domain's operative status label, and sweep the rest`

Evidence base named by the specification:
`cd1ebd84ca588a8ec946fc89e692f9e34760713d`

Target branch:
`science/adopt-parameter-domain-labels`

This review approves the specification identified by the SHA-256 above. It does not approve a different transcription, later revision, or substituted file.

---

## 1. Review conclusion

The task is appropriately classified **MATERIAL**.

The defect is real and material to interpretation. The adopted artifact defines `RECOMMENDATION` as non-binding, while the operative domain section still begins with `RECOMMENDATION, for PI adoption`. That leaves the artifact internally inconsistent: its title and status say ADOPTED, while the label attached to the adopted domain itself says the content binds nobody.

The proposed replacement is appropriately narrow. It changes the stale operative label without changing the coordinate, coupling range, scan grid, treatment of `mu`, treatment of `a`, any PI ruling, any measured result, or any open-item disposition.

**APPROVED.**

## 2. Gate-pin consequence

The specification correctly treats the pin update as a necessary consequence of the authorised artifact edit.

At the evidence base, `GATES.md` pins the currently operative bytes of
`derivations/P2-PHASE-01_microscopic_parameter_domain.md`. Once the artifact is changed, leaving that digest unchanged would create a known false correspondence.

The prior PI ruling that a gate pin denotes the exact operative bytes is sufficient authority for this re-pin. Applying that principle to an artifact modified by this task is an instance of the ruling, not a new governance decision.

The contract-draft pin must remain untouched because its target is not modified by this task.

**APPROVED.**

## 3. Scope and confinement

The frozen scope is coherent:

- three additions: specification, review, report;
- two modifications: the adopted microscopic-parameter-domain artifact and `GATES.md`;
- no other path is authorised.

The specification explicitly prohibits changes to either DRAFT, gate status, prerequisite states, headings, paths, other digest strings, science results, scripts, tests, and `main`.

The required `--unified=0` diffs are the correct evidence for confinement. In particular, P7 must not be relied upon because its gate-heading parser is already known to match zero real gate sections.

**APPROVED.**

## 4. The sweep is necessary

A5 is the strongest part of this task.

Two previous corrective tasks repaired only specifically reported anchors. That approach left a further stale label because it established local correctness, not whole-artifact consistency.

The whole-file census changes the evidence type: every labelled statement is enumerated and classified CURRENT or STALE, including the labels that are already correct.

The counting rule is sufficiently explicit: the four-line vocabulary definition is one labelled-statement entry, while the raw grep line count is separately reported. If the executor measures a different census, the specification requires reporting the discrepancy rather than forcing it to fourteen.

If another stale label is found, the executor must report it and leave it untouched. That preserves the frozen scope.

**APPROVED.**

## 5. A4 wording repair

The proposed replacement for:

`**RECOMMENDATION, for PI adoption.**`

is acceptable. It makes the operative status explicit and records why the stale label existed.

The replacement does not itself add a scientific conclusion. It records that the domain was already adopted by the PI and is already operative.

The wording `it binds` should be read narrowly: the adopted domain and its adopted input treatment bind this gate's governed enumeration. It does **not** mean that the artifact establishes phase admissibility, root completeness, thermodynamic dominance, finite-density coverage, or any result that the artifact expressly leaves open.

That interpretation should be preserved in the execution report.

## 6. A6 pin sweep

The requirement to enumerate every SHA-256 pin in `GATES.md`, assert that at least one pin exists, resolve its target, and compare the measured target digest is sound.

This avoids the vacuous-success failure mode already observed elsewhere in the checker.

The expected count of two is a prediction, not authority. The measured count governs. Any mismatch must be reported.

## 7. Rule 16 assessment

The specification's proposed Rule 16 assessment is correct.

After this task, a reader could infer that label consistency and gate-pin correspondence are maintained automatically. They are not.

This task establishes only that:

1. the adopted artifact was swept once for the defined kind labels; and
2. all gate pins were compared with their targets once at this head.

Neither property is enforced by a validator or workflow. A one-time human sweep is evidence about one repository state, not a continuing invariant.

That limitation should appear prominently in the report.

## 8. Stop conditions

The stop conditions are appropriately strict.

Execution must stop if, among other stated conditions:

- either required ref does not match;
- the supplied review does not name this specification digest;
- the pre-edit artifact digest is not the pinned `a481955b...` value;
- the stale label anchor is not found exactly once;
- the old gate-pin digest is not found exactly once;
- RUN 2 reports any failure;
- a forbidden path changes;
- the gate diff touches anything beyond the single authorised digest string.

No pre-authorised exception is needed.

## 9. Reviewer findings

No blocking contradiction was found in the specification.

One interpretive caution should be carried into the report: after replacing the stale label, the phrase `ADOPTED ... and it binds` must not be allowed to expand into a claim that the domain artifact proves a phase exists or satisfies the gate. The artifact fixes the operative enumeration domain; `P2-PHASE-01` remains governed by its other prerequisite and its scientific acceptance conditions.

No change to the specification is required for this caution.

## 10. Review disposition

**APPROVED FOR EXECUTION.**

This approval is for the exact specification whose SHA-256 is:

`d358a9d9f021291eef380f65373686060d1e10473b9d0e29134038d545109ee7`

The review expects the executor to preserve the specification's frozen scope, perform the complete A5 census, re-pin only the authorised domain-artifact digest, treat P7 as evidentially vacuous, and stop on any stop-governing failure.

This review does not authorise integration or movement of `main`.
