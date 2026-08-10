Pre-execution review — diquark channel character carrying both η signs

Reviewer: ChatGPT
Disposition: APPROVE

Review scope

This review covers the task specification “diquark channel character, carrying both η signs”, with specification evidence base:

8701a97a6bb58550d4300f75c10638b057335731

The review assesses the specification for internal consistency, authority and provenance handling, conditional acceptance logic, interaction with Rules 1–17, and whether the task can be executed without requiring the Executor to invent an unfrozen convention.

This is a review of the specification. It is not an independent execution of the proposed physics derivation.

What I verified

I verified that the specification now treats the three unresolved particle–particle definitions distinctly:

* η is governed by the 2026-08-09 PI ruling and both exposed sign representatives are to be carried.
* particle–particle Grassmann ordering remains unfrozen.
* diquark operator normalisation remains unfrozen.

The specification does not silently freeze either of the latter two.

I verified that Step 3 no longer assumes that the tested particle–particle ordering alternatives exhaust the admissible convention space. It explicitly permits testing alternatives that can be defined while prohibiting the Executor from promoting those alternatives into a complete enumeration of the convention space.

I verified that the treatment of diquark normalisation separates:

* positive real rescaling, which may change coefficient magnitude without changing channel character;
* sign or phase conventions, which may affect sign and therefore channel character;
* complex normalisation, for which a simple attractive/repulsive classification may cease to be applicable.

This prevents a magnitude ambiguity from being incorrectly promoted to a sign ambiguity.

I verified that the specification has a coherent conditional outcome structure.

If Step 3 produces well-defined coefficient sets, A4, A5 and A6 require the coefficients, channel characters and the same/opposite diagnostic.

If the result depends on an explicit assumption, the result must remain conditional and the tested alternatives must be reported without claiming they exhaust the convention space.

If the computation cannot proceed without supplying an unauthorised convention, UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY is an explicitly valid result and no same/opposite verdict is required.

The report contract now follows the same branching structure. It does not require coefficient sets or a same/opposite verdict when the scientifically correct result is that those quantities are not defined.

I verified that A9 follows the same structural branching. Tests are always required for quantities necessarily reached by the derivation: the particle–hole control, the defining relation for C, and residual-scalar cancellation. The relation between the η = +1 and η = −1 coefficient sets is required only if those sets are actually defined. If the derivation stops earlier at the authorised unresolved outcome, the test obligation changes to verification of the demonstrated obstruction.

This removes the earlier contradiction in which a correct unresolved result could still fail acceptance because a test was required for a quantity that did not exist.

I verified that A8 now defines its forbidden-conclusion scan sufficiently precisely for execution: it is a character-exact, case-insensitive substring search over each authored file’s raw UTF-8 text, without normalisation and without matches spanning file boundaries. Hits are not required to be driven to zero and disclaimers remain permissible.

I verified the required ordering of governing artifacts and research artifacts:

* specification first;
* pre-execution review second;
* derivation note before production code;
* script, results artifact and test file in the subsequent work commit;
* report after the work whose evidence it records.

This is consistent with Rule 15 and AGENTS.md research rule 3 as represented in the specification.

I verified that the task remains branch-only, preserves P2-PHASE-01 as PROPOSED, does not authorise modification of frozen or pinned inputs, and does not authorise the Executor to select η, particle–particle ordering, or diquark normalisation.

I also verified that the specification explicitly prevents channel-character results from being promoted into claims about a composite-vector pole, existence or absence of a bound state, completeness of the channel picture, or a new Hubbard–Stratonovich selection.

Minor non-blocking observations

Step 5 still begins with the unconditional wording:

“State whether the two η representatives give the same channel character or opposite ones.”

A6 and the report contract clearly control the actual acceptance semantics and explicitly state that no same/opposite verdict is required under the unresolved outcome. I therefore do not consider this a contradiction. For maximum structural consistency, a future wording revision could begin Step 5 with:

“Where Step 3 makes the comparison well-defined, state whether …”

This is not required before execution.

A8 asks that every forbidden-string hit be reported “with its sentence”. A prose sentence is not naturally defined for JSON, Python or test code. “Containing line or prose sentence, as applicable” would be mechanically sharper. The present wording remains executable and is not a blocker.

What I could not independently verify

I did not independently execute the repository checks recorded in §8.

In particular, I did not independently verify from repository objects in this review that:

* DECISION_LOG.md at 8701a97a… contains the cited η ruling;
* the three required normalised phrases reproduce there;
* the five A1 SHA-256 pins match their repository objects;
* derivations/P2-PHASE-01_channel_character.md contains the stated blocker structure;
* the source branch can be created from the stated evidence base without repository-state conflict;
* the proposed validators or lint command pass.

The specification explicitly requires the Executor to perform these checks before relying on them, and makes mismatches STOP conditions. My approval therefore does not substitute for A1, A2, A2a, A12, A13 or A14.

I also did not verify the resulting particle–particle algebra, coefficient values, channel characters, or whether the final scientifically supported outcome will be a same/opposite verdict, an assumption-dependent result, or UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY. Determining that is the work authorised by this task.

Disposition

APPROVE.

The specification is internally executable and no longer requires the Executor to manufacture a result when the remaining unfrozen conventions prevent one.

The most important structural issue from the earlier drafts is resolved: the derivation, acceptance criteria, tests and report contract now all permit the same three outcome classes and impose obligations only on quantities the derivation actually reaches.

No blocking specification defect was identified in this review.
