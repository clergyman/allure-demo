from decimal import Decimal

import pytest

from demo_shop.catalog.pricing import apply_discount, price_with_tax


def test_price_with_tax_rounds_to_two_decimals():
    result = price_with_tax(Decimal("19.99"), Decimal("0.23"))

    assert result == Decimal("24.59")


def test_apply_discount_reduces_price():
    result = apply_discount(Decimal("50.00"), Decimal("10"))

    assert result == Decimal("45.00")


def test_apply_discount_rejects_invalid_percent():
    with pytest.raises(ValueError):
        apply_discount(Decimal("50.00"), Decimal("120"))

