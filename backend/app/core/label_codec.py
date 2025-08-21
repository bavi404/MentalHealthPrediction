from __future__ import annotations

from pathlib import Path
from typing import Optional

import numpy as np


DEFAULT_CLASSES = np.array(
    [
        "Stress",
        "Depression",
        "Bipolar disorder",
        "Personality disorder",
        "Anxiety",
    ]
)


class LabelCodec:
    def __init__(self, classes_path: Path) -> None:
        self.classes_path = classes_path
        self._classes: Optional[np.ndarray] = None

    @property
    def is_available(self) -> bool:
        return self.classes_path.exists()

    def load(self) -> np.ndarray:
        if self._classes is None:
            if self.classes_path.exists():
                self._classes = np.load(self.classes_path, allow_pickle=False)
            else:
                self._classes = DEFAULT_CLASSES
        return self._classes

    def decode(self, indices: np.ndarray) -> list[str]:
        classes = self.load()
        return [str(classes[i]) for i in indices]

    def num_classes(self) -> int:
        return int(self.load().shape[0])


