# E2E Tests

## 1. Playwright

```bash
npm install
npx playwright install
npx playwright test
```

## 2. Allure Report 3

```bash
npm install
npx playwright install
npx allure run --config ./allurerc.mjs -- npx playwright test
```

## 3. Allure 3 TestOps Upload

```bash
npm install
npx playwright install
export CI=true
export TESTOPS_URL=https://your-testops-host
export TESTOPS_TOKEN=your-token
export TESTOPS_PROJECT_ID=1

npx allure run --config ./allurerc.testops.mjs -- npx playwright test
```

## 4. allurectl TestOps Upload

```bash
npm install
npx playwright install
wget https://github.com/allure-framework/allurectl/releases/latest/download/allurectl_darwin_arm64 -O ./allurectl
chmod +x ./allurectl
export CI=true
export ALLURE_ENDPOINT=https://your-testops-host
export ALLURE_TOKEN=your-token
export ALLURE_PROJECT_ID=1
export ALLURE_RESULTS=allure-results
export ALLURE_LAUNCH_NAME="E2E Tests local Playwright"

./allurectl watch -- npx playwright test
```

## Open Local Results

```bash
npx playwright show-report
npx playwright show-trace test-results/path-to-test/trace.zip
npx allure open allure-report
```
