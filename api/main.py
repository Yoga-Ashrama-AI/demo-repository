# api/main.py
from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional, Dict, Any
import uuid

app = FastAPI(title="Demo API", version="0.1.0")

class EchoIn(BaseModel):
    message: str

class Envelope(BaseModel):
    status: str
    idempotency_key: Optional[str] = None
    correlation_id: str
    data: Optional[Dict[str, Any]] = None

@app.get("/healthz", response_model=Envelope)
def healthz(
    x_correlation_id: Optional[str] = Header(default=None, alias="X-Correlation-Id"),
):
    corr = x_correlation_id or str(uuid.uuid4())
    return Envelope(
        status="ok",
        idempotency_key=None,
        correlation_id=corr,
        data={"service": "healthy"},
    )

@app.post("/echo", response_model=Envelope)
def echo(
    body: EchoIn,
    x_idempotency_key: Optional[str] = Header(default=None, alias="X-Idempotency-Key"),
    x_correlation_id: Optional[str] = Header(default=None, alias="X-Correlation-Id"),
):
    corr = x_correlation_id or str(uuid.uuid4())
    return Envelope(
        status="ok",
        idempotency_key=x_idempotency_key,
        correlation_id=corr,
        data=body.model_dump(),
    )
