# Hierarchy is everything

Most "I'm not a designer" UIs fail not because the colors are wrong or the font is bad, but because **everything has equal visual weight**. When every element competes for attention, the screen feels noisy and undesigned, even if the underlying styling is fine.

Visual hierarchy is the deliberate ranking of importance — what should the eye land on first, second, third? It is the single highest-leverage design skill, and it has very little to do with artistic talent.

## Not all elements are equal

Take any cluttered UI. Without changing the colors, fonts, or layout — just by **de-emphasizing secondary content** and emphasizing the primary content — it will look dramatically more designed.

Most elements on a page should *not* be screaming for attention. A few primary elements should. The rest should fade into the background, available when needed but not competing.

## Size isn't everything

The default instinct for hierarchy is to make important things bigger. This produces UIs where headlines are too big, body text is too small, and the relative scale feels cartoonish.

Better order of tools, in order of preference:

1. **Font weight** — bolder = emphasized. A bold 16px headline can outperform a regular 28px headline.
2. **Color contrast** — darker against light backgrounds = more emphasis. A mid-grey for secondary text emphasizes the primary text more than a smaller font size would.
3. **Size** — only after weight and color, and only as much as actually needed.

For most UI work, you only need:
- **2–3 text colors**: a dark grey for primary, a mid-grey for secondary, optionally a light grey for tertiary.
- **2 font weights**: regular (400 or 500 depending on font) for most text, semibold/bold (600/700) for emphasis.

Avoid font weights below 400 in UI work — they're hard to read at small sizes. If you're considering a 300 to "make it secondary", use a lighter color or smaller size instead.

## Don't use grey text on colored backgrounds

Grey works on white because grey *reduces contrast against white*. The same logic does not work against blue, green, or any saturated color.

Grey on a colored background looks dirty or washed out. Worse, white-with-reduced-opacity (e.g. `rgba(255,255,255,0.7)`) looks pale and dull, and if the background has any pattern or image behind it, the pattern shows through the text.

The fix: hand-pick a new color in the **same hue** as the background, then adjust saturation and lightness until it has the contrast you want. So instead of `text-color: rgba(255,255,255,0.6)` on a blue button, you'd use a slightly lighter, slightly less saturated blue tinted toward white.

This applies to icons, borders, and any de-emphasized element on a colored background — not just text.

## Emphasize by de-emphasizing

When something doesn't stand out enough, the wrong instinct is to push it harder — louder color, bigger size. Often it's already loud enough; the problem is everything around it is also loud.

Examples:
- An active nav item won't stand out if the inactive items are also high-contrast. **Soften the inactive items.**
- A primary CTA gets lost when there are three secondary buttons next to it. **Demote the secondaries to outlined or text styles.**
- Main content feels cluttered next to a sidebar. **Strip the sidebar's background color** so it sits on the page background.

This shift in mindset — making things prominent by quieting their neighbors — solves a huge fraction of layout problems.

## Labels are a last resort

A common mistake when displaying database-like data is the `Label: Value` format:

```
Email: jane@example.com
Phone: (555) 765-4321
Department: Customer Support
```

This gives every piece of data equal visual weight and makes the display feel like a form printout instead of an interface.

### You often don't need a label at all

Format and context usually identify the data:
- `jane@example.com` — obviously an email
- `(555) 765-4321` — obviously a phone
- `$19.99` — obviously a price
- "Customer Support" listed under someone's name — obviously their department

When you can omit the label, you're free to give the actual data the visual treatment it deserves.

### Combine labels and values

When the value alone isn't clear, fold the label into the value:
- ❌ "In stock: 12" → ✅ "12 left in stock"
- ❌ "Bedrooms: 3" → ✅ "3 bedrooms"

Now you have one piece of content to style, not two competing ones.

### Make labels secondary

When you really do need a label (multiple similar data points on a dashboard, for example), demote it: smaller, lighter color, lighter weight. The data is what matters; the label exists for clarity, not attention.

### When to make the label primary instead

Sometimes the user is scanning for the *label*, not the value. On a phone's spec sheet, the user is looking for "Battery" or "Display size", not "5,000 mAh" or "6.7 inches". Make the labels the primary text and the values secondary.

## Separate visual hierarchy from document hierarchy

Browsers default to making `<h1>` huge and `<h6>` tiny. That's fine for documents but misleading for app UIs. An `<h1>` is a semantic claim ("this is the main heading of this document"), not a visual claim ("this should be enormous").

Many section titles in apps are functionally **labels** — they tell you what region you're in, but they're support, not main content. Style them like supporting text. In the extreme, you can even visually hide the heading entirely (`sr-only`-style) for accessibility while letting the content speak for itself.

**Choose elements for semantics; choose visual styling independently.**

## Balance weight and contrast

Bold text feels heavier than regular text because it covers more pixels in the same space. The same logic applies to non-text elements:

### Icons are heavy

Solid-fill icons especially have a lot of "weight" — they cover surface area like bold text does. When you place an icon next to text, the icon often visually dominates the text even though it's the same size.

You can't change the "weight" of an icon directly, so balance by **lowering its contrast**: a softer grey instead of pure dark. The icon now sits beside the text instead of fighting it.

### Borders feel thin or harsh

A 1px border in a soft color often vanishes. A 1px border in a darker color feels harsh and noisy. The fix: increase the **width** to ~2px while keeping the soft color. More weight, no harshness.

The pattern: **weight and contrast trade off**. Heavy element + low contrast = balanced. Light element + high contrast = balanced. Heavy + high = overwhelming. Light + low = invisible.

## Semantics are secondary (for buttons)

Every page has a pyramid of actions: typically one true primary, a few secondaries, and several tertiaries. Designing all the buttons "by what they do semantically" instead of "by where they sit in the hierarchy" produces UIs where everything looks equally clickable.

Instead:

- **Primary action**: solid, high-contrast background. Use sparingly — one per visual region. (Save / Submit / Sign Up.)
- **Secondary actions**: outlined or low-contrast filled. (Cancel / Edit / Filter.)
- **Tertiary actions**: text-only, styled like a link. (Help / Skip / Maybe later.)

### Destructive actions

Destructive ≠ primary. If "Delete" is just one of several actions on a page, make it tertiary or a text button — possibly red, but quiet. The big, red, bold styling belongs on the **confirmation step**, where Delete actually *is* the primary action.

This avoids the very common "every dangerous action is a giant red button" UI, which trains users to ignore red buttons and dilutes their meaning.

---

Hierarchy is the highest-leverage thing you can fix on most underwhelming UIs. Run through every region and ask: which element here is primary? Which are secondary? Which are tertiary? Then style each accordingly. Most "this looks bad" problems dissolve.
