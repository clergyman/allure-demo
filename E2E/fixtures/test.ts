import { test as base } from '@playwright/test';

import { demoUsers } from './users';

type DemoFixtures = {
  users: typeof demoUsers;
};

export const test = base.extend<DemoFixtures>({
  users: async ({}, use) => {
    await use(demoUsers);
  },
});

export { expect } from '@playwright/test';

