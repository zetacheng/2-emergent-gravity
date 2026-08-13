# Task specification — C3: is the curvature asymmetry physical or coordinate-induced?

Specification evidence base: `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`

    Branch to create   science/c3-curvature-asymmetry
    Cut from           authoritative main @ 1cb5550f…

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18.

**This task reads and derives. It modifies nothing that already exists**,
runs no script, and touches no pinned artifact. **Its output is two new
files.**

**It is independent of the adoption line and of `C1`'s branch.** Neither
is merged or required. **`C1`'s findings are referenced by their content,
which is already established, not by their branch.**

---

> ## THE AUTHOR DERIVED THE ANSWER BEFORE WRITING THIS
>
> **Blind pre-registration is not available and this section says so
> rather than pretending otherwise**, exactly as `C1`'s specification did
> once its reviewer had read the script.
>
> **The author derived a closed form for the curvature ratio and verified
> it against all ninety pairs.** §2 states it as a falsifiable
> prediction with its worst deviation. **The executor's task is to derive
> it independently, then check it, then rule on what it means.**
>
> **The executor must report whether the derivation was reached
> independently, reached after reading §2, or cannot be separated from
> it.** **All three are acceptable. Silence is not.**
>
> **A prediction stated with its numbers, in advance, and checkable
> against ninety cases is stronger evidence than an unanchored judgement
> — provided the anchor is declared.**

## 0. The question

**`C3` was commissioned by the adopted parameter-domain artifact:**
*is the curvature asymmetry physical, or induced by the chosen coordinate
or the second-derivative definition?*

**The observation.** For each coupling, the two non-trivial roots carry
very different restricted curvatures. Measured on grid `n = 48`,
`shift 0.0`:

    G/Gc    near-origin root    complement root      ratio
    0.80        -0.02259             0.41782        -18.5
    0.99        -0.00086             0.41127       -477.9
    1.20         0.01267             0.36149         28.5
    3.00         0.02315             0.10475          4.5

**Why it mattered.** **`C1` established that the production roots are
separately recovered rather than constructed**, and that the stored pairs
satisfy the Wilson-complement positional relation `m2 = -8 - m1` exactly.
**The mechanism responsible for their bit-exact floating-point mirroring
remains OPEN under `OPEN-CC-3`.**

**`C3` does not depend on that mechanism.** What `C3` needs is the
positional relation between the stored roots and the Wilson identity —
both established — **and nothing about why the last bit agrees.** **The
weaker statement is the one used here, deliberately.**

**The complement root's position carries no independent information**:
it is fixed by the identity. **The curvature asymmetry was the branch's
last candidate for independent content.**

**The four ordinary explanations the adopted artifact requires be
excluded before any physical reading:** whether the curvature definition
is covariant at the two points; whether the second derivative carries a
mass-dependent Jacobian or measure contribution differing between them;
whether the parameterisation in `Mhat` makes the second derivative
non-invariant under `m -> -8-m` by construction; and whether the
potential is symmetric while the derivative with respect to the chosen
coordinate picks up sign or coordinate effects.

## 1. What is read

    scripts/p2_phase01_scalar_exploratory.py
    sha256  3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0

    results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json

**Verify the script digest against the results file's `script_sha256`
field before reading. If they differ, STOP.**

**The regions that bear on the question:**

    line 97   first_derivative
    line 104  reduced_curvature
    line 108  bubble_and_derivative, as called there
    line 46   WilsonQuadrature, for how bubble and its derivative are formed

**Read whatever else is needed. If the answer turns on a line outside
this list, say which.**

## 2. The author's derivation, stated as a prediction

**Derive this independently before checking it. Then check it.**

From `first_derivative` at line 101 and `reduced_curvature` at line 109:

    V'(m)  = m * ( 1/(2G) - I0(m) )
    V''(m) = 1/(2G) - I0(m) - m * I0'(m)

**At any non-trivial root the gap condition holds**, `1/(2G) = I0(m)`,
**so the first two terms cancel exactly and**

    V''(root) = - m * I0'(m)

**Under `m -> -8-m`**: `I0` is invariant by the frozen identity, so
`I0'` is odd about `m = -4`, giving `I0'(-8-m) = -I0'(m)`. With
`m2 = -8 - m1`:

    V''(m2)   - m2 * I0'(m2)     -(-8-m1) * (-I0'(m1))         m2
    ------- = --------------- = ------------------------ = - ------
    V''(m1)   - m1 * I0'(m1)         - m1 * I0'(m1)             m1

**PREDICTION: the ratio of the two restricted curvatures equals
`-m2/m1` exactly, for every coupling and every grid.**

**Verified by the author against all ninety pairs**, using the stored
values only:

    pairs checked                              90
    worst relative deviation from -m2/m1       1.781e-03
    typical relative deviation, away from Gc   1e-5 to 1e-4

**The worst cases sit at `G/Gc = 0.98` and `0.99`**, where `m1`
approaches zero and the bisection resolution `6.103515625e-05` is a large
fraction of it.

**That pattern is CONSISTENT WITH root-resolution amplification as
`m1 -> 0`. It is not established as the sole source.** The stored root
records carry their own non-zero stationarity residuals, and the
quadrature has its own finite-grid error; **neither has been separated
out.** **Do not attribute the whole deviation to `m1` unless you
decompose the sources**, and if you do not, say the deviation is
consistent with that explanation rather than caused by it.

**If your check disagrees with these numbers, report yours** and treat
the disagreement as the finding.

## 3. The pre-registered verdicts and their consequences

**Fixed before the executor reads. Not renegotiated afterwards.**

**`COORDINATE-INDUCED`** — the asymmetry follows from the definition of
the quantity, with no free content: the ratio is fixed by `-m2/m1`, and
`m2` is itself fixed by the identity `m2 = -8 - m1`.

**The label is operational and narrower than its name.** What this
verdict asserts is **definition-induced / algebraically determined**: the
prefactor `mhat` in the third term of `V''` is not invariant under
`m -> -8-m` while the other two terms are, so the ratio is fixed once the
root positions are. **It does NOT assert that the asymmetry is a pure
coordinate-transformation Jacobian artefact**, and **it does not exclude
the other ordinary explanations** — covariance of the curvature
definition at the two points, and a measure or Jacobian contribution —
**which remain untested.** **§4(a) item 5 requires you to say which are
excluded and which are not, and "all four" is not an available answer on
this evidence.**

**Consequence:** **the curvature asymmetry carries no independent
physical content.** Combined with `C1`, **the negative-mass branch then
has no independent content of any kind that has been demonstrated** —
its stored position is fixed by the Wilson-complement identity, and its
curvature ratio is fixed by that position and a prefactor.

**Bit-exactness is deliberately absent from this consequence.** The
mechanism behind the mirroring is unresolved under `OPEN-CC-3`, and
**`C3` does not rest on it**; a consequence that cited it would tie this
verdict to an open question it does not need. **This is a finding about what the
existing evidence supports, NOT a demonstration that the branch is
unphysical.** **It is material to the PI ruling that admitted the branch
as a candidate, because the ruling's stated basis was that the branch
was the computable thing available.** **Report it; do not act on it.**

**`PARTIALLY-COORDINATE-INDUCED`** — the ratio relation holds but a
residual beyond resolution effects remains unaccounted.
**Consequence:** the residual is the only remaining candidate for
independent content, and **its size and origin must be stated** so that a
later task can decide whether it is worth pursuing.

**`PHYSICAL`** — the asymmetry is not accounted for by the definition.
**Consequence:** the branch retains independent content, `C1`'s
narrowing does not settle it, and **the adopted artifact's §5b must be
revisited by a later task.**

**`INCONCLUSIVE`** — the static reading and the stored values do not
settle it. **Consequence:** name the computation that would, and **do not
perform it.**

**If the reading establishes something none of these represents, STOP and
report a `SPECIFICATION_DEFECT`.** **Do not invent a consequence.**

## 4. The two files

### (a) The findings artifact

`derivations/P2-PHASE-01_C3_curvature_asymmetry.md`, containing:

1. **the verdict**, in the first line of its section;
2. **the derivation**, in the executor's own working, with the line
   numbers it rests on;
3. **the check** against all ninety pairs, with the worst deviation and
   where it occurs;
4. **the consequence**, transcribed from §3 **verbatim, not
   paraphrased**;
5. **which of the adopted artifact's four ordinary explanations are
   thereby excluded**, and which remain untested;
6. **what this does not establish**, per §6.

**No recommendation and no proposal for the next task.**

### (b) The open-items register

`derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md`, **a new file**, holding
**exactly three entries**, each with what is known, what is not, and
where the evidence sits:

    OPEN-CC-1  The adopted artifact's §5a CAUTION is PARTLY settled and
               its text is not. C1 established the first disjunct: the
               production complement root is NOT constructed from the
               ordinary root, but recovered by a separate bracketed
               search. THE SECOND IS NOT SETTLED — why the stored pairs
               mirror bit-exactly is unresolved, and OPEN-CC-3 records
               the mechanism as open. The adopted artifact on the
               branch still presents the whole provenance question as
               open, which is now wrong about the first disjunct and
               right about the second. Amending it is a later task; the
               branch is not integrated. An earlier draft of this entry
               said both disjuncts were resolved and that the exactness
               IS a search-structure artefact; that contradicted §0 and
               OPEN-CC-3 in the same document and is corrected here.

    OPEN-CC-2  What the de-duplication threshold suppresses is
               UNDETERMINED. Line 167 of the exploratory script
               discards a returned bracket root lying within 2.0e-4 of
               one already held, and the trivial root 0.0 is held
               first. At G/Gc = 1.00 the stored output carries the
               complement root near -8 and the trivial root, and no
               near-origin non-trivial root. WHAT IS ESTABLISHED: the
               de-duplication suppresses the separately searched
               near-zero bracket representative when it lies within
               2.0e-4 of the already-recorded trivial root. WHAT IS
               NOT: whether a DISTINCT stationary root was thereby
               lost. At criticality the near-origin non-trivial
               solution merges with the trivial one, so suppressing it
               may be correct branch-coalescence handling rather than a
               completeness defect. An earlier draft called this "a
               measured exception to root completeness"; that was
               stronger than the evidence.

    OPEN-CC-3  The mechanism of the bit-exact mirroring is UNRESOLVED.
               C1's report argued that reflection exchanges which
               endpoint's sign is tested, so the bisection paths stay
               complementary through all 17 iterations, and separately
               that both roots lie on a dyadic lattice of 2**-15. A
               simulation on a bit-exactly symmetric toy function over
               the same two brackets does NOT reproduce the
               complementarity: the paths diverge at the fourth
               iteration and the residual is one bisection step,
               6.103515625e-05. AND THE DYADIC ARGUMENT DOES NOT STAND
               ALONE: lying on a common lattice guarantees only that
               both roots are integer multiples of 2**-15; it does not
               make the two integer indices sum to -8 x 32768. Ninety
               exact pairings still require a mechanism that preserves
               the mirrored index, and no established argument supplies
               one. THE OBSERVATION IS MEASURED AND STANDS — 186 roots
               on the lattice, 90 pairs summing to exactly -8.0 — but
               C1's EXACTNESS PROVENANCE verdict rests on an argument
               with a counterexample and an argument that is
               insufficient. It should not be cited as settled.

**These are open items, not deferrals.** **Do not add them to
`derivations/P2-DEFERRED-ITEMS.md`**, whose own text says entries are
added by PI decision and which is not modified by this task.

**State in the file that it is a register of open items arising from the
C-check line, that nothing in it is a PI decision, and that entries are
added only by a task authorised to do so.**

## 5. What this task must not do

- **Do not modify any existing file.** Not the script, the results, the
  adopted artifact, `GATES.md`, or `P2-DEFERRED-ITEMS.md`.
- **Do not run the script** and do not write under `results/`.
- **Do not compute a new numerical result from the model.** **Reading
  stored values and forming ratios of them is arithmetic on existing
  evidence; evaluating `I0` or its derivative at a new point is not.**
  **If your check requires the latter, that is `INCONCLUSIVE`.**
- **Do not answer `C2`.** If the reading bears on it, one sentence, no
  conclusion.
- **Do not revisit the PI ruling on the negative-mass branch**, and do
  not recommend that it be revisited. **§3's consequence says report and
  do not act; that is the whole of the instruction.**
- **Do not change any gate, gate status, prerequisite state or verdict.**
- **Do not touch `main`**, do not merge.
- **Do not repair anything the reading turns up.** **Report it and leave
  it**, and **do not add a fourth open item** — the register's contents
  are frozen at three by §4(b).

## 6. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** A
`COORDINATE-INDUCED` verdict, together with `C1`, **removes the evidential
weight of everything currently known about the negative-mass branch.**
**It does not show the branch is unphysical, and it must not be reported
as showing that.** **The absence of independent evidence and evidence of
absence are different**, and the second has not been produced by anything
in this line.

**Also state the narrower limit.** All of this rests on **one restricted
one-dimensional curvature under a uniform scalar ansatz at `mu = 0`.**
**The full condensate-space Hessian has never been computed**, and
nothing here bears on what it would show.

## 7. Acceptance criteria

**A1 — Refs and the script.** `refs/heads/main` resolves to
`1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`. The script measures
`3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0` and
equals the results file's `script_sha256`. **Any mismatch → STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18, **carrying `reviewed specification SHA-256:` filled in.** **If blank
or naming a different digest, STOP and say which.** Report both digests
equal.

**A3 — The derivation, independently worked**, with the line numbers it
rests on, and **the anchoring disclosure** required by the block at the
head of this specification.

**A4 — The check over all ninety pairs.** **Report the count checked,
the worst relative deviation, and the coupling at which it occurs.**
**Ninety is the expected count; if you find another number, report yours
and say which pairs you included.**

**A5 — The verdict**, one of the four of §3, in the findings artifact's
first line.

**A6 — The consequence transcribed, not paraphrased.** Diff it against
§3's text for the selected verdict and report that they correspond. **A
rewritten consequence is a STOP.**

**A7 — The open-items register**, per §4(b): **exactly three entries**,
the three named, **no fourth**, and the statement that nothing in it is a
PI decision.

**A8 — Scope, per §8. Final base-to-head scope: 5 additions and 0
modifications.** **`modify:` is `[]` and must remain so.** **A single
modification anywhere is a STOP.**

**A9 — Nothing existing changed.** Every path existing at the evidence
base is blob-identical at commit 4. **Report the count of paths
compared**, and confirm explicitly for the script, the results file,
`GATES.md`, and `derivations/P2-DEFERRED-ITEMS.md`.

**A10 — The checker over this task's own range**, base `1cb5550f…`, head
**commit 3**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_c3-curvature-asymmetry.md

**Config for both runs, stated so that you supply no value of your own:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**`append_only_paths` is NOT `[]`** — an empty set turns `P3` from
`NOT_DECLARED` into `NOT_APPLICABLE`. **`authorised_modified_gates` IS
`[]`, and here that is truthful**: no gate may change. **The two empty
lists mean opposite things, and the difference is in the checker's code,
not in the notation.**

**`P7` will return `PASS` and it is evidence of nothing.** This task
changes no gate, so nothing rests on it; **A9 is what establishes that.**

**RUN 2 is stop-governing; any failure is a STOP.** **Both configs and
both JSON outputs verbatim.**

**A10-final, post-report evidence:** re-run RUN 2 at commit 4.

**A11 — Commit-message hygiene** on all four commits. **Commits 1–3 go
in the report; commit 4 is post-report evidence.**

## 8. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_c3-curvature-asymmetry.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_c3-curvature-asymmetry.md
    commit 3  derivations/P2-PHASE-01_C3_curvature_asymmetry.md
              derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md
    commit 4  reports/2026-08-XXT{HHMM}Z_c3-curvature-asymmetry.md

    stated: 5 additions, 0 modifications
    base: 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    head: <commit 4>
    mode: exact
    add:
      derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md
      derivations/P2-PHASE-01_C3_curvature_asymmetry.md
      reports/2026-08-XXT{HHMM}Z_c3-curvature-asymmetry.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_c3-curvature-asymmetry.md
      specs/2026-08-XXT{HHMM}Z_c3-curvature-asymmetry.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Both derivations files move
together in commit 3** — the register records what the findings leave
open, and a commit carrying one without the other would be a partial
record.

**Committed report — measured at commit 3:** A1–A9 and A11 for commits
1–3; **A10's two runs with both configs verbatim**; commit 1–3 SHAs and
stored messages; commit 4's intended message; **the final scope stated as
INTENDED.**

**Post-report evidence, NOT written back:** the final scope measured
base-to-commit-4; A10-final; A11 for commit 4; validators at commit 4;
the push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 9. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  two files of §4. **Nothing else, at all.**
- **No file existing at the evidence base may be modified**, for any
  reason.
- **Do not adjust the config to make RUN 2 pass.**
- **Do not describe `P7` as having checked gate integrity.**
- No force-push, no history rewrite, no branch deletion.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 10. Report contract

- everything in §8 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **the derivation and the anchoring disclosure**;
- **A4's ninety-pair check**, count, worst deviation, and where;
- **the verdict and confirmation the consequence was transcribed**;
- **which of the four ordinary explanations are excluded and which
  remain untested**;
- **A7's three register entries**, confirmed three and not four;
- **A9's path count**;
- **A10's two runs**, both configs verbatim, and the statement about the
  two empty lists;
- **whether answering `C3` made you want to act on the PI ruling.**
  **Say so, and confirm you did not**;
- **§6's Rule 16 assessment**, both limits;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 11. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**
**Every line was produced by running the stated method in a clean
clone.** **No measurement was taken through a truncated view.**

    target      the script and its recorded digest
    method      sha256sum at 1cb5550f; read script_sha256 from the
                results JSON
    MEASURED    3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0,
                identical in both places

    target      the two definitions the derivation rests on
    method      read lines 97-109 of the script at 1cb5550f
    MEASURED    line 101  return mhat * (1.0/(2.0*coupling)
                          - quadrature.bubble(mhat))
                line 109  return 1.0/(2.0*coupling) - bubble
                          - mhat * derivative
                The third term carries the prefactor mhat; the first two
                do not.

    target      the predicted ratio, over the whole stored set
    method      for every grid and coupling with two non-trivial roots,
                compare reduced_curvature(m2)/reduced_curvature(m1)
                against -m2/m1
    MEASURED    90 pairs; worst relative deviation 1.781e-03, at
                G/Gc = 0.98; deviations of order 1e-5 to 1e-4 away from
                criticality. Examples: G/Gc = 0.80 observed -18.4996
                against -18.5004; G/Gc = 3.00 observed 4.5242 against
                4.5242.

    target      the de-duplication threshold of OPEN-CC-2
    method      read line 167 of the script
    MEASURED    `if all(abs(root - known) > 2.0e-4 for known in roots)`
                — a returned bracket root is discarded when it lies
                within 2.0e-4 of one already held.

    target      the counterexample of OPEN-CC-3
    method      bisect a bit-exactly symmetric toy function over
                (-12,-4) and (-4,4) for 17 iterations and trace the
                kept-half sequence
    MEASURED    paths RLLLRRRRRRRRRRRRR and LRRLRRRRRRRRRRRRR — not
                complementary from the fourth step; residual
                -6.103515625e-05. The author cannot presently say
                whether the toy is degenerate or the argument
                incomplete.
    DERIVED     the dyadic-lattice argument does not close the gap
                either: a common lattice of 2**-15 constrains each root
                to be an integer multiple of it, and says nothing about
                whether the two integers sum to -262144. The author
                accepted that argument as decisive in earlier
                correspondence; the Reviewer's objection is correct and
                OPEN-CC-3 now records the mechanism as UNRESOLVED.
    MEASURED    the observation itself is unaffected: 186 non-trivial
                roots are exact multiples of 2**-15 and all 90 pairs
                sum to exactly -8.0.

    target      what the de-duplication suppresses, for OPEN-CC-2
    method      read line 162-169 of the script; read the G/Gc = 1.00
                root records from the results file
    MEASURED    algebraic_roots seeds the list with the trivial root
                0.0 before searching either bracket. At G/Gc = 1.00 the
                stored output holds the complement root near -8 and the
                trivial root, and no near-origin non-trivial root. At
                criticality the near-origin non-trivial solution merges
                with the trivial one, so the suppression may be correct
                handling. WHETHER A DISTINCT ROOT WAS LOST IS NOT
                ESTABLISHED, and OPEN-CC-2 is worded as a question.

    target      whether this task touches anything pinned
    method      grep 'sha256 `[0-9a-f]{64}`' over GATES.md at 1cb5550f
    MEASURED    TWO pins, naming the two DRAFT files. This task modifies
                neither, and modifies nothing at all, so no re-pin is
                required and none is authorised.

    target      derivations/P2-DEFERRED-ITEMS.md
    method      read its headings and closing section at 1cb5550f
    MEASURED    three entries, DEFERRED-01 to -03, and a closing
                statement that entries are added by PI decision. That
                is why §4(b) creates a separate file rather than
                appending here.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from blob 1922fe88… and
                executed — not re-implemented
    MEASURED    one scope block; stated 5 additions, 0 modifications;
                manifest lists five paths; parse OK, counted equals
                stated.
