# Execution report — `P2-RECON-EXT-01`

    OUTCOME     MEASURED. No abort fired. No landing; main unmoved.
                The discarded external components are the same order of
                magnitude as the retained ones. No criterion is set and
                none may be read out of this.

**Specification:** `specs/2026-08-19T0649Z_recon-ext-01-discarded-space.md`
**Review:** `reviews/chatgpt/2026-08-19T0649Z_recon-ext-01-discarded-space.md`
**Artifact:** `derivations/P2-RECON-EXT-01_discarded-external-space.md`, 471 lines
**Diagnostic:** `scripts/diagnostics/ext01_discarded_external_space.py`
**Evidence base:** `968e726a5a4322eecf4254ff69b25832f263c155`

**Measurement head: commit 5, `076934aa168dc4f45e9cf6f33da9b57610fa42e1`.**
`C9` is labelled INTENDED and measured in the post-report layer.

---

## §0 — Binding SHA (MEASURED, no A1 abort)

    observed refs/remotes/origin/main   968e726a5a4322eecf4254ff69b25832f263c155
    §0 declared evidence base           968e726a5a4322eecf4254ff69b25832f263c155

**Equal.**

**Review binding (Rule 18, Amendment N).** Field present, once, populated —
checked before its value.

    sha256 of the specification bytes as committed
      e0effac3ac0584c36f225542ced16fa5a72ec07f08366ed6b924c3784879c7cd
    the review's bound SHA
      e0effac3ac0584c36f225542ced16fa5a72ec07f08366ed6b924c3784879c7cd

**MATCH.** Verdict `APPROVE FOR EXECUTION`.

---

## Environment (MEASURED)

**Amendment D step 0.** Ref reads in `/home/user/2-emergent-gravity`; all
commits and the diagnostic run in the linked worktree `…/scratchpad/rext`,
created at the evidence base.

**Rule 13's diagnostic order.** Not shallow; 423 commits on HEAD, 576 across
all refs; Python 3.11.15; pytest 9.1.1; numpy 2.4.6; sympy 1.14.0; ruff 0.15.8;
**`scipy` ABSENT.** **No environment failure occurred, so neither of Rule 13's
two diagnostic orders was exercised.** The diagnostic imports `numpy` only;
`scipy` is not required by it.

---

## The three answers

### Q1 — what the projection discards

    full space  =  retained  +  discarded
        10      =      5     +      5

**Retained:** the symmetric traceless tensor of the 3-space orthogonal to
`q ∥ e₀`. **Discarded:** the four components carrying the axis index `0`
(`h00`, `(0,1)`, `(0,2)`, `(0,3)`) and **the spatial trace**
`(h11 + h22 + h33)/√3`.

**The basis is orthonormal to machine precision and spans the full space** —
Gram deviation `2.22e-16`, rank 10 — verified numerically, not asserted. **The
unit-Frobenius normalisation is the repository's own**, read off from
`TT_RECIPES`' comment calling each recipe "a unit-normalized tensor" and
confirmed against all three recipe shapes.

### Q2 — the magnitude

**Reported as measured, in the direction it falls.**

    component  q² coefficient        share    exponent
    R1         +2.223856432e-02    +28.80%     1.9887
    R2         +2.223856432e-02    +28.80%     1.9887
    R3         +2.180202143e-02    +28.24%     1.9894
    R4         +2.180202143e-02    +28.24%     1.9894
    R5         +2.180202143e-02    +28.24%     1.9894
    D1         -2.215669317e-02    -28.69%     1.9982
    D2         -7.265655290e-03     -9.41%     1.9940
    D3         -7.265655290e-03     -9.41%     1.9940
    D4         -7.265655290e-03     -9.41%     1.9940
    D5         +1.128540201e-02    +14.62%     1.9898

    sum all ten          +7.721493588e-02
    sum retained         +1.098831929e-01     +142.31%
    sum discarded        -3.266825703e-02      -42.31%
    mean retained        +2.197663858e-02
    |dis| / |ret|         0.297300
    largest |D| / mean R  1.008193

**`D1` alone is 1.008 times the mean retained component.** The discarded space
is not a small correction at this parameter point.

**Three caveats stated with the numbers and not after them.** The shares are
**signed** and are not bounded in `[0,1]` — the two groups carry opposite signs
and the denominator is their sum, which is why `+142%` and `−42%` appear; that
is what a signed decomposition with cancellation produces, not an error. Every
component scales as `q²` (exponents in `[1.9887, 1.9982]`), so the coefficient
is a meaningful extraction for all ten. And the symmetry structure holds
exactly — `R1 = R2`, `R3 = R4 = R5`, `D2 = D3 = D4` to every printed digit,
with nothing in the code enforcing it.

**Cross-check, computed after the parameters were fixed.** The mean over the
five retained components is `+2.1977e-02`; `CIRC-01:45` states its `total` row
as `≈ +2.20e-2` with exponent `≈ 1.99`. **They agree to the precision `CIRC-01`
states.** Reported as validation that the diagnostic reproduces the reference
object, not as a new result.

### Q3 — by what authority

**The projection arrives with the manuscript and no document records a
selection.**

**MEASURED:** the first commit introducing the string `axis-TT` anywhere is
`f95f2eb`, 2026-07-17, *"docs: import Paper 2 v2.15 and redo the comparison
against the source"* — **three days before `TT_RECIPES` first appears**
(`fb1da32`, 2026-07-20). A search of every `axis-TT` line in the repository's
markdown for selection language — `because`, `chosen`, `selected`, `inherit`,
`follows the paper`, `paper's definition` — **returns no lines.**

**One location supplies a ground of the first kind:**
`scripts/recovered_2026/mlog_coeff.py:2-13`, which grounds why the `m² ln m²`
part is universal and why the seagull and cosmological terms drop. **It does
not state why the transverse-traceless space is the right space to project onto
rather than a larger one.**

**Two supply a ground of a second kind — definitional inheritance.**
`GATES.md:280-281` and `P2-NORM-01:35-37` record that the axis-TT slope **is
the manuscript's definition of `Z`**. That is a ground for using the projection
— it is what the quantity being reproduced means — **and it is not a derivation
that the discarded space may be dropped.** The artifact keeps those two claims
apart.

**The remainder state only the choice**, including
`RECON-01_cleanroom_reconstruction.md:27-28`, which is the strongest of them and
still constrains only *how* the projection is used (fixed, identical for every
`k`), not *why this one*.

**This is a documentary finding, not a criticism.** A reproduction inheriting
a definition from the object it reproduces is ordinary. Whether it should be
re-derived is recorded open and is PI ruling 4's territory.

---

## §2 — Measurements

**M1** — the definition located and quoted at
`scripts/recovered_2026/mlog_coeff.py:21-31`; five retained components listed
with the normalisation convention derived from the file's own comment. **No
`A2` abort.**

**M2** — the full space located at `scripts/recovered_2026/seagull_check.py:49`,
`PAIRS`, ten components; the decomposition `10 = 5 + 5` stated with the five
discarded components enumerated; the arithmetic checked numerically.

**M3** — **the repository states no spin correspondence, and none was
supplied.** `helicity` returns 0 files. The one line relating `axis-TT` to a
spin label is `specs/…pole-b0-milestone-scope.md:191`, and it is a **warning
against** the identification: *"Distinguish an axis-TT projection from a
Barnes–Rivers spin decomposition if both appear."* `M3`'s second form is the
measured one and `§8` of the specification makes it a completed measurement.

**M4** — **pre-registered and committed at `9cb63733`, before the diagnostic
script existed.** `k = 1`, `n = 12`, `m = 0.3`, q-grid `[0.10, 0.16, 0.22,
0.28]`, fit `Π = A + Bq² + Cq⁴`, `EPSF = 1e-3` read from `proca_loop.EPSF`,
`q ∥ e₀`. **The parameters match `CIRC-01`'s** so the two decompositions are
comparable; they were not chosen after seeing anything.

**M5** — the table above, all ten components, none omitted.

**M6** — provenance recorded, including the target-bearing import.

**M7** — the documentary sweep, classified ground-versus-choice, with the
earliest location by commit date and the finding that no location records a
selector.

---

## §3 — Computation constraints

**K1** — no `β` quantity of any species, no ratio of two such, and nothing the
frozen anchor ranges over was computed, printed, logged or stored. The object
computed is the bubble's `q²` coefficient per external component.

**K2** — no scan over the determinant power. **And this is stronger than
compliance by restraint:** the call signatures were inspected and **none of
`component_bubble`, `derivsV`, `G_flat`, `avec` or `kin_form` takes that power
as an argument.** The power enters `Γ_k` downstream of the bubble. `§4`
pre-registered `k = 1` rather than assuming this, and `§6.3` records it as a
measurement of the code path.

**K3** — no target was read from `GATES.md` into any script, test or output.
The diagnostic does not open `GATES.md`.

**K4** — not invoked. **No computation was withheld**, and no item is recorded
`UNMEASURED`.

---

## §6 — Acceptance criteria

    C1   PASS   M1 and M2 present with the decomposition arithmetic shown:
                5 retained + 5 discarded = 10 = the ten PAIRS of the full
                space. Checked numerically — Gram max deviation from identity
                2.220446049250313e-16, orthonormal True, rank 10 — not
                asserted.
    C2   PASS   M3 present in its second form: no correspondence is stated by
                the repository, with the search shown and the one near-hit
                read and identified as a warning against the identification.
                §8 of the specification makes this a completed measurement.
    C3   PASS   Verified by commit order, independently of what either commit
                claims. The pre-registration is commit 3, 9cb63733; the
                diagnostic script is commit 4, f43242cd; the result is commit
                5, 076934aa. The prereg commit's §5 reads "NOT YET MEASURED"
                and its §4 carries the full parameter list — both confirmed
                by reading that commit's blob, not the working tree.
    C4   PASS   M5 reports every one of D1-D5 enumerated in M2, and all five
                retained components. Ten rows, no omission.
    C5   PASS   M6 lists every import with its path and target status:
                proca_loop, mlog_coeff and seagull_check under
                scripts/recovered_2026/, numpy from site-packages, four
                standard-library modules. proca_loop is recorded as
                target-bearing with the location of the line and a statement
                of what is used from it.
    C6   PASS   M7 records the gate location (GATES.md:739) and classifies
                every location as stating a ground or stating only the
                choice, in two separately headed subsections.
    C7   PASS   Search extent as §6 C7 defines it: the measurement artifact,
                the one added script, and the one output it emitted. `(k+2)`,
                `k+2`, `beta_V`, `beta_B` all return 0 in all three. The
                signed target literal returns 0 in all three under both minus
                encodings. `β_V`/`β_B` return one artifact line — §9's
                negation "It produces no β_V, no β_B, and no ratio of them" —
                which is a required non-establishment statement, not a value.
                **The specification and its review were excluded from this
                check, as C7 directs.**
    C8   PASS   The §5.7 statement of non-establishment is present as the
                artifact's §9, naming all three required items: one k and no
                k-dependence; no criterion; a magnitude is not a judgement of
                relevance. The artifact contains no recommendation and no
                acceptability judgement — verified by reading, and §5.3
                deliberately states the caveats without stating whether the
                measured fraction is acceptable.
    C9   INTENDED — measured in the post-report layer.
    C10  PASS   Both blobs under scripts/recon2026/ unchanged, ids recorded
                below. The directory has two files at the base and two at the
                head; nothing was added to it.

### C10 — `scripts/recon2026/` blob ids observed

    scripts/recon2026/proca_curved.py      03f46905e5798fb7f6880dfae9ed5a1931be895b
    scripts/recon2026/flat_validation.py   6b21f9d6db67641ec7de31b7006884b617de3e8c

**Identical at `968e726a` and at commit 5. The clean-room construction is
untouched.**

---

## §7 — Substring hazards, and how each was handled

**`TT` matches `tt_check` and `TT_RECIPES`.** The artifact never uses one token
for both: `tt_check.py` does not appear in it at all, and `TT_RECIPES` is
always written in full with its file and line.

**`trace` matches `traceless`, and they are different components here.** This
distinction is load-bearing rather than cosmetic: **`D5` is the spatial trace
and is discarded; `R1` and `R2` are the two traceless diagonal combinations and
are retained.** A check that conflated them would have moved a component across
the decomposition. The artifact states the distinction at `§2.1` and never
counts either token.

**`projection` does not match `projector`.** The artifact measures the
projection; the word `projector` appears in the repository for unrelated
rank-1 objects and was not searched as a proxy.

**`k`** — three uses are written alike. The artifact states which is meant at
each: the determinant power in `§4` and `§6.3`; lattice momentum components in
the code's `k0`, `kk`, `K1`; and the anchor's `k`, which the artifact does not
write at all.

**`external`** — the external index space and an external digest are unrelated
uses in this repository. Only the first appears here, and the artifact's title
and every section heading say "external index space" or "external component"
rather than the bare word.

---

## §1b — Non-objectives, all honoured

**No `β_V`, `β_B`, ratio, or anchor-ranging quantity was computed** — `C7`
records the search. **No `k`-scan and no `k`-dependence of anything** — and
`§6.3` shows there was nothing to scan. **Nothing was begun, scoped or
contributed to `RECON-01b`**; `scripts/recon2026/` is byte-identical and the
diagnostic sits under `scripts/diagnostics/` outside it. **Components 5 and 9
were not adjudicated** — the artifact records the `TT_RECIPES` question's
documentary state at `§7` and `§8.2` and stops. **No kill criterion, threshold
or acceptance band was set**, and `§4` states explicitly that none will be
added later. **Nothing was merged and `main` did not move.**

---

## Stops and clarifications

**`SPECIFICATION_DEFECT`** — **none.** Two provisions did real work. `C7`'s
explicit search extent is what makes the criterion satisfiable: the
specification has to name what it forbids, and a check covering the
specification would fail on its own governance text — the previous revision's
defect, and the review records it as resolved. And `M4`'s requirement that the
pre-registration commit *precede* the result commit is checkable by commit
order rather than by assertion, which is why `C3` could be verified against the
`9cb63733` blob rather than against a claim.

**`ENVIRONMENT`** — `scipy` absent for the eighteenth consecutive task; the
diagnostic imports `numpy` only and nothing failed. **No environment failure
occurred, so neither of Rule 13's two diagnostic orders was exercised.**

**`OBSERVATION_METHOD_ERROR`** — **none, and one avoided by construction.** The
`trace`/`traceless` collision `§7` names would have moved `D5` from the
discarded set to the retained set if the two had been conflated — a one-token
error that would have changed the decomposition from `5 + 5` to `4 + 6` and
removed the second-largest discarded contribution from the measurement. The
components were built from explicit pair lists and checked for orthonormality
against each other, so the error had no route in.

**`REPOSITORY_DEFECT`** — **none found**, and one observation that is not one.
`M7` establishes that the axis-TT projection entered the repository with the
imported manuscript and that no document records a selection or a selector.
**That is a gap in the documentary record, not a defect in the science**, and
it is exactly what `Q3` was written to measure. **It is recorded, not
classified**, because classifying it would be the adjudication PI ruling 4
reserves.

**`UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY`** — **six, all recorded in the
artifact's `§8` as open.** Whether the retained space is complete for the
quantity extracted; whether the projection should be re-derived rather than
inherited; whether a spin correspondence exists to be stated; whether the `q²`
scaling holds away from this parameter point; **what the ten-component sum
means as a normaliser** — a different denominator would give different-looking
shares from the same measurement, which is why `§5.1`'s raw coefficients are
given; and **why `D1` and the retained components are opposite in sign**, which
the measurement records without offering a mechanism.

**The last two matter for how this result should be read**, and neither is
settled here.

---

## Layering

**Everything above is measured at commit 5,
`076934aa168dc4f45e9cf6f33da9b57610fa42e1`**, except `C9`, labelled INTENDED.

**Returned to the Reviewer in chat, not written back:** `C9` as measured — the
diff against the base, the push exit status, the remote read-back, and
confirmation that `main` is still `968e726a`.

**This task performs no landing.** Integration of this branch, if the PI
directs it, is a separate specification under the `science/*` clause.
