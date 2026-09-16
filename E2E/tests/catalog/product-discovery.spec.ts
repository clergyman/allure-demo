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
    jira: 'ATO-614',
    smoke: true,
  });
  await allure.issue('27', 'epic');

  const catalogPage = new CatalogPage(page);

  await allure.step('Open product discovery surface', async () => {
    await catalogPage.open();
    await expect(page.getByLabel('Search catalog')).toBeVisible();
    await expect(page.getByLabel('Delivery speed')).toHaveValue('Standard delivery');
    await attachScreenshot('catalog-opened', await page.screenshot());
  });

  await allure.step('Narrow discovery to the backpack line', async () => {
    await catalogPage.search('backpack');
    await expect(page.getByRole('status')).toHaveText('Filtered catalog for backpack');
    await attachScreenshot('catalog-filtered-backpack', await page.screenshot());
  });

  await allure.step('Inspect product merchandising data', async () => {
    await allure.step('Verify product title', async () => {
      await expect(page.getByRole('heading', { name: 'Demo Backpack' })).toBeVisible();
    });
    await allure.step('Verify product availability and price are visible', async () => {
      await expect(page.getByText('$58.00')).toBeVisible();
      await expect(page.getByText('In stock')).toBeVisible();
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
    jira: 'ATO-615',
  });
  await allure.issue('27', 'epic');

  const catalogPage = new CatalogPage(page);

  await allure.step('Load catalog search results', async () => {
    await catalogPage.open();
    await catalogPage.search('bottle');
    await expect(page.getByRole('heading', { name: 'Demo Bottle' })).toBeVisible();
    await attachScreenshot('catalog-search-results', await page.screenshot());
  });

  await allure.step('Verify backpack is ranked as the best match', async () => {
    await catalogPage.search('backpack');
    await expect(page.getByRole('heading', { name: 'Demo Backpack' })).toBeVisible();
    await attachScreenshot('catalog-search-ranking-before-failure', await page.screenshot());
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
    jira: 'ATO-616',
  });
  await allure.issue('27', 'epic');

  const catalogPage = new CatalogPage(page);

  await allure.step('Open catalog during inventory refresh', async () => {
    await catalogPage.open();
    await catalogPage.selectExpressDelivery();
    await catalogPage.setQuantity(2);
    await attachScreenshot('catalog-before-inventory-refresh', await page.screenshot());
  });

  await allure.step('Wait for inventory refresh to settle', async () => {
    await page.waitForTimeout(75);
    maybeFlake(0.25, 'catalog action after slow inventory refresh');
  });

  await allure.step('Verify product action remains available', async () => {
    await expect(page.getByRole('button', { name: 'Add to cart' })).toBeEnabled();
    await expect(page.getByLabel('Quantity')).toHaveValue('2');
    await attachScreenshot('catalog-after-inventory-refresh', await page.screenshot());
  });
});
