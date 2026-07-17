import * as allure from 'allure-js-commons';

import { CatalogPage } from '../../pages/CatalogPage';
import { expect, test } from '../../fixtures/test';
import { maybeFlake } from '../flaky';
import { annotateScenario, attachScreenshot } from '../metadata';

test('buyer discovers the backpack product @smoke', async ({ page }) => {
  await annotateScenario({
    feature: 'Catalog',
    story: 'Product discovery',
    severity: 'critical',
    smoke: true,
  });
  await allure.issue('27', 'epic');

  const catalogPage = new CatalogPage(page);

  await allure.step('Open product discovery surface', async () => {
    await catalogPage.open();
    await attachScreenshot('catalog-opened', await page.screenshot());
  });

  await allure.step('Inspect product merchandising data', async () => {
    await allure.step('Verify product title', async () => {
      await expect(page.getByRole('heading', { name: 'Demo Backpack' })).toBeVisible();
    });
    await allure.step('Verify product action', async () => {
      await expect(page.getByRole('button', { name: 'Add to cart' })).toBeEnabled();
    });
  });
});

test('catalog search highlights the best matching product', async ({ page }) => {
  await annotateScenario({
    feature: 'Catalog',
    story: 'Product search relevance',
    severity: 'critical',
  });
  await allure.issue('27', 'epic');

  const catalogPage = new CatalogPage(page);

  await allure.step('Load catalog search results', async () => {
    await catalogPage.open();
    await attachScreenshot('catalog-search-results', await page.screenshot());
  });

  await allure.step('Verify backpack is ranked as the best match', async () => {
    await expect(page.getByRole('heading', { name: 'Demo Backpack' })).toBeVisible();
    expect
      .soft('Demo Bottle', 'Demo stable failure: catalog search ranking returned stale product data.')
      .toBe('Demo Backpack');
  });
});

test('catalog action survives a slow inventory refresh', async ({ page }) => {
  await annotateScenario({
    feature: 'Catalog',
    story: 'Inventory refresh resilience',
    severity: 'normal',
  });
  await allure.issue('27', 'epic');

  const catalogPage = new CatalogPage(page);

  await allure.step('Open catalog during inventory refresh', async () => {
    await catalogPage.open();
    await attachScreenshot('catalog-before-inventory-refresh', await page.screenshot());
  });

  await allure.step('Wait for inventory refresh to settle', async () => {
    await page.waitForTimeout(75);
    maybeFlake(0.25, 'catalog action after slow inventory refresh');
  });

  await allure.step('Verify product action remains available', async () => {
    await expect(page.getByRole('button', { name: 'Add to cart' })).toBeEnabled();
    await attachScreenshot('catalog-after-inventory-refresh', await page.screenshot());
  });
});
