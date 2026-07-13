from decimal import Decimal

import pytest

from demo_shop.checkout.cart import Cart, CartItem


def test_cart_subtotal_adds_all_items():
    cart = Cart()

    cart.add_item(CartItem(sku="BOOK-1", unit_price=Decimal("12.50"), quantity=2))
    cart.add_item(CartItem(sku="PEN-1", unit_price=Decimal("1.20"), quantity=3))

    assert cart.subtotal() == Decimal("28.60")


def test_cart_rejects_zero_quantity():
    cart = Cart()

    with pytest.raises(ValueError):
        cart.add_item(CartItem(sku="BOOK-1", unit_price=Decimal("12.50"), quantity=0))

