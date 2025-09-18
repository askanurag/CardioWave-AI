import numpy as np
import pandas as pd
def make_recording(seed=1):
    rng=np.random.default_rng(seed);fs=100;t=np.arange(3000)/fs;irregular=((t>=6)&(t<12))|((t>=20)&(t<26))
    x=.02*rng.normal(size=len(t))+.03*np.sin(2*np.pi*.2*t);beat=.4
    while beat<t[-1]:
        width=.018+rng.uniform(0,.005);amp=rng.uniform(.8,1.2)
        x+=amp*np.exp(-.5*((t-beat)/width)**2)+.2*np.exp(-.5*((t-beat-.22)/.06)**2)
        state=(6<=beat<12) or (20<=beat<26)
        beat+=float(rng.uniform(.38,1.1) if state else rng.normal(.8,.015))
    return pd.DataFrame({'patient_id':'ECG-SIM-%03d'%seed,'seconds':t,'amplitude':x,'irregular_marker':irregular.astype(int)})
