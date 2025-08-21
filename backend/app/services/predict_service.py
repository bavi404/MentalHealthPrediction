from __future__ import annotations

import time
from typing import List

import numpy as np

from backend.app.config import get_settings
from backend.app.core.label_codec import LabelCodec
from backend.app.core.model import ANNModel
from backend.app.core.text_cleaning import clean_texts
from backend.app.core.vectorizer import VectorizerStore


class PredictionService:
    def __init__(self) -> None:
        settings = get_settings()
        self.settings = settings
        self.codec = LabelCodec(settings.classes_path)
        self.vectorizer = VectorizerStore(settings.vectorizer_path)
        self.model = ANNModel(settings.model_path)

    def is_ready(self) -> bool:
        if self.settings.mock_predict:
            return True
        return self.vectorizer.is_available and self.model.is_available

    def predict(self, inputs: List[str]) -> tuple[list[str], list[float], list[list[float]], float]:
        start = time.perf_counter()

        # Sanitize and limit
        clipped = [t[: self.settings.max_text_length] for t in inputs[: self.settings.max_batch_size]]
        texts = clean_texts(clipped)
        if self.settings.mock_predict:
            # Deterministic mock: score class 0 as highest for all
            num_classes = self.codec.num_classes()
            probabilities = np.zeros((len(texts), num_classes), dtype=float)
            probabilities[:, 0] = 1.0
        else:
            X = self.vectorizer.transform(texts)
            probabilities = self.model.predict_proba(X)
        indices = probabilities.argmax(axis=1)
        labels = self.codec.decode(indices)
        scores = probabilities.max(axis=1).tolist()

        latency_ms = (time.perf_counter() - start) * 1000.0
        return labels, scores, probabilities.tolist(), latency_ms


