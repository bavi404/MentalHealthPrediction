import { Link, Outlet } from 'react-router-dom'

export function App() {
  return (
    <div className="min-h-screen bg-gray-50 text-gray-900">
      <header className="border-b bg-white">
        <div className="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
          <Link to="/" className="font-semibold">Mental Health Prediction</Link>
          <nav className="flex gap-4 text-sm">
            <Link to="/">Home</Link>
            <Link to="/try">Try It</Link>
            <Link to="/docs">Docs</Link>
            <Link to="/about">About</Link>
          </nav>
        </div>
      </header>
      <main className="max-w-5xl mx-auto px-4 py-8">
        <Outlet />
      </main>
      <footer className="border-t bg-white">
        <div className="max-w-5xl mx-auto px-4 py-3 text-sm text-gray-600">© {new Date().getFullYear()}</div>
      </footer>
    </div>
  )
}


