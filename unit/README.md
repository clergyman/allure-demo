# Unit Tests

## 1. Pytest

```bash
python3 -m venv .venv
.venv/bin/python3 -m pip install -r requirements.txt
.venv/bin/python3 -m pytest
```

## 2. Allure Report 3

```bash
python3 -m venv .venv
.venv/bin/python3 -m pip install -r requirements.txt
npx allure run --config ./allurerc.mjs -- .venv/bin/python3 -m pytest --alluredir allure-results
```

## 3. Allure 3 TestOps Upload

```bash
python3 -m venv .venv
.venv/bin/python3 -m pip install -r requirements.txt
export CI=true
export TESTOPS_URL=https://your-testops-host
export TESTOPS_TOKEN=your-token
export TESTOPS_PROJECT_ID=1

npx allure run --config ./allurerc.testops.mjs -- .venv/bin/python3 -m pytest --alluredir allure-results
```

## 4. allurectl TestOps Upload

```bash
python3 -m venv .venv
.venv/bin/python3 -m pip install -r requirements.txt
wget https://github.com/allure-framework/allurectl/releases/latest/download/allurectl_darwin_arm64 -O ./allurectl
chmod +x ./allurectl
export CI=true
export ALLURE_ENDPOINT=https://your-testops-host
export ALLURE_TOKEN=your-token
export ALLURE_PROJECT_ID=1
export ALLURE_RESULTS=allure-results
export ALLURE_LAUNCH_NAME="Unit Tests local pytest"

./allurectl watch -- .venv/bin/python3 -m pytest --alluredir allure-results
```
