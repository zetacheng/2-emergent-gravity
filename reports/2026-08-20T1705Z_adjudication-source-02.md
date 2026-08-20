# Execution report — `P2-ADJUDICATION-SOURCE-02`

    OUTCOME     COMPLETE. No abort fired. The adjudication source is landed,
                the item-2 divergence disposed of additively, and five records
                registered.

                A8 DID NOT FIRE, AND THE REASON IS MEASURED, NOT ASSUMED: the
                only divergence M2 found in what an item decides is the item-2
                divergence §5 rules on. Every other item is faithful, landed as
                the act it directs, or not landed.

                ONE DIFFERENCE WAS MEASURED THAT IS NOT AN A8 CASE and is
                recorded rather than passed over: item 4's required label
                landed without the source's trailing full stop, in both places
                it appears.

                TWO CITATIONS IN THE SPECIFICATION'S §5.2 DO NOT RESOLVE AS
                WRITTEN. The substance they assert is fully measured in the
                repository, at a different measurement number. Reported, not
                repaired.

**Specification:** `specs/2026-08-20T1705Z_adjudication-source-02.md`
**Review:** `reviews/chatgpt/2026-08-20T1705Z_adjudication-source-02.md`
**Decision record:** `decisions/2026-08-20-adjudication-source.md`
**Landing record:** `reports/2026-08-20T1705Z_adjudication-source-02_landing-record.md`
**Base:** `46a9c28697fd5b918c6b3d346bd76f8b68ae6d82`

**Measurement head: `ce07c48`,** the landing-record commit. This report is the
commit after it. `C15`'s push clause is INTENDED and measured in the
post-report layer.

---

## §0 — Binding SHAs (MEASURED, no `A1` abort)

    observed origin/main    46a9c28697fd5b918c6b3d346bd76f8b68ae6d82
    §0 integration base     46a9c28697fd5b918c6b3d346bd76f8b68ae6d82

**Equal**, measured twice: once at session start and once immediately before
execution, each after `git fetch origin main`. `A1` does not fire.

**The superseded branch.** §0 names `science/adjudication-source-01` at
`e3bbc7fb` as preserved and not to be integrated. **That ref does not exist on
the remote**, and the object is not reachable in this clone —
`git ls-remote origin refs/heads/science/adjudication-source-01` returns an
empty listing, and `git cat-file -t e3bbc7fb` returns
`fatal: Not a valid object name`, after a full unshallow that fetched all 130
remote refs. **It is unmoved because there is nothing here that could move
it**, which satisfies `C15`'s clause about it while establishing something
weaker than the clause presumes. This is `S-1`.

### Review binding (Rule 18, Amendment N) — checked for PRESENCE before value

`Reviewed specification SHA-256:` is **present**, populated, at
`reviews/chatgpt/2026-08-20T1705Z_adjudication-source-02.md:4` and restated at
`:105`.

    sha256 of the specification bytes as committed
      dcf710e445b8be55b823ea76f71a0e085c0c139e1f1ccb35fee2d190759c0198
    the review's bound SHA
      dcf710e445b8be55b823ea76f71a0e085c0c139e1f1ccb35fee2d190759c0198

**Equal**, measured against `git cat-file blob HEAD:specs/...` after commit 1,
so the binding is verified over the committed bytes and not only the supplied
ones.

**The source artifact and its own review bind too**, and both were checked:

    source transcription
      8c730eacc673153c2cd3b27fa9537186d2151f9c99d42a782cbb2219fb87daf1
    the source review's `Reviewed artifact SHA-256:`
      8c730eacc673153c2cd3b27fa9537186d2151f9c99d42a782cbb2219fb87daf1

**All four supplied artifacts arrived AS FILES.** None was pasted. `A7` does
not fire.

---

## Environment (MEASURED)

**Amendment D step 0.**

    execution location   /home/user/2-emergent-gravity
    worktree identity    a real git worktree, branch
                         science/integrate-adjudication-source-02
    resolved HEAD        ce07c48 at measurement
    extra worktrees      two detached worktrees created for M8 and removed
                         after it, outside the repository

    Python 3.11.15   pytest 9.1.1   numpy 2.4.6   sympy 1.14.0   ruff 0.16.3
    scipy  ABSENT — ModuleNotFoundError: No module named 'scipy'

**Thirty-sixth consecutive task without `scipy`.** This task computes nothing
and adds no script.

**The environment was NOT in its declared state at session start, and was
restored under Rule 13's standing authorization.** Two steps, both reported:
the four declared packages were absent and were installed; and the clone was
**shallow**, which is a workspace condition and is `S-2`.

**`ruff` is `0.16.3` here against `0.15.8` in the preceding tasks.** The
declared environment document states package names as the requirement and its
versions as a dated snapshot rather than pins, so this conforms. **The drift
was tested rather than assumed:** `ruff check .` at `46a9c286` returns
`Found 13 errors` under `0.15.8` and `Found 13 errors` under `0.16.3`, in the
same four files. The lint state is a property of the base, not of the version.

**Rule 13.** After restoration no environment failure occurred. The diagnostic
order was exercised at layer (4), filesystem and workspace — see `S-2`.

---

## §1 — Measurements

**Nothing was carried, including from the predecessor's report**, which in this
execution could not have been carried even had §1 permitted it. See `S-1`.

### `M1` — the item set, read from the source (MEASURED)

**Method, so that no count is asserted.** Every bold heading inside PART B was
enumerated; those beginning with a digit and a full stop were taken as the
numbered items; the numbers were read off in order of appearance.

    bold headings in PART B          8
    of those, numbered               7
    numbers, in order                1 2 3 4 5 6 7
    unnumbered bold headings         1   "Priority / sequencing"

PART B also carries one line of preamble before the first item,
`PI adjudication on the returned items:`.

**Each item's stated words are reproduced in the decision record**, extracted
programmatically from the source span rather than retyped.

**The unnumbered block is recorded and NOT classified**, either way. `R-11`
registers the question.

### `M2` — landed state, per item (MEASURED)

| # | landed? | by | into | comparison |
|---|---|---|---|---|
| 1 | yes | `P2-GOV-HOUSEKEEP-02` | `decisions/README.md:29-34` | **faithful** |
| 2 | yes | `P2-GOV-HOUSEKEEP-02` | `docs/GOVERNANCE-DEBT.md:305-312`, `G-13` | **divergent — the §5 divergence** |
| 3 | yes, as the act | `P2-REGISTRY-SPLIT-01` | `decisions/README.md:11-16`, `assumptions/README.md:14-15`, `:21-26` | no transcription to compare |
| 4 | yes | `P2-GOV-HOUSEKEEP-02` | `decisions/README.md:87-104`, `docs/GOVERNANCE-DEBT.md:346-370`, `G-14` | **faithful but for one full stop** |
| 5 | yes, as the act | `P2-RECON-PROJ-01` | `derivations/P2-RECON-PROJ-01_projection-adjudication.md` | no transcription to compare |
| 6 | **no** | — | — | not landed; no comparison |
| 7 | yes, as a **departure** | `P2-GOV-HOUSEKEEP-02` | `docs/GOVERNANCE-DEBT.md:391-442`, `G-15` | departure, ratified at §6 |

**The comparison method, stated as one function applied to BOTH sides.** Strip
blockquote prefixes, strip code delimiters, collapse all whitespace including
line breaks. This is a **normalised substantive** check, not a byte-exact one,
because PART A asserts byte-identity for neither side and states that the
comparison is against PART B's substantive wording.

**Item 1, the arithmetic.**

    normalised source   cfdf5eb6fbbc153d…
    normalised landed   cfdf5eb6fbbc153d…      equal

**Item 2, both texts in full** are recorded in the correction beneath `G-13`
and are not restated here.

    normalised source   39b182e151a3e4d3…
    normalised landed   0a5d0a5a12d001c7…      NOT equal

Two of the five differences are substantive: the landed text inserts
`carrying a Statement SHA` and omits `Do not infer append-only status and do
not settle the protection model in this task.`

**Item 4, the one difference, measured.** The required label landed as
`…does not alter the historical effective date of the PI decision` against the
source's `…of the PI decision.` — a trailing full stop, absent in **both**
landed instances (`G-14`'s indented block and `decisions/README.md:91-92`'s
inline backticked form). **Nothing else differs.** This is `S-5`.

**Items 3 and 5 have no landed block claiming to reproduce their words.** Item
3 directs that an existing taxonomy be preserved and the taxonomy is what is
landed; item 5 directs a bounded reassessment and the reassessment is what is
landed, cited by number at `specs/2026-08-19T2214Z_recon-proj-01.md:8`.
**Comparing a landing to a directive it executed, as though it were a
transcription of it, would manufacture a divergence out of a category
difference.**

**Item 6 is not landed**, established by search rather than by assumption: no
results directory exists for the extension, and it is named as an outstanding
follow-on at `specs/2026-08-19T2214Z_recon-proj-01.md:313` and
`specs/2026-08-19T2324Z_gov-housekeep-02.md:489`. **`D-2` at
`DECISION_LOG.md:2369` is not its landing** — that is `P2-RECON-EXT-01`'s own
execution-layer disposition, recorded for that task, and it defers the
extension rather than recording this item.

### `M3` — the citing artifacts, by reading (MEASURED, no count carried)

Enumerated in `R-8` and not restated here.

**The finding this measurement produced.** The citation form `PI ruling N` does
not identify a unique ruling set. `derivations/P2-RECON-EXT-01_discarded-external-space.md`
cites `PI ruling 4` at `:14`, `:421` and `:437` as reserving the `TT_RECIPES`
governance question and `PI ruling 2` at `:471` as deferring a criterion until
a magnitude is known; neither matches this document's item 2 or item 4.
**Each hit was read in context before being counted**, and these were excluded
from the citing set on that basis rather than included on the strength of the
match.

### `M4` — which register admits each record (MEASURED, per record)

Recorded in the `DECISION_LOG.md` entry, with each register's stated scope
read: `DECISION_LOG.md` admits all five; `derivations/P2-DEFERRED-ITEMS.md` and
`derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md` admit none;
`docs/GOVERNANCE-DEBT.md` admits `R-12` and would admit `R-8`. **The answer is
recorded both ways** — which admits and which does not — and **no register was
created.** All five are entered once, in `DECISION_LOG.md`.

### `M5` — is an additive correction permitted in `docs/GOVERNANCE-DEBT.md` (MEASURED)

**PERMITTED, and the form is already exercised in the very entry §5.3
corrects.** `G-13` carries a block headed
`**Evidence added, without altering the ruled text.**`, added beneath its ruled
quotation by `P2-GOV-HOUSEKEEP-02`. `G-14` and `G-15` carry comparable
sub-blocks.

The file declares no append-only status and states no prohibition on addition;
its head states that it "records what the rules, amendments and task reports
already carry" and that nothing in it binds. **`A9` does not fire.**

### `M6`, `M8`, `M9`, `M10`, `M7`, `M11`

Recorded in full in the landing record, with the manner of every emptiness.
Summary: dry-run conflict-free; the revert-hazard risk set empty, established
structurally and per path; validators `332 passed, 2 deselected, exit 0` on both
sides in real worktrees; the two `M9` measurements identical; the governing
clause at `docs/BRANCHING_POLICY.md:25-40` with no contradiction; both
`Statement SHA`s unchanged with both containing blobs identical.

---

## §2 — Abort conditions, each evaluated

    A1   base equals §0                                   DOES NOT FIRE
    A2   M10 reports conflicts                            DOES NOT FIRE
    A3   M8 failure not present at base                   DOES NOT FIRE
    A4   M7 finds no clause, or one contradicting §3      DOES NOT FIRE
    A5   product carries a branch blob where main advanced DOES NOT FIRE
    A6   a path outside the §0c manifest in M9            DOES NOT FIRE
    A7   the source document is not supplied              DOES NOT FIRE
    A8   a divergence other than the §5 one               DOES NOT FIRE
    A9   additive correction not permitted                DOES NOT FIRE

**`A8` deserves its reasoning, not just its verdict.** The Reviewer's §4 states
that `A8` fires if `M2` "obtains texts different from the exact divergence
recorded in §5, or finds another substantive source-versus-landed mismatch".

`M2`'s item-2 texts are the previously measured divergence: the inserted
qualifier and the omitted directive sentence, which §5's Level 3 and Level 2
respectively address — Level 3 by determining the forward scope the qualifier
narrowed, Level 2 by determining that the source wording governs the
substantive adjudication content **of that item**, which is what the omitted
sentence is part of. §5's heading is `The item-2 divergence`, singular and
identified by item.

**No other substantive mismatch was found.** Item 4's trailing full stop is a
difference of punctuation in a label and not a difference in what the item
decides — the test PART A states in terms. It is recorded in the decision
record and here rather than absorbed silently.

---

## §8 — Acceptance criteria

    C1   decision record with Part 1 and Part 2           SATISFIED
    C2   Part 1's item set equals M1's, in stated words   SATISFIED
    C3   §4.2's status and statements; both limbs absent  SATISFIED
    C4   §4.3 per item, in the form M2 assigns            SATISFIED
    C5   §4.4's two entries; ordering as four steps       SATISFIED
    C6   §5.3 correction with all six elements            SATISFIED
    C7   no landed quoted block altered                   SATISFIED
    C8   §5.1's three levels; negative limb absent        SATISFIED
    C9   §5.2's ground forward-looking, values read       SATISFIED — with S-3
    C10  §6's ratification, all four statements           SATISFIED
    C11  R-8..R-12 recorded and discharged per M4         SATISFIED
    C12  M6 with the manner of any emptiness              SATISFIED
    C13  M11 pins unchanged; append-only byte-prefix      SATISFIED
    C14  M9's list within the §0c manifest                SATISFIED
    C15  refs pushed exactly two; superseded unmoved      INTENDED — post-report

**`C2`, mechanically.** Each of the eight blocks measured by `M1` was tested
for byte-exact presence in the decision record as a quoted block. All eight
present; the numbered headings quoted in the record are `1 2 3 4 5 6 7` and no
others.

**`C7`, by diff and by blob.** `docs/GOVERNANCE-DEBT.md`: `121` insertions, `0`
deletions, **one hunk at `--unified=0`** — the context is named because a hunk
count is a property of a change and a context together. Its bytes through
`:344` hash to `ebbaa424c6b1e928…` at the base and on the branch alike. Every
artifact `M3` enumerates was compared blob-to-blob between `46a9c286` and the
branch head: **all UNCHANGED.**

**`C13`.** `A-EXT-01` `ca8e5a87…`, `H-EXT-01` `e5dd8a28…`, both unchanged;
`CONVENTIONS.md` blob `5be8e49b…` and `assumptions/H-EXT-01.md` blob
`3d3d3a0b…` identical at base and product. `DECISION_LOG.md`'s first `112339`
bytes hash to `5eb972fcde2158ab…`, which is the base blob's full-content digest
— **an append, verified by byte prefix and not by line count.**

**`C14`.** Five paths, each mapped to the manifest entry that admits it: `P1`
the decision record, `P2` `docs/GOVERNANCE-DEBT.md`, `P3` `DECISION_LOG.md`,
`P4` the spec and the review.

---

## §9 — Substring hazards, and how each was handled

    verbatim     Searched, then every hit read in context. The label under
                 examination is `PI RULING, registered verbatim:` at
                 `docs/GOVERNANCE-DEBT.md:305`. `CONVENTIONS.md:1456` and
                 `:1492` carry `PI RULING, adopted verbatim:` for Rules 21
                 and 22 — DIFFERENT rulings, not items of this document, and
                 excluded on that ground. Ordinary uses in `AGENTS.md`,
                 `MIGRATION.md` and `GATES.md` excluded by reading.
    item         Disambiguated by context throughout: the document's numbered
                 items, register items (`G-`, `R-`, `OPEN-CC-`), and ordinary
                 prose are distinct and are never counted together.
    scope        Three senses kept apart: the open protection question's
                 scope, a register's stated scope (`M4`), and this task's
                 authorised path manifest (`C14`).
    ruling       `PI ruling N` proved genuinely ambiguous across the
                 repository — that is `R-8`, and it was found by reading hits
                 rather than counting them.
    qualifier    The inserted phrase, distinguished from grammatical usage.
    divergence   Only one was found in what an item decides, and it is the
                 §5 one.

---

## §0b — Non-objectives, all honoured

No item was re-adjudicated and no item's stated words were altered. Which text
of the divergent item was originally issued is not decided, and the record says
it is not determinable. No landed quoted block was rewritten. Nothing was acted
on beyond §5 and §6. No landed-and-faithful item was re-opened. `R-1`–`R-4` are
untouched and no census was performed. **The superseded branch was not
integrated** — and could not have been, being absent from this clone. No file
under `scripts/` was modified; the changed-file set contains none. No
append-only file's history was edited, verified by byte prefix.

---

## §12 — What this task does not establish

It lands a source that was acted on without one and disposes of one known
divergence. **It produces no scientific result**, measures no physical
quantity, and moves no gate. `Q1`, `GAP-A`, `GAP-B`, `A-EXT-01` and `H-EXT-01`
are untouched; `P2-PHASE-01` is unchanged.

**It does not make the earlier citations correct**, and it does not establish
what the original document said where the evidence does not.

**Rule 16 — the accumulated reading.** The junction is named rather than
assured. `decisions/2026-08-20-adjudication-source.md` and the correction
beneath `G-13` now sit on one branch with `decisions/README.md`,
`docs/GOVERNANCE-DEBT.md`'s `G-13`/`G-14`/`G-15` and
`specs/2026-08-19T2324Z_gov-housekeep-02.md`. **The inference their combination
makes available, and which none of them states, is that the adjudication
document is now established as a historical record — that because its content
is confirmed and its items are landed, the document existed as recorded at the
time it was acted on.** It does not follow and is not established. The
confirmation is of content at this landing; the original issuance remains not
established by the surviving record, in either direction.

---

## Stops and clarifications

### `S-1` — the predecessor's branch and report are unreachable here

**Not a stop in this execution.** `science/adjudication-source-01` is absent
from the remote's 130 refs and `e3bbc7fb` is not a valid object in this clone,
after a full unshallow.

    $ git ls-remote origin refs/heads/science/adjudication-source-01
    (empty)
    $ git cat-file -t e3bbc7fb
    fatal: Not a valid object name e3bbc7fb

**Category: `ENVIRONMENT`.** The container is new; the previous session's
unpushed branches did not survive it.

**Why it changed nothing.** §1 forbids carrying the predecessor's `M1`, `M2` or
`M3` results, so the task was already required to re-measure them, and it did.
**The one thing it does change is `C15`'s clause about the superseded branch**,
which is satisfied vacuously rather than by observing an unmoved remote ref, and
that is stated rather than glossed.

### `S-2` — the clone arrived shallow, and six validator failures were its artifact

**Not a stop. Caught before any criterion consumed it.** At session start
`python -m pytest -q` returned:

    6 failed, 326 passed, 2 deselected

with every failure of the form

    scripts.governance_tools.core.InputError: git rev-parse --verify
    cc8adaa04ed75f5118ae2c25926a05e51a0056ff^{commit} failed:
    fatal: Needed a single revision

**Category: `ENVIRONMENT`, Rule 13 diagnostic layer (4), filesystem and
workspace.** The clone carried `.git/shallow` and 141 commits. Governance-tool
tests resolve historical commits by SHA, and a depth-truncated clone does not
carry them. `git fetch --unshallow` restored 613 commits and all remote refs,
after which the suite returned `332 passed, 2 deselected, exit 0` — the figure
this line has held for thirty-five consecutive tasks, and `326 + 6 = 332`
accounts for the deficit exactly.

**Why it is worth recording.** A task that ran its validators before
unshallowing would read six `REPOSITORY_DEFECT`s that are not defects, in the
governance tooling specifically. **Nothing in the environment document mentions
clone depth**, and nothing detects it.

### `S-3` — §5.2's two measurement citations do not resolve as written

**Not a stop. `C9` is satisfied; the citations are reported, not repaired.**

§5.2 names "`M3` of `P2-GOV-HOUSEKEEP-02` and `M6` of `P2-GAPA-INTEG`" as the
measurements grounding the Level 3 determination. Read at execution:

    P2-GOV-HOUSEKEEP-02  M3  "the two `W-` locators, RE-MEASURED"
                             — item 7's errata locators, a different subject
    P2-GOV-HOUSEKEEP-02  M6  "SHA-256 of each located file, and what binds it"
                             — THIS is the measurement §5.2 describes, and it
                             carries BOTH halves of the description
    P2-GAPA-INTEG        M6  "the governing clause" — `BRANCHING_POLICY.md:25-40`,
                             the same measurement this task's own M7 makes

**`P2-GOV-HOUSEKEEP-02`'s `M6` says so itself**, in its own closing sentence:
"This is the evidence §5.2 records beneath the ruled question." And `G-13`'s
landed evidence section already cites it correctly, as `M6`.

**Category: `SPECIFICATION_DEFECT`** — a dangling reference, one of the four
defect classes §0c's self-check enumerates. **The determination it grounds does
not fail**: the substance is fully measured, in one place, and its values are
read into the correction. **The executor did not amend the specification**, and
the correction cites the measurement that actually carries the values rather
than the number §5.2 gives.

### `S-4` — Rule 5 point 2 against §3's merge subject

**Not a stop, and the reasoning is recorded because the alternative was to
stop.**

Rule 5 point 2 reads "merge the pinned REMOTE ref, never a local branch". §3
directs a `--no-ff` merge of **this task's branch**, and its push scope —
"the integration branch and `refs/heads/main` and no other ref", restated by
`C15` — forbids pushing that branch. On its face the two cannot both be
satisfied.

**They do not conflict, because Rule 5 point 2's premise is not instantiated.**
Its subject is a source branch pinned by SHA in an integration specification
and prepared by an earlier task; the defect it prevents is merging a local copy
that differs from the reviewed remote one. This task's branch has no remote
counterpart to differ from, no pin, and was created in this same execution from
the commits this execution just made.

**And the shape is exercised precedent, in this very line.**
`P2-GOV-HOUSEKEEP-02` — the task that landed items 1, 2, 4 and 7 — did exactly
this: its work branch was never pushed as a ref, it was `--no-ff` merged into
`science/integrate-gov-housekeep-02`, and its tip `434b61f` survives on the
remote **only as a merge parent**, with no ref pointing at it. Measured:

    $ git ls-remote origin refs/heads/science/gov-housekeep-02
    (empty)
    $ git ls-remote origin | grep 434b61f
    (no match)

`docs/BRANCHING_POLICY.md` contemplates that state in terms — "Merged, tip
recoverable as a merge parent… The content, grouping and tip SHA survive in the
merge commit."

**What the executor did instead of deciding silently.** The reviewed-content
question Rule 5 point 2 protects was measured directly: the merge-base equals
the base equals `origin/main` at `46a9c286`, verified after fetching; the merge
is conflict-free; and the merge product's changed-file set equals the branch's
own contribution exactly. **If the Reviewer reads Rule 5 point 2 as reaching
this case, this is the finding to act on**, and the landing is the thing to
reverse.

### `S-5` — item 4's label lost a trailing full stop

**Not an `A8` case, and recorded rather than absorbed.** Measured above under
`M2`. It is a difference of punctuation at the end of a label, in both landed
instances, with nothing else differing. **PART A's stated test is whether what
an item decides differs**, and it does not. It is written into the decision
record beside item 4 so a later reader meets it rather than rediscovers it.

**Category: none — this is a measurement, not a defect.** Whether the label
literal should be exact is `R-12`'s territory and the census's, not this
task's.

### `S-6` — the supplied source artifacts are not admitted by the §0c manifest

**Not a stop. A scope reading, recorded because it was a judgement.**

The source transcription and its review were supplied as files and are
governing artifacts. **Neither is admitted by §0c.** `P1` covers "the decision
record(s) created under §4, and any review artifact supplied **for them**" — a
Part 2 review of the decision record, which was not supplied; `P2` and `P3` are
registers; `P4` is this task's spec, review, landing-record and report.

**So neither file's bytes were committed**, and committing them would have
fired `A6`. **The specification's own design is what makes this correct rather
than lossy**: §4.1 is the mechanism by which the source's content enters the
repository, item by item in stated words, and it did. Both digests are recorded
in the decision record's §6 and in this report.

**The residue, stated plainly.** The source review's bytes now exist only
outside the repository, while a digest naming them is committed. That is the
shape Amendment N(b) exists to make checkable, and here it is not checkable
from inside. **The executor did not extend the manifest to fix it**; it is
reported for the specifier.

### `S-7` — two `C3` checks returned false negatives on the first pass

**Not a stop; a method error caught by the method.** Two of `C3`'s required
statements initially reported `MISSING`. Both were present and line-wrapped;
the check was a single-line grep. Re-run with whitespace normalised across line
breaks, both are present, and all eight statements pass.

**Category: `OBSERVATION_METHOD_ERROR`.** This is a known defect class in this
line — "a single-line grep returns a false negative when the target string
spans a line break". **It is recorded because it nearly produced a false
report of an unsatisfied criterion**, which is the more expensive direction of
that error.

---

## Layering

This report is measured at `ce07c48`, the landing-record commit, which is commit
N−1. **`C15`'s push clause and the fast-forward of `main` are measured in the
post-report layer**; that evidence is returned to the Reviewer in chat and is
not written back into this file.
