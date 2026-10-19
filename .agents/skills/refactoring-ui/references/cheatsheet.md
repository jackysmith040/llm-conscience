# Cheatsheet — concrete values to lift directly

These are battle-tested defaults pulled from *Refactoring UI*. When you don't have a strong reason to invent something custom, use these. They pair cleanly with Tailwind defaults but work in any framework.

## Spacing & sizing scale

A single non-linear scale used for padding, margin, gap, width, height. Adjacent values differ by ≥ ~25%, which means the eye actually sees the difference.

| Token | px |
|---|---|
| 0 | 0 |
| px | 1 |
| 0.5 | 2 |
| 1 | 4 |
| 1.5 | 6 |
| 2 | 8 |
| 3 | 12 |
| 4 | 16 |
| 5 | 20 |
| 6 | 24 |
| 8 | 32 |
| 10 | 40 |
| 12 | 48 |
| 16 | 64 |
| 20 | 80 |
| 24 | 96 |
| 32 | 128 |
| 40 | 160 |
| 48 | 192 |
| 56 | 224 |
| 64 | 256 |
| 80 | 320 |
| 96 | 384 |

(This is the Tailwind scale, which itself comes from this book's logic.)

**Rule of thumb in use:**
- Gap *inside* a tight group (label → input): `1` or `2` (4–8px)
- Padding inside a button: `2`-`3` vertical, `4`-`6` horizontal
- Padding inside a card: `6`-`8` (24–32px)
- Gap between cards in a grid: `4`-`6`
- Gap between top-level page sections: `16`-`24` (64–96px)

## Type scale

Hand-picked, not modular. Avoids fractional values; gives you the sizes you actually want.

| Token | px | rem | Typical use |
|---|---|---|---|
| xs | 12 | 0.75 | meta labels, badges |
| sm | 14 | 0.875 | secondary text, captions |
| base | 16 | 1.0 | body |
| lg | 18 | 1.125 | emphasized body, lead paragraphs |
| xl | 20 | 1.25 | small headings, card titles |
| 2xl | 24 | 1.5 | section headings |
| 3xl | 30 | 1.875 | page titles |
| 4xl | 36 | 2.25 | small hero headlines |
| 5xl | 48 | 3.0 | hero headlines |
| 6xl | 60 | 3.75 | landing-page hero |
| 7xl | 72 | 4.5 | display |
| 8xl | 96 | 6.0 | display, larger |
| 9xl | 128 | 8.0 | display, very large |

**Don't use em for the scale** — em compounds when nested. Use px or rem.

## Font weights

Two weights handle 95% of UI:
- **400** (regular) — body, secondary, tertiary text
- **600** (semibold) or **700** (bold) — emphasis, primary headings, labels you want noticed

Skip weights below 400 in UI body text. They're fine on very large display headlines if the typeface supports them well.

## Line height

Inversely proportional to font size, and proportional to line length.

| Font size | Line-height |
|---|---|
| Body (16–18px), normal width | 1.5 |
| Body, wide column | 1.6–2.0 |
| 20–24px (small headings) | 1.4 |
| 30–48px (medium headings) | 1.2 |
| 60px+ (display) | 1.0–1.1 |

## Line length

For long-form reading content: **45–75 characters per line** (~20–35em). Constrain prose width with `max-width` even if the surrounding content area is wider. Mixed widths in the same column look more polished than forcing prose to fill a wide layout.

## Color: a starter grey scale

Cool-tinted greys (slight blue) — a safe, modern default. Adjust hue toward yellow/orange for a warmer feel.

| Shade | HSL |
|---|---|
| 50 | `hsl(210, 20%, 98%)` |
| 100 | `hsl(214, 15%, 95%)` |
| 200 | `hsl(214, 13%, 90%)` |
| 300 | `hsl(213, 12%, 80%)` |
| 400 | `hsl(214, 10%, 65%)` |
| 500 | `hsl(215, 9%, 50%)` |
| 600 | `hsl(216, 11%, 38%)` |
| 700 | `hsl(217, 14%, 28%)` |
| 800 | `hsl(218, 18%, 18%)` |
| 900 | `hsl(220, 24%, 10%)` |

Notice saturation rises slightly at the extremes — that compensates for HSL's tendency to wash out near 0% / 100% lightness.

## Color: starter primary (blue)

| Shade | HSL |
|---|---|
| 50 | `hsl(214, 100%, 97%)` |
| 100 | `hsl(214, 95%, 93%)` |
| 200 | `hsl(213, 97%, 87%)` |
| 300 | `hsl(212, 96%, 78%)` |
| 400 | `hsl(213, 94%, 68%)` |
| 500 | `hsl(217, 91%, 60%)` |
| 600 | `hsl(221, 83%, 53%)` |
| 700 | `hsl(224, 76%, 48%)` |
| 800 | `hsl(226, 71%, 40%)` |
| 900 | `hsl(224, 64%, 33%)` |

Notice the **hue rotates** slightly across the scale — from cyan-tinted lights toward purple-tinted darks. This keeps the lighter shades feeling fresh and the darker shades feeling rich, instead of muddy. (See `color.md` for the why.)

Typical use:
- 50/100 — alert/info backgrounds, hover tints
- 500/600 — buttons, links
- 700/800 — text on light, hover-darken for buttons
- 900 — large headings or text-on-tint

## Color: semantic accents

| Role | Approx hue | Mid shade |
|---|---|---|
| Success | 145° (green) | `hsl(142, 71%, 45%)` |
| Warning | 38° (amber) | `hsl(38, 92%, 50%)` |
| Danger | 0° (red) | `hsl(0, 72%, 51%)` |
| Info | 200° (cyan) | `hsl(199, 89%, 48%)` |

Build 9 shades for each, same way: pick base, find darkest and lightest, bisect.

## Shadows / elevation system

Five levels. Each combines a soft larger shadow with a tighter darker one.

```css
/* xs — subtle separation, e.g. card on grey background */
box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);

/* sm — buttons, inputs */
box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1),
            0 1px 2px -1px rgb(0 0 0 / 0.1);

/* md — dropdowns, popovers */
box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1),
            0 2px 4px -2px rgb(0 0 0 / 0.1);

/* lg — sticky headers, hovered cards */
box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1),
            0 4px 6px -4px rgb(0 0 0 / 0.1);

/* xl — modals, dialogs */
box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1),
            0 8px 10px -6px rgb(0 0 0 / 0.1);

/* 2xl — large modals, important overlays */
box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25);
```

Inset shadow for inputs and wells:
```css
box-shadow: inset 0 1px 2px 0 rgb(0 0 0 / 0.05);
```

Notice the smaller dark shadow fades as elevation grows — at 2xl there's no occlusion shadow at all because the element is "far" from the surface.

## Border radius scale

| Token | px |
|---|---|
| none | 0 |
| sm | 4 |
| md | 8 |
| lg | 12 |
| xl | 16 |
| 2xl | 24 |
| full | 9999 (pills, avatars) |

Pick one radius value as your project's default, and stick with it. Mixing 4px corners with 16px corners in the same UI almost always looks worse than committing to one.

- **No radius** → serious, formal, editorial
- **Small (4–8px)** → neutral, professional default
- **Medium-large (12–16px)** → modern, friendly
- **Very large / pills** → playful, casual

## Z-axis (when you need it)

```
0    page background
10   sticky elements (sticky header)
20   dropdown / popover
30   sticky toast
40   modal backdrop
50   modal
60   tooltip
```

## Standard component sizing defaults

| Component | Defaults |
|---|---|
| Button (default) | h: 40px, padding-x: 16px, font: 14–16px, weight: 500–600, radius: 6–8px |
| Button (large) | h: 48px, padding-x: 20–24px, font: 16–18px |
| Button (small) | h: 32px, padding-x: 12px, font: 14px |
| Input | h: 40px, padding-x: 12px, font: 16px (avoid <16px on mobile to prevent iOS zoom) |
| Card padding | 24–32px (`6`–`8`) |
| Modal max-width | 480–640px depending on content |
| Reading column | max-width: 65ch (or ~640–720px) |
| Page side padding (mobile) | 16–24px |
| Page side padding (desktop) | 32–64px or auto-margin with max-width |

## Quick reference: when something looks off

| You think you need | Try instead |
|---|---|
| A bigger headline | Heavier weight at current size |
| A smaller subtitle | Lighter color at current size |
| A more colorful element | De-saturate everything around it |
| A lighter font weight (300) | Smaller size or lighter color |
| A border to separate two things | More space, or different background |
| A shadow to make it pop | Different background color from its container |
| Grey-on-color text that doesn't look dirty | Hand-picked color in the same hue as the background |
