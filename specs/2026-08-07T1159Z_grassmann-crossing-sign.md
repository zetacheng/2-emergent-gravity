# Task specification — ratify the Grassmann crossing sign by explicit single-leg exchange

Specification evidence base: `9609677576b6d0d77a0813c93673aed81b0c4d5f`
Required verification target: the same commit.

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**This is a small, single-question task.** It exists because a declared
convention in a ratified freeze has never been effectively verified, and
the first computation to consume it — the `P2-PHASE-01` Fierz
verification — could not resolve it.

---

## 0. What is established, and what is not

**Established, and independently confirmed from the repository:**

`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` declares
`grassmann_crossing_sign: -1`. Its only consumer anywhere in the
repository is `scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py:459`,
which computes

    computed_fierz = (sign * projector * crossing * embedding).T * sign

**The scalar appears twice, and `.T` does not touch a scalar, so the two
occurrences multiply to `sign² = +1` for either declared value.** The
assertion `computed_fierz == frozen_fierz` is therefore identical
whether the freeze declares `-1` or `+1`. Verified by direct
substitution.

`tests/test_channel_freeze_mutations.py` contains no mutation of this
field — `grep -c grassmann` returns 0. **Flipping the declared value
would pass every existing check silently.**

An independent reconstruction of the Fierz matrix WITHOUT applying the
crossing sign reproduces the frozen `matrix_rational` in all 25 entries
exactly; WITH it, 21 of 25 entries flip.

**Not established: where the `-1` is meant to act.** Three pieces of
evidence pull in different directions and none settles it — the freeze
lists the sign as a separate convention field, suggesting application on
use; its §C prose says the sign "fixes the following matrix", suggesting
inclusion; and the checker applies it twice, consistent with the frozen
entries being unsigned. **Involution cannot arbitrate: `M² = (−M)² = 1`.**

**Nothing downstream depends on it yet.** No verdict, promotion, digest
or claim rests on the sign. The exposure is forward-looking: the first
consumer to apply it will obtain the global negative of what the
checker validated.

## 1. Objective

Paper 2 carries a derivation that **determines the Grassmann exchange
sign** relating a four-fermion operator to its exchanged form under the
frozen conventions, from an explicit calculation rather than convention
archaeology; and that **tests whether the frozen material is sufficient
to determine whether `matrix_rational` stores that sign.**

**The second is a test, not a determination.** The objective does not
presume the storage question has an answer in the frozen material.

**This is a computation, not a ruling.** It determines what the algebra
gives. Whether the freeze is then amended, and how, is a PI decision
this task does not take.

## 2. What to compute

**Work from an explicit four-fermion Grassmann monomial, not from a
matrix identity.** The matrix route is what failed to resolve this: an
overall sign on the transformation cannot be recovered from a matrix
whose square is the identity.

**The permutation is frozen here, because "one exchange of the fermion
legs" does not fix a sign.** For a Grassmann monomial the sign depends
entirely on the starting canonical ordering and the ending ordering, and
two defensible readings of the same phrase give opposite answers.

Start from the four-fermion monomial with every index role written out.
**Spinor indices are `α β γ δ`; internal indices are `i j k l`.** No
index letter carries two roles:

    ( psibar^{i}_{α}  Gamma_{αβ}  lam^{A}_{ij}  psi^{j}_{β} )
    ( psibar^{k}_{γ}  Gamma_{γδ}  lam^{A}_{kl}  psi^{l}_{δ} )

Label the four Grassmann objects, in the order written:

    1 = psibar^{i}_{α}    2 = psi^{j}_{β}
    3 = psibar^{k}_{γ}    4 = psi^{l}_{δ}

with **Grassmann order** exactly

    psibar_1  psi_2  psibar_3  psi_4

Rearrange to the pairing **1–4, 3–2**, retaining the final Grassmann
order exactly

    psibar_1  psi_4  psibar_3  psi_2

**Report the permutation taking the first ordering to the second, its
decomposition into transpositions, and the resulting sign.** Any other
reading of "exchange" is out of scope: this one is normative.

**Report:**

- the monomial used, with every index explicit;
- the exchange performed, stating which legs and in what order;
- each anticommutation applied, with its sign;
- the resulting overall sign, as a number;
- whether that sign equals the declared `grassmann_crossing_sign = -1`.

**Then treat the storage question as a SEPARATE question, because the
Grassmann calculation does not answer it.**

The explicit calculation determines the **operator-level crossing
sign** `s_G = ±1`, unambiguously. **It does not by itself determine
whether `matrix_rational` stores that sign**, which is a question about
the matrix's defining kernel equation — a representation convention, not
an algebraic fact.

After computing `s_G`, **inspect the frozen definition of the Fierz
kernel** and determine whether that definition uniquely specifies one
of:

    K_exch = M · K_direct
    K_exch = s_G · M · K_direct

**If the frozen material does not uniquely distinguish these, report the
Grassmann sign as ESTABLISHED and the matrix-storage convention as
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`.** That is a satisfactory
outcome, not a failure.

**Do not infer storage merely from the numerical equality of an unsigned
reconstruction with `matrix_rational`.** That equality is consistent
with either convention — it says the entries match a signless
construction, not that the defining equation omits the sign. **An
earlier draft of this specification asked you to choose between the two
on exactly that basis, and was wrong to.**

**Do not amend the freeze, the checker, or the mutation suite.** Report
what the algebra gives and what follows for the stored matrix; the
correction is a separate authorized task.

**Conventions are frozen and are not yours to choose.** Use the
Phase-A freeze's declared conventions, including the PI ruling of
2026-08-07 that `gamma5 = gamma(0)*gamma(1)*gamma(2)*gamma(3)` in the
Phase-A-freeze sense, Hermitian with `γ₅² = Id4`. **If any convention
needed for this calculation is not declared, report it as
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` and stop** rather than
selecting one.

## 3. A structural cross-check you should also report

Independently of the sign, the chiral decomposition of the rearranged
interaction is a strong check on the whole calculation and costs little.

Decompose the exchanged interaction onto chiral currents
`J^{L}_μ = ψ̄ γ_μ P_L ψ` and `J^{R}_μ = ψ̄ γ_μ P_R ψ`, and report the
four coefficients `LL`, `LR`, `RL`, `RR`.

**The projector convention is frozen here**, since this whole task
concerns sign conventions and an implicit one would defeat its purpose.
With the Phase-A `gamma5` (Hermitian, `γ₅² = Id4`):

    P_L = (Id4 - gamma5)/2        P_R = (Id4 + gamma5)/2

**`S² − P²` here means the canonical interaction AFTER the already-
ratified `iγ₅ → γ₅` basis conversion — it is not a new interaction
choice.** The canonical form is written `S² + (iγ₅)²`, and under the PI
ruling of 2026-08-07 with the Phase-A `gamma5`,
`(bilinear(lam(A), I*gamma5))² = −(bilinear(lam(A), gamma5))²`, which is
`S² − P²` in the frozen `[S,P,V,A,T]` basis.

**Expected, and stated so you can contradict it:** a preliminary
calculation on our side found that input to be purely left-right in the
scalar channel (`LL = RR = 0`), and the exchanged form to be purely
left-right in the current channel (`LL = RR = 0` again).
**If your calculation disagrees, your calculation is the evidence** —
report the disagreement rather than reproducing the expectation.

**This check is sign-blind**, since the overall sign multiplies all four
coefficients equally. It tests the rearrangement's structure, not the
sign, which is why both are worth having.

## 4. Acceptance criteria

**A0 — Commit order.** Commit 1 is this specification under `specs/`.
Commit 2 is the derivation note under `derivations/`, before any
production code, per `AGENTS.md` rule 3. Commits 3+ carry script,
results, test and report.

**A1 — Pinned inputs verified.** Verify each digest before use; any
mismatch is a STOP:

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a

    results/P2-CHANNEL-FREEZE/fierz_matrix.json
    5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9

    derivations/CANONICAL_INTERACTION.md
    27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81

**Also pinned, because §0 and A5 make substantive claims about them and
they are the executable source of the defect under study:**

    scripts/P2-CHANNEL-FREEZE/basis_freeze_check.py
    b3123855c225c6832c890c42fda6b03b4b8b81eef69a1c69ae654d7523367fdb

    tests/test_channel_freeze_mutations.py
    4abaaf1746f5ffdbe4c09d8b05711f3570b30d8d9b7e4cdbf510ddb80fe7c7c0

    tests/test_channel_freeze_phase_a.py
    80ee0e834287e5f5c2185c881633e656454ff9e7935382dabc6370e16c204d3d

**A2 — The Grassmann calculation**, per §2, with every anticommutation
shown. **A reported sign without the steps behind it does not satisfy
this criterion.**

**A3 — Two separate results, reported separately.**

**A3a — the operator-level Grassmann exchange sign** `s_G`, established
by the calculation of A2, with the frozen permutation of §2.

**A3b — the storage convention**: whether the frozen material's defining
kernel equation uniquely selects `K_exch = M·K_direct` or
`K_exch = s_G·M·K_direct`. **If it does not, report
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` and quote the text you
inspected.** A3a is expected to resolve; A3b may legitimately not.

**A4 — Chiral decomposition** per §3, four coefficients reported.

**A5 — The checker's double application characterised.** Confirm by
direct substitution that `(sign * X).T * sign` is invariant under
`sign → -sign`, and report both outputs. **Do not modify the checker.**

**A6 — Deliverables:** derivation note, script, results artifact, test
file, report. **Tests are required.** They must cover: the explicit
exchange sign; the chiral decomposition; and the checker's sign
invariance. **A test that only asserts the frozen matrix equals itself
does not test anything this task is about.**

**A7 — Nothing pre-existing disturbed.** No gate, gate status, verdict,
artifact digest, hash-pinned artifact, pre-existing test, `GATES.md`,
`CONVENTIONS.md`, `AGENTS.md`, or `pyproject.toml` is modified. **In
particular, do not modify the freeze, `basis_freeze_check.py`, or
`tests/test_channel_freeze_mutations.py`** — the missing tenth mutation
is a known gap and a separate task.

**A8 — Scope.** Exactly six added paths; you choose none of them except
the `{HHMM}Z` token, fixed once by commit 1 and reused verbatim:

    specs/2026-08-07T{HHMM}Z_grassmann-crossing-sign.md
    derivations/P2-CHANNEL-FREEZE-01_grassmann_crossing_sign.md
    scripts/p2_grassmann_crossing_sign.py
    results/P2-CHANNEL-FREEZE/grassmann-crossing-sign/crossing_sign.json
    tests/test_p2_grassmann_crossing_sign.py
    reports/2026-08-07T{HHMM}Z_grassmann-crossing-sign.md

Report the manifest in full and the scope-checker JSON including
`observed_operations`.

**A9 — Validators, exit status 0**, run individually with
`python -m pytest <path>` — that exact invocation, since `pytest` and
`python -m pytest` resolve to different versions on this host:
`tests/test_repository_structure.py`, `tests/test_si1_governance.py`,
`tests/test_gate_anchors.py`, `tests/test_governance_tools.py`, your new
test file, and — **because this task studies the freeze checker** —
`tests/test_channel_freeze_phase_a.py` and
`tests/test_channel_freeze_mutations.py` as regression evidence that the
branch changed no freeze behaviour. Report each command, complete stdout and stderr, exit
status, wall time, and the Python and pytest versions.

**A10 — Branch only.** Verify that `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to
`9609677576b6d0d77a0813c93673aed81b0c4d5f`, and create the branch from
that commit. **None of local `main`, `origin/main`, or remote `main` may
be moved**; a stale local `main` is not to be repaired. Report all three
separately. Push the task branch only.

## 5. Evidence layering

**Committed report:** everything available before the report commit —
the calculation, the storage verdict, the chiral decomposition, the
checker characterisation, pinned-input verification, the earlier commit
SHAs and messages, the pre-report head, and the intended report commit
message and its authoring-time trailer suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the committed head; **A9-final**, the validator
suite re-run on a clean worktree at that head; the push; the report
commit's stored message read back from the commit object; and the
ancestry confirmation.

**A9 runs twice: `A9-pre` at the pre-report head goes into the report;
`A9-final` at the report head is post-report evidence and carries the
acceptance verdict.** **Do not
amend the report to insert evidence whose production depends on the
report commit.**

## 6. Invariants and prohibitions

- Executor-writable: the six paths of A8 only.
- **Decide nothing.** Report what the algebra gives. Whether the freeze
  is amended is a PI decision outside this task.
- **Do not modify any frozen artifact**, the checker, or the mutation
  suite.
- Commit-message hygiene: inspect the proposed message before each
  commit and the stored message after; permit no `Co-Authored-By`, no
  session identifier or URL, no tool attribution. **Report, per commit,
  whether any trailer was suppressed and which — an authoring-time
  suppression is a fact to disclose, not an absence.**
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: `docs/BRANCHING_POLICY.md` enumerates `gate/`,
  `paper/`, `review/`, `fix/`, `archive/`; the policy-versus-practice
  contradiction remains an open PI item. Use
  `gate/p2-grassmann-crossing-sign`. If you judge that this conflicts,
  stop and report.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything**; report anything missing as a finding.
- Stop-on-unexpected-result applies to commands that read or alter
  repository state, not to your own development iteration.
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 7. Report contract

- **in the committed report:** raw output for A0–A8 as available before
  the report commit, plus **A9-pre** — the validator suite run on a
  clean worktree at the pre-report head;
- **post-report evidence, returned to the Reviewer and not written back:**
  the final scope check at the committed head, **A9-final**, A10, and
  the report commit's stored message read back from the commit object;
- the Grassmann calculation in full, every anticommutation shown;
- the storage verdict with its reasoning;
- the four chiral coefficients;
- **what follows for the `P2-PHASE-01` induced V and A coefficients** —
  their magnitude and structure are already established; state only what
  your result implies for their sign, and **do not restate or re-derive
  the rest**;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
