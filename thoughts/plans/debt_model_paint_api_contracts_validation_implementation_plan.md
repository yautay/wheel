# DEBT-002 API Contracts and Validation Foundations Implementation Plan

## Overview

Implement a contract-first API foundation for the model paint MVP by introducing shared request/response schemas, reusable color-input validation, a unified error envelope, and OpenAPI/Swagger-visible contracts for paints, palettes, workflows, and history. This work intentionally defines transport contracts and validation semantics before endpoint business logic so downstream tickets can implement against stable shapes.

## Current State Analysis

The repository has backend and frontend scaffolding, but no domain contract layer yet:
- FastAPI app currently exposes only `GET /health` and a single router include (`backend/app/main.py:19`, `backend/app/main.py:23`, `backend/app/main.py:29`).
- No domain API schemas exist yet; current Pydantic usage is settings-only (`backend/app/core/config.py:6`).
- Backend test pattern exists but is minimal (health smoke only) (`backend/tests/test_health.py:6`).
- DEBT-002 requires explicit shared schemas, color-mode union support, validation semantics, a standard error response, and OpenAPI visibility (`thoughts/tickets/debt_model_paint_api_contracts_validation.md:23`, `thoughts/tickets/debt_model_paint_api_contracts_validation.md:24`, `thoughts/tickets/debt_model_paint_api_contracts_validation.md:27`, `thoughts/tickets/debt_model_paint_api_contracts_validation.md:28`).

## Desired End State

After this plan is implemented, the backend exposes a stable and documented contract layer that includes:
- Shared schemas for create/update/list/detail/workflow/history payloads.
- A canonical discriminated color input contract supporting `HEX`, `LAB`, `RGB`, and `CMYK`.
- A standardized API error envelope for both validation and domain errors.
- OpenAPI model publication and Swagger UI discoverability for all major contract shapes.
- Contract validation and OpenAPI assertions covered by automated tests.

### Key Discoveries:
- DEBT-002 is intentionally separated from domain endpoint behavior and should focus on schema/validation foundations (`thoughts/tickets/debt_model_paint_api_contracts_validation.md:84`).
- Downstream API tickets explicitly depend on reusable shared contracts/validation (`thoughts/tickets/feature_model_paint_paints_crud_api.md:30`, `thoughts/tickets/feature_model_paint_palettes_management_api.md:30`, `thoughts/tickets/feature_model_paint_scale_effect_workflow.md:30`, `thoughts/tickets/feature_model_paint_modulation_workflow.md:30`).
- Workflow contracts must model ideal target colors and ranked recommendations with match scores (`thoughts/tickets/debt_model_paint_api_contracts_validation.md:25`, `thoughts/tickets/feature_model_paint_scale_effect_workflow.md:27`, `thoughts/tickets/feature_model_paint_modulation_workflow.md:29`).
- Frontend routes for paints/palettes/workflows/history already exist, so consistent payload naming now reduces integration churn (`frontend/src/router/index.ts:9`, `frontend/src/router/index.ts:14`, `frontend/src/router/index.ts:19`, `frontend/src/router/index.ts:24`, `frontend/src/router/index.ts:29`).

## What We're NOT Doing

- Implementing full paints/palettes/workflow/history domain logic in services/repositories.
- Implementing data persistence models/migrations (belongs to FEATURE-002 and later tickets).
- Implementing auth/ownership validation rules (explicitly out of DEBT-002 scope).
- Implementing import/export contracts (belongs to FEATURE-009).
- Finalizing workflow algorithms or score math semantics beyond transport contract fields.

## Implementation Approach

Use a contract-first transport layer with explicit schema separation and minimal placeholder endpoint surface to publish schemas in OpenAPI/Swagger now, while leaving business behavior for downstream feature tickets.

Key approach decisions for this implementation:
- Use shared recommendation submodels and separate top-level response models per workflow.
- Use a unified error envelope for validation and domain errors.
- Support both legacy `color_hex` input and new canonical `color_input` payloads for create/update contracts (with explicit precedence and deprecation note in docs/examples).
- Expose contract models through FastAPI routes on future-real API paths to avoid later OpenAPI/path churn.

## Phase 1: Contract Foundation and Module Layout

### Overview
Create schema package structure, naming conventions, and base contract primitives reused across all domains.

### Changes Required:

#### 1. Contract module scaffolding
**File**: `backend/app/schemas/__init__.py`
**Changes**: Add schema package exports and stable import surface.

#### 2. Shared base schemas
**File**: `backend/app/schemas/common.py`
**Changes**: Add base paging/list metadata models (if needed for MVP list responses), timestamps, IDs, and shared recommendation item model.

#### 3. Unified API error models
**File**: `backend/app/schemas/errors.py`
**Changes**: Define standard error envelope and typed detail structures for validation/domain cases.

```python
class ApiError(BaseModel):
    code: str
    message: str
    details: list[dict[str, Any]] = Field(default_factory=list)


class ApiErrorResponse(BaseModel):
    error: ApiError
```

### Success Criteria:

#### Automated Verification:
- [x] Schema modules import successfully: `cd backend && uv run python -c "from app.schemas.errors import ApiErrorResponse"`
- [x] Backend tests pass after module introduction: `cd backend && uv run pytest`

#### Manual Verification:
- [x] Contract package structure is clear to developers starting downstream tickets.
- [x] Error envelope shape is understandable and consistent for frontend consumers.

---

## Phase 2: Canonical Color Input Contract and Validation Rules

### Overview
Define canonical color input schemas with discriminated union support and strict validation boundaries.

### Changes Required:

#### 1. Color input schema family
**File**: `backend/app/schemas/color.py`
**Changes**: Add discriminated union for `HEX`, `LAB`, `RGB`, `CMYK` with mode-specific required fields and range validation.

```python
class HexColorInput(BaseModel):
    mode: Literal["HEX"]
    value: str


class LabColorInput(BaseModel):
    mode: Literal["LAB"]
    l: float
    a: float
    b: float


ColorInput = Annotated[
    Union[HexColorInput, LabColorInput, RgbColorInput, CmykColorInput],
    Field(discriminator="mode"),
]
```

#### 2. Legacy compatibility bridge
**File**: `backend/app/schemas/paint.py`
**Changes**: Allow both `color_hex` and `color_input` in create/update request schemas with documented precedence and validation failures for unsupported combinations.

#### 3. Validation error mapping rules
**File**: `backend/app/api/errors.py`
**Changes**: Map FastAPI `RequestValidationError` and domain exceptions into `ApiErrorResponse`.

### Success Criteria:

#### Automated Verification:
- [x] Tests validate accepted payloads for all 4 color modes: `cd backend && uv run pytest backend/tests/test_contracts_schema.py`
- [x] Tests validate malformed/out-of-range colors are rejected: `cd backend && uv run pytest backend/tests/test_contracts_schema.py`
- [x] Tests validate unsupported combinations fail with standardized error shape: `cd backend && uv run pytest backend/tests/test_contracts_schema.py`

#### Manual Verification:
- [x] A developer can infer valid color payloads from schema definitions and examples.
- [x] Error payloads for invalid color inputs are consistent and frontend-readable.

---

## Phase 3: Domain Contract Schemas (Paints, Palettes, Workflows, History)

### Overview
Define explicit domain request/response contracts with create/update/list/detail/workflow separation.

### Changes Required:

#### 1. Paint contracts
**File**: `backend/app/schemas/paint.py`
**Changes**: Add create/update/list/detail models and shared field constraints aligned with future CRUD/search/sort needs.

#### 2. Palette and membership contracts
**File**: `backend/app/schemas/palette.py`
**Changes**: Add palette create/update/list/detail, ordered membership response models, membership mutation contracts (assign/remove/reorder), duplicate request/response contract.

#### 3. Workflow contracts
**File**: `backend/app/schemas/workflow.py`
**Changes**: Add scale-effect and modulation request/response schemas, source scope contract (`catalog` vs `palette`), ideal target color outputs, ranked recommendations with match scores.

#### 4. History contracts
**File**: `backend/app/schemas/history.py`
**Changes**: Add list/detail/delete response contracts and full request/response snapshot shapes required for replay-friendly history.

### Success Criteria:

#### Automated Verification:
- [x] Domain schemas validate representative valid and invalid examples: `cd backend && uv run pytest backend/tests/test_contracts_schema.py`
- [x] Workflow schemas include ideal target color and ranked recommendations in both scale and modulation responses: `cd backend && uv run pytest backend/tests/test_contracts_schema.py`
- [x] History schemas include full request/response snapshot contract fields: `cd backend && uv run pytest backend/tests/test_contracts_schema.py`

#### Manual Verification:
- [x] Frontend developer can map forms and result views directly from schema names/fields.
- [x] Downstream backend tickets can reuse contracts without redefining base payloads.

---

## Phase 4: FastAPI/OpenAPI/Swagger Publication

### Overview
Expose contract schemas in generated OpenAPI and Swagger UI using placeholder contract endpoints on future-real paths.

### Changes Required:

#### 1. Contract publication router(s)
**File**: `backend/app/api/contracts.py`
**Changes**: Add contract-only route handlers for paints/palettes/workflows/history using `response_model`, request models, standardized error responses, tags, and summaries.

#### 2. App router registration
**File**: `backend/app/main.py`
**Changes**: Include contract router under API v1 prefix without replacing existing health route.

#### 3. OpenAPI example payloads
**File**: `backend/app/schemas/*.py`
**Changes**: Add `json_schema_extra` / field examples for key request and response models, especially color input variants and workflow responses.

### Success Criteria:

#### Automated Verification:
- [x] OpenAPI includes major request/response models for paints, palettes, workflows, and history: `cd backend && uv run pytest backend/tests/test_contracts_openapi.py`
- [x] OpenAPI includes standardized error response models on contract routes: `cd backend && uv run pytest backend/tests/test_contracts_openapi.py`
- [x] Backend test suite stays green: `cd backend && uv run pytest`

#### Manual Verification:
- [x] Swagger UI loads successfully at `/docs`.
- [x] Contract endpoints and models are visible and readable in Swagger.
- [x] Swagger examples cover `HEX`, `LAB`, `RGB`, and `CMYK` input modes.

---

## Phase 5: Contract Validation and OpenAPI Test Coverage

### Overview
Add targeted tests ensuring contracts remain stable and visible as downstream tickets evolve.

### Changes Required:

#### 1. Schema validation tests
**File**: `backend/tests/test_contracts_schema.py`
**Changes**: Add positive/negative cases for domain contracts, color union validation, and unsupported combinations.

#### 2. OpenAPI assertions
**File**: `backend/tests/test_contracts_openapi.py`
**Changes**: Assert path presence, schema component presence, error model presence, and examples in `/openapi.json`.

```python
def test_openapi_includes_contract_models() -> None:
    client = TestClient(app)
    doc = client.get("/openapi.json").json()
    assert "PaintCreateRequest" in doc["components"]["schemas"]
```

### Success Criteria:

#### Automated Verification:
- [x] Contract schema tests pass: `cd backend && uv run pytest backend/tests/test_contracts_schema.py`
- [x] OpenAPI contract tests pass: `cd backend && uv run pytest backend/tests/test_contracts_openapi.py`
- [x] Integrated smoke path remains green: `just smoke`

#### Manual Verification:
- [x] Contract changes are detectable through failing tests if schemas drift.
- [x] A developer can quickly validate contract integrity from tests + Swagger docs.

---

## Testing Strategy

### Unit Tests:
- Validate each color mode payload (`HEX`, `LAB`, `RGB`, `CMYK`) accepts valid fields and rejects malformed data.
- Validate create/update contract rules for mixed `color_hex` + `color_input` combinations.
- Validate workflow source scope contracts (`catalog` vs `palette`) and required fields.
- Validate history schema snapshot structures are replay-friendly.

### Integration Tests:
- Assert `/openapi.json` contains major contract models and route references.
- Assert route-level error responses are documented with standardized envelope.
- Assert Swagger/OpenAPI publication does not break existing `/health` behavior.

### Manual Testing Steps:
1. Start backend and open `http://127.0.0.1:8000/docs`.
2. Verify paints/palettes/workflows/history contract routes and schema models are present.
3. Expand model examples and confirm all four color modes are documented.
4. Trigger a validation error from Swagger “Try it out” and verify error envelope shape.
5. Confirm `GET /health` still returns `{"status": "ok"}`.

## Performance Considerations

- Keep contract routes lightweight and side-effect free; avoid DB access in placeholder handlers.
- Keep schema validation strict but deterministic to avoid hidden coercion costs and ambiguous parsing.
- Avoid deep generic layers; explicit models keep maintenance and import cost lower for MVP.

## Migration Notes

- This ticket introduces transport contracts only; DB migrations remain owned by FEATURE-002.
- Downstream tickets should import and reuse DEBT-002 schema models instead of redefining local payload classes.
- If legacy `color_hex` fields are retired later, perform explicit deprecation in a future ticket rather than silently removing support.

## References

- Original ticket: `thoughts/tickets/debt_model_paint_api_contracts_validation.md`
- Related review: `thoughts/reviews/debt_model_paint_mvp_scaffold_foundation_implementation_plan-review.md`
- Umbrella ticket: `thoughts/tickets/feature_model_paint_mvp_planning.md`
- Execution order: `thoughts/tickets/model_paint_mvp_execution_order.md`
- Downstream dependencies:
  - `thoughts/tickets/feature_model_paint_paints_crud_api.md`
  - `thoughts/tickets/feature_model_paint_palettes_management_api.md`
  - `thoughts/tickets/feature_model_paint_scale_effect_workflow.md`
  - `thoughts/tickets/feature_model_paint_modulation_workflow.md`
  - `thoughts/tickets/feature_model_paint_workflow_history_api.md`
