from __future__ import annotations

import time
from collections import defaultdict
from dataclasses import dataclass
from typing import Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse, Response


@dataclass
class Bucket:
    tokens: float
    last: float


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, requests_per_minute: int = 60, burst: int = 30):
        super().__init__(app)
        self.rate = requests_per_minute / 60.0
        self.burst = float(burst)
        self.buckets: dict[str, Bucket] = defaultdict(lambda: Bucket(tokens=self.burst, last=time.monotonic()))

    async def dispatch(self, request: Request, call_next: Callable[[Request], Response]) -> Response:
        client_ip = request.client.host if request.client else "anonymous"
        bucket = self.buckets[client_ip]

        now = time.monotonic()
        elapsed = now - bucket.last
        bucket.tokens = min(self.burst, bucket.tokens + elapsed * self.rate)
        bucket.last = now

        if bucket.tokens < 1.0:
            return JSONResponse({"detail": "Rate limit exceeded"}, status_code=429)

        bucket.tokens -= 1.0
        return await call_next(request)


