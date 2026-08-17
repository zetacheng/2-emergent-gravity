"""Clean-room metric-coupled Proca operators on a finite hypercubic lattice.

Builds two operators on a periodic L^4 Euclidean lattice with spacing a = 1:

    D1[g,h]   the metric-coupled 1-form (Proca) operator
    D0[g,h]   the metric-coupled compensating scalar operator

Both are built from covariant actions discretised with forward differences and
site-centred geometric factors.  Nothing is imported from, copied from, or
structurally modelled on any script under ``scripts/recovered_2026/``.

Conventions taken from ``CONVENTIONS.md``
----------------------------------------
:12  Euclidean signature, d = 4.
:24  Hypercubic lattice, spacing ``a == 1``, Brillouin zone ``p_mu in (-pi, pi]``,
     and the naive/scalar free-field momentum ``phat2 = sum_mu 4 sin^2(p_mu/2)``.

Conventions fixed HERE, which ``CONVENTIONS.md`` does not fix
------------------------------------------------------------
C1  Forward differences for every lattice derivative:
    ``(d_mu f)(x) = f(x + mu) - f(x)``.  This is what makes the free scalar
    kernel equal ``phat2`` of :24 and makes the flat 1-form kernel's
    longitudinal band exactly momentum-independent.
C2  Site-centred geometric factors: ``sqrt(g) g^{mu nu}`` and
    ``sqrt(g) g^{mu al} g^{nu be}`` are evaluated at the site ``x`` at which the
    difference is anchored, not at a link or plaquette midpoint.
C3  Periodic boundary conditions in all four directions.
C4  ``g^{mu nu}`` is the exact matrix inverse of ``g_{mu nu}``, not a truncated
    weak-field expansion, and ``sqrt(g) = sqrt(det g)``.
C5  The operators are defined by dividing the action's Hessian by the mass
    metric, so that the mass term is exactly ``m^2`` times the identity:
        D1 + m^2 = G1^{-1} (K1 + m^2 G1) = G1^{-1} K1 + m^2 * 1
    with ``G1`` the mass metric ``sqrt(g) g^{mu nu}`` and ``K1`` the Hessian of
    the field-strength action.  Same construction for the scalar with ``G0``,
    ``K0``.  This is a choice of what "the operator" means; a different split
    would move factors of ``G`` between the operator and the measure.
C6  The weak-field background is a single-cosine profile,
    ``h_{mu nu}(x) = amp * c_{mu nu} * cos(2 pi (q . x) / L)``, with ``c``
    symmetric and ``q`` an integer wavevector.  Nothing in the repository fixes
    a background profile.

Only ``numpy`` is used.  ``scipy`` is not a declared package of this
environment and is not installed.
"""

from __future__ import annotations

import itertools

import numpy as np

DIM = 4

__all__ = [
    "DIM",
    "LatticeGeometry",
    "flat_metric",
    "cosine_weak_field",
    "scalar_operator",
    "vector_operator",
    "flat_scalar_eigenvalues",
    "flat_vector_block",
    "phat2",
    "logdet_operator",
    "longitudinal_projector_flat",
]


# ----------------------------------------------------------------------------
# lattice bookkeeping
# ----------------------------------------------------------------------------


class LatticeGeometry:
    """Site indexing and forward-shift tables for a periodic ``L**DIM`` lattice.

    Sites are indexed in row-major order over ``(x_0, ..., x_3)``.  ``shift[mu]``
    maps a site index to the index of ``x + mu`` with periodic wrap (C3).
    """

    def __init__(self, extent: int) -> None:
        if extent < 2:
            raise ValueError("extent must be at least 2")
        self.extent = int(extent)
        self.nsite = self.extent**DIM
        coords = np.array(
            list(itertools.product(range(self.extent), repeat=DIM)), dtype=np.int64
        )
        self.coords = coords
        strides = np.array(
            [self.extent ** (DIM - 1 - d) for d in range(DIM)], dtype=np.int64
        )
        self._strides = strides
        shift = np.empty((DIM, self.nsite), dtype=np.int64)
        for mu in range(DIM):
            moved = coords.copy()
            moved[:, mu] = (moved[:, mu] + 1) % self.extent
            shift[mu] = moved @ strides
        self.shift = shift

    def site_index(self, coord) -> int:
        c = np.asarray(coord, dtype=np.int64) % self.extent
        return int(c @ self._strides)

    def __repr__(self) -> str:  # pragma: no cover - convenience only
        return f"LatticeGeometry(extent={self.extent}, nsite={self.nsite})"


def phat2(momentum) -> float:
    """``sum_mu 4 sin^2(p_mu / 2)`` -- CONVENTIONS.md:24's naive/scalar momentum."""
    p = np.asarray(momentum, dtype=float)
    return float(np.sum(4.0 * np.sin(p / 2.0) ** 2))


# ----------------------------------------------------------------------------
# metric fields
# ----------------------------------------------------------------------------


def _metric_fields(h):
    """Return ``(g_inv, root_g)`` from a site-wise metric perturbation ``h``.

    ``h`` has shape ``(nsite, DIM, DIM)`` and is symmetrised on entry.  The
    metric is ``g = 1 + h``; ``g_inv`` is the exact inverse and ``root_g`` is
    ``sqrt(det g)`` (C4).
    """
    h = np.asarray(h, dtype=float)
    if h.ndim != 3 or h.shape[1:] != (DIM, DIM):
        raise ValueError("h must have shape (nsite, DIM, DIM)")
    h = 0.5 * (h + np.transpose(h, (0, 2, 1)))
    g = np.eye(DIM)[None, :, :] + h
    det = np.linalg.det(g)
    if np.any(det <= 0.0):
        raise ValueError("metric determinant is non-positive; amplitude too large")
    return np.linalg.inv(g), np.sqrt(det)


def flat_metric(geom: LatticeGeometry):
    """``h = 0``: the flat background."""
    return np.zeros((geom.nsite, DIM, DIM), dtype=float)


def cosine_weak_field(geom: LatticeGeometry, amplitude, direction, wavevector):
    """A single-cosine symmetric perturbation (C6).

    ``direction`` is a ``(DIM, DIM)`` symmetric pattern ``c_{mu nu}``;
    ``wavevector`` is an integer 4-tuple ``q``.  The profile is
    ``amplitude * c_{mu nu} * cos(2 pi (q . x) / L)``.
    """
    c = np.asarray(direction, dtype=float)
    if c.shape != (DIM, DIM):
        raise ValueError("direction must be (DIM, DIM)")
    c = 0.5 * (c + c.T)
    q = np.asarray(wavevector, dtype=float)
    if q.shape != (DIM,):
        raise ValueError("wavevector must have DIM entries")
    phase = 2.0 * np.pi * (geom.coords @ q) / geom.extent
    return float(amplitude) * np.cos(phase)[:, None, None] * c[None, :, :]


# ----------------------------------------------------------------------------
# scalar sector
# ----------------------------------------------------------------------------


def _scalar_difference_rows(geom: LatticeGeometry):
    """Support of the forward difference ``(d_mu phi)(x)`` (C1).

    Returns ``(index, coeff)`` with ``index[mu]`` of shape ``(nsite, 2)`` and
    ``coeff`` of shape ``(2,)``: ``phi(x + mu) - phi(x)``.
    """
    idx = np.empty((DIM, geom.nsite, 2), dtype=np.int64)
    base = np.arange(geom.nsite, dtype=np.int64)
    for mu in range(DIM):
        idx[mu, :, 0] = geom.shift[mu]
        idx[mu, :, 1] = base
    return idx, np.array([1.0, -1.0], dtype=float)


def _scalar_hessian(geom: LatticeGeometry, g_inv, root_g):
    """Hessian ``K0`` of ``S0 = 1/2 sum_x sqrt(g) g^{mu nu} (d_mu phi)(d_nu phi)``."""
    idx, coeff = _scalar_difference_rows(geom)
    n = geom.nsite
    k0 = np.zeros((n, n), dtype=float)
    outer = np.outer(coeff, coeff)
    for mu in range(DIM):
        for nu in range(DIM):
            weight = root_g * g_inv[:, mu, nu]
            rows = np.broadcast_to(idx[mu][:, :, None], (n, 2, 2))
            cols = np.broadcast_to(idx[nu][:, None, :], (n, 2, 2))
            vals = weight[:, None, None] * outer[None, :, :]
            np.add.at(k0, (rows.ravel(), cols.ravel()), vals.ravel())
    return 0.5 * (k0 + k0.T)


def scalar_operator(geom: LatticeGeometry, h, mass_squared):
    """``D0[g,h] + m^2`` as a dense ``(nsite, nsite)`` matrix.

    Built as ``G0^{-1} K0 + m^2 * 1`` per C5, with ``G0 = diag(sqrt(g))``.  At
    ``h = 0`` the spectrum is ``phat2 + m^2`` over the Brillouin zone, i.e. the
    scalar is PROPAGATING, not ultralocal.
    """
    g_inv, root_g = _metric_fields(h)
    k0 = _scalar_hessian(geom, g_inv, root_g)
    return (k0 / root_g[:, None]) + float(mass_squared) * np.eye(geom.nsite)


def flat_scalar_eigenvalues(geom: LatticeGeometry, mass_squared):
    """Analytic flat spectrum of ``D0 + m^2``: ``phat2(p) + m^2`` per mode."""
    two_pi_over_l = 2.0 * np.pi / geom.extent
    out = np.empty(geom.nsite, dtype=float)
    for i, c in enumerate(geom.coords):
        out[i] = phat2(two_pi_over_l * c) + float(mass_squared)
    return np.sort(out)


# ----------------------------------------------------------------------------
# 1-form sector
# ----------------------------------------------------------------------------


def _field_strength_rows(geom: LatticeGeometry):
    """Support of ``F_{mu nu}(x) = (d_mu A_nu)(x) - (d_nu A_mu)(x)`` (C1).

    Component ``(x, mu)`` of the 1-form is stored at flat offset
    ``x * DIM + mu``.  Returns ``index`` of shape ``(DIM, DIM, nsite, 4)`` and
    ``coeff`` of shape ``(4,)`` for the ordered support
    ``[(x+mu, nu), (x, nu), (x+nu, mu), (x, mu)]``.
    """
    n = geom.nsite
    base = np.arange(n, dtype=np.int64)
    idx = np.empty((DIM, DIM, n, 4), dtype=np.int64)
    for mu in range(DIM):
        for nu in range(DIM):
            idx[mu, nu, :, 0] = geom.shift[mu] * DIM + nu
            idx[mu, nu, :, 1] = base * DIM + nu
            idx[mu, nu, :, 2] = geom.shift[nu] * DIM + mu
            idx[mu, nu, :, 3] = base * DIM + mu
    return idx, np.array([1.0, -1.0, -1.0, 1.0], dtype=float)


def _vector_hessian(geom: LatticeGeometry, g_inv, root_g):
    """Hessian ``K1`` of the field-strength action.

        S1 = 1/4 sum_x sqrt(g) g^{mu al} g^{nu be} F_{mu nu} F_{al be}

    The unrestricted sum over all four indices is taken, with the ``1/4``
    normalisation, so that at ``h = 0`` the momentum-space kernel is
    ``phat2 delta_{mu nu} - conj(s_mu) s_nu``.
    """
    idx, coeff = _field_strength_rows(geom)
    n = geom.nsite
    dof = n * DIM
    k1 = np.zeros((dof, dof), dtype=float)
    outer = np.outer(coeff, coeff)
    for mu in range(DIM):
        for nu in range(DIM):
            if mu == nu:
                continue  # F_{mu mu} == 0 identically
            for al in range(DIM):
                for be in range(DIM):
                    if al == be:
                        continue
                    weight = root_g * g_inv[:, mu, al] * g_inv[:, nu, be]
                    if not np.any(weight):
                        continue
                    rows = np.broadcast_to(idx[mu, nu][:, :, None], (n, 4, 4))
                    cols = np.broadcast_to(idx[al, be][:, None, :], (n, 4, 4))
                    vals = 0.5 * weight[:, None, None] * outer[None, :, :]
                    np.add.at(k1, (rows.ravel(), cols.ravel()), vals.ravel())
    return 0.5 * (k1 + k1.T)


def _vector_mass_metric(geom: LatticeGeometry, g_inv, root_g):
    """Block-diagonal mass metric ``G1[(x,mu),(x,nu)] = sqrt(g) g^{mu nu}``."""
    dof = geom.nsite * DIM
    g1 = np.zeros((dof, dof), dtype=float)
    blocks = root_g[:, None, None] * g_inv
    for mu in range(DIM):
        for nu in range(DIM):
            rows = np.arange(geom.nsite) * DIM + mu
            cols = np.arange(geom.nsite) * DIM + nu
            g1[rows, cols] = blocks[:, mu, nu]
    return g1


def vector_operator(geom: LatticeGeometry, h, mass_squared, return_parts=False):
    """``D1[g,h] + m^2`` as a dense ``(nsite*DIM, nsite*DIM)`` matrix.

    Built as ``G1^{-1} K1 + m^2 * 1`` per C5.  At ``h = 0`` the spectrum is
    ``{phat2 + m^2 (x3 transverse), m^2 (x1 longitudinal)}`` per momentum mode:
    the longitudinal band is exactly momentum-independent.

    With ``return_parts`` the raw ``(K1, G1)`` are returned alongside, which the
    determinant helper uses to avoid inverting ``G1`` twice.
    """
    g_inv, root_g = _metric_fields(h)
    k1 = _vector_hessian(geom, g_inv, root_g)
    g1 = _vector_mass_metric(geom, g_inv, root_g)
    dof = geom.nsite * DIM
    op = np.linalg.solve(g1, k1) + float(mass_squared) * np.eye(dof)
    if return_parts:
        return op, k1, g1
    return op


def flat_vector_block(momentum, mass_squared):
    """The exact flat ``DIM x DIM`` kernel of ``D1 + m^2`` at one momentum.

    With ``s_mu = exp(i p_mu) - 1`` the forward-difference symbol (C1), the
    field strength is ``Ftilde_{mu nu} = s_mu Atilde_nu - s_nu Atilde_mu`` and
    the quadratic form reduces to

        phat2 * delta_{mu nu} - s_mu conj(s_nu),

    because ``sum_{mu<nu} |Ftilde_{mu nu}|^2 = phat2 |Atilde|^2 - |s^dag
    Atilde|^2``.  The mass adds ``m^2 delta_{mu nu}``.

    The ORDER of the conjugation is load-bearing and is not visible in the
    spectrum: this kernel and its complex conjugate are both Hermitian with
    identical eigenvalues, but they have DIFFERENT null directions.  Getting it
    backwards leaves every eigenvalue check passing while the transverse and
    longitudinal subspaces are swapped.
    """
    p = np.asarray(momentum, dtype=float)
    s = np.exp(1j * p) - 1.0
    block = (phat2(p) + float(mass_squared)) * np.eye(DIM, dtype=complex)
    block -= np.outer(s, np.conjugate(s))
    return block


def longitudinal_projector_flat(momentum):
    """Rank-1 projector onto the flat longitudinal direction at ``momentum``.

    The flat kernel of :func:`flat_vector_block` annihilates ``s_mu``:
    ``(phat2 delta - s conj(s)) s = phat2 s - s |s|^2 = 0`` since
    ``|s|^2 == phat2``.  So ``s`` spans the longitudinal band.

    At zero momentum ``s == 0`` and there is no distinguished direction; the
    zero matrix is returned and the caller must treat that mode separately --
    at ``p == 0`` all four bands sit at ``m^2`` anyway.
    """
    p = np.asarray(momentum, dtype=float)
    s = np.exp(1j * p) - 1.0
    norm = float(np.vdot(s, s).real)
    if norm <= 1e-30:
        return np.zeros((DIM, DIM), dtype=complex)
    return np.outer(s, np.conjugate(s)) / norm


# ----------------------------------------------------------------------------
# determinants
# ----------------------------------------------------------------------------


def logdet_operator(matrix) -> float:
    """``log det`` of a matrix with positive determinant, via LU.

    Raises if the sign is not ``+1``, so a sign flip cannot pass silently.
    """
    sign, value = np.linalg.slogdet(np.asarray(matrix, dtype=float))
    if sign <= 0.0:
        raise ValueError(f"non-positive determinant: sign={sign}")
    return float(value)
