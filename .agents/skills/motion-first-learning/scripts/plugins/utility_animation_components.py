"""Reusable semantic animation recipes for motion-first lessons."""
from __future__ import annotations
from typing import Any
from core.recipe_contract import RecipeResult, require_targets

REGISTRY = {}

def _reg(fn, name=None, modes=('2d','2.5d','3d')):
    REGISTRY[name or fn.__name__]={'name':name or fn.__name__,'function':fn,'modes':modes,'version':'1.0','cost':{'events':1}}
    return fn

def _result(name, target, text, **event):
    return RecipeResult(name, [dict({'recipe_id':name,'target':target}, **event)], cost={'events':1}, accessible_text=text)

@_reg
def reveal_object(scene, target, start=0, duration=.5, **_):
    require_targets(scene,[target]); return _result('reveal_object',target,f'Reveal object {target}.',**{'from':start,'to':start+duration,'event':'show'})

@_reg
def reveal_label(scene, target, start=0, duration=.4, **_):
    require_targets(scene,[target]); return _result('reveal_label',target,f'Reveal the label for {target}.',**{'from':start,'to':start+duration,'event':'label_reveal'})

@_reg
def move_object(scene, target, start, duration, position_from, position_to, **_):
    require_targets(scene,[target]); return _result('move_object',target,f'Move {target} from {position_from} to {position_to}.',**{'from':start,'to':start+duration,'event':'move','property':'position','value':[position_from,position_to]})

@_reg
def draw_arrow(scene, target, start=0, duration=.6, **_):
    require_targets(scene,[target]); return _result('draw_arrow',target,f'Draw an arrow for {target}.',**{'from':start,'to':start+duration,'event':'draw_on','property':'progress','value':[0,1]})

@_reg
def trace_curve(scene, target, start, duration, **_):
    require_targets(scene,[target]); return _result('trace_curve',target,f'Trace the path of {target}.',**{'from':start,'to':start+duration,'event':'trace','property':'progress','value':[0,1]})

@_reg
def assemble_parts(scene, targets, start, duration, **_):
    require_targets(scene,targets); return RecipeResult('assemble_parts',[{'recipe_id':'assemble_parts','target':t,'from':start,'to':start+duration,'event':'assemble'} for t in targets],cost={'events':len(targets)},accessible_text='Assemble the parts into one system.')

@_reg
def split_group(scene, target, start, duration, **_):
    require_targets(scene,[target]); return _result('split_group',target,f'Split group {target} into its component parts.',**{'from':start,'to':start+duration,'event':'split'})

@_reg
def rotate_about_axis(scene, target, axis, start, duration, angle_from, angle_to, **_):
    require_targets(scene,[target]); return _result('rotate_about_axis',target,f'Rotate {target} around the {axis}-axis.',**{'from':start,'to':start+duration,'event':'rotate','property':f'rotation.{axis}','value':[angle_from,angle_to]})

@_reg
def camera_orbit(scene, start, duration, angle_from, angle_to, **_):
    return RecipeResult('camera_orbit',[{'recipe_id':'camera_orbit','target':'camera','from':start,'to':start+duration,'event':'camera_orbit','property':'angle','value':[angle_from,angle_to]}],cost={'events':1},accessible_text='Orbit the camera to reveal the spatial relationship.')

@_reg
def camera_reset(scene, start=0, **_): return RecipeResult('camera_reset',[{'recipe_id':'camera_reset','target':'camera','at':start,'event':'camera_reset'}],accessible_text='Reset the camera to the canonical view.')

@_reg
def parallax_layers(scene, targets, start, duration, shift, **_):
    require_targets(scene,targets); return RecipeResult('parallax_layers',[{'recipe_id':'parallax_layers','target':t,'from':start,'to':start+duration,'event':'parallax','property':'camera_shift','value':shift} for t in targets],cost={'events':len(targets)},accessible_text='Move layered objects with different depth responses to reveal parallax.')

@_reg
def axis_reveal(scene, target, start=0, duration=.5, **_): return _result('axis_reveal',target,f'Reveal coordinate axis {target}.',**{'from':start,'to':start+duration,'event':'axis_reveal'})

@_reg
def project_vector(scene, target, plane, start, duration, **_):
    require_targets(scene,[target]); return _result('project_vector',target,f'Project {target} onto the {plane}-plane.',**{'from':start,'to':start+duration,'event':'project','property':'projection','value':[0,1]})

@_reg
def before_after_compare(scene, target, start, duration, **_):
    require_targets(scene,[target]); return _result('before_after_compare',target,f'Compare the before and after states of {target}.',**{'from':start,'to':start+duration,'event':'compare'})

@_reg
def show_invariant(scene, target, property, label, start=0, **_):
    require_targets(scene,[target]); return _result('show_invariant',target,f'Invariant: {label} remains unchanged for {target}.',at=start,event='invariant',property=property)

@_reg
def pause_for_prediction(scene, prompt, at, **_): return RecipeResult('pause_for_prediction',[{'recipe_id':'pause_for_prediction','target':'learning','at':at,'event':'pause','prompt':prompt}],accessible_text=f'Pause and predict: {prompt}')

@_reg
def hide_then_reveal(scene, target, hide_at, reveal_at, **_):
    require_targets(scene,[target]); return RecipeResult('hide_then_reveal',[{'recipe_id':'hide_then_reveal','target':target,'at':hide_at,'event':'hide'},{'recipe_id':'hide_then_reveal','target':target,'at':reveal_at,'event':'show'}],cost={'events':2},accessible_text=f'Hide {target}, ask for prediction, then reveal it.')

@_reg
def transfer_prompt(scene, prompt, at, **_): return RecipeResult('transfer_prompt',[{'recipe_id':'transfer_prompt','target':'learning','at':at,'event':'transfer_prompt','prompt':prompt}],accessible_text=f'Transfer task: {prompt}')

def lookup(intent: str, mode: str | None = None):
    matches=[meta for meta in REGISTRY.values() if intent.lower() in meta['name'].lower() and (mode is None or mode in meta['modes'])]
    return [{k:v for k,v in meta.items() if k!='function'} for meta in matches]
