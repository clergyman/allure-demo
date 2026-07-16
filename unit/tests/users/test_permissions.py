import allure

from demo_shop.users.permissions import can

pytestmark = [
    allure.label("component", "user-permissions"),
]


def test_customer_can_create_order():
    with allure.step("Check customer order creation permission"):
        assert can("customer", "order:create") is True


def test_guest_cannot_create_order():
    with allure.step("Check guest order creation permission"):
        assert can("guest", "order:create") is False
