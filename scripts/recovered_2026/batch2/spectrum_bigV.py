import numpy as np, sys, json

r = 1.0
channels = ['S','P','Vs','As']

def bubbles_iE_sliced(m, E, n):
    p = 2*np.pi*np.arange(n)/n
    p1 = p.reshape(n,1,1); p2 = p.reshape(1,n,1); p3 = p.reshape(1,1,n)
    s2_spat = np.sin(p1)**2 + np.sin(p2)**2 + np.sin(p3)**2
    M_spat  = m + r*((1-np.cos(p1)) + (1-np.cos(p2)) + (1-np.cos(p3)))
    acc = {ch:0.0 for ch in channels}
    for p0 in p:
        s0  = np.sin(p0);        M  = M_spat + (1-np.cos(p0))
        z   = p0 + 1j*E
        s0p = np.sin(z);         Mp = M_spat + (1-np.cos(z))
        D   = s0**2  + s2_spat + M**2
        Dp  = s0p**2 + s2_spat + Mp**2
        w   = 4.0/(D*Dp)
        ss  = s0*s0p + s2_spat
        MM  = M*Mp
        acc['S']  += np.sum(w*(MM - ss)).real
        acc['P']  += np.sum(w*(MM + ss)).real
        acc['Vs'] += np.sum(w*(ss - (2.0/3.0)*s2_spat + MM)).real
        acc['As'] += np.sum(w*(ss - (2.0/3.0)*s2_spat - MM)).real
    V = float(n)**4
    return {ch: acc[ch]/V for ch in channels}

if __name__ == '__main__':
    m = float(sys.argv[1]); n = int(sys.argv[2])
    Es = [0.0, 0.01, 0.02]
    res = {}
    for E in Es:
        res[E] = bubbles_iE_sliced(m, E, n)
    print(f"m={m} n={n}")
    print(f"{'ch':>3} {'Pi(0)':>10} {'Z(E=0.01)':>11} {'Z(E=0.02)':>11}")
    out = {'m':m,'n':n,'Pi0':{},'Z':{}}
    for ch in channels:
        z1 = (res[0.01][ch]-res[0.0][ch])/0.01**2
        z2 = (res[0.02][ch]-res[0.0][ch])/0.02**2
        out['Pi0'][ch]=res[0.0][ch]; out['Z'][ch]=z1
        print(f"{ch:>3} {res[0.0][ch]:10.5f} {z1:11.5f} {z2:11.5f}")
    json.dump(out, open(f'/home/claude/spectral/res_m{m}_n{n}.json','w'))
