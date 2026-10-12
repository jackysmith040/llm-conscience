---
name: graphify-ide
description: >-
  Custom graphify workflow running inline in IDE without API keys to extract semantic AST graphs
  and generate executable Python run scripts. Trigger: /graphify-ide.
---

# /graphify-ide

When `/graphify-ide` is invoked, follow this workflow:

## 1. No API Keys & Inline Semantic Extraction
Perform semantic extraction inline without requiring external API keys. Review core architectural documents and inject lightweight semantic metadata into the build process.

## 2. Generate Runnable Script (Do Not Auto-Execute)
Write a Python script (`run_graphify.py`) handling:
- Detection (`graphify.detect`)
- AST and structural extraction (`graphify.extract`)
- Merging inline semantic graph nodes
- Building interactive graph visualizer and reports

Present the terminal command for the user to execute (e.g. `python3 run_graphify.py`).
