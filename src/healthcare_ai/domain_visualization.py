def plot_recording(frame):
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(figsize=(10,3));ax.plot(frame.seconds,frame.amplitude,lw=.7)
    ax.fill_between(frame.seconds,0,1,where=frame.irregular_marker.astype(bool),transform=ax.get_xaxis_transform(),alpha=.15,color='red')
    ax.set(xlabel='Time (seconds)',ylabel='Arbitrary amplitude',title='Synthetic ECG-like recording; shaded simulated irregular intervals')
    fig.tight_layout();return fig
