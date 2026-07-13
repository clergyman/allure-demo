import { Page } from '@playwright/test';

import { loginPageHtml } from '../helpers/demoPages';

export class LoginPage {
  constructor(private readonly page: Page) {}

  async open() {
    await this.page.setContent(loginPageHtml);
  }

  async login(email: string, password: string) {
    await this.page.getByLabel('Email').fill(email);
    await this.page.getByLabel('Password').fill(password);
    await this.page.getByRole('button', { name: 'Sign in' }).click();
  }
}
