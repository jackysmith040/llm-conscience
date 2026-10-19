---
name: color-palette
description: >-
  Generate complete, accessible colour palettes from a single brand hex.
  Produces 11-shade scale (50-950), semantic tokens, dark mode variants, and WCAG contrast checks.
---

# Color Palette Skill

[STATE: MOTOR_EXECUTION | INTENT: CRAFT_POLISH | PACE: STANDARD]

## Core Capabilities
From a single brand hex, generate an accessible, professional 11-shade color system (50–950) with semantic tokens, dark-mode adaptations, and WCAG AA/AAA validation.

## Generation Rules
1. **Perceptual Uniformity**: Adjust lightness smoothly across shades (50 = background tint, 500 = brand anchor, 900–950 = text/contrast).
2. **Semantic Tokens**:
   - `primary`, `secondary`, `accent`
   - `success` (emerald/green), `warning` (amber), `danger` (rose/red), `info` (sky/blue)
   - `surface`, `surface-subtle`, `border`, `text-primary`, `text-muted`
3. **Accessibility First**:
   - Normal text requires ≥ 4.5:1 contrast against surface.
   - Large text requires ≥ 3:1 contrast against surface.
   - Interactive components require visible focus states.
4. **Dark Mode Generation**: Invert lightness curve while preserving hue nuances; avoid pure black `#000000` (use dark charcoal/zinc).

## Reference Pointer (Progressive Disclosure)
> 🎨 **Tailwind v4 CSS Configurations, Hex-to-HSL Conversion Formulas & Contrast Calculators:**  
> Load only when calculating exact numeric shades or CSS token mappings:  
> `→ see .conscience/skills/color-palette/references/color_system_generator.md`
