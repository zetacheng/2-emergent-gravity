"""Restricted frozen vocabulary validator."""
import re
ALLOWED={"Sum","bilinear","lam","gamma","gamma5","Id4","IdN","I","G","N","A","mu","nu"}
def canonical(text):
    unknown=set(re.findall(r"[A-Za-z_][A-Za-z_0-9]*",text))-ALLOWED
    if unknown: raise ValueError(f"outside frozen vocabulary: {sorted(unknown)}")
    return re.sub(r"\s+","",text)
