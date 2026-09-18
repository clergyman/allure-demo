import allure

from http_demo import expect_status, metadata
from triage_contracts import european_price


def test_category_navigation(http_api):
    metadata('Catalog', 'Category navigation', 'catalog-service')
    response = http_api.request('GET', '/catalog/categories')
    expect_status(response, 200)
    assert 'bags' in response['json']['categories']


def test_product_review_summary(http_api):
    metadata('Catalog', 'Product reviews', 'catalog-service')
    response = http_api.request('GET', '/catalog/products/product-1/reviews')
    expect_status(response, 200)
    assert response['json']['count'] == 38
    assert 0 <= response['json']['rating'] <= 5


def test_availability_after_category_discovery(http_api):
    metadata('Catalog', 'Product availability', 'catalog-service')
    expect_status(http_api.request('GET', '/catalog/categories'), 200)
    response = http_api.request('GET', '/catalog/products/product-1/availability')
    expect_status(response, 200)
    assert response['json']['available'] and response['json']['stock'] > 0


def test_regional_price_uses_euros(http_api):
    european_price(http_api, 'EU', 'web', 'buyer')


def test_recommendations_survive_index_outage(http_api):
    metadata('Catalog', 'Product recommendations', 'catalog-service')
    response = http_api.request('GET', '/catalog/recommendations?product=product-1')
    expect_status(response, 200)


def test_product_gallery_has_primary_image(http_api):
    metadata('Catalog', 'Product media', 'catalog-service')
    response = http_api.request('GET', '/catalog/products/product-1/media')
    expect_status(response, 200)
    with allure.step('Decode primary gallery image'):
        assert response['json']['images'][0]['url'].startswith('https://')
