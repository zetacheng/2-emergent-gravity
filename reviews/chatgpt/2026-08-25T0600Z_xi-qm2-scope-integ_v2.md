# Review — P2-XI-QM2-SCOPE-INTEG v2

**Reviewed specification:** `2026-08-25T0600Z xi-qm2-scope-integ v2.md`  
**Reviewed specification SHA-256:** `043f7fa63a45854ca56c8d5b145f915aee5a503157ec498e18b6cc68baa160d6`  
**Review date:** 2026-08-30  
**Reviewer:** ChatGPT  
**Review verdict:** `APPROVE FOR EXECUTION`

## 1. Review binding

This review is bound exclusively to the exact specification bytes identified by:

`043f7fa63a45854ca56c8d5b145f915aee5a503157ec498e18b6cc68baa160d6`

It does not authorize execution of any other version of the specification.

## 2. v1 stop and v2 repair — PASS

The prior v1 execution correctly stopped under A1 because the reviewed Source field named a full SHA that did not exist in the repository.

The executor did not substitute the measured branch tip for the reviewed Source field.

v2 corrects that provenance defect by pinning the actual measured full source SHA:

`b133e6aab8a9f03a2c76345d5bd818898c6a1ab3`

The prior v1 review artifact does not authorize v2; this review is the new exact-byte authority.

## 3. Source identity — PASS

The corrected Source field is now consistent with the previously measured unique object resolving the `b133e6aa` abbreviation.

Execution must still re-measure the remote/source ref and require full-string equality before any write.

No abbreviation-based substitution is authorized.

## 4. Base and fork topology — PASS

The specification continues to pin Base at:

`08b46fb4a4e87f4db08a7f3b11b4086c9487b5c0`

and requires the stale-source merge-base to be re-measured at:

`0c01fc7f26e91dd84b032dccde0feac61f61d8ea`

The source does not descend from current Base, so the main-preservation sweep remains load-bearing.

## 5. Integration scope — PASS

The task remains limited to transporting the completed P2-XI-QM2-SCOPE-01 scope-assessment result.

It does not dispose or annotate Q-M2, treat the scope assessment as membership evidence, perform or design the future bounding computation, answer the PI-facing returns, prioritize follow-on scientific work, or reinterpret any input classification.

Q-M2 remains OPEN.

## 6. Source-contributed manifest — PASS

The source contribution remains pre-registered as exactly four added paths.

No modified, deleted, renamed, or additional path is authorized.

Any manifest deviation requires STOP rather than execution-time scope expansion.

## 7. Arriving-artifact digest checks — PASS

The four M3 expected digests remain unchanged from v1.

Execution must re-measure them from the merge product and require full-string equality.

The v1 pre-write stop does not permit these checks to be inherited as execution evidence.

## 8. Fork-aware union audit — PASS

The specification preserves direct measurement of `P_source`, `P_main`, `P_union`, and `P_overlap`.

Each path must satisfy the corresponding source/main/product blob rule.

Any both-changed path is a STOP condition rather than an opportunity for integration-time reconciliation.

## 9. Main-preservation sweep — PASS

For every path changed on main since the fork but untouched by the stale source, the merge product must preserve the current Base blob.

This protects the canonical G-18 state, Q-M3 constructive-gap result, and intervening governance/provenance artifacts from stale-source rollback.

## 10. Enumeration-first classification audit — PASS

M3c continues to require input enumeration from the arriving artifact's own structural markers before inspecting outcomes.

The complete input set and count are recorded first.

If the artifact does not provide a deterministic structural enumeration basis, the task stops rather than selecting inputs semantically.

## 11. Exactly-one-outcome verification — PASS

Each enumerated input must carry exactly one outcome from the arriving specification's fixed classification architecture.

The integration may not reconstruct or simplify the taxonomy from natural-language label counting.

## 12. PI-facing return reconstruction — PASS

The PI-facing return set is independently reconstructed from the enumerated inputs and their outcomes.

`REQUIRING A PI RULING` remains distinct from `ROUTED TO PI — CLASSIFICATION NOT DETERMINABLE`.

Transport must not collapse those epistemic categories.

## 13. DET-01 and landed-status semantics — PASS

`LANDED — NOT DETERMINABLE` continues to mean that the non-determinability status is landed.

It does not mean that the unknown functional-measure value has been obtained.

The integration is not authorized to weaken or reinterpret that distinction.

## 14. Scope-discipline statements — PASS

The arriving statements that the assessment proposes nothing and that listing a question is not evidence about its answer remain part of the transported result.

The `COND-D`, `COND-E`, and `COND-S` limitations must remain intact.

## 15. Measurement-method discipline — PASS

Structural probes must be constructed from landed bytes rather than remembered or rendered Markdown.

Fence, blockquote, emphasis, byte-offset, and normalization assumptions must be explicit.

Where an audit probe is shown to be defective by its own formatting assumption, it may be corrected and re-measured without changing product bytes, with the correction recorded.

## 16. Test / report sequencing — PASS

The execution sequence remains coherent:

`Base -> spec -> review -> merge -> fork/arrival audits -> tests -> report -> H_integ -> push`

The report records only measurements that already exist and does not attempt to state its own commit SHA.

`H_integ` is measured externally after the report commit.

## 17. Main / post-push separation — PASS

Main advances by fast-forward only to `H_integ`.

Any post-push audit addendum remains on the integration branch only.

## 18. Ref immobility — PASS

The source branch and other protected refs must remain unmoved except where the specification explicitly authorizes movement.

Only main and the integration branch may move under this task.

## 19. Version-change scope — PASS

The substantive protocol is unchanged from v1.

The v2 repair is confined to the corrected Source full SHA and the necessary version/provenance metadata identifying this revised specification.

No scientific, manifest, acceptance, or transport semantics are broadened by the repair.

## 20. Abort discipline — PASS

The abort structure remains coherent across Base/source drift, source-pin mismatch, merge conflict, digest mismatch, manifest deviation, overlap, main-preservation failure, classification-structure failure, unauthorized scientific reinterpretation, and non-fast-forward main movement.

No executor discretion is introduced to substitute a different source commit for the reviewed Source field.

## Final verdict

**`APPROVE FOR EXECUTION`**

Reviewer determinations:

- Source pin defect: `RESOLVED`
- Base / fork topology: `CONSISTENT`
- M3 manifest / digests: `PRESERVED`
- M3c classification audit: `PRESERVED`
- Q-M2 authority boundary: `PRESERVED`
- Protocol closure: `PASS`

`P2-XI-QM2-SCOPE-INTEG v2` is approved for execution subject to all exact-Base, exact-Source, source-pin, manifest, fork-audit, classification-domain, PI-return reconstruction, byte-measurement, testing, reporting, ref, and push controls stated in the specification.

**Reviewed specification SHA-256:** `043f7fa63a45854ca56c8d5b145f915aee5a503157ec498e18b6cc68baa160d6`
