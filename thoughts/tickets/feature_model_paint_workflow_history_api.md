---
type: feature
priority: high
created: 2026-04-23T16:53:59Z
status: created
tags: [backend, history, persistence, workflows, api]
keywords: [workflow history, saved results, history list, history detail, history delete, full payload persistence, scale effect history, modulation history]
patterns: [full input-output persistence, history timeline API, workflow type discrimination, delete-history flow, replay-friendly storage]
---

# FEATURE-008: Implement workflow history persistence and history API

## Description
Persist complete workflow runs for `scale effect` and `modulation`, and expose history APIs for listing, viewing, and deleting saved entries.

## Context
The user asked for a separate ticket for persistence/history and explicitly expanded the scope so history must store the full workflow input and output, not just a lightweight summary. The user also wants users to be able to delete history entries.

## Requirements
Add a durable workflow history layer for the MVP.

### Functional Requirements
- Create persistence models and migrations for workflow history entries.
- Store the full request and full response payload for successful `scale effect` runs.
- Store the full request and full response payload for successful `modulation` runs.
- Expose endpoints for listing history entries.
- Expose endpoints for retrieving a single history entry in full detail.
- Expose endpoints for deleting history entries.
- Preserve enough structured metadata to distinguish workflow type, source scope, and execution time.
- Keep stored data shaped so the frontend can reconstruct prior results without recomputation.

### Non-Functional Requirements
- Keep history storage simple and SQLite-friendly.
- Make history records replay-friendly for frontend detail views.
- Avoid introducing recipe entities or broader project tracking in this ticket.
- Include automated coverage for persistence and retrieval behavior.

## Current State
Workflow runs are not persisted and there is no history API.

## Desired State
The backend stores full workflow results and exposes a usable history interface for later frontend pages.

## Research Context
This ticket should guide later research toward durable but lightweight result persistence.

### Keywords to Search
- `saved results` - umbrella requirement for persisted workflows
- `workflow history` - list/detail/delete API behavior
- `full payload persistence` - store replayable request and response data
- `history detail` - frontend reconstruction requirements
- `workflow type` - distinguish scale effect and modulation records

### Patterns to Investigate
- `JSON payload persistence` - practical approach for full workflow snapshots
- `history summary + detail API` - efficient listing and full-view split
- `result replay storage` - keep enough fields for later re-display
- `delete-history endpoint tests` - verify destructive behavior safely

### Key Decisions Made
- History is tracked as a separate implementation ticket.
- Full request and response payloads must be persisted.
- History must support list, detail, and delete operations.
- Recipe/project features remain out of scope.

## Success Criteria
History support is complete when prior workflow runs can be revisited without rerunning the color engine.

### Automated Verification
- [ ] Automated tests cover storing `scale effect` workflow history entries.
- [ ] Automated tests cover storing `modulation` workflow history entries.
- [ ] Automated tests cover history list, detail, and delete endpoints.
- [ ] Automated tests verify that stored history contains enough data for later frontend reconstruction.

### Manual Verification
- [ ] A developer can inspect history entries after successful workflow runs.
- [ ] A history entry returns the complete request and response payloads.
- [ ] Deleting a history entry removes it predictably.

## Related Information
- Parent umbrella ticket: `thoughts/tickets/feature_model_paint_mvp_planning.md`
- Planned predecessor: `thoughts/tickets/feature_model_paint_modulation_workflow.md`
- Planned next ticket: `thoughts/tickets/feature_model_paint_catalog_import_export.md`

## Notes
- Keep history focused on workflow snapshots, not project organization.
- If implementation pressure rises, prefer simple summary fields plus a full serialized payload over a more normalized history model.
