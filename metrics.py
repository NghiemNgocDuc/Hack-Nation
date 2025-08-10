import time
class Timer:
    def __init__(self): self.t0=0; self.ms=0
    def __enter__(self): self.t0=time.perf_counter(); return self
    def __exit__(self, *exc): self.ms = (time.perf_counter()-self.t0)*1000
