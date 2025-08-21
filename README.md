# Mental Health Prediction Web App

This repo contains a FastAPI backend and Vite + React + TypeScript frontend for classifying short texts into mental health-related categories.

## Quickstart

### Backend (http://localhost:8000)
1. Python 3.10+
2. `pip install -r backend/requirements.txt`
3. Optional: `cp backend/.env.example backend/.env` and tweak values
4. Run: `python -m backend.app`

Mock mode: Set `MOCK_PREDICT=true` to run without model artifacts.
Place artifacts for real predictions:
- `backend/models/ann_model.keras`
- `backend/models/tfidf_vectorizer.pkl`
- optional `backend/models/classes.npy`

### Frontend (http://localhost:5173)
1. `cd frontend && npm install`
2. `npm run dev`
3. Set `VITE_API_BASE_URL` in `frontend/.env` if backend is remote.

## API
- POST `/api/v1/predict` → `{ predictions: [{label, score}], latency_ms, model_version }`
- GET `/api/v1/health` → `{ status, model_loaded, app_version }`
- GET `/api/v1/meta` → feature schema and example payload

## Tests
- Backend: `PYTHONPATH=. pytest -q backend/tests`
- Frontend: `cd frontend && npm test`

## Deployment
- Backend (Render/Fly.io): build `pip install -r backend/requirements.txt`, start `python -m backend.app`
- Frontend (Vercel/Netlify): build `npm run build`, publish `frontend/dist`, set `VITE_API_BASE_URL`

## CI
- GitHub Actions for backend and frontend under `.github/workflows/`

## Model Card
- See `backend/app/MODEL_CARD.md`
