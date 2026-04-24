from datetime import datetime, timezone

from fastapi import APIRouter, status

from app.schemas.color import HexColorInput
from app.schemas.common import DeleteResponse
from app.schemas.errors import ApiErrorResponse
from app.schemas.history import (
    WorkflowHistoryDeleteResponse,
    WorkflowHistoryDetailResponse,
    WorkflowHistoryListResponse,
    WorkflowSnapshot,
)
from app.schemas.paint import PaintCreateRequest, PaintDetailResponse, PaintListResponse, PaintSummary, PaintUpdateRequest
from app.schemas.palette import (
    PaletteCreateRequest,
    PaletteDetailResponse,
    PaletteDuplicateRequest,
    PaletteDuplicateResponse,
    PaletteListResponse,
    PaletteMembershipAssignRequest,
    PaletteMembershipRemoveResponse,
    PaletteMembershipReorderRequest,
    PaletteSummary,
    PaletteUpdateRequest,
)
from app.schemas.workflow import (
    IdealTargetColor,
    ModulationLevelResult,
    ModulationRequest,
    ModulationResponse,
    ScaleEffectRequest,
    ScaleEffectResponse,
    WorkflowSource,
)

router = APIRouter(prefix="/api/v1")

STANDARD_ERROR_RESPONSES = {
    status.HTTP_400_BAD_REQUEST: {"model": ApiErrorResponse, "description": "Domain error envelope"},
    status.HTTP_422_UNPROCESSABLE_CONTENT: {
        "model": ApiErrorResponse,
        "description": "Validation error envelope",
    },
}


def _now() -> datetime:
    return datetime.now(timezone.utc)


@router.post(
    "/paints",
    response_model=PaintDetailResponse,
    status_code=status.HTTP_201_CREATED,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["paints"],
    summary="Create paint contract",
)
def create_paint_contract(payload: PaintCreateRequest) -> PaintDetailResponse:
    color_hex = payload.color_hex or "#4A6B3A"
    if isinstance(payload.color_input, HexColorInput):
        color_hex = payload.color_input.value
    now = _now()
    return PaintDetailResponse(
        id=1,
        brand=payload.brand,
        code=payload.code,
        name=payload.name,
        color_hex=color_hex,
        created_at=now,
        updated_at=now,
    )


@router.get(
    "/paints",
    response_model=PaintListResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["paints"],
    summary="List paints contract",
)
def list_paints_contract() -> PaintListResponse:
    return PaintListResponse(items=[PaintSummary(id=1, brand="AK Interactive", code="AK11001", name="Dark Green", color_hex="#4A6B3A")], total=1)


@router.get(
    "/paints/{paint_id}",
    response_model=PaintDetailResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["paints"],
    summary="Get paint detail contract",
)
def get_paint_contract(paint_id: int) -> PaintDetailResponse:
    now = _now()
    return PaintDetailResponse(
        id=paint_id,
        brand="AK Interactive",
        code="AK11001",
        name="Dark Green",
        color_hex="#4A6B3A",
        created_at=now,
        updated_at=now,
    )


@router.patch(
    "/paints/{paint_id}",
    response_model=PaintDetailResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["paints"],
    summary="Update paint contract",
)
def update_paint_contract(paint_id: int, payload: PaintUpdateRequest) -> PaintDetailResponse:
    now = _now()
    return PaintDetailResponse(
        id=paint_id,
        brand=payload.brand or "AK Interactive",
        code=payload.code or "AK11001",
        name=payload.name or "Dark Green",
        color_hex=payload.color_hex or "#4A6B3A",
        created_at=now,
        updated_at=now,
    )


@router.delete(
    "/paints/{paint_id}",
    response_model=DeleteResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["paints"],
    summary="Delete paint contract",
)
def delete_paint_contract(paint_id: int) -> DeleteResponse:
    return DeleteResponse(deleted=True, id=paint_id)


@router.post(
    "/palettes",
    response_model=PaletteDetailResponse,
    status_code=status.HTTP_201_CREATED,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["palettes"],
    summary="Create palette contract",
)
def create_palette_contract(payload: PaletteCreateRequest) -> PaletteDetailResponse:
    now = _now()
    return PaletteDetailResponse(
        id=2,
        name=payload.name,
        description=payload.description,
        paints_count=0,
        paints=[],
        created_at=now,
        updated_at=now,
    )


@router.get(
    "/palettes",
    response_model=PaletteListResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["palettes"],
    summary="List palettes contract",
)
def list_palette_contract() -> PaletteListResponse:
    return PaletteListResponse(
        items=[PaletteSummary(id=2, name="WW2 Armor Greens", description="Go-to greens for armor work", paints_count=1)],
        total=1,
    )


@router.get(
    "/palettes/{palette_id}",
    response_model=PaletteDetailResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["palettes"],
    summary="Get palette detail contract",
)
def get_palette_contract(palette_id: int) -> PaletteDetailResponse:
    now = _now()
    return PaletteDetailResponse(
        id=palette_id,
        name="WW2 Armor Greens",
        description="Go-to greens for armor work",
        paints_count=0,
        paints=[],
        created_at=now,
        updated_at=now,
    )


@router.patch(
    "/palettes/{palette_id}",
    response_model=PaletteDetailResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["palettes"],
    summary="Update palette contract",
)
def update_palette_contract(palette_id: int, payload: PaletteUpdateRequest) -> PaletteDetailResponse:
    now = _now()
    return PaletteDetailResponse(
        id=palette_id,
        name=payload.name or "WW2 Armor Greens",
        description=payload.description,
        paints_count=0,
        paints=[],
        created_at=now,
        updated_at=now,
    )


@router.delete(
    "/palettes/{palette_id}",
    response_model=DeleteResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["palettes"],
    summary="Delete palette contract",
)
def delete_palette_contract(palette_id: int) -> DeleteResponse:
    return DeleteResponse(deleted=True, id=palette_id)


@router.post(
    "/palettes/{palette_id}/paints",
    response_model=PaletteDetailResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["palettes"],
    summary="Assign paint to palette contract",
)
def assign_palette_member_contract(palette_id: int, _: PaletteMembershipAssignRequest) -> PaletteDetailResponse:
    return get_palette_contract(palette_id)


@router.delete(
    "/palettes/{palette_id}/paints/{paint_id}",
    response_model=PaletteMembershipRemoveResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["palettes"],
    summary="Remove paint from palette contract",
)
def remove_palette_member_contract(palette_id: int, paint_id: int) -> PaletteMembershipRemoveResponse:
    return PaletteMembershipRemoveResponse(removed=True, palette_id=palette_id, paint_id=paint_id)


@router.post(
    "/palettes/{palette_id}/paints/reorder",
    response_model=PaletteDetailResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["palettes"],
    summary="Reorder palette membership contract",
)
def reorder_palette_member_contract(palette_id: int, _: PaletteMembershipReorderRequest) -> PaletteDetailResponse:
    return get_palette_contract(palette_id)


@router.post(
    "/palettes/{palette_id}/duplicate",
    response_model=PaletteDuplicateResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["palettes"],
    summary="Duplicate palette contract",
)
def duplicate_palette_contract(palette_id: int, payload: PaletteDuplicateRequest) -> PaletteDuplicateResponse:
    now = _now()
    duplicated = PaletteDetailResponse(
        id=8,
        name=payload.name or "WW2 Armor Greens Copy",
        description="Go-to greens for armor work",
        paints_count=0,
        paints=[],
        created_at=now,
        updated_at=now,
    )
    return PaletteDuplicateResponse(source_palette_id=palette_id, duplicated_palette=duplicated)


@router.post(
    "/workflows/scale-effect",
    response_model=ScaleEffectResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["workflows"],
    summary="Scale effect workflow contract",
)
def scale_effect_contract(payload: ScaleEffectRequest) -> ScaleEffectResponse:
    return ScaleEffectResponse(
        workflow="scale_effect",
        source=payload.source,
        ideal_target_color=IdealTargetColor(
            color_hex="#536E44",
            color_input=HexColorInput(mode="HEX", value="#536E44"),
        ),
        recommendations=[],
    )


@router.post(
    "/workflows/modulation",
    response_model=ModulationResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["workflows"],
    summary="Modulation workflow contract",
)
def modulation_contract(payload: ModulationRequest) -> ModulationResponse:
    levels = []
    for level, target in [
        ("-2", "#2E3F27"),
        ("-1", "#3C522F"),
        ("base", "#4A6B3A"),
        ("+1", "#5B7B4A"),
        ("+2", "#6D8D5B"),
    ]:
        levels.append(
            ModulationLevelResult(
                level=level,
                ideal_target_color=IdealTargetColor(
                    color_hex=target,
                    color_input=HexColorInput(mode="HEX", value=target),
                ),
                recommendations=[],
            )
        )
    return ModulationResponse(workflow="modulation", source=payload.source, levels=levels)


@router.get(
    "/history",
    response_model=WorkflowHistoryListResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["history"],
    summary="List history contract",
)
def list_history_contract() -> WorkflowHistoryListResponse:
    now = _now()
    item = WorkflowHistoryDetailResponse(
        id=9,
        workflow_type="scale_effect",
        source_type="catalog",
        palette_id=None,
        executed_at=now,
        snapshot=WorkflowSnapshot(
            workflow_type="scale_effect",
            source_type="catalog",
            palette_id=None,
            request_payload={"source": {"source_type": "catalog", "palette_id": None}},
            response_payload={"workflow": "scale_effect"},
        ),
    )
    return WorkflowHistoryListResponse(items=[item], total=1)


@router.get(
    "/history/{history_id}",
    response_model=WorkflowHistoryDetailResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["history"],
    summary="Get history detail contract",
)
def get_history_contract(history_id: int) -> WorkflowHistoryDetailResponse:
    now = _now()
    return WorkflowHistoryDetailResponse(
        id=history_id,
        workflow_type="scale_effect",
        source_type="catalog",
        palette_id=None,
        executed_at=now,
        snapshot=WorkflowSnapshot(
            workflow_type="scale_effect",
            source_type="catalog",
            palette_id=None,
            request_payload={"source": {"source_type": "catalog", "palette_id": None}},
            response_payload={"workflow": "scale_effect"},
        ),
    )


@router.delete(
    "/history/{history_id}",
    response_model=WorkflowHistoryDeleteResponse,
    responses=STANDARD_ERROR_RESPONSES,
    tags=["history"],
    summary="Delete history contract",
)
def delete_history_contract(history_id: int) -> WorkflowHistoryDeleteResponse:
    return WorkflowHistoryDeleteResponse(deleted=True, id=history_id)
