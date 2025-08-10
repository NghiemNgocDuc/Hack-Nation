# API-compatible shim for A’s original RingBuffer
class RingBuffer:
    def __init__(self, capacity:int):
        self._cap = capacity; self._buf = []
    def push(self, x: bytes):
        self._buf.append(x)
        while sum(len(b) for b in self._buf) > self._cap:
            self._buf.pop(0)
    def clear(self): self._buf.clear()
    def concat(self): return b"".join(self._buf)
