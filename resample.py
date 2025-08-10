import numpy as np
def downsample(signal: np.ndarray, in_sr: int, out_sr: int) -> np.ndarray:
    if in_sr == out_sr: return signal
    ratio = in_sr / out_sr
    n = int(len(signal) / ratio)
    out = np.zeros(n, dtype=np.float32)
    for i in range(n):
        start, end = int(i*ratio), int((i+1)*ratio)
        if end <= start: end = start+1
        out[i] = signal[start:end].mean()
    return out
