# Execution report — integrate the `C-a` conventions consolidation, and land it

**Specification:** `specs/2026-08-14T2135Z_integrate-conventions-ca.md`
**Specification evidence base:** `bec0117168144d54fb23338b673cf7a7e4771868`
**Branch:** `governance/integrate-conventions-ca`, cut from authoritative `main` @ `bec01171…`
**Source merged:** `governance/conventions-consolidation-ca` @ `8de19fec0dd7e4ba52c2417f0dfe3fab84ae7ef6`
**Classification:** MATERIAL. Governed by Rule 15 and Rule 18.

**Every figure below is labelled MEASURED or INTENDED.** **This report is
written at commit 3, the merge commit, and measures nothing at commit 4.**

---

## 1. Outcome

**One merge, clean. Nothing auto-merged. Nothing edited.**

**MEASURED at commit 3:** 5 additions, 1 modification, 6 changed paths, empty
conflict list. `CONVENTIONS.md` is the only pre-existing file that changes
and it changes by addition only — **382 lines added, zero deleted**, with the
base file an exact in-order subsequence of the merged one, **1023 of 1023**.
All four checker invocations `PASS` at exit 0 with `P7` at 14 sections over
14 raw headings. Validators unchanged at 310.

    numbered rules      18 -> 21     contiguous 1..21
    amendment letters   A-I K L  ->  A-I K L M N O P     no J
    markers per principle            1 EXISTS   5 DEFERRED   1 RULE-ONLY

**What `main` will carry, and the reading it must not receive.** **The prose
contract is consolidated; most enforcement remains outstanding.** **Five of
the seven principles carry `MECHANISM DEFERRED` and prevent nothing by
themselves** — they record what should happen and rely on an author
remembering. **This merge converts hidden enforcement debt into countable
enforcement debt.** That is progress of a different kind, and §16 reports it
as the kind it is. **The governance gap is not closed.**

**Two deferred obligations are registered nowhere** — Amendment `N(b)`'s
review-digest comparison and Amendment `P(b)`'s line-survival check, both
fully specifiable inside the repository. **`C-c`'s debt set has grown and
this task has not registered them**, as §3 requires.

**A17, answered up front.** My harness's standing git guidance does instruct
a `Co-Authored-By` trailer and a session URL. **None was written on any of
the four commits**, nothing was suppressed by amendment, no commit was
amended.

---

## 2. Refs — A1, MEASURED

**Read from the remote after `git fetch origin`:**

    refs/heads/main                                        bec0117168144d54fb23338b673cf7a7e4771868   as specified
    refs/heads/governance/conventions-consolidation-ca     8de19fec0dd7e4ba52c2417f0dfe3fab84ae7ef6   as specified

**No mismatch. No stop.**

**§10's position figures, re-measured rather than quoted:**

    git rev-list --left-right --count bec0117...8de19fec    main-only 0, source-only 4
    is the source an ancestor of main?                      exit 1 — no

**Four commits ahead, zero behind, and not an ancestor. Agrees with §10.**

---

## 3. The pre-execution review — A2, MEASURED

    supplied specification    026d8ce8f81c62e75b7aec1878f2125f63a297e243d75bc27c2cfd4cd2708ecf
    committed specification   026d8ce8f81c62e75b7aec1878f2125f63a297e243d75bc27c2cfd4cd2708ecf   equal
    supplied review           3e1731fb77207ba10cdc392bce076ec7a8fddff009f95e6e85312066da18a6d8
    committed review          3e1731fb77207ba10cdc392bce076ec7a8fddff009f95e6e85312066da18a6d8   equal

The review's `reviewed specification SHA-256:` is filled in and reads
`026d8ce8f81c62e75b7aec1878f2125f63a297e243d75bc27c2cfd4cd2708ecf` — **the
digest of the specification actually committed and executed.** Committed
unedited, per Rule 18, and **before the merge**, per Rule 15's timing clause.

### 3.1 Which rules governed this task, and which land in it — A2

**This distinction is on the record because A2 requires it to be stated
rather than inferred.**

**GOVERNED THIS TASK — the eighteen rules and eleven amendments in force at
`bec01171…`.** Among them, and load-bearing here: **Rule 15** (governing
artifacts committed; specification first, review before the work it
authorises); **Rule 18** (review supplied as a file, executor verifies
correspondence, never authors or edits a review); **Rule 5** (merge
discipline); **Rule 11** (integration is a separate authorization); **Rule 7**
(evidence precedence); **Rule 16** (accumulated reading), which §16
discharges.

**LAND IN THIS MERGE, and bind prospectively FROM the landing — not before.**
Amendments **M, N, O, P** and Rules **19, 20, 21**.

**Amendment N in particular did not govern this task's own review.**
Amendment N(b) requires a review to record `reviewed specification SHA-256:`;
**this task's review does record it**, and that is a property of how the
review happened to be written, **not compliance with a rule that did not yet
exist.** **I claim no compliance with a rule that lands here**, and §8 of the
specification forbids exactly that claim.

**One observation worth its own sentence.** Amendment N(a) makes supplying
the specification as a file a producer-side obligation. **Both the
specification and the review arrived as FILES on this task**, which Rule 18
already required me to report. **That is the pre-existing Rule 18 obligation
being met, not the new one** — the new one binds the producer from the
landing forward.

---

## 4. Merge parentage — A3, three separately derived measurements

**Each by a different method, all taken BEFORE the merge existed.**

| Value | Method | MEASURED |
|---|---|---|
| parent 1 | `git rev-parse HEAD` on the branch tip after commit 2 | `1bd6060fc8fa1bd71cea9bfa203741730102ccc6` |
| parent 2 | `git rev-parse 8de19fec…^{commit}` — the pinned ref resolved to a commit object | `8de19fec0dd7e4ba52c2417f0dfe3fab84ae7ef6` |
| merge-base | `git merge-base HEAD 8de19fec…` — computed from the two | `bec0117168144d54fb23338b673cf7a7e4771868` |

**The merge-base equals the evidence base:** yes. **It is NOT parent 1** —
parent 1 carries this task's two commits, so the base lies behind it.
**Commit 1 is an ancestor of parent 1:** `git merge-base --is-ancestor
af26d6b5… 1bd6060f…` → **exit status 0**.

**Confirmed against the merge commit as stored:**

    git rev-list --parents -n 1 HEAD
    95dd796f…  1bd6060f…  8de19fec…

**A fourth derivation arrived from the checker.** `P5` recomputes parentage
and reports the same three values with `merge_base_equals_parent_1: false`.

---

## 5. The conflict list — A4, MEASURED

    git diff --name-only --diff-filter=U      (no output)
    unmerged path count                       0
    git ls-files -u | wc -l                   0

**Empty.** `git merge --no-ff --no-commit` printed only *"Automatic merge
went well; stopped before committing as requested"*.

**Additionally, MEASURED tree-wide over every tracked file at commit 3:** a
search for conflict markers at line start returns **0 hits**, over all
tracked paths with no directory exclusion.

---

## 6. Scope — A5

**MEASURED at commit 3, the merge commit:**

    M  CONVENTIONS.md
    A  reports/2026-08-14T1241Z_conventions-consolidation-ca.md
    A  reviews/chatgpt/2026-08-14T1241Z_conventions-consolidation-ca.md
    A  reviews/chatgpt/2026-08-14T2135Z_integrate-conventions-ca.md
    A  specs/2026-08-14T1241Z_conventions-consolidation-ca.md
    A  specs/2026-08-14T2135Z_integrate-conventions-ca.md

    additions 5   modifications 1   deleted/renamed/copied/type-changed/unmerged/unknown 0
    total changed paths 6

**INTENDED at commit 4:** 6 additions and 1 modification — the six above plus
`reports/2026-08-14T2135Z_integrate-conventions-ca.md`, giving the manifest's
seven paths.

**Both figures with the head each was measured at: 5/1 at commit 3
`95dd796f…`, MEASURED; 6/1 at commit 4, INTENDED.**

    6   changed paths at the merge commit
    4   contributed by source branch 8de19fec…   ← what A6 compares
    2   authored here and present at the merge   (this specification, this review)

---

## 7. Source-branch artifacts and the absence of an auto-merge — A6

**The four were DERIVED from the source branch —
`git diff --name-status bec0117 8de19fec` — not read from the
specification's list**, and the derivation returned exactly four, split three
added and one modified. **No disagreement to report.**

**Source tip blob vs merge-commit blob, all four:**

    CONVENTIONS.md                                                85b437869cface425ae1d5f3207644a599f2c9de   IDENTICAL
    reports/2026-08-14T1241Z_conventions-consolidation-ca.md      e7114dbcdc835cbbffa2a4b00ba439d8a170387b   IDENTICAL
    reviews/chatgpt/2026-08-14T1241Z_conventions-consolidation-ca.md
                                                                  416ed5a16248749640a9fdd82a20c80dfe119e78   IDENTICAL
    specs/2026-08-14T1241Z_conventions-consolidation-ca.md        a52b1695181bf9776456ae6cecd58d40ab67c512   IDENTICAL

**All four identical, `CONVENTIONS.md` among them.** **Not one byte of the
arriving text was authored, edited or reformatted by this task.**

### 7.1 Nothing was auto-merged — VERIFIED, not assumed

**A6 requires this verified rather than assumed, and it is verified three
ways.**

**(1) `git` reported no auto-merge.** The merge printed no `Auto-merging`
line for any path. Contrast the `P1` integration two tasks ago, which printed
three.

**(2) `main` cannot have touched `CONVENTIONS.md` since the source was cut.**
**MEASURED: the merge-base IS `main`** — `bec0117168144d54fb23338b673cf7a7e4771868`
is both the merge-base and `refs/heads/main`. There is no commit on `main`
after the merge-base, so there is no commit that could have touched the file.
**`git rev-list --count bec0117..bec0117 -- CONVENTIONS.md` returns 0**, which
is the same fact stated as a count.

**(3) The merged blob equals the SOURCE side exactly.**

    base   bec0117   b3c96300a1f3eab967d3d141a1e81b278887342c
    source 8de19fec  85b437869cface425ae1d5f3207644a599f2c9de
    merged 95dd796f  85b437869cface425ae1d5f3207644a599f2c9de   == source

**Here "merged equals one side" is the CORRECT result and not a warning
sign.** In an auto-merge of two changed sides it would mean a side was lost —
which is what Amendment `P(b)`, landing in this very merge, exists to detect.
**Here only one side changed the file, so taking that side whole is the only
correct outcome.** **The two situations produce the same measurement and mean
opposite things, and the difference is (2).**

---

## 8. `CONVENTIONS.md` grows by addition only — A7, two independent measurements

### 8.1 (i) Zero deleted lines

    git diff --numstat bec0117 HEAD -- CONVENTIONS.md      382 added, 0 deleted
    diff lines beginning with '-', excluding the '---' header      0

    hunk headers, all of the form -N,0 — every one a pure addition:
      @@ -260,0  +261,49 @@    Amendment P, into Rule 5
      @@ -335,0  +385,66 @@    Amendment M, into Rule 7
      @@ -777,0  +893,44 @@    Amendment O, into Rule 12
      @@ -1022,0 +1182,223 @@   Amendment N, Rules 19-21, and the consolidation record

### 8.2 (ii) The base file is an exact in-order subsequence of the merged file

    base line count       1023
    matched in order      1023
    merged line count     1405
    IN-ORDER SUBSEQUENCE  True

**Every one of the base file's 1023 lines appears in the merged file, in its
original order.**

### 8.3 Why both, stated as A7 states it

**(ii) is an INDEPENDENT preservation check, and that is its value.** It
establishes directly that every base line survives in its original order,
**rather than inferring preservation solely from `git`'s line-diff
accounting.**

**It is NOT stronger by covering a case (i) misses.** **A rewritten line
appears in a line diff as a deletion and an addition**, so (i) already
excludes rewriting under the stated measurement. **(ii) is stronger by not
depending on the same instrument** — it reads both files and compares them
directly, so a fault in `git`'s diff accounting would not propagate into both
answers.

**Both are required and both were performed. Two independent measurements of
one property are worth more than one**, which is the reasoning A7 gives and
which I am reporting rather than restating in my own terms.

---

## 9. Rule and amendment counts — A8, MEASURED at the head

    numbered rules      21
    sequence            1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21     contiguous, no gap
    amendment letters   A B C D E F G H I K L M N O P     fifteen
    Amendment J         0 occurrences

**Pre-existing survival, verified by extracting every `### ` heading and
every `**Amendment X,` heading from the base file and checking each appears
verbatim at the head:**

    pre-existing rule headings        18      missing at head   0
    pre-existing amendment headings   11      missing at head   0

**All eighteen rules and all eleven amendments are still present.**

---

## 10. Mechanism markers — A9, counted per principle

**Counted by BOUNDING each principle's text at the next heading and counting
within it — not by grepping the file.** Each of the seven carries exactly
one.

| Principle | Marker |
|---|---|
| Amendment M → Rule 7 | **RULE + MECHANISM DEFERRED** |
| Amendment N → Rule 18 | **RULE + MECHANISM DEFERRED** |
| Amendment O → Rule 12 | **RULE + MECHANISM DEFERRED** |
| Amendment P → Rule 5 | **RULE + MECHANISM DEFERRED** |
| Rule 19 — Pinned-artifact integrity | **RULE + MECHANISM EXISTS** |
| Rule 20 — Permitted pre-push hygiene repair | **RULE + MECHANISM DEFERRED** |
| Rule 21 — Artifact-state and statement-kind namespaces | **RULE-ONLY** |

    RULE + MECHANISM EXISTS      1
    RULE + MECHANISM DEFERRED    5
    RULE-ONLY                    1
    principles                   7

**As A9 expects: 1, 5, 1.**

### 10.1 The whole-file grep, and a sharpening of what produces twelve

**A9 warns that a whole-file grep returns twelve. MEASURED — it does, and it
is worth saying exactly which grep:**

    grep -c 'MECHANISM DEFERRED'                       7
    grep -c 'MECHANISM EXISTS'                         2
    grep -c 'RULE-ONLY'                                3
    total marker-TOKEN lines                          12

    grep -c 'Mechanism marker:'                        7      <- this one is correct

**The twelve comes from grepping the marker TOKENS, which the consolidation
record restates in its counts table and which one line uses to explain the
vocabulary.** **Grepping the marker LINE PREFIX — `Mechanism marker:` —
returns seven**, because that prefix appears only where a principle declares
its marker.

**I report this because it locates the error precisely rather than leaving
"a grep gives twelve" as folklore.** The failure was not that grepping is
wrong; it was that the token appears in prose about the markers as well as in
the markers themselves. **The per-principle bounding remains the method A9
requires and is what §10's table above is measured by.**

---

## 11. The consolidation record — A10, MEASURED

    section                    ## Consolidation record — C-a
    lines, at the source       57
    lines, at the merge head   57
    sha256, at the source      9f7ff5405d8015fcb3d6eeedfad91099f311bec29d9c362297beb44dbf659633
    sha256, at the merge head  9f7ff5405d8015fcb3d6eeedfad91099f311bec29d9c362297beb44dbf659633
    BYTE-IDENTICAL             True

**Unchanged. Not edited, not moved, not extended**, as §2's first PI ruling
requires.

**Lines containing `MUST`, `SHALL` or `binds`: ONE.** The line, quoted:

    **Nothing here binds; the rules and amendments it points to are what bind.**

**That is the sentence the PI's condition was checked against, and it is the
only one.** **All seven mechanism markers are attached to the amendments and
rules themselves, not to the record** — §10's table locates each one inside
its principle's own text.

---

## 12. The thirteen-row matrix — A11, MEASURED

    matrix rows                              13
    items found    A1 A2 A3 A4 A5 A6 A7 A8 B1 B2 B3 B4 E2
    each of the thirteen exactly once        True
    items not appearing exactly once         none

**Intact.**

---

## 13. Protected paths, gates and pins — A12 and A13

### 13.1 A12, MEASURED

    paths existing at the evidence base          389
    excluded (CONVENTIONS.md, the one modified)    1
    compared                                     388
    differing                                      0

    scripts/      0 differing        GATES.md                   2b3bd5069414f009e1a0466c4990db2949519bd8   IDENTICAL
    tests/        0 differing        DECISION_LOG.md            d9dd2bf3a8cca405f03b31c51b1f478c7db77ca2   IDENTICAL
    results/      0 differing        docs/BRANCHING_POLICY.md   3f0f35d4da448eb444d223fd003a5b0601792dc3   IDENTICAL
    derivations/  0 differing

### 13.2 A13 — gate invariants, MEASURED

    1.  ^## P2- section count          14
    2.  P2-PHASE-01                    Status: PROPOSED        (GATES.md line 973)
    3.  prerequisites                  ### Satisfied prerequisite — MICROSCOPIC PARAMETER DOMAIN        (line 1010)
                                       ### Satisfied prerequisite — PHASE INPUT / ADMISSIBILITY CONTRACT (line 1035)
                                       zero occurrences of "### Unsatisfied prerequisite"
    4.  pins                           2 found, both MATCH
                                         line 1017  derivations/P2-PHASE-01_microscopic_parameter_domain.md
                                         line 1040  derivations/P2-PHASE-01_input_admissibility_contract.md

**`GATES.md` is blob-identical to the evidence base**, so no gate, status,
prerequisite or pin changed.

### 13.3 A13 — `CONVENTIONS.md` is not pinned, VERIFIED

**This matters because this merge modifies `CONVENTIONS.md`, and Rule 19 —
which this merge lands — would oblige a re-pin if it were pinned.**

    'CONVENTIONS' references in GATES.md                              13
    pin-bearing lines                                                 1017, 1040 — two, and only two
    any pin line, or the five lines above one, naming CONVENTIONS     False

**Referenced thirteen times, pinned by neither pin. No re-pin is owed**, and
that is measured rather than assumed — which is what Rule 19 itself demands
of a task in this position.

---

## 14. The checker — A14, MEASURED at commit 3

    base   bec0117168144d54fb23338b673cf7a7e4771868
    head   95dd796f12d579348f687397d0f23dd23d9fa225   (commit 3, the merge commit)

**Both prospectivity readings for each of the two runs, so four invocations.
All four exited 0 with `overall: PASS`.**

    run 1 INCLUSIVE   exit 0   PASS   sha256 e35e53aaaa4a4712029058f96faf2cd4064cb86b8d0baaf4a434d71ecc1d8853
    run 1 EXCLUSIVE   exit 0   PASS   sha256 0902f7223458c32d752b0178ef6c5d690cb0e0a9ed7423dc75e1f18dffa6d385
    run 2 INCLUSIVE   exit 0   PASS   sha256 0597ff698d256df2d127af7f343e608e9fab6ac43596665e17bca81246615ee9
    run 2 EXCLUSIVE   exit 0   PASS   sha256 5c409a5c6dbc8ca425cea40756c7e19362fa866ccfb5dfef87a87571477a2560

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 PASS
    P6 PASS   P7 PASS   P8 PASS   P9 PASS

### 14.1 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "bec0117168144d54fb23338b673cf7a7e4771868",
      "head": "95dd796f12d579348f687397d0f23dd23d9fa225",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 14.2 RUN 2 config, verbatim — stop-governing

    {
      "base": "bec0117168144d54fb23338b673cf7a7e4771868",
      "head": "95dd796f12d579348f687397d0f23dd23d9fa225",
      "specification_paths": ["specs/2026-08-14T2135Z_integrate-conventions-ca.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I supplied of my own choosing; all are
taken from A14.** **`append_only_paths` is `["DECISION_LOG.md"]` and not
`[]`**, so `P3` is live. **`authorised_modified_gates` is `[]`, and here that
is truthful: no gate may change.** **The config was never adjusted to make
RUN 2 pass; it passed on its first invocation.**

### 14.3 The measured RUN 1 subject set — two specifications, where RUN 2 names one

**RUN 1's default selection chose TWO**, because the merge brings the source
task's specification into the range:

    specs/2026-08-14T1241Z_conventions-consolidation-ca.md   stated add 3 modify 1   counted add 3 modify 1   OK
    specs/2026-08-14T2135Z_integrate-conventions-ca.md       stated add 6 modify 1   counted add 6 modify 1   OK

**RUN 2 names only the second**, as A14 requires. **A real difference, not a
formatting one, so both JSON outputs are given verbatim below.** The two
prospectivity readings differ in exactly one line and in no verdict:

    280c280
    <         "inclusivity": "INCLUSIVE",
    ---
    >         "inclusivity": "EXCLUSIVE",

**`P1` compares per category on both** — the declared-total grammar landed
two tasks ago, reading the specification that consolidates the rule requiring
it.

### 14.4 `P7`, and the section count it saw

    raw_heading_count_base   14        section_count_base   14
    raw_heading_count_head   14        section_count_head   14
    unauthorised_changed     []        added_sections  []   removed_sections  []

**`PASS` at fourteen sections. `PASS` at zero would have been a STOP.**

### 14.5 RUN 1 output, verbatim

    {
      "base": "bec0117168144d54fb23338b673cf7a7e4771868",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "95dd796f12d579348f687397d0f23dd23d9fa225",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "counted": 4,
              "counted_add": 3,
              "counted_modify": 1,
              "counted_set": [
                "reports/2026-08-XXT{HHMM}Z_conventions-consolidation-ca.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_conventions-consolidation-ca.md",
                "specs/2026-08-XXT{HHMM}Z_conventions-consolidation-ca.md",
                "CONVENTIONS.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-14T1241Z_conventions-consolidation-ca.md",
              "stated": 4,
              "stated_add": 3,
              "stated_modify": 1,
              "stated_record": "stated: 3 additions, 1 modification"
            },
            {
              "counted": 7,
              "counted_add": 6,
              "counted_modify": 1,
              "counted_set": [
                "reports/2026-08-14T1241Z_conventions-consolidation-ca.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-conventions-ca.md",
                "reviews/chatgpt/2026-08-14T1241Z_conventions-consolidation-ca.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-conventions-ca.md",
                "specs/2026-08-14T1241Z_conventions-consolidation-ca.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-conventions-ca.md",
                "CONVENTIONS.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-14T2135Z_integrate-conventions-ca.md",
              "stated": 7,
              "stated_add": 6,
              "stated_modify": 1,
              "stated_record": "stated: 6 additions, 1 modification"
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
                "commit": "af26d6b55376e1f08ac4694a2ee2c5918ccfbdcd",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "1bd6060fc8fa1bd71cea9bfa203741730102ccc6",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "95dd796f12d579348f687397d0f23dd23d9fa225",
                "work_paths": [
                  "CONVENTIONS.md"
                ]
              }
            ],
            "first_review_commit": "1bd6060fc8fa1bd71cea9bfa203741730102ccc6",
            "first_work_commit": "95dd796f12d579348f687397d0f23dd23d9fa225",
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
          "evidence": [
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
              "merge": "95dd796f12d579348f687397d0f23dd23d9fa225",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "bec0117168144d54fb23338b673cf7a7e4771868",
              "recomputed_parent_1": "1bd6060fc8fa1bd71cea9bfa203741730102ccc6",
              "recomputed_parent_2": "8de19fec0dd7e4ba52c2417f0dfe3fab84ae7ef6",
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
              "commit": "af26d6b55376e1f08ac4694a2ee2c5918ccfbdcd",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "1bd6060fc8fa1bd71cea9bfa203741730102ccc6",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "4aa0b5f7e0d75750124b4bf53dbff3cd89e35e09",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "829442de6029f233b1f3b1c2a2ab9f816cd0af5d",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "e8308d3d3f7a284fabb4d02f1f724a396c4d5002",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "8de19fec0dd7e4ba52c2417f0dfe3fab84ae7ef6",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "95dd796f12d579348f687397d0f23dd23d9fa225",
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
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "unauthorised_changed": []
          },
          "id": "P7",
          "status": "PASS",
          "title": "gate integrity"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "first_commit": "af26d6b55376e1f08ac4694a2ee2c5918ccfbdcd",
            "first_commit_paths": [
              "specs/2026-08-14T2135Z_integrate-conventions-ca.md"
            ],
            "reports_added": [
              "reports/2026-08-14T1241Z_conventions-consolidation-ca.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-14T2135Z_integrate-conventions-ca.md",
              "reviews/chatgpt/2026-08-14T1241Z_conventions-consolidation-ca.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-14T2135Z_integrate-conventions-ca.md",
              "specs/2026-08-14T1241Z_conventions-consolidation-ca.md"
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
              "path": "reports/2026-08-14T1241Z_conventions-consolidation-ca.md",
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

### 14.6 RUN 2 output, verbatim

    {
      "base": "bec0117168144d54fb23338b673cf7a7e4771868",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "95dd796f12d579348f687397d0f23dd23d9fa225",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "counted": 7,
              "counted_add": 6,
              "counted_modify": 1,
              "counted_set": [
                "reports/2026-08-14T1241Z_conventions-consolidation-ca.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-conventions-ca.md",
                "reviews/chatgpt/2026-08-14T1241Z_conventions-consolidation-ca.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-conventions-ca.md",
                "specs/2026-08-14T1241Z_conventions-consolidation-ca.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-conventions-ca.md",
                "CONVENTIONS.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-14T2135Z_integrate-conventions-ca.md",
              "stated": 7,
              "stated_add": 6,
              "stated_modify": 1,
              "stated_record": "stated: 6 additions, 1 modification"
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
                "commit": "af26d6b55376e1f08ac4694a2ee2c5918ccfbdcd",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "1bd6060fc8fa1bd71cea9bfa203741730102ccc6",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "95dd796f12d579348f687397d0f23dd23d9fa225",
                "work_paths": [
                  "CONVENTIONS.md"
                ]
              }
            ],
            "first_review_commit": "1bd6060fc8fa1bd71cea9bfa203741730102ccc6",
            "first_work_commit": "95dd796f12d579348f687397d0f23dd23d9fa225",
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
          "evidence": [
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
              "merge": "95dd796f12d579348f687397d0f23dd23d9fa225",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "bec0117168144d54fb23338b673cf7a7e4771868",
              "recomputed_parent_1": "1bd6060fc8fa1bd71cea9bfa203741730102ccc6",
              "recomputed_parent_2": "8de19fec0dd7e4ba52c2417f0dfe3fab84ae7ef6",
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
              "commit": "af26d6b55376e1f08ac4694a2ee2c5918ccfbdcd",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "1bd6060fc8fa1bd71cea9bfa203741730102ccc6",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "4aa0b5f7e0d75750124b4bf53dbff3cd89e35e09",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "829442de6029f233b1f3b1c2a2ab9f816cd0af5d",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "e8308d3d3f7a284fabb4d02f1f724a396c4d5002",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "8de19fec0dd7e4ba52c2417f0dfe3fab84ae7ef6",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "95dd796f12d579348f687397d0f23dd23d9fa225",
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
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "unauthorised_changed": []
          },
          "id": "P7",
          "status": "PASS",
          "title": "gate integrity"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "first_commit": "af26d6b55376e1f08ac4694a2ee2c5918ccfbdcd",
            "first_commit_paths": [
              "specs/2026-08-14T2135Z_integrate-conventions-ca.md"
            ],
            "reports_added": [
              "reports/2026-08-14T1241Z_conventions-consolidation-ca.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-14T2135Z_integrate-conventions-ca.md",
              "reviews/chatgpt/2026-08-14T1241Z_conventions-consolidation-ca.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-14T2135Z_integrate-conventions-ca.md",
              "specs/2026-08-14T1241Z_conventions-consolidation-ca.md"
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
              "path": "reports/2026-08-14T1241Z_conventions-consolidation-ca.md",
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

---

## 15. Validators — A15, MEASURED

    before, at the evidence base bec0117…    310 passed, 2 deselected
    after,  at the merge commit 95dd796f…    310 passed, 2 deselected     exit 0

**Unchanged, as A15 expects: this merge adds no test. No change to explain.**

**The "before" figure was measured** by checking out the evidence base in a
separate worktree and running the suite there, not quoted. The temporary
worktree was removed.

---

## 16. Superseded branches — A16, MEASURED before the advance

    52f65117   exit 1      ebd531ab   exit 1      40168469   exit 1
    7146a093   exit 1      10c260b9   exit 1      d64cd912   exit 1

**Exit 1 means NOT an ancestor, the required result, for all six.** **No
superseded-register entry was written; nothing is superseded by this task.**

---

## 17. Commits — A17, MEASURED for commits 1–3

    commit 1   af26d6b55376e1f08ac4694a2ee2c5918ccfbdcd   specs/2026-08-14T2135Z_integrate-conventions-ca.md
    commit 2   1bd6060fc8fa1bd71cea9bfa203741730102ccc6   reviews/chatgpt/2026-08-14T2135Z_integrate-conventions-ca.md
    commit 3   95dd796f12d579348f687397d0f23dd23d9fa225   --no-ff merge of 8de19fec…

    UTC token fixed by commit 1:  2135Z        day at execution: 14

**Stored subjects, MEASURED:**

    commit 1   spec: integrate the C-a conventions consolidation, and land it
    commit 2   review: pre-execution review for the C-a conventions integration
    commit 3   merge: integrate the C-a conventions consolidation

| Commit | `Co-Authored-By` | session id or URL | tool attribution | Trailer suppressed? |
|---|---|---|---|---|
| 1 | none | none | none | **No — none was ever written** |
| 2 | none | none | none | **No — none was ever written** |
| 3 | none | none | none | **No — none was ever written** |

**Commit 4's message, INTENDED:**

    report: the C-a conventions consolidation lands on main

**Commit 4 is post-report evidence. Nothing in this report measures it.**

**`F1`, met and unrepaired.** The guidance is live in this session; each
message was composed without the trailers at first writing. **No commit was
amended and no history was rewritten.** `P6` reports `PASS` on all three
commits in every one of the four invocations.

**Rule 20, which lands in this merge, would have permitted an amend had a
trailer reached a commit.** **It did not, and Rule 20 was not operative for
this task in any case** — it binds prospectively from the landing, and the
landing had not occurred. **No amend was made and none was needed.**

---

## 18. Rule 16 assessment — all three junctions

### 18.1 First — twenty-one rules, and five of seven principles prevent nothing

**`main` will carry twenty-one rules where it carried eighteen, covering
twelve failures that previously had none. A reader may take that for the
failures being prevented. It is not.**

**The marker totals, beside the rule count, as §7 requires:**

    numbered rules on main       18 -> 21
    amendments                   11 -> 15
    principles landing            7
      RULE + MECHANISM EXISTS     1     Rule 19, enforced by tests/test_gate_pins.py
      RULE + MECHANISM DEFERRED   5     Amendments M, N, O, P and Rule 20
      RULE-ONLY                   1     Rule 21

**The prose contract is consolidated while most enforcement remains
outstanding.** **A rule marked `MECHANISM DEFERRED` records what should
happen and relies on an author remembering to do it.** **Five of seven.**

**Where a reader meets this on `main` after the merge** — named as locations,
not as a general caution:

- **`CONVENTIONS.md`, the consolidation record**, which carries the marker
  counts and the sentence that five of seven being deferred is the size of
  what `C-b` and `C-c` still owe;
- **each principle's own text**, which names its missing enforcement and
  where it is registered;
- **`derivations/GOVERNANCE-ENFORCEMENT_classification.md` §5**, unchanged by
  this merge, still recording twenty-two of twenty-nine objects with no
  machine behind them.

**What this merge actually achieves, stated as the kind of progress it is:**
**it converts hidden enforcement debt into countable enforcement debt.**
Before, the twelve failures were recorded in one classification draft and in
scattered reports. Now the obligations are in the governing file and each
says whether anything enforces it. **Countable is better than hidden. It is
not the same as enforced.**

### 18.2 Second — writing a rule is not detecting a violation

**Every one of the twelve failures was identified, interpreted or repaired
through human review or re-measurement.** **Landing the rules changes neither
fact**: seven principles now exist where none did, and **not one of them
observes anything.** Six rely on an author or reviewer applying them; the
seventh relies on a suite someone must run.

**Some underlying violations WERE mechanically caught, and `B4` is the
counterexample that keeps this claim honest.** The commit-hygiene violation
behind Rule 20 was caught by the checker at exit 2, on an unpushed commit,
before any publication. **A machine found the violation.** What no machine
did was observe that the harness would supply the trailer on every future
task, that no rule permitted the repair, or that the permission needed
conditions — **each of those came from human review.**

**Detection of a violation and identification of a governance gap are
different acts, and only the first was ever mechanical.**

### 18.3 Third — the rule set covers what was noticed

**The classification behind these rules is a list assembled across one
working session, not a survey.** **Several of its items were found only
because a later task tripped over them** — `A7`'s reading-list gap surfaced
because an executor found evidence outside its own reading list; `B3`'s
insufficiency surfaced because an executor measured beyond its criterion.

**So the twenty-one rules cover the observed failures and are silent about
the unobserved ones.** **The absence of a rule is not evidence that the
corresponding failure cannot occur** — it is evidence that nobody has yet
tripped over it. **That sentence travels with the rules**: it is carried in
the consolidation record on `main`, not only in this report.

**A search I did not perform.** I did not attempt to derive further failure
modes from first principles, and this task was not scoped to. **The rule
set's completeness is exactly the classification's, which the classification
itself declines to claim.**

---

## 19. Does `main` now read as though the governance gap were closed?

**No, and the honest answer needs the qualification.**

**MEASURED:** no file on `main` states the gap is closed; the classification's
§5 count is unchanged by this merge; `P1`, `P3` and `P7` still read
`PARTIAL`; and the consolidation record states in its own text that five of
seven principles are deferred.

**Where the residual risk lies.** **A conventions file growing from eighteen
rules to twenty-one reads as governance getting stronger, and a reader who
counts rules rather than markers will read it that way.** The rule count rose
by three; **the count of obligations anything enforces rose by one.**

**The mitigation on `main` is that every principle declares its own marker,
so the reader who looks finds it in the same paragraph as the rule.** **It is
an annotation, not a mechanism.** Nothing prevents a reader from skipping it.

---

## 20. The landing — INTENDED at the time of writing

**This task ends with authoritative `main` at its own final report commit,
named as commit 4 and not as a SHA**, because any SHA naming a commit that
carries this task's review is unreachable as a landing target under Rule 15.

**INTENDED, and measured only as post-report evidence:** the pre-advance
`--is-ancestor` exit status; a fast-forward push **without `--force` and
without `--force-with-lease`**;
`governance/conventions-consolidation-ca` neither deleted nor moved, its tip
verified after the advance; A13 and A16 re-run after the advance; A14-final
before the landing, **which stops the advance if it fails.**

**Nothing in this report claims the landing has happened.**

---

## 21. Stops and clarifications

### 21.1 Stops

**None.** No stop was reached in any of the five primary categories:
`SPECIFICATION_DEFECT`, `ENVIRONMENT`, `OBSERVATION_METHOD_ERROR`,
`REPOSITORY_DEFECT`, `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`.

**Every stop condition the specification names was tested and none
triggered:** A1's two refs matched; A2's review names the executed digest;
A4's conflict list is empty; A7 reports zero deletions and 1023 of 1023
matched; A9's per-principle count is 1/5/1; A10's record is byte-identical
with one binding-vocabulary line; A13 shows `GATES.md` unchanged; A14's RUN 2
exited 0 with `P7` at fourteen sections.

### 21.2 Secondary findings

**S1 — a sharpening of A9's warning, not a correction.** A9 says a whole-file
grep returns twelve. **It does — but only when grepping the marker TOKENS.**
Grepping the marker line prefix `Mechanism marker:` returns **seven**, the
correct figure. §10.1 gives both. **The distinction locates the error: the
tokens appear in prose about the markers as well as in the markers
themselves.** I report it because "a grep gives twelve" left as folklore
would mislead the next person to check.

**S2 — observation on A6's "merged equals source".** For `CONVENTIONS.md` the
merged blob equals the source blob exactly. **In an auto-merge of two changed
sides that measurement would mean a side was lost** — which is what Amendment
`P(b)`, landing in this merge, exists to detect. **Here it is the correct
result**, because only one side changed the file. §7.1 measures the
difference rather than asserting it. **The same number means opposite things
in the two cases, and only the merge-base measurement tells them apart.**

**S3 — `C-c`'s debt set has grown and this task did not register it.**
Amendment `N(b)`'s review-digest comparison and Amendment `P(b)`'s
line-survival check are both fully specifiable inside the repository and
registered under no mechanism item; the marker-vocabulary placement question
is likewise open. **§3 forbids this task from registering any of them, and it
has not.** **`C-c` should be told.**

**F1 and F2.** `F1` — the harness's forbidden trailer — **met and
unrepaired**, §17. `F2` — the `frozen Wilson D` docstring — **not met in this
task's reading**; `scripts/` is 0 paths differing, so it stands where it was.

### 21.3 Ambiguous, unsatisfiable, or what I would have specified differently

**Nothing was unsatisfiable, and no instruction was inconsistent with a
repository rule or with another instruction.** Three observations:

1. **A7's justification is the version I would keep, and it is worth saying
   why.** The earlier version claimed that a zero-deletion diff permits a
   line being rewritten and re-added elsewhere; **that is false, and the
   corrected text says so and gives the better reason** — independence of
   instrument rather than coverage of a missed case. **A specification that
   corrects its own reasoning in place, and says which claim it withdrew, is
   easier to execute than one that merely arrives correct**, because the
   executor can see which reading was rejected.
2. **A9's warning about the twelve is the most useful sentence in the
   specification**, and it prevented an error I would otherwise have been
   likely to make — the first thing one reaches for is a whole-file grep.
   **I would have added which grep gives seven**, which §10.1 now supplies.
3. **A6 asks for "nothing was auto-merged" to be verified rather than
   assumed but does not say how.** I verified it three ways (§7.1), of which
   the merge-base identity is the only one that would still hold if `git`'s
   output format changed. **I would have named the merge-base check
   specifically**, since the absence of an `Auto-merging` line is a property
   of a tool's messages rather than of the repository.

### 21.4 Rule 13

**No environment failure occurred, so neither of Rule 13's two diagnostic
orders was exercised.** **Rule 13 carries two such orders, a known open item;
I name neither as the one that applies.**

    Python   3.11.15
    pytest   9.1.1

**Nothing was installed.**

---

## 22. Evidence layering

**Committed in this report, MEASURED at commit 3:** A1–A13 and A15–A17 for
commits 1–3; A14's four invocations with both configs and both JSON outputs;
commits 1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; A5's final
base-to-head scope of 6 additions and 1 modification.

**Post-report evidence, returned to the Reviewer and NOT written back:** A5's
final scope measured base-to-commit-4; A14-final, being RUN 2 re-run at
commit 4 before the landing; A13 and A16 re-run after the advance; A17 for
commit 4; the pre-advance `--is-ancestor` exit status; the exact push
command; remote `main` read back; the source tip unchanged; final ancestry
confirmation.

**Nothing in this report claims to measure commit 4.**
