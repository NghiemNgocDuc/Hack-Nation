class Aggregator:
    def __init__(self): self._last = ""
    def update(self, s: str):
        if s != self._last:
            self._last = s; return s
        return None
