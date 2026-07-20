"""
General O(q^2) structure decomposition of the TT-projected kernel.

H(4)-invariant structures surviving the TT projection (q^2 factored,
written with the unit vector nh = q/|q|, N_{ab} = diag(nh_mu^2)):
  S0: covariant  sym(delta delta)            -> weight 1 (normalization)
  S1: delta4 (all four indices equal)
  S2: sym[N_{ar} delta_{bs}]
  S3: 4-pin  sum_l nh_l^2 (all indices = l)
  S4: N (x) N      (first pair) x (second pair)
  S5: sym[N_{ar} N_{bs}]
Least-squares over many momentum orientations; residual = consistency.
"""

import numpy as np
from seagull_check import projectors, fit_even

ORIENTS = [
    (1, 0, 0, 0), (1, 1, 0, 0), (1, 1, 1, 0), (1, 1, 1, 1),
    (2, 1, 0, 0), (2, 1, 1, 0), (2, 1, 1, 1), (3, 1, 1, 0),
]


def structures(nh):
    N = np.diag(np.array(nh) ** 2)
    d = np.eye(4)
    S = []
    S0 = 0.5 * (np.einsum("ar,bs->abrs", d, d)
                + np.einsum("as,br->abrs", d, d))
    S.append(S0)
    S1 = np.zeros((4, 4, 4, 4))
    for l in range(4):
        S1[l, l, l, l] = 1.0
    S.append(S1)
    S2 = 0.25 * (np.einsum("ar,bs->abrs", N, d)
                 + np.einsum("as,br->abrs", N, d)
                 + np.einsum("br,as->abrs", N, d)
                 + np.einsum("bs,ar->abrs", N, d))
    S.append(S2)
    S3 = np.zeros((4, 4, 4, 4))
    for l in range(4):
        S3[l, l, l, l] = nh[l] ** 2
    S.append(S3)
    S4 = np.einsum("ab,rs->abrs", N, N)
    S.append(S4)
    S5 = 0.5 * (np.einsum("ar,bs->abrs", N, N)
                + np.einsum("as,br->abrs", N, N))
    S.append(S5)
    return S


def weights_matrix():
    """W[orient, structure] = <P2(q), S_i(nh)> / 5."""
    W = []
    for o in ORIENTS:
        nh = np.array(o, float)
        nh /= np.linalg.norm(nh)
        P2 = projectors(nh)
        W.append([np.einsum("abrs,abrs->", P2, S) / 5.0
                  for S in structures(nh)])
    return np.array(W)


def decompose(slopes, names=None):
    """slopes: array over ORIENTS of measured TT q^2 slopes."""
    W = weights_matrix()
    coef, res, rank, sv = np.linalg.lstsq(W, slopes, rcond=None)
    fitted = W @ coef
    resid = np.abs(fitted - slopes).max() / np.abs(slopes).max()
    print(f"    structure basis rank = {rank} / {W.shape[1]}")
    labels = names or ["Z_cov", "c_d4", "c_Nd", "c_4pin", "c_NxN", "c_NN"]
    for lb, c in zip(labels, coef):
        print(f"    {lb:7s} = {c:+.6e}")
    print(f"    max relative residual over {len(ORIENTS)} orientations"
          f" = {resid:.2%}")
    return coef, resid


def measure_slopes(kernel_fn, eps=np.array([0.15, 0.25, 0.35, 0.45])):
    """kernel_fn(q) -> full (4,4,4,4) tensor; returns slope per orient."""
    out = []
    for o in ORIENTS:
        nh = np.array(o, float)
        nh /= np.linalg.norm(nh)
        vals = []
        for e in eps:
            q = tuple(e * nh)
            G = kernel_fn(q)
            P2 = projectors(q)
            vals.append(np.einsum("abrs,abrs->", P2, G) / 5.0)
        out.append(fit_even(eps, np.array(vals))[1])
    return np.array(out)
