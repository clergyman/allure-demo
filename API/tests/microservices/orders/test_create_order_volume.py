import allure

from flaky import maybe_fail


MAIN_FLAKY_PROBABILITY = 0.35


@allure.epic("Demo Shop")
@allure.feature("Orders")
@allure.story("Order creation volume")
@allure.severity("normal")
@allure.label("layer", "api")
@allure.label("component", "orders-service")
def test_create_order_accepts_single_backpack_purchase(orders_client):
    with allure.step("Simulate order queue stability"):
        maybe_fail(MAIN_FLAKY_PROBABILITY, "order queue accepted late")

    with allure.step("Submit an order for one backpack"):
        response = orders_client.create_order("user-1", "product-1", 1)

    with allure.step("Verify order is created with requested quantity"):
        assert response["status_code"] == 201
        assert response["json"]["id"] == "order-1"
        assert response["json"]["quantity"] == 1


@allure.epic("Demo Shop")
@allure.feature("Orders")
@allure.story("Order creation volume")
@allure.severity("normal")
@allure.label("layer", "api")
@allure.label("component", "orders-service")
def test_create_order_accepts_bulk_quantity_for_same_product(orders_client):
    with allure.step("Submit a larger order quantity"):
        response = orders_client.create_order("user-1", "product-1", 12)

    with allure.step("Verify bulk order is accepted"):
        assert response["status_code"] == 201
        assert response["json"]["quantity"] == 12
        assert response["json"]["status"] == "created"


@allure.epic("Demo Shop")
@allure.feature("Orders")
@allure.story("Order creation volume")
@allure.severity("critical")
@allure.label("layer", "api")
@allure.label("component", "orders-service")
def test_create_order_rejects_zero_quantity(orders_client):
    with allure.step("Submit an order with zero quantity"):
        response = orders_client.create_order("user-1", "product-1", 0)

    with allure.step("Verify invalid quantity is rejected"):
        assert response["status_code"] == 400
        assert response["json"]["error"] == "Quantity must be positive"
