# Creating depth

Depth in UI is about giving the user spatial cues — what's foreground, what's background, what's clickable, what's grouped. Done well, it makes interfaces feel tactile and easy to read. Done poorly, it produces "Web 2.0" gloss-and-bevel chaos.

The trick: **simulate light from one consistent source** and **use shadows to communicate elevation**, both with restraint.

## Emulate a light source

The reason a panel looks raised in real life is that:
- Its top edge is angled toward the sky → catches more light → appears lighter.
- Its bottom edge is angled away → less light → appears darker, plus casts a shadow below.

Insets are the opposite: top edge is in shadow (the lip above blocks light), bottom edge catches light (angled upward).

The single rule: **light comes from above.** Once you internalize that, shadows are no longer mysterious.

### Raised elements

To make something feel raised — a button, a card:

1. **Top edge slightly lighter** than the face of the element. A 1px lighter top border, or an inset box-shadow with a small positive vertical offset:
   ```css
   box-shadow: inset 0 1px 0 0 rgba(255,255,255,0.1);
   ```
2. **Bottom shadow slightly dark.** A small box-shadow with a positive vertical offset and a tight blur:
   ```css
   box-shadow: 0 1px 2px 0 rgba(0,0,0,0.1);
   ```

Don't use semi-transparent white for the top edge — it tends to suck saturation out of the underlying color and look chalky. Hand-pick a slightly lighter color in the same hue as the element.

For the dark shadow, **don't reach for huge blur radii**. Real-world shadows from low-elevation objects (a wall outlet, a window frame) have surprisingly tight, defined edges. A few pixels of blur is plenty.

### Inset elements

To make something feel recessed — a text input, a well, a checkbox:

1. **Bottom inner edge slightly lighter** (it's angled toward the sky). Inset shadow with negative vertical offset:
   ```css
   box-shadow: inset 0 -1px 0 0 rgba(255,255,255,0.1);
   ```
2. **Top inner edge slightly dark** (the lip above blocks light). Inset shadow with positive vertical offset:
   ```css
   box-shadow: inset 0 1px 2px 0 rgba(0,0,0,0.1);
   ```

The combination is what sells it.

### Don't get carried away

Once you understand light simulation, it's tempting to layer effects until your UI looks photo-realistic. Don't. The real-world cue should be a whisper — enough to make the element feel tactile, not enough to draw attention to the rendering.

## Use shadows to convey elevation

Shadows aren't just decoration. They tell the user **how far an element is from the surface** — i.e., where it sits on a virtual z-axis. The closer to the user, the more attention-grabbing.

### Map shadow size to elevation

| Elevation | Use case | Shadow profile |
|---|---|---|
| Barely raised | Subtle card on a grey background | Tiny, 1px offset, almost no blur |
| Low | Buttons, inputs, default cards | Small, ~2-3px blur, ~1-2px offset |
| Medium | Dropdowns, popovers, hover-raised cards | Medium, ~6-10px blur, ~4-6px offset |
| High | Modals, dialogs, command palettes | Large, ~15-25px blur, ~10-20px offset |
| Maximum | Full-screen overlays, important popovers | Very large, soft, possibly with backdrop |

(See `cheatsheet.md` for concrete CSS values.)

### Build a 5-level elevation system

Define your shadow scale up front, like everything else. Five levels handles almost everything. Start by defining the smallest and largest shadows; fill in three more between them, increasing relatively linearly.

Then style components by **picking from the scale** — "this dropdown is elevation 3" — instead of tweaking shadow values inline.

### Combine shadows with interaction

Shadows are great for showing state changes:

- **Drag handle**: when the user clicks-and-holds an item to reorder, raise it (larger shadow). Now it visually pops out of the list and the user knows it's "in their hand".
- **Button press**: switch to a smaller shadow (or remove it entirely) on `:active`. Feels like the button is being pushed into the page.
- **Card hover**: bump elevation by one step on hover. Subtle but conveys "interactive".

Choose shadows by where you want the element to **feel on the z-axis**, not by tweaking until it looks nice in isolation.

## Shadows can have two parts

Many polished shadows in the wild are actually two stacked shadows. There's a method, not random stacking.

### The two roles

**Shadow 1: cast shadow.**  
Larger, softer, with significant vertical offset and large blur radius. Simulates the shadow cast on the surface behind the object by a direct light source — a soft, diffuse projection.

```css
0 4px 8px rgba(0,0,0,0.08)
```

**Shadow 2: ambient occlusion.**  
Tighter, darker, less vertical offset, smaller blur. Simulates the dark shadow right under the object's edge where ambient light has trouble reaching — the contact shadow.

```css
0 1px 2px rgba(0,0,0,0.12)
```

Combined:
```css
box-shadow: 0 4px 8px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.12);
```

The cast shadow feels light and atmospheric; the ambient shadow defines the element's edge. With one shadow alone, you usually have to compromise — soft enough to be subtle, but then the edge isn't crisp; or sharp enough to define the edge, but then it's heavy.

### Account for elevation

The ambient occlusion shadow exists because the element is *close* to the surface. As the element gets further from the surface, ambient light has more chances to fill in under it — the dark contact shadow fades.

So in your elevation system:
- **Lowest elevation**: distinct ambient shadow + small cast shadow.
- **Highest elevation**: cast shadow only; ambient shadow gone or invisible.

This is how the book's cheatsheet shadows work — the dark layer fades as the cast layer grows.

## Even flat designs can have depth

"Flat design" doesn't mean "no depth". It means avoiding lighting effects (shadows, gradients, bevels). You can still convey layers and elevation in a flat aesthetic:

### Use color value for distance

Generally, **lighter elements feel closer**, **darker elements feel further**. Make foreground elements lighter than the background to imply they're raised; darker than the background to imply they're inset/recessed.

This is true regardless of the overall color scheme — within shades of the same color, lighter reads as closer.

Apply this to non-flat designs too — lighter buttons on darker headers, darker tinted backgrounds for "inset" content sections.

### Use solid offset shadows

A short, fully solid shadow with no blur creates a flat-aesthetic raised feel:

```css
box-shadow: 4px 4px 0 0 #1a202c;
```

It's graphic, illustrative, and very different from realistic shadowing. Pairs well with brutalist, retro, or playful designs.

## Overlap elements to create layers

One of the most powerful (and underused) ways to create depth: have elements **straddle the boundaries** of their parent containers.

### Overlap across backgrounds

A common pattern: a hero section with one background color flowing into a content section with another. Instead of containing a featured card *entirely* inside one or the other, position it to span the boundary — half above, half below the transition.

The card is now visibly in front of *both* background sections. The layering is unambiguous; the design feels architectural.

### Overlap within parents

- A hero image taller than its parent section, peeking above and below.
- Carousel arrow controls positioned outside the carousel's edges.
- A profile avatar half-overlapping its container's top border.
- A pricing card slightly taller than its peers in a row, overflowing above.

These small overlaps turn static-feeling rectangles into layered, three-dimensional compositions for almost no cost.

### Overlapping images need spacing

If you overlap multiple images directly, their edges clash and the composition feels muddy. Trick: give each image an "invisible border" — a few pixels of border in the **same color as the background**.

```css
img { border: 4px solid var(--bg); }
```

The visual gap between overlapping images cleans up the composition without breaking the overlap effect.

This works for any element where overlapping creates clashing — give them a same-as-background border to insulate them.
