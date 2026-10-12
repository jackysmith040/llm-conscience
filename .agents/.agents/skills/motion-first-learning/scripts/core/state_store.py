"""File-based session state primitives with explicit checkpoint and cleanup operations."""
from __future__ import annotations
import json, shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "1.0"

def _now() -> str:
    return datetime.now(timezone.utc).isoformat()

def create_session(objective: str, domain: str, learner_profile: dict[str, Any] | None = None) -> dict[str, Any]:
    return {"schema_version": SCHEMA_VERSION, "session_id": f"{domain}-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}", "domain": domain, "objective": objective, "learner_profile": learner_profile or {}, "current_state": "INIT", "adapter_version": "baseline", "mastery": {}, "evidence": [], "transition_history": [], "unresolved_questions": [], "next_action": "configure session", "updated_at": _now()}

def validate_state(state: dict[str, Any]) -> dict[str, Any]:
    required = ["schema_version", "session_id", "objective", "current_state", "adapter_version"]
    errors = [f"Missing field: {k}" for k in required if k not in state]
    return {"ok": not errors, "errors": errors, "warnings": [], "schema_version": state.get("schema_version")}

def save_state(state: dict[str, Any], path: str | Path) -> dict[str, Any]:
    check = validate_state(state)
    if not check["ok"]: return check
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    state = dict(state); state["updated_at"] = _now()
    path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return {"ok": True, "path": str(path), "errors": [], "warnings": []}

def load_state(path: str | Path) -> dict[str, Any]:
    state = json.loads(Path(path).read_text(encoding="utf-8"))
    check = validate_state(state)
    if not check["ok"]: raise ValueError("Invalid state: " + "; ".join(check["errors"]))
    return state

def create_checkpoint(state: dict[str, Any], workspace: str | Path, label: str = "validated") -> dict[str, Any]:
    workspace = Path(workspace); checkpoint_dir = workspace / "checkpoints"; checkpoint_dir.mkdir(parents=True, exist_ok=True)
    checkpoint = dict(state); checkpoint["checkpoint_label"] = label; checkpoint["checkpointed_at"] = _now()
    path = checkpoint_dir / f"{label}-{len(list(checkpoint_dir.glob('*.json')))+1:04d}.json"
    result = save_state(checkpoint, path)
    result["checkpoint"] = checkpoint
    return result

def resume_from_checkpoint(workspace: str | Path) -> dict[str, Any]:
    files = sorted(Path(workspace).glob("checkpoints/*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files: return {"ok": False, "errors": ["No checkpoint found"], "warnings": []}
    state = load_state(files[0])
    return {"ok": True, "state": state, "checkpoint_path": str(files[0]), "errors": [], "warnings": []}

def cleanup_session(workspace: str | Path, approved_summary: dict[str, Any] | None = None) -> dict[str, Any]:
    workspace = Path(workspace); summary_path = None
    if approved_summary is not None:
        summary_path = workspace / "approved-progress-summary.json"
        summary_path.write_text(json.dumps(approved_summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    removed = []
    for name in ("adapter", "evidence", "candidates", "artifacts"):
        target = workspace / name
        if target.exists(): shutil.rmtree(target); removed.append(str(target))
    return {"ok": True, "removed": removed, "summary_path": str(summary_path) if summary_path else None, "verified": all(not Path(p).exists() for p in removed), "errors": [], "warnings": []}
