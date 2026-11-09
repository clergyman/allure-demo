import * as allure from 'allure-js-commons';

import { CatalogPage } from '../../pages/CatalogPage';
import { expect, test } from '../../fixtures/test';
import { annotateScenario } from '../metadata';

test('bottle search reveals the unavailable product', async ({ page, users }) => {
  await annotateScenario({ feature: 'Catalog', story: 'Product availability', severity: 'normal' });
  const surface = new CatalogPage(page);
  await surface.open();
  await allure.step('Search for bottle', async () => {
    await surface.search('bottle');
  });
  await allure.step('Review unavailable product', async () => {
    const product = page.getByRole('article', { name: 'Demo Bottle product' });
    await expect(product).toBeVisible();
    await expect(product).toContainText('Out of stock');
    await expect(product.getByRole('button', { name: 'Add to cart' })).toHaveCount(0);
  });
});

test('catalog search ignores surrounding whitespace', async ({ page, users }) => {
  await annotateScenario({ feature: 'Catalog', story: 'Search normalization', severity: 'normal' });
  const surface = new CatalogPage(page);
  await surface.open();
  await allure.step('Search with padded query', async () => {
    await surface.search('  bottle  ');
    await expect(page.getByRole('article', { name: 'Demo Bottle product' })).toBeVisible();
    await expect(page.getByRole('status')).toHaveText('Filtered catalog for bottle');
  });
});

test('catalog search ignores letter case', async ({ page, users }) => {
  await annotateScenario({ feature: 'Catalog', story: 'Search normalization', severity: 'normal' });
  const surface = new CatalogPage(page);
  await surface.open();
  await allure.step('Search with uppercase query', async () => {
    await surface.search('BOTTLE');
    await expect(page.getByRole('article', { name: 'Demo Bottle product' })).toBeVisible();
    await expect(page.getByRole('status')).toHaveText('Filtered catalog for bottle');
  });
});

test('clearing search hides the bottle result', async ({ page, users }) => {
  await annotateScenario({ feature: 'Catalog', story: 'Clear catalog filters', severity: 'normal' });
  const surface = new CatalogPage(page);
  await surface.open();
  await allure.step('Reveal bottle', async () => {
    await surface.search('bottle');
    await expect(page.getByRole('article', { name: 'Demo Bottle product' })).toBeVisible();
  });
  await allure.step('Clear search', async () => {
    await surface.search('');
    await expect(page.getByRole('article', { name: 'Demo Bottle product' })).toBeHidden();
    await expect(page.getByRole('status')).toHaveText('Catalog filters cleared');
  });
});

test('buyer can return to standard delivery', async ({ page, users }) => {
  await annotateScenario({ feature: 'Catalog', story: 'Delivery preferences', severity: 'normal' });
  const surface = new CatalogPage(page);
  await surface.open();
  await allure.step('Switch delivery options', async () => {
    await surface.selectExpressDelivery();
    await expect(page.getByLabel('Delivery speed')).toHaveValue('Express delivery');
    await page.getByLabel('Delivery speed').selectOption('Standard delivery');
    await expect(page.getByLabel('Delivery speed')).toHaveValue('Standard delivery');
  });
});

test('backpack product displays its price and stock', async ({ page, users }) => {
  await annotateScenario({ feature: 'Catalog', story: 'Product detail summary', severity: 'normal' });
  const surface = new CatalogPage(page);
  await surface.open();
  await allure.step('Review backpack card', async () => {
    const product = page.getByRole('article', { name: 'Demo Backpack product' });
    await expect(product).toContainText('$58.00');
    await expect(product).toContainText('In stock');
    await expect(product.getByRole('button', { name: 'Add to cart' })).toBeEnabled();
  });
});
