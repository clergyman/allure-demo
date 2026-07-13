# API Tests

This folder contains Python API tests grouped by microservice.

There is no real server in this demo yet. The tests use tiny fake clients so the structure is easy to understand before we connect real APIs.

## What you need

- Python 3.11 or newer
- pytest

## Install

From this folder:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
```

On Windows PowerShell, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Run all API tests

```bash
python3 -m pytest
```

## Run tests for one microservice

```bash
pytest tests/microservices/identity
pytest tests/microservices/catalog
pytest tests/microservices/orders
```

## Demo volume and flakes

The suite collects 200 tests. The volume tests include rare demo flakes with a
0.1% per-test probability to make reports show occasional unstable API behavior.

For a deterministic verification run, disable the demo flakes:

```bash
DEMO_DISABLE_FLAKES=1 python3 -m pytest
```

## Why the tests are grouped this way

Each microservice has its own folder. This makes it easy to run only one service in CI later.
