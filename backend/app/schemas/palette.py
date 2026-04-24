from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class PaletteCreateRequest(BaseModel):
    name: str = Field(min_length=1, max_length=160, examples=["WW2 Armor Greens"])
    description: str | None = Field(default=None, max_length=500, examples=["Go-to greens for armor work"])


class PaletteUpdateRequest(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=160, examples=["WW2 Armor Greens"])
    description: str | None = Field(default=None, max_length=500, examples=["Go-to greens for armor work"])


class PaletteSummary(BaseModel):
    id: int = Field(ge=1, examples=[2])
    name: str = Field(min_length=1, max_length=160, examples=["WW2 Armor Greens"])
    description: str | None = Field(default=None, max_length=500, examples=["Go-to greens for armor work"])
    paints_count: int = Field(ge=0, examples=[12])


class PalettePaintMember(BaseModel):
    paint_id: int = Field(ge=1, examples=[7])
    position: int = Field(ge=0, examples=[0])
    brand: str = Field(min_length=1, max_length=120, examples=["AK Interactive"])
    code: str = Field(min_length=1, max_length=80, examples=["AK11001"])
    name: str = Field(min_length=1, max_length=160, examples=["Dark Green"])
    color_hex: str = Field(pattern=r"^#[0-9A-Fa-f]{6}$", examples=["#4A6B3A"])


class PaletteDetailResponse(PaletteSummary):
    paints: list[PalettePaintMember] = Field(default_factory=list)
    created_at: datetime = Field(examples=["2026-04-24T10:15:00Z"])
    updated_at: datetime = Field(examples=["2026-04-24T10:15:00Z"])


class PaletteListResponse(BaseModel):
    items: list[PaletteSummary] = Field(default_factory=list)
    total: int = Field(ge=0, examples=[1])


class PaletteMembershipAssignRequest(BaseModel):
    paint_id: int = Field(ge=1, examples=[7])
    position: int | None = Field(default=None, ge=0, examples=[0])


class PaletteMembershipRemoveResponse(BaseModel):
    removed: bool = Field(examples=[True])
    palette_id: int = Field(ge=1, examples=[2])
    paint_id: int = Field(ge=1, examples=[7])


class PaletteMembershipReorderRequest(BaseModel):
    paint_ids: list[int] = Field(min_length=1, examples=[[7, 9, 3]])


class PaletteDuplicateRequest(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=160, examples=["WW2 Armor Greens Copy"])


class PaletteDuplicateResponse(BaseModel):
    source_palette_id: int = Field(ge=1, examples=[2])
    duplicated_palette: PaletteDetailResponse

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "source_palette_id": 2,
                "duplicated_palette": {
                    "id": 8,
                    "name": "WW2 Armor Greens Copy",
                    "description": "Go-to greens for armor work",
                    "paints_count": 2,
                    "paints": [
                        {
                            "paint_id": 7,
                            "position": 0,
                            "brand": "AK Interactive",
                            "code": "AK11001",
                            "name": "Dark Green",
                            "color_hex": "#4A6B3A",
                        }
                    ],
                    "created_at": "2026-04-24T10:15:00Z",
                    "updated_at": "2026-04-24T10:15:00Z",
                },
            }
        }
    )
