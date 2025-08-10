export default function TranscriptList({lines}:{lines:{t0:number,t1:number,lang:string,speaker:string,text:string}[]}){
  return (<div className="transcript">{lines.map((l,i)=>(<div key={i} className={`line ${l.speaker}`}><span className="ts">[{l.t0.toFixed(1)}–{l.t1.toFixed(1)}] ({l.lang})</span><span className="who">{l.speaker}:</span><span className="txt">{l.text}</span></div>))}</div>)}
