---
type: feature
priority: high
created: 2026-04-23T16:53:59Z
status: created
tags: [frontend, vue, routing, pinia, paints, palettes, import-export]
keywords: [Vue Router, Pinia, API client, paints UI, palettes UI, separate routes, search filter sort, import export UI]
patterns: [frontend app shell, route-based desktop UI, shared API client, form-driven CRUD, list detail editing flows]
---

# FEATURE-010: Build the frontend foundation and catalog management screens

## Description
Create the frontend application shell, route structure, shared data-access layer, and the first catalog management screens for paints and palettes.

## Context
The user asked for separate routes rather than a single dashboard, and also expanded the catalog scope to include full CRUD, discovery features, palette curation, and import/export entry points. This ticket converts the backend catalog work into a usable desktop-first interface.

## Requirements
Deliver the first substantial frontend slice for the MVP.

### Functional Requirements
- Create the Vue frontend route structure with separate routes for `paints`, `palettes`, `scale effect`, `modulation`, and `history`.
- Add shared API client and state management foundations for later pages.
- Implement paints UI for create, list, detail, edit, and delete flows.
- Implement paints search, filtering, and sorting UI.
- Implement palettes UI for create, list, detail, edit, and delete flows.
- Implement palette paint assignment, removal, reordering, and duplication UI.
- Add import/export UI entry points for paints and palettes.
- Keep workflow and history routes present, even if their full screens arrive in the next ticket.

### Non-Functional Requirements
- Keep the UI functional, desktop-first, and intentionally simple.
- Reuse shared form and API patterns rather than creating page-specific behavior everywhere.
- Preserve route and state structure that later workflow/history pages can extend cleanly.
- Include frontend tests or smoke coverage appropriate to the repository setup.

## Current State
No usable frontend application shell or catalog management UI exists yet.

## Desired State
The frontend has a working routed shell and practical catalog screens that let a user manage paints and palettes from the browser.

## Research Context
This ticket should guide research toward a simple but maintainable Vue structure for the MVP.

### Keywords to Search
- `Vue Router` - separate-route requirement
- `Pinia` - shared client-side state strategy
- `paints UI` - catalog management screen patterns
- `palettes UI` - ordered collection management in the frontend
- `import export UI` - entry points for portability actions

### Patterns to Investigate
- `route-driven desktop shell` - top-level navigation and page boundaries
- `shared API composables or stores` - avoid repeating request logic
- `CRUD forms + searchable lists` - practical catalog management flow
- `ordered list drag/reorder or explicit move controls` - palette ordering UX pattern

### Key Decisions Made
- The frontend must use separate routes for the main MVP areas.
- Catalog management includes full CRUD plus search/filter/sort behavior.
- Palette management includes assignment, reordering, duplication, and import/export entry points.
- The UI can stay raw and functional as long as it is usable.

## Success Criteria
This ticket is complete when users can manage paints and palettes through a routed frontend instead of backend-only APIs.

### Automated Verification
- [ ] Frontend build passes with the routed shell and catalog screens in place.
- [ ] Frontend tests or smoke checks cover the main catalog page flows.
- [ ] API integration paths for paints, palettes, and import/export actions are exercised.

### Manual Verification
- [ ] A user can navigate between dedicated `paints` and `palettes` routes.
- [ ] A user can create, edit, delete, search, and sort paints.
- [ ] A user can create, edit, duplicate, and curate palettes, including paint ordering.
- [ ] Import/export actions are visible from the catalog UI.

## Related Information
- Parent umbrella ticket: `thoughts/tickets/feature_model_paint_mvp_planning.md`
- Planned predecessor: `thoughts/tickets/feature_model_paint_catalog_import_export.md`
- Planned next ticket: `thoughts/tickets/feature_model_paint_frontend_workflows_history.md`

## Notes
- Keep this ticket centered on app shell and catalog management only.
- Workflow execution and history rendering belong to the next frontend ticket.
