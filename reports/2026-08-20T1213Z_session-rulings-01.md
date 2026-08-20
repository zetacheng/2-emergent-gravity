# Execution report — `P2-SESSION-RULINGS-01`

    OUTCOME     STOPPED. Abort A8 fired.

                M2's census found adjudications that landed artifacts
                describe or rely on, that have no entry in `decisions/`,
                and that are NOT in §5's set. Under A8 execution stops
                before any merge and before any landing.

                NOTHING WAS LANDED. No decision record was created, no
                register record was written, no merge was performed and
                no dry-run merge was run. main is untouched.

                The four adjudications §5 covers are not disputed and are
                not the reason for the stop. The set is incomplete, and
                A8 says an incomplete set is re-scoped rather than
                partially landed.

**Specification:** `specs/2026-08-20T1213Z_session-rulings-01.md`
**Review:** `reviews/chatgpt/2026-08-20T1213Z_session-rulings-01.md`
**Base:** `46a9c28697fd5b918c6b3d346bd76f8b68ae6d82`

**Measurement head: `709c3b3`,** the review commit. This report is commit 3 and
is measured at commit N−1.

---

## §0 — Binding SHA (MEASURED, no A1 abort)

    observed origin/main   46a9c28697fd5b918c6b3d346bd76f8b68ae6d82
    §0 declared base       46a9c28697fd5b918c6b3d346bd76f8b68ae6d82

**Equal.**

**Review binding (Rule 18, Amendment N).** The
`Reviewed specification SHA-256:` field was checked for PRESENCE before its
value was compared. Present, once, populated, at
`reviews/chatgpt/2026-08-20T1213Z_session-rulings-01.md:4`.

    sha256 of the specification bytes as committed
      ac0a76f375335428fab1ccc1446e5af87ffe75574a2810f0a73c4918d8c7fef2
    the review's bound SHA
      ac0a76f375335428fab1ccc1446e5af87ffe75574a2810f0a73c4918d8c7fef2

**MATCH.** Verdict `APPROVE FOR EXECUTION`. **This is the revised review**, which
states at its own closing that it supersedes the review of the earlier
revision for execution purposes.

---

## Environment (MEASURED)

**Amendment D step 0.**

    execution location   /tmp/claude-0/-home-user-2-emergent-gravity/
                         30ed7c63-4aac-52db-8b0d-16eb01e07bca/scratchpad/srul
    worktree identity    a real git worktree, branch science/session-rulings-01
    resolved HEAD        709c3b3
    ref reads            /home/user/2-emergent-gravity

    Python 3.11.15   pytest 9.1.1   numpy 2.4.6   sympy 1.14.0   ruff 0.15.8
    scipy  ABSENT — ModuleNotFoundError: No module named 'scipy'

Thirty-fourth consecutive task without `scipy`. Nothing here imports it.

**Rule 13.** No environment failure occurred. Neither diagnostic order was
exercised.

---

## §1 — Measurements

### `M1` — the existing `R-1`–`R-4` entry, verbatim (MEASURED)

`DECISION_LOG.md:2506-2591`, `## 2026-08-20 — OBS-IDENT open records,
registered and none answered`, with `:2509` "Decision owner: Executor, adopted
for the OBS-IDENT integration" and `:2510` "Effect: registers four open
records; answers none; settles nothing".

**What it says about their status**, verbatim, per item:

    :2523   "**`R-1` — `D-2`'s PURPOSE IS UNDECIDED.**"
            and :2526-2527 "Whether `D-2` is re-specified, and as what, is
            not decided."
    :2530   "**`R-2` — THE SCOPE OF `GAP-B`, `MM-1`, `MM-3` AND `MM-5` IS
            UNDECIDED.**"
            and :2533 "What each is about, given the relation, is not decided
            here."
    :2535-2536  "**`R-3` — WHETHER ANY LANDED DESCRIPTION OF `EXT-01`'s
            MEASUREMENT REQUIRES NARROWING IS UNDECIDED**, and so is the
            mechanism if one does."
    :2541   "**`R-4` — THE `A-EXT-01` AMBIGUITY IS OPEN.**"
            and :2543-2544 "Whether a definitional convention silent at that
            point requires supersession is not decided".

and the entry's `### Consequences` at `:2571`: "**Nothing is settled by these
four records.** `R-1` re-specifies nothing, `R-2` rescopes nothing, `R-3`
narrows nothing and alters no landed description, and `R-4` amends no
definitional statement."

**The entry is unmodified by this task.** `DECISION_LOG.md`'s blob is unchanged
from the base; nothing was appended, because `A8` stops before any landing.

### `M2` — THE CENSUS, and it is why execution stopped (MEASURED)

**The census set, bounded from landed text rather than from memory of the
session.** `decisions/README.md:84-85` states: "**PI decisions are filed here
going forward.**" `decisions/` was created by the registry split, landed at
`main` `4257e2a2`. **So the set is adjudications described or relied on by
artifacts landed after that**, and the sweep ran over every path
`git diff --name-only --diff-filter=A 4257e2a2..46a9c28` returns, plus
`DECISION_LOG.md`, `CONVENTIONS.md`, `decisions/README.md` and
`docs/GOVERNANCE-DEBT.md`.

**What `decisions/` contains:** one decision file,
`2026-08-19-inconclusive-disposition.md`, and `README.md`.

**Adjudications with landed provenance — recorded so the census is legible and
not only its residue.**

    ruling 1, PI decisions take effect when issued
        decisions/README.md:29-34, "PI RULING, adopted verbatim", with its
        provenance subsection naming P2-REGISTRY-SPLIT-01 as where the
        superseded PROVISIONAL disposition was first landed.
    ruling 2, the protection model, OPEN      docs/GOVERNANCE-DEBT.md, G-13
    ruling 4, the retrospective reviews       docs/GOVERNANCE-DEBT.md, G-14
    ruling 7, the two wording corrections     docs/GOVERNANCE-DEBT.md, G-15
    the rule 22 mechanism                     decisions/2026-08-19-inconclusive-disposition.md
    the registry split                        DECISION_LOG.md:2425-2451
    the science/* branch class                docs/BRANCHING_POLICY.md:25-40,
                                              and docs/GOVERNANCE-DEBT.md G-12

### `M2`'s FINDING — four adjudications described or relied on, with no landed record of the adjudication

    A   "PI adjudication item 5"
        specs/2026-08-19T2214Z_recon-proj-01.md:8, in that task's Origin
        field: "Origin  PI adjudication item 5, and the projection question
        routed here by EXT-01's execution-layer disposition D-3".
        MEASURED: a repository-wide search for "adjudication item" returns
        THAT LINE AND NOTHING ELSE. The other "item 5" hits are §4 item 5 of
        two unrelated specifications.
        **A numbered PI adjudication with at least five items is cited as a
        landed task's authority, and no landed record of it exists.**

    B   "the PI's ruling that [D-2] is a measurement and not a prerequisite"
        specs/2026-08-19T2214Z_recon-proj-01.md:313-315.
        MEASURED: D-2 IS landed — DECISION_LOG.md:2369-2374 — but as an
        EXECUTOR disposition, "EXTENSION IN MASS AND VOLUME IS DEFERRED, with
        reason", adopted for the EXT-01 integration. **That is not the ruling
        this specification cites**, and no landed record classifies D-2 as a
        measurement rather than a prerequisite.

    C   "the PI has ruled it is not upgraded", of component 9
        specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md:288.
        MEASURED: the other "not upgraded" hits are downstream reasoning about
        WHY component 9 is not upgraded — P2-RECON-PROJ-01's adjudication at
        :435 and its report at :140 — not a record of a PI ruling.
        **A ruling is relied on and no landed record of it exists.**

    D   "the PI tied the component re-scope to the changed epistemic status
        of the projection question"
        specs/2026-08-19T2214Z_recon-proj-01.md:321-323, given as the reason
        Q1 and Q2/Q3 are one task.
        MEASURED: no landed record.

**Against §0b's taxonomy and the Reviewer's §17 caution.** §17 directs that a
recommendation, proposed experiment, open question, or executor-level
disposition must not be classified as an adjudication merely because it
influenced later work. **Applied:**

    B and C are each described IN TERMS as a PI ruling — "the PI's ruling
    that", "the PI has ruled" — and each DECIDES something: a classification
    (measurement, not prerequisite) and a state (not upgraded). Neither is a
    recommendation, an open question, or an executor disposition. Under §0b
    each is a PI RULING.

    A is cited as a task's ORIGIN — the authority under which it was
    commissioned — and is numbered, implying a set. It is not a
    recommendation.

    D is the weakest: a decision about how a task is scoped. It is recorded
    for completeness and the stop does not depend on it.

**The stop does not depend on the weakest case.** **B and C alone are outside
§5's set**, and each is explicitly called a PI ruling by a landed
specification.

**One reading tested and reported rather than chosen silently.** `M2`'s literal
test is "no entry in `decisions/`". Read strictly, rulings 2, 4 and 7 would
also qualify — they are landed in `docs/GOVERNANCE-DEBT.md`, not in
`decisions/`. **They are not counted as findings here**, because §0a states the
defect `M2` looks for is *missing provenance* — "a task that relies on an
unlanded ruling cannot show its authority" — and those three have landed,
citable provenance placed there by a reviewed specification's own direction.
**Both readings reach the same conclusion: adjudications outside §5's set
exist**, so `A8` fires either way, and the difference is reported rather than
resolved by preference.

### `M3` — the registers, read but not written (MEASURED)

Four registers exist: `derivations/P2-DEFERRED-ITEMS.md`,
`derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md`, `docs/GOVERNANCE-DEBT.md` and
`DECISION_LOG.md`. **No §6 record was written to any of them**, because `A8`
stops before any landing. `R-6` and `R-7` do not exist.

### `M5` — the governing clause (MEASURED)

`docs/BRANCHING_POLICY.md:25-40`, `## Science branch integration`. **Located,
and not used** — no merge was performed.

### `M8` — the two Statement SHAs (MEASURED)

    A-EXT-01  ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
    H-EXT-01  e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47

Each present once; neither file modified. **This task modified no file under
`CONVENTIONS.md`, `assumptions/`, `decisions/`, `docs/` or `scripts/`.**

### `M4`, `M6`, `M7`, `M9` — NOT REACHED

Each takes a merge product or a merge as its subject. **`A8` stops execution
before any merge**, and none was performed — including **`M9`'s dry run**,
which is a merge operation and was therefore not run. `A2`, `A3`, `A5` and `A6`
are defined over them and were not evaluated; **they did not pass, they were
not reached.**

---

## §2 — Abort determination

    A1  DID NOT FIRE.  origin/main equals the §0 base.
    A2  NOT REACHED.   Defined over M9; no dry run was performed.
    A3  NOT REACHED.   Defined over M6.
    A4  DID NOT FIRE.  M5 located the clause.
    A5  NOT REACHED.   Defined over M4.
    A6  NOT REACHED.   Defined over M7.
    A7  DID NOT FIRE.  No §4 adjudication was found unlandable as its stated
                       words give it. The stop is about the SET, not about
                       any of the four.
    A8  FIRED.

**`A8`, verbatim from §2:**

>     A8   `M2` finds any adjudication outside §5's set. **Execution stops
>          before any merge and before any landing.** The finding is recorded
>          in the task report and returned to the Researcher; **no §5 decision
>          record and no §6 register record is landed.** The scope of a
>          retrospective provenance task is the set it was written for, and a
>          set found to be incomplete is re-scoped rather than partially
>          landed.

**Complied with exactly.** No decision record was created; no register record
was written; no merge and no dry-run merge was performed; `main` is untouched
at `46a9c286`.

**`C8` was never reached**, and §9 says so: "An execution that finds an extra
adjudication does not fail `C8`; it never reaches it, and `A8` governs
instead." **`R-7` is therefore not written, and its absence is not a defect.**

**No acceptance criterion is reported as satisfied or failed.** Every one is a
property of a landed state, and nothing was landed.

---

## §8 — Substring hazards, and how each was handled

    ruling          THE DECISIVE ONE, and §8 says so: "S-3 arose from exactly
                    this". PI rulings, the rule set, and "ruled" as ordinary
                    past tense all match. Every M2 candidate was reached by
                    READING the sentence and asking who decided what — not by
                    counting the word. B and C survive because each names the
                    PI as the decider and states what was decided; D is
                    reported as the weakest for the same reason.
    decision        `decisions/`, `DECISION_LOG.md`, and "decided". M2's test
                    is over the DIRECTORY, and the two files are kept
                    distinct throughout: D-2 is in DECISION_LOG.md and not in
                    decisions/, which is exactly what makes candidate B a
                    finding rather than a false positive.
    open            an open record, an open question, and "open" as a verb.
                    The Reviewer's §17 turns on the first two not being
                    adjudications; both were excluded by reading.
    R-1..R-7        THREE UNRELATED NAMESPACES, as §8 names: this task's
                    R-labels, the GAP-A integration's R-1/R-2, and the R_i
                    recipe labels of the derivations. All three occur in the
                    material read. Every use above names which, and no
                    R-label was matched across namespaces.
    disposition     the execution-layer sense and ordinary usage. Candidate
                    B turns on the distinction: D-2 is landed AS an
                    execution-layer disposition, which is why the PI ruling
                    cited beside it is not thereby landed.

**Rule.** "A check that cannot state its exclusions is performed by reading."

---

## §0c — Non-objectives, all honoured

    1  act on any adjudication         NOT DONE. Nothing was landed at all.
    2  adjudicate anything the PI did
       not decide, or extend a
       decision beyond its words       NOT DONE.
    3  edit DECISION_LOG.md's R-1..R-4
       entry                           NOT DONE. Its blob is unchanged from
                                       the base.
    4  correct the register-census
       claim                           NOT DONE.
    5  modify any file under scripts/  NOT DONE. The tree is unchanged except
                                       for this task's own three artifacts.

---

## Stops and clarifications

### `S-1` — `SPECIFICATION_DEFECT`: the set §5 was written for is incomplete

**Returned to the Researcher, as `A8` directs.**

**The four adjudications §5 covers are not in dispute.** `R-1` and `R-2` as
ratified dispositions, `R-3` and `R-4` as PI rulings, with their stated words
and their "does not decide" clauses — nothing in the census contradicts any of
them, and nothing here reworks them.

**What the census found is that they are not the whole set.** Two adjudications
are described **in terms** as PI rulings by landed specifications and have no
landed record:

    B   D-2 is a measurement and not a prerequisite
        relied on by specs/2026-08-19T2214Z_recon-proj-01.md:313-315
    C   component 9 is not upgraded
        relied on by specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md:288

and two more are cited as authority without a landed record:

    A   "PI adjudication item 5", the Origin of P2-RECON-PROJ-01
    D   the PI tying the component re-scope to the projection question's
        changed status

**`B` interacts with `R-1` and the interaction is why partial landing would
have been wrong.** `§4.1` lands `R-1`, which **retires `D-2` and splits it**.
Candidate `B` is a separate, earlier ruling about **what `D-2` is** — a
measurement, not a prerequisite. **Landing the retirement of an item while the
ruling that classified it remains unlanded would leave the record with the
disposition and not its ground**, which is the defect §0a describes, reproduced
inside the task meant to close it.

**A re-issue naming the full set is the Researcher's act.** This report does not
propose the set's contents beyond recording what was found, and it does not
land a reduced set — `A8` is explicit that a set found incomplete is re-scoped
rather than partially landed.

### `S-2` — a naming slip in §0a, non-blocking and not the reason for the stop

§0a attributes the effect-when-issued rule to "`P2-GAPB-HOUSEKEEP-02`".
**Measured: no such task exists in the repository.** The rule was landed by
**`P2-GOV-HOUSEKEEP-02`** — `reports/2026-08-19T2324Z_gov-housekeep-02.md:1`,
and `decisions/README.md:36-45` carries the rule with its provenance.

**The rule §0a relies on is real, landed and correctly characterised**; only the
task name is wrong. **Recorded because a later task citing §0a would cite a
task that does not exist**, and because `S-3` of the preceding landing was
about exactly this class — a description that no landed record supports.

### `S-3` — what a strict reading of `M2` would have swept in, and why it is reported rather than acted on

`M2`'s literal test is "no entry in `decisions/`". **Rulings 2, 4 and 7 have no
entry in `decisions/`** — they are in `docs/GOVERNANCE-DEBT.md` as `G-13`,
`G-14` and `G-15`.

**They are not reported as `M2` findings**, because §0a defines the defect as
missing provenance and theirs is landed, citable, and placed there by the
direction of a reviewed specification whose `M4` selected that register.

**Reported rather than silently resolved**, because the two readings differ in
what they sweep in, and an executor choosing the narrower one without saying so
would be making a scope decision inside a census. **Both readings fire `A8`.**

### `S-4` — this is the second consecutive task to find an adjudication described without a landed record

`P2-GAPB-INTEG`'s `S-3` found three items described as ruled with no landed
ruling, and this task was written to close that gap. **The census found four
more of the same shape, older, in specifications landed on 2026-08-19.**

**Recorded as an observation about frequency, not as a proposal.** The
specification's §0a already names the class — "a fact that is true, correctly
relied upon, and never established against the record" — and lists the `S-2`
characterisation rule as not yet landed. **This is a third instance and it is
not landed here either.**

---

## Layering

This report is measured at `709c3b3`, commit N−1. Nothing was landed, `main` is
untouched at `46a9c28697fd5b918c6b3d346bd76f8b68ae6d82`, and the only ref this
task writes is its own branch.
