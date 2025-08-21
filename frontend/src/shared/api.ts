const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

type PredictRequest = { inputs: string[] }
type PredictResponse = { predictions: { label: string; score: number; probabilities?: number[] }[]; latency_ms: number; model_version: string }

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const r = await fetch(`${BASE_URL}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...init,
  })
  if (!r.ok) {
    const text = await r.text()
    throw new Error(text || r.statusText)
  }
  return r.json() as Promise<T>
}

export const api = {
  predict: (body: PredictRequest) => request<PredictResponse>('/api/v1/predict', { method: 'POST', body: JSON.stringify(body) }),
  health: () => request('/api/v1/health'),
  meta: () => request('/api/v1/meta'),
}


