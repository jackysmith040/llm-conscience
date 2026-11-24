#!/usr/bin/env python3
"""
Generates .conscience/skills.toml manifest by inspecting all 51 installed skills.
"""
import re
from pathlib import Path

skills_dir = Path(".conscience/skills")

domains = {
    "planning": [
        "same-wavelength",
        "grill",
        "to-spec",
        "to-tickets",
        "wayfinder",
        "architect",
        "prototype",
        "route",
        "icm-architect",
    ],
    "engineering": [
        "senior-stable-delivery",
        "pipeline",
        "rabit-auditor",
        "review",
        "recover",
        "git-workflow",
        "git-mode",
        "vibesec",
        "ponytail",
        "browser",
        "implement-spec",
    ],
    "craft": [
        "impeccable",
        "i-am-impeccable",
        "refactoring-ui",
        "color-palette",
        "emil-design-eng",
        "imprint",
        "nothing-design",
        "review-animations",
        "favicon-gen",
        "applying-brand-guidelines",
    ],
    "clarity": [
        "caveman",
        "ste-writing",
        "remember",
        "session-handoff",
        "the-basis",
        "retro",
        "skill-creator",
        "autopoiesis",
        "pace",
    ],
    "motion": [
        "gsap-plugins",
        "motion-first-learning",
        "visual-learning-software",
        "playground-builder",
        "excalidraw-diagram",
        "mermaid-visualizer",
        "beautiful-article",
    ],
    "specialized": [
        "financial-analysis",
        "stock-analysis",
        "excel-generator",
        "systematic-research",
        "graphify-ide",
    ],
}


def get_domain(name):
    for d, members in domains.items():
        if name in members:
            return d
    return "specialized"


def clean_desc(raw):
    raw = raw.strip().replace('"', "'")
    lines = [l.strip().lstrip(">-").lstrip(">").strip() for l in raw.splitlines() if l.strip()]
    cleaned = " ".join(lines)
    return cleaned[:140] if cleaned else "Specialized agent capability"


header = """# ==============================================================================
# Conscience OS Skills Dependency Manifest (skills.toml)
# Authoritative registry of all capabilities, domains, triggers, and metadata.
# ==============================================================================

[manifest]
version = "3.1.0"
last_updated = "2026-11-23"
total_skills = 51

[domains]
planning = "High-level discovery, specifications, decision mapping, and architectural breakdown"
engineering = "Production code delivery, testing, stability, security, and refactoring"
craft = "UI/UX design, visual engineering, tactile feedback, and anti-slop styling"
clarity = "Token compression, clean prose, session continuity, and conceptual study"
motion = "Interactive widgets, animations, diagrams, and visual simulations"
specialized = "Domain-specific tools for finance, spreadsheets, research, and graph extraction"

"""

body = ""
count = 0

for skill_folder in sorted(skills_dir.iterdir()):
    if not skill_folder.is_dir():
        continue
    name = skill_folder.name
    skill_file = skill_folder / "SKILL.md"
    desc = "Specialized agent capability"

    if skill_file.is_file():
        content = skill_file.read_text(encoding="utf-8", errors="ignore")
        if "description:" in content:
            raw_desc = content.split("description:")[1].split("---")[0]
            desc = clean_desc(raw_desc)

    dom = get_domain(name)
    body += f"[skills.{name}]\n"
    body += f'domain = "{dom}"\n'
    body += f'trigger = "/{name}"\n'
    body += f'summary = "{desc}"\n'
    body += "installed = true\n\n"
    count += 1

output_file = Path(".conscience/skills.toml")
output_file.write_text(header + body, encoding="utf-8")
print(f"[*] Generated {output_file} with {count} skills!")
