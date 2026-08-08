# Task specification — normalisation audit: reconcile `G_ω` with the derived vector coefficient

Specification evidence base: `eb88a2c9174cfda746c266924e741a6f88134234`
Related branch, not merged: `gate/p2-channel-character` @
`cb604a4e3a96f9120787a685120f205d8e4c7c88`

Classification: **MATERIAL**. Branch only; integration is a separate
authorization.

**This is an evidence-production task, not an investigation.** Its
output is one row of the evidence table that
`derivations/CANONICAL_INTERACTION.md` requires for its own
ratification and which has never been produced.

---

## 0. Why this exists, and what it is not

The channel-character derivation reported the induced vector singlet
coefficient as `−G/(2N)` for `(ψ̄γ_μψ)²`, and flagged that
`CANONICAL_INTERACTION.md` records a Paper-3 claim of `G_ω = −G/N`.
**Taken at face value that is a factor of two.**

**But `CANONICAL_INTERACTION.md` already anticipated exactly this
check.** It states:

> the executor must generate and attach an evidence table on a clean
> clone: … (normalizations match → exact quoted definitions) … The
> Discriminator's approval of this document is conditional on that
> evidence table; **self-description is not evidence.**

That table has never been produced, which is why the document carries a
`DRAFT v0.5 — ratification candidate` banner. **The banner is accurate,
not stale.** This task produces the normalisation row.

**Our own reading, reported as a QUESTION and not an answer.** Paper 3's
note appears to state `L_V = (G_V/2) J_μ J^μ` — a factor of one half in
the current normalisation — which would make `G_ω = 2 × (−G/(2N)) =
−G/N` consistent rather than contradictory. **Verify or refute this
independently. If your computation disagrees, your computation is the
evidence.**

**What this task must NOT do:** it does not ratify
`CANONICAL_INTERACTION.md`, does not remove its banner, does not modify
any Paper-3 content, and does not decide whether the remaining rows of
that evidence table are satisfied. **One row, recorded.**

## 1. Cross-repository reading, and its limits

`AGENTS.md` forbids MERGING content from another paper repository. **It
does not forbid reading one**, and the established pattern is to pin an
external evidence base.

    External evidence base: zetacheng/3-vector-sector
                            8c363ef08368f5c022278ea5f36e01496be3d5ca

    derivations/u3-fierz/u3_fierz.md
    6784d51a5a8d5f8b70b55213e4bf9b3eb50fc8c331397e80a239d16285d58f49

**Read-only.** Nothing in Paper 3 is modified, and no Paper-3 file is
copied into this repository. **Quote what you need; do not import.**

**If the pinned Paper-3 revision is unreachable, report
`UNAVAILABLE EVIDENCE` and stop — not `ABSENT CONTENT`.** They are
different findings: one says the evidence could not be fetched, the
other says it does not exist.

## 2. What to establish

**A — The two operator normalisations, quoted exactly.**

- From Paper 3 at the pinned revision: the exact definition under which
  `G_ω` is stated — the operator, the current definition, and any
  factor of one half or other prefactor. **Quote the line.**
- From this repository: the normalisation under which
  `results/P2-PHASE-01/channel-character/channel_character.json` reports
  its vector coefficient. **Quote the definition it declares.**

**B — The reconciliation, computed rather than asserted.** Convert one
to the other symbolically, keeping `N` general, and report whether the
two values agree under that conversion. **Show the conversion factor and
where it comes from.**

**Then reach ONE of these three verdicts, and state which:**

    NORMALISATION MAPPING   the two agree once the declared
                            normalisations are accounted for; record
                            the mapping
    REPOSITORY_DEFECT       the same operator under the same
                            normalisation carries two different values
    UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY
                            one or both normalisations are not stated
                            precisely enough to compare

**If the verdict is `REPOSITORY_DEFECT`, STOP and report.** A Paper-3
claim recorded as `VERIFIED` with a factor-of-two error would be a
serious finding, and it must not be quietly folded into a mapping note.
**Do not adjust either value to make them agree.**

**C — Independent recomputation, not transcription.** Recompute the
vector singlet coefficient yourself from the frozen canonical
interaction and the verified Fierz matrix, under the normalisation you
will report it in. **Agreement with the channel-character result is
corroboration; disagreement is a finding about that result and a STOP.**

**D — What this row does and does not close.** State explicitly that the
remaining rows of `CANONICAL_INTERACTION.md`'s evidence requirement —
starting-interaction match, claim-status registry, test count,
convention-compatibility table — **are not addressed here**, and that
the document's banner therefore stands.

## 3. Acceptance criteria

**A0 — Commit order.** Commit 1 is this specification under `specs/`.
Commit 2 is the derivation note under `derivations/`, before any
production code. Commits 3+ carry script, results, test and report.
**Parent 1 of any commit is whatever you are standing on.**

**A1 — Pinned inputs**, verified before use; any mismatch is a STOP:

    derivations/CANONICAL_INTERACTION.md
    27daae02ef0921602947cb25bfc7989031c8849172d0ea190cdcf1753f348a81

    derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md
    fe68b9c645c80287afa45288d7c3e0490328b76663aafbe78af20dfc12a4e67a

    results/P2-CHANNEL-FREEZE/fierz_matrix.json
    5085463db1b3a21c0ea1ad2d0b0cdb5da3abb5fd8a78e9623c6b6942879667a9

    derivations/P2-PHASE-01_fierz_sign_addendum.md
    a0553b8a79cfcd521620448f7d1d6928475573e751dd404698adcd48ad6871df

plus the external pin of §1. **The channel-character branch is NOT
pinned as an input** — it is unmerged, and C requires you to recompute
rather than to consume it. You may compare against it after computing.

**A2 — Both normalisations quoted verbatim**, each with its source path
and, for Paper 3, its line reference at the pinned revision.

**A3 — The conversion computed symbolically**, `N` general, with the
factor and its origin shown.

**A4 — One of the three verdicts**, stated explicitly, with the evidence
that selects it.

**A5 — Independent recomputation** agreeing or disagreeing with the
channel-character result, reported either way.

**A6 — Scope boundary stated:** the other evidence-table rows are not
addressed; the banner stands. **Do not modify
`CANONICAL_INTERACTION.md`.**

**A7 — Nothing pre-existing disturbed.** No gate, gate status, verdict,
artifact digest, hash-pinned artifact, pre-existing test, `GATES.md`,
`CONVENTIONS.md`, `AGENTS.md`, or `pyproject.toml` is modified. Verify
`GATES.md`'s blob from the object.

**A8 — Scope**, five additions; you choose none of the paths except the
`{HHMM}Z` token, fixed once by commit 1 and reused:

    specs/2026-08-08T{HHMM}Z_normalisation-audit.md
    derivations/P2-NORMALISATION-AUDIT_g_omega.md
    scripts/p2_normalisation_audit.py
    results/P2-PHASE-01/normalisation-audit/g_omega_audit.json
    reports/2026-08-08T{HHMM}Z_normalisation-audit.md

**Final base-to-head scope: 5 additions, 0 modifications.** **No new
test file is required**: this task computes one conversion and quotes
two definitions, and the recomputation of C is itself the check. **If
you judge a test worth adding, say so in the report rather than adding
one outside this manifest.**

**A9 — Validators, exit status 0**, run individually with
`python -m pytest <path>`: `tests/test_repository_structure.py`,
`tests/test_si1_governance.py`, `tests/test_gate_anchors.py`,
`tests/test_governance_tools.py`. **A9-pre** at the pre-report head goes
in the report; **A9-final** at the pushed head is post-report evidence.

**A10 — Lint clean** with `ruff check` on the files you author.

**A11 — Branch only.** Verify `refs/remotes/origin/main` and remote
`refs/heads/main` both resolve to `eb88a2c9…`; create the branch from
that commit; move no `main` ref. **Local `main` is stale by design.**
Report all three. Push the task branch only. **Delete no branch.**

## 4. Evidence layering

**Committed report:** A1–A8, A9-pre, A10, earlier commit SHAs and
messages, the pre-report head, the intended final manifest, and the
intended report commit message with its authoring-time trailer
suppression.

**Post-report evidence, returned to the Reviewer and NOT written back:**
the final scope check at the pushed head, A9-final, the push, the report
commit's stored message read back from the object, and ancestry
confirmation.

## 5. Invariants and prohibitions

- Executor-writable: the five paths of A8 only.
- **Do not modify anything in Paper 3**, and do not copy any Paper-3
  file into this repository.
- **Do not modify `CANONICAL_INTERACTION.md`**, and do not remove or
  amend its banner.
- **Do not adjust either coefficient to make them agree.**
- **Do not ratify anything.** This produces evidence; ratification is
  the PI's.
- Do not consume the quarantined `−3.2(5)`, the suspended
  `P2-BETAV-CIRC-01` result, or the historical Finding 5 extraction.
  **List every repository input you actually read, by path**, across
  both repositories.
- Commit-message hygiene: inspect the proposed message before each
  commit and the stored message after; permit no `Co-Authored-By`, no
  session identifier or URL, no tool attribution. **Report per commit
  whether any trailer was suppressed and which.**
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: use `fix/normalisation-audit-g-omega`.
- Environment: rule 13's diagnostic order applies. **Do not install
  anything.**
- If any instruction here is inconsistent with a repository rule or with
  another instruction, stop and report; do not decide which prevails.

## 6. Report contract

- raw output for A1–A10, scope-checker JSON verbatim including
  `observed_operations`;
- both normalisations quoted, with sources;
- the conversion, symbolically, with its factor;
- the verdict and the evidence selecting it;
- the independent recomputation, and its agreement or disagreement with
  the channel-character result;
- **what this row does NOT close**, listed;
- **whether reading a second repository raised any difficulty this
  programme has not met before** — cross-repository evidence is rare
  here and the procedure is not well tested;
- a **Stops and clarifications** section using the five primary
  categories — `SPECIFICATION_DEFECT`, `ENVIRONMENT`,
  `OBSERVATION_METHOD_ERROR`, `REPOSITORY_DEFECT`,
  `UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY` — one primary per stop,
  secondary findings separate, included even if there were none;
- anything ambiguous, unsatisfiable, or that you would have specified
  differently.
