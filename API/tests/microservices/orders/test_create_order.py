import allure


@allure.epic("Demo Shop API")
@allure.feature("Orders Service")
@allure.story("Order creation")
@allure.severity(allure.severity_level.BLOCKER)
@allure.label("layer", "api")
@allure.label("component", "orders-service")
@allure.tag("smoke")
def test_create_order_returns_created_order(orders_client):
    with allure.step("Create an order for an in-stock product"):
        response = orders_client.create_order(
            user_id="user-1",
            product_id="product-1",
            quantity=2,
        )

    with allure.step("Verify the order is accepted"):
        assert response["status_code"] == 201
        assert response["json"]["status"] == "created"


@allure.epic("Demo Shop API")
@allure.feature("Orders Service")
@allure.story("Order creation")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("layer", "api")
@allure.label("component", "orders-service")
def test_create_order_rejects_zero_quantity(orders_client):
    with allure.step("Create an order with zero quantity"):
        response = orders_client.create_order(
            user_id="user-1",
            product_id="product-1",
            quantity=0,
        )

    with allure.step("Verify the orders service rejects the request"):
        assert response["status_code"] == 400
