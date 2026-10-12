#!/usr/bin/env python3
"""
Git Mode Manager for Conscience OS
Handles dual-mode operation:
- 'host_project': Isolates Conscience OS from host repository git tracking, injecting .gitignore entries.
- 'meta_dev': Enables git tracking on Conscience OS to develop and improve the core system.
"""

import sys
import os
import json
from datetime import datetime
from pathlib import Path

CONFIG_FILENAME = "git-mode.json"

GITIGNORE_MARKER_START = "# >>> Conscience OS Isolation (Host Mode) >>>"
GITIGNORE_MARKER_END = "# <<< Conscience OS Isolation (Host Mode) <<<"

GITIGNORE_ENTRIES = [
    ".conscience/",
    ".agents/memory/",
    ".agents/git-mode.json",
    "memory/episodic_log.md",
    "memory/KANBAN.md",
    "memory/feedback.md",
    "memory/graph/brain_data.js",
    "memory/neocortex/",
    "memory/wiki/",
    "INBOX.md",
]


def find_workspace_root() -> Path:
    current = Path.cwd().resolve()
    for p in [current] + list(current.parents):
        if (p / ".agents").is_dir() or (p / "CONSCIENCE.md").is_file():
            return p
    return current


def get_config_path() -> Path:
    root = find_workspace_root()
    return root / ".agents" / CONFIG_FILENAME


def load_config() -> dict:
    cfg_path = get_config_path()
    if cfg_path.is_file():
        try:
            with open(cfg_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "mode": "meta_dev",
        "isolated": False,
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "description": "Default configuration",
    }


def save_config(cfg: dict) -> None:
    cfg_path = get_config_path()
    cfg_path.parent.mkdir(parents=True, exist_ok=True)
    with open(cfg_path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)


def apply_host_gitignore(root: Path) -> bool:
    gitignore_path = root / ".gitignore"
    existing = ""
    if gitignore_path.is_file():
        existing = gitignore_path.read_text(encoding="utf-8")

    if GITIGNORE_MARKER_START in existing:
        return True  # Already injected

    block = "\n\n" + GITIGNORE_MARKER_START + "\n"
    for entry in GITIGNORE_ENTRIES:
        block += f"{entry}\n"
    block += GITIGNORE_MARKER_END + "\n"

    new_content = existing.rstrip() + block
    gitignore_path.write_text(new_content, encoding="utf-8")
    return True


def remove_host_gitignore(root: Path) -> bool:
    gitignore_path = root / ".gitignore"
    if not gitignore_path.is_file():
        return False
    content = gitignore_path.read_text(encoding="utf-8")
    if GITIGNORE_MARKER_START not in content:
        return False

    start = content.find(GITIGNORE_MARKER_START)
    end = content.find(GITIGNORE_MARKER_END)
    if start != -1 and end != -1:
        end += len(GITIGNORE_MARKER_END)
        cleaned = content[:start].rstrip() + "\n" + content[end:].lstrip()
        gitignore_path.write_text(cleaned.strip() + "\n", encoding="utf-8")
        return True
    return False


def set_mode(mode: str) -> None:
    root = find_workspace_root()
    cfg = load_config()

    if mode == "host_project":
        cfg["mode"] = "host_project"
        cfg["isolated"] = True
        cfg["last_updated"] = datetime.utcnow().isoformat() + "Z"
        apply_host_gitignore(root)
        save_config(cfg)
        print(f"[*] Mode updated: HOST_PROJECT (Isolated)")
        print(f"[*] Injected Conscience OS isolation block into {root / '.gitignore'}")
        print("[*] Agent memory and brain states are shielded from host git.")
    elif mode == "meta_dev":
        cfg["mode"] = "meta_dev"
        cfg["isolated"] = False
        cfg["last_updated"] = datetime.utcnow().isoformat() + "Z"
        remove_host_gitignore(root)
        save_config(cfg)
        print(f"[*] Mode updated: META_DEV (Tracked)")
        print("[*] Conscience OS tracking enabled for core system improvements.")
    else:
        print(f"[!] Unknown mode '{mode}'. Choose 'host_project' or 'meta_dev'.")
        sys.exit(1)


def print_status() -> None:
    root = find_workspace_root()
    cfg = load_config()
    mode = cfg.get("mode", "unknown")
    isolated = cfg.get("isolated", False)
    print("=" * 55)
    print("  Conscience OS Git Mode Status")
    print("=" * 55)
    print(f"  Workspace Root : {root}")
    print(f"  Active Mode    : {mode.upper()}")
    print(f"  Git Isolated   : {'YES (Shielded from Host Git)' if isolated else 'NO (Core Development Mode)'}")
    print(f"  Last Updated   : {cfg.get('last_updated', 'N/A')}")
    print("=" * 55)
    print("  Commands:")
    print("    python git_mode_manager.py set host_project  -> Isolate agent")
    print("    python git_mode_manager.py set meta_dev      -> Track agent")
    print("=" * 55)


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("status", "-s"):
        print_status()
    elif sys.argv[1] == "set" and len(sys.argv) >= 3:
        set_mode(sys.argv[2])
    elif sys.argv[1] in ("isolate", "host"):
        set_mode("host_project")
    elif sys.argv[1] in ("dev", "meta"):
        set_mode("meta_dev")
    else:
        print("Usage: python git_mode_manager.py [status | isolate | dev | set <mode>]")


if __name__ == "__main__":
    main()
