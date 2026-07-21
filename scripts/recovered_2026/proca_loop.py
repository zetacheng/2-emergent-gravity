"""
Lattice Proca loop: universal m^2 log m^2 coefficient of a massive
vector field coupled to a background metric.

Action (Euclidean, forward differences D_mu f(x) = f(x+mu)-f(x)):
  S = sum_x [ (1/4) J2^{mu alpha nu beta}(x) F_{mu nu} F_{alpha beta}
              + (m^2/2) J^{mu nu}(x) A_mu A_nu ],
  J2 = sqrt(g) g^{-1} (x) g^{-1},   J = sqrt(g) g^{-1}   (exact),
  F_{mu nu} = D_mu A_nu - D_nu A_mu.

Flat kernel: M(k) = (shat^2 + m^2) I - aconj (x) a,  a_mu = e^{ik_mu}-1:
  eigenvalues {shat^2+m^2 (x3 transverse), m^2 (x1 longitudinal)}.
Longitudinal mode has exactly no kinetic term on the lattice
(forward differences commute -> F[D phi] = 0): the compensating-
scalar structure of the Proca determinant is built in.

Loop sign: boson, Gamma = +(1/2) <ln det M>.
Target:   beta_V / beta_B = -3   (falsifiable; companion analytics).
"""

import numpy as np
from seagull_check import PAIRS, hmat, fit_even, EPSF
from mlog_coeff import TT_RECIPES, fit_mlog


def geomV(h):
    g = np.eye(4) + h
    w, v = np.linalg.eigh(g)
    edet = np.prod(np.sqrt(w))
    ginv = v @ np.diag(1.0 / w) @ v.T
    J2 = edet * np.einsum("ua,vb->uavb", ginv, ginv)
    return J2, edet * ginv


def derivsV():
    dJ2, dJ, d2J2, d2J = {}, {}, {}, {}
    J20, J0 = geomV(np.zeros((4, 4)))
    for p in PAIRS:
        Ap, ap = geomV(hmat([(p, +EPSF)]))
        Am, am = geomV(hmat([(p, -EPSF)]))
        dJ2[p] = (Ap - Am) / (2 * EPSF)
        dJ[p] = (ap - am) / (2 * EPSF)
    for p1 in PAIRS:
        d2J2[p1], d2J[p1] = {}, {}
        for p2 in PAIRS:
            if p1 == p2:
                Ap, ap = geomV(hmat([(p1, +EPSF)]))
                Am, am = geomV(hmat([(p1, -EPSF)]))
                d2J2[p1][p2] = (Ap - 2 * J20 + Am) / EPSF**2
                d2J[p1][p2] = (ap - 2 * J0 + am) / EPSF**2
            else:
                aJ2, aJ = 0.0, 0.0
                for sa, sb in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    Ax, ax = geomV(hmat([(p1, sa * EPSF), (p2, sb * EPSF)]))
                    aJ2 = aJ2 + sa * sb * Ax
                    aJ = aJ + sa * sb * ax
                d2J2[p1][p2] = aJ2 / (4 * EPSF**2)
                d2J[p1][p2] = aJ / (4 * EPSF**2)
    return dJ2, dJ, d2J2, d2J


def avec(kk):
    """a_mu(k) = e^{ik_mu}-1 as (npts,4) complex array."""
    return np.stack([np.exp(1j * kk[mu]) - 1.0 for mu in range(4)], axis=1)


def kin_form(D, ac, b):
    """Bilinear kernel of (1/4) D^{uavb} F*(k)_{uv} F(k+q)_{ab}
    in the (A*_rho(k), A_sigma(k+q)) basis. ac = conj(a(k)), b = a(k+q).
    D may carry a leading stack axis r (recipes)."""
    if D.ndim == 4:
        D = D[None]
    T1 = np.einsum("ruavb,pu,pa->rpvb", D, ac, b)
    T2 = np.einsum("ruavb,pu,pb->rpva", D, ac, b)
    T3 = np.einsum("ruavb,pv,pa->rpub", D, ac, b)
    T4 = np.einsum("ruavb,pv,pb->rpua", D, ac, b)
    out = 0.25 * (T1 - T2 - T3 + T4)
    return out[0] if out.shape[0] == 1 else out


def vertexV(kk, q, D2, Dm, m):
    """Reflection-symmetrized one-graviton vertex (npts,4,4) for the
    structure tensors D2 (kinetic) and Dm (mass)."""
    a1 = avec(kk)
    b2 = avec([kk[mu] + q[mu] for mu in range(4)])
    U = 2.0 * kin_form(D2, np.conj(a1), b2)      # Hessian normalization
    return U + m**2 * Dm[None, :, :]


def G_flat(kk, m):
    """Sherman-Morrison Proca propagator (npts,4,4)."""
    a = avec(kk)
    s2 = np.sum(np.abs(a) ** 2, axis=1)
    c = s2 + m**2
    G = np.eye(4)[None, :, :] / c[:, None, None]
    G = G + np.einsum("pu,pv->puv", a, np.conj(a)) / (c * m**2)[:, None, None]
    return G


def M_full(kk, h, m):
    """Exact kernel at constant h (for validation)."""
    J2, J = geomV(h)
    a = avec(kk)
    M = 2.0 * kin_form(J2, np.conj(a), a)
    return M + m**2 * J[None, :, :]


def g2_axis_proca(q0, n, m, dJ2, dJ):
    k1 = 2.0 * np.pi * np.arange(n) / n - np.pi
    K1, K2, K3 = np.meshgrid(k1, k1, k1, indexing="ij")
    K1, K2, K3 = K1.ravel(), K2.ravel(), K3.ravel()
    q = (q0, 0.0, 0.0, 0.0)
    mq = (-q0, 0.0, 0.0, 0.0)
    # stacked recipe structure tensors
    R2 = np.stack([sum(c * dJ2[p] for p, c in r) for r in TT_RECIPES])
    Rm = np.stack([sum(c * dJ[p] for p, c in r) for r in TT_RECIPES])
    total = 0.0
    for k0 in k1:
        kk = [np.full_like(K1, k0), K1, K2, K3]
        kkq = [kk[0] + q0, K1, K2, K3]
        G1 = G_flat(kk, m)
        G2g = G_flat(kkq, m)
        a1, b1 = avec(kk), avec(kkq)
        U1 = 2.0 * kin_form(R2, np.conj(a1), b1)             + m**2 * Rm[:, None, :, :]
        a2, b2 = avec(kkq), avec(kk)
        U2 = 2.0 * kin_form(R2, np.conj(a2), b2)             + m**2 * Rm[:, None, :, :]
        X = np.einsum("pij,rpjk->rpik", G1, U1)
        Y = np.einsum("pij,rpjk->rpik", G2g, U2)
        total += (-0.5) * np.einsum("rpij,rpji->", X, Y).real
    return total / (n ** 4) / 5.0


def const_h_check(n, m, dJ2, dJ, d2J2, d2J):
    k1 = 2.0 * np.pi * np.arange(n) / n - np.pi
    K = np.meshgrid(k1, k1, k1, k1, indexing="ij")
    kk = [g.ravel() for g in K]

    def gam(h):
        M = M_full(kk, h, m)
        sign, ld = np.linalg.slogdet(M)
        assert np.all(sign.real > 0)
        return +0.5 * ld.mean().real

    g0 = gam(np.zeros((4, 4)))
    # perturbative second derivative at q -> 0: bubble + seagull
    G1 = G_flat(kk, m)
    print("  constant-h validation (Proca):")
    for p1, p2 in [((0, 0), (0, 0)), ((0, 1), (0, 1)), ((0, 0), (1, 1))]:
        U1 = vertexV(kk, (0, 0, 0, 0), dJ2[p1], dJ[p1], m)
        U2 = vertexV(kk, (0, 0, 0, 0), dJ2[p2], dJ[p2], m)
        X = np.einsum("pij,pjk->pik", G1, U1)
        Y = np.einsum("pij,pjk->pik", G1, U2)
        bub = (-0.5) * np.einsum("pij,pji->p", X, Y).mean().real
        V2 = 2.0 * kin_form(d2J2[p1][p2], np.conj(avec(kk)), avec(kk))
        V2 = V2 + m**2 * d2J[p1][p2][None, :, :]
        sg = (+0.5) * np.einsum("pij,pji->p",
                                G1, V2).mean().real
        pert = bub + sg
        if p1 == p2:
            gp = gam(hmat([(p1, +EPSF)]))
            gm = gam(hmat([(p1, -EPSF)]))
            ex = (gp - 2 * g0 + gm) / EPSF**2
        else:
            vv = [gam(hmat([(p1, sa * EPSF), (p2, sb * EPSF)]))
                  for sa, sb in [(1, 1), (1, -1), (-1, 1), (-1, -1)]]
            ex = (vv[0] - vv[1] - vv[2] + vv[3]) / (4 * EPSF**2)
        print(f"    {p1}{p2}: exact={ex:+.6e}  pert={pert:+.6e}"
              f"  diff={abs(ex - pert):.1e}")


def slope(n, m, dJ2, dJ, eps=np.array([0.10, 0.16, 0.22, 0.28])):
    vals = np.array([g2_axis_proca(e, n, m, dJ2, dJ) for e in eps])
    return fit_even(eps, vals, order=2)[1]
