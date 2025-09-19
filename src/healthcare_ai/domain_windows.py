import numpy as np
from .domain_contract import validate_recording
def segments(frame,seconds=5,stride=5):
    fs=validate_recording(frame)
    if not np.isfinite([seconds,stride]).all() or min(seconds,stride)<=0:raise ValueError('Positive finite window settings')
    size,step=round(fs*seconds),round(fs*stride)
    if size<30 or step<1:raise ValueError('Window too short')
    return [frame.iloc[a:a+size].copy() for a in range(0,len(frame)-size+1,step)]
