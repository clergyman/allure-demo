import { LoginPage } from '../../pages/LoginPage';
import { expect, test } from '../../fixtures/test';
import { maybeFlake } from '../flaky';

const sessionScenarios = [
  {
    name: 'guest can open the sign in form',
    probability: 0,
    email: 'guest@example.com',
  },
  {
    name: 'buyer receives a welcome message after sign in',
    probability: 0.05,
    email: 'buyer@example.com',
  },
  {
    name: 'returning buyer session banner is announced',
    probability: 0.1,
    email: 'returning.buyer@example.com',
  },
  {
    name: 'keyboard-first buyer can submit credentials',
    probability: 0.2,
    email: 'keyboard.buyer@example.com',
  },
  {
    name: 'password retry flow recovers after a typo',
    probability: 0.4,
    email: 'retry.buyer@example.com',
  },
];

for (const scenario of sessionScenarios) {
  test(`${scenario.name} @flake-${Math.round(scenario.probability * 100)}`, async ({
    page,
    users,
  }) => {
    const loginPage = new LoginPage(page);

    await test.step('Open the sign in page', async () => {
      await loginPage.open();
    });

    await test.step(`Submit credentials for ${scenario.email}`, async () => {
      await loginPage.login(scenario.email, users.buyer.password);
    });

    await test.step('Simulate session service stability', async () => {
      maybeFlake(scenario.probability, scenario.name);
    });

    await test.step('Verify the session welcome message', async () => {
      await expect(page.getByRole('status')).toHaveText('Welcome back');
    });
  });
}
