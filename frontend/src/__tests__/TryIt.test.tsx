import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import { TryIt } from '../pages/TryIt'

vi.mock('../shared/api', () => ({
  api: { predict: vi.fn().mockResolvedValue({ predictions: [{ label: 'Stress', score: 1 }], latency_ms: 1, model_version: '0.1.0' }) }
}))

describe('TryIt', () => {
  beforeEach(() => {
    localStorage.clear()
  })

  it('shows validation error on empty submit', async () => {
    render(<TryIt />)
    const btn = screen.getByText('Predict')
    fireEvent.click(btn)
    expect(await screen.findByRole('alert')).toHaveTextContent('Please enter text')
  })
})

