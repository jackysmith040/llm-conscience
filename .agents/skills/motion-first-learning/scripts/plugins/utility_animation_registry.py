"""Registry facade for reusable Utility Animation Components."""
from __future__ import annotations
from .utility_animation_components import REGISTRY, lookup

def list_components(mode: str | None = None):
    items=[]
    for name, meta in REGISTRY.items():
        if mode is None or mode in meta['modes']:
            items.append({'name':name,'modes':meta['modes'],'version':meta['version'],'cost':meta['cost']})
    return sorted(items, key=lambda x:x['name'])

def get_component(name: str):
    if name not in REGISTRY: raise KeyError(f'Unknown component: {name}')
    return REGISTRY[name]['function']

def component_manifest():
    return {'api_version':'1.0','count':len(REGISTRY),'components':list_components()}
