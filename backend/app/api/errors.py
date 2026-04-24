from typing import Any

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.schemas.errors import ApiErrorResponse, DomainErrorDetail, ValidationErrorDetail


class DomainError(Exception):
    def __init__(self, code: str, message: str, details: list[DomainErrorDetail] | None = None) -> None:
        self.code = code
        self.message = message
        self.details = details or []
        super().__init__(message)


def _validation_details(exc: RequestValidationError) -> list[dict[str, Any]]:
    details: list[dict[str, Any]] = []
    for error in exc.errors():
        detail = ValidationErrorDetail(
            location=list(error.get("loc", [])),
            message=error.get("msg", "Validation error"),
            error_type=error.get("type", "validation_error"),
            input=error.get("input"),
        )
        details.append(detail.model_dump(exclude_none=True))
    return details


def _domain_details(exc: DomainError) -> list[dict[str, Any]]:
    return [detail.model_dump(exclude_none=True) for detail in exc.details]


def register_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(_: Request, exc: RequestValidationError) -> JSONResponse:
        payload = ApiErrorResponse(
            error={
                "code": "validation_error",
                "message": "Request payload validation failed.",
                "details": _validation_details(exc),
            }
        )
        return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, content=payload.model_dump())

    @app.exception_handler(DomainError)
    async def domain_exception_handler(_: Request, exc: DomainError) -> JSONResponse:
        payload = ApiErrorResponse(
            error={
                "code": exc.code,
                "message": exc.message,
                "details": _domain_details(exc),
            }
        )
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=payload.model_dump())
