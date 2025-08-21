from __future__ import annotations

import pickle
from pathlib import Path
from typing import Optional

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


class VectorizerStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._vectorizer: Optional[TfidfVectorizer] = None

    @property
    def is_available(self) -> bool:
        return self.path.exists()

    def load(self) -> TfidfVectorizer:
        if self._vectorizer is None:
            with self.path.open("rb") as f:
                self._vectorizer = pickle.load(f)
        return self._vectorizer

    def transform(self, texts: list[str]) -> np.ndarray:
        vec = self.load()
        X = vec.transform(texts)
        # Model expects dense arrays
        return X.toarray()


