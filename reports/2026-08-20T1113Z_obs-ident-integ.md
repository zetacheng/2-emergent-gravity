# Execution report — `P2-OBS-IDENT-INTEG`

    OUTCOME     MERGED AND LANDED. No abort fired.
                The PROXY ONLY audit is on main. Four consequences are
                registered as open records and none is drawn.

                M5 FOUND A REGISTER THE LAST THREE INTEGRATIONS DID NOT
                CONSIDER. DECISION_LOG.md's stated scope admits all four
                records, on a precedent in the log itself. The three
                preceding tasks enumerated three registers and did not
                examine the fourth — that omission is reported at S-1.

                M4's subject set is empty, and this time the reason is
                stronger than additivity: main did not advance at all
                since the source was cut. Measured over both complete
                trees anyway.

**Specification:** `specs/2026-08-20T1113Z_obs-ident-integ.md`
**Review:** `reviews/chatgpt/2026-08-20T1113Z_obs-ident-integ.md`
**Landing record:**
`reports/2026-08-20T1113Z_obs-ident-integ_landing-record.md`
**Base:** `f23a0e1e1a24398d082a9597444ff9f750ed38e1`
**Source:** `science/obs-ident-01 @ 612817cb9ffa75ca02341e4f408f5fc952000557`

**Measurement head: `c4a46d8`,** the landing commit. This report is the commit
after it. `C2` and `C14` are INTENDED and measured in the post-report layer.

---

## §0 and `M1` — Binding SHAs, and the abbreviation (MEASURED, no A1 abort)

**§0 records the source SHA abbreviated and forbids merging against it.**

    git ls-remote origin refs/heads/science/obs-ident-01
      -> 612817cb9ffa75ca02341e4f408f5fc952000557

    §0's abbreviation    612817cb
    M1's full value      612817cb9ffa75ca02341e4f408f5fc952000557
    begins with it?      YES

    main   observed f23a0e1e1a24398d082a9597444ff9f750ed38e1   declared identical

**`A1` does not fire on either limb**, and **no command in this task was given
the abbreviation** — every merge and ancestry call names the full forty hex.

**Review binding (Rule 18, Amendment N).** The
`Reviewed specification SHA-256:` field was checked for PRESENCE before its
value was compared. Present, once, populated, at
`reviews/chatgpt/2026-08-20T1113Z_obs-ident-integ.md:4`.

    sha256 of the specification bytes as committed
      e8ceebdf16432b51c3616b3ff19f1c457253c10376867f05b75c34a5adfdd5ec
    the review's bound SHA
      e8ceebdf16432b51c3616b3ff19f1c457253c10376867f05b75c34a5adfdd5ec

**MATCH.** Verdict `APPROVE FOR EXECUTION`, with one interpretive note at the
review's §19, honoured below.

---

## Environment (MEASURED)

**Amendment D step 0.**

    execution location   …/scratchpad/iobsid   integration branch
                         …/scratchpad/base06   detached at f23a0e1e
    worktree identity    two real git worktrees
    resolved HEAD        science/integrate-obs-ident-01, c4a46d8
    ref reads            /home/user/2-emergent-gravity

    Python 3.11.15   pytest 9.1.1   numpy 2.4.6   sympy 1.14.0   ruff 0.15.8
    scipy  ABSENT — ModuleNotFoundError: No module named 'scipy'

Thirty-second consecutive task without `scipy`. Nothing here imports it.

**Rule 13.** No environment failure occurred. Neither diagnostic order was
exercised.

**The Reviewer's §19 note, honoured.** "No new result and no measurement" is
read as no new **subject-matter** result. **This task performed merge,
transport, register-admission and revert-hazard measurements**, and they are
reported as measurements below.

---

## §2 — Measurements

Nothing was carried, including from the source's execution report and from the
Researcher's verification of it.

### `M2` — validators, both sides (MEASURED)

    merge product 54823844   332 passed, 2 deselected   exit 0
    base f23a0e1e            332 passed, 2 deselected   exit 0

Real git worktrees. Identical. **`A3` does not fire.**

### `M3` — dry-run merge (MEASURED)

    git merge --no-commit --no-ff 612817cb9ffa75ca02341e4f408f5fc952000557
      exit 0, "Automatic merge went well; stopped before committing as requested"
      conflicting paths (--diff-filter=U): 0
      aborted; HEAD restored to bac1513

**`A2` does not fire.**

### `M4` — the revert hazard: the subject set is EMPTY, established by comparison (MEASURED)

**`M4` requires the set be measured even if it is expected to be empty.** It
was, over both complete trees:

    paths on main f23a0e1e                        579
    paths on source 612817cb                      583
    present on BOTH at DIFFERING blobs              0

**And the reason is stronger than in the preceding integration.**

    fork point = git merge-base f23a0e1e 612817cb
               = f23a0e1e1a24398d082a9597444ff9f750ed38e1

**The fork point IS the base. `main` did not advance at all since the source
was cut** — `git diff --name-status <fork>..f23a0e1e` returns nothing. The four
paths the source adds are the only difference between the trees.

**`A5` cannot fire.** It is recorded this way rather than as "expected empty"
because §`M4` says an empty set established by comparison is evidence and one
inferred from a short fork distance is not. **The comparison was run; the
inference would also have been available and is not what is reported.**

### `M5` — registers, per record (MEASURED — and this is the finding)

**All four records are admitted by `DECISION_LOG.md`.**

**Its stated scope**, from its head: "This log is append-only. New decisions
must use the entry template below and must not erase superseded decisions."

**The precedent, in the log itself.** `DECISION_LOG.md:2346` —
"## 2026-08-19 — EXT-01 execution-layer dispositions and open findings", with
`:2349` "Decision owner: Executor, adopted for the EXT-01 integration",
`:2359-2360` "**`O-1` and `O-2` are open findings, not decisions. Nothing is
settled by recording them.**", and a `### Reason` at `:2396-2400` explaining
that dispositions otherwise live only in a task report.

**`R-1` to `R-4` have exactly that shape**: open records, registered by an
executor for an integration, none answered. **The log admits them on its own
stated scope and its own precedent, not by resemblance.**

**Landed as one entry** dated 2026-08-20, using the template's
`### Decision` / `### Reason` / `### Consequences` / `### Related gate` /
`### Related branch and files` sections.

**`R-4` was NOT duplicated into `docs/GOVERNANCE-DEBT.md`.** It is adjacent to
`G-13` and the entry cross-references it while stating the difference: `G-13`
asks whether a reviewed definitional statement **may be** edited in place —
permission; `R-4` asks whether **this** statement's silence at its load-bearing
point **requires** supersession — necessity, about one instance. **A second
entry would create a second place for one status to drift**, which
`docs/GOVERNANCE-DEBT.md`'s `## Not entered here — D4` section warns against.

**Append-only verified on BOTH measures**, because `DECISION_LOG.md` declares
itself append-only at its `:3-4`:

    line measure   git diff --numstat  ->  87 added, 0 deleted
    byte measure   the new file's first 105456 bytes are byte-for-byte the
                   old file; 109667 bytes after

**No register was created and none was used by convenience.** **No record
restates an existing obligation**, and **the count of obligations with no
admissible home is not incremented by this task** — all four found a home.

### `M6` — the governing clause (MEASURED)

`docs/BRANCHING_POLICY.md:25-40`, `## Science branch integration`: `--no-ff`
into a dedicated integration branch, squash/rebase prohibited; "only the
integration branch and `refs/heads/main` may be pushed"; "Source branch,
session branches and unrelated refs must not move"; "`main` advances only by
fast-forward". **No contradiction with §4. `A4` does not fire.**

### `M7` — two measurements, and they differ (MEASURED)

**Base-relative, `git diff --name-only f23a0e1e..c4a46d8` — EIGHT paths:**

    M  DECISION_LOG.md                                          P2
    A  derivations/P2-OBS-IDENT-01_observable-identity.md        P1
    A  reports/2026-08-20T1050Z_obs-ident-01.md                  P1
    A  reports/2026-08-20T1113Z_obs-ident-integ_landing-record.md P3
    A  reviews/chatgpt/2026-08-20T1050Z_obs-ident-01.md          P1
    A  reviews/chatgpt/2026-08-20T1113Z_obs-ident-integ.md       P3
    A  specs/2026-08-20T1050Z_obs-ident-01.md                    P1
    A  specs/2026-08-20T1113Z_obs-ident-integ.md                 P3

**Source's own contribution, `git diff --name-status <fork>..612817cb` — FOUR
paths, all `A`:**

    derivations/P2-OBS-IDENT-01_observable-identity.md
    reports/2026-08-20T1050Z_obs-ident-01.md
    reviews/chatgpt/2026-08-20T1050Z_obs-ident-01.md
    specs/2026-08-20T1050Z_obs-ident-01.md

**THEY DIFFER: eight against four.** The four extra are this task's own three
artifacts and the register entry.

**`A6` does not fire**: every base-relative path maps to `P1`, `P2` or `P3`, and
`DECISION_LOG.md` is the register `M5` selected, which `P2` authorises.

**A note on the two measurements coinciding in an unusual way here.** Because
the fork point is the base, `git diff f23a0e1e..612817cb` would return the same
four paths as the fork-relative measurement — **the two would agree for once.**
Both were still taken separately, because their agreement is a property of this
fork distance and not of the method.

### `M8` — the reviewed result, transcribed (TRANSCRIBED)

Transcribed in the landing record's §1 and §2:

    outcome                PROXY ONLY
    definitional location  CONVENTIONS.md:21, the species coefficient as the
                           coefficient of m² ln m² in Z(m²); with :20 defining
                           Z(m²), and GATES.md:152 stating the same for the
                           scalar and adding "from a lattice mass scan"
    step 2                 proca_loop.slope :171-173 — varies q, holds m,
                           returns the q² coefficient. This is Z(m²).
    step 3                 reproduce_betav.vector_ZV :53-57 with
                           mlog_coeff.fit_mlog :81-89, docstring at :82 —
                           varies m, returns the m² ln m² coefficient.
    which step EXT-01 did  step 2, per component, at one mass. Not step 3.
    D3                     the difference is the MASS TREATMENT, and
                           consequently the extraction; the projection, the
                           object, the basis, the direction, the extent and
                           the momentum grid are common.

### `M9` — the two Statement SHAs (MEASURED)

    A-EXT-01  ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
    H-EXT-01  e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47

Each present once. `git diff --stat f23a0e1e..c4a46d8 -- CONVENTIONS.md
assumptions/H-EXT-01.md` is **empty** — **neither file modified**. **`A7` does
not fire.**

---

## §3 — Abort conditions

    A1  DID NOT FIRE.  Both §0 SHAs equal; M1's full value begins with §0's
                       abbreviation; no command used the abbreviation.
    A2  DID NOT FIRE.  Dry-run conflict-free, zero unmerged paths.
    A3  DID NOT FIRE.  M2 identical on both sides.
    A4  DID NOT FIRE.  M6 found the clause; it contradicts nothing in §4.
    A5  COULD NOT FIRE. M4's subject set is empty, measured over both trees;
                       main did not advance since the fork.
    A6  DID NOT FIRE.  Eight base-relative paths, all in the §1d manifest.
    A7  DID NOT FIRE.  No item required editing A-EXT-01, H-EXT-01, an
                       arriving file, or any landed artifact describing
                       EXT-01's measurement — C3 and C10 below.

---

## §7 — Acceptance criteria

    C1   SATISFIED   612817cb… is an ancestor of the integration head and is a
                     merge parent: 54823844 parents bac15134 612817cb.
    C2   INTENDED    Fast-forward from f23a0e1e, measured post-report.
    C3   SATISFIED   Four arriving paths, four byte-identical blobs, per path.
    C4   SATISFIED   M4's set is empty, established by comparing both complete
                     trees; no silent revert, and none was possible.
    C5   SATISFIED   §5.1 and §5.2 present in the landing record with M8's
                     citations.
    C6   SATISFIED   All four §5.3 items present.
    C7   SATISFIED   §5.4, §5.5 and §5.6 present; §5.5 carries its search
                     extent AND its exclusion.
    C8   SATISFIED   See below.
    C9   SATISFIED   R-1 to R-4 discharged per M5's admitting branch, in
                     DECISION_LOG.md, one entry, append-only on both measures.
    C10  SATISFIED   No landed artifact describing EXT-01's measurement is
                     modified. Verified by diff over six such paths: zero.
    C11  SATISFIED   Both Statement SHAs unchanged; neither file modified.
    C12  SATISFIED   The base-relative list contains no path outside §1d.
    C13  SATISFIED   M7 records both and states that they differ, 8 against 4.
    C14  INTENDED    Measured in the post-report layer.

### `C3`, per path

    path                                                source        product
    derivations/P2-OBS-IDENT-01_observable-identity.md   6dd35a0351c9  6dd35a0351c9  IDENTICAL
    reports/2026-08-20T1050Z_obs-ident-01.md             0b95b358c824  0b95b358c824  IDENTICAL
    reviews/chatgpt/2026-08-20T1050Z_obs-ident-01.md     859313f9be27  859313f9be27  IDENTICAL
    specs/2026-08-20T1050Z_obs-ident-01.md               bb439e483b48  bb439e483b48  IDENTICAL

### `C8`, with its exclusions — the criterion this landing was most exposed to

§10.4 of the specification names it: **"this landing's most likely defect is a
consequence drawn in passing"**, not a wrong measurement.

**Verified by reading, with the search stated.** The landing record was searched
for `without consequence`, `immaterial`, `merely procedural`, `purely
procedural` and `no consequence`. **Two hits, and both are permitted forms:**

    :4    "no consequence of the result is drawn" — a statement of what the
          record does, not that the outcome is without consequence
    :201  "It is not without consequence" — the DENIAL §1b requires

**And for consequences drawn.** Every occurrence of `GAP-B`, `MM-1`, `MM-3`,
`MM-5` and `D-2` in the landing record was read. **Four occurrences, in two
places:** the §3 statement that `Q1`, `GAP-A`, `GAP-B` and `H-EXT-01` are
**unchanged in status** — which §5.3 requires — and the §7 registrations of
`R-1` and `R-2`, which name them as undecided. **No occurrence draws a
consequence.**

### `C10`, the diff that proves nothing was rewritten

`git diff --name-only f23a0e1e..c4a46d8` restricted to the six landed artifacts
that describe `EXT-01`'s measurement —
`derivations/P2-RECON-EXT-01_discarded-external-space.md`, its report,
`derivations/P2-RECON-PROJ-01_projection-adjudication.md`,
`derivations/P2-PROJ-01-CLASS-01_q1-classification.md`,
`derivations/P2-GAPB-BRIDGE-01_regime-transfer.md` and
`scripts/diagnostics/ext01_discarded_external_space.py` — returns **zero
paths.**

---

## §8 — Substring hazards, and how each was handled

    observable      Three senses: this task's, the manuscript's channel
                    sense, and ordinary prose. Only the first occurs above,
                    and every use names the quantity it refers to.
    coefficient     THE DISTINCTION BETWEEN TWO OF ITS SENSES IS THE FINDING:
                    the q² coefficient (Z) and the mass-log coefficient (the
                    target). A projector's trace coefficient and the recipe
                    coefficients are the other two and appear nowhere above.
                    No count over the word was used anywhere; each occurrence
                    names which.
    proxy           Matches "proxy" in unrelated governance prose. Here it
                    occurs only as the outcome token PROXY ONLY.
    extraction      Matches "extract" in code prose. M8's steps were
                    transported from the reviewed result's citations, not
                    found by matching the word.
    step            The two extraction steps and ordinary usage. The landing
                    record numbers them 2 and 3 following the reviewed
                    result, and records that a step 1 precedes them, so the
                    numbering is not silently re-based.
    D-2 / D3        A DEFERRED ITEM AND A DETERMINATION STEP, UNRELATED, and
                    both occur in this task. D-2 is the item registered in
                    DECISION_LOG.md on 2026-08-19 and is R-1's subject; D3 is
                    the reviewed result's determination step transported at
                    M8. Every use above names which.

**Rule.** "A check that cannot state its exclusions is performed by reading."

---

## §1c — Non-objectives, all honoured

    1  draw any consequence for GAP-B, MM-1, MM-3, MM-5 or D-2
       NOT DONE. C8, with the occurrences read.
    2  amend, narrow, annotate or reword any landed description of EXT-01's
       measurement
       NOT DONE. C10 — zero paths in the diff.
    3  resolve the A-EXT-01 ambiguity
       NOT DONE. Transported and registered as R-4; the statement is
       unaltered and M9 confirms the pin.
    4  integrate science/gapb-bridge-01
       NOT DONE. That ref is untouched and is not an ancestor of the merge
       product.
    5  perform any measurement, or specify one beyond what the reviewed
       result already specifies
       NOT DONE. The landing record restates the reviewed result's
       specification of the extraction and adds nothing to it.
    6  modify any file under scripts/
       NOT DONE. The scripts/ diff is empty.
    7  modify any file arriving from the source
       NOT DONE. C3, per path.

---

## Stops and clarifications

### `S-1` — `M5` found a register the last three integrations did not consider, and that is an omission of mine

**`P2-PROJ-01-INTEG`, `P2-RECON-01B-B0-INTEG` and `P2-GAPA-INTEG` each executed
an `M5` step and each reported that no register admitted some record.** In all
three, the registers enumerated were
`derivations/P2-DEFERRED-ITEMS.md`,
`derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md` and
`docs/GOVERNANCE-DEBT.md`.

**`DECISION_LOG.md` was not among them, and it should have been examined.** It
is a register by any reading its own text supports, it is append-only, it
requires an entry template, and — measured — **it already held `O-1` and `O-2`
as open findings registered by an executor for an integration**, at its
`:2346-2394`. That is the same shape as the records those tasks reported
homeless.

**What follows, and what does not.** Whether those earlier records would have
been admitted by `DECISION_LOG.md` **is not decided here**, and this task does
not reach back to place them: they belong to landed tasks, and the register
question for each is theirs. **What is established is that their `M5`
enumerations were incomplete**, which bears on the standing of the
"three obligations with no admissible home" figure those reports carry.

**Recorded as an executor omission**, not as a defect in those specifications:
each said "read the registers' stated scopes", and I read three of four.

### `S-2` — `M4`'s emptiness has a different cause this time, and the distinction is worth keeping

`P2-GAPA-INTEG` reported an empty subject set because `main`'s advance since
that fork was **purely additive**. **Here `main` did not advance at all** — the
fork point and the base are the same commit.

**Both are empty sets and they are not equally strong.** An additive advance
leaves paths that *could* have differed and did not; no advance leaves no
opportunity. **The comparison was run in both cases, which is why the
difference is visible rather than assumed**, and `M4`'s wording — measure it
even when it is expected to be empty — is what makes that so.

### `S-3` — the compliance self-correction was transported, and it is about the check and not the checker

§5.6 required transporting the observation that the reviewed result's own
compliance paragraph, in first draft, listed the literals it was proving absent
— into a document the same criterion's search extent covered.

**Transported in the general form the specification asks for**: a compliance
report that proves a literal absent by quoting it has introduced the thing it
was checking for, and **the check's extent must be read before its evidence is
written.**

**Recorded here that the same trap was present in this report and was avoided
deliberately.** `C8`'s verification above names the phrasings searched for —
which is safe, because `C8` bars *statements that the outcome is without
consequence*, and naming the phrase inside a criterion check is not making the
statement. **The distinction is that `C8`'s subject is an assertion and the
earlier criterion's subject was a literal.** A criterion over literals cannot
be verified by quoting them; a criterion over assertions can be verified by
naming the words an assertion would use.

---

## Layering

This report is measured at `c4a46d8`, the landing commit, which is commit N−1.
`C2` (the fast-forward) and `C14` (the ref-push scope) are measured in the
post-report layer; that evidence is returned to the Reviewer in chat and is not
written back into this file.
