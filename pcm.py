import base64, numpy as np
def int16_to_float32(x: bytes):
    a = np.frombuffer(x, dtype=np.int16).astype(np.float32) / 32768.0
    return a, a.shape[0]
def float32_to_b64(x: np.ndarray) -> str:
    b = (x.clip(-1,1) * 32767.0).astype('<i2').tobytes()
    return base64.b64encode(b).decode()
def b64_to_int16(b64: str) -> bytes:
    return base64.b64decode(b64)
