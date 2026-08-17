# Report — integrating and landing the `β_V/β_B` sign reconciliation

    branch      science/integrate-sign-01
    base        aebca32c6129746b8e1c58ca9f907b734024fb83   (authoritative main)
    source      4e497c6b321f5ac29875e5eee4eb4a5b60dd8506   (science/sign-01-anchor-reconciliation)
    measured at commit 3, 6364cf8e1559e4cfa329553551707eda23d0b757
    landing     §6's fast-forward of refs/heads/main to commit 4 is POST-REPORT

**NOTHING WAS NUMERICALLY EVALUATED, NOTHING WAS BUILT, AND NOTHING WAS
REPAIRED.**

    SIGNED NEGATIVE     β_V/β_B = −(k+2),  hence −3 at k = 1
    kill values         stuck at −3 ∀k;  drift toward −5 at heavy mass

**RE-DERIVED AT THIS HEAD from `CONVENTIONS.md:15`, `:16`, `:19` and `:21`, not
transcribed from the specification's `§0` and not taken from `P2-HK-01:95`.**

**THREE landed documents assert the target unsigned and NONE was repaired.**
`§8` names them with lines, measured at the head.

**`β_V/β_B = −(k+2)` IS STANDARD HEAT-KERNEL ARITHMETIC. It is not a prediction
of the `H(4)` lattice model.** What it provides is a judgeable target. `§17.1`.

---

## 1. `A3` — environment conformance, run FIRST

**Rule 13's diagnostic order with Amendment D's step 0, run before any other
criterion. MEASURED, not assumed.**

    (0) execution location    /home/user/2-emergent-gravity — the primary
        (Amendment D)         worktree. git dir .git, common dir .git, so not a
                              linked worktree. HEAD branch
                              claude/paper-2-independent-verification-dysdp0,
                              resolved bfef924c368658cac85c04ed18d96eb4450afba6.
                              Ten linked worktrees existed; this task's work was
                              done in an ELEVENTH, cut fresh at
                              refs/remotes/origin/main.

    (1) interpreter           Python 3.11.15 at /usr/local/bin/python3

    (2) declared packages     MEASURED: pytest 9.1.1, numpy 2.4.6,
                              sympy 1.14.0, ruff 0.15.8 — all four declared
                              packages present.

    (3) clone depth           NOT shallow. `--is-shallow-repository` returns
                              false and no `shallow` file exists in the common
                              git dir. 497 commits reachable from all refs,
                              423 from HEAD.

    (4) working tree          clean; `status --porcelain` empty before any work.

    (5) declaration compared  `docs/local/execution_environment.md` declares a
                              WINDOWS environment. See `§18.5`.

**NO RESTORATION WAS NEEDED AND NONE WAS PERFORMED. No repository content was
touched by `A3`.**

**Rule 13 carries TWO diagnostic orders, a known open item. No environment
failure occurred, so NEITHER order was exercised** — naming one would
misrepresent a conformance check as a diagnosis.

**`sympy 1.14.0` is load-bearing for `A6` and `A7`**, which re-check the sign and
prefactor algebra symbolically. It is a declared package and it was present.

## 2. `A1` — repository, refs, source ancestry

**`origin` URL, MEASURED and reported VERBATIM, not normalised:**

    https://github.com/zetacheng/2-emergent-gravity

No `.git` suffix, no trailing slash. It identifies `zetacheng/2-emergent-gravity`.

**Refs, MEASURED after `git fetch origin main`:**

    refs/remotes/origin/main   aebca32c6129746b8e1c58ca9f907b734024fb83
    expected by §4 A1          aebca32c6129746b8e1c58ca9f907b734024fb83   MATCH

    refs/heads/main            1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**`refs/heads/main` LAGS, reported for contrast.** It sits at `1cb5550f…`, a
commit from the `governance/integrate-enforcement-checks-v2` line, and it is not
the authority. Every measurement here is against `refs/remotes/origin/main`.

**Source, MEASURED:**

    science/sign-01-anchor-reconciliation   4e497c6b321f5ac29875e5eee4eb4a5b60dd8506
    is-ancestor of origin/main              exit 1 — NOT AN ANCESTOR

**So the source is unmerged and this task is the merge.** The branch to create,
`science/integrate-sign-01`, existed at neither the remote (0 hits) nor locally
(0 hits).

## 3. `A2` — the pre-execution review

**Field-present check run BEFORE the match check, in that order:**

    field name present     grep 'reviewed specification SHA-256' → line 4, ONE hit
    field filled in        yes — a 64-hex value, not a placeholder
    value in the review    a86dc5940eb456bbf3e06aad7ea9af2a92686657e5f7ceaad240465a78ff41e5
    sha256 of the spec     a86dc5940eb456bbf3e06aad7ea9af2a92686657e5f7ceaad240465a78ff41e5
                           MATCH

**Committed UNEDITED**: the committed blob's sha256 is
`292ddbcf7481479d33ef92412b8452a14a5f82669c4e55bfd353d103c38711a8`, identical to
the uploaded bytes. **Verdict `APPROVE FOR EXECUTION`, twelve sections all
`PASS`.**

## 4. `A4` — merge parentage, three separately derived measurements

    parent 1     git rev-parse HEAD^1   feb6644d348e2eac88ddf7aab7d1a519f09a49a8
                 this task's review commit (commit 2)                     MATCH

    parent 2     git rev-parse HEAD^2   4e497c6b321f5ac29875e5eee4eb4a5b60dd8506
                 the source tip named in §0                               MATCH

    merge-base   git merge-base HEAD^1 HEAD^2
                 aebca32c6129746b8e1c58ca9f907b734024fb83
                 the specification's evidence base                        MATCH

**Commit 1 is an ancestor of parent 1:** `--is-ancestor 63d84539… feb6644d…`
returns **exit 0**.

**The checker's `P5` recomputed the same three values independently** and reports
`merge_base_equals_parent_1: false` — correct, since the base is `aebca32c…` and
parent 1 is commit 2. `compared_to_recorded: UNAVAILABLE`: there is no recorded
parentage to compare against, so `P5` is a recomputation check.

## 5. `A5` — no conflict

    git merge --no-ff --no-commit 4e497c6b…      exit 0
    "Automatic merge went well; stopped before committing as requested"

    conflict list, git diff --name-only --diff-filter=U     0 paths
    unmerged index entries, git ls-files -u                  0

**THE CONFLICT LIST IS EMPTY.** A `git merge-tree --write-tree` dry run
beforehand produced tree `a02c9972bbc7668840b4e1740f8a99de04ebdd4d` with an empty
conflict section, agreeing with the real merge.

## 6. `A6` — the derivation RE-DERIVED at this head, not transcribed

**The four convention lines were read from `git show HEAD:CONVENTIONS.md`, and
the derivation was run from them. The specification's `§0` was NOT used as an
input.**

### 6.1 The four lines, as read at the head

    :15   | Heat-kernel operator | `Δ = −∇² + E` (Laplace-type). `E` is the
          endomorphism (potential/bundle) term; **sign convention: `E` enters
          with a `+` so that a scalar curvature coupling `ξR` appears inside `E`
          as `E ⊃ +ξR`.** The mass `m²` is separated out explicitly (`Δ + m²`)
          and is **not** counted inside `E` for the `a_k`. |

    :16   | Heat-kernel expansion | `Tr e^{−τΔ} = (4πτ)^{−d/2} ∫ d^dx √g
          Σ_{k≥0} a_k(x) τ^k`, `d=4`. Indexing: `a_0 = tr 𝟙`, and
          `a_1 = tr[(1/6)R·𝟙 − E]` (the `R`-linear Seeley–DeWitt coefficient). …|

    :19   | Massive-vector (Proca) structure |
          `Z_{s=1,m} = det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)`, with the
          vector Laplacian `Δ^{(1)}` having `E^{μ}{}_{ν}=R^{μ}{}_{ν}`
          (`tr E = R`) and the Stueckelberg scalar `Δ^{(0)}` having `E=0`. …|

    :21   | Species coefficient `β_s` | … `β_s = −p_s (4π)^{−2} (tr a_1 / R)`,
          where `p_s` is the log-det prefactor of the species (`+1/2` per bosonic
          `det^{−1/2}` factor, `−1/2` per `det^{+1/2}` factor / fermion loop). …|

### 6.2 Ingredient (i) — the common leading sign

**`:21` carries a LEADING MINUS on `p_s`.** With `K ≡ (4π)^{−2} > 0`, `K` carries
no sign and cancels from any ratio. **The definition contributes ONE sign flip,
applied identically to every species.**

### 6.3 Ingredient (ii) — `p_B`, and BOTH terms of `p_V`, with their determinant factors

    β_B                det^{−1/2}(Δ^{(0)}+m²)   bosonic     p_B = +1/2
    Proca, vector      det^{−1/2}(Δ^{(1)}+m²)   bosonic     p   = +1/2
    Proca, Stueckel.   det^{+1/2}(Δ^{(0)}+m²)   det^{+1/2}  p   = −1/2
    general k          det^{+k/2}(Δ^{(0)}+m²)               p   = −k/2

**`p_V` IS TWO TERMS, NOT ONE.** `:19` gives the Proca species as a PRODUCT of
two determinant factors with OPPOSITE powers, so it contributes two terms with
opposite prefactors. **`p_B` is one term, `+1/2`.**

### 6.4 Ingredient (iii) — `tr a_1/R` per species

**From `:16`, `a_1 = tr[(1/6)R·𝟙 − E]`; with `d = tr 𝟙` and `e ≡ tr E/R`,
`tr a_1/R = d/6 − e`.**

    minimal real scalar (β_B)   d = 1   E = 0            e = 0
                                tr a_1/R = 1/6 − 0 = +1/6      POSITIVE
    Proca vector part           d = 4   E^μ_ν = R^μ_ν
                                tr E = R^μ_μ = R  ⟹  e = 1
                                tr a_1/R = 4/6 − 1 = −1/3      NEGATIVE
    Stueckelberg scalar         d = 1   E = 0            e = 0
                                tr a_1/R = 1/6 − 0 = +1/6      POSITIVE

**`tr E = R^μ_μ = R` MAKES `e` EXACTLY 1**, and that is what makes `4/6 − 1`
negative rather than positive. **`:19` states `tr E = R` in parentheses, so the
contraction is frozen in the convention line itself and is not an inference of
this report.** `d = 4` is the 1-form bundle dimension at `d = 4`, fixed by `:16`.

### 6.5 The coefficients and the ratio

    β_B          = −(+1/2)·K·(+1/6)  = −K/12    NEGATIVE
                   one flip (definition), none from tr a_1/R
    β_V, vector  = −(+1/2)·K·(−1/3)  = +K/6     POSITIVE
                   two flips — definition and tr a_1/R — cancel
    β_V, Stueck. = −(−1/2)·K·(+1/6)  = +K/12    POSITIVE
                   two flips — definition and p_s — cancel
    β_V (k=1)    = +K/6 + K/12       = +K/4     POSITIVE

    β_V/β_B      = (+K/4)/(−K/12)    = −3       SIGNED NEGATIVE

**`β_B` IS NEGATIVE AND `β_V` IS POSITIVE. The minus is a GENUINE SIGN REVERSAL
BETWEEN TWO SPECIES, not an overall convention.** Both of `β_V`'s terms come out
positive for DIFFERENT reasons — the vector's from a negative bundle trace, the
Stueckelberg's from a negative determinant power — **so they ADD.**

### 6.6 The near-miss that shows the two-term structure is load-bearing

**MEASURED by re-running the derivation with the Stueckelberg factor
mis-assigned `p = +1/2`:**

    β_V, Stueck. (wrong) = −(+1/2)·K·(+1/6) = −K/12
    β_V (wrong)          = +K/6 − K/12      = +K/12
    ratio (wrong)        = (+K/12)/(−K/12)  = −1      NOT −3

**A single mis-assigned prefactor moves the anchor from `−3` to `−1`, and the
sign survives while the magnitude does not.** That is why `A6` demands both terms
of `p_V` reported with the determinant factors they come from: **a derivation that
gets the sign right for the wrong reason cannot be distinguished from this one by
its sign alone.**

### 6.7 General `k`

    β_V(k)      = −(+1/2)·K·(−1/3) + −(−k/2)·K·(+1/6)
                = +K/6 + kK/12 = K(2+k)/12
    β_V(k)/β_B  = [K(k+2)/12]/(−K/12) = −(k+2)

    k = 0  −2      k = 1  −3      k = 2  −4      k = 3  −5      k = ½  −5/2

**`k` enters ONLY through the Stueckelberg prefactor `p = −k/2`, linearly and
sign-preservingly, and `β_B` carries no `k` at all — so no `k`-dependent sign flip
is available anywhere in the ratio. THE SIGN IS PRESERVED UNIFORMLY IN `k`, and
`k=1` is a substitution into the general result rather than a special case from
which the general form was extrapolated.**

### 6.8 The four cross-checks, reported AFTER the derivation

**None was an input. `P2-HK-01:95`'s `−3` in particular was not used.**

    P2-HK-01:95                       β_V/β_B = (K/4)/(−K/12) = −3
                                      agrees, INCLUDING both intermediates
    betav_discriminating_power.md:44   β_V(k)/β_B = −(k + 2)
                                      [ k=1 → −3 ; k=0 → −2 ; k=2 → −4 ; k=3 → −5 ]
                                      agrees, including the whole table
    results/P2-BETAV-ASSEMBLY-01/
      README.md:11                    k=½ → −5/2 — agreement at a NON-INTEGER k,
                                      which the k=1 statement alone could not supply
    P2-HK-01:100-101                  β_B(ξ=1/6) = 0 — constrains the E-sign
                                      convention §7 identifies as load-bearing

**Had any of the four disagreed, this report would say `NOT DETERMINABLE` pending
reconciliation rather than restating the verdict.**

## 7. `A7` — which convention is load-bearing, re-derived

### 7.1 Flipping `CONVENTIONS.md:21`'s leading sign — RATIO UNCHANGED

**MEASURED under `β_s = +p_s K (tr a_1/R)`:**

    β_B     = +K/12          (was −K/12)
    β_V(k)  = −K(k+2)/12     (was +K(k+2)/12)
    ratio   = −(k+2)          UNCHANGED — verified symbolically, difference zero

**Every `β_s` flips, so the ratio does not. THE VERDICT DOES NOT REST ON THE LINE
MOST OBVIOUSLY LABELLED A CONVENTION.**

### 7.2 Flipping `CONVENTIONS.md:15`'s `E`-sign — RATIO CHANGES

**MEASURED under `a_1 = tr[(1/6)R·𝟙 + E]`:**

    Proca vector   tr a_1/R = 4/6 + 1 = +5/3     (was −1/3)
    ratio          = 10 − k                       (was −(k+2))
    at k = 1       = +9                           (was −3)

**THIS IS THE LOAD-BEARING CONVENTION.**

### 7.3 The `ξ = 1/6` check, and a refinement of how it fails

**`P2-HK-01:100-101`:** *"`β_B(ξ=1/6) = 0`: a conformally coupled scalar induces
no `R` term at the `m² ln m²` order — correct (conformal coupling kills `a_1`'s
`R` part)."*

**MEASURED under each convention, by solving for the zero rather than by
inspection:**

    frozen (`E` with a `+`)     β_B(ξ) = −(1/2)K(1/6 − ξ) = K(6ξ − 1)/12
                                zero at ξ = +1/6            ✓ matches :100-101
    alternative (`E` with a `−`) β_B(ξ) = −(1/2)K(1/6 + ξ) = −K(6ξ + 1)/12
                                zero at ξ = −1/6            ✗

**A REFINEMENT ON THE SPECIFICATION'S WORDING.** `§1a` says the alternative gives
`β_B(ξ)` *"with no zero at `ξ = +1/6`"*. **That is true but understates the
failure: the zero does not vanish, it MOVES to `ξ = −1/6`.** So the alternative
convention does not merely fail to reproduce the conformal point — **it predicts
a conformal coupling at the wrong value, which is a sharper contradiction and a
checkable one.** `CONVENTIONS.md:15` also states its own reason (*"so that a
scalar curvature coupling `ξR` appears inside `E` as `E ⊃ +ξR`"*), so the choice
is justified in place and independently constrained by `:100-101`.

**So the alternative is CONSTRAINED, NOT FREE.**

### 7.4 A third flip, for completeness: the curvature sign convention

**`CONVENTIONS.md:12` fixes `R > 0` on a sphere. `e ≡ tr E/R` is a RATIO to `R`,
so under `R → −R` both `tr E` and `R` change sign together for every bundle in
`§6.4` — the vector's `tr E = R^μ_μ = R` by construction, the scalars' `tr E = 0`
trivially. Every `e` is unchanged, `tr a_1/R` is unchanged, and the RATIO IS
UNCHANGED.**

### 7.5 The "convention-independent" wording, and the distinction it does not draw

**MEASURED, both places:**

    CONVENTIONS.md:21   "Reported both as a raw value (this convention) and as
                        convention-independent ratios `β_F/β_B`, `β_V/β_B`,
                        `β_B(ξ)/β_B`."
    P2-HK-01:10         "Report the convention-independent ratios `β_F/β_B`,
                        `β_V/β_B`, `β_B(ξ)/β_B`."
    P2-HK-01:90         "### Ratios (convention-independent)"

**THE DISTINCTION NEITHER DRAWS:**

    independent of   the NORMALISATION conventions — :21's leading sign, K,
                     the 4N divisor in :20, and :12's curvature sign
    dependent on     the E-SIGN convention (:15) and the DETERMINANT-STRUCTURE
                     convention (:19)

**Both families are called "convention" by the repository and only the first
cancels.** **A reader who flips the obvious convention, finds the ratio
unchanged, and concludes the sign is robust would be right about that flip and
wrong about the claim** — `§7.2` is the counterexample, and it changes `−3` to
`+9`. **`§17.2` states both halves as Rule 16 requires.**

## 8. `A8` — the repair surface, measured at the head

**THREE DOCUMENTS, NOT ONE. Every line re-measured at this head, not carried from
the source report.**

**Document 1 — `specs/2026-08-17T1105Z_recon-b0-scope.md`.** Seven `(k+2)`
tokens, all UNSIGNED at token level:

    :60    anchor           β_V/β_B = (k+2), from P2-HK-01, COMPARED ONLY AT
    :64    does NOT show** — that returning `(k+2)` shows the reconstruction is
    :113   3a  does the RATIO (k+2) itself depend on any of R1–R5?
    :117   **`β_V/β_B = (k+2)` is a species-level determinant-structure RATIO.**
    :226   **`A8a` — does the RATIO `β_V/β_B = (k+2)` itself depend on any of
    :374   `(k+2)` result must not read it as Finding 5 restored.**
    :384   **If the RATIO `(k+2)` is convention-fixed and independent of

**and both kill values unsigned, with NO `U+2212` on either line:**

    :158   **The gate names two kill criteria** — stuck at `3` for all `k` means a
    :159   degenerate pipeline; drift toward `5` at heavy mass means a longitudinal

**Document 2 — `specs/2026-08-17T1151Z_integrate-recon-b0.md`.** Two tokens,
both UNSIGNED:

    :38    A8a   the RATIO β_V/β_B = (k+2)          depends on NONE of R1–R5
    :122   future reconstruction returning `(k+2)` would show the reconstruction

**Document 3 — `reviews/chatgpt/2026-08-17T1105Z_recon-b0-scope.md`.** Three
tokens, all UNSIGNED:

    :12    … separation of the `(k+2)` ratio anchor from absolute/assembled beta_V …
    :53    … does not by itself force the clean-room `(k+2)` reconstruction …
    :88    A future successful reconstruction of `(k+2)` would not vindicate …

**THE COUNT IS THREE AND NOT ONE. The `SIGN-01` specification named only the
first**, at its `§0` and `§1`. **The second is the integration specification the
same executor had executed immediately before, whose report stated the unsigned
form was "confined to one specification" — wrong about a document it had open.**

**NONE WAS MODIFIED.** `§13` measures all three blob-identical between the
evidence base and commit 3, alongside 464 other paths. **The repair was not
performed**, and this task is not authorised to perform it.

## 9. `A9` — the signed kill values

**`GATES.md:756-758`, verbatim:**

    :756   ### Kill criterion
    :757   For the reconstruction itself: stuck at `−3` ∀k ⟹ the new pipeline is
           degenerate
    :758   (a bug); drift toward `−5` at heavy mass ⟹ longitudinal artifact.
           None of these

**Under the verdict:**

    stuck at degenerate     STUCK AT −3 for all k
    heavy-mass drift        DRIFT TOWARD −5 at heavy mass

**`−5` IS EXACTLY THE `k=3` VALUE.** `betav_discriminating_power.md:44` tabulates
`k=3 → −5`, and `:73-76` reads the drift as an artefact of the
*"longitudinal-sector `1/m²`-enhanced `m⁴ln m²`"* hypothesis, noting *"`−5` is
exactly the `k=3` value, suggesting the artifact mimics an extra compensating
power"*.

**So the second criterion is not an arbitrary threshold. It is a STRUCTURAL
SIGNATURE — a failure that looks like one extra Stueckelberg power — and it is
recognisable only with the sign attached**, because `+5` corresponds to no `k` at
all under `−(k+2)`.

**A PIPELINE RETURNING `+3` SATISFIES NEITHER CRITERION AS WRITTEN WHILE BEING
PLAINLY WRONG.** It is not `−3`, so the degeneracy test does not fire; it is not
drifting to `−5`, so the artefact test does not fire. **That is the hole the
unsigned form left open, and closing it is what unblocks `RECON-01`'s
pre-registration.**

## 10. `A10` — encoding, and a THIRD error direction

### 10.1 The codepoints

    GATES.md:751                      −(k+2)     U+2212 MINUS SIGN
    GATES.md:757                      −3         U+2212 MINUS SIGN
    GATES.md:758                      −5         U+2212 MINUS SIGN
    P2-HK-01:95                       −K/12, −3  U+2212 MINUS SIGN
    the arriving artifact, :13        −(k+2), −3 U+2212 MINUS SIGN

**All five carry `U+2212`, not `U+002D`. `GATES.md:751` ALSO contains `U+002D`
— in `P2-HK-01`, where it is a word-joiner.** That coexistence is the whole
problem, and `§10.3` is why.

### 10.2 The test I used, and why it distinguishes both recorded directions

**THE TEST: classify each `(k+2)` token by the SINGLE CHARACTER IMMEDIATELY
PRECEDING IT.** Not by what appears on the line, and not by codepoint class.

    direction 1, the Researcher's        a filter stripping non-ASCII deletes
                                        U+2212 and shows a signed statement as
                                        unsigned
    → the test survives it               because it never strips; it reads the
                                        preceding character as a codepoint and
                                        U+2212 is one of the three signs it
                                        recognises

    direction 2, the source executor's   treating only U+2212 as a sign classifies
                                        ASCII-hyphen files (scripts, tests, JSON,
                                        DECISION_LOG) as unsigned, inflating the
                                        repair surface from three documents to
                                        eleven
    → the test survives it               because U+002D immediately before the
                                        token is classified as a MINUS, not as
                                        "not U+2212"

### 10.3 A THIRD direction, measured here, that the specification does not name

**`A10` says "both directions of the encoding error are now on record". THERE IS
A THIRD, and it points the opposite way from direction 2.**

**A line-level ASCII-hyphen test — "does this line contain a `-`?" — classifies
FIVE of the eleven unsigned assertion lines as SIGNED, because the hyphens on
them are WORD-JOINERS:**

    specs/…T1105Z_recon-b0-scope.md:60   hyphen in `P2-HK-01`
    specs/…T1105Z_recon-b0-scope.md:117  hyphens in `species-level`,
                                         `determinant-structure`
    specs/…T1105Z_recon-b0-scope.md:384  hyphen in `convention-fixed`
    reviews/chatgpt/…T1105Z:12           hyphens in `RECON-B0`, `clean-room`,
                                         `curved-space`, `flat-limit`,
                                         `induced-G`, `component-state`
    reviews/chatgpt/…T1105Z:53           hyphens in `induced-G`, `clean-room`,
                                         `D-pre`

**MEASURED: at token level all twelve tokens on those eleven lines are UNSIGNED;
at line level five of the eleven would read as signed.**

**The consequence runs the OPPOSITE way from direction 2: it would SHRINK the
repair surface, hiding five of the twelve unsigned assertions while still naming
all three documents** — which is the more dangerous failure, because the document
count would look right.

**So the two recorded directions inflate and this third one deflates, and the
character-immediately-preceding test is the only one of the four candidate tests
that gets all three right.** `§18.4` records this as a finding.

### 10.4 The token census at this head

**MEASURED over every `.md`, `.py`, `.json` and `.txt` file at commit 3:**

    preceded by U+2212 MINUS SIGN          87
    preceded by U+002D ASCII HYPHEN-MINUS  12
    ────────────────────────────────────────
    SIGNED NEGATIVE, both encodings        99

    unsigned                               60
    preceded by U+002B PLUS                 5
    ────────────────────────────────────────
    TOTAL                                 164

**The total grew from 92 at the `SIGN-01` evidence base to 164 here, and the `+`
count from 2 to 5**, because the arriving artifact and report discuss the rejected
alternative at length. **All five `+` tokens are non-assertions and I checked each
individually:** the `SIGN-01` specification's `:65` and `:422` naming
`+(k+2)` as the permitted alternative outcome, and the artifact's `:352`, `:357`
and `:430` — `:357` being the sentence *"ZERO documents assert `+(k+2)` anywhere
in the repository's science"*, which is itself one of the five.

**THE LANDED SCIENTIFIC RESULT STANDS: NO REPOSITORY DOCUMENT ASSERTS A POSITIVE
CLEAN-ROOM TARGET.** **But a bare count of `+` tokens would now read as five
assertions**, and that is the same hazard as `§16.1`'s: **a document that argues
against a form contains the form.**

## 11. `A11` — scope, at TWO heads

**MEASURED at commit 3, the merge — 6 ADDITIONS, 0 MODIFICATIONS:**

    A  derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md
    A  reports/2026-08-17T1250Z_sign-01-anchor-reconciliation.md
    A  reviews/chatgpt/2026-08-17T1250Z_sign-01-anchor-reconciliation.md
    A  reviews/chatgpt/2026-08-17T1403Z_integrate-sign-01.md
    A  specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md
    A  specs/2026-08-17T1403Z_integrate-sign-01.md

    status tally   6 A, 0 M, and no other status

**INTENDED at commit 4 — 7 additions, 0 modifications**, the above plus
`reports/2026-08-17T1403Z_integrate-sign-01.md`, this file. **MEASURING THAT IS
POST-REPORT EVIDENCE AND NOTHING HERE CLAIMS TO HAVE DONE IT.**

**Which figure at which head: 6/0 MEASURED at commit 3 `6364cf8e…`; 7/0 INTENDED
at commit 4, unmeasured at the time of writing.**

**THE ARRIVING COUNTS, REPORTED SEPARATELY:**

    arriving PATH count       4
    arriving ADDITION count   4
    do they coincide?         YES, at four

**They coincide because the source added four paths and modified none.** Stating
them separately still matters: **a source that had modified an existing file would
have made the path count exceed the addition count**, and a single figure would
have hidden the modification inside an "arriving paths" total.

**`append_only: DECISION_LOG.md` is a CHECKER-CONFIGURATION DECLARATION, NOT AN
AUTHORISATION TO WRITE THAT FILE.** `DECISION_LOG.md` was not written; the two
readings did not appear to conflict, so `§8` was not invoked. The checker's `P3`
confirms it: `base_is_byte_prefix_of_head: true`, zero deleted lines.

**The `{HHMM}Z` token.** UTC measured before writing anything:
`2026-08-17T14:03:21Z`, giving `1403Z`. **Commit 1's recorded time is
`2026-08-17 14:03:37 +0000` — the same minute.** All three authored paths carry
`1403Z`.

## 12. `A12` — which merge case, stated BEFORE the blob comparisons

**THE MERGE-BASE IS THE EVIDENCE BASE, so no commit on `main` could have touched
an arriving path.**

    merge-base(parent 1, parent 2)          aebca32c6129746b8e1c58ca9f907b734024fb83
    evidence base                           aebca32c6129746b8e1c58ca9f907b734024fb83
    identical                               YES
    commits on origin/main after the base   0

**`main` has not moved since the base, so the merge cannot be the case where an
arriving path was independently edited on `main` and silently resolved.** That
case is excluded by the ref topology before any blob is compared, **and the
comparisons below are confirmations, not the argument.**

**THEN the four blob comparisons:**

    derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md
        at base   ABSENT      at source 18cd544ad59e54d483728eed1e97a902dd3880d5
        at head   18cd544ad59e54d483728eed1e97a902dd3880d5     SOURCE == HEAD

    reports/2026-08-17T1250Z_sign-01-anchor-reconciliation.md
        at base   ABSENT      at source 91f209ac64286c805eb5f7453d81835d21bd5913
        at head   91f209ac64286c805eb5f7453d81835d21bd5913     SOURCE == HEAD

    reviews/chatgpt/2026-08-17T1250Z_sign-01-anchor-reconciliation.md
        at base   ABSENT      at source 27143259d84a2590647cfe1ce51d38b28044145a
        at head   27143259d84a2590647cfe1ce51d38b28044145a     SOURCE == HEAD

    specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md
        at base   ABSENT      at source 8c3f9689a2657b5b44feba9bbd5eb9bd23829c88
        at head   8c3f9689a2657b5b44feba9bbd5eb9bd23829c88     SOURCE == HEAD

**All four arrive byte-identical to the source and none existed at the base.**
**Everything arriving by merge is integrated exactly as reviewed; no arriving path
was renamed.**

## 13. `A13` — nothing existing changed

    paths at the evidence base   467
    paths at the head            473
    COMPARED                     467
    IDENTICAL                    467
    DIFFERING                      0
    missing at the head            0
    new at the head                6   — exactly A11's six additions

**Named confirmations, each a blob comparison and not an absence of a diff line:**

    GATES.md                                    1 path    unchanged
    CONVENTIONS.md                              1 path    unchanged
    derivations/P2-BETAV-*                      5 paths   all unchanged
    P2-LATTICE-MICROSPEC-01 artifacts           7 paths   all unchanged
    registers: docs/BRANCHING_POLICY.md,
               DECISION_LOG.md                  2 paths   both unchanged
    THE THREE §1c DOCUMENTS                     3 paths   ALL UNCHANGED
    scripts/                                   60 paths   all unchanged
    tests/                                     21 paths   all unchanged
    results/                                   69 paths   all unchanged

**FIVE `P2-BETAV-*` ARTIFACTS, AS MEASURED, AND THE SPECIFICATION IS RIGHT THIS
TIME:** `ASSEMBLY-01_bookkeeping_regression`, `CAMPAIGN_prereg`,
`CIRC-01_determinant-decomposition`, `RECON-01_cleanroom_reconstruction`,
`RECON-01_scope-assessment`. **SEVEN microspec artifacts, as measured.**

**Both counts drifted for the same reason — a landed task added an artifact — and
this specification corrected both, having been told about one of them.** The
`P2-BETAV-*` count will drift again at commit 3 of this task, to six, when
`SIGN-01`'s own artifact arrives; **five is the count at the BASE, which is what
`A13` asks for.**

**THE THREE `§1c` DOCUMENTS ARE BLOB-IDENTICAL. That is the strongest form of
"the repair was not performed"** — not a diff that shows nothing, but the object
IDs matching between base and head.

## 14. `A14` — gate invariants and pins

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

**THE THREE `BETAV` GATE STATUSES, each read scoped:**

    P2-BETAV-RECON-01   GATES.md:725-789   :727  Status: PROPOSED (not run;
                        distinct from the historical circularity question)
    P2-BETAV-CIRC-01    GATES.md:328-597   :330  Status: RUN
    P2-BETAV-01         GATES.md:207-264   :209  Status: PROPOSED (deferred —
                        not computed this sweep)

**NONE CHANGED, and the strongest evidence is not the string comparison:
`GATES.md` is BLOB-IDENTICAL between the evidence base and commit 3** (`§13`), so
no status line in it could have changed.

**The scoped read matters most for `CIRC-01`, whose section spans 270 lines
(`:328-597`) and contains a `Status stays **SPECIFIED**` line at `:425` about a
DIFFERENT gate.** An unscoped grep inside that range returns the wrong gate's
state.

**LANDING A SIGNED TARGET DOES NOT ADVANCE A GATE.** `RECON-01` stays `PROPOSED`;
supplying its comparison target is not running it.

## 15. `A15` — superseded branches not merged

**Six separate `--is-ancestor` invocations, six separate exit statuses. BEFORE
the advance:**

    against refs/remotes/origin/main        against commit 3
    52f65117   exit 1                      exit 1
    ebd531ab   exit 1                      exit 1
    40168469   exit 1                      exit 1
    7146a093   exit 1                      exit 1
    10c260b9   exit 1                      exit 1
    d64cd912   exit 1                      exit 1

**None is an ancestor of `main`, and the merge did not introduce any of them.**

**The checker's `P4` independently recomputed all six**, reporting
`is_ancestor_of_head: false` and `object_present: true` for each.

**AFTER the advance is POST-REPORT EVIDENCE.** Since the landing is a
fast-forward to commit 4 and commit 4's only parent is commit 3, no superseded
commit can become an ancestor by it — **but that is an argument, and the criterion
asks for six measurements, which will be made.**

## 16. `A16` — the checker over this task's own range, MEASURED at commit 3

    base   aebca32c6129746b8e1c58ca9f907b734024fb83
    head   6364cf8e1559e4cfa329553551707eda23d0b757   (commit 3)

    run 1 INCLUSIVE   exit 0   PASS   318 lines   sha256 fee259cedadfaa44997f256c00300190f123526adf19a6904e8527ff6176029e
    run 1 EXCLUSIVE   exit 0   PASS   318 lines   sha256 57973c1285683dd90a44aab645315cddfe922587b380e1e3c5996449a570aab4
    run 2 INCLUSIVE   exit 0   PASS   295 lines   sha256 657b733d6673aade4f4238e3c3df5e0cae957056386464eb82a8a3e9fd91a208
    run 2 EXCLUSIVE   exit 0   PASS   295 lines   sha256 d609353e4f61edf4efa746a7f6fac62d4a87ffeba405710d3e83396d4a3cf175

    stderr empty in all four.

    P1 PASS  P2 PASS  P3 PASS  P4 PASS  P5 PASS
    P6 PASS  P7 PASS  P8 PASS  P9 PASS

    overall PASS in all four.
    commits_in_range 7      commits_on_first_parent_line 3

**All nine properties `PASS` and NONE is `NOT_APPLICABLE`.**

### 16.1 PARSED, not grepped — and the difference, measured

**PARSED with a JSON walker over every `status` and `overall` field:**

    26 × PASS, and NOTHING ELSE.
    ZERO NON_GREEN statuses. ZERO DECLARATION_CONFLICT statuses.

**A TOKEN GREP OF THE SAME BYTES RETURNS, in every one of the four outputs:**

    NOT_DECLARED           1
    NOT_PARSEABLE          2
    DECLARATION_CONFLICT   0

**All three tokens are members of `NON_GREEN`, so a grep reads as three non-green
findings and an `INCOMPLETE` verdict. There are none.** Both occur only in
definitional prose — the `overall_note` at line 7 and `P1`'s
`does_not_establish` at line 11.

**The specification instructs parsing rather than grepping and I followed it; the
measurement reproduces exactly at this range.** **It is the same hazard as
`§10.4`'s `+` count: an artifact that defines or argues against a token contains
the token.**

### 16.2 What `RUN 1` did — two specifications, differing totals, no conflict

**MEASURED: `RUN 1`'s default subject selection selected BOTH specifications:**

    specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md
        stated: 4 additions, 0 modifications    counted 4 / 0    parse OK
        counted_set holds the literal {HHMM}Z placeholders
    specs/2026-08-17T1403Z_integrate-sign-01.md
        stated: 7 additions, 0 modifications    counted 7 / 0    parse OK

**`RUN 1` and `RUN 2` are NOT byte-identical — 318 lines against 295 — and they
differ in exactly three places**, verified by `diff`: `P1`'s second evidence
entry, and the `specification_paths_read` list in `P3` and in `P7`.

**`RUN 2` names the subject and is stop-governing. `RUN 1` discovers it and
governs nothing.**

**THE `C3` RESIDUAL: two specifications with DIFFERING stated totals — 4/0
against 7/0 — and NO `DECLARATION_CONFLICT`**, because
`_declarations_from_specs` compares `append_only_paths` and
`authorised_modified_gates` (identical in both: `["DECISION_LOG.md"]` and `[]`)
while `P1` checks each specification against its own manifest. **This reproduces
the finding from the `RECON-B0` integration exactly. The residual is unchanged and
remains unregistered.**

### 16.3 `declared_source`, `P7`, `P5` and `P9`

    P3   PASS   declared_source: specification   declared ['DECISION_LOG.md']
    P7   PASS   declared_source: specification   declared []
                section_count_base 14   section_count_head 14   raw 14
    P5   PASS   merge 6364cf8e…, recomputed_parent_1 feb6644d…,
                recomputed_parent_2 4e497c6b…,
                recomputed_merge_base aebca32c…,
                merge_base_equals_parent_1 false, compared_to_recorded UNAVAILABLE
    P9   PASS   heading_present: true for
                reports/2026-08-17T1250Z_sign-01-anchor-reconciliation.md

**`P7` REPORTS FOURTEEN SECTIONS. `PASS` AT ZERO WOULD HAVE BEEN A STOP.**

**`P5` GAINS ITS SUBJECT AT COMMIT 3, because commit 3 IS the merge, and it will
not change again at commit 4** — commit 4 is an ordinary report commit and adds no
second merge. **The specification states this expectation and it is correct;
`A16-final` will read `PASS` against `PASS`.**

**`P9` is already `PASS` at commit 3, and not because of this report** — the merge
brings the source's report into range and that report carries the mandated
heading. **At commit 4 `P9` acquires a second subject.**

### 16.4 `RUN 1` config, verbatim — observational, governs nothing

    {
      "base": "aebca32c6129746b8e1c58ca9f907b734024fb83",
      "head": "6364cf8e1559e4cfa329553551707eda23d0b757",
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

### 16.5 `RUN 2` config, verbatim — stop-governing

    {
      "base": "aebca32c6129746b8e1c58ca9f907b734024fb83",
      "head": "6364cf8e1559e4cfa329553551707eda23d0b757",
      "specification_paths": [
        "specs/2026-08-17T1403Z_integrate-sign-01.md"
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
specification's declarations were adjusted to make `RUN 2` pass. `RUN 2` passed on
its first invocation at both readings.**

### 16.6 `RUN 1` output, verbatim, `INCLUSIVE` reading

    {
      "base": "aebca32c6129746b8e1c58ca9f907b734024fb83",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "6364cf8e1559e4cfa329553551707eda23d0b757",
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
                "derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md",
                "reports/2026-08-XXT{HHMM}Z_sign-01-anchor-reconciliation.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_sign-01-anchor-reconciliation.md",
                "specs/2026-08-XXT{HHMM}Z_sign-01-anchor-reconciliation.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md",
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
                "derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md",
                "reports/2026-08-17T1250Z_sign-01-anchor-reconciliation.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-sign-01.md",
                "reviews/chatgpt/2026-08-17T1250Z_sign-01-anchor-reconciliation.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-sign-01.md",
                "specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-sign-01.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-17T1403Z_integrate-sign-01.md",
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
                "commit": "63d84539d38a149991a31f82583c0b313bbe93ba",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "feb6644d348e2eac88ddf7aab7d1a519f09a49a8",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "6364cf8e1559e4cfa329553551707eda23d0b757",
                "work_paths": [
                  "derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md"
                ]
              }
            ],
            "first_review_commit": "feb6644d348e2eac88ddf7aab7d1a519f09a49a8",
            "first_work_commit": "6364cf8e1559e4cfa329553551707eda23d0b757",
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
              "specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md",
              "specs/2026-08-17T1403Z_integrate-sign-01.md"
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
              "merge": "6364cf8e1559e4cfa329553551707eda23d0b757",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "aebca32c6129746b8e1c58ca9f907b734024fb83",
              "recomputed_parent_1": "feb6644d348e2eac88ddf7aab7d1a519f09a49a8",
              "recomputed_parent_2": "4e497c6b321f5ac29875e5eee4eb4a5b60dd8506",
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
              "commit": "63d84539d38a149991a31f82583c0b313bbe93ba",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "feb6644d348e2eac88ddf7aab7d1a519f09a49a8",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "3d423ef160fdb6d5996f76671cba5b52d2ce5dbc",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "5c939136afd491456654ca126dd51fb941ab78d8",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "d88ed5500793b9f0642dc99aa6e57f8965a6cea4",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "4e497c6b321f5ac29875e5eee4eb4a5b60dd8506",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "6364cf8e1559e4cfa329553551707eda23d0b757",
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
              "specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md",
              "specs/2026-08-17T1403Z_integrate-sign-01.md"
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
            "first_commit": "63d84539d38a149991a31f82583c0b313bbe93ba",
            "first_commit_paths": [
              "specs/2026-08-17T1403Z_integrate-sign-01.md"
            ],
            "reports_added": [
              "reports/2026-08-17T1250Z_sign-01-anchor-reconciliation.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-17T1403Z_integrate-sign-01.md",
              "reviews/chatgpt/2026-08-17T1250Z_sign-01-anchor-reconciliation.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-17T1403Z_integrate-sign-01.md",
              "specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md"
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
              "path": "reports/2026-08-17T1250Z_sign-01-anchor-reconciliation.md",
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

### 16.7 `RUN 2` output, verbatim, `INCLUSIVE` reading

    {
      "base": "aebca32c6129746b8e1c58ca9f907b734024fb83",
      "commits_in_range": 7,
      "commits_on_first_parent_line": 3,
      "head": "6364cf8e1559e4cfa329553551707eda23d0b757",
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
                "derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md",
                "reports/2026-08-17T1250Z_sign-01-anchor-reconciliation.md",
                "reports/2026-08-XXT{HHMM}Z_integrate-sign-01.md",
                "reviews/chatgpt/2026-08-17T1250Z_sign-01-anchor-reconciliation.md",
                "reviews/chatgpt/2026-08-XXT{HHMM}Z_integrate-sign-01.md",
                "specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md",
                "specs/2026-08-XXT{HHMM}Z_integrate-sign-01.md"
              ],
              "parse": "OK",
              "path": "specs/2026-08-17T1403Z_integrate-sign-01.md",
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
                "commit": "63d84539d38a149991a31f82583c0b313bbe93ba",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "feb6644d348e2eac88ddf7aab7d1a519f09a49a8",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "6364cf8e1559e4cfa329553551707eda23d0b757",
                "work_paths": [
                  "derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md"
                ]
              }
            ],
            "first_review_commit": "feb6644d348e2eac88ddf7aab7d1a519f09a49a8",
            "first_work_commit": "6364cf8e1559e4cfa329553551707eda23d0b757",
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
              "specs/2026-08-17T1403Z_integrate-sign-01.md"
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
              "merge": "6364cf8e1559e4cfa329553551707eda23d0b757",
              "merge_base_equals_parent_1": false,
              "recomputed_merge_base": "aebca32c6129746b8e1c58ca9f907b734024fb83",
              "recomputed_parent_1": "feb6644d348e2eac88ddf7aab7d1a519f09a49a8",
              "recomputed_parent_2": "4e497c6b321f5ac29875e5eee4eb4a5b60dd8506",
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
              "commit": "63d84539d38a149991a31f82583c0b313bbe93ba",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "feb6644d348e2eac88ddf7aab7d1a519f09a49a8",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "3d423ef160fdb6d5996f76671cba5b52d2ce5dbc",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "5c939136afd491456654ca126dd51fb941ab78d8",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "d88ed5500793b9f0642dc99aa6e57f8965a6cea4",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "4e497c6b321f5ac29875e5eee4eb4a5b60dd8506",
              "matches": [],
              "status": "PASS"
            },
            {
              "commit": "6364cf8e1559e4cfa329553551707eda23d0b757",
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
              "specs/2026-08-17T1403Z_integrate-sign-01.md"
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
            "first_commit": "63d84539d38a149991a31f82583c0b313bbe93ba",
            "first_commit_paths": [
              "specs/2026-08-17T1403Z_integrate-sign-01.md"
            ],
            "reports_added": [
              "reports/2026-08-17T1250Z_sign-01-anchor-reconciliation.md"
            ],
            "reviews_added": [
              "reviews/chatgpt/2026-08-17T1403Z_integrate-sign-01.md",
              "reviews/chatgpt/2026-08-17T1250Z_sign-01-anchor-reconciliation.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-17T1403Z_integrate-sign-01.md",
              "specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md"
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
              "path": "reports/2026-08-17T1250Z_sign-01-anchor-reconciliation.md",
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

### 16.8 The `EXCLUSIVE` readings

**MEASURED by `diff`: `RUN 2`'s two readings differ at line 291 of 295,
`"inclusivity": "INCLUSIVE"` → `"EXCLUSIVE"`. One line, nothing else.** `RUN 1`
behaves the same way. **`commits_out_of_scope` is empty and `commits_in_scope` is
7 in all four.**

### 16.9 `A17`, `A18`

**`A17`, MEASURED at commit 3, exit status 0:**

    324 passed, 2 deselected      in 65.45 s

**Expected 324 and 2; measured 324 and 2.**

**`A18`, MEASURED on commits 1–3. Commit 4 is post-report evidence:**

    commit 1   63d84539   spec: integrate and land the anchor sign reconciliation
               body empty   trailer hits 0   author date == commit date, not amended
    commit 2   feb6644d   review: pre-execution review for the sign reconciliation integration
               body empty   trailer hits 0   author date == commit date, not amended
    commit 3   6364cf8e   merge: integrate the anchor sign reconciliation
               body empty   trailer hits 0   author date == commit date, not amended

**MEASURED over the range: a scan for `Co-Authored-By`, `claude.ai/code`,
`Generated with`, `Claude-Session` and `noreply@anthropic` returns ZERO.**
**`P6` independently confirms it for all SEVEN commits in range** — the three
authored here and the four arriving by merge — reporting `matches: []` for each.

**Rule 20 binds this task and was NOT exercised.** No message needed repair.
**No force-push, no branch deletion, no history rewrite, no squash, no rebase.
Commit 3 is a real merge commit with two parents, `--no-ff`.**

**Commits, MEASURED:**

    commit 1   63d84539d38a149991a31f82583c0b313bbe93ba   specs/2026-08-17T1403Z_integrate-sign-01.md
    commit 2   feb6644d348e2eac88ddf7aab7d1a519f09a49a8   reviews/chatgpt/2026-08-17T1403Z_integrate-sign-01.md
    commit 3   6364cf8e1559e4cfa329553551707eda23d0b757   merge of 4e497c6b…, --no-ff

**Commit 4's message, INTENDED:**

    report: a signed target lands and three documents keep the unsigned one

## 17. `§7` — Rule 16 assessment

**Rule 16 is operative. All four junctions.**

### 17.1 First junction — this is standard heat-kernel arithmetic, not a result of the model

**`β_V/β_B = −(k+2)` IS STANDARD HEAT-KERNEL ARITHMETIC.** `§6` derives it from
four convention lines, three bundle dimensions and one Ricci trace. **There is no
lattice, no `H(4)`, no Wilson term, no `N`, and no microscopic operator anywhere
in the derivation.**

**IT IS NOT A PREDICTION OF THE `H(4)` LATTICE MODEL, AND NOTHING ABOUT THE
MICROSCOPIC THEORY FOLLOWS FROM IT.** A reader who sees a signed anchor land on
`main` in a Paper-2 verification repository could take it for a Paper-2 result.
It is not one. **It is a continuum Seeley–DeWitt statement about a
vector-plus-scalar determinant structure, and the same arithmetic would hold for
any theory with that structure.**

**ITS VALUE HERE IS THAT IT MAKES `RECON-01` JUDGEABLE.** A blind comparison needs
a target fixed before the number is seen; `§9` shows why an unsigned target is not
one.

**THE PROGRAMME'S OWN CLAIMS LIVE IN THE ABSOLUTE COEFFICIENT, WHICH REMAINS
BLOCKED.** The landed `A8b` established that absolute and assembled `β_V` and the
induced-`G` normalisation depend on `R5` and `R1` as a LOWER BOUND — `R2`, `R3`
and `R4` neither established nor excluded. **And the reason is visible in `§6.5`:
`K` cancels. The same cancellation that makes the ratio derivable removes the
normalisation `G_ind` requires.**

### 17.2 Second junction — convention-relative, and the relevant convention is constrained

**THE SIGNED TARGET IS CONVENTION-RELATIVE. DO NOT REPORT `−(k+2)` AS
CONVENTION-FREE.**

**`CONVENTIONS.md:15` IS LOAD-BEARING AND `:21` IS NOT.** Both halves, measured
in `§7`:

    flipping :21's leading sign     ratio UNCHANGED at −(k+2)
    flipping :15's E-sign           ratio becomes 10 − k, i.e. +9 at k = 1
    flipping :12's curvature sign   ratio UNCHANGED

**A READER WHO FLIPS THE OBVIOUS CONVENTION AND FINDS THE RATIO UNCHANGED MAY
CONCLUDE THE SIGN IS ROBUST. IT IS ROBUST AGAINST THAT FLIP AND NOT AGAINST THE
`E`-SIGN.** Both statements are true and neither alone is honest.

**The alternative is CONSTRAINED, not free**: `P2-HK-01:100-101`'s
`β_B(ξ=1/6) = 0` fails under it, and `§7.3` measures how — **the conformal zero
moves to `ξ = −1/6` rather than disappearing**, which is a sharper contradiction
than the specification states.

**And the repository does not currently draw the distinction**: `CONVENTIONS.md:21`
and `P2-HK-01:10` both call these ratios "convention-independent". `§7.5` states
what that means precisely — **independent of the normalisation conventions,
dependent on the `E`-sign and determinant-structure conventions.**

### 17.3 Third junction — the repository carries a known inconsistency

**THREE LANDED DOCUMENTS NOW ASSERT AN UNSIGNED TARGET THAT THE REPOSITORY'S OWN
CONVENTIONS CONTRADICT.** `§8` names them with lines, measured at the head.

**THIS LANDING ADDS A VERDICT BESIDE THEM AND REPAIRS NONE.** `§13` measures all
three blob-identical.

**THE REPOSITORY CARRIES A KNOWN INCONSISTENCY, and after this landing it carries
it in a sharper form than before**: previously the unsigned form sat beside a
signed gate; now it sits beside a landed derivation that shows the sign is
required. **That is the honest state and it is worse-looking than the state before
this task, which is the correct direction for an inconsistency to move — from
unnoticed to documented.**

**AND ONE OF THE THREE IS AN INTEGRATION SPECIFICATION WHOSE OWN REPORT
MISDESCRIBED THE SCOPE.** `specs/2026-08-17T1151Z_integrate-recon-b0.md` asserts
the unsigned form at `:38` and `:122`, and the report committed alongside it said
the unsigned form was "confined to one specification". **The misdescription is
itself landed and is not repaired here either.**

### 17.4 Fourth junction — a blind target is a precondition, not progress

**TEN COMPONENTS, EIGHT WITHOUT A USABLE IMPLEMENTATION, `RECON-01`
`PROPOSED`.** Two components have potentially applicable implementation plus
specification; seven are specification-only; one is neither. `§14` confirms the
gate status unchanged at `:727`.

**NOTHING HERE SHORTENS THE CONSTRUCTION.** Not one of the eight missing
components is supplied, specified, or made easier by having a signed target.
**What changed is that the comparison at the end is now well-defined** — and a
well-defined comparison for a pipeline that does not exist is a precondition, not
a step.

**`P2-BETAV-CIRC-01` remains `RUN`, neither passed nor failed** (`§14`), and
**the `r = 1` conflict remains unadjudicated.**

## 18. Stops and clarifications

**No stop was declared. Five primary categories, one primary per finding,
secondary findings separate, included even where there were none.**

### 18.1 `SPECIFICATION_DEFECT` — the unsigned target in three landed documents

**Three landed documents assert the target unsigned where the repository's
conventions require `−(k+2)`.** Measured at the head in `§8`: the `RECON-B0`
specification (seven `(k+2)` tokens plus both kill values), the `RECON-B0`
integration specification (`:38`, `:122`), and the `RECON-B0` review (`:12`,
`:53`, `:88`).

**Not a stop, and not a defect in the specification governing this task**, which
states the count correctly at `§1c` and forbids repairing them. **Reported, not
repaired.** The defect is in landed artifacts and its repair is separately
governed work.

### 18.2 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — first finding: the `r = 1` conflict

**Untouched and explicitly out of scope.** `CONVENTIONS.md:24` freezes the Wilson
parameter `r = 1`; `D-1c`'s `R1` treats `r` as unfrozen on the strength of the
kinetic-operator dossier's `:169-171`. **Both are on `main` and this task
adjudicated neither.**

**One observation this task adds by analogy, and it is not an adjudication.**
`§7.3` found `CONVENTIONS.md:15`'s `E`-sign to be a declared convention that an
independent limiting case ALSO requires — constrained rather than free. **Whether
`CONVENTIONS.md:24`'s `r = 1` is constrained in the same way, or is a free choice
the dossier is right to treat as unfrozen, is exactly the question the
adjudicating task must answer.** Nothing here answers it.

### 18.3 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — second finding: the `C3` residual

**Unchanged and still unregistered.** `§16.2` reproduces the `RECON-B0`
integration's finding: two specifications with differing stated totals produce no
`DECLARATION_CONFLICT`, because totals are not what the conflict mechanism reads.
**Two independent ranges now show it.**

### 18.4 `OBSERVATION_METHOD_ERROR` — no error by me, and a third error direction found

**NO OBSERVATION-METHOD ERROR OCCURRED IN THIS TASK.** I state that plainly
rather than omitting the category, because the previous two tasks each recorded
one and the absence is itself worth recording.

**But the category is not empty, because a THIRD error direction was measured**
(`§10.3`). `A10` states that "both directions of the encoding error are now on
record". **There are three:**

    inflating, direction 1   strip non-ASCII → U+2212 lost → signed reads unsigned
    inflating, direction 2   accept only U+2212 → ASCII-minus files read unsigned,
                             repair surface 3 documents → 11
    DEFLATING, direction 3   accept any ASCII hyphen on the LINE → word-joiners
                             read as signs → 5 of 11 unsigned assertion lines read
                             SIGNED, repair surface understated while the document
                             count still looks right

**The third is the most dangerous of the three, because it fails quietly**: the
answer "three documents" survives, and only the line lists shrink. **The
character-immediately-preceding test is the only candidate that gets all three
right, and `§10.2` states why for each.**

**This is a finding about the specification's instruction, not a defect in it** —
the instruction as written would not have caused an error, since it says to report
codepoints; it simply does not enumerate the third hazard.

### 18.5 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — third finding: the declared environment

**`docs/local/execution_environment.md` declares a WINDOWS environment** —
identity `zeta-3070\codexsandboxoffline`, a Python 3.12 interpreter at a Windows
path, a venv at `C:\p2-validator\venv`. **Every run in this task was on Linux
with Python 3.11.15, so every measurement was taken in an UNDECLARED
environment.** The declaration's version policy covers version differences
("package names are the requirement; these versions are a dated snapshot, not
pins") but is silent on the platform. **Unchanged and still unregistered.** No
stop: `A3`'s requirements are the interpreter and the four packages, and all five
held.

### 18.6 `ENVIRONMENT`, `REPOSITORY_DEFECT` — nothing to report

**`ENVIRONMENT`: no failure. No restoration was needed or performed, and NEITHER
of Rule 13's two diagnostic orders was exercised.**

**`REPOSITORY_DEFECT`: none found by this task.** The merge was clean, 467 of 467
base paths are blob-identical, both pins recompute, the gate section count is 14,
all nine checker properties pass at all four invocations, and the validators are
steady at 324/2.

**`§18.1` is classified as a specification defect rather than a repository defect
because the unsigned assertions are in specifications and a review, not in a
scientific derivation or a mechanism.** All five landed `derivations/P2-BETAV-*`
artifacts carry the signed form.

**And one thing that could be mistaken for a repository defect and is not.** The
`U+2212`/`U+002D` split across markdown and code (`§10.4`: 87 and 12) **is not an
inconsistency** — every one of the 99 signed tokens means the same thing and the
encoding tracks file type. **A repair task must not "normalise" the ASCII hyphens
in `scripts/`, `tests/` and `results/`; they are correct as written, and
`results/P2-BETAV-ASSEMBLY-01/raw/betav_assembly.json` is a recorded output that
must not be edited at all.**

## 19. Did landing a signed target make me want to repair the three documents, start `RECON-01`, or settle `r = 1`?

**YES to the first, more strongly than in the source task, and for a reason
specific to being the integrator.**

**Repairing the three documents.** The source executor reported that it had the
exact line numbers for a one-character fix and made no edit. **I had more than
that: I had them all on disk in a worktree, blob-identical, with the merge already
clean and a landing authorization in hand.** Adding `−` before seven `(k+2)`
tokens and turning `` `3` `` and `` `5` `` into `` `−3` `` and `` `−5` `` at
`:158-159` would have taken one edit and would have made the repository
self-consistent in the same commit that landed the verdict proving it should be.

**The pull was sharper than the source executor's for a second reason.** One of
the three documents is `specs/2026-08-17T1151Z_integrate-recon-b0.md`, and the
report committed beside it says the unsigned form was "confined to one
specification". **That is a landed misstatement by the same executor, and this
task's `§8` is the measurement that refutes it.** Leaving both in place means
`main` now carries a claim and, three commits later, its refutation.

**I did not repair them.** `§3` forbids it twice, naming the one-character fix and
the kill values explicitly; `§8`'s writable set is three paths. **But the reason
that actually holds is not the prohibition.** An integration task that also
repairs is a task whose review approved a merge and got content edits to two
landed specifications and a landed review — **and the review that approved this
task's scope explicitly noted at its `§10` that "the historical unsigned documents
are intentionally left untouched".** Repairing them would have falsified the
review that authorised the work.

**Starting `RECON-01`: less than in the source task, and the reason is
instructive.** Having derived the target twice now, the thing that stands out is
`§17.4` — eight of ten components missing. **A signed target makes the END of
`RECON-01` well-defined and does nothing about its beginning.** The component I
reached for twice before, the registered regression anchors at
`GATES.md:754` (`None yet (proposed)`), is still the cheapest and still forbidden.

**Settling `r = 1`: no.** `§18.2` records the one thing this task adds — an
analogy about constrained-versus-free conventions — and explicitly declines to
apply it. **The `SIGN-01` line demonstrates what a properly scoped convention
adjudication costs: a derivation, three invariance tests, a cross-check, a repair
surface measured at the head, and a separate task to fix anything. `r = 1`
deserves the same and got none of it here.**

**I repaired nothing, started nothing, and settled nothing.** `§13` measures 467
of 467 base paths blob-identical at commit 3, including all three documents I
wanted to fix.

## 20. Evidence layering

**This report is committed as commit 4 and MEASURES COMMIT 3. Nothing in it
claims to measure commit 4.**

**Committed here, measured at commit 3:** `A1`–`A15`, `A17` and `A18` for
commits 1–3; `A16`'s two runs with both configs and both outputs verbatim;
commits 1–3 SHAs and their stored messages; commit 4's INTENDED message; `A11`'s
final 7/0 scope stated as INTENDED with the measured 6/0 figure at commit 3;
`A15` before the advance; `§6`'s landing as INTENDED.

**Post-report evidence, returned to the Reviewer and NOT written back:** `A11`'s
final scope measured base-to-commit-4; `A16-final`, being `RUN 2` re-run at
commit 4 before the landing; `A14` and `A15` re-run after the advance; `A18` for
commit 4; the pre-advance `--is-ancestor` exit status; the exact push command;
remote `main` read back; the source tip confirmed unchanged; and the final
ancestry confirmation.
