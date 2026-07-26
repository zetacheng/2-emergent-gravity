"""Exact Euclidean 4x4 Clifford algebra for the frozen Phase-A checker."""

import sympy as sp

IMAG = sp.I
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -IMAG], [IMAG, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
z, u = sp.zeros(2), sp.eye(2)


def block(a, b, c, d):
    return a.row_join(b).col_join(c.row_join(d))


GAMMAS = [block(z, -IMAG * s, IMAG * s, z) for s in (s1, s2, s3)] + [block(z, u, u, z)]
GAMMA5 = GAMMAS[0] * GAMMAS[1] * GAMMAS[2] * GAMMAS[3]


def sigma(mu, nu):
    return IMAG * (GAMMAS[mu] * GAMMAS[nu] - GAMMAS[nu] * GAMMAS[mu]) / 2


def basis():
    return (
        [("S", sp.eye(4)), ("P", GAMMA5)]
        + [("V", g) for g in GAMMAS]
        + [("A", IMAG * g * GAMMA5) for g in GAMMAS]
        + [("T", sigma(mu, nu)) for mu in range(4) for nu in range(mu + 1, 4)]
    )


def fierz_family_matrix():
    groups = {
        "S": [0],
        "P": [1],
        "V": list(range(2, 6)),
        "A": list(range(6, 10)),
        "T": list(range(10, 16)),
    }
    mats = [m for _, m in basis()]
    rows = []
    for src in groups.values():
        row = []
        for dst in groups.values():
            cs = [
                sp.simplify(
                    sum(
                        (
                            sp.trace(mats[i] * mats[j] * mats[i] * mats[j]) / 16
                            for i in src
                        ),
                        sp.S.Zero,
                    )
                )
                for j in dst
            ]
            assert len(set(cs)) == 1
            row.append(cs[0])
        rows.append(row)
    return sp.Matrix(rows)
