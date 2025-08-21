export function Docs() {
  return (
    <div className="space-y-4">
      <h2 className="text-xl font-semibold">Documentation</h2>
      <ul className="list-disc pl-5 space-y-2 text-gray-700">
        <li>API docs: <a className="text-blue-700 underline" href="http://localhost:8000/docs" target="_blank" rel="noreferrer">FastAPI Swagger UI</a></li>
        <li>OpenAPI JSON: <a className="text-blue-700 underline" href="http://localhost:8000/openapi.json" target="_blank" rel="noreferrer">/openapi.json</a></li>
      </ul>
      <h3 className="text-lg font-medium">Model Card</h3>
      <p className="text-gray-700">See backend/app/MODEL_CARD.md</p>
    </div>
  )
}


