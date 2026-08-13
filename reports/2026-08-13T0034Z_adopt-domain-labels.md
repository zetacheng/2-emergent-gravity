# Report — repair the adopted domain's operative status label, and sweep the rest

Specification: `specs/2026-08-13T0034Z_adopt-domain-labels.md`
Review: `reviews/chatgpt/2026-08-13T0034Z_adopt-domain-labels.md` — APPROVED FOR EXECUTION
Evidence base: `cd1ebd84ca588a8ec946fc89e692f9e34760713d` (`science/adopt-parameter-domain-repair`)
Branch: `science/adopt-parameter-domain-labels`, cut from that commit.
**Authoritative `main` = `1cb5550f…`, NOT touched and not merged.**

**Every figure is labelled MEASURED or INTENDED.** **Nothing here claims to
measure commit 5.**

---

## 0. Executive summary

**One anchored edit, one re-pin, and the census.** The OLD label was found
verbatim exactly once; the artifact diff is one region at line 85 under both
zero and default context. `GATES.md` changed in one region, one digest string.
**A6 finds two pins and both MATCH.** All five A7 invariants hold. **A9's
RUN 2 — stop-governing — PASSED exit 0 on both prospectivity readings.**

**A5's census reconciles to the specification's fourteen, and it does so at the
head only because two pattern errors cancel.** That is the finding of this
report and it is stated before the table rather than after it:

- **the specification's own label pattern does not match the NEW label.** The
  repaired line 85 reads `**ADOPTED.**`, and `ADOPTED` is not among
  `MEASURED | PI RULING | DERIVED | RECOMMENDATION | CAUTION | Status:`.
  **MEASURED: the pattern does not match line 85 at the head.**
- **the pattern does match line 88, which is not a label.** The repaired text
  quotes the old label — `` `RECOMMENDATION, for PI adoption` `` — inside
  backticks, and the pattern picks the quotation up.

**One label the census should see and misses, one non-label it counts. 17 raw
lines and 14 labelled statements at both revisions, by arithmetic that is right
and reasoning that is not.** §5 gives the corrected census.

**A further observation, reported and left per §2:** the repair introduces
`ADOPTED` as a kind label at line 85, and **the artifact's vocabulary at lines
25–28 defines four kinds and does not include it.** §3 mandates the replacement
text verbatim and §2 forbids touching the vocabulary definition, so I changed
neither.

**No further STALE label was found.** The three surviving `RECOMMENDATION`
labels were each read in place and are CURRENT. **Nothing was repaired beyond
§3.**

**`C1`, `C2` and `C3` were not answered.** No physics was computed.
**`P7` returned `PASS` and it is evidence of nothing.** §7.

**One thing I got wrong in the previous task's report, and it is why this task
exists.** I found line 85 in that task's fourth-defect search, reported it with
its line number, and **classified it CURRENT** — *"a label on the recommendation
the PI has since ruled on rather than a claim that the artifact awaits
adoption."* **That classification was wrong.** Line 28 defines `RECOMMENDATION`
as binding nobody, which makes the label a claim about state and not a
structural description. **Reporting it rather than repairing it is what let the
PI and Reviewer overrule me; had I stayed silent, there would have been no
fourth round to correct it in.**

---

## 1. A1 — Refs

**MEASURED**, read from the remote:

```
cd1ebd84ca588a8ec946fc89e692f9e34760713d	refs/heads/science/adopt-parameter-domain-repair
1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab	refs/heads/main
```

**Both match. No STOP.**

## 2. A2 — The review, committed unedited, with its specification digest

**MEASURED.** The review carries, at its head and again in its disposition:

    reviewed specification SHA-256:
      d358a9d9f021291eef380f65373686060d1e10473b9d0e29134038d545109ee7

**It is filled in and it is correct:**

    supplied specification file, sha256
      d358a9d9f021291eef380f65373686060d1e10473b9d0e29134038d545109ee7   EQUAL

**Not blank, not a different digest. A2's stop is not triggered.** The review
also states outright that it approves *"the specification identified by the
SHA-256 above"* and not *"a different transcription, later revision, or
substituted file"*.

    supplied review   c2741ceea3eb7d77b8312569a20196ed14c40643df1358c447291f86c7439fb5
    committed blob    c2741ceea3eb7d77b8312569a20196ed14c40643df1358c447291f86c7439fb5
    EQUAL

**Both arrived as FILES.** Rule 18 satisfied on both; neither was pasted.
**Still practice rather than rule: no repository convention requires the
digest.**

## 3. A3 — Pinned inputs at the evidence base

**MEASURED.**

    derivations/P2-PHASE-01_microscopic_parameter_domain.md, sha256
      a481955be9bfa248b925ef7bf49f0f57cc462799ee72278507f71f99ac70cfc8
    A3 requires
      a481955be9bfa248b925ef7bf49f0f57cc462799ee72278507f71f99ac70cfc8
    EQUAL — no STOP

**Git blob ids at `cd1ebd84`:**

```
eb01088018361db34361e717082f0d8c52fef445  GATES.md
c7910bc6a6cca5c684b082aef87de85b6a3d6f4c  derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md
f6f0e524daa11f2f8e3470cc4ab44fd3f6630615  derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
```

**The specification's own line-number claims, checked before use:**

    file length                     425 lines        as §11 states
    line 85                         "**RECOMMENDATION, for PI adoption.**"
    the OLD anchor's count          exactly 1
    line 28 defines RECOMMENDATION  "the Researcher's and binds nobody"
    other RECOMMENDATION labels     lines 131, 252, 357   as §0 states
    GATES.md:1017 pin count         exactly 1

**One off-by-one in §11, and it changes nothing.** §11 says
`## 3. The domain` is *"at line 84"*. **MEASURED: it is at line 83**; line 84 is
blank and line 85 is the label. §0's looser phrasing — the label sits
*"immediately under"* the heading — is correct.

## 4. A4 — The one anchored edit

**MEASURED.**

    artifact, before   a481955be9bfa248b925ef7bf49f0f57cc462799ee72278507f71f99ac70cfc8
    artifact, after    4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214

**The "after" digest is read from the COMMITTED BLOB at commit 3**, not from a
working-tree file, because §4's re-pin embeds it.

**ONE operation. The OLD anchor was required to occur exactly once; a count
other than one was coded to abort, not to search for a near match.**

    OLD anchor  "**RECOMMENDATION, for PI adoption.**"   1 match, substituted

**CONTEXT SETTING STATED, because a hunk count without it is not a
measurement:**

    git diff --unified=0    1 region
    git diff (--unified=3)  1 region

**Both settings give one region, so no coalescing question arises here.**
**Changed-line accounting: 1 line removed, 6 added, all at line 85.**

**Full diff at `--unified=0`:**

```diff
+++ b/derivations/P2-PHASE-01_microscopic_parameter_domain.md
@@ -85 +85,6 @@ as physics.
-**RECOMMENDATION, for PI adoption.**
+**ADOPTED.** The domain below was proposed by the Researcher and
+**adopted by the PI**; it is the operative content of this artifact
+and it binds. **An earlier version of this line read
+`RECOMMENDATION, for PI adoption`, which line 28 defines as binding
+nobody** — a label left behind when the artifact's status changed,
+and the last of four such labels to be corrected.
```

**Nothing in `## 3. The domain` changed** — not the range, not the sixteen
values, not the treatment of `mu` or of `a`. **Only the label above it.** The
diff's single region begins and ends at line 85; the domain block itself starts
below it and is untouched.

**The replacement keeps the record of its own repair** rather than reading as
though the label had always been right, and **names its own line 28 as the
definition it contradicted.** A later reader can see what was wrong.

**And it is the reviewer's caution, restated because §5 of the review asks for
it to be preserved:** `it binds` means **the adopted domain and its adopted
input treatment bind this gate's governed enumeration.** **It does NOT mean the
artifact establishes phase admissibility, root completeness, thermodynamic
dominance, finite-density coverage, or any result the artifact expressly leaves
open.** The artifact's §7 and its boundary statement are unchanged and still say
so.

## 5. A5 — The sweep

**MEASURED at the head, over the whole 430-line file, with no `head`, no
`tail`, and no sampling.**

### The census, corrected for what the specification's pattern gets wrong

    LINE   LABEL                                    CURRENT / STALE
      3    Status: ADOPTED                          CURRENT
     25-28 the vocabulary definition                CURRENT — a definition of
                                                    four kinds, not a claim
                                                    about state. ONE entry.
     52    MEASURED                                 CURRENT
     64    MEASURED                                 CURRENT
     85    ADOPTED                                  CURRENT — repaired by A4;
                                                    was the one STALE entry
                                                    at the evidence base
    134    PI RULING (2026-08-12)                   CURRENT
    136    RECOMMENDATION on how to record          CURRENT
    167    DERIVED, not chosen                      CURRENT
    185    MEASURED                                 CURRENT
    224    CAUTION                                  CURRENT
    236    MEASURED                                 CURRENT
    257    RECOMMENDATION, deliberately weaker      CURRENT
    283    MEASURED                                 CURRENT
    362    RECOMMENDATION                           CURRENT

    14  labelled statements at the head
     0  STALE
     1  entry repaired by this task (line 85)

**Line numbers from 134 onward are the evidence base's shifted by +5**, the six
lines A4 added less the one it removed. MEASURED, entry by entry: 129→134,
131→136, 162→167, 180→185, 219→224, 231→236, 252→257, 278→283, 357→362.

### The counting rule, and both numbers

**Under the specification's pattern
`MEASURED | PI RULING | DERIVED | RECOMMENDATION | CAUTION | Status:`:**

    17  matching lines at the evidence base
    17  matching lines at the head
    -4  the four definition lines at 25-28
    +1  counted once, as the definition
    ------
    14  labelled statements, at both revisions

**My count is fourteen and it agrees with §5's. I did not reconcile it to
fourteen — it arrived there.** But **the membership at the head is not what the
arithmetic suggests**, and this is the finding:

    at the evidence base, the 17 lines include line 85, the STALE label
    at the head,            the 17 lines include line 88 INSTEAD — the
                            quotation of the old label inside the repaired
                            text — and DO NOT include line 85's new
                            "**ADOPTED.**" label at all

**MEASURED, both halves:**

    sed -n '85p' | grep -E <the specification's pattern>   ->  NO MATCH
    line 88 reads: `RECOMMENDATION, for PI adoption`, which line 28 defines as binding

**So one real label is invisible to the pattern and one non-label is counted,
and the two cancel exactly.** **A census whose total is right because its errors
offset is not a census that would have caught a change of a different size.**
**If the replacement text had quoted the old label twice, or not at all, the
pattern's total would have moved while the true count did not.**

**The corrected census above counts line 85 as an entry and line 88 as part of
it**, which is why it also totals fourteen — for the right reason.

### The title, counted separately

**MEASURED: line 1 reads `# \`P2-PHASE-01\` microscopic parameter domain —
ADOPTED`.** §5's table does not list it and I have not added it: **a title is
not a kind label.** It is recorded here so the omission is deliberate rather
than missed, and it is CURRENT.

### Was any further STALE label found?

**No.** **The three surviving `RECOMMENDATION` labels were each read in place,
not classified from their line numbers:**

    136  advice on how to record the PI ruling — "Record it as included in the
         enumeration as a candidate, not as satisfying the gate's existential
         quantifier." Advice. Binds nobody. That it has since been followed
         does not make the label a false statement about state.
    257  "RECOMMENDATION, deliberately weaker than the previous version of
         this sentence" — an explicitly weakened reading of an observation,
         listing four ordinary explanations to exclude first. Binds nobody.
    362  "All three are cheap and all three are things this artifact assumes
         rather than knows" — C1, C2 and C3, none commissioned. Binds nobody.

**All three CURRENT. None touched.** **No `MEASURED`, `PI RULING`, `DERIVED` or
`CAUTION` label was touched, and the vocabulary definition at 25–28 is
unchanged.**

**One observation, reported and LEFT, per §2's "report it and leave it".**
**The repair introduces `ADOPTED` as a kind label at line 85, and the
vocabulary at lines 25–28 defines `MEASURED`, `PI RULING`, `DERIVED` and
`RECOMMENDATION` — four kinds, not including it.** §3 mandates the replacement
verbatim and §2 forbids editing the vocabulary, **so this is not a defect I was
free to repair, and I did not.** **It is a finding for whoever decides whether
the vocabulary should name the label the artifact now uses for its own operative
content** — and it is the kind of thing A5 exists to surface, arriving on the
same line the sweep was commissioned to fix.

## 6. A6 — Every pin checked against its target

**MEASURED at the head**, by enumerating every occurrence of
`` (sha256 `<64 hex>`) `` over the WHOLE file and resolving the artifact path
named immediately above each.

**AT-LEAST-ONE ASSERTION: 2 pins found, `>= 1` satisfied.** **A sweep that
found no pins and reported success would be the vacuous green this programme
has now met twice, and the assertion is coded rather than assumed.**

    pin 1   GATES.md line 1017
      path    derivations/P2-PHASE-01_microscopic_parameter_domain.md
      pinned  4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
      actual  4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
      MATCH

    pin 2   GATES.md line 1040
      path    derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
      pinned  e373efcb0d14db641604537c6a264e2c48536ab516162b7fef6a995cbd11d1cb
      actual  e373efcb0d14db641604537c6a264e2c48536ab516162b7fef6a995cbd11d1cb
      MATCH

    PINS FOUND: 2   (the specification predicts TWO; the measurement governs)
    all matching: yes

**Pin 2 was verified untouched by count as well as by value:** MEASURED, the
contract-draft digest occurs once in `GATES.md` before the substitution and once
after.

## 7. A7 — `GATES.md` changes in exactly one place, and the five invariants

**MEASURED. CONTEXT SETTING STATED:**

    git diff --unified=0    1 region
    git diff (--unified=3)  1 region

**One region, one digest string. Full diff at `--unified=0`:**

```diff
+++ b/GATES.md
@@ -1017 +1017 @@ not a gate ID. Adopted artifact:
-(sha256 `a481955be9bfa248b925ef7bf49f0f57cc462799ee72278507f71f99ac70cfc8`).
+(sha256 `4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214`).
```

**No heading, no path, no prerequisite state and no `Status:` line appears in
the diff. A7's stop is not triggered.**

**The five invariants, MEASURED at commit 4 against the evidence base:**

    1  '^## P2-' section count        base 14   head 14        UNCHANGED
    2  every '^Status:' line          15 lines, TEXTUALLY IDENTICAL
    3  P2-PHASE-01                    Status: PROPOSED
    4  MICROSCOPIC PARAMETER DOMAIN   Prerequisite state: **SATISFIED**
    5  PHASE INPUT / ADMISSIBILITY    **UNSATISFIED**

**All five hold.**

### `P7` returned `PASS` and it checked nothing

**MEASURED, from this task's own run:**

```json
{
  "gates_path": "GATES.md",
  "authorised_modified": ["P2-PHASE-01"],
  "section_count_base": 0,
  "section_count_head": 0,
  "unauthorised_changed": [],
  "added_sections": [],
  "removed_sections": []
}
```

**Zero sections at base and zero at head, against a file carrying fourteen
gates.** `GATE_HEADING` is `^## (P2-[A-Z0-9-]+)\s*$` and every real heading
continues past the ID. **P7 compared two empty maps.**

**This task modifies `GATES.md`, so the vacuous green is again exactly where it
is most dangerous.** **The edit's confinement is established by A7's
single-region diff and A6's pin table, both direct measurements of the file —
not by `P7`.**

## 8. A8 — Protected paths, and the commit order

**MEASURED at commit 4**, whole-tree `git ls-tree -r` blob comparison, path by
path:

    paths at base                    350
    paths at commit 4                352
    removed                          none
    added                              2   (this specification, this review)
    changed                            2
    identical                        348
    changed set == §6's modify: set  TRUE
    unexpected changes               none

    results/    base  69  head  69   differing: none
    scripts/    base  60  head  60   differing: none
    tests/      base  20  head  20   differing: none
    reports/    base  68  head  68   differing: none

    derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md   SAME
    derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md   SAME
    CONVENTIONS.md                                                  SAME
    DECISION_LOG.md                                                 SAME
    docs/BRANCHING_POLICY.md                                        SAME

**Both DRAFT files untouched, as §2 requires** — and the contract draft had to
stay untouched because its pin already matched and must still match, which A6
confirms it does.

**Commits, MEASURED, in the order §6 specifies:**

    commit 1  234c17a21324f1d3cb6fd888002177eb43224ac6  specs/2026-08-13T0034Z_adopt-domain-labels.md
    commit 2  641c5ec1374a83245631c3489af4e0b0520e7262  reviews/chatgpt/2026-08-13T0034Z_adopt-domain-labels.md
    commit 3  563f3f8344a1d15ec34e4f649ca8d12c8f2fe14e  derivations/P2-PHASE-01_microscopic_parameter_domain.md
    commit 4  7d5c665b7e87e050b9f1a0a135012403991da791  GATES.md
    commit 5  INTENDED                                  reports/2026-08-13T0034Z_adopt-domain-labels.md

**Commit 3 precedes commit 4 because the re-pin embeds commit 3's blob digest**,
and that digest was read from the blob.

**The UTC token `0034` and the day `13` were MEASURED** (`date -u`) when commit 1
was written, not chosen. **The day rolled over from 12 to 13 between the previous
task and this one**, so this task's paths carry `2026-08-13` while the artifact
it repairs is adopted by a `2026-08-12` specification. **That is the measured
clock and not a choice.**

**The final scope, INTENDED** — commit 5 does not exist while this is written:

    stated: 3 additions, 2 modifications
    base: cd1ebd84ca588a8ec946fc89e692f9e34760713d
    head: <commit 5, INTENDED>
    mode: exact
    add:
      reports/2026-08-13T0034Z_adopt-domain-labels.md
      reviews/chatgpt/2026-08-13T0034Z_adopt-domain-labels.md
      specs/2026-08-13T0034Z_adopt-domain-labels.md
    modify:
      GATES.md
      derivations/P2-PHASE-01_microscopic_parameter_domain.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Five paths. MEASURED at commit 4: two of the three additions are in place and
both modifications are; the third addition is this file.** **The scope measured
base-to-commit-5 is post-report evidence and is not claimed here.**

## 9. A9 — The two checker runs, and A10 — validators

Base `cd1ebd84…`, head **commit 4** `7d5c665b…`. **Both prospectivity readings
run.**

### RUN 1 — default subject selection, observational, governs nothing

```json
{
  "base": "cd1ebd84ca588a8ec946fc89e692f9e34760713d",
  "head": "7d5c665b7e87e050b9f1a0a135012403991da791",
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": ["P2-PHASE-01"],
  "register_path": "docs/BRANCHING_POLICY.md"
}
```

### RUN 2 — `specification_paths` naming only this specification

```json
{
  "base": "cd1ebd84ca588a8ec946fc89e692f9e34760713d",
  "head": "7d5c665b7e87e050b9f1a0a135012403991da791",
  "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
  "append_only_paths": ["DECISION_LOG.md"],
  "authorised_modified_gates": ["P2-PHASE-01"],
  "specification_paths": ["specs/2026-08-13T0034Z_adopt-domain-labels.md"],
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

**RUN 2's stop is not triggered.** Four commits in range, four in scope on both
readings.

**What RUN 2 excluded: NOTHING. MEASURED: RUN 1's and RUN 2's JSON are
byte-identical**, because the range adds exactly one specification and the
default selection already selects it. **I will not describe the narrowing as
having protected anything.**

**No config value was supplied by me.** `append_only_paths` is
`["DECISION_LOG.md"]`, never `[]`. **`P3` passed truthfully:** MEASURED
`base_bytes` 89541, `head_bytes` 89541, `base_is_byte_prefix_of_head` true,
`deleted_lines_base_to_head` 0.

**`P1` PASS, counted 5 against a stated 5** — three additions and two
modifications. **It reached that by reading the `stated:` line as prose**, since
this branch descends from `main` and not from the unlanded declared-total repair.

### A10 — Validators

**MEASURED**, the repository's own invocation, in a detached worktree at the
evidence base and then at commit 4:

    BEFORE  cd1ebd84   280 passed, 2 deselected   exit 0
    AFTER   commit 4   280 passed, 2 deselected   exit 0

**Identical, as expected: this task changes prose and one digest string. No test
changed behaviour.**

**And, stated plainly as A10 requires: the suite cannot distinguish a matching
pin from a stale one.** **MEASURED in the previous task at three revisions** —
280 passed with the contract pin stale, and 280 passed at commit 4 and commit 5
with it repaired. **This task adds a fourth revision to that record**: 280
passed at `cd1ebd84` where the domain pin matched, and 280 passed at commit 4
after both the artifact and its pin changed. **No count moved at any point.**
**A suite whose output is invariant across the property in question is not
testing that property.**

## 10. A11 — Commit-message hygiene

**MEASURED.** Proposed messages scanned before each commit; stored messages read
back after:

    234c17a2  spec: repair the adopted domain's operative status label, and sweep the rest
    641c5ec1  review: pre-execution review for the adopted-domain label repair
    563f3f83  derivations: label the adopted domain ADOPTED instead of a recommendation
    7d5c665b  gates: re-pin the adopted domain artifact to its operative bytes

    trailers on each of the four                        none
    'Co-Authored-By' in any stored message                0
    session identifier or URL in any stored message       0
    tool or model attribution in any stored message       0

**Case-insensitive scan over all four stored bodies: 0 matches.**

**Commit 5's INTENDED message**, first line:

    report: record the operative-label repair and the whole-file label census

## 11. §8 — Rule 16 assessment

**Rule 16 is operative. I confirm the specification's candidate junction and add
one the specification could not have named, because it arose during execution.**

### The junction: consistency by sequence is not consistency by construction

**After this task the adopted artifact is labelled consistently and both pins
match — MEASURED, §5 and §6.** **A reader may infer that the adoption line is
now self-consistent by construction. It is not.**

**It is self-consistent because four tasks in sequence each found and repaired
what the previous one left.** The record, MEASURED across this session:

    the adoption task        anchored the status line; left 3 neighbours
    the repair task          anchored those 3; left the operative label at 85
    this task                anchored line 85; swept the rest
    and at each of the last three, editing a pinned artifact staled its pin,
    which the specification had to carry because nothing detects it

**Three consecutive tasks needed a re-pin written into the specification by
hand.** **The only reason a fifth round is not needed is A5's census, and that
census was performed once, by a person, over one revision.**

**Neither the label consistency nor the pin correspondence is checked by
anything that runs.** **MEASURED, not argued: no test compares a `GATES.md` pin
to its target, and the suite reports 280 passed across four revisions spanning a
stale pin, a repaired pin, an edited artifact and a re-pinned one** (§9). **A
one-time human sweep is evidence about one repository state, not a continuing
invariant.** **The next task that edits a pinned artifact will go stale in the
same silence unless its own specification remembers.**

### The junction execution added: the census can be right and blind at once

**A5's arithmetic reconciled to fourteen while its pattern missed the one label
this task created and counted a quotation in its place** (§5). **Two errors that
cancel.**

**This is the same defect shape as the labels themselves, one level up.** The
label at line 85 asserted a state the document was no longer in; **the census
pattern asserts a coverage it no longer has.** **A reader who sees "fourteen,
matching the expected fourteen" has been given a number that agrees for reasons
that do not hold.** **What would fix it is a pattern derived from the artifact's
own vocabulary rather than hand-listed** — and the vocabulary now needs a fifth
kind, since the repair uses `ADOPTED` as a label and lines 25–28 define four
(§5). **That is a finding for the next specification and I did not act on it.**

### What this task does not establish

**Nothing about the science changed.** No prerequisite state, gate status or
verdict moved. `P2-PHASE-01` is `PROPOSED`, its ADMISSIBILITY CONTRACT
prerequisite is `UNSATISFIED`, and that block still reads *"No operational
stability or admissibility rule is presently frozen."* **The label now says the
domain binds; the reviewer's §5 caution is preserved in §4 above: it binds this
gate's governed enumeration and establishes no phase, no root completeness, no
full-space stability, no thermodynamic dominance and no finite-density
coverage.** **A tidier artifact is not a readier gate.**

## 12. Stops and clarifications

### `SPECIFICATION_DEFECT` — none

**No anchor failed, no count came out wrong, and no stop condition fired.** The
two §11 line-number slips are recorded as secondary findings, not stops: they
change no measurement.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — none

**The re-pin needed no new ruling.** §1 of the specification rests it on the PI
ruling already recorded in `specs/2026-08-12T2326Z_adopt-domain-repair.md` §1,
and the review's §2 agrees that applying that ruling to an artifact modified by
this task is an instance of it rather than a new governance decision. **I did not
have to supply that reading and did not.**

### `REPOSITORY_DEFECT` — two, both pre-existing and out of scope

**1. `P7` is vacuous against the real `GATES.md`.** §7. Known, not touched, and
**not offered as evidence for anything in this report.**

**2. No validator compares a `GATES.md` pin to its target, and none sweeps
label consistency.** §11. **MEASURED across four revisions.** A6 and A5
compensate for both, once each, by hand.

### `ENVIRONMENT` — none

**No environment failure occurred.** **`CONVENTIONS.md` Rule 13 carries two
conflicting diagnostic orders, a known open item; neither was exercised**, and I
am not naming one as having applied. Nothing was installed.

### `OBSERVATION_METHOD_ERROR` — one, from the previous task, and it is why this task exists

**In the previous task's report I classified the line-85 label CURRENT and gave
my reason: that it was "a label on the recommendation the PI has since ruled on
rather than a claim that the artifact awaits adoption."** **That was wrong**, and
the specification's §0 gives the reason it was wrong: **line 28 defines
`RECOMMENDATION` as binding nobody, so the label is a claim about state, and it
labels the operative content rather than framing it.**

**What worked is that I reported it with its line number instead of passing over
it.** §2 of the previous specification required exactly that — *"report it and
leave it"* — and reporting is what let the PI and Reviewer overrule my
classification. **Had I judged it current and stayed silent, there would have
been no fourth round.** **The lesson is not that the classification was a
judgement call; it is that a label defined in the same file as non-binding
cannot be read as structural description, and I should have checked the label
against its own definition, which was 57 lines above it.**

**A second method choice, recorded because it could have gone the other way.**
The re-pin's value was read from **commit 3's committed blob**
(`git show HEAD:<path> | sha256sum`), not from the working-tree file, as §4
requires. The two agreed; **the working-tree value would have been the
unverified one and is not what was used.**

**A third, recorded because it changed what I reported.** My first census run
used a pattern extended with `ADOPTED`, which gave 19 raw lines and disagreed
with §5's 17. **Re-running under the specification's own pattern gave 17 and
exposed why**: the extended pattern sees line 1 and line 85, the specification's
sees neither. **The disagreement was the finding, not an error to reconcile
away**, and §5 reports both patterns' counts rather than the flattering one.

### Secondary findings, kept separate

- **§11 places `## 3. The domain` at line 84; MEASURED, it is at line 83.**
  Off by one. §0's "immediately under" is correct and nothing turns on it.
- **The census pattern's coverage gap and the undefined `ADOPTED` kind.** §5,
  §11. Reported and left.
- **RUN 2's narrowing excluded nothing** — byte-identical to RUN 1. §9.
- **The two prospectivity readings differ in one field and no verdict.** §9.
- **`P1` passed by reading a structured `stated:` declaration as prose.** §9.
- **The validator counts are identical across four revisions spanning every
  state this line has been in.** §9, §11.

### Anything ambiguous, unsatisfiable, or that I would have specified differently

- **A5's pattern should be derived from lines 25–28, not hand-listed.** As
  written it cannot see a label the task itself introduces, and it counts
  quotations of labels as labels. **Both showed up on the first run.** A census
  that reads the artifact's own vocabulary and then greps for those words —
  plus whatever the artifact actually uses in bold at line start — would have
  flagged `ADOPTED` as an undefined kind instead of silently missing it.
- **A5 and A6 should be tests, not criteria.** They are the only two checks in
  this task that could have failed for a reason nobody anticipated, and both are
  performed by hand. **I said this of A6 last task and it remains true of both.**
  **Four rounds is enough evidence that "the next specification will remember"
  is not a mechanism.**
- **§3's replacement text introduces a label word the artifact does not
  define.** I would have added the fifth vocabulary entry in the same task,
  since the alternative is that the repair leaves a new inconsistency of exactly
  the kind it was written to remove — **smaller than the one it fixed, but the
  same shape.** §2 forbade it here and I obeyed.
- **A4 asked for the context setting to be stated, and that was the right
  lesson to carry forward** from the previous task's coalescing surprise. **Here
  both settings give one region**, so the question is moot — but the criterion is
  now written so that it could not have been reported misleadingly.

## 13. Confirmations the report contract asks for explicitly

- **Any further STALE label found? NO.** §5. The three surviving
  `RECOMMENDATION` labels were read in place and are CURRENT.
- **Anything the sweep turned up was left unrepaired.** The one observation —
  `ADOPTED` used as a kind the vocabulary does not define — **is reported and
  untouched**, per §2.
- **`P2-PHASE-01`'s `Status:` line reads `PROPOSED`**; MICROSCOPIC PARAMETER
  DOMAIN reads `SATISFIED`; PHASE INPUT / ADMISSIBILITY CONTRACT reads
  `UNSATISFIED`. All MEASURED at commit 4.
- **`C1`, `C2` and `C3` were not answered**, and no claim is made about the
  complement root's provenance, the global sign of `I0(Mhat)`, or the curvature
  asymmetry.
- **No enumeration was run and nothing was computed.**
- **No superseded-register entry was written.** MEASURED:
  `docs/BRANCHING_POLICY.md` is blob-identical.
- **`main` was not touched and no merge was performed.**
