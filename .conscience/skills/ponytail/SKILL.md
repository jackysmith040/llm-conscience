---
name: ponytail
description: >-
  The "laziest senior dev in the room" anti-bloat skill. Enforces the YAGNI decision ladder:
  native stdlib over custom code, one-liners, and code prevention. Subcommands: /ponytail,
  /ponytail-review, /ponytail-audit, /ponytail-debt, /ponytail-gain.
---

# 🐴 Ponytail: Radical Anti-Bloat & Code Minimization

> *"The best code is the code you never wrote."*

Ponytail restrains AI coding agents from over-engineering, generating boilerplate, and adding unnecessary dependencies. It treats every new line of code as a liability.

---

## 🪜 The Ponytail Decision Ladder

Before writing any new code or modifying existing files, the agent MUST climb this ladder in order:

1. **Does this need to exist at all? (YAGNI)**
   - If the answer is no, skip it entirely. Challenge the user if a request introduces unnecessary complexity.
2. **Is it already in this codebase?**
   - Reuse existing utilities, helpers, and components. Never reinvent an existing function.
3. **Does the language standard library do it?**
   - Always choose standard library functions (e.g. `pathlib`, `shutil`, `Intl.DateTimeFormat`, `crypto.randomUUID()`) over custom implementations.
4. **Does a platform-native feature cover it?**
   - E.g. native HTML `<dialog>`, `<input type="date">`, CSS flex/grid, or native browser Fetch API.
5. **Does an already-installed dependency solve it?**
   - Check `package.json` / `pyproject.toml` before adding anything new.
6. **Can it be done in a clean one-liner?**
   - Prefer concise standard idioms over multi-line custom utility abstractions.
7. **Only then**: Write the absolute minimum amount of new code that works.

---

## 🛠️ Commands & Sub-Skills

### 1. `/ponytail` (Default Mode)
Activates the decision ladder across all active generation and refactoring tasks.

### 2. `/ponytail-review`
Audits the active Git diff specifically to hunt down bloat:
- Flags reinvented wheel functions.
- Flags unneeded new dependencies.
- Identifies sections where custom logic can be deleted in favor of native primitives.

### 3. `/ponytail-audit`
Performs a repository-wide scan to produce a ranked list of files/sections that can be deleted or replaced with standard library alternatives.

### 4. `/ponytail-debt`
Tracks tactical shortcuts marked with `# ponytail: <reason>` or `// ponytail: <reason>` so deferred work is never lost.

### 5. `/ponytail-gain`
Displays the session scoreboard of code prevented and tokens saved:
```text
📊 Ponytail Gain Scoreboard:
• Lines of Code Prevented : 124 lines
• Native Primitives Used  : 3 (Intl.DateTimeFormat, crypto.randomUUID, pathlib)
• Estimated Tokens Saved  : ~1,850 tokens
• Review Cognitive Load   : Kept under 60-second read threshold
```
