---
type: feature
priority: high
created: 2026-04-23T16:33:30Z
status: created
tags: [planning, mvp, color-engine, paints, palettes, fastapi, vue]
keywords: [model paint app, scale effect, modulation, color engine, paints CRUD, palettes, color conversions, FastAPI, Vue 3, SQLite]
patterns: [service and repository layers, color conversion utilities, heuristic scoring, result persistence, desktop-first forms, modular engine design]
---

# FEATURE-001: Plan and scaffold strategy for model paint color workflow MVP

## Description
Create the planning and implementation foundation for an MVP web application for scale modelers focused on practical color workflows. The first implementation slice should prioritize `scale effect` and `modulation`, supported by user-managed paints and simple palettes, with saved results and recommendation scoring against an ideal target color.

This ticket is intentionally an umbrella planning ticket. Its purpose is to define MVP scope, research hooks, constraints, and a recommended breakdown into smaller development tickets for backend, frontend, color engine, persistence, testing, and documentation.

## Context
The source prompt in `agents/codex53_prompt_modelarska_aplikacja.md` describes a broad desktop-first application spanning auth, paints, palettes, recipes, projects, and multiple color engine modes. During scope clarification, the MVP boundary was narrowed to the most valuable workflow for hobbyists: `scale effect` and five-level `modulation` based on owned paints.

This application is intended as a practical workshop tool rather than a pigment-accurate laboratory system. The first release should therefore optimize for usability, clear architecture, and future extensibility rather than perfect color science.

Business and product context captured from the user:
- Primary users are hobbyists.
- The app is standalone.
- The immediate outcome of this ticket should be a build plan and checklist that can be converted into smaller dev tickets.
- The initial frontend may be raw and functional; refined UX can come later.

## Requirements
Define, research, and prepare implementation for an MVP with a narrow core workflow and clear out-of-scope boundaries.

### Functional Requirements
- Support manual paint entry by the user.
- Support paint input and processing in `HEX`, `LAB`, `CMYK`, and `RGB` forms.
- Convert between supported color representations as needed based on user input method.
- Provide a user-owned paint catalog with at least:
  - `brand`
  - `code`
  - `name`
  - `color_hex`
- Provide simple user palettes as collections of owned paints.
- Implement `scale effect` as a dedicated backend capability and API endpoint.
- Implement `modulation` with five tonal levels (`-2`, `-1`, `base`, `+1`, `+2`) as a dedicated backend capability and API endpoint.
- Recommend concrete paints from the user's collection/palette for the generated result.
- Return the ideal target color the engine is aiming toward.
- Return a match score describing how close the recommendation is to the ideal result.
- Persist saved results/history for `scale effect` and `modulation` runs.
- Provide a minimal frontend for:
  - adding paints
  - running `scale effect`
  - running `modulation`
  - listing saved results
- Include migrations, seed data for development/testing, and README setup instructions.
- Produce a suggested breakdown into smaller dev tickets covering backend, frontend, color engine, persistence, tests, and docs.

### Non-Functional Requirements
- Use the stack from the source prompt unless research reveals a blocking issue:
  - Python 3.12+
  - FastAPI
  - SQLAlchemy 2.x or SQLModel
  - Alembic
  - SQLite
  - Loguru
  - Vue 3
  - TypeScript
  - Pinia
  - Vue Router
  - TailwindCSS
- Keep the first version desktop-first.
- Keep the first version functional and intentionally simple.
- Use a modular color-engine design so heuristics can be upgraded later.
- Prefer a dedicated color-engine service boundary that allows swapping or extending algorithms later.
- Keep backend structure compatible with future expansion to auth and broader per-user ownership rules.
- Include automated tests for core color conversion and primary API flows.
- Keep the project easy to extend later to richer paint metadata, auth, and more advanced algorithms.

## Current State
There is currently a specification/prompt describing a much larger product surface in `agents/codex53_prompt_modelarska_aplikacja.md`, but the effective MVP boundaries and implementation order were not yet captured in a planning ticket.

The clarified MVP scope is narrower than the original prompt:
- `scale effect` and `modulation` are the product core.
- `mix` is explicitly out of the first implementation slice.
- Auth is not required in the first stage.
- `projects` are deferred.
- `ColorWheel` is deferred.
- Full recipe support can come later; initial persistence may focus on saved result history.

## Desired State
The project should have a clear umbrella ticket that allows research and planning agents to:
- understand the exact MVP boundary
- identify what is intentionally deferred
- research concrete implementation patterns in the repository and target stack
- generate follow-up implementation tickets in a sensible order
- verify success against explicit functional and technical criteria

The first implementation wave should be able to deliver a usable vertical slice where a hobbyist can manage a minimal paint library, group paints into a palette, run `scale effect` or `modulation`, see the ideal target color and recommendation score, and save the result.

## Research Context
This section is intended for downstream research agents.

### Keywords to Search
- `codex53_prompt_modelarska_aplikacja` - source scope document for the original broad request
- `scale effect` - core MVP capability and endpoint naming
- `modulation` - second core MVP capability and tonal output model
- `color engine` - service boundary for heuristic logic
- `HEX LAB RGB CMYK conversion` - required input/output color conversions
- `paints CRUD` - minimal user paint catalog implementation
- `palettes` - simple collections required for color workflows
- `saved results` - persistence target for first-stage output history
- `match score` - scoring mechanism against ideal target color
- `ideal target color` - response shape and algorithm output requirement
- `FastAPI router service repository` - desired backend layering pattern
- `Vue 3 Pinia Vue Router Tailwind` - expected frontend integration points
- `Alembic SQLite seed data` - persistence and environment bootstrap requirements

### Patterns to Investigate
- `router -> service -> repository` - backend structure for maintainable API growth
- `Pydantic schema separation` - request/response validation boundaries
- `modular heuristic engine` - separate service or strategy boundary for later algorithm upgrades
- `LAB-oriented utility layer` - practical color math foundation with conversion helpers
- `scoring against target color` - distance and ranking pattern for paint recommendations
- `saved operation history` - result persistence shape for scale effect and modulation runs
- `minimal CRUD + workflow UI` - practical desktop-first frontend composition for MVP
- `seed fixtures for paints` - developer/test setup without external catalog integrations
- `future auth readiness` - scoping data models so user ownership can be added later without major rewrites

### Key Decisions Made
- Focus the first MVP on `scale effect` and `modulation` because they are the highest-value workflows for hobbyists.
- Exclude `mix` from the first implementation slice.
- Exclude auth from the first stage; add it later when broader per-user workflow needs justify it.
- Use manual paint entry for v1 instead of import/catalog integrations.
- Keep `palettes` in scope as simple collections because they are needed for practical user workflows.
- Defer `projects` to a later phase.
- Defer `ColorWheel` to a later phase.
- Keep the initial frontend simple and functional rather than visually polished.
- Persist results/history now; fuller recipe capabilities can evolve later.
- Support `HEX`, `LAB`, `CMYK`, and `RGB` inputs from the start.
- Include recommendation scoring and the ideal target color in engine responses.
- Use a modular color-engine service design so heuristics can be replaced or expanded later.
- Include migrations, seed data, tests, and README in the first implementation plan.

## Suggested Ticket Breakdown
Recommended follow-up implementation order:

1. Project scaffold and backend core setup
2. Database models, Alembic setup, and seed data
3. Color conversion utility layer for `HEX/LAB/RGB/CMYK`
4. Minimal paints CRUD API
5. Minimal palettes API and paint-to-palette assignment
6. `scale effect` engine endpoint and scoring model
7. `modulation` engine endpoint and five-level tonal output
8. Persistence for saved results/history
9. Minimal Vue frontend for paints, workflows, and saved results
10. Automated tests for conversions, validation, and API flows
11. README and developer setup documentation
12. Deferred roadmap tickets for auth, mix, projects, ColorWheel, and richer recipe support

### Child Tickets Execution Order
This implementation backlog is intentionally sequential so each ticket unlocks the next without same-level dependencies.

1. `thoughts/tickets/debt_model_paint_mvp_scaffold_foundation.md` - `DEBT-001: Establish MVP workspace and scaffold foundation`
2. `thoughts/tickets/debt_model_paint_api_contracts_validation.md` - `DEBT-002: Define API contracts and validation foundations`
3. `thoughts/tickets/feature_model_paint_data_models_migrations_seed.md` - `FEATURE-002: Implement core data models, migrations, and paint seed data`
4. `thoughts/tickets/feature_model_paint_color_conversion_layer.md` - `FEATURE-003: Build the color conversion utility layer`
5. `thoughts/tickets/feature_model_paint_paints_crud_api.md` - `FEATURE-004: Deliver paints catalog CRUD API with search and sorting`
6. `thoughts/tickets/feature_model_paint_palettes_management_api.md` - `FEATURE-005: Deliver palettes management API with full operations`
7. `thoughts/tickets/feature_model_paint_scale_effect_workflow.md` - `FEATURE-006: Implement the scale effect workflow engine and API`
8. `thoughts/tickets/feature_model_paint_modulation_workflow.md` - `FEATURE-007: Implement the modulation workflow engine and API`
9. `thoughts/tickets/feature_model_paint_workflow_history_api.md` - `FEATURE-008: Implement workflow history persistence and history API`
10. `thoughts/tickets/feature_model_paint_catalog_import_export.md` - `FEATURE-009: Implement catalog import and export for paints and palettes`
11. `thoughts/tickets/feature_model_paint_frontend_foundation_catalog.md` - `FEATURE-010: Build the frontend foundation and catalog management screens`
12. `thoughts/tickets/feature_model_paint_frontend_workflows_history.md` - `FEATURE-011: Build the frontend workflow and history screens`
13. `thoughts/tickets/debt_model_paint_business_scope_docs.md` - `DEBT-003: Write the concise business scope document for the MVP`
14. `thoughts/tickets/debt_model_paint_technical_architecture_docs.md` - `DEBT-004: Write the technical architecture document for the MVP`
15. `thoughts/tickets/debt_model_paint_developer_guide.md` - `DEBT-005: Write the developer setup and operations guide`
16. `thoughts/tickets/debt_model_paint_user_guide.md` - `DEBT-006: Write the end-user guide with example workflows`

## Success Criteria
This umbrella ticket is complete when it enables concrete downstream execution and the resulting MVP can be verified.

### Automated Verification
- [ ] Backend test suite covers color conversions between `HEX`, `LAB`, `RGB`, and `CMYK`.
- [ ] Automated tests cover request validation for invalid color payloads and malformed workflow inputs.
- [ ] Automated tests cover `scale effect` API behavior, including ideal target color and score fields.
- [ ] Automated tests cover `modulation` API behavior, including five tonal outputs and recommendations.
- [ ] Automated tests cover saving and listing workflow results/history.
- [ ] Database migrations run cleanly on SQLite.
- [ ] Seed data can be loaded successfully for development/testing.
- [ ] Frontend build and basic smoke checks pass once the UI slice exists.

### Manual Verification
- [ ] A developer can follow the README to run the app locally.
- [ ] A user can add owned paints manually.
- [ ] A user can assemble a simple palette from owned paints.
- [ ] A user can submit a `scale effect` request using supported color input formats.
- [ ] A user can submit a `modulation` request and receive five tonal levels.
- [ ] Workflow results display recommended paints, the ideal target color, and a match score.
- [ ] A user can save and revisit previous workflow results.
- [ ] Deferred items remain out of scope for the first implementation slice.

## Related Information
- Source specification: `agents/codex53_prompt_modelarska_aplikacja.md`
- Potential supporting documents:
  - `agents/modelarska_aplikacja_spec.md`
  - `agents/modelarska_aplikacja_spec_rozszerzona.md`

## Notes
- This ticket should be treated as an umbrella planning ticket rather than a single coding task.
- If implementation pressure grows, split persistence/history and palette management into separate child tickets to keep delivery slices atomic.
- Future research should explicitly evaluate whether saved result history and full recipe entities should remain separate or converge later.
- Future research should define how user ownership/auth is introduced without rewriting the color engine or persistence model.
