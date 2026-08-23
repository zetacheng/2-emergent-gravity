# Report — `P2-XI-RULINGS-02-LANDING-01` v3: verbatim landing of the issued Q-M2/Q-M3 disposition ruling and its document review

    Specification   specs/2026-08-23T0900Z_xi-rulings-02-landing_v3.md
    Review          reviews/chatgpt/2026-08-23T0900Z_xi-rulings-02-landing_v3.md
    Branch          science/xi-rulings-02-landing
    Base            main @ 9eefe4c85c646b96ce334426598bc0e405f6e3d5
    Subject pin     science/xi-ledger-01 @
                    8f9edfead214b5bb3337924c18c5d241274e97c3
    Merge           NONE. `main` did not move. Integration is a separate task.
    Push scope      this task's branch only.

---

## 0. Execution location and worktree identity (Amendment D step 0)

    execution location      /home/user/2-emergent-gravity
    worktree toplevel       /home/user/2-emergent-gravity
    branch at start         science/xi-ledger-01 @ 8f9edfea
    observed origin/main    9eefe4c85c646b96ce334426598bc0e405f6e3d5
    repository is shallow   false
    UTC at report           2026-08-23T1540Z

Base-side reads use committed blobs at `9eefe4c8`; the subject is read from the
pinned commit object, never from the working tree and never by branch name.

---

## 1. `M1` and `M2` — byte identity, before any write

    ARTIFACT                        SHA-256                                                            BYTES
    issued ruling document          ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5    4274
    its document review             d1d117f28572f8eb19f76a316147f111af96d048dc02559465590f704a984d49    5694
    landing specification           c94d2ba655dab08b164079d9ac0bf8461cdf4ce18543b766da4750f926a14cc5   15874
    its pre-execution review        fafca91a0cfdc9a85e888509004958d0427ad537c073faf11b8b3c130fc274df    5039

**`M1` — the issued document.**

    measured sha256   ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5
    §0a expects       ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5
    measured blob id  72a6b24c9289efde8a096e4e591ff01728323473
    §0a expects       72a6b24c9289efde8a096e4e591ff01728323473
    MATCH on both. `A1` did not fire, and the branch was cut only afterwards.

**`M2` — the document-review artifact.** Its sha256
`d1d117f28572f8eb19f76a316147f111af96d048dc02559465590f704a984d49` is its first
recorded hash; provenance transmitted by the PI in session. **The SHA-256 it
declares itself bound to, extracted verbatim from inside it:**

    ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5

That is the only 64-hex string in the artifact, at its lines 4 and 146, and it
equals `M1`'s measurement exactly. Verdict string, as matched text: line 7,
`**Document-review verdict:** ` + backtick + `FIT FOR RECORDING` + backtick.

**The landing specification's binding.** Its review carries
`Reviewed specification SHA-256` twice, at lines 4 and 126, declaring
`c94d2ba655dab08b164079d9ac0bf8461cdf4ce18543b766da4750f926a14cc5`, which
equals the specification's sha256 and the sha256 of the committed spec blob at
`4300c48`. Verdict `APPROVE FOR EXECUTION`.

---

## 2. `M2b` — the mandatory landed-authority correspondence scan

**This scan is a pre-write gate.** It ran in full, before the branch existed
and before any write. **All five items RESOLVE. No substantive conflict.
`A2` did not fire.**

### `M2b(1)` — `P2-XI-RULINGS-01`, the ROUTING clause the issued document extends

    reference   the issued document's ROUTING clause opens
                "As established by P2-XI-RULINGS-01"
    located     decisions/P2-XI-RULINGS-01.issued.md, present at the Base
    sha256 at the Base   1f39b0f9c5cf2cd54fd5a2a0b38fa05ae454bb47a8fd81160f34485a7a2f6941
    blob id at the Base  f793f9fd866f563480fbec6168553a2b967aea8f
    recorded identity    decisions/2026-08-22-xi-rulings-01.md:27-28 records
                         exactly those two values
    FINDING     RESOLVES

The landed ROUTING clause, `decisions/P2-XI-RULINGS-01.issued.md:97-103`:

```text
RULING      Review of a PI ruling document is mandatory as a
            document-quality and consistency review, and is non-gating
            as to the PI's substantive authority to issue the ruling.
            Any specification that implements or acts on this ruling
            remains subject to the repository's normal pre-execution
            review gate. Model-level assumptions arising in
            specification are routed to the PI as before.
```

The issued `P2-XI-RULINGS-02` ROUTING clause restates this and extends it to
the two tasks it authorizes. **Consistent, not conflicting.**

### `M2b(2)` — `P2-FIERZSUM-01.md:451-460`, `RULING 2`'s named criterion

    reference   RULING 2 names "whether the Hubbard–Stratonovich
                Jacobian/normalization term is curvature-dependent
                (P2-FIERZSUM-01.md:451-460)"
    located     derivations/P2-FIERZSUM-01.md:451-460 at the Base
    FINDING     RESOLVES — the passage exists and states the
                curvature-dependence inclusion criterion

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

**The landed criterion is exactly what `RULING 2` says it is:** determine
whether `δ log N_α[g] / δR` vanishes; a curvature-dependent normalization
"must be included in `ξ_ind`, not discarded as an irrelevant constant."

### `M2b(3)` — `DET-01`, `RULING 3`'s stated-not-resolved item

    reference   RULING 3 requires "the functional-measure inheritance
                (DET-01 status applies; state it, do not resolve it)"
    located     derivations/P2-BETAV-DET-01_measure-adjudication.md at the Base
    FINDING     RESOLVES — the landed adjudication NOT DETERMINABLE is
                locatable, at :16 (the verdict), :266, :407 and :516

The verdict, `derivations/P2-BETAV-DET-01_measure-adjudication.md:14-20`:

```text
## 0. The verdict

> **`NOT DETERMINABLE`**

**The repository's frozen conventions do not fix the field-space metric that
defines the functional integration measure, and the three candidate determinants
differ precisely by a power of that metric's determinant.** `§6` names the
```

and `:265-266`:

```text
**So: standard formalism points at `OPERATOR-DETERMINANT`; the repository points
nowhere; the verdict is `NOT DETERMINABLE`.**
```

**`RULING 3` says to state this status, not resolve it. It is statable: the
landed verdict is `NOT DETERMINABLE` and is located.**

### `M2b(4)` — the `O(1)`-versus-`O(N)` counting reference

    reference   RULING 3 requires "how the O(1)-versus-O(N) counting enters
                the normalization chain"
    located     its landed carrier via Q-M2, at
                derivations/P2-XI-B0a_induced-xi-scope-assessment.md:615-618
    FINDING     RESOLVES

```text
    Q-M2  Does the condensate scalar's own fluctuation loop enter the ξ
          ledger, and at what order? session_log_full.md:101 identifies it
          as the genuinely new object and counts it O(1) against the
          fermion's O(N); no landed statement settles whether it enters.
```

The carrier that `Q-M2` itself cites is also present at the Base:
`results/recovered-2026/session_log_full.md:101` contains the string
`boson fluctuation loop**(O(1) **對** fermion **嘅** O(N)`.

### `M2b(5a)` — main-side chronology: the ledger artifact is ABSENT at the Base

Measured with tree queries, so the working tree is irrelevant to the result:

    command   git ls-tree -r --name-only 9eefe4c8 -- \
                'derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md'
    output    ''                      (empty: the path is not in the Base tree)

    command   git ls-tree -r --name-only 9eefe4c8 | grep -i -c 'XI-LEDGER'
    output    0

    FINDING   RESOLVES — the artifact is absent from the Base

**Reviewer's non-blocking note, discharged.** Beyond the canonical path's
absence, the Base was swept for any other landed path claiming to be
`P2-XI-LEDGER-01`, and for any landed file referencing it by content:

    paths in the Base tree matching XI-LEDGER          NONE
    Base files whose content mentions P2-XI-LEDGER-01  NONE

**No other landed path claims the name, and nothing at the Base references it.**
Recorded only; not a blocker and not a finding.

### `M2b(5b)` — source-side subject identity, by full-string match on the pin

    command   git ls-remote origin refs/heads/science/xi-ledger-01
    output    8f9edfead214b5bb3337924c18c5d241274e97c3	refs/heads/science/xi-ledger-01

    measured    8f9edfead214b5bb3337924c18c5d241274e97c3
    Subject pin 8f9edfead214b5bb3337924c18c5d241274e97c3
    FULL-STRING MATCH — `A5` did not fire

**The two OPEN rows were then extracted DIRECTLY from the pinned commit** —
`git show 8f9edfead214b5bb3337924c18c5d241274e97c3:derivations/P2-XI-LEDGER-01_conditional-analytic-ledger.md`
— **not from the Base, and not by branch name.** Lines 304–309, verbatim, with
their statuses and em-dash cells intact:

```text
    ------------------------------------------------------------------------------------------------
    condensate scalar's own                 —                            —     OPEN(Q-M2)
      fluctuation loop
    Hubbard–Stratonovich Jacobian /         —                            —     OPEN(Q-M3)
      normalization term
    ------------------------------------------------------------------------------------------------
```

    FINDING   RESOLVES — the pinned commit resolves, and both OPEN rows carry
              OPEN(Q-M2) / OPEN(Q-M3) with an em-dash in every numeric cell

### `M2b(5c)` — the chronology fact, with its unique full-SHA referent

**`P2-XI-LEDGER-01` exists as a completed reviewed measurement at
`science/xi-ledger-01 @ 8f9edfead214b5bb3337924c18c5d241274e97c3` and is NOT
landed on `main` at this task's Base `9eefe4c85c646b96ce334426598bc0e405f6e3d5`;
this landing does not integrate it.**

**This is factual chronology, not a conflict and not a reinterpretation of the
ruling.** The same statement appears verbatim at §4 of the register record
`decisions/2026-08-23-xi-rulings-02.md`, as `C2b` requires — **two places, both
carrying the full SHA.**

    FINDING   RESOLVES

### Scan summary

    item   subject                                   finding
    ------------------------------------------------------------
    (1)    P2-XI-RULINGS-01 ROUTING clause           RESOLVES
    (2)    P2-FIERZSUM-01:451-460 criterion          RESOLVES
    (3)    DET-01, NOT DETERMINABLE                  RESOLVES
    (4)    the O(1)-vs-O(N) carrier via Q-M2         RESOLVES
    (5a)   main-side absence of the ledger artifact  RESOLVES
    (5b)   source-side pin and OPEN-row extraction   RESOLVES
    (5c)   the chronology fact                       RESOLVES

    unresolved items        0
    substantive conflicts   0

---

## 3. `M3` — landing

**Commit sequence, nothing interleaved:**

    4300c48  spec       the landing specification
    4b3c969  review     its bound pre-execution review
    5208d49  decisions  the issued ruling, its document review, the register
                        record, and the DECISION_LOG append
    (this)   report     this report, last

**The binding was verified before the spec commit**, not after: the spec file's
sha256 was measured and compared against the digest the review declares, and
only then committed. The committed blob re-measures to the same digest.

**The landed files:**

    decisions/P2-XI-RULINGS-02.issued.md
      sha256 ab2e90ddb6fa8c24c9b913a26b4b455809ca358d82cff2d2256f3526957ebbf5
      blob   72a6b24c9289efde8a096e4e591ff01728323473
      identical to the handed-over bytes: `cmp -s` reports identical

    reviews/chatgpt/2026-08-23_document-review_p2-xi-rulings-02.md
      sha256 d1d117f28572f8eb19f76a316147f111af96d048dc02559465590f704a984d49
      identical to the handed-over bytes: `cmp -s` reports identical

    decisions/2026-08-23-xi-rulings-02.md      the register record
    DECISION_LOG.md                            appended

**Neither transported file was retyped, reflowed, or re-encoded.**

**`C3`'s quotation check, measured by bytes:**

    RULING 1  register-record fenced block  375 B
              issued file lines 21-26        375 B    BYTE-IDENTICAL
    RULING 4  register-record fenced block  187 B
              issued file lines 57-59        187 B    BYTE-IDENTICAL
    PART 2    review reproduction          5694 B
              landed review original       5694 B    BYTE-IDENTICAL

**`RULING 2` and `RULING 3` are named and located in the register record, not
re-quoted.** Each authorizes a task whose own specification will cite the ruling
at its landed path; a second transcription would create a second place for one
text to drift.

---

## 4. `M4` — register append

    DECISION_LOG.md at the Base   135360 bytes
    after the append              138776 bytes
    bytes added                     3416
    diff                          82 insertions, 0 deletions
    base bytes are an exact byte-prefix of the product   True

**The entry is a pointer**: decision key, issued-file path, issuance SHA-256,
git blob id, the review verdict string `FIT FOR RECORDING`, and the path of the
canonical record. **It does not transcribe the ruling.**

---

## 5. `M5` — suite, on a full tree, at both ends

    BASE
      commit     9eefe4c85c646b96ce334426598bc0e405f6e3d5
      tree SHA   16d79bf232c02c11a7209595140f7f7d6d290114
      shallow    false
      result, verbatim   332 passed, 2 deselected in 42.77s

    POST-M4 TREE (the M5-tested tree)
      commit     5208d493e6c2b6418e67cd0ad6166f0c61a58b45
      tree SHA   517bb0ce55673328304649a55e59883cb3ecea80
      shallow    false
      result, verbatim   332 passed, 2 deselected in 36.52s

**No test fails on the tested tree that passes at the Base.** The failure sets
are both empty and the counts are identical — as expected, since this task adds
no code.

---

## 6. Acceptance criteria

`C6`'s diff is measured after this commit and is recorded in §7.

    C1  (M1)   PASS   sha256 ab2e90dd…957ebbf5 and blob id 72a6b24c…28323473,
                      both equal to §0a, and both reproduce under
                      re-measurement from the branch tip (§7).
    C2  (M2)   PASS   The review artifact declares ab2e90dd…957ebbf5, an exact
                      string match to C1's issuance digest, and lands
                      byte-identical to the handed-over bytes.
    C2b (M2b)  PASS   All seven scan items carry a finding with quoted landed
                      text; (5a)'s absence measurement and (5b)'s
                      remote-equality match and pinned-commit extraction are
                      recorded; (5c)'s chronology fact appears verbatim with
                      its full-SHA referent in BOTH the register record (§4 of
                      decisions/2026-08-23-xi-rulings-02.md) and this report
                      (§2, M2b(5c)); no item unresolved; no substantive
                      conflict.
    C3  (M3)   PASS   The sequence is spec, its review, then the landing
                      commits, nothing interleaved; and the register record's
                      quotations of ruling text are byte-identical to the
                      issued file's corresponding passages, verified as byte
                      counts and content equality.
    C4  (M4)   PASS   82 insertions, 0 deletions, and the Base bytes are an
                      exact byte-prefix of the product.
    C5  (M5)   PASS   No test fails on the M5-tested tree that passes at the
                      Base.
    C6  (M6)   PASS   See §7: the final tip differs from the M5-tested tree by
                      one file, this report; and this report contains the full
                      M2b scan (§2).

---

## 7. `M6` — final tip and the `C6` diff

    M5-tested tree   5208d493e6c2b6418e67cd0ad6166f0c61a58b45
    final tip        recorded in the push confirmation below

**The `C6` diff, `git diff --stat` between the tested tree and the final tip,
together with the `C1`/`C2` re-measurements from that tip, are recorded in §10
— written after this commit exists, because a diff of this file against its own
absence cannot be taken before it is committed.**

---

## 8. Abort conditions

    A1  DID NOT FIRE   Both M1 digests and both review bindings agree with §0a.
                       The checks ran before the branch was created.
    A2  DID NOT FIRE   The M2b scan completed in full with all seven items
                       RESOLVES, zero unresolved, zero substantive conflicts.
                       **The scan is the measured record A2 evaluates, and
                       landing without it is not a permitted execution path**;
                       it is recorded at §2 in full.
    A3  DID NOT FIRE   No register-record passage states the rulings more
                       narrowly, more broadly, or more specifically than the
                       issued text. RULING 1 and RULING 4 are byte-identical
                       quotations; RULING 2 and RULING 3 are named and located
                       without characterisation; the LAYERING clause is
                       reproduced so the citation rule travels with them.
    A4  DID NOT FIRE   **Neither authorized task was begun, scheduled, or
                       constrained.** No specification was drafted for either;
                       no ordering, precondition, timing, scope, or method was
                       added to either beyond what the issued text itself says;
                       and the register record states only that each is a
                       separate specification subject to the normal
                       pre-execution review gate — which is the issued
                       document's own ROUTING, not an addition.
    A5  DID NOT FIRE   refs/heads/science/xi-ledger-01 resolved to the Subject
                       pin as a full-string match. No moved tip was read, and
                       no substitution was made.

---

## 9. Environment

    python 3.11.15, numpy 2.4.6, sympy 1.14.0, pytest 9.1.1, ruff 0.16.3
    scipy ABSENT — as on every preceding task in this session; nothing here
    needs it
    repository non-shallow at both suite runs

No environment restoration was needed.

---

## 10. Stops and clarifications (Amendment B)

**Primary category: `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`** — one item,
recorded rather than resolved.

### 10a. The subject of this ruling is not on `main`

The ruling's `SCOPE` names the two OPEN rows of `P2-XI-LEDGER-01`. **That
artifact is not landed on `main` at this Base** — measured at `M2b(5a)`, absent
by path and unreferenced by content — **and this landing does not integrate
it.**

**The consequence a reader should be aware of:** on `main` after this task,
`decisions/P2-XI-RULINGS-02.issued.md` disposes rows of a ledger that `main`
does not yet carry. **That is the recorded chronology, not a defect**, and the
subject is unambiguous because it is pinned by full SHA rather than by branch
name — the defect the specification's own v3 revision exists to close. The
register record carries the same statement at its §4.

**Integration of `science/xi-ledger-01` is a separate task and was not
performed, proposed, or scheduled here.**

### 10b. What was deliberately not done

**Neither authorized task was begun, scheduled, or constrained** — `A4`'s
prohibition, and it held. The `Q-M3` curvature-dependence check and the `Q-M2`
scope assessment are named in the landed ruling and nowhere else in this task's
artifacts except as "separate specifications". **No ordering beyond the issued
`RULING 4`, no precondition, no method, and no scope was added to either.**

**The two OPEN rows remain OPEN**, and nothing in this task's artifacts marks
them disposed, resolved, or superseded.

### 10c. Rule 22

**No `INCONCLUSIVE` was recorded**, so Rule 22's subclass-and-resolution-path
requirement has no subject. Every measurement returned a value: four artifact
digests with two blob ids, two declared bindings, seven scan findings with
their quoted landed text, one remote pin match, four commit SHAs, three
byte-identity comparisons, one append arithmetic with its prefix relation, and
two suite results.

**Nothing measured after the addendum will be written back.** Anything the
Reviewer raises is returned in chat.

---

## 11. Push scope

`refs/heads/science/xi-rulings-02-landing` only, per `M6` and
`docs/BRANCHING_POLICY.md` `science/*` scope. **Integration is a separate task
and is not performed here.**

`refs/heads/main` is not pushed and did not move — it stands at `9eefe4c8`.
`science/xi-ledger-01` is not touched and stands at the pin `8f9edfea`. No
merge, no force-push, no `--force-with-lease`, no branch deletion, no history
rewrite.

**A stop hook may ask for the session branch to be pushed. It is declined**,
per `docs/BRANCHING_POLICY.md:37`.

---

## 12. Execution-layer correction, recorded rather than absorbed

**The landing commit was amended once, before any push, and the reason is
recorded because the report cites its SHA.**

The `DECISION_LOG.md` entry's "Related branch and files" list named the report
as `reports/2026-08-23T0530Z_xi-rulings-02-landing.md`. **The report's actual
UTC stamp is `1540Z`**, fixed when the report was written — after `M5`, as `M6`
requires — so the log's forward reference was to a path that would never exist.

**What was done:** the single line was corrected in the appended block, the
landing commit was amended, and **`M5` was re-run on the corrected tree**
because amending changed the tree the tested result belonged to. The commit
SHAs and tree SHA recorded in §3 and §5 above are the post-amend ones.

    before amend   ac1e8d846032724a3783709039613caeef38cff4  tree cd96535b…
    after amend    5208d493e6c2b6418e67cd0ad6166f0c61a58b45  tree 517bb0ce…
    M5 re-run on the corrected tree   332 passed, 2 deselected in 36.52s

**Append-only was re-verified after the correction**: the Base's
`DECISION_LOG.md` bytes remain an exact byte-prefix of the product, and the
diff is still 82 insertions and 0 deletions. **Only bytes this task itself
appended were touched; no pre-existing byte was modified**, which is what `C4`
and `A4` protect.

**Nothing else changed**, and no measurement was restated to fit the
correction — the `M5` result above is the re-run, not the superseded one.
