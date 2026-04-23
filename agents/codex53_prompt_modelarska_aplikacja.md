# Codex 5.3 implementation prompt
## Generate scaffold and first implementation for a model paint color mixing web app

You are implementing a desktop-first web application for scale modelers.

## Goal

Build an MVP web application for managing owned paints, palettes, recipes, and color workflows for model painting.

The app must support:
1. color mixing from owned paints toward a target color
2. scale effect presets
3. color modulation with five tonal levels

This is a practical workshop tool, not a laboratory-accurate system.

## Required stack

### Backend
- Python 3.12+
- FastAPI
- SQLAlchemy 2.x or SQLModel
- Alembic
- SQLite
- Loguru
- JWT auth with access + refresh tokens

### Frontend
- Vue 3
- TypeScript
- Pinia
- Vue Router
- TailwindCSS

## General rules

- Use clean architecture with separate routers, services, repositories, schemas, and models.
- Keep code readable and production-oriented.
- Include strong typing.
- Use clear naming.
- Avoid unnecessary abstraction.
- Add reasonable comments only where helpful.
- Make the project easy to extend later to PostgreSQL.
- All data must be scoped per user.
- Implement owner-based access control.
- Use Loguru for application logging.
- Use SQLite for MVP.
- Do not implement camera scanning yet.
- Do not implement email password reset yet.
- Do not implement social login.

## Product modules

### Auth
Implement:
- register
- login
- logout
- refresh token
- me endpoint
- change password

### Paints
Implement CRUD for user-owned paints.
Fields:
- brand
- line
- code
- name
- paint_type
- finish
- notes
- color_hex
- lab_l
- lab_a
- lab_b
- stock_status
- is_owned

### Palettes
Implement CRUD for palettes and attaching paints to palettes.

### Recipes
Implement create/list/read/delete for saved recipe results.
Recipe contains:
- mode
- name
- target color
- predicted color
- notes
- list of recipe items with proportions

### Projects
Implement CRUD for projects.
Fields:
- name
- scale
- project_type
- notes

## Color engine

Implement 3 endpoints:

### 1. POST /api/v1/color-engine/mix
Input:
- target color
- selected paint ids
- optional constraints

Output:
- primary mix proposal
- alternatives
- warnings

Implementation can be heuristic. It does not need to simulate pigments accurately.
Use practical approximation logic in LAB color space.

### 2. POST /api/v1/color-engine/scale-effect
Input:
- base color
- scale preset
- style preset

Scale presets:
- 1:35
- 1:48
- 1:72
- 1:144
- 1:350
- 1:700

Style presets:
- neutral
- warm
- cool
- faded
- dusty
- naval

Output:
- shifted target color
- recommended lightening paint from owned paints
- alternatives
- warnings

### 3. POST /api/v1/color-engine/modulation
Input:
- base color
- strength preset
- optional model type

Strength presets:
- subtle
- standard
- strong

Model types:
- armor
- aircraft
- ship
- figure

Output:
- five tonal levels:
  -2, -1, base, +1, +2
- recommended paint suggestions

## Frontend requirements

Create a Vue 3 app with:
- login and registration views
- protected routes
- dashboard
- paints view
- palettes view
- recipes view
- projects view
- mixing view
- scale effect view
- modulation view
- profile view

Implement Pinia stores:
- authStore
- paintsStore
- palettesStore
- recipesStore
- projectsStore
- colorEngineStore

Use Tailwind for layout and styling.

## Color wheel

Create a reusable Vue component named ColorWheel.

Requirements:
- render a segmented color wheel using SVG
- not a smooth gradient
- support approximately 24 hue segments
- support multiple tonal rings
- allow marker overlays
- allow click selection
- allow mode-specific markers later

It does not need to be mathematically perfect in v1, but it must be visually clean and structured for extension.

## Backend file structure

Use a structure similar to:

app/
  main.py
  api/v1/
  core/
  models/
  schemas/
  services/
  repositories/
  utils/

## Frontend file structure

Use a structure similar to:

src/
  api/
  components/
  views/
  stores/
  router/
  types/
  composables/

## Deliverables

Generate:
1. backend scaffold with working auth, models, migrations-ready setup, routers, services, repositories
2. frontend scaffold with router, stores, login flow, dashboard, basic CRUD views
3. initial ColorWheel SVG component
4. initial heuristic implementations for:
   - mixing
   - scale effect
   - modulation
5. clear README with setup instructions

## Important implementation notes

- Use password hashing securely.
- Use Pydantic schemas for API contracts.
- Return consistent JSON responses.
- Add basic validation and error handling.
- Keep the UI desktop-first.
- Make the first version functional rather than overengineered.
- Use mock-safe heuristic color logic where needed, but structure code so it can be improved later.
- The color engine should operate in LAB-oriented utilities, with helper conversion functions.

## Output style

Produce the codebase scaffold and implementation in a clean, maintainable way.
When uncertain, prefer pragmatic MVP choices over elaborate architecture.
