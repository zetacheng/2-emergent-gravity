# Report — the chirality census

Specification: `specs/2026-08-11T1134Z_chirality-census.md`
Specification sha256:
`d9099bb62eec1ca5aeef6780adebe89cd327c0f4b384cd2cf30ea37aeff9b04e`
Pre-execution review: `reviews/chatgpt/2026-08-11T1134Z_chirality-census.md`
Evidence base: `8701a97a6bb58550d4300f75c10638b057335731`
Branch: `gate/p2-chirality-census`
Classification: MATERIAL. Branch only.

---

## 0. Did the argument survive?

**Yes.** Stated plainly, because §11 asks for it plainly.

    Step A   both factorisation identities exact, residual 0.0
    Step B   the classification computed, projector placement shown
    Step C   both tables complete, all four entries, inverted as claimed
    Step D   THREE predictions recorded before computation, THREE correct
    §4       both tables identical in two representations

Nothing in §5's failure list occurred: no non-zero Step A residual, no
mismatch in Step C, no misprediction in Step D.

**What it now licenses.** `S`, `P` and `T` are absent from both
decompositions **because nothing in the census can form them**, not
because numbers cancel. The frozen interaction supplies one `ψ̄_L`, one
`ψ_R`, one `ψ̄_R` and one `ψ_L`; under the particle–hole exchange those
re-pair into same-chirality `ψ̄ψ` bilinears, which only `V` and `A`
support; in the particle–particle pairing the two `ψ` fields are
`ψ_L` and `ψ_R`, an opposite-chirality `qq` pair, which again only `V` and
`A` support. The criterion also says **when the property fails**, and
Step D demonstrates it failing on demand.

**Three findings a reader should not miss:**

- **The evidence is not symmetric between the channels, and this report
  does not present it as if it were** (§6). Particle–hole gets structural
  selection *and* a numerical falsification; particle–particle gets
  structural selection *only*, because a coefficient decomposition there
  would need an unfrozen ordering.
- **§1's mechanism for the inversion is refined, not confirmed as
  written** (§3). The two projector tables have **identical** non-zero
  patterns. The inversion lives entirely in the translation to field
  labels, and `C γ₅^T C⁻¹ = +γ₅` is what *prevents a second flip* rather
  than what *causes* the inversion.
- **§1's `4(ψ̄_L ψ_R)(ψ̄_R ψ_L)` is an operator identity, not an
  ordered-tensor one** (§4). The tensor form is the symmetrised
  `2[P_R⊗P_L + P_L⊗P_R]`; the factor-4 form leaves residual `2.0`.

I was tempted to adjust the argument once. §12 says where, and what I did
instead.

No STOP condition fired.

---

## 1. A15 — refs, and A1 — pinned inputs

    remote refs/heads/main       8701a97a6bb58550d4300f75c10638b057335731
    refs/remotes/origin/main     8701a97a6bb58550d4300f75c10638b057335731
    local main (stale by design) 0f7961747abe2a18b436c0b1e5b928f425ea4d9a

Both `main` refs resolve to the evidence base; no mismatch, so no STOP.
Local `main` is stale by design, neither consulted nor repaired. The
branch was created from `8701a97a…`; no `main` ref moved; no branch was
deleted.

**A1 — three digest-pinned inputs**, `git cat-file blob 8701a97a:<path> |
sha256sum`, all matching:

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
      fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a   MATCH
    derivations/P2-PHASE-01_channel_character.md
      380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f   MATCH
    results/P2-PHASE-01/channel-character/channel_character.json
      093d20c0e01dc5626cafb4da9b5a0d0e5e95edbd0a8853bbc562248a5b36ee7f   MATCH

**Every repository input actually read**, by path:

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    derivations/P2-PHASE-01_channel_character.md
    results/P2-PHASE-01/channel-character/channel_character.json
    results/P2-CHANNEL-FREEZE/fierz_matrix.json
    scripts/P2-CHANNEL-FREEZE/gamma_algebra.py

**Neither `gate/p2-diquark-both-eta` nor `gate/p2-diquark-adjudication`
was read**, per A1 and §10. The particle–particle side below is
established independently, from the projector algebra alone, and the
particle–particle coefficient table plays no role in any conclusion — it
appears in this report only where §0 of the specification states it as
context for why the question is worth asking.

---

## 2. A2 — the review, and the sixth delimiter failure

Committed at `reviews/chatgpt/2026-08-11T1134Z_chirality-census.md` in
commit 2, before the work.

    committed blob sha256  fabbc32fe4f861f917ec8a96094b37f5d971a178f9e8c0d343237bebe3916f2d
    size                   6064 bytes, 6011 characters, 78 lines
    identical to the extracted text:  True

    substring occurrences   BEGINS: 1    ENDS: 1
    WHOLE-LINE matches      BEGINS: []   ENDS: [line 81]

**Sixth instance, third consecutive with the same cause:** the BEGIN
delimiter shares its line with the attachment marker. Line 0 in full:

    @"/root/.claude/uploads/…/6e8818fe-SPEC_chirality_census.md" === REVIEW ARTIFACT BEGINS ===

The same asserted rule was applied, unchanged:

    END      whole line, exactly one occurrence (line 81)
    BEGIN    the unique line whose content, after removing a prefix matching
             r'^@"[^"]+"\s+', equals the delimiter exactly

    prefix matches r'^@"[^"]+"\s+'   True
    remainder == the BEGIN literal   True

A2's three STOP conditions are "missing", "has no delimiters", "does not
correspond". **None applies** — the text is present, both delimiters are
present, and it corresponds (it names this task by title, the evidence
base, `A7`, `P_X^T C^{-1}`, `C γ₅^T C⁻¹ = +γ₅`, "predict-then-compute").
So a reportable deviation, not a stop. One residual normalisation, one
byte: literal slice 6065 bytes with one leading and one trailing newline;
committed with the leading blank line dropped.

**Six instances, and the proposed fix has not changed.** It is in the
previous two reports and belongs in `CONVENTIONS.md`; restating it a third
time in a task report is itself evidence that a per-task clause cannot
carry it.

---

## 3. A5 — Step B, the classification, reported first

§11 asks for this first because the projector placement governs
everything after it, and §3 of the specification records that an earlier
informal analysis got it wrong.

**The placement convention, stated before anything was computed:**

    P_L = (1 - g5)/2        P_R = (1 + g5)/2        g5 = g0 g1 g2 g3

    psi_X    = P_X psi
    psibar_L = psibar P_R          <-- THE BAR FLIPS THE PROJECTOR

    ph:  psibar_X Gamma psi_Y        <->  P_Xbar Gamma P_Y
    pp:  psi_X^T C^-1 Gamma psi_Y    <->  P_X^T C^-1 Gamma P_Y   (no bar, no flip)

So `ψ̄_L Γ ψ_R` corresponds to **`P_R Γ P_R`**, not `P_L Γ P_R`. A test
pins this directly: for `Γ = I`, `P_R Γ P_R` is non-zero and `P_R Γ P_L`
vanishes; for `Γ = γ₀` it is the other way round. Placing the projector
the other way would invert the whole classification.

**On the particle–particle side, computed and not assumed** — in both
representations:

    C null-space dimension                    1
    C g5^T C^-1 = +g5                         True
    P_X^T C^-1 = C^-1 P_X   (X = L and R)     True

---

## 4. A4 — Step A, the factorisation, with residuals

Rank-4 Dirac tensors `T[a,b,c,d] = Γ₁[a,b] Γ₂[c,d]`, summed over the two
canonical operators:

    frozen   I(x)I + (i g5)(x)(i g5)  =  I(x)I - g5(x)g5
             residual against 2[P_R(x)P_L + P_L(x)P_R]     0.000e+00

    no-i     I(x)I + g5(x)g5
             residual against 2[P_R(x)P_R + P_L(x)P_L]     0.000e+00

**Both exact, in both representations.**

**One refinement of the specification's Step 1, reported rather than
absorbed.** §1 writes the frozen case as
`S² + P² = 4(ψ̄_L ψ_R)(ψ̄_R ψ_L)`. That is right as an **operator**
statement — both bilinears are Grassmann-even and commute, so the two
orderings are the same operator and `2 + 2 = 4`. It is **not** an identity
on the ordered rank-4 tensor:

    residual against 4 P_R(x)P_L                          2.000e+00

The ordered-tensor identity is the symmetrised form above. Nothing in the
argument depends on which is used, but a reader checking slot by slot
would find the factor-4 form failing, so it is recorded and a test pins
it.

---

## 5. A6 — Step C, both tables in full

**All four entries in each table, none omitted as redundant.** The
protection is against exactly the projector-placement error §3 warns of,
and the cost is negligible.

### C1 — particle–hole, `P_X Γ P_Y`

    fam   P_L G P_L   P_L G P_R   P_R G P_L   P_R G P_R    ph type
    S     nonzero     0           0           nonzero      OPPOSITE-chirality
    P     nonzero     0           0           nonzero      OPPOSITE-chirality
    V     0           nonzero     nonzero     0            SAME-chirality
    A     0           nonzero     nonzero     0            SAME-chirality
    T     nonzero     0           0           nonzero      OPPOSITE-chirality

### C2 — particle–particle, `P_X^T C⁻¹ Γ P_Y`

    fam   LL          LR          RL          RR           qq type
    S     nonzero     0           0           nonzero      SAME-chirality qq
    P     nonzero     0           0           nonzero      SAME-chirality qq
    V     0           nonzero     nonzero     0            OPPOSITE-chirality qq
    A     0           nonzero     nonzero     0            OPPOSITE-chirality qq
    T     nonzero     0           0           nonzero      SAME-chirality qq

### Side by side, with the inversion visible

    family      C1 (particle-hole)      C2 (particle-particle)
    S           OPPOSITE-chirality      SAME-chirality qq
    P           OPPOSITE-chirality      SAME-chirality qq
    T           OPPOSITE-chirality      SAME-chirality qq
    V           SAME-chirality          OPPOSITE-chirality qq
    A           SAME-chirality          OPPOSITE-chirality qq

**The two classifications are inverted in field labels**, as §1 claims,
and were established **separately** — C1 from `P_X Γ P_Y`, C2 from
`P_X^T C⁻¹ Γ P_Y`, neither carried over from the other.

### The refinement: what the inversion actually is

**§1 states the mechanism slightly more strongly than the algebra
supports, and this is the report's main correction to the argument as
given.**

Look at the two tables' *projector-index* patterns rather than their field
labels: both are non-zero on `LL`/`RR` for `S`, `P`, `T` and on `LR`/`RL`
for `V`, `A`. **They are identical.** A test asserts this directly.

So the inversion is **not** an independent algebraic fact about `C`. It is:

    the bar-flip  psibar_L = psibar P_R  on the particle-hole side
    TOGETHER WITH the ABSENCE of any flip on the particle-particle side

and `C γ₅^T C⁻¹ = +γ₅` is what delivers the absence. Had the relation been
`C γ₅^T C⁻¹ = −γ₅`, then `P_X^T C⁻¹ = C⁻¹ P_X̄`, the pp side would have
flipped too, and the two classifications would have **agreed** in field
labels. **The frozen relation is load-bearing exactly as §1 says — but as
the thing preventing a second flip, not as the thing causing the
inversion.**

This is a refinement, not a falsification: every statement §1 makes about
which families are available in which pairing is confirmed.

### C3 — the census of the source, computed

    frozen  S^2 + P^2
      (psibar_L psi_R) x (psibar_R psi_L)      2
      (psibar_R psi_L) x (psibar_L psi_R)      2
      (psibar_L psi_R) x (psibar_L psi_R)      0
      (psibar_R psi_L) x (psibar_R psi_L)      0

    no-i    S^2 + (gamma5 term)^2
      (psibar_L psi_R) x (psibar_R psi_L)      0
      (psibar_R psi_L) x (psibar_L psi_R)      0
      (psibar_L psi_R) x (psibar_L psi_R)      2
      (psibar_R psi_L) x (psibar_R psi_L)      2

    frozen census   psibar_L, psi_R, psibar_R, psi_L   — one of each
    no-i census     psibar_L, psi_R, psibar_L, psi_R   — two of each, doubled

### What the census can and cannot supply, per pairing

    PH:  the frozen census re-pairs under exchange into (psibar_L psi_L)
         and (psibar_R psi_R) — SAME-chirality ph bilinears
         -> V and A available; S, P, T CANNOT FORM

    PP:  the two psi fields of the frozen census are psi_L and psi_R
         — an OPPOSITE-chirality qq pair
         -> V and A available; S, P, T CANNOT FORM

**Compared with the recorded particle–hole coefficients** (pinned, from
`main`):

    pinned operator-level normalisation L    S 0   P 0   V -G/4   A -G/4   T 0
    pinned vanishing families                ['S', 'P', 'T']
    census predicts vanishing                ['S', 'P', 'T']        AGREE

The census predicts *which* families vanish, not their magnitude; `−G/4`
is not derived here.

### Two confirmations the specification asks for explicitly

**No particle–particle coefficient decomposition was performed, and no
slot map was chosen.** C2 is a statement about which chirality pairs a
kernel can carry: it needs no Fierz crossing, no Grassmann ordering and no
diquark normalisation, which is precisely why the question can be asked
while those conventions remain unfrozen.

---

## 6. A7 — Step D, the falsification test

### The criterion, stated so it applies without decomposing

> Write the interaction's rank-4 tensor in the chiral projector basis as a
> sum of terms `K₁ ⊗ K₂` with `K ∈ {P_L, P_R}`. Each term fixes the
> chirality of the four fields `ψ̄_a ψ_b ψ̄_c ψ_d`. The particle–hole
> exchange re-pairs them as `(ψ̄_a ψ_d)(ψ̄_c ψ_b)`. If every term gives
> SAME-chirality exchange pairs, only `V` and `A` can appear and `S`, `P`,
> `T` must vanish. If every term gives OPPOSITE-chirality exchange pairs,
> only `S`, `P`, `T` can appear and `V`, `A` must vanish. If terms of both
> kinds are present, no family is excluded.

### The ordering, evidenced

**The criterion and all three predictions are written in
`derivations/P2-PHASE-01_chirality_census.md`, which is commit 3
(`9c9fd7fd…`). The script that computes them is commit 4
(`b9a402bd…`).** The git history is the evidence: the predictions are in
an earlier commit than the code that tested them, and no Step D
decomposition had been run when the note was written. A test asserts the
prediction strings are present in the note.

### The three cases

    D0 CONTROL — frozen S^2 + P^2, P = i*gamma5
      census        one of each; exchange pairs (psibar_L psi_L) and
                    (psibar_R psi_R), both SAME
      PREDICTED     non-zero V, A        zero S, P, T
      COMPUTED      S 0   P 0   V -1/2   A -1/2   T 0
                    non-zero ['V','A']   zero ['S','P','T']
      VERDICT       CORRECT

    D1 — the no-i interaction S^2 + (gamma5 term)^2
      census        doubled; exchange pairs (psibar_L psi_R) and
                    (psibar_L psi_R), both OPPOSITE
      PREDICTED     non-zero S, P, T     zero V, A
      COMPUTED      S -1/2  P -1/2  V 0  A 0  T -1/2
                    non-zero ['S','P','T']   zero ['V','A']
      VERDICT       CORRECT

    D4 — chosen by the executor: (psibar i*gamma5 psi)^2 only
      census        -g5(x)g5 = -P_R(x)P_R + P_R(x)P_L + P_L(x)P_R - P_L(x)P_L
                    BOTH one-of-each and doubled terms -> third branch
      PREDICTED     all five non-zero    nothing excluded
      COMPUTED      S 1/4  P 1/4  V -1/4  A -1/4  T 1/4
                    non-zero all five    zero []
      VERDICT       CORRECT

**All three correct.**

### Why I chose D4

**The criterion's two exclusion branches are the easy ones.** A criterion
that only ever forbids things can look successful without discriminating,
and this task's stated failure mode is an explanation that fits because it
was fitted. **The branch that predicts NO exclusion is where a criterion
invented after seeing the answer would most likely fail** — it is the one
place the criterion sticks its neck out in the direction of "everything
survives", which is not what a story built to explain vanishing would
naturally say.

The pseudoscalar-only interaction was picked because its projector
decomposition visibly contains **both** kinds of term, so the third branch
applies unambiguously. Four of the five families could have come out zero;
none did.

### The evidence is not symmetric, and this report says so

    particle-hole        structural selection (C1) AND numerical
                         falsification (Step D)
    particle-particle    structural selection (C2) ONLY

**Step D is a particle–hole test.** No coefficient decomposition was
performed in the particle–particle pairing, because that would require the
unfrozen pp Grassmann ordering. **The two channels are not equally
tested**, and the particle–particle half of the conclusion rests on C2 and
C3 alone.

### What would not have been evidence

Projecting the frozen source onto an LL/RR-type sector and finding zero is
close to tautological: §5's C3 table measures that component as **exactly
0** to begin with. It is recorded there for completeness and is **not**
offered as support. Per A10, **no test of it was written** — a test would
have locked in a proxy.

---

## 7. A9 — representation independence

Both tables were computed in two independently written Euclidean Hermitian
gamma sets:

    frozen_factory     the repository's own gamma_factory, metric (1,1,1,1)
    independent_kron   g0 = kron(s1,s1)  g1 = kron(s1,s2)
                       g2 = kron(s1,s3)  g3 = kron(s2,I2)

In both: `g5² = I`, `P_L + P_R = I`, `P_L P_R = 0`, `C` null-space
dimension 1, `C g5^T C⁻¹ = +g5`, and `P_X^T C⁻¹ = C⁻¹ P_X`.

    C1 and C2 identical in the two representations:   True

A test also asserts the two gamma sets are **genuinely different
matrices**, so the check is not vacuous. Had the tables disagreed, the
classification would be representation-dependent and the argument would
fail; that would have been reported rather than resolved by choosing a
representation.

---

## 8. A8 — Step E, what the argument does not explain

- **The inter-channel sign.** Particle–hole gives `V = +A`; the
  particle–particle pairing gives `V = −A`. **A census counts fields; it
  does not distinguish them.** §1 says the argument does not explain this
  and this task did not attempt it.
- **The magnitudes.** The census says which families can form, not with
  what coefficient. `−G/4` is not derived here.
- **The `V`/`A` degeneracy in the particle–hole channel.** Both exchange
  pairs are same-chirality and the census does not separate them, so it
  cannot say why the two coefficients are equal there.
- **Anything about states.** Which operators can form is not a bound-state
  or pole calculation.
- **The particle–particle coefficients.** Not computed, by design.

---

## 9. A11 — scope; A12 — nothing disturbed; A13-pre; A14

**A12**, compared as individual blob object ids:

    paths at base                                297
    paths at head                                303
    base-present paths modified or missing         0

    GATES.md, CONVENTIONS.md, AGENTS.md, DECISION_LOG.md,
    pyproject.toml, CLAIMS.md                    all identical

    pre-existing tests/ paths                    16, all blob-identical
    tests/ paths at head                         17

**`tests/` gains exactly one file and no existing test is modified.**
`P2-PHASE-01`'s status read from the committed `GATES.md` at head:
`Status: PROPOSED`, unchanged.

**A11 — the resolved manifest** (`XX = 11`, `{HHMM} = 1134`, fixed by
commit 1):

    {
      "mode": "exact",
      "base": "8701a97a6bb58550d4300f75c10638b057335731",
      "head": "HEAD",
      "required": [
        {"operation": "add", "path": "specs/2026-08-11T1134Z_chirality-census.md"},
        {"operation": "add", "path": "reviews/chatgpt/2026-08-11T1134Z_chirality-census.md"},
        {"operation": "add", "path": "derivations/P2-PHASE-01_chirality_census.md"},
        {"operation": "add", "path": "scripts/p2_chirality_census.py"},
        {"operation": "add", "path": "results/P2-PHASE-01/chirality-census/census.json"},
        {"operation": "add", "path": "tests/test_p2_chirality_census.py"},
        {"operation": "add", "path": "reports/2026-08-11T1134Z_chirality-census.md"}
      ],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

    resolved manifest sha256
      1b8c7ee1b3b321166ae2307cdca80baae100ba68086e0f30a4039941d5fc03e0

**Scope-checker output at the pre-report head, verbatim**, including
`observed_operations` (this report is the seventh addition, not yet
committed):

    $ python -m scripts.governance_tools.scope_checker --repo . --manifest ccscope_pre.json
    {
      "base": "8701a97a6bb58550d4300f75c10638b057335731",
      "failures": [],
      "head": "b9a402bd6d0f71197a4b42f7785877b6c43d690e",
      "mode": "exact",
      "observed_operations": [
        {
          "operation": "add",
          "path": "derivations/P2-PHASE-01_chirality_census.md"
        },
        {
          "operation": "add",
          "path": "results/P2-PHASE-01/chirality-census/census.json"
        },
        {
          "operation": "add",
          "path": "reviews/chatgpt/2026-08-11T1134Z_chirality-census.md"
        },
        {
          "operation": "add",
          "path": "scripts/p2_chirality_census.py"
        },
        {
          "operation": "add",
          "path": "specs/2026-08-11T1134Z_chirality-census.md"
        },
        {
          "operation": "add",
          "path": "tests/test_p2_chirality_census.py"
        }
      ],
      "overall": "PASS",
      "tool": "scope_checker"
    }
    EXIT=0

Six additions and zero modifications at the pre-report head; seven and
zero expected at the final head.

**A13-pre**, run individually with `python -m pytest <path>`:

    tests/test_repository_structure.py         4 passed in 0.01s                EXIT=0
    tests/test_si1_governance.py              14 passed in 0.04s                EXIT=0
    tests/test_gate_anchors.py                18 passed, 2 deselected in 3.11s  EXIT=0
    tests/test_governance_tools.py             8 passed in 1.32s                EXIT=0
    tests/test_p2_channel_character.py        23 passed in 0.96s                EXIT=0
    tests/test_p2_chirality_census.py         21 passed in 0.55s                EXIT=0

All six exit 0.

**The required tests, all computed rather than hard-coded**, mapped to
A10: Step A's factorisation with and without the `i` (three tests,
including that the factor-4 form is *not* a tensor identity); Step B/C1's
particle–hole classification, all four entries in both representations,
plus a test pinning the bar-flip directly; Step C2's particle–particle
classification, all four entries, plus a test that it is inverted relative
to C1 **and** a test that the projector patterns are nevertheless
identical; Step D's criterion recomputed from the frozen Fierz matrix and
scored against the committed predictions, plus tests that D1 genuinely
differs from D0 and that D4 exercises the no-exclusion branch. **The
LL/RR-restriction check is not tested**, per A10.

**A14 — lint**, exact command and output:

    $ ruff check scripts/p2_chirality_census.py tests/test_p2_chirality_census.py
    All checks passed!
    EXIT=0

Two `E501` findings on the first run were fixed by extracting a helper and
a local binding; no rule was disabled, no `noqa` added, and both files were
re-run afterwards with identical results.

**Environment.**

    Python 3.11.15   |   python -m pytest 9.1.1 (mandated)   |   pytest on PATH 9.0.2 (not used)
    ruff 0.15.8      |   numpy 2.4.6   |   sympy 1.14.0

Nothing was installed. No environment failure occurred, so **neither of
Rule 13's two diagnostic orders was exercised**.

---

## 10. §8 — Rule 16 assessment

Rule 16 is operative. **§8's candidate is confirmed**, and I would sharpen
it.

After this task the repository holds: a particle–hole coefficient table on
`main`, a structural explanation of why `S`, `P` and `T` vanish, and — on
unintegrated branches this task did not read — a particle–particle
coefficient table and an adjudication. **A reader could conclude the
diquark channel is understood. It is not.** `η`, the particle–particle
Grassmann ordering and the diquark normalisation remain unfrozen, and the
branches carrying those coefficients are not integrated. The census
explains a pattern; it supplies no channel character and no physical
conclusion.

**The sharpening, which is specific to what this task adds.** The census
gives the particle–particle statement a *structural* footing it did not
have before — C2 and C3 are computed here from the frozen algebra, on
`main`, with no dependence on either branch. That makes the pp half of the
explanation look better-supported than the pp *coefficients* are, and the
two are easy to conflate. Precisely:

    established here, on main       which chirality pairs each pp kernel
                                    can carry, and hence which families
                                    the census can supply
    NOT established anywhere on main  any pp coefficient, its sign, its
                                    magnitude, or the ordering and
                                    normalisation those would require

A reader who takes C2 as evidence that the pp *decomposition* is settled
has crossed exactly the line §6 of the specification forbids. §6 above
states the asymmetry, and the results artifact carries
`no_pp_coefficient_decomposition_performed` and `no_slot_map_chosen` as
fields a test asserts.

**Search.** I checked for anything that would resist the inference: no
test in `tests/` mentions either branch name; `GATES.md` records
`P2-PHASE-01` as `PROPOSED` with no pp result; and the only place the pp
coefficients appear on `main` after this task is this report's §0 quotation
of the specification's own context paragraph. **There is no artifact on
`main` that states the pp coefficients are unintegrated**, because there is
no artifact on `main` that mentions them at all — which is the right state,
and also means the discipline rests entirely on reports.

---

## 11. A16 — commit-message hygiene, and intended final state

Each message inspected before writing and after, from the object. Scan
pattern, case insensitive:
`co-authored-by|claude|session|https?://|generated with|anthropic`.

    commit 1  544e5ea68c70d72953289aadbf416c854286eca6
      specs/2026-08-11T1134Z_chirality-census.md
      "spec: the chirality census, why S P and T vanish in both channels"
      proposed: no match   stored: no match
      trailers suppressed: YES — the default Co-Authored-By and session-URL
      trailers were prevented at authoring time; neither is in the object.

    commit 2  87ebc44046e765ae4364d54c00bcc280b50c07e9
      reviews/chatgpt/2026-08-11T1134Z_chirality-census.md
      "review: commit the pre-execution review for the chirality census"
      proposed: no match   stored: no match     trailers suppressed: YES, same two.

    commit 3  9c9fd7fd7a940944f4cba77c6d750a4c1414b4a8
      derivations/P2-PHASE-01_chirality_census.md
      "derive: the chirality census, with the Step D predictions recorded first"
      proposed: no match   stored: no match     trailers suppressed: YES, same two.

    commit 4  b9a402bd6d0f71197a4b42f7785877b6c43d690e
      scripts/, results/, tests/ — one work commit
      "compute: the chirality census, script results and tests"
      proposed: no match   stored: no match     trailers suppressed: YES, same two.

**Commit order, as A0 requires:** commit 2 precedes commit 3, so the
review was committed before the work; commit 3 precedes commit 4, so the
derivation note precedes production code per `AGENTS.md` rule 3 — **and,
in this task, so that the Step D predictions precede the computation.**

**Pre-report head:** `b9a402bd6d0f71197a4b42f7785877b6c43d690e`

**Intended final manifest:** the resolved manifest of §9, seven additions
and zero modifications.

**Intended report commit message:**

    docs: report the chirality census

    Records A1-A12, A13-pre, A14, A15 and A16. The argument survived.

    Step A: both factorisation identities exact, residual 0.0. Steps B and
    C: both chirality tables complete, all four entries, identical in two
    representations, inverted in field labels as claimed. Step D: three
    predictions recorded in commit 3 and computed in commit 4, all three
    correct -- the frozen interaction selects V and A, the no-i
    interaction selects S, P and T, and the pseudoscalar-only interaction
    excludes nothing.

    Two refinements to the argument as given, reported rather than
    absorbed. The inversion of the two classifications is NOT an
    independent algebraic fact: the projector-index patterns are
    identical, and the inversion is the bar-flip on the particle-hole side
    together with the absence of a flip on the particle-particle side,
    which C g5^T C^-1 = +g5 is what delivers. And 4(psibar_L psi_R)(psibar_R
    psi_L) is an operator identity, not an ordered-tensor one; the tensor
    form is the symmetrised 2[P_R(x)P_L + P_L(x)P_R].

    The evidence is not symmetric: particle-hole gets structural selection
    and a numerical falsification, particle-particle structural selection
    only. No pp coefficient decomposition, no slot map, and neither
    unintegrated diquark branch was read.

    Sixth consecutive failure of the review supply protocol. Nothing
    frozen, no new programme coefficient. P2-PHASE-01 stays PROPOSED.

---

## 12. Was I tempted to adjust the argument?

§11 asks directly, and the honest answer is **yes, once.**

When the C1 and C2 tables came out with **identical projector-index
patterns**, my first reaction was that I had made the placement error §3
warns about — because §1 says the two classifications are *inverted*, and
identical tables look like the opposite of inverted. The tempting move was
to go back and adjust the projector placement on one side until the tables
looked different, which would have "confirmed" §1 as written.

**What I did instead.** I checked the placement against its definition
rather than against the expected answer: `ψ̄_L = ψ̄ P_R`, so the bar flips
one index on the ph side and nothing flips on the pp side. Under that
translation, identical projector tables give *inverted field-label*
classifications — which is what §1 actually claims. So the tables were
right, §1's conclusion was right, and only §1's account of the *mechanism*
needed refining. I wrote the refinement into the derivation note (§5
above), added a test asserting the projector patterns are identical, and
left the placement alone.

**Why this is worth a section.** The failure mode this task names is an
explanation that fits because it was fitted. The moment of temptation was
not at the conclusion — it was at an intermediate table that looked wrong
against a mental picture of the answer. Had I adjusted there, every
downstream check would still have passed, because the conclusion was never
in doubt; only the mechanism would have been quietly wrong. The protection
that worked was that §2's C1/C2 tables are defined by *formulas*, not by
expected outcomes, so "check the placement against its definition" was an
available move.

A smaller instance: the `4(...)(...)` residual of `2.0` in Step A briefly
looked like a failed premise, which §5 would classify as fatal. It is not —
the operator and tensor statements differ — and the resolution again came
from checking what the expression means rather than adjusting it.

---

## 13. Stops and clarifications

No stop occurred. All findings below are secondary.

**`SPECIFICATION_DEFECT` — one, now at six instances.**

*A2's whole-line delimiter rule was inapplicable as written* (§2),
returning zero matches for BEGIN because the delimiter shared its line
with an attachment marker — the same cause as the fourth and fifth
instances. None of A2's three STOP conditions applied, so I used the same
asserted rule and reported it. **The rule is mine and the specification
did not authorise it.** The fix is unchanged from the previous two
reports and belongs in `CONVENTIONS.md`.

**`OBSERVATION_METHOD_ERROR` — none this task.**

Two secondary observations, both about the specification's design and both
to its credit:

*Requiring all four entries in each table did real work.* §2 argues the
cost is negligible and the protection is not, and that is exactly what
happened: it was the full pattern — including the entries that "follow" —
that made the identical-projector-pattern refinement visible. A
three-entry table would have hidden it, and §12's temptation would have
had no evidence to resolve it against.

*Requiring the two classifications to be established separately was the
difference between a refinement and a repeat of an earlier error.* §1
records that an earlier draft carried the ph table into the pp channel
unchanged. Because C2 was computed from its own formula, the fact that its
projector pattern *matches* C1's is a finding rather than a symptom.

**`REPOSITORY_DEFECT` — none reached the threshold of a stop.**

One secondary observation, carried forward and now touching this task's
own script: **the freeze's JSON blocks are located by hard-coded line
number** (`BASIS_BLOCK_LINE = 98`). My script inherits that pattern from
the existing channel-character script for consistency. It is correct at
this evidence base and the pinned digest guards it, but an inserted line
above line 98 would silently change which JSON is parsed. This is
Amendment L's shape; I did not repair it, because a repair would touch a
pre-existing script this task may not modify. **Recorded as located, not
asserted as a defect.**

Also unchanged: `CONVENTIONS.md`'s seventeen rules still have no
structural validator, and the review supply protocol still lives nowhere.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — none.**

The argument survived and the task's questions were answerable from the
frozen material. What remains open is not ambiguity but scope: the
particle–particle half is structurally supported and numerically untested,
and §6 and §10 say so.

**`ENVIRONMENT` — none.** No environment failure occurred, so neither of
Rule 13's two diagnostic orders was exercised. Nothing was installed.

**Things I would have specified differently.**

*§1's Step 1 should give the tensor identity, not the operator one.* The
factor of `4` is right for operators and wrong for the ordered rank-4
tensor an executor actually builds, and the discrepancy looks like a
failed premise under §5's first failure mode. One clause — "as an operator
identity; the ordered-tensor form is the symmetrised
`2[P_R⊗P_L + P_L⊗P_R]`" — removes a false alarm.

*§1's account of the inversion should name the bar-flip.* It attributes
the inversion to `C γ₅^T C⁻¹ = +γ₅` alone. That relation is necessary, but
what it does is *prevent* a flip; the inversion needs the bar-flip on the
other side to exist at all. As written, an executor who computes both
tables and finds identical patterns has reason to think they have made the
error §3 warns about.

*A10's test list is well chosen, and the exclusion is the best part of
it.* Explicitly saying the LL/RR check is **not** a required test — with
the reason — is the clause that stopped a tautology from being locked into
`tests/` where it would have looked like evidence forever. More acceptance
criteria should name what must *not* be tested.
