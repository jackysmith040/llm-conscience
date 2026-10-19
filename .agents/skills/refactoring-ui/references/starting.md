# Starting from scratch

When designing a new app, page, or feature, the order in which you make decisions has a huge effect on whether you get unstuck or end up paralyzed. This chapter is about that order.

## Start with a feature, not a layout

The single biggest mistake when starting a new design is asking "what should the app look like?" before asking "what does the app *do*?".

When most people start designing an app, they reach for the shell — top nav vs sidebar, logo on the left or center, full-width container or boxed. None of those questions can be answered well in the abstract. The shell exists to support the features; until you've designed at least one real feature, you don't know what the shell needs to support.

**Do this:** pick a single concrete piece of functionality and design it. For a flight booking site: design "search for a flight" as a self-contained block (departure field, destination field, date fields, search button). Once that's solid, the layout decisions ("does this need a top nav?", "where does the logo go?") become much easier — many of them turn out not to matter.

## Detail comes later

In early stages, do not get stuck on typeface, shadows, icon details, or color. They matter eventually but not now.

Tricks for staying low-fidelity early:
- **Sharpie on paper.** Jason Fried's trick. You physically cannot fuss over 1px decisions with a thick marker, so you focus on layout and structure.
- **Greyscale only.** Without color, you're forced to use spacing, contrast, and size to do the heavy lifting — which produces a stronger underlying hierarchy that color enhances later instead of papers over.
- **Treat sketches as disposable.** They exist to clarify a decision, then you throw them away and build the real thing.

The whole point of low-fidelity is to move fast. The moment you find yourself adjusting the curvature on a wireframe button, you've lost the plot.

## Don't design too much

Don't try to design every screen and edge case before you start building. It's tempting, because it feels safer, but it's a trap:

- You can't actually predict in advance what edge cases will matter.
- Issues that obvious in the real running interface are invisible in mockups.
- You'll burn time refining screens for features you might not even ship.

Instead, work in short cycles: design the next feature simply, build it, find the problems by using it, fix them, design the next one.

## Be a pessimist

When designing a feature, **don't imply functionality you aren't ready to build**. Say you're designing comments for a project tool, and you sketch in an attachments UI because "wouldn't it be cool to support attachments". You then go to implement and discover attachments are a week of backend work you can't justify right now. Now the entire comment system can't ship until you finish the attachment work — when it could have gone live without them and been useful.

Design the smallest version you can actually ship. Add features later. Keep the design honest about what's actually being built.

## Choose a personality

Every design has a personality, intentional or not. You can mostly control it via four levers:

### Font choice
- **Serif** → elegant, classic, editorial, formal
- **Rounded sans-serif** (e.g. Nunito, Quicksand) → playful, friendly, approachable
- **Neutral sans-serif** (e.g. Inter, system-ui) → clean, neutral, "professional"
- **Slab serif** → strong, confident, sometimes retro
- **Geometric / display** → bold, characterful, but use sparingly

### Color
- **Blue** is the safe default — trustworthy, familiar, "no one ever complains about blue".
- **Gold / amber** → expensive, premium, sophisticated.
- **Pink / magenta / coral** → fun, playful, approachable.
- **Green** → growth, finance, health (or relaxation/nature).
- **Black + single accent** → minimal, editorial, fashion.

Color psychology is overhyped, but the gut reactions colors evoke are real and worth deferring to.

### Border radius
This single value carries more personality weight than you'd expect.
- **No radius (0)** → serious, formal, structural, editorial.
- **Small (2–6px)** → neutral, doesn't push the design in any direction.
- **Medium-large (8–16px)** → modern, friendly.
- **Very large or pill-shaped** → playful, casual, sometimes toy-like.

**Stay consistent** — mixing square corners with rounded corners in the same interface almost always looks worse than picking one.

### Language
Words shape personality as much as visuals. "Are you sure you want to do this? This action cannot be undone." vs. "Heads up — this is permanent!". Both can work; pick one and commit. The voice in your microcopy is part of the design.

### How to actually pick a personality

You'll often have a gut feeling. If not, look at what other sites your target users use, and lean in a similar direction (without copying any one of them outright — you don't want to look like a second-rate clone of a competitor).

## Limit your choices

Without constraints, every minor decision is torture because there's always more than one right choice. "Should this be 12px or 13px? 14px or 15px?" None of those have a "right" answer in isolation, so you cycle through them indefinitely.

The fix: define **systems** with constrained sets of values, in advance.

- A type scale of, say, 11 sizes
- A spacing scale of ~12 values
- A color palette with 9 shades per color
- A shadow scale with 5 levels
- A radius scale with 3-4 options

Then, every design decision becomes a multiple-choice problem with 3–10 options instead of an open-ended one.

### Designing by process of elimination

Once you have a constrained set, picking is mechanical. Need an icon size? Suppose your scale offers 12, 16, 24, 32px. Pick the one that intuitively seems right (say 16) — then check 12 and 24 next to it. Usually two of the three will be obviously wrong; the remaining one is your answer. If 16 looks wrong, you now know whether you want to go bigger (24) or smaller (12), and you can repeat.

This isn't just faster; it produces more cohesive designs because everything snaps to a system.

### Systematize everything

Things to systematize early:
- Font sizes
- Font weights (~2 are enough)
- Line heights
- Colors (greys, primaries, accents — 9 shades each)
- Margin / padding values
- Width, height
- Box shadows / elevation
- Border radius
- Border width
- Opacity values

You don't have to pick every value before starting. The mindset matters more than the exhaustive list — every time you reach for an arbitrary value, ask if it should be added to a scale instead, so that future-you doesn't have to re-decide.
