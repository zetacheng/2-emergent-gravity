# Execution report — `P2-PROVENANCE-CENSUS-INTEG`

    OUTCOME     COMPLETE. No abort fired. The census is landed, the criterion
                it turned on is ratified by a PI ruling landed alongside, and
                three records are registered.

                A7 DID NOT FIRE, AND THE COMPARISON IS RECORDED WITH BOTH
                TEXTS. The criterion the census applied and the criterion §5
                ratifies agree in their operative limb; §5's affirmative limb
                moves no member.

                §5.3's THIRD GROUND IS WEAKER THAN THE SPECIFICATION'S
                WORDING SUGGESTS, AND THE RECORD SAYS SO. The earlier task
                behaved consistently with the distinction, but no artifact of
                that line states it as its motive — and the only landed texts
                that do state it are the census's own artifact and report,
                which cannot ground the ratification of their own criterion.

                M7's TWO MEASUREMENTS DIFFER, for a stated reason: this task's
                own specification and review.

**Specification:** `specs/2026-08-21T0503Z_provenance-census-integ.md`
**Review:** `reviews/chatgpt/2026-08-21T0503Z_provenance-census-integ.md`
**Decision record:** `decisions/2026-08-21-specification-is-not-provenance.md`
**Landing record:** `reports/2026-08-21T0503Z_provenance-census-integ_landing-record.md`
**Source:** `science/provenance-census-01` @ `f69c1a1df5a7d9658ec4e9077cea3894300a1e16`
**Base:** `d9f676a4b7d0a851c82177f8e14cba1af467b06f`

**Measurement head: `de7e777`,** the landing commit. This report is the commit
after it. `C15`'s push clause is INTENDED and measured in the post-report
layer.

---

## §0 — Binding SHAs (MEASURED, no `A1` abort)

    observed origin/main                 d9f676a4b7d0a851c82177f8e14cba1af467b06f
    §0 integration base                  d9f676a4b7d0a851c82177f8e14cba1af467b06f

    observed source ref, from the remote f69c1a1df5a7d9658ec4e9077cea3894300a1e16
    §0 abbreviation                      f69c1a1d

**`M1` read the FULL ref value from `git ls-remote` before anything else, and
it begins with §0's abbreviation.** No merge was attempted against the
abbreviation, and the merge was performed against
`refs/remotes/origin/science/provenance-census-01` — **the remote ref, not the
local branch**, per Rule 5 point 2. `A1` does not fire on either SHA.

### Review binding (Rule 18, Amendment N) — presence checked before value

`Reviewed specification SHA-256:` is **present**, populated, at
`reviews/chatgpt/2026-08-21T0503Z_provenance-census-integ.md:4`, restated at
`:110`.

    sha256 of the specification bytes as committed
      eebcd4c5161f2fa0d49b815ef650a0cef9bfc04496d6e8ecae4154aac0b43efa
    the review's bound SHA
      eebcd4c5161f2fa0d49b815ef650a0cef9bfc04496d6e8ecae4154aac0b43efa

**Equal**, measured against `git cat-file blob` on the committed blob. Both
artifacts arrived AS FILES; neither was pasted.

---

## Environment (MEASURED)

**Amendment D step 0.**

    execution location   /home/user/2-emergent-gravity
    worktree identity    a real git worktree, branch
                         science/integrate-provenance-census-01
    resolved HEAD        de7e777 at measurement
    extra worktrees      two detached worktrees for M2, at the base and at
                         the merge product, outside the repository

    Python 3.11.15   pytest 9.1.1   numpy 2.4.6   sympy 1.14.0   ruff 0.16.3
    scipy  ABSENT — ModuleNotFoundError: No module named 'scipy'

**Clone depth, recorded because `M2` requires it.** No `.git/shallow` exists
and **665 commits are reachable from all refs**. The clone was unshallowed in
an earlier session of this container and remains so. **The shallow-clone
condition that once produced six governance-test failures did not recur, and
its absence was measured rather than assumed.**

**Rule 13.** No environment failure occurred. Neither diagnostic order was
exercised.

---

## §1 — Measurements

Nothing was carried, including from the census execution report. **Every census
figure in the landing record was read from the landed artifact under `M8`.**

    M1   source ref read from the remote                    f69c1a1d… ✓
    M2   validators both sides, unshallowed, real worktrees  332/332 ✓
    M3   dry-run merge                                       conflict-free ✓
    M4   revert hazard                                       subject set EMPTY ✓
    M5   registers' stated scopes, per record                recorded ✓
    M6   the governing clause                                :25-40 ✓
    M7   two diffs                                           they DIFFER ✓
    M8   the census's own values, read not carried           recorded ✓
    M9   the two statement pins                              unchanged ✓
    M10  append-only byte prefix                             verified ✓

**`M2`, `M3`, `M4`, `M6`, `M7`, `M9`, `M10` are recorded in full in the landing
record with their raw values and are not restated here.**

### `M8` — the census's values, READ from the landed artifact

    S_C 263    S_A 151    S_P 120    S_missing 31
    adjudications 33 — 23 with a landed record, 10 with none

**Provenance states the artifact distinguishes:** `FULL` (19) and `SUMMARY` (4)
among the landed, and the ten with none. **The `SUMMARY` state is the one the
artifact surfaced that no rule covers**, and it is transported in the artifact's
own terms.

**The criterion the executor applied under `S-6`, in the artifact's own words**
(`derivations/P2-PROVENANCE-CENSUS-01_census.md:160-161`):

> **A specification is not treated as a landed record of the adjudication it
> transcribes.**

### `M5` — which register admits each §6 record

Recorded in the `DECISION_LOG.md` entry with each register's stated scope read.
`DECISION_LOG.md` admits all three; `derivations/P2-DEFERRED-ITEMS.md` and
`derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md` admit none;
`docs/GOVERNANCE-DEBT.md` admits `R-13` and `R-14` and would admit `R-15`.
**The answer is recorded both ways, and no register was created.** All three
are entered once, in `DECISION_LOG.md`.

---

## `A7` — the guard, evaluated with both texts

**`A7` fires if the criterion recorded in the artifact differs IN SUBSTANCE
from the one §5 ratifies.** Both were read and compared rather than assumed
equivalent.

    AS THE CENSUS APPLIED IT, artifact :160-161
      A specification is not treated as a landed record of the adjudication
      it transcribes.

    AS §5 RATIFIES IT, working translation of the issued text
      A specification that transcribes the words of an adjudication is
      evidence of that adjudication's content, but does not itself constitute
      that adjudication's canonical landed provenance record.

**The operative limb is the same in both**: a specification transcribing an
adjudication is not that adjudication's landed provenance record. **That is the
limb every census value turns on**, and it is identical.

**§5 carries an affirmative limb the artifact's sentence does not** — that the
transcription IS evidence of the content. **It was checked for contradiction
and for effect, separately.** The artifact nowhere claims the content is
unknown, lost or missing; a search for such a claim returns nothing, and the
artifact states at `:164` that the ten "are set out in a specification or a
derivation", which is the same fact §5's FACT LAYER states. And the limb moves
no member: `S_P` membership turns on whether a landed record exists, and
calling the transcription evidence of content does not make it one.

**`A7` DOES NOT FIRE.** The difference is an addition that is consistent with
the artifact and changes nothing it measured.

---

## §2 — Abort conditions, each evaluated

    A1   base or source SHA differs; M1 not matching §0     DOES NOT FIRE
    A2   M3 reports conflicts                               DOES NOT FIRE
    A3   M2 failure not present at the base, unshallowed    DOES NOT FIRE
    A4   M6 finds no clause, or one contradicting §4        DOES NOT FIRE
    A5   product carries a source blob where main advanced  DOES NOT FIRE
    A6   a path outside the §0c manifest in M7              DOES NOT FIRE
    A7   the criterion differs in substance from §5's       DOES NOT FIRE

---

## §7 — Acceptance criteria

    C1   source tip an ancestor of main, and a merge parent   SATISFIED
    C2   main reached its tip by fast-forward from d9f676a4   INTENDED — post-report
    C3   arriving blobs byte-identical, per path              SATISFIED
    C4   §4.1 with the passage/adjudication distinction       SATISFIED
    C5   §4.2 and §4.4, the latter with the wrong-pass check  SATISFIED
    C6   §4.3 verbatim, including the A7-route sentence       SATISFIED
    C7   §4.5 with each of its named items                    SATISFIED
    C8   the §5 record, Part 1 and Part 2                     SATISFIED
    C9   §5.2's layers, §5.3's grounds, §5.4's effect         SATISFIED
    C10  R-13..R-15 recorded and discharged per M5            SATISFIED
    C11  no landing value differs from M8's reading           SATISFIED
    C12  M9's pins unchanged; M10's byte prefix per file      SATISFIED
    C13  M7's base-relative list within the §0c manifest      SATISFIED
    C14  M4 with the manner of any emptiness                  SATISFIED
    C15  refs pushed exactly two                              INTENDED — post-report

**`C3`, on the arriving paths only.** The five paths the merge brought in were
identified by first-parent diff and each compared blob-to-blob against the
source: **all five IDENTICAL**, ids in the landing record. See `S-1` for why the
naive path set was the wrong subject.

**`C6`, byte-exact.** §4.3's block was **extracted programmatically from the
committed specification** by locating its first and last lines, not by
transcription and not by assumed line numbers, and then tested for byte-exact
presence in the landing record. Present, including the sentence that a
reconstruction from citations is what `A7` of the adjudication-source route
forbids.

**`C11`, by comparison and not by assertion.** Seven figures — the four
cardinalities and the three adjudication counts — were re-parsed from the
landed artifact and from the landing record independently and compared pairwise.
**All seven match.**

**`C12`.** `A-EXT-01` `ca8e5a87…` and `H-EXT-01` `e5dd8a28…` identical at source
and base; neither containing file is in the changed-file set. `M10` records the
byte-prefix result: at the merge product **no append-only file is modified**,
and at the landing head `DECISION_LOG.md` is, with `117791` base bytes hashing
identically as a prefix of the `123159`-byte result.

**`C13`.** Seven paths: five arriving from the source (`P1`), and this task's
own specification and review (`P4`).

---

## §8 — Substring hazards, and how each was handled

    record          the provenance record, a census row, and "record" as a
                    verb. §5's ruling is about the FIRST; the landing record's
                    §2 is about the second; the distinction is why §5.2 exists.
    passage         census passages against prose passages — the landing
                    record states the count distinction in the same place as
                    the counts, per §4.1.
    adjudication    the act, the document, and the census class. §4.1's
                    "action set" sentence turns on the first.
    transcription   the source transcription and a specification's
                    transcription of a ruling. §5 turns on the SECOND, and
                    §5.3(a)-(b) cite the first as ground for the second.
    landed          landed on main, against "landed record" as the census's
                    term. §5's ruling uses the census's sense.
    criterion       the S-6 criterion against acceptance criteria. A7 compares
                    the first; §7 lists the second.

---

## §0b — Non-objectives, all honoured

No census member was recomputed, re-scoped or reclassified. **No adjudication
the census found unrecorded was reconstructed, drafted or landed**, and none
was placed, registered or filed. The provenance-tier question is registered
open, not resolved. No citation was amended. No file under `scripts/` was
modified — one arrived by the merge, byte-identical. **No census figure was
stated from anywhere but `M8`'s reading**, verified by `C11`.

---

## Stops and clarifications

**No stop occurred.**

### `S-1` — the first `C3` measurement took the wrong subject and reported a false difference

**Not a stop; caught within the measurement.** `C3` was first run over
`git diff --name-only d9f676a4..<product>`, which returns **seven** paths. Two
of them — this task's own specification and review — are not on the source
branch at all, so `git rev-parse <source>:<path>` had no blob to return and both
reported as differing.

    first run    7 paths, 5 IDENTICAL, 2 reported as *** DIFFERS ***
    corrected    5 arriving paths by first-parent diff, all 5 IDENTICAL

**Category: `OBSERVATION_METHOD_ERROR`.** The criterion says "every ARRIVING
path", and the arriving set is the first-parent diff of the merge, not the
base-relative diff of the branch. **Had the false difference been reported
rather than diagnosed, it would have read as a corrupted merge.**

**The same distinction is what makes `M7`'s two measurements differ**, and that
difference is expected: `M7(a)` is base-relative and includes this task's `P4`
artifacts, `M7(b)` is the source's own contribution and does not. Both are
recorded with the reason.

### `S-2` — §5.3's third ground does not carry the weight its wording invites

**Not a stop, and the review anticipated it.** §5.3 lists as its third ground
that "a later task built a separate record for a document whose items an
earlier specification had already transcribed", adding that whether that was
its stated motive "is established by citation at execution, not asserted here."

**Executed, the citation does not exist.** The behaviour is real and was
verified: `specs/2026-08-19T2324Z_gov-housekeep-02.md:152` heads
`## 5. TRANSCRIPTION — PI rulings 1, 2, 4`, that specification is landed, and
`P2-ADJUDICATION-SOURCE-02` nonetheless built
`decisions/2026-08-20-adjudication-source.md`, which states at `:15-22` that the
document "was acted on before any record of it existed" and "sat nowhere in the
repository" while listing the transcriptions that did exist.

**But no artifact of that earlier line states the distinction as its motive.**
A search of the landed scope for such a statement returns exactly three hits:

    derivations/P2-PROVENANCE-CENSUS-01_census.md:160
    derivations/P2-PROVENANCE-CENSUS-01_census.md:164
    reports/2026-08-21T0308Z_provenance-census-01.md:429

**All three are the census's own.** They are the work this ruling ratifies, and
**they cannot serve as independent ground for ratifying their own criterion.**

**What was done.** The decision record states (c) as **operational
demonstration and not as stated motive**, names the three hits and says whose
they are, and records that the ruling rests on grounds (a) and (b) together
with the PI's own authority. **The ground was weakened in the record rather
than reported as met.**

**Category: `SPECIFICATION_DEFECT`, minor and self-flagged.** §5.3 already
required this check and named the risk; the specification is not wrong, and
what it asked for was done. **It is recorded because the natural reading of
§5.3's three-item list is that all three are established, and one is not.**

### `S-3` — the ruling is landed in a language the repository does not otherwise use

**Not a stop; a disclosure.** §5.1 requires the issued text landed verbatim and
the English rendering identified as a working translation and not as the
ruling. **Both are in the record, and the issued text is stated to govern.**

**The executor cannot verify the translation against the issued text as an
independent check** — it renders a text the executor did not author and cannot
attest to. **It is reproduced exactly as the specification supplies it**, and
the record says the translation "is not the ruling and is not to be cited as
it."

**The Researcher's §10.5 verification step covers precisely this**: reading
§5.1 for whether the translation is anywhere presented as the ruling. **It is
not**, in the decision record, the landing record or this report — each cites
the issued text as the ruling and marks the English as a rendering.

### `S-4` — Part 2 is `REVIEW PENDING`, and a supplied review was NOT used as it

**Not a stop.** §5.5 permits either. **No review of Part 1 was supplied.** The
review that was supplied reviews the SPECIFICATION that landed the record, not
the record; it saw §5's treatment of the ruling and not the record's
construction. **It is named in Part 2 as what it is and is not presented as
Part 2**, which would be the same substitution the ruling itself is about.

---

## Rule 16 — the accumulated reading

**The junction is named.** This landing puts on one branch: the census's
measured `S_missing`, a PI ruling stating that a specification transcription is
not a provenance record, and ten adjudications whose only text sits in exactly
such transcriptions.

**The inference their combination makes available, and which none of them
states, is that those ten adjudications are now KNOWN TO LACK AUTHORITY, or
that their content is lost.** **Neither follows, and both are barred in
terms** — by §4.3's verbatim block, which says the content is not unknown and
the transcriptions may serve as candidate source material; by §5.2's FACT
LAYER; and by §11, which records that no unrecorded adjudication is established
to have lacked authority.

**The opposite misreading is also available and also barred**: that because the
content is present, the ten need only be copied into a register. §4.3 forbids
exactly that — they are single-source, unverified, and **a transcription of
this kind has already been measured to diverge from its source.** They require
PI confirmation, by the route the adjudication-source document took.

---

## Layering

This report is measured at `de7e777`, the landing commit, which is commit N−1.
**`C2`'s fast-forward and `C15`'s push clause are measured in the post-report
layer**; that evidence is returned to the Reviewer in chat and is not written
back into this file.
