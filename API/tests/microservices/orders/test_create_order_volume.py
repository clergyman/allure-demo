import allure
import pytest

from flaky import maybe_fail


MAIN_FLAKY_PROBABILITY = 0.35

ORDER_CASES = [
    (
        f"order-create-{quantity}",
        "user-1",
        "product-1",
        quantity,
        201 if quantity > 0 else 400,
    )
    for quantity in (
        -7,
        -3,
        -1,
        0,
        1,
        2,
        3,
        4,
        5,
        7,
        8,
        9,
        11,
        12,
        14,
        15,
        18,
        21,
        23,
        24,
        27,
        31,
        32,
        34,
        37,
        41,
        55,
        89,
        144,
    )
]


@allure.epic("Demo Shop")
@allure.feature("Orders")
@allure.story("Order creation volume")
@allure.severity("normal")
@allure.label("layer", "api")
@allure.label("component", "orders-service")
@pytest.mark.parametrize(
    ("case_id", "user_id", "product_id", "quantity", "expected_status"), ORDER_CASES
)
def test_create_order_volume(
    orders_client, case_id, user_id, product_id, quantity, expected_status
):
    with allure.step("Simulate order queue stability"):
        maybe_fail(MAIN_FLAKY_PROBABILITY, "order queue accepted late")

    with allure.step(f"Submit order creation request ({case_id})"):
        response = orders_client.create_order(user_id, product_id, quantity)

    with allure.step("Verify order creation response status"):
        assert response["status_code"] == expected_status
