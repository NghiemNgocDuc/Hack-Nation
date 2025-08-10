import requests
def post_risk(url: str, payload: dict):
    payload.setdefault("type", "risk"); requests.post(url, json=payload, timeout=5)
