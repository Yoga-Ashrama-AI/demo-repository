# tests/conftest.py
import os, sys
# add repo root to sys.path so `import api` always works in CI and locally
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
