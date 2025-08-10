import numpy as np, soundfile as sf, tempfile
from .model_loader import get_model
def decode_pcm16_to_text(pcm16: bytes, sr: int):
    x = np.frombuffer(pcm16, dtype=np.int16).astype('float32')/32768.0
    with tempfile.NamedTemporaryFile(suffix='.wav') as tmp:
        sf.write(tmp.name, x, sr)
        segs, info = get_model().transcribe(tmp.name, beam_size=1, vad_filter=False)
        text = ''.join(s.text for s in segs).strip()
        lang = getattr(info, 'language', 'en') or 'en'
    return text, lang
