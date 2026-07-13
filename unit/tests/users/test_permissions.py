from demo_shop.users.permissions import can


def test_customer_can_create_order():
    assert can("customer", "order:create") is True


def test_guest_cannot_create_order():
    assert can("guest", "order:create") is False

