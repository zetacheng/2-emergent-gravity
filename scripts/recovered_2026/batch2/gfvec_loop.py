"""
Gauge-fixed (minimal) lattice vector: precision route to beta_V.

Add to the Proca action the covariant gauge-fixing-like term
  S_gf = (1/2) sum_x E(x) B(x)^2,
  B(x) = sum_mu [ (J^{mu nu} A_nu)(x) - (J^{mu nu} A_nu)(x - mu) ],
  E = 1/sqrt(g),  J = sqrt(g) g^{-1},
whose continuum limit is (1/2) integral sqrt(g) (nabla.A)^2.
Then  -(1/4)FF - (1/2)(nabla.A)^2 = (1/2) A (-box delta + Ric) A,
so the operator becomes the MINIMAL vector Delta^(1) + m^2:
flat kernel (shat^2 + m^2) * Identity -- no longitudinal flat band,
diagonal propagator, no 1/m^2 enhancement.

Solodukhin identity:  Gamma_Proca = Gamma_minvec - Gamma_scalar(m),
hence  beta_V = beta_gfvec - beta_B  with the sharp targets
  beta_gfvec / beta_B = -2.00   and   beta_V / beta_B = -3.00 .

Flat gf structure (exact):  M_gf = E (a.J) (x) (abar.J),
a_mu = e^{ik_mu} - 1.  One-h vertex (h momentum -q, legs Abar(k),
A(k+q)):
  U_gf = dE a(k) (x) abar(k+q)
       + E0 a(k) (x) (abar(k).dJ)
       + E0 (a(k+q).dJ) (x) abar(k+q).
"""

import numpy as np
from seagull_check import PAIRS, hmat, fit_even, EPSF
from mlog_coeff import TT_RECIPES
from proca_loop import geomV, kin_form, avec


def geomE(h):
    g = np.eye(4) + h
    return 1.0 / np.sqrt(np.linalg.det(g))


def derivsGF():
    """First derivatives of J2 (kinetic), J (mass & gf), E (gf)."""
    dJ2, dJ, dE = {}, {}, {}
    for p in PAIRS:
        J2p, Jp = geomV(hmat([(p, +EPSF)]))
        J2m, Jm = geomV(hmat([(p, -EPSF)]))
        dJ2[p] = (J2p - J2m) / (2 * EPSF)
        dJ[p] = (Jp - Jm) / (2 * EPSF)
        dE[p] = (geomE(hmat([(p, +EPSF)]))
                 - geomE(hmat([(p, -EPSF)]))) / (2 * EPSF)
    return dJ2, dJ, dE


def Mgf_full(kk, h):
    """Exact gf kernel at constant h: E (a.J)(x)(abar.J)."""
    _, J = geomV(h)
    E = geomE(h)
    a = avec(kk)
    w = np.einsum("pm,mr->pr", a, J)          # (a.J)_rho
    v = np.einsum("pm,ms->ps", np.conj(a), J)  # (abar.J)_sigma
    return E * np.einsum("pr,ps->prs", w, v)


def M_minvec(kk, h, m):
    """Full minimal-vector kernel at constant h (validation)."""
    from proca_loop import M_full
    return M_full(kk, h, m) + Mgf_full(kk, h)


def vertexGF(kk, q, dJ2p, dJp, dEp, m):
    """One-graviton vertex of the gauge-fixed vector (npts,4,4)."""
    a1 = avec(kk)
    kkq = [kk[mu] + q[mu] for mu in range(4)]
    b2 = avec(kkq)
    # Proca part (kinetic Hessian x2 + mass)
    U = 2.0 * kin_form(dJ2p, np.conj(a1), b2) + m**2 * dJp[None, :, :]
    # gf part
    U = U + dEp * np.einsum("pr,ps->prs", a1, np.conj(b2))
    t2 = np.einsum("pm,ms->ps", np.conj(a1), dJp)
    U = U + np.einsum("pr,ps->prs", a1, t2)
    t3 = np.einsum("pm,mr->pr", b2, dJp)
    U = U + np.einsum("pr,ps->prs", t3, np.conj(b2))
    return U


def const_h_check_gf(n, m):
    dJ2, dJ, dE = derivsGF()
    k1 = 2.0 * np.pi * np.arange(n) / n - np.pi
    K = np.meshgrid(k1, k1, k1, k1, indexing="ij")
    kk = [g.ravel() for g in K]

    def gam(h):
        M = M_minvec(kk, h, m)
        sign, ld = np.linalg.slogdet(M)
        return +0.5 * ld.mean().real

    g0 = gam(np.zeros((4, 4)))
    a = avec(kk)
    s2 = np.sum(np.abs(a) ** 2, axis=1)
    G = np.eye(4)[None, :, :] / (s2 + m**2)[:, None, None]
    q0 = (0.0, 0.0, 0.0, 0.0)
    print("  constant-h validation (gauge-fixed vector):")
    for p1, p2 in [((0, 0), (0, 0)), ((0, 1), (0, 1)), ((0, 0), (1, 1))]:
        U1 = vertexGF(kk, q0, dJ2[p1], dJ[p1], dE[p1], m)
        U2 = vertexGF(kk, q0, dJ2[p2], dJ[p2], dE[p2], m)
        X = np.einsum("pij,pjk->pik", G, U1)
        Y = np.einsum("pij,pjk->pik", G, U2)
        bub = (-0.5) * np.einsum("pij,pji->p", X, Y).mean().real
        # seagull: numerical second derivative of the full kernel
        if p1 == p2:
            Mp = M_minvec(kk, hmat([(p1, +EPSF)]), m)
            Mm = M_minvec(kk, hmat([(p1, -EPSF)]), m)
            M0 = M_minvec(kk, np.zeros((4, 4)), m)
            d2M = (Mp - 2 * M0 + Mm) / EPSF**2
        else:
            acc = 0.0
            for sa, sb in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                Mx = M_minvec(kk, hmat([(p1, sa * EPSF),
                                        (p2, sb * EPSF)]), m)
                acc = acc + sa * sb * Mx
            d2M = acc / (4 * EPSF**2)
        sg = (+0.5) * np.einsum("pij,pji->p", G, d2M).mean().real
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


def g2_axis_gfvec(q0, n, m, dJ2, dJ, dE):
    k1 = 2.0 * np.pi * np.arange(n) / n - np.pi
    K1, K2, K3 = np.meshgrid(k1, k1, k1, indexing="ij")
    K1, K2, K3 = K1.ravel(), K2.ravel(), K3.ravel()
    q = (q0, 0.0, 0.0, 0.0)
    mq = (-q0, 0.0, 0.0, 0.0)
    rec = []
    for r in TT_RECIPES:
        rec.append((sum(c * dJ2[p] for p, c in r),
                    sum(c * dJ[p] for p, c in r),
                    sum(c * dE[p] for p, c in r)))
    total = 0.0
    for k0 in k1:
        kk = [np.full_like(K1, k0), K1, K2, K3]
        kkq = [kk[0] + q0, K1, K2, K3]
        a1, b1 = avec(kk), avec(kkq)
        s2a = np.sum(np.abs(a1) ** 2, axis=1)
        s2b = np.sum(np.abs(b1) ** 2, axis=1)
        g1 = 1.0 / (s2a + m**2)
        g2 = 1.0 / (s2b + m**2)
        for D2, Dm, De in rec:
            U1 = vertexGF(kk, q, D2, Dm, De, m)
            U2 = vertexGF(kkq, mq, D2, Dm, De, m)
            # diagonal propagators: trace = g1 g2 tr[U1 U2]
            tr = np.einsum("pij,pji->p", U1, U2)
            total += (-0.5) * (g1 * g2 * tr).sum().real
    return total / (n ** 4) / 5.0


def slope_gf(n, m, dJ2, dJ, dE,
             eps=np.array([0.10, 0.16, 0.22, 0.28])):
    vals = np.array([g2_axis_gfvec(e, n, m, dJ2, dJ, dE) for e in eps])
    return fit_even(eps, vals, order=2)[1]


def derivs2GF():
    """Second derivatives d2J (of sqrt(g) g^{-1}) and d2E (of 1/sqrt(g))."""
    from seagull_check import PAIRS, hmat, EPSF
    d2J, d2E = {}, {}
    _, J0 = geomV(np.zeros((4, 4)))
    E0 = geomE(np.zeros((4, 4)))
    for p1 in PAIRS:
        d2J[p1], d2E[p1] = {}, {}
        for p2 in PAIRS:
            if p1 == p2:
                _, Jp = geomV(hmat([(p1, +EPSF)]))
                _, Jm = geomV(hmat([(p1, -EPSF)]))
                d2J[p1][p2] = (Jp - 2*J0 + Jm) / EPSF**2
                d2E[p1][p2] = (geomE(hmat([(p1, +EPSF)]))
                               - 2*E0 + geomE(hmat([(p1, -EPSF)]))) / EPSF**2
            else:
                aJ, aE = 0.0, 0.0
                for sa, sb in [(1,1),(1,-1),(-1,1),(-1,-1)]:
                    h = hmat([(p1, sa*EPSF), (p2, sb*EPSF)])
                    _, Jx = geomV(h)
                    aJ = aJ + sa*sb*Jx
                    aE = aE + sa*sb*geomE(h)
                d2J[p1][p2] = aJ / (4*EPSF**2)
                d2E[p1][p2] = aE / (4*EPSF**2)
    return d2J, d2E


def gf_seagull(kk, q, dE1, dJ1, dE2, dJ2v, d2Ec, d2Jc):
    """q-dependent gf seagull vertex V[rho sigma](k; q).
    h(p1) carries -q, h(p2) carries +q (matching the bubble convention).
    dE1,dJ1 = first derivs for p1; dE2,dJ2v for p2;
    d2Ec,d2Jc = combined second derivatives d2[p1][p2]."""
    a0 = avec(kk)
    kp = [kk[mu] + q[mu] for mu in range(4)]
    km = [kk[mu] - q[mu] for mu in range(4)]
    ap, am = avec(kp), avec(km)
    ab0 = np.conj(a0)
    # V1: d2E with flat brackets
    V = d2Ec * np.einsum("pr,ps->prs", a0, ab0)
    # V2: E0 * d2J in bra or ket (E0 = 1)
    t = np.einsum("pm,mr->pr", a0, d2Jc)
    V = V + np.einsum("pr,ps->prs", t, ab0)
    t = np.einsum("pm,ms->ps", ab0, d2Jc)
    V = V + np.einsum("pr,ps->prs", a0, t)
    # V3: dE x dJ cross terms with phases
    tbra = np.einsum("pm,mr->pr", am, dJ2v)      # dJ(p2,+q) in bra: a(k-q)
    tket = np.einsum("pm,ms->ps", np.conj(ap), dJ2v)  # in ket: abar(k+q)
    V = V + dE1 * (np.einsum("pr,ps->prs", tbra, ab0)
                   + np.einsum("pr,ps->prs", a0, tket))
    tbra = np.einsum("pm,mr->pr", ap, dJ1)       # dJ(p1,-q) in bra: a(k+q)
    tket = np.einsum("pm,ms->ps", np.conj(am), dJ1)   # in ket: abar(k-q)
    V = V + dE2 * (np.einsum("pr,ps->prs", tbra, ab0)
                   + np.einsum("pr,ps->prs", a0, tket))
    # V4: dJ x dJ across brackets
    w = np.einsum("pm,mr->pr", ap, dJ1)          # p1 in bra (Q=-q)
    v = np.einsum("pm,ms->ps", np.conj(ap), dJ2v)  # p2 in ket (Q=+q)
    V = V + np.einsum("pr,ps->prs", w, v)
    w = np.einsum("pm,mr->pr", am, dJ2v)         # p2 in bra (Q=+q)
    v = np.einsum("pm,ms->ps", np.conj(am), dJ1)   # p1 in ket (Q=-q)
    V = V + np.einsum("pr,ps->prs", w, v)
    return V


def g2_axis_gfvec_v2(q0, n, m, dJ2, dJ, dE, d2J, d2E):
    """Slope kernel with the q-dependent gf seagull included."""
    k1 = 2.0 * np.pi * np.arange(n) / n - np.pi
    K1, K2, K3 = np.meshgrid(k1, k1, k1, indexing="ij")
    K1, K2, K3 = K1.ravel(), K2.ravel(), K3.ravel()
    q = (q0, 0.0, 0.0, 0.0)
    mq = (-q0, 0.0, 0.0, 0.0)
    rec = []
    for r in TT_RECIPES:
        D2 = sum(c * dJ2[p] for p, c in r)
        Dm = sum(c * dJ[p] for p, c in r)
        De = sum(c * dE[p] for p, c in r)
        DDm = sum(c1 * c2 * d2J[p1][p2]
                  for p1, c1 in r for p2, c2 in r)
        DDe = sum(c1 * c2 * d2E[p1][p2]
                  for p1, c1 in r for p2, c2 in r)
        rec.append((D2, Dm, De, DDm, DDe))
    total = 0.0
    qarr = np.array(q)
    for k0 in k1:
        kk = [np.full_like(K1, k0), K1, K2, K3]
        kkq = [kk[0] + q0, K1, K2, K3]
        a1, b1 = avec(kk), avec(kkq)
        g1 = 1.0 / (np.sum(np.abs(a1) ** 2, axis=1) + m**2)
        g2 = 1.0 / (np.sum(np.abs(b1) ** 2, axis=1) + m**2)
        for D2, Dm, De, DDm, DDe in rec:
            U1 = vertexGF(kk, q, D2, Dm, De, m)
            U2 = vertexGF(kkq, mq, D2, Dm, De, m)
            tr = np.einsum("pij,pji->p", U1, U2)
            total += (-0.5) * (g1 * g2 * tr).sum().real
            Vgf = gf_seagull(kk, qarr, De, Dm, De, Dm, DDe, DDm)
            total += (+0.5) * (g1 * np.einsum("pii->p", Vgf)).sum().real
    return total / (n ** 4) / 5.0


def slope_gf_v2(n, m, dJ2, dJ, dE, d2J, d2E,
                eps=np.array([0.10, 0.16, 0.22, 0.28])):
    vals = np.array([g2_axis_gfvec_v2(e, n, m, dJ2, dJ, dE, d2J, d2E)
                     for e in eps])
    return fit_even(eps, vals, order=2)[1]
