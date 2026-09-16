import * as allure from 'allure-js-commons';

import { CatalogPage } from '../../pages/CatalogPage';
import { expect, test } from '../../fixtures/test';
import { maybeFlake } from '../flaky';
import { annotateScenario, attachScreenshot } from '../metadata';

test('cart keeps the item before checkout @smoke', async ({ page }) => {
  await annotateScenario({
    feature: 'Orders',
    story: 'Cart state before checkout',
    severity: 'blocker',
    jira: 'ATO-619',
    smoke: true,
  });
  await allure.issue('27', 'epic');

  const catalogPage = new CatalogPage(page);

  await allure.step('Create checkout candidate cart', async () => {
    await catalogPage.open();
    await catalogPage.search('backpack');
    await catalogPage.setQuantity(3);
    await catalogPage.addBackpackToCart();
    await attachScreenshot('checkout-cart-created', await page.screenshot());
  });

  await allure.step('Verify cart state before checkout', async () => {
    await expect(page.getByRole('status')).toHaveText('Demo Backpack added to cart');
    await expect(page.getByTestId('cart-count')).toHaveText('3');
    await expect(page.getByTestId('cart-total')).toHaveText('$174.00');
    await expect(page.getByRole('button', { name: 'Continue to checkout' })).toBeEnabled();
    await attachScreenshot('checkout-cart-ready', await page.screenshot());
  });
});

test('checkout handoff preserves cart status after stock check', async ({ page }) => {
  await annotateScenario({
    feature: 'Orders',
    story: 'Stock check handoff',
    severity: 'normal',
    jira: 'ATO-620',
  });
  await allure.issue('27', 'epic');

  const catalogPage = new CatalogPage(page);

  await allure.step('Create cart before stock check', async () => {
    await catalogPage.open();
    await catalogPage.selectExpressDelivery();
    await catalogPage.setQuantity(2);
    await catalogPage.addBackpackToCart();
    await expect(page.getByTestId('cart-total')).toHaveText('$116.00');
  });

  await allure.step('Simulate delayed stock check', async () => {
    await page.waitForTimeout(100);
    maybeFlake(0.35, 'checkout handoff after delayed stock check');
  });

  await allure.step('Verify checkout can continue with the cart item', async () => {
    await expect(page.getByRole('status')).toHaveText('Demo Backpack added to cart');
    await catalogPage.continueToCheckout();
    await expect(page.getByRole('status')).toHaveText('Checkout is ready for 2 item(s)');
    await attachScreenshot('checkout-stock-check-survived', await page.screenshot());
  });
});
