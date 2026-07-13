from decimal import Decimal, ROUND_HALF_UP

import pytest

from demo_shop.catalog.pricing import apply_discount, price_with_tax
from demo_shop.checkout.cart import Cart, CartItem
from demo_shop.users.permissions import ROLE_PERMISSIONS, can


TAX_CASES = [
    (
        Decimal(f"{10 + index}.{index % 100:02d}"),
        Decimal(f"0.{(index % 25) + 1:02d}"),
    )
    for index in range(175)
]

DISCOUNT_CASES = [
    (
        Decimal(f"{25 + index}.{(index * 3) % 100:02d}"),
        Decimal(str(index % 60)),
    )
    for index in range(160)
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

PERMISSION_CASES = [
    (role, permission, permission in ROLE_PERMISSIONS[role])
    for role in ROLE_PERMISSIONS
    for permission in [
        "catalog:read",
        "cart:write",
        "order:create",
        "product:write",
        "support:read",
        "admin:delete",
    ]
]

UNKNOWN_ROLE_CASES = [
    (f"unknown-role-{index}", "catalog:read") for index in range(20)
]


@pytest.mark.parametrize(("price", "tax_rate"), TAX_CASES)
def test_volume_price_with_tax_matches_formula(price, tax_rate):
    expected = (price * (Decimal("1") + tax_rate)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )

    assert price_with_tax(price, tax_rate) == expected


@pytest.mark.parametrize(("price", "percent"), DISCOUNT_CASES)
def test_volume_apply_discount_matches_formula(price, percent):
    expected = (price * (Decimal("1") - percent / Decimal("100"))).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )

    assert apply_discount(price, percent) == expected


@pytest.mark.parametrize("items", CART_CASES)
def test_volume_cart_subtotal_matches_items(items):
    cart = Cart()

    for item in items:
        cart.add_item(item)

    expected = sum(item.unit_price * item.quantity for item in items)
    assert cart.subtotal() == expected


@pytest.mark.parametrize(("role", "permission", "expected"), PERMISSION_CASES)
def test_volume_role_permissions(role, permission, expected):
    assert can(role, permission) is expected


@pytest.mark.parametrize(("role", "permission"), UNKNOWN_ROLE_CASES)
def test_volume_unknown_roles_have_no_permissions(role, permission):
    assert can(role, permission) is False
