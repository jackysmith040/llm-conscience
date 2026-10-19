---
name: to-spec
description: >-
  Turn the current conversation into a structured spec and publish it to KANBAN.md.
  No interview — pure synthesis of what has already been discussed. Run after /grill or /same-wavelength.
  Trigger: /to-spec.
---

# /to-spec

[STATE: MOTOR_EXECUTION | INTENT: IMPLEMENTATION | PACE: STANDARD]

**Pipeline position**: Step 2 of 6 — runs after `/grill`, before `/to-tickets`.

## What

Synthesize everything already discussed into a versioned, structured spec and publish it as a KANBAN task. Do NOT interview the user again — the grill already happened.

## Process

1. **Explore the repo** (if you haven't already). Understand the current codebase state, relevant files, and any ADRs or constraints in play. Use terms from `GLOSSARY.md` throughout.

2. **Identify test seams**. Sketch the boundary points where the feature can be tested. Prefer existing seams over new ones. Use the highest seam possible. Confirm with the user if seams are non-obvious.

3. **Write the spec** using the template below.

4. **Publish to KANBAN**: Append the spec as a new task in `.conscience/memory/KANBAN.md` under `## 🎯 To Do (Backlog)` with checkbox `- [ ]`.

5. **Log the session**: Append a one-line summary to `.conscience/memory/episodic_log.md`.

6. **Hand off**: Tell the user → `Spec published. Next: run /to-tickets to split this into buildable tasks.`

## Spec Template

```markdown
## Spec: <title>

**Date**: <ISO date>
**Status**: ready-for-tickets

### Problem Statement
<The problem from the user's perspective. One paragraph.>

### Solution
<The proposed solution. What changes, at what level of abstraction.>

### Test Seams
- <Seam 1: file or boundary where tests attach>
- <Seam 2: ...>

### Acceptance Criteria
- [ ] <Verifiable criterion 1>
- [ ] <Verifiable criterion 2>
- [ ] <Verifiable criterion 3>

### Implementation Notes
<Constraints, gotchas, dependencies, or architecture decisions that must be respected.>
```

## Rules

- Use domain terms from `GLOSSARY.md`. Never invent synonyms.
- One spec per `/to-spec` invocation. If multiple features were discussed, create one spec per feature.
- Never auto-start implementation. The spec requires explicit approval or a `/to-tickets` run.
