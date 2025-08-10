from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .ws_hub import WSHub
router = APIRouter()
hub: WSHub | None = None  # set by main
@router.post("/ingest/segment")
async def ingest_segment(payload: dict):
    payload.setdefault("type", "segment")
    await hub.send_json(payload)
    return JSONResponse({"ok": True})
@router.post("/ingest/transcript")
async def ingest_transcript(payload: dict):
    payload.setdefault("type", "transcript")
    await hub.send_json(payload)
    return {"ok": True}
@router.post("/ingest/risk")
async def ingest_risk(payload: dict):
    payload.setdefault("type", "risk")
    await hub.send_json(payload)
    return {"ok": True}
