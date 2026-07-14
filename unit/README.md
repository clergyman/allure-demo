# Unit Tests

This folder contains small Python unit tests.

The code lives in `src/demo_shop`. The tests live in `tests`.

## What you need

- Python 3.11 or newer

## Copy-paste from repo root

```bash
python3 -m venv unit/.venv
unit/.venv/bin/python3 -m pip install -r unit/requirements.txt
unit/.venv/bin/python3 -m pytest unit
```

## Copy-paste from this folder

If your terminal is already inside `unit`:

```bash
python3 -m venv .venv
.venv/bin/python3 -m pip install -r requirements.txt
.venv/bin/python3 -m pytest
```

On Windows PowerShell from inside `unit`:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pytest
```

Dependencies are listed in `requirements.txt`.

## What the tests cover

- product pricing
- shopping cart totals
- user permissions

## Demo volume

The suite collects 500 tests. The volume tests are deterministic, so unit tests
should not fail randomly.
