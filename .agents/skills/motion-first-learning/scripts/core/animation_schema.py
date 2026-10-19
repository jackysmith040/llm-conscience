"""Validation for renderer-neutral 2D/2.5D/3D scene specifications."""
from __future__ import annotations
from typing import Any

MODES={'2d','2.5d','3d'}
KINDS={'group','point','line','vector','axis','grid','plane','sphere','cube','cylinder','curve','mesh','rect','circle','polygon','text','image','arrow'}

def validate_scene(scene: dict[str, Any]) -> dict[str, Any]:
    errors=[]; warnings=[]
    if scene.get('schema_version') != 'animation-1.0': errors.append('Unsupported or missing schema_version')
    mode=scene.get('mode','2d')
    if mode not in MODES: errors.append(f'Unsupported mode: {mode}')
    objects=scene.get('objects',[]); ids=[o.get('id') for o in objects]
    if len(ids)!=len(set(ids)): errors.append('Object IDs must be unique')
    for o in objects:
        if not o.get('id'): errors.append('Object missing id')
        if o.get('kind') not in KINDS: errors.append(f"Unsupported object kind: {o.get('kind')}")
        pos=o.get('transform',{}).get('position',[0,0,0])
        if not isinstance(pos,list) or len(pos)!=3: errors.append(f"Invalid position for {o.get('id')}")
        if mode=='2d' and pos[2] != 0: warnings.append(f"2D object {o.get('id')} has nonzero z; ignored")
    for event in scene.get('timeline',[]):
        if 'at' not in event and not {'from','to'} <= set(event): errors.append('Timeline event needs at or from/to')
        if event.get('target') and event['target'] not in ids: errors.append(f"Unknown timeline target: {event['target']}")
    return {'ok':not errors,'errors':errors,'warnings':warnings,'object_count':len(objects),'mode':mode}
