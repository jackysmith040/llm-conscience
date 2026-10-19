---
name: wayfinder
description: >-
  Plan multi-session big efforts wrapped in fog as a shared Decision Map.
  Resolves architectural and design questions one at a time, graduating resolved decisions into KANBAN tasks.
  Trigger: /wayfinder.
---

# /wayfinder

[STATE: MOTOR_EXECUTION | INTENT: ARCHITECTURE | PACE: STANDARD]

**Altitude**: Strategic Planning — runs BEFORE the Main Flow for efforts too large for a single session.

## What
When an effort is too big or ambiguous to spec immediately, `/wayfinder` builds and navigates a **Decision Map** at `.conscience/memory/DECISION_MAP.md`. It tracks questions whose resolution is a *decision* (not immediate code execution).

## Process

1. **Orientation**: Read `.conscience/memory/DECISION_MAP.md` (if it exists) and `.conscience/memory/KANBAN.md`. If starting fresh, define the **Destination** (1–2 sentences describing what reaching the end looks like).

2. **Chart or Advance the Frontier**:
   - Identify the immediate unanswered architectural questions ("Decision Tickets").
   - Give each decision ticket a clear name, rationale, and options.
   - Categorize unanswerable fog under `## Not Yet Specified` and non-goals under `## Out of Scope`.

3. **Resolve One Decision**:
   - Focus on exactly ONE decision ticket from the frontier per step.
   - Drive the tradeoff analysis with the user or codebase inspection.
   - Once resolved, record the 1-line gist in `## Decisions So Far`.

4. **Graduate to Execution**:
   - Convert the resolved decision into an actionable ticket in `.conscience/memory/KANBAN.md` under `## 🎯 To Do (Backlog)`.
   - Update `.conscience/memory/episodic_log.md` with the session resolution.

5. **Hand off to Main Flow**:
   - When the path to the destination is clear, hand off to `/grill` or `/to-spec`.

---

> 🎯 **Next step**: If the decision is ready to be specified, run `/to-spec` or `/grill`. If more decisions remain on the frontier, continue with `/wayfinder`.
