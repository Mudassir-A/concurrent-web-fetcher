from datetime import UTC, datetime

from pydantic import ValidationError

from fetcher.models import Page, Status

page = Page(
    url="https://docs.python.org/3/library/asyncio.html",
    status=Status.OK,
    attempts=1,
    elapsed_ms=212,
    fetched_at=datetime(2026, 10, 21, 9, 30, tzinfo=UTC),
    http_status=200,
    title="asyncio - Asynchronous I/O",
    text="asyncio is a library to write concurrent code using the async/await syntax.",
    word_count=12,
)
print(page.model_dump_json(indent=2))

bad = {
    "url": "https://x.com",
    "status": "okay",
    "attempts": "two",
    "elapsed_ms": 5,
    "fetched_at": "today",
}
try:
    Page.model_validate(bad)
except ValidationError as e:
    print(e)
