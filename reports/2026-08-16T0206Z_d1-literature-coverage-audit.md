# Report — `D-1`: literature coverage audit for reflection positivity

    branch      science/d1-literature-coverage-audit
    base        bfef924c368658cac85c04ed18d96eb4450afba6   (authoritative main)
    measured at commit 3, 8625c8991d407254f4e74bae71d5a485ee8fa29e
    main        NOT TOUCHED. No merge. Integration is a separate task.

**RESULT: the `§1` network precondition FAILED. The audit was not
conducted, and per `A3` criteria `A4` through `A8` were not attempted.**
**This is reported as the result, not as an incomplete run.**

---

## 1. `A3` — the `§1` precondition, before any content

**MEASURED 2026-08-16 in the execution container. Every host attempted, and
the outcome of each.**

### 1.1 Fetch path 1 — HTTPS through the container's egress proxy

    HOST                     PATH                                        OUTCOME

    arxiv.org                /abs/hep-lat/9707022                        curl (56) CONNECT tunnel failed, response 403 — http_code 000
    export.arxiv.org         /abs/hep-lat/9707022                        curl (56) CONNECT tunnel failed, response 403 — http_code 000
    doi.org                  /10.1016/0003-4916(78)90039-8               curl (56) CONNECT tunnel failed, response 403 — http_code 000
    link.springer.com        /article/10.1007/BF01645738                 curl (56) CONNECT tunnel failed, response 403 — http_code 000
    www.sciencedirect.com    /science/article/pii/0003491678900398       curl (56) CONNECT tunnel failed, response 403 — http_code 000
    projecteuclid.org        /journals/communications-in-mathematical-physics
                                                                         curl (56) CONNECT tunnel failed, response 403 — http_code 000
    pos.sissa.it             /105/267/pdf                                curl (56) CONNECT tunnel failed, response 403 — http_code 000
    api.semanticscholar.org  /graph/v1/paper/DOI:10.1016/0003-4916(78)90039-8
                                                                         curl (56) CONNECT tunnel failed, response 403 — http_code 000
    inspirehep.net           /api/literature?q=arxiv:hep-lat/9707022     curl (56) CONNECT tunnel failed, response 403 — http_code 000
    www.osti.gov             /                                           curl (56) CONNECT tunnel failed, response 403 — http_code 000
    inis.iaea.org            /records/w5b1b-sr829                        curl (56) CONNECT tunnel failed, response 403 — http_code 000
    example.com              /                                           curl (56) CONNECT tunnel failed, response 403 — http_code 000

**MEASURED: eleven scholarly or bibliographic hosts attempted, ZERO
reached.** `§1` names `arxiv.org`, `doi.org` and "any publisher host you
would need"; **all three classes were attempted, and a preprint mirror, two
bibliographic APIs and two repository hosts besides.**

`example.com` is a **non-scholarly control** and fails identically.

### 1.2 Fetch path 2 — the environment's own fetch tool, a distinct client

**Tried so the finding does not rest on one client's configuration.**

    arxiv.org, export.arxiv.org, doi.org, link.springer.com,
    www.sciencedirect.com, projecteuclid.org, pos.sissa.it,
    inis.iaea.org, api.semanticscholar.org, example.com

    EVERY HOST:  EGRESS_BLOCKED — "Access to <host> is blocked by the
                 network egress proxy."

**MEASURED: two independent fetch paths, ten and twelve hosts, the same
outcome on every one.**

### 1.3 Controls — the container's network is not down

    pypi.org      /simple/     http_code 200   REACHED
    github.com    /            http_code 400   REACHED (gateway-level response)

**Outbound HTTPS works. What is unavailable is scholarly and bibliographic
egress, specifically, by policy.** **The control matters**: without it, a
uniform failure is equally consistent with a broken proxy, and the finding
this task is meant to establish — *this environment cannot do literature
work* — would not be distinguishable from *this container is temporarily
broken*.

### 1.4 The proxy's own account

**MEASURED**, read from the container's proxy status endpoint, once per
attempted scholarly host:

    kind    connect_rejected
    detail  gateway answered 403 to CONNECT (policy denial or upstream failure)

**This is an organisational policy denial.** The environment's operating
instructions state that policy denials of this kind are to be reported and
not retried. **No circumvention was attempted**: TLS verification was not
disabled, `HTTPS_PROXY` was not unset, and no alternative route was sought.

### 1.5 A search path returned results, and was deliberately not used

**Disclosed in full, because a reader must not conclude that nothing
whatever came back, and because concealing it would leave the strongest
objection to this report's conclusion unstated.**

**One web-search invocation was made as a probe of a third and distinct
path.** It returned result titles, URLs, and prose synthesised from
snippets by the search backend.

**It fetched nothing.** No document was retrieved, no page bytes were
obtained, and **no evidential depth — listing, abstract or full text —
could be established for any work.** **Every URL it returned is among the
hosts blocked in `§1.1` and `§1.2`**, so nothing it named could then be
opened.

**Judgement, and it is mine, and it is reported so the Reviewer can
disagree with it:** search-result prose is not a fetch. `§3` requires that
a work supporting a conclusion be *fetched to the evidential depth the
conclusion requires*, and `§1` forbids substituting recollection for a
fetch. Snippet-derived prose is a summary produced by a model over material
this container cannot open — **the recalled-content failure `D-1` exists to
correct, wearing the costume of a citation.**

**No work, identifier, title, claim or statement from that probe appears in
the coverage artifact, in this report, or anywhere in `D-1`.**

**And the alternative reading changes nothing.** If the PI or the Reviewer
judges that returning search metadata constitutes "reaching a scholarly
source", the audit is still not conductable: `§3`'s fetch requirement
cannot be met for **any** work, so every verdict would be `NOT
DETERMINABLE` on the per-work precondition instead of the global one.
**The outcome is invariant under the disputed reading**, which is why this
is reported as a clarification and not as a stop needing resolution before
the task can end.

### 1.6 The consequence

**The `§1` GLOBAL PRECONDITION fires. The task STOPS at the
precondition.**

**Per `A3`, criteria `A4` through `A8` were not attempted.** The finding
established is the one `§1` says it is:

> **conducting this audit requires an executor with library or scholarly
> network access; this container does not have it, and no amount of care
> within it would substitute.**

**`§1` designates this a successful outcome of the task, and `§11` states
the task is complete when it is reported.** It is reported.

---

## 2. `A1` — refs

**MEASURED**, `git ls-remote origin refs/heads/main`:

    bfef924c368658cac85c04ed18d96eb4450afba6    refs/heads/main

**Confirmed `bfef924c…`, as the specification's evidence base requires. It
has not advanced. No stop on this criterion.**

**Clarification, carried forward and unchanged.** The container's local
`refs/heads/main` is a stale artefact of how the working copy was created
and is a strict ancestor of the authoritative ref. **Every measurement in
this report reads the remote ref or the fetched object, never the local
`main` ref.** The branch was cut from `bfef924c…` by explicit SHA, not by
branch name.

## 3. `A2` — the pre-execution review

**MEASURED.**

    field `Reviewed specification SHA-256:` PRESENT      yes, line 4
    value carried by the review                          1739dfe4fa3e94f613208b064cd63ea46e1a5c3235886f2bdb7c8d9b1fbe2384
    SHA-256 of the committed specification bytes         1739dfe4fa3e94f613208b064cd63ea46e1a5c3235886f2bdb7c8d9b1fbe2384
    MATCH                                                yes
    review verdict                                       APPROVE FOR EXECUTION
    committed unedited                                   yes — the committed blob is byte-identical to the supplied review

**The field's presence was checked before its value was compared**, in that
order, as `A2` requires. **A review carrying no digest field at all is a
different failure from one carrying a wrong digest**, and this programme has
met the first: the `D-pre-A`/`A2` integration's first review artifact had no
digest field whatever and the task stopped before creating a branch.

**A finding about this review's content, reported and NOT a stop — see
`§13.5`.** The review's finding 10 enumerates "acceptance criteria A1–A11"
and describes `A10` as the Rule 16 assessment and `A11` as the no-`main`
scope. **The specification it is digest-bound to carries `A1`–`A15` plus
`A13-final`**, in which `A10` is the frozen scope manifest, `A11` is
nothing-existing-changed, and the Rule 16 assessment is `§9`, not a
criterion at all. **The digest matches; the description of the criteria does
not.**

## 4. `A4` — NOT ATTEMPTED

**`A3` states that if the precondition failed the task stops there and `A4`
through `A8` are not attempted.** The precondition failed. **`A4` was not
attempted, and no part of `derivations/P2-LATTICE-MICROSPEC-01_tm-rp-scope.md`
was read for its content by this task.**

**Not attempted is not the same as attempted and empty**, and this report
does not report a zero where it performed no measurement.

## 5. `A5`, `A6`, `A7`, `A8` — NOT ATTEMPTED

**All four, for the same reason, per `A3`.**

    A5   identifiers and fetch depth                     NOT ATTEMPTED
    A6   seven axes and theorem-specific hypotheses      NOT ATTEMPTED
    A7   four verdicts and discrete burden accounting    NOT ATTEMPTED
    A8   works encountered and not pursued               NOT ATTEMPTED

**MEASURED, and it is the only number these criteria yield here: zero works
fetched, zero works identified for the record, zero statements marked
`RECALLED` — because no work was recorded at all, at any depth.**

**On `A7` specifically, and this is the one place where two instructions
pull against each other.** `§5` defines a verdict `NOT DETERMINABLE` whose
stated meaning is *the precondition failed, or the works could not be
fetched*, and `§5`'s burden rule for it is *no burden conclusion at all*.
**So the verdict taxonomy plainly contemplates this outcome.** But `A3` says
`A7` is **not attempted**, and recording four verdicts is attempting it.

**I did not decide which prevails, and I did not record verdicts.** `A3` is
the more specific instruction, it is explicitly about this case, and not
recording is the conservative side: a reader can be told a verdict was never
taken, whereas a verdict written down cannot be un-read. **The tension is
reported at `§13.1` for the Reviewer to rule on.** A reader should not infer
from the absence of verdicts that `§5` failed to anticipate the case: **it
anticipated it precisely.**

## 6. `A9` — no selection, no route design

**MEASURED. Searched the coverage artifact, this report, and all four commit
messages** for `select`, `prefer`, `rank`, `better`, `best`, `favour`,
`eliminate`, `recommend`, and for route-design phrasings — *the proof would*,
*one would prove*, *constructing the proof*, *route to a proof*.

    coverage artifact     1 match, line 122, and it is a DENIAL:
                          "No candidate is selected, eliminated, ranked or
                           preferred, no proof route is designed..."
    this report           matches occur only in this criterion's own
                          statement of the search and in denials
    commit messages 1–4   0 matches

**No sentence anywhere selects, eliminates, ranks or prefers a candidate,
and none describes how a missing proof would be constructed.**

**Treatment length per candidate, MEASURED as occurrences of each candidate
name in the coverage artifact:**

    naive        0
    Wilson       0
    staggered    0
    overlap      0

**The lengths do not differ. All four are zero.**

**The reason, and it is the reason `A9` asks for:** `A9` expects unequal
lengths, because coverage genuinely differs between candidates and levelling
that would be a distortion. **Here nothing was fetched, so no candidate has
any coverage treatment at all**, and the equality is not levelling — it is
the arithmetic of an audit that did not run. **A future executor with
network access should expect the lengths to differ, and should not read this
report's uniform zero as a precedent for uniform treatment.**

## 7. `A10` — scope, against the frozen manifest

**MEASURED, base to commit 3:**

    A   derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md
    A   reviews/chatgpt/2026-08-16T0206Z_d1-literature-coverage-audit.md
    A   specs/2026-08-16T0206Z_d1-literature-coverage-audit.md

    3 additions, 0 modifications
    status-code tally: 3 × A, and no other code appears

**INTENDED, base to commit 4: 4 additions, 0 modifications** — the fourth
being this report. **INTENDED and not MEASURED: this report is written
before the commit that contains it.**

**`modify:` is `[]` and remained so.** **None of the forbidden operations —
delete, rename, copy, type change, unmerged, unknown — appears.**

**The `{HHMM}Z` token is `0206Z`, fixed once by commit 1 and reused
unchanged in commits 2 and 4. No path was chosen by me**; all four are
transcribed from the manifest with the token substituted.

**If `§1` fails, commit 3 is still written** — `A10` says so, and it was.
**It records the precondition failure and the hosts attempted, and nothing
else.**

## 8. `A11` — nothing existing changed

**MEASURED, blob by blob, every path present at the evidence base:**

    paths at the evidence base      433
    compared                        433
    blob-identical                  433
    differing                         0
    missing at head                   0

    paths at head                   436   (433 + this task's three)

**The count at the base is 433, where the preceding task reported 426.**
That is the seven paths `D-pre-B0`'s integration landed on `main`, and it is
the expected arithmetic, not a discrepancy.

**No existing file was modified. No register entry was added anywhere.**

## 9. `A12` — gate invariants and pins

**MEASURED at commit 3, all four:**

    ^## P2- count                        14
    P2-PHASE-01                          Status: PROPOSED
    first prerequisite                   Prerequisite state: SATISFIED
    second prerequisite                  Prerequisite state: SATISFIED
    pin at line 1017                     MATCH
    pin at line 1040                     MATCH

**The pins were verified by recomputation, not by reading them twice:**

    GATES.md:1017   4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
    sha256 of derivations/P2-PHASE-01_microscopic_parameter_domain.md
                    4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214

    GATES.md:1040   e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
    sha256 of derivations/P2-PHASE-01_input_admissibility_contract.md
                    e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3

## 10. `A13` — the checker, MEASURED at commit 3

    base   bfef924c368658cac85c04ed18d96eb4450afba6
    head   8625c8991d407254f4e74bae71d5a485ee8fa29e   (commit 3)

    run 1 INCLUSIVE   exit 0   PASS   sha256 78721ce6b714c2af07247ee0281c3cdebe7cb11466985063215bf8a45086e064
    run 1 EXCLUSIVE   exit 0   PASS   sha256 c8f1974d4b7111eb47c8f58dd8b7a20f10f3cf4fbe5360778c6624a20627c0ec
    run 2 INCLUSIVE   exit 0   PASS   sha256 78721ce6b714c2af07247ee0281c3cdebe7cb11466985063215bf8a45086e064
    run 2 EXCLUSIVE   exit 0   PASS   sha256 c8f1974d4b7111eb47c8f58dd8b7a20f10f3cf4fbe5360778c6624a20627c0ec

    P1 PASS   P2 PASS   P3 PASS   P4 PASS
    P5 NOT_APPLICABLE — no merge commit in range
    P6 PASS   P7 PASS   P8 PASS
    P9 NOT_APPLICABLE — range adds no report

    overall PASS in all four invocations.

**`P5` and `P9` are `NOT_APPLICABLE`, which does not make the run
INCOMPLETE**, and both reasons are structural: this task makes no merge, and
commit 3 is measured before the report exists. **Neither is a green over
nothing that was silently converted.**

### 10.1 What `RUN 1` did

**MEASURED: `RUN 1`'s default subject selection selected exactly one
specification** — this task's own, the only one in range:

    specs/2026-08-16T0206Z_d1-literature-coverage-audit.md
    stated 4 / 0    counted 4 / 0    parse OK

**`RUN 1` and `RUN 2` produced BYTE-IDENTICAL output**, digest for digest, at
each prospectivity reading. That is expected here and is not evidence that
the two runs are the same check: **`RUN 2` names the subject and `RUN 1`
discovers it, and they coincide only because the range contains one
specification.**

**The `C3` multi-specification residual did not arise**, and the reason is
that there is one declaring specification, not that declarations agreed.
**The diagnosis is unchanged and the residual remains unregistered:**
`_declarations_from_specs` raises on a *difference* between declarations,
so a range with a single specification cannot trigger it and a range with
two agreeing ones does not either. **`D-pre-B0` established the second half
of that; this task exercises the first.**

### 10.2 `P1`'s counted set, and why it is not the diff

**MEASURED: `P1` counted 4 and reported `counted_set` as the four LITERAL
manifest paths**, `…2026-08-XXT{HHMM}Z…` token and all — not the paths
actually added.

**This is `P1` working as specified and is stated here so it is not mistaken
for a discrepancy with `§7`'s measured 3 additions.** `P1` compares a
specification's `stated:` total against the paths its own manifest block
enumerates. **It is an internal-consistency check on the specification, not
a comparison against the diff**, and its `does_not_establish` field says so.

### 10.3 `declared_source`, `P3` and `P7`

    P3   PASS   declared_source: specification   declared: ['DECISION_LOG.md']
    P7   PASS   declared_source: specification   section_count_head 14

**`P7` reports FOURTEEN sections. `PASS` at zero would have been a STOP,
and it is not zero.**

**MEASURED: `DECLARATION_CONFLICT` appears ZERO times in all four
outputs.**

**`DECISION_LOG.md` is not modified by this range**, so `P3` passed without
exercising the append property; the checker still reports
`base_is_byte_prefix_of_head: true` over 89541 identical bytes.

### 10.4 `RUN 1` config, verbatim — observational, governs nothing

    {
      "base": "bfef924c368658cac85c04ed18d96eb4450afba6",
      "head": "8625c8991d407254f4e74bae71d5a485ee8fa29e",
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 10.5 `RUN 2` config, verbatim — stop-governing

    {
      "base": "bfef924c368658cac85c04ed18d96eb4450afba6",
      "head": "8625c8991d407254f4e74bae71d5a485ee8fa29e",
      "specification_paths": ["specs/2026-08-16T0206Z_d1-literature-coverage-audit.md"],
      "append_only_paths": ["DECISION_LOG.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "EXCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `INCLUSIVE` reading is the same file with `"inclusivity": "INCLUSIVE"`.

**No value in either config is one I chose**, and **neither the config nor
this specification's declarations were adjusted to make `RUN 2` pass** —
`§10` forbids both, and neither was touched. **`RUN 2` passed on its first
invocation at both readings.**

### 10.6 `RUN 2` output, verbatim, `INCLUSIVE` reading

**Reproduced byte for byte as the checker emitted it, indented by four
spaces for the code block and otherwise unaltered.**

    {
      "base": "bfef924c368658cac85c04ed18d96eb4450afba6",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "8625c8991d407254f4e74bae71d5a485ee8fa29e",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "append_only": [
                "DECISION_LOG.md"
              ],
              "authorised_gates": [],
              "counted": 4,
              "counted_add": 4,
              "counted_modify": 0,
              "counted_set": [
                "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md",
                "reports/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md",
                "specs/2026-08-XXT{HHMM}Z_d1-literature-coverage-audit.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-16T0206Z_d1-literature-coverage-audit.md",
              "stated": 4,
              "stated_add": 4,
              "stated_modify": 0,
              "stated_record": "stated: 4 additions, 0 modifications"
            }
          ],
          "id": "P1",
          "status": "PASS",
          "title": "scope manifest arithmetic"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "commits": [
              {
                "adds_review": false,
                "commit": "8f3852d16c85f36c82bc2f11a957f7301b9f5265",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "bc625b1101b7b9b1c0b59e7d7202f4ec3ac830d8",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "8625c8991d407254f4e74bae71d5a485ee8fa29e",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md"
                ]
              }
            ],
            "first_review_commit": "bc625b1101b7b9b1c0b59e7d7202f4ec3ac830d8",
            "first_work_commit": "8625c8991d407254f4e74bae71d5a485ee8fa29e",
            "in_scope": 3,
            "out_of_scope": []
          },
          "id": "P2",
          "status": "PASS",
          "title": "Rule 15 commit order"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
          "evidence": {
            "declared": [
              "DECISION_LOG.md"
            ],
            "declared_by_specification": [
              "DECISION_LOG.md"
            ],
            "declared_key": "append_only",
            "declared_source": "specification",
            "paths": [
              {
                "base_bytes": 89541,
                "base_is_byte_prefix_of_head": true,
                "commits_with_deletions": [],
                "deleted_lines_base_to_head": 0,
                "head_bytes": 89541,
                "path": "DECISION_LOG.md",
                "status": "PASS"
              }
            ],
            "specification_paths_read": [
              "specs/2026-08-16T0206Z_d1-literature-coverage-audit.md"
            ],
            "supplied_by_config": [
              "DECISION_LOG.md"
            ]
          },
          "id": "P3",
          "status": "PASS",
          "title": "append-only on both measures"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "entries": [
              {
                "branch": "fix/pi-decisions-and-deferred",
                "commit": "52f651174dc1fef03b4fb9276078fa1f08d94bd7",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "fix/pi-decisions-v2",
                "commit": "ebd531ab568aaffabd86a4a94d925a711e62aa36",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-v2",
                "commit": "40168469608618aef6812735ff70e32de0e3cbc8",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-and-superseded",
                "commit": "7146a093c65788a57d63a747b71d86edb91eddc6",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "review/role-model-and-executors",
                "commit": "10c260b96882ac12610f78840aeeabd07be2d7cb",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "gate/p2-land-diquark-line",
                "commit": "d64cd912ca9ff78a85787f0e54f345f474cdb192",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              }
            ],
            "register_path": "docs/BRANCHING_POLICY.md"
          },
          "id": "P4",
          "status": "PASS",
          "title": "superseded branches are not merged"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the executor derived the parentage values independently; three correct values are equally consistent with fresh recomputation and with one field copied into another. The diquark task's shared-rationale defect would pass this check.",
          "evidence": {
            "merges": []
          },
          "id": "P5",
          "reason": "no merge commit in range",
          "status": "NOT_APPLICABLE",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "8f3852d16c85f36c82bc2f11a957f7301b9f5265",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "bc625b1101b7b9b1c0b59e7d7202f4ec3ac830d8",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "8625c8991d407254f4e74bae71d5a485ee8fa29e",
              "matches": [],
              "status": "PASS"
            }
          ],
          "id": "P6",
          "status": "PASS",
          "title": "commit-message hygiene"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
          "evidence": {
            "added_sections": [],
            "authorised_modified": [],
            "declared": [],
            "declared_by_specification": [],
            "declared_key": "authorised_gates",
            "declared_source": "specification",
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "specification_paths_read": [
              "specs/2026-08-16T0206Z_d1-literature-coverage-audit.md"
            ],
            "supplied_by_config": [],
            "unauthorised_changed": []
          },
          "id": "P7",
          "status": "PASS",
          "title": "gate integrity"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "first_commit": "8f3852d16c85f36c82bc2f11a957f7301b9f5265",
            "first_commit_paths": [
              "specs/2026-08-16T0206Z_d1-literature-coverage-audit.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-16T0206Z_d1-literature-coverage-audit.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-16T0206Z_d1-literature-coverage-audit.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {},
          "id": "P9",
          "reason": "range adds no report",
          "status": "NOT_APPLICABLE",
          "title": "reports carry a Stops and clarifications section"
        }
      ],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 3,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

**The `EXCLUSIVE` output differs from the above in exactly one line** —
`"inclusivity": "EXCLUSIVE"` — **MEASURED by diff, which reports a single
changed line at position 252 and nothing else.**

## 11. `A14`, `A15` — validators and hygiene

**`A14`, MEASURED, `python -m pytest` from the repository root, exit status
0:**

    at commit 3      324 passed, 2 deselected      (40.19s)

**Unchanged from the base, as expected: neither this task nor a stopped
audit adds a test.**

**`A15`, MEASURED on commits 1–3. Commit 4 is post-report evidence.**

    commit 1   8f3852d1   spec: audit what the literature establishes for reflection positivity
               trailer hits 0      not amended
    commit 2   bc625b11   review: pre-execution review for the literature coverage audit
               trailer hits 0      not amended
    commit 3   8625c899   derivation: the reflection-positivity literature audit stops on the
                          network precondition
               trailer hits 0      not amended

**MEASURED over the whole range: a scan for `Co-Authored-By`,
`claude.ai/code`, `Generated with`, `Claude-Session` and `noreply@anthropic`
returns ZERO.**

**Rule 20 binds this task and was NOT exercised.** **No force-push, no
branch deletion, no history rewrite of any kind.**

**Commits, MEASURED:**

    commit 1   8f3852d16c85f36c82bc2f11a957f7301b9f5265   specs/2026-08-16T0206Z_d1-literature-coverage-audit.md
    commit 2   bc625b1101b7b9b1c0b59e7d7202f4ec3ac830d8   reviews/chatgpt/2026-08-16T0206Z_d1-literature-coverage-audit.md
    commit 3   8625c8991d407254f4e74bae71d5a485ee8fa29e   derivations/P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md

**Commit 4's message, INTENDED:**

    report: no scholarly host is reachable and the coverage audit cannot be conducted

## 12. `§9` — Rule 16 assessment

**Rule 16 is operative. All four junctions are addressed. Each is addressed
in the form the precondition failure leaves available, and where a junction
turns on material this task did not gather, that is said rather than
papered over.**

### 12.1 First junction — what `COVERED` would mean, and what it would not

**`COVERED` means the fetched theorem, or the explicitly composable fetched
theorem set, has had EVERY common axis and EVERY theorem-specific
hypothesis explicitly mapped to the candidate action. It means the
literature result is applicable under that mapping.**

**It does not mean the programme independently reproved the theorem.**

**And the accurate limitation is narrower than "not a proof".** If the
hypotheses are fully mapped, the published theorem applies as mathematics.
**What would be missing is a repository-level applicability derivation and
its provenance, not a further physics proof** — which is exactly what `§5`'s
*replaced by theorem-applicability documentation* accounts for.

**This junction is stated in the conditional throughout, and deliberately.**
**MEASURED: this task recorded zero `COVERED` verdicts, and zero verdicts of
any kind.** Stating the junction indicatively would imply an applicability
determination that was never made.

### 12.2 Second junction — coverage is not evidence about physics

**A candidate with more literature behind it is not more likely to be the
right microscopic theory. It is a candidate other people happened to
study.**

**`§9` requires this said where a reader meets the four verdicts.** **There
are no verdicts, so there is no such place**, and the statement is made here
and only here. **A future executor who does produce four verdicts must place
it beside them**, in the artifact, and not rely on this report having said
it once.

**This is the junction most exposed by the stop**, and it is worth naming
why: an audit that runs partially and reports coverage for the candidates it
could reach would create exactly the false signal this junction guards
against. **Reporting nothing is the only outcome that cannot be misread as
weak evidence for a candidate.**

### 12.3 Third junction — the audit is bounded by what was fetched

**MEASURED: works fetched, ZERO. Statements remaining `RECALLED`, ZERO —
because none was recorded.**

**A `NO COVERAGE FOUND` verdict would mean nothing fetched applies, not that
nothing exists.** **Here the bound is total**: nothing was fetched, so
nothing at all is established about what the literature contains, in either
direction.

**In particular this report establishes NOTHING about whether the relevant
theorems exist.** They may all exist and be directly applicable; they may
not. **This task cannot distinguish those, and a reader must not take the
absence of coverage here as evidence of absence anywhere.**

### 12.4 Fourth junction — `L3` is a gap, and it is still open

**`L3` names no work.** The source task recorded `AUTHOR/WORK NOT RECALLED`,
and expressly declined to count it as a claim on the ground that *a standard
construction exists* is the absence of one.

**This audit did NOT fill that gap. It left it open, exactly as it found
it.**

**And the unfilled gap must not be read as an absence of coverage.** The two
are different: an absence of coverage would be a finding about the
literature, reached by looking; **an unfilled gap is a finding about this
container, reached by being unable to look.** `L3` was not investigated,
disconfirmed, or narrowed. **It is unchanged.**

**Restated as a caution to the next task:** the staggered row rests on
nothing, it rested on nothing before `D-1`, and it rests on nothing after.
**`D-1` changed the status of no row.**

## 13. Stops and clarifications

**ONE STOP occurred, and the specification designates it a successful
outcome.**

    SPECIFICATION_DEFECT                          0 stops, 1 finding
    ENVIRONMENT                                   1 stop,  0 further findings
    OBSERVATION_METHOD_ERROR                      0 stops, 1 finding
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   0 stops, 2 findings

### 13.1 `ENVIRONMENT` — the stop, and the primary category

**The `§1` global precondition failed: no scholarly or bibliographic host is
reachable from this container by any fetch path.** `§11` categorises a `§1`
precondition failure as `ENVIRONMENT`, and states the task is complete when
it is reported. **Reported at `§1` above, with every host and every error.**

**This is a policy denial at the organisation's egress gateway, not a defect
in the repository, not a defect in the specification, and not a mistake in
how it was measured** — the control hosts in `§1.3` establish the last of
those.

**Rule 13 carries two diagnostic orders, a known open item.** **Neither was
exercised**, and I am not naming one as having applied: **the failure is a
network policy denial and no diagnostic order was needed to identify it.**
**Nothing was installed.** Python 3.11.15 and pytest 9.1.1, as present.

### 13.2 `SPECIFICATION_DEFECT` — one finding, not a stop

**`A3` and `§5`/`A7` pull against each other on the precondition-failure
path, as set out at `§5` above.** `A3` says `A7` is not attempted; `§5`
defines a verdict `NOT DETERMINABLE` whose stated meaning is *the
precondition failed*, and which therefore exists for no other case.

**`§10` says that where an instruction is inconsistent with another
instruction I must stop and report and not decide which prevails.** **The
task had already stopped** — at the precondition, one criterion earlier —
**so this is reported into that stop rather than raising a second one.**

**What I did: I followed `A3` and recorded no verdicts, and I am saying so
explicitly rather than presenting the omission as though `§5` had no view.**
**The Reviewer should rule on whether a precondition-failed run ought to
record four `NOT DETERMINABLE` verdicts.** **Nothing in this task's output
would change if the ruling goes the other way except the addition of four
cells**, since `§5` assigns `NOT DETERMINABLE` no burden conclusion at all.

**This is adjacent to `G-08`** — an artifact asserting something false about
its own bytes — **but is not the same shape.** Nothing here is false; two
true instructions do not compose. `G-08` is about self-description;
**this is about two normative paths that meet only in a case neither
expected to be the live one.**

### 13.3 `OBSERVATION_METHOD_ERROR` — one finding, mine, caught within the task

**My first precondition probe tested four hosts with one client and would
have supported the same conclusion.** **It was not sufficient**, and the
reason is `G-11`-adjacent: a uniform negative from one client on four hosts
is equally consistent with a broken client, a broken proxy, and a policy
denial, **and those have different consequences for the programme.** A
broken container is worth retrying; a policy denial is not, and is a finding.

**Corrected within the task by three additions**: a second, independent
fetch client; a widened host list including preprint mirrors and
bibliographic APIs; **and a non-scholarly control**, `example.com`, which is
the measurement that actually separates the hypotheses.

**Recorded because the strength of this report's conclusion rests on the
control, and a reader should be able to see that the control was added
deliberately rather than assume the first probe was adequate.**

### 13.4 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — first finding

**A search path returned scholarly result metadata while every fetch path
was blocked**, `§1.5`. **Whether that constitutes "reaching a scholarly
source" under `§1` is a question this task cannot settle from the
specification's text.**

**I judged it does not**, for the reasons at `§1.5`, and **used nothing from
it.** **The outcome is invariant under the other reading**, because `§3`'s
fetch requirement fails for every work either way. **Reported, NOT
registered** — `§6` forbids adding a register entry.

### 13.5 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — second finding

**The pre-execution review is digest-bound to the correct specification
bytes and mis-describes that specification's acceptance criteria**, `§3`.
It enumerates `A1`–`A11` where the bound bytes carry `A1`–`A15` plus
`A13-final`, and its `A10` and `A11` descriptions correspond to no criterion
in the bound file.

**`A2` requires the digest field to be present and to match. Both hold.**
**No criterion in this specification checks a review's description of the
criteria against the criteria**, and I did not treat this as a stop, because
`A2`'s test is the one the specification states and the verdict is `APPROVE
FOR EXECUTION`.

**This is the complement of `G-05`.** `G-05` records that nothing compares a
review's cited digest against the committed specification. **Here the digest
comparison was performed and passed** — `A2` now requires it — **and the
failure moved to the review's prose**, which no check reaches. **Closing one
gap revealed the next one along.**

**Reported, NOT registered.** The governance register is frozen at eleven
entries and `§6` forbids adding to it.

### 13.6 `REPOSITORY_DEFECT` — nothing to report

**No defect in the repository was found by this task.** Every path at the
evidence base is blob-identical at the head; the gate invariants hold; the
pins recompute; the checker passes nine of nine at both prospectivity
readings; the validators are unchanged at 324 passed, 2 deselected.

### 13.7 What I would have specified differently

**`§1` asks for the hosts attempted and the errors. It does not ask for a
control.** I added one, and it is the single measurement that makes the
report's conclusion load-bearing rather than merely uniform. **I would have
had `§1` require a reachable-host control explicitly**, so that a future
executor reporting a total failure is obliged to show that the failure is
selective.

**And `§1` speaks of "fetching" without defining it against a search path
that returns metadata without bytes.** That definition did not matter until
a container existed with one and not the other. **I would have had `§1` say
that a source is REACHED when its bytes are retrieved**, which would have
made `§13.4` a determinate answer instead of a carried ambiguity.

**Nothing in the specification was unsatisfiable.** The precondition test
was performable, and its failure is an outcome the specification explicitly
provides for.

## 14. Did the audit make me want to design a proof route or select a candidate?

**Asked by `§11`, and the honest answer is that the pull was weaker here
than in any preceding task in this line, for a reason worth recording.**

**A stopped task offers very little to be tempted by.** The preceding tasks
put working objects in front of me — a staggered Dirac matrix, a plaquette
identity, a determinant that wanted a transfer matrix one function away.
**This task put a wall in front of me. There is nothing to build on the far
side of a blocked host.**

**Where the pull did appear, it was of a different shape, and it appeared
twice.**

**First, and it is the one I would flag: the pull to substitute what I know
for what I could not fetch.** I could name several of the works `B0`
gestured at, and I could state, from recollection, roughly what some of them
assume. **That is precisely the failure `D-1` exists to correct**, and it is
seductive exactly because the recollection is not obviously wrong — it is
plausible, specific, and would have produced a report that reads as
substantially more useful than this one. **A plausible recalled hypothesis
list is worse than no list**, because a later task cannot tell it from a
fetched one. **I recorded nothing recalled, and the coverage artifact
records nothing recalled.**

**Second, the pull to let the search probe count.** It returned real titles
and real URLs. **Treating them as `NOT FETCHED` records under `§3` would
have been defensible-sounding and would have let `A8` report a non-zero
count** — a partial audit built on non-fetched content, which `§1` forbids in
those words.

**Neither pull touched a proof route.** I did not consider how a missing
reflection-positivity proof would be constructed for any candidate, and this
task's stop is at a point where doing so would require the very literature
it could not reach.

**I confirm: I selected, eliminated, ranked and preferred no candidate;
designed no proof route and stated nothing about what a proof would look
like; did not re-derive or revise `B0`'s construction estimate; added no
register entry; modified no existing file; wrote no next specification; did
not touch `main` and performed no merge.**

## 15. Evidence layering

**Committed in this report, MEASURED at commit 3:** `A1`, `A2`, `A3`, `A9`,
`A11`, `A12`, `A14`, `A15` for commits 1–3; `A13`'s four invocations with
both configs and the `RUN 2` output verbatim; `A10`'s scope base-to-commit-3
at 3 additions and 0 modifications; commits 1–3 SHAs and their stored
messages.

**Committed in this report, INTENDED:** commit 4's message; `A10`'s final
base-to-commit-4 scope of 4 additions and 0 modifications.

**NOT ATTEMPTED, per `A3`:** `A4`, `A5`, `A6`, `A7`, `A8`.

**Post-report evidence, returned to the Reviewer and NOT written back:**
`A10`'s final scope measured base-to-commit-4; `A13-final`, being `RUN 2`
re-run at commit 4; `A14` at commit 4; `A15` for commit 4; the exact push
command; the branch tip read back from the remote; confirmation that
`refs/heads/main` is unchanged at `bfef924c…`.

**Nothing in this report claims to measure commit 4.**
