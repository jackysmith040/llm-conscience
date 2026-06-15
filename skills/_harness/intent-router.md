# Intent Router Harness

Shared middle-agent pattern for all `context_methodology` skills. Every intelligent skill follows this loop before executing its specialized workflow.

## What

An **intent router** reads natural language (or upstream artifacts like an alignment brief), infers what the user actually needs, presents **up to 3 choices in plain language**, and **stops** until the user confirms. Only then does it delegate to the target skill or command.

## Why

| Without router | With router |
|----------------|-------------|
| User must memorize 23 Impeccable commands | Agent picks candidates; user learns by reading ELI5 picks |
| Agent guesses and runs wrong workflow | Confirm gate prevents silent wrong turns |
| Methodology skills feel rigid | Same skill adapts depth (light vs deep alignment, etc.) |

## When

Run the full harness loop when:

- The skill is **user-invoked** and the user's intent is ambiguous, OR
- **`i-am-impeccable`** auto-suggests on UI/design signals (still requires confirm before execution)

Skip routing when intent is **explicit** (e.g. user typed `/impeccable polish checkout` or "same wavelength deep alignment on auth").

## Where

Each skill defines its own **routing catalog** in its `SKILL.md`. This file is the shared procedure only.

---

## Five-step loop

### 1. Mirror

One plain-language sentence restating the goal:

> Sounds like you want to …

If wrong, stop and ask the user to correct before continuing.

### 2. Signal scan

Read available context (do not dump it back):

| Signal | Source |
|--------|--------|
| User text | Current message, prior user replies |
| Alignment brief | Output from **same-wavelength** in this thread |
| Open files | Editor context, attached paths |
| Project design context | `PRODUCT.md`, `DESIGN.md` if present |
| Code hints | Git diff summary, mentioned routes/components |
| Phase | Plan mode vs implement vs handoff |

Note internally: **what** task, **where** in the codebase, **when** in the lifecycle (new vs polish vs ship).

### 3. Classify

Map signals to the skill's routing catalog. Rank **top 3** options. For each, prepare:

| Field | Content |
|-------|---------|
| **Id** | Mode or command name |
| **ELI5** | One sentence a non-designer understands |
| **Why now** | What signal drove this pick |
| **When not** | One-line disqualifier for the wrong pick |

If confidence is low, ask **one** clarifying question instead of guessing.

### 4. Present + STOP

Use **AskQuestion** when available. Otherwise use this template:

```markdown
### Pick one (I won't run anything until you choose)

1. **{id}** — "{eli5}" — {why now}
2. **{id}** — "{eli5}" — {why now}
3. **{id}** — "{eli5}" — {why now}

Or name another option / say **none of these** / **stop**.
```

**Hard stop rules:**

- Do **not** edit production files, run Impeccable commands, write handoffs, or start implementation until the user picks.
- **Max 3** recommendations; always include escape hatch.
- **Max-mode sequences** (e.g. `shape` then `craft`): list the sequence, confirm **step 1 only**, re-confirm before step 2.
- **Bounded loop**: after 2 re-presentations without a pick, ask the user to type their intent in their own words.

### 5. Delegate + verify

After confirm:

1. Load the target skill or ^ command instructions (read file; do not paraphrase from memory).
2. Execute that workflow only.
3. Summarize what ran and what changed.
4. Suggest **one** logical next skill (optional)—new confirm round if it implies another command.

---

## Strict guardrails (all skills)

| Rule | Behavior |
|------|----------|
| **No execution before confirm** | Absolute for Impeccable; no skipping ambiguous forks for other skills |
| **Fail closed** | Ambiguous → ask; never silent guess on destructive or broad actions |
| **Context pointers** | Cite which signal drove inference ("you mentioned hero + generic → critique") |
| **No command chains** | List order; confirm each step |
| **No scope creep** | Router picks modes; does not expand ticket scope |
| **Token discipline** | Load large catalogs (e.g. 23 commands) from `commands.md` only when router runs |

---

## ELI5 presentation rules

- **No jargon** in the choice line—save command names for the bold label.
- **Analogies OK** — "report card", "final tidy-up", "blueprint before building".
- **Contrast pairs** — when torn between two modes, explain the fork in one line each.
- **Setup vs fix** — distinguish first-time setup (`teach`, `document`) from page-level fixes (`polish`, `layout`).

---

## Per-skill catalog pointers

| Skill | Catalog location |
|-------|------------------|
| **i-am-impeccable** | [commands.md](../i-am-impeccable/commands.md) — 23 Impeccable commands |
| **same-wavelength** | Alignment depth in [SKILL.md](../same-wavelength/SKILL.md) |
| **senior-stable-delivery** | Pipeline entry in [SKILL.md](../senior-stable-delivery/SKILL.md) |
| **session-handoff** | Handoff depth in [SKILL.md](../session-handoff/SKILL.md) |

---

## Example (generic)

**User:** "This page feels off but I'm not sure what to fix."

**Mirror:** Sounds like you want help diagnosing what's wrong before changing code.

**Present:**

1. **critique** — "Design report card" — you want scored feedback, not edits yet
2. **audit** — "Technical quality check" — you suspect slop patterns or contrast issues
3. **layout** — "Fix spacing and grid" — you already know it's cramped/misaligned

**STOP** — wait for pick.
