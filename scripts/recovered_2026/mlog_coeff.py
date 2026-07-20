"""
Universal m^2 log(m^2) coefficient of the induced graviton kinetic term.

Scheme-independent statement: counterterms are mass-independent, and the
IR (k ~ m) region of the loop is effectively continuum+covariant, so the
m^2 ln m^2 part of the axis-TT slope Z(m) is the universal covariant
induced contribution.  Continuum benchmark (heat kernel):
   beta_Dirac / beta_real-min-scalar = 2   (convention-free ratio test).

Method: bubble-only axis-TT slope (seagull and CC are q^0 / q-independent
and drop from the slope).  TT projector spectrally decomposed into 5
transverse-traceless basis tensors -> 5 effective vertices.
Streaming over k0 slices for memory control.
"""

import numpy as np
from seagull_check import (GAM, PAIRS, propagator, vertex_U, first_derivs,
                           fit_even)
from boson_loop import derivsB, vertexB, MB_flat

# 5 TT basis tensors for q || e0, expressed as pair-combination recipes:
#   each entry: list of (pair, coefficient) such that
#   U_eff = sum coeff * U^{pair}   corresponds to a unit-normalized tensor.
TT_RECIPES = [
    [((1, 1), 1 / np.sqrt(2)), ((2, 2), -1 / np.sqrt(2))],
    [((1, 1), 1 / np.sqrt(6)), ((2, 2), 1 / np.sqrt(6)),
     ((3, 3), -2 / np.sqrt(6))],
    [((1, 2), 1 / np.sqrt(2))],
    [((1, 3), 1 / np.sqrt(2))],
    [((2, 3), 1 / np.sqrt(2))],
]


def g2_axis_fermion(q0, n, m, r, dF, dE, dG):
    k1 = 2.0 * np.pi * np.arange(n) / n - np.pi
    K1, K2, K3 = np.meshgrid(k1, k1, k1, indexing="ij")
    K1, K2, K3 = K1.ravel(), K2.ravel(), K3.ravel()
    q = (q0, 0.0, 0.0, 0.0)
    mq = (-q0, 0.0, 0.0, 0.0)
    total = 0.0
    for k0 in k1:
        kk = [np.full_like(K1, k0), K1, K2, K3]
        kkq = [kk[0] + q0, K1, K2, K3]
        S1 = propagator(kk, m, r)
        S2 = propagator(kkq, m, r)
        for recipe in TT_RECIPES:
            U1 = sum(c * vertex_U(kk, q, p, dF, dE, dG, m, r)
                     for p, c in recipe)
            U2 = sum(c * vertex_U(kkq, mq, p, dF, dE, dG, m, r)
                     for p, c in recipe)
            X = np.einsum("pij,pjk->pik", S1, U1)
            Y = np.einsum("pij,pjk->pik", S2, U2)
            total += np.einsum("pij,pji->p", X, Y).sum().real
    return total / (n ** 4) / 5.0


def g2_axis_boson(q0, n, mB, dJ, dE):
    k1 = 2.0 * np.pi * np.arange(n) / n - np.pi
    K1, K2, K3 = np.meshgrid(k1, k1, k1, indexing="ij")
    K1, K2, K3 = K1.ravel(), K2.ravel(), K3.ravel()
    q = (q0, 0.0, 0.0, 0.0)
    mq = (-q0, 0.0, 0.0, 0.0)
    total = 0.0
    for k0 in k1:
        kk = [np.full_like(K1, k0), K1, K2, K3]
        kkq = [kk[0] + q0, K1, K2, K3]
        G1 = 1.0 / MB_flat(kk, mB)
        G2g = 1.0 / MB_flat(kkq, mB)
        for recipe in TT_RECIPES:
            U1 = sum(c * vertexB(kk, q, p, dJ, dE, mB) for p, c in recipe)
            U2 = sum(c * vertexB(kkq, mq, p, dJ, dE, mB) for p, c in recipe)
            total += (-0.5) * (G1 * U1 * G2g * U2).sum().real
    return total / (n ** 4) / 5.0


def slope(fn, eps=np.array([0.10, 0.16, 0.22, 0.28])):
    vals = np.array([fn(e) for e in eps])
    return fit_even(eps, vals, order=2)[1]


def fit_mlog(m2, Z, with_m4=True):
    """Z(m^2) = z0 + z1 m^2 + beta m^2 ln(m^2) (+ z2 m^4)."""
    cols = [np.ones_like(m2), m2, m2 * np.log(m2)]
    if with_m4:
        cols.append(m2 ** 2)
    A = np.stack(cols, axis=1)
    coef, *_ = np.linalg.lstsq(A, Z, rcond=None)
    resid = np.abs(A @ coef - Z).max()
    return coef, resid
