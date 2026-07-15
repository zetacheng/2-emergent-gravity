# Research Workflow

## Scope

This repository contains Paper 2 only: *Emergent Gravity from Lattice Fermion
Fields*. Historical scientific status must be imported and audited; it must not
be inferred from repository infrastructure.

## Role separation

### ChatGPT

ChatGPT supports conceptual discussion, physical interpretation, analytic
derivation planning, gate design, preparation of calculation specifications,
and identification of assumptions and competing interpretations. ChatGPT does
not certify numerical results.

### Codex

Codex maintains the repository, implements symbolic and numerical work, creates
tests and regression anchors, ensures reproducibility, stores result files, and
enforces branch and commit discipline. Codex must not promote a result into a
paper claim without review.

### Claude

Claude independently reviews and discriminates among derivations and results,
issues verdicts on whether gates pass, identifies overclaims, and updates the
paper only after results are accepted.

### User / Principal Investigator

The User / Principal Investigator owns the physical programme, approves
assumptions, gates, and scope changes, accepts or rejects final verdicts, and
decides when paper text may be updated.

## Gate lifecycle

1. Record a proposed gate in `GATES.md`.
2. Specify the question, scope, assumptions, conventions, inputs, analytic and
   regression anchors, kill criterion, computations, and deliverables.
3. Obtain Principal Investigator approval for assumptions, gate, and scope.
4. Commit a complete derivation note before production code.
5. Implement and run the gate on a dedicated `gate/<gate-name>` branch.
6. Preserve raw outputs and produce processed artifacts with full provenance.
7. Run tests and compare all registered anchors.
8. Submit the derivation and result record for independent Claude review.
9. Record `PASS`, `FAIL`, `INCONCLUSIVE`, `SUSPENDED`, or `RETIRED` and its
   consequences without deleting failed routes.
10. Promote a result to `VERIFIED`, merge a closed gate, or update paper text
    only after reviewer acceptance and the Principal Investigator's decision.

Code execution alone is never a scientific verdict.
