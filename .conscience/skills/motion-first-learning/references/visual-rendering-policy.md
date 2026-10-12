# Visual rendering policy

## Routing

Use the simplest visual that faithfully represents the concept.

| Need | Primary | Fallback |
|---|---|---|
| State machine, workflow, architecture | Mermaid/deterministic diagram | Transition or relationship table |
| Mechanism or process | Staged frames, storyboard, or simulation | Numbered states |
| Continuous mathematical/geometric motion | Manim preview, then selective final render | Staged frames or browser model |
| Quantitative relationship | Deterministic plot | Data table |
| Proof or argument | Progressive proof/argument map | Premise/conclusion outline |
| Video-derived explanation | Keyframes and reconstructed storyboard | Timestamped description |

## Artifact contract

Each visual must include a machine-readable source, rendered output, caption, accessible text equivalent, and source identifiers. Validate that labels, arrows, state names, and transitions match the structured model.

## Manim

Use Manim only when continuous motion materially improves the model. Render a low-cost preview first, then final quality after validation. Keep scenes modular, cache unchanged assets, and render short segments. Never block a learning session on a long render; use the declared fallback.

## Accessibility and density

Provide an equivalent text description that names entities, ordering, transitions, and conclusions. Split diagrams that are too dense into linked views. Use ASCII only when rendering is unavailable, text-only output is requested, or the visual is supplemental.
