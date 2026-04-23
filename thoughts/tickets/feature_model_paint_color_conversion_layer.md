---
type: feature
priority: high
created: 2026-04-23T16:53:59Z
status: created
tags: [color, conversion, utilities, lab, rgb, cmyk, hex]
keywords: [color conversion, HEX, LAB, RGB, CMYK, canonical color model, utility layer, validation]
patterns: [LAB-oriented utility layer, conversion helpers, normalization pipeline, deterministic math, test-first utilities]
---

# FEATURE-003: Build the color conversion utility layer

## Description
Implement the shared color conversion utilities needed to normalize `HEX`, `LAB`, `RGB`, and `CMYK` inputs into a reliable internal representation for later workflow engines.

## Context
The umbrella MVP requires multi-format color input from the start. Later tickets for paints, `scale effect`, and `modulation` all depend on predictable conversion behavior and strong validation.

## Requirements
Create a reusable conversion layer that can be called by APIs and workflow services.

### Functional Requirements
- Support conversion between `HEX`, `LAB`, `RGB`, and `CMYK`.
- Normalize workflow and catalog inputs to a canonical internal representation.
- Expose clear utility functions or service helpers for later backend tickets.
- Validate value ranges and reject malformed color payloads.
- Support round-trip test cases where practical.
- Document assumptions and tolerances where exact round-trip fidelity is not realistic.

### Non-Functional Requirements
- Keep conversions deterministic and easy to test.
- Prefer a LAB-oriented internal model because later recommendation scoring will compare perceptual distance.
- Avoid coupling the conversion layer directly to FastAPI or persistence concerns.
- Include thorough automated test coverage because later tickets depend on these results.

## Current State
No reusable color conversion implementation exists yet.

## Desired State
The backend has a stable utility layer that accepts supported color formats, validates them, and returns canonical representations for domain services.

## Research Context
This ticket should give later research and implementation a stable mathematical foundation.

### Keywords to Search
- `HEX LAB RGB CMYK conversion` - required transformation support
- `LAB color distance` - future scoring compatibility
- `normalization helper` - canonical internal representation
- `color validation` - input boundary checks

### Patterns to Investigate
- `LAB-first color pipeline` - normalize before workflow logic
- `stateless conversion helpers` - keep utilities reusable and easy to test
- `tolerance-based assertions` - realistic test strategy for color math
- `payload-to-domain normalization` - convert API input into engine-friendly structures

### Key Decisions Made
- All four color formats must be supported in the first MVP slice.
- The conversion layer should be reusable by both CRUD and workflow tickets.
- LAB-oriented internals are preferred for later heuristic scoring.
- Conversion logic should stay isolated from transport and storage layers.

## Success Criteria
This ticket is complete when later services can trust the color conversion layer as their normalization entry point.

### Automated Verification
- [ ] Automated tests cover valid conversions among `HEX`, `LAB`, `RGB`, and `CMYK`.
- [ ] Automated tests cover malformed input and out-of-range values.
- [ ] Automated tests verify expected tolerances for representative round-trip conversions.

### Manual Verification
- [ ] A developer can inspect the utility layer and understand the canonical internal color flow.
- [ ] Later domain services can call the conversion layer without adding format-specific logic.
- [ ] Representative sample colors produce sensible converted values.

## Related Information
- Parent umbrella ticket: `thoughts/tickets/feature_model_paint_mvp_planning.md`
- Planned predecessor: `thoughts/tickets/feature_model_paint_data_models_migrations_seed.md`
- Planned next ticket: `thoughts/tickets/feature_model_paint_paints_crud_api.md`

## Notes
- Do not implement workflow heuristics in this ticket.
- Keep the API-facing validation rules aligned with the separate contract ticket.
