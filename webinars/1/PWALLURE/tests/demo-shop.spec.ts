import { expect, type Page, test } from '@playwright/test';

async function openDemoShop(page: Page) {
  await page.setContent(`
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8" />
        <title>Webinar Demo Shop</title>
        <style>
          body {
            margin: 0;
            font-family: Arial, sans-serif;
            color: #202124;
            background: #f6f7f9;
          }
          main {
            max-width: 880px;
            margin: 32px auto;
            padding: 24px;
            background: white;
            border: 1px solid #d7dce2;
          }
          header {
            display: flex;
            justify-content: space-between;
            gap: 16px;
            align-items: center;
            border-bottom: 1px solid #d7dce2;
            padding-bottom: 16px;
          }
          label, input, button {
            font-size: 14px;
          }
          input {
            padding: 8px;
            border: 1px solid #aeb6c2;
          }
          button {
            padding: 9px 12px;
            border: 0;
            color: white;
            background: #1f6feb;
            cursor: pointer;
          }
          section {
            margin-top: 20px;
          }
          .product {
            display: flex;
            justify-content: space-between;
            gap: 16px;
            align-items: center;
            padding: 14px 0;
            border-bottom: 1px solid #edf0f4;
          }
          .product:hover {
            background: #f2f6ff;
          }
          .flash {
            outline: 3px solid #79ffe1;
            transition: outline 200ms ease;
          }
          .muted {
            color: #667085;
          }
          .error {
            color: #b42318;
          }
        </style>
      </head>
      <body>
        <main>
          <header>
            <div>
              <h1>Webinar Demo Shop</h1>
              <p class="muted">A tiny checkout flow for reporting examples.</p>
            </div>
            <strong data-testid="session-state">Guest</strong>
          </header>

          <section aria-label="Sign in">
            <label for="email">Email</label>
            <input id="email" data-testid="email" value="sasha@example.com" />
            <button data-testid="sign-in">Sign in</button>
          </section>

          <section aria-label="Catalog">
            <label for="search">Search catalog</label>
            <input id="search" data-testid="search" placeholder="Search products" />
            <p data-testid="search-result" class="muted">Showing all products</p>
            <div class="product" data-product-name="Travel Backpack">
              <span>Travel Backpack</span>
              <button data-testid="add-backpack">Add to cart</button>
            </div>
            <div class="product" data-product-name="Noise Canceling Headphones">
              <span>Noise Canceling Headphones</span>
              <button data-testid="add-headphones">Add to cart</button>
            </div>
          </section>

          <section aria-label="Cart">
            <h2>Cart</h2>
            <p data-testid="cart-count">0 items</p>
            <p data-testid="cart-total">$0.00</p>
            <p data-testid="checkout-status" class="muted">Cart is empty</p>
            <label for="promo">Promo code</label>
            <input id="promo" data-testid="promo-code" />
            <button data-testid="apply-promo">Apply promo</button>
            <p data-testid="promo-status" class="muted">No promo applied</p>
            <p data-testid="promo-message" class="error" hidden>Promo code expired</p>
          </section>
        </main>

        <script>
          const sessionState = document.querySelector('[data-testid="session-state"]');
          const email = document.querySelector('[data-testid="email"]');
          const search = document.querySelector('[data-testid="search"]');
          const searchResult = document.querySelector('[data-testid="search-result"]');
          const cartCount = document.querySelector('[data-testid="cart-count"]');
          const cartTotal = document.querySelector('[data-testid="cart-total"]');
          const checkoutStatus = document.querySelector('[data-testid="checkout-status"]');
          const promoCode = document.querySelector('[data-testid="promo-code"]');
          const promoStatus = document.querySelector('[data-testid="promo-status"]');
          const promoMessage = document.querySelector('[data-testid="promo-message"]');

          let items = 0;
          let total = 0;

          document.querySelector('[data-testid="sign-in"]').addEventListener('click', () => {
            sessionState.textContent = 'Signed in as ' + email.value;
          });

          search.addEventListener('input', () => {
            const value = search.value.trim();
            searchResult.textContent = value
              ? 'Showing results for "' + value + '"'
              : 'Showing all products';
          });

          function refreshCart(message) {
            cartCount.textContent = items + (items === 1 ? ' item' : ' items');
            cartTotal.textContent = '$' + total.toFixed(2);
            checkoutStatus.textContent = message;
            cartTotal.classList.add('flash');
            window.setTimeout(() => cartTotal.classList.remove('flash'), 350);
          }

          document.querySelector('[data-testid="add-backpack"]').addEventListener('click', () => {
            items += 1;
            total += 79;
            refreshCart('Travel Backpack added');
          });

          document.querySelector('[data-testid="add-headphones"]').addEventListener('click', () => {
            items += 1;
            total += 129;
            refreshCart('Checking headphones discount...');
            window.setTimeout(() => {
              checkoutStatus.textContent = 'Discount service returned no adjustment';
            }, 300);
          });

          document.querySelector('[data-testid="apply-promo"]').addEventListener('click', () => {
            promoStatus.textContent = 'Validating promo code...';
            window.setTimeout(() => {
              promoMessage.hidden = promoCode.value !== 'EXPIRED10';
              promoStatus.textContent = promoMessage.hidden
                ? 'Promo code accepted'
                : 'Promo code rejected';
            }, 300);
          });
        </script>
      </body>
    </html>
  `);
}

test.beforeEach(async ({ page }) => {
  await openDemoShop(page);
});

test('returning shopper can sign in', async ({ page }) => {
  await page.getByTestId('email').clear();
  await page.getByTestId('email').pressSequentially('sasha@example.com', {
    delay: 35,
  });
  await page.getByTestId('sign-in').click();

  await expect(page.getByTestId('session-state')).toHaveText(
    'Signed in as sasha@example.com',
  );
});

test('shopper can search the catalog', async ({ page }) => {
  await page.getByTestId('search').pressSequentially('backpack', { delay: 40 });

  await expect(page.getByTestId('search-result')).toHaveText(
    'Showing results for "backpack"',
  );
});

test('shopper can add a backpack to the cart', async ({ page }) => {
  await page.getByTestId('add-backpack').hover();
  await page.getByTestId('add-backpack').click();

  await expect(page.getByTestId('cart-count')).toHaveText('1 item');
  await expect(page.getByTestId('cart-total')).toHaveText('$79.00');
  await expect(page.getByTestId('checkout-status')).toHaveText(
    'Travel Backpack added',
  );
});

test('checkout total includes the selected headphones discount', async ({ page }) => {
  await page.getByTestId('add-headphones').hover();
  await page.getByTestId('add-headphones').click();
  await expect(page.getByTestId('checkout-status')).toHaveText(
    'Discount service returned no adjustment',
  );
  await test.info().attach('checkout-discount-audit.csv', {
    body:
      'sku,quantity,unit_price,promo_code,expected_total,actual_total\n' +
      'headphones,1,129.00,LOYAL30,99.00,129.00\n' +
      'backpack,0,79.00,LOYAL30,0.00,0.00\n' +
      'subtotal,1,,LOYAL30,129.00,129.00\n' +
      'discount,1,,LOYAL30,-30.00,0.00\n' +
      'grand_total,1,,LOYAL30,99.00,129.00\n',
    contentType: 'text/csv',
  });
  await page.getByTestId('cart-total').hover();

  await expect(page.getByTestId('cart-total')).toHaveText('$99.00');
});

test('expired promo code is accepted for loyal shoppers', async ({ page }) => {
  await page.getByTestId('promo-code').pressSequentially('EXPIRED10', {
    delay: 35,
  });
  await page.getByTestId('apply-promo').click();
  await expect(page.getByTestId('promo-status')).toHaveText(
    'Promo code rejected',
  );

  await expect(page.getByTestId('promo-message')).toBeHidden();
});

test('payment service returns a valid approval contract', async ({ page }) => {
  await page.getByTestId('add-backpack').click();

  throw new Error('Payment service response is missing approvalCode.');
});
