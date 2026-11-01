from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel


class Status(StrEnum):
    OK = "ok"
    HTTP_ERROR = "http_error"
    NETWORK_ERROR = "network_error"
    BLOCKED = "blocked_by_robots"
    NOT_HTML = "not_html"


class Page(BaseModel):
    url: str
    status: Status
    attempts: int
    elapsed_ms: int
    fetched_at: datetime
    http_status: int | None = None
    final_url: str | None = None
    title: str | None = None
    text: str | None = None
    word_count: int = 0
    error: str | None = None
