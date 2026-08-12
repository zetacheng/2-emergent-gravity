# Task report — supply protocol v2: STOPPED at A3, before any governance file was touched

Specification:        `specs/2026-08-12T0111Z_supply-protocol-v2.md`
Pre-execution review: `reviews/chatgpt/2026-08-12T0111Z_supply-protocol-v2.md`
Specification evidence base: `0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5`
Branch:               `governance/supply-protocol-v2`
Pre-report head:      `da88a4d15087c4495ccd05cda4f5337bc7ac0ae6`
UTC token `{HHMM}Z`:  `0111`, fixed by commit 1; `XX` = `12`; **differs from
                      `2337`** as A0 requires

## STOP

**`A3` and `§0` cannot both be satisfied. Primary category:
`SPECIFICATION_DEFECT`.**

**A3 requires the landed Rule 18 to contain "the delimiter literals and
the blank-line clause". The Rule 18 that §0 directs to be landed
contains neither, and abandons both by design.** Measured against the
committed specification blob, not read from memory:

    delimiter literal "=== REVIEW ARTIFACT BEGINS ===" present : False
    delimiter literal "=== REVIEW ARTIFACT ENDS ==="   present : False
    any occurrence of "REVIEW ARTIFACT"                        : 0
    blank-line clause ("leading blank line") present           : False
    any occurrence of "blank line"                             : 0

**§6 is the operative instruction, and it is unconditional:** *"If any
instruction here is inconsistent with a repository rule or with another
instruction, stop and report; do not decide which prevails."*

**`CONVENTIONS.md`, `docs/BRANCHING_POLICY.md` and `DECISION_LOG.md` were
not touched.** A0's commit 3 was not made. No `main` ref was moved.

**This stop is the direct lesson of the branch this task supersedes.**
The re-issue header says of `governance/supply-protocol-and-superseded @
7146a093…`: *"A2 required applying Rule 18; Rule 18 forbade the only
available action. **That is an inconsistency between instructions, and
the standing invariant says to stop.** The executor did not."* **The same
class of inconsistency is present in this issue, at A3.** Having been
told that resolving one silently was the error, I have not resolved this
one.

---

## 1. What was completed before the stop

**Everything the inconsistency does not touch**, so that a re-issue
inherits verified ground rather than repeating it.

| criterion | result |
|---|---|
| A0 commits 1–2 | done, in order, at the frozen paths; token `0111` ≠ `2337` |
| A1 pinned inputs | **both match** |
| A2 review supplied as a file, committed byte-unchanged | **done, digests equal** |
| A6 register membership | **all five entries verified; 49 branches enumerated; no additions** |
| A10-pre validators | **all four exit 0** |
| A11 branch only | **verified; no `main` ref moved; no branch deleted** |
| A12 hygiene | **clean on every commit made** |
| A3, A4 | **NOT EXECUTED — the stop** |
| A5, A7 | **NOT EXECUTED — entangled in A0's frozen commit 3** |
| A9 | **cannot reach 3 additions + 3 modifications — a consequence of the stop** |

## 2. A1 — Pinned inputs, verified before use

Method as specified, at `0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5`:

```
e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451  -   CONVENTIONS.md
0ba1e2a006d287800d19b1bfadb5fe24f4bda72dedaf38ad3289ddfa700b9da9  -   docs/BRANCHING_POLICY.md
```

**Both match A1's pinned values. No STOP on A1.**

## 3. A11 — Branch only

```
local  refs/heads/main        0f7961747abe2a18b436c0b1e5b928f425ea4d9a
remote-tracking origin/main   0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
remote refs/heads/main        0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
evidence base                 0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
```

All three reported. **`refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to the evidence base.** **Local `main` is
stale by design and was not repaired.** The branch was created from the
evidence base, clean:

```
Preparing worktree (new branch 'governance/supply-protocol-v2')
HEAD is now at 0ab6369 docs: report the landing of the diquark line
head: 0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
branch: governance/supply-protocol-v2
dirty: 0
```

**No branch was deleted.** **`governance/supply-protocol-and-superseded @
7146a093…` was not touched, reused or deleted** — verified in §5. No PR,
no force-push, no history rewrite, no merge into `main`.

## 4. A2 — The review, and whether Rule 18 was sufficient

### The mechanics

```
supplied file  : d026723c68037ca164734b4d032a6b7f7e60092c4073ab3c2f2d46c47adaadea
staged copy    : d026723c68037ca164734b4d032a6b7f7e60092c4073ab3c2f2d46c47adaadea
committed blob : d026723c68037ca164734b4d032a6b7f7e60092c4073ab3c2f2d46c47adaadea
```

**All three equal.** 27 lines, 2950 bytes, committed at
`reviews/chatgpt/2026-08-12T0111Z_supply-protocol-v2.md`.

**Correspondence verified before committing.** The review's line 1 is
`# Pre-execution review — supply protocol v2`, which identifies this
specification by task name — A2's stated alternative to a digest. It
reviews this specification's actual content: the file-supply replacement,
the superseded attribute's orthogonality to the deletion states, the
revised membership threshold, and Rule 18's first live test. **Not a
different specification. No STOP on correspondence.**

Supply-integrity checks on the file as received:

    occurrences of "REVIEW ARTIFACT"            0
    lines beginning with an attachment marker   0

### Was Rule 18 sufficient? **Yes — and this is the first time the answer
has been yes.**

A2 and §7 ask three specific questions. Answering each exactly:

- **Did the review arrive as a file?** **Yes.** At
  `…/56239d13-supply_protocol_v2_pre_execution_review.md`. Not pasted.
- **Did its bytes reach the commit unchanged?** **Yes**, by SHA-256 at
  three points: as supplied, as staged, and as stored in the Git object.
  **No extraction, no delimiter search, no normalisation, no stripping of
  anything.**
- **Did ANY step require a judgement of any kind?** **No.** There was no
  boundary to locate, so none could be inferred. `cp` and a digest
  comparison are the whole procedure. **The correspondence check is the
  one remaining act of verification, and it is a check with a stated
  criterion, not a judgement about bytes** — "identify the specification
  by digest or task name" either holds or it does not, and here it holds
  by task name on line 1.

**The residual judgement that eight previous supplies left, and that the
first issue of this task left, is gone.** Not narrowed — gone, because
the object it operated on no longer exists.

**One observation the next task should have, since §7 asks for anything
still incomplete.** **The specification itself arrived as pasted text,
not as a file** — including this task's, whose line 0 again carried the
attachment marker fused to the title. **Rule 18 as drafted explicitly
permits that** ("The specification may be supplied either way — it is
instruction, not an artifact committed byte-for-byte"), so this is
compliant, not a defect. **But A0 commit 1 requires the specification to
be committed at a frozen path**, which means an artifact *is* being
created from pasted text. I transcribed it faithfully and it is
committed; **its bytes are my transcription, not the sender's file**, and
no digest can attest that they match, because there is no supplied file
to compare against. **The asymmetry is worth closing** — supplying the
specification as a file too would make commit 1 verifiable in the same
way commit 2 now is. **It is not a stop**: the rule authorises the paste
and denies the specification byte-authority.

**The trade §0 names is real and I confirm it from execution.** The
review's text did not appear in the conversation. **I could verify its
integrity but not that the PI had read it.** The correspondence check is
a weaker substitute than visibility, exactly as §0 says. Recording it as
observed, not as an objection.

## 5. A6 — Register membership determined

### The five supplied entries, verified from `git ls-remote`

```
fix/pi-decisions-and-deferred                 52f651174dc1  MATCHES  not an ancestor of main
fix/pi-decisions-v2                           ebd531ab568a  MATCHES  not an ancestor of main
governance/supply-protocol-and-superseded     7146a093c657  MATCHES  not an ancestor of main
review/role-model-and-executors               10c260b96882  MATCHES  not an ancestor of main
gate/p2-land-diquark-line                     d64cd912ca9f  MATCHES  not an ancestor of main
```

**All five present at exactly the stated commits; none is an ancestor of
`main`. No STOP.** `fix/pi-decisions-v3` @ `93de3218…` **is** an ancestor
of `main` — the surviving instance, correctly absent from the register.

**`review/role-model-and-executors` is now supplied as a member, and its
tip is unchanged at `10c260b9…`.** §1's revised threshold — *"The
artifact must record the FACT, not use a particular WORD"* — resolves the
exclusion the first issue reported under
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`, in the direction that
report recommended. **The evidence was already gathered and needed no
re-litigation**; only the threshold changed. Its existing "permanently
preserved" disposition is untouched, as §1 requires — **nothing in this
task edited `docs/BRANCHING_POLICY.md` at all.**

### Enumeration of all 49 remote branches

**Re-run under the revised threshold**, because a relaxation from
"explicitly records" to "records the FACT" can admit branches a stricter
scan dismissed. Two independent methods, agreeing.

**Method 1 — relaxed vocabulary scan.** Every one of the 325 tracked
files at the evidence base was decoded and searched for each of the 49
branch names; every hit was tested in a ±8-line window against a
vocabulary **widened beyond the first issue's** to include exactly the
class the relaxation admits:

    supersed | re-issu | replac | rebuil | abandon | obsolet | withdraw
    regenerat | successor | re-instantiat | instead of | clean rebuild
    preserved untouched | not (to be) integrated

**Method 2 — integration status.** A branch that is an ancestor of `main`
was integrated, so it cannot be "preserved as evidence rather than for
integration". **Topology is used only to EXCLUDE, never to include**, as
§1 requires.

```
remote branches: 49
ancestors of main: 44   non-ancestors: 5
non-ancestors: ['fix/pi-decisions-and-deferred', 'fix/pi-decisions-v2',
                'gate/p2-land-diquark-line',
                'governance/supply-protocol-and-superseded',
                'review/role-model-and-executors']
```

**The five non-ancestors are exactly the five supplied register entries.**
The two methods coincide with no residue.

Per-branch result, all 49:

| branch | tip | ancestor of `main` | relaxed hits | classification |
|---|---|---|---|---|
| `main` | 0ab6369a | yes | 155 | not a candidate |
| `claude/paper-2-independent-verification-dysdp0` | 5395d4b3 | yes | 5 | integrated; false positive |
| `concepts/p2-dual-pipeline` | 9ee30ab3 | yes | 0 | integrated |
| `docs/canonical-interaction` | 78872798 | yes | 1 | integrated; false positive |
| `explore/p2-phase-01-scalar` | a2ed2af8 | yes | 0 | integrated |
| `fix/branch-deletion-policy` | f2da41ae | yes | 0 | integrated |
| `fix/branch-deletion-policy-amendment` | 1c106372 | yes | 0 | integrated; an amendment, not a replacement |
| `fix/exponent-mapping-ruling` | 79399dfd | yes | 0 | integrated |
| `fix/freeze-checker-sign-repair` | 0ab0ca9d | yes | 0 | integrated |
| `fix/integrate-si1-crossref` | 8701a97a | yes | 0 | integrated |
| `fix/normalisation-audit-g-omega` | 9c6ff5b3 | yes | 0 | integrated |
| `fix/pi-decisions-and-deferred` | 52f65117 | **no** | 4 | **REGISTER MEMBER** |
| `fix/pi-decisions-v2` | ebd531ab | **no** | 8 | **REGISTER MEMBER** |
| `fix/pi-decisions-v3` | 93de3218 | yes | 6 | surviving instance; NOT superseded |
| `fix/si1-deferred-02-crossref` | 38302141 | yes | 1 | integrated; false positive |
| `gate/p2-attraction-ruling-and-layers` | 878b632c | yes | 1 | integrated; *verdicts* superseded, not a branch |
| `gate/p2-betav-campaign-prereg` | 21efcf85 | yes | 0 | integrated |
| `gate/p2-betav-circ` | ca334fe0 | yes | 3 | integrated; "successor HEAD", see below |
| `gate/p2-betav-cleanup` | 602569db | yes | 0 | integrated |
| `gate/p2-betav-decomp` | 05a1e7f8 | yes | 2 | integrated; observed-SHA record |
| `gate/p2-channel-character` | cb604a4e | yes | 0 | integrated |
| `gate/p2-channel-freeze` | 47e271bb | yes | 0 | integrated |
| `gate/p2-chirality-census` | e4bea1c9 | yes | 0 | integrated |
| `gate/p2-diquark-adjudication` | 3767973b | yes | 6 | integrated; hits describe its landing |
| `gate/p2-diquark-both-eta` | bc1e5c74 | yes | 6 | integrated; hits describe its landing |
| `gate/p2-generator-sum-criticality` | 84aad96d | yes | 0 | integrated |
| `gate/p2-governance-amendment` | d63f33b9 | yes | 0 | integrated |
| `gate/p2-grassmann-crossing-sign` | cf4c7895 | yes | 0 | integrated |
| `gate/p2-integrate-chirality-census` | 57c5a6eb | yes | 0 | integrated |
| `gate/p2-land-diquark-line` | d64cd912 | **no** | 9 | **REGISTER MEMBER** |
| `gate/p2-land-diquark-line-v2` | 0ab6369a | yes | 5 | the replacement; *is* `main` |
| `gate/p2-lattice-ontology-01` | edb08c2a | yes | 0 | integrated |
| `gate/p2-phase-01-fierz-and-branch-depths` | dca52269 | yes | 0 | integrated |
| `gate/p2-si1-unblock` | c1f1bec2 | yes | 2 | integrated; merge record, branch intact |
| `governance/adopt-rules-8-12` | 75c84226 | yes | 0 | integrated |
| `governance/execution-environment-refinements` | 99aaa0e2 | yes | 0 | integrated |
| `governance/land-amendments-e-to-l` | c58f1b91 | yes | 0 | integrated |
| `governance/land-rules-14-15` | e045ee00 | yes | 0 | integrated |
| `governance/p2-phase-dependency-ruling` | d69bc0f7 | yes | 1 | integrated; false positive |
| `governance/rules-8-12-tools` | 376ec62f | yes | 0 | integrated |
| `governance/supply-protocol-and-superseded` | 7146a093 | **no** | 0 | **REGISTER MEMBER** |
| `governance/supply-protocol-v2` | this branch | no | 0 | this task; not a candidate |
| `recover/batch2-gfvec-and-foundations` | 324ef969 | yes | 0 | integrated |
| `recover/betav-complete` | 836bf144 | yes | 0 | integrated |
| `recover/lattice-gravity-engine` | cdcbd840 | yes | 1 | integrated; `MIGRATION.md` text superseded |
| `review/role-model-and-executors` | 10c260b9 | **no** | 13 | **REGISTER MEMBER** |
| `review/role-model-and-executors-clean` | 6fee7ed4 | yes | 5 | the replacement instance; integrated |
| `run/p2-betav-arm-h-decisive` | 9b0ceedf | yes | 1 | integrated; *wording* superseded |
| `run/p2-betav-arm-p-decisive` | 48c5cc59 | yes | 0 | integrated |
| `sea-ice/gate-stubs` | b02c7027 | yes | 1 | integrated; false positive |

### Additions beyond the five supplied: none

**I added no sixth entry**, and the register — had commit 3 been made —
would have carried exactly the five supplied.

### Exclusions, so that they are auditable

**No branch was excluded on suggestive-but-insufficient evidence this
time.** The first issue's single such case,
`review/role-model-and-executors`, is now a supplied member. **The
exclusion set is therefore the 44 ancestors of `main` plus this branch**,
excluded because they were integrated.

**Every relaxed-vocabulary hit on a merged branch was read in context and
is a false positive.** The kinds, with the one that most deserved a
second look named first:

- **"Report-only successor HEAD"** — `gate/p2-betav-circ`. The relaxed
  vocabulary caught `successor`, and this is the closest thing in the
  repository to a replacement record for a merged branch. **It is not
  one:** it names a later *commit* on the same branch, distinguishing the
  reviewed scientific HEAD from the report-only HEAD. **A successor HEAD
  is not a successor branch.**
- **Merge records confirming a branch survived** —
  `gate/p2-si1-unblock`, `gate/p2-betav-circ`, `sea-ice/gate-stubs`,
  `claude/paper-2-…`: "Source branch remains intact — not deleted."
  **The vocabulary matched on `replac`/`preserved`; the sentences assert
  the opposite of supersession.**
- **`### Related branch and files` fields** whose ±8-line window happens
  to reach an adjacent `DECISION_LOG.md` entry —
  `docs/canonical-interaction`, `governance/p2-phase-dependency-ruling`,
  `claude/paper-2-…`. **Window artifacts, not statements.**
- **Supersession of a *claim*, *verdict* or *wording*, never a branch** —
  `gate/p2-attraction-ruling-and-layers` (verdicts superseded by later
  evidence), `run/p2-betav-arm-h-decisive` (over-claimed wording),
  `recover/lattice-gravity-engine` (`MIGRATION.md`'s "nothing can be
  re-run").
- **Descriptions of a *landing*** — `gate/p2-diquark-*`,
  `gate/p2-land-diquark-line-v2`, `review/role-model-and-executors-clean`.
  Being merged is the opposite of being superseded.

**In no case does supersession language take a merged branch as its
subject.**

### The search, described, per §1 and Rule 16

- **325 tracked paths** at the evidence base, every one decoded and
  searched — not a sample.
- **49 remote branch names**, each searched across all of them.
- **The vocabulary was deliberately widened** for the revised threshold,
  from 7 patterns to 13, adding the rebuild/successor/regenerate family.
  **The widening changed the hit counts and changed no classification** —
  `review/role-model-and-executors` rose from 3 hits to 13, which is the
  relaxation working as intended on the one branch it was written for.
- **Both methods were run to completion and compared**, rather than one
  being used to shortcut the other.

## 6. A10-pre — Validators

Run individually with `python -m pytest <path>`. Python 3.11.15;
`python -m pytest` = **pytest 9.1.1**, the mandated invocation. The
`pytest` on `PATH` is a different version and was not used.

```
--- tests/test_repository_structure.py ---   4 passed        EXIT STATUS: 0
--- tests/test_si1_governance.py ---        14 passed        EXIT STATUS: 0
--- tests/test_gate_anchors.py ---          18 passed, 2 deselected   EXIT STATUS: 0
--- tests/test_governance_tools.py ---       8 passed        EXIT STATUS: 0
```

**All four exit 0.** The 2 deselected are `@pytest.mark.slow`, excluded
by `pyproject.toml`'s `addopts = "-m 'not slow'"` — pre-existing, and
unchanged by this task.

### What the validators assert about rule count and branching-policy structure

**Nothing.** Asked because both files were to gain content; reported even
though neither did.

- **`tests/test_repository_structure.py`** lists `CONVENTIONS.md` in
  `REQUIRED_TOP_LEVEL_FILES` and `docs/BRANCHING_POLICY.md` in
  `REQUIRED_NESTED_PATHS`, both tested by `is_file()` — **existence
  only.** Its remaining test cross-references gate IDs between
  `CLAIMS.md` and `GATES.md`.
- **`tests/test_governance_tools.py`** uses `CONVENTIONS.md` as a
  **fixture path** for the manifest evaluator — a `prefix_hash`
  criterion expected to classify `INVALID_OR_UNDERSPECIFIED`, and
  `required_paths`/`forbidden_paths` entries exercising contradiction
  detection. **It asserts the evaluator's classifications, never the
  file's content.**
- **`tests/test_si1_governance.py`** opens neither file.
- **`tests/test_gate_anchors.py`** contains zero `read_text`/`open` calls
  and reads no repository document at all.

**So Rule 18 could have been landed in any form, or rules 1–17 deleted
outright, with all four validators still green.** **No validator would
have caught the A3/§0 inconsistency either** — it is a defect in the
instructions, which nothing mechanical inspects. §9 returns to this.

## 7. A0 and A12 — Commits made, and message hygiene

    commit 1  a5bdcbc118929742919c7a7709d3fc2c4b421605
              A specs/2026-08-12T0111Z_supply-protocol-v2.md
    commit 2  da88a4d15087c4495ccd05cda4f5337bc7ac0ae6
              A reviews/chatgpt/2026-08-12T0111Z_supply-protocol-v2.md
    commit 3  THIS REPORT, at A0's frozen commit-4 path

**A0's commit 3 — `CONVENTIONS.md`, `docs/BRANCHING_POLICY.md`,
`DECISION_LOG.md` — was NOT MADE.** This report therefore lands as the
branch's third commit at the path A0 froze for its fourth. **That is a
deviation from A0 and I am naming it rather than presenting the sequence
as conforming.** It is the same shape as
`gate/p2-land-diquark-line`, which this specification's own register
describes as "the record of a correct refusal, not of failed work"; I
have followed that precedent because A0 provides no path for a stop
record and §7 requires a report.

**Commit 2 precedes the work, per Rule 15** — and in this case precedes
the decision not to do it.

Blob digests at the pre-report head:

```
specs/2026-08-12T0111Z_supply-protocol-v2.md
  blob=… sha256 recorded in commit 1; transcription, see §4's closing note
reviews/chatgpt/2026-08-12T0111Z_supply-protocol-v2.md
  sha256=d026723c68037ca164734b4d032a6b7f7e60092c4073ab3c2f2d46c47adaadea
  == the supplied file, exactly
```

### A12 — per commit

**Method.** The proposed message was written to a file and scanned before
committing; the stored message was read back from the object and scanned
again. Pattern:
`co-authored-by|claude-session|generated with|noreply@|https?://|opus|sonnet|anthropic`,
case-insensitive.

    commit 1   proposed: none found    stored: none found
               trailers suppressed: NONE — none was produced
    commit 2   proposed: none found    stored: none found
               trailers suppressed: NONE — none was produced
    commit 3   proposed: none found at authoring time
               trailers suppressed: NONE — none was produced
               (stored message is post-report evidence)

**No trailer was suppressed on any commit, because none appeared.**
Commits used `git -c commit.gpgsign=false commit -F <file>`; the
repository carries no `commit.template` and no `core.hooksPath`. **No
persistent user or global configuration was changed.**

**One distinction reported rather than glossed.** Scanning the *raw
commit object* matches `author Claude <noreply@anthropic.com>`. That is
the author/committer identity field, **not a message trailer** — A12
governs the message, and all messages scan clean. That identity is the
repository's standing one, carried by 204 of `main`'s commits including
the evidence base itself. Nothing was introduced.

**Intended commit-3 message**, inspected at authoring time:

```
docs: stop report for supply protocol v2 — A3 conflicts with the rule it lands

A3 requires the landed Rule 18 to carry the delimiter literals and the
blank-line clause. The Rule 18 that section 0 directs to be landed
contains neither and abandons delimiters by design. Two instructions,
mutually unsatisfiable; the standing invariant is to stop and report
rather than decide which prevails.

CONVENTIONS.md, docs/BRANCHING_POLICY.md and DECISION_LOG.md are
untouched. A1, A2, A6, A10-pre, A11 and A12 were completed and are
recorded: the review arrived as a file and its bytes reached the commit
unchanged, which is the first time the supply protocol has left no
residual judgement.
```

## 8. A8 — Nothing else touched

```
A	reviews/chatgpt/2026-08-12T0111Z_supply-protocol-v2.md
A	specs/2026-08-12T0111Z_supply-protocol-v2.md
```

**Two additions, zero modifications, zero deletions** at the pre-report
head. The three governance targets are blob-identical to the evidence
base:

```
  CONVENTIONS.md               base=0db56c39d44e head=0db56c39d44e identical=true
  docs/BRANCHING_POLICY.md     base=3fad8856b0d6 head=3fad8856b0d6 identical=true
  DECISION_LOG.md              base=04539f26a6bc head=04539f26a6bc identical=true
```

`GATES.md`, `AGENTS.md`, `pyproject.toml` and every path under
`scripts/`, `results/`, `tests/`, `derivations/` and `reviews/` are
untouched — the diff above is exhaustive, so no path-by-path table is
needed to establish it. **No gate status changed.** **No test was
added.** `reviews/` gains exactly one base-absent authorised path.

Scope check at the stopped pre-report head, verbatim:

```
{
  "base": "0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5",
  "failures": [],
  "head": "da88a4d15087c4495ccd05cda4f5337bc7ac0ae6",
  "mode": "exact",
  "observed_operations": [
    {
      "operation": "add",
      "path": "reviews/chatgpt/2026-08-12T0111Z_supply-protocol-v2.md"
    },
    {
      "operation": "add",
      "path": "specs/2026-08-12T0111Z_supply-protocol-v2.md"
    }
  ],
  "overall": "PASS",
  "tool": "scope_checker"
}
EXIT STATUS: 0
```

**This manifest is mine, not A9's.** **A9's manifest — 3 additions and 3
modifications — is unsatisfiable on this branch**, because three of its
six paths are the ones the stop leaves untouched. **The `PASS` above
attests that nothing unauthorised happened; it does not attest that A9
was met, and it must not be read as doing so.** The final scope at the
pushed head will show 3 additions and 0 modifications.

## 9. Rule 16 assessment

**Rule 16 is operative** — this task adds MATERIAL artifacts bearing on
supersession and review supply, questions Amendment K and Rule 15 already
address. **But the assessment §4 proposed cannot be given as written**,
because its premise did not come true: `CONVENTIONS.md` does **not** now
carry eighteen rules, and `docs/BRANCHING_POLICY.md` does **not** now
carry a register. **§4's candidate junction is therefore not confirmed —
it is not yet available.** Replacing it with the junction this branch
does create:

    specs/2026-08-12T0111Z_supply-protocol-v2.md  (Rule 18 v2, in full)
      + reviews/chatgpt/…_supply-protocol-v2.md   (APPROVED FOR EXECUTION)
      + this report                               (A1, A2, A6, A10, A11 all pass)
    ---------------------------------------------------------------------
    available inference:  Rule 18 v2 is IN FORCE, and the register EXISTS

**Neither is true.** **The branch carries an approved specification, a
clean review, and a report full of passing criteria — and lands no rule
and no register.** A reader skimming three green artifacts on a branch
named `supply-protocol-v2` would reasonably infer the opposite. **That
inference is the specific thing this assessment exists to block**, and it
is why §7 states the deviation from A0 in the same breath as the
successes.

**Two further limitations whose omission would change the reading.**

- **§4's own assessment stands unlanded and therefore unrecorded on
  `main`.** The gap it names — recorded, not enforced — remains exactly
  as true as before this task, and **nothing in the repository's
  authoritative history now mentions it.** The first issue's report says
  the same thing on a branch that is also not integrated. **The
  observation has been made twice and landed zero times.**
- **A2's success is a fact about one supply, not about the rule's
  standing.** Rule 18 v2 worked perfectly here **and is not in
  `CONVENTIONS.md`.** The next task's review is governed by nothing
  written down, exactly as the eight before it were. **This report is
  evidence for the rule, not the rule.**

## 10. Stops and clarifications

### `SPECIFICATION_DEFECT`

**One, BLOCKING — the stop.** **A3 is inconsistent with §0's Rule 18.**

A3, verbatim from the committed specification:

> **A3 — Rule 18 added** as a new `### 18.` section after Rule 17, in the
> file's existing style, with the delimiter literals and the blank-line
> clause present.

The Rule 18 §0 directs to be landed contains **zero** occurrences of
`REVIEW ARTIFACT` and **zero** of `blank line`, and states *"No
extraction, no delimiters, no normalisation."* §0's prose is explicit
that this is deliberate: *"The delimiter approach is abandoned, not
repaired."* The preamble adds: *"No delimiters are used and none should
be looked for."*

**Both cannot hold.** Satisfying A3 would mean landing a rule §0
abandons; satisfying §0 would mean failing A3 on both of its named
literals. **§6 forbids me to decide which prevails**, so I stopped.

**My reading, offered as information and not acted on:** A3 appears to be
carried over unchanged from the first issue, where it was correct because
Rule 18 v1 *was* a delimiter rule. §0 was rewritten and A3 was not.
**A re-issue that deletes A3's final clause — "with the delimiter
literals and the blank-line clause present" — and replaces it with the
file-supply rule's own testable content** (supplied as a file, bytes
unchanged, correspondence check, no extraction) **would leave nothing
inconsistent.** I have not made that edit; it is the specification
author's.

**Secondary, non-blocking — the register's ordinals and count.** §1
lists **five** entries, then says *"Verify all **three** are still
present on the remote at those commits"*, while A6 says *"all **five**
known entries"*. The count was updated in one place and not the other.
Worse for A5, had it been reached: §1's paragraph *"The **third** entry
differs in kind from the first two … its specification was defective, the
executor stopped before any tree changed"* describes
`gate/p2-land-diquark-line`, which is now the **fifth** entry. The actual
third is `governance/supply-protocol-and-superseded`, whose executor did
**not** stop and whose work was substantial. **Landing that paragraph
verbatim would have committed a false statement about the third entry;
adapting it would have been an unauthorised rewrite.** I verified all
five, per A6, and note that A5 carried a second latent conflict
independent of the A3 stop.

**Secondary, non-blocking — §0's historical prose is stale under its own
replacement.** §0 still says *"Rule 18 below generalises it from one
specification's clause to a standing rule"* of the blank-line clause,
which the new Rule 18 does not contain, and still says the shared line
*"is the mode a standing rule must fix"* when no standing rule about
delimiters is now proposed. Also, as the Reviewer's non-blocking
clarification notes and §0 itself half-acknowledges, the headline
*"eight attempts and five distinct failure modes"* counts modes 1 and 2
as distinct while describing them as the same mode twice; §0 then adds a
sixth mode, so the deduplicated tally is **five modes across nine
attempts** counting this task. **Affects no criterion.** Not corrected —
§2 authorises no edit to the specification.

### `ENVIRONMENT`

**None. Neither of Rule 13's two diagnostic orders was exercised**,
because no environment failure occurred. Rule 13 carrying two conflicting
orders remains a known open item, untouched. Nothing was installed.

### `OBSERVATION_METHOD_ERROR`

**None reached a conclusion.** One methodological choice worth recording
because it could have hidden a register member: **the first issue's
vocabulary was too narrow for the revised threshold**, which admits
records that say "rebuilt" rather than "superseded". I widened it from 7
patterns to 13 before drawing any negative conclusion, and report that
the widening changed hit counts but no classification. **Had I reused the
narrow vocabulary, the scan would have understated the evidence for the
one branch the relaxation was written for.**

### `REPOSITORY_DEFECT`

**None introduced; nothing in the repository was modified.** The
pre-existing gap stands and is measured in §6: **no validator asserts
anything about `CONVENTIONS.md`'s rule count or
`docs/BRANCHING_POLICY.md`'s structure.** §2 forbids adding a test and
none was added. **A second, sharper instance of the same gap is now
visible: nothing mechanical inspects a specification for internal
consistency**, which is why the A3/§0 conflict reached execution at all —
and why it was caught by reading rather than by a tool.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`

**None.** The first issue's single instance,
`review/role-model-and-executors`, is resolved: §1's revised threshold
makes it a supplied register member, and its tip is verified unchanged at
`10c260b96882ac12610f78840aeeabd07be2d7cb`. **No branch remains in the
suggestive-but-unestablished category.**

## 11. Ambiguous, unsatisfiable, or would have specified differently

- **A9 is unsatisfiable as a consequence of the stop**, not
  independently: three of its six paths are the untouched ones. Reported
  in §8 so the `PASS` there is not mistaken for A9 being met.
- **A0 provides no path for a stop report.** Its commit 3 is the blocked
  action and its commit 4 is the report. I used the frozen report path
  and named the deviation. **A future A0 could say where a stop record
  goes** — the programme has now produced two stops and improvised the
  answer twice.
- **A3's "in the file's existing style" was the one part I could have
  satisfied**, and I note for the re-issue that the first issue
  established the style question: rules 1–17 carry no trailing period in
  their headings, while both issues' draft heading shows
  `**18. Review supply protocol.**` with one. **`### 18. Review supply
  protocol` is the conforming form.**
- **§1's "What to add" blockquote is the text to land; the paragraphs
  after it are specification prose.** The first issue landed an adapted
  version of the "third entry" paragraph and of the threshold. **A
  re-issue should say explicitly which surrounding paragraphs are part of
  the artifact**, because the ordinal defect above only bites if that
  paragraph is landed, and nothing states whether it should be.
- **A2's correspondence criterion worked and is worth keeping verbatim.**
  "Identify the specification by digest or task name" is checkable
  without judgement. **Requiring the digest alone would have failed
  here**, since a review written before commit 1 cannot cite the blob
  digest that commit 1 fixes — a circularity the first issue's Reviewer
  had already flagged in a different task. **The disjunction is the
  right design.**
- **Nothing else was unsatisfiable.** No instruction conflicted with a
  repository rule. The one instruction-to-instruction conflict is the
  stop, and I have named the resolution I believe correct without taking
  it.

## 12. What this task did not do

**It landed no rule and no register.** `CONVENTIONS.md`,
`docs/BRANCHING_POLICY.md` and `DECISION_LOG.md` are byte-identical to
the evidence base. No fourth deletion state; the closed count identity
untouched because the file is untouched. **No branch was deleted and no
branch ref changed.** **`governance/supply-protocol-and-superseded @
7146a093…` was not touched, reused or deleted**, and no superseded branch
was integrated. **No assessment was made of any branch's content** —
supersession is not a verdict on content. **No test was added.**
**`AGENTS.md` was not modified.** No gate, gate status, verdict, digest or
hash-pinned artifact was modified. `main` was not moved and nothing was
merged into it. **No PR was opened.**
