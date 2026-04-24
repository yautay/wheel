from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from app.schemas.color import ColorInput
from app.schemas.common import PaintRecommendation


class WorkflowSource(BaseModel):
    source_type: Literal["catalog", "palette"] = Field(examples=["catalog"])
    palette_id: int | None = Field(default=None, ge=1, examples=[2])

    @model_validator(mode="after")
    def validate_source_scope(self) -> "WorkflowSource":
        if self.source_type == "palette" and self.palette_id is None:
            msg = "palette_id is required when source_type is palette."
            raise ValueError(msg)
        if self.source_type == "catalog" and self.palette_id is not None:
            msg = "palette_id is not allowed when source_type is catalog."
            raise ValueError(msg)
        return self


class ScaleEffectRequest(BaseModel):
    source: WorkflowSource
    input_color: ColorInput
    strength: float = Field(default=1.0, gt=0.0, le=2.0, examples=[1.0])
    limit: int = Field(default=5, ge=1, le=25, examples=[5])

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "source": {"source_type": "catalog", "palette_id": None},
                "input_color": {"mode": "HEX", "value": "#4A6B3A"},
                "strength": 1.0,
                "limit": 5,
            }
        }
    )


class IdealTargetColor(BaseModel):
    color_hex: str = Field(pattern=r"^#[0-9A-Fa-f]{6}$", examples=["#536E44"])
    color_input: ColorInput | None = Field(default=None)


class ScaleEffectResponse(BaseModel):
    workflow: Literal["scale_effect"] = "scale_effect"
    source: WorkflowSource
    ideal_target_color: IdealTargetColor
    recommendations: list[PaintRecommendation] = Field(default_factory=list)


class ModulationLevelResult(BaseModel):
    level: Literal["-2", "-1", "base", "+1", "+2"]
    ideal_target_color: IdealTargetColor
    recommendations: list[PaintRecommendation] = Field(default_factory=list)


class ModulationRequest(BaseModel):
    source: WorkflowSource
    input_color: ColorInput
    contrast: float = Field(default=1.0, gt=0.0, le=2.0, examples=[1.0])
    limit: int = Field(default=5, ge=1, le=25, examples=[5])

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "source": {"source_type": "palette", "palette_id": 2},
                "input_color": {"mode": "RGB", "r": 74, "g": 107, "b": 58},
                "contrast": 1.0,
                "limit": 5,
            }
        }
    )


class ModulationResponse(BaseModel):
    workflow: Literal["modulation"] = "modulation"
    source: WorkflowSource
    levels: list[ModulationLevelResult] = Field(default_factory=list, min_length=5, max_length=5)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "workflow": "modulation",
                "source": {"source_type": "catalog", "palette_id": None},
                "levels": [
                    {
                        "level": "-2",
                        "ideal_target_color": {
                            "color_hex": "#2E3F27",
                            "color_input": {"mode": "HEX", "value": "#2E3F27"},
                        },
                        "recommendations": [
                            {
                                "paint_id": 7,
                                "brand": "AK Interactive",
                                "code": "AK11001",
                                "name": "Dark Green",
                                "color_hex": "#4A6B3A",
                                "match_score": 0.89,
                            }
                        ],
                    },
                    {
                        "level": "-1",
                        "ideal_target_color": {
                            "color_hex": "#3C522F",
                            "color_input": {"mode": "HEX", "value": "#3C522F"},
                        },
                        "recommendations": []
                    },
                    {
                        "level": "base",
                        "ideal_target_color": {
                            "color_hex": "#4A6B3A",
                            "color_input": {"mode": "HEX", "value": "#4A6B3A"},
                        },
                        "recommendations": []
                    },
                    {
                        "level": "+1",
                        "ideal_target_color": {
                            "color_hex": "#5B7B4A",
                            "color_input": {"mode": "HEX", "value": "#5B7B4A"},
                        },
                        "recommendations": []
                    },
                    {
                        "level": "+2",
                        "ideal_target_color": {
                            "color_hex": "#6D8D5B",
                            "color_input": {"mode": "HEX", "value": "#6D8D5B"},
                        },
                        "recommendations": []
                    },
                ],
            }
        }
    )
