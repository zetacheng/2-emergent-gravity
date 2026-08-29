# Report — `P2-XI-CLAR-01-LANDING` v3: resumption from the `M4` stop, COMPLETE

    Specification   specs/2026-08-24T0900Z_xi-clar-01-landing_v3.md
    Review          reviews/chatgpt/2026-08-24T0900Z_xi-clar-01-landing_v3.md
    Branch          science/xi-clar-01-landing — commits appended to the
                    existing stopped branch. NO new branch was cut.
    Base            science/xi-clar-01-landing @
                    2936e967f7fb893e455547e348243bf49b56aff4  (the stopped
                    branch tip, NOT main)
    main            9af94a4a11cd06e90ef2d24183565412b4043c6a — unmoved, and
                    not touched by this task
    Commit points   Base       2936e967f7fb893e455547e348243bf49b56aff4
                    B_task     498f8524e1e0938eb5f48bf10c6315ae3518a2ef
                    H_land     61b08811c5782bda7132530ac6ba39991d22cea4
                    T          61b08811c5782bda7132530ac6ba39991d22cea4  (= H_land)
    Scope of file   `M0` through `M6a`, and nothing later.

**This report does not state its own commit SHA.** It is committed onto
`T = 61b08811c5782bda7132530ac6ba39991d22cea4`, and **it is itself the next
commit on `T`.** `H_final` is measured externally, after this commit exists, and
is not named inside this report.

---

## 0. Execution location and worktree identity (Amendment D step 0)

    execution location      /home/user/2-emergent-gravity
    worktree toplevel       /home/user/2-emergent-gravity
    branch at start         science/xi-clar-01-landing @ 2936e967
    repository is shallow   false
    UTC at report           2026-08-29T1648Z

---

## 1. Bindings verified before any write

    ARTIFACT                     SHA-256                                                            BYTES
    v3 specification             0a6c9e2bed9a9541e5a09561fef91e9fd5e59f940c472b875413d5c31ad2d1cb   13458
    its pre-execution review     93b7e4d7ff4ead9739892d3c58e1f255830093de51599852cfb3f0dbe9b2ad57    4764

The review carries `Reviewed specification SHA-256` twice, and
`0a6c9e2bed9a9541e5a09561fef91e9fd5e59f940c472b875413d5c31ad2d1cb` is the only
64-hex string in it. It equals the specification's sha256 and the sha256 of the
committed spec blob at `a564a68`. Verdict `APPROVE FOR EXECUTION`. The review
has no pre-committed hash; the digest above is its first recorded one,
provenance transmitted by the PI in session.

---

## 2. Results carried forward from v2, BY REFERENCE

**`M1`, `M2`, `M2b` and `M3` were executed under v2 and are NOT re-run here.**
They are carried forward by reference, not by re-assertion:

    reports/2026-08-24T0043Z_xi-clar-01-landing.md

That report's §2 records `M1` and `M2`; its §3 records the three-item `M2b`
correspondence scan, all `RESOLVE`, including the scope relation between the
landed criterion's "For every admissible decoupling `α`" and the
clarification's landed-decoupling scope; its §4 records the `M3` landing.
**Those measurements are not restated here**, and this report does not
re-derive them.

**They are re-verified only by identity, at `M0`.**

---

## 3. `M0` — resumption audit, before any write

**All five items match. `A0` did not fire.**

    (1) branch tip equals the Base, full string
          measured 2936e967f7fb893e455547e348243bf49b56aff4
          Base     2936e967f7fb893e455547e348243bf49b56aff4      EQUAL

    (2) main equals 9af94a4a and does not contain the clarification
          measured 9af94a4a11cd06e90ef2d24183565412b4043c6a
          stated   9af94a4a11cd06e90ef2d24183565412b4043c6a      EQUAL
          command  git ls-tree -r --name-only 9af94a4a \
                     -- decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md
          output   ''            ABSENT, as required

    (3) the clarification on the Base has the stated identity
          sha256 measured 0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22
          sha256 stated   0e549c7c457f22d8e80b62fbca00cf362c410992771ddcee6cad13dc0d363f22
          blob   measured 1786124bbe3bfa02809d83c2890d0800e0d3edd8
          blob   stated   1786124bbe3bfa02809d83c2890d0800e0d3edd8      MATCH on both

    (4) DECISION_LOG.md at the Base is byte-identical to main's
          at the Base  138776 bytes, sha256 d3d907c37ca0fed55d683acd1e6c82ec53c292145317f56cb2b5e98616ab6a68
          at main      138776 bytes, sha256 d3d907c37ca0fed55d683acd1e6c82ec53c292145317f56cb2b5e98616ab6a68
          blob id both 5879d746b8b1530e4370fd6b5ed8f0be9f47bcd0
          BYTE-IDENTICAL — the v2 run wrote nothing to it, so the append-only
          reasoning of M4/M5 rests on main's own bytes

    (5) the register record's §4 statement is present
          decisions/2026-08-24-xi-rulings-02-clarification-01.md:119
          "### 4. THE OPEN ITEM THE CLARIFICATION DIRECTS IS NOT YET REGISTERED"
          quoted in full at §5 of the stop report; present and located

---

## 4. `B_task` — the v3 provenance commits

    a564a68  spec(P2-XI-CLAR-01-LANDING v3): resumption from the M4 stop, with the PI register ruling
    498f852  review(P2-XI-CLAR-01-LANDING v3): ChatGPT pre-execution review, APPROVE FOR EXECUTION

    B_task                    498f8524e1e0938eb5f48bf10c6315ae3518a2ef
    commits Base..B_task      2

**The binding was measured before the spec commit**, not after. Nothing was
committed between the two.

---

## 5. `M2c` — provenance extraction for the ruled mechanism

**`A1` did not fire: both nodes located at the Base.**

### 5a. `M2c(a)` — the landed `UNESTABLISHED` format precedent

`DECISION_LOG.md:2147-2215` at the Base — the 2026-08-19 `POLE-B0` construction
item. Its entry structure is the format `M4` follows:

    :2147   heading, dated, naming the open item and its UNESTABLISHED status
    :2149   Date
    :2150   Decision owner: Principal Investigator
    :2151   Effect
    :2153   ### Decision, with the item quoted verbatim as a blockquote
    :2167   **Status: UNESTABLISHED.** inside the quoted item
    :2194   ### Reason
    :2213   ### Consequences

**Its `Reason` states the mechanism's authority**, `DECISION_LOG.md:2199-2200`,
quoted verbatim:

```text
That distinction determines which register admits it, and this log is the
register whose stated scope covers an item opened as `UNESTABLISHED`.
```

**And its `Reason` surveys the other registers and reaches the same finding the
`M4` stop reached** — `:2202-2211` records that `P2-DEFERRED-ITEMS` scopes
itself to considered-and-postponed work, `P2-PHASE-01_C-CHECK_OPEN-ITEMS` to the
C-check line, and `GOVERNANCE-DEBT` to rule gaps rather than scientific
questions. **The stop and the ruling are consistent, not in tension.**

### 5b. `M2c(b)` — the clarification's registration direction and escalation condition

From the landed issued bytes,
`decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md:32-40`, extracted at 579
bytes, sha256 `a15b2b652ff01216f20409e68a7a5741f25f64f77da2b472faa610c124d217b1`:

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

**The escalation condition alone**, `:36-40`, is 305 bytes with its terminator,
sha256 `1270f73fd098326085321d3eccc9dc3286e21a47cd40686008293f091836e025`. It is
this span that `M4` reproduces byte-identical.

**The family-membership note** is at `:51-54` of the same file, in the
`RATIONALE`: the family-wide question "concerns the reliability of the
representation across a decoupling family, whose membership is itself an
unlanded model-level choice".

---

## 6. `M3b` — the canonical record of the PI ruling

    path   decisions/2026-08-24-xi-open-item-register-routing.md
    key    2026-08-24-xi-open-item-register-routing

**The ruling was extracted from the committed specification blob, not
retyped:**

    extraction        git cat-file blob <spec-blob>:specs/2026-08-24T0900Z_xi-clar-01-landing_v3.md
                      | sed -n '92,99p'
    extracted bytes   590 with the trailing terminator; the landed fenced block
                      is 589 bytes, the same span without the final newline that
                      the fence supplies
    sha256 of the extraction
                      85c0827436f42a8bdcaa020229de120e745ed82ce1e5f5b783ea989135716198

**It is landed in the language it was issued in**, inside a fenced block with
its `> ` markers intact, so the landed bytes are §0c's bytes and not a
re-rendering. **The English rendering beneath it is marked "A working
translation, identified as such", with "THE ISSUED TEXT GOVERNS ... It is not
the ruling and is not to be cited as it."**

**Byte-identity of all three quotations in the record, measured:**

    PI ruling, spec §0c :92-99          landed 589 B   source 589 B   BYTE-IDENTICAL
    P2-DEFERRED-ITEMS.md :19-26         landed 498 B   source 498 B   BYTE-IDENTICAL
    DECISION_LOG.md :2199-2200          landed 143 B   source 143 B   BYTE-IDENTICAL

**A citation defect was found and corrected before the commit was pushed, and is
recorded rather than absorbed.** The `P2-DEFERRED-ITEMS` quotation was first
written as a sentence-accurate excerpt labelled `:19-23`; measurement showed the
landed block (290 B) did not equal that line range (348 B), because the excerpt
stopped mid-line at "settled." The block was replaced with the byte-exact
`:19-26` span and the label corrected, and the commit amended. **The label and
the bytes now agree.**

**The ruling's own scope limits are recorded as a list** at §3 of the record —
this item only; no register's scope extended; no register created; no general
rule for future XI-line open items — **and every one of them is in the issued
text, not an addition by the record.** The record states explicitly that
`derivations/P2-DEFERRED-ITEMS.md` is not extended to the XI line and that the
`M4` stop's finding about its scope stands.

**PART 2 is marked `REVIEW PENDING`** per `decisions/README.md`.

---

## 7. `M4` — registration of the directed open item

**Appended to `DECISION_LOG.md` in the `M2c(a)` format.**

    heading   ## 2026-08-24 — Open item: family-wide representation stability
              of the ξ ledger is UNESTABLISHED
    Date: 2026-08-24
    Decision owner: Principal Investigator
    Effect: opens the representation-stability inquiry as an open item

**Every required element measured present in the entry:**

    Date / Decision owner / Effect                              present
    ### Decision / ### Reason / ### Consequences                present
    Status: UNESTABLISHED. REGISTERED, NOT AUTHORIZED.          present
    "Registration is not authorization"                         present
    link to P2-FIERZSUM-01 §8                                   present
    the unlanded model-level family-membership note             present
    Reason cites decisions/2026-08-24-xi-open-item-register-routing.md  present
    the ruling's scope limit, "for this item only"              present

**The escalation condition is BYTE-IDENTICAL to the clarification's.** Measured
against `decisions/P2-XI-RULINGS-02-CLARIFICATION-01.issued.md:36-40` after
stripping the blockquote prefix the entry adds:

    landed  304 B
    source  304 B
    BYTE-IDENTICAL: True

**The question is stated no broader and no narrower than the clarification
states it** — it is quoted from the clarification's own words, and the entry
adds no scope of its own.

---

## 8. `M5` — the landing index append

Appended after the `M4` entry: decision key
`2026-08-24-xi-rulings-02-clarification-01`, the issued-file path, the issuance
SHA-256 `0e549c7c…0d363f22`, the review verdict `FIT FOR RECORDING`, and the
identifier of the open item registered at `M4`.

**Ordering and append-only, both measured on the committed state:**

    M4 entry offset in the product   137979
    M5 index offset                  142862
    M4 PRECEDES M5                   True

    DECISION_LOG.md at the Base      138776 bytes
    at H_land                        146709 bytes
    appended                           7933 bytes
    diff                             179 insertions, 0 deletions
    Base bytes are an exact byte-prefix of the product   True

---

## 9. `M5b` — the register-record correction

**Appended a dated note to
`decisions/2026-08-24-xi-rulings-02-clarification-01.md`. The original §4
sentence is NOT edited.**

The note records: that §4's statement was true when written and its register
survey stands unchanged; that it is false as a statement about the present; what
registered the item, with the ruling's path and key; the ruling's scope limit;
and the `M4` entry's identifier.

**Measured on the committed state:**

    at the Base            14040 bytes
    at H_land              16568 bytes
    appended                2528 bytes
    Base bytes are an exact byte-prefix of the result        True
    every line the file had at the Base is unchanged and in place   True
    line 119 at the Base and at H_land are identical         True
    §4 body lines 119-142 identical                          True

**That last row is the check that matters:** the §4 heading and its whole body
survive byte-for-byte, so the historical statement is preserved and clarified,
not rewritten.

    H_land = 61b08811c5782bda7132530ac6ba39991d22cea4

---

## 10. `M6a` — suite, on a full tree, at both ends

    main
      commit     9af94a4a11cd06e90ef2d24183565412b4043c6a
      tree SHA   9353d6282cb9bee47a0b64f66eda524f1ef2265b
      shallow    false
      result, verbatim   344 passed, 2 deselected in 45.16s

    T — the post-M5b tree
      commit     61b08811c5782bda7132530ac6ba39991d22cea4
      tree SHA   852599c3b0a042aa1c71b1326e8a4bdecabc5e48
      shallow    false
      result, verbatim   344 passed, 2 deselected in 39.10s

**No test fails on `T` that passes at `main`.** Both failure sets are empty and
the counts are identical, as expected for a task that adds no code.

**These are the `M6a` measurements, taken after the resumed `M4`/`M5`/`M5b`
state actually exists.** The environmental suite runs recorded in the v2 stop
report §6 were explicitly labelled there as **not** `M6a`, and are not promoted
into this evidence.

---

## 11. Acceptance criteria

`C6`'s second limb is measured after this commit and is recorded in the
branch-only addendum.

    C0  (M0)          PASS   All five resumption-audit values match: branch tip,
                             main, the clarification's sha256 and blob id, the
                             DECISION_LOG identity with main, and the register
                             record's §4 statement present.
    C1  (M2c)         PASS   Both extracted nodes appear as verbatim quotations
                             with path:line resolving at the Base — the
                             UNESTABLISHED precedent at DECISION_LOG.md:2147-2215
                             with its Reason at :2199-2200, and the
                             clarification's direction and escalation condition
                             at :32-40.
    C2  (M3b)         PASS   The canonical record exists at
                             decisions/2026-08-24-xi-open-item-register-routing.md
                             with §0c's ruling byte-identical (589 B), in the
                             language issued, its English rendering marked a
                             translation and not the ruling, and the ruling's own
                             scope limits stated as a list.
    C3  (M4)          PASS   The entry is in the M2c(a) format with Status
                             UNESTABLISHED and REGISTERED, NOT AUTHORIZED; the
                             escalation condition is byte-identical to the
                             clarification's (304 B); the
                             registration-is-not-authorization sentence is
                             present; the Reason cites M3b's canonical record.
    C4  (M4/M5/M5b)   PASS   The Base's DECISION_LOG.md bytes are an exact
                             byte-prefix of the product; the M4 entry precedes
                             the M5 index entry, by measured offset; the register
                             record's Base bytes are an exact byte-prefix of its
                             M5b result, and its original §4 sentence — heading
                             and body — is unedited.
    C5  (M6a)         PASS   No test fails on T that passes at main.
    C6  (M6b, M6c)    PASS on its first limb: this report records M0 through M6a
                             and no later measurement, names T, does not assert
                             its own SHA or H_final, and carries v2's results by
                             reference to the stop report at its path rather than
                             re-asserting them. **Its second limb — that H_final
                             differs from T only by this report — is measured in
                             the addendum**, because the diff cannot be taken
                             until H_final exists.

---

## 12. Abort conditions

    A0  DID NOT FIRE   Every M0 value matches, measured before any write. In
                       particular DECISION_LOG.md at the Base is byte-identical
                       to main's, so the v2 run wrote nothing to it and the
                       append-only reasoning of M4/M5 stands as specified.
    A1  DID NOT FIRE   Both M2c nodes located at the Base.
    A2  DID NOT FIRE   No passage in the canonical record, the M4 entry, or the
                       M5b note states the ruling or the clarification more
                       narrowly, more broadly, or more specifically than the
                       issued text. The ruling and the escalation condition are
                       byte-identical quotations; the question is quoted from the
                       clarification's own words; the ruling's scope limits are
                       reproduced from the ruling and not summarised into
                       something stronger. **The one citation defect found — a
                       line-range label that did not match its bytes — was
                       corrected before push and is recorded at §6, not
                       absorbed.**
    A3  DID NOT FIRE   **No register's scope was extended or modified, no
                       register was created, and no general rule for future
                       XI-line open items was stated.** The canonical record says
                       so explicitly and names P2-DEFERRED-ITEMS.md as
                       specifically not extended. The M4 entry uses an existing
                       mechanism with a landed precedent; it does not enlarge it.
    A4  DID NOT FIRE   **No step began, scheduled, constrained or prioritised**
                       the Q-M3 check, the Q-M2 scope assessment, or the
                       registered representation-stability inquiry. The item is
                       registered REGISTERED, NOT AUTHORIZED, and the entry says
                       in terms that registration is not authorization and that
                       the escalation condition is recorded, not triggered —
                       it requires both a DEPENDENT return and subsequently
                       established L-growth, and this task establishes neither.
    A5  DID NOT FIRE   The original §4 sentence is unedited (§9, measured
                       line-by-line); no landed byte of the stop report was
                       touched; and no file arriving from v2's M3 was modified
                       other than by the M5b append to the register record, which
                       M5b directs and which preserves every Base byte in place.
    A6  DID NOT FIRE   No merge, no fast-forward, and main is unmoved at
                       9af94a4a. Integration is a separate task.

---

## 13. Environment

    python 3.11.15, numpy 2.4.6, sympy 1.14.0, pytest 9.1.1, ruff 0.16.3
    scipy ABSENT — as on every preceding task in this session
    repository non-shallow at both M6a runs

---

## 14. Stops and clarifications (Amendment B)

**No stop. The task completed.** The `M4` stop of the v2 run is resolved, not
carried forward.

**Primary category, for the one thing worth a reader's attention:
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — and it is now narrower than it
was.**

### 14a. What the ruling settled, and what it left open

**Settled: where this one item is filed.** The item is registered.

**Left open, by the ruling's own terms:** where future XI-line open items are
registered. The ruling says that is "left to be ruled separately if and when
needed", and **this task recorded that limit rather than quietly generalising
from it.** The next XI-line open item will face the same register survey the
`M4` stop performed, unless a later ruling settles it.

**Also left standing:** the `M4` stop's finding that
`derivations/P2-DEFERRED-ITEMS.md`'s stated scope is bound to `P2-PHASE-01`.
The ruling did not overturn it and did not need to; it identified a different
mechanism.

### 14b. What is registered is not authorized

**The representation-stability inquiry is registered and not commissioned.** Its
escalation condition is recorded and not triggered. `Q-M3` remains conditional
on the landed Hubbard–Stratonovich decoupling, and the family-wide residue sits
in the register rather than attaching to that binary membership check.

### 14c. This landing does not make the clarification canonical

**`main` is unmoved at `9af94a4a` and does not contain the clarification.**
Integration is a separate reviewed task. **`P2-XI-QM3-DEP-01`'s `M0`
prerequisite — the clarification at its canonical path on the appropriate Base —
is not satisfied by this landing alone.**

### 14d. Rule 22

**No `INCONCLUSIVE` was recorded.** Every measurement returned a value: five
resumption-audit comparisons, two binding digests, two extracted provenance
nodes with their digests, four commit SHAs, five byte-identity comparisons,
eight element-presence checks on the `M4` entry, two byte-prefix relations with
their byte counts, one entry-ordering offset comparison, one line-by-line
identity check over the register record, and two suite results.

**Nothing measured after the addendum will be written back.** Anything the
Reviewer raises is returned in chat.

---

## 15. Push scope

`refs/heads/science/xi-clar-01-landing` only, per `M6c` and
`docs/BRANCHING_POLICY.md` `science/*` scope.

**`main` is not pushed and is not touched** — it stands at
`9af94a4a11cd06e90ef2d24183565412b4043c6a`. No merge, no fast-forward, no
force-push, no branch deletion, no history rewrite. **Integration is a separate
task and is not performed here.**

---

# ADDENDUM — `M6c`: `H_final`, the `C6` diff, and the push

**On this branch ONLY.** `main` is not touched. This addendum exists because
`C6`'s second limb observes an object that does not exist until the report is
committed — and because §0 committed this report to not naming `H_final`, which
is recorded here now that it exists.

## A1. `H_final`

    T          61b08811c5782bda7132530ac6ba39991d22cea4
    H_final    ba9987a2cb5e11e4df975289e4da5ae463fe56a9

That is the SHA the report deliberately did not state.

## A2. `C6`, second limb — measured, not asserted

`git diff --stat T H_final`:

```
 .../2026-08-29T1648Z_xi-clar-01-landing-resumed.md | 488 +++++++++++++++++++++
 1 file changed, 488 insertions(+)
```

`git diff --name-status`:

```
A	reports/2026-08-29T1648Z_xi-clar-01-landing-resumed.md
```

    files changed   1 — the M6b report artifact, and nothing else

**`H_final` differs from `T` only by the report artifact. `C6` PASSES on both
limbs.**

## A3. The push

    pushed   refs/heads/science/xi-clar-01-landing
    main     NOT pushed, NOT touched — stands at
             9af94a4a11cd06e90ef2d24183565412b4043c6a

**Integration is a separate task and was not performed.**

## A4. The branch, end to end

    Base       2936e967f7fb893e455547e348243bf49b56aff4   the v2 stop tip
    a564a68    + the v3 specification
    B_task     498f8524e1e0938eb5f48bf10c6315ae3518a2ef   + its bound review
    496ff0d    + M3b, the canonical record of the PI ruling
    H_land     61b08811c5782bda7132530ac6ba39991d22cea4   + M4, M5, M5b
    T          61b08811c5782bda7132530ac6ba39991d22cea4   = H_land
    H_final    ba9987a2cb5e11e4df975289e4da5ae463fe56a9   + the M6b report

## A5. Final state of what the task was for

    the issued clarification        landed byte-exact, sha256 0e549c7c…0d363f22
    its document review             landed byte-identical, FIT FOR RECORDING
    its register record             landed, with the M5b note appended and its
                                    original §4 unedited
    the PI register ruling          landed byte-identical, PART 2 REVIEW PENDING
    the directed open item          REGISTERED — DECISION_LOG.md, 2026-08-24,
                                    "Open item: family-wide representation
                                    stability of the ξ ledger is UNESTABLISHED"
                                    Status: UNESTABLISHED. REGISTERED, NOT
                                    AUTHORIZED.
    the landing index               appended after it

**Nothing is authorized.** The `Q-M3` check, the `Q-M2` scope assessment and the
registered inquiry are all exactly where they were.
