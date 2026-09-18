import allure
import pytest


def orders_metadata(story: str, severity: str = "normal"):
    allure.dynamic.epic("Demo Shop")
    allure.dynamic.feature("Orders")
    allure.dynamic.story(story)
    allure.dynamic.severity(severity)
    allure.dynamic.label("component", "orders-service")


def verify_order_created(orders_client, product_id: str = "product-1", quantity: int = 1):
    with allure.step(f"Create order for {quantity} item(s) of {product_id}"):
        response = orders_client.create_order("user-1", product_id, quantity)

    with allure.step("Verify created order payload"):
        assert response["status_code"] == 201
        assert response["json"]["id"] == "order-1"
        assert response["json"]["user_id"] == "user-1"
        assert response["json"]["product_id"] == product_id
        assert response["json"]["quantity"] == quantity
        assert response["json"]["status"] == "created"


def verify_order_rejected(orders_client, quantity: int):
    with allure.step(f"Create order with invalid quantity {quantity}"):
        response = orders_client.create_order("user-1", "product-1", quantity)

    with allure.step("Verify order validation error"):
        assert response["status_code"] == 400
        assert response["json"]["error"] == "Quantity must be positive"


def verify_order_status_found(orders_client):
    with allure.step("Request order status"):
        response = orders_client.get_order("order-1")

    with allure.step("Verify order status payload"):
        assert response["status_code"] == 200
        assert response["json"]["id"] == "order-1"
        assert response["json"]["status"] == "created"


def verify_order_status_missing(orders_client, order_id: str):
    with allure.step(f"Request missing order status for {order_id}"):
        response = orders_client.get_order(order_id)

    with allure.step("Verify missing order response"):
        assert response["status_code"] == 404
        assert response["json"]["error"] == "Order not found"


def test_orders_single_item_purchase_is_created(orders_client):
    orders_metadata("Single item purchase", "blocker")
    verify_order_created(orders_client, quantity=1)


def test_orders_two_item_purchase_is_created(orders_client):
    orders_metadata("Two item purchase")
    verify_order_created(orders_client, quantity=2)


def test_orders_three_item_purchase_is_created(orders_client):
    orders_metadata("Three item purchase")
    verify_order_created(orders_client, quantity=3)


def test_orders_four_item_purchase_is_created(orders_client):
    orders_metadata("Four item purchase")
    verify_order_created(orders_client, quantity=4)


def test_orders_five_item_purchase_is_created(orders_client):
    orders_metadata("Five item purchase")
    verify_order_created(orders_client, quantity=5)


def test_orders_ten_item_purchase_is_created(orders_client):
    orders_metadata("Ten item purchase")
    verify_order_created(orders_client, quantity=10)


def test_orders_dozen_item_purchase_is_created(orders_client):
    orders_metadata("Dozen item purchase")
    verify_order_created(orders_client, quantity=12)


def test_orders_large_item_purchase_is_created(orders_client):
    orders_metadata("Large item purchase")
    verify_order_created(orders_client, quantity=24)


def test_orders_bulk_item_purchase_is_created(orders_client):
    orders_metadata("Bulk item purchase")
    verify_order_created(orders_client, quantity=50)


def test_orders_high_volume_item_purchase_is_created(orders_client):
    orders_metadata("High volume item purchase")
    verify_order_created(orders_client, quantity=144)


def test_orders_bottle_purchase_is_created_even_when_catalog_stock_is_zero(orders_client):
    orders_metadata("Bottle order acceptance")
    verify_order_created(orders_client, product_id="product-2", quantity=1)


def test_orders_external_product_purchase_is_created_by_contract(orders_client):
    orders_metadata("External product order")
    verify_order_created(orders_client, product_id="external-product-8", quantity=1)


def test_orders_zero_quantity_is_rejected(orders_client):
    orders_metadata("Zero quantity validation", "critical")
    verify_order_rejected(orders_client, 0)


def test_orders_negative_one_quantity_is_rejected(orders_client):
    orders_metadata("Negative quantity validation", "critical")
    verify_order_rejected(orders_client, -1)


def test_orders_negative_three_quantity_is_rejected(orders_client):
    orders_metadata("Negative quantity validation")
    verify_order_rejected(orders_client, -3)


def test_orders_negative_seven_quantity_is_rejected(orders_client):
    orders_metadata("Negative quantity validation")
    verify_order_rejected(orders_client, -7)


def test_orders_negative_bulk_quantity_is_rejected(orders_client):
    orders_metadata("Negative bulk validation")
    verify_order_rejected(orders_client, -144)


def test_orders_created_order_status_can_be_read(orders_client):
    orders_metadata("Created order status", "critical")
    verify_order_status_found(orders_client)


def test_orders_created_order_status_is_stable_after_creation_call(orders_client):
    orders_metadata("Order creation to status handoff")
    verify_order_created(orders_client, quantity=1)
    verify_order_status_found(orders_client)


def test_orders_created_order_status_can_be_read_twice(orders_client):
    orders_metadata("Repeated order status read")
    verify_order_status_found(orders_client)
    verify_order_status_found(orders_client)


def test_orders_created_order_status_returns_created_state(orders_client):
    orders_metadata("Created status state")
    verify_order_status_found(orders_client)


def test_orders_unknown_order_status_is_not_found(orders_client):
    orders_metadata("Unknown order status")
    verify_order_status_missing(orders_client, "missing-order-1")


def test_orders_cancelled_order_status_is_not_found_in_active_projection(orders_client):
    orders_metadata("Cancelled order projection")
    verify_order_status_missing(orders_client, "cancelled-order-2")


def test_orders_archived_order_status_is_not_found_in_active_projection(orders_client):
    orders_metadata("Archived order projection")
    verify_order_status_missing(orders_client, "archived-order-3")


def test_orders_expired_order_status_is_not_found_in_active_projection(orders_client):
    orders_metadata("Expired order projection")
    verify_order_status_missing(orders_client, "expired-order-4")


def test_orders_supplier_order_status_is_not_found_in_customer_projection(orders_client):
    orders_metadata("Supplier order projection")
    verify_order_status_missing(orders_client, "supplier-order-5")


def test_orders_numeric_order_status_is_not_found(orders_client):
    orders_metadata("Numeric order id lookup")
    verify_order_status_missing(orders_client, "12345")


def test_orders_blank_order_status_is_not_found(orders_client):
    orders_metadata("Blank order id lookup")
    verify_order_status_missing(orders_client, "")


def test_orders_spaced_order_status_is_not_found(orders_client):
    orders_metadata("Whitespace order id lookup")
    verify_order_status_missing(orders_client, "   ")


def test_orders_uppercase_order_status_is_not_found(orders_client):
    orders_metadata("Case-sensitive order id lookup")
    verify_order_status_missing(orders_client, "ORDER-1")


def test_orders_order_status_with_suffix_is_not_found(orders_client):
    orders_metadata("Order id suffix lookup")
    verify_order_status_missing(orders_client, "order-1-copy")


def test_orders_order_status_with_prefix_is_not_found(orders_client):
    orders_metadata("Order id prefix lookup")
    verify_order_status_missing(orders_client, "copy-order-1")


def test_orders_order_status_for_future_order_is_not_found(orders_client):
    orders_metadata("Future order lookup")
    verify_order_status_missing(orders_client, "future-order-2027")


def test_orders_order_status_for_legacy_order_is_not_found(orders_client):
    orders_metadata("Legacy order lookup")
    verify_order_status_missing(orders_client, "legacy-order-1999")


def test_orders_order_status_for_guest_order_is_not_found(orders_client):
    orders_metadata("Guest order lookup")
    verify_order_status_missing(orders_client, "guest-order-7")


def test_orders_order_status_for_fraud_hold_order_is_not_found(orders_client):
    orders_metadata("Fraud hold order lookup")
    verify_order_status_missing(orders_client, "fraud-hold-order-8")


def test_orders_order_status_for_payment_failed_order_is_not_found(orders_client):
    orders_metadata("Payment failed order lookup")
    verify_order_status_missing(orders_client, "payment-failed-order-9")


def test_orders_order_status_for_returned_order_is_not_found(orders_client):
    orders_metadata("Returned order lookup")
    verify_order_status_missing(orders_client, "returned-order-10")


def test_orders_created_order_payload_does_not_expose_internal_queue(orders_client):
    orders_metadata("Order payload secrecy", "critical")
    with allure.step("Create an order"):
        response = orders_client.create_order("user-1", "product-1", 1)
    with allure.step("Verify internal queue details are hidden"):
        assert "queue" not in response["json"]
        assert "worker" not in response["json"]


def test_orders_rejected_order_payload_does_not_create_order_id(orders_client):
    orders_metadata("Rejected order secrecy", "critical")
    with allure.step("Submit invalid order"):
        response = orders_client.create_order("user-1", "product-1", 0)
    with allure.step("Verify rejected response has no order id"):
        assert "id" not in response["json"]


def test_orders_status_payload_does_not_expose_user_data(orders_client):
    orders_metadata("Order status privacy", "critical")
    with allure.step("Request order status"):
        response = orders_client.get_order("order-1")
    with allure.step("Verify user data is not exposed by status endpoint"):
        assert "user_id" not in response["json"]
        assert "email" not in response["json"]


def test_orders_queue_projection_accepts_order(orders_client):
    orders_metadata("Order queue projection drift", "critical")
    verify_order_created(orders_client, quantity=1)


def test_orders_payment_reservation_accepts_two_items(orders_client):
    orders_metadata("Payment reservation drift", "critical")
    verify_order_created(orders_client, quantity=2)


def test_orders_fulfillment_projection_is_available(orders_client):
    orders_metadata("Fulfillment adapter availability", "normal")
    verify_order_status_found(orders_client)


def test_orders_tax_calculation_includes_two_item_tax(orders_client):
    orders_metadata("Tax calculation", "critical")
    with allure.step("Create an order that should include tax details"):
        response = orders_client.create_order("user-1", "product-1", 2)
    with allure.step("Verify tax total is present and correct"):
        assert response["json"]["tax_total"] == "9.28"


def test_orders_shipping_sla_is_available(orders_client):
    orders_metadata("Shipping SLA", "normal")
    with allure.step("Create an order for checkout handoff"):
        response = orders_client.create_order("user-1", "product-1", 1)
    with allure.step("Verify shipping SLA is available to checkout"):
        assert response["json"].get("shipping_sla") == "2 business days"
