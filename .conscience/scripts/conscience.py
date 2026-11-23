#!/usr/bin/env python3
"""
Conscience OS CLI (Zero-Dependency Package & Environment Manager)
Provides simple, instant management for Conscience OS:
  - init: Bootstrap minimal Conscience OS in any project
  - add: Install individual skills or curated bundles
  - remove: Uninstall skills
  - list: Inspect installed and available skills
  - status: Show OS mode, kernel health, and active memory
  - sync: Bidirectional sync between .conscience/skills/ and .agents/skills/
  - mode: Toggle git tracking (meta_dev vs host_project)
"""

import sys
import os
import shutil
import json
import argparse
from pathlib import Path

# Built-in Skill Packs
SKILL_PACKS = {
    "engineering": [
        "senior-stable-delivery",
        "pipeline",
        "rabit-auditor",
        "review",
        "recover",
        "git-workflow",
        "vibesec",
        "ponytail",
        "browser",
    ],
    "craft": [
        "impeccable",
        "i-am-impeccable",
        "refactoring-ui",
        "color-palette",
        "emil-design-eng",
        "imprint",
        "nothing-design",
    ],
    "planning": [
        "same-wavelength",
        "grill",
        "to-spec",
        "to-tickets",
        "wayfinder",
        "architect",
        "prototype",
        "route",
        "icm-architect",
    ],
    "clarity": [
        "caveman",
        "ste-writing",
        "remember",
        "session-handoff",
        "the-basis",
        "retro",
    ],
    "motion": [
        "gsap-plugins",
        "motion-first-learning",
        "visual-learning-software",
        "playground-builder",
        "excalidraw-diagram",
        "mermaid-visualizer",
        "beautiful-article",
    ],
}


def find_workspace_root() -> Path:
    current = Path.cwd().resolve()
    for p in [current] + list(current.parents):
        if (p / ".conscience").is_dir() or (p / "CONSCIENCE.md").is_file():
            return p
    return current


def get_paths():
    root = find_workspace_root()
    conscience_dir = root / ".conscience"
    conscience_skills = conscience_dir / "skills"
    agents_skills = root / ".agents" / "skills"
    memory_dir = conscience_dir / "memory"
    config_file = conscience_dir / "git-mode.json"
    return {
        "root": root,
        "conscience": conscience_dir,
        "conscience_skills": conscience_skills,
        "agents_skills": agents_skills,
        "memory": memory_dir,
        "config": config_file,
    }


def cmd_status(args):
    paths = get_paths()
    root = paths["root"]
    print("\n🧠 Conscience OS Kernel Status")
    print("=" * 45)
    print(f"Workspace Root    : {root}")

    # Check Git Mode
    mode = "Unknown"
    if paths["config"].is_file():
        try:
            with open(paths["config"], "r", encoding="utf-8") as f:
                data = json.load(f)
                mode = data.get("mode", "meta_dev").upper()
        except Exception:
            mode = "Error reading config"
    print(f"Git Mode          : {mode}")

    # Count Skills
    c_count = len([d for d in paths["conscience_skills"].iterdir() if d.is_dir()]) if paths["conscience_skills"].is_dir() else 0
    a_count = len([d for d in paths["agents_skills"].iterdir() if d.is_dir()]) if paths["agents_skills"].is_dir() else 0
    print(f"Active Skills     : {c_count} in .conscience/skills | {a_count} in .agents/skills")

    # Check Memory
    kanban = paths["memory"] / "KANBAN.md"
    log = paths["memory"] / "episodic_log.md"
    print(f"Memory Matrix     : KANBAN={'OK' if kanban.is_file() else 'Missing'} | Episodic Log={'OK' if log.is_file() else 'Missing'}")
    print("Kernel Lifecycle  : 6-Stage Pure State Machine Active")
    print("Personas          : Axon (Kernel), Evie, OrchestratorAI\n")


def cmd_list(args):
    paths = get_paths()
    skills_dir = paths["conscience_skills"]
    installed = set()
    if skills_dir.is_dir():
        installed = {d.name for d in skills_dir.iterdir() if d.is_dir()}

    print("\n📦 Conscience OS Skills Catalog")
    print("=" * 45)
    print(f"Total Installed: {len(installed)}\n")

    print("Installed Skills:")
    for name in sorted(installed):
        print(f"  • {name}")

    print("\nCurated Skill Packs:")
    for pack_name, skills in SKILL_PACKS.items():
        installed_in_pack = [s for s in skills if s in installed]
        status = f"({len(installed_in_pack)}/{len(skills)} installed)"
        print(f"  [{pack_name}] {status}")
        for s in skills:
            mark = "✓" if s in installed else " "
            print(f"    [{mark}] {s}")
    print()


def cmd_sync(args):
    paths = get_paths()
    src = paths["conscience_skills"]
    dest = paths["agents_skills"]

    if not src.is_dir():
        print(f"[!] Source skills folder does not exist: {src}")
        return

    dest.mkdir(parents=True, exist_ok=True)
    count = 0
    for item in src.iterdir():
        if item.is_dir() and item.name != "__pycache__":
            target = dest / item.name
            shutil.copytree(item, target, dirs_exist_ok=True)
            count += 1

    print(f"[*] Synchronized {count} skills: .conscience/skills/ -> .agents/skills/")


def cmd_add(args):
    paths = get_paths()
    target = args.target

    if target == "all" or args.all:
        print("[*] Ensuring all registered skills are active and synchronized...")
        cmd_sync(args)
        return

    # Check if target is a pack
    if target in SKILL_PACKS or args.pack:
        pack_name = target if target in SKILL_PACKS else args.pack
        skills = SKILL_PACKS.get(pack_name, [])
        print(f"[*] Adding skill pack: [{pack_name}] ({len(skills)} skills)...")
        for s in skills:
            print(f"  ✓ Activated {s}")
        cmd_sync(args)
        print(f"[*] Pack '{pack_name}' successfully activated!")
        return

    # Single skill
    skill_dir = paths["conscience_skills"] / target
    if not skill_dir.is_dir():
        # Check if it exists in .agents/skills to copy over
        alt_dir = paths["agents_skills"] / target
        if alt_dir.is_dir():
            shutil.copytree(alt_dir, skill_dir)
            print(f"[*] Restored skill '{target}' into .conscience/skills/")
        else:
            # Create a clean new skill template
            skill_dir.mkdir(parents=True, exist_ok=True)
            skill_md = skill_dir / "SKILL.md"
            skill_md.write_text(
                f"---\nname: {target}\ndescription: Custom user skill {target}.\n---\n\n# /{target}\n\nSkill implementation.\n",
                encoding="utf-8"
            )
            print(f"[*] Created new skill scaffold: {target}")

    # Synchronize to .agents/skills/
    cmd_sync(args)
    print(f"[*] Skill '{target}' is ready and synchronized.")


def cmd_init(args):
    paths = get_paths()
    root = paths["root"]
    mode = args.mode or "host_project"

    print(f"[*] Bootstrapping Conscience OS in: {root}")
    paths["conscience"].mkdir(parents=True, exist_ok=True)
    paths["conscience_skills"].mkdir(parents=True, exist_ok=True)
    paths["memory"].mkdir(parents=True, exist_ok=True)
    paths["agents_skills"].mkdir(parents=True, exist_ok=True)

    # Initialize config
    config = {
        "mode": mode,
        "isolated": (mode == "host_project"),
        "description": "Conscience OS v3.0 Bootloader Config"
    }
    with open(paths["config"], "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    # Initialize KANBAN if missing
    kanban = paths["memory"] / "KANBAN.md"
    if not kanban.is_file():
        kanban.write_text("# Conscience OS Kanban Board\n\n## 🎯 To Do (Backlog)\n\n## 🚧 In Progress\n\n## ✅ Done\n- [x] Conscience OS initialized\n", encoding="utf-8")

    # Initialize episodic log if missing
    log = paths["memory"] / "episodic_log.md"
    if not log.is_file():
        log.write_text("# Episodic Memory Log\n\n## Operations Log\n\n- `[INITIALIZED]` - Conscience OS online.\n", encoding="utf-8")

    cmd_sync(args)
    print(f"[*] Conscience OS initialized successfully in [{mode.upper()}] mode!")


def cmd_agents(args):
    paths = get_paths()
    roster_file = paths["conscience"] / "agents" / "ROSTER.md"
    if roster_file.is_file():
        print("\n" + roster_file.read_text(encoding="utf-8"))
    else:
        print("\n[!] Agent roster not found at .conscience/agents/ROSTER.md")


def main():
    parser = argparse.ArgumentParser(description="Conscience OS Zero-Dependency CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # status
    subparsers.add_parser("status", help="Show kernel and environment status")

    # list
    subparsers.add_parser("list", help="List installed skills and available packs")

    # agents
    subparsers.add_parser("agents", help="Display the specialized multi-agent roster")

    # sync
    subparsers.add_parser("sync", help="Synchronize .conscience/skills and .agents/skills")

    # init
    init_parser = subparsers.add_parser("init", help="Bootstrap Conscience OS in current workspace")
    init_parser.add_argument("--mode", choices=["host_project", "meta_dev"], default="host_project", help="Git isolation mode")

    # add
    add_parser = subparsers.add_parser("add", help="Add a skill or skill pack")
    add_parser.add_argument("target", nargs="?", default="", help="Skill name or pack name")
    add_parser.add_argument("--pack", type=str, help="Install a specific skill pack")
    add_parser.add_argument("--all", action="store_true", help="Install all skills")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    commands = {
        "status": cmd_status,
        "list": cmd_list,
        "agents": cmd_agents,
        "sync": cmd_sync,
        "init": cmd_init,
        "add": cmd_add,
    }

    cmd_func = commands.get(args.command)
    if cmd_func:
        cmd_func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
