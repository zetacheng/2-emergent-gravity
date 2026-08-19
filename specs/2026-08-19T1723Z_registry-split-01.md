# P2-REGISTRY-SPLIT-01 — Assumptions and decisions get their own directories

    Status            SPECIFIED — not executable until Reviewer approval is committed (Rule 15)
    Author role       Researcher
    Executor          sole write-access holder
    Verifier          Researcher, from a clean clone, no git writes
    Origin            PI ruling of this session

---

## 0. Binding SHA

    Evidence base (main at authorship)   ff21836549d9f9e18deab172f1f3f8e02cf8064f

If `main` has advanced when execution begins, execution does not proceed and
the specification returns to the Researcher for re-issue.

**This specification transcribes a PI ruling.** Where the ruling cannot be
applied as given, that is an abort and a return to the PI, not an executor
edit.

---

## 1. The ruling, as given

1. `reviews/` holds **reviews of specifications only**.
2. Assumptions get their own directory.
3. PI decisions get their own directory.
4. An assumption's content and its review may live in **one file, as Part 1
   and Part 2**.
5. **PI decisions are also to be reviewed.**

## 1a. Non-objectives

This task does **not**:

1. rewrite, delete, or retrospectively re-file any historical record;
2. re-review any landed assumption, decision, or specification;
3. adjudicate `RECON-PROJ-01`, component 5, or component 9;
4. modify any file under `scripts/`;
5. change the exact statement of `A-EXT-01` or `H-EXT-01` — a statement edit
   would void their pinned reviews under the rule landed at `ff218365`.

## 1b. Authorised path manifest — defined once

    P1   the new assumptions directory and its contents
    P2   the new decisions directory and its contents
    P3   reviews/README.md
    P4   CONVENTIONS.md
    P5   DECISION_LOG.md
    P6   this task's own spec, review and report artifacts

`A5` and `C11` both refer to this manifest and neither restates it.

---

## 2. Measurements

Nothing is carried. Every value is measured at `ff218365`.

    M1   Read `reviews/README.md` and record the layout convention it fixes,
         the author directories it names, and the `Function:` header rule.
    M2   Record the contents of `reviews/pi/` — file names and what each
         record is by its own header.
    M3   Locate the assumption-review artifact landed under `reviews/chatgpt/`
         for `A-EXT-01` / `H-EXT-01` and record its path and digest.
    M4   Record where `A-EXT-01` and `H-EXT-01` currently live, and the
         `Review SHA` each pins together with what those digests are taken
         over.
    M5   Read `CONVENTIONS.md`'s append-only and forbidden-delete rule and
         record, for each of `DECISION_LOG.md` and `CONVENTIONS.md`, whether
         removing an existing entry from it is permitted.
    M6   Test suite on the merge product and at `ff218365`, in real git
         worktrees.
    M7   `git diff --name-only ff218365..<merge product>`.
    M8   Determine, by recomputing, whether each pinned digest recorded in
         `M4` is taken over the exact-statement bytes ALONE, excluding the
         surrounding field labels. Record the recomputation and the result.
         **This governs whether §5.1a's rename may proceed.**

---

## 3. Abort conditions

    A1   the base SHA observed differs from §0
    A2   the ruling of §1 cannot be applied as given — for example if `M5`
         shows a required relocation would violate append-only. Return to the
         PI; the executor does not choose a workaround.
    A3   `M6` shows a failure not also present at `ff218365`
    A4   the merge is not conflict-free
    A5   a path outside the §1b manifest appears in `M7`

---

## 4. Merge mechanics

Governed by the `science/*` integration clause of `docs/BRANCHING_POLICY.md`,
located and recorded before use. `--no-ff` into a dedicated integration
branch; `main` advances by fast-forward only; push scope is the integration
branch and `refs/heads/main` and no other ref.

---

## 5. What is created

### 5.1 `assumptions/`

Holds **physical assumptions and physical hypotheses** — propositions that
could in principle be established or refuted. **It does not hold definitional
conventions.** Those are the Convention Registry's, and the separation is the
one landed at `ff218365`: a definition is not a falsifiable proposition, and
filing it among assumptions would undo that distinction three days after
making it.

The four-way separation this task establishes:

    CONVENTIONS.md    definitions and conventions
    assumptions/      falsifiable or unestablished scientific propositions
    decisions/        PI rulings
    reviews/          reviews of specifications

One file per entry, structured:

    PART 1 — THE ENTRY
             the schema landed at ff218365, with the SHA field split as
             below:
             ID / Type / Status / Exact statement / Scope /
             What depends on it / What does NOT depend on it / Evidence /
             Falsifier or resolution condition / Review /
             Statement SHA / Review Artifact SHA / Date / Supersedes

    PART 2 — THE REVIEW
             the independent review of Part 1, carrying a `Function:` header,
             naming its author, and stating which parts of Part 1 it accepted,
             required to be changed, and did not address.

### 5.1a The SHA fields, disambiguated

The field landed at `ff218365` as `Review SHA` in fact carries the digest of
the exact-statement bytes. The name says review; the content is a statement
binding. Left as is, the next executor asks the same question this one
already had to return.

    Statement SHA          SHA-256 of the exact-statement bytes.
                           THIS IS THE BINDING PIN.
    Review Artifact SHA    SHA-256 identifying the review artifact.
                           Provenance, not a pin.

Landed with the schema:

> **Editing the exact statement invalidates the attached review and requires
> re-review.** Editing Part 2, the field labels, or any other field does not.

This is why the pin is over the statement and not over the file: with Part 1
and Part 2 in one file, a file digest would break on every review edit and
survive nothing that matters.

**The rename is applied to the two entries landed at `ff218365`.** It changes
field labels only. `M8` establishes, before the rename, that the pinned digest
is taken over the statement blockquote alone and not over the labels, and
`C9` re-verifies both digests afterwards. If `M8` shows otherwise, the rename
is not performed and the item returns to the Researcher.

### 5.2 `decisions/`

Holds PI decisions, each as **one file per decision**, structured:

    PART 1 — THE DECISION   what was decided, by whom, on what date, its
                            effect, and its scope
    PART 2 — THE REVIEW     the independent review of Part 1

### 5.3 Review of PI decisions — mechanism, PROVISIONAL

`§1.5` requires PI decisions to be reviewed. **It does not say when a PI
decision takes effect, and that question is a governance authority matter, not
an implementation detail.** The Researcher does not have authority to fix it.

The following is therefore landed **explicitly as a PROVISIONAL
execution-layer disposition, reversible by PI adjudication, and NOT as a
permanent repository rule.** It is recorded so that the directory can be used
before the question is formally settled, and §12.2 registers the adjudication
as owed.

> **PROVISIONAL.** A review of a PI decision is recorded, not gating. The
> decision takes effect when the PI issues it. The review is an independent
> assessment landed in Part 2, and its function is to surface consequences,
> conflicts with landed records, and ambiguities — which may prompt the PI to
> revise or supersede the decision. **A review does not withhold effect from a
> PI decision**, because a gating review would place the Reviewer above the
> PI, inverting the authority model in `AGENTS.md`.

A decision whose Part 2 is not yet written is recorded with Part 2 marked
`REVIEW PENDING`, and the decision is in effect meanwhile.

**The `decisions/` README states that this disposition is provisional and
names the pending adjudication.** A reader must not be able to mistake it for
a settled rule.

### 5.4 Each directory carries a README

Stating what the directory holds, what it does not hold, the Part 1 / Part 2
structure, and — for `assumptions/` — the pin rule of §5.1.

---

## 6. What moves, and what does not

`M5` governs. **No relocation is performed that the append-only rule
forbids.**

    R-1   The A-EXT-01 / H-EXT-01 assumption review currently under
          reviews/chatgpt/ is the review of an assumption, not of a
          specification, so §1.1 excludes it from reviews/.
          It is reproduced as PART 2 of the corresponding assumptions/ file.
          **Whether the reviews/chatgpt/ copy is removed or left in place with
          a pointer is determined by M5**, not chosen here.

    R-2   H-EXT-01's canonical location becomes assumptions/.
          Its DECISION_LOG.md entry is append-only and is NOT deleted.
          A new appended entry records the relocation and names the new
          canonical location. The original entry stands as historical record.

    R-3   A-EXT-01 REMAINS CANONICAL IN CONVENTIONS.md, and no stub entry is
          created for it in assumptions/.
          Ground: §5.1 scopes assumptions/ to falsifiable or unestablished
          propositions. A-EXT-01's Type is DEFINITIONAL CONVENTION,
          CONVENTIONS.md:1 names itself the Convention Registry, and the
          placement was reviewed and approved at ff218365. A stub would have
          re-admitted a definition into the assumptions taxonomy the previous
          landing was written to keep it out of.
          **assumptions/README.md cross-references CONVENTIONS.md** so a
          reader looking for the A-EXT-01 / H-EXT-01 pair finds both, and
          H-EXT-01's own entry names A-EXT-01 in its Scope and Evidence
          fields as it already does.

    R-4   reviews/pi/'s three existing records are historical.
          They are NOT moved, NOT rewritten, and NOT re-reviewed.
          reviews/README.md records that PI decisions are filed under
          decisions/ going forward and that these three remain valid
          historical evidence in place — the same treatment the README
          already gives records predating the Function: header.

    R-5   reviews/README.md is amended to state that reviews/ holds reviews
          of specifications, that assumption reviews live in assumptions/ as
          Part 2, and that PI decisions live in decisions/. The by-author
          layout and the Function: header rule are unchanged for what remains.

---

## 7. Acceptance criteria

    C1   assumptions/ exists with a README stating the Part 1 / Part 2
         structure, the four-way separation of §5.1, the pin rule of §5.1a,
         and a cross-reference to CONVENTIONS.md for definitional entries.
         The README must NOT state that assumptions/ holds definitional
         conventions.
    C2   decisions/ exists with a README stating the Part 1 / Part 2
         structure and the §5.3 disposition, labelled PROVISIONAL and naming
         the pending adjudication. Verified by reading.
    C3   H-EXT-01 exists in assumptions/ with the full field set of §5.1,
         including both `Statement SHA` and `Review Artifact SHA`, and its
         exact statement byte-identical to the statement landed at ff218365.
         Verified by digest against M4's recorded pin.
    C4   The A-EXT-01 / H-EXT-01 review appears as PART 2 of the H-EXT-01
         file, and is identified as an assumption review with a Function:
         header.
    C5   DECISION_LOG.md's original H-EXT-01 entry is unchanged, and a new
         appended entry records the relocation. Append-only verified by byte
         prefix.
    C6   assumptions/ carries NO A-EXT-01 entry or stub. CONVENTIONS.md's
         A-EXT-01 entry is unchanged except for the §5.1a field rename, and
         its exact statement verifies against M4's pin.
    C7   reviews/README.md carries the §6 R-5 amendment; the three
         reviews/pi/ records are unchanged.
    C8   §5.3's disposition is landed and identified as PROVISIONAL and
         reversible by PI adjudication — not as a settled repository rule and
         not as a rule the Researcher has authority to fix.
    C9   No exact statement of any landed entry is altered. Both digests
         recorded in M4 re-verify after the §5.1a rename. If M8 found the
         pinned digest covers field labels, the rename was not performed and
         that is recorded instead.
    C10  M6 recorded for both sides; M7 recorded.
    C11  M7 lists no path outside the §1b manifest.
    C12  Refs pushed are exactly the integration branch and refs/heads/main.

---

## 8. Substring hazards

    review          matches reviews/, review SHA, pre-execution review, and
                    assumption review; four different objects
    decision        matches DECISION_LOG.md, decisions/, and "decision owner"
    assumption      matches "locked assumptions" in gate text, a different
                    register
    Part 1 / Part 2 the assumptions and decisions files both use these labels;
                    state which file is meant at each use

A check that cannot state its exclusions is performed by reading.

## 9. Criterion satisfiability

`C3`, `C6` and `C9` are digest comparisons against values `M4` records before
any change is made; both sides of each comparison exist before the check runs.

`C8` requires a label to be present, which §5.3 supplies as required content;
it does not require the executor to discover a disposition.

---

## 10. Post-execution verification (Researcher)

1. digest `A-EXT-01`'s and `H-EXT-01`'s exact statements and compare against
   the pins recorded at `ff218365`;
2. confirm `DECISION_LOG.md` append-only by byte prefix;
3. read both READMEs against §5.1–5.4;
4. confirm the three `reviews/pi/` records are byte-identical;
5. confirm `C12` by `git ls-remote`;
6. anything unevaluable is recorded **INCONCLUSIVE**, not PASS.

---

## 11. What this task does not establish

A directory layout is not a scientific result. This produces no `β_V`, moves
no gate, and does not advance `P2-PHASE-01`. What it changes is that a reader
can tell a definition from a hypothesis from a decision from a specification
review by where the file sits, and that every one of them carries its review
with it.

---

## 12. Returned to the PI, not decided here

1. **Whether `assumptions/` should hold definitional conventions too.** `R-3`
   keeps `A-EXT-01` canonical in the Convention Registry and creates no stub,
   on the ground that `§5.1` scopes `assumptions/` to falsifiable
   propositions. If the intent is otherwise, `A-EXT-01` moves and
   `CONVENTIONS.md` carries the pointer.
2. **When a PI decision takes effect, and whether its review is ever
   gating.** `§5.3` adopts non-gating PROVISIONALLY, on the ground that a
   gating review would invert the authority model. **This is a governance
   authority question and is owed a formal PI ruling**; the disposition is a
   stopgap so the directory is usable, not an answer. Suggested ruling text
   for the PI to accept, amend or reject: *PI decisions take effect when
   issued; their reviews are mandatory but non-gating; a review may identify
   defects and recommend revision or supersession, but does not suspend the
   decision unless the PI so rules.*
3. **Whether the three historical `reviews/pi/` records should be reviewed
   retrospectively.** `R-4` leaves them as historical evidence, consistent
   with the README's existing treatment of pre-header records.
