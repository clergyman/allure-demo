import * as allure from 'allure-js-commons';

import { CatalogPage } from '../../pages/CatalogPage';
import { expect, test } from '../../fixtures/test';
import { annotateScenario, attachScreenshot } from '../metadata';

test('buyer adds backpack to the cart @smoke', async ({ page }) => {
  await annotateScenario({
    feature: 'Orders',
    story: 'Add product to cart',
    severity: 'blocker',
    jira: 'ATO-617',
    smoke: true,
  });
  await allure.issue('27', 'epic');

  const catalogPage = new CatalogPage(page);

  await allure.step('Prepare catalog for cart action', async () => {
    await allure.step('Render catalog page', async () => {
      await catalogPage.open();
    });
    await allure.step('Choose delivery and quantity before cart action', async () => {
      await catalogPage.selectExpressDelivery();
      await catalogPage.setQuantity(2);
      await expect(page.getByLabel('Delivery speed')).toHaveValue('Express delivery');
      await expect(page.getByLabel('Quantity')).toHaveValue('2');
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
    await expect(page.getByTestId('cart-count')).toHaveText('2');
    await expect(page.getByTestId('cart-total')).toHaveText('$116.00');
    await attachScreenshot('cart-add-confirmed', await page.screenshot());
  });
});

test('cart preview total matches checkout handoff', async ({ page }) => {
  await annotateScenario({
    feature: 'Orders',
    story: 'Checkout preview handoff',
    severity: 'critical',
    jira: 'ATO-618',
  });
  await allure.issue('27', 'epic');

  const catalogPage = new CatalogPage(page);

  await allure.step('Build cart preview state', async () => {
    await catalogPage.open();
    await catalogPage.setQuantity(1);
    await catalogPage.addBackpackToCart();
    await expect(page.getByTestId('cart-count')).toHaveText('1');
    await attachScreenshot('checkout-preview-source-cart', await page.screenshot());
  });

  await allure.step('Verify checkout preview total', async () => {
    await expect(page.getByRole('status')).toHaveText('Demo Backpack added to cart');
    await expect(page.getByTestId('cart-total')).toHaveText('$58.00');
    await catalogPage.continueToCheckout();
    await expect(page.getByRole('status')).toHaveText('Checkout is ready for 1 item(s)');
    await attachScreenshot('checkout-preview-before-total-failure', await page.screenshot());
    expect
      .soft('57.00', 'Demo stable failure: checkout preview total drifted from order creation.')
      .toBe('58.00');
  });
});
