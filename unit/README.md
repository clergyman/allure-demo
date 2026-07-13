# Unit Tests

This folder contains small Python unit tests.

The code lives in `src/demo_shop`. The tests live in `tests`.

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

## Run the tests

```bash
python3 -m pytest
```

## What the tests cover

- product pricing
- shopping cart totals
- user permissions

## Demo volume

The suite collects 500 tests. The volume tests are deterministic, so unit tests
should not fail randomly.
