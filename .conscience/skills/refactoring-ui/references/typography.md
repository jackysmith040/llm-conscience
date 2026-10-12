# Typography

Typography problems are a top-3 source of "this UI looks amateur" feelings. Most of them are mechanical — once you know the rules, the problems are easy to spot and fix.

## Establish a type scale

Most UIs use far too many font sizes. Without a system in place, almost every pixel value from 10px to 24px ends up used somewhere. This produces inconsistency and slows you down (because you re-decide between 13px and 14px every time).

Define a constrained type scale and pick from it.

### Modular scales aren't ideal for UI

A modular scale uses a ratio (4:5, golden ratio, etc.) to generate sizes from a base. It's mathematically clean but has two problems for interface work:

1. **Fractional values.** A 16px base × 1.25 → 20, then × 1.25 → 25, then × 1.25 → 31.25, then 39.0625, etc. Browsers handle subpixel rounding differently, so fractional sizes can produce off-by-one inconsistencies. If you want a modular scale, round each value to whole pixels yourself.
2. **Wrong granularity.** Modular scales are good for long-form content (article body + 2-3 heading levels). For UIs you typically want more sizes, especially at the small end where a UI label, body text, lead paragraph, small heading, and big heading all want to be distinguishable.

### Hand-crafted scales are better for UI

Just pick the values by hand. A scale that works well for most projects:

```
12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72px
```

Constrained enough to speed decisions; granular enough to give you the size you actually want without compromise.

(Full table with rem equivalents and typical uses in `cheatsheet.md`.)

### Avoid em units in your scale

`em` is relative to the parent's font size. If you set `font-size: 1.25em` on an outer element and then `font-size: 0.875em` on a child, the child's computed size is `1.25 × 0.875 × base = 1.094 × base` — a value that probably isn't in your scale.

Stick to **px** or **rem** for type sizes. You stay in your scale.

## Use good fonts

Picking a typeface is intimidating because there are thousands. A few heuristics:

### Play it safe with system fonts

If you don't trust your taste, use the system font stack:
```
-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica Neue, sans-serif
```
Each OS uses its native UI font — users are used to seeing it, performance is great, no font loading.

For a slightly more designed feel, **Inter** is a popular safe default. (Don't over-use it though — it's become an "AI default" tell.)

### Filter by weight count

Typefaces with **5+ weights** (10+ when you include italics) are usually crafted with more care. On Google Fonts, this filter cuts ~85% of the catalog and leaves you with the well-made ones.

### Optimize for legibility at your sizes

Fonts are designed for specific use cases:
- **Display fonts** have tighter letter-spacing, shorter x-heights, and more decorative letterforms. They work great at large sizes and look cramped at small sizes.
- **Text fonts** have wider letter-spacing, taller x-heights, and simpler letterforms. They're readable at small sizes.

Don't use a display font for body copy. Don't use a text font for huge hero headlines (it'll look loose).

### Steal from people who care

Inspect the typography on sites you admire. Designers who care about type pick fonts you'd never find through "popular sans serifs" lists. This is one of the fastest ways to develop your own taste.

## Keep your line length in check

For paragraph text, the readable range is **45–75 characters per line** (roughly 20–35em). Lines longer than that make it easy for the eye to get lost when wrapping; lines shorter make reading feel choppy.

If your content area is wide (e.g. an article with images that span a wide column), it's fine to constrain just the paragraph text to the readable range while letting other elements be wider. Mixed widths in a column look more polished than forcing prose to fill the full layout width.

## Baseline, not center

When you have multiple font sizes on a single line (e.g. a card title in the top-left and a smaller list of actions in the top-right), aligning them by their **baseline** (the line letters sit on) almost always looks better than centering them vertically.

The reason: your eye perceives baselines naturally. Centered mixed sizes have offset baselines, which the eye reads as "off" — particularly when the sizes are close together.

In CSS this is `align-items: baseline` for flex containers, or just `vertical-align: baseline` for inline contexts.

## Line height is proportional, not constant

The "1.5 line-height" rule is a starting point, not a universal answer. Choose line-height based on:

### Line length

Wide lines need more space between them so the eye doesn't lose its place when wrapping. Narrow content can use shorter line-height (1.4–1.5); wide content might want as tall as 2.0.

### Font size

**Line height and font size are inversely proportional.** Small text needs more relative space; large text needs less.

| Font size | Line-height |
|---|---|
| 12–14px | 1.5–1.6 |
| 16–18px (body) | 1.5 |
| 20–24px | 1.4 |
| 30–48px | 1.2 |
| 60px+ | 1.0–1.1 |

A 60px hero headline at 1.5 looks loose and disconnected; at 1.0 it feels confident and tight.

## Not every link needs a color

Inside body text, links should pop — that's how readers know they're clickable. Color + underline works.

But in app UIs where **almost everything is interactive**, applying body-text-link styling to every clickable element is overwhelming. Instead:

- For most links in app contexts, use a slightly heavier weight or slightly darker color than surrounding text — much subtler than blue underlined.
- For ancillary links (footer, secondary), you can show no styling by default and only underline/color on hover. Discoverable without competing for attention.

The pattern: link styling intensity should be proportional to **how necessary it is for the user to immediately see** the link.

## Align with readability in mind

### Don't center long-form text

Centered blocks of text look great for headlines or short independent statements (a hero quote, a tagline). But once a block runs more than 2–3 lines, **left-aligned reads better** — your eye knows where each new line starts.

If you have several short centered blocks and one is slightly too long: rewrite it to be shorter rather than letting it ruin the alignment.

### Right-align numbers in tables

When a column is numeric, right-align the values. Decimal points line up; same-magnitude numbers visually share the same column. It's much easier to scan "is this number larger?" at a glance.

Left-align text columns; right-align numeric columns. Mixed columns (e.g. a price column with currency symbols) — right-align.

### Hyphenate justified text

Justified text (full edges on both sides) without hyphenation creates ugly word gaps. If you're going to justify, **enable hyphenation** (`hyphens: auto`). Justified text is rare on the web outside of print-emulating designs (online magazines); for most UIs, left-aligned is fine.

## Use letter-spacing effectively

Letter-spacing is the most often-forgotten typographic lever. The default rule: trust the typeface designer and leave it alone. But two cases warrant adjustment.

### Tightening headlines

Body fonts (e.g. Open Sans) have wide letter-spacing for legibility at small sizes. If you use a body font for big headlines, **decrease letter-spacing slightly** (`-0.02em` to `-0.04em`) to mimic the tight spacing of purpose-built display fonts.

Don't try the reverse — display fonts rarely work at small sizes even with looser letter-spacing.

### Improving all-caps legibility

Letter-spacing in most fonts is optimized for **sentence case** (one capital, rest lowercase). All-caps text loses the visual diversity that descenders (g, y, p) and ascenders (b, f, t) provide, so letters blur together.

For all-caps text, **increase letter-spacing** by ~0.05–0.1em. The "expanded" look is also why all-caps reads as label-like or formal — it's a stylistic signal, not just legibility.

```css
.uppercase-label {
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-size: 12px;
  font-weight: 600;
}
```
