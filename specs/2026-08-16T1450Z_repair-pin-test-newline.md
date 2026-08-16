# Task specification — repair the pin validator's undeclared platform assumption

Specification evidence base: `bfef924c368658cac85c04ed18d96eb4450afba6`

    Repository         zetacheng/2-emergent-gravity
    Branch to create   governance/repair-pin-test-newline
    Cut from           authoritative main — refs/remotes/origin/main

Classification: **MATERIAL**. Governed by Rule 15, Rule 18, and
**Amendments M–P and Rules 19–21.**

**This task does not touch `main`.** Integration is a separate task.

**One line of test code changes.** **No production code, no checker
property, no gate, no artifact.**

---

## 0. The defect, measured

**`tests/test_gate_pins.py::test_a_stale_pin_is_detected` fails on
Windows and passes on Linux.** **Nothing in the repository declares that
the suite requires a POSIX line-ending convention.**

**The test at lines 178–184 does this:**

    artifact.write_text("content\n", encoding="utf-8")
    measured = hashlib.sha256(artifact.read_bytes()).hexdigest()
    assert measured != _HEX_A
    assert hashlib.sha256(b"content\n").hexdigest() == measured

**`Path.write_text` opens in TEXT MODE.** **On Windows, text mode
translates `\n` to `\r\n` on write.** So `read_bytes()` returns
`b"content\r\n"` while the assertion compares against a hard-coded
`b"content\n"`.

**Measured, and the two figures reported by the executor match to the
digit:**

    sha256(b"content\n")     434728a410a78f56fc1b5899c3593436e61ab0c731e9072d95e96db290205e53
    sha256(b"content\r\n")   fc06f48221d98ad6106c3845b33a2a41152482ab9e697f736ad26db4853fa657

    executor's "expected"    434728a4…    the LF hash
    executor's "measured"    fc06f482…    the CRLF hash

**Measured: `_HEX_A = "a" * 64`.** **Both digests differ from it on
every platform**, so the first assertion passes everywhere and is not
where the failure is.

**The failure is at the SECOND assertion, and only there.** The test
states a byte expectation — `b"content\n"` — while creating the fixture
through a platform-translating text mode. **On Linux the two agree; on
Windows they cannot.**

**An earlier draft of this section claimed `434728a4…` IS `_HEX_A` and
built an argument about the fixture colliding with its own control.**
**That is false.** `_HEX_A` is sixty-four `a` characters. **The claim was
inferred from context and written under a `MEASURED` label without the
constant ever being read**, which is the failure this programme has now
recorded under several names.

## 1. Why this is a repository defect and not an environment problem

**`tests/test_gate_pins.py` is the pin validator built by `C-b` to close
the gap in which the suite could not distinguish a stale pin from a
correct one.**

**It now fails on a platform nobody had run it on, reporting a digest
mismatch that is an artefact of fixture creation rather than of any
pin.** **The check built to prevent a false green produces a false
red.**

**This is the same shape as the odd-extent periodic-lattice hazard
`D-pre-A3` recorded**: a correct check that reads as wrong under a
convention nobody declared.

**It was never caught because every executor so far ran on Linux.**
**The assumption was invisible while the environment was constant.**

## 2. What to change, and what not to

**Change line 181 only:**

    artifact.write_text("content\n", encoding="utf-8", newline="")

**`newline=""` disables the translation.** **The written bytes are then
`b"content\n"` on every platform**, and the second assertion tests what
it was written to test.

**Verified by the specification author**: with `newline=""` the file
contains `b"content\n"` and hashes to `434728a4…`; without it, on a
POSIX platform, the same — **which is precisely why the defect is
invisible here.**

**Do not change the assertions.** **Do not change `_HEX_A`.** **Do not
change the fixture string.** **The test's logic is correct; only its
write was platform-dependent.**

**Do not repair the other seventeen `write_text` calls.** **Measured:
`tests/` contains eighteen `write_text` calls and NONE specifies
`newline=`.** **Seventeen of them do not compare written bytes against a
hard-coded byte string, so none of them fails today** — **but they carry
the same assumption, and it is a finding rather than a repair.** §3
governs.

## 3. The finding, reported and not registered

**Seventeen further `write_text` calls in `tests/` carry the same
undeclared platform assumption.** **Report the count and the files.**

**None fails today.** **A future test that writes with `write_text` and
compares against a hard-coded byte literal would fail on Windows the same
way**, and nothing in the repository would warn its author.

**Do not repair them.** **Do not add a register entry** — the governance
debt register is frozen at eleven. **Report it as a finding, with the
file list, so the next task that touches `tests/` meets it.**

## 4. What this task must not do

- **Do not touch `main`**, do not merge.
- **Do not change any file but `tests/test_gate_pins.py`**, and **within
  it, only the one write call.**
- **Do not change the assertions, `_HEX_A`, or the fixture string.**
- **Do not repair the other seventeen call sites.**
- **Do not add a `conftest.py`, a lint rule, or a helper** to prevent
  recurrence. **That is a mechanism and it needs its own specification.**
- **Do not modify `GATES.md`**, any gate state, any register, or
  anything under `derivations/`, `scripts/` or `results/`.
- **Do not claim this repairs a class of defect.** It repairs one call.

## 5. Acceptance criteria

**A1 — Repository and refs.** Report the `origin` remote URL as measured
and confirm it is
`https://github.com/zetacheng/2-emergent-gravity.git`. **Fetch, then
report `refs/remotes/origin/main` and confirm it is
`bfef924c368658cac85c04ed18d96eb4450afba6`.** **Report
`refs/heads/main` for contrast; a lagging local ref is not a stop.**
**Any mismatch of the authoritative ref → STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18 and Amendment `N`, **carrying `reviewed specification SHA-256:`
filled in.** **Check the FIELD IS PRESENT before checking it matches.**

**A3 — The defect reproduced BEFORE the change.** Report:

    sha256(b"content\n")        expect 434728a4…
    sha256(b"content\r\n")      expect fc06f482…

**and the platform you are running on.** **On Linux, ALSO report that
the test currently passes and state that you cannot reproduce the
failure locally** — **the repair is made on the evidence of the reported
Windows failure and this specification's arithmetic, not on a local
reproduction.** **Say so plainly rather than implying you observed it.**

**A4 — The diff.** Report `git diff` for `tests/test_gate_pins.py` in
full. **Exactly one line changes.** **Report the added-line and
deleted-line counts** — expected one and one.

**A5 — The test passes after the change**, on your platform. Report the
node id and the result. **And report what the change does on Windows,
derived from `newline=""`'s documented behaviour, marked DERIVED and not
MEASURED** — **you cannot measure it here.**

**A6 — Validators, exit status 0.** Run `python -m pytest` from the
repository root. **Report pass and deselect counts before and after.**
**Expected unchanged at 324 passed, 2 deselected** — the test passed
before on this platform and passes after. **A change is a finding.**

**A7 — The seventeen other call sites**, per §3. **Report the count and
the file list**, and **confirm none was modified.**

**A8 — Scope, frozen manifest.**

    stated: 3 additions, 1 modification
    append_only:
      DECISION_LOG.md
    authorised_gates: []
    base: bfef924c368658cac85c04ed18d96eb4450afba6
    head: <commit 4>
    mode: exact
    add:
      reports/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md
      specs/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md
    modify:
      tests/test_gate_pins.py
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Four paths.**

**A9 — Protected paths.** Every path at the evidence base other than
`tests/test_gate_pins.py` is blob-identical at the head. **Report the
count compared**, and confirm explicitly for `GATES.md`,
`CONVENTIONS.md`, `docs/GOVERNANCE-DEBT.md`, and everything under
`scripts/`, `derivations/` and `results/`.

**A10 — Gate invariants and pins.** `^## P2-` count **14**;
`P2-PHASE-01` reads `Status: PROPOSED`; both prerequisites read
`SATISFIED`; both pins match their targets. **Report all four.**

**A11 — The checker over this task's own range**, base `bfef924c…`, head
**commit 3**. Two runs, `RUN 1` observational and `RUN 2` naming only
this task's specification.

**Config for both runs:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  []
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**Report `declared_source` for each** and **confirm no
`DECLARATION_CONFLICT`.** **`P7` must report fourteen sections.**
**`PASS` at zero is a STOP.** **RUN 2 is stop-governing.** **Both configs
and both JSON outputs verbatim.**

**A11-final, post-report evidence:** re-run RUN 2 at commit 4.

**A12 — Commit-message hygiene** on all four commits. **Rule 20 binds
this task.**

## 6. Commit order and evidence layering

    commit 1  specs/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md
    commit 3  tests/test_gate_pins.py
    commit 4  reports/2026-08-XXT{HHMM}Z_repair-pin-test-newline.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused. **You choose
no path.**

**Committed report — measured at commit 3:** A1–A10 and A12; **A11's two
runs with both configs verbatim**; commit 1–3 SHAs and stored messages;
commit 4's intended message; **A8's final scope stated as INTENDED.**

**Post-report evidence, NOT written back:** A8's final scope measured
base-to-commit-4; A11-final; A6 at commit 4; A12 for commit 4; the push;
the branch tip read back.

**Nothing in the committed report may claim to measure commit 4.**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**Three junctions, all three required in the report.**

**First.** **This repairs one call site, not a class.** **Seventeen
others carry the same assumption and are untouched.** **Nothing prevents
the next author writing the same defect**, and **this task deliberately
does not build that prevention.** **Say so.**

**Second.** **The repair is made without local reproduction.** **On
Linux the test passes before and after.** **The evidence is the executor
report from a Windows environment plus this specification's arithmetic**
— **two hashes that match the reported figures to the digit.** **Say that
the change is justified by derivation and a remote observation, not by a
local failure you watched.**

**Third.** **A validator built to prevent a false green produced a false
red on an unexamined platform.** **Nothing establishes that the other
validators are free of the same class of assumption**, and **this task
did not look.** **Say whether you looked, and over what** — **and if you
did not, say that.**

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  one line in `tests/test_gate_pins.py`. **Nothing else, at all.**
- **Do not adjust the config or this specification's declarations to
  make RUN 2 pass.**
- **No force-push and no branch deletion. No history rewrite except the
  narrowly permitted pre-push hygiene repair under Rule 20.**
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §6 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A3's two hashes and your platform**, with the explicit statement
  that the failure was not reproduced locally;
- **A4's full diff with the one-and-one line counts**;
- **A5's node id and result, and the DERIVED statement about Windows**;
- **A6's before-and-after counts**;
- **A7's seventeen call sites with the file list**;
- **A9's path count**;
- **A10's four invariants**;
- **A11's two runs**, both configs verbatim, the section count `P7` saw,
  and what `RUN 1` did;
- **§7's three Rule 16 junctions**;
- **whether the one-line repair made you want to fix the other
  seventeen, or add a helper.** **Say so, and confirm you did not**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H and
Amendment M.**

    target      the repository and the evidence base
    method      git remote get-url origin; git rev-parse origin/main
    MEASURED    https://github.com/zetacheng/2-emergent-gravity.git;
                origin/main = bfef924c368658cac85c04ed18d96eb4450afba6.

    target      the failing test's source
    method      read tests/test_gate_pins.py at origin/main
    MEASURED    test_a_stale_pin_is_detected writes with
                Path.write_text("content\n", encoding="utf-8"), reads
                back with read_bytes(), and asserts equality against
                hashlib.sha256(b"content\n"). Line 181 is the write.

    target      the two digests
    method      hashlib.sha256 on both byte strings
    MEASURED    b"content\n"   -> 434728a410a78f56fc1b5899c3593436e61ab0c731e9072d95e96db290205e53
                b"content\r\n" -> fc06f48221d98ad6106c3845b33a2a41152482ab9e697f736ad26db4853fa657
                These match the executor's reported "expected" and
                "measured" values to the digit.

    target      _HEX_A, read rather than inferred
    method      read line 138 of tests/test_gate_pins.py at origin/main
                and evaluate it
    MEASURED    _HEX_A = "a" * 64, sixty-four 'a' characters. BOTH the
                LF digest 434728a4… and the CRLF digest fc06f482…
                differ from it, on every platform. The first assertion
                therefore passes everywhere and is not the failure site.
                The platform-dependent failure occurs ONLY at the second
                equality assertion.
    RETRACTED   an earlier draft of this record asserted that
                434728a4… IS _HEX_A, under a MEASURED label, without
                the constant having been read. It was inferred from the
                surrounding code. The Reviewer read the file and
                refuted it.

    target      how widely the assumption is carried
    method      grep write_text across tests/, and grep for newline=
    MEASURED    EIGHTEEN write_text calls; ZERO specify newline=.
                Seventeen do not compare written bytes against a
                hard-coded literal and do not fail today. 3 records this
                as a finding and 4 forbids repairing them.

    target      the suite at the evidence base, on Linux
    method      python3 -m pytest -q in a clean clone
    MEASURED    324 passed, 2 deselected in 26.5 seconds. The test
                passes here, which is why A3 requires the executor to
                state that it cannot reproduce the failure locally.

    target      THIS specification's own scope block
    method      parse this file and list its scope keys
    MEASURED    stated, append_only, authorised_gates, base, head, mode,
                add, modify, forbidden_operations.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from the checker at
                origin/main and executed — not re-implemented
    MEASURED    one scope block; stated 3 additions, 1 modification;
                parse OK, counted equals stated per category.
