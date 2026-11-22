---
name: route
description: >-
  Conscience OS Intent Router. Maps open-ended requests or vague goals to proven multi-skill playbooks
  (Discovery, Delivery, Craft, Study, Recovery). Triggers: /route, /dispatch, or auto-mapped in State 2.
---

# 🧭 Conscience Intent Router (`/route`)

**Position**: Sits at `[STATE 2: INTENT_MAPPING]` of the 6-Stage Kernel Lifecycle.  
**Purpose**: Solves choice paralysis. Instead of manually remembering 46+ specialized commands, you declare your intent, and the router sequences the optimal multi-skill execution playbook.

---

## 🚀 The 5 Proven Playbooks

### 1. `PLAYBOOK_DISCOVERY` (Vague idea → Locked Spec & Tickets)
*When to use: "I have a new feature idea", "Not sure how to structure this", "Let's explore this project"*
```
Step 1: /same-wavelength  ← Grill interview (locks scope, users, non-goals, DoD)
Step 2: /architect        ← Pre-build planning and architectural decision surfacing
Step 3: /to-spec          ← Conversation-to-spec synthesis published to KANBAN.md
Step 4: /to-tickets       ← Decompose spec into vertical tracer-bullet tasks
```

### 2. `PLAYBOOK_DELIVERY` (Rigorous, bug-free production engineering)
*When to use: "Build this ticket", "Ship this feature safely", "Refactor core service"*
```
Step 1: /senior-stable-delivery ← Enforce stability over novelty, triage risks
Step 2: /pipeline               ← Chain-of-thought, state isolation & TDD implementation
Step 3: /ponytail-review        ← Diff audit for bloat, unnecessary deps & YAGNI violations
Step 4: /rabit-auditor          ← Senior multi-pass security, correctness & performance audit
```

### 3. `PLAYBOOK_CRAFT` (World-class UI/UX, styling & tactile polish)
*When to use: "Make this look modern", "Design this dashboard", "Fix UI slop"*
```
Step 1: /impeccable shape   ← Set aesthetic direction, layout & typographic foundations
Step 2: /refactoring-ui     ← Apply Adam Wathan & Steve Schoger tactical spacing/depth rules
Step 3: /emil-design-eng    ← Polish hover physics, micro-interactions & feedback states
Step 4: /impeccable audit   ← Deterministic anti-slop check (eliminates purple gradients & Inter clichés)
```

### 4. `PLAYBOOK_STUDY` (Deconstruct complex code & absorb mental models)
*When to use: "Explain how this works", "I want to learn this math/pattern", "Document this system"*
```
Step 1: /persona evie  ← Activate Socratic professor persona
Step 2: /the-basis     ← Ground abstract math/code in physical first-principles intuition
Step 3: Synthesize     ← Generate permanent atomic neuron in .conscience/memory/neocortex/
```

### 5. `PLAYBOOK_RECOVERY` (Diagnose & fix broken builds, errors, or tests)
*When to use: "Build broke", "Test failing", "Getting strange runtime error"*
```
Step 1: /recover      ← 3-mode failure taxonomy triage (Targeted Bug vs Polluted Context vs Wrong Assumption)
Step 2: Minimal Fix   ← Climb Law 20 parsimony ladder for single-shot minimal fix
Step 3: Verify & Log  ← Run passing test in single command and record backpropagation in episodic_log.md
```

---

## ⚡ Execution Modes

1. **Explicit Trigger**:
   ```
   /route "I need to build an authenticated billing dashboard for our SaaS"
   ```
   *The Router outputs the selected playbook, the sequence of skills, and asks for confirmation to begin.*

2. **Automated Kernel Hook (`STATE 2: INTENT_MAPPING`)**:
   When Axon processes an open-ended request during State 2, it automatically matches the prompt against the intent taxonomy:
   - If complex/multi-stage: Axon outputs `[ROUTER: Selected PLAYBOOK_<NAME>]` with the step sequence before transitioning to `STATE 3: CONTEXT_HANDSHAKE`.
