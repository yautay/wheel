---
type: feature
priority: high
created: 2026-04-23T16:53:59Z
status: created
tags: [frontend, workflows, history, scale-effect, modulation, vue]
keywords: [scale effect UI, modulation UI, history UI, ranked recommendations, ideal target color, match score, palette scope]
patterns: [workflow form pages, multi-result rendering, history detail views, reusable result components, route-based workflow screens]
---

# FEATURE-011: Build the frontend workflow and history screens

## Description
Implement the frontend pages for running `scale effect` and `modulation`, rendering ranked recommendations and target colors, and browsing saved workflow history.

## Context
This ticket completes the MVP vertical slice by exposing the two main color workflows and their persisted history through the routed frontend foundation established earlier.

## Requirements
Deliver the remaining end-user screens required by the MVP.

### Functional Requirements
- Implement the `scale effect` page and form flow.
- Implement the `modulation` page and form flow.
- Allow workflow execution against either the full catalog or a selected palette.
- Render ideal target color output for workflow results.
- Render ranked recommendation lists and match scores.
- Render all five tonal levels for `modulation` results.
- Implement history list, detail, and delete flows in the frontend.
- Ensure saved history can be revisited without rerunning the engine.

### Non-Functional Requirements
- Keep the pages functional and desktop-first.
- Reuse shared result-rendering patterns where possible.
- Keep the UI clear enough for hobbyist use even if design polish remains minimal.
- Include frontend tests or smoke coverage for the critical workflow paths.

## Current State
The frontend shell may exist, but workflow execution and history usage are not yet available to users.

## Desired State
Users can run both core workflows from the browser, inspect results, and browse saved history entries.

## Research Context
This ticket should guide research toward practical workflow UX and reusable result rendering.

### Keywords to Search
- `scale effect UI` - first workflow page requirements
- `modulation UI` - five-level rendering pattern
- `ideal target color` - primary result visualization
- `match score` - recommendation explanation field
- `history detail` - replay-friendly frontend rendering

### Patterns to Investigate
- `workflow page with structured result panel` - form + results layout
- `shared recommendation list component` - reuse between workflows
- `multi-level results rendering` - clear display of modulation outputs
- `history route detail view` - revisit stored results without rerun

### Key Decisions Made
- Separate routes are required for workflow and history views.
- Users must be able to run workflows against the full catalog or a chosen palette.
- Workflow results must show ideal target colors, ranked recommendations, and match scores.
- History must support list, detail, and delete actions.

## Success Criteria
This ticket is complete when the MVP is usable end-to-end from the frontend for the main workflow loop.

### Automated Verification
- [ ] Frontend build passes with workflow and history screens implemented.
- [ ] Frontend tests or smoke checks cover executing `scale effect` and `modulation` flows.
- [ ] Frontend tests or smoke checks cover history list, detail, and delete behavior.

### Manual Verification
- [ ] A user can run `scale effect` from the frontend and inspect the ranked output.
- [ ] A user can run `modulation` and inspect all five tonal results.
- [ ] A user can choose either the whole catalog or a palette as the recommendation source.
- [ ] A user can open and delete saved workflow history entries.

## Related Information
- Parent umbrella ticket: `thoughts/tickets/feature_model_paint_mvp_planning.md`
- Planned predecessor: `thoughts/tickets/feature_model_paint_frontend_foundation_catalog.md`
- Planned next ticket: `thoughts/tickets/debt_model_paint_business_scope_docs.md`

## Notes
- Keep advanced visual polish, charts, and deferred roadmap UI out of scope.
- The goal is a usable workflow interface, not final design refinement.
