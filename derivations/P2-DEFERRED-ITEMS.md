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
