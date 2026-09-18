from http_demo import expect_status, metadata
from triage_contracts import european_price


def test_portuguese_web_buyer_price(http_api):
    european_price(http_api, 'PT', 'web', 'buyer')


def test_german_mobile_buyer_price(http_api):
    european_price(http_api, 'DE', 'mobile', 'buyer')


def test_french_guest_price(http_api):
    european_price(http_api, 'FR', 'web', 'guest')


def test_spanish_loyalty_price(http_api):
    european_price(http_api, 'ES', 'web', 'loyalty')


def test_italian_app_price(http_api):
    european_price(http_api, 'IT', 'app', 'buyer')


def test_dutch_business_price(http_api):
    european_price(http_api, 'NL', 'web', 'business')


def test_irish_guest_mobile_price(http_api):
    european_price(http_api, 'IE', 'mobile', 'guest')


def test_belgian_loyalty_app_price(http_api):
    european_price(http_api, 'BE', 'app', 'loyalty')


def test_austrian_business_mobile_price(http_api):
    european_price(http_api, 'AT', 'mobile', 'business')


def test_category_tree_contains_bottles(http_api):
    metadata('Catalog', 'Category navigation', 'catalog-service')
    response = http_api.request('GET', '/catalog/categories')
    expect_status(response, 200)
    assert 'bottles' in response['json']['categories']


def test_category_names_are_unique(http_api):
    metadata('Catalog', 'Category navigation', 'catalog-service')
    response = http_api.request('GET', '/catalog/categories')
    expect_status(response, 200)
    categories = response['json']['categories']
    assert len(categories) == len(set(categories))


def test_reviews_do_not_expose_customer_emails(http_api):
    metadata('Catalog', 'Product reviews', 'catalog-service')
    response = http_api.request('GET', '/catalog/products/product-1/reviews')
    expect_status(response, 200)
    assert 'email' not in response['json']


def test_review_count_is_integer(http_api):
    metadata('Catalog', 'Product reviews', 'catalog-service')
    response = http_api.request('GET', '/catalog/products/product-1/reviews')
    expect_status(response, 200)
    assert isinstance(response['json']['count'], int)


def test_stock_is_non_negative(http_api):
    metadata('Catalog', 'Product availability', 'catalog-service')
    response = http_api.request('GET', '/catalog/products/product-1/availability')
    expect_status(response, 200)
    assert response['json']['stock'] >= 0


def test_stock_flag_matches_quantity(http_api):
    metadata('Catalog', 'Product availability', 'catalog-service')
    response = http_api.request('GET', '/catalog/products/product-1/availability')
    expect_status(response, 200)
    assert response['json']['available'] == (response['json']['stock'] > 0)


def test_us_price_remains_in_dollars(http_api):
    metadata('Catalog', 'Regional pricing', 'catalog-service')
    response = http_api.request('GET', '/catalog/products/product-1/price?region=US')
    expect_status(response, 200)
    assert response['json']['currency'] == 'USD'


def test_price_is_positive_after_review_read(http_api):
    metadata('Catalog', 'Regional pricing', 'catalog-service')
    expect_status(http_api.request('GET', '/catalog/products/product-1/reviews'), 200)
    response = http_api.request('GET', '/catalog/products/product-1/price?region=US')
    expect_status(response, 200)
    assert response['json']['amount'] > 0
