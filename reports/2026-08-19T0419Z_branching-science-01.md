# Execution report — `P2-BRANCHING-SCIENCE-01`

    OUTCOME     AMENDMENT APPLIED AND LANDED.
                science/ enters the taxonomy; the class receives a merge-mode
                and allowed-ref rule; the retroactive gap is registered as
                G-12. No abort condition fired.

**Specification:** `specs/2026-08-19T0419Z_branching-science-01.md`
**Review:** `reviews/chatgpt/2026-08-19T0419Z_branching-science-01.md`
**Integration base:** `11af14a792c5858b368180d99ab9ee4692a7f698`

**Measurement head for everything below the landing section: the merge
product, `343fad3430c9127a63b448ba963f495c8508b53a`.** Figures depending on
commit 4 or on the push are labelled **INTENDED** or appear in the
post-report layer returned to the Reviewer in chat.

**This specification transcribes a PI ruling and does not adjudicate.** The
ruled text of §5 was landed as ruled. **Nothing in it was reworded.** Two
editorial decisions the ruling did not settle are recorded in full at §"Two
choices the ruling left open" below, so the Researcher can reverse either.

---

## §0 — Binding SHA and provenance (MEASURED, no A1 abort)

    origin URL, verbatim   https://github.com/zetacheng/2-emergent-gravity
    observed origin/main   11af14a792c5858b368180d99ab9ee4692a7f698
    §0 declared base       11af14a792c5858b368180d99ab9ee4692a7f698

**Equal. Not a stale-base stop.**

**Review binding (Rule 18, Amendment N).** Field
`Reviewed specification SHA-256:` **present**, once, populated — checked
before its value.

    sha256 of the specification bytes as committed
      1ead5cd5dcfe6b18508dfafb532ca343f97d170152e5c2526451a111db6f593a
    the review's bound SHA
      1ead5cd5dcfe6b18508dfafb532ca343f97d170152e5c2526451a111db6f593a

**MATCH.** Verdict `APPROVE FOR EXECUTION`.

**A note on how this specification arrived, recorded because it bears on the
binding.** An earlier attempt at this task supplied two attachments that were
byte-identical copies of the review (`f248fc1c…`) with no specification. I
stopped rather than reconstruct the specification from its review, because a
reconstruction would hash to something other than `1ead5cd5…` and would carry
the Reviewer's approval on bytes the Reviewer never saw. **The specification
supplied this turn hashes to the bound value**, and that is the only reason
execution proceeded.

---

## Environment (MEASURED)

**Amendment D step 0.** Execution location `/home/user/2-emergent-gravity`
for the ref reads, then two linked worktrees created at the integration base:
`…/scratchpad/bsci` for the task branch and `…/scratchpad/ibsci` for the
integration branch.

**Rule 13's diagnostic order.** Not shallow; 423 commits on HEAD, 558 across
all refs; Python 3.11.15; pytest 9.1.1; numpy 2.4.6; sympy 1.14.0; ruff
0.15.8; **`scipy` ABSENT.** **No environment failure occurred, so neither of
Rule 13's two diagnostic orders was exercised.** §1a.4 and §12 place the
scipy question outside this task and it is not pursued here.

---

## §2 — Pre-execution measurements

### M1 — Remote `science/*` refs that are ancestors of `main` at `11af14a7`

    command   for each ref returned by
                git ls-remote --heads origin 'refs/heads/science/*'
              run
                git merge-base --is-ancestor <sha> 11af14a7

    observed  total remote science/* refs        40
              ancestors of main at 11af14a7      37

**37, measured.** The read was taken from `git ls-remote` rather than from
local refs, because `docs/BRANCHING_POLICY.md`'s own remote-refs clause makes
the remote the sole authority and records that local refs in this repository
are known to drift.

**The figure in the `P2-POLE-B0-INTEG-01` stop report was 37.** Per M1's own
text that figure is a historical observation and not a target; the measured
value agrees with it, and had it not, the measured value is what §6 would
record. **37 is what G-12 carries.**

### M2 — Test suite

    invocation   python3 -m pytest -q

    merge product 343fad34   332 passed, 2 deselected in 42.23s, exit 0
    base 11af14a7            332 passed, 2 deselected in 39.84s, exit 0

**Identical. No A3 abort.**

Both runs were taken in real git worktrees. **This is deliberate and is worth
one sentence, because the previous task in this line got it wrong:** the
`P2-POLE-B0-INTEG-01` execution first measured its suite in a `git archive`
extraction, which is not a git repository, and six git-history-dependent
governance tests failed as a result. Nothing here was measured outside a
worktree.

### M3 — `git diff --name-only 11af14a7..343fad34`

    CONVENTIONS.md
    docs/BRANCHING_POLICY.md
    docs/GOVERNANCE-DEBT.md
    reviews/chatgpt/2026-08-19T0419Z_branching-science-01.md
    specs/2026-08-19T0419Z_branching-science-01.md

    count 5

**All five are inside the §1b manifest. No A5 abort. C8 passes.**

    P1  docs/BRANCHING_POLICY.md
    P2  CONVENTIONS.md
    P3  docs/GOVERNANCE-DEBT.md      — the register selected under §6
    P4  the spec and review at their authorised paths

**§1b's note is borne out exactly:** the spec and review appear in M3 because
Rule 15 commits them before execution, and an abort condition omitting P4
would have fired on correct execution.

### M4 — Dry-run merge

    git merge-tree --write-tree <integration branch tip> 497151bf
      exit 0
      tree 01a3dd9c351b6ce47bd18f28cec615f349bd5b97
      conflict lines 0

**Conflict-free. No A2 abort.**

### M5 — The branch-name taxonomy block, as observed

**Measured at the base, before any edit.**

    fence opens        :5   ```text
    entries            :6-10
    fence closes       :11

    :6   gate/<gate-name>
    :7   paper/<paper-version>
    :8   review/<review-topic>
    :9   fix/<issue>
    :10  archive/<retired-route>

**Observed span `:5-11`**, agreeing with the orientation figure the
specification quotes, and measured independently of it. The fence-open and
fence-close lines were located by their own commands rather than assumed.

**The form the block uses:** a fenced `text` block, one entry per line,
`<prefix>/<placeholder-in-angle-brackets>`, no bullets and no backticks.
**`science/<scientific-task>` fits that form directly, so §5.1 is applicable
as written and A4 did not fire.**

---

## §5 — The amendment as landed

### 5.1 Taxonomy — landed

    :5   ```text
    :6   gate/<gate-name>
    :7   paper/<paper-version>
    :8   review/<review-topic>
    :9   fix/<issue>
    :10  archive/<retired-route>
    :11  science/<scientific-task>
    :12  ```

**In the block's own form. No existing entry was reordered, reworded or
touched.** The placement decision is recorded below.

### 5.2 New integration section — landed verbatim

A new `## Science branch integration` section, at `:25-40` of the amended
file, carrying **all six ruled statements**:

    :27  `science/*` is a recognized scientific-task branch class.
    :29  Approved science branches integrate by `--no-ff` into a dedicated
    :30  integration branch.
    :32  Squash/rebase integration prohibited.
    :34  During landing, only the integration branch and `refs/heads/main` may be
    :35  pushed.
    :37  Source branch, session branches and unrelated refs must not move.
    :39  `main` advances only by fast-forward from its reviewed evidence base to the
    :40  completed integration head.

**Six statements, landed as ruled.** The only transformation applied was line
wrapping to the file's existing width; no word was added, removed or changed.

### 5.3 Retroactive note — landed verbatim

At `:42-47`, under a `### Retroactive note` subheading:

> Through pre-amendment `main` `11af14a7`, `science/*` was used operationally
> but absent from the formal branch taxonomy and had no policy-level
> merge-mode rule. Historical landed science branches remain accepted; no
> retrospective rewrite or re-merge is authorized.

**The substitution §5.3 authorises was applied and no other.** The ruling's
placeholder for its own commit is replaced by *"pre-amendment `main`
`11af14a7`"*, because a commit cannot cite its own identifier.

**`11af14a7` is named as the pre-amendment tip and NOT as the point from which
the policy takes effect.** The sentence's grammar carries this: *"Through
pre-amendment `main` `11af14a7`"* describes the state that obtained **up to**
that commit. The policy takes effect with this amendment, which is strictly
later than `11af14a7` — it is `343fad34`'s second parent's content, landed
above it. **Nothing in the landed text presents `11af14a7` as an effective
date.**

### 5.4 `CONVENTIONS.md` cross-reference — landed verbatim

At `:215-216`:

> Branch-specific merge mode and allowed-ref policy are defined in
> `docs/BRANCHING_POLICY.md`.

**Placed immediately after `CONVENTIONS.md`'s existing passage on superseded
branches**, which is the one place the file already cross-references
`docs/BRANCHING_POLICY.md` for branch-level policy — so a reader meets the two
references together.

**No merge-mode or ref rule is duplicated there.** Measured over the whole
file after the edit: `no-ff` 0, `fast-forward` 0, `squash` 0, `rebase` 0,
`refs/heads/main` 0. **The cross-reference is the only thing added, and the
single source of truth remains the policy file.**

---

## §6 — Register entry

**The register was selected by reading the three candidates' own stated
scopes, not by preference.**

`docs/GOVERNANCE-DEBT.md:1` calls itself *"Governance debt — an authoritative
register"*, and `:16-19` states why it exists in the terms that decide this
question:

> Two registers already existed at the evidence base and both are
> science-side: `derivations/P2-DEFERRED-ITEMS.md`, whose own text says
> entries are added by PI decision, and
> `derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md`, created by `C3` for the
> C-check line. **There was no governance-side register.**

**`G-1` is a class-level governance gap in a policy document.** The other two
registers scope themselves science-side — one to PI-deferred scientific work,
one to the C-check line. **`docs/GOVERNANCE-DEBT.md` is the only register whose
stated scope admits it**, and `:12-14` describes this item's discovery route
exactly — quoted here **as it read at the base, before this task's own edit to
its numerals**: *"Governance debt has been carried in task reports… Three of
the eleven entries below were found only because a later task tripped over
them."*

**No location was coined and no vocabulary was invented.** The disposition
`RULED` — *"a PI ruling settled it"* — is taken from the register's own list at
`:25-31`, and `G-07` was used as the format model.

### The entry as landed

**`## \`G-12\` — \`science/\` was an operational branch class the policy did
not name`, Disposition RULED**, at `:258` of the amended register. It records
the pre-amendment absence of `science/` from the taxonomy, the absence of any
policy-level merge-mode rule for any class, **the M1-measured integer 37 with
the command that produced it**, and the ruling that historical landings remain
accepted with no retrospective rewrite or re-merge authorised. **One entry for
the class, not one per branch**, stated in the entry itself.

**The tally at `:37-44` was updated to match:** `RULED` from 1 to 2, entries
from 11 to 12.

---

## §7 — Acceptance criteria

**Every criterion below was verified by reading the landed text at the merge
product, not by counting file-wide hits.** §8's exclusions are stated with
each search that was performed by search.

    C1   PASS   science/<scientific-task> present at :11 of the taxonomy
                block located by M5. Verified by reading the block :5-12,
                not by a file-wide count of "science" — which would also
                match "scientific-task" in the entry itself, "scientific"
                in the Rules section, and the whole of §5.2's prose.
    C2   PASS   all six ruled statements present at :27-40. Read
                individually and listed above.
    C3   PASS   the retroactive note is present at :44-47, names 11af14a7
                as the pre-amendment tip, and does not present it as the
                effective date. Verified by reading the sentence.
    C4   PASS   the cross-reference is present at :215-216 and CONVENTIONS.md
                restates no merge mode or ref rule: no-ff 0, fast-forward 0,
                squash 0, rebase 0, refs/heads/main 0. The "merge" and "push"
                collisions §8 names were avoided by searching the specific
                mode tokens rather than the bare words.
    C5   PASS   G-12 exists and carries the M1-measured integer 37.
    C6   PASS   M1-M5 recorded above with observed values and the commands
                or reads used.
    C7   INTENDED — the landing is below; measured values are in the
                post-report layer.
    C8   PASS   M3 lists five paths and all five are in the §1b manifest.
    C9   PASS   scripts/recon2026/proca_curved.py blob at the merge product
                is 03f46905e5798fb7f6880dfae9ed5a1931be895b, unchanged from
                the base. §12's freeze is intact and §1a.5 was honoured.

---

## Two choices the ruling left open, recorded so they can be reversed

**The ruling fixed the text. It did not fix these two, and I record both
rather than letting an editorial decision pass as a transcription.**

### Where in the taxonomy block `science/` goes

The existing five are ordered `gate`, `paper`, `review`, `fix`, `archive` —
not alphabetical, and roughly by workflow with the terminal class last.
**§5.1 says to add the entry; it does not say where.**

**I appended it after `archive/`.** The reason is that appending is the only
placement that reorders nothing: any position among the existing five would
have moved an existing line, and moving a line the ruling did not mention is a
larger act than adding one. **The cost is that an active class now sits below
a terminal one.** If the Researcher prefers `science/` before `archive/`, that
is a one-line move and this report is the record that it was a choice.

### Whether to update the register's two prose counts

At the base, `docs/GOVERNANCE-DEBT.md:13` said *"Three of the eleven entries
below"* and `:274` said *"Three of its eleven entries"* — the latter now at
`:317`, the added entry having moved it down. **Adding `G-12` made both
false.**

**I updated them to "Four of the twelve".** Two reasons, and the second is
measured rather than editorial: both sentences are present-tense claims about
what the file contains, so leaving them would have landed a file that
contradicts its own tally at `:37-44`; and **`G-12` genuinely is a fourth
instance of the thing they describe** — it was found because
`P2-POLE-B0-INTEG-01` tripped over it, which is documented in that task's stop
report.

**This is the one edit in this task that goes beyond the ruled text**, it is
confined to two numerals, and it is flagged here so the Researcher can revert
it if the sentences were meant to be anchored to the register's creation by
`C-c` rather than to its current contents.

---

## §1a — Non-objectives, all honoured

`science/pole-b0-milestone-scope` was **not** merged and did not move. No
historical `science/*` branch was modified, re-merged, re-verified or
retrospectively authorised — **M3 lists five paths and none of them is a
branch operation.** `AGENTS.md` was **not** amended; its blob is untouched.
`docs/local/execution_environment.md` was **not** touched.
`scripts/recon2026/proca_curved.py` was **not** touched, and C9 records its
unchanged blob. **No POLE construction register entry was created** — `G-12`
is the branch-policy gap and nothing else.

**And the ruling was not adjudicated.** Where §5 gave text, the text was
landed. Where the ruling was silent — the two choices above — the silence is
reported as silence and the choice is named as mine.

---

## §11 — What this task does not establish

**It produces no physical number, moves no gate, and adds no support to the
programme.** `P2-PHASE-01` does not move; it remains `Status: PROPOSED`.
**What it removes is a rule-lookup failure that blocked an integration**, and
nothing more. The `science/*` branches already landed are not made more
correct by being named in a taxonomy, and the amendment does not claim they
are.

---

## Stops and clarifications

**`SPECIFICATION_DEFECT`** — **none.** Two things are worth recording on the
positive side. §1b's note anticipated that P4 must be in the manifest or A5
would fire on correct execution, and M3 confirms it would have. And §0a's
bootstrap clause is what made this task executable at all: delegating its own
merge mode to the policy it creates would have been circular, and the
specification saw that before the executor met it.

**`ENVIRONMENT`** — `scipy` absent for the fifteenth consecutive task. No
environment failure occurred, so neither of Rule 13's two diagnostic orders
was exercised. **§1a.4 and §12 put the scipy question outside this task and it
was not pursued**; §12's reasoning — that the file's blob is pinned in three
landed records and a confirmation not mentioning the freeze does not authorise
an unfreeze — is recorded as landed evidence, and C9 shows the blob intact.

**`OBSERVATION_METHOD_ERROR`** — none in this task. The suite was measured in
real git worktrees on both sides, which is the correction the previous task in
this line had to make mid-execution. §8's three named collisions were handled
by reading: the taxonomy check read the block rather than counting `science`
file-wide; the `CONVENTIONS.md` check searched the specific mode tokens rather
than the bare words `merge` and `push`.

**`REPOSITORY_DEFECT`** — **one, and this task is its repair.** The gap
`G-12` records is the subject of the amendment, and it is registered rather
than merely fixed, because `docs/GOVERNANCE-DEBT.md:33` is explicit that
*"Nothing here is closed by being written down"* — and because the gap's
cause was not that anyone erred but that nothing checks a policy against
practice. **`G-03`'s reservation applies to this repair as much as to any
other: nothing detects the next such gap.**

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`** — **none blocking, one
observation.** The specification labels the register item `G-1`; the register's
own entries run `G-01` through `G-11`. **I entered it as `G-12`, following the
register's sequence, and said so in the entry's own second paragraph** so the
mapping from the specification's label to the register's ID is on the page
rather than in this report alone. `G-1` would have read as a near-collision
with `G-01`. §6 forbids coining a *location*; the ID follows the location's
existing form, which is the opposite of coining one.

---

## Post-commit correction, recorded rather than rewritten

**Commit 5 of this branch corrects two citations in the section above, and
this note is part of that commit.**

As first committed, the report quoted `docs/GOVERNANCE-DEBT.md:12-14` and
`:317` with their **pre-edit** wording while giving **post-edit** line
numbers — a report about citation precision citing imprecisely. The two
sentences now say which state each figure belongs to.

**The correction was made as a new commit and not by amending commit 4**,
because §4 prohibits history rewrite and lists it separately from force-push.
The cost is that the report's own commit is not its final text; the benefit is
that nothing in this branch's history was rewritten to hide a slip. **Nothing
substantive changed — no measurement, no criterion result, and no landed
text.**
