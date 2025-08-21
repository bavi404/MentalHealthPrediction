from __future__ import annotations

from pathlib import Path
from typing import Optional

import numpy as np

try:
    from tensorflow.keras.models import load_model as tf_load_model
except Exception:  # pragma: no cover - optional runtime dependency
    tf_load_model = None  # type: ignore[assignment]


class ANNModel:
    def __init__(self, model_path: Path) -> None:
        self.model_path = model_path
        self._model = None

    @property
    def is_available(self) -> bool:
        return self.model_path.exists()

    def load(self):
        if self._model is None:
            if tf_load_model is None:
                raise RuntimeError(
                    "TensorFlow is not available. Install tensorflow to load the model."
                )
            self._model = tf_load_model(self.model_path)
        return self._model

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        model = self.load()
        # Returns softmax probabilities
        return model.predict(X)


