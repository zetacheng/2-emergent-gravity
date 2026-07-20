# SI-1 dependency record (`P2-SI1-UNBLOCK-01`)

Governance clarification of the operational dependency graph, 2026-07-20. Not a
scientific verdict; no gate outcome, claim status, or numerical value changed.

## SI-1 may begin

The following SI-1 activities consume **no** historical Finding 5 numerical
value and may proceed:

- channel-basis freeze (`P2-CHANNEL-FREEZE-01`);
- Fierz-basis registration;
- parameter-domain registration;
- phase registration (`P2-PHASE-01`);
- pre-registration of the SI-2 health metrics.

## Historical Finding 5 remains quarantined

```
β_V/β_B = −3.2(5)
status  = unreproduced   (historical pipeline NOT LOCATED)
gate    = P2-BETAV-CIRC-01 = SUSPENDED
```

It must not be cited as validated numerical evidence anywhere downstream.

## SI-2 numerical kernel work — permitted vector inputs

The `P2-MULTIPHASE-GRAV-01` (SI-2) numerical graviton-kernel evaluation must use
**exactly one** of:

- **A.** `P2-BETAV-RECON-01` **after** it has status `PASS` (a reconstructed
  curved-background lattice Proca pipeline; currently `PROPOSED`, not run); or
- **B.** the pinned **analytic** vector input from Paper 3:
  - repository `zetacheng/3-vector-sector`
  - commit `8c363ef08368f5c022278ea5f36e01496be3d5ca`
  - claim `P3-C-001`
  - gate `P3-FIERZ-01`

## Conditions on path B

- Path B must be **frozen in `P2-CHANNEL-FREEZE-01` before** any SI-2
  computation.
- Path B is **repulsive** (`G_ω = −G/N`; `D_00 = g_0/(1+g_0Π_V) → 1/Π_V`) and is
  an **honest-prior headwind**, not a rescue mechanism.
- Path B receives **no validation** from the suspended Finding 5 lattice value
  `−3.2(5)`. Using the suspended value to validate its own replacement would
  close a circular provenance loop and is prohibited.

## Follow-up sequence

`P2-CHANNEL-FREEZE-01` → `P2-PHASE-01`, with `P2-BETAV-RECON-01` proceeding in
parallel, all **before** any `P2-MULTIPHASE-GRAV-01` numerical execution.
