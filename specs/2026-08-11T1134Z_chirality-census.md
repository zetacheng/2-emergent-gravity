# Task specification — the chirality census: why S, P and T vanish in both channels

Specification evidence base: `8701a97a6bb58550d4300f75c10638b057335731`

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**Rules 1–17 are in force**, so this task is governed by Rule 15: its
pre-execution review is a committed artifact — see A0 commit 2 and A2.

**`AGENTS.md` research rule 3 applies:** a derivation note before
production code.

**This task explains a result the programme already has.** **It
introduces no new programme coefficient or channel-character result**;
any coefficients it computes are **diagnostic reproductions used only to
test the structural explanation**, and it decides no convention.

---

## 0. What is being explained, and why it is worth a task

Two independent decompositions of the frozen `S² + P²` interaction, in
two different channels, both give:

    channel                S    P    T      V       A
    particle-hole          0    0    0    -G/4    -G/4
    particle-particle      0    0    0    +c      -c

**S, P and T vanish in both. That parallel has never been explained**,
and the programme currently holds it as two separate numerical facts.

**Their status differs, and this task must not blur it.** The
particle–hole coefficients are on `main` and pinned at A1. **The
particle–particle coefficients were produced and adjudicated on an
UNINTEGRATED branch; they are NOT authoritative main-line input to this
task**, and A1 forbids reading them. **They are context for why the
question is worth asking, not evidence this task may rest on.**

**A candidate explanation exists and is stated in §1.** It is a counting
argument over chirality, not a cancellation of numbers. **If it holds,
it is a stronger result than either coefficient table**: it says which
interactions have this property without decomposing them, and it
predicts when the property fails.

**This task tests that argument. It may fail**, and a failure is a
result — §5 says how to report it.

## 1. The candidate explanation, stated so it can be falsified

**Step 1 — the interaction factorises on chirality.** With the frozen
pseudoscalar operator `P = iγ₅`:

    S² + P²  =  4 (psibar_L psi_R)(psibar_R psi_L)

**and without the i, for contrast:**

    S² + (gamma5 term)²  =  2[(psibar_L psi_R)² + (psibar_R psi_L)²]

**Step 2 — the chirality census.**

    frozen   psibar_L , psi_R , psibar_R , psi_L    one of each
    no i     psibar_L , psi_R , psibar_L , psi_R    two of each, doubled

**Step 3 — the rearrangement.** A Fierz rearrangement re-pairs the four
fields. **Under the CROSSED particle–hole pairing**, `(ψ̄_L ψ_R)(ψ̄_R
ψ_L)` is re-grouped as `(ψ̄_L ψ_L)(ψ̄_R ψ_R)` — **same-chirality
bilinears.**

**The selection rule is what is strict.** *"The `ψ_R` is taken by the
`ψ̄_R`"* is intuition, not the argument; **the argument is the
projector algebra of Step 4**, and Step B measures it.

**Step 4 — which families are which, and the classification is NOT the
same in the two pairings.**

    particle-hole    psibar Gamma psi
      S, P, T        opposite-chirality  (Gamma commutes with g5)
      V, A           same-chirality      (Gamma anticommutes)

    particle-particle    psi^T C^-1 Gamma psi
      S, P, T        SAME-chirality qq
      V, A           OPPOSITE-chirality qq

**The two are INVERTED**, and the reason is the frozen relation
`C γ₅^T C⁻¹ = +γ₅`, which gives `P_X^T C⁻¹ = C⁻¹ P_X`. **An earlier
draft of this specification carried the particle–hole table into the
particle–particle channel unchanged. That was wrong**, and Step B exists
to establish each independently.

**Step 5 — the conclusion, reached twice by different routes.**

    PH:  re-pairing gives psibar_L psi_L and psibar_R psi_R
         -> SAME-chirality ph bilinears  -> V, A

    PP:  the two psi fields are psi_L and psi_R
         -> OPPOSITE-chirality qq pair   -> V, A

**Both select V and A, from the same census, through inverted
classifications.** **S, P and T vanish because nothing can form them**,
not because numbers cancel. **Under the doubled census the argument runs
the other way**, which is the ablation's observed behaviour.

**What the argument does NOT explain.** The relative sign between the
channels — `V = +A` in particle–hole against `V = −A` in
particle–particle. **A census does not distinguish them**, and this task
does not attempt to.

## 2. What to compute

**Step A — the factorisation, verified not asserted.** Show
`S² + P² = 4(ψ̄_L ψ_R)(ψ̄_R ψ_L)` as an identity on the rank-4 Dirac
tensor, and the no-`i` counterpart. **Report the residual.**

**Step B — the family chirality classification**, computed from the
frozen basis elements, not quoted. For each of S, P, V, A, T report
whether `P_R Γ P_L` and `P_R Γ P_R` vanish, and hence whether the
bilinear is same- or opposite-chirality.

**Step C — chirality support, computed separately for each pairing and
WITHOUT choosing a particle–particle ordering.**

    C1  particle-hole:  the COMPLETE 2x2 table
        P_X Gamma P_Y   for X, Y in {L, R}   -- all four entries

    C2  particle-particle:  the COMPLETE 2x2 table
        P_X^T C^-1 Gamma P_Y   for X, Y in {L, R}   -- all four

**Report all four entries in each table even where symmetry makes some
redundant.** **This task exists partly to eliminate projector-placement
error**, and a table with entries omitted because they *follow* is
half-inferred rather than measured. **The cost is negligible; the
protection is not.**

**C2 is a structural question about which chirality pairs a kernel can
carry.** **It requires NO Fierz crossing, NO Grassmann ordering and NO
diquark normalisation** — which is why this task can ask it while those
conventions remain unfrozen. **Do not perform a particle–particle
coefficient decomposition**, and **do not choose a slot map.**

**C3 — the census of the frozen source**, computed: which chiral fields
`S² + P²` contains, and with what multiplicity.

**Then state, for each pairing, which families the census can and cannot
supply**, and compare with the recorded particle–hole coefficients.

**A note on what would NOT be evidence.** Projecting the frozen source
onto an LL/RR-type source sector and finding zero is **close to
tautological**: `S² + P² = 4(ψ̄_L ψ_R)(ψ̄_R ψ_L)` has no such component
to begin with. **Report it if you compute it, but do not present it as
support.** §2's Step D carries the falsification.

**Step D — THE FALSIFICATION TEST, and this task's primary evidence.**

**The no-`i` interaction changes the census** — from one field of each
chirality to two of each — **and the adjudication already recorded that
the support moves from V/A to S/P/T.** **That is the discriminating
experiment**, because the source sector genuinely differs rather than
being projected out of something that never contained it.

State the argument's criterion in a form applicable to an interaction
**without decomposing it**, then:

    D1  predict the no-i interaction's support from the census ALONE,
        BEFORE computing it
    D2  compute it, in the particle-hole pairing
    D3  report whether the prediction was right

**Record the prediction before the computation, in that order**, and say
so. **A criterion stated after seeing the answer is not a prediction.**

**D4 — a second interaction, freely chosen by you**, with the same
predict-then-compute discipline, and **your reason for choosing it.**

**The evidence is NOT symmetric between the channels, and the report
must say so.**

    particle-hole        structural selection (C1) AND numerical
                         falsification (D)
    particle-particle    structural selection (C2) ONLY

**The no-`i` coefficient decomposition is a particle–hole falsification
test only.** For the particle–particle pairing this task tests the
census **structurally**, through C2 and C3, and **performs no
coefficient decomposition, because that would require an unfrozen pp
ordering.** **Do not present the two channels as equally tested.**

**Step E — what the argument fails to explain**, stated explicitly: the
`V = +A` versus `V = −A` distinction, and anything else you find it
silent on.

## 3. Conventions

**Use the frozen conventions**, and quote them from the pinned freeze:
the canonical pseudoscalar operator carries `i·γ₅`, and the A and T
family basis elements each carry an explicit factor of `i`.

**These are load-bearing here in a way they were not before.** The
adjudication established that dropping them moves the surviving support
from V/A to S/P/T. **Verify by quotation that the freeze says what this
specification says it says. If it does not, STOP.**

**Chirality projectors.** `P_L = (1 − γ₅)/2`, `P_R = (1 + γ₅)/2`, with
`γ₅` the frozen `γ₀γ₁γ₂γ₃`. **Note that `ψ̄_L = ψ̄ P_R`**, so a
`ψ̄_L Γ ψ_R` bilinear corresponds to `P_R Γ P_R`. **A sign or projector
placement error here inverts the whole classification** — Step B exists
to catch it, and **an earlier informal analysis did make exactly this
error.**

## 4. Representation independence

**Chirality is not a property of the gamma representation.** Run Step C
in two inequivalent-looking representations and confirm the family
tables agree. **If they do not, the classification is representation-
dependent and the argument fails** — report that rather than choosing a
representation.

## 5. If the argument fails

**A failure is a result and must be reported as one**, not repaired.

    Step A residual non-zero        the factorisation is wrong; the
                                    argument has no premise
    Step C does not match           the census does not control the
                                    outcome; report what does vary
    Step D mispredicts              the criterion is not sufficient;
                                    report the counterexample

**Do not adjust the argument to fit the data.** **If it survives, say
what it now licenses; if it does not, say what killed it.**

## 6. What must not be concluded

- **Do not state that a composite vector exists or is absent.** This is
  a structural argument about which operators can form, **not a
  bound-state calculation.**
- **Do not state that the diquark channel is settled.** `η`, the
  particle–particle Grassmann ordering and the diquark normalisation
  remain unfrozen, and **the two branches carrying that computation are
  not integrated.**
- **Do not select a Hubbard–Stratonovich channel** or revisit the
  2026-08-09 rulings.
- **Do not claim the census explains the inter-channel sign.** §1 says
  it does not.
- **Do not restate either coefficient table as this task's result.**
  This task explains a pattern; it does not re-derive the numbers.

## 7. Acceptance criteria

**A0 — Commit order and paths, frozen.**

    commit 1  specs/2026-08-XXT{HHMM}Z_chirality-census.md
    commit 2  reviews/chatgpt/2026-08-XXT{HHMM}Z_chirality-census.md
    commit 3  derivations/P2-PHASE-01_chirality_census.md
    commit 4  scripts/p2_chirality_census.py,
              results/P2-PHASE-01/chirality-census/census.json,
              tests/test_p2_chirality_census.py
    commit 5  reports/2026-08-XXT{HHMM}Z_chirality-census.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused; `XX` is the
day at execution. **You choose no path.** **Commit 2 precedes the
work**; **commit 3 precedes production code.**

**A1 — Pinned inputs**, verified before use; a mismatch is a STOP.
Method: `git cat-file blob <rev>:<path> | sha256sum`.

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a

    derivations/P2-PHASE-01_channel_character.md
    380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f

    results/P2-PHASE-01/channel-character/channel_character.json
    093d20c0e01dc5626cafb4da9b5a0d0e5e95edbd0a8853bbc562248a5b36ee7f

**The particle–particle numbers are NOT pinned here** and are not an
input. **They live on an unintegrated branch**, and this task's Step C
recomputes the pp side itself. **Do not read from
`gate/p2-diquark-both-eta` or `gate/p2-diquark-adjudication`.**

**A2 — This task's pre-execution review committed, unedited**, at the
`reviews/chatgpt/` path of A0. The delimiters are these two lines, each
occupying a whole line:

    === REVIEW ARTIFACT BEGINS ===
    === REVIEW ARTIFACT ENDS ===

**Match them as COMPLETE LINES**, not as first occurrences of the
string — this specification contains them. **Exclude any preamble
before the BEGIN line, the delimiter lines, and any accompanying
instruction.** **Placeholders inside the review's text stay as
written**; resolve them in the path only. **If the supplied text is
missing, has no delimiters, or does not correspond to this
specification, STOP and say which.**

**A3 — Frozen conventions quoted**, per §3, with occurrence counts.

**A4 — Step A verified**, with the residual reported, for both the
frozen and no-`i` combinations.

**A5 — Step B computed**, with the projector placement shown explicitly
and the `ψ̄_L = ψ̄ P_R` correspondence stated.

**A6 — Step C delivered as C1, C2 and C3**, with the particle–hole and
particle–particle classifications **established separately** and shown
inverted. **Both tables report all four `X, Y ∈ {L, R}` entries**, none
omitted as redundant. **No particle–particle coefficient decomposition
is performed and no slot map is chosen** — confirm both explicitly.

**A7 — Step D: prediction recorded BEFORE computation** for the no-`i`
interaction and for one of your choosing, with each marked correct or
not, and **the ordering of prediction and computation evidenced.**

**A8 — Step E: what the argument does not explain**, including the
inter-channel sign.

**A9 — Representation independence** per §4, in two representations.

**A10 — Deliverables**: derivation note, script, results artifact, test
file, report.

**Tests required**, all computed rather than hard-coded:

    Step A's factorisation identity, both with and without the i
    Step B/C1's particle-hole classification, all four entries
    Step C2's particle-particle classification, all four entries,
      and that it is INVERTED relative to C1
    Step D's no-i prediction, as a test that the criterion and the
      computed support agree

**The LL/RR-restriction check is NOT a required test.** §2 explains why
it is close to tautological; **a test of it would lock in a proxy.**

**A11 — Scope**, seven additions:

    add:
      specs/2026-08-XXT{HHMM}Z_chirality-census.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_chirality-census.md
      derivations/P2-PHASE-01_chirality_census.md
      scripts/p2_chirality_census.py
      results/P2-PHASE-01/chirality-census/census.json
      tests/test_p2_chirality_census.py
      reports/2026-08-XXT{HHMM}Z_chirality-census.md
    modify: []
    forbidden_operations:
      delete, rename, copy, type_change, unmerged, unknown

**Final base-to-head scope: 7 additions and 0 modifications**, matching
the seven paths above. **`tests/` gains exactly one new file and no
existing test is modified.**

**A12 — Nothing pre-existing disturbed.** No gate, gate status, verdict,
digest, hash-pinned artifact, pre-existing test, `GATES.md`,
`CONVENTIONS.md`, `AGENTS.md`, `DECISION_LOG.md` or `pyproject.toml` is
modified. **`P2-PHASE-01` remains `PROPOSED`.**

**A13 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`, `tests/test_p2_channel_character.py`,
and your new test file. **A13-pre** at the pre-report head goes in the
report; **A13-final** at the pushed head is post-report evidence.

**A14 — Lint clean:**
`ruff check scripts/p2_chirality_census.py tests/test_p2_chirality_census.py`.

**A15 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to
`8701a97a6bb58550d4300f75c10638b057335731`; create the branch from that
commit; move no `main` ref. **Local `main` is stale by design.** Report
all three. Push the task branch only. **Delete no branch.**

**A16 — Commit-message hygiene** on every commit: inspect the proposed
message before, the stored message after; permit no `Co-Authored-By`, no
session identifier or URL, no tool attribution. **Report per commit
whether any trailer was suppressed and which.**

## 8. Rule 16 assessment

**Rule 16 is operative and governs this task.** State what the assembled
set does NOT establish, **naming the junction or reporting a search.**

**A candidate, offered so you can confirm or replace it.** If this
argument survives, the repository will hold: two coefficient tables, an
adjudication, and a structural explanation of why S, P and T vanish.
**A reader could conclude the diquark channel is understood.** **It is
not** — `η`, the pp Grassmann ordering and the diquark normalisation
remain unfrozen, **and the branches carrying those coefficients are not
integrated.** The census explains a pattern; **it does not supply a
channel character or a physical conclusion.**

## 9. Evidence layering

**Committed report:** A1–A12, A13-pre, A14, A16 for the earlier commits;
their SHAs and messages; the pre-report head; the intended final
manifest; and the intended report commit message with its authoring-time
trailer suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A13-final, the push, the
report commit's stored message read back from the object, and ancestry
confirmation.

## 10. Invariants and prohibitions

- Executor-writable: the seven paths of A11 only.
- **Do not read from either unintegrated diquark branch.**
- **Do not draw any conclusion §6 forbids.**
- **Do not repair the argument to make it survive.** §5 governs.
- **List every repository input you actually read, by path.**
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: use `gate/p2-chirality-census`.
- Environment: `CONVENTIONS.md` Rule 13's diagnostic order applies.
  **Rule 13 carries two such orders, a known open item; if no
  environment failure occurs, say neither was exercised rather than
  naming one.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 11. Report contract

- raw output for A1–A14, scope-checker JSON verbatim including
  `observed_operations`;
- **Step B first**, since the classification's projector placement
  governs everything after it;
- Step A's residuals; **Step C's C1, C2 and C3 in full**, with the two
  classifications shown side by side and their inversion visible;
- **Step D's criterion, and each prediction marked correct or not** —
  including the freely chosen interaction and why you chose it;
- Step E, and anything else the argument is silent on;
- the representation-independence result;
- **whether the argument survived**, stated plainly, **and if it did
  not, what killed it**;
- **whether you were tempted to adjust the argument** at any point, and
  what you did instead. **This task's failure mode is an explanation
  that fits because it was fitted**;
- **§8's Rule 16 assessment**, junction named or search described;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.

## 12. Pre-issue literal verification record

**Executed by the specification author before issue, per Amendment H.**

    target      a scratch construction, not the repository
    method      direct tensor identity and least-squares decomposition
    check type  NUMERICAL, tolerance 1e-9

    CONFIRMED   S² + P²  =  4 (psibar_L psi_R)(psibar_R psi_L)  exactly,
                with the frozen P = i*gamma5
    CONFIRMED   S² + (gamma5 term)²  =  2[(LbarR)² + (RbarL)²]  exactly
    CONFIRMED   particle-hole:  S, P, T opposite-chirality;
                                V, A same-chirality
    CONFIRMED   C g5^T C^-1 = +g5, hence P_X^T C^-1 = C^-1 P_X
    CONFIRMED   particle-particle:  S, P, T SAME-chirality qq;
                                    V, A OPPOSITE-chirality qq
                -- INVERTED relative to particle-hole
    CONFIRMED   source restricted to LR reproduces the full result in
                both pairings; restricted to LL/RR gives zero in both.
                **Recorded for completeness only; §2 explains why this
                is close to tautological and is not the evidence.**

**These are the specification author's numbers and are not evidence that
the argument is right.** **A4 through A9 require you to establish each
independently**; **if your result disagrees with this record, that is a
finding and you should report it rather than adopting either.**
