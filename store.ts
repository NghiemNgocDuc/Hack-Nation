import { useState } from 'react'
export function useLines(){ return useState<any[]>([]) }
export function useRisk(){ return useState<{score:number,label:string}|null>(null) }
