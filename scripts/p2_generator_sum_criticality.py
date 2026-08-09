"""Generator-sum mean-field scalar criticality (P2-PHASE-01 open item).

Symbolic derivation, carried out with explicit U(N) generators, of whether
``G_c = 1/(2 I_0)`` (P2-GAP-01, singlet-only form) transfers to the full
U(N) generator-sum canonical interaction under the uniform flavour-singlet
scalar condensate.

Everything below is *computed*: the generators are built explicitly, the
frozen normalisation ``Tr(lam^A lam^B) = 2 delta_AB`` and the completeness
relation are verified against the constructed bases, and the mean-field
combinatorial factor is read off the reduced ``sum_A lam^A Tr(lam^A)``. The
only external numbers are the frozen ``Tr(Id4) = 4`` and the P2-GAP-01
Hartree factor 2.

Run: ``python -m scripts.p2_generator_sum_criticality``.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

# Frozen inputs (Phase-A freeze / P2-GAP-01), stated once.
TR_ID4 = sp.Integer(4)          # trace(Id4), freeze section C
HARTREE_FACTOR = sp.Integer(2)  # two placements of the mean field on O^2

RESULT_PATH = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "P2-PHASE-01"
    / "generator-sum-criticality"
    / "criticality.json"
)


def build_generators(n: int) -> list[sp.Matrix]:
    """Complete Hermitian U(N) basis, ``Tr(lam^A lam^B) = 2 delta_AB``.

    Index 0 is the singlet ``lam^0 = sqrt(2/N) 1_N``; the remaining
    ``N**2 - 1`` are the SU(N) generators (symmetric off-diagonal,
    antisymmetric off-diagonal, diagonal Cartan), all normalised to 2.
    """
    gens: list[sp.Matrix] = [sp.sqrt(sp.Rational(2, n)) * sp.eye(n)]
    for i in range(n):
        for j in range(i + 1, n):
            sym = sp.zeros(n)
            sym[i, j] = 1
            sym[j, i] = 1
            gens.append(sym)
            asym = sp.zeros(n)
            asym[i, j] = -sp.I
            asym[j, i] = sp.I
            gens.append(asym)
    for k in range(1, n):
        diag = sp.zeros(n)
        for a in range(k):
            diag[a, a] = 1
        diag[k, k] = -k
        gens.append(sp.sqrt(sp.Rational(2, k * (k + 1))) * diag)
    return gens


def check_normalisation(gens: list[sp.Matrix]) -> bool:
    """Verify ``Tr(lam^A lam^B) = 2 delta_AB`` exactly."""
    m = len(gens)
    for a in range(m):
        for b in range(m):
            want = 2 if a == b else 0
            got = sp.simplify((gens[a] * gens[b]).trace())
            if got != want:
                return False
    return True


def check_completeness(gens: list[sp.Matrix]) -> bool:
    """Verify ``sum_A lam^A_ij lam^A_kl = 2 delta_il delta_kj`` exactly."""
    n = gens[0].shape[0]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for ll in range(n):
                    got = sp.simplify(
                        sum(g[i, j] * g[k, ll] for g in gens)
                    )
                    want = 2 if (i == ll and k == j) else 0
                    if got != want:
                        return False
    return True


def sum_lambda_trace(gens: list[sp.Matrix]) -> sp.Matrix:
    """``sum_A lam^A Tr(lam^A)`` — only the singlet survives."""
    n = gens[0].shape[0]
    acc = sp.zeros(n)
    for g in gens:
        acc += g * g.trace()
    return sp.simplify(acc)


def singlet_projection_factor(gens: list[sp.Matrix]) -> sp.Expr:
    """Diagonal value of ``sum_A lam^A Tr(lam^A)`` (equals 2 for every N)."""
    mat = sum_lambda_trace(gens)
    n = gens[0].shape[0]
    # confirm it is a multiple of the identity, return that multiple
    val = sp.simplify(mat[0, 0])
    assert mat == val * sp.eye(n), "sum_A lam^A Tr(lam^A) is not scalar"
    return val


def analyse(n: int) -> dict:
    """Full mean-field analysis for a given N."""
    gens = build_generators(n)
    assert len(gens) == n * n, "basis is not complete"
    norm_ok = check_normalisation(gens)
    comp_ok = check_completeness(gens)
    s = singlet_projection_factor(gens)  # computed factor (= 2)

    G, I0 = sp.symbols("G I0", positive=True)

    # Generator-sum: Sigma_ij = (G/N) * (sum_A lam^A Tr lam^A)_ij * Phi
    #              = (G/N) * s * Phi * delta_ij  ->  per-flavour mass (s G/N) Phi.
    # Tadpole Phi = -TR_ID4 * m * I0.  Gap prefactor (canonical G):
    prefactor_gen = sp.simplify(sp.Rational(1, n) * s * TR_ID4)  # = 8/N
    gc_gen = sp.simplify(1 / (prefactor_gen * I0))               # = N/(8 I0)

    # Control (a), coefficient-in-front G_N: Hartree 2 * trace 4 = 8.
    prefactor_singlet = sp.simplify(HARTREE_FACTOR * TR_ID4)     # = 8
    gc_singlet = sp.simplify(1 / (prefactor_singlet * I0))       # = 1/(8 I0)

    ratio = sp.simplify(gc_gen / gc_singlet)                     # = N
    # Consequence for the exploratory work, which applied 1 = 2 G I0
    # (channel value G_c = 1/(2 I0)) to the canonical coupling:
    gc_channel = sp.simplify(1 / (2 * I0))
    consequence = sp.simplify(gc_gen / gc_channel)               # = N/4

    return {
        "N": n,
        "basis_size": len(gens),
        "normalisation_2deltaAB": norm_ok,
        "completeness_verified": comp_ok,
        "singlet_projection_factor": str(s),
        "gap_prefactor_generator_sum_canonicalG": str(prefactor_gen),
        "gap_equation_generator_sum": f"1 = ({prefactor_gen}) * G * I0",
        "Gc_generator_sum_canonicalG": str(gc_gen),
        "gap_prefactor_singlet_coeff_in_front": str(prefactor_singlet),
        "Gc_singlet_coeff_in_front": str(gc_singlet),
        "ratio_Gc_gen_over_singlet": str(ratio),
        "exploratory_correction_factor_vs_half_I0": str(consequence),
    }


def control_channel_form() -> dict:
    """Control in P2-GAP-01 channel units: 1 = 2 G I0, G = 4 G_N."""
    G, GN, I0 = sp.symbols("G G_N I0", positive=True)
    # 1 = 8 G_N I0 ; absorb trace: G = 4 G_N -> 1 = 2 G I0
    gap_singlet_GN = sp.Eq(1, sp.simplify(HARTREE_FACTOR * TR_ID4) * GN * I0)
    G_channel = 4 * GN
    prefactor_channel = sp.simplify(
        (HARTREE_FACTOR * TR_ID4 * GN) / G_channel
    )  # = 2
    gc_channel = sp.simplify(1 / (prefactor_channel * I0))  # 1/(2 I0)
    return {
        "gap_singlet_only_in_GN": str(gap_singlet_GN),
        "G_channel_equals": "4*G_N",
        "prefactor_channel": str(prefactor_channel),
        "Gc_channel": str(gc_channel),
        "reproduces_P2_GAP_01": prefactor_channel == 2
        and gc_channel == sp.simplify(1 / (2 * sp.Symbol("I0", positive=True))),
    }


def build_report() -> dict:
    per_n = [analyse(n) for n in (2, 3, 4)]
    control = control_channel_form()
    n_sym = sp.Symbol("N", positive=True)
    return {
        "gate": "P2-PHASE-01 (open item: generator-sum criticality)",
        "frozen_inputs": {
            "Tr_Id4": str(TR_ID4),
            "hartree_factor": str(HARTREE_FACTOR),
            "generator_normalisation": "Tr(lam^A lam^B) = 2*delta_AB",
            "singlet": "lam^0 = sqrt(2/N)*Id_N",
        },
        "control_singlet_only": control,
        "generator_sum_symbolic": {
            "gap_equation": "1 = (8/N) * G * I0",
            "Gc_canonicalG": "N/(8*I0)",
            "ratio_Gc_gen_over_singlet_symbolic": str(n_sym),
            "exploratory_correction_factor_symbolic": str(n_sym / 4),
            "case": "N-dependent",
        },
        "per_N": per_n,
        "verdict": (
            "G_c = 1/(2 I0) is the trace-absorbed channel-coupling result "
            "of the singlet-only gap; it does NOT transfer to the canonical "
            "coupling G of the generator sum, where 1 = (8/N) G I0 and "
            "G_c = N/(8 I0). Ratio (coefficient-in-front) = N; equals 1 only "
            "at N=1. The exploratory G/G_c positions carry an N/4 factor."
        ),
    }


def main() -> None:
    report = build_report()
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {RESULT_PATH}")
    for entry in report["per_N"]:
        print(
            f"N={entry['N']}: gap 1=({entry['gap_prefactor_generator_sum_canonicalG']})"
            f" G I0 ; Gc={entry['Gc_generator_sum_canonicalG']} ;"
            f" ratio={entry['ratio_Gc_gen_over_singlet']}"
        )


if __name__ == "__main__":
    main()
