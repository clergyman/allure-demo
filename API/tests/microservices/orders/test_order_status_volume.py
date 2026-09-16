import allure

from flaky import maybe_fail


NEIGHBOR_FLAKY_PROBABILITY = 0.08


@allure.epic("Demo Shop")
@allure.feature("Orders")
@allure.story("Order status volume")
@allure.severity("normal")
@allure.label("layer", "api")
@allure.label("component", "orders-service")
def test_order_status_returns_created_state_for_existing_order(orders_client):
    with allure.step("Simulate order projection stability"):
        maybe_fail(NEIGHBOR_FLAKY_PROBABILITY, "order projection not ready")

    with allure.step("Request status for an existing order"):
        response = orders_client.get_order("order-1")

    with allure.step("Verify created order status is returned"):
        assert response["status_code"] == 200
        assert response["json"] == {"id": "order-1", "status": "created"}


@allure.epic("Demo Shop")
@allure.feature("Orders")
@allure.story("Order status volume")
@allure.severity("normal")
@allure.label("layer", "api")
@allure.label("component", "orders-service")
def test_order_status_returns_not_found_for_missing_order(orders_client):
    with allure.step("Request status for a missing order"):
        response = orders_client.get_order("missing-order-23")

    with allure.step("Verify missing order response"):
        assert response["status_code"] == 404
        assert response["json"]["error"] == "Order not found"


@allure.epic("Demo Shop")
@allure.feature("Orders")
@allure.story("Order status volume")
@allure.severity("minor")
@allure.label("layer", "api")
@allure.label("component", "orders-service")
def test_order_status_returns_not_found_for_expired_projection(orders_client):
    with allure.step("Request status for an expired projection id"):
        response = orders_client.get_order("archived-order-88")

    with allure.step("Verify expired projection is not exposed as active"):
        assert response["status_code"] == 404
        assert response["json"]["error"] == "Order not found"
