import * as allure from 'allure-js-commons';

import { LoginPage } from '../../pages/LoginPage';
import { expect, test } from '../../fixtures/test';
import { annotateScenario } from '../metadata';
import { maybeFlake } from '../flaky';

test('buyer password is masked while typing', async ({ page, users }) => {
  await annotateScenario({ feature: 'Identity', story: 'Credential privacy', severity: 'normal' });
  const surface = new LoginPage(page);
  await surface.open();
  await allure.step('Enter password', async () => {
    await page.getByLabel('Password').fill(users.buyer.password);
  });
  await allure.step('Verify password privacy', async () => {
    await expect(page.getByLabel('Password')).toHaveAttribute('type', 'password');
    await expect(page.getByLabel('Password')).toHaveValue(users.buyer.password);
  });
});

test('buyer can clear credentials before signing in', async ({ page, users }) => {
  await annotateScenario({ feature: 'Identity', story: 'Sign in form reset', severity: 'normal' });
  const surface = new LoginPage(page);
  await surface.open();
  await allure.step('Enter credentials', async () => {
    await page.getByLabel('Email').fill(users.buyer.email);
    await page.getByLabel('Password').fill(users.buyer.password);
  });
  await allure.step('Reset credentials', async () => {
    await page.getByRole('button', { name: 'Reset sign in form' }).click();
    await expect(page.getByLabel('Email')).toHaveValue('');
    await expect(page.getByLabel('Password')).toHaveValue('');
  });
});

test('reset clears the signed in confirmation', async ({ page, users }) => {
  await annotateScenario({ feature: 'Identity', story: 'Sign in form reset', severity: 'normal' });
  const surface = new LoginPage(page);
  await surface.open();
  await allure.step('Sign in', async () => {
    await surface.login(users.buyer.email, users.buyer.password);
    await expect(page.getByRole('status')).toHaveText('Welcome back');
  });
  await allure.step('Clear confirmation', async () => {
    await page.getByRole('button', { name: 'Reset sign in form' }).click();
    await expect(page.getByRole('status')).toBeEmpty();
  });
});

test('buyer can turn off remembering this device', async ({ page, users }) => {
  await annotateScenario({ feature: 'Identity', story: 'Session preferences', severity: 'normal' });
  const surface = new LoginPage(page);
  await surface.open();
  await allure.step('Toggle device preference', async () => {
    await page.getByLabel('Remember this device').check();
    await expect(page.getByLabel('Remember this device')).toBeChecked();
    await page.getByLabel('Remember this device').uncheck();
    await expect(page.getByLabel('Remember this device')).not.toBeChecked();
  });
});

test('buyer can reach authentication help', async ({ page, users }) => {
  await annotateScenario({ feature: 'Identity', story: 'Sign in assistance', severity: 'normal' });
  const surface = new LoginPage(page);
  await surface.open();
  await allure.step('Open help link', async () => {
    await page.getByRole('link', { name: 'Need help?' }).click();
    await expect(page.getByRole('link', { name: 'Need help?' })).toHaveAttribute('href', '#help');
    await expect(page.getByLabel('Email')).toBeVisible();
  });
});

test('buyer can sign in again after resetting the form', async ({ page, users }) => {
  await annotateScenario({ feature: 'Identity', story: 'Repeat sign in', severity: 'normal' });
  const surface = new LoginPage(page);
  await surface.open();
  await allure.step('Complete first sign in', async () => {
    await surface.login(users.buyer.email, users.buyer.password);
    await expect(page.getByRole('status')).toHaveText('Welcome back');
    await page.getByRole('button', { name: 'Reset sign in form' }).click();
  });
  await allure.step('Sign in after reset', async () => {
    maybeFlake(0.25, 'session renewal after sign in form reset');
    await surface.login(users.buyer.email, users.buyer.password);
    await expect(page.getByRole('status')).toHaveText('Welcome back');
  });
});
