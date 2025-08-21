from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, constr, field_validator


class PredictRequest(BaseModel):
    inputs: List[constr(strip_whitespace=True, min_length=1)] = Field(
        ..., description="List of input texts to classify"
    )

    @field_validator("inputs")
    @classmethod
    def _non_empty(cls, v: list[str]):
        if not v:
            raise ValueError("inputs must contain at least one item")
        return v


class PredictionItem(BaseModel):
    label: str
    score: float
    probabilities: Optional[List[float]] = None


class PredictResponse(BaseModel):
    predictions: List[PredictionItem]
    model_version: str
    latency_ms: float


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    app_version: str


class MetaResponse(BaseModel):
    feature_schema: dict
    example_payload: dict


