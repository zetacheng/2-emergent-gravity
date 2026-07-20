# Provenance search — Finding 5 lattice pipeline (`P2-BETAV-CIRC-01`)

**Question.** Can the exact historical artifact that produced Paper 2 Finding 5's
`β_V/β_B = −3.2(5)` (eq. `betaVlat`) be located, so that its
projection/normalization can be exercised for the circularity test?

**Date:** 2026-07-19. **Base:** `main = e21f81e`, branch `gate/p2-betav-circ`.

## What was searched

1. **The value itself** — `grep -rniE '3\.2\(5\)|-3\.2|7\.2|betaVlat|beta_?V'`
   across all `*.py`, `*.md`, `*.tex`, `*.json`.
2. **The machinery the gate stub says is required** — lattice vector/1-form
   operator, Stueckelberg/compensating scalar determinant, metric perturbation,
   `h`-derivative / graviton projection, per-species normalization:
   `grep -rniE 'proca|stueckelberg|1-form|log ?det|logdet|det.*Delta|h-deriv|
   graviton|metric.*perturb|forward diff|Sherman|eigenvalue struct|g\^-1|sqrt.g'`
   over `scripts/`, plus `grep -rniE 'linalg|det\(|eigval|eigh|slogdet'`.
3. **Legacy / provenance pointers** — `MIGRATION.md`, a repository-wide search
   for any `PROVENANCE*` file, and the paper's own reproducibility / code
   availability text in `paper/emergent_gr_paper_v2_15.tex`.

## What exists

- `β_V/β_B = −3.2(5)` appears **only** in `paper/emergent_gr_paper_v2_15.tex`
  (eq. `betaVlat`, line 1309; `β_V = −7.2e-4`, line 1307) and in this
  repository's own *commentary* about it (`derivations/betav_discriminating_power.md`,
  `scripts/betav_discriminating.py`, `reviews/claude/2026-07-19-paper2-followup.md`,
  `results/comparison/PAPER_COMPARISON.md`).
- The only `numpy.linalg` call in `scripts/` is `lstsq` in
  `scripts/lattice_beta_scan.py` — the **scalar** `P2-BETA-01` tadpole fit.
- `scripts/hk_species.py` and `scripts/normalization_chain.py` mention
  "Proca / Stueckelberg / 1-form" only as **symbolic Seeley–DeWitt bundle
  traces** (analytic `a_1`), not as a lattice operator.

## What does NOT exist (in this repository)

- No lattice vector / 1-form operator `Δ^{(1)}[g,h]`.
- No Stueckelberg / compensating-scalar determinant on the lattice.
- No metric-perturbation implementation, no numerical `h`-derivative, no
  graviton / axis-TT projection code.
- No per-species normalization that divides a vector loop by `β_B`.
- No raw output, table, or config from which `−3.2(5)` was produced.
- No `PROVENANCE.md`; `MIGRATION.md` states plainly: *"Paper 2 has no legacy
  repository, no archived script, no stored result file, and no reproducible
  provenance for its headline numbers … Nothing can be re-run."*
- The paper's header references `github.com/zetacheng/3-vector-sector` only for
  the Fierz gate `P3-FIERZ-01` and cites a "companion vector-channel paper" for
  the Proca **construction** (`Π_V`, pole audit) — **not** for the `β_V/β_B`
  graviton extraction. The paper further registers the induced-gravity budget
  insertion as "an open computation, not a result". `3-vector-sector` is also
  outside this session's repository scope.

## Verdict

**NOT LOCATED.** The historical Finding 5 lattice pipeline that produced
`−3.2(5)` is not present in this repository, and no provenance trail points to a
recoverable artifact. `scripts/lattice_beta_scan.py` is the **scalar**
`P2-BETA-01` tadpole and must **not** be substituted for the
curved-background lattice Proca extraction — it implements none of the required
machinery.

## Consequence

The circularity test of `P2-BETAV-CIRC-01` **cannot be performed directly**: the
pipeline whose projection/normalization is in question does not exist here.
`P2-BETAV-CIRC-01` is therefore **blocked by provenance** and is set to
`SUSPENDED`. The two honest, separately-labelled substitutes — neither of which
closes `P2-BETAV-CIRC-01` — are:

- `P2-BETAV-ASSEMBLY-01` — an implementation-regression gate (does the
  determinant bookkeeping preserve `k`-dependence on the shared lattice
  integral, with no hardcoded `−3`?). **PASS on its own terms; does not test the
  historical projection.**
- `P2-BETAV-RECON-01` — a clean-room curved-background Proca reconstruction
  (`PROPOSED`; if built, it tests *that reconstruction*, not the historical
  pipeline).

Finding 5's `−3.2(5)` remains an **unreproduced paper value**. The cross-repo
flag to `3-vector-sector` `P3-C-004` is unchanged (that claim rests on the `C_6`
sign structure, not on `−3.2(5)`).
