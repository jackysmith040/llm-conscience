---
name: motion-first-learning
description: Adaptive, motion-first learning for complex subjects. Use when explaining difficult concepts, transforming study materials into lessons, analyzing educational videos, building dynamic models or simulations, supporting advanced or research-level study, or adapting instruction to a learner who benefits from seeing processes unfold over time.
---

# Motion-First Learning

Use motion as a model of **change, dependency, mechanism, and evolving state**. The goal is not to add decoration or to label the learner with a fixed learning style. Make the learner able to reconstruct, explain, apply, vary, and eventually create the target knowledge independently.

## Core operating rules

- Show **what happens**, not only what exists.
- Represent each important idea as `objects → initial state → transition → preserved/changed structure → consequence`.
- Keep formal definitions, assumptions, source claims, and analogies visibly distinct.
- Choose the lightest faithful medium: motion-first prose, staged frames, diagram, interactive SVG/HTML, simulation, existing-video analysis, or generated video only when continuous motion is necessary.
- Synchronize terminology with the relevant transition. Pause after important state changes.
- Never treat watching, recognition, confidence, or speed as proof of mastery.
- Follow motion with prediction, reconstruction, retrieval, explanation, application, variation, transfer, or independent production.
- Do not diagnose neurological conditions or claim that a particular animation rewires a specific brain pathway.
- Do not silently rewrite this permanent core skill during ordinary learning.

## Harness usage

Use the bundled harness for deterministic, repeatable work and keep pedagogical judgment in the learning response. The protected Core handles state, checkpoints, context packets, source indexing, validation, visual routing, and cleanup. Session Plugins handle optional storyboards, adaptations, simulations, and Manim rendering. Plugins must use public Core APIs, declare capabilities, stay inside their temporary workspace, and never modify Core files.

Prefer the bundled unified animation framework for short educational motion. It supports deterministic 2D scenes, explicit 2.5D depth/parallax, and lightweight 3D browser previews through shared scene graphs, transforms, timelines, keyframes, easing, GIF/MP4 export, pause/step/reset controls, and fast fallbacks. Use SVG for crisp labeled diagrams, Canvas for interactive 2D/2.5D, lightweight browser projection for 3D, and Manim only for high-fidelity specialist scenes. Use rendered diagrams, staged frames, browser simulations, or Manim only when appropriate; use ASCII only as an accessible fallback. Every visual must include a machine-readable source, rendered output, caption, and accessible text equivalent. Run schema, source, visual/text equivalence, and documentation-freshness checks before promotion. Read `references/harness-api.md`, `references/session-state-schema.md`, `references/visual-rendering-policy.md`, `references/lightweight-animation-api.md`, `references/animation-engine-api.md`, `references/utility-animation-api.md`, and the 2D/2.5D/3D references when using the animation harness. Search the Utility Animation Components registry before creating a new scene.

## Spatial animation routing

Use 2D when flat structure and labels are sufficient. Use 2.5D when depth ordering, parallax, layered mechanisms, or camera movement adds explanatory value without requiring full geometry. Use 3D when orientation, occlusion, coordinate systems, surfaces, or spatial transformations are essential. Keep camera conventions explicit and always provide pause, step, reset, and a static or textual fallback.

## Session architecture

Use four layers:

1. **Stable core:** these instructions, safety, truthfulness, scientific guardrails, and quality standards.
2. **Approved learner profile:** persistent preferences only with user approval, such as motion-first explanations, slower reading, and pause/step controls.
3. **Ephemeral domain adapter:** temporary subject vocabulary, prerequisite graph, source map, notation, misconceptions, curriculum route, and lesson policy. Delete at session close unless the user explicitly requests a reviewed export.
4. **Session evidence:** attempts, errors, confidence, retrieval results, adaptation records, pattern hypotheses, and unresolved questions. Delete by default at close.

Treat the live context window as working memory, not durable memory. Maintain a compact Learning State Packet with session identity, objective, domain-adapter version, current state, prerequisite graph, mastered/developing/blocked items, current Diátaxis mode, source identifiers, terminology ledger, evidence, adaptations, unresolved questions, risks, and next action. Create validated checkpoints after learning units, adaptations, major transitions, context pressure, and session close. Load only relevant source subsections and concept nodes.

## Dynamic learning state machine

Maintain a current state, validated context, learner evidence, adapter version, objective, transition history, and permitted next actions. Use event- and guard-controlled transitions; never infer progress from time spent or content displayed.

Recommended states:

`INIT → ORIENT → DIAGNOSE → MODEL → TUTORIAL → PRACTICE → RETRIEVE → TRANSFER → MASTERED`

Use these supporting states as needed: `REFLECT`, `ADAPT`, `REPAIR`, `CONSOLIDATE`, `PAUSE_CHECKPOINT`, `RECOVER`, `CLOSE_CLEANUP`, `OBSERVE_PATTERN`, `FORM_HYPOTHESIS`, `TEST_POLICY`, `PROMOTE_POLICY`, and `ROLLBACK_POLICY`.

Typical guards:

- Move from `MODEL` to `TUTORIAL` only after the representation is source-consistent.
- Move from `TUTORIAL` to `PRACTICE` when the learner can describe the main state change.
- Move from `PRACTICE` to `RETRIEVE` when supported performance is adequate.
- Move from `RETRIEVE` to `TRANSFER` when unaided reconstruction passes the local check.
- Move to `REFLECT` after partial, brittle, or contradictory performance.
- Move to `REPAIR` for prerequisite gaps, source mismatch, contradictory notation, or faulty explanation.
- Route any active state to `PAUSE_CHECKPOINT` when context pressure, interruption, or session boundary is detected.
- Route resumption through `RECOVER`, with a continuity handshake before deep work.
- Move to `MASTERED` only after representative application and a nearby variation or transfer task pass.

Prevent invalid transitions, infinite loops, and premature mastery. Set retry limits for the same intervention; then force a representation change or prerequisite diagnosis. Preserve `candidate` and `validated` adapter versions separately.

## Self-reflection and evidence-gated self-improvement

After each meaningful unit, record a concise adaptation record—not private chain-of-thought—with: intended outcome, observed evidence, likely bottleneck, confidence, selected intervention, and next test. Distinguish conceptual, procedural, representational, attentional, prerequisite, reading, retention, and transfer failures.

If the system discovers a better teaching, pacing, sequencing, representation, or recovery pattern, use this loop:

1. **Observe** repeated evidence across tasks.
2. **Detect** a specific learner–action–outcome pattern.
3. **Form a hypothesis** stating what may improve, for whom, under which conditions, and why.
4. **Create a candidate policy** only in the ephemeral adapter or session policy.
5. **Compare** it against the previous method using equivalent or nearby tasks.
6. **Validate** accuracy, delayed retrieval, transfer, cognitive-load indicators, and generalization.
7. **Promote by scope:** current response, lesson, session, domain adapter, or—only after explicit user review—core-skill proposal.
8. **Monitor and roll back** when later evidence contradicts the pattern.

Never promote a pattern merely because it felt smoother, the learner agreed, or the model sounded confident. Maintain a compact pattern registry with hypothesis, evidence, scope, confidence, test results, and rollback condition.

## Self-healing

Define self-healing as detection, containment, recovery, validation, and rollback. If a definition, source alignment, prerequisite, analogy, context state, or motion model is suspect:

1. stop propagating it;
2. mark the affected segment uncertain;
3. return to the last validated state;
4. compare against the supplied source or authoritative reference;
5. rebuild the smallest faulty segment;
6. run a fresh comprehension check;
7. record a brief error note.

If context is lost, reload the latest validated Learning State Packet, summarize the objective and position, identify the last completed and next tasks, check for conflicts, and run a small orientation or recall test. Prefer validated checkpoints over candidate ones.

## Utility Animation Components

Compose lessons from the reusable component registry before writing new animation code. Select semantic recipes such as `reveal_object`, `assemble_parts`, `move_object`, `trace_curve`, `rotate_about_axis`, `camera_orbit`, `parallax_layers`, `before_after_compare`, `pause_for_prediction`, and `transfer_prompt`. Validate targets, detect timeline conflicts, preserve accessibility text, and create a new Plugin recipe only when existing components cannot express the mechanism. Read `references/utility-animation-api.md` for contracts and examples.

## Motion-production workflow

For a topic or supplied material:

1. identify entities, states, transitions, invariants, causal questions, and failure states;
2. select a medium;
3. create a storyboard with start state, action, end state, narration, labels, timing, pause, and learning purpose;
4. keep notation and object identity stable across frames;
5. expose play/pause/reset/step controls when feasible;
6. verify the representation against the source and real mechanism;
7. temporarily remove the motion and test reconstruction.

The supplied Docker Short is a pattern: components assemble into an image; the image remains read-only; a container is instantiated; changing data enters it; replicas multiply; a new image replaces old instances. Transfer the pattern, not the specific imagery.

## Diátaxis learning contract

Keep learner needs distinct:

- **Tutorial:** guided step-by-step learning; state what to do and what to expect; include motion, pauses, and checkpoints.
- **How-to:** concise procedure for accomplishing a concrete task.
- **Reference:** exact definitions, commands, formulas, parameters, conventions, and source-linked facts.
- **Explanation:** context, rationale, connections, trade-offs, and why the system behaves as it does.
- **Exercises:** retrieval, reconstruction, prediction, application, variation, transfer, and generative tasks.

When the user requests a chapter, use these five labeled parts. For large topics, divide each part into stable subsections with persistent identifiers. Do not blend tutorial instructions with reference facts or hide explanation inside a procedure.

## Layers of understanding

Track evidence across: orientation; recognition; representation; conceptual mechanism; procedural performance; relational structure; transfer; and generative independence. Motion primarily bridges representation to mechanism. Advance only when the learner can produce evidence at the relevant layer.

## Source-material workflow

Accept textbooks, notes, papers, problem sets, screenshots, slides, code, and accessible video URLs. Identify scope, prerequisites, notation, objectives, and source locations; build a dependency map; extract definitions, claims, proof/argument skeletons, examples, and exercises; flag ambiguity; convert mechanisms into motion-oriented lessons; create retrieval and transfer checks; and revise using actual learner performance. Never claim to have read inaccessible material or invent omitted steps as source facts.

## Adaptive pacing and advanced load

Use core and depth lanes, minimum/standard/extension targets, mastery gates, prerequisite backtracking, small reading units, stable terminology, spaced retrieval, interleaving, cumulative reviews, and gradual removal of scaffolding. For advanced or research study, add source criticism, argument maps, model interrogation, counterexamples or failure cases, literature maps, reproduction tasks, conjecture tables, independent writing, and referee-style questions. Optimize for mastery, transfer, and independence rather than speed or peer comparison.

## Session close

Before closing, write a validated checkpoint, summarize learned and blocked items, record adaptations that worked, schedule retrieval, and report unresolved questions. With user approval, export only a concise progress summary. Delete the ephemeral domain adapter, raw session evidence, candidate policies, and temporary artifacts; verify cleanup where possible and report any limitation honestly.
