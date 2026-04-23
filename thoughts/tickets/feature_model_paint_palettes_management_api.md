---
type: feature
priority: high
created: 2026-04-23T16:53:59Z
status: created
tags: [backend, api, palettes, paints, ordering, duplication]
keywords: [palettes API, palette CRUD, palette items, reorder paints, duplicate palette, search palettes, filter palettes]
patterns: [ordered collections, duplicate entity flow, palette membership API, search and sort endpoints, service-backed mutations]
---

# FEATURE-005: Deliver palettes management API with full operations

## Description
Implement the backend API for complete palette management, including full CRUD, paint assignment and removal, explicit ordering, duplication, and palette discovery.

## Context
The user expanded scope beyond simple palette collections and requested a full feature set. That includes a complete management surface rather than a minimal MVP subset.

## Requirements
Build a practical palette API that supports workshop-style organization of owned paints.

### Functional Requirements
- Implement endpoints for creating, listing, retrieving, updating, and deleting palettes.
- Support assigning paints to palettes.
- Support removing paints from palettes.
- Support explicit ordering and reordering of paints within a palette.
- Support palette duplication.
- Support search, filtering, and sorting for palette browsing.
- Return palette detail responses that include assigned paints in order.
- Reuse the shared API contract and validation layer.

### Non-Functional Requirements
- Keep the API structure aligned with the paint catalog endpoints.
- Preserve deterministic ordering semantics because later workflows may use palette-scoped recommendation runs.
- Include automated tests for duplicate, reorder, and membership edge cases.
- Do not fold import/export into this ticket.

## Current State
The repository has no palette management API yet.

## Desired State
The backend exposes a complete palette management API that supports realistic grouping and curation of owned paints.

## Research Context
This ticket should help research agents inspect patterns for ordered collections and duplication behavior.

### Keywords to Search
- `palettes` - core grouped-catalog feature
- `palette item ordering` - ordered membership behavior
- `duplicate palette` - cloning flow and naming strategy
- `palette search` - discovery needs for a growing catalog
- `paint assignment` - add/remove membership operations

### Patterns to Investigate
- `ordered child collection` - keep paint order stable after edits
- `duplicate with membership copy` - clone palette contents safely
- `collection detail endpoint` - return ordered nested items
- `membership mutation tests` - validate reorder and deletion edge cases

### Key Decisions Made
- Palette scope is full management, not minimal create/list-only behavior.
- Explicit ordering and duplication are in scope.
- Search, filtering, and sorting are in scope.
- Import/export will be handled separately.

## Success Criteria
Palette management is complete when a user can create, curate, duplicate, and organize paint groups entirely through the backend API.

### Automated Verification
- [ ] Automated tests cover palette create, list, detail, update, and delete flows.
- [ ] Automated tests cover assigning, removing, and reordering paints.
- [ ] Automated tests cover duplicate-palette behavior.
- [ ] Automated tests cover palette search/filter/sort behavior.

### Manual Verification
- [ ] A developer can create a palette and populate it with existing paints.
- [ ] Paint order changes are reflected consistently in responses.
- [ ] A duplicated palette preserves expected contents without corrupting the original.

## Related Information
- Parent umbrella ticket: `thoughts/tickets/feature_model_paint_mvp_planning.md`
- Planned predecessor: `thoughts/tickets/feature_model_paint_paints_crud_api.md`
- Planned next ticket: `thoughts/tickets/feature_model_paint_scale_effect_workflow.md`

## Notes
- Keep this ticket focused on palette-domain APIs.
- Do not implement workflow logic here.
