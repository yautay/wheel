from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field


class HexColorInput(BaseModel):
    mode: Literal["HEX"] = "HEX"
    value: str = Field(pattern=r"^#[0-9A-Fa-f]{6}$", examples=["#4A6B3A"])


class LabColorInput(BaseModel):
    mode: Literal["LAB"] = "LAB"
    l: float = Field(ge=0.0, le=100.0, examples=[42.6])
    a: float = Field(ge=-128.0, le=127.0, examples=[-12.3])
    b: float = Field(ge=-128.0, le=127.0, examples=[18.9])


class RgbColorInput(BaseModel):
    mode: Literal["RGB"] = "RGB"
    r: int = Field(ge=0, le=255, examples=[74])
    g: int = Field(ge=0, le=255, examples=[107])
    b: int = Field(ge=0, le=255, examples=[58])


class CmykColorInput(BaseModel):
    mode: Literal["CMYK"] = "CMYK"
    c: float = Field(ge=0.0, le=100.0, examples=[30.0])
    m: float = Field(ge=0.0, le=100.0, examples=[0.0])
    y: float = Field(ge=0.0, le=100.0, examples=[45.0])
    k: float = Field(ge=0.0, le=100.0, examples=[58.0])


ColorInput = Annotated[
    HexColorInput | LabColorInput | RgbColorInput | CmykColorInput,
    Field(discriminator="mode"),
]


class ColorInputExamples(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {"mode": "HEX", "value": "#4A6B3A"},
                {"mode": "LAB", "l": 42.6, "a": -12.3, "b": 18.9},
                {"mode": "RGB", "r": 74, "g": 107, "b": 58},
                {"mode": "CMYK", "c": 30.0, "m": 0.0, "y": 45.0, "k": 58.0},
            ]
        }
    )
