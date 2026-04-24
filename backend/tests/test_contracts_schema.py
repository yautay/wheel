from datetime import datetime, timezone

import pytest
from fastapi.testclient import TestClient
from pydantic import TypeAdapter, ValidationError

from app.main import app
from app.schemas.color import ColorInput
from app.schemas.history import WorkflowHistoryDetailResponse, WorkflowSnapshot
from app.schemas.paint import PaintCreateRequest
from app.schemas.workflow import IdealTargetColor, ModulationLevelResult, ModulationResponse, ScaleEffectResponse


def test_color_input_accepts_all_supported_modes() -> None:
    adapter = TypeAdapter(ColorInput)

    payloads = [
        {"mode": "HEX", "value": "#4A6B3A"},
        {"mode": "LAB", "l": 42.6, "a": -12.3, "b": 18.9},
        {"mode": "RGB", "r": 74, "g": 107, "b": 58},
        {"mode": "CMYK", "c": 30.0, "m": 0.0, "y": 45.0, "k": 58.0},
    ]

    for payload in payloads:
        validated = adapter.validate_python(payload)
        assert validated.mode == payload["mode"]


@pytest.mark.parametrize(
    ("payload", "snippet"),
    [
        ({"mode": "HEX", "value": "123456"}, "String should match pattern"),
        ({"mode": "LAB", "l": 101, "a": 0, "b": 0}, "less than or equal to 100"),
        ({"mode": "RGB", "r": 256, "g": 10, "b": 10}, "less than or equal to 255"),
        ({"mode": "CMYK", "c": -1, "m": 0, "y": 0, "k": 0}, "greater than or equal to 0"),
    ],
)
def test_color_input_rejects_malformed_and_out_of_range_values(payload: dict[str, object], snippet: str) -> None:
    adapter = TypeAdapter(ColorInput)

    with pytest.raises(ValidationError) as exc_info:
        adapter.validate_python(payload)

    assert snippet in str(exc_info.value)


def test_paint_create_requires_color_hex_or_color_input() -> None:
    with pytest.raises(ValidationError):
        PaintCreateRequest(brand="AK", code="A1", name="Green")


def test_paint_create_rejects_unsupported_color_hex_and_color_input_combination() -> None:
    with pytest.raises(ValidationError) as exc_info:
        PaintCreateRequest(
            brand="AK",
            code="A1",
            name="Green",
            color_hex="#4A6B3A",
            color_input={"mode": "LAB", "l": 42.6, "a": -12.3, "b": 18.9},
        )

    assert "color_hex can only be combined" in str(exc_info.value)


def test_paint_create_rejects_mismatched_hex_bridge_values() -> None:
    with pytest.raises(ValidationError) as exc_info:
        PaintCreateRequest(
            brand="AK",
            code="A1",
            name="Green",
            color_hex="#4A6B3A",
            color_input={"mode": "HEX", "value": "#001122"},
        )

    assert "color_hex must match color_input.value" in str(exc_info.value)


def test_invalid_combination_returns_standardized_error_envelope() -> None:
    client = TestClient(app)

    response = client.post(
        "/api/v1/paints",
        json={
            "brand": "AK",
            "code": "A1",
            "name": "Green",
            "color_hex": "#4A6B3A",
            "color_input": {"mode": "LAB", "l": 42.6, "a": -12.3, "b": 18.9},
        },
    )

    body = response.json()
    assert response.status_code == 422
    assert set(body.keys()) == {"error"}
    assert body["error"]["code"] == "validation_error"
    assert isinstance(body["error"]["details"], list)


def test_workflow_responses_include_ideal_target_and_ranked_recommendations() -> None:
    scale = ScaleEffectResponse(
        workflow="scale_effect",
        source={"source_type": "catalog", "palette_id": None},
        ideal_target_color=IdealTargetColor(
            color_hex="#536E44",
            color_input={"mode": "HEX", "value": "#536E44"},
        ),
        recommendations=[
            {
                "paint_id": 7,
                "brand": "AK Interactive",
                "code": "AK11001",
                "name": "Dark Green",
                "color_hex": "#4A6B3A",
                "match_score": 0.92,
            }
        ],
    )
    assert scale.ideal_target_color.color_hex == "#536E44"
    assert scale.recommendations[0].match_score == pytest.approx(0.92)

    levels = [
        ModulationLevelResult(
            level=level,
            ideal_target_color=IdealTargetColor(
                color_hex="#536E44",
                color_input={"mode": "HEX", "value": "#536E44"},
            ),
            recommendations=[
                {
                    "paint_id": 7,
                    "brand": "AK Interactive",
                    "code": "AK11001",
                    "name": "Dark Green",
                    "color_hex": "#4A6B3A",
                    "match_score": 0.9,
                }
            ],
        )
        for level in ["-2", "-1", "base", "+1", "+2"]
    ]
    modulation = ModulationResponse(
        workflow="modulation",
        source={"source_type": "palette", "palette_id": 2},
        levels=levels,
    )
    assert len(modulation.levels) == 5
    assert all(level.ideal_target_color.color_hex for level in modulation.levels)
    assert all(level.recommendations for level in modulation.levels)


def test_history_detail_contains_replay_friendly_snapshots() -> None:
    detail = WorkflowHistoryDetailResponse(
        id=11,
        workflow_type="modulation",
        source_type="palette",
        palette_id=2,
        executed_at=datetime.now(timezone.utc),
        snapshot=WorkflowSnapshot(
            workflow_type="modulation",
            source_type="palette",
            palette_id=2,
            request_payload={"input_color": {"mode": "HEX", "value": "#4A6B3A"}},
            response_payload={"levels": [{"level": "base", "recommendations": []}]},
        ),
    )

    assert "input_color" in detail.snapshot.request_payload
    assert "levels" in detail.snapshot.response_payload
