# 📋 PRODUCT.md & DESIGN.md Specification Standards

Impeccable separates durable product context (`PRODUCT.md`) from the living visual system (`DESIGN.md`).

---

## 1. PRODUCT.md — Durable Product Truth
Generated or updated via `/impeccable init`. Captures the high-level business and user requirements that do not change from page to page.

### Required Sections:
```markdown
# Product Context

## Audience & Users
- Primary persona: Who is using this? (e.g. Senior engineers, retail customers, internal ops)
- User mindset: What are they trying to accomplish under what constraints?

## Problem & Value Proposition
- Core problem solved:
- Value proposition / differentiator:

## Surface Architecture & Modes
- Marketing surfaces: Persuade
- Main app / console: Operate
- Docs / Help: Read

## Non-Negotiables & Constraints
- Browser support, performance budgets, accessibility requirements (WCAG AA).
- Brand voice: Tone, vocabulary, copy personality.
```

---

## 2. DESIGN.md — Living Visual Design System
Generated via `/impeccable document` or maintained collaboratively with `/imprint`. Captures all tokens and structural visual contracts.

### Required Sections:
```markdown
# Design System

## 1. Color Palette & Tokens
- **Brand**: Primary, Secondary, Accent (with exact HSL/Hex values and semantic roles).
- **Surfaces**: Canvas, Card, Elevated, Overlay.
- **Text**: Foreground, Muted, Subtle (always tinted to surface hue; never pure gray).
- **Status**: Success, Warning, Danger, Info.

## 2. Typography Scale
- Display: font-family, weight, line-height, letter-spacing.
- Heading 1–4: explicit size steps.
- Body & Small: font-family, measure (65–75ch), line-height (1.6).

## 3. Spatial System
- Base unit (e.g. 4px / 8px).
- Spacing scale: xs (4px), sm (8px), md (16px), lg (24px), xl (32px), 2xl (48px).

## 4. Elevation, Radii & Depth
- Corner radii scale: sm, md, lg, full.
- Shadows: Soft directional blur (`y: 2-8px, blur: 8-24px, opacity: 6-12%`).

## 5. Component Patterns
- Cross-references components registered in `ui-registry.md`.
```
