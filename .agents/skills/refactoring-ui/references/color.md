# Working with color

Color is where most UIs go from "okay" to "actually professional". The trick isn't artistic talent — it's having a real palette and understanding the HSL color space.

## Ditch hex for HSL

Hex (`#3b82f6`) and RGB don't map to how your eye perceives color. Two hex codes that are visually similar can look totally different in code; two that look related in code can be wildly different colors.

**HSL** uses three attributes the eye actually uses:

- **Hue** — the color's position on the color wheel (0–360°). 0° = red, 60° = yellow, 120° = green, 180° = cyan, 240° = blue, 300° = magenta. Two colors with similar hue feel like the same color even at different lightness.
- **Saturation** — how vivid (0–100%). 0% = pure grey (no color), 100% = maximum vividness. Without saturation, hue is irrelevant.
- **Lightness** — how close to black or white (0–100%). 0% = pure black, 100% = pure white, 50% = the pure color at that hue.

When you adjust hue/saturation/lightness, the result is what you'd expect. When you adjust hex, you're guessing.

### HSL ≠ HSB

Design tools usually use **HSB (Brightness)**; browsers use **HSL (Lightness)**. They're different:
- In HSB, 100% brightness is the *pure color* at full saturation. White is hue-independent at 0% saturation, 100% brightness.
- In HSL, 100% lightness is *always pure white*, regardless of hue or saturation.

If you're designing for the web, work in HSL.

## You need way more colors than you think

Color palette generators that hand you "5 perfect colors" are useless for product work. You can't build a real interface with 5 hex codes. You need:

### Greys: 9–10 shades

Most of an interface is grey. Body text, secondary text, tertiary text, borders, dividers, panel backgrounds, page backgrounds, button backgrounds, disabled states, form controls, chrome — the list is long.

Three shades of grey isn't enough. You'll constantly want something between #1 and #2, or a touch lighter than #3.

Don't use **pure black** for your darkest grey — it looks unnatural on screen. Start from a very dark grey (something like 8–12% lightness) and step up.

### Primary color(s): 9 shades

The color users associate with your brand — Facebook blue, Stripe purple, etc. You need:
- 1–2 ultra-light shades for tinted backgrounds (alert backgrounds, hover states)
- 1–2 mid-light shades for hover/focus tints
- A mid shade for buttons and primary actions
- A few darker shades for hover/pressed states, dense headings, and text-on-tint

### Accent colors: 5–10 shades each

For semantic states and supporting flair:
- **Success** (green) — confirmations, positive trends
- **Warning** (yellow/amber) — caution states
- **Danger** (red) — destructive confirmations, errors
- **Info** (cyan/blue) — neutral notifications
- Plus brand accents for highlighting features, charts, tags, calendar categories, etc.

You'll have at least 60–100 colors in a real palette. That sounds like a lot until you start building and realize each one has a job.

## Define your shades up front

Don't generate shades on the fly with `lighten()`/`darken()` functions in your CSS preprocessor. You'll end up with 35 nearly-identical blues that all read as "the same blue" and bloat your design.

Build the palette intentionally:

### Step 1: Pick the base color

The middle shade — the one your other shades are based on. For a primary or accent color, pick a shade that would work well as a button background. Trust your eye; there's no "start at 50% lightness" rule.

### Step 2: Find the edges

Pick your **darkest** shade and **lightest** shade.
- Darkest is usually for text on the lightest tint, or for dense headings against a pale tint background.
- Lightest is usually for tinted backgrounds (alert backgrounds, hover states).

A simple alert component is a great test bed — the dark text on light-tinted background uses both extremes.

Start from your base color's hue, then adjust saturation and lightness for each end until they look right.

### Step 3: Bisect to fill in the gaps

If you label darkest as 900, base as 500, lightest as 100 — pick 700 (between 500 and 900) and 300 (between 100 and 500). Each should feel like a perfect compromise between its neighbors.

That gives you 5 shades. Bisect again to get 800, 600, 400, 200 → 9 shades total.

Nine is a great number because it bisects cleanly. Use the conventional 50/100/200/.../900 naming so others can read your palette at a glance.

### What about greys?

Same process. The "base" matters less for greys (it's just a midtone). Start by picking the darkest grey (your darkest text color) and the lightest grey (a subtle off-white background). Bisect.

### Don't be a slave to math

A systematic approach gets you most of the way. Once you start using the colors in actual designs, you'll want to tweak — bump saturation on shade 100, make 800 a touch darker, etc. Trust your eyes over the algorithm.

But: don't add new shades casually. If you're not strict about your palette, you don't really have one.

## Don't let lightness kill your saturation

In HSL, as lightness approaches 0% or 100%, **saturation has less effect**. The same `saturation: 80%` value at 50% lightness produces a vivid color; at 90% lightness, it produces something washed-out and grey.

To keep light/dark shades feeling colorful instead of muddy:

> As lightness moves away from 50% (in either direction), **increase saturation**.

A typical scale might look like:
- Shade 500 (50% lightness): saturation 85%
- Shade 300 (75% lightness): saturation 90%
- Shade 100 (95% lightness): saturation 100%
- Shade 700 (35% lightness): saturation 80%
- Shade 900 (15% lightness): saturation 70%

Subtle, but it keeps the palette feeling intentional rather than washed out. This is especially important for shades that cover large areas (button backgrounds, tinted alerts).

## Perceived brightness — and rotating hue to compensate

Two colors with identical HSL "lightness" can look different brightnesses. A pure yellow (60°, 100%, 50%) looks much lighter than a pure blue (240°, 100%, 50%) even though their HSL lightness is the same. Why?

**Every hue has an inherent perceived brightness.** Yellow is intrinsically bright; blue is intrinsically dark. The bright hues are roughly 60° (yellow), 180° (cyan), 300° (magenta). The dark hues are 0° (red), 120° (green), 240° (blue).

You can use this. Instead of (or in addition to) changing lightness, you can change perceived brightness by **rotating the hue**.

### To make a color lighter

Rotate the hue toward the nearest bright hue (60°, 180°, or 300°). For example, a blue (240°) lightens nicely if you rotate toward 300° (magenta) — your light blues drift slightly toward periwinkle, and they feel fresh instead of washed-out.

### To make a color darker

Rotate the hue toward the nearest dark hue (0°, 120°, or 240°). A yellow (60°) darkens richly if you rotate toward 0° (red) — your dark yellows become orange and amber rather than muddy olive-brown.

Practical example: when building a yellow scale, the dark shades should drift toward orange/red, not just lower in lightness, or they look like dirty mustard. When building a green scale, the light shades can drift toward cyan/yellow, the dark shades toward blue/teal.

**Don't rotate too far** — more than 20–30° and it looks like a different color, not the same color at a different brightness.

You can combine: get some brightness change from the hue rotation, the rest from lightness adjustment.

## Greys don't have to be grey

Pure desaturated grey (saturation: 0%) looks dead. Most "greys" in well-designed UIs have a small amount of saturation — that's what makes some greys feel cool and others feel warm.

### Color temperature

- **Cool greys** — saturated with a tiny amount of blue (hue ~210–220°, saturation 5–15%). Feel clean, technical, modern.
- **Warm greys** — saturated with a tiny amount of yellow/orange (hue ~30–45°, saturation 5–10%). Feel friendly, inviting, organic.

Match the temperature of your greys to the temperature of your primary color and overall feel.

To keep temperature consistent across the scale, **bump saturation a bit at the extremes** (just like with primary colors above), so the lightest and darkest greys don't drift toward neutral.

How saturated to go is up to you — even 5% is enough to tip the temperature; 15–20% gives a strongly tinted feel.

## Accessible doesn't have to mean ugly

WCAG recommends:
- Body text (under ~18px): contrast ratio ≥ **4.5:1** against background.
- Large text (≥18px or ≥14px bold): contrast ratio ≥ **3:1**.

For typical dark-on-light, this is easy. It gets tricky with color.

### White text on colored backgrounds

To meet 4.5:1 with white text, the background often needs to be **much darker** than feels natural — sometimes too dark for the visual weight you wanted (a navbar shouldn't necessarily be black-blue).

If a dark colored background fights your hierarchy: **flip the contrast**. Use **dark colored text on a light colored background** instead. The color is still present (the bg-tint), but the element doesn't shout.

This is why "tinted alert" components work so well — light coloured background, dark coloured text, both in the same hue. Plenty of accessibility, no visual heaviness.

### Colored text on colored backgrounds

Need secondary text inside a dark coloured panel? Adjusting only saturation and lightness, you'll find it hard to hit 4.5:1 without ending up almost white.

Trick: **rotate the hue toward a brighter hue** (cyan, magenta, yellow). The rotated hue gets contrast from its inherent brightness, not from getting closer to white — so the text stays colorful and intentional. (Same trick as the earlier brightness-via-hue-rotation; useful here for accessibility specifically.)

## Don't rely on color alone

Color reinforces information; it should rarely be the only carrier.

- **Red-down / green-up arrows** → unreadable for red-green colorblind users. Add a `+`/`–` sign or distinct icon.
- **Multi-line graphs in different colors** → hard to distinguish for many. Use different line styles, weights, or contrast as a secondary signal.
- **Form fields highlighted only in red on error** → add an icon and explicit error text.

A useful test: imagine the UI in greyscale. Is the information still clear? If not, color is doing too much work alone.
