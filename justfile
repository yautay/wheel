set shell := ["bash", "-cu"]

backend-install:
	cd backend && uv sync

backend-dev:
	cd backend && uv run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

backend-smoke:
	cd backend && uv run pytest && uv run alembic current

frontend-install:
	cd frontend && corepack pnpm install

frontend-dev:
	cd frontend && corepack pnpm dev

frontend-build:
	cd frontend && corepack pnpm build

frontend-lint:
	cd frontend && corepack pnpm lint

frontend-test:
	cd frontend && corepack pnpm test

install: backend-install frontend-install

dev:
	trap 'kill 0' INT TERM EXIT; (cd backend && uv run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload) & (cd frontend && corepack pnpm dev) & wait

smoke:
	just backend-smoke && just frontend-build
