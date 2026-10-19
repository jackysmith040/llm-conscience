# Layout and spacing

Most layout problems aren't actually layout problems — they're spacing problems. This chapter covers the systems and rules that fix the majority of "this feels off" issues.

## Start with too much white space

The default failure mode when designing for the web is **adding** white space — you build something tight, decide it looks cramped, and add a few pixels of padding until it doesn't look bad. The result: every element gets just enough breathing room to not look actively broken, which is far short of what a polished UI needs.

A better approach: **start with way too much space, then remove it until you're happy**. What looks like "a little too much" on an isolated component usually ends up being "just right" in the context of a full page.

White space is the cheapest and most universally effective polish you can apply. If you only do one thing to clean up a tired-looking UI, increase the spacing.

### When dense UIs are correct

There are real cases where density is the right answer — dashboards displaying lots of information at once, data tables, professional tools. Dense is fine when it's a deliberate choice, not the default. Make the call consciously.

## Establish a spacing and sizing system

Stop arguing with yourself between 120px and 125px. Use a constrained scale.

### A linear scale doesn't work

"Make everything a multiple of 4px" sounds disciplined but doesn't help — you can still pick any multiple of 4 you want, so 120, 124, and 128 are all "valid" and you're back to picking between them.

### Adjacent values must be ~25% apart

For a scale to actually constrain decisions, **the relative difference between adjacent values must be perceptible**. At small sizes, 12px to 16px is a 33% jump — clearly different. At large sizes, 500px to 520px is a 4% jump — invisible. So a useful scale is **non-linear**: tightly packed at the small end, increasingly spread out at the large end.

A practical scale, starting from 16px as the base:
```
0, 1, 2, 4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512
```

(See `cheatsheet.md` for the full scale and typical uses.)

### One scale for everything

Use the same scale for padding, margin, gap, and (for many things) width and height. The pieces of your UI will end up in subtle proportional relationships you didn't have to design — they just emerge from sharing a system.

## You don't have to fill the whole screen

Modern displays give you 1400px+ to work with. That doesn't mean you have to use 1400px.

If a login card is best at 480px, use 480px on a 1920px display. Stretching it to 800px makes it harder to scan, not better. If a sidebar is best at 280px, use 280px regardless of viewport. Padding-around-elements is free to be generous; not every container has to push outward to its parent.

This applies inside layouts too: sub-sections don't all have to be full-width just because the parent is. Give each piece the width it actually needs.

### Shrink the canvas

Designing a small UI inside a huge canvas is harder than designing it inside a small canvas. If you're working on something compact, shrink your design surface to ~400px and design mobile-first. Once it's solid, scale up to desktop and make adjustments — usually fewer than you'd expect.

### Thinking in columns

If a piece of UI is best at a narrow width but feels lonely in a wide space, **don't make it wider** — break it into columns instead. A narrow form with a column of supporting text/illustrations next to it feels balanced and uses the space without compromising the form's optimal width.

### Don't force it

Conversely, don't compress everything to fit a small space if the content really does want room. Let big things be big, small things be small.

## Grids are overrated

A 12-column grid is a useful tool for some layout decisions. It is not a religion, and outsourcing all your layout choices to it produces UIs that feel rigid and oddly proportioned.

### Fluid widths aren't always right

A grid system gives elements **percentage-based widths** chosen from a constrained set. That's appropriate when the element's optimal width really does depend on the viewport.

It's not appropriate when the element has its own intrinsic optimal width. Examples:

- **Sidebars** want a fixed width optimized for their content. Making a sidebar 25% means it bloats on wide screens (wasting space the main content could use) and shrinks below readable widths on narrow screens.
- **Cards / login forms** have an optimal width (often 400-500px). Below that, content cramps; above that, lines get too long and it looks bloated.

### Don't shrink an element until you have to

Suppose your login card is 6 columns (50%) on large screens. On medium screens, the card looks too narrow, so you bump it to 8 columns. There's now a viewport range where the card is *wider* on medium screens than on large screens, because percentages are confusing.

Better: pick the optimal width (e.g. 480px), give it `max-width: 480px`, and only let it shrink when the viewport itself drops below that.

**Use grids where they help. Don't be a slave to them.**

## Relative sizing doesn't scale

It's tempting to define everything relative to everything else, on the theory that resizing one thing rescales the whole UI nicely. It almost never works.

### Across breakpoints

If your headline is 2.5× your body text on desktop (45px headline / 18px body), and you reduce body text to 14px on mobile, you'd get a 35px headline — way too big for a small screen. The right mobile headline is more like 20-24px, which is a totally different ratio (1.5×, not 2.5×).

The lesson: **define sizes independently per breakpoint**, not relative to each other. Larger elements need to shrink more than smaller elements; the spread between large and small text should be **less extreme** at smaller viewports.

### Within components

If a button has 16px font and 12px vertical padding, it's tempting to define padding as `0.75em` so larger buttons scale proportionally. Try it: a "large" button at 24px font would have 18px padding, and a "small" button at 12px would have 9px padding. Both look weird because the proportion was right for the medium size and nothing else.

Real buttons want disproportionately *more* padding at large sizes (a big button feels generous and roomy) and disproportionately *less* at small sizes (a small button feels tight and tappable). Tune them independently.

**Don't conflate "scale" with "stay proportional". Things should resize independently.**

## Avoid ambiguous spacing

When elements share space without an explicit separator (no border, no background change), the **only signal** for grouping is the spacing itself. The rule:

> Space within a group must be smaller than space around the group.

If the gap between a label and its input equals the gap between successive form fields, the form has no visual structure — labels could attach to inputs above or below, and the eye has to work to figure out which.

Same problem appears in:
- **Headings vs body text**: not enough space above a section heading and it merges with the text above; readers can't tell where one section ends and the next begins.
- **List items**: bullets spaced by the same amount as line-height inside a single bulleted item make multi-line bullets look like one big run-on.
- **Horizontal layouts**: cards in a row need more horizontal space between them than between the contents within each card.

This is one of the simplest, most universally applicable rules in design — and it's violated everywhere. Every form, list, and grouped layout should pass the proximity test.
