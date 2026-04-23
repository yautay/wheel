# DEBT-001 MVP Scaffold Foundation Implementation Plan

## Overview

Implement the first executable workspace slice for the model paint MVP using a minimal monorepo-style structure with dedicated `backend` and `frontend` apps. This plan establishes runnable application shells, baseline developer commands, environment templates, backend logging, and SQLite/Alembic integration points so all downstream tickets can focus on domain delivery.

## Current State Analysis

The repository is currently planning-focused with no runnable app code:
- Root docs are minimal (`README.md:1`).
- DEBT-001 requirements define scaffold scope and acceptance (`thoughts/tickets/debt_model_paint_mvp_scaffold_foundation.md:25`).
- This ticket is the first blocking item in the sequence (`thoughts/tickets/model_paint_mvp_execution_order.md:5`).
- Stack compatibility constraints are already fixed by umbrella planning (`thoughts/tickets/feature_model_paint_mvp_planning.md:57`).

## Desired End State

After this plan is implemented, the repo has:
- A clear root workspace split: `backend/` and `frontend/`.
- A runnable FastAPI backend with Loguru setup and a health/smoke endpoint.
- A runnable Vue 3 + TypeScript frontend with Pinia, Vue Router, and TailwindCSS baseline integration.
- `uv` backend dependency/bootstrap flow, `pnpm` frontend flow, and root `just` commands for common developer actions.
- SQLite + Alembic integration points ready for FEATURE-002 migrations.
- Root setup documentation that lets a developer install and run both apps.

### Key Discoveries:
- DEBT-001 explicitly requires backend/frontend split, app skeletons, env templates, Loguru, SQLite/Alembic touchpoints, health endpoint, and root README (`thoughts/tickets/debt_model_paint_mvp_scaffold_foundation.md:25`).
- Lightweight tooling is required; avoid orchestration overhead (`thoughts/tickets/debt_model_paint_mvp_scaffold_foundation.md:36`).
- Follow-on DEBT-002 contract work depends on this scaffold being in place (`thoughts/tickets/debt_model_paint_api_contracts_validation.md:80`).
- Current repo has no existing backend/frontend scaffold to preserve, so conventions established here become the initial standard.

## What We're NOT Doing

- Implementing domain features (paints, palettes, workflows, history), as explicitly out of scope (`thoughts/tickets/debt_model_paint_mvp_scaffold_foundation.md:91`).
- Implementing auth or ownership model in scaffold (`thoughts/tickets/debt_model_paint_mvp_scaffold_foundation.md:68`).
- Finalizing full developer handbook/user docs (those are separate later tickets).
- Adding heavy workspace orchestration (Turbo/Nx/Docker-first setup) unless required to satisfy baseline run/smoke outcomes.

## Implementation Approach

Use a lean layered scaffold with explicit boundaries but minimal code volume:
- Keep root workspace simple and command-driven through `just`.
- Bootstrap backend with predictable layout compatible with later router/service/repository and contract-first work.
- Bootstrap frontend with routed shell and state foundation only; no domain screens beyond placeholders.
- Add only the DB/logging/config primitives necessary to unblock subsequent tickets.

## Phase 1: Workspace and Tooling Foundation

### Overview
Create root structure, shared conventions, and command surface that standardizes daily local operations.

### Changes Required:

#### 1. Root workspace skeleton and conventions
**File**: `README.md`
**Changes**: Replace placeholder readme with scaffold-level setup guide, command reference, and troubleshooting basics.

#### 2. Root command orchestration
**File**: `justfile`
**Changes**: Add baseline commands for install/run/smoke/test/build flows across backend and frontend.

```make
# command names only (illustrative)
backend-install
backend-dev
backend-smoke
frontend-install
frontend-dev
frontend-build
dev
smoke
```

#### 3. Top-level hygiene
**File**: `.gitignore`
**Changes**: Add Python, Node, env, cache, and editor ignores aligned with `backend/` and `frontend/`.

### Success Criteria:

#### Automated Verification:
- [x] Root command file is valid and invokable: `just --list`
- [x] Repository includes expected top-level scaffold files and directories

#### Manual Verification:
- [x] A developer can understand project shape from root docs alone
- [x] Command names and intent are clear for backend/frontend workflows

---

## Phase 2: Backend Bootstrap (FastAPI + Loguru + SQLite/Alembic Touchpoints)

### Overview
Stand up a runnable backend shell with config, logging, routing, and migration scaffolding required by downstream backend tickets.

### Changes Required:

#### 1. Backend dependency and project config
**File**: `backend/pyproject.toml`
**Changes**: Define Python project metadata and baseline dependencies (FastAPI, Uvicorn, Pydantic settings, Loguru, SQLAlchemy/SQLModel, Alembic, pytest).

#### 2. Backend environment template
**File**: `backend/.env.example`
**Changes**: Add required env keys (app env, host/port, DB URL, logging level) with sane local defaults.

#### 3. FastAPI app shell and smoke endpoint
**File**: `backend/app/main.py`
**Changes**: Create app entrypoint, router registration, and minimal health endpoint.

```python
@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
```

#### 4. Logging setup
**File**: `backend/app/core/logging.py`
**Changes**: Centralize Loguru configuration and startup integration for consistent local diagnostics.

#### 5. DB + migration integration points
**File**: `backend/alembic.ini`
**Changes**: Add Alembic bootstrap configuration.

**File**: `backend/alembic/env.py`
**Changes**: Wire migration environment to app DB settings.

**File**: `backend/app/db/session.py`
**Changes**: Provide engine/session factory stub aligned to SQLite-first local development.

#### 6. Backend smoke test
**File**: `backend/tests/test_health.py`
**Changes**: Add simple API smoke test for health endpoint.

### Success Criteria:

#### Automated Verification:
- [x] Backend dependencies install via `uv`: `cd backend && uv sync`
- [x] FastAPI app starts locally: `cd backend && uv run uvicorn app.main:app --reload`
- [x] Health endpoint responds successfully: `curl http://127.0.0.1:8000/health`
- [x] Alembic command surface is functional: `cd backend && uv run alembic current`
- [x] Backend smoke test passes: `cd backend && uv run pytest`

#### Manual Verification:
- [x] Logs are emitted with Loguru during app startup/request handling
- [x] Backend directory structure is clear and extensible for DEBT-002/FEATURE-002
- [x] Env template fields are understandable and sufficient for local boot

---

## Phase 3: Frontend Bootstrap (Vue 3 + TS + Pinia + Router + Tailwind)

### Overview
Stand up a runnable frontend shell with typed app entrypoint and route/state foundations required by future frontend tickets.

### Changes Required:

#### 1. Frontend project setup
**File**: `frontend/package.json`
**Changes**: Define Vue/Vite TypeScript app with scripts for dev/build/test/lint and dependencies for Pinia, Vue Router, Tailwind.

#### 2. Frontend environment template
**File**: `frontend/.env.example`
**Changes**: Add `VITE_API_BASE_URL` and any required local frontend env defaults.

#### 3. Frontend app shell
**File**: `frontend/src/main.ts`
**Changes**: Initialize Vue app, register router and Pinia.

**File**: `frontend/src/App.vue`
**Changes**: Minimal shell layout and navigation placeholder.

**File**: `frontend/src/router/index.ts`
**Changes**: Add baseline route definitions for future pages (`paints`, `palettes`, `scale-effect`, `modulation`, `history`) with placeholder components.

#### 4. Tailwind baseline
**File**: `frontend/tailwind.config.ts`
**Changes**: Add initial Tailwind config wired to app content paths.

### Success Criteria:

#### Automated Verification:
- [x] Frontend dependencies install via `pnpm`: `cd frontend && pnpm install`
- [x] Frontend dev server starts: `cd frontend && pnpm dev`
- [x] Frontend build succeeds: `cd frontend && pnpm build`
- [x] Baseline lint/test script commands are present in `package.json`

#### Manual Verification:
- [x] App shell renders on desktop browser with working route navigation
- [x] Frontend can be configured to target backend URL via env template
- [x] Route structure is ready for FEATURE-010 and FEATURE-011 expansion

---

## Phase 4: Integrated Smoke Path and Documentation Finalization

### Overview
Ensure one coherent local run path from fresh clone to both apps running and smoke checks passing.

### Changes Required:

#### 1. Root developer runbook
**File**: `README.md`
**Changes**: Finalize exact step-by-step setup flow for prerequisites, install, run, smoke checks, and common failures.

#### 2. Command unification
**File**: `justfile`
**Changes**: Ensure root `dev` and `smoke` commands call backend/frontend flows consistently and match README examples.

```make
dev: backend-dev frontend-dev
smoke: backend-smoke frontend-build
```

### Success Criteria:

#### Automated Verification:
- [x] Root smoke command passes with expected local services: `just smoke`
- [x] Root command catalog remains valid and discoverable: `just --list`

#### Manual Verification:
- [x] A new developer can follow `README.md` and run both apps end-to-end
- [x] Backend/frontend separation and responsibilities are obvious from structure and docs
- [x] Troubleshooting section addresses likely first-run failures (missing Python/pnpm, env file omissions, port conflicts)

---

## Testing Strategy

### Unit Tests:
- Backend: health endpoint smoke and any minimal config/db bootstrap tests.
- Frontend: lightweight app-shell smoke (if test harness included), otherwise script placeholders verified.
- Just command-level checks for script existence and expected invocation behavior.

### Integration Tests:
- Backend startup + `/health` response.
- Frontend startup and successful build against configured API base URL.
- Root `just smoke` orchestration path.

### Manual Testing Steps:
1. Clone repo, copy env templates, and run install commands via `just`.
2. Start backend and confirm `/health` returns success.
3. Start frontend and verify shell renders with route navigation placeholders.
4. Run `just smoke` to validate baseline startup checks.
5. Confirm README instructions match actual command behavior.

## Performance Considerations

- Keep dev startup time low; avoid heavy tooling and unnecessary background services.
- Prefer simple local SQLite and direct process startup for rapid iteration.
- Keep logging useful but not noisy at default level.

## Migration Notes

- Alembic is scaffolded as an integration point only in this ticket; no domain schema migration is finalized here.
- FEATURE-002 will own concrete model migrations and seed lifecycle, building on this scaffold.

## References

- Original ticket: `thoughts/tickets/debt_model_paint_mvp_scaffold_foundation.md`
- Parent umbrella ticket: `thoughts/tickets/feature_model_paint_mvp_planning.md`
- Execution order: `thoughts/tickets/model_paint_mvp_execution_order.md`
- Planned next ticket: `thoughts/tickets/debt_model_paint_api_contracts_validation.md`

## Deviations from Plan

### Phase 3: Frontend Bootstrap (Vue 3 + TS + Pinia + Router + Tailwind)
- **Original Plan**: Validate frontend install/run/build directly with `pnpm` commands.
- **Actual Implementation**: Executed frontend commands with `corepack pnpm` and updated root `justfile` frontend recipes to use `corepack pnpm` for reliability when a global `pnpm` binary is unavailable.
- **Reason for Deviation**: The implementation environment did not expose a direct `pnpm` binary, but Corepack-provided `pnpm` was available and fully compatible.
- **Impact Assessment**: No functional impact on scaffold requirements; command behavior remains `pnpm`-based and reproducible for developers using Corepack.
- **Date/Time**: 2026-04-23
