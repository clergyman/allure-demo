import allure


@allure.epic("Demo Shop API")
@allure.feature("Orders Service")
@allure.story("Order status")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("layer", "api")
@allure.label("component", "orders-service")
def test_get_order_returns_status(orders_client):
    with allure.step("Request an existing order by id"):
        response = orders_client.get_order("order-1")

    with allure.step("Verify the order status is returned"):
        assert response["status_code"] == 200
        assert response["json"]["status"] == "created"


@allure.epic("Demo Shop API")
@allure.feature("Orders Service")
@allure.story("Order status")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("layer", "api")
@allure.label("component", "orders-service")
def test_get_order_returns_not_found_for_unknown_order(orders_client):
    with allure.step("Request a missing order by id"):
        response = orders_client.get_order("missing-order")

    with allure.step("Verify the orders service returns not found"):
        assert response["status_code"] == 404
