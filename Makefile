.PHONY: dev test build
dev:
\tuvicorn api.main:app --reload --port 8000
test:
\tpytest
build:
\tdocker build -t demo-repo:$(shell git rev-parse --short HEAD) .
