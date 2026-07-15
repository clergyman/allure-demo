# API Tests

This folder contains Python API tests grouped by microservice.

There is no real server in this demo yet. The tests use tiny fake clients so the structure is easy to understand before we connect real APIs.

## What you need

- Python 3.11 or newer

## Setup

From the repository root:

```bash
python3 -m venv API/.venv
API/.venv/bin/python3 -m pip install -r API/requirements.txt
```

From this folder:

```bash
python3 -m venv .venv
.venv/bin/python3 -m pip install -r requirements.txt
```

On Windows PowerShell from inside `API`:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:DEMO_DISABLE_FLAKES = "1"
.venv\Scripts\python.exe -m pytest
```

## Run With Pytest

From this folder:

```bash
DEMO_DISABLE_FLAKES=1 .venv/bin/python3 -m pytest
```

From the repository root:

```bash
DEMO_DISABLE_FLAKES=1 API/.venv/bin/python3 -m pytest API
```

## Run With Allure

From this folder:

```bash
DEMO_DISABLE_FLAKES=1 npx allure run --config ./allurerc.mjs -- .venv/bin/python3 -m pytest --alluredir allure-results
```

From the repository root:

```bash
DEMO_DISABLE_FLAKES=1 npx allure run --config API/allurerc.mjs -- API/.venv/bin/python3 -m pytest API --alluredir API/allure-results
```

## Run With Allure TestOps

From this folder:

```bash
export CI=true
export TESTOPS_URL=https://your-testops-host
export TESTOPS_TOKEN=your-token
export TESTOPS_PROJECT_ID=1
export DEMO_DISABLE_FLAKES=1

npx allure run --config ./allurerc.testops.mjs -- .venv/bin/python3 -m pytest --alluredir allure-results
```

## API request logging

API tests write simulated request logs to `api-test.log`:

```bash
DEMO_DISABLE_FLAKES=1 .venv/bin/python3 -m pytest
```

To also stream API logs in the terminal:

```bash
DEMO_DISABLE_FLAKES=1 .venv/bin/python3 -m pytest -o log_cli=true --log-cli-level=INFO
```

## Run tests for one microservice

```bash
DEMO_DISABLE_FLAKES=1 .venv/bin/python3 -m pytest tests/microservices/identity
DEMO_DISABLE_FLAKES=1 .venv/bin/python3 -m pytest tests/microservices/catalog
DEMO_DISABLE_FLAKES=1 .venv/bin/python3 -m pytest tests/microservices/orders
```

## Demo volume and flakes

The suite collects 200 tests. The volume tests include rare demo flakes with a
0.1% per-test probability to make reports show occasional unstable API behavior.

For deterministic runs, the commands above set `DEMO_DISABLE_FLAKES=1`.

To force visible flaky failures for a demo, set a higher probability:

```bash
DEMO_FLAKE_PROBABILITY=0.25 .venv/bin/python3 -m pytest tests/microservices/orders/test_create_order_volume.py
```

From the repository root:

```bash
DEMO_FLAKE_PROBABILITY=0.25 API/.venv/bin/python3 -m pytest API/tests/microservices/orders/test_create_order_volume.py
```

Dependencies are listed in `requirements.txt`.

## Why the tests are grouped this way

Each microservice has its own folder. This makes it easy to run only one service in CI later.
