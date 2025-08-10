from pydantic import BaseModel
from typing import Literal

class AudioEvent(BaseModel):
    type: Literal["audio"] = "audio"
    seq: int
    sr: int = 16000
    session_id: str
    pcm16_b64: str

class SegmentEvent(BaseModel):
    type: Literal["segment"] = "segment"
    sr: int = 16000
    t0: float
    t1: float
    speaker: str = "caller"
    bytes_b64: str
    session_id: str

class TranscriptEvent(BaseModel):
    type: Literal["transcript"] = "transcript"
    text: str
    lang: str = "en"
    t0: float
    t1: float
    speaker: str = "caller"
    partial: bool = False
    session_id: str
    seq: int | None = None

class RiskEvent(BaseModel):
    type: Literal["risk"] = "risk"
    score: int
    label: str
    reasons: list[dict] = []
    spoof_prob: float | None = None
    lang: str = "en"
    t0: float
    t1: float
    session_id: str
    seq: int | None = None

class StatusEvent(BaseModel):
    type: Literal["status"] = "status"
    latency_ms: int | None = None
    message: str
    session_id: str
    ts: int
