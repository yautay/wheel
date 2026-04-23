---
type: debt
priority: high
created: 2026-04-23T16:53:59Z
status: created
tags: [mvp, scaffold, monorepo, backend, frontend, fastapi, vue]
keywords: [workspace, backend, frontend, FastAPI, Vue 3, TypeScript, TailwindCSS, Alembic, SQLite, Loguru]
patterns: [monorepo layout, backend bootstrap, frontend bootstrap, environment configuration, developer commands, logging setup]
---

# DEBT-001: Establish MVP workspace and scaffold foundation

## Description
Create the base project structure for the model paint MVP as a minimal monorepo-style workspace with separate `backend` and `frontend` applications, shared delivery conventions, environment setup, logging, and baseline developer commands.

## Context
The umbrella MVP ticket requires a practical implementation sequence with no same-level dependencies. This ticket is the first execution slice because it creates the directories, tooling boundaries, and setup conventions that every later ticket will rely on.

The user explicitly asked to include the monorepo/workspace shape up front and to keep README/setup work as part of scaffolding.

## Requirements
Create a minimal but durable project foundation that supports sequential delivery of backend, frontend, and documentation work.

### Functional Requirements
- Create a workspace structure with dedicated `backend` and `frontend` applications.
- Bootstrap a runnable FastAPI backend application skeleton.
- Bootstrap a runnable Vue 3 + TypeScript frontend application skeleton.
- Add baseline dependency management, startup commands, and environment file templates for both apps.
- Add logging setup for the backend using `Loguru`.
- Add SQLite and Alembic integration points needed by later persistence tickets.
- Add a minimal health or smoke endpoint on the backend for local verification.
- Add a root-level developer README covering local setup, install, run, and basic troubleshooting.
- Define a simple directory and naming convention that later tickets can follow.

### Non-Functional Requirements
- Keep tooling intentionally lightweight; avoid unnecessary workspace complexity.
- Preserve compatibility with Python 3.12+, FastAPI, Vue 3, TypeScript, Pinia, Vue Router, TailwindCSS, SQLite, and Alembic.
- Keep the structure ready for later auth and broader domain growth without implementing auth now.
- Keep the first version desktop-first and optimized for fast iteration.
- Include automated smoke checks for local startup where practical.

## Current State
Only the umbrella planning ticket exists. The implementation workspace, application skeletons, and developer run path are not yet formalized.

## Desired State
The repository contains a clear MVP workspace with runnable backend and frontend shells, basic configuration, logging, and enough setup documentation to let later tickets focus on domain delivery instead of bootstrapping.

## Research Context
This ticket should help research agents identify practical repository layout and bootstrap patterns before domain work begins.

### Keywords to Search
- `FastAPI app factory` - backend bootstrap pattern to mirror
- `Vue 3 TypeScript scaffold` - frontend shell setup approach
- `Pinia Vue Router Tailwind` - frontend baseline integration points
- `Alembic SQLite` - migration bootstrap expectations
- `Loguru configuration` - backend logging conventions

### Patterns to Investigate
- `backend/frontend workspace split` - minimal monorepo layout without excess tooling
- `environment template files` - `.env.example` and configuration loading pattern
- `smoke startup commands` - simple run and check flow for both apps
- `root README + app-local README` - documentation layering for setup clarity

### Key Decisions Made
- Use a monorepo-style structure with separate backend and frontend apps.
- Keep setup documentation inside the scaffolding ticket rather than a separate scaffold README ticket.
- Keep tooling minimal and implementation-friendly rather than introducing additional orchestration for its own sake.
- Defer auth and user ownership concerns from the scaffold itself.

## Success Criteria
Scaffolding is complete when later tickets can build on a stable workspace instead of inventing structure on the fly.

### Automated Verification
- [ ] Backend dependencies install successfully and the FastAPI app starts locally.
- [ ] Frontend dependencies install successfully and the Vue app starts locally.
- [ ] A backend smoke endpoint responds successfully.
- [ ] Baseline lint/build/test commands are defined for later use, even if some suites are still placeholders.

### Manual Verification
- [ ] A developer can clone the repo and follow the root README to start both apps.
- [ ] The repository clearly separates backend and frontend concerns.
- [ ] Environment templates are present and understandable.
- [ ] Later tickets can reference this scaffold without redefining project structure.

## Related Information
- Parent umbrella ticket: `thoughts/tickets/feature_model_paint_mvp_planning.md`
- Planned execution order: 1 of the child-ticket sequence
- Planned next ticket: `thoughts/tickets/debt_model_paint_api_contracts_validation.md`

## Notes
- This ticket should not implement domain features such as paints, palettes, workflows, or history.
- Keep the setup intentionally small; only add infrastructure that clearly unblocks later sequential tickets.
