---
name: visual-learning-software
description: Build browser-based visual learning software from lecture notes, textbooks, slide decks, documents, images, or other source materials. Use when the user wants an interactive course, study game, tutorial app, quiz system, exam-prep tool, or visual educational experience that teaches from zero to assessment readiness.
---

# Visual Learning Software

Build educational software as a **learning system**, not a collection of decorative screens. Convert source material into a progression from intuition to formal language, worked examples, guided reasoning, retrieval practice, and exam readiness.

## Use this skill when

Use this skill when a user provides source notes or asks for a visual, interactive way to learn a subject. It applies to mathematics, science, engineering, languages, medicine, history, and other content domains. Prefer a browser-based WebDev project unless the user requests another platform.

## Required input and assumptions

Ask for the source material before inventing curriculum content. Accept PDFs, slide decks, documents, images, URLs, or structured syllabi. Ask only the minimum clarifying questions needed: target learner level, assessment format, preferred platform, and deadline or topic priorities. If the source is incomplete, label assumptions and keep unsupported content separate from source-grounded content.

Never fabricate citations, theorems, worked solutions, exam questions, reviews, ratings, or learner outcomes. Distinguish **source-grounded content**, **pedagogical scaffolding**, and **generated practice variants**.

## End-to-end workflow

1. **Inspect the source.** Extract text and page structure from each provided file. Build a topic map containing definitions, propositions, theorems, proof ideas, examples, notation, prerequisites, and likely assessment targets. Preserve page or section references internally.
2. **Design the learning route.** Organize the map into zones or modules with prerequisites and mastery signals. Use: visual intuition → formal definition → anchor example → nearby examples → step-by-step reasoning → scoped retrieval quiz → exam-style challenge.
3. **Write the design brief.** For a non-replication project, create `ideas.md` with three genuinely different visual approaches, choose one, and define its movement, principles, palette philosophy, layout, motifs, interactions, animation, typography, voice, and logo concept. For a reference-matching project, record the reference as the ground-truth spec.
4. **Initialize the product.** Start a WebDev project with `webdev_init_project` unless one already exists. Read the appropriate WebDev template skill and, for browser games, the `game-dev` skill. Use generated or properly uploaded visual assets for prominent areas; do not commit large local media into the project.
5. **Model the content.** Create a typed content model before building UI. A zone should support `id`, `title`, `prerequisites`, `visual`, `definition`, `examples`, `reviewSteps`, `questionBank`, `commonMistakes`, and `masteryRule`. A question should include `prompt`, `answers`, `correct`, `explanation`, `hint`, `difficulty`, `sourceSection`, and `skillTag`.
6. **Implement the learning loop.** Build a route map, lesson view, review view, scoped quiz view, and exam view. Make every button perform a real action or show an intentional disabled state. Implement tab state explicitly; never ship decorative tab buttons. Give every state a visible back path and clear next action.
7. **Gate assessment intelligently.** A zone quiz selects only questions from the active zone. Do not force learners to answer material they have not studied unless they deliberately choose diagnostic or full mock-exam mode. Use progressive difficulty: recognition, conceptual transfer, then proof or multi-step reasoning. Explain every answer and offer a route back to the exact review content after a miss.
8. **Build feedback that teaches.** Track attempts, accuracy, hints, unanswered items, and time used. Report performance by zone and skill tag. Make weak-topic recommendations actionable: clicking one must navigate to the relevant zone and open its review or visual starting point. Avoid vague feedback such as “study more.”
9. **Verify in layers.** Run type-check and build checks. Inspect client and dev-server logs. Capture representative desktop and mobile screenshots. Test route navigation, every lesson tab, answer selection, retry, timer expiry, submit, result links, and reset. If browser automation is unavailable, state that interaction testing is limited and compensate with deterministic checks and preview verification.
10. **Checkpoint and deliver.** Update `PLAN.md`, `STRUCTURE.md`, `MEMORY.md`, `ASSETS.md`, and `todo.md`; save one checkpoint after the implementation is coherent; deliver the checkpoint attachment; explain how to open the preview and publish it. Never publish on the user’s behalf.

## Subject-specific teaching rules

For mathematical or proof-heavy subjects, introduce notation before using it, name hypotheses before applying a theorem, show the invariant or geometric meaning, and separate a proof outline from a formal proof. For every theorem, include what it says, why it is useful, the hypothesis checklist, a small example, a common failure mode, and an exam prompt.

For other subjects, replace theorem checklists with the relevant structure: causal chain, procedure, vocabulary, timeline, mechanism, or decision rule. Keep the same intuition → formalization → example → retrieval → assessment progression.

## Content quality checks

Before delivery, verify that every zone has at least one visual explanation, one precise definition or rule, two examples, four review steps, three questions at increasing difficulty, answer explanations, and a recovery path after an incorrect answer. Verify that question options are unambiguous, the correct answer is not always in one position, and source claims are not overstated.

Prefer concise interfaces over content walls. Use progressive disclosure so details appear when needed. Make uncertainty visible when a source is ambiguous. Do not claim that a learner is exam-ready based only on completion; report observed practice performance instead.

## Bundled references

Read `references/content-model.md` when defining typed lesson and question data. Read `references/verification-matrix.md` when testing an implementation or preparing a checkpoint. Use the project’s `PLAN.md`, `STRUCTURE.md`, `MEMORY.md`, `ASSETS.md`, and `ideas.md` to preserve decisions across sessions.
