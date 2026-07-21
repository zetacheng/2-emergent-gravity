import numpy as np

# Wilson fermions, r=1, lattice n^4, antiperiodic? -> use periodic momenta first;
# (paper's convention unknown; try both if mismatch)
n = 32
r = 1.0

def momenta(n, antiperiodic_t=False):
    k = np.arange(n)
    p = 2*np.pi*k/n
    pt = p + (np.pi/n if antiperiodic_t else 0.0)
    return pt, p

def bubbles_q0(m, n=32, anti_t=False):
    pt, ps = momenta(n, anti_t)
    # build 4D grids via broadcasting
    p0 = pt.reshape(n,1,1,1); p1 = ps.reshape(1,n,1,1)
    p2 = ps.reshape(1,1,n,1); p3 = ps.reshape(1,1,1,n)
    s = [np.sin(p0), np.sin(p1)+0*p0, np.sin(p2)+0*p0, np.sin(p3)+0*p0]
    # broadcast fully
    s = [np.broadcast_to(x, (n,n,n,n)) for x in s]
    s2 = sum(x**2 for x in s)
    M = m + r*((1-np.cos(p0))+(1-np.cos(p1))+(1-np.cos(p2))+(1-np.cos(p3)))
    M = np.broadcast_to(M, (n,n,n,n))
    D = s2 + M**2
    V = n**4
    out = {}
    # raw traces T = (1/V) sum tr[Gamma S Gamma S], trace factor 4 included
    out['S']  = 4*np.sum((M**2 - s2)/D**2)/V
    out['P']  = 4*np.sum((M**2 + s2)/D**2)/V     # = 4 * sum 1/D
    # vector per component nu: numerator 4(s2 - 2 s_nu^2 + M^2)
    for i,lab in enumerate(['V0','V1','V2','V3']):
        out[lab] = 4*np.sum((s2 - 2*s[i]**2 + M**2)/D**2)/V
    out['Vavg'] = np.mean([out['V0'],out['V1'],out['V2'],out['V3']])
    # axial: M^2 -> -M^2
    for i,lab in enumerate(['A0','A1','A2','A3']):
        out[lab] = 4*np.sum((s2 - 2*s[i]**2 - M**2)/D**2)/V
    out['Aavg'] = np.mean([out['A0'],out['A1'],out['A2'],out['A3']])
    # tadpole (chiral condensate loop) and simple sums
    out['tad_M/D'] = np.sum(M/D)/V
    out['sum_1/D'] = np.sum(1/D)/V
    return out

anchors_V = {0.05:0.297, 0.2:0.264, 0.5:0.228}
print(f"{'m':>5} {'S':>9} {'P':>9} {'Vavg':>9} {'Aavg':>9} {'tadM/D':>9} {'1/D':>9}  anchorV")
res = {}
for m in [0.05,0.2,0.5]:
    o = bubbles_q0(m); res[m]=o
    print(f"{m:5.2f} {o['S']:9.4f} {o['P']:9.4f} {o['Vavg']:9.4f} {o['Aavg']:9.4f} {o['tad_M/D']:9.4f} {o['sum_1/D']:9.4f}  {anchors_V[m]:.3f}")

print()
print("ratio anchorV / Vavg per m:", [round(anchors_V[m]/res[m]['Vavg'],4) for m in [0.05,0.2,0.5]])
print("ratio anchorV / V0   per m:", [round(anchors_V[m]/res[m]['V0'],4) for m in [0.05,0.2,0.5]])
print("ratio anchorV / (Vavg/4) etc can be inferred from above")
print()
print("Axial check: c*Aavg with c from vector fit, m=0.05..0.5:")
for m in [0.05,0.2,0.5]:
    c = anchors_V[m]/res[m]['Vavg']
    print(f"  m={m}: c={c:.4f}, c*Aavg={c*res[m]['Aavg']:.4f}  (anchor ~ -0.19)")
print()
print("Scalar criticality candidates at small m (G_c published = 5.93):")
for m in [0.05,0.2,0.5]:
    o=res[m]
    print(f"  m={m}: 1/S={1/o['S'] if o['S']!=0 else float('inf'):9.3f}   1/(tadM/D)={1/o['tad_M/D']:7.3f}   1/(4 tadM/D)={1/(4*o['tad_M/D']):7.3f}   1/(P)={1/o['P']:7.3f}")
