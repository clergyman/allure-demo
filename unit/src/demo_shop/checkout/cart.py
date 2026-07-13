from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class CartItem:
    sku: str
    unit_price: Decimal
    quantity: int


class Cart:
    def __init__(self) -> None:
        self._items: list[CartItem] = []

    def add_item(self, item: CartItem) -> None:
        if item.quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        self._items.append(item)

    def subtotal(self) -> Decimal:
        return sum(
            item.unit_price * item.quantity for item in self._items
        ) if self._items else Decimal("0.00")

