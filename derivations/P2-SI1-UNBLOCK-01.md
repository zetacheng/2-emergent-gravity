# Governance clarification — `P2-SI1-UNBLOCK-01`

**Kind:** governance clarification (dependency graph). **Not a scientific
verdict, not a bypass, not a PASS for any suspended gate.**

## 1. Historical audit and operational dependency are distinct questions

Two different questions have been conflated by the blanket "SI-1 depends on
`P2-BETAV-CIRC-01`" wording:

- **Historical audit** — `P2-BETAV-CIRC-01`: *was the historical Finding 5
  lattice pipeline circular?* This is about that specific (absent) code.
- **Operational dependency** — *what numerical vector input does SI-1/SI-2
  actually consume?* This is about what feeds `K_ij(p)`.

These are not interchangeable. The provenance failure of the historical audit
must not permanently block SI-1 activities that **do not consume the historical
lattice value**.

## 2. `P2-BETAV-CIRC-01` remains SUSPENDED

Unchanged. The historical Finding 5 pipeline was NOT LOCATED
(`results/P2-BETAV-CIRC-01/PROVENANCE_SEARCH.md`); circularity can be neither
demonstrated nor ruled out. This clarification does not alter that status.

## 3. Finding 5's `β_V/β_B = −3.2(5)` remains unreproduced

Unchanged. It has no archived provenance and is reproduced nowhere in this
repository.

## 4. SI-1 activities that do NOT consume the historical value may proceed

The following consume no historical Finding 5 numerical value and may proceed:

- channel-basis freeze (`P2-CHANNEL-FREEZE-01`);
- Fierz-basis registration;
- parameter-domain registration;
- phase catalogue (`P2-PHASE-01`);
- pre-registration of the SI-2 health metric.

## 5. This is not a bypass and not a PASS for the historical gate

Nothing here upgrades `P2-BETAV-CIRC-01`, `P2-BETAV-ASSEMBLY-01`, or
`P2-BETAV-RECON-01`. No suspended gate is treated as passed.

## 6. No downstream computation may cite `−3.2(5)` as validated evidence

The suspended historical lattice value is quarantined. It must not appear as a
validated numerical input to any SI-1 or SI-2 computation.

## 7. Permitted numerical vector-sector inputs (future)

Future numerical vector-sector work must use exactly one of:

- **(a)** `P2-BETAV-RECON-01` **after it has actually PASSED** (a new
  reconstructed pipeline; currently PROPOSED, not run); or
- **(b)** a separately pre-registered **analytic** vector-sector input sourced
  from Paper 3 (locked in §Provenance below).

---

## Provenance lock — the analytic vector-sector input (Task 2)

The analytic vector input is **not** described generically. Its exact
provenance:

- **Repository:** `zetacheng/3-vector-sector`
- **Pinned commit:** `8c363ef08368f5c022278ea5f36e01496be3d5ca`
- **Claim:** `P3-C-001`
- **Gate:** `P3-FIERZ-01`
- **Frozen sign / coupling structure:** `G_ω = −G/N`. The vector channel is
  **repulsive**.
- **Response saturates / screens:** `D_00 = g_0 / (1 + g_0 Π_V) → 1/Π_V`, so
  increasing the nominal vector coupling does not automatically strengthen
  anything.

**This analytic vector input is a headwind for healthy gravity, not a rescue
mechanism.**

### Validation boundary (prevents a circular provenance loop)

- The analytic input **is validated** by the pinned Paper 3 sign/Fierz result
  (`P3-C-001` / `P3-FIERZ-01` at `8c363ef`).
- The analytic input is **NOT validated** by Finding 5's historical lattice
  value `−3.2(5)`.
- The suspended historical lattice value **must not** be used to validate the
  analytic replacement path. Doing so would close a circular provenance loop
  (using an unreproduced, suspended value to validate its own replacement).

## Status

Governance clarification only. No gate outcome, claim status, numerical value,
or scientific tolerance is changed by this note.
