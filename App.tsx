import { useMemo, useState } from 'react'
import { useFeed } from './lib/useFeed'
import TranscriptList from './components/TranscriptList'
import { startAudio } from './audio'
const WS_URL = (import.meta as any).env?.VITE_WS_URL || (import.meta as any).env?.NEXT_PUBLIC_WS_URL || 'ws://localhost:5050/ws'
export default function App(){
  const sessionId = useMemo(()=>crypto.randomUUID(),[])
  const {events, ws} = useFeed(WS_URL)
  const [on, setOn] = useState(false)
  const [risk, setRisk] = useState<{score:number,label:string}|null>(null)
  const [lines, setLines] = useState<any[]>([])
  if(events.length){
    const e = events[events.length-1]
    if(e.type==='transcript' && !e.partial){ if(!lines.find(l=>l.t0===e.t0 && l.t1===e.t1)) setLines([...lines,{t0:e.t0,t1:e.t1,lang:e.lang,speaker:e.speaker||'caller',text:e.text}]) }
    if(e.type==='risk'){ if(!risk || risk.score!==e.score) setRisk({score:e.score,label:e.label}); if(e.label==='SCAM') speakOnce('This call may be fraudulent. Do not share verification codes.') }
  }
  return (<div className="wrap"><h1>Voice Scam Shield</h1><div className="controls"><button onClick={()=>toggle(ws,sessionId,setOn)}>{on?'Stop':'Start'}</button><span className="dot" data-on={on}></span><span className="risk">{risk?`${risk.label} (${risk.score})`:'—'}</span></div><TranscriptList lines={lines}/></div>)
}
async function toggle(ws:WebSocket|undefined, sessionId:string, setOn:(b:boolean)=>void){ if(!ws) return; if((ws as any)._stop){ (ws as any)._stop(); (ws as any)._stop=null; setOn(false); return } const stop = await startAudio(ws, sessionId); (ws as any)._stop = stop; setOn(true) }
function speakOnce(t:string){ const s=(window as any).speechSynthesis; if(!s||s.speaking)return; s.speak(new SpeechSynthesisUtterance(t)) }
