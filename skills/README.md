# Context methodology — skill suite

Copy this folder into any repo (e.g. `project-plan/templates/context_methodology/` or `.cursor/skills/` pointers).

| Skill | Folder | Invoke when | Auto-suggest? |
|-------|--------|-------------|---------------|
| **I am impeccable** | `i-am-impeccable/` | UI/design work; `/impeccable` without a command; say `i_am_impeccable` | Yes on design signals — **confirm required** |
| **Senior stable delivery** | `senior-stable-delivery/` | Implementing or reviewing work; plan + pre-PR Rabit pass | No — user-invoked |
| **Same wavelength** | `same-wavelength/` | You say “same wavelength” — align scope, architecture, persona before coding | No — user-invoked |
| **Session handoff** | `session-handoff/` | Ending a session — compact continuation for human + next agent | No — user-invoked |

**Shared impact:** You describe problems in plain language; each intelligent skill infers intent, shows up to 3 ELI5 choices, and waits for your pick before executing.

**Shared harness:** [_harness/intent-router.md](_harness/intent-router.md) — mirror → signal scan → classify → present + STOP → delegate.

**Layout:** Laravel-first core in `senior-stable-delivery/`; stack appendix optional per project.

## Git workflow

Portable guide: [`templates/context/git-workflow.md`](templates/context/git-workflow.md) · index: [`git-workflow.md`](git-workflow.md)

Copy into each repo as `context/git-workflow.md`. Copy [`templates/scripts/`](templates/scripts/) to repo `scripts/` for post-merge cleanup.

**Flow:** `feat/<slug>` → PR → `develop` (you merge) → delete `feat/*` → PR → `main` (you merge) → sync `develop`.

## Install

### Impeccable (upstream design commands)

```bash
npx skills add pbakaus/impeccable
```

Installs to `.agents/skills/impeccable/`. Update periodically:

```bash
npx impeccable skills update
```

### This suite (router + methodology)

Copy `context_methodology/` into the repo and wire `.cursor/skills/*` as thin pointers (see existing `same-wavelength` pattern).

**Deprecated:** `stable-ai-delivery/` — replaced by `senior-stable-delivery/` (redirect only; do not use).
