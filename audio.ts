export async function startAudio(ws: WebSocket, sessionId: string) {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
  const ctx = new (window.AudioContext || (window as any).webkitAudioContext)({ sampleRate: 48000 })
  const source = ctx.createMediaStreamSource(stream)
  const processor = ctx.createScriptProcessor(4096, 1, 1)
  const targetRate = 16000
  let seq = 0
  processor.onaudioprocess = (e) => {
    const input = e.inputBuffer.getChannelData(0)
    const down = downsample(input, ctx.sampleRate, targetRate)
    const int16 = floatTo16BitPCM(down)
    const b64 = btoa(String.fromCharCode(...new Uint8Array(int16.buffer)))
    ws.readyState === ws.OPEN && ws.send(JSON.stringify({ type:'audio', seq: ++seq, sr: targetRate, session_id: sessionId, pcm16_b64: b64 }))
  }
  source.connect(processor); processor.connect(ctx.destination)
  return () => { processor.disconnect(); source.disconnect(); stream.getTracks().forEach(t=>t.stop()); ctx.close() }
}
function downsample(buffer: Float32Array, inRate: number, outRate: number){ if(outRate===inRate) return buffer; const ratio=inRate/outRate; const outLength=Math.floor(buffer.length/ratio); const result=new Float32Array(outLength); for(let i=0;i<outLength;i++){ const start=Math.floor(i*ratio), end=Math.floor((i+1)*ratio); let sum=0; for(let j=start;j<end && j<buffer.length;j++) sum += buffer[j]; result[i]=sum/Math.max(1,end-start) } return result }
function floatTo16BitPCM(float32: Float32Array){ const out=new Int16Array(float32.length); for(let i=0;i<float32.length;i++){ let s=Math.max(-1,Math.min(1,float32[i])); out[i]= s< 0 ? s*0x8000 : s*0x7fff } return out }
