"""GAP-A: is the Barnes-Rivers spin-2 subspace the span of TT_RECIPES?

Bounded structural identification, P2-GAPA-BRIDGE-01.  Pure linear algebra on
real symmetric 4x4 matrices.  No propagator, no lattice sum, no loop integral,
no dynamical quantity, and no coupling of any kind is evaluated here.

Two conjuncts are answered:

  D1/D2  span(TT_RECIPES) == Im(P2)  as subspaces of Sym^2(R^4)
  D3     the complement of Im(P2) is the set EXT-01 enumerates as discarded,
         component by component

D1 is symbolic (sympy, symbolic momentum q0).  D2 is numerical (numpy, SVD)
and reconstructs both subspaces by a different route.  They are independent
implementations of the same formal definitions, not independent evidence.

Definitions are read from the repository, not reconstructed from memory:
  Barnes-Rivers  scripts/recovered_2026/tt_check.py:105-126
                 scripts/recovered_2026/seagull_check.py:241-253
  TT_RECIPES     scripts/recovered_2026/mlog_coeff.py:24-31
  discarded      derivations/P2-RECON-EXT-01_discarded-external-space.md:74-78
"""

import numpy as np
import sympy as sp

D = 4  # spacetime dimension, from tt_check.py's np.eye(4)
TRACE_DENOM = 3  # the trace coefficient tt_check.py:119 writes as / 3.0

# ---------------------------------------------------------------- basis ----
# Orthonormal basis of Sym^2(R^4) under the Frobenius inner product, in the
# order EXT-01 lists PAIRS: (a, b) for a in range(4) for b in range(a, 4).
PAIRS = [(a, b) for a in range(D) for b in range(a, D)]


def basis_matrix(pair):
    """Unit-Frobenius symmetric matrix for one PAIRS slot."""
    a, b = pair
    M = np.zeros((D, D))
    if a == b:
        M[a, a] = 1.0
    else:
        M[a, b] = M[b, a] = 1.0 / np.sqrt(2.0)
    return M


BASIS = [basis_matrix(p) for p in PAIRS]


def to_coords(M):
    """Coordinates of a symmetric matrix in BASIS (Frobenius-orthonormal)."""
    return np.array([np.sum(M * B) for B in BASIS])


def hmat_from_recipe(recipe):
    """A recipe's h-matrix, following seagull_check.hmat: h[a,b] += v and,
    for a != b, h[b,a] += v as well."""
    M = np.zeros((D, D))
    for (a, b), c in recipe:
        M[a, b] += c
        if a != b:
            M[b, a] += c
    return M


# The five recipes, transcribed from mlog_coeff.py:24-31.
TT_RECIPES = [
    [((1, 1), 1 / np.sqrt(2)), ((2, 2), -1 / np.sqrt(2))],
    [((1, 1), 1 / np.sqrt(6)), ((2, 2), 1 / np.sqrt(6)),
     ((3, 3), -2 / np.sqrt(6))],
    [((1, 2), 1 / np.sqrt(2))],
    [((1, 3), 1 / np.sqrt(2))],
    [((2, 3), 1 / np.sqrt(2))],
]

# EXACT-RADICAL MIRRORS, for the symbolic path.  D1 must not be fed numpy
# floats: 1/sqrt(6) as a float leaves a 5.6e-17 residual that an exact symbolic
# comparison reads as "not fixed by P2", which is a defect of the check and not
# a result.  These are verified against the float tables below before use.
TT_RECIPES_EXACT = [
    [((1, 1), 1 / sp.sqrt(2)), ((2, 2), -1 / sp.sqrt(2))],
    [((1, 1), 1 / sp.sqrt(6)), ((2, 2), 1 / sp.sqrt(6)),
     ((3, 3), -2 / sp.sqrt(6))],
    [((1, 2), 1 / sp.sqrt(2))],
    [((1, 3), 1 / sp.sqrt(2))],
    [((2, 3), 1 / sp.sqrt(2))],
]

DISCARDED_EXACT = {
    "D1": [((0, 0), sp.Integer(1))],
    "D2": [((0, 1), 1 / sp.sqrt(2))],
    "D3": [((0, 2), 1 / sp.sqrt(2))],
    "D4": [((0, 3), 1 / sp.sqrt(2))],
    "D5": [((1, 1), 1 / sp.sqrt(3)), ((2, 2), 1 / sp.sqrt(3)),
           ((3, 3), 1 / sp.sqrt(3))],
}


def exact_coords(recipe):
    """Coordinates of an exact-radical recipe in BASIS, symbolically."""
    v = [sp.Integer(0)] * len(PAIRS)
    for (a, b), c in recipe:
        idx = PAIRS.index((a, b) if a <= b else (b, a))
        v[idx] = sp.simplify(v[idx] + (c if a == b else c * sp.sqrt(2)))
    return sp.Matrix(v)


# The five discarded components, transcribed from EXT-01 :74-78.
DISCARDED = {
    "D1": [((0, 0), 1.0)],
    "D2": [((0, 1), 1 / np.sqrt(2))],
    "D3": [((0, 2), 1 / np.sqrt(2))],
    "D4": [((0, 3), 1 / np.sqrt(2))],
    "D5": [((1, 1), 1 / np.sqrt(3)), ((2, 2), 1 / np.sqrt(3)),
           ((3, 3), 1 / np.sqrt(3))],
}


# ------------------------------------------------------- D1: symbolic ------
def d1_symbolic():
    """Barnes-Rivers P2 built symbolically from the repository formula, at a
    symbolic axial momentum q = (q0, 0, 0, 0)."""
    q0 = sp.Symbol("q0", positive=True)
    q = sp.Matrix([q0, 0, 0, 0])
    q2 = (q.T * q)[0]
    om = sp.Matrix(D, D, lambda a, b: sp.simplify(q[a] * q[b] / q2))
    th = sp.eye(D) - om

    def P2(a, b, c, d):
        return sp.simplify(
            sp.Rational(1, 2) * (th[a, c] * th[b, d] + th[a, d] * th[b, c])
            - th[a, b] * th[c, d] / TRACE_DENOM)

    def P1(a, b, c, d):
        return sp.simplify(sp.Rational(1, 2) * (
            th[a, c] * om[b, d] + th[a, d] * om[b, c]
            + th[b, c] * om[a, d] + th[b, d] * om[a, c]))

    def P0s(a, b, c, d):
        return sp.simplify(th[a, b] * th[c, d] / TRACE_DENOM)

    def P0w(a, b, c, d):
        return sp.simplify(om[a, b] * om[c, d])

    def as_map(P):
        """P as a 10x10 matrix on Sym^2(R^4) in the orthonormal BASIS.

        (P h)_{ab} = sum_{c,d} P[a,b,c,d] h_{cd}, summed over ALL c and d.
        """
        cols = []
        for Bk in BASIS:
            img = sp.zeros(D, D)
            for a in range(D):
                for b in range(D):
                    img[a, b] = sum(P(a, b, c, d) * sp.nsimplify(Bk[c, d])
                                    for c in range(D) for d in range(D))
            cols.append(sp.Matrix([sum(img[a, b] * sp.nsimplify(Bj[a, b])
                                       for a in range(D) for b in range(D))
                                   for Bj in BASIS]))
        return sp.simplify(sp.Matrix.hstack(*cols))

    M2 = as_map(P2)
    M1 = as_map(P1)
    M0s = as_map(P0s)
    M0w = as_map(P0w)
    return q0, M2, M1, M0s, M0w


# ------------------------------------------------------ D2: numerical ------
def br_arrays(q):
    """The four Barnes-Rivers projector arrays, exactly as tt_check.py builds
    them, by explicit quadruple loop."""
    q = np.asarray(q, dtype=float)
    q2 = np.dot(q, q)
    om = np.outer(q, q) / q2
    th = np.eye(D) - om
    P2 = np.zeros((D, D, D, D))
    P1 = np.zeros((D, D, D, D))
    for a in range(D):
        for b in range(D):
            for c in range(D):
                for d in range(D):
                    P2[a, b, c, d] = (0.5 * (th[a, c] * th[b, d]
                                             + th[a, d] * th[b, c])
                                      - th[a, b] * th[c, d] / 3.0)
                    P1[a, b, c, d] = 0.5 * (th[a, c] * om[b, d]
                                            + th[a, d] * om[b, c]
                                            + th[b, c] * om[a, d]
                                            + th[b, d] * om[a, c])
    P0s = np.einsum("ab,cd->abcd", th, th) / 3.0
    P0w = np.einsum("ab,cd->abcd", om, om)
    return P2, P1, P0s, P0w


def seagull_p2(q):
    """The SECOND repository implementation, seagull_check.py:241-253."""
    q = np.asarray(q, float)
    om = np.outer(q, q) / np.dot(q, q)
    th = np.eye(4) - om
    P2 = np.zeros((4, 4, 4, 4))
    for a in range(4):
        for b in range(4):
            for cc in range(4):
                for d in range(4):
                    P2[a, b, cc, d] = (0.5 * (th[a, cc] * th[b, d]
                                              + th[a, d] * th[b, cc])
                                       - th[a, b] * th[cc, d] / 3.0)
    return P2


def as_map_numeric(P):
    """P as a 10x10 matrix on Sym^2(R^4), built by applying P to each basis
    matrix and projecting back — a different route from D1's."""
    cols = []
    for Bk in BASIS:
        img = np.einsum("abcd,cd->ab", P, Bk)
        cols.append(to_coords(img))
    return np.column_stack(cols)


def orth_basis(cols, tol):
    """Orthonormal basis of the column span, by SVD."""
    U, s, _ = np.linalg.svd(np.asarray(cols, dtype=float))
    r = int(np.sum(s > tol))
    return U[:, :r], s


def main():
    tol = 1e-10
    out = []

    def say(line=""):
        out.append(line)
        print(line)

    say("=" * 72)
    say("GAP-A  basis identification  (P2-GAPA-BRIDGE-01)")
    say("linear algebra only: no propagator, no lattice sum, no loop integral")
    say("=" * 72)

    # ---- the two subspaces, in coordinates --------------------------------
    R = np.column_stack([to_coords(hmat_from_recipe(r)) for r in TT_RECIPES])
    Dm = np.column_stack([to_coords(hmat_from_recipe(DISCARDED[k]))
                          for k in ("D1", "D2", "D3", "D4", "D5")])

    say("")
    say("-- convention check: both families unit-Frobenius, as recorded ------")
    say(f"   retained  norms  {np.round(np.linalg.norm(R, axis=0), 12)}")
    say(f"   discarded norms  {np.round(np.linalg.norm(Dm, axis=0), 12)}")
    G = np.column_stack([R, Dm]).T @ np.column_stack([R, Dm])
    say(f"   Gram of all ten vs I, max|G-I| = {np.max(np.abs(G - np.eye(10))):.3e}")

    # ---- D1: symbolic ------------------------------------------------------
    say("")
    say("-- D1  SYMBOLIC (sympy, symbolic q0) ----------------------------------")
    q0, M2s, M1s, M0ss, M0ws = d1_symbolic()
    say(f"   P2 map is independent of q0: {M2s.free_symbols == set()}")
    say(f"   rank Im(P2)  = {M2s.rank()}")
    say(f"   rank Im(P1)  = {M1s.rank()}")
    say(f"   rank Im(P0s) = {M0ss.rank()}")
    say(f"   rank Im(P0w) = {M0ws.rank()}")
    Z10 = sp.zeros(10, 10)
    say(f"   P2 idempotent (P2*P2 == P2): "
        f"{sp.simplify(M2s * M2s - M2s) == Z10}")
    say(f"   P2 symmetric  (P2^T == P2):  "
        f"{sp.simplify(M2s.T - M2s) == Z10}")
    say(f"   P2+P1+P0s+P0w == I:          "
        f"{sp.simplify(M2s + M1s + M0ss + M0ws - sp.eye(10)) == Z10}")

    Rs = sp.Matrix.hstack(*[exact_coords(r) for r in TT_RECIPES_EXACT])
    drift = float(np.max(np.abs(np.array(Rs.evalf(20), dtype=float) - R)))
    say(f"   exact-radical recipe table matches the float table: "
        f"max|diff| = {drift:.3e}")
    fixed = [sp.simplify(M2s * Rs[:, j] - Rs[:, j]) == sp.zeros(10, 1)
             for j in range(5)]
    say(f"   each recipe fixed by P2 (P2 v == v): {fixed}")
    joint = sp.Matrix.hstack(M2s, Rs)
    say(f"   rank[ Im(P2) | recipes ] = {joint.rank()}   (5 means same span)")
    Ds = sp.Matrix.hstack(*[exact_coords(DISCARDED_EXACT[k])
                            for k in ("D1", "D2", "D3", "D4", "D5")])
    killed = [sp.simplify(M2s * Ds[:, j]) == sp.zeros(10, 1) for j in range(5)]
    say(f"   each discarded component annihilated by P2: {killed}")
    d1_holds = (all(fixed) and joint.rank() == 5 and M2s.rank() == 5
                and all(killed) and drift < 1e-12)

    # ---- D2: numerical -----------------------------------------------------
    say("")
    say("-- D2  NUMERICAL (numpy, SVD, tol = 1e-10) ----------------------------")
    q = np.array([0.7, 0.0, 0.0, 0.0])  # q || e0, the direction TT_RECIPES fix
    P2, P1, P0s, P0w = br_arrays(q)
    say(f"   tt_check.py and seagull_check.py P2 arrays agree: "
        f"max|diff| = {np.max(np.abs(P2 - seagull_p2(q))):.3e}")
    A2 = as_map_numeric(P2)
    say(f"   rank(P2 map) = {np.linalg.matrix_rank(A2, tol=tol)}")
    say(f"   ||P2*P2 - P2||_F = {np.linalg.norm(A2 @ A2 - A2):.3e}")
    say(f"   ||P2^T - P2||_F  = {np.linalg.norm(A2.T - A2):.3e}")

    Q_recipes = R @ np.linalg.pinv(R.T @ R) @ R.T
    resid = np.linalg.norm(A2 - Q_recipes)
    say(f"   projector difference ||P2map - Q_span(recipes)||_F = {resid:.3e}")
    say(f"   tolerance = {tol:.1e}   ->  equal: {resid < tol}")
    Ub, s_all = orth_basis(np.column_stack([A2, R]), tol)
    say(f"   rank[ P2map | recipes ] = {Ub.shape[1]}   singular values "
        f"{np.array2string(s_all[:7], precision=4)}")
    d2_holds = (np.linalg.matrix_rank(A2, tol=tol) == 5
                and resid < tol and Ub.shape[1] == 5)

    # ---- D3: the second conjunct, component by component -------------------
    say("")
    say("-- D3  THE COMPLEMENT, COMPONENT BY COMPONENT -------------------------")
    A1 = as_map_numeric(P1)
    A0s = as_map_numeric(P0s)
    A0w = as_map_numeric(P0w)
    blocks = {"P1": A1, "P0s": A0s, "P0w": A0w}
    per_component = {}
    for name in ("D1", "D2", "D3", "D4", "D5"):
        v = to_coords(hmat_from_recipe(DISCARDED[name]))
        killed_by_P2 = np.linalg.norm(A2 @ v)
        fixed_by = [b for b, Ab in blocks.items()
                    if np.linalg.norm(Ab @ v - v) < tol]
        per_component[name] = (killed_by_P2, fixed_by)
        say(f"   {name}: ||P2 v|| = {killed_by_P2:.3e}   fixed by {fixed_by}")

    comp_rank = np.linalg.matrix_rank(Dm, tol=tol)
    A_non = A1 + A0s + A0w
    resid_c = np.linalg.norm(A_non - Dm @ np.linalg.pinv(Dm.T @ Dm) @ Dm.T)
    say(f"   rank(span D1..D5) = {comp_rank}")
    say(f"   ||(P1+P0s+P0w) - Q_span(D1..D5)||_F = {resid_c:.3e}")
    d3_holds = (comp_rank == 5 and resid_c < tol
                and all(k < tol and len(f) == 1
                        for k, f in per_component.values()))

    # ---- direction dependence, measured rather than assumed ---------------
    say("")
    say("-- BOUNDING THE CLAIM: which momentum directions it holds for --------")
    say("   TT_RECIPES are hard-coded for q || e0 (mlog_coeff.py:21, :38).")
    say("   The Barnes-Rivers projectors are built from q. Measured:")
    dirs = {
        "e0 (the axis TT_RECIPES fix)": [0.7, 0.0, 0.0, 0.0],
        "e1": [0.0, 0.7, 0.0, 0.0],
        "e2": [0.0, 0.0, 0.7, 0.0],
        "e3": [0.0, 0.0, 0.0, 0.7],
        "diagonal (1,1,1,1)": [0.5, 0.5, 0.5, 0.5],
        "e0 rescaled (q0 = 13.0)": [13.0, 0.0, 0.0, 0.0],
    }
    dir_rows = []
    for name, qd in dirs.items():
        Ad = as_map_numeric(br_arrays(qd)[0])
        rd = np.linalg.norm(Ad - Q_recipes)
        dir_rows.append((name, rd))
        say(f"   {name:32s} ||P2map - Q_recipes||_F = {rd:.3e}"
            f"   equal: {rd < tol}")

    # ---- outcome -----------------------------------------------------------
    say("")
    say("=" * 72)
    say(f"D1 (symbolic) first conjunct : {d1_holds}")
    say(f"D2 (numerical) first conjunct: {d2_holds}")
    say(f"D3 second conjunct           : {d3_holds}")
    say(f"D1 and D2 agree              : {d1_holds == d2_holds}")
    say("=" * 72)
    return 0 if (d1_holds and d2_holds and d3_holds) else 1


if __name__ == "__main__":
    raise SystemExit(main())
