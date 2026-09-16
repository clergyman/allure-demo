import * as allure from 'allure-js-commons';

import { LoginPage } from '../../pages/LoginPage';
import { expect, test } from '../../fixtures/test';
import { annotateScenario, attachScreenshot } from '../metadata';

test('buyer signs in with valid credentials @smoke', async ({ page, users }) => {
  await annotateScenario({
    feature: 'Identity',
    story: 'Buyer sign in',
    severity: 'blocker',
    jira: 'ATO-610',
    smoke: true
  });
  await allure.label('work_item', '27');
  await allure.issue('27', 'epic');
  await allure.description(
    'Validates the primary buyer authentication path from form load to signed-in confirmation.',
  );

  const loginPage = new LoginPage(page);

  await allure.step('Open authentication surface', async () => {
    await allure.step('Render the sign in page', async () => {
      await loginPage.open();
    });
    await allure.step('Review authentication support links', async () => {
      await expect(page.getByRole('link', { name: 'Sign in' })).toBeVisible();
      await expect(page.getByRole('link', { name: 'Need help?' })).toBeVisible();
    });
    await allure.step('Verify the form is ready for input', async () => {
      await expect(page.getByLabel('Email')).toBeVisible();
      await expect(page.getByLabel('Password')).toBeVisible();
      await expect(page.getByLabel('Remember this device')).toBeVisible();
    });
    await attachScreenshot('login-form-ready', await page.screenshot());
  });

  await allure.step('Prepare buyer session preferences', async () => {
    await page.getByLabel('Remember this device').check();
    await expect(page.getByLabel('Remember this device')).toBeChecked();
    await attachScreenshot('login-remember-device-selected', await page.screenshot());
  });

  await allure.step('Submit buyer credentials', async () => {
    await allure.step('Fill email and password', async () => {
      await loginPage.login(users.buyer.email, users.buyer.password);
    });
    await expect(page.getByRole('status')).toContainText(/Checking credentials|Welcome back/);
    await attachScreenshot('login-submitted', await page.screenshot());
  });

  await allure.step('Confirm signed-in state', async () => {
    await expect(page.getByRole('status')).toHaveText('Welcome back');
    await attachScreenshot('login-success', await page.screenshot());
  });
});
