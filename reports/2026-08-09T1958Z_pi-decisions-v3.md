# Execution report — replay the PI decisions and deferred-items task on the current base

Specification: `specs/2026-08-09T1958Z_pi-decisions-v3.md`
Pre-execution review: `reviews/chatgpt/2026-08-09T1958Z_pi-decisions-v3.md`
Specification evidence base: `7c5cba5df76de6ef8f52af390ca92100dcdf0d8b`
Branch: `fix/pi-decisions-v3`, cut from the evidence base
Approved source: `fix/pi-decisions-v2` @ `ebd531ab568aaffabd86a4a94d925a711e62aa36`
Pre-report head: `1deaf63c0a6b0440cd005c1c5a1f88002cb14ec4`

**Outcome.** The approved content is re-instantiated on the current base.
**No merge conflict arose, none was resolved, and no ordering between
independently appended histories was chosen.** All seven A1 pins and all
eleven §7 literal checks reproduce. **A4's normalisation function,
applied independently to the approved register and to this one, yields
byte-identical sequences**; the only pre-normalisation difference is the
`Authority:` line. Both append-only measures are zero, the two governance
entries on `main` are present and unaltered, and the three PI rulings
follow them. Four validators pass.

**Two things the Reviewer should read before the detail.**

**(a) §6 asks whether this specification told me how to represent a
stale-base replay without judgement. It did — §14 — and the one place
Amendment K fits only loosely is named there.**

**(b) A4's step 2 is vacuous on BOTH sides: 0 occurrences of a report
path in the source register and 0 in mine.** §5.2. **I did not
manufacture a report reference to give the step something to do.** The
specification anticipated this and said a vacuous substitution is not a
failure; I report the zero.

---

## 1. A11 — refs, read from the remote

    refs/remotes/origin/main    7c5cba5df76de6ef8f52af390ca92100dcdf0d8b
    remote refs/heads/main      7c5cba5df76de6ef8f52af390ca92100dcdf0d8b
    local  refs/heads/main      0f7961747abe2a18b436c0b1e5b928f425ea4d9a

Both remote refs resolve to the evidence base. **Local `main` is stale by
design and was not repaired.** No `main` ref was moved.

**`fix/pi-decisions-v3` did not exist before this task** —
`git ls-remote origin refs/heads/fix/pi-decisions-v3` returned zero refs
— so "create the new branch from that commit" was executable as written.

**`{HHMM}Z` is `1958` and `XX` is `09`**, fixed by commit 1 and reused.
**It differs from `0430` and `1416`**, so the three executions of this
task are distinguishable by path and no path collides.

## 2. A1 — pinned inputs, seven of them, verified before use

Method as specified: `git cat-file blob <rev>:<path> | sha256sum`, read
from the git objects at the evidence base. **All seven matched.**

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
      fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a   MATCH
    derivations/P2-PHASE-01_channel_character.md
      380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f   MATCH
    derivations/P2-PHASE-01_channel_character_layers.md
      4cea53a7163ccc6aadadd0fca276714c16d805ad8aed3594d64d66d412606711   MATCH
    results/P2-PHASE-01/channel-character-layers/layers.json
      fe343c74389cc996e42567d7dd510f479f1e7ed01cba81de61ff1d6f7e9d1542   MATCH
    reports/2026-08-05_p2-phase-01_scalar-stationary-exploratory.md
      70ab88eda32483420c0bfd522babd2ca4a73941bc2d2d20f8414976641756cbe   MATCH
    results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json
      a4537efad3b46e5e429b5310baad8b4dbf36d9c95582873dbfa0b03cc44d7028   MATCH
    derivations/P2-PHASE-01_scalar_stationary_exploratory.md
      80586e33ef07e307729af4597f72b48f6ecee74fc6a0f396b593f735ef322599   MATCH

**A1's account of the three-way split of `DEFERRED-02`'s evidence is
confirmed by observation.** In the pinned exploratory derivation note,
normalised:

    contains "7.59"          False
    contains "complement"    False   (case-insensitive)

**The note carries no roots, no curvatures and no complement relation.**
It carries the scope limitation, quoted in §4.3. **That is why all three
are pinned**, and it is what makes the "restricted, not stable"
narrowing verifiable from A1 rather than asserted.

## 3. §7 — the pre-issue literal verification record, re-run

**Check type as declared: NORMALISED SUBSTANTIVE — one function applied
to both sides.** Blockquote prefixes `> ` stripped, `**` and backticks
stripped, whitespace collapsed to single spaces, **en dashes preserved**.
Target: `DECISION_LOG.md` at `fix/pi-decisions-v2 @ ebd531ab…`.

    PASS count=3  'scalar channel with a real auxiliary field'
    PASS count=1  'This is a choice of direct route'
    PASS count=1  'It is deferred, not excluded'
    PASS count=1  'This does not close OPEN-AC-1'
    PASS count=1  'the programme evaluates both the'
    PASS count=1  'rather than selecting between them'
    PASS count=2  'depends on an unresolved sign convention'
    PASS count=2  'DEFERRED, not excluded'
    PASS count=1  'they do not establish full condensate-space stability, phase
                   admissibility, or absence of physical content'
    PASS count=1  'cannot by itself classify this branch as an unphysical lattice artifact'
    PASS count=1  "that criterion's quantifier range is undetermined"
    ALL ELEVEN REPRODUCE: True

**No target was adjusted.**

**§7's A4 source-side counts, re-run** against
`derivations/P2-DEFERRED-ITEMS.md` at `ebd531ab…`, blob
`ffeae5eb52115e131536e10508b72ac3ff51379d` (confirmed by
`git rev-parse ebd531ab:derivations/P2-DEFERRED-ITEMS.md`):

    specs/2026-08-09T1416Z_pi-decisions-v2.md      1 occurrence
    reports/2026-08-09T1416Z_pi-decisions-v2.md    0 occurrences
    residual 'pi-decisions-v2' after substitution  0
    residual '1416Z' after substitution            0

**All reproduce.** The distinction between these byte-exact checks — the
blob id and the seven SHA-256 digests — and the normalised substantive
checks above is preserved and not mixed.

## 4. A2 — evidence re-verified, not inherited

Every quotation was located afresh in the pinned material **at this
task's evidence base**, and separately confirmed present in the register
this task lands. **None was carried over on the strength of the earlier
approval.**

### 4.1 `DEFERRED-01`

**Located** in `derivations/P2-PHASE-01_channel_character_layers.md`
§3.2 — pinned `4cea53a7…`:

    channel                     g_L          g_P        sign(g)   real HS
    scalar_singlet_direct         G/N    2*G/N**2         +1        yes
    induced_V_singlet            -G/2       -G/N          -1        no
    induced_A_singlet            -G/2       -G/N          -1        no

Both induced rows verified present in the source and in the register.

**Located** in `results/P2-PHASE-01/channel-character-layers/layers.json`
— pinned `fe343c74…`, read as JSON:

    layer_1b.channels.induced_V_singlet.g_in_normalisation_L              "-G/2"
    layer_1b.channels.induced_V_singlet.real_linear_HS_field_admissible   false
    layer_1b.channels.induced_A_singlet.g_in_normalisation_L              "-G/2"
    layer_1b.channels.induced_A_singlet.real_linear_HS_field_admissible   false

**No stop.**

### 4.2 `DEFERRED-02` — the numerical findings

**Located** in `reports/2026-08-05_p2-phase-01_scalar-stationary-exploratory.md`
— pinned `70ab88ed…`:

> There is instead an exact Wilson-complement relation
> `I0(Mhat)=I0(-8-Mhat)`, induced by `p_mu -> pi-p_mu`; numerical
> differences for four checked pairs are at most `1.1e-16`. It relates
> algebraic roots but is not an `Mhat -> -Mhat` symmetry. Positive and
> negative roots are therefore not declared phase-equivalent.

and the three sub-critical rows, **each verified as a complete row of
the source table** in its source form, not only in the register's
re-columned form:

    | 0.80 | -7.589264 | -0.410736 | 0.417872 | -0.022615 | 0.021346 |
    | 0.90 | -7.813202 | -0.186798 | 0.400036 | -0.009564 | 0.009487 |
    | 0.98 | -7.966034 | -0.033966 | 0.404749 | -0.001725 | 0.001743 |

    columns: G/Gc | Mhat_left | Mhat_right | curvature(left) | curvature(right) | curvature(0)

**Corroborated** in
`results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json`
— pinned `a4537efa…`:

    symmetry.wilson_complement_relation
      "I0(Mhat) = I0(-8 - Mhat), from p_mu -> pi-p_mu; numerically checked below."
    symmetry.complement_pairs
      4 pairs, max |difference| = 1.1102230246251565e-16

### 4.3 `DEFERRED-02` — the scope limitation

**Located** in `derivations/P2-PHASE-01_scalar_stationary_exploratory.md`
— pinned `80586e33…`:

> Neither curvature is a full condensate-space Hessian or a
> phase-admissibility statement.

**This is the sentence that narrowed Decision 3** from "stable" to
positive restricted curvature. **All three parts of `DEFERRED-02`'s
evidence are in pinned material. No stop.**

### 4.4 `DEFERRED-03` — absence of evidence is content

    Status: PI HYPOTHESIS, UNTESTED.     present
    Evidence: none.                       present

**No lookup was attempted and none should be.**

## 5. A4 — substantive equivalence to the approved branch

### 5.1 Every differing line, BEFORE normalisation

`derivations/P2-DEFERRED-ITEMS.md`, approved source at `ebd531ab…`
against the file landed here:

    -Authority: `specs/2026-08-09T1416Z_pi-decisions-v2.md`.
    +Authority: `specs/2026-08-09T1958Z_pi-decisions-v3.md`.

    2 differing lines — one pair, one line

**That is the whole difference.** **My file is NOT blob-identical to
`ffeae5eb…`, and must not be**: A4 says so, because blob equality would
force the register to keep an `Authority:` pointer to a superseded
specification.

### 5.2 The occurrence counts, both sides, independently

    source  specs/2026-08-09T1416Z_pi-decisions-v2.md      1 occurrence
    source  reports/2026-08-09T1416Z_pi-decisions-v2.md    0 occurrences
    dest    specs/2026-08-09T1958Z_pi-decisions-v3.md      1 occurrence
    dest    reports/2026-08-09T1958Z_pi-decisions-v3.md    0 occurrences

**Step 2 is vacuous on both sides.** §7 predicted it might be, and it is:
neither register cites its task's report, because a register written at
commit 3 cannot cite a report committed at commit 4. **I did not add a
report reference to give step 2 something to substitute.** A vacuous
substitution is not a failure, and reporting the zero is the correct
result.

**Residual v2 identifiers in the destination: 0 `pi-decisions-v2`, 0
`1416Z`.**

### 5.3 The function applied independently, and the byte comparison

    for each text independently:
      1  replace the exact specification path identifying that execution
         with the literal token <TASK_SPEC>
      2  replace the exact report path identifying that execution, if
         present, with the literal token <TASK_REPORT>
      3  no other replacement, deletion, whitespace normalisation or
         reformatting

    <TASK_SPEC>    occurrences: source 1, destination 1
    <TASK_REPORT>  occurrences: source 0, destination 0

    resulting byte sequences IDENTICAL:  True
    normalised lengths:                  8344 and 8344

**The whole register matches byte for byte after canonicalisation.**
Every `DEFERRED` entry's status, reason, PI position, evidence,
evidence-strength qualification, blocks line and hypothesis wording is
inside that equality. **No substantive drift.**

### 5.4 The three `DECISION_LOG.md` rulings

**Compared under A4's stated normalisation for the rulings** — strip
`> `, strip `**` and backticks, collapse whitespace, keep en dashes —
applied to both sides.

**Every differing line, before normalisation — seven pairs, all inside
`### Related branch and files`:**

    -`fix/pi-decisions-v2`;                            (×3)
    +`fix/pi-decisions-v3`;
    -`specs/2026-08-09T1416Z_pi-decisions-v2.md`.      (×3, plus one
    +`specs/2026-08-09T1958Z_pi-decisions-v3.md`.       trailing-blank pair)

    14 differing lines, 7 pairs

**Under the stated normalisation the two strings are not identical**, and
the differences are exactly the digits of the task identity:

    replace '2' -> '3'        (branch suffix)      ×3
    replace '416' -> '958'    (the {HHMM} token)   ×3
    replace '2' -> '3'        (spec suffix)        ×3

**Adding A4's task-identity canonicalisation — the specification path and
the branch name — makes them identical.** Reported this way, rather than
by extending the function myself, because **A4 defines the function for
the register and prescribes only the textual normalisation for the
rulings.** The branch name is a task-identity token the function does not
name; I report the difference and its reason rather than normalising it
away silently.

**Every difference is a task-identity pointer.** No ruling's substantive
text differs by a character.

## 6. A5 — required phrases, against the destination

Same normalisation, run here against the landed `DECISION_LOG.md`
rulings, not inherited from §3:

    PASS count=3  'scalar channel with a real auxiliary field'
    PASS count=1  'This is a choice of direct route'
    PASS count=1  'It is deferred, not excluded'
    PASS count=1  'This does not close OPEN-AC-1'
    PASS count=1  'the programme evaluates both the'
    PASS count=1  'rather than selecting between them'
    PASS count=2  'depends on an unresolved sign convention'
    PASS count=2  'DEFERRED, not excluded'
    PASS count=1  'they do not establish full condensate-space stability, phase
                   admissibility, or absence of physical content'
    PASS count=1  'cannot by itself classify this branch as an unphysical lattice artifact'
    PASS count=1  "that criterion's quantifier range is undetermined"
    ALL PRESENT: True

**Every required phrase is inside the verbatim ruling text. No ruling was
edited, and none needed to be.** The en dash in `Hubbard–Stratonovich`
was confirmed `U+2013` and not normalised away.

## 7. A6 — append-only, on both measures, with the governance entries shown

**Measure 1 — evidence base to branch head:**

    git diff --numstat 7c5cba5d… 1deaf63c…
      256     0       DECISION_LOG.md
      193     0       derivations/P2-DEFERRED-ITEMS.md
       78     0       reviews/chatgpt/2026-08-09T1958Z_pi-decisions-v3.md
      412     0       specs/2026-08-09T1958Z_pi-decisions-v3.md

    deleted lines across the whole diff:  0

**Measure 2 — each commit against its parent:**

    a44c2b0   deletions=0    specs/…
    071c3c1   deletions=0    reviews/chatgpt/…
    1deaf63   deletions=0    DECISION_LOG.md, derivations/P2-DEFERRED-ITEMS.md

**Both zero.** `DECISION_LOG.md` is written once, by one commit, and never
revisited. **The head has the base as an exact byte prefix**, with 10605
characters appended.

### 7.1 The two governance entries, present and unaltered

Compared as byte slices between the evidence base and the branch head:

    line 1519   ## 2026-08-09 — `CONVENTIONS.md` amendments A–D adopted;
                Rules 14 and 15 added
                present: True    unaltered: True

    line 1625   ## 2026-08-09 — `CONVENTIONS.md` amendments E–L adopted;
                Rules 16 and 17 added
                present: True    unaltered: True

### 7.2 The three PI rulings, appended after them

    line 1749   ## 2026-08-09 — Mean-field channel for `P2-PHASE-01`: the
                scalar channel with a real auxiliary field
    line 1827   ## 2026-08-09 — The charge-conjugation phase `eta` is not
                selected; both signs are computed
    line 1907   ## 2026-08-09 — The negative-mass stationary branch is
                DEFERRED, not excluded

    all three appear after both governance entries:  True
    top-level entries:  27 at the base  ->  30 at the head

**That order records entry into the authoritative lineage, not a decision
date.** All three rulings remain dated `2026-08-09`; no decision date is
altered, and no entry on either side is moved, reordered or rewritten.
**Nothing chose between two orderings, because nothing had to** — the
branch was cut from the base that already carried the governance
entries.

## 8. A3 — this task's pre-execution review, committed unedited before the work

    reviews/chatgpt/2026-08-09T1958Z_pi-decisions-v3.md
      committed blob sha256
        aef3d920b7e6e6c3c8c9d8063928d5d164489647a80cd6c68735998ca400bbab
      git blob id
        eb77adfb19f288df2a64cdf76cb3b4f5a8185fd9
      78 lines

**Committed as commit 2, before the work in commit 3** — Rule 15's timing
clause, and A0's frozen order.

**Exactly what I did.** The text was supplied between two delimiter
lines. **The delimiter lines and the instruction accompanying them are
excluded**, per A3. Blank lines adjoining the delimiters were dropped and
the file ends with exactly one newline. **No character of the review's
own content was added, removed or altered**, verified by comparing the
committed blob to the extracted text.

**No placeholder was resolved in the body.** The review contains none
requiring it; the path token was resolved in the filename only.

**It corresponds to this specification**, checked rather than assumed. It
names the specification by title; it cites the evidence base
`7c5cba5df76de6ef8f52af390ca92100dcdf0d8b`, the approved source
`ebd531ab568aaffabd86a4a94d925a711e62aa36`, the register blob
`ffeae5eb52115e131536e10508b72ac3ff51379d` and the v2 authority line
`Authority: specs/2026-08-09T1416Z_pi-decisions-v2.md` — **all four of
which §1, §3 and §5 reproduce independently.** It addresses A4's revised
normalisation function, A6's append-only construction, the Rule 15
lifecycle and the Rule 16 requirement. **Disposition: APPROVED /
ISSUABLE.**

**The review's own limits, honoured.** It records that it did not execute
the task, did not reproduce the seven A1 digests, the A2 quotations, the
eleven A5 phrase checks, the A4 comparison, the A6 measures, the A7
reachability checks, the A8 comparison, the A9 scope check or the A10
validators, and that **its approval converts no unexecuted acceptance
criterion into a PASS.** §2 through §11 are those executions.

## 9. A7 — superseded branches untouched

Read from the remote before the push:

    refs/heads/fix/pi-decisions-and-deferred   52f651174dc1fef03b4fb9276078fa1f08d94bd7
    refs/heads/fix/pi-decisions-v2             ebd531ab568aaffabd86a4a94d925a711e62aa36

    59c763ab… reachable in fix/pi-decisions-and-deferred:  YES
    52f65117… reachable in fix/pi-decisions-and-deferred:  YES

**`fix/pi-decisions-v2` is at its recorded value**, and both earlier
execution commits remain reachable. **Nothing was touched, reset,
rewritten or force-pushed; no branch was deleted.** The post-push
re-verification is post-report evidence.

## 10. A8 — nothing else touched

    GATES.md          bd48205…  IDENTICAL
    CONVENTIONS.md    0db56c39…  IDENTICAL
    AGENTS.md         5e60b5f…  IDENTICAL
    pyproject.toml    9fc6fdd…  IDENTICAL

**Every path under `scripts/`, `results/`, `tests/`, `derivations/`,
`docs/` and `reviews/` that exists at the evidence base**, enumerated
from the base and compared one by one — **not as tree objects**, since
`reviews/` gains a path and `derivations/P2-DEFERRED-ITEMS.md` does not
exist at the base:

    185 pre-existing paths checked, 0 differ

and the only changes to those directories, both additions of paths absent
at the base:

    A   derivations/P2-DEFERRED-ITEMS.md
    A   reviews/chatgpt/2026-08-09T1958Z_pi-decisions-v3.md

**No existing review record was modified or back-filled.**
**`scripts/p2_channel_character_layers.py` is inside the 185 and is
identical** — Amendment L's known instance is untouched and no
conventions-index entry was added.

**No gate status changed.** `GATES.md` blob-identical, `^## P2-` anchor
count 14, **`P2-GAP-01` still `PASS`, `P2-PHASE-01` still `PROPOSED`.**

**Nothing was computed.** No script was run against repository data other
than the governance tools and `pytest`; the diquark calculation Decision
2 authorizes was not performed. **The SI-1 cross-reference was not
added.**

## 11. A9 — scope, and A10-pre

### 11.1 Scope

**Manifest template** (SHA-256
`27f14b9c775f240ec7ade9d75171c6df1de19c497bd25bd710e002c4991528c0`):

    {
      "base": "7c5cba5df76de6ef8f52af390ca92100dcdf0d8b",
      "head": "{PUSHED_HEAD}",
      "mode": "exact",
      "required": [
        {"operation": "add", "path": "specs/2026-08-09T1958Z_pi-decisions-v3.md"},
        {"operation": "add", "path": "reviews/chatgpt/2026-08-09T1958Z_pi-decisions-v3.md"},
        {"operation": "add", "path": "derivations/P2-DEFERRED-ITEMS.md"},
        {"operation": "add", "path": "reports/2026-08-09T1958Z_pi-decisions-v3.md"},
        {"operation": "modify", "path": "DECISION_LOG.md"}
      ],
      "optional": [],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

**Intended final resolution:** `head` set to the pushed head, all five
records required — **4 additions and 1 modification.** A sixth path would
be a defect.

**Pre-report scope check** at `1deaf63c…`, with the report record removed
because the report does not yet exist — checker output verbatim:

    {
      "base": "7c5cba5df76de6ef8f52af390ca92100dcdf0d8b",
      "failures": [],
      "head": "1deaf63c0a6b0440cd005c1c5a1f88002cb14ec4",
      "mode": "exact",
      "observed_operations": [
        {
          "operation": "modify",
          "path": "DECISION_LOG.md"
        },
        {
          "operation": "add",
          "path": "derivations/P2-DEFERRED-ITEMS.md"
        },
        {
          "operation": "add",
          "path": "reviews/chatgpt/2026-08-09T1958Z_pi-decisions-v3.md"
        },
        {
          "operation": "add",
          "path": "specs/2026-08-09T1958Z_pi-decisions-v3.md"
        }
      ],
      "overall": "PASS",
      "tool": "scope_checker"
    }

    exit status 0

**The final scope check at the pushed head is post-report evidence.**

### 11.2 A10-pre — validators at the pre-report head

Run individually with `python -m pytest <path>`, that exact invocation,
since `pytest` on this host resolves to 9.0.2 while `python -m pytest`
resolves to 9.1.1.

    tests/test_repository_structure.py    exit=0    4 passed
    tests/test_si1_governance.py          exit=0   14 passed
    tests/test_gate_anchors.py            exit=0   18 passed, 2 deselected
    tests/test_governance_tools.py        exit=0    8 passed

`pytest 9.1.1`, Python 3.11.15. **Under Rule 14** each is a PASS on the
full contract: the process started, completed without timeout or external
termination, returned exit 0, and no test, collection or teardown phase
was skipped or aborted. The two deselections are the file's own marker
configuration, present identically at the base. **A10-final at the pushed
head is post-report evidence.**

## 12. A0 — commit order, SHAs and messages

    commit 1  a44c2b053b54d90a1acb8cfe57daa8a458b4521d
              specs/2026-08-09T1958Z_pi-decisions-v3.md
              committed content sha256
                6d317c8ff05f6f0e065ea2ec25893f729fa64124271fb81d936b22bce92e5835
              "spec: replay the PI decisions and deferred-items task on the current base"

    commit 2  071c3c16515a8ffdb174e8585773d6a7b9ef335c
              reviews/chatgpt/2026-08-09T1958Z_pi-decisions-v3.md
              "review: pre-execution review of the PI decisions v3 replay"

    commit 3  1deaf63c0a6b0440cd005c1c5a1f88002cb14ec4
              DECISION_LOG.md, derivations/P2-DEFERRED-ITEMS.md
              "docs: record three PI decisions and open the deferred-items register"

**Commit 2 precedes the work in commit 3**, per Rule 15's timing clause.

**The specification's sha256 is recorded because Rule 4 requires it** —
the execution prompt committed *and* its digest in the run's report.

**The specification file is byte-identical to the specification as
supplied**, 412 lines.

### Commit-message hygiene

Each message was written to a file, inspected for `Co-Authored-By`,
`Claude-Session`, `claude.ai`, `Generated with` and `http` before
committing, committed with `git commit -F <file>` and never `-m`, and the
stored message read back from the object afterwards.

    commit 1   trailers suppressed: Co-Authored-By, Claude-Session
    commit 2   trailers suppressed: Co-Authored-By, Claude-Session
    commit 3   trailers suppressed: Co-Authored-By, Claude-Session

**Suppression is a fact to disclose, not an absence.** The intended
report commit message was prepared the same way, with the same two
suppressed:

    docs: report the PI decisions v3 replay on the current base

    Records the fourth execution of the approved content, on a branch cut
    from the current evidence base under a new task identity. All seven
    pins and all eleven literal checks reproduce; every evidence
    quotation was re-located in the pinned material rather than
    inherited.

    A4's normalisation function, applied independently to the approved
    register and to this one, yields byte-identical sequences; the only
    pre-normalisation difference is the Authority line. Step 2 is vacuous
    on both sides and is reported as zero rather than given something to
    do. The three rulings differ only in seven task-identity pointer
    lines.

    Both append-only measures are zero, the two governance entries on
    main are present and unaltered, and the three PI rulings follow them
    — an order that records entry into the authoritative lineage, not a
    decision date.

    Reports that the specification required no judgement about how to
    represent a stale-base replay, and names the one place Amendment K
    fits this case only loosely.

## 13. §3 — the accumulated-reading assessment, under Rule 16

**Rule 16 is operative at this evidence base and governs this task.**

### 13.1 The candidate junction, confirmed and sharpened

**§3 offers:** four executions of this task now exist — `59c763ab`,
`52f65117`, `ebd531ab` and this one, each preserved — and a reader could
conclude the content was revised three times. **It was revised once, on
substance.**

**I confirm the junction and can now say exactly what the record shows**,
because §5 measured it:

    59c763ab -> 52f65117   SUBSTANCE. Decision 3 narrowed from "stable"
                           to positive restricted curvature; A1 gained
                           the two artifacts carrying DEFERRED-02's
                           evidence.
    52f65117 -> ebd531ab   REPRESENTATION ONLY. Seven task-identity
                           pointer lines; substance byte-identical after
                           canonicalisation.
    ebd531ab -> this       BASE ONLY. One task-identity pointer line in
                           the register, seven in the rulings; the
                           register is byte-identical after the A4
                           function.

**The one substantive revision is between the first and second
executions, and nothing since has changed a word of the decisions.**

### 13.2 What the assembled set does NOT establish

1. **That the content was reviewed four times.** It was approved once on
   substance; the later executions were re-issues about representation
   and base, and their reviews addressed the re-issue mechanism, not the
   decisions.
2. **That any of the three PI decisions has been acted on.** All three
   are recorded; none is executed. Decision 2 authorizes a two-sign
   diquark calculation that has not been performed, and this task is
   forbidden from performing it.
3. **That `DEFERRED-02`'s `Blocks:` line has been addressed.** It states
   that the SI-1 kill criterion's quantifier range is undetermined. **It
   has now survived four executions of this task and is still referenced
   from nowhere but the register** — `GATES.md` does not point at it, and
   `GATES.md` is protected in every one of these specifications.
4. **That the branch is integrable.** It is not integrated; integration
   is a separate authorization, and the reason this replay exists is that
   integrability, not content, lapsed.

**The limitation whose omission would most change the natural reading is
(1)**, and it is the one §3 named.

### 13.3 A stronger junction, offered as an addition rather than a replacement

**§3's junction is about this task's own history. There is a second, and
it spans tasks.**

    derivations/P2-DEFERRED-ITEMS.md   DEFERRED-01 records that the V/A
                                       representation is deferred, not
                                       excluded, on g_V = g_A = -G/2
    DECISION_LOG.md 2026-08-09         the scalar channel is selected for
                                       mean-field work
    results/…/channel-character-layers/layers.json
                                       the induced V and A singlets are
                                       REPULSIVE and admit no real linear
                                       HS field

**The inference their combination makes available:** *the V/A sector has
been examined and set aside on physical grounds.*

**It has not.** DEFERRED-01's own PI position says the opposite — the V/A
representation "may contain physically relevant information and must be
returned to", and "no evidence indicates it is unphysical". **The
deferral is about which machinery exists, not about which physics is
right.** The three artifacts are individually careful; the assembled
reading is not available from any one of them.

**I report this in addition to §3's, not instead of it**, because §3's
concerns how to read the repository's history and this one concerns how
to read its physics — and the second is the one a downstream paper could
act on.

## 14. §6 — did this specification tell me how to represent a stale-base replay?

**Yes. No judgement was required and I invented no construction.**

**What made it executable, item by item.**

- **§0 states the cause and the resolution together** — the dry-run
  conflict, why it was not resolved by hand, and that this is a replay
  rather than a repair. **The reason given is not "it would be
  non-append-only"** — §0 says explicitly that keeping every entry from
  both sides would itself have been append-only — **but that it would
  create an authority to order two independently authored sets of
  entries.** That distinction is what makes the instruction followable
  rather than merely obeyed.
- **§1 gives the construction outright**: new branch from the current
  base, new task identity, superseded branch preserved, approved content
  re-instantiated.
- **A0 forbids the two used tokens and says why.**
- **A4 defines the normalisation as a FUNCTION**, and §5.3 is that
  function executed. **The earlier version described permitted
  differences; this one is executable**, which is the difference
  Amendment H names.
- **A4 states that blob equality would be wrong and why**, so the one
  place where the replay must differ from the approved artifact is
  authorised in advance rather than discovered.
- **§7 records the source-side counts and warns that step 2 may be
  vacuous on both sides**, which is exactly what §5.2 found. **Without
  that sentence, a zero would have looked like a failed check.**
- **§5's environment clause tells me to say neither Rule 13 order was
  exercised if no failure occurs**, rather than naming one. §16 does
  that.

### 14.1 Where Amendment K fits this case only loosely

**§6 asks, and this is the answer worth having.**

**K's stated case is a specification that has already been executed and
pushed being re-issued.** Its trigger is that **the specification was
corrected** — K's incident is a re-issue after defects were found, and
its remedy is a new branch under a new task identity so the two
executions do not collide on the same paths.

**This case has a different cause.** **The specification was not
corrected and the content was not defective.** `ebd531ab` remains
approved. What changed is outside the task entirely: `main` advanced, and
the branch stopped being conflict-free.

**Three consequences of that difference:**

**(a) K's "superseded" carries a connotation this case does not have.**
K says the original branch "is identified as superseded". §1 is careful
to write **"superseded for integration, preserved, not carried forward …
Its content remains APPROVED; only its integrability lapsed."** **That
qualification is the specification's, not K's.** A reader applying K
alone would record `ebd531ab` as superseded and lose the distinction.

**(b) K's prohibition on integrating a superseded branch reads
differently here.** K forbids it because two branches would claim to land
the same entries. **That reason holds. But the accompanying implication —
that the superseded branch was wrong — does not**, and nothing in K
separates the two.

**(c) K's re-issue is triggered by the executor or reviewer finding a
defect; this one is triggered by the passage of time.** **Nothing in K
tells anyone to look.** A branch can become non-integrable silently, and
the only reason this was caught is that someone ran a dry-run merge.

**What I would add to K**, offered as observation and not as a change I
am authorised to make: **a named subclass for loss of conflict-free
integrability**, stating that the content remains approved, that the
branch is superseded for integration only, and that **an approved branch
should be dry-run merged against the current base before an integration
is authorised** — which would turn a silent lapse into a detected one.

**§0 says "If K is ever revised, this class belongs in it explicitly."**
**I agree, and (c) is the part I would not want lost**: the class needs a
detection step, not only a construction.

## 15. Stops and clarifications

**No stop occurred.**

### `SPECIFICATION_DEFECT`

**None.** Every criterion was satisfiable as written. The two places an
earlier version was blocking — A4's blob-equality requirement and its
description-instead-of-function — are both corrected in the issued text,
and §5 executes the corrected form.

### `ENVIRONMENT`

None. Nothing was installed.

**No environment failure occurred, so neither of Rule 13's two
diagnostic orders was exercised.** §5 of the specification asks me to say
that rather than name one, and naming one would assert a procedure I
never ran — which is what Amendment E exists to prevent.

### `OBSERVATION_METHOD_ERROR`

**None reached an output. One was caught during execution**, and it is
the same class as the one recorded at the previous integration.

My first extraction of the review artifact located the delimiters with
`text.index("=== REVIEW ARTIFACT BEGINS ===")`. **That matched the
delimiters' first mention — inside the accompanying instruction sentence,
which names both in prose** — and returned a four-character fragment.

**The two available readings were "the artifact is nearly empty" and "my
locator matched the wrong occurrence."** The second was correct. The
extraction was redone by requiring each delimiter to be **a line of its
own**, which found exactly one of each at lines 5 and 86, and the
boundaries were printed and checked before anything was written. **No
file was created by the failed attempt.**

**This is the second occurrence of this exact error**, and the cause is
the same both times: the accompanying instruction quotes the delimiters
it is describing. **The fix is mine to make once — always locate a
delimiter as a whole line — and I have now made it twice.**

### `REPOSITORY_DEFECT`

None.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`

**None that blocked.** One recorded in §5.4: A4 defines the
task-identity function for the register and prescribes only a textual
normalisation for the rulings, so the rulings' **branch-name** token is
not covered by either. **I reported the difference and its reason rather
than extending the function myself**, which would have been supplying a
construction the specification does not describe.

## 16. Secondary findings, and what I would have specified differently

**1. An approved branch can stop being integrable without anyone
looking.** §14.1(c). This one was caught by a dry-run merge that nothing
required. **A check that dry-run merges every approved-but-unintegrated
branch against the current `main` would turn a silent lapse into a
detected one**, and it is cheap. There is currently one such branch left
in this state — `fix/pi-decisions-and-deferred` @ `52f65117` — whose
integrability nobody has tested since `main` advanced twice.

**2. `DEFERRED-02`'s `Blocks:` line has now survived four executions
unreferenced.** §13.2(3). It states a live constraint on a future gate
specification — SI-1's quantifier range — and is discoverable only from
the register. **`GATES.md` is protected in every one of these
specifications**, so the cross-reference cannot happen as a side effect
and needs its own authorization.

**3. The delimiter-quoting problem should be fixed in the supply format,
not only in my locator.** §15. Twice now, an instruction has named the
delimiters it describes, and twice a first-occurrence search has found
the wrong one. **A supply convention — the delimiters appear only as
their own lines, and the instruction refers to them without reproducing
them — would remove the trap** rather than relying on the executor
remembering.

**4. Amendment L's obligation still has no assignee**, and this task
confirmed the instance is untouched (§10). Raised at the E–L landing and
at its integration; unchanged.

**5. What I would have specified differently — A4 should name the branch
token.** §5.4. The function covers the specification path and the report
path; the rulings also carry the branch name, which is task identity by
exactly the same argument. **Adding it as step 1b would let the rulings
be compared byte-for-byte after canonicalisation**, the same standard A4
already applies to the register, instead of leaving a textual difference
for the report to explain.
