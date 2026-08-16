# Review — D-1b RP Gap Classification Specification

**Reviewed artifact:** `SPEC d1b rp gap classification(1).md`  
**Reviewed specification SHA-256:** `4b37e09bed455c116e1ad449d7715fbe0a0835c38c9fa7286af19a429feab406`  
**Review date:** 2026-08-16  
**Review verdict:** `APPROVE FOR EXECUTION`

## Review scope

This review is bound to the exact uploaded specification bytes identified by the SHA-256 above.

The complete D-1b specification was reviewed for evidence-base binding, classification semantics, repository verification requirements, treatment of ambiguous D-1 `FAIL` material, multi-tag and `UNDETERMINED` handling, shared-gap analysis, acceptance criteria, Rule 16 epistemic boundaries, scope, candidate neutrality, and separation from subsequent proof-design or burden-sizing work.

## 1. Evidence base and task boundary — PASS

The specification correctly binds D-1b to authoritative main:

`822cd4fbfe9bff6e43867caed95c5635344683d0`

D-1b is correctly scoped as a post-D-1 classification task. It does not modify the landed D-1 coverage tables and does not reopen the D-1 literature search.

The task classifies the raw unmatched hypotheses already produced by D-1; it does not select an operator, design a proof, or recompute the broader B0 construction estimate.

## 2. Classification taxonomy — PASS

The specification uses the three intended scientific categories:

- `UNFROZEN DATUM`
- `INCOMPATIBLE HYPOTHESIS`
- `UNESTABLISHED APPLICABILITY BRIDGE`

It also permits:

- multiple/layered tags where the evidence genuinely supports more than one category; and
- `UNDETERMINED` where the available repository evidence does not justify a classification.

This avoids forcing ambiguous gaps into an artificial mutually exclusive taxonomy.

## 3. `UNFROZEN DATUM` evidential threshold — PASS

The revised specification correctly requires **affirmative repository evidence of non-freezing** before assigning `UNFROZEN DATUM`.

It explicitly rejects the invalid inference:

`failure to locate a freeze` → `therefore unfrozen`.

If the executor cannot establish the programme status from authoritative repository material, the appropriate outcome is `UNDETERMINED`.

Likewise, D-1 phrases such as `not mapped`, `not convention-mapped`, or `not frozen/mapped` are not by themselves sufficient to assign `UNFROZEN DATUM`.

This is load-bearing because D-1 deliberately used mixed applicability-failure language that D-1b must now disaggregate rather than merely relabel.

## 4. Repository verification — PASS

Where an `UNFROZEN DATUM` classification is proposed, the specification requires the executor to inspect the relevant ontology, microscopic specification, freeze/decision material, gates, prerequisites, and other authoritative repository text.

The classification therefore depends on programme state rather than on first-read wording in the D-1 table.

Repository silence is not upgraded into a scientific conclusion.

## 5. Incompatible hypothesis versus unestablished bridge — PASS

The specification preserves the distinction between:

- a theorem hypothesis that is actually inconsistent with an established programme fact; and
- a mapping, specialization, factorization, measure relation, auxiliary-field junction, or other applicability bridge that has simply not been established.

This prevents “the fetched literature does not supply the bridge” from being overstated as “the mathematics does not exist” or “the theorem is incompatible”.

## 6. Multi-tag and boundary-case handling — PASS

The specification allows a single raw gap to carry more than one tag where different layers of the same applicability failure support different classifications.

Boundary cases are a required deliverable rather than an error condition.

FG26-type factorization/reflection hypotheses and KU10-type auxiliary-field/measure junctions are correctly treated as classification seeds rather than preclassified conclusions.

## 7. Shared subject versus shared closure — PASS

The revised A8 now distinguishes:

- **shared subject** — the same programme datum or named hypothesis/junction appears for multiple candidates; and
- **shared closure** — existing evidence establishes that the same ruling or mathematical bridge would resolve the relevant entries for multiple candidates.

The specification explicitly prohibits inferring shared closure merely from similar wording.

Where only the common subject is established, the executor must report:

`SHARED SUBJECT / CLOSURE NOT ESTABLISHED`

This prevents D-1b from silently turning textual similarity into a construction-saving result.

## 8. Aggregate reporting — PASS

The A5 / report-contract arithmetic is now internally consistent.

The report must provide:

- one count for each of the three tag categories;
- the count of gaps carrying more than one tag; and
- the `UNDETERMINED` count.

These are reported separately rather than compressed into an incorrect “four counts” description.

## 9. Literature re-fetch boundary — PASS

D-1b does not re-fetch the literature as part of this task.

Accordingly, the revised Rule 16 language does not require the executor to speculate about how a direct source reread would change a classification.

Instead, it requires the report to state whether a tag was independently verified in this task. Where the source itself was not re-fetched, whether direct source rereading would alter the tag is correctly reported as:

`NOT DETERMINABLE BY THIS TASK`

## 10. Raw-count reconstruction — PASS

The specification requires the raw D-1 `FAIL` material to be reconstructed under an explicit counting rule rather than copied uncritically from prose summaries.

`UNKNOWN AT ABSTRACT DEPTH` is kept distinct from `FAIL`, and legend text or other non-entry occurrences are not to be counted as scientific gap entries.

This preserves reproducibility and avoids the grep-counting failure mode already observed elsewhere in the programme.

## 11. No burden sizing or proof design — PASS

The classification tags are not treated as cost estimates.

In particular:

- `UNFROZEN DATUM` does not imply that a later freeze will be scientifically trivial;
- `UNESTABLISHED APPLICABILITY BRIDGE` does not imply that the missing bridge is easy;
- `INCOMPATIBLE HYPOTHESIS` does not by itself determine the size of a replacement proof programme.

D-1b does not recompute B0's `7–11` estimate and does not design the missing lemma or RP construction.

## 12. Candidate neutrality — PASS

The distribution of tags may not be used to select, rank, prefer, or eliminate naive, Wilson, staggered, or overlap.

A candidate with apparently fewer bridge gaps is not thereby preferred.

A candidate with an incompatible theorem basis is not thereby refuted as a microscopic operator.

The task remains diagnostic rather than selective.

## 13. Scope and repository integrity — PASS

The specification retains a narrow governed scope of four additions and zero modifications.

Existing D-1, D-pre-B0, ontology, microscopic-specification, gate, and decision artifacts are evidence inputs and are not rewritten by D-1b.

The required repository checks, existing-path preservation, gate/pin validation, checker execution, validator suite, and commit-message/trailer hygiene remain part of the execution contract.

## 14. Acceptance criteria and Rule 16 — PASS

The revised acceptance criteria are consistent with the body of the specification.

They require the executor to expose ambiguous classifications, distinguish shared subject from shared closure, verify programme-state claims from the repository, and preserve the no-selection/no-proof-design boundary.

Rule 16 now respects the fact that literature is not re-fetched and does not ask the executor to make an unsupported counterfactual claim about what a direct reread would show.

## Final verdict

**`APPROVE FOR EXECUTION`**

I find no remaining scientific, evidential, classification, scope, execution-order, or governance defect requiring another revision before D-1b execution.

This approval applies **only** to the specification with SHA-256:

`4b37e09bed455c116e1ad449d7715fbe0a0835c38c9fa7286af19a429feab406`
