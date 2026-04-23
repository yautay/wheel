---
type: feature
priority: high
created: 2026-04-23T16:53:59Z
status: created
tags: [database, models, migrations, seed, paints, palettes, sqlite]
keywords: [SQLAlchemy, SQLModel, Alembic, SQLite, paints table, palettes table, palette items, seed data]
patterns: [repository-ready models, join table ordering, migration bootstrap, seed fixtures, future-safe persistence]
---

# FEATURE-002: Implement core data models, migrations, and paint seed data

## Description
Create the initial persistence layer for the catalog domain, including database models, migrations, and development seed data for paints.

## Context
The umbrella MVP requires owned paints and simple palettes as the foundation for every workflow. The user also wants seed data only for paints, not for palettes or workflow history. This ticket establishes the core persistence needed by later CRUD and workflow tickets.

## Requirements
Implement the first database slice for the MVP catalog domain.

### Functional Requirements
- Create database models for paints.
- Create database models for palettes.
- Create a join model for paint-to-palette membership with explicit ordering support.
- Add all required Alembic migrations for the initial catalog schema.
- Add seed data and a seed-loading path for development and testing using paint examples only.
- Define repository-ready fields needed by later search, sorting, duplicate-palette, and import/export work.
- Preserve the minimum paint attributes required by the umbrella ticket: `brand`, `code`, `name`, `color_hex`.
- Allow room for canonical color storage choices needed by later workflow tickets.

### Non-Functional Requirements
- Keep auth and ownership columns out of scope for MVP v1.
- Keep the schema simple enough for SQLite while still supporting later growth.
- Use naming and constraints that make CRUD, palette ordering, and data portability predictable.
- Include automated migration and seed verification.

## Current State
No persistent domain models or migrations exist yet.

## Desired State
The repository contains an initial catalog schema that later API and frontend tickets can use directly, plus paint seed data for local development.

## Research Context
This ticket should guide research into storage patterns that support catalog management first and workflow persistence later.

### Keywords to Search
- `paint model` - required fields and indexing needs
- `palette model` - parent entity for grouped paints
- `palette item ordering` - ordered many-to-many storage pattern
- `Alembic initial migration` - repository bootstrap sequence
- `seed fixtures` - development dataset strategy

### Patterns to Investigate
- `ordered join table` - preserve explicit paint order inside a palette
- `repository-friendly model boundaries` - keep services easy to add later
- `seed command integration` - bootstrap paint samples for dev/test flows
- `SQLite-safe constraints` - use constraints that remain practical in local development

### Key Decisions Made
- Seed data should cover paints only.
- Ownership/auth fields are out of scope for this MVP phase.
- Palette membership must support explicit ordering.
- The schema should be simple but future-safe for later workflow and import/export tickets.

## Success Criteria
Core catalog persistence is complete when CRUD and workflow tickets can rely on stable models and repeatable database setup.

### Automated Verification
- [ ] Alembic migrations run cleanly on SQLite.
- [ ] Database models can be initialized without runtime errors.
- [ ] Seed data loads successfully into a clean local database.
- [ ] Automated tests cover core model constraints and palette ordering behavior.

### Manual Verification
- [ ] A developer can create the schema from scratch using documented commands.
- [ ] Paint seed data is available after the seed step completes.
- [ ] The resulting schema visibly supports paints, palettes, and ordered palette membership.

## Related Information
- Parent umbrella ticket: `thoughts/tickets/feature_model_paint_mvp_planning.md`
- Planned predecessor: `thoughts/tickets/debt_model_paint_api_contracts_validation.md`
- Planned next ticket: `thoughts/tickets/feature_model_paint_color_conversion_layer.md`

## Notes
- Do not add workflow history persistence in this ticket; that is tracked separately.
- Keep the schema focused on catalog entities and their immediate MVP needs.
