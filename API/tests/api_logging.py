import logging
from typing import Any


LOGGER = logging.getLogger("demo_api")


def log_api_call(
    *,
    service: str,
    operation: str,
    method: str,
    path: str,
    status_code: int,
    **details: Any,
) -> None:
    context = " ".join(
        f"{key}={value}" for key, value in details.items() if value is not None
    )
    suffix = f" {context}" if context else ""

    LOGGER.info(
        "%s.%s %s %s -> %s%s",
        service,
        operation,
        method,
        path,
        status_code,
        suffix,
    )
