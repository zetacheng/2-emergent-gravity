# Report — `CHANNEL-B0`: which channel is gravity, and which is a fifth force?

    TASK        channel-b0-spin-scope
    BRANCH      science/channel-b0-spin-scope
    BASE        af145d5a3e36e6bca62f038092748ada3abdcec1
    SPEC SHA    3a80d0c963d634dfae8ae53ea869b41b96b3d33ec618dd5b0b86c6335f98a54a
    REVIEW      APPROVE FOR EXECUTION, bound to that SHA
    VERDICT     CHANNELS SEPARATED — the universality claim is scoped to the
                SPIN-2 TT channel

**EVERY FIGURE IS MEASURED AT COMMIT 3 UNLESS THE LINE SAYS `INTENDED`.** This
report is commit 4. **Nothing here claims to measure commit 4.**

**EVERY SHA IS PASTED FROM COMMAND OUTPUT, WITH THE COMMAND SHOWN.**

## 1. `A3` — environment, run FIRST

**Rule 13's diagnostic order applies and was NOT exercised: no environment
failure occurred.** Rule 13 carries two such orders — a known open item — and I
name neither as the one used.

**Amendment D step 0, before anything else:**

    execution location    vm — Linux 6.18.5-fc-v20
    git common dir        /home/user/2-emergent-gravity/.git
    resolved HEAD at step 0       bfef924c368658cac85c04ed18d96eb4450afba6
    HEAD symbolic ref at step 0   refs/heads/claude/paper-2-independent-verification-dysdp0
    task worktree         /tmp/.../scratchpad/chb0, branch science/channel-b0-spin-scope

**Clone depth, command output pasted:**

    $ git rev-parse --is-shallow-repository
    false
    $ git rev-list --count HEAD
    423
    $ git rev-list --count --all
    539

**NOT SHALLOW.** It was shallow earlier in this session and was deepened with
`git fetch --unshallow`; that is the origin of the recurring stop-hook claim of
405 unpushed commits on the session branch, which is `main`'s own published
history made countable.

**Toolchain, MEASURED:**

    python   3.11.15 (main, Mar  3 2026, 09:26:23) [GCC 13.3.0]
    pytest   9.1.1
    numpy    2.4.6
    sympy    1.14.0
    ruff     0.15.8
    scipy    ABSENT — ModuleNotFoundError: No module named 'scipy'

**`pyproject.toml:12` declares `"scipy>=1.11"` and it is not installed.**
Eleventh consecutive task. This task runs no numerics.

**`docs/local/execution_environment.md` declares a Windows environment**
(`zeta-3070\codexsandboxoffline`, Python 3.12, `C:\p2-validator\venv`). Every run
has been on Linux. Undeclared, unregistered.

## 2. `A1` — repository, refs, branch availability, and `A11`'s stop condition

    $ git remote get-url origin
    https://github.com/zetacheng/2-emergent-gravity

**It identifies `zetacheng/2-emergent-gravity`.**

    $ git rev-parse refs/remotes/origin/main
    af145d5a3e36e6bca62f038092748ada3abdcec1

**A1 expects `af145d5a3e36e6bca62f038092748ada3abdcec1`. MATCH.**

**`A11` REQUIRED A STOP IF `origin/main` HAD ADVANCED WHILE `EPS-B0` RAN AGAINST
THE SAME BASE. IT HAS NOT.** `origin/main` is at the declared evidence base, so
no stop was triggered and no rebase was performed.

    $ git rev-parse refs/heads/main
    1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**A stale local ref, reported for contrast. `main` is not touched by this task.**

**BRANCH AVAILABILITY:**

    refs/heads/science/channel-b0-spin-scope          DID NOT EXIST
    origin refs/heads/science/channel-b0-spin-scope   0 matching refs

### 2.1 `§1a` verified as a CONSTRAINT, not adopted as evidence

**I VERIFIED THAT `EPS-B0` IS ABSENT FROM MY EVIDENCE BASE, WHICH IS THE ONLY
THING ABOUT IT I COULD VERIFY:**

    $ git merge-base --is-ancestor efb8d63f… refs/remotes/origin/main
    exit 1        NOT an ancestor of main
    $ git cat-file -e <base>:derivations/P2-EPS-B0_epsilon-tractability-scope.md
    exit 128      ABSENT from this evidence base

**`§1a`'s statement of `EPS-B0`'s verdict is therefore reported as A REPORTING
CONSTRAINT I WAS GIVEN, not as a finding I verified.** I did not cite it, and
§9.3 confirms the artifact and every commit message contain no reference to it.

**What the constraint required of me was independent of whether it is true:** do
not report the scalar coupling's microscopic magnitude as frozen or derived.
**That constraint would be correct even if I could verify nothing about `ε` at
all**, because §5.2 measures directly that this manuscript states no magnitude.

## 3. `A2` — the review, committed unedited

**FIELD PRESENCE CHECKED FIRST, THEN THE VALUE**, because a review carrying no
`reviewed specification SHA-256:` field would otherwise pass a naive comparison
against an empty string.

    field present?   YES — review line 4 carries "Reviewed specification SHA-256:"
    value            3a80d0c963d634dfae8ae53ea869b41b96b3d33ec618dd5b0b86c6335f98a54a
    uploaded spec    3a80d0c963d634dfae8ae53ea869b41b96b3d33ec618dd5b0b86c6335f98a54a
    IDENTICAL
    committed specs/2026-08-18T2219Z_channel-b0-spin-scope.md   3a80d0c96…  IDENTICAL
    verdict, review line 6   APPROVE FOR EXECUTION

## 4. `A4` — the two-pass inventory

    PASS 1, manuscript lines         PASS 2, manuscript lines
      transverse-traceless   10        tensor              33
      TT                    147        scalar mode          0
      spin-2                 13        angular mode         9
      spin-0                  0        mixing angle         1
      graviton               21        composition          5
      equivalence principle   1        Eötvös               0
      universal              26        test body            0
      fifth force             0        geodesic             0
      Yukawa                  4        source               3
      monopole                3        charge               0
      derivative coupling     0        gauge redundancy     2

      PASS 1 union          212        PASS 2 union        53

    PASS 1 only   203
    BOTH            9
    PASS 2 only    44
    UNION         256      of 1833 lines

**THE RESEARCHER'S SIX FILE COUNTS OVER `derivations/` AND `paper/` REPRODUCE
EXACTLY:** `spin-2` 1 file, `spin-0` 0, `fifth force` 0, `transverse-traceless`
2, `equivalence principle` 1, `universal coupl` 1.

### 4.1 `TT` is 147 lines of noise and 10 of signal

**`TT` matched case-insensitively as a substring returns 147 manuscript lines. As
an uppercase token `\bTT\b` it returns TEN.** The other 137:

    lattice 68 · matter 21 · witten 8 · splitting 7 · ttcheck 6 · lett 6 · attractive 6

**A count of 147 would have suggested the TT channel saturates the manuscript.**

### 4.2 Terms I added, and the one that mattered

**Added: `spin-1/0`, `spin-1`, `scalar channel`, `scalar sector`, `scalar
block`, `species-dependent`, `baryon number`, `charge-to-mass`, `torsion
balance`.**

**`spin-1/0` IS THE ADDITION THAT DECIDED THE VERDICT.** `spin-0` returns zero
lines; **`spin-1/0` returns one — `:812` — and that line is the sharpest
separation statement in the manuscript.** §7.

**`scalar channel` (5 lines) and `scalar sector` (2) carry the contrast that
`scalar mode` (0) misses.**

**Neither supplied list is exhaustive and neither is mine.** I read the union
plus the surrounding argument at each cluster, not the whole file.

## 5. `A5` and `A6` — the two channels' couplings

### 5.1 `A5` — `Z`'s channel and the TT source

**`CONVENTIONS.md:20` defines `Z` as the TT graviton KINETIC COEFFICIENT — a
spin-2 object. It states no coupling.**

**I CONFIRM I DID NOT INFER A COUPLING FROM A KINETIC COEFFICIENT.** A kinetic
coefficient says how a field propagates and is silent about what excites it. The
source below comes from entirely different lines; **had those lines not existed,
this section would report that the repository says nothing.**

**THE REPOSITORY DOES STATE THE TT CHANNEL'S SOURCE — `T^{μν}`, twice:**

    :669-671  S[\psi, h] = S[\psi, \eta] + \frac{\kappa}{2}\int d^4x\;
              h_{\mu\nu}\,T^{\mu\nu} + \mathcal{O}(h^2)
    :673-675  T^{\mu\nu} = \frac{i}{4}\,\bar{\psi}\gamma^{(\mu}
              \!\overleftrightarrow{\partial}{}^{\nu)}\psi + \mathrm{h.c.}
              - \eta^{\mu\nu}\mathcal{L}
    :678-679  "where $T^{\mu\nu}$ is the symmetric energy-momentum tensor of
               the fermions"
    :680      "Note that the source of gravity is the derivative bilinear …"
    :830-831  "Hence all matter couples as $\kappa\int d^4x\,h_{\mu\nu}
               T^{\mu\nu}$ with a common $\kappa$"

**AND IT IS A STRUCTURAL STATEMENT, NOT A COMPUTED SOURCE.** `SRC-B0` established
that no configuration usable for computation is present. **The programme has
computed one side of the TT channel — the kinetic coefficient — and not the
other.**

### 5.2 `A6` — `θ̃`'s coupling, quoted

    :633  One element of this identification remains open: the effective
    :634  coupling of the angular mode to visible (baryonic) matter with the
    :635  scalar (monopole) structure used phenomenologically in
    :636  Ref.~\cite{Cheng:2025sparc}.
    :637  A pure Goldstone couples derivatively; a monopole coupling must be
    :638  induced by the explicit breaking and/or by mixing with the heavy
    :639  radial mode, and is therefore suppressed by powers of
    :640  $\varepsilon$ and the mixing angle.

**THE SUPPRESSION THE MANUSCRIPT GIVES:** a monopole coupling must be INDUCED —
by the explicit breaking and/or by mixing with the heavy radial mode — and is
therefore SUPPRESSED by powers of `ε` and the mixing angle. `:641-643` adds that
establishing the chain quantitatively is deferred and that the cited work treats
the coupling as an effective parameter.

**NO MAGNITUDE IS REPORTED HERE AS FROZEN, DERIVED, OR INDEPENDENTLY
DETERMINED.** The manuscript states none, and this report computes none.

### 5.3 `A6` — universality, the SEPARATE finding

> ## `UNSTATED`

**NOT `NON-UNIVERSAL`, AND THE SUPPRESSION IS NOT EVIDENCE FOR IT.** Suppression
concerns magnitude; universality concerns whether the scalar charge is the same
across matter species or test bodies. **A coupling `g ~ ε·α` with `α` common to
all matter is weak AND universal.**

**SEARCHED FOR ANY STATEMENT OF OBJECT DEPENDENCE. NONE EXISTS:**

    composition-dependent    0        charge-to-mass      0
    composition dependence   0        Eötvös              0
    baryon number            0        test body           0
    per baryon               0        torsion balance     0

**`composition` returns five lines and ALL FIVE ARE `decomposition`** — `:105`,
`:278`, `:380`, `:392`, `:1093`. **Counting them would have returned
`NON-UNIVERSAL` on a substring.**

**`species-dependent` returns two lines, `:196` and `:870`, and both are about
species-dependent LIMITING SPEEDS** — the Lorentz-violation analysis, not matter
species.

**THE ONE ADJACENT FACT, REPORTED BECAUSE IT IS ADJACENT AND NOT BECAUSE IT
SETTLES ANYTHING.** `:634` says the coupling is to *"visible (baryonic) matter"*.
**That names a target, not a charge law.** A coupling to baryonic matter could be
proportional to mass — universal among ordinary bodies — or to some other
baryonic quantity that is not. **The manuscript does not say**, and `:633` calls
the whole coupling "open".

**SO `UNSTATED`, and unstated because the manuscript DEFERS the question**
(`:641-642`), not because it is silent by oversight.

## 6. `A7` — the conflation search

> **COUNT: ZERO.**

**Searched `halo`, `attract`, `gravitational effect`, `gravitational force`,
`gravitational attraction`. EVERY HIT NAMES ITS CHANNEL:**

    :207         "matter halo profile from THE SCALAR SECTOR"        scalar, named
    :126         "Two corrections to THE VECTOR ROUTE … its
                  attractive branch"                                  vector, named
    :407, :417   "an additional attractive pairing operator";
                  "its induced VECTOR COUPLING is repulsive
                  rather than attractive"                             vector, named
    :1270        "Which VECTOR CHANNEL this is matters …
                  The attractive channel"                             vector, named
    :1612, :1677 "the attractive VECTOR CHANNEL"                      vector, named

**THE `attract` HITS ARE NOT ABOUT GRAVITY VERSUS THE SCALAR AT ALL.** They
belong to the Hubbard–Stratonovich channel analysis — which HS channel supports a
bound state. **Counting them as conflation would have been a false positive from
a shared English word.**

**AND THE CLEAREST SEPARATION STATEMENT IS `:1531-1534`:**

    :1531  Ref.~\cite{Cheng:2025sparc}, the lattice fermion framework
    :1532  produces both gravitational dynamics (induced sector) and
    :1533  ultralight dark-matter phenomenology (angular condensate mode)
    :1534  from the same microscopic Lagrangian~\eqref{eq:L0}.

**Both effects named, each with its channel in parentheses, in one sentence.**

## 7. `A8` — the universality claim's scope, and the equivalence principle

### 7.1 The scope is the SPIN-2 TT CHANNEL, and the section states it

    :816  \subsection{Emergent gauge redundancy and universal coupling}
    :818  Up to $\mathcal{O}(p^2/\Lambda^2)$ corrections, the quadratic
    :819  action defined by Eq.~\eqref{eq:PiTT} is the Fierz--Pauli action,
    :820  invariant under linearized diffeomorphisms
    :821  $h_{\mu\nu} \to h_{\mu\nu} + \partial_\mu\xi_\nu
    :822  + \partial_\nu\xi_\mu$ \cite{Fierz:1939ix}.
    :823  This gauge redundancy is not imposed; it emerges from the infrared
    :824  Ward identity.
    :825  Gauge invariance of the linear matter coupling
    :826  $\int h_{\mu\nu}X^{\mu\nu}$ requires
    :827  $\partial_\mu X^{\mu\nu} = 0$, and in a local infrared effective
    :828  theory the unique conserved symmetric tensor (up to improvements)
    :829  is the energy-momentum tensor.
    :830  Hence all matter couples as
    :831  $\kappa\int d^4x\,h_{\mu\nu}T^{\mu\nu}$ with a common $\kappa$:
    :832  the equivalence principle is an emergent consequence of the
    :833  infrared gauge structure.

**THE SCOPE IS NOT INFERRED — IT IS DECLARED IN THE FIRST SENTENCE.** `:818-819`
names *"the quadratic action defined by Eq.~\eqref{eq:PiTT}"*, and `eq:PiTT` is
the TT kernel at `:780-785`, `Γ^{(2)} = Z_h p² P^{TT} + O(p⁴/Λ²)×(non-TT)`.

**EVERY OBJECT IN THE ARGUMENT IS THE SPIN-2 FIELD** — `h_{μν}` at `:821`, `:826`
and `:831`, linearized diffeomorphisms at `:820-822`, the linear coupling
`∫h_{μν}X^{μν}` at `:826`. **`θ̃` does not appear in the subsection at all.**

**WHAT THAT MEANS FOR THE OTHER CHANNEL, STATED CAREFULLY:** the argument
constrains what may couple to `h_{μν}`. **It says nothing about whether an
additional scalar exchange exists or how it couples.** A `θ̃` exchange would be an
interaction beyond `κ∫h_{μν}T^{μν}`, and this subsection neither permits nor
forbids it. **The claim's silence about `θ̃` is a consequence of its scope, not a
statement about `θ̃`.**

### 7.2 The equivalence principle — one of four states

> ## `DERIVED HERE` — for the spin-2 channel, at the level of the linear coupling

**NOT merely `CLAIMED`:** `:825-831` gives an argument with premises and a
conclusion — gauge invariance requires `∂_μ X^{μν} = 0`; the unique conserved
symmetric tensor is the energy-momentum tensor; **"Hence"** all matter couples
with a common `κ`. **The word "consequence" at `:832` is backed by the two
sentences before it.**

**NOT `DERIVED ELSEWHERE AND CITED`:** the only citation in the passage is Fierz,
for the Fierz–Pauli action's form, not for the universality conclusion.

**NOT `TESTED`:** `Eötvös` 0, `test body` 0, `torsion balance` 0, and no
composition-dependence analysis anywhere in the repository.

**AND THE DERIVATION'S OWN LIMITS, RECORDED RATHER THAN GLOSSED:** four lines
long; holds *"up to `O(p²/Λ²)` corrections"* per `:818`; its uniqueness premise is
asserted *"in a local infrared effective theory … (up to improvements)"* at
`:827-829` rather than proved here; and it is a statement at the level of the
LINEAR coupling. **`DERIVED HERE` is the correct state of the four, and it is not
the same as established.**

## 8. `A9` — the verdict

> ## `CHANNELS SEPARATED`
>
> **The repository distinguishes spin-2 from spin-0 mediation, and the
> universality claim is scoped to the SPIN-2 TT CHANNEL.**

### 8.1 The evidence, and it does not rest on vocabulary counts

**FIRST — the two channels contrasted explicitly, `:96`:** *"we verify this by
explicit one-loop lattice computations in both **the scalar channel** and **the
graviton (stress-tensor) channel**."*

**SECOND — both light modes named separately, `:574-576`:** *"The light degrees of
freedom of the theory are exclusively the collective bosonic modes: the angular
condensate mode below, and the induced graviton of Section~\ref{sec:induced}."*

**THIRD, AND SHARPEST — `:810-814` MAKES THE SEPARATION A TEST CRITERION:**

    :810  A lattice measurement of the Barnes--Rivers--projected
    :811  stress-tensor correlator, checking for a single $p^2 = 0$ pole in
    :812  the spin-2 sector with vanishing spin-1/0 residues, is the decisive
    :813  test; we identify it as the key numerical milestone for this
    :814  programme.

**REQUIRING THE SPIN-1/0 RESIDUES TO VANISH IN THE TT CORRELATOR IS AN EXPLICIT
DEMAND THAT THE CHANNELS BE SEPARATE**, and the manuscript calls it the
programme's key numerical milestone.

**FOURTH — `:787-788`:** *"the only possible massless pole resides in the TT
spin-2 channel."*

**FIFTH — `:1531-1534`** attributes the two phenomenologies to the two channels by
name, in one sentence.

**SIXTH — the universality subsection scopes itself to `eq:PiTT` in its opening
sentence and never mentions `θ̃`** — §7.1.

**THE VERDICT RESTS ON READING THE ARGUMENT.** `spin-0` returns zero and `fifth
force` returns zero, **and neither absence was used as evidence for anything.**
The separation is stated in the manuscript's own vocabulary — `spin-1/0`, *the
scalar channel*, *the graviton (stress-tensor) channel*, *the angular condensate
mode*, *the induced graviton* — and **the specification's word list was the thing
that was wrong, exactly as its §3 anticipated it might be.**

### 8.2 The manuscript's own classification of the scalar channel

**REPORTED AS THE MANUSCRIPT'S CLASSIFICATION, NOT DERIVED FROM THE MEDIATOR'S
SPIN.** The manuscript calls the angular mode a DARK-MATTER mechanism at `:81`,
`:443` (*"Condensate; light angular mode (dark matter [cite])"*), `:612`
(*"Identification with the dark-matter mode"*), `:1533` and `:1557`.

**This report neither endorses nor disputes that classification**, and does not
derive it from `θ̃` being spin-0. **A spin-0 mediator is a scalar-mediated
additional force; which ontology it belongs to depends on the coupling structure
— which §5.3 found `UNSTATED`.**

### 8.3 The parameter-independence statement, verbatim as `A9` requires

> **Channel separation does not establish parameter independence.** The spin-0
> and spin-2 observables may be conceptually distinct while the scalar channel's
> strength remains dependent on unresolved microscopic data through `ε`.

### 8.4 The two confirmations `A9` requires

**NO COUPLING MAGNITUDE IS REPORTED AS FROZEN OR DERIVED.** §5.2 reports the
manuscript's suppression statement as a statement; no value appears anywhere in
the artifact or this report.

**`EPS-B0` WAS NOT CITED AS EVIDENCE.** §9.3 measures it: the artifact and every
commit message contain zero occurrences of `EPS-B0`, `eps-b0`, `efb8d63f` and
`BLOCKED PENDING`. **§1a is reported in §2.1 as a constraint I was given and
whose only verifiable part — that the artifact is absent from my base — I
checked myself.**

## 9. `A10` – `A13` — nothing derived, scope, integrity

### 9.1 `A11` — scope

    stated: 4 additions, 0 modifications          INTENDED, final at commit 4
    append_only:  DECISION_LOG.md                 a CHECKER-CONFIGURATION declaration,
                                                  NOT an authorisation to write it
    authorised_gates: []
    base: af145d5a3e36e6bca62f038092748ada3abdcec1
    head: commit 4
    mode: exact
    modify: []
    forbidden_operations: delete, rename, copy, type_change, unmerged, unknown

**CUMULATIVE per commit — MEASURED:**

    base .. commit 1  869a0737     1 addition,  0 modifications
    base .. commit 2  193814f8     2 additions, 0 modifications
    base .. commit 3  85d06a2c     3 additions, 0 modifications
    base .. commit 4               4 additions, 0 modifications   INTENDED

**CONTRIBUTION per commit — MEASURED, separately labelled:**

    commit 1   A specs/2026-08-18T2219Z_channel-b0-spin-scope.md
    commit 2   A reviews/chatgpt/2026-08-18T2219Z_channel-b0-spin-scope.md
    commit 3   A derivations/P2-CHANNEL-B0_spin-channel-scope.md
    commit 4   A reports/2026-08-18T2219Z_channel-b0-spin-scope.md   INTENDED

**Each commit contributes one path, so the two coincide numerically here.** They
are reported separately because that is a fact about this task's shape, not a
general identity.

**`DECISION_LOG.md` was not written; its blob is unchanged — §9.2.**

**The UTC time was measured, not assumed: `2026-08-18T22:19:08Z`, giving the
token `2219Z`.** Commit 1 was made in the same minute.

### 9.2 `A12` — nothing existing changed

    PATHS COMPARED (all paths at the evidence base)    505
    paths at the head                                  508
    paths whose blob DIFFERS at the head                 0
    git diff --name-status base..head                    3 entries, ALL status A
    entries of any other status                          0

**THE MANUSCRIPT BLOB AT BOTH ENDS, as `A12` requires explicitly:**

    $ git rev-parse <base>:paper/emergent_gr_paper_v2_15.tex
    c8246f890b07f53ab8094981cbd5a02972fda4c1
    $ git rev-parse HEAD:paper/emergent_gr_paper_v2_15.tex
    c8246f890b07f53ab8094981cbd5a02972fda4c1

**IDENTICAL. Every line this task quotes was read from a file it did not touch.**

    GATES.md · CONVENTIONS.md · docs/BRANCHING_POLICY.md · DECISION_LOG.md
    scripts/recon2026/proca_curved.py · scripts/recon2026/flat_validation.py
    tests/test_recon2026_flat_limit.py            ALL UNCHANGED

**`derivations/P2-*` RE-MEASURED, not carried: base 49, head 50** — the one
addition is this task's own artifact. **`results/` subtree
`9015049f68d5ace2790b5c62976e798298442bce` at both ends.** Both registers
unchanged.

### 9.3 `A10` — nothing derived

**SEARCHED the artifact and every commit message in the range.**

    CATEGORY                                          ARTIFACT   COMMIT MESSAGES
    a statement about what a channel SHOULD couple to         0                 0
    a computed suppression or mixing factor                   0                 0
    a judgement about whether the EP holds                    0                 0

**AND THE `A9` CONFIRMATIONS, MEASURED THE SAME WAY:**

    EPS-B0            0    0
    eps-b0            0    0
    efb8d63f          0    0
    BLOCKED PENDING   0    0

**A search for any coupling magnitude reported as frozen or derived —
`magnitude is frozen|derived|known`, `coupling is frozen|derived|determined` —
returns nothing in the artifact.**

**The artifact reports what the manuscript says a channel DOES couple to, never
what it should; it quotes the suppression without evaluating it; and it
classifies the equivalence principle's evidentiary state without saying whether
the principle holds.**

**`A10` NAMES THE REPORT AS A SEARCH SUBJECT TOO, AND THIS REPORT IS NOT ZERO —
FOR REASONS THAT HAVE NOTHING TO DO WITH THE PROHIBITION.** A report that must
say what it searched for has to write the patterns down, and a report that must
say which temptation it declined has to name the temptation. **The result is
therefore given POSITIONALLY rather than as a count, because a count of a
document's own pattern list and its own denials changes with every later edit to
that document** — the failure mode this line recorded at `DET-01`'s `A10`.

**POSITIONALLY, AND STABLE UNDER EDITING — outside this section, which
necessarily contains its own patterns:**

    "should couple"            NOWHERE except §9.3's own table row
    a computed factor          NOWHERE at all
    an EP judgement            ONE occurrence, §13's question "Did I want to
                               say the equivalence principle holds?" — a
                               declared temptation followed by "I did not take
                               it", not an assertion

**There is no other place. No sentence in the landed set says what a channel
should couple to, states a computed suppression or mixing factor, or asserts
whether the equivalence principle holds.** **The artifact and every commit
message are clean of all three, and those are the two subjects the prohibition
protects.**

**On `EPS-B0`: this report names it TEN times, and every one is §2.1's or §8.4's
treatment of it as a CONSTRAINT I was given** — including the two places that
record what I verified about it (absent from my base) and the one that records
what I did not verify (its verdict). **The measured zero in the table above is
for the artifact and the commit messages, which is where `A9`'s
non-citation requirement bites.**

### 9.4 `A13` — gate invariants and pins

**Read SCOPED: `P2-PHASE-01` is `GATES.md:971–1108`, bounded by the next
`^## P2-` heading.**

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

## 10. `A14` — the checker over this task's own range

**Base `af145d5a…`, head commit 3. Two runs at both prospectivity readings — four
invocations, all exit `0`.**

**THE OUTPUT WAS PARSED, NOT GREPPED.** Each JSON file was loaded with
`json.loads` and every property read from the parsed structure by key (`id`,
`status`, `classification`, `evidence`). The property list is a JSON *array* of
objects rather than a map keyed by property id, so a key lookup returns `None`,
and a grep for `PASS` would count the word wherever it occurs — including inside
the `does_not_establish` prose every `PARTIAL` property carries.

**`RUN 1` config, verbatim — observational, governs nothing:**

    {
      "base": "af145d5a3e36e6bca62f038092748ada3abdcec1",
      "head": "85d06a2ce23eb25e4d6a720f66ca4f5a6732f25c",
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
      "head": "85d06a2ce23eb25e4d6a720f66ca4f5a6732f25c",
      "specification_paths": [
        "specs/2026-08-18T2219Z_channel-b0-spin-scope.md"
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

**`P5` and `P9` are `NOT_APPLICABLE`, the correct result and not a weak pass.** No
merge in this range; at commit 3 no report exists.

**WHAT `RUN 1` DID.** Its default subject selection discovered exactly ONE
specification in range — this task's, `stated: 4 additions, 0 modifications`,
counted 4 (add 4 / mod 0), parse OK. **`RUN 1` and `RUN 2` are therefore
BYTE-IDENTICAL at each reading**, so the four invocations produce exactly TWO
distinct byte strings differing only at line 252. **That does not make them the
same check: `RUN 2` names the subject and `RUN 1` discovers it.**

**THE `C3` MULTI-SPECIFICATION RESIDUAL DID NOT ARISE — one declaring
specification, the "cannot trigger" half.** It fired in each of the three
integration ranges earlier in this session and remains unregistered.

**Neither the config nor this specification's declarations were adjusted to make
`RUN 2` pass. `RUN 2` passed on its first invocation at both readings.**

### 10.1 The JSON output, verbatim

**`RUN 1` and `RUN 2` at the `INCLUSIVE` reading are BYTE-IDENTICAL, so the file
below IS both outputs. Each `EXCLUSIVE` output is this file with line 252 reading
`"inclusivity": "EXCLUSIVE"`.**

    {
      "base": "af145d5a3e36e6bca62f038092748ada3abdcec1",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "85d06a2ce23eb25e4d6a720f66ca4f5a6732f25c",
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
                "derivations/P2-CHANNEL-B0_spin-channel-scope.md",
                "reports/2026-08-XXT{HHMM}Z_channel-b0-spin-scope.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_channel-b0-spin-scope.md",
                "specs/2026-08-XXT{HHMM}Z_channel-b0-spin-scope.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-18T2219Z_channel-b0-spin-scope.md",
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
                "commit": "869a07370f9f4e5182d4d4d6e9332ea4f2a59f4a",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "193814f843d990c92132a759a94825f44392c82c",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "85d06a2ce23eb25e4d6a720f66ca4f5a6732f25c",
                "work_paths": [
                  "derivations/P2-CHANNEL-B0_spin-channel-scope.md"
                ]
              }
            ],
            "first_review_commit": "193814f843d990c92132a759a94825f44392c82c",
            "first_work_commit": "85d06a2ce23eb25e4d6a720f66ca4f5a6732f25c",
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
              "specs/2026-08-18T2219Z_channel-b0-spin-scope.md"
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
              "commit": "869a07370f9f4e5182d4d4d6e9332ea4f2a59f4a",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "193814f843d990c92132a759a94825f44392c82c",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "85d06a2ce23eb25e4d6a720f66ca4f5a6732f25c",
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
              "specs/2026-08-18T2219Z_channel-b0-spin-scope.md"
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
            "first_commit": "869a07370f9f4e5182d4d4d6e9332ea4f2a59f4a",
            "first_commit_paths": [
              "specs/2026-08-18T2219Z_channel-b0-spin-scope.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-18T2219Z_channel-b0-spin-scope.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-18T2219Z_channel-b0-spin-scope.md"
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

## 11. `A15` and `A16` — validators and hygiene

    $ python3 -m pytest -q
    332 passed, 2 deselected in 37.59s
    exit status 0

**332 passed, 2 deselected, exactly as expected. This task adds no code.**

**`A16` — hygiene. Rule 20 binds this task and was not needed: no message
required repair, no history was rewritten. Every SHA pasted from
`git rev-parse`:**

    commit 1  869a07370f9f4e5182d4d4d6e9332ea4f2a59f4a
              spec: which channel is gravity, and which is a fifth force
    commit 2  193814f843d990c92132a759a94825f44392c82c
              review: pre-execution review for the spin-channel scope
    commit 3  85d06a2ce23eb25e4d6a720f66ca4f5a6732f25c
              scope: the channels are separated and the universality claim is spin-2 only
    commit 4  INTENDED message:
              report: the channels are separated and the universality claim is spin-2 only

    Co-Authored-By          0        Generated with        0
    Co-authored-by          0        Claude-Session        0
    claude.ai/code          0        any model identifier  0
    🤖                      0        noreply@anthropic.com 0

**All zero. `A16` for commit 4 is post-report evidence and is not written here.**

## 12. `§7` — Rule 16 assessment

### 12.1 First — this reports what the repository SAYS

**IT DOES NOT ESTABLISH WHICH CHANNEL IS PHYSICALLY RESPONSIBLE FOR ANYTHING.**

**`CHANNELS SEPARATED` MEANS THE DOCUMENTS ARE CLEAR, NOT THAT THE SEPARATION IS
CORRECT.** The manuscript states that the massless pole is in the TT spin-2
channel and requires the spin-1/0 residues to vanish; **whether they do is the
lattice measurement `:810-814` calls the programme's key numerical milestone, and
it has not been performed.** The separation is a stated structure with a named
outstanding test.

### 12.2 Second — universality and strength are separable, and only the first was assessed

**THIS TASK CLASSIFIED THE SCALAR COUPLING'S STRUCTURE. IT DID NOT REPORT ITS
MAGNITUDE.** §5.2 quotes the manuscript's suppression statement; §5.3 answers
universality separately and returns `UNSTATED`. **Neither answer was used to
support the other.**

**Under §1a's reporting constraint — reported in §2.1 as a constraint I was given
and could not verify — the microscopic magnitude is not reported as frozen or
derived.** **And that constraint costs this task nothing**, because §5.2 measures
directly that the manuscript states no magnitude: `:641-642` defers the chain and
`:642-643` records the cited work treating the coupling as an effective
parameter.

**A NON-UNIVERSAL SCALAR FORCE WOULD NOT BE A DEFECT, AND NEITHER WOULD A
UNIVERSAL ONE.** Scalar-mediated dark matter is a legitimate mechanism; so is a
universally coupled scalar in the gravitational sector. **This is a
CLASSIFICATION, not a criticism** — and the classification returned `UNSTATED`,
so it is not even a classification of the coupling yet.

**AND WHAT THE CLASSIFICATION DOES NOT FOLLOW FROM: not from the mediator's spin,
and not from the coupling's suppression.** Both non-inferences were available and
both were declined — §5.3, §8.2. **The manuscript calls the halo a dark-matter
mechanism, and that is reported as THE MANUSCRIPT'S CLASSIFICATION**, not derived
here from `θ̃` being spin-0.

### 12.3 Third — `Z` is a kinetic coefficient

**IT TELLS NOTHING ABOUT ITS SOURCE.** §5.1 confirms no coupling was read from
it; the source statement comes from `:669-680` and `:830-831`, different lines
entirely.

**THE PROGRAMME HAS COMPUTED ONE SIDE OF THE TT CHANNEL AND NOT THE OTHER**, and
**`SRC-B0` already established that the source side is absent from this
repository** — no configuration usable for computation is present. **The
manuscript states the TT source structurally; nothing computes it.**

### 12.4 Fourth — the equivalence principle's four states are not interchangeable

**A CLAIM IS NOT A DERIVATION; A DERIVATION ELSEWHERE IS NOT A DERIVATION HERE;
AND NEITHER IS A TEST.**

**THE REPOSITORY SUPPORTS `DERIVED HERE`** — an argument with premises and a
"Hence" at `:825-831`, for the spin-2 channel, at the level of the linear
coupling. **Not `CLAIMED`, because there is an argument. Not `DERIVED ELSEWHERE
AND CITED`, because the only citation is Fierz for the action's form. Not
`TESTED`, because `Eötvös`, `test body` and `torsion balance` all return zero.**

**And `DERIVED HERE` is not the same as established** — §7.2 records the
derivation's own four limits, including that its uniqueness premise is asserted
rather than proved.

### 12.5 Fifth — the vocabulary was the Researcher's and both passes missed the wording

**THE SEPARATION IS STATED IN TERMS NEITHER PASS CONTAINS.** `spin-0` returns
zero; the manuscript writes `spin-1/0` at `:812`, *the scalar channel*, *the
graviton (stress-tensor) channel*, *the angular condensate mode*, *the induced
graviton*.

**AN ABSENCE OF `spin-0` AND `fifth force` IS NOT EVIDENCE THAT THE CHANNELS ARE
CONFLATED** — and in this case it was evidence of nothing at all.

**WHAT WAS SEARCHED:** PASS 1's eleven terms, PASS 2's eleven, and nine of my own
— `spin-1/0`, `spin-1`, `scalar channel`, `scalar sector`, `scalar block`,
`species-dependent`, `baryon number`, `charge-to-mass`, `torsion balance`.
**Thirty-one terms, 256 distinct lines of 1833, plus the surrounding argument at
each cluster.** **I did not read the manuscript end to end**, and a separation or
a conflation stated outside all thirty-one would have been missed.

## 13. The temptation, answered directly

**Did reading make me want to decide which channel is right?** **Yes, and the
material makes the decision look easy — which is the warning.** The manuscript
has a spin-2 channel with a derived universal coupling and a spin-0 channel whose
coupling is open, and it is one short step to "so the gravity is the real result
and the dark matter is the speculative part". **That is a judgement about the
physics, and this task's question was whether the documents keep the channels
apart.** I did not make it, and §12.1 says plainly that a clear separation is not
a correct one.

**Did I want to derive the monopole coupling?** **Briefly, and the pull was
technical rather than rhetorical.** `:637-640` names the mechanism — induced by
explicit breaking and/or radial-mode mixing — precisely enough that its
parametric form suggests itself. **Writing it would have answered `A6`'s
universality question by construction rather than by reading**, which is exactly
the inference §4 forbids. **§5.3's answer is `UNSTATED` because the manuscript
does not state it, and I did not supply what it withheld.**

**Did I want to say the equivalence principle holds?** **Yes, and this was the
subtlest one.** `:825-833` is a clean argument and it reads convincingly.
**Reporting `DERIVED HERE` was already the strongest of the four states, and the
step from there to "so the EP holds in this framework" is one word.** I did not
take it: §7.2 records four explicit limits on the derivation, and §12.4 states
that `DERIVED HERE` is not the same as established.

**One restraint nothing asked for.** The verdict is favourable to the
manuscript — the channels ARE separated, and cleanly. **A favourable finding
invites less scrutiny than an unfavourable one**, and §8.1's evidence list is
longer than it needed to be for that reason: six independent passages rather than
the one or two that would have sufficed.

## 14. Stops and clarifications

**NO STOP WAS DECLARED. All acceptance criteria completed.** One primary category
per finding; secondary findings separate.

### 14.1 Stops

**NONE.** `A11`'s stop condition — `origin/main` advancing while `EPS-B0` ran
against the same base — was checked and did not obtain. §2.

### 14.2 Findings, one primary category each

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — `TT` returns 147
manuscript lines as a substring and 10 as an uppercase token.** 68 of the
remainder are `lattice`, 21 `matter`. §4.1.

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — `composition`
returns five lines and all five are `decomposition`.** **Had they been counted,
`A6` would have returned `NON-UNIVERSAL` on a substring**, which is the single
most consequential false positive available in this task. §5.3.

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — the `attract` hits
belong to the Hubbard–Stratonovich vector-channel analysis, not to gravity versus
the scalar.** Counting them as conflation would have been a false positive from a
shared English word. §6.

**`SPECIFICATION_DEFECT` (minor, non-blocking) — the specification's channel
vocabulary did not match the manuscript's.** `spin-0` and `fifth force` return
zero while `spin-1/0` at `:812` carries the separation. **§3 of the specification
anticipated exactly this and said so**, which is why it is recorded as a
vocabulary gap rather than a defect that affected the outcome. §4.2, §8.1.

**`ENVIRONMENT` — `scipy` is declared at `pyproject.toml:12` and is not
installed.** Eleventh consecutive task. Not needed here. §1.

**`ENVIRONMENT` — `docs/local/execution_environment.md` declares a Windows
environment that has never been the one used.** Undeclared, unregistered. §1.

**`REPOSITORY_DEFECT` — the `C3` multi-specification residual remains
unregistered.** It could not trigger in this range, but fired in each of the
three integration ranges earlier in this session. §10.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — `θ̃`'s universality is
`UNSTATED` and the manuscript defers the question explicitly** at `:641-642`.
**It cannot be answered from this repository**, and it is the question that would
decide whether the scalar channel is a fifth force in the
equivalence-principle-violating sense. §5.3.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the spin-1/0 residue test that
would confirm the separation dynamically has not been performed.** `:810-814`
names it as the programme's key numerical milestone. §12.1.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — `§1a`'s statement of `EPS-B0`'s
verdict could not be verified from this evidence base and was not treated as
evidence.** The only verifiable part — that the artifact is absent — I checked
myself: not an ancestor of `main`, `cat-file -e` exit 128. §2.1.

### 14.3 Clarifications, not defects

**`P2-CHANNEL-B0` adds one artifact to `derivations/P2-*`, 49 → 50.** §9.2.

**Rule 13's two diagnostic orders were not exercised**, because no environment
failure occurred; I name neither as the one used, per §8.

**`refs/heads/main` is a stale local ref at `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`.**
This task's base is `refs/remotes/origin/main` and `main` is not touched. §2.

**The stop-hook's recurring "405 unpushed commits" claim on the session branch is
an artefact of the clone having been unshallowed.** The session branch has
nothing unpublished and is not pushed by this task. §1.
