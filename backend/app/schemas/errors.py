from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ValidationErrorDetail(BaseModel):
    location: list[str | int] = Field(default_factory=list, examples=[["body", "color_input", "mode"]])
    message: str = Field(examples=["Field required"])
    error_type: str = Field(examples=["missing"])
    input: Any | None = None


class DomainErrorDetail(BaseModel):
    field: str | None = Field(default=None, examples=["palette_id"])
    reason: str = Field(examples=["palette_not_found"])
    context: dict[str, Any] = Field(default_factory=dict)


class ApiError(BaseModel):
    code: str = Field(examples=["validation_error"])
    message: str = Field(examples=["Request payload validation failed."])
    details: list[dict[str, Any]] = Field(default_factory=list)


class ApiErrorResponse(BaseModel):
    error: ApiError

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "error": {
                    "code": "validation_error",
                    "message": "Request payload validation failed.",
                    "details": [
                        {
                            "location": ["body", "color_input", "mode"],
                            "message": "Field required",
                            "error_type": "missing",
                        }
                    ],
                }
            }
        }
    )
