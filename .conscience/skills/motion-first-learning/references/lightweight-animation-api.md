# Lightweight animation API

The lightweight animation framework is the default renderer for short educational motion when a full Manim scene is unnecessary.

## Core API

```python
from core.animation import Scene, Element, Keyframe, Renderer

scene = Scene(width=1280, height=480, fps=12, duration=4, title='Concept behaving')
scene.add(Element('box', 'rect', {'x': 80, 'y': 180, 'w': 180, 'h': 80, 'text': 'State A'}, [
    Keyframe(0, 1, {'x': (80, 300)})
]))
Renderer(scene).export('output', 'demo')
```

The stable primitives are `rect`, `arrow`, and `label`. Keyframes interpolate numeric properties with a bounded easing function. `Renderer.render()` produces PNG frames; `Renderer.export()` produces MP4 and GIF artifacts.

## Plugin API

The session-scoped `plugins.lightweight_animation` module accepts a JSON-compatible specification:

```python
from plugins.lightweight_animation import render_scene
render_scene(spec, 'output', 'lesson')
```

The Plugin may create or modify scene specifications during a session, but it must use the Core renderer and remain sandboxed.

## Performance policy

Use small canvases, 8–15 FPS previews, short scenes, reusable primitives, and segment rendering. Render only the scene needed for the current learning step. Use MP4 for delivery and GIF for quick inspection. Use Manim when continuous mathematical geometry, symbolic layout, or higher-fidelity transformations justify its higher render cost.

## Educational quality contract

Every animation should make one process visible, name the states, show the transition, and end with a learner action such as prediction, reconstruction, retrieval, or transfer. Include an accessible text equivalent and a static keyframe fallback.
