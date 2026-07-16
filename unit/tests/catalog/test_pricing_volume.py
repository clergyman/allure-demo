from decimal import Decimal, ROUND_HALF_UP

import allure
import pytest

from demo_shop.catalog.pricing import apply_discount, price_with_tax

pytestmark = [
    allure.label("component", "catalog-pricing"),
]

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


@pytest.mark.parametrize(("price", "tax_rate"), TAX_CASES)
def test_price_with_tax_matches_formula(price, tax_rate):
    with allure.step("Calculate expected tax-inclusive price"):
        expected = (price * (Decimal("1") + tax_rate)).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

    with allure.step("Verify pricing calculation"):
        assert price_with_tax(price, tax_rate) == expected


@pytest.mark.parametrize(("price", "percent"), DISCOUNT_CASES)
def test_apply_discount_matches_formula(price, percent):
    with allure.step("Calculate expected discounted price"):
        expected = (price * (Decimal("1") - percent / Decimal("100"))).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

    with allure.step("Verify discount calculation"):
        assert apply_discount(price, percent) == expected
