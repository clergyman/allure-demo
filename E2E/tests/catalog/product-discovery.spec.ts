import { CatalogPage } from '../../pages/CatalogPage';
import { expect, test } from '../../fixtures/test';
import { maybeFlake } from '../flaky';

const catalogScenarios = [
  {
    name: 'buyer sees backpack product tile',
    probability: 0,
    expectedStatus: 'Demo Backpack added to cart',
  },
  {
    name: 'buyer adds backpack after product recommendations load',
    probability: 0.15,
    expectedStatus: 'Demo Backpack added to cart',
  },
  {
    name: 'cart toast appears after add to cart',
    probability: 0.25,
    expectedStatus: 'Demo Backpack added to cart',
  },
  {
    name: 'catalog remains usable after a slow inventory refresh',
    probability: 0.3,
    expectedStatus: 'Demo Backpack added to cart',
  },
  {
    name: 'repeat catalog visit keeps product actions enabled',
    probability: 0.1,
    expectedStatus: 'Demo Backpack added to cart',
  },
];

for (const scenario of catalogScenarios) {
  test(`${scenario.name} @flake-${Math.round(scenario.probability * 100)}`, async ({
    page,
  }) => {
    const catalogPage = new CatalogPage(page);

    await test.step('Open the catalog page', async () => {
      await catalogPage.open();
    });

    await test.step('Verify the Demo Backpack product tile is visible', async () => {
      await expect(
        page.getByRole('heading', { name: 'Demo Backpack' }),
      ).toBeVisible();
    });

    await test.step('Add Demo Backpack to the cart', async () => {
      await catalogPage.addBackpackToCart();
    });

    await test.step('Simulate catalog service stability', async () => {
      maybeFlake(scenario.probability, scenario.name);
    });

    await test.step('Verify the catalog confirmation message', async () => {
      await expect(page.getByRole('status')).toHaveText(
        scenario.expectedStatus,
      );
    });
  });
}
