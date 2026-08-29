# PI decision — register routing for the `P2-XI-RULINGS-02-CLARIFICATION-01` open item

**Function:** a PI decision, in the two parts `decisions/README.md` requires.

    Decision key     2026-08-24-xi-open-item-register-routing
    Decision owner   PI (Zeta Hoi-Ho Cheng)
    Issued           2026-08-24, in session
    Recorded by      Executor, under
                     `specs/2026-08-24T0900Z_xi-clar-01-landing_v3.md`
    Effect           determines the applicable register for the one open item
                     `P2-XI-RULINGS-02-CLARIFICATION-01` directs be registered,
                     unblocking the `M4` stop of that clarification's landing
    Scope            THIS ITEM ONLY. See §3.

---

## PART 1 — THE DECISION

### 1. What was returned, and why a ruling was needed

The landing of `P2-XI-RULINGS-02-CLARIFICATION-01` stopped at its `M4` under
`A3`. The clarification directs that a family-wide representation-stability
inquiry "is to be registered as a named open item"; the executor measured every
register at that Base and found none whose stated scope admitted it, and
returned the question rather than placing the item in the nearest register. That
measurement is at `reports/2026-08-24T0043Z_xi-clar-01-landing.md` §5, and the
landed register record `decisions/2026-08-24-xi-rulings-02-clarification-01.md`
§4 records on its face that the item was not yet registered.

**The PI has ruled the applicable mechanism.**

### 2. The ruling, as issued

**Landed byte-identical, in the language it was issued in. This is the
ruling.** It is reproduced inside a fenced block with its `> ` markers intact,
so the landed bytes are the bytes of §0c of
`specs/2026-08-24T0900Z_xi-clar-01-landing_v3.md`, lines 92–99, and not a
re-rendering of them.

```text
> 就 P2-XI-RULINGS-02-CLARIFICATION-01 指令註冊嘅
> representation-stability inquiry:適用登記處為 DECISION_LOG.md 嘅
> UNESTABLISHED 條目機制,即 derivations/P2-DEFERRED-ITEMS.md 自身文本為
> open questions 指名嘅路由。呢項裁決只就本 item 而言,唔擴大或修改任何
> register 嘅 scope,唔建立新 register,亦唔就日後 XI-line open items 嘅
> 登記處作一般性決定 — 後者留待需要時另裁。條目按 clarification 原文登記,
> 狀態 REGISTERED, NOT AUTHORIZED,escalation condition 逐字引錄。
> — Zeta, PI, 2026-08-24
```

    Extracted bytes   590
    sha256            85c0827436f42a8bdcaa020229de120e745ed82ce1e5f5b783ea989135716198
    Extraction        git cat-file blob <spec-blob>:specs/2026-08-24T0900Z_xi-clar-01-landing_v3.md
                      | sed -n '92,99p'

**The ruling text was extracted from the committed specification blob, not
retyped.** Nothing in it was reflowed, re-encoded, or re-punctuated.

**A working translation, identified as such:**

> Concerning the representation-stability inquiry whose registration
> `P2-XI-RULINGS-02-CLARIFICATION-01` directs: the applicable register is
> `DECISION_LOG.md`'s `UNESTABLISHED` entry mechanism — that is, the route
> `derivations/P2-DEFERRED-ITEMS.md`'s own text names for open questions. This
> ruling is in respect of this item only; it does not extend or modify any
> register's scope, does not create a new register, and does not make a general
> determination about where future XI-line open items are registered — that is
> left to be ruled separately if and when needed. The item is registered
> according to the clarification's own text, with status
> `REGISTERED, NOT AUTHORIZED`, and the escalation condition quoted verbatim.
> — Zeta, PI, 2026-08-24

**THE ISSUED TEXT GOVERNS.** The translation is recorded because this
repository's records are otherwise in English. **It is not the ruling and is
not to be cited as it.**

### 3. The scope limits the ruling itself states

**Reproduced as a list because each is operative, and none is an addition by
this record — every one is in the issued text above.**

    THIS ITEM ONLY        the ruling is "只就本 item 而言"
    NO SCOPE EXTENDED     it does not extend or modify any register's scope
    NO REGISTER CREATED   it does not create a new register
    NO GENERAL RULE       it makes no general determination about where future
                          XI-line open items are registered; that is left to a
                          separate ruling if and when needed

**In particular, `derivations/P2-DEFERRED-ITEMS.md` is not extended to the XI
line by this ruling**, and the finding that its stated scope is bound to
`P2-PHASE-01` stands as the executor measured it. **What the ruling identifies
is a different mechanism**: the route that register's own text names for open
questions.

### 4. The route the ruling names, and where it is landed

The ruling routes the item to the mechanism `derivations/P2-DEFERRED-ITEMS.md`
itself names for open questions. That register states, at `:19-26`, quoted
byte-exact over the whole line range:

```text
**How to tell the two apart in this repository.** Open questions live in
the `OPEN-AC-*` and `OPEN-PD-*` items of the admissibility-contract and
parameter-domain drafts, and in `DECISION_LOG.md` entries that open an
item as `UNESTABLISHED`. Those record that something has not been
settled. **An entry here records that something was looked at, was
understood well enough to be set aside deliberately, and was set aside
anyway** — with the reason, the evidence, and the PI's position at the
time.
```

**The mechanism has a landed precedent**, and `M4` follows its format:
`DECISION_LOG.md:2147-2215`, the 2026-08-19 `POLE-B0` construction item, whose
own `Reason` states at `:2199-2200`:

```text
That distinction determines which register admits it, and this log is the
register whose stated scope covers an item opened as `UNESTABLISHED`.
```

**That precedent's `Reason` also surveys the other registers and reaches the
same finding the executor's `M4` measurement reached** — that
`P2-DEFERRED-ITEMS` scopes itself to considered-and-postponed work,
`P2-PHASE-01_C-CHECK_OPEN-ITEMS` to the C-check line, and `GOVERNANCE-DEBT` to
rule gaps rather than scientific questions. **The stop and this ruling are
consistent, not in tension.**

### 5. What this ruling does not do

**It authorizes no scientific work.** The item is registered
`REGISTERED, NOT AUTHORIZED`; nothing in the ruling or in this record begins,
schedules, constrains, or prioritises the representation-stability inquiry, the
`Q-M3` dependence check, or the `Q-M2` scope assessment.

**It changes no ruling of `P2-XI-RULINGS-02` and no word of the
clarification.** It settles where the directed item is filed, and nothing else.

### 6. When this decision took effect

**On issuance**, per `decisions/README.md`'s adopted rule that PI decisions take
effect when issued and their reviews are mandatory but non-gating.

---

## PART 2 — THE REVIEW

**`REVIEW PENDING`.**

No review of Part 1 of this file has been supplied. Under `decisions/README.md`
a decision whose Part 2 is not yet written is recorded with Part 2 marked
pending, **and the decision is in effect meanwhile.**

**The pre-execution review of the resumption specification is not this review.**
That artifact (`reviews/chatgpt/2026-08-24T0900Z_xi-clar-01-landing_v3.md`)
reviews the specification that carries this ruling and directs this record's
creation; it does not review the record.
