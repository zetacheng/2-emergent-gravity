# Task specification — land the Euclidean exponent mapping ruling and open the generator-sum criticality item

Specification evidence base: `481f4ad77cb4ec92ef9d58471530784087e67a43`

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**This task records two things and computes nothing.** It lands a PI
ruling that supplies a convention the frozen material never carried, and
it opens an unrelated derivation item that must not be folded into that
ruling's justification.

**No gate status changes.** `P2-GAP-01` remains `PASS`; `P2-PHASE-01`
remains `PROPOSED`. **Nothing frozen is modified.**

---

## 0. The ruling

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

## 1. The separate open item

**This is NOT a caveat on the ruling and must not be recorded as one.**
The two answer different questions:

- the ruling answers **with which sign `X` enters the exponent** — a
  convention;
- this item answers **whether the full generator-sum interaction
  reproduces the criticality of the singlet-only form** — an unperformed
  dynamical and combinatorial derivation.

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

## 2. Acceptance criteria

**A0 — Commit order.** Commit 1 is this specification under `specs/`.
Commit 2 carries `DECISION_LOG.md`. Commit 3 is the report. **No
derivation note is required**: this task performs no derivation, and
`AGENTS.md` rule 3 governs production code, of which there is none.
**Parent 1 of any commit is whatever you are standing on.**

**A1 — Pinned inputs**, verified before use; any mismatch is a STOP:

    derivations/P2-GAP-01_gap_criticality.md
    17b6f613ffefb79fae8c0a5c40e3bd67ad31a101112af615945647e143fade00

    derivations/CANONICAL_INTERACTION.md
    27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a

**A2 — Verify the basis, do not take it on trust.** Confirm from the
pinned material that:

- **no Euclidean action, free part, or exponent mapping is stated
  anywhere in it** — quote your search;
- **`P2-GAP-01` introduces a real scalar auxiliary field** — quote the
  line;
- **`P2-GAP-01` works from the singlet-only form** `L_int = G_N(ψ̄ψ)²`
  with `G = 4·G_N` — quote the line.

**If any of these is not what the material says, STOP and report.** The
ruling's basis rests on all three, and a PI ruling built on a
misdescription is worse than no ruling.

**A3 — Ruling recorded.** One `DECISION_LOG.md` entry in the file's
existing `## <date> — <title>` / `Date:` / `Decision owner:` / `Effect:`
/ `### Decision` / `### Reason` format.

**The SUBSTANTIVE RULING TEXT of §0 is reproduced verbatim within the
entry; the structural metadata that format requires may be added around
it.** §0 does not itself carry the log's scaffolding, so "verbatim"
governs the ruling's wording, not the entry's frame.

The entry must contain these exact factual phrases:

    Date: 2026-08-08
    Decision owner: Principal Investigator
    Effect: supplies a convention absent from the frozen material
    Not a recovery of an original intent
    S_E = S_E,0 - X
    g = +2c
    constrained by executed usage
    selects no Hubbard-Stratonovich channel

**A4 — Open item recorded, separately.** A second `DECISION_LOG.md`
entry — **not a subsection of the first** — whose substantive open-item
text reproduces §1 verbatim, with the log format's structural metadata
added around it as in A3. It must contain:

    Status: UNESTABLISHED
    P2-GAP-01's PASS stands for the form it computed
    Not implied by the exponent ruling

**The two entries must be independently readable.** A reader arriving at
the second must not need the first to understand what is unestablished,
and a reader of the first must not come away thinking the second is a
qualification of it.

**A5 — Append-only.** `DECISION_LOG.md` gains exactly two entries and
loses nothing. Verify by diff that the change contains **zero deleted
lines**.

**A6 — Nothing else touched.** `GATES.md`, `CONVENTIONS.md`,
`AGENTS.md`, `pyproject.toml`, `derivations/CANONICAL_INTERACTION.md`,
`derivations/P2-GAP-01_gap_criticality.md`, the Phase-A freeze,
`results/P2-CHANNEL-FREEZE/fierz_matrix.json` and its `.sha256`, and
every path under `scripts/`, `results/` and `tests/`: blob-identical to
the evidence base. **Read from the objects.**

**`P2-GAP-01`'s gate entry is not edited.** Its `PASS` stands. **Do not
add a caveat to it** — the open item lives in `DECISION_LOG.md`, and
amending a PASSed gate's text is a separate authorization this task does
not carry.

**A7 — Scope**, two additions and one modification:

    add:
      specs/2026-08-08T{HHMM}Z_exponent-mapping-ruling.md
      reports/2026-08-08T{HHMM}Z_exponent-mapping-ruling.md
    modify:
      DECISION_LOG.md
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 2 additions and 1 modification.** Report the
template, the resolved manifest, its SHA-256, and the checker JSON
including `observed_operations`.

**A8 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`. **A8-pre** at the pre-report head goes
in the report; **A8-final** at the pushed head is post-report evidence
and carries the verdict.

**A9 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to
`481f4ad77cb4ec92ef9d58471530784087e67a43`; create the branch from that
commit; move no `main` ref. **Local `main` is stale by design — do not
repair it.** Report all three. Push the task branch only. **Delete no
branch.**

## 3. Evidence layering

**Committed report:** A1–A7, A8-pre, the earlier commit SHAs and
messages, the pre-report head, the intended final manifest, and the
intended report commit message with its authoring-time trailer
suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A8-final, the push, the report
commit's stored message read back from the object, and ancestry
confirmation.

## 4. Invariants and prohibitions

- Executor-writable: the three paths of A7 only.
- **Do not re-run Layer 1b or Layer 2.** The ruling makes them
  computable; computing them is a separate authorized task. **Do not
  anticipate their results in the report.**
- **Do not select a Hubbard–Stratonovich channel**, and do not freeze
  `η`, the particle–particle Grassmann ordering, or the diquark
  normalisation.
- **Do not edit `P2-GAP-01`'s gate entry or derivation**, and do not
  qualify its `PASS`.
- **Do not record the generator-sum item as a caveat, footnote, or
  subsection of the ruling.** Separate entries; §1 explains why.
- **Do not modify `CANONICAL_INTERACTION.md`** or remove its banner.
- Commit-message hygiene: inspect the proposed message before each
  commit and the stored message after; permit no `Co-Authored-By`, no
  session identifier or URL, no tool attribution. **Report per commit
  whether any trailer was suppressed and which — an authoring-time
  suppression is a fact to disclose, not an absence.**
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: use `fix/exponent-mapping-ruling`.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 5. Report contract

- raw output for A1–A8, scope-checker JSON verbatim including
  `observed_operations`;
- the three A2 verifications with their quoted material;
- both `DECISION_LOG.md` entries quoted in full;
- the diff proving zero deleted lines;
- **whether the two entries read independently** — say so in your own
  words, having read them as a stranger would;
- **anything in the ruling's basis you judge weaker than stated.** The
  ruling rests on inference from one gate's method, not on a frozen
  definition; **if that inference looks thinner to you than it does to
  us, that is worth more than a clean report**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
