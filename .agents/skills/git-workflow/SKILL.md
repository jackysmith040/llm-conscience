---
name: git-workflow
description: >-
  Canonical portable Git workflow for feature branches, pull requests, develop/main releases,
  and branch cleanup. Trigger: /git-workflow.
---

# /git-workflow

## Flow Overview
`feat/<slug>` -> PR -> `develop` (merge) -> delete `feat/*` -> PR -> `main` (merge) -> sync `develop`.

## Rules
1. **Branch Naming**:
   - Features: `feat/<short-slug>`
   - Bugfixes: `fix/<short-slug>`
   - Chores/Refactoring: `refactor/<short-slug>`
2. **Commit Hygiene**:
   - Atomic commits with clear descriptions.
   - Run tests and linters before committing.
3. **Pull Request Protocol**:
   - Provide summary of changes, rationale, and test evidence.
   - Run Rabit audit prior to PR submission.
4. **Post-Merge Cleanup**:
   - Delete local and remote feature branch after merge into develop.
   - Fast-forward or rebase develop to match main on release.
