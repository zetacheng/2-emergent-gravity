# Review — P2-BRANCHING-SCIENCE-01

**Reviewed artifact:** `P2-BRANCHING-SCIENCE-01(1).md`  
**Reviewed specification SHA-256:** `1ead5cd5dcfe6b18508dfafb532ca343f97d170152e5c2526451a111db6f593a`  
**Review date:** 2026-08-18  
**Review verdict:** `APPROVE FOR EXECUTION`

## 1. Governance purpose — PASS

The specification correctly addresses the policy gap exposed by the POLE-B0 integration abort: `science/*` is already an operationally important branch class, but it is absent from the formal branch taxonomy and has no policy-level merge-mode rule.

The task therefore repairs the governance layer rather than issuing another one-off integration exception.

## 2. `science/*` taxonomy — PASS

The revised specification correctly adds a `science/<scientific-task>` branch class to the formal branching taxonomy.

This aligns the documented policy with repository practice and prevents future integration tasks from having to infer authority from precedent.

## 3. Merge mode — PASS

The specification correctly establishes a durable integration rule for completed and Reviewer-approved `science/*` task branches:

- integrate the pinned remote source tip into a dedicated integration branch using a non-fast-forward merge;
- prohibit squash and rebase integration;
- preserve the source branch tip as a merge parent;
- advance authoritative `main` only by fast-forward from the reviewed evidence base to the completed integration head.

This is appropriate for the repository's evidence-oriented workflow because it preserves task identity, source ancestry, review provenance, and the scientific branch tip.

## 4. Bootstrap handling — PASS

The specification correctly avoids circular governance.

This task cannot delegate its own merge mode to the very policy amendment it is creating.

Accordingly, the task's own integration mechanics are explicitly authorized in the specification itself, while the new policy governs future `science/*` integrations prospectively.

## 5. Authoritative frozen manifest — PASS

The previous A5/C8 contradiction is resolved.

The specification now defines one authoritative frozen manifest and requires all relevant scope checks to use that same manifest.

The manifest includes:

- `docs/BRANCHING_POLICY.md`;
- `CONVENTIONS.md`;
- the existing repository register selected for the class-level governance-gap record; and
- this task's authorized specification, review, and report artifacts.

The task's own identity artifacts therefore no longer trigger a false scope abort.

## 6. Retrospective governance-gap wording — PASS

The revised wording correctly states the historical boundary as:

`Through pre-amendment main 11af14a7...`

rather than implying that the old main tip itself was the amendment's effective commit.

The specification explicitly distinguishes:

- the pre-amendment repository state; from
- the prospective policy that will begin with this amendment.

This provides accurate governance provenance without rewriting history.

## 7. Historical `science/*` branches — PASS

The specification correctly treats the pre-existing landed `science/*` history as one class-level retrospective governance gap.

It does **not** require 37 individual retroactive approvals, rewrites, or re-merges.

Historical accepted scientific landings remain accepted.

The amendment is prospective and records the prior policy omission rather than attempting to manufacture authority retroactively.

## 8. Governance-gap register selection — PASS

The specification appropriately requires the executor to inspect the repository's existing governance/debt registers and use an existing location whose semantics actually fit the class-level policy gap.

The executor may not invent new register vocabulary or silently force the item into a semantically unsuitable register.

If no appropriate existing register exists, the task must return that finding rather than creating new governance semantics without authorization.

## 9. Push-scope policy — PASS

The revised policy correctly places ref-level integration mechanics in the branching/governance layer rather than in `AGENTS.md`.

For future `science/*` integrations, the allowed landing behavior is defined in the branch policy, with `CONVENTIONS.md` acting only as the execution-discipline cross-reference.

This maintains a clearer single source of truth.

## 10. `AGENTS.md` boundary — PASS

The specification correctly leaves `AGENTS.md` unchanged.

`AGENTS.md` governs roles, authority, review requirements, and executor scope.

Branch-class merge mode and allowed-ref mechanics belong in the branching/integration policy rather than the role model.

## 11. SciPy issue excluded — PASS

The task correctly excludes the SciPy/environment documentation question from this amendment.

The earlier apparent `pyproject.toml` versus `proca_curved.py` contradiction was not reproduced as stated.

The remaining distinction between project dependencies and the declared minimum execution environment is a separate documentation/environment issue and should not be opportunistically folded into this branch-policy repair.

## 12. POLE-B0 register issue excluded — PASS

The task correctly does not use this governance amendment to decide where the POLE-B0 `construction not yet scoped` item belongs.

That question remains separate from the `science/*` branch-policy gap.

The amendment therefore avoids broadening its scope into scientific programme-design governance.

## 13. No POLE-B0 integration — PASS

The specification does not merge or land the POLE-B0 scientific branch.

Its purpose is to repair the policy authority needed for a later re-issued POLE-B0 integration task.

This preserves the separation between governance repair and scientific-result landing.

## 14. Prospective effect — PASS

The amendment is correctly prospective.

Its scientific effect is governance only:

- future `science/*` integrations receive a formal merge-mode rule;
- source provenance is preserved by merge-parent structure;
- unrelated refs remain outside the integration task's authority;
- historical science landings are not reinterpreted.

No scientific gate or manuscript claim changes because of this task.

## 15. Internal consistency — PASS

The revised specification no longer contains the manifest contradiction or the ambiguous retrospective boundary identified in the previous review.

The bootstrap mechanics, scope, historical-gap treatment, policy amendment, register-selection rule, and exclusions are mutually consistent.

No STOP-level specification defect remains.

## Final verdict

**`APPROVE FOR EXECUTION`**

`P2-BRANCHING-SCIENCE-01(1).md` may be executed.

This approval is bound exclusively to the exact uploaded specification bytes with SHA-256:

`1ead5cd5dcfe6b18508dfafb532ca343f97d170152e5c2526451a111db6f593a`

The central governance result to preserve is:

**`science/*` becomes a formally recognized scientific-task branch class whose approved integrations use a non-fast-forward source merge into a dedicated integration branch, followed by a fast-forward-only advance of `main`; the amendment is prospective and does not retroactively rewrite or re-merge previously accepted science branches.**
