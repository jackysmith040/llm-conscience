---
name: same-wavelength
description: >-
  Pre-work alignment interview: lock requirements, architecture tradeoffs, non-goals, risk appetite,
  and definition of done before coding. User-invoked only. Trigger: /same-wavelength, same wavelength.
---

# /same-wavelength

## What
A structured alignment session before implementation—like a rigorous "grill me," but oriented toward shipping safely, not debate for its own sake. Output is written locks: scope, non-goals, decisions, open questions, and definition of done.

## Session Flow
1. **Mirror (1 paragraph)**: Restate the user's goal in plain language. Ask: *"Is this the problem we're solving?"*
2. **Grill blocks**:
   - Scope: In / out; MVP vs later; single ticket boundary.
   - Users & Context: Who, constraints (mobile, public, admin).
   - Architecture: Data flow, boundaries, coupling restrictions.
   - Failure & Security: AuthZ, abuse, invalid inputs, fail-open vs closed.
   - Done: Verifiable checklist, tests, smoke steps.
   - Persona: Stability vs speed, creep policy.
3. **Challenge pass**: Push on hidden assumptions, duplicate systems, creep risks.
4. **Alignment Brief**: Output clean brief summarizing Locked IN, Locked OUT, Decisions table, and DoD.
5. **Explicit Consent**: Do not write production code until user confirms the brief.
