import numpy as np
from scipy.signal import butter,sosfiltfilt
def clean_signal(x,fs,cutoff=25):
    x=np.asarray(x,dtype=float)
    if len(x)<30 or not np.isfinite(x).all() or not 0<cutoff<fs/2:raise ValueError('Invalid offline filter input')
    return sosfiltfilt(butter(3,cutoff,fs=fs,output='sos'),x-x.mean())
