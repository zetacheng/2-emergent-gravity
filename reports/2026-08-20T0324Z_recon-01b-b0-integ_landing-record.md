# Landing record — `P2-RECON-01B-B0-INTEG`

**Transport only.** Every statement below is one the reviewed result already
made. **Nothing here is a new classification, and no component is
reclassified.**

    Source   science/recon-01b-b0-scope   1093fc04c85e54c3b9fc0dbcca1a2ebc98c69e23
    Base     a6be149f531c4a55ad331f26412a16472b803628
    Fork     968e726a5a4322eecf4254ff69b25832f263c155

**Discharges `O-3` of `P2-PROJ-01-INTEG`.**

---

## 1. The inventory, transported

`derivations/P2-RECON-01B-B0_scope-assessment.md:32-43`, measured at
`968e726a`:

    #   component                                              state
    1   metric-coupled 1-form operator Δ⁽¹⁾[g,h] on a
        weak-field background, exact geometric factors         IMPLEMENTATION + SPECIFICATION
    2   compensating scalar Δ⁽⁰⁾[g,h]                          IMPLEMENTATION + SPECIFICATION
    3   Γ_k = ½ logdet Δ⁽¹⁾ − (k/2) logdet Δ⁽⁰⁾ at the
        determinant level                                      SPECIFICATION ONLY
    4   numerical h-derivatives at determinant/eigenvalue
        level, with Richardson check                           IMPLEMENTATION + SPECIFICATION
    5   fixed axis-TT projection, identical for every k,
        pre-registered                                         SPECIFICATION ONLY
    6   the k-scan driver over k ∈ {0,1,2,3,½}                  SPECIFICATION ONLY
    7   flat-limit validation against the Proca eigenstructure  IMPLEMENTATION + SPECIFICATION
    8   blind two-stage harness: frozen output, external
        digest, deferred comparison                            IMPLEMENTATION + SPECIFICATION
    9   ratio-error tolerance rule, numerator and
        denominator correlated                                 SPECIFICATION ONLY
    10  registered regression anchors for the reconstruction
        itself                                                 NEITHER

### 1.1 Totals, and the arithmetic checked against the lists

    N_both      5      components 1, 2, 4, 7, 8
    N_impl      0
    N_spec      4      components 3, 5, 6, 9
    N_neither   1      component 10
               --
    N_total    10      5 + 0 + 4 + 1 = 10

**Checked here against the per-state lists, not asserted.** The `N_both` list
names five components and `N_both` is 5; the `N_spec` list names four and
`N_spec` is 4; the `N_neither` list names one and `N_neither` is 1; `N_impl` is
0 and no component is listed for it. The four lists are disjoint, their union
is `{1,…,10}` with each number appearing exactly once, and the table has ten
rows. **`5 + 0 + 4 + 1 = 10`.**

### 1.2 Comparison against the prior assessment, as the reviewed result makes it

Prior assessment: `derivations/P2-BETAV-RECON-01_scope-assessment.md`, evidence
base `ece34f7bacbbee00efa0fecf0be644d593eed72f`, table at `:473-484`, totals at
`:486-491`.

    #    prior state                    state at 968e726a               differs
    1    SPECIFICATION ONLY             IMPLEMENTATION + SPECIFICATION   YES
    2    SPECIFICATION ONLY             IMPLEMENTATION + SPECIFICATION   YES
    3    SPECIFICATION ONLY             SPECIFICATION ONLY               no
    4    SPECIFICATION ONLY             IMPLEMENTATION + SPECIFICATION   YES
    5    SPECIFICATION ONLY             SPECIFICATION ONLY               no
    6    SPECIFICATION ONLY             SPECIFICATION ONLY               no
    7    IMPLEMENTATION + SPECIFICATION IMPLEMENTATION + SPECIFICATION   no
    8    IMPLEMENTATION + SPECIFICATION IMPLEMENTATION + SPECIFICATION   no
    9    SPECIFICATION ONLY             SPECIFICATION ONLY               no
    10   NEITHER                        NEITHER                          no

    totals        prior                     968e726a
    N_both          2   (7, 8)                5   (1, 2, 4, 7, 8)
    N_impl          0                         0
    N_spec          7   (1,2,3,4,5,6,9)       4   (3, 5, 6, 9)
    N_neither       1   (10)                  1   (10)
                   --                        --
    N_total        10                        10

**Both columns check against their own lists:** `2 + 0 + 7 + 1 = 10` and
`5 + 0 + 4 + 1 = 10`.

**The stated cause, as the reviewed result measures it.** Three components
differ and **one event accounts for all three**: `scripts/recon2026/` did not
exist at the prior base — `git ls-tree -r --name-only ece34f7b scripts/ |
grep -c 'recon2026'` returns `0`, and the prior assessment's text contains `0`
occurrences of `recon2026`. `P2-BETAV-RECON-01a` landed the clean-room
construction between the two bases, so components 1, 2 and 4 moved to
`IMPLEMENTATION + SPECIFICATION` **because an applicable implementation came
into existence, not because the applicability test was applied differently.**

**The reviewed result records that the prior classification was correct when it
was made**, at its `:248`, and this landing does not say otherwise.

**One refinement that is NOT a state difference**, transported because the
reviewed result records it so it will not be mistaken for one: component 6 is a
fourth instance of "code exists and is not applicable", which the prior
assessment did not list as one. **Both readings reach `SPECIFICATION ONLY` for
component 6**, and the blob is unchanged —
`f3d8fa25d233871c4cd3de8c7acc3343bdc7bf9f` at both bases.

---

## 2. The component-3 reading, both branches

**The reviewed result records this as open and answers it one way. Both
branches are transported; neither is settled here.**

**THE READING ADOPTED BY THE REVIEWED RESULT — `SPECIFICATION ONLY`**, at
`derivations/P2-RECON-01B-B0_scope-assessment.md:90`:

> **Component 3 — `SPECIFICATION ONLY`.**
> **The determinant primitive exists and the combination does not.**

with its ground: `scripts/recon2026/proca_curved.py:356` supplies
`logdet_operator(matrix)`, **but `Γ_k` is the `k`-weighted combination
`½ logdet Δ⁽¹⁾ − (k/2) logdet Δ⁽⁰⁾`, and no code forms it.** *"A primitive is
not the component. The component is the assembly, and the assembly is specified
and unbuilt."*

**THE ALTERNATIVE READING, as the reviewed result states it** at its `:498-504`:

> **Whether "an implementation exists" for a component
> should be judged on the assembly or on its primitives is a classification
> question this assessment answered one way** — on the assembly, since that is
> what the component names — **and a different reader could answer it the other
> way and reach `IMPLEMENTATION + SPECIFICATION`.** The evidence for both
> readings is at `§1.2`.

**The alternative reading would move component 3 from `SPECIFICATION ONLY` to
`IMPLEMENTATION + SPECIFICATION`**, and with it `N_both` from 5 to 6 and
`N_spec` from 4 to 3. **That inventory is NOT adopted here and is recorded only
as what the other reading yields.**

**This integration transports the ambiguity and does not resolve it.**

---

## 3. What the landing changes, and what it does not

**IT CHANGES which assessment is `main`'s component baseline.** Before this
landing the baseline was `derivations/P2-BETAV-RECON-01_scope-assessment.md`;
after it, `derivations/P2-RECON-01B-B0_scope-assessment.md` is present on `main`
and is the current one. **A completed result is no longer reachable only from a
branch.**

**IT DOES NOT CHANGE any determination made against the older baseline.**
`P2-RECON-PROJ-01`'s component findings were made while `main` carried the
earlier assessment. Whether they are affected is `O-1`, not this task.

**MEASURED, and recorded because it is the natural first question:**
`P2-RECON-PROJ-01` classified components 5 and 9 as `SPECIFICATION ONLY`, and
the newly landed assessment classifies both the same way — `:117` and `:174`.
`P2-RECON-PROJ-01:527-530` **said so in advance**, recording that the unlanded
re-measurement "also classified components 5 and 9 as `SPECIFICATION ONLY`, so
the comparison is unaffected; the fact is recorded so the baseline is not
mistaken." **That observation is now a fact about `main` rather than about a
branch. Nothing follows from it here** — whether any consequence attaches is
`O-1`.

**NO GATE MOVES. `P2-PHASE-01` is unchanged.**

---

## 4. The delay, recorded

**The result was executed, reviewed and independently verified, and then was
not integrated.** Measured at execution: **seven task specifications landed on
`main` between the source's fork point `968e726a` and this task's base
`a6be149f`** while `1093fc04` was not an ancestor of `main`. Counting task
specifications on branches that never landed adds two more, `gov-housekeep-01`
and `gapa-bridge-01`, for **nine tasks executed** in the interval.

**The omission was the Researcher's**, who verified the result and did not
follow it with an integration specification.

**Recorded once, as fact.**

---

## 5. The obligation record

**Per `M4`: no register's stated scope admits it.** The scopes read, on the
merge product:

    derivations/P2-DEFERRED-ITEMS.md
        ":12-17" — work "CONSIDERED and consciously postponed", each entry
        carrying "the PI's position at the time of deferral"; ":191" —
        "Entries are added by PI decision."
        EXCLUDED by who may write: this task is not a PI decision and holds
        no PI position to record.

    derivations/P2-PHASE-01_C-CHECK_OPEN-ITEMS.md
        ":3-5" — "open items arising from the C-check line", the follow-up
        checks C1, C2 and C3.
        EXCLUDED by subject: O-1 does not arise from that line.

    docs/GOVERNANCE-DEBT.md
        ":1-6" — the governance-side register, recording "what the rules,
        amendments and task reports already carry".
        EXCLUDED by kind: O-1 is a readiness question about component states,
        not a gap in a rule or mechanism.

**The record, which therefore lands here and nowhere else:**

> **`O-1` — the register consequences of the newly landed baseline are
> undecided.** `main`'s component baseline is now
> `derivations/P2-RECON-01B-B0_scope-assessment.md`. What, if anything, a
> readiness register should record from that, and whether any determination
> made against the earlier baseline is affected, is not decided by this
> integration and would be a classification it may not add.

**The executor did not create a register and did not place the record by
convenience.**

**This does not add a fourth homeless obligation.** Its content is `O-1`, which
was already homeless after `P2-PROJ-01-INTEG`. **What changed is its ground:**
`O-1` was "consequences of `PROJ-01`'s component determinations" and is now
also "consequences of the newly landed baseline". **The count of obligations
with no admissible home stays at three; one of them now has two occasions
behind it.**

---

## 6. `science/gapa-bridge-01` is not integrated here

Its result carries a scope condition — the identification holds for `q` along
one axis and fails by `O(1)` elsewhere — which its integration must land as a
constraint on how the result may be cited. **Bundling it into a housekeeping
merge would risk that constraint arriving as an aside.** It remains outstanding
with its own specification owed.

---

## 7. What this landing does not establish

It lands a re-measurement already made, reviewed and verified. **It produces no
new result.** No `β_V`, no `k`-scan, no computation of any kind. No gate moves;
`P2-PHASE-01` unchanged; `H-EXT-01` unchanged; `Q1` unchanged.
