---
name: prototype
description: >-
  Build throwaway code to answer a design, state model, or UI question before building for real.
  Strictly temporary — deleted or cleaned up once the decision is locked. Trigger: /prototype.
---

# /prototype

[STATE: MOTOR_EXECUTION | INTENT: IMPLEMENTATION | PACE: FAST]

**Category**: Strategic Exploration — runs before or during `/wayfinder` or `/grill` to resolve high-risk unknowns.

## What
A prototype is **throwaway code that answers a specific question**. Never polish it for production. Delete or discard it as soon as the question is answered.

## Pick a Branch

1. **"Does this logic / state model work?" (Logic Branch)**
   - Build a standalone interactive harness (e.g. single HTML file or node/python test script).
   - Push edge cases and weird state transitions through the logic.
   - Non-developers or agents can run it to verify behavior.

2. **"What should this look like / feel like?" (UI Branch)**
   - Generate quick visual variations on a single screen/route.
   - Keep styles and components isolated and clearly marked.

## The 4 Prototype Rules
1. **Mark as Throwaway**: Start every prototype file with:  
   `/* ⚠️ THROWAWAY PROTOTYPE: Built only to answer: [Question]. Delete before merge. */`
2. **Narrow Scope**: Answer ONLY the question asked. Do not build error handling, auth, or edge polish.
3. **No Production Leaks**: Do not import prototype code into production paths.
4. **Clean Exit**: Once the question is answered, record the decision in `.conscience/memory/DECISION_MAP.md` or the spec, and delete the prototype files.

---

> 🎯 **Question answered?** → Next: delete the prototype artifacts and resume the Main Flow with `/grill` or `/to-spec`.
