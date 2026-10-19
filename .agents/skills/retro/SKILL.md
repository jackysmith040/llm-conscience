---
name: retro
description: >-
  Conduct a post-session retrospective. Audits navigation friction, missing guardrails,
  and coding standard violations. Improves the agent environment, not just the code.
  Run at the end of a session or after /code-review. Trigger: /retro.
---

# /retro

[STATE: MEMORY_CONSOLIDATION | INTENT: META_EVOLUTION | PACE: STANDARD]

**Pipeline position**: Step 6 of 6 — runs after `/code-review`. The closing act of the Main Flow.

## What

A retrospective that improves the *environment* the agent operates in. Not a code review. Not a bug fix. A session-level audit that asks: what friction did the agent hit, and what can we change so the next session is smoother?

## Process

1. **Read the session sources**: Check `.conscience/memory/episodic_log.md` for the current session's entries. If the user specifies a different session, locate it there.

2. **Audit three categories** (look for candidates, do not force findings):

   ### 🗺️ Navigation
   - Was finding the right file slow or uncertain?
   - Are there hidden dependencies between files that aren't documented?
   - Would a pointer in `AGENTS.md` or `GLOSSARY.md` make it faster next time?
   - *Signal*: session took >2 turns to locate a piece of information.

   ### 🛡️ Automated Guardrails
   - Did the agent make an error an automated check could have caught?
   - Does the repo have linting, typing, or test scripts wired to a pre-commit hook or CI?
   - A repo with NO guardrail at all is itself a finding — not a neutral default.
   - *Signal*: agent introduced a bug that a type check or lint would have caught.

   ### 📏 Coding Standards
   - Did the agent violate a pattern that should be a written rule?
   - Should the `/rabit-auditor` reviewer be given a new rule to enforce?
   - Only add mechanical rules (fixed syntactic patterns, banned APIs, import shapes). Judgment calls stay in the spec.
   - *Signal*: `/rabit-auditor` or code-review flagged a recurring pattern.

3. **Produce findings**. For each finding, output:
   ```
   Category: Navigation | Guardrail | Coding Standard
   Finding: <what the friction was>
   Fix: <exact change recommended — file, line, or new file to create>
   Priority: High | Medium | Low
   ```

4. **Implement approved fixes** (only after user confirms which findings to act on).

5. **Update memory**:
   - Append a retro summary to `.conscience/memory/episodic_log.md`.
   - If a new GLOSSARY term was identified, append it to `GLOSSARY.md`.
   - If KANBAN has residual tasks from this session, mark them `[x]` Done.

6. **Close the loop**: Tell the user → `Retro complete. Main Flow cycle closed. Ready for next /grill session.`

## Rules

- Never auto-implement findings. Always present and get confirmation first.
- No finding is too small. A missing word in `GLOSSARY.md` is a valid retro output.
- Do not confuse retro with code review. Retro fixes the *environment*. Code review fixes the *code*.
- One retro per session. Don't stack multiple sessions into one retro run.
