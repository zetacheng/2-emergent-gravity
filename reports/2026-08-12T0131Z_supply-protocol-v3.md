# Task report — the review supply protocol, and a superseded-branch attribute

Specification:        `specs/2026-08-12T0131Z_supply-protocol-v3.md`
Pre-execution review: `reviews/chatgpt/2026-08-12T0131Z_supply-protocol-v3.md`
Specification evidence base: `0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5`
Branch:               `governance/supply-protocol-v3`
Pre-report head:      `5a96682213ffe34929d4e1946ad932ecbaed0d18`
UTC token `{HHMM}Z`:  `0131`, fixed by commit 1; `XX` = `12`.
                      **Differs from `2337` (first issue) and from `0111`
                      (the v2 issue)**, as A0 requires.

**Headline. Rule 18 landed, and it was sufficient.** The review arrived as
a file; its SHA-256 was identical at supply, staging and commit; **no step
required a judgement of any kind.** A3's four presence checks and both
absence checks pass. Rules 1–17 are byte-identical after removing the Rule
18 section — the stripped file digests to A1's pinned value. The deletion
state machine is byte-identical. The register carries all six supplied
entries, by name and grouped by kind. **The third attempt is the one that
landed.**

**Two things the specification asked me to report explicitly, both
answered in full below:** the correspondence marker I actually used (§4.2),
and how the specification itself arrived (§4.4 — **pasted, not as a
file**, which Rule 18 permits and requires me to say).

---

## 1. A1 — Pinned inputs, verified before use

Method as specified, at `0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5`:

```
e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451  -   CONVENTIONS.md
0ba1e2a006d287800d19b1bfadb5fe24f4bda72dedaf38ad3289ddfa700b9da9  -   docs/BRANCHING_POLICY.md
```

**Both match A1's pinned values. No STOP.** Verified before the worktree
was created and before either file was read for editing.

## 2. A11 — Branch only

```
local  refs/heads/main      0f7961747abe2a18b436c0b1e5b928f425ea4d9a
origin/main (tracking)      0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
remote refs/heads/main      0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
evidence base               0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
```

All three reported. **`refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to the evidence base.** **Local `main` is
stale by design and was not repaired.** Branch created from that commit,
clean:

```
Preparing worktree (new branch 'governance/supply-protocol-v3')
HEAD is now at 0ab6369 docs: report the landing of the diquark line
head:   0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
branch: governance/supply-protocol-v3
dirty:  0
```

**No `main` ref was moved. No branch was deleted.** **Both superseded
branches were left untouched** — `7146a093…` and `40168469…`, re-verified
in §5.1. No PR, no force-push, no history rewrite, no merge into `main`.

## 3. A0, A12 — Commits and message hygiene

    commit 1  6910ddfa065b40b21cd23ce4eace84832f5666a9
              A specs/2026-08-12T0131Z_supply-protocol-v3.md
    commit 2  1b940c00f6901ec48e416a52ae960e22a5728da1
              A reviews/chatgpt/2026-08-12T0131Z_supply-protocol-v3.md
    commit 3  5a96682213ffe34929d4e1946ad932ecbaed0d18
              M CONVENTIONS.md
              M DECISION_LOG.md
              M docs/BRANCHING_POLICY.md
    commit 4  THIS REPORT

**Commit 2 precedes the work, per Rule 15.** All four paths are the
specification's; I chose none. **A0's stop-path clause was not needed** —
the task did not stop before commit 3, so this report is commit 4 both by
A0's numbering and in actual sequence. **The clause A0 added after two
improvised stops went unexercised, and that is the right outcome to
report rather than to leave silent.**

Blob digests at the pre-report head:

```
CONVENTIONS.md            sha256=928dea15d7a2699384510240381f6bc9f86fd9bb3a7cbfaff5370839b430ce2d
docs/BRANCHING_POLICY.md  (modified; deletion-state section byte-identical, §7)
DECISION_LOG.md           (append-only, §8)
specs/…0131Z_supply-protocol-v3.md
                          sha256=7e7a2419b1e6933ee993dd630fe56f7b0d2ff41fa741a0381f7f979c47d385c8
reviews/chatgpt/…0131Z_supply-protocol-v3.md
                          sha256=206530ee0ccd1da4fd1a7b764fdc36e8c4b0262f23214f07f1e381d644612719
```

### A12 — per commit, proposed before and stored after

**Method.** The proposed message was written to a file and scanned before
committing; the stored message was read back from the commit object and
scanned again. Pattern, case-insensitive:
`co-authored-by|claude-session|generated with|noreply@|https?://|opus|sonnet|anthropic`.

    commit 1   proposed: none found    stored: none found
               trailers suppressed: NONE — none was produced
    commit 2   proposed: none found    stored: none found
               trailers suppressed: NONE — none was produced
    commit 3   proposed: none found    stored: none found
               trailers suppressed: NONE — none was produced
    commit 4   proposed: none found at authoring time
               trailers suppressed: NONE — none was produced
               (stored message is post-report evidence)

**No trailer was suppressed on any commit, because none appeared** — at
either the proposal or the stored stage. Commits used
`git -c commit.gpgsign=false commit -F <file>`; the repository carries no
`commit.template` and no `core.hooksPath`. **No persistent user or global
configuration was changed** — the setting was passed per invocation.

**One distinction, reported rather than glossed.** Scanning the *raw
commit object* matches `author Claude <noreply@anthropic.com>`. That is
the author/committer identity field, **not a message trailer** — A12
governs the message, and every message scans clean. That identity is the
repository's standing one, carried by 204 of `main`'s commits including
the evidence base itself. Nothing was introduced by this task.

Stored message of commit 3, read back from the object:

```
governance: add Rule 18 review supply protocol and a SUPERSEDED branch attribute

Rule 18 lands the file-supply protocol: a pre-execution review is supplied
as a file and its bytes are committed unchanged, with no extraction, no
delimiters and no normalisation, plus a correspondence check and its STOP
conditions. The delimiter approach is abandoned rather than patched.
Rules 1-17 are unchanged and unrenumbered.

docs/BRANCHING_POLICY.md gains SUPERSEDED as an attribute orthogonal to the
deletion states, with a register of six branches grouped by kind and
referred to by branch name rather than ordinal. The Stage-1 deletion machine
and its closed count identity are byte-identical, and the existing
permanently-preserved entry is untouched.

DECISION_LOG.md records both additions as prospective.
```

**Intended commit 4 message**, inspected at authoring time; its scan under
the same pattern found none, so there is no trailer to suppress:

```
docs: execution report for supply protocol v3 and the superseded attribute

Records A1-A12 raw output, A3's four presence and two absence checks on the
landed Rule 18, A4's body comparison of rules 1-17, A5's before-and-after of
the deletion state machine, both append-only measures, and the enumeration
of all 50 remote branches.

Rule 18 was sufficient on its first live application: the review arrived as
a file, its digest was identical at supply, staging and commit, and no step
required a judgement. The specification arrived pasted, which the rule
permits and requires the executor to report.
```

## 4. A2 — The review, and whether Rule 18 was sufficient

### 4.1 The mechanics

```
supplied : 206530ee0ccd1da4fd1a7b764fdc36e8c4b0262f23214f07f1e381d644612719
staged   : 206530ee0ccd1da4fd1a7b764fdc36e8c4b0262f23214f07f1e381d644612719
committed: 206530ee0ccd1da4fd1a7b764fdc36e8c4b0262f23214f07f1e381d644612719
```

**All three equal**, as A2 requires the supplied file's and the committed
blob's digests to be shown. 181 lines, 10116 bytes, committed at
`reviews/chatgpt/2026-08-12T0131Z_supply-protocol-v3.md`. Supply-integrity
checks on the file as received:

    occurrences of "REVIEW ARTIFACT"            0
    lines beginning with an attachment marker   0

**The whole procedure was `cp` and three digests.**

### 4.2 The correspondence marker actually used

**Stated explicitly because the Reviewer's findings section asks for
exactly this.** **Marker used: TASK NAME, not digest.** The evidence, at
three points in the supplied file:

    line 1   # Pre-execution review — supply protocol v3 and
             superseded-branch attribute
    line 8   … task identity `supply-protocol-v3`, at the stated evidence
             base: 0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5
    line 50  This review identifies the task by the task name
             `supply-protocol-v3` and by the title of the specification
             under review.

**The task name matches this task's identity**, which A0's paths carry as
`…_supply-protocol-v3.md`. The review also quotes the specification's
title verbatim and its evidence base. **Not a different specification. No
STOP.**

**Why the marker had to be the task name and not a digest**, since A2
offers both: **the review is committed as commit 2 and the specification's
blob digest is fixed by commit 1**, so a review authored before execution
cannot cite it. **The disjunction is what makes A2 satisfiable at all**,
and I record that as an argument for keeping it.

### 4.3 Was Rule 18 sufficient? **Yes.**

§7 asks three questions. Answering each exactly:

- **Did the review arrive as a file?** **Yes**, at
  `…/0bb904a4-202608XXT_HHMMZ_supplyprotocolv3_review.md`. Not pasted.
- **Did its bytes reach the commit unchanged?** **Yes**, by SHA-256 at
  three points. **No extraction, no delimiter search, no normalisation,
  nothing stripped.**
- **Did ANY step require a judgement of any kind?** **No.**

**On the third question, the Reviewer's finding deserves a direct
answer rather than agreement.** It says Rule 18 "does not eliminate all
judgement… The executor must still determine whether the supplied file
*corresponds*". **In this instance that determination required no
judgement at all**, because the review states its own correspondence in
so many words at line 50 — it names the task identity and says it is
doing so. **There was nothing to weigh.**

**But the Reviewer's point is right as a general claim about the rule, and
I do not want the report to read as refuting it.** A review that neither
cited a digest nor named the task, yet plainly discussed this
specification's content, would put the executor in exactly the position
the Reviewer describes. **Rule 18 handles that case by outcome — "if it
does not [identify the specification], STOP"** — so the residual is
bounded: the executor either finds a stated marker or stops. **It cannot
end in a silent inference, which is what broke the delimiter protocol.**
That is a materially different situation from a judgement point, and the
distinction is the reason this answer is "yes".

**The comparison that matters.** Under the delimiter protocol the
executor had to *construct* the artifact's boundary and could get it
silently wrong. Under the file protocol the artifact is given, and the one
remaining check has a stated criterion and a stated failure action.
**Nothing about the committed bytes depended on anything I decided.**

### 4.4 How the specification arrived — Rule 18's new reporting clause

**The specification arrived PASTED, not as a file.** Rule 18 as landed
requires me to say so and permits it:

> **A pasted specification is permitted and is not a STOP**, because it is
> instruction rather than an artifact whose exact bytes carry authority.
> **But the executor reports which way it arrived**, and where it was
> pasted, says so.

**Where:** as the body of the task message, with the attachment marker for
the review file fused to line 0 ahead of the specification's title —
the same transport behaviour that broke the first issue, now harmless
because nothing is extracted from it.

**The consequence, stated plainly.** `specs/2026-08-12T0131Z_supply-protocol-v3.md`
carries **my transcription**, digest
`7e7a2419b1e6933ee993dd630fe56f7b0d2ff41fa741a0381f7f979c47d385c8`.
**No supplied file exists to compare it against, so no digest can attest
that it matches the sender's text.** I transcribed it faithfully and
verified the parts A3 depends on by measurement against the committed blob
(§6). **This clause working as designed is a small but real result: the
gap is now recorded in the artifact rather than noticed by an executor
and mentioned in prose.** Supplying the specification as a file would
close it, which is what the rule's SHOULD asks for.

## 5. A6 — Register membership determined

### 5.1 The six supplied entries, verified

`git ls-remote origin` is the sole authority, per `docs/BRANCHING_POLICY.md`.

```
fix/pi-decisions-and-deferred                 52f651174dc1  MATCHES  not an ancestor
fix/pi-decisions-v2                           ebd531ab568a  MATCHES  not an ancestor
governance/supply-protocol-v2                 401684696086  MATCHES  not an ancestor
governance/supply-protocol-and-superseded     7146a093c657  MATCHES  not an ancestor
review/role-model-and-executors               10c260b96882  MATCHES  not an ancestor
gate/p2-land-diquark-line                     d64cd912ca9f  MATCHES  not an ancestor

fix/pi-decisions-v3                           93de3218095c  MATCHES  IS ancestor of main
```

**All six present at exactly the stated commits; none is an ancestor of
`main`. No STOP.** `fix/pi-decisions-v3` **is** an ancestor — the
surviving instance, correctly absent from the register.

**Both of this rule's own earlier issues are verified unmoved**, which
matters because §6 forbids touching them and this task is their
replacement: `7146a093c657` and `401684696086`, both still exactly as the
specification records them.

### 5.2 Enumeration of all 50 remote branches

**Two independent methods, agreeing with no residue.**

**Method 1 — relaxed vocabulary scan.** All 325 tracked files at the
evidence base decoded and searched for each of the 50 branch names; every
hit tested in a ±8-line window against 13 patterns chosen to catch the
*fact* of replacement rather than the word, per §1's threshold:

    supersed | re-issu | replac | rebuil | abandon | obsolet | withdraw
    regenerat | successor | re-instantiat | instead of
    preserved untouched | not (to be) integrated

**Method 2 — integration status.** A branch that is an ancestor of `main`
was integrated, so it cannot be "preserved as evidence rather than for
integration". **Topology is used only to EXCLUDE, never to include**, as
§1 requires.

```
remote branches: 50
ancestors of main: 44   non-ancestors: 6
non-ancestors: ['fix/pi-decisions-and-deferred', 'fix/pi-decisions-v2',
                'gate/p2-land-diquark-line',
                'governance/supply-protocol-and-superseded',
                'governance/supply-protocol-v2',
                'review/role-model-and-executors']

non-ancestors minus register minus this branch: EMPTY — no unclassified non-ancestor
register members that ARE ancestors (would be a contradiction): NONE
```

**The six non-ancestors are exactly the six supplied register entries.**
Both directions were checked: no non-ancestor is unaccounted for, and no
register member is secretly merged.

| branch | tip | ancestor of `main` | hits | classification |
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
| `gate/p2-attraction-ruling-and-layers` | 878b632c | yes | 1 | integrated; *verdicts* superseded |
| `gate/p2-betav-campaign-prereg` | 21efcf85 | yes | 0 | integrated |
| `gate/p2-betav-circ` | ca334fe0 | yes | 3 | integrated; "successor HEAD", see §5.4 |
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
| `governance/supply-protocol-v2` | 40168469 | **no** | 0 | **REGISTER MEMBER** |
| `recover/batch2-gfvec-and-foundations` | 324ef969 | yes | 0 | integrated |
| `recover/betav-complete` | 836bf144 | yes | 0 | integrated |
| `recover/lattice-gravity-engine` | cdcbd840 | yes | 1 | integrated; `MIGRATION.md` text superseded |
| `review/role-model-and-executors` | 10c260b9 | **no** | 13 | **REGISTER MEMBER** |
| `review/role-model-and-executors-clean` | 6fee7ed4 | yes | 5 | the replacement instance; integrated |
| `run/p2-betav-arm-h-decisive` | 9b0ceedf | yes | 1 | integrated; *wording* superseded |
| `run/p2-betav-arm-p-decisive` | 48c5cc59 | yes | 0 | integrated |
| `sea-ice/gate-stubs` | b02c7027 | yes | 1 | integrated; false positive |

**`governance/supply-protocol-v3` — this branch — is absent from the
table because it was not yet pushed when the enumeration ran.** It is not
a register candidate: it is the surviving instance.

**A note on the two register members scoring 0 hits.**
`governance/supply-protocol-and-superseded` and
`governance/supply-protocol-v2` score zero because **the artifacts
recording their supersession are this task's own specification and this
report, neither of which existed at the evidence base the scan reads.**
Their durable evidence is the stop report on
`governance/supply-protocol-v2` itself plus the specification committed as
commit 1. **A zero hit count here is a fact about the scan's base, not
absence of evidence** — and it is worth flagging because a later auditor
re-running this scan against a later base will get a different number.

### 5.3 Additions beyond the six supplied: none

**I added no seventh entry.** The register as landed carries exactly the
six supplied, and §7 asks for a reason for any addition beyond them —
there are none to give.

### 5.4 Exclusions, so that they are auditable

**No branch was excluded on suggestive-but-insufficient evidence.** The
first issue's single such case, `review/role-model-and-executors`, is a
supplied member under the revised threshold. **The exclusion set is the 44
ancestors of `main`, excluded because they were integrated.**

**Every relaxed-vocabulary hit on a merged branch was read in context and
is a false positive.** The kinds, closest call first:

- **"Report-only successor HEAD"** — `gate/p2-betav-circ`. The relaxed
  vocabulary caught `successor`, and this is the nearest thing in the
  repository to a replacement record for a merged branch. **It is not
  one:** it distinguishes the reviewed scientific HEAD from a later
  report-only HEAD **on the same branch.** **A successor HEAD is not a
  successor branch.**
- **Merge records asserting a branch survived** — `gate/p2-si1-unblock`,
  `gate/p2-betav-circ`, `sea-ice/gate-stubs`, `claude/paper-2-…`: "Source
  branch remains intact — not deleted." **The vocabulary matched on
  `replac`/`preserved`; the sentences assert the opposite of
  supersession.**
- **`### Related branch and files` fields** whose ±8-line window reaches
  an adjacent `DECISION_LOG.md` entry — `docs/canonical-interaction`,
  `governance/p2-phase-dependency-ruling`, `claude/paper-2-…`. **Window
  artifacts, not statements.**
- **Supersession of a *claim*, *verdict* or *wording*, never a branch** —
  `gate/p2-attraction-ruling-and-layers`, `run/p2-betav-arm-h-decisive`,
  `recover/lattice-gravity-engine`.
- **Descriptions of a *landing*** — `gate/p2-diquark-*`,
  `gate/p2-land-diquark-line-v2`, `review/role-model-and-executors-clean`.
  Being merged is the opposite of being superseded.

**In no case does supersession language take a merged branch as its
subject.**

### 5.5 The search, described, per §1 and Rule 16

- **325 tracked paths** at the evidence base, every one decoded and
  searched — not a sample.
- **50 remote branch names**, each searched across all of them.
- **13 vocabulary patterns**, deliberately wider than the word
  "superseded", because §1's threshold turns on the fact and not the word.
- **Both methods run to completion and cross-checked in both directions**
  — no unclassified non-ancestor, no register member that is an ancestor.
- **Result: no further members**, and the reason is structural rather than
  lexical: **every branch not in the register was integrated**, and an
  integrated branch cannot be preserved-instead-of-integrated.

## 6. A3 — Rule 18 added, checked, and quoted in full

Added as a new `### 18.` section after Rule 17. Headings after the edit:

```
923:### 15. Governing artifacts are committed
943:### 16. Accumulated reading
982:### 17. Integrations do not add epistemic or governance classifications
992:### 18. Review supply protocol
```

`CONVENTIONS.md`: 990 → 1022 lines; the section is 1441 bytes. **The
heading carries no trailing period, matching rules 1–17**; the
specification's draft heading shows one.

### A3's six checks, each reported as required

Measured on the landed section:

```
  --- required PRESENT ---
  "AS A FILE"                                                present
  "no delimiters"                                            present
  a correspondence requirement                               present
  a STOP for a missing / pasted / non-corresponding review   present
  --- required ABSENT ---
  "=== REVIEW ARTIFACT"                                      ABSENT
  "blank line"                                               ABSENT
```

**The two absences were verified as absences, not assumed**, and verified
twice — on the section and on the whole file:

```
    "=== REVIEW ARTIFACT" in CONVENTIONS.md : 0 occurrences
    "blank line" in CONVENTIONS.md          : 0 occurrences
```

**One check needs its mapping stated rather than just its verdict.** A3
asks for "a STOP for a missing, **pasted** or non-corresponding review".
**The landed rule does not use the word "pasted" in its STOP clause**; it
lists three conditions, and the pasted case falls under the second:

    "if it does not [identify the specification]"   -> non-corresponding by omission
    "or if no file is supplied"                     -> MISSING, and PASTED
    "or if the file corresponds to a different
     specification"                                 -> non-corresponding
    "STOP and say which."

**A pasted review means no file is supplied, so it is covered.** I report
the mapping rather than claim a literal match, and I did not add a clause
to make the word appear — §0's blockquote is the rule to land, and
extending it would be authoring.

### Rule 18 as landed, quoted in full

> ### 18. Review supply protocol
>
> **A pre-execution review is supplied to the executor AS A FILE, not as
> text pasted into a prompt.** The executor commits that file's bytes
> unchanged.
>
> **No extraction, no delimiters, no normalisation.** There is no boundary
> to locate, so **no boundary can be inferred**; there are no transport
> artifacts to strip, so **no stripping rule is needed.**
>
> **The specification SHOULD also be supplied as a file.** It is committed
> at a frozen path by the task's first commit, so **a pasted specification
> makes commit 1's bytes the executor's transcription with no supplied file
> to digest against** — verifiable in the way commit 2 now is only if it
> too arrives as a file.
>
> **A pasted specification is permitted and is not a STOP**, because it is
> instruction rather than an artifact whose exact bytes carry authority.
> **But the executor reports which way it arrived**, and where it was
> pasted, says so.
>
> **The executor verifies correspondence before committing**: the supplied
> review must identify the specification it reviews, by digest or by task
> name. **If it does not, or if no file is supplied, or if the file
> corresponds to a different specification, STOP and say which.**
>
> **The executor never authors, edits, summarises or reformats a review**,
> and never reconstructs one from a conversation.
>
> **Placeholders inside a review's text stay as written.** Placeholders are
> resolved in the artifact's PATH only.

## 7. A4 and A5 — What did not change

### A4 — Rules 1–17, by body comparison

**Heading equality is reported as a proxy; the body comparison is the
measure.** Method: locate the single `### 18. Review supply protocol`,
remove from the blank line preceding it to end of file, keeping the
newline that terminated Rule 17, and digest the remainder.

```
base bytes: 53250  sha256: e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451
new  bytes: 54691  sha256: 928dea15d7a2699384510240381f6bc9f86fd9bb3a7cbfaff5370839b430ce2d
stripped bytes: 53250  sha256: e3afa5219e56ece43baf2902fe879dc871cb57801c5a1d035357c911cf94a451

A4 RESULT — rules 1-17 byte-identical after removing the Rule 18 section: True
Rule 18 section byte length: 1441

A4 heading proxy — base: 17 new: 18 first 17 identical: True
the single new heading: ['### 18. Review supply protocol']
```

**The stripped file's SHA-256 is A1's pinned digest** — so rules 1–17 are
byte-identical, not merely equal in their headings. **No rule was
renumbered, reworded or reordered.**

### A5 — The deletion state machine, before and after

Placed as a new `## Superseded branches` section **immediately after
`## Deletion authorization states`**, so a reader meets "this is not a
fourth state" adjacent to the closed machine it disclaims — Amendment K's
second option, "stated where an integrator will meet it".

```
3:## Branch names
13:## Rules
24:## Branch lifecycle
66:## Deletion authorization states
104:## Superseded branches
231:## Remote refs are the sole deletion authority
```

`docs/BRANCHING_POLICY.md`: 129 → 255 lines.

**BEFORE and AFTER of `## Deletion authorization states`:**

```
BEFORE bytes: 1435  sha256: dced093f6baa1bd1da2155ad360000209aaa42626ed633aac7df53406d210ca2
AFTER  bytes: 1435  sha256: dced093f6baa1bd1da2155ad360000209aaa42626ed633aac7df53406d210ca2
BYTE-IDENTICAL: True
```

The section, which is the same text on both sides:

`````
## Deletion authorization states

**Deletion authorization has three Stage-1 outcomes, and every listed
branch reaches exactly one:**

```text
present on remote,  verified_merged true   -> PENDING_DELETE
present on remote,  verified_merged false  -> NOT_AUTHORIZED      (terminal)
listed, absent from remote                 -> ABSENT_FROM_REMOTE  (terminal)
```

**Stage 2 acts on `PENDING_DELETE` entries and no others.**
**Stage 3** resolves `PENDING_DELETE` to `DELETED` or `SKIPPED`;
`NOT_AUTHORIZED` and `ABSENT_FROM_REMOTE` entries are left exactly as
they are.

**`verified_merged` is `n/a` for an `ABSENT_FROM_REMOTE` entry.** With
no tip there is no ancestry to test, and recording `true` or `false`
would assert something that does not exist.

**The counts satisfy a closed identity, which is machine-checkable:**

```text
listed_count = pending_delete_count
             + not_authorized_count
             + absent_from_remote_count
```

**Report the identity as an equation with its arithmetic, not as a
claim.** Its purpose is that a mis-stated entry shows up as a number
that does not add up.

**The two terminal states are not interchangeable.** `NOT_AUTHORIZED`
means present but not eligible; `ABSENT_FROM_REMOTE` means there is
nothing to delete. A branch in the second state may be pushed later and
would then be assessed afresh; a branch in the first will not become
deletable by anything happening on the remote.
`````

Literal counts and every pre-existing section:

```
  'PENDING_DELETE'                       base=3   new=3
  'NOT_AUTHORIZED'                       base=3   new=4
  'ABSENT_FROM_REMOTE'                   base=4   new=4
  'listed_count = pending_delete_count'  base=1   new=1

closed-identity block intact: True

  ## Branch names                                    identical=True
  ## Rules                                           identical=True
  ## Branch lifecycle                                identical=True
  ## Deletion authorization states                    identical=True
  ## Remote refs are the sole deletion authority     identical=True
```

**Every pre-existing section is byte-identical. No fourth deletion state
was added and the closed count identity is untouched.**

**`NOT_AUTHORIZED` gains one occurrence, and it is mine**, in the new
section's orthogonality sentence: each register entry is present and
unmerged, so each is `NOT_AUTHORIZED` for deletion. **That is a use of an
existing state, not a new one**, and it is reported because a bare count
would otherwise look like a change to the machine.

**§1's protection of the existing preservation entry, verified:**

```
"permanently preserved" entry present verbatim in the new file: True
```

**It was not edited, replaced or weakened.** The branch now carries both
dispositions, which is the point — do not delete, and do not integrate.

### The superseded section, quoted in full as landed

> ## Superseded branches
>
> **A branch is SUPERSEDED when its work has been re-issued or replaced
> and it is preserved as evidence rather than for integration.**
>
> **A superseded branch MUST NOT be integrated.** Its content may remain
> correct — supersession is about integrability and task identity, not
> about correctness — **but the authoritative instance is the branch that
> replaced it.**
>
> **This is an attribute, not a deletion state.** A superseded branch
> still reaches exactly one Stage-1 deletion outcome, and the closed count
> identity above is unchanged. **The two questions are independent:
> whether a branch may be deleted, and whether it may be integrated.**
> Each entry below is present on the remote and unmerged, so each is
> `NOT_AUTHORIZED` for deletion; that is its deletion outcome, and it says
> nothing about integrability.
>
> **Supersession is recorded in the register below**, naming the branch,
> its commit, what replaced it, and why. **A Git ref carries no such
> marker, so the register is where it lives.**
>
> **The register:**
>
>     fix/pi-decisions-and-deferred @ 52f651174dc1fef03b4fb9276078fa1f08d94bd7
>       superseded by  fix/pi-decisions-v2, then fix/pi-decisions-v3
>       reason         re-issued on a clean branch after the second
>                      execution overwrote the first execution's pushed
>                      records on the same branch
>       content        the substantive content was approved; the
>                      representation was not
>
>     fix/pi-decisions-v2 @ ebd531ab568aaffabd86a4a94d925a711e62aa36
>       superseded by  fix/pi-decisions-v3
>       reason         stale base: main advanced through two governance
>                      landings and the branch lost conflict-free
>                      integrability
>       content        APPROVED and unchanged; only its integrability
>                      lapsed
>
>     governance/supply-protocol-v2
>                               @ 40168469608618aef6812735ff70e32de0e3cbc8
>       superseded by  governance/supply-protocol-v3
>       reason         its A3 required the landed Rule 18 to contain
>                      delimiter literals and a blank-line clause, while
>                      the rule it directed abandoned both; the executor
>                      stopped at that inconsistency
>       content        no governance file was touched; the branch carries
>                      a stop report and the first successful live test of
>                      the file-supply rule
>
>     governance/supply-protocol-and-superseded
>                               @ 7146a093c65788a57d63a747b71d86edb91eddc6
>       superseded by  governance/supply-protocol-v3
>       reason         its A2 required applying a Rule 18 whose own text
>                      forbade the only available action; the executor
>                      derived a boundary and continued where the
>                      standing inconsistency invariant required a stop
>       content        the governance work was correct and the committed
>                      review was byte-correct; what failed was the rule
>                      it was landing, which this version replaces
>
>     review/role-model-and-executors
>                               @ 10c260b96882ac12610f78840aeeabd07be2d7cb
>       superseded by  review/role-model-and-executors-clean, merged
>       reason         rebuilt SOLELY to remove undeclared commit
>                      metadata from history; the clean-rebuild
>                      specification names the successor and the reason
>       content        VERIFIED CORRECT before the rebuild — seven
>                      declared paths, correct commit layering, protected
>                      paths unchanged, the role model landed as approved
>       note           this branch ALREADY carries a durable disposition:
>                      "permanently preserved ... the unmerged record of a
>                      commit-metadata defect, retained as
>                      negative-provenance evidence". That disposition
>                      stands unchanged. The two answer different
>                      questions -- permanently preserved means do not
>                      delete; superseded means do not integrate -- and
>                      the register exists because they are independent.
>
>     gate/p2-land-diquark-line @ d64cd912ca9ff78a85787f0e54f345f474cdb192
>       superseded by  gate/p2-land-diquark-line-v2
>       reason         the specification stated an impossible merge-base
>                      and the executor STOPPED at the pre-merge guard;
>                      the re-issue corrected the value
>       content        the branch carries a report of the stop and NO
>                      merge; it is the record of a correct refusal, not
>                      of failed work
>
> **The entries differ in kind and the register does not flatten that.**
> **Refer to them by BRANCH NAME, never by ordinal** — an ordinal is
> correct only until the list grows, and a paragraph of this register has
> already been wrong once for exactly that reason.
>
>     approved work re-instantiated elsewhere
>       fix/pi-decisions-and-deferred
>       fix/pi-decisions-v2
>       review/role-model-and-executors
>
>     no work at all: a defective specification, an executor that
>     stopped, and the evidence that a stop happened and why
>       gate/p2-land-diquark-line
>       governance/supply-protocol-v2
>
>     work completed but the execution contract breached, so not
>     integrable although the content was correct
>       governance/supply-protocol-and-superseded
>
> **Supersession covers all three kinds; the register records which.**
>
> **Entry threshold.** **A branch is added to this register only where a
> durable repository artifact records its re-issue, replacement or
> supersession and identifies the replacement or the reason.** **The
> artifact must record the FACT, not use a particular WORD** — a
> specification that says a branch was rebuilt and names both the
> successor and the reason satisfies this even if the word "superseded"
> never appears. **Naming similarity, age, Git topology, or the mere
> existence of a later branch do NOT suffice**, singly or together.
> **Where evidence suggests supersession but does not establish it, the
> branch is left out pending a PI decision** and the evidence is reported.
> **Finding the artifact that already records a supersession is an
> observation; classifying a branch as superseded is a decision.**

**Two deliberate representation choices, stated so they are not mistaken
for drift.** The specification's register says "superseded by **this
task**" for the two supply-protocol entries; **as landed, that is the
branch name `governance/supply-protocol-v3`**, because "this task" has no
referent once the text lives in a standing document. And **the
`review/role-model-and-executors` note's bold emphasis and its final
"**Do not edit, replace or weaken the existing preservation entry**"
instruction are omitted from the landed register**: the first because
`text` blocks do not render markup, the second because it is an
instruction to *this* executor, not a property of the branch. **The
instruction was obeyed** (§7's verification) rather than transcribed.

## 8. A7 — `DECISION_LOG.md`, append-only on both measures

Entry added at line 2005 in the file's existing format — `Date:` /
`Decision owner:` / `Effect:` header, then `### Decision`, `### Reason`,
`### Prospective only`, `### Consequences`, `### Supersedes`,
`### Related gate`, `### Related branch and files`. 2003 → 2145 lines.

**Measure 1 — against the evidence base:**

```
142	0	DECISION_LOG.md
base is an exact byte PREFIX of new: True
base bytes: 82337  new: 89541  appended: 7204
base sha256  : c1366d67f0485da1414d3838d5b42632143cce71b32943c9aedc672b9ebabbde
prefix sha256: c1366d67f0485da1414d3838d5b42632143cce71b32943c9aedc672b9ebabbde
```

**142 lines added, 0 deleted**, and the base is an **exact byte prefix** —
a stronger statement than line counts, since it excludes an in-place edit
offset by an equal-length insertion.

**Measure 2 — per commit against its parent:**

```
6910ddfa065b  DECISION_LOG.md not touched by this commit
1b940c00f690  DECISION_LOG.md not touched by this commit
5a96682213ff  added/removed: 142	0	DECISION_LOG.md
```

**Zero deleted lines on both measures.** The entry records both additions
and states that they are prospective, under its own `### Prospective only`
heading.

## 9. A8, A9 — Nothing else touched; scope

### A8, path by path

```
base paths: 325  head paths: 327

ADDED  : ['reviews/chatgpt/2026-08-12T0131Z_supply-protocol-v3.md',
          'specs/2026-08-12T0131Z_supply-protocol-v3.md']
REMOVED: []
CHANGED: ['CONVENTIONS.md', 'DECISION_LOG.md', 'docs/BRANCHING_POLICY.md']
unauthorised additions: NONE
unauthorised modifications: NONE

=== named protected files ===
  GATES.md                                                   identical=True  blob=849a4fbfe62d
  AGENTS.md                                                  identical=True  blob=5e60b5fcd6e9
  pyproject.toml                                             identical=True  blob=9fc6fdd196dd
  CLAIMS.md                                                  identical=True  blob=df75ff4de214
  PROGRESS.md                                                identical=True  blob=5ef6e65a1e3f
  MIGRATION.md                                               identical=True  blob=464d4ab5e6ef
  docs/BRANCH_DELETION_RECORD_2026-08-07.md                  identical=True  blob=c91126d39d79
  docs/amendments/2026-08-09_observation-and-propagation.md   identical=True  blob=642b2541571d

=== every base path under the five prefixes, path by path ===
  scripts/       base=59   identical=59   differing=0  gained=[]
  results/       base=69   identical=69   differing=0  gained=[]
  tests/         base=19   identical=19   differing=0  gained=[]
  derivations/   base=34   identical=34   differing=0  gained=[]
  reviews/       base=20   identical=20   differing=0  gained=['reviews/chatgpt/2026-08-12T0131Z_supply-protocol-v3.md']
  total base paths verified: 201
```

**All 201 base paths under the five prefixes are blob-identical, compared
individually rather than by a directory digest.** `reviews/` gains exactly
one base-absent authorised path. **`AGENTS.md` is unmodified**, as §2
requires. **No test was added** — `tests/` holds 19 paths at base and
head.

**No gate status changed**, measured on the form `GATES.md` actually uses:

```
  "^Status:" lines            base=15  head=15  identical=True
  bare status tokens          base=95  head=95  identical=True
  GATES.md blob identical:    True
```

**The blob identity is the decisive check**; the two token measures are
independent confirmations. §11 records that my first attempt at this
measure matched nothing on either side and was replaced.

### A9 — scope at the pre-report head, verbatim

Manifest mode `exact` (the tool accepts `exact` or `subset`).

```
{
  "base": "0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5",
  "failures": [],
  "head": "5a96682213ffe34929d4e1946ad932ecbaed0d18",
  "mode": "exact",
  "observed_operations": [
    {
      "operation": "modify",
      "path": "CONVENTIONS.md"
    },
    {
      "operation": "modify",
      "path": "DECISION_LOG.md"
    },
    {
      "operation": "modify",
      "path": "docs/BRANCHING_POLICY.md"
    },
    {
      "operation": "add",
      "path": "reviews/chatgpt/2026-08-12T0131Z_supply-protocol-v3.md"
    },
    {
      "operation": "add",
      "path": "specs/2026-08-12T0131Z_supply-protocol-v3.md"
    }
  ],
  "overall": "PASS",
  "tool": "scope_checker"
}
EXIT STATUS: 0
```

**PASS, exit 0.** 2 additions and 3 modifications at the pre-report head;
no forbidden operation observed.

**Intended final manifest**, identical but for the report path, giving
A9's required **3 additions and 3 modifications**:

```json
{
  "mode": "exact",
  "base": "0ab6369a59d83f5f7410ee2b6d6750d12a36bcb5",
  "head": "HEAD",
  "required": [
    {"operation": "add", "path": "specs/2026-08-12T0131Z_supply-protocol-v3.md"},
    {"operation": "add", "path": "reviews/chatgpt/2026-08-12T0131Z_supply-protocol-v3.md"},
    {"operation": "add", "path": "reports/2026-08-12T0131Z_supply-protocol-v3.md"},
    {"operation": "modify", "path": "CONVENTIONS.md"},
    {"operation": "modify", "path": "docs/BRANCHING_POLICY.md"},
    {"operation": "modify", "path": "DECISION_LOG.md"}
  ],
  "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
}
```

The final scope check at the pushed head is post-report evidence.

## 10. A10-pre — Validators

Run individually with `python -m pytest <path>`. Python 3.11.15;
`python -m pytest` = **pytest 9.1.1**, the mandated invocation; the
`pytest` on `PATH` is a different version and was not used.

```
--- python -m pytest tests/test_repository_structure.py ---
4 passed in 0.03s
EXIT STATUS: 0
--- python -m pytest tests/test_si1_governance.py ---
14 passed in 0.08s
EXIT STATUS: 0
--- python -m pytest tests/test_gate_anchors.py ---
18 passed, 2 deselected in 6.42s
EXIT STATUS: 0
--- python -m pytest tests/test_governance_tools.py ---
8 passed in 2.10s
EXIT STATUS: 0
```

**All four exit 0.** The 2 deselected are `@pytest.mark.slow`, excluded by
`pyproject.toml`'s `addopts = "-m 'not slow'"` — pre-existing, unchanged.

### What the validators assert about rule count and branching-policy structure

**Nothing.** Both files gained content, so the question is live.

- **`tests/test_repository_structure.py`** lists `CONVENTIONS.md` in
  `REQUIRED_TOP_LEVEL_FILES` and `docs/BRANCHING_POLICY.md` in
  `REQUIRED_NESTED_PATHS`, both tested by `is_file()` — **existence
  only.** Its remaining test cross-references gate IDs between `CLAIMS.md`
  and `GATES.md`.
- **`tests/test_governance_tools.py`** uses `CONVENTIONS.md` as a
  **fixture path** for the manifest evaluator — a `prefix_hash` criterion
  expected to classify `INVALID_OR_UNDERSPECIFIED`, and
  `required_paths`/`forbidden_paths` entries exercising contradiction
  detection. **It asserts the evaluator's classifications, never the
  file's content.**
- **`tests/test_si1_governance.py`** opens neither file. It reads
  `GATES.md`, `CLAIMS.md`, two derivations, two campaign scripts and one
  report.
- **`tests/test_gate_anchors.py`** contains zero `read_text`/`open` calls
  and zero occurrences of `GATES`; it recomputes numerical anchors and
  reads no repository document at all.

**Consequence, measured rather than asserted.** Rules 1–17 could have been
renumbered, reworded or deleted; Rule 18 could have landed as a delimiter
rule, or not at all; the closed count identity could have been broken —
**and all four validators would still exit 0.** A3's six checks, A4's body
comparison and A5's section digest are the only things standing behind
those invariants, and they were executed once, by me, in this report.
**That is the gap §4 names, and §2 forbids this task to close it.**

## 11. Rule 16 assessment

**Rule 16 is operative: this task adds MATERIAL governance artifacts
bearing on questions Amendment K and Rule 15 already address.**

**§4's candidate junction is confirmed, and I adopt it rather than
replace it.** Named precisely:

    CONVENTIONS.md Rule 18 (eighteen rules)
      + docs/BRANCHING_POLICY.md's superseded register (six entries)
      + DECISION_LOG.md's entry recording both
      + four validators green
    ---------------------------------------------------------------
    available inference:  supersession and review supply are now
                          ENFORCED

**They are recorded, not enforced.** §10 measures how far short: **no test
checks any of the eighteen rules**, and nothing prevents an integration
task from merging a superseded branch without ever reading the register.
**The register is a document a task must choose to consult.** The
Reviewer's assessment states the same junction and adds the precise
mechanism — enforcement would need "a mechanical governance checker or
workflow" that actually reaches the register. **Neither exists.**

**Three additions of my own that the candidate does not cover.**

- **The register will read as a complete census of the programme's
  supersessions.** It has six entries; what it records is **six
  supersessions that durable artifacts establish.** The threshold is
  landed in the file for exactly this reason, and §5.4 makes the
  exclusions auditable. **A register whose exclusions are invisible reads
  as exhaustive.**
- **Rule 18's presence will read as a solved problem — and this time that
  is nearly true, which is the more dangerous case.** It worked here with
  no residual judgement. **But it has been tested once, on one supply,
  where the review helpfully stated its own correspondence in words.** The
  Reviewer's finding names the untested case: a review that discusses this
  specification but names neither digest nor task. **Rule 18 answers it
  with a STOP rather than a judgement, and that answer has not yet been
  exercised.** One success is not a track record.
- **Two of the six register entries are this rule's own failed landings**,
  and the accumulated artifacts now tell a story of a rule that took three
  attempts. **A reader could infer the rule is therefore fragile.** The
  opposite reading is better supported: **each failure was in a
  specification's acceptance criteria, not in the protocol** — v1's rule
  forbade the act it required, v2's A3 contradicted its own §0. **The
  file-supply mechanism itself has never failed.** That distinction is
  worth stating because the register records the branches, not the
  diagnosis.

## 12. Stops and clarifications

**One primary category per stop; secondary findings separate. Included
even where there were none.**

### `SPECIFICATION_DEFECT`

**None blocking. No stop occurred.** The v2 issue's A3/§0 contradiction is
resolved: A3 now tests for the file-supply rule's content and for the
delimiter concepts' **absence**, and all six checks pass against the text
§0 directs. **The two instructions that were mutually unsatisfiable now
agree.**

**Secondary, non-blocking — §0's historical prose retains three remnants
of the delimiter version.** §0 was substantially corrected in this issue
(the tally is now "five distinct failure modes across nine attempts", and
the blank-line clause is expressly declared moot rather than generalised).
What remains:

    "**That is the eighth instance**, and it is the mode a standing rule
     must fix, because no amount of care by a sender prevents a
     specification from containing the delimiter it names."

  — **no standing rule about delimiters is now proposed**, so "the mode a
  standing rule must fix" no longer has a referent.

    "Eight attempts produced five failure modes"      (§0, rule preamble)
    "five distinct failure modes across nine attempts" (§0, opening)
    "Reviews were pasted, and failed eight times."     (§0, evidence)

  — **three different counts of the same history**, now nine attempts
  counting this one. Affects no criterion; the operative rule is
  count-independent.

**Secondary, non-blocking — the Reviewer's two points, both confirmed.**
Its finding that correspondence remains a check the executor performs is
correct and I have answered it directly in §4.3 rather than by agreement:
**bounded by a stated criterion with a stated failure action, so not the
uncontrolled judgement that broke the delimiter protocol** — and §4.2
states which marker was used, as it asks. Its second point, that
"Specifications have been supplied as files throughout" is historical
justification rather than an acceptance predicate, is also correct, **and
this task falsifies the claim as stated**: this specification arrived
pasted (§4.4). **Nothing in the approval or in Rule 18 depends on it**,
which is exactly what the Reviewer said.

**Not corrected: §2 authorises no edit to the specification**, and the
specification is committed as commit 1.

### `ENVIRONMENT`

**None. Neither of Rule 13's two diagnostic orders was exercised**,
because no environment failure occurred. Rule 13 carrying two conflicting
orders remains a known open item, untouched here. Nothing was installed.

### `OBSERVATION_METHOD_ERROR`

**One, caught by its own output before anything rested on it.** **My first
gate-status measure matched nothing and reported success.** The pattern
`^\*\*Status:\*\*\s*(.+)$` returned **0 tokens at the base and 0 at the
head**, and compared them equal — **an empty comparison presented as
evidence of no change.** `GATES.md` writes status as `Status: PASS (…)`,
without bold. Re-measured: **15 `^Status:` lines on both sides, identical**,
and 95 bare status tokens on both sides, identical. **The decisive check
was always the blob identity**, which held throughout; the defect was that
a vacuous measure was about to be reported alongside it as if it added
something. **Reported because an empty match that returns `True` is the
most dangerous kind of green.**

**One methodological choice, recorded rather than classified as an error.**
The branch scan's vocabulary was widened from 7 patterns to 13 for §1's
fact-not-word threshold, before any negative conclusion was drawn. The
first issue's narrower vocabulary would have understated the evidence for
the one branch the relaxation was written for.

### `REPOSITORY_DEFECT`

**None introduced. One pre-existing gap measured**, and it is the known
open item §4 names: **no validator asserts anything about
`CONVENTIONS.md`'s rule count or `docs/BRANCHING_POLICY.md`'s
structure** — both existence-checked only. §10 gives the per-validator
evidence. **§2 forbids adding a test and none was added.**

**A second instance of the same gap, now with two data points: nothing
mechanical inspects a specification for internal consistency.** The v1 and
v2 defects both reached execution and were caught by reading. **The
programme's guard against specification defects is currently an
executor.**

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`

**None.** The first issue's single instance,
`review/role-model-and-executors`, is resolved by §1's revised threshold
and is a supplied register member with its tip verified unchanged at
`10c260b96882ac12610f78840aeeabd07be2d7cb`. **No branch remains in the
suggestive-but-unestablished category**, and §5.4 records why each of the
44 exclusions falls outside it.

## 13. Ambiguous, unsatisfiable, or would have specified differently

- **A3's "pasted" check needed a mapping rather than a literal match**
  (§6). The landed rule's STOP clause covers a pasted review under "no
  file is supplied" and never uses the word. **A future A3 could say
  "a STOP whose conditions cover a missing, pasted or non-corresponding
  review", making the check unambiguous** without inviting an executor to
  add a clause so that a word appears.
- **A0's stop-path clause is well specified and went unused.** Recorded
  because a clause added after two improvised stops deserves confirmation
  that it was read and would have been followed, not silence.
- **§1's "What to add" blockquote is the text to land; the paragraphs
  after it are specification prose** — and this issue's kind-grouping
  paragraph and entry threshold sit outside the blockquote while clearly
  belonging in the file. **I landed both**, and §7 states the two places
  where landed text necessarily differs from the specification's ("this
  task" → the branch name; an instruction to the executor omitted rather
  than transcribed). **A future specification could mark the boundary
  explicitly**, since the previous issue's ordinal defect only bit if that
  paragraph was landed and nothing said whether it should be.
- **A2's disjunction — digest OR task name — is load-bearing and should
  stay.** The digest alone is unusable: commit 1 fixes it, and the review
  precedes commit 1 (§4.2).
- **A5's "report that section's before and after explicitly" is literally
  redundant when the two are byte-identical.** §7 prints the section once
  and reports both digests and the boolean. **Flagged in case two literal
  printings were intended**; this is the third issue in which I have read
  it the same way.
- **Nothing was unsatisfiable.** No instruction conflicted with a
  repository rule or with another instruction, so §6's stop-and-report
  clause was not triggered.

## 14. What this task did not do

No science, no gate, no computation. **No gate status changed** and no
gate was registered. No verdict, digest or hash-pinned artifact was
modified. **No branch was deleted and no branch ref changed.** **Neither
superseded branch was touched, reused or deleted** — `7146a093…` and
`40168469…` are unmoved. **No superseded branch was integrated**, and no
assessment was made of whether any branch's content is correct —
**supersession is not a verdict on content.** **No fourth deletion state
was added** and the closed count identity is byte-identical. **The
existing permanently-preserved entry was not edited, replaced or
weakened.** **No test was added.** **`AGENTS.md` was not modified.**
Rules 1–17 were neither renumbered nor reworded. `main` was not moved,
nothing was merged into it, and no PR was opened.
