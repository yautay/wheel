---
type: feature
priority: high
created: 2026-04-23T16:53:59Z
status: created
tags: [workflow, modulation, color-engine, scoring, tonal-levels]
keywords: [modulation, five tonal levels, ideal target color, ranked recommendations, match score, palette scope, catalog scope]
patterns: [multi-output workflow, per-level recommendation ranking, tonal target generation, engine strategy isolation, structured workflow response]
---

# FEATURE-007: Implement the modulation workflow engine and API

## Description
Implement the backend `modulation` workflow with five tonal levels and per-level recommendation ranking, exposed through a dedicated API endpoint.

## Context
`Modulation` is the second core MVP workflow. The user clarified that its output should mirror the `scale effect` shape in spirit, but separately for each of the five tonal levels: `-2`, `-1`, `base`, `+1`, `+2`.

## Requirements
Deliver the second complete recommendation workflow for the MVP.

### Functional Requirements
- Implement a dedicated `modulation` service boundary in the color engine layer.
- Add an API endpoint for running `modulation` requests.
- Accept supported input colors in `HEX`, `LAB`, `RGB`, and `CMYK` forms.
- Accept execution against either the full paint catalog or a selected palette.
- Generate five tonal levels: `-2`, `-1`, `base`, `+1`, `+2`.
- For each tonal level, calculate and return an ideal target color.
- For each tonal level, return a ranked list of recommended paints and match scores.
- Reuse the shared contract and conversion layers.

### Non-Functional Requirements
- Keep the implementation modular so `modulation` logic can evolve independently of `scale effect`.
- Keep response shape predictable for later frontend rendering.
- Include robust automated coverage because the response is structurally richer than `scale effect`.
- Do not persist workflow history in this ticket.

## Current State
No `modulation` workflow logic or endpoint exists yet.

## Desired State
The backend exposes a working `modulation` endpoint that returns five tonal outputs, each with an ideal target color and ranked paint recommendations.

## Research Context
This ticket should focus later research on structured multi-result workflow design and recommendation consistency.

### Keywords to Search
- `modulation` - second core workflow capability
- `five tonal levels` - required output shape
- `ideal target color` - required per-level output
- `ranked recommendations` - per-level match list
- `match score` - recommendation quality field

### Patterns to Investigate
- `multi-level workflow response` - structured output for five tonal targets
- `shared ranking primitives` - reuse scoring behavior where appropriate
- `per-level engine calculation` - derive tonal targets consistently
- `workflow response tests` - verify structural completeness and edge cases

### Key Decisions Made
- `Modulation` is in scope for the first MVP slice.
- The endpoint must return five tonal levels with separate ideal targets and recommendation rankings.
- Users must be able to run the workflow against the full catalog or a selected palette.
- Persistence remains out of scope for this ticket and belongs to the history ticket.

## Success Criteria
This ticket is complete when the backend can generate usable five-level modulation recommendations from owned paints.

### Automated Verification
- [ ] Automated tests cover successful `modulation` requests using supported color input formats.
- [ ] Automated tests cover palette-scoped and catalog-scoped recommendation runs.
- [ ] Automated tests verify that all five tonal levels are present with ideal target colors, ranked recommendations, and match scores.
- [ ] Automated tests cover malformed workflow inputs and unsupported combinations.

### Manual Verification
- [ ] A developer can submit a valid `modulation` request and receive five tonal outputs.
- [ ] Each tonal level includes its own ideal target color and ranked paint recommendations.
- [ ] Running the same request against a palette changes the recommendation pool as expected.

## Related Information
- Parent umbrella ticket: `thoughts/tickets/feature_model_paint_mvp_planning.md`
- Planned predecessor: `thoughts/tickets/feature_model_paint_scale_effect_workflow.md`
- Planned next ticket: `thoughts/tickets/feature_model_paint_workflow_history_api.md`

## Notes
- Keep the algorithm practical and aligned with hobbyist workflow value.
- Do not add deferred roadmap items such as mix, projects, or ColorWheel.
