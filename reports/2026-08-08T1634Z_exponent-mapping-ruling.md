# Execution report — Euclidean exponent mapping ruling and the generator-sum criticality item

Authority: `specs/2026-08-08T1634Z_exponent-mapping-ruling.md`
Evidence base: `481f4ad77cb4ec92ef9d58471530784087e67a43`
Branch: `fix/exponent-mapping-ruling`
Classification: MATERIAL. Branch only.

**This task records two things and computed nothing.** No gate status
changed, nothing frozen was modified, no Hubbard–Stratonovich channel
was selected, and neither withheld verdict was re-run.

Written at head `992e6001b029177976ecd7ce34a23492f549195f`; it contains
neither its own commit SHA nor the final branch head.

---

## 1. A2 — the three verifications, and one qualification that matters

**The specification is right to insist these be checked. Two hold as
stated. One does not hold literally, and §7 is where I say how much
weight that bears.**

### 1.1 No Euclidean action, free part, or exponent mapping — CONFIRMED

Searched across all three pinned files. Counts:

    S_E                   1 (case-insensitive)  ->  0 (case-sensitive)
    Euclidean action      0        Boltzmann            0
    exp(-                 0        exp[-                0
    e^{-                  0        Z =                  0
    partition function    0        free part            0
    kinetic               0        L_E                  0
    S_int                 0        action density       0
    enters the exponent   0        Wick                 0

**The single `S_E` hit was a false positive** and is shown rather than
waved away: the case-insensitive pattern matched the substring `s_e`
inside `basis_elements` on line 98 of the Phase-A freeze —

    ","T"],"basis_elements":[{"

A case-sensitive search for `S_E` returns **0 in all three files**.

**Confirmed: the pinned material contains no Euclidean action, no free
or kinetic part, and no exponent mapping.** This is the part of the
ruling's basis that is strongest — it is a null result about text, and
it is complete.

### 1.2 `P2-GAP-01` works from the singlet-only form — CONFIRMED

`derivations/P2-GAP-01_gap_criticality.md`, **lines 42–44**:

    combinatorial prefactor of the gap equation is exactly `2`. (In the alternative
    "NJL" normalization `L_int = G_N(ψ̄ψ)²`, one has `G = 4 G_N` and the gap
    equation reads `1 = 8 G_N B`; the physics — the value of `I_0` and the ratio of

and **line 27**:

    See `CONVENTIONS.md`. Euclidean `d=4`; attractive scalar (`ψ̄ψ`) channel;

**Confirmed exactly as stated**, including `G = 4 G_N`.

### 1.3 `P2-GAP-01` introduces a **real** scalar auxiliary — NOT LITERALLY WHAT THE MATERIAL SAYS

This is the one I want the Reviewer to look at.

**What the note actually says**, lines 32–33:

    Mean-field (Hubbard–Stratonovich) treatment of the attractive scalar-channel
    four-fermion interaction. Introducing the scalar auxiliary `Σ` (the dynamical
    self-energy), the gap equation is the tadpole self-consistency

**The word "real" does not appear in the note. Anywhere.** Nor does
"imaginary", "complex", or "contour":

    real 0      imaginary 0      complex 0      contour 0

So the phrase in the ruling — "introduces a **real** scalar auxiliary
field `Σ`" — is **the PI's characterisation, not the gate's wording.**

**Σ's reality is nonetheless established, by usage rather than by
declaration**, and the usage is unambiguous:

- line 15–16: `V(Σ)` is a "mean-field effective potential" for the
  "scalar self-energy `Σ`" that "first develops a nontrivial stationary
  point" — a real-variable potential picture;
- line 58: `D = p² + Σ²` — a positive-definite propagator denominator;
- line 73: `D = Σ_μ sin²p_μ + (W(p)+Σ)²` — `Σ` added directly to the
  real Wilson term `W(p)`, i.e. used as a real mass;
- line 47: "A nontrivial solution `Σ ≠ 0` bifurcates from `Σ = 0`";
- lines 61, 67: `I_0^cont = Λ²/(16π²)` and `G_c^cont = 8π²/Λ²`, both
  real and positive.

**I did not stop.** The verification A2 asks for is that the gate
introduces a real scalar auxiliary; it does introduce a scalar auxiliary,
and that auxiliary is real throughout its use. The gap between "stated"
and "used" is real but narrow, and halting would have delivered nothing
while the substance holds. **It is reported here as a first-class
finding rather than absorbed**, and §7 sets out what it costs the ruling
— together with a route that does not depend on it at all.

## 2. A1 — pinned inputs

Read from the git objects at the evidence base. All three matched; no
STOP.

    derivations/P2-GAP-01_gap_criticality.md
      17b6f613ffefb79fae8c0a5c40e3bd67ad31a101112af615945647e143fade00   MATCH
    derivations/CANONICAL_INTERACTION.md
      27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81   MATCH
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
      fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a   MATCH

## 3. A3 and A4 — the two entries, quoted in full

Both `§0` and `§1` are reproduced **verbatim** inside their entries,
verified by `diff` against the specification: the §0 blockquote is 36
lines and identical; the §1 blockquote is 17 lines and identical.

### 3.1 Entry one, as landed

    ## 2026-08-08 — Euclidean exponent mapping: the canonical interaction is written in the exponent
    
    Date: 2026-08-08
    Decision owner: Principal Investigator
    Effect: supplies a convention absent from the frozen material
    
    ### Decision
    
    The PI ruling of 2026-08-08, reproduced verbatim:
    
    > **PI ruling, 2026-08-08 — Euclidean exponent mapping.**
    >
    > The canonical interaction expression
    >
    >     X = (G/(2N)) * Sum( bilinear(lam(A), Id4)**2
    >                       + bilinear(lam(A), I*gamma5)**2, (A, 0, N**2-1) )
    >
    > is written **as it appears in the Boltzmann exponent**. Equivalently,
    > it enters the Euclidean action with a minus sign:
    >
    >     exp(-S_E) contains exp(+X)        <=>        S_E = S_E,0 - X
    >
    > Consequently, for a channel whose coefficient in `X` is written
    > `c * J**2`, the Hubbard–Stratonovich coefficient is
    >
    >     g = +2c
    >
    > **Basis, stated exactly.** This is **NOT derived from the frozen
    > material.** The frozen material contains no Euclidean action, no free
    > or kinetic part, and no exponent mapping; the derivation that raised
    > this question searched for one and found none. The ruling is
    > **constrained by executed usage**: `P2-GAP-01` is a PASSed gate whose
    > mean-field treatment introduces a **real** scalar auxiliary field `Σ`,
    > which is admissible only when the scalar channel has `g > 0`. Under
    > the opposite mapping the scalar channel would give `g < 0` and that
    > gate's method would not be available.
    >
    > **This supplies a definition the frozen material never carried. It is
    > not a recovery of an original intent.**
    >
    > **Scope.** This ruling resolves the exponent mapping and nothing else.
    > It selects no Hubbard–Stratonovich channel — that remains `OPEN-AC-1`
    > and is the PI's. It freezes none of the three diquark-definition gaps
    > (`η`, particle–particle Grassmann ordering, diquark normalisation). It
    > reaches no conclusion about a composite vector. It does not by itself
    > re-run any withheld verdict.
    
    ### Reason
    
    The exponent mapping was identified as missing by the channel-character
    derivation, which searched the frozen material for it and found none,
    and therefore withheld two verdicts: `REAL-HS ADMISSIBILITY NOT DEFINED
    BY THE FROZEN MATERIAL` and `ATTRACTIVE/REPULSIVE NOT DEFINED BY THE
    FROZEN MATERIAL`. Both remain withheld until separately recomputed; this
    entry does not re-run them.
    
    The ruling is **constrained by executed usage** rather than derived.
    `P2-GAP-01` is a PASSed gate whose method requires the scalar channel to
    admit a real linear auxiliary field.
    
    **Not a recovery of an original intent** — no document ever stated the
    mapping, and the constraint fixes which of two conventions the programme
    has in fact been using, not which one was once intended.
    
    ### Consequences
    
    For any channel whose coefficient in `X` is `c`, the exponent-level
    Hubbard–Stratonovich coefficient is `g = +2c`. The withheld Layer-1b and
    Layer-2 verdicts of the channel-character derivation become computable;
    computing them is a separate authorized task and is not performed here.
    
    This ruling **selects no Hubbard-Stratonovich channel**. `OPEN-AC-1`
    remains open and is the PI's. The three diquark-definition gaps — `η`,
    the particle–particle Grassmann ordering, and the diquark normalisation
    — are untouched and remain unfrozen.
    
    No gate status changes. `P2-GAP-01` remains `PASS` and `P2-PHASE-01`
    remains `PROPOSED`.
    
    ### Related gate
    
    None. This ruling supplies a convention; it registers no gate and
    changes no gate status.
    
    ### Related branch and files
    
    `fix/exponent-mapping-ruling`;
    `DECISION_LOG.md`,
    `specs/2026-08-08T1634Z_exponent-mapping-ruling.md`.

### 3.2 Entry two, as landed

    ## 2026-08-08 — Open derivation item: generator-sum criticality is UNESTABLISHED
    
    Date: 2026-08-08
    Decision owner: Principal Investigator
    Effect: opens an unperformed derivation item
    
    ### Decision
    
    The open item, reproduced verbatim:
    
    > **Open derivation item — generator-sum criticality.**
    >
    > `P2-GAP-01` obtained `G_c = 1/(2·I_0)` working from the singlet-only
    > form `L_int = G_N (ψ̄ψ)²`, with `G = 4·G_N`. **The mean-field
    > combinatorics of the full U(N) generator-sum canonical interaction
    > have never been performed**, in that gate or since.
    >
    > **Status: UNESTABLISHED.** Whether `G_c = 1/(2·I_0)` transfers to the
    > canonical generator-sum interaction is not known. **`P2-GAP-01`'s PASS
    > stands for the form it computed**; this item concerns whether that
    > result may be lifted to the canonical form, and it may not be assumed.
    >
    > **Not implied by the exponent ruling.** That `P2-GAP-01`'s real-`Σ`
    > usage constrains the exponent mapping says nothing about whether its
    > `G_c` applies to the generator-sum form. **Treating HS contour
    > consistency as evidence for a gap equation would conflate a convention
    > with a derivation.**
    
    ### Reason
    
    The canonical interaction designated by `CANONICAL_INTERACTION.md` §2 is
    the U(N) generator-sum form `(G/2N) Σ_A [S^A² + P^A²]`. `P2-GAP-01`
    computed its critical coupling from the singlet-only NJL form
    `L_int = G_N(ψ̄ψ)²`. Those are different interactions: the generator sum
    carries `N²` internal channels where the singlet-only form carries one,
    and the mean-field combinatorics that produce the gap equation's
    prefactor have never been carried out for it.
    
    The question this item opens is narrow and dynamical: **does
    `G_c = 1/(2·I_0)` survive the change of interaction?** It is a
    derivation, not a convention, and no ruling can settle it.
    
    ### Consequences
    
    `G_c = 1/(2·I_0)` may not be quoted for the canonical generator-sum
    interaction until the derivation is performed. It remains quotable for
    the form `P2-GAP-01` actually computed.
    
    **`P2-GAP-01`'s gate entry is not edited and its `PASS` is not
    qualified.** The gate passed for the interaction it computed, and that
    remains true; this item records a question about lifting the result, not
    a doubt about it.
    
    Stated once without markup, so the record carries the sentence plainly:
    P2-GAP-01's PASS stands for the form it computed.
    
    ### Related gate
    
    `P2-GAP-01`, whose status is unchanged at `PASS`. This entry registers no
    gate and changes no gate status.
    
    ### Related branch and files
    
    `fix/exponent-mapping-ruling`;
    `DECISION_LOG.md`,
    `specs/2026-08-08T1634Z_exponent-mapping-ruling.md`.

## 4. A5 — append-only, proved two ways

    $ git diff --stat 481f4ad7… HEAD -- DECISION_LOG.md
     DECISION_LOG.md | 157 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
     1 file changed, 157 insertions(+)

    $ git diff --numstat -- DECISION_LOG.md
    157	0	DECISION_LOG.md          (added  deleted  path)

    hunk header:  @@ -1232,3 +1232,160 @@
    lines beginning with a single '-':  0

**Zero deleted lines.** The single hunk starts at line 1232 of a
1234-line file and only adds, which is the signature of a pure append.

A second, stronger check — the base blob compared byte-for-byte against
the head of the new file:

    $ git cat-file blob 481f4ad7…:DECISION_LOG.md > base.txt
    $ head -c $(stat -c%s base.txt) DECISION_LOG.md | cmp - base.txt
    (no output)

**The previous file is a byte-exact prefix of the new one.** Nothing was
reordered, reflowed or silently rewritten anywhere above the append
point.

`DECISION_LOG.md` gained exactly two entries: 1234 lines → 1391 lines.

## 5. A3/A4 — the required exact phrases

Counted with `grep -c -F` over the whole file.

**A3, all eight present:**

    "Date: 2026-08-08"                                             2
    "Decision owner: Principal Investigator"                       6
    "Effect: supplies a convention absent from the frozen material" 1
    "Not a recovery of an original intent"                         1
    "S_E = S_E,0 - X"                                              1
    "g = +2c"                                                      2
    "constrained by executed usage"                                2
    "selects no Hubbard-Stratonovich channel"                      1

**A4, all three present:**

    "Status: UNESTABLISHED"                                        1
    "P2-GAP-01's PASS stands for the form it computed"             1
    "Not implied by the exponent ruling"                           1

**Two of these required a placement decision, and it is a
`SPECIFICATION_DEFECT` I had to resolve — see §8, Stop 1.** The verbatim
§0 and §1 text *cannot* contain two of the required strings:

- §0 writes "It is **not a recovery of an original intent.**" — lower
  case `not`, and line-wrapped after "It is";
- §1 writes "**`P2-GAP-01`'s PASS stands for the form it computed**" —
  with **backticks** around the gate name and a line wrap after `PASS`.

So reproducing §0 and §1 verbatim, as A3 and A4 require, guarantees that
neither exact phrase appears inside the blockquote. Both criteria cannot
be satisfied in the same block of text.

**Resolution used:** A3 states that "the structural metadata that format
requires may be added around it", so both phrases were placed in the
surrounding prose of their own entries, unwrapped and without markup, in
the `### Reason` and `### Consequences` sections. Entry two carries the
line

    Stated once without markup, so the record carries the sentence plainly:
    P2-GAP-01's PASS stands for the form it computed.

which says why it is there. The verbatim blockquotes were **not** altered
to make a grep pass — that would have broken the verbatim requirement,
which is the more important of the two.

## 6. Do the two entries read independently?

**Yes, and I checked this by reading them cold rather than by
construction.** In my own words, having read entry two first, as a
stranger arriving at the bottom of the log would:

Entry two names its own subject in its heading — "generator-sum
criticality is UNESTABLISHED" — and its `### Decision` block opens by
stating what `P2-GAP-01` computed (`G_c = 1/(2·I_0)` from
`L_int = G_N(ψ̄ψ)²` with `G = 4·G_N`) before saying what is unknown.
**A reader needs nothing from entry one to understand it.** Its
`### Reason` explains the physics gap — the generator sum carries `N²`
internal channels where the singlet-only form carries one, and the
mean-field combinatorics were never done for it — without invoking the
exponent mapping at all. The only mention of the ruling is the sentence
saying it does **not** imply this item, which is a disclaimer, not a
dependency.

Reading entry one alone: it ends at its own `### Related gate` and
`### Related branch and files` sections and never gestures at an
outstanding qualification. Its `### Consequences` say what becomes
computable and what stays open — `OPEN-AC-1`, the three diquark gaps —
and generator-sum criticality is not among them. **A reader of entry one
would not come away expecting a caveat**, because none is implied there.

The one thing that *could* mislead is that both entries carry the same
date and the same `Related branch and files`. I judged that acceptable:
they were landed by one task, which is a fact about provenance, not a
logical link. If the Reviewer disagrees, the fix is a one-line change to
entry two's provenance block.

**Neither entry is a subsection of the other.** Both are `##` top-level
headings at the same level as every other log entry; the only `##`
headings in the appended region are those two, everything between them
is `###`.

## 7. What in the ruling's basis I judge weaker than stated

The specification asks for this directly and says it is worth more than
a clean report. **Three things, in decreasing order of how much they
matter.**

### 7.1 "Real" is the PI's word, not the gate's — and the inference has two steps, not one

§1.3 above. The ruling says `P2-GAP-01` "introduces a **real** scalar
auxiliary field `Σ`, which is admissible only when the scalar channel
has `g > 0`". Unpacking that, it is two inferential steps:

1. **`Σ` is real.** Not declared; established by usage (`D = p² + Σ²`,
   `W(p)+Σ`, a real `V(Σ)` with a stationary point, a real positive
   `G_c`). Solid, but usage.
2. **The route was the standard linear HS identity.** The note calls its
   treatment "(Hubbard–Stratonovich)" in one parenthesis and then
   **never writes the identity, never writes an exponent, and never
   writes an action.** It goes straight to the gap equation
   `Σ = 2G·Σ·B(Σ)`. So the claim "a real `Σ` requires `g > 0`" is a
   claim about a step the note does not display.

Neither step is doubtful. But "constrained by executed usage" is doing
more work than the phrase suggests: it is constrained by *usage of a
step that was not written down*, inferred from the shape of the result.

### 7.2 A firmer route exists, and I would put it in the ruling

**The sign of `G_c` discriminates the mapping without needing `Σ`'s
reality at all.**

`P2-GAP-01` reports `1 = 2 G_c I_0` with `I_0 = Λ²/(16π²) > 0`, giving
`G_c = +8π²/Λ² > 0`, under the convention `G > 0` = attractive. Had the
interaction entered the exponent with the opposite sign, the mean-field
bifurcation condition would have carried the opposite sign and the
critical coupling would have come out **negative** — which is not what
the gate computed, and not consistent with `G > 0` being the attractive
direction.

That argument uses only numbers the gate published, no undeclared
adjective, and no unwritten step. **It is not fully independent** — it
runs through the same executed calculation, so it is a second reading of
one gate rather than a second gate. But it does not depend on the word
"real", which is exactly the gap §7.1 identifies. **I would add it to
the ruling's basis**; it costs nothing and repairs the one soft joint.

### 7.3 The basis rests on a single gate, and that is a structural limit

Both routes go through `P2-GAP-01`. No second gate, and no frozen
document, constrains the mapping. If `P2-GAP-01` were ever found to have
used a non-standard mean-field route, the ruling's basis would go with
it — the ruling would still stand as a PI convention, but its
justification would be gone.

**The ruling is honest about this** — "NOT derived from the frozen
material", "supplies a definition the frozen material never carried",
"not a recovery of an original intent" — and I am not disputing the
ruling. I am recording that its evidential base is one gate wide, and
that this is a fact about the repository, not a defect in the ruling.

**What would strengthen it**, none of it in scope here: performing the
generator-sum mean-field derivation of entry two would exercise the same
mapping a second time; and recording the exponent mapping in
`CONVENTIONS.md`, where the other locked conventions live, would make it
findable by the next derivation that needs it rather than only by
reading `DECISION_LOG.md`.

## 8. A6, A7, A8-pre, A9

### 8.1 A6 — nothing else touched

Blob OIDs read from the objects at the evidence base:

    GATES.md                                            bd4820513217ae7e1c493328dc49536e69b8cfb8   IDENTICAL
    CONVENTIONS.md                                      2d4f735c55a14fdfc5d1031a58698a8ca075fbbd   IDENTICAL
    AGENTS.md                                           5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3   IDENTICAL
    pyproject.toml                                      9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4   IDENTICAL
    derivations/CANONICAL_INTERACTION.md                6e5d9e1bb7dffe67e7b9ada026b366ef0e10a2a9   IDENTICAL
    derivations/P2-GAP-01_gap_criticality.md            70b43834873aac435aaed24af70201a9a16b79b7   IDENTICAL
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md   0be773f6a52c759abd23438c66da6b43bca44930   IDENTICAL
    results/P2-CHANNEL-FREEZE/fierz_matrix.json         5c3d572ed3887df2ad5880d8b5d4d2ea903cfde8   IDENTICAL
    results/P2-CHANNEL-FREEZE/fierz_matrix.json.sha256  601a5db8871bd6bc2534a0a7aa33d7a70d8159cf   IDENTICAL

Checked at tree level, which covers every path beneath:

    scripts/   4e56b73ecba4f40688bfe1338d77c1641a6b1b5c   IDENTICAL
    results/   70d75be5b5dd18fc1fec0b8435ad425669466333   IDENTICAL
    tests/     f5eb78aaa6a4413a41dab445869800fab4ec6d38   IDENTICAL

**`P2-GAP-01`'s gate entry is unedited and its `PASS` is not qualified**,
read from the merged tree:

    ## P2-GAP-01 — Gap-equation criticality (continuum + lattice)

    Status: PASS (continuum exact; lattice `I_0` agrees with paper at matched mass)

`derivations/CANONICAL_INTERACTION.md` is unchanged and its DRAFT banner
is untouched.

### 8.2 A7 — scope

Manifest template, `{PUSHED_HEAD}` placeholder so the digest does not
depend on the report commit. SHA-256:
`3bbd5cc4010f469524498e8f6e1bbdab02f46e40e44aef120768b4f8553eeeca`.

    {
      "base": "481f4ad77cb4ec92ef9d58471530784087e67a43",
      "head": "{PUSHED_HEAD}",
      "mode": "exact",
      "required": [
        {"operation": "add", "path": "specs/2026-08-08T1634Z_exponent-mapping-ruling.md"},
        {"operation": "add", "path": "reports/2026-08-08T1634Z_exponent-mapping-ruling.md"},
        {"operation": "modify", "path": "DECISION_LOG.md"}
      ],
      "optional": [],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

**2 additions and 1 modification**, matching A7. The `{HHMM}` token
resolved to `1634` at commit 1 and is reused. The resolved manifest, its
SHA-256 and the checker JSON at the pushed head are post-report evidence.

Pre-report check at `992e6001`, where the report commit does not yet
exist:

    $ python -m scripts.governance_tools.scope_checker --repo . --manifest <pre>
    {
      "base": "481f4ad77cb4ec92ef9d58471530784087e67a43",
      "failures": [],
      "head": "992e6001b029177976ecd7ce34a23492f549195f",
      "mode": "exact",
      "observed_operations": [
        {
          "operation": "modify",
          "path": "DECISION_LOG.md"
        },
        {
          "operation": "add",
          "path": "specs/2026-08-08T1634Z_exponent-mapping-ruling.md"
        }
      ],
      "overall": "PASS",
      "tool": "scope_checker"
    }
    === exit 0 ===

`failures` empty, and **`DECISION_LOG.md` is the only modification** —
which for this task is the criterion that matters, since every other
protected path must stand still.

### 8.3 A8-pre — four validators, at head `992e6001`

    $ python -m pytest tests/test_repository_structure.py   ->  4 passed              exit 0
    $ python -m pytest tests/test_si1_governance.py         -> 14 passed              exit 0
    $ python -m pytest tests/test_gate_anchors.py           -> 18 passed, 2 deselected exit 0
    $ python -m pytest tests/test_governance_tools.py       ->  8 passed              exit 0

All four exit 0, captured from `python -m pytest` itself and not from the
tail of a pipeline.

### 8.4 A9 — branch only

    refs/remotes/origin/main   481f4ad77cb4ec92ef9d58471530784087e67a43
    remote refs/heads/main     481f4ad77cb4ec92ef9d58471530784087e67a43
    local main                 0f7961747abe2a18b436c0b1e5b928f425ea4d9a  (stale by design)

**Local `main` was not repaired.** `fix/exponent-mapping-ruling` was
created from `481f4ad7…` in a separate worktree; the primary worktree was
not touched. **No branch was deleted or renamed.** No merge, no PR, no
force-push, no history rewrite.

## 9. Stops and clarifications

**Stop 1 — `SPECIFICATION_DEFECT`, resolved without halting.** A3 and A4
each require an exact phrase that the verbatim text they also require
**cannot contain**: §0 writes `not a recovery of an original intent`
with a lower-case `not` and a line wrap, and §1 writes
`` `P2-GAP-01`'s PASS stands for the form it computed `` with backticks
and a line wrap. Reproducing §0 and §1 verbatim therefore guarantees both
greps fail inside the blockquote.

**Resolution:** A3 explicitly permits structural metadata around the
verbatim text, so both phrases were placed in the entries' own
`### Reason` and `### Consequences` prose, unwrapped and unmarked. **The
verbatim blockquotes were not touched.** I did not halt because the
criteria are jointly satisfiable once "the entry must contain" is read as
"anywhere in the entry", which is what it says, and because altering the
verbatim text to satisfy a grep would have violated the more important
requirement. **Flagged for ruling**: if the intent was that the phrases
appear *inside* the quoted ruling, then §0 and §1 need rewording, not the
entries.

**Stop 2 — none.** A1 matched on all three pins, and A2's stop condition
is discussed at §1.3 and judged not to fire.

**Finding 1 — `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`, and the
substantive one.** The ruling's characterisation of `Σ` as **real** is
not the gate's wording; the word does not occur in
`P2-GAP-01_gap_criticality.md`. `Σ`'s reality is established by usage,
not declaration. §1.3 gives the evidence and §7.1 gives the cost. **The
ruling as landed is unchanged** — it is the PI's text, reproduced
verbatim, and this finding does not alter it.

**Finding 2 — secondary, an offered strengthening.** §7.2: the sign of
`G_c` discriminates the exponent mapping without relying on `Σ`'s
reality. Not independent of `P2-GAP-01`, but independent of the soft
joint. Offered for a future amendment, not applied.

**Finding 3 — secondary, placement.** The exponent mapping is a locked
convention in substance but lives only in `DECISION_LOG.md`.
`CONVENTIONS.md` is where the other locked conventions live and is where
the next derivation would look. Not moved: `CONVENTIONS.md` is on A6's
protected list and amending it is a separate authorization.

**Clarification 1 — no derivation note.** A0 states none is required
because no production code exists. I agree and produced none;
`AGENTS.md` rule 3 reads "Commit a derivation note before production
code", and there is no production code here.

**Clarification 2 — both entries share a provenance block.** §6. Same
date, same branch, same specification file. A provenance fact, not a
logical dependency, but noted since the specification is emphatic that
the entries must not read as linked.

## 10. Anything ambiguous, unsatisfiable, or that I would have specified differently

**One thing was unsatisfiable as literally written** — Stop 1 — and it
was satisfiable under the reading A3's own sentence supplies. Everything
else was met as written.

**(a) The exact-phrase lists should be checked against the verbatim text
they sit beside.** Two of eleven phrases could not appear where a reader
would most expect them. Generating the required-phrase list *from* the
verbatim source, rather than paraphrasing it, would remove the class of
defect entirely.

**(b) A2's third bullet should say "uses a real scalar auxiliary" rather
than "introduces a real scalar auxiliary field".** The distinction is
the whole of §1.3: the gate introduces an auxiliary and uses it as real.
Asking me to confirm the gate *says* something it does not say put me one
word away from a STOP on a point where the substance is sound.

**(c) I would specify where a convention of this kind lives.** Finding 3.
The ruling fixes a convention as load-bearing as any row of
`CONVENTIONS.md`, and it lands in a log that is chronological rather than
indexed.

One thing I would keep exactly as written: **the insistence that the
generator-sum item be a separate entry, with §1's explanation of why.**
The temptation to record it as a caveat is strong — it *feels* like a
qualification of a ruling that leans on `P2-GAP-01` — and the
specification's own sentence about conflating "HS contour consistency"
with "evidence for a gap equation" is exactly the error a caveat would
have baked into the record.

## 11. Commits, and commit-message hygiene

**Commit 1** — `628e9051fa51f0e4c6ce1411c525a7d2f2572728`

    spec: land the Euclidean exponent mapping ruling and open the criticality item

    Records the PI specification, evidence base
    481f4ad77cb4ec92ef9d58471530784087e67a43, transcribed verbatim.

    The task records two things and computes nothing. It lands the ruling
    that the canonical interaction expression is written as it appears in
    the Boltzmann exponent, so that g = +2c, supplying a convention the
    frozen material never carried. It separately opens the generator-sum
    criticality item as UNESTABLISHED, which the specification is emphatic
    must not be recorded as a caveat on the ruling: one is a convention, the
    other an unperformed derivation.

    No gate status changes, nothing frozen is modified, no
    Hubbard-Stratonovich channel is selected, and the withheld verdicts are
    not re-run here.

**Commit 2** — `992e6001b029177976ecd7ce34a23492f549195f`

    docs: record the exponent mapping ruling and the generator-sum item

    Two DECISION_LOG.md entries, appended. The file loses nothing: the
    previous content is a byte-exact prefix of the new one and the diff
    carries zero deleted lines.

    The first entry records the PI ruling that the canonical interaction
    expression is written as it appears in the Boltzmann exponent, so
    S_E = S_E,0 - X and g = +2c. Its basis is stated as constrained by
    executed usage rather than derived: the frozen material carries no
    Euclidean action, free part or exponent mapping, and P2-GAP-01's method
    requires the scalar channel to admit a real linear auxiliary field.

    The second entry opens the generator-sum criticality item as
    UNESTABLISHED. It is a separate top-level entry, not a subsection or
    caveat of the first, because the two answer different questions: one is
    a convention, the other an unperformed derivation. P2-GAP-01's gate
    entry is untouched and its PASS is not qualified.

    Both §0 and §1 are reproduced verbatim inside their entries; the exact
    phrases the specification requires are carried in the surrounding
    structural prose, where they can appear unwrapped and without markup.

**Intended report commit message** (commit 3):

    docs: report the exponent mapping ruling and the criticality item

    Records A1-A7 and A8-pre. Both DECISION_LOG.md entries are quoted in
    full, the append is proved twice over — zero deleted lines, and the
    base blob a byte-exact prefix — and all eleven required exact phrases
    are present.

    Reports one specification defect: two required phrases cannot occur
    inside the verbatim text that A3 and A4 also mandate, because the
    source wraps them and backticks a gate name. Resolved by placing them
    in the surrounding structural prose rather than altering the quotation.

    Reports that the ruling's characterisation of Sigma as real is the PI's
    word and not the gate's, established by usage rather than declaration,
    and offers a route through the sign of G_c that does not depend on it.

### Trailer suppression, per commit

The harness convention in this environment appends `Co-Authored-By:` and
`Claude-Session:` trailers. This specification permits neither. Both were
**actively suppressed** on every commit of this branch by composing the
message in a file and committing with `git commit -F`, never with `-m`.

    commit 1  628e9051   suppressed: Co-Authored-By, Claude-Session
    commit 2  992e6001   suppressed: Co-Authored-By, Claude-Session
    commit 3  (report)   suppression applied identically; stored message
                         read back as post-report evidence

Each proposed message was inspected before committing and each stored
message read back with `git log -1 --format=%B` after; a `grep` for
`co-authored-by`, `claude-session`, `claude.ai`, `generated with` and
`noreply@anthropic` matched nothing in either form, for both commits.

**Suppression is a fact disclosed here, not an absence** — a convention
that would have added the trailers was deliberately bypassed.

Author and committer identity (`Claude <noreply@anthropic.com>`) and the
SSH signature from the global `commit.gpgsign=true` are commit-object
headers, not message content, and are outside this specification's scope.
