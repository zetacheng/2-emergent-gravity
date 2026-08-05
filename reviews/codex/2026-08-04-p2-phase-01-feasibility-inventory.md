# Feasibility inventory — `P2-PHASE-01` (SI-1, the Ice)

**Author:** Codex executor  
**Adopting authority:** Principal Investigator  
**Status:** PI-authorized feasibility inventory; pending result review  
**Paper 2 evidence base:** `1e8d56da124c2ae791fb7a00b23a188d329c56f8`  
**Programme prior-art evidence base:** `0-programme` commit `315451829412067f2e86d3559975e36b1b2ee03c`

This inventory records repository state at the evidence bases, BEFORE the PI ruling recorded in `DECISION_LOG.md`; its dependency-ambiguity finding is resolved by that ruling, while its scientific-prerequisite findings remain operative.

## Dependency / unblock status

`P2-PHASE-01` depends on `P2-CHANNEL-FREEZE-01` and says phase enumeration may proceed once “the channel freeze is committed,” without consuming Finding 5's `-3.2(5)`. It does not name a phase of the freeze. (`GATES.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `## P2-PHASE-01`, `### Dependency`, lines 994–999.)

The dependency instead records `Freeze state: PHASE-A FROZEN`, `Metric state: PHASE-B PENDING`, and `SI-2 admissibility: BLOCKED UNTIL PHASE-B FREEZE`. (`GATES.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `## P2-CHANNEL-FREEZE-01`, lines 874–886.) The Phase-A artifact says it freezes no SI-2 calculation or Phase-B metric. (`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, lines 1–7.)

The SI-1 clarification lists the phase catalogue among activities that do not consume the historical value and “may proceed.” (`derivations/P2-SI1-UNBLOCK-01.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `## 4`.) It does not state whether Phase A alone suffices after the A/B distinction was recorded. That is the governance ambiguity found here, not a scientific conclusion.

## Gate requirements and defined inputs

The gate asks whether the fixed lattice-fermion theory possesses at least one physically admissible stable condensed phase. Its scope is stationary solutions `δΓ/δΦ_i = 0` of the full effective action, with condensates from frozen channels, at finite density / `μ`, in the pre-registered microscopic parameter domain. Its listed inputs are frozen channels, `Γ[Φ_i]`, and finite density / `μ`. (`GATES.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `P2-PHASE-01 / Scientific question`, `Scope`, and `Inputs`, lines 978–1003.)

Frozen channels are concrete: the Phase-A machine data records genuine coordinate `G`, non-scan-eligible `HS_scale` and `Fierz_basis`, and five HS families `S`, `P`, `V`, `A`, `T` with a `K_ij` registry. (`derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `## §B` and lines 115–122.) No Paper 2 definition of `Γ[Φ_i]`, finite-density prescription, or bounded microscopic parameter domain was located. The literal parameter-domain phrase appears in the phase-gate scope only; “frozen space” appears in its kill criterion only. (`GATES.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `P2-PHASE-01`.)

## Existing relevant material

`P2-GAP-01` is a completed scalar-channel, leading-order / mean-field gap-equation criticality calculation. It derives `G_c = 1/(2 I_0)` for continuum sharp-cutoff and Wilson-lattice scalar gap equations. (`GATES.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `P2-GAP-01`, lines 81–124; `derivations/P2-GAP-01_gap_criticality.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `## Scientific question`.)

Its derivation identifies a nontrivial scalar stationary point of a leading-order effective potential, but expressly says it is not channel-bubble criticality and cannot distinguish channel criticalities beyond leading order. (`derivations/P2-GAP-01_gap_criticality.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, lines 14–23.) Its artifacts are `scripts/gap_criticality.py`, `derivations/P2-GAP-01_gap_criticality.md`, and `results/P2-GAP-01/`. (`GATES.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `P2-GAP-01 / Required deliverables`.) The repository does not designate these as a reusable all-channel, finite-density, physical-admissibility solution.

No `P2-PHASE-01` derivation, script, results directory, or report exists at this base. (`git ls-tree -r` at `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, searched for `PHASE`, `phase`, `condens`, `stationary`, and `stability`; only the `GATES.md` phase block was found.)

## Missing prerequisites

| Missing item | Evidence at Paper 2 evidence base | Owner |
|---|---|---|
| Phase-A-versus-full-freeze interpretation | Phase gate says “channel freeze”; dependency separates Phase A/B. (`GATES.md`, both named gate blocks.) | Not assigned |
| Microscopic parameter domain | Required by the phase gate; no bounds or domain artifact found. (`GATES.md`, `P2-PHASE-01 / Scope`.) | Paper 2 gate owner; no narrower owner assigned |
| `Γ[Φ_i]` and finite-density input contract | Named as inputs only. (`GATES.md`, `P2-PHASE-01 / Inputs`.) | Paper 2 gate owner; no narrower owner assigned |
| Phase enumeration computation/deliverables | All execution fields are `(not started)`. (`GATES.md`, `P2-PHASE-01 / Required computations` through `Reviewer verdict`.) | Paper 2 |
| Operational admissibility/stability rules | None are frozen in the phase-gate block. | Paper 2 gate owner; no narrower owner assigned |

## Quarantine and exclusion ledger

| Item | Classification | Evidence |
|---|---|---|
| Finding 5 value `β_V/β_B = −3.2(5)` | Hard prohibited / quarantined as validated numerical input | “must not appear as a validated numerical input to any SI-1 or SI-2 computation.” (`derivations/P2-SI1-UNBLOCK-01.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `## 6`.) |
| Historical extraction | Hard prohibited as operational numerical input | `P2-BETAV-CIRC-01` blocks use of historical extraction as operational input. (`GATES.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `P2-BETAV-CIRC-01 / Operational consequence`, lines 548–576.) |
| `P2-BETAV-CIRC-01` | Inconclusive but not prohibited reading; non-blocking for SI-1 | Status `RUN`, verdict `INCONCLUSIVE`; it “does not block” `P2-PHASE-01`. (`GATES.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, lines 328–347 and 548–563.) |
| `P2-BETAV-NUMREPRO-01` | Inconclusive but not prohibited reading | Status `RUN`, verdict `INCONCLUSIVE`. (`GATES.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, lines 598–602.) |
| Withdrawn additive `k`-scan | Historical / non-live | Retained only as a historical record, not a live specification. (`GATES.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `P2-BETAV-CIRC-01 / Superseded specification`.) |
| Recovered Ward summary | Historical / non-canonical | Recorded, not adopted; no gate, paper text, or prior may cite it as established. (`GATES.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `P2-BETAV-CIRC-01 / Ward summary`.) |

## Frozen parameter domain

No frozen microscopic parameter domain exists in Paper 2. Therefore the domain of the phase gate's universal kill criterion is not defined. (`GATES.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `P2-PHASE-01 / Scope` and `Kill criterion`.)

The separate Programme policy says couplings, cutoff ratios, and density/`μ` ranges are to be registered before SI-1/SI-2, but gives no actual bounds. It is `Status: PROPOSED`, Programme-owned, and says paper-level gates are authoritative. (`sea-ice/SEA_ICE_PREREGISTRATION_POLICY.md` @ `315451829412067f2e86d3559975e36b1b2ee03c`, lines 1–10 and `## 4`; `sea-ice/SEA_ICE_RESEARCH_MAP.md` @ `315451829412067f2e86d3559975e36b1b2ee03c`, lines 3–11.)

## Programme prior art — separate evidence base

The locally available `0-programme` repository was inspected only at `315451829412067f2e86d3559975e36b1b2ee03c`, on local branch `programme/p2-lattice-ontology-01` with matching local remote-tracking ref `origin/programme/p2-lattice-ontology-01`; no fetch was performed.

`sea-ice/SEA_ICE_RESEARCH_MAP.md` exists at that commit. It is a PROPOSED, routing-only map and identifies `P2-CHANNEL-FREEZE-01 -> P2-PHASE-01 -> P2-MULTIPHASE-GRAV-01`. (`sea-ice/SEA_ICE_RESEARCH_MAP.md` @ `315451829412067f2e86d3559975e36b1b2ee03c`, lines 1–11 and 24–55.) The named `sea-ice/gate-stubs` branch was unavailable both as a local ref and locally stored remote-tracking ref; that is unavailable evidence, not proof of remote absence.

## Stability and physical admissibility

Paper 2 freezes no operational Hessian-positivity, free-energy/global-preference, metastability, susceptibility, causality/unitarity, or finite-density stability test. It uses “physically admissible stable” without a decision procedure. (`GATES.md` @ `1e8d56da124c2ae791fb7a00b23a188d329c56f8`, `P2-PHASE-01 / Scientific question` and `Scope`.)

The only criteria-like text found is the proposed Programme policy: stationary solution, frozen-channel condensates, well-defined quadratic fluctuation operator, no established-gate exclusion, parameters in the registered domain, and no new interaction/degree of freedom. It gives no positivity, global-comparison, or numerical-bound rule. (`sea-ice/SEA_ICE_PREREGISTRATION_POLICY.md` @ `315451829412067f2e86d3559975e36b1b2ee03c`, `## 2`.)

## Conclusion

At the evidence bases, `P2-PHASE-01` is not runnable. The channel inventory exists, but the dependency interpretation, parameter domain, effective-action/finite-density input contract, and operational admissibility criteria are not all frozen. The smallest prior work indicated is a dependency ruling, a microscopic-parameter-domain artifact, and a phase input/admissibility contract. This is an inventory conclusion, not a proposed physics method or scientific result.
