# PI decision — executor identity for `P2-XI-RULINGS-LANDING-01`

**Function:** a PI decision, in the two parts `decisions/README.md` requires.

    Decision key     2026-08-23-xi-landing-executor-identity
    Decision owner   PI
    Issued           2026-08-23, in session
    Recorded by      Executor, under
                     `specs/2026-08-23T0000Z_xi-rulings-landing-integ_v4.md`
    Task affected    `P2-XI-RULINGS-LANDING-01`
    Effect           settles executor identity for that one execution;
                     changes nothing else
    Scope            executor identity only

---

## PART 1 — THE DECISION

### 1. The ruling, as issued

**Landed byte-identical to the blockquote at §0a of
`specs/2026-08-23T0000Z_xi-rulings-landing-integ_v4.md`, lines 89–93.**

**It is reproduced inside a fenced block, with §0a's `> ` markers intact**, so
that the landed bytes are the specification's bytes and not a re-rendering of
them. A blockquote here would have re-prefixed lines that already carry the
marker; this repository has had checks defeated three times by exactly that
class of alteration. **The reproduction is verifiable by a byte comparison
against lines 89–93 of the specification blob**, and against the extraction
digest recorded below.

```text
> I confirm. Claude Code was the designated executor for
> P2-XI-RULINGS-LANDING-01 under AGENTS.md:86. The specification's
> "Codex only" label is superseded for executor identity only by that
> runtime PI designation. No scientific, measurement, scope, or
> acceptance criterion is changed, and no re-execution is required.
```

    Extraction        git cat-file blob <spec-blob>:specs/2026-08-23T0000Z_xi-rulings-landing-integ_v4.md
                      | sed -n '89,93p'
    Extracted bytes   326
    sha256 of those bytes
                      ca6dbb3c30c37c99074594d4dcfb23692b230f146b800999d7287f36e84ff95f

**The ruling text was extracted from the committed specification blob, not
retyped.** Nothing in it was reflowed, re-encoded, or re-punctuated.

### 2. What the ruling settles, and what it does not

    SETTLES      that Claude Code was the designated executor for
                 `P2-XI-RULINGS-LANDING-01`, under `AGENTS.md:86`
                 ("The PI announces which executor is in use")

    SETTLES      that the reviewed specification's label is superseded
                 **for executor identity only**, and **for that execution
                 only**, by the runtime PI designation

    DOES NOT     change any scientific content, any measurement, any scope,
                 or any acceptance criterion — the ruling says so in its own
                 words

    DOES NOT     require re-execution — the ruling says so in its own words

### 3. The historical fact the ruling supersedes

**Recorded because a reader must be able to see what the record said before
the ruling, and what the ruling changed.**

The reviewed specification `specs/2026-08-22T2001Z_xi-rulings-landing_v2.md`
carries, in its `§0` header block, the field

    Execution      Executor (Codex) only. The Researcher holds no write
                   access and this specification grants none.

**That text is not rewritten and is not withdrawn.** It stands in the landed
specification as the reviewed bytes it always was. What the ruling above does
is supersede it **for executor identity only, for the execution of
`P2-XI-RULINGS-LANDING-01` only.**

The executing task did not assume this. It recorded the divergence at §6a of
`reports/2026-08-22T2021Z_xi-rulings-landing.md` and returned it for the PI to
confirm or correct. **The ruling above is that confirmation.**

### 4. What is NOT landed here

**The forward executor-field convention is not landed by this decision.** The
phrasing "the executor designated by the PI at execution time", as a
programme-wide specification-authoring rule, is a Researcher authoring
practice. It is not a PI ruling, and an integration task does not land one. **If
the PI issues it, it lands as its own limb through the normal path**, distinct
from the retrospective ruling above.

### 5. When this decision took effect

**On issuance**, per `decisions/README.md`'s adopted rule that PI decisions
take effect when issued and their reviews are mandatory but non-gating.

---

## PART 2 — THE REVIEW

**`REVIEW PENDING`.**

No review of Part 1 of this file has been supplied. Under `decisions/README.md`
a decision whose Part 2 is not yet written is recorded with Part 2 marked
`REVIEW PENDING`, **and the decision is in effect meanwhile.**

**The pre-execution review of the integration specification is not this
review.** That artifact
(`reviews/chatgpt/2026-08-23T0000Z_xi-rulings-landing-integ_v4.md`) reviews the
specification that directed this record to be created; it does not review the
record.
