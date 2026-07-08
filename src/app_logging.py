# src/doc_processor/logger.py
import logging
import os

DEFAULT_LOG_FORMAT = "%(asctime)s %(levelname)s [%(name)s] %(message)s"

def configure_logging() -> None:
    level_name = os.getenv("LOG_LEVEL", "WARNING").upper()
    level = getattr(logging, level_name, logging.INFO)

    logging.basicConfig(
        level=level,
        format=DEFAULT_LOG_FORMAT,
        force=True,
    )

