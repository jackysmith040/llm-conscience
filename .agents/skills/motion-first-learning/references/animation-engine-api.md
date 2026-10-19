# Animation engine API

## Core modules

| Module | Public API | Purpose |
|---|---|---|
| `core.animation` | `Scene`, `Element`, `Keyframe`, `Renderer` | Fast deterministic 2D rendering and export |
| `core.math3d` | `Vec3`, `lerp_vec`, `mat4_mul`, `mat4_apply`, `translation`, `scale`, `rotation_y`, `perspective`, `orthographic`, `project` | Tested spatial math |
| `core.animation_schema` | `validate_scene` | Schema and semantic validation |
| `core.scene_graph` | `Node`, `SceneGraph.add`, `SceneGraph.world_position`, `SceneGraph.snapshot`, `SceneGraph.from_scene` | Hierarchical object identity and snapshots |
| `core.timeline` | `evaluate_value`, `evaluate_timeline` | Keyframes, event markers, pauses, and deterministic evaluation |
| `core.renderer_router` | `choose` | Cost-aware backend routing |

## Plugins

| Module | Public API | Purpose |
|---|---|---|
| `plugins.lightweight_animation` | `build_scene`, `render_scene` | Declarative fast animation scenes |
| `plugins.web_canvas_renderer` | `generate_html` | Dependency-free interactive 2D/2.5D/3D preview |
| `plugins.manim_plugin` | `plan_render`, `command`, `fallback_manifest` | Optional preview-first Manim planning |

Every change to these APIs must update this reference and pass documentation freshness validation. The documentation checker is release-blocking.

## Inherited and utility APIs

The following public utility functions remain part of the documented harness surface and are covered by `references/harness-api.md`: `create_session`, `save_state`, `load_state`, `validate_state`, `create_checkpoint`, `resume_from_checkpoint`, `cleanup_session`, `ease_in_out`, `mat4_identity`, `public_functions`, `check_freshness`, `propose_adaptation`, `promote_adaptation`, and `rollback_adaptation`.

The math and rendering helpers documented in the tables above include `lerp`, `lerp_vec`, `translation`, `scale`, `rotation_y`, `mat4_mul`, `mat4_apply`, `perspective`, `orthographic`, `project`, `validate_scene`, `choose`, `route`, `evaluate_value`, `evaluate_timeline`, `plan_render`, `command`, `fallback_manifest`, `generate_html`, `build_scene`, and `render_scene`.

## Utility Animation Components API

The utility component Plugin public API is documented in `references/utility-animation-api.md`. Its freshness-checked public functions are: `assemble_parts`, `axis_reveal`, `before_after_compare`, `camera_orbit`, `camera_reset`, `component_manifest`, `draw_arrow`, `get_component`, `hide_then_reveal`, `keyframe`, `list_components`, `lookup`, `move_object`, `parallax_layers`, `pause_for_prediction`, `project_vector`, `require_targets`, `reveal_label`, `reveal_object`, `rotate_about_axis`, `show_invariant`, `split_group`, `trace_curve`, `transfer_prompt`.
