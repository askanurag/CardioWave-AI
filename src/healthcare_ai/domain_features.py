import numpy as np
from scipy.signal import find_peaks,peak_widths
from .settings import FEATURES
def segment_features(segment,fs):
    x=np.asarray(segment.amplitude,dtype=float);peaks,_=find_peaks(x,distance=max(1,round(.25*fs)),prominence=.35)
    rr=np.diff(peaks)/fs;spectrum=abs(np.fft.rfft(x-x.mean()))**2;w=spectrum/max(spectrum.sum(),1e-12)
    width=float(np.median(peak_widths(x,peaks,rel_height=.5)[0])/fs) if len(peaks) else 0.
    r={'heart_rate':float(60/rr.mean()) if len(rr) else 0.,'rr_variability':float(rr.std()) if len(rr) else 0.,'qrs_width':width,
       'signal_noise':float(np.median(abs(np.diff(x)))/.954),'spectral_entropy':float(-np.sum(w*np.log(w+1e-12))),
       'peak_amplitude':float(np.median(x[peaks])) if len(peaks) else 0.}
    return {f:r[f] for f in FEATURES}
