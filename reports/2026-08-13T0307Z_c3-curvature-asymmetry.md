# Report — C3: is the curvature asymmetry physical or coordinate-induced?

Specification: `specs/2026-08-13T0307Z_c3-curvature-asymmetry.md`
Review: `reviews/chatgpt/2026-08-13T0307Z_c3-curvature-asymmetry.md` — APPROVED FOR EXECUTION
Evidence base: `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab` (authoritative `main`)
Branch: `science/c3-curvature-asymmetry`, cut from that commit.
**`main` was not touched. Nothing existing was modified.**

**Every figure is labelled MEASURED or INTENDED.** **Nothing here claims to
measure commit 4.**

---

## 0. Verdict, and the one place this went further than the specification

**Verdict: `COORDINATE-INDUCED`** — operationally, definition-induced /
algebraically determined, and no wider. **At a non-trivial root the gap
condition removes the first two terms of `V''`, leaving `-m * I0'(m)`, whose only
asymmetry is the explicit prefactor; `I0'` cancels from the ratio, giving
`V''(m2)/V''(m1) = -m2/m1 = (8+m1)/m1`, fixed once the positions are.**

**The check reproduces the specification's figure: 90 pairs, worst relative
deviation `1.7811e-03`.** **It occurs at `G/Gc = 0.99`, not at `0.98` as §11
states** — §2's looser phrasing, that the worst cases sit at both, is right.

**And the deviation is accounted for exactly rather than bounded, which is more
than §2 asked for.** §2 permits calling the near-critical pattern *consistent
with* resolution amplification and forbids attributing it without decomposing
the sources. **The sources decompose without any new evaluation, because the
omitted term is itself stored.** Since `divided_gap(m) = 1 - 2*G*I0(m)`, the
first two terms of `V''` are exactly `divided_gap_factor(m)/(2G)`, and
`divided_gap_factor` sits in every stored root record:

    quantity compared                        max over 90 pairs      median
    raw   V''(m2)/V''(m1)  vs  -m2/m1             1.7811e-03      4.925e-05
    with divided_gap_factor/(2G) removed          1.1951e-14      6.664e-16

**Eleven orders of magnitude, and after the subtraction the residual no longer
tracks `|m1|` at all.** **So the entire deviation is the leftover from roots
resolved only to the bisection step, and nothing remains beyond round-off.**
**That licenses attribution rather than consistency**, and the artifact says so
in those terms.

**A by-product worth naming: the same subtraction measures the differentiated
identity.** After it, the compared quantities are `-m2*I0'(m2)` and
`-m1*I0'(m1)` as the script computed them, so agreement with `-m2/m1` to
`1.2e-14` **also confirms `I0'(-8-m) = -I0'(m)` on all six finite grids** — a
premise the derivation assumed and the stored data now support.

**Anchoring disclosure, and it is split.** **The mechanism was mine and is on
the record; the closed form was not.** My `C1` artifact and report, committed at
`92726596f29e12ec12e7f795bd68b902ac712d50` on **2026-08-13T02:02:05Z** — about
an hour before this specification's token — state that
`reduced_curvature`'s *"third term is not invariant under `m -> -8 - m` while the
first two are, which bears directly on `C3`'s question"*. **But I read §2's
closed form, its gap-condition cancellation and its verification numbers before
writing the derivation.** **So: mechanism independently identified and
timestamped; derivation as presented completed after reading §2. I do not claim
it blind.**

**Two of the four ordinary explanations are excluded, two are not**, and "all
four" is not claimed. §6.

**`C2` was not answered. The script was not run. No model quantity was
evaluated at any new point.**

---

## 1. A1 — Refs and the script

**MEASURED.**

```
git ls-remote origin refs/heads/main
1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab	refs/heads/main

scripts/p2_phase01_scalar_exploratory.py, sha256 at 1cb5550f
  3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0
results/.../scalar_stationary.json, script_sha256 field
  3bb26bd942c0a7392e7fc6468a3f4744fcaa7371861d74791f56ea4ecd0e9bf0
EQUAL
```

**Both match the specification's §1 value. No STOP.**

## 2. A2 — The review, committed unedited, with its specification digest

**MEASURED.** The review carries
`reviewed specification SHA-256: 0d0898be55c14af3bb9c6e77c119869160bc744c4b214ff089e8965d954b7734`.

    supplied specification file, sha256
      0d0898be55c14af3bb9c6e77c119869160bc744c4b214ff089e8965d954b7734   EQUAL

    supplied review   437753f315eacbf87d99eba17f866d15e70f4627cde43bc698914da2930d2eff
    committed blob    437753f315eacbf87d99eba17f866d15e70f4627cde43bc698914da2930d2eff
    EQUAL

**Filled in, correct, and neither blank nor naming a different digest. A2's stop
is not triggered.** Both arrived as FILES; Rule 18 satisfied on both.

## 3. A3 — The derivation, and the anchoring disclosure

**The working is in the findings artifact and is not repeated here.** It rests on
these lines, each verified by fixed-string comparison against the pinned script
— **9 fragments checked, 0 mismatches**:

    101  return mhat * (1.0 / (2.0 * coupling) - quadrature.bubble(mhat))
    107  docstring: "Analytic derivative of the complete reduced first derivative"
    108  bubble, derivative = quadrature.bubble_and_derivative(mhat)
    109  return 1.0 / (2.0 * coupling) - bubble - mhat * derivative
    135  return 1.0 - 2.0 * coupling * quadrature.bubble(mhat)
    183  "divided_gap_factor": gap_factor,
    167  if all(abs(root - known) > 2.0e-4 for known in roots):
     84  derivative -= float(np.sum(2.0 * w / (denominator * denominator)))
     85  value = bubble / self.n**4, derivative / self.n**4

**Two lines outside §1's list carried the answer, and §1 asks which.** **Line
135 (`divided_gap`) and line 183 (`divided_gap_factor`)** are what made the
decomposition possible: §1 named lines 97, 104, 108 and 46, which are enough for
the derivation but not for attributing the deviation. **Lines 84–85 also matter**,
because they show `derivative` is the analytic mass derivative of the same
quadrature sum rather than a finite difference — without which `I0'` in the
working would be a different object from the code's.

**The disclosure, in the three terms the specification offers.** **Neither
"independently" nor "cannot be separated" is the honest answer; it is "reached
after reading §2", with a documented prior.** §0 above gives the timestamped
prior claim and states exactly what was and was not anticipated. **The
prediction being in front of me is why the check is the load-bearing part of
this task rather than the derivation** — and the check is against ninety stored
cases and reproducible by anyone.

## 4. A4 — The check over all ninety pairs

**MEASURED, using only stored fields** — `mhat`, `reduced_curvature`,
`divided_gap_factor`, `G`. **Nothing was evaluated from the model.**

    pairs checked                                   90
    worst relative deviation from -m2/m1            1.7811e-03
    where                        G/Gc = 0.99, n = 48, shift 0.25
    median relative deviation                       4.925e-05

**Which pairs were included:** every grid-coupling point returning **two**
non-trivial roots, `m1` taken as the near-origin root and `m2` as the
complement. **96 grid-coupling points exist; the six at `G/Gc = 1.00` return one
non-trivial root and are not pairs, giving 90** — which is `C1`'s accounting and
the specification's expected count.

**§11's attribution of the worst case is off by one coupling.** Every pair at the
two couplings §2 names:

    G/Gc = 0.98   n=32/0.0  8.2605e-05   n=32/0.25 4.8791e-04
                  n=40/0.0  2.6028e-04   n=40/0.25 8.4225e-04
                  n=48/0.0  7.2606e-04   n=48/0.25 2.0842e-04
    G/Gc = 0.99   n=32/0.0  1.6097e-03   n=32/0.25 3.6815e-04
                  n=40/0.0  1.3363e-03   n=40/0.25 1.2037e-03
                  n=48/0.0  6.9409e-04   n=48/0.25 1.7811e-03   <- worst

**The maximum at `0.98` is `8.4225e-04`, less than half the maximum at `0.99`.**
**The magnitude `1.781e-03` is exactly right; only the coupling label is wrong.**
**§2's wording — "the worst cases sit at `G/Gc = 0.98` and `0.99`" — is correct**,
so the two sections disagree with each other and §2 is the accurate one.

**§11's two worked examples reproduce exactly**, on the grid §0 names:

    G/Gc = 0.80, n=48, shift 0.0   observed -18.4996   predicted -18.5004
    G/Gc = 3.00, n=48, shift 0.0   observed   4.5242   predicted   4.5242

### The decomposition, which upgrades "consistent with" to "accounted for"

**MEASURED.** Because `divided_gap(m) = 1 - 2*G*I0(m)` at line 135, the first two
terms of `V''` equal `divided_gap_factor(m)/(2G)` exactly, and
`divided_gap_factor` is stored per root at line 183. **The stored roots are not
exact roots** — their `stationarity_residual` runs up to `1.875e-05` — so that
bracket does not vanish and the prediction omits it.

    quantity compared                        max over 90 pairs      median
    raw                                           1.7811e-03      4.925e-05
    with divided_gap_factor/(2G) removed          1.1951e-14      6.664e-16

    corrected maximum, per coupling: never exceeds 1.2e-14, and no
    longer varies systematically with |m1|

**Before the decomposition I also ran the weaker consistency test the
specification's caution anticipates**, and I report it because it is what a
non-decomposing check would have concluded: multiplying each deviation by `|m1|`
collapses the spread from **4034x** to **65x**. **That is strong support for
amplification and would NOT have justified attribution** — 65x remains
unexplained, and the stored stationarity residuals are not constant either, so
that test separates nothing. **The exact subtraction is what settles it, and it
leaves 1.2e-14.**

**So the deviation is attributed, not merely bounded**, and the artifact states
it as attribution. **Had the subtraction left a residual above round-off, the
verdict would have been `PARTIALLY-COORDINATE-INDUCED` and §3 requires its size
and origin; it did not, so that verdict is not selected.**

## 5. A5, A6 — The verdict and the transcribed consequence

**A5: `COORDINATE-INDUCED`, in the first line of the findings artifact's verdict
section.**

**A6, MEASURED mechanically.** The consequence paragraph was extracted
programmatically from the committed specification blob by exact substring slice
and written into the artifact unaltered, then both were searched for the
extracted string:

    consequence text                          910 chars
      present verbatim in the specification   True
      present verbatim in the artifact        True

**Not retyped, not paraphrased. A6's rewritten-consequence STOP is not
triggered.**

**§3's mechanism-not-represented STOP was considered and does not apply.** The
finding is exactly `COORDINATE-INDUCED` as §3 defines it — the ratio fixed by
`-m2/m1` with `m2` fixed by the identity — and the artifact keeps the label
inside its stated narrow meaning.

## 6. Which ordinary explanations are excluded, and which are not

**Two excluded, two untested. "All four" is not available and is not claimed.**

**EXCLUDED — the `Mhat` parameterisation makes `V''` non-invariant under
`m -> -8-m` by construction.** **It does**: the prefactor `m` in the third term
is not invariant while the first two terms are, and at a root only the third
survives. **This is the demonstrated mechanism, not a residual possibility.**

**EXCLUDED — the potential is symmetric while the derivative in the chosen
coordinate picks up sign or coordinate effects.** **It does**: `I0` is even about
`m = -4`, `I0'` is odd about it, and that sign flip combined with the prefactor
produces `-m2/m1`. **Confirmed numerically to `1.2e-14` by §4's decomposition.**

**NOT EXCLUDED — covariance of the curvature definition at the two points.**
**Untested.** The derivation works entirely inside the script's single
parameterisation. **It shows the asymmetry is fixed within that
parameterisation; it says nothing about what a covariant second-derivative
definition would give**, and nothing here computes one.

**NOT EXCLUDED — a Wilson mass-dependent Jacobian or measure contribution
differing between the two points.** **Untested.** `reduced_curvature` carries no
such factor, so the open question is not whether the implemented quantity has one
— it does not — **but whether a fuller formulation should.** Outside this
reading.

**The review's §3 and §4 make the same limitation and I have not widened it:**
`COORDINATE-INDUCED` here means definition-induced for this restricted
curvature, **not** covariance under a general field reparameterisation and
**not** exclusion of measure or Jacobian terms.

## 7. A7 — The open-items register

**MEASURED: exactly THREE entries, the three named, and no fourth.**

    ## `OPEN-CC-1` — the adopted artifact's §5a CAUTION is partly settled and its text is not
    ## `OPEN-CC-2` — what the de-duplication threshold suppresses is undetermined
    ## `OPEN-CC-3` — the mechanism of the bit-exact mirroring is unresolved

    count of '^## `OPEN-CC-' headings   3

**The file states in its own header that it is a register of open items arising
from the C-check line, that nothing in it is a PI decision, and that entries are
added only by a task authorised to do so.** It also records that it is not
`derivations/P2-DEFERRED-ITEMS.md`, whose entries are added by PI decision —
**and A9 confirms that file is blob-identical.**

**`OPEN-CC-3` qualifies my own previous verdict, and I wrote it as the
specification requires rather than defending the earlier argument.** `C1`'s
`EXACTNESS PROVENANCE = SEARCH-STRUCTURE-INDUCED` rests on two arguments; the
register records that the first has a counterexample — a symmetric toy function
whose bisection paths diverge at the fourth iteration — and that the second is
insufficient, because a common `2**-15` lattice does not force the two integer
indices to sum to `-262144`. **The measured observation is unaffected and the
register says so. The verdict should not be cited as settled, and this report
does not cite it.** **I note that my `C1` report presented the case analysis as
establishing the mechanism; the counterexample shows it did not, and I did not
argue the point here.**

**No fourth item was added**, though §5's prohibition was tested: the deviation
decomposition of §4 is arguably a finding about the study's numerical hygiene.
**It belongs in the findings artifact, which reports it, and not in a register
frozen at three.**

## 8. A8, A9 — Scope and protected paths

**A9, MEASURED at commit 3**, whole-tree `git ls-tree -r` blob comparison:

    PATHS COMPARED (every path existing at the evidence base)   343
    of those, blob-identical at commit 3                         343
    MODIFIED                                                      0
    removed                                                       0
    added                                                         4

    scripts/p2_phase01_scalar_exploratory.py                     IDENTICAL
    results/.../scalar_stationary.json                           IDENTICAL
    GATES.md                                                     IDENTICAL
    derivations/P2-DEFERRED-ITEMS.md                             IDENTICAL

**All four explicitly required confirmations hold.** **The script I read and the
results file I did arithmetic on are byte-identical between the evidence base and
the head** — reading and ratio-forming left no trace.

**A8:** `modify:` is `[]` and remains `[]`. **Zero modifications; A8's
single-modification STOP is not triggered.**

**The final scope, INTENDED** — commit 4 does not exist while this is written:

    stated: 5 additions, 0 modifications
    base: 1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    head: <commit 4, INTENDED>
    mode: exact
    add:
      derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md
      derivations/P2-PHASE-01_C3_curvature_asymmetry.md
      reports/2026-08-13T0307Z_c3-curvature-asymmetry.md
      reviews/chatgpt/2026-08-13T0307Z_c3-curvature-asymmetry.md
      specs/2026-08-13T0307Z_c3-curvature-asymmetry.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Five paths, all additions. MEASURED at commit 3: four are in place; the fifth
is this file.** **The scope measured base-to-commit-4 is post-report evidence.**

## 9. A10 — The two checker runs, and the two empty lists

Base `1cb5550f…`, head **commit 3** `5a2539e2…`. **Both prospectivity readings
run.**

### RUN 1 — default subject selection, observational, governs nothing

```json
{
  "base": "1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab",
  "head": "5a2539e253488c6bb2afb4ee84c07a83902601f3",
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
  "head": "5a2539e253488c6bb2afb4ee84c07a83902601f3",
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": [],
  "specification_paths": ["specs/2026-08-13T0307Z_c3-curvature-asymmetry.md"],
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

**RUN 2's stop is not triggered.** **What RUN 2 excluded: NOTHING** — RUN 1's and
RUN 2's JSON are byte-identical, because the range adds one specification and the
default selection already selects it.

**The two empty lists mean opposite things**, and this task carries one of each,
exactly as the previous one did:

    append_only_paths          ["DECISION_LOG.md"]   NOT []
    authorised_modified_gates  []                    IS [], truthfully

**`P3` treats `[]` as "nothing to check"** — supplying it would convert
`NOT_DECLARED` into `NOT_APPLICABLE`, the check switched off rather than passed —
so the config names a real subject and `P3` passes on it. **`P7` treats `[]` as
"nothing may change"**, which is the truthful declaration here: no gate may
change and none did. **The difference is in the checker's code, not in the
notation**, and a reader comparing the two lines cannot tell which is which
without reading `check_p3` and `check_p7`.

**`P7` returned `PASS` and it is evidence of nothing** — `GATE_HEADING` matches
zero of the fourteen real gate headings, so it compared two empty maps. **This
task changes no gate, so nothing rests on it; A9's 343-for-343 blob identity is
what establishes that.**

## 10. A11 — Hygiene, and the commit order

**MEASURED.** Proposed messages scanned before each commit, stored messages read
back after:

    a566c7cd  spec: C3, is the curvature asymmetry physical or coordinate-induced?
    7881422d  review: pre-execution review for C3 curvature asymmetry
    5a2539e2  derivations: answer C3 COORDINATE-INDUCED, and open a C-check register

    trailers on each of the three                       none
    'Co-Authored-By' in any stored message                0
    session identifier or URL in any stored message       0
    tool or model attribution in any stored message       0

**Case-insensitive scan over all three stored bodies: 0 matches.**

**Commits, MEASURED, in the order §8 specifies — FOUR:**

    commit 1  a566c7cdff8d80e58073db375861ec1abd18072a  specs/2026-08-13T0307Z_c3-curvature-asymmetry.md
    commit 2  7881422d721590dfd208fe75f024056a5d39d501  reviews/chatgpt/2026-08-13T0307Z_c3-curvature-asymmetry.md
    commit 3  5a2539e253488c6bb2afb4ee84c07a83902601f3  BOTH derivations files
    commit 4  INTENDED                                  reports/2026-08-13T0307Z_c3-curvature-asymmetry.md

**Both derivations files moved together in commit 3**, as §8 requires — MEASURED,
`git show --stat` on commit 3 lists exactly two files, 320 insertions, no
deletions. **A commit carrying the findings without the register would have been
a partial record.**

**The UTC token `0307` and the day `13` were MEASURED** (`date -u`) at commit 1.

**Commit 4's INTENDED message**, first line:

    report: record the C3 verdict and the exact decomposition of the deviation

## 11. Did answering `C3` make me want to act on the PI ruling?

**Yes, and I did not.**

**The pull is real and worth stating precisely.** §3's consequence says that,
combined with `C1`, the negative-mass branch **has no independent content of any
kind that has been demonstrated** — and it notes the ruling's stated basis was
that the branch was the computable thing available. **Both halves of what made it
computable are now accounted for: the position by the Wilson identity, the
curvature ratio by that position and a prefactor.** **So the natural next thought
is that the ruling rests on less than it appeared to.**

**§3 says report and do not act; §5 forbids revisiting the ruling and forbids
recommending that it be revisited. I have done neither.** **The findings artifact
contains no recommendation and no proposal for a next task**, and this report
makes none. **I have also not written the observation into the open-items
register**, because the register is frozen at three and because a fourth entry
saying "the ruling may need revisiting" would be the recommendation §5 prohibits
wearing a different hat.

**What I have done is report it once, here, in the terms §3 uses**, and note that
the person who decides what follows is the PI and not the executor who found it.

**The other pull, smaller:** `OPEN-CC-3` obliged me to record that my own `C1`
exactness verdict rests on a refuted argument, and the tempting move was to
defend the case analysis. **I did not argue it. The counterexample is recorded as
the specification wrote it**, and §13 states plainly that my `C1` report
overclaimed.

## 12. §6 — Rule 16 assessment

**Rule 16 is operative. I confirm the specification's candidate and add the
narrower limit it asks for, plus one this execution exposed.**

**The junction: this removes evidential weight, it does not produce evidence of
absence.** A `COORDINATE-INDUCED` verdict together with `C1` **removes the
demonstrated independent content of everything currently known about the
negative-mass branch** — position and restricted curvature both. **It does not
show the branch is unphysical or absent, and it must not be reported as showing
that.** **The absence of independent evidence and evidence of absence are
different, and nothing in this line has produced the second.** The branch may be
real; what has been established is that the stored numbers do not
independently witness it.

**The narrower limit, stated as required.** **All of this rests on one restricted
one-dimensional curvature under a uniform scalar ansatz at `mu = 0`.** **The full
condensate-space Hessian has never been computed**, and nothing here bears on
what it would show. The results file's own `limitations` field records the same
three boundaries, and `OPEN-AC-3` still blocks the common-normalised depth
comparison.

**A third junction this execution added: an exact agreement is not a strong
result when the quantity was never free.** **The corrected ratio matches
`-m2/m1` to `1.2e-14` across ninety pairs, and that number is impressive-looking
and nearly content-free.** It confirms that the script computes the derivative it
says it computes and that the frozen identity holds on the grids — **arithmetic
and implementation checks, not physics.** **A reader meeting `1.2e-14` beside
ninety cases could take it for a strong physical confirmation; it is the
signature of a quantity with no freedom left in it.** **That is the same reading
error `C1` warned about for the ninety zero residuals, arriving one level up**, and
it is the reason the artifact states the verdict before any number.

**And the limit on my own method.** **This is a static reading plus arithmetic on
stored values.** It establishes what the code defines and that the stored values
are consistent with the identity to round-off. **It does not re-execute the study,
does not test the quadrature against an independent implementation, and cannot
detect an error common to both the stored curvature and the stored
`divided_gap_factor`** — they come from the same run of the same code.

## 13. Stops and clarifications

### `SPECIFICATION_DEFECT` — none blocking; one internal disagreement recorded

**No stop condition fired.** §3's mechanism-not-represented STOP was considered
and does not apply: the finding is `COORDINATE-INDUCED` exactly as §3 defines it.

**§2 and §11 disagree about where the worst deviation sits, and §11 is wrong.**
§11 records *"worst relative deviation 1.781e-03, at `G/Gc = 0.98`"*; MEASURED,
the worst is `1.7811e-03` at **`G/Gc = 0.99`** (n=48, shift 0.25), and the
maximum at `0.98` is `8.4225e-04`. **§2's own phrasing — "the worst cases sit at
`G/Gc = 0.98` and `0.99`" — is correct**, so this is an internal disagreement
rather than a defect in the premise the task depends on. **The magnitude is
exactly right in both sections.** A4 instructed me to report my number if it
differed; the number does not differ, only its label.

### `OBSERVATION_METHOD_ERROR` — none in this task's final measurements

**One method decision is recorded because it changed the strength of the answer,
and going the other way would have been defensible and weaker.** §2 permits
describing the near-critical deviations as *consistent with* resolution
amplification and forbids attribution without decomposing. **I first ran the
weak test** — multiplying each deviation by `|m1|`, which collapsed the spread
from 4034x to 65x — **and that test would have licensed only "consistent with",
which is what §2 anticipated.** **I then noticed the omitted term is itself a
stored field** (`divided_gap_factor`, line 183, and `divided_gap` at line 135),
subtracted it exactly, and got `1.2e-14`. **Reporting only the first test would
have satisfied the specification while leaving an accounted-for deviation
described as merely consistent.**

**No prior-task error surfaced in this execution's own measurements**, and the
line-number verification was done with fixed-string comparison from the start —
**9 fragments, 0 mismatches** — rather than with the shell `grep` that produced
four false mismatches in the previous task.

### `REPOSITORY_DEFECT` — one, pre-existing, out of scope; and one prior verdict qualified

**`P7` is vacuous against the real `GATES.md`.** §9. Known, untouched, **not
offered as evidence** — A9 carries that weight.

**And `C1`'s `EXACTNESS PROVENANCE` verdict is qualified rather than defended.**
`OPEN-CC-3` records that its reflection argument has a counterexample and its
dyadic argument is insufficient. **My `C1` report presented the case analysis as
establishing the mechanism. It did not.** The measured observation — 186 roots on
the `2**-15` lattice, 90 pairs summing to exactly `-8.0` — **stands and is
unaffected**; the explanation does not. **`C3` was deliberately built not to
depend on it**, which is why this task's verdict is unaffected by that
qualification.

### `ENVIRONMENT` — none

**No environment failure occurred.** **`CONVENTIONS.md` Rule 13 carries two
conflicting diagnostic orders, a known open item; neither was exercised**, and I
am not naming one as having applied. Nothing was installed; the exploratory
script was not run.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — none

**Blind pre-registration was unavailable and the specification said so first**,
which is why there is nothing to resolve: the disclosure block fixed in advance
what an honest answer looks like, and §0 and §3 give it, split by what was and
was not anticipated.

### Secondary findings, kept separate

- **Two lines outside §1's reading list carried the answer** — 135 and 183, which
  made the decomposition possible — **and lines 84–85 matter too**, because they
  establish that `derivative` is analytic rather than a finite difference. §3.
- **The decomposition doubles as a measurement of the differentiated identity**,
  `I0'(-8-m) = -I0'(m)`, to `1.2e-14` on all six grids. §0, §4.
- **`V''(m2)/V''(m1) = (8+m1)/m1` diverges as `m1 -> 0`**, so the adopted
  artifact's §5b table of large near-critical ratios is that divergence and not a
  physical effect. **The adopted artifact's own text does not say this**; it is on
  a branch and amending it is a later task.
- **RUN 2's narrowing excluded nothing** — byte-identical to RUN 1. §9.
- **The two prospectivity readings differ in one field and no verdict.** §9.
- **`P1` passed by reading a structured `stated:` declaration as prose**, on a
  branch cut from `main`, which does not carry the declared-total repair.

### Anything ambiguous, unsatisfiable, or that I would have specified differently

- **§11 should not have named a single coupling for the worst case when §2 named
  two.** The precise claim is falsifiable and false; the loose one is true.
  **I would have written §11 to carry the full twelve-value table for the two
  near-critical couplings**, which is small and settles the question.
- **§1's reading list should have included `divided_gap` and the root record's
  fields.** It lists what the derivation needs and not what the *check* needs.
  **§1 does ask which outside line the answer turns on** — 135 and 183 — so the
  specification anticipated the gap without closing it, exactly as `C1`'s §1 did.
- **§2's caution was calibrated for a weaker check than was available.** It
  assumed the executor could only bound the deviation, and instructed accordingly.
  **The stored `divided_gap_factor` makes exact attribution possible with no new
  evaluation, and a specification that had noticed that could have required the
  decomposition rather than permitting the weaker statement.** **This is the one
  place where following the specification literally would have understated the
  result.**
- **The register's three-entry freeze is right and it cost something.** §4's
  decomposition is a finding about the study's numerics that has no home: it is
  not `C3`'s verdict and it is not one of the three entries. **It is in the
  findings artifact and in this report, and nowhere that a future task would look
  for open items.** **I would rather the freeze had been "exactly the three
  named, plus any the executor must report, marked as such".**
- **`PARTIALLY-COORDINATE-INDUCED` was live until the subtraction ran.** With a
  `65x` unexplained spread it was the defensible verdict, and §3 attaches a real
  consequence to it. **What ruled it out was an exact decomposition, not a
  judgement about how small a residual may be** — and that is the right way for
  it to have been ruled out.
