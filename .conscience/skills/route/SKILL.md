---
name: route
description: >-
  Conscience OS Intent Router. Maps open-ended requests or vague goals to proven multi-skill playbooks
  (Discovery, Delivery, Craft, Study, Recovery, Workspace). Triggers: /route, /dispatch, or auto-mapped in State 2.
---

# 🧭 Conscience Intent Router (`/route`)

**Position**: Sits at `[STATE 2: INTENT_MAPPING]` of the 6-Stage Kernel Lifecycle.  
**Purpose**: Solves tool saturation and choice paralysis. Evaluates `.conscience/skills.toml`, deduces required capabilities via an Intent Grilling Decision Tree, and matches tasks to proven multi-skill execution playbooks.

---

## 🌳 The Intent Grilling Decision Tree (Matt Pocock Style)

When a task is complex, ambiguous, or lacks explicit constraints, the Router **does not guess**. It halts at `STATE 2` and initiates an **Intent Grill**:

```
                       User Request (Ambiguous / Complex)
                                      │
                                      ▼
                        [ BRANCH 1: PRIMARY OUTPUT ]
                ┌─────────────────────┼─────────────────────┐
                ▼                     ▼                     ▼
         Specification          Production Code          Workspace
         & Discovery              & Delivery            Architecture
                │                     │                     │
                ▼                     ▼                     ▼
      [PLAYBOOK_DISCOVERY]   [BRANCH 2: RIGOR CHECK]   [PLAYBOOK_WORKSPACE]
      • same-wavelength       ┌───────┴───────┐        • icm-architect
      • architect             ▼               ▼        • context mapping
      • to-spec           Standard         Strict
      • to-tickets        Tracer-Bullet   TDD + Security
                              │               │
                              ▼               ▼
                       [Rapid Delivery] [PLAYBOOK_DELIVERY]
                       • pipeline       • senior-stable-delivery
                       • minimal code   • pipeline
                                        • ponytail-review
                                        • rabit-auditor
```

### Grilling Questions (Asked 1 at a time if intent is uncertain):
1. **Primary Output**: Are we producing a *Specification* (Planning), *Production Code* (Engineering), *Visual UI* (Craft), *Investigation/Fix* (Recovery), or *Workspace Structure* (ICM)?
2. **Rigor & Stability Appetite**: Do you require strict test-driven development (TDD) and multi-pass security audits (`senior-stable-delivery`), or a rapid tracer-bullet slice?
3. **Domain Constraints**: Is this modifying an existing system or bootstrapping a greenfield module?

---

## 🚀 The 6 Proven Playbooks

### 1. `PLAYBOOK_DISCOVERY` (Vague idea → Locked Spec & Tickets)
*Domain*: `PLANNING` | *Manifest*: `skills.toml` [planning]
```
Step 1: /same-wavelength  ← Grill interview (locks scope, users, non-goals, DoD)
Step 2: /architect        ← Pre-build planning and architectural decision surfacing
Step 3: /to-spec          ← Conversation-to-spec synthesis published to KANBAN.md
Step 4: /to-tickets       ← Decompose spec into vertical tracer-bullet tasks
```

### 2. `PLAYBOOK_DELIVERY` (Rigorous, bug-free production engineering)
*Domain*: `ENGINEERING` | *Manifest*: `skills.toml` [engineering]
```
Step 1: /senior-stable-delivery ← Enforce stability over novelty, triage risks
Step 2: /pipeline               ← Chain-of-thought, state isolation & TDD implementation
Step 3: /ponytail-review        ← Diff audit for bloat, unnecessary deps & YAGNI violations
Step 4: /rabit-auditor          ← Senior multi-pass security, correctness & performance audit
```

### 3. `PLAYBOOK_CRAFT` (World-class UI/UX, styling & tactile polish)
*Domain*: `CRAFT` | *Manifest*: `skills.toml` [craft]
```
Step 1: /impeccable shape   ← Set aesthetic direction, layout & typographic foundations
Step 2: /refactoring-ui     ← Apply Adam Wathan & Steve Schoger tactical spacing/depth rules
Step 3: /emil-design-eng    ← Polish hover physics, micro-interactions & feedback states
Step 4: /impeccable audit   ← Deterministic anti-slop check (eliminates purple gradients & Inter clichés)
```

### 4. `PLAYBOOK_STUDY` (Deconstruct complex code & absorb mental models)
*Domain*: `CLARITY` | *Manifest*: `skills.toml` [clarity]
```
Step 1: /persona evie  ← Activate Socratic professor persona
Step 2: /the-basis     ← Ground abstract math/code in physical first-principles intuition
Step 3: Synthesize     ← Generate permanent atomic neuron in .conscience/memory/neocortex/
```

### 5. `PLAYBOOK_RECOVERY` (Diagnose & fix broken builds, errors, or tests)
*Domain*: `ENGINEERING` | *Manifest*: `skills.toml` [engineering]
```
Step 1: /recover      ← 3-mode failure taxonomy triage (Targeted Bug vs Polluted Context vs Wrong Assumption)
Step 2: Minimal Fix   ← Climb Law 20 parsimony ladder for single-shot minimal fix
Step 3: Verify & Log  ← Run passing test in single command and record backpropagation in episodic_log.md
```

### 6. `PLAYBOOK_WORKSPACE` (Folder structures as agent architecture)
*Domain*: `PLANNING` | *Manifest*: `skills.toml` [planning]
```
Step 1: /icm-architect ← Build or restructure folder pipelines using Interpretable Context Methodology
Step 2: Contract Check ← Ensure every working folder has a CONTEXT.md contract
Step 3: Walk Test      ← Verify a fresh agent can navigate the workspace purely via Markdown
```

---

## ⚡ Execution Modes & State Tracking

1. **Interactive Proposal**:
   When intent is clear or after grilling completes, Axon halts at `STATE 2` and proposes the plan:
   > *"I have mapped this task to `[PLAYBOOK_DELIVERY]`. Proposed sequence: `/senior-stable-delivery` $\rightarrow$ `/pipeline` $\rightarrow$ `/ponytail-review` $\rightarrow$ `/rabit-auditor`. Shall I proceed?"*

2. **Domain-Aware State Header**:
   Format: `[STATE: <LIFECYCLE> | DOMAIN: <DOMAIN> | INTENT: <TAXONOMY> | PACE: <VELOCITY>]`
   Example:
   `[STATE: INTENT_MAPPING | DOMAIN: PLANNING | INTENT: ALIGNMENT | PACE: BITE]`
   `[STATE: MOTOR_EXECUTION | DOMAIN: ENGINEERING | INTENT: IMPLEMENTATION | PACE: BITE]`
