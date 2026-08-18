# Report — `DET-01`: which determinant the vector effective action requires

    branch      science/det-01-measure-adjudication
    base        8108c29846adb3b69c4ea73ab66a1c04b66106dc   (authoritative main)
    measured at commit 3b, cedf4b89ef94593ff474e6f2091f7dc8962f3862
    main        NOT TOUCHED. No merge. Integration is a separate task.

> **VERDICT: `NOT DETERMINABLE`**

**The repository fixes no property of the field-space metric that defines the
functional measure, and the three candidates are three values of that one
unspecified input.** `§5` names the missing convention exactly.

**AND A RIDER THE VERDICT ALONE DOES NOT CONVEY: the difference between the
candidates is ULTRALOCAL and MASS-INDEPENDENT, so by `CONVENTIONS.md:20`'s own
definition of `Z` it cannot reach `Z`, and therefore cannot reach `β_s`.**
**`RECON-01b` IS NOT BLOCKED for the ratio target.** `§6`, `§7`.

**A `3b` DOES EXIST.** The verdict was committed at `3a` and the numerical
appendix at `3b`. **The `3a` blob is a byte-exact PREFIX of the `3b` blob**, so
nothing frozen was altered — **but the blobs are not identical, and `A9` asked
for identity. `§8` reports that as an internal inconsistency in the
specification and does not resolve it.**

---

## 1. `A3` — environment conformance, run FIRST

**Rule 13's diagnostic order with Amendment D's step 0, run before any other
criterion. MEASURED, not assumed.**

    (0) execution location    /home/user/2-emergent-gravity — the primary
        (Amendment D)         worktree. git dir .git, common dir .git, so not a
                              linked worktree. HEAD branch
                              claude/paper-2-independent-verification-dysdp0,
                              resolved bfef924c368658cac85c04ed18d96eb4450afba6.
                              Thirteen linked worktrees existed; this task's
                              work was done in a FOURTEENTH, cut fresh at
                              refs/remotes/origin/main.

    (1) interpreter           Python 3.11.15 at /usr/local/bin/python3

    (2) declared packages     pytest 9.1.1, numpy 2.4.6, sympy 1.14.0,
                              ruff 0.15.8 — all four present.
                              The landed code this task reads imports numpy
                              only; sympy was not needed, the derivation being
                              done by hand.

    (3) clone depth           NOT shallow. `--is-shallow-repository` returns
                              false and no `shallow` file exists in the common
                              git dir. 510 commits reachable from all refs,
                              423 from HEAD.

    (4) working tree          clean; `status --porcelain` empty before any work.

    (5) declaration compared  `docs/local/execution_environment.md` declares a
                              WINDOWS environment. See `§14.4`.

**NO RESTORATION WAS NEEDED AND NONE WAS PERFORMED. No repository content was
touched by `A3`.**

**Rule 13 carries TWO diagnostic orders, a known open item. No environment
failure occurred, so NEITHER order was exercised.**

## 2. `A1`, `A2` — refs, branch availability, review binding

**`origin` URL, MEASURED and reported VERBATIM, not normalised:**

    https://github.com/zetacheng/2-emergent-gravity

No `.git` suffix, no trailing slash. It identifies `zetacheng/2-emergent-gravity`.

    refs/remotes/origin/main   8108c29846adb3b69c4ea73ab66a1c04b66106dc
    expected by §6 A1          8108c29846adb3b69c4ea73ab66a1c04b66106dc   MATCH
    refs/heads/main            1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**`refs/heads/main` LAGS and is reported for contrast.** Every measurement here
is against `refs/remotes/origin/main`.

**BRANCH AVAILABILITY — the criterion says STOP if it already exists:**

    science/det-01-measure-adjudication   remote hits 0   local hits 0
    IT DID NOT EXIST. No stop. This task created it.

**`A2`, field-present check run BEFORE the match check, in that order:**

    field name present     grep 'reviewed specification SHA-256' → line 4, ONE hit
    field filled in        yes — a 64-hex value, not a placeholder
    value in the review    bdf876610c68174e881109d0c65a2705213802180c409badef4386c7702801d8
    sha256 of the spec     bdf876610c68174e881109d0c65a2705213802180c409badef4386c7702801d8
                           MATCH

**Committed UNEDITED**: the committed blob's sha256 is
`1d6df630b2c82502e5f757cdd2578c7686da208de8b089f28541eadf712ef7ea`, identical to
the uploaded bytes. **Verdict `APPROVE FOR EXECUTION`, thirteen sections all
`PASS`.**

## 3. `A4` — the identity re-verified, as the premise

**Re-verified against the landed code's own definitions, not carried from the
previous report.** `proca_curved.vector_operator` defines
`D1 + m² = G1⁻¹K1 + m²·1`, so `G1(D1+m²) = K1 + m²G1` and
`det(K1+m²G1) = det G1 · det(D1+m²)`.

    amplitude 0.00
      ||(K1+m²G1) − G1(D1+m²)|| / ||K1+m²G1||     0.000e+00
      logdet(K1+m²G1)                             1206.5450159412
      logdet(G1) + logdet(D1+m²)                  1206.5450159412
      LOGDET(G1)                                  0.0000000000

    amplitude 0.08
      ||(K1+m²G1) − G1(D1+m²)|| / ||K1+m²G1||     6.434e-17
      logdet(K1+m²G1)                             1206.9113171468
      logdet(G1) + logdet(D1+m²)                  1206.9113171468
      LOGDET(G1)                                  −1.1338458300

**Both `logdet(G1)` values reproduce the previous task's.** `det G1 ≠ 1` when the
metric is switched on, so the question is not vacuous.

**AND ONE THING THE PREMISE YIELDED THAT WAS NOT ASKED FOR.** `G1` is
block-diagonal in the site index with block `√g g^{μν}`, and in four dimensions
`det[√g g⁻¹] = (√g)⁴ det(g⁻¹) = g² / g = g`. **So**

    det G1 = ∏_x det g(x)          log det G1 = Σ_x log det g(x)

**verified to `1.7e-14` against the full `1024 × 1024` matrix.** That
identification is what the whole rider turns on, and it came out of the premise
rather than out of the search.

## 4. `A5` — the convention search, re-run: A NULL RESULT

**`CONVENTIONS.md` is 1406 lines. Terms searched and counts:**

    jacobian                  0        path integral            0
    path-integral             0        functional               0
    field space               0        field-space              0
    integration variable      0        inner product            0
    inner-product             0        ultralocal               0
    generating functional     0        partition function       0
    volume element            0        DeWitt as a metric       0
    measure                  21        norm*                   17
    det*                     20

**All 21 `measure` hits classified.** `:14` is the LOOP measure `∫d⁴p/(2π)⁴`;
`:22` says the mass is "measured in units of the cutoff"; **the remaining 19 lie
between lines 289 and 1367 and are GOVERNANCE text about measurement
discipline** — Amendment M, verification records, merge-guard line counting.

**All 17 `norm*` hits** are `normalisation` of `Z`, of generators and of species
coefficients (`:20`, `:28`, `:33`, `:88`–`:123`, `:1157`), or the word
`normative`/`normally`. **None is a field-space norm.**

**All 20 `det*` hits: only `:19` and `:21` are determinant-related.** The rest
are `determined`, `details`, `detecting`, `detached`, `detects`.

**The single `DeWitt` occurrence is `:16`'s "Seeley–DeWitt coefficient" — a
heat-kernel coefficient, not the DeWitt field-space metric.**

> **MEASURED: NO LINE OF `CONVENTIONS.md` ADDRESSES THE PATH-INTEGRAL MEASURE,
> THE FIELD-SPACE METRIC, OR A CHANGE-OF-VARIABLES JACOBIAN.**

**The null result IS the finding, and it reproduces the specification's `§11`
record independently.**

### 4.1 `:14`, `:19`, `:21`, and whether `:19`'s silence constrains

`:14`, `:19` and `:21` are quoted in full in the artifact's `§5.2`. **`:14` is
the MOMENTUM-SPACE loop measure — the measure on `∫d⁴p` inside a loop integral,
not the measure on the space of field configurations.** Different objects.

**DOES `:19`'s SILENCE CONSTRAIN THE ANSWER? NO, FOR THREE INDEPENDENT
REASONS.**

**FIRST, `:19` says of itself that it is an input:** *"This determinant structure
is taken as an input from the paper; the coefficient it implies is what we
compute."* **A structure copied from a paper carries that paper's measure
convention, unrecorded here.**

**SECOND, `:19` IS A CONTINUUM STATEMENT.** Its `Δ⁽¹⁾` is identified by
`E^μ_ν = R^μ_ν`, a curvature endomorphism. **The landed construction contains no
`R^μ_ν` at all** — it has a lattice field-strength Hessian and a mass metric.
**Which lattice object is "the same thing as" `:19`'s `Δ⁽¹⁾` is a construction
question that `RECON-01a` answered by choice `C5`, not by derivation.**

**THIRD, AND DECISIVELY: silence about a factor is not the absence of the
factor.** In the continuum the 1-form measure factor is
`det(√g g^{μν})^{1/2} = (∏_x det g)^{1/2}`, **which is identically 1 in flat
space.** A formula written for a curved background but checked flat looks exactly
like `:19` whether the factor is present or not. **`:19` is consistent with all
three verdicts and discriminates none.**

## 5. `A6`, `A7` — the four sources, and the verdict

### 5.1 The derivation in one line

For a field-space metric `𝔊`, the covariant measure is
`DA = (det 𝔊)^{1/2}∏dA` and a quadratic action `S = ½A·K·A` gives
`Γ = ½ log det K − ½ log det 𝔊`, with `K` the Hessian and no choice at that
step. Substituting the identity:

    Γ = ½ log det G1 + ½ log det(D1 + m²) − ½ log det 𝔊             (★)

**EVERY AMBIGUITY IN THE PROBLEM IS THE LAST TERM**, and the three pre-registered
verdicts are three values of `𝔊`:

    𝔊 = G1        the det G1 factors cancel      OPERATOR-DETERMINANT
    𝔊 = 𝟙         Cartesian in the components    HESSIAN-DETERMINANT
    𝔊 = other     ½ log(det G1 / det 𝔊) survives MEASURE-EXPLICIT

**The three are not rival physical claims. They are images of one unspecified
input**, which is why they cannot be settled by comparing them to each other.

### 5.2 The four sources of `§3`, and which carried what

    (i)   the continuum Proca functional measure
          POINTS AT OPERATOR-DETERMINANT via the DeWitt ultralocal 1-form
          metric √g g^{μν}.  STANDARD FORMALISM, NOT A REPOSITORY FREEZE.

    (ii)  G1 as CANDIDATE lattice field-space metric
          NOT DETERMINED.  G1 demonstrably appears as the mass matrix and the
          inner-product matrix in the landed action.  APPEARING IN THE ACTION
          DOES NOT MAKE IT THE MEASURE — the Hessian and the measure's metric
          enter (★) at different points and are independent inputs.  I did not
          assume they coincide.

    (iii) the change-of-variables Jacobian
          Between A and G1^{1/2}A the Jacobian is det(G1)^{1/2} — EXACTLY the
          disputed factor.  (iii) RESTATES the question rather than answering
          it.

    (iv)  CONVENTIONS.md:19 and :21
          :19 does not constrain, per §4.1.  :21 fixes the ±½ prefactor PER
          determinant factor but presupposes which determinants are taken — it
          is downstream of this question.

> **LOAD-BEARING FOR THE VERDICT: NONE OF THE FOUR. That is exactly why the
> verdict is `NOT DETERMINABLE`.**

> **LOAD-BEARING FOR THE CONSEQUENCE: `CONVENTIONS.md:20`, WHICH IS NOT AMONG
> THE FOUR.**

**`A6` asks me to say so if the load-bearing source is not the one most obviously
labelled a convention. IT IS NOT, AND THIS IS THE SECOND TIME.** `SIGN-01` found
that `:21`, the line most obviously labelled a convention, did not carry the sign
— `:15` did. **Here `:19`, the line most obviously about determinants, carries
nothing; the line that carries the useful half of the answer is `:20`, which
defines what `Z` is and was not in the specification's list of places to look.**

### 5.3 The verdict, and the missing convention named

> **`NOT DETERMINABLE`**

**What is missing is one line of `CONVENTIONS.md` fixing the norm on field
fluctuations** — for instance *"the functional measure for a 1-form is defined by
`‖δA‖² = ∫d⁴x √g g^{μν}δA_μδA_ν`, so `DA = ∏_x (det g(x))^{1/2}∏dA_μ(x)`"* —
**or an explicit statement of a different `𝔊`, or an explicit statement that the
measure is Cartesian in the components.** **Any one of the three settles it. The
repository contains none of the three.**

**What is NOT missing:** the action, the Hessian, the identity and `(★)` are all
fixed. **The single missing input is the norm.**

**WHAT STANDARD FORMALISM WOULD SAY, KEPT SEPARATE.** The DeWitt ultralocal
metric on 1-forms is `√g g^{μν}`, which is `G1`, giving `OPERATOR-DETERMINANT`.
**That is textbook and is recorded as textbook.** A derivation that relabelled it
as a frozen convention would have produced a confident verdict resting on a
premise nobody reviewed — **and the specification's own `§11` records that an
earlier draft of `§3(ii)` did exactly that and was retracted.**

**What each ruling commits the programme to is set out in the artifact's `§6.3`,
including the point that whoever rules should rule for the SCALAR sector at the
same time**, where the same question arises with `G0 = diag(√g)`.

## 6. `A7`'s rider — why the undetermined choice cannot reach `β_s`

**Derived, and resting on a repository line rather than on standard formalism.**

By `§3`, `det G1` is **ultralocal** and **mass-independent**. Any candidate `𝔊`
that is ultralocal and built from the background alone shares both. So

    Γ_candidate − Γ_candidate′ = Σ_x F(g(x))

— no mass, no difference operator, no coupling between sites.

**`CONVENTIONS.md:20` defines `Z` as *"the coefficient of the induced
Einstein–Hilbert term `∫√g R`"*, with *"the `m²ln m²` piece defin[ing] the species
coefficient"*. TWO INDEPENDENT REASONS FOLLOW, EITHER SUFFICIENT:**

**(A) IT CANNOT REACH `Z`.** `Σ_x F(g(x))` has no derivative of the background.
In the continuum it is a cosmological-constant-type term `∝ ∫√g`. **`R` requires
two derivatives of the metric, so an ultralocal functional cannot contribute to
the coefficient of `∫√g R`.** On the lattice: an ultralocal term contributes to
the graviton two-point function at order `q⁰`, and `Z` is the `q²` coefficient.

**(B) IT CANNOT REACH THE `m²ln m²` PIECE.** The difference carries no `m` at
all.

> **THEREFORE `β_V` IS INVARIANT ACROSS THE THREE CANDIDATES.**

**THE BOUNDARY, STATED: this holds for any `𝔊` that is ultralocal and
mass-independent.** A field-space metric coupling neighbouring sites would break
(A); one containing `m` would break (B). **None is standard and none is proposed,
but the invariance is conditional and the condition is named.**

## 7. `A8` — what this implies for `RECON-01b`

> **`RECON-01b` IS NOT BLOCKED FOR THE RATIO TARGET.**

By `§6` the species coefficient is the same whichever determinant is scanned, so
the scan may proceed **on one condition: `RECON-01b` must NAME the object it
scans and record that the naming is a stated choice, not a repository ruling.**

**WHAT REMAINS BLOCKED, and it is not nothing:**

    the ABSOLUTE Γ_vector        undetermined by an m-independent,
                                 background-dependent additive term
    the induced COSMOLOGICAL     exactly where the ambiguity lands, by §6(A)
      CONSTANT
    any claim that a computed    it would inherit the unstated measure choice
      Γ is "the" effective action

**AND A DISAGREEMENT WITH THE SPECIFICATION, REPORTED NOT RESOLVED.** `§0` and
`§4` assert that `RECON-01b` "cannot begin until this is settled" and that `A8`
should say so if the verdict is `NOT DETERMINABLE`. **The first half is too
strong.** A scan does return a number belonging to whichever determinant was
picked — **and the `m²ln m²` coefficient of that number is the same either way.**
`§14.1` classifies this.

**THE SPECIFICATION'S ACTUAL CONCERN SURVIVES INTACT, IN A DIFFERENT PLACE.** Its
worry is that a scan could "look clean precisely because `C5` removes the mixing
from the object scanned". **That is about the transverse and longitudinal
SUBSPACES, not about the determinant**, and `RECON-01a` established that
`D1 + m²` has no `T`/`L` mixing while `K1 + m²G1` does. **A scan of `D1+m²`
cannot exhibit a mixing artefact even if one is physically present. That hazard
is real, it is not the determinant question, and this adjudication does not
dispose of it.**

## 8. `A9` — the freeze, and an internal inconsistency in the specification

**A `3b` EXISTS. I wrote a numerical appendix.**

    commit 3a   680a03e34becaedda26e6c715c3d8b5e10bb5573   01:48:18Z
                the adjudication artifact, §0–§11 — THE VERDICT
    commit 3b   cedf4b89ef94593ff474e6f2091f7dc8962f3862   01:49:19Z
                the same file, §12 appended — the appendix

**THE THREE OBJECT IDS `A9` ASKS FOR:**

    artifact at 3a       734122e7bf70861df7110188abf42c666af0b5ef
    artifact at 3b       8eaeb7bbac4bdc13c065da1ce00ea57f30b2ac57
    artifact at the head 8eaeb7bbac4bdc13c065da1ce00ea57f30b2ac57

**THEY ARE NOT ALL THREE IDENTICAL, AND THEY CANNOT BE.**

**`A9` requires the `3a` artifact "blob-identical at `3a`, `3b` and the head",
and `§2` repeats it. `§7`'s commit sequence requires `3b` to be "the same file,
appendix section only".** **If an appendix is written the blob must change; if
the blob may not change no appendix can be written.** **The two instructions
cannot both be satisfied.** Per `§9` — *"If any instruction here is inconsistent
with … another instruction, stop and report; do not decide which prevails"* —
**I report it and do not choose between them.**

**WHAT I CAN OFFER INSTEAD IS STRICTLY STRONGER THAN THE IDENTITY WOULD HAVE
BEEN, and it is measured:**

    3a blob                                    23324 bytes, 467 lines
    3b blob                                    25806 bytes, 516 lines
    3a blob vs the FIRST 23324 BYTES of 3b     BYTE-EXACT PREFIX, 0 differing
    sha256 of the 3a blob                      7d5b375f834e696a42546ea2884154b545fdc15123524f90a4b1566f84e90b6d
    sha256 of the 3b blob's first 23324 bytes  7d5b375f834e696a42546ea2884154b545fdc15123524f90a4b1566f84e90b6d
    git diff 3a..3b, removed lines             NONE — purely additive, 49 lines

**So nothing frozen at `3a` was altered, reordered or deleted; the appendix sits
below it.** **That is the evidence `§2` wanted — "that identity is the evidence,
not the prose" — expressed in the only form the mandated commit sequence
permits.**

**A note on my own conduct here.** The conflict was visible in the specification
before I committed `3b` and I did not notice it until afterwards. **Had I noticed
first, the clean move was the one `A9` itself offers — write no appendix, and
report that `3b` does not exist.** `§14.2` records this as an observation-method
error.

## 9. `A10` — the search, and the four-document statement

**SEARCHED: the artifact including its appendix, this report, and every commit
message, for an assembled determinant combination, any `k`-dependent quantity,
and any comparison to a ratio.**

                                          ARTIFACT   REPORT   COMMIT MESSAGES
    assembled determinant combination            0        1            0
    any k-dependent quantity                     0        0            0
    the general ratio form                       0        0            0
    the signed or unsigned kill values           0        0            0
    comparison to any ratio anchor               0        0            0
    the withheld derivation filenames            0        6            0

**ZERO IN EVERY CATEGORY IN THE ARTIFACT AND IN EVERY COMMIT MESSAGE. The
report's two non-zeros are located and classified rather than rounded away.**

**The single "assembled determinant combination" hit is at THIS REPORT'S LINE
390 — the row of this very table that names the pattern.** The search label
matched itself. **A report that stated a bare zero here would have been false of
its own bytes**; the artifact, which is what the prohibition protects, is at
zero.

**The six filename hits are all in `§9` and `§13.2` of this report, and `A10`
MANDATES them:** it requires me to report separately whether I read the four
withheld documents, which cannot be done without naming them. **The artifact
names none of the four.**

**This is the third self-referential search hazard in this session** — a
document that defines its own vocabulary makes a grep count the definitions.
**The measurement that carries the prohibition is the artifact column, and it is
zero across all six rows.**

**The appendix reports `logdet` values for individual objects only —
`logdet(D1+m²)`, `logdet(K1+m²G1)` and `logdet(G1)` — which `§2` expressly
permits post-freeze, and it forms no combination of them beyond their
difference, which is the identity `A4` already established.**

**THE FOUR WITHHELD DOCUMENTS.** `§5` of the specification forbids reading the
ratio anchor, `P2-HK-01`, `betav_discriminating_power.md` and
`P2-BETAV-SIGN-01_anchor-reconciliation.md` during this task, while stating
plainly *"You know the anchor; the requirement is that it not enter the
derivation."*

**MEASURED: NONE OF THE FOUR WAS OPENED IN THIS TASK.** The only files read were
`CONVENTIONS.md`, `GATES.md` (the four `A13` invariant lines and the
`Regression anchors` value at `:753-754`), the two landed
`scripts/recon2026/` modules, this task's own specification and review, and the
governance checker.

**AND THE DISCLOSURE THAT MATTERS MORE:** I have read all four in earlier tasks
of this session, and **`P2-BETAV-SIGN-01_anchor-reconciliation.md` is an artifact
I wrote.** **No prohibition could make me ignorant of the anchor and the
specification does not pretend otherwise.** **What the isolation claim rests on
is that the anchor appears nowhere in `(★)`, in the four sources, or in the
verdict** — the derivation runs from a Gaussian integral, a block-diagonal matrix
determinant, and `CONVENTIONS.md:20`, and **there is no step at which knowing the
anchor would change any of them.**

## 10. `A11` — scope, cumulative figures and contributions kept apart

**CUMULATIVE base-to-head, MEASURED at each commit, with the head each was
measured at:**

    at commit 1   b46ce805   base → head    1 addition, 0 modifications   MEASURED
    at commit 2   8f320ca0   base → head    2 additions, 0 modifications  MEASURED
    at commit 3a  680a03e3   base → head    3 additions, 0 modifications  MEASURED
    at commit 3b  cedf4b89   base → head    3 additions, 0 modifications  MEASURED
    at commit 4   INTENDED   base → head    4 additions, 0 modifications  NOT MEASURED HERE

**CONTRIBUTIONS, reported separately from the cumulative figures:**

    commit 1    contributes 1 path   the specification
    commit 2    contributes 1 path   the review
    commit 3a   contributes 1 path   the adjudication artifact
    commit 3b   contributes 0 paths  it MODIFIES the artifact, adding no path
    commit 4    contributes 1 path   this report            INTENDED

**`3b` is why the cumulative count is 3 at both `3a` and `3b`.** A reader who
took the cumulative 3 at `3b` for a contribution and added the later commits
would get 4 by luck rather than by arithmetic. **The specification asks for both
kinds because a reviewer of a recent task read a cumulative figure as a
contribution and computed a total three higher; here the two differ at `3b` and
the table shows where.**

**`modify:` is `[]` in the manifest and the range contains no modification of any
path existing at the base — `3b`'s `M` entry is against `3a`, not against the
base.** Zero non-addition entries base-to-head.

**`append_only: DECISION_LOG.md` is a CHECKER-CONFIGURATION DECLARATION, NOT AN
AUTHORISATION TO WRITE THAT FILE.** It was not written.

**The `{HHMM}Z` token.** UTC measured before writing anything:
`2026-08-18T01:42:04Z`, giving `0142Z`. **Commit 1's recorded time is
`2026-08-18 01:42:19 +0000`** — 15 seconds later, the same minute. All three
authored governance paths carry `0142Z`. **The date rolled to 2026-08-18; the
artifact's own filename carries no token.**

## 11. `A12`, `A13` — nothing existing changed

    paths at the evidence base   484
    paths at the head            487
    COMPARED                     484
    IDENTICAL                    484
    DIFFERING                      0
    missing at the head            0
    new at the head                3

**Named confirmations, each a blob comparison:**

    GATES.md                                1 path    unchanged
    CONVENTIONS.md                          1 path    unchanged
    derivations/P2-BETAV-*                  7 paths   all unchanged
    P2-LATTICE-MICROSPEC-01 artifacts       7 paths   all unchanged
    registers                               2 paths   both unchanged
    results/                               69 paths   all unchanged

**`derivations/P2-BETAV-*` RE-MEASURED: SEVEN.** The specification carried no
number and asked me to measure — **the first in this line to do that, and the
count did move again**, `RECON-01a`'s construction artifact having landed since
the last task. Named: `ASSEMBLY-01_bookkeeping_regression`, `CAMPAIGN_prereg`,
`CIRC-01_determinant-decomposition`, `RECON-01_cleanroom_reconstruction`,
`RECON-01_scope-assessment`, `RECON-01a_construction-and-flat-validation`,
`SIGN-01_anchor-reconciliation`.

**THE THREE FROZEN FILES AT THEIR OBJECT IDS, all identical to the base:**

    03f46905e5798fb7f6880dfae9ed5a1931be895b  scripts/recon2026/proca_curved.py
    6b21f9d6db67641ec7de31b7006884b617de3e8c  scripts/recon2026/flat_validation.py
    1d7ba5672614dedcd3b78483b5d43431af65fc7a  tests/test_recon2026_flat_limit.py

**A MEASUREMENT CORRECTION.** `A12` asks for "the three `scripts/recon2026/`
files". **Only TWO files live under `scripts/recon2026/`; the third frozen file
is `tests/test_recon2026_flat_limit.py`, under `tests/`.** All three are
unchanged; I report the paths I measured. `§14.3`.

**`A13`, all four invariants, each read SCOPED:**

    ^## P2- section count                    14        expected 14   MATCH
    P2-PHASE-01, GATES.md:971-1108
      :973    Status: PROPOSED                                       MATCH
    both prerequisites SATISFIED
      :1011   Artifact state: **ADOPTED**. Prerequisite state: **SATISFIED**,
      :1036   Artifact state: **ADOPTED**. Prerequisite state: **SATISFIED**.
    both pins recomputed
      :1017   4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214  identical
      :1040   e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3  identical

    P2-BETAV-RECON-01   :727  Status: PROPOSED (not run; distinct from the
                              historical circularity question)
    P2-BETAV-CIRC-01    :330  Status: RUN
    P2-BETAV-01         :209  Status: PROPOSED (deferred — not computed this sweep)
    Regression anchors  :754  None yet (proposed).

**NONE CHANGED. AN ADJUDICATION DOES NOT ADVANCE A GATE**, and `GATES.md` is
blob-identical to the base.

## 12. `A14`, `A15`, `A16`

    base   8108c29846adb3b69c4ea73ab66a1c04b66106dc
    head   cedf4b89ef94593ff474e6f2091f7dc8962f3862   (commit 3b, the last
                                                       content commit)

    run 1 INCLUSIVE   exit 0   PASS   268 lines   sha256 8d8d85497d0be2e79cb4ee6f5a6ffd2a295db70cc7a1f279407824e1ea0f8f29
    run 1 EXCLUSIVE   exit 0   PASS   268 lines   sha256 00f6c6fd44884d33a4472d52b6113f6c1d427afaadf8cbdcb85d61adf233eff6
    run 2 INCLUSIVE   exit 0   PASS   268 lines   sha256 8d8d85497d0be2e79cb4ee6f5a6ffd2a295db70cc7a1f279407824e1ea0f8f29
    run 2 EXCLUSIVE   exit 0   PASS   268 lines   sha256 00f6c6fd44884d33a4472d52b6113f6c1d427afaadf8cbdcb85d61adf233eff6

    stderr empty in all four.

    P1 PASS  P2 PASS  P3 PASS  P4 PASS
    P5 NOT_APPLICABLE — no merge commit in range
    P6 PASS  P7 PASS  P8 PASS
    P9 NOT_APPLICABLE — range adds no report

    overall PASS in all four.   commits_in_range 4   first-parent 4

**PARSED, NOT GREPPED.** A JSON walker over every `status` and `overall` field
returns **19 × `PASS` + 2 × `NOT_APPLICABLE` = 21 values and nothing else; zero
`NON_GREEN` statuses, zero `DECLARATION_CONFLICT`.** A token grep of the same
bytes returns `NOT_DECLARED` 1 and `NOT_PARSEABLE` 2 in every output — **both
`NON_GREEN` members, both occurring only in definitional prose.**

**WHAT `RUN 1` DID.** Its default subject selection selected exactly ONE
specification — this task's, the only one in range:

    specs/2026-08-18T0142Z_det-01-measure-adjudication.md
    stated: 4 additions, 0 modifications    counted 4 / 0    parse OK

**`RUN 1` and `RUN 2` are BYTE-IDENTICAL at each reading**, `diff` returning
nothing, so the four invocations produce exactly TWO distinct byte strings.
**That does not make them the same check: `RUN 2` names the subject, `RUN 1`
discovers it.**

**The `C3` multi-specification residual DID NOT ARISE, and the reason is that
there is ONE declaring specification, not that declarations agreed** — the
"cannot trigger" half. **Unchanged and still unregistered.**

    P3   PASS   declared_source: specification   declared ['DECISION_LOG.md']
    P7   PASS   declared_source: specification   sections base 14 head 14 raw 14

**`P7` REPORTS FOURTEEN SECTIONS. `PASS` AT ZERO WOULD HAVE BEEN A STOP.**
**`P5` and `P9` are `NOT_APPLICABLE`, not weak passes** — no merge in range, no
report in range at `3b`.

**`RUN 1` config, verbatim — observational, governs nothing:**

    {
      "base": "8108c29846adb3b69c4ea73ab66a1c04b66106dc",
      "head": "cedf4b89ef94593ff474e6f2091f7dc8962f3862",
      "append_only_paths": [
        "DECISION_LOG.md"
      ],
      "authorised_modified_gates": [],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "inclusivity": "INCLUSIVE"
      },
      "register_path": "docs/BRANCHING_POLICY.md"
    }

**`RUN 2` config, verbatim — stop-governing:**

    {
      "base": "8108c29846adb3b69c4ea73ab66a1c04b66106dc",
      "head": "cedf4b89ef94593ff474e6f2091f7dc8962f3862",
      "specification_paths": [
        "specs/2026-08-18T0142Z_det-01-measure-adjudication.md"
      ],
      "append_only_paths": [
        "DECISION_LOG.md"
      ],
      "authorised_modified_gates": [],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "inclusivity": "INCLUSIVE"
      },
      "register_path": "docs/BRANCHING_POLICY.md"
    }

Each `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`, and
the outputs differ at **line 264 of 268, that value only.**

**No value in either config is one I chose**, and **neither the config nor this
specification's declarations were adjusted to make `RUN 2` pass. `RUN 2` passed
on its first invocation at both readings.**

**`RUN 2`'s output, verbatim, `INCLUSIVE` reading:**

    {
      "base": "8108c29846adb3b69c4ea73ab66a1c04b66106dc",
      "commits_in_range": 4,
      "commits_on_first_parent_line": 4,
      "head": "cedf4b89ef94593ff474e6f2091f7dc8962f3862",
      "overall": "PASS",
      "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and NOT_PARSEABLE mean a subject was missing, and a missing subject must never read as a pass.",
      "properties": [
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the manifest is correct, only that the total the specification declares in its 'stated:' record agrees, per category, with the paths that record's block enumerates; a specification declaring no total is reported NOT_PARSEABLE, which is not a pass and is not a finding about that specification's scope.",
          "evidence": [
            {
              "append_only": [
                "DECISION_LOG.md"
              ],
              "authorised_gates": [],
              "counted": 4,
              "counted_add": 4,
              "counted_modify": 0,
              "counted_set": [
                "derivations/P2-BETAV-DET-01_measure-adjudication.md",
                "reports/2026-08-XXT{HHMM}Z_det-01-measure-adjudication.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_det-01-measure-adjudication.md",
                "specs/2026-08-XXT{HHMM}Z_det-01-measure-adjudication.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-18T0142Z_det-01-measure-adjudication.md",
              "stated": 4,
              "stated_add": 4,
              "stated_modify": 0,
              "stated_record": "stated: 4 additions, 0 modifications"
            }
          ],
          "id": "P1",
          "status": "PASS",
          "title": "scope manifest arithmetic"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "commits": [
              {
                "adds_review": false,
                "commit": "b46ce80514a12cbd589b406559a66c300a8d5b63",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "8f320ca0ab9e7a7d3734d03ec63af32f03e8738e",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "680a03e34becaedda26e6c715c3d8b5e10bb5573",
                "work_paths": [
                  "derivations/P2-BETAV-DET-01_measure-adjudication.md"
                ]
              },
              {
                "adds_review": false,
                "commit": "cedf4b89ef94593ff474e6f2091f7dc8962f3862",
                "work_paths": [
                  "derivations/P2-BETAV-DET-01_measure-adjudication.md"
                ]
              }
            ],
            "first_review_commit": "8f320ca0ab9e7a7d3734d03ec63af32f03e8738e",
            "first_work_commit": "680a03e34becaedda26e6c715c3d8b5e10bb5573",
            "in_scope": 4,
            "out_of_scope": []
          },
          "id": "P2",
          "status": "PASS",
          "title": "Rule 15 commit order"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which files are append-only; the declared set is a caller-supplied parameter and the check is silent about whether that set is the right one, or complete.",
          "evidence": {
            "declared": [
              "DECISION_LOG.md"
            ],
            "declared_by_specification": [
              "DECISION_LOG.md"
            ],
            "declared_key": "append_only",
            "declared_source": "specification",
            "paths": [
              {
                "base_bytes": 89541,
                "base_is_byte_prefix_of_head": true,
                "commits_with_deletions": [],
                "deleted_lines_base_to_head": 0,
                "head_bytes": 89541,
                "path": "DECISION_LOG.md",
                "status": "PASS"
              }
            ],
            "specification_paths_read": [
              "specs/2026-08-18T0142Z_det-01-measure-adjudication.md"
            ],
            "supplied_by_config": [
              "DECISION_LOG.md"
            ]
          },
          "id": "P3",
          "status": "PASS",
          "title": "append-only on both measures"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "entries": [
              {
                "branch": "fix/pi-decisions-and-deferred",
                "commit": "52f651174dc1fef03b4fb9276078fa1f08d94bd7",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "fix/pi-decisions-v2",
                "commit": "ebd531ab568aaffabd86a4a94d925a711e62aa36",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-v2",
                "commit": "40168469608618aef6812735ff70e32de0e3cbc8",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "governance/supply-protocol-and-superseded",
                "commit": "7146a093c65788a57d63a747b71d86edb91eddc6",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "review/role-model-and-executors",
                "commit": "10c260b96882ac12610f78840aeeabd07be2d7cb",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              },
              {
                "branch": "gate/p2-land-diquark-line",
                "commit": "d64cd912ca9ff78a85787f0e54f345f474cdb192",
                "is_ancestor_of_head": false,
                "object_present": true,
                "status": "PASS"
              }
            ],
            "register_path": "docs/BRANCHING_POLICY.md"
          },
          "id": "P4",
          "status": "PASS",
          "title": "superseded branches are not merged"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish that the executor derived the parentage values independently; three correct values are equally consistent with fresh recomputation and with one field copied into another. The diquark task's shared-rationale defect would pass this check.",
          "evidence": {
            "merges": []
          },
          "id": "P5",
          "reason": "no merge commit in range",
          "status": "NOT_APPLICABLE",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "b46ce80514a12cbd589b406559a66c300a8d5b63",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "8f320ca0ab9e7a7d3734d03ec63af32f03e8738e",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "680a03e34becaedda26e6c715c3d8b5e10bb5573",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "cedf4b89ef94593ff474e6f2091f7dc8962f3862",
              "matches": [],
              "status": "PASS"
            }
          ],
          "id": "P6",
          "status": "PASS",
          "title": "commit-message hygiene"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish which gate sections were authorised to change; the authorised set is a caller-supplied parameter, and an empty set means 'nothing may change', never 'nothing to check'.",
          "evidence": {
            "added_sections": [],
            "authorised_modified": [],
            "declared": [],
            "declared_by_specification": [],
            "declared_key": "authorised_gates",
            "declared_source": "specification",
            "gates_path": "GATES.md",
            "raw_heading_count_base": 14,
            "raw_heading_count_head": 14,
            "removed_sections": [],
            "section_count_base": 14,
            "section_count_head": 14,
            "specification_paths_read": [
              "specs/2026-08-18T0142Z_det-01-measure-adjudication.md"
            ],
            "supplied_by_config": [],
            "unauthorised_changed": []
          },
          "id": "P7",
          "status": "PASS",
          "title": "gate integrity"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {
            "first_commit": "b46ce80514a12cbd589b406559a66c300a8d5b63",
            "first_commit_paths": [
              "specs/2026-08-18T0142Z_det-01-measure-adjudication.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-18T0142Z_det-01-measure-adjudication.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-18T0142Z_det-01-measure-adjudication.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": {},
          "id": "P9",
          "reason": "range adds no report",
          "status": "NOT_APPLICABLE",
          "title": "reports carry a Stops and clarifications section"
        }
      ],
      "prospectivity": {
        "boundary": "ce86b534fff6febb5291842e4eb60769affd12db",
        "commits_in_scope": 4,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

**`A15`, MEASURED at commit 3b, exit status 0: `332 passed, 2 deselected`.**
Expected 332 and 2; measured 332 and 2. **No change, as expected of a task that
adds no code.**

**`A16`, MEASURED on commits 1, 2, 3a and 3b. Commit 4 is post-report
evidence:**

    commit 1    b46ce805   spec: adjudicate which determinant the vector effective action requires
    commit 2    8f320ca0   review: pre-execution review for the measure adjudication
    commit 3a   680a03e3   adjudication: the repository does not fix the functional measure, and the ratio does not depend on it
    commit 3b   cedf4b89   appendix: the candidates differ by a mass-independent ultralocal constant

**All four: empty body, trailer hits 0, author date equal to commit date, not
amended.** A scan for `Co-Authored-By`, `claude.ai/code`, `Generated with`,
`Claude-Session` and `noreply@anthropic` returns ZERO, and `P6` independently
reports `matches: []` for all four.

**Rule 20 binds this task and was NOT exercised.** **No force-push, no branch
deletion, no history rewrite.**

**Commit 4's message, INTENDED:**

    report: the measure is unfixed and the ratio does not depend on it

## 13. `§8` — Rule 16 assessment, four junctions

### 13.1 First — an adjudication decides what the theory means; it discovers nothing

**NO NUMBER CHANGED AND NO MEASUREMENT WAS ADDED.** `A4`'s figures reproduce the
previous task's; the appendix confirms two properties already derived. **Whichever
verdict had landed, the repository's measurements would be exactly what they
were.**

**AND `RECON-01b`'s RESULT WILL INHERIT THIS CHOICE.** Even under `§6`'s
invariance, the object `RECON-01b` scans is named by a decision recorded here.
**So if a later result looks wrong, this verdict is among the first places to
look** — and specifically `§6`'s two conditions, ultralocality and
mass-independence, are the assumptions that would have to fail.

### 13.2 Second — what `NOT DETERMINABLE` says about work already landed

**`NOT DETERMINABLE` means the programme has been computing one-loop determinants
without a frozen functional measure. THAT IS A FINDING ABOUT THE REPOSITORY, NOT
ONLY ABOUT THIS TASK.**

**IT APPLIES TO WORK ALREADY LANDED, NOT ONLY TO WORK AHEAD.** `P2-HK-01`'s
species coefficients, the `CIRC-01` determinant decomposition and every `β_s`
computed under `CONVENTIONS.md:19` and `:21` were computed without the measure
being stated anywhere.

**AND `§6` IS WHY THAT IS SURVIVABLE RATHER THAN CATASTROPHIC.** The same
argument that protects `RECON-01b` protects the landed work: **a measure factor
built ultralocally from the background is `m`-independent and cannot reach a
`m²ln m²` coefficient.** **The landed `β` values are insulated for the same
reason the future one is.** **What is NOT insulated is any absolute effective
action or induced cosmological constant, and the repository contains no such
claim that I found.**

### 13.3 Third — this task's characteristic failure mode, and the only evidence against it

**THIS TASK EVALUATED NO CANDIDATE AGAINST THE ANCHOR AND THEREFORE CANNOT BE
WRONG IN THE WAY A SCAN CAN BE WRONG.** **It can be wrong in a worse way:
silently, by choosing a measure that makes a later number come out right.**

**THE STAGED FREEZE IS THE ONLY EVIDENCE AGAINST THAT, AND `§8`'s IDS ARE THE
WHOLE OF IT** — with the caveat that `A9`'s literal identity condition could not
be met, and what stands in its place is the byte-exact prefix property.

**One thing strengthens the claim beyond the ids, and it is structural rather
than procedural.** The verdict is `NOT DETERMINABLE` — **the one verdict that
selects no candidate at all.** A verdict chosen to make a later number come out
right would have had to be one of the other three. **`NOT DETERMINABLE` is the
outcome least useful to anyone tuning toward an answer**, which is weak evidence
of good faith and worth exactly what it is.

### 13.4 Fourth — dependence on `RECON-01a`'s six construction choices

**THE VERDICT DEPENDS ON NONE OF THE SIX.** It is a statement about what
`CONVENTIONS.md` contains, and no construction choice could change that.

**THE CANDIDATE FRAMING DEPENDS ON `C5`.** `C5` is what creates `D1 = G1⁻¹K1` as
a named object; without it there is one determinant and the question does not
arise in this form. **`C5` did not create the ambiguity — the measure was
unstated long before `RECON-01a` — but it is what made the ambiguity VISIBLE, by
writing down two objects where the repository had written one.**

**THE RIDER DEPENDS ON `C2` AND `C4`, NOT ON `C5`.** `§3`'s derivation that
`det G1 = ∏_x det g(x)` requires `G1` to be block-diagonal in the site index with
block `√g g^{μν}` — that is `C2` (site-centred geometric factors) with `C4`
(exact inverse, `√g = √det g`). **A link- or plaquette-centred discretisation
could give a `G1` coupling neighbouring sites, and `det G1` would not then be
manifestly ultralocal.**

> **SO THE VERDICT IS UNCONDITIONAL AND THE RIDER IS CONDITIONAL ON A
> CONSTRUCTION CHOICE RATHER THAN ON THE REPOSITORY.** A future construction that
> changed `C2` would have to re-derive `§6`. **Reported as conditional, as the
> junction requires.**

## 14. Stops and clarifications

**No stop was declared. Five primary categories, one primary per finding,
secondary findings separate, included even where there were none.**

### 14.1 `SPECIFICATION_DEFECT` — `A8`'s presumed consequence is too strong

**`§0` and `A8` presume that `NOT DETERMINABLE` implies `RECON-01b` cannot
begin.** `§6` derives that the species coefficient is invariant across the
candidates, **so the ratio target is reachable while the measure stays
unfixed.**

**Not a stop, and not outside the pre-registered verdict space.** `§4` says to
stop if the derivation establishes something none of the four verdicts
represents; **the VERDICT is one of the four. What is too strong is `A8`'s
stated consequence, not the verdict**, and `A8` asks what the verdict implies,
which `§7` answers as measured.

### 14.2 `OBSERVATION_METHOD_ERROR` — I committed `3b` into a contradiction I could have seen first

**`A9` requires the artifact blob identical at `3a`, `3b` and the head; `§7`
requires `3b` to append to that same file. Both are in the specification I read
before starting, and I noticed the conflict only after committing `3b`.**

**The clean move was available and `A9` names it: write no appendix and report
that `3b` does not exist.** I did not take it because I did not see the conflict.

**What I did instead was the best available afterwards** — report both ids, show
the `3a` content is a byte-exact prefix of `3b`, and decline to choose which
instruction prevails. **I did not rewrite history to make the ids match**, which
would have been forbidden and would also have destroyed the very evidence at
issue.

**Secondary, and also mine:** the previous task's report cited
`pyproject.toml:11` for a declaration at `:12`. That correction is already
landed on `main` in this task's evidence base and is not re-opened here.

### 14.3 `SPECIFICATION_DEFECT` — the "three `scripts/recon2026/` files"

**`A12` asks me to confirm "the three `scripts/recon2026/` files at their frozen
object ids". Only TWO files live under `scripts/recon2026/`.** The third frozen
file is `tests/test_recon2026_flat_limit.py`. **All three are unchanged and
`§11` reports all three with their paths as measured.** Not a stop; the operative
requirement holds.

### 14.4 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — first: the missing measure convention

**This is the task's own verdict and it is recorded here as the standing open
item.** `§5.3` names the missing line precisely. **Until a PI rules, every
determinant in the programme is computed under an unstated measure**, and `§13.2`
records that this applies to landed work.

### 14.5 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — second: the environment

**`docs/local/execution_environment.md` declares a WINDOWS environment with a
Python 3.12 interpreter. Every measurement here was on Linux with Python
3.11.15 — an UNDECLARED environment.** Unchanged and still unregistered; the
version policy covers versions and is silent on the platform.

### 14.6 `ENVIRONMENT`, `REPOSITORY_DEFECT` — nothing to report

**`ENVIRONMENT`: no failure. No restoration was needed or performed, and NEITHER
of Rule 13's two diagnostic orders was exercised.**

**`REPOSITORY_DEFECT`: none found by this task.** 484 of 484 base paths
blob-identical, both pins recompute, `^## P2-` is 14, the three frozen files
carry their base object ids, all four checker invocations pass at 21 parsed
values, and the validators are steady at 332.

**`§14.4`'s missing convention is classified as a governance ambiguity rather
than a repository defect** — the repository is not broken; it is silent, and the
silence had not been located before.

## 15. Did deriving make me want to evaluate a candidate, assemble the determinant combination, or choose the measure that gives a familiar answer?

**All three, and the third is the one that mattered.**

**EVALUATING A CANDIDATE BEFORE THE FREEZE: yes, and the pull was concrete.** The
previous executor reported being one line of arithmetic from the combination with
both `logdet`s printed; **this task starts from that position and adds a reason
to look** — I wanted to know whether the difference was `m`-independent before
committing to an argument that it was.

**I did not.** `§2` forbids it and `A4` bounds what is permitted to the premise.
**The alternative was better than the shortcut: I derived
`det G1 = ∏_x det g(x)` from the block structure and read mass-independence off
`G1`'s definition, both before `3a`.** **Then the appendix confirmed both to
`1.4e-12` and `1.7e-14`.** **Deriving first and checking second is what let the
check be evidence; had I measured first, the derivation would have been a story
told about a number.**

**ASSEMBLING THE DETERMINANT COMBINATION: yes, weakly, and it never became
tempting** — because `§6`'s argument makes the combination irrelevant to the
question. Once the difference is known to be ultralocal and `m`-independent,
assembling anything `k`-dependent adds nothing to the adjudication. **Not
assembled at any stage, including in the appendix.**

**CHOOSING THE MEASURE THAT GIVES A FAMILIAR ANSWER: THIS IS THE ONE, AND IT WAS
SUBTLER THAN I EXPECTED.** The temptation was not to reverse-engineer from the
anchor. **It was to write `OPERATOR-DETERMINANT` because standard formalism gives
it, the DeWitt metric is genuinely `√g g^{μν}`, and `𝔊 = G1` makes the factors
cancel beautifully.** That verdict would have been defensible, would have read as
derived, and **would have quietly promoted a textbook convention into a
repository ruling** — which is the exact failure the specification's own `§11`
records an earlier draft committing, and which `SIGN-01` was written to prevent
on a different question.

**What stopped it was the distinction the review's `§10` insists on:** what the
repository freezes, what follows from standard formalism, and what is a lattice
choice are three different things. **`§5.3` records the textbook answer as
textbook and the verdict as `NOT DETERMINABLE`, and I think that separation is
the most useful thing this task produced.**

**I evaluated no candidate before the freeze, assembled nothing, and chose no
measure.** `§11` measures 484 of 484 base paths blob-identical.

## 16. Evidence layering

**This report is committed as commit 4 and MEASURES COMMIT 3b. Nothing in it
claims to measure commit 4.**

**Committed here, measured at commit 3b:** `A1`–`A13`, `A15` and `A16` for
commits 1, 2, 3a and 3b; `A14`'s two runs with both configs and `RUN 2`'s output
verbatim; the four commit SHAs and stored messages; commit 4's INTENDED message;
`A11`'s cumulative figures at commits 1, 2, 3a and 3b as MEASURED and at commit 4
as INTENDED.

**Post-report evidence, returned to the Reviewer and NOT written back:** `A11`'s
final scope measured base-to-commit-4; `A14-final`, being `RUN 2` re-run at
commit 4; `A15` at commit 4; `A16` for commit 4; the push; and the branch tip
read back.
