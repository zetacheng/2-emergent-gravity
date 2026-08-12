# Pre-execution review --- adopt-domain repair

**Review disposition: APPROVED FOR EXECUTION**

reviewed specification SHA-256:
`665ef240218bc6d0d7b3ae7dfe2d75e9d2ad104eccb25e166e05b13c904c3488`\
reviewed artifact SHA-256:
`c27e57f080ecf8a2472a7f614aedcc19c5c72622650f6ddd0bc802d3fced5003`

Reviewed specification: `SPEC adopt domain repair.md`\
Specification evidence base: `2e4cc6eb9ae8a34d7a5e81c86d82a5b631dabe7a`\
Intended branch: `science/adopt-parameter-domain-repair`\
Repository: `zetacheng/2-emergent-gravity`

## 1. Scope of review

I reviewed the supplied repair specification as a pre-execution
governance artifact. The supplied specification file hashes to
`665ef240218bc6d0d7b3ae7dfe2d75e9d2ad104eccb25e166e05b13c904c3488`. The
artifact under repair is
`derivations/P2-PHASE-01_microscopic_parameter_domain.md` at the stated
evidence base; the adoption report records its committed SHA-256 as
`c27e57f080ecf8a2472a7f614aedcc19c5c72622650f6ddd0bc802d3fced5003`.

This review authorises only the repair task described by the reviewed
specification. It does not authorise integration into `main`, a
gate-status change, a prerequisite-state change, a new admissibility
verdict, physics computation, or any repair outside the frozen manifest.

## 2. Finding on the two defects

**Defect A is real and material as documentation/governance wording.**
The adopted artifact was committed with an adopted status while
retaining neighbouring draft-era statements. The proposed three anchored
substitutions are appropriately narrow: they make the title,
operative-status paragraph, and supersession paragraph agree with the
adoption that already occurred. They do not alter the adopted
microscopic parameter decisions or any scientific result.

**Defect B is real.** The preceding adoption intentionally modified
`derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md`,
changing its bytes while leaving the registered-gate digest unchanged.
The prior execution report records the resulting mismatch. Leaving that
mismatch in an integrable branch would make the gate pin assert a false
byte correspondence.

The specification also correctly identifies the consequential second
pin: repairing Defect A changes the adopted parameter-domain artifact's
bytes, so its presently correct pin necessarily becomes stale unless it
is updated in the same corrective task.

## 3. Ruling interpretation

**I approve the specification's §1 interpretation.** The PI ruling is
not limited in principle to the one stale pin it names. Its operative
principle is general: a registered-gate artifact pin denotes the exact
operative bytes, and an authorised intentional modification must not
land with a knowingly stale digest. The ruling then specifically
requires a separately reviewed corrective task for the already-stale
admissibility-contract pin.

The parameter-domain pin is different only temporally: it is correct at
the evidence base and becomes stale because this reviewed corrective
task intentionally changes the pinned artifact. Applying the same
principle to that newly stale pin is necessary to preserve the
exact-byte invariant the ruling states. I therefore read the ruling as
authorising **both** re-pins specified in §4, provided the executor
performs exactly the three authorised wording substitutions first,
measures RE-PIN 1 from commit 3's committed blob, and changes no other
digest or `GATES.md` text.

On that reading, there is no unresolved governance ambiguity requiring a
STOP before execution.

## 4. Review of execution design

The five-commit ordering is sound. In particular, commit 3 must precede
commit 4 because the replacement SHA-256 for the parameter-domain
artifact does not exist until the repaired artifact is committed.
Measuring that digest from the committed blob rather than the working
tree is the correct evidence boundary.

The frozen scope is appropriately narrow: three additions and two
modifications. The two DRAFT files are protected from further editing.
`GATES.md` is limited to two digest-string substitutions. No gate
`Status:` line, prerequisite state, path, heading, or admissibility
verdict is authorised to change.

The specification's stop conditions are adequate for the literal
repairs: each OLD wording anchor must occur verbatim exactly once, and
each old 64-hex digest must occur exactly once before substitution. A
mismatch is a STOP rather than authority to search for or infer a
replacement location.

A6 is particularly important and should be treated as independent
evidence rather than validator evidence. The task requires every SHA-256
pin in `GATES.md` to be enumerated and checked against its target at the
final head. This directly addresses the failure mode that survived the
preceding validator suite.

## 5. Checker and validator interpretation

The specification correctly refuses to treat `P7` as gate-integrity
evidence. At this evidence base its gate-heading expression matches none
of the fourteen real gate headings, so a `PASS` is vacuous. For this
task, compliance of the `GATES.md` edit rests on the exact
base-to-commit-4 diff required by A5 and the explicit pin verification
required by A6.

RUN 2 remains stop-governing exactly as specified. The executor is not
authorised to narrow the subject set, replace `append_only_paths` with
an empty set, drop a property, or otherwise alter the supplied checker
configuration to obtain a pass.

Validator success likewise does not establish pin correctness. A
validator suite that previously passed while a gate pin was stale cannot
substitute for A6's direct byte-correspondence check.

## 6. Rule 16 assessment

The specification identifies the correct junction. If this repair
succeeds, a reader will encounter two matching gate pins and may infer
that repository machinery keeps such pins synchronized. **It does not.**
The correspondence will be correct because this task explicitly checks
it by hand. No persistent validator described by the evidence
automatically compares every `GATES.md` digest with the bytes of its
referenced artifact.

Accordingly, this task establishes that the pins match at its measured
head; it does **not** establish a continuing invariant for later tasks.
A check performed once by an executor is not a check that runs. Any
future task modifying a hash-pinned artifact must again remember to
authorise, perform, and verify the corresponding re-pin unless
repository automation is added separately.

## 7. What this review does not establish

This review does not establish that `P2-PHASE-01` is ready to run or
pass. It does not change `P2-PHASE-01` from `PROPOSED`; it does not
change the PHASE INPUT / ADMISSIBILITY CONTRACT prerequisite from
`UNSATISFIED`; and it does not revisit the scientific content adopted by
the preceding task.

It does not answer `C1`, `C2`, or `C3`, certify root completeness,
establish full-space stability or thermodynamic dominance, exclude
negative `G`, establish finite-density coverage, or certify any phase.

It also does not authorise integration. The purpose of this task is to
make the adoption branch internally consistent enough to be considered
by a separate integration task.

## 8. Stops and clarifications

**SPECIFICATION_DEFECT:** none identified that prevents execution.

**ENVIRONMENT:** none identified in pre-execution review. If an
environment failure occurs, the executor remains bound by the
repository's Rule 13 discipline. If none occurs, neither of the two
known diagnostic orders should be claimed as exercised.

**OBSERVATION_METHOD_ERROR:** none identified in the specification's
prescribed methods. Exact anchors, committed-blob measurement, full-file
pin enumeration, and path-by-path protected-path comparison are
appropriate.

**REPOSITORY_DEFECT:** the known vacuous `P7` remains a repository
defect and must not be represented as gate-integrity evidence. The
absence of an automated gate-pin-to-target digest validator is also a
continuing repository weakness; this task compensates for it only once
through A6.

**UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY:** none requiring a
pre-execution STOP. I specifically approve the reading that the PI
ruling's exact-operative-bytes principle covers the second re-pin
created by this repair task.

## 9. Final disposition

**APPROVED FOR EXECUTION**, against specification SHA-256
`665ef240218bc6d0d7b3ae7dfe2d75e9d2ad104eccb25e166e05b13c904c3488` and
reviewed artifact SHA-256
`c27e57f080ecf8a2472a7f614aedcc19c5c72622650f6ddd0bc802d3fced5003`.

Approval is conditional on exact execution of the reviewed
specification, including all STOP conditions, the frozen five-commit
layering, the two and only two `GATES.md` digest substitutions, complete
A6 pin verification, and preservation of all stated gate invariants.

The repaired adopted artifact should read as an adopted document from
its first line. That wording repair is documentary consistency, not a
new adoption decision and not evidence that a phase has been found.
