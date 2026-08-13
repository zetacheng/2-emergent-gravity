# `P2-PHASE-01` microscopic parameter domain — ADOPTED

**Status: ADOPTED.** Adopted by
`specs/2026-08-12T2258Z_adopt-parameter-domain.md`, under the
pre-execution review committed alongside it. **This artifact is in
force.** It was written for PI confirmation and reviewer scrutiny,
both of which it received; **the sentences that described it as
awaiting them were left behind by an anchored substitution that
repaired only the status line, and are corrected here.**

**It supersedes one artifact.**
`derivations/P2-PHASE-01_microscopic_parameter_domain_DRAFT.md`
deliberately adopted no domain and retained five open items; **it is
now marked SUPERSEDED and is retained as historical evidence.** **This
artifact answers four of those items and leaves one open**, and says
which is which.

**Evidence base:** `1cb5550f6db0c95c7faa9f22b7864ff7d80f9bab`.
Every numerical statement below was read from
`results/P2-PHASE-01/exploratory-scalar-stationary/scalar_stationary.json`
at that revision. **Nothing is quoted from a summary.** Two statements in
§5 were not in any prior artifact and were produced by reading that file
directly.

**Each statement below carries its kind.** `MEASURED` is a number read
from the results file. `PI RULING` is a decision, not a derivation.
`DERIVED` follows from a ruling plus a measurement and is not an
independent choice. `RECOMMENDATION` is the Researcher's and binds
nobody.

**Revision provenance.** This artifact has been reviewed three times and
the reviews are not interchangeable:

    daaaca4e…   first draft; four revisions required
    49be9046…   those four applied. THE SECOND REVIEW RESTATED THE SAME
                FOUR, verbatim, against text that no longer contained
                the phrases it quoted — it had been given the stale
                file. Verified by checking all four quoted phrases
                absent and all seven required changes present.
    this version  the third review's three minor revisions applied

**A review identifies this artifact by NAME, not by digest.** **So a
review of a stale version and a review of a substituted version are both
mechanically undetectable.** One of those has now happened once.
**Quote the digest of the version reviewed**, in the review and in the
covering message, until the practice is written into the conventions.

---

## 1. The coordinate, unchanged

**MEASURED.** The Phase-A freeze gives
`interaction_coordinate_rank = 1`: **`G` is the only scan-eligible
microscopic coordinate.** `HS_scale` and `Fierz_basis` are auxiliary
representation parameters, not coordinates. Source:
`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` §B and §D.

**This artifact does not alter that freeze and adds no coordinate.** The
"parameter domain" is therefore a range in one variable, plus the
treatment of two quantities that are not scanned.

## 2. The evidence this domain is drawn around

**MEASURED**, all from the results file at the pinned revision:

    quadrature       4D product-midpoint BZ grid
    grids            n = 32, 40, 48 × offset shift 0.0, 0.25  (six)
    density          mu = 0.0 throughout
    I0(0)            0.08532107 .. 0.08538273 across the six
    Gc               5.85598486 .. 5.86021696 across the six
    couplings        16 values of G/Gc:
                     0.80 0.90 0.98 0.99 1.00 1.01 1.02 1.05
                     1.10 1.20 1.40 1.60 1.80 2.00 2.50 3.00
    Mhat = 1         crossing at G/Gc = 1.768341 .. 1.769619
    residual         max stationarity residual 1.875e-05
    stationarity     1 = 2 G I0(Mhat); full derivative
                     Mhat * (1/(2G) - I0(Mhat))

**Stable scales only:** `I0(0) ≈ 0.0854`, `Gc ≈ 5.86`, crossing
`≈ 1.77`. Further digits are finite-grid values and must not be quoted
as physics.

## 3. The domain

**ADOPTED.** The domain below was proposed by the Researcher and
**adopted by the PI**; it is the operative content of this artifact
and it binds. **An earlier version of this line read
`RECOMMENDATION, for PI adoption`, which line 28 defines as binding
nobody** — a label left behind when the artifact's status changed,
and the last of four such labels to be corrected.

    coordinate     G, expressed as the dimensionless ratio G/Gc
    range          G/Gc in [0.80, 3.00], CLOSED
                   POSITIVE-COUPLING ENUMERATION WINDOW, provisional
    grid           the sixteen values of §2, PRE-REGISTERED
    density        mu = 0, a FIXED INPUT, not a scan dimension
    lattice a      NOT FIXED. All quantities dimensionless:
                   G/Gc and Mhat = aM. No conversion to physical
                   units is performed or implied at this gate.
    mass Mhat      NOT A COORDINATE. Mhat is solved for at each G;
                   every root RETURNED is in scope, of either sign.

**"Every root returned is in scope" does not establish that every
stationary root in the domain has been found.** **Completeness of the
root enumeration is a separate numerical property, and no artifact
establishes it.** Accepting whatever the solver returns, and the solver
having returned everything there is, are different claims. **If phase
enumeration is later to serve as gate evidence, completeness must be
established, or the gate's answer inherits the solver's blind spots.**

**The restriction to positive `G` is PROVISIONAL.** Until C2 establishes
the sign of `I0(Mhat)` over the stated admissible mass domain,
`[0.80, 3.00]` is **the adopted positive-coupling enumeration window, and
not a proof that negative `G` lies outside the microscopic domain.**
**This artifact carries that limitation itself**; it is not left to be
supplied by whoever quotes the domain.

**The range's upper edge is the edge of computed evidence, not a physical
bound.** **Say so wherever it is quoted.** The earlier draft's
`Mhat = 1` crossing at `G/Gc ≈ 1.77` is **an observation and is NOT
adopted as a bound** — that is `OPEN-PD-1`, answered in the negative.

**The lower edge is likewise the edge of computed evidence.** Nothing
establishes that no admissible phase exists below `G/Gc = 0.80` or above
`3.00`.

## 4. The four open items this closes, and how

**`OPEN-PD-1` — is `Mhat = 1` a domain bound?**
**Answer: NO.** The crossing is an observation with no admissibility
criterion attached. The domain extends past it to `3.00`.

**`OPEN-PD-3` / `OPEN-AC-2` — is the negative-mass branch included?**
**PI RULING (2026-08-12): YES, as a candidate in the enumeration.**

**RECOMMENDATION on how to record that ruling.** Record it as
*included in the enumeration as a candidate*, **not** as *satisfying the
gate's existential quantifier*. The gate asks for a phase that is
**physically admissible and stable**; what exists for this branch is
one-dimensional restricted curvature, and **full condensate-space
stability was not computed and admissibility was not assessed**. **Name
the condition under which the candidate would be upgraded, so that the
upgrade is a measurement and not a second ruling:**

    a full condensate-space Hessian, PLUS the gate's admissibility
    assessment; AND, if "stable" in the gate's question means
    thermodynamic rather than merely local stability, a free-energy or
    effective-potential depth comparison under a COMMON NORMALISATION

**The third clause is not padding.** A positive-definite Hessian
establishes **local** stability only: that the state does not fall apart
under small perturbations. **It does not establish that the state is
selected** over a competing stationary point that sits deeper. **Whoever
reads a positive Hessian and upgrades a candidate to a phase on that
basis has substituted local stability for the property the gate asks
about.**

**The common normalisation this needs is `OPEN-AC-3`, which is open.** So
the upgrade path is currently blocked by an open item, and that should be
visible now rather than discovered later.

**This matters beyond this gate.** `P2-PHASE-01` feeds
`P2-MULTIPHASE-GRAV-01` (SI-2). A phase admitted on restricted evidence
carries that restriction into a gate the programme treats as decisive.

**`OPEN-PD-2` — does the domain extend below `Gc`?**
**Answer: YES. DERIVED, not chosen.** The negative-mass branch's
evidence lies at `G/Gc = 0.80, 0.90, 0.98, 0.99` — all sub-critical.
**Including the branch entails including sub-critical couplings.** This
is a consequence of the ruling above and should not be recorded as an
independent decision.

**`OPEN-PD-5` — treatment of `a`.**
**Answer: not fixed.** Everything stays dimensionless. The question
returns when a physical scale is needed; it is not needed here.

## 5. Two findings made while preparing this artifact

**Neither appears in any prior artifact.** Both were produced by reading
the results file directly rather than the deferred-item summary, which
lists only four sub-critical rows.

### 5a. The negative roots carry no independent positional information

**MEASURED.** Over all six grids and all sixteen couplings the two
non-trivial roots sum to `−8` with `max |sum + 8| = 0.00e+00`.

**The three examples below are from grid `n = 48`, `shift 0.0`; the
five-decimal figures are not grid-independent.** The accounting that
follows is over all six grids.

**The accounting, because ninety is not six times sixteen:**

    96  grid-coupling points   (6 grids × 16 couplings)
    90  points returning a PAIR of non-trivial roots
     6  points returning ONE — the six G/Gc = 1.00 cases, one per grid,
        where the ordinary non-trivial root merges with the trivial one
        at criticality, leaving the complement root (Mhat ~= -8)
        unpaired

**90 pairs = 6 grids × 15 non-critical couplings, none omitted.**
Examples:

    G/Gc = 0.80    -0.41025  and  -7.58975
    G/Gc = 1.20    +0.29056  and  -8.29056
    G/Gc = 3.00    +2.27005  and -10.27005

This is the frozen Wilson-complement relation `I0(Mhat) = I0(-8-Mhat)`.
**The reported complement-root position satisfies
`Mhat_comp = −8 − Mhat_ord` exactly in the stored results.** **Whether
that is an independently recovered root or a constructed companion is
NOT established here and is deferred to C1.**

**The algebraic relation and the numerical provenance are two different
claims and this artifact asserts only the first.** The Wilson-complement
identity is a property of the frozen integral; **that the solver
independently found the second root is a property of the script**, and
no artifact has read the script.

**Consequence for the expectation that working on this branch will reveal
something new: it will not be revealed in the root positions**, which are
algebraically determined by the other branch.

**CAUTION, and this is a check rather than a finding.** A residual of
exactly `0.00e+00` across ninety pairs is a property of the method, not
evidence of physics. **It is consistent with the complement root being
CONSTRUCTED from the relation rather than solved for independently**, and
also with a root-search grid symmetric about `Mhat = −4`. **Which of
these is the case must be read from the script before the branch is given
any weight.** If the complement root is constructed, it is not an
independent numerical result at all.

### 5b. The curvature is NOT mirrored, and that is where any distinction
### between the two reported branches must first be DIAGNOSED

**MEASURED**, grid `n = 48`, shift `0.0`:

    G/Gc    near-origin root   complement root      ratio
    0.80        -0.02259             0.41782        -18.5
    0.99        -0.00086             0.41127       -477.9
    1.01         0.00085             0.41757        492.6
    1.20         0.01267             0.36149         28.5
    2.00         0.02440             0.17919          7.3
    3.00         0.02315             0.10475          4.5

**Below `Gc` the near-origin root lies at NEGATIVE `Mhat`** — at
`G/Gc = 0.80` the two non-trivial roots are `-0.41025` and
`-7.58975`. **It is not the positive-mass condensate branch of
§5c, which does not exist below `Gc`.** The column is named for
position, not for sign, and §5b and §5c do not conflict.

**The positions mirror exactly; the stability measure does not.** The
ratio is not a constant: it diverges near `Gc`, because the ordinary
branch's curvature passes through zero there while the complement's does
not.

**RECOMMENDATION, deliberately weaker than the previous version of this
sentence.** This asymmetry is **an observation, and it is not yet
evidence of branch-specific physics.** **The first question is not "what
new physics is here" but "is this an artifact of how the quantity was
defined".** Four ordinary explanations must be excluded before any
physical reading:

- whether the curvature definition is genuinely covariant at the two
  stationary points;
- whether the second derivative carries a Wilson mass-dependent
  Jacobian or measure contribution that differs between them;
- whether the parameterisation in `Mhat` makes the second derivative
  non-invariant under `Mhat -> -8 - Mhat` by construction;
- whether the potential is symmetric while the derivative with respect
  to the chosen coordinate picks up sign or coordinate effects.

**Only after those are excluded is the asymmetry a candidate for
branch-specific physics.** **Calling it "where the new content lives"
before that is the substitution this programme exists to avoid.**

### 5c. A correction to how this branch was described to the PI

**The Researcher previously told the PI that the negative-mass branch was
the only computable option.** **That was wrong, and the error came from
reading the deferred-item summary instead of the results file.**

**MEASURED**, grid `n = 48`, `shift 0.0`; **the five-decimal figures
are not grid-independent** — `+0.02134` reads `+0.02133` at
`n = 32, shift 0.0` and `+0.02135` at `n = 48, shift 0.25`. **The
qualitative pattern holds on all six.** The ordinary branch shows a
textbook transition:

    G/Gc    trivial root curvature    non-trivial positive root
    0.80           +0.02134           none
    1.00            0.00000           none (critical)
    1.01           -0.00085           Mhat = +0.01627, curvature +0.00085
    1.20           -0.01423           Mhat = +0.29056, curvature +0.01267
    3.00           -0.05691           Mhat = +2.27005, curvature +0.02315

**Stated with the branch qualification it needs:** *below `Gc`, the
ordinary symmetry-breaking scalar branch has no non-trivial positive-mass
condensate solution, while the trivial vacuum remains locally stable
within the restricted scalar ansatz; above `Gc` the trivial vacuum
becomes locally unstable and a positive-mass branch appears and is
locally stable.*

**The unqualified form — "below `Gc` no condensate exists" — is false in
this document's own terms**, because the complement stationary root
exists at every coupling including sub-critical ones, and §4 has just
admitted it as a candidate. **Without the qualification, §5c contradicts
§4.**

So qualified, this is what the gate's question describes, and it requires
no special pleading.

**By contrast the complement branch exists at every coupling with
curvature near `0.4` throughout and does not participate in the
transition at all.** **A branch that neither appears nor disappears at
the critical point does not behave like a condensate.** That is not a
disqualification — it is a description, and the PI's ruling stands — but
it should be visible next to the ruling.

## 6. Pre-registration, and the circularity this domain has

**The range is drawn around the region already computed.** Choosing the
region where evidence exists, and then reporting that evidence was found
there, is circular.

**Two mitigations, both required if this is adopted.**

**Pre-registration.** The range and the sixteen values are frozen by
adoption, **before any enumeration is run**. Any later extension is a
new decision with its own record, and **an extension made after seeing a
result is recorded as such.**

**A non-exclusion statement, quoted wherever the domain is.** *Finding an
admissible phase inside `[0.80, 3.00]` does not establish that none
exists outside it, and does not establish that none outside it is
deeper, more stable, or more admissible.*

## 7. What this artifact does NOT establish

- **It does not establish that any phase is admissible.** It fixes where
  to look.
- **It says nothing about stability in the full condensate space.** All
  curvature quoted is one-dimensional and restricted to the uniform
  scalar ansatz, per the results file's own limitations field.
- **It covers `mu = 0` only.** `P2-PHASE-01`'s scope in `GATES.md`
  includes finite density. **Any SI-1 answer produced under this domain
  is an answer about the `mu = 0` slice** and must be stated that way.
- **It does not settle the non-scalar channels.** `OPEN-AC-1` — the
  P/V/A/T mean-field construction — remains open and blocks any
  enumeration beyond the scalar route. **It does not block the scalar
  route, which is the PI's chosen route.**
- **It does not touch the exclusions**: the quarantined `−3.2(5)`, the
  suspended `P2-BETAV-CIRC-01` result, and the historical Finding 5
  extraction remain excluded.

**Adoption freezes the enumeration window and the treatment of
inputs. It does not certify root completeness, full-space stability,
thermodynamic dominance, negative-`G` exclusion, or finite-density
coverage.**

## 8. Checks to commission with, or before, the first enumeration

**RECOMMENDATION.** All three are cheap and all three are things this
artifact assumes rather than knows.

**C1 — Is the complement root solved for, or constructed?** Read the
generating script. §5a cannot be interpreted until this is answered.

**C2 — Does negative `G` admit any non-trivial root?** Stationarity is
`1 = 2 G I0(Mhat)`. Every `I0` measured in the results file is
positive. **The brackets, with their scope stated:** the root-level
`I0` values span `0.0284403` to `0.1067275` over all six grids;
on the single grid `n = 48`, `shift 0.0` they span `0.0284534` to
`0.1067006`; across every `I0`-valued field in the file the upper
bound reaches `0.1439968`. **An earlier version of this artifact
quoted the single-grid bracket as if it covered the file.**

**Partial negative-mass evidence already exists and was overlooked.**
The file's `symmetry.sign_pairs` evaluates `I0` at
`Mhat = -0.1, -0.5, -1.0`, giving `0.09046`, `0.11173`, `0.14400` —
**all positive, at negative mass.** **So it is not true that no
measurement has tested the sign there.** What has not been
established is **global** non-negativity over the admissible mass
domain, and a negative `G` requires `I0(Mhat) < 0` somewhere in it. If `I0` is
positive everywhere, the negative-`G` half-line is empty and the domain's
restriction to positive `G` would be derived rather than assumed.

**Determine from the analytic definition whether `I0(Mhat)` is strictly
non-negative over the admissible mass domain. If that is not manifest
from the integrand, commission a bounded numerical sign check over a
stated interval, and state the interval.**

**A single evaluation cannot discharge this and must not be offered as if
it could.** An earlier version of this artifact called C2 "one
evaluation"; **that was wrong.** One evaluation establishes the sign of
`I0` at one mass, and **"positive somewhere" and "positive everywhere"
are different claims.** **Until C2 is discharged in one of the two forms
above, the restriction to positive `G` is an ASSUMPTION and is labelled
as one wherever the domain is quoted.**

**C3 — Is the curvature asymmetry physical, or induced by the chosen
coordinate or the second-derivative definition?** §5b lists the four
ordinary explanations to exclude first. **This is prior-neutral by
construction**, and that is the point: the earlier form of this check
asked what sets the scale, which presumes there is a scale to set.

## 9. Remaining OPEN

**`OPEN-PD-4` — finite density.** `mu` is fixed at `0` by §3, which is a
decision about **this** enumeration and not an answer to the open item.
**Whether `mu` becomes a scan dimension, and over what range, is
undecided**, and no evidence at non-zero `mu` exists.

**`OPEN-AC-1` — the P/V/A/T construction.** Unchanged and untouched.

**`OPEN-AC-4` — exact/remnant symmetry and Goldstone implications.**
**REMAINS OPEN.** **An earlier version of this artifact omitted it
entirely.** It bears on stability and therefore on any later upgrade
of a candidate to a phase; **it is not a peripheral item and it is
not addressed here.**

**`OPEN-AC-5` — whether `Mhat = 1` is an admissibility bound.**
**CLOSED, by the same answer that closes `OPEN-PD-1`: NO.** The two
are the same question recorded in two artifacts. **An earlier
version of this one answered `OPEN-PD-1` and was silent on its
twin**, which is how a reader of the admissibility contract would
have gone on believing the question undecided.

**`OPEN-AC-3` — cross-family comparison.** Unchanged and untouched. Note
that comparing the two branches' depths, as distinct from their
curvatures, would need the common normalisation this item covers.
