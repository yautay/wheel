from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class WorkflowSnapshot(BaseModel):
    workflow_type: Literal["scale_effect", "modulation"]
    source_type: Literal["catalog", "palette"]
    palette_id: int | None = Field(default=None, ge=1, examples=[2])
    request_payload: dict[str, Any] = Field(default_factory=dict)
    response_payload: dict[str, Any] = Field(default_factory=dict)


class WorkflowHistorySummary(BaseModel):
    id: int = Field(ge=1, examples=[9])
    workflow_type: Literal["scale_effect", "modulation"]
    source_type: Literal["catalog", "palette"]
    palette_id: int | None = Field(default=None, ge=1, examples=[2])
    executed_at: datetime = Field(examples=["2026-04-24T10:15:00Z"])


class WorkflowHistoryListResponse(BaseModel):
    items: list[WorkflowHistorySummary] = Field(default_factory=list)
    total: int = Field(ge=0, examples=[1])


class WorkflowHistoryDetailResponse(WorkflowHistorySummary):
    snapshot: WorkflowSnapshot

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 9,
                "workflow_type": "scale_effect",
                "source_type": "catalog",
                "palette_id": None,
                "executed_at": "2026-04-24T10:15:00Z",
                "snapshot": {
                    "workflow_type": "scale_effect",
                    "source_type": "catalog",
                    "palette_id": None,
                    "request_payload": {
                        "source": {"source_type": "catalog", "palette_id": None},
                        "input_color": {"mode": "HEX", "value": "#4A6B3A"},
                        "strength": 1.0,
                        "limit": 5,
                    },
                    "response_payload": {
                        "workflow": "scale_effect",
                        "source": {"source_type": "catalog", "palette_id": None},
                        "ideal_target_color": {
                            "color_hex": "#536E44",
                            "color_input": {"mode": "HEX", "value": "#536E44"},
                        },
                        "recommendations": [],
                    },
                },
            }
        }
    )


class WorkflowHistoryDeleteResponse(BaseModel):
    deleted: bool = Field(examples=[True])
    id: int = Field(ge=1, examples=[9])
