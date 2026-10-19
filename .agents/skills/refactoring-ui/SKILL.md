---
name: refactoring-ui
description: "Apply the design principles from Adam Wathan and Steve Schoger's Refactoring UI book to build clean, professional, polished interfaces. Use this skill whenever building, refining, or critiquing any UI — web pages, components, dashboards, forms, landing pages, artifacts, mockups, marketing sites, app screens — even when the user does not explicitly ask for 'design help'. Trigger on cues like 'make this look better', 'why does this look amateur', 'design a [page/component]', 'build me a [dashboard/landing page/form]', 'style this UI', or any task that produces visual output where polish matters. The skill provides systematic rules for hierarchy, spacing, type scales, color palettes, depth/shadows, imagery, and finishing touches. Use it together with the frontend-design skill when bold aesthetic direction is also needed; this skill handles foundational craft, frontend-design handles distinctive visual character."
---

# Refactoring UI

A craft skill for designing interfaces that look professional and intentional, drawn from Adam Wathan and Steve Schoger's *Refactoring UI*. The book's core thesis: most "I'm not a designer" UIs fail not from lack of taste but from lack of **systems** and **hierarchy**. This skill encodes those systems into rules you can apply mechanically.

Use this skill anytime you produce visual output — HTML/CSS, React, SVG mockups, Tailwind components, design critiques. Even when the user says "just make it work", clean visual output costs almost nothing extra and immediately distinguishes the result.

## How to use this skill

The skill is organized so the SKILL.md gives you the high-impact rules you'll apply on almost every UI task. The `references/` folder has deeper chapter-by-chapter material. Read a reference file when:

- You're doing detailed work in that area (designing a color palette → `references/color.md`)
- Something looks wrong and you need diagnostic depth
- The user asks for a specific deep dive ("walk me through how to pick shadow values")

Reference files:
- `references/starting.md` — Starting from scratch, choosing personality, limiting choices
- `references/hierarchy.md` — The full hierarchy chapter; deeper than the rules below
- `references/layout.md` — Spacing system construction, grids, ambiguous spacing
- `references/typography.md` — Type scale construction, line length, alignment, letter-spacing
- `references/color.md` — HSL workflow, building a 9-shade palette, perceived brightness
- `references/depth.md` — Light source emulation, shadow systems, two-part shadows
- `references/images.md` — Photography, contrast on backgrounds, scaling pitfalls
- `references/finishing.md` — Empty states, accent borders, decorated backgrounds, fewer borders
- `references/cheatsheet.md` — Concrete starter values (type scale, color shades, shadows, spacing)

When in doubt about a specific decision, glance at `references/cheatsheet.md` first — it gives you working defaults so you don't stall.

## The mental model

Bad UIs come from making one decision at a time, in isolation, with infinite options. Good UIs come from **defining systems up front** and **picking from a small constrained set** every time you need a value. Every pixel value should come from a scale, every color from a palette, every shadow from an elevation system.

Hierarchy is the second pillar. Every element on a screen sits in a pyramid of importance. If everything looks equally important, the screen feels chaotic and undesigned. Your job is to deliberately emphasize a few things and **de-emphasize everything else**.

Almost every rule below flows from one of those two ideas.

## The rules

These are the highest-leverage rules from the book. Apply them by default on any UI task.

### 1. Start with a feature, not a layout

When designing a new app or page, do not start with the navbar, sidebar, logo, or container. Start with one concrete piece of functionality — the actual thing the user came to do. The shell only makes sense once you know what it has to contain. Dive into a real feature first; the layout decisions become obvious downstream.

### 2. Define systems before picking values

Before placing any element, have (or sketch) at least these scales:

- **Spacing/sizing scale** — non-linear, e.g. `4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512px`. No two adjacent values should be closer than ~25%.
- **Type scale** — hand-picked, e.g. `12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72px`.
- **Color palette** — 9 shades each for: greys, 1–2 primaries, plus accent colors (success/warning/danger as needed).
- **Shadow/elevation scale** — typically 5 levels from "barely raised" to "modal".
- **Border radius scale** — typically 3-4 values (e.g. `0, 4, 8, 16px`, plus full).
- **Font weights** — 2 weights for most UI work (400/500 normal, 600/700 emphasis).

Then **only pick from these scales**. If something doesn't look right with any value in the scale, the fix is rarely a new value — it's usually a different element of the design (spacing instead of size, weight instead of color, etc.).

`references/cheatsheet.md` has a complete starter system you can lift directly.

### 3. Hierarchy lives in weight, color, and size — in that order

Do not reach for font size first. Font size is the bluntest tool and easily becomes either too big (primary) or too small (secondary).

- **Primary content**: heavier weight (600/700), darker color, slightly larger size.
- **Secondary content**: regular weight, mid-grey color, similar or smaller size.
- **Tertiary content**: regular weight, light grey, often unchanged size.

Two or three text colors is enough for most UIs:
- Dark grey for primary text
- Mid grey for secondary
- Lighter grey for tertiary

Two font weights is enough. Skip weights below 400 in UI body text.

### 4. Emphasize by de-emphasizing

When something doesn't stand out enough, the instinct is to push it harder — bigger, bolder, more colored. Often the right move is the opposite: **soften everything around it**. Fade inactive nav items so the active one pops. Strip a sidebar of its background color so the main content breathes. Mute icons so they sit beside text instead of fighting it.

### 5. Don't use grey text on colored backgrounds

Grey-on-white works because grey reduces contrast against white. Grey-on-blue does not reduce contrast against blue — it just looks dirty. To de-emphasize text on a colored background, hand-pick a new color in the **same hue** as the background, then nudge saturation/lightness until contrast feels right. Do not use white-with-reduced-opacity either — it looks washed out and bleeds when there's a pattern behind.

### 6. Labels are a last resort

Don't lay data out as `Label: Value`. Most data is self-evident from format (`$19.99` is a price, `jane@example.com` is an email) or context. When you really need a label, **make it secondary** to the value (smaller, lighter), unless the user is specifically scanning for the label (e.g., spec sheets) — in which case make the label primary.

### 7. Separate visual hierarchy from document hierarchy

`<h1>` does not mean "big". It means "this is the document's main heading". Style heading tags however the visual hierarchy demands — section titles in apps are often closer to small labels than big headlines. Pick HTML elements for semantics; pick visual treatment independently.

### 8. Start with too much white space, then take some away

Do not add space until things look "okay". Start with way too much, then tighten. The sweet spot for an entire UI is usually further than any single component alone seems to want.

Whitespace is the cheapest single upgrade you can give a tired-looking UI.

### 9. Group with proximity; never with ambiguous spacing

When elements should feel grouped (a label and its input, a list of fields), **the space within the group must be smaller than the space around the group**. If both are equal, the eye gets no signal and the form feels broken. Same rule for headings to body text, list items, and horizontally-laid-out columns.

### 10. Don't let everything be full-width

Just because the screen is 1440px doesn't mean your form has to be. Give each element the width it actually needs. Login cards want ~400-500px regardless of viewport. A reading column wants 45–75 characters per line (~20–35em).

Corollary: **don't be enslaved to a 12-column grid**. Sidebars want fixed widths optimized for their content; the main area flexes around them. Cards have a max-width and stop growing past it.

### 11. Relative sizing doesn't scale

Do not wire the headline size to body size with `em`. The relationship that works at desktop (e.g. 2.5×) is wrong at mobile. Instead, set sizes independently per breakpoint. Bigger things shrink faster than smaller things on small screens; the *spread* between large and small text should be **less extreme** at smaller viewports.

Same idea inside components: button padding should not scale linearly with font size. Larger buttons want disproportionately more padding; smaller buttons want disproportionately less. Tune them independently.

### 12. Use HSL, not hex

In hex, `#3b82f6` and `#60a5fa` look unrelated; in HSL they're obviously the same hue at different lightnesses. HSL maps to how the eye actually sees color (hue / saturation / lightness), so adjustments are intuitive. Use it whenever you're picking or tweaking colors.

Note: HSL is in browsers; HSB is in design tools. They're not the same — `100% lightness` is white, `100% brightness` is the pure color at full saturation.

### 13. You need way more colors than five

Color generators that hand you "the 5 perfect colors" produce sites that look like color palettes, not products. A real palette has:

- **Greys: 9–10 shades.** Most of every UI is grey (text, backgrounds, borders, form controls). Don't use pure black — start from a very dark grey.
- **One or two primaries: 9 shades each.** Light tints for backgrounds (alerts, hover states), mid for buttons/links, dark for text-on-light or dense headlines.
- **Accent colors: 5–10 shades each, used sparingly** — typically success (green), warning (yellow), danger (red), plus any brand accents.

Build the palette by picking the base, then the lightest and darkest shades, then bisecting to fill in the rest. Trust your eye for tweaks; don't ship algorithmically-lightened/darkened shades — they'll all blur into each other.

### 14. As lightness → 0% or 100%, push saturation up

A color at `hsl(220, 80%, 50%)` looks vivid. The same hue at `hsl(220, 80%, 90%)` looks washed-out grey. The fix: as you go to lighter or darker shades, **raise the saturation** to keep the color feeling intentional rather than faded.

Alternative trick: instead of just changing lightness, **rotate the hue 10–20°** toward a brighter or darker neighboring hue (60°/180°/300° are the bright ones; 0°/120°/240° are the dark ones). A yellow's dark shade often wants to drift toward orange to stay rich, not toward muddy brown.

### 15. Greys aren't grey

Pure desaturated grey looks dead. Tint your greys: cool (blue-tinged) for technical/clean feels, warm (yellow/orange-tinged) for friendly/inviting feels. Even a tiny saturation (5–10%) is enough.

### 16. Never rely on color alone for information

Red-up / green-down arrows are unreadable to red-green colorblind users. Add an icon, a `+`/`–` sign, or contrast difference. For multi-line graphs, prefer different *line styles or weights* over color alone.

For accessible contrast (WCAG): body text on background ≥ 4.5:1; large text ≥ 3:1. White-on-color often needs the color to be much darker than feels comfortable — when that breaks hierarchy, **flip to dark-color-on-light-color** instead.

### 17. Light comes from above; emulate it

Want something to feel raised (a button)? Top edge slightly lighter, bottom shadow slightly dark, both subtle and tight. Want something to feel inset (a text input, a well)? Top inner shadow dark, bottom inner edge slightly light. That's the entire trick.

### 18. Shadows convey elevation; pick from a scale

Tight + small shadow = barely-raised (button). Medium = floating (dropdown). Large + diffuse = far-from-page (modal). Have ~5 named shadows in your system; pick one based on **how high you want the element to feel**, not by tweaking blur until it looks nice.

For more refined shadows, use **two layers**: one large soft shadow simulating cast light, one small dark shadow simulating ambient occlusion right under the edge. As elevation increases, the small dark shadow fades (further from the surface = less occlusion).

### 19. Even flat designs can have depth

If you're avoiding shadows, you can still imply layers:
- Make foreground elements *lighter* than the background (raised feel) or *darker* (inset feel).
- Use a **solid offset shadow** with no blur for a flat-graphic raised feel.
- **Overlap elements** across boundaries (a card straddling two background sections, controls that hang outside their container, an image protruding above the section it sits in). Overlapping creates layering for free.

### 20. Use good photos, at intended sizes

A bad photo torpedoes any layout. If you can't shoot, use Unsplash or pay a stock site. Don't design with placeholders thinking you'll swap in phone snaps later — the design will collapse.

Icons drawn for 16–24px will always look chunky at 64px+. If you need a big icon, **enclose the small icon in a colored shape** so it stays at intended size. Conversely, never shrink a 128px logo down to a 16px favicon — redraw a simplified version.

For text on hero images: lower the image's contrast first; then add an overlay (dark for white text, light for dark text); only then style the text. A subtle `text-shadow` (large blur, no offset) acts as a glow that lifts text against busy backgrounds without looking heavy-handed.

For user-uploaded images: enforce a fixed aspect ratio (`object-fit: cover`), and use a subtle inset box shadow or semi-transparent inner border to prevent backgrounds bleeding into your UI.

### 21. Buttons follow hierarchy, not semantics

Most pages have one true primary action, a couple of secondary actions, and a few tertiary actions. Style accordingly:

- **Primary**: solid, high-contrast background. Use sparingly — one per region.
- **Secondary**: outlined, or low-contrast background fill.
- **Tertiary**: text-only, styled like a link.

A "destructive" action (Delete) is not automatically a big red primary button. If it's not the page's primary action, it should be a tertiary or text button — **with the destructive primary styling reserved for the confirmation step**.

### 22. Don't overlook empty states, error states, and edge cases

The first time a user sees a feature, they see it empty. An empty list with the same chrome (filters, sort, tabs) but no rows looks broken. Hide irrelevant chrome on empty states; lead with an illustration or icon and a clear primary CTA. Treat the empty state as the introduction it actually is.

### 23. Use fewer borders

Borders are a habit. Try alternatives first:
- Different background colors between adjacent sections
- A subtle box shadow
- Just more space

Stripping borders is one of the easiest ways to make a busy UI feel calmer.

### 24. Supercharge the defaults

Cheap upgrades that disproportionately improve perceived polish:
- Replace `<ul>` bullets with icons (checkmarks, arrows, or topical icons like a padlock for a security list).
- Style your own checkboxes/radios in your brand colors instead of OS defaults.
- Add a colorful accent border to cards, alerts, active nav items, or headlines.
- Decorate flat backgrounds with a subtle pattern, gentle gradient (≤30° hue spread), or a simple geometric shape — keeping contrast low so it doesn't compete with content.
- Custom link underlines (thicker, colored, partially overlapping the text).

### 25. Think outside the box for stale components

Dropdowns, tables, radio groups all have "default" appearances that we copy reflexively. None of them have to look that way:
- Dropdowns can be multi-column, sectioned, with icons and descriptions.
- Tables can combine columns, mix text with images, color-encode values.
- Radio groups can be selectable cards with full descriptions.

When a component is central to your UI, ask whether the default treatment is doing the design any favors.

## A short workflow for any UI task

When given a UI task, walk through this order. It's not strictly linear, but each step prevents wasted effort downstream.

1. **Identify the one feature or content piece this screen/component is really for.** Design that. The shell can wait.
2. **Decide the personality** (one or two adjectives — calm/professional, lively/friendly, etc). Personality is mostly conveyed by font choice, color choice, and border radius. (`references/starting.md`)
3. **Lock in the systems** you'll use: spacing scale, type scale, color palette, shadow scale. Lift defaults from `references/cheatsheet.md` if you don't have your own.
4. **Establish hierarchy** for every region: which element is primary, which are secondary, which are tertiary? Use weight + color first, size last.
5. **Lay out with whitespace generously**, then tighten. Group with proximity; gaps within groups must be smaller than gaps between groups.
6. **Add depth** only where it serves hierarchy: shadows by elevation, lighter-than-background for raised, darker-than-background for inset.
7. **Polish**: empty/error states, accent borders, supercharged defaults, fewer borders, custom checkbox states. (`references/finishing.md`)

## Common diagnostics

When a UI looks "off" but you can't say why, run through these — they cover ~80% of issues.

| Symptom | Likely cause | Fix |
|---|---|---|
| Feels noisy / chaotic | Everything has equal hierarchy | De-emphasize secondary/tertiary content with lighter colors and lower weight |
| Headlines too big | Over-relying on size for hierarchy | Reduce size, increase weight |
| Looks washed-out / dingy | Lighter shades lost saturation | Bump saturation in light/dark shades; or rotate hue |
| Form feels disconnected | Equal spacing inside and between fields | Add more space between field groups than inside them |
| Cramped | Not enough whitespace | Increase padding everywhere first; tighten only where it then feels too loose |
| Sidebar competing with content | Sidebar has its own background | Remove sidebar background; let it sit on the page background |
| Greys feel "dead" | Pure grey, 0% saturation | Tint with 5–10% blue (cool) or yellow/orange (warm) |
| Text on photo unreadable | Image dynamics fight the text | Lower image contrast; add overlay; add subtle text-shadow glow |
| Icons feel heavier than the text next to them | Icons are surface-area-heavy | Lower the icon's contrast (softer color), don't shrink it |
| Buttons all look equally important | Styled by semantics not hierarchy | Pick one primary, demote the rest to outlined/text |

## When to lean on `references/cheatsheet.md`

If the user wants to move fast and isn't asking for a custom design system, just use the values in the cheatsheet. They're battle-tested defaults that match the book's recommendations and pair cleanly with Tailwind. Do not invent a new spacing scale or type scale on every project; lift the cheatsheet, then customize where you have a real reason to.

## Relationship to other skills

- **`frontend-design`**: Use both together for production frontend work. `frontend-design` chooses a *bold aesthetic direction* and distinctive personality; this skill applies the *foundational craft rules* underneath. They reinforce each other — the bold direction stays cohesive when its underlying scales, hierarchy, and systems are sound.
- **Document/slide skills (docx, pptx)**: Most of these rules carry over, especially hierarchy, type scale, color palette, and "labels are a last resort". Spacing systems are less applicable inside Word/PowerPoint, but the rest applies.

## A final note

This skill encodes rules, but design is judgment. The rules are right ~90% of the time and a good default to work from. When you knowingly break one, that's fine — just know which one and why. The failure mode is breaking them by accident.
