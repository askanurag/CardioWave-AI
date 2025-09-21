import numpy as np
COLUMNS=['patient_id','seconds','amplitude','irregular_marker']
def validate_recording(frame):
    if not set(COLUMNS)<=set(frame):raise ValueError('Missing ECG columns')
    if frame.patient_id.isna().any() or frame.patient_id.nunique()!=1:raise ValueError('One patient per recording')
    t=frame.seconds.to_numpy(dtype=float);x=frame.amplitude.to_numpy(dtype=float)
    if len(t)<30 or not np.isfinite(t).all() or not np.isfinite(x).all() or not (np.diff(t)>0).all():raise ValueError('Finite regular timestamps and amplitudes required')
    dt=np.diff(t);fs=1/float(np.median(dt))
    if not np.allclose(dt,1/fs,rtol=.01,atol=1e-8):raise ValueError('Nonuniform sampling')
    if not set(frame.irregular_marker.unique())<={0,1}:raise ValueError('Binary simulator markers required')
    return fs
