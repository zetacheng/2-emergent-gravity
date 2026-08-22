# Landing record — `P2-BETAV-EXTCOMP-INTEG`

**Transport only.** Every figure below is READ from the landed artifact under
`M8`. **None is carried from the measurement's execution report**, and this
task's specification states none.

    Source          science/betav-extcomp-01
                    7035e0b7b4a6eaeefb91900eefc0a74e78f78fa0
    Base            caf5111dacad21da9e204b79b4b7add1f648107c
    Fork point      caf5111dacad21da9e204b79b4b7add1f648107c
    Merge product   03aa08fb7d5f368192eae1b39eebe66fabd31f2f

---

## 1. The measurement, as measured

**Both aggregations are shown together for every variant, and NEITHER is
presented as the result.**

    variant                            B_R             B_D    R_signed       R_abs
    HEAVY|V2a_with_m4        +2.297033e-03   +1.443306e-03      0.6283      0.6283
    HEAVY|V2b_no_m4          +4.960433e-04   +9.309336e-04      1.8767      1.8767
    LIGHT|V2a_with_m4        -8.685872e-03   -4.556727e-03      0.5246      0.5246
    LIGHT|V2b_no_m4          -1.132365e-03   -3.060544e-04      0.2703      0.7009

**The per-component coefficients, all ten, over all four frozen variants:**

    component          HEAVY|V2a_with_m4         HEAVY|V2b_no_m4       LIGHT|V2a_with_m4         LIGHT|V2b_no_m4
    R1                    +3.311124e-03           +1.207456e-03           -8.172226e-03           -3.919449e-04
    R2                    +3.311124e-03           +1.207456e-03           -8.172226e-03           -3.919449e-04
    R3                    +1.620972e-03           +2.176838e-05           -9.028303e-03           -1.625978e-03
    R4                    +1.620972e-03           +2.176838e-05           -9.028303e-03           -1.625978e-03
    R5                    +1.620972e-03           +2.176837e-05           -9.028303e-03           -1.625978e-03
    D1                    +1.482084e-03           +2.227417e-03           -7.762685e-03           -7.533763e-04
    D2                    +1.146967e-03           +1.090053e-04           -4.530628e-03           -6.653118e-04
    D3                    +1.146967e-03           +1.090053e-04           -4.530628e-03           -6.653118e-04
    D4                    +1.146967e-03           +1.090053e-04           -4.530628e-03           -6.653118e-04
    D5                    +2.293546e-03           +2.100235e-03           -1.429066e-03           +1.219040e-03

**Every component produced a coefficient under every variant.** The artifact
records all ten as `REPORTED` under all four, with no fit `NON-FINITE`, none
`EXACTLY SINGULAR`, and no component `NOT EVALUABLE`.

**The variant whose two aggregations diverge, with the component that accounts
for it.** `LIGHT|V2b_no_m4` gives `R_signed` `0.2703` against `R_abs`
`0.7009`. The artifact attributes this to `D5`, which in that combination
carries the opposite sign to `D1`–`D4`, so the signed sum cancels partially
while the sum of magnitudes does not. **In the other three combinations the two
aggregations coincide.**

**The band — the spread over the four frozen combinations, which is the only
band there is:**

    B_R        min  -8.685872e-03   max  +2.297033e-03   spread 1.098290e-02
    B_D        min  -4.556727e-03   max  +1.443306e-03   spread 6.000033e-03
    R_signed   min  +2.702790e-01   max  +1.876718e+00   spread 1.606439e+00
    R_abs      min  +5.246136e-01   max  +1.876718e+00   spread 1.352105e+00

**The reproduction check.** One component's coefficient was recomputed in a
second independent pass and the artifact records the two as **identical at the
printed precision**.

## 2. The assembly weights, and why they mattered

**The landed assembly's weight was established from the pipeline, not
assumed.** `w_i = 1/5` — a mean over the five retained components — fixed at
`scripts/recovered_2026/proca_loop.py:130`.

**Established by two routes, as the artifact records them.** Structurally: the
landed axis-TT bubble and the per-component bubble build identical tensors and
differ only in whether the recipe index is summed, plus the `/ 5.0`, so the
landed output is the mean of the per-component outputs by construction.
Numerically: at one point the two agree to a relative difference of
`2.531e-15`.

**What a wrong weight would have done.** Unity in place of `1/5` would have
multiplied **every aggregate by five**, while leaving each per-component
coefficient correct — a uniform factor in a result table, which is the hardest
class of error to notice.

**And what it does not do.** Because the retained and discarded sets each have
five members, the factor appears identically above and below and **cancels in
both ratios**. It does **not** cancel in `B_R` or `B_D`. **The artifact records
this in its pre-registration, before any number existed**, so it could not
afterwards be offered as a reason the weight choice did not matter.

**`v_i = 1/5` on the discarded side is THIS TASK'S CHOICE and not a landed
definition** — the repository has never assembled those components. The
artifact labels it as a choice wherever a result uses it.

## 3. The sign reversal, transported open

**The retained aggregate changes sign between the two frozen mass windows.**
`B_R` is positive on `HEAVY` and negative on `LIGHT`, in both fit forms; every
per-component coefficient does the same.

**Its spread exceeds either endpoint's magnitude.** The artifact's secondary
quantity records `|B_R|` across the four combinations as running from
`4.960433e-04` to `8.685872e-03`, with an absolute spread of `1.098290e-02` —
larger than the larger endpoint.

**The secondary quantity exists to make this visible.** Without the
denominator's own band beside the ratio's, a ratio can look stable while
numerator and denominator move together.

**NO EXPLANATION IS OFFERED AND NONE IS LANDED HERE.** The measurement recorded
the reversal open, and this record transports it open. Why it occurs is
registered as `R-17` in `DECISION_LOG.md` and is not answered by this landing.

## 4. The pre-registered consequence, marked as not a verdict

**`§0b` of the measurement's specification stated, before any number existed,
what each outcome would and would not mean.** That text is transported as the
measurement transported it — **as a pre-registered consequence, and not as a
verdict of the measurement or of this landing.**

The record states, **with its scope attached and not detachable from it**:

> Under the repository's presently locked operational definition, the
> target-bearing coefficient is the retained-space coefficient. The
> discarded-space measurement therefore does not numerically redefine that
> repository quantity. **This is a statement about the scope of the registered
> observable — not a conclusion that the discarded components are physically
> irrelevant, and not a conclusion that the retained-space quantity is the
> unique covariant coefficient.**

**The second sentence is why the first is safe to land.** Without it the first
reads as a physical result. **Whether the retained-space coefficient is the
physically relevant one is exactly what `H-EXT-01` leaves open**, and what
`GAP-B`'s identifiability mismatch has not settled.

**Provenance of this qualification, recorded rather than blurred.** The scoped
wording above is **required by this integration's specification for safe
landing**. The measurement artifact carries the pre-registered `§0b` text and
the reach-not-correctness distinction; **it does not carry this exact scoped
sentence.** This record does not imply that it did.

## 5. The prediction

**The pre-registered methodological prediction held.** The artifact predicted,
before any number existed, that the ratio's spread would be smaller than the
spread of its numerator and denominator separately, and records the outcome:

    relative spread   B_R        3.4382
    relative spread   B_D        3.8543
    relative spread   R_signed   1.4965
    relative spread   R_abs      1.1261

**Both ratios have a smaller relative spread than either aggregate.**

**Its holding is consistent with the stated cause without establishing it.**
The artifact draws that distinction and this record does not weaken it: a
smaller relative spread is consistent with shared systematics partly
cancelling between numerator and denominator, and **does not establish that as
the cause.**

## 6. Window count, preserved

**The pipeline defines MORE mass windows than the measurement used.** The
artifact records three at `scripts/recovered_2026/reproduce_betav.py`:
`paper_win` at `:61`, `light` at `:62` and `heavy` at `:63`.

**The measurement used two** — `light` and `heavy`, the two the vector path
consumes at `:70-71`.

**The ground on which the third was excluded** is the measurement protocol's:
`paper_win` is the scalar `β_B` window, and the measurement's own §0d.1 forbids
computing `β_B`.

**This is not rewritten as a repository with fewer windows.** The third window
exists, is named, and its exclusion is a fact about what this measurement was
authorised to compute — **not a new repository-wide convention.**

## 7. What the measurement does not establish

As the artifact states it:

**ONE LATTICE EXTENT.** `n = 12`, the extent `EXT-01` used. Nothing measures
the approach to any continuum or infinite-volume limit.

**ONE FROZEN VARIANT SET**, of four combinations — two windows by two fit
forms. The band is that set's spread and nothing else; there is no statistical
uncertainty in this computation.

**NO CRITERION.** No threshold, pass band or acceptance range appears for any
quantity, and none exists in the repository against which to read the result.

**`H-EXT-01` IS UNRESOLVED, IN EITHER DIRECTION.** The measurement bears on it
and resolves it neither way.

---

## 8. What this landing does NOT decide

**Stated plainly, because each is a reading the result invites:**

- **what the result implies for `H-EXT-01`** — not decided; registered `R-16`;
- **whether `GAP-B`'s mismatches change status** — not decided; registered
  `R-16`;
- **whether any correction to the target-bearing coefficient follows** — not
  decided, and §4's scoped statement is the reason the question remains open
  rather than answered;
- **why the retained aggregate reverses sign** — not decided; registered
  `R-17`.

**Rule 17.** No governance or epistemic classification is added that the
reviewed result did not carry. `Q1` remains `INCONCLUSIVE`. `GAP-A` remains
closed with its momentum condition. `GAP-B` remains as its reviewed result left
it. `H-EXT-01` remains `UNESTABLISHED` and `NOT ASSUMED BY RECON-01b`. No gate
moves; `P2-PHASE-01` is unchanged.

**No further mass window is opened, proposed or scoped by this landing**, and
`R-17` records why one would be the wrong instrument.

---

## 9. The merge, measured

### `M1` — the source ref, from the remote (MEASURED)

    git ls-remote origin refs/heads/science/betav-extcomp-01
      7035e0b7b4a6eaeefb91900eefc0a74e78f78fa0

**Begins with §0's abbreviation `7035e0b7`.** No merge was attempted against
the abbreviation. `A1` does not fire.

### `M3` — dry-run merge (MEASURED)

`git merge-tree --write-tree --messages` returned tree
`0086201dc071aae5fffe95327610b8d00665764e`, exit `0`, **no conflicting paths.**
`A2` does not fire.

### `M4` — the revert hazard: the subject set is EMPTY (MEASURED)

**Paths present on both `caf5111d` and the source at differing blobs, measured
by `git diff --name-only --diff-filter=M`: NONE.** The source only ADDS paths.

**HOW THE EMPTINESS WAS ESTABLISHED, two ways.**

**Structurally:** the fork point and `origin/main` resolve to the same commit,
`caf5111d`, so there is no path at which `main` could carry a blob newer than
the fork's.

**Per path:** `git diff --name-only <fork> <origin/main>` returns an empty
listing. **The empty result is the measurement, not the absence of one.**

**No file was changed on both sides**, so Amendment P(b)'s line-survival
obligation does not arise; its non-arising follows from the emptiness of the
modified-path set rather than from a clean merge. `A5` does not fire.

### `C3` — every arriving path, blob-identical to its source blob (MEASURED)

Measured over the paths the merge brought in, by first-parent diff:

    derivations/P2-BETAV-EXTCOMP-01_external-…md   a7d8b50fb57ed192…  IDENTICAL
    reports/2026-08-21T2224Z_betav-extcomp-01.md   152b8ea63a04404b…  IDENTICAL
    results/P2-BETAV-EXTCOMP-01/…_mlog.json        b91a2a88edbb9f53…  IDENTICAL
    reviews/chatgpt/2026-08-21T2224Z_…md           18138991eb9681f6…  IDENTICAL
    scripts/diagnostics/betav_extcomp_01.py        1e66bee318f441c8…  IDENTICAL
    specs/2026-08-21T2224Z_betav-extcomp-01.md     17c62b72c40eb10e…  IDENTICAL

### `M2` — validators, both sides, in real worktrees (MEASURED)

    merge product  03aa08f   332 passed, 2 deselected, exit 0
    base           caf5111   332 passed, 2 deselected, exit 0

**The clone is unshallowed**, per `M2`: no `.git/shallow` exists and 679
commits are reachable from all refs. **The shallow-clone condition that once
produced six governance-test failures did not recur, and its absence was
measured rather than assumed.** `A3` does not fire.

### `M6` — the governing clause (MEASURED)

`docs/BRANCHING_POLICY.md:25-40`, `## Science branch integration`: `--no-ff`
into a dedicated integration branch, squash/rebase prohibited; "During landing,
only the integration branch and `refs/heads/main` may be pushed"; "Source
branch, session branches and unrelated refs must not move"; "`main` advances
only by fast-forward from its reviewed evidence base to the completed
integration head." **No contradiction with §3. `A4` does not fire.**

### `M7` — two measurements, and they DIFFER (MEASURED)

    (a) base-relative              8 paths
    (b) the source's contribution  6 paths

**They differ, and the difference is exactly this task's own specification and
review** — both absent from the source and both committed to the integration
branch before the merge, as Rule 15's order requires. **Recorded as two
measurements that disagree for a stated reason.**

### `M9` — the pins and the frozen scripts (MEASURED)

    A-EXT-01   ca8e5a870b5c7734321a9b6b97f3844046d8ceb689aece0ca65082b70a522378
    H-EXT-01   e5dd8a28eaff7623af23ab11404ef2d43dc8053599807162863cf38aca239a47

Unchanged, and neither containing file is modified. **All thirteen blobs under
`scripts/recon2026/` and `scripts/recovered_2026/` are unchanged at the merge
product**, compared individually.

### `M10` — append-only verification (MEASURED)

**At the merge product, NO file is modified at all** — every arriving path is
an addition, established by `M4`'s empty modified-path set. **No append-only
file is therefore modified by the merge product**, and that is recorded here so
the criterion has a source either way.

**At the landing head, `DECISION_LOG.md` is modified by this task's §6
records**, and is verified:

    base blob, full content            123159 bytes
      sha256  b998176615402a8235d926f02b42d0bf8f436f7faed445f211c6a8f8e371be29
    first 123159 bytes of the product
      sha256  b998176615402a8235d926f02b42d0bf8f436f7faed445f211c6a8f8e371be29
    product                            128409 bytes

**The complete base bytes are an exact prefix of the product bytes.**
