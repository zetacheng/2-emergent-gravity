# Pre-execution Review — Integrate the Governance Checker and Land It (v2)

**Review status: APPROVED**

Task reviewed: **integrate the governance checker, and land it**

Evidence base: `8939ff4a46445d88c6470fb4f27eec71f2f39172`

Source branch: `governance/enforcement-checks @ fe8de65de8288593f39a74110c1ea370ce27021f`

Proposed integration branch: `governance/integrate-enforcement-checks-v2`

## Executive finding

This re-issue fixes the blocking problem exposed by the first integration attempt.

The first attempt failed because the existing P1 grammar read the nearest count-bearing **line**, while the integration specification wrapped its governing count across lines and also placed `(none)` under `modify:`. The resulting false positive was `stated 0, counted 10`.

This specification removes both producer-side triggers without modifying the reviewed checker:

- the governing P1 count is intentionally kept on one line for this task only;
- the empty modification set is represented as `modify: []`, which the existing parser already accepts.

That is sufficient to make this integration task executable while preserving the reviewed source branch byte-for-byte.

Importantly, this task does **not** claim to repair the checker. The line-versus-paragraph grammar defect remains and is explicitly deferred to a later task after the checker is on authoritative `main`.

## Resolution of the previous ancestry/P4 concern

The earlier proposed repair task was structurally unsatisfiable because it would have cut a replacement branch from `fe8de65d…` while simultaneously registering `fe8de65d…` as SUPERSEDED. P4 would then necessarily fail because the registered superseded commit would be an ancestor of the replacement head.

This integration specification does not make that mistake.

It:

- merges `fe8de65d…` as the reviewed source result;
- does **not** register `fe8de65d…` as superseded;
- preserves the stopped integration attempt at `58a996a4…`;
- does not write any supersession entry in this task;
- defers the stopped-attempt register entry to a later task authorised to modify `docs/BRANCHING_POLICY.md`.

Therefore the existing six-entry P4 register remains unchanged, and none of those six commits is made an ancestor by this merge according to the pre-issue measurements.

The previous ancestry blocker is removed.

## P1 accommodation is explicit and bounded

A5 now contains the governing count on one physical line:

> **Final base-to-head scope: 9 additions and 0 modifications.**

and the manifest uses:

```text
modify: []
```

rather than `(none)`.

This is a valid accommodation to the existing parser for this integration.

The specification is also explicit that the one-line form is **not a house style** and not the eventual repair. It is temporary for this one task. That distinction is important and is sufficiently visible in §2b and the report contract.

I recommend preserving that wording in the committed artifact and not shortening it during execution.

## A10 is now logically sound

The two-run design resolves the conflict between preserving the deliberately defective source specification and requiring this integration task itself to pass the checker.

### RUN 1

Default specification discovery is observational only.

It may include the merged source specification with the planted `five versus six` defect. If P1 fails there for that reason, that is expected evidence that the checker was not configured to hide a known defect.

RUN 1 does not govern the stop decision.

### RUN 2

The stop-governing subject is fixed to exactly:

`specs/2026-08-XXT{HHMM}Z_integrate-enforcement-checks-v2.md`

That exclusion is explicit rather than silent.

For this specification, the existing P1 grammar has been pre-tested against the actual text and measured:

`stated 9, counted 9, PASS`.

The config may not be narrowed further, properties may not be dropped, and empty declared sets may not be supplied merely to obtain green. Those prohibitions make the RUN 2 result meaningful.

This resolves the previous A10 contradiction.

## Evidence layering is consistent

The report is commit 4 and therefore cannot contain measurements of itself.

The specification now correctly separates:

- measurements made at commit 3 and committed in the report;
- the final nine-path scope as an **INTENDED** manifest in the report;
- commit-4 checks, A10-final, commit-4 message hygiene and pushed-main verification as post-report evidence.

This removes the earlier self-reference problem in which the report was required to contain measurements of an object that did not yet exist.

## Scope and merge shape

The stated scope is internally consistent:

- source branch contributes six additions;
- this task authors specification, review and report;
- final base-to-head scope is nine additions and zero modifications;
- merge-head scope before the report is eight additions and zero modifications.

The manifest contains nine added paths and `modify: []`.

No protected existing path is authorised to change.

## Deferred stopped-attempt register entry

The specification correctly does **not** add
`governance/integrate-enforcement-checks @ 58a996a4…`
to the superseded register in this task.

That would be a new governance classification and would require modifying
`docs/BRANCHING_POLICY.md`, which this integration is not authorised to do.

The branch is nevertheless pinned and protected by A1 and the invariants.

Deferring the register entry is therefore acceptable, provided the report records the deferral exactly as required.

## What this task still does not fix

This task fixes the **integration blockage**, not the checker defect.

After a successful landing:

- P1 still uses the old line-based grammar;
- the classification still describes a sentence-based grammar that the implementation does not actually implement;
- the real `1820Z` specification remains a live counterexample;
- CI still does not invoke `task_checker.py`;
- governance verification remains available, not enforced.

The follow-up grammar repair is still materially necessary.

The most important future constraint is that the repair should be performed on the now-authoritative `main` state, rather than by creating a replacement branch that descends from a branch simultaneously declared superseded.

## Minor wording observation

The sentence in §2b:

> **This specification carries both fixes.**

is immediately qualified correctly: `modify: []` is a producer correction, while the one-line count is only an accommodation.

For maximal precision I would prefer wording such as:

> **This specification removes both triggers of the known false positive.**

That avoids momentarily calling the one-line accommodation a “fix”.

This is non-blocking because the distinction is made explicitly in the following paragraph.

## Rule 16 assessment

Two inference junctions remain important.

First, landing forty-two green checker tests can easily be read as “governance is covered by tests”. That remains false. The tests establish checker behaviour on fixtures; CI does not invoke the checker, and twenty-two of twenty-nine classified governance objects have no machine behind them.

Second, the false `MEASURED` statement in the integrated source specification remains immutable and has no local pointer to its correction. The correction exists in the accompanying report, but discoverability depends on a reader already knowing to inspect that report. No existing convention appears to create a direct correction pointer from the false statement to its correcting artifact.

Neither issue blocks this integration because both are explicitly disclosed and neither is altered by this task.

## Decision

**APPROVED for execution.**

This specification can fix the immediate integration problem that caused the first attempt to stop.

Approval is specifically for the strategy used here:

1. integrate the reviewed `fe8de65d…` branch unchanged;
2. make the integration specification parseable by the existing P1 grammar using the documented one-task accommodation;
3. keep the stopped integration branch untouched;
4. land by fast-forward only after RUN 2, A10-final and the remaining acceptance criteria pass;
5. repair the P1 grammar in a separate subsequent task on the authoritative landed state.

Do not reinterpret this approval as approval of the current P1 grammar itself. The grammar defect remains a confirmed follow-up item.
