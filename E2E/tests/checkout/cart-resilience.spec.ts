import { CatalogPage } from '../../pages/CatalogPage';
import { expect, test } from '../../fixtures/test';
import { maybeFlake } from '../flaky';

const cartScenarios = [
  {
    name: 'cart accepts first backpack item',
    probability: 0,
  },
  {
    name: 'cart preserves add action during checkout handoff',
    probability: 0.35,
  },
  {
    name: 'cart status survives a delayed stock check',
    probability: 0.5,
  },
  {
    name: 'checkout intent is remembered after catalog refresh',
    probability: 0.5,
  },
  {
    name: 'cart badge update is visible before checkout',
    probability: 0.45,
  },
];

for (const scenario of cartScenarios) {
  test(`${scenario.name} @flake-${Math.round(scenario.probability * 100)}`, async ({
    page,
  }) => {
    const catalogPage = new CatalogPage(page);

    await test.step('Open the catalog page', async () => {
      await catalogPage.open();
    });

    await test.step('Add Demo Backpack to the cart', async () => {
      await catalogPage.addBackpackToCart();
    });

    await test.step('Simulate checkout handoff stability', async () => {
      maybeFlake(scenario.probability, scenario.name);
    });

    await test.step('Verify the cart still shows the added item', async () => {
      await expect(page.getByRole('status')).toHaveText(
        'Demo Backpack added to cart',
      );
    });
  });
}
