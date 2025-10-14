from fastapi import FastAPI, Header
from pydantic import BaseModel
import uuid

app = FastAPI(title="Demo API", version="0.1.0")

class EchoIn(BaseModel):
message: str

class Envelope(BaseModel):
status: str
idempotency_key: str | None = None
correlation_id: str
data: dict | None = None

@app.get("/healthz", response_model=Envelope)
def healthz(correlation_id: str = Header(default_factory=lambda: str(uuid.uuid4()))):
return Envelope(status="ok", idempotency_key=None, correlation_id=correlation_id, data={"service":"healthy"})

@app.post("/echo", response_model=Envelope)
def echo(
body: EchoIn,
x_idempotency_key: str | None = Header(default=None),
x_correlation_id: str | None = Header(default=None),
):
corr = x_correlation_id or str(uuid.uuid4())
return Envelope(status="ok", idempotency_key=x_idempotency_key, correlation_id=corr, data=body.dict())
