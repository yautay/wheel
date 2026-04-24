from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from loguru import logger

from app.api.contracts import router as contract_router
from app.api.errors import register_error_handlers
from app.core.config import get_settings
from app.core.logging import configure_logging

settings = get_settings()
configure_logging(settings)

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    logger.info("Starting backend in {env} mode", env=settings.app_env)
    yield


app = FastAPI(title="Model Paint MVP API", lifespan=lifespan)
register_error_handlers(app)
router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    logger.info("Health endpoint called")
    return {"status": "ok"}


app.include_router(router)
app.include_router(contract_router)
