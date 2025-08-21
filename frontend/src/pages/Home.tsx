import { Link } from 'react-router-dom'

export function Home() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">Mental Health Prediction</h1>
      <p className="text-gray-700">Classify short texts into mental-health related categories. This is not a diagnostic tool.</p>
      <Link to="/try" className="inline-block bg-blue-600 text-white px-4 py-2 rounded">Try it</Link>
    </div>
  )
}


