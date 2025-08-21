from __future__ import annotations

from fastapi import APIRouter, HTTPException

from backend.app.config import get_settings
from backend.app.schemas.predict import (
    HealthResponse,
    MetaResponse,
    PredictRequest,
    PredictResponse,
    PredictionItem,
)
from backend.app.services.predict_service import PredictionService


router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    settings = get_settings()
    service = PredictionService()
    return HealthResponse(
        status="ok",
        model_loaded=service.is_ready(),
        app_version=settings.app_version,
    )


@router.get("/meta", response_model=MetaResponse)
def meta() -> MetaResponse:
    settings = get_settings()
    feature_schema = {
        "type": "object",
        "properties": {
            "inputs": {
                "type": "array",
                "items": {"type": "string"},
                "minItems": 1,
                "maxItems": settings.max_batch_size,
            }
        },
        "required": ["inputs"],
    }
    example_payload = {"inputs": ["I feel anxious before my exam"]}
    return MetaResponse(feature_schema=feature_schema, example_payload=example_payload)


@router.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest) -> PredictResponse:
    service = PredictionService()
    if not service.is_ready():
        raise HTTPException(status_code=503, detail="Model artifacts are not available")

    labels, scores, probabilities, latency_ms = service.predict(payload.inputs)
    items = [
        PredictionItem(label=label, score=score, probabilities=probs)
        for label, score, probs in zip(labels, scores, probabilities)
    ]
    return PredictResponse(
        predictions=items,
        model_version=get_settings().app_version,
        latency_ms=latency_ms,
    )


