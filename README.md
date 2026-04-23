# Model Paint MVP Workspace

This repository hosts the MVP scaffold for a model paint workflow application.
It is a lightweight workspace with two apps:

- `backend/`: FastAPI + Loguru + SQLite/Alembic scaffold
- `frontend/`: Vue 3 + TypeScript + Pinia + Router + Tailwind scaffold

## Prerequisites

- `just`
- Python `3.12+`
- `uv`
- Node.js `20+`
- `pnpm`

## Project Layout

```text
.
├── backend/
├── frontend/
├── justfile
└── thoughts/
```

## Quick Start

1. Install dependencies:
   - `just backend-install`
   - `just frontend-install`
2. Copy environment templates:
   - `cp backend/.env.example backend/.env`
   - `cp frontend/.env.example frontend/.env`
3. Start services:
   - Backend only: `just backend-dev`
   - Frontend only: `just frontend-dev`
   - Both apps: `just dev`

## Command Reference

- `just backend-install`: install backend dependencies with `uv sync`
- `just backend-dev`: run FastAPI app in reload mode
- `just backend-smoke`: run backend health smoke (`pytest` + `alembic current`)
- `just frontend-install`: install frontend dependencies with `pnpm install`
- `just frontend-dev`: run Vite dev server
- `just frontend-build`: build frontend with Vite
- `just frontend-lint`: run frontend lint script
- `just frontend-test`: run frontend test script
- `just install`: install dependencies for both apps
- `just dev`: run backend and frontend dev servers together
- `just smoke`: run baseline backend smoke and frontend build

Run `just --list` to discover all available commands.

## Smoke Checks

- Backend health endpoint: `curl http://127.0.0.1:8000/health`
- Combined smoke path: `just smoke`

## Troubleshooting

- Missing `uv`: install from <https://docs.astral.sh/uv/>
- Missing `pnpm`: run `corepack enable` and `corepack prepare pnpm@latest --activate`
- Env not loaded: ensure `.env` files exist in `backend/` and `frontend/`
- Port conflicts:
  - Backend default is `8000`
  - Frontend default is `5173`
- If `alembic current` fails before first migration, this is expected until migration revisions are added in follow-up tickets.
