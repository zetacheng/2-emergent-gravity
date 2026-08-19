# Governance debt — an authoritative register

**Nothing in this file binds.** It records what the rules, amendments and task
reports already carry, and it creates, modifies and explains no obligation.
The rules and amendments in `CONVENTIONS.md` are what govern; this file is a
place a reader meets the debt without reconstructing it from task reports.

Created by `C-c` at evidence base `80595d4cd575d1d024d1415b9b599947bf847677`.

## Why this file exists

Governance debt has been carried in task reports. **A report is a record of
one task**, and nothing aggregated them. Four of the first twelve entries below
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

    REPAIRABLE            2     G-02  G-15
    SPECIFIABLE           3     G-04  G-05  G-06
    NOT REPAIRABLE HERE   1     G-01
    RULED                 3     G-07  G-12  G-14
    METHOD NOTE           1     G-11
    OPEN                  5     G-03  G-08  G-09  G-10  G-13
    ------------------------------------------------
    entries              15

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

## `G-12` — `science/` was an operational branch class the policy did not name

**Disposition: RULED.**

Recorded as this specification's `G-1` item. The identifier follows this
register's own two-digit sequence; `G-1` is the specification's label for the
item, not a register ID.

**ONE entry for the class, not one per branch.**

Through pre-amendment `main` `11af14a7`, `docs/BRANCHING_POLICY.md` named five
branch prefixes — `gate/`, `paper/`, `review/`, `fix/`, `archive/` — and
`science/` was not among them. The word `science` did not occur in the file.
The policy also carried no merge-mode rule for any branch class: `--no-ff`,
`fast-forward` and `rebase` each returned zero, and the only `squash` hit was
`Never squash scientific derivation history`, a prohibition on one mode rather
than a selection among the others.

**MEASURED at `11af14a7`: 37 remote `science/*` refs were already ancestors of
`main`.** Counted by running `git merge-base --is-ancestor` against
`11af14a7` for every ref returned by
`git ls-remote --heads origin 'refs/heads/science/*'`, which is the authority
`docs/BRANCHING_POLICY.md`'s own remote-refs clause requires. 40 remote
`science/*` refs existed in total.

**The PI ruled that these remain accepted, and that no retrospective rewrite
or re-merge is authorized.** The amendment landed by this task is prospective;
it takes effect with the amendment, which is strictly later than `11af14a7`.

**How it was found, and why it sat unnoticed.** Every integration
specification before `P2-POLE-B0-INTEG-01` stated its own merge mode inline.
`P2-POLE-B0-INTEG-01` instead delegated the mode to the policy — and the
lookup failed, producing an `A4` abort with no landing. **The gap was not
created by that task; it was made visible by the first task that asked the
policy the question.** `G-03`'s reservation applies with force here: nothing
would have detected this, and nothing detects the next one.

**Evidence.** `reports/2026-08-19T0319Z_pole-b0-integ-01.md`, the `A4` abort
and its §4 search record; `specs/2026-08-19T0419Z_branching-science-01.md`,
which transcribes the PI ruling; the taxonomy block and
`## Science branch integration` section of `docs/BRANCHING_POLICY.md` as
landed by this task.

## `G-13` — the protection model for review-bound records is unspecified

**Disposition: OPEN.**

**PI RULING, registered verbatim:**

> `CONVENTIONS.md` contains programme-level definitional records, including
> review-bound statements carrying a `Statement SHA`. The repository does not
> presently specify the protection model for such reviewed entries. The open
> question is whether a reviewed definitional statement may be edited in
> place, or instead requires supersession, a new `Statement SHA`, and a new
> review.

**Evidence added, without altering the ruled text.** The question the PI ruled
open names one class of record. **It arises for a second class the ruling does
not name.** `P2-GOV-HOUSEKEEP-02`'s `M6` measured that landed specifications
under `specs/` also carry live review bindings:

    specs/2026-08-19T1723Z_registry-split-01.md
      sha256 6a90c815d4e1912c431e827e0887eb723f2d6bde507782e6245238ad94a49bad
      bound at reviews/chatgpt/2026-08-19T1723Z_registry-split-01.md:4

    specs/2026-08-19T1141Z_integrate-recon-ext-01.md
      sha256 ac0ec0b59e96094bf285d7d1c2e2ebe0528ab425ceb46699c783ee3c0cda4697
      bound at reviews/chatgpt/2026-08-19T1141Z_integrate-recon-ext-01.md:4
      and at reviews/chatgpt/2026-08-19T1141Z_assumption-review_a-ext-01_h-ext-01.md:21
      and at assumptions/H-EXT-01.md:106

**The second file is bound in three places, one of them a landed assumption
record.** A change to its bytes would leave three separate documents naming a
digest the file no longer has.

**The ruled question is NOT rewritten to cover this class.** The measurement is
recorded beneath it as evidence that the open question is broader than the
class it names. **Whether the answer is the same for both classes is part of
what is open.**

**The occasion.** `P2-GOV-HOUSEKEEP-01` stopped on `A2` and, in establishing
where two mis-attributed wording corrections actually lived, measured these
bindings. The discovery is a by-product of a correct refusal.

**Evidence.** `specs/2026-08-19T2324Z_gov-housekeep-02.md` §5.2 and §7;
`reports/2026-08-19T2303Z_gov-housekeep-01.md`, the stop report;
`reports/2026-08-19T2324Z_gov-housekeep-02.md`, this task's `M6`.

## `G-14` — three historical PI records are each owed a retrospective review

**Disposition: RULED.**

**The PI ruled that each of the three `reviews/pi/` records receives a
retrospective review**, labelled

    RETROSPECTIVE REVIEW — non-gating; does not alter the historical effective
    date of the PI decision

reviewing the exact historical bytes actually in force. The historical
decisions are not rewritten to conform to the new registry structure, and a
retrospective review is landed **beside** a record, never into it.

**Status: `REVIEW PENDING` for all three.** **No retrospective-review artifact
has been supplied**, and none was authored — the executor does not write review
content. What is owed, by path and blob id measured at `4257e2a2`:

    930748ed27736c3e369b956b27ec26eb4bff90e8
        reviews/pi/2026-08-03-governance-tools-environment-authorization.md
    dad02415788f153e2c26266f75d6d7a32c7c6001
        reviews/pi/2026-08-03-outcome-based-task-specification-amendment.md
    1e9be1f8dbbffb09b416a483c3b0410da1f4c5fa
        reviews/pi/2026-08-03-p2-dual-pipeline-probe-repin.md

**The disposition is `RULED` and not `OPEN` because the question — whether the
three are reviewed — is settled. The work is not done.** Nothing in this
register discharges it, and nothing here detects that it has gone stale.

**One landed clause was superseded by this ruling.**
`decisions/README.md`'s "Historical PI records" paragraph said the three
records are "not retrospectively reviewed". That clause is no longer operative.
**It was marked in place rather than deleted**, so a reader sees what the
repository said before the ruling.

**The Reviewer recommended against these retrospective reviews.** Under the PI
ruling on when a decision takes effect, that recommendation does not suspend
the ruling. Recorded because it is the first operation of that rule, not
because it is a dispute.

**Evidence.** `specs/2026-08-19T2324Z_gov-housekeep-02.md` §5.3;
`decisions/README.md`, the "When a PI decision takes effect" and "Historical PI
records" sections; `reports/2026-08-19T2324Z_gov-housekeep-02.md`, `M2` and
`M5`.

## `G-15` — errata: two wording corrections not applied to the landed bytes

**Disposition: REPAIRABLE.**

**The repair is known and is blocked only by scope** — specifically by `G-13`,
which must be answered before either correction could be applied where the text
actually sits.

**`W-1` — an overstated clause.**

    file    specs/2026-08-19T1723Z_registry-split-01.md:327-328
    within  §11, "What this task does not establish"
    text    "...by where the file sits, and that every one of them carries
             its review with it."
    reading The clause overstates. The Part 1 / Part 2 structure applies to
            assumptions/ and decisions/. It is not a claim that every record
            referred to carries a review in that layout.

**The narrowing was already recorded beside the passage** before this errata
existed, at `reviews/chatgpt/2026-08-19T1723Z_registry-split-01.md:185`, which
reads the prose "in the context of reviewed scientific propositions and
decisions, not as a claim that every conventional definition necessarily uses
the same Part-1/Part-2 layout."

**`W-2` — article agreement.**

    file    specs/2026-08-19T1141Z_integrate-recon-ext-01.md:286-287
    within  §7, criterion C7
    text    "each identified as a
             execution-layer disposition or an open finding"
    reading "an execution-layer disposition". Article agreement only.

**THE LANDED BYTES ARE DELIBERATELY UNMODIFIED.** Three reasons, on record in
`specs/2026-08-19T2324Z_gov-housekeep-02.md` §7.2: a landed specification's
bytes are the evidence of what was executed and what was reviewed; editing a
review-bound landed record would settle `G-13` by practice while the PI has
ruled it open; and an errata record delivers the same benefit to a reader at no
provenance cost.

**The cost, stated.** A reader who never consults this entry sees the
uncorrected text. **That is `G-03` exactly** — corrections are not discoverable
from what they correct — and this entry does not escape it.

**Both locators were wrong when first written, and were re-measured.**
`P2-GOV-HOUSEKEEP-01` attributed `W-1` to `P2-POLE-B0-INTEG-02` §11 and `W-2`
to `P2-REGISTRY-SPLIT-01` `C7`; both are transpositions. The locations above
are `M3`'s measurement, not a carried figure.

**Evidence.** `specs/2026-08-19T2324Z_gov-housekeep-02.md` §7;
`reports/2026-08-19T2303Z_gov-housekeep-01.md`, which stopped rather than
redirect the ruling; `reports/2026-08-19T2324Z_gov-housekeep-02.md`, `M3`.

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

**It is a list of what was noticed, not a survey.** Four of its first twelve
entries were found only because a later task tripped over them. **The absence of an
entry is not evidence that the corresponding debt does not exist**, and no
survey was performed.

**Nothing in it is repaired by being written down.**
