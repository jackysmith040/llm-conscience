# Harness API

The harness is split into protected Core utilities and sandboxed session Plugins.

## Core

| Module | Public operation | Purpose |
|---|---|---|
| `core.state_store` | `create_session`, `save_state`, `load_state`, `validate_state`, `create_checkpoint`, `resume_from_checkpoint`, `cleanup_session` | Durable state and lifecycle |
| `core.state_machine` | `StateMachine.allowed`, `StateMachine.apply`, `StateMachine.inspect` | Guarded transitions and history |
| `core.visualize` | `route` | Route structured models to Mermaid sources and accessible text |
| `core.documentation` | `public_functions`, `check_freshness` | Discover and verify documented public APIs |

All Core operations return JSON-compatible dictionaries or typed results. State-changing operations validate required fields before writing.

## Plugins

| Module | Public operation | Purpose |
|---|---|---|
| `plugins.adaptation` | `propose_adaptation`, `promote_adaptation`, `rollback_adaptation` | Candidate teaching policies |
| `plugins.manim_plugin` | `plan_render`, `command`, `fallback_manifest` | Optional preview-first Manim planning |

Plugins are provisional by default. They must not modify Core files or bypass Core validation.

## Manim policy

`plan_render(..., quality="preview")` creates a low-cost render plan. Use `quality="final"` only after the storyboard and learning check pass. If Manim is unavailable or slow, use the declared fallback medium.
