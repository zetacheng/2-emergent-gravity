# Report — integrate the `ε` tractability assessment, and land it

    TASK        integrate-eps-b0
    BRANCH      science/integrate-eps-b0
    BASE        af145d5a3e36e6bca62f038092748ada3abdcec1
    SOURCE      science/eps-b0-scope
    SPEC SHA    238787ca8dbf22dc0ebfc2e477db805a1658d5e9731ba7ab59c8d5c3df6767f8
    REVIEW      APPROVE FOR EXECUTION, bound to that SHA
    VERDICT     BLOCKED PENDING A RULING — R1 DEPENDENCE ESTABLISHED, R1 OPEN
    RIDER       even if R1 were ruled tomorrow, this route would not produce
                a NUMBER

**EVERY FIGURE IS MEASURED AT COMMIT 3 UNLESS THE LINE SAYS `INTENDED`.** This
report is commit 4. **Nothing here claims to measure commit 4.**

**EVERY SHA IS PASTED FROM COMMAND OUTPUT, WITH THE COMMAND SHOWN.**

**TWO COUNT CORRECTIONS TO THE ARRIVING DOCUMENTS ARE REPORTED IN §8.2 AND
§10.2.** Both are the executor's own, both are re-measured here, and neither
changes the verdict.

## 1. `A3` — environment, run FIRST

**Rule 13's diagnostic order applies and was NOT exercised: no environment
failure occurred.** Rule 13 carries two such orders — a known open item — and I
name neither as the one used.

**Amendment D step 0, before anything else:**

    execution location    vm — Linux 6.18.5-fc-v20
    git common dir        /home/user/2-emergent-gravity/.git
    resolved HEAD at step 0       bfef924c368658cac85c04ed18d96eb4450afba6
    HEAD symbolic ref at step 0   refs/heads/claude/paper-2-independent-verification-dysdp0
    task worktree         /tmp/.../scratchpad/iepsb0, branch science/integrate-eps-b0

    $ git rev-parse --is-shallow-repository
    false
    $ git rev-list --count HEAD
    423
    $ git rev-list --count --all
    543

**Toolchain, MEASURED:**

    python 3.11.15 · pytest 9.1.1 · numpy 2.4.6 · sympy 1.14.0 · ruff 0.15.8
    scipy  ABSENT — ModuleNotFoundError: No module named 'scipy'

**`pyproject.toml:12` declares `"scipy>=1.11"` and it is not installed.** Twelfth
consecutive task. **`docs/local/execution_environment.md` declares a Windows
environment that has never been the one used.** Both undeclared, unregistered.

## 2. `A1` — repository, refs, and the second branch

    $ git remote get-url origin
    https://github.com/zetacheng/2-emergent-gravity

**It identifies `zetacheng/2-emergent-gravity`.**

    $ git rev-parse refs/remotes/origin/main
    af145d5a3e36e6bca62f038092748ada3abdcec1

**A1 expects `af145d5a3e36e6bca62f038092748ada3abdcec1`. MATCH.**

    $ git rev-parse refs/heads/science/eps-b0-scope
    efb8d63f0f2e4a208dc735af0936a40db7ce3fe8
    $ git ls-remote origin refs/heads/science/eps-b0-scope
    efb8d63f0f2e4a208dc735af0936a40db7ce3fe8	refs/heads/science/eps-b0-scope

**A1 expects `efb8d63f0f2e4a208dc735af0936a40db7ce3fe8`. MATCH.**

    $ git merge-base --is-ancestor <source> refs/remotes/origin/main
    exit 1        NOT an ancestor of main, as required

### 2.1 The second branch from the same base

    $ git rev-parse refs/heads/science/channel-b0-spin-scope
    8c27a606643ef315d11e1a1dad8875aa2f1029b1

**IT WAS MEASURED AND NOT MERGED.** §5's merge names one parent besides this
task's own — `efb8d63f…` — and §6's blob comparison covers four paths, all from
`EPS-B0`. **`CHANNEL-B0` contributes nothing to commit 3, and `8c27a606…` appears
in no parent, no tree and no message of this task.**

**After this lands, `CHANNEL-B0`'s integration will need a new base**, and the
review states the same: its evidence base must be replaced with this task's
commit 4, its measurements re-established, and its review reissued.

    $ git rev-parse refs/heads/main
    1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**A stale local ref, reported for contrast; the landing pushes
`HEAD:refs/heads/main` to `origin` and does not move it.**

## 3. `A2` — the review, committed unedited

**FIELD PRESENCE CHECKED FIRST, THEN THE VALUE.**

    field present?   YES — review line 4 carries "Reviewed specification SHA-256:"
    value            238787ca8dbf22dc0ebfc2e477db805a1658d5e9731ba7ab59c8d5c3df6767f8
    uploaded spec    238787ca8dbf22dc0ebfc2e477db805a1658d5e9731ba7ab59c8d5c3df6767f8
    IDENTICAL
    committed specs/2026-08-18T2325Z_integrate-eps-b0.md   238787ca8…   IDENTICAL
    verdict, review line 6   APPROVE FOR EXECUTION

## 4. `A13` — which merge case, stated BEFORE the blob comparisons

    $ git merge-base HEAD <source>
    af145d5a3e36e6bca62f038092748ada3abdcec1

    evidence base                            af145d5a3e36e6bca62f038092748ada3abdcec1
    IDENTICAL
    commits on origin/main after the base    0

**THE MERGE-BASE IS THE EVIDENCE BASE, SO NO COMMIT ON `main` COULD HAVE TOUCHED
AN ARRIVING PATH.**

**Then the four blob comparisons — source tip against the merge head:**

    derivations/P2-EPS-B0_epsilon-tractability-scope.md   2b3e513424d4 → 2b3e513424d4  IDENTICAL
    reports/2026-08-18T2124Z_eps-b0-scope.md              fd06491f01a2 → fd06491f01a2  IDENTICAL
    reviews/chatgpt/2026-08-18T2124Z_eps-b0-scope.md      fa26bba12a7c → fa26bba12a7c  IDENTICAL
    specs/2026-08-18T2124Z_eps-b0-scope.md                88c6be550dcf → 88c6be550dcf  IDENTICAL

**Everything arriving by merge is integrated exactly as reviewed.**

## 5. `A5` and `A4` — the merge

    $ git merge-tree --write-tree HEAD <source>
    exit 0, tree 622130d89c96f9f2d0cfd936fe274f75c5429f2a
    conflict list                            EMPTY
    $ git merge --no-ff
    exit 0, 'ort' strategy
    unmerged paths                           0
    $ git ls-files -u
    0 lines

**The conflict list is empty. Any conflict would have been an immediate stop.**

    $ git rev-parse HEAD^1
    d769867d95491e4a0f5dad87110fcc9557ce89bb
    $ git rev-parse HEAD^2
    efb8d63f0f2e4a208dc735af0936a40db7ce3fe8
    $ git merge-base <parent 1> <parent 2>
    af145d5a3e36e6bca62f038092748ada3abdcec1
    $ git merge-base --is-ancestor <commit 1> <parent 1>
    exit 0

**Three values, each from its own command. Parent 2 is the `EPS-B0` tip and
nothing else.**

## 6. `A6` — the `R1` dependence, re-derived from both documents at the head

### 6.1 The two passages, quoted

    paper:525  The phase is therefore fixed not at one loop but by the subleading
    paper:526  effects that explicitly break the chiral $U(1)$: the axial anomaly,
    paper:527  realized on the lattice through the Wilson term and the surviving
    paper:528  doublers, together with the discrete ($Z_M$) structure of the phase
    paper:529  landscape.

    ledger:78                    "*Freeze:* … the canonical lattice Dirac operator; the
    ledger:79                     species ledger and doubling treatment"
    ledger:89      CONTROLS    W8  the Wilson parameter r
    ledger:96      STATUS      OPEN. §5 records the search.

**`ε`'S STATED MECHANISM IS ITEM-FOR-ITEM `R1`'S SUBJECT.** The Wilson term is
`R1`'s control `W8`; the surviving doublers are the species ledger and doubling
treatment `R1` must freeze; `R1` is `OPEN`.

### 6.2 Neither document cites the other on this point

    the manuscript mentioning the ledger / MICROSPEC / D-1c    0 occurrences
    the ledger mentioning the manuscript path                   0 occurrences

**The inference is the executor's own, drawn by setting two documents side by
side. Neither says `ε` needs `R1`.**

### 6.3 The dependency is newly established

    derivations/P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md   varepsilon 0  epsilon 0
    derivations/P2-LATTICE-ONTOLOGY-01.md                          varepsilon 0  epsilon 0
    derivations/P2-LATTICE-ROUTE-01.md                             varepsilon 0  epsilon 0

**ZERO IN ALL THREE. `ε` had never been mapped to any `R`-node.** This is a new
dependency, not a restatement of one.

### 6.4 The executor's own limit, reported verbatim as `A6` requires

> **It did NOT claim `ε`'s VALUE would change under a different ruling — that
> would be physics.** **What is established is that the computation AS DESCRIBED
> cannot be posed without the ruling, because its stated ingredients are the
> ruling's subject.**

**A DEPENDENCY ESTABLISHED TEXTUALLY IS WEAKER THAN ONE ESTABLISHED PHYSICALLY,
AND IT IS THE ONE THAT WAS ESTABLISHED.** No physical demonstration was
attempted, and none was required by the source specification.

## 7. `A7` — the four other `R`-node states

    R1  DEPENDENCE ESTABLISHED    §6
    R2  DEPENDENCE NOT ESTABLISHED   no repository line connects ε to lattice extent
    R3  DEPENDENCE NOT ESTABLISHED   no repository line connects ε to boundary conditions
    R4  DEPENDENCE NOT ESTABLISHED   ROUTE:189 requires "microscopic variables and
                                     measure" frozen as a GENERAL matter and R4 is
                                     open, but no line ties ε's computation to the
                                     measure specifically
    R5  DEPENDENCE ESTABLISHED FOR THE Λ LEG ONLY
                                     :714's M_Pl² = c₂NΛ²/(8π²) contains N; R5 is N;
                                     R5 is open. It does not enter ε itself.

**I CONFIRM `R2`, `R3` AND `R4` ARE REPORTED `NOT ESTABLISHED` AND NOT
`INDEPENDENT`.** The repository is silent about `ε` at those nodes, **and silence
is not independence.** Reporting them as independent would convert an absence of
evidence into a physics conclusion.

## 8. `A8` — the coefficient failure, and a correction to the arriving count

### 8.1 The three relations, quoted at the head

    :533  \qquad K \sim \varepsilon\,\Lambda^4,\quad \varepsilon \ll 1,
    :589  Goldstone mode, with decay constant $f \sim v$ and Lagrangian
    :598  m_\theta^2 \;\sim\; \varepsilon\,\Lambda^2 ,

**THREE TILDES.** And **the ambiguity is inside `ε`'s OWN DEFINITION, not
downstream of it** — `:533` introduces `ε` by a scaling relation, so "computing
`ε`" is not numerically well-posed until a normalisation is fixed, and none is.

### 8.2 The tilde count re-measured — the arriving documents say six; it is four

**`A8` REQUIRES THE TILDE COUNT ON `m_\theta` LINES. I MEASURED IT DIRECTLY
RATHER THAN CARRYING IT, AND IT DOES NOT REPRODUCE.**

    :598    TILDE  \sim         m_\theta^2 \;\sim\; \varepsilon\,\Lambda^2
    :605    STATES NO RELATION  "Radiative corrections to $m_\theta^2$ are
                                 proportional to the …"
    :609    STATES NO RELATION  "An ultralight value of $m_\theta$ therefore
                                 reflects a small …"
    :615    EXACT  =            $r_c = 1/m_\theta$.
    :620    TILDE  \sim         $m_\theta \sim 10^{-27}\,\mathrm{eV}$
    :621    TILDE  \sim         $\varepsilon \sim m_\theta^2/\Lambda^2$
    :1556   TILDE  \sim         naturally small mass $m_\theta^2 \sim
                                 \varepsilon\Lambda^2$

    lines total                7
    carrying \sim              4
    carrying an exact =        1     (:615)
    stating no relation        2     (:605, :609)
    NON-EXACT (7 minus 1)      6

**THE ARRIVING REPORT AT ITS `:312`, THE ARRIVING ARTIFACT AT ITS `:163`, AND
THIS SPECIFICATION'S `§2a` ALL SAY "SIX OF THE SEVEN CARRY `~`". THE TILDE COUNT
IS FOUR.**

**SIX IS THE COUNT OF NON-EXACT LINES — seven minus the one equality at `:615`.**
It was reported as a count of tildes. **A measurement true of one proposition
carried into an assertion about a different one** — the same failure this line
has now recorded under several names, and this instance is the executor's own.

**THE SUBSTANTIVE CLAIM SURVIVES INTACT AND IS ARGUABLY SHARPER WHEN STATED
CORRECTLY:** of the five `m_\theta` lines that state a relation at all, **four
carry `~` and one carries `=`, and the one equality is `SRC-01a`'s
`r_c = 1/m_θ`, not a coefficient.** The coefficient is unfixed either way.

**THE ARRIVING DOCUMENTS ARE NOT REPAIRED.** They arrive by merge, §4 forbids
modifying any file, and Rule 20 permits only pre-push message repair with the
tree unchanged. **The correction is recorded here**, which is where an
integration's authoritative correction belongs.

## 9. `A9` — the `Λ` failure

    CONVENTIONS.md:31  "| Cutoff and lattice units | `Λ ≡ 1` (continuum),
                        `a ≡ 1` (lattice); masses quoted as `m/Λ` or `m a`. |"

**`Λ ≡ 1` IS A UNIT, NOT A VALUE.** A quantity set to one by convention cannot
supply a physical scale to anything.

    paper:717  For $\Lambda \sim 1/a$ at the Planck scale and

**"At the Planck scale" is an input to a consistency check, not an output.**

    paper:714  M_{\mathrm{Pl}}^2 = \frac{c_2\,N\Lambda^2}{8\pi^2}.

**The one relation to a measurable requires an OBSERVED `M_Pl`, plus `c₂`, plus
`N`. And of `c₂`:**

    paper:737  cutoff, $c_2$ is part of the definition of the model rather than a
    paper:738  derived quantity, and Eq.~\eqref{eq:Mpl} with $c_2 > 0$ is at
    paper:739  present a defining assumption.

**`N` is `R5`, verified open.**

> **SO THE CHAIN DOES NOT REVERSE; IT LOOPS.** A prediction of `r_c` in physical
> units needs `Λ` in physical units, and the only route to `Λ` in physical units
> passes through an observed `M_Pl`, a defining assumption `c₂`, and an open
> ruling `N`.

**THE BEST OUTCOME REACHABLE FROM A SETTLED `R1` IS `TRACTABLE BUT ONLY A
RELATION`.**

## 10. `A10` — the three further findings, verified at the head

### 10.1 No gate covers this object

    ^## P2- count in GATES.md    14

    varepsilon 0 · epsilon 0 · ε 0 · angular 0 · Goldstone 0
    dark matter 0 · instanton 0 · anomaly 0 · m_theta 0

**ZERO ON ALL NINE ACROSS ALL FOURTEEN SECTIONS.**

### 10.2 `M`, the `Z_M` order — and a second correction to the arriving count

**`M`, the order of the discrete `Z_M` phase symmetry, is a required input that
no document fixes and no `R`-node covers.** Without it
`V_θ(θ) ≃ −K cos(Mθ)` is not a computable object, and `R1`–`R5` are about the
Dirac operator, the extent, the boundary conditions, the measure and `N`.

    Z_M in CONVENTIONS.md and GATES.md    0

**AND THE LINE COUNT DOES NOT REPRODUCE EITHER.**

    the literal token Z_M in the manuscript          2 lines — :528, :594
    the discrete-phase-symmetry cluster
      (Z_M twice, plus cos(Mθ) at :532)              3 lines

**THE ARRIVING ARTIFACT AT ITS `:130` AND `:278` AND THE ARRIVING REPORT AT ITS
`:446` SAY `Z_M` OCCURS ON "EXACTLY THREE LINES". THE TOKEN OCCURS ON TWO.** The
third line, `:532`, carries `cos(M\theta)` — the same symmetry's ORDER, not the
symbol `Z_M`.

**SAME SPECIES OF ERROR AS §8.2: a count of one thing reported as a count of
another.** **And the substantive finding survives unchanged** — the `Z_M`
collision with the Fierz/channel-freeze normalisation constant of the same name
holds whether the phase-symmetry `Z_M` occurs on two lines or three, and `M`
remains unfixed either way.

**Not repaired, for the same reason as §8.2.**

### 10.3 The anomaly is one term of `ε`, not all of it

    paper:601  where $\varepsilon$ collects the explicit-breaking coefficients.

**PLURAL.** And `:541-543` singles out one of them for the open computation:
*"in particular whether the ANOMALY CONTRIBUTION is exponentially
instanton-suppressed"*. **A computation settling only the anomaly term's
suppression would not have computed `ε`.**

## 11. `A11` — nothing computed

**SEARCHED the arriving artifact and every commit message in the range.**

    CATEGORY                              ARTIFACT   COMMIT MESSAGES
    any physical-unit numeral                    0                 0
    any suppression factor                       0                 0
    any quotient of manuscript values            0                 0

**THE SOURCE EXECUTOR REPORTED THAT THE ARTIFACT CONTAINS NO PHYSICAL-UNIT
NUMERAL AT ALL. VERIFIED: ZERO.** A word-bounded search for `kpc`, `eV`, `GeV`,
`TeV`, `10^{-27}` and `10⁻²⁷` returns nothing in the artifact.

**THE SPECIFIC TEMPTATION `§4` NAMES WAS NOT PERFORMED HERE EITHER.** `:621`
gives `ε ~ m_θ²/Λ²`, `:620` gives `m_θ`, `:717` puts `Λ` at the Planck scale —
two numbers and a division. **That division would run `SRC-01a`'s chain and
launder an observational input into a microscopic quantity.** It appears nowhere
in the arriving documents, in this report, or in any commit message.

**THIS REPORT IS NOT ITSELF AT ZERO, AND THE REASON IS STRUCTURAL RATHER THAN A
BREACH.** Stated POSITIONALLY, because a count of a document's own quotations and
pattern lists changes with every later edit to it — the failure mode this line
recorded at `DET-01`'s `A10`:

    §11, THIS SECTION             its pattern list, and this accounting, both
                                  of which must name the tokens to report on them
    §8.2's classification table   quotes manuscript line :620 VERBATIM,
                                  `$m_\theta \sim 10^{-27}\,\mathrm{eV}$`,
                                  because A8 requires showing WHICH lines carry
                                  a tilde and :620 is one of the four

**There is no third place.** **The quoted value is transcribed from a cited
manuscript line to classify its relation symbol; nothing is computed from it, and
no quotient of it with any other value appears anywhere.** **The artifact and
every commit message — the two subjects the prohibition protects — are at zero.**

## 12. `A12` – `A16` — scope and integrity

### 12.1 `A12` — scope

    stated: 7 additions, 0 modifications          INTENDED, final at commit 4
    append_only:  DECISION_LOG.md                 a CHECKER-CONFIGURATION declaration,
                                                  NOT an authorisation to write it
    authorised_gates: []
    base: af145d5a3e36e6bca62f038092748ada3abdcec1
    head: commit 4
    mode: exact
    modify: []
    forbidden_operations: delete, rename, copy, type_change, unmerged, unknown

**CUMULATIVE per commit — MEASURED:**

    base .. commit 1  c1f94a6d     1 addition,  0 modifications
    base .. commit 2  d769867d     2 additions, 0 modifications
    base .. commit 3  d60eb7ed     6 additions, 0 modifications
    base .. commit 4               7 additions, 0 modifications   INTENDED

**SOURCE'S OWN CONTRIBUTION — MEASURED, separately labelled: 4 additions, 0
modifications.**

      derivations/P2-EPS-B0_epsilon-tractability-scope.md
      reports/2026-08-18T2124Z_eps-b0-scope.md
      reviews/chatgpt/2026-08-18T2124Z_eps-b0-scope.md
      specs/2026-08-18T2124Z_eps-b0-scope.md

**`6` IS CUMULATIVE, NOT THE MERGE'S CONTRIBUTION.** The merge contributes four;
the range holds six at commit 3 because commits 1 and 2 added two more. **They
are not addends.**

**ARRIVING PATH COUNT `4`; ARRIVING ADDITION COUNT `4`. They coincide**, because
every arriving path is an addition and none arrives twice.

**The UTC time was measured, not assumed: `2026-08-18T23:25:54Z`, giving the token
`2325Z`.** Commit 1 was made in the same minute.

### 12.2 `A14` — nothing existing changed

    PATHS COMPARED (all paths at the evidence base)    505
    paths at the head                                  511
    paths whose blob DIFFERS at the head                 0
    git diff --name-status base..head                    6 entries, ALL status A

**THE MANUSCRIPT BLOB AT BOTH ENDS:**

    $ git rev-parse <base>:paper/emergent_gr_paper_v2_15.tex
    c8246f890b07f53ab8094981cbd5a02972fda4c1
    $ git rev-parse HEAD:paper/emergent_gr_paper_v2_15.tex
    c8246f890b07f53ab8094981cbd5a02972fda4c1

**IDENTICAL — and §6, §8, §9 and §10 all quote it, so this matters: every line
re-verified above was read from a file this task did not touch.**

    GATES.md · CONVENTIONS.md · docs/BRANCHING_POLICY.md · DECISION_LOG.md
    scripts/recon2026/proca_curved.py · scripts/recon2026/flat_validation.py
    tests/test_recon2026_flat_limit.py            ALL UNCHANGED

**`derivations/P2-*` RE-MEASURED: base 49, head 50** — the specification's
pre-issue figure of 49 reproduces, and the one addition is `EPS-B0`'s artifact.
**`results/` subtree `9015049f68d5ace2790b5c62976e798298442bce` at both ends.**

### 12.3 `A15` — gate invariants and pins

**Read SCOPED: `P2-PHASE-01` is `GATES.md:971–1108`.**

    ^## P2- count                     14
    P2-PHASE-01 status  GATES.md:973  Status: PROPOSED
    prerequisite 1      GATES.md:1011 ADOPTED / SATISFIED
    prerequisite 2      GATES.md:1036 ADOPTED / SATISFIED

**Both pins verified by recomputing each pinned artifact's digest:**

    P2-PHASE-01_microscopic_parameter_domain.md
      recomputed 4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
      pinned at GATES.md:1017 — MATCH
    P2-PHASE-01_input_admissibility_contract.md
      recomputed e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
      pinned at GATES.md:1040 — MATCH

### 12.4 `A16` — superseded branches, before the advance

    52f65117 exit 1 · ebd531ab exit 1 · 40168469 exit 1
    7146a093 exit 1 · 10c260b9 exit 1 · d64cd912 exit 1

**Exit 1 means NOT an ancestor, which is required. The after-the-advance re-run
is post-report evidence and is not written here.**

## 13. `A17` — the checker over this task's own range

**Base `af145d5a…`, head commit 3. Two runs at both prospectivity readings — four
invocations, all exit `0`.**

**THE OUTPUT WAS PARSED, NOT GREPPED.** Each JSON file was loaded with
`json.loads` and every property read from the parsed structure by key. The
property list is a JSON *array* of objects rather than a map keyed by property
id, so a key lookup returns `None`, and a grep for `PASS` would count the word
wherever it occurs — including inside the `does_not_establish` prose every
`PARTIAL` property carries.

**`RUN 1` config, verbatim — observational, governs nothing:**

    {
      "base": "af145d5a3e36e6bca62f038092748ada3abdcec1",
      "head": "d60eb7ed168400b7b2f0563a5952ea89e08b256b",
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
      "base": "af145d5a3e36e6bca62f038092748ada3abdcec1",
      "head": "d60eb7ed168400b7b2f0563a5952ea89e08b256b",
      "specification_paths": [
        "specs/2026-08-18T2325Z_integrate-eps-b0.md"
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

**Each `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`,
and the outputs differ at exactly one line — 314 of 318 for `RUN 1`, 291 of 295
for `RUN 2`.**

**Results, identical across all four invocations:**

    P1  PASS  PARTIAL     scope manifest arithmetic
    P2  PASS  MECHANICAL  Rule 15 commit order
    P3  PASS  PARTIAL     append-only on both measures        declared_source: specification
    P4  PASS  MECHANICAL  superseded branches are not merged
    P5  PASS  PARTIAL     merge parentage against recomputed facts
    P6  PASS  PARTIAL     commit-message hygiene
    P7  PASS  PARTIAL     gate integrity                      declared_source: specification
    P8  PASS  MECHANICAL  Rule 15 placement and specification-first
    P9  PASS  MECHANICAL  reports carry a Stops and clarifications section

    overall                        PASS
    exit status, all four           0
    NOT_DECLARED / NOT_PARSEABLE    none
    DECLARATION_CONFLICT            NONE — confirmed
    commits_in_range                7
    commits_on_first_parent_line    3
    prospectivity in scope 3, out of scope []

**`P7` REPORTS FOURTEEN SECTIONS** — base 14, head 14, raw 14 and 14. **`PASS` at
zero would have been a stop; it is not zero.**

**`P5` is `PASS` rather than `NOT_APPLICABLE`** — this range contains a merge and
the checker recomputed its parentage. **`P9` is `PASS` on the arriving `EPS-B0`
report.**

### 13.1 What `RUN 1` did, and the `C3` residual

**`RUN 1`'s default subject selection discovered TWO specifications in range:**

    specs/2026-08-18T2124Z_eps-b0-scope.md
      stated: 4 additions, 0 modifications    counted 4    parse OK
    specs/2026-08-18T2325Z_integrate-eps-b0.md
      stated: 7 additions, 0 modifications    counted 7    parse OK

**`RUN 2` names only this task's and sees one.** **`RUN 1` discovers the subject;
`RUN 2` names it. That is not the same check even when the verdicts agree.**

**THE `C3` MULTI-SPECIFICATION RESIDUAL AROSE AGAIN AND AGAIN RAISED NOTHING** —
stated totals `4` and `7`, differing, **no `DECLARATION_CONFLICT`.**
`_declarations_from_specs` compares `append_only_paths` and
`authorised_modified_gates`, which agreed; **it does not compare stated totals.**

**SEVENTH INDEPENDENT RANGE IN THIS SESSION, FOURTH WITH TWO GENUINELY DIFFERING
DECLARATIONS. Still unregistered.**

**Neither the config nor this specification's declarations were adjusted to make
`RUN 2` pass. `RUN 2` passed on its first invocation at both readings.**

### 13.2 The two JSON outputs, verbatim

**`RUN 1`, `INCLUSIVE` — 318 lines. The `EXCLUSIVE` output is this file with line
314 reading `"inclusivity": "EXCLUSIVE"`.**

    {
      "base": "af145d5a3e36e6bca62f038092748ada3abdcec1",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "d60eb7ed168400b7b2f0563a5952ea89e08b256b",
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
                "derivations/P2-EPS-B0_epsilon-tractability-scope.md",
                "reports/2026-08-XXT{HHMM}Z_eps-b0-scope.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_eps-b0-scope.md",
                "specs/2026-08-XXT{HHMM}Z_eps-b0-scope.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-18T2124Z_eps-b0-scope.md",
              "stated": 4,
              "stated_add": 4,
              "stated_modify": 0,
              "stated_record": "stated: 4 additions, 0 modifications"
            },
            {
              "append_only": [
                "DECISION_LOG.md"
              ],
              "authorised_gates": [],
              "counted": 7,
              "counted_add": 7,
              "counted_modify": 0,
              "counted_set": [
                "derivations/P2-EPS-B0_epsilon-tractability-scope.md",
                "reports/2026-08-18T2124Z_eps-b0-scope.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-eps-b0.md",
                "reviews/chatgpt/2026-08-18T2124Z_eps-b0-scope.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-eps-b0.md",
                "specs/2026-08-18T2124Z_eps-b0-scope.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-eps-b0.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-18T2325Z_integrate-eps-b0.md",
              "stated": 7,
              "stated_add": 7,
              "stated_modify": 0,
              "stated_record": "stated: 7 additions, 0 modifications"
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
                "commit": "c1f94a6ded76d23050138c205f2915beb0ba2d8f",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "d769867d95491e4a0f5dad87110fcc9557ce89bb",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "d60eb7ed168400b7b2f0563a5952ea89e08b256b",
                "work_paths": [
                  "derivations/P2-EPS-B0_epsilon-tractability-scope.md"
                ]
              }
            ],
            "first_review_commit": "d769867d95491e4a0f5dad87110fcc9557ce89bb",
            "first_work_commit": "d60eb7ed168400b7b2f0563a5952ea89e08b256b",
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
              "specs/2026-08-18T2124Z_eps-b0-scope.md",
              "specs/2026-08-18T2325Z_integrate-eps-b0.md"
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
              "merge": "d60eb7ed168400b7b2f0563a5952ea89e08b256b",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "af145d5a3e36e6bca62f038092748ada3abdcec1",
              "recomputed_parent_1": "d769867d95491e4a0f5dad87110fcc9557ce89bb",
              "recomputed_parent_2": "efb8d63f0f2e4a208dc735af0936a40db7ce3fe8",
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
              "commit": "c1f94a6ded76d23050138c205f2915beb0ba2d8f",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "d769867d95491e4a0f5dad87110fcc9557ce89bb",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "5619b448cc15dcd1c2f742f5d71fe16d4851b031",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "f591ecc121fd56a3c94530bc1a70b5dfc64ead59",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "e959a4c3bc9d753c1f7fb0dd92488c1f074226a7",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "efb8d63f0f2e4a208dc735af0936a40db7ce3fe8",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "d60eb7ed168400b7b2f0563a5952ea89e08b256b",
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
              "specs/2026-08-18T2124Z_eps-b0-scope.md",
              "specs/2026-08-18T2325Z_integrate-eps-b0.md"
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
            "first_commit": "c1f94a6ded76d23050138c205f2915beb0ba2d8f",
            "first_commit_paths": [
              "specs/2026-08-18T2325Z_integrate-eps-b0.md"
            ],
            "reports_added": [
              "reports/2026-08-18T2124Z_eps-b0-scope.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-18T2325Z_integrate-eps-b0.md",
              "reviews/chatgpt/2026-08-18T2124Z_eps-b0-scope.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-18T2325Z_integrate-eps-b0.md",
              "specs/2026-08-18T2124Z_eps-b0-scope.md"
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
              "path": "reports/2026-08-18T2124Z_eps-b0-scope.md",
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

**`RUN 2`, `INCLUSIVE` — 295 lines, stop-governing. The `EXCLUSIVE` output is
this file with line 291 reading `"inclusivity": "EXCLUSIVE"`.**

    {
      "base": "af145d5a3e36e6bca62f038092748ada3abdcec1",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "d60eb7ed168400b7b2f0563a5952ea89e08b256b",
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
              "counted": 7,
              "counted_add": 7,
              "counted_modify": 0,
              "counted_set": [
                "derivations/P2-EPS-B0_epsilon-tractability-scope.md",
                "reports/2026-08-18T2124Z_eps-b0-scope.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-eps-b0.md",
                "reviews/chatgpt/2026-08-18T2124Z_eps-b0-scope.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-eps-b0.md",
                "specs/2026-08-18T2124Z_eps-b0-scope.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-eps-b0.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-18T2325Z_integrate-eps-b0.md",
              "stated": 7,
              "stated_add": 7,
              "stated_modify": 0,
              "stated_record": "stated: 7 additions, 0 modifications"
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
                "commit": "c1f94a6ded76d23050138c205f2915beb0ba2d8f",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "d769867d95491e4a0f5dad87110fcc9557ce89bb",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "d60eb7ed168400b7b2f0563a5952ea89e08b256b",
                "work_paths": [
                  "derivations/P2-EPS-B0_epsilon-tractability-scope.md"
                ]
              }
            ],
            "first_review_commit": "d769867d95491e4a0f5dad87110fcc9557ce89bb",
            "first_work_commit": "d60eb7ed168400b7b2f0563a5952ea89e08b256b",
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
              "specs/2026-08-18T2325Z_integrate-eps-b0.md"
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
              "merge": "d60eb7ed168400b7b2f0563a5952ea89e08b256b",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "af145d5a3e36e6bca62f038092748ada3abdcec1",
              "recomputed_parent_1": "d769867d95491e4a0f5dad87110fcc9557ce89bb",
              "recomputed_parent_2": "efb8d63f0f2e4a208dc735af0936a40db7ce3fe8",
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
              "commit": "c1f94a6ded76d23050138c205f2915beb0ba2d8f",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "d769867d95491e4a0f5dad87110fcc9557ce89bb",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "5619b448cc15dcd1c2f742f5d71fe16d4851b031",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "f591ecc121fd56a3c94530bc1a70b5dfc64ead59",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "e959a4c3bc9d753c1f7fb0dd92488c1f074226a7",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "efb8d63f0f2e4a208dc735af0936a40db7ce3fe8",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "d60eb7ed168400b7b2f0563a5952ea89e08b256b",
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
              "specs/2026-08-18T2325Z_integrate-eps-b0.md"
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
            "first_commit": "c1f94a6ded76d23050138c205f2915beb0ba2d8f",
            "first_commit_paths": [
              "specs/2026-08-18T2325Z_integrate-eps-b0.md"
            ],
            "reports_added": [
              "reports/2026-08-18T2124Z_eps-b0-scope.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-18T2325Z_integrate-eps-b0.md",
              "reviews/chatgpt/2026-08-18T2124Z_eps-b0-scope.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-18T2325Z_integrate-eps-b0.md",
              "specs/2026-08-18T2124Z_eps-b0-scope.md"
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
              "path": "reports/2026-08-18T2124Z_eps-b0-scope.md",
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

## 14. `A18` and `A19` — validators and hygiene

    $ python3 -m pytest -q
    332 passed, 2 deselected in 44.17s
    exit status 0

**332 passed, 2 deselected, exactly as expected. The arriving task adds no
code.**

**`A19` — hygiene on all four commits. Rule 20 binds this task and was not
needed: no message required repair, no history was rewritten. Every SHA pasted
from `git rev-parse`:**

    commit 1  c1f94a6ded76d23050138c205f2915beb0ba2d8f
              spec: integrate and land the epsilon tractability assessment
    commit 2  d769867d95491e4a0f5dad87110fcc9557ce89bb
              review: pre-execution review for the epsilon tractability integration
    commit 3  d60eb7ed168400b7b2f0563a5952ea89e08b256b
              merge: integrate the epsilon tractability assessment
    commit 4  INTENDED message:
              report: the epsilon route is blocked pending R1 and would not give a number

    Co-Authored-By          0        Generated with        0
    Co-authored-by          0        Claude-Session        0
    claude.ai/code          0        any model identifier  0
    🤖                      0        noreply@anthropic.com 0

**All zero. `A19` for commit 4 is post-report evidence and is not written here.**

## 15. `§7` — Rule 16 assessment

### 15.1 First — the `R1` dependence is TEXTUAL

**TWO DOCUMENTS DESCRIBE THE SAME OBJECTS; NEITHER SAYS `ε` NEEDS `R1`.** §6.2
measured it: the manuscript never mentions the ledger, and the ledger never
mentions the manuscript.

**THE INFERENCE IS THE EXECUTOR'S.** It is sound as a reading — the manuscript
names the Wilson term and the surviving doublers as `ε`'s mechanism, and the
ledger names exactly those as what `R1` must rule and has not. **A physical
demonstration was neither attempted nor required**, and §6.4 carries the
executor's own limit verbatim: the claim is that the computation as described
cannot be posed, not that `ε`'s value would change.

**A READER WHO TAKES `R1 DEPENDENCE ESTABLISHED` AS A PHYSICAL NECESSITY WOULD BE
READING MORE THAN WAS SHOWN.**

### 15.2 Second — `R1` is not the only blocker and is not the deepest

**THE COEFFICIENT GAP SITS INSIDE `ε`'S OWN DEFINITION** — `:533` introduces `ε`
by `K ~ εΛ⁴`, a scaling relation — **and `Λ ≡ 1` is a unit convention, not a
value.**

**A READER WHO TAKES `BLOCKED PENDING R1` AS "UNBLOCKED ONCE `R1` LANDS" WOULD BE
WRONG.** Neither the coefficient nor `Λ` is any `R`-node's subject, and either
alone reduces the outcome to a scaling law.

> **THE BEST OUTCOME REACHABLE FROM A SETTLED `R1` IS `TRACTABLE BUT ONLY A
> RELATION`.**

### 15.3 Third — this closes a route, not a question

**WHETHER `m_θ` IS PREDICTABLE REMAINS OPEN.** What is established is that **THIS
repository's stated path to it does not reach a number.**

**A DIFFERENT FORMULATION MIGHT.** A treatment that fixed a normalisation for
`ε`, derived `c₂` rather than assuming it, or determined `Λ` internally would
face none of the three obstacles this landing records. **Nothing here bears on
whether such a treatment exists** — the finding is about what this repository
says, not about what is computable in principle.

### 15.4 Fourth — `SRC-01a`'s verdict is unchanged

**`FORM DERIVED / SCALE FITTED` STANDS.** This landing removes the candidate
route for changing the second half of it.

**THE SCALE REMAINS OBSERVATIONAL.** `SPARC → r_c → m_θ → ε` runs
observation-inward, and the reversal `microscopic theory → ε → m_θ → r_c` is not
available. **`ε` was the candidate for turning a fitted scale into a predicted
one, and it is not.**

### 15.5 Fifth — the dependency map is incomplete

**`M`, the `Z_M` order, is a required input covered by NO DOCUMENT AND NO
`R`-NODE.** Without it the angular potential is not a computable object, and
`R1`–`R5` are about the Dirac operator, the extent, the boundary conditions, the
measure and `N`.

**`D-1c` MAPPED WHAT `D-1` FOUND, AND `D-1` WAS A REFLECTION-POSITIVITY AUDIT.**
The five nodes are the ruling-shaped gaps that audit surfaced. **A quantity like
`M`, which no reflection-positivity question touches, was never in that audit's
field of view** — so its absence from the ledger is a consequence of the ledger's
provenance, not evidence that `M` is settled.

**THE MAP IS INCOMPLETE IN A WAY ITS OWN CONSTRUCTION EXPLAINS**, and this
landing is the first task to name an input that falls outside it.

## 16. The temptation, answered directly

**Did landing a blocked route make me want to compute `ε`?** **Yes, and §4 names
the exact form: `:621` gives `ε ~ m_θ²/Λ²`, `:620` gives `m_θ`, `:717` puts `Λ`
at the Planck scale — two numbers and a division.** **The pull is that it would
LOOK like closing the gap the report says is open.** It would do the opposite: it
would run `SRC-01a`'s chain backwards and relabel an observational input as a
microscopic quantity. **§11 measures that it appears nowhere — zero physical-unit
numerals in the arriving artifact, zero in this report, zero in every commit
message.**

**Did I want to declare `R1` the only blocker?** **Yes, and this was the more
insidious one, because it is a simplification rather than an invention.**
"Blocked pending `R1`" is a clean sentence and a reader remembers it; "blocked
pending `R1`, and also the coefficient, and also `Λ`" is not. **§15.2 exists to
stop that compression**, and the rider is carried in the report's own header
rather than buried.

**Did I want to call `R2`–`R4` independent?** **Yes, and the pull was toward
tidiness.** Having established one dependence textually, it would round the
finding off to say the others are ruled out. **The repository is silent about `ε`
at those nodes, and silence is not independence** — §7 reports all three as `NOT
ESTABLISHED` and says why the distinction matters.

**One thing I did that nothing asked for, and it is the substance of §8.2 and
§10.2.** `A8` said "report the tilde count" and `A10` said "verify at the head".
**I re-measured both rather than transcribing them from the arriving documents,
and both came back different** — four tildes where three documents say six, two
`Z_M` lines where three documents say three. **The errors are mine, from the
source task.** They change nothing about the verdict, and reporting them was not
optional: the criteria said measure, and a measurement that agrees with a carried
figure only because it was copied is not a measurement.

## 17. Stops and clarifications

**NO STOP WAS DECLARED. All acceptance criteria completed.**

### 17.1 Stops

**NONE.**

### 17.2 Findings, one primary category each

**`OBSERVATION_METHOD_ERROR` — the arriving report `:312`, the arriving artifact
`:163` and this specification's `§2a` state "six of the seven `m_\theta` lines
carry `~`". The tilde count is FOUR.** Six is the count of NON-EXACT lines. **A
count of one thing reported as a count of another**, and the executor's own from
the source task. Not repaired — the documents arrive by merge and Rule 20 permits
only pre-push message repair. **The substantive claim survives.** §8.2.

**`OBSERVATION_METHOD_ERROR` — the arriving artifact `:130` and `:278` and the
arriving report `:446` state that `Z_M` occurs on "exactly THREE lines". The
token occurs on TWO** — `:528` and `:594`; the third line `:532` carries
`cos(Mθ)`, the same symmetry's order, not the symbol. **Same species of error.
Not repaired. The collision finding survives.** §10.2.

**`REPOSITORY_DEFECT` — no gate covers `ε`, the angular mode, the
pseudo-Goldstone, or the dark-matter scalar.** `GATES.md` returns zero on all
nine terms across its fourteen sections. §10.1.

**`REPOSITORY_DEFECT` — `M`, the `Z_M` order, is a required input that no
document fixes and no `R`-node covers.** §10.2, §15.5.

**`REPOSITORY_DEFECT` — the `C3` multi-specification residual remains
unregistered.** Two specifications in range with stated totals `4` and `7` raised
no `DECLARATION_CONFLICT`. **Seventh independent range this session; fourth with
two genuinely differing declarations.** §13.1.

**`ENVIRONMENT` — `scipy` is declared at `pyproject.toml:12` and is not
installed.** Twelfth consecutive task. §1.

**`ENVIRONMENT` — `docs/local/execution_environment.md` declares a Windows
environment that has never been the one used.** Undeclared, unregistered. §1.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the `R1` dependence is textual,
not physical, and the two documents that establish it do not cite each other.**
The inference is the executor's. §6, §15.1.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — `R2`, `R3` and `R4` are
`DEPENDENCE NOT ESTABLISHED`, which is weaker than `INDEPENDENT` and must not be
read as it.** §7.

### 17.3 Clarifications, not defects

**`science/channel-b0-spin-scope @ 8c27a606…` was measured and NOT merged.** It
branches from the same base and its integration will need commit 4 as its new
evidence base. §2.1.

**Rule 13's two diagnostic orders were not exercised**, because no environment
failure occurred; I name neither as the one used, per §8.

**`refs/heads/main` is a stale local ref at `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`.**
The landing pushes `HEAD:refs/heads/main` to `origin`; the local ref is not the
target and is not moved. §2.

**The `derivations/P2-*` count of 49 in the specification's pre-issue record
reproduces exactly**, and the head is 50. §12.2.

**The stop-hook's recurring "405 unpushed commits" claim on the session branch is
an artefact of the clone having been unshallowed.** The session branch has
nothing unpublished and is not pushed by this task. §1.
