"""Compose reusable recipes into an inspectable animation plan."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable

@dataclass
class Composition:
    scene: Any
    events: list[dict[str, Any]] = field(default_factory=list)
    occupied: dict[tuple[str,str], tuple[float,float,str]] = field(default_factory=dict)
    def add(self, result, parallel=False):
        for e in result.events: self.add_event(e, parallel=parallel)
        return self
    def add_event(self, event, parallel=False):
        target=event.get('target','*'); prop=event.get('property',event.get('event','event')); start=event.get('from',event.get('at',0)); end=event.get('to',start)
        key=(target,prop)
        if not parallel and key in self.occupied:
            a,b,old=self.occupied[key]
            if start < b and end > a: raise ValueError(f'Timeline conflict on {target}.{prop}: {old} overlaps {event.get("event",prop)}')
        self.occupied[key]=(start,end,event.get('event',prop)); self.events.append(event); return self
    def manifest(self):
        return {'event_count':len(self.events),'targets':sorted({e.get('target') for e in self.events if e.get('target')}),'duration':max([e.get('to',e.get('at',0)) for e in self.events] or [0]),'warnings':[]}
    def snapshot(self): return {'events':list(self.events),'manifest':self.manifest()}
