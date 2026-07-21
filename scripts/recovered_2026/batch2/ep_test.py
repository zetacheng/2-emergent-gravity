import numpy as np
from scipy.optimize import brentq

r=1.0
# deformation: temporal kinetic and temporal Wilson term scaled by (1+eps)
def channel_Z(m, n, eps, direction, E=0.02):
    """Z = [Pi(k)-Pi(0)]/k^2 for external momentum k along 'direction':
       't' -> q0=iE continuation; 's' -> real spatial q=(k,0,0).
       Returns dict per channel: S,P,Vt2(transverse pol 2),At2."""
    xi = 1.0+eps
    p=2*np.pi*np.arange(n)/n
    p1=p.reshape(n,1,1); p2=p.reshape(1,n,1); p3=p.reshape(1,1,n)
    s1,s2_,s3 = np.sin(p1),np.sin(p2),np.sin(p3)
    w_spat = (1-np.cos(p1))+(1-np.cos(p2))+(1-np.cos(p3))
    out={}
    for shifted in [False,True]:
        acc={c:0.0 for c in ['S','P','V2','A2']}
        for p0 in p:
            s0=xi*np.sin(p0); M=m+r*(xi*(1-np.cos(p0))+w_spat)
            if not shifted:
                s0p,s1p,Mp = s0,s1,M
            elif direction=='t':
                z=p0+1j*E
                s0p=xi*np.sin(z); s1p=s1; Mp=m+r*(xi*(1-np.cos(z))+w_spat)
            else: # spatial shift along 1 by real k=E
                s0p=s0; s1p=np.sin(p1+E); Mp=m+r*(xi*(1-np.cos(p0))+(1-np.cos(p1+E))+(1-np.cos(p2))+(1-np.cos(p3)))
            D =(xi*np.sin(p0))**2*0 + s0**2+s1**2+s2_**2+s3**2+M**2
            Dp=s0p**2+s1p**2+s2_**2+s3**2+Mp**2
            wgt=4.0/(D*Dp)
            ss=s0*s0p+s1*s1p+s2_**2+s3**2
            MM=M*Mp
            acc['S'] +=np.sum(wgt*(MM-ss)).real
            acc['P'] +=np.sum(wgt*(MM+ss)).real
            acc['V2']+=np.sum(wgt*(ss-2*s2_**2+MM)).real   # transverse pol along 2
            acc['A2']+=np.sum(wgt*(ss-2*s2_**2-MM)).real
        V=float(n)**4
        out['shift' if shifted else 'zero']={c:acc[c]/V for c in acc}
    Z={c:(out['shift'][c]-out['zero'][c])/E**2 for c in ['S','P','V2','A2']}
    if direction=='s': Z={c:-Z[c] for c in Z}   # spatial: Pi(k)=Pi(0)-Z k^2 vs temporal +Z E^2
    return Z

def fermion_c2(m, eps):
    """free anisotropic Wilson fermion speed^2 at p->0 from pole dispersion."""
    xi=1.0+eps
    def Epole(ps):
        f=lambda E: -(xi*np.sinh(E))**2 + ps**2 + (m + r*(xi*(1-np.cosh(E)) + (1-np.cos(ps))))**2
        return brentq(f,1e-9,3.0)
    E0=Epole(0.0); dp=0.02
    return (Epole(dp)**2-E0**2)/dp**2

for m,n in [(0.2,48)]:
    print(f"===== m_f a = {m}, n = {n} =====")
    for eps in [0.0, 0.05, 0.10]:
        Zt=channel_Z(m,n,eps,'t'); Zs=channel_Z(m,n,eps,'s')
        c2={c: Zs[c]/Zt[c] for c in Zt}
        cf2=fermion_c2(m,eps)
        print(f"eps={eps:4.2f}  c^2: fermion={cf2:.5f}  " + "  ".join(f"{c}={c2[c]:.5f}" for c in ['P','S','V2','A2']))
