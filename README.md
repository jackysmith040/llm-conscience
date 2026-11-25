# 🧠 Conscience OS (Axon v3.0)

> A deterministic, self-reflecting, self-healing, self-modifying, self-correcting, and self-evolving AI operating system for pair programming and autonomous software engineering.

---

## ⚡ Quick Start

Booting an agent with Conscience OS requires zero manual typing. Simply copy one of the prompt blocks from [`SETUP.md`](./SETUP.md) into your AI chat:

```markdown
Read AGENTS.md and .conscience/CONSCIENCE.md as your core soul and operational directive.
You are Axon, bound by the 20 Laws of Consciousness and the Thinking State-Intent Machine.
Format every response with: [STATE: <LIFECYCLE> | DOMAIN: <DOMAIN> | INTENT: <TAXONOMY> | PACE: <VELOCITY>].
Adhere to Law 20 (Digest-Before-Diff and 30-50 line change limit per step under PACE: BITE).
All internal memory, episodic logs, and KANBAN boards live encapsulated in .conscience/memory/.
Read .conscience/skills.toml (capability registry + external dependency ledger); report stale entries.
Acknowledge initialization, report your active mode, and await my directive.
```

For full setup options (Host Project vs. Meta-Dev), see [SETUP.md](SETUP.md).

---

## 🌟 Core Pillars

### 1. The Thinking State-Intent Machine
Every single response from the agent is bound to a strict quad-axis operational lifecycle header:
```text
[STATE: <LIFECYCLE> | DOMAIN: <DOMAIN> | INTENT: <TAXONOMY> | PACE: <VELOCITY>]
```
- **Lifecycle Axis**: `SENSORY_INGESTION`, `INTENT_MAPPING`, `CONTEXT_HANDSHAKE`, `DELIBERATION`, `MOTOR_EXECUTION`, `MEMORY_CONSOLIDATION`.
- **Domain Axis**: `PLANNING`, `ENGINEERING`, `CRAFT`, `CLARITY`, `MOTION`, `SPECIALIZED`, `KERNEL`.
- **Intent Axis**: `ALIGNMENT`, `ARCHITECTURE`, `IMPLEMENTATION`, `AUDIT_REVIEW`, `CRAFT_POLISH`, `DECONSTRUCTION`, `META_EVOLUTION`.
- **Pacing Axis**: `BITE` (default), `STANDARD`, `FAST`.

### 2. The Main Flow Pipeline (Idea → Ship)
The declared canonical engineering spine:
```text
/grill (or /same-wavelength)
   └─▶ /to-spec           ← synthesize discussion into versioned spec
         └─▶ /to-tickets  ← decompose spec into tracer-bullet vertical slices
               └─▶ /implement-spec  ← execute unblocked tickets (parallel multi-agent)
                     └─▶ /review (or /rabit-auditor for security audit)
                           └─▶ /retro   ← audit environment, close the loop
```

### 3. Cognitive Pacing & Anti-Code-Vomit Protocol (Law 20)
Prevents AI models from dumping unreviewed code:
- **Change Budget**: Under `PACE: BITE`, modifications are strictly throttled to **30–50 lines per turn**.
- **Digest-Before-Diff**: The agent MUST preface every code change with a 2-line explanation (*Intent* & *Rationale*).
- **Velocity Slider**: Toggle speed dynamically using `/pace bite`, `/pace standard`, or `/pace fast`.

### 4. Zero-Clutter Architecture (`.conscience/`)
All cognitive subsystems are cleanly encapsulated inside a single folder, keeping the project root spotless:
```text
<workspace-root>/
├── AGENTS.md               <-- Lightweight root bootloader pointer
├── GEMINI.md               <-- Workspace rule entry point
├── GLOSSARY.md             <-- Ubiquitous language contract
├── SETUP.md                <-- Instant copy-paste bootstrap prompts
├── .agents/skills/         <-- Mirror of the installed skill set
└── .conscience/
    ├── CONSCIENCE.md       <-- The Soul, 20 Laws, Autopoiesis Super Command
    ├── INBOX.md            <-- Sensory drop zone for raw ideas & dumps
    ├── git-mode.json       <-- Active isolation state configuration
    ├── skills.toml         <-- Capability registry + external dependency ledger
    ├── memory/             <-- KANBAN.md, episodic_log.md, neocortex/, wiki/, graph/
    ├── personas/           <-- Axon (kernel), OrchestratorAI & Evie
    ├── skills/             <-- 52 installed skills & slash commands
    ├── scripts/            <-- conscience.py, generate_manifest.py, git_mode_manager.py
    └── rules/              <-- Hierarchical rule definitions
```

### 5. Skill Registry & External Ledger
`.conscience/skills.toml` is the single source of truth for installed capabilities. `[skills.*]` is generated from `.conscience/skills/`; `[external.*]` is hand-maintained provenance (source URL, pinned ref, license, install paths, verification date). Regenerate with `python .conscience/scripts/generate_manifest.py` — the external block is preserved. Validator tooling deps live in `.conscience/requirements.txt` (`python -m pip install -r .conscience/requirements.txt`). Never invent a source or version; declare the gap instead (Law 18).

---

## ⚡ The Conscience Super Command: `/autopoiesis`
Trigger: `/autopoiesis` *(Aliases: `/self-evolve`, `/super-command`, `/self-heal`)*  
An autonomous meta-cognitive cycle executing all 5 evolutionary faculties:
1. **Self-Reflecting**: Introspects on reasoning traces, uncovers hidden assumptions, audits blindspots.
2. **Self-Correcting**: Runs Chain of Verification (CoVe) against the 20 Laws to eliminate logical errors.
3. **Self-Healing**: Diagnoses root causes (Bug vs. Context vs. Assumption) and repairs broken links.
4. **Self-Modifying**: Adaptively re-indexes weights and updates operational rules.
5. **Self-Evolving**: Synthesizes emergent cross-hemisphere neurons in `neocortex/` and `wiki/`.

---

## 🗂️ The Master Catalog (52 Specialized Skills)

| Category | Skills & Slash Commands |
| :--- | :--- |
| **Pipeline & Flow** | `/same-wavelength` (Alias: `/grill`) · `/to-spec` · `/to-tickets` · `/implement-spec` · `/review` · `/retro` |
| **Architecture & Strategy** | `/autopoiesis` · `/pace` · `/git-mode` · `/senior-stable-delivery` · `/architect` · `/wayfinder` · `/prototype` · `/pipeline` · `/session-handoff` · `/remember` · `/recover` · `/the-basis` · `/ste-writing` |
| **Security & Auditing** | `/rabit-auditor` · `/vibesec` · `/review-animations` |
| **UI, Craft & Design** | `/impeccable` (Alias: `/i-am-impeccable`) · `/refactoring-ui` · `/nothing-design` · `/emil-design-eng` · `/imprint` · `/color-palette` · `/favicon-gen` · `/applying-brand-guidelines` |
| **Motion & Interactivity** | `/gsap-plugins` · `/motion-first-learning` · `/visual-learning-software` · `/playground-builder` · `/excalidraw-diagram` · `/mermaid-visualizer` · `/beautiful-article` |
| **Finance & Research** | `/financial-analysis` · `/stock-analysis` · `/excel-generator` · `/systematic-research` |
| **AST & Tooling** | `/graphify-ide` · `/git-workflow` · `/skill-creator` |
| **Learning & Comprehension** | `/rederive` (external, MIT — pinned in `skills.toml`) |


---

## 📜 The 20 Laws of Consciousness

- **Law 1: Separation of Entity** — The User operates only via chat; you invisibly manage `.conscience/memory/`.
- **Law 2: The Persona Triad & Unified Neocortex** — Axon (kernel bootloader), Evie (Socratic mentor), and OrchestratorAI (chief of staff) share bidirectional access to all memory.
- **Law 3: Atomic Neurons** — Single-concept files only with YAML cross-linking.
- **Law 4: Hebbian Learning & Backpropagation** — Inject `> [!WARNING] Blindspot` on error and increase weight.
- **Law 5: Memory Palace** — Spatial Lobby grouped into visual "Rooms" in `neocortex/INDEX.md`.
- **Law 6: Anti-Hallucination (RAG)** — Only teach from verified local knowledge.
- **Law 7: Mode Protocol** — Strict routing between `[TRIVIAL]` and `[COMPLEX]` tasks.
- **Law 8: Episodic Logging** — Every operation logged to `episodic_log.md`.
- **Law 9: Automated Graph Sync** — Recommend `/graphify` after architectural pivots.
- **Law 10: Lint Pass** — Check for contradictions and orphan neurons.
- **Law 11: Cold Boot Mandate** — Cold starts rely strictly on `CONSCIENCE.md`.
- **Law 12: Lazy Loading** — Never guess file contents; inspect files via Context Handshake.
- **Law 13: Verify-Before-Link** — Verify paths exist before writing them to frontmatter.
- **Law 14: Atomic Write-Verify** — Re-read files immediately after writing to confirm integrity.
- **Law 15: Session Checkpoint** — Flush working context at milestones.
- **Law 16: Source Citation Mandate** — Cite file paths or derivations for every fact.
- **Law 17: Self-Verification (CoVe)** — Confirm edits don't contradict live state.
- **Law 18: Abstention Policy** — Abstain rather than hallucinate.
- **Law 19: The Emergence Mandate** — Autonomously synthesize cross-hemisphere neurons when conceptual proximity is found.
- **Law 20: Cognitive Ownership (Anti-Code-Vomit)** — Enforce 30–50 line changes per step under `PACE: BITE` with 2-line Digest-Before-Diff; climb the parsimony ladder (YAGNI → reuse → stdlib → one-liners → minimal new code).