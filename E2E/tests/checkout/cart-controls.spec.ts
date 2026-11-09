import * as allure from 'allure-js-commons';

import { CatalogPage } from '../../pages/CatalogPage';
import { expect, test } from '../../fixtures/test';
import { annotateScenario } from '../metadata';
import { maybeFlake } from '../flaky';

test('empty cart cannot continue to checkout', async ({ page, users }) => {
  await annotateScenario({ feature: 'Orders', story: 'Empty cart protection', severity: 'normal' });
  const surface = new CatalogPage(page);
  await surface.open();
  await allure.step('Verify empty cart', async () => {
    await expect(page.getByTestId('cart-count')).toHaveText('0');
    await expect(page.getByTestId('cart-total')).toHaveText('$0.00');
    await expect(page.getByRole('button', { name: 'Continue to checkout' })).toBeDisabled();
  });
});

test('single backpack enables checkout', async ({ page, users }) => {
  await annotateScenario({ feature: 'Orders', story: 'Checkout readiness', severity: 'normal' });
  const surface = new CatalogPage(page);
  await surface.open();
  await allure.step('Add backpack', async () => {
    await surface.addBackpackToCart();
    await expect(page.getByTestId('cart-count')).toHaveText('1');
    await expect(page.getByTestId('cart-total')).toHaveText('$58.00');
    await expect(page.getByRole('button', { name: 'Continue to checkout' })).toBeEnabled();
  });
});

test('four backpacks have the correct checkout total', async ({ page, users }) => {
  await annotateScenario({ feature: 'Orders', story: 'Multiple item checkout', severity: 'normal' });
  const surface = new CatalogPage(page);
  await surface.open();
  await allure.step('Build four item cart', async () => {
    await surface.setQuantity(4);
    await surface.addBackpackToCart();
    await expect(page.getByTestId('cart-total')).toHaveText('$232.00');
  });
  await allure.step('Continue to checkout', async () => {
    await surface.continueToCheckout();
    await expect(page.getByRole('status')).toHaveText('Checkout is ready for 4 item(s)');
  });
});

test('filtering catalog preserves the cart preview', async ({ page, users }) => {
  await annotateScenario({ feature: 'Orders', story: 'Cart preservation', severity: 'normal' });
  const surface = new CatalogPage(page);
  await surface.open();
  await allure.step('Build cart', async () => {
    await surface.setQuantity(2);
    await surface.addBackpackToCart();
  });
  await allure.step('Search without losing cart', async () => {
    maybeFlake(0.25, 'cart preview synchronization after catalog filtering');
    await surface.search('bottle');
    await expect(page.getByTestId('cart-count')).toHaveText('2');
    await expect(page.getByTestId('cart-total')).toHaveText('$116.00');
    await expect(page.getByRole('button', { name: 'Continue to checkout' })).toBeEnabled();
  });
});

test('delivery selection preserves the checkout quantity', async ({ page, users }) => {
  await annotateScenario({ feature: 'Orders', story: 'Delivery and checkout', severity: 'normal' });
  const surface = new CatalogPage(page);
  await surface.open();
  await allure.step('Build cart with standard delivery', async () => {
    await surface.setQuantity(3);
    await surface.addBackpackToCart();
  });
  await allure.step('Change delivery and continue', async () => {
    await surface.selectExpressDelivery();
    await expect(page.getByTestId('cart-total')).toHaveText('$174.00');
    await surface.continueToCheckout();
    await expect(page.getByRole('status')).toHaveText('Checkout is ready for 3 item(s)');
  });
});
