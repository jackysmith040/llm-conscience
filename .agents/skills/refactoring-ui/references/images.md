# Working with images

A great UI with bad photos still looks bad. Most "this design feels off" problems involving images come from a few specific failure modes.

## Use good photos

Bad photos undermine everything else.

### Your two real options

1. **Hire a professional photographer.** If you need specific photos for your project (your team, your product, your space), pay someone who knows what they're doing. Good photography isn't about an expensive camera — it's lighting, composition, and color, which take years to develop.
2. **Use high-quality stock photos.** If your needs are generic (a person at a laptop, a landscape, an abstract texture), use high-quality stock. Unsplash and Pexels offer great free options; Stocksy and Death to Stock have curated paid catalogs.

### Don't design with placeholder photos

Placeholder photos are a trap. You design around the photo's color and composition, then later try to swap in your own photos and they don't fit. The design falls apart, and you blame the design when it was the original photo doing more work than you realized.

If you don't have real photos yet, **design without them**, leaving holes you can fill later — or use the *actual* stock photos you'll ship with.

## Text needs consistent contrast against images

Putting white text on a dynamic photo (lots of light areas and dark areas) is a guaranteed legibility problem — white pops against the dark areas and vanishes against the light ones. The reverse is true for dark text.

The problem isn't the text styling — it's the image. Reduce the image's dynamic range so the contrast is consistent.

### Add an overlay

The most common fix: a semi-transparent overlay on the image.

- **Dark overlay** (e.g. `rgba(0,0,0,0.5)`) → tones down the bright areas, letting white text sit consistently against a darker overall image.
- **Light overlay** → brightens the dark areas, letting dark text sit consistently against a lighter overall image.

```css
.hero {
  background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url(...);
}
```

### Lower the image's contrast

The overlay tones down the *whole* image, including the parts that didn't need it. For more control, **reduce the image's contrast** in your editor before exporting. Lower contrast → less dramatic difference between light and dark areas → text reads consistently.

Reducing contrast also reduces overall brightness, so adjust brightness up afterward to compensate.

### Colorize the image

Another option: convert the image to a single hue. This is a strong stylistic choice and ties images into your brand colors.

Three steps in any photo editor:
1. Lower the image's contrast.
2. Desaturate it (now it's greyscale).
3. Apply a solid fill in your brand color, using a "multiply" blend mode.

The result: a tinted image with consistent contrast, in a color that matches your design.

### Add a text-shadow as a glow

If you want to preserve the image's dynamics (e.g. it's a beautiful photo and an overlay would dull it), add a subtle glow behind the text. Use a large blur and **no offset** so it reads as a glow rather than a directional shadow:

```css
text-shadow: 0 0 12px rgba(0,0,0,0.5);
```

Combine with a slight contrast reduction and you get a polished result that still shows off the image.

## Everything has an intended size

Bitmap images obviously degrade when scaled up. But there's a less-obvious failure mode that applies even to vector assets: **assets are designed for a specific intended size**, and using them outside that size makes them look wrong even if the rendering is technically perfect.

### Don't scale up small icons

Most icon sets are drawn at 16–24px. The tiny shapes are tuned to read clearly at that size — they have minimal detail, thick relative strokes, and chunky proportions.

Blow them up to 64px or 128px and they look amateurish. They're vector, so they're sharp, but they look like an inflated version of a tiny icon — disproportionately chunky and lacking detail.

If you need a large icon and only have small ones, **enclose the small icon in a colored shape** (a circle, rounded square, or hexagon). The icon stays at its intended size; the shape fills the larger area you need:

```html
<div class="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center">
  <svg class="w-6 h-6 text-blue-600">...</svg>
</div>
```

This is also a useful pattern for "feature" sections on landing pages.

### Don't scale down screenshots

If you take a 1920x1080 screenshot and shrink it to fit a 300x200 box, you've crammed a 16px font into a 4px font. Visitors will be squinting at unreadable text, and the screenshot fails as a communication tool.

Fixes:
1. **Take the screenshot at a smaller screen size** (e.g. tablet layout) so less needs to fit. The text in the screenshot stays readable when displayed.
2. **Take a partial screenshot** — just the part that demonstrates what you want to show. Display it without scaling.
3. **Draw a simplified version** of the UI for your screenshot — replace small text with simple lines, remove inessential details. The visitor gets the big-picture impression without trying to read tiny text.

### Don't scale down icons either

Icons drawn for large sizes look choppy when shrunk. The most extreme example: shrinking a detailed 128px logo down to a 16px favicon — all the detail turns to mush as the browser tries to anti-alias it into 256 pixels.

Redraw a **simplified version** of the logo at the target size. You control the compromises (which strokes to keep, which to drop, what to round) instead of leaving them to the browser's renderer.

## Beware user-uploaded content

When users upload images, you don't get to fine-tune them. They'll have wildly varying aspect ratios, color profiles, brightness, and quality. You can still protect your design.

### Control shape and size

Don't display user images at their intrinsic aspect ratio in your layout. They'll wreck the page structure when an unusually tall or wide one appears.

Use a fixed container with consistent dimensions, and crop the image to fit:

```css
.user-avatar {
  width: 64px;
  height: 64px;
  object-fit: cover;
  object-position: center;
}
```

Or with a background image:
```css
background-size: cover;
background-position: center;
```

The center of the image is preserved (where the subject usually is); anything that doesn't fit is cropped.

### Prevent background bleed

If a user uploads an image whose background color matches your UI background, the image's edges disappear and the photo looks like it's bleeding into the page.

Don't use a border to fix this — borders clash with image colors and look heavy. Instead, use a **subtle inset box-shadow**:

```css
.user-image {
  box-shadow: inset 0 0 0 1px rgba(0,0,0,0.1);
}
```

It defines the edge clearly without competing with the image's content. Most users won't even notice it's there.

A semi-transparent inner border works too:

```css
.user-image {
  border: 1px solid rgba(0,0,0,0.1);
}
```

The point: there should always be **some visible boundary** between user-uploaded images and the UI behind them, even when the image's edges happen to match.
