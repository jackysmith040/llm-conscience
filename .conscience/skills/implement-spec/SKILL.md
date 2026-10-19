---
name: implement-spec
description: >-
  Orchestrate parallel multi-agent implementation of a spec and ticket graph from KANBAN.md.
  Spawns worker subagents on unblocked tickets, manages the frontier, and merges cleanly. Trigger: /implement-spec.
---

# /implement-spec

[STATE: MOTOR_EXECUTION | INTENT: IMPLEMENTATION | PACE: STANDARD]

**Pipeline position**: Step 4 (Parallel) of 6 — runs after `/to-tickets`, before `/code-review`.

## What
Executes an entire ticket graph from `.conscience/memory/KANBAN.md` using subagents. Navigates the dependency graph by advancing the unblocked **frontier**.

## Core Orchestration Rules
1. **Context Pointers Only**: When dispatching subagents, pass file pointers (`spec path`, `ticket ID`, `GLOSSARY.md`, test seam file paths). Never dump huge code blocks into subagent prompts.
2. **The Frontier**: Only tickets whose dependencies (`Blocked by: None` or all blockers completed) are eligible to be grabbed.
3. **Subagent Specialization**:
   - **Exploration Subagent**: Checks existing codebase patterns and test harnesses.
   - **Implementer Subagent**: Executes one single vertical slice ticket.
4. **Law 20 Enforcement**: Every subagent change must respect cognitive ownership and review limits.
5. **Progressive Merge**:
   - Verify tests pass on each ticket completion.
   - Check off `- [x] [TICKET-ID]` in `.conscience/memory/KANBAN.md`.
   - Recalculate frontier and grab newly unblocked tickets.

## Process
1. **Load Graph**: Read `KANBAN.md` and parse ticket blockers.
2. **Identify Frontier**: Find all tickets with all blockers checked off.
3. **Dispatch Workers**: Launch implementer subagents on frontier tickets.
4. **Verify & Mark Complete**: As each subagent finishes, test the seam, update `KANBAN.md`, and log to `episodic_log.md`.
5. **Cycle until Spec Complete**: Repeat until all tickets under the active spec are resolved.

---

> 🏁 **All tickets green?** → Next: run `/code-review` (or `/rabit-auditor`) for a multi-pass security and architectural audit.
