---
name: i-am-impeccable
description: >-
  Natural-language router for Impeccable design commands: infers intent, presents up to 3 ELI5 choices,
  and delegates to design workflows. Trigger: /impeccable, /i_am_impeccable.
---

# /i-am-impeccable

**Alias**: `/impeccable`, `i_am_impeccable`

## What
Infers design intent from prompts or UI descriptions, presents up to 3 plain-language choices with ELI5 explanations, and waits for your selection before executing design improvements.

## Procedure
1. **Preflight**: Verify design context and current tokens.
2. **Classify**: Map user requirements to appropriate design action:
   - *Critique*: Audit aesthetics, layout, and visual hierarchy.
   - *Typeset*: Fix typography scale, line-heights, and font pairings.
   - *Polish*: Refine spacing, hairline borders, and micro-interactions.
   - *Bolder*: Elevate visual impact, contrast, and depth.
3. **Present + STOP**: Present max 3 options and wait for user confirmation.
4. **Execute**: Apply only confirmed styling transformations.
