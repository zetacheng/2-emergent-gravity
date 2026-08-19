# Execution report — `P2-RECON-EXT-01-INTEG`

    OUTCOME     MERGED AND LANDED. No abort fired.
                A-EXT-01 registered as a definitional convention in the
                Convention Registry; H-EXT-01 as a physical hypothesis in
                the Decision Log; the assumption review landed as its own
                artifact and pinned by statement digest.

**Specification:** `specs/2026-08-19T1141Z_integrate-recon-ext-01.md`
**Review:** `reviews/chatgpt/2026-08-19T1141Z_integrate-recon-ext-01.md`
**Landing record:** `reports/2026-08-19T1141Z_integrate-recon-ext-01_landing-record.md`
**Assumption review:** `reviews/chatgpt/2026-08-19T1141Z_assumption-review_a-ext-01_h-ext-01.md`
**Base:** `968e726a5a4322eecf4254ff69b25832f263c155`
**Source:** `science/recon-ext-01-discarded-space @ 70f0e257b9afcd9f97445c5c2c62530fa742321e`

**Measurement head: commit 5, `5fefd84e26edf2f74ae2b50ea6e3fc06adb0b9f2`.**
`C1` and `C10` are labelled INTENDED and measured in the post-report layer.

---

## §0 — Binding SHAs (MEASURED, no A1 abort)

    observed origin/main       968e726a5a4322eecf4254ff69b25832f263c155
    §0 declared base           968e726a5a4322eecf4254ff69b25832f263c155
    observed source tip        70f0e257b9afcd9f97445c5c2c62530fa742321e
    §0 declared source         70f0e257b9afcd9f97445c5c2c62530fa742321e

**Both match.**

**Review binding (Rule 18, Amendment N).** Field present, once, populated —
checked before its value.

    sha256 of the specification bytes as committed
      ac0ec0b59e96094bf285d7d1c2e2ebe0528ab425ceb46699c783ee3c0cda4697
    the review's bound SHA
      ac0ec0b59e96094bf285d7d1c2e2ebe0528ab425ceb46699c783ee3c0cda4697

**MATCH.** Verdict `APPROVE FOR EXECUTION`.

---

## Environment (MEASURED)

**Amendment D step 0.** Ref reads in `/home/user/2-emergent-gravity`; commits
in the linked worktree `…/scratchpad/irext`, created at the base; the `M1`
comparison run in a detached worktree created at `968e726a` and removed after.

**Rule 13's diagnostic order.** Not shallow; 423 commits on HEAD, 582 across
all refs; Python 3.11.15; pytest 9.1.1; numpy 2.4.6; sympy 1.14.0; ruff 0.15.8;
**`scipy` ABSENT.** **No environment failure occurred, so neither of Rule 13's
two diagnostic orders was exercised.**

---

## §2 — Pre-execution measurements

**M1 — test suite.**

    invocation   python3 -m pytest -q

    merge product 45e7b904   332 passed, 2 deselected in 48.09s, exit 0
    base 968e726a            332 passed, 2 deselected in 45.03s, exit 0

**Identical. No A3 abort.** Both in real git worktrees, confirmed by
`git rev-parse --is-inside-work-tree` before the run. **The base comparison was
re-taken in a worktree checked out at `968e726a` itself** after a first attempt
used a worktree that was at a branch head rather than the base — the figures
happened to agree, but the run was repeated at the correct commit rather than
accepted.

**M2 — ancestry before the merge.** `git merge-base --is-ancestor 70f0e257
origin/main` → **exit 1**. Not an ancestor; the branch was unlanded.

**M3 — dry-run merge.** `git merge-tree --write-tree` exit 0, tree
`c042bda99b3718cfdcbedda13214c01624be284b`, **conflict lines 0. No A2 abort.**

**M4 — `git diff --name-only 968e726a..<head>`**, measured at commit 5:

    CONVENTIONS.md
    DECISION_LOG.md
    derivations/P2-RECON-EXT-01_discarded-external-space.md
    reports/2026-08-19T0649Z_recon-ext-01-discarded-space.md
    reports/2026-08-19T1141Z_integrate-recon-ext-01_landing-record.md
    reviews/chatgpt/2026-08-19T0649Z_recon-ext-01-discarded-space.md
    reviews/chatgpt/2026-08-19T1141Z_assumption-review_a-ext-01_h-ext-01.md
    reviews/chatgpt/2026-08-19T1141Z_integrate-recon-ext-01.md
    scripts/diagnostics/ext01_discarded_external_space.py
    specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md
    specs/2026-08-19T1141Z_integrate-recon-ext-01.md

**Eleven paths, all inside the §1b manifest. No A5 abort. C9 passes.**
`CONVENTIONS.md` and `DECISION_LOG.md` are P1/P2, the register files `M6`
selected. The assumption review is P1. The `1141Z` spec, review, landing record
and this report are P3. The four `0649Z` paths and the diagnostic script are
P4, arriving with the merge.

**M5 — the `science/*` clause**, located at `docs/BRANCHING_POLICY.md:25-40`.
Merge mode `--no-ff` into a dedicated integration branch, squash and rebase
prohibited; allowed-ref scope the integration branch and `refs/heads/main`,
source and session branches must not move; `main` advances by fast-forward
only. **This matches §4's shape in every particular. No A4 abort.**

**M7 — the two robust ratios, recomputed from the landed coefficients.**

    |sum discarded| / |sum retained|    recomputed 0.297300   reported 0.297300
    max|discarded| / mean|retained|     recomputed 1.008193   reported 1.008193

**Both reproduce. No A6 abort.** The recomputation parsed the ten coefficients
out of the landed table and summed them; it did not read the reported ratios
and derive from them.

---

## M6 — register selection, read

**Seven candidates were read. The classes land in different registers, which
`M6` anticipated.**

**A DEFINITIONAL CONVENTION → `CONVENTIONS.md`.** Its `:1` names it *"Convention
Registry"*. §5.0 of the specification directs a definitional entry to a
conventions or definitions register in preference to an assumption register,
and this is that register.

**A PHYSICAL HYPOTHESIS → `DECISION_LOG.md`.** A hypothesis is not a
convention, so the Convention Registry does not admit it. `DECISION_LOG.md`
already records open items as `UNESTABLISHED` — the precedent at its `:1326`,
*"Open derivation item: generator-sum criticality is UNESTABLISHED"*, and the
`POLE` construction entry landed earlier today.

**The §6 dispositions and open findings → `DECISION_LOG.md`.** `D-1` to `D-3`
are dispositions, and this is the decision log; `O-1` and `O-2` are open
findings, which the same log carries in the `UNESTABLISHED` form.

**The registers that do not admit them, with their own stated scopes:**

    derivations/P2-DEFERRED-ITEMS.md
      :12-17  holds work "CONSIDERED and consciously postponed", not open
              questions; :191 entries are added by PI decision
    derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md
      :3-5    scoped to the C1-C3 follow-ups of the C-check line
    derivations/P2-PHASE-01_input_admissibility_contract.md   (OPEN-AC-*)
      the P2-PHASE-01 admissibility standard
    derivations/P2-PHASE-01_microscopic_parameter_domain.md   (OPEN-PD-*)
      the P2-PHASE-01 parameter domain
    docs/GOVERNANCE-DEBT.md
      :3-6    records what rules, amendments and task reports already carry;
              governance debt, not scientific definitions or hypotheses
    CLAIMS.md
      :3-4    allowed statuses are PROPOSED, SUPPORTED, VERIFIED, FAILED,
              RETIRED, CONDITIONAL, INCONCLUSIVE. **UNESTABLISHED is not
              among them**, and :11 defines PROPOSED as "quantities not
              computed" — H-EXT-01 is not a quantity. The vocabulary does not
              admit it.

**No register semantics were coined and no new register was created.**

---

## §5 — What was registered

**`A-EXT-01`** in a new `## Definitional conventions with a recorded schema`
section of `CONVENTIONS.md`, with the full thirteen-field schema, its exact
statement verbatim, `Type: DEFINITIONAL CONVENTION`, `Status: ADOPTED for the
RECON line`, and **no falsifier** — the field records instead what would change
its scope.

**The locked-conventions table is unchanged.** The new section states this in
its own text, and `A-EXT-01`'s `Supersedes` field states specifically that it
does not supersede the table's `Definition of Z(m²)` row at `:20`, which
defines `Z` as the induced axis/TT graviton kinetic coefficient. **The two are
consistent:** the table says what `Z` is; `A-EXT-01` names the extracted
quantity `Z_axis-TT` and records that identifying it with the full physical
response is not established.

**`H-EXT-01`** as a dated `DECISION_LOG.md` entry with the same schema,
`Type: PHYSICAL HYPOTHESIS`, `Status: UNESTABLISHED — NOT ASSUMED BY
RECON-01b`, and a falsifier stated in both directions.

**§5.3's distinction and its provenance** land in `CONVENTIONS.md` alongside
`A-EXT-01`, including the statement that a definition is not falsifiable, the
identification of `H-EXT-01` as the falsifiable proposition, and the record
that the Researcher's earlier draft made a type error which an assumption
review corrected.

**§5.5's claim restriction** lands with them, carrying both prohibitions.

---

## §5.4 — the assumption review, and one thing about it stated plainly

**Landed as its own artifact** at
`reviews/chatgpt/2026-08-19T1141Z_assumption-review_a-ext-01_h-ext-01.md`,
headed `Function: Reviewer` per `reviews/README.md`, and identified in its own
first block as an **assumption review** and **not** a specification review.

**The executor received no free-standing assumption-review document.** The
Reviewer's assessment of these two statements was delivered inside the
pre-execution review of this integration specification. **The artifact says so
in its §0**, quotes that review verbatim with its own section numbers, and
states which sentences the executor wrote — the framing and the digests — and
which are the Reviewer's. **Nothing is attributed to the Reviewer that the
Reviewer did not write.**

**Path decision, and the tension it resolves.** §5.4 asks for *"a reviews path
for assumption reviews, distinct from the specification-review path"*.
`reviews/README.md` fixes the layout as **by author directory**
(`chatgpt/`, `claude/`, `codex/`, `pi/`) with a `Function:` header. **A new
top-level `reviews/assumptions/` directory would contradict that landed
convention.** The artifact is therefore a distinct file with a name that says
what it is, inside the author directory the convention requires — distinct from
the specification-review path, without inventing a layout that competes with
one already landed. **Whether a by-kind directory is wanted is returned as a
question**, not decided here.

**The `Review SHA` fields pin the exact statement bytes, not the artifact.**
That is the reading the binding rule requires: *"binds to the exact bytes
reviewed… if an entry's statement is later edited, the pinned review no longer
applies."* A digest over the artifact would not break when a statement is
edited; a digest over the statement does. **The artifact's own digest is
recorded too, in both entries, so either reading is served.**

    A-EXT-01 statement   ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
    H-EXT-01 statement   e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47
    review artifact      e641d4877a15975f224e57320b7e28dcbcd5850fcfecdc8e95a7f716650a0953

**Both statement digests were re-verified against the landed bytes after
landing** — extracted from `CONVENTIONS.md` and `DECISION_LOG.md` by reading
the blockquote runs — and both match.

---

## §7 — Acceptance criteria

    C1   INTENDED — post-landing.
    C2   PASS   A-EXT-01 and H-EXT-01 exist as two separate entries in two
                different files, each carrying its §5.1 / §5.2 text verbatim
                and the full §5.0 field set. Type distinguishes DEFINITIONAL
                CONVENTION from PHYSICAL HYPOTHESIS, and H-EXT-01 carries
                "NOT ASSUMED BY RECON-01b" in its Status line. Verified by
                reading both entries; neither states the other's content.
    C3   PASS   §5.3's distinction is present in CONVENTIONS.md, including
                "A definition is not a falsifiable proposition" and the
                identification of H-EXT-01 as the falsifiable one.
    C4   PASS   The provenance statement is present, recording the
                Researcher's weaker single-entry draft, naming it a type
                error, and recording that the review corrected it.
    C5   PASS   The assumption review is its own artifact, identified as an
                assumption review and not a specification review, with
                Function: Reviewer. Each entry's Review SHA pins the exact
                statement bytes, verified after landing. The §5.4 binding
                rule is landed with the schema in CONVENTIONS.md.
    C6   PASS   §5.5's claim restriction is present with both prohibitions —
                not stated as having reconstructed the full gravitational Z,
                and not cited as evidence for vanishing spin-1/0 residues.
    C7   PASS   D-1, D-2, D-3, O-1, O-2 all exist in one dated DECISION_LOG
                entry, each identified as an execution-layer disposition or
                an open finding. The register's identifier sequence is its
                dated headings; the entry states that D-1 to D-3 and O-1, O-2
                are the specification's labels and that the dated heading is
                this register's identifier for them.
    C8   PASS   M7's recomputed ratios are recorded beside the reported ones,
                in this report and in the landing record. Both reproduce.
    C9   PASS   M4 lists eleven paths, all inside the §1b manifest.
    C10  INTENDED — post-landing.
    C11  PASS   No existing blob under scripts/ is modified: 62 files at the
                base, 63 at the head, MODIFIED existing NONE, REMOVED NONE,
                and the one addition is the diagnostic arriving with the
                merge. scripts/recon2026/ ids recorded below.

### C11 — `scripts/recon2026/` blob ids observed

    scripts/recon2026/proca_curved.py      03f46905e5798fb7f6880dfae9ed5a1931be895b
    scripts/recon2026/flat_validation.py   6b21f9d6db67641ec7de31b7006884b617de3e8c

**Identical at `968e726a` and at commit 5.**

---

## §8 — Substring hazards, and how each was handled

**`TT` matches `tt_check` and `TT_RECIPES`.** Neither appears in the register
entries; the landed text writes `axis-TT` and `Z_axis-TT` in full.

**`trace` matches `traceless`.** The landing record does not restate the
component decomposition, so the collision had no route into this task's own
text; the source artifact keeps them apart and is merged unaltered.

**`projection` does not match `projector`.** Only the projection is discussed.

**`assumption` matches `locked assumptions` in gate text — 16 occurrences in
`GATES.md`, a different register.** This is why `M6` was answered by reading
the registers' own scope statements rather than by searching for the word:
a search would have pointed at `GATES.md`, which is not a register of
assumptions at all.

**`A-EXT-01` / `H-EXT-01` share a suffix and a search for one matches neither
reliably.** `C2` was established by reading both entries in full and confirming
that neither states the other's content — not by counting either identifier.

---

## §1a — Non-objectives, all honoured

**No criterion, threshold or acceptance band was set** on the discarded space;
`D-1` records that none is set and why. **The axis-TT projection question was
not adjudicated** — `D-3` routes it to `RECON-PROJ-01`. **Components 5 and 9
were not adjudicated.** **The frozen blind target was not modified or
re-registered**, and this task computed nothing it ranges over.
**`RECON-01b` was not begun.** **No file under `scripts/` was modified** — C11
records 62 → 63 files with zero modifications, the one addition arriving with
the merge.

---

## Stops and clarifications

**`SPECIFICATION_DEFECT`** — **none at STOP level.** The review notes one
non-substantive editorial point at its §18, `a execution-layer disposition`
in C7, and records that it does not alter execution semantics; this report
uses the grammatical form and flags nothing further. **Two provisions did real
work.** §1b's note that `P3` and `P4` are necessarily in the diff meant `A5`
did not fire on correct execution. And `M6`'s instruction to record separately
which register admits a definitional convention and which admits a physical
hypothesis, *"these may differ"*, is what produced a two-file landing rather
than a forced single location — **they do differ, and the Convention Registry
would have been the wrong home for a hypothesis.**

**`ENVIRONMENT`** — `scipy` absent for the nineteenth consecutive task; nothing
failed. **No environment failure occurred, so neither of Rule 13's two
diagnostic orders was exercised.**

**`OBSERVATION_METHOD_ERROR`** — **two, both mine, both caught before entering
the record.**

**First, in the `M7` recomputation.** My first parse of the landed coefficient
table returned **five retained and one discarded** component and produced
ratios of `0.102704` and `0.513518` against the reported `0.297300` and
`1.008193`. **That would have been an `A6` abort had I reported it.** The cause
was the sign character: the landed table writes negatives with **U+2212 MINUS
SIGN**, and my character class matched only ASCII hyphen, so the four negative
discarded rows were silently dropped and only the positive `D5` survived.
**This is the same encoding hazard `SIGN-01` was written about**, arriving here
in a parser rather than in a document. Re-parsed sign-aware, all ten rows are
found and both ratios reproduce exactly.

**Second, in the digest verification.** My first extraction of the `A-EXT-01`
statement used a regex with `re.S`, which let `.` match newlines and
over-captured the whole field block into the "statement", giving a digest
mismatch against the pin. **The landed bytes were correct; the harness was
wrong.** Re-extracted line by line, the digest matches. **A pin that appears to
break is exactly the alarm the binding rule is for, so a false alarm from a
sloppy extraction is worth recording rather than quietly fixing.**

**`REPOSITORY_DEFECT`** — **none found.**

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`** — **two, returned.**

**One: where an assumption review belongs.** §5.4 asks for a reviews path *for
assumption reviews*; `reviews/README.md` fixes a *by-author* layout. **I placed
the artifact in the author directory with a name that states its kind**, which
satisfies "distinct from the specification-review path" without creating a
second competing layout. **Whether a by-kind directory is wanted is a
convention question and is returned, not decided.**

**Two: which reading of `Review SHA` governs.** §5.4 can be read as pinning the
review artifact or as pinning the reviewed statement. **The binding rule's own
consequence — that an edit to a statement voids the pin — is only true under
the second reading**, so that is the one implemented, with the artifact digest
recorded alongside so the first is served too. **If the intent was the first
reading alone, the entries carry both values and nothing needs re-landing.**

---

## Layering

**Everything above is measured at commit 5,
`5fefd84e26edf2f74ae2b50ea6e3fc06adb0b9f2`**, except `C1` and `C10`, labelled
INTENDED.

**Returned to the Reviewer in chat, not written back:** the `--is-ancestor`
verification and its exit status, the push exit statuses, the remote read-back,
`C1` and `C10` as measured, and confirmation that
`science/recon-ext-01-discarded-space` still points at `70f0e257`.
