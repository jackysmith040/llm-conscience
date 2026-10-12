"""Deterministic renderer selection for unified educational animation scenes."""
from __future__ import annotations
from typing import Any

def choose(scene: dict[str, Any], needs_interaction=False, needs_continuous_motion=False, complexity_budget=200) -> dict[str, Any]:
    mode=scene.get('mode','2d'); objects=scene.get('objects',[]); count=len(objects)
    if count > complexity_budget:
        return {'renderer':'staged_frames','reason':'scene exceeds complexity budget','fallback':'2d'}
    if mode=='3d':
        if needs_interaction: return {'renderer':'webgl_3d','reason':'interactive spatial scene','fallback':'2.5d'}
        if needs_continuous_motion: return {'renderer':'manim_3d_preview','reason':'continuous 3D motion','fallback':'webgl_3d'}
        return {'renderer':'webgl_3d','reason':'spatial scene','fallback':'2.5d'}
    if mode=='2.5d':
        return {'renderer':'canvas_2_5d','reason':'layered depth/parallax','fallback':'2d'}
    if needs_interaction: return {'renderer':'canvas_2d','reason':'interactive flat scene','fallback':'svg'}
    if needs_continuous_motion: return {'renderer':'pillow_ffmpeg_2d','reason':'short deterministic motion','fallback':'staged_frames'}
    return {'renderer':'svg_2d','reason':'crisp labeled vector scene','fallback':'pillow_ffmpeg_2d'}
