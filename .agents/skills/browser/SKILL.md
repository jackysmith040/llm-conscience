---
name: browser
description: >-
  Lightweight, agent-first browser skill. Replaces heavy headless Chrome with dual-engine execution:
  Engine A (Local CDP attachment to open Chrome) and Engine B (Ego Lite isolated workspaces with semantic snapshots).
---

# 🌐 Conscience Agent Browser (`/browser`)

> **Zero-Bloat, Agent-First Web Automation & Inspection**

Traditional headless Chrome is too heavy (500MB–1.5GB RAM) and dumps noisy HTML (20,000+ tokens per view). The Conscience Browser skill introduces a **dual-engine architecture** designed for agent speed, pre-authentication, and token efficiency.

---

## 🚀 The Dual-Engine Architecture

### Engine A: Local CDP Attachment (Zero Extra RAM)
*Inspired by `QA_agent_tasks/qa_harness` on your local machine:*
- **How it works**: Attaches directly to an already-open Chrome window using the Chrome DevTools Protocol (`localhost:9222`).
- **RAM Footprint**: **0 MB additional memory** (reuses your existing browser process).
- **Authentication**: Seamless. You are already logged in to your dashboards, GitHub, Jira, and staging apps.
- **Composable Utility Model**: Uses 4 orthogonal interaction primitives:
  - **Scope**: Target containers (`modal`, `table`, `form`, `card`, `main`).
  - **Affordance**: Semantic intents (`submit`, `cancel`, `input:Search`, `select:Combobox`).
  - **Action**: Tactile physics interactions with auto-scroll and self-healing pointers.
  - **Oracle**: Universal invariants (`no-crash`, `feedback`, `boundary`).

### Engine B: Ego Lite Integration (`lite.ego.app`)
*Built specifically for autonomous AI coding agents:*
- **How it works**: Communicates with the desktop Ego Lite client via `ego-browser` using PowerShell here-strings.
- **Isolated Spaces**: Tasks run in their own sandboxed `TaskSpace` inside Ego Lite—your active tabs and windows are never hijacked.
- **Semantic Snapshots**: Generates clean, LLM-optimized semantic page views (**200–400 tokens**) via `snapshotText()` instead of massive raw HTML.
- **Shared Profile**: Imports your Chrome cookies, logins, and bookmarks during onboarding.

---

## ⚡ Usage & Execution Patterns

### 1. Launching or Checking Browser Status
```bash
# Check available engines and browser connectivity
/browser status
```

### 2. Engine A: Live CDP Execution (Quick Automation)
Launch Chrome with remote debugging enabled:
```powershell
# Windows launch command
chrome.exe --remote-debugging-port=9222
```
Agent runs actions against `http://localhost:9222` to inspect elements, verify UI state, or run smoke tests without spawning extra processes.

### 3. Engine B: Ego Lite Execution (PowerShell Heredoc)
```powershell
ego-browser nodejs <<'EOF'
const task = await useOrCreateTaskSpace('audit landing page');
cliLog('Task space: ' + task.id);
await openOrReuseTab('https://localhost:3000', { wait: true, timeout: 20 });
const snapshot = await snapshotText();
cliLog(snapshot);
EOF
```

---

## 🎯 Engine Auto-Selection Heuristic
1. If `localhost:9222` responds $\rightarrow$ Engine A (Local CDP) is selected for zero-overhead live pairing.
2. If `ego-browser` is found in PATH $\rightarrow$ Engine B (Ego Lite) is selected for background task spaces.
3. Explicit overrides supported via `--cdp` or `--ego` flags.
