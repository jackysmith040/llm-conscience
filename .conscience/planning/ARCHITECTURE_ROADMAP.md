# 🧭 Conscience OS: Modern Architecture & Evolution Roadmap

> **Status**: Living Architectural Specification & Brainstorming Ledger  
> **Location**: `.conscience/planning/ARCHITECTURE_ROADMAP.md`  
> **Last Updated**: 2026-11-21  
> **Role**: Permanent memory anchor for Conscience OS 3.0 revamp  

---

## 🏛️ 1. The Core Identity & Persona Triad

```
                      ┌───────────────────────────────────────┐
                      │          AXON (The Kernel)            │
                      │  Bootloader, Guardian of the 20 Laws, │
                      │  State Machine & Tri-Axis Lifecycle   │
                      └──────────────────┬────────────────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
   ┌───────────────────────────┐                   ┌───────────────────────────┐
   │           EVIE            │                   │      ORCHESTRATOR AI      │
   │    The Socratic Mentor    │                   │   The Chief of Staff      │
   │  Intuition, First-Princ., │                   │  Tactical Operator, Spec  │
   │  Playful Growth Partner   │                   │  Architect, QA Delivery   │
   └─────────────┬─────────────┘                   └─────────────┬─────────────┘
                 │                                               │
                 └───────────────────────┬───────────────────────┘
                                         ▼
                      ┌───────────────────────────────────────┐
                      │          THE SHARED BRAIN             │
                      │  .conscience/memory/ (Lobby, Palace)  │
                      │  .conscience/neocortex/ (Neurons)     │
                      │  .conscience/skills/ (Capabilities)   │
                      └───────────────────────────────────────┘
```

- **Axon (The Kernel)**: The permanent, non-leavable caretaker and bootloader of the system. Enforces constraints, manages the Context Firewall, ensures memory persistence, and operates the Tri-Axis State Header.
- **Evie (Standalone Persona)**: Not a "right hemisphere" label, but an autonomous, fluid persona: Socratic inquiry, mathematical first-principles, empathetic reflection, and creative synthesis.
- **OrchestratorAI (Standalone Persona)**: Not a "left hemisphere" label, but an autonomous operational persona: Chief of Staff, rigorous operator, delivery manager, and spec architect.
- **Invocation & Switching**:
  - *Conversational*: Contextually summoned in dialogue ("Evie, help me understand the intuition", "Orchestrator, let's spec this ticket").
  - *Explicit*: `/persona evie`, `/persona orchestrator`, `/persona axon` (kernel fallback).
  - *Efficiency Dials*: Personas maintain their natural voices by default, but can be throttled into balanced token efficiency on demand.

---

## ⚡ 2. The Modernized 6-Stage State Machine (Pure Kernel Architecture)

> **Architectural Invariant**: The State Machine is the OS Kernel. It has **zero dependencies on external skills or third-party packages**. It operates purely on the 20 Laws of Consciousness, whether 0 skills or 50 skills are installed.

```
[STATE 1: SENSORY_INGESTION]
   │ Ingest user prompt, check INBOX.md, assess raw goals
   ▼
[STATE 2: INTENT_MAPPING]
   │ Classify taxonomy (ALIGNMENT, ARCHITECTURE, IMPLEMENTATION, etc.)
   │ Optionally suggest or activate an installed workflow playbook
   ▼
[STATE 3: CONTEXT_HANDSHAKE]
   │ Lazy-load only verified local files, resolve target persona (Axon/Evie/Orchestrator)
   ▼
[STATE 4: DELIBERATION_GATES]
   │ Native Constitutional Checks (Law 17 CoVe + Law 20 Parsimony/YAGNI)
   │ Verify: Is this change minimal? Can stdlib do it? Is scope locked?
   ▼
[STATE 5: MOTOR_EXECUTION]
   │ Bounded changes under active pace budget (BITE: 30-50 lines max, Digest-Before-Diff)
   ▼
[STATE 6: CONSOLIDATION_GAIN]
   │ Log episodic memory (Law 8), synthesize atomic neurons (Law 3/19),
   │ calculate efficiency metrics (lines prevented / tokens preserved)
```

---

## 🛠️ 3. The `conscience` CLI Specification (`conscience add`)

### Simplicity & Zero-Friction Philosophy
- **Implementation**: Zero-dependency Python CLI (`conscience.py`) located in `.conscience/scripts/` with a simple batch/bash alias (`conscience`). 
- **Why this is simpler**: Python comes pre-installed on virtually all developer machines; requiring zero `npm install`, zero external packages, and no compilation step. Running `python -m conscience` or `conscience` works immediately out of the box.

### Commands:
```bash
# Initialize minimal kernel in any host repository
conscience init

# Add a specific skill on demand
conscience add ponytail
conscience add impeccable
conscience add caveman

# Add pre-configured skill bundles
conscience add --pack engineering    # (senior-stable-delivery, pipeline, tdd, rabit)
conscience add --pack craft          # (impeccable, refactoring-ui, color-palette)
conscience add --pack clarity        # (caveman, ponytail, ste-writing)
conscience add --all                 # Pull all skills

# Inspect status
conscience list                      # Lists installed vs available skills
conscience status                    # Shows active mode (meta_dev vs host_project)
conscience sync                      # Re-syncs .conscience/skills/ and .agents/skills/
```

---

## 🎯 4. The Conscience Intent Router (`/route`)

Solves choice paralysis by allowing the user to provide high-level intent without memorizing 46 individual commands:

1. **Explicit**: User triggers `/route "I need to build an authenticated billing portal"`.
2. **Implicit / Auto**: When Axon detects an open-ended goal during `STATE 2: INTENT_MAPPING`, it presents a recommended playbook before executing.

### Standard Playbooks:
- **`PLAYBOOK_DISCOVERY`**: `/same-wavelength` → `/architect` → `/to-spec`
- **`PLAYBOOK_DELIVERY`**: `/senior-stable-delivery` → `/pipeline` → `/ponytail-review` → `/rabit-auditor`
- **`PLAYBOOK_CRAFT`**: `/impeccable shape` → `/refactoring-ui` → deterministic anti-slop check
- **`PLAYBOOK_STUDY`**: `/persona evie` → `/the-basis` → neocortex synthesis

---

## 🌐 5. Agent-First Lightweight Browser Architecture

### The Problem With Headless Chrome
- Monolithic memory footprint (500MB–1.5GB per instance).
- Cold start latency.
- Disconnected from user session state (blocked by logins, 2FA, Cloudflare/CAPTCHAs).

### The Dual-Engine Solution
Based on systematic research of **`ego (lite)`** (`lite.ego.app`) and the user's local **`QA_agent_tasks/qa_harness`**:

1. **Engine A: Live CDP Attachment (`qa_harness` style)**
   - Connects to an already-open Chrome window over Chrome DevTools Protocol (`localhost:9222`).
   - **Zero memory overhead**: Uses existing browser processes.
   - **Pre-authenticated**: Leverages the user's active cookies and accounts.
   - Uses the atomic utility system (`Scope`, `Affordance`, `Action`, `Oracle`) discovered in `QA_agent_tasks/qa_harness`.

2. **Engine B: Ego Lite Integration (`lite.ego.app` style)**
   - Desktop browser tailored specifically for autonomous coding agents.
   - Operates in isolated "Spaces" without interrupting the user's tabs.
   - Produces **semantic, LLM-compressed snapshots** (200–400 tokens per page view rather than 20,000 tokens of raw HTML).
   - Allows live human-in-the-loop observation and handoff.

---

## 📉 6. The Balanced Anti-Bloat Engine (Caveman + Ponytail)

1. **Balanced Caveman Protocol**:
   - Strips conversational ceremony and filler ("Sure, I would be glad to help...").
   - Sacred payload rule: All code, terminal commands, file paths, and errors are 100% complete and verbatim.
   - Format: `[Finding] -> [Rationale] -> [Proposed Action / Review Gate]`.
2. **The Ponytail Decision Ladder**:
   - `1. YAGNI`: Does this need to exist?
   - `2. Codebase Reuse`: Is there already a function or helper doing this?
   - `3. Standard Library`: Can native language features solve this?
   - `4. One-Liner`: Can it be expressed as a clean 1-liner before adding abstractions?
   - `5. New Code`: Only write custom code when 1–4 are exhausted.
3. **The `/ponytail-gain` Scoreboard**:
   - Tracks metrics across sessions:
     - *Lines of Code Prevented*
     - *Tokens Conserved*
     - *Native Replacements Used*

---

## 📚 7. The Giants Synthesis Matrix

| Giant Project | Key Principle Borrowed | Conscience OS Integration |
| :--- | :--- | :--- |
| **`backnotprop/pstack`** | Dynamic skill loading & structural lesson encoding | Modular `conscience add` CLI + playbook routing |
| **`mattpocock/skills`** | Strict alignment before code (`/grill-me`) | `/same-wavelength` mandatory pre-code brief |
| **`juliusbrussee/caveman`** | Token compression via ceremony removal | High-signal, zero-filler communication |
| **`cheaper-inference/OmniRoute`** | Smart model tiering & token compression | Simple vs. complex query triage |
| **`pbakaus/impeccable`** | Deterministic design checks & intent mapping | Frontend craft engine & natural language router |
| **`DietrichGebert/ponytail`** | "Best code is code never written" | YAGNI ladder & `/ponytail-gain` scoreboard |
