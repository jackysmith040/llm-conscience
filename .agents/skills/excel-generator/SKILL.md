---
name: excel-generator
description: >-
  Professional Excel spreadsheet creation with a focus on aesthetics and data analysis.
  Use when creating spreadsheets for organizing, analyzing, and presenting structured data.
---

# Excel Generator Skill

[STATE: MOTOR_EXECUTION | INTENT: CRAFT_POLISH | PACE: STANDARD]

## Goal & Core Principles
Create spreadsheets that allow the user to gain instant insights upon opening. Enrich visuals meaningfully while ensuring content clarity without cognitive burden.

> **Precedence Note**: For finance/valuation/modeling deliverables (DCF, LBO, comps, 3-statement models, DD trackers), defer to finance-pro-playbooks. This skill governs general-purpose spreadsheets.

## 4-Step Build Workflow
1. **Analyze Needs**: Define user questions, primary metrics, and key decisions the sheet informs.
2. **Layout & Hierarchy**:
   - Multi-sheet workbooks MUST have an **Overview / Summary sheet** first.
   - Use freeze panes on headers, pre-sorting for high-value rows, and consistent number formatting (currency, percentages, dates).
3. **Visual Cues & Data Bars**:
   - Use soft, functional color palettes (never harsh primary saturations).
   - Add data bars or sparklines for quick at-a-glance magnitude comparison.
   - Dedicate a callout section for **KEY INSIGHTS**.
4. **Validation**: Test formulas, verify relative references, ensure zero `#DIV/0!` or `#VALUE!` errors.

## Reference Pointer (Progressive Disclosure)
> 📊 **Theme Palettes, Typography Scales & Formula Patterns:**  
> Load only when implementing deep formatting or chart templates:  
> `→ see .conscience/skills/excel-generator/references/excel_design_system.md`
