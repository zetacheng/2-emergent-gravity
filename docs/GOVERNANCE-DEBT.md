# Governance debt — an authoritative register

**Nothing in this file binds.** It records what the rules, amendments and task
reports already carry, and it creates, modifies and explains no obligation.
The rules and amendments in `CONVENTIONS.md` are what govern; this file is a
place a reader meets the debt without reconstructing it from task reports.

Created by `C-c` at evidence base `80595d4cd575d1d024d1415b9b599947bf847677`.

## Why this file exists

Governance debt has been carried in task reports. **A report is a record of
one task**, and nothing aggregated them. Three of the eleven entries below
were found only because a later task tripped over them.

Two registers already existed at the evidence base and both are science-side:
`derivations/P2-DEFERRED-ITEMS.md`, whose own text says entries are added by PI
decision, and `derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md`, created by `C3`
for the C-check line. **There was no governance-side register.**

## Dispositions

Each entry carries exactly one.

    REPAIRABLE            a repair is known and blocked only by scope
    SPECIFIABLE           the mechanism is fully specifiable inside this
                          repository and none exists
    NOT REPAIRABLE HERE   the cause lies outside this repository
    RULED                 a PI ruling settled it
    METHOD NOTE           a practice, not a defect
    OPEN                  none of the above

**No entry is marked CLOSED.** Nothing here is closed by being written down.
**`SPECIFIABLE` means specifiable, not specified** — it records that a
mechanism shape is known, and no mechanism exists for any entry carrying it.

    REPAIRABLE            1     G-02
    SPECIFIABLE           3     G-04  G-05  G-06
    NOT REPAIRABLE HERE   1     G-01
    RULED                 1     G-07
    METHOD NOTE           1     G-11
    OPEN                  4     G-03  G-08  G-09  G-10
    ------------------------------------------------
    entries              11

---

## `G-01` — the executor harness conflicts with `P6`

**Disposition: NOT REPAIRABLE HERE.**

Generic git guidance supplied to the executor adds a `Co-Authored-By` trailer
and a session URL to commit messages. `P6` forbids both. The conflict recurs on
every task, because the guidance is reissued to every execution.

The cause lies outside this repository and cannot be removed from inside it.
What exists instead is a per-task acceptance criterion for commit-message
hygiene, which each specification remembers to write, and Rule 20, which
permits a pre-push amend to repair a message already written.

**Evidence.** Rule 20 and its source item `B4` in the `C-a` consolidation
record, `CONVENTIONS.md`. The instance that produced Rule 20 is
`reports/2026-08-13T1239Z_ac4-symmetry-goldstone.md`, where three commits
carried the trailers, `P6` failed, and the unpushed history was amended.

## `G-02` — a docstring asserts a freeze the determination rejects

**Disposition: REPAIRABLE.** Blocked only by scope: no task has been
authorised to modify anything under `scripts/`.

`scripts/p2_phase01_scalar_exploratory.py` line 73 reads:

    """Return ``I0(Mhat)`` and ``d I0 / d Mhat`` for the frozen Wilson D."""

The canonical lattice Dirac operator is **not** frozen. The docstring is the
conflation that the `AC-4` determination rejects. The repair is one line.

**Evidence.** The line itself, at the path and line number above, verified
present at the evidence base. The determination is in the `AC-4` line of work.

## `G-03` — corrections are not discoverable from what they correct

**Disposition: OPEN.**

A false `MEASURED` line and its correction landed in the same merge with
nothing linking them, and the shape recurred afterwards. A reader who meets the
false line has no route to the correction.

An executor proposed a repository-level `CORRECTIONS.md` index keyed by
`path:line`. The reservation on record is that nothing would keep such a file
updated. **`C-c` does not decide this**, and the reservation applies to this
register too — see the closing note.

**Evidence.** `reports/2026-08-12T1919Z_integrate-enforcement-checks-v2.md`
line 433, where the index was proposed and the reservation recorded.

## `G-04` — nothing requires a newly issued specification to carry `stated:`

**Disposition: SPECIFIABLE.** The obligation a mechanism would enforce: a
newly issued scope-bearing specification carries a `stated:` record. The shape:
over the specifications a task's range adds, require each scope-bearing one to
carry the key, rather than reaching the question only through subject
selection.

`P1` refuses a scope block without `stated:`, but that refusal is exercised
only when the specification is actually selected as a `P1` subject. A
specification never selected is never asked. The governance-enforcement
classification calls the missing enforcement `C2` and records it as unbuilt.

**This entry is about `stated:` alone.** `append_only:` and
`authorised_gates:` are deliberately not folded in. `C-b` established them as a
declaration mechanism in which `DECLARED_EMPTY` is a valid and meaningful
state, so whether a given task needs either depends on the task, and no
uniform obligation follows.

**Measured, `stated:` alone, specifications under `specs/` carrying the key:**

    13 of 50   at bec01171
    15 of 52   at f179b45e
    17 of 54   at 80595d4c   (this evidence base)

The set carrying the key is contiguous: every specification issued from
`specs/2026-08-12T2015Z_p1-declared-total.md` onward carries it and none before
it does. The specification that issued this task attributed the figure `13 of
50` to `f179b45e`; that figure belongs to `bec01171`, one landing earlier, and
the corrected attribution is recorded here.

**Evidence.** `derivations/GOVERNANCE-ENFORCEMENT_classification.md` line 145,
naming `C2` as unbuilt; the `C-a` consolidation record in `CONVENTIONS.md`,
which records Amendment `O(a)`'s missing enforcement as `C2`.

## `G-05` — nothing compares a review's cited digest against the specification

**Disposition: SPECIFIABLE.** The obligation a mechanism would enforce:
Amendment `N(b)` — a review records the digest it reviewed, and that digest is
the digest of the specification committed beside it. The shape: compare the
digest the review cites against the SHA-256 of the committed specification
blob.

Amendment `N(b)` states the obligation. Nothing checks it, so the check happens
when a task's acceptance criteria remember to ask for it.

**Evidence.** Amendment `N` at `CONVENTIONS.md` line 1183, its source item `A3`
in the `C-a` consolidation record, and that record's own statement that the
review-digest comparison is fully specifiable and registered nowhere.

## `G-06` — nothing performs the auto-merge line-survival check

**Disposition: SPECIFIABLE.** The obligation a mechanism would enforce:
Amendment `P(b)` — an auto-merge is verified by content and not only by blob.
The shape: measure line survival across the merge.

Amendment `P(b)` states the obligation. It has been measured by hand once, by
an executor going beyond its criterion.

**Evidence.** Amendment `P` at `CONVENTIONS.md` line 262, its source item `B3`
in the `C-a` consolidation record, and that record's own statement that the
line-survival check is fully specifiable and registered nowhere.

## `G-07` — the mechanism-marker vocabulary is defined only in a record

**Disposition: RULED.**

The binding rules use the mechanism markers; the sentence explaining what
`MECHANISM DEFERRED` means sits in the `C-a` consolidation record, which is
expressly not a principle. A vocabulary used by rules is therefore defined in
something that governs nothing.

The PI ruled this acceptable, on the ground that a marker is an annotation and
not a requirement. It is recorded here so a later reader knows it was decided
rather than overlooked.

**Evidence.** The markers in use at `CONVENTIONS.md` lines 264, 388, 896 and
1185; the explaining sentence and the marker counts in the `C-a` consolidation
record at lines 1378–1391.

## `G-08` — a criterion can assert something false about its own specification

**Disposition: OPEN.**

A pre-issue verification record checks a specification's literals against the
repository. It does not check what a specification asserts about its own bytes.

The instance: `C-b`'s `A13` asserted that its own scope block declared
`append_only` and `authorised_gates`. It declared neither. The executor
followed the expressly defined config-only path, and the PI ruled the
continuation accepted with `A13` recorded as a specification defect rather than
retroactively satisfied.

This is a narrower subtype of the classification's `C4`. No mechanism shape is
recorded for the general case, which is why the disposition is `OPEN` and not
`SPECIFIABLE`.

**Evidence.** `specs/2026-08-14T2212Z_mechanisms-cb.md`, criterion `A13`;
`reports/2026-08-14T2212Z_mechanisms-cb.md`, where the falsified premise was
reported as a finding; the PI ruling recorded in
`specs/2026-08-14T2307Z_integrate-mechanisms-cb.md` §2.

## `G-09` — nothing independently validates the shared gate-heading grammar

**Disposition: OPEN.**

`C-b` removed the divergence. There is now one shared helper, not two
production grammars, and the two call sites are measured to agree.

What remains is common-mode failure. The helper, the tests asserting it is
correct, and the completeness invariant comparing parsed sections to a raw
count all derive from one author's reading of what a gate heading is. **The
problem is the absence of an independent oracle, not divergence** — there is
nothing left to diverge. An earlier draft phrased this as two grammars drifting
together, which would misdescribe the repository after `C-b`.

This is the residual of `C1`, which is otherwise closed. A mechanism shape for
an independent oracle is not defined, so the disposition is `OPEN`.

**Evidence.** `scripts/governance_tools/task_checker.py`, the shared helper and
the separate `RAW_GATE_HEADING` guard; `tests/test_repository_structure.py`,
the second call site; `reports/2026-08-14T2212Z_mechanisms-cb.md` and
`reports/2026-08-14T2307Z_integrate-mechanisms-cb.md`.

## `G-10` — nothing detects a guard going vacuous

**Disposition: OPEN.**

The pin validator asserts it found at least one pin. `P7` asserts that parsed
sections equal an independently written raw count. Both guards exist because
vacuous passes were met three times, and both were written by the hand that
wrote the thing they guard.

The classification calls this `C5`. **Naming the regress is not solving it**,
and no mechanism shape is defined for detecting a guard that has gone vacuous,
so the disposition is `OPEN`.

**Evidence.** `tests/test_gate_pins.py`, the non-empty-pin-set assertion;
`scripts/governance_tools/task_checker.py`, `P7`'s completeness invariant;
`reports/2026-08-14T0325Z_p7-repair-and-pin-validator.md`, where the vacuous
`P7` was found and repaired.

## `G-11` — a probe contradicting an existing check is likelier to be wrong

**Disposition: METHOD NOTE.** A practice, not a defect in the repository.

The instance: a hand-written pin probe read a field name the pin collector does
not emit, and printed `MISMATCH` for two pins that a landed test had already
passed on. The check was right and the probe was wrong.

The practice this records: when an ad-hoc probe contradicts a check that is
committed and passing, suspect the probe first.

**Evidence.** This entry's instance arose as post-report evidence returned to
the Reviewer for the `C-b` integration and **was not written back into the
repository**, so it does not resolve at the evidence base. The committed
artifacts it concerns are `tests/test_gate_pins.py` and its `collect_pins`
field names. The unresolvable reference is recorded rather than dropped.

---

## Not entered here — `D4`

The classification's `D4`, the unresolved mechanism behind the bit-exact
mirroring, **is not an entry in this register.** It is already registered as
`OPEN-CC-3` in `derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md`, and that
register is where its status lives. A second entry would create a second place
for one status to drift.

## What this register does not do

**It has no mechanism.** Nothing requires an entry to be added when governance
debt is found, nothing checks that an entry stays current, and nothing detects
an entry that has gone stale. **`G-03`'s reservation applies to this file as
much as to the `CORRECTIONS.md` it describes** — the objection that nothing
would keep such a file updated is not answered by this file existing.

**It is a list of what was noticed, not a survey.** Three of its eleven entries
were found only because a later task tripped over them. **The absence of an
entry is not evidence that the corresponding debt does not exist**, and no
survey was performed.

**Nothing in it is repaired by being written down.**
