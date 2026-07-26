# CANONICAL_INTERACTION.md — DRAFT v0.5 (ratification candidate)

**Status: DRAFT v0.5 — ratification candidate under the Discriminator's
CONDITIONAL APPROVAL (2026-07-25). Editorial items from that ruling are
applied; landing requires the §5 executor evidence table to pass in
full. Pending: Discriminator confirmation → PI
approval → executor landing WITH the §5 evidence table. Nothing here has
governing force until the ratification record replaces this banner.**

---

## §1 — Fundamental postulate (the microscopic layer)

The programme postulates a discrete fermionic microscopic substrate,
provisionally represented by a Planck-scale lattice (spacing `a ~ ℓ_P`,
cutoff `Λ ~ a⁻¹`) with local hopping. The N low-energy modes are
hypothesized to be realizations of a common underlying fermionic object
and are represented operatively as components of one internal multiplet.
**This physical picture motivates, but does not derive, the U(N)
structure adopted in §2** — the exact U(N) choice is an axiom of §2, not
a consequence of the single-object picture.

No specific vacuum orientation is fixed by this document. In particular,
the historically explored **purely imaginary vacuum is non-operative**:
it was abandoned when its proposed stationary point was found not to be
the physical minimum. The canonical interaction below is fully decoupled
from that historical interpretation.

This layer is a **postulate**. No derivation from §1 to §2 is claimed
(§4).

## §2 — Operative canonical interaction (the working layer)

The interaction **designated** as the unique operative canonical
interaction governing Paper 2 and its registered downstream derivations
is the **U(N) chiral NJL interaction**
(generator-sum form), stated with the complete contraction:

Fields: `ψ_{aα}(x)` — Dirac index `α = 1…4`; internal index `a = 1…N`
labelling the N modes, which carry a **U(N) internal structure** (the
modes rotate into one another; they are not inert copies). `ψ̄ = ψ†γ⁰`.
Internal generators `λ^A`, `A = 0 … N²−1`, normalized
`Tr[λ^A λ^B] = 2δ^{AB}`, with the singlet `λ⁰ = √(2/N)·1_N`.
Gamma-matrix and further conventions: `CONVENTIONS.md` (Paper 2) and the
convention-lock section of the Paper-3 derivation note
`derivations/u3-fierz/u3_fierz.md` at the pinned Paper-3 commit (§5) —
these two sources are consistent (§7(b)).

Bilinears (every contraction explicit):

    S^A(x) ≡ Σ_{a,b=1}^{N} Σ_{α,β=1}^{4} ψ̄_{aα}(x) (λ^A)_{ab} (1)_{αβ} ψ_{bβ}(x)
    P^A(x) ≡ Σ_{a,b=1}^{N} Σ_{α,β=1}^{4} ψ̄_{aα}(x) (λ^A)_{ab} (iγ₅)_{αβ} ψ_{bβ}(x)

The canonical action:

    L = Σ_{a=1}^{N} ψ̄_a (iγ^μ ∂_μ) ψ_a
        + (G / 2N) Σ_{A=0}^{N²−1} [ S^A(x)² + P^A(x)² ]

with:
- `G > 0` — the **single independent coupling of the operative canonical
  four-fermion interaction** (attractive in the scalar channel under the
  registered convention; §7(b));
- the `1/N` prefactor defining the large-N limit; `N` kept symbolic in
  all algebra;
- classical symmetry `U(N)_L × U(N)_R`; the anomalous breaking of the
  axial `U(1)_A` is **not** part of this canonical interaction and is
  governed by its own records (§7(e)).

**Superseded shorthand (recorded):** the Paper-2 manuscript's `L0`
(`paper/emergent_gr_paper_v2_15.tex` L238–271) writes the singlet-only
pair `(Σ_a ψ̄_aψ_a)² + (Σ_a ψ̄_a iγ₅ψ_a)²`. As literally written this is
a *different* interaction (direct singlet channel only; incomplete chiral
symmetry). It is hereby recorded as **imprecise shorthand** for the
generator-sum form above, superseded by this document. The designation is
forced jointly by: the PI's physical picture (§1); the completeness of
the chiral symmetry; and the fact that the programme result recorded as VERIFIED, subject to §5
evidence confirmation, is derived from the generator-sum form.

## §3 — Operative canonical coordinates

**Operative coordinates of the canonical four-fermion theory (exhaustive
within the present Paper-2 axiom):**

| coordinate | nature |
|---|---|
| `G` | the single independent coupling of the operative canonical four-fermion interaction, `G > 0` |
| `N` | internal multiplicity — a model symbol (integer), symbolic in all algebra |
| `Λ = a⁻¹` | regulator/cutoff scale used by the operative effective theory |

**Scope of this table:** it is exhaustive only for the operative
four-fermion theory of §2. It is NOT a claim that a future microscopic
lattice completion possesses no additional UV parameters (hopping
coefficients, link/bond stiffness, graph parameters, regulator kernels,
or the UV combination that produces `G` are all open questions of the
PM-0007 line).

**Dimensional note:** in four spacetime dimensions `[G] = −2` (mass
dimension); dimensionless comparisons are expressed through a declared
combination such as `GΛ²`, without promoting it to an additional
independent coupling. `Λ` is not an independently adjustable
interaction-channel coupling; any numerical scan involving `Λ` must be
identified as regulator or scale analysis, never as enlargement of the
microscopic channel space.

**Not free parameters:** vector, axial, and tensor structures carry no
independent couplings in the operative theory. Whatever appears in those
channels arises only as Fierz images of the canonical interaction and/or
radiatively induced structures — computed, never chosen. The recorded instance, subject to §5 evidence confirmation: the
vector-singlet Fierz image `G_ω = −G/N` (repulsive), claim `P3-C-001`
(§5).

**Rejected alternative (recorded):** the manuscript's `Lgen` — an
independent coupling per Dirac channel — is a multi-coupling theory
family, not this theory. Promoting any channel coefficient to an
independent coupling is a theory **extension** (AE-4), never a
reinterpretation.

## §4 — Epistemic status (honest layer separation)

The canonical interaction of §2 is, at the current programme stage, a
**POSTULATED AXIOM** — not a derived result. The lattice-origin
derivation (hopping/bond → effective four-fermion; whether it yields §2
uniquely and fixes all channel ratios) is an open research objective:
recorded as brainstorming candidate `PM-0007` in `0-programme` (Level-5
taxonomy; quaternionic sub-direction), with the registry-gate name
`P2-HOPPING-4F-01` **reserved but not yet registered** (§7(d)). No
document or prompt may describe §2 as "derived from the lattice."

**Falsification clause:** if that derivation is one day completed and
yields an interaction different from §2, the derivation wins — §2 is
falsified as an axiom and amended through the full chain. The derivation
owes no loyalty to this document.

## §5 — Paper-3 consistency record (verified at landing; evidence: reports/2026-07-25_canonical-interaction_evidence.md)

The Paper-3 derivation note `derivations/u3-fierz/u3_fierz.md` (Paper-3
commit `8c363ef08368f5c022278ea5f36e01496be3d5ca`) takes as its starting
interaction **exactly the generator-sum form of §2** (at N=3), locks its
conventions before computation, re-derives the Fierz table from the
16-dim Dirac completeness relation, and obtains the vector-singlet
coefficient `G_ω = −G/N` (repulsive; ω survives screening) — claim
`P3-C-001`, status **VERIFIED** (mutation-tested anchors, clean-room
reproduction, 12/12 tests). Consequences:

1. the §7(c) provenance check **passes**: `G_ω = −G/N` is Fierz-derived
   from the canonical interaction, not independently postulated;
2. Paper 3's pinned analytic vector input (the Phase-A §E path) connects
   to this canonical statement **without adjudication**;
3. scope unchanged: Paper 3 pins the vector coupling, sign, and
   pole/screening conventions; the vector channel's contribution to the
   mixed gravitational kernel remains an SI-2 computation.

**Evidence requirement for ratification:** the statements above are
assertions about repository content. Before ratification, the executor
must generate and attach an evidence table on a clean clone: (starting
interaction matches §2 → file path + line range + pinned SHA);
(normalizations match → exact quoted definitions); (`G_ω = −G/N` →
derivation equation reference); (claim status VERIFIED → registry path +
entry); (test count → command + output digest); (convention
compatibility → explicit comparison table). The Discriminator's approval
of this document is conditional on that evidence table; self-description
is not evidence.

**Attribution guard (recorded for honesty):** the betaV campaign's
INCONCLUSIVE verdicts are attributable to the numerical instability of
the historical eps-extrapolation estimator, **not** to the
singlet-vs-generator-sum distinction. The interaction designation fixes
what SI-1/SI-2 must enumerate and sum; it does not retroactively explain,
excuse, or repair any recorded numerical result.

## §6 — Governing-source clause and supersession

**This document is the unique governing source for Paper-2
canonical-interaction algebra and its registered descendants.** All prompts, freeze documents, and derivations quote the
interaction from this file (path + file sha256), never from any
manuscript. It supersedes every historical wording, including the
December-2025 unified manuscript's scalar-only `S0` and the Paper-2
manuscript's `Lgen`/`L0` presentation. Manuscripts remain living expository documents with no governing force
over the algebra. Historical formulations are preserved as development
records; **where their literal algebra differs from the ratified
canonical interaction, they are non-operative and require expository
alignment** — no historical expression may override the governing source.
**Mandatory manuscript-alignment action:** ratification of this
designation creates a required Paper-2 action — the manuscript's
presentation must be amended to display the generator-sum interaction
explicitly, or to state unambiguously that its singlet notation is
shorthand for the complete generator contraction. This action is tracked
from ratification until the manuscript is aligned; at landing, the
executor creates the tracking item under the repository's existing
action/gate format (e.g. a named entry of the form
`P2-ACT-CANONICAL-ALIGN-01` — this example does not reserve or register
the identifier), following existing governance conventions rather than a
format invented by this document. Amendments to this document go through the full chain with a
version bump and recorded reason; silent edits are prohibited.

## §7 — Resolution record (2026-07-25; supersedes v0.1's open items)

**(a) Internal structure — RESOLVED: generator-sum (U(N)).** PI's
physical rationale: all fermions descend from one fundamental object; the
N modes are its variants and rotate into one another. Consistency
rationale: the programme's only VERIFIED Fierz result is derived from
this form; the singlet-only reading would sever the Paper-3 vector input.
The manuscript's "condensate multiplicity, not flavor species" phrasing
is retained as interpretation (the N modes are not Standard-Model
flavors) and is compatible with the U(N) structure.

**(b) Sign/normalization audit — VERIFIED (landing evidence table, row 6).** `G > 0` = scalar-channel
attraction is consistent across Paper-2 `CONVENTIONS.md` and the Paper-3
convention lock (mostly-minus Minkowski quotations; Euclidean Clifford
algebra for Fierz numbers — pure algebraic ratios, signature-independent;
pseudoscalar bilinear `iγ₅`; classification `G_V < 0` repulsive/ω
survives). No sign-convention collision found.

**(c) Paper-3 provenance — VERIFIED (landing evidence table, rows 1–5).** See §5.

**(d) Gate registration — DEFERRED.** `P2-HOPPING-4F-01` name reserved;
the UV programme is recorded as `PM-0007` in `0-programme`; registration
as a registry gate happens through governance when the research line
produces its first concrete model.

**(e) U(1)_A breaking term — SEPARATED.** No U(1)_A-breaking operator is
part of the canonical interaction defined in §2. Any anomaly term,
explicit breaking term, topological potential, or regulator-induced
contribution belongs to a separately governed research record
(`U1A_BREAKING_CANDIDATES` note, HYPOTHESIS class) and must not be
inserted into the canonical interaction without a full-chain amendment.
No candidate mechanism is selected here.

## Change log (v0.2 → v0.3, per the Discriminator's REVISE ruling)

1. §1: purely-imaginary-vacuum phrase removed; explicit non-operative
   statement added; single-object picture demoted to motivation
   (Blocker 1, Major 4).
2. §3: retitled "Operative canonical coordinates"; `G` restated as the
   operative canonical coupling; UV-completion disclaimer, `[G] = −2`
   note, and Λ-scan wording added (Blocker 2, Minors 2–3).
3. §5: ratification-time executor evidence table required; assertions no
   longer self-certifying (Major 5).
4. §6: governing scope limited; manuscript-alignment action made
   mandatory; historical-wording clause tightened (Minors 1, 4, 5).
5. §7(e): speculative U(1)_A content moved to a separate
   HYPOTHESIS-class note; minimal separation statement retained
   (Major 3).

## Change log (v0.3 → v0.4)

1. §2: "single genuine microscopic coupling" → "single independent
   coupling of the operative canonical four-fermion interaction" (the
   surviving blocker). *(v0.3's change log wrongly claimed this was
   already fixed; corrected here.)*
2. §2: "unique" recast as governance designation.
3. §5 title and §7(b)/(c): "verified" → verification pending
   ratification evidence.
4. §6: alignment tracking item to be created by the executor under
   existing governance format.

## Change log (v0.4 → v0.5, editorial per CONDITIONAL APPROVAL)

1. Change-log numbering repaired (three v0.3 items were misfiled under
   v0.4; logs now correctly partitioned).
2. §2/§3 residual "VERIFIED" phrasings aligned to
   "recorded as VERIFIED, subject to §5 evidence confirmation".
3. §6 action-ID example marked as non-reserving.
4. Ratification-record template adjusted for the self-reference rule
   (see below).

---

*Ratification record (completed at landing): Discriminator review:
CONDITIONAL APPROVAL issued 2026-07-25; conditions satisfied by the
clean-clone §5 evidence table (see the landing report). PI approval:
Zeta Cheng, PI / 2026-07-25 (the PI's authorization of the landing). Per the
self-reference rule, the landing commit SHA and this file's final sha256
are recorded in the landing report and the tracking entries, never
inside this file.*
