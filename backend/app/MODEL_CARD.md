# Model Card: Mental Health Text Classifier

- Model: TF-IDF (5000 features) + Dense ANN (128 -> 64 -> softmax)
- Task: Multi-class classification of short English texts into mental health-related categories.
- Classes: Stress, Depression, Bipolar disorder, Personality disorder, Anxiety
- Training data: CSV with columns `text` and `target`. Data provenance should be documented by the operator.
- Metrics (example): ~0.69 accuracy on held-out split; per-class precision/recall vary.

Assumptions and Limitations
- Designed for short, English texts. Performance on other languages or long documents is unknown.
- Not a diagnostic tool. Do not use for clinical decision-making.
- Class mapping must match the training.

Intended Use
- Educational/demonstration web app with clear disclaimers.

Safety & Privacy
- Avoid logging raw user inputs; strip PII where possible.
- Use rate limiting and CORS restrictions.

Versioning
- API version: v1
- App version: 0.1.0

Artifacts
- backend/models/ann_model.keras
- backend/models/tfidf_vectorizer.pkl
- backend/models/classes.npy (optional; defaults embedded)

Contact
- Maintainer: Your Name <email@example.com>
