"""
Condensate-boson (real scalar) one-loop contribution to the induced
graviton kernel on the lattice.

Scalar action (forward differences, no doublers), minimal coupling:
  S = sum_x [ (1/2) sum_{mu nu} J^{mu nu}(x) (D_mu phi)(x) (D_nu phi)(x)
              + (1/2) edet(x) m_B^2 phi(x)^2 ],
  J = sqrt(g) g^{-1}  (exact),  D_mu phi(x) = phi(x+mu) - phi(x).

Momentum space:  M_B(k; h) = sum_{mu nu} J^{mu nu} abar_mu(k) a_nu(k)
                              + edet m_B^2,
with a_mu(k) = e^{i k_mu} - 1  (flat: sum_mu 4 sin^2(k_mu/2) + m^2).

Boson loop:  Gamma_B[h] = +(1/2) <ln M_B(h)>   (real scalar, per dof)
Kernel = bubble + seagull, vertices from exact numerical derivatives
of J(h), edet(h);  validated against constant-h second differences.

Orientation decomposition as in the fermion case:
  slope(axis) = Z + 0.4 c4 ; slope(face) = Z + c4/3 ; slope(diag) = Z + 0.3 c4.
"""

import numpy as np
from seagull_check import PAIRS, hmat, fit_even, projectors, to_tensor, EPSF


def geomB(h):
    g = np.eye(4) + h
    w, v = np.linalg.eigh(g)
    edet = np.prod(np.sqrt(w))
    ginv = v @ np.diag(1.0 / w) @ v.T
    return edet * ginv, edet          # J, edet


def derivsB():
    dJ, dE, d2J, d2E = {}, {}, {}, {}
    J0, e0 = geomB(np.zeros((4, 4)))
    for p in PAIRS:
        Jp, ep = geomB(hmat([(p, +EPSF)]))
        Jm, em = geomB(hmat([(p, -EPSF)]))
        dJ[p] = (Jp - Jm) / (2 * EPSF)
        dE[p] = (ep - em) / (2 * EPSF)
    for p1 in PAIRS:
        d2J[p1], d2E[p1] = {}, {}
        for p2 in PAIRS:
            if p1 == p2:
                Jp, ep = geomB(hmat([(p1, +EPSF)]))
                Jm, em = geomB(hmat([(p1, -EPSF)]))
                d2J[p1][p2] = (Jp - 2 * J0 + Jm) / EPSF**2
                d2E[p1][p2] = (ep - 2 * e0 + em) / EPSF**2
            else:
                acc_J, acc_e = 0.0, 0.0
                for sa, sb in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    Jx, ex = geomB(hmat([(p1, sa * EPSF), (p2, sb * EPSF)]))
                    s = sa * sb
                    acc_J = acc_J + s * Jx
                    acc_e = acc_e + s * ex
                d2J[p1][p2] = acc_J / (4 * EPSF**2)
                d2E[p1][p2] = acc_e / (4 * EPSF**2)
    return dJ, dE, d2J, d2E


def kgrid(n):
    k1 = 2.0 * np.pi * np.arange(n) / n - np.pi
    grids = np.meshgrid(k1, k1, k1, k1, indexing="ij")
    return [g.ravel() for g in grids]


def MB_flat(kk, mB):
    return sum(4.0 * np.sin(kk[mu] / 2) ** 2 for mu in range(4)) + mB**2


def vertexB(kk, q, pair, dJ, dE, mB):
    """U_B(k,q): vertex between phi(k) and phi(k+q) legs.

    From J(x) carrying momentum q with the two forward differences:
    contraction  conj(a_mu(k)) * a_nu(k+q), symmetrized via J symmetry."""
    a1 = [np.exp(1j * kk[mu]) - 1.0 for mu in range(4)]
    a2 = [np.exp(1j * (kk[mu] + q[mu])) - 1.0 for mu in range(4)]
    U = np.zeros(kk[0].size, dtype=complex)
    for mu in range(4):
        for nu in range(4):
            c = dJ[pair][mu, nu]
            if abs(c) > 1e-12:
                U += c * 0.5 * (np.conj(a1[mu]) * a2[nu]
                                + a1[mu] * np.conj(a2[nu]))
    U += dE[pair] * mB**2
    return U


def seagullB(kk, d2J, d2E, mB, p1, p2):
    a = [np.exp(1j * kk[mu]) - 1.0 for mu in range(4)]
    V = np.zeros(kk[0].size, dtype=complex)
    for mu in range(4):
        for nu in range(4):
            c = d2J[p1][p2][mu, nu]
            if abs(c) > 1e-12:
                V += c * 0.5 * (np.conj(a[mu]) * a[nu]
                                + a[mu] * np.conj(a[nu]))
    V += d2E[p1][p2] * mB**2
    return V


def kernelB(q, n, mB, dJ, dE, d2J, d2E, want_seagull=True):
    kk = kgrid(n)
    kkq = [kk[mu] + q[mu] for mu in range(4)]
    G1, G2g = 1.0 / MB_flat(kk, mB), 1.0 / MB_flat(kkq, mB)
    mq = tuple(-x for x in q)
    U1 = {p: vertexB(kk, q, p, dJ, dE, mB) for p in PAIRS}
    U2 = {p: vertexB(kkq, mq, p, dJ, dE, mB) for p in PAIRS}
    K = {}
    for p1 in PAIRS:
        A = G1 * U1[p1] * G2g
        for p2 in PAIRS:
            bub = -(0.5) * (A * U2[p2]).mean().real
            sg = 0.0
            if want_seagull:
                sg = +(0.5) * (G1 * seagullB(kk, d2J, d2E, mB, p1, p2)
                               ).mean().real
            K[(p1, p2)] = bub + sg
    return K


def const_h_check(n, mB, dJ, dE, d2J, d2E):
    kk = kgrid(n)

    def gammaB(h):
        J, ed = geomB(h)
        a = [np.exp(1j * kk[mu]) - 1.0 for mu in range(4)]
        M = sum(J[mu, nu] * 0.5 * (np.conj(a[mu]) * a[nu]
                                    + a[mu] * np.conj(a[nu]))
                for mu in range(4) for nu in range(4)) + ed * mB**2
        return +0.5 * np.log(M.real).mean()

    g0 = gammaB(np.zeros((4, 4)))
    K0 = kernelB((1e-4, 0, 0, 0), n, mB, dJ, dE, d2J, d2E)
    print("  constant-h validation:")
    for p1, p2 in [((0, 0), (0, 0)), ((0, 1), (0, 1)), ((0, 0), (1, 1))]:
        if p1 == p2:
            gp = gammaB(hmat([(p1, +EPSF)]))
            gm = gammaB(hmat([(p1, -EPSF)]))
            ex = (gp - 2 * g0 + gm) / EPSF**2
        else:
            vv = [gammaB(hmat([(p1, sa * EPSF), (p2, sb * EPSF)]))
                  for sa, sb in [(1, 1), (1, -1), (-1, 1), (-1, -1)]]
            ex = (vv[0] - vv[1] - vv[2] + vv[3]) / (4 * EPSF**2)
        print(f"    {p1}{p2}: exact={ex:+.6e}  pert={K0[(p1,p2)]:+.6e}"
              f"  diff={abs(ex - K0[(p1, p2)]):.1e}")


def run(n=20, mB=0.5):
    dJ, dE, d2J, d2E = derivsB()
    print(f"SCALAR LOOP  (n={n}^4, m_B a = {mB})")
    const_h_check(16, mB, dJ, dE, d2J, d2E)
    eps = np.array([0.15, 0.25, 0.35, 0.45, 0.55])
    dirs = {"axis": lambda e: (e, 0, 0, 0),
            "face": lambda e: (e / np.sqrt(2), e / np.sqrt(2), 0, 0),
            "diag": lambda e: (e / 2, e / 2, e / 2, e / 2)}
    sl = {}
    for nm, pf in dirs.items():
        vals = []
        for e in eps:
            q = pf(e)
            G = to_tensor(kernelB(q, n, mB, dJ, dE, d2J, d2E))
            vals.append(np.einsum("abcd,abcd->", projectors(q), G) / 5.0)
        sl[nm] = fit_even(eps, np.array(vals))[1]
    Z = 4 * sl["diag"] - 3 * sl["axis"]
    c4 = 10 * (sl["axis"] - sl["diag"])
    pred = Z + c4 / 3
    dev = abs(pred - sl["face"]) / abs(sl["face"])
    print(f"  slopes: axis={sl['axis']:+.4e} face={sl['face']:+.4e}"
          f" diag={sl['diag']:+.4e}")
    print(f"  Z_cov^B = {Z:+.6e}   c4^B = {c4:+.6e}   "
          f"face check dev = {dev:.1%}")
    return Z, c4


if __name__ == "__main__":
    for mB in (0.25, 0.5, 1.0):
        run(20, mB)
