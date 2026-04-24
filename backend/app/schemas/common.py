from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class IdMixin(BaseModel):
    id: int = Field(ge=1, examples=[1])


class EntityTimestamps(BaseModel):
    created_at: datetime = Field(examples=["2026-04-24T10:15:00Z"])
    updated_at: datetime = Field(examples=["2026-04-24T10:15:00Z"])


class ListMeta(BaseModel):
    total: int = Field(ge=0, examples=[1])


class PaintRecommendation(BaseModel):
    paint_id: int = Field(ge=1, examples=[7])
    brand: str = Field(min_length=1, max_length=120, examples=["AK Interactive"])
    code: str = Field(min_length=1, max_length=80, examples=["AK11001"])
    name: str = Field(min_length=1, max_length=160, examples=["Dark Green"])
    color_hex: str = Field(pattern=r"^#[0-9A-Fa-f]{6}$", examples=["#4A6B3A"])
    match_score: float = Field(ge=0.0, le=1.0, examples=[0.92])

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "paint_id": 7,
                "brand": "AK Interactive",
                "code": "AK11001",
                "name": "Dark Green",
                "color_hex": "#4A6B3A",
                "match_score": 0.92,
            }
        }
    )


class DeleteResponse(BaseModel):
    deleted: bool = Field(examples=[True])
    id: int = Field(ge=1, examples=[1])
