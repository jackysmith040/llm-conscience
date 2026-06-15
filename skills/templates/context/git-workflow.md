# Git workflow (portable)

Copy this file into each repo as `context/git-workflow.md` (or `project-plan/context/git-workflow.md`). Copy [`../scripts/`](../scripts/) into the repo root as `scripts/` for PowerShell cleanup helpers.

**Manual merges on GitHub.** Agents implement on feature branches, push, and open PRs; **you** merge in the UI. Agents run branch cleanup **only after you confirm** a PR was merged.

## Branches

| Branch | Role | Delete? |
| ------ | ---- | ------- |
| `main` | Production-ready code | Never |
| `develop` | Integration / staging — default for all new work | Never |
| `feat/<slug>` | One ticket or cohesive change (e.g. `feat/ph6-001-deck-export`) | Yes, after merge into `develop` |

Use **`feat/<slug>`** with slashes (not `feat:slug`) — Windows-friendly.

```
main          ← you merge PR: develop → main (release)
  ↑
develop       ← you merge PR: feat/* → develop (daily integration)
  ↑
feat/ph6-001  ← agent work; deleted after merge
```

## Start feature work

```bash
git fetch origin --prune
git checkout develop
git pull origin develop
git checkout -b feat/<slug>
```

Work, commit, push:

```bash
git push -u origin feat/<slug>
```

Open a PR on GitHub: **base `develop`** ← compare `feat/<slug>`. Merge when ready (you).

## After you merge `feat/*` → `develop`

Tell the agent *"feat PR merged"* (or the branch name). Agent runs:

```powershell
.\scripts\git-cleanup-merged-feature.ps1 -Branch feat/<slug>
```

Or manually:

```bash
git fetch origin --prune
git checkout develop
git pull origin develop
git branch -d feat/<slug>
git push origin --delete feat/<slug>
```

## Release: `develop` → `main`

When staging is ready, open a PR: **base `main`** ← compare `develop`. Merge when ready (you).

## After you merge `develop` → `main`

Tell the agent *"release PR merged"*. Agent runs:

```powershell
.\scripts\git-sync-develop-after-main-merge.ps1
```

Or manually:

```bash
git fetch origin --prune
git checkout main
git pull origin main
git checkout develop
git merge main
git push origin develop
```

This keeps `develop` aligned with production. **Do not delete `develop`.**

## Agent rules

1. **Default branch for implementation:** `develop` (not `main`).
2. **Never** commit directly to `main` unless the user explicitly asks for a hotfix on `main`.
3. **Never** delete `main` or `develop` (local or remote).
4. **Always** delete merged `feat/*` branches (local + `origin`) after the user confirms the PR merge.
5. **Never** run cleanup before merge confirmation — avoid deleting work that was not merged.
6. One feature branch per ticket when possible; keep PRs small and reviewable.

## Remote

Record the project remote in `context/progress-tracker.md` (e.g. `origin` URL). **Default branch on GitHub:** `main` (production). **Integration branch:** `develop` (must exist on `origin`).

## PR titles (convention)

- Feature → develop: `feat: <ticket> — short description`
- Release → main: `release: merge develop into main` or milestone name
