import re
from functools import lru_cache
from typing import Iterable

try:
    import nltk
    from nltk.corpus import stopwords
except Exception:  # pragma: no cover - optional runtime dep
    nltk = None  # type: ignore[assignment]
    stopwords = None  # type: ignore[assignment]


@lru_cache()
def _get_stop_words() -> set[str]:
    words: set[str] = set()
    if stopwords is None or nltk is None:
        return words
    try:
        # Ensure stopwords available
        nltk.download("stopwords", quiet=True)
        words = set(stopwords.words("english"))
    except Exception:
        words = set()
    return words


def clean_text(text: str) -> str:
    """Clean input text similarly to the notebook:
    - Remove URLs
    - Keep only letters
    - Lowercase
    - Remove stopwords (if available)
    """
    if not isinstance(text, str):
        return ""

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower()

    words = _get_stop_words()
    if words:
        text = " ".join([w for w in text.split() if w not in words])
    else:
        text = " ".join(text.split())
    return text


def clean_texts(texts: Iterable[str]) -> list[str]:
    return [clean_text(t) for t in texts]


