from .schema import SegmentEvent, TranscriptEvent, RiskEvent
def ensure_segment(d: dict) -> SegmentEvent:
    return SegmentEvent(**d)
def ensure_transcript(d: dict) -> TranscriptEvent:
    return TranscriptEvent(**d)
def ensure_risk(d: dict) -> RiskEvent:
    return RiskEvent(**d)
