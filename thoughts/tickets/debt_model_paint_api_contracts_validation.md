---
type: debt
priority: high
created: 2026-04-23T16:53:59Z
status: implemented
tags: [architecture, api, validation, schemas, pydantic, fastapi]
keywords: [API contracts, validation, Pydantic, request schema, response schema, color payload, error model, OpenAPI]
patterns: [schema separation, shared validation rules, error response model, color input union, contract-first API design]
---

# DEBT-002: Define API contracts and validation foundations

## Description
Define the shared request and response contracts, validation rules, and error semantics for the MVP APIs before endpoint implementation begins.

## Context
The user preferred a separate ticket for shared validation and API contracts instead of burying them inside domain tickets. This ticket reduces churn across later paints, palettes, workflow, history, and frontend work by standardizing payload shapes early.

## Requirements
Create a contract-first API foundation covering the domain entities and workflow payloads that later implementation tickets will use.

### Functional Requirements
- Define shared request and response schemas for paints, palettes, palette membership, workflows, and history entries.
- Define a canonical color input contract supporting `HEX`, `LAB`, `RGB`, and `CMYK` input modes.
- Define response contracts for ranked recommendations, ideal target colors, and workflow metadata.
- Define validation rules for malformed colors, unsupported payload combinations, and invalid workflow options.
- Define a standard API error response shape for validation and domain errors.
- Ensure the contracts are reflected in FastAPI/OpenAPI output.
- Document field-level expectations needed by frontend forms and later persistence tickets.

### Non-Functional Requirements
- Keep the contract layer stable enough to reduce breaking changes across later tickets.
- Prefer explicit schema separation for create, update, list, detail, and workflow payloads.
- Keep validation rules aligned with a LAB-oriented internal color model without locking the implementation too early.
- Avoid adding generic abstractions that are not required by the MVP.

## Current State
The umbrella ticket defines required behaviors, but no shared API contract or validation model exists yet.

## Desired State
The MVP has a clear, documented contract layer that domain tickets can implement directly and the frontend can consume without guessing shapes.

## Research Context
This ticket gives downstream research a stable target for schema naming, validation boundaries, and response semantics.

### Keywords to Search
- `Pydantic schema separation` - create/update/detail/list schema pattern
- `FastAPI validation error` - framework-native error handling options
- `color payload schema` - union or discriminated input structure
- `OpenAPI examples` - documentation support for frontend and testing
- `workflow response shape` - ranked recommendation and ideal target modeling

### Patterns to Investigate
- `contract-first backend design` - define schemas before implementing services
- `shared error envelope` - consistent error output for UI and tests
- `discriminated color input` - payload shape for multiple color formats
- `schema reuse without over-abstraction` - keep contracts clear but minimal

### Key Decisions Made
- Shared validation and contract design should be tracked as a separate ticket.
- Contracts must support all four color input formats from the start.
- Workflow responses must explicitly model ideal target colors and ranked recommendations.
- The contract layer should serve both backend implementation and frontend integration.

## Success Criteria
This ticket is complete when later domain tickets can implement endpoints against stable, explicit contracts.

### Automated Verification
- [ ] Schemas validate valid and invalid payload examples for paints, palettes, workflows, and history.
- [ ] OpenAPI output includes the major request and response models.
- [ ] Validation tests cover malformed color payloads and unsupported workflow combinations.

### Manual Verification
- [ ] A developer can read the schema layer and understand expected endpoint payloads.
- [ ] Frontend work can consume field names, error shapes, and response structures without inventing local assumptions.
- [ ] Later endpoint tickets do not need to redefine base validation rules.

## Related Information
- Parent umbrella ticket: `thoughts/tickets/feature_model_paint_mvp_planning.md`
- Planned predecessor: `thoughts/tickets/debt_model_paint_mvp_scaffold_foundation.md`
- Planned next ticket: `thoughts/tickets/feature_model_paint_data_models_migrations_seed.md`

## Notes
- Do not implement full domain endpoint behavior here; focus on schema and validation foundations.
- Keep auth, ownership rules, and deferred roadmap concerns out of scope.
