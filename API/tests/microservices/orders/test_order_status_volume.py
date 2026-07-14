import allure
import pytest

from flaky import maybe_fail


NEIGHBOR_FLAKY_PROBABILITY = 0.08

ORDER_STATUS_CASES = [
    ("order-status-existing", "order-1", 200),
    *[
        (f"order-status-missing-{index}", f"missing-order-{index}", 404)
        for index in (1, 2, 4, 7, 11, 16, 23, 31, 46, 58, 73, 88)
    ],
]


@allure.epic("Demo Shop API")
@allure.feature("Orders Service")
@allure.story("Order status volume")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("layer", "api")
@allure.label("component", "orders-service")
@pytest.mark.parametrize(("case_id", "order_id", "expected_status"), ORDER_STATUS_CASES)
def test_order_status_volume(orders_client, case_id, order_id, expected_status):
    with allure.step("Simulate order projection stability"):
        maybe_fail(NEIGHBOR_FLAKY_PROBABILITY, "order projection not ready")

    with allure.step(f"Request order status for {order_id} ({case_id})"):
        response = orders_client.get_order(order_id)

    with allure.step("Verify order status response"):
        assert response["status_code"] == expected_status
