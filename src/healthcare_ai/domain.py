import numpy as np
def simulate_waveform(seconds=10,fs=100,irregular=False,seed=42):
    rng=np.random.default_rng(seed);t=np.arange(int(seconds*fs))/fs;x=.02*rng.normal(size=len(t));beat=.5
    while beat<seconds:
        x+=np.exp(-.5*((t-beat)/.025)**2)-.15*np.exp(-.5*((t-beat-.08)/.04)**2)
        beat+=float(rng.uniform(.45,1.15) if irregular else .8)
    return t,x
def extract_features(x,fs=100):
    from scipy.signal import find_peaks
    x=np.asarray(x);peaks,_=find_peaks(x,distance=int(.3*fs),prominence=.4);rr=np.diff(peaks)/fs
    spectrum=abs(np.fft.rfft(x))**2;weights=spectrum/max(spectrum.sum(),1e-12)
    return {'estimated_rate':float(60/rr.mean()) if len(rr) else None,'rr_std':float(rr.std()) if len(rr) else None,
      'spectral_entropy':float(-np.sum(weights*np.log(weights+1e-12))),'peak_count':len(peaks)}
