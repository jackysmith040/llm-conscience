---
name: emil-design-eng
description: >-
  Encodes Emil Kowalski's philosophy on UI polish, component craft, animation physics,
  and the invisible details that make software feel great.
---

# Emil Design Engineering Skill

[STATE: MOTOR_EXECUTION | INTENT: CRAFT_POLISH | PACE: STANDARD]

## Core Philosophy
- **Taste is trained**: Good taste is recognizing what elevates. Study why great interfaces feel right.
- **Unseen details compound**: Invisible correctness makes software feel magical without users knowing why.
- **Beauty is leverage**: Taste and polish are primary product differentiators.

## Review Table Mandate
When auditing UI code, you MUST output an explicit markdown table:
| Before | After | Why |
|---|---|---|
| `transition: all 300ms` | `transition: transform 200ms ease-out` | Target specific properties; avoid `all` |
| `transform: scale(0)` | `transform: scale(0.95); opacity: 0` | Nothing in physics appears from 0 |
| `ease-in` on dropdown | `ease-out` with custom bezier | `ease-in` feels sluggish |

## Key Animation & Interaction Rules
1. **Never animate `all`**: Animate only composite-friendly properties (`transform`, `opacity`).
2. **Origin matters**: Dropdowns and popovers must scale from their trigger point (`transform-origin`).
3. **Active feedback**: Every clickable surface requires `:active` tactile response (e.g. `scale(0.97)`).
4. **Duration physics**: Small micro-interactions = 100–180ms; large transitions = 250–350ms max.

## Reference Pointer (Progressive Disclosure)
> 🎨 **Component Recipes, Spring Physics & Cubic-Bezier Tables:**  
> Load only when implementing detailed component animations or physics tuning:  
> `→ see .conscience/skills/emil-design-eng/references/emil_philosophy_and_components.md`
