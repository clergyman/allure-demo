from decimal import Decimal, ROUND_HALF_UP


def price_with_tax(price: Decimal, tax_rate: Decimal) -> Decimal:
    total = price * (Decimal("1") + tax_rate)
    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def apply_discount(price: Decimal, percent: Decimal) -> Decimal:
    if percent < 0 or percent > 100:
        raise ValueError("Discount percent must be between 0 and 100.")

    discounted = price * (Decimal("1") - percent / Decimal("100"))
    return discounted.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

