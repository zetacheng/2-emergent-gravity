# Pre-execution review — adopt the microscopic parameter domain, with evidence corrections

**Review disposition: APPROVED FOR EXECUTION**

**Task reviewed:** `adopt the microscopic parameter domain, with evidence corrections`  
**Specification evidence base:** `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`  
**Reviewed source artifact SHA-256:** `096220d188bcb9db2a2428dba7938c625215fec09b4ed46c879795cdeb13efba`

This review identifies the task by task name and identifies the source artifact being adopted by digest. The digest above is part of this review's correspondence statement and MUST be checked before execution. A supplied source artifact with any other digest is not the artifact reviewed here.

## 1. Disposition

The specification is internally coherent enough to execute as written.

The substantive adoption decisions are sufficiently separated from the evidence corrections. The task does not ask the executor to make a scientific judgement, to answer C1/C2/C3, or to infer an unrecorded governance decision. The PI rulings in §3a supply the authority needed for the otherwise non-binary treatment of the lattice scale `a`.

I therefore approve execution subject to the specification's own STOP conditions.

## 2. The microscopic-domain ruling is adequate

The earlier ambiguity in the prerequisite has been resolved.

The gate wording asks for a disposition of cutoff ratios and finite-density `mu`. The specification now records two PI rulings:

1. `"Not operative at this gate"` is an admissible third disposition for a quantity that neither enters the dimensionless computation as a fixed numerical input nor defines a scan coordinate.
2. For the quantities presently identified at this gate, no independent cutoff ratio requires disposition beyond the lattice-scale quantity `a`; `Lambda ≡ 1` and `a ≡ 1` are unit conventions rather than assignments of a physical cutoff scale.

Together these rulings are sufficient authority for the proposed `GATES.md` prerequisite state `SATISFIED`.

The expiry clause is essential and correctly preserved: if a gate quantity later acquires physical dependence on `a`, or if another independent cutoff ratio is identified, the present disposition no longer exhausts the prerequisite and a new explicit disposition is required before affected results may serve as gate evidence.

This approval does **not** determine that the original gate wording naturally implied this third disposition. It approves the PI's explicit ruling as the governance authority that resolves the ambiguity.

## 3. Scientific meaning remains properly bounded

The adopted artifact fixes an enumeration domain; it does not establish a phase.

The following distinctions are correctly preserved and MUST remain visible in execution and reporting:

- `G/Gc in [0.80, 3.00]` is an adopted positive-coupling enumeration window, not a physical proof of the full microscopic domain.
- `mu = 0` is a fixed input for this enumeration, not a resolution of finite-density coverage.
- the negative-mass/complement branch is included as a candidate for enumeration, not certified as physically admissible, locally stable in full condensate space, or thermodynamically selected;
- `Mhat = 1` is not adopted as an admissibility bound;
- lattice spacing `a` is not assigned a physical scale;
- no claim of root completeness is made;
- no claim of full-space stability or common-normalisation free-energy dominance is made.

The boundary statement required by §5 is therefore appropriate and should remain in the adopted artifact itself, not merely in the execution report.

## 4. The evidence corrections are legitimate adoption-time corrections

The five corrections in §4 are narrow, specified by exact OLD/NEW text, and do not change the substantive PI decisions.

I find the corrections appropriate:

- **C-1** repairs an over-broad numerical scope claim and records already-existing negative-mass samples without converting partial evidence into a global sign claim.
- **C-2** and **C-3** add the missing grid qualification to quoted finite-grid values.
- **C-4** removes a branch-label reading hazard and explicitly distinguishes the sub-critical near-origin negative root from the positive-mass condensate branch.
- **C-5** restores the omitted `OPEN-AC-4` and reconciles `OPEN-AC-5` with the already-adopted answer to the same `Mhat = 1` question.

These are evidence-precision, bookkeeping, and interpretive corrections. None requires the executor to choose among scientific alternatives.

The specification's eight-operation accounting is arithmetically consistent:

- C-1: 1
- C-2: 1
- C-3: 1
- C-4: 2
- C-5: 1
- §5 boundary insertion: 1
- status-header replacement: 1

Total: **8 edit operations on 8 anchored strings or insertion points**.

A mismatch in that count is correctly specified as a STOP rather than something the executor may reconcile.

## 5. `OPEN-AC-2` and `OPEN-AC-5`

The A7 cross-reference is materially better than rewriting the historic admissibility-contract entries.

`OPEN-AC-2` is correctly labelled **RESOLVED FOR ENUMERATION**, not `CLOSED`. The PI ruling determines that the negative-mass branch may appear as a candidate in enumeration; it does not determine that the branch is physical, admissible, or stable.

`OPEN-AC-5` can properly be marked **CLOSED** by cross-reference because it is the same `Mhat = 1` admissibility-bound question answered by `OPEN-PD-1`.

The original contract text remaining untouched is important. The inserted paragraph records a later authoritative consequence without falsifying the historical state of the draft.

## 6. `GATES.md` change

I approve the specified prerequisite transition:

`MICROSCOPIC PARAMETER DOMAIN: UNSATISFIED -> SATISFIED`

provided all of A6 is satisfied literally.

This approval does **not** approve any change to the gate's `Status:` line. `P2-PHASE-01` must remain `PROPOSED`.

The second prerequisite, `PHASE INPUT / ADMISSIBILITY CONTRACT`, must remain `UNSATISFIED`.

Accordingly, the resulting repository state must not be described as the gate being ready, passed, open for verdict, or scientifically satisfied. Only one prerequisite is being adopted.

## 7. P7 is known-vacuous and supplies no evidence

The specification correctly records that the landed checker's `GATE_HEADING` expression matches zero of the fourteen real `P2-` headings.

Therefore a P7 `PASS` in A9 is **not evidence that gate integrity was checked**. It is a vacuous pass over two empty maps.

The executor should still run the required checker exactly as specified, because the task requires the complete tool output and other properties remain informative. But the report must not use P7 to support the claim that the A6 edit stayed confined to the authorised gate block. That claim must instead rest on the direct A5/A6/A10 diff and blob/path measurements required by the specification.

A vacuous green result is especially dangerous here because the task really does modify `GATES.md`.

## 8. C1, C2 and C3 remain outside this task

The specification correctly prohibits answering C1, C2 or C3.

In particular:

- do not inspect the exploratory script to decide whether the complement root is constructed or independently recovered;
- do not turn the existing positive `I0` samples into a proof of global non-negativity;
- do not interpret the curvature asymmetry as physical or coordinate-induced.

Those are follow-up scientific checks. Their existence does not block adoption of the enumeration domain because the adopted artifact explicitly records the corresponding limits.

## 9. Rule 16 assessment

Two inference junctions require explicit handling in the report.

First, a reader may encounter `Prerequisite state: SATISFIED` and infer that `P2-PHASE-01` itself is ready. That inference is false. The gate remains `PROPOSED`, the admissibility-contract prerequisite remains `UNSATISFIED`, and the adopted domain certifies only where and with what fixed inputs the scalar enumeration may be performed.

Second, the checker may print `P7: PASS`. A reader may infer that machine gate-integrity enforcement succeeded. That inference is also false because the current heading parser matches no real gate section.

The report should state both limits adjacent to the corresponding positive-looking result.

## 10. Review of scope and evidence layering

The frozen scope is internally consistent:

- **4 additions**
- **3 modifications**
- **7 total paths**

The commit order is coherent. In particular, committing the adopted artifact before the `GATES.md` update is necessary because A6 embeds the committed artifact's measured digest.

The report-layering rule is also coherent: commit 5 cannot be measured by the report that becomes commit 5, so final-scope, final-checker, final-message, push, and remote-tip evidence correctly remain post-report evidence.

No additional commit is authorised or necessary.

## 11. Minor observation, non-blocking

The phrase in §3 that a gate requirement is "arguably not met" describes the pre-ruling ambiguity. After §3a it is no longer unresolved. The surrounding text makes that chronology sufficiently clear, so I do not require a wording change.

Similarly, the new `GATES.md` text still describes `a` as a "third answer to this gate's binary question." That wording is useful rather than problematic because it prevents the PI ruling from being mistaken for an interpretation that was already present in the gate text.

## 12. Execution conditions

Execution is approved only if all of the following remain true:

- authoritative `main` is exactly `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`;
- the supplied source artifact SHA-256 is exactly `096220d188bcb9db2a2428dba7938c625215fec09b4ed46c879795cdeb13efba`;
- this review arrives as a file and is committed byte-unchanged;
- all exact OLD anchors required by §4 are found verbatim;
- A4 produces exactly eight authorised edit operations;
- no unlisted diff hunk appears in the adopted artifact;
- `P2-PHASE-01` remains `PROPOSED`;
- the admissibility-contract prerequisite remains `UNSATISFIED`;
- C1, C2 and C3 are not answered;
- no path outside the frozen manifest is changed;
- `main` is not moved.

Any contrary condition is governed by the specification's STOP clauses.

## 13. Final disposition

**APPROVED FOR EXECUTION.**

The task may adopt the microscopic parameter domain with the exact evidence corrections, PI rulings, pointer insertions, gate-prerequisite update, and boundary statement specified.

This approval establishes only that the adoption task is sufficiently specified and that the recorded PI rulings provide authority for the prerequisite transition. It does **not** establish that an admissible phase exists, that the phase gate is satisfied, that negative `G` is excluded, that the root enumeration is complete, or that the checker mechanically validates gate integrity.

**Reviewed source artifact SHA-256:** `096220d188bcb9db2a2428dba7938c625215fec09b4ed46c879795cdeb13efba`
