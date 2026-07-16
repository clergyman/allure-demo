from decimal import Decimal

import allure
import pytest

from demo_shop.checkout.cart import Cart, CartItem

pytestmark = [
    allure.label("component", "checkout-cart"),
]

CART_CASES = [
    [
        CartItem(
            sku=f"SKU-{case_index}-{item_index}",
            unit_price=Decimal(f"{item_index + 1}.{case_index % 100:02d}"),
            quantity=(case_index + item_index) % 5 + 1,
        )
        for item_index in range(1, 4)
    ]
    for case_index in range(120)
]


@pytest.mark.parametrize("items", CART_CASES)
def test_cart_subtotal_matches_items(items):
    cart = Cart()

    with allure.step("Add all items to cart"):
        for item in items:
            cart.add_item(item)

    with allure.step("Verify subtotal equals item total"):
        expected = sum(item.unit_price * item.quantity for item in items)
        assert cart.subtotal() == expected
