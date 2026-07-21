import numpy as np
r = 1.0
def bubbles_masked(m, E, n, central_only=False):
    p = 2*np.pi*np.arange(n)/n
    p1 = p.reshape(n,1,1); p2 = p.reshape(1,n,1); p3 = p.reshape(1,1,n)
    s2_spat = np.sin(p1)**2 + np.sin(p2)**2 + np.sin(p3)**2
    M_spat  = m + r*((1-np.cos(p1)) + (1-np.cos(p2)) + (1-np.cos(p3)))
    mask_spat = (np.cos(p1)>0)&(np.cos(p2)>0)&(np.cos(p3)>0) if central_only else True
    accS = 0.0; accV = 0.0
    for p0 in p:
        if central_only and np.cos(p0) <= 0: continue
        s0  = np.sin(p0);  M  = M_spat + (1-np.cos(p0))
        z   = p0 + 1j*E
        s0p = np.sin(z);   Mp = M_spat + (1-np.cos(z))
        D   = s0**2  + s2_spat + M**2
        Dp  = s0p**2 + s2_spat + Mp**2
        w   = 4.0/(D*Dp) * mask_spat
        ss  = s0*s0p + s2_spat; MM = M*Mp
        accS += np.sum(w*(MM - ss)).real
        accV += np.sum(w*(ss - (2/3)*s2_spat + MM)).real
    V = float(n)**4
    return accS/V, accV/V

for m,n in [(0.05,96),(0.2,64)]:
    for cen in [False, True]:
        S0,V0 = bubbles_masked(m,0.0,n,cen); S1,V1 = bubbles_masked(m,0.01,n,cen)
        print(f"m={m} n={n} central_only={cen}:  Z_S={(S1-S0)/1e-4:9.5f}   Z_Vs={(V1-V0)/1e-4:9.5f}")
