# Review — POLE-B0 Milestone Scope Specification

**Reviewed artifact:** `SPEC pole b0 milestone scope(1).md`  
**Reviewed specification SHA-256:** `d69d0d4d04feec8d164ba67c75a8a341fee545c652f56991ff85bb7c4d076df7`  
**Review date:** 2026-08-19  
**Review verdict:** `APPROVE FOR EXECUTION`

## 1. Scientific question — PASS

The specification asks a properly scoped question: whether the programme presently contains enough frozen structure to formulate and eventually test the manuscript's proposed spin-channel pole milestone.

It does **not** ask this scope task to establish that a massless spin-2 pole exists.

The distinction is essential:

`induced Einstein-Hilbert / heat-kernel coefficient`

is not equivalent to

`a genuine massless spin-2 pole in the interacting stress-tensor correlator`.

Accordingly, success of the βV reconstruction line would not by itself establish the POLE milestone.

## 2. Milestone definition — PASS

The milestone is correctly tied to the manuscript's own proposed observable: a Barnes-Rivers-projected stress-tensor correlator with a spin-2 massless pole and vanishing spin-1/0 residues.

The task is therefore aimed at a falsifiable dynamical observable rather than merely another coefficient-level consistency check.

## 3. Scope discipline — PASS

The specification is a scope/tractability assessment.

It does not authorize the executor to:

- compute the stress-tensor correlator;
- estimate a pole location or residue;
- choose numerical tolerances;
- choose finite-volume or mass extrapolation thresholds;
- infer that the pole exists;
- rank this task against other programme tasks.

This separation is appropriate.

## 4. A11 clarification — RESOLVED / PASS

The previous ambiguity around `any computed quantity` has been repaired.

A11 now targets a:

`NEWLY COMPUTED OR ESTIMATED SCIENTIFIC QUANTITY BELONGING TO THIS MILESTONE`

including milestone outputs such as the stress-tensor correlator, projected correlator, Π^(2)(p), pole position, spin-0/1 residues, or numerical estimates/bounds on those quantities.

The specification separately excludes repository/governance measurements required to execute and audit the task, such as path counts, hit counts, SHAs, blob IDs, checker output, test counts, and environment versions.

A11 therefore no longer conflicts with the acceptance criteria that require such measurements.

The separate prohibition on statements that one task should precede another also correctly enforces `scope, don't rank`.

## 5. SRC-B0 boundary — PASS

The specification correctly refuses to infer that the POLE observable is unavailable merely because SRC-B0 found the source-side configuration absent.

A source configuration for a force calculation and a vacuum/ensemble stress-tensor two-point function are different objects.

Whether the latter is constructible must be assessed directly from the repository's definitions and frozen microscopic structure.

## 6. Microscopic-state / measure dependence — PASS

The specification appropriately leaves open whether R4 or another microscopic ruling is required to define the expectation value underlying ⟨TT⟩.

This is exactly the kind of dependency POLE-B0 should determine from evidence rather than assume in advance.

A finding of dependence, independence, or insufficient evidence must therefore be justified by the repository's actual definitions.

## 7. Projector and channel structure — PASS

The task correctly requires assessment of the ingredients needed to distinguish the spin-2 pole from spin-1/0 contamination.

This is consistent with CHANNEL-B0's landed result that the manuscript itself treats these as separate channels and proposes vanishing spin-1/0 residues as part of the decisive test.

The scope task must not convert that proposed criterion into an already-established numerical result.

## 8. Vanishing-residue criterion — PASS

The specification correctly recognises that `vanishing` is not operationally meaningful on a finite lattice without a frozen discrimination rule.

A future executable milestone may require, among other things, a tolerance or scaling criterion, finite-volume behaviour, mass dependence, momentum-window rules, and a way to distinguish lattice artefacts from genuine non-spin-2 residues.

POLE-B0 should identify which such items require freezing but must not choose their numerical values in this scope task.

## 9. Falsifiability — PASS

The proposed milestone is scientifically useful because it can fail.

A clean spin-2 pole with the required channel structure would support the manuscript's dynamical graviton claim.

A missing pole, a displaced/non-massless pole, persistent spin-0/1 residues, or an inability to define the observable from the frozen microscopic theory would each constitute materially different outcomes.

The scope assessment should preserve these distinctions.

## 10. Relationship to existing βV work — PASS

The specification correctly prevents coefficient-level reconstruction from being treated as a substitute for the pole test.

The βV/heat-kernel line and the POLE line test different layers:

`local curvature coefficient / induced-action consistency`

versus

`interacting correlator / propagating-state content`.

Agreement in the first does not logically guarantee success in the second.

## 11. Epistemic classification — PASS

The executor should report only what the repository establishes about tractability and dependencies.

In particular:

- absence of a keyword is not evidence that a structure is absent;
- an open microscopic ruling is not automatically a blocker unless the observable actually depends on it;
- a proposed observable is not a computed observable;
- a tractable milestone is not an established pole;
- identifying missing prerequisites does not establish their physical values.

The specification maintains these boundaries.

## 12. Governance and execution discipline — PASS

The task retains the repository's established audit structure: bind the review to exact specification bytes, verify refs and evidence base, measure scope, preserve append-only restrictions, run the required checker/validator suite, and distinguish report-head measurements from post-report evidence.

No scientific computation is authorized merely because the supporting numerical machinery exists.

## 13. Remaining specification defects

None found at STOP level.

The only material issue identified in the previous review — A11's overly broad `computed quantity` language — is resolved in this revision.

## Final verdict

**`APPROVE FOR EXECUTION`**

POLE-B0 may proceed as a scope/tractability assessment.

This approval is bound exclusively to the exact uploaded specification bytes with SHA-256:

`d69d0d4d04feec8d164ba67c75a8a341fee545c652f56991ff85bb7c4d076df7`

The central boundary to preserve during execution is:

**POLE-B0 may determine whether the decisive spin-2 pole test is presently well-defined and executable; it must not perform that test, estimate its result, or convert tractability into evidence that the pole exists.**
