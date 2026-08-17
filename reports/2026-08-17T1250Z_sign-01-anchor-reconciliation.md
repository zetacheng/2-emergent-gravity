# Report — `SIGN-01`: reconciling the `β_V/β_B` anchor sign

    branch      science/sign-01-anchor-reconciliation
    base        aebca32c6129746b8e1c58ca9f907b734024fb83   (authoritative main)
    measured at commit 3, d88ed5500793b9f0642dc99aa6e57f8965a6cea4
    main        NOT TOUCHED. No merge. Integration is a separate task.

**NOTHING WAS COMPUTED NUMERICALLY AND NOTHING WAS BUILT. No script was
executed. No document was corrected.**

**VERDICT: `SIGNED NEGATIVE`.** The repository's frozen conventions require
`β_V/β_B = −(k+2)`, hence `−3` at `k = 1`. **It was DERIVED from
`CONVENTIONS.md:15`, `:16`, `:19` and `:21`, not quoted from `P2-HK-01`'s stated
`−3`.**

**THREE documents are left inconsistent with the verdict, not one.** The
`RECON-B0` specification, the `RECON-B0` INTEGRATION specification, and the
`RECON-B0` pre-execution review. **None was repaired.**

---

## 1. `A3` — environment conformance, run FIRST

**Rule 13's diagnostic order with Amendment D's step 0, run before any other
criterion. MEASURED, not assumed.**

    (0) execution location    /home/user/2-emergent-gravity — the primary
        (Amendment D)         worktree. git dir .git, common dir .git, so not a
                              linked worktree. HEAD branch
                              claude/paper-2-independent-verification-dysdp0,
                              resolved bfef924c368658cac85c04ed18d96eb4450afba6.
                              Nine linked worktrees existed; this task's work was
                              done in a TENTH, cut fresh at
                              refs/remotes/origin/main.

    (1) interpreter           Python 3.11.15 at /usr/local/bin/python3

    (2) declared packages     MEASURED: pytest 9.1.1, numpy 2.4.6,
                              sympy 1.14.0, ruff 0.15.8 — all four declared
                              packages present.

    (3) clone depth           NOT shallow. `--is-shallow-repository` returns
                              false and no `shallow` file exists in the common
                              git dir. 493 commits reachable from all refs,
                              423 from HEAD.

    (4) working tree          clean; `status --porcelain` empty before any work.

    (5) declaration compared  `docs/local/execution_environment.md` declares a
                              WINDOWS environment. See `§14.4`.

**NO RESTORATION WAS NEEDED AND NONE WAS PERFORMED. No repository content was
touched by `A3`.**

**Rule 13 carries TWO diagnostic orders, a known open item. No environment
failure occurred, so NEITHER order was exercised** — this is a conformance
report, and naming one of the two would misrepresent which was followed.

**`sympy 1.14.0` matters to this task specifically**, because `§5` of the
artifact re-checks the sign algebra symbolically. It is a declared package and it
was present.

## 2. `A1` — repository, refs, branch availability

**`origin` URL, MEASURED and reported VERBATIM, not normalised:**

    https://github.com/zetacheng/2-emergent-gravity

No `.git` suffix, no trailing slash. It identifies `zetacheng/2-emergent-gravity`.

**Refs, MEASURED after `git fetch origin main`:**

    refs/remotes/origin/main   aebca32c6129746b8e1c58ca9f907b734024fb83
    expected by §5 A1          aebca32c6129746b8e1c58ca9f907b734024fb83   MATCH

    refs/heads/main            1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab

**`refs/heads/main` LAGS and is reported for contrast, which the criterion
states is not a stop.** It has lagged at `1cb5550f…` throughout this session's
tasks. Every measurement here is against `refs/remotes/origin/main`.

**BRANCH AVAILABILITY — the criterion says STOP if it already exists:**

    science/sign-01-anchor-reconciliation   remote hits 0   local hits 0
    IT DID NOT EXIST. No stop. This task created it.

## 3. `A2` — the pre-execution review

**Field-present check run BEFORE the match check, in that order:**

    field name present     grep 'reviewed specification SHA-256' → line 4, ONE hit
    field filled in        yes — a 64-hex value, not a placeholder
    value in the review    d869c956b37f12b077592243a5fe22a08e281067bd25b85ac313421129535387
    sha256 of the spec     d869c956b37f12b077592243a5fe22a08e281067bd25b85ac313421129535387
                           MATCH

**Committed UNEDITED**: the committed blob's sha256 is
`de6d2b07743debc47fb4518c3481878c25244111ffdf96e216bb59ca0d68bbcf`, identical to
the uploaded bytes. **Verdict `APPROVE FOR EXECUTION`, fourteen sections all
`PASS`.**

## 4. `A4` — the four statements, quoted with sign codepoints

**Read as bytes. Codepoints enumerated per line rather than displaying filtered
text.**

### 4.1 `GATES.md`

    :751   `β_V/β_B = −(k+2)` (from `P2-HK-01`), compared only at the end.
           sign character: U+2212 MINUS SIGN
    :731   tracks `β_V/β_B = −(k+2)`. **Scope label: a 2026 reconstructed
           pipeline, NOT a …                     U+2212 MINUS SIGN
    :757   For the reconstruction itself: stuck at `−3` ∀k ⟹ the new pipeline
           is degenerate                         U+2212 MINUS SIGN
    :758   (a bug); drift toward `−5` at heavy mass ⟹ longitudinal artifact.
                                                 U+2212 MINUS SIGN
    :228   `β_V/β_B=−3` (from `P2-HK-01`).       U+2212 MINUS SIGN

**All sixteen `β_V/β_B` occurrences in `GATES.md` were read and classified.
MEASURED: `10 + 2 + 4 = 16`.**

    U+2212 MINUS SIGN present   10   :56 :228 :347 :426 :441 :449 :537 :620
                                     :731 :751
    ASCII hyphen, GATE HEADING   2   :207 `## P2-BETAV-01 — Lattice β_V/β_B …`
                                     :598 `## P2-BETAV-NUMREPRO-01 — …`
                                     — the hyphen is part of a gate NAME, not a
                                     sign
    no sign character            4   :19 :212 :531 :645 — each names the ratio
                                     without asserting a value

**NO OCCURRENCE ANYWHERE IN `GATES.md` ASSERTS A POSITIVE VALUE.** Five of the
ten signed ones (`:347`, `:426`, `:441`, `:449`, `:620`) attach the minus to
LATTICE or quarantined figures — `−3.2(5)`, `≈ −2.23` — rather than to the
analytic anchor; **they are consistent with the verdict but are not evidence for
it**, and `§9` explains why none of the sixteen is evidence for it.

### 4.2 `derivations/P2-HK-01_heat_kernel_species.md`

    :95    β_V/β_B    = (K/4)/(−K/12)   = −3
           sign character: U+2212 MINUS SIGN, twice
    :102   - `β_V/β_B = −3` reproduces the analytic value the paper quotes for
           the Proca ratio (recorded here as a pre-registered prediction,
           **not** as a target).            U+2212 MINUS SIGN
    :10    convention-independent ratios `β_F/β_B`, `β_V/β_B`, `β_B(ξ)/β_B`.
           no sign character — names the ratios, asserts no value

### 4.3 `derivations/betav_discriminating_power.md`

    :44    β_V(k)/β_B = −(k + 2)     [ k=1 → −3 ; k=0 → −2 ; k=2 → −4 ; k=3 → −5 ].
           U+2212 MINUS SIGN on the general form and on all four tabulated values
    :8     Paper 2 Finding 5 reports `β_V/β_B|_lat = −3.2(5)` against analytic `−3`
           U+2212 MINUS SIGN
    :60    - **Settled (analytic layer):** the `β_V/β_B` target is not a constant
           `−3`; it …                       U+2212 MINUS SIGN

### 4.4 The `RECON-B0` assessment, `derivations/P2-BETAV-RECON-01_scope-assessment.md`

    :340   #### `A8a` — does the RATIO `β_V/β_B = −(k+2)` depend on any of `R1`–`R5`?
           U+2212 MINUS SIGN
    :29    Analytic anchors    (:751)   `β_V/β_B = −(k+2)` (from `P2-HK-01`) …
           U+2212 MINUS SIGN
    :48    anchor as `−(k+2)` and the kill criteria as `−3` and `−5`. **The
           specification …                  U+2212 MINUS SIGN
    :49    governing this assessment writes them unsigned** — `(k+2)`, `3`, `5`.
           NO sign character — and this is a QUOTATION of the specification's
           defect, not an assertion by the assessment

**THE ASSESSMENT IS SIGNED THROUGHOUT AND FLAGS THE UNSIGNED SPECIFICATION
ITSELF. It is not among the inconsistent documents.**

### 4.5 `CONVENTIONS.md:21`, in full

    | Species coefficient `β_s` | Coefficient of `m² ln m²` in `Z(m²)`. Computed
    from `a_1`: `β_s = −p_s (4π)^{−2} (tr a_1 / R)`, where `p_s` is the log-det
    prefactor of the species (`+1/2` per bosonic `det^{−1/2}` factor, `−1/2` per
    `det^{+1/2}` factor / fermion loop). Reported both as a raw value (this
    convention) and as convention-independent ratios `β_F/β_B`, `β_V/β_B`,
    `β_B(ξ)/β_B`. |

**The leading `−` on `p_s` is `U+2212` and is part of the definition.**

## 5. `A5` — the ratio DERIVED from the conventions

**Three ingredients separately, then the ratio. Derived, not quoted.**

### 5.1 Ingredient (i) — the sign convention in `β_s`'s own definition

**`CONVENTIONS.md:21` carries a LEADING MINUS on `p_s`:
`β_s = −p_s (4π)^{−2} (tr a_1 / R)`.** Writing `K ≡ (4π)^{−2}`, **`K > 0`**, so
`K` carries no sign and cancels from any ratio. **The definition contributes ONE
sign flip, applied identically to every species.**

### 5.2 Ingredient (ii) — `p_V` and `p_B` with their determinant factors

    β_B                det^{−1/2}(Δ^{(0)}+m²)   bosonic     p_B = +1/2
    Proca, vector      det^{−1/2}(Δ^{(1)}+m²)   bosonic     p   = +1/2
    Proca, Stueckel.   det^{+1/2}(Δ^{(0)}+m²)   det^{+1/2}  p   = −1/2

**`p_V` IS NOT A SINGLE NUMBER.** `CONVENTIONS.md:19` gives the Proca species as
a PRODUCT of two determinant factors with OPPOSITE powers, so it contributes two
terms with opposite prefactors. **That structural fact is what the whole sign
turns on**, and treating `p_V` as one prefactor is implicitly what an unsigned
reading of the anchor does.

### 5.3 Ingredient (iii) — the sign of `tr a_1 / R` for each species

**From `CONVENTIONS.md:16`, `a_1 = tr[(1/6)R·𝟙 − E]`; with `d = tr 𝟙` and
`e ≡ tr E/R`, `tr a_1/R = d/6 − e`. `E` enters `a_1` with a MINUS while
`CONVENTIONS.md:15` fixes `E` entering `Δ` with a PLUS. Both frozen, both
load-bearing.**

    minimal real scalar (β_B)   d = 1   E = 0        e = 0
                                tr a_1/R = 1/6 − 0 = +1/6      POSITIVE
    Proca vector part           d = 4   E^μ_ν = R^μ_ν
                                tr E = R^μ_μ = R  ⟹  e = 1
                                tr a_1/R = 4/6 − 1 = −1/3      NEGATIVE
    Stueckelberg scalar         d = 1   E = 0        e = 0
                                tr a_1/R = 1/6 − 0 = +1/6      POSITIVE

**`d = 4` is the 1-form bundle dimension in `d = 4`; `tr E = R^μ_μ = R` is the
Ricci-endomorphism trace, making `e = 1` exactly and `4/6 − 1` NEGATIVE. THAT
SINGLE NEGATIVE IS WHERE THE RATIO'S MINUS SIGN IS BORN.**

### 5.4 The two coefficients, and the ratio

    β_B          = −(+1/2)·K·(+1/6)  = −K/12    NEGATIVE
                   one flip (definition), none from tr a_1/R
    β_V, vector  = −(+1/2)·K·(−1/3)  = +K/6     POSITIVE
                   two flips — definition and tr a_1/R — cancel
    β_V, Stueck. = −(−1/2)·K·(+1/6)  = +K/12    POSITIVE
                   two flips — definition and p_s — cancel
    β_V (k=1)    = +K/6 + K/12       = +K/4     POSITIVE

    β_V/β_B = (+K/4)/(−K/12) = −3               SIGNED NEGATIVE

**`β_B` is NEGATIVE and `β_V` is POSITIVE: the minus is a genuine sign REVERSAL
between two species, not an overall convention.** **Both of `β_V`'s terms come
out positive for DIFFERENT reasons — a negative bundle trace, and a negative
determinant power — so they ADD.** A derivation assigning the Stueckelberg factor
`p = +1/2` would have obtained `+K/12` and a ratio of `−1`.

**DERIVED, NOT QUOTED.** `P2-HK-01:95`'s stated `−3` was not an input; the
agreement is reported in `§7` as a cross-check.

## 6. `A6` — the general-`k` form, and the two signed kill values

**WHERE `(k+2)` IS DERIVED: `derivations/betav_discriminating_power.md:34-50`.**
It generalises `CONVENTIONS.md:19`'s structure at its `:37` to
`det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)^k`, so the Stueckelberg factor is
`det^{+k/2}` and `CONVENTIONS.md:21`'s rule gives `p = −k/2`.

**DOES THAT DERIVATION USE `CONVENTIONS.md:21`'S SIGN RULE? YES, EXPLICITLY.**
`:41` attributes the recipe to "the `a_1` recipe (P2-HK-01 conventions)", and
`:47-49` reproduces the rule term by term: *"vector factor contributes
`−p·K·(tr a_1/R) = −(½)K(−1/3)=+K/6`; scalar`^k` factor `det^{+k/2}` has
`p=−k/2`, contributing `+kK/12`; `β_V(k)=K(2+k)/12`, and `β_B=−K/12`."*

**IS THE SIGN PRESERVED AT GENERAL `k`, OR ONLY STATED AT `k=1`? PRESERVED, AND
DERIVED UNIFORMLY IN `k`.** Re-derived independently:

    β_V(k)      = −(+1/2)·K·(−1/3) + −(−k/2)·K·(+1/6)
                = +K/6 + kK/12 = K(2+k)/12
    β_V(k)/β_B  = [K(k+2)/12]/(−K/12) = −(k+2)

    k = 0  −2      k = 1  −3      k = 2  −4      k = 3  −5      k = ½  −5/2

**`k` enters ONLY through the Stueckelberg prefactor `p = −k/2`, linearly and
sign-preservingly. `β_B` carries no `k` at all, so no `k`-dependent sign flip is
available anywhere in the ratio.** **`k=1` is a substitution into the general
result, not a special case from which the general form was extrapolated.**

### 6.1 THE TWO KILL VALUES UNDER THIS VERDICT

    stuck at degenerate     STUCK AT −3 for all k
    heavy-mass drift        DRIFT TOWARD −5 at heavy mass

**BOTH ARE NEGATIVE AND THE SIGN IS PART OF EACH TEST.** `−5` is exactly the
`k=3` value, which `betav_discriminating_power.md:74-76` notes as *"suggesting
the artifact mimics an extra compensating power"* — **so the second criterion is
not an arbitrary threshold but a recognisable structural signature, and it is
recognisable only with the sign attached.**

**A pipeline sitting at `+3` satisfies NEITHER criterion as written while plainly
being wrong.** That is the hole the unsigned form leaves open, and closing it is
what this task delivers.

## 7. `A7` — the verdict

**`SIGNED NEGATIVE`. The conventions require `−(k+2)`, hence `−3` at `k=1`. The
unsigned form in the `RECON-B0` specification is an error and is recorded as
one.**

**The derivation is `§5` and `§6`.** Four independent cross-checks agree and none
was an input:

    P2-HK-01:95                       −3, with the same intermediates K/4 and −K/12
    betav_discriminating_power.md:44  −(k+2) and the table k=0→−2 … k=3→−5
    results/P2-BETAV-ASSEMBLY-01/
      README.md:11                    k=½ → −5/2 — agreement at a NON-INTEGER k,
                                      which the k=1 statement alone could not supply
    P2-HK-01:100-101                  β_B(ξ=1/6) = 0, which independently constrains
                                      the E-sign convention §8.3 identifies as the
                                      load-bearing one

**Had any of the four disagreed, the verdict would have been `NOT DETERMINABLE`
pending reconciliation of the disagreement.**

### 7.1 Documents now inconsistent with the verdict — NAMED, NOT CORRECTED

**THREE, not one.** Full listing in the artifact's `§6.1`.

    1. specs/2026-08-17T1105Z_recon-b0-scope.md          the RECON-B0 specification
       :60, :64, :113, :117, :226, :374, :384   seven unsigned assertions of (k+2)
       :158, :159                               both kill values unsigned as `3`, `5`
       NO sign character on any of the nine lines

    2. specs/2026-08-17T1151Z_integrate-recon-b0.md      the INTEGRATION specification
       :38    A8a   the RATIO β_V/β_B = (k+2)          depends on NONE of R1–R5
       :122   future reconstruction returning `(k+2)` would show the reconstruction

    3. reviews/chatgpt/2026-08-17T1105Z_recon-b0-scope.md   the RECON-B0 review
       :12    … separation of the `(k+2)` ratio anchor from absolute/assembled beta_V …
       :53    … does not by itself force the clean-room `(k+2)` reconstruction …
       :88    A future successful reconstruction of `(k+2)` would not vindicate …

**THE SPECIFICATION'S §1 NAMES ONLY "the `RECON-B0` spec". THE REPAIR SCOPE IS
THREE DOCUMENTS.** See `§14.1`.

**I CORRECTED NONE OF THEM.** `§11` measures 467 of 467 base paths
blob-identical.

## 8. `§7` — Rule 16 assessment

**Rule 16 is operative. All four junctions.**

### 8.1 First junction — a sign verdict corrects nothing

**WHICHEVER WAY THIS WENT, AT LEAST ONE LANDED DOCUMENT WOULD BE LEFT
INCONSISTENT.** Under `SIGNED NEGATIVE` it is three documents. **Under `SIGNED
POSITIVE` it would have been sixty-six signed tokens' worth** — `GATES.md`,
`P2-HK-01`, `betav_discriminating_power.md`, the `RECON-B0` assessment, four
other `derivations/P2-BETAV-*` artifacts, `CLAIMS.md`, `PROGRESS.md`,
`MIGRATION.md`, `DECISION_LOG.md`, three scripts, a test, and two `results/`
records.

**THIS TASK LISTS THEM AND REPAIRS NONE.**

**THE REPOSITORY WILL CARRY A KNOWN INCONSISTENCY UNTIL A REPAIR TASK LANDS.**
That is deliberate: **landing a verdict and landing a correction are different
acts**, and conflating them would put an unreviewed edit to a landed
specification inside a task whose review approved only a verdict.

### 8.2 Second junction — this unblocks pre-registration and nothing else

**`RECON-01` now has a BLIND TARGET, `−(k+2)`, with signed kill criteria `−3`
and `−5`. THAT IS A PRECONDITION FOR STARTING, NOT A STEP TOWARD FINISHING.**

**TEN COMPONENTS REMAIN, EIGHT WITHOUT A USABLE IMPLEMENTATION** — seven
specification-only and one neither, per the landed `RECON-B0` inventory.
**Nothing here reduces that by one. A pre-registerable target is a document, not
a pipeline.**

**`P2-BETAV-CIRC-01` remains `RUN`, neither passed nor failed** (`§12`), and
nothing here judges whether the historical Finding 5 is circular.

### 8.3 Third junction — is `CONVENTIONS.md:21` a convention or a derivation?

**IT IS REGISTERED AS A CONVENTION AND ITS CONTENT IS DERIVED ELSEWHERE.**

**Registered as a convention:** a row in the table under
`## Locked conventions for the independent-verification sweep` (`CONVENTIONS.md:8`),
in a file whose `:3` reads *"No calculation may begin until every relevant
convention below is filled, reviewed, and locked"*. **Its own text calls itself
one** — *"Reported both as a raw value (this convention) …"*.

**Derived elsewhere:** `P2-HK-01:23-51` obtains the same relation from
`W = p·Tr ln(Δ+m²)` via `ln(Δ+m²) = −∫₀^∞ (dτ/τ) e^{−τ(Δ+m²)}` at `:27` and the
proper-time integral whose `m² ln m²` coefficient it computes as exactly `+1` at
`:45-47`, arriving at `β_s = −p_s (4π)^{−2}(tr a_1/R)` at `:50`.

**WHAT FOLLOWS — AND IT IS NOT WHAT THE JUNCTION ANTICIPATES.** The junction asks
whether a different convention would give a different signed target with no
physics changing. **For `CONVENTIONS.md:21` the answer is NO. The ratio is
INVARIANT under flipping its leading sign**, because the flip applies to
numerator and denominator alike:

    under β_s = +p_s K (tr a_1/R):   β_B = +K/12   β_V(k) = −K(k+2)/12
                                     ratio = −(k+2)      UNCHANGED

**So the verdict does not rest on `:21` being right about its own sign.**

**The convention that DOES carry the sign is `CONVENTIONS.md:15`'s
`E`-enters-with-a-plus:**

    under a_1 = tr[(1/6)R·𝟙 + E]:    vector tr a_1/R = 4/6 + 1 = +5/3
                                     ratio = 10 − k,  i.e. +9 at k = 1
                                     CHANGED

**That one is a declared choice — but it is NOT FREE.** `CONVENTIONS.md:15` gives
its reason (*"`E` enters with a `+` so that a scalar curvature coupling `ξR`
appears inside `E` as `E ⊃ +ξR`"*), and `P2-HK-01:100-101`'s conformal check
`β_B(ξ=1/6) = 0` fails under the alternative: `β_B(ξ)` would read
`−(1/2)K(1/6 + ξ)`, which has no zero at `ξ = +1/6`.

**A third flip changes nothing: the curvature sign convention at
`CONVENTIONS.md:12`.** `e ≡ tr E/R` is a ratio to `R`, so under `R → −R` every
`e` is unchanged and so is `tr a_1/R`.

**SO: the signed target is CONVENTION-RELATIVE, and the relevant convention is
CONSTRAINED rather than arbitrary. IT IS NOT AN ADDITIONAL CONVENTION-INDEPENDENT
PHYSICAL PREDICTION and must not be reported as one.**

**A finer point than either document draws.** `CONVENTIONS.md:21` and
`P2-HK-01:10` both call the ratios "convention-independent". **`§5` and this
junction make that precise: they are independent of the NORMALISATION conventions
— the leading sign, `K`, the `4N` divisor, the curvature sign — and DEPENDENT on
the `E`-sign convention and the determinant-structure convention.** Neither
document distinguishes those two families.

### 8.4 Fourth junction — nothing here touches the absolute `β_V` or `G_ind`

**A SIGNED RATIO TARGET DOES NOT MAKE THE ABSOLUTE QUANTITY ASSEMBLABLE.**

**The landed `A8b` established that absolute and assembled `β_V` and the
induced-`G` normalisation depend on `R5` and on `R1`, AS A LOWER BOUND — `R2`,
`R3` and `R4` are neither established nor excluded.** Nothing here changes that.

**And the reason is visible in `§5.4`: `K` CANCELS.** The same cancellation that
makes the ratio's sign derivable removes the normalisation `G_ind` requires.
**`K` cancels here; `N` cancels in the landed `A8a` analysis. Both cancellations
are what make the ratio clean, and both are exactly what the absolute quantity
still needs.**

## 9. `A8` — no majority reasoning

**MEASURED occurrence counts of `β_V/β_B`, reported because the criterion asks
for them:**

    GATES.md                                             16
    derivations/P2-HK-01_heat_kernel_species.md            3
    derivations/betav_discriminating_power.md               3
    derivations/P2-BETAV-RECON-01_scope-assessment.md       4
    CONVENTIONS.md                                          1

**These agree with the specification's `§10` record exactly.**

**THE VERDICT DOES NOT REST ON THEM, AND THE SEARCH CONFIRMING THAT IS
REPORTED.** Searching the artifact for count-based reasoning — the strings
`more often`, `majority`, `most documents`, `sixteen`, `prevalent`, `outnumber`,
`more frequent` — returns **ZERO HITS.** **No step of the artifact's `§3`, `§4`
or `§5` cites a count of documents.**

**The same search over THIS report returns hits, and every one is in a denial**:
this paragraph, and `§9`'s closing statement that sixteen mentions are not
sixteen derivations. **The artifact carries the derivation and contains no such
string at all; the report carries the required disclaimer and therefore must
contain them.** Reporting the search this way rather than as a single number is
deliberate — a bare "zero hits" would be false of the report and true of the
artifact, and the criterion asks about the reasoning, not the file.

**The derivation chain is: `CONVENTIONS.md:15` and `:16` fix `tr a_1/R`;
`CONVENTIONS.md:19` fixes the determinant powers; `CONVENTIONS.md:21` fixes the
prefactor rule; the bundle dimensions and the Ricci trace do the rest.** **Not
one of those five inputs is a count of documents.**

**SIXTEEN MENTIONS IN `GATES.md` IS NOT SIXTEEN DERIVATIONS.** `GATES.md`
attributes the anchor to `P2-HK-01` at both `:228` and `:751` — **so most of its
sixteen are citations of ONE derivation, and counting them would count that
derivation many times over.** Had the derivation come out positive, sixteen
signed mentions would have been sixteen errors, not sixteen reasons.

## 10. `A9` — nothing numerically evaluated, nothing corrected

### 10.1 First search — NEW NUMERICAL RECONSTRUCTION OUTPUT

**Searched: the artifact, this report, and the commit messages, for numerically
evaluated `β` coefficients, determinant values, eigenvalues, finite-difference or
derivative outputs, fitted quantities, or reconstruction-run results.**

**EXPRESSLY EXCLUDED, as the criterion states: governance measurements, line
numbers, SHAs, quoted repository values, AND THE SYMBOLIC SIGN AND PREFACTOR
ARITHMETIC THAT `A4`–`A6` REQUIRE** — including `p_V` and `p_B`, the determinant
factors they come from, `−K/12`, `+K/4`, `K(2+k)/12`, the derived signed ratio
`−(k+2)`, and the signed kill values `−3` and `−5`.

**MEASURED FINDING: ZERO new numerical reconstruction output.**

**Every numeric token in the artifact and this report resolves to one of:**

    symbolic sign/prefactor algebra   p_s = ±1/2, −k/2, d/6 − e, −K/12, +K/6,
                                      +K/12, +K/4, K(2+k)/12, −(k+2), 1/6, −1/3,
                                      4/6, 5/3, 10 − k, −5/2 — all A5–A6 outputs,
                                      all excluded, none numerically evaluated
    quoted repository values          −3, −5, −2, −4, −3.2(5), β_B(ξ=1/6)=0,
                                      the +1 proper-time coefficient
    governance measurements           path counts, section counts, test counts,
                                      occurrence counts, exit statuses
    line numbers and SHAs             throughout
    section numbers                   §3.4, §5.2, 2.1 …
    version numbers                   Python 3.11.15, pytest 9.1.1, numpy 2.4.6,
                                      sympy 1.14.0, ruff 0.15.8

**NO DETERMINANT WAS EVALUATED, NO EIGENVALUE COMPUTED, NO DERIVATIVE TAKEN, NO
`k`-SCAN RUN, AND NO SCRIPT EXECUTED.** The symbolic re-check operated on the
symbols `K`, `k`, `d` and `e` and returned exact rationals and symbolic
expressions — `-K/12`, `K*(k + 2)/12`, `-k - 2`, `10 - k` — **with no
floating-point arithmetic at any step.**

**MEASURED, because "no decimals" would be the wrong claim and I checked rather
than asserting it:** a decimal-literal scan returns hits in both documents, and
**every hit is a section number (`§3.4`, `2.1`), a version number
(`3.11.15`, `9.1.1`, `2.4.6`, `1.14.0`, `0.15.8`), the pytest wall-clock
`53.22 s`, or the quoted repository figure `−3.2(5)`.** All four classes are
expressly excluded by the criterion. **Not one decimal in either document was
produced by evaluating an operator, and the artifact contains no decimal at all
outside its own section numbers.**

**Commit messages: no numeric token of any kind in any of the four.** Commit 3's
message reads *"the conventions require a negative anchor, and three documents
say otherwise"* — a verdict and a document count, both excluded.

**A NOTE ON WHY THE EXCLUSION MATTERS, since the specification flags it.** `A5`
requires `p_V` and `p_B` with their determinant factors; `A6` requires the two
signed kill values; `A4` requires `−3` and `−5` quoted. **Under the earlier
draft's wording — "any numerical `β` value, determinant or eigenvalue result" —
a correct execution would have violated the search by satisfying `A4`–`A6`.**
The distinction that resolves it is `symbolic reconciliation` versus `numerical
reconstruction`, **and the operative test is whether a number was PRODUCED BY
EVALUATING an operator. None was.**

### 10.2 Second search — any edit to a document other than this task's four paths

    git diff --name-status aebca32c…..commit 3
    A  derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md
    A  reviews/chatgpt/2026-08-17T1250Z_sign-01-anchor-reconciliation.md
    A  specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md

    git diff --diff-filter=MDRCTUX --name-status  →  EMPTY
    non-addition status entries in the range      →  0

**MEASURED: ZERO edits to any document outside this task's own paths. Three
additions, all of them this task's own, and no modification, deletion, rename,
copy, type change, unmerged or unknown entry anywhere in the range.**

## 11. `A10`, `A11` — scope, and nothing existing changed

**`A10`, MEASURED at commit 3 — 3 ADDITIONS, 0 MODIFICATIONS**, listed in
`§10.2`. **INTENDED at commit 4 — 4 additions, 0 modifications**, adding
`reports/2026-08-17T1250Z_sign-01-anchor-reconciliation.md`, this file.
**MEASURING THAT IS POST-REPORT EVIDENCE AND NOTHING HERE CLAIMS TO HAVE DONE
IT.**

**`modify:` is `[]` and remained `[]`.**

**`append_only: DECISION_LOG.md` is a CHECKER-CONFIGURATION DECLARATION, NOT AN
AUTHORISATION TO WRITE THAT FILE.** **`DECISION_LOG.md` was not written; the two
readings did not appear to conflict, so `§8` was not invoked.** The checker's
`P3` confirms it: `base_is_byte_prefix_of_head: true`, zero deleted lines, no
commit with deletions.

**The `{HHMM}Z` token.** UTC measured before writing anything:
`2026-08-17T12:50:02Z`, giving `1250Z`. **Commit 1's recorded time is
`2026-08-17 12:50:15 +0000` — the same minute.** All three authored paths carry
`1250Z`.

**`A11`, every path at the evidence base blob-compared at the head:**

    paths at the evidence base   467
    paths at the head            470
    COMPARED                     467
    IDENTICAL                    467
    DIFFERING                      0
    missing at the head            0
    new at the head                3   — exactly A10's three additions

**Named confirmations, each a blob comparison:**

    GATES.md                                    1 path    unchanged
    CONVENTIONS.md                              1 path    unchanged
    derivations/P2-BETAV-*                      5 paths   all unchanged
    P2-LATTICE-MICROSPEC-01 artifacts           7 paths   all unchanged
    registers: docs/BRANCHING_POLICY.md,
               DECISION_LOG.md                  2 paths   both unchanged
    scripts/                                   60 paths   all unchanged
    tests/                                     21 paths   all unchanged
    results/                                   69 paths   all unchanged

**SEVEN microspec artifacts, as the criterion now states**, and this report names
them: `kinetic-operator-dossier`, `plaquette-provenance`, `rp-dependency-ledger`,
`rp-gap-classification`, `rp-literature-coverage`, `selection-discriminants`,
`tm-rp-scope`.

**MEASUREMENT CORRECTION: `derivations/P2-BETAV-*` IS FIVE AT THIS EVIDENCE BASE,
NOT FOUR.** The criterion says "all four". The fifth is
`P2-BETAV-RECON-01_scope-assessment.md`, **which the previous task landed into
this very evidence base.** All five are unchanged. **I report the count I
measured.** See `§14.2`.

## 12. `A12` — gate invariants and pins

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
`GATES.md` is BLOB-IDENTICAL between the evidence base and commit 3** (`§11`), so
no status line in it could have changed.

**The scoped read is load-bearing here more than usual.** `P2-BETAV-CIRC-01`'s
section spans `GATES.md:328-597` — 270 lines — **and contains a
`Status stays **SPECIFIED**` line at `:425` about a DIFFERENT gate.** An unscoped
grep for a status inside that range returns the wrong gate's state.

**A SIGN VERDICT DOES NOT ADVANCE A GATE.** `RECON-01` stays `PROPOSED`;
delivering its target is not running it.

## 13. `A13`, `A14`, `A15` — checker, validators, hygiene

    base   aebca32c6129746b8e1c58ca9f907b734024fb83
    head   d88ed5500793b9f0642dc99aa6e57f8965a6cea4   (commit 3)

    run 1 INCLUSIVE   exit 0   PASS   256 lines   sha256 488fed7f9c4a87dcad1a3b00263700438a9f944a612a0f05ca21d133ea358632
    run 1 EXCLUSIVE   exit 0   PASS   256 lines   sha256 952b015826b62a648ddcba56a19d2f755db2952c3d7fda018ae2e886322d740f
    run 2 INCLUSIVE   exit 0   PASS   256 lines   sha256 488fed7f9c4a87dcad1a3b00263700438a9f944a612a0f05ca21d133ea358632
    run 2 EXCLUSIVE   exit 0   PASS   256 lines   sha256 952b015826b62a648ddcba56a19d2f755db2952c3d7fda018ae2e886322d740f

    stderr empty in all four.

    P1 PASS   P2 PASS   P3 PASS   P4 PASS
    P5 NOT_APPLICABLE — no merge commit in range
    P6 PASS   P7 PASS   P8 PASS
    P9 NOT_APPLICABLE — range adds no report

    overall PASS in all four.   commits_in_range 3   first-parent 3

### 13.1 The output was PARSED, not grepped — and here is the difference

**PARSED with a JSON walker over every `status` and `overall` field:**

    18 × PASS   +   2 × NOT_APPLICABLE   =   20 values, and NOTHING ELSE.
    ZERO NON_GREEN statuses. ZERO DECLARATION_CONFLICT statuses.

**A TOKEN GREP OF THE SAME BYTES RETURNS, in every one of the four outputs:**

    NOT_DECLARED           1
    NOT_PARSEABLE          2
    DECLARATION_CONFLICT   0

**All three of those tokens are members of `NON_GREEN`, so the grep reads as
three non-green findings and an `INCOMPLETE` verdict. There are none.** Both
tokens occur only in definitional prose — the `overall_note` at line 7 and `P1`'s
`does_not_establish` at line 11. **The previous executor measured this and the
specification carries it forward as an instruction; I followed the instruction and
confirm the measurement reproduces exactly at this range.**

### 13.2 What `RUN 1` did

**MEASURED: `RUN 1`'s default subject selection selected exactly ONE
specification** — this task's, the only one in range:

    specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md
    stated: 4 additions, 0 modifications    counted 4 / 0    parse OK

**`RUN 1` and `RUN 2` are BYTE-IDENTICAL at each reading**, verified by `diff`
returning nothing, **so the four invocations produce exactly TWO distinct byte
strings.** **That does not make them the same check: `RUN 2` names the subject and
`RUN 1` discovers it.**

**The `C3` multi-specification residual DID NOT ARISE, and the reason is that
there is ONE declaring specification, not that declarations agreed.** **This is
the "cannot trigger" half of that diagnosis, not the "agreed" half** — the
previous task recorded the other half, where two specifications with DIFFERING
stated totals produced no conflict because totals are not what the mechanism
compares. **The residual is unchanged and remains unregistered.**

**`P1`'s `counted_set` holds the literal `{HHMM}Z` placeholders**, e.g.
`reports/2026-08-XXT{HHMM}Z_sign-01-anchor-reconciliation.md`, because `P1`
compares a specification's `stated:` total against its own manifest block rather
than against the diff.

### 13.3 `declared_source`, and `P7`

    P3   PASS   declared_source: specification   declared ['DECISION_LOG.md']
                supplied_by_config ['DECISION_LOG.md'] — they agree
    P7   PASS   declared_source: specification   declared []
                section_count_base 14   section_count_head 14   raw 14

**`P7` REPORTS FOURTEEN SECTIONS. `PASS` AT ZERO WOULD HAVE BEEN A STOP** — a
gate file parsing to no sections would satisfy "nothing changed" vacuously.

**`P5` and `P9` are `NOT_APPLICABLE`, not weak passes.** `P5` has no merge in
range; `P9` has no report in range at commit 3. **At commit 4 `P9` acquires a
subject, and measuring that is post-report evidence.**

### 13.4 `RUN 1` config, verbatim — observational, governs nothing

    {
      "base": "aebca32c6129746b8e1c58ca9f907b734024fb83",
      "head": "d88ed5500793b9f0642dc99aa6e57f8965a6cea4",
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

### 13.5 `RUN 2` config, verbatim — stop-governing

    {
      "base": "aebca32c6129746b8e1c58ca9f907b734024fb83",
      "head": "d88ed5500793b9f0642dc99aa6e57f8965a6cea4",
      "specification_paths": [
        "specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md"
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
specification's declarations were adjusted to make `RUN 2` pass. `RUN 2` passed
on its first invocation at both readings.**

### 13.6 The output, verbatim, `INCLUSIVE` reading

**`RUN 1` and `RUN 2` are byte-identical here, verified by `diff`.**

    {
      "base": "aebca32c6129746b8e1c58ca9f907b734024fb83",
      "commits_in_range": 3,
      "commits_on_first_parent_line": 3,
      "head": "d88ed5500793b9f0642dc99aa6e57f8965a6cea4",
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
                "commit": "3d423ef160fdb6d5996f76671cba5b52d2ce5dbc",
                "work_paths": []
              },
              {
                "adds_review": true,
                "commit": "5c939136afd491456654ca126dd51fb941ab78d8",
                "work_paths": []
              },
              {
                "adds_review": false,
                "commit": "d88ed5500793b9f0642dc99aa6e57f8965a6cea4",
                "work_paths": [
                  "derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md"
                ]
              }
            ],
            "first_review_commit": "5c939136afd491456654ca126dd51fb941ab78d8",
            "first_work_commit": "d88ed5500793b9f0642dc99aa6e57f8965a6cea4",
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
              "specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md"
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
              "specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md"
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
            "first_commit": "3d423ef160fdb6d5996f76671cba5b52d2ce5dbc",
            "first_commit_paths": [
              "specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md"
            ],
            "reports_added": [],
            "reviews_added": [
              "reviews/chatgpt/2026-08-17T1250Z_sign-01-anchor-reconciliation.md"
            ],
            "reviews_missing_function_directory": [],
            "specification_is_first_commit": true,
            "specs_added": [
              "specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md"
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

### 13.7 The `EXCLUSIVE` reading

**MEASURED by `diff`: line 252 of 256, `"inclusivity": "INCLUSIVE"` →
`"EXCLUSIVE"`. One line, nothing else.** `commits_out_of_scope` is empty and
`commits_in_scope` is 3 in all four.

### 13.8 `A14`, `A15`

**`A14`, MEASURED at commit 3, exit status 0:**

    324 passed, 2 deselected      in 53.22 s

**Expected 324 and 2; measured 324 and 2.**

**`A15`, MEASURED on commits 1–3. Commit 4 is post-report evidence:**

    commit 1   3d423ef1   spec: reconcile the beta_V/beta_B anchor sign before pre-registration
               body empty   trailer hits 0   author date == commit date, not amended
    commit 2   5c939136   review: pre-execution review for the anchor sign reconciliation
               body empty   trailer hits 0   author date == commit date, not amended
    commit 3   d88ed550   derivation: the conventions require a negative anchor, and three documents say otherwise
               body empty   trailer hits 0   author date == commit date, not amended

**MEASURED over the range: a scan for `Co-Authored-By`, `claude.ai/code`,
`Generated with`, `Claude-Session` and `noreply@anthropic` returns ZERO**, and
`P6` independently reports `matches: []` for all three.

**Rule 20 binds this task and was NOT exercised.** No message needed repair.
**No force-push, no branch deletion, no history rewrite.**

**Commits, MEASURED:**

    commit 1   3d423ef160fdb6d5996f76671cba5b52d2ce5dbc   specs/2026-08-17T1250Z_sign-01-anchor-reconciliation.md
    commit 2   5c939136afd491456654ca126dd51fb941ab78d8   reviews/chatgpt/2026-08-17T1250Z_sign-01-anchor-reconciliation.md
    commit 3   d88ed5500793b9f0642dc99aa6e57f8965a6cea4   derivations/P2-BETAV-SIGN-01_anchor-reconciliation.md

**Commit 4's message, INTENDED:**

    report: the conventions require a negative anchor

## 14. Stops and clarifications

**No stop was declared. Five primary categories, one primary per finding,
secondary findings separate, included even where there were none.**

### 14.1 `SPECIFICATION_DEFECT` — first finding: the repair scope is three documents, not one

**`SIGN-01`'s `§0` and `§1` name one unsigned document, "the `RECON-B0` spec".
MEASURED: THREE documents assert the target unsigned** — the `RECON-B0`
specification (nine lines), the `RECON-B0` INTEGRATION specification (`:38`,
`:122`), and the `RECON-B0` pre-execution review (`:12`, `:53`, `:88`). Listed in
`§7.1` and in the artifact's `§6.1`.

**Not a stop:** the criterion asks me to name every document inconsistent with
the verdict, which I did; the framing's undercount is in the prose, not in a
criterion I had to satisfy. **The consequence is for the repair task, which would
otherwise fix one document and leave two.**

**A note on my own exposure here.** The integration specification is the one I
executed immediately before this task, and **my report on it stated that the
unsigned form was "confined to one specification". That was wrong about a
specification I had in front of me** — I measured the `RECON-B0` spec's unsigned
lines and did not check the integration spec's own text for the same defect. See
`§14.5`.

### 14.2 `SPECIFICATION_DEFECT` — second finding: the `P2-BETAV-*` count

**`A11` asks me to confirm "all four `derivations/P2-BETAV-*` artifacts". THERE
ARE FIVE at this evidence base**, the fifth being
`P2-BETAV-RECON-01_scope-assessment.md`, **landed into this very evidence base by
the task immediately preceding.** All five are unchanged.

**Not a stop**, and the operative requirement holds more widely than stated.
**Worth recording because the same specification explicitly corrected the
microspec count from six to seven** — the correction was applied to one count and
not to the neighbouring one, and both drifted for the same reason: a landed task
added an artifact.

### 14.3 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — first finding: the `r = 1` conflict

**Untouched by this task and explicitly out of scope.** `CONVENTIONS.md:24`
freezes the Wilson parameter `r = 1`; `D-1c`'s `R1` treats `r` as unfrozen on the
strength of the kinetic-operator dossier's `:169-171`. **Both are on `main`.
I did not adjudicate it.** See `§15`.

### 14.4 `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — second finding: the declared environment

**`docs/local/execution_environment.md` declares a WINDOWS environment** —
identity `zeta-3070\codexsandboxoffline`, a Python 3.12 interpreter at a Windows
path, a venv at `C:\p2-validator\venv`. **Every run in this task was on Linux
with Python 3.11.15, so every measurement was taken in an UNDECLARED
environment.** The declaration's version policy covers the version differences
("package names are the requirement; these versions are a dated snapshot, not
pins") but says nothing about the platform. **Unchanged and still unregistered.**
No stop: `A3`'s requirements are the interpreter and the four packages, and all
five held.

### 14.5 `OBSERVATION_METHOD_ERROR` — one finding, mine, caught inside the task

**My first repository-wide sweep classified a line as SIGNED if `U+2212` appeared
ANYWHERE on it.** That labelled `DECISION_LOG.md`, `tests/test_gate_anchors.py`,
`scripts/betav_assembly.py`, `scripts/betav_discriminating.py`,
`scripts/betav_decomp_q2.py`, `results/P2-BETAV-ASSEMBLY-01/raw/betav_assembly.json`
and `reviews/claude/2026-07-19-paper2-followup.md` as UNSIGNED — **when each
carries `U+002D ASCII HYPHEN-MINUS` immediately before the token, which is a
minus sign in the encoding those file types use.**

**It would have inflated the repair scope from three documents to eleven and
reported the repository as internally split on the sign when it is not.**

**Corrected by classifying the character IMMEDIATELY PRECEDING each `(k+2)`
token instead of scanning the line** — the method the artifact's `§6` reports and
whose counts `§6.3` gives.

**THIS IS THE SAME CLASS OF ERROR AS THE RESEARCHER'S NON-ASCII FILTER, MADE IN
THE OPPOSITE DIRECTION.** The Researcher stripped `U+2212` and saw unsigned where
there was a minus; I searched only for `U+2212` and saw unsigned where there was
an ASCII minus. **Both mistake an ENCODING for a SIGN, and `§3` of the
specification warns against only one of the two directions.** A specification that
said "enumerate codepoints" rather than "beware the non-ASCII filter" would have
caught both.

**Secondary, also mine:** the artifact's `§6.2` classification of unsigned tokens
into assertions and mentions **is a judgment read from document context, not a
measurement**, and the artifact now says so and lists every token individually so
the classification can be checked. The 56 / 10 / 24 / 2 sign counts are measured;
the 12 / 12 split inside the 24 is not.

### 14.6 `ENVIRONMENT`, `REPOSITORY_DEFECT` — nothing to report

**`ENVIRONMENT`: no failure. No restoration needed or performed, and NEITHER of
Rule 13's two diagnostic orders was exercised.**

**`REPOSITORY_DEFECT`: none found.** 467 of 467 base paths blob-identical, both
pins recompute, the gate section count is 14, all four checker invocations pass,
and the validators are steady at 324/2. **`§14.1` and `§14.2` are classified as
specification defects because both are discrepancies between a specification's
prose and the repository, not broken repository mechanisms.**

**And one thing that could have been a repository defect and is not.** The
`U+2212`/ASCII split across markdown and code (`§14.5`) **is not an
inconsistency**: every one of the 66 signed tokens means the same thing, and the
encoding difference tracks file type. **A repair task must not "normalise" the
ASCII hyphens in `scripts/`, `tests/` and `results/` — they are correct as
written, and `results/…/betav_assembly.json` is a recorded output that must not be
edited at all.**

## 15. Did deriving the sign make me want to correct a document, start `RECON-01`, or settle `r = 1`?

**YES to the first, and it was the strongest pull in this task by a wide margin.**

**Correcting a document: acutely, and the temptation had a specific shape.** Once
`§5` came out negative, the `RECON-B0` specification's `:117` — *"`β_V/β_B =
(k+2)` is a species-level determinant-structure RATIO"* — is a one-character fix,
and I had just measured the exact nine lines. **Worse, one of the three
inconsistent documents is the integration specification whose report I wrote
forty minutes earlier, in which I asserted the defect was "confined to one
specification".** The pull was not merely to fix a typo; it was to fix my own
prior misstatement.

**I did not.** `§4` forbids modifying those files, `§8` limits writable paths to
four, and Rule 20 permits only a pre-push message repair with the tree unchanged.
**But the governance reason is not the strongest one.** A verdict task that also
repairs is a task whose review approved a derivation and got an edit to a landed
specification — **and the edit would have been made by the same executor who
derived the verdict it implements, with no independent check between the two.**
The separation is what makes the repair reviewable. **`§11` measures 467 of 467
base paths blob-identical.**

**Starting `RECON-01`: no, and I want to be precise about why not, because the
absence of temptation here is itself informative.** Having a signed target makes
pre-registration possible and makes building feel closer. **But `§8.2`'s count is
unchanged — eight of ten components lack a usable implementation — and the
component I would have reached for is the same one I nearly reached for last
task: the registered regression anchors, still `None yet (proposed)` at
`GATES.md:754`.** Writing one now would be writing part of the `RECON-01`
specification, which `§4` forbids twice over.

**Settling `r = 1`: no, and this task made it easier to leave alone rather than
harder.** `SIGN-01` shows what a properly scoped convention adjudication looks
like — derive from the frozen lines, test which convention is load-bearing, name
the inconsistent documents, repair nothing. **The `r = 1` conflict deserves the
same treatment and would not fit in a paragraph of this report.** The one thing
`§5.2` adds to it is a warning by analogy: **`CONVENTIONS.md:15`'s `E`-sign turned
out to be constrained by an independent cross-check rather than free, and
`CONVENTIONS.md:24`'s `r = 1` may or may not be — that is exactly the question
the adjudicating task has to answer, and I did not answer it here.**

**I corrected nothing, started nothing, and settled nothing.**

## 16. Evidence layering

**This report is committed as commit 4 and MEASURES COMMIT 3. Nothing in it
claims to measure commit 4.**

**Committed here, measured at commit 3:** `A1`–`A12`, `A14` and `A15` for
commits 1–3; `A13`'s two runs with both configs and the output verbatim;
commits 1–3 SHAs and their stored messages; commit 4's INTENDED message; `A10`'s
final 4/0 scope stated as INTENDED with the measured 3/0 figure at commit 3.

**Post-report evidence, returned to the Reviewer and NOT written back:** `A10`'s
final scope measured base-to-commit-4; `A13-final`, being `RUN 2` re-run at
commit 4; `A14` at commit 4; `A15` for commit 4; the push; and the branch tip
read back.
