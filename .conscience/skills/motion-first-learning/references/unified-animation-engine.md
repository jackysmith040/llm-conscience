# Unified animation engine

## Renderer selection

Use SVG for crisp low-object-count diagrams and labels. Use Canvas for interactive 2D and 2.5D playback. Use lightweight browser projection for simple 3D spatial previews. Use Pillow/FFmpeg for deterministic short exports. Use Manim only when specialist mathematical fidelity justifies its render cost.

## 2.5D

Represent flat objects with explicit `z`, layer, parallax factor, and camera response. A camera move shifts distant layers less than near layers. Keep an orthographic reset view so the learner can verify that the apparent depth effect has not changed the underlying relationship.

## 3D

Declare handedness, up-axis, units, angle units, and projection. Use explicit model, view, and projection stages. Keep primitives small: points, lines, vectors, axes, grids, planes, curves, spheres, cubes, and labels. Require stable semantic IDs and accessible descriptions.

## Animation quality

Every scene should have an initial state, a visible transformation, a pause or prediction checkpoint, and a learner action. Avoid motion that is decorative, ambiguous, or faster than the learner can interpret. Use easing to support attention, not to falsify a process.

## Performance

Set a complexity budget. Cache static layers, reuse objects, batch repeated geometry, cap preview FPS, and split dense scenes. Fall back from 3D to 2.5D, 2D, staged frames, or text when the richer medium does not add explanatory value.
