from libs.audio.vad import Vad20ms
from .config import SR, FRAME_MS, SILENCE_END_MS
class Segmenter:
    def __init__(self):
        self.vad = Vad20ms(2, SR)
        self.samples_per_frame = SR * FRAME_MS // 1000
        self.silence_frames = SILENCE_END_MS // FRAME_MS
        self.in_speech=False; self.silence=0
        self.buf = bytearray(); self.sample_pos=0
    def push(self, frame: bytes):
        is_speech = self.vad.is_speech(frame)
        if is_speech:
            self.in_speech=True; self.silence=0; self.buf.extend(frame)
        else:
            if self.in_speech:
                self.silence+=1; self.buf.extend(frame)
                if self.silence>=self.silence_frames:
                    seg = bytes(self.buf); self.buf.clear(); self.in_speech=False; self.silence=0
                    seg_len = len(seg)//2
                    t1 = (self.sample_pos + seg_len)/SR
                    t0 = t1 - seg_len/SR
                    self.sample_pos += self.samples_per_frame
                    return {"t0":round(t0,3),"t1":round(t1,3),"bytes":seg}
        self.sample_pos += self.samples_per_frame
        return None
