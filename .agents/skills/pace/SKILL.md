---
name: pace
description: >-
  Controls agent execution velocity and cognitive digest granularity: 'bite' (30-50 lines max, digest-before-diff, step confirmation),
  'standard' (component slices with reviews), or 'fast' (autonomous batch execution). Trigger: /pace.
---

# /pace

Configures the execution speed and cognitive granularity of Conscience OS to match the developer's review velocity.

## Pacing Modes

1. **`bite` (Default — Maximum Cognitive Ownership)**:
   - **Line Budget**: Maximum 30–50 lines of code change per turn.
   - **Digest-Before-Diff**: Requires a 2-sentence rationale before modifying files:
     - *Intent*: Exact small slice being added.
     - *Rationale*: Why this architectural pattern/decision was selected.
   - **Step-and-Acknowledge**: Pauses after each discrete increment for human inspection and guidance.
   - **Best for**: Complex features, multi-file refactors, architecture boundaries, preventing fatigue.

2. **`standard` (Component Velocity)**:
   - **Line Budget**: Single logical unit / file slice (~100 lines).
   - Generates component or module with inline summary and awaits approval before moving to next module.
   - **Best for**: Established patterns, standard CRUD, test suites.

3. **`fast` (Batch Velocity)**:
   - Unrestricted generation budget.
   - Generates full scaffolds in one-shot without mid-turn pauses.
   - **Only engage when explicitly requested by the Director.**
   - **Best for**: Trivial boilerplate, mock data fixtures, rapid prototyping.

## Commands
- `/pace status` — Inspect current velocity setting.
- `/pace bite` — Engage micro-step cognitive pacing.
- `/pace standard` — Set component-level velocity.
- `/pace fast` — Set batch velocity.

## Protocol for the AI Agent
1. When `/pace` is set to `bite`:
   - Enforce strict 30-50 line change limit per step.
   - Always lead code edits with the 2-sentence Digest-Before-Diff block.
   - Pause and yield control to the Director before starting the next file or block.
2. In the State Header:
   - Always reflect the active velocity in the third axis: `[PACE: BITE]`, `[PACE: STANDARD]`, or `[PACE: FAST]`.
