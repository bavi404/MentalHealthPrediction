from functools import lru_cache
from pathlib import Path
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables and .env.

    This governs model paths, API behavior, and security defaults.
    """

    # App
    app_name: str = Field(default="Mental Health Prediction API")
    app_version: str = Field(default="0.1.0")

    # Server
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8000)

    # CORS
    cors_origins: List[str] = Field(default_factory=lambda: ["http://localhost:5173"])

    # Model artifacts
    model_dir: Path = Field(default=Path("backend/models"))
    model_path: Path = Field(default=Path("backend/models/ann_model.keras"))
    vectorizer_path: Path = Field(default=Path("backend/models/tfidf_vectorizer.pkl"))
    classes_path: Path = Field(default=Path("backend/models/classes.npy"))

    # Behavior
    mock_predict: bool = Field(default=False)
    max_text_length: int = Field(default=1000)
    max_batch_size: int = Field(default=32)

    # Rate limiting (very simple in-memory token bucket)
    rate_limit_rpm: int = Field(default=60, description="Requests per minute per IP")
    rate_limit_burst: int = Field(default=30, description="Allowed burst tokens")

    model_config = SettingsConfigDict(
        env_file=Path("backend/.env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()


