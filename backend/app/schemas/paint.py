from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, model_validator

from app.schemas.color import ColorInput, HexColorInput


class PaintWriteBase(BaseModel):
    brand: str = Field(min_length=1, max_length=120, examples=["AK Interactive"])
    code: str = Field(min_length=1, max_length=80, examples=["AK11001"])
    name: str = Field(min_length=1, max_length=160, examples=["Dark Green"])
    color_hex: str | None = Field(
        default=None,
        pattern=r"^#[0-9A-Fa-f]{6}$",
        examples=["#4A6B3A"],
        description="Legacy color input format. Deprecated in favor of color_input.",
    )
    color_input: ColorInput | None = Field(
        default=None,
        description="Canonical color input. If both color_hex and color_input are provided, color_input takes precedence.",
    )

    @model_validator(mode="after")
    def validate_color_bridge(self) -> "PaintWriteBase":
        if self.color_hex is None and self.color_input is None:
            msg = "Either color_hex or color_input must be provided."
            raise ValueError(msg)

        if self.color_hex and self.color_input and not isinstance(self.color_input, HexColorInput):
            msg = "color_hex can only be combined with color_input when color_input.mode is HEX."
            raise ValueError(msg)

        if self.color_hex and isinstance(self.color_input, HexColorInput):
            if self.color_hex.upper() != self.color_input.value.upper():
                msg = "color_hex must match color_input.value when both are provided."
                raise ValueError(msg)

        return self


class PaintCreateRequest(PaintWriteBase):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "brand": "AK Interactive",
                "code": "AK11001",
                "name": "Dark Green",
                "color_hex": "#4A6B3A",
                "color_input": {"mode": "HEX", "value": "#4A6B3A"},
            }
        }
    )


class PaintUpdateRequest(BaseModel):
    brand: str | None = Field(default=None, min_length=1, max_length=120, examples=["AK Interactive"])
    code: str | None = Field(default=None, min_length=1, max_length=80, examples=["AK11001"])
    name: str | None = Field(default=None, min_length=1, max_length=160, examples=["Dark Green"])
    color_hex: str | None = Field(
        default=None,
        pattern=r"^#[0-9A-Fa-f]{6}$",
        examples=["#4A6B3A"],
        description="Legacy color input format. Deprecated in favor of color_input.",
    )
    color_input: ColorInput | None = Field(
        default=None,
        description="Canonical color input. If both color_hex and color_input are provided, color_input takes precedence.",
    )

    @model_validator(mode="after")
    def validate_color_bridge(self) -> "PaintUpdateRequest":
        if self.color_hex and self.color_input and not isinstance(self.color_input, HexColorInput):
            msg = "color_hex can only be combined with color_input when color_input.mode is HEX."
            raise ValueError(msg)

        if self.color_hex and isinstance(self.color_input, HexColorInput):
            if self.color_hex.upper() != self.color_input.value.upper():
                msg = "color_hex must match color_input.value when both are provided."
                raise ValueError(msg)

        return self


class PaintSummary(BaseModel):
    id: int = Field(ge=1, examples=[1])
    brand: str = Field(min_length=1, max_length=120, examples=["AK Interactive"])
    code: str = Field(min_length=1, max_length=80, examples=["AK11001"])
    name: str = Field(min_length=1, max_length=160, examples=["Dark Green"])
    color_hex: str = Field(pattern=r"^#[0-9A-Fa-f]{6}$", examples=["#4A6B3A"])


class PaintDetailResponse(PaintSummary):
    created_at: datetime = Field(examples=["2026-04-24T10:15:00Z"])
    updated_at: datetime = Field(examples=["2026-04-24T10:15:00Z"])


class PaintListResponse(BaseModel):
    items: list[PaintSummary] = Field(default_factory=list)
    total: int = Field(ge=0, examples=[1])
