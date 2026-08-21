# P2-PROVENANCE-CENSUS-01 — What is cited, what is landed, and what is neither

    Status            SPECIFIED — not executable until Reviewer approval is committed (Rule 15)
    Author role       Researcher
    Executor          sole write-access holder
    Verifier          Researcher, from a clean clone, no git writes
    Kind              MEASUREMENT. No landing. No merge.

---

## 0. Binding SHA

    Evidence base (main at authorship)   d9f676a4b7d0a851c82177f8e14cba1af467b06f

If `main` has advanced when execution begins, execution does not proceed.

---

## 0a. Why this task exists, and why it produces no set of its own

Two specifications stopped because they carried a predeclared set of
adjudications and execution found the set incomplete. **The architecture agreed
afterwards separates discovery from action**: this task discovers, a later task
acts on what it froze.

**This specification therefore names no adjudication, lists no item, and
states no count.** Its product *is* the set. A specification that both
enumerates a set and requires it to be measured is the defect that stopped its
predecessors.

## 0b. What has already been found, and why the census is wider than expected

Three findings from executed tasks bear on how the matching must be done.
**They are stated as context, not as results to reproduce**; each is
re-established under §2 or not used.

    CITATION FORM       `PI ruling N` was found not to identify a unique
    IS NOT UNIQUE       ruling set. At least one landed artifact cites
                        numbered rulings that do not correspond to the items
                        of the document landed under that name.
                        **Matching by number alone is therefore unsound**, and
                        §3 requires matching on content.

    LABELS ARE NOT      A block labelled as reproducing what was ruled was
    EVIDENCE            measured and found not to. **A label asserting
                        faithfulness is not evidence of it**, and §3 requires
                        comparison rather than reliance on the label.

    A LANDED HOME IS    Rulings landed into a register other than `decisions/`
    NOT ONLY `decisions/`   have provenance. **"Not in `decisions/`" is not
                        the test**; §3 uses "has no authoritative landed
                        record anywhere governance admits".

## 0c. Non-objectives

This task does **not**:

1. land, register, place, or record any adjudication anywhere;
2. decide whether any citation, label or record should be amended;
3. resolve any discrepancy it finds — **it reports both sides**;
4. adjudicate whether the citation form should change, or propose a rule;
5. merge anything, or move `main`;
6. modify any file under `scripts/`, or any file at all outside its own
   artifacts;
7. carry any figure from a prior task's report.

## 0d. Authorised path manifest — defined once

    P1   the census artifact this task produces
    P2   any new script created solely for this census, under a diagnostic or
         analysis path, **each named in the report**. **No existing script may
         be modified.**
    P3   this task's own spec, review and report artifacts, wherever their
         authorised paths lie, including under specs/

`A5` and `C11` both refer to this manifest and neither restates it.

**Self-check on this specification**, against the defect classes this line has
produced:

    asserted count        no number in the prose is asserted rather than
                          measured
    unmeasured universal  no "sole", "only", "every", "no other" is asserted
                          rather than measured
    dangling reference    every `M`, `A`, `C` and `§` reference resolves
    predeclared set       **this specification's whole point**: no set is
                          enumerated anywhere in it
    contested control     no acceptance criterion covers a case an abort
                          condition covers
    self-referential      counts of this document's own enumerated content
    count                 are checked against that content

---

## 1. Scope, fixed by the PI

    SEARCHED      specs/  derivations/  decisions/  docs/
                  CONVENTIONS.md  GATES.md  DECISION_LOG.md

    NOT SEARCHED  reviews/  reports/

**The exclusion has a reason and it is recorded**: reviews and reports are
statements *about* artifacts, not sources the repository relies on. **This is
a scope decision, not a finding that nothing relevant is there**, and `§7`
registers what a wider scope might add.

The commit range is the repository as it stands at `§0`'s base. **No date
range is imposed**; a citation's age does not change whether it resolves.

---

## 2. Measurements

Nothing is carried, including from the reports that surfaced §0b.

    M1   **S_C — candidate mentions.** Enumerate every passage in the searched
         scope that cites, describes, or relies on an adjudication, ruling,
         PI decision, or ratified disposition. Record path, line, and the
         passage. **Search on more than one form**: numbered citations,
         named citations, and prose asserting that something was ruled,
         decided, agreed, or directed. Record the forms searched and the
         exclusions stated for each.

         **`S_C` is a candidate set, not an assertion that each member is an
         adjudication.**

    M2   **S_A — confirmed adjudications.** For each member of `S_C`,
         classify it. The classes are those §3 defines. Record the
         classification and the evidence for it, per member.

    M3   **S_P — those with authoritative landed provenance.** For each
         member of `S_A`, determine whether a landed record of the
         adjudication itself exists anywhere governance admits — **not only
         `decisions/`**. Record where, with line citations, or record that
         none exists.

         **Matching is on content, not on number or name**, per §0b. Where a
         numbered citation and a landed item share a number but not content,
         record that as a non-match and say so explicitly.

    M4   **S_missing = S_A − S_P.** Record it as a list, each member with its
         citing passages and the evidence that no landed record was found.

    M5   **The label question.** For every block in the searched scope that
         asserts it reproduces what was ruled, compare it against the source
         the repository holds for that ruling, where one exists. Record:
         faithful, divergent with both texts, or no source available for
         comparison.

    M6   **The citation-form question.** Record how many distinct numbered
         adjudication sets are cited in the searched scope, how each is
         identified, and which citations resolve to which set. **Record any
         citation that resolves to none, or to more than one.**

    M7   Record the `Statement SHA` of `A-EXT-01` and `H-EXT-01`; confirm this
         task alters neither.

---

## 3. Classification, defined before the search

**A member of `S_C` belongs to `S_A` when the searched evidence supports that
the passage refers to a PI ruling or a PI-ratified Researcher disposition.**

**A landed authoritative record of that adjudication is NOT required for
membership in `S_A`.** Whether such a record exists is measured separately, by
`M3`.

    Evidence that an adjudication occurred   ->  decides S_A
    Evidence that it has landed provenance   ->  decides S_P

**These are different thresholds and merging them destroys the census.** If
`S_A` required a landed record, then `S_missing = S_A − S_P` could never have
a member, and a passage a landed specification relies on — "the PI has ruled
X", with no landed record of that ruling — would be excluded by construction.
**That case is exactly what this census exists to find.**

The classes:

    PI RULING               a question was put to the PI and the PI decided it
    RATIFIED DISPOSITION    a Researcher proposed it and the PI agreed
    EXECUTOR DISPOSITION    an executor decided it within its own authority
    RECOMMENDATION          a Reviewer or Researcher proposed it; no PI
                            agreement is evidenced
    DEPENDENCY DESCRIPTION  it describes the relation between adjudications
                            rather than deciding anything
    OPEN FINDING            it records that something is unsettled
    INDETERMINATE           the passage does not permit classification

**The first two are `S_A`. The rest are not.**

**A passage is not admitted to `S_A` merely because it uses words such as
"ruled", "decided", "agreed" or "directed".** Membership requires contextual
evidence that the passage refers to a PI ruling or a PI-ratified disposition —
what is decided, by whom, and on what occasion — not the presence of a verb.

**Whether an authoritative landed record of that adjudication exists is what
`M3` measures**, separately and afterwards. A member of `S_A` with no such
record is a member of `S_missing`, which is a result, not a classification
error.

**Where a passage cannot be classified, `INDETERMINATE` is recorded with the
reason.** It is not forced into a class, and it is not dropped.

---

## 4. Abort conditions

    A1   the base SHA observed differs from §0
    A2   the searched scope cannot be read
    A3   settling any classification would require an adjudication the
         executor is not authorised to make — **no**: that item is recorded
         `INDETERMINATE` per §3 and execution continues. This entry exists so
         a reader scanning aborts finds the answer here.
    A4   `main` moves during execution
    A5   a path outside the §0d manifest is modified

**`A3` is not an abort.** `A1`, `A2`, `A4` and `A5` stop execution.

---

## 5. Branch mechanics

    Branch       a new science/<scientific-task> branch
    Merge        NONE. `main` MUST NOT MOVE from `d9f676a4`.
    Push scope   this task's branch only.
    Prohibited   force-push; `--force-with-lease`; branch deletion; history
                 rewrite.

**Integration of this census is a separate specification.**

---

## 6. Required content of the census artifact

1. `S_C`, `S_A`, `S_P` and `S_missing` as explicit lists, each member with its
   evidence.
2. The classification of every `S_C` member, with the reason.
3. `M5`'s label comparison, per block.
4. `M6`'s citation-form finding, including any citation resolving to none or
   to several.
5. The forms searched and the exclusions stated, so the search is
   reproducible.
6. A statement of what the census does not establish, naming at minimum: that
   `S_missing` is a measurement over the searched scope and not over the
   repository; that a member of `S_missing` may have had authority whose
   record did not survive; and that no member's effective date is determined
   here.
7. Any question raised and not settled, recorded as open.

**The artifact recommends nothing.** `C6` fails on a recommendation.

---

## 7. Records the artifact carries, not registered elsewhere

**This task registers nothing** — it merges nothing, so it writes to no
register. The following are recorded *in the artifact* for a later task:

    the scope exclusion   what a search including `reviews/` and `reports/`
                          might add is unmeasured
    the citation form     whether the form should change is not decided
    the label practice    whether other labels hold is `M5`'s to report and
                          nobody's here to fix

---

## 8. Acceptance criteria

    C1   All four sets present as explicit lists, each member with evidence.
    C2   Every `S_C` member carries a classification from §3 and its reason.
    C3   `S_A ⊆ S_C` and `S_P ⊆ S_A` and `S_missing = S_A − S_P`, checked
         member by member, not asserted.
    C4   No member is placed in `S_A` merely because a passage uses words
         such as "ruled", "decided" or "agreed". Membership rests on the
         contextual evidence §3 requires. **`M3` evidence is NOT a condition
         of `S_A` membership** — a member with no landed record belongs in
         `S_A` and then in `S_missing`. Verified by reading the reasons.
    C5   `M5` and `M6` present in the forms §2 requires, including the
         "resolves to none or to several" cases if `M6` finds any.
    C6   The artifact contains no recommendation and no proposed rule.
         Verified by reading; **passes on absence**.
    C7   §6.6's statement of non-establishment present with all three of its
         named items.
    C8   `INDETERMINATE` members are recorded with reasons and are not
         dropped or forced.
    C9   The forms searched and their exclusions are recorded.
    C10  `M7`'s two Statement SHAs unchanged.
    C11  No path outside the §0d manifest is modified; `main` unmoved at
         `d9f676a4`; only this task's branch pushed.

---

## 9. Substring hazards

    ruling          PI rulings, the rule set, "ruled" as ordinary past tense,
                    and "ruling N" in two distinct namespaces — `M6`'s subject
    decision        `decisions/`, `DECISION_LOG.md`, "decided", and "decision
                    owner"
    adjudication    the act, the document, and the phrase inside unrelated
                    clauses
    agreed          PI agreement, and ordinary usage
    item            numbered items of a document, register items, list items
    verbatim        the label under examination, and ordinary usage

A check that cannot state its exclusions is performed by reading.

## 10. Criterion satisfiability

`C1` through `C5` are satisfiable whatever the sets contain, including empty.

`C6` is negative and satisfiable by reading for absence.

`C8` is satisfiable because §3 admits `INDETERMINATE` as a classification.

**No criterion is reachable in a case an abort condition covers**, and `A3`'s
non-abort status is stated in `A3`.

---

## 11. Post-execution verification (Researcher)

1. spot-check `S_C` for omission — **search independently with at least one
   form the executor did not use**, since a census's characteristic failure is
   a member never seen;
2. re-apply §3's classification to a sample of `S_A` and a sample of the
   classes excluded from it;
3. check `C4` specifically, and **in both directions** — that no member
   entered `S_A` on a verb alone, and that **no member was excluded from
   `S_A` for lacking a landed record**. The second is the failure the
   Reviewer caught in the draft: it would make `S_missing` empty by
   construction, and an empty `S_missing` reported as a finding rather than
   as an artefact of the threshold is the worst outcome this census can
   produce;
4. re-derive `C3`'s set relations;
5. read for anything barred by `C6`;
6. recompute `M7`'s digests;
7. confirm `C11` by `git ls-remote`;
8. anything unevaluable is recorded **INCONCLUSIVE**, with a subclass and a
   `Resolution path` per rule 22.

---

## 12. What this task does not establish

It produces no scientific result, no `β_V`, moves no gate, and
`P2-PHASE-01` is unchanged. It decides nothing about any adjudication it
finds, and it does not establish that any member of `S_missing` lacked
authority — **only that no landed record of it was found in the searched
scope.**

---

## 13. Next

1. **Integration of this census** — a separate specification.
2. **`P2-SESSION-RULINGS-02`** — over the set this census freezes, not over a
   predeclared one.
3. **`R-4`'s measurement**, then **`R-3`**, then the extraction protocol
   freeze.
