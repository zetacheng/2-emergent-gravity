# Execution report — `P2-REGISTRY-SPLIT-01`

    OUTCOME     MERGED AND LANDED. No abort fired.
                assumptions/ and decisions/ created; H-EXT-01 relocated by
                cross-reference with its original entry untouched;
                A-EXT-01 left canonical in the Convention Registry;
                the SHA field split applied and both pins re-verified.

**Specification:** `specs/2026-08-19T1723Z_registry-split-01.md`
**Review:** `reviews/chatgpt/2026-08-19T1723Z_registry-split-01.md`
**Base:** `ff21836549d9f9e18deab172f1f3f8e02cf8064f`

**Measurement head: the merge product,
`da8ce590cafcdd6d1fde893f9778d0b4307f7e45`.** `C12` is INTENDED and measured
in the post-report layer.

---

## §0 — Binding SHA (MEASURED, no A1 abort)

    observed origin/main   ff21836549d9f9e18deab172f1f3f8e02cf8064f
    §0 declared base       ff21836549d9f9e18deab172f1f3f8e02cf8064f

**Equal.**

**Review binding (Rule 18, Amendment N).** Field present, once, populated —
checked before its value.

    sha256 of the specification bytes as committed
      6a90c815d4e1912c431e827e0887eb723f2d6bde507782e6245238ad94a49bad
    the review's bound SHA
      6a90c815d4e1912c431e827e0887eb723f2d6bde507782e6245238ad94a49bad

**MATCH.** Verdict `APPROVE FOR EXECUTION`.

---

## Environment (MEASURED)

**Amendment D step 0.** Ref reads in `/home/user/2-emergent-gravity`; work in
the linked worktrees `…/scratchpad/rsplit` (task branch) and
`…/scratchpad/irsplit` (integration branch), both created at the base; the
`M6` comparison in a detached worktree at `ff218365`, removed after.

**Rule 13's diagnostic order.** Not shallow; 423 commits on HEAD, 588 across
all refs; Python 3.11.15; pytest 9.1.1; numpy 2.4.6; sympy 1.14.0; ruff 0.15.8;
**`scipy` ABSENT.** **No environment failure occurred, so neither of Rule 13's
two diagnostic orders was exercised.**

---

## §2 — Measurements

### M1 — `reviews/README.md`'s layout convention

**Layout fixed as by-author.** `:3` — *"Store independent review records here,
organised by author directory"*. **Author directories named:** `chatgpt/`,
`claude/`, `codex/`, `pi/`.

**`Function:` header rule**, `:11-17`: because the Researcher and Reviewer
functions are exchanged by PI instruction, the author directory alone does not
say in which function a record was produced, so every record created or
substantively amended after the 2026-08-06 role-model decision must carry

    Function: Researcher | Reviewer | Executor | PI authorization

**Records predating the requirement remain valid historical evidence** and are
not retrospectively non-conforming. **That treatment is the precedent `R-4`
applies to `reviews/pi/`.**

### M2 — `reviews/pi/`, and what each record is by its own header

    2026-08-03-governance-tools-environment-authorization.md
      "# PI authorization record — governance-tools validator environment"
    2026-08-03-outcome-based-task-specification-amendment.md
      "# Amendment to CONVENTIONS.md — role separation and outcome-based task
       specification"; its own status line calls it the RATIONALE RECORD for
       an adoption
    2026-08-03-p2-dual-pipeline-probe-repin.md
      "# PI amendment record — geometry-response probe re-pin (LANDING-ROUTED)"

**Three records. One authorization, one rationale record, one amendment
record.** **None is a review of a specification**, which is why `§1.1` would
exclude them from `reviews/` prospectively — and why `R-4` leaves them in place
rather than moving them.

### M3 — the assumption-review artifact

    path    reviews/chatgpt/2026-08-19T1141Z_assumption-review_a-ext-01_h-ext-01.md
    sha256  e641d4877a15975f224e57320b7e28dcbcd5850fcfecdc8e95a7f716650a0953
    blob    2f5fc0e29c4f83e7905bf3c242e52f55ef36c2b4

### M4 — where the two entries live, and what their pins are taken over

    A-EXT-01   CONVENTIONS.md, section "### `A-EXT-01`" at :65
               Review SHA  ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
               annotated in place as "the digest of the exact statement bytes
               above"

    H-EXT-01   DECISION_LOG.md, entry "## 2026-08-19 — Physical hypothesis
               `H-EXT-01`", its Review SHA field at :2290-2291
               Review SHA  e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47
               annotated as "the digest of the exact statement bytes above"

**Both fields are named `Review SHA` and both are annotated as covering the
statement.** That is the mismatch `§5.1a` exists to fix.

### M5 — append-only, and what may be removed

**`DECISION_LOG.md` — removal NOT permitted.** Its own `:3-4`: *"This log is
append-only. New decisions must use the entry template below and must not erase
superseded decisions."* **Measured across landed specifications: `DECISION_LOG.md`
is declared `append_only` 82 times, and it is the only path ever so
declared.**

**`CONVENTIONS.md` — removal is not flatly forbidden, and it is not free.**
It **does not declare itself append-only** — a search for such a declaration
returns 0 — and has never been declared `append_only` in any landed
specification. Its `## Change control` at `:153-156` requires that any change
to a *locked convention* after a gate has been committed be recorded as a
superseding `DECISION_LOG.md` entry and trigger re-examination of every gate
that consumed it, and states that *"Conventions are never changed silently"*.

`CONVENTIONS.md:332-340` supplies the evaluation rule for both — append-only
and forbidden-delete are evaluated against the last pushed state of the branch
as well as against the evidence base.

**Consequence for this task.** **Nothing is removed from either file.**
`DECISION_LOG.md` is appended to only. `CONVENTIONS.md` receives a field-label
rename inside a section landed three days ago; **that is not a change to a
locked convention** — the locked-conventions table is untouched — **and the
statement it annotates is byte-identical.**

**Consequence for `R-1`.** The assumption review under `reviews/chatgpt/` is
covered by neither rule. **It is left in place, and that is determined and not
chosen:** `§1a.1` forbids this task from deleting any historical record, and
that artifact is one. It is reproduced as Part 2 of `assumptions/H-EXT-01.md`,
which names it as the landed original and pins its digest.

### M6 — test suite

    invocation   python3 -m pytest -q
    merge product da8ce590   332 passed, 2 deselected in 45.99s, exit 0
    base ff218365            332 passed, 2 deselected in 46.97s, exit 0

**Identical. No A3 abort.** Both in real git worktrees; the base run was taken
in a worktree checked out at `ff218365` itself.

### M7 — `git diff --name-only ff218365..da8ce590`

    CONVENTIONS.md
    DECISION_LOG.md
    assumptions/H-EXT-01.md
    assumptions/README.md
    decisions/README.md
    reviews/README.md
    reviews/chatgpt/2026-08-19T1723Z_registry-split-01.md
    specs/2026-08-19T1723Z_registry-split-01.md

**Eight paths, all inside the §1b manifest. No A5 abort.** P1 `assumptions/`,
P2 `decisions/`, P3 `reviews/README.md`, P4 `CONVENTIONS.md`, P5
`DECISION_LOG.md`, P6 the spec and review — and this report joins as P6.
**Zero paths under `scripts/`.**

### M8 — what the pinned digests actually cover — **the measurement that governs §5.1a**

**Recomputed before any change was made, by extracting each entry's exact
statement blockquote alone and hashing it.**

    A-EXT-01   statement extracted from CONVENTIONS.md: 7 lines, 469 bytes
               recomputed  ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
               pinned      ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
               MATCH

    H-EXT-01   statement extracted from DECISION_LOG.md: 2 lines, 143 bytes
               recomputed  e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47
               pinned      e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47
               MATCH

**Counter-check, so the match is not read as a coincidence of extent:** the
same statement with a field label prepended hashes to `15005396d99a92a7…`,
which does **not** match the pin.

**Both pins are taken over the exact-statement bytes ALONE, excluding the
surrounding field labels. The `§5.1a` rename may proceed**, and it was
performed.

---

## §5 and §6 — what was created and what moved

### `assumptions/`

`assumptions/README.md` states what the directory holds — physical assumptions
and physical hypotheses — and **that it does not hold definitional
conventions**, with the reason: a definition is not a falsifiable proposition,
and filing one there would undo a distinction the repository made deliberately.
It carries the four-way separation, the Part 1 / Part 2 structure, the pin rule
of `§5.1a`, and **a cross-reference to `CONVENTIONS.md`** so a reader looking
for the `A-EXT-01` / `H-EXT-01` pair finds both.

`assumptions/H-EXT-01.md` carries **Part 1**, the full field set with
`Statement SHA` and `Review Artifact SHA` as separate fields, and **Part 2**,
the review with a `Function: Reviewer` header, identified as an assumption
review and not a specification review.

### `decisions/`

`decisions/README.md` states the Part 1 / Part 2 structure and carries the
`§5.3` disposition **labelled PROVISIONAL, reversible by PI adjudication, and
explicitly not a permanent repository rule**, with the pending adjudication
named and the suggested ruling text reproduced. It records `REVIEW PENDING` as
the Part 2 state for a decision not yet reviewed, and that the decision is in
effect meanwhile.

**No decision file was created.** The specification requires none, `C2` asks
only for the directory and its README, and filing an existing PI record here
would be the retrospective re-filing `§1a.1` forbids. **The three `reviews/pi/`
records stay where they are and `decisions/README.md` says so.**

### What moved, and what did not

**`R-1`** — the assumption review is **left in place** and reproduced as Part 2.
Determined by `M5` and `§1a.1`, not chosen.

**`R-2`** — `H-EXT-01`'s canonical location is now `assumptions/H-EXT-01.md`.
**Its `DECISION_LOG.md` entry is unchanged** — verified byte-for-byte, 4512
bytes identical — and a new appended entry records the relocation and names the
new canonical location.

**`R-3`** — **`A-EXT-01` remains canonical in `CONVENTIONS.md` and no stub was
created.** `assumptions/` carries no `A-EXT-01` entry.

**`R-4`** — the three `reviews/pi/` records are **byte-identical**, verified by
blob id, not moved, not rewritten, not re-reviewed.

**`R-5`** — `reviews/README.md` carries a new section stating that `reviews/`
holds reviews of specifications, that assumption reviews live in `assumptions/`
as Part 2 and PI decisions in `decisions/`, that nothing already there is
moved, and that the by-author layout and `Function:` rule are unchanged for
what remains.

### The `§5.1a` rename, applied where it could be

**In `CONVENTIONS.md`:** the schema line, the binding-rule paragraph, and
`A-EXT-01`'s own two fields. **The one surviving occurrence of the string
`Review SHA` is at `:77`**, inside the sentence explaining what the old label
was — deliberate, and the only place it should remain.

**In `assumptions/H-EXT-01.md`:** the canonical `H-EXT-01` entry is written
with the new labels from the start.

**NOT in `DECISION_LOG.md`.** Renaming a label inside the existing entry would
have edited an append-only file. **`R-2` makes that unnecessary rather than
forcing a conflict**: the canonical entry moves, the historical one stands as
landed. **No `A2` abort arose.**

---

## §7 — Acceptance criteria

    C1   PASS   assumptions/README.md states the Part 1 / Part 2 structure,
                the four-way separation, the pin rule, and the CONVENTIONS.md
                cross-reference. It states that the directory does NOT hold
                definitional conventions — verified by reading; it nowhere
                says it does.
    C2   PASS   decisions/README.md states the Part 1 / Part 2 structure and
                the §5.3 disposition, labelled PROVISIONAL in three places
                and naming the pending adjudication with its suggested ruling
                text. Verified by reading.
    C3   PASS   assumptions/H-EXT-01.md carries the full field set including
                both Statement SHA and Review Artifact SHA, and its exact
                statement is byte-identical to the one landed at ff218365 —
                2 lines, 143 bytes, digest
                e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47,
                matching M4's recorded pin.
    C4   PASS   The review appears as PART 2 of that file, headed
                "Function: Reviewer" and "Kind ASSUMPTION REVIEW of Part 1 of
                this file. NOT a specification review."
    C5   PASS   DECISION_LOG.md's original H-EXT-01 entry is byte-identical —
                4512 bytes, compared directly against the base blob — and a
                new appended entry records the relocation. Append-only
                verified by byte prefix: base 101986 bytes is a prefix of
                head 105456 bytes.
    C6   PASS   assumptions/ carries no A-EXT-01 entry or stub.
                CONVENTIONS.md's A-EXT-01 entry is unchanged except for the
                §5.1a field rename and the surrounding notes, and its exact
                statement verifies against M4's pin after the rename.
    C7   PASS   reviews/README.md carries the R-5 amendment; all three
                reviews/pi/ records are UNCHANGED by blob id.
    C8   PASS   §5.3's disposition is landed and identified as PROVISIONAL
                and reversible by PI adjudication, with an explicit statement
                that the Researcher does not have authority to fix the
                question and that a reader must not mistake it for a settled
                rule.
    C9   PASS   No exact statement was altered. Both digests re-verify on the
                merge product: A-EXT-01 ca8e5a87… and H-EXT-01 e5dd8a28…
                M8 found the pins cover the statement alone, so the rename
                proceeded.
    C10  PASS   M6 recorded for both sides; M7 recorded.
    C11  PASS   M7 lists eight paths, all inside the §1b manifest.
    C12  INTENDED — measured in the post-report layer.

---

## §8 — Substring hazards, and how each was handled

**`review` matches `reviews/`, `Review SHA`, `pre-execution review` and
`assumption review` — four different objects.** This one did real work: **`M2`
was answered by reading each `reviews/pi/` record's own header**, and the
answer is that none of the three is a review of a specification. A count of the
word would have said nothing. The `§5.1a` rename likewise was applied by
locating four specific blocks and replacing them, then reading back the one
surviving occurrence, rather than by a blanket substitution.

**`decision` matches `DECISION_LOG.md`, `decisions/` and `Decision owner`.**
The report and the landed text name the file, the directory, or the field
explicitly at each use; no check was performed by searching the bare word.

**`assumption` matches "locked assumptions" in gate text, a different
register** — 16 occurrences in `GATES.md`. **`M5` and the register reasoning
were done by reading the registers' own scope statements**, so `GATES.md` never
entered the question.

**`Part 1` / `Part 2` are used by both the assumptions and decisions files.**
Every use above names which file is meant.

---

## §1a — Non-objectives, all honoured

**Nothing historical was rewritten, deleted, or retrospectively re-filed** —
`DECISION_LOG.md` append-only verified by byte prefix, its H-EXT-01 entry
byte-identical, the three `reviews/pi/` records unchanged by blob id, and the
assumption review left in place. **Nothing was re-reviewed.**
**`RECON-PROJ-01`, component 5 and component 9 were not adjudicated.** **No
file under `scripts/` was modified** — zero `scripts/` paths in `M7`. **Neither
exact statement was changed**, and both pins verify.

---

## Stops and clarifications

**`SPECIFICATION_DEFECT`** — **none at STOP level.** The review notes one
non-blocking wording point at its `§185`, that broad prose about every
epistemic record "carrying its review with it" should be read in the context of
reviewed scientific propositions and decisions rather than as a claim about
every conventional definition. **The landed text does not make the broad
claim:** `CONVENTIONS.md`'s definitional section keeps the flat field-list form
it already had and is not given a Part 1 / Part 2 layout, and only
`assumptions/` and `decisions/` state that structure.

**Two provisions did real work.** `M8` is the reason the rename was safe to
perform: had the pins covered the field labels, renaming them would have broken
both, and the specification made that a measurement before an action rather
than an assumption. And `M5` is what decided `R-1` — the specification says the
outcome *is determined by `M5`*, not chosen, and it was.

**`ENVIRONMENT`** — `scipy` absent for the twentieth consecutive task; nothing
failed. **No environment failure occurred, so neither of Rule 13's two
diagnostic orders was exercised.**

**`OBSERVATION_METHOD_ERROR`** — **none reached the record. One harness fault,
caught immediately.** My first attempt at the `CONVENTIONS.md` rename asserted
against a schema block that did not match the file — I had reconstructed the
three-line field list from memory of its wrapping rather than reading it. **The
assertion fired before any write, so nothing was modified**, and the block was
re-read and replaced correctly. **That the edit script asserts each block's
uniqueness before substituting is why a wrong guess failed loudly instead of
silently matching nothing.**

**`REPOSITORY_DEFECT`** — **none found.** One observation, recorded and not
classified: **`CONVENTIONS.md` has never been declared `append_only` in any of
the 82 landed scope blocks that declare `DECISION_LOG.md`**, and does not
declare itself so. Its protection is the change-control rule, which binds
*changes to locked conventions* and is silent on removal of other material.
**Nothing here relies on that gap and nothing was removed**, but a reader
assuming the Convention Registry is append-only would be assuming something the
repository does not say.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`** — **three, all returned by
the specification and left as it left them.**

**One: whether `assumptions/` should hold definitional conventions too.** `R-3`
keeps `A-EXT-01` canonical in the Convention Registry and creates no stub, on
the ground that `§5.1` scopes `assumptions/` to falsifiable propositions.
**If the intent is otherwise, `A-EXT-01` moves and `CONVENTIONS.md` carries the
pointer** — a one-file change, and this report is the record that it was the
specification's ground and not the executor's preference.

**Two: when a PI decision takes effect, and whether its review is ever
gating.** Landed PROVISIONALLY as non-gating, with the ground stated — a gating
review would place the Reviewer above the PI — **and with the adjudication
named as owed in the directory's own README, so a reader meets it there and not
only here.**

**Three: whether the three historical `reviews/pi/` records should be reviewed
retrospectively.** `R-4` leaves them as historical evidence, consistent with the
README's existing treatment of pre-header records.

---

## Layering

**Everything above is measured at the merge product,
`da8ce590cafcdd6d1fde893f9778d0b4307f7e45`**, except `C12`, labelled INTENDED.

**Returned to the Reviewer in chat, not written back:** the `--is-ancestor`
verification and its exit status, the push exit statuses, the remote read-back,
and `C12` as measured.
