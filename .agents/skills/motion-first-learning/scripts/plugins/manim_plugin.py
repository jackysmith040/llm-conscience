"""Optional Manim adapter metadata and command planning.

This plugin does not import Manim at module load time. It plans preview/final
renders so the core workflow remains usable when Manim is absent or slow.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

@dataclass
class RenderPlan:
    scene_file: str
    output_dir: str
    quality: str = "preview"
    frame_rate: int = 15
    resolution: str = "854x480"
    fallback: str = "staged_frames"
    estimated_cost: str = "unknown"
    def to_dict(self) -> dict[str, Any]: return asdict(self)

def plan_render(scene_file: str, output_dir: str, quality: str = "preview", fallback: str = "staged_frames") -> RenderPlan:
    if quality == "final":
        return RenderPlan(scene_file, output_dir, "final", 30, "1920x1080", fallback, "high")
    return RenderPlan(scene_file, output_dir, "preview", 15, "854x480", fallback, "low")

def command(plan: RenderPlan) -> list[str]:
    quality_flag = "-ql" if plan.quality == "preview" else "-qh"
    return ["manim", quality_flag, plan.scene_file]

def fallback_manifest(plan: RenderPlan) -> dict[str, Any]:
    return {"ok": True, "renderer": "manim", "plan": plan.to_dict(), "fallback": plan.fallback, "non_blocking": True}
