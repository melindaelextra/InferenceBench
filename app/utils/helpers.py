"""General utility helpers."""

from datetime import datetime


def utc_timestamp() -> str:
    """Return the current UTC timestamp in ISO format."""
    return datetime.utcnow().isoformat()
