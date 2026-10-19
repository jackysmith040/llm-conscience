# 🎨 Impeccable 24-Command Reference (v4.6.0)

Impeccable provides a shared, structured design vocabulary for AI agents and developers. All commands are accessed via `/impeccable <command> [target]` or direct slash shortcuts.

---

## 1. Create & Build
| Command | Arguments | Category | Description |
|---|---|---|---|
| `init` | none | Setup | One-time setup: interviews user for durable product context, writes `PRODUCT.md`, detects platform mode, and recommends next design actions. |
| `shape` | `[feature]` | Build | UX/UI discovery and planning before code is written. Bridges problem statements into structured visual briefs and test seams. |
| `craft` | `[feature]` | Build | Full end-to-end shape-then-build workflow with visual iteration. |
| `document` | none | Design System | Audits existing codebase styles/tokens and generates root `DESIGN.md` (tokens, typography scale, color palette, component catalog). |
| `extract` | `[target]` | Design System | Scans existing components and extracts repeated UI patterns/styles into shared design system tokens and reusable components. |

---

## 2. Evaluate & Critique
| Command | Arguments | Category | Description |
|---|---|---|---|
| `critique` | `[target]` | Evaluate | High-level UX design review with heuristic scoring. Audits visual hierarchy, cognitive clarity, emotional resonance, and identifies AI slop tells. |
| `audit` | `[target]` | Evaluate | Technical quality check. Verifies WCAG accessibility (contrast ≥4.5:1), touch targets (≥44px), responsive behavior across breakpoints, and native platform conventions. |

---

## 3. Refine & Stylize
| Command | Arguments | Category | Description |
|---|---|---|---|
| `polish` | `[target]` | Refine | Final quality pass before shipping. Eliminates hairline flaws, aligns spacing to grid tokens, themes browser surfaces (scrollbars, selection, focus rings). |
| `bolder` | `[target]` | Refine | Amplifies safe, boring, or timid designs. Increases typographical scale, boosts contrast, deepens shadows, and injects distinctive visual character. |
| `quieter` | `[target]` | Refine | Tones down loud, chaotic, over-designed, or visually aggressive interfaces. Removes unnecessary decorative borders, gradients, and extraneous accents. |
| `animate` | `[target]` | Motion | Adds purposeful animations and transition physics. Replaces harsh instant jumps with natural exponential ease-outs (100–300ms max). |
| `colorize` | `[target]` | Color | Introduces strategic, intentional color to bland or monochromatic UIs. Tints neutrals and creates harmonious semantic status tokens. |
| `typeset` | `[target]` | Typography | Fixes typography hierarchy, font pairings, line-heights, letter-spacing (tracking floor -0.04em), and reading measures (65–75 characters max). |
| `layout` | `[target]` | Spatial | Fixes spacing rhythm, grid alignment, padding hierarchy, and visual grouping. Enforces tight groups and generous section margins. |
| `delight` | `[target]` | Craft | Adds memorable personality, subtle celebratory micro-interactions, tactile feedback, and signature product moments. |
| `overdrive` | `[target]` | Craft | Pushes past conventional UI limits with extraordinary, award-winning visual effects (canvas shaders, rich glass, layered depth, dynamic cursors). |

---

## 4. Simplify & Fix
| Command | Arguments | Category | Description |
|---|---|---|---|
| `distill` | `[target]` | Simplify | Strips interface to its essential core. Eliminates decorative clutter, redundant containers, and unnecessary chrome to let content lead. |
| `clarify` | `[target]` | Copy | Rewrites confusing UX copy, ambiguous form labels, and passive error messages into punchy, helpful, human language. |
| `adapt` | `[target]` | Responsive | Adapts an existing interface for different viewports, form factors, devices (desktop, tablet, mobile), or native OS conventions (iOS, Android). |
| `optimize` | `[target]` | Performance | Diagnoses and resolves UI performance bottlenecks: eliminates layout thrashing, minimizes paint times, optimizes CSS animations, and secures 60fps. |

---

## 5. Harden & Interactive Iteration
| Command | Arguments | Category | Description |
|---|---|---|---|
| `harden` | `[target]` | Resilience | Makes UI bulletproof: covers error boundaries, network failure states, extreme text overflow, i18n long strings, and empty data states. |
| `onboard` | `[target]` | Activation | Crafts engaging first-run experiences, empty state call-to-actions, progressive disclosure tooltips, and fast user activation pathways. |
| `live` | none | Browser | Starts live browser variant iteration mode, allowing interactive element selection and instantaneous styling experimentation. |
| `generate` | `[n] [element]` | Browser | Generates alternative visual variants or component treatments directly in browser for side-by-side user comparison. |
