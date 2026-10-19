---
name: to-tickets
description: >-
  Break a spec or plan into tracer-bullet vertical tickets with explicit blocking edges,
  published directly to KANBAN.md. Run after /to-spec. Trigger: /to-tickets.
---

# /to-tickets

[STATE: MOTOR_EXECUTION | INTENT: ARCHITECTURE | PACE: STANDARD]

**Pipeline position**: Step 3 of 6 — runs after `/to-spec`, before `/implement`.

## What
Decomposes an approved specification into **tracer-bullet vertical slices**, each declaring explicit blocking dependencies. Publishes the tickets directly to `.conscience/memory/KANBAN.md`.

## Vertical Slice Rules
- **Vertical, not horizontal**: Each slice cuts through all necessary layers (types/schema, logic/API, UI/CLI, test). Never write a ticket that is "just the database" or "just the UI".
- **Verifiable in isolation**: A completed ticket must pass tests or be demoable on its own.
- **Sized for one context session**: Small enough for a single focused implementation step (under Law 20 review limits).
- **Explicit blockers**: Each ticket states its dependency (`Blocked by: Ticket A`). Tickets with no blockers are the immediate **frontier**.
- **Wide refactors**: If a change touches hundreds of call sites, sequence via **expand–contract** (expand: add new alongside old; migrate call sites in batches; contract: remove old).

## Process
1. **Read Spec**: Ingest the spec from `KANBAN.md` or the active conversation. Reference vocabulary from `GLOSSARY.md`.
2. **Draft Slices**: Split into numbered vertical slices with explicit names and blocking tags.
3. **Publish to KANBAN**: Add tickets to `.conscience/memory/KANBAN.md` under `## 🎯 To Do (Backlog)` using:
   `- [ ] [TICKET-ID] Ticket Name (Blocked by: [ID / None])`
4. **Log**: Record summary in `.conscience/memory/episodic_log.md`.

---

> 🚀 **Tickets published?** → Next: pick the unblocked frontier ticket and run `/implement` (or `/implement-spec` for parallel execution).
