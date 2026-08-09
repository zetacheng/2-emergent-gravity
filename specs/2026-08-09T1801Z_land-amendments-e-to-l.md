# Task specification — land amendments E–L and new Rules 16 and 17

Specification evidence base: `a4bfb337bd6ee92d60303e5cbb8f0646c48c16ed`

> **Rules 1–15 are in force at this evidence base**, and this task is the
> first governed by Rule 15. **Its pre-execution review is therefore a
> committed artifact of this task** — see A0 commit 2 and A4a. **The
> prospective exemption the Rules 14/15 landing relied on is no longer
> available**, because Rule 15 is now operative on `main`.

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**This is an EXECUTION task, not a review request.** The source draft is
marked `PROPOSED` and says it is not an executor prompt; **that marking
describes the draft, not this specification.** The draft has completed
review and is approved. **You are landing it.**

---

## 0. The source

    /mnt/user-data/outputs/DRAFT_amendment_observation_and_propagation.md
    6368aff4ad66126f115be3fd0689e513db59e6061a28dd4e599b9bb5aa91c0e4

Supplied with this specification. **Verify the digest before use.**

**The draft contains SEVEN refinements to existing rules, one proposed
new rule originally labelled "Amendment J", and one proposed "New Rule
16".** Each carries the incident that produced it, marked `CAUGHT
PRE-ISSUE` or `REACHED EXECUTION`. **The incident records are the rules'
justification and are not instructions to you.**

**"E–L" in this specification's title is the draft's labelling, not a
count of refinements.** The draft's Amendment J becomes a new rule here
and is not one of the seven — **an earlier version of this
specification said "eight amendments", which contradicted its own
mapping.**

## 1. What lands, and the numbering this specification resolves

    Amendment E  -> Rule 14   a failed observation is not a negative result
    Amendment F  -> Rule 12   mutation tests must prove reach
    Amendment G  -> Rule 9    structural changes propagate
    Amendment H  -> Rule 3    literals are verified by execution
    Amendment I  -> Rule 8    mid-task authority needs reviewer-visible
                              provenance
    Amendment K  -> Rule 5    re-issuing an executed specification
    Amendment L  -> Rule 9    consumed conventions must be discoverable

    New Rule 16               accumulated reading
    New Rule 17               integrations do not add epistemic or
                              governance classifications

**The numbering of the two new rules is decided here, because the draft
left it open.** The draft labels the accumulated-reading rule "New Rule
16" and labels Amendment J only "(new)", with no number. **Both are new
rules and both need one.**

**Resolution: the accumulated-reading rule keeps the number the approved
draft gives it, 16; Amendment J becomes Rule 17.** The alternative —
renumbering the accumulated-reading rule to make room — would change a
label the review settled. **Do not adopt any other assignment.**

**Two amendments attach to Rule 9.** G concerns structural propagation
within a specification; L concerns whether a consumed convention is
discoverable. **They are distinct refinements of the same rule and both
attach to it. Do not merge them.**

## 2. What must not happen

- **Do not renumber rules 1–15**, and do not reword or reorder them
  beyond the seven stated refinements.
- **Do not alter the substance of any amendment.** Adapt wording to the
  file's style; **the normative content is settled.**
- **Do not import the incident records into `CONVENTIONS.md`.** The
  rules land; their justifications live in the draft, which A4 commits
  as an artifact.
- **Do not back-fill or modify any EXISTING review record.** Create only
  the Rule-15-required review artifact for this task, per A4a. **An
  earlier version forbade creating any `reviews/` record at all —
  which, with Rule 15 now in force, would have made this task unable to
  comply with a rule already operative.**
- **Do not modify `AGENTS.md`.** Its research rules are a different
  numbering from `CONVENTIONS.md`'s execution-discipline rules.

## 3. Acceptance criteria

**A0 — Commit order and paths, frozen.**

    commit 1  specs/2026-08-XXT{HHMM}Z_land-amendments-e-to-l.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_land-amendments-e-to-l.md
    commit 3  CONVENTIONS.md, DECISION_LOG.md,
              docs/amendments/2026-08-09_observation-and-propagation.md
    commit 4  reports/2026-08-XXT{HHMM}Z_land-amendments-e-to-l.md

**Commit 2 is Rule 15's timing requirement**: the pre-execution review
is committed **before the work it authorises proceeds.** Commit 3 is the
work.

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.**

**A1 — Pinned inputs**, verified before use; any mismatch is a STOP:

    CONVENTIONS.md
    639ee10fb8e72ddfca5c0f307705328dcd303c6e246cd2917d8a8ba682349612

    the supplied amendment draft
    6368aff4ad66126f115be3fd0689e513db59e6061a28dd4e599b9bb5aa91c0e4

**A2 — Rules 14 and 15 confirmed present.** `CONVENTIONS.md` at the
evidence base carries execution-discipline rules **1 through 15**, with
no 16 or 17. Report the extracted heading list. **If Rule 14 is absent,
STOP** — Amendment E has nothing to attach to, and that is this task's
stated premise.

**A3 — Seven refinements applied**, each to its stated rule, reproducing
the draft's normative text.

**For each amendment report three things**, because "before and after"
alone admits two defensible readings — the whole rule, or only the
insertion point:

    1  the pre-existing rule text, unchanged
    2  the exact normative text the amendment adds
    3  the resulting rule section

**For Rule 9, identify and report the G and L insertions separately.**

**A4 — The draft committed as a governing artifact.** Place the source
draft at `docs/amendments/2026-08-09_observation-and-propagation.md`,
**byte-identical to the supplied file**, and report its digest at the
committed blob. **This task requires it as the durable provenance of the reviewed
amendments**, consistent with Rule 15's governing-artifact principle.

**Do not claim that Rule 15's literal text names a reviewed source draft
as a governing artifact.** It names specifications, pre-execution
reviews, task reports and supplied manifests — **asserting more than it
says is what Amendment J forbids.** **Quote Rule 15 as landed** and cite
it in the report; describing a rule is not evidence that it says so.

**A4a — The pre-execution review committed, unedited.** The Reviewer's
approval of THIS specification is supplied with it. Place it at
`reviews/chatgpt/2026-08-XXT{HHMM}Z_land-amendments-e-to-l.md`,
**byte-identical to the text supplied**, and report its committed blob
digest.

**You do not write it, edit it, summarise it, or reformat it.** It
records what the Reviewer said, and **an executor-authored document that
looks like a review would satisfy the letter of Rule 15 while defeating
it.** If the supplied text is missing or does not correspond to this
specification, **STOP**.

**A5 — Rules 16 and 17 added**, per §1's assignment, as new sections in
the file's existing `### <n>. <title>` style, after Rule 15.

**A6 — Rules 1–15 unchanged apart from the seven authorised
insertions.** Their numbers and titles are identical, **and — after
removing only the seven authorised inserted amendment blocks — the
remaining pre-existing text is byte-identical to the evidence-base
version.**

**Heading equality alone is a proxy, not the property.** It would not
detect a rule silently reworded under an unchanged heading. Report both
checks.

**A7 — `DECISION_LOG.md` entry** in the file's existing format,
recording the adoption, the numbering resolution of §1, and that the
rules are prospective. **Append-only: zero deleted lines, verified both
against the evidence base AND against each commit's parent.** The second
measure is Amendment K's, and **this task is among the first to be
checked by a rule it is landing.**

**A8 — Amendment H applied pre-issue, and reproducibly.** This
specification carries a **Pre-issue literal verification record** (§7)
identifying, for each literal-sensitive check: its target, its check
type (byte-exact or normalised substantive), the normalisation function
where one applies, the executable verification method, and PASS.

**You independently re-run those stated checks.** **If a recorded check
cannot be reproduced, STOP** and report which — do not adjust the target
to make it pass.

**An earlier version asserted only that the author had run the checks.**
That is unverifiable from the repository and is exactly the proxy
Amendment H forbids: **the record must let you re-run it, not ask you to
believe it happened.**

**A9 — Nothing else touched.** `AGENTS.md`, `GATES.md`,
`pyproject.toml`, and **every path under `scripts/`, `results/`,
`tests/`, `derivations/`, `reviews/` and `docs/` THAT EXISTS AT THE
EVIDENCE BASE**: blob-identical to the evidence base. **No gate status
changes.**

**Two paths this task adds do not exist at the base** — the
`docs/amendments/…` draft and the `reviews/chatgpt/…` review — so no
exception is needed for either. **But do not compare `docs/` or
`reviews/` as whole tree objects**, which would report differences A10
authorises. **No EXISTING review record is modified or back-filled.**

**A10 — Scope**, three additions and two modifications:

    add:
      specs/2026-08-XXT{HHMM}Z_land-amendments-e-to-l.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_land-amendments-e-to-l.md
      docs/amendments/2026-08-09_observation-and-propagation.md
      reports/2026-08-XXT{HHMM}Z_land-amendments-e-to-l.md
    modify:
      CONVENTIONS.md
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 4 additions and 2 modifications.** Report the
template, the resolved manifest, its SHA-256, and the scope-checker JSON
including `observed_operations`.

**A11 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`. **A11-pre** at the pre-report head
goes in the report; **A11-final** at the pushed head is post-report
evidence.

**If any validator asserts a rule count or `CONVENTIONS.md` structure,
report what it asserts** — a governance test constraining the file this
task edits is worth knowing about, and adding two rules may trip it.

**A12 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to the evidence base; create the branch
from that commit; move no `main` ref. **Local `main` is stale by
design.** Report all three. Push the task branch only. **Delete no
branch.**

## 4. Evidence layering

**Committed report:** A1–A10, A11-pre, the earlier commit SHAs and
messages, the pre-report head, the intended final manifest, and the
intended report commit message with its authoring-time trailer
suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A11-final, the push, the
report commit's stored message read back from the object, and ancestry
confirmation.

## 5. Invariants and prohibitions

- Executor-writable: the five paths of A10 only.
- **Do not apply any other numbering** than §1's.
- **Do not merge Amendments G and L**, which attach to the same rule.
- **Do not alter the amendment draft** when committing it under A4. It
  is committed as reviewed, byte for byte.
- Commit-message hygiene: inspect the proposed message before each
  commit and the stored message after; permit no `Co-Authored-By`, no
  session identifier or URL, no tool attribution. **Report per commit
  whether any trailer was suppressed and which.**
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: use `governance/land-amendments-e-to-l`.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 6. Report contract

- raw output for A1–A11, scope-checker JSON verbatim including
  `observed_operations`;
- the rule heading list **before and after**, showing 1–15 unchanged and
  16–17 added;
- the seven refinements, each with its before and after, **Rule 9's two
  shown separately**;
- Rules 16 and 17 quoted in full as landed;
- the committed draft's blob digest, shown byte-identical to the
  supplied file;
- the `DECISION_LOG.md` entry with **both** append-only measures;
- **whether any of the seventeen rules now reads as contradicted by
  another.** Seventeen rules written at different times can conflict,
  and **you are reading them together in a way nobody has**;
- **whether any rule you just landed would have changed how you executed
  this task.** Several of them govern specification and execution
  practice directly — **if one of them is violated by this very task,
  that is worth more than a clean report**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 7. Pre-issue literal verification record

**Executed by the specification author against the supplied draft before
issue, per Amendment H.** Re-run these; if any fails to reproduce, STOP.

    target      DRAFT_amendment_observation_and_propagation.md
    digest      6368aff4ad66126f115be3fd0689e513db59e6061a28dd4e599b9bb5aa91c0e4
    method      Python substring containment against the file's raw text
    check type  EXACT LITERAL SUBSTRING — no normalisation applied to
                either side; the literal itself is character-for-
                character identical

    PASS   Amendment E (attached to Rule 14)
    PASS   Amendment F (attached to Rule 12)
    PASS   Amendment G (attached to Rule 9)
    PASS   Amendment H (attached to Rule 3)
    PASS   Amendment I (attached to Rule 8)
    PASS   Amendment J (new)
    PASS   Amendment K (attached to Rule 5)
    PASS   Amendment L (attached to Rule 9)
    PASS   New Rule 16 — accumulated reading

**The em dash in the last entry is `—` (U+2014) and is SEMANTIC**; it is
not normalised away. **No normalisation function applies to any check in
this table** — the literals are character-for-character identical.

**These heading checks establish the INSERTION TARGETS only.** Fidelity
of the amendments' substantive content is established against the
digest-pinned complete draft under A1 and A3.

**Checks against `CONVENTIONS.md` at the evidence base**, same method,
same check type:

    target      CONVENTIONS.md at a4bfb337…
    digest      639ee10fb8e72ddfca5c0f307705328dcd303c6e246cd2917d8a8ba682349612

    PASS   ### 3. Declared frozen scope is normative
    PASS   ### 5. Minimum mandatory merge discipline
    PASS   ### 8. Responsibility separation
    PASS   ### 9. Outcome-based task specification
    PASS   ### 12. Acceptance criteria must be mechanically checkable
    PASS   ### 14. Validator outcome contract
    PASS   ### 15. Governing artifacts are committed

**These are the seven insertion targets** — the rules Amendments E, F,
G, H, I, K and L attach to. **Rule 9 appears once and takes two
insertions**, G and L.
