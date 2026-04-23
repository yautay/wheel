---
type: feature
priority: high
created: 2026-04-23T16:53:59Z
status: created
tags: [workflow, scale-effect, color-engine, scoring, recommendations]
keywords: [scale effect, color engine, ideal target color, ranked recommendations, match score, palette scope, catalog scope]
patterns: [workflow service boundary, target-color calculation, ranking algorithm, palette-or-catalog source selection, engine response model]
---

# FEATURE-006: Implement the scale effect workflow engine and API

## Description
Implement the backend `scale effect` workflow, including ideal target color calculation, ranked paint recommendations, match scoring, and API exposure.

## Context
`Scale effect` is one of the two core MVP capabilities called out in the umbrella ticket. The user also expanded the expected output so the endpoint should return both the ideal target color and a ranking of candidate paints, and it should work against either the full catalog or a selected palette.

## Requirements
Deliver the first complete recommendation workflow for the MVP.

### Functional Requirements
- Implement a dedicated `scale effect` service boundary in the color engine layer.
- Add an API endpoint for running `scale effect` requests.
- Accept supported input colors in `HEX`, `LAB`, `RGB`, and `CMYK` forms.
- Accept execution against either the full paint catalog or a selected palette.
- Calculate and return the ideal target color for the workflow result.
- Return a ranked list of recommended paints rather than only a single best match.
- Return match scores for the ranked recommendations.
- Reuse the shared contract and conversion layers.

### Non-Functional Requirements
- Keep the implementation heuristic and modular rather than pigment-science heavy.
- Keep the engine boundary replaceable for future algorithm upgrades.
- Make the ranking logic deterministic enough for automated tests.
- Do not persist workflow history in this ticket.

## Current State
No `scale effect` workflow logic or endpoint exists yet.

## Desired State
The backend exposes a working `scale effect` endpoint that returns an ideal target color plus ranked recommendations from the selected paint source.

## Research Context
This ticket should help downstream research agents focus on the first color-engine slice for the MVP.

### Keywords to Search
- `scale effect` - core workflow requirement
- `ideal target color` - primary workflow output
- `match score` - ranking explanation field
- `paint recommendation ranking` - result ordering behavior
- `palette-scoped workflow` - support limited paint subsets

### Patterns to Investigate
- `engine service boundary` - isolate heuristic logic from transport code
- `target-first ranking` - calculate ideal color before recommendation scoring
- `catalog vs palette source selection` - choose recommendation pool predictably
- `workflow endpoint tests` - cover valid, invalid, and edge-case inputs

### Key Decisions Made
- `Scale effect` is a core MVP workflow.
- The response must include both the ideal target color and a ranking of candidate paints.
- Users must be able to run the workflow against the full catalog or a chosen palette.
- Persistence is intentionally deferred to the separate history ticket.

## Success Criteria
This ticket is complete when the backend can produce practical `scale effect` recommendations for a hobbyist's owned paints.

### Automated Verification
- [ ] Automated tests cover successful `scale effect` requests using supported color input formats.
- [ ] Automated tests cover palette-scoped and catalog-scoped recommendation runs.
- [ ] Automated tests verify that the response includes an ideal target color, ranked recommendations, and match scores.
- [ ] Automated tests cover malformed workflow inputs and unsupported combinations.

### Manual Verification
- [ ] A developer can submit a valid `scale effect` request and receive ranked paint recommendations.
- [ ] The ideal target color is clearly present in the response.
- [ ] Running the same request against a palette changes the recommendation pool as expected.

## Related Information
- Parent umbrella ticket: `thoughts/tickets/feature_model_paint_mvp_planning.md`
- Planned predecessor: `thoughts/tickets/feature_model_paint_palettes_management_api.md`
- Planned next ticket: `thoughts/tickets/feature_model_paint_modulation_workflow.md`

## Notes
- Keep the algorithm practical and explainable rather than scientifically exhaustive.
- Do not add mix workflows or recipe generation.
