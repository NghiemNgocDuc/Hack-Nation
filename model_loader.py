from faster_whisper import WhisperModel
from .config import MODEL, COMPUTE
_model = None
def get_model():
    global _model
    if _model is None:
        _model = WhisperModel(MODEL, compute_type=COMPUTE)
    return _model
