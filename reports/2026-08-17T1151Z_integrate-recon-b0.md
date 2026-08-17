# Report — integrating and landing the clean-room Proca reconstruction scope assessment

    branch      science/integrate-recon-b0
    base        ece34f7bacbbee00efa0fecf0be644d593eed72f   (authoritative main)
    source      e219ae0e5e2a740c9212795599bb37460ba8d5bf   (science/recon-b0-scope)
    measured at commit 3, 3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8
    landing     §7's fast-forward of refs/heads/main to commit 4 is POST-REPORT

**NOTHING WAS BUILT, NOTHING WAS RUN, AND NOTHING WAS ADJUDICATED.**

**`A8a` returned NO DEPENDENCE. The clean-room `β_V/β_B` RATIO reconstruction
line may proceed while `R1`–`R5` remain open.** **It is the RATIO line, not
"the `βV` reconstruction"** — absolute and assembled `β_V`, and `G_ind`, remain
constrained by `A8b`.

**Three unresolved items arrive with it, and this task resolved none of them.**

---

## 1. `A3` — environment conformance, run FIRST

**Rule 13's diagnostic order, with Amendment D's step 0, run before any other
criterion. MEASURED, not assumed.**

    (0) execution location    /home/user/2-emergent-gravity — the primary
        (Amendment D)         worktree. git dir .git, common dir .git, so this
                              is not a linked worktree. HEAD branch
                              claude/paper-2-independent-verification-dysdp0,
                              resolved bfef924c368658cac85c04ed18d96eb4450afba6.
                              Eight linked worktrees exist; this task's work was
                              done in a NINTH, cut fresh at
                              refs/remotes/origin/main.

    (1) interpreter           Python 3.11.15 at /usr/local/bin/python3

    (2) declared packages     MEASURED: pytest 9.1.1, numpy 2.4.6,
                              sympy 1.14.0, ruff 0.15.8 — all four declared
                              packages present.

    (3) clone depth           NOT shallow. No `shallow` file in the common git
                              dir; `--is-shallow-repository` returns false.
                              489 commits reachable from all refs, 423 from
                              HEAD.

    (4) working tree          clean; `status --porcelain` empty in the primary
                              worktree before any work began.

    (5) declaration compared  `docs/local/execution_environment.md` declares a
                              WINDOWS environment. See `§19.3`.

**NO RESTORATION WAS NEEDED AND NONE WAS PERFORMED. No repository content was
touched by `A3`.**

**Rule 13 carries TWO diagnostic orders, a known open item.** **No environment
failure occurred, so NEITHER order was exercised** — this is a conformance
report, not a diagnosis, and naming one of the two here would misrepresent
which was followed.

**One measurement method note.** `ruff` is present as a CLI at
`/root/.local/bin/ruff` and reports `0.15.8`, but `python3 -c "import ruff"`
raises `ModuleNotFoundError`. **The declared requirement is the package name
and `ruff`'s interface is its executable, so this is conformance, not a
shortfall.** Recording the method matters: an import-only probe would have
reported a missing declared package and triggered a restoration that was not
needed.

## 2. `A1` — repository, refs, source ancestry

**`origin` URL, MEASURED and reported VERBATIM, not normalised:**

    https://github.com/zetacheng/2-emergent-gravity

**No `.git` suffix and no trailing slash.** It identifies
`zetacheng/2-emergent-gravity`, which is the specification's repository, and the
specification accepts either URL form.

**Refs, MEASURED after `git fetch origin main`:**

    refs/remotes/origin/main   ece34f7bacbbee00efa0fecf0be644d593eed72f
    expected by §4 A1         ece34f7bacbbee00efa0fecf0be644d593eed72f   MATCH

    refs/heads/main            1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**`refs/heads/main` is reported for contrast and it LAGS.** It sits at
`1cb5550f…`, a commit from the `governance/integrate-enforcement-checks-v2`
line, and it is **not** the authority. **Every measurement in this report is
against `refs/remotes/origin/main`.** A local `main` that lags is a trap for
anyone who reads `main` without the `origin/` prefix.

**Source, MEASURED:**

    science/recon-b0-scope     e219ae0e5e2a740c9212795599bb37460ba8d5bf
    is-ancestor of origin/main exit 1 — NOT AN ANCESTOR

**So the source is unmerged, and this task is the merge.** The branch to create,
`science/integrate-recon-b0`, existed at neither the remote (0 hits) nor locally
(0 hits) before this task created it.

## 3. `A2` — the pre-execution review

**The FIELD-PRESENT check was run BEFORE the match check, in that order, as the
criterion requires.**

    field name present     grep 'reviewed specification SHA-256' → line 4, ONE hit
    field filled in        yes — a 64-hex value, not a placeholder
    value in the review    b99d8cfaa9dfd2a8f46054e1d57b5bfb24fe59d40232f9fcd60a2bb87de05157
    sha256 of the spec     b99d8cfaa9dfd2a8f46054e1d57b5bfb24fe59d40232f9fcd60a2bb87de05157
                           MATCH

**The order is load-bearing.** A review with the field absent altogether and a
review whose field disagrees are different defects; comparing first cannot tell
them apart, because an absent field compares as "no match".

**The review is committed UNEDITED.** The committed blob's sha256 is
`f3b857e7468b59f376bf352dcfe5fa096e7ccc16b3701e75d88cf57d39126910`, identical to
the uploaded bytes. **Verdict `APPROVE FOR EXECUTION`, thirteen sections all
`PASS`.**

## 4. `A4` — merge parentage, three separately derived measurements

**Each derived on its own, not read off the merge:**

    parent 1     git rev-parse HEAD^1   eb4bad24185adc7f267de0b3138e33af38786966
                 this task's review commit (commit 2)                     MATCH

    parent 2     git rev-parse HEAD^2   e219ae0e5e2a740c9212795599bb37460ba8d5bf
                 the source tip named in §0                               MATCH

    merge-base   git merge-base HEAD^1 HEAD^2
                 ece34f7bacbbee00efa0fecf0be644d593eed72f
                 the specification's evidence base                        MATCH

**Commit 1 is an ancestor of parent 1:** `--is-ancestor 960b0629… eb4bad24…`
returns **exit 0**.

**The checker's `P5` recomputed the same three values independently** and
reports `merge_base_equals_parent_1: false` — correct, since the base is
`ece34f7b…` and parent 1 is commit 2. `compared_to_recorded: UNAVAILABLE`: the
checker has no recorded parentage to compare against, so `P5` is a recomputation
check, not a cross-check against a declaration.

## 5. `A5` — no conflict

    git merge --no-ff --no-commit e219ae0e…    exit 0
    "Automatic merge went well; stopped before committing as requested"

    conflict list, git diff --name-only --diff-filter=U     0 paths
    unmerged index entries, git ls-files -u                  0

**THE CONFLICT LIST IS EMPTY, as §4 A5 requires.** A dry run via
`git merge-tree --write-tree` beforehand produced tree
`256d0c91e3cd8974e7254943d3054ad07f20b9c5` with an empty conflict section,
agreeing with the real merge.

## 6. `A6` — `A8a` and `A8b`, re-derived from the arriving assessment

### 6.1 `A8a` — does the RATIO depend on any of `R1`–`R5`?

**VERDICT: IT DEPENDS ON NONE OF THEM.** Re-derived from
`derivations/P2-BETAV-RECON-01_scope-assessment.md:340-374`.

**The lines it rests on, each verified present in the repository:**

    CONVENTIONS.md:21          reports results "both as a raw value (this
                               convention) and as convention-independent ratios
                               `β_F/β_B`, `β_V/β_B`, `β_B(ξ)/β_B`"
    CONVENTIONS.md:15          `Δ = −∇² + E`, E entering with a `+`, m²
                               separated out and not counted inside E
    CONVENTIONS.md:16          `a_1 = tr[(1/6)R·𝟙 − E]`, d = 4 fixed
    CONVENTIONS.md:19          `Z_{s=1,m} = det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)`
                               with `E^μ_ν = R^μ_ν` for the vector and `E = 0`
                               for the Stueckelberg scalar
    P2-HK-01:90                heads its ratio section
                               "### Ratios (convention-independent)"
    P2-HK-01:10                repeats the phrase

**And `CONVENTIONS.md:5-6` records that these were fixed before any computation
in `P2-HK-01` and were not adjusted afterwards to reproduce a paper value** —
which is what makes "convention-fixed" a provenance statement and not a
tautology.

**None of the four input lines is any of `R1`–`R5`'s subject.** `R1`'s lattice
Dirac operator, `R2`'s extent, `R3`'s boundary conditions and `R4`'s measure are
absent from every one: the ratio is a continuum Seeley–DeWitt statement about a
vector-plus-scalar determinant structure.

### 6.2 The cancellation mechanism, verified against `CONVENTIONS.md` and not against the assessment

**`R5` is the one that must be handled, and `N` GENUINELY IS IN
`CONVENTIONS.md`.** **I read lines 20 and 29 from the repository directly, as
`A6` requires, rather than accepting the assessment's quotation of them:**

    CONVENTIONS.md:20  | Definition of `Z(m²)` | The induced axis/transverse-traceless
                       (TT) graviton kinetic coefficient, i.e. the coefficient of the
                       induced Einstein–Hilbert term `∫√g R` normalized **per unit `4N`**
                       of fermionic degrees of freedom (`4` spinor components × `N`
                       flavors). Concretely `Z ≡ 1/(16πG_ind)` in the TT channel,
                       expressed per `4N`. The `m²ln m²` piece defines the species
                       coefficient: `Z ⊃ β_s · m² ln m²`. |

    CONVENTIONS.md:29  | Flavor basis | `N` degenerate flavors; the induced coefficient
                       is reported per unit `4N`. |

**Both lines are present and both say what the assessment records.**

**THE MECHANISM: `N` enters through the NORMALISATION OF `Z`, not through
either species' coefficient.** `:20` normalises `Z` itself per unit `4N`, and
`:21` defines `β_s` as the coefficient of `m² ln m²` in that same `Z`. **So the
per-`4N` factor is common to `β_V` and `β_B` alike, identically, and it divides
out of `β_V/β_B`.** The ratio is a quotient of two coefficients of the same
normalised object.

**THE TRAP SENTENCE, transcribed from the arriving assessment (`:373-374`):**

> **An assessment that answered `A8a` "yes, via `R5`" would have found `N` in
> the right document and drawn the wrong conclusion.**

**This is why the mechanism has to land with the verdict.** A later reader who
opens `CONVENTIONS.md`, finds `N` at `:20` and `:29`, sees that `R5` is open, and
concludes the ratio is ruling-dependent **would reverse a correct result using
correct evidence** — every step of that reasoning is sound except the one that
checks *where* `N` enters. **The verdict alone is not checkable; the verdict
plus the mechanism is.**

### 6.3 `A8b` — does the ABSOLUTE or assembled `β_V`, or the induced-`G` normalisation, depend on any of `R1`–`R5`?

**VERDICT: YES — on `R5`, and on `R1`.**

**`R5`, internal multiplicity `N`. The lines:** `CONVENTIONS.md:20` and `:29`,
quoted verbatim above. **`Z` is `1/(16πG_ind)` per unit `4N`, so converting a
per-`4N` coefficient into an induced `G` requires `N`**, and
`P2-CHANNEL-FREEZE-01_phaseA_freeze.md:43` keeps `N` symbolic. **`R5` is open,
so the induced-`G` normalisation is ruling-dependent.**

**`R1`, the canonical kinetic operator AND SPECIES ACCOUNTING. The line:**

    P2-LATTICE-ONTOLOGY-01.md:189   "| Canonical kinetic operator and species
                                     accounting | DELEGATED: D-pre (§4 obligation
                                     binds it) |"

**"Species accounting" is the multiplicity ledger**, and an assembled `β_V` that
sums microscopic species contributions needs to know how many species of each
kind the declared operator carries. **The kinetic-operator dossier's
per-candidate species ledgers make it concrete: the four candidates carry
different species counts.**

**`R2`, `R3` and `R4` are NOT ASSERTED.** The assessment records that a lattice
extraction of an absolute `β` plausibly touches the extent and the measure, that
it did not find lines establishing it, and that `A8b` asks for lines — **so
those three are reported as NOT ESTABLISHED rather than as absent.** See `§7.3`.

### 6.4 Which verdict the parallel-or-serial conclusion rests on

**IT RESTS ON `A8a`, AND ON `A8a` ALONE.**

**`A8a` returns no dependence, so the ratio is convention-fixed and a clean-room
pipeline can be built and checked against it while `R1`–`R5` stay open — TWO
PARALLEL LINES.**

**`A8b`'s dependence does not change that answer.** The assembled quantity's
dependence is not the ratio's, and projecting it back onto the ratio is exactly
the error the two-verdict structure exists to prevent. **What `A8b` constrains
is a different deliverable — an absolute induced `G` — which the `RECON-01` gate
does not ask for.**

## 7. `A7` — the three unresolved items, reported and NOT resolved

### 7.1 `1a` — the sign of the `β_V/β_B` anchor

**MEASURED BY READING THE BYTES.** I enumerated every non-ASCII codepoint on
each line rather than displaying filtered text, because the character in dispute
is `U+2212 MINUS SIGN` and a `[:print:]`-class filter deletes it — **which is
what happened to the Researcher, per the specification's `§11`.**

**The three anchors, signs preserved:**

    GATES.md:751     `β_V/β_B = −(k+2)` (from `P2-HK-01`), compared only at the end.
                     non-ASCII on the line: β U+03B2, − U+2212 MINUS SIGN

    GATES.md:757     For the reconstruction itself: stuck at `−3` ∀k ⟹ the new
    GATES.md:758     pipeline is degenerate (a bug); drift toward `−5` at heavy
                     mass ⟹ longitudinal artifact.
                     non-ASCII: − U+2212 MINUS SIGN on both lines

    P2-HK-01:95      β_V/β_B    = (K/4)/(−K/12)   = −3
                     non-ASCII: β U+03B2, − U+2212 MINUS SIGN

    RECON-B0 spec    `β_V/β_B = (k+2)` at :60, :117, :226; `(k+2)` at :113, :374,
    (as landed)      :384; kill values `3` and `5` at its §3 question five.
                     non-ASCII on those lines: β U+03B2, dashes U+2013/U+2014.
                     NO U+2212 ANYWHERE. UNSIGNED.

**THE REPOSITORY IS CONSISTENT AT MINUS in both places. The unsigned form is the
`RECON-B0` specification's alone.**

**THIS DISCREPANCY BLOCKS `RECON-01`'S PRE-REGISTRATION.** A blind comparison
whose target sign is undecided is not a blind comparison: a pipeline returning
`+3` could be read as a sign-convention artefact or as a failure, **and that
reading would be made after seeing the number** — which is the one thing
blinding exists to prevent. **Both kill criteria are sign-specific too: "stuck
at `−3`" and "stuck at `3`" are different tests**, and a pipeline that sat at
`+3` would satisfy neither as written while plainly being degenerate.

**I did not resolve it.** No value was recomputed and no sign was chosen; the
reconciliation is its own task and this one does not scope it.

**One refinement, measured, that narrows what actually lands.** **Both arriving
science artifacts carry the SIGNED form and both record the discrepancy
themselves:**

    assessment:29,43,48,340,460,559   all write `−(k+2)` with U+2212
    assessment:35-36, 432-433         quote the kill criteria as `−3` and `−5`
    assessment:48-51                  "The gate writes the anchor as `−(k+2)` and
                                      the kill criteria as `−3` and `−5`. The
                                      specification governing this assessment
                                      writes them unsigned … No value is
                                      recomputed here and the discrepancy is
                                      reported, not adjudicated."
    report:96,107,112,279,465,1124    same, and §16.2 carries it as a finding

**So the landed scientific record is signed, and the unsigned form is confined
to one specification, which the two artifacts alongside it explicitly flag.**
**That does not unblock `RECON-01`** — the specification is on `main` either way
and a pre-registration must name one sign — **but it means the repository is not
acquiring an unsigned anchor in its derivations.**

### 7.2 `1b` — `CONVENTIONS.md:24` freezes `r = 1`; `D-1c`'s `R1` treats `r` as unfrozen

**BOTH ANCHORS, QUOTED AS MEASURED.**

**The freeze:**

    CONVENTIONS.md:24   | Lattice regularization | Hypercubic lattice, spacing `a`
                        (`a ≡ 1` in lattice units), Brillouin zone `p_μ ∈ (−π, π]`.
                        Free-field lattice momenta: `p̂² = Σ_μ 4 sin²(p_μ/2)`
                        (naive/scalar), `s̄_μ = sin p_μ`, Wilson term
                        `W(p) = r Σ_μ (1 − cos p_μ)` with Wilson parameter `r = 1`. |

**The treatment as unfrozen:**

    P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md:89
        R1  CONTROLS  W8  the Wilson parameter r
    same:171
        R1   W8 W9 n8 k7 s9                    5

    and the datum W8 rests on, in D-1b:
    P2-LATTICE-MICROSPEC-01_rp-gap-classification.md:103
        | W8 | `r` — `FAIL` (programme value unfrozen) | `UD` |
    same:216
        | Wilson parameter `r` | W8 |
        `P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md:169-171` —
        *"the value of `r` as a canonical choice — `r = 1` is what the exploratory
        script uses, not something the repository freezes"* | VERIFIED UNFROZEN |

    and the dossier line itself:
    P2-LATTICE-MICROSPEC-01_kinetic-operator-dossier.md:169-171
        **NOT ESTABLISHED for this candidate:** the value of `r` as a canonical
        choice — `r = 1` is what the exploratory script uses, not something the
        repository freezes; the interacting fate of the lifted branches.

**The conflict is sharp and it is between LANDED artifacts.** `CONVENTIONS.md`,
the dossier, `D-1b` and `D-1c`'s ledger are all present at
`refs/remotes/origin/main` — I confirmed each with `git cat-file -e`. **The
dossier's wording is the part that collides directly: it says `r = 1` is "not
something the repository freezes", and `CONVENTIONS.md:24` is repository content
that freezes it.**

**I DID NOT ADJUDICATE IT.** I did not decide which artifact is right, did not
edit either, and did not revise any count.

**What it would imply if resolved toward `CONVENTIONS.md`, stated as a
consequence to be checked by whoever adjudicates it and NOT as a conclusion of
this task:** the ledger's `§6.2` records that **`R1` groups four quantities —
`r`, the mass/hopping domain, `M_0`, and the staggered phases — under one
datum**, and `§6.2` names that grouping as the one the ledger's five-node figure
is most sensitive to. **If `r` were removed from `R1`'s controlled set, `R1`'s
constituent count and its `CONTROLS` count of five would both change, and the
25-occurrence decomposition at `§3.1` would have to be re-derived.** **Whether
any of that follows is for the adjudicating task to determine; nothing here
establishes that it does.**

### 7.3 `1c` — `A8b`'s verdict is a LOWER BOUND

**`R5` and `R1` are ESTABLISHED as dependencies of the assembled quantity, each
on named lines. `R2`, `R3` and `R4` are NEITHER ESTABLISHED NOR EXCLUDED.**

**Confirmed by search, and the search is reported positionally rather than as a
count, because a count would be wrong.** A grep for `two of five`, `2 of 5`,
`two out of five`, `2/5` and `depends on exactly two` over this report returns
**FOUR matching lines, and every one of them is either the search itself or a
denial**: two are the two lines this paragraph spends printing the pattern, and
two are `§18.4`'s, which state the prohibition and describe the counterfactual.
**NOT ONE OF THEM ASSERTS `A8b`'s VERDICT AS A COUNT OUT OF FIVE**, which is
what `A7` asks me to confirm. `§6.3` states the non-assertion for `R2`, `R3` and
`R4` explicitly on its own line.

**I record the method because a bare count here would have been a false
negative** — "zero hits" is what a report that never mentioned the hazard would
say, and it is not what this one can say. **`§15.10` documents the same hazard in
the checker's output; this is the same trap sprung on my own text.**

**"Depends on `R5` and `R1`" is a floor, not a tally**, and reading it as a tally
would convert an honest absence of evidence into a finding of independence.

## 8. `A8` — the component inventory, re-derived

**Re-derived from the arriving assessment's `§4` table row by row, not taken
from commit 4's message.**

    N_both      2      IMPLEMENTATION + SPECIFICATION   components 7, 8
    N_impl      0      IMPLEMENTATION ONLY              none
    N_spec      7      SPECIFICATION ONLY               components 1,2,3,4,5,6,9
    N_neither   1      NEITHER                          component 10
               --
    N_total    10      2 + 0 + 7 + 1 = 10               MEASURED, and it reconciles

**THE TWO USABLE COMPONENTS, NAMED:**

    component 7   flat-limit validation against the Proca eigenstructure
                  implementation: scripts/betav_decomp_check.py, which records the
                  flat eigenstructure and propagator eigenvalues from actual
                  operators and states that it carries no target

    component 8   blind two-stage harness: frozen output, external digest,
                  deferred comparison
                  implementation: scripts/P2-BETAV-CAMPAIGN/harness_compute.py
                  and compare.py — no target numbers, frozen JSON with an
                  external digest, all comparison deferred

**THE EXISTENCE CLASSIFICATION IS REPORTED SEPARATELY FROM THE CLEAN-ROOM REUSE
CLASSIFICATION, and the arriving assessment says so at its `:471`: "This is
SEPARATE from `§2`'s reuse classification."** They are different questions —
`§2` asks what role a script could play, `§4` asks whether a component exists at
all — and the assessment's `§4.2` is where they interact: **three components
(1, 2 and 5) have code in the repository and are still counted
`SPECIFICATION ONLY`, each for a stated reason** (clean-room contamination from
the recovered pipeline, `CIRC-01`'s finding that `boson_loop`'s scalar is not the
Proca longitudinal eigenfactor, and the pre-registration requirement that keeps
targets out of code). **So the `SPECIFICATION ONLY` seven contains three
components that DO have code** — which is what makes the two classifications
non-interchangeable rather than merely differently named.

## 9. `A9` — nothing built, nothing run

**SEARCH, as specified: the artifact, the report and the commit messages, for
any numerical value claimed as NEWLY COMPUTED RECONSTRUCTION PHYSICS OUTPUT —
determinant or eigenvalue results, numerical `h`-derivatives, `β` values, `β`
ratios beyond quotation of the anchor, `k`-scan outputs. Governance and checker
measurements, inventory counts, line numbers, SHAs and timestamps are expressly
excluded.**

**Two complementary passes were run, because either alone is defeatable.**

**Pass 1, by vocabulary** — `logdet`, `determinant value`, `eigenvalue`,
`eigenstructure`, `h-derivative`, `Richardson`, `k-scan`, `tolerance`,
`computed`, `I ran`, `printed`, `returned the value` and related terms, over all
six in-range artifacts. **25 candidate lines in the assessment, 25 in the report,
9 in the RECON-B0 specification, 1 in this specification, 2 in each review.**

**Pass 2, by numeric literal** — a regex for decimal literals and
exponent-notation values over the two arriving science artifacts. **23 hits in
the assessment, 71 in the report.**

**MEASURED FINDING: ZERO newly computed reconstruction physics values, in all
three places searched.** Every hit resolves to one of:

    section numbers             2.1 … 4.3, 15.1 … 19.7 — the bulk of both passes
    line and length counts      "173 lines", "GATES.md:751"
    version numbers             Python 3.11.15, pytest 9.1.1, numpy 2.4.6,
                                sympy 1.14.0, ruff 0.15.8
    SHA fragments               see the method note below
    a test duration             "324 passed, 2 deselected in 42.55 s"
    quoted repository values    `~1e-7` from GATES.md:404; the propagator FORMS
                                `1/(p̂²+m²)` and `1/m²`; the anchor `−(k+2)` and
                                kill values `−3`, `−5` as quotations
    component names             "Γ_k = ½ logdet Δ⁽¹⁾ − (k/2) logdet Δ⁽⁰⁾" is the
                                NAME of component 3, a specification of what must
                                be built — not a value
    denials                     "NOTHING WAS BUILT AND NOTHING WAS COMPUTED";
                                "I ran none of them, including to see what they
                                print"; "No value is recomputed here"

**Commit messages: no numeric value of any kind in any of the seven in the
range.** Commit 4's arriving message reads *"ten components, two usable, and the
ratio is ruling-independent"* — **an inventory count and a verdict, both
expressly excluded from this search.**

**METHOD NOTE, disclosed because it inflates a naive count.** My literal regex
included `\d+e[+-]?\d+` to catch exponent notation, and that pattern matches
substrings of hexadecimal SHAs: `9e1` inside
`21195f71c2aea936ec8f55727889def7970ea9e1`, `49e21210` inside a checker digest,
`0e54` inside `d64cd912ca9ff78a85787f0e54f345f474cdb192`. **Roughly forty of the
report's seventy-one hits are of this kind.** A report that stated the raw hit
count as a finding would have claimed dozens of exponent-notation physics values
in a document that contains none. **Each hit was resolved individually; the
count was not.**

## 10. `A10` — scope, at TWO heads

**MEASURED at commit 3, the merge — 6 ADDITIONS, 0 MODIFICATIONS:**

    A  derivations/P2-BETAV-RECON-01_scope-assessment.md
    A  reports/2026-08-17T1105Z_recon-b0-scope.md
    A  reviews/chatgpt/2026-08-17T1105Z_recon-b0-scope.md
    A  reviews/chatgpt/2026-08-17T1151Z_integrate-recon-b0.md
    A  specs/2026-08-17T1105Z_recon-b0-scope.md
    A  specs/2026-08-17T1151Z_integrate-recon-b0.md

    status tally   6 A, 0 M, and no other status

**INTENDED at commit 4, the final head — 7 additions, 0 modifications**, the
above plus `reports/2026-08-17T1151Z_integrate-recon-b0.md`, this file.
**MEASURING THAT IS POST-REPORT EVIDENCE AND NOTHING HERE CLAIMS TO HAVE DONE
IT.**

**Which figure was measured at which head: 6/0 MEASURED at commit 3
`3bdbaa57…`; 7/0 INTENDED at commit 4, unmeasured at the time of writing.**

**THE ARRIVING COUNTS, REPORTED SEPARATELY AS §4 A10 REQUIRES:**

    arriving PATH count       4
    arriving ADDITION count   4
    do they coincide?         YES, at four

**They coincide because the source branch added four paths and modified none.**
**Stating them separately still matters: they are different quantities, and a
source that had modified an existing file would have made the path count exceed
the addition count** — at which point a single figure would have hidden a
modification inside an "arriving paths" total.

**The frozen manifest's `append_only: DECISION_LOG.md` is a
CHECKER-CONFIGURATION DECLARATION, NOT AN AUTHORISATION TO WRITE THAT FILE.**
**`DECISION_LOG.md` was not written, and the two readings did not appear to
conflict, so `§8` was not invoked.** The checker's `P3` confirms it: base and
head both 89541 bytes, `base_is_byte_prefix_of_head: true`, zero deleted lines,
no commit with deletions.

**The `{HHMM}Z` token.** I measured UTC before writing anything:
`2026-08-17T11:51:38Z`, giving the token `1151Z`. **Commit 1's recorded time is
`2026-08-17 11:51:54 +0000` — the same minute.** All three authored paths carry
`1151Z`.

## 11. `A11` — which merge case, stated BEFORE the blob comparisons

**THE MERGE-BASE IS THE EVIDENCE BASE, so no commit on `main` could have touched
an arriving path.**

    merge-base(parent 1, parent 2)   ece34f7bacbbee00efa0fecf0be644d593eed72f
    evidence base                    ece34f7bacbbee00efa0fecf0be644d593eed72f
    identical                        YES
    commits on origin/main after the base   0

**`main` has not moved since the base, so the merge cannot be the case where an
arriving path was independently edited on `main` and silently resolved.** That
case is excluded by the ref topology, before any blob is compared — and the
comparisons below are therefore confirmations, not the argument.

**THEN the four blob comparisons:**

    derivations/P2-BETAV-RECON-01_scope-assessment.md
        at base   ABSENT (git rev-parse fatal: path does not exist)
        at source b2c6c0b3483d655007fb5dc56e0098f77b096e25
        at head   b2c6c0b3483d655007fb5dc56e0098f77b096e25   SOURCE == HEAD

    reports/2026-08-17T1105Z_recon-b0-scope.md
        at base   ABSENT
        at source 00431e520dcbc8dc3e414b392594931622893bc4
        at head   00431e520dcbc8dc3e414b392594931622893bc4   SOURCE == HEAD

    reviews/chatgpt/2026-08-17T1105Z_recon-b0-scope.md
        at base   ABSENT
        at source 4b564e98a28222d01d9ca7c8651946d916a97bda
        at head   4b564e98a28222d01d9ca7c8651946d916a97bda   SOURCE == HEAD

    specs/2026-08-17T1105Z_recon-b0-scope.md
        at base   ABSENT
        at source 829dbc2f829da0c2494697d81f874ed81dafde4e
        at head   829dbc2f829da0c2494697d81f874ed81dafde4e   SOURCE == HEAD

**All four arrive byte-identical to the source, and none existed at the base.**
**Everything arriving by merge is integrated exactly as reviewed; no arriving
path was renamed.**

## 12. `A12` — nothing existing changed

**Every path present at the evidence base, blob-compared at the head:**

    paths at the evidence base   460
    paths at the head            466
    COMPARED                     460
    IDENTICAL                    460
    DIFFERING                      0
    missing at the head            0
    new at the head                6   — exactly A10's six additions

**Named confirmations, each a blob comparison and not an absence of a diff
line:**

    GATES.md                                    1 path    unchanged
    CONVENTIONS.md                              1 path    unchanged
    derivations/P2-BETAV-*                      4 paths   all unchanged
    P2-LATTICE-MICROSPEC-01 artifacts           7 paths   all unchanged
    registers: docs/BRANCHING_POLICY.md,
               DECISION_LOG.md                  2 paths   both unchanged
    scripts/                                   60 paths   all unchanged
    tests/                                     21 paths   all unchanged
    results/                                   69 paths   all unchanged

**The four `P2-BETAV-*` artifacts, named:** `P2-BETAV-ASSEMBLY-01_bookkeeping_regression.md`,
`P2-BETAV-CAMPAIGN_prereg.md`, `P2-BETAV-CIRC-01_determinant-decomposition.md`,
`P2-BETAV-RECON-01_cleanroom_reconstruction.md`.

**The microspec artifacts, named:** `kinetic-operator-dossier`,
`plaquette-provenance`, `rp-dependency-ledger`, `rp-gap-classification`,
`rp-literature-coverage`, `selection-discriminants`, `tm-rp-scope`.

**MEASUREMENT CORRECTION TO THE SPECIFICATION'S COUNT.** `§4 A12` asks me to
confirm "all six microspec artifacts". **There are SEVEN at the evidence base,
and all seven are unchanged.** The confirmation the criterion asks for holds and
holds more widely than stated; **I report the count I measured rather than the
count I was given.** See `§19.4`.

## 13. `A13` — gate invariants and pins

**All four, MEASURED at commit 3, each read SCOPED to its own gate section:**

    (1)  ^## P2- section count                    14        expected 14   MATCH

    (2)  P2-PHASE-01, section GATES.md:971-1108
         GATES.md:973    Status: PROPOSED                                 MATCH

    (3)  both prerequisites SATISFIED
         GATES.md:1011   Artifact state: **ADOPTED**. Prerequisite state:
                         **SATISFIED**,
         GATES.md:1036   Artifact state: **ADOPTED**. Prerequisite state:
                         **SATISFIED**.

    (4)  both pins recomputed
         GATES.md:1017   4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
         sha256 derivations/P2-PHASE-01_microscopic_parameter_domain.md   identical
         GATES.md:1040   e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
         sha256 derivations/P2-PHASE-01_input_admissibility_contract.md   identical

**The scoped read is the point.** `SATISFIED` and `Status:` both occur in more
than one gate section, and `P2-BETAV-CIRC-01`'s section alone contains a
`Status stays **SPECIFIED**` line at `:425` about a *different* gate. An
unscoped grep would return a status line belonging to something else.

**THE THREE `BETAV` GATE STATUSES, each read scoped to its own section:**

    P2-BETAV-RECON-01   GATES.md:725-789   :727  Status: PROPOSED (not run;
                        distinct from the historical circularity question)
    P2-BETAV-CIRC-01    GATES.md:328-597   :330  Status: RUN
    P2-BETAV-01         GATES.md:207-264   :209  Status: PROPOSED (deferred —
                        not computed this sweep)

**NONE CHANGED, and the strongest evidence is not the string comparison:
`GATES.md` is BLOB-IDENTICAL between the evidence base and commit 3** (`§12`),
so no status line in it could have changed. **`RECON-B0` landing an assessment
does not advance the `RECON-01` gate, and `CIRC-01` stays `RUN` — neither passed
nor failed.**

## 14. `A14` — superseded branches not merged

**Six separate `git merge-base --is-ancestor` invocations, six separate exit
statuses. BEFORE the advance, against `refs/remotes/origin/main`:**

    52f65117   exit 1     not an ancestor
    ebd531ab   exit 1     not an ancestor
    40168469   exit 1     not an ancestor
    7146a093   exit 1     not an ancestor
    10c260b9   exit 1     not an ancestor
    d64cd912   exit 1     not an ancestor

**And against this task's head, commit 3 — all six also exit 1**, so the merge
did not introduce any of them.

**The checker's `P4` independently recomputed all six**, reporting
`is_ancestor_of_head: false` and `object_present: true` for each, and names them:
`fix/pi-decisions-and-deferred`, `fix/pi-decisions-v2`,
`governance/supply-protocol-v2`, `governance/supply-protocol-and-superseded`,
`review/role-model-and-executors`, `gate/p2-land-diquark-line`.

**AFTER the advance is POST-REPORT EVIDENCE.** The re-run is required by `§5`
and is returned to the Reviewer, not written here. **Since the landing is a
fast-forward to commit 4 and commit 4's only parent is commit 3, no superseded
commit can become an ancestor by it — but that is an argument, and the criterion
asks for six measurements, which will be made.**

## 15. `A15` — the checker over this task's own range, MEASURED at commit 3

    base   ece34f7bacbbee00efa0fecf0be644d593eed72f
    head   3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8   (commit 3)

    run 1 INCLUSIVE   exit 0   PASS   318 lines   sha256 647af8f349ac7acd358dd5662361cd52982988018f0df518fd865bb22c573c42
    run 1 EXCLUSIVE   exit 0   PASS   318 lines   sha256 339b163a629a266dc0363711c89326f2c4354b0cbd2df737ace19113f82a2ec7
    run 2 INCLUSIVE   exit 0   PASS   295 lines   sha256 0e145d3544a08f780409797c65d08b369180589fbb914d4b8e0e0c19af03ded3
    run 2 EXCLUSIVE   exit 0   PASS   295 lines   sha256 08486bcef9b26ce6e97cf0276f03e6fcc1d28f11fa08f19b0b876ff07e203ebb

    stderr empty in all four.

    P1 PASS   P2 PASS   P3 PASS   P4 PASS   P5 PASS
    P6 PASS   P7 PASS   P8 PASS   P9 PASS

    overall PASS in all four.
    commits_in_range 7      commits_on_first_parent_line 3

**Every one of the nine properties is `PASS`, and NONE is `NOT_APPLICABLE` —
the first time in this line of tasks that all nine were exercised.** A
machine-read tally of every `status` field in `RUN 2`'s output returns
**26 × `PASS` and nothing else.**

**`commits_in_range` is 7 and the first-parent line is 3.** The merge brings the
source's four commits into the range while leaving this task's own line at three
— the distinction the prospectivity `scope_note` exists to make.

### 15.1 What `RUN 1` did — TWO specifications in range

**MEASURED: `RUN 1`'s default subject selection selected BOTH specifications**,
this task's and the one arriving by merge:

    specs/2026-08-17T1105Z_recon-b0-scope.md
        stated: 4 additions, 0 modifications    counted 4 / 0    parse OK
        counted_set holds the literal {HHMM}Z placeholders, e.g.
        "reports/2026-08-XXT{HHMM}Z_recon-b0-scope.md"

    specs/2026-08-17T1151Z_integrate-recon-b0.md
        stated: 7 additions, 0 modifications    counted 7 / 0    parse OK

**`RUN 1` and `RUN 2` are NOT byte-identical here — 318 lines against 295 — and
they differ in exactly three places**, verified by `diff`: `P1`'s second
evidence entry, and the `specification_paths_read` list in `P3` and in `P7`.
**In the source task the two runs coincided because only one specification was
in range; here they genuinely diverge, and the divergence is the arriving
specification.**

**`RUN 2` names the subject and is stop-governing. `RUN 1` discovers it and
governs nothing.**

### 15.2 The `C3` multi-specification residual — a NEW half of the diagnosis

**MEASURED: `DECLARATION_CONFLICT` appears ZERO times as a status in all four
outputs.** **`RUN 1` read TWO specifications and did not raise it.**

**The reason is new to this session's record, and it is not the reason from the
earlier integration tasks.** In tasks 4, 6 and 8 two specifications were in
range and their declarations AGREED, so no conflict could arise. **Here the two
specifications DISAGREE on their stated totals — 4 additions against 7 — and
there is still no conflict, because the totals are not what the conflict
mechanism reads.**

    what _declarations_from_specs compares    append_only_paths, authorised_modified_gates
    RECON-B0 spec                             ["DECISION_LOG.md"], []
    this specification                        ["DECISION_LOG.md"], []
    difference                                NONE → no conflict

    what P1 compares                          each specification's own 'stated:'
                                              total against its OWN manifest block
    result                                    4/0 vs 4/0 and 7/0 vs 7/0, independently

**So differing totals are structurally incapable of raising
`DECLARATION_CONFLICT`, and `P1` is per-specification by construction.** **The
residual remains unregistered and is unchanged**; what this task adds is the
demonstration that the earlier "no conflict because they agreed" observation was
about the wrong quantity — they agreed on the keys that matter and disagreed on
the ones that do not.

### 15.3 `declared_source`, `P7`, and the four other properties

    P1   PASS   declared_source field: absent from P1 (it reads each spec directly)
    P3   PASS   declared_source: specification   declared: ['DECISION_LOG.md']
                supplied_by_config: ['DECISION_LOG.md']   — they agree
    P7   PASS   declared_source: specification   declared: []   supplied_by_config: []
                section_count_base 14   section_count_head 14   raw_heading_count_head 14
                added_sections []   removed_sections []   unauthorised_changed []

**`P7` REPORTS FOURTEEN SECTIONS. `PASS` AT ZERO WOULD HAVE BEEN A STOP** — a
gate file that parsed to no sections at all would satisfy "nothing changed"
vacuously, which is why the count and not just the verdict is reported.

    P2   PASS   first_review_commit eb4bad24…  first_work_commit 3bdbaa57…
                out_of_scope []  — the review precedes the work
    P8   PASS   specification_is_first_commit: true
                first_commit_paths ['specs/2026-08-17T1151Z_integrate-recon-b0.md']
    P9   PASS   heading_present: true for reports/2026-08-17T1105Z_recon-b0-scope.md

**`P9` is already `PASS` at commit 3, and not because of this report.** The
merge brings the source's report into the range, and that report carries the
mandated `Stops and clarifications` heading. **At commit 4 `P9` will have a
second subject — this file — and measuring that is post-report evidence.**

### 15.4 `P5`'s state at commit 3, and what to expect at commit 4

    at commit 3   P5 PASS
                  merge 3bdbaa57…, recomputed_parent_1 eb4bad24…,
                  recomputed_parent_2 e219ae0e…,
                  recomputed_merge_base ece34f7b…,
                  merge_base_equals_parent_1 false,
                  compared_to_recorded UNAVAILABLE

    at commit 4   INTENDED expectation: PASS, unchanged.

**A PRECISION NOTE ON THE SPECIFICATION'S `A15-final` EXPECTATION.** `§4` says
to expect `P5` to change state, "the merge giv[ing] it a subject where the
source task's range had none". **The state change is real, but it happens at
COMMIT 3, not between commit 3 and commit 4.** `P5` was `NOT_APPLICABLE` in the
source task's range because that range contained no merge; it is `PASS` here
because commit 3 *is* the merge. **Commit 4 is an ordinary report commit and
adds no second merge, so `P5` has nothing left to change into.** The comparison
`§10` asks for will therefore read `PASS` against `PASS`, and the state change
the specification anticipated is the one already recorded above. **I report this
rather than re-running at commit 4 hoping for a transition that cannot occur.**

### 15.5 `RUN 1` config, verbatim — observational, governs nothing

    {
      "base": "ece34f7bacbbee00efa0fecf0be644d593eed72f",
      "head": "3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8",
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

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

### 15.6 `RUN 2` config, verbatim — stop-governing

    {
      "base": "ece34f7bacbbee00efa0fecf0be644d593eed72f",
      "head": "3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8",
      "specification_paths": [
        "specs/2026-08-17T1151Z_integrate-recon-b0.md"
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

The `EXCLUSIVE` reading is the same file with `"inclusivity": "EXCLUSIVE"`.

**No value in either config is one I chose**, and **neither the config nor this
specification's declarations were adjusted to make `RUN 2` pass**. **`RUN 2`
passed on its first invocation at both readings.**

### 15.7 `RUN 1` output, verbatim, `INCLUSIVE` reading

    {
      "base": "ece34f7bacbbee00efa0fecf0be644d593eed72f",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8",
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
                "derivations/P2-BETAV-RECON-01_scope-assessment.md",
                "reports/2026-08-XXT{HHMM}Z_recon-b0-scope.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_recon-b0-scope.md",
                "specs/2026-08-XXT{HHMM}Z_recon-b0-scope.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-17T1105Z_recon-b0-scope.md",
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
                "derivations/P2-BETAV-RECON-01_scope-assessment.md",
                "reports/2026-08-17T1105Z_recon-b0-scope.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-recon-b0.md",
                "reviews/chatgpt/2026-08-17T1105Z_recon-b0-scope.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-recon-b0.md",
                "specs/2026-08-17T1105Z_recon-b0-scope.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-recon-b0.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-17T1151Z_integrate-recon-b0.md",
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
                "commit": "960b0629691449c528c232175021c6180e15ead2",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "eb4bad24185adc7f267de0b3138e33af38786966",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8",
                "work_paths": [
                  "derivations/P2-BETAV-RECON-01_scope-assessment.md"
                ]
              }
            ],
            "first_review_commit": "eb4bad24185adc7f267de0b3138e33af38786966",
            "first_work_commit": "3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8",
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
              "specs/2026-08-17T1105Z_recon-b0-scope.md",
              "specs/2026-08-17T1151Z_integrate-recon-b0.md"
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
              "merge": "3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "ece34f7bacbbee00efa0fecf0be644d593eed72f",
              "recomputed_parent_1": "eb4bad24185adc7f267de0b3138e33af38786966",
              "recomputed_parent_2": "e219ae0e5e2a740c9212795599bb37460ba8d5bf",
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
              "commit": "960b0629691449c528c232175021c6180e15ead2",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "eb4bad24185adc7f267de0b3138e33af38786966",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "42b93893f17154867777f17b823cfb86743e2843",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "0643f31796de1849df6a48ebf69010fe5c43fb44",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "21195f71c2aea936ec8f55727889def7970ea9e1",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "e219ae0e5e2a740c9212795599bb37460ba8d5bf",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8",
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
              "specs/2026-08-17T1105Z_recon-b0-scope.md",
              "specs/2026-08-17T1151Z_integrate-recon-b0.md"
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
            "first_commit": "960b0629691449c528c232175021c6180e15ead2",
            "first_commit_paths": [
              "specs/2026-08-17T1151Z_integrate-recon-b0.md"
            ],
            "reports_added": [
              "reports/2026-08-17T1105Z_recon-b0-scope.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-17T1151Z_integrate-recon-b0.md",
              "reviews/chatgpt/2026-08-17T1105Z_recon-b0-scope.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-17T1151Z_integrate-recon-b0.md",
              "specs/2026-08-17T1105Z_recon-b0-scope.md"
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
              "path": "reports/2026-08-17T1105Z_recon-b0-scope.md",
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

### 15.8 `RUN 2` output, verbatim, `INCLUSIVE` reading

    {
      "base": "ece34f7bacbbee00efa0fecf0be644d593eed72f",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8",
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
                "derivations/P2-BETAV-RECON-01_scope-assessment.md",
                "reports/2026-08-17T1105Z_recon-b0-scope.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-recon-b0.md",
                "reviews/chatgpt/2026-08-17T1105Z_recon-b0-scope.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-recon-b0.md",
                "specs/2026-08-17T1105Z_recon-b0-scope.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-recon-b0.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-17T1151Z_integrate-recon-b0.md",
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
                "commit": "960b0629691449c528c232175021c6180e15ead2",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "eb4bad24185adc7f267de0b3138e33af38786966",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8",
                "work_paths": [
                  "derivations/P2-BETAV-RECON-01_scope-assessment.md"
                ]
              }
            ],
            "first_review_commit": "eb4bad24185adc7f267de0b3138e33af38786966",
            "first_work_commit": "3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8",
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
              "specs/2026-08-17T1151Z_integrate-recon-b0.md"
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
              "merge": "3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "ece34f7bacbbee00efa0fecf0be644d593eed72f",
              "recomputed_parent_1": "eb4bad24185adc7f267de0b3138e33af38786966",
              "recomputed_parent_2": "e219ae0e5e2a740c9212795599bb37460ba8d5bf",
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
              "commit": "960b0629691449c528c232175021c6180e15ead2",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "eb4bad24185adc7f267de0b3138e33af38786966",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "42b93893f17154867777f17b823cfb86743e2843",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "0643f31796de1849df6a48ebf69010fe5c43fb44",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "21195f71c2aea936ec8f55727889def7970ea9e1",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "e219ae0e5e2a740c9212795599bb37460ba8d5bf",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8",
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
              "specs/2026-08-17T1151Z_integrate-recon-b0.md"
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
            "first_commit": "960b0629691449c528c232175021c6180e15ead2",
            "first_commit_paths": [
              "specs/2026-08-17T1151Z_integrate-recon-b0.md"
            ],
            "reports_added": [
              "reports/2026-08-17T1105Z_recon-b0-scope.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-17T1151Z_integrate-recon-b0.md",
              "reviews/chatgpt/2026-08-17T1105Z_recon-b0-scope.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-17T1151Z_integrate-recon-b0.md",
              "specs/2026-08-17T1105Z_recon-b0-scope.md"
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
              "path": "reports/2026-08-17T1105Z_recon-b0-scope.md",
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

### 15.9 The `EXCLUSIVE` readings

**MEASURED by `diff`: `RUN 2`'s two readings differ at line 291 of 295,
`"inclusivity": "INCLUSIVE"` → `"EXCLUSIVE"`. One line, nothing else.** `RUN 1`
behaves the same way. **`commits_out_of_scope` is empty and `commits_in_scope`
is 7 in all four**, so the prospectivity boundary excludes nothing in this range
under either reading.

### 15.10 A grep hazard in the checker's own output

**A whole-file grep of any of the four outputs returns `NOT_DECLARED` once and
`NOT_PARSEABLE` twice.** Both are members of `NON_GREEN`, so a count taken that
way reads as three non-green findings and an `INCOMPLETE` verdict.

**They are neither.** Read positionally, both tokens occur only in definitional
prose:

    line 7    "overall_note": "INCOMPLETE is non-zero deliberately: NOT_DECLARED and
              NOT_PARSEABLE mean a subject was missing, and a missing subject must
              never read as a pass."
    line 11   P1's "does_not_establish": "… a specification declaring no total is
              reported NOT_PARSEABLE, which is not a pass …"

**Every actual `status` value in the output is `PASS`, 26 of them.** **This is
the fourth instance in this line of tasks of the same hazard — an artifact that
defines its own vocabulary makes a grep count the definitions** — and the first
where the artifact is the governance tool's output rather than a derivation.
**The lesson generalises: the checker's output must be parsed, not grepped.**

## 16. `A16`, `A17` — validators and hygiene

**`A16`, MEASURED at commit 3, exit status 0:**

    324 passed, 2 deselected      in 36.22 s

**Expected 324 and 2; measured 324 and 2.**

**`A17`, MEASURED on commits 1–3. Commit 4 is post-report evidence:**

    commit 1   960b0629   spec: integrate and land the clean-room reconstruction scope assessment
               body empty      trailer hits 0      author date == commit date, not amended
    commit 2   eb4bad24   review: pre-execution review for the reconstruction scope integration
               body empty      trailer hits 0      author date == commit date, not amended
    commit 3   3bdbaa57   merge: integrate the clean-room reconstruction scope assessment
               body empty      trailer hits 0      author date == commit date, not amended

**MEASURED over the whole range: a scan for `Co-Authored-By`, `claude.ai/code`,
`Generated with`, `Claude-Session` and `noreply@anthropic` returns ZERO.**

**`P6` independently confirms it for all SEVEN commits in the range** — the
three authored here and the four arriving by merge — reporting `matches: []` for
each.

**Rule 20 binds this task and was NOT exercised.** No message needed repair, so
none was amended. **No force-push, no branch deletion, no history rewrite, no
squash and no rebase. Commit 3 is a real merge commit with two parents,
`--no-ff`.**

**Commits, MEASURED:**

    commit 1   960b0629691449c528c232175021c6180e15ead2   specs/2026-08-17T1151Z_integrate-recon-b0.md
    commit 2   eb4bad24185adc7f267de0b3138e33af38786966   reviews/chatgpt/2026-08-17T1151Z_integrate-recon-b0.md
    commit 3   3bdbaa57dcdd10bb61c40d856a0024b3fac0a3a8   merge of e219ae0e…, --no-ff

**Commit 4's message, INTENDED:**

    report: the ratio line is unblocked and three items arrive unresolved

## 17. The landing — INTENDED, and entirely post-report

**§7's landing has NOT happened at the time this report is committed, and
nothing here claims otherwise.**

    INTENDED   verify --is-ancestor commit-3 origin/main-target BEFORE the push,
               and report the exit status as a measurement
    INTENDED   git push origin refs/heads/main, no --force, no --force-with-lease
    INTENDED   read remote main back and confirm it equals commit 4
    INTENDED   confirm science/recon-b0-scope still at e219ae0e…, not deleted,
               not moved
    INTENDED   confirm no other ref was pushed

**The fast-forward is available in principle: `ece34f7b…` is this branch's base
and `origin/main` has not moved from it — 0 commits after the base. IF A
FAST-FORWARD IS NOT AVAILABLE AT THE MOMENT OF THE PUSH, THE TASK STOPS.** That
is a measurement to be made then, not now.

**Only `refs/heads/main` and `science/integrate-recon-b0` will be pushed. No
session branch, no `science/recon-b0-scope`, no `D-1` branch.**

## 18. `§8` — Rule 16 assessment

**Rule 16 is operative. All four junctions are addressed.**

### 18.1 First junction — a parallel line is an available line, not a completed one

**`A8a`'s NO DEPENDENCE means the clean-room `β_V/β_B` RATIO reconstruction line
MAY PROCEED while `R1`–`R5` remain open.** That is the reason this landing
matters: **before it, the programme had one blocked line; after it, it has two,
one of which is not waiting on `D-pre`.**

**IT DOES NOT MEAN THE RECONSTRUCTION WILL SUCCEED, OR THAT THE `RECON-01` GATE
WILL PASS.** The gate is `PROPOSED` and unrun; nothing about a dependency
verdict predicts an outcome.

**Ten components are inventoried. TWO have potentially applicable implementation
plus specification. EIGHT LACK A POTENTIALLY APPLICABLE IMPLEMENTATION — seven
specification-only and one neither.**

**THE EIGHT IS `7 + 1`, AND IT COUNTS COMPONENTS LACKING A USABLE
IMPLEMENTATION, NOT COMPONENTS LACKING BOTH.** **`NEITHER` IS ONE.** An earlier
draft of the governing specification said "eight are neither implemented nor
specified", which contradicts the arriving inventory; the specification as issued
corrects it, and the corrected reading is the one measured in `§8` of this
report.

**A COMPONENT COUNT IS NOT A DIFFICULTY.** Two usable out of ten is not "eighty
percent remaining" in any meaningful unit. The arriving assessment makes the
point against itself at its `§4.3`: **the one component in the `NEITHER` state —
registered regression anchors — is plausibly the cheapest of the ten to
produce.** State does not track effort.

**A PARALLEL LINE IS AN AVAILABLE LINE, NOT A COMPLETED ONE.** Nothing has been
built.

### 18.2 Second junction — the mechanism is what makes the verdict checkable

**The `N`-cancellation mechanism LANDS WITH THE VERDICT, at `§6.2` of this
report, verified against `CONVENTIONS.md:20` and `:29` in the repository.**

**`N` IS IN `CONVENTIONS.md`, AND A READER WHO FINDS IT THERE CAN REVERSE `A8a`
FROM CORRECT EVIDENCE.** The document is right, the line numbers are right, and
`R5` really is open. The only thing such a reader would get wrong is *where* `N`
enters — the normalisation of `Z`, identically for both species — and that is
one inference, not an error of fact.

**SO THE MECHANISM IS WHAT MAKES THE VERDICT CHECKABLE.** A landed verdict
without it is an assertion a diligent reader can contradict with repository
lines; a landed verdict with it is a claim whose refutation requires showing the
cancellation fails. **The trap sentence is transcribed at `§6.2` for exactly
this reason.**

### 18.3 Third junction — the repository now carries a contradiction it did not carry before this line began

**`1b`'s `r = 1` conflict is between TWO LANDED ARTIFACTS.**
**`CONVENTIONS.md:24` FREEZES IT; `D-1c`'s `R1` TREATS IT AS UNFROZEN, resting
on `D-1b:216` and the dossier's `:169-171`.** **Both are on `main`, and I
confirmed each with `git cat-file -e` against `refs/remotes/origin/main`.**

**THIS TASK ADJUDICATES NEITHER.**

**THE REPOSITORY NOW CARRIES A CONTRADICTION IT DID NOT CARRY BEFORE THIS LINE
BEGAN.** `CONVENTIONS.md:24` long predates `D-1`; what `D-1b` and `D-1c` added
was an artifact that asserts, in the opposite direction, that the repository does
not freeze `r`. **The contradiction is a product of the dependency-reduction
line itself, and it is the honest cost of that line's method: `D-1b` classified
from the dossier's own statements without cross-checking `CONVENTIONS.md`.**

**RESOLVING IT MAY CHANGE `D-1c`'S NODE COUNT.** `R1` groups four quantities
under one datum; removing `r` would change that grouping, `R1`'s `CONTROLS`
count of five, and the 25-occurrence decomposition. **Whether it does is for the
adjudicating task; nothing here establishes it, and I did not revise any count.**

### 18.4 Fourth junction — `A8b` is a lower bound

**`R2`, `R3` AND `R4` ARE NEITHER ESTABLISHED NOR EXCLUDED as dependencies of
the assembled quantity.**

**"DEPENDS ON `R5` AND `R1`" MUST NOT READ AS "DEPENDS ON EXACTLY TWO".** The
two are established because lines establish them; the other three are silent
because no line was found either way, and the arriving assessment says so at its
`:405-408`: *"Not asserted for `R2`, `R3`, `R4`. … I did not find lines that
establish it, and `A8b` asks for lines. Reported as not established rather than
as absent."*

**The asymmetry is deliberate and it is the conservative direction.** A future
task that finds `R2` also constrains the assembled `β_V` would be ADDING to a
floor, not overturning a finding. **Had `A8b` been reported as "two of five",
that same discovery would read as a correction to a landed result** — which is
how a lower bound quietly becomes a false ceiling.

## 19. Stops and clarifications

**No stop was declared. Five primary categories, one primary per finding,
secondary findings kept separate, included even where there were none.**

### 19.1 `SPECIFICATION_DEFECT` — the anchor's sign, arriving and unresolved

**The `RECON-B0` specification on `main` writes the anchor and both kill values
UNSIGNED where the gate and `P2-HK-01` write them with `U+2212`.** Measured in
`§7.1`. **This is a defect in a landed specification, not in the specification
governing this task**, which states the discrepancy correctly at its `§1a` and
forbids resolving it. **Reported, not resolved. It blocks `RECON-01`'s
pre-registration.**

**Secondary, and it narrows the exposure:** both arriving science artifacts write
the signed form throughout and each flags the specification's unsigned form
itself. **The landed derivation record is signed.**

### 19.2 `SPECIFICATION_DEFECT` — the microspec artifact count

**`§4 A12` asks for "all six microspec artifacts". There are seven.** Measured
and named in `§12`. **Not a stop:** the criterion's operative requirement is
that they be unchanged, all seven are, and the discrepancy is a count in the
prompt rather than a claim about the repository. **I reported the measured seven
rather than confirming a six I did not find** — the same discipline that applied
when an earlier task's `A1` named a branch that did not exist.

### 19.3 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — first finding: the `r = 1` conflict

**Two landed artifacts contradict each other about whether the repository
freezes the Wilson parameter.** Both anchors quoted in `§7.2`. **This task did
not adjudicate it and was forbidden to.** It is recorded here so that the
adjudicating task inherits both anchors and the consequence to check, rather than
rediscovering them.

### 19.4 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — second finding: the declared environment

**`docs/local/execution_environment.md` declares a WINDOWS environment** —
identity `zeta-3070\codexsandboxoffline`, a Python 3.12 interpreter at a Windows
path, a venv at `C:\p2-validator\venv`. **Every run in this task was on Linux
with Python 3.11.15, so every measurement here was taken in an UNDECLARED
environment.**

**The declaration's own version policy says package names are the requirement and
the versions are "a dated snapshot, not pins", which is why the version
differences are not a conformance failure. The platform difference is not
addressed by that policy either way.** **Unchanged from earlier tasks in this
line and still unregistered.** No stop: `A3`'s conformance requirements are
about the interpreter and the four packages, and all five held.

### 19.5 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — third finding: the `C3` residual, with a new half

**The multi-specification residual is unchanged and remains unregistered.**
`§15.2` adds a measurement the earlier record did not have: **two specifications
with DIFFERING stated totals produce no `DECLARATION_CONFLICT`, because totals
are not the quantity the conflict mechanism compares.** The earlier
"no conflict because they agreed" observations were true but about the wrong
field.

### 19.6 `OBSERVATION_METHOD_ERROR` — two findings, both mine, both caught inside the task

**FIRST. My `A9` numeric-literal regex included `\d+e[+-]?\d+`, which matches
substrings of hexadecimal SHAs.** About forty of seventy-one hits in the report
were SHA fragments such as `9e1` and `49e21210`. **Caught by resolving every hit
individually instead of reporting the count**, and disclosed in `§9`. Had I
reported the raw total as a finding, this report would have claimed dozens of
exponent-notation physics values in a document containing none.

**SECOND, and it was already written down before I caught it.** `§7.3`'s
`A7`-mandated confirmation first read: *"The phrasings … appear nowhere in
it."* **The sentence was false of the file the moment I wrote it, because
naming the phrasings in order to deny them puts them in the file.** The
verification grep returned hits on my own denial. **Caught by running the search
against the drafted report rather than trusting the assertion, and rewritten to
report the search positionally** — four matching lines, every one the search or a
denial, none an assertion.

**This is the same defect as `D-1`'s `§6` self-report in an earlier task, with
one difference that matters: that one was found after its commit, where Rule 20
permits only a message repair, so it could only be reported. This one was found
before commit 4 existed, so it was fixed.** The fix is in the artifact; the error
is recorded here because the artifact no longer shows it.

**Secondary, also mine and also caught:** `python3 -c "import ruff"` fails while
the `ruff` CLI is present and reports `0.15.8`. An import-only probe would have
declared a required package absent and triggered an unnecessary Rule 13
restoration. Disclosed in `§1`.

### 19.7 `ENVIRONMENT`, `REPOSITORY_DEFECT` — nothing to report

**`ENVIRONMENT`: no failure. No restoration was needed or performed, and NEITHER
of Rule 13's two diagnostic orders was exercised** — naming one would
misrepresent a conformance check as a diagnosis.

**`REPOSITORY_DEFECT`: none found by this task.** The merge was clean, all 460
base paths are blob-identical at the head, both pins recompute, the gate section
count is 14, and all nine checker properties pass. **`§19.1`'s sign defect is
classified as a specification defect because it is a discrepancy between a
specification and the gate, not a broken repository mechanism.**

### 19.8 Did landing a parallel line make me want to build it, adjudicate `r = 1`, or revise `D-1c`'s node count?

**YES to two of the three, and the honest answer is that the second was the
strong one.**

**Building it: mildly, and the pull was specific.** Component 10 — registered
regression anchors — is the one component in the `NEITHER` state, and the
arriving assessment itself observes it is plausibly the cheapest of the ten. The
flat Proca eigenstructure is already stated precisely in three places. **Adding
a regression anchor for it would have felt like tidying rather than building.**
**It would have been construction: `GATES.md:754` reads
`Regression anchors — None yet (proposed)`, and writing one would advance an
unrun gate from within an integration task. I did not.**

**Adjudicating `r = 1`: strongly, and this is the one I had to argue myself out
of.** The evidence looks decisive — `CONVENTIONS.md:24` says `r = 1` in plain
words, the dossier says the repository does not freeze `r`, and one of those is
simply wrong about the repository. **The temptation was to write "so `D-1b`'s
`W8` is misclassified" and be done.** **Two things stopped it.** First, `§3`
forbids it outright and `§9` says not to decide which instruction prevails.
**Second, and independently: I do not know that `CONVENTIONS.md:24` and the
dossier are talking about the same thing.** `CONVENTIONS.md:24` sits in a
lattice-regularization row that fixes `a ≡ 1` alongside `r = 1` — it may be
fixing a convention for the `P2-HK-01` computation rather than freezing a
programme-wide microscopic parameter, and the dossier's claim is about the latter.
**That is precisely the kind of distinction an adjudication has to make with
evidence, and making it in passing inside an integration report is how a
plausible reading becomes a landed ruling.**

**Revising `D-1c`'s node count: no, and not because I resisted it.** The
revision does not follow from anything measured here. It follows only from an
adjudication that has not happened, and `§7.2` states it as a consequence to be
checked rather than a conclusion. **`D-1c`'s ledger is blob-identical at commit
3, and it will be at commit 4.**

**I did not build, adjudicate, or revise. Nothing existing was modified: 460 of
460 base paths are blob-identical at the head.**

## 20. Evidence layering

**This report is committed as commit 4 and MEASURES COMMIT 3. Nothing in it
claims to measure commit 4.**

**Committed here, measured at commit 3:** `A1`–`A14`, `A16` and `A17` for
commits 1–3; `A15`'s two runs with both configs and both outputs verbatim;
commits 1–3 SHAs and their stored messages; commit 4's INTENDED message;
`A10`'s final 7/0 scope stated as INTENDED with the measured 6/0 figure at
commit 3; `A14` before the advance; `§17`'s landing as INTENDED.

**Post-report evidence, returned to the Reviewer and NOT written back:**
`A10`'s final scope measured base-to-commit-4; `A15-final`, being `RUN 2` re-run
at commit 4 before the landing; `A13` and `A14` re-run after the advance; `A17`
for commit 4; the pre-advance `--is-ancestor` exit status; the exact push
command; remote `main` read back; the source tip confirmed unchanged; and the
final ancestry confirmation.
