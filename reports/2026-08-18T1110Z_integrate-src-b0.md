# Report — integrate the source-side scope assessment, and land it

    TASK        integrate-src-b0
    BRANCH      science/integrate-src-b0
    BASE        0a7a988cb1c1ca7de4cbfebd46fd690245789a2d
    SOURCE      science/src-b0-source-side-scope
    SPEC SHA    a93e84b8e1a6a8a92196ef96b50997e23ed9821cac2654a66586636bc3df5fac
    REVIEW      APPROVE FOR EXECUTION, bound to that SHA

**EVERY FIGURE IS MEASURED AT COMMIT 3 (`68438490`) UNLESS THE LINE SAYS
`INTENDED`.** This report is commit 4. **Nothing here claims to measure commit
4**; the commit-4 evidence goes to the Reviewer in chat.

**EVERY SHA IN THIS REPORT WAS RESOLVED WITH `git rev-parse` AT REPORTING TIME**,
per §0. None was transcribed from earlier in the session or carried from a prior
report.

## 1. `A3` — environment, run FIRST

**Rule 13's diagnostic order applies and was NOT exercised: no environment
failure occurred.** Rule 13 carries two such orders — a known open item — and I
name neither as the one used.

**Amendment D step 0, before anything else:**

    execution location    vm — Linux 6.18.5-fc-v20
    git common dir        /home/user/2-emergent-gravity/.git
    resolved HEAD at step 0    bfef924c368658cac85c04ed18d96eb4450afba6
    HEAD symbolic ref at step 0  refs/heads/claude/paper-2-independent-verification-dysdp0
    task worktree         /tmp/.../scratchpad/isrcb0, branch science/integrate-src-b0

**Clone depth:**

    git rev-parse --is-shallow-repository    false
    git rev-list --count HEAD                423
    git rev-list --count --all               523

**NOT SHALLOW.** It was shallow earlier in this session and was deepened with
`git fetch --unshallow`; that is the origin of the recurring stop-hook claim of
405 unpushed commits on the session branch, which is `main`'s own published
history made countable. The `--all` count rose from 519 to 523 because this
task's branch and the source branch now carry commits the earlier count did not.

**Toolchain, MEASURED:**

    python   3.11.15 (main, Mar  3 2026, 09:26:23) [GCC 13.3.0]
    pytest   9.1.1
    numpy    2.4.6
    sympy    1.14.0
    ruff     0.15.8
    scipy    ABSENT — ModuleNotFoundError: No module named 'scipy'

**`pyproject.toml:12` declares `"scipy>=1.11"` and it is not installed.** Seventh
consecutive task. The symbolic work in §7 used `sympy`, which is present.

**`docs/local/execution_environment.md` declares a Windows environment**
(`zeta-3070\codexsandboxoffline`, Python 3.12, `C:\p2-validator\venv`). Every run
has been on Linux. Undeclared, unregistered.

## 2. `A1` — repository, refs, and the source tip

**`origin` URL, verbatim as measured, not normalised:**

    https://github.com/zetacheng/2-emergent-gravity

**It identifies `zetacheng/2-emergent-gravity`.**

    refs/remotes/origin/main    0a7a988cb1c1ca7de4cbfebd46fd690245789a2d
    A1 expects                  0a7a988cb1c1ca7de4cbfebd46fd690245789a2d   MATCH
    refs/heads/main             1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab   STALE LOCAL REF

**`refs/heads/main` is reported for contrast and is not the landing
target.** The landing pushes `HEAD:refs/heads/main` to `origin`.

**THE SOURCE TIP, RE-RESOLVED BY `git rev-parse` AT REPORTING TIME — three
independent resolutions:**

    refs/heads/science/src-b0-source-side-scope           cb07f3a9d4a6e2f1461098f4606b8b1b12f7ea56
    refs/remotes/origin/science/src-b0-source-side-scope  cb07f3a9d4a6e2f1461098f4606b8b1b12f7ea56
    git ls-remote origin refs/heads/science/src-b0-...    cb07f3a9d4a6e2f1461098f4606b8b1b12f7ea56
    A1 expects                                            cb07f3a9d4a6e2f1461098f4606b8b1b12f7ea56   MATCH

    git merge-base --is-ancestor <source> origin/main   exit 1 — NOT an ancestor, as required

### 2.1 The reported-SHA finding, measured rather than accepted

**§0 states that the `SRC-B0` execution report gave `8f5e3c4c…` and the `DET-01`
integration report gave `55c2e4a4…`, neither resolvable. I verified both halves
of that claim separately, and they do not both hold.**

**WHAT REPRODUCES:**

    git cat-file -t 8f5e3c4c    fatal: Not a valid object name 8f5e3c4c
    git cat-file -t 55c2e4a4    fatal: Not a valid object name 55c2e4a4

**Neither id names an object in this repository.** That part of §10's pre-issue
record is exactly right.

**WHAT DOES NOT REPRODUCE: the attribution to the reports.**

    git grep for 8f5e3c4c / 55c2e4a4 in the SRC-B0 tree at cb07f3a9    0 hits
    the same, in the DET-01 landing tree at 0a7a988c                    0 hits

**NEITHER STRING APPEARS ANYWHERE IN EITHER COMMITTED REPORT, OR ANYWHERE IN
EITHER TREE.**

**AND I AUDITED EVERY IDENTIFIER IN BOTH REPORTS RATHER THAN ONLY THE TWO
NAMED.** Extracting every distinct 8-to-40-character hex token from each and
resolving each with `git cat-file -e`:

    reports/2026-08-18T0434Z_integrate-det-01.md          50 distinct hex tokens
      not resolvable as git objects: 04cce754, d571cf4b   — sha256 FILE DIGESTS,
                                                            correctly not git objects
                                     10775238428919313,
                                     10775238428919343   — fragments of the float
                                                            −0.10775238428919313
    reports/2026-08-18T0507Z_src-b0-source-side-scope.md  29 distinct hex tokens
      not resolvable as git objects: a14625c4             — a sha256 FILE DIGEST

**EVERY TOKEN PRESENTED AS A GIT OBJECT IN EITHER REPORT RESOLVES.** The four
exceptions are file digests and a decimal fraction, none of which is offered as
a commit id.

**Both committed reports also decline to state their own commit-4 SHA at all**,
because §5 of each forbade claiming to measure commit 4 — so the id §0 says they
gave is an id neither was permitted to contain.

**I DO NOT KNOW WHERE THE TWO IDS CAME FROM, AND I DO NOT SPECULATE.** What I
can measure is the repository, and the repository says the reports are clean.
**Neither report is repaired, per §3, and neither needs repair.**

**§0'S OPERATIVE INSTRUCTION IS SOUND INDEPENDENTLY OF ITS PREMISE, AND I
FOLLOWED IT:** every SHA in this report was re-resolved with `git rev-parse` at
reporting time. **A reported identifier that nothing checks is exactly the kind
of evidence that can drift**, and §7.5 records that as the standing gap.

## 3. `A2` — the review, committed unedited

**FIELD PRESENCE CHECKED FIRST, THEN THE VALUE**, because a review with no
`reviewed specification SHA-256:` field at all would otherwise pass a naive
comparison against an empty string.

    field present?    YES — review line 4 carries "Reviewed specification SHA-256:"
    value             a93e84b8e1a6a8a92196ef96b50997e23ed9821cac2654a66586636bc3df5fac
    uploaded spec     a93e84b8e1a6a8a92196ef96b50997e23ed9821cac2654a66586636bc3df5fac
    IDENTICAL
    committed specs/2026-08-18T1110Z_integrate-src-b0.md   a93e84b8…   IDENTICAL
    verdict, line 6   APPROVE FOR EXECUTION

**The review is committed byte-for-byte as received.**

## 4. `A10` — which merge case, stated BEFORE the blob comparisons

    merge-base(commit 2, source)   0a7a988cb1c1ca7de4cbfebd46fd690245789a2d
    evidence base                  0a7a988cb1c1ca7de4cbfebd46fd690245789a2d
    IDENTICAL
    commits on origin/main after the base    0

**THE MERGE-BASE IS THE EVIDENCE BASE, SO NO COMMIT ON `main` COULD HAVE TOUCHED
AN ARRIVING PATH.** `main` has not moved since the source branched, so the four
arriving additions cannot collide with anything.

**Then the four blob comparisons — the arriving blob at the source tip against
the same path at the merge head:**

    derivations/P2-SRC-B0_source-side-scope.md              68660548ac08 → 68660548ac08  IDENTICAL
    reports/2026-08-18T0507Z_src-b0-source-side-scope.md    f8403f0e9f54 → f8403f0e9f54  IDENTICAL
    reviews/chatgpt/2026-08-18T0507Z_src-b0-source-...md    ab7b1916eaaf → ab7b1916eaaf  IDENTICAL
    specs/2026-08-18T0507Z_src-b0-source-side-scope.md      b9cd1ff9feb1 → b9cd1ff9feb1  IDENTICAL

**Everything arriving by merge is integrated exactly as reviewed.**

## 5. `A5` — no conflict

    git merge-tree --write-tree (dry run)   exit 0, tree bdbe04ae344639c125634b3dc5c2a10166e9056e
    conflict list                           EMPTY
    git merge --no-ff                       exit 0, 'ort' strategy
    unmerged paths after the merge          0
    git ls-files -u                         0 lines

**The conflict list is empty, as required. Any conflict would have been an
immediate stop.**

## 6. `A4` — merge parentage, three separately derived

    parent 1 (git rev-parse HEAD^1)      d787a7ce940f754605bb211b7da792f3237ba20c
    parent 2 (git rev-parse HEAD^2)      cb07f3a9d4a6e2f1461098f4606b8b1b12f7ea56
    merge-base(parent 1, parent 2)       0a7a988cb1c1ca7de4cbfebd46fd690245789a2d
    commit 1 is an ancestor of parent 1  exit 0

**Parent 1 is this task's review commit, parent 2 is the source tip AS
RE-RESOLVED, and their merge-base is the evidence base.** Each value came from
its own command.

## 7. `A6` — §1a re-derived, not transcribed

### 7.1 The variation of an ultralocal functional does not vanish

**METHOD: symbolic, `sympy` 1.14.0, over a general symmetric `4×4` inverse
metric `g^{μν}` of ten free symbols. Two cases, because one case would not
establish the general claim.**

**CASE A — the specific `F` the `DET-01` ambiguity produces.** In four
dimensions `det G1 = ∏ₓ det g(x)`, so the candidate difference is
`±½ Σₓ log det g(x)`; take `F(g) = ½ log det g`:

    δ/δg^{μν}(y)  Σₓ F(g(x))  =  [ ∂F/∂g^{μν} ](y) · δ_{x,y}     ULTRALOCAL

    ∂/∂g^{μν} [ ½ log det g ]  =  − ½ g_{μν}

**Every component matched the closed form with residual exactly `0`**, taking
the symmetric-matrix multiplicity into account for the off-diagonal symbols.

**IT DOES NOT VANISH.** `−½ g_{μν}` is zero only if `g_{μν} = 0`, which is not
an admissible metric — the inverse metric would be singular.

**CASE B — a general ultralocal `F`, to show the conclusion is not an accident
of that particular `F`.** For `F = a log det g^{μν} + b det g^{μν} + c tr g^{μν}`,
the derivative `∂F/∂g^{00}` is a non-trivial rational function of the ten
symbols plus `c`, and **it is identically zero only if `a = b = c = 0`, i.e.
only if `F` is constant.**

**THE GENERAL STATEMENT, WHICH IS WHAT MATTERS:**

> **Ultralocality constrains WHERE the variation is supported — a `δ_{x,y}`,
> with no derivatives of the metric — not WHETHER it is zero.** **A functional
> that is ultralocal and non-constant has a non-vanishing metric variation.**

**THEREFORE IT CONTRIBUTES TO `T_μν`.** `T_μν = (2/√g) δΓ/δg^{μν}` is a
variation with respect to `g`, so an ambiguity that survives the variation
enters the stress tensor. **The contribution is itself ultralocal and, for the
`DET-01` case, proportional to `g_{μν}` — an undetermined vacuum-like source
term.**

**`DET-01`'s rider proved the ambiguity harmless for the `m² ln m²` coefficient
of `Z`. That is a statement about a coefficient in an expansion, not about a
functional derivative, and it does not extend to one.**

### 7.2 Why `d = 4` does not rescue it

**MEASURED, from two determinant identities — `det(cM) = c^d det M` and
`det(M⁻¹) = 1/det M`:**

    det[ √(det g) · g⁻¹ ] = (√(det g))^d · (det g)⁻¹ = (det g)^{d/2 − 1}

    d = 2   (det g)^0     = 1, IDENTICALLY
    d = 3   (det g)^{1/2}
    d = 4   (det g)^1     = det g
    d = 5   (det g)^{3/2}
    d = 6   (det g)^2

**Confirmed symbolically with the full inverse at `d = 2` and `d = 3` —
`lhs − rhs` simplifies to `0` in both — and numerically on random symmetric
positive-definite matrices at `d = 4, 5, 6`, worst relative deviation
`3.6e-15`.**

**THE TWO STATEMENTS ARE ABOUT DIFFERENT THINGS, AND THAT IS THE WHOLE
ANSWER:**

    (i)   d = 4 fixes the FORM of the determinant: det G1 = ∏ₓ det g(x).
    (ii)  the variation then acts on that form: ∂/∂g^{μν}[½ log det g] = −½ g_{μν}.

**`(i)` is what makes `F` explicit. It does not make `∂F/∂g` vanish.** Being
able to write the ambiguity down in closed form is not the same as its
derivative being zero — **if anything it is the opposite, since a closed form is
exactly what lets the derivative be computed.**

**THE ONE DIMENSION WHERE THE VARIATION DOES VANISH IS `d = 2`, AND IT VANISHES
FOR THE OPPOSITE REASON.** There `det[√g g⁻¹] = 1` identically, so
`F = ½ log 1 = 0`: **the ambiguity is EMPTY, not cancelled.** There is nothing to
differentiate. **`d = 4` is the dimension in which the term exists and is
simplest — not the dimension in which it goes away.**

### 7.3 What this finding changed, and its exact strength

**THIS IS THE FINDING THAT CHANGED WHAT THE PROPOSED CALCULATION WOULD
REQUIRE.** A landing that carried `NOT PRESENT` without it would leave the
programme unaware that a `Γ`-defined source observable carries a second
prerequisite.

**AND IT IS CONDITIONAL, NOT UNCONDITIONAL** — see §9. **A landing that stated
it unconditionally would overstate what was established**, because the same
execution located a classical-action definition in the repository that does not
inherit it.

## 8. `A7` — the two-level report

### 8.1 The eight literal term counts

**Files matching, `git grep -lic` over the whole tree. TWO measurements, at two
heads, because they differ and the difference is entirely explained:**

    TERM              AT COMMIT 3   AT THE EVIDENCE BASE
    sparc                       7                      3
    halo                        9                      3
    yukawa                     11                      7
    domain wall                 6                      2
    profile                    12                      6
    r_c                        58                     53
    soliton                     4                      0
    rotation curve              4                      0

**THE EVIDENCE-BASE COLUMN REPRODUCES THE RESEARCHER'S MEASUREMENT EXACTLY, ON
ALL EIGHT TERMS.** The commit-3 column is higher because this task's
specification and review, and the four arriving `SRC-B0` documents, are now in
the tree and all of them discuss these terms. **Both columns are correct at
their own head; neither supersedes the other.**

**`soliton` and `rotation curve` go from `0` to `4` purely that way**: the four
files that mention them are this task's specification, its review, the `SRC-B0`
specification, and the `SRC-B0` report — **documents about the search, not
material found by it.**

### 8.2 Where the non-zero hits live

**At the evidence base, excluding this task's and `SRC-B0`'s own documents:**

    sparc (3)         paper/emergent_gr_paper_v2_15.tex
                      results/recovered-2026/emergent_gr_paper_v2_7.tex
                      results/recovered-2026/session_log_full.md
    halo (3)          the same three files
    yukawa (7)        P2-LATTICE-MICROSPEC-01_rp-gap-classification.md
                      P2-LATTICE-MICROSPEC-01_rp-literature-coverage.md
                      reports/2026-08-16T1952Z_d1-literature-coverage-audit.md
                      reports/2026-08-16T2255Z_d1b-rp-gap-classification.md
                      paper + recovered twin + session_log_full.md
    domain wall (2)   P2-LATTICE-MICROSPEC-01_rp-dependency-ledger.md
                      reports/2026-08-17T0322Z_d1c-dependency-reduction.md
    profile (6)       P2-BETAV-RECON-01a_construction-and-flat-validation.md
                      scripts/recon2026/proca_curved.py
                      reports/2026-08-16T2121Z_integrate-d1-coverage.md
                      reports/2026-08-17T1653Z_recon-01a-construction.md
                      paper + recovered twin

**AND EACH IS A DIFFERENT OBJECT FROM THE ONE THE SEARCH IS LOOKING FOR:**

- **`yukawa`** is `D-1`'s reflection-positivity literature — `rp-gap-classification.md:171`
  reads "a different chiral Yukawa interaction treated; the programme
  interaction is not", and `rp-literature-coverage.md:41` catalogues a
  Kikukawa–Usui paper with "a non-gauge chiral Yukawa example, not the
  programme interaction". **Lattice-fermion formalism, not a dark-matter
  profile.**
- **`domain wall`** is `rp-dependency-ledger.md:270`, an enumeration of fermion
  discretisations — "domain wall, overlap, staggered, finite volume". **A
  lattice regularisation, not a field configuration.**
- **`profile`** in `proca_curved.py:37` and `:147` is `C6`'s single-cosine
  **weak-field background** — the metric perturbation `h`, not a matter
  distribution.
- **`sparc` and `halo`** are the manuscript's references to Paper 1 and the
  recovered chat log.

**`r_c` DESERVES ITS OWN LINE, BECAUSE THE LITERAL COUNT IS ALMOST ENTIRELY
NOISE.** As a substring, 53 files at the base and 58 at commit 3. **As a token
`\br_c\b`, it is TWO files at the base** — the manuscript and its recovered twin
— **and seven at commit 3, the five extra being this task's and `SRC-B0`'s own
documents.** **A count of 53 that is really 2 is the clearest illustration in
this task of why a literal count is not a finding.**

### 8.3 The verdict, and which measurement it is

> **THE VERDICT IS THE AVAILABILITY FINDING:
> `NOT PRESENT / EXTERNAL STATUS NOT DETERMINED`.**
>
> **THE EIGHT LITERAL COUNTS ARE NOT THE VERDICT.** They are lexical
> measurements, they are non-zero, and not one of the hits is a usable source
> configuration.

**The source-side calculation cannot presently be executed from repository
materials.** There is no configuration here whose `T_μν` could be computed.

**The `SRC-B0` specification asked for eight term counts and did not require the
literal/available distinction. The source executor drew it anyway.** That was
right: a report of eight non-zero counts without the distinction would have read
as "material exists". **`A7` now requires both, which closes the gap.**

**NO INFERENCE WAS DRAWN ABOUT ANY EXTERNAL PROFILE'S PROVENANCE.** `NOT
PRESENT` and `FITTED` are different findings and the second cannot be reached
from here. §11.2 records why that is a measurement rather than a courtesy.

## 9. `A8` — the prerequisites, enumerated and correctly quantified

**ONE UNCONDITIONAL PREREQUISITE AND ONE CONDITIONAL ONE. NOT TWO
UNCONDITIONAL ONES.**

    UNCONDITIONAL   A USABLE SOURCE CONFIGURATION.
                    Without it neither a classical source stress tensor nor a
                    Γ-defined one can be evaluated for the proposed object.
                    This prerequisite attaches on every route.

    CONDITIONAL     THE FUNCTIONAL MEASURE, OR AN ADMISSIBLE SOURCE-SIDE
                    SUBTRACTION PRESCRIPTION — IF AND ONLY IF the source
                    observable is defined through the full quantum effective
                    action Γ.

**THE CONDITION, STATED EXPLICITLY:**

    T_μν = (2/√g) δΓ/δg^{μν}    INHERITS the unfixed measure — §7.1 shows the
                                ambiguity survives the variation
    T_μν = (2/√g) δS/δg^{μν}    DOES NOT — a metric variation of a classical
                                action involves no functional measure at all

**The repository supplies the second form itself**, at
`paper/emergent_gr_paper_v2_15.tex:673-676`, where `T^{μν}` is a bilinear
operator built from the classical action. **A classical-action-defined stress
tensor does not inherit the measure prerequisite.**

**WHICH DEFINITION THE PROGRAMME REQUIRES IS UNRESOLVED**, and this task does
not settle it. It depends on the source construction, which does not exist yet:
a one-loop condensate expectation value takes the first route, a classical
soliton of a stated effective action the second. **The integration does not
choose between absolute and background-subtracted, or between `Γ`-defined and
`S`-defined, source stress energy.**

### 9.1 The subtraction rule's ACTUAL state, all five points verified

**I did not report that no prescription exists. I checked each point against the
repository.**

    (1) DOES A PRESCRIPTION EXIST?
        YES. P2-LATTICE-ONTOLOGY-01.md:232-234 establishes that the observable
        is a RESPONSE and that "a baseline subtraction (relative to the
        flat/reference configuration) remains". Its required structure is
        specified at :238-252 — a reference EQUIVALENCE CLASS plus an
        invariance requirement, with the verifiable form ΔE[r₁] = ΔE[r₂].

    (2) WHAT IS ITS FROZEN SCOPE?
        RESPONSE OBSERVABLES. ONTOLOGY:288-291, marked "Governance separation
        (frozen)": "the response subtraction of §2 authorizes removing the
        common baseline from RESPONSE observables only".

    (3) DOES THAT SCOPE AUTHORIZE SOURCE-SIDE USE?
        NO. The same frozen clause limits it to response observables, and the
        proposed calculation needs a source observable.

    (4) IS IT SCOPED AWAY FROM COSMOLOGICAL SOURCE ENERGY?
        YES, EXPLICITLY. ONTOLOGY:290-292: "it does not authorize deleting the
        substrate energy from the cosmological SOURCE. … Response energy and
        source energy are separate ledger entries until that map is frozen."

    (5) IS COMMUTATION WITH METRIC VARIATION SETTLED?
        NO. P2-LATTICE-ROUTE-01.md:247-248 lists among the things a later gate
        must verify: "whether the flat/reference subtraction is applied before
        or after ∂/∂G; and whether the derivative and the subtraction commute."

**AND A SIXTH FACT THAT BEARS ON (1):** even for response observables the rule
is not fully frozen. `ONTOLOGY:254-257` says the renormalization deliverable
"collapses into a finite, explicit subtraction-and-matching rule, **which
FIERZSUM must still freeze**", and `:191` records "Reference equivalence class
and matching conditions | DELEGATED: FIERZSUM §4.2 / D-pre".

**THE CORRECT REPOSITORY STATEMENT, THEREFORE:**

> **No repository prescription AUTHORIZES the required SOURCE-side subtraction.
> The existing frozen subtraction is scoped to RESPONSE observables and is
> explicitly scoped away from cosmological source energy, and whether it
> commutes with metric variation remains open.**

**"EXISTS BUT IS NOT AUTHORIZED FOR THIS USE" AND "DOES NOT EXIST" ARE DIFFERENT
PROGRAMME STATES**, and the difference is not cosmetic: **the first means a
governed extension has to be argued past an explicit refusal; the second would
mean the ground is simply empty.** The repository has already considered whether
the response subtraction reaches the source and said no.

**A separate observation, and it is why the algebra does not settle this.** The
ambiguity's contribution to `T_μν` is configuration-independent, so a contrast
taken between two configurations at the same metric cancels it algebraically.
**That is an algebraic cancellation, not a governed physical definition.** A
programme-level source subtraction needs an authorized prescription, and §3
forbids this task from defining one. **I did not.**

## 10. `A9`, `A11`, `A12`, `A13` — scope and integrity

### 10.1 `A9` — scope

    stated: 7 additions, 0 modifications          INTENDED, final at commit 4
    append_only:  DECISION_LOG.md                 a CHECKER-CONFIGURATION declaration,
                                                  NOT an authorisation to write it
    authorised_gates: []
    base: 0a7a988cb1c1ca7de4cbfebd46fd690245789a2d
    head: commit 4
    mode: exact
    modify: []
    forbidden_operations: delete, rename, copy, type_change, unmerged, unknown

**`DECISION_LOG.md` was not written; its blob is unchanged — §10.2.**

**CUMULATIVE per commit — MEASURED:**

    base .. commit 1  58cfe7e7     1 addition,  0 modifications
    base .. commit 2  d787a7ce     2 additions, 0 modifications
    base .. commit 3  68438490     6 additions, 0 modifications
    base .. commit 4               7 additions, 0 modifications   INTENDED

**SOURCE'S OWN CONTRIBUTION — MEASURED, separately labelled:**

    base .. cb07f3a9   4 additions, 0 modifications

      derivations/P2-SRC-B0_source-side-scope.md
      reports/2026-08-18T0507Z_src-b0-source-side-scope.md
      reviews/chatgpt/2026-08-18T0507Z_src-b0-source-side-scope.md
      specs/2026-08-18T0507Z_src-b0-source-side-scope.md

**`6` IS CUMULATIVE, NOT THE MERGE'S CONTRIBUTION.** The merge contributes four;
the range contains six at commit 3 because commits 1 and 2 added two more.
**They are not addends** — a reviewer of an earlier task added a cumulative
figure to a contribution and got a total three too high.

**ARRIVING PATH COUNT `4`; ARRIVING ADDITION COUNT `4`. THEY COINCIDE, at
four**, because every arriving path is an addition and none arrives twice. They
are reported separately because they would diverge if the source had modified a
path as well as adding one.

**Seven paths in the final manifest: four arrive by merge, three authored here.**

**The UTC time was measured, not assumed: `2026-08-18T11:10:13Z`, giving the
token `1110Z`.** Commit 1 was made in the same minute.

### 10.2 `A11` — nothing existing changed

    PATHS COMPARED (all paths at the evidence base)    491
    paths at the head                                  497
    paths whose blob DIFFERS at the head                 0
    git diff --name-status base..head                    6 entries, ALL status A
    entries of any other status                          0

    GATES.md                              2b3bd5069414f009…   UNCHANGED
    CONVENTIONS.md                        8badc51f38d85d54…   UNCHANGED
    docs/BRANCHING_POLICY.md              3f0f35d4da448eb4…   UNCHANGED
    DECISION_LOG.md                       d9dd2bf3a8cca405…   UNCHANGED
    scripts/recon2026/proca_curved.py     03f46905e5798fb7…   UNCHANGED
    scripts/recon2026/flat_validation.py  6b21f9d6db67641e…   UNCHANGED
    tests/test_recon2026_flat_limit.py    1d7ba5672614dedc…   UNCHANGED

**`derivations/P2-BETAV-*` RE-MEASURED, not carried: EIGHT at the base and
EIGHT at the head.** The specification's own note — seven at the previous base,
the `DET-01` landing adding one — reproduces, and this task adds none.

**Seven microspec artifacts, all unchanged. Two files under
`scripts/recon2026/`.** **Both registers unchanged.**

**`paper/` and `results/` verified by SUBTREE OBJECT, one comparison each:**

    paper/    8af4fcc6c126e6ba20d7d44770c8c1d1eb12bef0   base = head
    results/  9015049f68d5ace2790b5c62976e798298442bce   base = head

**`paper/` matters here more than usual**, because §7 and §8 of this report quote
the manuscript repeatedly. **The subtree object is identical, so nothing I quoted
was altered by quoting it.**

### 10.3 `A12` — gate invariants and pins

**Read SCOPED: `P2-PHASE-01` is `GATES.md:971–1108`, bounded by the next
`^## P2-` heading, and every value was taken inside those bounds.**

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

**The three `BETAV` statuses, each read inside its own section:**

    P2-BETAV-RECON-01   heading :725   :727  Status: PROPOSED (not run; distinct from
                                             the historical circularity question)
    P2-BETAV-CIRC-01    heading :328   :330  Status: RUN
    P2-BETAV-01         heading :207   :209  Status: PROPOSED (deferred — not computed
                                             this sweep)

**An unscoped read returns `GATES.md:15` for all three** — the status of
`P2-HK-01`, the first gate in the file — **which is a real status of a real gate
and therefore reads as entirely plausible.** The values above are bounded.

**`Regression anchors` inside `P2-BETAV-RECON-01`, `GATES.md:753-754`: still
`None yet (proposed)`.** No regression anchor was registered by this task.

### 10.4 `A13` — superseded branches, before the advance

**Six separate `git merge-base --is-ancestor <c> origin/main` invocations. Exit
`1` means NOT an ancestor, which is required.**

    52f65117  exit 1     ebd531ab  exit 1     40168469  exit 1
    7146a093  exit 1     10c260b9  exit 1     d64cd912  exit 1

    origin/main at measurement time    0a7a988cb1c1ca7de4cbfebd46fd690245789a2d

**And against this task's own head (commit 3), which the landing will make
`main`: all six exit `1`.** **None can enter `main` by this landing.** The
after-the-advance re-run is post-report evidence and is not written here.

## 11. `A14` — the checker over this task's own range

**Base `0a7a988c…`, head commit 3 `68438490…`. Two runs at both prospectivity
readings — four invocations, all exit `0`.**

**THE OUTPUT WAS PARSED, NOT GREPPED.** Each JSON file was loaded with
`json.loads` and every property read from the parsed structure by key (`id`,
`status`, `classification`, `evidence`). The property list is a JSON *array* of
objects, not a map keyed by property id — a key lookup returns `None`, and a
grep for `PASS` would count the word wherever it occurs, including inside the
`does_not_establish` prose that every `PARTIAL` property carries.

**`RUN 1` config, verbatim — observational, governs nothing:**

    {
      "base": "0a7a988cb1c1ca7de4cbfebd46fd690245789a2d",
      "head": "6843849016e4da260e322216526dfabc1505038e",
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
      "head": "6843849016e4da260e322216526dfabc1505038e",
      "specification_paths": [
        "specs/2026-08-18T1110Z_integrate-src-b0.md"
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
The `EXCLUSIVE` output differs from the `INCLUSIVE` one at exactly one line —
314 of 318 for `RUN 1`, 291 of 295 for `RUN 2` — that value only. **No property
result changes between readings.**

**Results, identical across all four invocations:**

    P1  PASS  PARTIAL     scope manifest arithmetic
    P2  PASS  MECHANICAL  Rule 15 commit order
    P3  PASS  PARTIAL     append-only on both measures         declared_source: specification
    P4  PASS  MECHANICAL  superseded branches are not merged
    P5  PASS  PARTIAL     merge parentage against recomputed facts
    P6  PASS  PARTIAL     commit-message hygiene
    P7  PASS  PARTIAL     gate integrity                       declared_source: specification
    P8  PASS  MECHANICAL  Rule 15 placement and specification-first
    P9  PASS  MECHANICAL  reports carry a Stops and clarifications section

    overall                        PASS
    exit status, all four           0
    NOT_DECLARED                    none
    NOT_PARSEABLE                   none
    DECLARATION_CONFLICT            NONE — confirmed
    commits_in_range                7
    commits_on_first_parent_line    3
    prospectivity in scope 3, out of scope []

**`P7` REPORTS FOURTEEN SECTIONS** — `section_count_base` 14,
`section_count_head` 14, `raw_heading_count_base` 14, `raw_heading_count_head`
14. **`PASS` at zero would have been a stop; it is not zero.**

**`P5` is `PASS` rather than `NOT_APPLICABLE`** — this range contains a merge and
the checker recomputed its parentage independently. **`P9` is `PASS` on the
arriving `SRC-B0` report**, which carries its `Stops and clarifications` section.

### 11.1 What `RUN 1` did, and the `C3` residual

**`RUN 1`'s default subject selection discovered TWO specifications in range:**

    specs/2026-08-18T0507Z_src-b0-source-side-scope.md
      stated: 4 additions, 0 modifications    counted 4 (add 4 / mod 0)   parse OK
    specs/2026-08-18T1110Z_integrate-src-b0.md
      stated: 7 additions, 0 modifications    counted 7 (add 7 / mod 0)   parse OK

**`RUN 2` names only this task's and therefore sees one.** That is the entire
difference between the two outputs: `RUN 1`'s JSON carries the extra `SRC-B0`
evidence block and the extra path in two subject lists. **`RUN 1` discovers the
subject; `RUN 2` names it. That is not the same check even when the verdicts
agree.**

**THE `C3` MULTI-SPECIFICATION RESIDUAL AROSE AGAIN AND AGAIN RAISED NOTHING.**
Two specifications, **stated totals `4` and `7` — differing — and no
`DECLARATION_CONFLICT`.** `_declarations_from_specs` compares `append_only_paths`
and `authorised_modified_gates`, which agreed (`["DECISION_LOG.md"]` and `[]`);
**it does not compare stated totals.**

**THIS IS THE FIFTH INDEPENDENT RANGE IN THIS SESSION TO EXHIBIT IT, AND THE
SECOND IN WHICH TWO GENUINELY DIFFERING DECLARATIONS WERE BOTH PRESENT.** Still
unregistered. **Not a stop: `P1`'s per-specification arithmetic is correct for
each specification taken alone.**

**Neither the config nor this specification's declarations were adjusted to make
`RUN 2` pass. `RUN 2` passed on its first invocation at both readings**, and
every value in both configs came from the specification.

### 11.2 The JSON outputs, verbatim

**`RUN 1`, `INCLUSIVE` reading — 318 lines. The `EXCLUSIVE` output is this file
with line 314 reading `"inclusivity": "EXCLUSIVE"`.**

    {
      "base": "0a7a988cb1c1ca7de4cbfebd46fd690245789a2d",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "6843849016e4da260e322216526dfabc1505038e",
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
                "derivations/P2-SRC-B0_source-side-scope.md",
                "reports/2026-08-18T0507Z_src-b0-source-side-scope.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-src-b0.md",
                "reviews/chatgpt/2026-08-18T0507Z_src-b0-source-side-scope.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-src-b0.md",
                "specs/2026-08-18T0507Z_src-b0-source-side-scope.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-src-b0.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-18T1110Z_integrate-src-b0.md",
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
                "commit": "58cfe7e7d64f86055f09ca5cd8659ec0cfeb526a",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "d787a7ce940f754605bb211b7da792f3237ba20c",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "6843849016e4da260e322216526dfabc1505038e",
                "work_paths": [
                  "derivations/P2-SRC-B0_source-side-scope.md"
                ]
              }
            ],
            "first_review_commit": "d787a7ce940f754605bb211b7da792f3237ba20c",
            "first_work_commit": "6843849016e4da260e322216526dfabc1505038e",
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
              "specs/2026-08-18T0507Z_src-b0-source-side-scope.md",
              "specs/2026-08-18T1110Z_integrate-src-b0.md"
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
              "merge": "6843849016e4da260e322216526dfabc1505038e",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "0a7a988cb1c1ca7de4cbfebd46fd690245789a2d",
              "recomputed_parent_1": "d787a7ce940f754605bb211b7da792f3237ba20c",
              "recomputed_parent_2": "cb07f3a9d4a6e2f1461098f4606b8b1b12f7ea56",
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
              "commit": "58cfe7e7d64f86055f09ca5cd8659ec0cfeb526a",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "d787a7ce940f754605bb211b7da792f3237ba20c",
              "matches": [],
              "status": "PASS"
            },
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
            },
            {
              "commit": "cb07f3a9d4a6e2f1461098f4606b8b1b12f7ea56",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "6843849016e4da260e322216526dfabc1505038e",
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
              "specs/2026-08-18T0507Z_src-b0-source-side-scope.md",
              "specs/2026-08-18T1110Z_integrate-src-b0.md"
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
            "first_commit": "58cfe7e7d64f86055f09ca5cd8659ec0cfeb526a",
            "first_commit_paths": [
              "specs/2026-08-18T1110Z_integrate-src-b0.md"
            ],
            "reports_added": [
              "reports/2026-08-18T0507Z_src-b0-source-side-scope.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-18T1110Z_integrate-src-b0.md",
              "reviews/chatgpt/2026-08-18T0507Z_src-b0-source-side-scope.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-18T1110Z_integrate-src-b0.md",
              "specs/2026-08-18T0507Z_src-b0-source-side-scope.md"
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
              "path": "reports/2026-08-18T0507Z_src-b0-source-side-scope.md",
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

**`RUN 2`, `INCLUSIVE` reading — 295 lines, stop-governing. The `EXCLUSIVE`
output is this file with line 291 reading `"inclusivity": "EXCLUSIVE"`.**

    {
      "base": "0a7a988cb1c1ca7de4cbfebd46fd690245789a2d",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "6843849016e4da260e322216526dfabc1505038e",
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
                "derivations/P2-SRC-B0_source-side-scope.md",
                "reports/2026-08-18T0507Z_src-b0-source-side-scope.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-src-b0.md",
                "reviews/chatgpt/2026-08-18T0507Z_src-b0-source-side-scope.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-src-b0.md",
                "specs/2026-08-18T0507Z_src-b0-source-side-scope.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-src-b0.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-18T1110Z_integrate-src-b0.md",
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
                "commit": "58cfe7e7d64f86055f09ca5cd8659ec0cfeb526a",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "d787a7ce940f754605bb211b7da792f3237ba20c",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "6843849016e4da260e322216526dfabc1505038e",
                "work_paths": [
                  "derivations/P2-SRC-B0_source-side-scope.md"
                ]
              }
            ],
            "first_review_commit": "d787a7ce940f754605bb211b7da792f3237ba20c",
            "first_work_commit": "6843849016e4da260e322216526dfabc1505038e",
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
              "specs/2026-08-18T1110Z_integrate-src-b0.md"
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
              "merge": "6843849016e4da260e322216526dfabc1505038e",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "0a7a988cb1c1ca7de4cbfebd46fd690245789a2d",
              "recomputed_parent_1": "d787a7ce940f754605bb211b7da792f3237ba20c",
              "recomputed_parent_2": "cb07f3a9d4a6e2f1461098f4606b8b1b12f7ea56",
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
              "commit": "58cfe7e7d64f86055f09ca5cd8659ec0cfeb526a",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "d787a7ce940f754605bb211b7da792f3237ba20c",
              "matches": [],
              "status": "PASS"
            },
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
            },
            {
              "commit": "cb07f3a9d4a6e2f1461098f4606b8b1b12f7ea56",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "6843849016e4da260e322216526dfabc1505038e",
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
              "specs/2026-08-18T1110Z_integrate-src-b0.md"
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
            "first_commit": "58cfe7e7d64f86055f09ca5cd8659ec0cfeb526a",
            "first_commit_paths": [
              "specs/2026-08-18T1110Z_integrate-src-b0.md"
            ],
            "reports_added": [
              "reports/2026-08-18T0507Z_src-b0-source-side-scope.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-18T1110Z_integrate-src-b0.md",
              "reviews/chatgpt/2026-08-18T0507Z_src-b0-source-side-scope.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-18T1110Z_integrate-src-b0.md",
              "specs/2026-08-18T0507Z_src-b0-source-side-scope.md"
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
              "path": "reports/2026-08-18T0507Z_src-b0-source-side-scope.md",
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

## 12. `A15` and `A16` — validators and hygiene

    python3 -m pytest -q         332 passed, 2 deselected in 45.17s
    exit status                  0

**332 passed, 2 deselected, exactly as expected. The arriving task adds no
code**, so the count is unchanged from the evidence base.

**`A16` — commit-message hygiene, all four commits. Rule 20 binds this task and
was not needed: no message required repair and no history was rewritten.**

    commit 1  58cfe7e7d64f86055f09ca5cd8659ec0cfeb526a
              spec: integrate and land the source-side scope assessment
    commit 2  d787a7ce940f754605bb211b7da792f3237ba20c
              review: pre-execution review for the source-side scope integration
    commit 3  6843849016e4da260e322216526dfabc1505038e
              merge: integrate the source-side scope assessment
    commit 4  INTENDED message:
              report: the source side is absent, and the ambiguity survives the variation

**All three stored SHAs above were produced by `git rev-parse` at reporting
time**, per §0.

**Forbidden-token scan over every message in `0a7a988c..commit 3`:**

    Co-Authored-By          0        Generated with        0
    Co-authored-by          0        Claude-Session        0
    claude.ai/code          0        any model identifier  0
    🤖                      0        noreply@anthropic.com 0

**All zero. `A16` for commit 4 is post-report evidence and is not written here.**

## 13. `§7` — Rule 16 assessment: what the assembled set does NOT establish

### 13.1 First — `NOT PRESENT` is a finding about this repository and nothing else

**IT DOES NOT BEAR ON WHETHER THE PHYSICS WORKS.** The PI's intuition — that an
inhomogeneous condensate lump should source a gravitational field governed by
this programme's own induced `G` — is untouched by this landing. **Nothing here
is evidence for or against it.**

**AND IT DOES NOT CHARACTERISE PAPER 1'S PROFILE.** Whether that profile is
derived from field equations or fitted to rotation curves is undetermined, and
was deliberately not pursued. **The `SRC-B0` execution recorded why the question
cannot be settled from here, and it is sharper than a general caution about
inferring from filenames:** this repository's own two descriptions of the cited
work disagree — `paper:206-208` says "we **derived** … and **tested** it", while
the bibliography title at `:1815-1816` reads "**Fits** to 175 SPARC Galaxies".
**The available evidence is internally ambivalent.** `NOT PRESENT` and `FITTED`
are different findings and the second was not reached.

### 13.2 Second — the landing's real content

**THE MEASURE AMBIGUITY THAT `DET-01` SHOWED HARMLESS FOR `β_V` REACHES A
`Γ`-DEFINED `T_μν`.** §7 re-derived it: `∂/∂g^{μν}[½ log det g] = −½ g_{μν}`,
non-zero, and non-zero for any non-constant ultralocal `F`.

**THIS GIVES ONE UNCONDITIONAL PREREQUISITE — a configuration — AND ONE
CONDITIONAL PREREQUISITE that attaches only if the source observable is defined
through `Γ`.** **A classical-action-defined stress tensor does not inherit it**,
and the repository contains such a definition at `paper:673-676`. **Which
definition the programme requires is unresolved.**

**THE CONDITIONAL PREREQUISITE WAS DISCOVERED BY ASKING A QUESTION THE PREVIOUS
TASK'S RIDER DID NOT COVER.** `DET-01` asked whether the ambiguity reaches a
COEFFICIENT in a derivative expansion, and proved it does not. `SRC-B0` asked
whether it survives a VARIATION, which is a different operation on the same
object. **The rider was not wrong; it was answering a different question, and
its domain was narrower than its phrasing suggested.**

**REPORTING IT AS UNCONDITIONAL WOULD OVERSTATE WHAT WAS ESTABLISHED.** An
earlier draft of the specification did exactly that, writing two unconditional
prerequisites. **The difference matters because it changes which future work is
blocked: under the unconditional reading, every source-side route waits on the
measure; under the correct one, only the `Γ` route does.**

**AND THE SUBTRACTION RULE EXISTS.** It is scoped to response observables,
explicitly scoped away from cosmological source energy, and of unsettled
commutation with metric variation — **not absent.** §9.1 verifies all five
points with lines. **"Exists but is not authorized for this use" and "does not
exist" are different programme states**, and only the first tells a future task
that an explicit refusal stands in the way.

### 13.3 Third — the vacuum, stated exactly

**A HOMOGENEOUS LORENTZ-INVARIANT VACUUM GRAVITATES; IT DOES NOT CLUSTER.** It
contributes a cosmological-constant-type stress tensor, and a positive `Λ`
produces de Sitter-type relative acceleration. **It does not provide the
localized clustering source the proposed halo and rotation-curve test needs.**

**THOSE ARE TWO STATEMENTS AND NEITHER IMPLIES THE OTHER.** "No localized
source" must not be read as "no gravitational effect", which would be false.

**THE PROPOSED TEST PROBES THE CONDENSATE'S INHOMOGENEOUS SECTOR ONLY**, and **a
null result there would say nothing about the vacuum sector, which `DET-01` left
unfixed.**

**§7.1 turns that last clause from a caveat into a measurement.** The ambiguity's
contribution to a `Γ`-defined `T_μν` is `∝ g_{μν}`, ultralocal, and
configuration-independent — **a vacuum term exactly, and exactly the sector a
null inhomogeneous result would leave untouched.**

### 13.4 Fourth — no failure criterion has been fixed

**UNTIL THE COMPARED QUANTITY, THE TOLERANCE AND THE DIRECTION ARE
PRE-REGISTERED, THE PROPOSED CALCULATION IS NOT A TEST.** It is a measurement
followed by a judgement, and the judgement would be made by someone who has
already seen the measurement.

**A FACTOR-OF-THREE DISAGREEMENT WOULD BE ADJUDICATED AFTER THE NUMBER IS
SEEN.** It reads as "same order of magnitude — success for a parameter-free
calculation" or as "wrong by three", **both defensible, and which one wins is
decided by whoever is holding the number** unless the criterion is fixed first.

**This task chose no tolerance, no quantity and no direction**, and neither did
the source. §3 forbids it and it is a PI ruling.

### 13.5 Fifth — reported identifiers, and what checks them

**§0 records that two consecutive execution reports gave unresolvable commit
ids. §2.1 measures that claim and reports what I found: the two ids do not
resolve, and they also do not appear in either committed report or anywhere in
either tree.** Every git-object identifier in both reports resolves. **I could
not reproduce the attribution, and I do not speculate about its origin.**

**WHAT IS TRUE REGARDLESS, AND IS THE POINT WORTH LANDING:** **nothing in this
repository checks a reported SHA against the ref it names.** The governance
checker verifies scope arithmetic, commit order, append-only, gate integrity,
parentage, hygiene, and report structure. **It does not read a report's prose
and resolve the identifiers in it.** A report could name any id at all and every
mechanical property would still pass.

**SO THE EVIDENCE CHAIN DEPENDS ON REPORTED IDENTIFIERS BEING RE-RESOLVED RATHER
THAN TRANSCRIBED**, and that discipline currently lives entirely in the
executor's practice and the Researcher's reading. **Both prior tasks' work was
sound — commit messages, structure, scope and content all matched — so whatever
the discrepancy was, it did not reach the repository.** That is the good case,
and it is not a mechanism.

## 14. The temptation, answered directly

**Did landing a `NOT PRESENT` verdict make me want to characterise the external
profile?** **Yes, and more sharply than in the source task, because integration
put the manuscript's own words in front of me twice.** `paper:1815-1816` says
"**Fits** to 175 SPARC Galaxies" — one word in a bibliography title, and writing
"the external profile appears to be fitted" would have felt like reporting rather
than inferring. **It would have converted a title into a provenance ruling about
work this repository does not contain.** I did not, and §13.1 records the
measurement that makes the restraint substantive rather than procedural: the
repository's own two descriptions disagree, so the title is not even locally
consistent evidence.

**Did I want to choose a tolerance?** **Less than I expected, and the reason is
instructive.** With no configuration and no potential, there is nothing to set a
tolerance on — **the absence of the unconditional prerequisite removes the
temptation to pre-empt the PI's ruling.** Had a profile been present, §13.4
would have been much harder to leave empty.

**Did I want to define a subtraction?** **Yes, and this was the real one.** §7.1
gives the ambiguity's contribution as configuration-independent, so a contrast
at fixed metric cancels it exactly — **the algebra is one line and it is
correct.** Writing "therefore a background-subtracted source observable is
unaffected" would have read as a derivation. **It would have been a programme-level
definition smuggled in as an algebraic remark, against an explicit frozen
refusal at `ONTOLOGY:290-292` and with the commutation question at
`ROUTE-01:247-248` still open.** I reported the algebra and the governance
separately, and did not join them into a prescription.

**Did I want to compute a `T_μν`?** **No — and I note that as the one place the
prohibitions cost nothing**, because the object to compute it for does not
exist.

## 15. Stops and clarifications

**NO STOP WAS DECLARED. All acceptance criteria completed.** One primary
category per finding; secondary findings separate.

### 15.1 Stops

**NONE.**

### 15.2 Findings, one primary category each

**`SPECIFICATION_DEFECT` — §0's attribution of two unresolvable SHAs to two
execution reports does not reproduce.** The ids do not resolve, which is what
§10's pre-issue record measured; but neither appears in either committed report
or anywhere in either tree, and every git-object identifier in both reports
resolves. §2.1. **Reported as required; neither report was repaired, and neither
needed repair.**

**`REPOSITORY_DEFECT` — nothing in this repository checks a reported SHA against
the ref it names.** The checker's nine properties do not read report prose.
§13.5. **Unregistered.**

**`REPOSITORY_DEFECT` — the `C3` multi-specification residual remains
unregistered.** Two specifications in range with stated totals `4` and `7` raised
no `DECLARATION_CONFLICT`, because `_declarations_from_specs` compares
`append_only_paths` and `authorised_modified_gates` and not stated totals.
**Fifth independent range in this session; second with two genuinely differing
declarations.** §11.1.

**`REPOSITORY_DEFECT` — the landed `DET-01` artifact states its rider without a
dimensional qualifier** at `:24` and `:302`, carrying "in four dimensions" only
inside the algebra at `:64`. **The relation `det[√g g⁻¹] = det g` holds at
`d = 4` alone and is EMPTY at `d = 2`.** Carried forward from `SRC-B0`; not
repaired, since this task modifies nothing. §7.2.

**`ENVIRONMENT` — `scipy` is declared at `pyproject.toml:12` and is not
installed.** Seventh consecutive task. Not needed here. §1.

**`ENVIRONMENT` — `docs/local/execution_environment.md` declares a Windows
environment that has never been the one used.** Undeclared, unregistered. §1.

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — the `r_c` literal
count is 53 files at the base and 2 as a token.** A substring search for `r_c`
matches inside ordinary words and identifiers. **Reporting 53 without the token
measurement would have suggested the quantity is discussed throughout the
repository when it appears in two files, both of them the manuscript.** §8.2.

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — the eight literal
counts differ between the evidence base and commit 3, and the whole difference
is this task's and `SRC-B0`'s own documents.** `soliton` and `rotation curve` go
from `0` to `4` that way. **Reporting only the commit-3 column would have made
documents about the search look like material found by it.** §8.1.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the self-referential search
hazard, now visible in an integration range.** Every term `A7` asks about gains
hits when this task's own specification and review land, one and two commits
before the search runs. **No governance mechanism addresses a measurement whose
subject includes the instruction to measure.**

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — provenance cannot be settled
from this repository's own descriptions**, which call the same external work
both "derived" and "Fits". §13.1.

### 15.3 Clarifications, not defects

**Rule 13's two diagnostic orders were not exercised**, because no environment
failure occurred; I name neither as the one used, per §8 of the specification.

**`refs/heads/main` is a stale local ref at `1cb5550f`**, reported for contrast
as `A1` requires. The landing pushes `HEAD:refs/heads/main` to `origin`; the
local ref is not the target and is not moved. §2.

**The `--all` commit count rose from 519 (measured in the previous task) to
523.** The four new commits are this task's own. Not a defect; recorded so the
figure is not read as instability. §1.

**The stop-hook's recurring "405 unpushed commits" claim on the session branch is
an artefact of the clone having been unshallowed.** The session branch has
nothing unpublished and is not pushed by this task. §1.
