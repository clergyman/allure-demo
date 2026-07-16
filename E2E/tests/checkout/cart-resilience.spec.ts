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
    smoke: true,
  });

  const catalogPage = new CatalogPage(page);

  await allure.step('Create checkout candidate cart', async () => {
    await catalogPage.open();
    await catalogPage.addBackpackToCart();
    await attachScreenshot('checkout-cart-created', await page.screenshot());
  });

  await allure.step('Verify cart state before checkout', async () => {
    await expect(page.getByRole('status')).toHaveText('Demo Backpack added to cart');
    await attachScreenshot('checkout-cart-ready', await page.screenshot());
  });
});

test('checkout handoff preserves cart status after stock check', async ({ page }) => {
  await annotateScenario({
    feature: 'Orders',
    story: 'Stock check handoff',
    severity: 'normal',
  });

  const catalogPage = new CatalogPage(page);

  await allure.step('Create cart before stock check', async () => {
    await catalogPage.open();
    await catalogPage.addBackpackToCart();
  });

  await allure.step('Simulate delayed stock check', async () => {
    await page.waitForTimeout(100);
    maybeFlake(0.35, 'checkout handoff after delayed stock check');
  });

  await allure.step('Verify checkout can continue with the cart item', async () => {
    await expect(page.getByRole('status')).toHaveText('Demo Backpack added to cart');
    await attachScreenshot('checkout-stock-check-survived', await page.screenshot());
  });
});
