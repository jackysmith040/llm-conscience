"""Deterministic timeline evaluation for educational animations."""
from __future__ import annotations
from typing import Any
from .animation import ease_in_out, lerp

def evaluate_value(a: Any, b: Any, t: float):
    t=ease_in_out(t)
    if isinstance(a,(int,float)) and isinstance(b,(int,float)): return lerp(a,b,t)
    if isinstance(a,list) and isinstance(b,list) and len(a)==len(b): return [evaluate_value(x,y,t) for x,y in zip(a,b)]
    return b if t>=1 else a

def evaluate_timeline(scene: dict[str,Any], time: float) -> dict[str,Any]:
    result={o['id']:dict(o) for o in scene.get('objects',[])}
    events=[]; pauses=[]
    for event in scene.get('timeline',[]):
        at=event.get('at', event.get('from',0)); end=event.get('to',at)
        if event.get('event')=='pause' or at in scene.get('learning',{}).get('pause_at',[]): pauses.append(at)
        if at<=time: events.append(event)
        target=event.get('target'); prop=event.get('property')
        if target in result and prop and at<=time:
            q=min(1,max(0,(time-at)/(end-at))) if end>at else 1
            result[target].setdefault('animated',{})[prop]=evaluate_value(event.get('from_value',event.get('value',[0,0])[0] if isinstance(event.get('value'),list) and len(event['value'])==2 else event.get('value')), event.get('to_value',event.get('value',[0,0])[1] if isinstance(event.get('value'),list) and len(event['value'])==2 else event.get('value')), q)
    return {'time':time,'objects':result,'events':events,'pause_points':sorted(set(pauses)),'paused':any(abs(time-p)<1e-6 for p in pauses)}
