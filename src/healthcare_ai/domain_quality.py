import numpy as np
from .domain_contract import validate_recording
def recording_quality(frame):
    fs=validate_recording(frame);x=frame.amplitude.to_numpy()
    return {'samples':len(x),'sampling_hz':fs,'duration_seconds':len(x)/fs,'std_amplitude':float(x.std()),'flat':bool(x.std()<1e-8),'largest_step':float(abs(np.diff(x)).max())}
