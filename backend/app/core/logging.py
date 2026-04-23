import sys

from loguru import logger

from app.core.config import Settings


def configure_logging(settings: Settings) -> None:
    logger.remove()
    logger.add(
        sys.stdout,
        level=settings.log_level.upper(),
        format="{time:YYYY-MM-DD HH:mm:ss} | {level:<8} | {message}",
    )
