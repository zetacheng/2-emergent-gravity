# Report — `SRC-B0`: can this programme ask whether two configurations attract?

    TASK        src-b0-source-side-scope
    BRANCH      science/src-b0-source-side-scope
    BASE        0a7a988cb1c1ca7de4cbfebd46fd690245789a2d
    SPEC SHA    a14625c4ca6aa4a629752a7f391b786fd5f236a884379f6b79b02a9675c2cce2
    REVIEW      APPROVE FOR EXECUTION, bound to that SHA
    VERDICT     NOT PRESENT / EXTERNAL STATUS NOT DETERMINED

**EVERY FIGURE IS MEASURED AT COMMIT 3 (`21f8b910`) UNLESS THE LINE SAYS
`INTENDED`.** This report is commit 4. **Nothing here claims to measure commit
4**; the commit-4 evidence is returned to the Reviewer in chat and is not
written back into this file.

**THIS TASK COMPUTED NO PHYSICAL QUANTITY.** The symbolic work in §7 derives the
STRUCTURE of a functional derivative and the dimensional dependence of a
determinant. Neither is a value of a physical quantity, and §12 verifies that
by search.

## 1. `A3` — environment, run FIRST

**Rule 13's diagnostic order applies and was NOT exercised: no environment
failure occurred.** Rule 13 carries two such orders — a known open item — and
because nothing failed I name neither as the one used.

**Amendment D step 0, taken before anything else:**

    execution location   vm — Linux 6.18.5-fc-v20
    git common dir       /home/user/2-emergent-gravity/.git
    resolved HEAD at step 0   bfef924c368658cac85c04ed18d96eb4450afba6
    HEAD symbolic ref at step 0   refs/heads/claude/paper-2-independent-verification-dysdp0
    task worktree        /tmp/.../scratchpad/srcb0, branch science/src-b0-source-side-scope

**Clone depth, as `A3` requires:**

    git rev-parse --is-shallow-repository    false
    git rev-list --count HEAD                423
    git rev-list --count --all               519

**THE CLONE IS NOT SHALLOW.** It was shallow earlier in this session and was
deepened by `git fetch --unshallow`. **That is the origin of the recurring stop-hook
claim of "405 unpushed commits" on the session branch: the 405 is
`5395d4b3..bfef924c`, `main`'s own published history made countable by the
unshallowing.** The session branch has nothing unpublished and was not pushed.

**Toolchain, MEASURED:**

    python   3.11.15 (main, Mar  3 2026, 09:26:23) [GCC 13.3.0]
    pytest   9.1.1
    numpy    2.4.6
    sympy    1.14.0
    ruff     0.15.8
    scipy    ABSENT — ModuleNotFoundError: No module named 'scipy'

**`pyproject.toml:12` declares `"scipy>=1.11"` and it is not installed.** Sixth
consecutive task. Nothing here needed it; **the symbolic work used `sympy`,
which is present.**

**`docs/local/execution_environment.md` declares a Windows environment**
(`zeta-3070\codexsandboxoffline`, Python 3.12, `C:\p2-validator\venv`). Every
run has been on Linux. Undeclared and unregistered.

## 2. `A1` — repository, refs, branch availability

**`origin` URL, verbatim as measured, not normalised:**

    https://github.com/zetacheng/2-emergent-gravity

**It identifies `zetacheng/2-emergent-gravity`.** The URL form is HTTPS without
a `.git` suffix; either form is accepted by `A1`.

    fetched, then:
    refs/remotes/origin/main   0a7a988cb1c1ca7de4cbfebd46fd690245789a2d
    A1 expects                 0a7a988cb1c1ca7de4cbfebd46fd690245789a2d   MATCH
    refs/heads/main            1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab   STALE LOCAL REF

**`refs/heads/main` is reported for contrast and is 
not this task's base.** The branch was cut from `refs/remotes/origin/main`, the
authoritative ref. **`main` is not touched by this task at all.**

**Branch availability:**

    refs/heads/science/src-b0-source-side-scope     DID NOT EXIST
    origin refs/heads/science/src-b0-source-side-scope   0 matching refs

**Neither existed, so no stop was triggered.** The branch was created from
`refs/remotes/origin/main`.

## 3. `A2` — the review, committed unedited

**FIELD PRESENCE CHECKED FIRST, THEN THE VALUE** — as `A2` requires, because a
review with no `reviewed specification SHA-256:` field at all would otherwise
pass a naive comparison against an empty string.

    field present?     YES — review line 4: "**Reviewed specification SHA-256:**"
    value, line 5      a14625c4ca6aa4a629752a7f391b786fd5f236a884379f6b79b02a9675c2cce2
    uploaded spec      a14625c4ca6aa4a629752a7f391b786fd5f236a884379f6b79b02a9675c2cce2
    IDENTICAL
    committed spec blob (sha256 of file bytes)   a14625c4…   IDENTICAL
    verdict, line 7    APPROVE FOR EXECUTION

**The review states it "supersedes any review bound to an earlier pre-rebase
version".** The specification I executed is the rebased one the review approved.

## 4. `A4` — the right-side search, re-run over the WHOLE TREE

**The specification's author searched `derivations/` and measured zero on eight
terms. The whole-tree search does NOT return zero, and `A4` required the
difference reported.**

    TERM                 FILES   CLASSIFICATION OF THE HITS
    stress tensor            5   2 this task's spec+review · 2 manuscript+twin ·
                                 1 results/recovered-2026/session_log_full.md
    energy-momentum          3   1 this task's spec · 2 manuscript+twin
    T_{mu nu}                1   this task's specification only
    T_mu_nu                  1   this task's review only
    source term              1   this task's specification only
    Einstein equation        3   1 this task's spec · 2 manuscript+twin
    field equation           3   1 this task's spec · 2 manuscript+twin
    geodesic                 1   this task's specification only
    test particle            1   this task's specification only
    Poisson                  3   1 this task's spec · 2 manuscript+twin
    Newtonian limit          7   1 this task's spec · 2 manuscript+twin ·
                                 1 session_log_full.md · 3 programme text

**Variants also run and null: `energy momentum` 0, `T_{\mu\nu}` 0, `T_munu` 0,
`T_{μν}` 0, `Tmunu` 0.**

**EVERY NON-ZERO COUNT RESOLVES INTO THREE CLASSES, AND NOT ONE IS A REPOSITORY
COMPUTATION.**

**Class 1 — this task's own committed specification and review.** Six of the
eleven terms appear ONLY there. Commits 1 and 2 installed the search vocabulary
into the corpus two commits before the search ran.

**Class 2 — the manuscript under verification**, `paper/emergent_gr_paper_v2_15.tex`,
its recovered duplicate `results/recovered-2026/emergent_gr_paper_v2_7.tex`, and
the recovered chat log `results/recovered-2026/session_log_full.md`. **The
manuscript is the object being verified, not verified material.**

**Class 3 — three programme-text hits, all for `Newtonian limit` alone:**

    README.md:6                        "…Einstein-Hilbert term, Newtonian limit,
                                        and induced gravitational source."
    GATES.md:1191                      "…a headwind for a healthy Newtonian limit,
                                        not a help: SI-2 is more likely to fail
                                        than to pass."
    P2-CHANNEL-FREEZE-01_phaseA:222     the same sentence in the gate's artifact

**THE DIFFERENCE FROM THE AUTHOR'S MEASUREMENT IS ENTIRELY EXPLAINED BY SCOPE**,
and the author's conclusion survives it: **nothing under `derivations/`,
`scripts/`, `tests/` or `results/` computes a right-hand side.** What the wider
search adds is that the manuscript writes one down (§7.1) and that `README.md:6`
names "induced gravitational source" as core scientific responsibility of this
repository — **declared, and unmet.**

## 5. `A5` — the configuration search, and the availability verdict

**Whole-tree, by CONTENT and separately by FILENAME:**

    TERM                CONTENT FILES   FILENAME MATCHES
    sparc                           4                  0
    halo                            5                  0
    soliton                         1                  0
    domain wall                     3                  0
    domain-wall                     6                  0
    yukawa                          8                  0
    rotation curve                  1                  0
    rotation-curve                  2                  0
    profile                         8                  0
    r_c (token \br_c\b)             4                  0

**The Researcher's "NO FILES MATCH" reproduces exactly on the filename measure:
zero on every term.** The content measure is not zero, and every content hit
classifies:

- **`soliton`, `rotation curve`, `rotation-curve` — this task's own spec and
  review only.**
- **`sparc`, `halo`, `yukawa` — the manuscript, and only as references to Paper
  1**, a separate repository and a manuscript in preparation.
- **`profile`, `domain-wall`, `r_c` — governance and unrelated technical text,
  plus the two manuscript lines `paper:615` and `paper:619`.**

**No profile function, no parameter values, no fitted potential.**

### 5.1 The verdict

> **`NOT PRESENT / EXTERNAL STATUS NOT DETERMINED`**

**THE PROPOSED SOURCE-SIDE CALCULATION CANNOT PRESENTLY BE EXECUTED FROM
REPOSITORY MATERIALS.** There is no configuration here whose `T_μν` could be
computed.

**I DO NOT CHARACTERISE WHAT IS OUTSIDE**, and §3 of the artifact records why
that is a measurement rather than a concession: **this repository's own two
descriptions of the cited work point in opposite directions.** The body text at
`paper:206-208` says "we **derived** a Yukawa-type dark matter halo profile …
and **tested** it against 175 SPARC galaxies"; the bibliography title at
`paper:1815-1816` reads "…Condensate: **Fits** to 175 SPARC Galaxies".
**A rule that a title cannot settle provenance is normally a caution about
inference; here it is a fact about the evidence in front of me.**

**The non-circularity statement, stated because `A5` requires it in the
`FITTED` branch and the reasoning is what makes the verdict matter:** if a
profile were fitted to the same rotation-curve data against which a
reconstructed potential is then judged, reproducing that data would carry no
information. **This task does not determine whether that is the case**, and
therefore does not claim the calculation would be circular — only that it
cannot be posed from what is here.

**`NOT PRESENT` IS A STATEMENT ABOUT THIS REPOSITORY, NOT ABOUT THE PHYSICS.**

**What would have to land** — four items, listed in the artifact §3: the
configuration as a function with the equations it solves; its provenance record
stated by whoever lands it; the reference observable in readable form; and the
`r_c` scaling relation if it is part of the comparison.

**THE CALCULATION IS BLOCKED AND THIS ASSESSMENT CONTINUED**, per `A5`. The
remaining questions are more useful under `NOT PRESENT`, not less: they name
what would have to exist.

## 6. `A8` — Paper 1's material

**MEASURED. The potential, the profile and the `r_c` scaling relation are NOT
present in any form this repository can read.**

**The `r_c ∝ V_max^{0.82}` relation in particular.** Searching the whole tree
for `0.82` as a standalone decimal — `(^|[^0-9.])0\.82([^0-9]|$)`, so that
digit runs inside SHAs do not count — returns **exactly one file: this task's
own specification, at its line 130, the sentence asking whether the relation
exists.** A naive substring search for `0.82` returns 30 files, all of them
fragments of hashes and unrelated decimals. **The relation exists nowhere else
in the repository.**

**`V_max` appears in four files and is a different object** — the Fierz
effective-potential envelope `[V_min, V_max]` of `P2-PHASE-01`, not a rotation
velocity.

**What IS present is a citation, one descriptive sentence, and a title**, all
in the manuscript. `paper:613-615` additionally states the functional FORM —
"The static field equation of `θ̃` is that of a massive scalar, with Yukawa
Green's function of range `r_c = 1/m_θ`" — but **a form is not a profile: no
amplitude, no normalisation, no parameter values, and no data.**

**What would have to land here first:** the potential or observable itself in a
machine-readable form, its provenance record, and the coupling chain the
manuscript itself records as open at `paper:633-643` — where the angular mode's
coupling to baryonic matter "remains open", is "deferred to future work", and
"in Ref. [Cheng:2025sparc] the coupling is treated as an effective parameter".

**I did not import, reconstruct or restate any of it.**

## 7. `A6` — `T_μν`'s definitional dependence, in four parts

### 7.1 Does defining `T_μν` require the measure `DET-01` found unfixed?

**CONDITIONALLY YES, AND THE CONDITION IS WHICH OBJECT IS MEANT.**

**`T_μν = (2/√g) δΓ/δg^{μν}` requires `Γ`, and `DET-01` established that the
functional measure is `NOT DETERMINABLE` from the frozen conventions.** So a
stress tensor defined from the full quantum effective action **does** inherit
the unfixed measure.

**THAT IS NOT A UNIVERSAL THEOREM, AND THE REPOSITORY SUPPLIES THE
COUNTEREXAMPLE ITSELF.** The manuscript defines, at
`paper/emergent_gr_paper_v2_15.tex:673-676`,

> `T^{μν} = (i/4) ψ̄ γ^{(μ} ∂⃡^{ν)} ψ + h.c. − η^{μν} L`

and calls it at `:678-679` "the symmetric energy-momentum tensor of the
fermions". **That is a bilinear operator built from the CLASSICAL action.
Varying a classical action needs no functional measure at all.**

    Γ-DEFINED   T_μν = (2/√g) δΓ/δg^{μν}    REQUIRES the unfixed measure
    S-DEFINED   T_μν = (2/√g) δS/δg^{μν}    DOES NOT

**WHICH ROAD THE PROPOSED CALCULATION TAKES IS NOT SETTLED HERE**, because it
depends on a configuration that is not present: a one-loop condensate expectation
value takes the first, a classical soliton of a stated effective action the
second. **I report which object the repository supports rather than converting
the `Γ` definition into a universal statement.**

**And the manuscript's own use of its `T^{μν}` runs the other way.** At
`:462-465` the graviton "is obtained by the induced-gravity route … one couples
the fermions to an external metric perturbation and reads off the induced
dynamics from the stress-tensor correlators" — the EMT is an INPUT to the
left-side calculation. **At `:1515-1523` the Newtonian-limit section takes the
source as GIVEN**, writing the linearized Einstein equation "sourced by a static
mass distribution `T^{00} = ρ(r)`" and reading off `∇²Φ_N = 4πGρ`. **`ρ` is an
input there; nothing derives it from the condensate.**

### 7.2 Does `DET-01`'s rider carry over to `δ/δg`? DERIVED, and NO

**I did not assume it. I derived it.**

**METHOD: symbolic, `sympy` 1.14.0, over a general symmetric `4×4` inverse
metric `g^{μν}` of ten free symbols.** For the case `DET-01` established —
`det G1 = ∏ₓ det g(x)` in four dimensions, so the candidate difference is
`±½ Σₓ log det g(x)` — take `F(g) = ½ log det g`:

    δ/δg^{μν}(y)  Σₓ F(g(x))  =  [ ∂F/∂g^{μν} ](y) · δ_{x,y}      ULTRALOCAL

    ∂/∂g^{μν} [ ½ log det g ]  =  − ½ g_{μν}                       NOT ZERO

**Every component of the symbolic derivative matched the closed form `−½ g_{μν}`
with residual exactly `0`**, taking the symmetric-matrix multiplicity into
account for the off-diagonal symbols.

**THE RIDER DOES NOT CARRY OVER.** `DET-01` proved that the ambiguity does not
reach the `m² ln m²` coefficient of `Z`. **It reaches a `Γ`-defined stress
tensor.**

**The STRUCTURE of what it contributes is the substantive part:**

- **not zero** — so a `Γ`-defined `T_μν` inherits an undetermined piece;
- **still ultralocal** — a `δ_{x,y}`, no derivatives of the metric;
- **proportional to `g_{μν}` itself** — the form of a cosmological-constant /
  vacuum stress tensor, `T_μν ∝ g_{μν}`;
- **independent of the configuration** — `F` is a function of the metric alone,
  so the term is identical for a lump and for the vacuum around it at the same
  metric.

**SO THE AMBIGUITY ENTERS THE SOURCE OBSERVABLE AS AN UNDETERMINED VACUUM-LIKE
TERM — exactly where `DET-01` said the unfixed measure would land.** The two
derivations are of different objects and they agree. **Nothing here settles the
measure or chooses a `𝔊`.**

### 7.3 Could a background-subtracted stress tensor remove it?

**ALGEBRAICALLY, AT FIXED METRIC, YES. GOVERNANCE-WISE, NO PRESCRIPTION IS
AVAILABLE — AND THE ONE THE REPOSITORY HAS FROZEN IS ADVERSE.**

**The algebra is favourable for a reason stronger than ultralocality:** because
the term depends on `g(x)` alone and not on the configuration, a difference
taken between two configurations at the SAME metric cancels it identically.
**Ultralocality alone would not give that; configuration-independence does.**

**MEASURED — no frozen subtraction prescription exists:**

    P2-LATTICE-ONTOLOGY-01.md:191   "| Reference equivalence class and matching
                                     conditions | DELEGATED: FIERZSUM §4.2 / D-pre |"
    P2-LATTICE-ONTOLOGY-01.md:256   the renormalization deliverable "collapses into
                                     a finite, explicit subtraction-and-matching
                                     rule, which FIERZSUM MUST STILL FREEZE"

**AND THE FROZEN GOVERNANCE SEPARATION IS DIRECTLY ADVERSE**, at
`P2-LATTICE-ONTOLOGY-01.md:289-292`:

> "**Governance separation (frozen):** the response subtraction of `§2`
> authorizes removing the common baseline from RESPONSE observables only; it does
> not authorize deleting the substrate energy from the cosmological SOURCE."

**The subtraction this repository does have is authorised for RESPONSE
observables — the left side — and EXPRESSLY NOT for a SOURCE observable, which
is what the proposed calculation needs.** So the subtraction it would rely on is
not merely unfrozen: **the one thing frozen about it is that it does not reach
there.**

**A SECOND DEPENDENCY IS ALREADY ON RECORD**, at `P2-LATTICE-ROUTE-01.md:247-248`:
a later gate must verify "whether the flat/reference subtraction is applied
before or after `∂/∂G`; and whether the derivative and the subtraction commute."
**Subtract-then-vary and vary-then-subtract are exactly the two orders this
calculation would have to choose between, and the repository records the choice
as open.**

**DEPENDENCY: an explicit subtraction-and-matching rule covering SOURCE
observables, with its composition order against `δ/δg` fixed. Neither exists,
and one is currently withheld by a frozen separation rather than merely
absent.** **I did not invent one.**

### 7.4 The rider's dimensional scope

**MEASURED INDEPENDENTLY, not transcribed. The general relation follows from
`det(cM) = c^d det M` and `det(M⁻¹) = 1/det M`:**

    det[ √(det g) · g⁻¹ ] = (√(det g))^d · (det g)⁻¹ = (det g)^{d/2 − 1}

    d = 2   (det g)^0     = 1          NO DETERMINANT AT ALL
    d = 3   (det g)^{1/2}
    d = 4   (det g)^1     = det g      the DET-01 relation
    d = 5   (det g)^{3/2}
    d = 6   (det g)^2

**Confirmed symbolically in full at `d = 2` and `d = 3` — `lhs − rhs`
simplifies to `0` in both — and numerically on random symmetric
positive-definite matrices at `d = 4, 5, 6`, worst relative deviation
`3.6e-15`.**

**`d = 4` IS THE ONLY DIMENSION WHERE THE RELATION IS `det g`. At `d = 2` the
rider is EMPTY, not approximately true**: the determinant is identically `1` for
every metric, so there is no ambiguity to be ultralocal about.

**`RECON-01a`'s construction hard-codes the dimension** —
`scripts/recon2026/proca_curved.py:52` sets `DIM = 4` and every operator in the
module is built on it — **so the equality is a property of that construction,
not a general identity.**

**DOES THE LANDED ARTIFACT STATE THE QUALIFIER? ONCE, AND ONLY INSIDE THE
ALGEBRA.** `derivations/P2-BETAV-DET-01_measure-adjudication.md:64` reads "and
per site, with `g ≡ det g_{μν}` and `√g = g^{1/2}` in four dimensions," followed
at `:66` by `det[√g g⁻¹] = (√g)^4 · det(g⁻¹) = g² · g⁻¹ = g`. **The `(√g)^4`
carries the dimension.** **But the artifact's two headline statements of the
rider — `:24` and `:302` — carry no dimensional qualifier**, and a reader who
takes the rider without the algebra would read `det G1 = ∏ₓ det g(x)` as a
general identity. **It is not one.** Recorded, not repaired: this task modifies
nothing.

## 8. `A7` — dimensionlessness

**FINDING: NO REPOSITORY-GROUNDED DIMENSIONLESS COMPARISON HAS BEEN
ESTABLISHED.** That is not the claim that none could exist.

**The absolute route is blocked, and the blockers are already measured**, in
`derivations/P2-BETAV-RECON-01_scope-assessment.md` `§A8b`:

    R5   CONVENTIONS.md:20 defines Z per unit 4N with Z ≡ 1/(16πG_ind).
         "Converting a per-4N coefficient into an induced G requires N."
         R5 is OPEN — P2-CHANNEL-FREEZE-01_phaseA_freeze.md:43 keeps N symbolic.
    R1   canonical kinetic operator and species accounting — DELEGATED to D-pre
         at P2-LATTICE-ONTOLOGY-01.md:189.

**So a comparison requiring an absolute `G_ind` inherits `R5` and `R1`.**

**A dimensionless comparison would not** — `§A8a` of the same artifact records
that the RATIO depends on none of `R1`–`R5`, `R5` in particular cancelling
"in a ratio of two species coefficients both reported per unit `4N``". **The
escape route is real in principle, and the ratio side is the precedent for it.**

**BUT NO CONCRETE DIMENSIONLESS OBSERVABLE CAN BE BUILT FROM WHAT IS HERE, FOR
TWO INDEPENDENT REASONS.**

**First, a comparison needs two sides and the source side is absent.** A
shape-only comparison still requires both profiles; §5 measured that neither is
present.

**Second, the only length scale the repository names on the computed side is
imported from the data the comparison would test.** `paper:613-615` gives
`r_c = 1/m_θ`; `paper:618-620` then fixes `m_θ` FROM the observed scale — the
"SPARC-scale cutoff radii `r_c ∼ 10 kpc` correspond to `m_θ ∼ 10⁻²⁷ eV`". **Both
figures are QUOTED from those lines and nothing is computed here.** **The
inference runs phenomenology → parameter.** Using `r_c` as the computed side's
own scale would put the measured quantity inside the prediction.

**I did not invent a dimensionless observable because one is conceivable in
principle.** The correct finding is that none has been established from
repository material.

## 9. `A9` — what a failure criterion would have to fix

**NOTHING IS CHOSEN HERE. Choosing is a PI ruling.** What a pre-registration
must fix, BEFORE the number is seen:

    1  THE COMPARED QUANTITY — a specific functional, at a specific place, in
       specific units, THE SAME on both sides: a value at a stated radius, a
       logarithmic slope over a stated interval, a ratio of two radii, or a
       shape after a stated normalisation.  "The potential" is not a quantity.
    2  THE TOLERANCE — a number, with the metric it is measured in (relative,
       absolute, or in units of a stated uncertainty) and that uncertainty's
       own source, since neither side currently carries one.
    3  THE DIRECTION — which outcome is failure: a two-sided band, a one-sided
       bound, or a sign requirement; and which side is the prediction.

**A COMPARISON WITHOUT A FIXED TOLERANCE IS NOT A TEST.** It is a measurement
followed by a judgement made by someone who has already seen the measurement.

**THE FACTOR-OF-THREE CASE IS THE CLEAN EXAMPLE.** A factor-of-three
disagreement reads as "same order of magnitude — success for a parameter-free
calculation" or as "wrong by three". **Both are defensible, and which one wins
is decided after the number is seen unless the criterion is fixed first.**

## 10. `A10` — the component inventory

**Eleven components, each in exactly one of four mutually exclusive states. An
implementation counts only if POTENTIALLY APPLICABLE here.**

    #   COMPONENT                                          STATE
    1   metric-coupled lattice operator machinery           IMPL + SPEC
    2   validator / regression harness                      IMPL ONLY
    3   definition of a stress tensor for matter            SPEC ONLY
    4   a localized condensate configuration                NEITHER
    5   the functional measure for a Γ-defined T_μν         NEITHER
    6   a subtraction-and-matching rule covering SOURCES    NEITHER
    7   the absolute induced G (needs R5 and R1)            NEITHER
    8   the geometry map {t_ij} ↔ g, e, ω                   NEITHER
    9   a solver taking a source to a field or potential    NEITHER
    10  Paper 1's potential, profile, or r_c relation       NEITHER
    11  a pre-registered failure criterion                  NEITHER

    N_both    = 1
    N_impl    = 1
    N_spec    = 1
    N_neither = 8
    N_total   = 1 + 1 + 1 + 8 = 11

**Component 1** is `scripts/recon2026/proca_curved.py` and `flat_validation.py`,
specified by `P2-BETAV-RECON-01a` §C1–C6: exact `√g g⁻¹` factors, `K1`, `G1`,
`D1` on a weak-field background. Potentially applicable — it is the only code
here that knows about a metric.

**Component 3** is the manuscript's operator form at `paper:673-676`. **It is a
manuscript equation, not a verified repository prescription**, and it is the EMT
of the elementary fermion rather than of a condensate configuration.

**A LEXICAL TRAP IN COMPONENT 9, WORTH NAMING.**
`scripts/p2_phase01_scalar_exploratory.py:112` defines `reconstructed_potential`
and `scripts/p2_phase01_fierz_and_depths.py` calls it six times. **That is the
effective potential `V_eff` in field space, not a gravitational potential in
position space.** Counting it would have improved readiness by matching a word.

**COMPONENT 8 IS EASY TO OVERLOOK AND IS NOT SMALL.** The metric in
`RECON-01a` is an INPUT — `g = δ + h` supplied by hand. It is not built from
lattice variables. `P2-LATTICE-ONTOLOGY-01.md:190` records the geometry map
`{t_ij} ↔ g, e, ω` as `DELEGATED: D-pre`, and `:132-134` records that the
substrate variables to be promoted are "still to be identified". **A source-side
calculation would produce a `T_μν` with no frozen way to say which geometry its
configuration lives in.**

**THE COUNT IS AN INVENTORY, NOT A DIFFICULTY**, and this report estimates no
effort in time. Some of the eight may be short. **Component 5 is a question
`DET-01` proved cannot be answered from the present conventions at all**, which
is a different kind of missing.

## 11. `A12` — scope

**Manifest as declared:**

    stated: 4 additions, 0 modifications          INTENDED, final at commit 4
    append_only:  DECISION_LOG.md                 a CHECKER-CONFIGURATION declaration,
                                                  NOT an authorisation to write it
    authorised_gates: []
    base: 0a7a988cb1c1ca7de4cbfebd46fd690245789a2d
    head: commit 4
    mode: exact
    modify: []
    forbidden_operations: delete, rename, copy, type_change, unmerged, unknown

**`DECISION_LOG.md` was not written; its blob is unchanged from the base — §13.**

**CUMULATIVE per commit — MEASURED:**

    base .. commit 1  790c0712     1 addition,  0 modifications
    base .. commit 2  45d541d6     2 additions, 0 modifications
    base .. commit 3  21f8b910     3 additions, 0 modifications
    base .. commit 4               4 additions, 0 modifications   INTENDED

**CONTRIBUTION per commit — MEASURED, and separately labelled:**

    commit 1   A specs/2026-08-18T0507Z_src-b0-source-side-scope.md
    commit 2   A reviews/chatgpt/2026-08-18T0507Z_src-b0-source-side-scope.md
    commit 3   A derivations/P2-SRC-B0_source-side-scope.md
    commit 4   A reports/2026-08-18T0507Z_src-b0-source-side-scope.md   INTENDED

**Each commit contributes exactly one path, so cumulative and contribution
coincide numerically at every step here.** They are still reported separately,
because a reviewer of an earlier task read a cumulative figure as a contribution
and computed a total three too high — and the coincidence is a fact about this
task's shape, not a general identity.

**The UTC time was measured, not assumed: `2026-08-18T05:07:01Z`, giving the
token `0507Z`.** Commit 1 was made in the same minute.

## 12. `A11` — nothing computed

**SEARCHED: the artifact, this report and every commit message in the range, for
any computed physical quantity, any potential, any profile value, any
order-of-magnitude estimate, and any chosen tolerance.** Governance
measurements, file counts, line numbers, SHAs and quoted repository values are
excluded by `A11` itself.

    CATEGORY                              ARTIFACT   COMMIT MESSAGES
    a computed physical quantity                 1                 0
    a potential (a value of one)                 0                 0
    a profile value                              0                 0
    an order-of-magnitude estimate               0                 0
    a chosen tolerance                           0                 0

**THE SINGLE NON-ZERO IS A PATTERN ARTEFACT AND IT IS LOCATED, NOT ROUNDED
AWAY.** It is artifact line 228, "**THE STRUCTURE OF THE RESULT IS THE POINT.**"
— my pattern `the result is` matching an English sentence about structure.
**No value of any physical quantity is stated anywhere in the artifact.**

**Two classes of number DO appear in the artifact, and both are excluded by
`A11`'s own terms:** file counts and line numbers throughout, and **two quoted
repository values** — `r_c ∼ 10 kpc` and `m_θ ∼ 10⁻²⁷ eV`, both quoted from
`paper:618-620` with the line cited, in the course of showing that the scale on
the computed side would be imported from the data. **Neither was produced here.**

**What the symbolic work produced is a STRUCTURE, not a value:** that
`∂/∂g^{μν} [½ log det g] = −½ g_{μν}`, and that
`det[√g g⁻¹] = (det g)^{d/2−1}`. **Neither is a physical quantity, and §11 of the
review records this distinction as the correct reading of the no-computation
boundary.**

### 12.1 The same search over THIS report's bytes, and why no count is stated

**`A11` names the report as a search subject, so I ran the same five categories
over this file's bytes. It returns non-zero, and every hit is this section
itself.**

**I state that POSITIONALLY AND BY MECHANISM RATHER THAN AS A COUNT, DELIBERATELY.**
The `DET-01` report stated a count of `1` for a self-matching category and named
the line it sat on; the edit that produced the final text deleted the spelling
that caused the hit, so the committed report described bytes it no longer
contained. **A count of a document's own vocabulary is invalidated by any
subsequent edit to that document, including the edit that writes the count.**

**THE MECHANISM, WHICH IS STABLE UNDER EDITING:** every hit in this file falls
into one of two places — §12, which states the search terms in prose, carries
them again as the CATEGORY column of its table, and quotes the artifact's line
228 in order to classify it; and §19.3, which quotes that same line. **There is
no third place, and no hit anywhere in this file is a value of a physical
quantity.**

**The measurement that carries the prohibition is unaffected: the ARTIFACT and
ALL COMMIT MESSAGES are as tabulated above**, and those two subjects contain no
sentence about searching.

## 13. `A13` — nothing existing changed

    PATHS COMPARED (all paths at the evidence base)   491
    paths at the head                                 494
    paths whose blob DIFFERS at the head                0
    git diff --name-status base..head                   3 entries, ALL status A
    entries of any other status                         0

**Named confirmations, blob ids at the head:**

    GATES.md                              2b3bd5069414f009…   UNCHANGED
    CONVENTIONS.md                        8badc51f38d85d54…   UNCHANGED
    docs/BRANCHING_POLICY.md              3f0f35d4da448eb4…   UNCHANGED
    DECISION_LOG.md                       d9dd2bf3a8cca405…   UNCHANGED
    scripts/recon2026/proca_curved.py     03f46905e5798fb7…   UNCHANGED
    scripts/recon2026/flat_validation.py  6b21f9d6db67641e…   UNCHANGED
    tests/test_recon2026_flat_limit.py    1d7ba5672614dedc…   UNCHANGED

**`derivations/P2-BETAV-*` RE-MEASURED, not carried: EIGHT at the base and
EIGHT at the head.**

      P2-BETAV-ASSEMBLY-01_bookkeeping_regression.md
      P2-BETAV-CAMPAIGN_prereg.md
      P2-BETAV-CIRC-01_determinant-decomposition.md
      P2-BETAV-DET-01_measure-adjudication.md
      P2-BETAV-RECON-01_cleanroom_reconstruction.md
      P2-BETAV-RECON-01_scope-assessment.md
      P2-BETAV-RECON-01a_construction-and-flat-validation.md
      P2-BETAV-SIGN-01_anchor-reconciliation.md

**It was SEVEN at the previous base and the `DET-01` landing added one.** This
count was wrong in three consecutive specifications by being carried; it is
re-measured here and the specification's own pre-issue record of EIGHT
reproduces.

**Seven microspec artifacts**, all `derivations/P2-LATTICE-MICROSPEC-01_*`,
count 7, all unchanged. **Two files under `scripts/recon2026/`.** **Both
registers unchanged.** **`results/`: 69 paths at both ends, and the subtree
object is `9015049f68d5ace2790b5c62976e798298442bce` at both — one comparison
covering all 69.**

## 14. `A14` — gate invariants and pins

**Read SCOPED: the `P2-PHASE-01` section is `GATES.md:971–1108`, bounded by the
next `^## P2-` heading, and every value below was taken inside those bounds.**

    ^## P2- count                     14
    P2-PHASE-01 status  GATES.md:973  Status: PROPOSED
    prerequisite 1      GATES.md:1011 Artifact state: ADOPTED. Prerequisite state: SATISFIED
    prerequisite 2      GATES.md:1036 Artifact state: ADOPTED. Prerequisite state: SATISFIED

**Both pins verified by recomputing the digest of the artifact each pins:**

    derivations/P2-PHASE-01_microscopic_parameter_domain.md
      recomputed  4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
      pinned at GATES.md:1017 — MATCH
    derivations/P2-PHASE-01_input_admissibility_contract.md
      recomputed  e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
      pinned at GATES.md:1040 — MATCH

**All four invariants hold.**

## 15. `A15` — the checker over this task's own range

**Base `0a7a988c…`, head commit 3 `21f8b910…`. Two runs at both prospectivity
readings — four invocations, all exit `0`.**

**THE OUTPUT WAS PARSED, NOT GREPPED.** Each JSON file was loaded with
`json.loads` and every property read out of the parsed structure by key (`id`,
`status`, `classification`, `evidence`). **No status was determined by matching
text.** The property list is a JSON *array* of objects rather than a map keyed
by property id, so a key lookup returns `None` and a grep for `PASS` would count
the word wherever it occurs — including inside `does_not_establish` prose.

**`RUN 1` config, verbatim — observational, governs nothing:**

    {
      "base": "0a7a988cb1c1ca7de4cbfebd46fd690245789a2d",
      "head": "21f8b9104e02ca9c728a199fa98fab134999d36e",
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

**`RUN 2` config, verbatim — stop-governing, naming only this task's
specification:**

    {
      "base": "0a7a988cb1c1ca7de4cbfebd46fd690245789a2d",
      "head": "21f8b9104e02ca9c728a199fa98fab134999d36e",
      "specification_paths": [
        "specs/2026-08-18T0507Z_src-b0-source-side-scope.md"
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

**Each `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.**

**Results, identical across all four invocations:**

    P1  PASS             PARTIAL     scope manifest arithmetic
    P2  PASS             MECHANICAL  Rule 15 commit order
    P3  PASS             PARTIAL     append-only on both measures      declared_source: specification
    P4  PASS             MECHANICAL  superseded branches are not merged
    P5  NOT_APPLICABLE   PARTIAL     merge parentage against recomputed facts
    P6  PASS             PARTIAL     commit-message hygiene
    P7  PASS             PARTIAL     gate integrity                    declared_source: specification
    P8  PASS             MECHANICAL  Rule 15 placement and specification-first
    P9  NOT_APPLICABLE   MECHANICAL  reports carry a Stops and clarifications section

    overall                        PASS
    exit status, all four           0
    NOT_DECLARED                    none
    NOT_PARSEABLE                   none
    DECLARATION_CONFLICT            NONE — confirmed
    commits_in_range                3
    commits_on_first_parent_line    3
    prospectivity in scope 3, out of scope []

**`P7` REPORTS FOURTEEN SECTIONS** — `section_count_base` 14, `section_count_head`
14, `raw_heading_count_base` 14, `raw_heading_count_head` 14. **`PASS` at zero
would have been a stop; it is not zero.**

**`P5` and `P9` are `NOT_APPLICABLE`, and that is the correct result, not a weak
pass.** There is no merge in this range, so `P5` has no subject; and at commit 3
no report exists yet, so `P9` has none either. **`NOT_APPLICABLE` does not make
the run incomplete, and the checker's own vocabulary distinguishes it from
`DECLARED_EMPTY` and from `PASS`.**

**`P3`'s evidence records `DECISION_LOG.md` unchanged from the base**, which
satisfies append-only on both measures trivially.

### 15.1 What `RUN 1` did

**`RUN 1`'s default subject selection discovered exactly ONE specification in
range — this task's:**

    specs/2026-08-18T0507Z_src-b0-source-side-scope.md
      stated: 4 additions, 0 modifications    counted 4 (add 4 / mod 0)   parse OK

**`RUN 1` and `RUN 2` are therefore BYTE-IDENTICAL at each reading**, `diff`
returning nothing, so the four invocations produce exactly TWO distinct byte
strings, differing only at line 252, the `inclusivity` value. **That does not
make them the same check: `RUN 2` names the subject and `RUN 1` discovers it.
They agree here because there is only one subject to find.**

**THE `C3` MULTI-SPECIFICATION RESIDUAL DID NOT ARISE, and the reason is that
there is ONE declaring specification — the "cannot trigger" half.** The previous
task's range had two specifications with differing stated totals (4 and 7) and
raised no `DECLARATION_CONFLICT`, because `_declarations_from_specs` compares
`append_only_paths` and `authorised_modified_gates` and not stated totals.
**Unchanged, and still unregistered.**

**Neither the config nor this specification's declarations were adjusted to make
`RUN 2` pass. `RUN 2` passed on its first invocation at both readings**, and
every value in both configs was supplied by the specification.

### 15.2 The JSON output, verbatim

**`RUN 1` and `RUN 2` at the `INCLUSIVE` reading are BYTE-IDENTICAL — `diff`
returns nothing — so the file below IS both outputs, not a sample of one.**
**Each `EXCLUSIVE` output is this file with line 252 reading
`"inclusivity": "EXCLUSIVE"`, and is otherwise identical.**

    {
      "base": "0a7a988cb1c1ca7de4cbfebd46fd690245789a2d",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "21f8b9104e02ca9c728a199fa98fab134999d36e",
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
                "derivations/P2-SRC-B0_source-side-scope.md",
                "reports/2026-08-XXT{HHMM}Z_src-b0-source-side-scope.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_src-b0-source-side-scope.md",
                "specs/2026-08-XXT{HHMM}Z_src-b0-source-side-scope.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-18T0507Z_src-b0-source-side-scope.md",
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
                "commit": "790c07122c116690b88a5367c097df5a6947a343",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "45d541d629ce1a609ffbc185b9a562f078dbe444",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "21f8b9104e02ca9c728a199fa98fab134999d36e",
                "work_paths": [
                  "derivations/P2-SRC-B0_source-side-scope.md"
                ]
              }
            ],
            "first_review_commit": "45d541d629ce1a609ffbc185b9a562f078dbe444",
            "first_work_commit": "21f8b9104e02ca9c728a199fa98fab134999d36e",
            "in_scope": 3,
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
              "specs/2026-08-18T0507Z_src-b0-source-side-scope.md"
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
              "commit": "790c07122c116690b88a5367c097df5a6947a343",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "45d541d629ce1a609ffbc185b9a562f078dbe444",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "21f8b9104e02ca9c728a199fa98fab134999d36e",
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
              "specs/2026-08-18T0507Z_src-b0-source-side-scope.md"
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
            "first_commit": "790c07122c116690b88a5367c097df5a6947a343",
            "first_commit_paths": [
              "specs/2026-08-18T0507Z_src-b0-source-side-scope.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-18T0507Z_src-b0-source-side-scope.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-18T0507Z_src-b0-source-side-scope.md"
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
        "commits_in_scope": 3,
        "commits_out_of_scope": [],
        "inclusivity": "INCLUSIVE",
        "scope_note": "P2, P5, P8 and P9 walk the task's own first-parent line; commits arriving by merge were governed by the task that made them."
      },
      "tool": "task_checker"
    }

## 16. `A16` and `A17` — validators and hygiene

    python3 -m pytest -q         332 passed, 2 deselected in 39.34s
    exit status                  0

**332 passed, 2 deselected, exactly as expected.** This task adds no code, so the
count is unchanged from the evidence base.

**`A17` — commit-message hygiene. Rule 20 binds this task and was not needed: no
message required repair and no history was rewritten.**

    commit 1  790c07122c116690b88a5367c097df5a6947a343
              spec: can this programme ask whether two configurations attract
    commit 2  45d541d629ce1a609ffbc185b9a562f078dbe444
              review: pre-execution review for the source-side scope assessment
    commit 3  21f8b9104e02ca9c728a199fa98fab134999d36e
              scope: the source side is not present, and the rider does not survive a metric variation
    commit 4  INTENDED message:
              report: the source side is absent, and the measure ambiguity reaches T

**Forbidden-token scan over every message in the range:**

    Co-Authored-By          0        Generated with        0
    Co-authored-by          0        Claude-Session        0
    claude.ai/code          0        any model identifier  0
    🤖                      0        noreply@anthropic.com 0

**All zero. `A17` for commit 4 is post-report evidence and is not written here.**

## 17. `§6` — Rule 16 assessment: what the assembled set does NOT establish

### 17.1 First — `NOT PRESENT` is not a physics verdict

**A `NOT PRESENT` verdict does not mean the physics is wrong. It means the
calculation cannot be posed non-circularly from what is here.** The PI's
intuition — that an inhomogeneous condensate lump should source a gravitational
field, and that this programme's own induced `G` should govern it — is not
touched by this finding. **Nothing here bears on whether it is true.**

**WHAT WOULD CHANGE IT** is listed in `§5` and `§6`: the configuration as a
function with its equations and boundary conditions; a provenance record stated
by whoever lands it; the reference observable in readable form; and, if the
`r_c` relation is to be part of the comparison, that relation. **Four items, and
none of them requires this repository to change anything it has already
established.**

### 17.2 Second — this assessment is bounded by this repository

**Paper 1 is a separate repository and a manuscript in preparation.** **A
configuration existing there is not a configuration available here.**

**WHAT I COULD DETERMINE:** that no profile, potential, parameter value or
scaling relation is present in this repository under any of the searched terms,
by content or by filename; that the `0.82` relation occurs in exactly one file,
this task's own specification; that the manuscript cites Paper 1 in eleven
places and describes it in one sentence.

**WHAT I COULD NOT DETERMINE:** whether the external configuration is derived or
fitted. **And the reason is sharper than the general caution against inferring
from a title.** This repository's own two descriptions of the same work
disagree: `paper:206-208` says "we **derived** … and **tested** it", while the
bibliography title at `:1815-1816` says "**Fits** to 175 SPARC Galaxies". **The
evidence available here is internally ambivalent, which is why a filename — or a
title — cannot settle it.**

### 17.3 Third — the PI's question is not the question this programme answers

**The programme computes the coefficient of `∫√g R`: how stiff spacetime is.
The PI asked for a solution with a source: what curves it, and whether two
lumps of it attract.**

**BOTH ARE LEGITIMATE PHYSICS QUESTIONS ABOUT THE SAME THEORY. ONLY THE FIRST
HAS BEEN ATTEMPTED.**

**And the second was in scope from the beginning:** `README.md:6` names
"induced gravitational source" among this repository's core scientific
responsibilities. **The gap is not an oversight discovered by this task; it is a
declared responsibility that no gate has taken up.**

**A third fact belongs here, from the specification's own pre-issue record and
confirmed by me:** `P2-LATTICE-ONTOLOGY-01.md:190` delegates the geometry map
`{t_ij} ↔ g, e, ω` to D-pre, and `:132-134` records that the lattice degrees of
freedom corresponding to the metric are "still to be identified". **The metric
used in `RECON-01a` is an input, not an emergent quantity.** So even the
left-side calculation works with a geometry it has not yet derived from the
substrate — **which is worth stating plainly, because a source-side calculation
would need that map and the left side has been able to proceed without it.**

### 17.4 Fourth — the vacuum, stated exactly

**A homogeneous Lorentz-invariant vacuum contributes a
cosmological-constant-type stress tensor.** **It does not provide the localized,
clustering source the proposed halo and rotation-curve test requires.**

**AND THAT IS NOT THE SAME AS HAVING NO GRAVITATIONAL EFFECT, WHICH WOULD BE
FALSE.** A cosmological-constant stress-energy gravitates; a positive `Λ`
produces de Sitter-type relative acceleration. **Saying "two uniform regions do
not attract" conflates "no localized clustering source" with "no gravitational
effect at all".**

**What provides a clustering source is INHOMOGENEITY** — a condensate lump
differing from the vacuum around it. **THE PROPOSED CALCULATION THEREFORE PROBES
THE CONDENSATE'S INHOMOGENEOUS SECTOR**, and **a null result there would say
nothing about the vacuum sector, which `DET-01` left unfixed.**

**§7.2 sharpens that last clause into a measurement rather than a caveat.** The
measure ambiguity's contribution to a `Γ`-defined `T_μν` is `∝ g_{μν}`,
ultralocal, and configuration-independent. **It is a vacuum term exactly, and it
is exactly the sector a null inhomogeneous result would leave untouched.**

### 17.5 Fifth — a component count is not a difficulty

**Eleven components with eight missing is an inventory.** It is not an effort
estimate, and this report gives none: `§3` of the specification forbids
estimating effort in time, and counting components is what replaced it.

**AND AN ASSESSMENT THAT FOUND THE CALCULATION POSABLE WOULD NOT HAVE MADE IT
LIKELY TO SUCCEED.** Posability is about whether the question can be asked.
**Whether the answer would agree with anything is a different matter entirely,
and no part of this assessment bears on it.**

## 18. The temptation, answered directly

**Did assessing make me want to compute a potential?** **Yes, and the pull was
concrete rather than vague.** By `§7.2` I had the structure of the ambiguity's
contribution, and by `§8` I had the manuscript's statement that the mode's
Green's function is Yukawa with range `r_c = 1/m_θ`. **Writing down a Yukawa
potential from those two facts is one line, and it would have looked like
analysis.** **It would have been a physical quantity produced by this task,
which `§3` forbids and `A11` searches for.** I did not.

**Did I want to estimate an order of magnitude?** **Yes, and this was the
stronger pull, because the repository hands you the numbers.** `paper:618-620`
quotes `r_c ∼ 10 kpc` and `m_θ ∼ 10⁻²⁷ eV`. **Multiplying anything by anything
there would have produced a number the PI has been asking about all session.**
**I quoted both figures with their line and did nothing else with them** — which
is precisely the line `A11` draws between a quoted repository value and a
computed one.

**Did I want to reconstruct Paper 1's profile from memory?** **Briefly, and
this is the one I want to be most explicit about, because I cannot fully verify
my own compliance.** The paper's description is specific enough — Yukawa, scalar
sector, 175 SPARC galaxies — that a plausible functional form suggests itself.
**Writing it would have made the `NOT PRESENT` verdict disappear and replaced a
measurement with a recollection.** **I did not**, and the artifact contains no
functional form for any profile. **What I can verify is the artifact's bytes;
what I cannot verify is that no recollection influenced how I read the
repository, and I say so rather than claiming an isolation I cannot demonstrate.**

**THE THING THAT MADE DECLINING EASY WAS THE VERDICT ITSELF.** `NOT PRESENT`
is not a disappointing result to a task whose subject is whether a calculation
can be posed. **It is the answer, and it is more useful than a computed number
would have been, because it names four things that would have to land.**

## 19. Stops and clarifications

**NO STOP WAS DECLARED. All acceptance criteria completed.** One primary
category per finding; secondary findings separate.

### 19.1 Stops

**NONE.**

### 19.2 Findings, one primary category each

**`REPOSITORY_DEFECT` — `README.md:6` declares "induced gravitational source"
as a core scientific responsibility of this repository, and no repository
computation addresses it.** Recorded as an observation about programme scope,
not attributed to any task. §4.

**`REPOSITORY_DEFECT` — the landed `DET-01` artifact states the rider without
its dimensional qualifier** at `:24` and `:302`, carrying `in four dimensions`
only inside the algebra at `:64`. **The relation `det[√g g⁻¹] = det g` holds at
`d = 4` alone and is EMPTY at `d = 2`.** Not repaired; this task modifies
nothing. §7.4.

**`REPOSITORY_DEFECT` — the `C3` multi-specification residual remains
unregistered.** It could not trigger in this range (one declaring
specification), but it did arise in the immediately preceding range with two
specifications declaring differing totals and raised nothing. §15.1.

**`ENVIRONMENT` — `scipy` is declared at `pyproject.toml:12` and is not
installed.** Sixth consecutive task. Not needed here. §1.

**`ENVIRONMENT` — `docs/local/execution_environment.md` declares a Windows
environment that has never been the one used.** Undeclared, unregistered. §1.

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — a naive `0.82`
substring search returns 30 files, all fragments of hashes and unrelated
decimals.** The standalone-decimal pattern returns one. **Reporting the naive
count would have suggested the scaling relation is widespread when it occurs
exactly once, in the sentence asking about it.** §6.

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — a lexical search
for a "potential" implementation matches `reconstructed_potential`**, which is
an effective potential in field space, not a gravitational potential. Counting
it would have inflated component readiness. §10.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the self-referential search
hazard, at its sharpest yet.** Six of `A4`'s eleven terms and three of `A5`'s
occur ONLY in this task's own committed specification and review, committed one
and two commits before the searches ran. **The `r_c ∝ V_max^{0.82}` relation
exists in exactly one file in the repository: the sentence asking whether it
exists.** **No governance mechanism addresses a search whose subject includes
the instruction to search.**

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — provenance cannot be settled
from this repository's own descriptions, and not merely because titles are weak
evidence.** `paper:206-208` and `paper:1815-1816` describe the same work as
"derived and tested" and as "Fits" respectively. §5.1, §17.2.

### 19.3 Clarifications, not defects

**The `A11` non-zero is a pattern artefact**, located at artifact line 228 —
"THE STRUCTURE OF THE RESULT IS THE POINT" matching the pattern `the result is`.
No physical quantity is stated. §12.

**Rule 13's two diagnostic orders were not exercised**, because no environment
failure occurred; I name neither as the one used, per §7 of the specification.

**`refs/heads/main` is a stale local ref at `1cb5550f`**, reported for contrast
as `A1` requires. This task's base is `refs/remotes/origin/main`, and `main` is
not touched at all. §2.

**The stop-hook's recurring "405 unpushed commits" claim on the session branch
is an artefact of the clone having been unshallowed**, and the session branch
has nothing unpublished. It was not pushed. §1.
