import { useEffect, useRef, useState } from 'react'
export function useFeed(url: string) {
  const [events, setEvents] = useState<any[]>([])
  const wsRef = useRef<WebSocket|null>(null)
  useEffect(() => { const ws = new WebSocket(url); wsRef.current = ws; ws.onmessage = ev => { try{ setEvents(e=>[...e, JSON.parse(ev.data)]) }catch{} }; return () => ws.close() }, [url])
  return { events, ws: wsRef.current }
}
