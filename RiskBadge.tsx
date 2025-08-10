export default function RiskBadge({val}:{val:{score:number,label:string}|null}){
  return <span className="risk">{val ? `${val.label} (${val.score})` : '—'}</span>
}
