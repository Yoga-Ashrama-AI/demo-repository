# Demo Repository — CI/CD + LLMOps Patterns (Public, Redacted)

This repo showcases my contract-ready skills without exposing private IP:
- **CI/CD**: reusable GitHub Actions, semantic releases, SBOM + image signing.
- **API**: FastAPI service with idempotent request pattern + health endpoints.
- **LLMOps/RAG**: JSONL ingestion schema + minimal retriever stub.
- **Governance**: pre-commit, commitlint, SECURITY.md, LICENSE.

> Private YAAI repo contains proprietary modules, data, and agent configs; this public repo mirrors the **patterns** only.

## Quickstart
```bash
make dev          # run FastAPI with reload
make test         # run pytest
make build        # docker build + sbom + attest
