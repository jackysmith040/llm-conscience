"""Route structured learning models to readable visual artifacts."""
from __future__ import annotations
from pathlib import Path
from typing import Any

SUPPORTED = {"state_machine", "flow", "architecture", "dependency", "process", "proof", "argument", "spatial", "quantitative"}

def route(model_type: str, model: dict[str, Any], output_dir: str | Path) -> dict[str, Any]:
    if model_type not in SUPPORTED:
        return {"ok": False, "errors": [f"Unsupported model type: {model_type}"], "warnings": []}
    out = Path(output_dir); out.mkdir(parents=True, exist_ok=True)
    source = out / f"{model_type}.mmd"
    accessible = out / f"{model_type}.txt"
    title = model.get("title", model_type.replace("_", " ").title())
    lines = [f"---", f"title: {title}", "---"]
    if model_type in {"state_machine", "flow", "architecture", "dependency", "proof", "argument"}:
        lines.append("flowchart LR")
        nodes = model.get("nodes", [])
        for node in nodes:
            node_id, label = node.get("id"), node.get("label", node.get("id"))
            lines.append(f'    {node_id}["{label}"]')
        for edge in model.get("edges", []):
            lines.append(f'    {edge["source"]} -->|{edge.get("label", "")} | {edge["target"]}')
    else:
        lines.append("flowchart LR")
        for i, state in enumerate(model.get("states", [])):
            lines.append(f'    s{i}["{state}"]')
            if i: lines.append(f"    s{i-1} --> s{i}")
    source.write_text("\n".join(lines) + "\n", encoding="utf-8")
    description = model.get("accessible_text") or f"{title}. " + "; ".join(str(x) for x in model.get("description", []))
    accessible.write_text(description.strip() + "\n", encoding="utf-8")
    return {"ok": True, "source": str(source), "accessible_text": str(accessible), "errors": [], "warnings": []}
