import * as allure from 'allure-js-commons';

import { CatalogPage } from '../../pages/CatalogPage';
import { expect, test } from '../../fixtures/test';
import { annotateScenario, attachScreenshot } from '../metadata';

test('buyer adds backpack to the cart @smoke', async ({ page }) => {
  await annotateScenario({
    feature: 'Cart',
    story: 'Add product to cart',
    severity: 'blocker',
    smoke: true,
  });

  const catalogPage = new CatalogPage(page);

  await allure.step('Prepare catalog for cart action', async () => {
    await allure.step('Render catalog page', async () => {
      await catalogPage.open();
    });
    await allure.step('Confirm backpack card is actionable', async () => {
      await expect(page.getByRole('heading', { name: 'Demo Backpack' })).toBeVisible();
      await expect(page.getByRole('button', { name: 'Add to cart' })).toBeEnabled();
    });
    await attachScreenshot('cart-product-ready', await page.screenshot());
  });

  await allure.step('Add selected product to cart', async () => {
    await catalogPage.addBackpackToCart();
    await attachScreenshot('cart-add-submitted', await page.screenshot());
  });

  await allure.step('Verify customer-facing cart confirmation', async () => {
    await expect(page.getByRole('status')).toHaveText('Demo Backpack added to cart');
    await attachScreenshot('cart-add-confirmed', await page.screenshot());
  });
});

test('cart preview total matches checkout handoff', async ({ page }) => {
  await annotateScenario({
    feature: 'Cart',
    story: 'Checkout preview handoff',
    severity: 'critical',
  });

  const catalogPage = new CatalogPage(page);

  await allure.step('Build cart preview state', async () => {
    await catalogPage.open();
    await catalogPage.addBackpackToCart();
    await attachScreenshot('checkout-preview-source-cart', await page.screenshot());
  });

  await allure.step('Verify checkout preview total', async () => {
    await expect(page.getByRole('status')).toHaveText('Demo Backpack added to cart');
    expect
      .soft('57.00', 'Demo stable failure: checkout preview total drifted from order creation.')
      .toBe('58.00');
  });
});
