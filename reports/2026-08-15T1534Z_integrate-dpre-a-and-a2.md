# Execution report — integrate `D-pre-A` and `D-pre-A2` together, and land them

**Specification:** `specs/2026-08-15T1534Z_integrate-dpre-a-and-a2.md`
**Specification evidence base:** `ae3604def317667b44ea59458569ba105463fd6b`
**Branch:** `science/integrate-dpre-a-and-a2`, cut from authoritative `main` @ `ae3604de…`
**Sources merged, in this order:** `27fabe17c2e56d62df4b686b57e6a654a8983520`, then `4749961a486c796f560bef94160c1e397d3e8a90`
**Classification:** MATERIAL. Governed by Rule 15, Rule 18, and **Amendments M–P and Rules 19–21.**

**Every figure below is labelled MEASURED or INTENDED.** **This report is
written at commit 4, the second merge commit, and measures nothing at commit
5.**

---

## 1. Outcome

**Two merges, both clean. Nothing auto-merged. Nothing edited.**

**MEASURED at commit 4:** both conflict lists empty; both merge-bases the
evidence base; 6 additions and 1 modification at merge 1, **10 and 1 at merge
2**; all nine arriving paths blob-identical to their contributing source; the
deferred register append-only on **both** measures with the base a **byte
prefix** of the head; 407 of 407 other paths blob-identical; validators
unchanged at 324 passed, 2 deselected; **RUN 2 exits 0 with nine of nine
`PASS`** at both prospectivity readings.

**Two findings are carried and neither is registered**, §4 forbidding it:

- **`RUN 1` does not complete, and the reason is the declaration mechanism
  working as designed.** The three specifications in the range declare
  different `append_only` sets — each correctly for its own task — and the
  mechanism refuses to reconcile them rather than guessing. §12 gives the
  measurement. **`RUN 1` governs nothing and `RUN 2` is stop-governing, so this
  is not a STOP.**
- **`A10`'s "eight arriving paths" is eight arriving ADDITIONS; there are
  nine arriving paths.** `A5`'s own decomposition gives 4+1 from `D-pre-A` and
  4 from `D-pre-A2`. **I report all nine comparisons**, all `IDENTICAL`.

**No operator is selected. No ontology question is ruled. The plaquette flux is
not weighed.**

---

## 2. Refs, and the two ancestry statuses — A1

**MEASURED, read from `origin` with `git ls-remote`:**

    refs/heads/main                            ae3604def317667b44ea59458569ba105463fd6b
    science/dpre-a-kinetic-operator-dossier    27fabe17c2e56d62df4b686b57e6a654a8983520
    science/dpre-a2-selection-discriminants    4749961a486c796f560bef94160c1e397d3e8a90

**All three match the specification. No mismatch, no STOP.**

**The two ancestry exit statuses, from the two commands A1 names and no
others:**

    git merge-base --is-ancestor 27fabe17… ae3604de…      exit 1
    git merge-base --is-ancestor 27fabe17… 4749961a…      exit 1

**Both non-zero: the dossier is an ancestor of neither `main` nor the
discriminants branch.** **That is why §0 merges both**, and §9 measures that
the merge order repaired it.

---

## 3. The review binds to these bytes — A2, and it did not on the first attempt

**MEASURED.**

    SHA-256 of the arriving specification      5e0cf03d6aeed76c8c48ad5713451d731a515a2cf2cda3c0a9a56df7baeef795
    SHA-256 the review records as reviewed     5e0cf03d6aeed76c8c48ad5713451d731a515a2cf2cda3c0a9a56df7baeef795

**Equal.** Both arriving files committed byte-identical, verified by `cmp`;
neither modified.

### 3.1 The first review carried no digest, and the task stopped

**Recorded because the stop is part of this task's history and the second
review's binding is only meaningful against it.**

**MEASURED on the review artifact first supplied:**

    'reviewed specification'              0 occurrences
    'SHA-256' / 'sha256'                  0 occurrences
    'digest'                              0 occurrences
    64-hex strings anywhere in the file   0
    'Reviewed artifact:'                  1   — a filename, not a digest

**A filename does not bind.** It does not distinguish the bytes reviewed from
any later revision under the same name, which is the substitution Amendment
`N(b)` exists to prevent. **`A2` could not be satisfied under any reading**, so
the task stopped before creating a branch or any commit, and `main` was
untouched.

**The corrected review carries the digest and names it correctly**, and the
`{=tex}` conversion damage present in the first artifact — 5 lines of it — is
absent from the second. **MEASURED: 0 occurrences of `{=tex}`.**

**This is `G-05` in the freshly landed debt register behaving exactly as
recorded:** *"No mechanism compares a review's cited specification digest
against the specification committed beside it. Amendment N(b) states the
obligation; nothing checks it."* **Nothing in the repository caught it. A
per-task acceptance criterion did**, which is the authoring habit `G-04`
records as insufficient in general. **The instance is reported; no register
entry is added**, per §4.

---

## 4. Merge parentage — A3, six values separately derived

**Merge 1, commit 3 = `79773d51`, MEASURED:**

    parent 1          04b943994d18e7436c28c622e15e5bc65876a72c   this task's review commit
    parent 2          27fabe17c2e56d62df4b686b57e6a654a8983520   the dossier
    merge-base(1,2)   ae3604def317667b44ea59458569ba105463fd6b   the evidence base

**Merge 2, commit 4 = `45d8e0ff`, MEASURED:**

    parent 1          79773d5158efb95993b4dccb9c7fecd8313bb284   the first merge commit
    parent 2          4749961a486c796f560bef94160c1e397d3e8a90   the discriminants
    merge-base(1,2)   ae3604def317667b44ea59458569ba105463fd6b   the evidence base

**Each equals what A3 requires**, and **both merge-bases are the evidence
base** — verified independently for each merge, not inferred from the first.

**Neither merge-base is its own parent 1**, because parent 1 in each case
already carries commits made after the base on this branch.

### 4.1 No conflict in either merge — A4

**MEASURED, both merges:** `git diff --diff-filter=U` returns nothing and the
index carries **0** unmerged entries.

**MEASURED: no `Auto-merging` line was emitted by either merge.** Nothing was
content-merged, so Amendment `P(b)`'s line-survival check has no auto-merge to
verify; §6 gives the reason from the merge case.

---

## 5. Scope — A5 and A6

### 5.1 A6, derived from EACH SOURCE and not from A5

**MEASURED, `ae3604de…` to each source independently:**

    D-pre-A   27fabe17
      M  derivations/P2-DEFERRED-ITEMS.md
      A  derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md
      A  reports/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md
      A  reviews/chatgpt/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md
      A  specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md
         4 additions, 1 modification

    D-pre-A2  4749961a
      A  derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md
      A  reports/2026-08-15T1343Z_dpre-a2-selection-discriminants.md
      A  reviews/chatgpt/2026-08-15T1343Z_dpre-a2-selection-discriminants.md
      A  specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md
         4 additions, 0 modifications

**MEASURED: the two source path sets are DISJOINT.** No path is changed by
both, so merge 2 cannot have overwritten anything merge 1 brought. **This was
established before either merge ran.**

**Agreement with A5's arithmetic: 4+1, then 4, then 3 authored here = 11
additions and 1 modification.** **No disagreement to report on the totals.**

### 5.2 The three scope figures, each with the head it was measured at

    6 additions, 1 modification      MEASURED at commit 3, merge 1
    10 additions, 1 modification     MEASURED at commit 4, merge 2
    11 additions, 1 modification     INTENDED at commit 5, with this report

**The third is INTENDED, not MEASURED: this report is written before the commit
containing it.**

**MEASURED: no status code other than `A` or `M` appears at either merge** — no
delete, rename, copy, type change, unmerged or unknown.

### 5.3 A finding on the arriving-path count

**A5 says "Eight arrive from the two sources — four additions and one
modification from `D-pre-A`, four additions from `D-pre-A2`", and A10 says
"All eight arriving paths".**

**MEASURED: 4 + 1 + 4 = 9 arriving paths.** The count of eight is correct for
arriving **additions** — 4 from `D-pre-A` and 4 from `D-pre-A2` — and the
modification of `derivations/P2-DEFERRED-ITEMS.md` is the ninth arriving path.

**The manifest itself is right:** its `add:` list carries 11 entries of which 3
are authored here, leaving 8 arriving additions, and `modify:` carries 1.
**Twelve paths total, as A5 says.** **The slip is only in the prose gloss, and
it changes no figure.**

**I report all NINE comparisons in §7.2** rather than eight, because dropping
one would have left the only modified arriving path unverified — which is
exactly the path A7 singles out as needing its merge case established first.

---

## 6. Which merge case — A7, established BEFORE any blob comparison

**MEASURED, before either blob comparison was interpreted:**

    merge-base(HEAD, dossier)          ae3604def317667b44ea59458569ba105463fd6b
    merge-base(HEAD, discriminants)    ae3604def317667b44ea59458569ba105463fd6b
    authoritative main tip             ae3604def317667b44ea59458569ba105463fd6b
    commits on main after the base     0

**Both merge-bases ARE `main`.** **No commit exists on `main` after the base**,
so no commit on `main` could have touched any arriving path.

**THE CASE IS ONE-SIDED, for every arriving path, in both merges.**

**Therefore a merged blob equal to the source side is the CORRECT outcome**,
and is not evidence that a side was lost. **In a two-sided merge the same
measurement would mean the opposite**, and Amendment `P(b)`'s line-survival
measurement would have been required instead of blob equality. **It is not
required here, and I did not substitute one for the other.**

### 6.1 `derivations/P2-DEFERRED-ITEMS.md` specifically

**MEASURED: it is modified by `D-pre-A` and by nothing else.**

    changed by 27fabe17 (D-pre-A)      1 path
    changed by 4749961a (D-pre-A2)     0 paths
    changed by main after the base     0 paths

**So the merged blob equals the `D-pre-A` side, and that is correct.** **A7
exists so this is stated rather than assumed**: the one file with a
modification rather than an addition is the one where an unexamined blob
equality would have been indistinguishable from a lost side.

**MEASURED: merged blob `c347e8db793d…` equals the `D-pre-A` side.**

---

## 7. Append-only, and the arriving artifacts — A8, A10

### 7.1 The deferred register, both measures — A8

**MEASURED, base to commit 4:**

    deleted lines                                             0
    base bytes                                             8403
    head bytes                                            11442

    BYTE PREFIX  — after.startswith(before)                True
    in-order subsequence — the weaker property             True    194 of 194

**The byte prefix is the property `check_p3` actually enforces.** I read the
implementation rather than assuming: `check_p3` computes
`after.startswith(before)`. **A subsequence check would pass content inserted
mid-file that `P3` rejects**, so the two are not interchangeable and A8 is
right to demand the stronger one. **Both are reported; the stronger one is the
operative one.**

**MEASURED: four entries, and the first three byte-identical:**

    ## `DEFERRED-01`      1798 bytes    identical to base
    ## `DEFERRED-02`      2788 bytes    identical to base
    ## `DEFERRED-03`      1463 bytes    identical to base
    ## `DEFERRED-04`      new

### 7.2 The nine arriving paths, blob-identical to their contributing source — A10

**MEASURED, each against the source that contributes it:**

    from D-pre-A  27fabe17
      derivations/P2-DEFERRED-ITEMS.md                              c347e8db793d   IDENTICAL
      derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md 0b227206f356 IDENTICAL
      reports/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md    2c1a5f44cc3a   IDENTICAL
      reviews/chatgpt/2026-08-15T0353Z_dpre-a-…-dossier.md           5cb8cc303915   IDENTICAL
      specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md      056aa2d3b134   IDENTICAL

    from D-pre-A2  4749961a
      derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md fb2f51479bf0   IDENTICAL
      reports/2026-08-15T1343Z_dpre-a2-selection-discriminants.md    6af5c5a3244c   IDENTICAL
      reviews/chatgpt/2026-08-15T1343Z_dpre-a2-…-discriminants.md    af5f0b41fc4b   IDENTICAL
      specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md      210e2b55d539   IDENTICAL

**Nine of nine identical. Nothing arriving by merge was edited**, and in the
one-sided case that is what correctness looks like.

**The dossier is correct as written and was not changed** — the loose claim
that prompted an earlier objection was in the `D-pre-A` execution summary, not
in the artifact.

---

## 8. The citations now resolve — A9

**This is the reason the two merges are one task.**

**MEASURED: the arriving discriminants artifact cites the dossier branch SHA
TWICE:**

    line 10    27fabe17c2e56d62df4b686b57e6a654a8983520
    line 21    27fabe17

**MEASURED at commit 4:**

    git merge-base --is-ancestor 27fabe17… HEAD          exit 0
    the cited dossier artifact present at the head        YES

**Exit 0 — the cited commit is in the ancestry**, where before the merges it
was an ancestor of neither `main` nor the discriminants branch (§2, both exit
1).

**Had `D-pre-A2` landed alone, `main` would carry an artifact whose two
load-bearing citations resolve to a branch that is not there.** **That is the
shape the debt register already carries** — an identifier cited on `main` whose
authoritative source is absent from `main`. **This line found that failure;
the merge order is why it did not repeat it.**

---

## 9. Protected paths and gate invariants — A11, A12

**A11, MEASURED path by path, base to commit 4:**

    paths at the evidence base                          408
    excluded (derivations/P2-DEFERRED-ITEMS.md)           1
    compared                                            407
    blob-identical                                      407
    differing                                             0
    missing at head                                       0

**The named ones, MEASURED individually:**

    GATES.md                                   2b3bd5069414   IDENTICAL
    CONVENTIONS.md                             8badc51f38d8   IDENTICAL
    derivations/P2-LATTICE-ONTOLOGY-01.md      6544fb1a72ef   IDENTICAL
    docs/GOVERNANCE-DEBT.md                    b77e961d49c2   IDENTICAL

    everything under scripts/, tests/, results/:   0 paths changed

**The ontology was consumed and not reopened. `GATES.md` was modified for no
reason, because it was not modified at all.**

**A12, all four invariants, MEASURED at commit 4:**

    1.  ^## P2- count                14
    2.  P2-PHASE-01                  Status: PROPOSED
    3.  first prerequisite           Prerequisite state: SATISFIED
    4.  second prerequisite          Prerequisite state: SATISFIED

    both pins match their targets:
      line 1017   derivations/P2-PHASE-01_microscopic_parameter_domain.md   MATCH
      line 1040   derivations/P2-PHASE-01_input_admissibility_contract.md   MATCH

**MEASURED: neither pin names `derivations/P2-DEFERRED-ITEMS.md`.** **That file
is modified by this range and is pinned by no gate, so no re-pin is owed under
Rule 19** — verified through the committed pin collector rather than a
hand-written probe.

**A13, MEASURED before the advance. Six separate exit statuses, all 1 — not
merged:**

    52f65117  exit 1        7146a093  exit 1
    ebd531ab  exit 1        10c260b9  exit 1
    40168469  exit 1        d64cd912  exit 1

---

## 10. Validators and hygiene — A15, A16

**A15, MEASURED, `python -m pytest` from the repository root, exit status 0
both times:**

    before, at the base ae3604de     324 passed, 2 deselected
    after,  at commit 4              324 passed, 2 deselected

**Unchanged, as expected: neither source adds a test.** **No change to
explain.**

**A16, MEASURED on commits 1–4, both merges included. Commit 5 is post-report
evidence.**

    commit 1   ec4efef7   spec: integrate D-pre-A and D-pre-A2 together, and land them
               trailer hits 0      not amended
    commit 2   04b94399   review: pre-execution review for the D-pre-A and D-pre-A2 integration
               trailer hits 0      not amended
    commit 3   79773d51   merge: integrate the D-pre-A kinetic-operator dossier
               trailer hits 0      not amended
    commit 4   45d8e0ff   merge: integrate the D-pre-A2 selection discriminants
               trailer hits 0      not amended

**MEASURED over the whole range: a scan for `Co-Authored-By`, `claude.ai/code`,
`Generated with`, `Claude-Session` and `noreply@anthropic` returns nothing.**

**Rule 20 binds this task and was NOT exercised.** No commit was written with a
hygiene violation to repair. **No force-push, no branch deletion, no history
rewrite of any kind occurred.**

---

## 11. Commits

    commit 1   ec4efef775abfa6ba6ff4623f8e74b41c9b0757d   specs/2026-08-15T1534Z_integrate-dpre-a-and-a2.md
    commit 2   04b943994d18e7436c28c622e15e5bc65876a72c   reviews/chatgpt/2026-08-15T1534Z_integrate-dpre-a-and-a2.md
    commit 3   79773d5158efb95993b4dccb9c7fecd8313bb284   --no-ff merge of 27fabe17…  the dossier
    commit 4   45d8e0ff3fc3decaacfb4e664f2ad8bdccb986ff   --no-ff merge of 4749961a…  the discriminants

**Commit 2 precedes both merges**, per Rule 15's timing clause. **The dossier
merged first so the discriminants' citations resolve at every commit from
commit 4 onward** — §8 measures that they do.

**Commit 5's message, INTENDED:**

    report: the dossier and the discriminants land on main

---

## 12. The checker — A14, MEASURED at commit 4

    base   ae3604def317667b44ea59458569ba105463fd6b
    head   45d8e0ff3fc3decaacfb4e664f2ad8bdccb986ff   (commit 4, the second merge)

    run 1 INCLUSIVE   exit 3   TOOL_ERROR   sha256 019c9bf95560ded74ad568906528b667c0b2dfa448504ec82c468dd8b28c8f53
    run 1 EXCLUSIVE   exit 3   TOOL_ERROR   sha256 019c9bf95560ded74ad568906528b667c0b2dfa448504ec82c468dd8b28c8f53
    run 2 INCLUSIVE   exit 0   PASS         sha256 1499e68387bcaa3dc0b6702cc9306c26110e415c02bda91da329cc44bde6e865
    run 2 EXCLUSIVE   exit 0   PASS         sha256 1032404e56aa2e20d52baf85c0f690619157b871bed48c894020868ad0efbe86

**RUN 2 is the stop-governing run and it passes at both prospectivity
readings**, nine of nine:

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 PASS
    P6 PASS   P7 PASS   P8 PASS   P9 PASS

**RUN 1 governs nothing, by the specification's own words.** §12.3 reports what
it did and why, as a finding.

### 12.1 RUN 1 config, verbatim — default subject selection, observational, governs nothing

    {
      "base": "ae3604def317667b44ea59458569ba105463fd6b",
      "head": "45d8e0ff3fc3decaacfb4e664f2ad8bdccb986ff",
      "append_only_paths": ["DECISION_LOG.md", "derivations/P2-DEFERRED-ITEMS.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 12.2 RUN 2 config, verbatim — stop-governing

    {
      "base": "ae3604def317667b44ea59458569ba105463fd6b",
      "head": "45d8e0ff3fc3decaacfb4e664f2ad8bdccb986ff",
      "specification_paths": ["specs/2026-08-15T1534Z_integrate-dpre-a-and-a2.md"],
      "append_only_paths": ["DECISION_LOG.md", "derivations/P2-DEFERRED-ITEMS.md"],
      "authorised_modified_gates": [],
      "prospectivity": {"boundary": "ce86b534fff6febb5291842e4eb60769affd12db", "inclusivity": "INCLUSIVE"},
      "register_path": "docs/BRANCHING_POLICY.md"
    }

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.
**No value in either config is one I chose**; all are fixed by A14. **Neither
the config nor this specification's declarations were adjusted to make RUN 2
pass** — §8 forbids both, and neither was touched after RUN 1's result was
seen.

### 12.3 The RUN 1 subject set, as measured, and why the run does not complete

**A14 predicts RUN 1 will select three specifications and asks for the set it
actually selected. MEASURED: it selects exactly those three**, and they are
named in the tool's own error:

    specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md
    specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md
    specs/2026-08-15T1534Z_integrate-dpre-a-and-a2.md

**RUN 1's complete output, verbatim, both readings identical:**

    {
      "error": "subject specifications declare different 'append_only' values: specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md=['DECISION_LOG.md', 'derivations/P2-DEFERRED-ITEMS.md']; specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md=['DECISION_LOG.md']; specs/2026-08-15T1534Z_integrate-dpre-a-and-a2.md=['DECISION_LOG.md', 'derivations/P2-DEFERRED-ITEMS.md']",
      "overall": "TOOL_ERROR",
      "tool": "task_checker"
    }

**MEASURED, each specification's declaration read from its committed bytes, and
checked against what its own task actually did:**

    D-pre-A     declares DECISION_LOG.md + P2-DEFERRED-ITEMS.md
                and it DID modify P2-DEFERRED-ITEMS.md        — correct
    D-pre-A2    declares DECISION_LOG.md only
                and it did NOT modify P2-DEFERRED-ITEMS.md    — correct
    this task   declares DECISION_LOG.md + P2-DEFERRED-ITEMS.md
                and it DOES carry that modification in by merge — correct

**All three declarations are correct for their own tasks. None is a mistake.**

**The mechanism refuses to reconcile them, and that is what it was built to
do.** `_declarations_from_specs` raises rather than choosing when two subject
specifications declare different values for the same key — because silently
picking one would reproduce the defect the `C-b` work removed, a subject set
supplied by something no reviewer sees.

**This is not a STOP.** A14 makes RUN 2 stop-governing and says of RUN 1 in the
same breath that it is observational and **governs nothing**. RUN 2 names one
specification, has one declaration to read, and passes.

### 12.4 What the RUN 1 result establishes, stated narrowly

**It is a limitation of the declaration mechanism, newly surfaced, and it is a
`C3` residual not in the debt register.**

**The mechanism has no rule for a range containing several specifications whose
declarations legitimately differ.** Every multi-source integration will have
this shape whenever its sources touch different append-only paths — which is
the normal case, not a pathological one. **The default subject selection is
therefore unusable on multi-source integrations**, and the stop-governing run
is unaffected only because it names its subject explicitly.

**IDENTIFIED, NOT REGISTERED.** §4 forbids adding a register entry, and none is
added. **This is reported for whoever holds the register.** **It is not a
defect in any of the three specifications, and no specification needs
changing.**

### 12.5 `declared_source`, and `P3` on each of the two declared paths

**MEASURED in RUN 2, identical at both prospectivity readings:**

    P3   PASS   declared_source: specification
         declared: ['DECISION_LOG.md', 'derivations/P2-DEFERRED-ITEMS.md']

    P7   PASS   declared_source: specification   declared: []

**`P3`'s result for EACH declared path, and why they differ:**

    DECISION_LOG.md                    PASS   deleted 0   prefix True    89541 → 89541 bytes
    derivations/P2-DEFERRED-ITEMS.md   PASS   deleted 0   prefix True     8403 → 11442 bytes

**They differ in what was tested, not in what was concluded.**
`DECISION_LOG.md` is **not modified by this range** — its byte count is
identical either side, so the prefix test is satisfied trivially and the check
confirms an absence of change. `derivations/P2-DEFERRED-ITEMS.md` **is
modified**, by `D-pre-A` and carried here by merge; it grew by 3039 bytes with
zero deletions and the base preserved as a byte prefix, so the check confirms a
genuine append.

**A declared path that nothing touched and a declared path that grew both
return `PASS`, and only one of them exercised the property.** **That is worth
stating**, because a reader counting two `PASS` results might take both as
evidence of a verified append.

**MEASURED: `DECLARATION_CONFLICT` appears nowhere in either RUN 2 output.**
The config supplied the same two paths this specification's scope block
declares, so the precedence rule resolved to `specification` with nothing to
conflict.

**`P7` reports fourteen sections. `PASS` at zero would have been a STOP.**

### 12.6 RUN 2 output, verbatim, INCLUSIVE reading

    {
      "base": "ae3604def317667b44ea59458569ba105463fd6b",
      "commits_in_range": 12,
      "commits_on_first_parent_line": 4,
      "head": "45d8e0ff3fc3decaacfb4e664f2ad8bdccb986ff",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "append_only": [
                "DECISION_LOG.md",
                "derivations/P2-DEFERRED-ITEMS.md"
              ],
              "authorised_gates": [],
              "counted": 12,
              "counted_add": 11,
              "counted_modify": 1,
              "counted_set": [
                "derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md",
                "derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md",
                "reports/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md",
                "reports/2026-08-15T1343Z_dpre-a2-selection-discriminants.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-dpre-a-and-a2.md",
                "reviews/chatgpt/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md",
                "reviews/chatgpt/2026-08-15T1343Z_dpre-a2-selection-discriminants.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-dpre-a-and-a2.md",
                "specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md",
                "specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-dpre-a-and-a2.md",
                "derivations/P2-DEFERRED-ITEMS.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-15T1534Z_integrate-dpre-a-and-a2.md",
              "stated": 12,
              "stated_add": 11,
              "stated_modify": 1,
              "stated_record": "stated: 11 additions, 1 modification"
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
                "commit": "ec4efef775abfa6ba6ff4623f8e74b41c9b0757d",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "04b943994d18e7436c28c622e15e5bc65876a72c",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "79773d5158efb95993b4dccb9c7fecd8313bb284",
                "work_paths": [
                  "derivations/P2-DEFERRED-ITEMS.md",
                  "derivations/P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md"
                ]
              },
              {
                "adds_review": true,
                "commit": "45d8e0ff3fc3decaacfb4e664f2ad8bdccb986ff",
                "work_paths": [
                  "derivations/P2-LATTICE-MICROSPEC-01_selection-discriminants.md"
                ]
              }
            ],
            "first_review_commit": "04b943994d18e7436c28c622e15e5bc65876a72c",
            "first_work_commit": "79773d5158efb95993b4dccb9c7fecd8313bb284",
            "in_scope": 4,
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
              "DECISION_LOG.md",
              "derivations/P2-DEFERRED-ITEMS.md"
            ],
            "declared_by_specification": [
              "DECISION_LOG.md",
              "derivations/P2-DEFERRED-ITEMS.md"
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
              },
              {
                "base_bytes": 8403,
                "base_is_byte_prefix_of_head": true,
                "commits_with_deletions": [],
                "deleted_lines_base_to_head": 0,
                "head_bytes": 11442,
                "path": "derivations/P2-DEFERRED-ITEMS.md",
                "status": "PASS"
              }
            ],
            "specification_paths_read": [
              "specs/2026-08-15T1534Z_integrate-dpre-a-and-a2.md"
            ],
            "supplied_by_config": [
              "DECISION_LOG.md",
              "derivations/P2-DEFERRED-ITEMS.md"
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
          "evidence": [
            {
              "compared_to_recorded": "UNAVAILABLE",
              "merge": "79773d5158efb95993b4dccb9c7fecd8313bb284",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "ae3604def317667b44ea59458569ba105463fd6b",
              "recomputed_parent_1": "04b943994d18e7436c28c622e15e5bc65876a72c",
              "recomputed_parent_2": "27fabe17c2e56d62df4b686b57e6a654a8983520",
              "status": "PASS"
            },
            {
              "compared_to_recorded": "UNAVAILABLE",
              "merge": "45d8e0ff3fc3decaacfb4e664f2ad8bdccb986ff",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "ae3604def317667b44ea59458569ba105463fd6b",
              "recomputed_parent_1": "79773d5158efb95993b4dccb9c7fecd8313bb284",
              "recomputed_parent_2": "4749961a486c796f560bef94160c1e397d3e8a90",
              "status": "PASS"
            }
          ],
          "id": "P5",
          "status": "PASS",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "ec4efef775abfa6ba6ff4623f8e74b41c9b0757d",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "04b943994d18e7436c28c622e15e5bc65876a72c",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "51e3035b177b7dae3c9f5fd567bb576a0f19c39f",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "eb6ac5c49231f968b59c980349c4a668455be3b1",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "d133a813f3897fbbe8e56867400699f62fe4449a",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "27fabe17c2e56d62df4b686b57e6a654a8983520",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "79773d5158efb95993b4dccb9c7fecd8313bb284",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "8979e83c59663bfd8adac86c7e20dfcb97ac29b2",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "a90da0410b2bd6151e7e3afc2bb7d68b981541aa",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "2dee195b74887e2d49207d6b8c6df4639450bb26",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "4749961a486c796f560bef94160c1e397d3e8a90",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "45d8e0ff3fc3decaacfb4e664f2ad8bdccb986ff",
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
              "specs/2026-08-15T1534Z_integrate-dpre-a-and-a2.md"
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
            "first_commit": "ec4efef775abfa6ba6ff4623f8e74b41c9b0757d",
            "first_commit_paths": [
              "specs/2026-08-15T1534Z_integrate-dpre-a-and-a2.md"
            ],
            "reports_added": [
              "reports/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md",
              "reports/2026-08-15T1343Z_dpre-a2-selection-discriminants.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-15T1534Z_integrate-dpre-a-and-a2.md",
              "reviews/chatgpt/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md",
              "reviews/chatgpt/2026-08-15T1343Z_dpre-a2-selection-discriminants.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-15T1534Z_integrate-dpre-a-and-a2.md",
              "specs/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md",
              "specs/2026-08-15T1343Z_dpre-a2-selection-discriminants.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": [
            {
              "heading_present": true,
              "path": "reports/2026-08-15T0353Z_dpre-a-kinetic-operator-dossier.md",
              "status": "PASS"
            },
            {
              "heading_present": true,
              "path": "reports/2026-08-15T1343Z_dpre-a2-selection-discriminants.md",
              "status": "PASS"
            }
          ],
          "id": "P9",
          "status": "PASS",
          "title": "reports carry a Stops and clarifications section"
        }
      ],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 4,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

---

## 13. Did landing these make me want to select an operator or rule on a question?

**Asked by §9, and the answer is yes to one and no to the other.**

**On selecting an operator: no, and the reason is that the dossier makes the
absence of grounds vivid rather than frustrating.** Three uniform `NOT
ESTABLISHED` results across reflection positivity, the species-to-`N` mapping,
and ten of sixteen compatibility cells are not a near-miss. **There was nothing
to be tempted by**, and I record that plainly because the honest answer to a
temptation question is sometimes that the temptation did not arise.

**On ruling a question: yes, on question two, and it was the same pull the
`D-pre-A2` report disclosed — stronger here.** Landing the two artifacts
together puts §7.4's derivation and §3's plaquette finding on `main` in one
step, and the combined picture reads as though Case B is simply the correct
reading of the ontology: line 115 does not need finite range, the overlap is
exponentially localised, and the ontology is silent. **Three facts pointing the
same way feel like a conclusion.**

**They are not one.** Silence is not permission — Case B is the absence of a
requirement, not a commitment that infinite range is admissible — and §183's
physically-real-substrate claim is an argument for finite range that has
nothing to do with line 115. **I did not rule it, and the merge messages do not
rule it.**

**A third pull was specific to this task and worth naming because it is
structural.** The plaquette finding of §3 arrives with a measured value that
coincides exactly with the Clifford commutator's, on the same six planes. **A
coincidence that exact invites the conclusion that the two are the same
structure**, which would resolve the provenance question in one direction — or,
read the other way, that a coincidence so exact must be significant, which
resolves it in the other. **Coincidence of value is not identity of structure**,
and neither direction is established. **I weighed it in neither.**

**I confirm I selected no operator, ranked, recommended and preferred no
candidate, ruled on neither ontology question, and weighed the plaquette flux
in neither direction.** **I added no register entry**, modified no arriving
file, and changed no gate state.

---

## 14. Rule 16 assessment — what the assembled set does NOT establish

**Rule 16 is operative. All four junctions the specification names are
addressed.**

### 14.1 First junction — a dossier on `main` is not an operator nearly chosen

**After this lands, `main` carries a candidate dossier and a discriminant
analysis.** **A reader may take that for the operator being nearly chosen. It
is not.**

**MEASURED, and this is the load-bearing sentence: no candidate is eliminated
on grounds the programme has already committed to.** Question one's elimination
of staggered holds only under Reading A, and it is an elimination of a
**presentation** — whether another convention passes Reading A is `NOT
ESTABLISHED`. Question two's elimination of overlap holds only under Case A,
which requires adopting a new ontology commitment.

**Under Reading B and Case B — the readings that require no new commitment —
ALL FOUR candidates survive.** naive, Wilson, staggered and overlap. **That is
the state of the evidence on `main` after this lands.**

**`C-iii` is not unblocked and `D0` is not unblocked.** A dossier and a
discriminant test are neither a freeze nor an Euclidean–spectral equivalence.

### 14.2 Second junction — what Case A would cost, and what it would not buy

**Question two's elimination would cost a new physical commitment about the
substrate.**

**MEASURED, from the landed discriminants artifact: ontology line 115 does not
require finite range.** Its mechanism needs a convergent derivative expansion,
which analyticity supplies and exponential localisation implies; finite range
is sufficient and strictly stronger than necessary.

**So adopting Case A would protect a claim the ontology has not made** — that a
physically real substrate must have couplings of bounded range — **rather than
repairing a gap in a claim it has made.**

**That is what makes Case A a decision rather than a correction.** A correction
restores something the frozen text already needed; **Case A adds something it
never asked for**, and the addition is what does the eliminating.

### 14.3 Third junction — the plaquette flux, in the specification's own words

**The staggered formulation carries a uniform, redefinition-invariant plaquette
phase `P_μν = −1`. Whether this is a staggered-specific microscopic structure,
or the spin-diagonalised representation of the Clifford anticommutation
structure already present in the other formulations, is NOT ESTABLISHED. This
task does not weigh it.**

**IDENTIFIED, PROVENANCE NOT ESTABLISHED, NOT REGISTERED, NOT WEIGHED.**

**It is NOT reported as a physical difference between candidates.** The Clifford
group commutator `γ_μ γ_ν γ_μ⁻¹ γ_ν⁻¹` carries the same value `−1` on the same
six planes, and **spin diagonalisation is precisely the step that moves the
Dirac structure into site and link phases** — so the staggered flux may be that
same anticommutation structure written in different variables. **Coincidence of
value is not identity of structure, and the identity has not been shown either
way.**

**Nothing in this report should read as a finding for or against staggered, in
either direction.** The flux does not threaten isotropy — a value equal on all
six planes is invariant under axis permutation — and the structure that is not
manifestly symmetric, the single-link sign pattern, is exactly the one a
redefinition removes. **This integration carries the question to `main`, not an
answer to it.**

### 14.4 Fourth junction — the cheap discriminants are now exhausted

**Both ontology-level discriminants have been tested, and what they yield is
contingent on rulings not yet made.** **No third cheap discriminant was
manufactured**, and none is proposed here.

**What remains is reflection positivity**, `NOT ESTABLISHED` for all four
candidates, **which needs a transfer matrix that does not exist.** That
construction **overlaps `D-pre-B`'s Euclidean–spectral equivalence**, which
also needs transfer-matrix normalisation.

**Whether the two should be scoped together is the open question**, and it is
worth the PI's consideration precisely because they share their principal
construction and neither can be attempted cheaply.

**This task does not scope them, and begins neither construction.** **Naming
the overlap is not scoping it.**

---

## 15. Stops and clarifications

**No stop occurred in this execution.** **One stop occurred before it**, on the
first review artifact, and §3.1 records it.

    SPECIFICATION_DEFECT                          0 stops, 1 finding
    ENVIRONMENT                                   0 stops, 0 findings
    OBSERVATION_METHOD_ERROR                      0 stops, 0 findings
    REPOSITORY_DEFECT                             0 stops, 0 findings
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY   1 stop,  1 finding

### 15.1 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the stop, and one finding

**THE STOP: the first review artifact carried no specification digest at all.**
§3.1 gives the measurement — zero occurrences of `reviewed specification`,
`SHA-256`, `digest`, and zero 64-hex strings anywhere in the file. **`A2` could
not be satisfied**, and the task stopped before creating a branch or any
commit.

**Primary category is `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` rather than
`SPECIFICATION_DEFECT`**, because the specification was not defective and the
repository was not defective: what could not be resolved from the evidence was
whether the review was bound to those specification bytes.

**The corrected review binds correctly and execution proceeded.** **Recorded as
`G-05`'s first live instance since the register landed**, and no register entry
is added.

**THE FINDING: `RUN 1`'s multi-subject declaration failure**, §12.3 and §12.4.
**The declaration mechanism has no rule for a range whose specifications
legitimately declare different append-only sets**, which every multi-source
integration will exhibit. **A `C3` residual, identified and not registered.**

### 15.2 `SPECIFICATION_DEFECT` — one finding, not a stop

**A5's gloss says "Eight arrive from the two sources" and A10 says "All eight
arriving paths"; the correct count of arriving paths is NINE.** §5.3 gives the
measurement: eight arriving **additions** plus one arriving **modification**.

**Not a stop.** The manifest itself is correct — twelve paths, eleven additions
and one modification — and the slip is in the prose gloss only. **I reported
all nine comparisons rather than eight**, because the omitted one would have
been `derivations/P2-DEFERRED-ITEMS.md`, the single modified arriving path and
the one A7 singles out as needing its merge case established before its blob
equality means anything.

### 15.3 `ENVIRONMENT`, `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT` — nothing to report

**No environment failure occurred.** **Rule 13 carries two diagnostic orders, a
known open item. Neither was exercised**, and I am not naming one as having
applied. **Nothing was installed.** Python 3.11.15 and pytest 9.1.1, as
present.

**No probe of mine contradicted a committed check in this task.** Where the
checker returned `TOOL_ERROR` I read its message and the implementation rather
than assuming the tool was wrong — **and the tool was right.**

**No defect in the repository was found by this task.**

### 15.4 What I would have specified differently

**A14 predicts "RUN 1 will select three specifications" and asks for the set it
actually selected.** It does not anticipate that selecting three would make the
run fail. **The prediction was right about the selection and silent about the
consequence**, and a task with a narrower report contract might have recorded
"three, as predicted" and not noticed that no properties were evaluated.

**I would have had A14 ask what RUN 1 RETURNED, not only what it selected.**
The distinction cost nothing here because RUN 2 governs, **but the mechanism
limitation of §12.4 is only visible in the return value**, and it is the most
substantive governance finding this task produced.

**Nothing in the specification was unsatisfiable.** The one criterion whose
arithmetic slipped, A10's eight, was unambiguous about what to compare and I
compared all of it.

---

## 16. Evidence layering

**Committed in this report, MEASURED at commit 4:** A1–A13, A15 and A16 for
commits 1–4; A14's four invocations with both configs and the outputs; commits
1–4 SHAs and their stored messages.

**Committed in this report, INTENDED:** commit 5's message; A5's final
base-to-commit-5 scope of 11 additions and 1 modification.

**Post-report evidence, returned to the Reviewer and NOT written back:** A5's
final scope measured base-to-commit-5; A14-final, being RUN 2 re-run at commit
5 before the landing; A12 and A13 re-run after the advance; A16 for commit 5;
the pre-advance `--is-ancestor` exit status; the exact push command; remote
`main` read back; both source tips unchanged; final ancestry confirmation.

**Nothing in this report claims to measure commit 5.**
