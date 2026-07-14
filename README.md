# Allure Report Demo Monorepo

This repository is a small demo workspace with three independent test projects.

There is no Allure setup yet. Each project runs with its original test runner:

- `unit` uses Python and `pytest`
- `API` uses Python and `pytest`
- `E2E` uses Playwright

## Project folders

```text
unit/  Python unit tests for a small package
API/   Python API tests grouped by microservice
E2E/   Playwright browser tests organized by user journey
```

## Quick start

Each folder has copy-paste setup commands in its README. Python dependencies are
listed in `requirements.txt` files inside `unit/` and `API/`; install them into
local virtual environments instead of your system Python.

Each folder is intentionally independent so it can later run as a separate CI job or matrix job.
