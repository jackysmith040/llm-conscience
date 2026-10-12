# Utility Animation Components API

The component catalog contains small semantic recipes that produce timeline events and accessible explanations. Components are session-scoped Plugins and use the Core scene/timeline contracts.

## Registry

```python
from plugins.utility_animation_registry import list_components, get_component, component_manifest
```

`list_components(mode=None)` returns names, supported modes, versions, and cost metadata. `get_component(name)` returns the recipe function. `component_manifest()` returns the registry snapshot.

## Current recipes

| Recipe | Purpose | Required parameters |
|---|---|---|
| `reveal_object` | Introduce an object | `scene`, `target` |
| `reveal_label` | Introduce terminology at the object | `scene`, `target` |
| `move_object` | Show a position transition | `target`, `start`, `duration`, `position_from`, `position_to` |
| `draw_arrow` | Draw direction or relation | `target` |
| `trace_curve` | Reveal a path over time | `target`, `start`, `duration` |
| `assemble_parts` | Show components becoming a system | `targets`, `start`, `duration` |
| `split_group` | Show a system decomposing | `target`, `start`, `duration` |
| `rotate_about_axis` | Show rotation in 2D/2.5D/3D | `target`, `axis`, `start`, `duration`, `angle_from`, `angle_to` |
| `camera_orbit` | Reveal a spatial relationship | `start`, `duration`, `angle_from`, `angle_to` |
| `camera_reset` | Restore canonical view | `start` |
| `parallax_layers` | Show layered depth | `targets`, `start`, `duration`, `shift` |
| `axis_reveal` | Establish coordinate orientation | `target` |
| `project_vector` | Show projection onto a plane | `target`, `plane`, `start`, `duration` |
| `before_after_compare` | Contrast initial and final states | `target`, `start`, `duration` |
| `show_invariant` | Mark a preserved property | `target`, `property`, `label` |
| `pause_for_prediction` | Freeze the scene for a prediction | `prompt`, `at` |
| `hide_then_reveal` | Require reconstruction before reveal | `target`, `hide_at`, `reveal_at` |
| `transfer_prompt` | Move the model to a nearby case | `prompt`, `at` |

## Recipe contract

Recipes return `RecipeResult` with `recipe_id`, semantic `events`, `warnings`, estimated `cost`, and `accessible_text`. They must validate targets, avoid unexplained property writes, and remain compatible with the selected renderer.

## Composition

Use `core.composition.Composition` to append recipe results, detect overlapping writes, produce a manifest, and preserve a machine-readable composition snapshot. Keep macros thin and inspectable; compose primitives rather than hiding a complete lesson inside one opaque function.

## Extension policy

Create a new Plugin recipe only when the registry cannot express a repeated mechanism. New recipes require a version, supported modes, cost metadata, accessibility text, tests, and documentation in this file. Documentation freshness checks are release-blocking.

## Public function index

The current public component and registry functions are: `assemble_parts`, `axis_reveal`, `before_after_compare`, `camera_orbit`, `camera_reset`, `component_manifest`, `draw_arrow`, `get_component`, `hide_then_reveal`, `keyframe`, `list_components`, `lookup`, `move_object`, `parallax_layers`, `pause_for_prediction`, `project_vector`, `require_targets`, `reveal_label`, `reveal_object`, `rotate_about_axis`, `show_invariant`, `split_group`, `trace_curve`, and `transfer_prompt`. These names are part of the freshness-checked API surface and must remain synchronized with the implementation.
