# Report — integrating and landing the clean-room Proca construction and flat validation

    branch      science/integrate-recon-01a
    base        f21198cd25ae285b789b706f7c4ac0730f9fff69   (authoritative main)
    source      be9ee961ca6231aee02987db3ab3c2a8c43bbc79   (science/recon-01a-construction)
    measured at commit 3, 11fb9397f4c83da419622bf873d2c24c720f788f
    landing     §6's fast-forward of refs/heads/main to commit 4 is POST-REPORT

**THIS IS THE FIRST LANDING IN THIS LINE THAT PUTS EXECUTABLE CODE ON `main`.**
**Nothing existing is modified: 474 of 474 base paths blob-identical.**

**THE CONSTRUCTION FREEZE VERIFIED AT NINE OBJECT IDS.** The three code files are
byte-identical at the source's `3a`, at its `3b`, and at this task's head. `§5`.

**THE ARRIVING VALIDATIONS WERE RE-DERIVED BY EXECUTION, NOT BY READING. Every
figure reproduces.** `§6`.

**`RECON-01b`'s BLOCKER, verified against the arriving code's own definitions:**
`K1 + m²G1 = G1(D1 + m²)`, so `det(K1 + m²G1) = det G1 · det(D1 + m²)`. **The
mixing did not leave the physics; it moved into `det G1`.** `§7`. **THIS TASK
DOES NOT SETTLE IT.**

> **Spectrum agreement does not imply operator correctness.**

**`§4(b)`'s comparison verdict: `NON-COMMENSURABLE — VALIDATION TARGET MISMATCH
DISCOVERED`.** Not `PASS`, not a scientific discrepancy. `§9`.

---

## 1. `A3` — environment conformance, run FIRST

**Rule 13's diagnostic order with Amendment D's step 0, run before any other
criterion. MEASURED, not assumed.**

    (0) execution location    /home/user/2-emergent-gravity — the primary
        (Amendment D)         worktree. git dir .git, common dir .git, so not a
                              linked worktree. HEAD branch
                              claude/paper-2-independent-verification-dysdp0,
                              resolved bfef924c368658cac85c04ed18d96eb4450afba6.
                              Twelve linked worktrees existed; this task's work
                              was done in a THIRTEENTH, cut fresh at
                              refs/remotes/origin/main.

    (1) interpreter           Python 3.11.15 at /usr/local/bin/python3

    (2) packages the ARRIVING CODE IMPORTS, and the declared set:
                              numpy   2.4.6     IMPORTED by proca_curved.py
                                                and flat_validation.py
                              pytest  9.1.1     runs the arriving test
                              ruff    0.15.8    declared
                              sympy   1.14.0    declared; NOT imported by any
                                                arriving file
                              scipy   ABSENT — ModuleNotFoundError
                              All four DECLARED packages present.

    (3) clone depth           NOT shallow. `--is-shallow-repository` returns
                              false and no `shallow` file exists in the common
                              git dir. 506 commits reachable from all refs,
                              423 from HEAD.

    (4) working tree          clean; `status --porcelain` empty before any work.

    (5) declaration compared  `docs/local/execution_environment.md` declares a
                              WINDOWS environment. See `§16.4`.

**NO RESTORATION WAS NEEDED AND NONE WAS PERFORMED. NOTHING WAS INSTALLED**, as
`A3` directs.

**Rule 13 carries TWO diagnostic orders, a known open item. No environment
failure occurred, so NEITHER order was exercised.**

### 1.1 The `scipy` finding, and a line-number correction that is mine

**`A3` asks me to report `pyproject.toml:11`'s `scipy>=1.11` declaration.
MEASURED: `scipy>=1.11` IS AT `pyproject.toml:12`, NOT `:11`.**

    pyproject.toml:10   dependencies = [
    pyproject.toml:11     "numpy>=1.26",
    pyproject.toml:12     "scipy>=1.11",
    pyproject.toml:13     "sympy>=1.12",
    pyproject.toml:14   ]

**THE WRONG LINE NUMBER IS MINE.** The `RECON-01a` report — which I wrote —
cited `pyproject.toml:11` for the `scipy` declaration in its `§1`, `§9.4` and
`§15.5`. **This specification took the citation from that report in good faith.**
`§16.2` records it.

**The substance is unaffected and confirmed:** `scipy` IS declared a project
dependency and IS NOT installed. **Nothing broke, because the arriving
construction imports `numpy` alone** — verified by reading the two `import`
blocks, not inferred: `proca_curved.py` imports `itertools` and `numpy`;
`flat_validation.py` imports `numpy` and the sibling module. **The full suite
passes at 332.**

**A future stage reaching for `scipy` on the strength of `pyproject.toml` would
fail at import.** Reported, not repaired — `pyproject.toml` is not writable here.

## 2. `A1` — repository, refs, source ancestry

**`origin` URL, MEASURED and reported VERBATIM, not normalised:**

    https://github.com/zetacheng/2-emergent-gravity

No `.git` suffix, no trailing slash. It identifies `zetacheng/2-emergent-gravity`.

**Refs, MEASURED after `git fetch origin main`:**

    refs/remotes/origin/main   f21198cd25ae285b789b706f7c4ac0730f9fff69
    expected by §4 A1          f21198cd25ae285b789b706f7c4ac0730f9fff69   MATCH

    refs/heads/main            1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**`refs/heads/main` LAGS and is reported for contrast.** It has lagged at
`1cb5550f…` throughout this session; **every measurement here is against
`refs/remotes/origin/main`**, which is also the landing authority `§6` names.

**Source, MEASURED:**

    science/recon-01a-construction   be9ee961ca6231aee02987db3ab3c2a8c43bbc79
    is-ancestor of origin/main       exit 1 — NOT AN ANCESTOR

**So the source is unmerged and this task is the merge.** The branch to create,
`science/integrate-recon-01a`, existed at neither the remote (0 hits) nor
locally (0 hits).

## 3. `A2` — the pre-execution review

**Field-present check run BEFORE the match check, in that order:**

    field name present     grep 'reviewed specification SHA-256' → line 4, ONE hit
    field filled in        yes — a 64-hex value, not a placeholder
    value in the review    8b40de145b6aa7d7fe2107a011dd930db24639ff2df8dec867dc9e1659ad587f
    sha256 of the spec     8b40de145b6aa7d7fe2107a011dd930db24639ff2df8dec867dc9e1659ad587f
                           MATCH

**Committed UNEDITED**: the committed blob's sha256 is
`02e2cf081f97c4668953fd16c2b258582678087faa8937c7da17d4b95504de22`, identical to
the uploaded bytes. **Verdict `APPROVE FOR EXECUTION`, twelve sections — eleven
`PASS` and one `PASS WITH RECORDED AMBIGUITY`, its `§7`, which is `§10`'s
subject.**

## 4. `A4`, `A5` — parentage and the merge

**`A4`, three separately derived measurements:**

    parent 1     git rev-parse HEAD^1   967873888742829da9a7bc15cf0373e1a6e266a6
                 this task's review commit (commit 2)                     MATCH
    parent 2     git rev-parse HEAD^2   be9ee961ca6231aee02987db3ab3c2a8c43bbc79
                 the source tip named in §0                               MATCH
    merge-base   git merge-base HEAD^1 HEAD^2
                 f21198cd25ae285b789b706f7c4ac0730f9fff69
                 the specification's evidence base                        MATCH

**Commit 1 is an ancestor of parent 1:** `--is-ancestor a7a32350… 96787388…`
returns **exit 0**.

**The checker's `P5` recomputed the same three values independently** and reports
`merge_base_equals_parent_1: false` — correct, since the base is `f21198cd…` and
parent 1 is commit 2 — with `compared_to_recorded: UNAVAILABLE`.

**`A5`, the conflict list:**

    git merge --no-ff --no-commit be9ee961…     exit 0
    "Automatic merge went well; stopped before committing as requested"

    conflict list, git diff --name-only --diff-filter=U     0 paths
    unmerged index entries, git ls-files -u                  0

**THE CONFLICT LIST IS EMPTY.** A `git merge-tree --write-tree` dry run
beforehand produced tree `6bf456e7363fe59368da6dc9339880ae5f23d936` with an empty
conflict section, agreeing with the real merge.

## 5. `A6` — the freeze verified at nine object ids

**MEASURED. Three files × three revisions.**

    scripts/recon2026/proca_curved.py
        source 3a  03f46905e5798fb7f6880dfae9ed5a1931be895b
        source 3b  03f46905e5798fb7f6880dfae9ed5a1931be895b
        this head  03f46905e5798fb7f6880dfae9ed5a1931be895b     IDENTICAL

    scripts/recon2026/flat_validation.py
        source 3a  6b21f9d6db67641ec7de31b7006884b617de3e8c
        source 3b  6b21f9d6db67641ec7de31b7006884b617de3e8c
        this head  6b21f9d6db67641ec7de31b7006884b617de3e8c     IDENTICAL

    tests/test_recon2026_flat_limit.py
        source 3a  1d7ba5672614dedcd3b78483b5d43431af65fc7a
        source 3b  1d7ba5672614dedcd3b78483b5d43431af65fc7a
        this head  1d7ba5672614dedcd3b78483b5d43431af65fc7a     IDENTICAL

**ALL THREE SETS IDENTICAL.**

**WHY THIS IS THE WHOLE ENFORCEMENT MECHANISM.** The source built and measured at
`3a` knowing only the analytic flat requirement, then read `CIRC-01`'s
quantitative figure, then wrote its artifact at `3b`. **The reveal happened
BETWEEN two commits whose code trees are byte-identical.** So the quantitative
target demonstrably did not reach the construction — **not because the executor
says so, but because the object ids say so.** **A landing that did not check this
would leave the isolation claim resting on prose**, and the source executor
disclosed that it already knew the withheld values from earlier tasks, which is
exactly why prose could not carry it.

## 6. `A7` — the validations RE-DERIVED BY EXECUTION at the merged head

**`python3 -m scripts.recon2026.flat_validation` run at commit 3. Exit 0, stderr
empty. This is the first integration in this line that can re-derive a source
result by RUNNING it, and I ran it.**

    (a) FLAT 1-FORM SPECTRUM
        relative asymmetry at h = 0        0.0
        max abs deviation                  7.460699e-14      source: 7.46e-14
        flat-band multiplicity             259 / required 259
        logdet, full operator              1206.5450159412
        logdet, momentum blocks            1206.5450159412
        logdet absolute difference         1.136868e-12      source: 1.14e-12

    (c) COMPENSATING SCALAR
        max abs deviation                  2.842171e-14      source: 2.84e-14
        min / max eigenvalue               0.249999999999994 / 16.250000000000018
        spread                            16.000000000000025
        distinct eigenvalues               9
        is_ultralocal                      False

    (d) EXTENTS AND MASSES
        L=4 m²=0.25   vec 7.461e-14   logdet 1.137e-12   band  259/259
        L=4 m²=1.00   vec 7.816e-14   logdet 2.501e-12   band  259/259
        L=6 m²=0.25   vec 1.474e-13   logdet 2.728e-11   band 1299/1299
        L=6 m²=1.00   vec 1.510e-13   logdet 2.910e-11   band 1299/1299
        scalar not ultralocal in all four rows

    (e) MASS DERIVATIVE vs CLOSED FORM  36.45856448712421
        step 0.04   err 4.9246e-03
        step 0.02   err 1.2281e-03    ratio 4.010
        step 0.01   err 3.0682e-04    ratio 4.003
        Richardson  err 2.5719e-07

    (e) BACKGROUND DERIVATIVE, symmetry-enforced zero
        baseline logdet                  1412.4669172372
        first derivative, three steps    -3.979e-11, +4.547e-11, -4.547e-11
        largest magnitude                 4.547e-11  =  3.22e-14 of baseline
        second derivative                454.12222740 / 454.04455675 / 454.02514492
        Richardson second                454.01867430882703

**EVERY FIGURE REPRODUCES THE SOURCE'S. NOT ONE DIFFERS.** The convergence ratios
`4.010` and `4.003` confirm the second-order stencil independently; the first
derivative's **sign alternates while its magnitude does not fall**, which is the
signature of a quantity that is zero up to round-off rather than merely small.

**`A7` said to treat any difference as a finding. There is no difference to
report** — and that is a stronger statement than the source could make, because
the source measured its own code and I measured the same code after a merge, in a
different worktree, from a different commit.

## 7. `A8` — the determinant relation, checked against the arriving code's definitions

**The arriving `proca_curved.vector_operator` defines
`D1 + m² = G1⁻¹K1 + m²·1`. From that definition alone:**

    G1 (D1 + m²) = G1 G1⁻¹ K1 + m² G1 = K1 + m² G1        one line, an identity
    det(K1 + m² G1) = det(G1) · det(D1 + m²)               multiplicativity

**VERIFIED NUMERICALLY against the code's own `return_parts` output:**

    amplitude 0.00
      ||(K1+m²G1) − G1(D1+m²)|| / ||K1+m²G1||     0.000e+00
      logdet(K1+m²G1)                             1206.5450159412
      logdet(G1) + logdet(D1+m²)                  1206.5450159412
      difference                                  0.000e+00
      logdet(G1) alone                            0.0000000000

    amplitude 0.08
      ||(K1+m²G1) − G1(D1+m²)|| / ||K1+m²G1||     6.434e-17
      logdet(K1+m²G1)                             1206.9113171468
      logdet(G1) + logdet(D1+m²)                  1206.9113171468
      difference                                  6.821e-13
      logdet(G1) alone                            −1.1338458300

**THE TWO MIXING FIGURES AND THEIR POWERS, re-run:**

    ||Pi_T X Pi_L||_F / ||X||_F        operator D1+m²      Hessian K1+m²G1
      amplitude 0.00                     3.0721e-16          3.0721e-16
      amplitude 0.02                     3.2752e-16          1.7467e-04
      amplitude 0.04                     3.2335e-16          3.4933e-04
      amplitude 0.08                     3.2533e-16          6.9864e-04
      leading power in amplitude           −0.004837            0.999960

**`logdet(G1)` IS EXACTLY ZERO AT `h = 0` AND `−1.1338458300` AT AMPLITUDE
`0.08`. That number is the mixing's new address.** The two determinants are not
equal on a curved background, they differ by precisely that factor, and **only
the Hessian form mixes the transverse and longitudinal bands.**

**THIS IS `RECON-01b`'s BLOCKER AND THIS TASK DOES NOT SETTLE IT.** `RECON-01b`
cannot begin a determinant-power scan until it is decided which of the two
determinants the effective action requires, **because a scan run before the
choice is made could return a clean-looking result from the wrong determinant** —
and the result would look clean precisely because choice C5 removes the mixing
from the object being scanned.

**Nothing here converts the algebraic identity into a physics ruling.** The
identity is arithmetic; which determinant belongs in the reconstruction is a
question about measures and Jacobians that a separate adjudication must answer.

## 8. `A9` — spectrum agreement does not imply operator correctness

**THE TWO KERNEL FORMS:**

    the source's first version    phat2 δ_{μν} − conj(s_μ) s_ν
    the correct form              phat2 δ_{μν} − s_μ conj(s_ν)

**THEIR EIGENVALUES ARE IDENTICAL.** Both are Hermitian, and they are complex
conjugates of one another, so their spectra coincide exactly. **They differ only
in the null direction — `conj(s)` versus `s` — so the transverse and longitudinal
subspaces were interchanged.**

**WHICH VALIDATIONS PASSED WITH THE ERROR PRESENT:**

    (a) the flat spectrum comparison            PASSED at 2e-13
        the logdet / momentum-block cross-check  PASSED
    (c) the compensating scalar check            PASSED
    (d) the extent and mass scan                 PASSED

**WHICH ONE CAUGHT IT:**

    (b) the transverse/longitudinal separation   CAUGHT IT — relative mixing
                                                 0.238 where machine zero was
                                                 required

**Three of four spectrum- and determinant-level validations passed a wrong
operator.** The source diagnosed it analytically — expanding
`Σ_{μ<ν}|F̃_{μν}|²` fixes the conjugation order — and fixed it before the freeze.

> **SPECTRUM AGREEMENT DOES NOT IMPLY OPERATOR CORRECTNESS.**

**`RECON-01b` AND EVERYTHING AFTER MUST RETAIN A PROJECTOR- OR
SUBSPACE-SENSITIVE TEST. THAT IS NOT OPTIONAL QUALITY ASSURANCE.** Eigenvalues,
determinants and traces are all invariant under the substitution that was wrong
here; only something that looks at eigenvectors can see it. **The arriving
`tests/test_recon2026_flat_limit.py` contains two such tests, and they land with
the code.**

## 9. `A10` — the `§4(b)` verdict

**`NON-COMMENSURABLE — VALIDATION TARGET MISMATCH DISCOVERED`.**

**Not `PASS`. Not a scientific discrepancy.**

**The specification asked for two numbers and a comparison. The source reported
both numbers and declined the comparison**, because its quantity is a
single-momentum operator-level mixing and `CIRC-01`'s is a two-momentum bubble
coefficient at order `q²`.

**`CIRC-01` ITSELF WITHDREW THE SINGLE-MOMENTUM MEASUREMENT. Quoted with
lines:**

    derivations/P2-BETAV-CIRC-01_determinant-decomposition.md:26-29
      The relevant test is **not** whether the one-graviton vertex off-block norm
      vanishes as `q→0`. `Z` is the `q²` coefficient of the induced kernel; a vertex
      mixing `U_TL(q)=O(q)` still yields a **finite** mixed bubble
      `U_TL·U_LT=O(q²)` — a leading-order contribution to `Z`. So the adjudication is

    derivations/P2-BETAV-CIRC-01_determinant-decomposition.md:50-52
      - The one-graviton vertex mixing `U_TL` **vanishes as `q→0`** (the earlier
        vertex-norm figure was measured in the wrong, single-momentum basis and is
        withdrawn).

**CONFIRMED: THE SOURCE'S QUANTITY FALLS IN THE WITHDRAWN CLASS.** Its `§4(b)`
measures `||Π_T X Π_L||` in the flat projector basis at a single momentum — a
one-graviton vertex off-block norm. `CIRC-01:26` names that as *not* the relevant
test, and `:51` describes the earlier measurement of it as *"measured in the
wrong, single-momentum basis"*.

**THE SPECIFICATION DEFECT WAS THE RESEARCHER'S.** `RECON-01a`'s `§4(b)` asked
for a comparison between two quantities on the assumption they were comparable.
**They are not, and `CIRC-01` had already said so in the document `§4(b)` pointed
at.** The source executor was right to refuse the comparison rather than report a
ratio of incommensurable numbers as agreement or disagreement.

**A CURVED-BACKGROUND VALIDATION WILL NEED A CHECK IN `CIRC-01`'s OWN
TWO-MOMENTUM BASIS** — projectors built independently at `k` and `k+q`, decomposed
at the bubble level. **Building one is not this task's**, and `§15.1` records it
as what the next validation stage owes.

## 10. `A11` — the two scans, uncollapsed

**Both are reported. Neither is collapsed into the other, and `A9` of the source
specification is NOT claimed to have fully passed.**

    SEMANTIC anchor-information scan, 17 patterns
      scripts/recon2026/proca_curved.py        hits 0
      scripts/recon2026/flat_validation.py     hits 0
      tests/test_recon2026_flat_limit.py       hits 0
      TOTAL in the three code files            0

    BROAD literal scan, 18 patterns (the 17 plus a bare word-boundary token)
      scripts/recon2026/proca_curved.py        hits 0
      scripts/recon2026/flat_validation.py     hits 0
      tests/test_recon2026_flat_limit.py       hits 2
      TOTAL in the three code files            2

**THE TWO HITS, LOCATED:** both in the module docstring of
`tests/test_recon2026_flat_limit.py`, at its lines 1 and 4, and both are the
phrase `regression anchor` — **`GATES.md`'s own field name, and the wording the
`RECON-01a` specification's `§3` instructed for that very file.**

**A FIELD NAME CARRIES NO VALUE.** No ratio, no sign, no determinant power, no
number.

**THE `RECON-01a` SPECIFICATION USED THE WORD `anchor` FOR TWO DIFFERENT THINGS —
the withheld numerical target, and the gate's `Regression anchors` field — and
made any literal hit a `STOP`. That is the Researcher's defect**, and `§15.5`
carries it as a Rule 16 junction.

**THE FROZEN CODE WAS NOT EDITED TO MAKE A CHECKER GREEN.** It could not have
been: `§5` of the source froze it at `3a` and `§8` here forbids touching it. **The
three blobs are identical at nine measured object ids** (`§5`). **So the literal
condition remains unsatisfied and the semantic one is clean, and I report both
states rather than choosing the flattering one.**

## 11. `A12`, `A13` — nothing existing changed, and the gate is untouched

    paths at the evidence base   474
    paths at the head            483
    COMPARED                     474
    IDENTICAL                    474
    DIFFERING                      0
    missing at the head            0
    new at the head                9   — exactly A15's cumulative count at commit 3

**Named confirmations, each a blob comparison:**

    GATES.md                                1 path    unchanged
    CONVENTIONS.md                          1 path    unchanged
    derivations/P2-BETAV-*                  6 paths   all unchanged
    P2-LATTICE-MICROSPEC-01 artifacts       7 paths   all unchanged
    registers                               2 paths   both unchanged
    scripts/recovered_2026/                24 paths   ALL UNCHANGED
    results/                               69 paths   all unchanged

**`derivations/P2-BETAV-*` RE-MEASURED AT THE EVIDENCE BASE: SIX, and the
specification states six.** Named:
`ASSEMBLY-01_bookkeeping_regression`, `CAMPAIGN_prereg`,
`CIRC-01_determinant-decomposition`, `RECON-01_cleanroom_reconstruction`,
`RECON-01_scope-assessment`, `SIGN-01_anchor-reconciliation`.

**THIS IS THE FIRST SPECIFICATION IN FOUR TO CARRY THIS COUNT CORRECTLY.** The
`SIGN-01` specification said four, its integration said five, the `RECON-01a`
specification said five. **All three were one behind for the same reason; this
one is right, and the reason it is right is that the previous report reported the
drift.** It will be seven for the next task in the line.

**`GATES.md` IN PARTICULAR — the `Regression anchors` field, read by explicit
line range:**

    GATES.md:753   ### Regression anchors
    GATES.md:754   None yet (proposed).

**IT STILL READS `None yet (proposed)`.** **The arriving test was NOT registered
as the gate's anchor, and `GATES.md` is blob-identical to the base.**

**`A13`, all four invariants, each read SCOPED:**

    ^## P2- section count                    14        expected 14   MATCH
    P2-PHASE-01, GATES.md:971-1108
      :973    Status: PROPOSED                                       MATCH
    both prerequisites SATISFIED
      :1011   Artifact state: **ADOPTED**. Prerequisite state: **SATISFIED**,
      :1036   Artifact state: **ADOPTED**. Prerequisite state: **SATISFIED**.
    both pins recomputed
      :1017   4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214   identical
      :1040   e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3   identical

**THE THREE `BETAV` STATUSES, scoped:**

    P2-BETAV-RECON-01   GATES.md:725-789   :727  Status: PROPOSED (not run;
                        distinct from the historical circularity question)
    P2-BETAV-CIRC-01    GATES.md:328-597   :330  Status: RUN
    P2-BETAV-01         GATES.md:207-264   :209  Status: PROPOSED (deferred —
                        not computed this sweep)

**NONE CHANGED. LANDING EXECUTABLE CODE DOES NOT ADVANCE A GATE**, and the
strongest evidence is that `GATES.md` is blob-identical.

## 12. `A14` — superseded branches not merged

**Six separate `--is-ancestor` invocations, six exit statuses. BEFORE the
advance:**

    against refs/remotes/origin/main        against commit 3
    52f65117   exit 1                      exit 1
    ebd531ab   exit 1                      exit 1
    40168469   exit 1                      exit 1
    7146a093   exit 1                      exit 1
    10c260b9   exit 1                      exit 1
    d64cd912   exit 1                      exit 1

**None is an ancestor of `main`, and the merge did not introduce any of them.**
The checker's `P4` independently recomputed all six with
`is_ancestor_of_head: false` and `object_present: true`.

**AFTER the advance is POST-REPORT EVIDENCE**, required by `§5` and returned to
the Reviewer. **The landing is a fast-forward to commit 4 whose only parent is
commit 3, so no superseded commit can become an ancestor by it — but that is an
argument and the criterion asks for six measurements.**

## 13. `A15` — the four cumulative figures, and what each was measured at

**ALL FOUR MEASURED. The expectation was 1, 2, 9, 10.**

    at commit 1   a7a32350   base → head    1 addition, 0 modifications   MEASURED
    at commit 2   96787388   base → head    2 additions, 0 modifications  MEASURED
    at commit 3   11fb9397   base → head    9 additions, 0 modifications  MEASURED
    at commit 4   INTENDED   base → head   10 additions, 0 modifications  NOT MEASURED HERE

**THE SOURCE'S OWN CONTRIBUTION, MEASURED SEPARATELY as the merge's staged diff
against parent 1 — not inferred from the cumulative count:**

    A  derivations/P2-BETAV-RECON-01a_construction-and-flat-validation.md
    A  reports/2026-08-17T1653Z_recon-01a-construction.md
    A  reviews/chatgpt/2026-08-17T1653Z_recon-01a-construction.md
    A  scripts/recon2026/flat_validation.py
    A  scripts/recon2026/proca_curved.py
    A  specs/2026-08-17T1653Z_recon-01a-construction.md
    A  tests/test_recon2026_flat_limit.py

    arriving PATH count       7
    arriving ADDITION count   7
    do they coincide?         YES, at seven

**They coincide because the source added seven paths and modified none.** Stating
them separately still matters: **a source that had modified an existing file would
have made the path count exceed the addition count**, and a single figure would
have hidden the modification.

**`9` IS NOT THE MERGE'S CONTRIBUTION.** It is the cumulative base-to-head count
AT the merge commit, and it already contains this task's own first two commits:
`7 arriving + 2 already committed = 9`. **The merge itself brings 7.** The final
figure is `7 + 3 = 10`, not `9 + 3 = 12`. **The reviewer's earlier 12 came from
reading the 9 as the merge's contribution; the four measured figures above make
the distinction unambiguous, because 1 and 2 are visible before the merge exists.**

**`modify:` is `[]` and remained `[]`. Zero non-addition status entries in the
range** — no modification, deletion, rename, copy, type change, unmerged or
unknown entry anywhere.

**`append_only: DECISION_LOG.md` is a CHECKER-CONFIGURATION DECLARATION, NOT AN
AUTHORISATION TO WRITE THAT FILE.** It was not written; `P3` confirms
`base_is_byte_prefix_of_head: true` with zero deleted lines.

**The `{HHMM}Z` token.** UTC measured before writing anything:
`2026-08-17T22:03:17Z`, giving `2203Z`. **Commit 1's recorded time is
`2026-08-17 22:03:35 +0000`** — 18 seconds later, the same minute. All three
authored paths carry `2203Z`.

## 14. `A16`, `A17`, `A18`, `A19`

### 14.1 `A16` — which merge case, stated BEFORE the blob comparisons

**THE MERGE-BASE IS THE EVIDENCE BASE, so no commit on `main` could have touched
an arriving path.**

    merge-base(parent 1, parent 2)          f21198cd25ae285b789b706f7c4ac0730f9fff69
    evidence base                           f21198cd25ae285b789b706f7c4ac0730f9fff69
    identical                               YES
    commits on origin/main after the base   0

**`main` has not moved since the base, so the merge cannot be the case where an
arriving path was independently edited on `main` and silently resolved.** That is
excluded by the ref topology before any blob is compared; **the comparisons below
are confirmations, not the argument.**

**THEN the seven blob comparisons. All seven ABSENT at the base and
SOURCE == HEAD:**

    derivations/P2-BETAV-RECON-01a_construction-and-flat-validation.md  142ceb46a84b5d98e4b813c56128fca95ab52f49
    reports/2026-08-17T1653Z_recon-01a-construction.md                  88e2225655ceab311be80954c719f9cc746b23a9
    reviews/chatgpt/2026-08-17T1653Z_recon-01a-construction.md          371a7de5f0f539b8eb5b2dc4832d397bb1bc067b
    scripts/recon2026/flat_validation.py                                6b21f9d6db67641ec7de31b7006884b617de3e8c
    scripts/recon2026/proca_curved.py                                   03f46905e5798fb7f6880dfae9ed5a1931be895b
    specs/2026-08-17T1653Z_recon-01a-construction.md                    24d66aba207e37e474ebefbc00ea03fdbddacb8b
    tests/test_recon2026_flat_limit.py                                  1d7ba5672614dedcd3b78483b5d43431af65fc7a

**Everything arriving by merge is integrated exactly as reviewed; no arriving path
was renamed.** The three code blobs match `§5`'s frozen ids.

### 14.2 `A17` — the checker, MEASURED at commit 3

    base   f21198cd25ae285b789b706f7c4ac0730f9fff69
    head   11fb9397f4c83da419622bf873d2c24c720f788f   (commit 3)

    run 1 INCLUSIVE   exit 0   PASS   332 lines   sha256 6bca6af92d0cc0013a9cd479008911387f936108e9351118b2e0de3682a9892c
    run 1 EXCLUSIVE   exit 0   PASS   332 lines   sha256 7b6ee5a3a9a35848f200491466ae81b64f7db3519087a19138b9b03ad565b75d
    run 2 INCLUSIVE   exit 0   PASS   306 lines   sha256 3cb87057ab3a0c74a9b1b461adbf21c965edac0be480c1d18df803eae6937e7f
    run 2 EXCLUSIVE   exit 0   PASS   306 lines   sha256 5c4bd776e1ce0d3f72325931f7413237832905480cec7c6c2c41b6fbfe1094ef

    stderr empty in all four.

    P1 PASS  P2 PASS  P3 PASS  P4 PASS  P5 PASS
    P6 PASS  P7 PASS  P8 PASS  P9 PASS

    overall PASS in all four.
    commits_in_range 8      commits_on_first_parent_line 3

**All nine properties `PASS` and NONE is `NOT_APPLICABLE`.**

**PARSED, NOT GREPPED, and here is the difference.** A JSON walker over every
`status` and `overall` field returns **27 × `PASS` and nothing else — zero
`NON_GREEN` statuses, zero `DECLARATION_CONFLICT`.** A token grep of the same
bytes returns, in every one of the four outputs, `NOT_DECLARED` 1 and
`NOT_PARSEABLE` 2 — **both `NON_GREEN` members, both occurring only in
definitional prose (the `overall_note` and `P1`'s `does_not_establish`).**

**WHAT `RUN 1` DID — two specifications in range, differing totals, no
conflict:**

    specs/2026-08-17T1653Z_recon-01a-construction.md
        stated: 7 additions, 0 modifications    counted 7 / 0    parse OK
        counted_set holds the literal {HHMM}Z placeholders for its three
        governance paths, and the three CODE paths literally
    specs/2026-08-17T2203Z_integrate-recon-01a.md
        stated: 10 additions, 0 modifications   counted 10 / 0   parse OK

**`RUN 1` and `RUN 2` are NOT byte-identical — 332 lines against 306 — differing
in exactly three places** verified by `diff`: `P1`'s extra evidence entry and the
`specification_paths_read` list in `P3` and `P7`. **`RUN 2` names the subject and
is stop-governing; `RUN 1` discovers it and governs nothing.**

**THE `C3` RESIDUAL: two specifications with DIFFERING stated totals — 7/0 and
10/0 — and NO `DECLARATION_CONFLICT`**, because `_declarations_from_specs`
compares `append_only_paths` and `authorised_modified_gates`, identical in both,
while `P1` checks each specification against its own manifest. **Third
independent range to show it. Unchanged and still unregistered.**

    P3   PASS   declared_source: specification   declared ['DECISION_LOG.md']
    P7   PASS   declared_source: specification   sections base 14 head 14 raw 14
    P5   PASS   merge 11fb9397…, parents 96787388… and be9ee961…,
                merge-base f21198cd…, merge_base_equals_parent_1 false
    P9   PASS   heading_present: true for
                reports/2026-08-17T1653Z_recon-01a-construction.md

**`P7` REPORTS FOURTEEN SECTIONS. `PASS` AT ZERO WOULD HAVE BEEN A STOP.**

**`P9` is already `PASS` at commit 3, and not because of this report** — the merge
brings the source's report into range and it carries the mandated heading.

**`RUN 1` config, verbatim — observational, governs nothing:**

    {
      "base": "f21198cd25ae285b789b706f7c4ac0730f9fff69",
      "head": "11fb9397f4c83da419622bf873d2c24c720f788f",
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
      "base": "f21198cd25ae285b789b706f7c4ac0730f9fff69",
      "head": "11fb9397f4c83da419622bf873d2c24c720f788f",
      "specification_paths": [
        "specs/2026-08-17T2203Z_integrate-recon-01a.md"
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

Each `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

**No value in either config is one I chose**, and **neither the config nor this
specification's declarations were adjusted to make `RUN 2` pass. `RUN 2` passed
on its first invocation at both readings.**

**`RUN 2`'s output, verbatim, `INCLUSIVE` reading:**

    {
      "base": "f21198cd25ae285b789b706f7c4ac0730f9fff69",
      "commits_in_range": 8,
      "commits_on_first_parent_line": 3,
      "head": "11fb9397f4c83da419622bf873d2c24c720f788f",
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
              "counted": 10,
              "counted_add": 10,
              "counted_modify": 0,
              "counted_set": [
                "derivations/P2-BETAV-RECON-01a_construction-and-flat-validation.md",
                "reports/2026-08-17T1653Z_recon-01a-construction.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-recon-01a.md",
                "reviews/chatgpt/2026-08-17T1653Z_recon-01a-construction.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-recon-01a.md",
                "scripts/recon2026/flat_validation.py",
                "scripts/recon2026/proca_curved.py",
                "specs/2026-08-17T1653Z_recon-01a-construction.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-recon-01a.md",
                "tests/test_recon2026_flat_limit.py"
              ],
              "parse": "OK",
              "path": "specs/2026-08-17T2203Z_integrate-recon-01a.md",
              "stated": 10,
              "stated_add": 10,
              "stated_modify": 0,
              "stated_record": "stated: 10 additions, 0 modifications"
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
                "commit": "a7a323500569c7440a62fb47fc2855f34d410c91",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "967873888742829da9a7bc15cf0373e1a6e266a6",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "11fb9397f4c83da419622bf873d2c24c720f788f",
                "work_paths": [
                  "derivations/P2-BETAV-RECON-01a_construction-and-flat-validation.md",
                  "scripts/recon2026/flat_validation.py",
                  "scripts/recon2026/proca_curved.py",
                  "tests/test_recon2026_flat_limit.py"
                ]
              }
            ],
            "first_review_commit": "967873888742829da9a7bc15cf0373e1a6e266a6",
            "first_work_commit": "11fb9397f4c83da419622bf873d2c24c720f788f",
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
              "specs/2026-08-17T2203Z_integrate-recon-01a.md"
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
          "evidence": [
            {
              "compared_to_recorded": "UNAVAILABLE",
              "merge": "11fb9397f4c83da419622bf873d2c24c720f788f",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "f21198cd25ae285b789b706f7c4ac0730f9fff69",
              "recomputed_parent_1": "967873888742829da9a7bc15cf0373e1a6e266a6",
              "recomputed_parent_2": "be9ee961ca6231aee02987db3ab3c2a8c43bbc79",
              "status": "PASS"
            }
          ],
          "id": "P5",
          "status": "PASS",
          "title": "merge parentage against recomputed facts"
        },
        {
          "classification": "PARTIAL",
          "does_not_establish": "Does not establish absence of 'session identifier' or 'tool attribution', which no repository document defines; only Co-Authored-By trailers and URLs are matched, and the author and committer identity fields are not message content and are out of scope.",
          "evidence": [
            {
              "commit": "a7a323500569c7440a62fb47fc2855f34d410c91",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "967873888742829da9a7bc15cf0373e1a6e266a6",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "4bddd1162b27ec6ec6012f8680492ca81641d4b5",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "d183d36dfaf808d58be66f77293ef71e22f38196",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "1a9c4af369baffd189c34caf521a7fe349427fb7",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "611292b5c6b9deb55a852852f531ae9badcb75c7",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "be9ee961ca6231aee02987db3ab3c2a8c43bbc79",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "11fb9397f4c83da419622bf873d2c24c720f788f",
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
              "specs/2026-08-17T2203Z_integrate-recon-01a.md"
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
            "first_commit": "a7a323500569c7440a62fb47fc2855f34d410c91",
            "first_commit_paths": [
              "specs/2026-08-17T2203Z_integrate-recon-01a.md"
            ],
            "reports_added": [
              "reports/2026-08-17T1653Z_recon-01a-construction.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-17T2203Z_integrate-recon-01a.md",
              "reviews/chatgpt/2026-08-17T1653Z_recon-01a-construction.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-17T2203Z_integrate-recon-01a.md",
              "specs/2026-08-17T1653Z_recon-01a-construction.md"
            ]
          },
          "id": "P8",
          "status": "PASS",
          "title": "Rule 15 placement and specification-first"
        },
        {
          "classification": "MECHANICAL",
          "evidence": [
            {
              "heading_present": true,
              "path": "reports/2026-08-17T1653Z_recon-01a-construction.md",
              "status": "PASS"
            }
          ],
          "id": "P9",
          "status": "PASS",
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

**The `EXCLUSIVE` reading differs at line 302 of 306, `"inclusivity"` only.**
`commits_out_of_scope` is empty and `commits_in_scope` is 8 in all four.

### 14.3 `A18`, `A19`

**`A18`, MEASURED at commit 3, exit status 0:**

    332 passed, 2 deselected      in 54.93 s

**Expected 332 and 2; measured 332 and 2.** **324 at the base plus the eight
arriving tests. No other change**, so the arriving code neither broke nor altered
any pre-existing validator.

**`A19`, MEASURED on commits 1–3. Commit 4 is post-report evidence:**

    commit 1   a7a32350   spec: integrate and land the clean-room Proca construction
    commit 2   96787388   review: pre-execution review for the construction integration
    commit 3   11fb9397   merge: integrate the clean-room Proca construction and flat validation

**All three: empty body, trailer hits 0, author date equal to commit date, not
amended.** A scan for `Co-Authored-By`, `claude.ai/code`, `Generated with`,
`Claude-Session` and `noreply@anthropic` over the range returns **ZERO**, and
`P6` independently reports `matches: []` for all EIGHT commits in range — the
three authored here and the five arriving.

**Rule 20 binds this task and was NOT exercised.** No message needed repair.
**No force-push, no branch deletion, no history rewrite, no squash, no rebase.
Commit 3 is a real merge with two parents, `--no-ff`.**

**Commit 4's message, INTENDED:**

    report: executable code lands, and the determinant question blocks the next stage

## 15. `§7` — Rule 16 assessment, five junctions

### 15.1 First — a validated flat limit does not validate the curved construction

**`h = 0` SWITCHES OFF THE METRIC COUPLING — the one thing the reconstruction
exists to exercise.** `§6`'s validations `(a)`, `(c)`, `(d)` and the mass
derivative are all flat-background statements. The curved content is `§7`'s
mixing measurement and the symmetry-enforced zero, **and both are structural or
symmetry checks rather than comparisons against a known curved answer.**

**WHAT A CURVED-BACKGROUND VALIDATION WOULD REQUIRE AND THIS STAGE DOES NOT
PROVIDE:** an independently known curved quantity — a continuum Seeley–DeWitt
coefficient extracted from this operator and checked against its analytic value,
or a second independent discretisation of the same continuum action agreeing in
the small-`h` limit.

**AND `CIRC-01`'s TWO-MOMENTUM BASIS IS WHERE SUCH A CHECK WOULD HAVE TO LIVE.**
`§9` establishes that the single-momentum measure is the withdrawn one; a
curved-background validation of the transverse/longitudinal structure must be
built at the bubble level with projectors constructed independently at `k` and
`k+q`. **Nothing in this landing does that, and `§9`'s verdict is precisely the
discovery that the earlier target was the wrong observable.**

### 15.2 Second — `C5` relocated the mixing, and that is a blocker the construction discovered

**`§7` measures it: the mixing moved into `det G1`, which is exactly zero at
`h = 0` and `−1.1338458300` at amplitude `0.08`.**

**`RECON-01b` CANNOT BEGIN UNTIL THE DETERMINANT QUESTION IS SETTLED, and a
`k`-scan run before it could return a clean-looking result from the wrong
determinant** — clean-looking *because* C5 removes the mixing from the object
scanned. **The failure mode is a plausible number, not an error.**

**THIS IS A BLOCKER DISCOVERED BY THE CONSTRUCTION, WHICH IS WHAT A CLEAN-ROOM
BUILD IS FOR.** It is not in `GATES.md`'s `Scope`, not in `RECON-B0`'s
ten-component inventory, and not in `CIRC-01`. **It became visible only when
somebody wrote the operator down twice — once as an action's Hessian and once as
an operator with a unit mass term — and measured both.** A build that only
produced numbers would have produced one and never seen the question.

**THIS TASK DOES NOT SETTLE IT** (`§7`), and settling it is a separate
adjudication.

### 15.3 Third — spectrum agreement does not imply operator correctness

**A WRONG KERNEL PASSED THREE OF THE FOUR VALIDATIONS**, and the fourth caught
it. `§8` names which. **The substitution that was wrong is invisible to every
eigenvalue, every determinant and every trace.**

**EVERY LATER STAGE MUST RETAIN A SUBSPACE-SENSITIVE TEST.** The two such tests
in the arriving suite land with the code.

**AND IT WAS FOUND BY A VALIDATION, NOT BY THE CONSTRUCTION'S PROVENANCE.** The
construction was clean-room throughout — the source opened none of the 24 files
under `scripts/recovered_2026/` — **and it was still wrong.** Clean-room
guarantees independence of derivation, not correctness of result, and this is the
concrete demonstration.

### 15.4 Fourth — six conventions were fixed by the construction

**SIX, and they are the construction's decisions, not repository facts.**
Forward differences; site-centred geometric factors; periodic boundaries; the
exact matrix inverse rather than a weak-field truncation; the operator defined by
dividing the Hessian by the mass metric; and the single-cosine background.
**`CONVENTIONS.md` supplies only its `:12` and `:24`.**

**A LATER READER MUST BE ABLE TO TELL THE TWO APART**, and the arriving artifact
lists all six explicitly as choices. **If `RECON-01b` returns a wrong number,
that list is where the search starts, and the source names C5 as the entry to try
first** — because `§7` shows C5 changes what object is under study, rather than
how accurately it is represented.

**A seventh item belongs on the same list without being a convention:** the
target document's momentum symbol was ambiguous between two functions
`CONVENTIONS.md:24` defines, and the construction's difference stencil resolved
it. **A construction resolving it the other way would disagree with the same
quoted line.**

### 15.5 Fifth — `A9`'s literal condition fired on the specification's own instructed wording

**THE CHECKER IS NOT GREEN UNDER A LITERAL READING, AND THE CODE WAS NOT EDITED
TO MAKE IT SO. BOTH ARE TRUE AND BOTH ARE REPORTED** (`§10`).

**THE AMBIGUITY IS THE SPECIFICATION'S.** `RECON-01a` used `anchor` for the
withheld numerical target in its `§2` and for `GATES.md`'s `Regression anchors`
field in its `§3` and `A11`, then made any literal hit a `STOP`. **One word, two
referents, one stop condition.**

**What the two scans establish jointly, and neither alone:** the semantic scan's
zero says no anchor INFORMATION reached the construction; the literal scan's two
say the deliverable is described by the name the specification told it to use.
**Collapsing them either way would lose one of those facts** — reporting only the
zero would overclaim, and reporting only the two would suggest contamination that
`§5`'s freeze and `§10`'s located hits both refute.

## 16. Stops and clarifications

**No stop was declared. Five primary categories, one primary per finding,
secondary findings separate, included even where there were none.**

### 16.1 `SPECIFICATION_DEFECT` — the withdrawn validation target

**`RECON-01a`'s `§4(b)` asked for a comparison between two non-commensurable
quantities, and `CIRC-01` had already withdrawn the single-momentum measurement
in the document `§4(b)` pointed at.** Verdict recorded as
`NON-COMMENSURABLE — VALIDATION TARGET MISMATCH DISCOVERED` (`§9`). **The defect
is the Researcher's; the source executor's refusal to report a comparison was
correct.** Not a stop: the criterion asked for two numbers and both were
delivered.

### 16.2 `OBSERVATION_METHOD_ERROR` — a citation error of mine, propagated into this specification

**`A3` asks me to report `pyproject.toml:11`'s `scipy>=1.11` declaration.
`scipy>=1.11` is at `:12`; `:11` is `"numpy>=1.26"`.** Measured in `§1.1`.

**THE WRONG LINE NUMBER IS MINE.** The `RECON-01a` report cited `:11` in three
places, and this specification took it from there. **I checked the substance and
not the line number when writing it** — the substance is right, and the citation
is off by one.

**The correction is available here only because `A3` required the line read
again.** A criterion that had asked me to confirm the claim rather than re-read
the line would have propagated it a third time. **`§16.5` records what that
implies for the `P2-BETAV-*` count, which broke the same way three times and was
fixed the same way.**

**No stop:** the operative finding — declared and absent, nothing broken — holds.

### 16.3 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — first: the determinant/measure question

**`det(K1 + m²G1) = det G1 · det(D1 + m²)`, and which side the reconstruction
needs is unsettled.** `§7` and `§15.2`. **Landing the identity is not settling the
question, and this task did neither more nor less than land it.** It is the
RECON line's active blocker.

### 16.4 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — second: the environment and `scipy`

**`docs/local/execution_environment.md` declares a WINDOWS environment with a
Python 3.12 interpreter. Every measurement here was on Linux with Python 3.11.15
— an UNDECLARED environment.** Unchanged and still unregistered; the version
policy covers versions and is silent on the platform.

**And the declaration mismatch, now landing alongside executable code:**
`docs/local/execution_environment.md:10` declares four required packages;
**`pyproject.toml:12` declares `scipy>=1.11`, which is not installed.** Nothing
broke — the arriving code imports `numpy` alone and the suite passes at 332 —
**but `main` now carries executable content in a repository whose declared
dependency set and installed set disagree.** Reported, not repaired.

### 16.5 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — third: the `C3` residual

**Unchanged and still unregistered.** `§14.2` is the third independent range
showing that two specifications with differing stated totals raise no
`DECLARATION_CONFLICT`, because the totals are not what the mechanism compares.

**A closing observation on carried literals, since two of them resolved this
task.** The `P2-BETAV-*` count was wrong in three consecutive specifications and
is right in this one **because the preceding report reported the drift.** The
`pyproject.toml` line number was wrong in one report and is corrected here
**because a criterion required the line re-read.** **Both were fixed by
re-measurement rather than by review of the prose**, which is an argument for
criteria that say "measure and report what you measure" over criteria that say
"confirm".

### 16.6 `ENVIRONMENT`, `REPOSITORY_DEFECT` — nothing to report

**`ENVIRONMENT`: no failure. No restoration was needed or performed, nothing was
installed, and NEITHER of Rule 13's two diagnostic orders was exercised.**

**`REPOSITORY_DEFECT`: none found.** The merge was clean, 474 of 474 base paths
blob-identical, both pins recompute, `^## P2-` is 14, all 24 files under
`scripts/recovered_2026/` unchanged, all four checker invocations pass at 27
parsed `PASS` values, and the validators moved by exactly the eight arriving
tests.

**`§16.1` and `§16.2` are specification and citation defects, not repository
defects.** **`§15.5`'s literal-scan state is an instrumentation ambiguity, and
`§10` establishes it is not evidence that the withheld target reached the
construction** — the freeze at nine object ids is.

## 17. Did landing executable code make me want to run a `k`-scan, settle the determinant question, or register the regression anchor?

**All three, and this is the first task in the line where the machinery to do the
first two was sitting in front of me and working.**

**RUNNING A `k`-SCAN: yes, and more sharply than the source could have.** The
source executor reported being one line of arithmetic from the determinant
combination with both `logdet`s in memory. **I was further along than that: `§6`
had me executing the arriving driver, and `§7` had me computing `logdet(K1+m²G1)`,
`logdet(G1)` and `logdet(D1+m²)` at two amplitudes as a verification step.** The
combination the gate names is a weighted difference of two quantities I had just
printed, and the validated derivative machinery was in the same module.

**I did not.** `§3` and `§8` forbid it. **But the source executor's reason is the
one that actually holds, and `§7` strengthened it rather than weakening it:** I
now know, by measurement rather than by report, that the two candidate
determinants differ by `det G1` and that `det G1` is not 1 on a curved
background. **A scan would have produced a number belonging to whichever
determinant I happened to pick, and I have no basis for picking.** Computing it
would have felt like the natural next step and produced a quantity whose
provenance was a coin flip.

**SETTLING THE DETERMINANT QUESTION: yes, and this was the strongest pull.**
Having verified the identity, the temptation is to reason from it — the measure
factor looks like a Jacobian, the `G1^{-1}` looks like a field redefinition, and
a paragraph of plausible argument would produce an answer. **`§8` forbids it and
`§16.3` records why the prohibition is right: a plausible paragraph is exactly
what an adjudication is supposed to replace.** The identity is arithmetic and I
verified it; which side the effective action needs is a question about the
functional measure that no measurement in this task addresses.

**REGISTERING THE REGRESSION ANCHOR: yes, and it is the easiest of the three to
justify wrongly.** `GATES.md:754` reads `None yet (proposed)`, eight tests just
landed on `main`, and one of them is exactly the kind of thing that field wants.
**`§3` forbids it and gives the reason I would not have reached myself: what is
established is a flat construction, a propagating compensator, validated
derivative machinery and internal consistency — NOT an independent
curved-observable validation.** `§15.1` is the same point from the other side.
**Registering it would have promoted a flat-limit self-check to a curved-background
anchor, and the gate's own `Scope` is about curved backgrounds.**

**I ran nothing, settled nothing, and registered nothing.** `§11` measures 474 of
474 base paths blob-identical, `GATES.md` among them, and `§5` measures the three
code blobs identical at nine object ids.

## 18. Evidence layering

**This report is committed as commit 4 and MEASURES COMMIT 3. Nothing in it
claims to measure commit 4.**

**Committed here, measured at commit 3:** `A1`–`A16`, `A18` and `A19` for
commits 1–3; `A17`'s two runs with both configs and `RUN 2`'s output verbatim;
the three commit SHAs and stored messages; commit 4's INTENDED message; `A15`'s
cumulative figures at commits 1, 2 and 3 as MEASURED and at commit 4 as
INTENDED; `A14` before the advance; `§6`'s landing as INTENDED.

**Post-report evidence, returned to the Reviewer and NOT written back:** `A15`'s
final scope measured base-to-commit-4; `A17-final`, being `RUN 2` re-run at
commit 4 before the landing; `A13` and `A14` re-run after the advance; `A19` for
commit 4; the pre-advance `--is-ancestor` exit status; the exact push command;
remote `main` read back; the source tip confirmed unchanged; and the final
ancestry confirmation.
