# Task specification — repair the adopted artifact's wording and both stale gate pins

Specification evidence base: `2e4cc6eb9ae8a34d7a5e81c86d82a5b631dabe7a`

    Branch to create   science/adopt-parameter-domain-repair
    Cut from           science/adopt-parameter-domain @ 2e4cc6eb…
    Authoritative main 1cb5550f… — NOT touched by this task

Classification: **MATERIAL**. Governed by Rule 15 and Rule 18.

**This task does not touch `main` and does not merge.** It corrects a
branch so that the branch becomes integrable. **Integration is a separate
task**, and the adoption branch must not be integrated before this one
lands on it.

**Cut from the adoption branch, not from `main`.** The adoption work is
not superseded and is not being redone; it is being completed. **No
register entry is written and nothing is declared superseded.**

---

## 0. What is wrong, and why one of the two problems creates the other

**Two defects, and they are linked.**

**Defect A — three sentences in the adopted artifact still describe it as
a draft.** At `2e4cc6eb…`,
`derivations/P2-PHASE-01_microscopic_parameter_domain.md` carries
`**Status: ADOPTED.**` and, around it:

    line 1   a title ending "— DRAFT FOR ADOPTION"
    lines 5-7 "Adoption requires a task with its own specification and
             pre-execution review; nothing here is in force until that
             task lands."
    line 9   "It supersedes nothing."

**The last is now false**: `GATES.md` calls the old draft superseded and
the old draft has been stamped `SUPERSEDED.`. **The first is worse than
false — it is the first line a reader sees**, and it says DRAFT above a
status line that says ADOPTED.

**The adopting specification anchored only the bold status sentence.**
That is the defect: **an anchored substitution repairs exactly what it
anchors**, and three neighbouring sentences carried the same claim.

**Defect B — `GATES.md` pins a digest that no longer matches.**

    GATES.md:1040  pins  a3ec0cb6…
                   for   derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
    that file at 2e4cc6eb…  is  e373efcb…

The adopting task was authorised to insert a cross-reference paragraph
into that file, and the insertion changed its bytes. **The specification
that authorised the modification did not authorise the consequent
re-pin**, and the executor correctly refused to re-pin without authority.

**And repairing Defect A creates a third stale pin unless it is handled
in the same task.**

    GATES.md:1017  pins  c27e57f0…
                   for   derivations/P2-PHASE-01_microscopic_parameter_domain.md

**Editing that artifact changes its digest.** **So this task must re-pin
BOTH lines, and the second re-pin exists only because of the first
repair.** **A task that fixed the wording and re-pinned only line 1040
would land in exactly the state it was written to remove.**

## 1. The PI ruling that authorises the re-pin

**Recorded verbatim as issued. It is a ruling, not a derivation.**

> **PI RULING.** A registered-gate artifact pin denotes the exact
> operative bytes of the referenced artifact. Where an authorised task
> intentionally modifies that artifact, retaining the old digest would
> create a false correspondence and is not an acceptable landed state.
> The prohibition on an executor re-pinning a gate without authority
> prevents unilateral repair; it does not require an authorised
> modification to leave a knowingly stale pin. Accordingly, before
> integration of `science/adopt-parameter-domain`, a separately reviewed
> corrective task must update the `P2-PHASE-01` admissibility-contract
> draft pin from `a3ec0cb6…` to the digest of the exact bytes intended to
> land. No prerequisite state, gate status, or admissibility verdict is
> changed by that re-pin.

**This task is that separately reviewed corrective task.**

**The ruling names one pin. This task updates two**, because the second
became stale inside this task rather than the previous one. **The
ruling's principle covers it** — a pin denotes exact operative bytes, and
`c27e57f0…` will not be the operative bytes once A4 lands. **If the
Reviewer reads the ruling as authorising only the named pin, STOP and say
so**, because then Defect A cannot be repaired in this task either.

## 2. What this task must not do

- **Do not touch `main`**, do not merge, do not fast-forward.
- **Do not change any gate `Status:` line**, any prerequisite state, or
  any admissibility verdict. **`P2-PHASE-01` stays `PROPOSED`; the
  ADMISSIBILITY CONTRACT prerequisite stays `UNSATISFIED`; the
  MICROSCOPIC PARAMETER DOMAIN prerequisite stays `SATISFIED`.**
- **Change nothing in `GATES.md` except the two digest strings.** Not the
  surrounding words, not the paths, not the headings.
- **Do not edit the two DRAFT files.** They are already correct; the
  contract draft's bytes at the evidence base are what the new pin must
  denote.
- **Do not answer `C1`, `C2` or `C3`**, and do not read
  `scripts/p2_phase01_scalar_exploratory.py`.
- **Do not correct anything in the adopted artifact beyond §3.** If you
  find a fourth wording defect, **report it and leave it.**
- **Do not write a superseded-register entry.**

## 3. The three wording repairs, verbatim

**OLD-1** — the title, line 1:

    # `P2-PHASE-01` microscopic parameter domain — DRAFT FOR ADOPTION

**NEW-1:**

    # `P2-PHASE-01` microscopic parameter domain — ADOPTED

**OLD-2:**

    **Status: ADOPTED.** Adopted by
    `specs/2026-08-12T2258Z_adopt-parameter-domain.md`. This artifact
    is written for PI confirmation and reviewer scrutiny. **Adoption requires
    a task with its own specification and pre-execution review**; nothing
    here is in force until that task lands.

**NEW-2:**

    **Status: ADOPTED.** Adopted by
    `specs/2026-08-12T2258Z_adopt-parameter-domain.md`, under the
    pre-execution review committed alongside it. **This artifact is in
    force.** It was written for PI confirmation and reviewer scrutiny,
    both of which it received; **the sentences that described it as
    awaiting them were left behind by an anchored substitution that
    repaired only the status line, and are corrected here.**

**OLD-3:**

    **It supersedes nothing.** `derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`
    deliberately adopted no domain and retained five open items. **This
    artifact answers four of them and leaves one open**, and says which is
    which.

**NEW-3:**

    **It supersedes one artifact.**
    `derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`
    deliberately adopted no domain and retained five open items; **it is
    now marked SUPERSEDED and is retained as historical evidence.** **This
    artifact answers four of those items and leaves one open**, and says
    which is which.

**Three operations on three anchored strings.** **If any OLD string is
not found verbatim exactly once, STOP and report which** — do not locate
an approximate match.

## 4. The two re-pins, verbatim

**RE-PIN 1**, `GATES.md` line 1017, under the MICROSCOPIC PARAMETER
DOMAIN block:

    OLD  (sha256 `c27e57f080ecf8a2472a7f614aedcc19c5c72622650f6ddd0bc802d3fced5003`).
    NEW  (sha256 `<the digest of derivations/P2-PHASE-01_microscopic_parameter_domain.md
          measured from the COMMITTED BLOB at commit 3>`).

**RE-PIN 2**, `GATES.md` line 1040, under the PHASE INPUT /
ADMISSIBILITY CONTRACT block:

    OLD  (sha256 `a3ec0cb6f7968cf92528e2197f34aedd86882eed08bfc58410142fdb875a9e73`).
    NEW  (sha256 `e373efcb0d14db641604537c6a264e2c48536ab516162b7fef6a995cbd11d1cb`).

**RE-PIN 2's value is stated here because it is already fixed** — that
file is not modified by this task, so its digest at the evidence base is
its digest at the head. **Measure it and confirm it equals the value
above; if it does not, STOP.**

**RE-PIN 1's value cannot be stated here**, because it does not exist
until §3 is committed. **Measure it from the committed blob, not from a
working-tree file.**

**Two operations, on the two digest strings only.** Each 64-hex string
occurs exactly once in `GATES.md`; **verify that before substituting.**

## 5. Commit order and evidence layering

Cut `science/adopt-parameter-domain-repair` from
`2e4cc6eb9ae8a34d7a5e81c86d82a5b631dabe7a`.

    commit 1  specs/2026-08-XXT{HHMM}Z_adopt-domain-repair.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_adopt-domain-repair.md
    commit 3  derivations/P2-PHASE-01_microscopic_parameter_domain.md
    commit 4  GATES.md
    commit 5  reports/2026-08-XXT{HHMM}Z_adopt-domain-repair.md

    stated: 3 additions, 2 modifications
    base: 2e4cc6eb9ae8a34d7a5e81c86d82a5b631dabe7a
    head: <commit 5>
    mode: exact
    add:
      reports/2026-08-XXT{HHMM}Z_adopt-domain-repair.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_adopt-domain-repair.md
      specs/2026-08-XXT{HHMM}Z_adopt-domain-repair.md
    modify:
      GATES.md
      derivations/P2-PHASE-01_microscopic_parameter_domain.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.**

**Commit 3 precedes commit 4 because RE-PIN 1 embeds commit 3's blob
digest.** The same ordering the adopting task used, for the same reason.

**Committed report — measured at commit 4:** A1–A8 and A10–A11 for
commits 1–4; **A9's two checker runs with both configs verbatim**;
commit 1–4 SHAs and stored messages; commit 5's intended message; **the
final scope stated as INTENDED.**

**Post-report evidence, NOT written back:** the final scope measured
base-to-commit-5; A9-final at commit 5; A11 for commit 5; validators at
commit 5; the push; the branch tip read back.

**Nothing in the committed report may claim to measure commit 5.**

## 6. Acceptance criteria

**A1 — Refs.** `science/adopt-parameter-domain` resolves to
`2e4cc6eb9ae8a34d7a5e81c86d82a5b631dabe7a`; `refs/heads/main` resolves to
`1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`. **Any mismatch → STOP.**

**A2 — This task's pre-execution review committed, unedited**, per Rule
18: supplied as a file, no delimiters, bytes unchanged. **It must carry
`reviewed specification SHA-256:` AND `reviewed artifact SHA-256:`
filled in** — the specification digest as well as the artifact digest,
because a review that names only the artifact cannot establish which
specification it approved. **If either is blank or names a different
digest, STOP and say which.** Report the supplied file's digest and the
committed blob's digest and show them equal.

**A3 — Pinned inputs at the evidence base**, Git blob ids, all four
measured and reported:

    GATES.md
    derivations/P2-PHASE-01_microscopic_parameter_domain.md
    derivations/P2-PHASE-01_input_admissibility_contract_DRAFT.md
    derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md

**Also measure and report the SHA-256** of the two files named in §4, at
the evidence base. **The contract draft must measure
`e373efcb0d14db641604537c6a264e2c48536ab516162b7fef6a995cbd11d1cb`; if
it does not, STOP.**

**A4 — The three wording repairs**, per §3, applied to
`derivations/P2-PHASE-01_microscopic_parameter_domain.md`. **Report the
digest before and after, and the count of operations: THREE.** **Diff
that file base to commit 3 and report it in full: exactly three hunks,
each corresponding to §3.** **A fourth hunk is a STOP.**

**A5 — The two re-pins**, per §4, and **`GATES.md` changes in no other
way.** **Diff `GATES.md` base to commit 4 and report it in full: exactly
two hunks, each a single digest string.** **A hunk touching a heading, a
path, a prerequisite state or a `Status:` line is a STOP.**

**A6 — Every pin in `GATES.md` is checked against its target at the
final head.** **Not only the two this task changes.** For each occurrence
of `` (sha256 `<64 hex>`) `` in `GATES.md`, identify the artifact path
named immediately above it, measure that path's SHA-256 at the head, and
**report the pair.**

**Expected: two pins, both matching.** **Report the count you found and
every pair, matching or not.** **A pin whose target does not match is a
finding and must be named** — even if this task did not create it, and
even if repairing it is out of scope.

**This criterion exists because no validator performs it.** The staleness
that caused this task was invisible to a 280-test suite; **the check is
performed here by hand and reported, and that is not the same as it being
enforced.**

**A7 — Gate invariants unchanged.** At commit 4: `^## P2-` count is
**14**; every `Status:` line is textually identical to the evidence base;
`P2-PHASE-01` reads `Status: PROPOSED`; the MICROSCOPIC PARAMETER DOMAIN
prerequisite reads `SATISFIED`; the PHASE INPUT / ADMISSIBILITY CONTRACT
prerequisite reads `UNSATISFIED`. **Report all five.**

**A8 — Protected paths.** Every path existing at the evidence base other
than the two in §5's `modify:` list is blob-identical at commit 5. **In
particular both DRAFT files, every path under `results/`, `scripts/` and
`tests/`.** Compare path by path.

**A9 — The checker over this task's own range**, base `2e4cc6eb…`, head
**commit 4**. Two runs:

    RUN 1  default subject selection, observational, governs nothing
    RUN 2  specification_paths naming ONLY
           specs/2026-08-XXT{HHMM}Z_adopt-domain-repair.md

**Config for both runs, stated so that you supply no value of your own:**

    append_only_paths          ["DECISION_LOG.md"]
    authorised_modified_gates  ["P2-PHASE-01"]
    prospectivity              boundary ce86b534…, both readings run
    register_path              docs/BRANCHING_POLICY.md

**`append_only_paths` is NOT `[]`.** An empty set turns `P3` from
`NOT_DECLARED` into `NOT_APPLICABLE` — the check switched off rather than
passed.

**`P7` will return `PASS` and it is evidence of nothing.** At this
evidence base `GATE_HEADING` matches zero of the fourteen real gate
headings, so `P7` compares two empty maps. **This task modifies
`GATES.md`, so that vacuous green is exactly where it is most
dangerous.** **The claim that the `GATES.md` edit stayed within two
digest strings rests on A5's diff, not on `P7`.**

**RUN 2 is stop-governing; any failure is a STOP, with no pre-authorised
exception.** **Both configs and both JSON outputs verbatim.**

**A9-final, post-report evidence:** re-run RUN 2 at commit 5. **If it
fails, STOP.**

**A10 — Validators, exit status 0**, run as the repository defines them,
and **report the pass and deselect counts before and after.** **Name any
test whose behaviour changed.** **Expected: none** — this task changes
prose and two digest strings.

**A11 — Commit-message hygiene** on all five commits: proposed message
inspected before, stored message after; no `Co-Authored-By`, no session
identifier or URL, no tool attribution. **Commits 1–4 go in the report;
commit 5 is post-report evidence.**

## 7. Rule 16 assessment

**Rule 16 is operative.** State what the assembled set does NOT
establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** After this
task, both pins in `GATES.md` will match their targets. **A reader may
infer that gate pins are kept correct.** **Nothing keeps them correct.**
The two that match do so because A6 was performed by hand in this one
task; **no test compares any pin to any file**, and the next task that
edits a pinned artifact will go stale in the same silence unless its
specification remembers.

**Say that plainly**, and say that a check performed once by a person is
not a check that runs.

## 8. Invariants and prohibitions

- Executor-writable: this specification, its review, its report, and the
  two paths in §5's `modify:` list. **Nothing else.**
- **Do not change any digest string other than the two in §4**, and do
  not add a pin.
- **Do not adjust the config to make RUN 2 pass.** Narrowing a subject
  set, supplying an empty declared set or dropping a property is a
  specification stop.
- **Do not describe `P7` as having checked gate integrity.**
- No force-push, no history rewrite, no branch deletion.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- everything in §5 under its correct layer, **each committed figure
  labelled MEASURED or INTENDED**;
- **A4's before and after digests**, the operation count, and the full
  three-hunk diff;
- **A5's full two-hunk diff of `GATES.md`**;
- **A6's complete pin table**, with the count of pins found;
- **A7's five gate invariants**;
- **A9's two runs, both configs verbatim**, and the explicit statement
  about `P7`;
- **whether the adopted artifact now reads as an adopted document from
  its first line**, which is the defect this task exists to remove;
- **§7's Rule 16 assessment**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently — **in particular whether §1's reading, that the ruling's
  principle covers the second pin, is sound.**

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**
**Every line was produced by running the stated method in a clean
clone.** **No measurement was taken through a truncated view.**

    target      the branch and main
    method      git fetch; git rev-parse against origin
    MEASURED    science/adopt-parameter-domain = 2e4cc6eb9ae8a34d7a…;
                main = 1cb5550f… ; the branch head is NOT an ancestor
                of main

    target      the stale pin of Defect B
    method      read GATES.md at 2e4cc6eb; sha256sum the named target
                at 1cb5550f and at 2e4cc6eb
    MEASURED    GATES.md:1040 pins a3ec0cb6…; the contract draft is
                a3ec0cb6… at 1cb5550f and e373efcb… at 2e4cc6eb.
                The pin was correct before the adopting task and is
                stale after it.

    target      the pin that THIS task's repair would make stale
    method      read GATES.md at 2e4cc6eb; sha256sum the adopted
                artifact
    MEASURED    GATES.md:1017 pins c27e57f0…, which matches the adopted
                artifact's current bytes. Editing that artifact breaks
                this pin. THIS IS WHY §4 CARRIES TWO RE-PINS AND NOT
                ONE.

    target      every pin in GATES.md, counted over the whole file
    method      grep -nB2 'sha256 `[0-9a-f]{64}`' — no head, no tail
    MEASURED    exactly TWO pins, at lines 1017 and 1040. The
                parameter-domain draft's former pin d8e15469… is gone,
                removed as a side effect of the adopting task's block
                replacement.

    target      the three wording anchors of §3
    method      read the committed blob at
                2e4cc6eb:derivations/P2-PHASE-01_microscopic_parameter_domain.md
    MEASURED    each OLD string occurs exactly once

    target      gate invariants at the evidence base
    method      grep -c '^## P2-'; read the P2-PHASE-01 block
    MEASURED    14 sections; Status: PROPOSED; MICROSCOPIC PARAMETER
                DOMAIN SATISFIED; PHASE INPUT / ADMISSIBILITY CONTRACT
                UNSATISFIED

    target      whether any validator checks a pin
    method      the adopting task's report records 280 tests passing
                with the pin already stale
    MEASURED    the stale pin survived a full validator run. No test
                compares a GATES.md pin to its target. A6 is performed
                by hand for that reason.

    target      this specification under the landed P1 grammar
    method      the parser extracted VERBATIM from blob 1922fe88… and
                executed — not re-implemented
    MEASURED    one scope block; stated 3 additions, 2 modifications;
                manifest lists three and two; parse OK, counted equals
                stated.
