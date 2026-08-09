"""Regression anchors for the generator-sum criticality derivation.

These import and run the real derivation functions (no re-typed results) and
check them against this repository's own computed values, with a
mutation-detection companion on the headline ratio so the anchor is shown to
discriminate.
"""

import sympy as sp

from scripts import p2_generator_sum_criticality as gsc


# ---------------------------------------------------------------------------
# Frozen generator normalisation Tr(lam^A lam^B) = 2 delta_AB, N = 2,3,4
# ---------------------------------------------------------------------------
def test_generator_normalisation_2deltaAB():
    for n in (2, 3, 4):
        gens = gsc.build_generators(n)
        assert len(gens) == n * n
        assert gsc.check_normalisation(gens) is True


def test_completeness_relation_holds():
    # The Fierz completeness the rearrangement needs, verified from the
    # explicitly constructed bases (a consequence of the frozen facts).
    for n in (2, 3, 4):
        assert gsc.check_completeness(gsc.build_generators(n)) is True


def test_singlet_projection_factor_is_two():
    # sum_A lam^A Tr(lam^A) = 2 * Id_N for every N; the "2" is computed.
    for n in (2, 3, 4):
        assert gsc.singlet_projection_factor(gsc.build_generators(n)) == 2


# ---------------------------------------------------------------------------
# Control: 1 = 2 G_c I0 (P2-GAP-01), reproduced
# ---------------------------------------------------------------------------
def test_control_reproduces_p2_gap_01():
    control = gsc.control_channel_form()
    assert control["reproduces_P2_GAP_01"] is True
    assert control["prefactor_channel"] == "2"
    assert control["Gc_channel"] == "1/(2*I0)"


# ---------------------------------------------------------------------------
# Generator-sum gap equation and the ratio, computed by the script
# ---------------------------------------------------------------------------
def test_generator_sum_prefactor_and_Gc():
    I0 = sp.Symbol("I0", positive=True)
    for n in (2, 3, 4):
        entry = gsc.analyse(n)
        # gap prefactor 8/N, computed from the reduced sum_A lam^A Tr(lam^A)
        assert sp.simplify(
            sp.sympify(entry["gap_prefactor_generator_sum_canonicalG"])
            - sp.Rational(8, n)
        ) == 0
        # critical coupling N/(8 I0)  (parse with the shared I0 symbol)
        gc = sp.sympify(
            entry["Gc_generator_sum_canonicalG"], locals={"I0": I0}
        )
        assert sp.simplify(gc - n / (8 * I0)) == 0


def test_ratio_is_N_and_discriminates():
    for n in (2, 3, 4):
        ratio = sp.sympify(gsc.analyse(n)["ratio_Gc_gen_over_singlet"])
        assert ratio == n
        # mutation-detection companion: the ratio is genuinely N, not 1
        # (a "transfers unchanged" result would give 1 for every N).
        assert ratio != 1


def test_exploratory_correction_factor_is_N_over_4():
    for n in (2, 3, 4):
        factor = sp.sympify(
            gsc.analyse(n)["exploratory_correction_factor_vs_half_I0"]
        )
        assert factor == sp.Rational(n, 4)
