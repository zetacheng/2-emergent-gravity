# Task specification — generator-sum mean-field criticality: does `G_c = 1/(2·I_0)` transfer?

Specification evidence base: `51d4bbe1a2e965b0793b18f4ead5a11dab54c364`

Classification: **MATERIAL**. Branch only; integration is a separate
authorization. **This is a DERIVATION.** It decides nothing: `P2-GAP-01`
keeps `PASS`, `P2-PHASE-01` keeps `PROPOSED`. `AGENTS.md` rule 3 applies —
derivation note before production code.

## The open item

`DECISION_LOG.md` records `UNESTABLISHED`: `P2-GAP-01` obtained
`G_c = 1/(2·I_0)` from the singlet-only form `L_int = G_N (ψ̄ψ)²`; the
mean-field combinatorics of the full U(N) generator-sum canonical
interaction have never been performed. The `P2-PHASE-01` exploratory work
quotes every position in `G/G_c` (e.g. `M̂=1` at `G/G_c=1.769`, the
282-row branch-depth table, the drafted domain). If the generator-sum
`G_c` differs, those positions move. Calibration question; no scientific
verdict changes.

## Objective and computation

Perform the mean-field treatment of the full U(N) generator-sum canonical
interaction in the scalar channel; report the gap equation, its critical
coupling, and whether `G_c = 1/(2·I_0)` transfers from the singlet-only
form. Both treatments are carried out here under one set of conventions:

    (a) singlet-only   L_int = G_N (psibar psi)^2      [control]
    (b) generator-sum  X = (G/(2N)) * Sum( bilinear(lam(A),Id4)^2
                                         + bilinear(lam(A),I*gamma5)^2,
                                         (A, 0, N**2-1) )

- Reproduce (a) as a control: it must return `1 = 2·G_c·I_0` under
  `P2-GAP-01`'s normalisation (`G = 4·G_N`, `tr 1_4 = 4` absorbed,
  prefactor 2). If not, STOP.
- Perform (b) under the frozen uniform flavour-singlet scalar condensate
  ansatz. Carry the `λ^A` indices explicitly; DETERMINE which generator
  components acquire non-zero mean fields (an output, not an input). Do
  not assume the sum reduces to `A=0`; compute how it contracts.
- Report the mean-field combinatorial factor, the gap equation and its
  critical coupling, the ratio of (b)'s `G_c` to (a)'s (symbolic in `N`,
  at `N=2,3,4`), and whether they agree; if not, exactly which step
  differs.
- `Tr(λ^Aλ^B)=2δ_AB` and the completeness relation the rearrangement
  needs are frozen (the generator normalisation and the complete
  `A=0..N²-1` Hermitian basis are in the Phase-A freeze). If a needed
  relation is not frozen, report `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`
  and do not supply it.
- Use the same uniform scalar condensate ansatz the exploratory study
  used. Do not introduce an adjoint condensate; report whether the
  singlet ansatz is the only one the frozen material supports.

## What must not happen

- Do not modify `P2-GAP-01`'s entry, derivation or `PASS`. A ratio ≠ 1 is
  a finding about transferability, not an error there.
- Do not restate the exploratory results in new units; report the
  implication, do not perform the rescaling.
- Do not select an HS channel beyond the scalar one; do not touch the
  diquark question; do not amend the parameter-domain draft.

## Acceptance criteria (summary; full task text governs)

- **A0** commit order: (1) spec; (2) derivation note (before code, rule 3);
  (3+) script, results, test, report. Token `2350` fixed by commit 1.
- **A1** pinned inputs verified (STOP on mismatch):
  `derivations/P2-GAP-01_gap_criticality.md`
  `17b6f613ffefb79fae8c0a5c40e3bd67ad31a101112af615945647e143fade00`;
  `scripts/gap_criticality.py`
  `b99f9a66b9a0c7dc9b05cc2ce93c1bb75acc1b47edfa95da1285e853b38a90c2`;
  `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`
  `fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a`;
  `derivations/P2-PHASE-01_scalar_stationary_exploratory.md`
  `80586e33ef07e307729af4597f72b48f6ecee74fc6a0f396b593f735ef322599`.
- **A2** control reproduced (`1 = 2·G_c·I_0`); STOP if not.
- **A3** generator-sum gap equation derived, `λ^A` sums explicit, every
  combinatorial factor shown.
- **A4** ratio reported, symbolic in `N`, at `N=2,3,4`, case named.
- **A5** ansatz observation reported without supplying a second ansatz.
- **A6** deliverables incl. tests (control `1=2G_cI_0`; `Tr(λ^Aλ^B)=2δ_AB`
  for `N=2,3,4`; ratio computed by the script).
- **A7** nothing pre-existing disturbed (`GATES.md`, `CONVENTIONS.md`,
  `AGENTS.md`, `DECISION_LOG.md`, `pyproject.toml`, gates, digests).
- **A8** six additions, zero modifications.
- **A9** listed validators + new test exit 0 via `python -m pytest <path>`.
- **A10** lint clean (`ruff check`) on authored files.
- **A11** branch only from `51d4bbe1`; `main` unmoved; push task branch.

## Invariants

- Executor-writable: the six A8 paths only.
- Do not modify `P2-GAP-01`; do not rescale existing results; do not amend
  the domain draft.
- Do not supply a condensate ansatz, completeness relation, or
  normalisation the frozen material does not fix — report the gap.
- Do not consume the quarantined `−3.2(5)`, the suspended
  `P2-BETAV-CIRC-01` result, or the historical Finding 5 extraction; list
  every repository input read, by path.
- Commit-message hygiene: no `Co-Authored-By`, no session id/URL, no tool
  attribution; report suppression per commit.
- No merge, PR, force-push, or history rewrite. Branch
  `gate/p2-generator-sum-criticality`. Install nothing.
