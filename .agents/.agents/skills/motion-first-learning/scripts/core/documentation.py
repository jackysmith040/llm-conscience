"""Lightweight documentation freshness checks for the Core/Plugin API."""
from __future__ import annotations
import ast
from pathlib import Path
from typing import Any

def public_functions(path: str | Path) -> list[str]:
    tree = ast.parse(Path(path).read_text(encoding="utf-8"))
    return sorted(node.name for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not node.name.startswith("_"))

def check_freshness(source_files: list[str | Path], documentation: str | Path) -> dict[str, Any]:
    docs = Path(documentation).read_text(encoding="utf-8")
    discovered = []
    missing = []
    for source in source_files:
        names = public_functions(source)
        discovered.extend(names)
        missing.extend(name for name in names if name not in docs)
    return {"ok": not missing, "discovered": sorted(set(discovered)), "missing": sorted(set(missing)), "errors": [f"Undocumented public API: {x}" for x in sorted(set(missing))], "warnings": []}
