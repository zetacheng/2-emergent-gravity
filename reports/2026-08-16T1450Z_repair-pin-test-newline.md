# Report — repair the pin validator's undeclared platform assumption

    branch      governance/repair-pin-test-newline
    base        bfef924c368658cac85c04ed18d96eb4450afba6   (authoritative main)
    measured at commit 3, 3461484f60e5725c96d7bd06a962d9e1c70b00c2
    main        NOT TOUCHED. No merge. Integration is a separate task.

**One line of test code changed. No production code, no checker property, no
gate, no artifact.**

---

## 1. `A1` — repository and refs

**MEASURED:**

    git remote get-url origin        https://github.com/zetacheng/2-emergent-gravity
    refs/remotes/origin/main         bfef924c368658cac85c04ed18d96eb4450afba6
    refs/heads/main                  1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**`refs/remotes/origin/main` is `bfef924c…`, as the evidence base requires.
No stop.** The fetch was performed before the ref was read.

**`refs/heads/main` lags, and `A1` says a lagging local ref is not a stop.**
It is reported for contrast. **Note that it lags at a DIFFERENT value from
the one the preceding task's container carried** — see `§12.2`; the
container was recreated between the two tasks, and the local ref is an
artefact of how each clone was made, not of any programme action.

**One discrepancy, reported and NOT a stop.** `A1` says to confirm the URL is
`https://github.com/zetacheng/2-emergent-gravity.git`. **MEASURED, it has no
`.git` suffix.** The two forms designate the same repository and git accepts
both; **and `A1`'s stop condition is scoped by its own words to the
authoritative REF, not to the URL string** — *"Any mismatch of the
authoritative ref → STOP"*. **I did not treat a suffix difference as a stop,
and I did not silently normalise it either.** `§12.4` carries it as a
finding.

## 2. `A2` — the pre-execution review

**MEASURED.**

    field `Reviewed specification SHA-256:` PRESENT   yes, line 4
    value carried by the review                       242f2339dd8c055a4f821b28ff08c6463bfdf3c49327647982c7182508847c31
    SHA-256 of the committed specification bytes      242f2339dd8c055a4f821b28ff08c6463bfdf3c49327647982c7182508847c31
    MATCH                                             yes
    review verdict                                    APPROVE FOR EXECUTION
    committed unedited                                yes — byte-identical to the supplied review

**The field's presence was checked before its value was compared**, in that
order, as `A2` requires.

## 3. `A3` — the defect, before the change

**MEASURED, on this platform:**

    sha256(b"content\n")     434728a410a78f56fc1b5899c3593436e61ab0c731e9072d95e96db290205e53
    sha256(b"content\r\n")   fc06f48221d98ad6106c3845b33a2a41152482ab9e697f736ad26db4853fa657

**Both match the specification's figures to the digit.**

**`_HEX_A` READ, not inferred — imported from the module and printed:**

    _HEX_A                   aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    _HEX_A == "a" * 64       True,  length 64
    LF digest == _HEX_A      False
    CRLF digest == _HEX_A    False

**So the first assertion, `measured != _HEX_A`, passes on every platform and
is not the failure site.** **The specification's retraction of the earlier
`_HEX_A` collision claim is correct, and I verified it by reading the
constant rather than by trusting the retraction.**

**The source, MEASURED at the evidence base:** `test_a_stale_pin_is_detected`
begins at line 178 and the write is line 181, exactly as `§0` and the
pre-issue record state.

**My platform, MEASURED:**

    platform      Linux-6.18.5-fc-v20-x86_64-with-glibc2.39
    system        Linux
    os.linesep    '\n'
    Python        3.11.15

**MEASURED: the test PASSES here before the change.**

    tests/test_gate_pins.py::test_a_stale_pin_is_detected    1 passed

**I CANNOT REPRODUCE THE WINDOWS FAILURE LOCALLY, and I did not observe
it.** On a POSIX platform text mode performs no translation, so the written
bytes are already `b"content\n"` and both assertions hold. **The repair is
made on the evidence of the reported Windows failure and this
specification's arithmetic — not on a failure I watched.** Stating otherwise
would be the `MEASURED`-label failure this specification's own record
retracts.

**And there is a sharper way to put the platform question — see `§12.3`.**
**MEASURED: `docs/local/execution_environment.md` declares the execution
environment to be WINDOWS.** So the failing platform is the DECLARED one,
and this Linux container is the environment that does not satisfy the
declaration. **That inverts the usual reading of "it only fails on
Windows".**

## 4. `A4` — the diff

**MEASURED, `git diff tests/test_gate_pins.py`, in full:**

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

**MEASURED, `git diff --numstat`:**

    1 added   1 deleted   tests/test_gate_pins.py

**Exactly one line changes, and it is the write.** **The assertions, `_HEX_A`
and the fixture string are untouched** — they are visible unchanged in the
context lines above, which is why the diff is reported with context rather
than as two bare lines.

**MEASURED, `git status --porcelain` at that point: one entry,
`M tests/test_gate_pins.py`. No other file in the working tree changed.**

## 5. `A5` — the test after the change

**MEASURED:**

    node id     tests/test_gate_pins.py::test_a_stale_pin_is_detected
    result      1 passed

**And the fixture bytes verified directly, MEASURED on this platform:**

    Path.write_text("content\n", encoding="utf-8", newline="")
    read_bytes()   b'content\n'
    sha256         434728a410a78f56fc1b5899c3593436e61ab0c731e9072d95e96db290205e53
    equals the LF digest    True

**DERIVED, NOT MEASURED — what the change does on Windows.** `newline=""`
is documented to disable newline translation on write: with it, no `"\n"`
in the string is translated, so the bytes committed to disk are exactly the
encoded string. **On Windows the fixture therefore becomes `b"content\n"`
instead of `b"content\r\n"`, its digest becomes `434728a4…`, and the second
assertion — which compares against `sha256(b"content\n")` — holds.**

**This is a derivation from documented behaviour and from the two digests in
`§3`. I have no Windows machine and did not run one.** **Labelled `DERIVED`
here and everywhere it appears.**

## 6. `A6` — validators, before and after

**MEASURED, `python -m pytest` from the repository root, exit status 0:**

    BEFORE the change (commit 2)   324 passed, 2 deselected
    AFTER  the change (commit 3)   324 passed, 2 deselected

**Unchanged, as `A6` expects.** The test passed on this platform before and
passes after; **the repair is invisible to a Linux run by construction, which
is the whole shape of the defect.**

**A6 says a change in the counts is a finding, and there WAS one before the
environment was restored.** **MEASURED, on first invocation in this
container: 5 failed, 319 passed, 2 deselected.** **That was not caused by
anything in this task** — it was measured at the evidence base, before any
edit — **and it was an environment condition, not a repository defect.**
**Diagnosed and restored under Rule 13; the full account is at `§12.2`.**
**Both figures above were taken after restoration**, and the report says so
rather than quoting the good number and omitting the bad one.

## 7. `A7` — the seventeen other call sites

**MEASURED: `tests/` contains EIGHTEEN `write_text` calls in `.py` sources,
and ZERO specify `newline=` at the evidence base.** One is repaired here;
**SEVENTEEN remain.**

    tests/test_governance_tools.py            9    lines 39, 59, 64, 65, 92, 109, 128, 222, 259
    tests/test_task_checker.py                4    lines 100, 913, 926, 933
    tests/test_betav_campaign_guards.py       2    lines 158, 159
    tests/test_gate_pins.py                   1    line 143     (the OTHER call in the same file)
    tests/test_p2_channel_character_layers.py 1    line 51
                                             --
                                             17

**MEASURED: none of the seventeen was modified.** `§8`'s path comparison
confirms it at the blob level — `tests/test_gate_pins.py` is the only path
in the repository that differs from the base, and within it the diff is one
line at 181.

**The sharpest of the seventeen is `tests/test_gate_pins.py:143`** — the
second call in the very file being repaired. **`§4` of the specification
says "within it, only the one write call", so it was left alone**, and it is
named here so nobody later reads "the pin test was repaired" as meaning the
file was made platform-independent. **It was not.**

**None of the seventeen fails today**: they do not compare written bytes
against a hard-coded byte literal, so a translated `\r\n` never reaches an
equality assertion. **They carry the same undeclared assumption, and a future
test that added such a comparison would fail on Windows with nothing in the
repository to warn its author.**

**Reported as a finding. NOT repaired, NOT registered** — `§3` and `§4`
forbid both, and the governance debt register is frozen at eleven entries.

## 8. `A8`, `A9` — scope and protected paths

**`A8`, MEASURED base to commit 3:**

    A   reviews/chatgpt/2026-08-16T1450Z_repair-pin-test-newline.md
    A   specs/2026-08-16T1450Z_repair-pin-test-newline.md
    M   tests/test_gate_pins.py

    2 additions, 1 modification

**INTENDED, base to commit 4: 3 additions and 1 modification**, the third
addition being this report. **INTENDED and not MEASURED: this report is
written before the commit containing it.**

**No status code other than `A` and `M` appears.** **None of the forbidden
operations — delete, rename, copy, type change, unmerged, unknown —
occurs.**

**The `{HHMM}Z` token is `1450Z`, fixed once by commit 1 and reused
unchanged. No path was chosen by me.**

**`A9`, MEASURED path by path over every path present at the evidence
base:**

    paths at the evidence base      433
    compared                        433
    blob-identical                  432
    differing                         1   —  tests/test_gate_pins.py, and only it
    missing at head                   0

**The named paths, MEASURED individually — all IDENTICAL:**

    GATES.md                        IDENTICAL
    CONVENTIONS.md                  IDENTICAL
    docs/GOVERNANCE-DEBT.md         IDENTICAL
    scripts/                        60 paths,  0 changed
    derivations/                    45 paths,  0 changed
    results/                        69 paths,  0 changed

**No gate state, no register, and no artifact was touched.**

## 9. `A10` — gate invariants and pins

**MEASURED at commit 3, all four:**

    ^## P2- count                        14
    P2-PHASE-01                          Status: PROPOSED          (GATES.md:973)
    first prerequisite                   Prerequisite state: SATISFIED   (GATES.md:1011)
    second prerequisite                  Prerequisite state: SATISFIED   (GATES.md:1036)
    pin at line 1017                     MATCH
    pin at line 1040                     MATCH

**The pins were verified by RECOMPUTING the target digests, not by reading
the pin twice:**

    GATES.md:1017   4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
    sha256 derivations/P2-PHASE-01_microscopic_parameter_domain.md
                    4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214

    GATES.md:1040   e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
    sha256 derivations/P2-PHASE-01_input_admissibility_contract.md
                    e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3

**This is the check the repaired test exists to support**, and it is worth
noting that it is performed here by an independent recomputation rather than
through the test — **the test's job is to prove the validator can tell a
stale pin from a correct one, not to perform this comparison.**

## 10. `A11` — the checker, MEASURED at commit 3

    base   bfef924c368658cac85c04ed18d96eb4450afba6
    head   3461484f60e5725c96d7bd06a962d9e1c70b00c2   (commit 3)

    run 1 INCLUSIVE   exit 0   PASS   sha256 e6cbaf411d80eb577b48639bccf048418ea6c971a7d4fc533fa2fe064fb1f613
    run 1 EXCLUSIVE   exit 0   PASS   sha256 26c3a6890e84a5303320339d6c7bd0d20728199912b99e6c4a8494add1e1d752
    run 2 INCLUSIVE   exit 0   PASS   sha256 e6cbaf411d80eb577b48639bccf048418ea6c971a7d4fc533fa2fe064fb1f613
    run 2 EXCLUSIVE   exit 0   PASS   sha256 26c3a6890e84a5303320339d6c7bd0d20728199912b99e6c4a8494add1e1d752

    P1 PASS   P2 PASS   P3 PASS   P4 PASS
    P5 NOT_APPLICABLE — no merge commit in range
    P6 PASS   P7 PASS   P8 PASS
    P9 NOT_APPLICABLE — range adds no report

    overall PASS in all four invocations.

**`P5` and `P9` are `NOT_APPLICABLE`, which does not make the run
INCOMPLETE**, and both reasons are structural: this task makes no merge, and
commit 3 is measured before the report exists.

### 10.1 What `RUN 1` did

**MEASURED: `RUN 1`'s default subject selection selected exactly one
specification** — this task's own, the only one in range:

    specs/2026-08-16T1450Z_repair-pin-test-newline.md
    stated 3 add / 1 modify    counted 3 add / 1 modify    parse OK

**`RUN 1` and `RUN 2` produced BYTE-IDENTICAL output at each prospectivity
reading**, digest for digest. **That is expected here and does not mean the
two runs are the same check**: `RUN 2` names the subject and `RUN 1`
discovers it, and they coincide only because the range contains one
specification.

**The `C3` multi-specification residual did not arise**, and the reason is
that there is one declaring specification, not that declarations agreed. The
trigger in `_declarations_from_specs` is a DIFFERENCE between declarations,
so a single-specification range cannot reach it. **The residual is unchanged
and unregistered.**

**`P1`'s `counted_set` holds the four LITERAL manifest paths**, token and
all — `reports/2026-08-XXT{HHMM}Z…` — **not the paths actually changed.**
That is `P1` working as specified: it compares a specification's `stated:`
total against the paths its own manifest block enumerates, an
internal-consistency check on the specification and not a comparison against
the diff. Stated here so it is not mistaken for a discrepancy with `§8`'s
measured 2 additions and 1 modification at commit 3.

### 10.2 `declared_source`, `P3` and `P7`

    P3   PASS   declared_source: specification   declared: ['DECISION_LOG.md']
    P7   PASS   declared_source: specification   section_count_head 14

**`P7` reports FOURTEEN sections. `PASS` at zero would have been a STOP, and
it is not zero.**

**MEASURED: `DECLARATION_CONFLICT` appears ZERO times in all four
outputs.**

**`DECISION_LOG.md` is not modified by this range**, so `P3` passed without
exercising the append property; the checker still reports
`base_is_byte_prefix_of_head: true` over 89541 identical bytes.

### 10.3 `RUN 1` config, verbatim — observational, governs nothing

    {
      "base": "bfef924c368658cac85c04ed18d96eb4450afba6",
      "head": "3461484f60e5725c96d7bd06a962d9e1c70b00c2",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 10.4 `RUN 2` config, verbatim — stop-governing

    {
      "base": "bfef924c368658cac85c04ed18d96eb4450afba6",
      "head": "3461484f60e5725c96d7bd06a962d9e1c70b00c2",
      "specification_paths": ["specs/2026-08-16T1450Z_repair-pin-test-newline.md"],
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

### 10.5 The outputs, verbatim

**`RUN 1` and `RUN 2` are byte-identical at each reading**, verified by
`diff`, so the four invocations produce exactly TWO distinct byte strings.
**Both are reproduced below in full — that is both runs and both readings,
with no bytes omitted and none duplicated.**

**`INCLUSIVE` reading — the output of `RUN 1` and of `RUN 2`, byte for
byte:**

    {
      "base": "bfef924c368658cac85c04ed18d96eb4450afba6",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "3461484f60e5725c96d7bd06a962d9e1c70b00c2",
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
                "commit": "4fb1a4ff7f31fee449cda2b8109994ccfde97789",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "5a7a90911a16e59cb9db4fdcf32ff53cbaad7e89",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "3461484f60e5725c96d7bd06a962d9e1c70b00c2",
                "work_paths": [
                  "tests/test_gate_pins.py"
                ]
              }
            ],
            "first_review_commit": "5a7a90911a16e59cb9db4fdcf32ff53cbaad7e89",
            "first_work_commit": "3461484f60e5725c96d7bd06a962d9e1c70b00c2",
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
              "specs/2026-08-16T1450Z_repair-pin-test-newline.md"
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
          "evidence": {
            "merges": []
          },
          "id": "P5",
          "reason": "no merge commit in range",
          "status": "NOT_APPLICABLE",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
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
              "specs/2026-08-16T1450Z_repair-pin-test-newline.md"
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
            "first_commit": "4fb1a4ff7f31fee449cda2b8109994ccfde97789",
            "first_commit_paths": [
              "specs/2026-08-16T1450Z_repair-pin-test-newline.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-16T1450Z_repair-pin-test-newline.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-16T1450Z_repair-pin-test-newline.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {},
          "id": "P9",
          "reason": "range adds no report",
          "status": "NOT_APPLICABLE",
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

**`EXCLUSIVE` reading — the output of `RUN 1` and of `RUN 2`, byte for
byte:**

    {
      "base": "bfef924c368658cac85c04ed18d96eb4450afba6",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "3461484f60e5725c96d7bd06a962d9e1c70b00c2",
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
                "commit": "4fb1a4ff7f31fee449cda2b8109994ccfde97789",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "5a7a90911a16e59cb9db4fdcf32ff53cbaad7e89",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "3461484f60e5725c96d7bd06a962d9e1c70b00c2",
                "work_paths": [
                  "tests/test_gate_pins.py"
                ]
              }
            ],
            "first_review_commit": "5a7a90911a16e59cb9db4fdcf32ff53cbaad7e89",
            "first_work_commit": "3461484f60e5725c96d7bd06a962d9e1c70b00c2",
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
              "specs/2026-08-16T1450Z_repair-pin-test-newline.md"
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
          "evidence": {
            "merges": []
          },
          "id": "P5",
          "reason": "no merge commit in range",
          "status": "NOT_APPLICABLE",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
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
              "specs/2026-08-16T1450Z_repair-pin-test-newline.md"
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
            "first_commit": "4fb1a4ff7f31fee449cda2b8109994ccfde97789",
            "first_commit_paths": [
              "specs/2026-08-16T1450Z_repair-pin-test-newline.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-16T1450Z_repair-pin-test-newline.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-16T1450Z_repair-pin-test-newline.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {},
          "id": "P9",
          "reason": "range adds no report",
          "status": "NOT_APPLICABLE",
          "title": "reports carry a Stops and clarifications section"
        }
      ],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 3,
        "commits_out_of_scope": [],
        "inclusivity": "EXCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

## 11. `A12` — commit-message hygiene

**MEASURED on commits 1–3. Commit 4 is post-report evidence.**

    commit 1   4fb1a4ff   spec: repair the pin test's undeclared platform assumption
               trailer hits 0      not amended
    commit 2   5a7a9091   review: pre-execution review for the pin-test newline repair
               trailer hits 0      not amended
    commit 3   3461484f   test: write the pin fixture with an explicit newline policy
               trailer hits 0      not amended

**MEASURED over the whole range: a scan for `Co-Authored-By`,
`claude.ai/code`, `Generated with`, `Claude-Session` and `noreply@anthropic`
returns ZERO.** **`P6` independently reports `matches: []` for all three
commits.**

**Rule 20 binds this task and was NOT exercised.** **No force-push, no
branch deletion, no history rewrite of any kind.**

**Commits, MEASURED:**

    commit 1   4fb1a4ff7f31fee449cda2b8109994ccfde97789   specs/2026-08-16T1450Z_repair-pin-test-newline.md
    commit 2   5a7a90911a16e59cb9db4fdcf32ff53cbaad7e89   reviews/chatgpt/2026-08-16T1450Z_repair-pin-test-newline.md
    commit 3   3461484f60e5725c96d7bd06a962d9e1c70b00c2   tests/test_gate_pins.py

**Commit 4's message, INTENDED:**

    report: the pin fixture's platform assumption is repaired at one call site

## 12. Stops and clarifications

**NO STOP occurred.** All four checker invocations exited 0, `RUN 2` passed
at both prospectivity readings, and no acceptance criterion failed.

    SPECIFICATION_DEFECT                          0 stops, 0 findings
    ENVIRONMENT                                   0 stops, 2 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 1 finding
    REPOSITORY_DEFECT                             0 stops, 1 finding
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 1 finding

### 12.1 `REPOSITORY_DEFECT` — the one this task repairs

**The defect is the one the specification states**, and I confirmed each of
its load-bearing parts by measurement rather than by reading the
specification back: the write at line 181, the two digests, `_HEX_A` read
from the module, and the fact that the first assertion cannot be the failure
site. **All four hold.**

**It is repaired at one call site. Seventeen others carry the same
assumption and are untouched**, `§7`.

### 12.2 `ENVIRONMENT` — first finding: the container was recreated and was not conformant

**MEASURED, and it is the reason `§6`'s first invocation gave 5 failed, 319
passed.** Diagnosed in Rule 13's order, extended by Amendment D's step 0.

    (0) execution location    /home/user/2-emergent-gravity, worktree
                              governance/repair-pin-test-newline at bfef924c…
                              MEASURED: `git worktree list` showed only this
                              task's worktree. Every worktree from the
                              preceding tasks in this line was gone, and
                              refs/heads/main sat at a different value from
                              the one that container carried. THE CONTAINER
                              WAS RECREATED BETWEEN TASKS.
    (1) execution identity    root, uid 0.  Not the declared identity — see
                              12.3; this is a standing condition, not new.
    (2) interpreter           Python 3.11.15 present and executable.
    (3) permissions           no permission failure at any step.
    (4) filesystem/workspace  MEASURED: the clone was SHALLOW —
                              `git rev-parse --is-shallow-repository` true,
                              142 commits, `.git/shallow` present. Historical
                              objects the governance tests resolve by SHA were
                              absent: `git cat-file -t 8d48798e…` → could not
                              get object info.
    (5) package availability  MEASURED: pytest, numpy and sympy ABSENT from
                              the interpreter. `python -m pytest` →
                              ModuleNotFoundError. Only an isolated uv-managed
                              pytest 9.0.2 on PATH, which cannot import the
                              repository's dependencies.

**Two restorations performed under Rule 13's STANDING AUTHORIZATION, each
reported in one line as the rule requires:**

    RESTORED  installed the declared packages pytest, numpy and sympy into the
              interpreter; resulting versions pytest 9.1.1, numpy 2.4.6,
              sympy 1.14.0.
    RESTORED  completed the shallow clone with `git fetch --unshallow origin`;
              142 → 423 commits, and the historical objects resolve.

**After the second restoration the suite reads 324 passed, 2 deselected —
the declared figure — and the five failures are gone.** **All five were
`git rev-parse … failed: Needed a single revision` on historical SHAs**, and
none of them touched `tests/test_gate_pins.py`.

**Both restorations are environment-layer and changed no repository
content.** Rule 13 is explicit in both directions — an environment problem is
fixed in the environment, and repository content is never modified because a
different environment would make the modification unnecessary. **Nothing in
`§4`'s prohibitions was approached: the only repository byte this task
changed is the one line the specification names.**

**The package versions differ from the declared snapshot for numpy —
2.4.6 against 2.5.1 — and the declaration's own version policy says package
NAMES are the requirement and the versions are a dated snapshot, not
pins.** **Reported rather than left implicit.**

**Rule 13 carries two diagnostic orders, a known open item.** **The extended
order — Amendment D's step 0 followed by Rule 13's five — was the one
exercised, and it was exercised because an environment failure DID occur.**
**Step 0 is what caught it**: without checking worktree identity and the
resolved HEAD I would have attributed the five failures to the repository
and looked for a defect that is not there.

### 12.3 `ENVIRONMENT` — second finding: the declared environment is Windows

**MEASURED, `docs/local/execution_environment.md`:**

    Execution identity     zeta-3070\codexsandboxoffline
    Interpreter            C:\...\Python312\python.exe
    Virtual environment    C:\p2-validator\venv
    Required packages      pytest, ruff, numpy, sympy

**The declared execution environment is WINDOWS. This container is Linux and
has never satisfied that declaration** — not in this task and not in any
preceding one.

**This bears directly on the defect.** The specification's `§1` says the
assumption "was never caught because every executor so far ran on Linux".
**That is true as history, and the inversion is worth stating: the platform
where the test FAILS is the DECLARED one, and the platforms where it passes
are the undeclared ones.** **So this is not a test that works in the real
environment and breaks in an exotic one. It is the reverse.**

**That strengthens the `§1` classification rather than weakening it.** A
validator that fails under the repository's own declared environment, while
passing everywhere its results have actually been produced, is a repository
defect on any reading — **and the reason it survived is that the declaration
and the practice diverged, which no check compares.**

**Reported. NOT registered** — `§4` forbids adding a register entry.

### 12.4 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the remote URL suffix

**`A1` requires confirming a URL ending in `.git`; the measured URL has no
suffix**, `§1`. **`A1`'s stop is scoped to the ref, which matches**, so I did
not stop, and I did not adjust anything to make the strings agree.

**Reported so the next specification in this line can state the URL in
whichever form it wants checked**, rather than leaving an executor to decide
that a suffix is immaterial. **I believe it is immaterial. That belief is not
a measurement, which is why this is a finding and not a silent pass.**

**Reported, NOT registered.**

### 12.5 `OBSERVATION_METHOD_ERROR` — one finding, mine, caught within the task

**My first attempt to establish the platform facts ran `python3 -c` and
crashed on `import pytest` inside the test module**, and my first reaction
was to reach for a different interpreter rather than to ask why the declared
package was missing. **Reaching for a working command is how an environment
defect gets absorbed instead of diagnosed.**

**Corrected by running Rule 13's order properly** — which is what surfaced
the shallow clone at step 4, a condition that would otherwise have shown up
only as five unexplained test failures and might well have been misread as a
repository defect.

**Recorded because the near-miss is the informative part**: the five
failures and the missing packages have a single cause — a recreated,
non-conformant container — and finding it required the ordered diagnosis
rather than a workaround.

### 12.6 `SPECIFICATION_DEFECT` — nothing to report

**Nothing in this specification was found false about the repository or
about its own bytes.** Its pre-issue record was checked against the
repository at four points — the write site and its line number, the two
digests, `_HEX_A`, and the eighteen `write_text` calls with zero `newline=`
— **and MEASURED agrees with it at every one.**

**Its retraction of the earlier `_HEX_A` claim is itself correct**, verified
by reading the constant.

**Nothing in the specification was unsatisfiable.**

### 12.7 What I would have specified differently

**`A6` says "Expected unchanged at 324 passed, 2 deselected" and "a change is
a finding", but it does not say WHEN the before-count is taken.** Here the
honest before-count depended on whether the environment had been restored
first, and the two answers differ by five failures. **I would have had `A6`
require the before-count to be reported with the environment-conformance
state it was taken in**, so that a degraded container cannot produce a
number that reads as a repository regression.

**And `A3` asks for the platform, which is the right question but not quite
the sharpest one.** **I would have had it ask for the platform AND for
whether that platform satisfies `docs/local/execution_environment.md`** —
`§12.3` is only visible because I went and looked, and no criterion required
me to.

## 13. `§7` — Rule 16 assessment

**Rule 16 is operative. All three junctions are addressed.**

### 13.1 First junction — one call site, not a class

**This repairs ONE call. It does not establish that any other fixture in the
repository is platform-independent.**

**MEASURED: seventeen further `write_text` calls in `tests/` carry the same
undeclared assumption and are untouched**, `§7`, including one in the very
file repaired.

**Nothing prevents the next author writing the same defect**, and **this task
deliberately does not build that prevention.** No `conftest.py`, no lint
rule, no helper, no class-wide rewrite. **Such a mechanism needs its own
specification**, and `§4` forbids this task from supplying one.

**So the honest summary is: the repository is one call site less exposed, and
exactly as unprotected as before.**

### 13.2 Second junction — repaired without local reproduction

**On Linux the test passes before AND after. I did not watch it fail.**

**The evidence for the change is (a) the executor report from a Windows
environment and (b) this specification's arithmetic — two digests I
recomputed and which match the reported "expected" and "measured" figures to
the digit.** **The change is justified by derivation and a remote
observation, not by a local failure.**

**What that does not establish**: it does not establish that the reported
Windows failure had this cause and no other. **The arithmetic is consistent
with the report, which is weaker than confirming it.** A Windows run after
this change is the observation that would close it, and **nobody in this task
performed one.**

**`§5`'s Windows statement is marked `DERIVED` for exactly this reason**, and
it is marked `DERIVED` at every occurrence.

### 13.3 Third junction — the other validators were not examined

**A validator built to prevent a false green produced a false red on an
unexamined platform.**

**Did I look at whether the other validators carry the same class of
assumption? PARTLY, and I will say exactly how far.**

**MEASURED: I searched `tests/` for `write_text` and for `newline=`** —
eighteen and zero — **which is the specific mechanism `§3` asks about, and
it is the search `A7` requires.**

**I did NOT search for the class.** No search was made for `open()` in text
mode, `read_text`, `os.linesep`, path separators, locale or encoding
assumptions, case-sensitivity assumptions, or any other
platform-dependence — **and each of those is a way a validator could carry
the same kind of undeclared assumption.**

**So: nothing here establishes that the other validators are free of this
class of assumption, and this task did not look beyond one mechanism.**

**And `§12.3` sharpens why that matters.** The suite's declared environment
is Windows while every observation of it has been made on Linux. **A whole
class of platform assumption could sit in the validators unexercised, and
this task's one grep does not begin to bound it.**

## 14. Did the repair make me want to fix the other seventeen, or add a helper?

**Yes to both, and the second more strongly than the first. Neither was
done.**

**The seventeen: the pull was real but weak.** The change is one keyword
argument, it is mechanical, and having made it once, making it seventeen more
times costs almost nothing. **What stopped it is not effort but evidence:
none of the seventeen fails today, so seventeen edits would be seventeen
untested changes to working tests**, justified by a hazard rather than by a
defect. **A repair with no failing case is a refactor**, and it does not
belong in a task whose scope is one measured failure.

**The helper: this is the one I would flag.** A `conftest.py` fixture, or a
`write_text_bytes()` helper the tests use, would make the defect
unrepresentable rather than repaired — **and "make the bad state
unrepresentable" is the right instinct in almost every other setting.** It
is the reason the pull was stronger.

**`§4` forbids it in terms — "That is a mechanism and it needs its own
specification"** — **and the specification is right, for a reason worth
stating.** A mechanism introduced as a side effect of a one-line repair
arrives without a review, without a scope manifest, and without anyone having
decided whether the whole suite should adopt it. **This programme has a name
for that shape**: a change that is correct in itself and unreviewed in
provenance. **The repair is one line because that is what was specified and
what was evidenced.**

**I also considered, and did not do, adding a comment at line 181 explaining
why `newline=""` is there.** It would be defensible and it is still an
unspecified edit to a file whose permitted change is one line. **Not done.**

**I confirm: I changed exactly one line in exactly one file; did not touch
the assertions, `_HEX_A`, or the fixture string; repaired none of the other
seventeen call sites; added no `conftest.py`, lint rule or helper; modified
no gate, register, artifact, script or result; added no register entry; did
not touch `main` and performed no merge.**

## 15. Evidence layering

**Committed in this report, MEASURED at commit 3:** `A1`–`A7`, `A9`, `A10`
and `A12` for commits 1–3; `A8`'s scope base-to-commit-3 at 2 additions and
1 modification; `A11`'s four invocations with both configs and both distinct
outputs verbatim; commits 1–3 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 4's message; `A8`'s final
base-to-commit-4 scope of 3 additions and 1 modification.

**Labelled `DERIVED` and not measured anywhere:** the behaviour of the
repaired line on Windows, `§5` and `§13.2`.

**Post-report evidence, returned to the Reviewer and NOT written back:**
`A8`'s final scope measured base-to-commit-4; `A11-final`, being `RUN 2`
re-run at commit 4; `A6` at commit 4; `A12` for commit 4; the exact push
command; the branch tip read back from the remote; confirmation that
`refs/heads/main` is unchanged at `bfef924c…`.

**Nothing in this report claims to measure commit 4.**
