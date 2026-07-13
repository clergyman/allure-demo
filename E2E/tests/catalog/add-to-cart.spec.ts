import { CatalogPage } from '../../pages/CatalogPage';
import { expect, test } from '../../fixtures/test';

test('buyer can add a product to the cart', async ({ page }) => {
  const catalogPage = new CatalogPage(page);

  await test.step('Open the catalog page', async () => {
    await catalogPage.open();
  });

  await test.step('Add Demo Backpack to the cart', async () => {
    await catalogPage.addBackpackToCart();
  });

  await test.step('Verify the cart confirmation message', async () => {
    await expect(page.getByRole('status')).toHaveText(
      'Demo Backpack added to cart',
    );
  });
});
