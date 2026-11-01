from dataclasses import dataclass

DEFAULT_USER_AGENT = (
    "mudassir-bot/0.1 (+https://github.com/Mudassir-A/concurrent-web-fetcher)"
)


@dataclass(frozen=True, slots=True)
class FetchConfig:
    concurrency: int = 10
    per_host_rps: float = 10.0
    timeout_s: float = 10.0
    max_attempts: int = 4
    backoff_base_s: float = 0.5
    backoff_cap_s: float = 8.0
    clean_workers: int = 4
    respect_robots: bool = True
    user_agent: str = DEFAULT_USER_AGENT
