"""Session-scoped scene builder for the lightweight animation Core."""
from __future__ import annotations
from pathlib import Path
from typing import Any
from core.animation import Scene, Element, Keyframe, Renderer


def build_scene(spec: dict[str, Any]) -> Scene:
    scene = Scene(width=spec.get('width',1280), height=spec.get('height',480), fps=spec.get('fps',12), duration=spec.get('duration',6.0), title=spec.get('title',''))
    for raw in spec.get('elements', []):
        keyframes=[]
        for k in raw.get('keyframes', []):
            keyframes.append(Keyframe(k['start'], k['end'], {name: tuple(values) for name, values in k.get('values', {}).items()}))
        scene.add(Element(raw['id'], raw['kind'], raw.get('props', {}), keyframes))
    return scene


def render_scene(spec: dict[str, Any], output_dir: str | Path, name: str = 'learning_animation') -> dict[str, Any]:
    return Renderer(build_scene(spec)).export(output_dir, name)
