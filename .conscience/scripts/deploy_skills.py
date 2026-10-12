import os
import shutil
from pathlib import Path

workspace = Path(r"c:\Users\Fafa\Desktop\CodeSpace")
staging_dir = workspace / ".conscience" / "staging_skills"
conscience_skills_dir = workspace / ".conscience" / "skills"
agents_skills_dir = workspace / ".agents" / "skills"

print("Starting skill refinement and deployment...")

# 1. Update skill-creator
skill_creator_md = staging_dir / "skill-creator" / "SKILL.md"
if skill_creator_md.is_file():
    content = skill_creator_md.read_text(encoding="utf-8", errors="ignore")
    # Replace references to Manus with Antigravity / Conscience OS
    content = content.replace("extend Manus via specialized knowledge", "extend Antigravity and Conscience OS via specialized knowledge")
    content = content.replace("Manus", "Antigravity")
    skill_creator_md.write_text(content, encoding="utf-8")
    print("Refined skill-creator.")

# 2. Update applying-brand-guidelines
brand_md = staging_dir / "applying-brand-guidelines" / "SKILL.md"
if brand_md.is_file():
    content = brand_md.read_text(encoding="utf-8", errors="ignore")
    content = content.replace("Company: Acme Corporation", "Company: [Declared in BRAND.md or prompt]")
    content = content.replace('Tagline: "Innovation Through Excellence"', 'Tagline: [Declared in BRAND.md or prompt]')
    content = content.replace("Industry: Technology Solutions", "Industry: [Declared in BRAND.md or prompt]")
    brand_md.write_text(content, encoding="utf-8")
    print("Refined applying-brand-guidelines.")

# 3. Update beautiful-article
article_md = staging_dir / "beautiful-article" / "SKILL.md"
if article_md.is_file():
    content = article_md.read_text(encoding="utf-8", errors="ignore")
    # Provide clean frontmatter
    clean_frontmatter = """---
name: beautiful-article
description: >-
  Render user content (URL, PDF, DOCX, Markdown, plain text, or notes) into an offline-shareable,
  visually stunning single-file HTML article using responsive typography, clean layout, and rich styling.
---
"""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = clean_frontmatter + parts[2].lstrip()
    article_md.write_text(content, encoding="utf-8")
    print("Refined beautiful-article.")

# 4. Alias /grill to same-wavelength
grill_skill_md = conscience_skills_dir / "grill" / "SKILL.md"
if grill_skill_md.is_file():
    grill_alias_content = """---
name: grill
description: >-
  Alias for /same-wavelength. Actively grill the user before complex or ambiguous tasks to uncover
  assumptions, challenge flaws, and force explicit technical alignment. Trigger: /grill, /same-wavelength.
---

# /grill (Alias for /same-wavelength)

`/grill` is consolidated with `/same-wavelength`.

When triggered, immediately invoke the full **Same Wavelength** alignment interview:
1. Mirror user's intent.
2. Run grill blocks (Scope, Users, Architecture, Failure/Security, Done, Persona).
3. Challenge pass on hidden assumptions and feature creep.
4. Output Alignment Brief with locked decisions and wait for explicit confirmation.
"""
    grill_skill_md.write_text(grill_alias_content, encoding="utf-8")
    print("Aliased /grill to /same-wavelength.")

# 5. Move all 19 staged skills into .conscience/skills/
staged_folders = [p for p in staging_dir.iterdir() if p.is_dir() and p.name != "__pycache__"]
for folder in staged_folders:
    # Use folder name or skill name
    target_name = folder.name
    dest = conscience_skills_dir / target_name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(folder, dest)
    print(f"Deployed: {target_name} -> .conscience/skills/{target_name}")

# 6. Synchronize with .agents/skills/
agents_skills_dir.mkdir(parents=True, exist_ok=True)
for item in conscience_skills_dir.iterdir():
    if item.is_dir():
        d = agents_skills_dir / item.name
        if d.exists():
            shutil.rmtree(d)
        shutil.copytree(item, d)

print("Synchronized all skills to .agents/skills/!")

# 7. Remove staging directory
shutil.rmtree(staging_dir)
print("Cleaned up staging folder.")

print(f"Total deployed skills in .conscience/skills/: {len(list(conscience_skills_dir.iterdir()))}")
