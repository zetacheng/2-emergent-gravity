# Execution report — record three PI decisions and open a deferred-items register

Specification: `specs/2026-08-09T0430Z_pi-decisions-and-deferred.md` (re-issued)
Specification evidence base: `f309f61c9c14b0e2c63e078f9c0d0809422742e7`
Branch: `fix/pi-decisions-and-deferred`
Pre-report head: `5daa04fdfe9ebc4e79794e9ac10711d2dfaf9839`

**Outcome.** Three separate `DECISION_LOG.md` entries and the register
are landed. Both defects reported against the first issue are gone: all
six pins verify, `DEFERRED-02`'s evidence is in the pinned material, and
every required phrase is satisfiable without touching a ruling. Nothing
was computed, no gate status changed, no frozen or pinned artifact was
touched, and the SI-1 gate text was not amended. Net diff against the
evidence base is **3 additions and 1 modification, zero deleted lines.**
All four validators pass.

**One thing the Reviewer must read first, because it is a governance
decision I made and can be reversed.** This specification is the
**second issue** of a task whose first issue I executed and pushed to
`fix/pi-decisions-and-deferred` at `59c763ab…`. **The branch already
existed.** §1 sets out the collision, the four constraints that appear
to conflict, and the construction that satisfies all of them without a
force-push and without destroying the superseded record. **If the PI
intended something else, nothing is lost** — the first issue's commits
remain reachable in this branch's history.

---

## 1. The branch already existed, and what I did about it

### 1.1 The collision

The first issue of this specification was executed and pushed:

    fix/pi-decisions-and-deferred   59c763abcfd406bf6757859825c17bff4e4a0c25

carrying the superseded specification, an earlier `DECISION_LOG.md`
triple, an earlier register, and an execution report — all at the same
four paths this issue names, because `{HHMM}Z` was fixed as `0430` and
this issue does not change it.

**Four constraints of this specification appear to conflict:**

    A6   final base-to-head scope is exactly 3 additions and 1 modification
    A8   create the branch from f309f61c…, push the task branch
    §4   branch naming: use fix/pi-decisions-and-deferred
    §4   no force-push, no history rewrite

**A fresh `{HHMM}Z` token fails A6** — the tree would carry both the old
and the new specification and both reports, five or six additions, and
removing the old ones needs `delete`, which A6 lists as a forbidden
operation. **A different branch name violates §4.** **Resetting the
branch and force-pushing violates §4** and would destroy an unmerged
record, which this programme's own policy treats as destroying content
rather than a name.

### 1.2 The construction that satisfies all four

**`git diff base head` compares trees, not history.** Building the
re-issued content *on top of* `59c763ab…`, at the same four paths, makes
the net base-to-head scope exactly what A6 demands, while the branch
still descends from `f309f61c…` and every earlier commit stays
reachable.

    commit 1  overwrites specs/2026-08-09T0430Z_… with the re-issued text
    commit 2  rebuilds DECISION_LOG.md as (evidence-base blob) + (three
              re-issued entries), and rewrites the register
    commit 3  overwrites reports/2026-08-09T0430Z_… with this report

**`DECISION_LOG.md` was rebuilt from the evidence-base blob**, not
edited in place: the file was written as the base blob followed by the
three new entries, so the superseded triple is absent from the final
tree and the base-to-head diff is append-only with **zero deletions**.
Verified in §5.1.

**No force-push. No history rewrite. No `delete` operation. The
superseded record is preserved** in the branch's own history at
`59c763ab…` and its parents.

### 1.3 What this costs, stated plainly

**The first issue's specification and report are no longer in the
final tree** — they are only in git history. That is the price of
reusing the path, and reusing the path is what A6's three-addition
scope forces once `delete` is forbidden.

**I did not treat this as a stop.** §4 says to stop and report when
instructions are inconsistent; the construction above means they are
not inconsistent, because all four are satisfied simultaneously. **But
the PI may have intended a reset, or a fresh branch, or may not have
known the branch existed.** All three remain available and nothing here
prevents them:

    to reset      the branch history holds every superseded commit
    to rename     no ref outside this branch was touched
    to keep       nothing further is required

## 2. A8 — refs, read from the remote

    refs/remotes/origin/main                  f309f61c9c14b0e2c63e078f9c0d0809422742e7
    remote refs/heads/main                    f309f61c9c14b0e2c63e078f9c0d0809422742e7
    local  refs/heads/main                    0f7961747abe2a18b436c0b1e5b928f425ea4d9a
    remote refs/heads/fix/pi-decisions-and-deferred
                                              59c763abcfd406bf6757859825c17bff4e4a0c25  (before this task)

Both remote `main` refs resolve to the evidence base. **Local `main` is
stale by design and was not repaired.** No `main` ref was moved. The
task branch descends from `f309f61c…`, confirmed by
`git merge-base --is-ancestor`. `review/role-model-and-executors` is
untouched at `10c260b9…`. **No branch was deleted.**

**`{HHMM}Z` is `0430`**, carried over from the first issue's commit 1
for the reason in §1.2.

## 3. A1 — pinned inputs, six of them, verified before use

Digests read from the git objects at the evidence base; all six matched.

    derivations/P2-PHASE-01_scalar_stationary_exploratory.md
      80586e33ef07e307729af4597f72b48f6ecee74fc6a0f396b593f735ef322599   MATCH
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

**The last two are the pins added by this issue**, and they are what
makes A2 satisfiable from A1's enumerated set. The digests match the
ones I supplied in the first issue's report, which is the expected
outcome of a correct amendment rather than an independent confirmation
— they came from the same two files at the same commit.

## 4. A2 — cited evidence, verified and quoted, all from pinned material

### 4.1 `DEFERRED-01`

**Cited:** `g_V = g_A = -G/2`, no real linear HS field admissible
(channel-character layers derivation).

**Found** in `derivations/P2-PHASE-01_channel_character_layers.md` §3.2
— pinned, `4cea53a7…`:

    channel                     g_L          g_P        sign(g)   real HS
    scalar_singlet_direct         G/N    2*G/N**2         +1        yes
    induced_V_singlet            -G/2       -G/N          -1        no
    induced_A_singlet            -G/2       -G/N          -1        no

and in `results/P2-PHASE-01/channel-character-layers/layers.json` —
pinned, `fe343c74…`:

    layer_1b.channels.induced_V_singlet.g_in_normalisation_L              "-G/2"
    layer_1b.channels.induced_V_singlet.real_linear_HS_field_admissible   false
    layer_1b.channels.induced_A_singlet.g_in_normalisation_L              "-G/2"
    layer_1b.channels.induced_A_singlet.real_linear_HS_field_admissible   false

**Both values and both flags present in pinned material. No stop.**

### 4.2 `DEFERRED-02`

**Cited:** exact Wilson complement `I_0(M) = I_0(-8-M)`; positive
restricted curvature below `G_c` (exploratory scalar stationary study
report and results artifact).

**Found** in `reports/2026-08-05_p2-phase-01_scalar-stationary-exploratory.md`
— pinned, `70ab88ed…`, verified as an exact substring after whitespace
normalisation:

> There is instead an exact Wilson-complement relation
> `I0(Mhat)=I0(-8-Mhat)`, induced by `p_mu -> pi-p_mu`; numerical
> differences for four checked pairs are at most `1.1e-16`. It relates
> algebraic roots but is not an `Mhat -> -Mhat` symmetry. Positive and
> negative roots are therefore not declared phase-equivalent.

and, from the same report's finest-offset root table, the sub-critical
rows, each verified as an exact row of the source table:

    G/Gc    Mhat_left    Mhat_right   curvature(left)   curvature(right)
    0.80    -7.589264     -0.410736         0.417872          -0.022615
    0.90    -7.813202     -0.186798         0.400036          -0.009564
    0.98    -7.966034     -0.033966         0.404749          -0.001725

**Positive curvature on the complement branch at `G/G_c < 1` is the
"positive restricted curvature below `G_c`" of the cited line**, and
`-7.589264` is the `M̂ ≈ -7.59` of the entry title.

Corroborated in
`results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json`
— pinned, `a4537efa…`:

    symmetry.wilson_complement_relation
      "I0(Mhat) = I0(-8 - Mhat), from p_mu -> pi-p_mu; numerically checked below."
    symmetry.complement_pairs
      4 pairs, max |difference| = 1.1102230246251565e-16

**Both halves of the evidence line are in pinned material. No stop.**

**And the qualifier is verified too.** The `Evidence strength:` field
quotes the pinned derivation note
`derivations/P2-PHASE-01_scalar_stationary_exploratory.md` —
`80586e33…`:

> Neither curvature is a full condensate-space Hessian or a
> phase-admissibility statement.

confirmed as an exact substring of that note. **The pinned note is a
pre-registration document and carries no roots or curvature values**;
that is why it is the source of the qualifier and not of the numbers,
and why this issue pins the other two files as well.

### 4.3 `DEFERRED-03` — absence of evidence is content

A2 requires, for this entry, that it **states `Evidence: none` and
supplies no evidentiary citation.** Verified in the landed register:

    Status: PI HYPOTHESIS, UNTESTED.
    Evidence: none. This entry records a hypothesis and its motivation.
    It records no result.

**No lookup was attempted and none should be.** Treating this as a
failed evidence check would be the confusion between *not observed* and
*observed negative*.

## 5. A3 — three `DECISION_LOG.md` entries, one per decision

Three separate top-level entries, **not one combined entry**:

    1519  ## 2026-08-09 — Mean-field channel for `P2-PHASE-01`: the scalar channel with a real auxiliary field
    1597  ## 2026-08-09 — The charge-conjugation phase `eta` is not selected; both signs are computed
    1677  ## 2026-08-09 — The negative-mass stationary branch is DEFERRED, not excluded

Each reproduces its §0 ruling **verbatim**, copied programmatically from
the specification and compared line by line after insertion:

    Decision 1   23 lines   identical
    Decision 2   22 lines   identical
    Decision 3   38 lines   identical

Structural metadata (`Date:`, `Decision owner:`, `Effect:`, and the
`### Reason`, `### Consequences`, `### Related gate`,
`### Related branch and files` sections) was added around each, not
inside it.

### 5.1 Append-only

    git diff --numstat f309f61c… 5daa04fd… -- DECISION_LOG.md
      256     0       DECISION_LOG.md

    deleted lines across the entire base-to-head diff (^-[^-]):  0

**256 added, zero deleted**, and the final file is byte-identical to the
evidence-base blob followed by the three entries — by construction, not
by inspection: §1.2's rebuild wrote it that way. The file grew from 1517
to 1773 lines.

**Only three `## 2026-08-09` headings exist in the final file.** The
superseded triple is not present alongside them.

### 5.2 Required phrases, checked against normalised text

Blockquote prefixes `> ` stripped, `**` and backticks stripped, all
whitespace collapsed to single spaces, en dashes left as they are.

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

**Every required phrase is now inside the verbatim ruling text**, with
`Date:`-style metadata not required this time. The first issue's
unsatisfiable `rests on an arbitrary sign` has been replaced by
`depends on an unresolved sign convention`, which Decision 2's ruling
contains in its own words: *"then the diquark channel character depends
on an unresolved sign convention"*. **No ruling text was edited to make
a check pass, and none needed to be.**

The second occurrence of `depends on an unresolved sign convention` in
entry 2 is in my `### Consequences` prose, which paraphrases the
ruling's diagnostic; the required occurrence is the one in the ruling.

### 5.3 The three entries, quoted

Each is reproduced with its ruling blockquote in full; the file carries
the prose sections complete.

**Entry 1** — `Date: 2026-08-09`,
`Decision owner: Principal Investigator`,
`Effect: selects a route for mean-field work; defers an alternative`.

    > **PI ruling, 2026-08-09 — mean-field channel for `P2-PHASE-01`.**
    >
    > Mean-field work proceeds in the **scalar channel with a real auxiliary
    > field.** Under the 2026-08-08 rulings the scalar singlet has `g > 0`
    > and admits the standard real linear Hubbard–Stratonovich
    > representation; the induced V and A singlets have `g < 0` and do not.
    >
    > **This is a choice of direct route, not a judgement that the V/A
    > representation is wrong.** The programme's existing machinery — the
    > gap equation, `I_0`, the stationary-branch study — is built on a real
    > auxiliary field. **The V/A channel does not admit the standard real
    > linear HS contour that machinery uses, and would require a non-real
    > contour or an otherwise reformulated bosonisation apparatus.**
    >
    > **No evidence indicates the V/A representation is unphysical, and the
    > PI's position is that it may contain physically relevant information
    > and must be returned to. It is deferred, not excluded** — see
    > `DEFERRED-01`.
    >
    > **This does not close `OPEN-AC-1`.** It selects the channel for
    > mean-field work; the Fierz ambiguity — that channels equivalent as
    > operators are inequivalent after truncation — is unaffected by which
    > one is used.

Its `### Reason` records that the Layer-1b recomputation established
which channels admit the real contour, and states that **no calculation
in this repository bears on whether the V/A representation is
physically correct.** Its `### Consequences` record the route, the
`DEFERRED-01` entry, that `OPEN-AC-1` is not closed, and that no gate
status changes.

**Entry 2** — `Date: 2026-08-09`,
`Decision owner: Principal Investigator`,
`Effect: declines to select a convention; prescribes a two-sign
evaluation`.

    > **PI ruling, 2026-08-09 — `η` is not selected; both signs are
    > computed.**
    >
    > The diquark rearrangement requires `ψ̄^c = η ψ^T C⁻¹`. **The frozen
    > material fixes no value of `η`, and unlike the exponent mapping no
    > executed calculation constrains it.**
    >
    > **For the SIGN AMBIGUITY exposed by the channel-character derivation,
    > the programme evaluates both the `η = +1` and the `η = −1`
    > representative rather than selecting between them.** This does not
    > assert that the full convention space is exactly two elements — the
    > residual phase freedom has not been characterised — only that the
    > ambiguity shown to affect the paired product is a sign, and both signs
    > are to be carried through and reported.
    >
    > **The reason is diagnostic.** If both signs give the same channel
    > character, **the exposed `η = ±1` sign ambiguity does not affect that
    > character, and that sign question closes** — the wider phase freedom
    > remains uncharacterised either way. **If they give opposite
    > characters, then the diquark channel character depends on an
    > unresolved sign convention — and that is something the programme must
    > know rather than conceal behind a choice.**

Its `### Consequences` record that the two-sign evaluation is a separate
authorized task and **is not performed here**, that the residual phase
freedom remains uncharacterised in either outcome, and that the
particle–particle Grassmann ordering and the diquark normalisation
remain unfrozen.

**Entry 3** — `Date: 2026-08-09`,
`Decision owner: Principal Investigator`,
`Effect: declines to classify; records a consequence for SI-1`.

    > **PI ruling, 2026-08-09 — the negative-mass branch is DEFERRED, not
    > excluded.**
    >
    > The exploratory study found a second stationary branch at
    > `M̂ ≈ −7.59`, the exact Wilson complement of the trivial branch, **with
    > positive restricted curvature in the explored one-dimensional
    > stationary analysis, including below `G_c`.**
    >
    > **"Restricted", not "stable", is the accurate word.** The pinned
    > exploratory note states of exactly that quantity: *"Neither curvature
    > is a full condensate-space Hessian or a phase-admissibility
    > statement."* **A bare "stable" would let a later reader take the
    > premise as stronger than the evidence.**
    >
    > **It is not classified as a lattice artifact.** The complement
    > relation and the observed restricted stability **tie the branch
    > structurally to the Wilson term; they do not establish full
    > condensate-space stability, phase admissibility, or absence of
    > physical content.** Under the substrate reading there is no continuum limit, so
    > **the standard continuum-decoupling argument cannot by itself classify
    > this branch as an unphysical lattice artifact.**
    >
    > **The PI's position is that a solution stable under the analysis
    > actually performed corresponds to something that warrants physical
    > interpretation rather than automatic dismissal.** The branch is
    > deferred pending the main line — see `DEFERRED-02`.
    >
    > **The qualifier is load-bearing.** Written as *a stable solution
    > corresponds to something real*, the position would quietly restore the
    > stability claim narrowed two paragraphs above.
    >
    > **Consequence for SI-1, recorded now so it is not met by surprise.**
    > `P2-PHASE-01`'s kill criterion asks whether any admissible phase exists
    > in the frozen space. **With this branch neither admitted nor excluded,
    > that criterion's quantifier range is undetermined**, and the SI-1
    > specification must state whether the branch falls inside it. **This
    > ruling does not answer that; it records that the question is now
    > unavoidable.**

Its `### Reason` explains why "restricted" is doing work and quotes the
pinned note. Its `### Consequences` state explicitly that the ruling
**does not answer the SI-1 question and does not amend the SI-1 gate
text**, and that no exploratory result, branch-depth row, or line of the
parameter-domain draft is altered.

**This ruling closed the finding I raised against the first issue.** I
reported that Decision 3's premise was one word stronger than the
evidence — "stable" where the evidence supports "positive restricted
curvature". The re-issued ruling narrows it in its own text, three
times, and adds a paragraph saying the qualifier is load-bearing.
**Nothing was left for the register to compensate for**, which is the
right place for the correction to have been made.

## 6. A4 — the register, quoted in full

`derivations/P2-DEFERRED-ITEMS.md`, 193 lines, reproduced verbatim:

    # Deferred-items register — `P2-PHASE-01`

    **Kind:** a register. It records decisions, computes nothing, registers
    no gate and changes no status.

    Authority: `specs/2026-08-09T0430Z_pi-decisions-and-deferred.md`.

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

## 7. Does the register read as open questions, or as consciously deferred work?

**It reads as consciously deferred work, and this issue made it read
more clearly than the last one did.** The distinction is carried by
structure, not by the opening paragraph alone.

**What carries it.**

- **The purpose statement is quoted verbatim at the top**, and a
  paragraph after it names where open questions actually live in this
  repository — the `OPEN-AC-*` and `OPEN-PD-*` items of the two drafts,
  and `DECISION_LOG.md` entries opened as `UNESTABLISHED`. **A reader
  can check the boundary rather than take it on trust.**
- **Every entry has a `Reason:` and a `PI position:`.** An open
  question has neither. A reason for deferring is only writable about
  something already understood; a position is only holdable about
  something already examined.
- **`Evidence strength:` is new in this issue and does more than it
  looks.** It separates what was computed from what the PI holds in
  light of it, and by existing at all it tells a reader that the two
  are different kinds of claim. **A list of open questions has no such
  field, because it has nothing to grade.** `DEFERRED-01` now carries
  one too, recording that its coefficients are exact but conditional on
  the two 2026-08-08 rulings.
- **Every entry states what it blocks.** `DEFERRED-01` blocks nothing;
  `DEFERRED-02` blocks the quantifier range of the SI-1 kill criterion.
  **A list of open questions does not know its own load-bearing
  status.**
- **`Status:` lines say what kind of non-answer each is** — "deferred,
  not excluded", "neither admitted nor excluded". Those are refusals to
  classify, which is a different act from not having looked.

**Where it is weakest, stated plainly.** `DEFERRED-03` is a hypothesis
with no evidence, and a hypothesis sits closer to an open question than
either of the others. It is marked four ways: `Status: PI HYPOTHESIS,
UNTESTED` in capitals, `Evidence: none` on its own line, a paragraph
saying it "does not have the standing of the two above" and that
"nothing here may be cited as a finding", and a "what would be needed to
test it" paragraph recording that no such calculation exists. **With
those it reads as a recorded hypothesis. Remove any one and it starts to
read like an item nobody has got to yet.**

**One structural risk I flag rather than fix.** The register lives under
`derivations/`, alongside notes that do contain derivations, and
`derivations/README.md` states what a derivation note must contain —
a contract this file does not meet and should not. Its first line says
`**Kind:** a register. It records decisions, computes nothing`, which is
the only thing standing between the location and the wrong expectation.
**A `registers/` location, or an exemption in `derivations/README.md`,
would carry it structurally instead of textually** — but that file is
protected under A5 and I did not touch it.

## 8. A5 — nothing else touched

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

**Every pre-existing file under `derivations/`**, enumerated from the
evidence base and compared one by one:

    29 pre-existing derivations files checked, 0 differ

and the only change to that directory:

    A   derivations/P2-DEFERRED-ITEMS.md

**All six pinned artifacts are inside those identical trees**, so no
pinned or frozen artifact was modified.

**No gate status changed.** `GATES.md` is blob-identical, its `^## P2-`
anchor count is 14 at both ends, `P2-GAP-01` still reads `Status: PASS
(continuum exact; lattice I_0 agrees with paper at matched mass)` and
`P2-PHASE-01` still reads `Status: PROPOSED`. **Decision 3 altered no
gate**; it records that a question about SI-1's quantifier range is
unavoidable, which is not a change to SI-1, and the SI-1 gate text was
not edited.

**Nothing was computed.** No script was run against repository data
other than the governance tools and `pytest`; no results artifact was
written or regenerated.

## 9. A6 — scope

**Manifest template** (SHA-256
`0a540d745378ef37bec9a313d695caf3d9bb835e6c714fb2275667dab5e0c485`,
unchanged from the first issue because the path set is unchanged):

    {
      "base": "f309f61c9c14b0e2c63e078f9c0d0809422742e7",
      "head": "{PUSHED_HEAD}",
      "mode": "exact",
      "required": [
        {"operation": "add", "path": "specs/2026-08-09T0430Z_pi-decisions-and-deferred.md"},
        {"operation": "add", "path": "derivations/P2-DEFERRED-ITEMS.md"},
        {"operation": "add", "path": "reports/2026-08-09T0430Z_pi-decisions-and-deferred.md"},
        {"operation": "modify", "path": "DECISION_LOG.md"}
      ],
      "optional": [],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

**Intended final resolution:** `head` set to the pushed head, all four
records required — **3 additions and 1 modification.** A fifth path
would be a defect. `derivations/P2-DEFERRED-ITEMS.md` does not exist at
the evidence base and is confirmed an `add`.

**Scope check at the pre-report head** `5daa04fd…`, checker output
verbatim:

    {
      "base": "f309f61c9c14b0e2c63e078f9c0d0809422742e7",
      "failures": [],
      "head": "5daa04fdfe9ebc4e79794e9ac10711d2dfaf9839",
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
          "path": "reports/2026-08-09T0430Z_pi-decisions-and-deferred.md"
        },
        {
          "operation": "add",
          "path": "specs/2026-08-09T0430Z_pi-decisions-and-deferred.md"
        }
      ],
      "overall": "PASS",
      "tool": "scope_checker"
    }

    exit status 0

**One honest wrinkle in reading that output.** Unlike the first issue,
the report path is already an observed addition *at the pre-report
head* — because the superseded report occupies it. **The check passes
on the path set, not on the content at that path**, and the content
there at `5daa04fd…` is still the first issue's report. Commit 3
replaces it. **A reader must not take the pre-report check as evidence
that this report existed when it ran.**

Raw `git diff --name-status` at the same head, with line counts:

    M   DECISION_LOG.md                                            256   0
    A   derivations/P2-DEFERRED-ITEMS.md                           193   0
    A   reports/2026-08-09T0430Z_pi-decisions-and-deferred.md      894   0   (superseded content)
    A   specs/2026-08-09T0430Z_pi-decisions-and-deferred.md        357   0

**Zero deletions on every path.** The final scope check at the pushed
head is post-report evidence and is returned to the Reviewer.

## 10. A7-pre — validators at the pre-report head

Run individually with `python -m pytest <path>`, that exact invocation,
since `pytest` on this host resolves to 9.0.2 while `python -m pytest`
resolves to 9.1.1.

    tests/test_repository_structure.py    exit=0    4 passed
    tests/test_si1_governance.py          exit=0   14 passed
    tests/test_gate_anchors.py            exit=0   18 passed, 2 deselected
    tests/test_governance_tools.py        exit=0    8 passed

`pytest 9.1.1`, Python 3.11.15. **A7-final at the pushed head is
post-report evidence.**

**No new test was written**, and none was required: this task computes
nothing, so there is no computation to regression-lock.

## 11. A0 — commit order, SHAs and messages

    commit 1  a08817a6aab05b8289463002541dede0d3d07f93
              specs/2026-08-09T0430Z_pi-decisions-and-deferred.md
              "spec: re-issued specification for the PI decisions and deferred register"

    commit 2  5daa04fdfe9ebc4e79794e9ac10711d2dfaf9839
              DECISION_LOG.md, derivations/P2-DEFERRED-ITEMS.md
              "docs: record three PI decisions and open the deferred-items register"

**No derivation note was written**, as A0 states none is required: this
task performs no derivation and `AGENTS.md` rule 3 governs production
code, of which there is none.

**The specification file is byte-identical to the re-issued
specification as received**, with a single trailing newline added
because the issued text did not end in one and every other file in
`specs/` does. 357 lines.

### Commit-message hygiene

Each message was written to a file, inspected for `Co-Authored-By`,
`Claude-Session`, `claude.ai`, `Generated with` and `http` before
committing, committed with `git commit -F <file>` and never `-m`, and
the stored message read back from the object afterwards with
`git log -1 --format=%B`.

    commit 1   trailers suppressed: Co-Authored-By, Claude-Session
    commit 2   trailers suppressed: Co-Authored-By, Claude-Session

**Suppression is a fact to disclose, not an absence.** This harness
appends both by default; `-F` prevents it, and the read-back confirmed
neither reached any stored message. The intended report commit message
was prepared the same way, with the same two suppressed:

    docs: report the three PI decisions and the deferred-items register

    Records the re-issued specification's execution: three separate
    DECISION_LOG.md entries reproducing their PI rulings verbatim, and
    the deferred-items register with DEFERRED-01, DEFERRED-02 and
    DEFERRED-03.

    Both defects reported against the first issue are gone. All six
    pins verify and DEFERRED-02's evidence is in the pinned material;
    every required phrase is satisfied inside the verbatim rulings, so
    no ruling was edited and no phrase needed placing in prose.

    Reports the branch collision with the superseded first issue and
    the construction used: the re-issued content was built on top at
    the same four paths, and DECISION_LOG.md was rebuilt from the
    evidence-base blob, so the net base-to-head scope is 3 additions
    and 1 modification with zero deletions, without a force-push and
    without destroying the superseded record.

## 12. Repository inputs actually read, by path

    DECISION_LOG.md
    GATES.md
    docs/BRANCHING_POLICY.md
    derivations/P2-PHASE-01_scalar_stationary_exploratory.md
    derivations/P2-PHASE-01_channel_character.md                (digest only)
    derivations/P2-PHASE-01_channel_character_layers.md
    derivations/P2-DEFERRED-ITEMS.md                            (as landed here)
    results/P2-PHASE-01/channel-character-layers/layers.json
    results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json
    reports/2026-08-05_p2-phase-01_scalar-stationary-exploratory.md
    scripts/governance_tools/scope_checker.py

**Exclusions.** The quarantined `−3.2(5)`, the suspended
`P2-BETAV-CIRC-01` result, and the historical Finding 5 extraction were
**NOT READ**.

**Nothing was installed.**

## 13. Stops and clarifications

**No stop occurred.** Both conditions that stopped or nearly stopped the
first issue are resolved by this re-issue, and the one new condition —
the branch collision — was satisfiable without violating any
instruction.

### `SPECIFICATION_DEFECT`

**None in this issue.** For the record, both defects I raised against
the first issue are fixed here and neither recurred:

    A1 pinned only the exploratory derivation note, which is a
    pre-registration and carries no roots or curvature
      -> this issue pins the report and the results artifact as well,
         and A2 is satisfiable from A1's enumerated set

    A3 required `rests on an arbitrary sign`, absent from the ruling
      -> this issue requires `depends on an unresolved sign
         convention`, which the ruling contains verbatim

**The re-issue also states the general rule** that a required phrase may
live in surrounding prose where the ruling does not contain it, which
removes the class of defect rather than only the instance.

### `ENVIRONMENT`

None. Nothing was installed.

### `OBSERVATION_METHOD_ERROR`

None.

### `REPOSITORY_DEFECT`

None.

### `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`

**One, and it is §1.** The specification names a branch that already
carries a superseded execution of itself, and does not say whether to
replace, extend, or rename. I did not resolve that by choosing among
the four apparently conflicting constraints; **I found the construction
that satisfies all four** and reported it. **But whether the PI wanted
the superseded specification and report to remain in the tree is a
question the specification does not answer, and §1.3 records that they
do not.** Reversible in every direction.

## 14. Secondary findings, and what I would have specified differently

**1. A re-issued specification needs to say what to do with the first
issue's branch.** This is now a recurring shape: a specification is
executed, the executor reports defects, the specification is re-issued
with the same branch name and the same `{HHMM}Z`-derived paths. **The
re-issue should state whether the branch is replaced, extended, or
renamed**, because A6's exact scope, the `delete` prohibition, and the
force-push prohibition together leave exactly one construction, and an
executor who does not find it will stop with nothing delivered.

**2. Reusing `{HHMM}Z` across issues is what makes the construction
work, and it is nowhere stated.** A0 says the token is "fixed once by
commit 1", which for a re-issue is ambiguous — commit 1 of which issue?
**Fixing it once per task rather than once per issue is the reading that
satisfies A6**, and I would say so explicitly.

**3. `DEFERRED-02`'s `Blocks:` line is still the most consequential
output of this task, and nothing points at it.** It states that the SI-1
kill criterion's quantifier range is undetermined — a live constraint on
a future gate specification, recorded in a register that `GATES.md` does
not reference, and `GATES.md` is protected here. **A follow-up adding a
cross-reference from the gate to the register** would put the constraint
where someone reading the gate will find it. I raised this against the
first issue and it is unchanged.

**4. Recurring, and raised for the seventh time.** The `CONVENTIONS.md`
index entry deferred by
`specs/2026-08-08T1702Z_integrate-exponent-mapping-ruling.md` §0(b) is
still unwritten. There are now **five** conventions and decisions living
only as dated `DECISION_LOG.md` entries, and one merged script already
locates two of them by exact heading text. **Every entry added raises
the cost of the index task and the risk of the next executor
concluding, again, that something is not defined.**

**5. A small thing the re-issue does well, recorded because it is worth
repeating.** Decision 3 does not merely use the narrower word; it
contains a paragraph saying *why* the qualifier is load-bearing and what
the loose wording would have restored. **A correction that explains its
own mechanism survives paraphrase**, and this one will still be intact
after someone summarises the entry.
