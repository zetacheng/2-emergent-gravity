# Report — integrate the configuration provenance verdict, and land it

    TASK        integrate-src-01a
    BRANCH      science/integrate-src-01a
    BASE        de547d9d6e152f6be0ef2215cb30c9c3fe3bd248
    SOURCE      science/src-01a-configuration-provenance
    SPEC SHA    32f40d6bd7da4b31cdd348e92e0d1b92ff2530a15ae891517c7ea7f3d81c89b0
    REVIEW      APPROVE FOR EXECUTION, bound to that SHA
    VERDICT     FORM DERIVED / SCALE FITTED

**EVERY FIGURE IS MEASURED AT COMMIT 3 UNLESS THE LINE SAYS `INTENDED`.** This
report is commit 4. **Nothing here claims to measure commit 4**; the commit-4
evidence goes to the Reviewer in chat.

**EVERY SHA BELOW IS PASTED FROM COMMAND OUTPUT, WITH THE COMMAND SHOWN.**

## 0. The landing statement, uncompressed in both directions

> **`FORM DERIVED / SCALE FITTED`.** The manuscript derives the FUNCTIONAL FORM —
> a Yukawa Green's function of range `r_c = 1/m_θ`, from the static field
> equation of a massive scalar. **It does not derive the SCALE.** The chain runs
>
>     SPARC observation → r_c ~ 10 kpc → m_θ ~ 10⁻²⁷ eV → ε
>
> **observation inward, not theory outward.** **`r_c ~ 10 kpc` is not a
> first-principles prediction of this framework.** **`r_c = 1/m_θ` is a DERIVED
> RELATION; it is not a derived numerical value of `r_c`.**
>
> **And the Green's function is not a halo profile.** Getting from one to the
> other needs a source distribution and a coupling, and neither is established.

**`SRC-B0`'s two-way taxonomy could not express this. The four-way taxonomy was
a repair, and the repaired option is the one that obtained.**

## 1. `A3` — environment, run FIRST

**Rule 13's diagnostic order applies and was NOT exercised: no environment
failure occurred.** Rule 13 carries two such orders — a known open item — and I
name neither as the one used.

**Amendment D step 0, before anything else:**

    execution location    vm — Linux 6.18.5-fc-v20
    git common dir        /home/user/2-emergent-gravity/.git
    resolved HEAD at step 0       bfef924c368658cac85c04ed18d96eb4450afba6
    HEAD symbolic ref at step 0   refs/heads/claude/paper-2-independent-verification-dysdp0
    task worktree         /tmp/.../scratchpad/isrc01a, branch science/integrate-src-01a

**Clone depth, command output pasted:**

    $ git rev-parse --is-shallow-repository
    false
    $ git rev-list --count HEAD
    423
    $ git rev-list --count --all
    531

**NOT SHALLOW.** It was shallow earlier in this session and was deepened with
`git fetch --unshallow`; that is the origin of the recurring stop-hook claim of
405 unpushed commits on the session branch, which is `main`'s own published
history made countable. **The `--all` count has moved 519 → 523 → 527 → 531
across the last four tasks; each increment is that task's own commits.**

**Toolchain, MEASURED:**

    python   3.11.15 (main, Mar  3 2026, 09:26:23) [GCC 13.3.0]
    pytest   9.1.1
    numpy    2.4.6
    sympy    1.14.0
    ruff     0.15.8
    scipy    ABSENT — ModuleNotFoundError: No module named 'scipy'

**`pyproject.toml:12` declares `"scipy>=1.11"` and it is not installed.** Ninth
consecutive task. Nothing here needed it.

**`docs/local/execution_environment.md` declares a Windows environment**
(`zeta-3070\codexsandboxoffline`, Python 3.12, `C:\p2-validator\venv`). Every run
has been on Linux. Undeclared, unregistered.

## 2. `A1` — repository and refs

    $ git remote get-url origin
    https://github.com/zetacheng/2-emergent-gravity

**It identifies `zetacheng/2-emergent-gravity`.**

    $ git rev-parse refs/remotes/origin/main
    de547d9d6e152f6be0ef2215cb30c9c3fe3bd248

**A1 expects `de547d9d6e152f6be0ef2215cb30c9c3fe3bd248`. MATCH.**

    $ git rev-parse refs/heads/main
    1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**A stale local ref, reported for contrast; the landing pushes
`HEAD:refs/heads/main` to `origin` and does not move it.**

**THE SOURCE TIP, PASTED FROM THREE INDEPENDENT COMMANDS:**

    $ git rev-parse refs/heads/science/src-01a-configuration-provenance
    6193df29eddd911c8e5829b3745fc342b5dc8065
    $ git rev-parse refs/remotes/origin/science/src-01a-configuration-provenance
    6193df29eddd911c8e5829b3745fc342b5dc8065
    $ git ls-remote origin refs/heads/science/src-01a-configuration-provenance
    6193df29eddd911c8e5829b3745fc342b5dc8065	refs/heads/science/src-01a-configuration-provenance

**A1 expects `6193df29eddd911c8e5829b3745fc342b5dc8065`. MATCH.**

    $ git merge-base --is-ancestor <source> refs/remotes/origin/main
    exit 1        NOT an ancestor of main, as required

**ON THE PASTE REQUIREMENT.** I follow it because a pasted identifier can be
checked against the ref it names and a statement that I checked cannot. **That
reasoning stands on its own** and does not rest on the retracted attribution
about earlier reports — which the previous integration and the Researcher both
found unsupported, the tokens appearing zero times in the reports concerned.

## 3. `A2` — the review, committed unedited

**FIELD PRESENCE CHECKED FIRST, THEN THE VALUE**, because a review with no
`reviewed specification SHA-256:` field would otherwise pass a naive comparison
against an empty string.

    field present?   YES — review line 4 carries "Reviewed specification SHA-256:"
    value            32f40d6bd7da4b31cdd348e92e0d1b92ff2530a15ae891517c7ea7f3d81c89b0
    uploaded spec    32f40d6bd7da4b31cdd348e92e0d1b92ff2530a15ae891517c7ea7f3d81c89b0
    IDENTICAL
    committed specs/2026-08-18T1238Z_integrate-src-01a.md   32f40d6b…   IDENTICAL
    verdict, review line 6   APPROVE FOR EXECUTION

## 4. `A12` — which merge case, stated BEFORE the blob comparisons

    $ git merge-base HEAD <source>
    de547d9d6e152f6be0ef2215cb30c9c3fe3bd248

    evidence base                            de547d9d6e152f6be0ef2215cb30c9c3fe3bd248
    IDENTICAL
    commits on origin/main after the base    0

**THE MERGE-BASE IS THE EVIDENCE BASE, SO NO COMMIT ON `main` COULD HAVE TOUCHED
AN ARRIVING PATH.** `main` has not moved since the source branched.

**Then the four blob comparisons — arriving blob at the source tip against the
same path at the merge head:**

    derivations/P2-SRC-01a_configuration-provenance.md         05d450615986 → 05d450615986  IDENTICAL
    reports/2026-08-18T1205Z_src-01a-configuration-...md       7b2a2323aaf9 → 7b2a2323aaf9  IDENTICAL
    reviews/chatgpt/2026-08-18T1205Z_src-01a-...md             77c1ae59b76c → 77c1ae59b76c  IDENTICAL
    specs/2026-08-18T1205Z_src-01a-configuration-...md         59928afe4222 → 59928afe4222  IDENTICAL

**Everything arriving by merge is integrated exactly as reviewed.**

## 5. `A5` — no conflict

    $ git merge-tree --write-tree HEAD <source>
    exit 0, tree 7790feb55299e55a4f14b98f9ac0e57ef93ee453
    conflict list                            EMPTY
    $ git merge --no-ff
    exit 0, 'ort' strategy
    unmerged paths after the merge           0
    $ git ls-files -u
    0 lines

**The conflict list is empty, as required. Any conflict would have been an
immediate stop.**

## 6. `A4` — merge parentage, three separately derived

    $ git rev-parse HEAD^1
    35851d274c0f1ff8518307a16e74be34e2b9aedc
    $ git rev-parse HEAD^2
    6193df29eddd911c8e5829b3745fc342b5dc8065
    $ git merge-base <parent 1> <parent 2>
    de547d9d6e152f6be0ef2215cb30c9c3fe3bd248

    $ git merge-base --is-ancestor <commit 1> <parent 1>
    exit 0

**Parent 1 is this task's review commit, parent 2 is the source tip as
re-resolved, and their merge-base is the evidence base.** Each came from its own
command.

## 7. `A6` — the four-step chain, re-read at the head

**The manuscript blob at the merge head is
`c8246f890b07f53ab8094981cbd5a02972fda4c1`, unchanged from the base — §12.2.
Every line below was read there, not taken from the specification.**

    :80   This mode is identified with the ultralight scalar responsible for
    :81   the dark-matter phenomenology of Ref.~\cite{Cheng:2025sparc}.

    :613  The static field equation of $\tilde\theta$ is that of a massive
    :614  scalar, with Yukawa Green's function of range
    :615  $r_c = 1/m_\theta$.

    :616  We identify $\tilde\theta$ with the ultralight scalar $\chi$ whose
    :617  galactic-scale phenomenology was tested in
    :618  Ref.~\cite{Cheng:2025sparc}; the SPARC-scale cutoff radii
    :619  $r_c \sim 10\,\mathrm{kpc}$ correspond to
    :620  $m_\theta \sim 10^{-27}\,\mathrm{eV}$, i.e.\

    :641  Establishing this coupling chain quantitatively is deferred to
    :642  future work; in Ref.~\cite{Cheng:2025sparc} the coupling is
    :643  treated as an effective parameter, so the phenomenological results

### 7.1 The four steps classified

    1  θ̃ exists — the angular pseudo-Goldstone mode of the
       complex condensate, its mass protected by an approximate U(1)
                                                          DERIVED HERE
       The only step of the four that this manuscript performs from
       its own microscopic structure.

    2  θ̃ ≡ χ                                             IDENTIFIED HERE
       :80-81 and :616-618. Made because χ already accounts for the
       phenomenology; not derived from anything internal.

    3  Yukawa form, r_c = 1/m_θ                            DERIVED HERE,
       :613-615 — but as the field equation of the identified massive
       scalar. The derivation is one line from the mass term and it
       runs downstream of step 2.

    4  m_θ ~ 10⁻²⁷ eV                                     INFERRED FROM
       :619-620 — from the SPARC-scale r_c.                OBSERVATION

    and the coupling that would connect the mode to matter  DEFERRED
       :641-643.

**"RESPONSIBLE FOR" AND "CORRESPOND TO" ARE IDENTIFICATION LANGUAGE, NOT
DERIVATION LANGUAGE.** Neither sentence asserts that anything follows from
anything; each asserts that two objects are the same one, or that two numbers go
together.

### 7.2 The direction of the scale chain

    SPARC observation  →  r_c ~ 10 kpc  →  m_θ ~ 10⁻²⁷ eV  →  ε

**CONFIRMED: NO STEP RUNS THEORY-OUTWARD.** `:619-620` takes the SPARC-scale
radii as given and reads the mass off them. `:621` then infers `ε ~ m_θ²/Λ²` from
that mass. **The arriving artifact measured the remaining possibility and closed
it**: `:541-544` records the magnitude of `ε` as "the dedicated computation left
open", and `:1681-1683` lists connecting `ε` to the SPARC-scale phenomenology as
future work. **The theory-outward direction is named in the manuscript as work
not done.**

## 8. `A7` — the two compressions, both guarded

### 8.1 The relation-versus-value distinction, in my own words

**`r_c = 1/m_θ` IS A DERIVED RELATION.** It follows from `:613-615`: a massive
scalar's static field equation has a Yukawa Green's function whose range is the
inverse mass. **That is a statement about the SHAPE of a dependence between two
quantities, and it is derived.**

**`r_c` IS NOT A DERIVED VALUE.** The relation fixes neither side. It converts a
mass into a length and a length into a mass, and it is silent about which one is
known. **The value enters at `:619` from observation, and the relation then
carries it to the other side.**

**A relation that converts two unknowns into one unknown has reduced the count of
free parameters by one. It has not predicted either.**

### 8.2 The two searches

**Search 1 — any sentence calling the halo derived.** Patterns: `halo is
derived`, `derived halo`, `halo profile is derived`, `derives the halo`, `halo …
derived from first principles`, and `the halo is a prediction`.

    hits in the ARTIFACT           0
    hits in ALL COMMIT MESSAGES    0
    hits in THIS REPORT            the pattern list above, and nothing else

**Search 2 — any sentence calling `r_c ~ 10 kpc` a prediction.** Patterns:
`predicts r_c`, `r_c is predicted`, `predicted r_c`, `prediction of r_c`,
`10 kpc is a prediction`, `predicts 10 kpc`, `first-principles prediction`.

    hits in the ARTIFACT           0
    hits in ALL COMMIT MESSAGES    0
    hits in THIS REPORT            the pattern list above, and §0's DENIAL

**THE RESULTS ARE REPORTED POSITIONALLY, NOT AS COUNTS, AND THAT IS
DELIBERATE.** A report that must confirm it never called the halo derived has to
write the phrase in order to deny it, and it has to write the patterns in order
to say what it searched for. **A count would therefore be non-zero for a reason
that has nothing to do with the prohibition, and it would change with any later
edit to this file** — which is exactly how `DET-01`'s `A10` came to state a
figure its own committed bytes contradicted.

**SO THE STATEMENT IS POSITIONAL AND STABLE UNDER EDITING:** every occurrence of
either phrasing in this report is inside §8.2's own pattern lists or inside §0's
required denial, *"`r_c ~ 10 kpc` is not a first-principles prediction of this
framework"*. **There is no third place.** **The artifact and every commit message
are clean of both, and those are the two subjects the prohibition protects.**

## 9. `A8` — compatibility with `SRC-B0`

**`SRC-B0`: "the source side is absent." `SRC-01a`: "the form is derived." THESE
DO NOT CONFLICT, AND THE REASON IS ONE PASSAGE.**

    :641  Establishing this coupling chain quantitatively is deferred to
    :642  future work; in Ref.~\cite{Cheng:2025sparc} the coupling is
    :643  treated as an effective parameter, so the phenomenological results

**A GREEN'S FUNCTION WITHOUT A SOURCE DISTRIBUTION AND A COUPLING IS NOT A
HALO.** `:613-615` establishes how the MEDIATING FIELD falls off. To get a halo
one needs, in addition:

    what the field is sourced BY        no source distribution anywhere in the
                                        manuscript
    how strongly it couples             :641-643 — deferred, and carried in the
                                        cited work as a free effective parameter
    the amplitude / normalisation       not addressed at all

**So the two verdicts describe different objects at different depths.** `SRC-B0`
asked whether a computable configuration is present and found none. `SRC-01a`
asked where the manuscript's account of that configuration comes from and found a
derived form with an observational scale. **Both are true simultaneously, and a
reader meeting them on `main` should not take them for a conflict.**

**`SRC-B0`'S VERDICT STANDS UNCHANGED. This task supplies no configuration.**

## 10. `A9` — the identification as the upstream finding

**THE `SRC-01a` SPECIFICATION ASKED ABOUT PARAMETER PROVENANCE. THE
LOAD-BEARING STEP IS EARLIER.**

**The manuscript's own wording, at both places it makes the identification:**

    :80-81    "This mode is identified with the ultralight scalar RESPONSIBLE FOR
               the dark-matter phenomenology of Ref.~\cite{Cheng:2025sparc}."
    :616-618  "We IDENTIFY $\tilde\theta$ with the ultralight scalar $\chi$ WHOSE
               galactic-scale phenomenology WAS TESTED IN Ref.~\cite{Cheng:2025sparc}"

**THE IDENTIFICATION IS FIXED BY THE PHENOMENOLOGY, AS `m_θ` IS.** The mode is
identified with `χ` because `χ` already accounts for the observations; the mass is
inferred from an observed radius. **Neither is fixed by anything internal to the
framework**, and `:641-643` records that the coupling which might have grounded
the identification dynamically is deferred to future work. **So the
identification rests on no internal dynamical reason.**

**AND THEY ARE NOT FIXED IN THE SAME EPISTEMIC WAY. THE DISTINCTION IS KEPT
BECAUSE IT IS REAL:**

    THE IDENTIFICATION   a QUALITATIVE phenomenological identification. Two
                         objects are asserted to be one. It admits no numerical
                         residual and cannot be checked by measuring a
                         discrepancy; it is either right or it is not.

    m_θ                  a QUANTITATIVE inference from an observed r_c. A
                         number is read off another number through a derived
                         relation. It has a value, an uncertainty in principle,
                         and could in principle be contradicted by a
                         first-principles calculation of ε.

**"FIXED BY THE PHENOMENOLOGY" COVERS BOTH. "FIXED IN THE SAME WAY" DOES NOT.**

**A NOTE ON THE SPECIFICATION'S OWN WORDING, REPORTED AND NOT ADJUDICATED.**
`§1` states the distinction and says explicitly: *"'Fixed by the phenomenology'
covers both; 'fixed in the same way' does not."* **`A9` and `§7`'s second
junction both ask me to report that the identification is fixed by the
phenomenology "in the same way `m_θ` is".** Those are inconsistent as written.
**`§9`'s report contract requires "the qualitative-versus-quantitative
distinction kept", and the review's `§5` records that the revised wording
"correctly avoids saying that those two are 'fixed in the same way'".** **I have
not decided which prevails**, per `§8`: I report the shared claim that both are
fixed by the phenomenology, and I keep the distinction that `§1`, `§9` and the
review all require. **Every instruction's substance is satisfied; the conflict is
in phrasing and is recorded in §16.2.**

**WHY THIS IS THE VERDICT'S UPSTREAM HALF.** A landing that reported only "scale
fitted" would leave the impression that the identification is secure and only a
number is borrowed. **It is not secure — it is the step on which every downstream
statement depends, and it is asserted.** Withdraw it and the manuscript still has
a pseudo-Goldstone mode of undetermined mass, with nothing connecting it to a
galaxy.

## 11. `A10` — the circularity implication, scoped to one layer

**STATED AS AN IMPLICATION OF THE VERDICT. THIS REPORT DOES NOT SAY WHETHER THE
SOURCE-SIDE TEST SHOULD BE DONE.**

    USING χ's FIELD EQUATION
      CIRCULAR FOR TESTING THE YUKAWA FORM. The form is already built into the
      input: χ is the phenomenological scalar whose Yukawa behaviour is what a
      test would be checking. A computation that returned it would carry no
      information about whether the microscopic theory predicts that form.

    USING θ̃'s INDEPENDENTLY DERIVED MICROSCOPIC FIELD EQUATION
      AVOIDS THAT SPECIFIC CIRCULARITY — under a stated condition: that the
      derivation does not take the phenomenological θ̃ ≡ χ identification as an
      input. And it requires R1, R5 and D-pre, none of which is closed.

**THAT IS NOT THE SAME AS THE TEST BEING NON-CIRCULAR.**

**THREE PROVENANCES WERE NOT EXAMINED, AND I CONFIRM I DID NOT EXAMINE THEM:**

    the source and configuration mapping   NOT EXAMINED
    the coupling                           NOT EXAMINED
    the normalisation                      NOT EXAMINED

**`SRC-01a` established circularity for ONE LAYER — the Yukawa form — and looked
at no other.** **If any of the three is also fixed by the same phenomenology,
circularity re-enters by another door.** **Whether the eventual source-side test
is non-circular AS A WHOLE remains unresolved.**

**THE SEARCH `A10` REQUIRES.** Patterns for an unqualified non-circularity
claim: `is non-circular`, `non-circular route`, `route is non-circular`,
`microscopic route is non-circular`, `avoids circularity` without a following
scope word, and `not circular`.

    unqualified assertions in the ARTIFACT            0
    unqualified assertions in ALL COMMIT MESSAGES     0
    unqualified assertions in THIS REPORT             0 — every occurrence is
                                                      either the pattern list in
                                                      this section, or a scoped
                                                      statement, or a denial

**POSITIONALLY, for the same reason as §8.2.** The occurrences in this report are:
this paragraph's pattern list; the scoped forms *"avoids THAT SPECIFIC
circularity"* and *"circular FOR TESTING THE YUKAWA FORM"*; and the denial
*"whether the eventual source-side test is non-circular AS A WHOLE remains
unresolved"*. **No sentence in the landed set asserts that the microscopic route
is non-circular without qualification.**

**AND I DID NOT SAY WHETHER THE TEST SHOULD BE DONE.** Neither this report nor
the arriving artifact contains a recommendation. The classification is reported;
the programme decision is not made.

## 12. `A11` – `A15` — scope and integrity

### 12.1 `A11` — scope

    stated: 7 additions, 0 modifications          INTENDED, final at commit 4
    append_only:  DECISION_LOG.md                 a CHECKER-CONFIGURATION declaration,
                                                  NOT an authorisation to write it
    authorised_gates: []
    base: de547d9d6e152f6be0ef2215cb30c9c3fe3bd248
    head: commit 4
    mode: exact
    modify: []
    forbidden_operations: delete, rename, copy, type_change, unmerged, unknown

**CUMULATIVE per commit — MEASURED:**

    base .. commit 1  ed6691bb     1 addition,  0 modifications
    base .. commit 2  35851d27     2 additions, 0 modifications
    base .. commit 3  df8abcf7     6 additions, 0 modifications
    base .. commit 4               7 additions, 0 modifications   INTENDED

**SOURCE'S OWN CONTRIBUTION — MEASURED, separately labelled:**

    base .. 6193df29   4 additions, 0 modifications

      derivations/P2-SRC-01a_configuration-provenance.md
      reports/2026-08-18T1205Z_src-01a-configuration-provenance.md
      reviews/chatgpt/2026-08-18T1205Z_src-01a-configuration-provenance.md
      specs/2026-08-18T1205Z_src-01a-configuration-provenance.md

**`6` IS CUMULATIVE, NOT THE MERGE'S CONTRIBUTION.** The merge contributes four;
the range contains six at commit 3 because commits 1 and 2 added two more.
**They are not addends.**

**ARRIVING PATH COUNT `4`; ARRIVING ADDITION COUNT `4`. THEY COINCIDE, at
four**, because every arriving path is an addition and none arrives twice. They
are reported separately because they would diverge if the source had modified a
path as well as adding one.

**Seven paths in the final manifest: four arrive by merge, three authored here.**

**The UTC time was measured, not assumed: `2026-08-18T12:38:31Z`, giving the
token `1238Z`.** Commit 1 was made in the same minute.

### 12.2 `A13` — nothing existing changed

    PATHS COMPARED (all paths at the evidence base)    498
    paths at the head                                  504
    paths whose blob DIFFERS at the head                 0
    git diff --name-status base..head                    6 entries, ALL status A
    entries of any other status                          0

    paper/emergent_gr_paper_v2_15.tex     c8246f890b07f53a…   UNCHANGED
    GATES.md                              2b3bd5069414f009…   UNCHANGED
    CONVENTIONS.md                        8badc51f38d85d54…   UNCHANGED
    docs/BRANCHING_POLICY.md              3f0f35d4da448eb4…   UNCHANGED
    DECISION_LOG.md                       d9dd2bf3a8cca405…   UNCHANGED
    scripts/recon2026/proca_curved.py     03f46905e5798fb7…   UNCHANGED
    scripts/recon2026/flat_validation.py  6b21f9d6db67641e…   UNCHANGED
    tests/test_recon2026_flat_limit.py    1d7ba5672614dedc…   UNCHANGED

**`paper/emergent_gr_paper_v2_15.tex` IS THE SOURCE OF EVERY QUOTATION IN §7 AND
ITS BLOB IS UNCHANGED.** The `paper/` subtree object is
`8af4fcc6c126e6ba20d7d44770c8c1d1eb12bef0` at both ends — one comparison covering
the manuscript, its README and the figures directory.

**BOTH ARTIFACT COUNTS RE-MEASURED, not carried:**

    derivations/P2-BETAV-*    base 8   head 8
    derivations/P2-SRC-*      base 1   head 2

      P2-SRC-01a_configuration-provenance.md      ← arrives by merge
      P2-SRC-B0_source-side-scope.md

**Seven microspec artifacts; two files under `scripts/recon2026/`; both registers
unchanged.** **`results/` subtree `9015049f68d5ace2790b5c62976e798298442bce` at
both ends.**

### 12.3 `A14` — gate invariants and pins

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

### 12.4 `A15` — superseded branches, before the advance

**Six separate `git merge-base --is-ancestor <c> origin/main` invocations. Exit
`1` means NOT an ancestor, which is required.**

    52f65117  exit 1     ebd531ab  exit 1     40168469  exit 1
    7146a093  exit 1     10c260b9  exit 1     d64cd912  exit 1

    origin/main at measurement time    de547d9d6e152f6be0ef2215cb30c9c3fe3bd248

**And against commit 3, which the landing will make `main`: all six exit `1`.**
The after-the-advance re-run is post-report evidence and is not written here.

## 13. `A16` — the checker over this task's own range

**Base `de547d9d…`, head commit 3. Two runs at both prospectivity readings — four
invocations, all exit `0`.**

**THE OUTPUT WAS PARSED, NOT GREPPED.** Each JSON file was loaded with
`json.loads` and every property read from the parsed structure by key (`id`,
`status`, `classification`, `evidence`). The property list is a JSON *array* of
objects rather than a map keyed by property id, so a key lookup returns `None`,
and a grep for `PASS` would count the word wherever it occurs — including inside
the `does_not_establish` prose every `PARTIAL` property carries.

**`RUN 1` config, verbatim — observational, governs nothing:**

    {
      "base": "de547d9d6e152f6be0ef2215cb30c9c3fe3bd248",
      "head": "df8abcf7b34478218abab5097c9f070f4b7b6650",
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
      "head": "df8abcf7b34478218abab5097c9f070f4b7b6650",
      "specification_paths": [
        "specs/2026-08-18T1238Z_integrate-src-01a.md"
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
The `EXCLUSIVE` output differs from the `INCLUSIVE` one at exactly one line — 314
of 318 for `RUN 1`, 291 of 295 for `RUN 2` — that value only. **No property result
changes between readings.**

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
    NOT_DECLARED / NOT_PARSEABLE    none
    DECLARATION_CONFLICT            NONE — confirmed
    commits_in_range                7
    commits_on_first_parent_line    3
    prospectivity in scope 3, out of scope []

**`P7` REPORTS FOURTEEN SECTIONS** — base 14, head 14, raw 14 and 14. **`PASS` at
zero would have been a stop; it is not zero.**

**`P5` is `PASS` rather than `NOT_APPLICABLE`** — this range contains a merge and
the checker recomputed its parentage independently. **`P9` is `PASS` on the
arriving `SRC-01a` report**, which carries its `Stops and clarifications`
section.

### 13.1 What `RUN 1` did, and the `C3` residual

**`RUN 1`'s default subject selection discovered TWO specifications in range:**

    specs/2026-08-18T1205Z_src-01a-configuration-provenance.md
      stated: 4 additions, 0 modifications    counted 4 (add 4 / mod 0)   parse OK
    specs/2026-08-18T1238Z_integrate-src-01a.md
      stated: 7 additions, 0 modifications    counted 7 (add 7 / mod 0)   parse OK

**`RUN 2` names only this task's and sees one.** That is the entire difference
between the two outputs: `RUN 1`'s JSON carries the extra `SRC-01a` evidence block
and the extra path in two subject lists. **`RUN 1` discovers the subject; `RUN 2`
names it. That is not the same check even when the verdicts agree.**

**THE `C3` MULTI-SPECIFICATION RESIDUAL AROSE AGAIN AND AGAIN RAISED NOTHING.**
Two specifications, **stated totals `4` and `7` — differing — and no
`DECLARATION_CONFLICT`.** `_declarations_from_specs` compares `append_only_paths`
and `authorised_modified_gates`, which agreed (`["DECISION_LOG.md"]` and `[]`);
**it does not compare stated totals.**

**SIXTH INDEPENDENT RANGE IN THIS SESSION, AND THE THIRD IN WHICH TWO GENUINELY
DIFFERING DECLARATIONS WERE BOTH PRESENT.** Still unregistered. **Not a stop:
`P1`'s per-specification arithmetic is correct for each specification alone.**

**Neither the config nor this specification's declarations were adjusted to make
`RUN 2` pass. `RUN 2` passed on its first invocation at both readings.**

### 13.2 The two JSON outputs, verbatim

**`RUN 1`, `INCLUSIVE` reading — 318 lines. The `EXCLUSIVE` output is this file
with line 314 reading `"inclusivity": "EXCLUSIVE"`.**

    {
      "base": "de547d9d6e152f6be0ef2215cb30c9c3fe3bd248",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "df8abcf7b34478218abab5097c9f070f4b7b6650",
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
                "derivations/P2-SRC-01a_configuration-provenance.md",
                "reports/2026-08-18T1205Z_src-01a-configuration-provenance.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-src-01a.md",
                "reviews/chatgpt/2026-08-18T1205Z_src-01a-configuration-provenance.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-src-01a.md",
                "specs/2026-08-18T1205Z_src-01a-configuration-provenance.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-src-01a.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-18T1238Z_integrate-src-01a.md",
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
                "commit": "ed6691bb429e1e66d1519f6aa109ab2ff4504b4f",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "35851d274c0f1ff8518307a16e74be34e2b9aedc",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "df8abcf7b34478218abab5097c9f070f4b7b6650",
                "work_paths": [
                  "derivations/P2-SRC-01a_configuration-provenance.md"
                ]
              }
            ],
            "first_review_commit": "35851d274c0f1ff8518307a16e74be34e2b9aedc",
            "first_work_commit": "df8abcf7b34478218abab5097c9f070f4b7b6650",
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
              "specs/2026-08-18T1205Z_src-01a-configuration-provenance.md",
              "specs/2026-08-18T1238Z_integrate-src-01a.md"
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
              "merge": "df8abcf7b34478218abab5097c9f070f4b7b6650",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "de547d9d6e152f6be0ef2215cb30c9c3fe3bd248",
              "recomputed_parent_1": "35851d274c0f1ff8518307a16e74be34e2b9aedc",
              "recomputed_parent_2": "6193df29eddd911c8e5829b3745fc342b5dc8065",
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
              "commit": "ed6691bb429e1e66d1519f6aa109ab2ff4504b4f",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "35851d274c0f1ff8518307a16e74be34e2b9aedc",
              "matches": [],
              "status": "PASS"
            },
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
            },
            {
              "commit": "6193df29eddd911c8e5829b3745fc342b5dc8065",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "df8abcf7b34478218abab5097c9f070f4b7b6650",
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
              "specs/2026-08-18T1205Z_src-01a-configuration-provenance.md",
              "specs/2026-08-18T1238Z_integrate-src-01a.md"
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
            "first_commit": "ed6691bb429e1e66d1519f6aa109ab2ff4504b4f",
            "first_commit_paths": [
              "specs/2026-08-18T1238Z_integrate-src-01a.md"
            ],
            "reports_added": [
              "reports/2026-08-18T1205Z_src-01a-configuration-provenance.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-18T1238Z_integrate-src-01a.md",
              "reviews/chatgpt/2026-08-18T1205Z_src-01a-configuration-provenance.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-18T1238Z_integrate-src-01a.md",
              "specs/2026-08-18T1205Z_src-01a-configuration-provenance.md"
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
              "path": "reports/2026-08-18T1205Z_src-01a-configuration-provenance.md",
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
      "base": "de547d9d6e152f6be0ef2215cb30c9c3fe3bd248",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "df8abcf7b34478218abab5097c9f070f4b7b6650",
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
                "derivations/P2-SRC-01a_configuration-provenance.md",
                "reports/2026-08-18T1205Z_src-01a-configuration-provenance.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-src-01a.md",
                "reviews/chatgpt/2026-08-18T1205Z_src-01a-configuration-provenance.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-src-01a.md",
                "specs/2026-08-18T1205Z_src-01a-configuration-provenance.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-src-01a.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-18T1238Z_integrate-src-01a.md",
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
                "commit": "ed6691bb429e1e66d1519f6aa109ab2ff4504b4f",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "35851d274c0f1ff8518307a16e74be34e2b9aedc",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "df8abcf7b34478218abab5097c9f070f4b7b6650",
                "work_paths": [
                  "derivations/P2-SRC-01a_configuration-provenance.md"
                ]
              }
            ],
            "first_review_commit": "35851d274c0f1ff8518307a16e74be34e2b9aedc",
            "first_work_commit": "df8abcf7b34478218abab5097c9f070f4b7b6650",
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
              "specs/2026-08-18T1238Z_integrate-src-01a.md"
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
              "merge": "df8abcf7b34478218abab5097c9f070f4b7b6650",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "de547d9d6e152f6be0ef2215cb30c9c3fe3bd248",
              "recomputed_parent_1": "35851d274c0f1ff8518307a16e74be34e2b9aedc",
              "recomputed_parent_2": "6193df29eddd911c8e5829b3745fc342b5dc8065",
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
              "commit": "ed6691bb429e1e66d1519f6aa109ab2ff4504b4f",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "35851d274c0f1ff8518307a16e74be34e2b9aedc",
              "matches": [],
              "status": "PASS"
            },
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
            },
            {
              "commit": "6193df29eddd911c8e5829b3745fc342b5dc8065",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "df8abcf7b34478218abab5097c9f070f4b7b6650",
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
              "specs/2026-08-18T1238Z_integrate-src-01a.md"
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
            "first_commit": "ed6691bb429e1e66d1519f6aa109ab2ff4504b4f",
            "first_commit_paths": [
              "specs/2026-08-18T1238Z_integrate-src-01a.md"
            ],
            "reports_added": [
              "reports/2026-08-18T1205Z_src-01a-configuration-provenance.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-18T1238Z_integrate-src-01a.md",
              "reviews/chatgpt/2026-08-18T1205Z_src-01a-configuration-provenance.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-18T1238Z_integrate-src-01a.md",
              "specs/2026-08-18T1205Z_src-01a-configuration-provenance.md"
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
              "path": "reports/2026-08-18T1205Z_src-01a-configuration-provenance.md",
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

## 14. `A17` and `A18` — validators and hygiene

    $ python3 -m pytest -q
    332 passed, 2 deselected in 67.71s
    exit status 0

**332 passed, 2 deselected, exactly as expected. The arriving task adds no
code.**

**`A18` — hygiene on all four commits. Rule 20 binds this task and was not
needed: no message required repair and no history was rewritten. Every SHA below
pasted from `git rev-parse`:**

    commit 1  ed6691bb429e1e66d1519f6aa109ab2ff4504b4f
              spec: integrate and land the configuration provenance verdict
    commit 2  35851d274c0f1ff8518307a16e74be34e2b9aedc
              review: pre-execution review for the configuration provenance integration
    commit 3  df8abcf7b34478218abab5097c9f070f4b7b6650
              merge: integrate the configuration provenance verdict
    commit 4  INTENDED message:
              report: the form is derived, the scale is observational, and the identification is asserted

    Co-Authored-By          0        Generated with        0
    Co-authored-by          0        Claude-Session        0
    claude.ai/code          0        any model identifier  0
    🤖                      0        noreply@anthropic.com 0

**All zero. `A18` for commit 4 is post-report evidence and is not written here.**

## 15. `§7` — Rule 16 assessment: what the assembled set does NOT establish

### 15.1 First — "form derived" is not "halo derived"

**A DERIVED RELATION IS NOT A DERIVED VALUE.** `r_c = 1/m_θ` is derived at
`:613-615`; `r_c ~ 10 kpc` enters at `:619` from observation. **The relation
reduces two unknowns to one. It predicts neither.**

**AND A GREEN'S FUNCTION IS NOT A HALO.** What `:613-615` establishes is how the
mediating field falls off. A halo additionally needs a source distribution, a
coupling and a normalisation, and the manuscript supplies none of the three —
`:641-643` records the coupling as deferred.

**THE SCALE CHAIN RUNS OBSERVATION-INWARD:** `SPARC → r_c → m_θ → ε`, with the
theory-outward direction named in the manuscript itself as work not done
(`:541-544`, `:1681-1683`).

### 15.2 Second — the identification is the upstream half

**IT IS FIXED BY THE PHENOMENOLOGY, AS THE NUMBER IS**, and **the coupling that
might have grounded it internally is deferred to future work by the manuscript's
own words** at `:641-643`. **They are not fixed in the same epistemic way** —
§10 keeps the qualitative/quantitative distinction, as `§9`'s report contract
requires.

**REPORTING ONLY "SCALE FITTED" WOULD LEAVE THE IDENTIFICATION LOOKING SECURE**,
as though a settled physical object had merely borrowed a number from
observation. **The object itself is the borrowed thing.** Step 1 of §7.1 is the
only one of the four the manuscript derives from its own microscopic structure;
steps 2 through 4 all run through `Ref.~\cite{Cheng:2025sparc}`.

### 15.3 Third — this is a verdict about a claim

**PAPER 1 WAS NOT READ AND IS NOT IN THIS REPOSITORY.** Every statement about
what Paper 1 derived, fitted or tested is Paper 2's claim about it.

**A `FORM DERIVED` FINDING REACHED THIS WAY IS, IN PART, A FINDING ABOUT A
CLAIM.** The distinction is not uniform across the verdict and I state it
precisely: **the Yukawa step at `:613-615` is a derivation I read in a file I
have** — that half is about what was done. **The statements about Paper 1's
profile, its fit to 175 galaxies, and its treatment of the coupling as an
effective parameter are about what is CLAIMED**, and nothing here verifies them.

### 15.4 Fourth — the search vocabulary is not exhaustive

**IT CAME FROM THE RESEARCHER AND FROM A DESCRIPTION, NOT FROM THE MANUSCRIPT'S
OWN INDEX.** The arriving artifact ran two passes — ten seed terms and nine
identification terms — plus one term the executor added (`varepsilon`) after
PASS 2 showed the parameter chain ran through it. **Twenty terms, 161 distinct
lines out of 1833.**

**WHAT THAT COST IS ON RECORD:** `m_theta` returns zero because the file writes
`m_\theta`; `rotation curve` returns zero because the phrase is absent; PASS 1
alone never reaches `:80`, the carrier identification. **A step using vocabulary
outside all three lists would have been missed**, and neither the arriving
artifact nor this integration read the manuscript end to end.

### 15.5 Fifth — this landing removes no blocker

**`SRC-B0`'s absent configuration is still absent. `R1`–`R5` are still open. The
`Γ`-versus-`S` source-definition question is still unresolved.** This task
touches none of them.

**WHAT IT ESTABLISHES IS NARROWER THAN IT MAY READ:**

> **ONE ROUTE is circular FOR TESTING THE YUKAWA FORM — the route that uses `χ`'s
> field equation, because the form is already in the input. THE MICROSCOPIC ROUTE
> CAN AVOID THAT SPECIFIC CIRCULARITY, provided its derivation does not take the
> phenomenological `θ̃ ≡ χ` identification as an input.**
>
> **THIS TASK DOES NOT ESTABLISH THAT THE EVENTUAL SOURCE-SIDE TEST AS A WHOLE IS
> NON-CIRCULAR.**

**THE SOURCE MAPPING, THE COUPLING AND THE NORMALISATION EACH CARRY THEIR OWN
PROVENANCE. NONE WAS EXAMINED.** **Circularity could re-enter through any of
them** — and the one of the three the manuscript does discuss, the coupling, it
describes at `:641-643` as treated in the cited work as a free effective
parameter, which is a provenance in its own right.

## 16. The temptation, answered directly

**Did landing this make me want to call the halo derived?** **Yes, and the pull
came from the shape of the finding rather than from carelessness.** "The form is
derived" is the affirmative half of a two-part verdict, and it is the half that
sounds like a result. **`FORM DERIVED / SCALE FITTED` shortens to "form derived"
in a way that `SCALE FITTED` does not shorten to anything**, so any summary drifts
toward the first clause. §8.2's searches are what I did about it rather than
relying on intending not to.

**Did I want to say the test is worth doing?** **Yes, and §11 is where it was
strongest.** Having established that one route is circular and another may not
be, the natural next sentence names the second as the way forward. **That is a
programme decision, and §4 forbids it.** The three unexamined provenances are the
substantive reason as well as the procedural one: **recommending a route whose
other three layers have never been looked at would be a recommendation about a
fraction of the problem.**

**Did I want to reason from Paper 1?** **Less than in the source task, and for an
uncomfortable reason: by now I have read Paper 2's account of it four times
across two tasks, and the account has begun to feel like knowledge of the
paper.** It is not. **Every statement about Paper 1 in this report carries the
Paper 2 line that makes it**, and §15.3 marks which half of the verdict is about
a claim rather than about a derivation.

**One restraint nothing asked for.** §10 finds the identification asserted rather
than derived, and it would be easy to let that read as a criticism of the
manuscript. **It is not one. An identification is a legitimate modelling step,
and the manuscript makes it openly**, in both places, in identification language.
The finding is about what the identification can bear, not about whether making
it was proper.

## 17. Stops and clarifications

**NO STOP WAS DECLARED. All acceptance criteria completed.** One primary category
per finding; secondary findings separate.

### 17.1 Stops

**NONE.**

### 17.2 Findings, one primary category each

**`SPECIFICATION_DEFECT` — `A9` and `§7`'s second junction ask me to report that
the identification is fixed by the phenomenology "in the same way `m_θ` is",
while `§1` states explicitly that *"'fixed in the same way' does not"* cover
both.** `§9`'s report contract requires the qualitative-versus-quantitative
distinction kept, and the review's `§5` records that the revised wording avoids
"fixed in the same way". **The instructions are inconsistent as written. Per `§8`
I did not decide which prevails**: §10 reports the shared claim and keeps the
distinction, satisfying every instruction's substance. §10.

**`REPOSITORY_DEFECT` — the `C3` multi-specification residual remains
unregistered.** Two specifications in range with stated totals `4` and `7` raised
no `DECLARATION_CONFLICT`. **Sixth independent range this session; third with two
genuinely differing declarations.** §13.1.

**`ENVIRONMENT` — `scipy` is declared at `pyproject.toml:12` and is not
installed.** Ninth consecutive task. Not needed here. §1.

**`ENVIRONMENT` — `docs/local/execution_environment.md` declares a Windows
environment that has never been the one used.** Undeclared, unregistered. §1.

**`OBSERVATION_METHOD_ERROR` (avoided, recorded as method) — `A7` and `A10` ask
for searches whose patterns the searching document necessarily contains.** A
report that must confirm it never called the halo derived has to write the phrase
in order to deny it. **Both searches are reported POSITIONALLY rather than as
counts**, because a count of a document's own denials is invalidated by any later
edit to that document — the failure mode this line recorded at `DET-01`'s `A10`.
§8.2, §11.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the identification is asserted,
load-bearing, and unfalsifiable from this repository.** The object it identifies
the mode WITH is defined in a manuscript that is not here. §10, §15.3.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — three provenances remain
unexamined and any of them could reintroduce circularity.** The source and
configuration mapping, the coupling, and the normalisation. §11, §15.5.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — the search vocabulary is not
exhaustive and no end-to-end reading of the manuscript was performed.** Twenty
terms, 161 lines of 1833. §15.4.

### 17.3 Clarifications, not defects

**Rule 13's two diagnostic orders were not exercised**, because no environment
failure occurred; I name neither as the one used, per `§8`.

**`refs/heads/main` is a stale local ref at `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`.**
The landing pushes `HEAD:refs/heads/main` to `origin`; the local ref is not the
target and is not moved. §2.

**The `--all` commit count is 531, up from 527.** The four new commits are this
task's own. Recorded so the figure is not read as instability. §1.

**The stop-hook's recurring "405 unpushed commits" claim on the session branch is
an artefact of the clone having been unshallowed.** The session branch has
nothing unpublished and is not pushed by this task. §1.
