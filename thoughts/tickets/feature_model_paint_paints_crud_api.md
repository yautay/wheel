---
type: feature
priority: high
created: 2026-04-23T16:53:59Z
status: created
tags: [backend, api, paints, crud, search, sorting]
keywords: [paints CRUD, FastAPI router, paint service, paint repository, search, filter, sort, color_hex]
patterns: [router-service-repository, pageless list API, search and sort contracts, validation reuse, CRUD endpoint tests]
---

# FEATURE-004: Deliver paints catalog CRUD API with search and sorting

## Description
Implement the backend API for full paint catalog management, including create, list, detail, update, delete, and catalog discovery capabilities.

## Context
The user explicitly expanded the scope to full CRUD plus search, filtering, and sorting for the paint catalog. This ticket turns the persistence and conversion foundations into usable catalog endpoints.

## Requirements
Create a complete MVP paint catalog API suitable for desktop-first management flows.

### Functional Requirements
- Implement endpoints for creating paints.
- Implement endpoints for listing paints.
- Implement endpoints for retrieving paint details.
- Implement endpoints for updating paints.
- Implement endpoints for deleting paints.
- Support search and filtering by `brand`, `code`, and `name`.
- Support predictable sorting for catalog browsing.
- Reuse the shared color validation and conversion foundations for supported color inputs.
- Return stable response shapes defined by the contract ticket.

### Non-Functional Requirements
- Follow the planned `router -> service -> repository` structure.
- Keep endpoint behavior simple and predictable for the future frontend.
- Ensure tests cover both CRUD behavior and search/filter/sort logic.
- Avoid mixing import/export behavior into this ticket.

## Current State
The repository has no paint management API yet.

## Desired State
The backend exposes a complete paint catalog API that supports both data entry and desktop-first browsing workflows.

## Research Context
This ticket should direct later research toward standard CRUD and discovery patterns that fit the repository structure.

### Keywords to Search
- `paints CRUD` - core endpoint set to implement
- `paint search` - query behavior for catalog browsing
- `paint sort` - ordering options for desktop tables or lists
- `router service repository` - target backend structure
- `color_hex` - minimum catalog field expected across the app

### Patterns to Investigate
- `service-backed CRUD router` - keep transport and persistence concerns separate
- `filter + sort query params` - simple discovery API for the frontend
- `conversion on write` - validate and normalize color fields during create/update
- `endpoint-level CRUD tests` - verify behavior and regressions early

### Key Decisions Made
- Paint catalog scope is full CRUD, not create/list-only.
- Search, filtering, and sorting are in scope for MVP.
- Import/export is intentionally tracked in a later dedicated ticket.
- Tests are mandatory inside this ticket rather than in a separate QA ticket.

## Success Criteria
The paint catalog API is complete when the frontend can manage and browse owned paints entirely through supported endpoints.

### Automated Verification
- [ ] Automated tests cover create, list, detail, update, and delete paint flows.
- [ ] Automated tests cover search, filter, and sort behavior.
- [ ] Automated tests cover invalid create/update payloads.

### Manual Verification
- [ ] A developer can create and edit paints using the API.
- [ ] Paints can be searched and sorted by the expected fields.
- [ ] Deleted paints are removed predictably and consistently.

## Related Information
- Parent umbrella ticket: `thoughts/tickets/feature_model_paint_mvp_planning.md`
- Planned predecessor: `thoughts/tickets/feature_model_paint_color_conversion_layer.md`
- Planned next ticket: `thoughts/tickets/feature_model_paint_palettes_management_api.md`

## Notes
- Keep the ticket focused on paint catalog management only.
- Do not add user ownership or external catalog integration.
