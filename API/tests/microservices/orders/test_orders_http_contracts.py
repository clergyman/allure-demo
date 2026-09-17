import allure

from http_demo import expect_status, metadata


def test_quote_includes_shipping(http_api):
    metadata('Orders', 'Shipping quote', 'orders-service')
    response = http_api.request('POST', '/orders/quote', {'product_id': 'product-1', 'quantity': 1})
    expect_status(response, 200)
    assert response['json']['total'] == response['json']['subtotal'] + response['json']['shipping']


def test_customer_cancels_order(http_api):
    metadata('Orders', 'Order cancellation', 'orders-service')
    response = http_api.request('POST', '/orders/order-1/cancel', {'reason': 'Changed my mind'})
    expect_status(response, 200)
    assert response['json']['status'] == 'cancelled'


def test_delivery_tracking_after_quote(http_api):
    metadata('Orders', 'Delivery tracking', 'orders-service')
    expect_status(http_api.request('POST', '/orders/quote', {'product_id': 'product-1', 'quantity': 1}), 200)
    response = http_api.request('GET', '/orders/order-1/tracking')
    expect_status(response, 200)
    assert response['json']['status'] == 'in_transit'


def test_full_refund_returns_paid_amount(http_api):
    metadata('Orders', 'Refund settlement', 'orders-service')
    response = http_api.request('POST', '/orders/order-1/refund', {'amount': 49.99, 'currency': 'EUR'})
    expect_status(response, 200)
    with allure.step('Verify full refund amount'):
        assert response['json']['amount'] == 49.99, 'Payment ledger omitted shipping adjustment'


def test_payment_authorization_completes(http_api):
    metadata('Orders', 'Payment authorization', 'orders-service')
    response = http_api.request('POST', '/orders/order-1/payment', {'payment_method': 'demo-card', 'amount': 49.99})
    expect_status(response, 200)


def test_invoice_exposes_tax_breakdown(http_api):
    metadata('Orders', 'Invoice tax breakdown', 'orders-service')
    response = http_api.request('GET', '/orders/order-1/invoice')
    expect_status(response, 200)
    with allure.step('Decode invoice tax contract'):
        assert response['json']['invoice']['tax']['rate'] == 0.2
