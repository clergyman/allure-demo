import { LoginPage } from '../../pages/LoginPage';
import { expect, test } from '../../fixtures/test';

test('buyer can sign in', async ({ page, users }) => {
  const loginPage = new LoginPage(page);

  await test.step('Open the sign in page', async () => {
    await loginPage.open();
  });

  await test.step('Submit buyer credentials', async () => {
    await loginPage.login(users.buyer.email, users.buyer.password);
  });

  await test.step('Verify the buyer is welcomed', async () => {
    await expect(page.getByRole('status')).toHaveText('Welcome back');
  });
});
