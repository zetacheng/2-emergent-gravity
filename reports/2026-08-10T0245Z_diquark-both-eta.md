# Report — diquark channel character, carrying both `eta` signs

Specification: `specs/2026-08-10T0245Z_diquark-both-eta.md`
Specification sha256:
`9a8e84c9fa00e7c5c71a58aecc75f6d488bd380ecd6a1bfa054cb511bce00662`
Pre-execution review: `reviews/chatgpt/2026-08-10T0245Z_diquark-both-eta.md`
Evidence base: `8701a97a6bb58550d4300f75c10638b057335731`
Branch: `gate/p2-diquark-both-eta`
Classification: MATERIAL. Branch only; integration is a separate
authorization.

---

## 0. Result, stated first

**The computation went through.** It did not terminate at
`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`, and it did not require
supplying an unauthorized convention.

**The diagnostic verdict is OPPOSITE**, and it is well-defined
**independently of both remaining unfrozen definitions.** Every
coefficient has the form `c = K * eta` where `K` contains the
particle–particle ordering sign and the diquark normalisation but not
`eta`; the ratio `c(eta = -1) / c(eta = +1)` is exactly `-1` with those
symbols still present and cancelling. So, in the ruling's own words:
**the diquark channel character depends on an unresolved sign
convention.**

    S, P, T      no induced diquark coefficient at all — exact cancellation
    V            c = + G*eta*nu*s_pp/(2*N)
    A            c = - G*eta*nu*s_pp/(2*N)

**The absolute attractive/repulsive label per family is NOT well-defined**
and is reported conditional on `s_pp` and `nu`. That split — a determinate
comparison over indeterminate absolutes — is the substance of the result,
and §7 states each half separately rather than averaging them.

Under A6 this is the **first** bullet for the same/opposite verdict and
the **second** for the absolute labels. Neither is the `UNRESOLVED`
outcome, which A6 also permitted and which the computation did not need.

Three execution findings a reader should not miss:

- **A1a's whole-line delimiter rule returned zero matches for BEGIN**
  (§3). The delimiter shared its line with an attachment marker. This is
  the **fourth** distinct failure of the review supply protocol, and the
  first in which the fix from the previous task is what broke.
- **My first blocker check was a proxy that returned the opposite of the
  truth, and my own test caught it** (§5). Searching for `eta = -1`
  matched the sentence that says nothing fixes `eta`.
- **Three of five families vanish** (§6). The earlier exploratory attempt
  vanished in all four it examined. The failure mode did not recur, but
  the result sits one sign error away from it, which is why every
  decomposition is reconstruction-verified.

No STOP condition fired.

---

## 1. A14 — refs, and the branch

    remote refs/heads/main      8701a97a6bb58550d4300f75c10638b057335731
    refs/remotes/origin/main    8701a97a6bb58550d4300f75c10638b057335731
    local main (stale by design) 0f7961747abe2a18b436c0b1e5b928f425ea4d9a

Both `main` refs resolve to the evidence base; no mismatch, so no STOP.
Local `main` is stale by design and was neither consulted nor repaired.
The branch `gate/p2-diquark-both-eta` was created from
`8701a97a…`. No `main` ref moved. No branch was deleted.

---

## 2. A1 — pinned inputs

Verified before use, `git cat-file blob 8701a97a:<path> | sha256sum`. All
five match; no mismatch, so no STOP.

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
      fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a   MATCH
    results/P2-CHANNEL-FREEZE/fierz_matrix.json
      5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9   MATCH
    derivations/P2-PHASE-01_channel_character.md
      380bb11171f7084e4eb30bfd3c393a4ff1c7d8d22063eb56ce3e05e3d8152c5f   MATCH
    derivations/P2-PHASE-01_channel_character_layers.md
      4cea53a7163ccc6aadadd0fca276714c16d805ad8aed3594d64d66d412606711   MATCH
    results/P2-PHASE-01/channel-character-layers/layers.json
      fe343c74389cc996e42567d7dd510f479f1e7ed01cba81de61ff1d6f7e9d1542   MATCH

**Every repository input actually read**, by path, as §6 requires:

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    results/P2-CHANNEL-FREEZE/fierz_matrix.json
    derivations/P2-PHASE-01_channel_character.md
    derivations/P2-PHASE-01_channel_character_layers.md
    results/P2-PHASE-01/channel-character-layers/layers.json
    DECISION_LOG.md
    scripts/P2-CHANNEL-FREEZE/gamma_algebra.py

`DECISION_LOG.md` is read for A2a and for the `g = 2c` and
attraction-label rulings; `gamma_algebra.py` supplies the exact Clifford
representation. Nothing else was read. Neither the quarantined `-3.2(5)`
value, nor the suspended `P2-BETAV-CIRC-01` result, nor the historical
Finding 5 extraction was consumed.

---

## 3. A1a — the review, and the fourth delimiter failure

Committed at `reviews/chatgpt/2026-08-10T0245Z_diquark-both-eta.md` in
commit 2, before the derivation note.

    committed blob sha256  8ce6e928781680d73ab651033177238196ad000af8cfd677e2778c1f18871a02
    size                   7167 bytes, 7112 characters, 105 lines
    identical to the extracted text:  True

### The whole-line rule returned zero matches for BEGIN

A1a states the two delimiter literals and says **"Match them as COMPLETE
LINES, not as first occurrences of the string"**. Executed:

    substring occurrences   BEGINS: 1    ENDS: 1
    WHOLE-LINE matches      BEGINS: []   ENDS: [line 108]

The BEGIN delimiter was not on a line of its own. Line 0 of the supplied
message reads, in full:

    @"/root/.claude/uploads/…/a5d8fe48-SPEC_diquark_both_eta.md" === REVIEW ARTIFACT BEGINS ===

**So the procedure A1a mandates failed outright** — not ambiguously, but
with an empty match set — while the first-occurrence search it forbids
would have succeeded, because the specification was supplied as an
attachment and its own §A1a literals were never in the message text. The
two rules disagreed on this message and the mandated one is the one that
failed.

### What I did, stated so it can be checked rather than trusted

A1a also says **"Exclude any preamble sentence that precedes the BEGIN
line."** Here the preamble precedes the delimiter *on* that line, which I
read as within the clause's contemplation rather than against it. So:

    END      located as a whole line, exactly one occurrence (line 108)
    BEGIN    located as the unique line whose content, after removing a
             prefix matching r'^@"[^"]+"\s+', equals the delimiter exactly

Both assertions were executed, not assumed:

    prefix matches r'^@"[^"]+"\s+'   True
    stripped prefix                  '@"/root/…/a5d8fe48-SPEC_diquark_both_eta.md" '
    remainder == the BEGIN literal   True

Nothing else was removed, added, reflowed or reformatted. No placeholder
appears in the review's text, so none was resolved.

A1a's STOP conditions are "the supplied text is missing" and "does not
correspond to this specification". Neither is met — the text is present
and corresponds unambiguously, naming this task by title, both SHAs,
criterion `A2a`, `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` and Rules
1–17. So this is a reportable deviation, not a stop.

### One residual normalisation, quantified

    literal slice between the delimiter lines   7168 bytes
      leading newlines 1     trailing newlines 1
    committed                                    7167 bytes
      difference: one leading blank line removed; single trailing newline kept
      identical after stripping leading/trailing newlines:  True

This is the same one-byte gap the previous task's report predicted would
remain, unchanged: A1a says "byte-identical to the text between the
delimiters" while the delimiters are line-oriented, so "between" is
ambiguous by exactly the adjacent newlines. Every prior artifact in
`reviews/chatgpt/` begins at its own first content line, which is the
evidence the choice rests on.

### The pattern, now four instances

    1  a delimiter string matched inside the instruction naming it
    2  the same again
    3  no delimiters supplied at all
    4  the delimiters supplied, but BEGIN not on a line of its own

Instance 4 is the interesting one: **the previous specification's fix
caused it.** Stating the literals and mandating whole-line matching
removed instances 1–3 and created a rule that a shared line breaks. The
recurrence is not carelessness in drafting; it is that the protocol is
being re-derived from the last failure each time, one clause per task, in
a task-scoped document that the next task must rediscover.

**The concrete fix, one paragraph, and it belongs in `CONVENTIONS.md`
rather than in the next specification:** the review artifact is delimited
by the two literals; each is located as the unique line whose content
equals the literal *after removal of any leading attachment-marker or
preamble text on that line*; the committed artifact is the lines strictly
between them, with leading and trailing blank lines removed and a single
trailing newline. That covers all four instances, and being in
`CONVENTIONS.md` it stops the per-task rediscovery.

### The review's two non-blocking observations

*Step 5's opening wording.* The Reviewer suggested Step 5 begin "Where
Step 3 makes the comparison well-defined, state whether …". **The
specification I received already reads exactly that way** — §2 Step 5
opens "**Where Step 3 makes the comparison well-defined**, state whether
…". So the observation was made against an earlier draft and the change
is already in the digest I executed. Nothing to act on, and nothing that
required me to choose between readings.

*A8's "with its sentence".* The Reviewer suggested "containing line or
prose sentence, as applicable". **A8 as I received it already says
exactly that.** Also already in the digest. The scan in §9 reports
containing lines throughout, so the sharpened wording is what was
executed.

Both observations are therefore discharged by the specification rather
than by me — which is worth recording, because it is the first time in
this sequence that a reviewer's observation arrived already resolved in
the artifact under review.

---

## 4. A2a — the `eta` ruling, located and quoted

Located by its exact `DECISION_LOG.md` heading, which appears exactly
once at the evidence base:

    ## 2026-08-09 — The charge-conjugation phase `eta` is not selected; both signs are computed

The production script locates it the same way, so removing or retitling
the entry stops the run rather than letting it proceed under a ruling the
repository no longer carries. Quoted from the entry:

> **PI ruling, 2026-08-09 — `η` is not selected; both signs are
> computed.**
>
> The diquark rearrangement requires `ψ̄^c = η ψ^T C⁻¹`. **The frozen
> material fixes no value of `η`, and unlike the exponent mapping no
> executed calculation constrains it.**
>
> **For the SIGN AMBIGUITY exposed by the channel-character derivation,
> the programme evaluates both the `η = +1` and the `η = −1`
> representative rather than selecting between them.** This does not
> assert that the full convention space is exactly two elements — the
> residual phase freedom has not been characterised — only that the
> ambiguity shown to affect the paired product is a sign, and both signs
> are to be carried through and reported.
>
> **The reason is diagnostic.** If both signs give the same channel
> character, **the exposed `η = ±1` sign ambiguity does not affect that
> character, and that sign question closes** — the wider phase freedom
> remains uncharacterised either way. **If they give opposite
> characters, then the diquark channel character depends on an
> unresolved sign convention — and that is something the programme must
> know rather than conceal behind a choice.**

The date is 2026-08-09 and the instruction to evaluate both
representatives is explicit. **The ruling is present and says what A2a
requires**, so no STOP.

**§8's normalised substantive check, re-run independently** rather than
taken from the specification's record. One function applied to both
sides: strip `> ` prefixes, strip `**` and backticks, collapse
whitespace; en dashes preserved.

    PASS   the programme evaluates both the
    PASS   rather than selecting between them
    PASS   depends on an unresolved sign convention

The third phrase matters for §7: the ruling itself supplies the wording
for the outcome this computation reached, so the report is not inventing
a characterisation.

---

## 5. A2 — the three blockers, re-established, and a proxy error I made

### The search

Case-insensitive substring counts on raw UTF-8, no normalisation:

    term                     channel_character.md   phaseA_freeze.md
    'eta'                            13                    4
    'Grassmann'                       5                    2
    'ordering'                        5                    0
    'compound_index_order'            1                    1
    'diquark'                         5                    0
    'charge conjugation'              2                    0

The nine `eta` lines of `channel_character.md`, quoted; the three
load-bearing ones:

>     psibar^c = eta psi^T C^-1          -> lambda^-1 psibar^c   (eta a sign convention)

>     The sign/phase `eta` in `psibar^c = eta psi^T C^-1` appears **once**
>     in the paired product, so it multiplies the pp coefficient by `eta`
>     and **flips its sign** for `eta = -1`. Nothing in the frozen material
>     fixes `eta`.

>     under the un-frozen charge-conjugated-field convention `eta`, and the
>     frozen material fixes neither `eta` nor the pp Grassmann ordering nor the
>     diquark normalisation.

**All three confirmed unfixed:**

- **`eta`** — no value is fixed anywhere in the pinned material; the
  ruling declines to supply one.
- **The particle–particle Grassmann ordering** — the freeze fixes
  `compound_index_order = ['dirac_family', 'internal_family',
  'component']` and `grassmann_crossing_sign = -1`, the latter stated for
  the particle–hole exchange `(alpha,beta,gamma,delta) ->
  (alpha,delta,gamma,beta)`. A particle–particle pairing is a different
  permutation of the same four Grassmann factors and no target ordering
  is declared for it.
- **The diquark operator normalisation** — absent from the frozen
  material entirely.

None is in fact fixed, so Step 1's STOP condition is not met.

### The proxy error, and how it was caught

My first version of this check asked whether a value for `eta` is
*assigned* anywhere, by regex `\beta\s*=\s*[-+]?\s*1\b`. It returned
`True`, which would mean Step 1's STOP fires. **The test file I had just
written failed on it**, which is how I found out rather than reporting a
spurious stop.

The single hit, with its context:

    channel_character.md line 336   matched 'eta = -1'
      and **flips its sign** for `eta = -1`. Nothing in the frozen material

**The occurrence is a case label inside a sentence about the ambiguity,
and the very next clause of that sentence states the opposite of what my
regex concluded.** Searching for the string `eta = ±1` is a proxy for "a
value of `eta` is fixed", and it fails on exactly the sentence that denies
the property — a textbook instance of the umbrella principle the E–L
amendments carry: *evidence must establish the property claimed, not
merely a correlated proxy for it.*

**What I changed, and what I did not.** I did not delete the observation.
The script now reports every literal `eta = ±1` occurrence with its
source, line number, matched text and containing line, explicitly
classified as a case label; and the property it *asserts* is the pinned
note's own statement, checked by normalised containment of "Nothing in the
frozen material fixes eta", with a raised assertion if that statement ever
disappears. A dedicated test pins the classification and fails if the
occurrence vanishes, so a future edit cannot quietly remove the thing
this check exists to explain.

**Why this is reported as a finding rather than absorbed as a bug.** A
proxy that returns the *right* answer is invisible; this one returned the
wrong answer and was caught only because the test was written before the
check was trusted. Had I written the check first and the test to match it,
this report would have claimed a STOP that the material does not support.

---

## 6. A3 — `C` and the demonstrated cancellation, and A7 — the control

### A7 first, because everything depends on it

Recomputed from the frozen Fierz block and the frozen canonical
coefficient, normalisation **L**:

    canonical per-family coefficient, read from the freeze   G/(2*N)

    direct scalar     c_S = G/(2*N)      sign +1
    matrix level      S 0   P 0   V G/4    A G/4    T 0
    operator level    S 0   P 0   V -G/4   A -G/4   T 0     (s_G applied once)

    reproduces c_S > 0 and c_V = c_A = -G/4:   True

**The control passes**, so the gating condition is satisfied and the
particle–particle results rest on machinery that gives the right answer
where the answer is known. The script raises rather than emitting a result
if it ever fails, and a test mutates the crossing sign to confirm the
control is not vacuous.

**A structural contrast, recorded because a reader would otherwise assume
it away:** in the particle–hole rearrangement `V` and `A` survive with
**equal** coefficients; in the particle–particle rearrangement of §7 they
survive with **opposite** ones. Different crossings of the same frozen
interaction; there is no reason for them to agree.

### A3 — `C`'s residual freedom, demonstrated

    defining relation      C gamma_mu^T C^-1 = -gamma_mu
    solution space         complex dimension exactly 1

    representative C_0 = [[ 0, 1, 0, 0],
                          [-1, 0, 0, 0],
                          [ 0, 0, 0,-1],
                          [ 0, 0, 1, 0]]

    C_0^T = -C_0                True
    C_0^dagger C_0 = Id4        True
    det C_0 = 1                 True
    defining relation, all mu   True

**The residual scalar is demonstrated to cancel, not cited.** With
`C -> lambda C_0`:

    (lambda C_0)(lambda C_0)^-1 == C_0 C_0^-1                         True
    (lambda C_0) gamma_mu^T (lambda C_0)^-1 == C_0 gamma_mu^T C_0^-1  True, all four mu
    the assembled coefficients of §7 contain no lambda                True

**And the demonstration is checked non-vacuous:** a structure with `C`
appearing *twice* rather than once does not cancel `lambda` —
`(lambda C_0)(lambda C_0) != C_0 C_0` — so the cancellation test is
sensitive to the paired product's structure rather than passing for
unrelated reasons. Without that check, "the scalar cancels" would be an
assertion about the algebra of inverses instead of about this
rearrangement.

`C` is therefore not the obstruction. A settled `C` licenses nothing about
`eta`, the ordering, or the normalisation.

---

## 7. A4, A5, A6 — the coefficients, the characters, and the verdict

### 7.1 The crossing

The particle–particle rearrangement groups the two `psibar` and the two
`psi`: Dirac pairing `(alpha,gamma)` and `(beta,delta)`, internal pairing
`(a,c)` and `(b,d)`. With `M_a = Gamma_a C` and `N_b = C^-1 Gamma_b`, the
decomposition

    Gamma_{alpha,beta} Gamma_{gamma,delta}
        = Sum_ab f_ab (Gamma_a C)_{alpha,gamma} (C^-1 Gamma_b)_{beta,delta}

is unique because `{Gamma_a}` is complete and `C` invertible.
Coefficients from one trace,
`f_ab = trace[(C^-1 Gamma_a Gamma)(Gamma Gamma_b C)^T] / 16`, valid
because the frozen basis was checked **trace-orthonormal on all 256
pairs** rather than assumed.

    basis trace-orthonormal on all 256 pairs        True
    decomposition diagonal in the family basis      True
    reconstruction exact on all 256 components      scalar True, pseudoscalar True

**Every decomposition is verified by reconstruction**, entry by entry
against the original tensor, not accepted from the trace formula.

    family    scalar term    pseudoscalar term    sum
    S            -1/4             +1/4              0
    P            -1/4             +1/4              0
    V            +1/4             +1/4             +1/2
    A            -1/4             -1/4             -1/2
    T            +1/4             -1/4              0

`S`, `P` and `T` cancel exactly between the two canonical terms; `V` and
`A` reinforce with opposite signs. The mechanism is chiral: the frozen
interaction is the chirally symmetric `S^2 + P^2`, and its
particle–particle image lands in the chirally covariant `V` and `A`
diquark structures.

### 7.2 Statistics, and the internal factor

`psi_{b,beta} psi_{d,delta}` is antisymmetric under simultaneous
exchange, so a Dirac-symmetric structure pairs with an
internal-antisymmetric one. `M_a` and `N_a` were computed to have the
**same** symmetry type in every family — a consistency condition that had
to hold and was checked, with the script raising if it ever fails:

    family    Gamma_a C     C^-1 Gamma_a    internal channel
    S         antisym       antisym         internal-symmetric
    P         antisym       antisym         internal-symmetric
    V         sym           sym             internal-antisymmetric
    A         antisym       antisym         internal-symmetric
    T         sym           sym             internal-antisymmetric

The two surviving families live in **different** internal channels: the
induced `V` diquark is internally antisymmetric, the induced `A` diquark
internally symmetric.

The internal factor `2 delta_ad delta_cb` splits as

    N=2   internal-symmetric +2   internal-antisymmetric +2
    N=3   internal-symmetric +2   internal-antisymmetric +2
    N=4   internal-symmetric +2   internal-antisymmetric +2
    N=5   internal-symmetric +2   internal-antisymmetric +2

**The load-bearing fact is the equality of sign, not the value:** the
internal projection contributes no relative sign between families, so the
relative sign of the `V` and `A` coefficients is the Dirac one. The
magnitude is subject to `nu` regardless.

### 7.3 A4 — the coefficients, both `eta`, side by side

Where `eta` enters, by construction rather than assertion:

    Delta_a    = psibar^c Gamma_a psi = eta * psi^T C^-1 Gamma_a psi
    Deltabar_a = psibar Gamma_a psi^c =       psibar Gamma_a C psibar^T

`Delta` carries `eta`; `Deltabar` does not, because in Euclidean signature
`psi` and `psibar` are independent Grassmann variables and `psibar^c` is a
separate definition rather than a conjugate. The product carries it
**once** — reproducing the pinned note's counting from the construction.

    c_pp(family) = c_canonical * internal_weight * s_pp * eta * nu * f(family)
                 = (G/(2*N)) * 2 * s_pp * eta * nu * f(family)

    S   0
    P   0
    V   + G*eta*nu*s_pp/(2*N)
    A   - G*eta*nu*s_pp/(2*N)
    T   0

**These are labelled assumption-dependent because they are.** `s_pp` and
`nu` are carried, not supplied.

**`s_pp`, the orderings this computation can define** — parities computed,
not asserted:

    (psibar_alpha psibar_gamma)(psi_beta psi_delta)    s_pp = -1
    (psi_beta psi_delta)(psibar_alpha psibar_gamma)    s_pp = -1
    (psibar_gamma psibar_alpha)(psi_beta psi_delta)    s_pp = +1
    (psibar_alpha psibar_gamma)(psi_delta psi_beta)    s_pp = +1

**This is not an enumeration of the admissible ordering space.** The
frozen material says no ordering is fixed; it does not say which are
admissible. The same caution the ruling applies to `eta` applies here, and
the artifact carries that sentence rather than leaving it to the report.

**`nu`, three cases kept apart** — because collapsing them would send a
magnitude question to a verdict it does not deserve:

    positive real rescaling            magnitude only; character invariant
    real negative sign convention      flips the sign, so the character
    genuinely complex nu               no sign at all; an attractive/repulsive
                                       label is inapplicable

### 7.4 A5 — channel character per `eta`

Applying `g = 2c` (2026-08-08 ruling) and the attraction/repulsion label
assigned to the sign of `g` (2026-08-09 ruling), both cited from
`DECISION_LOG.md`, at `s_pp = -1` and `nu = +1`:

    eta = +1     V   c = -G/(2*N)   g = -G/N   REPULSIVE
                 A   c = +G/(2*N)   g = +G/N   ATTRACTIVE

    eta = -1     V   c = +G/(2*N)   g = +G/N   ATTRACTIVE
                 A   c = -G/(2*N)   g = -G/N   REPULSIVE

    S, P, T      c = 0 for both eta;  no character defined

**Every label in that table is conditional on `s_pp = -1` and `nu = +1`,
neither of which is frozen.** Changing either flips all four.

### 7.5 A6 — the verdict

    question   do the two eta representatives give the same channel
               character or opposite ones?
    verdict    OPPOSITE
    surviving families            V, A
    ratio c(eta=-1)/c(eta=+1)     V: -1     A: -1
    symbols still present when the ratio is taken   s_pp, nu

**The verdict is independent of both remaining unfrozen definitions.**
Each coefficient is `c = K * eta` with `K` containing every unfrozen
quantity except `eta`, so for any real nonzero `K` the two signs are
opposite whatever `K` is. The ratio was computed with `s_pp` and `nu`
symbolic and they cancelled; a test asserts both symbols are present in
the un-ratioed expression, so the cancellation is genuine rather than an
artefact of having substituted values.

**In the ruling's own words: the diquark channel character depends on an
unresolved sign convention.** This is the outcome the ruling was designed
to expose, and it is more informative than a single label, which would
have concealed the dependence instead of measuring it.

**Well-defined, independently of `eta`, `s_pp` and `nu`:**

    S, P and T carry no induced diquark coefficient at all
    V and A are the only surviving families
    V and A always carry opposite characters to each other
    flipping eta flips the character of every surviving family

**Not well-defined:**

    whether the induced V diquark is attractive or repulsive
    whether the induced A diquark is attractive or repulsive
    the magnitude of either coefficient

**Two scope limits on the verdict**, stated because omitting them would
overclaim it:

- It requires `nu` real and nonzero. For complex `nu` there is no
  attractive/repulsive label to compare and **no verdict is licensed** —
  A6's third outcome applies to that case.
- `S`, `P` and `T` vanish for both `eta`, so they have no character in
  either. **That is the absence of a quantity to compare, not a "same"
  answer.**

---

## 8. What remains unfrozen after this task

- **`eta`.** Not selected. Both representatives carried and reported. The
  residual phase freedom beyond the `eta = ±1` sign remains
  uncharacterised — the ruling says so and this computation adds nothing
  to it.
- **The particle–particle Grassmann ordering.** Not selected. Four
  orderings defined and evaluated; the admissible space is not
  enumerated.
- **The diquark operator normalisation.** Not selected. Its three cases
  are distinguished, not resolved.

Whether any should be frozen, and to what, is a PI decision this
computation informs and does not take. `conventions_frozen_by_this_
computation` in the results artifact is the empty list, and a test asserts
it.

---

## 9. A8 — forbidden-conclusion scan

    check type    character-exact substring, CASE-INSENSITIVE, on each authored
                  file's raw UTF-8 text; no normalisation; matches do not span
                  file boundaries
    excluded      specs/2026-08-10T0245Z_diquark-both-eta.md, the committed
                  specification, per A8

Targets: `composite vector`, `we select`, `we choose`,
`the channel picture is complete`, `rules out`.

    derivations/P2-PHASE-01_diquark_both_eta.md            2 hits
    scripts/p2_diquark_both_eta.py                         0 hits
    results/P2-PHASE-01/diquark-both-eta/diquark.json      0 hits
    tests/test_p2_diquark_both_eta.py                      0 hits
    reports/2026-08-10T0245Z_diquark-both-eta.md           see below

The two hits, matched text reported **as it appears** rather than
lower-cased, with containing lines:

    target 'composite vector'                  line 396
      matched: 'composite vector'
      **It makes no statement about whether a massive composite vector can
      form, in either `eta` case.**
      CLASSIFICATION: DISCLAIMER. The sentence denies the conclusion.

    target 'the channel picture is complete'   line 402
      matched: 'the channel picture is complete'
      **It does not state that the channel picture is complete.** It computes
      one crossing of one frozen interaction.
      CLASSIFICATION: DISCLAIMER. The sentence denies the conclusion.

**Both are required disclaimers and neither was reworded to avoid a hit**,
per A8. The count was not driven to zero.

**This report is itself an authored file and scans as follows** — measured,
not predicted, immediately before commit 5:

**This report matches all five targets, necessarily**, at four kinds of
site: the target list above, which names each of them once; the two
disclaimer lines quoted verbatim from the derivation note, with their
`target` and `matched` labels; the sentence about the JSON key; and the
back-references in §12 and §13. **Classification: every one is the scan
describing itself; none is an assertion.** No hit is driven to zero and no
disclaimer is reworded to avoid one, per A8.

**The report's own per-target counts are deliberately not printed here.**
Two earlier drafts of this paragraph tried. The first predicted that three
targets "do not appear", which was false the moment it was written, since
the target list above contains all three. The second printed counts that
its own printing changed — **stating the counts inside the file being
scanned is a fixed point**, and each correction moved the very numbers it
was correcting. So the exact counts are measured against the **committed
blob** and reported in the post-report evidence, where they cannot perturb
what they describe. What belongs in the report is the method, the
classification, and the stable part:

    derivation note   2 hits, both disclaimers (quoted above)
    script            0
    results artifact  0
    test file         0
    this report       all five targets present; every hit self-descriptive

Both drafts were the same error as §5's in miniature: a claim about text,
asserted rather than executed. The difference is that §5's was caught by a
test and these were caught by re-running the scan — which is the argument
for running it rather than predicting it.

**A finding about the check's own reach.** The script and the JSON return
0 hits, and that is not because they lack the disclaimer — the script
carries it, under the key
`no_statement_about_a_massive_composite_vector`, spelled with
underscores. A substring scan for `composite vector` cannot see it. So
the scan measures prose, and a JSON key naming convention is invisible to
it. That is not a defect in this task's artifacts, but it does mean a zero
count in a code or JSON file is weaker evidence than the same count in
prose, and a future scan intending to cover machine artifacts would need
to normalise separators — which A8 deliberately forbids, and rightly, since
normalisation is what made earlier checks unfalsifiable.

---

## 10. A10 — nothing pre-existing disturbed; A11 — scope

**A10**, compared as individual blob object IDs from `git ls-tree -r`:

    paths at base                                297
    paths at head                                303
    base-present paths modified or missing        0

    GATES.md          base 849a4fbfe62d   head 849a4fbfe62d   identical
    CONVENTIONS.md    base 0db56c39d44e   head 0db56c39d44e   identical
    AGENTS.md         base 5e60b5fcd6e9   head 5e60b5fcd6e9   identical
    DECISION_LOG.md   base 04539f26a6bc   head 04539f26a6bc   identical
    pyproject.toml    base 9fc6fdd196dd   head 9fc6fdd196dd   identical
    CLAIMS.md         base df75ff4de214   head df75ff4de214   identical

`GATES.md`'s blob read from the object:
`849a4fbfe62d6478f092a84b0175357a74bbbb06`. No gate, gate status, verdict,
artifact digest or hash-pinned artifact was modified.

    pre-existing tests/ paths        16, all blob-identical
    tests/ paths at head             17

**`tests/` gains exactly one file and no existing test is modified,
renamed or removed** — the one thing this specification authorises there,
and the reason the count is stated both ways.

**A11 — the template** as the specification states it:

    add:
      specs/2026-08-XXT{HHMM}Z_diquark-both-eta.md
      reviews/chatgpt/2026-08-XXT{HHMM}Z_diquark-both-eta.md
      derivations/P2-PHASE-01_diquark_both_eta.md
      scripts/p2_diquark_both_eta.py
      results/P2-PHASE-01/diquark-both-eta/diquark.json
      tests/test_p2_diquark_both_eta.py
      reports/2026-08-XXT{HHMM}Z_diquark-both-eta.md
    modify: []
    forbidden_operations: delete, rename, copy, type_change, unmerged, unknown

**The resolved manifest** (`XX = 10`, `{HHMM} = 0245`, fixed by commit 1):

    {
      "mode": "exact",
      "base": "8701a97a6bb58550d4300f75c10638b057335731",
      "head": "HEAD",
      "required": [
        {"operation": "add", "path": "specs/2026-08-10T0245Z_diquark-both-eta.md"},
        {"operation": "add", "path": "reviews/chatgpt/2026-08-10T0245Z_diquark-both-eta.md"},
        {"operation": "add", "path": "derivations/P2-PHASE-01_diquark_both_eta.md"},
        {"operation": "add", "path": "scripts/p2_diquark_both_eta.py"},
        {"operation": "add", "path": "results/P2-PHASE-01/diquark-both-eta/diquark.json"},
        {"operation": "add", "path": "tests/test_p2_diquark_both_eta.py"},
        {"operation": "add", "path": "reports/2026-08-10T0245Z_diquark-both-eta.md"}
      ],
      "forbidden_operations": ["delete", "rename", "copy", "type_change", "unmerged", "unknown"]
    }

    resolved manifest sha256
      e88b9a7c504cc2e21a934a8ae71ff884be00f0a6fe8c0810a76decba9d460826

**Scope-checker output at the pre-report head**, verbatim, including
`observed_operations` (this report is the seventh addition and is not yet
committed):

    $ python -m scripts.governance_tools.scope_checker --repo . --manifest dq_scope_pre.json
    {
      "base": "8701a97a6bb58550d4300f75c10638b057335731",
      "failures": [],
      "head": "fd02a2ef51429d76d75ffab231d2e67e0b307f77",
      "mode": "exact",
      "observed_operations": [
        {
          "operation": "add",
          "path": "derivations/P2-PHASE-01_diquark_both_eta.md"
        },
        {
          "operation": "add",
          "path": "results/P2-PHASE-01/diquark-both-eta/diquark.json"
        },
        {
          "operation": "add",
          "path": "reviews/chatgpt/2026-08-10T0245Z_diquark-both-eta.md"
        },
        {
          "operation": "add",
          "path": "scripts/p2_diquark_both_eta.py"
        },
        {
          "operation": "add",
          "path": "specs/2026-08-10T0245Z_diquark-both-eta.md"
        },
        {
          "operation": "add",
          "path": "tests/test_p2_diquark_both_eta.py"
        }
      ],
      "overall": "PASS",
      "tool": "scope_checker"
    }
    EXIT=0

Six additions, zero modifications at the pre-report head; seven and zero
expected at the final head. The final check is post-report evidence.

---

## 11. A12-pre — validators; A13 — lint

Run individually with `python -m pytest <path>`, at the pre-report head
`fd02a2ef…`:

    tests/test_repository_structure.py           4 passed in 0.02s                EXIT=0
    tests/test_si1_governance.py                14 passed in 0.05s                EXIT=0
    tests/test_gate_anchors.py                  18 passed, 2 deselected in 6.13s  EXIT=0
    tests/test_governance_tools.py               8 passed in 1.48s                EXIT=0
    tests/test_p2_channel_character.py          23 passed in 0.97s                EXIT=0
    tests/test_p2_channel_character_layers.py   26 passed in 0.94s                EXIT=0
    tests/test_p2_diquark_both_eta.py           20 passed in 6.43s                EXIT=0

All seven exit 0. The two pre-existing `P2-PHASE-01` suites are included
because this task touches that gate's material; both were untouched and
both still pass.

**What the new test file covers**, mapped to A9's conditional structure:

    always required
      the particle-hole control                    2 tests (one gating-mutation)
      the C defining relation                      2 tests
      the residual-scalar cancellation             2 tests (one non-vacuity)

    required because Step 3 produced coefficient sets
      the eta relation between the two sets        2 tests, COMPUTED — the ratio
                                                   is recomputed symbolically with
                                                   s_pp and nu present, not
                                                   compared against a stored value

    the crossing itself                            5 tests
    authority and scope                            5 tests, including the
                                                   case-label classification of §5

The `UNRESOLVED` branch of A9 did not apply: coefficient sets exist, so
the relation test is applicable and was written rather than replaced by an
obstruction test.

**A13 — lint**, exact command and output:

    $ ruff check scripts/p2_diquark_both_eta.py tests/test_p2_diquark_both_eta.py
    All checks passed!
    EXIT=0

Those two files only. Four `E501` line-length errors were found on the
first run and the lines were rewrapped; no rule was disabled, no
`noqa` added, and the script and tests were re-run after rewrapping (same
20 passes, identical artifact).

**Environment.**

    Python              3.11.15
    python -m pytest    9.1.1      (the version A12 mandates)
    pytest on PATH      9.0.2      (not used)
    ruff                0.15.8

Nothing was installed. No environment failure occurred, so Rule 13's
diagnostic order was not exercised.

---

## 12. Commit-message hygiene, and intended final state

Each message inspected before writing (proposed file) and after
(`git log -1 --format='%B'`, read from the object). Scan pattern, case
insensitive: `co-authored-by|claude|session|https?://|generated with|
anthropic`.

    commit 1  fcde56db77508e05de74ce06e2bd51aaba804cfc
      specs/2026-08-10T0245Z_diquark-both-eta.md
      "spec: diquark channel character carrying both eta signs"
      proposed: no match   stored: no match
      trailers suppressed: YES — the default Co-Authored-By and session-URL
      trailers were prevented at authoring time; neither is in the object.

    commit 2  757a0b6d411a83876835127da2e94f47355fbfb8
      reviews/chatgpt/2026-08-10T0245Z_diquark-both-eta.md
      "review: commit the pre-execution review for the diquark both-eta
       derivation"
      proposed: no match   stored: no match
      trailers suppressed: YES — same two.

    commit 3  941aa78036bcdeaaa522147d03056f18dc437b50
      derivations/P2-PHASE-01_diquark_both_eta.md
      "derive: diquark channel character carrying both eta signs"
      proposed: no match   stored: no match
      trailers suppressed: YES — same two.

    commit 4  fd02a2ef51429d76d75ffab231d2e67e0b307f77
      scripts/, results/, tests/ — one work commit
      "compute: the diquark both-eta particle-particle rearrangement"
      proposed: no match   stored: no match
      trailers suppressed: YES — same two.

**Commit order, as A0 requires:** commit 2 precedes commit 3, so the
review was committed before the work it authorises; commit 3 precedes
commit 4, so the derivation note precedes production code per `AGENTS.md`
research rule 3; commits 4 and 5 are separate because this report carries
the step-4 evidence and cannot be part of the commit whose evidence it
records.

**Pre-report head:** `fd02a2ef51429d76d75ffab231d2e67e0b307f77`

**Intended final manifest:** the resolved manifest of §10, seven
additions and zero modifications.

**Intended report commit message:**

    docs: report the diquark both-eta channel-character derivation

    Records A1-A11, A12-pre, A13 and A14. The computation went through and
    did not need the UNRESOLVED outcome.

    Verdict OPPOSITE, and well-defined independently of both remaining
    unfrozen definitions: every coefficient is c = K*eta with K holding
    s_pp and nu, so the ratio is -1 with those symbols still cancelling.
    S, P and T vanish by exact cancellation; V and A survive with opposite
    signs. The absolute attractive/repulsive label per family is NOT
    well-defined and is reported conditional on s_pp and nu.

    Three execution findings. A1a's whole-line delimiter rule returned zero
    matches for BEGIN because the delimiter shared a line with an
    attachment marker -- the fourth distinct failure of the review supply
    protocol, and the first caused by the previous task's fix; the report
    proposes the one paragraph that covers all four and belongs in
    CONVENTIONS.md. My first blocker check was a proxy that returned the
    opposite of the truth, matching the sentence that says nothing fixes
    eta, and my own test caught it. Three of five families vanish, one sign
    error away from the earlier attempt's all-zero failure, which is why
    every decomposition is reconstruction-verified on all 256 components.

    Nothing frozen. P2-PHASE-01 stays PROPOSED.

**A8 re-scan of this report before commit 5**, since the report is an
authored file: all five targets are present and every hit is the scan
describing itself. Per §9, the exact counts are measured against the
committed blob and returned as post-report evidence rather than printed in
the report, because printing them inside the scanned file changes them.

---

## 13. Stops and clarifications

No stop occurred. All findings below are secondary.

**`SPECIFICATION_DEFECT` — one, and it is the fourth instance of the same
thing.**

*A1a's whole-line delimiter rule was inapplicable as written* (§3). It
returned zero matches for the BEGIN literal because the delimiter shared
its line with an attachment marker. Neither of A1a's STOP conditions was
met — the text was present and corresponded — so I applied a derived rule,
asserted it mechanically, and stated it in full rather than stopping.
**The rule I applied is mine and the specification did not authorise it.**
The one-paragraph fix is in §3 and belongs in `CONVENTIONS.md`, not in the
next specification, because the four instances show the protocol is being
re-derived from the last failure once per task.

A secondary observation inside the same finding: the residual one-byte
normalisation the previous report predicted is unchanged, and A1a's
"byte-identical to the text between the delimiters" is still ambiguous by
exactly the newlines adjacent to line-oriented delimiters.

**`OBSERVATION_METHOD_ERROR` — one, mine, caught by my own test.**

*My first blocker check was a proxy for the wrong property and returned
the opposite of the truth* (§5). A regex for `eta = ±1` matched line 336
of the pinned note — inside the sentence "…flips its sign for `eta = -1`.
**Nothing in the frozen material fixes `eta`**" — and would have had me
report that Step 1's STOP fires. The test file caught it before the
artifact was committed. The check now asserts the pinned note's own
statement and *reports* the literal occurrences with their context and
classification rather than deleting them, with a test pinning the
classification. Recorded because a proxy that happens to return the right
answer is invisible; this one is only visible because it was wrong.

**`REPOSITORY_DEFECT` — none reached the threshold of a stop.**

One secondary observation, unchanged from the previous task and repeated
because it now touches this task's own deliverable: **`CONVENTIONS.md`'s
seventeen rules have no structural validator**, and the review supply
protocol of §3 is exactly the kind of thing that belongs there and
currently lives nowhere. This task authorises one new test file and does
not modify `tests/`, so neither is addressed here.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — reported as a scoped
result, not as a stop.**

The computation did not need A6's third outcome, but part of its result
has that character and should be labelled: **the absolute
attractive/repulsive label of the induced `V` and `A` diquarks is not
determinable from the frozen material**, because it is the product of
three signs of which two are unfrozen. And for genuinely complex `nu`
there is no attractive/repulsive label at all, so **no verdict is
licensed in that case** — A6's third outcome applies to it specifically.
What is *not* ambiguous is the same/opposite comparison, and §7.5 keeps
the two apart rather than letting the ambiguity swallow the determinate
part.

**`ENVIRONMENT` — none.** No environment failure occurred, so Rule 13's
diagnostic order was not exercised. Nothing was installed.

**Things I would have specified differently.**

*The review supply protocol should be a repository rule, not a
specification clause.* Four tasks, four failures, each fixed one clause
at a time in a document the next task cannot inherit. §3 gives the
paragraph.

*A2's "quote the search" invites a substring count, which is what went
wrong in §5.* A criterion that asked instead for *the property
established and the sentence that establishes it* would have made my proxy
visibly inadequate at the point of writing it rather than at the point of
testing it. This is the E–L umbrella principle applied to an acceptance
criterion's own wording.

*A8's scan is prose-shaped and should say so.* §9 shows a disclaimer that
the scan cannot see because it lives in a JSON key with underscores. The
right response is not to normalise separators — A8 forbids that, correctly
— but to state that a zero count in code or JSON is weaker evidence than
the same count in prose.

*The specification's §0 wording is worth keeping.* Its instruction that
`eta` entering once means the sign flip is "EXPECTED … WITHIN A FIXED
particle-particle ordering convention" and must be "RE-ESTABLISHED rather
than assumed" is exactly the distinction the result turns on: the flip is
re-derived here from the construction, and the reason the verdict survives
the unfrozen ordering is that the ordering enters as a common factor.
Had the specification simply said "confirm the sign flips", the invariance
argument in §7.5 would have looked like an extra rather than the point.
