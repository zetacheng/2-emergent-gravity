import numpy as np

r=1.0
def Zs_multi(m, n, eps, Es=(0.01,0.02,0.03)):
    """Return E->0 extrapolated Z_t, Z_s for channels P, V2.
    Zero-shift pass computed once; quadratic extrapolation Z(E)=Z0+cE^2."""
    xi=1.0+eps
    p=2*np.pi*np.arange(n)/n
    p1=p.reshape(n,1,1); p2=p.reshape(1,n,1); p3=p.reshape(1,1,n)
    s1,s2_,s3=np.sin(p1),np.sin(p2),np.sin(p3)
    w_spat=(1-np.cos(p1))+(1-np.cos(p2))+(1-np.cos(p3))
    V=float(n)**4
    # zero-shift
    z0={'P':0.0,'V2':0.0}
    Dcache=[]
    for p0 in p:
        s0=xi*np.sin(p0); M=m+r*(xi*(1-np.cos(p0))+w_spat)
        D=s0**2+s1**2+s2_**2+s3**2+M**2
        w=4.0/(D*D); ss=s0**2+s1**2+s2_**2+s3**2; MM=M*M
        z0['P']+=np.sum(w*(MM+ss)); z0['V2']+=np.sum(w*(ss-2*s2_**2+MM))
    z0={c:z0[c]/V for c in z0}
    out={}
    for direction in ['t','s']:
        Zvals={'P':[], 'V2':[]}
        for E in Es:
            acc={'P':0.0,'V2':0.0}
            for p0 in p:
                s0=xi*np.sin(p0); M=m+r*(xi*(1-np.cos(p0))+w_spat)
                D=s0**2+s1**2+s2_**2+s3**2+M**2
                if direction=='t':
                    z=p0+1j*E
                    s0p=xi*np.sin(z); s1p=s1; Mp=m+r*(xi*(1-np.cos(z))+w_spat)
                else:
                    s0p=s0; s1p=np.sin(p1+E)
                    Mp=m+r*(xi*(1-np.cos(p0))+(1-np.cos(p1+E))+(1-np.cos(p2))+(1-np.cos(p3)))
                Dp=s0p**2+s1p**2+s2_**2+s3**2+Mp**2
                w=4.0/(D*Dp); ss=s0*s0p+s1*s1p+s2_**2+s3**2; MM=M*Mp
                acc['P']+=np.sum(w*(MM+ss)).real; acc['V2']+=np.sum(w*(ss-2*s2_**2+MM)).real
            for c in acc: Zvals[c].append((acc[c]/V - z0[c])/E**2)
        # quadratic extrapolation in E^2: Z(E)=Z0+c1*E^2 (fit 3 points, take intercept)
        E2=np.array(Es)**2
        Zext={}
        for c in Zvals:
            A=np.vstack([np.ones(3),E2]).T
            coef,_,_,_=np.linalg.lstsq(A,np.array(Zvals[c]),rcond=None)
            Zext[c]=coef[0]
        out[direction]=Zext
    c2={c: (-out['s'][c])/out['t'][c] for c in ['P','V2']}   # spatial sign convention
    return c2

def split_sigma(m,n,eps=0.05):
    c0=Zs_multi(m,n,0.0); c1=Zs_multi(m,n,eps)
    rP=c1['P']/c0['P']; rV=c1['V2']/c0['V2']
    sigma=(rP/rV-1)/eps
    return sigma, c0

print(f"{'m':>6} {'n':>4} {'sigma_PV':>10} {'baseP':>8} {'baseV':>8}")
data=[]
for m,n in [(0.2,48),(0.1,64),(0.05,96),(0.05,128)]:
    s,c0=split_sigma(m,n)
    print(f"{m:6.3f} {n:4d} {s:10.5f} {c0['P']:8.5f} {c0['V2']:8.5f}")
    data.append((m,n,s))

# law comparison using the two smaller-m converged points anchored at m=0.2
import math
m0,_,s0 = data[0]
L=lambda m: math.log(1.0/m)
print("\nlaw predictions anchored at m=0.2:")
for m in [0.1,0.05]:
    print(f"  m={m}: 1/L -> {s0*L(m0)/L(m):.5f}   1/L^2 -> {s0*(L(m0)/L(m))**2:.5f}   m^1 -> {s0*m/m0:.5f}   m^0.5 -> {s0*math.sqrt(m/m0):.5f}")
