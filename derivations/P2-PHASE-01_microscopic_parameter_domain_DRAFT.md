# `P2-PHASE-01` microscopic parameter domain — DRAFT, NOT ADOPTED

**SUPERSEDED.** Adopted as
`derivations/P2-PHASE-01_microscopic_parameter_domain.md`. This file
is retained as historical evidence and is not operative.

## Status and evidence boundary

This is a **DRAFT, NOT ADOPTED** prerequisite artifact.  It does not define
or adopt a microscopic parameter domain, and `P2-PHASE-01` remains
`PROPOSED`.  It records only questions and numerical observations already in
the integrated exploratory scalar study,
`reports/2026-08-05_p2-phase-01_scalar-stationary-exploratory.md`, and in its
machine companion,
`results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json`.

## Frozen coordinate information

The Phase-A freeze identifies `G` as the one genuine scan-eligible microscopic
coordinate (`interaction_coordinate_rank = 1`).  It classifies `HS_scale` and
`Fierz_basis` as auxiliary representation parameters, not scan-eligible
coordinates.  Source: `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`,
§B and §D.  This draft does not alter that freeze or add a coordinate.

## Exploratory observations relevant to a later domain decision

The integrated scalar study is the declared `mu = 0` slice, not the full
finite-density scope of `P2-PHASE-01`.  It reports its outputs naturally as
the dimensionless ratio `G/Gc` and lattice mass `Mhat = aM`; it introduces no
dimensionful scan range.  The future adopted artifact must decide how `a` is
treated (for example, as an externally matched quantity or a declared fixed
input); this draft makes neither choice.

Across the six grid/offset controls (`n = 32, 40, 48`, shifts `0` and `0.25`),
the integrated report gives `I0(0)` from `0.08532107` to `0.08538273` and `Gc`
from `5.85598486` to `5.86021696`.  It therefore reports only the stable
scales `I0(0) ~= 0.0854` and `Gc ~= 5.86`; further digits are finite-grid
values.  The reported `Mhat = 1` crossing ranges from `G/Gc = 1.768341` to
`1.769619`, with stable scale `G/Gc ~= 1.77`.  That crossing is an observation,
not a bound.

The scalar report also establishes that simple `Mhat -> -Mhat` reflection is
not a symmetry of the Wilson functional, while recording the Wilson-complement
relation `I0(Mhat) = I0(-8-Mhat)`.  The mass axis is therefore not featureless.
Sources for all numerical statements in this section are the integrated report
§§A1--A2 and A5--A7 and its JSON companion named above.

## Decisions retained as OPEN

### OPEN-PD-1  Whether Mhat = 1 is a domain bound

**OPEN.** The scalar study observes the crossing near `G/Gc ~= 1.77`; it does
not supply an admissibility criterion or a domain bound.

### OPEN-PD-2  Whether the domain extends below Gc

**OPEN.** The integrated report contains stationary scalar roots below `Gc`.
Whether that fact places subcritical couplings inside an adopted domain is a
future decision, not an inference of this draft.

### OPEN-PD-3  Whether the negative-mass branch is included

**OPEN.** The reported algebraic branches include negative `Mhat` roots, but
the study neither classifies them as physical phases nor excludes them.

### OPEN-PD-4  Finite density: scan dimension or fixed input

**OPEN.** This evidence is restricted to `mu = 0`; `P2-PHASE-01`'s scope in
`GATES.md` includes finite density / `mu`.  A future adopted artifact must
decide whether `mu` is a scan dimension or a fixed input and, if it is scanned,
freeze its range.

### OPEN-PD-5  Treatment of the lattice spacing a

**OPEN.** This draft records `Mhat = aM` only as the reported lattice-unit mass.
It does not decide whether `a` is fixed by external matching, supplied as a
fixed input, or treated otherwise.

## Non-adoption statement

No range, bound, domain membership, finite-density prescription, or
admissibility condition is adopted by this draft.
