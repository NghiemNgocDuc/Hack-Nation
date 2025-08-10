from time import monotonic
class Seq:
    def __init__(self): self.i=0
    def next(self): self.i+=1; return self.i
start = monotonic
