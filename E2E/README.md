# E2E Tests

This folder contains Playwright end-to-end tests.

The demo tests render small pages inside the browser, so you do not need a real website yet.

## What you need

- Node.js 20 or newer
- npm

## Install

From this folder:

```bash
npm install
npx playwright install
```

## Run all tests

```bash
npx playwright test
```

## Run tests in one browser

```bash
npx playwright test --project=chromium
```

## See the HTML test report

```bash
npx playwright show-report
```

## Demo volume and flakes

The suite collects 51 browser executions across Chromium, Firefox, and WebKit.
Some product scenarios are intentionally flaky, with probabilities shown in the
test names such as `@flake-25` or `@flake-50`.

For a deterministic verification run, disable the demo flakes:

```bash
DEMO_DISABLE_FLAKES=1 npx playwright test
```

## Folder layout

```text
tests/     user journeys grouped by product area
pages/     page objects used by tests
fixtures/  shared Playwright setup and test data
helpers/   small reusable helper functions
```
