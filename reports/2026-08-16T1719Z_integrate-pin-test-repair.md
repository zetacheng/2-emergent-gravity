# Report — integrate the pin-test newline repair, and land it

    branch      governance/integrate-pin-test-repair
    base        bfef924c368658cac85c04ed18d96eb4450afba6   (authoritative main)
    source      governance/repair-pin-test-newline @ 202914f57916b0379d8106cc168ec86bcc752fac
    measured at commit 3, 6aee68e21edff0a2b457eca886e0b329562f32cc   (the merge commit)

**One merge, no conflict. One line of test code lands. Nothing is
modified by this task.**

---

## 1. `A3` — environment conformance, before any measurement

**Run first, as `A3` requires, in Rule 13's diagnostic order extended by
Amendment D's step 0. Reported before any figure that depends on it.**

    (0) execution location    /home/user/2-emergent-gravity, HEAD bfef924c…
                              MEASURED: `git worktree list` shows this
                              session's checkout AND the source task's
                              worktree at 202914f5. THE CONTAINER IS THE
                              SAME ONE the source task ran in.
    (1) execution identity    root, uid 0
    (2) interpreter           Python 3.11.15 at /usr/local/bin/python
    (3) permissions           repository writable; no permission failure
    (4) filesystem/workspace  MEASURED: `git rev-parse --is-shallow-repository`
                              → false. No `.git/shallow`. 423 commits.
                              NOT SHALLOW.
    (5) package availability  MEASURED: pytest 9.1.1, numpy 2.4.6,
                              sympy 1.14.0, ruff 0.15.8 — all four declared
                              packages present and importable.

**NO RESTORATION WAS NEEDED IN THIS TASK, and none was performed.** The
container is conformant because the source task restored it — packages
installed and the shallow clone completed — and this task inherits that
state rather than repeating it. **No repository content was touched by
this criterion.**

**This is why `A3` exists**, and the source task is the reason: its first
suite invocation gave 5 failed, 319 passed, all five `git rev-parse …
Needed a single revision` on historical SHAs, none touching the pin test.
**A suite result taken before this check is uninterpretable**, and `A7`'s
figure below is reported only because this check ran first.

**Rule 13 carries two diagnostic orders, a known open item. NO
ENVIRONMENT FAILURE OCCURRED IN THIS TASK**, and **neither order was
exercised** — I am not naming one as having applied. The order above was
run as a CONFORMANCE CHECK because `A3` requires it, not in response to a
failure.

## 2. `A1` — repository and refs

**MEASURED, and reported VERBATIM. NOT normalised:**

    git remote get-url origin        https://github.com/zetacheng/2-emergent-gravity

**It carries NO `.git` suffix.** The specification's own pre-issue record
notes that the Researcher's clone reports the URL WITH the suffix, and
`§10` says both identify the same repository. **I did not add the suffix,
did not remove it anywhere, and did not treat the difference as a stop.**
**It identifies `zetacheng/2-emergent-gravity`**, which is the
confirmation `A1` asks for and the one that carries weight.

**Refs, MEASURED after fetching:**

    refs/remotes/origin/main                      bfef924c368658cac85c04ed18d96eb4450afba6
    refs/heads/main                               1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab
    governance/repair-pin-test-newline (remote)   202914f57916b0379d8106cc168ec86bcc752fac

**`refs/remotes/origin/main` is `bfef924c…`, as the evidence base
requires. No stop.**

**`refs/heads/main` lags, and `A1` says a lagging local ref is not a
stop.** Reported for contrast. Every measurement in this report reads the
remote-tracking ref or an explicit SHA, never the local `main` ref, and
the branch was cut from `bfef924c…` by SHA rather than by name.

**The source is `202914f5…`, as specified.**

**MEASURED: it is NOT an ancestor of `main`.**

    git merge-base --is-ancestor 202914f5… refs/remotes/origin/main
    exit status 1   →  NOT an ancestor

**That is the precondition for this task existing.** Had it been an
ancestor, the repair would already be on `main` and the merge would be a
no-op.

## 3. `A2` — the pre-execution review

**MEASURED.**

    field `Reviewed specification SHA-256:` PRESENT   yes, line 4
    value carried by the review                       77217bb55eb35ad3ac1069f866b002cbc0c69d852122be1495cd50053a7af74d
    SHA-256 of the committed specification bytes      77217bb55eb35ad3ac1069f866b002cbc0c69d852122be1495cd50053a7af74d
    MATCH                                             yes
    review verdict                                    APPROVE FOR EXECUTION
    committed unedited                                yes — byte-identical to the supplied review

**The field's presence was checked before its value was compared**, in
that order, as `A2` requires.

## 4. `A9` — which merge case, stated BEFORE the blob comparisons

**MEASURED, before the merge was made:**

    merge-base(origin/main, 202914f5…)                bfef924c368658cac85c04ed18d96eb4450afba6
    commits on main after the base                    0

**The merge-base IS the evidence base, and `main` carries no commit after
it. So no commit on `main` could have touched an arriving path**, and the
merge is one-sided.

**This ordering is load-bearing and is why `A9` demands it.** In a
two-sided merge, "all four arriving paths are blob-identical to the
source tip" would be equally consistent with the merge having discarded
`main`'s side. **One-sidedness is what makes the blob comparison mean
what it appears to mean**, and it is established first.

**NOW the comparisons, MEASURED at the merge commit against the source
tip `202914f5…`:**

    reports/2026-08-16T1450Z_repair-pin-test-newline.md            IDENTICAL
    reviews/chatgpt/2026-08-16T1450Z_repair-pin-test-newline.md    IDENTICAL
    specs/2026-08-16T1450Z_repair-pin-test-newline.md              IDENTICAL
    tests/test_gate_pins.py                                        IDENTICAL

**All four arriving paths blob-identical. Nothing arriving was altered in
transit.**

## 5. `A5` — no conflict

**MEASURED, `git diff --name-only --diff-filter=U` at the merge:**

    (empty)

    conflict entries    0

**The conflict list is EMPTY, and `git status --porcelain` reports no
unmerged entry.** The merge was clean, matching the Researcher's dry run.
**`§0` makes any conflict an immediate stop; none arose.**

## 6. `A4` — merge parentage, three separately derived measurements

**Each value derived by its own command, not read from the others:**

    merge commit                              6aee68e21edff0a2b457eca886e0b329562f32cc
    parent 1   git rev-parse HEAD^1           c12843fbc4b5b280ab661b4afcba3e7fc1aa3640
    parent 2   git rev-parse HEAD^2           202914f57916b0379d8106cc168ec86bcc752fac
    merge-base git merge-base HEAD^1 HEAD^2   bfef924c368658cac85c04ed18d96eb4450afba6

**Parent 1 IS this task's review commit, commit 2. Parent 2 IS the
specified source tip. The merge-base IS the evidence base.** All three as
specified.

**Commit 1 is an ancestor of parent 1, MEASURED:**

    git merge-base --is-ancestor 77966b298cf44400c6a0e9b5c48622110a385545 HEAD^1
    exit status 0   →  YES

**The checker's `P5` independently recomputed all three** and reports the
same values — see `§13`. **Its `does_not_establish` field notes that three
correct values are equally consistent with fresh recomputation and with
one field copied into another**, which is exactly why `A4` asks for them
separately derived and why I derived them that way.

## 7. `A6` — the diff at the merged head

**MEASURED, `git diff bfef924c… HEAD -- tests/test_gate_pins.py`, in
full:**

    diff --git a/tests/test_gate_pins.py b/tests/test_gate_pins.py
    index 32664ad..20dc56c 100644
    --- a/tests/test_gate_pins.py
    +++ b/tests/test_gate_pins.py
    @@ -178,7 +178,7 @@ def test_collect_pins_reports_no_path_when_none_is_named(tmp_path: Path) -> None
     def test_a_stale_pin_is_detected(tmp_path: Path) -> None:
         """The digest comparison itself, on a file whose bytes are known."""
         artifact = tmp_path / "artifact.md"
    -    artifact.write_text("content\n", encoding="utf-8")
    +    artifact.write_text("content\n", encoding="utf-8", newline="")
         measured = hashlib.sha256(artifact.read_bytes()).hexdigest()
         assert measured != _HEX_A
         assert hashlib.sha256(b"content\n").hexdigest() == measured

**MEASURED, numstat:**

    1 added   1 deleted   tests/test_gate_pins.py

**Exactly one line added and one deleted, and it is the write.**

**The assertions, `_HEX_A` and the fixture string are UNCHANGED,
confirmed by reading them at the merged head rather than by inspecting
the diff alone:**

    constant   —  tests/test_gate_pins.py:138    _HEX_A = "a" * 64
    fixture string                                "content\n"      (unchanged)
    first assertion                               assert measured != _HEX_A
    second assertion                              assert hashlib.sha256(b"content\n").hexdigest() == measured

**Both assertions and the constant appear in the diff as CONTEXT lines,
which is a second and independent way of seeing that they did not
change.**

## 8. `A7` — the suite at the merged head

**MEASURED, `python -m pytest` from the repository root, exit status 0:**

    324 passed, 2 deselected      in 44.07 s

**The expected figure.** The Researcher measured the same counts at the
merged head in the dry run.

**It is NOT 5 failed / 319 passed**, and `§1` is the reason: the
environment was checked for conformance before this run, the clone is not
shallow, and the historical objects the governance tests resolve by SHA
are present. **Had the count been 5/319, `A7` directs the reader back to
`A3`, and that pointer would have been correct.**

**The run time differs from the Researcher's 25.6 s. That is machine
speed, not a finding**, and the counts — which are what `A7` asks for —
agree exactly.

## 9. `A8` — scope, the two figures and the arriving arithmetic

**MEASURED at commit 3, the merge commit:**

    A   reports/2026-08-16T1450Z_repair-pin-test-newline.md
    A   reviews/chatgpt/2026-08-16T1450Z_repair-pin-test-newline.md
    A   reviews/chatgpt/2026-08-16T1719Z_integrate-pin-test-repair.md
    A   specs/2026-08-16T1450Z_repair-pin-test-newline.md
    A   specs/2026-08-16T1719Z_integrate-pin-test-repair.md
    M   tests/test_gate_pins.py

    5 additions, 1 modification     MEASURED AT COMMIT 3

**INTENDED, base to commit 4: 6 additions and 1 modification**, the sixth
addition being this report. **INTENDED and not MEASURED: this report is
written before the commit containing it.**

**Each figure is labelled with the head it was measured at**, as `A8`
requires: 5/1 at commit 3, 6/1 intended at commit 4.

**No status code other than `A` and `M` appears. None of the forbidden
operations — delete, rename, copy, type change, unmerged, unknown —
occurs.**

### 9.1 The arriving counts, stated separately

**MEASURED, `git diff --name-status bfef924c… 202914f5…`:**

    arriving PATHS           4
    arriving ADDITIONS       3
    arriving MODIFICATIONS   1

    THEY DO NOT COINCIDE.  Four paths, three additions.

**This is the case the distinction exists for.** `D-pre-A3`'s executor
observed that the guard should stay visible even when it does nothing,
and `D-pre-B0`'s integration reported it doing nothing — four paths, four
additions, coinciding. **Here it does work**: a task that reported "four
arriving additions" would have described the modification of
`tests/test_gate_pins.py` as an addition, and that modification is the
entire substance of what lands.

### 9.2 The arriving paths as measured, against the manifest

**The manifest cannot name the source's `{HHMM}Z` token. MEASURED, the
actual arriving paths carry `1450Z`:**

    manifest                                              measured
    …{HHMM}Z_repair-pin-test-newline.md  (reports)         reports/2026-08-16T1450Z_repair-pin-test-newline.md
    …{HHMM}Z_repair-pin-test-newline.md  (reviews/chatgpt) reviews/chatgpt/2026-08-16T1450Z_repair-pin-test-newline.md
    …{HHMM}Z_repair-pin-test-newline.md  (specs)           specs/2026-08-16T1450Z_repair-pin-test-newline.md
    tests/test_gate_pins.py                                tests/test_gate_pins.py

**CONFIRMED: they match the manifest in EVERY component but that token** —
directory, date, task slug and extension all agree, and
`tests/test_gate_pins.py` agrees exactly.

**This task's own three carry `1719Z`**, fixed once by commit 1 and reused
unchanged. **I chose no path.**

## 10. `A10` — protected paths

**MEASURED path by path over every path present at the evidence base:**

    paths at the evidence base      433
    compared                        433
    blob-identical                  432
    differing                         1   —  tests/test_gate_pins.py, and only it
    missing at head                   0

**The named paths, MEASURED individually — all IDENTICAL:**

    GATES.md                              IDENTICAL
    CONVENTIONS.md                        IDENTICAL
    docs/GOVERNANCE-DEBT.md               IDENTICAL
    docs/local/execution_environment.md   IDENTICAL
    scripts/                              60 paths,  0 changed
    derivations/                          45 paths,  0 changed
    results/                              69 paths,  0 changed

**`docs/local/execution_environment.md` is checked explicitly and is
unchanged**, and that matters here more than usual: **`§1` of the
specification is a finding ABOUT that file, and a task that reported the
finding while altering the file would have moved the evidence.** It did
not move.

**No register entry was added anywhere. No gate state, no artifact, and
no script was touched.**

## 11. `A11` — gate invariants and pins

**MEASURED at commit 3, all four:**

    ^## P2- count                        14
    P2-PHASE-01                          Status: PROPOSED      (GATES.md:973)
    first prerequisite                   Prerequisite state: SATISFIED   (GATES.md:1011)
    second prerequisite                  Prerequisite state: SATISFIED   (GATES.md:1036)
    pin at line 1017                     MATCH
    pin at line 1040                     MATCH

**The `Status:` line was located WITHIN the `P2-PHASE-01` section, not by
a first match.** The section heading is at `GATES.md:971` and its status
line at 973. **A bare `grep 'Status: PROPOSED' | head -1` returns line
209, which belongs to a DIFFERENT gate** and reads `Status: PROPOSED
(deferred — not computed this sweep)`. **Reported because a
first-match read would have produced the right word from the wrong
gate.**

**The pins were verified by RECOMPUTING the target digests, not by
reading the pin twice:**

    GATES.md:1017   4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
    sha256 derivations/P2-PHASE-01_microscopic_parameter_domain.md
                    4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214

    GATES.md:1040   e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
    sha256 derivations/P2-PHASE-01_input_admissibility_contract.md
                    e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3

**Both MATCH.** **This is the comparison the landing test exists to
protect**, and it is performed here independently of that test.

## 12. `A12` — superseded branches, before the advance

**MEASURED at commit 3. Six separate exit statuses, all 1 — none is an
ancestor of the head:**

    52f65117  exit 1        7146a093  exit 1
    ebd531ab  exit 1        10c260b9  exit 1
    40168469  exit 1        d64cd912  exit 1

**The checker's `P4` independently reports `is_ancestor_of_head: false`
and `object_present: true` for all six** — see `§13`. **`object_present`
is worth a line: it is true only because the clone is complete, and in
the source task's shallow container this check would have had nothing to
resolve.**

**The post-advance repetition is post-report evidence and is not claimed
here.**

## 13. `A13` — the checker, MEASURED at commit 3

    base   bfef924c368658cac85c04ed18d96eb4450afba6
    head   6aee68e21edff0a2b457eca886e0b329562f32cc   (commit 3, the merge commit)

    run 1 INCLUSIVE   exit 0   PASS   sha256 1602cbfe0cb74116e350392a78acd3ca9972c899042d26a1de71269acddb38b1
    run 1 EXCLUSIVE   exit 0   PASS   sha256 f0ebdb04cabff35a7ad1ad33fa226407b9494841c9c2cc0f4038f7d068f4856a
    run 2 INCLUSIVE   exit 0   PASS   sha256 b716c83f47482dc3fda664f189918e59c09fad44fc7d4623e1a4802ffdde2b9c
    run 2 EXCLUSIVE   exit 0   PASS   sha256 983799858dec71bb2f8020bdb1c7e847377ba1d6211f378804aa20effeb32dcf

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 PASS
    P6 PASS   P7 PASS   P8 PASS   P9 PASS

**NINE OF NINE IN EVERY INVOCATION.** **No property is
`NOT_APPLICABLE` in this range** — unlike the source task, where `P5` and
`P9` both were. **The merge supplies `P5` a subject and the arriving
report supplies `P9` one.**

    commits_in_range                 7
    commits_on_first_parent_line     3

### 13.1 What `RUN 1` did — two specifications, and no `C3` conflict

**MEASURED: `RUN 1`'s default subject selection found BOTH specifications
in range** and evaluated `P1` against each:

    specs/2026-08-16T1450Z_repair-pin-test-newline.md     stated 3 add / 1 mod   counted 3 / 1   parse OK
    specs/2026-08-16T1719Z_integrate-pin-test-repair.md   stated 6 add / 1 mod   counted 6 / 1   parse OK

**Both PASS.** **`RUN 2` names only this task's specification and
evaluated `P1` against that one alone**, which is why `RUN 1` and `RUN 2`
produce DIFFERENT bytes here — unlike the two preceding tasks, where a
single-specification range made them identical.

**The `C3` multi-specification residual did NOT arise, and this is the
case that discriminates the diagnosis.** `_declarations_from_specs`
raises `InputError` when two subject specifications in range declare
DIFFERENT values for the same key. **MEASURED: `P3` reports
`specification_paths_read` as BOTH specifications and resolves to a
single declared set, `['DECISION_LOG.md']`, with `declared_source:
specification`.** `P7` likewise reads both and resolves `authorised_gates`
to `[]`.

**So two specifications were in range and agreed, and the tool passed.**
**That is the second half of the diagnosis established in the `D-pre-B0`
line — the trigger is a DIFFERENCE between declarations, not their
number — and this task exercises it directly** rather than by the absence
of a second specification. **The residual is unchanged and remains
unregistered.**

### 13.2 `P5`, and what it does and does not establish

    P5   PASS
    recomputed_merge_base    bfef924c368658cac85c04ed18d96eb4450afba6
    recomputed_parent_1      c12843fbc4b5b280ab661b4afcba3e7fc1aa3640
    recomputed_parent_2      202914f57916b0379d8106cc168ec86bcc752fac
    merge_base_equals_parent_1   false
    compared_to_recorded     UNAVAILABLE

**`compared_to_recorded: UNAVAILABLE` means the merge commit records no
parentage values in its message for the tool to compare against.** **So
`P5` verified that the parentage is internally coherent, not that it
matches anything I wrote down.** `§6`'s three separately derived values
are the independent measurement, and `P5` agrees with all three.

**`merge_base_equals_parent_1: false` is expected**: parent 1 is this
task's review commit, which is two commits after the base.

### 13.3 `declared_source`, `P3`, `P7` and `P9`

    P3   PASS   declared_source: specification   declared: ['DECISION_LOG.md']
    P7   PASS   declared_source: specification   section_count_head 14
    P9   PASS   reports/2026-08-16T1450Z_repair-pin-test-newline.md   heading_present: true

**`P7` reports FOURTEEN sections at both base and head. `PASS` at zero
would have been a STOP, and it is not zero.**

**MEASURED: `DECLARATION_CONFLICT` appears ZERO times in all four
outputs.**

**`DECISION_LOG.md` is not modified by this range**, so `P3` passed
without exercising the append property; the checker still reports
`base_is_byte_prefix_of_head: true` over 89541 identical bytes.

**`P9` found the arriving report and confirmed its `Stops and
clarifications` heading.** In the source task's own range `P9` was
`NOT_APPLICABLE`, because the report did not yet exist at the head being
checked. **The property is only exercised now, at integration** — which
is worth noting, since it means a report's Stops section is first
mechanically checked one task after it is written.

### 13.4 `RUN 1` config, verbatim — observational, governs nothing

    {
      "base": "bfef924c368658cac85c04ed18d96eb4450afba6",
      "head": "6aee68e21edff0a2b457eca886e0b329562f32cc",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 13.5 `RUN 2` config, verbatim — stop-governing

    {
      "base": "bfef924c368658cac85c04ed18d96eb4450afba6",
      "head": "6aee68e21edff0a2b457eca886e0b329562f32cc",
      "specification_paths": ["specs/2026-08-16T1719Z_integrate-pin-test-repair.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

**No value in either config is one I chose**, and **neither the config nor
this specification's declarations were adjusted to make `RUN 2` pass** —
`§8` forbids both, and neither was touched. **`RUN 2` passed on its first
invocation at both readings.**

### 13.6 `RUN 1` output, verbatim, `INCLUSIVE` reading

    {
      "base": "bfef924c368658cac85c04ed18d96eb4450afba6",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "6aee68e21edff0a2b457eca886e0b329562f32cc",
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
              "counted_add": 3,
              "counted_modify": 1,
              "counted_set": [
                "reports/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md",
                "specs/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md",
                "tests/test_gate_pins.py"
              ],
              "parse": "OK",
              "path": "specs/2026-08-16T1450Z_repair-pin-test-newline.md",
              "stated": 4,
              "stated_add": 3,
              "stated_modify": 1,
              "stated_record": "stated: 3 additions, 1 modification"
            },
            {
              "append_only": [
                "DECISION_LOG.md"
              ],
              "authorised_gates": [],
              "counted": 7,
              "counted_add": 6,
              "counted_modify": 1,
              "counted_set": [
                "reports/2026-08-XXT{HHMM}Z_integrate-pin-test-repair.md",
                "reports/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-pin-test-repair.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-pin-test-repair.md",
                "specs/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md",
                "tests/test_gate_pins.py"
              ],
              "parse": "OK",
              "path": "specs/2026-08-16T1719Z_integrate-pin-test-repair.md",
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
                "commit": "77966b298cf44400c6a0e9b5c48622110a385545",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "c12843fbc4b5b280ab661b4afcba3e7fc1aa3640",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "6aee68e21edff0a2b457eca886e0b329562f32cc",
                "work_paths": [
                  "tests/test_gate_pins.py"
                ]
              }
            ],
            "first_review_commit": "c12843fbc4b5b280ab661b4afcba3e7fc1aa3640",
            "first_work_commit": "6aee68e21edff0a2b457eca886e0b329562f32cc",
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
              "specs/2026-08-16T1450Z_repair-pin-test-newline.md",
              "specs/2026-08-16T1719Z_integrate-pin-test-repair.md"
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
              "merge": "6aee68e21edff0a2b457eca886e0b329562f32cc",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "bfef924c368658cac85c04ed18d96eb4450afba6",
              "recomputed_parent_1": "c12843fbc4b5b280ab661b4afcba3e7fc1aa3640",
              "recomputed_parent_2": "202914f57916b0379d8106cc168ec86bcc752fac",
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
              "commit": "77966b298cf44400c6a0e9b5c48622110a385545",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "c12843fbc4b5b280ab661b4afcba3e7fc1aa3640",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "4fb1a4ff7f31fee449cda2b8109994ccfde97789",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "5a7a90911a16e59cb9db4fdcf32ff53cbaad7e89",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "3461484f60e5725c96d7bd06a962d9e1c70b00c2",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "202914f57916b0379d8106cc168ec86bcc752fac",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "6aee68e21edff0a2b457eca886e0b329562f32cc",
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
              "specs/2026-08-16T1450Z_repair-pin-test-newline.md",
              "specs/2026-08-16T1719Z_integrate-pin-test-repair.md"
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
            "first_commit": "77966b298cf44400c6a0e9b5c48622110a385545",
            "first_commit_paths": [
              "specs/2026-08-16T1719Z_integrate-pin-test-repair.md"
            ],
            "reports_added": [
              "reports/2026-08-16T1450Z_repair-pin-test-newline.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-16T1719Z_integrate-pin-test-repair.md",
              "reviews/chatgpt/2026-08-16T1450Z_repair-pin-test-newline.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-16T1719Z_integrate-pin-test-repair.md",
              "specs/2026-08-16T1450Z_repair-pin-test-newline.md"
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
              "path": "reports/2026-08-16T1450Z_repair-pin-test-newline.md",
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

### 13.7 `RUN 2` output, verbatim, `INCLUSIVE` reading

    {
      "base": "bfef924c368658cac85c04ed18d96eb4450afba6",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "6aee68e21edff0a2b457eca886e0b329562f32cc",
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
              "counted_add": 6,
              "counted_modify": 1,
              "counted_set": [
                "reports/2026-08-XXT{HHMM}Z_integrate-pin-test-repair.md",
                "reports/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-pin-test-repair.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-pin-test-repair.md",
                "specs/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md",
                "tests/test_gate_pins.py"
              ],
              "parse": "OK",
              "path": "specs/2026-08-16T1719Z_integrate-pin-test-repair.md",
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
                "commit": "77966b298cf44400c6a0e9b5c48622110a385545",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "c12843fbc4b5b280ab661b4afcba3e7fc1aa3640",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "6aee68e21edff0a2b457eca886e0b329562f32cc",
                "work_paths": [
                  "tests/test_gate_pins.py"
                ]
              }
            ],
            "first_review_commit": "c12843fbc4b5b280ab661b4afcba3e7fc1aa3640",
            "first_work_commit": "6aee68e21edff0a2b457eca886e0b329562f32cc",
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
              "specs/2026-08-16T1719Z_integrate-pin-test-repair.md"
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
              "merge": "6aee68e21edff0a2b457eca886e0b329562f32cc",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "bfef924c368658cac85c04ed18d96eb4450afba6",
              "recomputed_parent_1": "c12843fbc4b5b280ab661b4afcba3e7fc1aa3640",
              "recomputed_parent_2": "202914f57916b0379d8106cc168ec86bcc752fac",
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
              "commit": "77966b298cf44400c6a0e9b5c48622110a385545",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "c12843fbc4b5b280ab661b4afcba3e7fc1aa3640",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "4fb1a4ff7f31fee449cda2b8109994ccfde97789",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "5a7a90911a16e59cb9db4fdcf32ff53cbaad7e89",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "3461484f60e5725c96d7bd06a962d9e1c70b00c2",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "202914f57916b0379d8106cc168ec86bcc752fac",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "6aee68e21edff0a2b457eca886e0b329562f32cc",
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
              "specs/2026-08-16T1719Z_integrate-pin-test-repair.md"
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
            "first_commit": "77966b298cf44400c6a0e9b5c48622110a385545",
            "first_commit_paths": [
              "specs/2026-08-16T1719Z_integrate-pin-test-repair.md"
            ],
            "reports_added": [
              "reports/2026-08-16T1450Z_repair-pin-test-newline.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-16T1719Z_integrate-pin-test-repair.md",
              "reviews/chatgpt/2026-08-16T1450Z_repair-pin-test-newline.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-16T1719Z_integrate-pin-test-repair.md",
              "specs/2026-08-16T1450Z_repair-pin-test-newline.md"
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
              "path": "reports/2026-08-16T1450Z_repair-pin-test-newline.md",
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

### 13.8 The `EXCLUSIVE` readings

**MEASURED by `diff`, and this is the whole of the difference:**

    run 1   line 314 of 318:   "inclusivity": "INCLUSIVE"  →  "EXCLUSIVE"
    run 2   line 291 of 295:   "inclusivity": "INCLUSIVE"  →  "EXCLUSIVE"

**One line each, and nothing else.** No property status, evidence field or
scope figure differs between the readings, and
`commits_out_of_scope` is empty in all four.

## 14. `A14` — commit-message hygiene

**MEASURED on commits 1–3. Commit 4 is post-report evidence.**

    commit 1   77966b29   spec: integrate the pin-test newline repair, and land it
               trailer hits 0      not amended
    commit 2   c12843fb   review: pre-execution review for the pin-test repair integration
               trailer hits 0      not amended
    commit 3   6aee68e2   merge: integrate the pin-test newline repair
               trailer hits 0      not amended

**MEASURED over the whole range, including the arriving commits: a scan
for `Co-Authored-By`, `claude.ai/code`, `Generated with`,
`Claude-Session` and `noreply@anthropic` returns ZERO.** **`P6`
independently reports `matches: []` for every commit in range.**

**Rule 20 binds this task and was NOT exercised.** **No force-push, no
branch deletion, no history rewrite of any kind.**

**Commits, MEASURED:**

    commit 1   77966b298cf44400c6a0e9b5c48622110a385545   specs/2026-08-16T1719Z_integrate-pin-test-repair.md
    commit 2   c12843fbc4b5b280ab661b4afcba3e7fc1aa3640   reviews/chatgpt/2026-08-16T1719Z_integrate-pin-test-repair.md
    commit 3   6aee68e21edff0a2b457eca886e0b329562f32cc   --no-ff merge of 202914f5…

**Commit 4's message, INTENDED:**

    report: the pin-test newline repair lands on main

## 15. `§7` — Rule 16 assessment

**Rule 16 is operative. All four junctions are addressed.**

### 15.1 First junction — one known blocker closes, and that is all

**This closes ONE KNOWN BLOCKER to `D-1`.** `D-1` has stopped four times:
a scholarly-egress precondition, a lagging local ref, the wrong
repository, and this test. **The test is the one this task removes.**

**Is any other KNOWN blocker outstanding? YES, and naming it is the
point.** **`D-1`'s most recent execution stopped on the `§1` network
precondition** — no scholarly or bibliographic host is reachable from
this container by any fetch path, across two independent clients and
twelve hosts, with a non-scholarly control blocked identically and the
proxy reporting a policy denial. **That blocker is untouched by this
repair and is not addressed anywhere in this task.**

**So the honest statement is: one known blocker closes, and at least one
known blocker remains, and it is the egress precondition.**

**I do not write that `D-1` will now complete** — the egress blocker
alone refutes that. **I do not write that `D-1` is "still blocked"
because unknown obstacles might exist** — that inference does not hold,
and the specification is right to have retracted an earlier draft that
made it. **The two statements have different grounds**: the egress
blocker is reported because it was MEASURED, not because no proof of its
absence exists.

**And `D-1`'s literature question remains unanswered.** That is a fact
about what has been done, not about what stands in the way. **Nothing in
this repair bears on it.**

### 15.2 Second junction — the instance closes, the class stays open

**MEASURED at the merged head: `tests/` contains eighteen `write_text`
calls; SEVENTEEN carry no `newline=` argument**, including a second call
in the repaired file at line 143.

**The instance is closed. The defect class is OPEN.**

**None of the seventeen fails today** — they do not compare written bytes
against a hard-coded byte literal — **and nothing in the repository
prevents the next author writing the same defect.** No `conftest.py`, no
helper, no lint rule was added, here or in the source task.

**A reader who takes "the pin test was repaired" to mean the suite is
platform-independent would be wrong**, and the second call in the very
same file is the sharpest reason.

### 15.3 Third junction — the declared environment is Windows

**MEASURED: `docs/local/execution_environment.md` declares a Windows
execution environment** — identity `zeta-3070\codexsandboxoffline`, a
Windows interpreter path, and `C:\p2-validator\venv`.

**So the platform on which this test failed is the DECLARED one, and
every Linux environment in which this suite's results have been produced
is undeclared.** **This is not a Linux check misreporting on Windows. It
is a check written on an undeclared platform, failing on the declared
one.**

**That STRENGTHENS the repository-defect classification rather than
weakening it.** A validator that fails under the repository's own
declared environment, while passing everywhere its results have actually
been produced, is a repository defect on any reading.

**And the reason it survived: NOTHING IN THE REPOSITORY COMPARES THE
DECLARED ENVIRONMENT TO THE ONE IN USE.** Rule 13 says the environment
SHALL satisfy the declaration and gives a diagnostic order for failures;
**no check, no test and no checker property evaluates the declaration
against the running system.** The divergence was invisible while it was
uniform.

**Reported. NOT registered** — `§4` forbids adding a register entry and
the governance debt register is frozen at eleven.

### 15.4 Fourth junction — a suite result before Rule 13 is uninterpretable

**The source task's container was NOT conformant**, and Rule 13's order
with Amendment D's step 0 is what caught it: only that task's worktree
present, a SHALLOW clone at 142 commits, and pytest, numpy and sympy
ABSENT.

**Its first suite invocation gave 5 failed, 319 passed, 2 deselected —
all five `git rev-parse … Needed a single revision`, none touching the
pin test.** **Taken at face value, that report would have sent the
programme after a repository defect that does not exist.**

**A SUITE RESULT IS UNINTERPRETABLE BEFORE RULE 13'S DIAGNOSTIC ORDER HAS
BEEN RUN**, and this task ran it — `§1` — before any figure that depends
on it. **`A7`'s 324 passed, 2 deselected is reported as meaningful only
because `§1` precedes it.**

**Two restorations were made in the source task under Rule 13's standing
authorisation** — packages installed, `git fetch --unshallow` taking 142
to 423 commits — **and no repository content was touched to make the
environment work.** **This task inherited the restored container and
performed no restoration of its own.**

**And the source executor's own `OBSERVATION_METHOD_ERROR`, carried
here:** its first instinct on the missing interpreter package was to
reach for a working interpreter rather than to diagnose. **That is how an
environment defect gets absorbed instead of found** — and had it been
absorbed, the shallow clone at step 4 would never have surfaced, leaving
five failures with no explanation.

## 16. Did integrating a one-line repair make me want to fix the other seventeen, or add a helper?

**Yes, and the shape of the pull was different from the source task's,
which is the part worth recording.**

**The source task named the helper its strongest temptation** and
declined it. **Integrating changed the calculus in a way that made the
pull WORSE, not better, and I want to be precise about why.**

**Seeing the merge land four paths for one line of substance makes the
overhead visible.** Three provenance artifacts, a review, a report, a
merge commit, four checker invocations and a full suite run — for one
keyword argument. **The thought that follows immediately is: the marginal
cost of seventeen more edits inside this same ceremony is essentially
zero.** That is arithmetically true and it is the wrong argument. **The
ceremony is not overhead being amortised; it is the review attaching to a
specific, evidenced change.** Seventeen unevidenced edits smuggled in
under one review would have exactly as much provenance as the ceremony
suggests and none of the scrutiny.

**The helper pull returned too, sharpened by `§15.3`.** Knowing the
declared environment is Windows makes the seventeen look less like a
latent hazard and more like seventeen live ones — **nobody has run this
suite in the declared environment, so "none fails today" is a claim about
Linux.** That is a genuine observation and it is an argument for a
specification, not for an edit. **I did not make the edit and I did not
write that specification.**

**One further temptation, and it is the one I would flag as most
specific to an integration task: to widen `§15.1`'s first junction into
an assessment of what `D-1` needs.** Having measured the egress blocker
myself in the preceding task, I could have written a route. **`§4`
forbids claiming anything about `D-1`'s completion, and a route is a
stronger claim than either forbidden sentence.** Not written.

**I confirm: I modified no file; repaired none of the seventeen call
sites; added no `conftest.py`, helper, or lint rule; added no register
entry; pushed no session branch and did not move or fast-forward one;
did not normalise the `origin` URL; did not delete or move the source
branch; wrote no next specification; and made exactly one merge, with no
rebase, no squash and no fast-forward at the integration.**

## 17. Stops and clarifications

**NO STOP occurred.** The merge was clean, all four checker invocations
exited 0, `RUN 2` passed at both prospectivity readings, the conflict
list was empty, and no acceptance criterion failed.

    SPECIFICATION_DEFECT                          0 stops, 0 findings
    ENVIRONMENT                                   0 stops, 1 finding
    OBSERVATION_METHOD_ERROR                      0 stops, 1 finding
    REPOSITORY_DEFECT                             0 stops, 1 finding
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 2 findings

### 17.1 `REPOSITORY_DEFECT` — the one this integration lands the repair for

**The pin-test platform assumption, repaired at one call site and landed
here.** **The class remains open at seventeen sites**, `§15.2`. **Nothing
in this task enlarged, reinterpreted or reduced the repair**: the diff at
the merged head is byte-for-byte the source's diff, and all four arriving
paths are blob-identical.

### 17.2 `ENVIRONMENT` — one finding, carried and not registered

**The declared execution environment is Windows and every result this
suite has produced comes from undeclared Linux environments**, `§15.3`.
**Nothing in the repository compares the two.**

**Carried from the source task, verified here** — `docs/local/execution_environment.md`
was read at the merged head and is blob-identical to the base, `§10`.
**Reported, NOT registered.**

**No environment failure occurred in THIS task, and neither of Rule 13's
two diagnostic orders was exercised.** The order was run as `A3`'s
conformance check, not in response to a failure. **Nothing was installed
by this task.**

### 17.3 `OBSERVATION_METHOD_ERROR` — one finding, carried from the source

**The source executor's first instinct on a missing interpreter package
was to reach for a working interpreter rather than to diagnose**,
`§15.4`. **Carried here because `§3` requires it and because the near-miss
is the informative part**: the workaround would have produced a green
suite and left the shallow clone — and therefore the five unexplained
failures — undiagnosed.

**No new observation-method error of my own arose in this task.** The one
place it could have — `A11`'s `Status: PROPOSED` — was caught: **a
first-match grep returns line 209, a different gate**, and I scoped the
read to the `P2-PHASE-01` section instead, `§11`. **Recorded there rather
than counted as a second finding, because it was caught before it entered
a measurement.**

### 17.4 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — first finding

**The `origin` URL differs between clones**: the Researcher measures it
WITH a `.git` suffix, this container WITHOUT one, `§2`. **Both identify
`zetacheng/2-emergent-gravity`.**

**`A1` here resolves what the source task carried as an open question** —
it requires the URL reported verbatim and NOT normalised, which is what I
did. **The residual ambiguity is narrower than before: it is now clear
what to report, and still unstated what a mismatch would mean if one ever
mattered.**

**Reported, NOT registered.**

### 17.5 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — second finding

**The Windows effect of the repaired line remains `DERIVED` and has never
been MEASURED by anyone in this line.** The source task could not
reproduce the failure locally and said so; **this task cannot either, and
the landing does not change that.**

**What IS established: a remote executor reported a Windows failure whose
"expected" and "measured" digests match `434728a4…` and `fc06f482…` to
the digit, and `newline=""` is documented to disable the translation that
produces the second.** **What is NOT established: that the reported
failure had this cause and no other.** **The arithmetic is consistent
with the report, which is weaker than confirming it.**

**A Windows run after this landing is the observation that would close
it. Nobody in this task performed one**, and the repair is now on `main`
without it. **That is the correct disposition on the evidence and it is
not a verification.**

**Reported, NOT registered.**

### 17.6 `SPECIFICATION_DEFECT` — nothing to report

**Nothing in this specification was found false about the repository or
about its own bytes.** Its pre-issue record was checked at seven points —
the base, the source tip and its non-ancestry, the merge cleanliness and
merge-base, the 5/1 figure at the merge commit, the one-line diff and its
numstat, `_HEX_A`, the declared execution environment, and the eighteen
`write_text` calls — **and MEASURED agrees with it at every one.** **The
suite figure it predicted at the merged head, 324 passed and 2 deselected,
is what the suite returns.**

**Nothing in the specification was unsatisfiable.**

### 17.7 What I would have specified differently

**`A11` names four invariants and does not say how to locate the
`Status:` line.** A first-match read returns the right word from the
wrong gate, `§11`. **I would have had `A11` require the status line
located WITHIN the `P2-PHASE-01` section, by its heading**, so that a
correct-looking answer cannot come from line 209.

**And `A13` says "`RUN 1` has two specifications in range; report what it
actually did" — which is right, and it stops one step short.** The
interesting fact is not that `RUN 1` read two, but that reading two
without conflict is the measurement that DISCRIMINATES the `C3`
diagnosis, `§13.1`. **I would have had `A13` require that stated: two
specifications in range, agreeing, and therefore no conflict — because
the trigger is a difference and not a count.** Reporting only "it read
two" would leave the residual's diagnosis exactly as speculative as it
was.

## 18. Evidence layering

**Committed in this report, MEASURED at commit 3:** `A1`–`A7` and
`A9`–`A12`, and `A14` for commits 1–3; `A8`'s scope base-to-commit-3 at 5
additions and 1 modification, and the arriving counts; `A13`'s four
invocations with both configs and both runs' output verbatim; commits 1–3
SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; `A8`'s final
base-to-commit-4 scope of 6 additions and 1 modification.

**Labelled `DERIVED` and not measured anywhere:** the behaviour of the
repaired line on Windows, `§17.5`.

**Post-report evidence, returned to the Reviewer and NOT written back:**
`A8`'s final scope measured base-to-commit-4; `A13-final`, being `RUN 2`
re-run at commit 4 BEFORE the landing; `A7` and `A11` re-run after the
advance; `A12`'s six exit statuses after the advance; `A14` for commit 4;
the pre-advance `--is-ancestor` exit status; the exact push command;
remote `main` read back; the source tip unchanged; confirmation that no
session branch was pushed; final ancestry confirmation.

**Nothing in this report claims to measure commit 4.**
