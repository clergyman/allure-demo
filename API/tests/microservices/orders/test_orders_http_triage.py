from http_demo import expect_status, metadata
from triage_contracts import full_refund


def test_card_refund_for_customer_cancellation(http_api):
    full_refund(http_api, 'customer-cancellation', 'card', 'web')


def test_wallet_refund_for_damaged_delivery(http_api):
    full_refund(http_api, 'damaged-delivery', 'wallet', 'app')


def test_bank_refund_for_lost_parcel(http_api):
    full_refund(http_api, 'lost-parcel', 'bank', 'support')


def test_card_refund_for_wrong_product(http_api):
    full_refund(http_api, 'wrong-product', 'card', 'mobile')


def test_wallet_refund_for_late_delivery(http_api):
    full_refund(http_api, 'late-delivery', 'wallet', 'web')


def test_card_refund_for_duplicate_purchase(http_api):
    full_refund(http_api, 'duplicate-purchase', 'card', 'app')


def test_bank_refund_for_supplier_recall(http_api):
    full_refund(http_api, 'supplier-recall', 'bank', 'support')


def test_wallet_refund_for_missing_accessory(http_api):
    full_refund(http_api, 'missing-accessory', 'wallet', 'mobile')


def test_card_refund_for_failed_quality_check(http_api):
    full_refund(http_api, 'quality-check', 'card', 'support')


def test_quote_shipping_is_non_negative(http_api):
    metadata('Orders', 'Shipping quote', 'orders-service')
    response = http_api.request('POST', '/orders/quote', {'product_id': 'product-1', 'quantity': 1})
    expect_status(response, 200)
    assert response['json']['shipping'] >= 0


def test_quote_subtotal_is_positive(http_api):
    metadata('Orders', 'Shipping quote', 'orders-service')
    response = http_api.request('POST', '/orders/quote', {'product_id': 'product-1', 'quantity': 1})
    expect_status(response, 200)
    assert response['json']['subtotal'] > 0


def test_quote_does_not_create_order(http_api):
    metadata('Orders', 'Shipping quote', 'orders-service')
    response = http_api.request('POST', '/orders/quote', {'product_id': 'product-1', 'quantity': 1})
    expect_status(response, 200)
    assert 'id' not in response['json']


def test_cancel_does_not_expose_payment_details(http_api):
    metadata('Orders', 'Order cancellation', 'orders-service')
    response = http_api.request('POST', '/orders/order-1/cancel', {'reason': 'Changed my mind'})
    expect_status(response, 200)
    assert 'payment_method' not in response['json']


def test_tracking_has_carrier(http_api):
    metadata('Orders', 'Delivery tracking', 'orders-service')
    response = http_api.request('GET', '/orders/order-1/tracking')
    expect_status(response, 200)
    assert response['json']['carrier'] == 'Demo Courier'


def test_tracking_hides_billing_address(http_api):
    metadata('Orders', 'Delivery tracking', 'orders-service')
    response = http_api.request('GET', '/orders/order-1/tracking')
    expect_status(response, 200)
    assert 'billing_address' not in response['json']


def test_invoice_has_document_id(http_api):
    metadata('Orders', 'Invoice tax breakdown', 'orders-service')
    response = http_api.request('GET', '/orders/order-1/invoice')
    expect_status(response, 200)
    assert response['json']['invoice']['id'] == 'invoice-1'
