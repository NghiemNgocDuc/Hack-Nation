import webrtcvad
class Vad20ms:
    def __init__(self, mode: int = 2, sr: int = 16000):
        self.v = webrtcvad.Vad(mode); self.sr = sr; self.frame_ms = 20
        self.samples = sr * self.frame_ms // 1000
    def is_speech(self, frame_bytes: bytes) -> bool:
        return self.v.is_speech(frame_bytes, self.sr)
