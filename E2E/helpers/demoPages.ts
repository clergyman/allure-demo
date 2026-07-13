export const loginPageHtml = `
  <main>
    <h1>Demo Shop</h1>
    <label>Email <input aria-label="Email" /></label>
    <label>Password <input aria-label="Password" type="password" /></label>
    <button>Sign in</button>
    <p role="status"></p>
  </main>
  <script>
    document.querySelector('button').addEventListener('click', () => {
      document.querySelector('[role="status"]').textContent = 'Welcome back';
    });
  </script>
`;

export const catalogPageHtml = `
  <main>
    <h1>Catalog</h1>
    <article>
      <h2>Demo Backpack</h2>
      <button>Add to cart</button>
    </article>
    <p role="status"></p>
  </main>
  <script>
    document.querySelector('button').addEventListener('click', () => {
      document.querySelector('[role="status"]').textContent = 'Demo Backpack added to cart';
    });
  </script>
`;

