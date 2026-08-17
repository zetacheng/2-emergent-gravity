# `P2-BETAV-SIGN-01` — reconciling the `β_V/β_B` anchor sign

**Kind:** convention reconciliation. **It computes nothing and builds nothing.**
It determines which signed form the repository's own frozen conventions require,
so that `RECON-01` can be pre-registered against a blind target.

**Evidence base:** `aebca32c6129746b8e1c58ca9f907b734024fb83`.

## 0. The verdict, stated first

**`SIGNED NEGATIVE`.**

**The repository's frozen conventions require `β_V/β_B = −(k+2)`, hence `−3` at
the physical `k = 1`. The unsigned form carried by the `RECON-B0` specification
is an error.**

**It was DERIVED from `CONVENTIONS.md:15`, `:16`, `:19` and `:21` plus the bundle
data, NOT quoted from `P2-HK-01`'s stated `−3`.** The derivation is `§3`. The
agreement with `P2-HK-01:95` is a cross-check reported after the fact, not the
basis.

**Three documents are left inconsistent with this verdict, not one.** `§6` names
them with lines. **This artifact corrects none of them.**

## 1. The question

> **Under the repository's own frozen conventions, what signed value is the
> correct pre-registration target for `β_V/β_B` at general `k`?**

**Three outcomes were available and the derivation was run before any of them was
preferred.** `SIGNED NEGATIVE`, `SIGNED POSITIVE`, `NOT DETERMINABLE`.

**`NOT DETERMINABLE` was a live possibility and is not the outcome**, for a
reason `§5` makes precise: the conventions the sign depends on are frozen, and
the one convention that could have left it open turns out not to matter.

## 2. The four statements, quoted with sign codepoints

**Read as bytes. Every non-ASCII codepoint on each line was enumerated rather
than displayed through a filter**, because the character in dispute is
`U+2212 MINUS SIGN` and a `[:print:]`-class filter deletes it.

### 2.1 `GATES.md`

    :751   `β_V/β_B = −(k+2)` (from `P2-HK-01`), compared only at the end.
           sign character: U+2212 MINUS SIGN
    :731   tracks `β_V/β_B = −(k+2)`. **Scope label: a 2026 reconstructed
           pipeline, NOT a …
           sign character: U+2212 MINUS SIGN
    :757   For the reconstruction itself: stuck at `−3` ∀k ⟹ the new pipeline
           is degenerate
    :758   (a bug); drift toward `−5` at heavy mass ⟹ longitudinal artifact.
           sign character on both: U+2212 MINUS SIGN
    :228   `β_V/β_B=−3` (from `P2-HK-01`).
           sign character: U+2212 MINUS SIGN

### 2.2 `derivations/P2-HK-01_heat_kernel_species.md`

    :95    β_V/β_B    = (K/4)/(−K/12)   = −3
           sign character: U+2212 MINUS SIGN, twice
    :102   - `β_V/β_B = −3` reproduces the analytic value the paper quotes for
           the Proca ratio (recorded here as a pre-registered prediction,
           **not** as a target).
           sign character: U+2212 MINUS SIGN

### 2.3 `derivations/betav_discriminating_power.md`

    :44    β_V(k)/β_B = −(k + 2)     [ k=1 → −3 ; k=0 → −2 ; k=2 → −4 ; k=3 → −5 ].
           sign character: U+2212 MINUS SIGN, on the general form and on all four
           tabulated values
    :47-49 (Derivation: vector factor contributes `−p·K·(tr a_1/R) =
           −(½)K(−1/3)=+K/6`; scalar`^k` factor `det^{+k/2}` has `p=−k/2`,
           contributing `+kK/12`; `β_V(k)=K(2+k)/12`, and `β_B=−K/12`.)
           sign characters: U+2212 MINUS SIGN throughout

### 2.4 The `RECON-B0` assessment, `derivations/P2-BETAV-RECON-01_scope-assessment.md`

    :340   #### `A8a` — does the RATIO `β_V/β_B = −(k+2)` depend on any of `R1`–`R5`?
           sign character: U+2212 MINUS SIGN
    :48-49 anchor as `−(k+2)` and the kill criteria as `−3` and `−5`. **The
           specification governing this assessment writes them unsigned** —
           `(k+2)`, `3`, `5`.
           :48 U+2212 MINUS SIGN; :49's `(k+2)`, `3`, `5` carry NO sign
           character — and that is a QUOTATION of the specification's defect,
           not an assertion by the assessment

**THE ASSESSMENT IS SIGNED THROUGHOUT AND FLAGS THE UNSIGNED SPECIFICATION
ITSELF.** It is not among the inconsistent documents.

### 2.5 `CONVENTIONS.md:21`, in full

    | Species coefficient `β_s` | Coefficient of `m² ln m²` in `Z(m²)`. Computed
    from `a_1`: `β_s = −p_s (4π)^{−2} (tr a_1 / R)`, where `p_s` is the log-det
    prefactor of the species (`+1/2` per bosonic `det^{−1/2}` factor, `−1/2` per
    `det^{+1/2}` factor / fermion loop). Reported both as a raw value (this
    convention) and as convention-independent ratios `β_F/β_B`, `β_V/β_B`,
    `β_B(ξ)/β_B`. |

**The leading `−` on `p_s` is `U+2212`, and it is part of the definition.**

### 2.6 The three supporting convention rows

    :15   | Heat-kernel operator | `Δ = −∇² + E` (Laplace-type). `E` is the
          endomorphism (potential/bundle) term; **sign convention: `E` enters
          with a `+` so that a scalar curvature coupling `ξR` appears inside `E`
          as `E ⊃ +ξR`.** The mass `m²` is separated out explicitly (`Δ + m²`)
          and is **not** counted inside `E` for the `a_k`. |

    :16   | Heat-kernel expansion | … `a_0 = tr 𝟙`, and `a_1 = tr[(1/6)R·𝟙 − E]`
          (the `R`-linear Seeley–DeWitt coefficient). |

    :19   | Massive-vector (Proca) structure |
          `Z_{s=1,m} = det^{−1/2}(Δ^{(1)}+m²)·det^{+1/2}(Δ^{(0)}+m²)`, with the
          vector Laplacian `Δ^{(1)}` having `E^{μ}{}_{ν}=R^{μ}{}_{ν}`
          (`tr E = R`) and the Stueckelberg scalar `Δ^{(0)}` having `E=0`. |

**And `CONVENTIONS.md:5-6` records that these were fixed before any computation
in `P2-HK-01` and were not adjusted afterwards to reproduce a paper value.**

## 3. The ratio, DERIVED from the conventions

**Three ingredients, reported separately as the criterion requires.**

### 3.1 Ingredient (i) — the sign convention in `β_s`'s own definition

**`CONVENTIONS.md:21` carries a LEADING MINUS on `p_s`:**

    β_s = −p_s (4π)^{−2} (tr a_1 / R)

**Write `K ≡ (4π)^{−2}`. `K > 0`**, being the square of a real reciprocal, so
`K` contributes no sign and cancels from any ratio.

**So the definition contributes ONE sign flip relative to `p_s (tr a_1/R)`,
applied identically to every species.** `§5.1` shows this flip cannot affect the
ratio.

### 3.2 Ingredient (ii) — `p_V` and `p_B`, with the determinant factors they come from

**`CONVENTIONS.md:21`'s prefactor rule: `+1/2` per bosonic `det^{−1/2}` factor,
`−1/2` per `det^{+1/2}` factor or fermion loop.**

**The baseline boson `β_B` is the minimal real scalar**, one bosonic
`det^{−1/2}` factor:

    β_B     determinant factor  det^{−1/2}(Δ^{(0)}+m²)      p_B = +1/2

**The Proca species is NOT a single determinant.** `CONVENTIONS.md:19` gives it
as a PRODUCT of two factors with OPPOSITE powers, so it contributes TWO terms,
each with its own prefactor:

    vector part        det^{−1/2}(Δ^{(1)}+m²)      p = +1/2
    Stueckelberg part  det^{+1/2}(Δ^{(0)}+m²)      p = −1/2

**This is the structural fact the whole sign turns on: `p_V` is not a single
number.** Writing "`p_V`" as one prefactor is what an unsigned reading of the
anchor implicitly does, and it is why `§6`'s repair scope matters. **At general
`k` the Stueckelberg factor is `det^{+1/2}(Δ^{(0)}+m²)^k = det^{+k/2}`, giving
`p = −k/2`** — `§4`.

### 3.3 Ingredient (iii) — the sign of `tr a_1 / R` for each

**From `CONVENTIONS.md:16`, `a_1 = tr[(1/6)R·𝟙 − E]`. Writing `d = tr 𝟙` for the
bundle dimension and `e ≡ tr E / R`:**

    tr a_1 / R = d/6 − e

**`E` enters `a_1` with a MINUS, and `CONVENTIONS.md:15` fixes `E` entering `Δ`
with a PLUS. Both signs are frozen and both are load-bearing.**

**Per bundle, from `CONVENTIONS.md:19`'s assignments:**

    minimal real scalar (β_B)   d = 1   E = 0                e = 0
                                tr a_1/R = 1/6 − 0 = +1/6      POSITIVE

    Proca vector part           d = 4   E^μ_ν = R^μ_ν
                                tr E = R^μ_μ = R  ⟹  e = 1
                                tr a_1/R = 4/6 − 1 = −1/3      NEGATIVE

    Stueckelberg scalar part    d = 1   E = 0                e = 0
                                tr a_1/R = 1/6 − 0 = +1/6      POSITIVE

**`d = 4` for the vector part is the 1-form bundle dimension in `d = 4`, and
`tr E = R^μ_μ = R` is the trace of the Ricci endomorphism — the contraction that
makes `e = 1` exactly, and therefore makes `4/6 − 1` NEGATIVE rather than
positive.** **That single negative is where the ratio's minus sign is born.**

### 3.4 The two species coefficients

**Applying `β_s = −p_s K (tr a_1/R)` term by term:**

    β_B          = −(+1/2)·K·(+1/6)             = −K/12          NEGATIVE
                   one flip from the definition, none from tr a_1/R

    β_V, vector  = −(+1/2)·K·(−1/3)             = +K/6           POSITIVE
                   TWO flips — the definition's, and tr a_1/R's — which cancel

    β_V, Stueck. = −(−1/2)·K·(+1/6)             = +K/12          POSITIVE
                   TWO flips — the definition's, and p_s's — which cancel

    β_V (k=1)    = +K/6 + K/12 = 2K/12 + K/12   = +K/4           POSITIVE

**`β_B` is NEGATIVE and `β_V` is POSITIVE. The ratio's minus sign is a genuine
sign REVERSAL between the two species, not an overall convention.**

**Both of `β_V`'s terms come out positive for DIFFERENT reasons** — the vector's
from a negative bundle trace, the Stueckelberg's from a negative determinant
power — **and they therefore ADD rather than partially cancelling.** A derivation
that assigned the Stueckelberg factor `p = +1/2` would have obtained
`+K/6 − K/12 = +K/12` and a ratio of `−1`, not `−3`.

### 3.5 The ratio at `k = 1`

    β_V/β_B = (+K/4)/(−K/12) = (1/4)·(−12) = −3

**`K` cancels, as `CONVENTIONS.md:21` says it must for a ratio.**

    β_V/β_B = −3      at k = 1      SIGNED NEGATIVE

**DERIVED, not quoted.** `P2-HK-01:95` states the same value; that agreement is
recorded in `§7` as a cross-check and was not an input.

## 4. The general-`k` form

**WHERE IT IS DERIVED: `derivations/betav_discriminating_power.md:34-50`.**

**It generalises `CONVENTIONS.md:19`'s determinant structure at its `:37`:**

    Z_{s=1,m} = det^{−1/2}(Δ^{(1)}+m²) · det^{+1/2}(Δ^{(0)}+m²)^k ,   k ∈ ℝ

**with `k=1` the physical Proca, one compensating scalar.** So
`det^{+1/2}(·)^k = det^{+k/2}(·)`, and `CONVENTIONS.md:21`'s prefactor rule
gives `p = −k/2` — which `:48` states in exactly those terms.

**DOES THAT DERIVATION USE `CONVENTIONS.md:21`'S SIGN RULE? YES, EXPLICITLY.**
`:41` attributes the recipe to "the `a_1` recipe (P2-HK-01 conventions)", and
`:47-49` reproduces the rule term by term: *"vector factor contributes
`−p·K·(tr a_1/R) = −(½)K(−1/3)=+K/6`; scalar`^k` factor `det^{+k/2}` has
`p=−k/2`, contributing `+kK/12`; `β_V(k)=K(2+k)/12`, and `β_B=−K/12`."`
**That is `CONVENTIONS.md:21`'s formula with `CONVENTIONS.md:16`'s bundle traces,
not a separate convention.**

**IS THE SIGN PRESERVED AT GENERAL `k`, OR ONLY STATED AT `k=1`? PRESERVED, AND
DERIVED UNIFORMLY IN `k`.** Re-deriving independently:

    β_V(k)  = −(+1/2)·K·(−1/3)  +  −(−k/2)·K·(+1/6)
            = +K/6 + kK/12
            = K(2 + k)/12                        POSITIVE for k > −2

    β_V(k)/β_B = [K(k+2)/12] / (−K/12) = −(k+2)

**`k` enters ONLY through the Stueckelberg factor's prefactor `p = −k/2`, and
that is a LINEAR, SIGN-PRESERVING dependence.** `β_B` carries no `k` at all, so
no `k`-dependent sign flip is available anywhere in the ratio. **The `k=1` case
is a substitution into the general result, not a separate calculation from which
the general form was extrapolated.**

    k = 0    −2         no compensating scalar
    k = 1    −3         physical Proca
    k = 2    −4
    k = 3    −5
    k = ½    −5/2

**These agree with `betav_discriminating_power.md:44`'s table and with
`results/P2-BETAV-ASSEMBLY-01/README.md:11`, which records
`k=0→−2, 1→−3, 2→−4, 3→−5, ½→−5/2`.**

### 4.1 The two kill values under this verdict

**`GATES.md:757-758`'s criteria, as signed numbers under `SIGNED NEGATIVE`:**

    stuck at degenerate     stuck at −3 for all k
                            i.e. the pipeline returns the k=1 value regardless
                            of k, so it is not resolving the determinant
                            structure

    heavy-mass drift        drift toward −5 at heavy mass
                            and −5 is EXACTLY the k=3 value, which
                            betav_discriminating_power.md:74-76 notes as
                            "suggesting the artifact mimics an extra
                            compensating power"

**BOTH ARE NEGATIVE, AND THE SIGN IS PART OF EACH TEST.** *Stuck at `−3`* and
*stuck at `3`* are different criteria, and under this verdict only the first is
the registered one. **A pipeline sitting at `+3` satisfies NEITHER criterion as
written while plainly being wrong** — which is precisely the hole the unsigned
form leaves open.

## 5. What the sign does and does not depend on

**Three convention flips were tested. The algebra was done by hand in `§3` and
`§4` and then re-checked symbolically; both agree.**

### 5.1 Flipping `CONVENTIONS.md:21`'s own leading sign — RATIO UNCHANGED

**Under `β_s = +p_s K (tr a_1/R)`:**

    β_B    = +K/12          (was −K/12)
    β_V(k) = −K(k+2)/12     (was +K(k+2)/12)
    ratio  = −(k+2)          UNCHANGED

**Every `β_s` flips, so the ratio does not.** **The leading minus in
`CONVENTIONS.md:21` is therefore NOT what makes the target negative** — a fact
that matters for `§8.3`, because it means the verdict does not hang on the one
line most obviously labelled a convention.

### 5.2 Flipping the `E`-sign convention at `CONVENTIONS.md:15` — RATIO CHANGES

**Under `a_1 = tr[(1/6)R·𝟙 + E]`, i.e. `E` entering with the opposite sign:**

    vector    tr a_1/R = 4/6 + 1 = +5/3     (was −1/3)
    ratio     = 10 − k                       (was −(k+2))
    at k = 1  = +9                           (was −3)

**THIS IS THE LOAD-BEARING CONVENTION.** It is frozen at `CONVENTIONS.md:15`
**with a stated reason** — *"`E` enters with a `+` so that a scalar curvature
coupling `ξR` appears inside `E` as `E ⊃ +ξR`"* — and it is cross-checked inside
`P2-HK-01` by an independent limiting case: `:100-101` records
`β_B(ξ=1/6) = 0`, a conformally coupled scalar inducing no `R` term. **That
check fixes the relative sign of `ξ` against `1/6` inside `a_1`, which is the
same sign the ratio depends on.** Under the flipped convention `β_B(ξ)` would
read `−(1/2)K(1/6 + ξ)`, which has no zero at `ξ = +1/6`, and the conformal
cross-check would fail.

**So the convention the sign depends on is not merely declared; it is
independently constrained by a limiting case the repository already records.**

### 5.3 Flipping the curvature sign convention at `CONVENTIONS.md:12` — RATIO UNCHANGED

**`e ≡ tr E / R` is a RATIO to `R`.** Under `R → −R`, both `tr E` and `R` change
sign together for every bundle in `§3.3` — the vector's `tr E = R^μ_μ = R` by
construction, the scalars' `tr E = 0` trivially — **so every `e` is unchanged,
`tr a_1/R = d/6 − e` is unchanged, and the ratio is unchanged.**

## 6. Documents left inconsistent with the verdict

**`SIGNED NEGATIVE` leaves documents that assert the target UNSIGNED
inconsistent with it.** **THIS ARTIFACT CORRECTS NONE OF THEM.** They are listed
so the repair task knows its scope.

**MEASURED repository-wide: 92 `(k+2)` tokens, classified by the character
IMMEDIATELY PRECEDING the token — not by whether a minus appears anywhere on the
line.**

    preceded by U+2212 MINUS SIGN          56
    preceded by U+002D ASCII HYPHEN-MINUS  10
    ────────────────────────────────────────
    SIGNED NEGATIVE, both encodings        66

    unsigned                               24
    preceded by U+002B PLUS                 2   — both in THIS task's own
                                                specification, naming
                                                `+(k+2)` as the alternative
                                                outcome to test
    ────────────────────────────────────────
    TOTAL                                  92

**ZERO documents assert `+(k+2)` anywhere in the repository's science.** The two
`+` tokens are this task's specification stating the outcome it was required to
leave open.

**The 24 unsigned tokens split TWELVE and TWELVE into ASSERTIONS and MENTIONS,
and only assertions are inconsistencies.**

**THIS SPLIT IS A JUDGMENT, NOT A MEASUREMENT, AND I MARK IT AS ONE.** The token
`(k+2)` is byte-identical in both classes; what separates them is whether the
containing document presents it AS the anchor or reports that someone else wrote
it that way. **The counts 56 / 10 / 24 / 2 are measured; the 12 / 12 split inside
the 24 is read from context and a different reader could move a borderline case.**
`§6.1` and `§6.2` list every token individually so the classification can be
checked rather than taken.

### 6.1 Inconsistent — unsigned ASSERTIONS of the target

**Document 1 — `specs/2026-08-17T1105Z_recon-b0-scope.md`, the `RECON-B0`
specification. SEVEN unsigned assertions plus both kill values:**

    :60    anchor           β_V/β_B = (k+2), from P2-HK-01, COMPARED ONLY AT
    :64    does NOT show** — that returning `(k+2)` shows the reconstruction is
    :113   3a  does the RATIO (k+2) itself depend on any of R1–R5?
    :117   **`β_V/β_B = (k+2)` is a species-level determinant-structure RATIO.**
    :226   **`A8a` — does the RATIO `β_V/β_B = (k+2)` itself depend on any of
    :374   `(k+2)` result must not read it as Finding 5 restored.**
    :384   **If the RATIO `(k+2)` is convention-fixed and independent of

    :158   **The gate names two kill criteria** — stuck at `3` for all `k` means a
    :159   degenerate pipeline; drift toward `5` at heavy mass means a longitudinal

    NO sign character on any of the nine lines.

**Document 2 — `specs/2026-08-17T1151Z_integrate-recon-b0.md`, the `RECON-B0`
INTEGRATION specification. TWO unsigned assertions:**

    :38    A8a   the RATIO β_V/β_B = (k+2)          depends on NONE of R1–R5
    :122   future reconstruction returning `(k+2)` would show the reconstruction

**Document 3 — `reviews/chatgpt/2026-08-17T1105Z_recon-b0-scope.md`, the
`RECON-B0` pre-execution review. THREE unsigned assertions:**

    :12    … curved-space operator requirements, flat-limit regression targets,
           separation of the `(k+2)` ratio anchor from absolute/assembled beta_V …
    :53    A dependency of final microscopic assembly or induced-G normalization
           does not by itself force the clean-room `(k+2)` reconstruction
           downstream of D-pre.
    :88    A future successful reconstruction of `(k+2)` would not vindicate the
           historical Finding 5 value.

**THE REPAIR SCOPE IS THREE DOCUMENTS, NOT ONE.** **`SIGN-01`'s framing names
only "the `RECON-B0` spec"; the integration specification and the `RECON-B0`
review carry the same defect and were not named.** `§9.1` records this.

### 6.2 NOT inconsistent — unsigned MENTIONS

**Twelve unsigned tokens, on eleven lines, name the form or quote the defect
rather than asserting a target, and are consistent with the verdict:**

    derivations/P2-BETAV-RECON-01_scope-assessment.md:49   quotes the defect
    specs/…T1151Z_integrate-recon-b0.md:78, :443, :447     quote the defect
    specs/…T1250Z_sign-01-…md:44                           quotes the defect
    specs/…T1250Z_sign-01-…md:98, :179                     name the general form
    reviews/chatgpt/…T1250Z_sign-01-…md:40                 names the general form
    reports/…T1105Z_recon-b0-scope.md:113, :1126           quote the defect
    reports/…T1151Z_integrate-recon-b0.md:288              quotes the defect —
                                                          TWO tokens on this one
                                                          line, which is why
                                                          twelve tokens occupy
                                                          eleven lines

**`specs/…T1250Z_sign-01-…md:98` and `:179` deserve their classification stated
rather than assumed: they are THIS specification naming "the `(k+2)`
generalisation" while its own `§1` holds the sign open and offers `+(k+2)` as a
permitted outcome.** A document that declares the sign undetermined cannot be
asserting it. **The same token in the `RECON-B0` specification, which presents
`(k+2)` as the anchor, is an assertion.** Context, not bytes, is what separates
them.

**The distinction is not cosmetic.** A document that writes *"the specification
writes them unsigned — `(k+2)`, `3`, `5`"* is EVIDENCE OF the defect; repairing
it would delete the record of it.

### 6.3 The ASCII-hyphen population, and why it is not a second discrepancy

**Ten `(k+2)` tokens carry `U+002D ASCII HYPHEN-MINUS` rather than `U+2212`:**

    DECISION_LOG.md
    scripts/betav_assembly.py
    scripts/betav_decomp_q2.py
    scripts/betav_discriminating.py
    tests/test_gate_anchors.py
    results/P2-BETAV-ASSEMBLY-01/raw/betav_assembly.json
    reviews/claude/2026-07-19-paper2-followup.md
    reviews/chatgpt/2026-08-17T1151Z_integrate-recon-b0.md

**THESE ARE SIGNED NEGATIVE AND CONSISTENT WITH THE VERDICT.** The encoding
differs because code, JSON and test files use ASCII; the sign does not differ.

**This matters as a method warning in both directions.** A search for `U+2212`
alone reports these files as unsigned — **which is the mirror image of the
Researcher's error, and I made it on the first pass** (`§9.2`). A search that
strips non-ASCII reports the `U+2212` population as unsigned. **Only classifying
the character immediately before the token gets both populations right.**

## 7. Cross-checks, reported after the derivation and not used as its basis

**`P2-HK-01:95` states `β_V/β_B = (K/4)/(−K/12) = −3`.** My `§3.4` obtained
`β_V = +K/4` and `β_B = −K/12` independently from `CONVENTIONS.md:15`, `:16`,
`:19` and `:21`. **Agreement, including both intermediate values.**

**`betav_discriminating_power.md:44` states `−(k+2)` with the table
`k=0→−2, 1→−3, 2→−4, 3→−5`.** My `§4` obtained `β_V(k) = K(2+k)/12` and
`−(k+2)` independently. **Agreement, including the table.**

**`results/P2-BETAV-ASSEMBLY-01/README.md:11` records `k=½→−5/2`.** My general
form gives `−(½+2) = −5/2`. **Agreement at a non-integer `k`**, which the `k=1`
statement alone could not have supplied.

**`P2-HK-01:100-101`'s conformal check `β_B(ξ=1/6) = 0`** independently
constrains the `E`-sign convention `§5.2` identifies as load-bearing.

**Four independent agreements, none of them an input.** Had any disagreed, the
verdict would have been `NOT DETERMINABLE` pending reconciliation of the
disagreement.

## 8. Rule 16 assessment

**Rule 16 is operative. All four junctions.**

### 8.1 First junction — a sign verdict corrects nothing

**WHICHEVER WAY THIS WENT, AT LEAST ONE LANDED DOCUMENT WOULD BE LEFT
INCONSISTENT WITH IT.** Under `SIGNED NEGATIVE` it is three documents (`§6.1`);
under `SIGNED POSITIVE` it would have been `GATES.md`, `P2-HK-01`,
`betav_discriminating_power.md`, the `RECON-B0` assessment, four
`derivations/P2-BETAV-*` artifacts, `CLAIMS.md`, `PROGRESS.md`, `MIGRATION.md`,
`DECISION_LOG.md`, three scripts, a test, and two `results/` records — 66 signed
tokens' worth.

**THIS TASK LISTS THEM AND REPAIRS NONE.**

**THE REPOSITORY WILL CARRY A KNOWN INCONSISTENCY UNTIL A REPAIR TASK LANDS.**
That is a deliberate cost: **landing a verdict and landing a correction are
different acts, and conflating them would put an unreviewed edit to a landed
specification inside a task whose review approved only a verdict.**

### 8.2 Second junction — this unblocks pre-registration and nothing else

**`RECON-01` now has a BLIND TARGET: `−(k+2)`, with signed kill criteria `−3`
and `−5`.** **That is a PRECONDITION FOR STARTING, NOT A STEP TOWARD
FINISHING.**

**TEN COMPONENTS REMAIN, EIGHT WITHOUT A USABLE IMPLEMENTATION** — seven
specification-only and one neither, per the landed `RECON-B0` inventory.
**Nothing in this artifact reduces that count by one.** A pre-registerable
target is a document, not a pipeline.

**`P2-BETAV-CIRC-01` remains `RUN`, neither passed nor failed, and this artifact
does not touch the question whether the historical Finding 5 is circular.**

### 8.3 Third junction — is `CONVENTIONS.md:21` a convention or a derivation?

**IT IS REGISTERED AS A CONVENTION AND ITS CONTENT IS DERIVED ELSEWHERE.**

**Registered as a convention:** it is a row in `CONVENTIONS.md`'s table under the
heading `## Locked conventions for the independent-verification sweep` (`:8`), in
a file whose `:3` reads *"No calculation may begin until every relevant
convention below is filled, reviewed, and locked"*. **Its own text calls itself
one** — *"Reported both as a raw value (this convention) and as
convention-independent ratios"*.

**Derived elsewhere:** `P2-HK-01:23-51` obtains the same relation from
`W = p Tr ln(Δ+m²)` via `ln(Δ+m²) = −∫₀^∞ (dτ/τ) e^{−τ(Δ+m²)}` and the
proper-time integral, whose `m² ln m²` coefficient it computes as exactly `+1`
at `:45-47`, arriving at `β_s = −p_s (4π)^{−2}(tr a_1/R)` at `:50`.

**WHAT FOLLOWS, AND IT IS NOT WHAT THE JUNCTION ANTICIPATES.** The junction asks
whether a different convention would give a different signed target without any
physics changing. **For `CONVENTIONS.md:21` specifically, the answer is NO —
`§5.1` shows the ratio is INVARIANT under flipping its leading sign**, because
the flip applies to numerator and denominator alike. **So the verdict does not
rest on `:21` being right about its own sign.**

**The convention that DOES carry the sign is `CONVENTIONS.md:15`'s `E`-enters-
with-a-plus** (`§5.2`), and a different choice there would give `10 − k`, i.e.
`+9` at `k=1`. **That one is a convention in the sense that it is a declared
choice — but it is not free: `P2-HK-01:100-101`'s conformal cross-check
`β_B(ξ=1/6) = 0` fails under the alternative.** **So the sign is fixed by a
declared convention that an independent limiting case also requires.**

**Stated plainly: the signed target is convention-relative, and the relevant
convention is constrained rather than arbitrary. It is NOT an additional
convention-independent physical prediction**, and it must not be reported as
one. **`CONVENTIONS.md:21` and `P2-HK-01:10` both call the ratios
"convention-independent"; `§5` makes that precise — they are independent of the
NORMALISATION conventions, and dependent on the `E`-sign and determinant-
structure conventions.** That distinction is finer than either document draws.

### 8.4 Fourth junction — nothing here touches the absolute `β_V` or `G_ind`

**A SIGNED RATIO TARGET DOES NOT MAKE THE ABSOLUTE QUANTITY ASSEMBLABLE.**

**`A8b` of the landed `RECON-B0` assessment established that absolute and
assembled `β_V` and the induced-`G` normalisation depend on `R5` and on `R1`,
AS A LOWER BOUND — `R2`, `R3` and `R4` are neither established nor excluded.**
Nothing in this artifact changes that, and the ratio's `K`-cancellation is
exactly why: **the same cancellation that makes the ratio's sign derivable
removes the normalisation that `G_ind` requires.**

**`K` cancels in `§3.5`; `N` cancels in the landed `A8a` analysis. Both
cancellations are what make the ratio clean, and both are what the absolute
quantity still needs.**

## 9. Method notes and limits

### 9.1 A repair-scope finding the specification did not anticipate

**`SIGN-01`'s framing names one unsigned document. There are three** (`§6.1`).
The integration specification's `:38` and `:122`, and the `RECON-B0` review's
`:12`, `:53` and `:88`, assert the target unsigned. **Reported, not repaired.**

### 9.2 An observation-method error of mine, caught inside the task

**My first repository-wide sweep classified a line as signed if `U+2212` appeared
ANYWHERE on it.** That labelled `DECISION_LOG.md`, `tests/test_gate_anchors.py`,
`scripts/betav_assembly.py`, `scripts/betav_discriminating.py`,
`scripts/betav_decomp_q2.py` and `results/…/betav_assembly.json` as UNSIGNED,
when each carries an ASCII hyphen-minus immediately before the token — **signed,
in the encoding those file types use.** It would have inflated the repair scope
from three documents to eleven and reported the repository as internally split
when it is not.

**Corrected by classifying the character immediately preceding each token
instead of scanning the line** (`§6.3`). **This is the same class of error as
the Researcher's non-ASCII filter — mistaking an encoding for a sign — made in
the opposite direction.**

### 9.3 What this artifact does not establish

- **It does not establish that `RECON-01` will succeed, or that a reconstruction
  returning `−(k+2)` would vindicate the historical Finding 5.**
- **It does not establish the ratio as a convention-free prediction** (`§8.3`).
- **It does not establish anything about `R1`–`R5`, the `r = 1` conflict, or the
  absolute `β_V`.**
- **It does not repair, and does not authorise a repair.** The three documents in
  `§6.1` are unchanged.
- **It evaluated nothing numerically.** The `§3`–`§5` arithmetic is symbolic sign
  and prefactor algebra over `K`, `p_s`, `d`, `e` and `k`, which `A5`–`A6`
  require; no determinant, eigenvalue, derivative or `β` coefficient was
  numerically evaluated.
