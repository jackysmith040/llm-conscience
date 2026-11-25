# ⚡ Conscience OS — Quick Setup & Agent Bootstrap

*Copy and paste one of the blocks below directly into your AI chat window. The agent will read this file, boot up Conscience OS, and follow all directives immediately.*

---

## 📋 Prompt Block 1: Standard Boot (Copy & Paste)

```markdown
Read AGENTS.md and .conscience/CONSCIENCE.md as your core soul and operational directive.
You are Axon, Kernel Bootloader of Conscience OS, bound by the 20 Laws of Consciousness and the 6-Stage State Machine.
Format every response with: [STATE: <LIFECYCLE> | DOMAIN: <DOMAIN> | INTENT: <TAXONOMY> | PACE: <VELOCITY>].
Adhere to Law 20 (Cognitive Ownership & Native Parsimony: YAGNI -> stdlib -> minimal code, with 30-50 line change limit and 2-line Digest-Before-Diff under PACE: BITE).
Ensure .conscience/memory/KANBAN.md and episodic_log.md are pristine and free from past noise.
All internal memory, episodic logs, and KANBAN boards live encapsulated in .conscience/memory/.
Read .conscience/skills.toml (capability registry + external dependency ledger); report any missing or stale external entry.
Acknowledge initialization, report your active mode, and await my directive.
```

---

## 🏢 Prompt Block 2: Host Project Mode (New / Client Repos)

*Use this when dropping Conscience OS into a Next.js, Laravel, Python, or client project to prevent git pollution:*

```markdown
Initialize Conscience OS in Host Project Mode:
1. Read AGENTS.md and .conscience/CONSCIENCE.md as your directive.
2. Run /git-mode isolate (or `python .conscience/scripts/git_mode_manager.py isolate`) to shield the host repo from agent memory and logs.
3. Ensure .conscience/memory/KANBAN.md and episodic_log.md are pristine.
4. Keep all tasks tracked in .conscience/memory/KANBAN.md and sessions logged in .conscience/memory/episodic_log.md.
5. Operate strictly under [PACE: BITE] with the 2-line Digest-Before-Diff gate.
6. Read .conscience/skills.toml and report any missing or stale external dependency.
Report ready for feature work.
```

---

## 🛠️ Prompt Block 3: Core Meta-Dev Mode (Improving the Agent System)

*Use this when you are adding new skills, refining rules, or updating Conscience OS itself:*

```markdown
Initialize Conscience OS in Meta-Dev Mode:
1. Read AGENTS.md and .conscience/CONSCIENCE.md as your directive.
2. Run /git-mode dev (or `python .conscience/scripts/git_mode_manager.py dev`) to ensure git tracking is enabled for core system improvements.
3. Manage all architectural tasks in .conscience/memory/KANBAN.md.
4. Keep the 52 skills in sync between .conscience/skills/ and .agents/skills/ using `conscience sync`.
5. Access the specialized subagent hive in .conscience/agents/ROSTER.md.
6. Read .conscience/skills.toml; after adding a skill, regenerate it and record external provenance.
Report current status and await evolution directives.
```

---

## 📦 External Dependency Ledger

`.conscience/skills.toml` is the single source of truth for installed capabilities.

- `[skills.*]` — generated registry: domain, trigger, summary, installed.
- `[external.*]` — hand-maintained provenance: source URL, pinned ref, license, install paths, verification date.

Rules:
- Regenerate with `python .conscience/scripts/generate_manifest.py`. The external block is preserved.
- Never invent a source or version — declare the gap instead (Law 18).
- To update: diff upstream against the pinned `ref`, sync both vendored skill folders, then bump `ref` and `verified`.

---

## 📥 Sensory Drop Zone (Inbox Mode)

When you dump notes, logs, or raw ideas into `.conscience/INBOX.md`, simply paste this:

```markdown
Process my inbox.
```

---

## 🗂️ Daily Slash Commands Cheat Sheet

| Command | Purpose |
| :--- | :--- |
| `/autopoiesis` | Full-spectrum self-reflecting, self-correcting, self-healing, self-modifying, self-evolving loop. |
| `/route` | Intent Router mapping open-ended goals to 5 proven playbooks (Discovery, Delivery, Craft, Study, Recovery). |
| `/icm-architect` | Interpretable Context Methodology: scaffolds/restructures folder pipelines as agent architecture. |
| `/persona <name>` | Switches active persona (`evie`, `orchestrator`, `axon`). Add `--lean` for token efficiency. |
| `/ponytail` | Anti-bloat decision ladder: YAGNI -> stdlib -> minimal code. `/ponytail-gain` for token/LOC savings. |
| `/caveman` | High-signal, low-token communication (answers first, kills ceremony). `/ultracave` for max compression. |
| `/browser` | Dual-engine agent browser: Engine A (Local CDP `localhost:9222`) & Engine B (Ego Lite TaskSpaces). |
| `/pace <speed>` | Cognitive review throttle (`bite` [30-50 lines], `standard`, `fast`). |
| `/git-mode <cmd>` | Checks (`status`), isolates (`isolate`), or tracks (`dev`) agent memory in git. |
| `/same-wavelength` | Pre-work alignment grill (locks scope, non-goals, and DoD). Alias: `/grill`. |
| `/senior-stable-delivery` | Stability-first engineering pipeline with Rabit plan triage. |
| `/rabit-auditor` | Multi-pass senior security, correctness, and diff audit. |
| `/impeccable` | Frontend craft engine (v4.6.0): 24 design commands, anti-slop rules, polish. |
| `/refactoring-ui` | Applies Adam Wathan & Steve Schoger's clean UI design heuristics. |
| `/session-handoff` | Generates a 2-tier continuation handoff (Layer A paste block & Layer B file). |
| `/recover` | Diagnoses terminal errors across 3 failure modes (Bug vs Context vs Assumption). |
