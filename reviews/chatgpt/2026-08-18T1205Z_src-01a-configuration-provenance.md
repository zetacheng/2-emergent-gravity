# Review — SRC-01a Configuration Provenance Specification

**Reviewed artifact:** `SPEC src 01a configuration provenance(2).md`  
**Reviewed specification SHA-256:** `1b87f571dbcfb4e063f32a5a7d734c39513a6faea971d95ac1fb6ff3da093473`  
**Review date:** 2026-08-18  
**Review verdict:** `APPROVE FOR EXECUTION`

## Review scope

This review is bound to the exact uploaded specification bytes identified by the SHA-256 above.

The revised SRC-01a specification was reviewed for configuration provenance, manuscript-bounded evidence, identification of the relevant scalar/mode, claim-versus-derivation status, parameter provenance, fitted-versus-derived classification, circularity risk, testability, historical SHA-attribution handling, repository integrity, and execution scope.

## 1. Historical SHA-attribution handling — PASS

The revised specification correctly removes the prior unsupported claim that three consecutive execution reports had necessarily reported specific unresolvable commit IDs.

It now distinguishes:

- a token that does not resolve as a Git object; from
- evidence that a particular report actually presented that token as its commit ID.

The task explicitly does not rely on the disputed historical attribution.

Instead, SRC-01a requires its own reported identifiers to come directly from contemporaneous `git rev-parse` output.

The retracted prior wording is preserved as provenance rather than silently erased.

## 2. Scientific purpose — PASS

SRC-01a is correctly framed as an epistemic provenance task rather than a phenomenology calculation.

It asks what the Paper 2 manuscript itself establishes about the origin of the halo configuration and its parameters.

It does not attempt to reconstruct the external Paper 1 calculation or import external results.

## 3. Provenance taxonomy — PASS

The four permitted classifications are appropriate:

- `DERIVED`
- `FITTED`
- `FORM DERIVED / SCALE FITTED`
- `NOT DETERMINABLE FROM THIS MANUSCRIPT`

The inclusion of the mixed classification is especially important because a theoretical functional form and an empirically fixed scale are logically distinct provenance claims.

## 4. Manuscript-bounded evidence — PASS

The task correctly limits itself to what the repository manuscript actually says and demonstrates.

A statement such as “we derived” is not automatically treated as a derivation performed in the present manuscript.

The executor must distinguish:

- `CLAIMED HERE AND DERIVED HERE`
- `CLAIMED HERE, CITED TO PAPER 1`
- `NOT ADDRESSED`

This prevents citation of external work from being misreported as an in-manuscript derivation.

## 5. Two-pass inventory — PASS

The revised two-pass search design is scientifically stronger than a vocabulary-only search.

PASS 1 locates phenomenology terms such as halo, SPARC, Yukawa, profile, and scaling language.

PASS 2 separately traces the scalar/mode identification chain.

This reduces the risk of missing the upstream question of which field or mode the manuscript actually associates with the phenomenological source configuration.

## 6. Identification provenance — PASS

The specification correctly requires the executor to establish how the relevant scalar or condensate mode is identified before classifying the halo profile.

The field identification itself may be derived, cited, assumed, or not addressed.

That provenance is distinct from the later profile and parameter provenance and must be reported separately.

## 7. Parameter relation versus parameter determination — PASS

The specification correctly distinguishes a relation such as

`r_c = 1 / m_theta`

from a determination of either `r_c` or `m_theta`.

A conversion between two parameters does not establish where the numerical scale came from.

The executor must therefore trace whether the scale is predicted from theory, inferred from data, fitted, cited externally, or not determinable.

## 8. Coupling and amplitude provenance — PASS

The task appropriately requires separate treatment of coupling and amplitude information.

A theoretically motivated profile shape does not become a parameter-free prediction if its normalization or coupling is fitted or imported as an effective parameter.

This distinction is necessary for any later claim of independent testability.

## 9. Circularity assessment — PASS

The specification correctly treats a profile fitted to the same rotation-curve data used for later validation as potentially circular.

It also correctly avoids overgeneralizing that risk.

If only a scale is fitted while other shape or cross-system predictions remain independent, the entire programme is not automatically circular.

The task therefore asks what remains testable under the derived provenance classification rather than prejudging the value of the source-side programme.

## 10. Paper 1 boundary — PASS

SRC-01a does not read, reconstruct, or import the external Paper 1 result.

It assesses only how Paper 2 characterizes that result.

This preserves repository provenance and prevents the task from silently changing evidence domains.

## 11. No numerical phenomenology — PASS

The task does not fit SPARC data, compute halo profiles, solve source equations, choose a coupling, or evaluate an attraction observable.

Any numerical values already present in the manuscript may be quoted and classified by provenance, but no new phenomenological result is produced.

## 12. Repository integrity and task scope — PASS

The specification is constrained to its governed SRC-01a artifacts.

Existing scientific derivations, manuscript text, gates, conventions, and prior SRC/RECON artifacts remain protected from opportunistic modification.

The task records provenance findings without rewriting the manuscript.

## 13. Execution and reporting discipline — PASS

The specification requires:

- contemporaneous ref/SHA resolution;
- explicit search counts and union accounting;
- separation of author observations from executor evidence;
- a four-commit artifact/report structure;
- final checker and validator execution;
- branch-only push discipline.

These controls are consistent with the scientific purpose and repository governance.

## Final verdict

**`APPROVE FOR EXECUTION`**

The revised specification resolves the remaining provenance defect by withdrawing the unsupported historical SHA-attribution claim and making that history non-load-bearing.

It also provides a rigorous classification framework for distinguishing theoretical form, fitted scale, external citation, parameter relation, coupling provenance, and what remains independently testable.

I find no remaining scientific-scope, provenance, circularity, manuscript-boundary, repository-integrity, or governance defect requiring another revision before execution.

This approval applies **only** to the specification with SHA-256:

`1b87f571dbcfb4e063f32a5a7d734c39513a6faea971d95ac1fb6ff3da093473`
