# Report — `SRC-01a`: is the halo configuration derived, fitted, or both?

    TASK        src-01a-configuration-provenance
    BRANCH      science/src-01a-configuration-provenance
    BASE        de547d9d6e152f6be0ef2215cb30c9c3fe3bd248
    SPEC SHA    1b87f571dbcfb4e063f32a5a7d734c39513a6faea971d95ac1fb6ff3da093473
    REVIEW      APPROVE FOR EXECUTION, bound to that SHA
    VERDICT     FORM DERIVED / SCALE FITTED

**EVERY FIGURE IS MEASURED AT COMMIT 3 (`7167d155…`) UNLESS THE LINE SAYS
`INTENDED`.** This report is commit 4. **Nothing here claims to measure commit
4**; the commit-4 evidence goes to the Reviewer in chat.

**EVERY SHA BELOW IS PASTED FROM `git rev-parse` OUTPUT TAKEN AT REPORTING
TIME**, with the command shown. **Nothing computed and nothing imported**; §8
verifies that by search.

## 1. `A3` — environment, run FIRST

**Rule 13's diagnostic order applies and was NOT exercised: no environment
failure occurred.** Rule 13 carries two such orders — a known open item — and I
name neither as the one used.

**Amendment D step 0, before anything else:**

    execution location    vm — Linux 6.18.5-fc-v20
    git common dir        /home/user/2-emergent-gravity/.git
    resolved HEAD at step 0       bfef924c368658cac85c04ed18d96eb4450afba6
    HEAD symbolic ref at step 0   refs/heads/claude/paper-2-independent-verification-dysdp0
    task worktree         /tmp/.../scratchpad/src01a
                          branch science/src-01a-configuration-provenance

**Clone depth, as `A3` requires:**

    $ git rev-parse --is-shallow-repository
    false
    $ git rev-list --count HEAD
    423
    $ git rev-list --count --all
    527

**THE CLONE IS NOT SHALLOW.** It was shallow earlier in this session and was
deepened with `git fetch --unshallow`; that is the origin of the recurring
stop-hook claim of 405 unpushed commits on the session branch, which is `main`'s
own published history made countable. **The `--all` count moved 519 → 523 → 527
across the last three tasks; the increments are those tasks' own commits.**

**Toolchain, MEASURED:**

    python   3.11.15 (main, Mar  3 2026, 09:26:23) [GCC 13.3.0]
    pytest   9.1.1
    numpy    2.4.6
    sympy    1.14.0
    ruff     0.15.8
    scipy    ABSENT — ModuleNotFoundError: No module named 'scipy'

**`pyproject.toml:12` declares `"scipy>=1.11"` and it is not installed.** Eighth
consecutive task. Nothing here needed it — this task runs no numerics at all.

**`docs/local/execution_environment.md` declares a Windows environment**
(`zeta-3070\codexsandboxoffline`, Python 3.12, `C:\p2-validator\venv`). Every run
has been on Linux. Undeclared, unregistered.

## 2. `A1` — repository, refs, branch availability

**Command output pasted verbatim, as `A1` requires:**

    $ git remote get-url origin
    https://github.com/zetacheng/2-emergent-gravity

**It identifies `zetacheng/2-emergent-gravity`.**

    $ git rev-parse refs/remotes/origin/main
    de547d9d6e152f6be0ef2215cb30c9c3fe3bd248

**A1 expects `de547d9d6e152f6be0ef2215cb30c9c3fe3bd248`. MATCH.**

    $ git rev-parse refs/heads/main
    1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**`refs/heads/main` is a stale local ref and is not this task's base.** The
branch was cut from `refs/remotes/origin/main`. **`main` is not touched at all by
this task.**

**BRANCH AVAILABILITY:**

    refs/heads/science/src-01a-configuration-provenance          DID NOT EXIST
    origin refs/heads/science/src-01a-configuration-provenance   0 matching refs

**Neither existed, so no stop was triggered.**

**ON THE PASTE REQUIREMENT.** I follow it because a pasted identifier can be
checked against the ref it names and a statement that I checked cannot — **which
is `A1`'s own reasoning, and it stands without reference to the retracted
history.** §11.5 records what that episode shows.

## 3. `A2` — the review, committed unedited

**FIELD PRESENCE CHECKED FIRST, THEN THE VALUE**, because a review carrying no
`reviewed specification SHA-256:` field at all would otherwise pass a naive
comparison against an empty string.

    field present?    YES — review line 4 carries "Reviewed specification SHA-256:"
    value             1b87f571dbcfb4e063f32a5a7d734c39513a6faea971d95ac1fb6ff3da093473
    uploaded spec     1b87f571dbcfb4e063f32a5a7d734c39513a6faea971d95ac1fb6ff3da093473
    IDENTICAL
    committed specs/2026-08-18T1205Z_src-01a-...md   1b87f571…   IDENTICAL
    verdict, review line 6   APPROVE FOR EXECUTION

## 4. `A4` — the manuscript inventory, in two passes

    paper/emergent_gr_paper_v2_15.tex        1833 lines
    wc -l and grep -c "" agree at 1833; the file ends with a newline

**The specification's pre-issue record gives 1834.** The difference is the usual
one between counting newlines and counting a final unterminated line; **there is
no unterminated final line, so both conventions give 1833 here.** Nothing turns
on it and every line number below was read at the head.

### 4.1 PASS 1 — the seed terms

    sparc              15        fit                 7
    halo                2        derive              5
    rotation curve      0        profile             1
    r_c                 2        Yukawa              4
    m_theta             0        m_\theta            7

    PASS 1 distinct lines: 36

**`m_theta` RETURNS ZERO AND `m_\theta` RETURNS SEVEN**, exactly as the
specification warned. **`rotation curve` returns zero — the phrase does not
occur in the manuscript at all.**

**AND `halo` OCCURS ON EXACTLY TWO LINES OUT OF 1833**: `:207`, inside the
sentence citing Paper 1, and `:1815`, the bibliography title. **The manuscript
never computes, plots, or characterises a halo profile.**

### 4.2 PASS 2 — the identification terms

    chi                72        dark matter         3
    \theta             29        Green               2
    \tilde\theta        3        cutoff             14
    ultralight         11        identif            14
    scalar sector       2

    PASS 2 distinct lines: 137

### 4.3 The union, and what PASS 2 adds

    PASS 1 only      24
    BOTH             12
    PASS 2 only     125
    UNION           161

**PASS 2 CONTRIBUTES 125 LINES PASS 1 DOES NOT REACH — more than three times
PASS 1's entire yield of 36.** Among them is `:80`:

> `This mode is identified with the ultralight scalar responsible for`

**That is the carrier identification and PASS 1 does not reach it.** An inventory
on the seed list alone would have found the parameters and missed the step that
makes them relevant — **a provenance verdict about a subset of the argument,
exactly as the specification anticipated.**

**THE SPECIFICATION'S AUTHOR MEASURED 136 PASS-2-ONLY LINES; I MEASURE 125.**
Both are correct under their own matching convention: the figure depends on how
`fit`, `derive` and `m_\theta` are matched in PASS 1, and a wider PASS 1 moves
lines into the intersection and lowers the PASS-2-only count. **My method:
case-insensitive substring on every term, one line counted once.** **The
substantive claim reproduces exactly — `:80` is PASS-2-only, and PASS 2 supplies
the large majority of the union.**

### 4.4 Which `chi` hits are substantive

**`chi` returns 72 lines and SEVENTY-ONE OF THEM ARE ABOUT SOMETHING ELSE.**

    lines containing the LaTeX macro \chi           15
    lines with "chi" but no \chi macro              57
      chiral 36 · chirally 8 · machinery 7 · machine 3 · matching 2 · chiralmass 1

**And of the fifteen `\chi` lines, FOURTEEN denote a different object:**

    :260                          G_\chi        a chiral-sector coupling
    :938 :944 :983–:986 :994      c_\chi^2      the collective-mode speed
    :953 :955                     \xi_\chi      a non-minimal coupling
    :1198–:1200 :1203             \tilde\chi    the RADIAL fluctuation

**EXACTLY ONE OF SEVENTY-TWO IS THE SUBJECT:**

    :616   We identify $\tilde\theta$ with the ultralight scalar $\chi$ whose

**A count of 72 that is really 1.** The same symbol carries four physical
meanings in this manuscript, and `\tilde\chi` at `:1198` is the mode that
`:628-631` explicitly excludes from low-energy relevance — **the nearest
neighbour in notation is the one object the argument sets aside.**

### 4.5 Vocabulary added beyond both lists

**I ADDED `varepsilon` AND READ ALL ELEVEN OF ITS LINES.** PASS 2 established
that `m_θ` is fixed through `m_θ² ~ εΛ²`, and neither list reaches the breaking
parameter itself. **That addition produced §7.3's finding** — without it the
parameter chain would have terminated one step early, at `m_θ`, and the
manuscript's own statement that `ε` is uncomputed would have gone unmeasured.

**NEITHER LIST IS EXHAUSTIVE.** They are the Researcher's and came from a
description of the manuscript rather than from the manuscript. **A derivation
using vocabulary outside all three would be missed by this inventory**, and I
say so rather than implying coverage I did not establish.

## 5. `A5` — the passages, and whether the Researcher's reading survives

**Quoted verbatim from the head. The artifact carries all four passages in
full; the two the specification names are reproduced here.**

    :206  In Ref.~\cite{Cheng:2025sparc}, we derived a Yukawa-type dark
    :207  matter halo profile from the scalar sector of the same lattice
    :208  fermion framework and tested it against 175 SPARC galaxies.
    :209  The present paper develops the gravitational sector and the vacuum
    :210  structure that underlies both papers.

    :612  \item \textbf{Identification with the dark-matter mode.}
    :613  The static field equation of $\tilde\theta$ is that of a massive
    :614  scalar, with Yukawa Green's function of range
    :615  $r_c = 1/m_\theta$.
    :616  We identify $\tilde\theta$ with the ultralight scalar $\chi$ whose
    :617  galactic-scale phenomenology was tested in
    :618  Ref.~\cite{Cheng:2025sparc}; the SPARC-scale cutoff radii
    :619  $r_c \sim 10\,\mathrm{kpc}$ correspond to
    :620  $m_\theta \sim 10^{-27}\,\mathrm{eV}$, i.e.\
    :621  $\varepsilon \sim m_\theta^2/\Lambda^2$, an extraordinarily good
    :622  approximate symmetry.

**THE SURROUNDING ARGUMENT.** Section `sec:angular` establishes the vacuum
structure: the substrate fermions are gapped at `O(Λ)` and unobservable, while
the angular direction of the complex condensate hosts a pseudo-Goldstone mode
whose mass is protected by an approximate `U(1)` broken only by the lattice
(`:73-79`). `:598` gives `m_θ² ~ ε Λ²`. Two properties are then listed: technical
naturalness (`:604-611`) and identification with the dark-matter mode
(`:612-625`). Immediately after, `:628-631` sets the radial mode aside, and
`:633-644` records the coupling to baryons as open.

**DOES THE RESEARCHER'S READING SURVIVE? YES — and it understates the case in
one direction and overstates it in another.**

**IT SURVIVES ON THE FORM.** `:613-615` derives the Yukawa Green's function from
the static field equation of a massive scalar. **That is a step this manuscript
performs, not one it cites.**

**IT SURVIVES ON THE SCALE, AND `:618-620` IS MORE EXPLICIT THAN THE READING
SUGGESTED.** The direction is unambiguous — the SPARC-scale radii "correspond
to" the mass. **The observation is the input and the mass is the output**, and
`:621` runs the chain one step further to `ε`.

**WHERE IT UNDERSTATES: the manuscript says `ε` is not computed** — §7.3.

**WHERE IT OVERSTATES: `:613-615` is not the halo profile.** It is the Green's
function of the mediating field. **A halo profile additionally needs a source
distribution and a coupling to it, and this manuscript supplies neither.**

## 6. `A6` — claimed here versus established here

    CLAIMED HERE AND DERIVED HERE                                        3
    CLAIMED HERE, CITED TO PAPER 1                                       6
    NOT ADDRESSED (explicitly open in this manuscript)                   3
    TOTAL load-bearing statements classified                            12

**DERIVED HERE — 3:** the pseudo-Goldstone mode and its symmetry protection
(`:76-79`); the mass relation `m_θ² ~ εΛ²` (`:598`), with `ε` undetermined; the
Yukawa Green's function of range `r_c = 1/m_θ` from the static field equation
(`:613-615`).

**CITED TO PAPER 1 — 6:** the mode IS the ultralight scalar of the cited work
(`:80-81`); "we derived a Yukawa-type dark matter halo profile … and tested it
against 175 SPARC galaxies" (`:206-208`); the light angular mode is "dark matter
[cite]" (`:443`); `θ̃` is identified with `χ` "whose galactic-scale phenomenology
was tested in Ref." (`:616-618`); the framework "produces both gravitational
dynamics and ultralight dark-matter phenomenology" (`:1529-:1534`); the summary
restatement (`:1555-:1558`).

**NOT ADDRESSED — 3:** the magnitude of `ε` is "the dedicated computation left
open" (`:541-544`); the monopole coupling to baryons "remains open", "deferred to
future work" (`:633-644`); the same under Limitations, "the quantitative chain is
open" (`:1626-1630`).

**THE DISTRIBUTION IS THE FINDING. Three steps are performed here, six are
asserted and pointed elsewhere, three are declared open by the manuscript
itself.** **A sentence beginning "we derived" is a claim about another paper, and
this manuscript does not contain the derivation it names.** **Nothing here
verifies any of the six.**

## 7. `A7` — the identification first, then the parameters

### 7.1 The identification

    WHICH MODE      the angular (phase) direction of the complex condensate,
                    the pseudo-Goldstone θ̃
    WITH WHAT       χ, the ultralight scalar of Ref. [Cheng:2025sparc]
    WHERE           :80-81 and :616-618; restated at :443, :1531-:1534, :1555-:1558
    ON WHAT BASIS   ASSERTED. The manuscript states it and does not derive it.
                    The one supporting remark, :623-625, is that the
                    pseudo-Goldstone origin puts the scale "on the same
                    mechanistic footing as axion-like ultralight dark-matter
                    scenarios" — a plausibility statement about a CLASS of
                    models, not a derivation that this mode IS that scalar.
    A6 CATEGORY     CLAIMED HERE, CITED TO PAPER 1

**THE IDENTIFICATION IS LOAD-BEARING AND IS THE WEAKEST LINK.** Everything
downstream depends on it: that `r_c` is a galactic scale at all, that `m_θ` is
ultralight, that `ε` is tiny. **Withdraw it and the manuscript still has a
pseudo-Goldstone mode of undetermined mass, with nothing connecting it to a
galaxy.**

**AND IT IS PARTLY FIXED BY THE PHENOMENOLOGY IT EXPLAINS.** The mode is
identified with the dark-matter scalar, and the dark-matter scalar's observed
scale is then used to fix the mode's mass. **The manuscript is explicit about
this direction and does not disguise it.**

### 7.2 `r_c`

    RELATION GIVEN      r_c = 1/m_θ, derived at :613-615
    VALUE DETERMINED BY OBSERVATION — :618-619 takes "the SPARC-scale cutoff
                        radii r_c ~ 10 kpc" as given
    PROVENANCE          FITTED (an observational input, quoted from :619)

### 7.3 `m_θ` — stated plainly, as `A7` requires

    RELATIONS GIVEN     m_θ² ~ ε Λ²   (:598)   and   r_c = 1/m_θ   (:615)
    VALUE DETERMINED BY :619-620 — "the SPARC-scale cutoff radii r_c ~ 10 kpc
                        correspond to m_θ ~ 10⁻²⁷ eV"
    PROVENANCE          FITTED, via r_c

> **`r_c ~ 10 kpc` IS TAKEN FROM SPARC AND `m_θ` IS INFERRED FROM IT.**

**`r_c = 1/m_θ` IS A RELATION, NOT A DETERMINATION** — it converts one unknown
into another. **The determination enters at `:619` and it is observational.**

**AND `ε` DOES NOT RESCUE IT, BECAUSE THE MANUSCRIPT SAYS `ε` IS NOT COMPUTED.**
`:621` runs the same direction — `ε ~ m_θ²/Λ²`, i.e. `ε` inferred FROM `m_θ` —
and `:541-544` states:

> `(The magnitude of $\varepsilon$ on the $H(4)$ substrate---in particular
> whether the anomaly contribution is exponentially instanton-suppressed---is
> the dedicated computation left open in Section~\ref{sec:angular}.)`

**THE SCALE CHAIN RUNS OBSERVATION → `r_c` → `m_θ` → `ε`, AND NO STEP RUNS THE
OTHER WAY.** `:1681-1683` lists the reverse as future work: "the explicit-breaking
chain fixing the angular-mode coupling to baryons, **connecting `ε` to the
SPARC-scale phenomenology**".

### 7.4 The coupling and the amplitude

    FIXED BY            NOTHING HERE. :633-644 records the monopole coupling of
                        the angular mode to baryonic matter as open, names the
                        mechanism that would have to produce it, and defers the
                        quantitative chain. :1626-1630 repeats it under
                        Limitations.
    WHAT THE MANUSCRIPT SAYS PAPER 1 DOES WITH IT
                        ":642-644  in Ref. the coupling is treated as an
                        effective parameter, so the phenomenological results
                        there are unaffected."
    PROVENANCE          NEITHER DERIVED NOR FITTED HERE — explicitly open, and
                        carried in the cited work as a free effective parameter
    AMPLITUDE           NOT ADDRESSED AT ALL. No normalisation, no source
                        distribution, no profile function anywhere in 1833 lines.

## 8. `A8` — the verdict

> ## `FORM DERIVED / SCALE FITTED`

    DERIVED HERE
      the FUNCTIONAL FORM — Yukawa, the Green's function of a massive scalar,
        from θ̃'s static field equation                        :613-615
      the RELATION r_c = 1/m_θ                                 :613-615
      the RELATION m_θ² ~ ε Λ²                                 :598

    FITTED — set from observation
      r_c    taken as the SPARC-scale radius                   :619
      m_θ    inferred from r_c                                 :619-620
      ε      inferred from m_θ                                 :621

    NEITHER — explicitly open in this manuscript
      the coupling of the mode to baryonic matter              :633-644, :1626-1630
      the amplitude / normalisation of any profile             not addressed
      the magnitude of ε from first principles                 :541-544

**WHY NOT `DERIVED`.** Nothing in this manuscript predicts `m_θ`, `r_c` or `ε`.
Every numerical scale in the chain enters at `:619` from observation.

**WHY NOT `FITTED`.** The Yukawa form is not chosen to match anything. It follows
from the mode being a massive scalar, which follows from the pseudo-Goldstone
structure this manuscript derives. **A fitted profile is one selected for its
agreement; this form is forced by the field equation and then given a scale.**

**WHY NOT `NOT DETERMINABLE FROM THIS MANUSCRIPT`, AND THE SCOPE THAT DECIDES
IT.** The verdict is about the object this manuscript actually treats: **the
Yukawa Green's function of the identified mode, with range `r_c`.** For that
object the manuscript is explicit on both halves.

**FOR A BROADER OBJECT — Paper 1's dark-matter halo profile fitted to 175
galaxies — THE ANSWER IS `NOT DETERMINABLE FROM THIS MANUSCRIPT`**, and the two
must not be conflated. `:206-208` claims that profile was derived and tested;
**this manuscript performs neither step, mentions `halo` on two lines out of
1833, contains no profile function, no source distribution and no data, and
leaves the coupling that would connect the mode to baryons explicitly open.**
**What would settle it is Paper 1, which is not in this repository.**

**Both are reported because the question admits both objects; compressing them
into one verdict would lose the distinction.** The primary verdict is the first,
because the question names "the halo profile" and the manuscript's own treatment
of it is the Yukawa form with a fitted scale.

## 9. `A9` — what would remain testable, as an implication

**This is what the classification implies. It is not a recommendation, and this
report does not say whether the source-side test should be done.**

**NOT TESTABLE AGAINST THE SAME DATA:**

- **any statement whose content is the value of `r_c`, `m_θ` or `ε`** — these
  were set from the SPARC-scale radius, so a calculation recovering `r_c` would
  be recovering its own input;
- **the overall normalisation of any potential**, since the coupling is a free
  effective parameter in the cited work and open here.

**POTENTIALLY TESTABLE, BECAUSE NOT FIXED BY THE FITTED SCALE:**

- **the SHAPE at fixed `r_c`** — Yukawa is a one-parameter family once the range
  is given, and whether real systems follow that shape after the range is fitted
  is not guaranteed by having fitted the range;
- **CROSS-SYSTEM behaviour** — one fitted scale cannot absorb a scaling relation
  across many systems. **Whether the framework predicts such a relation is not
  determinable here**: this manuscript contains no scaling relation, and
  `SRC-B0` measured that `r_c ∝ V_max^{0.82}` occurs nowhere in the repository;
- **the coupling chain itself** — `:1681-1683`'s future-work item (iii), deriving
  `ε` and the monopole coupling from the explicit-breaking structure and then
  checking the resulting `m_θ`. **That runs the chain in the opposite direction
  from `:619-621` and would be a genuine prediction**, and it is exactly the
  computation `:541-544` records as open.

**THE CIRCULARITY RISK IS REAL BUT BOUNDED, AND THE BOUND IS THE USEFUL PART.** A
test comparing a computed potential's scale to the SPARC scale would be circular.
A test of shape or cross-system behaviour at fixed range would not be, **provided
the range is declared as an input rather than a result.**

## 10. `A10` – `A16`

### 10.1 `A10` — nothing imported, nothing computed

**SEARCHED the artifact and every commit message in the range for a computed
quantity, a numerical value not quoted from the manuscript, a statement sourced
to Paper 1 directly, and a fit performed here.**

    CATEGORY                                        ARTIFACT   COMMIT MESSAGES
    a computed quantity                                    0                 0
    a numerical value NOT quoted from the manuscript        0                 0
    a statement sourced to Paper 1 directly                 0                 0
    a fit performed here                                    0                 0

**ALL FOUR ZERO, AND THE SECOND ROW NEEDS ITS METHOD STATED.** A loose pattern
returns 38 hits, almost all of them `eV` matching inside `every`, `relevance`,
`level` and `evaluates`. **Word-bounded, the artifact contains exactly twelve
occurrences of a physical numeral, and they are three values repeated:**
`r_c ~ 10 kpc`, `m_θ ~ 10⁻²⁷ eV`, and `175 SPARC galaxies`. **Every one is a
quotation from a cited manuscript line** — `:619`, `:620`, `:208` — which `A10`
expressly permits. **No value was produced here.**

**The one apparent "fit" hit is `NEITHER DERIVED NOR FITTED HERE` at artifact
line 321 — a denial matching a pattern for the thing it denies.**

**Paper 1 was not read.** Every statement about it in the artifact is attributed
to this manuscript's description, with the manuscript line cited.

### 10.2 `A11` — scope

    stated: 4 additions, 0 modifications          INTENDED, final at commit 4
    append_only:  DECISION_LOG.md                 a CHECKER-CONFIGURATION declaration,
                                                  NOT an authorisation to write it
    authorised_gates: []
    base: de547d9d6e152f6be0ef2215cb30c9c3fe3bd248
    head: commit 4
    mode: exact
    modify: []
    forbidden_operations: delete, rename, copy, type_change, unmerged, unknown

**CUMULATIVE per commit — MEASURED:**

    base .. commit 1  713af349     1 addition,  0 modifications
    base .. commit 2  fe62ed85     2 additions, 0 modifications
    base .. commit 3  7167d155     3 additions, 0 modifications
    base .. commit 4               4 additions, 0 modifications   INTENDED

**CONTRIBUTION per commit — MEASURED, separately labelled:**

    commit 1   A specs/2026-08-18T1205Z_src-01a-configuration-provenance.md
    commit 2   A reviews/chatgpt/2026-08-18T1205Z_src-01a-configuration-provenance.md
    commit 3   A derivations/P2-SRC-01a_configuration-provenance.md
    commit 4   A reports/2026-08-18T1205Z_src-01a-configuration-provenance.md   INTENDED

**Each commit contributes exactly one path, so the two coincide numerically at
every step here.** They are reported separately because that coincidence is a
fact about this task's shape, not a general identity — a reviewer of an earlier
task read a cumulative figure as a contribution.

**`DECISION_LOG.md` was not written; its blob is unchanged — §10.3.**

**The UTC time was measured, not assumed: `2026-08-18T12:05:34Z`, giving the
token `1205Z`.** Commit 1 was made in the same minute.

### 10.3 `A12` — nothing existing changed

    PATHS COMPARED (all paths at the evidence base)    498
    paths at the head                                  501
    paths whose blob DIFFERS at the head                 0
    git diff --name-status base..head                    3 entries, ALL status A
    entries of any other status                          0

    paper/emergent_gr_paper_v2_15.tex     c8246f890b07f53a…   UNCHANGED
    GATES.md                              2b3bd5069414f009…   UNCHANGED
    CONVENTIONS.md                        8badc51f38d85d54…   UNCHANGED
    docs/BRANCHING_POLICY.md              3f0f35d4da448eb4…   UNCHANGED
    DECISION_LOG.md                       d9dd2bf3a8cca405…   UNCHANGED
    scripts/recon2026/proca_curved.py     03f46905e5798fb7…   UNCHANGED
    scripts/recon2026/flat_validation.py  6b21f9d6db67641e…   UNCHANGED
    tests/test_recon2026_flat_limit.py    1d7ba5672614dedc…   UNCHANGED

**`paper/emergent_gr_paper_v2_15.tex` IS THE SUBJECT OF THIS ENTIRE TASK AND ITS
BLOB IS UNCHANGED.** Every line this task quotes was read from a file it did not
touch. **The `paper/` subtree object is `8af4fcc6c126e6ba20d7d44770c8c1d1eb12bef0`
at both ends** — one comparison covering the manuscript, its README and the
figures directory.

**BOTH ARTIFACT COUNTS RE-MEASURED, not carried:**

    derivations/P2-BETAV-*    base 8   head 8
    derivations/P2-SRC-*      base 1   head 2

      P2-SRC-01a_configuration-provenance.md      ← added by this task
      P2-SRC-B0_source-side-scope.md

**`results/` subtree `9015049f68d5ace2790b5c62976e798298442bce` at both ends.**
Both registers unchanged.

### 10.4 `A13` — gate invariants and pins

**Read SCOPED: `P2-PHASE-01` is `GATES.md:971–1108`, bounded by the next
`^## P2-` heading; every value was taken inside those bounds.**

    ^## P2- count                     14
    P2-PHASE-01 status  GATES.md:973  Status: PROPOSED
    prerequisite 1      GATES.md:1011 Artifact state: ADOPTED. Prerequisite state: SATISFIED
    prerequisite 2      GATES.md:1036 Artifact state: ADOPTED. Prerequisite state: SATISFIED

**Both pins verified by recomputing the digest of the artifact each pins:**

    P2-PHASE-01_microscopic_parameter_domain.md
      recomputed 4a3bd8211502d36f9e950086b766ef6ef587f1f4504661d1565962213cd3d214
      pinned at GATES.md:1017 — MATCH
    P2-PHASE-01_input_admissibility_contract.md
      recomputed e63f5a7f1db276ce7263c8954bd8afff8ed24a069b988b098c9fe28bf3a91af3
      pinned at GATES.md:1040 — MATCH

### 10.5 `A15` and `A16`

    python3 -m pytest -q         332 passed, 2 deselected in 78.25s
    exit status                  0

**332 passed, 2 deselected, exactly as expected. This task adds no code.**

**`A16` — hygiene. Rule 20 binds this task and was not needed: no message
required repair, no history was rewritten. Every SHA below pasted from
`git rev-parse`:**

    commit 1  713af349c974b7ccc3d3786f46fbd0fc6ac618fc
              spec: is the halo configuration derived, fitted, or both
    commit 2  fe62ed85f184704d2fc8e7b507c65d2d11b999c8
              review: pre-execution review for the configuration provenance assessment
    commit 3  7167d1557e2d6653165c3f1604f210a8c8705b76
              provenance: the form is derived and the scale comes from observation
    commit 4  INTENDED message:
              report: the form is derived and the scale is observational

    Co-Authored-By          0        Generated with        0
    Co-authored-by          0        Claude-Session        0
    claude.ai/code          0        any model identifier  0
    🤖                      0        noreply@anthropic.com 0

**All zero. `A16` for commit 4 is post-report evidence and is not written here.**

### 10.6 `A14` — the checker over this task's own range

**Base `de547d9d…`, head commit 3 `7167d155…`. Two runs at both prospectivity
readings — four invocations, all exit `0`.**

**THE OUTPUT WAS PARSED, NOT GREPPED.** Each JSON file was loaded with
`json.loads` and every property read from the parsed structure by key (`id`,
`status`, `classification`, `evidence`). The property list is a JSON *array* of
objects rather than a map keyed by property id, so a key lookup returns `None`,
and a grep for `PASS` would count the word wherever it occurs — including inside
the `does_not_establish` prose every `PARTIAL` property carries.

**`RUN 1` config, verbatim — observational, governs nothing:**

    {
      "base": "de547d9d6e152f6be0ef2215cb30c9c3fe3bd248",
      "head": "7167d1557e2d6653165c3f1604f210a8c8705b76",
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
      "base": "de547d9d6e152f6be0ef2215cb30c9c3fe3bd248",
      "head": "7167d1557e2d6653165c3f1604f210a8c8705b76",
      "specification_paths": [
        "specs/2026-08-18T1205Z_src-01a-configuration-provenance.md"
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
    NOT_DECLARED / NOT_PARSEABLE    none
    DECLARATION_CONFLICT            NONE — confirmed
    commits_in_range                3
    commits_on_first_parent_line    3
    prospectivity in scope 3, out of scope []

**`P7` REPORTS FOURTEEN SECTIONS** — base 14, head 14, raw 14 and 14. **`PASS` at
zero would have been a stop; it is not zero.**

**`P5` and `P9` are `NOT_APPLICABLE`, which is the correct result and not a weak
pass.** There is no merge in this range, so `P5` has no subject; at commit 3 no
report exists yet, so `P9` has none. **`NOT_APPLICABLE` does not make the run
incomplete, and the checker's vocabulary separates it from `DECLARED_EMPTY` and
from `PASS`.**

**WHAT `RUN 1` DID.** Its default subject selection discovered exactly ONE
specification in range — this task's, `stated: 4 additions, 0 modifications`,
counted 4 (add 4 / mod 0), parse OK. **`RUN 1` and `RUN 2` are therefore
BYTE-IDENTICAL at each reading**, `diff` returning nothing, so the four
invocations produce exactly TWO distinct byte strings differing only at line 252.
**That does not make them the same check: `RUN 2` names the subject and `RUN 1`
discovers it. They agree here because there is one subject to find.**

**THE `C3` MULTI-SPECIFICATION RESIDUAL DID NOT ARISE, and the reason is that
there is ONE declaring specification — the "cannot trigger" half.** The two
preceding ranges each had two specifications with differing stated totals and
raised no `DECLARATION_CONFLICT`, because `_declarations_from_specs` compares
`append_only_paths` and `authorised_modified_gates` and not stated totals.
**Unchanged and still unregistered.**

**Neither the config nor this specification's declarations were adjusted to make
`RUN 2` pass. `RUN 2` passed on its first invocation at both readings.**

### 10.7 The JSON output, verbatim

**`RUN 1` and `RUN 2` at the `INCLUSIVE` reading are BYTE-IDENTICAL, so the file
below IS both outputs rather than a sample of one. Each `EXCLUSIVE` output is
this file with line 252 reading `"inclusivity": "EXCLUSIVE"`.**

    {
      "base": "de547d9d6e152f6be0ef2215cb30c9c3fe3bd248",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "7167d1557e2d6653165c3f1604f210a8c8705b76",
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
                "derivations/P2-SRC-01a_configuration-provenance.md",
                "reports/2026-08-XXT{HHMM}Z_src-01a-configuration-provenance.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_src-01a-configuration-provenance.md",
                "specs/2026-08-XXT{HHMM}Z_src-01a-configuration-provenance.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-18T1205Z_src-01a-configuration-provenance.md",
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
                "commit": "713af349c974b7ccc3d3786f46fbd0fc6ac618fc",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "fe62ed85f184704d2fc8e7b507c65d2d11b999c8",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "7167d1557e2d6653165c3f1604f210a8c8705b76",
                "work_paths": [
                  "derivations/P2-SRC-01a_configuration-provenance.md"
                ]
              }
            ],
            "first_review_commit": "fe62ed85f184704d2fc8e7b507c65d2d11b999c8",
            "first_work_commit": "7167d1557e2d6653165c3f1604f210a8c8705b76",
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
              "specs/2026-08-18T1205Z_src-01a-configuration-provenance.md"
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
              "commit": "713af349c974b7ccc3d3786f46fbd0fc6ac618fc",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "fe62ed85f184704d2fc8e7b507c65d2d11b999c8",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "7167d1557e2d6653165c3f1604f210a8c8705b76",
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
              "specs/2026-08-18T1205Z_src-01a-configuration-provenance.md"
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
            "first_commit": "713af349c974b7ccc3d3786f46fbd0fc6ac618fc",
            "first_commit_paths": [
              "specs/2026-08-18T1205Z_src-01a-configuration-provenance.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-18T1205Z_src-01a-configuration-provenance.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-18T1205Z_src-01a-configuration-provenance.md"
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

## 11. `§7` — Rule 16 assessment: what the assembled set does NOT establish

### 11.1 First — this reads Paper 2's description of Paper 1's work

**IT DOES NOT READ PAPER 1. PAPER 1 IS NOT IN THIS REPOSITORY.**

**Every statement here about what Paper 1 derived, fitted or tested is THIS
MANUSCRIPT'S CLAIM, and nothing here verifies any of it.** §6 counts six such
claims and classifies them as claims.

**AND THE VERDICT MUST BE READ WITH THAT BOUNDARY.** The `FORM DERIVED` half is
a verdict about a step this manuscript performs at `:613-615` — that one is about
what was DONE, in a file I read. **The statements about Paper 1's halo profile
are verdicts about what is CLAIMED.** A `DERIVED` verdict reached from a citation
would be a verdict about a claim; **I did not reach one, and the reason the
distinction matters is that the manuscript's own wording invites it.** "we
derived a Yukawa-type dark matter halo profile" reads as a derivation until you
notice its subject is another paper.

### 11.2 Second — a provenance verdict supplies no configuration

**`SRC-B0`'s finding stands unchanged: nothing usable for computation is in this
repository.** No profile function, no source distribution, no parameter values.

**THIS TASK MOVES THE QUESTION, NOT THE BLOCKER.** Before it, the programme knew
a configuration was absent. Now it also knows that the manuscript's own account
of the configuration derives a form and takes a scale from data. **That changes
what a future task would be testing; it does not change what a future task
could compute today, which is still nothing.**

### 11.3 Third — the taxonomy needed repairing

**YES, IT DID.** `SRC-B0`'s two-way `DERIVED` / `FITTED` split cannot express
this manuscript's actual position, and the position is not exotic — **it is the
ordinary situation of a theory that predicts a functional form and takes a scale
from experiment.** A two-way taxonomy forces that into whichever box the reporter
finds more salient.

**A TAXONOMY WHICH CANNOT EXPRESS THE ANSWER IS A DEFECT IN THE QUESTION, NOT IN
THE MATERIAL.** The four-way taxonomy in this specification is a repair, and the
third verdict is the one it added.

**AND THE REPAIR IS STILL NOT COMPLETE, WHICH I RECORD RATHER THAN PAPER OVER.**
§8 needed a scope qualification the four-way taxonomy does not provide: the same
question has two defensible answers depending on whether "the halo profile" means
the Yukawa Green's function this manuscript derives or the fitted profile it
cites. **A fifth category is not the fix; naming the object is.**

### 11.4 Fourth — the search terms are not exhaustive

**THEY ARE THE RESEARCHER'S AND THEY CAME FROM A DESCRIPTION, NOT FROM THE
MANUSCRIPT.** §4 records what that costs: `m_theta` returns zero because the file
writes `m_\theta`; `rotation curve` returns zero because the phrase is absent;
PASS 1 misses the carrier identification at `:80` entirely.

**I SEARCHED:** PASS 1's ten terms, PASS 2's nine, and `varepsilon`, which I
added after PASS 2 showed the parameter chain ran through it. **Twenty terms,
161 distinct lines out of 1833.**

**A CONFIGURATION OR A DERIVATION USING VOCABULARY OUTSIDE ALL THREE WOULD BE
MISSED.** I did not read the manuscript end to end; I read the union plus the
surrounding argument at each cluster. **That is a bounded reading and I state its
bound rather than implying coverage.**

### 11.5 Fifth — the retracted SHA attribution, and what it shows

**THIS SPECIFICATION'S OWN EARLIER DRAFT ASSERTED THAT THREE EXECUTION REPORTS
GAVE UNRESOLVABLE COMMIT IDS, AND LABELLED IT `MEASURED`.** §10 of the issued
specification retracts it.

**WHAT WAS MEASURED: the tokens do not resolve as Git objects.** That is true and
I re-confirmed it in the previous task.

**WHAT WAS NOT MEASURED: that those reports gave them.** A search finds them zero
times in the reports they were attributed to — the previous integration
established that independently, and the Researcher has since confirmed the same.
**The tokens reached the specification through conversation, not through the
repository.**

**`A1`'S PASTE REQUIREMENT RESTS ON ITS OWN REASONING AND NOT ON THAT
ATTRIBUTION.** A pasted identifier can be checked against the ref it names; a
statement that the executor checked cannot. **That argument would be sound if the
episode had never occurred**, and it is why I followed the requirement without
relying on the precedent.

**WHAT THE EPISODE SHOWS: a measurement of one proposition was carried into an
assertion about a different one.** *These tokens do not resolve* was measured.
*These reports gave these tokens* was asserted. **The two share a subject and
nothing else**, and the `MEASURED` label attached to the first travelled to the
second.

**THIS LINE HAS RECORDED THAT FAILURE UNDER SEVERAL NAMES ALREADY** — a
`P2-BETAV-*` count carried across three specifications instead of re-measured; a
`pyproject.toml` line number cited from memory; a self-referential search count
invalidated by the edit that fixed it. **The common structure is a figure that
was true of something, detached from what it was true of.** **`A11`'s
re-measurement requirements and `A1`'s paste requirement are both instruments
against it**, and neither is redundant with the other: one guards against
carrying a number forward in time, the other against carrying it sideways between
propositions.

## 12. The temptation, answered directly

**Did reading the manuscript make me want to evaluate the phenomenology?**
**Yes, and specifically at `:621`.** The manuscript calls
`ε ~ m_θ²/Λ² ~ 10⁻²⁷ eV squared over a lattice scale` "an extraordinarily good
approximate symmetry", and the obvious next thought is whether a number that
small is natural or alarming. **That is a judgement about whether the physics
works, and the question I was asked is where the number came from.** I did not
form the judgement in the artifact, and §8 classifies `ε` by provenance only.

**Did I want to reason from Paper 1 directly?** **Yes, and this was the strongest
pull of the three.** By `:642-644` the manuscript states that Paper 1 treats the
coupling as an effective parameter, which is a fairly specific fact about a paper
I have not read — **and it is exactly the kind of fact that invites completing
the picture from what one imagines the cited paper must contain.** I did not.
Every statement about Paper 1 in the artifact carries the manuscript line that
makes it, and the verdict for Paper 1's profile is `NOT DETERMINABLE FROM THIS
MANUSCRIPT` rather than a reconstruction.

**Did I want to say whether the source-side test is worth doing?** **Yes, and the
material almost writes the sentence for you.** §9's split — scale not testable,
shape and cross-system behaviour possibly testable — reads as a recommendation
one clause away from being one. **§3 of the specification forbids judging it**,
and the reason is sound: whether a partially-informative test is worth its cost
is a programme decision, not a measurement. **I reported the implication and
stopped at it.**

**One further restraint worth naming, because nothing asked for it.** The
identification at `:80-81` and `:616-618` is asserted rather than derived, and it
would be easy to let that observation slide into a criticism of the manuscript.
**It is not a criticism — an identification is a legitimate modelling step, and
the manuscript is explicit that it is making one.** §7.1 classifies it and says
what depends on it, and does not grade it.

## 13. Stops and clarifications

**NO STOP WAS DECLARED. All acceptance criteria completed.** One primary category
per finding; secondary findings separate.

### 13.1 Stops

**NONE.**

### 13.2 Findings, one primary category each

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — `chi` returns 72
lines of which exactly one is the subject.** Seventy-one are `chiral`,
`chirally`, `machinery`, `machine`, `matching`, or three other physical objects
sharing the symbol — including `\tilde\chi`, the radial mode the argument
explicitly sets aside. §4.4.

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — `m_theta` returns
zero and `m_\theta` returns seven.** A term list written from a description of a
file misses the notation the file uses. §4.1.

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — a loose `eV`
pattern returns 38 hits in `A10`'s second category, all but twelve of them inside
English words.** Word-bounded, the artifact carries three manuscript values,
each quoted with its line. §10.1.

**`REPOSITORY_DEFECT` — the `C3` multi-specification residual remains
unregistered.** It could not trigger in this range (one declaring specification),
but it arose in each of the two preceding ranges with two specifications
declaring differing totals and raised nothing. §10.6.

**`ENVIRONMENT` — `scipy` is declared at `pyproject.toml:12` and is not
installed.** Eighth consecutive task. Not needed here. §1.

**`ENVIRONMENT` — `docs/local/execution_environment.md` declares a Windows
environment that has never been the one used.** Undeclared, unregistered. §1.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the identification at `:80-81`
and `:616-618` is asserted, load-bearing, and unfalsifiable from this
repository.** The object it identifies the mode WITH is defined in a manuscript
that is not here. §7.1.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the four-way taxonomy still
cannot carry the verdict without a scope qualification.** The same question has
two defensible answers depending on which object "the halo profile" names. §11.3.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the retracted SHA attribution
is an instance of a recurring failure this line has now recorded under four
names.** A measurement true of one proposition was carried into an assertion
about another. §11.5.

### 13.3 Clarifications, not defects

**The manuscript is 1833 lines, not 1834.** `wc -l` and `grep -c ""` agree; the
file ends with a newline, so both counting conventions give the same number.
Nothing depends on it. §4.

**My PASS-2-only count is 125 where the specification's author measured 136.**
Both are correct under their own matching convention for `fit`, `derive` and
`m_\theta` in PASS 1. **The substantive claim — `:80` is PASS-2-only and PASS 2
supplies the large majority of the union — reproduces exactly.** §4.3.

**Rule 13's two diagnostic orders were not exercised**, because no environment
failure occurred; I name neither as the one used, per §8 of the specification.

**`refs/heads/main` is a stale local ref at `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`.**
This task's base is `refs/remotes/origin/main` and `main` is not touched. §2.

**The stop-hook's recurring "405 unpushed commits" claim on the session branch is
an artefact of the clone having been unshallowed.** The session branch has
nothing unpublished and is not pushed by this task. §1.
