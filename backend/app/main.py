from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.v1.routes import router as api_router
from backend.app.config import get_settings
from backend.app.middleware.rate_limit import RateLimitMiddleware
from backend.app.logging_setup import configure_logging


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging()
    app = FastAPI(title=settings.app_name, version=settings.app_version)

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(o) for o in settings.cors_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Rate limit
    app.add_middleware(
        RateLimitMiddleware,
        requests_per_minute=settings.rate_limit_rpm,
        burst=settings.rate_limit_burst,
    )

    # Routes
    app.include_router(api_router, prefix="/api/v1")
    return app


app = create_app()


