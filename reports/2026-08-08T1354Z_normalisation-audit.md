# Execution report — normalisation audit: `G_ω` against the derived vector coefficient

Authority: `specs/2026-08-08T1354Z_normalisation-audit.md`
Evidence base: `eb88a2c9174cfda746c266924e741a6f88134234`
External evidence base: `zetacheng/3-vector-sector` @
`8c363ef08368f5c022278ea5f36e01496be3d5ca`
Branch: `fix/normalisation-audit-g-omega`
Classification: MATERIAL. Branch only.

**This produces one row of an evidence table. It ratifies nothing.**
`derivations/CANONICAL_INTERACTION.md` is unmodified and its DRAFT v0.5
banner stands. No Paper-3 content was modified and no Paper-3 file was
copied into this repository.

Written at head `dde66fce424a0443c1cb35c5e6ec9c6e01efc4ff`; it contains
neither its own commit SHA nor the final branch head.

---

## 1. The verdict, first

### **`NORMALISATION MAPPING`**

    Paper 2 (this repository)   c_J     = -G/(2N)   coefficient of (psibar gamma_mu psi)^2
    Paper 3                     G_omega = -G/N      defined by L_V = (G_V/2) J_mu J^mu
    mapping                     G_omega = 2 * c_J

**Your reading is confirmed, and by stronger evidence than expected.**
The Paper-3 note does not merely imply the factor of one half — **it
writes the coefficient of `J_μJ^μ` explicitly as `−(G/2N)` on the same
line on which it converts to `G_ω`.** That is the same number this
repository derives, for the same operator, in the same normalisation.

**The two documents never disagreed about a coefficient. They disagreed
about which quantity they name.** `G_ω` is not the operator coefficient;
it is twice it, by Paper 3's declared convention.

`REPOSITORY_DEFECT` is excluded because the same operator under the same
normalisation carries the *same* value in both documents.
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` is excluded because both
normalisations are stated precisely and quotably. **Neither value was
adjusted.**

## 2. A1 — pinned inputs

**Local**, read from the git objects at the evidence base. All four
matched; no STOP.

    derivations/CANONICAL_INTERACTION.md
      27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81   MATCH
    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
      fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a   MATCH
    results/P2-CHANNEL-FREEZE/fierz_matrix.json
      5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9   MATCH
    derivations/P2-PHASE-01_fierz_sign_addendum.md
      a0553b8a79cfcd521620448f7d1d6928475573e751dd404698adcd48ad6871df   MATCH

**External**, `zetacheng/3-vector-sector` @ `8c363ef0…`:

    derivations/u3-fierz/u3_fierz.md
      6784d51a5a8d5f8b70b55213e4bf9b3eb50fc8c331397e80a239d16285d58f49   MATCH

**The evidence is AVAILABLE.** No `UNAVAILABLE EVIDENCE` finding arises,
and the distinction the authority draws was not needed — but §8 records
what would have been reported had the fetch failed.

**The channel-character branch was not used as an input.** Its artifact
does not exist at the evidence base — verified:

    $ git cat-file -e eb88a2c9…:results/P2-PHASE-01/channel-character/channel_character.json
    fatal: path '…' does not exist in 'eb88a2c9…'

It was read only *after* the recomputation, and only for its declared
normalisation (§3.2) and the value comparison (§5.2).

## 3. A2 — both normalisations, quoted verbatim

### 3.1 Paper 3, at the pinned revision

`derivations/u3-fierz/u3_fierz.md`, **line 10**:

    Classification (Paper 3 convention `L_V = (G_V/2) J_mu J^mu`, `J_mu = psibar gamma_mu psi`):

**line 11**:

    `G_V < 0` repulsive (omega survives) / `G_V > 0` attractive (fails) / `G_V = 0` no channel.

**lines 185–190**, the assembly:

    - **Level 3 — normalize to `J_mu`.** `psibar gamma_mu lambda^0 psi =
      sqrt(2/3) psibar gamma_mu psi = sqrt(2/3) J_mu`, so
      `(psibar gamma_mu lambda^0 psi)^2 = (2/3) J_mu J^mu`. Restoring `L_int = (G/2N)*[...]`:

          L_int -> (G/2N) * (-3/2) * (2/3) J_mu J^mu  =  -(G/2N) J_mu J^mu
                 =  (G_omega/2) J_mu J^mu   with   G_omega = -G/N.

**Line 189 is the decisive text.** It states the operator coefficient
and the reported coupling side by side, and the `1/2` between them is
explicit.

Two guards in the script assert that line 10 still contains
`L_V = (G_V/2) J_mu J^mu` and line 190 still contains
`G_omega = -G/N`, so a future revision that moved them would fail loudly
rather than silently quote the wrong lines.

### 3.2 This repository

The channel-character artifact declares, verbatim:

    normalisation_L_definition : coefficient of (psibar lam(0) Gamma psi)^2
    normalisation_P_definition : coefficient of (psibar Gamma psi)^2
    normalisation_relation     : c_P = (2/N) * c_L, from lam(0) = sqrt(2/N) Id_N

and reports the induced V singlet as

    normalisation_L : -G/4        normalisation_P : -G/(2*N)      sign : -1
    origin          : Fierz image, operator level (s_G applied once)

**Neither declared normalisation carries a factor of one half.** Both
are plain coefficients of a squared bilinear. `G_ω` is a third quantity.

## 4. A3 — the conversion, symbolically

    Paper 3 convention        L_V = (G_V/2) J_mu J^mu
    relation                  G_omega = 2 * c_J
    conversion factor         2
    factor origin             the explicit 1/2 in L_V = (G_V/2) J_mu J^mu,
                              line 10 of the Paper-3 note

**The factor is definitional, not algebraic.** It is a prefactor on the
*reported coupling*, and it appears nowhere in the frozen Paper-2
material because Paper 2 reports plain operator coefficients throughout.

A secondary conversion connects this repository's two internal
normalisations, and **both documents perform it identically**:

    c_J = (2/N) * c_L      from the frozen  lam(0) = sqrt(2/N) Id_N

Paper 3 does this at its Level 3, writing `sqrt(2/3)` for `N = 3`. `N` is
kept general throughout on this side.

## 5. A5 — independent recomputation

### 5.1 Recomputed from the frozen material

Not transcribed. The chain, `N` symbolic:

    canonical per-family coefficient (from interaction_decomposition)  G/(2*N)
    dirac row after the frozen matrix_rational        [0, 0, 1/2, 1/2, 0]
    c_V^Dirac                                                              1/2
    s_G applied once at operator use                                        -1
    c_V inside the bracket, general N                                     -N/2
    c_V inside the bracket at N = 3                                       -3/2
    c_L  coefficient of (psibar lam(0) gamma_mu psi)^2                    -G/4
    c_J  coefficient of J_mu J^mu                                     -G/(2*N)
    G_omega = 2 * c_J                                                     -G/N

### 5.2 Agreement with Paper 3 at every level

**Stronger than endpoint agreement, and the reason this verdict is
secure:**

    quantity                               Paper 3      recomputed    agree
    c_V^Dirac                                +1/2           1/2       True
    c_V bracket at N=3                       -3/2          -3/2       True
    coefficient of (psibar lam0 g psi)^2     -G/4          -G/4       True
    coefficient of J.J                    -G/(2*N)      -G/(2*N)      True
    G_omega                                  -G/N          -G/N       True
    all levels agree                                                  True

Agreement at every intermediate level rules out compensating errors.
**Paper 3 also applies the crossing sign once, at operator use** —
`c_V^(0) = (Grassmann -1) * c_V^Dirac * f_singlet` — which is exactly the
convention the 2026-08-07 ruling fixed here. Had the two differed on
that, endpoint agreement would have been accidental.

Paper 3's `f_singlet = 3` is `N` at `N = 3`; the general-`N` form of its
Level 2 is `−N/2`, which is what this recomputation produces.

### 5.3 Comparison with the channel-character result

Performed **after** computing, per the authority's ordering:

    c_L   channel-character: -G/4        recomputed: -G/4
    c_J   channel-character: -G/(2*N)    recomputed: -G/(2*N)
    status: CORROBORATION

**With a caveat I want on the record.** Both computations run the same
chain over the same frozen material, and both were authored in the same
session by the same executor. **That corroborates the chain, not the
judgement behind it.** A repeated calculation by the same author is weak
evidence against a conceptual error, however strong it is against a
transcription error.

**The genuinely independent check here is Paper 3**, which re-derives its
Fierz table from the 16-dimensional completeness relation at `N = 3` by a
different route, was written before this programme existed, and
reproduces every intermediate quantity. That is what makes §5.2 worth
more than §5.3.

## 6. A6 — what this row does NOT close

`derivations/CANONICAL_INTERACTION.md` §5 requires an evidence table with
several rows. **This audit produces one.** Not addressed here:

1. **starting-interaction match** — file path, line range and pinned SHA
   showing Paper 3 begins from §2's generator-sum form;
2. **`G_ω` provenance** to its derivation equation reference, as a
   provenance record — distinct from the normalisation reconciliation
   performed here;
3. **claim status `VERIFIED`** — registry path and entry;
4. **test count** — command and output digest;
5. **convention-compatibility table** — explicit comparison.

**`CANONICAL_INTERACTION.md` retains its DRAFT v0.5
ratification-candidate banner**, verified present after all work:

    1:# CANONICAL_INTERACTION.md — DRAFT v0.5 (ratification candidate)
    3:**Status: DRAFT v0.5 — ratification candidate under the Discriminator's

**Nothing here ratifies anything.** The banner is accurate, and this task
does not touch the file.

**This audit also does not revisit** the channel-character task's Layer
1b and Layer 2 withholdings. The comparison performed here is between
**algebraic coefficients of the same operator inside the written
`L_int`** — Layer 1a in that task's terms, the unconditional layer. It
says nothing about how either document's `L_int` enters a Boltzmann
exponent, and nothing about attractive/repulsive labels. In particular,
Paper 3's own line 11 classification (`G_V < 0` repulsive) is **quoted,
not adopted**.

## 7. A7 — nothing pre-existing disturbed

Blob OIDs read from the objects at the evidence base:

    GATES.md                              bd4820513217ae7e1c493328dc49536e69b8cfb8   IDENTICAL
    CONVENTIONS.md                        2d4f735c55a14fdfc5d1031a58698a8ca075fbbd   IDENTICAL
    AGENTS.md                             5e60b5fcd6e9e30e96300f3bd09811fb9c3221f3   IDENTICAL
    pyproject.toml                        9fc6fdd196dd2e0c2c323bfbf4a6f3fe183e8ee4   IDENTICAL
    derivations/CANONICAL_INTERACTION.md  6e5d9e1bb7dffe67e7b9ada026b366ef0e10a2a9   IDENTICAL

No gate, gate status, verdict, artifact digest, hash-pinned artifact or
pre-existing test was modified. The base-to-head change list contains
additions only (§9).

**The Paper-3 clone is clean and at the pinned revision** after all
reading:

    $ git -C /workspace/zetacheng/3-vector-sector status --porcelain=v1 | wc -l
    0
    $ git -C /workspace/zetacheng/3-vector-sector rev-parse HEAD
    8c363ef08368f5c022278ea5f36e01496be3d5ca

### Repository inputs actually read, by path, across both repositories

    2-emergent-gravity
      derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
      results/P2-CHANNEL-FREEZE/fierz_matrix.json
      derivations/CANONICAL_INTERACTION.md
      derivations/P2-PHASE-01_fierz_sign_addendum.md
      results/P2-PHASE-01/channel-character/channel_character.json
        [read from the unmerged branch object, not the base tree]

    3-vector-sector (read-only, external pin)
      derivations/u3-fierz/u3_fierz.md

**None of the three prohibited sources appears.** The quarantined
`−3.2(5)`, the suspended `P2-BETAV-CIRC-01` result, and the historical
Finding 5 extraction were **NOT READ**.

## 8. Reading a second repository — difficulties met

The authority asks specifically, because the procedure is not well
tested here. **Four things came up; none blocked the task, and two are
worth carrying forward.**

**(a) The external repository is not in this session's attached scope,
and did not need to be.** `add_repo` reported it as a public repository
served by the session's anonymous git proxy, attaching nothing. That is
the lighter path and the correct one for read-only evidence: **no
credentials were minted and no push capability was acquired for a
repository this task must not modify.** Worth recording as the pattern
to reuse.

**(b) A shallow clone might not have contained the pinned revision.** It
did — the pin is the current default HEAD — but that was luck, not
design. I fetched the revision by SHA explicitly (`git fetch --depth 1
origin <sha>`, exit 0) rather than relying on it, so the procedure works
for a pin that is *not* HEAD. **A future audit pinning an older Paper-3
commit should do the same**; a bare `--depth 1` clone would silently give
a different revision, and the digest check would then fail confusingly
rather than informatively.

**(c) Line numbers are a fragile citation key across repositories.** The
authority asks for line references, and I have given them — but a
Paper-3 revision that inserts a paragraph invalidates them while the
digest still describes a different file. I mitigated this with **content
guards** in the script: it asserts that line 10 still contains
`L_V = (G_V/2) J_mu J^mu` and line 190 still contains `G_omega = -G/N`,
and raises if either moved. **I would make that guard a standing
requirement for cross-repository quotation**, since the failure mode
otherwise is a quotation that is confidently wrong.

**(d) "Read, don't merge" needed an explicit boundary in the tooling,
not just in intent.** The clone lives at `/workspace/zetacheng/3-vector-sector`,
outside this repository's tree, so no Paper-3 file can reach a commit
here by accident — the scope checker would catch it, but the layout means
it cannot arise. **The quotations in this report and in the derivation
note are the only Paper-3 content that entered this repository**, as
quoted text inside documents I authored.

## 9. A8, A9-pre, A10

### 9.1 A8 — manifest template

`{PUSHED_HEAD}` placeholder so the digest does not depend on the report
commit. SHA-256:
`1dcee507de0a7913a54b54a8e91fcb3710e5a93829492e01bac6bf4a38be92f1`.

    {
      "base": "eb88a2c9174cfda746c266924e741a6f88134234",
      "head": "{PUSHED_HEAD}",
      "mode": "exact",
      "required": [
        {"operation": "add", "path": "specs/2026-08-08T1354Z_normalisation-audit.md"},
        {"operation": "add", "path": "derivations/P2-NORMALISATION-AUDIT_g_omega.md"},
        {"operation": "add", "path": "scripts/p2_normalisation_audit.py"},
        {"operation": "add", "path": "results/P2-PHASE-01/normalisation-audit/g_omega_audit.json"},
        {"operation": "add", "path": "reports/2026-08-08T1354Z_normalisation-audit.md"}
      ],
      "optional": [],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

**Five additions, zero modifications**, matching A8. The `{HHMM}` token
resolved to `1354` at commit 1 and is reused. The resolved manifest, its
SHA-256 and the checker JSON at the pushed head are post-report evidence.

Pre-report check at `dde66fce`, where the report commit does not yet
exist, so four additions:

    $ python -m scripts.governance_tools.scope_checker --repo . --manifest <pre>
    {
      "base": "eb88a2c9174cfda746c266924e741a6f88134234",
      "failures": [],
      "head": "dde66fce424a0443c1cb35c5e6ec9c6e01efc4ff",
      "mode": "exact",
      "observed_operations": [
        {
          "operation": "add",
          "path": "derivations/P2-NORMALISATION-AUDIT_g_omega.md"
        },
        {
          "operation": "add",
          "path": "results/P2-PHASE-01/normalisation-audit/g_omega_audit.json"
        },
        {
          "operation": "add",
          "path": "scripts/p2_normalisation_audit.py"
        },
        {
          "operation": "add",
          "path": "specs/2026-08-08T1354Z_normalisation-audit.md"
        }
      ],
      "overall": "PASS",
      "tool": "scope_checker"
    }
    === exit 0 ===

`failures` empty, **zero modifications** — the criterion that matters
here, since `CANONICAL_INTERACTION.md` must not move.

### 9.2 A9-pre, at head `dde66fce`

    $ python -m pytest tests/test_repository_structure.py   ->  4 passed               exit 0
    $ python -m pytest tests/test_si1_governance.py         -> 14 passed               exit 0
    $ python -m pytest tests/test_gate_anchors.py           -> 18 passed, 2 deselected  exit 0
    $ python -m pytest tests/test_governance_tools.py       ->  8 passed               exit 0

All four exit 0, captured from `python -m pytest` itself and not from the
tail of a pipeline.

### 9.3 A10 — lint

    $ ruff check scripts/p2_normalisation_audit.py
    All checks passed!
    === exit 0 ===

Run from the repository root so `[tool.ruff]` applies. Clean on the first
attempt.

### 9.4 On the absent test file

A8 states no new test file is required and asks me to say so if I judge
one worth adding. **I judge one worth adding, and did not add it.**

The script already fails loudly on the two conditions that matter — a
digest mismatch on the external pin, and either Paper-3 line moving away
from its expected content — and it raises if the recomputation disagrees
with the channel-character result. Those are assertions in production
code, which is weaker than a test only in that nothing re-runs them on a
schedule.

What a test would add is **regression coverage for the mapping itself**:
that `G_omega == 2 * c_J`, and that `c_J == -G/(2N)` recomputed from the
freeze. If the freeze or the Fierz matrix ever changed, that test would
fail where today only a re-run of this script would notice. `tests/`
already carries `test_p2_phase01_fierz_and_depths.py`, which is the
natural home. **I did not add it because the manifest is frozen at five
paths and a sixth would be a scope violation**, which is the correct
precedence.

### 9.5 Reproducibility

The artifact is byte-reproducible: two consecutive runs both gave
`e695a30550de85713f54e2f84441516ba3c1b8bb62ffd97aedc39d0b229e7fb7`.

## 10. A11 — branch only

    refs/remotes/origin/main   eb88a2c9174cfda746c266924e741a6f88134234
    remote refs/heads/main     eb88a2c9174cfda746c266924e741a6f88134234
    local main                 0f7961747abe2a18b436c0b1e5b928f425ea4d9a  (stale by design)

**Local `main` was not repaired.** `fix/normalisation-audit-g-omega` was
created from `eb88a2c9…` in a separate worktree; the primary worktree was
not touched. **No branch was deleted or renamed.** No merge, no PR, no
force-push, no history rewrite.

## 11. Stops and clarifications

**Stops: none.** All five pins matched; the external evidence was
available; the recomputation agreed with the channel-character result, so
its STOP did not fire; and the verdict was `NORMALISATION MAPPING`, not
`REPOSITORY_DEFECT`, so that STOP did not fire either.

**Finding 1 — secondary, and it resolves a finding I raised yesterday.**
The channel-character report recorded as its Finding 4 that
`CANONICAL_INTERACTION.md` §3's `G_ω = −G/N` did not equal the derived
`−G/(2N)`, that the signs agreed but the magnitudes did not, and that it
could not be resolved because the source note was not in this repository.
**That finding is now closed: it was a normalisation difference, exactly
as this task's authority suspected.** I was right to flag it and right
not to assert the explanation without the source; the explanation I
guessed at — "a different definition of what `G_ω` multiplies" — turns
out to be correct, but it was a guess then and is evidence now.

**Finding 2 — secondary, a documentation observation.**
`CANONICAL_INTERACTION.md` §3 records `G_ω = −G/N` **without stating the
`L_V = (G_V/2) J_μ J^μ` convention that defines it.** A reader of Paper 2
alone therefore cannot tell that `G_ω` is twice an operator coefficient,
which is precisely the confusion this audit resolved. **The fix would be
one clause in §3** naming the convention, or a pointer to the Paper-3
line. I have not made it: the file is frozen to this task and amending it
is a governance action.

**Finding 3 — secondary, method.** Line-number citation across
repositories is fragile; see §8(c). Mitigated here with content guards,
recommended as a standing requirement.

**Clarification 1 — reading the unmerged branch.** §2A asks for the
normalisation *declared* by `channel_character.json`, while A1 says the
channel-character branch is not a pinned input. I read it from the branch
object **after** completing the recomputation, and used only the
declaration strings and — in §5.3, explicitly after the fact — the
values, for comparison. **No value from that branch entered the
computation.** I flag the reading because the two clauses could be taken
to conflict, and I resolved them by ordering rather than by choosing one.

**Clarification 2 — `derivations/P2-PHASE-01_fierz_sign_addendum.md` was
pinned and verified but not quoted.** It is pinned by A1 and its digest
matched. Its content — the 2026-08-07 ruling's consequence for the
induced V and A — is background to the `s_G` convention used in §5.1, but
no line of it is quoted in the reconciliation, because the reconciliation
turns on the operator coefficient rather than on the sign ruling. Noted
so the input list is not read as implying more use than was made.

## 12. Anything ambiguous, unsatisfiable, or that I would have specified differently

**Nothing was unsatisfiable.** A1–A11 were met as written.

**(a) The `UNAVAILABLE EVIDENCE` / `ABSENT CONTENT` distinction is
excellent and I would generalise it.** It did not arise — the fetch
worked — but it is the same failure-to-observe-versus-negative-result
distinction that has produced findings three times this week, stated
prospectively for once instead of caught afterwards. **I would put it in
`CONVENTIONS.md`**, not only in individual specifications.

**(b) A8 freezes five paths and A8 also invites me to judge whether a
test is warranted.** §9.4 explains that I judge one warranted and could
not add it. That is the right precedence — a frozen manifest should win —
but the specification could resolve it directly by either authorising a
sixth path conditionally or stating that the follow-up test is a separate
task. As written I can only record the judgement.

**(c) §2A asks for "the normalisation under which
`channel_character.json` reports its vector coefficient", and that file
is on an unmerged branch.** Clarification 1. Since A1 deliberately
excludes that branch as an input, saying explicitly that the artifact may
be *quoted* but not *consumed* would have removed the tension I had to
resolve by ordering.

One thing I would keep exactly as written: **"If your computation
disagrees, your computation is the evidence," together with "do not
adjust either coefficient to make them agree."** The expected answer was
supplied in §0 and it turned out to be right, which is the case where an
executor is most likely to reason backwards from it. Being told in
advance that disagreement was an acceptable output is what made it
possible to check rather than confirm — and the check ended up stronger
than the endpoint comparison, because it went through Paper 3's
intermediates.

## 13. Commits, and commit-message hygiene

**Commit 1** — `dc4a2b4e52fb593cffa7a9408c1bfd23b691b3e4`

    spec: normalisation audit reconciling G_omega with the derived coefficient

    Records the PI specification for the normalisation audit, evidence base
    eb88a2c9174cfda746c266924e741a6f88134234, transcribed verbatim.

    The task produces one row of the evidence table CANONICAL_INTERACTION.md
    requires for its own ratification and which has never been produced: the
    normalisations-match row. It quotes both operator normalisations, one
    from this repository and one from Paper 3 at a pinned external revision,
    converts one to the other symbolically with N general, and reaches one
    of three named verdicts.

    It ratifies nothing, removes no banner, modifies no Paper-3 content, and
    closes no other row of that table. The vector coefficient is recomputed
    here rather than consumed from the unmerged channel-character branch.

**Commit 2** — `6f030117e707f5d30c4b54fcea036465b9d0a573`

    derivation: G_omega reconciles with the derived vector coefficient

    Fixes the analytic content before any production code, per AGENTS.md
    rule 3.

    Verdict: NORMALISATION MAPPING. Paper 3 defines G_omega by
    L_V = (G_V/2) J_mu J^mu, so G_omega is twice the coefficient of
    J_mu J^mu. Line 189 of the pinned Paper-3 note writes that coefficient
    explicitly as -(G/2N) before converting it, which is the same value this
    repository derives for the same operator. The two documents never
    disagreed about a coefficient, only about which quantity they name, so
    the apparent factor of two is definitional and neither value was
    adjusted.

    The recomputation reproduces Paper 3's intermediate quantities at every
    level, not only the endpoint: the Dirac coefficient +1/2, the bracket
    coefficient -3/2 at N=3, -G/4 for the lam(0) bilinear squared, and
    -G/(2N) for J.J. Paper 3 also applies the crossing sign once at operator
    use, matching the 2026-08-07 ruling.

    This is one row of the CANONICAL_INTERACTION.md evidence table. The
    other rows are untouched and its DRAFT banner stands.

**Commit 3** — `dde66fce424a0443c1cb35c5e6ec9c6e01efc4ff`

    feat: compute the G_omega normalisation reconciliation

    Adds the script and the results artifact for the normalisation audit.

    The vector singlet coefficient is recomputed from the frozen
    interaction_decomposition and the frozen matrix_rational before the
    unmerged channel-character artifact is read, and the Paper-3 note is
    read from a read-only clone of the pinned external revision with its
    digest verified. Both normalisations are quoted with line references,
    the conversion factor of two is traced to the explicit half in
    L_V = (G_V/2) J_mu J^mu, and the verdict is selected by the evidence
    rather than declared.

    Verdict NORMALISATION MAPPING: G_omega = 2 * c_J, and the recomputation
    reproduces Paper 3 at every intermediate level, not only the endpoint.
    The comparison against the channel-character result is corroboration,
    recorded with the caveat that both run the same chain and the genuinely
    independent check is Paper 3's separate route.

    No Paper-3 file is copied here and CANONICAL_INTERACTION.md is
    unmodified. The artifact is byte-reproducible across runs.

**Intended report commit message** (commit 4):

    docs: report the G_omega normalisation audit

    Records A1-A11 for the normalisation row of the CANONICAL_INTERACTION.md
    evidence table.

    Verdict NORMALISATION MAPPING, selected by evidence: line 189 of the
    pinned Paper-3 note writes the coefficient of J.J as -(G/2N) on the same
    line on which it converts to G_omega = -G/N, and -(G/2N) is what this
    repository derives for the same operator. G_omega is twice an operator
    coefficient by Paper 3's declared L_V = (G_V/2) J.J convention, so the
    apparent factor of two is definitional. The recomputation reproduces
    Paper 3 at every intermediate level.

    Closes the channel-character report's Finding 4. Records what the row
    does not close, the DRAFT banner standing, four observations on
    cross-repository reading, and a test judged worth adding but outside
    the frozen manifest.

### Trailer suppression, per commit

The harness convention in this environment appends `Co-Authored-By:` and
`Claude-Session:` trailers. This specification permits neither. Both were
**actively suppressed** on every commit of this branch by composing the
message in a file and committing with `git commit -F`, never with `-m`.

    commit 1  dc4a2b4e   suppressed: Co-Authored-By, Claude-Session
    commit 2  6f030117   suppressed: Co-Authored-By, Claude-Session
    commit 3  dde66fce   suppressed: Co-Authored-By, Claude-Session
    commit 4  (report)   suppression applied identically; stored message
                         read back as post-report evidence

Each proposed message was inspected before committing and each stored
message read back with `git log -1 --format=%B` after; a `grep` for
`co-authored-by`, `claude-session`, `claude.ai`, `generated with` and
`noreply@anthropic` matched nothing in either form, for all three commits.

**Suppression is a fact disclosed here, not an absence** — a convention
that would have added the trailers was deliberately bypassed.

Author and committer identity (`Claude <noreply@anthropic.com>`) and the
SSH signature from the global `commit.gpgsign=true` are commit-object
headers, not message content, and are outside this specification's scope.
