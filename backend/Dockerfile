FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy backend code under /app/backend so Python module path is 'backend.*'
COPY . /app/backend

RUN pip install --no-cache-dir -r /app/backend/requirements.txt

EXPOSE 8000

CMD ["python", "-m", "backend.app"]

