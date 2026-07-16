from decimal import Decimal

import allure
import pytest

from demo_shop.catalog.pricing import apply_discount, price_with_tax

pytestmark = [
    allure.feature("Catalog"),
    allure.label("component", "catalog-pricing"),
]


def test_price_with_tax_rounds_to_two_decimals():
    with allure.step("Calculate tax-inclusive price"):
        result = price_with_tax(Decimal("19.99"), Decimal("0.23"))

    with allure.step("Verify rounded price"):
        assert result == Decimal("24.59")


def test_apply_discount_reduces_price():
    with allure.step("Apply percentage discount"):
        result = apply_discount(Decimal("50.00"), Decimal("10"))

    with allure.step("Verify discounted price"):
        assert result == Decimal("45.00")


def test_discounted_price_matches_catalog_projection():
    with allure.step("Apply catalog promotion"):
        result = apply_discount(Decimal("80.00"), Decimal("15"))

    with allure.step("Verify catalog projection"):
        assert result == Decimal(
            "66.00"
        ), "Demo stable failure: catalog pricing projection returned stale discount."


def test_apply_discount_rejects_invalid_percent():
    with allure.step("Reject discount above allowed range"):
        with pytest.raises(ValueError):
            apply_discount(Decimal("50.00"), Decimal("120"))
