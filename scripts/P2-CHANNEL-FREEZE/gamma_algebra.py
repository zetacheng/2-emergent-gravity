"""Primitive exact matrix operations; no frozen basis or conventions live here."""

import sympy as sp


def gamma_factory(metric):
    """Return an exact 4x4 Clifford representation for the parsed diagonal metric."""
    if tuple(metric) != (sp.Integer(1),) * 4:
        raise ValueError("unsupported metric signature")
    imag = sp.I
    pauli = (
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -imag], [imag, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    )
    zero, unit = sp.zeros(2), sp.eye(2)

    def block(a, b, c, d):
        return a.row_join(b).col_join(c.row_join(d))

    return [block(zero, -imag * s, imag * s, zero) for s in pauli] + [
        block(zero, unit, unit, zero)
    ]
