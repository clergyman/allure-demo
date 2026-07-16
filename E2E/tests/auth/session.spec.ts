import * as allure from 'allure-js-commons';

import { LoginPage } from '../../pages/LoginPage';
import { expect, test } from '../../fixtures/test';
import { maybeFlake } from '../flaky';
import { annotateScenario, attachScreenshot } from '../metadata';

test('guest opens the sign in form', async ({ page }) => {
  await annotateScenario({
    feature: 'Identity',
    story: 'Guest session entry',
    severity: 'trivial',
  });

  const loginPage = new LoginPage(page);

  await allure.step('Open sign in entry point', async () => {
    await loginPage.open();
    await expect(page.getByRole('heading', { name: 'Demo Shop' })).toBeVisible();
    await attachScreenshot('guest-session-entry', await page.screenshot());
  });

  await allure.step('Verify no authenticated state is shown yet', async () => {
    await expect(page.getByRole('status')).toHaveText('');
  });
});

test('returning buyer sees the session banner', async ({ page, users }) => {
  await annotateScenario({
    feature: 'Identity',
    story: 'Returning buyer session',
    severity: 'normal',
  });

  const loginPage = new LoginPage(page);

  await allure.step('Recreate returning buyer session', async () => {
    await allure.step('Open the sign in page', async () => {
      await loginPage.open();
    });
    await allure.step('Submit known buyer credentials', async () => {
      await loginPage.login(users.buyer.email, users.buyer.password);
    });
  });

  await allure.step('Verify visible session banner', async () => {
    await expect(page.getByRole('status')).toHaveText('Welcome back');
    await attachScreenshot('returning-buyer-session', await page.screenshot());
  });
});

test('password retry recovers after a typo', async ({ page, users }) => {
  await annotateScenario({
    feature: 'Identity',
    story: 'Password retry',
    severity: 'minor',
  });

  const loginPage = new LoginPage(page);

  await allure.step('Start retry flow after typo', async () => {
    await loginPage.open();
    await page.getByLabel('Email').fill(users.buyer.email);
    await page.getByLabel('Password').fill('wrong-password');
    await attachScreenshot('password-typo-before-retry', await page.screenshot());
  });

  await allure.step('Recover with the correct password', async () => {
    await page.getByLabel('Password').fill(users.buyer.password);
    await page.getByRole('button', { name: 'Sign in' }).click();
  });

  await allure.step('Confirm retry success', async () => {
    maybeFlake(0.2, 'password retry confirmation after a corrected typo');
    await expect(page.getByRole('status')).toHaveText('Welcome back');
    await attachScreenshot('password-retry-success', await page.screenshot());
  });
});
