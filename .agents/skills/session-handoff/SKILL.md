---
name: session-handoff
description: >-
  Compact end-of-session continuation for humans and next agent. Filters out noise and outputs
  Layer A paste block and Layer B HANDOFF.md with objective, locked decisions, and next actions. Trigger: /session-handoff.
---

# /session-handoff

## What
A relevance-filtered snapshot of the session so the next human or agent can continue without context pollution. Modeled after tight continuation blocks: tight executive context, explicit next actions, zero transcript spam.

## When
- User says handoff, continue later, or ends a session mid-ticket.
- Before switching to a new chat in the same repo.
- After completing a milestone.

## Tiered Output
1. **Layer A — Paste Block**: Markdown (<= 120 lines) for pasting directly into the next chat session.
2. **Layer B — File**: Written to `HANDOFF.md` at project root.

## Layer A Template
```markdown
## HANDOFF — {project} — {ticket or topic}
**Status:** {in progress | blocked | ready for PR | done}
**Branch:** {name or unknown}

### Objective
{one sentence}

### Locked decisions
- ...

### Current state
{2–5 bullets: what was implemented, what was not}

### Files (high signal)
- `path` — {why}

### Tests
- Last: `{command}` → {pass | fail}

### Next session (do these first)
1. ...
2. ...
3. ...
```
