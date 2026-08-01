# Review record — `P2-LATTICE-ONTOLOGY-01` concept specification

Artifact under review:
`concepts/P2-LATTICE-ONTOLOGY-01.md`
sha256 `1a03870eb5a24a748f3803e066a281dbbe4b64fa67860dad32409b41c0660b5c`
(landed on branch `programme/p2-lattice-ontology-01`, commit
`83eb0877ebcd13562fc95721cd1d2bf5dfe5a7da`)

Supporting non-canonical evidence:
`exploratory/euclidean_reconstruction.py`
sha256 `30e3b59a0006b2ecc2d6ecce391ab918ce9ba542b2af649c55570e0643e63a78`
Status: EXPLORATORY — not preregistered, not adopted, carries no
evidential weight for any gate verdict.

This record exists so that the registration of this gate rests on an
in-repository, hash-pinned review artifact rather than on assertions
made in a prompt or recalled from a session.

---

## 1. Review process

Adversarial multi-round review. Roles: PI (Zeta) holds sole
authorization; Claude acted as Discriminator (adversarial review,
independent verification, clean-clone audit); ChatGPT acted as parallel
reviewer; Codex acted as executor for all repository writes. No
reviewer performed git writes; the executor performed no review.

Rounds and outcomes, in order:

| Round | Reviewer | Verdict | Principal findings |
|---|---|---|---|
| 1 | Parallel reviewer | REQUEST CHANGES (4 blockers, 5 revisions) | freeze-list incompleteness; Hamiltonian/Euclidean ambiguity undeclared; finiteness claim too broad; reference/subtraction rule underspecified; falsification levels conflated |
| 2 | Parallel reviewer | REQUEST CHANGES (2 blockers, 5 revisions) | vacuum-selection claim too strong (C symmetry); three positivity/equivalence propositions conflated; table internally inconsistent; O(4) emergence unconditional; 10¹²⁰ presented as computed |
| 3 | Parallel reviewer | APPROVE (4 editorial fixes) | Bill 3 internal contradiction; occupancy wording; §1e completeness overclaim; probe epistemic status |
| 4 | Parallel reviewer | APPROVE (3 precision fixes) | vacuum-eigenvalue degeneracy; continuum-subtraction contrast overgeneralized; c=1/2 claim narrowed |
| 5 | Discriminator | APPROVE FOR REGISTRATION | content-level clean-clone audit of the landed artifact |

All accepted findings from rounds 1–4 were incorporated before the
artifact was pinned at the hash stated above.

## 2. Discriminator clean-clone audit (round 5)

Performed against a fresh clone of
`programme/p2-lattice-ontology-01` at head
`315451829412067f2e86d3559975e36b1b2ee03c`, not against a working copy.

- **Hash fidelity:** both artifact sha256 values reproduced from the
  clean clone and matched the executor's report byte for byte.
- **Residual-contradiction sweep (12 checks, all zero):** no surviving
  instance of any claim withdrawn during review — unconditional rest
  frame; "ontologically dynamical" header; Hamiltonian in the
  fundamental column; "prices Bill 2"; C-symmetry uniqueness of half
  filling; "symmetry-selected rather than energy-compared"; "nothing
  diverges"; single-level axis-independence deliverable; unhedged
  10¹²⁰; occupancy as a fundamental variable; blanket Wilson
  reflection-positivity; "correct c=1/2 critical content".
- **Commitment-presence sweep (16 checks, all present):** maximal-
  eigenvalue eigenspace rule; three-level axis deliverable; the
  bosonic-Ising non-transplantability warning; MICROSPEC delegation;
  "never determinative of"; candidate-mechanism framing for O(4);
  `ΔE[r₁] = ΔE[r₂]`; D0 blocking deliverable; anti-escape rule;
  non-operative alternative hypothesis; ratify-summary resolution;
  reference-equivalence-class rule; continuum-subtraction hedge;
  cosmological-source separation; Consumers section.
- **Structure:** §0 through §7 present and ordered; cross-references
  internally consistent.
- **Script re-execution from the clean clone:** transfer-matrix
  positivity True for all three tested coupling pairs; `log Z` equal
  between slicings to 0–7×10⁻¹⁵; `m₁L → 0.50`; `m₂/m₁ → 7.93`,
  consistent with the note's stated values.

**Discriminator verdict: APPROVE FOR REGISTRATION AS `SPECIFIED`** on
the pinned version. This is a REVIEW verdict, not the gate status
`PASS`; no gate-completion status is asserted or implied by this
record.

## 3. Scope of this approval (explicit limits)

This approval certifies that the specification is sufficiently
complete, internally consistent, and honestly bounded for registration
as `SPECIFIED`. It does NOT assert that the §1e delegated obligations
are discharged, and it does **not** certify:

- that the physical-substrate hypothesis is true;
- that the H(4) fermion action is reflection-positive (an open,
  per-operator obligation);
- that axis equivalence holds at levels 2–3 for the H(4) theory;
- that O(4) or Lorentz symmetry emerges (a candidate mechanism, to be
  demonstrated);
- that the vacuum-selection rule is unique or symmetry-determined;
- any physical coefficient whatsoever.

The exploratory probe illustrates the internal viability of the
Euclidean→Hamiltonian formulation in a finite 2D bosonic example. It
proves nothing about the target theory.

## 4. Known reviewer-error record (reliability data)

Errors made by the Discriminator during this review cycle and corrected
before the pinned version, recorded because no single reviewer is
sufficient: rank↔species conflation; over-extension of the 0.4%
transverse–longitudinal mixing datum; a 250× coefficient claim that
compared two different quantities; a locality-control range claimed
beyond what the canonical script executed; describing a 7% drift as
"constant"; an axis-independence test of wrong design (gap ratios
rather than partition function); a CFT ratio comment contradicted by
the data; the C-symmetry vacuum-uniqueness overclaim; conflation of
transfer-matrix positivity with OS reflection positivity.

Several of these were caught by the parallel reviewer executing the
scripts and comparing outputs against the prose. The governing lesson
is recorded: narrative must follow data, and claims must not exceed
what the canonical artifact executes.
