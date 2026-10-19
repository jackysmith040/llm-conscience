---
name: i-am-impeccable
description: >-
  Natural-language router and alias for the Impeccable design engine (v4.6.0).
  Infers design intent and routes to all 24 Impeccable craft commands. Trigger: /impeccable, /i_am_impeccable.
---

# /i-am-impeccable (Alias for /impeccable)

[STATE: MOTOR_EXECUTION | INTENT: CRAFT_POLISH | PACE: STANDARD]

`/i-am-impeccable` is consolidated with the full **Impeccable Design Engine** (`/impeccable`).

When triggered:
1. Ingest the user's design problem or UI description.
2. If ambiguous, present up to 3 plain-language choices with ELI5 explanations mapped to Impeccable commands (e.g. `critique`, `polish`, `bolder`, `typeset`, `distill`, `harden`).
3. Once confirmed or when an explicit command is requested, immediately delegate to `/impeccable`:
   `→ see .conscience/skills/impeccable/SKILL.md`
