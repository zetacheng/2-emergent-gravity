# Report — `P2-XI-CLAR-01-LANDING` v2: STOPPED AT `M4` under `A3`

    Specification   specs/2026-08-24T0000Z_xi-clar-01-landing_v2.md
    Review          reviews/chatgpt/2026-08-24T0000Z_xi-clar-01-landing_v2.md
    Branch          science/xi-clar-01-landing
    Base            main @ 9af94a4a11cd06e90ef2d24183565412b4043c6a
    Outcome         M1, M2, M2b and M3 COMPLETE. **M4 STOPPED.** M5, M6a, M6b
                    and M6c NOT REACHED.
    Merge           NONE. `main` did not move.
    Push scope      this task's branch only.

**This report records M1 through M3 and the M4 stop. It records nothing later,
because nothing later occurred.** It does not state its own commit SHA: it is
committed onto `8e4e2e659df4e383d2522dc9490abe826aa00f99` and **is itself the
next commit on it**.

---

## 0. The stop, stated first

**`M4` could not be executed as specified, and the reason is a governance
question that is not the executor's to resolve.**

The clarification directs that the family-wide representation-stability inquiry
"is to be registered as a named open item". `M4` requires that registration in
"the repository's open-item register", and requires the executor to "record the
register path used **and why it is the applicable register**".

**No register at this task's Base has a stated scope that admits this item.**
The measurement is at §5. Rather than place the item in a convenient but
inapplicable register, execution stopped and returns the question.

**`A3` is the abort that fits**: "any later step surfaces a conflict between the
issued clarification and landed text. STOP; report verbatim; do not reconcile."
The conflict is between what the issued clarification requires — a named open
item in a register — and what landed register scopes provide.

**What was completed stands and is sound.** The clarification and its document
review are landed byte-exact with their register record, on an unintegrated
branch. **Only the registration is outstanding.**

---

## 1. Execution location and worktree identity (Amendment D step 0)

    execution location      /home/user/2-emergent-gravity
    worktree toplevel       /home/user/2-emergent-gravity
    branch at start         science/integrate-xi-ledger-01 @ eeec8884
    observed origin/main    9af94a4a11cd06e90ef2d24183565412b4043c6a  = Base
    repository is shallow   false
    UTC at report           2026-08-24T0043Z

---

## 2. `M1` and `M2` — byte identity, before any write

    ARTIFACT                       SHA-256                                                            BYTES
    issued clarification           0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22    3427
    its document review            c586f0a4c0ec5023705dcac88f4db4b88ff911b99fa3324b3973031b5cad3018    5072
    landing specification          2a30601952c0cdf48d000f0a46f39241c0c6315e590c766c40b1c3d8be620ca6   13168
    its pre-execution review       f16bd61a59f74ea219666621e7ef4f8dd7e86acc471b7ddc2da7be9d1323ad3b    5639

**`M1` — the issued clarification.**

    measured sha256   0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22
    §0a expects       0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22
    measured blob id  1786124bbe3bfa02809d83c2890d0800e0d3edd8
    §0a expects       1786124bbe3bfa02809d83c2890d0800e0d3edd8
    MATCH on both. `A1` did not fire, and the branch was cut only afterwards.

**`M2` — the document-review artifact.** Its sha256
`c586f0a4c0ec5023705dcac88f4db4b88ff911b99fa3324b3973031b5cad3018` is its first
recorded hash; provenance transmitted by the PI in session. **The SHA-256 it
declares itself bound to, extracted verbatim from inside it:**

    0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22

That is the only 64-hex string in the artifact, at its lines 4 and 136, and it
equals `M1`'s measurement exactly. Verdict string, as matched text: line 7,
`**Document-review verdict:** ` + backtick + `FIT FOR RECORDING` + backtick.

**The landing specification's binding.** Its review carries
`Reviewed specification SHA-256` twice, declaring
`2a30601952c0cdf48d000f0a46f39241c0c6315e590c766c40b1c3d8be620ca6`, which equals
the specification's sha256 and the sha256 of the committed spec blob at
`8c351c1`. Verdict `APPROVE FOR EXECUTION`.

---

## 3. `M2b` — the mandatory pre-write correspondence scan

**Ran in full before the branch existed. All three items RESOLVE. No
substantive conflict at this step.**

### `M2b(1)` — `P2-XI-RULINGS-02`, Ruling 2: the parent whose scope is clarified

    located     decisions/P2-XI-RULINGS-02.issued.md, present at the Base
    sha256 at the Base   ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5
    blob id at the Base  72a6b24c9289efde8a096e4e591ff01728323473
    FINDING     RESOLVES

`decisions/P2-XI-RULINGS-02.issued.md:30-39`, quoted verbatim:

```text
RULING      Route (ii). A task is authorized to perform the undone
            check that landed text already names — whether the
            Hubbard–Stratonovich Jacobian/normalization term is
            curvature-dependent (P2-FIERZSUM-01.md:451-460). The landed
            criterion governs the outcome: if dependent, the row enters
            the ledger and its L-scaling is then to be determined; if
            independent, the row closes. This task adjudicates
            dependence only; it does not estimate magnitude beyond what
            the landed criterion requires. Normal specification and
            pre-execution review path.
```

**The clarification fixes the representation on which this authorized check is
performed. It does not alter the ruling.** Consistent, not conflicting.

### `M2b(2)` — `P2-FIERZSUM-01 §8`'s representation-stability disclosure

    located     derivations/P2-FIERZSUM-01.md — the disclosure is deliverable 8
                of §4 at :231-233, and §8's machine-checkable conditions at
                :424-464 carry its scan, ":464 - **Representation-stability scan**
                producing `Δ_Fierz^(F)` (§7B)."
    FINDING     RESOLVES

`derivations/P2-FIERZSUM-01.md:231-233`, quoted verbatim:

```text
8. **Representation-stability disclosure**: how far `ξ_ind` moves under
   change of decoupling within a preregistered family (§7, Route B) —
   reported as a number with its qualifications, never asserted zero.
```

**This is the disclosure the clarification links the open item to.** It exists
at the Base and is locatable.

### `M2b(3)` — `P2-FIERZSUM-01.md:451-460`, the membership criterion the Q-M3 check feeds

    located     derivations/P2-FIERZSUM-01.md:451-460 at the Base
    FINDING     RESOLVES

Quoted verbatim:

```text
- **HS-normalization / Jacobian curvature test.** For every admissible
  decoupling `α`, verify not only recovery of the frozen quartic
  interaction but the full identity
  `Z_HS^(α)[g] = N_α[g] · Z_fermionic[g]`, and determine whether
  `δ log N_α[g] / δR` vanishes. A field-independent normalization is
  harmless in flat-space scattering, but here the observable IS
  `−log Z[g]`: any metric-, regulator- or curvature-dependent
  normalization, contour phase, or Jacobian contributes to the
  cosmological and `R` terms and **must be included in `ξ_ind`, not
  discarded as an irrelevant constant**.
```

**THE SCOPE RELATION, RECORDED AS `M2b(3)` REQUIRES.**

**The landed criterion is written "For every admissible decoupling `α`"** — the
words are at `:451-452` and are reproduced above with nothing changed.

**The clarification scopes the authorized task to the landed decoupling**, the
Hubbard–Stratonovich transformation of the assembled chain, leaving the
family-wide residue to the registered open item. Its words are in the register
record at `decisions/2026-08-24-xi-rulings-02-clarification-01.md` §2, quoted
byte-identical from the issued file.

**Both texts are preserved verbatim. Neither is reworded.** This is a recorded
scope relation — **not a conflict, and not a reconciliation.** The landed
criterion is not narrowed; what the clarification fixes is the representation on
which the authorized task evaluates it, and the family-wide residue is preserved
as an open item rather than discharged. **The executor reconciled nothing and
was not asked to.**

### Scan summary

    item   subject                                            finding
    ---------------------------------------------------------------------
    (1)    P2-XI-RULINGS-02 Ruling 2                          RESOLVES
    (2)    P2-FIERZSUM-01 §8 representation-stability disclosure  RESOLVES
    (3)    P2-FIERZSUM-01:451-460 criterion + scope relation   RESOLVES

    unresolved items        0
    substantive conflicts   0

---

## 4. `M3` — landing, COMPLETE

**Commit sequence, nothing interleaved:**

    8c351c1  spec        the landing specification
    14da675  review      its bound pre-execution review
    8e4e2e6  decisions   the issued clarification, its document review, and the
                         register record
    (this)   report      this report

**The binding was verified before the spec commit**, not after.

**The landed files:**

    decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md
      sha256 0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22
      blob   1786124bbe3bfa02809d83c2890d0800e0d3edd8
      identical to the handed-over bytes: `cmp -s` reports identical

    reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02-clarification-01.md
      sha256 c586f0a4c0ec5023705dcac88f4db4b88ff911b99fa3324b3973031b5cad3018
      identical to the handed-over bytes: `cmp -s` reports identical

    decisions/2026-08-24-xi-rulings-02-clarification-01.md   the register record

**Neither transported file was retyped, reflowed, or re-encoded.**

**`C3`'s quotation check, measured by bytes:**

    CLARIFICATION 1   register-record block 444 B   issued lines 24-30 444 B   BYTE-IDENTICAL
    CLARIFICATION 2   register-record block 578 B   issued lines 32-40 578 B   BYTE-IDENTICAL
    CLARIFICATION 3   register-record block 243 B   issued lines 42-45 243 B   BYTE-IDENTICAL
    §6 criterion      register-record block 136 B   P2-FIERZSUM-01:451-452 136 B  BYTE-IDENTICAL
    PART 2 review     reproduction        5072 B   landed original    5072 B   BYTE-IDENTICAL

**The register record states explicitly, at its §1, that the document is a
CLARIFICATION and not an independent ruling**, as §1 of the specification
requires, and quotes the issued text's own third `CLARIFICATION` block as the
evidence for it.

**The register record's §4 records that the directed open item is NOT YET
REGISTERED**, so the landed record does not imply a registration that did not
happen.

---

## 5. `M4` — STOPPED. The register-selection measurement

**Three registers exist at the Base.** The sweep that establishes this covered
every Base file self-describing as a register and every file whose title line
contains "register":

    derivations/P2-DEFERRED-ITEMS.md              # Deferred-items register — `P2-PHASE-01`
    derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md # `P2-PHASE-01` C-check line — register of open items
    docs/GOVERNANCE-DEBT.md                       # Governance debt — an authoritative register

**Each was tested against its own stated scope.**

### (A) `derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md` — DOES NOT ADMIT

`:3-5`, verbatim:

```text
**This is a register of open items arising from the C-check line** — the
follow-up checks `C1`, `C2` and `C3` commissioned by
`derivations/P2-PHASE-01_microscopic_parameter_domain.md`.
```

The item arises from a PI clarification on the XI line, not from the C-check
line. **Its stated scope excludes it.**

### (B) `docs/GOVERNANCE-DEBT.md` — DOES NOT ADMIT

`:16-19`, verbatim:

```text
Two registers already existed at the evidence base and both are science-side:
`derivations/P2-DEFERRED-ITEMS.md`, whose own text says entries are added by PI
decision, and `derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md`, created by `C3`
for the C-check line. **There was no governance-side register.**
```

**By its own text this is the governance-side register**, and its six
dispositions — `REPAIRABLE`, `SPECIFIABLE`, `NOT REPAIRABLE HERE`, `RULED`,
`METHOD NOTE`, `OPEN` — are governance-defect dispositions. The item is a
scientific question about the representation stability of a physical quantity.
**Its stated scope excludes it.**

### (C) `derivations/P2-DEFERRED-ITEMS.md` — ADMITS THE KIND, WRONG LINE

**The landed admissibility test for this register**, quoted from
`DECISION_LOG.md:2723-2727`:

```text
        DOES NOT ADMIT any of the five. It holds work CONSIDERED and
        consciously POSTPONED, carrying the PI's position at deferral, and
        its entries are added by PI decision. Its own text routes open
        questions elsewhere, naming `DECISION_LOG.md` entries that open an
        item as UNESTABLISHED.
```

**Applied to this item, all three limbs are satisfied** — and this is the first
item in this line for which that is true:

    (1) considered and consciously postponed   SATISFIED. The clarification
        excludes the inquiry from the Q-M3 task by name and directs its
        registration; it was examined and set aside deliberately.
    (2) carries the PI's position at deferral  SATISFIED. The RATIONALE states
        it: the family-wide question is "real but distinct", concerns a family
        "whose membership is itself an unlanded model-level choice", and is
        "better served by a dedicated inquiry under its registered item".
    (3) entries are added by PI decision       SATISFIED. The clarification is
        an issued PI document directing the registration.

**But the register's stated scope is bound to a different line.** Its title is
`# Deferred-items register — `P2-PHASE-01``; its four entries are

    ## `DEFERRED-01` — V/A mean-field representation
    ## `DEFERRED-02` — Negative-mass stationary branch, `M̂ ≈ -7.59`
    ## `DEFERRED-03` — Possible relation between `DEFERRED-01` and `DEFERRED-02`
    ## `DEFERRED-04` — does `H(4)` dynamics remove or gap some microscopic species?

all `P2-PHASE-01` items, and **no line of its text extends it to another line.**
Its own "Scope of this register" section at `:184-193` states what it does not
do and how entries are added; it does not state that it takes items from lines
other than `P2-PHASE-01`.

### The determination

**No register's stated scope explicitly admits this item.** The one whose kind
matches is scoped to a different line; the two whose lines could be argued do
not admit the kind.

**`derivations/P2-DEFERRED-ITEMS.md` is exactly "the nearest one".** Placing the
item there would be the convenient-but-inapplicable placement the Reviewer's
§13 execution note forbids: *"If no existing register clearly admits the item,
that is a governance issue to return rather than a reason to place it in a
convenient but inapplicable register."*

**`M4` therefore stopped, and the question is returned to the PI.** The
executor does not create a register, does not extend one register's scope to
another line, and does not stretch a stated scope to fit.

**What the PI's ruling would need to settle**, stated as the question and not as
a recommendation:

    - whether `derivations/P2-DEFERRED-ITEMS.md`'s scope extends beyond
      `P2-PHASE-01`, or
    - whether another existing register's scope admits the item, or
    - whether a register for XI-line open items is to be created, and by what
      authority

**Nothing above proposes an answer**, and this task neither created nor amended
any register.

---

## 6. `M5`, `M6a`, `M6b`, `M6c` — NOT REACHED

**`M5` requires "the open item's identifier"**, which does not exist because
`M4` stopped. `DECISION_LOG.md` is therefore **unmodified by this task** —
verified: `git diff --name-status` against the Base lists no entry for it.

**`M6a` specifies the suite "at the base and at the post-M5 tree".** There is no
post-`M5` tree. **`M6a` did not execute**, and this report is not the `M6b`
report the specification describes.

**Recorded as environmental evidence and explicitly NOT `M6a`**, because a
reader should be able to see the branch is sound:

    BASE          tree 9353d6282cb9bee47a0b64f66eda524f1ef2265b
                  344 passed, 2 deselected in 47.62s
    BRANCH TIP    8e4e2e659df4e383d2522dc9490abe826aa00f99
                  tree 8438b55570c7b36cee6e4649e78eea6f0802a394
                  344 passed, 2 deselected in 42.66s

Both on a non-shallow tree. **This is not the `M6a` measurement and must not be
cited as one.**

---

## 7. Acceptance criteria

    C1  (M1)   PASS   sha256 0e549c7c…0d363f22 and blob id 1786124b…0e0d3edd8,
                      both equal to §0a. Re-measurement from the final tip is
                      part of C1; §8 records it.
    C2  (M2)   PASS   The review artifact declares 0e549c7c…0d363f22, an exact
                      string match to C1's digest, and lands byte-identical to
                      the handed-over bytes.
    C2b (M2b)  PASS   All three scan items carry a finding with quoted landed
                      text; item (3)'s scope relation is recorded verbatim with
                      both texts preserved; no item unresolved; no substantive
                      conflict at the scan.
    C3  (M3)   PASS   Commit order is spec, its review, then the landing
                      commits, nothing interleaved; every register-record
                      quotation is byte-identical to its source.
    C4  (M4)   NOT SATISFIED — NOT REACHED. The open item is not registered.
                      This is the stop, not a failure of the measurement: no
                      applicable register exists to register it in.
    C5  (M5)   NOT REACHED. DECISION_LOG.md is unmodified.
    C6  (M6a/b/c)  NOT REACHED.

---

## 8. Abort conditions

    A1  DID NOT FIRE   Both M1 digests and both review bindings agree with §0a,
                       measured before the branch existed.
    A2  DISCHARGED     The Reviewer concurs that a clarification may use the
                       decisions/ two-file layout with its clarification status
                       stated in PART 1. The regression limb did not fire: the
                       structure as executed is §1's, and the clarification
                       status is stated in PART 1 §1.
    A3  **FIRED, at M4.**  A conflict between the issued clarification and
                       landed text: the clarification requires the inquiry "to
                       be registered as a named open item", and no landed
                       register's stated scope admits it. **Reported verbatim at
                       §5; nothing was reconciled.**
    A4  DID NOT FIRE   No register-record or open-item passage states the
                       clarification more narrowly, more broadly, or more
                       specifically than the issued text. All three
                       CLARIFICATION blocks are byte-identical quotations, and
                       no open-item passage exists to test, because none was
                       written.
    A5  DID NOT FIRE   **No step began, scheduled, constrained, or prioritised**
                       the Q-M3 check, the Q-M2 scope assessment, or the
                       representation-stability inquiry. The inquiry is not even
                       registered, and §5 records the question without proposing
                       an answer. **Registration is not authorization — and here
                       not even registration occurred.**

---

## 9. Environment

    python 3.11.15, numpy 2.4.6, sympy 1.14.0, pytest 9.1.1, ruff 0.16.3
    scipy ABSENT — as on every preceding task in this session
    repository non-shallow at both suite runs

---

## 10. Stops and clarifications (Amendment B)

**Primary category: `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`.**

### 10a. The `M4` stop, returned for a PI ruling

**Stated at §0 and measured at §5.** The clarification directs a registration;
no landed register's stated scope admits the item; the executor did not choose
a register by proximity.

**The whole of the rest of the task is complete and sound.** The clarification
is landed byte-exact with its document review and register record. **When the
register question is settled, `M4`, `M5` and `M6` resume on this branch.**

### 10b. What the stop does not mean

**It is not a finding against the clarification**, whose text is landed intact
and whose direction is clear. **It is not a finding against any register** —
each register's scope is doing exactly what it was written to do. **It is a gap
between them**, and gaps of that kind are the PI's to close.

**Nothing was left implicit to make the branch look complete:** the register
record's §4 says on its face that the directed item is not yet registered.

### 10c. Rule 22

**No `INCONCLUSIVE` was recorded**, so Rule 22's subclass-and-resolution-path
requirement has no subject. Every measurement that ran returned a value: four
artifact digests with one blob id, two declared bindings, three scan findings
with their quoted landed text, three commit SHAs, five byte-identity
comparisons, three register-scope determinations, and two suite results.

**Nothing measured after this report will be written back.** Anything the
Reviewer raises is returned in chat.

---

## 11. Push scope

`refs/heads/science/xi-clar-01-landing` only, per `docs/BRANCHING_POLICY.md`
`science/*` scope. **Integration is a separate task and is not performed here**
— and cannot be, while `M4` is outstanding.

`refs/heads/main` is not pushed and did not move — it stands at `9af94a4a`. No
merge, no force-push, no branch deletion, no history rewrite.
