import allure

from http_demo import expect_status, metadata


class TriageDefect(AssertionError):
    """A known demo defect whose service-level traceback is used for grouping."""


def verify_european_price(response):
    if response['json']['currency'] != 'EUR':
        raise TriageDefect('CAT-PRICE-001: regional price index ignores EUR storefront currency')


def verify_refresh_available(response):
    if response['status_code'] != 200:
        raise AssertionError('Token refresh must return HTTP 200')


def verify_full_refund(response):
    if response['json']['amount'] != 49.99:
        raise AssertionError('Full refund must include the paid shipping adjustment')


def european_price(http_api, country, channel, customer):
    metadata('Catalog', 'Regional pricing', 'catalog-service')
    allure.dynamic.parent_suite('Catalog')
    allure.dynamic.suite('Regional pricing')
    allure.dynamic.sub_suite('EUR storefronts')
    allure.dynamic.tag('triage-cluster')
    allure.dynamic.label('defect', 'CAT-PRICE-001')
    response = http_api.request('GET', f'/catalog/products/product-1/price?region=EU&country={country}&channel={channel}&customer={customer}')
    expect_status(response, 200)
    with allure.step('Validate regional price projection'):
        verify_european_price(response)


def refresh_session(http_api, client, reason, scope):
    metadata('Identity', 'Token rotation', 'identity-service')
    response = http_api.request('POST', '/identity/token/refresh', {
        'refresh_token': 'demo-refresh-secret', 'client': client,
        'reason': reason, 'scope': scope,
    })
    with allure.step('Validate signing key availability'):
        verify_refresh_available(response)


def full_refund(http_api, reason, method, channel):
    metadata('Orders', 'Refund settlement', 'orders-service')
    response = http_api.request('POST', '/orders/order-1/refund', {
        'amount': 49.99, 'currency': 'EUR', 'reason': reason,
        'payment_method': method, 'channel': channel,
    })
    expect_status(response, 200)
    with allure.step('Validate full refund ledger amount'):
        verify_full_refund(response)
