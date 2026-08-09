# Report — cross-reference SI-1's gate entry to `DEFERRED-02`

Specification: `specs/2026-08-09T2153Z_si1-deferred-02-crossref.md`
Specification sha256:
`b1e53a14404b0b739c69d2c25a76a16fd05640820e3a94763bc4b1c974943172`
Pre-execution review: `reviews/chatgpt/2026-08-09T2153Z_si1-deferred-02-crossref.md`
Evidence base: `898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7`
Branch: `fix/si1-deferred-02-crossref`
Classification: MATERIAL. Branch only; no merge, no PR.

---

## 0. Summary

One reference was added to `GATES.md`, at the end of `P2-PHASE-01`'s
`### Scope`. Nothing else in the repository changed. `GATES.md` contained
zero occurrences of `P2-DEFERRED-ITEMS` at the evidence base; it now
contains one.

Three findings are reported as first-class results rather than
housekeeping:

- **The pre-execution review was supplied with no delimiter lines.** A2's
  location procedure had nothing to locate. The boundary rule actually
  applied is stated in §5, and the stripped prefix is characterised
  exactly.
- **A8's premise is wrong for one of its two named validators.**
  `tests/test_gate_anchors.py` does not read `GATES.md` and does not
  contain the string `GATES`. Deleting `P2-PHASE-01`'s entire 103-line
  entry leaves both named validators fully green (§12).
- **`### Quantifier note` was seriously considered and rejected**, and
  the reference wording names the quantifier's home statement to avoid
  colliding with existing gate text (§6, §7).

No STOP condition fired.

---

## 1. A9 — repository refs and branch

    origin/main             898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7
    remote refs/heads/main  898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7
    local main              0f7961747abe2a18b436c0b1e5b928f425ea4d9a

`refs/remotes/origin/main` and the remote `refs/heads/main` both resolve
to the evidence base, as required. Local `main` is stale by design and
was not touched, repaired, or consulted.

    $ git rev-parse --abbrev-ref HEAD
    fix/si1-deferred-02-crossref
    $ git merge-base HEAD 898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7
    898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7

The branch was created from the evidence base; the merge-base equals the
base exactly, so no other commit intervenes. No `main` ref moved. No
branch was deleted.

---

## 2. A1 — pinned inputs

Method: `git cat-file blob 898aecd1:<path> | sha256sum`. All three match
the specification; no mismatch, so no STOP.

    GATES.md
      expected  dbe797ab53c3748baaf44f59442971e5e48b2c2719542b88e0c2f956fe14fd5f
      observed  dbe797ab53c3748baaf44f59442971e5e48b2c2719542b88e0c2f956fe14fd5f  MATCH

    derivations/P2-DEFERRED-ITEMS.md
      expected  47b22bbb2c59a4d4ee44c4ff98726a1fa65d963a4c6a979763b6903c1c0658cd
      observed  47b22bbb2c59a4d4ee44c4ff98726a1fa65d963a4c6a979763b6903c1c0658cd  MATCH

    derivations/P2-PHASE-01_scalar_stationary_exploratory.md
      expected  80586e33ef07e307729af4597f72b48f6ecee74fc6a0f396b593f735ef322599
      observed  80586e33ef07e307729af4597f72b48f6ecee74fc6a0f396b593f735ef322599  MATCH

---

## 3. §7 — the author's pre-issue literal verification, reproduced

Reproduced independently against the pinned blobs, same check type as
declared: exact literal substring, no normalisation.

    target      derivations/P2-DEFERRED-ITEMS.md @ 898aecd1
    digest      47b22bbb…0658cd (verified, §2)

    PASS  "the quantifier range of the SI-1 kill criterion"      1 occurrence

    target      GATES.md @ 898aecd1
    digest      dbe797ab…14fd5f (verified, §2)

    PASS  "## P2-PHASE-01 — Admissible stable condensed phase (the Ice)"
                                                                1 occurrence
    PASS  "### Scope"                                           14 occurrences
    CONFIRMED  occurrences of "P2-DEFERRED-ITEMS" in GATES.md:    0

`### Scope` occurring 14 times — once per gate — is worth stating
explicitly, because it means "the `### Scope` section" is not by itself a
unique anchor in this file. The edit was anchored on the four-line
`P2-PHASE-01` Scope paragraph verbatim, asserted unique before
substitution:

    anchor occurrences: 1

After the edit, `P2-DEFERRED-ITEMS` occurs once. That count going 0 → 1
is the finding the task exists to change.

---

## 4. A3 — `DEFERRED-02`'s `Blocks:` line, quoted from the pinned register

Quoted from `derivations/P2-DEFERRED-ITEMS.md` at the pinned digest
`47b22bbb…0658cd`, verbatim:

> **Blocks:** the quantifier range of the SI-1 kill criterion. That
> criterion asks whether any admissible phase exists in the frozen space;
> with this branch neither admitted nor excluded, the SI-1 specification
> must state whether the branch falls inside the range. **This register
> does not answer that and does not amend the SI-1 gate text.**

The register says what §0 of the specification quotes it as saying, so
the task's premise holds and no STOP fired.

**Correspondence to the added reference**, clause by clause:

    register clause                          reference clause
    ---------------------------------------  --------------------------------
    "with this branch neither admitted nor    "a stationary branch that is
     excluded"                                 neither admitted nor excluded"
    "the quantifier range of the SI-1 kill    "whether it falls within the
     criterion, … must state whether the       existential quantifier of this
     branch falls inside the range"            gate's scientific question is
                                               therefore undetermined"
    "This register … does not amend the       the reference is one-directional;
     SI-1 gate text"                           the register is not edited, and
                                               no gate text other than the
                                               added paragraph changes

The register places the obligation on "the SI-1 specification". The
reference is what makes that obligation reachable from the gate entry
that an SI-1 specification would be written from.

---

## 5. A2 — the pre-execution review, and a finding about how it was supplied

Committed at `reviews/chatgpt/2026-08-09T2153Z_si1-deferred-02-crossref.md`
in commit 2, before the work commit, per Rule 15.

    extracted text   4823 bytes, 4819 characters, 46 lines
    committed blob   sha256 5767fa80f0539aa5da312f98d03a47b350ccf6faef975c9309e12727a5ebd403
    byte-identical to the extracted text:  True

(The 4-byte/4-character gap is two em-dashes and two other non-ASCII
characters, three UTF-8 bytes each; it is not a normalisation.)

**Finding — the review was supplied with no delimiters.** A2 says:

> Locate the delimiters as WHOLE LINES, not as first occurrences of the
> delimiter string — an instruction naming a delimiter contains it.

There were none to locate. Checked programmatically against the supplied
message before extraction:

    "=== REVIEW ARTIFACT" in message   ->  False

A2's two STOP conditions are "the supplied text is missing" and "does not
correspond to this specification". Neither is met: the text is present,
and it corresponds unambiguously — it names `DEFERRED-02`, `GATES.md`,
the `### Scope` placement rule, the `## P2-` section comparison, and Rule
16, all of which are this specification's contents and no other's. So
this is a reportable deviation, not a stop.

**The boundary rule actually applied**, stated so it can be checked
rather than trusted: the review begins at its own title line
`Pre-execution review — SI-1 DEFERRED-02 cross-reference` and runs to the
end of the message. The only text preceding the title was asserted to
match the regular expression `@"[^"]+"\s` exactly and in full — the
attachment marker for the specification file plus one whitespace
character. That is harness syntax, not review content, and nothing else
was stripped. Nothing was added, reflowed, or reformatted; no placeholder
appears in the review's text, so none was resolved.

**Why this is worth reporting rather than absorbing.** A2's location
procedure exists because the first-occurrence search failed twice in
earlier tasks — an instruction naming a delimiter contains it. Here the
procedure was inapplicable for the opposite reason, and I substituted a
boundary rule of my own. That rule is defensible and is stated above in
full, but it is mine, and the specification did not authorise it. The
guarantee A2 wants — that the committed review is exactly what the
Reviewer wrote, decidable without executor judgement — held only because
the review's own title line happened to be an unambiguous start marker.

---

## 6. §1 — placement, and why `### Scope`

§1 names `### Scope` as the natural home and permits another section "if
the entry's structure makes another section clearly better". I used
`### Scope`, after considering two alternatives seriously enough that the
reasons belong in the record.

**`### Quantifier note` (GATES.md line 1038 at base), rejected.** This
section exists and its entire content is about the quantifier:

> ### Quantifier note
> The kill criterion cannot be evaluated until the MICROSCOPIC PARAMETER
> DOMAIN prerequisite creates the frozen space over which its universal
> quantifier runs.

On its face this is the better home — it is the section about the
quantifier, and it already records one unresolved input. Two things
decided against it.

First, it sits *after* `### Kill criterion` in the entry. §1's stated
purpose is to place the reference "where a reader designing the gate will
meet it before writing criteria". `### Scope` precedes the criteria by
some fifty lines; the Quantifier note does not.

Second and more substantively, the Quantifier note is a *blocking*
notice: it says the criterion cannot be evaluated **yet**, and gives a
prerequisite that will eventually be satisfied. Appending `DEFERRED-02`
there would subordinate it to that timeline and invite the reading "one
more thing that clears when the parameter domain lands". It does not
clear then. The branch's status is independent of whether the frozen
space exists; once the space exists, the question of whether this branch
lies in it is still open and still requires a PI decision.

**`### Integrated exploratory evidence`, rejected.** This section points
at the scalar stationary study that the negative-mass branch comes from —
`derivations/P2-PHASE-01_scalar_stationary_exploratory.md`, the third
pinned input. It is where the branch's provenance lives. But it is a
record of what was done, not an input to the gate's design; a reader
writing an execution specification reads it for context, not for
constraints. Placing the constraint there files it as history.

**`### Scope` is where the constraint actually bites.** The section reads:

> Stationary solutions `δΓ/δΦ_i = 0` of the full effective action, with
> all condensates drawn from the frozen channels, at finite density /
> `μ`, within the pre-registered microscopic parameter domain (policy §2,
> §4).

The negative-mass branch is a stationary solution of exactly this kind.
The open question — is it in the set the gate quantifies over? — is
literally a question about this paragraph's extension. So the reference
is not merely near the right place; it attaches to the sentence whose
meaning is in dispute.

This is §1's default, so no deviation is claimed on placement. The
alternatives are recorded because the specification asked for a reason if
another section were chosen, and a reader is better served by knowing
which were weighed than by silence.

---

## 7. A5 — the reference, quoted in full

Added as a new paragraph at the end of `P2-PHASE-01`'s `### Scope`:

> `derivations/P2-DEFERRED-ITEMS.md` records, as `DEFERRED-02`, a
> stationary branch that is neither admitted nor excluded; whether it
> falls within the existential quantifier of this gate's scientific
> question is therefore undetermined.

**Three things and no more**, mapped to §1's list:

    1  "records, as DEFERRED-02, a stationary branch that is neither
        admitted nor excluded"
    2  "whether it falls within the existential quantifier of this gate's
        scientific question is therefore undetermined"
    3  "derivations/P2-DEFERRED-ITEMS.md"

There is no fourth clause. The sentence contains no verb of judgement, no
recommendation, no schedule, and no statement about what anyone should do.

**The three prohibitions, one by one:**

*It does not assert or deny that the branch is admissible.* The only
predicate applied to the branch is "neither admitted nor excluded", which
reports the register's recorded status and is a statement about the
record, not about the physics. The word "admissible" does not appear.

*It does not qualify the gate's status, question or criteria.* `Status:
PROPOSED` is unmodified and unmentioned (verified in §8). The scientific
question is referred to but not restated, altered or conditioned — the
phrase "this gate's scientific question" is a pointer to the existing
`### Scientific question` section, whose text is byte-identical to base.
The kill criterion is not mentioned at all; no qualifier, hedge or
annotation was attached to it.

*It does not suggest the gate cannot proceed.* The sentence says a
question is undetermined; it says nothing about what follows from that.
Specifically, it does not say the gate is blocked, does not say the
criterion cannot be evaluated, and does not defer anything. The word
"undetermined" attaches to the quantifier-membership question, not to
SI-1's tractability.

**One wording precision, declared.** §1 item 2 asks the reference to state
"that whether it falls within this gate's existential quantifier is
therefore undetermined". I wrote "the existential quantifier of this
gate's **scientific question**". The added words are a disambiguation, not
a change of content, and they were added for a specific reason: the entry
already contains the phrase "its **universal** quantifier", in the
`### Quantifier note`. Both are correct — the scientific question is
existential (`≥1 physically admissible stable condensed phase`) and the
kill criterion is its universal negation (`No admissible phase
anywhere`), the two being duals — but a document that says "existential
quantifier" in one section and "universal quantifier" in another, with no
indication that they are about different statements, reads as a
contradiction. Naming the home statement removes that without touching
either sentence. Recorded here because §1's list is the controlling
specification of the reference's content and I did not follow its wording
letter-for-letter.

---

## 8. A4 — section-by-section comparison

Each `## P2-` section was extracted from base and head — heading line to
the line before the next `## P2-` heading — and compared body to body.
Digests are sha256 of the whole section text, truncated to 8 hex
characters for the table.

    ^## P2- count   base: 14   head: 14
    headings identical (all 14, in order): True

    SECTION HEADING                                                BASE     HEAD
    ## P2-HK-01 — Heat-kernel species coefficients                 6be205b8 6be205b8  identical
    ## P2-GAP-01 — Gap-equation criticality (continuum + lattice)  d3d35fe2 d3d35fe2  identical
    ## P2-BETA-01 — Lattice mass-scan extraction of `β_B`          9655d3b7 9655d3b7  identical
    ## P2-BETAV-01 — Lattice `β_V/β_B` (Proca / Stueckelberg)      5c2b98b8 5c2b98b8  identical
    ## P2-NORM-01 — Locate the `β`/`G` normalization factor 2      afaed93c afaed93c  identical
    ## P2-BETAV-CIRC-01 — Does the lattice `β_V` test discriminate f9c7fbb0 f9c7fbb0  identical
    ## P2-BETAV-NUMREPRO-01 — Numerical reproduction of `β_V/β_B`  d44e7373 d44e7373  identical
    ## P2-BETAV-RECON-01 — Clean-room curved-background Proca reco f520f45f f520f45f  identical
    ## P2-BETAV-ASSEMBLY-01 — Determinant-bookkeeping regression ( 6656473b 6656473b  identical
    ## P2-CHANNEL-FREEZE-01 — Freeze the HS/Fierz channel basis +  81a57766 81a57766  identical
    ## P2-PHASE-01 — Admissible stable condensed phase (the Ice)   c1fb257d dc86eff9  *** DIFFERS ***
    ## P2-MULTIPHASE-GRAV-01 — Programme-death: does any phase giv 18c94ae3 18c94ae3  identical
    ## P2-GRAV-ENGINE-RECOVERED-01 — Recovered historical gravity  7d92c83a 7d92c83a  identical
    ## P2-LATTICE-ONTOLOGY-01 — Physical H(4) lattice substrate sp e08a5419 e08a5419  identical

    sections differing: 1

This is a **body** comparison, not a heading comparison: thirteen section
bodies hash identically. §A4 warns that heading equality is a proxy; the
table above reports the proxy (headings identical, first line) and the
substantive check (body digests) separately, and the substantive check is
the one relied on.

The one differing body, in full:

    ---- body diff for: ## P2-PHASE-01 — Admissible stable condensed phase (the Ice)
    --- base
    +++ head
    @@ -15,2 +15,7 @@
     the pre-registered microscopic parameter domain (policy §2, §4).
    +
    +`derivations/P2-DEFERRED-ITEMS.md` records, as `DEFERRED-02`, a stationary
    +branch that is neither admitted nor excluded; whether it falls within the
    +existential quantifier of this gate's scientific question is therefore
    +undetermined.

The difference is the added reference and nothing else — five added
lines, zero deleted, zero modified.

Statuses, read by the same method the repository's own validator uses
(first `Status:` line after the `## <gate-id> ` heading):

    P2-PHASE-01  base: 'PROPOSED'
                 head: 'PROPOSED'                                    unchanged
    P2-GAP-01    base: 'PASS (continuum exact; lattice `I_0` agrees with paper at matched mass)'
                 head: 'PASS (continuum exact; lattice `I_0` agrees with paper at matched mass)'
                                                                     unchanged

Text outside the `## P2-` sections was compared as well, since the
section extraction would not otherwise cover it:

    text before the first ## P2- heading, identical:  True

`P2-DEFERRED-ITEMS` occurrences in `GATES.md`: base 0, head 1.

    GATES.md base sha256  dbe797ab53c3748baaf44f59442971e5e48b2c2719542b88e0c2f956fe14fd5f
    GATES.md head sha256  8ce38b8a5f95bda421007245d4d21bdd3e32f35e83629ed76f848ddca072e526

---

## 9. A6 — nothing else touched, compared path by path

Compared as individual blob object IDs from `git ls-tree -r`, not as tree
objects, so a `reviews/` addition cannot mask a `reviews/` modification.

    protected paths present at base:   192
    protected paths differing at head:   0

The four named files, explicitly:

    CONVENTIONS.md      base 0db56c39d44e   head 0db56c39d44e   identical
    AGENTS.md           base 5e60b5fcd6e9   head 5e60b5fcd6e9   identical
    DECISION_LOG.md     base 04539f26a6bc   head 04539f26a6bc   identical
    pyproject.toml      base 9fc6fdd196dd   head 9fc6fdd196dd   identical

The register, which A6 singles out:

    derivations/P2-DEFERRED-ITEMS.md
                        base 33b3a664e057   head 33b3a664e057   identical

The reference is one-directional. `DEFERRED-02` was read and quoted; it
was not edited, annotated, or back-referenced.

Per-prefix counts of base-present paths, all blob-identical:

    scripts/        56
    results/        66
    tests/          16
    derivations/    30
    docs/            7
    reviews/        13

Base-absent paths present at head:

    reviews/chatgpt/2026-08-09T2153Z_si1-deferred-02-crossref.md
    specs/2026-08-09T2153Z_si1-deferred-02-crossref.md

Both are authorised A7 paths. The `reviews/` addition is the one A6
anticipates. Paths present at base and absent at head: none.

---

## 10. A7 — scope, at the pre-report head

Manifest as run (`mode: exact`; `head` is required by the tool and was
supplied — see §17):

    {
      "mode": "exact",
      "base": "898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7",
      "head": "HEAD",
      "required": [
        {"operation": "add",    "path": "specs/2026-08-09T2153Z_si1-deferred-02-crossref.md"},
        {"operation": "add",    "path": "reviews/chatgpt/2026-08-09T2153Z_si1-deferred-02-crossref.md"},
        {"operation": "modify", "path": "GATES.md"}
      ],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

Verbatim tool output, including `observed_operations`:

    $ python -m scripts.governance_tools.scope_checker --repo . --manifest ../si1_manifest_pre.json
    {
      "base": "898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7",
      "failures": [],
      "head": "143c8f399f575a2eaa2bdf16f5f6ccf06ef97f9d",
      "mode": "exact",
      "observed_operations": [
        {
          "operation": "modify",
          "path": "GATES.md"
        },
        {
          "operation": "add",
          "path": "reviews/chatgpt/2026-08-09T2153Z_si1-deferred-02-crossref.md"
        },
        {
          "operation": "add",
          "path": "specs/2026-08-09T2153Z_si1-deferred-02-crossref.md"
        }
      ],
      "overall": "PASS",
      "tool": "scope_checker"
    }
    EXIT=0

Two additions and one modification at the pre-report head; this report is
the third addition. The intended final manifest is in §16 and the final
scope check is post-report evidence per §4 of the specification.

---

## 11. A8-pre — validators at the pre-report head

Run individually with `python -m pytest <path>`, exit status recorded:

    $ python -m pytest tests/test_repository_structure.py -q
    4 passed in 0.03s                                            EXIT=0

    $ python -m pytest tests/test_si1_governance.py -q
    14 passed in 0.07s                                           EXIT=0

    $ python -m pytest tests/test_gate_anchors.py -q
    18 passed, 2 deselected in 8.71s                             EXIT=0

    $ python -m pytest tests/test_governance_tools.py -q
    8 passed in 1.43s                                            EXIT=0

All four exit 0. Nothing failed, so the A8 clause "if either fails, do not
adjust the reference to satisfy it without saying so" was never engaged —
the reference text was not altered at any point to make a test pass.

---

## 12. What `test_gate_anchors.py` and `test_si1_governance.py` assert about `GATES.md`

A8 states that both "constrain this file". That is true of one of them.

**`tests/test_gate_anchors.py` — asserts nothing about `GATES.md`.**

    occurrences of the string "GATES" in the file:  0
    file reads (read_text / open( / Path( / ROOT):  none

It is a numerical regression suite: 20 tests over heat-kernel
coefficients, gap-equation criticality, the lattice `β_B` mass scan, the
`β_V` ratio and the assembly bookkeeping, several of them mutation tests
on the physics. Despite the name, it constrains derivation code and
results, not the gate ledger.

**`tests/test_si1_governance.py` — does read `GATES.md`, in seven of its
fourteen tests.** What it asserts, in full:

    helper _gate_status(gate_id)
      first "Status:" line after the "## <gate_id> " heading; raises if absent.
      Called for: P2-BETAV-CIRC-01, P2-BETAV-RECON-01, P2-BETAV-NUMREPRO-01,
                  P2-BETAV-ASSEMBLY-01.   Not called for P2-PHASE-01.

    test_circ01_run_verdict_recorded_separately
      "recovered" present; "DECOMP-UNAVAILABLE-AS-RECOVERED" present;
      "Previous additive k-scan design: WITHDRAWN" present; plus checks inside
      the P2-BETAV-CIRC-01 block.
    test_recon01_remains_proposed        "PROPOSED" in P2-BETAV-RECON-01's status
    test_numrepro01_run_verdict_recorded_separately
                                          checks inside the P2-BETAV-NUMREPRO-01 block
    test_audit_pass_alone_does_not_promote_c9
      "alone does not verify or promote" present;
      "does not by itself promote `P2-C9`" present
    test_dual_gate_promotion_rule_present
      "P2-BETAV-CIRC-01 = PASS" and "P2-BETAV-NUMREPRO-01 = PASS" present;
      "requires" and "P2-C9" present
    test_circ_pass_alone_does_not_promote  "A PASS does **not** verify or promote" present
    test_assembly01_remains_pass           "PASS" in P2-BETAV-ASSEMBLY-01's status
    test_paper3_analytic_input_is_pinned   commit 8c363ef0… present in GATES.md
    test_channel_freeze_no_longer_requires_circ_pass
      "no longer requires" and "P2-BETAV-CIRC-01" both present anywhere in the file

Every one of these is a substring-presence check, and every gate ID named
belongs to the `P2-BETAV-*` family or `P2-CHANNEL-FREEZE-01`. **No
assertion in either file mentions `P2-PHASE-01`, and none mentions
`DEFERRED`** (`grep -rn 'DEFERRED' tests/` returns nothing).

**Mutation check, because presence-of-passing-tests is not evidence of
coverage.** I deleted `P2-PHASE-01`'s entire entry from `GATES.md` — all
103 lines, heading through the line before `## P2-MULTIPHASE-GRAV-01` —
and re-ran both:

    --- MUTATION: entire P2-PHASE-01 entry deleted (103 lines) ---
    $ python -m pytest tests/test_si1_governance.py -q
    14 passed in 0.03s                                           EXIT=0
    $ python -m pytest tests/test_gate_anchors.py -q
    18 passed, 2 deselected in 5.03s                             EXIT=0

Both stay green. The working tree was then restored and verified against
the committed object:

    $ git checkout -- GATES.md
    identical to HEAD:GATES.md  True
    sha256 8ce38b8a5f95bda421007245d4d21bdd3e32f35e83629ed76f848ddca072e526
    $ git status --short
    (clean)

**Conclusion.** The gate section this task edits has no validator
coverage whatsoever. The four green suites in §11 are evidence that I
broke nothing the tests watch; they are not evidence that the edit is
correct, and they would not have caught its deletion. The only
mechanically checkable protection this change had is A4's
section-by-section comparison in §8, which I ran myself — it is not in
`tests/`, so it will not run again. That is a repository gap, reported in
§18.

---

## 13. §3 — Rule 16 assessment

Rule 16 is operative. The reading now available from the assembled set —
`GATES.md` with the reference, `derivations/P2-DEFERRED-ITEMS.md` with
`DEFERRED-02`, and the exploratory scalar study the branch comes from —
that the set does not establish:

**The candidate offered in §3 is confirmed, and I would sharpen it.**

`GATES.md` now points at `DEFERRED-02`, and `DEFERRED-02` names SI-1's
quantifier range. A reader who follows the pointer sees a register entry,
written in the vocabulary of an open-items tracker, referenced from a
governance ledger. Both genres normally imply ownership. **A reader could
conclude the quantifier question is resolved, or is being tracked toward
resolution. It is neither.** Nobody is assigned; answering it requires a
PI decision on whether the negative-mass branch is an admissible phase,
and no such decision exists.

The sharpening: **this task makes the inference more available than it
was before, not less.** Before it, the register was unreachable from the
gate entry and no reader would have formed any belief about ownership.
After it, the pointer exists and reads like a live tracking link. The
task's purpose — discoverability — and the false inference it enables are
produced by the same edit. That is not an argument against the edit; it
is the junction Rule 16 asks to be named, and the register's own sentence
"**This register does not answer that and does not amend the SI-1 gate
text**" is the only thing in the assembled set that pushes back on it.

**A second junction, which §3 does not name.** The set now co-locates:
the exploratory scalar study (a stationary branch found at `M̂ ≈ −7.59`,
`mu = 0` slice, no admissibility verdict), `DEFERRED-01`'s recorded PI
position that the V/A representation "may contain physically relevant
information" with "**no evidence indicates it is unphysical**", and a
`GATES.md` `### Scope` paragraph that now carries a deferral notice.
Reading these together, the available inference is that **the gate's
scope has been narrowed to what has been examined, with the remainder
parked**. It has not. `### Scope` still says "all condensates drawn from
the frozen channels"; the added paragraph does not subtract from that set
and was written specifically not to. What is parked is one branch's
*classification*, not any part of the gate's *range*. Whether the added
paragraph is read as a deferral of scope or as a flag on an unresolved
membership question depends on the reader, and nothing in the assembled
set forces the correct reading.

**Search.** I checked whether anything mechanical resists either
inference: no test mentions `DEFERRED` (§12), no test mentions
`P2-PHASE-01` in `test_si1_governance.py` or `test_gate_anchors.py`, and
`GATES.md` carries no status or ownership field on the added reference —
by design, since §1 forbids adding one. There is no artifact in the
repository that would register an objection if the quantifier question
stayed open indefinitely.

---

## 14. Would the added reference change how I would write an SI-1 execution specification?

The specification asks this directly and makes it dispositive: if the
answer is no, the pointer is in the wrong place and the task has failed.

**Yes, and at a specific point.** Writing an SI-1 execution specification
from this gate entry, the first thing to fix is the enumeration domain —
which stationary solutions of `δΓ/δΦ_i = 0` count as candidates. That is
what `### Scope` defines, and it is the paragraph immediately above the
added reference. I cannot write the enumeration clause without deciding
whether the `M̂ ≈ −7.59` branch is in the set being enumerated, because
the reference says in that same section that the answer is undetermined.
The decision cannot be made silently: the register's `Blocks:` line
requires the SI-1 specification to "state whether the branch falls inside
the range", and following the pointer produces that sentence.

**The counterfactual, which is the actual test.** At the evidence base,
`GATES.md` contained zero occurrences of `P2-DEFERRED-ITEMS`. A person
writing an SI-1 specification from the gate entry — the entry being where
anyone starts, and the entry being self-contained in appearance, with
scope, assumptions, inputs, dependency, two prerequisites, kill criterion
and quantifier note — would have read all of that, met no mention of the
register, and written an enumeration clause that silently either included
or excluded the branch. There was nothing in their path to stop them. The
constraint existed, was recorded, and was unreachable from the only
document they would have read.

**Where it would still fail.** The reference is discoverable to a reader
of `P2-PHASE-01`'s entry. It is not discoverable to someone who starts
from `results/`, from the exploratory study, or from `CLAIMS.md`, and no
validator enforces the pointer's continued existence (§12) — a later edit
could remove it and every suite would stay green. The pointer is in the
right place for the reader the specification names; it is one paragraph,
protected by nothing but this report.

---

## 15. A10 — commit-message hygiene

Every commit was inspected before writing (proposed message file) and
after (`git log -1 --format='%B'` read back from the object). The scan
pattern was `co-authored-by|claude|session|https?://|generated with|
anthropic`, case-insensitive, applied to both.

    commit 1  92ff2d941d6eb03ca6139c0a2dc0b3b193dc4bde
      spec: cross-reference SI-1's gate entry to DEFERRED-02
      proposed scan: no match     stored scan: no match
      trailers suppressed: yes — the default Co-Authored-By and session-URL
      trailers were prevented at authoring time; none appears in the object.

    commit 2  5a56486a5b5144201d230fe331bc6a2178a8020d
      review: commit the pre-execution review for the SI-1 DEFERRED-02 cross-reference
      proposed scan: no match     stored scan: no match
      trailers suppressed: yes — same two.

    commit 3  143c8f399f575a2eaa2bdf16f5f6ccf06ef97f9d
      gates: cross-reference SI-1's scope to the DEFERRED-02 register entry
      proposed scan: no match     stored scan: no match
      trailers suppressed: yes — same two.

No `Co-Authored-By` line, no session identifier or URL, and no tool
attribution appears in any stored message. The report commit's message is
in §16; its authoring-time suppression is reported post-report, per §4.

---

## 16. Intended final state

**Intended final manifest** (this report added to the A7 set):

    {
      "mode": "exact",
      "base": "898aecd1ebd5f5a35df0a73c2ce635670e6cd8d7",
      "head": "HEAD",
      "required": [
        {"operation": "add",    "path": "specs/2026-08-09T2153Z_si1-deferred-02-crossref.md"},
        {"operation": "add",    "path": "reviews/chatgpt/2026-08-09T2153Z_si1-deferred-02-crossref.md"},
        {"operation": "add",    "path": "reports/2026-08-09T2153Z_si1-deferred-02-crossref.md"},
        {"operation": "modify", "path": "GATES.md"}
      ],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

Expected final base-to-head scope: 3 additions and 1 modification.

**Intended report commit message:**

    docs: report the SI-1 DEFERRED-02 cross-reference

    Records A1-A7, A8-pre, A9 and A10 for the one reference added to
    P2-PHASE-01's ### Scope in GATES.md.

    Three findings beyond the acceptance criteria. The pre-execution
    review was supplied with no delimiter lines, so A2's whole-line
    location procedure had nothing to locate; the boundary rule actually
    applied is stated in full. tests/test_gate_anchors.py does not read
    GATES.md and contains no occurrence of the string GATES, so A8's
    premise holds for only one of its two named validators; deleting
    P2-PHASE-01's entire 103-line entry leaves both green. The reference
    names the quantifier's home statement -- the gate's scientific
    question -- because the entry already says "universal quantifier" of
    the kill criterion, and the two readings are duals.

    Placement is ### Scope, the specification's default, with
    ### Quantifier note and ### Integrated exploratory evidence weighed
    and the reasons recorded.

    P2-PHASE-01's entry has no validator coverage: deleting all 103 lines
    of it leaves both named suites green.

**Pre-report head:** `143c8f399f575a2eaa2bdf16f5f6ccf06ef97f9d`

**Blob digests at the pre-report head:**

    specs/2026-08-09T2153Z_si1-deferred-02-crossref.md
      b1e53a14404b0b739c69d2c25a76a16fd05640820e3a94763bc4b1c974943172
    reviews/chatgpt/2026-08-09T2153Z_si1-deferred-02-crossref.md
      5767fa80f0539aa5da312f98d03a47b350ccf6faef975c9309e12727a5ebd403
    GATES.md
      8ce38b8a5f95bda421007245d4d21bdd3e32f35e83629ed76f848ddca072e526

---

## 17. Environment

    Python              3.11.15
    python -m pytest    9.1.1      (the version the specifications mandate)
    pytest on PATH      9.0.2      (not used)
    ruff                0.15.8

Nothing was installed. All validators were run as `python -m pytest`.

`CONVENTIONS.md` Rule 13 carries two diagnostic orders, a known open item.
**No environment failure occurred, so neither order was exercised.** I am
not naming one as the order followed, because none was.

---

## 18. Stops and clarifications

No stop occurred. All findings below are secondary.

**`SPECIFICATION_DEFECT` — none reached the threshold of a stop.**

Two secondary findings in this category:

*A8's premise about `tests/test_gate_anchors.py` is incorrect.* A8 states
that it and `test_si1_governance.py` "both constrain this file". The
former reads no file at all and contains zero occurrences of `GATES`
(§12). The instruction was still executable — the criterion asks me to
report what they assert, and "nothing" is a reportable answer — so this
did not block execution and is not a stop. Recorded because A8's evident
purpose was to make me look at what protects `GATES.md`, and the honest
answer to that purpose is: for this section, nothing does.

*A2's location procedure was inapplicable as written.* No delimiters were
supplied (§5). A2 anticipates a delimiter appearing where it should not;
it does not anticipate none appearing. Neither of its STOP conditions was
met, so I applied a boundary rule of my own and stated it in full rather
than stopping. Recorded because the rule is mine and the specification did
not authorise it.

**`ENVIRONMENT` — none.** No environment failure occurred; neither of Rule
13's two diagnostic orders was exercised (§17).

**`OBSERVATION_METHOD_ERROR` — none reached the threshold of a stop.**

One secondary finding: `### Scope` occurs 14 times in `GATES.md`, once per
gate, so the section name alone is not a unique anchor. I anchored on the
four-line `P2-PHASE-01` Scope paragraph verbatim and asserted uniqueness
(count == 1) before substituting. Recorded because "insert into
`### Scope`" is exactly the kind of instruction a first-occurrence search
would satisfy wrongly, and the assertion is what makes the placement
checkable rather than trusted.

**`REPOSITORY_DEFECT` — none reached the threshold of a stop.**

One secondary finding, and it is the substantive one: **`P2-PHASE-01`'s
gate entry has no validator coverage.** Deleting all 103 lines of it
leaves `test_si1_governance.py` and `test_gate_anchors.py` green (§12).
`test_si1_governance.py` covers the `P2-BETAV-*` family and
`P2-CHANNEL-FREEZE-01` by substring presence; nothing covers the gate this
task edits, and nothing anywhere in `tests/` mentions `DEFERRED`. A
consequence specific to this task: the reference added here is protected
by no test, so a later edit could remove it and the full suite would still
pass. A8's section-by-section comparison exists only in this report.

A pre-existing item, unchanged by this task and repeated for continuity:
`CONVENTIONS.md` now carries 17 rules with no structural validator — no
test asserts rule count, numbering, or heading form.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — none reached the
threshold of a stop.**

One secondary finding: the entry now contains "existential quantifier" (in
`### Scope`) and "universal quantifier" (in `### Quantifier note`). These
are duals and both are correct about their own statements, but nothing in
the entry says so. I mitigated it by naming the home statement in the
added text (§7) rather than by editing the existing sentence, which §5
forbids. The residual ambiguity is real and is a PI matter: the entry
describes its quantifier two ways, and only one of them is now
cross-referenced.

**Things I would have specified differently.**

*A8 should not name a validator without stating what it is expected to
constrain.* Naming a file and asserting it "constrains this file" invited
me to find the constraint rather than to check whether one exists. I
checked, and there is none; a differently-disposed executor could have
reported the four green suites as coverage. The general form: an
acceptance criterion that names evidence should say what property the
evidence is supposed to establish, so that its absence is detectable.

*A2 should state the fallback when no delimiter is present*, rather than
leaving the executor to invent a boundary rule. The current text hardens
against one failure mode (a delimiter string appearing in prose) and is
silent about its complement.

*§1's item 2 fixes a word — "existential" — that collides with committed
gate text.* Had the specification's literal-verification record in §7
included a check for "quantifier" occurrences in the `P2-PHASE-01` entry,
the collision would have surfaced before issue rather than during
execution.

**What this task did not do**, stated because §5 lists these as
prohibitions and the record should show them discharged: the register was
not edited; no gate status, verdict, question, scope statement, locked
assumption or criterion was changed beyond the added paragraph; the
negative-mass branch was not stated or implied to be admissible or
inadmissible; SI-1 was not stated or implied to be unable to proceed; the
quantifier range was not resolved; no digest-pinned artifact was modified;
there was no merge, PR, force-push, or history rewrite; no branch was
deleted; and local `main` was left stale.
