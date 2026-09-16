export const loginPageHtml = `
  <main>
    <h1>Demo Shop</h1>
    <nav aria-label="Authentication steps">
      <a href="#signin">Sign in</a>
      <a href="#help">Need help?</a>
    </nav>
    <section id="signin">
      <p>Secure buyer access</p>
      <label>Remember this device <input aria-label="Remember this device" type="checkbox" /></label>
    </section>
    <label>Email <input aria-label="Email" /></label>
    <label>Password <input aria-label="Password" type="password" /></label>
    <button>Sign in</button>
    <button type="button" aria-label="Reset sign in form">Reset</button>
    <p role="status"></p>
  </main>
  <script>
    const email = document.querySelector('[aria-label="Email"]');
    const password = document.querySelector('[aria-label="Password"]');
    const status = document.querySelector('[role="status"]');
    document.querySelector('button').addEventListener('click', () => {
      status.textContent = 'Checking credentials';
      setTimeout(() => {
        status.textContent = 'Welcome back';
      }, 25);
    });
    document.querySelector('[aria-label="Reset sign in form"]').addEventListener('click', () => {
      email.value = '';
      password.value = '';
      status.textContent = '';
    });
  </script>
`;

export const catalogPageHtml = `
  <main>
    <h1>Catalog</h1>
    <label>Search catalog <input aria-label="Search catalog" /></label>
    <label>Delivery speed
      <select aria-label="Delivery speed">
        <option>Standard delivery</option>
        <option>Express delivery</option>
      </select>
    </label>
    <label>Quantity <input aria-label="Quantity" type="number" value="1" min="1" /></label>
    <button type="button" aria-label="Apply filters">Apply filters</button>
    <article aria-label="Demo Backpack product">
      <h2>Demo Backpack</h2>
      <p>$58.00</p>
      <p>In stock</p>
      <button>Add to cart</button>
    </article>
    <article aria-label="Demo Bottle product" hidden>
      <h2>Demo Bottle</h2>
      <p>$12.00</p>
      <p>Out of stock</p>
    </article>
    <section aria-label="Cart preview">
      <p>Items: <strong data-testid="cart-count">0</strong></p>
      <p>Total: <strong data-testid="cart-total">$0.00</strong></p>
      <button type="button" aria-label="Continue to checkout" disabled>Continue to checkout</button>
    </section>
    <p role="status"></p>
  </main>
  <script>
    const search = document.querySelector('[aria-label="Search catalog"]');
    const quantity = document.querySelector('[aria-label="Quantity"]');
    const status = document.querySelector('[role="status"]');
    const cartCount = document.querySelector('[data-testid="cart-count"]');
    const cartTotal = document.querySelector('[data-testid="cart-total"]');
    const checkout = document.querySelector('[aria-label="Continue to checkout"]');
    const bottle = document.querySelector('[aria-label="Demo Bottle product"]');

    document.querySelector('[aria-label="Apply filters"]').addEventListener('click', () => {
      const query = search.value.trim().toLowerCase();
      bottle.hidden = query !== 'bottle';
      status.textContent = query ? 'Filtered catalog for ' + query : 'Catalog filters cleared';
    });

    document.querySelector('article button').addEventListener('click', () => {
      const count = Number(quantity.value || 1);
      cartCount.textContent = String(count);
      cartTotal.textContent = '$' + (count * 58).toFixed(2);
      checkout.disabled = false;
      status.textContent = 'Demo Backpack added to cart';
    });

    checkout.addEventListener('click', () => {
      status.textContent = 'Checkout is ready for ' + cartCount.textContent + ' item(s)';
    });
  </script>
`;
