# Task specification — adjudicate the diquark decomposition discrepancy, layer by layer

Specification evidence base: `8701a97a6bb58550d4300f75c10638b057335731`

    Branch under adjudication  gate/p2-diquark-both-eta
                               bc1e5c743aada004c52dc7ab7ce2af61de439955

Classification: **MATERIAL**. Branch only. **The branch under
adjudication is NOT integrated by this task and its disposition is
`HOLD — MATERIAL RESULT DISCREPANCY`.**

**Rules 1–17 are in force**, so this task is governed by Rule 15: its
pre-execution review is a committed artifact — see A0 commit 2 and A2.

**This task finds where two computations first diverge. It does not
decide which is right, and it does not produce a channel-character
result.**

---

## 0. The discrepancy

Two independent computations of the particle–particle Dirac
decomposition of the frozen `S² + P²` interaction disagree about **which
families survive**:

    per-component family sums     S       P       T       V       A
    method A, the branch          0       0       0     +1/2    -1/2
    method B, independent        -1/2    -1/2   ±1/2      0       0

**Both report exact reconstruction over all 256 components.** Method B's
off-diagonal residual is ~1e-14 and its rank is 256/256.

**Exact reconstruction is not the property in dispute.** It shows that
each decomposition is self-consistent **for the tensor it was actually
given**. **It does not show that both were given the same tensor.**
That distinction is the whole of this task.

**Four family-convention variations were tried on method B** —
`A = γ_μ γ₅` versus `γ₅ γ_μ`, and `T = ½[γ_μ,γ_ν]` versus
`σ_μν = (i/2)[γ_μ,γ_ν]` — and **none reconciles them.** Method B's V and
A vanish under all four.

**What is unlikely to explain it.** A `γ₅` sign, `C → λC`, a
normalisation factor, or `internal_weight = 2` would change signs or an
overall scale. **None would move the surviving irreps as a group from
V/A to S/P/T.**

**What is likely to explain it, and is the reason this task exists.**
The two computations may be projecting **different rank-4 tensors** —
differing by an index permutation, a transpose, the placement of `C`
versus `C⁻¹`, or the Grassmann crossing applied before projection. **Any
of those admits perfect reconstruction while representing a different
rearrangement.**

**And that possibility lands near an unfrozen convention.** The
particle–particle Grassmann ordering is not fixed by the frozen
material — the branch itself established this.

**If the two self-consistent results correspond to two orderings BOTH
of which satisfy every frozen constraint and differ only where the
frozen material is silent, then the surviving family support depends on
that unfrozen ordering**, and the branch's claim of independence is
wrong.

**That conditional is load-bearing and must not be dropped.** A
divergence between two index maps establishes only that the maps
differ. **Promoting it to convention dependence requires showing both
maps admissible** — and A7 requires exactly that showing.

**That would not be a failed derivation. It would be a deeper blocker
than the one the task set out to examine**, and it is worth more than
either coefficient set.

## 1. What is, and is not, still standing

**Standing, and not under adjudication.** For a fixed set of every other
convention and a fixed pp tensor construction, if each coefficient has
the form `c_a = η K_a`, then `c_a(−1) = −c_a(+1)` for every `K_a ≠ 0`.
**This is algebra and both computations satisfy it.**

**NOT standing.** That the diquark channel character is well defined
independently of the pp ordering. **If one ordering leaves V and A
non-zero and another leaves S, P and T non-zero, then the η sign flip is
robust while WHICH channel's character it flips is not.** **Do not
restate the branch's independence claim as established.**

## 2. Method B, specified so it is reproducible

**Construct it yourself from this description. Do not import it.**

    gamma, Euclidean, Hermitian, {g_m, g_n} = 2 delta_mn:
      g0 = kron(s1, s1)      g1 = kron(s1, s2)
      g2 = kron(s1, s3)      g3 = kron(s2, I2)
    with s1, s2, s3 the Pauli matrices and I2 the 2x2 identity.

    g5 = g0 g1 g2 g3          (Hermitian; g5^2 = I4)

    C: solve  C g_m^T + g_m C = 0  for all m, as a HOMOGENEOUS LINEAR
       SYSTEM over a general 4x4 complex matrix, and report the
       null-space dimension. In this representation a representative
       is  C = g0 g2,  with  C^T = -C.

       **Searching a 16-element basis for elements that work is a
       proxy**: it cannot exclude a linear combination that also works.
       **Compute the null space.**

    families:
      S = {I}                 P = {g5}
      V = {g_m}               A = {g_m g5}
      T = {(g_m g_n - g_n g_m)/2,  m < n}

    the rank-4 tensor, BEFORE any projection, for Gamma in {I, g5}:
      T[a,b,c,d] = Gamma[a,b] * Gamma[c,d]
    with a,c the psibar indices and b,d the psi indices.

    the decomposition:
      Gamma_{ab} Gamma_{cd} = sum_pq f_pq (Gamma_p C)_{ac} (C^-1 Gamma_q)_{bd}

    f extracted by least squares over the full 256-element product
    basis, NOT by a closed-form trace formula, so that exactness is
    measured rather than assumed.

**Method B applies no Grassmann crossing sign and no `η`, `s_pp` or `ν`
before projection.** It decomposes the bare Dirac tensor. **If method A
applies any of them earlier, that is a finding, not an error** — record
it at the layer where it happens.

## 3. The comparison, layer by layer, with the first divergence dispositive

**Perform these in order. At the FIRST layer that differs, record it and
CONTINUE to the remaining layers anyway** — knowing whether the
divergence persists downstream is part of the answer — **but report
clearly which layer was first.**

    L1  the matrices actually used
        g_0..g_3, g5, C, C^-1, element by element, both methods

    L2  the RAW canonical rank-4 tensor, before any pp reordering
        T[a,b,c,d] for the scalar and pseudoscalar canonical terms,
        with THE POSITION OF EVERY SPINOR INDEX STATED

    L3  the pp SLOT/INDEX MAP and the Grassmann permutation taking the
        source four-fermion ordering to the diquark bilinears, written
        out, with its parity and sign

    L4  the actual 256-component TARGET VECTOR  t  presented to the
        extractor, i.e. L2's tensor after L3's map, flattened in the
        order the extractor consumes

    L5  the projector kernels and the full 256 x 256 DESIGN MATRIX  M
        — the explicit Gamma_a C and C^-1 Gamma_a, and the dual basis

    L6  the coefficient vector  f  and its family aggregation

**The comparison is of the linear system `M f = t` actually solved, not
of the raw tensor.** An earlier version of this specification made L2
decisive and concluded that identical raw tensors implied a broken
projector. **That inference is invalid**: two methods can share a raw
tensor and then present it under different slot maps, **and both
projectors can be entirely correct.** That is precisely the unfrozen pp
ordering this task exists to probe.

## 4. Both methods, re-run in one environment

**Re-run method A and method B yourself, in this task, in the same
environment.** Do not compare a fresh method B against the branch's
recorded numbers.

**Reproduce method A from the branch's committed script**, pinned at
A1, and **report whether its numbers reproduce.** If they do not, that
is a finding about the branch and this task stops there.

**Run each method twice** and confirm both are deterministic.

**"Deterministic" means:** compare the complete numerical payload used
in L1–L6; **byte-identical integer and index data, and numerically
identical floating arrays under a stated tolerance.** **Ignore no field
unless this specification names it as non-computational metadata** —
and it names none. **State the tolerance you used.**

**A result that does not reproduce within one environment is not a
discrepancy between methods; it is an unstable computation**, and the
adjudication would be meaningless.

## 5. What must not happen

- **Do not decide which method is correct** where the evidence does not
  settle it. **`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` naming the
  first diverging layer is a satisfactory outcome.**
- **Do not select a particle–particle Grassmann ordering**, freeze `η`,
  or fix the diquark normalisation.
- **Do not produce a channel-character result**, and do not restate
  either coefficient set as the programme's finding.
- **Do not modify the branch under adjudication**, and do not integrate
  it.
- **Do not repair method A's script** even if you find a defect in it.
  **Report the defect and its location; a repair is a separate task with
  its own review.**
- **Do not conclude that the pp ordering is harmless.** If the
  divergence is upstream of projection, **the live possibility is the
  opposite**, and §0 says why.

## 6. Acceptance criteria

**A0 — Commit order and paths, frozen.**

    commit 1  specs/2026-08-XXT{HHMM}Z_diquark-adjudication.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_diquark-adjudication.md
    commit 3  derivations/P2-PHASE-01_diquark_adjudication.md
    commit 4  scripts/p2_diquark_adjudication.py,
              results/P2-PHASE-01/diquark-adjudication/adjudication.json,
              tests/test_p2_diquark_adjudication.py
    commit 5  reports/2026-08-XXT{HHMM}Z_diquark-adjudication.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes the
work**, per Rule 15; **commit 3 precedes production code**, per
`AGENTS.md` rule 3.

**A1 — Inputs, pinned two different ways.** Method for every digest:
`git cat-file blob <rev>:<path> | sha256sum`.

**(a) DIGEST-PINNED — a mismatch is a STOP**, at the evidence base:

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a

    results/P2-CHANNEL-FREEZE/fierz_matrix.json
    5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9

**(b) COMMIT-PINNED — their content is fixed by the branch commit
`bc1e5c743aada004c52dc7ab7ce2af61de439955`**, not by a digest supplied
here:

      scripts/p2_diquark_both_eta.py
      results/P2-PHASE-01/diquark-both-eta/diquark.json
      derivations/P2-PHASE-01_diquark_both_eta.md

**Verify each path exists at that commit and compute and report its
SHA-256.** **There is no independently supplied expected SHA-256 for
these three, so a "digest mismatch" criterion does not apply to them**;
**absence, or failure to read, is a STOP.**

**The distinction is deliberate.** A digest supplied by a specification
author is not evidence that a file says what the author believes; **the
commit is the pin, and the digest is measured and recorded, not
checked.**

**A2 — This task's pre-execution review committed, unedited**, at the
`reviews/chatgpt/` path of A0. The delimiters are these two lines, each
occupying a whole line:

    === REVIEW ARTIFACT BEGINS ===
    === REVIEW ARTIFACT ENDS ===

**Match them as COMPLETE LINES**, not as first occurrences of the
string — this specification contains them. **Exclude any preamble
sentence before the BEGIN line, the delimiter lines themselves, and any
accompanying instruction.** **If a placeholder appears inside the
review's text it stays as written**; resolve placeholders in the path
only.

**A3 — Determinism.** Each method run twice, results identical. **If
either is not reproducible, STOP** — §4 says why.

**A4 — Method A reproduced** from its committed script, with its
recorded numbers confirmed or the difference reported.

**A5 — Method B constructed from §2**, with its `C` obtained as the
**null space of the homogeneous system** `C γ_μ^T + γ_μ C = 0`, its
**null-space dimension reported as computed** rather than inferred from
a basis search, and its reconstruction exactness measured.

**A6 — L1 through L6 reported**, each with an explicit verdict of
identical or differing, **and the FIRST diverging layer named.**

**A7 — The case decided, over `(t, M, f)`.** State which ONE of these
holds:

    T_A^S != T_B^S  or  T_A^P != T_B^P
        divergence is in the canonical construction itself.
        **Compare the scalar and pseudoscalar tensors SEPARATELY** —
        one matching while the other does not is itself diagnostic and
        a summed comparison would hide it.

    both canonical tensors match  but  t_A != t_B
        ORDERING / INDEX-MAP DIVERGENCE before projection. **Both
        extractors may be correct for their respective inputs.**

        **This establishes dependence on the UNFROZEN pp ordering
        convention ONLY IF both L3 maps are shown to satisfy every
        frozen constraint and to differ solely by a convention the
        frozen material leaves open.** **If the admissibility of either
        map cannot be established, report
        `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`.**

        **Do not promote construction divergence to convention
        dependence.** Method B is defined in §2 to apply no Grassmann
        crossing; **if that leaves its source-to-diquark rearrangement
        incomplete, method B is a useful diagnostic comparator but not
        a second admissible ordering**, and the stronger reading does
        not follow.

    t_A == t_B  but  M_A != M_B
        basis / projector-convention divergence. **Neither method is
        thereby wrong**; they are extracting in different bases.

    t_A == t_B  and  M_A == M_B  but  f_A != f_B
        **ONLY HERE** may an implementation defect in coefficient
        extraction or the solver be asserted, and L6 localises it.

**Do not assert an implementation defect outside the last case.**

**The classification follows the EARLIEST differing quantity in this
hierarchy.** **Downstream quantities may also differ**, and A6 requires
them reported regardless. **"Exactly one case" means one classification,
not that only one numerical difference exists.**

**A8 — The independence claim assessed.** The branch states its verdict
is *independent of the two remaining unfrozen definitions*. **Report
whether the evidence supports that.**

**Answer at the strongest level the evidence licenses, and no
further:**

    the evidence supports independence
    the evidence contradicts it, with both maps shown admissible
    the maps differ but admissibility of one or both is not
      established  ->  UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY

**The third is a satisfactory outcome.** §0's conditional says why the
second requires more than a difference between maps.

**A9 — Scope**, seven additions:

    add:
      specs/2026-08-XXT{HHMM}Z_diquark-adjudication.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_diquark-adjudication.md
      derivations/P2-PHASE-01_diquark_adjudication.md
      scripts/p2_diquark_adjudication.py
      results/P2-PHASE-01/diquark-adjudication/adjudication.json
      tests/test_p2_diquark_adjudication.py
      reports/2026-08-XXT{HHMM}Z_diquark-adjudication.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 7 additions and 0 modifications**, matching
the seven paths listed above. **`tests/` gains exactly one new file and
no existing test is modified.**

**A10 — Nothing pre-existing disturbed.** No gate, gate status, verdict,
digest, hash-pinned artifact, pre-existing test, `GATES.md`,
`CONVENTIONS.md`, `AGENTS.md`, `DECISION_LOG.md` or `pyproject.toml` is
modified. **The branch under adjudication is not touched.**

**A11 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`, `tests/test_p2_channel_character.py`,
and your new test file. **A11-pre** at the pre-report head goes in the
report; **A11-final** at the pushed head is post-report evidence.

**A12 — Lint clean:**
`ruff check scripts/p2_diquark_adjudication.py tests/test_p2_diquark_adjudication.py`.
**Those two files only.**

**A13 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to
`8701a97a6bb58550d4300f75c10638b057335731`; create the branch from that
commit; move no `main` ref. **Local `main` is stale by design.** Report
all three. Push the task branch only. **Delete no branch.**

**A14 — Commit-message hygiene** on every commit: inspect the proposed
message before, the stored message after; permit no `Co-Authored-By`, no
session identifier or URL, no tool attribution. **Report per commit
whether any trailer was suppressed and which.**

## 7. Evidence layering

**Committed report:** A1–A10, A11-pre, A12, A14 for the earlier commits;
the earlier commit SHAs and messages; the pre-report head; the intended
final manifest; and the intended report commit message with its
authoring-time trailer suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A11-final, the push, the
report commit's stored message read back from the object, and ancestry
confirmation.

## 8. Invariants and prohibitions

- Executor-writable: the seven paths of A9 only.
- **Do not draw any conclusion §5 forbids.**
- **List every repository input you actually read, by path.**
- Commit-message hygiene as in A14.
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: use `gate/p2-diquark-adjudication`.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 9. Report contract

- raw output for A1–A12, scope-checker JSON verbatim including
  `observed_operations`;
- **the determinism check first**, since everything else depends on it;
- **L1 through L6, each with its verdict, and the first diverging layer
  named**;
- **A7's case decision, stated as EXACTLY ONE of the four cases**, with
  the scalar and pseudoscalar tensors compared separately;
- **A8's assessment of the independence claim**;
- **whether either method contains a defect you can localise** — with
  its file and line, and **without repairing it**;
- **whether the two results could both be correct** for two different
  but currently admissible pp ordering conventions. **If so, that is the
  finding, and it is larger than the discrepancy that prompted this
  task**;
- **what remains unresolved**, named precisely;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 10. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**

    target      method B, constructed from §2 in a scratch environment
    method      direct computation, then least-squares decomposition
    check type  NUMERICAL, tolerance 1e-9

    CONFIRMED   the Clifford algebra {g_m, g_n} = 2 delta_mn holds
    CONFIRMED   g5^2 = I4
    CONFIRMED   the homogeneous system C g_m^T + g_m C = 0, solved over
                a general 4x4 complex matrix by SVD, has NULL-SPACE
                DIMENSION 1; a representative is g0 g2; C^T = -C.
                **An earlier version of this record cited a 16-element
                basis search instead — a proxy that cannot exclude a
                linear combination. The null space was computed.**
    CONFIRMED   reconstruction exact, rank 256/256, off-diagonal
                residual ~1e-14, for both the scalar and pseudoscalar
                canonical terms
    CONFIRMED   per-component family sums  S -1/2, P -1/2, T ±1/2,
                V 0, A 0
    CONFIRMED   four A/T convention variations leave V and A at zero

**These are method B's own numbers, not a claim that method B is
right.** **A5 requires you to construct it from §2 and measure it
yourself**; if your construction disagrees with this record, **that is
itself a finding and you should report it rather than adopting either.**
