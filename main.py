import asyncio, json, os, websockets
from libs.common import get_logger
from .engine import score
from .publisher import post_risk
WS = os.getenv("GATEWAY_WS", "ws://localhost:5050/ws")
log = get_logger("risk")
async def run():
    while True:
        try:
            async with websockets.connect(WS, ping_interval=None) as ws:
                log.info("connected %s", WS)
                async for raw in ws:
                    try: msg = json.loads(raw)
                    except: continue
                    if msg.get("type") != "transcript" or msg.get("partial"):
                        continue
                    s, label, reasons = score(msg.get("text",""), msg.get("lang","en"))
                    post_risk(os.getenv("POST_RISK","http://localhost:5050/ingest/risk"), {
                        "score": s, "label": label, "reasons": reasons,
                        "lang": msg.get("lang","en"), "t0": msg.get("t0"), "t1": msg.get("t1"),
                        "session_id": msg.get("session_id")
                    })
        except Exception as e:
            log.warning("reconnect: %s", e); await asyncio.sleep(1)
if __name__ == "__main__":
    asyncio.run(run())
