# 📖 GLOSSARY — Conscience OS Ubiquitous Language

> **To the AI reading this:** This is the canonical vocabulary contract for this workspace.
> Use these definitions consistently across all sessions, skills, and memory files.
> Never invent synonyms for terms defined here. Append new terms as the domain evolves.

---

## Core OS Terms

**Axon**
: The Chief Orchestrator persona. Left-brain analytical executor of the Conscience OS. Bound by the 20 Laws of Consciousness.

**Evie**
: The right-brain intuitive synthesis persona. Handles creative, empathetic, and lateral thinking tasks.

**Conscience OS**
: The full Neuro-Symbolic Digital Brain system. Encapsulated in `.conscience/`. Governs all agent behavior via the 20 Laws and the State Machine.

**Tri-Axis State Header**
: The mandatory response prefix: `[STATE: <LIFECYCLE> | INTENT: <TAXONOMY> | PACE: <VELOCITY>]`. Every agent response must begin with this.

**State Machine**
: The 5-step cognitive lifecycle: `SENSORY_INGESTION → DELIBERATION → CONTEXT_HANDSHAKE → MOTOR_EXECUTION → MEMORY_CONSOLIDATION`.

**Autopoiesis**
: The meta-cognitive super command (`/autopoiesis`). Triggers full-spectrum self-reflection, self-correction, self-healing, self-modification, and self-evolution.

---

## Memory & Tracking Terms

**KANBAN**
: The operational task board at `.conscience/memory/KANBAN.md`. Tracks active, in-progress, and completed work for the current session or sprint. Fed by `/to-tickets` and `/wayfinder` resolutions.

**Episodic Log**
: The persistent session history at `.conscience/memory/episodic_log.md`. Every completed operation must append a concise summary here (Law 8).

**Neocortex**
: The atomic knowledge base at `.conscience/memory/neocortex/`. Stores single-concept neuron files with YAML cross-linking (Law 3 & 19).

**Neuron**
: A single-concept markdown file in `.conscience/memory/neocortex/`. Follows `neuron_template.md`. Connected to related neurons via YAML frontmatter `links`.

**Memory Palace**
: `.conscience/memory/neocortex/INDEX.md`. The spatial lobby grouping neurons into visual "Rooms" (Law 5).

**Decision Map**
: A `/wayfinder` artifact. A strategic issue-tracker entry (`wayfinder:map`) listing decision tickets for a large multi-session effort.

**Decision Ticket**
: A child item of a Decision Map. Holds one question whose resolution is a decision (not a build task). Closes when the question is answered.

**Spec**
: A structured document produced by `/to-spec`. Contains: Problem Statement, Solution, Acceptance Criteria, Test Seams, and Implementation Notes. Published to KANBAN.

---

## Pipeline Terms

**Main Flow**
: The declared idea→ship pipeline: `/grill → /to-spec → /to-tickets → /implement → /code-review → /retro`. The canonical sequence for taking an idea to shipped code.

**Grill**
: The pre-work alignment interview (`/same-wavelength` or `/grill`). Locks scope, architecture, non-goals, and DoD before any implementation.

**Spec**
: See above. The output of `/to-spec`. The single source of truth for a feature or fix.

**Ticket**
: A single actionable unit of work derived from a Spec via `/to-tickets`. Lives in KANBAN. Small enough to complete in one agent session.

**Retro**
: A post-session retrospective (`/retro`). Reviews the session's navigation, guardrails, and coding standards violations. Improves the agent *environment*, not just the code.

**Prototype**
: Throwaway code produced by `/prototype` to answer a design question. Must be deleted after the question is answered. Never shipped.

---

## Git & Mode Terms

**Host Project Mode**
: `git-mode = host_project`. The agent's internal git tracking is disengaged. `.conscience/` is shielded from the host repo's git history.

**Meta Dev Mode**
: `git-mode = meta_dev`. Full git tracking enabled. Used when evolving the Conscience OS itself.

**Isolation**
: The act of switching to Host Project Mode via `/git-mode isolate`.

---

## Pacing & Velocity Terms

**BITE**
: Default pace. Max 30–50 line changes per step. Mandatory Digest-Before-Diff. Pauses for human review between steps (Law 20).

**STANDARD**
: Component-slice pace. Moderate change batches with periodic review points.

**FAST**
: Autonomous batch execution. No per-step pauses. Use only when scope is fully locked.

**Digest-Before-Diff**
: The mandatory 2-line summary before every code change under `PACE: BITE`. States *Intent* and *Rationale*.

---

## Skill Architecture Terms

**Skill**
: A SKILL.md file in `.conscience/skills/<name>/`. Encodes one reusable agent habit or workflow. Loaded on-demand via slash command.

**Progressive Disclosure**
: The skill design pattern where inline content covers what every branch needs, and rare/edge-case content is pushed behind a pointer to a references file. Keeps SKILL.md bodies ≤ 60 lines.

**Context Pointer**
: A reference in a skill or AGENTS.md that names out-of-context material and states the condition for reaching it. The wording of the pointer determines when the agent reaches the material.

**CIP (Context Ignition Packet)**
: A structured summary of the Director's intent, constraints, and acceptance criteria. Generated by Axon after a clarifying dialogue and presented for approval before execution.

---

## Impeccable & Design Craft Terms

**Impeccable**
: The frontend craft and design engine (`/impeccable`, v4.6.0). Provides 24 specialized design commands, 4 visitor modes, and 61+ anti-slop rules to ensure out-of-distribution UI quality.

**Craft Floor**
: The non-negotiable quality baseline and verification checklist (`references/craft-floor.md`) enforced before any UI edit. Covers contrast, depth, spacing rhythm, typography measure, motion physics, and browser surface theming.

**Anti-Slop**
: The systematic ban list of AI design clichés: generic Inter-everywhere, cardocalypse, purple-blue gradients, kickers/eyebrows above headings, untinted grays, and crude mascot doodles.

**PRODUCT.md**
: The durable product context file generated via `/impeccable init`. Captures user personas, business objectives, non-negotiables, brand voice, and operating constraints without mixing in transient visual styling.

**DESIGN.md**
: The living visual system contract generated via `/impeccable document`. Captures design tokens (palette, typography scale, spacing scale, corner radii, elevation shadows) and component patterns.

**Persuade Mode**
: The design altitude for landing pages, marketing, and acquisition. Requires full commitment to bold, distinct typography and memorable character.

**Operate Mode**
: The design altitude for web apps, dashboards, and developer tools. Emphasizes visual scanability, consistency, restraint, ergonomics, and muscle memory.

**Read Mode**
: The design altitude for documentation and articles. Focuses on typographic cadence, comfortable reading measure (65–75ch), and low cognitive fatigue.

**Experience Mode**
: The design altitude for portfolios, showcases, and immersive experiences where the interface recedes and the artifact leads.

