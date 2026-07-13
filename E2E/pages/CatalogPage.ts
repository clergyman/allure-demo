import { Page } from '@playwright/test';

import { catalogPageHtml } from '../helpers/demoPages';

export class CatalogPage {
  constructor(private readonly page: Page) {}

  async open() {
    await this.page.setContent(catalogPageHtml);
  }

  async addBackpackToCart() {
    await this.page.getByRole('button', { name: 'Add to cart' }).click();
  }
}
