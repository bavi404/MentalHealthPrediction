import { useEffect, useMemo, useState } from 'react'
import { api } from '../shared/api'

type PredictItem = { label: string; score: number; probabilities?: number[] }

export function TryIt() {
  const [text, setText] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [result, setResult] = useState<PredictItem[] | null>(null)

  const recentKey = 'mh_recent_inputs'
  const recent = useMemo<string[]>(() => {
    try {
      return JSON.parse(localStorage.getItem(recentKey) || '[]')
    } catch { return [] }
  }, [])

  useEffect(() => {
    if (text.trim()) return
    if (recent[0]) setText(recent[0])
  }, [])

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault()
    setError(null)
    setResult(null)
    const value = text.trim()
    if (!value) { setError('Please enter text'); return }
    setLoading(true)
    try {
      const res = await api.predict({ inputs: [value] })
      setResult(res.predictions)
      const merged = [value, ...recent.filter(v => v !== value)].slice(0, 5)
      localStorage.setItem(recentKey, JSON.stringify(merged))
    } catch (err: any) {
      setError(err?.message ?? 'Request failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-semibold">Try It</h2>
      <form onSubmit={onSubmit} className="space-y-3">
        <label className="block text-sm font-medium">Text</label>
        <textarea
          aria-label="input text"
          value={text}
          onChange={e => setText(e.target.value)}
          className="w-full min-h-[120px] p-2 border rounded"
          placeholder="Type your text here"
          disabled={loading}
        />
        <div className="flex items-center gap-2">
          <button disabled={loading} className="bg-blue-600 text-white px-4 py-2 rounded disabled:opacity-50">
            {loading ? 'Predicting…' : 'Predict'}
          </button>
          {recent.length > 0 && (
            <select
              aria-label="recent inputs"
              className="border rounded p-2 text-sm"
              onChange={(e) => setText(e.target.value)}
            >
              <option>Recent inputs…</option>
              {recent.map((r, idx) => (
                <option key={idx} value={r}>{r.slice(0, 60)}</option>
              ))}
            </select>
          )}
        </div>
      </form>
      {error && <div role="alert" className="text-red-700">{error}</div>}
      {result && (
        <div aria-live="polite" className="space-y-2">
          <div className="font-medium">Result</div>
          <div className="border rounded p-3 bg-white">
            <div className="flex items-center justify-between">
              <div className="text-lg">{result[0].label}</div>
              <div className="text-sm text-gray-600">score: {result[0].score.toFixed(3)}</div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}


