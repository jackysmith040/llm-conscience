"""Stable contract for composable animation recipes."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class RecipeResult:
    recipe_id: str
    events: list[dict[str, Any]] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    cost: dict[str, Any] = field(default_factory=dict)
    accessible_text: str = ''
    def as_dict(self): return {'recipe_id':self.recipe_id,'events':self.events,'warnings':self.warnings,'cost':self.cost,'accessible_text':self.accessible_text}

def require_targets(scene, targets):
    ids={e.element_id for e in getattr(scene,'elements',[])}
    missing=[x for x in targets if x not in ids]
    if missing: raise ValueError('Unknown animation targets: '+', '.join(missing))

def keyframe(name, start, end, a, b):
    from .animation import Keyframe
    return Keyframe(start, end, {name:(a,b)})
