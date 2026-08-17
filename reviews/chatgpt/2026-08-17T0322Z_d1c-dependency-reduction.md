# Review — D-1c Dependency Reduction Specification

**Reviewed artifact:** `SPEC d1c dependency reduction(2).md`  
**Reviewed specification SHA-256:** `cadbe6d886e990f13ce26ee5e469c4b760850e39b2817927401a02f20abefe1d`  
**Review date:** 2026-08-16  
**Review verdict:** `APPROVE FOR EXECUTION`

## Review scope

This review is bound to the exact uploaded specification bytes identified by the SHA-256 above.

The complete D-1c specification was reviewed for evidence-base binding, dependency-node semantics, treatment of `UNFROZEN DATUM` and `INCOMPATIBLE HYPOTHESIS` occurrences, explicit exclusion of `UNESTABLISHED APPLICABILITY BRIDGE` and `UNDETERMINED` occurrences from reduction, repository-authority requirements, occurrence-level versus dependency-level counting, Rule 16 boundaries, scope controls, and candidate neutrality.

## 1. Task boundary — PASS

D-1c is correctly scoped as a non-mathematical dependency-reduction task.

It asks how many distinct programme rulings underlie the 25 `UNFROZEN DATUM` occurrences, and how many distinct established incompatibility facts underlie the 8 `INCOMPATIBLE HYPOTHESIS` occurrences.

It does not reopen D-1b classification, does not re-fetch literature, and does not design an RP proof or applicability lemma.

## 2. Asymmetric treatment of gap classes — PASS

The specification correctly treats the four D-1b outcome classes asymmetrically:

- `UNFROZEN DATUM` — eligible for programme-ruling reduction;
- `INCOMPATIBLE HYPOTHESIS` — eligible for established-fact reduction;
- `UNESTABLISHED APPLICABILITY BRIDGE` — explicitly outside reduction scope;
- `UNDETERMINED` — explicitly outside reduction scope.

This prevents the executor from deciding whether two unestablished mathematical bridges are “really the same bridge”, which would require new mathematical judgment and exceed D-1c.

## 3. W6/n6 exclusion — PASS

The specification correctly prohibits reopening W6/n6.

D-1b has already established the programme-side non-gauge status and classified the remaining issue as an applicability bridge. D-1c therefore treats that result as settled input rather than rerunning the classification.

## 4. `UNFROZEN DATUM` dependency nodes — PASS

A `RULING` node may be created only where repository evidence establishes that the same still-open programme datum controls the mapped occurrences.

Shared wording, common source literature, or apparent mathematical similarity is insufficient.

The specification also provides a lawful path if a proposed ruling datum turns out to be already frozen or if programme status cannot be determined.

## 5. Occurrence-level versus dependency-level accounting — PASS

The revised specification correctly separates dependency/datum-level status from occurrence-level disposition.

At the dependency/datum level, the executor reports the proposed/open/frozen/undetermined datum statuses.

At the occurrence level, all 25 `UNFROZEN DATUM` occurrences must be dispositioned exactly once through:

- verified-open ruling-node mapping;
- already-frozen classification finding; or
- programme-status-not-determinable finding.

The required reconciliation is therefore:

`25 = N_mapped + N_frozen_finding + N_undetermined_finding`

without requiring the dependency-level counts to equal the occurrence-level counts.

This resolves the previous ambiguity where one rejected datum could govern several occurrences.

## 6. Repository-authority verification — PASS

The four named freeze/specification documents are correctly treated as mandatory minimum evidence rather than an exhaustive authority universe.

For every proposed programme-ruling node, the executor must also inspect current authoritative gate, decision-log, and registered/frozen specification material where relevant.

This prevents a later ruling recorded elsewhere in the repository from being misclassified as still open merely because it is absent from the primary four documents.

## 7. `INCOMPATIBLE HYPOTHESIS` reduction — PASS

The 8 `INCOMPATIBLE HYPOTHESIS` occurrences may be grouped only where the same already-established programme fact conflicts with the relevant theorem hypotheses.

This is fact dependency reduction, not theorem redesign.

The specification does not permit an incompatibility node to be created merely because two entries look similar or cite the same paper.

## 8. UB epistemic wording — PASS

The specification now states only that the relevant applicability bridge is **not established in the present evidence basis**.

It does not claim that the required mathematics or proof does not exist.

This preserves the bounded-evidence discipline established in D-1 and D-1b.

## 9. Negative grouping tests — PASS

The specification appropriately requires rejected grouping cases to be reported.

This makes the grouping rule falsifiable and auditable rather than merely asserted after the fact.

The MP87 Wilson/naive case is correctly useful as a negative-control-style example: shared source wording alone does not establish one dependency node.

## 10. No shared-closure analysis — PASS

D-1c does not attempt to establish whether multiple UB occurrences could be closed by one mathematical bridge.

It does not infer shared closure from shared subject, common theorem, or similar wording.

The 21 UB occurrences therefore remain outside this task's reduction arithmetic.

## 11. No burden sizing or B0 recomputation — PASS

A reduced count of programme-ruling or incompatibility nodes is not treated as a workload estimate.

For example, a result such as `25 UD occurrences → 4 ruling nodes` would mean only that 25 manifestations depend on four distinct programme questions. It would not show that those four questions are easy or that total RP construction burden has fallen to four tasks.

The specification does not recompute B0's `7–11` estimate.

## 12. Candidate neutrality — PASS

The dependency distribution may not be used to select, rank, prefer, or eliminate naive, Wilson, staggered, or overlap.

Fewer ruling nodes or fewer incompatibility nodes do not constitute candidate merit.

The task remains diagnostic and programme-structural rather than selective.

## 13. Writable scope and checker declaration — PASS

The specification keeps the execution scope to the governed D-1c artifacts and does not authorise modification of existing scientific or governance files.

The `append_only: DECISION_LOG.md` declaration is explicitly identified as checker configuration rather than write authorisation.

If checker interpretation conflicts with the normative no-modification scope, the executor must stop and report rather than write to the file.

## 14. Acceptance criteria and Rule 16 — PASS

The acceptance criteria are consistent with the task body.

They require complete occurrence disposition, dependency-node evidence, explicit rejected-grouping records, repository verification of ruling status, no UB reduction, no UNDET grouping, no proof design, no candidate selection, and no burden re-estimation.

Rule 16 correctly prevents the reduced dependency counts from being overstated as mathematical closure or workload reduction.

## Final verdict

**`APPROVE FOR EXECUTION`**

I find no remaining scientific, evidential, dependency-accounting, repository-authority, scope, or governance defect requiring another revision before D-1c execution.

This approval applies **only** to the specification with SHA-256:

`cadbe6d886e990f13ce26ee5e469c4b760850e39b2817927401a02f20abefe1d`
