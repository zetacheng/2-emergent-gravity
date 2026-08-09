# Task specification — replay the PI decisions and deferred-items task on the current base

Specification evidence base: `7c5cba5df76de6ef8f52af390ca92100dcdf0d8b`

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**Rules 1–17 are in force at this evidence base**, so this task is
governed by Rule 15: its pre-execution review is a committed artifact —
see §4 commit 2 and A3.

**This is Amendment K's first stale-base re-issue.** The content is
approved and unchanged; only the base has moved.

---

## 0. Why this exists, and what it is not

`fix/pi-decisions-v2 @ ebd531ab568aaffabd86a4a94d925a711e62aa36` was
executed, reviewed and verified. **It was cut from `f309f61c…`, and
`main` has since advanced through two governance landings.** A dry-run
merge onto the current `main` **conflicts in `DECISION_LOG.md`**:

    on the approved branch only   three 2026-08-09 PI rulings
                                  (scalar channel; eta; negative-mass branch)
    on main only                  two governance rulings
                                  (Rules 14/15; Rules 16/17)

**Nothing is deleted or altered on either side.** Both appended at the
file's end and Git cannot order them. **The conflict is purely
ordering.**

**Why the conflict was not resolved by hand.** Keeping every entry from
both sides, with zero deletions and zero modifications, **would itself
have been append-only** — that is not the objection. **The objection is
that it would create an authority that has never existed: an integration
task deciding the relative order of two independently authored sets of
decision entries.** That authority belongs to neither source task. **It
could be granted, but granting it sets a precedent that an append-only
log's conflicts may be arranged by whoever integrates**, and there is no
need to open that.

**So this is a replay, not a repair.** The approved substantive content
is re-instantiated on the current authoritative base under a new task
identity.

**What the resulting order means.** The three PI rulings will follow the
two governance rulings in the log. **That reflects when each entered the
authoritative `main` lineage, not when it was decided** — the rulings
remain dated 2026-08-09, and no decision date is altered.

**This task applies Amendment K's re-issue discipline to a stale-base
case under explicit PI authorization in this specification.** K's stated
case is the re-issue of an executed specification, cut from the evidence
base under a new task identity. **K does not yet name stale-base loss of
conflict-free integrability as a subclass**, so **this specification
supplies the missing construction rather than asking the Executor to
infer it** — which is what K itself requires when a resolution needs a
construction the specification does not describe.

**If K is ever revised, this class belongs in it explicitly.**

## 1. What to do

**Create a NEW branch from the evidence base**, under a new name and new
task-identity paths, and re-instantiate the approved content.

    superseded for integration, preserved, not carried forward:
      fix/pi-decisions-v2 @ ebd531ab568aaffabd86a4a94d925a711e62aa36
      Its content remains APPROVED; only its integrability lapsed.

    this task:
      fix/pi-decisions-v3   cut from 7c5cba5d…

**Re-instantiate; do not re-derive and do not re-word.** The three
`DECISION_LOG.md` rulings and `derivations/P2-DEFERRED-ITEMS.md` carry
the substance of `ebd531ab…`, which review settled. **Re-opening that
wording is out of scope.**

**But re-verify rather than transcribing blind.** Confirm each evidence
quotation independently against the pinned material and run the literal
checks yourself. **A replay that copies an approved artifact without
re-checking it inherits any error the approval missed.**

## 2. Acceptance criteria

**A0 — Commit order and paths, frozen.**

    commit 1  specs/2026-08-XXT{HHMM}Z_pi-decisions-v3.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_pi-decisions-v3.md
    commit 3  DECISION_LOG.md, derivations/P2-DEFERRED-ITEMS.md
    commit 4  reports/2026-08-XXT{HHMM}Z_pi-decisions-v3.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **The token MUST differ from
`0430` and `1416`**, used by the two superseded executions — reusing
either would make the executions indistinguishable by path.

**Commit 2 precedes the work**, per Rule 15's timing clause.

**A1 — Pinned inputs**, verified before use; any mismatch is a STOP:

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a

    derivations/P2-PHASE-01_channel_character.md
    380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f

    derivations/P2-PHASE-01_channel_character_layers.md
    4cea53a7163ccc6aadadd0fca276714c16d805ad8aed3594d64d66d412606711

    results/P2-PHASE-01/channel-character-layers/layers.json
    fe343c74389cc996e42567d7dd510f479f1e7ed01cba81de61ff1d6f7e9d1542

    reports/2026-08-05_p2-phase-01_scalar-stationary-exploratory.md
    70ab88eda32483420c0bfd522babd2ca4a73941bc2d2d20f8414976641756cbe

    results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json
    a4537efad3b46e5e429b5310baad8b4dbf36d9c95582873dbfa0b03cc44d7028

    derivations/P2-PHASE-01_scalar_stationary_exploratory.md
    80586e33ef07e307729af4597f72b48f6ecee74fc6a0f396b593f735ef322599

**`DEFERRED-02`'s evidence is split across three of these**: the report
and results artifact carry the roots, curvatures and tested complement
relation; **the exploratory derivation note carries the SCOPE
LIMITATION** — *"Neither curvature is a full condensate-space Hessian or
a phase-admissibility statement"* — which is what narrowed Decision 3
from "stable" to positive restricted curvature.

**Method for each check: `git cat-file blob <rev>:<path> | sha256sum`.**

**A2 — Evidence re-verified, not inherited.** For `DEFERRED-01` and
`DEFERRED-02`, locate each `Evidence:` statement in the pinned material
and quote it. **If either is not there, STOP.**

**For `DEFERRED-03`, verify instead that the entry states
`Evidence: none` and supplies no citation. The absence of evidence is
intentional content there, not a failed lookup.**

**A3 — This task's pre-execution review committed, unedited.** The
Reviewer's approval of THIS specification is supplied with it. Place it
at `reviews/chatgpt/2026-08-XXT{HHMM}Z_pi-decisions-v3.md`,
**byte-identical to the text supplied between the supplied delimiters,
excluding the delimiter lines and any instruction accompanying them.**
Report its committed blob digest.

**You do not write it, edit it, summarise it, or reformat it. If a
placeholder appears inside the review's text, it stays as written** —
resolve placeholders in the path only. **If the supplied text is missing
or does not correspond to this specification, STOP.**

**A4 — Substantive equivalence to the approved branch, with explicitly
permitted task-identity substitutions.**

**The approved source is identified by blob, not required as the
destination.** `derivations/P2-DEFERRED-ITEMS.md` at `ebd531ab…` has
blob id `ffeae5eb52115e131536e10508b72ac3ff51379d`; verify the SOURCE
with `git rev-parse ebd531ab:derivations/P2-DEFERRED-ITEMS.md`.

**Your file MUST NOT be blob-identical to it.** Line 6 of that register
reads `Authority: specs/2026-08-09T1416Z_pi-decisions-v2.md`, and yours
must point at this execution's specification. **Requiring blob equality
would force you to keep a pointer to a superseded specification** —
which is why an earlier version of this criterion could not be
satisfied.

**The task-identity normalisation function, defined here and applied to
BOTH texts.** An earlier version said "one explicitly defined
normalisation" while defining only which differences were permitted —
**Amendment H requires the function itself, not a description of its
effect.**

    For each text independently:

      1  replace the exact specification path identifying that
         execution with the literal token  <TASK_SPEC>
      2  replace the exact report path identifying that execution, if
         present, with the literal token  <TASK_REPORT>
      3  perform NO other replacement, deletion, whitespace
         normalisation or reformatting

    Source substitutions, applied to ebd531ab…'s register:
      specs/2026-08-09T1416Z_pi-decisions-v2.md    -> <TASK_SPEC>
      reports/2026-08-09T1416Z_pi-decisions-v2.md  -> <TASK_REPORT>

    Destination substitutions, applied to yours:
      the resolved specs/2026-08-XXT{HHMM}Z_pi-decisions-v3.md
                                                   -> <TASK_SPEC>
      the resolved reports/2026-08-XXT{HHMM}Z_pi-decisions-v3.md
                                                   -> <TASK_REPORT>

**After the function is applied to both files, the resulting byte
sequences MUST be identical.** This is stronger than ignoring
task-identity differences: **it canonicalises them exactly and then
requires the whole register to match byte for byte.**

**Before applying the function, report every differing line.** **Every
difference MUST be explained entirely by one of these substitutions** —
**all `DEFERRED` entry content, including status, reason, PI position,
evidence, blocks, evidence-strength qualification and hypothesis
wording, is inside the byte-identical requirement.**

**For the three `DECISION_LOG.md` rulings**, compare under this
normalisation applied to both sides: strip blockquote prefixes (`> `),
strip `**` and backticks, collapse whitespace to single spaces. **Keep
en dashes as they are.**

**A silent substantive drift between an approved artifact and its
replay is a defect.**

**A5 — Required phrases present**, checked against the same normalised
text:

    entry 1   scalar channel with a real auxiliary field
              This is a choice of direct route
              It is deferred, not excluded
              This does not close OPEN-AC-1
    entry 2   the programme evaluates both the
              rather than selecting between them
              depends on an unresolved sign convention
    entry 3   DEFERRED, not excluded
              they do not establish full condensate-space stability,
                phase admissibility, or absence of physical content
              cannot by itself classify this branch as an unphysical
                lattice artifact
              that criterion's quantifier range is undetermined

**A phrase may appear in the entry's surrounding prose where the
verbatim ruling does not contain it. Do not edit a ruling to make a
check pass.**

**A6 — `DECISION_LOG.md` append-only, on BOTH measures**, per Amendment
K:

    evidence base -> branch head          zero deleted lines
    each commit -> its parent             zero deleted lines

**Report both.** **The two governance entries already on `main` — Rules
14/15 and Rules 16/17 — must be present and unaltered at the branch
head, and the three PI rulings appended after them.**

**A7 — Superseded branch untouched.** After the push, verify from the
remote that `fix/pi-decisions-v2` still resolves to
`ebd531ab568aaffabd86a4a94d925a711e62aa36`, and that
`59c763ab…` and `52f65117…` remain reachable in the history of
`fix/pi-decisions-and-deferred`. **Delete no branch; force-push
nothing.**

**A8 — Nothing else touched.** `GATES.md`, `CONVENTIONS.md`,
`AGENTS.md`, `pyproject.toml`, and **every path under `scripts/`,
`results/`, `tests/`, `derivations/`, `docs/` and `reviews/` that exists
at the evidence base**: blob-identical to the evidence base. **Compare
path by path, not as tree objects** — `reviews/` gains a path this task
authorises, and `derivations/P2-DEFERRED-ITEMS.md` does not exist at the
base.

**`P2-PHASE-01` remains `PROPOSED`; `P2-GAP-01` remains `PASS`.**

**A9 — Scope**, four additions and one modification:

    add:
      specs/2026-08-XXT{HHMM}Z_pi-decisions-v3.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_pi-decisions-v3.md
      derivations/P2-DEFERRED-ITEMS.md
      reports/2026-08-XXT{HHMM}Z_pi-decisions-v3.md
    modify:
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 4 additions and 1 modification.**

**A10 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`. **A10-pre** at the pre-report head
goes in the report; **A10-final** at the pushed head is post-report
evidence.

**A11 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to
`7c5cba5df76de6ef8f52af390ca92100dcdf0d8b`; **create the new branch from
that commit — it does not yet exist.** Move no `main` ref. **Local
`main` is stale by design.** Report all three. Push the task branch
only.

## 3. Accumulated-reading assessment, in Rule 16's form

**Rule 16 is operative at this evidence base and governs this task.**
State what the assembled set does NOT establish, **naming the junction
or reporting a search.**

**A candidate, offered so you can confirm or replace it.** Three
executions of this task now exist — `59c763ab`, `52f65117`, `ebd531ab` —
plus this one, each preserved. **A reader could conclude the content was
revised three times.** It was revised once, on substance; **the other
two re-issues were about representation and base, not content.** If you
find a stronger junction, report that instead.

## 4. Evidence layering

**Committed report:** A1–A9, A10-pre, the earlier commit SHAs and
messages, the pre-report head, the intended final manifest, and the
intended report commit message with its authoring-time trailer
suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A10-final, the push, the
report commit's stored message read back from the object, and ancestry
confirmation.

## 5. Invariants and prohibitions

- Executor-writable: the five paths of A9 only.
- **Do not touch, reset, rewrite, or delete any superseded branch.**
- **Do not reuse the `0430` or `1416` tokens.**
- **Decide nothing.** The decisions are the PI's; record them.
- **Do not compute anything**, and do not perform the diquark
  calculation Decision 2 authorizes.
- **Do not add the SI-1 cross-reference** — `GATES.md` is protected and
  that is an agreed separate task.
- **Do not resolve any merge conflict.** This task creates a branch from
  the current base precisely so that none arises; **if one does, STOP.**
- Commit-message hygiene: inspect the proposed message before each
  commit and the stored message after; permit no `Co-Authored-By`, no
  session identifier or URL, no tool attribution. **Report per commit
  whether any trailer was suppressed and which.**
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: `fix/pi-decisions-v3`.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item. If they differ
  for what you need, report which you followed and why; if no
  environment failure occurs, say that neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 6. Report contract

- raw output for A1–A10, scope-checker JSON verbatim including
  `observed_operations`;
- the evidence quotations for `DEFERRED-01` and `DEFERRED-02`, with
  their source paths;
- **the A4 equivalence comparison**, with the normalisation stated and
  any difference reported with its reason;
- the A5 literal check results;
- **both append-only measures of A6**, stated separately, and the two
  governance entries shown present and unaltered;
- confirmation that every superseded branch and commit remains at its
  recorded value and reachable;
- **§3's accumulated-reading assessment**, junction named or search
  described;
- **whether this specification told you how to represent a stale-base
  replay clearly enough that no judgement was required.** Amendment K
  was written for a different cause; **if it fits this case only
  loosely, that is worth knowing before it is applied again**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 7. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**
Re-run these; if any fails to reproduce, STOP and report which — do not
adjust a target to make it pass.

    target      DECISION_LOG.md at fix/pi-decisions-v2 @ ebd531ab…
    method      Python substring containment after normalisation
    check type  NORMALISED SUBSTANTIVE — one function applied to both
                sides: strip "> " prefixes, strip ** and backticks,
                collapse whitespace; en dashes preserved

    PASS   scalar channel with a real auxiliary field
    PASS   This is a choice of direct route
    PASS   It is deferred, not excluded
    PASS   This does not close OPEN-AC-1
    PASS   the programme evaluates both the
    PASS   rather than selecting between them
    PASS   depends on an unresolved sign convention
    PASS   DEFERRED, not excluded
    PASS   they do not establish full condensate-space stability, phase
             admissibility, or absence of physical content
    PASS   cannot by itself classify this branch as an unphysical
             lattice artifact
    PASS   that criterion's quantifier range is undetermined

**A4's normalisation function, executed against the source register:**

    target      derivations/P2-DEFERRED-ITEMS.md at ebd531ab…
    blob        ffeae5eb52115e131536e10508b72ac3ff51379d

    specs/2026-08-09T1416Z_pi-decisions-v2.md      1 occurrence
    reports/2026-08-09T1416Z_pi-decisions-v2.md    0 occurrences
    residual `pi-decisions-v2` or `1416Z` strings after substitution: 0

**The function is complete for the source side**: one specification
reference, no report reference, and nothing identifying the v2 execution
survives it. **Step 2 will be vacuous on the source and may be vacuous
on yours; a vacuous substitution is not a failure.** **Verify the
destination side yourself** — your register must carry its own
specification reference, and if it also carries a report reference,
step 2 applies.

**All eleven reproduce on the approved branch**, which is the source A4
requires equivalence to. **The Git blob id and the seven pinned SHA-256
digests are byte-exact checks, not normalised ones**, and their method
is stated in A1 and A4.
