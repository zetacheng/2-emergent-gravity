# Execution report — `P2-SESSION-RULINGS-02`

    OUTCOME     COMPLETE. No abort fired. Nothing landed, nothing merged,
                nothing confirmed. `main` does not move.

                FIVE of the ten members have a candidate source; FIVE do not.
                Six blocks extracted verbatim by their own delimiters, with
                byte counts recorded so the extraction claim is checkable.

                A4 DID NOT FIRE BECAUSE NOTHING WAS COMBINED. Four members are
                SOURCE UNAVAILABLE, each carrying E5's record of what would
                have had to be combined and what each passage contributes.

                SIX OF THE THIRTY-ONE CITING PASSAGES CARRY A DIFFERENT
                ADJUDICATION'S WORDS than the member they are filed under —
                the shadowing pattern the census itself registered. Recorded,
                not repaired.

                ONE MEMBER'S DISPOSITION TURNS ON A STATED METHOD PARAMETER,
                and the parameter is recorded rather than tuned.

**Specification:** `specs/2026-08-21T1554Z_session-rulings-02.md`
**Review:** `reviews/chatgpt/2026-08-21T1554Z_session-rulings-02.md`
**Extraction artifact:** `derivations/P2-SESSION-RULINGS-02_candidate-sources.md`
**Script added:** `scripts/diagnostics/session_rulings_02_extract.py`
**Base:** `caf5111dacad21da9e204b79b4b7add1f648107c`

**Measurement head: `cc4c7d7`,** the extraction commit. This report is the
commit after it. `C11`'s push clause is INTENDED and measured in the
post-report layer.

---

## §0 — Binding SHA (MEASURED, no `A1` abort)

    observed origin/main    caf5111dacad21da9e204b79b4b7add1f648107c
    §0 evidence base        caf5111dacad21da9e204b79b4b7add1f648107c

**Equal**, measured after `git fetch origin main` at execution start and again
after the extraction commit. `A1` does not fire; `A5` does not fire.

### Review binding (Rule 18, Amendment N) — presence checked before value

`Reviewed specification SHA-256:` is **present**, populated, at
`reviews/chatgpt/2026-08-21T1554Z_session-rulings-02.md:4`, restated at `:113`.

    sha256 of the specification bytes as committed
      2791d7b4c53faa4ab8e431e6ef36a60f2851ee28b142bebf02be4ca74326d49e
    the review's bound SHA
      2791d7b4c53faa4ab8e431e6ef36a60f2851ee28b142bebf02be4ca74326d49e

**Equal**, measured against the committed blob. Both artifacts arrived AS
FILES; neither was pasted.

---

## Environment (MEASURED)

**Amendment D step 0.**

    execution location   /home/user/2-emergent-gravity
    worktree identity    a real git worktree, branch
                         science/session-rulings-02
    resolved HEAD        cc4c7d7 at measurement

    Python 3.11.15   pytest 9.1.1   numpy 2.4.6   sympy 1.14.0   ruff 0.16.3
    scipy  ABSENT — ModuleNotFoundError: No module named 'scipy'

**Clone is full**: no `.git/shallow`, 667 commits reachable from all refs.

**Validators: 332 passed, 2 deselected, exit 0.** Not a criterion here — this
task changes no existing code — and recorded as evidence that nothing broke.

**Lint.** `ruff check` on the added script returns `All checks passed!`. The
repository-wide count is unchanged from the base's standing 13, in four files
this task does not touch.

**Rule 13.** No environment failure occurred. Neither diagnostic order was
exercised.

---

## §1 — Measurements

Nothing was carried, including from the census execution report.

### `M1` — the subject set, READ from the landed census artifact

**Ten members, `ADJ-19` through `ADJ-28`, with 31 citing passages between
them.** Parsed from `derivations/P2-PROVENANCE-CENSUS-01_census.md` §1 by the
added script, which adds and removes nothing.

**`C1`, verified by comparison and not by assertion.** The member ids parsed
from the census and those in the extraction artifact are **identical and in the
same order**, ten and ten, neither more nor fewer. All 31 citing passages the
census records appear in the artifact carrying a classification; **the set
difference is empty**.

**A consistency check the specification did not require.** The 31 citing
passages of `M1` equal the census's own `S_missing` cardinality of 31. **The
two were measured independently and agree**, which is evidence that the subject
set was read rather than reconstructed.

### `M2` — per-passage classification

     6  QUOTED BLOCK
    19  REFERENCE ONLY
     6  INDETERMINATE
    ---
    31

**Every passage carries its reason in the artifact.** The classification turns
on `E3`: a delimited block presenting the adjudication's own words, against a
sentence reporting what was ruled however confidently.

### `M3` — comparison where a member has more than one block

**`ADJ-20`: two passages, ONE block.** `:802` introduces the blockquote at
`:804-842` and `:824` lies inside it. One candidate, not two; the
`AGREE`/`DIVERGE` axis does not arise. **Recorded because two passages sharing
a classification could otherwise read as two competing sources.**

**`ADJ-22`: two blocks, and they are NOT competing versions.** `:111-119` is
labelled `**PI RULING.**` and `:121-135` `**PI RULING — extension of §3a.**`
**The second is expressly an extension of the first.** Recording `DIVERGE`
would misdescribe them and `AGREE` would assert a correspondence that does not
exist. Both are recorded in full and neither is ranked.

**No other member has more than one block of its own.**

### `M4` — per-member disposition

    CANDIDATE AVAILABLE   5    ADJ-20  ADJ-21  ADJ-22  ADJ-23  ADJ-24
    SOURCE UNAVAILABLE    4    ADJ-19  ADJ-25  ADJ-26  ADJ-27
    INDETERMINATE         1    ADJ-28

### `M5` — the two statement pins

    A-EXT-01   ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
    H-EXT-01   e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47

Unchanged. Neither containing file is in this task's changed-file set.

---

## §2 — How the extraction was performed

**`E1` claims extraction rather than transcription, and the claim was made
checkable.** Every block was located by its own delimiter bounds and copied out
of the blob by the added script. **Each of the six candidates was then
INDEPENDENTLY RE-EXTRACTED** straight from `git cat-file blob` in a separate
pass and compared against the artifact's text and against the recorded byte
count.

    804-842   1749 B   in-artifact ✓   independent re-extract ✓   bytes ✓
    72-83      796 B   ✓ ✓ ✓
    111-119    578 B   ✓ ✓ ✓
    121-135   1025 B   ✓ ✓ ✓
    29-30      111 B   ✓ ✓ ✓
    70-75      418 B   ✓ ✓ ✓

**`E2` — one block, one artifact, never merged.** Every candidate is a single
contiguous span; the script has no path that concatenates two runs.

**`E4` — nothing supplied.** No ellipsis filled, no bracket expanded.

**The bounds rule, and its stated parameter.** A block is admitted where a
citing passage lies within it, or begins within **eight lines** of the
passage's recorded line with only a heading, a label or blanks between. **The
window is a parameter of the method and is recorded as one**; `S-2` records the
member whose disposition depends on it.

---

## §3 — Abort conditions, each evaluated

    A1   base SHA differs from §0                          DOES NOT FIRE
    A2   the census artifact cannot be read, or M1's set
         cannot be derived from it                         DOES NOT FIRE
    A3   a member of M1 cannot be located                  DOES NOT FIRE
    A4   a candidate produced by combining passages, or
         by supplying absent words                         DOES NOT FIRE
    A5   main moves during execution                       DOES NOT FIRE
    A6   a path outside the §0d manifest is modified       DOES NOT FIRE

**`A4` deserves its reasoning.** It fires only where a reconstruction **has
been written**. **None was.** Four members had no single sufficient block, and
each was recorded `SOURCE UNAVAILABLE` under `E5` with what would have had to
be combined — **which is the evidential result, not the procedural abort.** The
two are different events and the specification separates them; this execution
met the first and never approached the second.

---

## §6 — Acceptance criteria

    C1   M1's set matches the census, member for member      SATISFIED
    C2   every citing passage classified, with its reason    SATISFIED
    C3   M3 present where a member has >1 block              SATISFIED
    C4   no QUOTED BLOCK is a description of a ruling        SATISFIED
    C5   every candidate verbatim, method and byte count     SATISFIED
    C6   no confirmation, adoption or recommendation         SATISFIED
    C7   §5 item 5's statement, each named item              SATISFIED
    C8   SOURCE UNAVAILABLE members: no reconstruction, E5   SATISFIED
    C9   R-13, R-14, R-15 untouched                          SATISFIED
    C10  M5's two Statement SHAs unchanged                   SATISFIED
    C11  manifest, main unmoved, branch-only push            INTENDED — post-report

**`C4`, in the direction it is exposed in.** The Researcher's §9.3 names the
failure precisely: *a confident description of a ruling is the easiest thing to
admit as the ruling.* **Two members turn on exactly that and were classified
against the grain of how they read.**

`ADJ-19`'s passage opens `**PI ruling: Reading 1 governs.**` and closes
`**You were right to stop.**` — second-person address that reads like the PI's
own speech. **It is still `REFERENCE ONLY`**, because nothing marks where the
ruling's words end and the specification's reasoning begins, so there are no
bounds to extract by. `ADJ-26`'s passage opens `**PI decision, 2026-08-06:**`
and runs straight on into the specification's own justification — *"so that
every report has a corresponding instruction in the repository"* — with no
boundary. **Also `REFERENCE ONLY`.**

**Both would have yielded a plausible candidate had the reading been generous.
Neither did.**

**`C6`, verified by reading.** Every occurrence of "confirm" in the artifact is
a negation or a statement of what would be needed — *"Nothing is confirmed,
adopted, ranked or landed"*, *"No member is confirmed"*, *"what would settle it
is PI confirmation"*. **No candidate is stated to be correct, authoritative or
preferred.**

**`C9`, by reading.** `R-13`, `R-14` and `R-15` **appear nowhere in the
artifact**, in any form. No answer, no partial answer, no proposed rule.

**`C11`.** Four paths: `P1` the artifact, `P2` the script, `P3` the spec and
review.

---

## §7 — Substring hazards, and how each was handled

    ruling        PI rulings against "ruled" as ordinary past tense. Every
                  passage was read in context; the six INDETERMINATE cases are
                  precisely where a "ruling" turned out to be a different one.
    source        candidate source, source branch, source of record. The
                  artifact uses only the first; no branch is called a source
                  here because nothing is merged.
    verbatim      the LABEL on a block against the extraction METHOD. `E1`
                  performs extraction; a label only claims it — and the
                  distinction is load-bearing, since a labelled block has
                  already been measured in this repository to diverge from
                  what it claimed to reproduce.
    record        a canonical record, a census row, "record" as a verb. §5 of
                  the artifact turns on the first.
    quoted        a quotation against "quoted" describing a citation.
    block         a text block; no blocked task arises in this task.

---

## §0c — Non-objectives, all honoured

Nothing was confirmed, ratified, adopted or landed. **No adjudication's wording
was reconstructed from more than one citation**, and `A4` never came into
range. Nothing was paraphrased, summarised, normalised, translated or tidied —
the six candidates are byte-identical to their blobs, independently re-checked.
**No divergence was resolved**: `ADJ-22`'s two blocks are both recorded and
neither is ranked. The census was not re-opened, re-scoped or added to.
`R-13`, `R-14` and `R-15` are untouched. Nothing was merged, `main` did not
move, and no file under `scripts/` was modified — one was **added**, which `P2`
authorises and which is named here and in the artifact.

---

## Stops and clarifications

**No stop occurred.**

### `S-1` — six citing passages carry a different adjudication's words

**Not a stop, and not this task's to repair.**

Six of the 31 passages — `ADJ-22:395`, `ADJ-23:206`, `ADJ-23:313`,
`ADJ-24:79`, `ADJ-24:445`, `ADJ-28:77` — point at a block, or describe a
ruling, that is **not the member's own**. Two of them are delimited blockquotes
that would have extracted cleanly:

    ADJ-23:206  ->  a block at :208-210 whose words are the ARTIFACT-STATE /
                    STATEMENT-KIND namespace ruling
    ADJ-24:79   ->  a block at :79-81 whose words are the MECHANISM-marker
                    ruling

**In every one of the six, the other adjudication is one the census records as
LANDED.** Filing either block as a candidate would have produced a candidate
source for the wrong adjudication — and for an adjudication that does not need
one.

**Category: none for this task — it is a finding about the census's passage
attribution.** It is the pattern the census itself registered as
`THE SHADOWING RISK`, recording that whether other files carry more than one
ruling was unmeasured. **It is now measured, for these ten members: six
passages, in four files.**

**Nothing was expanded, contracted or re-attributed**, per the Reviewer's §11.
Each is classified `INDETERMINATE` with that reason, and the finding is
recorded in the artifact's §4 for the applicable reviewed process.

### `S-2` — `ADJ-28`'s disposition turns on a stated method parameter

**Not a stop; a disclosure, because the alternative was to tune the method to
get a result.**

`ADJ-28`'s two citing passages contain no block. But a delimited block labelled
`**Recorded verbatim as issued.**` sits at
`specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md:51-60`, 701 bytes —
**ten lines past the member's recorded citing line, and the bounds window is
eight.** Widening the window to ten would have produced a candidate.

**The window was not widened.** A parameter changed until it yields a candidate
is not a measurement. Instead the block is **named in the artifact's §6, with
its span and byte count, and explicitly NOT recorded as a candidate**, and the
member is `INDETERMINATE`.

**And the substantive doubt is independent of the window.** The block's subject
is whether an a priori target species count may be imposed. The citation this
member rests on — `derivations/P2-DEFERRED-ITEMS.md:199` — names *"the `D-pre-A`
ruling on the canonical kinetic operator"* as the authority for `DEFERRED-04`.
**Whether these are the same ruling is not established by the citing passages**,
and the artifact records what would settle it: PI confirmation that the block is
the ruling `DEFERRED-04` relies on. **That is this task's product, not its
defect.**

### `S-3` — the first `C5` check reported two false failures

**Not a stop; a method error in my own verification, caught immediately.**

`C5` was first run over **every located block**, of which there are eight, and
reported `in-artifact N` for two. Those two are the non-candidate blocks of
`S-1` — deliberately not reproduced, because they are other adjudications'
words. **The check had conflated "block the script located" with "candidate the
artifact records".**

    first run     8 blocks, 2 reported as absent from the artifact
    corrected     6 candidates, all present, all independently re-extracted,
                  all byte counts matching; the 2 non-candidates confirmed
                  absent, which is the correct state

**Category: `OBSERVATION_METHOD_ERROR`.** **Had the first result been reported
rather than diagnosed, it would have read as two candidates lost in
transcription** — the exact failure `E1` exists to exclude.

### `S-4` — `ADJ-25` is a numbered SET, and the artifact says so rather than splitting it

**Not a stop.** `ADJ-25` is *"the RECON-01B-B0 ruling set — rulings 1, 2 and
4"*: one census member covering three numbered rulings. Its only structured
presentation states each ruling's substance and the specification's response to
it in the same breath, so it is `REFERENCE ONLY` under `E3` and the member is
`SOURCE UNAVAILABLE`.

**Splitting it into three members would have been adding to the subject set**,
which §0c forbids. **Merging its three summaries into one candidate would have
fired `A4`.** Neither was done. The artifact records the question — whether a
set of this kind should be confirmed as one member or three — as open, and does
not answer it.

---

## Rule 16 — the accumulated reading

**The junction is named.** This artifact sits alongside the landed census and
the landed ruling that a specification transcription is not a provenance
record.

**The inference their combination makes available, and which none of them
states, is that the five members with a candidate are now READY TO LAND and the
four marked `SOURCE UNAVAILABLE` are LOST.** **Neither follows.**

A candidate is evidence of content awaiting PI confirmation, and the landed
ruling's second limb is precisely why confirmation is required before anything
becomes a record — **a labelled block in this repository has already been
measured to diverge from what it claimed to reproduce.** And
`SOURCE UNAVAILABLE` is a finding about the repository over the census's citing
passages, not about whether the adjudication was made; the artifact's §5 says
so in terms.

---

## Layering

This report is measured at `cc4c7d7`, the extraction commit, which is commit
N−1. **`C11`'s push clause is measured in the post-report layer**; that
evidence is returned to the Reviewer in chat and is not written back into this
file.
