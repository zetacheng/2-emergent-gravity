# Addendum — the Fierz sign ruling and its consequence for `P2-PHASE-01`

**Kind:** addendum. It records a consequence for results already
committed. It computes nothing new and revises no earlier document.

**Neither original report was altered.** Both are preserved exactly as
written:

- `reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md`
- `reports/2026-08-07T1159Z_grassmann-crossing-sign.md`

They record honestly what was known when each was written. Rewriting
them would destroy that record, which is why this addendum exists
instead.

## 1. The ruling

> **PI ruling, 2026-08-07 — Fierz matrix sign convention.**
>
> `matrix_rational` stores the Dirac/internal exchange matrix **without**
> the operator-level Grassmann crossing factor. The four-fermion operator
> exchange is therefore
>
>     K_exch = s_G · M · K_direct,     s_G = -1
>
> The declared `grassmann_crossing_sign` is applied **exactly once at
> operator use**. The existing double application in
> `basis_freeze_check.py` is an ineffective validation and does not
> define the storage convention.

**The ruling supplies a definition; it does not recover an original
intent.** No defining kernel equation exists anywhere in the frozen
material — `K_exch`, `K_direct`, `defining equation` and
`kernel equation` all occur zero times, verified independently. The
ruling rests on three pieces of indirect evidence, none of which is a
defining equation. `DECISION_LOG.md`, entry dated 2026-08-07, carries
the full record.

## 2. Consequence for the induced V and A coefficients

`reports/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md`
reported the induced singlet coefficients

    S: 0     P: 0     V: G/4     A: G/4     T: 0

**These are MATRIX-LEVEL values**, obtained by applying the frozen
`matrix_rational` to the converted coefficient vector. That report
**explicitly left the operator-level sign unresolved**, recording the
placement of `grassmann_crossing_sign` as a first-class finding and
stating that, were the `-1` applied on top, every induced coefficient
would flip while the magnitudes, the vanishing families and the
purely-singlet structure would be unaffected.

**Under this ruling that contingency is discharged.** Applying
`s_G = -1` exactly once at operator use gives the **OPERATOR-LEVEL**
coefficients

    S: 0     P: 0     V: -G/4     A: -G/4     T: 0

The matrix-level values are unchanged; what the ruling fixes is the one
further factor between them and the operator.

## 3. What the sign does not touch

The structural results are **unaffected by the sign**:

- **S, P and T vanish.** A vanishing coefficient is a result, not an
  omission, and no overall factor changes it.
- **V and A are equal and purely singlet.** The traceless induced
  coefficient is exactly zero, which follows from
  `lam(0) = sqrt(2/N) Id_N` and the frozen generator normalisation.
- **The exchanged form is purely left-right**, `LL = RR = 0`, with
  `LR = RL = 2` under the symmetric split. That check is sign-blind by
  construction: an overall sign multiplies all four coefficients
  equally.

Nothing in derivation (b) of the earlier task — the stationary-branch
potential depths — depends on the Fierz sign at all.

## 4. Consequence for the storage question

`reports/2026-08-07T1159Z_grassmann-crossing-sign.md` reported the
matrix storage convention as
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`, having established that
the frozen material contains no defining kernel equation.

**That question is now closed by ruling rather than by evidence.** The
distinction matters and is preserved here: the frozen material still
contains no defining equation, and the earlier report's finding remains
accurate as a statement about the frozen material. What has changed is
that a definition now exists, supplied by the PI and recorded in
`DECISION_LOG.md`.

The operator-level sign `s_G = -1` was and remains **established by
calculation**, independently of the ruling.

## 5. Out of scope

The freeze repair — a tenth mutation covering `grassmann_crossing_sign`,
correction of the double application in `basis_freeze_check.py`, and
pinning `scripts/P2-CHANNEL-FREEZE/vocab_parser.py` — is queued as a
separate authorized task and is **not** performed here. The Phase-A
freeze, its checker and its mutation suite are byte-identical to the
integration base.

`P2-CHANNEL-FREEZE-01` and `P2-PHASE-01` both remain `PROPOSED`. This
ruling changes a convention, not a gate.
