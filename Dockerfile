FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml /app/
RUN pip install --no-cache-dir fastapi uvicorn pydantic pytest httpx
COPY api /app/api
CMD ["uvicorn","api.main:app","--host","0.0.0.0","--port","8000"]
