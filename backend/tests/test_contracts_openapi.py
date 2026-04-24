from fastapi.testclient import TestClient

from app.main import app


def _openapi_doc() -> dict:
    client = TestClient(app)
    response = client.get("/openapi.json")
    assert response.status_code == 200
    return response.json()


def test_openapi_includes_contract_paths_and_models() -> None:
    doc = _openapi_doc()

    expected_paths = {
        "/api/v1/paints",
        "/api/v1/palettes",
        "/api/v1/workflows/scale-effect",
        "/api/v1/workflows/modulation",
        "/api/v1/history",
    }
    assert expected_paths.issubset(doc["paths"].keys())

    schemas = doc["components"]["schemas"]
    expected_schemas = {
        "PaintCreateRequest",
        "PaintDetailResponse",
        "PaletteDetailResponse",
        "ScaleEffectRequest",
        "ScaleEffectResponse",
        "ModulationRequest",
        "ModulationResponse",
        "WorkflowHistoryDetailResponse",
        "ApiErrorResponse",
    }
    assert expected_schemas.issubset(schemas.keys())


def test_openapi_documents_standardized_error_envelope_on_contract_routes() -> None:
    doc = _openapi_doc()

    paints_post = doc["paths"]["/api/v1/paints"]["post"]
    assert "400" in paints_post["responses"]
    assert "422" in paints_post["responses"]

    error_400 = paints_post["responses"]["400"]["content"]["application/json"]["schema"]
    error_422 = paints_post["responses"]["422"]["content"]["application/json"]["schema"]
    assert error_400["$ref"].endswith("/ApiErrorResponse")
    assert error_422["$ref"].endswith("/ApiErrorResponse")


def test_openapi_contains_examples_for_color_modes() -> None:
    doc = _openapi_doc()
    schemas = doc["components"]["schemas"]

    assert schemas["HexColorInput"]["properties"]["value"]["examples"][0] == "#4A6B3A"
    assert schemas["LabColorInput"]["properties"]["l"]["examples"][0] == 42.6
    assert schemas["RgbColorInput"]["properties"]["r"]["examples"][0] == 74
    assert schemas["CmykColorInput"]["properties"]["c"]["examples"][0] == 30.0
