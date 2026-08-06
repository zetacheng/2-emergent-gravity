# Task specification — deliver raw evidence, then integrate the clean role-model branch

Specification evidence base: `a0e9d11b7281f0c2185aa8d517bae009ab54807f`
Source branch: `review/role-model-and-executors-clean` @
`7d69fd3393de1b1843c0b80db9cd1752a56765d0`

Classification: **MATERIAL**. Three stages under one PI specification,
with a **mandatory Reviewer release** between Stage 1 and Stage 2.

**This specification authorizes Stages 0 and 1 immediately. Stage 2
becomes executable only when the Reviewer issues an explicit release**
covering S0, S1 and S2 together — not A6-final and A7-final alone, since
Stage 0 creates a new authority artifact and a new source head that must
themselves be verified. The release takes this form:

    Stage-0 authority commit: PASS
    Original A6-final at 7d69fd3393de1b1843c0b80db9cd1752a56765d0: PASS
    Stage-0 augmented source scope: PASS
    Original A7-final at 7d69fd3393de1b1843c0b80db9cd1752a56765d0: PASS
    Stage-0 augmented source validators: PASS
    Source head: <full Stage-0 SHA>
    Stage 2 is released for execution under this specification.

Absent that release, **do not merge.**

---

## 0. Two conditions the Reviewer set, and how each is met

The result review verified content, layering, scope, clean commit
messages and the A4 semantic correction, then withheld integration on
two grounds.

**Condition 1 — raw evidence.** A6-final and A7-final arrived
summarised. Stage 1 supplies them unsummarised. **The Reviewer verifies
Stage 1 before Stage 2 proceeds. Do not merge until told.**

**Condition 2 — the A4 line-rewrap. PI ratification, recorded here.**

> **PI ratification, 2026-08-06.** The line-wrap changes within the A4
> sentence in `AGENTS.md` are accepted as a non-semantic layout
> adjustment. The authorized A4 delta is the exact textual substitution
> together with reflow of that same sentence only, with no other token
> change. The branch is not to be rebuilt for this.

**Stage 0 below commits this specification, which is what puts the
ratification into the repository.** The previous draft asserted that it
would be committed while authorizing no path and no commit to do it —
the reviewer was right to call that a provenance claim without a
mechanism.

**This ratifies a defect in the specification, not a deviation by the
executor.** The specification required `AGENTS.md` to differ "by exactly
the A4 replacement and nothing else". In a file hard-wrapped near 70
columns, a textual substitution cannot satisfy that: the only
alternative to reflowing is leaving a 118-character line, which is
itself an unauthorized formatting change. **The criterion was strictly
unsatisfiable, and the executor took the reasonable branch and proved
equivalence mechanically.** Stage 0 commits this specification, so the
ratification enters the repository as a committed artifact rather than
remaining in conversation.

*Also recorded, as a specification lesson rather than an instruction:
"one-hunk diff" is a weak constraint — a hunk is a diff-algorithm
artifact and a wholesale paragraph rewrite is also one hunk. The
property that actually constrains the change is substitution-exactness
under whitespace normalisation, which the executor supplied unprompted
and which is what carried the verdict. Future specifications should ask
for that directly, and should supply byte-exact replacement strings in
an indented verbatim block rather than inline backticks.*

## Stage 0 — commit this specification

On the SOURCE branch `review/role-model-and-executors-clean`, add one
commit containing only this specification, at:

    specs/2026-08-06T{HHMM}Z_role-model-raw-evidence-and-integration.md

`{HHMM}Z` is a UTC token obtained immediately before the commit. Report
the resulting blob SHA-256, the commit SHA, and the complete stored
commit message. **The commit-message hygiene requirements of Stage 2 A9 apply equally to
the Stage-0 commit:** inspect the proposed message before committing;
inspect the STORED message after; permit no `Co-Authored-By`, session
identifier or URL, or tool attribution; **and if one appears despite the
pre-commit inspection, STOP before pushing.**

**This changes the integration source head.** Everything downstream —
the pre-merge manifest's `head`, `expected_parent_2`, the pinned source
branch value in A1 — becomes YOUR Stage-0 commit, not `7d69fd33…`.
Report both, and state the relationship explicitly. `7d69fd33…` remains
its parent and stays reachable.

**Nothing else is added or modified on that branch.** The three reviewed
commits are untouched; this is a fourth, additive commit carrying the
authority for what follows.

**Push it — by ordinary fast-forward only. Force-push is prohibited.**
Without this, the remote source branch stays at `7d69fd33…`, Stage 2
cannot merge the pinned remote ref, and A1 fails.

- **Before pushing**, verify the remote branch is exactly
  `7d69fd3393de1b1843c0b80db9cd1752a56765d0`. **Any pre-push remote
  mismatch is a STOP.**
- **After pushing**, fetch and verify that all three agree on the
  Stage-0 commit: local `review/role-model-and-executors-clean`;
  `refs/remotes/origin/review/role-model-and-executors-clean`; and
  `git ls-remote origin refs/heads/review/role-model-and-executors-clean`.

Report as raw evidence: pre-push local and remote refs; the push
command with **complete stdout, stderr and exit status**; the post-push
fetch; the three-way ref agreement; and confirmation that the Stage-0
commit's parent is `7d69fd33…`.

## Stage 1 — raw post-commit evidence, unsummarised

**Stage 1 is read-only. Run each check against the EXACT revision named
in that criterion** — S1a and S2a against the old reviewed head
`7d69fd3393de1b1843c0b80db9cd1752a56765d0`; S1b and S2b against the new
Stage-0 source head. These checks are deterministic and modify neither
revision.

**S0 — Stage-0 authority commit evidence.** Return: the Stage-0 commit
SHA and its parent; the complete stored commit message; changed-path
output proving **exactly one added path**; the specification path and
its blob SHA-256; the complete source-branch push evidence of Stage 0;
local, remote-tracking and `ls-remote` agreement; and an attestation of
any transcription, encoding or line-ending transformation introduced
while creating the artifact.

**Two scope verdicts are needed, not one.** Stage 0 adds a path to the
source head, so the previous task's eight-path manifest cannot be run
against the new head under `mode: exact` — it would fail on the ninth
path. Running it against the OLD head is still required, because that is
the historical acceptance evidence the Reviewer asked for. **Neither
substitutes for the other, and you may not edit the previous task's
frozen manifest.**

**S1a — the original A6-final, at the OLD head.** Run the clean-rebuild
task's eight-path final manifest against
`7d69fd3393de1b1843c0b80db9cd1752a56765d0`, unchanged. Return: the
original manifest TEMPLATE; the RESOLVED manifest; its SHA-256; the
exact command; **complete stdout; complete stderr; exit status.**

**S1b — Stage-0 augmented source scope, at the NEW head.** Run this
nine-path manifest, supplied here, against your Stage-0 commit. It
demonstrates that Stage 0 added the authorized authority artifact and
disturbed nothing else:

    base: a0e9d11b7281f0c2185aa8d517bae009ab54807f
    head: <full Stage-0 commit SHA>
    mode: exact
    add:
      specs/2026-08-06T{HHMM}Z_role-model-raw-evidence-and-integration.md
      specs/2026-08-06T1218Z_role-model-clean-rebuild.md
      specs/2026-08-06T0456Z_role-model-and-executors.md
      reports/2026-08-06T0456Z_role-model-and-executors.md
    modify:
      AGENTS.md
      reviews/README.md
      HANDOFF.md
      PROGRESS.md
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

Permitted transformations, and no others: replace
`<full Stage-0 commit SHA>` with the SHA verified under S0, and replace
`{HHMM}` with the token in the committed Stage-0 filename. Return
template, resolved manifest, SHA-256, exact command, complete stdout and
stderr, and exit status.

**Validator evidence splits for the same reason scope did.** The old
head and the Stage-0 head are different Git objects. Re-running at the
new head shows the authority artifact broke nothing; it does NOT supply
the historical acceptance evidence the Reviewer asked for, and cannot be
back-dated to stand for it. `tests/test_repository_structure.py` and
other governance tests could in principle respond to a newly added path,
so the two runs are not interchangeable even in the benign case.

**S2a — the original A7-final, at the OLD head
`7d69fd3393de1b1843c0b80db9cd1752a56765d0`.** If your earlier transcript
preserved the complete process outputs, deliver those. **If you re-run
instead, re-run AT THE OLD HEAD** — a new-head result may not be
substituted.

**S2b — Stage-0 augmented-source validators, at the NEW head**, your
Stage-0 commit, under identical controls.

For each of S2a and S2b, on a clean detached worktree, all five files
(`tests/test_repository_structure.py`, `tests/test_si1_governance.py`,
`tests/test_gate_anchors.py`, `tests/test_governance_tools.py`,
`tests/test_p2_phase01_scalar_exploratory.py`), return: the worktree
creation command; `git rev-parse HEAD` in it; `git status --porcelain`
**before and after** the runs; `python --version` and `pytest --version`
with outputs; and per file the exact command, **complete stdout,
complete stderr**, exit status and wall time.

**S3 — Branch, push and ancestry, raw.** **Separate THREE classes of
evidence here.** The original push stdout/stderr is process output, not
a Git object: it cannot be regenerated by a read-only rerun. Return it
if your execution transcript preserved it; **if not, mark it
`UNAVAILABLE HISTORICAL PROCESS OUTPUT`** — do not re-push, do not
simulate it, and do not present rerun ref evidence as though it were the
original push output.

**Three distinct classes, not to be substituted for one another:**

*Historical process evidence* — the original clean-branch push
stdout/stderr, if your transcript preserved it; otherwise
`UNAVAILABLE HISTORICAL PROCESS OUTPUT`.

*Stage-0 process evidence* — complete stdout, stderr and exit status
from the newly authorized Stage-0 fast-forward push (also reported under
S0).

*Current-state evidence* — after fetch, and **not including any push
output**: local refs for both `review/role-model-and-executors` and
`review/role-model-and-executors-clean`; remote-tracking refs;
`git ls-remote` outputs; the ancestry commands with exit statuses;
`git rev-list --count` for the main-ahead figure; and raw ref outputs
for local `main`, `origin/main`, and remote `refs/heads/main`.

**Raw means raw.** If an output is long, it is still returned in full.
The Reviewer could not verify the previous delivery precisely because
completeness was the thing summarising removed.

**Then stop and report. Do not proceed to Stage 2 until authorized.**

## Stage 2 — integration

Authorized only after the Reviewer accepts Stage 1.

**A1 — Base and source still as expected.** `origin/main` equals
`a0e9d11b7281f0c2185aa8d517bae009ab54807f`, and the source branch
`review/role-model-and-executors-clean` equals **YOUR Stage-0 commit**,
whose parent is `7d69fd3393de1b1843c0b80db9cd1752a56765d0`. Verify both
relationships and report both SHAs. Either mismatch → STOP and report
the new tip; approval covers branch and base together.

**Stage 2 runs in this fixed order. Everything verifiable locally is
verified BEFORE the push, because a failure discovered after pushing has
already changed `main`:**

    1  fetch; verify A1
    2  create an isolated clean integration worktree from the base
    3  PRE_MERGE guard (A3)
    4  create the --no-ff merge commit (A2)
    5  inspect the stored merge message and both parents (A9)
    6  on the UNPUSHED merged head: A7 protected paths, A8 source
       blobs, A10 validators, and the parent / scope / pinned-artifact
       checks of the post-merge manifest
    7  push ONLY IF every check at step 6 passed
    8  fetch; run the final POST_MERGE guard with
       remote_check_policy = REQUIRED (A4)

**Remote agreement is the only check that genuinely requires the push.**
If the merge guard offers no pre-push mode for the parent, scope and pin
checks, **do not pretend it does** — run the equivalent read-only checks
directly against the merged head and say which commands you used.

**A2 — Merge, `--no-ff`, on a local integration branch.** The source
descends from the base, so an ordinary merge would fast-forward and
produce no merge commit. Parent 1 = the base; parent 2 = **the Stage-0
commit**, which is the source branch head once Stage 0 is done.

**A3 — Pre-merge guard.** `PRE_MERGE` with `reviewed_base` = the base;
`reviewed_branch` = the Stage-0 commit; `expected_worktree_head` = the base
(the merge is performed from it); `expected_merge_base` = the base; the
scope manifest of A5; the pinned artifacts of A6.

**A4 — Post-merge guard**, after pushing: `POST_MERGE` with
`expected_parent_1` = the base; `expected_parent_2` = the Stage-0 commit
(the source head after Stage 0, NOT `7d69fd33…`);
`expected_merge_base` = the base; `remote_check_policy = REQUIRED`,
`expected_remote_ref = refs/remotes/origin/main` (the full ref, not the
shorthand), `expected_remote_sha` = the merge commit. **Fetch
immediately before this guard and report the fetch command and its raw
output**, so the remote-tracking ref is not a stale pre-push value. Expected `remote_agreement: PASS`. **Expected values are
supplied, never read back from the object under test.**

**A5 — TWO scope manifests, because pre-merge and post-merge examine
different objects.** The merge guard passes the manifest straight to the
scope evaluator; it does NOT substitute the merge commit for you. A
post-merge manifest still pointing at the source branch would evaluate
`base → source` and report PASS **without ever examining the merge
commit's tree** — the guard's whole purpose in that pass.

**Pre-merge manifest — used by the `PRE_MERGE` config:**

    base: a0e9d11b7281f0c2185aa8d517bae009ab54807f
    head: <the Stage-0 commit SHA>
    mode: exact
    add:
      specs/2026-08-06T{HHMM}Z_role-model-raw-evidence-and-integration.md
      specs/2026-08-06T1218Z_role-model-clean-rebuild.md
      specs/2026-08-06T0456Z_role-model-and-executors.md
      reports/2026-08-06T0456Z_role-model-and-executors.md
    modify:
      AGENTS.md
      reviews/README.md
      HANDOFF.md
      PROGRESS.md
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Post-merge manifest TEMPLATE — used by the `POST_MERGE` config:** the
same, except

    head: <computed merge commit SHA>

**Both blocks are frozen TEMPLATES. The permitted transformations are
exactly these, and no others:**

*Pre-merge template:* replace `<the Stage-0 commit SHA>` with the full
Stage-0 commit SHA verified under S0; replace the single `{HHMM}` with
the token in the committed Stage-0 filename.

*Post-merge template:* replace `<computed merge commit SHA>` with the
full merge commit SHA created under A2; replace the single `{HHMM}` with
that same Stage-0 token.

**No other path, operation assignment, `base`, `mode`,
forbidden-operation entry, or byte may change.** Do not describe the
head substitution as "adding a head": each template already has one, and
replacing it correctly is the point.

Report both templates, both resolved manifests, both SHA-256 values, and
both complete guard JSONs including `observed_operations`.

**A6 — Pinned artifacts survive unchanged:**

    derivations/P2-LATTICE-ONTOLOGY-01.md
    1a03870eb5a24a748f3803e066a281dbbe4b64fa67860dad32409b41c0660b5c

    scripts/euclidean_reconstruction.py
    30e3b59a0006b2ecc2d6ecce391ab918ce9ba542b2af649c55570e0643e63a78

**A7 — Protected paths.** `CONVENTIONS.md`, `GATES.md`,
`pyproject.toml`, and every blob path present under `tests/`,
`scripts/`, `derivations/`, `results/` at the base: blob ids identical
between base and the merged head; no path added, deleted, renamed or
type-changed under those prefixes. **`GATES.md`'s gate count and every
gate's `Status:` and `Reviewer verdict:` mapping are unchanged** —
extract at base and at merged head and show the difference is empty,
excluding explicitly labelled historical or superseded subsections.

**A8 — Source artifacts intact after merge.** (These six are unaffected
by Stage 0, which only adds a new specification file.) The five byte-identical
source blobs arrive unchanged, and `AGENTS.md` arrives as the source
branch had it:

    specs/2026-08-06T0456Z_role-model-and-executors.md  05472d8d339b1f89e6dee265ea7a14190ee01d21
    reviews/README.md                                   9ef4ec5e68091e6f7f226a5ad69e64aa81d0b038
    HANDOFF.md                                          e60026120d933c1977ad0568506d292721cce2e8
    PROGRESS.md                                         5ef6e65a1e3f927d92b708c6527eab0f839d569c
    DECISION_LOG.md                                     0464b854c8adf57b2e79841a2d754bccf2c68a05
    AGENTS.md                                           5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3

**A9 — Merge commit message.** The same commit-message hygiene
requirements applied to the Stage-0 commit apply to the merge commit: inspect the proposed
message before creating it, read the stored message back afterwards, and
**suppress every trailer this specification does not authorize** — no
`Co-Authored-By`, no session identifier or URL, no tool attribution. If
one appears despite pre-commit inspection, **STOP; do not push.**

**A10 — Validators, exit status 0**, run individually on the merged
head: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`,
`tests/test_p2_phase01_scalar_exploratory.py`. Report each command,
complete stdout and stderr, exit status, and wall time.

**A11 — Old branch preserved.** `review/role-model-and-executors` still
resolves to `10c260b96882ac12610f78840aeeabd07be2d7cb`, local and
remote. **It is the record of what happened, including the metadata
defect, and is not deleted, renamed, force-pushed or modified.**

## Invariants and prohibitions

- **Stage 0 exception.** The Executor may add exactly ONE new
  repository artifact, on `review/role-model-and-executors-clean`:
  `specs/2026-08-06T{HHMM}Z_role-model-raw-evidence-and-integration.md`,
  containing this specification faithfully and without substantive
  alteration. **That file is the only content difference permitted
  between `7d69fd3393de1b1843c0b80db9cd1752a56765d0` and the new source
  head.**
- **Apart from that Stage-0 authority artifact, no repository content is
  executor-editable.** Stage 2 may create only the authorized merge
  commit and may not alter the merged tree. The reviewed content is
  integrated exactly as reviewed.
- Merge commit only: no fast-forward, no squash, no rebase, no
  force-push, no history rewrite. Both source branches remain reachable.
- Merge the pinned remote ref, not a local copy that may have drifted.
- **Any merge conflict is an immediate stop.** None is expected and none
  is pre-authorized.
- No registered gate, gate status, verdict, digest, or hash-pinned
  artifact may be modified. `CONVENTIONS.md` and `pyproject.toml` are
  out of scope.
- **Do not fix the stale role text in `docs/RESEARCH_WORKFLOW.md`,
  `README.md`, or `docs/local/execution_environment.md`.** They are a
  separate authorized task.
- Do not change persistent or global configuration. Commit-object
  identity and signatures are outside this specification's scope, as the
  Reviewer found; **if commit-object metadata is to be governed, that
  needs its own authorization** and is not attempted here.
- Do not alter any existing worktree containing uncommitted content, and
  do not clean, stash, or discard untracked files anywhere.
- Stop-on-unexpected-result applies to commands that read or alter
  repository state, not to your own scratch tooling. Correct your own
  tooling and say that you did.
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## Report contract

- **Stage 1 raw evidence, in full**, returned before Stage 2 begins;
- for Stage 2: both guard JSONs verbatim including `observed_operations`;
  raw output for A1–A11; the merge commit SHA, both parents, and the
  complete stored merge-commit message with any suppressed trailer
  named; `origin/main` before and after;
- the states of the merge worktree and the main worktree, **stated
  separately**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
