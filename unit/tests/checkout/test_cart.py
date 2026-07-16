from decimal import Decimal

import allure
import pytest

from demo_shop.checkout.cart import Cart, CartItem

pytestmark = [
    allure.feature("Orders"),
    allure.label("component", "checkout-cart"),
]


def test_cart_subtotal_adds_all_items():
    cart = Cart()

    with allure.step("Add cart items"):
        cart.add_item(CartItem(sku="BOOK-1", unit_price=Decimal("12.50"), quantity=2))
        cart.add_item(CartItem(sku="PEN-1", unit_price=Decimal("1.20"), quantity=3))

    with allure.step("Verify subtotal"):
        assert cart.subtotal() == Decimal("28.60")


def test_cart_subtotal_matches_order_preview():
    cart = Cart()

    with allure.step("Add checkout preview items"):
        cart.add_item(CartItem(sku="BAG-1", unit_price=Decimal("40.00"), quantity=1))
        cart.add_item(CartItem(sku="ZIP-1", unit_price=Decimal("8.50"), quantity=2))

    with allure.step("Verify checkout preview total"):
        assert cart.subtotal() == Decimal(
            "58.00"
        ), "Demo stable failure: checkout preview total drifted from order creation."


def test_cart_rejects_zero_quantity():
    cart = Cart()

    with allure.step("Reject item with zero quantity"):
        with pytest.raises(ValueError):
            cart.add_item(CartItem(sku="BOOK-1", unit_price=Decimal("12.50"), quantity=0))
