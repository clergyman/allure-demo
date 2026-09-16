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

  async search(query: string) {
    await this.page.getByLabel('Search catalog').fill(query);
    await this.page.getByRole('button', { name: 'Apply filters' }).click();
  }

  async selectExpressDelivery() {
    await this.page.getByLabel('Delivery speed').selectOption('Express delivery');
  }

  async setQuantity(quantity: number) {
    await this.page.getByLabel('Quantity').fill(String(quantity));
  }

  async continueToCheckout() {
    await this.page.getByRole('button', { name: 'Continue to checkout' }).click();
  }
}
