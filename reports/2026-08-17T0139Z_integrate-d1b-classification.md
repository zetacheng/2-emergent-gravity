# Report — integrate the reflection-positivity gap classification, and land it

    branch      science/integrate-d1b-classification
    base        822cd4fbfe9bff6e43867caed95c5635344683d0   (authoritative main)
    source      science/d1b-rp-gap-classification @ 242b2f35d7d93c737ca15ffd654b272142c7ef55
    measured at commit 3, c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f   (the merge commit)

**One merge, no conflict. Six additions, ZERO modifications. Nothing is
modified — and not `D-1`'s tables.**

---

## 1. `A3` — environment conformance, and it ran FIRST

**The normative execution order, as `A3` states it, and the order actually
followed:**

    A3  environment conformance      ran first
    A1  repository identity and refs ran second
    A2  review binding               ran third
    A4  onward

**Criterion numbering is not execution order, and I followed the order the
specification states rather than the order the numbers suggest.**

    (0) execution location    /home/user/2-emergent-gravity; work in the
                              science/integrate-d1b-classification worktree cut
                              from 822cd4fb… by explicit SHA. MEASURED: five
                              worktrees present. SAME CONTAINER as the four
                              preceding tasks.
    (1) execution identity    root, uid 0
    (2) interpreter           Python 3.11.15 at /usr/local/bin/python
    (3) permissions           repository writable; no permission failure
    (4) filesystem/workspace  MEASURED: `git rev-parse --is-shallow-repository`
                              → false. No `.git/shallow`. 439 commits on the
                              authoritative line. NOT SHALLOW.
    (5) package availability  MEASURED: pytest 9.1.1, numpy 2.4.6,
                              sympy 1.14.0, ruff 0.15.8 — all four declared
                              packages present and importable.

**NO RESTORATION WAS NEEDED AND NONE WAS PERFORMED. No repository content
was touched by this criterion.**

**`A3`'s overlap with `A1` is intended and it did work here.** Step 0
records the workspace location; **`A1` records that it is the RIGHT
repository.** A conformant environment pointing at the wrong repository
passes `A3` and fails `A1` — **and this line has met that**, as preflight
`2b` of the `D-1` sequence.

**Rule 13 carries two diagnostic orders, a known open item. NO ENVIRONMENT
FAILURE OCCURRED**, and **neither order was exercised** — I am not naming
one as having applied. The order above was run as `A3`'s conformance check,
not in response to a failure.

## 2. `A1` — repository and refs

**MEASURED, VERBATIM and NOT normalised:**

    git remote get-url origin        https://github.com/zetacheng/2-emergent-gravity

**No `.git` suffix. `A1` accepts either form, and it identifies
`zetacheng/2-emergent-gravity`.**

**Refs, MEASURED after fetching:**

    refs/remotes/origin/main                              822cd4fbfe9bff6e43867caed95c5635344683d0
    refs/heads/main                                       1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    science/d1b-rp-gap-classification (remote)            242b2f35d7d93c737ca15ffd654b272142c7ef55

**`refs/remotes/origin/main` is `822cd4fb…`, as the evidence base requires.
No stop.** **`refs/heads/main` lags, and `A1` says a lagging local ref is
not a stop.** Every measurement here reads the remote-tracking ref or an
explicit SHA.

**MEASURED: the source is NOT an ancestor of `main`.**

    git merge-base --is-ancestor 242b2f35… refs/remotes/origin/main
    exit status 1   →  NOT an ancestor

## 3. `A2` — the pre-execution review

**MEASURED.**

    field `Reviewed specification SHA-256:` PRESENT   yes, line 4
    value carried by the review                       554eb2f8173a2fd5a2a13c417777db2fe639827303cc9b8b590d01800b7c0977
    SHA-256 of the committed specification bytes      554eb2f8173a2fd5a2a13c417777db2fe639827303cc9b8b590d01800b7c0977
    MATCH                                             yes
    review verdict                                    APPROVE FOR EXECUTION
    committed unedited                                yes — byte-identical to the supplied review

**The field's presence was checked before its value was compared.**

## 4. `A12` — which merge case, stated BEFORE the blob comparisons

**MEASURED, before the merge was made:**

    merge-base(origin/main, 242b2f35…)                822cd4fbfe9bff6e43867caed95c5635344683d0
    commits on main after the base                    0

**The merge-base IS the evidence base, and `main` carries no commit after
it, so no commit on `main` could have touched an arriving path.** The merge
is one-sided, and that is what makes the comparison below mean what it
appears to mean.

**NOW the comparisons, MEASURED at the merge commit against `242b2f35…`:**

    derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md      IDENTICAL
    reports/2026-08-16T2255Z_d1b-rp-gap-classification.md             IDENTICAL
    reviews/chatgpt/2026-08-16T2255Z_d1b-rp-gap-classification.md     IDENTICAL
    specs/2026-08-16T2255Z_d1b-rp-gap-classification.md               IDENTICAL

**All four arriving paths blob-identical. Nothing arriving was altered in
transit, and no path was renamed.**

## 5. `A5` — no conflict

**MEASURED, `git diff --name-only --diff-filter=U` at the merge:**

    (empty)      conflict entries    0

**`git status --porcelain` reports no unmerged entry.** The merge was clean,
matching the Researcher's dry run. **`§0` makes any conflict an immediate
stop; none arose.**

## 6. `A4` — merge parentage, three separately derived measurements

    merge commit                              c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f
    parent 1   git rev-parse HEAD^1           4f0e33d812baf5816d58ee467d039de5cabe31b1
    parent 2   git rev-parse HEAD^2           242b2f35d7d93c737ca15ffd654b272142c7ef55
    merge-base git merge-base HEAD^1 HEAD^2   822cd4fbfe9bff6e43867caed95c5635344683d0

**Parent 1 IS this task's review commit. Parent 2 IS the specified source
tip. The merge-base IS the evidence base.**

**Commit 1 is an ancestor of parent 1, MEASURED:**

    git merge-base --is-ancestor 7098e228cb80cb1876d2d2844727e93efd0993c4 HEAD^1      exit status 0   →  YES

**The checker's `P5` independently recomputed all three and agrees**, and
reports `compared_to_recorded: UNAVAILABLE` — the merge commit records no
parentage values in its message, so `P5` verified internal coherence and
not agreement with anything I wrote down. **The three values above are the
independent measurement, each from its own command.**

## 7. `A6` — the interceptions, re-derived from the repository

**This is the finding that justified splitting `D-1b` from the `D-1`
integration, and it is re-derived here from the repository and the arriving
tables — NOT quoted from the source report.**

### 7.1 The per-term, per-file occurrence counts

**MEASURED, `grep -oiF` per term per file across the three freeze
documents at the merged head:**

    term                 P2-LATTICE-ONTOLOGY-01.md   P2-CHANNEL-FREEZE-01_phaseA_freeze.md   P2-LATTICE-ROUTE-01.md
    site reflection                              0                                       0                        0
    link reflection                              0                                       0                        0
    reflection type                              0                                       0                        0
    reflection plane                             0                                       0                        0

**Twelve measurements, all ZERO.** **No reflection type is named anywhere in
the three documents that freeze the programme's ontology, interaction and
route.**

### 7.2 What the ontology does freeze

**MEASURED, `P2-LATTICE-ONTOLOGY-01.md:181`:**

> `| Reflection positivity of the action | FROZEN HERE as obligation (§1b) |`

**MEASURED, `:70-71`:** *"Reflection positivity is a frozen obligation, not
an assumption: the declared H(4) action must be reflection-positive, or no
quantum theory corresponds to it."*

**MEASURED, `:76-79`:** OS reflection positivity *"must be proved per
declared kinetic operator, and cannot be transplanted from a bosonic Ising
example."*

> **`RP obligation frozen` ≠ `reflection type frozen`.**

**The obligation is frozen. The reflection type is not named**, and the
operator the proof must be per is itself `DELEGATED` at `:189`.

### 7.3 The six interceptions, derived rather than transcribed

**Method: take the nine `UNDETERMINED` entries from the arriving artifact's
per-entry tables, and test each entry's own `D-1` text for
unfrozen-style wording — `unfrozen`, or `not mapped to a frozen …`.**
**An entry carrying that wording is one a wording-based pass would have
tagged `UNFROZEN DATUM` without repository justification.**

    entry   wording present?   subject
    W2      YES                axis 2 reflection type
    n2      YES                axis 2 reflection type
    f2      YES                axis 2 reflection type
    s2      YES                axis 2 reflection type
    k2      YES                axis 2 reflection type
    W10     YES                gauge-invariant observables, "programme algebra unfrozen"
    n7      no                 operator normalization, bare `FAIL`
    f9      no                 operator normalization, bare `FAIL`
    o1      no                 OS78 measure row, abstract depth

    INTERCEPTIONS: 6   —   five reflection type, one observable algebra

**Expected six, five and one; MEASURED six, five and one.**

**The other three `UNDETERMINED` entries are NOT interceptions**, and the
distinction matters: `n7` and `f9` carry no qualifier at all, so a wording
pass had nothing to act on, and `o1` is an EVIDENCE gap — `OS78`'s
hypotheses were never fetched — rather than a programme-status claim.
**Reporting nine interceptions would have overstated what the requirement
caught by half.**

### 7.4 "Could not determine = 0" is true by construction

**The source executor reported this and it is worth repeating because the
figure reads as luck and is not.** `D-1b`'s `A6` returned *verified
unfrozen 8 quantities / verified frozen 0 / could not determine 0*.

**The third is zero BY CONSTRUCTION: anything unverifiable became
`UNDETERMINED` and never received the tag.** **The nine `UNDETERMINED`
entries are where that discipline landed.** A run that reported "0 could not
determine" without saying so would present a design choice as a finding.

## 8. `A7` — the tag totals, re-derived from the per-entry tables

**Re-derived by parsing the tag column of the arriving artifact's six
per-entry tables — NOT by grepping the file.**

**`A7` warns that the obvious method fails, and MEASURED, it does:** a
whole-file grep for the tag names returns

    UNFROZEN DATUM                        6
    INCOMPATIBLE HYPOTHESIS               6
    UNESTABLISHED APPLICABILITY BRIDGE    6
    UNDETERMINED                         13

**against the true 25, 8, 21 and 9.** The grep counts prose occurrences —
definitions, junction discussion, denials — **not per-entry assignments.**
**The Researcher's inability to verify the relation by that method is
reproduced exactly, and the criterion's diagnosis is confirmed.**

**MEASURED from the tables, 52 entries parsed:**

    UNFROZEN DATUM                       25
    INCOMPATIBLE HYPOTHESIS               8
    UNESTABLISHED APPLICABILITY BRIDGE   21
                                         --
                                         54 tag occurrences

    entries carrying MORE THAN ONE tag   11
    entries UNDETERMINED                  9

**Expected as `§1`; measured as `§1`. Every figure agrees.**

**Per candidate, MEASURED:**

    candidate     entries   UD   IH   UB   UNDET
    naive              20    9    4    7       4
    Wilson             13    5    0    7       3
    staggered          10    6    3    3       1
    overlap             9    5    1    4       1

**Per basis, MEASURED, which the per-candidate table aggregates:**

    MP87 → Wilson      11    UD 5  IH 0  UB 6  UNDET 2
    MP87 → naive        9    UD 4  IH 0  UB 5  UNDET 2
    OS78 → Wilson       2    UD 0  IH 0  UB 1  UNDET 1
    FG26 → naive       11    UD 5  IH 4  UB 2  UNDET 2
    FG26 → staggered   10    UD 6  IH 3  UB 3  UNDET 1
    KU10 → overlap      9    UD 5  IH 1  UB 4  UNDET 1

### 8.1 The consistency relation, re-derived

    52 entries − 9 UNDETERMINED = 43 tagged entries
    43 tagged   + 11 multi-tag  = 54 tag occurrences
    sum of the three per-tag counts (25 + 8 + 21) = 54          ✓ agrees

**The relation holds ONLY if every multi-tag entry carries exactly two tags
and none carries three. VERIFIED FROM THE ARTIFACT:**

    entries with three or more tags                      0
    entries both UNDETERMINED and carrying a tag         0
    entries with no parseable tag                        0

    the eleven multi-tag entries, each carrying exactly two:
        W5  W9  n5  n8  f3  f5  s3  s5  s9  k1  k5

**No discrepancy to report.** The check was made by counting tags per row
rather than by assuming the arithmetic — **had one entry carried three, the
relation would have failed at 55 and the figures would have needed
restating, not reconciling.**

## 9. `A8` — shared subjects and shared closures, transcribed and not compressed

**MEASURED from the arriving artifact's `§6`: fourteen table rows, of which**

    SHARED SUBJECT / CLOSURE NOT ESTABLISHED    11
    not shared (candidate-specific)              3        r, M_0, staggered phases
    SHARED CLOSURE established                   0

**ELEVEN SHARED SUBJECTS. ZERO SHARED CLOSURES ESTABLISHED.**

### 9.1 The distinction, in the words that must not be compressed

> **`CLOSURE NOT ESTABLISHED` is not `CLOSURE REFUTED`.**

**`D-1b` re-read no source and did no mathematics.** What it established is
that, **on the repository and `D-1` evidence available, nothing supports
shared closure** — **not that shared closure does not exist.**

**The cheap shared-lemma case is UNRESOLVED, not ruled out.** A report
saying it were ruled out would close a question that is open, and the next
task would not ask it.

### 9.2 The two named cases

**The temporal boundary condition looks strongest and is not.** All four
candidates carry it, and one PI ruling fixes one boundary condition — **but
the four theorems assume DIFFERENT boundary data**: `FG26` anti-periodic in
both directions, `KU10` anti-periodic time with periodic space, `MP87` a
finite-lattice setup with arbitrary reflection-plane separation. **One ruling
matches some and excludes others**, and `D-1`'s own entries say so.

**`MP87`'s non-gauge specialization appears for Wilson and naive — same
paper, same-sounding gap — and rests on two different results inside it.**
The Wilson entry rests on `MP87`'s own site-reflection theorem; the naive
entry on `MP87`'s DISCUSSION of the earlier link-reflection proof at `r=0`.
**Shared wording is not even shared theorem there.**

### 9.3 Neither case is generalised

**That second case is ONE INSTANCE.** **It is not generalised to the other
ten**, and **the fact that one shared subject dissolved on inspection is not
evidence that shared closure is unlikely anywhere else.**

**The ten remaining shared subjects were not inspected to that depth by
`D-1b` and are not inspected here.** They are `CLOSURE NOT ESTABLISHED`
because nothing establishes closure, **not because anything refuted it.**

## 10. `A9` — the two entries where `D-1`'s tables and the repository disagree

**`W6` and `n6`.** `MP87 → Wilson` axis 7 records the non-gauge
specialization as *"not frozen and demonstrated in the programme action"*;
`MP87 → naive` axis 7 as *"not fixed in the programme"*.

**MEASURED, `P2-LATTICE-ONTOLOGY-01.md:26`:**

    | — | gauge bosons and composite particles |

**The line places gauge bosons in the EMERGENT column** of the
fundamental/emergent table, whose FUNDAMENTAL side carries the fermionic
variables, the Euclidean lattice action and the lattice Dirac operator —
**no gauge field.**

**BOTH READINGS, as `D-1b` reported them:**

**As a claim about the THEOREM, the entries are right** — what is not
established is that `MP87`'s gauge-theory result specializes to the
non-gauge case. **As a claim about PROGRAMME STATUS, the repository
contradicts them**: the microscopic action being non-gauge is settled, not
open.

**They were tagged `UNESTABLISHED APPLICABILITY BRIDGE` and neither was
tagged `UNFROZEN DATUM`.** **That handling is correct and this task does not
revisit it.**

**MEASURED: `D-1`'s tables are blob-identical at the head.**

    derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md
        at base   b9109c87ee8aa52ec96c9e095e6de85d2f1d8779
        at head   b9109c87ee8aa52ec96c9e095e6de85d2f1d8779      IDENTICAL

**The arriving artifact lands BESIDE `D-1`'s tables, not over them.** The
later classification is recorded alongside the historical evidence rather
than folded into it, **which is what keeps the trail auditable**: a reader
can still see what `D-1` wrote, what `D-1b` found about it, and that
nobody quietly reconciled the two.

## 11. `A10` — the `2255Z` token

**MEASURED, the four arriving paths VERBATIM:**

    derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md
    reports/2026-08-16T2255Z_d1b-rp-gap-classification.md
    reviews/chatgpt/2026-08-16T2255Z_d1b-rp-gap-classification.md
    specs/2026-08-16T2255Z_d1b-rp-gap-classification.md

**MEASURED, the source branch's commit 1:**

    7063a2a12326c029796ba241dd1d46cf2c35ce04    2026-08-16T23:39:43Z

    token in the filenames   2255Z
    commit 1 UTC             2339Z
    discrepancy              44 minutes

**The four statements `§0` requires, stated:**

1. **The token is inaccurate historical metadata.** The source executor
   measured the time and typed a different value.
2. **The measured commit-1 UTC was `2339Z`.**
3. **No scientific content depends on it**, and **no criterion checks a
   token against a clock.**
4. **This integration preserves the source history rather than rewriting
   provenance retrospectively.**

**MEASURED: no path was renamed and no commit was rewritten.** The four
arriving paths at the merge commit are byte-for-byte the source's, `§4`, and
`A11`'s manifest states them verbatim including `2255Z` with no token
substitution.

**And `2339Z` would not have been the right value either.** It is a COMMIT
timestamp, not a content-creation time. **Rewriting would have exchanged one
unreliable proxy for another across four layers of pushed history**, and
Rule 20 permits amending only a message with the tree unchanged, which a
rename is not.

**An error that happened, was found by its author, and is on the record is
better provenance than one that was erased.**

**This task's own token, MEASURED, for contrast:**

    token used in this task's three paths   2026-08-17T0139Z
    this task's commit 1 UTC                2026-08-17T0139Z      MATCH

**`§7` says to measure the time and use the value measured. I did, and the
two agree to the minute.**

## 12. `A11` — scope, and the arriving arithmetic

**MEASURED at commit 3, the merge commit:**

    A   derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md
    A   reports/2026-08-16T2255Z_d1b-rp-gap-classification.md
    A   reviews/chatgpt/2026-08-16T2255Z_d1b-rp-gap-classification.md
    A   reviews/chatgpt/2026-08-17T0139Z_integrate-d1b-classification.md
    A   specs/2026-08-16T2255Z_d1b-rp-gap-classification.md
    A   specs/2026-08-17T0139Z_integrate-d1b-classification.md

    6 additions, 0 modifications      MEASURED AT COMMIT 3

**INTENDED, base to commit 4: 7 additions and 0 modifications**, the seventh
being this report. **INTENDED and not MEASURED: this report is written
before the commit containing it.**

**Each figure carries the head it was measured at.**

**MEASURED: no status code other than `A` appears. `modify:` is `[]` and
remained so.** **None of the forbidden operations occurs.**

**The arriving counts, stated separately:**

    arriving PATHS           4
    arriving ADDITIONS       4
    arriving MODIFICATIONS   0

    THEY COINCIDE, at four.

**The guard does nothing here and saying so is what keeps it visible.** The
two counts differ only when a modification arrives; **one did two
integrations ago** — `tests/test_gate_pins.py`, where four arriving paths
were three additions — **and there the distinction carried the entire
substance of the landing.**

**MEASURED: the manifest's four arriving paths match the committed bytes
exactly, `2255Z` included, with NO token substitution.** This task's three
carry `2026-08-17T0139Z`, fixed once by commit 1 and reused. **I chose no
path.**

## 13. `A13` — nothing existing changed

**MEASURED path by path over every path present at the evidence base:**

    paths at the evidence base      446
    compared                        446
    blob-identical                  446
    differing                         0
    missing at head                   0

**ZERO differing. This range adds only.**

**The named paths, MEASURED individually — all IDENTICAL:**

    GATES.md                                                          IDENTICAL
    CONVENTIONS.md                                                    IDENTICAL
    docs/GOVERNANCE-DEBT.md                     (governance register) IDENTICAL
    docs/BRANCHING_POLICY.md                    (superseded register) IDENTICAL
    derivations/P2-LATTICE-ONTOLOGY-01.md            (freeze doc)     IDENTICAL
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md (freeze doc)    IDENTICAL
    derivations/P2-LATTICE-ROUTE-01.md               (freeze doc)     IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md   IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md    IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_plaquette-provenance.md       IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md                IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md     IDENTICAL

    scripts/    60 paths,  0 changed
    tests/      21 paths,  0 changed
    results/    69 paths,  0 changed

**All five earlier microspec artifacts are unchanged, including
`_rp-literature-coverage.md`** — the tables `§10` finds at odds with the
repository on one reading. **A task that reported that finding while editing
the tables would have destroyed the evidence for it.**

**The three freeze documents are unchanged too**, and that matters for the
same reason: `A6`'s twelve zero counts were measured against files this task
did not touch.

**No register entry was added anywhere.**

## 14. `A14` — gate invariants and pins

**MEASURED at commit 3, all four:**

    ^## P2- count                        14
    P2-PHASE-01                          Status: PROPOSED      (GATES.md:973)
    first prerequisite                   Prerequisite state: SATISFIED   (GATES.md:1011)
    second prerequisite                  Prerequisite state: SATISFIED   (GATES.md:1036)
    pin at line 1017                     MATCH
    pin at line 1040                     MATCH

**THE STATUS LINE WAS READ SCOPED TO ITS GATE SECTION**: the `P2-PHASE-01`
heading is at `GATES.md:971` and the status line was taken as the offset
`971 + 2`. **A bare first-hit grep returns line 209 — a different gate — and
would have produced the right word from the wrong place.**

**The pins were verified by RECOMPUTING the target digests:**

    GATES.md:1017   4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
    sha256 derivations/P2-PHASE-01_microscopic_parameter_domain.md    identical

    GATES.md:1040   e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
    sha256 derivations/P2-PHASE-01_input_admissibility_contract.md    identical

## 15. `A15` — superseded branches, before the advance

**MEASURED at commit 3. Six separate exit statuses, all 1 — none is an
ancestor of the head:**

    52f65117  exit 1        7146a093  exit 1
    ebd531ab  exit 1        10c260b9  exit 1
    40168469  exit 1        d64cd912  exit 1

**The checker's `P4` independently reports `is_ancestor_of_head: false` and
`object_present: true` for all six.**

**The post-advance repetition is post-report evidence and is not claimed
here.**

## 16. `A16` — the checker, MEASURED at commit 3

    base   822cd4fbfe9bff6e43867caed95c5635344683d0
    head   c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f   (commit 3, the merge commit)

    run 1 INCLUSIVE   exit 0   PASS   sha256 010f9efe268150cc99ab166433a456b9b898b71215001f0936879e52f1ee337b
    run 1 EXCLUSIVE   exit 0   PASS   sha256 e0925d3a8197d67063ef2e4dad8347e97fdd6e36c893e8f45b66a12d41a6e27c
    run 2 INCLUSIVE   exit 0   PASS   sha256 2d2ca4a56f4e305464bba7c081e6f28eada3e57f9ad444f55844a21bd340faf6
    run 2 EXCLUSIVE   exit 0   PASS   sha256 4574aade4d34e53e74acf14baaecdda113d32ba5ddf16845b4d6e4722b2d7efb

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 PASS
    P6 PASS   P7 PASS   P8 PASS   P9 PASS

    NINE OF NINE IN EVERY INVOCATION.  commits_in_range 7.

### 16.1 What `RUN 1` did

**MEASURED: `RUN 1`'s default subject selection found BOTH specifications in
range and evaluated `P1` against each:**

    specs/2026-08-16T2255Z_d1b-rp-gap-classification.md      stated 4 add / 0 mod   counted 4 / 0   parse OK
    specs/2026-08-17T0139Z_integrate-d1b-classification.md   stated 7 add / 0 mod   counted 7 / 0   parse OK

**Both PASS.** `RUN 2` names only this task's specification and evaluated
`P1` against that one alone, **which is why the two runs produce different
bytes.**

**The `C3` multi-specification residual did NOT arise.** MEASURED: `P3` and
`P7` both report `specification_paths_read` as BOTH specifications and
resolve to a single declared set each — `['DECISION_LOG.md']` and `[]` —
with `declared_source: specification`. **Two specifications in range,
agreeing, and no conflict.** The trigger is a DIFFERENCE between
declarations, not their number; **the residual is unchanged and remains
unregistered.**

**`P1`'s `counted_set` holds each specification's own literal manifest
paths.** For the arriving `D-1b` specification those are the real `2255Z`
paths; for this one they include the `2026-08-XXT{HHMM}Z` placeholders.
**`P1` is an internal-consistency check on a specification, not a comparison
against the diff**, and it is stated here so it is not mistaken for a
discrepancy with `§12`'s measured six.

### 16.2 `declared_source`, `P7` and `P9`

    P3   PASS   declared_source: specification   declared: ['DECISION_LOG.md']
    P7   PASS   declared_source: specification   section_count_head 14
    P9   PASS   reports/2026-08-16T2255Z_d1b-rp-gap-classification.md   heading_present: true

**`P7` reports FOURTEEN sections. `PASS` at zero would have been a STOP, and
it is not zero.**

**MEASURED: `DECLARATION_CONFLICT` appears ZERO times in all four
outputs.**

**`DECISION_LOG.md` is not modified by this range**, so `P3` passed without
exercising the append property.

**`P9` found the ARRIVING report and confirmed its `Stops and
clarifications` heading** — a property that could not be exercised in the
source task's own range, where the report did not exist at the head checked.

### 16.3 `RUN 1` config, verbatim — observational, governs nothing

    {
      "base": "822cd4fbfe9bff6e43867caed95c5635344683d0",
      "head": "c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 16.4 `RUN 2` config, verbatim — stop-governing

    {
      "base": "822cd4fbfe9bff6e43867caed95c5635344683d0",
      "head": "c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f",
      "specification_paths": ["specs/2026-08-17T0139Z_integrate-d1b-classification.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

**No value in either config is one I chose**, and **neither the config nor
this specification's declarations were adjusted to make `RUN 2` pass** —
`§9` forbids both. **`RUN 2` passed on its first invocation at both
readings.**

### 16.5 `RUN 1` output, verbatim, `INCLUSIVE` reading

    {
      "base": "822cd4fbfe9bff6e43867caed95c5635344683d0",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f",
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
                "derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md",
                "reports/2026-08-XXT{HHMM}Z_d1b-rp-gap-classification.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_d1b-rp-gap-classification.md",
                "specs/2026-08-XXT{HHMM}Z_d1b-rp-gap-classification.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-16T2255Z_d1b-rp-gap-classification.md",
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
                "derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md",
                "reports/2026-08-16T2255Z_d1b-rp-gap-classification.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-d1b-classification.md",
                "reviews/chatgpt/2026-08-16T2255Z_d1b-rp-gap-classification.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-d1b-classification.md",
                "specs/2026-08-16T2255Z_d1b-rp-gap-classification.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-d1b-classification.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-17T0139Z_integrate-d1b-classification.md",
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
                "commit": "7098e228cb80cb1876d2d2844727e93efd0993c4",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "4f0e33d812baf5816d58ee467d039de5cabe31b1",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md"
                ]
              }
            ],
            "first_review_commit": "4f0e33d812baf5816d58ee467d039de5cabe31b1",
            "first_work_commit": "c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f",
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
              "specs/2026-08-16T2255Z_d1b-rp-gap-classification.md",
              "specs/2026-08-17T0139Z_integrate-d1b-classification.md"
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
              "merge": "c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "822cd4fbfe9bff6e43867caed95c5635344683d0",
              "recomputed_parent_1": "4f0e33d812baf5816d58ee467d039de5cabe31b1",
              "recomputed_parent_2": "242b2f35d7d93c737ca15ffd654b272142c7ef55",
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
              "commit": "7098e228cb80cb1876d2d2844727e93efd0993c4",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "4f0e33d812baf5816d58ee467d039de5cabe31b1",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "7063a2a12326c029796ba241dd1d46cf2c35ce04",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "9e9f429f11dfcb72dd87798e22f236bd2ad37741",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "45f7b54a48a4395180c3e07e41b3c402829c3c4b",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "242b2f35d7d93c737ca15ffd654b272142c7ef55",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f",
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
              "specs/2026-08-16T2255Z_d1b-rp-gap-classification.md",
              "specs/2026-08-17T0139Z_integrate-d1b-classification.md"
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
            "first_commit": "7098e228cb80cb1876d2d2844727e93efd0993c4",
            "first_commit_paths": [
              "specs/2026-08-17T0139Z_integrate-d1b-classification.md"
            ],
            "reports_added": [
              "reports/2026-08-16T2255Z_d1b-rp-gap-classification.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-17T0139Z_integrate-d1b-classification.md",
              "reviews/chatgpt/2026-08-16T2255Z_d1b-rp-gap-classification.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-17T0139Z_integrate-d1b-classification.md",
              "specs/2026-08-16T2255Z_d1b-rp-gap-classification.md"
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
              "path": "reports/2026-08-16T2255Z_d1b-rp-gap-classification.md",
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

### 16.6 `RUN 2` output, verbatim, `INCLUSIVE` reading

    {
      "base": "822cd4fbfe9bff6e43867caed95c5635344683d0",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f",
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
                "derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md",
                "reports/2026-08-16T2255Z_d1b-rp-gap-classification.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-d1b-classification.md",
                "reviews/chatgpt/2026-08-16T2255Z_d1b-rp-gap-classification.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-d1b-classification.md",
                "specs/2026-08-16T2255Z_d1b-rp-gap-classification.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-d1b-classification.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-17T0139Z_integrate-d1b-classification.md",
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
                "commit": "7098e228cb80cb1876d2d2844727e93efd0993c4",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "4f0e33d812baf5816d58ee467d039de5cabe31b1",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_rp-gap-classification.md"
                ]
              }
            ],
            "first_review_commit": "4f0e33d812baf5816d58ee467d039de5cabe31b1",
            "first_work_commit": "c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f",
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
              "specs/2026-08-17T0139Z_integrate-d1b-classification.md"
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
              "merge": "c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "822cd4fbfe9bff6e43867caed95c5635344683d0",
              "recomputed_parent_1": "4f0e33d812baf5816d58ee467d039de5cabe31b1",
              "recomputed_parent_2": "242b2f35d7d93c737ca15ffd654b272142c7ef55",
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
              "commit": "7098e228cb80cb1876d2d2844727e93efd0993c4",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "4f0e33d812baf5816d58ee467d039de5cabe31b1",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "7063a2a12326c029796ba241dd1d46cf2c35ce04",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "9e9f429f11dfcb72dd87798e22f236bd2ad37741",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "45f7b54a48a4395180c3e07e41b3c402829c3c4b",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "242b2f35d7d93c737ca15ffd654b272142c7ef55",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f",
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
              "specs/2026-08-17T0139Z_integrate-d1b-classification.md"
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
            "first_commit": "7098e228cb80cb1876d2d2844727e93efd0993c4",
            "first_commit_paths": [
              "specs/2026-08-17T0139Z_integrate-d1b-classification.md"
            ],
            "reports_added": [
              "reports/2026-08-16T2255Z_d1b-rp-gap-classification.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-17T0139Z_integrate-d1b-classification.md",
              "reviews/chatgpt/2026-08-16T2255Z_d1b-rp-gap-classification.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-17T0139Z_integrate-d1b-classification.md",
              "specs/2026-08-16T2255Z_d1b-rp-gap-classification.md"
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
              "path": "reports/2026-08-16T2255Z_d1b-rp-gap-classification.md",
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

### 16.7 The `EXCLUSIVE` readings

**MEASURED by `diff`, and this is the whole of the difference:**

    run 1   line 314 of 318:   "inclusivity": "INCLUSIVE"  →  "EXCLUSIVE"
    run 2   line 291 of 295:   "inclusivity": "INCLUSIVE"  →  "EXCLUSIVE"

**One line each, and nothing else.** No property status, evidence field or
scope figure differs between the readings, and `commits_out_of_scope` is
empty in all four.

## 17. `A17`, `A18` — validators and hygiene

**`A17`, MEASURED at commit 3, `python -m pytest` from the repository root,
exit status 0:**

    324 passed, 2 deselected      in 44.81 s

**Expected 324 and 2; measured 324 and 2.**

**`A18`, MEASURED on commits 1–3. Commit 4 is post-report evidence:**

    commit 1   7098e228   spec: integrate the reflection-positivity gap classification, and land it
               trailer hits 0      not amended
    commit 2   4f0e33d8   review: pre-execution review for the gap-classification integration
               trailer hits 0      not amended
    commit 3   c9b9fe8b   merge: integrate the reflection-positivity gap classification
               trailer hits 0      not amended

**MEASURED over the whole range, including the arriving commits: a scan for
`Co-Authored-By`, `claude.ai/code`, `Generated with`, `Claude-Session` and
`noreply@anthropic` returns ZERO.** **`P6` independently reports
`matches: []` for every commit in range.**

**Rule 20 binds this task and was NOT exercised.** **No force-push, no
branch deletion, no history rewrite of any kind** — including for the
arriving `2255Z` token, which `§0` rules stays.

**Commits, MEASURED:**

    commit 1   7098e228cb80cb1876d2d2844727e93efd0993c4   specs/2026-08-17T0139Z_integrate-d1b-classification.md
    commit 2   4f0e33d812baf5816d58ee467d039de5cabe31b1   reviews/chatgpt/2026-08-17T0139Z_integrate-d1b-classification.md
    commit 3   c9b9fe8b58dfa3b0c2854b6bd603c4293645ac3f   --no-ff merge of 242b2f35…

**Commit 4's message, INTENDED:**

    report: the reflection-positivity gap classification lands on main

## 18. `§8` — Rule 16 assessment

**Rule 16 is operative. All four junctions are addressed.**

### 18.1 First junction — zero established is not zero

**ZERO SHARED CLOSURES ESTABLISHED IS NOT ZERO SHARED CLOSURES.**

**`D-1b` RE-READ NO SOURCE AND DID NO MATHEMATICS.** It classified entries
already present in `D-1`'s tables and verified one tag family against the
repository. **Nothing in it could have established a shared closure**, and
nothing in it could have refuted one.

**The cheap shared-lemma case — one applicability step serving several
candidates — is UNRESOLVED, not ruled out.** **A reader who takes "zero
shared closures" as "no shared closure exists" would close a live question**,
and the task that would otherwise ask it would not.

**The one case that dissolved on inspection — `MP87`'s two different proofs
— is one case.** It does not license the inference that the other ten would
dissolve too, and `§9.3` says so.

### 18.2 Second junction — a tag distribution is not candidate evidence

**`Wilson` carries ZERO `INCOMPATIBLE HYPOTHESIS` occurrences. THAT IS NOT A
REASON TO CHOOSE IT.**

**The zero is a fact about which theorems were fetched and how their
hypotheses read**, not about which microscopic theory is right. `MP87` is a
four-dimensional Wilson theorem, so the 2D-against-4D conflict that produces
three of the eight `IH` occurrences elsewhere never arises for Wilson; and
`OS78` contributes two entries of which one is an access gap. **Change the
fetched set and the zero changes, with nothing about Wilson having changed.**

**Equally, `naive`'s nine `UNFROZEN DATUM` occurrences do not make it closer
to admissible** — they make it a candidate whose gaps depend on rulings the
programme has not made, **and those rulings are the PI's.**

**This is stated in `§8` of this report, where a reader meets the table**,
and in the arriving artifact's own `§7`.

### 18.3 Third junction — fifty-two entries are not fifty-two problems

**Many entries are repeated manifestations of the same underlying programme
datum or theorem junction.** The temporal boundary condition appears five
times; the microscopic measure five times; `FG26`'s `H1/H2/H3` twice.

**THE REDUCTION FROM ENTRIES TO INDEPENDENT UNRESOLVED DEPENDENCIES HAS NOT
BEEN PERFORMED**, here or in `D-1b`. **Until it is, the tag totals OVERSTATE
how many distinct things are open.**

**That reduction is a separate task, not scoped here, and it asks a
different question from `A8`'s.** `A8` asks *does one bridge close several
gaps* — a mathematical question. **The reduction asks *does one programme
DECISION control several entries* — and a temporal-boundary freeze involves
no mathematics at all.** **The two are distinct**, and a task conflating
them would answer neither.

### 18.4 Fourth junction — which tags were verified against what

    UNFROZEN DATUM                       VERIFIED against the repository, quotation
                                         by quotation, in D-1b — and its six
                                         interceptions are re-derived here at §7.
    INCOMPATIBLE HYPOTHESIS              PARTIALLY verified. The PROGRAMME half —
                                         the frozen four dimensions, the frozen
                                         generator-sum interaction — was checked.
                                         The SOURCE half was not.
    UNESTABLISHED APPLICABILITY BRIDGE   NOT verified against anything outside D-1.

**No source has been re-fetched since `D-1`.** Neither `D-1b` nor this
integration retrieved `MP87`, `FG26`, `KU10` or `OS78`.

**Whether re-reading a source would change an `INCOMPATIBLE HYPOTHESIS` or
`UNESTABLISHED APPLICABILITY BRIDGE` tag is `NOT DETERMINABLE` from what has
landed.**

## 19. Did landing this make me want to choose a candidate, size a gap, or start the dependency reduction?

**All three. The third was much the strongest, and it is the one the
specification had to name explicitly to stop.**

**The dependency reduction: strongest, and structurally so.** `§18.3` is a
true and load-bearing observation — fifty-two entries are not fifty-two
problems — **and the moment you believe it, the reduction is the obviously
useful next thing to do.** The material is right there: the temporal boundary
condition appears five times, the measure five times, and grouping them takes
a few minutes. **`§5` of the specification forbids performing it AND
forbids scoping it**, and the second half is the part I would have violated
first — it is very easy to write "roughly N independent dependencies remain"
while believing you are only describing what someone else will do. **I wrote
no such figure.**

**Sizing: moderate, and it arrives through the same door.** `UNFROZEN
DATUM`'s closure mechanism is a PI ruling, which involves no mathematics —
**and "no mathematics" is one short step from "cheap".** It is also wrong:
`§9.2` establishes that no single ruling closes even two entries jointly, so
twenty-five `UD` occurrences are not twenty-five things one decision
resolves. **A tag is not a cost, and `B0`'s seven-to-eleven estimate is
unchanged and not re-derived here.**

**Choosing a candidate: weakest, and the most visually tempting.** Wilson's
zero in the `IH` column is the only zero in the table and the eye goes
straight to it. **I wrote the zero and then wrote why it is an artefact of
the fetched set** — `§18.2` — rather than leaving a reader to draw the
inference from a column.

**One further pull, specific to integrating rather than producing:** the
arriving artifact records `W6` and `n6` as entries where `D-1`'s tables and
the repository disagree, **and the tidy thing to do would be to fix the two
sentences in `D-1`'s tables while landing.** **That is exactly the
retroactive evidence-cleaning `§3` forbids**, and it would have destroyed the
record of a finding this line spent a whole task producing. **`D-1`'s tables
are blob-identical at the head**, `§10`.

**I confirm: I selected, eliminated, ranked and preferred no candidate;
sized no gap and estimated no effort; performed no dependency reduction and
stated no figure for how many dependencies remain; designed no lemma, proof
or construction; did not re-derive or revise `B0`'s estimate; modified no
file, renamed no arriving path, and did not touch `D-1`'s tables; added no
register entry; and made exactly one merge, with no rebase, no squash and no
fast-forward at the integration.**

## 20. Stops and clarifications

**NO STOP occurred.** The merge was clean, all four checker invocations
exited 0, `RUN 2` passed at both prospectivity readings, the conflict list
was empty, and no acceptance criterion failed.

    SPECIFICATION_DEFECT                          0 stops, 0 findings
    ENVIRONMENT                                   0 stops, 0 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 1 finding
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 2 findings

### 20.1 `OBSERVATION_METHOD_ERROR` — one finding, and it is the criterion's, not mine

**`A7` predicted that the obvious method fails, and MEASURED, it does.** A
whole-file grep for the three tag names returns 6, 6, 6 and 13 against the
true 25, 8, 21 and 9 — **the grep counts definitions, junction discussion
and denials, not per-entry assignments.**

**I did not make this error, because the criterion warned of it**, and I
report it as a finding rather than as a near-miss of mine: **the warning is
what prevented it, and a later task counting tags in this artifact will meet
the same trap.** **The count must come from the per-entry tables.**

**This is the third instance of the same shape in this line** — `D-pre-B0`'s
`REFUTED` at five occurrences and zero cells; `D-1`'s `FAIL` legend line;
and now the tag names. **A whole-file grep over an artifact that DEFINES its
own vocabulary counts the definitions.**

### 20.2 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — first finding

**The arriving `2255Z` token is inaccurate historical metadata that is now
landing on `main`**, `§11`. **`§0` rules that it stays, and I agree with the
ruling** — the rewrite would have touched four layers of pushed history to
substitute a commit timestamp that is not the content-creation time either.

**The residual: nothing in the repository records that the token is
inaccurate except this report and the source report.** **A reader
reconstructing chronology from filenames will be forty-four minutes wrong
and will have no signal that they are.** **Reported, NOT registered** — `§9`
forbids adding a register entry.

### 20.3 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — second finding

**Two entries of `D-1`'s tables assert a programme status the repository
contradicts on one reading**, `§10`, and **both readings now land on `main`
in different files**: `D-1`'s tables say "not frozen", `D-1b`'s
classification says the programme side is settled and tags the entries `UB`.

**Which reading `D-1` intended is not determinable from the table.** **This
is the correct disposition and it is still an ambiguity on the record**, and
a later task reading only `_rp-literature-coverage.md` would take the
programme-status reading at face value.

**Reported, NOT registered. `D-1`'s tables are unmodified.**

### 20.4 `SPECIFICATION_DEFECT` — nothing to report

**Nothing in this specification was found false about the repository or
about its own bytes.** Its pre-issue record was checked at six points — the
base and source and non-ancestry, the merge and its 6/0 figure, the four
arriving paths, the token against the clock, the twelve reflection-vocabulary
zero counts, and the ontology's line 26 — **and MEASURED agrees at every
one.**

**Its `§6` ordering statement is the one to note approvingly.** An earlier
draft said `A3` runs "before any measurement", which `A1` and `A2`
contradict — both require measurements. **The revised text states one
normative order and says that criterion numbering is not execution order.**
**Three tasks in this line have stopped on execution-order or
repository-identity ambiguity**, and this is the first specification in the
sequence to state the order rather than leave it inferable.

**Its `A7` warning about the whole-file grep is likewise correct and was
load-bearing**, `§20.1`.

### 20.5 `ENVIRONMENT`, `REPOSITORY_DEFECT` — nothing to report

**No environment failure occurred**, `§1`; **neither of Rule 13's two
diagnostic orders was exercised**, and nothing was installed.

**No defect in the repository was found by this task.** Every path at the
evidence base is blob-identical at the head; the gate invariants hold; both
pins recompute; the checker passes nine of nine at both readings; the
validators are unchanged at 324 passed, 2 deselected.

### 20.6 What I would have specified differently

**`A6` asks for the per-term per-file counts and the six interceptions, but
does not say how to derive the six.** I derived them by testing each
`UNDETERMINED` entry's own text for unfrozen-style wording, which gives six
and identifies which three of the nine are NOT interceptions. **I would have
had `A6` require that derivation method or an equivalent**, because "expected
six" invites transcription, and transcription is what `A6` exists to
prevent.

**And `A8` asks for eleven shared subjects and zero shared closures without
asking for the three NOT-shared rows.** The artifact's `§6` has fourteen
rows; **eleven plus three is what makes the count checkable**, and reporting
only the eleven leaves a reader unable to tell whether three rows were
dropped or never existed. **I reported all fourteen.**

## 21. Evidence layering

**Committed in this report, MEASURED at commit 3:** `A1`–`A15`, `A17` and
`A18` for commits 1–3; `A16`'s four invocations with both configs and both
runs' output verbatim; `A11`'s scope base-to-commit-3 at 6 additions and 0
modifications, and the arriving counts; commits 1–3 SHAs and their stored
messages.

**Committed in this report, INTENDED:** commit 4's message; `A11`'s final
base-to-commit-4 scope of 7 additions and 0 modifications.

**Stated as `NOT DETERMINABLE`:** whether re-reading a fetched source would
change an `INCOMPATIBLE HYPOTHESIS` or `UNESTABLISHED APPLICABILITY BRIDGE`
tag, `§18.4`.

**Post-report evidence, returned to the Reviewer and NOT written back:**
`A11`'s final scope measured base-to-commit-4; `A16-final`, being `RUN 2`
re-run at commit 4 BEFORE the landing; `A14` and `A15` re-run after the
advance; `A18` for commit 4; the pre-advance `--is-ancestor` exit status;
the exact push command; remote `main` read back; the source tip unchanged;
confirmation that no other ref was pushed; final ancestry confirmation.

**Nothing in this report claims to measure commit 4.**
