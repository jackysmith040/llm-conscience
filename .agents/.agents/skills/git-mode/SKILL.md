---
name: git-mode
description: >-
  Inspect or toggle Conscience OS Git tracking mode: 'host_project' (isolates agent git & memory from host repo)
  vs 'meta_dev' (tracks agent system changes for core evolution). Trigger: /git-mode.
---

# /git-mode

Controls whether Conscience OS operates as an isolated subsystem in a host project or tracks git history for core OS development.

## Modes

1. **`host_project` (Isolated Mode)**:
   - Use when working inside a separate product or client repository.
   - Shields the host repository from agent memory, episodic logs, KANBAN, and internal graph data.
   - Automatically maintains a clean `.gitignore` exclusion block in the host project root.
   - Agent does not track or commit internal state to the host repo.

2. **`meta_dev` (Tracked Mode)**:
   - Use when actively developing, modifying, or improving Conscience OS itself.
   - Normal git tracking is enabled for the Conscience OS repository.

## Commands

- `/git-mode status` — Displays active mode, workspace root, and isolation state.
- `/git-mode isolate` (or `/git-mode host`) — Switches to `host_project` mode and applies `.gitignore` rules.
- `/git-mode dev` (or `/git-mode meta`) — Switches to `meta_dev` mode.

## Agent Protocol
When the user invokes `/git-mode` without arguments:
1. Run `python .agents/scripts/git_mode_manager.py status`.
2. Present the active mode and ask if they wish to toggle between `host_project` and `meta_dev`.
3. If switching to `host_project`, execute `python .agents/scripts/git_mode_manager.py set host_project`.
4. If switching to `meta_dev`, execute `python .agents/scripts/git_mode_manager.py set meta_dev`.
