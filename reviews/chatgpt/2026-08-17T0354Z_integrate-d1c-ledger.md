# Review — Integrate D-1c Dependency-Reduction Ledger

**Reviewed artifact:** `SPEC integrate d1c ledger(1).md`  
**Reviewed specification SHA-256:** `bf7ce753aac2dccaf772d418d9193af662acd72fb31236ba146edd3fdad01b11`  
**Review date:** 2026-08-16  
**Review verdict:** `APPROVE FOR EXECUTION`

## Review scope

This review is bound to the exact uploaded specification bytes identified by the SHA-256 above.

The complete D-1c integration specification was reviewed for source/base binding, preservation of the dependency-reduction result, adopted-granularity qualifications, occurrence/node accounting, `k8` multi-dependency treatment, repository verification of open rulings, lexical-hit versus authoritative-ruling distinction, Rule 16 interpretation, scope arithmetic, candidate neutrality, and separation from subsequent ruling-ordering or mathematical work.

## 1. Source result and evidence base — PASS

The integration task correctly treats the completed D-1c branch as the source result to be landed against the specified authoritative main evidence base.

The source dependency ledger is to be preserved without retrospective modification of D-1, D-1b, or D-1c evidence artifacts.

## 2. D-1c reduction result — PASS

The integration preserves the source result:

- 25 `UNFROZEN DATUM` occurrences mapped to 5 `RULING` nodes under the adopted dependency-accounting granularity;
- 8 `INCOMPATIBLE HYPOTHESIS` occurrences mapped to 2 `ESTABLISHED FACT` nodes;
- 21 `UNESTABLISHED APPLICABILITY BRIDGE` occurrences left untouched;
- 9 `UNDETERMINED` entries left outside reduction.

The task does not reinterpret these node counts as total scientific workload.

## 3. Adopted granularity — PASS

The specification correctly states that the five-node UD result is a granularity-dependent accounting representation rather than a unique physical constant.

In particular, R1 groups the canonical kinetic-operator choice with associated delegated constituents. A finer constituent-level decomposition recorded by D-1c can yield eight nodes over the same 25 UD occurrences.

The integration must preserve both facts and must not present `25 → 5` as a unique granularity-independent decomposition.

## 4. Node semantics — PASS

The revised Rule 16 correctly defines a node as an:

**ADOPTED DEPENDENCY-ACCOUNTING UNIT**

and explicitly states that a node is not automatically:

- a to-do item;
- a question;
- a decision;
- a problem; or
- a unit of effort.

A lower node count therefore means only that more occurrences are grouped under fewer accounting units at the adopted granularity.

It does not establish fewer underlying scientific questions or easier work.

## 5. Exactly-once accounting versus intervention effects — PASS

The integration preserves the distinction between the ledger's exactly-once occurrence partition and causal retirement of gaps.

The `k8` entry is the critical example: it contains both finite-extent and boundary-data dependence, but exactly-once bookkeeping assigns it to R2.

This does not imply that R3 is irrelevant to `k8`, nor that freezing R2 alone would retire the occurrence.

The ledger is therefore dependency accounting, not an intervention-effect model.

## 6. Ruling-node verification — PASS

The integration independently verifies whether later authoritative programme rulings supersede the five open RULING nodes.

The required search extends beyond the primary freeze documents to current gate, decision-log, and referenced authoritative material.

The task does not infer “still open” merely from absence in one early specification.

## 7. Lexical hits versus authoritative rulings — PASS

The revised specification correctly distinguishes:

- literal lexical search hits; and
- the disposition of those hits after reading them in context.

In particular, `measure` has three lexical hits in `DECISION_LOG.md`.

Those hits must be inspected rather than reported as zero. The scientific conclusion to verify is whether any of them constitutes a later authoritative ruling for the R4 microscopic integration measure.

Thus the source executor's “zero” is interpreted, where supported after reading, as **zero later authoritative rulings**, not zero lexical occurrences.

## 8. Cross-paper grouping check — PASS

The integration preserves the evidence that D-1c grouping is not circularly based on paper identity.

R2, R3, and R4 span entries originating from different literature bases, while entries associated with the same source paper are not automatically grouped together.

W6/n6 remain outside this reduction because D-1b classified their remaining issue as an applicability bridge.

## 9. Shared-closure and UB boundary — PASS

The 21 UB occurrences remain outside dependency reduction.

The integration does not determine whether two UB occurrences are mathematically the same bridge and does not infer shared closure from similar wording, common source, or apparent mathematical similarity.

No applicability lemma or RP proof is designed.

## 10. Candidate-selection boundary — PASS

The dependency ledger cannot be used as an independent physical reason to choose the canonical kinetic operator.

In particular, RP-literature applicability cannot be inverted into an operator-selection criterion merely because a particular ruling would close or reorganize more ledger entries.

This preserves the programme's operator-first-from-independent-physics principle.

## 11. Interpretation of represented tag occurrences — PASS

The dependency reduction represents the 25 UD and 8 IH tag occurrences, i.e. 33 of the 54 tag occurrences in the D-1b classification inventory.

The remaining 21 UB tag occurrences are untouched by D-1c.

This should be described as representation within the UD/IH dependency reduction, not confused with D-1's formal literature verdict `COVERED`.

## 12. No ruling ordering in this integration — PASS

The integration does not decide which of R1–R5 should be frozen first.

It does not determine independence or precedence among those rulings, does not make any of the rulings, and does not infer that a ruling with more mapped occurrences has higher scientific priority.

Any ruling-ordering or independence audit belongs to a subsequent scientific task.

## 13. No burden re-estimation — PASS

The integration does not recompute B0's `7–11` construction estimate.

Neither the five RULING nodes nor the two ESTABLISHED FACT nodes are treated as construction counts or proof-cost units.

The 21 UB occurrences remain mathematically unresolved at the level established by D-1b.

## 14. Scope arithmetic and repository integrity — PASS

The integration scope is internally consistent:

- 4 arriving source additions;
- 2 pre-merge integration additions;
- 6 additions at the merge stage;
- final report added afterward;
- 7 additions / 0 modifications at completion.

Existing scientific, governance, classification, freeze, and dependency artifacts remain protected from opportunistic modification.

## 15. Acceptance criteria and Rule 16 — PASS

The acceptance contract is consistent with the scientific task boundary.

It requires preservation and independent verification of the D-1c ledger while preventing:

- node = question/task interpretations;
- causal-retirement claims from exactly-once accounting;
- UB grouping;
- shared-closure analysis;
- proof design;
- ruling ordering;
- operator selection; and
- B0 burden recomputation.

## Final verdict

**`APPROVE FOR EXECUTION`**

I find no remaining scientific, evidential, provenance, dependency-accounting, interpretation, scope, or governance defect requiring another revision before execution.

This approval applies **only** to the specification with SHA-256:

`bf7ce753aac2dccaf772d418d9193af662acd72fb31236ba146edd3fdad01b11`
