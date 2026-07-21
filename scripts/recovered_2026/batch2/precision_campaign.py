"""
PRECISION CAMPAIGN RUNNER -- for Zeta to execute locally (no timeout).
Targets:  beta_gfvec/beta_B = -2.000 ;  beta_V/beta_B = -3.000.
Strategy: light masses (m a = 0.04..0.12) on n = 48 lattices, where
the m^2 ln m^2 term dominates the analytic background.
Estimated runtime: several hours on a modern CPU. Run:
    python3 precision_campaign.py
Outputs: precision_results.json + printed fits.
All modules (seagull_check, boson_loop, mlog_coeff, proca_loop,
gfvec_loop) must be in the same directory.
"""
import numpy as np, json, time
from gfvec_loop import derivsGF, slope_gf
from proca_loop import derivsV, slope as slope_proca
from mlog_coeff import g2_axis_boson, fit_mlog
from boson_loop import derivsB
from seagull_check import fit_even

N = 48
MASSES = [0.05, 0.065, 0.08, 0.10, 0.12]
EPS = np.array([0.08, 0.13, 0.18, 0.23])

res = {'gfvec': {}, 'proca': {}, 'boson': {}}
dJ2g, dJg, dEg = derivsGF()
dJ2p, dJp, _, _ = derivsV()
dJb, dEb, _, _ = derivsB()
t0 = time.time()
for m in MASSES:
    res['gfvec'][m] = slope_gf(N, m, dJ2g, dJg, dEg, eps=EPS)
    res['proca'][m] = slope_proca(N, m, dJ2p, dJp, eps=EPS)
    vb = np.array([g2_axis_boson(e, N, m, dJb, dEb) for e in EPS])
    res['boson'][m] = fit_even(EPS, vb, order=2)[1]
    json.dump(res, open('precision_results.json', 'w'))
    print(f"m={m}: gfvec={res['gfvec'][m]:+.6e} proca={res['proca'][m]:+.6e}"
          f" boson={res['boson'][m]:+.6e}  [{(time.time()-t0)/60:.0f} min]")

ms = np.array(MASSES); m2 = ms**2
for sp in ('gfvec', 'proca', 'boson'):
    Z = np.array([res[sp][m] for m in ms])
    c, r = fit_mlog(m2, Z, with_m4=True)
    res[sp+'_beta'] = c[2]
    print(f'{sp}: beta = {c[2]:+.4e} (maxres {r:.0e})')
bB = res['boson_beta']
print(f"RATIOS: gfvec/B = {res['gfvec_beta']/bB:+.3f} (target -2.000)")
print(f"        proca/B = {res['proca_beta']/bB:+.3f} (target -3.000)")
print(f"CONSISTENCY: proca - (gfvec - boson) = "
      f"{res['proca_beta'] - res['gfvec_beta'] + bB:+.2e} (target 0)")
json.dump(res, open('precision_results.json', 'w'))
