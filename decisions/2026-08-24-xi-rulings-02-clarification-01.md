# PI clarification — `P2-XI-RULINGS-02`, Ruling 2 scope

**Function:** a PI decision record, in the two parts `decisions/README.md`
requires.

    Decision key     2026-08-24-xi-rulings-02-clarification-01
    Decision owner   PI (Zeta Hoi-Ho Cheng)
    Issued           2026-08-23, in session
    Recorded by      Executor, under
                     `specs/2026-08-24T0000Z_xi-clar-01-landing_v2.md`
    Effect           fixes the representation on which the Q-M3 dependence
                     check is performed, and directs the registration of a
                     named open item
    Scope            the scope of the Q-M3 dependence check authorized by
                     `P2-XI-RULINGS-02`, Ruling 2

---

## PART 1 — THE DECISION

### 1. This document is a CLARIFICATION, not an independent ruling

**Stated explicitly, because the filing location is shared with rulings.**
This record files a **clarification of `P2-XI-RULINGS-02` Ruling 2's scope**.
It is **not** an independent PI ruling, and nothing in this record makes it
one. The issued text says so in its own words, at its third `CLARIFICATION`
block:

```text
CLARIFICATION   This document clarifies scope only. It changes no
                ruling of P2-XI-RULINGS-02, issues no membership
                ruling, and authorizes no task beyond those
                P2-XI-RULINGS-02 already authorizes.
```

**The clarification is `decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md`.**
That file holds the issued bytes and nothing else. **This file is the
decision-register record for it**, and it is not the clarification.

    Issued document   decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md
    SHA-256           0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22
    git blob id       1786124bbe3bfa02809d83c2890d0800e0d3edd8
    Bytes             3427

**The SHA-256 above is the identity the clarification's document review bound
itself to**, and the landed file was verified against it before it was written
(`M1`, `C1`). The blob id is the repository-native fingerprint of the same
bytes; it is a different hash function and is a secondary check.

**The canonical decision key `2026-08-24-xi-rulings-02-clarification-01` is
assigned here as filing metadata**, under the issued document's own
`IDENTIFIER` clause, which provides that such assignment "does not modify this
ISSUED TEXT". **No byte of the issued text was altered to accommodate it.**

### 2. What was clarified, by section name

**This section does not paraphrase.** Where it refers to content it does so by
section name and by quotation from the issued file.

    CLARIFICATION — Q-M3 check scope    three CLARIFICATION blocks and one
                                        RATIONALE block
    ROUTING                             the review jurisdiction, as established
                                        by P2-XI-RULINGS-01

**The issued text layers itself**, and the layering governs how every line may
be cited:

    LAYERING    Lines marked CLARIFICATION are the issued content.
                Lines marked RATIONALE are rendering, recorded for
                context, and are not to be cited as the clarification.

**The first `CLARIFICATION` block, quoted byte-identical from the issued file,
lines 24–30:**

```text
CLARIFICATION   The Q-M3 check authorized by P2-XI-RULINGS-02, Ruling 2
                is scoped to the landed decoupling — the
                Hubbard–Stratonovich transformation of the assembled
                chain. The verdict it returns is conditional on that
                representation, and this conditionality is to be
                recorded in the artifact's conditions alongside its
                other stated conditions.
```

**The second `CLARIFICATION` block, quoted byte-identical from the issued file,
lines 32–40:**

```text
CLARIFICATION   A family-wide representation-stability inquiry is NOT
                part of this task. It is to be registered as a named
                open item, linked to the representation-stability
                disclosure of P2-FIERZSUM-01 §8, with the following
                escalation condition: if the check returns DEPENDENT
                and the term is subsequently found to grow with L, the
                representation-stability inquiry escalates to required
                status; otherwise it remains registered at ordinary
                priority.
```

**The third `CLARIFICATION` block is quoted at §1 above**, lines 42–45.

### 3. What this landing did, and what it did not

**It transported.** Two things were landed and nothing was adjudicated:

1. the issued clarification, byte-exact;
2. the document-review artifact bound to those bytes, reproduced in PART 2
   below and landed as a standalone original at
   `reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02-clarification-01.md`.

**No gate moves. No claim status changes. Nothing is computed.** **The two OPEN
ledger rows of `P2-XI-LEDGER-01` remain OPEN**, and this record adds no
disposition to either.

**No task was begun, scheduled, constrained, or prioritised** — not the Q-M3
check, not the Q-M2 scope assessment, and not the representation-stability
inquiry the clarification names.

### 4. THE OPEN ITEM THE CLARIFICATION DIRECTS IS NOT YET REGISTERED

**The clarification's second `CLARIFICATION` block, quoted at §2, directs that a
family-wide representation-stability inquiry "is to be registered as a named
open item".** The landing task's `M4` was to perform that registration.

**`M4` did not execute. It stopped, and the reason is a governance conflict
returned to the PI rather than resolved by the executor.** No register at this
task's Base has a stated scope that admits the item:

    derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md   scoped to items arising
        from the C-check line; this item arises from a PI clarification on the
        XI line — DOES NOT ADMIT
    docs/GOVERNANCE-DEBT.md   the governance-side register, by its own text;
        this item is a scientific question — DOES NOT ADMIT
    derivations/P2-DEFERRED-ITEMS.md   admits the KIND — considered and
        consciously postponed work carrying the PI's position, entries added by
        PI decision — but its title and every one of its four entries scope it
        to `P2-PHASE-01`, and no line of its text extends it to another line

**The measurement and its reasoning are in the task's execution report.** The
item is therefore **directed and not yet registered**, and this record says so
rather than implying otherwise. **Nothing was placed in a convenient but
inapplicable register.**

### 5. When this clarification took effect

**On issuance**, per `decisions/README.md`'s adopted rule that PI decisions take
effect when issued and their reviews are mandatory but non-gating. The document
review reproduced in PART 2 returned `FIT FOR RECORDING` and is recorded under
that rule.

### 6. The scope relation with the landed criterion, recorded and not reconciled

**Both texts stand as written, and neither is reworded.**

The landed membership criterion the Q-M3 check feeds,
`derivations/P2-FIERZSUM-01.md:451-452`, is written:

```text
- **HS-normalization / Jacobian curvature test.** For every admissible
  decoupling `α`, verify not only recovery of the frozen quartic
```

The clarification scopes the authorized task to the landed decoupling, leaving
the family-wide residue to the open item it directs.

**This is a recorded scope relation, not a conflict and not a reconciliation.**
The landed criterion is not narrowed by the clarification; what the
clarification fixes is the representation on which the authorized task
evaluates it, and the family-wide residue is preserved as an open item rather
than discharged.

---

## PART 2 — THE REVIEW

    Function: Reviewer
    Kind      DOCUMENT REVIEW of the issued clarification.
              NOT a specification review, and NOT a review of Part 1 of
              this file.
    Author    the Reviewer function, ChatGPT
    Date      2026-08-23
    Verdict   FIT FOR RECORDING
    Original  reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02-clarification-01.md
              sha256 c586f0a4c0ec5023705dcac88f4db4b88ff911b99fa3324b3973031b5cad3018
    Bound to  0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22
              — the issued document's SHA-256, extracted from inside the
              review artifact and matching `M1`'s measurement exactly.

**The review's own statement of its jurisdiction bounds what the verdict
means:**

> This review does **not** approve or reject the PI's substantive scientific
> choice of representation, ordering, or programme strategy.

**Reproduced verbatim below, inside a fenced block**, which preserves the
artifact's bytes exactly; a blockquote or re-indentation would alter them.

```markdown
# Document Review — P2-XI-RULINGS-02-CLARIFICATION-01

**Reviewed clarification document:** `P2-XI-RULINGS-02-CLARIFICATION-01.md`  
**Reviewed document SHA-256:** `0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22`  
**Review date:** 2026-08-23  
**Reviewer:** ChatGPT  
**Document-review verdict:** `FIT FOR RECORDING`

## 1. Review jurisdiction

This review does **not** approve or reject the PI's substantive scientific choice of representation, ordering, or programme strategy.

Those choices lie within PI authority.

This review is limited to document craft and governance fitness:

- internal consistency;
- category correctness;
- separation of clarification from rationale;
- compatibility with the previously issued P2-XI-RULINGS-02;
- clarity of scope;
- well-formed escalation and return paths;
- correct distinction between registering an open item and authorizing a task;
- preservation of the issued text as a stable governance record.

## 2. Clarification category — PASS

The document correctly identifies itself as a scope clarification.

It changes no ruling of P2-XI-RULINGS-02, issues no membership ruling, and authorizes no new scientific task beyond those already authorized by the parent ruling.

The operative effect is to fix the representation on which the Q-M3 dependence test is to be performed.

## 3. Q-M3 representation scope — PASS

The clarification fixes the Q-M3 dependence measurement to the landed Hubbard-Stratonovich decoupling of the assembled chain.

The resulting dependence finding is therefore conditional on that landed representation.

The document does not promote that conditional result into a family-wide representation-independent theorem.

## 4. Parent-ruling compatibility — PASS

The clarification preserves the parent ruling's dependence-to-membership mapping.

It does not alter the substantive Q-M3 criterion; it only removes ambiguity about the representation on which the criterion is evaluated.

No conflict with the operative content of P2-XI-RULINGS-02 was found.

## 5. Representation-stability separation — PASS

A family-wide representation-stability inquiry is explicitly excluded from the Q-M3 task.

The clarification therefore avoids expanding a bounded dependence test into an unbounded scan over alternative Fierz or Hubbard-Stratonovich representations.

## 6. Open-item registration — PASS

The unresolved representation-stability question is required to be registered as a named open item.

Registration does not itself authorize execution of that inquiry.

This preserves the distinction:

`open question recorded`

from

`scientific task commissioned`.

## 7. Escalation condition — PASS

The clarification provides a well-formed escalation rule.

The representation-stability inquiry becomes required only if:

1. the Q-M3 term is found curvature-dependent under the landed representation; and
2. growth with L is subsequently established.

The Q-M3 dependence task itself is not thereby authorized to measure L-growth.

## 8. Implementation boundary — PASS

A future Q-M3 specification must implement only the dependence test authorized by the parent ruling and scoped by this clarification.

It must not silently add:

- a representation-family scan;
- an L-growth measurement;
- magnitude estimation;
- or any other stronger deliverable.

Any such work requires separate reviewed authority.

## 9. Clarification / rationale layering — PASS

The document clearly separates operative `CLARIFICATION` text from `RATIONALE`.

Rationale may explain the PI's scope choice but is not itself to be cited as the clarification.

This protects the operative authority from later disagreement over explanatory wording.

## 10. Routing — PASS

The document correctly preserves the distinction between:

- mandatory document-quality review, which is non-gating as to PI substantive authority; and
- later pre-execution review of the Q-M3 implementation specification, which remains gating.

The clarification is therefore recordable without itself serving as an execution specification.

## 11. Internal consistency — PASS

No internal contradiction was found among:

- the landed-representation scope;
- the parent Q-M3 dependence criterion;
- the exclusion of family-wide representation stability from the immediate task;
- the named-open-item requirement;
- the conditional escalation rule;
- and the statement that no additional task is presently authorized.

## 12. Recording fitness

Within the Reviewer's jurisdiction, the clarification is fit to be recorded as an issued PI governance clarification.

This verdict concerns the quality, categorization, and governance fitness of the record only.

It does not express substantive approval or rejection of the PI's scientific choice.

## Final verdict

**`DOCUMENT REVIEW: FIT FOR RECORDING`**

`P2-XI-RULINGS-02-CLARIFICATION-01.md` is fit to be recorded.

**Reviewed document SHA-256:** `0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22`

This review is bound exclusively to those exact bytes.
```

**End of the reproduced review artifact.**

---

# ADDENDUM — 2026-08-24: §4's statement has been overtaken, and by what

**Appended under `specs/2026-08-24T0900Z_xi-clar-01-landing_v3.md`. The §4
statement above is NOT edited.** It is left exactly as written, and this note
records what has changed since.

## The temporal scope of §4's statement

§4 is headed **"THE OPEN ITEM THE CLARIFICATION DIRECTS IS NOT YET
REGISTERED"** and records that the landing's `M4` stopped because no register's
stated scope had been shown to admit the item.

**That was true when it was written, and its reasoning stands unchanged.** The
register survey it reports was not wrong and has not been withdrawn: at that
Base, `derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md` was scoped to the C-check
line, `docs/GOVERNANCE-DEBT.md` was the governance-side register, and
`derivations/P2-DEFERRED-ITEMS.md` admitted the kind but was scoped by its title
and all four of its entries to `P2-PHASE-01`.

**It is false as a statement about the present.** The item is now registered.

## What registered it

**A PI ruling supplied the mechanism the survey had not found.** It routes this
one item to `DECISION_LOG.md`'s `UNESTABLISHED` entry mechanism — the route
`derivations/P2-DEFERRED-ITEMS.md`'s own text names for open questions — and is
recorded canonically at:

    decisions/2026-08-24-xi-open-item-register-routing.md
    decision key   2026-08-24-xi-open-item-register-routing

**The ruling is for this item only.** It extends or modifies no register's
scope, creates no register, and makes no general determination about where
future XI-line open items are registered. **In particular
`derivations/P2-DEFERRED-ITEMS.md` is not extended to the XI line**, and §4's
finding about its scope stands as measured.

## The entry that now carries the item

    DECISION_LOG.md, entry dated 2026-08-24
    "Open item: family-wide representation stability of the ξ ledger is
     UNESTABLISHED"
    Status: UNESTABLISHED. REGISTERED, NOT AUTHORIZED.

**Registration is not authorization.** Nothing in that entry, in the ruling, or
in this note begins, schedules, constrains or prioritises the
representation-stability inquiry, the `Q-M3` check, or the `Q-M2` scope
assessment. **The escalation condition is recorded, not triggered.**

## What this note does not change

**No measurement, no verdict, no membership status.** The two OPEN ledger rows
remain `OPEN(Q-M2)` and `OPEN(Q-M3)`, valueless. The clarification's own bytes
are untouched, and no sentence of PART 1 above is edited.
