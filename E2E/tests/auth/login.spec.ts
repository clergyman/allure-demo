import * as allure from 'allure-js-commons';

import { LoginPage } from '../../pages/LoginPage';
import { expect, test } from '../../fixtures/test';
import { annotateScenario, attachScreenshot } from '../metadata';

test('buyer signs in with valid credentials @smoke', async ({ page, users }) => {
  await annotateScenario({
    feature: 'Authentication',
    story: 'Buyer sign in',
    severity: 'blocker',
    smoke: true,
  });
  await allure.description(
    'Validates the primary buyer authentication path from form load to signed-in confirmation.',
  );

  const loginPage = new LoginPage(page);

  await allure.step('Open authentication surface', async () => {
    await allure.step('Render the sign in page', async () => {
      await loginPage.open();
    });
    await allure.step('Verify the form is ready for input', async () => {
      await expect(page.getByLabel('Email')).toBeVisible();
      await expect(page.getByLabel('Password')).toBeVisible();
    });
    await attachScreenshot('login-form-ready', await page.screenshot());
  });

  await allure.step('Submit buyer credentials', async () => {
    await allure.step('Fill email and password', async () => {
      await loginPage.login(users.buyer.email, users.buyer.password);
    });
    await attachScreenshot('login-submitted', await page.screenshot());
  });

  await allure.step('Confirm signed-in state', async () => {
    await expect(page.getByRole('status')).toHaveText('Welcome back');
    await attachScreenshot('login-success', await page.screenshot());
  });
});
