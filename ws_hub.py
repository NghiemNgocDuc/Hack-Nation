import json
from typing import Set
from fastapi import WebSocket
class WSHub:
    def __init__(self):
        self.clients: Set[WebSocket] = set()
    async def add(self, ws: WebSocket):
        await ws.accept(); self.clients.add(ws)
    def remove(self, ws: WebSocket):
        self.clients.discard(ws)
    async def send_json(self, obj: dict):
        txt = json.dumps(obj)
        for c in list(self.clients):
            try: await c.send_text(txt)
            except Exception: self.clients.discard(c)
