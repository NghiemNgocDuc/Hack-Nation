from .rules import en, es, fr
from .detectors import advance_fee, otp_harvest, bank_cred, voice_spoof
LANGS = {"en": en, "es": es, "fr": fr}
DETECTORS = [advance_fee, otp_harvest, bank_cred, voice_spoof]

def score(text: str, lang: str) -> tuple[int, str, list]:
    t = text.lower(); L = LANGS.get(lang, en)
    s = 0; reasons = []
    for term in L.HIGH:
        if term in t: s += 40; reasons.append({"term":term,"w":40})
    for term in L.MED:
        if term in t: s += 15; reasons.append({"term":term,"w":15})
    for term in L.NEG:
        if term in t: s -= 20; reasons.append({"term":term,"w":-20})
    for det in DETECTORS:
        for term in det.TERMS:
            if term in t: s += det.WEIGHT; reasons.append({"term":term,"w":det.WEIGHT})
    s = max(0, min(100, s))
    label = "SAFE" if s < 30 else ("CAUTION" if s < 60 else "SCAM")
    return s, label, reasons[:3]
