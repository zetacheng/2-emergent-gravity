# Report — C1: is the complement root recovered or constructed?

Specification: `specs/2026-08-13T0150Z_c1-complement-provenance.md`
Review: `reviews/chatgpt/2026-08-13T0150Z_c1-complement-provenance.md` — APPROVED FOR EXECUTION
Evidence base: `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab` (authoritative `main`)
Branch: `science/c1-complement-root-provenance`, cut from that commit.
**`main` was not touched. Nothing that existed at the evidence base was modified.**

**Every figure is labelled MEASURED or INTENDED.** **Nothing here claims to
measure commit 4.**

---

## 0. Both verdicts, and the one thing nobody had explained

**ROOT PROVENANCE: `RECOVERED`.** **EXACTNESS PROVENANCE:
`SEARCH-STRUCTURE-INDUCED`.**

**That is the combination the specification's author predicted, and the
prediction is not what established it.** R1–R5 are all CONFIRMED against named
lines, and the exhaustive check is stronger than the five claims: **`-8.0 -`
occurs at exactly two lines in all 462, both inside `symmetry_check`.**

**The exactness question was open and this task closes it.** The review said
static inspection must still establish why the roots mirror bit-exactly rather
than within the bisection resolution, and §2a recorded that the author's own toy
simulation of the described structure produced `-6.103515625e-05` — one bisection
step — not zero. **The mechanism is now identified, and §2a's stated reason for
why it need not be zero is wrong.**

**The three findings that settle it:**

**1 — The exactness is carried by a dyadic lattice, not by the function.** Both
brackets have width `8 = 2**3` with exactly representable endpoints, so all 17
bisections land on multiples of `2**-14` and the returned midpoint on multiples
of `2**-15`. **MEASURED from the stored data: all 186 non-trivial roots are
exact integer multiples of `2**-15`, and all 90 pairs sum to exactly `-8.0`.**

**2 — The left/right exchange preserves the mirroring instead of breaking it.**
§2a expected it to break the invariant because reflection exchanges `left` and
`right`. **It also exchanges which endpoint's sign is tested**, and in a proper
bracket the two tests are complementary — so *A keeps its left half* corresponds
exactly to *B keeps its right half*, which is what an orientation-reversing
reflection requires. The invariant survives all 17 iterations. §4 gives the
case analysis.

**3 — The integrand is NOT bit-symmetric, and the study measured that itself.**
`symmetry.complement_pairs` reports `absolute_difference` values of
`1.1102230246251565e-16`, `1.3877787807814457e-17`, `2.0816681711721685e-17` and
`1.3877787807814457e-17`. **`I0(m)` and `I0(-8-m)` are not the same double.**
So the exactness cannot come from the function values — and it does not need to,
because the mechanism requires only sign agreement at 17 midpoints, where the
margin is about ten orders of magnitude. **The field the specification suspected
of being "computed from the relation" turns out to be the evidence that the
exactness is not a property of the integrand.**

**Disclosure, per the pre-registration block, and it differs by axis.**

    ROOT PROVENANCE      ANCHORED-THEN-AGREED. I read the review before the
                         script — both arrived together — so I knew R1-R5 and
                         the predicted verdict before opening the file. I
                         verified each claim against named lines and found no
                         refutation, but I cannot call the reading independent.

    EXACTNESS PROVENANCE INDEPENDENT. The review explicitly declined to settle
                         it, and §2a's stated mechanism is the one my reading
                         contradicts. Nobody supplied the lattice argument, the
                         tie-break compensation, or the 1e-16 asymmetry
                         evidence.

**Nothing was run. No new numerical result was produced.** §7 states exactly
what arithmetic was performed on stored values and why it is reading.

---

## 1. A1 — Refs and the script

**MEASURED.**

```
git ls-remote origin refs/heads/main
1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab	refs/heads/main

scripts/p2_phase01_scalar_exploratory.py at 1cb5550f
  blob    b44bc63d115f4e88a706d046e60488c51d8a06a0
  sha256  3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0
  lines   462

results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json
  script_sha256  3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0
  script         scripts/p2_phase01_scalar_exploratory.py
```

**All three match the specification's §1 values, and the results file's recorded
digest equals the measured one. No STOP.** **The study's outputs are
attributable to the bytes I read**, which is the only reason this task's answer
means anything.

## 2. A2 — The review, committed unedited, with its specification digest

**MEASURED.** The review carries:

    Reviewed specification SHA-256: 5669c174fb6b489a9d311bb3df0c116cb9f6e9900b420d900613bb43dea24176

**Filled in, and correct:**

    supplied specification file, sha256
      5669c174fb6b489a9d311bb3df0c116cb9f6e9900b420d900613bb43dea24176   EQUAL

    supplied review   c7312ea8d3a172e6dd7edc848f9d6980de28a111d99b6f539c0e8f0979512465
    committed blob    c7312ea8d3a172e6dd7edc848f9d6980de28a111d99b6f539c0e8f0979512465
    EQUAL

**A2's stop is not triggered.** Both arrived as FILES; Rule 18 satisfied on
both.

## 3. A3 — The two verdicts, with the lines establishing each

### ROOT PROVENANCE — `RECOVERED`

**Established by lines 138–159, 162–169, 172–187, 190–201, 387–420, and by an
exhaustive search of all 462 lines.**

    138-159  bisect_root obtains its root only by repeated evaluation of
             divided_gap; line 153 halves the bracket, line 154 evaluates,
             lines 155-158 choose a half, line 159 returns 0.5*(left+right)
    162-169  algebraic_roots calls bisect_root separately on (-12.0, -4.0)
             and (-4.0, 4.0) at lines 165-166
    172-187  root_record stores the value it is given: "mhat": mhat, line 181
    190-201  grid_result maps root_record over algebraic_roots' output,
             lines 197-200, and does not touch the pair
    387-420  build_results passes the grid list through as "grid_results": grids

**The exhaustive check, which is what actually settles it.** Every occurrence of
the literal `-8` and of the word `complement` in the whole file:

    163  docstring, "Wilson-complement sectors"
    297  complement_pairs = []                    inside symmetry_check
    311  second = quadrature.bubble(-8.0 - mhat)  inside symmetry_check
    312  complement_pairs.append(                 inside symmetry_check
    315  "complement": -8.0 - mhat,               inside symmetry_check
    325  "wilson_complement_relation": (          inside symmetry_check
    326  a string literal quoting the relation    inside symmetry_check
    329  "complement_pairs": complement_pairs,    inside symmetry_check

**`-8.0 -` occurs at exactly two lines, 311 and 315, and both are inside
`symmetry_check` (line 294).** **No production root anywhere in the script is
computed from another root.**

### EXACTNESS PROVENANCE — `SEARCH-STRUCTURE-INDUCED`

**Established by lines 165 (the bracket pair), 152–159 (the bisection), and the
stored data.** The mechanism is set out in full in the findings artifact and
summarised in §0 above. **It falls squarely inside §2's definition** — *"a pair
of brackets that are mirror images under `m -> -8-m`"* — so A4's
mechanism-not-represented STOP is not triggered.

**`RECOVERED` did not determine this**, and the artifact keeps the two verdicts
in separate sections for that reason: a recovered root table does not make its
exact mirroring meaningful.

## 4. R1–R5, each verified against the pinned bytes

**Every claim CONFIRMED. None refuted, none undetermined.**

**R1 — CONFIRMED.** *`algebraic_roots()` calls `bisect_root()` separately on the
two brackets `(-12,-4)` and `(-4,4)`.* Line 165 is
`for left, right in ((-12.0, -4.0), (-4.0, 4.0)):` and line 166 is
`root = bisect_root(left, right, coupling, quadrature)`. **Two separate calls,
one per bracket.**

**R2 — CONFIRMED, and by exhaustive search rather than by reading one function.**
*`bisect_root()` uses only `divided_gap()`; no root is computed as `-8 - mhat`.*
Lines 142, 143 and 154 are its only function evaluations and all three call
`divided_gap`. **And the literal `-8.0 -` does not occur anywhere in
`bisect_root`, `algebraic_roots`, `root_record`, `grid_result` or
`build_results` — it occurs only at lines 311 and 315.**

**R3 — CONFIRMED.** *`grid_result()` writes each root returned by
`algebraic_roots()` straight into the results, without post-processing the pair.*
Lines 197–200 are a comprehension over `algebraic_roots(...)` applying
`root_record`, and line 181 stores `"mhat": mhat` unaltered. **`build_results`
then passes the list through unchanged as `"grid_results": grids`**, which I
checked because R3's claim is about the whole path to the file and not only about
`grid_result`.

**R4 — CONFIRMED.** *`symmetry_check()` DOES construct `complement = -8.0 - mhat`
and compares `bubble(mhat)` against `bubble(-8-mhat)` — so the
`complement_pairs` field is a constructed diagnostic, while the production root
table is not.* Line 311 evaluates `bubble(-8.0 - mhat)`, line 315 stores the
constructed abscissa, line 316 stores `abs(first - second)`. **Both halves of
R4 hold: the construction is real, and it is confined to the diagnostic.**

**R5 — CONFIRMED.** *Therefore the code-provenance verdict is `RECOVERED`.*
**It follows from R1–R4 as verified, and I reached the same verdict.** **But R5
being true does not address exactness**, which the specification says plainly and
which §0 and §5 treat separately.

**One claim in the specification that is NOT among R1–R5 is REFUTED, and it is
reported here because §9 asks for anything I would have specified differently.**
§2a states: *"The reason it need not be zero: `m -> -8-m` maps the first bracket
onto the second **reversed**, and the tie-break in the bisection is written in
terms of `left` and `right`, which reflection exchanges."* **The exchange is
compensating, not breaking.** Reflection exchanges the endpoints *and* exchanges
which endpoint's sign the tie-break tests, and in a proper bracket those two
tests are complementary, so the two effects cancel exactly:

    f(a)*f(m) < 0   ->  A: right = m   (keeps [a, m], the LEFT half)
                        B: f(b)*f(m) > 0, else-branch, left = m
                           (keeps [m, d], the RIGHT half)
                        and phi([a,m]) = [phi(m), phi(a)] = [m_B, d]   OK

    f(a)*f(m) > 0   ->  A: left = m    (keeps [m, b], the RIGHT half)
                        B: f(b)*f(m) < 0, if-branch, right = m
                           (keeps [c, m], the LEFT half)
                        and phi([m,b]) = [phi(b), phi(m)] = [c, m_B]   OK

**The only case that would break it is `f_middle == 0.0` exactly**, where both
tests take the `<= 0` branch; it does not arise in the stored data, whose
`stationarity_residual` values are all nonzero. **The early returns at lines
144–147 also preserve the mirroring**, as the findings artifact shows.

**I cannot account for the author's toy result of `-6.103515625e-05` without its
source, and I did not write one.** **What I can say is that the value is exactly
`-2**-14`, one node spacing of the 17-iteration lattice**, so it corresponds to
a single mismatched branch decision at the final step — but which detail of the
toy differed from the script is not determinable from the script, and §3 forbids
me to run a variant. **That is the one question in this area I am leaving
open, and it is a question about the toy, not about the study.**

## 5. A4 — Both consequences transcribed, not paraphrased

**MEASURED, mechanically rather than by assertion.** Both paragraphs were
extracted programmatically from the committed specification blob by exact
substring slice and written into the artifact unaltered; the artifact was then
searched for each extracted string:

    RECOVERED consequence                 717 chars
      present verbatim in the specification   True
      present verbatim in the artifact        True
      diff between the two                   0 lines

    SEARCH-STRUCTURE-INDUCED consequence  280 chars
      present verbatim in the specification   True
      present verbatim in the artifact        True
      diff between the two                   0 lines

**Neither was retyped and neither was paraphrased. A4's rewritten-consequence
STOP is not triggered.**

**One observation about the `SEARCH-STRUCTURE-INDUCED` consequence, recorded
separately in the artifact because the transcription may not be amended.** Its
closing clause reasons from *"a function with an exact reflection symmetry"*.
**Measured, that symmetry is not exact** — the `complement_pairs` differences are
`1e-16` to `1e-17`. **The operative claim is unaffected and is stronger than its
own rationale**: the exactness survives an integrand that is only approximately
symmetric, which is precisely what shows the search structure and not the
symmetry is producing it. **I transcribed the paragraph as written and put the
observation beside it.**

**A4's mechanism-not-represented STOP was considered and is not triggered.** §2
defines `SEARCH-STRUCTURE-INDUCED` to include *"a pair of brackets that are
mirror images under `m -> -8-m`"*, which is exactly the mechanism found.
**`NOT-STRUCTURE-INDUCED` was not selected**, so its no-consequence STOP does
not arise either.

## 6. A5, A6, A7 — Nothing existing changed

**A6, MEASURED at commit 3**, whole-tree `git ls-tree -r` blob comparison, path
by path:

    paths existing at the evidence base, i.e. PATHS COMPARED   343
    of those, blob-identical at the head                       343
    MODIFIED                                                     0
    removed                                                      0
    added                                                        3

    scripts/p2_phase01_scalar_exploratory.py                          IDENTICAL
    results/.../scalar_stationary.json                                IDENTICAL
    GATES.md                                                          IDENTICAL
    derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md      IDENTICAL
    derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md      IDENTICAL

**The script I read and the results file I quoted are byte-identical between the
evidence base and the head.** **Reading left no trace, which is the property a
reading task has to be able to demonstrate.**

**A5:** `modify:` is `[]` and remains `[]`. **Zero modifications. A5's
single-modification STOP is not triggered**, including for whitespace — the
script's blob id is unchanged.

**A7, MEASURED:**

    GATES.md blob at base    849a4fbfe62d6478f092a84b0175357a74bbbb06
    GATES.md blob at head    849a4fbfe62d6478f092a84b0175357a74bbbb06   IDENTICAL
    '^## P2-' count          14
    P2-PHASE-01              Status: PROPOSED

**No gate, gate status, prerequisite state or verdict changed**, and A6 already
proves it at the blob level; A7 states it because a reader of a science task will
look for it.

## 7. What arithmetic was performed, and why it is reading

**§3 forbids computing a new numerical result and says quoting a number already
in the results file is reading. This section states exactly where the line was
drawn**, because the artifact's central evidence is arithmetic.

**Performed — all of it on values already stored in the results file:**

    the exact rational value of each stored root, to test whether it is an
      integer multiple of 2**-15                                    186 roots
    the float sum of each stored pair, to test whether it is -8.0     90 pairs
    the hex representation of two stored roots
    integer arithmetic on the multiples: -271665 + 9521 = -262144

**This is representation inspection of quoted values — the same method the
specification's author used in §2a when verifying `-0x1.e5cd800000000p+2` in
hex.** **No `bubble()`, no `divided_gap()`, no `bisect_root()`, and no part of
the script was executed. No file under `results/` was written or read except as
input.**

**NOT performed, deliberately:** any evaluation of the Wilson integral, any toy
bisection, any re-run over an asymmetric mass grid, and any check of whether
`bubble(m)` equals `bubble(-8-m)` bitwise. **The last would have been the
obvious thing to compute and I did not**: the study had already measured it and
stored the answer, so quoting `complement_pairs` was both sufficient and within
scope.

**The reflection and lattice arguments are symbolic**, carried out on the code's
structure rather than by simulation, which is why the artifact presents a case
analysis rather than a table of trial values.

## 8. A8 — The two checker runs, and the two empty lists

Base `1cb5550f…`, head **commit 3** `176ea0c6…`. **Both prospectivity readings
run.**

### RUN 1 — default subject selection, observational, governs nothing

```json
{
  "base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
  "head": "176ea0c6bc4fae7d69a8eb5a658373958920254c",
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": [],
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

### RUN 2 — `specification_paths` naming only this specification

```json
{
  "base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
  "head": "176ea0c6bc4fae7d69a8eb5a658373958920254c",
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": [],
  "specification_paths": ["specs/2026-08-13T0150Z_c1-complement-provenance.md"],
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

**The `EXCLUSIVE` variants are identical but for the one `inclusivity` field.**

**MEASURED — all four runs `overall` PASS, exit 0:**

    RUN 1  INCLUSIVE  exit 0  PASS
    RUN 2  INCLUSIVE  exit 0  PASS      <- stop-governing
    RUN 1  EXCLUSIVE  exit 0  PASS
    RUN 2  EXCLUSIVE  exit 0  PASS      <- stop-governing

    P1 PASS  P2 PASS  P3 PASS  P4 PASS  P5 NOT_APPLICABLE
    P6 PASS  P7 PASS  P8 PASS  P9 NOT_APPLICABLE

**RUN 2's stop is not triggered.** **What RUN 2 excluded: NOTHING** — MEASURED,
RUN 1's and RUN 2's JSON are byte-identical, because the range adds exactly one
specification and the default selection already selects it.

### The two empty lists mean opposite things

**This is the clearest illustration of it the programme has produced, because
this task carries one of each.**

    append_only_paths          ["DECISION_LOG.md"]   NOT []
    authorised_modified_gates  []                    IS [], and truthfully so

**`P3` treats `[]` as "nothing to check".** Supplying it would have turned `P3`
from `NOT_DECLARED` into `NOT_APPLICABLE` — the check switched off rather than
passed — so the config names `DECISION_LOG.md`, and `P3` passes on a real
subject. **MEASURED:** `base_bytes` 89541, `head_bytes` 89541,
`base_is_byte_prefix_of_head` true, `deleted_lines_base_to_head` 0.

**`P7` treats `[]` as "nothing may change".** Here that is the truthful value:
**no gate may change in this task, and none did.** So the same notation is the
weakest possible declaration in one property and the strongest in the other.
**The difference is in the checker's code, not in the notation**, and a reader
comparing the two lines of this config cannot tell which is which without
reading `check_p3` and `check_p7`.

### `P7` returned `PASS` and it is evidence of nothing

**MEASURED, from this task's own run:** `section_count_base` 0,
`section_count_head` 0, against a `GATES.md` carrying fourteen gates.
`GATE_HEADING` is `^## (P2-[A-Z0-9-]+)\s*$` and every real heading continues past
the ID, so **P7 compared two empty maps.**

**This task changes no gate, so nothing rests on `P7` either way** — and what
establishes that is A6's path-by-path comparison and A7's blob identity, not the
checker. **Had `P7` been the evidence, the strongest possible declaration
(`authorised_modified_gates: []`) would have been enforced by a parser that
matches nothing.**

## 9. A9 — Commit-message hygiene, and the commit order

**MEASURED.** Proposed messages scanned before each commit; stored messages read
back after:

    0bd3833b  spec: C1, is the complement root recovered or constructed?
    458c7942  review: pre-execution review for C1 complement-root provenance
    176ea0c6  derivations: answer C1 on two axes -- RECOVERED root table, forced exactness

    trailers on each of the three                       none
    'Co-Authored-By' in any stored message                0
    session identifier or URL in any stored message       0
    tool or model attribution in any stored message       0

**Case-insensitive scan over all three stored bodies: 0 matches.**

**Commits, MEASURED, in the order §5 specifies — FOUR, not five:**

    commit 1  0bd3833b9bea6a8962adf576f85ab139100cbd41  specs/2026-08-13T0150Z_c1-complement-provenance.md
    commit 2  458c794209a94f6ddf6ae01627698b60f82f5482  reviews/chatgpt/2026-08-13T0150Z_c1-complement-provenance.md
    commit 3  176ea0c6bc4fae7d69a8eb5a658373958920254c  derivations/P2-PHASE-01_C1_complement_root_provenance.md
    commit 4  INTENDED                                  reports/2026-08-13T0150Z_c1-complement-provenance.md

**There is no separate content commit because commit 3 is the content**, as §5
states. **No re-pin commit exists either, and this is the first task in this line
for which that is true** — the findings artifact is new, unpinned, and named by
no gate.

**The UTC token `0150` and the day `13` were MEASURED** (`date -u`) when commit 1
was written, not chosen.

**Commit 4's INTENDED message**, first line:

    report: record the C1 verdicts and the mechanism behind the exact zero

**The final scope, INTENDED** — commit 4 does not exist while this is written:

    stated: 4 additions, 0 modifications
    base: 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    head: <commit 4, INTENDED>
    mode: exact
    add:
      derivations/P2-PHASE-01_C1_complement_root_provenance.md
      reports/2026-08-13T0150Z_c1-complement-provenance.md
      reviews/chatgpt/2026-08-13T0150Z_c1-complement-provenance.md
      specs/2026-08-13T0150Z_c1-complement-provenance.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths, all additions. MEASURED at commit 3: three of the four are in
place; the fourth is this file.** **The scope measured base-to-commit-4 is
post-report evidence and is not claimed here.**

## 10. Whether the reading bore on `C2` or `C3`

**One sentence each, no conclusion drawn, per §3.**

**`C2`:** the reading exposes the form of the integrand summed by
`WilsonQuadrature.bubble` — `1.0 / denominator` with `denominator = s + w * w` at
lines 82–83, where `s` is a sum of `sin**2` terms — and that form bears directly
on `C2`'s question about the sign of `I0`.

**`C3`:** `reduced_curvature` at line 109 returns
`1.0 / (2.0 * coupling) - bubble - mhat * derivative`, whose third term is not
invariant under `m -> -8 - m` while the first two are, which bears directly on
`C3`'s question whether the curvature asymmetry is induced by the chosen
coordinate.

**Both are stated and stopped there. Neither is answered, and I did not follow
either one further** — including in the artifact, where the same two sentences
appear and nothing else.

## 11. Did answering `C1` make me want to change anything outside scope?

**Yes, three things. I changed none of them.**

**1 — The adopted artifact's §5a.** Its `CAUTION` says the exact-zero residual
*"is consistent with the complement root being CONSTRUCTED from the relation
rather than solved for independently, and also with a root-search grid symmetric
about `Mhat = -4`"*. **Both disjuncts are now settled: the first is false and the
second is the wrong shape** — the mechanism is a mirrored *bracket pair*, not a
symmetric grid. **§3 forbids softening or strengthening §5a and says amending it
is a later task with the verdict in hand.** **I did not touch it**, and it sits
on a branch rather than on `main` in any case.

**2 — `C2` looked answerable while I was in the file.** The integrand's form at
lines 82–83 is short and the question is about a sign. **§3 forbids answering
`C2` and allows one sentence.** **I wrote the sentence and stopped**, and I note
the pull explicitly because a reader should know the boundary was tested rather
than never approached.

**3 — The `2.0e-4` de-duplication threshold at line 167.** It is what discards
the bracket-B root at `G/Gc = 1.00` and produces the six singleton points, and a
reader of the results file cannot tell that from the file alone. **That is an
observation about the study's completeness, adjacent to the root-completeness
limitation the adopted artifact already records — and it is not `C1`.** **I
recorded it here and put nothing about it in the findings artifact**, which §4
requires to answer `C1` and stop.

## 12. §6 — Rule 16 assessment

**Rule 16 is operative. I confirm the specification's candidate and sharpen it.**

**This task establishes something about the SCRIPT, not about the physics.**
**C1 changes the weight of existing evidence and adds none.** No number in
`results/` moved; what changed is what may be said about ninety of them.

**Named plainly: `max |sum + 8| = 0.00e+00` is not a measurement of agreement,
and after this task it may not be quoted as one.** It is the arithmetic
signature of two bisections on mirrored dyadic brackets. **The ninety zeros are
one fact about bracket geometry reported ninety times.**

**The junction to guard is `numerical provenance -> physical interpretation`, and
it fails in both directions.** `RECOVERED` does not make the complement branch a
phase: the full condensate-space Hessian and the gate's admissibility assessment
are still absent, and `OPEN-AC-3` still blocks the common-normalised depth
comparison. And `SEARCH-STRUCTURE-INDUCED` does not make the branch unphysical —
**it removes evidential weight from a stored position, which is not the same as
removing the branch.**

**A second junction, which this execution added.** **A verdict of `RECOVERED`
invites the reading that the solver was validated, and it was — but only against
a symmetry the search structure was already going to reproduce.** The two
bisections are not independent determinations of one quantity; they are one
determination and its exact reflection. **So "the solver found both roots" is
true and "the solver's agreement with itself is a check" is not.** **What would
be a check is a search that is not a reflection of the first** — an asymmetric
mass grid or non-mirrored brackets — and **that computation is not performed
here and is a separate task with its own pre-registration**, exactly as §2's
`INCONCLUSIVE` consequence describes for a case this task did not select.

**And the limit on my own method.** **This is a static reading.** It establishes
what the code does; it does not establish that the code was run as read. The
`script_sha256` field ties the outputs to these bytes (§1), and the stored roots'
dyadic structure is consistent with the bisection I read — **but nothing here
re-executes the study, and the consistency of 186 roots with a lattice is strong
corroboration rather than proof of execution.**

## 13. Stops and clarifications

### `SPECIFICATION_DEFECT` — none blocking; one premise refuted

**No stop condition fired and no criterion was unsatisfiable.** A4's two STOP
branches were both considered and neither applies: the mechanism found is
explicitly inside §2's `SEARCH-STRUCTURE-INDUCED` definition, and
`NOT-STRUCTURE-INDUCED` was not selected.

**One premise of the specification is REFUTED, and it is a premise rather than a
criterion.** §2a's stated reason why the residual "need not be zero" — that the
`left`/`right` tie-break is exchanged by reflection — **identifies a real
asymmetry and draws the wrong conclusion from it.** §4 gives the case analysis:
the exchange is compensating. **Nothing in the specification depended on that
reason being right; it was offered as motivation for a question this task was
asked to answer, and answering it required contradicting it.** **I report it
rather than passing over it, because a premise left standing gets quoted.**

### `OBSERVATION_METHOD_ERROR` — one, self-caught, in this report

**I first verified the quoted script line numbers with a shell loop using
`grep` on patterns containing `*`, `[` and `(`, and four lines came back
`MISMATCH` when the printed content was visibly correct.** **The mismatches were
my own regex-metacharacter escaping, not the artifact's line numbers.** I
re-ran the check with fixed-string comparison over 27 fragments and got **27 OK,
0 mismatches**, which is the measurement §3 and §5 of the artifact rest on.
**Had I trusted the first run I would have "corrected" four correct line
references**; had I trusted it the other way I would have reported a
verification I had not performed.

**A second method choice, recorded because it bounded the answer.** **I did not
test whether `bubble(m) == bubble(-8-m)` bitwise, although it was the obvious
computation and would have taken one line.** The study had already measured it
and stored the result, so I quoted `complement_pairs` instead. **The stored
values turned out to be the decisive evidence** — they are nonzero, which is
what rules out the function-values explanation. **Computing it myself would have
produced the same conclusion and violated §3.**

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — none

**Pre-registration was compromised and the specification said so before I read
anything**, which is why there is no ambiguity to resolve: the disclosure block
fixed in advance what an honest answer looks like. **My disclosure differs by
axis** — anchored-then-agreed on root provenance, independent on exactness — and
§0 gives it in those terms rather than choosing the more flattering single word.

### `REPOSITORY_DEFECT` — one, pre-existing and out of scope

**`P7` is vacuous against the real `GATES.md`.** §8. Known, not touched, **and
not offered as evidence for anything here** — A6 and A7 carry that weight.

### `ENVIRONMENT` — none

**No environment failure occurred.** **`CONVENTIONS.md` Rule 13 carries two
conflicting diagnostic orders, a known open item; neither was exercised**, and I
am not naming one as having applied. Nothing was installed and the exploratory
script was not run.

### Secondary findings, kept separate

- **The `2.0e-4` de-duplication threshold at line 167** is what discards the
  bracket-B root at `G/Gc = 1.00`, producing the six singleton points a reader of
  the results file cannot otherwise account for. §11. **Adjacent to root
  completeness, not part of `C1`.**
- **`symmetry_check` tests the complement relation on `shift 0.0` only** (line
  295), never at `shift 0.25`. **The exactness conclusion does not depend on it**,
  because it does not depend on the integrand's symmetry holding to any
  precision.
- **RUN 2's narrowing excluded nothing** — byte-identical to RUN 1. §8.
- **The two prospectivity readings differ in one field and no verdict.** §8.
- **`P1` passed by reading a structured `stated:` declaration as prose**, on a
  branch cut from `main`, which does not carry the declared-total repair.
- **The author's toy residual `-6.103515625e-05` is exactly `-2**-14`**, one node
  spacing of the lattice — consistent with a single mismatched final decision,
  but not diagnosable from the script. §4.

### Anything ambiguous, unsatisfiable, or that I would have specified differently

- **§2a's mechanism claim should have been posed as a question, not a reason.**
  It reads as an explanation — *"the reason it need not be zero"* — and it is
  wrong. **Stated as "the author could not rule out that the tie-break exchange
  breaks the mirroring", it would have been true and would have cost the
  executor nothing.** As written, an executor who trusted it would have gone
  looking for a different mechanism and might have returned `INCONCLUSIVE`.
- **§1 should have named `WilsonQuadrature.bubble` among the regions to read.**
  The listed five are the right starting points for root provenance, but the
  exactness question turns on the integrand's symmetry, which lives at lines
  57–90. **§1 does say the list is a starting point and asks which outside line
  the answer turns on** — it turns on lines 82–83 and on `complement_pairs` — so
  the specification anticipated the gap correctly even though it did not close
  it.
- **The disclosure block asks for one answer where two are needed.** *"whether
  their reading was reached independently, agreed after anchoring, or cannot be
  separated"* is a single question, and the honest answer differs between the two
  verdicts. **I gave two, which the block does not forbid but does not
  anticipate.**
- **`INCONCLUSIVE` on exactness would have been the safe answer and it would have
  been wrong.** The specification made it available and attached a real
  consequence to it. **I record that the temptation existed**: a static reading
  that concludes "the code does not determine it" is unfalsifiable by the same
  static reading. **What made the positive answer defensible is that the stored
  data are checkable against it** — 186 roots on the lattice, 90 exact sums, and
  the nonzero `complement_pairs` — **so the claim can be refuted by anyone who
  re-reads the same file.**
