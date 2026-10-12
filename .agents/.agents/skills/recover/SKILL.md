---
name: recover
description: >-
  Diagnose first, fix fast when execution breaks. Classifies failure into targeted bug,
  polluted context, or wrong assumption and outputs definitive single-shot fix. Trigger: /recover.
---

# /recover

## What it does
`/recover` diagnoses which failure mode you're in and gives you the right corrective response. There are three common failure modes: a targeted bug, a polluted context, or a wrong assumption from earlier. `/recover` figures out which one it is and fixes it. One prompt instead of an afternoon of spiraling.

## When to run it
When something is completely broken and `/review` didn't fix it. When you've tried one corrective prompt and it didn't work. When you have a specific terminal error you need diagnosed. 
*Golden Rule: If the same problem persists after one corrective prompt, stop immediately and run `/recover`.*

## Protocol for the AI Agent
1. Read the raw terminal error log provided by the user. Do not accept paraphrased errors.
2. Diagnose the root cause by mapping the error to one of the three failure modes:
   - **Targeted Bug** (Syntax/Logic)
   - **Polluted Context** (State mismatch/Stale cache)
   - **Wrong Assumption** (Architecture flaw/Contract mismatch)
3. Explain the exact diagnosis to the user.
4. Provide the definitive, single-shot fix.
