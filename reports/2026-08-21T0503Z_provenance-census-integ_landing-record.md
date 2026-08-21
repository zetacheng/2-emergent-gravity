# Landing record — `P2-PROVENANCE-CENSUS-INTEG`

**Transport of a reviewed measurement, plus one PI decision landed alongside.**
Every census figure below is READ from the landed artifact under `M8`. **None
is carried from the census execution report**, and none is restated from this
task's specification, which states no figure.

    Source          science/provenance-census-01
                    f69c1a1df5a7d9658ec4e9077cea3894300a1e16
    Base            d9f676a4b7d0a851c82177f8e14cba1af467b06f
    Fork point      d9f676a4b7d0a851c82177f8e14cba1af467b06f
    Merge product   83b00edfd64fe75e8c57f08846891269b73a0e58

---

## 1. The result, as measured

**Read from `derivations/P2-PROVENANCE-CENSUS-01_census.md` at the merge
product.**

    S_C        263   candidate passages admitted by M1's predicate
    S_A        151   of those, passages referring to a PI ruling or a
                     PI-ratified disposition
    S_P        120   of those, whose adjudication has a landed record
    S_missing   31   of those, whose adjudication has none

    identity   S_missing = S_A - S_P   =>   151 - 120 = 31

    adjudications identified          33
      with a landed record            23
      with none found in this scope   10

**A PASSAGE COUNT IS NOT AN ADJUDICATION COUNT, and the two differ here by
threefold.** The 31 passages of `S_missing` refer to **TEN** distinct
adjudications; a single adjudication is cited in as many as seven of them.

**THE ACTION SET FOR ANY LATER TASK IS THE TEN ADJUDICATIONS, NOT THE THIRTY-ONE
PASSAGES.** Acting per passage would take up one adjudication as many times as
it happens to be cited, and would record it several times over.

## 2. The provenance states the census distinguishes

**Recorded as the artifact records them, in its own terms.** The artifact's §2
states:

    FULL      the adjudication's words are landed in a register or a
              governing document
    SUMMARY   a register records that it occurred and what it decided,
              without its words, and points elsewhere for them

**Of the twenty-three landed, nineteen are `FULL` and four are `SUMMARY`.**

**THE `SUMMARY` STATE IS ONE NO RULE COVERS.** The artifact records that
`G-08`'s evidence line points at a specification as the place its ruling is
recorded — the same arrangement as the ten with no record at all, differing
only in that a register notices it.

**The census's measurement was a binary and it is NOT revised here.** Whether
the model should be revised is registered open as `R-13`; it is not this
record's to decide, and this record decides nothing about it.

## 3. What `S_missing` means, and what it does not

**Reproduced verbatim from the governing specification, because the misreading
is the one that would do damage:**

> `S_missing` means **no landed provenance record was found in the searched
> scope**. It does **not** mean the content is unknown. Where a specification
> transcribes an adjudication's words, those words are **evidence of the
> content and may serve as candidate source material** — but they are a single
> source, unverified against any other, and a transcription of this kind has
> already been measured to diverge from its source. **They therefore require
> PI confirmation before becoming a record**, by the same route the
> adjudication-source document took.

**Any later task that reconstructs an adjudication from citations instead of
confirming a candidate source is doing what `A7` of that route forbids.**
## 4. The method findings, transported

**The census recorded its own method errors, and they travel with it.**

**The set-relation check that PASSED WHILE WRONG.** The census's independent
verification of `S_A ⊆ S_C`, `S_P ⊆ S_A` and `S_missing = S_A − S_P` was run
against a parse of its own printed table. A character-class error in that
parser — a range that excluded the letter marking membership of `S_P` — dropped
**every** `S_P` row before any relation was evaluated. All three relations then
held **trivially**: the empty set is a subset of anything, and subtracting it
changes nothing. The check reported green over a set it had never read.

**It was caught because a cardinality was implausible, not because a relation
failed.** This is transported because the failure is reusable, not because it
is this census's peculiarity: **set identities all evaluating true does not
establish that the parser is correct.** It is registered as `R-15`.

**Two further errors the census recorded.** A per-file rule for attributing a
citation to an adjudication shadowed two rulings that sit inside files about a
different ruling — caught by an arithmetic disagreement between the number of
unrecorded adjudications and the number appearing in `S_missing`, not by
re-reading. And an `M5` comparison run against an assumed line range produced a
false `DIVERGENT` against a landed rule before correction to `FAITHFUL`.

## 5. What the census does not establish

**As the artifact states it.**

**`S_missing` is a measurement over the SEARCHED SCOPE, not over the
repository.** `reviews/` and `reports/` were not searched, and `reviews/pi/`
holds three historical PI records the census could not read. An adjudication
landed only there would appear in `S_missing` and would not be missing.

**A member of `S_missing` may have had authority whose record did not
survive.** Absence of surviving provenance is not evidence of absence of
historical authorisation.

**No member's effective date is determined**, in either direction, for any of
the thirty-three.

## 6. Rule 17 — what this integration did NOT add

**No census member was recomputed, re-scoped or reclassified.** No adjudication
was reconstructed, drafted, placed, registered or filed. No citation was
amended. The provenance-tier question was not resolved. **The three records of
§7 are registered as open records that settle nothing**, and are recorded in
`DECISION_LOG.md` rather than drawn as conclusions here.

**The PI decision landed alongside is not Rule 17 territory, and the reason is
recorded.** It ratifies a criterion the executor had already applied and stated
for rejection; a ratification of an applied criterion reclassifies nothing. Had
the ruling gone the other way, the census would require recomputation and this
task would not have been the vehicle.

---

## 7. The merge, measured

### `M1` — the source ref, read from the remote (MEASURED)

    git ls-remote origin refs/heads/science/provenance-census-01
      f69c1a1df5a7d9658ec4e9077cea3894300a1e16

**Begins with §0's abbreviation `f69c1a1d`.** No merge was attempted against
the abbreviation. `A1` does not fire.

### `M3` — dry-run merge (MEASURED)

`git merge-tree --write-tree --messages` returned tree
`657352511c285b2647378340d5ed7f650f04bf30`, exit `0`, **no conflicting paths.**
`A2` does not fire.

### `M4` — the revert hazard: the subject set is EMPTY (MEASURED)

**Paths present on both `d9f676a4` and the source at differing blobs, measured
by `git diff --name-only --diff-filter=M`: NONE.** The source only ADDS paths.

**HOW THE EMPTINESS WAS ESTABLISHED, two ways and both recorded.**

**Structurally:** the fork point and `origin/main` resolve to the same commit,
`d9f676a4`, so there is no path at which `main` could carry a blob newer than
the fork's.

**Per path:** `git diff --name-only <fork> <origin/main>` returns an empty
listing. **The empty result is the measurement, not the absence of one.**

**No file was changed on both sides**, so Amendment P(b)'s line-survival
obligation does not arise; its non-arising is established by the emptiness of
the modified-path set rather than inferred from a clean merge. `A5` does not
fire.

### `C3` — every arriving path, blob-identical to its source blob (MEASURED)

Measured over the paths the merge brought in, by first-parent diff:

    derivations/P2-PROVENANCE-CENSUS-01_census.md       84d4c45787ed5a47…  IDENTICAL
    reports/2026-08-21T0308Z_provenance-census-01.md    9081d39cb6368eeb…  IDENTICAL
    reviews/chatgpt/2026-08-21T0308Z_provenance-…       e13d31a2b9f499e1…  IDENTICAL
    scripts/diagnostics/provenance_census_01.py         bccebc3b9e387153…  IDENTICAL
    specs/2026-08-21T0308Z_provenance-census-01.md      f6aaf64377a1f7ca…  IDENTICAL

### `M2` — validators, both sides, in real worktrees (MEASURED)

    merge product  83b00ed   332 passed, 2 deselected, exit 0
    base           d9f676a   332 passed, 2 deselected, exit 0

**The clone was unshallowed before running**, per `M2`: no `.git/shallow`
exists and 665 commits are reachable from all refs. **The shallow-clone
condition that produced six governance-test failures in an earlier session did
not recur, and its absence was measured rather than assumed.** `A3` does not
fire.

### `M6` — the governing clause (MEASURED)

`docs/BRANCHING_POLICY.md:25-40`, `## Science branch integration`: `--no-ff`
into a dedicated integration branch, squash/rebase prohibited; "During landing,
only the integration branch and `refs/heads/main` may be pushed"; "Source
branch, session branches and unrelated refs must not move"; "`main` advances
only by fast-forward from its reviewed evidence base to the completed
integration head." **No contradiction with §3. `A4` does not fire.**

### `M7` — two measurements, and they DIFFER (MEASURED)

    (a) base-relative              7 paths
    (b) the source's contribution  5 paths

**They differ, and the difference is exactly this task's own specification and
review** — `specs/2026-08-21T0503Z_provenance-census-integ.md` and
`reviews/chatgpt/2026-08-21T0503Z_provenance-census-integ.md`, both absent from
the source and both committed to the integration branch before the merge, as
Rule 15's order requires. **Recorded as two measurements that disagree for a
stated reason, not as one taken twice.**

### `M9` — the pins this task must not move (MEASURED)

    A-EXT-01   ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
    H-EXT-01   e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47

Identical at the source and at the base. Neither `CONVENTIONS.md` nor
`assumptions/H-EXT-01.md` appears in this task's changed-file set.

### `M10` — append-only, verified by byte prefix (MEASURED)

**At the merge product, NO file that declares itself append-only is modified**
— the merge only adds paths, established by the empty modified-path set of
`M4`.

**At the landing head, `DECISION_LOG.md` is modified by this task's §7
records**, and is verified:

    base blob, full content        117791 bytes
      sha256  f4d8fa6b90a4461ad81fdee11d3181bd12969322ccbeaa65d9eb4e5bf90c7c03
    first 117791 bytes of the new file
      sha256  f4d8fa6b90a4461ad81fdee11d3181bd12969322ccbeaa65d9eb4e5bf90c7c03
    new file                       123159 bytes

**The prefix is unchanged byte for byte**; the entry is an append.
