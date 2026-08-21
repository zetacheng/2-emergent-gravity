# Review — P2-PROVENANCE-CENSUS-INTEG

**Reviewed specification:** `P2-PROVENANCE-CENSUS-INTEG(1).md`  
**Reviewed specification SHA-256:** `eebcd4c5161f2fa0d49b815ef650a0cef9bfc04496d6e8ecae4154aac0b43efa`  
**Review date:** 2026-08-21  
**Reviewer:** ChatGPT  
**Review verdict:** `APPROVE FOR EXECUTION`

## 1. Review binding

This review is bound exclusively to the exact specification bytes identified by:

`eebcd4c5161f2fa0d49b815ef650a0cef9bfc04496d6e8ecae4154aac0b43efa`

It does not authorize execution of any other version of the specification.

## 2. Integration architecture — PASS

The specification correctly separates transport of the reviewed census result from the later PI ruling incorporated in §5.

The integration does not acquire authority to rewrite the census measurements, silently add candidates, or reclassify the reviewed result.

## 3. PI authority for the S-6 criterion — PASS

§5.1 now records an explicit PI ruling that a specification transcribing an adjudication's words is evidence of the adjudication's content but does not, by itself, constitute that adjudication's canonical landed provenance record.

The English rendering is expressly identified as a working translation rather than as the ruling itself. The authority chain is therefore explicit rather than inferred from Reviewer agreement or executor judgement.

## 4. Content evidence versus canonical provenance — PASS

The specification correctly distinguishes:

- evidence that a specification contains or transcribes adjudication content; and
- governance status as the canonical landed provenance record of that adjudication.

Specification transcriptions may remain candidate source material for later provenance repair, but they do not automatically move an adjudication into the canonical-provenance class.

## 5. Historical correction discipline — PASS

The specification does not erase the fact that an earlier draft described the S-6 criterion as an issued PI decision before explicit PI issuance had been established.

The correction is recorded rather than retrospectively beautifying the history.

The revised §5.3 also avoids asserting an unsupported historical motive. Repository behaviour may operationally demonstrate the distinction; whether that distinction was the stated historical motive must be established by execution-time citation.

## 6. Census-result preservation — PASS

The integration preserves the census's measured sets and does not predeclare or replace their execution-time values.

The distinction between passage count and distinct-adjudication count is maintained. Downstream remediation is scoped to distinct adjudications, not repeated passages referring to the same adjudication.

## 7. Ratification guard — PASS

The specification requires execution-time comparison between the criterion actually used by the census and the criterion now ratified by the PI.

If they differ substantively, the stated abort condition remains live. Ratification therefore does not silently cover a different executor criterion.

## 8. Provenance-tier finding — PASS

The specification preserves the original binary census measurement while registering the newly observed provenance-completeness question separately.

It does not retroactively replace the reviewed census with a new multi-tier model during integration.

## 9. Citation-identity finding — PASS

The specification correctly preserves the finding that forms such as `PI ruling N` are not necessarily globally unique.

It registers the governance issue without inventing a new canonical citation syntax inside this integration task.

## 10. Validation-method finding — PASS

The parser/set-relation incident is correctly retained as a finding for later adoption:

set identities passing does not, by itself, establish that the parser populated the sets correctly.

The integration does not convert that methodological observation into an unreviewed standing rule.

## 11. Append-only verification — PASS

The revised specification now provides an explicit measurement for append-only verification.

The executor must verify, for each applicable append-only file, that the base bytes are an exact prefix of the merge-product bytes and record the compared byte counts.

This supplies direct measurement evidence for the corresponding acceptance criterion.

## 12. Independent omission check — PASS WITH EXECUTION BOUNDARY

The Researcher-side independent omission spot-check remains appropriate.

If that check identifies a genuinely new candidate omitted by the census, the integration must not silently add it to the transported census result. Such a result is a verification finding or potential census defect and must be handled through the repository's review/governance process.

## 13. Branch, merge, and push controls

Execution remains subject to the specification's exact branch, merge, ancestry, manifest, and push-scope requirements and to `docs/BRANCHING_POLICY.md`.

No session or harness branch receives authority merely because it is the executor's current branch.

## 14. Execution authority

This approval authorizes execution only under the specification's exact measurements, abort conditions, acceptance criteria, manifests, and governance boundaries.

It does not independently ratify census members, alter census counts, settle the open provenance-tier question, establish a new citation convention, or authorize repair of newly discovered census omissions during integration.

## Final verdict

**`APPROVE FOR EXECUTION`**

`P2-PROVENANCE-CENSUS-INTEG(1).md` is approved for execution subject to all stated controls.

**Reviewed specification SHA-256:** `eebcd4c5161f2fa0d49b815ef650a0cef9bfc04496d6e8ecae4154aac0b43efa`
