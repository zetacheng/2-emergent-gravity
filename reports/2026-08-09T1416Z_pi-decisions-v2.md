# Execution report — re-issue the PI decisions and deferred-items task on a clean branch

Specification: `specs/2026-08-09T1416Z_pi-decisions-v2.md`
Specification evidence base: `f309f61c9c14b0e2c63e078f9c0d0809422742e7`
Branch: `fix/pi-decisions-v2`, cut from the evidence base
Superseded branch: `fix/pi-decisions-and-deferred` @ `52f651174dc1fef03b4fb9276078fa1f08d94bd7`
Pre-report head: `7dad9093f0453588501a1f5e2bb3212da1dc6e54`

**Outcome.** The approved content is landed on a clean branch. **No
judgement was required** — §5 asks whether this specification told me how
to represent a re-issue clearly enough, and the answer in §12 is yes,
with one small ambiguity that did not affect execution. All seven pins
verify. Every evidence quotation was re-located in the pinned material
rather than inherited. **Both append-only measures hold: zero deleted
lines against the evidence base and zero against every commit's parent.**
The superseded branch is untouched. Four validators pass.

**The only differences from the approved content are seven
task-identity pointers**, enumerated exactly in §5. Every other byte of
the three `DECISION_LOG.md` entries and of the register is reproduced
unchanged.

---

## 1. A10 — refs, read from the remote

    refs/remotes/origin/main    f309f61c9c14b0e2c63e078f9c0d0809422742e7
    remote refs/heads/main      f309f61c9c14b0e2c63e078f9c0d0809422742e7
    local  refs/heads/main      0f7961747abe2a18b436c0b1e5b928f425ea4d9a

Both remote refs resolve to the evidence base. **Local `main` is stale by
design and was not repaired.** No `main` ref was moved.

**`fix/pi-decisions-v2` did not exist before this task** — `git ls-remote
origin refs/heads/fix/pi-decisions-v2` returned zero refs — so
"create the new branch from that commit" was executable as written. It
was created from `f309f61c…` in a separate worktree.

**`{HHMM}Z` is `1416`**, fixed by commit 1 and reused. **It differs from
`0430`**, so the two executions are distinguishable by path: the
superseded branch carries `…T0430Z_pi-decisions-and-deferred.md`, this
one carries `…T1416Z_pi-decisions-v2.md`, and no path collides.

## 2. A1 — pinned inputs, seven of them, verified before use

Digests read from the git objects at the evidence base; **all seven
matched.**

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
      fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a   MATCH
    derivations/P2-PHASE-01_channel_character.md
      380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f   MATCH
    derivations/P2-PHASE-01_channel_character_layers.md
      4cea53a7163ccc6aadadd0fca276714c16d805ad8aed3594d64d66d412606711   MATCH
    results/P2-PHASE-01/channel-character-layers/layers.json
      fe343c74389cc996e42567d7dd510f479f1e7ed01cba81de61ff1d6f7e9d1542   MATCH
    reports/2026-08-05_p2-phase-01_scalar-stationary-exploratory.md
      70ab88eda32483420c0bfd522babd2ca4a73941bc2d2d20f8414976641756cbe   MATCH
    results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json
      a4537efad3b46e5e429b5310baad8b4dbf36d9c95582873dbfa0b03cc44d7028   MATCH
    derivations/P2-PHASE-01_scalar_stationary_exploratory.md
      80586e33ef07e307729af4597f72b48f6ecee74fc6a0f396b593f735ef322599   MATCH

**A1's account of the three-way split is confirmed by observation, not
accepted on assertion.** In the pinned exploratory derivation note,
normalised:

    contains "7.59"          False
    contains "complement"    False        (case-insensitive)

**The note carries no roots, no curvatures and no complement relation.**
It carries the scope limitation, verified as an exact substring in §4.3.
**Restoring it to the pinned set is what makes the "restricted, not
stable" narrowing verifiable from A1 rather than asserted** — which was
the residual gap after the second issue added the other two.

## 3. A3 — content reproduced from the superseded branch

**Method, so the reproduction is auditable.** The approved
`DECISION_LOG.md` at `52f65117…` was confirmed to have the evidence-base
blob as an exact byte prefix; the tail beyond that prefix is the three
approved entries and was extracted programmatically. The register was
taken as the whole approved blob. **Neither was retyped.**

**The landed `DECISION_LOG.md` is the evidence-base blob followed by
those entries**, so the file's earlier 1517 lines are byte-identical by
construction rather than by inspection.

**Differences from `52f65117…`: seven lines, all task-identity
pointers.** §5 gives them line by line. **Zero substantive differences.**

## 4. A2 — evidence re-verified, not inherited

Every quotation below was located afresh in the pinned material at the
evidence base, and separately confirmed present in the landed register.
**None was carried over on the strength of the earlier approval.**

### 4.1 `DEFERRED-01`

**Cited:** `g_V = g_A = -G/2`, no real linear HS field admissible.

**Located** in `derivations/P2-PHASE-01_channel_character_layers.md`
§3.2 — pinned `4cea53a7…`:

    channel                     g_L          g_P        sign(g)   real HS
    scalar_singlet_direct         G/N    2*G/N**2         +1        yes
    induced_V_singlet            -G/2       -G/N          -1        no
    induced_A_singlet            -G/2       -G/N          -1        no

Both `induced_V_singlet` and `induced_A_singlet` rows verified present in
the source and in the register.

**Located** in `results/P2-PHASE-01/channel-character-layers/layers.json`
— pinned `fe343c74…`, read as JSON rather than as text:

    layer_1b.channels.induced_V_singlet.g_in_normalisation_L              "-G/2"
    layer_1b.channels.induced_V_singlet.real_linear_HS_field_admissible   false
    layer_1b.channels.induced_A_singlet.g_in_normalisation_L              "-G/2"
    layer_1b.channels.induced_A_singlet.real_linear_HS_field_admissible   false

**Both values and both flags present in pinned material. No stop.**

### 4.2 `DEFERRED-02` — the numerical findings

**Cited:** exact Wilson complement `I_0(M) = I_0(-8-M)`; positive
restricted curvature below `G_c`.

**Located** in `reports/2026-08-05_p2-phase-01_scalar-stationary-exploratory.md`
— pinned `70ab88ed…`, verified as an exact substring after whitespace
normalisation:

> There is instead an exact Wilson-complement relation
> `I0(Mhat)=I0(-8-Mhat)`, induced by `p_mu -> pi-p_mu`; numerical
> differences for four checked pairs are at most `1.1e-16`. It relates
> algebraic roots but is not an `Mhat -> -Mhat` symmetry. Positive and
> negative roots are therefore not declared phase-equivalent.

**And the three sub-critical rows, each verified as a complete row of
the source table** — the source form checked, not only the register's
re-columned form:

    | 0.80 | -7.589264 | -0.410736 | 0.417872 | -0.022615 | 0.021346 |
    | 0.90 | -7.813202 | -0.186798 | 0.400036 | -0.009564 | 0.009487 |
    | 0.98 | -7.966034 | -0.033966 | 0.404749 | -0.001725 | 0.001743 |

    columns: G/Gc | Mhat_left | Mhat_right | curvature(left) | curvature(right) | curvature(0)

**Positive `curvature(left)` at `G/G_c < 1` is the "positive restricted
curvature below `G_c`" of the cited line**, and `-7.589264` is the
`M̂ ≈ -7.59` of the entry title. The register's three re-columned rows
were each verified to carry the same five numbers.

**Corroborated** in
`results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json`
— pinned `a4537efa…`:

    symmetry.wilson_complement_relation
      "I0(Mhat) = I0(-8 - Mhat), from p_mu -> pi-p_mu; numerically checked below."
    symmetry.complement_pairs
      4 pairs, max |difference| = 1.1102230246251565e-16

### 4.3 `DEFERRED-02` — the scope limitation

**Located** in `derivations/P2-PHASE-01_scalar_stationary_exploratory.md`
— pinned `80586e33…`, verified as an exact substring:

> Neither curvature is a full condensate-space Hessian or a
> phase-admissibility statement.

**This is the pin the second issue dropped**, and it is the sentence that
narrowed Decision 3 from "stable" to positive restricted curvature. With
the note back in A1, the narrowing is now verifiable from the pinned set
rather than resting on an unpinned assertion. **All three halves of
`DEFERRED-02`'s evidence are in pinned material. No stop.**

### 4.4 `DEFERRED-03` — absence of evidence is content

A2 requires that the entry **states `Evidence: none` and supplies no
citation.** Verified in the landed register:

    Status: PI HYPOTHESIS, UNTESTED.     present
    Evidence: none.                       present

**No lookup was attempted and none should be.** Treating this as a
failed evidence check would be the confusion between *not observed* and
*observed negative*.

## 5. Every difference between what I landed and `52f65117…`

**Seven lines. All are task-identity pointers, none is substantive.**
Produced by a unified diff of the approved content against the landed
content:

    DECISION_LOG.md entries — three `### Related branch and files` sections

      -`fix/pi-decisions-and-deferred`;
      +`fix/pi-decisions-v2`;
      -`specs/2026-08-09T0430Z_pi-decisions-and-deferred.md`.
      +`specs/2026-08-09T1416Z_pi-decisions-v2.md`.
                                                    (×3, once per entry)

    derivations/P2-DEFERRED-ITEMS.md — the Authority line

      -Authority: `specs/2026-08-09T0430Z_pi-decisions-and-deferred.md`.
      +Authority: `specs/2026-08-09T1416Z_pi-decisions-v2.md`.

**Why the change was necessary.** Left alone, the landed
`DECISION_LOG.md` would cite a superseded branch as the decisions' origin
and would point at a specification file that **does not exist in this
tree**. The register's `Authority:` line would name a file this branch
does not contain. **Both would be dangling references in the operative
record**, and the `Related branch and files` section exists precisely to
be followed.

**Nothing else was touched.** After substitution, the landed content
contains **zero** occurrences of `pi-decisions-and-deferred` and **zero**
of `0430` — verified by count, so no pointer was missed.

**No ruling text, no reason, no consequence, no evidence quotation, no
status line and no PI position differs by a single character.** The
three rulings remain verbatim as reproduced on the approved branch, and
`52f65117…` remains available for a byte comparison.

## 6. A4 — required phrases, checked against normalised text

Blockquote prefixes `> ` stripped, `**` and backticks stripped, all
whitespace collapsed to single spaces, en dashes left as they are. **The
check was executed here against the landed file, not inherited from the
earlier report.**

    --- entry 1 ---
      PASS count=3  'scalar channel with a real auxiliary field'
      PASS count=1  'This is a choice of direct route'
      PASS count=1  'It is deferred, not excluded'
      PASS count=1  'This does not close OPEN-AC-1'
    --- entry 2 ---
      PASS count=1  'the programme evaluates both the'
      PASS count=1  'rather than selecting between them'
      PASS count=2  'depends on an unresolved sign convention'
    --- entry 3 ---
      PASS count=2  'DEFERRED, not excluded'
      PASS count=1  'they do not establish full condensate-space stability, phase admissibility, or absence of physical content'
      PASS count=1  'cannot by itself classify this branch as an unphysical lattice artifact'
      PASS count=1  "that criterion's quantifier range is undetermined"
    ALL PRESENT: True

**Every required phrase is inside the verbatim ruling text. No ruling
was edited, and none needed to be.** The second occurrence of `depends
on an unresolved sign convention` in entry 2 is in the `### Consequences`
prose, which paraphrases the ruling's diagnostic; the required occurrence
is the one in the ruling itself.

**The en dash was confirmed as `U+2013`** in `Hubbard–Stratonovich` on
both sides of the comparison, so normalisation did not silently convert
it.

**Three top-level `## 2026-08-09` headings exist in the landed file**,
one per decision, none nested.

## 7. A5 — append-only, on both measures

**Measure 1 — evidence base to branch head:**

    git diff --numstat f309f61c… 7dad9093…
      256     0       DECISION_LOG.md
      193     0       derivations/P2-DEFERRED-ITEMS.md
      275     0       specs/2026-08-09T1416Z_pi-decisions-v2.md

    deleted lines across the whole diff:  0

**Measure 2 — each commit against its parent:**

    69fca93   deletions=0    275   0   specs/2026-08-09T1416Z_pi-decisions-v2.md
    7dad909   deletions=0    256   0   DECISION_LOG.md
                             193   0   derivations/P2-DEFERRED-ITEMS.md

**Both are zero.** `DECISION_LOG.md` is written once, by a single commit,
and never revisited — **there is no commit on this branch that removes or
replaces a line another commit on this branch added.** That is the
measure the superseded branch failed, where the parent-to-child diff
carried 364 deleted lines while the base-to-head diff carried none.

**The two measures are reported separately and neither is offered as
evidence for the other.**

## 8. A6 — nothing else touched

Blob and tree hashes read from the git objects, evidence base against
pre-report head:

    GATES.md          bd48205…  IDENTICAL
    CONVENTIONS.md    2d4f735…  IDENTICAL
    AGENTS.md         5e60b5f…  IDENTICAL
    pyproject.toml    9fc6fdd…  IDENTICAL

**Whole subtrees, compared as tree objects** — which covers every file
under each, present or absent, without enumerating:

    scripts/   tree 75f03934e5ff7ae131c64ae94851cb2342596fbf   IDENTICAL
    results/   tree 23fe5e80426a69feaf1f90f78cb187c396e1935a   IDENTICAL
    tests/     tree 422db3fd5170eada01b3393f5cfcf6bdc232372f   IDENTICAL

**Every path under `derivations/` that exists at the evidence base**,
enumerated from the base and compared one by one:

    29 paths checked, 0 differ

and the only change to that directory:

    A   derivations/P2-DEFERRED-ITEMS.md

**All seven pinned artifacts lie inside those identical trees**, so no
pinned or frozen artifact was modified.

**No gate status changed.** `GATES.md` is blob-identical, its `^## P2-`
anchor count is 14 at both ends, `P2-GAP-01` still reads `Status: PASS
(continuum exact; lattice I_0 agrees with paper at matched mass)` and
`P2-PHASE-01` still reads `Status: PROPOSED`.

**The SI-1 cross-reference was NOT added.** `GATES.md` is protected and
that is an agreed separate task; `DEFERRED-02`'s `Blocks:` line still
records the constraint from the register side only.

**Nothing was computed.** No script was run against repository data other
than the governance tools and `pytest`.

## 9. A7 — scope

**Manifest template** (SHA-256
`2a298a524f3b886c1aa58cb34f2012d8e7f186a04b8261448c8decf998cbffec`):

    {
      "base": "f309f61c9c14b0e2c63e078f9c0d0809422742e7",
      "head": "{PUSHED_HEAD}",
      "mode": "exact",
      "required": [
        {"operation": "add", "path": "specs/2026-08-09T1416Z_pi-decisions-v2.md"},
        {"operation": "add", "path": "derivations/P2-DEFERRED-ITEMS.md"},
        {"operation": "add", "path": "reports/2026-08-09T1416Z_pi-decisions-v2.md"},
        {"operation": "modify", "path": "DECISION_LOG.md"}
      ],
      "optional": [],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

**Intended final resolution:** `head` set to the pushed head, all four
records required — **3 additions and 1 modification.** A fifth path would
be a defect. `derivations/P2-DEFERRED-ITEMS.md` does not exist at the
evidence base and is confirmed an `add`.

**Pre-report scope check** at `7dad9093…`, with the report record removed
because the report does not yet exist — checker output verbatim:

    {
      "base": "f309f61c9c14b0e2c63e078f9c0d0809422742e7",
      "failures": [],
      "head": "7dad9093f0453588501a1f5e2bb3212da1dc6e54",
      "mode": "exact",
      "observed_operations": [
        {
          "operation": "modify",
          "path": "DECISION_LOG.md"
        },
        {
          "operation": "add",
          "path": "derivations/P2-DEFERRED-ITEMS.md"
        },
        {
          "operation": "add",
          "path": "specs/2026-08-09T1416Z_pi-decisions-v2.md"
        }
      ],
      "overall": "PASS",
      "tool": "scope_checker"
    }

    exit status 0

**Unlike the second issue, the report path is genuinely absent at the
pre-report head** — this branch has no earlier report occupying it — so
the pre-report check needs no caveat about content at that path.

**The final scope check at the pushed head is post-report evidence** and
is returned to the Reviewer.

## 10. A8 — the superseded branch, verified before the push

Read from the remote:

    refs/heads/fix/pi-decisions-and-deferred   52f651174dc1fef03b4fb9276078fa1f08d94bd7

    git merge-base --is-ancestor 59c763ab… 52f65117…   ->  exit 0
      59c763ab… is reachable as an ancestor of that head

    git ls-remote --heads origin 'refs/heads/fix/pi-decisions*'
      52f651174dc1fef03b4fb9276078fa1f08d94bd7  refs/heads/fix/pi-decisions-and-deferred

**One branch, not two.** The first execution is an ancestor commit on the
superseded branch, not a separate ref. **Nothing on it was touched,
reset, rewritten or force-pushed**, and no branch was deleted. **The
post-push re-verification is post-report evidence.**

## 11. A9-pre — validators at the pre-report head

Run individually with `python -m pytest <path>`, that exact invocation,
since `pytest` on this host resolves to 9.0.2 while `python -m pytest`
resolves to 9.1.1.

    tests/test_repository_structure.py    exit=0    4 passed
    tests/test_si1_governance.py          exit=0   14 passed
    tests/test_gate_anchors.py            exit=0   18 passed, 2 deselected
    tests/test_governance_tools.py        exit=0    8 passed

`pytest 9.1.1`, Python 3.11.15. **A9-final at the pushed head is
post-report evidence.**

**No new test was written**, and none was required: this task computes
nothing.

## 12. Did this specification tell me how to represent a re-issue?

**Yes. No judgement was required, and I invented no semantics.** §5 asks
this and says it matters more than a clean report, so here it is
precisely.

**What made it executable, item by item.**

- **§1 states the mechanism outright** — new branch, new name, new paths,
  cut from the evidence base — rather than leaving it to be derived from
  the acceptance criteria. The second issue's four-way conflict does not
  arise because there is nothing to reconcile.
- **A10 says the branch does not yet exist and that the instruction is
  executable here.** That is the sentence the second issue lacked. I
  verified it independently rather than taking it on trust:
  `git ls-remote origin refs/heads/fix/pi-decisions-v2` returned zero
  refs before I created it.
- **A0 forbids the `0430` token and says why** — indistinguishability by
  path. Given a reason, I could check the property rather than the rule,
  and confirm no path collides.
- **A5 names both append-only measures explicitly**, so the measure the
  second issue failed is not something an executor has to think to
  apply. **This is the single most valuable change**: it converts a
  property that was previously inferred from one measurement into two
  measurements, and it made the failure impossible to reproduce
  accidentally.
- **§0 states where the fault lay** — with the specification, not with
  the executor's resolution — which removes the incentive to defend a
  prior construction rather than replace it.
- **§1 says "reproduce, but re-verify rather than transcribing blind"**,
  which is what turned this from a copy into an execution. **The
  re-verification found nothing wrong**, but the instruction is what made
  that a result rather than an assumption.

**One ambiguity, which did not affect execution and is reported because
§5 asks.** §1 says *"Reproduce that content; do not re-derive it, and do
not re-open the wording that review settled"*, and A3 says *"the
expectation is none"* for differences. **Seven lines had to change**, and
the specification does not say whether task-identity pointers inside the
approved content count as "wording that review settled". I treated them
as pointers rather than wording, changed only those, verified by count
that none was missed, and enumerated every one in §5. **If the PI
intended the `Related branch and files` sections to keep naming the
superseded branch, that is a one-line correction and the rest of the
content is unaffected.**

**A note on what "the expectation is none" means in practice.** A
re-issue on a new branch **cannot** have zero differences if the approved
content contains its own branch name and specification path — those are
task identity, and A0 requires task identity to change. **The
expectation of none holds for substance and cannot hold for pointers.**
A future re-issue specification could say so directly, and then the
expectation would be exactly satisfiable.

## 5a. The register, quoted in full

`derivations/P2-DEFERRED-ITEMS.md`, 193 lines, as landed:

    # Deferred-items register — `P2-PHASE-01`

    **Kind:** a register. It records decisions, computes nothing, registers
    no gate and changes no status.

    Authority: `specs/2026-08-09T1416Z_pi-decisions-v2.md`.

    ---

    ## What this register is, and what it is not

    > **This register holds work that has been CONSIDERED and consciously
    > postponed.** It is not a list of open questions or of things not yet
    > thought about. **The distinction is the point**: an open item may
    > simply never have been examined, while an entry here was examined and
    > deferred with a reason, and carries the PI's position at the time of
    > deferral.

    **How to tell the two apart in this repository.** Open questions live in
    the `OPEN-AC-*` and `OPEN-PD-*` items of the admissibility-contract and
    parameter-domain drafts, and in `DECISION_LOG.md` entries that open an
    item as `UNESTABLISHED`. Those record that something has not been
    settled. **An entry here records that something was looked at, was
    understood well enough to be set aside deliberately, and was set aside
    anyway** — with the reason, the evidence, and the PI's position at the
    time.

    **Deferral is not a verdict.** No entry here is a finding that the
    deferred work is wrong, unphysical, or unnecessary. Where an entry
    records that a classification is *not* supported, that is a statement
    about the argument available, not about the object.

    **An entry's evidence and its PI position are separate fields, and they
    are not the same kind of claim.** The evidence is what was computed; the
    position is what the PI holds in the light of it. Where the two differ
    in strength, the entry says so in an `Evidence strength:` field rather
    than letting the position borrow the evidence's authority.

    **Every entry states what it is blocking**, so that a reader planning
    work knows whether a deferral is inert or load-bearing.

    ---

    ## `DEFERRED-01` — V/A mean-field representation

    **Status:** deferred, not excluded.

    **Reason.** The scalar channel is the direct route, and the programme's
    existing machinery — the gap equation, `I_0`, the scalar
    stationary-branch study — is built on a real auxiliary field. The V and
    A singlets do not admit the standard real linear
    Hubbard–Stratonovich contour that machinery uses, and would require a
    non-real contour or an otherwise reformulated bosonisation apparatus.

    **PI position.** The V/A representation may contain physically relevant
    information and must be returned to. **No evidence indicates it is
    unphysical.**

    **Evidence.** `g_V = g_A = -G/2`, with no real linear
    Hubbard–Stratonovich field admissible in either channel. From
    `derivations/P2-PHASE-01_channel_character_layers.md` §3.2, which
    tabulates

        channel                     g_L          g_P        sign(g)   real HS
        scalar_singlet_direct         G/N    2*G/N**2         +1        yes
        induced_V_singlet            -G/2       -G/N          -1        no
        induced_A_singlet            -G/2       -G/N          -1        no

    and from `results/P2-PHASE-01/channel-character-layers/layers.json`,
    where `layer_1b.channels.induced_V_singlet` and
    `layer_1b.channels.induced_A_singlet` each carry
    `g_in_normalisation_L: "-G/2"` and
    `real_linear_HS_field_admissible: false`.

    **Evidence strength.** The coefficients are exact symbolic quantities,
    reproduced from the frozen material by a gating control. **They are
    conditional** on the two PI rulings of 2026-08-08 — the Euclidean
    exponent mapping and the attraction/repulsion labels — as the source
    note records. Reversing the mapping reverses which channels admit the
    real contour.

    **Blocks:** nothing. The scalar route proceeds independently of this
    item.

    ---

    ## `DEFERRED-02` — Negative-mass stationary branch, `M̂ ≈ -7.59`

    **Status:** deferred, neither admitted nor excluded.

    **Reason.** The main line proceeds first.

    **Evidence strength.** Positive **restricted** one-dimensional
    curvature. The pinned exploratory note
    `derivations/P2-PHASE-01_scalar_stationary_exploratory.md` states of
    exactly that quantity:

    > Neither curvature is a full condensate-space Hessian or a
    > phase-admissibility statement.

    **"Restricted", not "stable", is the accurate word**, and this entry
    uses it throughout. What was measured is the curvature of the reduced
    one-dimensional scalar potential along the uniform `M̂` ansatz. **Full
    condensate-space stability was not computed, and phase admissibility
    was not assessed.**

    **PI position.** A solution stable under the analysis actually performed
    warrants physical interpretation rather than automatic dismissal.
    Classifying this branch as a lattice artifact is not supported: under
    the substrate reading there is no continuum limit, so the standard
    continuum-decoupling argument cannot by itself classify it as an
    unphysical lattice artifact.

    **Evidence.** An exact Wilson-complement relation
    `I_0(M̂) = I_0(-8-M̂)`, and positive restricted curvature at couplings
    below `G_c`. From
    `reports/2026-08-05_p2-phase-01_scalar-stationary-exploratory.md`:

    > There is instead an exact Wilson-complement relation
    > `I0(Mhat)=I0(-8-Mhat)`, induced by `p_mu -> pi-p_mu`; numerical
    > differences for four checked pairs are at most `1.1e-16`. It relates
    > algebraic roots but is not an `Mhat -> -Mhat` symmetry. Positive and
    > negative roots are therefore not declared phase-equivalent.

    and, from the same report's finest-offset root table, the sub-critical
    rows in which the complement branch carries positive restricted
    curvature while the near-zero branch does not:

        G/Gc    Mhat_left    curvature(left)    Mhat_right   curvature(right)
        0.80    -7.589264         0.417872       -0.410736       -0.022615
        0.90    -7.813202         0.400036       -0.186798       -0.009564
        0.98    -7.966034         0.404749       -0.033966       -0.001725

    Corroborated by
    `results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json`,
    whose `symmetry.wilson_complement_relation` reads
    `I0(Mhat) = I0(-8 - Mhat), from p_mu -> pi-p_mu; numerically checked
    below.` with four `complement_pairs` whose absolute differences are at
    most `1.1102230246251565e-16`.

    **Blocks:** the quantifier range of the SI-1 kill criterion. That
    criterion asks whether any admissible phase exists in the frozen space;
    with this branch neither admitted nor excluded, the SI-1 specification
    must state whether the branch falls inside the range. **This register
    does not answer that and does not amend the SI-1 gate text.**

    ---

    ## `DEFERRED-03` — Possible relation between `DEFERRED-01` and `DEFERRED-02`

    **Status: PI HYPOTHESIS, UNTESTED.**

    **Evidence: none.** This entry records a hypothesis and its motivation.
    It records no result.

    **This entry does not have the standing of the two above.** They are
    backed by computed quantities in named artifacts; this one is not backed
    by anything. It appears in the same register because it was considered
    and deliberately recorded, not because it is supported. **Nothing here
    may be cited as a finding, and no work should be planned on the
    assumption that the relation holds.**

    **Content.** Both deferred items arise in sectors outside the presently
    selected real-scalar mean-field route. The PI's hypothesis is that they
    are related.

    **Candidate link, offered as a starting point and not as a finding.**
    The Wilson term both generates the exact complement structure of the
    negative-mass branch and explicitly breaks chiral symmetry. Whether that
    breaking is related in any way to the deferred V/A representation is an
    untested PI hypothesis.

    **What would be needed to test it.** Not performed, and named only so
    the entry is actionable rather than decorative: something that connects
    the Wilson term's chiral-symmetry breaking to the vector/axial channel
    structure, in a calculation that does not presuppose the relation. **No
    such calculation exists in this repository**, and this entry does not
    authorize one.

    **Blocks:** nothing.

    ---

    ## Scope of this register

    It registers no gate and changes no status. `P2-PHASE-01` remains
    `PROPOSED` and `P2-GAP-01` remains `PASS`. No frozen or pinned artifact
    is modified, no result is recomputed, no gate text is amended, and no
    classification is made.

    **Entries are added by PI decision.** Nothing is removed from this
    register by an executor; an item that is taken up again is recorded as
    resumed, so that the deferral and its reason remain readable afterwards.

## 13. A0 — commit order, SHAs and messages

    commit 1  69fca932b53c17900c5b5241f6d9cfe152004b58
              specs/2026-08-09T1416Z_pi-decisions-v2.md
              "spec: re-issue the PI decisions and deferred-items task on a clean branch"

    commit 2  7dad9093f0453588501a1f5e2bb3212da1dc6e54
              DECISION_LOG.md, derivations/P2-DEFERRED-ITEMS.md
              "docs: record three PI decisions and open the deferred-items register"

**The specification file is byte-identical to the specification as
issued**, with a single trailing newline added because the issued text
did not end in one and every other file in `specs/` does. 275 lines.

### Commit-message hygiene

Each message was written to a file, inspected for `Co-Authored-By`,
`Claude-Session`, `claude.ai`, `Generated with` and `http` before
committing, committed with `git commit -F <file>` and never `-m`, and the
stored message read back from the object afterwards with
`git log -1 --format=%B`.

    commit 1   trailers suppressed: Co-Authored-By, Claude-Session
    commit 2   trailers suppressed: Co-Authored-By, Claude-Session

**Suppression is a fact to disclose, not an absence.** This harness
appends both by default; `-F` prevents it, and the read-back confirmed
neither reached any stored message. The intended report commit message
was prepared the same way, with the same two suppressed:

    docs: report the re-issued PI decisions and deferred-items task

    Records the third execution of the approved content, on a clean
    branch cut from the evidence base under a new task name and new
    paths. All seven pins verify, every evidence quotation was
    re-located in the pinned material rather than inherited, and both
    append-only measures are zero: against the evidence base and
    against every commit's parent.

    The only differences from the approved content at 52f65117 are seven
    task-identity pointers - three Related-branch-and-files sections and
    the register's Authority line - each enumerated with its reason.
    Every other byte is reproduced unchanged.

    Reports that this specification required no judgement about how to
    represent a re-issue, and names the one ambiguity it leaves: whether
    task-identity pointers inside approved content count as wording that
    review settled.

## 14. Repository inputs actually read, by path

    DECISION_LOG.md                                             (evidence base and 52f65117)
    GATES.md
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md           (digest only)
    derivations/P2-PHASE-01_channel_character.md                (digest only)
    derivations/P2-PHASE-01_channel_character_layers.md
    derivations/P2-PHASE-01_scalar_stationary_exploratory.md
    derivations/P2-DEFERRED-ITEMS.md                            (at 52f65117, as approved)
    results/P2-PHASE-01/channel-character-layers/layers.json
    results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json
    reports/2026-08-05_p2-phase-01_scalar-stationary-exploratory.md
    scripts/governance_tools/scope_checker.py

**Exclusions.** The quarantined `−3.2(5)`, the suspended
`P2-BETAV-CIRC-01` result, and the historical Finding 5 extraction were
**NOT READ**.

**Nothing was installed.**

## 15. Stops and clarifications

**No stop occurred, and none was near.** This is the first execution in
this task's three attempts where that is true without qualification.

### `SPECIFICATION_DEFECT`

**None.** For the record, all three defects raised against the earlier
issues are resolved here:

    issue 1   A1 pinned only the exploratory derivation note, which is a
              pre-registration and carries no roots or curvature
                -> the report and results artifact are pinned

    issue 2   the derivation note was dropped when the other two were
              added, leaving the scope-limitation quote unverifiable
              from A1
                -> all three are pinned, and A1 states the split and
                   why it matters

    issue 2   the re-issue mechanism was unspecified against an
              already-executed branch
                -> §1 states the mechanism; A10 confirms the new branch
                   does not exist; A0 forbids the old token; A5 names
                   both append-only measures

### `ENVIRONMENT`

None. Nothing was installed.

### `OBSERVATION_METHOD_ERROR`

None. One thing worth recording as method rather than error: **A1's
assertion that the exploratory note contains no numerical findings was
checked rather than accepted** (§2), and the check is what licenses the
report to describe the three-way evidence split as observed. **An
assertion in a specification about the content of a pinned file is still
an assertion until executed.**

### `REPOSITORY_DEFECT`

None.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`

**One, minor, and it did not block.** Whether task-identity pointers
inside approved content fall under "wording that review settled" (§1) or
under task identity that A0 requires to change. Resolved as pointers,
every instance enumerated in §5, residual count verified zero. **A
one-line clarification would remove it.**

## 16. Secondary findings, and what I would have specified differently

**1. "The expectation is none" is not satisfiable for a re-issue on a new
branch, and should be stated as "none in substance".** Approved content
that names its own branch and specification path necessarily changes when
those change. A3's expectation is right about substance and cannot hold
literally. **The fix is one clause**: *task-identity pointers inside the
reproduced content are expected to change and must be enumerated;
substance is expected to be identical.* That is exactly what I did, but
an executor reading A3 literally would see a criterion it could not meet
and might stop.

**2. A5's two-measure form is the reusable part of this specification.**
It converts "append-only" from a property inferred from one measurement
into two measurements that fail differently. **I would put it in every
specification that touches an append-only file**, not only in re-issues —
the superseded branch is proof that the single measure can read clean
while the property is violated, and nothing about that failure was
specific to re-issuing.

**3. The register's `Blocks:` line is still unreferenced from
`GATES.md`.** `DEFERRED-02` records that the SI-1 kill criterion's
quantifier range is undetermined — a live constraint on a future gate
specification, discoverable only by someone already reading the register.
The specification correctly forbids adding the cross-reference here and
names it an agreed separate task. **Recorded so it is not lost between
tasks**, as it has now survived three executions of this one.

**4. Recurring, and raised for the eighth time.** The `CONVENTIONS.md`
index entry deferred by
`specs/2026-08-08T1702Z_integrate-exponent-mapping-ruling.md` §0(b) is
still unwritten. **Five conventions and decisions now live only as dated
`DECISION_LOG.md` entries**, and a merged script on `main` locates two of
them by exact heading text — so a heading rename would break a
computation while changing no meaning. The proposed amendment set
explicitly defers this as a design question. **The design question is the
machine-readable format; the obligation to index a convention a
computation consumes is rule-shaped and separable from it.**

**5. What this task demonstrates about the amendment set, offered because
it is the first application.** The re-issue amendment's value showed up
in a specific, measurable way: **the second issue needed 364 deleted
lines on a parent-to-child diff to satisfy its criteria; this one needed
zero, and satisfied strictly more criteria.** The mechanism was not
merely cleaner — it removed the conflict that produced the deletions,
rather than asking the executor to resist resolving it.
