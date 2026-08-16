# Report — integrate the reflection-positivity literature coverage audit, and land it

    branch      science/integrate-d1-coverage
    base        b27926aad0d3a1ef39f5e7e886f8571657c5687c   (authoritative main)
    source      science/d1-literature-coverage-audit-3 @ f8fdcf64e4106fff3958ae726237e4aec453af04
    measured at commit 3, c9efb4af66d53546d4421d0519fa5adbb2b0bce2   (the merge commit)

**One merge, no conflict. Six additions, ZERO modifications. Nothing in the
repository is changed.**

---

## 1. `A3` — environment conformance, before any measurement

**Run first, as `A3` requires, in Rule 13's diagnostic order extended by
Amendment D's step 0.**

    (0) execution location    /home/user/2-emergent-gravity; work in the
                              science/integrate-d1-coverage worktree cut from
                              b27926aa… by explicit SHA. MEASURED: three
                              worktrees present, this task's and the two
                              preceding governance tasks'. SAME CONTAINER.
    (1) execution identity    root, uid 0
    (2) interpreter           Python 3.11.15 at /usr/local/bin/python
    (3) permissions           repository writable; no permission failure
    (4) filesystem/workspace  MEASURED: `git rev-parse --is-shallow-repository`
                              → false. No `.git/shallow`. 431 commits on the
                              authoritative line. NOT SHALLOW.
    (5) package availability  MEASURED: pytest 9.1.1, numpy 2.4.6,
                              sympy 1.14.0, ruff 0.15.8 — all four declared
                              packages present and importable.

**NO RESTORATION WAS NEEDED AND NONE WAS PERFORMED. No repository content
was touched by this criterion.**

**Rule 13 carries two diagnostic orders, a known open item. NO ENVIRONMENT
FAILURE OCCURRED**, and **neither order was exercised** — I am not naming
one as having applied. The order above was run as a CONFORMANCE CHECK
because `A3` requires it, not in response to a failure.

**`A15`'s and `A16`'s figures are reportable only because this ran first.**

## 2. `A1` — repository and refs

**MEASURED, VERBATIM and NOT normalised:**

    git remote get-url origin        https://github.com/zetacheng/2-emergent-gravity

**No `.git` suffix. `A1` accepts either form, and it identifies
`zetacheng/2-emergent-gravity`**, which is the confirmation that carries
weight.

**Refs, MEASURED after fetching:**

    refs/remotes/origin/main                          b27926aad0d3a1ef39f5e7e886f8571657c5687c
    refs/heads/main                                   1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    science/d1-literature-coverage-audit-3 (remote)   f8fdcf64e4106fff3958ae726237e4aec453af04

**`refs/remotes/origin/main` is `b27926aa…`, as the evidence base requires.
No stop.** **`refs/heads/main` lags, and `A1` says a lagging local ref is
not a stop.** Every measurement here reads the remote-tracking ref or an
explicit SHA.

**MEASURED: the source is NOT an ancestor of `main`.**

    git merge-base --is-ancestor f8fdcf64… refs/remotes/origin/main
    exit status 1   →  NOT an ancestor

### 2.1 The earlier `D-1` branches — and one of them does not exist

**`A1` asks me to report that `science/d1-literature-coverage-audit` and
`…-audit-2` still exist and are unchanged. MEASURED, from a full
`git ls-remote origin` dump:**

    science/d1-literature-coverage-audit      8267bd408683be0dc163853ac4faad6fc067e200   EXISTS, unchanged
    science/d1-literature-coverage-audit-2    ABSENT — NO SUCH REF ON THE REMOTE
    science/d1-literature-coverage-audit-3    f8fdcf64e4106fff3958ae726237e4aec453af04   EXISTS, the source

**`…-audit-2` is not among the remote's refs.** The listing was read in
full, not grepped for one name, and no ref matching `d1-literature`
other than the two above appears.

**And the commit `§0` attributes to execution 2 is not resolvable here:**

    git cat-file -t a537e036        fatal: Not a valid object name a537e036

**So execution 2's history is not present in this repository at all**, and
its record exists only in this specification's `§0` prose.

**I did not touch any of them.** I did not delete, reset, reuse, move or
push any `D-1` branch; `…-audit` stands at exactly the SHA the first
execution pushed, and `…-audit-3` is untouched at its tip — verified again
after the landing.

**This is reported as a finding and is NOT a stop**, `§17.4`. `A1`'s
operative confirmations — the base, the source, the non-ancestry — all
hold, and the integration depends on `…-audit-3`, which is present and
exactly as specified. **Stopping the landing of a completed scientific
result over a branch that never reached the remote would be
disproportionate**, and `§4`'s prohibition on deleting or reusing an
earlier `D-1` branch is satisfied by a task that touched none of them.

## 3. `A2` — the pre-execution review

**MEASURED.**

    field `Reviewed specification SHA-256:` PRESENT   yes, line 4
    value carried by the review                       461f8748a5d3c55fdd0201969b47289dd414284ac559a0da29d931fde7fe9ecd
    SHA-256 of the committed specification bytes      461f8748a5d3c55fdd0201969b47289dd414284ac559a0da29d931fde7fe9ecd
    MATCH                                             yes
    review verdict                                    APPROVE FOR EXECUTION
    committed unedited                                yes — byte-identical to the supplied review

**The field's presence was checked before its value was compared.**

**The review carries a `§12` "non-blocking editorial observation"** — that
the pre-issue record's gloss on `A7` is stale relative to the revised
normative `A7`. **MEASURED: the observation is correct.** `§10`'s record
says *"`A7` requires the classification derived from the tables"*, while
the normative `A7` forbids this task from classifying at all. **I followed
the NORMATIVE `A7` and performed no classification**, which is also what
the review directs. **Carried as a finding at `§17.5`.**

## 4. `A10` — which merge case, stated BEFORE the blob comparisons

**MEASURED, before the merge was made:**

    merge-base(origin/main, f8fdcf64…)                b27926aad0d3a1ef39f5e7e886f8571657c5687c
    commits on main after the base                    0

**The merge-base IS the evidence base, and `main` carries no commit after
it, so no commit on `main` could have touched an arriving path.** The merge
is one-sided.

**That ordering is what makes the comparison below mean what it appears to
mean.** In a two-sided merge, four identical blobs would be equally
consistent with the merge having discarded `main`'s side.

**NOW the comparisons, MEASURED at the merge commit against `f8fdcf64…`:**

    derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md   IDENTICAL
    reports/2026-08-16T1952Z_d1-literature-coverage-audit.md        IDENTICAL
    reviews/chatgpt/2026-08-16T1952Z_d1-literature-coverage-audit.md IDENTICAL
    specs/2026-08-16T1952Z_d1-literature-coverage-audit.md          IDENTICAL

**All four arriving paths blob-identical. Nothing arriving was altered in
transit, and the science landed here is the science that was reviewed.**

## 5. `A5` — no conflict

**MEASURED, `git diff --name-only --diff-filter=U` at the merge:**

    (empty)      conflict entries    0

**`git status --porcelain` reports no unmerged entry.** `§0` makes any
conflict an immediate stop; none arose.

## 6. `A4` — merge parentage, three separately derived measurements

    merge commit                              c9efb4af66d53546d4421d0519fa5adbb2b0bce2
    parent 1   git rev-parse HEAD^1           c2f4a27fad61bd734daadc6e49059783b6c205b6
    parent 2   git rev-parse HEAD^2           f8fdcf64e4106fff3958ae726237e4aec453af04
    merge-base git merge-base HEAD^1 HEAD^2   b27926aad0d3a1ef39f5e7e886f8571657c5687c

**Parent 1 IS this task's review commit. Parent 2 IS the specified source
tip. The merge-base IS the evidence base.**

**Commit 1 is an ancestor of parent 1, MEASURED:**

    git merge-base --is-ancestor 88aacd62ea86a5025e1323038e0aae9d2abcadb0 HEAD^1      exit status 0   →  YES

**The checker's `P5` independently recomputed all three and agrees.** Its
`does_not_establish` notes that three correct values are equally consistent
with recomputation and with one field copied into another — which is why
`A4` asks for them separately derived, and why each came from its own
command.

## 7. `A6` — the four verdicts and the burden accounting, re-derived

**Re-derived from the arriving artifact's `§4`–`§8`, by reading each
candidate section's own verdict line and then the coverage matrix
independently. MEASURED:**

    candidate     verdict     source section
    naive         PARTIAL     §4, "### Verdict: `PARTIAL`"
    Wilson        PARTIAL     §5, "### Verdict: `PARTIAL`"
    staggered     PARTIAL     §6, "### Verdict: `PARTIAL`"
    overlap       PARTIAL     §7, "### Verdict: `PARTIAL`"

**The artifact's own tally, `§8`, MEASURED verbatim:**

    Verdict counts: `COVERED = 0`, `PARTIAL = 4`, `NO COVERAGE FOUND = 0`,
    `NOT DETERMINABLE = 0`

**FOUR `PARTIAL`, ZERO `COVERED`.** Expected four and zero; measured four
and zero.

**The closing accounting sentence, MEASURED verbatim from `§8`:**

> `0` of the four candidate proof burdens are replaced by literature
> applicability; `4` remain open in full.

**Zero replaced, four open.** **`B0`'s seven-to-eleven estimate is
therefore unchanged, and this task neither re-derives nor revises it.**

**The accounting is DISCRETE. No fractional reduction appears anywhere in
the arriving artifact, and none is introduced here.**

## 8. `A7` — the gap classification is DEFERRED

**I did NOT classify the `FAIL` entries. `§2`'s three-way taxonomy —
`UNFROZEN DATUM`, `INCOMPATIBLE HYPOTHESIS`, `UNESTABLISHED APPLICABILITY
BRIDGE` — is RECORDED in the landed specification and NOT PERFORMED.**

**It is deferred to a separate task, `D-1b — RP gap classification`, which
this specification does not write and which I did not write either.**

**Why the deferral is right, and I agree with it:** classifying every
`FAIL` across four candidates and ten works is load-bearing scientific
analysis. Performed inside a landing report it would arrive with no
specification of its own and no pre-execution review of its method, and it
would then be relied on. **Every other integration in this line re-derived
conclusions ALREADY PRESENT in the arriving artifact. This one would author
a new one.**

### 8.1 The raw material — counts only, and the counting rule stated

**A count is not a classification.** These are occurrences of the literal
token `` `FAIL` `` in the arriving artifact, attributed to a candidate by
which basis block they appear in. **No tag was assigned to any entry.**

**MEASURED, per basis block in `§2.2`:**

    basis                                       axis rows   FAIL in axis table   FAIL in hypothesis prose   UNKNOWN AT ABSTRACT DEPTH
    MP87 → Wilson                                       7                    6                          5                           0
    MP87 → naive                                        7                    6                          3                           0
    OS78 → Wilson (abstract-depth cross-check)          7                    2                          0                           6
    FG26 → naive                                        7                    5                          6                           0
    FG26 → staggered                                    7                    5                          5                           0
    KU10 → overlap                                      7                    5                          4                           0

**MEASURED, per candidate:**

    candidate     bases   FAIL in axis tables   FAIL in hypothesis prose   TOTAL   UNKNOWN AT ABSTRACT DEPTH
    naive             2                    11                          9      20                           0
    Wilson            2                     8                          5      13                           6
    staggered         1                     5                          5      10                           0
    overlap           1                     5                          4       9                           0

**And the per-candidate `Exact failures preventing COVERED` bullet lists in
`§4`–`§7`, MEASURED: SIX bullets each, for all four candidates.**

**Three counting decisions, stated so the count is reproducible:**

**First, `UNKNOWN AT ABSTRACT DEPTH` is counted SEPARATELY and is not a
`FAIL`.** The artifact's own legend distinguishes them, and six of `OS78`'s
seven axis rows carry it. **Collapsing the two would inflate Wilson's count
by six and would misdescribe an ACCESS limitation as a MISMATCH** — the
distinction `A8` insists on, in a different place.

**Second, the legend line itself was excluded.** `§2.2` opens with
"`FAIL` names a mismatch or an unfrozen datum", which is a definition and
not an entry.

**Third, axis-table rows and theorem-specific hypothesis prose are counted
separately**, because the hypothesis lists are prose sentences rather than
table rows and a single figure would hide which is which.

### 8.2 The temptation, disclosed as `A7` requires

**`A7` says: "If you find yourself assigning tags while counting, stop and
report that you did."**

**I did not assign a tag to any entry, and no tag appears anywhere in this
report or in the commit messages.** **But the criterion is right that the
counting pulls toward it**, and the honest disclosure is that I could see
the classification forming while I read.

**Concretely: several rows say in terms that a programme datum is
unfrozen** — "programme reflection type is unfrozen", "programme temporal
boundary condition is unfrozen", "programme `M0` is unfrozen" — **and
several others say the source proves something about a different object** —
"dimension 2 is `FAIL` against 4", "different operator classes". **Reading
those, the taxonomy assigns itself.**

**That is exactly why the deferral matters and why I stopped at counting.**
**A classification that feels obvious on a first read is the kind most
likely to be wrong at the margin**, and the margin is the third category:
`UNESTABLISHED APPLICABILITY BRIDGE` entries such as `FG26`'s H1/H2/H3 or
`KU10`'s auxiliary-field bridge **read like either of the other two
depending on which sentence you weight.** **`D-1b` should do this with a
specification and a review, on all ten works and all four candidates, not
as a by-product of counting tokens in a landing report.**

**I report that I noticed the pull. I did not act on it.**

## 9. `A8` — works fetched, with depth and provenance

**MEASURED from the arriving artifact's `§2` source-depth ledger, parsed
row by row rather than read from its summary line:**

    key      depth        in B0's named seed set?
    OS73     FULL TEXT    yes
    OS75     FULL TEXT    yes
    OS78     ABSTRACT     yes
    N97      FULL TEXT    yes
    HJL98    FULL TEXT    yes
    MP87     FULL TEXT    NO
    KU10     FULL TEXT    NO
    GK22     FULL TEXT    NO
    FG26     FULL TEXT    NO
    STW81    ABSTRACT     NO
    L77      NOT FETCHED  NO

    fetched                  10       = 8 FULL TEXT + 2 ABSTRACT
    full text                 8       OS73, OS75, N97, HJL98, MP87, KU10, GK22, FG26
    abstract only             2       OS78, STW81
    encountered, not fetched  1       L77
    resting on recollection   0

**Expected ten, eight and two; measured ten, eight and two.** **The
artifact's own summary line agrees, and the figures above were derived by
parsing the table, not by copying that line.**

### 9.1 Outside `B0`'s seed set

**`B0`'s named seed set is FIVE works: `OS73`, `OS75`, `OS78`, `N97`,
`HJL98`.**

**MEASURED: FIVE fetched works were OUTSIDE it — `MP87`, `KU10`, `GK22`,
`FG26`, `STW81`.** Expected five; measured five.

**Of those five, THREE became load-bearing applicability bases**, and the
ledger says so in its own words:

    MP87   "Load-bearing Wilson-family RP evidence"
    KU10   "Load-bearing overlap RP evidence for a specified free theory"
    FG26   "Load-bearing interacting naive/staggered Euclidean RP evidence"

**The other two are not bases:** `GK22` is `ROUTE EVIDENCE` only, and
`STW81` is abstract-only formulation context "not used in a verdict".
Expected three; measured three.

**`L77` is a SIXTH outside-seed work, ENCOUNTERED AND NOT FETCHED** —
Lüscher's transfer-matrix construction, recorded as route evidence and not
pursued "because it does not by itself answer proposition (ii)."

**Every one of the four bases that carries a verdict is an outside-seed
work.** **A boundary-scoped audit would have found none of them**, and the
staggered row in particular would still be resting on `B0`'s unfilled `L3`
gap.

### 9.2 `OS78` — the access fact and the criterion, stated as two things

**BOTH, because `A8` requires both and an earlier draft named only the
second.**

**FIRST, AS A FACT ABOUT ACCESS: `OS78` was reachable only at ABSTRACT
depth.** The article body was not obtained. This is a limitation of what
the executor could reach, and it is not a judgement about the work. **The
arriving artifact records it plainly and marks six of its seven axis rows
`UNKNOWN AT ABSTRACT DEPTH` rather than `FAIL`** — an unfetched hypothesis
is unknown, not mismatched.

**SECOND, AND SEPARATELY: refusing to let it support `COVERED` is the
EVIDENTIAL CRITERION OPERATING CORRECTLY.** `D-1`'s specification says an
abstract cannot support `COVERED` unless the abstract itself states every
hypothesis the mapping needs. **`OS78`'s abstract reports physical
positivity for a lattice gauge/fermion construction and states none of the
reflection type, boundary conditions, or parameter restrictions the mapping
turns on.** The artifact confines it to "corroborating route evidence".

**The two statements are independent.** Better access would have removed
the first; nothing would have removed the second short of an abstract that
stated the hypotheses. **A report giving only the criterion would read as
if the audit chose not to use a work it could have used; a report giving
only the access limitation would read as if better network access would
have produced a `COVERED`. Neither alone is true.**

## 10. `A9` — scope, the two figures, and the arriving arithmetic

**MEASURED at commit 3, the merge commit:**

    A   derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md
    A   reports/2026-08-16T1952Z_d1-literature-coverage-audit.md
    A   reviews/chatgpt/2026-08-16T1952Z_d1-literature-coverage-audit.md
    A   reviews/chatgpt/2026-08-16T2121Z_integrate-d1-coverage.md
    A   specs/2026-08-16T1952Z_d1-literature-coverage-audit.md
    A   specs/2026-08-16T2121Z_integrate-d1-coverage.md

    6 additions, 0 modifications      MEASURED AT COMMIT 3

**INTENDED, base to commit 4: 7 additions and 0 modifications**, the
seventh being this report. **INTENDED and not MEASURED: this report is
written before the commit containing it.**

**Each figure carries the head it was measured at**, as `A9` requires.

**MEASURED: no status code other than `A` appears anywhere in the range.**
**`modify:` is `[]` and remained so** — this task modifies nothing, and
none of the forbidden operations occurs.

### 10.1 The arriving counts, stated separately

**MEASURED, `git diff --name-status b27926aa… f8fdcf64…`:**

    arriving PATHS           4
    arriving ADDITIONS       4
    arriving MODIFICATIONS   0

    THEY COINCIDE, at four.

**The guard does nothing here, and saying so is the point.** The two counts
differ only when a modification arrives. **One did in the immediately
preceding integration** — `tests/test_gate_pins.py`, where four arriving
paths were three additions — **and a task that had reported "four arriving
additions" there would have described the entire substance of that landing
as an addition.** **Reporting the coincidence keeps the distinction from
being quietly dropped by the next task in which it bites.**

**The arriving filenames carry the source's own `1952Z` token, which the
manifest could not know. MEASURED, they match the manifest in every
component but that token**, and `derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md`
matches exactly. **This task's three carry `2121Z`**, fixed once by commit
1 and reused. **I chose no path.**

## 11. `A11` — nothing existing changed

**MEASURED path by path over every path present at the evidence base:**

    paths at the evidence base      439
    compared                        439
    blob-identical                  439
    differing                         0
    missing at head                   0

    paths at head                   445   (439 + this range's six)

**ZERO differing. This range adds only, and modifies nothing.**

**The named paths, MEASURED individually — all IDENTICAL:**

    GATES.md                                                          IDENTICAL
    CONVENTIONS.md                                                    IDENTICAL
    docs/GOVERNANCE-DEBT.md                     (governance register) IDENTICAL
    docs/BRANCHING_POLICY.md                    (superseded register) IDENTICAL
    derivations/P2-DEFERRED-ITEMS.md            (deferred register)   IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md   IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md    IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md       IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md                IDENTICAL

    scripts/    60 paths,  0 changed
    tests/      21 paths,  0 changed
    results/    69 paths,  0 changed

**All four earlier microspec artifacts are unchanged**, including
`_tm-rp-scope.md`, which is the artifact `D-1` was written to correct.
**The audit lands BESIDE it and does not edit it** — the correction is a
new artifact, not a rewrite, and `B0`'s four recollections stay on the
record as recollections.

**No register entry was added anywhere.**

## 12. `A12` — gate invariants and pins

**MEASURED at commit 3, all four:**

    ^## P2- count                        14
    P2-PHASE-01                          Status: PROPOSED      (GATES.md:973)
    first prerequisite                   Prerequisite state: SATISFIED   (GATES.md:1011)
    second prerequisite                  Prerequisite state: SATISFIED   (GATES.md:1036)
    pin at line 1017                     MATCH
    pin at line 1040                     MATCH

**THE STATUS LINE WAS READ SCOPED TO ITS GATE SECTION, NOT BY A BARE
GREP**, as `A12` requires. The `P2-PHASE-01` heading is at `GATES.md:971`
and its status line at 973, read as an offset from that heading.

**MEASURED, for contrast and deliberately NOT used: a bare
`grep -n 'Status: PROPOSED' | head -1` returns line 209**, which belongs to
a different gate and reads `Status: PROPOSED (deferred — not computed this
sweep)`. **Seven hundred lines above the gate in question, and it would
have produced the right word from the wrong place.**

**The pins were verified by RECOMPUTING the target digests:**

    GATES.md:1017   4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
    sha256 derivations/P2-PHASE-01_microscopic_parameter_domain.md
                    4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214

    GATES.md:1040   e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
    sha256 derivations/P2-PHASE-01_input_admissibility_contract.md
                    e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3

**Both MATCH.**

## 13. `A13` — superseded branches, before the advance

**MEASURED at commit 3. Six separate exit statuses, all 1 — none is an
ancestor of the head:**

    52f65117  exit 1        7146a093  exit 1
    ebd531ab  exit 1        10c260b9  exit 1
    40168469  exit 1        d64cd912  exit 1

**The checker's `P4` independently reports `is_ancestor_of_head: false` and
`object_present: true` for all six.**

**The post-advance repetition is post-report evidence and is not claimed
here.**

## 14. `A14` — the checker, MEASURED at commit 3

    base   b27926aad0d3a1ef39f5e7e886f8571657c5687c
    head   c9efb4af66d53546d4421d0519fa5adbb2b0bce2   (commit 3, the merge commit)

    run 1 INCLUSIVE   exit 0   PASS   sha256 5673d56566802aa61b706c90b1f7ad790c5f76e6b92bae3b2a1603b5c438ea91
    run 1 EXCLUSIVE   exit 0   PASS   sha256 919e5742617253bb5ff17cd1658dc179666d16d7e8c057cf5dc253fcc28e9ca4
    run 2 INCLUSIVE   exit 0   PASS   sha256 91d4b3d732b5c5845ddb0c179b64e441fa9188569850a91f694d2a569c5bd2bc
    run 2 EXCLUSIVE   exit 0   PASS   sha256 ad60f59b6201c98444b3fd4c8156a1102fc8bd93b12e9fff84b2b803e7b02780

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 PASS
    P6 PASS   P7 PASS   P8 PASS   P9 PASS

    NINE OF NINE IN EVERY INVOCATION.  No property is NOT_APPLICABLE.

    commits_in_range               7
    commits_on_first_parent_line   3

### 14.1 What `RUN 1` did

**MEASURED: `RUN 1`'s default subject selection found BOTH specifications
in range and evaluated `P1` against each:**

    specs/2026-08-16T1952Z_d1-literature-coverage-audit.md   stated 4 add / 0 mod   counted 4 / 0   parse OK
    specs/2026-08-16T2121Z_integrate-d1-coverage.md          stated 7 add / 0 mod   counted 7 / 0   parse OK

**Both PASS. `RUN 2` names only this task's specification and evaluated
`P1` against that one alone**, which is why the two runs produce different
bytes.

**The `C3` multi-specification residual did NOT arise, and this is again
the discriminating case.** `_declarations_from_specs` raises when two
subject specifications in range declare DIFFERENT values for the same key.
**MEASURED: `P3` and `P7` both report `specification_paths_read` as BOTH
specifications, resolving to `['DECISION_LOG.md']` and `[]` respectively,
`declared_source: specification`.** **Two specifications, agreeing, and no
conflict — the trigger is a difference and not a count.** The residual is
unchanged and remains unregistered.

**`P1`'s `counted_set` holds each specification's own LITERAL manifest
paths, token placeholders and all.** That is `P1` working as specified — an
internal-consistency check on a specification, not a comparison against the
diff — and it is stated here so it is not mistaken for a discrepancy with
`§10`'s measured six.

### 14.2 `P5`, `P9` and `declared_source`

    P3   PASS   declared_source: specification   declared: ['DECISION_LOG.md']
    P7   PASS   declared_source: specification   section_count_head 14
    P9   PASS   reports/2026-08-16T1952Z_d1-literature-coverage-audit.md   heading_present: true

**`P7` reports FOURTEEN sections at both base and head. `PASS` at zero
would have been a STOP, and it is not zero.**

**MEASURED: `DECLARATION_CONFLICT` appears ZERO times in all four
outputs.**

**`DECISION_LOG.md` is not modified by this range**, so `P3` passed without
exercising the append property; it still reports
`base_is_byte_prefix_of_head: true` over 89541 identical bytes.

**`P5` recomputed the parentage independently** — merge-base `b27926aa…`,
parent 1 `c2f4a27f…`, parent 2 `f8fdcf64…` — **and reports
`compared_to_recorded: UNAVAILABLE`, because the merge commit records no
parentage values in its message.** **So `P5` verified internal coherence,
not agreement with anything I wrote down**; `§6`'s three separately derived
values are the independent measurement.

**`P9` found the ARRIVING report and confirmed its `Stops and
clarifications` heading.** It could not have done so in the source task's
own range, where the report did not exist at the head being checked.

### 14.3 `RUN 1` config, verbatim — observational, governs nothing

    {
      "base": "b27926aad0d3a1ef39f5e7e886f8571657c5687c",
      "head": "c9efb4af66d53546d4421d0519fa5adbb2b0bce2",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 14.4 `RUN 2` config, verbatim — stop-governing

    {
      "base": "b27926aad0d3a1ef39f5e7e886f8571657c5687c",
      "head": "c9efb4af66d53546d4421d0519fa5adbb2b0bce2",
      "specification_paths": ["specs/2026-08-16T2121Z_integrate-d1-coverage.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

**No value in either config is one I chose**, and **neither the config nor
this specification's declarations were adjusted to make `RUN 2` pass** —
`§8` forbids both. **`RUN 2` passed on its first invocation at both
readings.**

### 14.5 `RUN 1` output, verbatim, `INCLUSIVE` reading

    {
      "base": "b27926aad0d3a1ef39f5e7e886f8571657c5687c",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "c9efb4af66d53546d4421d0519fa5adbb2b0bce2",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "append_only": [
                "DECISION_LOG.md"
              ],
              "authorised_gates": [],
              "counted": 4,
              "counted_add": 4,
              "counted_modify": 0,
              "counted_set": [
                "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md",
                "reports/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md",
                "specs/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md",
              "stated": 4,
              "stated_add": 4,
              "stated_modify": 0,
              "stated_record": "stated: 4 additions, 0 modifications"
            },
            {
              "append_only": [
                "DECISION_LOG.md"
              ],
              "authorised_gates": [],
              "counted": 7,
              "counted_add": 7,
              "counted_modify": 0,
              "counted_set": [
                "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md",
                "reports/2026-08-16T1952Z_d1-literature-coverage-audit.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-d1-coverage.md",
                "reviews/chatgpt/2026-08-16T1952Z_d1-literature-coverage-audit.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-d1-coverage.md",
                "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-d1-coverage.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-16T2121Z_integrate-d1-coverage.md",
              "stated": 7,
              "stated_add": 7,
              "stated_modify": 0,
              "stated_record": "stated: 7 additions, 0 modifications"
            }
          ],
          "id": "P1",
          "status": "PASS",
          "title": "scope manifest arithmetic"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "commits": [
              {
                "adds_review": false,
                "commit": "88aacd62ea86a5025e1323038e0aae9d2abcadb0",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "c2f4a27fad61bd734daadc6e49059783b6c205b6",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "c9efb4af66d53546d4421d0519fa5adbb2b0bce2",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md"
                ]
              }
            ],
            "first_review_commit": "c2f4a27fad61bd734daadc6e49059783b6c205b6",
            "first_work_commit": "c9efb4af66d53546d4421d0519fa5adbb2b0bce2",
            "in_scope": 3,
            "out_of_scope": []
          },
          "id": "P2",
          "status": "PASS",
          "title": "Rule 15 commit order"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
          "evidence": {
            "declared": [
              "DECISION_LOG.md"
            ],
            "declared_by_specification": [
              "DECISION_LOG.md"
            ],
            "declared_key": "append_only",
            "declared_source": "specification",
            "paths": [
              {
                "base_bytes": 89541,
                "base_is_byte_prefix_of_head": true,
                "commits_with_deletions": [],
                "deleted_lines_base_to_head": 0,
                "head_bytes": 89541,
                "path": "DECISION_LOG.md",
                "status": "PASS"
              }
            ],
            "specification_paths_read": [
              "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md",
              "specs/2026-08-16T2121Z_integrate-d1-coverage.md"
            ],
            "supplied_by_config": [
              "DECISION_LOG.md"
            ]
          },
          "id": "P3",
          "status": "PASS",
          "title": "append-only on both measures"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "entries": [
              {
                "branch": "fix/pi-decisions-and-deferred",
                "commit": "52f651174dc1fef03b4fb9276078fa1f08d94bd7",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "fix/pi-decisions-v2",
                "commit": "ebd531ab568aaffabd86a4a94d925a711e62aa36",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-v2",
                "commit": "40168469608618aef6812735ff70e32de0e3cbc8",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-and-superseded",
                "commit": "7146a093c65788a57d63a747b71d86edb91eddc6",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "review/role-model-and-executors",
                "commit": "10c260b96882ac12610f78840aeeabd07be2d7cb",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "gate/p2-land-diquark-line",
                "commit": "d64cd912ca9ff78a85787f0e54f345f474cdb192",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              }
            ],
            "register_path": "docs/BRANCHING_POLICY.md"
          },
          "id": "P4",
          "status": "PASS",
          "title": "superseded branches are not merged"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the executor derived the parentage values independently; three correct values are equally consistent with fresh recomputation and with one field copied into another. The diquark task's shared-rationale defect would pass this check.",
          "evidence": [
            {
              "compared_to_recorded": "UNAVAILABLE",
              "merge": "c9efb4af66d53546d4421d0519fa5adbb2b0bce2",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "b27926aad0d3a1ef39f5e7e886f8571657c5687c",
              "recomputed_parent_1": "c2f4a27fad61bd734daadc6e49059783b6c205b6",
              "recomputed_parent_2": "f8fdcf64e4106fff3958ae726237e4aec453af04",
              "status": "PASS"
            }
          ],
          "id": "P5",
          "status": "PASS",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "88aacd62ea86a5025e1323038e0aae9d2abcadb0",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "c2f4a27fad61bd734daadc6e49059783b6c205b6",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "5d76e4026df421d41b385062b4b0dbaa203e6227",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "37d1a7e719f4016de61ace3756fd8a0c2105cf1f",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "f8fdcf64e4106fff3958ae726237e4aec453af04",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "c9efb4af66d53546d4421d0519fa5adbb2b0bce2",
              "matches": [],
              "status": "PASS"
            }
          ],
          "id": "P6",
          "status": "PASS",
          "title": "commit-message hygiene"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
          "evidence": {
            "added_sections": [],
            "authorised_modified": [],
            "declared": [],
            "declared_by_specification": [],
            "declared_key": "authorised_gates",
            "declared_source": "specification",
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "specification_paths_read": [
              "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md",
              "specs/2026-08-16T2121Z_integrate-d1-coverage.md"
            ],
            "supplied_by_config": [],
            "unauthorised_changed": []
          },
          "id": "P7",
          "status": "PASS",
          "title": "gate integrity"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "first_commit": "88aacd62ea86a5025e1323038e0aae9d2abcadb0",
            "first_commit_paths": [
              "specs/2026-08-16T2121Z_integrate-d1-coverage.md"
            ],
            "reports_added": [
              "reports/2026-08-16T1952Z_d1-literature-coverage-audit.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-16T2121Z_integrate-d1-coverage.md",
              "reviews/chatgpt/2026-08-16T1952Z_d1-literature-coverage-audit.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-16T2121Z_integrate-d1-coverage.md",
              "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": [
            {
              "heading_present": true,
              "path": "reports/2026-08-16T1952Z_d1-literature-coverage-audit.md",
              "status": "PASS"
            }
          ],
          "id": "P9",
          "status": "PASS",
          "title": "reports carry a Stops and clarifications section"
        }
      ],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 3,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

### 14.6 `RUN 2` output, verbatim, `INCLUSIVE` reading

    {
      "base": "b27926aad0d3a1ef39f5e7e886f8571657c5687c",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "c9efb4af66d53546d4421d0519fa5adbb2b0bce2",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "append_only": [
                "DECISION_LOG.md"
              ],
              "authorised_gates": [],
              "counted": 7,
              "counted_add": 7,
              "counted_modify": 0,
              "counted_set": [
                "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md",
                "reports/2026-08-16T1952Z_d1-literature-coverage-audit.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-d1-coverage.md",
                "reviews/chatgpt/2026-08-16T1952Z_d1-literature-coverage-audit.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-d1-coverage.md",
                "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-d1-coverage.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-16T2121Z_integrate-d1-coverage.md",
              "stated": 7,
              "stated_add": 7,
              "stated_modify": 0,
              "stated_record": "stated: 7 additions, 0 modifications"
            }
          ],
          "id": "P1",
          "status": "PASS",
          "title": "scope manifest arithmetic"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "commits": [
              {
                "adds_review": false,
                "commit": "88aacd62ea86a5025e1323038e0aae9d2abcadb0",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "c2f4a27fad61bd734daadc6e49059783b6c205b6",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "c9efb4af66d53546d4421d0519fa5adbb2b0bce2",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md"
                ]
              }
            ],
            "first_review_commit": "c2f4a27fad61bd734daadc6e49059783b6c205b6",
            "first_work_commit": "c9efb4af66d53546d4421d0519fa5adbb2b0bce2",
            "in_scope": 3,
            "out_of_scope": []
          },
          "id": "P2",
          "status": "PASS",
          "title": "Rule 15 commit order"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
          "evidence": {
            "declared": [
              "DECISION_LOG.md"
            ],
            "declared_by_specification": [
              "DECISION_LOG.md"
            ],
            "declared_key": "append_only",
            "declared_source": "specification",
            "paths": [
              {
                "base_bytes": 89541,
                "base_is_byte_prefix_of_head": true,
                "commits_with_deletions": [],
                "deleted_lines_base_to_head": 0,
                "head_bytes": 89541,
                "path": "DECISION_LOG.md",
                "status": "PASS"
              }
            ],
            "specification_paths_read": [
              "specs/2026-08-16T2121Z_integrate-d1-coverage.md"
            ],
            "supplied_by_config": [
              "DECISION_LOG.md"
            ]
          },
          "id": "P3",
          "status": "PASS",
          "title": "append-only on both measures"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "entries": [
              {
                "branch": "fix/pi-decisions-and-deferred",
                "commit": "52f651174dc1fef03b4fb9276078fa1f08d94bd7",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "fix/pi-decisions-v2",
                "commit": "ebd531ab568aaffabd86a4a94d925a711e62aa36",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-v2",
                "commit": "40168469608618aef6812735ff70e32de0e3cbc8",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-and-superseded",
                "commit": "7146a093c65788a57d63a747b71d86edb91eddc6",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "review/role-model-and-executors",
                "commit": "10c260b96882ac12610f78840aeeabd07be2d7cb",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "gate/p2-land-diquark-line",
                "commit": "d64cd912ca9ff78a85787f0e54f345f474cdb192",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              }
            ],
            "register_path": "docs/BRANCHING_POLICY.md"
          },
          "id": "P4",
          "status": "PASS",
          "title": "superseded branches are not merged"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the executor derived the parentage values independently; three correct values are equally consistent with fresh recomputation and with one field copied into another. The diquark task's shared-rationale defect would pass this check.",
          "evidence": [
            {
              "compared_to_recorded": "UNAVAILABLE",
              "merge": "c9efb4af66d53546d4421d0519fa5adbb2b0bce2",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "b27926aad0d3a1ef39f5e7e886f8571657c5687c",
              "recomputed_parent_1": "c2f4a27fad61bd734daadc6e49059783b6c205b6",
              "recomputed_parent_2": "f8fdcf64e4106fff3958ae726237e4aec453af04",
              "status": "PASS"
            }
          ],
          "id": "P5",
          "status": "PASS",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "88aacd62ea86a5025e1323038e0aae9d2abcadb0",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "c2f4a27fad61bd734daadc6e49059783b6c205b6",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "5d76e4026df421d41b385062b4b0dbaa203e6227",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "37d1a7e719f4016de61ace3756fd8a0c2105cf1f",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "86e2710ca3f04715519bd82b2fd8cac21274a75e",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "f8fdcf64e4106fff3958ae726237e4aec453af04",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "c9efb4af66d53546d4421d0519fa5adbb2b0bce2",
              "matches": [],
              "status": "PASS"
            }
          ],
          "id": "P6",
          "status": "PASS",
          "title": "commit-message hygiene"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
          "evidence": {
            "added_sections": [],
            "authorised_modified": [],
            "declared": [],
            "declared_by_specification": [],
            "declared_key": "authorised_gates",
            "declared_source": "specification",
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "specification_paths_read": [
              "specs/2026-08-16T2121Z_integrate-d1-coverage.md"
            ],
            "supplied_by_config": [],
            "unauthorised_changed": []
          },
          "id": "P7",
          "status": "PASS",
          "title": "gate integrity"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "first_commit": "88aacd62ea86a5025e1323038e0aae9d2abcadb0",
            "first_commit_paths": [
              "specs/2026-08-16T2121Z_integrate-d1-coverage.md"
            ],
            "reports_added": [
              "reports/2026-08-16T1952Z_d1-literature-coverage-audit.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-16T2121Z_integrate-d1-coverage.md",
              "reviews/chatgpt/2026-08-16T1952Z_d1-literature-coverage-audit.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-16T2121Z_integrate-d1-coverage.md",
              "specs/2026-08-16T1952Z_d1-literature-coverage-audit.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": [
            {
              "heading_present": true,
              "path": "reports/2026-08-16T1952Z_d1-literature-coverage-audit.md",
              "status": "PASS"
            }
          ],
          "id": "P9",
          "status": "PASS",
          "title": "reports carry a Stops and clarifications section"
        }
      ],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 3,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

### 14.7 The `EXCLUSIVE` readings

**MEASURED by `diff`, and this is the whole of the difference:**

    run 1   line 314 of 318:   "inclusivity": "INCLUSIVE"  →  "EXCLUSIVE"
    run 2   line 291 of 295:   "inclusivity": "INCLUSIVE"  →  "EXCLUSIVE"

**One line each, and nothing else.** No property status, evidence field or
scope figure differs between the readings, and `commits_out_of_scope` is
empty in all four.

## 15. `A15`, `A16`, `A17` — validators, Ruff, hygiene

**`A15`, MEASURED at commit 3, `python -m pytest` from the repository root,
exit status 0:**

    324 passed, 2 deselected      in 37.87 s

**Expected 324 and 2; measured 324 and 2. No change, and therefore no
finding.**

**`A16`, MEASURED, `ruff check .` — THIRTEEN findings, reported and
UNTOUCHED:**

    scripts/euclidean_reconstruction.py                8
        I001 import block un-sorted                            line 6
        E702 multiple statements on one line (semicolon)       lines 38, 48
        E501 line too long                                     lines 39, 55, 56, 63, 74
    tests/test_task_checker.py                         3
        E501 line too long                                     lines 625, 647, 657
    scripts/governance_tools/task_checker.py           1
        E741 ambiguous variable name `l`                       line 741
    tests/test_repository_structure.py                 1
        F401 `re` imported but unused                          line 8
                                                      --
                                                      13

**NONE was introduced or modified by the source task or by this one, and
the proof is structural rather than a comparison of counts:** **every
finding is in a `.py` file, and MEASURED, every path this range touches is
a `.md` file** — six additions, all Markdown. **`A11` confirms it
independently: `scripts/` 0 changed, `tests/` 0 changed.**

**They were NOT repaired and no lint configuration was added.** Two are
marked auto-fixable by Ruff, which is exactly the shape of an
opportunistic edit, and `§4` forbids it.

**`A17`, MEASURED on commits 1–3. Commit 4 is post-report evidence:**

    commit 1   88aacd62   spec: integrate the reflection-positivity literature coverage audit, and land it
               trailer hits 0      not amended
    commit 2   c2f4a27f   review: pre-execution review for the literature coverage integration
               trailer hits 0      not amended
    commit 3   c9efb4af   merge: integrate the reflection-positivity literature coverage audit
               trailer hits 0      not amended

**MEASURED over the whole range, including the arriving commits: a scan for
`Co-Authored-By`, `claude.ai/code`, `Generated with`, `Claude-Session` and
`noreply@anthropic` returns ZERO.** **`P6` independently reports
`matches: []` for every commit in range.**

**Rule 20 binds this task and was NOT exercised.** **No force-push, no
branch deletion, no history rewrite of any kind.**

**Commits, MEASURED:**

    commit 1   88aacd62ea86a5025e1323038e0aae9d2abcadb0   specs/2026-08-16T2121Z_integrate-d1-coverage.md
    commit 2   c2f4a27fad61bd734daadc6e49059783b6c205b6   reviews/chatgpt/2026-08-16T2121Z_integrate-d1-coverage.md
    commit 3   c9efb4af66d53546d4421d0519fa5adbb2b0bce2   --no-ff merge of f8fdcf64…

**Commit 4's message, INTENDED:**

    report: the reflection-positivity literature coverage audit lands on main

## 16. `§7` — Rule 16 assessment

**Rule 16 is operative. All four junctions are addressed.**

### 16.1 First junction — zero verdict-level discrimination, and what it DID deliver

**Four uniform `PARTIAL` verdicts provide ZERO VERDICT-LEVEL
DISCRIMINATION for operator selection**, just as `B0`'s four uniform `NOT
ESTABLISHED` statuses did, and as the dossier's four uniform results did
before that. **Reading four identical verdicts as a fact about the
candidates is reading noise.**

**AND THAT IS NOT THE SAME AS SAYING THE AUDIT ADDED NOTHING.** It added a
great deal that is not verdict-level:

    ten fetched works at recorded evidential depths, 8 full text and 2 abstract
    candidate-specific applicability declarations for every fetched work
    per-basis seven-axis and theorem-hypothesis mappings
    named, inspected unmatched hypotheses per candidate — raw FAIL material
    ROUTE EVIDENCE kept explicitly outside proposition (ii)
    B0's L3 naming gap filled by a named and inspected theorem

**Saying they "discriminate exactly as little" would erase all of that.**
The verdicts are uniform; **the material underneath them is not.**

**The audit removed ZERO construction units.** **A reader may take a
completed audit for progress toward selecting an operator, and it is
not.** **What it delivered is a much better-characterised description of
what remains — not less remaining work.**

**And `§2`'s three-way gap classification is NOT performed here.** It is
deferred to `D-1b`, so **this landing carries no statement about which gaps
are which.**

### 16.2 Second junction — `PARTIAL` is not "nearly covered"

**`PARTIAL` means a relevant theorem exists and at least one material
hypothesis is unmatched. It does NOT mean the remaining extension is
small.**

**Nothing landed here establishes that any remaining extension is small,
large, or anything in between.** **`§2`'s taxonomy is recorded and not
applied, so this landing carries NO statement about which gaps are
cheap.** **`D-1b` is where that question is asked.**

**And nothing here establishes that any missing mathematics does not
exist.** **`D-1` established that the FETCHED literature does not supply
it** — a bounded search, and **its bound is part of its result, not a
caveat on it.** The arriving artifact says so in its own closing note:
absence of `COVERED` "is not an exhaustive non-existence claim."

**The two failure modes this junction guards against are opposite and both
are live**: reading `PARTIAL` as *almost there*, and reading it as *proved
impossible*. **Neither is supported.**

### 16.3 Third junction — seeds, not a boundary

**MEASURED: FIVE of the TEN fetched works were OUTSIDE `B0`'s five-work
named seed set, and THREE of those five became load-bearing applicability
bases** — `MP87`, `KU10`, `FG26`.

**Every basis carrying a verdict is an outside-seed work.** **A
boundary-scoped audit would have missed all of them**, and would have
returned `NO COVERAGE FOUND` or `NOT DETERMINABLE` across the board while
the relevant theorems sat unread.

**`D-1`'s `§6` decision to treat `B0`'s claims as SEARCH SEEDS rather than
a hard boundary is what allowed them in**, and the reason that decision was
made is that **`B0`'s claims were RECALL** — four entries marked
`UNVERIFIED FROM THIS REPOSITORY`, one of them naming no work at all.
**An audit whose answer was a function of `B0`'s memory would have been
biased toward `NO COVERAGE FOUND` in exactly the rows where `B0` recalled
least.**

**NOTHING ESTABLISHES THAT THE RESULTING SEARCH WAS EXHAUSTIVE.** Ten works
were fetched and one more was encountered and left unfetched. **The
seeds-not-boundary decision widened the search; it did not close it**, and
a further applicable work may exist and be unfound.

### 16.4 Fourth junction — what the process cost, and what that does not establish

**`D-1` took THREE EXECUTIONS, THREE PREFLIGHT STOPS, and EIGHT
SPECIFICATION REVISIONS.**

    execution 1    …-audit @ 8267bd40      STOP at §1, sandbox egress
    preflight 2a   stale local refs/heads/main
    preflight 2b   wrong repository
    execution 2    …-audit-2 @ a537e036    STOP at A14, the pin test
    preflight 3a   branch-name occupancy
    execution 3    …-audit-3 @ f8fdcf64    COMPLETE

**NONE of the eight revisions concerned the literature audit itself.** They
concerned repository identity, ref semantics, branch naming, execution
order, provenance vocabulary, and environment preconditions — **the
specification's ASSUMPTIONS ABOUT THE EXECUTION ENVIRONMENT, not its
science.**

**Every revision fixed a real defect, and every one was caught.** The
scientific method the audit ran on its third execution is substantially the
method its first execution was given.

**NOTHING ESTABLISHES THAT THE REMAINING ASSUMPTIONS HAVE BEEN FOUND.**
Six failures were each discovered by hitting them, not by an audit of the
assumption set. **The preceding task in this line found another one the
same way** — a suite result that meant nothing until Rule 13's diagnostic
order had been run — **and there is no reason to think the sequence has
terminated.**

**And the honest sharpening: three of the six stops were about WHICH
REPOSITORY AND WHICH REF**, which is the kind of assumption nobody writes
down because it seems too basic to state. **Those are the assumptions least
likely to have been exhausted.**

## 17. Stops and clarifications

**NO STOP occurred.** The merge was clean, all four checker invocations
exited 0, `RUN 2` passed at both prospectivity readings, the conflict list
was empty, and no acceptance criterion failed.

    SPECIFICATION_DEFECT                          0 stops, 0 findings
    ENVIRONMENT                                   0 stops, 0 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 1 finding
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 3 findings

### 17.1 `ENVIRONMENT` — nothing to report

**No environment failure occurred.** The container was conformant on
arrival, `§1`. **Neither of Rule 13's two diagnostic orders was
exercised**, and I am not naming one as having applied. **Nothing was
installed by this task.**

### 17.2 `REPOSITORY_DEFECT` — nothing to report

**No defect in the repository was found by this task.** Every path at the
evidence base is blob-identical at the head; the gate invariants hold; both
pins recompute; the checker passes nine of nine at both readings; the
validators are unchanged at 324 passed, 2 deselected.

**The thirteen Ruff findings are pre-existing and are NOT counted as a
defect found here**, `§15`. They were present before this range, are
untouched by it, and `§4` forbids repairing them.

### 17.3 `SPECIFICATION_DEFECT` — nothing to report

**Nothing in this specification was found false about the repository or
about its own bytes.** Its pre-issue record was checked at seven points —
the base, the source tip and its non-ancestry, merge cleanliness and
merge-base, the 6/0 figure at the merge commit, the arriving 4/0 scope, the
verdicts and accounting, and the ten-work ledger with its five outside-seed
and three load-bearing counts — **and MEASURED agrees with it at every
one.**

**Its `§1` RETRACTION is itself correct.** An earlier draft said seven
fetched and three outside the seed set; **MEASURED, it is ten and five, and
three is the count of outside-seed works that became load-bearing bases.**
**I verified the retraction by parsing the ledger rather than by trusting
it.**

**The `…-audit-2` clause in `A1` is the one place the specification asserts
something the repository does not bear out**, and it is carried at `§17.4`
rather than here, because what is missing is a BRANCH rather than a
statement about the specification's own content.

### 17.4 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — first finding

**`science/d1-literature-coverage-audit-2` does not exist on the remote,
and commit `a537e036` is not a resolvable object in this repository**,
`§2.1`. **`A1` asks me to confirm it "still exists and is unchanged", and I
cannot.**

**I did not touch it, and there is nothing here to establish what
happened** — whether execution 2's branch was never pushed, or was pushed
and later removed. **This report states only what was measured.**

**The consequence is a provenance gap and it is worth naming precisely:**
**execution 2's record — its stop at `A14`, on the pin test this
programme then repaired — exists only in the landed specification's `§0`
prose.** **No commit, no report, and no branch backs it.** That is adjacent
to `G-03`, which records that corrections are not discoverable from what
they correct: **here the correction is discoverable and the thing corrected
is not.**

**Reported, NOT registered** — `§4` forbids adding a register entry and the
governance debt register is frozen at eleven.

### 17.5 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — second finding

**The landed specification's pre-issue record contradicts its own normative
`A7`**, `§3`. `§10` says *"`A7` requires the classification derived from
the tables"*; the normative `A7` forbids this task from classifying at all.

**The Reviewer caught this and recorded it as a non-blocking editorial
residue, and I agree with that disposition.** **I followed the normative
`A7`.** **But the two readings land on `main` together, and a later reader
consulting the verification record rather than the criterion would draw the
opposite instruction.**

**This is the `G-08` shape** — a specification asserting something false
about its own bytes — **arriving in a document whose review already
identified it.** **Reported, NOT registered.**

### 17.6 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — third finding

**The Windows behaviour of the test repaired in the preceding integration
remains `DERIVED` and unmeasured**, and it is relevant here because
**execution 2 of `D-1` stopped on that very test.** **Nothing in this task
verifies that the repair actually unblocks a Windows execution**; what is
established is that execution 3 completed on Linux, where the test passed
before the repair as well.

**Carried forward, NOT registered.**

### 17.7 `OBSERVATION_METHOD_ERROR` — one finding, mine, caught within the task

**My first instinct on `A7`'s "count the `FAIL` entries" was to run a
single whole-file `grep -c` for the token.** That would have returned one
number and it would have been wrong in three separate ways: **it would have
counted the legend line that DEFINES `FAIL`; it would have merged
`UNKNOWN AT ABSTRACT DEPTH` in or out without saying which; and it would
have given no per-candidate attribution at all**, which is the only form
`A7` asks for.

**Corrected within the task by parsing the artifact structurally** — basis
block by basis block, table rows separated from hypothesis prose, legend
excluded, `UNKNOWN AT ABSTRACT DEPTH` counted separately — **and the
counting rule is stated in `§8.1` so the figures can be reproduced or
disputed.**

**Recorded because this line has met the whole-file-grep hazard before.**
`D-pre-B0`'s integration found that whole-file greps returning 17, 5 and 6
were not cell counts of 12 and 0, and the sharpest case there was
`REFUTED`: five occurrences, zero cells, every occurrence a definition or a
denial. **The same shape, one task later, in a different artifact.**

### 17.8 What I would have specified differently

**`A7` says "the count of `FAIL` entries in the arriving tables" and does
not define an entry.** The artifact has axis-table rows, theorem-hypothesis
prose sentences, and per-candidate bullet lists, and `FAIL` appears in all
three. **I would have had `A7` name which of the three it means, and say
explicitly whether `UNKNOWN AT ABSTRACT DEPTH` counts** — otherwise two
careful executors produce different numbers and both are right.

**And `A1`'s branch clause states an expectation rather than asking a
question.** "Report that `…-audit-2` still exists and is unchanged"
presumes the answer. **I would have had it say: report whether each earlier
`D-1` branch exists, and its tip if it does** — which is answerable either
way and which would have made `§17.4` a measurement rather than a
discrepancy.

## 18. Did landing a completed audit make me want to select a candidate, design a route, or repair the Ruff findings?

**Three temptations, of very different strengths. None acted on.**

**Selecting a candidate: weak, and structurally so.** Four uniform
`PARTIAL` verdicts give nothing to select on — **the uniformity that makes
the result undiscriminating also makes the temptation empty.** **The one
place it flickered was the sentence "every basis carrying a verdict is an
outside-seed work"**: `MP87` covers Wilson and naive, `FG26` covers naive
and staggered, `KU10` covers overlap alone, and it is easy to slide from
*more works bear on this candidate* to *this candidate is better
supported*. **That slide is precisely what `§4` forbids and what `§16.1`
answers: coverage is a fact about what other people studied.** **I wrote
the counts and drew no conclusion from their distribution.**

**Designing a route: moderate, and it arrived through `A7`.** Reading six
axis tables in a row, the shape of what is missing becomes vivid — the
determinant-reflection and Grassmann-factorization junctions recur across
`FG26`'s two bases and `KU10`'s, and it is tempting to observe that one
lemma might serve several. **That observation IS a route sketch**, and it
would have been a stronger claim than either of the two `§4` forbids.
**Not written, and not written anywhere in this report.**

**Repairing the Ruff findings: the strongest, and the most banal.** Two of
the thirteen are auto-fixable, the command is one word, the suite would
still be green, and the diff would be four lines. **That is exactly the
profile of the change that arrives without a specification** — small enough
that objecting to it feels pedantic. **The preceding task in this line
recorded the identical pull about a `conftest.py` helper and declined it
for the identical reason**, and the reason is worth restating: **a
repository where small unreviewed edits ride along with landings is one
where provenance stops meaning anything, and the smallness is what makes it
plausible rather than what makes it safe.**

**I confirm: I selected, eliminated, ranked and preferred no candidate;
designed no proof route and made no statement about how large any remaining
extension is; did not perform `§2`'s classification and assigned no tag to
any `FAIL` entry; did not re-derive or revise `B0`'s seven-to-eleven
estimate; repaired none of the thirteen Ruff findings and added no lint
configuration; modified no file; added no register entry; deleted, reset,
reused and moved no earlier `D-1` branch; pushed no session branch; and
made exactly one merge, with no rebase, no squash and no fast-forward at
the integration.**

## 19. Evidence layering

**Committed in this report, MEASURED at commit 3:** `A1`–`A13` and
`A15`–`A17` for commits 1–3; `A9`'s scope base-to-commit-3 at 6 additions
and 0 modifications, and the arriving counts; `A14`'s four invocations with
both configs and both runs' output verbatim; commits 1–3 SHAs and their
stored messages.

**Committed in this report, INTENDED:** commit 4's message; `A9`'s final
base-to-commit-4 scope of 7 additions and 0 modifications.

**Post-report evidence, returned to the Reviewer and NOT written back:**
`A9`'s final scope measured base-to-commit-4; `A14-final`, being `RUN 2`
re-run at commit 4 BEFORE the landing; `A12` and `A13` re-run after the
advance; `A17` for commit 4; the pre-advance `--is-ancestor` exit status;
the exact push command; remote `main` read back; the source tip unchanged;
confirmation that no other ref was pushed; final ancestry confirmation.

**Nothing in this report claims to measure commit 4.**
