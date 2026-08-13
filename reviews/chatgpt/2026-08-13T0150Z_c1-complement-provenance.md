# Pre-execution review — C1 complement-root provenance

**Review status: APPROVED FOR EXECUTION.**

**Reviewed specification SHA-256:** `5669c174fb6b489a9d311bb3df0c116cb9f6e9900b420d900613bb43dea24176`

**Reviewed task:** `C1: is the complement root recovered or constructed?`

**Evidence base named by the specification:** `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`

## 1. Scope and disposition

The specification is executable as written. It is materially better than the earlier form because it now separates two questions that must not be conflated:

- **ROOT PROVENANCE** — whether the production root table independently searches for both roots or constructs one from the other.
- **EXACTNESS PROVENANCE** — why the independently returned pair satisfies `|Mhat_ord + Mhat_comp + 8| = 0.00e+00` exactly in the stored results.

That separation is necessary. `RECOVERED` answers the first question only. It does **not** by itself make the exact floating-point mirroring evidentially meaningful, and it does not make the complement position algebraically independent.

The specification also correctly discloses that pre-registration is compromised: this Reviewer read the pinned script while reviewing an earlier version and stated a code-provenance prediction. The revised task does not pretend otherwise. It converts those prior statements into explicit, falsifiable claims R1–R5 and requires the executor to disclose whether its reading was independent, anchored-then-agreed, or inseparable from the review.

## 2. Reviewer's anchored code-reading claims

Against the script identified in the specification at SHA-256
`3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0`,
my code-reading predictions are:

**R1 — CONFIRMED as a review prediction.** `algebraic_roots()` invokes `bisect_root()` separately on the two brackets `(-12.0, -4.0)` and `(-4.0, 4.0)`.

**R2 — CONFIRMED as a review prediction.** `bisect_root()` obtains its root by repeated evaluation of `divided_gap()` and does not compute a production root as `-8.0 - mhat`.

**R3 — CONFIRMED as a review prediction.** `grid_result()` passes each root returned by `algebraic_roots()` directly to `root_record()` for storage; it does not replace the pair by a complement-constructed pair.

**R4 — CONFIRMED as a review prediction.** `symmetry_check()` separately constructs the diagnostic value `-8.0 - mhat` and compares the two bubble evaluations. Thus `symmetry.complement_pairs` is a constructed **check of the symmetry relation**, not the mechanism used to populate the production root table.

**R5 — prediction: ROOT PROVENANCE = `RECOVERED`.** The production table therefore appears to contain roots recovered by separate bracketed searches rather than one root constructed from the other.

These are review anchors, not substitutes for A3. The executor must verify each claim against the pinned bytes and report `CONFIRMED`, `REFUTED`, or `CANNOT DETERMINE` per claim.

## 3. Exactness remains genuinely open to the executor

The review does **not** settle EXACTNESS PROVENANCE.

The two production brackets are reflections of one another under `m -> -8-m`, and the underlying Wilson-complement relation is exact. That makes `SEARCH-STRUCTURE-INDUCED` a plausible outcome. But static inspection must still establish why the implementation produces **bit-exact** mirrored roots ninety times, rather than merely roots agreeing within the bisection resolution.

The specification is right to require a separate exactness verdict and to allow `INCONCLUSIVE` if the static code does not determine the mechanism. It is also right to STOP if the mechanism is genuinely `NOT-STRUCTURE-INDUCED`, because that branch has no pre-registered consequence and a consequence written after seeing the evidence would defeat the purpose of the registration.

## 4. Consequence discipline

The revised `RECOVERED` consequence is scientifically appropriate.

Independent numerical recovery validates the solver's realised symmetry and establishes that the production complement root was not merely copied from the ordinary root. It **does not** establish independent positional physics, because under the exact relation the complement position remains algebraically determined by the ordinary position.

Likewise, if exactness is `SEARCH-STRUCTURE-INDUCED`, the exact zero residual must not be presented as independent numerical agreement. If exactness is `INCONCLUSIVE`, the artifact must say what static reading cannot establish and stop without running a new computation.

The consequence paragraphs should therefore be copied exactly as required by A4.

## 5. Rule 16 / scientific boundary

C1 changes the **weight and provenance of existing evidence**. It adds no new physics result.

A `RECOVERED` production root does not establish that the complement branch is a physical phase. Full condensate-space stability and admissibility remain absent, and the open common-normalisation issue still blocks a thermodynamic depth comparison. Conversely, a `CONSTRUCTED` verdict would not prove the branch unphysical; it would only remove numerical evidential weight from the stored position.

The junction to guard is therefore:

**numerical provenance -> physical interpretation**

The first does not imply the second.

## 6. Non-blocking observation

Section 0 retains the historical label `GRID-INDUCED` in its motivating three-way description, while the governing verdict vocabulary in §2 correctly uses the broader `SEARCH-STRUCTURE-INDUCED`.

I do **not** treat this as an execution ambiguity because §2 explicitly defines the operative verdict set and A3 repeats it. The executor should use the §2 vocabulary. This is a wording observation only and does not require the specification to be changed before execution.

## 7. Review conclusion

**APPROVED FOR EXECUTION.**

The specification now has a coherent two-axis verdict structure, pre-registered consequences for every non-stop outcome, an explicit treatment of the compromised review independence, and a correct separation between:

1. how the production roots were obtained;
2. why their stored positions mirror exactly; and
3. what either fact does or does not establish physically.

No change to the specification is required before execution.
