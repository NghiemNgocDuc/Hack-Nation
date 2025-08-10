from collections import deque
class RingBuffer:
    def __init__(self, capacity:int):
        self.buf = deque(maxlen=capacity); self.size=0
    def push(self, b: bytes):
        if len(self.buf)==self.buf.maxlen: self.size -= len(self.buf[0])
        self.buf.append(b); self.size += len(b)
    def clear(self): self.buf.clear(); self.size=0
    def concat(self) -> bytes: return b"".join(self.buf)
