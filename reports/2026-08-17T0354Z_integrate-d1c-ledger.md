# Report — integrate the reflection-positivity dependency ledger, and land it

    branch      science/integrate-d1c-ledger
    base        ec85f66b05b3ed92cd924bc75273b74a73eee23b   (authoritative main)
    source      science/d1c-dependency-reduction @ cdbfa6b9cb858d825a2047bd7683e96728d38c14
    measured at commit 3, 2cce4295dbeb0f046cd7c662d52da8ddb5823a40   (the merge commit)

**One merge, no conflict. Six additions, ZERO modifications. Nothing is
modified — not `D-1`'s tables, not `D-1b`'s classification, not `D-1c`'s
ledger.**

**One arithmetic finding about the arriving ledger, `§10`. It is reported
and the ledger lands unmodified.**

---

## 1. `A3` — environment conformance, run FIRST

**The normative execution order, and the order followed:**

    A3  environment conformance      ran first
    A1  repository identity and refs ran second
    A2  review binding               ran third
    A4  onward

**Criterion numbering is not execution order.**

    (0) execution location    /home/user/2-emergent-gravity; work in the
                              science/integrate-d1c-ledger worktree cut from
                              ec85f66b… by explicit SHA. MEASURED: seven
                              worktrees present. SAME CONTAINER as the six
                              preceding tasks.
    (1) execution identity    root, uid 0
    (2) interpreter           Python 3.11.15 at /usr/local/bin/python
    (3) permissions           repository writable; no permission failure
    (4) filesystem/workspace  MEASURED: `git rev-parse --is-shallow-repository`
                              → false. No `.git/shallow`. 447 commits on the
                              authoritative line. NOT SHALLOW.
    (5) package availability  MEASURED: pytest 9.1.1, numpy 2.4.6,
                              sympy 1.14.0, ruff 0.15.8 — all four declared
                              packages present and importable.

**NO RESTORATION WAS NEEDED AND NONE WAS PERFORMED. No repository content
was touched by this criterion.**

**Rule 13 carries two diagnostic orders, a known open item. NO ENVIRONMENT
FAILURE OCCURRED**, and **neither order was exercised** — I am not naming
one as having applied.

## 2. `A1` — repository and refs

**MEASURED, VERBATIM and NOT normalised:**

    git remote get-url origin        https://github.com/zetacheng/2-emergent-gravity

**No `.git` suffix. `A1` accepts either form, and it identifies
`zetacheng/2-emergent-gravity`.**

    refs/remotes/origin/main                       ec85f66b05b3ed92cd924bc75273b74a73eee23b
    refs/heads/main                                1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    science/d1c-dependency-reduction (remote)      cdbfa6b9cb858d825a2047bd7683e96728d38c14

**`refs/remotes/origin/main` is `ec85f66b…`, as the evidence base requires.
No stop.** **`refs/heads/main` lags, and `A1` says a lagging local ref is
not a stop.**

**MEASURED: the source is NOT an ancestor of `main`.**

    git merge-base --is-ancestor cdbfa6b9… refs/remotes/origin/main
    exit status 1   →  NOT an ancestor

## 3. `A2` — the pre-execution review

**MEASURED.**

    field `Reviewed specification SHA-256:` PRESENT   yes, line 4
    value carried by the review                       bf7ce753aac2dccaf772d418d9193af662acd72fb31236ba146edd3fdad01b11
    SHA-256 of the committed specification bytes      bf7ce753aac2dccaf772d418d9193af662acd72fb31236ba146edd3fdad01b11
    MATCH                                             yes
    review verdict                                    APPROVE FOR EXECUTION
    committed unedited                                yes — byte-identical to the supplied review

**The field's presence was checked before its value was compared.**

## 4. `A13` — which merge case, stated BEFORE the blob comparisons

**MEASURED, before the merge was made:**

    merge-base(origin/main, cdbfa6b9…)                ec85f66b05b3ed92cd924bc75273b74a73eee23b
    commits on main after the base                    0

**The merge-base IS the evidence base, and `main` carries no commit after
it, so no commit on `main` could have touched an arriving path.** The merge
is one-sided, and that is what makes the comparison below mean what it
appears to mean.

**NOW the comparisons, MEASURED at the merge commit against `cdbfa6b9…`:**

    derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md      IDENTICAL
    reports/2026-08-17T0322Z_d1c-dependency-reduction.md             IDENTICAL
    reviews/chatgpt/2026-08-17T0322Z_d1c-dependency-reduction.md     IDENTICAL
    specs/2026-08-17T0322Z_d1c-dependency-reduction.md               IDENTICAL

**All four blob-identical. Nothing arriving was altered in transit and no
path was renamed** — including the ledger, whose `§6.2` this report finds
an error in.

## 5. `A5` — no conflict

**MEASURED, `git diff --name-only --diff-filter=U` at the merge:**

    (empty)      conflict entries    0

**The conflict list is EMPTY**, matching the Researcher's dry run.

## 6. `A4` — merge parentage, three separately derived measurements

    merge commit                              2cce4295dbeb0f046cd7c662d52da8ddb5823a40
    parent 1   git rev-parse HEAD^1           f395ee4f9ae2abc780f4b9e01b31ee6659a865a1
    parent 2   git rev-parse HEAD^2           cdbfa6b9cb858d825a2047bd7683e96728d38c14
    merge-base git merge-base HEAD^1 HEAD^2   ec85f66b05b3ed92cd924bc75273b74a73eee23b

**Parent 1 IS this task's review commit. Parent 2 IS the specified source
tip. The merge-base IS the evidence base.**

    git merge-base --is-ancestor 9c9b35ffd7b61e9d44e69f5aa222cd49fc68e42c HEAD^1      exit status 0   →  YES

**`P5` independently recomputed all three and agrees**, reporting
`compared_to_recorded: UNAVAILABLE` — the merge commit records no parentage
in its message, so `P5` verified internal coherence, not agreement with
anything I wrote.

## 7. `A6` — the seven nodes, re-derived from the arriving ledger

**Parsed from the ledger's `§3` and `§4` node records, not transcribed from
the source report.**

    node   datum or fact                                        kind               controls                       status
    R1     the canonical kinetic operator and its parameters    RULING             W8 W9 n8 k7 s9            5    OPEN
    R2     the admissible lattice extent / finite volume        RULING             W3 n3 f3 f8 s3 s8 k3 k8   8    OPEN
    R3     boundary conditions, the temporal one in particular  RULING             W4 n4 f4 s4 k4            5    OPEN
    R4     the microscopic variables, state space and measure   RULING             W5 n5 f5 s5 k5            5    OPEN
    R5     the internal multiplicity N                          RULING             f7 s7                     2    OPEN
    F1     the H(4) lattice is four-dimensional                 ESTABLISHED FACT   f3 f6 s3 s6               4    —
    F2     the frozen U(N)_L × U(N)_R generator sum, G > 0      ESTABLISHED FACT   f1 f10 s1 k1              4    —

**Anchors, re-read from the repository rather than from the ledger, at
`§8`.**

### 7.1 The two decompositions, reported as separate figures

**DATUM LEVEL — counting proposed dependencies:**

    N_ruling                  5
    N_proposed_frozen         0
    N_proposed_undetermined   0

**OCCURRENCE LEVEL — counting `UD` occurrences:**

    N_mapped                 25
    N_frozen_finding          0
    N_undetermined_finding    0

**These are different units and are not equated.**

**MEASURED: the `UD` mapping covers 25 occurrences, all distinct — no
occurrence appears under two `RULING` nodes.** 5 + 8 + 5 + 5 + 2 = 25.

**MEASURED: the `IH` mapping covers 8 occurrences, all distinct.**
4 + 4 = 8.

**`f3` and `s3` appear in both mappings, and that is correct.** Each is a
multi-tag entry: its `UD` occurrence is borne by `R2`, its `IH` occurrence
by `F1`. **Two tag occurrences of one entry, each accounted once in its own
class** — the two mappings partition different sets.

## 8. `A7` — anchors verified against the repository, and lexical hits distinguished from rulings

### 8.1 The anchors, opened and read

**Every line below was read at the merged head. What I read is quoted.**

    R1  ONTOLOGY:189    "| Canonical kinetic operator and species accounting |
                         DELEGATED: D-pre (§4 obligation binds it) |"
        ROUTE:189-190   "*Freeze:* microscopic variables and measure; the canonical
                         lattice Dirac / operator; the species ledger and doubling
                         treatment; the"
        dossier:169-170 "**NOT ESTABLISHED for this candidate:** the value of `r` as a
                         canonical choice / — `r = 1` is what the exploratory script
                         uses, not something the repository"
        dossier:232-233 "`M_0` the kernel mass, equivalently the domain-wall height.
                         **`M_0` is a / convention this dossier states and does not
                         choose.**"
        dossier:274-275 "**NOT ESTABLISHED for this candidate:** which `M_0` the
                         programme would adopt, / that being part of the choice this
                         dossier does not make; whether the"

    R2  ONTOLOGY:192    "| Admissible thermodynamic / infinite-volume limits |
                         DELEGATED: the gate that first needs them, with
                         preregistration |"
        ROUTE:192-193   "the subtraction / reference-equivalence class; finite-volume
                         and / thermodynamic rules; boundary conditions."

    R3  ROUTE:193       "thermodynamic rules; boundary conditions."
        ROUTE:202       "measure and Jacobian factors; finite temporal extent;
                         temporal boundary"
        ONTOLOGY:27     "| boundary conditions, internal multiplicity `N` | Lorentz
                         symmetry, the light cone |"

    R4  ONTOLOGY:185    "| Microscopic Euclidean variables, state space and measure |
                         DELEGATED: a subordinate `P2-LATTICE-MICROSPEC-01` artifact
                         (or Route D D-pre acting as such) — NOT FIERZSUM |"
        ROUTE:189       "*Freeze:* microscopic variables and measure; …"

    R5  CHANNEL-FREEZE:43  "- the `1/N` prefactor defining the large-N limit; `N` kept
                            symbolic in"
        ONTOLOGY:27        as above

    F1  ONTOLOGY:62-64  "**Declaration.** The fundamental formulation is EUCLIDEAN:
                         the H(4) lattice is a four-dimensional
                         configuration-and-weight statistical system with all four
                         axes equivalent."
        ONTOLOGY:94-95  "H(4) isotropy (equal couplings on all four axes) joins the
                         freeze list."

    F2  CHANNEL-FREEZE:36-37  the canonical action with the (G/2N) generator sum
        CHANNEL-FREEZE:40     "- `G > 0` — the **single independent coupling of the
                               operative canonical"
        CHANNEL-FREEZE:45     "- classical symmetry `U(N)_L × U(N)_R`; …"

**Every anchor says what the ledger reports it says.** The two the
Researcher stated in advance — `ONTOLOGY:189` and `ROUTE:192-193` — **were
re-read rather than accepted, and both match.**

### 8.2 `R2` and `R3` are named in one semicolon-separated sentence

**MEASURED. `P2-LATTICE-ROUTE-01.md:192-193` reads:**

> *the subtraction / reference-equivalence class; finite-volume and
> thermodynamic rules; boundary conditions.*

**One `*Freeze:*` sentence, beginning at `:189`, listing items separated by
semicolons.** **`R2`'s datum and `R3`'s datum are two of those items.**

**`D-1c` KEPT THEM AS TWO NODES.** **Grouping them would have made five
nodes four on the strength of punctuation** — and the ledger's own grouping
rule forbids grouping on shared wording, which a shared sentence is the
strongest form of.

### 8.3 Lexical hits and rulings are different figures, and both are reported

**`DECISION_LOG.md`, LEXICAL HIT COUNTS, MEASURED with `grep -oiF`:**

    kinetic operator        0        measure                 3
    Dirac operator          0        microscopic measure     0
    Wilson parameter        0        multiplicity            0
    lattice extent          0        internal multiplicity   0
    finite volume           0        reflection type         0
    finite-volume           0
    thermodynamic           0
    boundary condition      0

**DISPOSITION AFTER READING, for the one non-zero count:**

    :416   "longitudinal mixing measured in the wrong (single-momentum) basis"
           — the ordinary verb, in a β_V sector-decomposition entry.  NOT A RULING.
    :1728  "Amendment K's append-only measure — evaluated against the last pushed
           state of the branch"
           — a governance metric.  NOT A RULING.
    :1963  "**The word 'restricted' is doing work.** The quantity measured is the
           curvature of the reduced one-dimensional scalar potential"
           — the ordinary verb.  NOT A RULING.

**THREE LEXICAL HITS. ZERO RULINGS. Neither figure is the other.**

**`GATES.md`, LEXICAL HIT COUNTS, MEASURED:**

    kinetic operator        0        finite-volume           2
    Dirac operator          0        thermodynamic           3
    Wilson parameter        0        boundary condition      0
    lattice extent          0        microscopic measure     0
    finite volume           0        internal multiplicity   0
                                     reflection type         0

**DISPOSITION AFTER READING, for the two non-zero counts:**

    finite-volume :156   "Infinite-volume BZ tadpole `Z=(1/12)∫1/(p̂²+m²)`, fit over
                         `m∈[0.125,0.55]`."
                         — the hit is the SUBSTRING inside "Infinite-volume". It is
                         not even the term.  NOT A RULING.
    finite-volume :694   "- the treatment of finite-volume / grid artifacts;"
                         — a method note in another gate.  NOT A RULING.
    thermodynamic :1032  "completeness, no full-space stability, no thermodynamic
                         dominance,"
    thermodynamic :1046  "flat directions; thermodynamic selection against the
                         comparison set"
    thermodynamic :1047  "of stationary solutions satisfying the non-thermodynamic
                         conditions"
                         — all three are the phase gate's stability and dominance
                         conditions.  NONE rules on the admissible lattice extent.

**FIVE LEXICAL HITS in `GATES.md`. ZERO RULINGS.**

### 8.4 The `D-1c` wording this criterion exists to correct

**`D-1c`'s report says `DECISION_LOG.md` "returns ZERO occurrences of every
term searched".**

**MEASURED: that statement is literally true of the terms `D-1c` searched**
— its list was `kinetic operator`, `boundary condition`, `finite volume`,
`thermodynamic`, `microscopic measure`, `internal multiplicity`, `reflection
type`, `Wilson parameter`, **and all eight return zero here too.**

**The imprecision is narrower and real: bare `measure` was NOT among them**,
and bare `measure` is the term most likely to catch a later ruling on `R4`.
**It returns three, and none is a ruling.**

**So `D-1c`'s conclusion survives and its search was narrower than its
sentence implies.** **Read as "zero later authoritative rulings", correct.
Read as "zero lexical hits for every term that might matter", not
demonstrated by the terms it ran.** **This integration ran the broader term
and read all three hits.**

**The core assertion of `D-1c` — that no later ruling exists for `R1`–`R5`
— survives, and it survives BECAUSE the two figures are kept apart.**

## 9. `A8` — `§1a`, `§1b`, `§1c` transcribed

### 9.1 `§1a` — five is an adopted granularity, not a measurement

**Transcribed in the form `§1` gives:**

> **Under `D-1c`'s adopted programme-dependency granularity, the 25 `UD`
> occurrences reduce to five `RULING` nodes; a finer constituent-level
> decomposition, explicitly recorded by `D-1c`, would yield eight nodes
> over the same 25 occurrences.**

**The source executor's own first sentence about the figure was that it is
a judgement, not a measurement.** `R1` groups `r`, the mass and hopping
domain, `M_0` and the staggered phases as constituents of ONE delegated
datum, on `ONTOLOGY:189` and the dossier's *part of the choice this dossier
does not make*. **Both readings are in the landed ledger**, `§6.2` of it.

### 9.2 `§1b` — `CONTROLS` is accounting, not intervention effect

**`k8` names two data — *"finite even extent and boundary data"* — and the
exactly-once rule forces it into `R2`. It depends on `R3` as well.**

    WRONG   freezing R2 would eliminate eight gaps
    RIGHT   eight UD occurrences are borne by R2 as their primary
            dependency node under D-1c's exactly-once accounting

**`D-1c` built a dependency-accounting partition, not an
intervention-effect model.**

**The source executor reported this as a bias its own bookkeeping
introduces, in `R2`'s favour, WITHOUT BEING ASKED** — the `A10` criterion
requiring it was written afterwards, and the disclosure is in the landed
report's `§18.3` and the ledger's `§3.2`.

### 9.3 `§1c` — a node count is not a question count

**The node count is a node count.** **It is not restated here as a number
of questions, decisions, or problems.**

**"Five open programme questions" would be a granularity-dependent
statement**, and `§9.1` is why: `R1` alone decomposes into four
constituents, and `R5`'s relation to the species ledger is itself
unsettled.

### 9.4 The three searches

**MEASURED over this report.**

    search 1   `25 → 5` / "25 to 5" written as a granularity-independent fact
               ALL occurrences of the arrow form carry an adopted-granularity
               qualifier in the same sentence or the sentence before.
               VIOLATIONS: 0

    search 2   any sentence stating how many gaps closing a node would retire
               — "would retire", "would eliminate", "would close N", "retires"
               VIOLATIONS: 0.  The only occurrences are §9.2's WRONG/RIGHT pair,
               which states the wrong form in order to forbid it.

    search 3   any sentence calling the node count a number of questions,
               decisions or problems — "five questions", "five decisions",
               "five problems", "N distinct questions"
               VIOLATIONS: 0.  The only occurrences are denials.

## 10. `A9` — the cross-paper check, re-derived — and MP87 has NINE, not eight

### 10.1 The check itself

**MEASURED, re-derived from `D-1b`'s per-entry tables and the ledger's
`CONTROLS` lists:**

    R2  spans 3 papers   MP87, FG26, KU10
    R3  spans 3 papers   MP87, FG26, KU10
    R4  spans 3 papers   MP87, FG26, KU10

**`R2`, `R3` and `R4` each span three different papers**, as `§2` of the
specification states. **`R1` also spans three** — `MP87`, `FG26`, `KU10`.
**`R5` spans one, `FG26`, because only `FG26` imposes a constraint on
`N`.**

**Had the grouping run ALONG papers, that would have been evidence the rule
was satisfied in name only.** **It runs across them**, and this is the only
empirical confirmation that the hard boundary held.

### 10.2 The finding: nine, not eight

**`§2` of this specification, and `§6.2` of the arriving ledger, and `§8.2`
of the arriving report, all state that `MP87` contributes EIGHT `UD`
occurrences, listed as `W3 W4 W5 W9` and `n3 n4 n5 n8`.**

**MEASURED, by counting `UD` entries in `D-1b`'s per-entry tables for the
two `MP87` bases:**

    MP87 → Wilson    UD entries   W3 W4 W5 W8 W9      5
    MP87 → naive     UD entries   n3 n4 n5 n8         4
                                                     --
    MP87 total UD occurrences                         9

**`W8` — the Wilson parameter `r` — is missing from the list of eight.**

**The ledger's own `R1` record lists `W8` correctly in its `CONTROLS`
field.** **So the ledger is internally inconsistent: `R1` accounts for
`W8` as an `MP87 → Wilson` occurrence, and `§6.2`'s prose omits it from
the `MP87` roll-call.**

**NOTHING ELSE IS AFFECTED.** The 25-occurrence partition is unchanged,
`5 + 8 + 5 + 5 + 2 = 25` still holds, and every node's `CONTROLS` list is
correct as written. **The error is confined to one prose sentence in each
of the two arriving artifacts, and to `§2` of this specification which
carried the figure forward.**

**The conclusion is unaffected and slightly strengthened.** **MEASURED:
all NINE of `MP87`'s `UD` occurrences sit in nodes that also contain
non-`MP87` occurrences:**

    R2   MP87 W3 n3      grouped with   f3 f8 s3 s8 k3 k8
    R3   MP87 W4 n4      grouped with   f4 s4 k4
    R4   MP87 W5 n5      grouped with   f5 s5 k5
    R1   MP87 W8 W9 n8   grouped with   k7 s9

**Not one `MP87` occurrence is grouped only with another `MP87`
occurrence.**

**Reported, and the arriving artifacts are NOT modified.** `§4` forbids it,
and this is the same disposition `D-1b`'s `W6`/`n6` finding received: **the
correction lands beside the record rather than over it.**

### 10.3 `W6` and `n6`

**`MP87`'s `W6` and `n6`, named in advance as the motivating case, are in
NEITHER one node nor two.** **They are `UNESTABLISHED APPLICABILITY BRIDGE`
occurrences and out of scope for the reduction entirely.**

## 11. `A10` — the `k8` double dependency

**MEASURED from the arriving ledger's `§3.2`.**

**`k8` reads *"finite even extent and boundary data"*.** **It names two
data.** **`D-1c`'s exactly-once accounting placed it in `R2`, on its
leading datum, the extent.** **It depends on `R3` as well.**

**The ledger records the `R3` component as a note and NOT as a second
disposition**, because counting it twice would break the exactly-once rule.

**The source executor reported this UNPROMPTED, as a bias its own
bookkeeping introduces in `R2`'s favour** — `§18.3` of the landed report
states that a later task computing occurrences-retired-per-ruling from the
`CONTROLS` lists would be wrong by one, in `R2`'s favour. **No criterion
asked for that disclosure; the `A10` requiring it was written after the
report.**

## 12. `A11` — out-of-scope counts

    UNESTABLISHED APPLICABILITY BRIDGE   21 occurrences
    UNDETERMINED                          9 entries
    covered by the reduction             33 of 54 tag occurrences

**MEASURED: no node's `CONTROLS` list contains a `UB` occurrence or an
`UNDETERMINED` entry.** **None was grouped, classified or judged, in the
ledger or here.**

## 13. `A12` — scope

**MEASURED at commit 3, the merge commit:**

    A   derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md
    A   reports/2026-08-17T0322Z_d1c-dependency-reduction.md
    A   reviews/chatgpt/2026-08-17T0322Z_d1c-dependency-reduction.md
    A   reviews/chatgpt/2026-08-17T0354Z_integrate-d1c-ledger.md
    A   specs/2026-08-17T0322Z_d1c-dependency-reduction.md
    A   specs/2026-08-17T0354Z_integrate-d1c-ledger.md

    6 additions, 0 modifications      MEASURED AT COMMIT 3

**INTENDED, base to commit 4: 7 additions and 0 modifications**, the
seventh being this report. **INTENDED and not MEASURED: this report is
written before the commit containing it.**

**Each figure carries the head it was measured at.**

**MEASURED: no status code other than `A` appears. `modify:` is `[]` and
remained so.** **None of the forbidden operations occurs.**

**The arriving counts, stated separately:**

    arriving PATHS           4
    arriving ADDITIONS       4
    arriving MODIFICATIONS   0

    THEY COINCIDE, at four.

**The guard does nothing here, and saying so keeps it visible.** It differs
only when a modification arrives, as one did two integrations before this.

**On `append_only: DECISION_LOG.md`, and no conflict arose.** It is a
checker-configuration declaration, not a write authorisation; `§9` limits
writable paths to this specification, its review and its report.
**MEASURED: `DECISION_LOG.md` is blob-identical at the head**, `§14`.
**The two never appeared to conflict, so no stop was required** — and had
they, `§9` would have governed.

**The `{HHMM}Z` token, MEASURED against the clock:**

    date -u at branch creation      2026-08-17T0354Z
    commit 1 author date, UTC       2026-08-17T0354Z      MATCH

**I measured the time and used the value I measured.** The token was fixed
once by commit 1 and reused; **I chose no path.**

## 14. `A14` — nothing existing changed

**MEASURED path by path over every path present at the evidence base:**

    paths at the evidence base      453
    compared                        453
    blob-identical                  453
    differing                         0
    missing at head                   0

**ZERO differing.**

**The named paths, MEASURED individually — all IDENTICAL:**

    GATES.md                                                          IDENTICAL
    CONVENTIONS.md                                                    IDENTICAL
    DECISION_LOG.md                                                   IDENTICAL
    docs/GOVERNANCE-DEBT.md                     (governance register) IDENTICAL
    docs/BRANCHING_POLICY.md                    (superseded register) IDENTICAL

    the four freeze documents:
    derivations/P2-LATTICE-ONTOLOGY-01.md                             IDENTICAL
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md                 IDENTICAL
    derivations/P2-LATTICE-ROUTE-01.md                                IDENTICAL
    derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md   IDENTICAL

    all six microspec artifacts:
    …_kinetic-operator-dossier.md                                     IDENTICAL
    …_selection-discriminants.md                                      IDENTICAL
    …_plaquette-provenance.md                                         IDENTICAL
    …_tm-rp-scope.md                                                  IDENTICAL
    …_rp-literature-coverage.md                                       IDENTICAL
    …_rp-gap-classification.md                                        IDENTICAL

    scripts/    60 paths,  0 changed
    tests/      21 paths,  0 changed
    results/    69 paths,  0 changed

**`D-1`'s tables, `D-1b`'s classification and the four documents every
anchor was verified against are all unchanged** — **and so is the arriving
ledger, whose `§6.2` `§10.2` finds an error in.** **A task that verified an
anchor and then edited the file, or that corrected the artifact it was
reporting on, would have destroyed its own evidence.**

**No register entry was added anywhere.**

## 15. `A15` — gate invariants and pins

**MEASURED at commit 3, all four:**

    ^## P2- count                        14
    P2-PHASE-01                          Status: PROPOSED      (GATES.md:973)
    first prerequisite                   Prerequisite state: SATISFIED   (GATES.md:1011)
    second prerequisite                  Prerequisite state: SATISFIED   (GATES.md:1036)
    pin at line 1017                     MATCH
    pin at line 1040                     MATCH

**THE STATUS LINE WAS READ SCOPED TO ITS GATE SECTION**: the heading is at
`GATES.md:971`, and the status line was taken as the offset `971 + 2`. **A
bare first-hit grep returns line 209, a different gate.**

**The pins were verified by RECOMPUTING the target digests:**

    GATES.md:1017   4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
    sha256 derivations/P2-PHASE-01_microscopic_parameter_domain.md    identical

    GATES.md:1040   e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
    sha256 derivations/P2-PHASE-01_input_admissibility_contract.md    identical

## 16. `A16` — superseded branches, before the advance

**MEASURED at commit 3. Six separate exit statuses, all 1 — none is an
ancestor of the head:**

    52f65117  exit 1        7146a093  exit 1
    ebd531ab  exit 1        10c260b9  exit 1
    40168469  exit 1        d64cd912  exit 1

**The checker's `P4` independently reports `is_ancestor_of_head: false` and
`object_present: true` for all six.** The post-advance repetition is
post-report evidence and is not claimed here.

## 17. `A17` — the checker, MEASURED at commit 3

    base   ec85f66b05b3ed92cd924bc75273b74a73eee23b
    head   2cce4295dbeb0f046cd7c662d52da8ddb5823a40

    run 1 INCLUSIVE   exit 0   PASS   sha256 89031a28b8163d706b0d949f24806ab4419d8f895cef667be268cfd555c7d2ee
    run 1 EXCLUSIVE   exit 0   PASS   sha256 e5db2ee513cd3562beac9b728712d97c96f816549cb6cdf188ace440d560c898
    run 2 INCLUSIVE   exit 0   PASS   sha256 1a9bea37049c6b684923098e8d15093f6615b73799b15119849a1e931d0269d9
    run 2 EXCLUSIVE   exit 0   PASS   sha256 1b7c0a14420a245c65636d550507903ab0be80d2a9ade3350ff97935fe98d57a

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 PASS
    P6 PASS   P7 PASS   P8 PASS   P9 PASS

    NINE OF NINE IN EVERY INVOCATION.   commits_in_range 7.

### 17.1 What `RUN 1` did

**MEASURED: `RUN 1`'s default subject selection found BOTH specifications
in range and evaluated `P1` against each:**

    specs/2026-08-17T0322Z_d1c-dependency-reduction.md    stated 4 add / 0 mod   counted 4 / 0   parse OK
    specs/2026-08-17T0354Z_integrate-d1c-ledger.md        stated 7 add / 0 mod   counted 7 / 0   parse OK

**Both PASS.** `RUN 2` names only this task's specification, **which is why
the two runs produce different bytes.**

**The `C3` multi-specification residual did NOT arise.** MEASURED: `P3` and
`P7` both report `specification_paths_read` as BOTH specifications and
resolve to a single declared set each — `['DECISION_LOG.md']` and `[]` —
with `declared_source: specification`. **Two specifications, agreeing, no
conflict.** The trigger is a DIFFERENCE between declarations, not their
number; the residual is unchanged and remains unregistered.

### 17.2 `declared_source`, `P7` and `P9`

    P3   PASS   declared_source: specification   declared: ['DECISION_LOG.md']
    P7   PASS   declared_source: specification   section_count_head 14
    P9   PASS   reports/2026-08-17T0322Z_d1c-dependency-reduction.md   heading_present: true

**`P7` reports FOURTEEN sections. `PASS` at zero would have been a STOP.**

**MEASURED: `DECLARATION_CONFLICT` appears ZERO times in all four
outputs.**

**`P9` found the ARRIVING report and confirmed its `Stops and
clarifications` heading** — a property the source task's own range could
not exercise.

### 17.3 `RUN 1` config, verbatim — observational, governs nothing

    {
      "base": "ec85f66b05b3ed92cd924bc75273b74a73eee23b",
      "head": "2cce4295dbeb0f046cd7c662d52da8ddb5823a40",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 17.4 `RUN 2` config, verbatim — stop-governing

    {
      "base": "ec85f66b05b3ed92cd924bc75273b74a73eee23b",
      "head": "2cce4295dbeb0f046cd7c662d52da8ddb5823a40",
      "specification_paths": ["specs/2026-08-17T0354Z_integrate-d1c-ledger.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

**No value in either config is one I chose**, and **neither the config nor
this specification's declarations were adjusted to make `RUN 2` pass**.
**`RUN 2` passed on its first invocation at both readings.**

### 17.5 `RUN 1` output, verbatim, `INCLUSIVE` reading

    {
      "base": "ec85f66b05b3ed92cd924bc75273b74a73eee23b",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "2cce4295dbeb0f046cd7c662d52da8ddb5823a40",
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
                "derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md",
                "reports/2026-08-XXT{HHMM}Z_d1c-dependency-reduction.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_d1c-dependency-reduction.md",
                "specs/2026-08-XXT{HHMM}Z_d1c-dependency-reduction.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-17T0322Z_d1c-dependency-reduction.md",
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
                "derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md",
                "reports/2026-08-17T0322Z_d1c-dependency-reduction.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-d1c-ledger.md",
                "reviews/chatgpt/2026-08-17T0322Z_d1c-dependency-reduction.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-d1c-ledger.md",
                "specs/2026-08-17T0322Z_d1c-dependency-reduction.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-d1c-ledger.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-17T0354Z_integrate-d1c-ledger.md",
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
                "commit": "9c9b35ffd7b61e9d44e69f5aa222cd49fc68e42c",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "f395ee4f9ae2abc780f4b9e01b31ee6659a865a1",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "2cce4295dbeb0f046cd7c662d52da8ddb5823a40",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md"
                ]
              }
            ],
            "first_review_commit": "f395ee4f9ae2abc780f4b9e01b31ee6659a865a1",
            "first_work_commit": "2cce4295dbeb0f046cd7c662d52da8ddb5823a40",
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
              "specs/2026-08-17T0322Z_d1c-dependency-reduction.md",
              "specs/2026-08-17T0354Z_integrate-d1c-ledger.md"
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
              "merge": "2cce4295dbeb0f046cd7c662d52da8ddb5823a40",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "ec85f66b05b3ed92cd924bc75273b74a73eee23b",
              "recomputed_parent_1": "f395ee4f9ae2abc780f4b9e01b31ee6659a865a1",
              "recomputed_parent_2": "cdbfa6b9cb858d825a2047bd7683e96728d38c14",
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
              "commit": "9c9b35ffd7b61e9d44e69f5aa222cd49fc68e42c",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "f395ee4f9ae2abc780f4b9e01b31ee6659a865a1",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "050323ab144175ee54b03fab3043e9f5dabd3702",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "6f7fe5ff1afd3ec1ccbe4ab93c08237e97eecfb6",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "5d2f3c2bcd5a80dae11d2186b8be2f3873b04c76",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "cdbfa6b9cb858d825a2047bd7683e96728d38c14",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "2cce4295dbeb0f046cd7c662d52da8ddb5823a40",
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
              "specs/2026-08-17T0322Z_d1c-dependency-reduction.md",
              "specs/2026-08-17T0354Z_integrate-d1c-ledger.md"
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
            "first_commit": "9c9b35ffd7b61e9d44e69f5aa222cd49fc68e42c",
            "first_commit_paths": [
              "specs/2026-08-17T0354Z_integrate-d1c-ledger.md"
            ],
            "reports_added": [
              "reports/2026-08-17T0322Z_d1c-dependency-reduction.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-17T0354Z_integrate-d1c-ledger.md",
              "reviews/chatgpt/2026-08-17T0322Z_d1c-dependency-reduction.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-17T0354Z_integrate-d1c-ledger.md",
              "specs/2026-08-17T0322Z_d1c-dependency-reduction.md"
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
              "path": "reports/2026-08-17T0322Z_d1c-dependency-reduction.md",
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

### 17.6 `RUN 2` output, verbatim, `INCLUSIVE` reading

    {
      "base": "ec85f66b05b3ed92cd924bc75273b74a73eee23b",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "2cce4295dbeb0f046cd7c662d52da8ddb5823a40",
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
                "derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md",
                "reports/2026-08-17T0322Z_d1c-dependency-reduction.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-d1c-ledger.md",
                "reviews/chatgpt/2026-08-17T0322Z_d1c-dependency-reduction.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-d1c-ledger.md",
                "specs/2026-08-17T0322Z_d1c-dependency-reduction.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-d1c-ledger.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-17T0354Z_integrate-d1c-ledger.md",
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
                "commit": "9c9b35ffd7b61e9d44e69f5aa222cd49fc68e42c",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "f395ee4f9ae2abc780f4b9e01b31ee6659a865a1",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "2cce4295dbeb0f046cd7c662d52da8ddb5823a40",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md"
                ]
              }
            ],
            "first_review_commit": "f395ee4f9ae2abc780f4b9e01b31ee6659a865a1",
            "first_work_commit": "2cce4295dbeb0f046cd7c662d52da8ddb5823a40",
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
              "specs/2026-08-17T0354Z_integrate-d1c-ledger.md"
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
              "merge": "2cce4295dbeb0f046cd7c662d52da8ddb5823a40",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "ec85f66b05b3ed92cd924bc75273b74a73eee23b",
              "recomputed_parent_1": "f395ee4f9ae2abc780f4b9e01b31ee6659a865a1",
              "recomputed_parent_2": "cdbfa6b9cb858d825a2047bd7683e96728d38c14",
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
              "commit": "9c9b35ffd7b61e9d44e69f5aa222cd49fc68e42c",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "f395ee4f9ae2abc780f4b9e01b31ee6659a865a1",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "050323ab144175ee54b03fab3043e9f5dabd3702",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "6f7fe5ff1afd3ec1ccbe4ab93c08237e97eecfb6",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "5d2f3c2bcd5a80dae11d2186b8be2f3873b04c76",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "cdbfa6b9cb858d825a2047bd7683e96728d38c14",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "2cce4295dbeb0f046cd7c662d52da8ddb5823a40",
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
              "specs/2026-08-17T0354Z_integrate-d1c-ledger.md"
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
            "first_commit": "9c9b35ffd7b61e9d44e69f5aa222cd49fc68e42c",
            "first_commit_paths": [
              "specs/2026-08-17T0354Z_integrate-d1c-ledger.md"
            ],
            "reports_added": [
              "reports/2026-08-17T0322Z_d1c-dependency-reduction.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-17T0354Z_integrate-d1c-ledger.md",
              "reviews/chatgpt/2026-08-17T0322Z_d1c-dependency-reduction.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-17T0354Z_integrate-d1c-ledger.md",
              "specs/2026-08-17T0322Z_d1c-dependency-reduction.md"
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
              "path": "reports/2026-08-17T0322Z_d1c-dependency-reduction.md",
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

### 17.7 The `EXCLUSIVE` readings

**MEASURED by `diff`:**

    run 1   line 314 of 318:   "inclusivity": "INCLUSIVE"  →  "EXCLUSIVE"
    run 2   line 291 of 295:   "inclusivity": "INCLUSIVE"  →  "EXCLUSIVE"

**One line each, and nothing else.** `commits_out_of_scope` is empty in all
four.

## 18. `A18`, `A19` — validators and hygiene

**`A18`, MEASURED at commit 3, exit status 0:**

    324 passed, 2 deselected      in 45.78 s

**Expected 324 and 2; measured 324 and 2.**

**`A19`, MEASURED on commits 1–3. Commit 4 is post-report evidence:**

    commit 1   9c9b35ff   spec: integrate the reflection-positivity dependency ledger, and land it
               trailer hits 0      not amended
    commit 2   f395ee4f   review: pre-execution review for the dependency-ledger integration
               trailer hits 0      not amended
    commit 3   2cce4295   merge: integrate the reflection-positivity dependency ledger
               trailer hits 0      not amended

**MEASURED over the whole range, including the arriving commits: a scan for
`Co-Authored-By`, `claude.ai/code`, `Generated with`, `Claude-Session` and
`noreply@anthropic` returns ZERO.** **`P6` independently reports
`matches: []` for every commit in range.**

**Rule 20 binds this task and was NOT exercised.** **No force-push, no
branch deletion, no history rewrite of any kind** — including for the
`MP87` count at `§10.2`, which lands as written.

**Commits, MEASURED:**

    commit 1   9c9b35ffd7b61e9d44e69f5aa222cd49fc68e42c   specs/2026-08-17T0354Z_integrate-d1c-ledger.md
    commit 2   f395ee4f9ae2abc780f4b9e01b31ee6659a865a1   reviews/chatgpt/2026-08-17T0354Z_integrate-d1c-ledger.md
    commit 3   2cce4295dbeb0f046cd7c662d52da8ddb5823a40   --no-ff merge of cdbfa6b9…

**Commit 4's message, INTENDED:**

    report: the dependency ledger lands at its adopted granularity

## 19. `§8` — Rule 16 assessment

**Rule 16 is operative. All four junctions are addressed.**

### 19.1 First junction — a ledger of five named nodes reads as a to-do list, and is not one

**Each node is an ADOPTED DEPENDENCY-ACCOUNTING UNIT.** **Not a to-do item,
not a question, not a decision, not a problem, not a unit of effort.**

**A low node count means only that more `UD` occurrences have been grouped
under fewer accounting nodes AT THE ADOPTED GRANULARITY.** **It does not
establish fewer underlying questions, and it does not establish easier
work.**

**`R1` is the sharpest case.** It contains the canonical kinetic-operator
choice together with its delegated constituents — **the choice this
programme has repeatedly declined to make for want of independent physical
grounds.** **Its representation as ONE node must not make that ontological
ruling look like one atomic task.** **`R1` alone decomposes into four
constituents**, `§9.1`.

**And nothing in this line has produced a ground for making it.** `D-1`
found no `COVERED` verdict; `D-1b` found the gaps uniform across
candidates; `D-1c` grouped them without weighing them. **Not one of the
three produced a physical reason to prefer any operator.**

### 19.2 Second junction — RP applicability is not a ground for choosing the operator

**If a ruling on `R1` were made because it would reorganise `UD`
occurrences, the programme would be deriving its microscopic content from
what the fetched literature happens to prove.**

**That is the inversion the whole `D-pre` line exists to avoid.** The
operator is to be chosen on independent physical grounds and the
reflection-positivity obligation discharged for it — **not chosen because
discharging it looks cheaper for one candidate.**

**The ledger's arithmetic is on the wrong side of that line to be evidence
about physics**, and its per-candidate figures — `naive` 12 in-scope
occurrences, `Wilson` 5 — **are facts about which theorems `D-1` fetched,
not about which operator is right.**

### 19.3 Third junction — the 21 bridges are untouched and unmeasured

**A reduced `UD` figure beside an unreduced `UB` figure invites reading the
total as reduced. It is not.**

    covered by the reduction     33 of 54 tag occurrences
    untouched                    21 UB occurrences
    unclassified                  9 UNDETERMINED entries

**Nothing establishes whether the 21 are one bridge or twenty-one**, and
establishing it needs mathematics no task in this line has done. **They are
`NOT ESTABLISHED IN THE PRESENT EVIDENCE BASIS`, which is a statement about
the evidence and not about mathematics.**

### 19.4 Fourth junction — four bounded layers, and the bounds compose

**This rests on `D-1c`, which rests on `D-1b`, which rests on `D-1`.**

    D-1    literature search BOUNDED — ten works fetched, one not
    D-1b   RE-READ NOTHING — classified D-1's tables
    D-1c   DID NO MATHEMATICS — grouped D-1b's occurrences by repository anchor
    this   verified anchors and arithmetic; fetched nothing, computed nothing new

**Four layers, and the bounds compose.** **A gap absent from `D-1`'s tables
is absent from the ledger**, and nothing at layer four recovers what was
not visible at layer one.

## 20. Did landing a five-node ledger make me want to order the rulings, say which is easiest, or say what `R1` should be?

**All three. Ordering was much the strongest, and `§4` had to forbid it in
terms.**

**Ordering the rulings: strongest by a wide margin, and it presents itself
as helpful rather than as overreach.** Reading the five nodes, dependencies
between them seem to suggest themselves — **a measure is defined over
variables, an extent is a property of a lattice, and it feels obvious which
must come first.** **It is not obvious, and I have no evidence for any of
it.** `D-1c` established which occurrences each node bears; **it established
nothing about whether `R4` presupposes `R1`, and neither does the
repository at any line I read.** **The ordering that "suggests itself" is a
physics intuition wearing a dependency graph's clothes.** **Not written:
no node is ordered, called independent, or said to depend on another.**

**Saying which is easiest: moderate, and it comes through `R5`.** Two
occurrences, one anchor sentence, one symbol — **`R5` looks like the small
one.** It is a smaller number of occurrences and that is all. **Deciding
what `N` the programme fixes is a physics decision about internal
multiplicity, and the count of theorems that tripped over it says nothing
about that.** **No node is called small, large, cheap or ready.**

**Saying what `R1` should be: weakest, and the most clearly forbidden.**
The dossier lays out four candidates with their properties and the ledger
shows all four blocked on the same undelivered choice; **the pull is to
observe that one of them looks most tractable.** **That is operator
selection by literature convenience, which `§19.2` is the junction against.**
**Not written.**

**One further pull, specific to integrating rather than producing: to
correct the ledger's `MP87` count while landing it.** `§10.2` finds it
says eight where nine is right, the fix is one character, and the artifact
is passing through my hands. **`§4` forbids modifying it, and the
prohibition is right** — the ledger's own `R1` record already carries `W8`
correctly, so the repository will hold both the error and its correction,
which is a better record than a silently clean one. **The ledger lands
byte-identical**, `§4` of this report.

**I confirm: I did not order `R1`–`R5`, say which could be decided first,
or say which is independent; made, recommended and indicated a preference
for no ruling; grouped no `UB` pair and judged no two bridges the same
problem; classified no `UNDETERMINED` entry; estimated no effort and did not
state, for any node, how many gaps freezing it would retire; selected no
candidate; added no
register entry; modified no file; renamed no arriving path; and made
exactly one merge, with no rebase, no squash and no fast-forward at the
integration.**

## 21. Stops and clarifications

**NO STOP occurred.** The merge was clean, all four checker invocations
exited 0, `RUN 2` passed at both readings, the conflict list was empty, and
no acceptance criterion failed.

    SPECIFICATION_DEFECT                          0 stops, 0 findings
    ENVIRONMENT                                   0 stops, 0 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 1 finding
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 2 findings

### 21.1 `OBSERVATION_METHOD_ERROR` — one finding, mine, from the preceding task

**`D-1c`'s `MP87` roll-call says eight and the measured figure is nine**,
`§10.2`. **The omitted occurrence is `W8`.** I wrote that sentence, in the
`D-1c` report and in the ledger, and the ledger's own `R1` record
contradicts it two sections earlier.

**The cause is worth naming because it is not a counting error.** `W8` is
`r`, an operator PARAMETER, and the roll-call was written while thinking of
`MP87`'s occurrences as axis rows — `W3 W4 W5` are axes 3, 4 and 6, and
`W9` is a hypothesis. **`W8` is the other hypothesis-level occurrence and
it fell out of a list assembled by pattern rather than by counting the
table.** **The same table was counted correctly for every arithmetic
figure in the ledger**, which is why nothing else moved.

**Detected here by re-deriving the roll-call from `D-1b`'s tables instead
of transcribing it**, which is what `A9` requires. **`A9` is the criterion
that caught it.**

### 21.2 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — first finding

**Two artifacts landing on `main` now contain a statement this report finds
wrong**, `§10.2`, **and the specification that governs the landing repeats
it.** `§4` forbids modifying the arriving artifacts, so the error and its
correction land together in different files.

**That is the right disposition and it leaves a residual**: a reader
consulting the ledger's `§6.2` alone gets eight. **The ledger's `R1` record
and this report both give nine.** **Reported, NOT registered** — the
governance debt register is frozen at eleven and `§4` forbids an entry.

### 21.3 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — second finding

**`D-1c`'s "zero on every term" for `DECISION_LOG.md` is true of the terms
it searched and narrower than the sentence suggests**, `§8.4`. Bare
`measure` was not among its eight terms and returns three hits, none a
ruling.

**The conclusion survives; the search that supports it was narrower than
stated.** **This integration ran the broader term and read all three
hits**, so the assertion is now supported by a search that covers it.

**The general residual: no criterion in this line has required a lexical
hit count and a disposition to be reported as separate figures until this
task.** **`A7` is the first, and it caught something.** **Reported, NOT
registered.**

### 21.4 `SPECIFICATION_DEFECT` — nothing to report

**Nothing in this specification was found false about the repository or
about its own bytes** — **with the exception of the `MP87` count in its
`§2`, which is inherited from the arriving artifacts and is reported at
`§10.2` as a finding about them rather than about the specification.** Its
own pre-issue record does not assert the figure; it explicitly marks the
node figures `NOT MEASURED by this author`.

**Its pre-issue record was checked at four points** — the base, the source
and its non-ancestry, the two anchors it quotes, and the `DECISION_LOG`
sweep — **and MEASURED agrees at every one, including the three `measure`
hits and their dispositions.**

**Its `A7` `RETRACTED` note is the one to mark.** An earlier draft observed
the hit-count discrepancy and wrote that the hits "are consistent with" the
source's claim **without reading them** — supplying a reason for a source
rather than verifying it. **The repair requires every non-zero hit read.**
**I read all eight non-zero hits across both files**, `§8.3`.

### 21.5 `ENVIRONMENT`, `REPOSITORY_DEFECT` — nothing to report

**No environment failure occurred**, `§1`; **neither of Rule 13's two
diagnostic orders was exercised**, and nothing was installed.

**No defect in the repository was found.** Every path at the evidence base
is blob-identical at the head; the gate invariants hold; both pins
recompute; the checker passes nine of nine at both readings; the validators
are unchanged.

### 21.6 What I would have specified differently

**`A9` states the `MP87` figure as eight and asks for it re-derived.** That
is exactly the right construction and it worked — **but a criterion that
states an expected figure invites confirmation.** **I would have had `A9`
ask for the count without stating it**, as `A6` does for the node figures
by marking them `NOT MEASURED by this author`.

**And `A7`'s lexical-versus-ruling distinction should be a standing
requirement rather than this task's innovation.** It caught a real
narrowing here, and **every future task that searches the repository for a
later ruling will face the same trap.** **I would have had it written as a
convention rather than as one criterion.**

## 22. Evidence layering

**Committed in this report, MEASURED at commit 3:** `A1`–`A16`, `A18` and
`A19` for commits 1–3; `A17`'s four invocations with both configs and both
runs' output verbatim; `A12`'s scope base-to-commit-3 at 6 additions and 0
modifications, and the arriving counts; commits 1–3 SHAs and their stored
messages.

**Committed in this report, INTENDED:** commit 4's message; `A12`'s final
base-to-commit-4 scope of 7 additions and 0 modifications.

**Post-report evidence, returned to the Reviewer and NOT written back:**
`A12`'s final scope measured base-to-commit-4; `A17-final`, being `RUN 2`
re-run at commit 4 BEFORE the landing; `A15` and `A16` re-run after the
advance; `A19` for commit 4; the pre-advance `--is-ancestor` exit status;
the exact push command; remote `main` read back; the source tip unchanged;
confirmation that no other ref was pushed.

**Nothing in this report claims to measure commit 4.**
